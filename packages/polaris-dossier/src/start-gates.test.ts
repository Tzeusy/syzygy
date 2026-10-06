import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { DECISIONS_DIR, INSTANCES_DIR, LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM, POLICY_PATH } from '@syzygy/polaris-generation-consent';
import { renderDossierLocalAgentAct, renderLocalAgentSignoff, renderPolicyAct, renderRecorderAct } from '@syzygy/polaris-generation-consent/testing';
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

// The clone: commit A (plain), commit B (adds a .syzygy/ path), commit C (adds an openspec/ path), commit U (never consented by the
// default records), and off A, commits S (a symlink entry named .syzygy), G (a gitlink entry named openspec) and A2 (plain).
let origin: string;
const commits: Record<'A' | 'B' | 'C' | 'U' | 'S' | 'G' | 'A2', string> = { A: '', B: '', C: '', U: '', S: '', G: '', A2: '' };
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
  // Off commit A, each on its own branch so a clone carries it: S adds a symlink entry named .syzygy, G a gitlink entry named openspec.
  const entryCommit = (branch: string, add: () => void, message: string): string => {
    git('checkout', '-q', '-b', branch, commits.A);
    add();
    git('-c', 'user.name=t', '-c', 'user.email=t@example.invalid', 'commit', '-q', '-m', message);
    const id = git('rev-parse', 'HEAD');
    git('checkout', '-q', 'main');
    return id;
  };
  commits.S = entryCommit('symlink', () => { fs.symlinkSync('src', path.join(origin, '.syzygy')); git('add', '.syzygy'); }, 'symlink .syzygy');
  commits.G = entryCommit('gitlink', () => git('update-index', '--add', '--cacheinfo', `160000,${commits.U},openspec`), 'gitlink openspec');
  commits.A2 = entryCommit('plain', () => { fs.writeFileSync(path.join(origin, 'src', 'util.c'), 'int util(void) { return 1; }\n'); git('add', 'src/util.c'); }, 'src/util.c');
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
const ENTRY_PATH = LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.installed;
const REGISTRY_ACT = `${DECISIONS_DIR}/${LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM.file}`;
const POLICY_ACT = `${DECISIONS_DIR}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`;

/** The local-agent entry's v1.0 sign-off record as the recorder renders it over `entry` installed. */
const signoffs = new Map<string, string>();
const signoffOver = (entry: string): string => {
  const hit = signoffs.get(entry);
  if (hit !== undefined) return hit;
  const scratch = tempDir('dossier-signoff-');
  fs.mkdirSync(path.dirname(path.join(scratch, ENTRY_PATH)), { recursive: true });
  fs.writeFileSync(path.join(scratch, ENTRY_PATH), entry);
  const text = renderLocalAgentSignoff(scratch, '2026-10-05', '2026-10-05T09:30:00Z');
  signoffs.set(entry, text);
  return text;
};

