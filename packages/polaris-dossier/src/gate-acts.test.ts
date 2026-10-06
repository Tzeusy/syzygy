import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { DECISIONS_DIR, LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM } from '@syzygy/polaris-generation-consent';
import { renderDossierLocalAgentAct, renderLocalAgentSignoff, type DossierLocalAgentActKey } from '@syzygy/polaris-generation-consent/testing';
import { afterEach, describe, expect, it } from 'vitest';
import { createPackageGateSources, providerStatementGate } from './gate-sources.js';

// syzygy-qkea.21: the gate sources read the local-agent sitting's acts (scripts/record_dossier_local_agent_acts.py) and the
// version-tagged sign-off of the local-agent registry entry (scripts/record_versioned_signoff.py). Act text comes from the real
// recorders over the real sitting records; expected values are literals, never imported from the module under test.

const sha = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const REAL_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const NOW = Date.UTC(2026, 9, 7, 12, 0, 0);
const DATE = '2026-10-07';
const INSTANT = '2026-10-07T09:30:00Z';
const AT = Date.UTC(2026, 9, 7, 9, 30, 0);
const INSTANCES = '.syzygy/governance/contracts/candidates/dossier-local-agent-acts/instances';
const SECURITY = '.syzygy/governance/doctrine/security.md';
const V1 = '.syzygy/governance/doctrine/v1.md';
const DIRECTION = `${DECISIONS_DIR}/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`;
const PROPOSED_ENTRY = '.syzygy/governance/contracts/candidates/public-git-source-acquisition-local-agent/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json';
const INSTALLED_ENTRY = '.syzygy/governance/declarations/adapter-registry/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-CANDIDATE.json';
const SIGNOFF = `${DECISIONS_DIR}/PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1.0.md`;

/** Each act: its record under the sitting's instances, and the dedicated decisions file the recorder writes for it. */
const ACTS: Record<DossierLocalAgentActKey, { readonly record: string; readonly file: string }> = {
  'redis-no-evidence-drawer': { record: `${INSTANCES}/redis/NO-EVIDENCE-DRAWER-STATEMENT.md`, file: `${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-REDIS-NO-EVIDENCE-DRAWER-ACT.md` },
  'redis-agent-anthropic': { record: `${INSTANCES}/redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md`, file: `${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-REDIS-AGENT-ANTHROPIC-ACT.md` },
  'redis-agent-openai': { record: `${INSTANCES}/redis/AGENT-PROVIDER-STATEMENT-OPENAI.md`, file: `${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-REDIS-AGENT-OPENAI-ACT.md` },
  'd9-in-force': { record: `${INSTANCES}/in-force/D9-IN-FORCE-RECORD.md`, file: `${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-D9-IN-FORCE-ACT.md` },
  'rfc7-20-reading-in-force': { record: `${INSTANCES}/in-force/RFC7-20-READING-IN-FORCE-RECORD.md`, file: `${DECISIONS_DIR}/DOSSIER-LOCAL-AGENT-RFC7-20-READING-IN-FORCE-ACT.md` },
};
const KEYS = Object.keys(ACTS) as DossierLocalAgentActKey[];
const real = (rel: string): string => fs.readFileSync(path.join(REAL_ROOT, rel), 'utf8');

const cleanups: (() => void)[] = [];
afterEach(() => { for (const cleanup of cleanups.splice(0).reverse()) cleanup(); });
const tempDir = (): string => {
  const dir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-gate-acts-')));
  cleanups.push(() => fs.rmSync(dir, { recursive: true, force: true }));
  return dir;
};
const write = (root: string, rel: string, text: string): void => {
  fs.mkdirSync(path.dirname(path.join(root, rel)), { recursive: true });
  fs.writeFileSync(path.join(root, rel), text);
};

/** A records root holding the real sitting records and the files they bind, with the named acts recorded at INSTANT, and (when
 * `signoff`) the local-agent entry installed and signed off v1.0. An unrelated decisions file keeps the directory present. */
