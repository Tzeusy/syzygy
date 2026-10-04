import { describe, expect, it, vi } from 'vitest';

import { budgetArithmetic, checkDossier, formatCheck } from './dossier-check.js';
import { fixtureRouteRoot } from './dossier-fixtures.testkit.js';
import { progressLine, shareProgress } from './dossier-generation.js';
import { main } from './dossier-main.js';
import { DOSSIER_RUN_PROFILE } from './dossier-run-profile.js';
import type { AdmissionRecordsPort, TriggerPorts } from './dossier-trigger.js';

const SHA_A = 'a'.repeat(40), SHA_B = 'b'.repeat(40);
const LS = `${SHA_A}\tHEAD\n${SHA_B}\trefs/tags/8.0.0\n`;
const URL = 'https://github.com/redis/redis';
const all: AdmissionRecordsPort = { source: 'fixture store', repositoryIdsFor: async () => ['fixture-record-id'], check: async r => ({ satisfied: true, record: `fixture/${r.kind}` }) };
const withMissing = (kind: string): AdmissionRecordsPort => ({ ...all, check: async r => (r.kind === kind ? { satisfied: false, why: `no ${kind} record` } : { satisfied: true, record: `fixture/${r.kind}` }) });

describe('budget arithmetic', () => {
  it('is derived from the run profile with literal expected figures', () => {
    const b = budgetArithmetic();
    expect(b).toMatchObject({ runTotalUnits: 4000, discoveryUnits: 1000, narrativeUnits: 3000, discoveryCallUnits: 40, maxDiscoveryCalls: 25, wallClockMs: 7_200_000, maxSelectedBytes: 400_000 });
    expect(b.baseStagesAtCeilingUnits).toBe(DOSSIER_RUN_PROFILE.stageCeilingUnits.inventory + 300 + DOSSIER_RUN_PROFILE.stageCeilingUnits.author + DOSSIER_RUN_PROFILE.stageCeilingUnits.edit + DOSSIER_RUN_PROFILE.stageCeilingUnits.fidelity);
    expect(b.narrativeHeadroomUnits).toBe(b.narrativeUnits - b.baseStagesAtCeilingUnits);
    expect(b.repairCycleAtCeilingUnits).toBe(DOSSIER_RUN_PROFILE.stageCeilingUnits.repair + DOSSIER_RUN_PROFILE.stageCeilingUnits.fidelity);
    // 400,000 bytes plus one, in thousands, rounded up.
    expect(b.fullSelectionMinimumUnits).toBe(401);
  });

  it('counts affordable repair cycles from the headroom, capped at the profile, and flags a selection that cannot fit a source-carrying stage', () => {
    const tight = { ...DOSSIER_RUN_PROFILE, owner: { ...DOSSIER_RUN_PROFILE.owner, runTotalUnits: 3_000 + 1_000 }, stageCeilingUnits: { inventory: 400, plan: 300, author: 400, edit: 400, fidelity: 300, repair: 300 } };
    const b = budgetArithmetic(tight);
    expect(b.baseStagesAtCeilingUnits).toBe(1800);
    expect(b.narrativeHeadroomUnits).toBe(1200);
    expect(b.repairCycleAtCeilingUnits).toBe(600);
    expect(b.repairCyclesAffordable).toBe(2);
    expect(b.smallestSourceStageCeilingUnits).toBe(300);
    expect(b.fullSelectionFits).toBe(false);
    // The least units equal the smallest ceiling: it fits.
    expect(budgetArithmetic({ ...tight, owner: { ...tight.owner, runTotalUnits: 5_000 }, stageCeilingUnits: { inventory: 401, plan: 300, author: 401, edit: 401, fidelity: 401, repair: 300 } }).fullSelectionFits).toBe(true);
    expect(budgetArithmetic({ ...tight, maxRepairCycles: 1 }).repairCyclesAffordable).toBe(1);
    // Headroom 1000 holds one cycle of 600, not two.
    expect(budgetArithmetic({ ...tight, owner: { ...tight.owner, runTotalUnits: 3_800 } }).repairCyclesAffordable).toBe(1);
    // 1,010 discovery units hold 25 calls of 40, not 26.
    expect(budgetArithmetic({ ...tight, owner: { ...tight.owner, runTotalUnits: 4_010, discoveryUnits: 1_010 } }).maxDiscoveryCalls).toBe(25);
    expect(formatCheck({ ...(budgetOnly(b)) })).toContain('DOES NOT FIT');
  });
});

