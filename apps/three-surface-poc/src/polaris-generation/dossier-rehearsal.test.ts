import { createHash } from 'node:crypto';
import { cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { afterAll, describe, expect, it } from 'vitest';

import { promptForStage } from '@syzygy/polaris-generation-core';

import { openGeneration } from './dossier-generation.js';
import type { GenerationOpenContext } from './dossier-trigger.js';

import { main } from './dossier-rehearsal-main.testkit.js';
import { CREDENTIAL, REHEARSAL_FORMAT, SCENARIOS, SCENARIO_NAMES, STUB_KEY, buildFixture, evaluatePages, formatRehearsal, inspectSite, recordChecks, rehearse, runScenario, stageOfSystem, type Ran, type RehearsalReport } from './dossier-rehearsal.testkit.js';

const sha = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const scratch: string[] = [];
afterAll(() => { for (const dir of scratch) rmSync(dir, { recursive: true, force: true }); });
const tmp = (): string => { const dir = mkdtempSync(path.join(tmpdir(), 'syzygy-rehearsal-test-')); scratch.push(dir); return dir; };

describe('the rehearsal over every scenario', () => {
  let report: RehearsalReport;
  it('runs, model-free and network-free, and names what each scenario proved', async () => {
    report = await rehearse();
    expect(report).toMatchObject({ format: REHEARSAL_FORMAT, providerCallPerformed: false, network: 'loopback stub only' });
    expect(report.scenarios.map(s => s.scenario)).toEqual([...SCENARIO_NAMES]);
    expect(report.fixtures.map(f => f.name).sort()).toEqual(['redis-shaped', 'small']);
  }, 120_000);

  it('passes every scenario but the Redis-shaped one, whose fidelity stage cannot carry the selection', () => {
    // [Observed] 2026-10-04, with the 400,000-byte selection cap: the inventory, author and edit requests (about 470 KB) fit their 600-unit ceilings,
    // but the fidelity request carries the same sources against a 300-unit ceiling and is refused as budget-exhausted, so the run stops partial (exit 7).
    // When the fidelity ceiling or what fidelity carries changes, this scenario passes and this test must be updated with it.
    expect(report.scenarios.filter(s => !s.passed).map(s => s.scenario)).toEqual(['complete-redis-shaped']);
    const failed = report.scenarios.find(s => s.scenario === 'complete-redis-shaped')!.checks.filter(c => !c.passed).map(c => c.id);
    expect(failed).toContain('selection-fits-every-source-carrying-stage');
    const redis = report.scenarios.find(s => s.scenario === 'complete-redis-shaped')!;
    expect(redis.exit).toBe(7);
    expect(redis.stagesRequested).toEqual([...Array(10).fill('discovery-map'), 'discovery-reduce', 'inventory', 'plan', 'author', 'edit']);
    expect(redis.checks.find(c => c.id === 'selection-fits-every-source-carrying-stage')!.detail).toContain('fidelity 300');
    expect(report.passed).toBe(false);
  });

  it('exits as the wiring documents for complete, at-ceiling, partial, wall-clock-stopped and each refusal', () => {
    const byName = Object.fromEntries(report.scenarios.map(s => [s.scenario, s.exit]));
    expect(byName).toMatchObject({ 'complete-small': 0, 'at-ceiling': 0, partial: 7, 'wall-clock': 6, 'refused-no-credential': 5, 'refused-no-consent': 3, 'refused-bad-input': 2 });
  });

  it('records, for the complete run, the profile, the dossier prompt digests and the budget it spent', () => {
    const complete = report.scenarios.find(s => s.scenario === 'complete-small')!;
    const ids = complete.checks.map(c => c.id);
    for (const id of ['site-opens', 'pages-evaluate', 'pages-all-claims-labelled', 'record-profile', 'record-prompt-profile', 'record-prompt-digests', 'record-budget', 'record-usage-known', 'credential-consumed']) expect(ids).toContain(id);
    expect(complete.checks.every(c => c.passed)).toBe(true);
    expect(complete.stagesRequested).toEqual(['discovery-map', 'discovery-reduce', 'inventory', 'plan', 'author', 'edit', 'fidelity']);
  });

  it('sends nothing and writes nothing for a refusal, and never checks the repository out', () => {
    for (const name of ['refused-no-credential', 'refused-no-consent', 'refused-bad-input']) {
      const s = report.scenarios.find(x => x.scenario === name)!;
      expect(s.stagesRequested, name).toEqual([]);
      expect(s.checks.find(c => c.id === 'no-checkout')?.passed, name).toBe(true);
      expect(s.checks.find(c => c.id === 'no-run-directory')?.passed, name).toBe(true);
    }
  });

  it('formats a summary that names every scenario and each failed check', () => {
    const text = formatRehearsal(report);
    expect(text).toContain('Dossier rehearsal (polaris-dossier-rehearsal-v1): FAIL');
    for (const name of SCENARIO_NAMES) expect(text).toContain(name);
    expect(text).toContain('selection-fits-every-source-carrying-stage');
    expect(text).toContain('PASS  complete-small');
  });
});

describe('the checks fail on a bad run (rule 6: mutate the input)', () => {
  const page = (body: string, extra = ''): string => `<!doctype html><html><head><meta http-equiv="Content-Security-Policy" content="default-src 'none'"><title>t</title>${extra}</head><body><main>${body}</main></body></html>`;
  const site = (files: Record<string, string>): string => {
    const dir = tmp();
    for (const [rel, body] of Object.entries(files)) { mkdirSync(path.dirname(path.join(dir, rel)), { recursive: true }); writeFileSync(path.join(dir, rel), body); }
    return dir;
  };
  const verdict = (files: Record<string, string>) => inspectSite(site(files))[0]!;
  const good = { 'index.html': page('<a href="pages/a.html#x">a</a>'), 'pages/a.html': page('<h2 id="x">x</h2><a href="../index.html">home</a>') };

  it('accepts a site whose links and anchors land', () => { expect(verdict(good)).toMatchObject({ id: 'site-opens', passed: true }); });
  it('refuses a missing entry page', () => { expect(verdict({ 'pages/a.html': page('x') })).toMatchObject({ passed: false, detail: 'index.html is missing' }); });
  it.each([
    ['a broken link', { ...good, 'index.html': page('<a href="pages/missing.html">a</a>') }, 'broken link'],
    ['a missing anchor', { ...good, 'index.html': page('<a href="pages/a.html#nope">a</a>') }, 'no anchor'],
    ['an external reference', { ...good, 'index.html': page('<a href="https://example.test/">a</a>') }, 'external reference'],
    ['a protocol-relative reference', { ...good, 'index.html': page('<img src="//example.test/x.png">') }, 'external reference'],
    ['a script', { ...good, 'index.html': page('<p>x</p>', '<script>1</script>') }, 'contains a script'],
    ['a missing policy', { ...good, 'index.html': '<!doctype html><html><head><title>t</title></head><body><main>x</main></body></html>' }, 'no content security policy'],
    ['a fragment document', { ...good, 'index.html': '<p>x</p>' }, 'not a complete document'],
    ['a page with no doctype', { ...good, 'index.html': page('x').replace('<!doctype html>', '') }, 'not a complete document'],
    ['a page with no main region', { ...good, 'index.html': page('x').replace('<main>', '<div>').replace('</main>', '</div>') }, 'not a complete document'],
    ['a page with no title', { ...good, 'index.html': page('x').replace('<title>t</title>', '') }, 'not a complete document'],
  ])('refuses %s', (_name, files, why) => {
    const result = verdict(files);
    expect(result.passed).toBe(false);
    expect(result.detail).toContain(why);
  });

  const stage = 'inventory' as const;
  const dossierSystem = promptForStage(stage, 'dossier').system;
  const ran = (generation: Record<string, unknown> | undefined, systems: string[] = [dossierSystem], profile = 'dossier-v1'): Ran => ({
    exit: 0, outcome: { state: 'complete' }, text: '', runDir: '', stages: [], fetched: [], sources: null, envAfter: {}, fixture: null as never,
    requests: systems.map(system => ({ system, input: '', maxTokens: 0, raw: '' })), record: generation === undefined ? null : { profile, generation },
  });
  const call = (over: Record<string, unknown> = {}) => ({ phase: 'narrative', stage, ceilingUnits: 600, countedUnits: 2, usageUnknown: false, promptDigest: sha(dossierSystem), ...over });
  const gen = (over: Record<string, unknown> = {}) => ({ accountingPolicy: 'dossier-units-v1', promptProfile: 'dossier', spend: { discoveryCountedUnits: 4, narrativeCountedUnits: 2 },
    budget: { runTotalUnits: 4000, discoveryUnits: 1000, narrativeUnits: 3000 }, calls: [call()], ...over });
  const failing = (r: Ran): string[] => recordChecks(r).filter(c => !c.passed).map(c => c.id);

  it('accepts a record that names the dossier profile, its prompt digests and a spend inside the budget', () => { expect(failing(ran(gen()))).toEqual([]); });
  it('refuses a record that names another run profile', () => { expect(failing(ran(gen(), [dossierSystem], 'manifesto-v1'))).toEqual(['record-profile']); });
  it('refuses prompt digests that never appeared on the wire', () => { expect(failing(ran(gen(), []))).toEqual(['record-prompt-digests']); });
  it('refuses a record with no generation block', () => { expect(failing(ran(undefined))).toEqual(['record-present']); });
  it('refuses a run that sent the manifesto prompts', () => {
    const manifesto = promptForStage(stage, 'manifesto').system;
    expect(failing(ran(gen({ promptProfile: 'manifesto', calls: [call({ promptDigest: sha(manifesto) })] }), [manifesto]))).toEqual(['record-prompt-profile', 'record-prompt-digests']);
  });
  it('refuses a digest that was never on the wire', () => { expect(failing(ran(gen({ calls: [call({ promptDigest: sha('invented') })] })))).toContain('record-prompt-digests'); });
  it('refuses a record with no calls', () => { expect(failing(ran(gen({ calls: [] })))).toContain('record-prompt-digests'); });
  it('refuses overspend in either share and in total', () => {
    expect(failing(ran(gen({ spend: { discoveryCountedUnits: 1001, narrativeCountedUnits: 0 } })))).toEqual(['record-budget']);
    expect(failing(ran(gen({ spend: { discoveryCountedUnits: 0, narrativeCountedUnits: 3001 } })))).toEqual(['record-budget']);
    expect(failing(ran(gen({ budget: { runTotalUnits: 5, discoveryUnits: 1000, narrativeUnits: 3000 } })))).toEqual(['record-budget']);
  });
  it('refuses a call whose usage was unknown', () => { expect(failing(ran(gen({ calls: [call({ usageUnknown: true })] })))).toEqual(['record-usage-known']); });
  it('refuses a call over its stage ceiling when the ceiling is the expectation', () => {
    const r = ran(gen({ calls: [call({ countedUnits: 601 })] }));
    expect(recordChecks(r, { expectCeilingSpend: true }).filter(c => !c.passed).map(c => c.id)).toContain('record-ceiling-spend');
  });
  it('recognises only dossier-profile stage prompts', () => {
    expect(stageOfSystem(dossierSystem)).toBe('inventory');
    expect(stageOfSystem(promptForStage(stage, 'manifesto').system)).toBe('unknown');
  });
});

describe('poc:dossier-rehearsal', () => {
  const run = async (argv: string[]) => { const out: string[] = [], err: string[] = []; const code = await main(argv, t => out.push(t), t => err.push(t)); return { code, out: out.join(''), err: err.join('') }; };
  it('exits 2 on an unknown flag, an unknown scenario or a flag with no value', async () => {
    for (const argv of [['--nope'], ['--scenario', 'nonesuch'], ['--scenario'], ['--report']]) expect((await run(argv)).code, argv.join(' ')).toBe(2);
  });
  it('exits 0 and writes the report when every selected scenario passes', async () => {
    const file = path.join(tmp(), 'report.json');
    const r = await run(['--scenario', 'refused-bad-input', '--scenario', 'refused-no-consent', '--report', file]);
    expect(r.code).toBe(0);
    expect(r.out).toContain('PASS');
    expect(JSON.parse((await import('node:fs')).readFileSync(file, 'utf8'))).toMatchObject({ format: REHEARSAL_FORMAT, passed: true });
  }, 60_000);
  it('exits 1 when a selected scenario fails', async () => {
    const r = await run(['--scenario', 'complete-redis-shaped']);
    expect(r.code).toBe(1);
    expect(r.out).toContain('FAIL');
  }, 120_000);
  it('removes its scratch space unless asked to keep it', async () => {
    const kept: string[] = [];
    const out: string[] = [];
    expect(await main(['--scenario', 'refused-bad-input', '--keep'], t => out.push(t), () => undefined)).toBe(0);
    const line = out.join('').split('\n').find(l => l.startsWith('Scratch space kept at '));
    expect(line).toBeDefined();
    kept.push(line!.slice('Scratch space kept at '.length));
    const { existsSync } = await import('node:fs');
    expect(existsSync(kept[0]!)).toBe(true);
    rmSync(kept[0]!, { recursive: true, force: true });
  }, 60_000);
});

describe('every scenario check fails on a tampered run (rule 6)', () => {
  const originals = new Map<string, string>();
  const rans = new Map<string, Ran>();
  const names = SCENARIO_NAMES.filter(n => n !== 'complete-redis-shaped');
  it('collects one real run of each small-corpus scenario', async () => {
    const report = await rehearse({ scenarios: names, observe: (name, r) => {
      originals.set(name, r.runDir);
      const copy = tmp();
      if (existsSync(r.runDir)) cpSync(r.runDir, path.join(copy, 'run'), { recursive: true });
      rans.set(name, { ...r, runDir: path.join(copy, 'run') });
    } });
    expect(report.passed).toBe(true);
    expect(rans.size).toBe(names.length);
  }, 120_000);

  const def = (name: string) => SCENARIOS.find(s => s.name === name)!;
  const failedIds = async (name: string, patch: Partial<Ran>): Promise<string[]> => (await def(name).checks({ ...rans.get(name)!, ...patch })).filter(c => !c.passed).map(c => c.id);
  const empty = (): string => path.join(tmp(), 'run');
  const withIndex = (): string => { const dir = empty(); mkdirSync(dir, { recursive: true }); writeFileSync(path.join(dir, 'index.html'), '<p>x</p>'); return dir; };

  it.each(names)('%s: the untampered run has no failed check', async name => { expect(await failedIds(name, {})).toEqual([]); });

  it('rehearse removed its scratch space', () => { for (const dir of originals.values()) expect(existsSync(dir), dir).toBe(false); });

  it('complete: refuses the wrong state, a leaked credential, an unrecognised or misordered stage, a missing site and a missing evaluation', async () => {
    const r = rans.get('complete-small')!;
    expect(await failedIds('complete-small', { outcome: { state: 'generation-stopped' } })).toContain('state-complete');
    expect(await failedIds('complete-small', { envAfter: { [CREDENTIAL]: STUB_KEY } })).toEqual(['credential-consumed']);
    expect(await failedIds('complete-small', { requests: [...r.requests.slice(0, 1), { ...r.requests[1]!, raw: `leaked ${STUB_KEY}` }, ...r.requests.slice(2)] })).toEqual(['credential-consumed']);
    expect(await failedIds('complete-small', { stages: [...r.stages, 'repair'] })).toEqual(['stage-order']);
    expect(await failedIds('complete-small', { stages: [...r.stages.slice(0, 2), 'plan', 'inventory', ...r.stages.slice(4)] })).toEqual(['stage-order']);
    expect(await failedIds('complete-small', { stages: ['inventory', 'plan', 'author', 'edit', 'fidelity'] })).toEqual(['stage-order']);
    expect(await failedIds('complete-small', { stages: [...r.stages, 'unknown'] })).toContain('no-unknown-stage');
    expect(await failedIds('complete-small', { runDir: empty() })).toContain('site-opens');
    expect(await failedIds('complete-small', { sources: null })).toContain('pages-evaluate');
    expect(await failedIds('complete-small', { runDir: empty() })).toEqual(expect.arrayContaining(['site-opens', 'pages-evaluate']));
  });

  it('partial, wall-clock and refusals: each check fails when its guarantee is broken', async () => {
    expect(await failedIds('partial', { outcome: { state: 'complete' } })).toEqual(['state-partial']);
    expect(await failedIds('partial', { stages: [...rans.get('partial')!.stages, 'author'] })).toEqual(['no-later-stage']);
    expect(await failedIds('partial', { runDir: empty() })).toContain('partial-render');
    expect(await failedIds('wall-clock', { outcome: { state: 'complete' } })).toEqual(['state-stopped']);
    expect(await failedIds('wall-clock', { stages: [...rans.get('wall-clock')!.stages, 'inventory'] })).toEqual(['no-narrative-stage']);
    expect(await failedIds('wall-clock', { runDir: withIndex() })).toContain('record-only');
    expect(await failedIds('wall-clock', { runDir: empty() })).toContain('record-only');
    for (const name of ['refused-no-credential', 'refused-no-consent', 'refused-bad-input']) {
      const base = rans.get(name)!;
      expect(await failedIds(name, { requests: [{ system: '', input: '', maxTokens: 0, raw: '' }] }), name).toContain('nothing-sent');
      expect(await failedIds(name, { runDir: withIndex() }), name).toContain('no-run-directory');
      expect(await failedIds(name, { fetched: [...base.fetched, 'checkout'] }), name).toContain('no-checkout');
    }
    expect(await failedIds('refused-no-credential', { outcome: { state: 'complete' } })).toEqual(['state-unavailable']);
    expect(await failedIds('refused-no-consent', { outcome: { state: 'complete' } })).toEqual(['state-admission-missing']);
    expect(await failedIds('refused-bad-input', { fetched: ['ls-remote'] })).toEqual(['nothing-listed']);
  });

  it('at-ceiling: every call really cost its permit, and the output cap held', async () => {
    const calls = (rans.get('at-ceiling')!.record!.generation as { calls: { stage: string; ceilingUnits: number; countedUnits: number }[] }).calls;
    expect(calls.length).toBeGreaterThan(5);
    for (const call of calls) expect(call.countedUnits, call.stage).toBe(call.ceilingUnits);
    expect(await failedIds('at-ceiling', { requests: rans.get('at-ceiling')!.requests.map(q => ({ ...q, maxTokens: 10_000_000 })) })).toContain('max-tokens-capped');
    expect(await failedIds('at-ceiling', { outcome: { state: 'generation-stopped' } })).toEqual(['state-complete']);
  });

  it('the evaluation check fails on an unlabelled claim and on an invented quotation in a cited block', async () => {
    const r = rans.get('complete-small')!;
    const tamper = (change: (html: string) => string): string => {
      const dir = path.join(tmp(), 'run');
      cpSync(r.runDir, dir, { recursive: true });
      const file = path.join(dir, 'index.html');
      writeFileSync(file, change(readFileSync(file, 'utf8')));
      return dir;
    };
    const ids = async (dir: string) => (await evaluatePages(dir, r.sources!)).filter(c => !c.passed).map(c => c.id);
    expect(await ids(r.runDir)).toEqual([]);
    expect(await ids(tamper(html => html.replace(/ data-epistemic="[a-z]+"/u, '')))).toEqual(expect.arrayContaining(['pages-all-claims-labelled']));
    expect(await ids(tamper(html => html.replace(/(<p data-claim-id="[^"]+"[^>]*>)/u, '$1The project states: &quot;words no source contains&quot; ')))).toContain('pages-evaluate');
  });

  it('a scenario is not passed when its exit code differs from the expectation, whatever its other checks say', async () => {
    const scratch = tmp();
    const fixture = buildFixture('small', scratch);
    const refused = SCENARIOS.find(s => s.name === 'refused-bad-input')!;
    const report = await runScenario({ ...refused, expectExit: 0, checks: () => [] }, fixture, scratch);
    expect(report).toMatchObject({ exit: 2, passed: false });
    expect(report.checks).toEqual([{ id: 'exit-code', passed: false, detail: 'exit 2, expected 0' }]);
  });

  it('a rehearsal that ran no scenario has not passed', async () => { expect((await rehearse({ scenarios: [] })).passed).toBe(false); });
  it('refuses an unknown scenario name', async () => { await expect(rehearse({ scenarios: ['nonesuch'] })).rejects.toThrow('unknown-scenario: nonesuch'); });
});

describe('the run record names the prompt profile of the request, defaulting to the manifesto profile', () => {
  const open = async (): Promise<{ session: Awaited<ReturnType<ReturnType<typeof openGeneration>>>; stop: () => Promise<void> }> => {
    const parent = tmp();
    const context: GenerationOpenContext = { target: { owner: 'redis', repo: 'redis' } as never, revision: 'a'.repeat(40), runDir: path.join(parent, 'run'),
      egress: { kind: 'egress-consent', repositoryId: 'redis-redis', commit: 'a'.repeat(40) } as never,
      records: { source: 'test', check: async () => ({ satisfied: true, record: 'EGRESS@1' }) as never, repositoryIdsFor: async () => ['redis-redis'], inForceEgress: async () => ({ record: 'EGRESS@1', digest: '0'.repeat(64) }) } as never };
    const session = await openGeneration({ route: 'messages-api', apiKey: STUB_KEY, root: path.resolve(__dirname, '../../../..'), providerFactory: build => ({ generate: async () => { throw new Error('no call'); }, attempts: () => [], gateDecisions: () => [], close: async () => undefined, ...(build ? {} : {}) }) as never })(context);
    return { session, stop: () => session.close() };
  };
  it.each([[undefined, 'manifesto'], ['dossier', 'dossier'], ['manifesto', 'manifesto']] as const)('request profile %s is recorded as %s', async (profile, recorded) => {
    const { session, stop } = await open();
    try {
      expect((session.record() as { promptProfile: unknown }).promptProfile).toBeNull();
      await session.runPipeline({ requestId: 'r', projectId: 'p', snapshotId: 's', routes: {}, startedAt: 0, budget: {}, sources: [], readerQuestions: [], requestedAssets: [], ...(profile === undefined ? {} : { promptProfile: profile }) } as never, new AbortController().signal);
      expect((session.record() as { promptProfile: unknown }).promptProfile).toBe(recorded);
    } finally { await stop(); }
  });
});
