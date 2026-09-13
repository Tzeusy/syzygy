import { afterEach, describe, expect, it, vi } from 'vitest';
import { runGenerationPipeline, type PipelinePorts, type PipelineRequest, type ProviderReply } from './pipeline.js';

const request = (): PipelineRequest => ({
  requestId: 'request-1', projectId: 'project-a', snapshotId: 'snapshot-1', providerRoute: 'synthetic', startedAt: Date.now(),
  budget: { maxCalls: 10, maxInputBytes: 200_000, maxOutputBytes: 20_000, maxUsageUnits: 100, maxElapsedMs: 10_000, maxRepairCycles: 1, accountingPolicy: 'synthetic-units-v1' },
  sources: [{ id: 'purpose', text: 'Reduce recurring mental labor.' }], readerQuestions: ['Why does this project exist?'],
});

function harness() {
  const sends: { stage: string; input: string }[] = [];
  const outcomes: string[] = [];
  const late: unknown[] = [];
  const admitted = new Set<string>();
  const ports: PipelinePorts = {
    now: () => Date.now(), verifySources: async () => true,
    admit: async input => {
      const id = `${input.requestId}:${input.ordinal}`;
      if (admitted.has(id)) return null;
      admitted.add(id);
      return { attemptId: id, maxUsageUnits: 5, maxOutputBytes: 1000 };
    },
    permitted: async () => true, releaseUnsent: async () => undefined,
    responseSchema: stage => ({ version: 'test-record-v1', schema: { type: 'object', properties: { stage: { const: stage } }, required: ['stage'], additionalProperties: false } }),
    generate: async input => { sends.push(input); return { body: JSON.stringify({ stage: input.stage }), model: 'synthetic-v1', usageUnits: 1 }; },
    validate: (stage, data) => {
      if (!data || typeof data !== 'object' || Object.keys(data).length !== 1 || (data as { stage?: unknown }).stage !== stage) throw Error('schema');
      return data;
    },
    record: async (_, outcome) => { outcomes.push(outcome.kind); },
    lateReceipt: async (_, receipt) => { late.push(receipt); },
    fidelity: () => ({ blocking: false, findings: [] }),
  };
  return { ports, sends, outcomes, late };
}
const signal = () => new AbortController().signal;
afterEach(() => vi.useRealTimers());

