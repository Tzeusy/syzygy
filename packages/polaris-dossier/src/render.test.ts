import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest';
import { evaluateDossier, parseDossierManifest, scanDossierPage } from '@syzygy/polaris-generation-core';
import { issueBrief } from './brief.js';
import { checkDraft, type CheckDeps } from './check.js';
import { runDossierCli } from './cli.js';
import { NO_PROJECT_INPUT, NO_PROVIDER_STATEMENTS, type GateSources, type GateState } from './gate-sources.js';
import { checkInventory } from './inventory.js';
import { NO_RENDERER, renderRun, type DossierRenderer, type DossierRendererInput, type RenderDeps } from './render.js';
import { reviewCheck, reviewPacket } from './review.js';
import { parseRunConfig } from './run-config.js';
import { NO_WORK_ITEM_REASON, encodeRunRecord, type RunSubject } from './run-record.js';
import { buildDossierScreen } from './screen.js';
import { launchForm, sessionPrompt } from './session-handover.js';

// syzygy-qkea.10 (S9a): `render` (REQ-polaris-generation-033, 034, 036). The clone is a real Git repository built here with the git
// CLI. Most cases draw through the real multi-page dossier renderer of apps/three-surface-poc, loaded by file URL because this package
// does not depend on that app (the `syzygy` composition root injects it; syzygy-qkea.19 moves it into a package). Expected byte offsets
// are found in the fixture strings here, object identifiers come from `git rev-parse`, and texts are literals written before the code ran.

const REAL_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const RENDERER_MODULE = pathToFileURL(path.join(REAL_ROOT, 'apps/three-surface-poc/src/polaris-generation/dossier-render.ts')).href;
const GIT_ENV = { ...process.env, GIT_CONFIG_GLOBAL: '/dev/null', GIT_CONFIG_SYSTEM: '/dev/null', GIT_AUTHOR_DATE: '2026-10-01T00:00:00Z', GIT_COMMITTER_DATE: '2026-10-01T00:00:00Z' };
const NOW = Date.UTC(2026, 9, 7, 12, 0, 0);
const LATER = NOW + 60_000;
const RUN_ID = `run-${'f'.repeat(32)}`;

const KESTREL = [
  '/* Kestrel keeps every key in memory.',
  ' * Each command **runs to completion** before',
  ' * the next one starts. */',
  'int main(void) { return 0; }',
  '// Café über: snapshots are written periodically.',
  '',
].join('\n');
const NOTES = 'Café notes.\nSnapshots are written periodically.\n';
const SECRETS = 'Deploy notes.\n';
const FILES: Record<string, string> = { 'src/kestrel.c': KESTREL, 'docs/notes.txt': NOTES, 'README.md': '# Kestrel\n', '.env': 'X=1\n', 'docs/deploy.md': SECRETS };
const LIVE_POLICY = JSON.parse(fs.readFileSync(path.join(REAL_ROOT, '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json'), 'utf8'));
const policy = (extensions: string[]): Uint8Array => new TextEncoder().encode(JSON.stringify({
  policyId: 'fixture-public-source', policyVersion: '1', detectors: LIVE_POLICY.detectors, sourceAdmission: LIVE_POLICY.sourceAdmission,
  publicSourceScope: { contentClassification: { rules: [{ class: 'code-content', sourceExtensions: extensions }] } },
}));
const SCREEN = buildDossierScreen(policy(['.c', '.txt']));

