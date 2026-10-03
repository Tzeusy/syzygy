import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { validateGenerationSources } from '@syzygy/polaris-generation-core';
import { PWB_DENIED_PATH_RULES, PWB_SECRET_POLICY } from '@syzygy/three-surface-poc-core';

import { checkoutPolicyActPort, loadPublicSourceScreen, PUBLIC_SOURCE_ACT_RECORD_PATH, PUBLIC_SOURCE_POLICY_PATH, PUBLIC_SOURCE_V2_ACT_RECORD_PATH, RFC5_CLASS_ACT_RECORD_PATH, RFC5_MODULE_PATH,
  readScreenedRepoCorpus, type PublicSourcePolicyActPort } from './public-source-screening.js';
import type { CorpusAdmissionPort } from './repo-corpus.js';

// The four variant rule objects and the prerequisite, exactly as the #326 builder emits them.
const PARITY = JSON.parse(readFileSync(fileURLToPath(new URL('./fixtures/screening-scope-v2-parity.json', import.meta.url)), 'utf8')) as {
  readonly rules: Record<string, Record<string, unknown>>; readonly prerequisite: Record<string, unknown> };
const SECRET = `const id = "${'AK'}IA${'Q'.repeat(16)}";\n`, PATH_TOKEN = `${'AK'}IA${'R'.repeat(16)}`;
const SENTINEL = 'V2-SCREEN-SENTINEL-41c9';
const FILES: Record<string, string> = {
  'src/clean.c': 'int answer(void) { return 42; }\n',
  'README.md': '# Fixture\n\nProse the rule maps.\n',
  'docs/guide.md': '# Guide\n',
  'LICENSE': 'Fixture licence text.\n',
  'licenses/extra.txt': 'Fixture licence text two.\n',
  // The licenses file name is held to the docs denylist (#326 round 4).
  'licenses/SECURITY.md': `${SENTINEL} security policy\n`,
  'MANIFESTO.md': '# Opt-in manifesto\n',
  // Not mapped: a denylist word, nested below the root, a build file under docs.
  'docs/adr/0001-choice.md': `${SENTINEL} decision record\n`,
  'src/README.md': `${SENTINEL} vendored readme\n`,
  'docs/requirements.txt': `${SENTINEL} pinned\n`,
  // Mapped paths still pass every screen: denied path, a path detector, a body detector, active content.
  'docs/.env.md': `${SENTINEL} env-prefixed\n`,
  [`docs/${PATH_TOKEN}.md`]: `${SENTINEL} path token\n`,
  'CHANGELOG.md': `${SENTINEL}\n${SECRET}`,
  'docs/active.md': `${SENTINEL}\n<script>alert(1)</script>\n`,
};
const MAPPED = ['LICENSE', 'README.md', 'docs/guide.md', 'licenses/extra.txt'];
const CLASS_ROW = '| `project-documentation` |';

const sha = (bytes: Uint8Array | string): string => createHash('sha256').update(bytes).digest('hex');
const scope = (variant: string, sourceExtensions: readonly string[] = ['.c'], documentationRules: unknown[] = [PARITY.rules[variant]]) => ({
  contentClassification: {
    classesClassified: ['code-structure', 'code-content', 'project-documentation', 'derived-composites'],
    rules: [{ class: 'code-structure', rule: 'paths' }, { class: 'code-content', sourceExtensions }, ...documentationRules, { class: 'derived-composites', rule: 'composites' }],
  },
  prerequisite: PARITY.prerequisite,
});
const policy = (variant = 'none', publicSourceScope: unknown = scope(variant), version = `1.3.0-public-source-candidate.1.${variant}`): Uint8Array => new TextEncoder().encode(`${JSON.stringify({
  policyId: 'synthetic-public-source-policy', policyVersion: version,
  sourceAdmission: { deniedPathBasenames: PWB_DENIED_PATH_RULES.basenames, deniedPathPrefixes: PWB_DENIED_PATH_RULES.prefixes, deniedPathSuffixes: PWB_DENIED_PATH_RULES.suffixes },
  detectors: PWB_SECRET_POLICY.detectors, publicSourceScope,
}, null, 2)}\n`);
const SUPERSESSION = `Supersession / revocation: this act supersedes, for the \`approve-policy\` role only, the 2026-10-04 act recorded at \`${PUBLIC_SOURCE_ACT_RECORD_PATH}\`.`;
const record = (identity: string, type: string, artifact: string, digests: readonly string[], supersession = SUPERSESSION): string => [
  '# Owner act — synthetic fixture', '', `Act identity: \`${identity}\``, '', `Act type: \`${type}\``, '', 'Project identity: `project:syzygy`', '',
  `Artifact identity: \`${artifact}\``, '', ...digests.map(digest => `Exact digest (SHA-256): \`${digest}\``), '', supersession, '',
].join('\n');
const V1_ID = 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-04';
const V2_ID = 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL-2026-10-04';
const RFC5_ID = 'RFC5-PROJECT-DOCUMENTATION-AMEND-2026-10-04';
const policyAct = (bytes: Uint8Array, identity = V2_ID) => record(identity, 'approve-policy', PUBLIC_SOURCE_POLICY_PATH, [sha(bytes)]);
const MODULE = new TextEncoder().encode(`# RFC-0005\n\n| Class | Meaning |\n|---|---|\n${CLASS_ROW} the project's own prose |\n`);
const classAct = (module: Uint8Array = MODULE, overrides: Partial<{ identity: string; type: string; artifact: string; digests: string[] }> = {}) =>
  record(overrides.identity ?? RFC5_ID, overrides.type ?? 'contract-amendment', overrides.artifact ?? RFC5_MODULE_PATH, overrides.digests ?? [sha(module)]);

