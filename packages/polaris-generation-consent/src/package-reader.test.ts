import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';
import { AdmissionRecordError } from './admission-record.js';
import { inForceRecords } from './consent-ports.js';
import { renderRecorderAct } from './recorder-fixtures.testkit.js';
import { DECISIONS_DIR, EGRESS_V2_INSTANCE, INSTANCES_DIR, POLICY_ACT_FILE, POLICY_PATH, createAdmissionRecordsPort, createPackageAdmissionReader, createPackageAdmissionRecordsPort, createPackagePolicyReader, type PackageReaderFs } from './package-reader.js';

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
const OWNER_ANSWERS_FILE = 'PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md';
/** The real direction, read from this checkout: the reader pins its digest. */
const ownerAnswers = (): string => readFileSync(fileURLToPath(new URL(`../../../${DECISIONS_DIR}/${OWNER_ANSWERS_FILE}`, import.meta.url)), 'utf8');
const sha = (t: string): string => createHash('sha256').update(t, 'utf8').digest('hex');
const REDIS_PATH = `${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`;
const EGRESS_PATH = `${INSTANCES_DIR}/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`;
/** An act record as the real recorder renders it (see recorder-fixtures.testkit.ts), minus its instant line (a date-only act), with the
 * fields a case varies replaced. The artifact picks the recorder's form: the redis observation unless it is one of the egress instances. */