function world(acts: readonly DossierLocalAgentActKey[], signoff = false): string {
  const root = tempDir();
  for (const rel of [...KEYS.map(k => ACTS[k].record), SECURITY, V1, DIRECTION]) write(root, rel, real(rel));
  write(root, `${DECISIONS_DIR}/UNRELATED.md`, '# Unrelated\n');
  for (const key of acts) write(root, ACTS[key].file, renderDossierLocalAgentAct(key, sha(real(ACTS[key].record)), DATE, INSTANT));
  if (signoff) {
    write(root, INSTALLED_ENTRY, real(PROPOSED_ENTRY));
    write(root, SIGNOFF, renderLocalAgentSignoff(root, DATE, INSTANT));
  }
  return root;
}
const sources = (root: string, now = NOW) => createPackageGateSources({ root, now: () => now });
const notEstablished = (what: string) => ({
  state: 'absent',
  why: `no owner-act record binds a digest of ${what}, so the act cross-check of RFC3-16(a) cannot establish it in force; a status word, a log row or a file's presence is not read as one`,
});
const D9_WHAT = 'the D9 text (SEC-3 amendment)';
const RFC720_WHAT = 'the RFC7-20 reading (POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05, item 1)';
const UNSTATED = { stated: false, why: 'no admitted project input record (REQ-polaris-generation-001) for this subject exists, so whether a kernel evidence drawer exists is not stated' };
const CLASSES = ['governance-text', 'code-structure', 'code-content', 'evidence-content', 'derived-composites'];

describe('the sitting\'s acts as gate sources, with no act recorded', () => {
  it('establish nothing: D9 and the reading not established, the drawer unstated, no statement, no registry entry', async () => {
    const s = sources(world([]));
    expect(await s.d9()).toEqual(notEstablished(D9_WHAT));
    expect(await s.rfc720Ruling()).toEqual(notEstablished(RFC720_WHAT));
    expect(await s.projectInput.drawerFor('redis-redis')).toEqual(UNSTATED);
    expect(await s.providerStatements.statementsFor('redis-redis')).toEqual([]);
    expect(await s.registryEntry()).toEqual({ state: 'absent', why: `no owner-act record ${SIGNOFF} exists` });
  });
  it('establish nothing on this checkout, whose sitting records are drafted and unsigned', async () => {
    const s = sources(REAL_ROOT, Date.now());
    expect(await s.d9()).toEqual(notEstablished(D9_WHAT));
    expect(await s.rfc720Ruling()).toEqual(notEstablished(RFC720_WHAT));
    expect(await s.projectInput.drawerFor('redis-redis')).toEqual(UNSTATED);
    expect(await s.providerStatements.statementsFor('redis-redis')).toEqual([]);
    expect(await s.registryEntry()).toEqual({ state: 'absent', why: `no owner-act record ${SIGNOFF} exists` });
  });
});