let origin: string, commit: string;
const objectIds: Record<string, string> = {};
let renderDossier: DossierRenderer;
beforeAll(async () => {
  renderDossier = ((await import(RENDERER_MODULE)) as { renderDossier: DossierRenderer }).renderDossier;
  origin = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-render-origin-')));
  const git = (...args: string[]): string => execFileSync('git', ['-C', origin, ...args], { encoding: 'utf8', env: GIT_ENV }).trim();
  git('init', '-q', '-b', 'main');
  for (const [file, body] of Object.entries(FILES)) {
    fs.mkdirSync(path.dirname(path.join(origin, file)), { recursive: true });
    fs.writeFileSync(path.join(origin, file), body);
  }
  git('add', '-A');
  git('-c', 'user.name=t', '-c', 'user.email=t@example.invalid', 'commit', '-q', '-m', 'fixture');
  commit = git('rev-parse', 'HEAD');
  for (const file of Object.keys(FILES)) objectIds[file] = git('rev-parse', `${commit}:${file}`);
});
afterAll(() => fs.rmSync(origin, { recursive: true, force: true }));

const cleanups: (() => void)[] = [];
afterEach(() => { for (const cleanup of cleanups.splice(0).reverse()) cleanup(); });
const tempDir = (prefix: string): string => {
  const dir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), prefix)));
  cleanups.push(() => fs.rmSync(dir, { recursive: true, force: true }));
  return dir;
};

const subject = (clone: string): RunSubject => ({
  repository: { url: 'https://github.com/redis/redis', repositoryId: 'redis-redis' },
  clone: { path: clone, declaredBy: 'operator', label: 'Inferred', use: 'read' },
  pinnedRevision: { commit, label: 'fixture', consentRecord: 'PUBLIC-OBS-FIXTURE@1', pinnedAt: '2026-10-07T11:00:00.000Z' },
  startGates: { registryEntry: 'REGISTRY-ACT-FIXTURE', screeningPolicy: 'POLICY-ACT-FIXTURE' },
  governed: { kind: 'non-governed', because: ['the project input fixture states that no kernel evidence drawer exists'] },
  providerStatement: null,
  workItem: { identity: null, reason: NO_WORK_ITEM_REASON },
});
const OK: GateState = { state: 'ok', record: 'FIXTURE-ACT' };
const RULING_ABSENT: GateState = { state: 'absent', why: 'no owner-act record binds it' };
const sources = (ruling: GateState = { state: 'ok', record: 'RFC7-20-RULING-FIXTURE' }): GateSources => ({
  recordsRoot: REAL_ROOT,
  repositoryIdsFor: async () => ['redis-redis'],
  consentedRevisionsFor: async () => [],
  observationConsentFor: async (_id, revision) => (revision === commit ? { satisfied: true, record: 'PUBLIC-OBS-FIXTURE@1' } : { satisfied: false, why: 'the consent does not name it' }),
  registryEntry: async () => OK,
  screeningPolicy: async () => OK,
  d9: async () => OK,
  rfc720Ruling: async () => ruling,
  projectInput: NO_PROJECT_INPUT,
  providerStatements: NO_PROVIDER_STATEMENTS,
});
const neverProbe = { probe: async () => { throw new Error('the credential probe must not run after a brief that permits no execution'); } };
const checkDeps = (): CheckDeps => ({ sources: sources(), now: () => LATER, probe: neverProbe, loadScreen: async () => SCREEN });
const renderDeps = (overrides: Partial<RenderDeps> = {}): RenderDeps => ({ sources: sources(), now: () => LATER, probe: neverProbe, loadScreen: async () => SCREEN, renderer: renderDossier, ...overrides });

