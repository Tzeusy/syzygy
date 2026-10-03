import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { AdmissionRecordError } from './admission-record.js';
import { DECISIONS_DIR, INSTANCES_DIR, POLICY_PATH, createAdmissionRecordsPort, createPackageAdmissionReader, createPackageAdmissionRecordsPort, createPackagePolicyReader, type PackageReaderFs } from './package-reader.js';

const REDIS_REV = '498ecd0d6d007db11ddb3aea9428552598a78622';
const OTHER_REV = 'd2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7';
const obsText = (over: { subject?: string; revocation?: string; rows?: string } = {}): string => `# redis observation consent (public repository)

Record ID: \`PUBLIC-OBS-REDIS-2026-10-03\`

Record version: \`0.1.0-candidate.7\`

Subject: \`${over.subject ?? '(project:syzygy, repository:redis-redis)'}\`

| Label | Commit object id |
|---|---|
${over.rows ?? `| \`8.10.2\` | \`${REDIS_REV}\` |\n| \`7.2.4\` | \`${OTHER_REV}\` |`}

Proposed revocation state: ${over.revocation ?? 'active; supersedes no earlier consent'}
`;
const egressText = (): string => `# Public-target egress consent

Record ID: \`PUBLIC-EGRESS-anthropic\`

Record version: \`0.1.0-candidate.7\`

Subject: \`(project:syzygy, provider:anthropic)\`

Permitted content classes (RFC5-14 closed vocabulary):

- \`governance-text\`
- \`code-structure\`

Retention: elsewhere.

Proposed revocation state: active; supersedes no earlier consent

## Scope

- \`(project:syzygy, repository:psf-requests)\`
- \`(project:syzygy, repository:redis-redis)\`
`;
const sha = (t: string): string => createHash('sha256').update(t, 'utf8').digest('hex');
const actText = (type: string, artifact: string, text: string, date = '2026-10-04', digest = sha(text)): string => `# Owner act — x

Date: ${date}

Owner: Tzeusy

Act type: \`${type}\`

Project identity: \`project:syzygy\`

Artifact identity: \`${artifact}\`

Exact digest (SHA-256): \`${digest}\`
`;
const REDIS_PATH = `${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`;
const EGRESS_PATH = `${INSTANCES_DIR}/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`;
const DAY = Date.UTC(2026, 9, 5);   // the day after the act date: in force from here