describe('the sitting\'s acts as gate sources, once recorded', () => {
  it('establish every source when every act is recorded, none hiding another', async () => {
    const s = sources(world(KEYS, true));
    expect(await s.d9()).toEqual({ state: 'ok', record: 'D9-IN-FORCE-OPERATOR-AGENT-2026-10-07' });
    expect(await s.rfc720Ruling()).toEqual({ state: 'ok', record: 'RFC7-20-READING-IN-FORCE-OPERATOR-AGENT-2026-10-07' });
    expect(await s.projectInput.drawerFor('redis-redis')).toEqual({ stated: true, drawer: 'absent', record: 'NO-EVIDENCE-DRAWER-redis-redis@0.1.0-candidate.1' });
    expect(await s.registryEntry()).toEqual({ state: 'ok', record: 'public-git-source-acquisition-local-agent-v1.0' });
    const statements = await s.providerStatements.statementsFor('redis-redis');
    expect(statements).toEqual([
      { recordId: 'AGENT-PROVIDER-redis-redis-anthropic', version: '0.1.0-candidate.1', digest: sha(real(ACTS['redis-agent-anthropic'].record)), agentTool: 'claude-code', provider: 'anthropic', contentClasses: CLASSES, withdrawn: false, act: { identity: 'AGENT-PROVIDER-REDIS-ANTHROPIC-2026-10-07', inForceAt: AT } },
      { recordId: 'AGENT-PROVIDER-redis-redis-openai', version: '0.1.0-candidate.1', digest: sha(real(ACTS['redis-agent-openai'].record)), agentTool: 'codex', provider: 'openai', contentClasses: CLASSES, withdrawn: false, act: { identity: 'AGENT-PROVIDER-REDIS-OPENAI-2026-10-07', inForceAt: AT } },
    ]);
    expect(providerStatementGate(statements, 'claude-code', 'anthropic', NOW)).toEqual({ state: 'ok', record: 'AGENT-PROVIDER-redis-redis-anthropic@0.1.0-candidate.1' });
    expect(providerStatementGate(statements, 'codex', 'openai', NOW)).toEqual({ state: 'ok', record: 'AGENT-PROVIDER-redis-redis-openai@0.1.0-candidate.1' });
  });
  it('consent to one tool with one provider: Codex with Anthropic, or Claude Code with OpenAI, finds no statement', async () => {
    const statements = await sources(world(KEYS)).providerStatements.statementsFor('redis-redis');
    expect(providerStatementGate(statements, 'codex', 'anthropic', NOW)).toEqual({ state: 'absent', why: 'no per-project statement names the operator\'s agent tool codex with the provider anthropic (AGENT-PROVIDER-redis-redis-anthropic@0.1.0-candidate.1 names claude-code with anthropic; AGENT-PROVIDER-redis-redis-openai@0.1.0-candidate.1 names codex with openai)' });
    expect(providerStatementGate(statements, 'claude-code', 'openai', NOW)).toEqual({ state: 'absent', why: 'no per-project statement names the operator\'s agent tool claude-code with the provider openai (AGENT-PROVIDER-redis-redis-anthropic@0.1.0-candidate.1 names claude-code with anthropic; AGENT-PROVIDER-redis-redis-openai@0.1.0-candidate.1 names codex with openai)' });
  });
  it('establish only what was recorded: one act alone leaves every other source as it was', async () => {
    const d9 = sources(world(['d9-in-force']));
    expect(await d9.d9()).toEqual({ state: 'ok', record: 'D9-IN-FORCE-OPERATOR-AGENT-2026-10-07' });
    expect(await d9.rfc720Ruling()).toEqual(notEstablished(RFC720_WHAT));
    expect(await d9.projectInput.drawerFor('redis-redis')).toEqual(UNSTATED);
    expect(await d9.providerStatements.statementsFor('redis-redis')).toEqual([]);
    const drawer = sources(world(['redis-no-evidence-drawer']));
    expect(await drawer.projectInput.drawerFor('redis-redis')).toEqual({ stated: true, drawer: 'absent', record: 'NO-EVIDENCE-DRAWER-redis-redis@0.1.0-candidate.1' });
    expect(await drawer.d9()).toEqual(notEstablished(D9_WHAT));
    const openai = await sources(world(['redis-agent-openai'])).providerStatements.statementsFor('redis-redis');
    expect(openai.map(r => r.recordId)).toEqual(['AGENT-PROVIDER-redis-redis-openai']);
    expect(providerStatementGate(openai, 'claude-code', 'anthropic', NOW)).toEqual({ state: 'absent', why: 'no per-project statement names the operator\'s agent tool claude-code with the provider anthropic' });
    expect((await sources(world(['rfc7-20-reading-in-force'])).rfc720Ruling()).state).toBe('ok');
  });
  it('state the drawer for redis-redis only', async () => {
    const s = sources(world(KEYS));
    expect(await s.projectInput.drawerFor('psf-requests')).toEqual(UNSTATED);
    expect(await s.providerStatements.statementsFor('psf-requests')).toEqual([]);
    expect(await s.projectInput.drawerFor('__proto__')).toEqual(UNSTATED);
  });
  it('establish nothing before the acts\' instant', async () => {
    const s = sources(world(KEYS, true), AT - 1);
    expect(await s.d9()).toEqual({ state: 'absent', why: 'the act D9-IN-FORCE-OPERATOR-AGENT-2026-10-07 is not in force yet' });
    expect(await s.projectInput.drawerFor('redis-redis')).toEqual({ stated: false, why: 'the project-input statement for this subject is not in force: the act NO-EVIDENCE-DRAWER-REDIS-2026-10-07 is not in force yet' });
    expect(await s.providerStatements.statementsFor('redis-redis')).toEqual([]);
    expect(await s.registryEntry()).toEqual({ state: 'absent', why: 'the sign-off public-git-source-acquisition-local-agent-v1.0 is not in force yet' });
  });
});