type Doc = Record<string, any>; // eslint-disable-line @typescript-eslint/no-explicit-any
const cite = (id: string, file = 'src/kestrel.c', startLine = 1, endLine = 5) => ({ id, path: file, startLine, endLine });
const UNDERSTANDING = ['purpose', 'beneficiary', 'proposition', 'capabilities', 'components', 'choices', 'tradeOffs', 'limits', 'terminology', 'contradictions', 'openQuestions'];
const AGENT_ONLY = 'So it is fast 5512.';
const draft = (): Doc => ({
  schemaVersion: 'polaris-dossier-local-draft-v1',
  pinnedRevision: commit,
  sessionId: 'authoring-session-1',
  title: 'Kestrel',
  introduction: { id: 'intro', label: 'inferred', basis: 'source', text: `The project states: "Kestrel keeps every key in memory." ${AGENT_ONLY}`, citations: [cite('c-intro', 'src/kestrel.c', 1, 1)], quotations: ['c-intro'] },
  understanding: Object.fromEntries(UNDERSTANDING.map((key) => [key, [{ id: `u-${key}`, label: 'inferred', statement: `Understanding of ${key} 8841.`, scope: 'The server.', citations: [cite(`u-${key}-c`)] }]])),
  sections: [{
    id: 'core-ideas', title: 'Core ideas',
    paragraphs: [
      { id: 'p1', label: 'inferred', basis: 'source', text: 'The project states: "Each command runs to completion before the next one starts."', citations: [cite('c-p1', 'src/kestrel.c', 2, 3)], quotations: ['c-p1'], children: [
        { id: 'p1a', label: 'unknown', reason: 'missing-evidence', text: 'No source says how keys expire.', citations: [] },
        { id: 'p1b', label: 'non-normative', text: 'Read on.' },
      ] },
      { id: 'p2', label: 'inferred', basis: 'source', text: 'The project states: "Snapshots are written periodically."', citations: [cite('c-p2', 'docs/notes.txt', 2, 2)], quotations: ['c-p2'], children: [] },
    ],
    disposition: { kind: 'produced', assetIds: ['core-ideas'] },
  }],
  diagrams: [],
  deepDives: [],
  unresolved: [],
  discovery: { inspected: ['src/kestrel.c', 'README.md'], selected: [], excluded: [], unresolved: [], deferred: [], stoppingReason: 'Read the server first, then the notes.' },
  clarifications: [],
  executions: [],
});
const inventory = (): Doc => ({
  schemaVersion: 'polaris-dossier-local-inventory-v1',
  pinnedRevision: commit,
  sessionId: 'inventory-1',
  entries: [
    { id: 'e-purpose', kind: 'purpose', label: 'inferred', statement: 'The project states: "Kestrel keeps every key in memory."', citations: [cite('c-e-purpose', 'src/kestrel.c', 1, 1)], quotations: ['c-e-purpose'] },
    { id: 'e-snap', kind: 'capability', label: 'inferred', statement: 'It writes snapshots.', citations: [cite('c-e-snap', 'docs/notes.txt', 2, 2)], quotations: [] },
  ],
  coverage: { inspected: ['src/kestrel.c', 'docs/notes.txt'], excluded: [], deferred: [], stoppingReason: 'Read every file.' },
});
const verdict = (packetSha256: string): Doc => ({
  schemaVersion: 'polaris-dossier-local-fidelity-verdict-v1',
  pinnedRevision: commit,
  packetSha256,
  sessionId: 'reviewer-1',
  inventoryCoverage: [
    { entryId: 'e-purpose', disposition: 'represented', blockIds: ['intro'], reason: 'The introduction says it.', quotations: [] },
    { entryId: 'e-snap', disposition: 'represented', blockIds: ['p2'], reason: 'p2 says it.', quotations: [] },
  ],
  inventoryAccuracy: [
    { entryId: 'e-purpose', accuracy: 'accurate', spanIds: ['span-1'], reason: 'The span says it.', quotations: [] },
    { entryId: 'e-snap', accuracy: 'accurate', spanIds: ['span-0'], reason: 'The span says it.', quotations: [] },
  ],
  blockSupport: [
    { blockId: 'intro', verdict: 'supported', spanIds: [], reason: 'The span says it.', quotations: [] },
    { blockId: 'p1', verdict: 'anchor-does-not-support', spanIds: [], reason: 'The span does not say it.', quotations: [] },
    { blockId: 'p1a', verdict: 'supported', spanIds: [], reason: 'Unknown fits the packet.', quotations: [] },
    { blockId: 'p1b', verdict: 'supported', spanIds: [], reason: 'Non-normative fits.', quotations: [] },
    { blockId: 'p2', verdict: 'supported', spanIds: [], reason: 'The span says it.', quotations: [] },
  ],
  findings: [],
  readiness: 'not-ready',
});

