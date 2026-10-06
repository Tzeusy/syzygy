import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { DECISIONS_DIR, POLICY_PATH } from '@syzygy/polaris-generation-consent';
import { renderPolicyAct } from '@syzygy/polaris-generation-consent/testing';
import { afterEach, describe, expect, it } from 'vitest';
import { buildDossierScreen, loadDossierScreen } from './screen.js';

// syzygy-qkea.7 (S6): the screen every blob a check reads passes (REQ-polaris-generation-033, 025). The records root is a temporary
// Syzygy checkout whose policy act is rendered by the real recorder; the policy carries this checkout's detectors and denied paths.

const REAL_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const LIVE = JSON.parse(fs.readFileSync(path.join(REAL_ROOT, POLICY_PATH), 'utf8'));
const NOW = Date.UTC(2026, 9, 7, 12, 0, 0);
const sha = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const policyOf = (scope: unknown = { contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['.c', '.txt'] }] } }, over: Record<string, unknown> = {}): string =>
  `${JSON.stringify({ policyId: 'fixture', policyVersion: '1', detectors: LIVE.detectors, sourceAdmission: LIVE.sourceAdmission, publicSourceScope: scope, ...over }, null, 2)}\n`;
const encode = (text: string): Uint8Array => new TextEncoder().encode(text);

const cleanups: (() => void)[] = [];
afterEach(() => { for (const cleanup of cleanups.splice(0).reverse()) cleanup(); });
const recordsRoot = (policy: string, actArgument: string = sha(policy)): string => {
  const root = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-screen-')));
  cleanups.push(() => fs.rmSync(root, { recursive: true, force: true }));
  for (const [rel, body] of [[POLICY_PATH, policy], [`${DECISIONS_DIR}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`, renderPolicyAct(actArgument, '2026-10-04', '2026-10-04T10:00:00Z')]] as const) {
    fs.mkdirSync(path.dirname(path.join(root, rel)), { recursive: true });
    fs.writeFileSync(path.join(root, rel), body);
  }
  return root;
};

describe('the screen', () => {
  const loaded = buildDossierScreen(encode(policyOf()));
  const screen = loaded.ok ? loaded.screen : null;

  it.each<[string, string | undefined]>([
    ['src/server.c', undefined],
    ['docs/notes.txt', undefined],
    ['README.md', 'unknown-extraction-class'],
    ['src/server.C', 'unknown-extraction-class'],
    ['config/.env', 'denied-path'],
    ['keys/server.pem.c', undefined],
    ['keys/server.pem', 'denied-path'],
    [`docs/${['AK', 'IA'].join('')}${'Q'.repeat(16)}.c`, 'secret-detector-match'],
  ])('screens the path %s', (repositoryPath, outcome) => {
    expect(screen?.screenPath(repositoryPath)).toBe(outcome);
  });

  it.each<[string, string, string | undefined]>([
    ['plain code', 'int main(void) { return 0; }\n', undefined],
    ['a credential assignment', `${['to', 'ken'].join('')} = "${'z'.repeat(12)}"\n`, 'secret-detector-match'],
    ['an HTML tag', 'List<String> names;\n', 'active-content'],
    ['a script element', '<script>run()</script>\n', 'active-content'],
  ])('screens a body with %s', (_name, body, outcome) => {
    expect(screen?.screenBody(body)).toBe(outcome);
  });

  it.each<[string, string]>([
    ['no public-source scope', policyOf(null)],
    ['no code-content extensions', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: [] }] } })],
    ['two code-content rules', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['.c'] }, { class: 'code-content', sourceExtensions: ['.h'] }] } })],
    ['an extension that is a path', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['./c'] }] } })],
    ['unreadable denied-path rules', policyOf(undefined, { sourceAdmission: { deniedPathBasenames: [] } })],
    ['detectors that do not compile', policyOf(undefined, { detectors: [{ id: 'x', kind: 'regular-expression', pattern: '(', flags: 'g' }] })],
    ['no identity', policyOf(undefined, { policyId: 7 })],
    ['bytes that are not JSON', '{'],
  ])('is refused for a policy with %s', (_name, policy) => {
    expect(buildDossierScreen(encode(policy))).toMatchObject({ ok: false });
  });
});

// Parity with the any-repo reader's screen, which these rules copy (TODO(syzygy-qkea.17): move the rules into one shared package, then
// delete the copy and this test). The app module is imported at test time by a computed path, so the package's own build never reaches
// into the app. Both screens are built from the same policy bytes and must agree on every path and body of the population, and on
// which malformed policies they refuse.
const APP_SCREENING = path.join(REAL_ROOT, 'apps/three-surface-poc/src/polaris-generation/public-source-screening.ts');
type AppScreen = { screenPath: (p: string) => string | undefined; screenBody: (b: string) => string | undefined };
const appScreen = async (policy: string): Promise<AppScreen> => {
  const app = await import(APP_SCREENING);
  const port = { read: async () => ({ actRecord: renderPolicyAct(sha(policy), '2026-10-04', '2026-10-04T10:00:00Z'), policy: encode(policy) }) };
  return app.loadPublicSourceScreen(port, new Uint8Array(32).fill(7));
};