type Read = Awaited<ReturnType<PublicSourcePolicyActPort['read']>>;
const v2Port = (overrides: Partial<Read> = {}, bytes = policy()): PublicSourcePolicyActPort => ({
  read: async () => ({ actRecord: undefined, policy: bytes, v2ActRecord: policyAct(bytes), classActRecord: classAct(), rfc5Module: MODULE, ...overrides }),
});
const KEY = Buffer.alloc(32, 9);
const allow: CorpusAdmissionPort = { decide: async () => ({ allowed: true, permissionIdentity: 'fixture-consent-v1' }) };

let root = '', commit = '';
beforeAll(() => {
  root = mkdtempSync(join(tmpdir(), 'syzygy-public-screen-v2-'));
  const run = (...args: string[]): string => execFileSync('git', ['-C', root, ...args], { encoding: 'utf8' }).trim();
  run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
  for (const [path, body] of Object.entries(FILES)) { mkdirSync(dirname(join(root, path)), { recursive: true }); writeFileSync(join(root, path), body); }
  run('add', '-A'); run('commit', '-q', '-m', 'fixture');
  commit = run('rev-parse', 'HEAD');
});
afterAll(() => { rmSync(root, { recursive: true, force: true }); });
const cfg = () => ({ repositoryId: 'repository:fixture', revision: commit, include: ['**'], exclude: [], oversize: 'split' as const });
const admitted = async (act: PublicSourcePolicyActPort) => {
  const corpus = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: act, runKey: KEY });
  validateGenerationSources(corpus.sources);
  return { corpus, paths: corpus.sources.filter(source => !source.exclusion.excluded).map(source => source.path).sort() };
};