/** A briefed run with a passed draft revision; with `reviewed`, an inventory of record and a counted fidelity review. */
async function prepared(doc: Doc = draft(), reviewed = true): Promise<string> {
  const clone = path.join(tempDir('dossier-render-clone-'), 'kestrel');
  execFileSync('git', ['clone', '-q', '--no-hardlinks', origin, clone], { env: GIT_ENV });
  const run = path.join(tempDir('dossier-render-state-'), RUN_ID);
  fs.mkdirSync(run);
  const parsed = parseRunConfig(JSON.stringify({
    operator: 'Tzeusy', agentTool: 'claude-code', agentToolVersion: '2.1.0', agentProvider: 'anthropic', model: 'claude-opus-5-5',
    deadline: 'PT1H', agentTokenBudget: 100_000, maxRepairCycles: 3, maxQuestions: 1, audience: 'an operator', operatorIsOwner: true,
  }));
  if (!parsed.ok) throw new Error('fixture configuration refused');
  fs.writeFileSync(path.join(run, 'run.json'), encodeRunRecord(parsed.config, subject(clone)));
  const brief = await issueBrief(run, { sources: sources(), now: () => NOW });
  if (!brief.ok) throw new Error(`fixture brief refused: ${brief.refusal.reason}`);
  fs.mkdirSync(path.join(run, 'drafts'), { recursive: true });
  fs.writeFileSync(path.join(run, 'drafts', 'next.json'), JSON.stringify(doc, null, 2));
  const checked = await checkDraft(run, {}, checkDeps());
  if (!checked.ok || checked.report.outcome !== 'passed') throw new Error(`fixture draft: ${JSON.stringify(checked.ok ? checked.report.findings : checked.refusal)}`);
  if (!reviewed) return run;
  const handed = await sessionPrompt(run, { role: 'inventory' }, { sources: sources(), now: () => LATER });
  if (!handed.ok) throw new Error(handed.refusal.reason);
  fs.writeFileSync(path.join(handed.report.directory, 'inventory.json'), JSON.stringify(inventory(), null, 2));
  const inv = await checkInventory(run, {}, checkDeps());
  if (!inv.ok || inv.report.outcome !== 'passed') throw new Error(`fixture inventory: ${JSON.stringify(inv.ok ? inv.report.findings : inv.refusal)}`);
  await launchForm(run, { role: 'inventory', form: 'terminal' }, { sources: sources(), now: () => LATER });
  const packet = await reviewPacket(run, { kind: 'fidelity' }, { sources: sources(), now: () => LATER, loadScreen: async () => SCREEN });
  if (!packet.ok) throw new Error(packet.refusal.reason);
  const review = await sessionPrompt(run, { role: 'review', kind: 'fidelity' }, { sources: sources(), now: () => LATER, loadScreen: async () => SCREEN });
  if (!review.ok) throw new Error(review.refusal.reason);
  const spans = JSON.parse(fs.readFileSync(path.join(review.report.directory, 'packet.json'), 'utf8')).spans as { id: string; path: string; startLine: number }[];
  const v = verdict(packet.report.packetSha256);
  v.inventoryAccuracy[0].spanIds = spans.filter((span) => span.path === 'src/kestrel.c' && span.startLine === 1).slice(0, 1).map((span) => span.id);
  v.inventoryAccuracy[1].spanIds = spans.filter((span) => span.path === 'docs/notes.txt').map((span) => span.id);
  v.blockSupport[0].spanIds = v.inventoryAccuracy[0].spanIds;
  v.blockSupport[4].spanIds = v.inventoryAccuracy[1].spanIds;
  fs.writeFileSync(path.join(review.report.directory, 'verdict.json'), JSON.stringify(v, null, 2));
  const validated = await reviewCheck(run, {}, { sources: sources(), now: () => LATER, loadScreen: async () => SCREEN });
  if (!validated.ok || validated.report.outcome !== 'validated') throw new Error(`fixture verdict: ${JSON.stringify(validated.ok ? validated.report.problems : validated.refusal)}`);
  await launchForm(run, { role: 'review', form: 'terminal' }, { sources: sources(), now: () => LATER });
  return run;
}

