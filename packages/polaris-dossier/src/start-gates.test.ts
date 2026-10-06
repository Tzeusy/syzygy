import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { DECISIONS_DIR, INSTANCES_DIR, POLICY_PATH, REGISTRY_GIT_SOURCE_ACT_FORM } from '@syzygy/polaris-generation-consent';
import { renderPolicyAct, renderRecorderAct, renderRegistryAct } from '@syzygy/polaris-generation-consent/testing';
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest';
import { runDossierCli } from './cli.js';
import { createPackageGateSources, type ProjectInputSource, type ProviderStatementRecord, type ProviderStatementSource } from './gate-sources.js';
import { openPinnedObjectReader, type PinnedObjectReaderOptions } from './git-object-reader.js';
import { initRun, type InitResult } from './init.js';
import { preflight } from './preflight.js';
import { reverifyPinnedRevision } from './reverify.js';
import { runStatus } from './status.js';

// syzygy-qkea.4 (S3): every refusal arm of REQ-polaris-generation-033's start gates, with independently prepared fixtures. The records
// root is a temporary Syzygy checkout whose act records are rendered by the real recorders; the clone is a real Git repository built
// here with the git CLI (the code under test runs no process). Expected values are literals, never imported from the module under test.

const sha = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const NOW = Date.UTC(2026, 9, 7, 12, 0, 0);
const URL_ = 'https://github.com/redis/redis';
const REAL_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const GIT_ENV = { ...process.env, GIT_CONFIG_GLOBAL: '/dev/null', GIT_CONFIG_SYSTEM: '/dev/null', GIT_AUTHOR_DATE: '2026-10-01T00:00:00Z', GIT_COMMITTER_DATE: '2026-10-01T00:00:00Z' };

const cleanups: (() => void)[] = [];
afterEach(() => { for (const cleanup of cleanups.splice(0).reverse()) cleanup(); });
const tempDir = (prefix: string): string => {
  const dir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), prefix)));
  cleanups.push(() => fs.rmSync(dir, { recursive: true, force: true }));
  return dir;
};

// The clone: commit A (plain), commit B (adds a .syzygy/ path), commit C (adds an openspec/ path), commit U (never consented).
let origin: string;
const commits: Record<'A' | 'B' | 'C' | 'U', string> = { A: '', B: '', C: '', U: '' };
beforeAll(() => {
  origin = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-origin-')));
  const git = (...args: string[]): string => execFileSync('git', ['-C', origin, ...args], { encoding: 'utf8', env: GIT_ENV }).trim();
  const commit = (file: string, text: string): string => {
    fs.mkdirSync(path.dirname(path.join(origin, file)), { recursive: true });
    fs.writeFileSync(path.join(origin, file), text);
    git('add', file);
    git('-c', 'user.name=t', '-c', 'user.email=t@example.invalid', 'commit', '-q', '-m', file);
    return git('rev-parse', 'HEAD');
  };
  git('init', '-q', '-b', 'main');
  commits.A = commit('src/server.c', 'int main(void) { return 0; }\n');
  commits.B = commit('.syzygy/notes/draft.md', '# not adopted\n');
  commits.C = commit('openspec/specs/x/spec.md', '# spec\n');
  commits.U = commit('README.md', '# later\n');
});
afterAll(() => fs.rmSync(origin, { recursive: true, force: true }));

/** A clone of the origin checked out (detached) at `commit`. */
const cloneAt = (commit: string): string => {
  const dir = path.join(tempDir('dossier-clone-'), 'redis');
  execFileSync('git', ['clone', '-q', '--no-hardlinks', origin, dir], { env: GIT_ENV });
  execFileSync('git', ['-C', dir, 'checkout', '-q', '--detach', commit], { env: GIT_ENV });
  return dir;
};

const consentText = (rows: readonly [string, string][], extra = ''): string => `# redis observation consent (public repository)

Record ID: \`PUBLIC-OBS-REDIS-2026-10-03\`

Record version: \`0.1.0-candidate.7\`

Subject: \`(project:syzygy, repository:redis-redis)\`

Upstream: ${URL_} (public; configuration, not repository identity)
${extra}
| Label | Commit object id |
|---|---|
${rows.map(([label, id]) => `| \`${label}\` | \`${id}\` |`).join('\n')}