describe('the sitting\'s acts fail closed', () => {
  it('refuse D9 once either doctrine file it binds changes, though the record and its act are untouched', async () => {
    for (const file of [SECURITY, V1]) {
      const root = world(['d9-in-force']);
      fs.appendFileSync(path.join(root, file), '\nedit\n');
      expect(await sources(root).d9()).toEqual({ state: 'refused', why: `the bytes of ${file} differ from the digest the act's artifact binds` });
    }
  });
  it('refuse the reading once the direction file changes, and when it is missing', async () => {
    const root = world(['rfc7-20-reading-in-force']);
    fs.appendFileSync(path.join(root, DIRECTION), '\nedit\n');
    expect(await sources(root).rfc720Ruling()).toEqual({ state: 'refused', why: `the bytes of ${DIRECTION} differ from the digest the act's artifact binds` });
    fs.rmSync(path.join(root, DIRECTION));
    expect(await sources(root).rfc720Ruling()).toEqual({ state: 'refused', why: `the bound file ${DIRECTION} cannot be read` });
  });
  it('refuse an in-force record whose table binds other files than the form names, even when an act binds its bytes', async () => {
    const root = world([]);
    const record = real(ACTS['d9-in-force'].record).replace(/^\| `\.syzygy\/governance\/doctrine\/v1\.md` \|.*\n/m, '');
    write(root, ACTS['d9-in-force'].record, record);
    write(root, ACTS['d9-in-force'].file, renderDossierLocalAgentAct('d9-in-force', sha(record), DATE, INSTANT));
    expect(await sources(root).d9()).toEqual({ state: 'refused', why: `the act's artifact binds ${SECURITY}, not exactly ${SECURITY}, ${V1}` });
    const readme = '.syzygy/governance/doctrine/README.md';
    write(root, readme, real(readme));
    const other = real(ACTS['d9-in-force'].record).replace(/^\| `\.syzygy\/governance\/doctrine\/v1\.md` \| `[0-9a-f]{64}` \|$/m, `| \`${readme}\` | \`${sha(real(readme))}\` |`);
    write(root, ACTS['d9-in-force'].record, other);
    write(root, ACTS['d9-in-force'].file, renderDossierLocalAgentAct('d9-in-force', sha(other), DATE, INSTANT));
    expect(await sources(root).d9()).toEqual({ state: 'refused', why: `the act's artifact binds ${SECURITY}, ${readme}, not exactly ${SECURITY}, ${V1}` });
    const twice = `${record}\n| File | SHA-256 |\n|---|---|\n`;
    write(root, ACTS['d9-in-force'].record, twice);
    write(root, ACTS['d9-in-force'].file, renderDossierLocalAgentAct('d9-in-force', sha(twice), DATE, INSTANT));
    expect(await sources(root).d9()).toEqual({ state: 'refused', why: 'the act\'s artifact does not carry exactly one bound-files table' });
  });
  it('refuse every act whose record changed after it', async () => {
    const root = world(KEYS);
    for (const key of KEYS) fs.appendFileSync(path.join(root, ACTS[key].record), ' ');
    const s = sources(root);
    expect((await s.d9()).state).toBe('refused');
    expect((await s.rfc720Ruling()).state).toBe('refused');
    expect(await s.projectInput.drawerFor('redis-redis')).toEqual({ stated: false, why: `the project-input statement for this subject is not in force: the bytes of ${ACTS['redis-no-evidence-drawer'].record} differ from the act's argument` });
    const statements = await s.providerStatements.statementsFor('redis-redis');
    expect(statements.map(r => [r.recordId, r.act])).toEqual([['AGENT-PROVIDER-redis-redis-anthropic', null], ['AGENT-PROVIDER-redis-redis-openai', null]]);
    expect(providerStatementGate(statements, 'claude-code', 'anthropic', NOW)).toEqual({ state: 'absent', why: 'no per-project statement naming the agent tool claude-code with the provider anthropic is in force: AGENT-PROVIDER-redis-redis-anthropic@unestablished has no owner act binding its bytes' });
  });
  it('refuse an act another decisions file names: a withdrawal in a form the reader does not define', async () => {
    const root = world(KEYS, true);
    write(root, `${DECISIONS_DIR}/WITHDRAW.md`, 'The owner withdraws NO-EVIDENCE-DRAWER-REDIS and AGENT-PROVIDER-REDIS-OPENAI, D9-IN-FORCE-OPERATOR-AGENT, RFC7-20-READING-IN-FORCE-OPERATOR-AGENT and the public-git-source-acquisition-local-agent sign-off.\n');
    const s = sources(root);
    const named = `${DECISIONS_DIR}/WITHDRAW.md names the act without being its record: a withdrawal or a form this reader does not define`;
    expect(await s.d9()).toEqual({ state: 'refused', why: named });
    expect(await s.rfc720Ruling()).toEqual({ state: 'refused', why: named });
    expect(await s.projectInput.drawerFor('redis-redis')).toEqual({ stated: false, why: `the project-input statement for this subject is not in force: ${named}` });
    expect((await s.providerStatements.statementsFor('redis-redis')).map(r => [r.recordId, r.act === null, r.withdrawn])).toEqual([['AGENT-PROVIDER-redis-redis-anthropic', false, false], ['AGENT-PROVIDER-redis-redis-openai', true, true]]);
    expect(await s.registryEntry()).toEqual({ state: 'refused', why: named });
    fs.rmSync(path.join(root, DECISIONS_DIR, 'WITHDRAW.md'));
    expect((await s.registryEntry()).state).toBe('ok');
    write(root, `${DECISIONS_DIR}/WITHDRAW-ENTRY.md`, `Withdrawn: \`${INSTALLED_ENTRY}\`.\n`);
    expect(await s.registryEntry()).toEqual({ state: 'refused', why: `${DECISIONS_DIR}/WITHDRAW-ENTRY.md names the act without being its record: a withdrawal or a form this reader does not define` });
  });
  // R-POLARIS-DOSSIER-GATE-SOURCES-1 finding 1: a statement says it is withdrawn by "a later owner act naming this record".
  it.each([
    ['its Record ID', (id: string) => `The owner withdraws the agent-provider statement \`${id}\`.\n`],
    ['its Record ID, in another case and spelling', (id: string) => `Withdrawn: ${id.toUpperCase().replaceAll('-', '_')}\n`],
    ['its Subject', (_id: string, provider: string) => `Subject: \`(project:syzygy, repository:redis-redis, agent-provider:${provider})\` withdrawn.\n`],
    ['its Subject in prose', (_id: string, provider: string) => `The owner withdraws consent for (project:syzygy, repository:redis-redis, agent-provider:${provider}).\n`],
  ])('withdraw a statement another decisions file names by %s, and only that statement', async (_name, withdrawal) => {
    for (const [id, provider, tool, other] of [['AGENT-PROVIDER-redis-redis-anthropic', 'anthropic', 'claude-code', 'AGENT-PROVIDER-redis-redis-openai'], ['AGENT-PROVIDER-redis-redis-openai', 'openai', 'codex', 'AGENT-PROVIDER-redis-redis-anthropic']] as const) {
      const root = world(KEYS);
      write(root, `${DECISIONS_DIR}/WITHDRAW.md`, withdrawal(id, provider));
      const statements = await sources(root).providerStatements.statementsFor('redis-redis');
      expect(statements.filter(r => r.withdrawn).map(r => r.recordId)).toEqual([id]);
      expect(statements.find(r => r.recordId === other)!.act).not.toBeNull();
      expect(providerStatementGate(statements, tool, provider, NOW)).toEqual({ state: 'absent', why: `no per-project statement naming the agent tool ${tool} with the provider ${provider} is in force: ${id}@unestablished is withdrawn` });
    }
  });
  it('withdraw a statement the aggregate acceptance record names on a Record ID or Subject field line, though not in its prose', async () => {
    const root = world(KEYS);
    const aggregate = `${DECISIONS_DIR}/ACCEPTANCE-ACT-RECORD.md`;
    write(root, aggregate, '# Acceptance\n\n| Record | Act |\n|---|---|\n| `AGENT-PROVIDER-redis-redis-anthropic` | (project:syzygy, repository:redis-redis, agent-provider:openai) |\n');
    expect((await sources(root).providerStatements.statementsFor('redis-redis')).map(r => r.withdrawn)).toEqual([false, false]);
    write(root, aggregate, '# Acceptance\n\nRecord ID: `AGENT-PROVIDER-redis-redis-anthropic` withdrawn\n');
    expect((await sources(root).providerStatements.statementsFor('redis-redis')).map(r => r.withdrawn)).toEqual([true, false]);
    write(root, aggregate, '# Acceptance\n\n- **Subject**: `(project:syzygy, repository:redis-redis, agent-provider:openai)` withdrawn\n');
    expect((await sources(root).providerStatements.statementsFor('redis-redis')).map(r => r.withdrawn)).toEqual([false, true]);
  });
  // Finding 2: the sign-off's act identity is its tag; the P-104 register row cites it before it exists and is read past, alone.
  it.each([
    ['its tag', 'The owner withdraws the sign-off tagged public-git-source-acquisition-local-agent-v1.0.\n'],
    ['its tag, in another case', 'Withdrawn: PUBLIC_GIT_SOURCE_ACQUISITION_LOCAL_AGENT_V1.0\n'],
    ['the package as signed off, spelled sign-off', 'The public-git-source-acquisition-local-agent sign-off is withdrawn.\n'],
    ['the package as signed off, spelled signoff', 'The public-git-source-acquisition-local-agent signoff is withdrawn.\n'],
  ])('refuse the registry sign-off another decisions file names by %s', async (_name, withdrawal) => {
    const root = world([], true);
    write(root, `${DECISIONS_DIR}/WITHDRAW.md`, withdrawal);
    expect(await sources(root).registryEntry()).toEqual({ state: 'refused', why: `${DECISIONS_DIR}/WITHDRAW.md names the act without being its record: a withdrawal or a form this reader does not define` });
  });
  it('read past the P-104 register row that cites the sign-off\'s tag, and that row only', async () => {
    const register = `${DECISIONS_DIR}/PENDING-OWNER-DECISIONS.md`;
    const row = real(register).split('\n').find(line => line.startsWith('| P-104 |'))!;
    expect(row).toContain('public-git-source-acquisition-local-agent-v1.0');
    const root = world([], true);
    write(root, register, `# Register\n\n| ID | Question |\n|---|---|\n${row}\n`);
    expect((await sources(root).registryEntry()).state).toBe('ok');
    write(root, register, `# Register\n\n| ID | Question |\n|---|---|\n${row}\n| P-105 | Withdraw public-git-source-acquisition-local-agent-v1.0 |\n`);
    expect(await sources(root).registryEntry()).toEqual({ state: 'refused', why: `${register} names the act without being its record: a withdrawal or a form this reader does not define` });
    write(root, register, `# Register\n\n${row.replace('| P-104 |', '| P-1040 |')}\n`);
    expect((await sources(root).registryEntry()).state).toBe('refused');
    write(root, `${DECISIONS_DIR}/OTHER.md`, `${row}\n`);
    write(root, register, '# Register\n');
    expect(await sources(root).registryEntry()).toEqual({ state: 'refused', why: `${DECISIONS_DIR}/OTHER.md names the act without being its record: a withdrawal or a form this reader does not define` });
  });
  // Note 4: the lines every recorder writes for RFC3-16(b) items 7 and 9.
  it.each([
    ['no owner', (t: string) => t.replace(/^Owner: Tzeusy\n/m, '')],
    ['another owner', (t: string) => t.replace(/^Owner: Tzeusy$/m, 'Owner: someone')],
    ['no provenance state', (t: string) => t.replace(/^Provenance state: .*\n/m, '')],
    ['another provenance state', (t: string) => t.replace('`owner-adopted (bootstrap, uncorrelated)`', '`agent-asserted`')],
    ['no A1 line', (t: string) => t.replace(/^A1 audit-record identity .*\n/m, '')],
    ['an A1 identity', (t: string) => t.replace('**explicitly absent**', '`a1:0001`')],
    ['no scope', (t: string) => t.replace(/^Scope: .*\n/m, '')],
    ['a wider scope', (t: string) => t.replace(/^Scope: .*$/m, 'Scope: every operator-agent run')],
    ['a second scope', (t: string) => t.replace(/^(Scope: .*)$/m, '$1\n\nScope: every operator-agent run')],
  ])('refuse an act record, and the registry sign-off, with %s', async (_name, mutate) => {
    const root = world(KEYS, true);
    for (const key of KEYS) write(root, ACTS[key].file, mutate(fs.readFileSync(path.join(root, ACTS[key].file), 'utf8')));
    write(root, SIGNOFF, mutate(fs.readFileSync(path.join(root, SIGNOFF), 'utf8')));
    const s = sources(root);
    expect((await s.d9()).state).toBe('refused');
    expect((await s.rfc720Ruling()).state).toBe('refused');
    expect((await s.projectInput.drawerFor('redis-redis')).stated).toBe(false);
    expect((await s.providerStatements.statementsFor('redis-redis')).map(r => r.act)).toEqual([null, null]);
    expect((await s.registryEntry()).state).toBe('refused');
  });
  // Note 5: the bound-files table, predicate by predicate.
  it.each([
    ['a second table inside a fence', (t: string) => `${t}\n\`\`\`\n| File | SHA-256 |\n|---|---|\n\`\`\`\n`, 'the act\'s artifact does not carry exactly one bound-files table'],
    ['another separator row', (t: string) => t.replace('| File | SHA-256 |\n|---|---|', '| File | SHA-256 |\n|:--|:--|'), 'the act\'s artifact does not carry exactly one bound-files table'],
    ['a third row', (t: string) => t.replace(/^(\| `\.syzygy\/governance\/doctrine\/v1\.md` \|.*)$/m, `$1\n| \`${SECURITY}\` | \`${'0'.repeat(64)}\` |`), `the act's artifact binds ${SECURITY}, ${V1}, ${SECURITY}, not exactly ${SECURITY}, ${V1}`],
  ])('refuse D9 when its record carries %s', async (_name, mutate, why) => {
    const root = world([]);
    const record = mutate(real(ACTS['d9-in-force'].record));
    write(root, ACTS['d9-in-force'].record, record);
    write(root, ACTS['d9-in-force'].file, renderDossierLocalAgentAct('d9-in-force', sha(record), DATE, INSTANT));
    expect(await sources(root).d9()).toEqual({ state: 'refused', why });
  });
  it.each([
    ['another subject', (t: string) => t.replace('repository:redis-redis)`', 'repository:redis-redis-fork)`')],
    ['another statement', (t: string) => t.replace('Statement: no kernel evidence drawer', 'Statement: a kernel evidence drawer')],
    ['no record id', (t: string) => t.replace(/^Record ID: .*\n/m, '')],
    ['no record version', (t: string) => t.replace(/^Record version: .*\n/m, '')],
    ['a second Record ID line', (t: string) => t.replace(/^(Record ID: .*)$/m, '$1\n\n$1')],
    ['a second Subject line', (t: string) => t.replace(/^(Subject: .*)$/m, '$1\n\n$1')],
  ])('leave the drawer unstated for a record with %s, even under an act', async (_name, mutate) => {
    const root = world([]);
    const record = mutate(real(ACTS['redis-no-evidence-drawer'].record));
    write(root, ACTS['redis-no-evidence-drawer'].record, record);
    write(root, ACTS['redis-no-evidence-drawer'].file, renderDossierLocalAgentAct('redis-no-evidence-drawer', sha(record), DATE, INSTANT));
    expect(await sources(root).projectInput.drawerFor('redis-redis')).toEqual({ stated: false, why: 'the record NO-EVIDENCE-DRAWER-REDIS-2026-10-07 binds does not state, for exactly this subject, that no kernel evidence drawer exists' });
  });
  it.each([
    ['another provider', (t: string) => t.replace('agent-provider:anthropic)`', 'agent-provider:openai)`')],
    ['another repository', (t: string) => t.replace('repository:redis-redis, agent-provider', 'repository:redis-fork, agent-provider')],
    ['another record id', (t: string) => t.replace('`AGENT-PROVIDER-redis-redis-anthropic`', '`AGENT-PROVIDER-redis-redis-openai`')],
    ['another agent tool', (t: string) => t.replace('Agent tool: Claude Code, run by', 'Agent tool: Codex, run by')],
    ['a second agent tool line', (t: string) => t.replace('Agent tool: Claude Code, run by', 'Agent tool: Claude Code, run by the operator\n\nAgent tool: Codex, run by')],
    ['no record version', (t: string) => t.replace(/^Record version: .*\n/m, '')],
    ['a second Record ID line', (t: string) => t.replace(/^(Record ID: .*)$/m, '$1\n\n$1')],
    ['a second Subject line', (t: string) => t.replace(/^(Subject: .*)$/m, '$1\n\n$1')],
  ])('carry no act for a statement whose record names %s, even under an act', async (_name, mutate) => {
    const root = world([]);
    const record = mutate(real(ACTS['redis-agent-anthropic'].record));
    write(root, ACTS['redis-agent-anthropic'].record, record);
    write(root, ACTS['redis-agent-anthropic'].file, renderDossierLocalAgentAct('redis-agent-anthropic', sha(record), DATE, INSTANT));
    expect((await sources(root).providerStatements.statementsFor('redis-redis')).map(r => [r.provider, r.act])).toEqual([['anthropic', null]]);
  });
});