describe('source to editorial draft pipeline', () => {
  it('executes independent inventory, planning, authoring, editing and source review with bound recipes', async () => {
    const h = harness();
    const result = await runGenerationPipeline(request(), h.ports, signal());
    expect(result.status).toBe('awaiting-rendered-review');
    expect(h.sends.map(x => x.stage)).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity']);
    const inventory = JSON.parse(h.sends[0]!.input);
    expect(Object.keys(inventory.inputs).sort()).toEqual(['readerQuestions', 'sources']);
    expect(inventory.responseSchemaVersion).toBe('test-record-v1');
    const fidelity = JSON.parse(h.sends[4]!.input).inputs;
    expect(fidelity.sources).toEqual(request().sources);
    expect(fidelity.inventory).toEqual({ stage: 'inventory' });
    expect(fidelity.draft).toEqual({ stage: 'edit' });
    expect(result.receipts).toHaveLength(5);
    expect(h.outcomes).toEqual(Array(5).fill('validated'));
  });

  it('repairs named findings then independently re-reviews, without treating source review as rendered readiness', async () => {
    const h = harness();
    let reviews = 0;
    const ports = { ...h.ports, fidelity: () => ({ blocking: ++reviews === 1, findings: ['unsupported edge'] }) };
    const result = await runGenerationPipeline(request(), ports, signal());
    expect(result.status).toBe('awaiting-rendered-review');
    expect(h.sends.map(x => x.stage)).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair', 'fidelity']);
    expect(JSON.parse(h.sends[5]!.input).inputs.findings).toEqual(['unsupported edge']);
  });

  it('refuses source failure, duplicate admissions and absent effect permission without sending', async () => {
    for (const field of ['verifySources', 'permitted'] as const) {
      const h = harness();
      const ports = { ...h.ports, [field]: async () => false };
      expect((await runGenerationPipeline(request(), ports, signal())).status).toBe('stopped');
      expect(h.sends).toHaveLength(0);
    }
    const h = harness(); const r = request();
    await runGenerationPipeline(r, h.ports, signal());
    expect(await runGenerationPipeline(r, h.ports, signal())).toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    expect(h.sends).toHaveLength(5);
  });

  it('rejects duplicate-key output before schema validation and never records its body', async () => {
    const h = harness();
    const validate = vi.fn(h.ports.validate);
    const ports = { ...h.ports, validate, generate: async () => ({ body: '{"stage":"inventory","stage":"injected"}', model: null, usageUnits: 1 }) };
    expect(await runGenerationPipeline(request(), ports, signal())).toMatchObject({ status: 'stopped', reason: 'invalid-output' });
    expect(validate).not.toHaveBeenCalled();
    expect(h.outcomes).toEqual(['invalid-output']);
  });

  it('stops when calls or repairs are exhausted and when usage is unknown', async () => {
    const h = harness(); const r = request();
    expect(await runGenerationPipeline({ ...r, budget: { ...r.budget, maxCalls: 2 } }, h.ports, signal())).toMatchObject({ reason: 'budget-exhausted' });
    expect(h.sends).toHaveLength(2);
    // A stopped run retains only previously validated stages for inspection.
    const partial = await runGenerationPipeline({ ...r, requestId: 'partial', budget: { ...r.budget, maxCalls: 2 } }, harness().ports, signal());
    expect(partial.artifacts.map(a => a.stage)).toEqual(['inventory', 'plan']);
    const h2 = harness();
    expect(await runGenerationPipeline({ ...r, budget: { ...r.budget, maxRepairCycles: 0 } }, { ...h2.ports, fidelity: () => ({ blocking: true, findings: [] }) }, signal())).toMatchObject({ reason: 'repair-exhausted' });
    const h3 = harness();
    expect(await runGenerationPipeline(r, { ...h3.ports, generate: async () => ({ body: '{}', model: null, usageUnits: null }) }, signal())).toMatchObject({ reason: 'usage-uncertain' });
  });

  it('cancellation during permission evaluation prevents dispatch', async () => {
    const h = harness(); const c = new AbortController();
    const release = vi.fn(async () => undefined);
    const result = await runGenerationPipeline(request(), { ...h.ports, releaseUnsent: release, permitted: async () => { c.abort(); return true; } }, c.signal);
    expect(result).toMatchObject({ status: 'stopped', reason: 'cancelled' });
    expect(h.sends).toHaveLength(0);
  });

  it.each(['verifySources', 'admit', 'permitted', 'record'] as const)('deadline bounds a stalled %s adapter', async field => {
    vi.useFakeTimers();
    const h = harness(); const r = request();
    const pending = runGenerationPipeline(r, { ...h.ports, [field]: () => new Promise(() => undefined) }, signal());
    await vi.advanceTimersByTimeAsync(r.budget.maxElapsedMs);
    expect(await pending).toMatchObject({ status: 'stopped', reason: 'deadline' });
  });

  it('dispatches the exact schema bound before asynchronous admission', async () => {
    const h = harness();
    const schema = { type: 'object', title: 'original' };
    const seen: unknown[] = [];
    const result = await runGenerationPipeline(request(), {
      ...h.ports,
      responseSchema: () => ({ version: 'fixture-v1', schema }),
      admit: async input => { schema.title = 'changed'; return h.ports.admit(input); },
      generate: async input => { seen.push(input.responseSchema); return h.ports.generate(input); },
    }, signal());
    expect(result.status).toBe('awaiting-rendered-review');
    expect(seen[0]).toEqual({ type: 'object', title: 'original' });
  });

  it('retains late usage capture even when recording the interruption fails', async () => {
    const h = harness(); const c = new AbortController();
    let complete!: (r: ProviderReply) => void;
    let started!: () => void;
    const start = new Promise<void>(resolve => { started = resolve; });
    const pending = runGenerationPipeline(request(), {
      ...h.ports,
      generate: () => { started(); return new Promise(resolve => { complete = resolve; }); },
      record: async () => { throw Error('recorder unavailable'); },
    }, c.signal);
    await start; c.abort();
    expect((await pending).status).toBe('stopped');
    complete({ body: '{}', model: 'late-model', usageUnits: 2 });
    await new Promise(resolve => setTimeout(resolve, 0));
    expect(h.late).toEqual([{ model: 'late-model', usageUnits: 2 }]);
  });
});