const budgetOnly = (budget: ReturnType<typeof budgetArithmetic>) => ({ state: 'check-ready' as const, target: { owner: 'a', repo: 'b', url: 'https://github.com/a/b', repositoryId: 'x' }, revision: SHA_A, resolvedRef: 'HEAD',
  revisionSource: { from: 'url' as const }, source: 's', requirements: [], budget });

describe('checkDossier reads nothing', () => {
  it('lists every record found and the budget, and touches only ls-remote and the records', async () => {
    const lsRemote = vi.fn(() => LS);
    const outcome = await checkDossier(URL, { lsRemote, records: all });
    expect(lsRemote).toHaveBeenCalledWith(URL);
    expect(outcome).toMatchObject({ state: 'check-ready', revision: SHA_A, resolvedRef: 'HEAD', revisionSource: { from: 'url' } });
    const text = formatCheck(outcome);
    for (const kind of ['observation-consent', 'public-source-policy', 'egress-consent']) expect(text).toContain(`OK       ${kind}: fixture/${kind}`);
    expect(text).toContain('Admission records consulted: fixture store');
    expect(text).toContain('run total 4000 = discovery 1000 + narrative 3000');
    expect(text).toContain('Nothing was read and no provider was called.');
  });

  it('names the revision source when a bare URL takes the consented revision', async () => {
    const records: AdmissionRecordsPort = { ...all, consentedRevisionsFor: async () => [{ label: '8.0.0', commitId: SHA_B }] };
    const outcome = await checkDossier(URL, { lsRemote: () => LS, records });
    expect(outcome).toMatchObject({ state: 'check-ready', revision: SHA_B, revisionSource: { from: 'consent', label: '8.0.0', commitId: SHA_B } });
    expect(formatCheck(outcome)).toContain(`the observation consent admits 8.0.0 (${SHA_B})`);
  });

  it('stops at the same gates a run stops at', async () => {
    expect(await checkDossier('https://example.com/a/b', { lsRemote: () => LS, records: all })).toMatchObject({ state: 'invalid-input' });
    expect(await checkDossier(URL, { lsRemote: () => { throw new Error('ls-remote-failed'); }, records: all })).toMatchObject({ state: 'unresolved-revision' });
    expect(await checkDossier(URL, { lsRemote: () => LS, records: withMissing('egress-consent') })).toMatchObject({ state: 'admission-missing', missing: 1 });
    expect(await checkDossier(URL, { lsRemote: () => LS })).toMatchObject({ state: 'admission-missing', missing: 3 });
  });
});