/** The renderer, recording what it was given. */
function capturing(): { renderer: DossierRenderer; inputs: DossierRendererInput[] } {
  const inputs: DossierRendererInput[] = [];
  return { inputs, renderer: (input) => { inputs.push(input); return renderDossier(input); } };
}
const readSite = (site: string): Map<string, string> => {
  const out = new Map<string, string>();
  const walk = (dir: string): void => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full); else out.set(path.relative(site, full), fs.readFileSync(full, 'utf8'));
    }
  };
  walk(site);
  return out;
};
const byteOffset = (body: string, needle: string): number => Buffer.byteLength(body.slice(0, body.indexOf(needle)));
/** The marking and Unknown reason on the opening tag of the claim with this id. */
const marked = (page: string, id: string): { epistemic: string; reason: string | null } => {
  const tag = page.match(new RegExp(`<[a-z]+[^>]*data-claim-id="${id.replace(/[/]/gu, '\\/')}"[^>]*>`, 'u'))?.[0] ?? '';
  return { epistemic: tag.match(/data-epistemic="([^"]+)"/u)?.[1] ?? 'none', reason: tag.match(/data-unknown-reason="([^"]+)"/u)?.[1] ?? null };
};
const html = (files:ReadonlyMap<string, string>): [string, string][] => [...files].filter(([file]) => file.endsWith('.html'));

