import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { parseRunConfig } from './run-config.js';
import { encodeRunRecord } from './run-record.js';
import { runStatus } from './status.js';

// `syzygy dossier status`: everything it reports is read from files the agent sessions can write, so
// every value is labelled Inferred; the principal is the operator with credential identity Unknown.
const CONFIG = {
  operator: 'Tzeusy', agentTool: 'codex', agentToolVersion: '0.40.0', agentProvider: 'openai', model: 'gpt-5.5',
  deadline: 'PT3H', agentTurnBudget: 300, maxRepairCycles: 2, maxQuestions: 0, audience: 'a new contributor',
  operatorIsOwner: false,
};
let runDir: string;
beforeEach(() => {
  runDir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-status-')));
  const parsed = parseRunConfig(JSON.stringify(CONFIG));
  if (!parsed.ok) throw new Error('fixture configuration refused');
  fs.writeFileSync(path.join(runDir, 'run.json'), encodeRunRecord(parsed.config));
});
afterEach(() => fs.rmSync(runDir, { recursive: true, force: true }));

const snapshot = (dir: string): string[] => fs.readdirSync(dir, { recursive: true, withFileTypes: true })
  .map((entry) => {
    const full = path.join(entry.parentPath, entry.name);
    const stats = fs.statSync(full);
    return `${path.relative(dir, full)} ${stats.size} ${stats.mtimeMs}`;
  }).sort();