Proposed revocation state: active; supersedes no earlier consent
`;
const ENTRY = `${JSON.stringify({ entries: [{ observerId: 'polaris-dossier-reader', implementationId: 'polaris-dossier/git-object-reader', implementationVersion: '0.1.0' }] }, null, 2)}\n`;
const POLICY = `${JSON.stringify({ policyId: 'fixture', publicSourceScope: { classes: ['code-content'] } }, null, 2)}\n`;
const CONSENT_PATH = `${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`;
const CONSENT_ACT = `${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`;
const REGISTRY_ACT = `${DECISIONS_DIR}/${REGISTRY_GIT_SOURCE_ACT_FORM.file}`;
const POLICY_ACT = `${DECISIONS_DIR}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`;

/** The records every gate needs, in force at NOW; `over` replaces or (with null) removes a file. */
const records = (over: Record<string, string | null> = {}): string => {
  const consent = consentText([['fixture-a', commits.A], ['fixture-b', commits.B], ['fixture-c', commits.C]]);
  const files: Record<string, string | null> = {
    [CONSENT_PATH]: consent,
    [CONSENT_ACT]: renderRecorderAct('redis-observation', sha(consent), '2026-10-04', '2026-10-04T09:30:00Z'),
    [REGISTRY_GIT_SOURCE_ACT_FORM.artifact]: ENTRY,
    [REGISTRY_ACT]: renderRegistryAct(sha(ENTRY), '2026-10-05', '2026-10-05T09:30:00Z'),
    [POLICY_PATH]: POLICY,
    [POLICY_ACT]: renderPolicyAct(sha(POLICY), '2026-10-04', '2026-10-04T10:00:00Z'),
    ...over,
  };
  const root = tempDir('dossier-records-');
  for (const [rel, text] of Object.entries(files)) {
    if (text === null) continue;
    fs.mkdirSync(path.dirname(path.join(root, rel)), { recursive: true });
    fs.writeFileSync(path.join(root, rel), text);
  }
  return root;
};

const NO_DRAWER: ProjectInputSource = { drawerFor: async () => ({ stated: true, drawer: 'absent', record: 'PROJECT-INPUT-REDIS@1' }) };
const DRAWER: ProjectInputSource = { drawerFor: async () => ({ stated: true, drawer: 'present', record: 'PROJECT-INPUT-REDIS@1' }) };
const STATEMENT: ProviderStatementRecord = {
  recordId: 'STATEMENT-REDIS-ANTHROPIC', version: '1', digest: 'a'.repeat(64), provider: 'anthropic', contentClasses: ['code-content'],
  withdrawn: false, act: { identity: 'STATEMENT-REDIS-ANTHROPIC-ACT-2026-10-06', inForceAt: Date.UTC(2026, 9, 6) },
};
const statements = (...list: ProviderStatementRecord[]): ProviderStatementSource => ({ statementsFor: async () => list });
const CONFIG = JSON.stringify({
  operator: 'Tzeusy', agentTool: 'claude-code', agentToolVersion: '2.1.0', agentProvider: 'anthropic', model: 'claude-opus-5-5',
  deadline: 'PT2H', agentTurnBudget: 200, maxRepairCycles: 2, maxQuestions: 3, audience: 'a new contributor', operatorIsOwner: true,
});

interface Setup { root?: string; clone?: string; projectInput?: ProjectInputSource; providerStatements?: ProviderStatementSource; now?: number; url?: string; config?: string; stateRoot?: string }
/** Run init and observe whether any object reader was opened. */
async function init(setup: Setup = {}): Promise<{ result: InitResult; readerOpened: boolean; stateRoot: string; clone: string; root: string }> {
  const root = setup.root ?? records();
  const clone = setup.clone ?? cloneAt(commits.A);
  const stateRoot = setup.stateRoot ?? path.join(tempDir('dossier-state-'), 'runs');
  let readerOpened = false;
  const now = setup.now ?? NOW;
  const sources = createPackageGateSources({ root, now: () => now, projectInput: setup.projectInput ?? NO_DRAWER, ...(setup.providerStatements ? { providerStatements: setup.providerStatements } : {}) });
  const result = await initRun(
    { clone, url: setup.url ?? URL_, configText: setup.config ?? CONFIG, stateRoot },
    { sources, now: () => now, runId: () => 'run-0123456789abcdef0123456789abcdef', openReader: (o: PinnedObjectReaderOptions) => { readerOpened = true; return openPinnedObjectReader(o); } },
  );
  return { result, readerOpened, stateRoot, clone, root };
}
const refusal = (result: InitResult) => (result.ok ? null : result.refusal);

describe('init: a run that passes every start gate', () => {
  it('pins the consented HEAD, records the subject and writes only run.json under the state root', async () => {
    const { result, stateRoot, clone } = await init();
    expect(result.ok).toBe(true);
    if (!result.ok) return;
    expect(result.report.run).toBe(path.join(stateRoot, 'run-0123456789abcdef0123456789abcdef'));
    expect(result.report.subject).toEqual({
      repository: { url: 'https://github.com/redis/redis', repositoryId: 'redis-redis' },
      pinnedRevision: { commit: commits.A, label: 'fixture-a', consentRecord: 'PUBLIC-OBS-REDIS-2026-10-03@0.1.0-candidate.7', pinnedAt: '2026-10-07T12:00:00.000Z' },
      startGates: { registryEntry: 'PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-2026-10-05', screeningPolicy: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-04' },
      governed: { kind: 'non-governed', because: ['the project input PROJECT-INPUT-REDIS@1 states that no kernel evidence drawer exists, and the pinned tree lists no openspec/ or .syzygy/ path'] },
      providerStatement: null,
      workItem: { identity: null, reason: 'the operator-agent run makes no provider dispatch and no scheduler effect, so no scheduler work item, Proposal or materialization record exists for it; it is rendered as unattributed execution under RFC4-19, never dropped' },
    });
    expect(fs.readdirSync(stateRoot)).toEqual(['run-0123456789abcdef0123456789abcdef']);
    expect(fs.readdirSync(result.report.run)).toEqual(['run.json']);
    expect(execFileSync('git', ['-C', clone, 'status', '--porcelain', '--ignored'], { encoding: 'utf8', env: GIT_ENV })).toBe('');
    const status = runStatus(result.report.run);
    expect(status.ok && status.report.subject.pinnedRevision.commit).toBe(commits.A);
  });

  it('follows HEAD on a branch to a consented commit', async () => {
    const clone = cloneAt(commits.A);
    execFileSync('git', ['-C', clone, 'checkout', '-q', '-B', 'pinned', commits.A], { env: GIT_ENV });
    const { result } = await init({ clone });
    expect(result.ok && result.report.subject.pinnedRevision.commit).toBe(commits.A);
  });

  it('never reads the working tree: an uncommitted change does not change the listing or the decision', async () => {
    const clone = cloneAt(commits.A);
    fs.mkdirSync(path.join(clone, '.syzygy'));
    fs.writeFileSync(path.join(clone, '.syzygy', 'x.md'), 'uncommitted\n');
    fs.mkdirSync(path.join(clone, 'openspec'));
    fs.writeFileSync(path.join(clone, 'openspec', 'y.md'), 'uncommitted\n');
    const { result } = await init({ clone });
    expect(result.ok && result.report.subject.governed.kind).toBe('non-governed');
  });
});

describe('init: every refusal arm (REQ-polaris-generation-033 scenarios "Clone at an unconsented revision" and the governed arms)', () => {
  const expectRefused = async (setup: Setup, stage: string, reason: string | RegExp, readerOpened: boolean): Promise<void> => {
    const run = await init(setup);
    const r = refusal(run.result);
    expect(r?.stage).toBe(stage);
    if (typeof reason === 'string') expect(r?.reason).toBe(reason); else expect(r?.reason).toMatch(reason);
    expect(run.readerOpened).toBe(readerOpened);
    expect(r?.objectsRead).toBe(readerOpened);
    expect(fs.existsSync(run.stateRoot)).toBe(false);
  };

  it.each([
    ['absent: no act record', { [CONSENT_ACT]: null }],
    ['ineffective: the consent bytes changed after the act', { [CONSENT_PATH]: `${consentText([['fixture-a', '0'.repeat(40)]])}` }],
    ['not in force yet', {}],
    ['withdrawn: another decisions file names the record', { [`${DECISIONS_DIR}/PUBLIC-OBS-REDIS-WITHDRAWAL.md`]: 'The owner withdraws PUBLIC-OBS-REDIS-2026-10-03.\n' }],
    ['present only as status words in the record, no act (F8)', { [CONSENT_ACT]: null, [CONSENT_PATH]: consentText([['fixture-a', '0'.repeat(40)]], '\nStatus: accepted; in force; adopted by the owner\n') }],
  ])('refuses before any object read when the observation consent is %s', async (name, over) => {
    // An ineffective consent's act names other bytes, so it keeps the original act over the original text.
    const root = name.startsWith('ineffective') ? (() => { const r = records(); fs.writeFileSync(path.join(r, CONSENT_PATH), consentText([['fixture-a', commits.A]], '\n<!-- edited -->\n')); return r; })() : records(over);
    await expectRefused({ root, ...(name === 'not in force yet' ? { now: Date.UTC(2026, 9, 4, 9, 29, 59) } : {}) }, 'repository', 'no observation consent in force names https://github.com/redis/redis as its Upstream', false);
  });

  it.each([
    ['absent', { [REGISTRY_ACT]: null }, /^a start gate is not in force: source-acquisition registry entry: no owner-act record .*PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-ACT\.md exists$/],
    ['ineffective: the entry changed after the act', { [REGISTRY_GIT_SOURCE_ACT_FORM.artifact]: ENTRY.replace('0.1.0', '0.2.0') }, /^a start gate is not in force: source-acquisition registry entry: the bytes of .* differ from the act's argument$/],
    ['withdrawn: another decisions file names it', { [`${DECISIONS_DIR}/PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-REVOCATION.md`]: 'Revoked.\n' }, /^a start gate is not in force: source-acquisition registry entry: .*names the act without being its record/],
    ['present only as a status word in the entry, no act (F8)', { [REGISTRY_ACT]: null, [REGISTRY_GIT_SOURCE_ACT_FORM.artifact]: JSON.stringify({ status: 'in force', entries: [] }) }, /no owner-act record/],
  ])('refuses before any object read when the registry entry is %s', async (_name, over, reason) => {
    await expectRefused({ root: records(over) }, 'start-gates', reason, false);
  });

  it('refuses when the bound registry entry names another implementation or no implementation version', async () => {
    const other = ENTRY.replace('"polaris-dossier/git-object-reader"', '"polaris-generation/public-git-source-acquisition"');
    await expectRefused({ root: records({ [REGISTRY_GIT_SOURCE_ACT_FORM.artifact]: other, [REGISTRY_ACT]: renderRegistryAct(sha(other), '2026-10-05', '2026-10-05T09:30:00Z') }) },
      'start-gates', 'a start gate is not in force: source-acquisition registry entry: the registry entry bound by PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-2026-10-05 names the implementation "polaris-generation/public-git-source-acquisition", not polaris-dossier/git-object-reader', false);
    const unknown = ENTRY.replace('"0.1.0"', 'null');
    await expectRefused({ root: records({ [REGISTRY_GIT_SOURCE_ACT_FORM.artifact]: unknown, [REGISTRY_ACT]: renderRegistryAct(sha(unknown), '2026-10-05', '2026-10-05T09:30:00Z') }) },
      'start-gates', 'a start gate is not in force: source-acquisition registry entry: the registry entry bound by PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-2026-10-05 has no implementation version (Unknown), so RFC4-3 admits no output from it', false);
  });

  it.each([
    ['absent', { [POLICY_ACT]: null }, 'a start gate is not in force: classification and screening policy: no screening-scope policy act is recorded'],
    ['ineffective: the policy changed after the act', { [POLICY_PATH]: POLICY.replace('fixture', 'edited') }, 'a start gate is not in force: classification and screening policy: the policy bytes differ from the in-force act\'s argument'],
  ])('refuses before any object read when the classification and screening policy is %s', async (_name, over, reason) => {
    await expectRefused({ root: records(over) }, 'start-gates', reason, false);
  });

  it('names every failed start gate, not only the first', async () => {
    const run = await init({ root: records({ [REGISTRY_ACT]: null, [POLICY_ACT]: null }) });
    expect(refusal(run.result)?.startGates).toMatchObject({ registryEntry: { state: 'absent' }, screeningPolicy: { state: 'absent' } });
  });

  it('refuses a HEAD the consent does not name, before any object read, listing the consented revisions', async () => {
    await expectRefused({ clone: cloneAt(commits.U) }, 'revision', `the clone's HEAD ${commits.U} (detached HEAD) is not a revision the in-force observation consent for redis-redis names: no record found: no owner act puts a observation-consent for redis-redis in force at revision ${commits.U}`, false);
    const run = await init({ clone: cloneAt(commits.U) });
    expect(refusal(run.result)?.consentedRevisions).toEqual([{ label: 'fixture-a', commit: commits.A }, { label: 'fixture-b', commit: commits.B }, { label: 'fixture-c', commit: commits.C }]);
  });

  it('refuses a clone whose .git is a gitdir pointer', async () => {
    const clone = tempDir('dossier-pointer-');
    fs.writeFileSync(path.join(clone, '.git'), `gitdir: ${path.join(cloneAt(commits.A), '.git')}\n`);
    await expectRefused({ clone }, 'head', `${path.join(clone, '.git')} is not a directory (a gitdir pointer is refused, never followed); use a plain clone`, false);
  });

  it('refuses a listing whose object no longer hashes to its identifier (scenario "Object store altered after pinning")', async () => {
    const clone = cloneAt(commits.A);
    // The clone keeps the origin's loose objects (copied, never hardlinked): overwrite the pinned commit's file with commit B's bytes.
    const looseOf = (id: string): string => path.join(clone, '.git', 'objects', id.slice(0, 2), id.slice(2));
    expect(fs.existsSync(looseOf(commits.A)) && fs.existsSync(looseOf(commits.B))).toBe(true);
    fs.chmodSync(looseOf(commits.A), 0o644);
    fs.copyFileSync(looseOf(commits.B), looseOf(commits.A));
    const run = await init({ clone });
    expect(refusal(run.result)?.stage).toBe('listing');
    expect(refusal(run.result)?.objectRead).toMatchObject({ reason: 'identifier-mismatch', objectId: commits.A });
    expect(refusal(run.result)?.objectsRead).toBe(true);
    expect(fs.existsSync(run.stateRoot)).toBe(false);
  });

  it.each([
    ['a .syzygy/ path, not adopted', 'B' as const, NO_DRAWER, 'governed'],
    ['an openspec/ path', 'C' as const, NO_DRAWER, 'governed'],
    ['a recorded kernel evidence drawer', 'A' as const, DRAWER, 'governed'],
    ['a project input that does not say', 'A' as const, { drawerFor: async () => ({ stated: false, why: 'no admitted project input record (REQ-polaris-generation-001) for this subject exists, so whether a kernel evidence drawer exists is not stated' }) } as ProjectInputSource, 'unstated'],
  ])('refuses a subject with %s and no per-project statement, after listing the pinned tree', async (_name, commit, projectInput, kind) => {
    await expectRefused({ clone: cloneAt(commits[commit]), projectInput }, 'statement', `the subject is ${kind} and the per-project statement is missing: no per-project statement names the operator's agent provider anthropic`, true);
  });

  it('treats the production project input as silent: with no statement every subject is refused', async () => {
    const root = records();
    const sources = createPackageGateSources({ root, now: () => NOW });
    const result = await initRun({ clone: cloneAt(commits.A), url: URL_, configText: CONFIG, stateRoot: path.join(tempDir('dossier-state-'), 'runs') }, { sources, now: () => NOW });
    expect(refusal(result)).toMatchObject({ stage: 'statement', governed: { kind: 'unstated' } });
  });

  it.each([
    ['names another provider', { ...STATEMENT, provider: 'openai' }],
    ['is withdrawn', { ...STATEMENT, withdrawn: true }],
    ['has no act', { ...STATEMENT, act: null }],
  ])('refuses a governed subject whose only statement %s', async (_name, statement) => {
    const run = await init({ clone: cloneAt(commits.B), providerStatements: statements(statement) });
    expect(refusal(run.result)?.stage).toBe('statement');
  });

  it('starts a governed or unstated run that relies on an in-force statement, and cites it', async () => {
    const governed = await init({ clone: cloneAt(commits.B), providerStatements: statements(STATEMENT) });
    expect(governed.result.ok && governed.result.report.subject.providerStatement).toBe('STATEMENT-REDIS-ANTHROPIC@1');
    expect(governed.result.ok && governed.result.report.subject.governed.kind).toBe('governed');
    const silent = await init({ projectInput: { drawerFor: async () => ({ stated: false, why: 'silent' }) }, providerStatements: statements(STATEMENT) });
    expect(silent.result.ok && silent.result.report.subject.governed.kind).toBe('unstated');
  });

  it.each([
    ['a URL with a ref', { url: 'https://github.com/redis/redis/tree/8.0.0' }, 'url'],
    ['a URL on another host', { url: 'https://gitlab.com/redis/redis' }, 'url'],
    ['a configuration with an unlimited limit', { config: CONFIG.replace('"maxRepairCycles":2', '"maxRepairCycles":"unlimited"') }, 'config'],
    ['a relative state root', { stateRoot: 'runs' }, 'state-root'],
  ])('refuses %s before reading anything', async (_name, setup, stage) => {
    const run = await init(setup);
    expect(refusal(run.result)?.stage).toBe(stage);
    expect(run.readerOpened).toBe(false);
  });

  it('refuses a state root inside the clone, or one that contains it', async () => {
    const clone = cloneAt(commits.A);
    expect(refusal((await init({ clone, stateRoot: path.join(clone, 'runs') })).result)?.stage).toBe('state-root');
    expect(refusal((await init({ clone, stateRoot: path.dirname(clone) })).result)?.stage).toBe('state-root');
    expect(fs.existsSync(path.join(clone, 'runs'))).toBe(false);
  });
});