function memoryFs(files: Record<string, string>): PackageReaderFs {
  return {
    readdir: async dir => { const prefix = `/r/${DECISIONS_DIR}`; if (dir !== prefix) throw new Error('enoent'); return Object.keys(files).filter(f => f.startsWith(`${DECISIONS_DIR}/`)).map(f => f.slice(DECISIONS_DIR.length + 1)); },
    readFile: async file => { const key = file.slice(3); if (!(key in files)) throw new Error('enoent'); return files[key]!; },
  };
}
const world = (over: Record<string, string> = {}): Record<string, string> => ({
  [REDIS_PATH]: obsText(), [EGRESS_PATH]: egressText(),
  [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`]: actText('consent-observation', REDIS_PATH, obsText()),
  [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md`]: actText('consent-egress', EGRESS_PATH, egressText()),
  [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`]: 'direction, not an act',
  ...over,
});
const reader = (files: Record<string, string>) => createPackageAdmissionReader({ root: '/r', fs: memoryFs(files) });
const requirement = (kind: 'observation-consent' | 'egress-consent' | 'public-source-policy', repositoryId = 'redis-redis', revision = REDIS_REV) => ({ kind, repositoryId, revision, url: 'https://github.com/redis/redis', needs: 'x' });

describe('package admission reader', () => {
  it('returns a record only for an instance that an act record names by path and digest', async () => {
    const records = await reader(world()).read();
    expect(records.map(r => `${r.class}:${r.repositoryId ?? r.providerId}`).sort()).toEqual(['egress:anthropic', 'observation:redis-redis']);
    const obs = records.find(r => r.class === 'observation')!;
    expect(obs).toMatchObject({ recordId: 'PUBLIC-OBS-REDIS-2026-10-03', version: '0.1.0-candidate.7', project: 'project:syzygy', withdrawnAt: null, supersedes: null, inForceAt: DAY, admittedRevisions: [REDIS_REV, OTHER_REV], digest: sha(obsText()) });
    expect(records.find(r => r.class === 'egress')).toMatchObject({ admittedRepositories: ['psf-requests', 'redis-redis'], contentClasses: ['governance-text', 'code-structure'] });
    expect(Object.isFrozen(obs) && Object.isFrozen(obs.admittedRevisions)).toBe(true);
  });
  it('returns nothing when no act record exists: a candidate instance binds nothing', async () => {
    const files = world();
    for (const key of Object.keys(files)) if (key.endsWith('-ACT.md')) delete files[key];
    expect(await reader(files).read()).toEqual([]);
  });
  it('marks a record not in force when the instance bytes changed after the act', async () => {
    const records = await reader(world({ [REDIS_PATH]: obsText() + '\nedited\n' })).read();
    expect(records.find(r => r.class === 'observation')!.inForceAt).toBeNull();
  });
  it('refuses the whole read on unknown shapes instead of guessing', async () => {
    const act = `${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`;
    const cases: Array<[string, Record<string, string>]> = [
      ['unrecognised package decision file', { [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-WITHDRAWAL.md`]: 'withdrawn' }],
      ['artifact outside the instances directory', { [act]: actText('consent-observation', '.syzygy/elsewhere.md', obsText()), '.syzygy/elsewhere.md': obsText() }],
      ['traversal in the artifact path', { [act]: actText('consent-observation', `${INSTANCES_DIR}/../x.md`, obsText()) }],
      ['act form under an unrecognised file name', { [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT-WITHDRAWN.md`]: actText('consent-observation', REDIS_PATH, obsText()) }],
      ['act for another project', { [act]: actText('consent-observation', REDIS_PATH, obsText()).replace('`project:syzygy`', '`project:butlers`') }],
      ['duplicate Record ID line', (() => { const t = obsText() + '\nRecord ID: `OTHER`\n'; return { [REDIS_PATH]: t, [act]: actText('consent-observation', REDIS_PATH, t) }; })()],
      ['unknown act type', { [act]: actText('consent-other', REDIS_PATH, obsText()) }],
      ['malformed digest', { [act]: actText('consent-observation', REDIS_PATH, obsText(), '2026-10-04', 'abc') }],
      ['bad date', { [act]: actText('consent-observation', REDIS_PATH, obsText(), '2026-13-45') }],
      ['artifact missing', { [act]: actText('consent-observation', `${INSTANCES_DIR}/gone/OBSERVATION-CONSENT.md`, obsText()) }],
      ['successor form not parsed', (() => { const t = obsText({ revocation: 'active; supersedes PUBLIC-OBS-REDIS-2026-09-01@1' }); return { [REDIS_PATH]: t, [act]: actText('consent-observation', REDIS_PATH, t) }; })()],
      ['branch name as revision', (() => { const t = obsText({ rows: '| `short` | `abc123` |' }); return { [REDIS_PATH]: t, [act]: actText('consent-observation', REDIS_PATH, t) }; })()],
      ['subject not a pair', (() => { const t = obsText({ subject: '(project:syzygy, repository:*)' }); return { [REDIS_PATH]: t, [act]: actText('consent-observation', REDIS_PATH, t) }; })()],
    ];
    for (const [name, over] of cases) await expect(reader(world(over)).read(), name).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('refuses when the decisions directory cannot be listed', async () => {
    await expect(createPackageAdmissionReader({ root: '/missing', fs: memoryFs(world()) }).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
});

describe('admission records port', () => {
  const port = (files: Record<string, string>, now: number) => createAdmissionRecordsPort({ reader: reader(files), now: () => now });
  it('satisfies observation and egress exactly when an act is in force, and not before the day after the act', async () => {
    expect(await port(world(), DAY).check(requirement('observation-consent'))).toEqual({ satisfied: true, record: 'PUBLIC-OBS-REDIS-2026-10-03@0.1.0-candidate.7' });
    expect(await port(world(), DAY).check(requirement('egress-consent'))).toEqual({ satisfied: true, record: 'PUBLIC-EGRESS-anthropic@0.1.0-candidate.7' });
    expect((await port(world(), DAY - 1).check(requirement('observation-consent'))).satisfied).toBe(false);
  });
  it('is unsatisfied for an unadmitted revision, an unadmitted repository, a stale instance and the policy record', async () => {
    const p = port(world(), DAY);
    expect(await p.check(requirement('observation-consent', 'redis-redis', 'f'.repeat(40)))).toMatchObject({ satisfied: false });
    expect(await p.check(requirement('observation-consent', 'psf-requests', REDIS_REV))).toMatchObject({ satisfied: false });
    expect(await p.check(requirement('egress-consent', 'butlers'))).toMatchObject({ satisfied: false });
    expect(await p.check(requirement('public-source-policy'))).toMatchObject({ satisfied: false });
    expect(await port(world({ [REDIS_PATH]: obsText() + 'x' }), DAY).check(requirement('observation-consent'))).toMatchObject({ satisfied: false });
  });
  it('does not take another provider\'s egress record for the Anthropic requirement', async () => {
    const other = egressText().replace('provider:anthropic', 'provider:other');
    expect(await port(world({ [EGRESS_PATH]: other, [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md`]: actText('consent-egress', EGRESS_PATH, other) }), DAY).check(requirement('egress-consent'))).toMatchObject({ satisfied: false });
  });
  it('is unsatisfied, with a reason, when records cannot be read or none exist', async () => {
    const none = world(); for (const key of Object.keys(none)) if (key.endsWith('-ACT.md')) delete none[key];
    expect(await port(none, DAY).check(requirement('observation-consent'))).toMatchObject({ satisfied: false, why: expect.stringContaining('no record found') });
    expect(await port(world({ [`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-X-WITHDRAWAL.md`]: 'x' }), DAY).check(requirement('egress-consent'))).toMatchObject({ satisfied: false, why: expect.stringContaining('could not be read') });
  });
  it('reads fresh on every check: a later withdrawal-form file turns a satisfied answer into a refusal', async () => {
    const files = world();
    const p = port(files, DAY);
    expect((await p.check(requirement('egress-consent'))).satisfied).toBe(true);
    files[`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-WITHDRAWAL.md`] = 'withdrawn';
    expect((await p.check(requirement('egress-consent'))).satisfied).toBe(false);
  });
});

