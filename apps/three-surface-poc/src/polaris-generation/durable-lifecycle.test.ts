import { mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { runGenerationPipeline, type PipelineRequest } from '@syzygy/polaris-generation-core';

import { createDurableScriptedLifecycle } from './durable-lifecycle.js';
import { syntheticGenerationSource } from './synthetic-source.js';

const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });
const scratch = (): string => { const path = mkdtempSync(join(tmpdir(), 'syzygy-generator-lifecycle-')); cleanups.push(path); return path; };
const request = (): PipelineRequest => ({
  requestId: 'run-one', projectId: 'project-one', snapshotId: 'snapshot-one', startedAt: Date.now(),
  routes: { inventory: 'route-inventory', plan: 'route-plan', author: 'route-author', edit: 'route-edit', fidelity: 'route-fidelity', repair: 'route-repair' },
  sources: [syntheticGenerationSource('project-one', 'a'.repeat(40), 'purpose', 'The declared purpose.')],
  readerQuestions: ['Why does it exist?'], requestedAssets: [],
  budget: { maxCalls: 7, maxInputBytes: 100_000, maxOutputBytes: 100_000, maxUsageUnits: 100,
    maxElapsedMs: 30_000, maxRepairCycles: 1, accountingPolicy: 'synthetic-units' },
});

function fixture(stateDir: string, sends: string[], options: { readonly failFidelitySchema?: boolean; readonly permission?: () => string; readonly generate?: (stage: string) => Promise<void> } = {}) {
  return createDurableScriptedLifecycle({ stateDir, permissionIdentity: async () => options.permission?.() ?? 'effective-permission-v1',
    verifySources: async () => true, permitted: async () => true,
    responseSchema: stage => { if (stage === 'fidelity' && options.failFidelitySchema) throw new Error('scripted reviewer unavailable');
      return { version: 'fixture-schema-v1', schema: { stage } }; },
    validate: (stage, value) => { if ((value as { stage?: unknown }).stage !== stage) throw new Error('schema'); return value; },
    fidelity: () => ({ blocking: false, findings: [] }),
    scriptedGenerate: async input => { sends.push(input.stage); await options.generate?.(input.stage);
      return { body: JSON.stringify({ stage: input.stage }), model: 'scripted-v1', usageUnits: 1 }; },
  });
}

describe('durable scripted lifecycle port', () => {
  it('reuses four verified checkpoints and sends only the missing fidelity stage after restart', async () => {
    const stateDir = scratch();
    const sends: string[] = [];
    const input = request();
    const first = await runGenerationPipeline(input, fixture(stateDir, sends, { failFidelitySchema: true }), new AbortController().signal);
    expect(first).toMatchObject({ status: 'stopped', reason: 'adapter-failure' });
    expect(sends).toEqual(['inventory', 'plan', 'author', 'edit']);
    const resumed = await runGenerationPipeline(input, fixture(stateDir, sends), new AbortController().signal);
    expect(resumed.status).toBe('awaiting-rendered-review');
    expect(sends).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity']);
    expect(resumed.receipts.map(receipt => receipt.reused)).toEqual([true, true, true, true, false]);
    expect(resumed.receipts.map(receipt => receipt.providerRoute)).toEqual(['route-inventory', 'route-plan', 'route-author', 'route-edit', 'route-fidelity']);
    expect(resumed.receipts.map(receipt => receipt.model)).toEqual(Array(5).fill('scripted-v1'));
  });

  it('refuses changed request, route or current permission and a forged completed artifact', async () => {
    const stateDir = scratch();
    const sends: string[] = [];
    const original = request();
    expect((await runGenerationPipeline(original, fixture(stateDir, sends), new AbortController().signal)).status).toBe('awaiting-rendered-review');
    const wrong = [
      { ...original, projectId: 'another-project' },
      { ...original, snapshotId: 'another-snapshot' },
      { ...original, routes: { ...original.routes, inventory: 'another-route' } },
      { ...original, sources: [syntheticGenerationSource('project-one', 'a'.repeat(40), 'purpose', 'A changed purpose.')] },
    ];
    for (const changed of wrong) expect(await runGenerationPipeline(changed, fixture(stateDir, sends), new AbortController().signal))
      .toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    expect(await runGenerationPipeline(original, fixture(stateDir, sends, { permission: () => 'withdrawn-permission-v2' }), new AbortController().signal))
      .toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    const file = join(stateDir, readdirSync(stateDir).find(name => name.endsWith('.json'))!);
    const entry = JSON.parse(readFileSync(file, 'utf8')) as { outcome: { outputDigest: string } };
    entry.outcome.outputDigest = 'f'.repeat(64);
    writeFileSync(file, JSON.stringify(entry));
    expect(await runGenerationPipeline(original, fixture(stateDir, sends), new AbortController().signal))
      .toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    expect(sends).toHaveLength(5);
  });

  it('keeps uncertain maximum reserved despite missing receipts and an expired lease field', async () => {
    const stateDir = scratch();
    const sends: string[] = [];
    const original = request();
    const first = await runGenerationPipeline(original, fixture(stateDir, sends, { generate: async stage => { if (stage === 'inventory') throw new Error('synthetic transport uncertainty'); } }), new AbortController().signal);
    expect(first).toMatchObject({ status: 'stopped', reason: 'effect-uncertain' });
    expect(sends).toEqual(['inventory']);
    const file = join(stateDir, readdirSync(stateDir).find(name => name.endsWith('.json'))!);
    const entry = JSON.parse(readFileSync(file, 'utf8')) as { state: string; permit: { maxUsageUnits: number; maxOutputBytes: number } } & Record<string, unknown>;
    expect(entry.state).toBe('uncertain');
    expect(entry.permit).toMatchObject({ maxUsageUnits: 5, maxOutputBytes: 10_000 });
    writeFileSync(file, JSON.stringify({ ...entry, late: undefined, leaseExpiresAt: 0 }));
    expect(await runGenerationPipeline(original, fixture(stateDir, sends), new AbortController().signal))
      .toMatchObject({ status: 'stopped', reason: 'effect-uncertain' });
    expect(sends).toHaveLength(1);
  });

  it('admits at most one concurrent dispatch and keeps distinct run artifacts separate', async () => {
    const stateDir = scratch();
    const sends: string[] = [];
    let release!: () => void;
    let started!: () => void;
    const observedStart = new Promise<void>(resolve => { started = resolve; });
    const hold = new Promise<void>(resolve => { release = resolve; });
    const original = request();
    const first = runGenerationPipeline(original, fixture(stateDir, sends, { generate: async stage => { if (stage === 'inventory') { started(); await hold; } } }), new AbortController().signal);
    await observedStart;
    expect(await runGenerationPipeline(original, fixture(stateDir, sends), new AbortController().signal))
      .toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    expect(sends).toEqual(['inventory']);
    release();
    expect((await first).status).toBe('awaiting-rendered-review');
    const another = { ...original, requestId: 'run-two' };
    expect((await runGenerationPipeline(another, fixture(stateDir, sends), new AbortController().signal)).status).toBe('awaiting-rendered-review');
    expect(readdirSync(stateDir).filter(name => name.endsWith('.json'))).toHaveLength(10);
  });
});