describe('reverifyPinnedRevision: the guard every later step calls (scenario "Recorded revision altered")', () => {
  const started = async (setup: Setup = {}) => {
    const run = await init(setup);
    if (!run.result.ok) throw new Error(`fixture run refused: ${JSON.stringify(run.result.refusal)}`);
    return { ...run, runDir: run.result.report.run };
  };
  const guard = (runDir: string, root: string, over: { providerStatements?: ProviderStatementSource; now?: number } = {}) =>
    reverifyPinnedRevision(runDir, createPackageGateSources({ root, now: () => over.now ?? NOW, ...(over.providerStatements ? { providerStatements: over.providerStatements } : {}) }), over.now ?? NOW);
  const rewritePin = (runDir: string, commit: string): void => {
    const file = path.join(runDir, 'run.json');
    const record = JSON.parse(fs.readFileSync(file, 'utf8')) as { subject: { pinnedRevision: { commit: string } } };
    record.subject.pinnedRevision.commit = commit;
    fs.writeFileSync(file, JSON.stringify(record, null, 2));
  };

  it('passes while every gate stays in force', async () => {
    const { runDir, root } = await started();
    expect(await guard(runDir, root)).toMatchObject({ ok: true, consentRecord: 'PUBLIC-OBS-REDIS-2026-10-03@0.1.0-candidate.7' });
  });

  it('refuses when the recorded pin is changed to a commit in the clone the consent does not name', async () => {
    const { runDir, root } = await started();
    rewritePin(runDir, commits.U);
    const result = await guard(runDir, root);
    expect(result.ok).toBe(false);
    expect(!result.ok && result.reasons).toEqual([`the recorded pinned revision ${commits.U} is not a revision the in-force observation consent for redis-redis names: no record found: no owner act puts a observation-consent for redis-redis in force at revision ${commits.U}`]);
  });

  it('refuses when the consent stops naming the recorded revision', async () => {
    const { runDir, root } = await started();
    const narrowed = consentText([['fixture-b', commits.B]]);
    fs.writeFileSync(path.join(root, CONSENT_PATH), narrowed);
    fs.writeFileSync(path.join(root, CONSENT_ACT), renderRecorderAct('redis-observation', sha(narrowed), '2026-10-06', '2026-10-06T09:30:00Z'));
    const result = await guard(runDir, root);
    expect(!result.ok && result.reasons.length).toBe(1);
    expect(!result.ok && result.reasons[0]).toContain(`the recorded pinned revision ${commits.A} is not a revision the in-force observation consent for redis-redis names`);
  });

  it.each([
    ['the observation consent is withdrawn', (root: string) => fs.writeFileSync(path.join(root, DECISIONS_DIR, 'PUBLIC-OBS-REDIS-WITHDRAWAL.md'), 'Withdrawn: PUBLIC-OBS-REDIS-2026-10-03.\n'), 2],
    ['the registry entry is withdrawn', (root: string) => fs.writeFileSync(path.join(root, DECISIONS_DIR, 'PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-REVOCATION.md'), 'Revoked.\n'), 1],
    ['the policy changes after its act', (root: string) => fs.writeFileSync(path.join(root, POLICY_PATH), POLICY.replace('fixture', 'edited')), 1],
  ])('refuses every later step when %s', async (_name, mutate, count) => {
    const { runDir, root } = await started();
    mutate(root);
    const result = await guard(runDir, root);
    expect(result.ok).toBe(false);
    expect(!result.ok && result.reasons.length).toBe(count);
  });

  it('refuses when the statement a governed run relies on is withdrawn mid-run', async () => {
    const { runDir, root } = await started({ clone: cloneAt(commits.B), providerStatements: statements(STATEMENT) });
    expect((await guard(runDir, root, { providerStatements: statements(STATEMENT) })).ok).toBe(true);
    const result = await guard(runDir, root, { providerStatements: statements({ ...STATEMENT, withdrawn: true }) });
    expect(!result.ok && result.reasons).toEqual(['the per-project statement STATEMENT-REDIS-ANTHROPIC@1 the run relies on is no longer in force: no per-project statement naming anthropic is in force: STATEMENT-REDIS-ANTHROPIC@1 is withdrawn']);
  });

  it('refuses a run record altered into an invalid shape', async () => {
    const { runDir, root } = await started();
    rewritePin(runDir, 'not-a-commit');
    expect(await guard(runDir, root)).toEqual({ ok: false, reasons: ['run.json subject is invalid: the pinned commit is not a full commit identifier'] });
  });

  it('accepts a pin moved to another consented revision: that the draft, inventory and verdict name the pinned revision is the later steps\' check', async () => {
    const { runDir, root } = await started();
    rewritePin(runDir, commits.C);
    expect((await guard(runDir, root)).ok).toBe(true);
  });
});