/** The records every gate needs, in force at NOW; `over` replaces or (with null) removes a file, `rows` replaces the consented revisions. */
const records = (over: Record<string, string | null> = {}, rows?: readonly [string, string][]): string => {
  const consent = consentText(rows ?? [['fixture-a', commits.A], ['fixture-b', commits.B], ['fixture-c', commits.C]]);
  const files: Record<string, string | null> = {
    [CONSENT_PATH]: consent,
    [CONSENT_ACT]: renderRecorderAct('redis-observation', sha(consent), '2026-10-04', '2026-10-04T09:30:00Z'),
    [ENTRY_PATH]: ENTRY,
    [REGISTRY_ACT]: signoffOver(ENTRY),
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
  recordId: 'STATEMENT-REDIS-ANTHROPIC', version: '1', digest: 'a'.repeat(64), agentTool: 'claude-code', provider: 'anthropic', contentClasses: ['code-content'],
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
      clone: { path: clone, declaredBy: 'operator', label: 'Inferred', use: 'read' },
      pinnedRevision: { commit: commits.A, label: 'fixture-a', consentRecord: 'PUBLIC-OBS-REDIS-2026-10-03@0.1.0-candidate.7', pinnedAt: '2026-10-07T12:00:00.000Z' },
      startGates: { registryEntry: 'public-git-source-acquisition-local-agent-v1.0', screeningPolicy: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-04' },
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

  it('records the clone by its real path, not the path typed: a symlink or a `..` segment is resolved (R-POLARIS-DOSSIER-S3-GATES-2 note 12)', async () => {
    const clone = cloneAt(commits.A);
    const link = path.join(tempDir('dossier-clone-link-'), 'via-link');
    fs.symlinkSync(clone, link);
    const linked = await init({ clone: link });
    expect(linked.result.ok && linked.result.report.subject.clone.path).toBe(clone);
    const dotted = await init({ clone: path.join(clone, 'src', '..') });
    expect(dotted.result.ok && dotted.result.report.subject.clone.path).toBe(clone);
  });

  it('records the clone by its real path when the operator names it through a symbolic link', async () => {
    const clone = cloneAt(commits.A);
    const link = path.join(tempDir('dossier-link-'), 'via');
    fs.symlinkSync(clone, link);
    const { result } = await init({ clone: link });
    expect(result.ok && result.report.subject.clone).toEqual({ path: fs.realpathSync(clone), declaredBy: 'operator', label: 'Inferred', use: 'read' });
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

  const NO_RECORD = 'no observation record names https://github.com/redis/redis as its Upstream';
  // The admission reader defines no withdrawal form: a decisions file naming the record refuses the whole read rather than be parsed.
  const UNREADABLE = 'the admission act records could not be read (invalid-records), so no consent can be established';
  const recordIs = (text: string): string => `the observation record(s) naming https://github.com/redis/redis are not in force: PUBLIC-OBS-REDIS-2026-10-03@0.1.0-candidate.7 ${text}`;
  it.each([
    ['absent: no act record', { [CONSENT_ACT]: null }, NO_RECORD],
    ['ineffective: the consent bytes changed after the act', { [CONSENT_PATH]: `${consentText([['fixture-a', '0'.repeat(40)]])}` }, recordIs('has no owner act in force over its current bytes')],
    ['not in force yet', {}, recordIs('is not in force yet')],
    ['withdrawn: another decisions file names the record', { [`${DECISIONS_DIR}/PUBLIC-OBS-REDIS-WITHDRAWAL.md`]: 'The owner withdraws PUBLIC-OBS-REDIS-2026-10-03.\n' }, UNREADABLE],
    ['present only as status words in the record, no act (F8)', { [CONSENT_ACT]: null, [CONSENT_PATH]: consentText([['fixture-a', '0'.repeat(40)]], '\nStatus: accepted; in force; adopted by the owner\n') }, NO_RECORD],
  ])('refuses before any object read when the observation consent is %s, naming why', async (name, over, why) => {
    // An ineffective consent's act names other bytes, so it keeps the original act over the original text.
    const root = name.startsWith('ineffective') ? (() => { const r = records(); fs.writeFileSync(path.join(r, CONSENT_PATH), consentText([['fixture-a', commits.A]], '\n<!-- edited -->\n')); return r; })() : records(over);
    await expectRefused({ root, ...(name === 'not in force yet' ? { now: Date.UTC(2026, 9, 4, 9, 29, 59) } : {}) }, 'repository', `no observation consent in force names https://github.com/redis/redis as its Upstream: ${why}`, false);
  });

  it.each([
    ['absent', { [REGISTRY_ACT]: null }, /^a start gate is not in force: source-acquisition registry entry: no owner-act record .*PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1\.0\.md exists$/],
    ['ineffective: the entry changed after the sign-off', { [ENTRY_PATH]: ENTRY.replace('0.1.0', '0.2.0') }, /^a start gate is not in force: source-acquisition registry entry: the bytes of .* differ from the SHA-256 the sign-off records$/],
    ['withdrawn: another decisions file names it', { [`${DECISIONS_DIR}/PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-REVOCATION.md`]: 'Revoked.\n' }, /^a start gate is not in force: source-acquisition registry entry: .*names the act without being its record/],
    ['present only as a status word in the entry, no act (F8)', { [REGISTRY_ACT]: null, [ENTRY_PATH]: JSON.stringify({ status: 'in force', entries: [] }) }, /no owner-act record/],
  ])('refuses before any object read when the registry entry is %s', async (_name, over, reason) => {
    await expectRefused({ root: records(over) }, 'start-gates', reason, false);
  });

  it('refuses when the signed registry entry names another implementation or no implementation version', async () => {
    const other = ENTRY.replace('"polaris-dossier/git-object-reader"', '"polaris-generation/public-git-source-acquisition"');
    await expectRefused({ root: records({ [ENTRY_PATH]: other, [REGISTRY_ACT]: signoffOver(other) }) },
      'start-gates', 'a start gate is not in force: source-acquisition registry entry: the registry entry bound by public-git-source-acquisition-local-agent-v1.0 names the implementation "polaris-generation/public-git-source-acquisition", not polaris-dossier/git-object-reader', false);
    const unknown = ENTRY.replace('"0.1.0"', 'null');
    await expectRefused({ root: records({ [ENTRY_PATH]: unknown, [REGISTRY_ACT]: signoffOver(unknown) }) },
      'start-gates', 'a start gate is not in force: source-acquisition registry entry: the registry entry bound by public-git-source-acquisition-local-agent-v1.0 has no implementation version (Unknown), so RFC4-3 admits no output from it', false);
  });

  it.each([
    ['absent', { [POLICY_ACT]: null }, 'a start gate is not in force: classification and screening policy: no screening-scope policy act is recorded'],
    ['ineffective: the policy changed after the act', { [POLICY_PATH]: POLICY.replace('fixture', 'edited') }, 'a start gate is not in force: classification and screening policy: the policy bytes differ from the in-force act\'s argument'],
  ])('refuses before any object read when the classification and screening policy is %s', async (_name, over, reason) => {
    await expectRefused({ root: records(over) }, 'start-gates', reason, false);
  });

  // The consent arm refuses first, at stage repository, before the registry and policy are read; preflight reports all three.
  it('names both the registry entry and the policy when both fail, not only the first', async () => {
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
    await expectRefused({ clone: cloneAt(commits[commit]), projectInput }, 'statement', `the subject is ${kind} and the per-project statement is missing: no per-project statement names the operator's agent tool claude-code with the provider anthropic`, true);
  });

  it.each([
    ['a symlink entry named .syzygy', 'S' as const, 'the pinned tree lists 1 path(s) under a .syzygy/ directory, counted adopted or not'],
    ['a gitlink entry named openspec', 'G' as const, 'the pinned tree lists 1 path(s) under an openspec/ directory'],
  ])('counts %s in the pinned tree as governing', async (_name, commit, because) => {
    const root = records({}, [['fixture-a', commits.A], [`fixture-${commit.toLowerCase()}`, commits[commit]]]);
    const run = await init({ root, clone: cloneAt(commits[commit]) });
    expect(refusal(run.result)).toMatchObject({ stage: 'statement', governed: { kind: 'governed', because: [because] } });
    const started = await init({ root, clone: cloneAt(commits[commit]), providerStatements: statements(STATEMENT) });
    expect(started.result.ok && started.result.report.subject.governed).toEqual({ kind: 'governed', because: [because] });
  });

  it('treats the production project input as silent: with no statement every subject is refused', async () => {
    const root = records();
    const sources = createPackageGateSources({ root, now: () => NOW });
    const result = await initRun({ clone: cloneAt(commits.A), url: URL_, configText: CONFIG, stateRoot: path.join(tempDir('dossier-state-'), 'runs') }, { sources, now: () => NOW });
    expect(refusal(result)).toMatchObject({ stage: 'statement', governed: { kind: 'unstated' } });
  });

  it.each([
    ['names another provider', { ...STATEMENT, provider: 'openai' }],
    ['names the provider for another agent tool', { ...STATEMENT, agentTool: 'codex' }],
    ['is withdrawn', { ...STATEMENT, withdrawn: true }],
    ['has no act', { ...STATEMENT, act: null }],
  ])('refuses a governed subject whose only statement %s', async (_name, statement) => {
    const run = await init({ clone: cloneAt(commits.B), providerStatements: statements(statement) });
    expect(refusal(run.result)?.stage).toBe('statement');
  });

  it('refuses a Codex run with Anthropic against the Claude Code statement: consent is to the declared tool and provider pair', async () => {
    const config = JSON.stringify({ ...JSON.parse(CONFIG), agentTool: 'codex', agentToolVersion: '0.40.0' });
    const run = await init({ clone: cloneAt(commits.B), config, providerStatements: statements(STATEMENT) });
    expect(refusal(run.result)).toMatchObject({ stage: 'statement', reason: 'the subject is governed and the per-project statement is missing: no per-project statement names the operator\'s agent tool codex with the provider anthropic (STATEMENT-REDIS-ANTHROPIC@1 names claude-code with anthropic)' });
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
  interface GuardOver { projectInput?: ProjectInputSource; providerStatements?: ProviderStatementSource; now?: number; opened?: string[] }
  /** The guard with the project input the fixture run started under (NO_DRAWER) unless `over` names another. */
  const guard = (runDir: string, root: string, over: GuardOver = {}) =>
    reverifyPinnedRevision(
      runDir,
      createPackageGateSources({ root, now: () => over.now ?? NOW, projectInput: over.projectInput ?? NO_DRAWER, ...(over.providerStatements ? { providerStatements: over.providerStatements } : {}) }),
      over.now ?? NOW,
      { openReader: (o: PinnedObjectReaderOptions) => { over.opened?.push(o.revision); return openPinnedObjectReader(o); } },
    );
  const editSubject = (runDir: string, edit: (subject: Record<string, any>) => void): void => {
    const file = path.join(runDir, 'run.json');
    const record = JSON.parse(fs.readFileSync(file, 'utf8')) as { subject: Record<string, any> };
    edit(record.subject);
    fs.writeFileSync(file, JSON.stringify(record, null, 2));
  };
  const editDeclared = (runDir: string, edit: (declared: Record<string, any>) => void): void => {
    const file = path.join(runDir, 'run.json');
    const record = JSON.parse(fs.readFileSync(file, 'utf8')) as { declared: Record<string, any> };
    edit(record.declared);
    fs.writeFileSync(file, JSON.stringify(record, null, 2));
  };
  const writeBriefRecord = (runDir: string, agent: unknown): void =>
    fs.writeFileSync(path.join(runDir, 'brief.json'), JSON.stringify({ format: 'polaris-dossier-brief/1', ...(agent === undefined ? {} : { agent }), label: 'Inferred' }));
  const rewritePin = (runDir: string, commit: string): void => editSubject(runDir, (subject) => { subject['pinnedRevision']['commit'] = commit; });
  const codes = (result: Awaited<ReturnType<typeof guard>>) => (result.ok ? [] : result.refusals.map(r => r.code));
  const DISCLOSED = [
    'the consent, registry, policy and statement records the gates read lie in Syzygy\'s checkout, which the agent sessions can write; Syzygy re-reads and re-checks them at every step, and cannot rule out that a session changed them',
    'the run record names the repository, the clone and the pinned commit to look at; whether that commit is consented, whether the subject is governed and whether a per-project statement is in force were decided again at this step from the records in force now and the pinned tree listed now',
    'which per-project statement applies is selected by the agent provider the run record declares: that provider, the statement citation it selects and the clone location are Inferred and lie within the agent sessions\' write reach; a tool or provider that differs from the one the brief record states refuses, but the brief record lies within the same reach, so an edit of both records together is not detected',
  ];
  const CONSENT_RECORD = 'PUBLIC-OBS-REDIS-2026-10-03@0.1.0-candidate.7';

  it('passes while every gate stays in force, listing the pinned tree from the recorded clone and deciding the subject again', async () => {
    const { runDir, root } = await started();
    const opened: string[] = [];
    const result = await guard(runDir, root, { opened });
    expect(result).toMatchObject({
      ok: true,
      consentRecord: CONSENT_RECORD,
      revision: { commit: commits.A, label: 'fixture-a', consentRecord: CONSENT_RECORD },
      governed: { kind: 'non-governed', statementRequired: false },
      providerStatement: null,
      disclosures: DISCLOSED,
    });
    expect(opened).toEqual([commits.A]);
  });

  it('reads no object when a gate fails', async () => {
    const { runDir, root } = await started();
    fs.writeFileSync(path.join(root, DECISIONS_DIR, 'PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-REVOCATION.md'), 'Revoked.\n');
    const opened: string[] = [];
    expect(codes(await guard(runDir, root, { opened }))).toEqual(['registry']);
    expect(opened).toEqual([]);
  });

  it('shows the label and consent record the live consent gives, never the run record\'s (R-POLARIS-DOSSIER-S3-GATES-1 finding 2)', async () => {
    const { runDir, root } = await started();
    editSubject(runDir, (subject) => { subject['pinnedRevision']['label'] = 'forged'; subject['pinnedRevision']['consentRecord'] = 'FORGED@1'; });
    expect(await guard(runDir, root)).toMatchObject({ ok: true, consentRecord: CONSENT_RECORD, revision: { commit: commits.A, label: 'fixture-a', consentRecord: CONSENT_RECORD } });
    const relabelled = consentText([['fixture-a-renamed', commits.A]]);
    fs.writeFileSync(path.join(root, CONSENT_PATH), relabelled);
    fs.writeFileSync(path.join(root, CONSENT_ACT), renderRecorderAct('redis-observation', sha(relabelled), '2026-10-06', '2026-10-06T09:30:00Z'));
    expect(await guard(runDir, root)).toMatchObject({ ok: true, revision: { label: 'fixture-a-renamed' } });
  });

  it('refuses when the pinned tree cannot be listed from the recorded clone', async () => {
    const { runDir, root, clone } = await started();
    fs.rmSync(path.join(clone, '.git', 'objects'), { recursive: true, force: true });
    const result = await guard(runDir, root);
    expect(codes(result)).toEqual(['listing']);
    expect(!result.ok && result.objectRead).toBeDefined();
  });

  it('refuses when the recorded pin is changed to a commit in the clone the consent does not name', async () => {
    const { runDir, root } = await started();
    rewritePin(runDir, commits.U);
    const result = await guard(runDir, root);
    expect(result.ok).toBe(false);
    expect(!result.ok && result.refusals).toEqual([{ code: 'revision-unnamed', reason: `the recorded pinned revision ${commits.U} is not a revision the in-force observation consent for redis-redis names: no record found: no owner act puts a observation-consent for redis-redis in force at revision ${commits.U}` }]);
  });

  it('refuses when the consent stops naming the recorded revision', async () => {
    const { runDir, root } = await started();
    const narrowed = consentText([['fixture-b', commits.B]]);
    fs.writeFileSync(path.join(root, CONSENT_PATH), narrowed);
    fs.writeFileSync(path.join(root, CONSENT_ACT), renderRecorderAct('redis-observation', sha(narrowed), '2026-10-06', '2026-10-06T09:30:00Z'));
    const result = await guard(runDir, root);
    expect(codes(result)).toEqual(['revision-unnamed']);
    expect(!result.ok && result.reasons[0]).toContain(`the recorded pinned revision ${commits.A} is not a revision the in-force observation consent for redis-redis names`);
  });

  it.each([
    ['the observation consent is withdrawn', (root: string) => fs.writeFileSync(path.join(root, DECISIONS_DIR, 'PUBLIC-OBS-REDIS-WITHDRAWAL.md'), 'Withdrawn: PUBLIC-OBS-REDIS-2026-10-03.\n'), ['consent-ids', 'revision-unnamed']],
    ['the registry entry is withdrawn', (root: string) => fs.writeFileSync(path.join(root, DECISIONS_DIR, 'PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-REVOCATION.md'), 'Revoked.\n'), ['registry']],
    ['the policy changes after its act', (root: string) => fs.writeFileSync(path.join(root, POLICY_PATH), POLICY.replace('fixture', 'edited')), ['policy']],
  ])('refuses every later step when %s', async (_name, mutate, expected) => {
    const { runDir, root } = await started();
    mutate(root);
    const result = await guard(runDir, root);
    expect(result.ok).toBe(false);
    expect(codes(result)).toEqual(expected);
    expect(!result.ok && result.reasons).toEqual(!result.ok && result.refusals.map(r => r.reason));
  });

  it.each([
    ['a withdrawal in a form the reader does not define refuses the whole read', (root: string) => fs.writeFileSync(path.join(root, DECISIONS_DIR, 'PUBLIC-OBS-REDIS-WITHDRAWAL.md'), 'Withdrawn: PUBLIC-OBS-REDIS-2026-10-03.\n'),
      'the admission act records could not be read (invalid-records), so no consent can be established'],
    ['the consent bytes changed after the act', (root: string) => fs.appendFileSync(path.join(root, CONSENT_PATH), '\n<!-- edited -->\n'),
      `the observation record(s) naming ${URL_} are not in force: ${CONSENT_RECORD} has no owner act in force over its current bytes`],
    ['the act record removed', (root: string) => fs.rmSync(path.join(root, CONSENT_ACT)), `no observation record names ${URL_} as its Upstream`],
  ])('names why the consent is gone when %s', async (_name, mutate, why) => {
    const { runDir, root } = await started();
    mutate(root);
    const result = await guard(runDir, root);
    expect(!result.ok && result.refusals[0]).toEqual({ code: 'consent-ids', reason: `the observation consents in force for ${URL_} are [], not exactly the recorded redis-redis: ${why}` });
  });

  it('refuses when the statement a governed run relies on is withdrawn mid-run', async () => {
    const { runDir, root } = await started({ clone: cloneAt(commits.B), providerStatements: statements(STATEMENT) });
    expect(await guard(runDir, root, { providerStatements: statements(STATEMENT) })).toMatchObject({ ok: true, providerStatement: 'STATEMENT-REDIS-ANTHROPIC@1', governed: { kind: 'governed' } });
    const result = await guard(runDir, root, { providerStatements: statements({ ...STATEMENT, withdrawn: true }) });
    expect(!result.ok && result.refusals).toEqual([{ code: 'statement', reason: 'the subject is governed now and has no per-project statement in force: no per-project statement naming the agent tool claude-code with the provider anthropic is in force: STATEMENT-REDIS-ANTHROPIC@1 is withdrawn' }]);
  });

  it('re-checks the statement against the run\'s declared tool: a Codex run with OpenAI keeps its Codex statement, and no Claude Code one stands in', async () => {
    const codex: ProviderStatementRecord = { ...STATEMENT, recordId: 'STATEMENT-REDIS-OPENAI', agentTool: 'codex', provider: 'openai' };
    const config = JSON.stringify({ ...JSON.parse(CONFIG), agentTool: 'codex', agentToolVersion: '0.40.0', agentProvider: 'openai', model: 'gpt-5.5' });
    const { runDir, root } = await started({ clone: cloneAt(commits.B), config, providerStatements: statements(codex) });
    expect((await guard(runDir, root, { providerStatements: statements(codex) })).ok).toBe(true);
    const result = await guard(runDir, root, { providerStatements: statements({ ...codex, agentTool: 'claude-code' }) });
    expect(!result.ok && result.refusals).toEqual([{ code: 'statement', reason: 'the subject is governed now and has no per-project statement in force: no per-project statement names the operator\'s agent tool codex with the provider openai (STATEMENT-REDIS-OPENAI@1 names claude-code with openai)' }]);
  });

  // R-POLARIS-DOSSIER-S3-GATES-2 finding 6: the provider is the operator's declaration, read from the run record; it selects the statement.
  const OPENAI: ProviderStatementRecord = { ...STATEMENT, recordId: 'STATEMENT-REDIS-OPENAI', provider: 'openai', act: { identity: 'STATEMENT-REDIS-OPENAI-ACT-2026-10-06', inForceAt: Date.UTC(2026, 9, 6) } };
  const rebound = async () => {
    const run = await started({ clone: cloneAt(commits.B), providerStatements: statements(STATEMENT) });
    editDeclared(run.runDir, (declared) => { declared['agentProvider'] = 'openai'; });
    editSubject(run.runDir, (subject) => { subject['providerStatement'] = 'STATEMENT-REDIS-OPENAI@1'; });
    return run;
  };
  const afterWithdrawal = statements({ ...STATEMENT, withdrawn: true }, OPENAI);

  it('before the brief, selects the statement by the provider the run record declares, and discloses that the provider is Inferred', async () => {
    const { runDir, root } = await rebound();
    const result = await guard(runDir, root, { providerStatements: afterWithdrawal });
    expect(result).toMatchObject({ ok: true, providerStatement: 'STATEMENT-REDIS-OPENAI@1', disclosures: DISCLOSED });
  });

  it('after the brief, refuses a provider or tool that differs from the one the brief record states, reading no object', async () => {
    const { runDir, root } = await rebound();
    writeBriefRecord(runDir, { tool: 'claude-code', provider: 'anthropic', declaredBy: 'operator', label: 'Inferred' });
    const opened: string[] = [];
    const result = await guard(runDir, root, { providerStatements: afterWithdrawal, opened });
    expect(!result.ok && result.refusals).toEqual([{ code: 'declared-changed', reason: 'the run record declares agent tool claude-code and provider openai, not the tool claude-code and provider anthropic the brief record states the run was briefed for; the provider selects the per-project statement' }]);
    expect(opened).toEqual([]);
    editDeclared(runDir, (declared) => { declared['agentProvider'] = 'anthropic'; declared['agentTool'] = 'codex'; });
    expect(codes(await guard(runDir, root, { providerStatements: afterWithdrawal }))).toEqual(['declared-changed']);
  });

  it('passes when the brief record states the tool and provider the run record declares; a coordinated edit of both is the disclosed residual', async () => {
    const { runDir, root } = await started({ clone: cloneAt(commits.B), providerStatements: statements(STATEMENT) });
    writeBriefRecord(runDir, { tool: 'claude-code', provider: 'anthropic', declaredBy: 'operator', label: 'Inferred' });
    expect(await guard(runDir, root, { providerStatements: statements(STATEMENT) })).toMatchObject({ ok: true, providerStatement: 'STATEMENT-REDIS-ANTHROPIC@1' });
    const both = await rebound();
    writeBriefRecord(both.runDir, { tool: 'claude-code', provider: 'openai', declaredBy: 'operator', label: 'Inferred' });
    expect(await guard(both.runDir, both.root, { providerStatements: afterWithdrawal })).toMatchObject({ ok: true, providerStatement: 'STATEMENT-REDIS-OPENAI@1', disclosures: DISCLOSED });
  });

  it.each([
    ['states no agent', undefined, 'it states no agent tool and provider'],
    ['states a provider that is not a string', { tool: 'claude-code', provider: 7 }, 'it states no agent tool and provider'],
  ])('refuses when the brief record exists but %s', async (_name, agent, why) => {
    const { runDir, root } = await started();
    writeBriefRecord(runDir, agent);
    const result = await guard(runDir, root);
    expect(!result.ok && result.refusals).toEqual([{ code: 'declared-changed', reason: `the brief record brief.json exists but ${why}, so whether the agent tool and provider changed since the brief cannot be decided` }]);
  });

  it('refuses when the brief record exists but is not JSON', async () => {
    const { runDir, root } = await started();
    fs.writeFileSync(path.join(runDir, 'brief.json'), '{not json');
    expect(codes(await guard(runDir, root))).toEqual(['declared-changed']);
  });

  it('refuses a run record altered into an invalid shape', async () => {
    const { runDir, root } = await started();
    rewritePin(runDir, 'not-a-commit');
    const reason = 'run.json subject is invalid: the pinned commit is not a full commit identifier';
    expect(await guard(runDir, root)).toEqual({ ok: false, reasons: [reason], refusals: [{ code: 'record-invalid', reason }], disclosures: DISCLOSED });
  });

  // R-POLARIS-DOSSIER-S3-GATES-1 finding 1(a): the pin moved, with no other edit, from non-governed A to governed, consented C.
  it('refuses a pin moved from a non-governed to a governed consented revision', async () => {
    const { runDir, root } = await started();
    rewritePin(runDir, commits.C);
    const opened: string[] = [];
    const result = await guard(runDir, root, { opened });
    expect(opened).toEqual([commits.C]);
    expect(codes(result)).toEqual(['governed-changed', 'statement']);
    expect(!result.ok && result.reasons[0]).toBe('the subject at the pinned revision is governed now (the pinned tree lists 1 path(s) under an openspec/ directory; the pinned tree lists 1 path(s) under a .syzygy/ directory, counted adopted or not), not the non-governed the run record states');
    // A statement in force does not rescue it: the run record still states another kind and relies on none.
    expect(codes(await guard(runDir, root, { providerStatements: statements(STATEMENT) }))).toEqual(['governed-changed', 'statement-changed']);
  });

  // Finding 1(b): a governed run's record edited down to non-governed with no statement, then the statement withdrawn.
  it('refuses a governed run whose record was downgraded to non-governed, before and after the statement is withdrawn', async () => {
    const { runDir, root } = await started({ clone: cloneAt(commits.B), providerStatements: statements(STATEMENT) });
    editSubject(runDir, (subject) => { subject['governed'] = { kind: 'non-governed', because: ['edited'] }; subject['providerStatement'] = null; });
    expect(runStatus(runDir).ok).toBe(true);
    expect(codes(await guard(runDir, root, { providerStatements: statements(STATEMENT) }))).toEqual(['governed-changed', 'statement-changed']);
    expect(codes(await guard(runDir, root, { providerStatements: statements({ ...STATEMENT, withdrawn: true }) }))).toEqual(['governed-changed', 'statement']);
  });

  it('refuses when the project input in force now records a drawer the run did not start under', async () => {
    const { runDir, root } = await started();
    expect(codes(await guard(runDir, root, { projectInput: DRAWER }))).toEqual(['governed-changed', 'statement']);
  });

  it('passes a pin moved between non-governed consented revisions, and shows the live label of the revision now pinned', async () => {
    const root = records({}, [['fixture-a', commits.A], ['fixture-a2', commits.A2]]);
    const { runDir } = await started({ root });
    rewritePin(runDir, commits.A2);
    expect(await guard(runDir, root)).toMatchObject({ ok: true, revision: { commit: commits.A2, label: 'fixture-a2' }, governed: { kind: 'non-governed' } });
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
      startGates: { registryEntry: { state: 'ok', record: 'public-git-source-acquisition-local-agent-v1.0' }, screeningPolicy: { state: 'ok' } },
      missing: [],
      cloneCommands: [`git clone ${URL_} <dir>`, `git -C <dir> checkout --detach ${commits.A}   # fixture-a`, `git -C <dir> checkout --detach ${commits.B}   # fixture-b`, `git -C <dir> checkout --detach ${commits.C}   # fixture-c`],
    });
  });
  it('names each missing record and is not ready', async () => {
    const result = await run(records({ [CONSENT_ACT]: null, [POLICY_ACT]: null }));
    expect(result.ok && result.report.outcome).toBe('not-ready');
    expect(result.ok && result.report.missing).toEqual([
      'observation consent: no observation consent in force names https://github.com/redis/redis as its Upstream: no observation record names https://github.com/redis/redis as its Upstream',
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
  it('reports D9 and the RFC7-20 reading established once the sitting\'s acts bind their records, and only while the bound bytes hold', async () => {
    const sitting = '.syzygy/governance/contracts/candidates/dossier-local-agent-acts/instances/in-force';
    const copied = [`${sitting}/D9-IN-FORCE-RECORD.md`, `${sitting}/RFC7-20-READING-IN-FORCE-RECORD.md`, '.syzygy/governance/doctrine/security.md', '.syzygy/governance/doctrine/v1.md', `${DECISIONS_DIR}/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`];
    const real = (rel: string): string => fs.readFileSync(path.join(REAL_ROOT, rel), 'utf8');
    const root = records({
      ...Object.fromEntries(copied.map(rel => [rel, real(rel)])),
      [`${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-D9-IN-FORCE-ACT.md`]: renderDossierLocalAgentAct('d9-in-force', sha(real(copied[0]!)), '2026-10-06', '2026-10-06T09:30:00Z'),
      [`${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-RFC7-20-READING-IN-FORCE-ACT.md`]: renderDossierLocalAgentAct('rfc7-20-reading-in-force', sha(real(copied[1]!)), '2026-10-06', '2026-10-06T09:30:00Z'),
    });
    const ready = await run(root);
    expect(ready.ok && [ready.report.d9, ready.report.rfc720Ruling]).toEqual([
      { state: 'ok', record: 'D9-IN-FORCE-OPERATOR-AGENT-2026-10-06' }, { state: 'ok', record: 'RFC7-20-READING-IN-FORCE-OPERATOR-AGENT-2026-10-06' },
    ]);
    fs.appendFileSync(path.join(root, '.syzygy/governance/doctrine/security.md'), '\nedit\n');
    const edited = await run(root);
    expect(edited.ok && edited.report.d9).toEqual({ state: 'refused', why: 'the bytes of .syzygy/governance/doctrine/security.md differ from the digest the act\'s artifact binds' });
    expect(edited.ok && edited.report.rfc720Ruling.state).toBe('ok');
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