describe('screening scope v2: project-documentation', () => {
  it('maps the rule paths once the class act is in force, and every screen still applies to them', async () => {
    const screen = await loadPublicSourceScreen(v2Port(), KEY);
    expect(screen.projectDocumentation).toBe('mapped');
    expect(screen.policyVersion).toBe('1.3.0-public-source-candidate.1.none');
    const { corpus, paths } = await admitted(v2Port());
    expect(paths).toEqual([...MAPPED, 'src/clean.c']);
    expect(corpus.count).toMatchObject({ listed: 14, deniedPath: 1, secretDetectorMatches: 2, activeContent: 1, indeterminate: 5 });
    expect(JSON.stringify(corpus)).not.toContain(SENTINEL);
    expect(['README.md', 'src/clean.c', 'docs/adr/0001-choice.md', 'MANIFESTO.md'].map(screen.classifyPath)).toEqual(['project-documentation', 'code-content', undefined, undefined]);
    // Path screens run before the class: a mapped path that is denied or carries a token is withheld for that reason.
    expect(['docs/.env.md', `docs/${PATH_TOKEN}.md`, 'docs/adr/x.md'].map(screen.screenPath)).toEqual(['denied-path', 'secret-detector-match', 'unknown-extraction-class']);
    expect(screen.screenBody(FILES['CHANGELOG.md']!)).toBe('secret-detector-match');
    expect(screen.screenBody(FILES['docs/active.md']!)).toBe('active-content');
  });

  it('maps the opt-in names only in the variant that adds them', async () => {
    for (const [variant, manifesto, architecture] of [['none', false, false], ['manifesto', true, false], ['architecture', false, true], ['both', true, true]] as const) {
      const screen = await loadPublicSourceScreen(v2Port({}, policy(variant)), KEY);
      expect([screen.classifyPath('MANIFESTO.md') !== undefined, screen.classifyPath('docs/architecture/x.md') !== undefined]).toEqual([manifesto, architecture]);
    }
    expect((await admitted(v2Port({}, policy('manifesto')))).paths).toEqual(['LICENSE', 'MANIFESTO.md', 'README.md', 'docs/guide.md', 'licenses/extra.txt', 'src/clean.c']);
  });

  it('a path both classes place is indeterminate', async () => {
    const screen = await loadPublicSourceScreen(v2Port({}, policy('none', scope('none', ['.c', '.md']))), KEY);
    expect(['README.md', 'docs/guide.md', 'src/x.md', 'LICENSE'].map(screen.classifyPath)).toEqual([undefined, undefined, 'code-content', 'project-documentation']);
    expect(screen.screenPath('README.md')).toBe('unknown-extraction-class');
  });
});

describe('screening scope v2: the RFC5-14 prerequisite', () => {
  const unmet: [string, Partial<Read>][] = [
    ['no class act', { classActRecord: undefined }],
    ['no installed module', { rfc5Module: undefined }],
    ['a module that is not the act argument', { rfc5Module: new TextEncoder().encode(`${CLASS_ROW} edited\n`) }],
    ['a module that does not list the class', { rfc5Module: new TextEncoder().encode('# RFC-0005\n'), classActRecord: classAct(new TextEncoder().encode('# RFC-0005\n')) }],
    ['another identity', { classActRecord: classAct(MODULE, { identity: 'RFC5-OTHER-AMEND-2026-10-04' }) }],
    ['another act type', { classActRecord: classAct(MODULE, { type: 'approve-policy' }) }],
    ['another artifact', { classActRecord: classAct(MODULE, { artifact: '.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md' }) }],
    ['two digests', { classActRecord: classAct(MODULE, { digests: [sha(MODULE), sha(MODULE)] }) }],
    ['another project', { classActRecord: classAct().replace('project:syzygy', 'project:other') }],
  ];
  for (const [name, overrides] of unmet) {
    it(`with ${name}, every path the rule names stays indeterminate and the rest of the scope is unchanged`, async () => {
      const screen = await loadPublicSourceScreen(v2Port(overrides), KEY);
      expect(screen.projectDocumentation).toBe('prerequisite-unmet');
      expect(MAPPED.map(screen.screenPath)).toEqual(Array(MAPPED.length).fill('unknown-extraction-class'));
      expect((await admitted(v2Port(overrides))).paths).toEqual(['src/clean.c']);
    });
  }
});