describe('parity with the any-repo reader\'s screen (syzygy-qkea.17)', () => {
  const policies: [string, string][] = [
    ['the fixture scope', policyOf()],
    ['a wider scope', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['.md', '.ts', '.json', '.py', '.pem.c'] }] } })],
  ];
  const tracked = execFileSync('git', ['-C', REAL_ROOT, 'ls-files', '-z'], { encoding: 'utf8' }).split('\0').filter(Boolean);
  const paths = [...tracked, 'src/server.c', 'src/server.C', 'config/.env', '.env.local', 'keys/server.pem', 'keys/server.pem.c', 'id_rsa',
    `docs/${['AK', 'IA'].join('')}${'Q'.repeat(16)}.c`, `docs/${['gh', 'p_'].join('')}${'k'.repeat(24)}.txt`, 'a/b/README', 'notes.txt'];
  const bodies = [
    'int main(void) { return 0; }\n', `${['to', 'ken'].join('')} = "${'z'.repeat(12)}"\n`, 'List<String> names;\n', '<script>run()</script>\n',
    `${['-----BEGIN ', 'PRIVATE KEY-----'].join('')}\n`, `https://u:${'p'.repeat(4)}@example.invalid/\n`, '', 'plain words\n',
    '<a href="x">link</a>\n', 'if (a < b && c > d) {}\n', '<!-- note -->\n', `${['api', '_key'].join('')}: ${'q'.repeat(10)}\n`,
  ];

  it.each(policies)('agrees on every path and body under %s', async (_name, policy) => {
    const ours = buildDossierScreen(encode(policy));
    if (!ours.ok) throw new Error(ours.why);
    const theirs = await appScreen(policy);
    expect(paths.length).toBeGreaterThan(1000);
    const pathDisagreements = paths.filter((p) => ours.screen.screenPath(p) !== theirs.screenPath(p));
    const bodyDisagreements = bodies.map((b, i) => [i, ours.screen.screenBody(b), theirs.screenBody(b)]).filter(([, a, b]) => a !== b);
    expect({ pathDisagreements, bodyDisagreements }).toEqual({ pathDisagreements: [], bodyDisagreements: [] });
    // The population exercises every outcome, so agreement is not agreement on one answer.
    expect(new Set(paths.map((p) => ours.screen.screenPath(p) ?? 'admitted'))).toEqual(new Set(['admitted', 'denied-path', 'secret-detector-match', 'unknown-extraction-class']));
    expect(new Set(bodies.map((b) => ours.screen.screenBody(b) ?? 'admitted'))).toEqual(new Set(['admitted', 'secret-detector-match', 'active-content']));
  });

  it.each<[string, string]>([
    ['no public-source scope', policyOf(null)],
    ['no code-content extensions', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: [] }] } })],
    ['two code-content rules', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['.c'] }, { class: 'code-content', sourceExtensions: ['.h'] }] } })],
    ['an extension that is a path', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['./c'] }] } })],
    ['an extension with a double dot', policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['..c'] }] } })],
    ['unreadable denied-path rules', policyOf(undefined, { sourceAdmission: { deniedPathBasenames: [] } })],
    ['detectors that do not compile', policyOf(undefined, { detectors: [{ id: 'x', kind: 'regular-expression', pattern: '(', flags: 'g' }] })],
    ['no identity', policyOf(undefined, { policyId: 7 })],
  ])('refuses a policy with %s, as the app does', async (_name, policy) => {
    expect(buildDossierScreen(encode(policy))).toMatchObject({ ok: false });
    await expect(appScreen(policy)).rejects.toThrow();
  });
});

describe('the screen of the policy in force', () => {
  it('loads the policy the act chain puts in force, naming its digest', async () => {
    const policy = policyOf();
    const result = await loadDossierScreen(recordsRoot(policy), NOW);
    expect(result).toMatchObject({ ok: true, screen: { policyId: 'fixture', policyVersion: '1', policySha256: sha(policy) } });
  });

  it('refuses a policy whose bytes are not the act\'s argument', async () => {
    const policy = policyOf();
    expect(await loadDossierScreen(recordsRoot(policy, sha(`${policy} `)), NOW)).toMatchObject({ ok: false, why: expect.stringContaining('no screening policy is in force') });
  });

  it('refuses a policy changed between the act check and the read the screen is built from', async () => {
    const policy = policyOf();
    const edited = policyOf({ contentClassification: { rules: [{ class: 'code-content', sourceExtensions: ['.md'] }] } });
    expect(await loadDossierScreen(recordsRoot(policy), NOW, () => Buffer.from(edited))).toEqual({
      ok: false, why: 'the screening policy changed after its act was checked; its bytes differ from the act\'s argument',
    });
  });

  it('refuses before the act takes effect', async () => {
    expect(await loadDossierScreen(recordsRoot(policyOf()), Date.UTC(2026, 9, 3))).toMatchObject({ ok: false });
  });

  // syzygy-s6xo: this checkout's own state, read from the tree, so the pin holds on either side of the sitting that records the
  // screening acts: refused while no screening-scope act is recorded, built once one is and the policy declares the scope.
  it('builds the screen on this checkout exactly when a screening-scope act is recorded and the policy declares the scope', async () => {
    const recorded = ['PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md', 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md']
      .some(file => fs.existsSync(path.join(REAL_ROOT, DECISIONS_DIR, file)));
    const load = await loadDossierScreen(REAL_ROOT, Date.now());
    if (!recorded) expect(load).toEqual({ ok: false, why: 'no screening policy is in force: no screening-scope policy act is recorded' });
    else if (Object.hasOwn(LIVE, 'publicSourceScope')) expect(load).toMatchObject({ ok: true });
    else expect(load).toEqual({ ok: false, why: 'the screening policy cannot be applied: it carries no publicSourceScope' });
  });
});