describe('render', () => {
  it('refuses with no renderer wired, before it opens the run, and writes nothing', async () => {
    const run = await prepared(draft(), false);
    const before = fs.readdirSync(run).sort();
    expect(await renderRun(run, renderDeps({ renderer: undefined }))).toMatchObject({ ok: false, refusal: { command: 'render', outcome: 'refused', stage: 'renderer', reason: NO_RENDERER } });
    expect(fs.readdirSync(run).sort()).toEqual(before);
  });

  it('renders every quotation as the bytes Syzygy located in the blob it read now, with an RFC7-10 anchor', async () => {
    const run = await prepared();
    const { renderer, inputs } = capturing();
    const result = await renderRun(run, renderDeps({ renderer }));
    if (!result.ok) throw new Error(result.refusal.reason);
    expect(result.report).toMatchObject({
      outcome: 'rendered', site: path.join(run, 'site', '0'), draftRevision: 0, draftLayer: { state: 'editorial-draft' },
      fidelityReview: { counts: true, label: 'Observed' }, quotations: { rendered: 3, withheld: 0, label: 'Observed' }, sources: { admitted: 2, excluded: 0 },
    });
    const files = readSite(result.report.site);
    const pages = html(files).map(([, page]) => page).join('\n');
    // The agent wrote "runs to completion before the next one starts."; the blob carries the emphasis and a line break, and the page shows the blob's bytes.
    const p1Start = byteOffset(KESTREL, 'Each command'), p1End = byteOffset(KESTREL, 'starts.') + 'starts.'.length;
    expect(pages).toContain(`data-quote-start="${p1Start}" data-quote-end="${p1End}">Each command **runs to completion** before\n * the next one starts.</q>`);
    const p2Start = byteOffset(NOTES, 'Snapshots'); // 13: "Café" is five bytes
    expect(p2Start).toBe(13);
    expect(pages).toContain(`data-quote-start="${p2Start}" data-quote-end="${p2Start + 35}">Snapshots are written periodically.</q>`);
    expect(pages).toContain(`data-anchor-class="evidence-artifact-identifier-with-integrity-digest" data-anchor-identifier="${objectIds['docs/notes.txt']}" data-anchor-algorithm="sha1" data-anchor-fragment="${p2Start}-${p2Start + 35}" data-anchor-target-state="${commit}"`);
    expect(pages).toContain(`data-anchor-identifier="${objectIds['src/kestrel.c']}" data-anchor-algorithm="sha1" data-anchor-fragment="${p1Start}-${p1End}" data-anchor-target-state="${commit}"`);
    // The evaluation harness finds every quote exact against the sources and every claim labelled, with no duplicate claim.
    const manifestText = files.get('dossier.json')!;
    const manifest = parseDossierManifest(manifestText);
    const report = await evaluateDossier({
      manifestText, pages: new Map(manifest.pages.map((page) => [page.path, new TextEncoder().encode(files.get(page.path)!)])), sources: inputs[0]!.sources,
      questionsText: JSON.stringify({ format: 'polaris-reader-questions-v1', questions: [{ id: 'q1', topics: ['mechanisms'], text: 'How does it work?' }] }),
    }, new AbortController().signal);
    expect(report.fidelity.quotes).toMatchObject({ denominator: 5, exact: 5, failures: [], outcome: 'all-resolved' });
    expect(report.fidelity.claims).toMatchObject({ duplicateClaimIds: [], outcome: 'all-labelled' });
    expect(report.scanFindings).toEqual([]);
  });

  it('labels blocks by the agent\'s label, the counted review and screening, and keeps the pages and machine view in parity per tuple', async () => {
    const run = await prepared();
    const result = await renderRun(run, renderDeps());
    if (!result.ok) throw new Error(result.refusal.reason);
    const files = readSite(result.report.site);
    const tuples = html(files).flatMap(([file, page]) => scanDossierPage(page).claims.map((claim) => `${file} ${claim.id} ${claim.epistemic}`)).sort();
    const machine = JSON.parse(files.get('machine.json')!);
    const machineTuples = (machine.claims as { page: string; id: string; epistemic: string }[]).map((claim) => `${claim.page} ${claim.id} ${claim.epistemic}`).sort();
    expect(tuples).toEqual(machineTuples);
    const marking = (id: string): string | undefined => tuples.find((tuple) => tuple.split(' ')[1] === id)?.split(' ')[2];
    expect(marking('intro')).toBe('inferred'); // supported
    expect(marking('p2')).toBe('inferred'); // supported
    expect(marking('p1')).toBe('unknown'); // the review judged its anchor does not support it
    expect(marking('p1a')).toBe('unknown'); // the agent's own Unknown
    expect(marking('p1b')).toBeUndefined(); // non-normative: no claim
    expect(machine.nonNormative).toEqual([{ page: 'index.html', id: 'p1b' }]);
    expect(marked(files.get('index.html')!, 'p1')).toEqual({ epistemic: 'unknown', reason: 'missing-evidence' });
    expect(files.get('index.html')).toMatch(/data-non-normative[^>]*>Read on\.[^<]*<span class="marking[^"]*">\[Non-normative\]/u);
    // The fidelity review page: the binding Observed, the verdict Inferred, the design review Unknown.
    expect(marking('review/fidelity/binding')).toBe('observed');
    expect(marking('review/fidelity/verdict')).toBe('inferred');
    expect(marking('review/design/none')).toBe('unknown');
    // Discovery: the agent's account Inferred, the objects this render read Observed.
    expect(marking('discovery/inspected')).toBe('inferred');
    expect(tuples.filter((tuple) => tuple.split(' ')[1]!.startsWith('discovery/read/')).map((tuple) => tuple.split(' ')[2])).toEqual(['observed', 'observed']);
  });

  it('carries the run disclosure on every page and in the machine view, and one review-status region per page holding no claim', async () => {
    const run = await prepared();
    const result = await renderRun(run, renderDeps());
    if (!result.ok) throw new Error(result.refusal.reason);
    const files = readSite(result.report.site);
    const machine = JSON.parse(files.get('machine.json')!);
    const ids = (machine.disclosure as { id: string }[]).map((item) => item.id);
    expect(ids).toEqual(['mode', 'agent', 'unrestricted-reading', 'read-account', 'execution-rule', 'reported-commands', 'no-provider-call', 'pinned-revision',
      'pinned-revision-verified', 'quotations', 'stored-records', 'records-within-reach', 'unattributed-execution', 'draft-layer']);
    expect(html(files).length).toBeGreaterThan(5);
    for (const [file, page] of html(files)) {
      expect(page.split('class="run-disclosure"').length - 1, file).toBe(1);
      for (const id of ids) expect(page, `${file} ${id}`).toContain(`data-disclosure-id="${id}"`);
      const regions = page.split('data-review-status-region="review-status"');
      expect(regions.length - 1, file).toBe(1);
      const region = regions[1]!.slice(0, regions[1]!.indexOf('</aside>'));
      expect(region, file).not.toContain('data-claim-id');
      expect(region, file).not.toMatch(/ id="/u);
    }
    expect(files.get('index.html')).toContain('Agent tool claude-code 2.1.0, provider anthropic, model claude-opus-5-5');
    expect(files.get('index.html')).toContain('Syzygy made no provider call and transmitted no project content.');
  });

  it('withholds the draft layer as Unknown while the RFC7-20 ruling is not in force, keeping sources, disclosure and discovery', async () => {
    const run = await prepared();
    const result = await renderRun(run, renderDeps({ sources: sources(RULING_ABSENT) }));
    if (!result.ok) throw new Error(result.refusal.reason);
    expect(result.report.draftLayer).toEqual({ state: 'unknown', reason: 'unconsented-source-or-provider', why: ['the owner\'s reading of RFC7-20 (POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05, item 1) is not in force: no owner-act record binds it'] });
    expect(result.report.quotations.rendered).toBe(0);
    const files = readSite(result.report.site);
    const all = [...files.values()].join('\n');
    expect(all).not.toContain(AGENT_ONLY);
    expect(all).not.toContain('8841');
    expect(files.has('understanding.html')).toBe(false);
    expect(files.has('discovery.html')).toBe(true);
    expect(marked(files.get('index.html')!, 'draft-layer/policy-state')).toEqual({ epistemic: 'unknown', reason: 'unconsented-source-or-provider' });
    expect(files.get('index.html')).toContain('Dossier of https://github.com/redis/redis at ');
    expect([...files.keys()].filter((file) => file.startsWith('sources/') && file !== 'sources/index.html')).toHaveLength(2);
    expect(JSON.parse(files.get('machine.json')!).draftLayer.state).toBe('unknown');
  });

  it('withholds a quotation from a file screening excludes and renders its block Unknown, with no source page for that file', async () => {
    const doc = draft();
    doc.sections[0].paragraphs[1] = { id: 'p2', label: 'inferred', basis: 'source', text: 'The project states: "Deploy notes."', citations: [cite('c-p2', 'docs/deploy.md', 1, 1)], quotations: ['c-p2'], children: [] };
    const run = await prepared(doc, false);
    const result = await renderRun(run, renderDeps());
    if (!result.ok) throw new Error(result.refusal.reason);
    expect(result.report).toMatchObject({ fidelityReview: { counts: false }, quotations: { withheld: 1 }, sources: { admitted: 1, excluded: 1 } });
    const files = readSite(result.report.site);
    expect(marked(files.get('index.html')!, 'p2')).toEqual({ epistemic: 'unknown', reason: 'excluded-content' });
    expect([...files.keys()].filter((file) => file.startsWith('sources/') && file !== 'sources/index.html')).toHaveLength(1);
    expect([...files.values()].filter((page) => page.includes('Deploy notes.')).length).toBe(0);
    // With no counted review, an Inferred-labelled block is Unknown for missing evidence.
    expect(marked(files.get('index.html')!, 'intro')).toEqual({ epistemic: 'unknown', reason: 'missing-evidence' });
  });

  it('screens at render with the policy in force now, not the one the check applied', async () => {
    const run = await prepared(draft(), false);
    const result = await renderRun(run, renderDeps({ loadScreen: async () => buildDossierScreen(policy(['.c'])) }));
    if (!result.ok) throw new Error(result.refusal.reason);
    expect(result.report).toMatchObject({ quotations: { rendered: 2, withheld: 1 }, sources: { admitted: 1, excluded: 1 } });
    const files = readSite(result.report.site);
    expect(marked(files.get('index.html')!, 'p2')).toEqual({ epistemic: 'unknown', reason: 'excluded-content' });
    expect([...files.values()].filter((page) => page.includes('Snapshots are written periodically.')).length).toBe(0);
  });

  it('refuses when an object at the pinned revision can no longer be read, and writes nothing', async () => {
    const run = await prepared(draft(), false);
    const clone = JSON.parse(fs.readFileSync(path.join(run, 'run.json'), 'utf8')).subject.clone.path as string;
    fs.rmSync(path.join(clone, '.git', 'objects'), { recursive: true, force: true });
    fs.mkdirSync(path.join(clone, '.git', 'objects'));
    expect(await renderRun(run, renderDeps())).toMatchObject({ ok: false, refusal: { stage: 'object-read' } });
    expect(fs.existsSync(path.join(run, 'site'))).toBe(false);
  });

  it('refuses when the stored passed draft revision is altered, after the deadline, and when the output lacks the disclosure', async () => {
    const run = await prepared(draft(), false);
    expect(await renderRun(run, renderDeps({ now: () => NOW + 3_600_000 }))).toMatchObject({ ok: false, refusal: { stage: 'deadline' } });
    const bare: DossierRenderer = (input) => ({ files: new Map([...renderDossier(input).files].map(([file, page]) => [file, page.replace('class="run-disclosure"', 'class="x"')])) });
    expect(await renderRun(run, renderDeps({ renderer: bare }))).toMatchObject({ ok: false, refusal: { stage: 'render' } });
    expect(await renderRun(run, renderDeps({ renderer: () => { throw new Error('boom'); } }))).toMatchObject({ ok: false, refusal: { stage: 'render', reason: 'the renderer refused the run: boom' } });
    expect(fs.existsSync(path.join(run, 'site'))).toBe(false);
    fs.appendFileSync(path.join(run, 'drafts', 'rev-0.json'), ' ');
    expect(await renderRun(run, renderDeps())).toMatchObject({ ok: false, refusal: { stage: 'draft' } });
  });

  it('writes each render into a new numbered site directory and never over an earlier one', async () => {
    const run = await prepared(draft(), false);
    const first = await renderRun(run, renderDeps());
    const second = await renderRun(run, renderDeps());
    if (!first.ok || !second.ok) throw new Error('render refused');
    expect([first.report.site, second.report.site]).toEqual([path.join(run, 'site', '0'), path.join(run, 'site', '1')]);
    expect(fs.readdirSync(path.join(run, 'site')).sort()).toEqual(['0', '1']);
  });

  it('is the `render` command of the CLI, which refuses when the composition root injects no renderer', async () => {
    const run = await prepared(draft(), false);
    const capture = () => { const out = { stdout: '', stderr: '' }; return { out, io: { stdout: (t: string) => { out.stdout += t; }, stderr: (t: string) => { out.stderr += t; } } }; };
    const ports = { sources: sources(), now: () => LATER, loadScreen: async () => SCREEN };
    const a = capture();
    expect(await runDossierCli(['render', run, '--json'], a.io, ports)).toBe(1);
    expect(JSON.parse(a.out.stdout)).toMatchObject({ stage: 'renderer', reason: NO_RENDERER });
    const b = capture();
    expect(await runDossierCli(['render', run, '--json'], b.io, { ...ports, renderer: renderDossier })).toBe(0);
    expect(JSON.parse(b.out.stdout)).toMatchObject({ format: 'polaris-dossier-render/1', outcome: 'rendered', site: path.join(run, 'site', '0') });
  });
});

