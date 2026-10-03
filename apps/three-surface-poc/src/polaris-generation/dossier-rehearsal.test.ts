import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { afterAll, describe, expect, it } from 'vitest';

import { promptForStage } from '@syzygy/polaris-generation-core';

import { main } from './dossier-rehearsal-main.testkit.js';
import { REHEARSAL_FORMAT, SCENARIO_NAMES, formatRehearsal, inspectSite, recordChecks, rehearse, stageOfSystem, type Ran, type RehearsalReport } from './dossier-rehearsal.testkit.js';

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

  it('passes every scenario but the Redis-shaped one, whose selection the narrative cannot yet afford', () => {
    // [Observed] 2026-10-04: 200 quotable sources, 1,893,524 bytes, against an inventory ceiling of 600 units under the 1-token-per-byte bound.
    // When discovery caps its selection by bytes, or the ceilings change, this scenario passes and this test must be updated with it.
    expect(report.scenarios.filter(s => !s.passed).map(s => s.scenario)).toEqual(['complete-redis-shaped']);
    const failed = report.scenarios.find(s => s.scenario === 'complete-redis-shaped')!.checks.filter(c => !c.passed).map(c => c.id);
    expect(failed).toContain('selection-fits-inventory-ceiling');
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
    expect(text).toContain('selection-fits-inventory-ceiling');
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
  ])('refuses %s', (_name, files, why) => {
    const result = verdict(files);
    expect(result.passed).toBe(false);
    expect(result.detail).toContain(why);
  });

  const stage = 'inventory' as const;
  const dossierSystem = promptForStage(stage, 'dossier').system;
  const ran = (generation: Record<string, unknown> | undefined, systems: string[] = [dossierSystem]): Ran => ({
    exit: 0, outcome: { state: 'complete' }, text: '', runDir: '', stages: [], fetched: [], sources: null, envAfter: {}, fixture: null as never,
    requests: systems.map(system => ({ system, input: '', maxTokens: 0, raw: '' })), record: generation === undefined ? null : { profile: 'dossier-v1', generation },
  });
  const call = (over: Record<string, unknown> = {}) => ({ phase: 'narrative', stage, ceilingUnits: 600, countedUnits: 2, usageUnknown: false, promptDigest: sha(dossierSystem), ...over });
  const gen = (over: Record<string, unknown> = {}) => ({ accountingPolicy: 'dossier-units-v1', promptProfile: 'dossier', spend: { discoveryCountedUnits: 4, narrativeCountedUnits: 2 },
    budget: { runTotalUnits: 4000, discoveryUnits: 1000, narrativeUnits: 3000 }, calls: [call()], ...over });
  const failing = (r: Ran): string[] => recordChecks(r).filter(c => !c.passed).map(c => c.id);

  it('accepts a record that names the dossier profile, its prompt digests and a spend inside the budget', () => { expect(failing(ran(gen()))).toEqual([]); });
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
