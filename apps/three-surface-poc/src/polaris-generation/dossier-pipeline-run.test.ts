import { createHash } from 'node:crypto';
import { existsSync, readdirSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { DECISIONS_DIR, EGRESS_V2_INSTANCE, INSTANCES_DIR, POLICY_PATH } from '@syzygy/polaris-generation-consent';
import { renderPolicyAct, renderRecorderAct } from '@syzygy/polaris-generation-consent/testing';
import { createMessagesApiGenerate } from '@syzygy/polaris-generation-provider';
import { LOOPBACK_FOR_TESTS } from '@syzygy/polaris-generation-provider/testing';

import { DOSSIER_REQUESTED_ASSETS, promptForStage, type PromptStage } from '@syzygy/polaris-generation-core';

import { main } from './dossier-main.js';
import { fixturePolicyActPort, fixtureRouteRoot } from './dossier-fixtures.testkit.js';
import type { ProviderFactory } from './dossier-generation.js';
import { EGRESS_V2_DIGEST } from './dossier-stage-authority.js';
import { startStubProvider } from './stub-provider.testkit.js';

let repo = '', commit = '';
beforeAll(() => {
  repo = mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-repo-'));
  const run = (...a: string[]): string => execFileSync('git', ['-C', repo, ...a], { encoding: 'utf8' }).trim();
  run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
  for (const [p, body] of Object.entries({ 'README.md': '# Fixture\nIt does a thing.\n', 'src/core.c': 'int core(void) { return 1; }\n' })) {
    mkdirSync(path.dirname(path.join(repo, p)), { recursive: true }); writeFileSync(path.join(repo, p), body);
  }
  run('add', '-A'); run('commit', '-qm', 'fixture'); commit = run('rev-parse', 'HEAD');
});
afterAll(() => rmSync(repo, { recursive: true, force: true }));


const REPO_ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../../../..');
const hex = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

/** A scratch Syzygy root in which the redis observation record (pinned to the fixture commit) and the real egress version 2 record are
 * in force by the recorders' own acts, plus the route's registry act. Nothing here is the repository's own decisions directory. */
function admissionRoot(route: 'messages-api'): string {
  const root = fixtureRouteRoot(route);
  const put = (rel: string, body: string): void => { mkdirSync(path.dirname(path.join(root, rel)), { recursive: true }); writeFileSync(path.join(root, rel), body); };
  const realObs = readFileSync(path.join(REPO_ROOT, INSTANCES_DIR, 'redis/OBSERVATION-CONSENT.md'), 'utf8');
  const obs = realObs.replace(/^\| `([^`\n]+)` \| `[0-9a-f]+` \|$/gm, (_m, label: string) => `| \`${label}\` | \`${commit}\` |`);
  const v2 = readFileSync(path.join(REPO_ROOT, EGRESS_V2_INSTANCE), 'utf8');
  put(`${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`, obs);
  put(EGRESS_V2_INSTANCE, v2);
  put(`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`, renderRecorderAct('redis-observation', hex(obs), '2026-09-01', '2026-09-01T09:30:00Z'));
  put(`${DECISIONS_DIR}/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md`, renderRecorderAct('egress-anthropic-v2', hex(v2), '2026-09-01', '2026-09-01T09:30:00Z'));
  const policy = `${JSON.stringify({ policyVersion: '1.2.0-public-source-candidate.1', publicSourceScope: { rules: [] } }, null, 1)}\n`;
  put(POLICY_PATH, policy);
  put(`${DECISIONS_DIR}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`, renderPolicyAct(hex(policy), '2026-09-01', '2026-09-01T09:30:00Z'));
  return root;
}

const loopback = (url: string): ProviderFactory => build => createMessagesApiGenerate({ model: build.profile.model, apiKey: build.apiKey, upstream: { url, loopbackForTests: LOOPBACK_FOR_TESTS },
  permitted: build.permitted, effort: build.profile.effort, thinking: build.profile.thinking, maxOutputTokens: build.profile.maxOutputTokens });

type Json = Record<string, any>;   // eslint-disable-line @typescript-eslint/no-explicit-any