describe('act instant', () => {
  const withInstant = (instant: string, date = '2026-10-04'): string => actText('consent-observation', REDIS_PATH, obsText(), date).replace(`Date: ${date}\n`, `Date: ${date}\n\nRecorded at (UTC): ${instant}\n`);
  const actPath = `${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`;
  it('uses the Recorded at (UTC) instant when the record carries exactly one', async () => {
    const records = await reader(world({ [actPath]: withInstant('2026-10-04T09:30:00Z') })).read();
    expect(records.find(r => r.class === 'observation')!.inForceAt).toBe(Date.UTC(2026, 9, 4, 9, 30, 0));
  });
  it('refuses a malformed, repeated, wrong-day or non-whole-second instant', async () => {
    for (const bad of ['2026-10-04T09:30:00', '2026-10-04T09:30:00.5Z', '2026-10-05T00:00:00Z', '2026-10-04T25:00:00Z', '2026-10-04T24:00:00Z', '2026-02-30T00:00:00Z', 'soon'])
      await expect(reader(world({ [actPath]: withInstant(bad) })).read(), bad).rejects.toBeInstanceOf(AdmissionRecordError);
    const twice = withInstant('2026-10-04T09:30:00Z').replace('Recorded at (UTC): 2026-10-04T09:30:00Z', 'Recorded at (UTC): 2026-10-04T09:30:00Z\n\nRecorded at (UTC): 2026-10-04T10:30:00Z');
    await expect(reader(world({ [actPath]: twice })).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('keeps the next-UTC-day fallback for a record with only a date', async () => {
    expect((await reader(world()).read()).find(r => r.class === 'observation')!.inForceAt).toBe(DAY);
  });
});

describe('public-source policy act', () => {
  const policyText = (scope = true): string => JSON.stringify({ policyVersion: '1.2.0-public-source-candidate.1', ...(scope ? { publicSourceScope: { rules: [] } } : {}) }, null, 1) + '\n';
  const policyAct = (over: { type?: string; digest?: string; instant?: string | null; project?: string; identity?: string } = {}, text = policyText()): string => `# Owner act — policy

Date: 2026-10-04
${over.instant === null || over.instant === undefined ? '' : `\nRecorded at (UTC): ${over.instant}\n`}
Act identity: \`${over.identity ?? 'PWB-APPROVE-POLICY-PUBLIC-SOURCE-2026-10-04'}\`

Act type: \`${over.type ?? 'approve-policy'}\`

Project identity: \`${over.project ?? 'project:syzygy'}\`

Artifact identity: \`${POLICY_PATH}\`

Exact digest (SHA-256): \`${over.digest ?? sha(text)}\`
`;
  const POLICY_ACT = `${DECISIONS_DIR}/ANY-NAME-AT-ALL.md`;
  const policyWorld = (policy = policyText(), act = policyAct({}, policy), extra: Record<string, string> = {}): Record<string, string> => ({ ...world(), [POLICY_PATH]: policy, [POLICY_ACT]: act, ...extra });
  const policyReader = (files: Record<string, string>) => createPackagePolicyReader({ root: '/r', fs: memoryFs(files) });
  const check = (files: Record<string, string>, now: number) => createPackageAdmissionRecordsPort({ root: '/r', now: () => now, fs: memoryFs(files) }).check(requirement('public-source-policy'));

  it('recognises the act by path and digest, whatever the record is named, in force from a date-only next day', async () => {
    expect(await policyReader(policyWorld()).read()).toEqual([{ actIdentity: 'PWB-APPROVE-POLICY-PUBLIC-SOURCE-2026-10-04', digest: sha(policyText()), inForceAt: DAY }]);
    expect(await check(policyWorld(), DAY)).toEqual({ satisfied: true, record: 'PWB-APPROVE-POLICY-PUBLIC-SOURCE-2026-10-04' });
    expect(await check(policyWorld(), DAY - 1)).toMatchObject({ satisfied: false });
  });
  it('uses the act instant when present', async () => {
    const files = policyWorld(policyText(), policyAct({ instant: '2026-10-04T09:30:00Z' }));
    expect(await check(files, Date.UTC(2026, 9, 4, 9, 30, 0))).toMatchObject({ satisfied: true });
    expect(await check(files, Date.UTC(2026, 9, 4, 9, 29, 59))).toMatchObject({ satisfied: false });
  });
  it('is unsatisfied when the policy declares no public-source scope, even under an act over those bytes', async () => {
    const old = policyText(false);
    expect(await check(policyWorld(old, policyAct({}, old)), DAY)).toMatchObject({ satisfied: false });
  });
  it('is unsatisfied when the policy bytes changed after the act, or the act is another type', async () => {
    expect(await check(policyWorld(policyText() + ' ', policyAct({}, policyText())), DAY)).toMatchObject({ satisfied: false });
    expect(await check(policyWorld(policyText(), policyAct({ type: 'adopt-doctrine' })), DAY)).toMatchObject({ satisfied: false });
  });
  it('is unsatisfied with no act record', async () => {
    const files = policyWorld(); delete files[POLICY_ACT];
    expect(await check(files, DAY)).toMatchObject({ satisfied: false });
  });
  it('refuses the read on a record that names the policy without a readable act form, or for another project', async () => {
    for (const act of [policyAct({ digest: 'abc' }), policyAct({ project: 'project:butlers' }), policyAct({ instant: 'soon' }), policyAct().replace('Act identity:', 'Act ident:')])
      await expect(policyReader(policyWorld(policyText(), act)).read(), act).rejects.toBeInstanceOf(AdmissionRecordError);
    expect(await check(policyWorld(policyText(), policyAct({ digest: 'abc' })), DAY)).toMatchObject({ satisfied: false, why: expect.stringContaining('could not be read') });
  });
  it('refuses when the policy file is missing or not JSON', async () => {
    const files = policyWorld(); delete files[POLICY_PATH];
    await expect(policyReader(files).read()).rejects.toBeInstanceOf(AdmissionRecordError);
    await expect(policyReader(policyWorld('not json')).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('without a policy reader the requirement stays unsatisfied', async () => {
    expect(await createAdmissionRecordsPort({ reader: reader(world()), now: () => DAY }).check(requirement('public-source-policy'))).toMatchObject({ satisfied: false });
  });
});