describe('poc:dossier --check', () => {
  const root = fixtureRouteRoot('agent-sdk');
  const run = async (args: string[], ports: TriggerPorts, env: Record<string, string | undefined> = {}) => {
    const out: string[] = [], err: string[] = [];
    const code = await main(args, ports, { root, env, stdout: t => out.push(t), stderr: t => err.push(t) });
    return { code, out: out.join(''), err: err.join('') };
  };

  it('exits 0 with no credential, no route and no generation, and calls nothing past the gates', async () => {
    const materialize = vi.fn(), runPipeline = vi.fn(), openGeneration = vi.fn();
    const { code, out } = await run(['--check', URL], { lsRemote: () => LS, records: all, materialize, runPipeline, openGeneration });
    expect(code).toBe(0);
    expect(out).toContain('READY');
    expect(materialize).not.toHaveBeenCalled();
    expect(runPipeline).not.toHaveBeenCalled();
    expect(openGeneration).not.toHaveBeenCalled();
  });

  it('exits with the code of the gate that stops it', async () => {
    expect((await run(['--check', 'https://example.com/a/b'], { lsRemote: () => LS, records: all })).code).toBe(2);
    expect((await run(['--check', URL], { lsRemote: () => { throw new Error('ls-remote-failed'); }, records: all })).code).toBe(4);
    const missing = await run(['--check', URL], { lsRemote: () => LS, records: withMissing('observation-consent') });
    expect(missing.code).toBe(3);
    expect(missing.out).toContain('MISSING  observation-consent');
    expect(missing.out).not.toContain('READY');
  });

  it('exits 5 when a chosen route is not in force, like a run, and 2 for an unknown route or --out', async () => {
    expect((await run(['--check', URL, '--route', 'messages-api'], { lsRemote: () => LS, records: all })).code).toBe(5);
    expect((await run(['--check', URL, '--route', 'carrier-pigeon'], { lsRemote: () => LS, records: all })).code).toBe(2);
    expect((await run(['--check', URL, '--out', '/tmp/x'], { lsRemote: () => LS, records: all })).code).toBe(2);
    expect((await run(['--check', URL, '--route', 'agent-sdk'], { lsRemote: () => LS, records: all })).code).toBe(0);
  });

  it('without --check the route is still required', async () => {
    expect((await run([URL], { lsRemote: () => LS, records: all })).code).toBe(2);
  });

  it('prints the outcome as JSON with the budget', async () => {
    const { code, out } = await run(['--check', URL, '--json'], { lsRemote: () => LS, records: all });
    expect(code).toBe(0);
    expect(JSON.parse(out)).toMatchObject({ state: 'check-ready', budget: { runTotalUnits: 4000, narrativeUnits: 3000 } });
  });
});

describe('progress line', () => {
  it('measures each call against the share it belongs to', () => {
    const calls = [{ phase: 'discovery' as const, countedUnits: 40 }, { phase: 'narrative' as const, countedUnits: 300 }, { phase: 'discovery' as const, countedUnits: 25 }, { phase: 'narrative' as const, countedUnits: 11 }];
    expect(shareProgress('discovery', calls, DOSSIER_RUN_PROFILE)).toEqual({ spent: 65, units: 1000 });
    expect(shareProgress('narrative', calls, DOSSIER_RUN_PROFILE)).toEqual({ spent: 311, units: 3000 });
  });
  it('switches to minutes and hours exactly at their boundaries', () => {
    const call = { phase: 'narrative' as const, stage: 'edit' as const, countedUnits: 1, ceilingUnits: 2, usageUnknown: false };
    expect(progressLine(call, 1, 2, 59_000)).toContain('elapsed 59s');
    expect(progressLine(call, 1, 2, 60_000)).toContain('elapsed 1m00s');
    expect(progressLine(call, 1, 2, 3_599_000)).toContain('elapsed 59m59s');
    expect(progressLine(call, 1, 2, 3_600_000)).toContain('elapsed 1h00m');
    expect(progressLine(call, 1, 2, -5000)).toContain('elapsed 0s');
  });
  const call = { phase: 'narrative' as const, stage: 'author' as const, countedUnits: 312, ceilingUnits: 524, usageUnknown: false };
  it('names stage, units against ceiling and share, and elapsed time, and nothing else', () => {
    expect(progressLine(call, 700, 3000, 130_000)).toBe('[narrative author] counted 312 of ceiling 524; narrative share 700 of 3000 units; elapsed 2m10s\n');
    expect(progressLine({ ...call, phase: 'discovery', stage: 'discovery-map' as never, countedUnits: 12, ceilingUnits: 40 }, 12, 1000, 4_400)).toBe('[discovery discovery-map] counted 12 of ceiling 40; discovery share 12 of 1000 units; elapsed 4s\n');
    expect(progressLine(call, 1, 2, 3_900_000)).toContain('elapsed 1h05m');
  });
  it('says so when the usage is unknown and was counted at the ceiling', () => {
    expect(progressLine({ ...call, countedUnits: 524, usageUnknown: true }, 524, 3000, 0)).toContain('(usage unknown, counted at the call ceiling)');
  });
});