/** A well-formed reply for each stage, computed from the request's own inputs: every source cited, every requested asset produced. */
function replyFor(system: string, input: string): string {
  const stage = (['inventory', 'plan', 'author', 'edit', 'repair', 'fidelity', 'discovery-map', 'discovery-reduce'] as const).find(s => promptForStage(s).system === system) as PromptStage;
  const inputs: Json = (JSON.parse(input) as Json).inputs;
  if (stage === 'discovery-map') return JSON.stringify({ claims: inputs.items.map((item: Json) => ({ blobId: item.blobId, claim: 'Relevant to the reader questions.', relevance: 5 })) });
  if (stage === 'discovery-reduce') return JSON.stringify({ ranked: inputs.subsystems.flatMap((s: Json) => s.claims.map((c: Json) => c.blobId)).filter((id: string, i: number, all: string[]) => all.indexOf(id) === i).slice(0, inputs.maxSelected) });
  const sources: string[] = inputs.sources.map((s: Json) => s.sourceId);
  const sections: Json[] = DOSSIER_REQUESTED_ASSETS.filter(a => a.kind === 'section') as unknown as Json[];
  const produced = (id: string) => ({ kind: 'produced', assetIds: [id] });
  if (stage === 'inventory') {
    return JSON.stringify({ entries: sources.map((id, i) => ({ id: `entry-${i}`, sourceIds: [id], statement: `Source ${i} states a purpose.`, kind: 'purpose', disposition: produced('core-ideas') })) });
  }
  if (stage === 'plan') {
    return JSON.stringify({ sections: sections.map(s => ({ id: s.id, title: s.id, reason: 'A reader question asks for it.', sourceIds: sources, disposition: produced(s.id) })) });
  }
  const block = (id: string, text: string) => ({ id, text, sourceIds: sources, children: [] });
  if (stage === 'fidelity') {
    const draft: Json = inputs.draft;
    const blocks: Json[] = [draft.introduction, ...draft.sections.flatMap((s: Json) => s.paragraphs.flatMap((b: Json) => [b, ...b.children])),
      ...draft.diagrams.flatMap((d: Json) => [...d.nodes, ...d.edges]), ...draft.deepDives.flatMap((d: Json) => d.paragraphs.flatMap((b: Json) => [b, ...b.children]))];
    return JSON.stringify({
      inventoryCoverage: inputs.inventory.entries.map((e: Json) => ({ entryId: e.id, disposition: 'represented', blockIds: ['intro'], reason: 'The introduction states it.' })),
      blockSupport: blocks.map(b => ({ blockId: b.id, verdict: 'supported', sourceIds: b.sourceIds, reason: 'The cited span states it.' })), findings: [],
    });
  }
  return JSON.stringify({
    title: 'Fixture dossier', introduction: { id: 'intro', text: 'The project does a thing.', sourceIds: sources },
    sections: sections.map(s => ({ id: s.id, title: s.id, paragraphs: [block(`${s.id}-p`, `Input supplies the output for ${s.id}.`)], disposition: produced(s.id) })),
    diagrams: [{ id: 'workflow-diagram', title: 'Workflow', sectionId: 'end-to-end-workflows', kind: 'flow', relationship: 'How input becomes output', disposition: produced('workflow-diagram'),
      nodes: [{ id: 'n1', label: 'input', sourceIds: sources, epistemic: 'observed' }, { id: 'n2', label: 'output', sourceIds: sources, epistemic: 'observed' }],
      edges: [{ id: 'e1', from: 'n1', to: 'n2', label: 'supplies', sourceIds: sources, epistemic: 'observed' }] }],
    deepDives: [{ id: 'mechanism-deep-dive', title: 'Mechanism', sectionId: 'mechanisms', paragraphs: [block('deep-p', 'The mechanism is a function.')], disposition: produced('mechanism-deep-dive') }],
    unresolved: [],
  });
}

const KEY = 'sk-test-pipeline-0123456789';
const walk = (dir: string): string[] => readdirSync(dir).flatMap(e => { const f = path.join(dir, e); return statSync(f).isDirectory() ? walk(f) : [f]; });
const stageOf = (system: string): string => (['inventory', 'plan', 'author', 'edit', 'repair', 'fidelity', 'discovery-map', 'discovery-reduce'] as const).find(s => promptForStage(s).system === system) ?? 'unknown';