const actText = (type: string, artifact: string, text: string, date = '2026-10-04', digest = sha(text)): string => {
  const key = artifact === EGRESS_PATH ? 'egress-anthropic' : artifact === EGRESS_V2_INSTANCE ? 'egress-anthropic-v2' : 'redis-observation';
  return renderRecorderAct(key, '0'.repeat(64), date, `${date}T09:30:00Z`)
    .replace(/Recorded at \(UTC\): \S+\n\n/, '').replace('0'.repeat(64), digest)
    .replace(/^Act type: `[^`]+`/m, `Act type: \`${type}\``).replace(/^Artifact identity: `[^`]+`/m, `Artifact identity: \`${artifact}\``);
};
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
  [`${DECISIONS_DIR}/${OWNER_ANSWERS_FILE}`]: ownerAnswers(),
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
  it('refuses any other spelling or placement of a recorded-at line instead of falling back', async () => {
    for (const loose of ['  Recorded at (UTC): 2026-10-04T09:30:00Z', 'recorded at (utc): 2026-10-04T09:30:00Z', 'Recorded at: 2026-10-04T09:30:00Z', 'Recorded At (UTC):  2026-10-04T09:30:00Z', 'RECORDED AT (UTC): 2026-10-04T09:30:00Z']) {
      const text = actText('consent-observation', REDIS_PATH, obsText()).replace('Date: 2026-10-04\n', `Date: 2026-10-04\n\n${loose}\n`);
      await expect(reader(world({ [actPath]: text })).read(), loose).rejects.toBeInstanceOf(AdmissionRecordError);
    }
    const strictAndLoose = withInstant('2026-10-04T09:30:00Z').replace('Owner: Tzeusy', 'Owner: Tzeusy\n\n  recorded at 2026-10-04T10:00:00Z');
    await expect(reader(world({ [actPath]: strictAndLoose })).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('accepts only the pinned owner-answers file by name and bytes', async () => {
    const dir = (name: string) => `${DECISIONS_DIR}/${name}`;
    await expect(reader(world({ [dir(OWNER_ANSWERS_FILE)]: ownerAnswers() + ' ' })).read()).rejects.toBeInstanceOf(AdmissionRecordError);   // edited bytes
    await expect(reader(world({ [dir('PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-04.md')]: ownerAnswers() })).read()).rejects.toBeInstanceOf(AdmissionRecordError);   // another name, same bytes
    await expect(reader(world({ [dir('PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-04.md')]: 'direction, not an act' })).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('keeps the next-UTC-day fallback for a record with only a date', async () => {
    expect((await reader(world()).read()).find(r => r.class === 'observation')!.inForceAt).toBe(DAY);
  });
});

describe('public-source policy act', () => {
  const policyText = (scope = true): string => JSON.stringify({ policyVersion: '1.2.0-public-source-candidate.1', ...(scope ? { publicSourceScope: { rules: [] } } : {}) }, null, 1) + '\n';
  // The act text is what the recorder itself renders (scripts/record_public_source_screening_scope_act.py), so the reader's expected
  // forms cannot drift from the writer's. Only the fields a case varies are replaced afterwards.
  const rendered = new Map<string, string>();
  const render = (date: string): string => {
    const hit = rendered.get(date);
    if (hit !== undefined) return hit;
    const py = `import sys; sys.path.insert(0, 'scripts'); import record_public_source_screening_scope_act as m
sys.stdout.write(m.render_act(m.ACT, '0'*64, '${date}', 'b'*64, 'c'*40, 'CONFIRM', m.Selection('opening', 'label', 'description'), 'f'*64, '${date}T09:30:00Z', '1'*64, '1.2.0-public-source-candidate.1'))`;
    const run = spawnSync('python3', ['-c', py], { cwd: path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..'), encoding: 'utf8' });
    if (run.status !== 0) throw new Error(`recorder render failed: ${run.stderr}`);
    rendered.set(date, run.stdout);
    return run.stdout;
  };
  const policyAct = (over: { type?: string; digest?: string; instant?: string | null; project?: string; identity?: string; date?: string } = {}, text = policyText()): string => {
    const date = over.date ?? '2026-10-04';
    let act = render(date).replace('0'.repeat(64), over.digest ?? sha(text));
    act = over.instant === null || over.instant === undefined ? act.replace(/Recorded at \(UTC\): \S+\n\n/, '') : act.replace(/(Recorded at \(UTC\): )\S+/, `$1${over.instant}`);
    if (over.type !== undefined) act = act.replace(/^Act type: `[^`]+`/m, `Act type: \`${over.type}\``);
    if (over.identity !== undefined) act = act.replace(/^Act identity: `[^`]+`/m, `Act identity: \`${over.identity}\``);
    if (over.project !== undefined) act = act.replace(/^Project identity: `[^`]+`/m, `Project identity: \`${over.project}\``);
    return act;
  };
  const POLICY_ACT = `${DECISIONS_DIR}/${POLICY_ACT_FILE}`;
  const policyWorld = (policy = policyText(), act = policyAct({}, policy), extra: Record<string, string> = {}): Record<string, string> => ({ ...world(), [POLICY_PATH]: policy, [POLICY_ACT]: act, ...extra });
  const policyReader = (files: Record<string, string>) => createPackagePolicyReader({ root: '/r', fs: memoryFs(files) });
  const check = (files: Record<string, string>, now: number) => createPackageAdmissionRecordsPort({ root: '/r', now: () => now, fs: memoryFs(files) }).check(requirement('public-source-policy'));

  it('recognises the recorder\'s record by its exact path and format, in force from a date-only next day', async () => {
    expect(await policyReader(policyWorld()).read()).toEqual([{ actIdentity: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-04', digest: sha(policyText()), inForceAt: DAY }]);
    expect(await check(policyWorld(), DAY)).toEqual({ satisfied: true, record: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-04' });
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
  it('refuses a record other than the recorder\'s that names the policy as its artifact (packets, quotations, other act types)', async () => {
    const line = `Artifact identity: \`${POLICY_PATH}\``;
    const forms: Record<string, string> = {
      'a prepared packet quoting an act': `# PREPARED packet\n\n${policyAct()}`,
      'a fenced quotation': `# Notes\n\n\`\`\`text\n${line}\n\`\`\`\n`,
      'another act type under another name': policyAct({ type: 'adopt-doctrine' }),
    };
    for (const [name, text] of Object.entries(forms)) await expect(policyReader(policyWorld(policyText(), policyAct(), { [`${DECISIONS_DIR}/SOME-OTHER-RECORD.md`]: text })).read(), name).rejects.toBeInstanceOf(AdmissionRecordError);
    // a block-quoted mention is not a line that names the artifact, and the three historical acts are skipped by name
    const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
    const historical = ['PWB-SECRET-CLASSIFICATION-POLICY-ACT.md', 'PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md', 'PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md'];
    const realBytes = Object.fromEntries(historical.map(name => [`${DECISIONS_DIR}/${name}`, readFileSync(path.join(repoRoot, DECISIONS_DIR, name), 'utf8')]));
    const quiet = { [`${DECISIONS_DIR}/NOTES.md`]: `> ${line}\n`, ...realBytes };
    const files = policyWorld(policyText(false), policyAct({}, policyText(false)), quiet); delete files[POLICY_ACT];
    expect(await policyReader(files).read()).toEqual([]);
    // the same file names, edited: a forged withdrawal in a historical act refuses the read, whichever file it is placed in
    for (const name of Object.keys(realBytes)) await expect(policyReader({ ...files, [name]: `${realBytes[name]}\nWithdrawn: this act is withdrawn.\n` }).read(), name).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('does not count a Recorded-at line inside a code fence (both readers)', async () => {
    const fenced = (act: string): string => act.replace(/Recorded at \(UTC\): \S+\n\n/, '').replace('Owner: Tzeusy', 'Owner: Tzeusy\n\n```text\nRecorded at (UTC): 2026-10-04T00:00:01Z\n```');
    const act = fenced(policyAct({ instant: '2026-10-04T09:30:00Z' }));
    await expect(policyReader(policyWorld(policyText(), act)).read()).rejects.toBeInstanceOf(AdmissionRecordError);
    // a real line beside a fenced one is the instant
    const both = policyAct({ instant: '2026-10-04T09:30:00Z' }).replace('Owner: Tzeusy', 'Owner: Tzeusy\n\n```text\nRecorded at (UTC): 2026-10-04T00:00:01Z\n```');
    expect((await policyReader(policyWorld(policyText(), both)).read())[0]!.inForceAt).toBe(Date.UTC(2026, 9, 4, 9, 30, 0));
    const obsFenced = world(); const key = Object.keys(obsFenced).find(k => k.endsWith('-ACT.md') && k.includes('OBSERVATION'))!;
    obsFenced[key] = obsFenced[key]!.replace(/Recorded at \(UTC\): \S+\n\n?/, '') + '\n```text\nRecorded at (UTC): 2026-10-04T00:00:01Z\n```\n';
    await expect(reader(obsFenced).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('refuses the recorder\'s file when its act type, identity, title or provenance is not the recorder\'s form', async () => {
    for (const bad of [policyAct({ type: 'amend-policy' }), policyAct({ type: 'amend-policy', identity: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-04' }), policyAct({ identity: 'something-else' }), policyAct().replace('(public-source screening scope)', ''), policyAct().replace('owner-adopted (bootstrap, uncorrelated)', 'owner-adopted'), policyAct({ date: '2026-10-05' }).replace('2026-10-05', '2026-10-04')])
      await expect(policyReader(policyWorld(policyText(), bad)).read(), bad).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('refuses a malformed recorded-at line in the policy act', async () => {
    for (const loose of ['  Recorded at (UTC): 2026-10-04T09:30:00Z', 'recorded at (utc): 2026-10-04T09:30:00Z']) {
      const act = policyAct().replace('Owner: Tzeusy', `${loose}\n\nOwner: Tzeusy`);
      await expect(policyReader(policyWorld(policyText(), act)).read(), loose).rejects.toBeInstanceOf(AdmissionRecordError);
    }
  });
  it('without a policy reader the requirement stays unsatisfied', async () => {
    expect(await createAdmissionRecordsPort({ reader: reader(world()), now: () => DAY }).check(requirement('public-source-policy'))).toMatchObject({ satisfied: false });
  });
});

describe('egress version 2 record', () => {
  const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
  const v2Text = (): string => readFileSync(path.join(repoRoot, EGRESS_V2_INSTANCE), 'utf8');   // the real candidate bytes
  const V2_ACT = `${DECISIONS_DIR}/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md`;
  const V1_ACT = `${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md`;
  /** Version 1 took effect the day before version 2: version 2 supersedes it only by being strictly later. */
  const v2World = (over: Record<string, string> = {}): Record<string, string> => world({ [V1_ACT]: actText('consent-egress', EGRESS_PATH, egressText(), '2026-10-03'), [EGRESS_V2_INSTANCE]: v2Text(), [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, v2Text()), ...over });
  const port = (files: Record<string, string>, now: number) => createAdmissionRecordsPort({ reader: reader(files), now: () => now });

  it('is read from the recorder\'s act: version 2 supersedes version 1 once in force', async () => {
    const records = await reader(v2World()).read();
    const v2 = records.find(r => r.version === '0.2.0-candidate.1')!;
    expect(v2).toMatchObject({ class: 'egress', providerId: 'anthropic', digest: sha(v2Text()), inForceAt: DAY, supersedes: 'PUBLIC-EGRESS-anthropic@0.1.0-candidate.7', admittedRepositories: ['psf-requests', 'redis-redis'] });
    expect(v2.contentClasses).toContain('project-documentation');
    expect(inForceRecords(records, DAY).filter(r => r.class === 'egress').map(r => r.version)).toEqual(['0.2.0-candidate.1']);
    expect(await port(v2World(), DAY).check(requirement('egress-consent'))).toEqual({ satisfied: true, record: 'PUBLIC-EGRESS-anthropic@0.2.0-candidate.1' });
  });
  it('leaves version 1 standing before the version 2 act takes effect, and with no version 1 act at all', async () => {
    expect(inForceRecords(await reader(v2World()).read(), DAY - 1).filter(r => r.class === 'egress').map(r => r.version)).toEqual(['0.1.0-candidate.7']);   // version 2 is not in force yet
    const later = v2World({ [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, v2Text(), '2026-10-09') });
    expect(inForceRecords(await reader(later).read(), DAY).filter(r => r.class === 'egress').map(r => r.version)).toEqual(['0.1.0-candidate.7']);
    const only = v2World(); delete only[V1_ACT];
    expect(inForceRecords(await reader(only).read(), DAY).filter(r => r.class === 'egress').map(r => r.version)).toEqual(['0.2.0-candidate.1']);
  });
  it('refuses when version 2 did not take effect strictly after version 1: the same instant, or earlier', async () => {
    await expect(reader(v2World({ [V1_ACT]: actText('consent-egress', EGRESS_PATH, egressText(), '2026-10-04') })).read()).rejects.toBeInstanceOf(AdmissionRecordError);   // same day, both date-only
    await expect(reader(v2World({ [V1_ACT]: actText('consent-egress', EGRESS_PATH, egressText(), '2026-10-05') })).read()).rejects.toBeInstanceOf(AdmissionRecordError);   // version 1 later
    expect((await reader(v2World()).read()).length).toBe(3);
  });
  it('binds the exact bytes: an edited record is not in force', async () => {
    const edited = await reader(v2World({ [EGRESS_V2_INSTANCE]: `${v2Text()}\nedited\n` })).read();
    expect(edited.find(r => r.version === '0.2.0-candidate.1')!.inForceAt).toBeNull();
  });
  it('accepts the closed list only: other names, identities, artifacts, titles and revocation lines refuse the read', async () => {
    const cases: Array<[string, Record<string, string>]> = [
      ['another file name under the version 2 prefix', { [`${DECISIONS_DIR}/PUBLIC-EGRESS-V2-ANTHROPIC-WITHDRAWAL.md`]: 'withdrawn' }],
      ['a copy of the act under another name', { [`${DECISIONS_DIR}/PUBLIC-EGRESS-V2-OTHER-ACT.md`]: actText('consent-egress', EGRESS_V2_INSTANCE, v2Text()) }],
      ['the version 1 identity on the version 2 act', { [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, v2Text()).replace(/^Act identity: `[^`]+`/m, 'Act identity: `PUBLIC-EGRESS-ANTHROPIC-2026-10-04`') }],
      ['the version 1 instance under the version 2 act', { [V2_ACT]: actText('consent-egress', EGRESS_PATH, egressText()) }],
      ['an observation type on the version 2 act', { [V2_ACT]: actText('consent-observation', EGRESS_V2_INSTANCE, v2Text()) }],
      ['a title that is not the recorder\'s', { [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, v2Text()).replace(', version 2', '') }],
      ['version 1 revocation wording in the version 2 record', (() => { const t = v2Text().replace(/^Proposed revocation state: .*$/m, 'Proposed revocation state: active; supersedes no earlier consent'); return { [EGRESS_V2_INSTANCE]: t, [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, t) }; })()],
      ['an altered successor in the version 2 record', (() => { const t = v2Text().replace('0.1.0-candidate.7', '0.0.9'); return { [EGRESS_V2_INSTANCE]: t, [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, t) }; })()],
      ['a version 2 act over the version 1 record id and version', (() => { const t = v2Text().replace('0.2.0-candidate.1', '0.1.0-candidate.7'); return { [EGRESS_V2_INSTANCE]: t, [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, t) }; })()],
    ];
    for (const [name, over] of cases) await expect(reader(v2World(over)).read(), name).rejects.toBeInstanceOf(AdmissionRecordError);
  });
  it('ignores a Recorded-at line inside a code fence in the version 2 act, and refuses a fenced-only one', async () => {
    const fence = '\n```text\nRecorded at (UTC): 2026-10-04T00:00:01Z\n```\n';
    const real = actText('consent-egress', EGRESS_V2_INSTANCE, v2Text()).replace('Date: 2026-10-04\n', 'Date: 2026-10-04\n\nRecorded at (UTC): 2026-10-04T09:30:00Z\n');
    const both = (await reader(v2World({ [V2_ACT]: real + fence })).read()).find(r => r.version === '0.2.0-candidate.1')!;
    expect(both.inForceAt).toBe(Date.UTC(2026, 9, 4, 9, 30, 0));
    await expect(reader(v2World({ [V2_ACT]: actText('consent-egress', EGRESS_V2_INSTANCE, v2Text()) + fence })).read()).rejects.toBeInstanceOf(AdmissionRecordError);
  });
});