describe('the registry entry\'s version-tagged sign-off', () => {
  it('refuses once the installed entry changes', async () => {
    const root = world([], true);
    fs.appendFileSync(path.join(root, INSTALLED_ENTRY), ' ');
    expect(await sources(root).registryEntry()).toEqual({ state: 'refused', why: `the bytes of ${INSTALLED_ENTRY} differ from the SHA-256 the sign-off records` });
    fs.rmSync(path.join(root, INSTALLED_ENTRY));
    expect(await sources(root).registryEntry()).toEqual({ state: 'refused', why: `the signed entry ${INSTALLED_ENTRY} cannot be read` });
  });
  it.each([
    ['another title', (t: string) => t.replace('local-agent version — version-tagged sign-off v1.0', 'local-agent version — version-tagged sign-off v1.1')],
    ['another version', (t: string) => t.replace(/^Version: 1\.0$/m, 'Version: 1.1')],
    ['another tag', (t: string) => t.replace(/^Tag: .*$/m, 'Tag: public-git-source-acquisition-v1.0')],
    ['another package', (t: string) => t.replace(/^Package: .*$/m, 'Package: public-admission-registry-entries')],
    ['another kind', (t: string) => t.replace(/^Kind: .*$/m, 'Kind: specification delta')],
    ['another installed path', (t: string) => t.replace(/^Installed entry: .*$/m, `Installed entry: ${PROPOSED_ENTRY}`)],
    ['another act type', (t: string) => t.replace('`adopt-registry-entry`', '`approve-policy`')],
    ['a REVISE verdict', (t: string) => t.replace(/^Review verdict: CONFIRM$/m, 'Review verdict: REVISE')],
    ['no recording instant', (t: string) => t.replace(/^Recorded at \(UTC\): .*\n/m, '')],
    ['an instant on another day', (t: string) => t.replace(`Recorded at (UTC): ${INSTANT}`, 'Recorded at (UTC): 2026-10-06T09:30:00Z')],
    ['its SHA-256 only inside a fence', (t: string) => t.replace(/^(Installed entry SHA-256: [0-9a-f]{64})$/m, '```\n$1\n```')],
  ])('refuses a record with %s', async (_name, mutate) => {
    const root = world([], true);
    write(root, SIGNOFF, mutate(fs.readFileSync(path.join(root, SIGNOFF), 'utf8')));
    expect((await sources(root).registryEntry()).state).toBe('refused');
  });
  it('is the form the recorder writes for this package', () => {
    expect(LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM).toMatchObject({ file: 'PUBLIC-GIT-SOURCE-ACQUISITION-LOCAL-AGENT-SIGNOFF-v1.0.md', installed: INSTALLED_ENTRY });
  });
});