describe('a whole run through the wiring against the loopback stub', () => {
  const run = async (respond: (system: string, input: string, n: number) => string, env: Record<string, string | undefined> = { SYZYGY_POLARIS_PROVIDER_API_KEY: KEY }) => {
    const stub = await startStubProvider((request, n) => ({ text: respond(request.system, request.input, n) }));
    const out: string[] = [];
    const dir = mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-out-'));
    const runDir = path.join(dir, 'run');
    const code = await main(['https://github.com/redis/redis', '--route', 'messages-api', '--out', runDir, '--json'], { lsRemote: () => `${commit}\tHEAD\n`, materialize: async () => repo, policyAct: fixturePolicyActPort() },
      { root: admissionRoot('messages-api'), env, providerFactory: loopback(stub.url), stdout: t => out.push(t), stderr: t => out.push(t) });
    await stub.close();
    return { code, env, runDir, stateDir: `${runDir}.state`, requests: stub.requests, outcome: JSON.parse(out.join('')) as { state: string; detail: string } };
  };

  it('discovers, runs all five narrative stages, renders the dossier with its optional assets, and stays inside the budget', async () => {
    const r = await run(replyFor);
    expect(r.code).toBe(0);
    expect(r.outcome).toMatchObject({ state: 'complete' });
    expect('SYZYGY_POLARIS_PROVIDER_API_KEY' in r.env).toBe(false);   // read once, then removed from the environment
    expect(r.requests.map(q => stageOf(q.system))).toEqual(['discovery-map', 'discovery-reduce', 'inventory', 'plan', 'author', 'edit', 'fidelity']);
    const record = JSON.parse(readFileSync(path.join(r.runDir, 'run-record.json'), 'utf8')) as { generation: { accountingPolicy: string; route: string; spend: { discoveryCountedUnits: number; narrativeCountedUnits: number }; budget: { runTotalUnits: number }; calls: { phase: string; usageUnknown: boolean }[] } };
    expect(record.generation).toMatchObject({ accountingPolicy: 'dossier-units-v1', route: 'messages-api', budget: { runTotalUnits: 4000 } });
    expect(record.generation.spend.discoveryCountedUnits).toBeGreaterThan(0);
    expect(record.generation.spend.discoveryCountedUnits).toBeLessThanOrEqual(1000);
    expect(record.generation.spend.narrativeCountedUnits).toBeGreaterThan(0);
    expect(record.generation.spend.narrativeCountedUnits).toBeLessThanOrEqual(3000);
    expect(record.generation.calls.filter(c => c.phase === 'discovery')).toHaveLength(2);
    expect(record.generation.calls.every(c => !c.usageUnknown)).toBe(true);
    const files = walk(r.runDir).map(f => path.relative(r.runDir, f));
    expect(files).toContain('index.html');
    expect(files).toContain('run-record.json');
    const pages = files.filter(f => f.endsWith('.html')).map(f => readFileSync(path.join(r.runDir, f), 'utf8')).join('\n');
    expect(files).toContain('deep-dives/mechanism-deep-dive.html');
    expect(pages).toContain('<figure><figcaption>Workflow</figcaption>');   // the optional diagram, rendered from the requested asset
    if (process.env.SYZYGY_PIPELINE_EVIDENCE) {
      const sha = (f: string): string => createHash('sha256').update(readFileSync(path.join(r.runDir, f))).digest('hex');
      writeFileSync(process.env.SYZYGY_PIPELINE_EVIDENCE, `${JSON.stringify({
        subject: 'poc:dossier wiring (dossier-main.ts through dossier-generation.ts) run against a loopback stub provider on route messages-api',
        testFile: { path: 'apps/three-surface-poc/src/polaris-generation/dossier-pipeline-run.test.ts', sha256: createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex') },
        providerCallPerformed: false, note: 'every request went to a 127.0.0.1 stub through the egress gate; the repository is a two-file synthetic fixture; the records are the real recorders\' acts over the real egress version 2 bytes in a scratch root',
        exitCode: r.code, outcome: r.outcome, stagesRequested: r.requests.map(q => stageOf(q.system)),
        generation: record.generation, files: files.filter(f => f !== 'run-record.json').map(f => ({ path: f, sha256: sha(f), bytes: statSync(path.join(r.runDir, f)).size })),
      }, null, 2)}\n`);
    }
  }, 60_000);

  it('never writes the credential into the run directory or the state directory, and never sends it in a body', async () => {
    const r = await run(replyFor);
    for (const file of [...walk(r.runDir), ...walk(r.stateDir)]) expect(readFileSync(file, 'utf8'), file).not.toContain(KEY);
    for (const q of r.requests) expect(q.raw).not.toContain(KEY);
    expect(existsSync(r.stateDir)).toBe(true);
  }, 60_000);

  it('with no credential stops before anything is fetched or sent', async () => {
    const r = await run(replyFor, {});
    expect(r.code).toBe(5);
    expect(r.requests).toHaveLength(0);
    expect(existsSync(r.runDir)).toBe(false);
  }, 60_000);

  it('a reply that fails validation stops the run and the stages after it are never requested', async () => {
    const r = await run((system, input, n) => (stageOf(system) === 'plan' ? '{}' : replyFor(system, input)));
    expect(r.code).toBe(7);   // the inventory finished before the plan failed: a partial render, not nothing
    expect(r.requests.map(q => stageOf(q.system)).filter(s => s === 'author' || s === 'edit' || s === 'fidelity')).toEqual([]);
  }, 60_000);

  it('with every reply costing exactly its permit the whole run still lands inside the budget, and each call is held to its stage ceiling', async () => {
    const units = (system: string): number => ({ 'discovery-map': 40, 'discovery-reduce': 40, inventory: 600, plan: 300, author: 600, edit: 600, fidelity: 300, repair: 300 } as Record<string, number>)[stageOf(system)]!;
    const stub = await startStubProvider(request => ({ text: replyFor(request.system, request.input), inputTokens: 1000, outputTokens: (units(request.system) - 1) * 1000 }));
    const dir = mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-out-'));
    const runDir = path.join(dir, 'run');
    const code = await main(['https://github.com/redis/redis', '--route', 'messages-api', '--out', runDir, '--json'], { lsRemote: () => `${commit}\tHEAD\n`, materialize: async () => repo, policyAct: fixturePolicyActPort() },
      { root: admissionRoot('messages-api'), env: { SYZYGY_POLARIS_PROVIDER_API_KEY: KEY }, providerFactory: loopback(stub.url), stdout: () => undefined, stderr: () => undefined });
    await stub.close();
    const spend = (JSON.parse(readFileSync(path.join(runDir, 'run-record.json'), 'utf8')) as { generation: { spend: { discoveryCountedUnits: number; narrativeCountedUnits: number } } }).generation.spend;
    expect(code).toBe(0);
    expect(spend).toEqual({ discoveryCountedUnits: 80, narrativeCountedUnits: 600 + 300 + 600 + 600 + 300 });
    expect(spend.discoveryCountedUnits + spend.narrativeCountedUnits).toBeLessThanOrEqual(4000);
    // the output cap the adapter sent never let one call past its ceiling
    for (const q of stub.requests) expect(q.maxTokens).toBeLessThanOrEqual(units(q.system) * 1000);
  }, 60_000);

  it('a route with no act in force refuses before anything is fetched, read or sent', async () => {
    const stub = await startStubProvider(() => ({ text: '{}' }));
    const fetched: string[] = [];
    const out: string[] = [];
    const runDir = path.join(mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-out-')), 'run');
    const code = await main(['https://github.com/redis/redis', '--route', 'messages-api', '--out', runDir], { lsRemote: () => { fetched.push('ls'); return `${commit}\tHEAD\n`; }, materialize: async () => { fetched.push('checkout'); return repo; }, policyAct: fixturePolicyActPort() },
      { root: fixtureRouteRoot('messages-api', { skipAct: true }), env: { SYZYGY_POLARIS_PROVIDER_API_KEY: KEY }, providerFactory: loopback(stub.url), stdout: t => out.push(t), stderr: t => out.push(t) });
    await stub.close();
    expect(code).toBe(5);
    expect(out.join('')).toContain('provider route is not in force');
    expect(fetched).toEqual([]);
    expect(stub.requests).toHaveLength(0);
    expect(existsSync(runDir)).toBe(false);
  });

  it('withdrawing the observation consent mid-run stops the next stage: it is never requested', async () => {
    const root = admissionRoot('messages-api');
    const instance = path.join(root, INSTANCES_DIR, 'redis/OBSERVATION-CONSENT.md');
    const stub = await startStubProvider((request, n) => {
      if (stageOf(request.system) === 'inventory') writeFileSync(instance, `${readFileSync(instance, 'utf8')}\nedited after the act\n`);   // the act no longer binds these bytes
      return { text: replyFor(request.system, request.input) };
    });
    const runDir = path.join(mkdtempSync(path.join(tmpdir(), 'syzygy-pipeline-out-')), 'run');
    const code = await main(['https://github.com/redis/redis', '--route', 'messages-api', '--out', runDir, '--json'], { lsRemote: () => `${commit}\tHEAD\n`, materialize: async () => repo, policyAct: fixturePolicyActPort() },
      { root, env: { SYZYGY_POLARIS_PROVIDER_API_KEY: KEY }, providerFactory: loopback(stub.url), stdout: () => undefined, stderr: () => undefined });
    await stub.close();
    expect(stub.requests.map(q => stageOf(q.system))).toEqual(['discovery-map', 'discovery-reduce', 'inventory']);
    expect(code).toBe(7);
  }, 60_000);
});