describe('preflight', () => {
  const run = (root: string, input = URL_, now = NOW) => preflight(input, createPackageGateSources({ root, now: () => now }), now);
  it('reports a ready repository, its consented revisions and the clone commands, reading no object', async () => {
    const result = await run(records());
    expect(result.ok).toBe(true);
    if (!result.ok) return;
    expect(result.report).toMatchObject({
      outcome: 'ready',
      url: URL_,
      repository: { repositoryId: 'redis-redis' },
      consentedRevisions: [{ label: 'fixture-a', commit: commits.A }, { label: 'fixture-b', commit: commits.B }, { label: 'fixture-c', commit: commits.C }],
      startGates: { registryEntry: { state: 'ok', record: 'PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-2026-10-05' }, screeningPolicy: { state: 'ok' } },
      missing: [],
      cloneCommands: [`git clone ${URL_} <dir>`, `git -C <dir> checkout --detach ${commits.A}   # fixture-a`, `git -C <dir> checkout --detach ${commits.B}   # fixture-b`, `git -C <dir> checkout --detach ${commits.C}   # fixture-c`],
    });
  });
  it('names each missing record and is not ready', async () => {
    const result = await run(records({ [CONSENT_ACT]: null, [POLICY_ACT]: null }));
    expect(result.ok && result.report.outcome).toBe('not-ready');
    expect(result.ok && result.report.missing).toEqual([
      'observation consent: no observation consent in force names https://github.com/redis/redis as its Upstream',
      'classification and screening policy: no screening-scope policy act is recorded',
    ]);
  });
  it('reports D9 and the RFC7-20 reading as not established: no owner-act record binds their digests', async () => {
    const result = await run(records());
    const why = (what: string) => `no owner-act record binds a digest of ${what}, so the act cross-check of RFC3-16(a) cannot establish it in force; a status word, a log row or a file's presence is not read as one`;
    expect(result.ok && result.report.d9).toEqual({ state: 'absent', why: why('the D9 text (SEC-3 amendment)') });
    expect(result.ok && result.report.rfc720Ruling).toEqual({ state: 'absent', why: why('the RFC7-20 reading (POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05, item 1)') });
  });
  it('reports D9 not established on this checkout, though the doctrine amendment log records its adoption', async () => {
    expect(fs.readFileSync(path.join(REAL_ROOT, DECISIONS_DIR, 'DOCTRINE-AMENDMENT-LOG.md'), 'utf8')).toMatch(/^\| D9 \|/m);
    const result = await preflight(URL_, createPackageGateSources({ root: REAL_ROOT, now: () => Date.now() }), Date.now());
    expect(result.ok && result.report.d9.state).toBe('absent');
    expect(result.ok && result.report.rfc720Ruling.state).toBe('absent');
  });
  it('would establish D9 through the same cross-check once an act form exists, and only while the act binds the bytes', async () => {
    const root = records();
    const d9 = (r: string) => createPackageGateSources({ root: r, now: () => NOW, d9Form: REGISTRY_GIT_SOURCE_ACT_FORM }).d9();
    expect(await d9(root)).toEqual({ state: 'ok', record: 'PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-2026-10-05' });
    fs.writeFileSync(path.join(root, REGISTRY_GIT_SOURCE_ACT_FORM.artifact), `${ENTRY}\n`);
    expect((await d9(root)).state).toBe('refused');
  });
  it('refuses a URL it cannot parse, and never fetches', async () => {
    expect(await run(records(), 'https://github.com/redis/redis/tree/unstable')).toMatchObject({ ok: false });
  });
});