describe('screening scope v2: the policy act gate', () => {
  const refused = (act: PublicSourcePolicyActPort) => expect(loadPublicSourceScreen(act, KEY)).rejects.toThrow(/^Corpus read refused: public-source-policy: /u);
  const v1Policy = policy('none', { contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['.c'] }] } }, '1.2.0-public-source-candidate.1');

  it('reads the v2 act whenever it exists, over a v1 act that no longer matches', async () => {
    const bytes = policy();
    const screen = await loadPublicSourceScreen({ read: async () => ({ actRecord: policyAct(v1Policy, V1_ID), policy: bytes, v2ActRecord: policyAct(bytes), classActRecord: classAct(), rfc5Module: MODULE }) }, KEY);
    expect(screen.policySha256).toBe(sha(bytes));
    // Without the v2 act, the v1 act decides and v2 bytes do not hash to it.
    await expect(loadPublicSourceScreen({ read: async () => ({ actRecord: policyAct(v1Policy, V1_ID), policy: bytes }) }, KEY)).rejects.toThrow(/policy bytes do not hash to the act argument/u);
  });

  it('refuses a v2 act of the wrong identity, type, artifact or digest', async () => {
    const bytes = policy();
    for (const v2ActRecord of [policyAct(bytes, V1_ID), record(V2_ID, 'contract-amendment', PUBLIC_SOURCE_POLICY_PATH, [sha(bytes)]),
      record(V2_ID, 'approve-policy', 'other.json', [sha(bytes)]), record(V2_ID, 'approve-policy', PUBLIC_SOURCE_POLICY_PATH, [sha(bytes), sha(bytes)]), policyAct(v1Policy)])
      await refused(v2Port({ v2ActRecord }, bytes));
  });

  it('refuses a v2 act that names no superseded v1 record', async () => {
    const bytes = policy();
    for (const supersession of ['', 'Supersession / revocation: none recorded by this act.', SUPERSESSION.replace('Supersession / revocation: ', 'Supersession: '),
      SUPERSESSION.replace(PUBLIC_SOURCE_ACT_RECORD_PATH, PUBLIC_SOURCE_V2_ACT_RECORD_PATH)])
      await expect(loadPublicSourceScreen(v2Port({ v2ActRecord: record(V2_ID, 'approve-policy', PUBLIC_SOURCE_POLICY_PATH, [sha(bytes)], supersession) }, bytes), KEY)).rejects.toThrow(/v2 act record names no superseded v1 record/u);
  });

  it('refuses a v2 act over a policy without the rule, and a rule without the v2 act', async () => {
    await expect(loadPublicSourceScreen(v2Port({ v2ActRecord: policyAct(v1Policy) }, v1Policy), KEY)).rejects.toThrow(/the v2 act approves a policy without the project-documentation rule/u);
    const bytes = policy();
    await expect(loadPublicSourceScreen({ read: async () => ({ actRecord: policyAct(bytes, V1_ID), policy: bytes }) }, KEY)).rejects.toThrow(/a project-documentation rule needs the v2 act/u);
  });

  it('refuses a malformed v2 policy', async () => {
    const twice = policy('none', scope('none', ['.c'], [PARITY.rules.none, PARITY.rules.none]));
    await expect(loadPublicSourceScreen(v2Port({}, twice), KEY)).rejects.toThrow(/more than one project-documentation rule/u);
    const unlisted = scope('none');
    unlisted.contentClassification.classesClassified = ['code-structure', 'code-content'];
    await expect(loadPublicSourceScreen(v2Port({}, policy('none', unlisted)), KEY)).rejects.toThrow(/classesClassified does not list project-documentation/u);
    for (const prerequisite of [undefined, { requires: 'x' }]) {
      await expect(loadPublicSourceScreen(v2Port({}, policy('none', { ...scope('none'), prerequisite })), KEY)).rejects.toThrow(/no readable prerequisite/u);
    }
    // The none rule under a manifesto version: the variant and the bytes disagree.
    await expect(loadPublicSourceScreen(v2Port({}, policy('none', scope('none'), '1.3.0-public-source-candidate.1.manifesto')), KEY)).rejects.toThrow(/project-documentation rule: variant manifesto disagrees/u);
  });

  it('the checkout port reads the v2 act, the class act and the installed module by their paths', async () => {
    const dir = mkdtempSync(join(tmpdir(), 'syzygy-public-screen-v2-port-'));
    try {
      const bytes = policy();
      for (const [path, body] of [[PUBLIC_SOURCE_POLICY_PATH, bytes], [PUBLIC_SOURCE_V2_ACT_RECORD_PATH, policyAct(bytes)], [RFC5_CLASS_ACT_RECORD_PATH, classAct()], [RFC5_MODULE_PATH, MODULE]] as const) {
        mkdirSync(dirname(join(dir, path)), { recursive: true }); writeFileSync(join(dir, path), body);
      }
      const read = await checkoutPolicyActPort(dir).read();
      expect(read.actRecord).toBeUndefined();
      expect((await loadPublicSourceScreen(checkoutPolicyActPort(dir), KEY)).projectDocumentation).toBe('mapped');
      writeFileSync(join(dir, PUBLIC_SOURCE_ACT_RECORD_PATH), 'v1');
      expect((await checkoutPolicyActPort(dir).read()).actRecord).toBe('v1');
      rmSync(join(dir, RFC5_MODULE_PATH));
      expect((await loadPublicSourceScreen(checkoutPolicyActPort(dir), KEY)).projectDocumentation).toBe('prerequisite-unmet');
    } finally { rmSync(dir, { recursive: true, force: true }); }
  });
});
