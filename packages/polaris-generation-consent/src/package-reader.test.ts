import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { AdmissionRecordError } from './admission-record.js';
import { DECISIONS_DIR, INSTANCES_DIR, createAdmissionRecordsPort, createPackageAdmissionReader, type PackageReaderFs } from './package-reader.js';

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
      ['unknown act type', { [act]: actText('consent-other', REDIS_PATH, obsText()) }],
      ['malformed digest', { [act]: actText('consent-observation', REDIS_PATH, obsText(), '2026-10-04', 'abc') }],
      ['bad date', { [act]: actText('consent-observation', REDIS_PATH, obsText(), '2026-13-45') }],
      ['artifact missing', { [act]: actText('consent-observation', `${INSTANCES_DIR}/gone/OBSERVATION-CONSENT.md`, obsText()) }],
      ['successor form not parsed', (() => { const t = obsText({ revocation: 'active; supersedes PUBLIC-OBS-REDIS-2026-09-01@1' }); return { [REDIS_PATH]: t, [act]: actText('consent-observation', REDIS_PATH, t) }; })()],
      ['branch name as revision', (() => { const t = obsText({ rows: '| `main` | `main` |' }); return { [REDIS_PATH]: t, [act]: actText('consent-observation', REDIS_PATH, t) }; })()],
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