describe('the CLI: preflight and init', () => {
  const cli = async (argv: readonly string[], root: string, env: Record<string, string> = {}, projectInput: ProjectInputSource = NO_DRAWER) => {
    let stdout = '';
    let stderr = '';
    const sources = createPackageGateSources({ root, now: () => NOW, projectInput });
    const code = await runDossierCli(argv, { stdout: t => { stdout += t; }, stderr: t => { stderr += t; } }, { env, now: () => NOW, sources });
    return { code, stdout, stderr };
  };
  const configFile = (): string => { const file = path.join(tempDir('dossier-config-'), 'run.json'); fs.writeFileSync(file, CONFIG); return file; };

  it('init refuses with no state root, there being no default', async () => {
    const clone = cloneAt(commits.A);
    const result = await cli(['init', clone, '--url', URL_, '--config', configFile(), '--json'], records());
    expect(result.code).toBe(1);
    expect(JSON.parse(result.stdout)).toEqual({ command: 'init', outcome: 'refused', stage: 'state-root', reason: 'no state root: pass --state-root <dir> or set SYZYGY_DOSSIER_STATE_ROOT; there is no default, and none is derived from the clone', objectsRead: false });
  });
  it('init takes the state root from the environment when no flag is given, and the flag over the environment', async () => {
    const fromEnv = path.join(tempDir('dossier-state-'), 'env');
    const viaEnv = await cli(['init', cloneAt(commits.A), '--url', URL_, '--config', configFile(), '--json'], records(), { SYZYGY_DOSSIER_STATE_ROOT: fromEnv });
    expect(viaEnv.code).toBe(0);
    expect(JSON.parse(viaEnv.stdout).run.startsWith(`${fromEnv}/run-`)).toBe(true);
    const fromFlag = path.join(tempDir('dossier-state-'), 'flag');
    const viaFlag = await cli(['init', cloneAt(commits.A), '--url', URL_, '--config', configFile(), '--state-root', fromFlag, '--json'], records(), { SYZYGY_DOSSIER_STATE_ROOT: fromEnv });
    expect(JSON.parse(viaFlag.stdout).run.startsWith(`${fromFlag}/run-`)).toBe(true);
  });
  it('init refuses a missing configuration file and prints the refusal in both forms', async () => {
    const missing = path.join(tempDir('dossier-config-'), 'absent.json');
    const result = await cli(['init', cloneAt(commits.A), '--url', URL_, '--config', missing, '--state-root', path.join(tempDir('s-'), 'r'), '--json'], records());
    expect(result.code).toBe(1);
    expect(JSON.parse(result.stdout)).toMatchObject({ stage: 'config', reason: `${missing} cannot be read (ENOENT)` });
    expect(result.stderr).toContain('stage: config\n');
  });
  it.each([
    [['init'], 'init takes exactly one positional argument, the clone directory'],
    [['init', '/c'], 'init requires --url <url> and --config <run.json>'],
    [['init', '/c', '--url'], '--url requires a value'],
    [['init', '/c', '--url', 'u', '--url', 'v'], '--url given more than once'],
    [['init', '/c', '--force'], 'unknown option: --force'],
    [['preflight'], 'preflight takes exactly one argument, the repository URL'],
    [['preflight', URL_, '--provider'], 'unknown option for preflight: --provider'],
  ])('exits 2 for %j', async (argv, detail) => {
    const result = await cli(argv, records());
    expect(result.code).toBe(2);
    expect(result.stderr.startsWith(`syzygy dossier: ${detail}\n`)).toBe(true);
  });
  it('preflight exits 0 when ready and 1 when a record is missing, printing the report on stdout both times', async () => {
    const ready = await cli(['preflight', URL_, '--json'], records());
    expect(ready.code).toBe(0);
    expect(JSON.parse(ready.stdout).outcome).toBe('ready');
    const missing = await cli(['preflight', URL_], records({ [REGISTRY_ACT]: null }));
    expect(missing.code).toBe(1);
    expect(missing.stdout).toContain('outcome: not-ready\n');
    expect(missing.stdout).toMatch(/^missing\.0: source-acquisition registry entry: no owner-act record /m);
  });
});