describe('status (REQ-polaris-generation-033)', () => {
  it('reports a configured run, every value Inferred and operator-declared', () => {
    const result = runStatus(runDir);
    expect(result.ok).toBe(true);
    if (!result.ok) return;
    expect(result.report).toEqual({
      command: 'status',
      outcome: 'reported',
      run: runDir,
      label: 'Inferred',
      basis: 'the run directory, which the agent sessions can write',
      mode: 'operator-agent',
      route: 'none: the dossier commands serve no route, accept no network request and hold no credential that authenticates to Syzygy',
      principal: { name: 'Tzeusy', declaredBy: 'operator', credentialIdentity: 'Unknown' },
      state: 'configured',
      configuration: {
        declaredBy: 'operator',
        label: 'Inferred',
        values: {
          operator: 'Tzeusy', agentTool: 'codex', agentToolVersion: '0.40.0', agentProvider: 'openai', model: 'gpt-5.5',
          modelVersion: 'not shown by the agent tool', deadline: 'PT3H', agentTokenBudget: 'not declared',
          agentTurnBudget: 300, maxRepairCycles: 2, maxQuestions: 0, audience: 'a new contributor', operatorIsOwner: false,
        },
        modelVersionProvider: 'no provider-reported model version is available in the operator-agent mode',
      },
      steps: {
        brief: 'not recorded', draftRevisions: 0, checkedRevisions: 0, inventory: 'not recorded',
        reviewPackets: 0, reviewVerdicts: 0, site: 'not recorded', closed: false,
      },
      limitsSpent: {
        repairCycles: '0 checked revisions recorded of 2 repair cycles declared',
        questions: 'not recorded of 0 declared',
        deadline: 'PT3H; not started (no brief recorded)',
        agentUsage: 'not recorded; Syzygy cannot observe the agent sessions\' usage',
      },
      openFindings: 'not recorded',
      reviewsStillRequired: ['inventory', 'fidelity review', 'rendered-design review'],
      unrecognizedEntries: [],
    });
  });

  it('counts recorded steps by the layout\'s own names and lists, never reads, anything else', () => {
    fs.writeFileSync(path.join(runDir, 'brief.md'), '# brief\n');
    fs.mkdirSync(path.join(runDir, 'drafts'));
    fs.writeFileSync(path.join(runDir, 'drafts', 'rev-0.json'), '{}');
    fs.writeFileSync(path.join(runDir, 'drafts', 'rev-1.json'), '{}');
    fs.writeFileSync(path.join(runDir, 'drafts', 'next.json'), '{}');
    fs.mkdirSync(path.join(runDir, 'checks'));
    fs.writeFileSync(path.join(runDir, 'checks', 'rev-0.json'), '{}');
    fs.writeFileSync(path.join(runDir, 'checks', 'rev-01.json'), '{}');
    fs.writeFileSync(path.join(runDir, 'notes.txt'), 'agent scratch');
    const result = runStatus(runDir);
    expect(result.ok && result.report.steps).toEqual({
      brief: 'recorded', draftRevisions: 2, checkedRevisions: 1, inventory: 'not recorded',
      reviewPackets: 0, reviewVerdicts: 0, site: 'not recorded', closed: false,
    });
    expect(result.ok && result.report.state).toBe('drafting');
    expect(result.ok && result.report.limitsSpent.repairCycles).toBe('1 checked revisions recorded of 2 repair cycles declared');
    expect(result.ok && result.report.limitsSpent.deadline).toBe('PT3H from the brief; elapsed time not recorded');
    expect(result.ok && result.report.unrecognizedEntries).toEqual(['notes.txt']);
  });

  it.each([
    ['reviewing', (dir: string) => { fs.mkdirSync(path.join(dir, 'inventory')); }],
    ['rendered', (dir: string) => { fs.mkdirSync(path.join(dir, 'site')); }],
    ['closed', (dir: string) => { fs.writeFileSync(path.join(dir, 'record.json'), '{}'); }],
  ])('derives the state %s from the files recorded', (state, make) => {
    make(runDir);
    const result = runStatus(runDir);
    expect(result.ok && result.report.state).toBe(state);
  });

  it('writes nothing', () => {
    const before = snapshot(runDir);
    runStatus(runDir);
    expect(snapshot(runDir)).toEqual(before);
  });

  it('refuses a missing run directory', () => {
    const result = runStatus(path.join(runDir, 'absent'));
    expect(result).toEqual({ ok: false, reason: `run directory ${path.join(runDir, 'absent')} cannot be read (ENOENT)` });
  });

  it('refuses a directory with no run.json', () => {
    fs.rmSync(path.join(runDir, 'run.json'));
    const result = runStatus(runDir);
    expect(result.ok).toBe(false);
    expect(!result.ok && result.reason).toBe(`${runDir} holds no readable run.json (ENOENT)`);
  });

  it.each([
    ['a stored limit made unlimited', (record: Record<string, any>) => { record['declared']['maxRepairCycles'] = null; }, 'run.json declares an invalid run configuration'],
    ['the label changed to Observed', (record: Record<string, any>) => { record['label'] = 'Observed'; }, 'run.json is not a polaris-dossier-run/1 record of the operator-agent mode'],
    ['a fabricated credential identity', (record: Record<string, any>) => { record['principal']['credentialIdentity'] = 'token-abc'; }, 'run.json principal must be the declared operator, operator-declared, with credential identity Unknown'],
    ['a principal other than the operator', (record: Record<string, any>) => { record['principal']['name'] = 'someone-else'; }, 'run.json principal must be the declared operator, operator-declared, with credential identity Unknown'],
    ['an execution choice smuggled into the record', (record: Record<string, any>) => { record['declared']['executionChoice'] = 'allow'; }, 'run.json declares an invalid run configuration'],
    ['an extra top-level field', (record: Record<string, any>) => { record['observed'] = true; }, 'run.json carries fields declared, declaredBy, format, label, mode, modelVersionProvider, observed, principal; expected declared, declaredBy, format, label, mode, modelVersionProvider, principal'],
  ])('re-validates the stored record and refuses %s', (_label, mutate, reason) => {
    const file = path.join(runDir, 'run.json');
    const record = JSON.parse(fs.readFileSync(file, 'utf8')) as Record<string, any>;
    mutate(record);
    fs.writeFileSync(file, JSON.stringify(record));
    const result = runStatus(runDir);
    expect(result.ok).toBe(false);
    expect(!result.ok && result.reason).toBe(reason);
  });
});
