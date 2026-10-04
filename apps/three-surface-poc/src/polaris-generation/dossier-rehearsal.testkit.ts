/**
 * Dossier dry-run rehearsal: `poc:dossier` end to end against a synthetic Redis-shaped repository and a loopback stub provider, with
 * the owner's pre-flight questions asked of what comes out. Model-free and network-free: every request goes to a 127.0.0.1 stub that
 * returns scripted, schema-valid stage outputs; the repository is generated, never fetched; the admission records are the recorders'
 * own acts over the real egress bytes in a scratch root. A passing rehearsal says the wiring behaves; it says nothing about a real
 * model's output or a real provider's behaviour ([Unknown] until the first real call).
 *
 * This is a testkit file because it imports `@syzygy/polaris-generation-provider/testing`, which production code must not.
 */
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { DECISIONS_DIR, EGRESS_V2_INSTANCE, INSTANCES_DIR, POLICY_PATH } from '@syzygy/polaris-generation-consent';
import { renderPolicyAct, renderRecorderAct } from '@syzygy/polaris-generation-consent/testing';
import { createMessagesApiGenerate, minimumUsageUnits } from '@syzygy/polaris-generation-provider';
import { LOOPBACK_FOR_TESTS } from '@syzygy/polaris-generation-provider/testing';
import {
  DOSSIER_REQUESTED_ASSETS, dossierQuestionsFile, evaluateDossier, parseDossierManifest, promptForStage,
  type GenerationSource, type PromptProfile, type PromptStage,
} from '@syzygy/polaris-generation-core';

import { fixturePolicyActPort, fixtureRouteRoot } from './dossier-fixtures.testkit.js';
import type { ProviderFactory } from './dossier-generation.js';
import { main } from './dossier-main.js';
import { renderDossier } from './dossier-render.js';
import { buildRedisShapedFixture } from './redis-shaped-fixture.js';
import { startStubProvider, type StubRequest } from './stub-provider.testkit.js';

export const REHEARSAL_FORMAT = 'polaris-dossier-rehearsal-v1';
const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
export const CREDENTIAL = 'SYZYGY_POLARIS_PROVIDER_API_KEY';
export const STUB_KEY = 'sk-rehearsal-0123456789';
const TARGET = 'https://github.com/redis/redis';
const STAGES = ['inventory', 'plan', 'author', 'edit', 'repair', 'fidelity', 'discovery-map', 'discovery-reduce'] as const;
/** Stage ceilings of the dossier-units-v1 accounting policy, as the wiring enforces them. */
const CEILING: Record<string, number> = { 'discovery-map': 40, 'discovery-reduce': 40, inventory: 600, plan: 300, author: 600, edit: 600, fidelity: 300, repair: 300 };
const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const profileDigest = (stage: PromptStage, profile: PromptProfile): string => sha256(promptForStage(stage, profile).system);

/** A synthetic repository and its pinned commit. */
export interface RehearsalFixture { readonly name: FixtureName; readonly dir: string; readonly commit: string; readonly files: number; readonly oversizeFiles: number }
export type FixtureName = 'small' | 'redis-shaped';

function buildSmallFixture(dir: string): RehearsalFixture {
  const git = (...args: string[]): string => execFileSync('git', ['-C', dir, ...args], { encoding: 'utf8' }).trim();
  const files: Record<string, string> = {
    'README.md': '# Synthetic key-value server\n\nIt keeps keys in memory and answers commands over a socket.\n',
    'src/server.c': 'int main(void) { return serve(); }\n', 'src/db.c': 'int lookup(const char *key) { return 0; }\n', 'src/db.h': 'int lookup(const char *key);\n',
  };
  mkdirSync(dir, { recursive: true });
  git('init', '-q'); git('config', 'user.email', 'f@example.invalid'); git('config', 'user.name', 'F');
  for (const [file, body] of Object.entries(files)) { mkdirSync(path.dirname(path.join(dir, file)), { recursive: true }); writeFileSync(path.join(dir, file), body); }
  git('add', '-A'); git('commit', '-qm', 'synthetic fixture');
  return { name: 'small', dir, commit: git('rev-parse', 'HEAD'), files: Object.keys(files).length, oversizeFiles: 0 };
}

export function buildFixture(name: FixtureName, parent: string): RehearsalFixture {
  if (name === 'small') return buildSmallFixture(path.join(parent, 'small'));
  const built = buildRedisShapedFixture(path.join(parent, 'redis-shaped'));
  return { name, dir: path.join(parent, 'redis-shaped'), commit: built.commit, files: built.files.size, oversizeFiles: built.oversize.length };
}

export interface RehearsalCheck { readonly id: string; readonly passed: boolean; readonly detail: string }
export interface ScenarioReport {
  readonly scenario: string;
  readonly fixture: FixtureName;
  readonly intent: string;
  readonly expectedExit: number;
  readonly exit: number;
  readonly state: string | null;
  readonly stagesRequested: readonly string[];
  readonly checks: readonly RehearsalCheck[];
  readonly passed: boolean;
}
export interface RehearsalReport {
  readonly format: typeof REHEARSAL_FORMAT;
  readonly providerCallPerformed: false;
  readonly network: 'loopback stub only';
  readonly fixtures: readonly { readonly name: FixtureName; readonly files: number; readonly oversizeFiles: number; readonly commit: string }[];
  readonly scenarios: readonly ScenarioReport[];
  readonly passed: boolean;
}

// ---------------------------------------------------------------------------
// The scripted provider: a well-formed reply for each stage, computed from the request's own inputs.

type Json = Record<string, any>;   // eslint-disable-line @typescript-eslint/no-explicit-any

/** The stage a request's system text belongs to under the dossier profile, or `unknown` (a manifesto prompt on the wire is a wiring fault). */
export const stageOfSystem = (system: string): string => STAGES.find(stage => promptForStage(stage, 'dossier').system === system) ?? 'unknown';

export function scriptedReply(request: StubRequest): string {
  const stage = stageOfSystem(request.system);
  const inputs: Json = (JSON.parse(request.input) as Json).inputs;
  if (stage === 'discovery-map') return JSON.stringify({ claims: inputs.items.map((item: Json) => ({ blobId: item.blobId, claim: 'Relevant to the reader questions.', relevance: 5 })) });
  if (stage === 'discovery-reduce') {
    const ids: string[] = inputs.subsystems.flatMap((s: Json) => s.claims.map((c: Json) => c.blobId));
    return JSON.stringify({ ranked: ids.filter((id, i) => ids.indexOf(id) === i).slice(0, inputs.maxSelected) });
  }
  // The plan stage lists the whole counted population, excluded rows included; only the quotable ones can be cited.
  const sources: string[] = inputs.sources.filter((s: Json) => s.excluded !== true).map((s: Json) => s.sourceId);
  const cited = sources;   // the draft cites every source it was given, as the pipeline requires
  const sections: Json[] = DOSSIER_REQUESTED_ASSETS.filter(a => a.kind === 'section') as unknown as Json[];
  const produced = (id: string) => ({ kind: 'produced', assetIds: [id] });
  if (stage === 'inventory') {
    return JSON.stringify({ entries: sources.map((id, i) => ({ id: `entry-${i}`, sourceIds: [id], statement: `Source ${i} states a purpose.`, kind: 'purpose', disposition: produced('core-ideas') })) });
  }
  if (stage === 'plan') {
    return JSON.stringify({ sections: sections.map(s => ({ id: s.id, title: s.id, reason: 'A reader question asks for it.', sourceIds: cited, disposition: produced(s.id) })) });
  }
  const block = (id: string, text: string) => ({ id, text, sourceIds: cited, children: [] });
  if (stage === 'fidelity') {
    const draft: Json = inputs.draft;
    const blocks: Json[] = [draft.introduction, ...draft.sections.flatMap((s: Json) => s.paragraphs.flatMap((b: Json) => [b, ...b.children])),
      ...draft.diagrams.flatMap((d: Json) => [...d.nodes, ...d.edges]), ...draft.deepDives.flatMap((d: Json) => d.paragraphs.flatMap((b: Json) => [b, ...b.children]))];
    return JSON.stringify({
      inventoryCoverage: inputs.inventory.entries.map((e: Json) => ({ entryId: e.id, disposition: 'represented', blockIds: ['intro'], reason: 'The introduction states it.' })),
      blockSupport: blocks.map(b => ({ blockId: b.id, verdict: 'supported', sourceIds: b.sourceIds, reason: 'The cited span states it.' })),
      findings: [],
    });
  }
  return JSON.stringify({
    title: 'Rehearsal dossier', introduction: { id: 'intro', text: 'The project does a thing.', sourceIds: cited },
    sections: sections.map(s => ({ id: s.id, title: s.id, paragraphs: [block(`${s.id}-p`, `Input supplies the output for ${s.id}.`)], disposition: produced(s.id) })),
    diagrams: [{ id: 'workflow-diagram', title: 'Workflow', sectionId: 'end-to-end-workflows', kind: 'flow', relationship: 'How input becomes output', disposition: produced('workflow-diagram'),
      nodes: [{ id: 'n1', label: 'input', sourceIds: cited, epistemic: 'observed' }, { id: 'n2', label: 'output', sourceIds: cited, epistemic: 'observed' }],
      edges: [{ id: 'e1', from: 'n1', to: 'n2', label: 'supplies', sourceIds: cited, epistemic: 'observed' }] }],
    deepDives: [{ id: 'mechanism-deep-dive', title: 'Mechanism', sectionId: 'mechanisms', paragraphs: [block('deep-p', 'The mechanism is a function.')], disposition: produced('mechanism-deep-dive') }],
    unresolved: [],
  });
}

// ---------------------------------------------------------------------------
// Scratch admission root: the recorders' own acts over the real egress bytes, the observation record pinned to the fixture commit.

function admissionRoot(commit: string, withObservation: boolean): string {
  const root = fixtureRouteRoot('messages-api');
  const put = (rel: string, body: string): void => { mkdirSync(path.dirname(path.join(root, rel)), { recursive: true }); writeFileSync(path.join(root, rel), body); };
  const v2 = readFileSync(path.join(REPO_ROOT, EGRESS_V2_INSTANCE), 'utf8');
  put(EGRESS_V2_INSTANCE, v2);
  put(`${DECISIONS_DIR}/PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md`, renderRecorderAct('egress-anthropic-v2', sha256(v2), '2026-09-01', '2026-09-01T09:30:00Z'));
  if (withObservation) {
    const realObs = readFileSync(path.join(REPO_ROOT, INSTANCES_DIR, 'redis/OBSERVATION-CONSENT.md'), 'utf8');
    const obs = realObs.replace(/^\| `([^`\n]+)` \| `[0-9a-f]+` \|$/gm, (_m, label: string) => `| \`${label}\` | \`${commit}\` |`);
    put(`${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`, obs);
    put(`${DECISIONS_DIR}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md`, renderRecorderAct('redis-observation', sha256(obs), '2026-09-01', '2026-09-01T09:30:00Z'));
  }
  const policy = `${JSON.stringify({ policyVersion: '1.2.0-public-source-candidate.1', publicSourceScope: { rules: [] } }, null, 1)}\n`;
  put(POLICY_PATH, policy);
  put(`${DECISIONS_DIR}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md`, renderPolicyAct(sha256(policy), '2026-09-01', '2026-09-01T09:30:00Z'));
  return root;
}

const loopback = (url: string): ProviderFactory => build => createMessagesApiGenerate({ model: build.profile.model, apiKey: build.apiKey, upstream: { url, loopbackForTests: LOOPBACK_FOR_TESTS },
  permitted: build.permitted, effort: build.profile.effort, thinking: build.profile.thinking, maxOutputTokens: build.profile.maxOutputTokens });

// ---------------------------------------------------------------------------
// Checks on what a run leaves behind.

const walk = (dir: string): string[] => readdirSync(dir).flatMap(entry => { const f = path.join(dir, entry); return statSync(f).isDirectory() ? walk(f) : [f]; });
const check = (id: string, passed: boolean, detail: string): RehearsalCheck => ({ id, passed, detail });

/** "The rendered dossier opens": every page is a complete document, links nothing outside the run directory, and every internal link and fragment lands. */
export function inspectSite(runDir: string): RehearsalCheck[] {
  if (!existsSync(runDir)) return [check('site-opens', false, 'there is no run directory')];
  const files = walk(runDir).map(f => path.relative(runDir, f)).filter(f => f.endsWith('.html')).sort();
  if (!files.includes('index.html')) return [check('site-opens', false, 'index.html is missing')];
  const problems: string[] = [];
  const text = new Map(files.map(f => [f, readFileSync(path.join(runDir, f), 'utf8')]));
  for (const [file, html] of text) {
    if (!/^<!doctype html>/iu.test(html) || !/<main[\s>]/u.test(html) || !/<title>[^<]+<\/title>/u.test(html)) problems.push(`${file}: not a complete document`);
    if (!/<meta http-equiv="Content-Security-Policy"/u.test(html)) problems.push(`${file}: no content security policy`);
    if (/<script[\s>]/iu.test(html)) problems.push(`${file}: contains a script`);
    for (const match of html.matchAll(/\s(?:href|src)="([^"]*)"/gu)) {
      const target = match[1]!.replaceAll('&amp;', '&');
      if (/^[a-z][a-z0-9+.-]*:/iu.test(target) || target.startsWith('//')) { problems.push(`${file}: external reference ${target}`); continue; }
      const [rel, fragment] = target.split('#') as [string, string | undefined];
      const resolved = rel === '' ? file : path.posix.normalize(path.posix.join(path.posix.dirname(file), rel));
      const targetHtml = text.get(resolved);
      if (!existsSync(path.join(runDir, resolved))) problems.push(`${file}: broken link ${target}`);
      else if (fragment !== undefined && fragment !== '' && targetHtml !== undefined && !targetHtml.includes(`id="${fragment}"`)) problems.push(`${file}: no anchor ${target}`);
    }
  }
  return [check('site-opens', problems.length === 0, problems.length === 0 ? `${files.length} pages: complete documents, no script, no external reference, every internal link and anchor lands` : problems.slice(0, 5).join('; '))];
}

/** Every dossier page through `evaluateDossier`: no fidelity failures of any kind, and the reader cost measured. */
export async function evaluatePages(runDir: string, sources: readonly GenerationSource[]): Promise<RehearsalCheck[]> {
  try { return await evaluateRun(runDir, sources); }
  catch (error) { return [check('pages-evaluate', false, `the evaluator refused the run: ${error instanceof Error ? error.message : 'unknown'}`)]; }
}

async function evaluateRun(runDir: string, sources: readonly GenerationSource[]): Promise<RehearsalCheck[]> {
  const manifestText = readFileSync(path.join(runDir, 'dossier.json'), 'utf8');
  const manifest = parseDossierManifest(manifestText);
  const pages = new Map(manifest.pages.map(page => [page.path, new TextEncoder().encode(readFileSync(path.join(runDir, page.path), 'utf8'))]));
  const report = await evaluateDossier({ manifestText, pages, sources, questionsText: dossierQuestionsFile() }, new AbortController().signal);
  const f = report.fidelity;
  const outcomes = { quotes: f.quotes.outcome, claims: f.claims.outcome, inBlockQuotes: f.inBlockQuotes.outcome };
  const failing = Object.entries(outcomes).filter(([, outcome]) => outcome === 'failures').map(([name]) => name);
  return [
    check('pages-evaluate', failing.length === 0, failing.length === 0
      ? `${manifest.pages.length} pages; quotes ${f.quotes.exact}/${f.quotes.denominator} exact, claims ${f.claims.labelled}/${f.claims.denominator} labelled, in-block quotes ${outcomes.inBlockQuotes}`
      : `fidelity failures in: ${failing.join(', ')}`),
    check('pages-all-claims-labelled', f.claims.denominator > 0 && f.claims.labelled === f.claims.denominator, `${f.claims.labelled} of ${f.claims.denominator} claims carry an epistemic label`),
  ];
}

// ---------------------------------------------------------------------------
// Scenarios.

export interface Ran {
  readonly exit: number;
  readonly outcome: { state?: string; detail?: string } | null;
  readonly text: string;
  readonly runDir: string;
  readonly stages: readonly string[];
  readonly requests: readonly StubRequest[];
  readonly fetched: readonly string[];
  readonly sources: readonly GenerationSource[] | null;
  readonly envAfter: Record<string, string | undefined>;
  readonly record: Json | null;
  readonly fixture: RehearsalFixture;
}
export interface ScenarioDef {
  readonly name: string;
  readonly fixture: FixtureName;
  readonly intent: string;
  readonly expectExit: number;
  /** The trigger's clock, to age a run past its wall-clock allowance without waiting. */
  readonly clock?: () => () => number;
  readonly env?: Record<string, string>;
  readonly withObservation?: boolean;
  readonly args?: (runDir: string) => readonly string[];
  readonly respond?: (request: StubRequest) => string;
  /** Tokens the stub reports per stage, to make every call cost exactly its ceiling. */
  readonly costAtCeiling?: boolean;
  readonly checks: (ran: Ran) => Promise<RehearsalCheck[]> | RehearsalCheck[];
}

/** The outcome state with its detail, so a failed check says why the run stopped. */
const stateDetail = (r: Ran): string => `state ${String(r.outcome?.state)}${r.outcome?.detail === undefined ? '' : ` (${r.outcome.detail})`}`;
/** Consecutive repeats of a stage collapsed: `discovery-map x24 > discovery-reduce > inventory`. */
const stageSummary = (stages: readonly string[]): string => stages.reduce<[string, number][]>((acc, s) => { const last = acc[acc.length - 1]; if (last?.[0] === s) last[1]++; else acc.push([s, 1]); return acc; }, []).map(([s, n]) => (n > 1 ? `${s} x${n}` : s)).join(' > ');
const quotableBytes = (sources: readonly GenerationSource[]): number => sources.reduce((sum, x) => sum + x.spans.reduce((n, span) => n + Buffer.byteLength(span.text), 0), 0);
const recordOf = (runDir: string): Json | null => { try { return JSON.parse(readFileSync(path.join(runDir, 'run-record.json'), 'utf8')) as Json; } catch { return null; } };
export const noCheckout = (r: Ran): RehearsalCheck => check('no-checkout', !r.fetched.includes('checkout'), r.fetched.includes('checkout') ? 'the repository was checked out' : 'the repository content was never checked out (a metadata listing is allowed)');
export const nothingSent = (r: Ran): RehearsalCheck => check('nothing-sent', r.requests.length === 0, `${r.requests.length} requests reached the stub`);
export const noRunDir = (r: Ran): RehearsalCheck => check('no-run-directory', !existsSync(r.runDir), existsSync(r.runDir) ? 'a run directory was written' : 'no run directory');

/** The record names the profile the run was started under, the prompt digest of every call, and the budget it spent. */
export function recordChecks(r: Ran, opts: { readonly expectCeilingSpend?: boolean } = {}): RehearsalCheck[] {
  const rec = r.record;
  if (rec === null || rec.generation === undefined) return [check('record-present', false, 'run-record.json carries no generation record')];
  const g = rec.generation as Json;
  const calls: Json[] = g.calls;
  const stale = calls.filter(call => call.promptDigest !== profileDigest(call.stage as PromptStage, 'dossier'));
  const manifestoWire = calls.filter(call => call.promptDigest === profileDigest(call.stage as PromptStage, 'manifesto') && profileDigest(call.stage as PromptStage, 'manifesto') !== profileDigest(call.stage as PromptStage, 'dossier'));
  const wireDigests = new Set(r.requests.map(q => sha256(q.system)));
  const spend = g.spend as { discoveryCountedUnits: number; narrativeCountedUnits: number };
  const budget = g.budget as { runTotalUnits: number; discoveryUnits: number; narrativeUnits: number };
  const out = [
    check('record-profile', rec.profile === 'dossier-v1', `run profile ${String(rec.profile)}`),
    check('record-prompt-profile', g.promptProfile === 'dossier', `prompt profile ${String(g.promptProfile)}${manifestoWire.length > 0 ? ' (manifesto prompts were sent)' : ''}`),
    check('record-prompt-digests', calls.length > 0 && stale.length === 0 && calls.every(call => wireDigests.has(call.promptDigest)),
      stale.length === 0 ? `${calls.length} calls, each naming the sha256 of the dossier-profile prompt for its stage, and each seen on the wire` : `${stale.length} calls name a digest that is not the dossier prompt for their stage`),
    check('record-budget', spend.discoveryCountedUnits <= budget.discoveryUnits && spend.narrativeCountedUnits <= budget.narrativeUnits
      && spend.discoveryCountedUnits + spend.narrativeCountedUnits <= budget.runTotalUnits,
    `spent ${spend.discoveryCountedUnits} discovery + ${spend.narrativeCountedUnits} narrative of ${budget.discoveryUnits} + ${budget.narrativeUnits} (run total ${budget.runTotalUnits}); accounting ${String(g.accountingPolicy)}`),
    check('record-usage-known', calls.every(call => call.usageUnknown === false), `${calls.filter(call => call.usageUnknown !== false).length} calls with unknown usage`),
  ];
  if (opts.expectCeilingSpend === true) {
    const expected = calls.reduce((sum, call) => sum + (CEILING[call.stage] ?? 0) * (call.phase === 'discovery' ? 1 : 1), 0);
    out.push(check('record-ceiling-spend', calls.every(call => call.countedUnits <= (CEILING[call.stage] ?? 0)) && spend.discoveryCountedUnits + spend.narrativeCountedUnits <= expected,
      `every call held to its stage ceiling; total ${spend.discoveryCountedUnits + spend.narrativeCountedUnits} of ${expected} at ceiling`));
  }
  return out;
}

export const completeChecks = async (r: Ran): Promise<RehearsalCheck[]> => [
  check('state-complete', r.outcome?.state === 'complete', stateDetail(r)),
  check('stage-order', JSON.stringify(r.stages.filter(s => !s.startsWith('discovery'))) === JSON.stringify(['inventory', 'plan', 'author', 'edit', 'fidelity']) && r.stages.some(s => s === 'discovery-map'),
    `stages ${stageSummary(r.stages)}`),
  check('no-unknown-stage', !r.stages.includes('unknown'), r.stages.includes('unknown') ? 'a request carried a system text that is not a dossier-profile stage prompt' : 'every request carried a dossier-profile stage prompt'),
  check('credential-consumed', !(CREDENTIAL in r.envAfter) && r.requests.every(q => !q.raw.includes(STUB_KEY)), 'read once, removed from the environment, in no request body'),
  ...inspectSite(r.runDir), ...(r.sources === null ? [check('pages-evaluate', false, 'the renderer was never reached')] : await evaluatePages(r.runDir, r.sources)),
  ...recordChecks(r),
];

/** The stages whose request carries the selected sources' text. */
const SOURCE_STAGES = ['inventory', 'author', 'edit', 'fidelity'] as const;

export const SCENARIOS: readonly ScenarioDef[] = [
  { name: 'complete-small', fixture: 'small', expectExit: 0, intent: 'A normal run on a four-file repository: discovery, the five narrative stages, a rendered dossier that opens, evaluates cleanly and is accounted for in the run record.', checks: completeChecks },
  {
    name: 'complete-redis-shaped', fixture: 'redis-shaped', expectExit: 0,
    intent: 'The same run on the Redis-shaped corpus (510 files, five over 100,000 characters): discovery selects up to 200 sources and the narrative must be able to afford them.',
    checks: async r => [
      check('selection-fits-every-source-carrying-stage', r.sources !== null && SOURCE_STAGES.every(stage => minimumUsageUnits(quotableBytes(r.sources!)) <= (CEILING[stage] ?? 0)),
        r.sources === null ? 'no sources' : `${r.sources.filter(x => x.spans.length > 0).length} quotable sources, ${quotableBytes(r.sources)} bytes of text, at least ${minimumUsageUnits(quotableBytes(r.sources))} units (1 token per byte bound) per request; ceilings ${SOURCE_STAGES.map(stage => `${stage} ${CEILING[stage]}`).join(', ')}`),
      ...await completeChecks(r),
    ],
  },
  {
    name: 'at-ceiling', fixture: 'small', expectExit: 0, costAtCeiling: true, intent: 'Every reply costs exactly its permit: the run still lands inside the budget and no call exceeds its stage ceiling.',
    checks: r => [check('state-complete', r.outcome?.state === 'complete', stateDetail(r)), ...recordChecks(r, { expectCeilingSpend: true }),
      check('max-tokens-capped', r.requests.every(q => q.maxTokens <= (CEILING[stageOfSystem(q.system)] ?? 0) * 1000), 'no request asked for more output than its stage ceiling allows')],
  },
  {
    name: 'partial', fixture: 'small', expectExit: 7, intent: 'The plan reply is invalid: the run stops, the inventory already done is rendered, nothing after the plan is requested.',
    respond: request => (stageOfSystem(request.system) === 'plan' ? '{}' : scriptedReply(request)),
    checks: r => [
      check('state-partial', r.outcome?.state === 'generation-stopped-partial', stateDetail(r)),
      check('no-later-stage', !r.stages.some(s => ['author', 'edit', 'fidelity', 'repair'].includes(s)), `stages ${stageSummary(r.stages)}`),
      check('partial-render', existsSync(path.join(r.runDir, 'index.html')) && existsSync(path.join(r.runDir, 'run-record.json')), 'a partial page and the run record were written'),
      ...recordChecks(r),
    ],
  },
  {
    name: 'wall-clock', fixture: 'small', expectExit: 6, intent: 'Discovery uses the whole two-hour allowance (the clock jumps): the narrative never starts, and the record alone is kept.',
    clock: () => { let calls = 0; const start = Date.now(); return () => start + (calls++ === 0 ? 0 : 8_000_000); },
    checks: r => [
      check('state-stopped', r.outcome?.state === 'generation-stopped', stateDetail(r)),
      check('no-narrative-stage', !r.stages.some(s => !s.startsWith('discovery')), `stages ${stageSummary(r.stages)}`),
      check('record-only', existsSync(path.join(r.runDir, 'run-record.json')) && !existsSync(path.join(r.runDir, 'index.html')), 'run-record.json written, no page'),
    ],
  },
  {
    name: 'refused-no-credential', fixture: 'small', expectExit: 5, env: {}, intent: 'No provider credential: refused before the repository is checked out or anything is sent.',
    checks: r => [check('state-unavailable', r.outcome?.state === 'generation-unavailable', stateDetail(r)), nothingSent(r), noRunDir(r), noCheckout(r)],
  },
  {
    name: 'refused-no-consent', fixture: 'small', expectExit: 3, withObservation: false, intent: 'No observation consent for the target: refused as admission-missing before the repository content is read or anything is sent.',
    checks: r => [check('state-admission-missing', r.outcome?.state === 'admission-missing', stateDetail(r)), nothingSent(r), noRunDir(r), noCheckout(r)],
  },
  {
    name: 'refused-bad-input', fixture: 'small', expectExit: 2, args: runDir => ['not-a-url', '--route', 'messages-api', '--out', runDir, '--json'], intent: 'A target that is not a GitHub repository URL: exit 2, nothing read or sent.',
    checks: r => [nothingSent(r), noRunDir(r), noCheckout(r), check('nothing-listed', r.fetched.length === 0, `${r.fetched.length} repository operations`)],
  },
];

export const SCENARIO_NAMES: readonly string[] = SCENARIOS.map(s => s.name);

export async function runScenario(def: ScenarioDef, fixture: RehearsalFixture, scratch: string, observe?: (ran: Ran) => void): Promise<ScenarioReport> {
  const fetched: string[] = [];
  let captured: readonly GenerationSource[] | null = null;
  const respond = def.respond ?? scriptedReply;
  const stub = await startStubProvider(request => {
    const stage = stageOfSystem(request.system);
    return def.costAtCeiling === true
      ? { text: respond(request), inputTokens: 1000, outputTokens: ((CEILING[stage] ?? 1) - 1) * 1000 }
      : { text: respond(request) };
  });
  const out: string[] = [], progress: string[] = [];
  const runDir = path.join(mkdtempSync(path.join(scratch, 'out-')), 'run');
  const env: Record<string, string | undefined> = def.env === undefined ? { [CREDENTIAL]: STUB_KEY } : { ...def.env };
  let exit: number;
  try {
    exit = await main([...(def.args?.(runDir) ?? [TARGET, '--route', 'messages-api', '--out', runDir, '--json'])],
      {
        lsRemote: () => { fetched.push('ls-remote'); return `${fixture.commit}\tHEAD\n`; },
        materialize: async () => { fetched.push('checkout'); return fixture.dir; },
        policyAct: fixturePolicyActPort(['.c', '.h', '.md', '.txt', '.tcl', '.sh']),
        render: ({ result, sources }) => { captured = sources; return renderDossier({ result, sources, requestedAssets: DOSSIER_REQUESTED_ASSETS }); },
        ...(def.clock === undefined ? {} : { now: def.clock() }),
      },
      { root: admissionRoot(fixture.commit, def.withObservation !== false), env, providerFactory: loopback(stub.url), stdout: t => out.push(t), stderr: t => progress.push(t) });
  } finally { await stub.close(); }
  const text = out.join('');
  let outcome: Ran['outcome'] = null;
  try { outcome = JSON.parse(text) as Ran['outcome']; } catch { /* a usage message or a plain-text refusal */ }
  const ran: Ran = { exit, outcome, text, runDir, stages: stub.requests.map(q => stageOfSystem(q.system)), requests: stub.requests, fetched, sources: captured, envAfter: env,
    record: existsSync(runDir) ? recordOf(runDir) : null, fixture };
  observe?.(ran);
  const checks = [check('exit-code', exit === def.expectExit, `exit ${exit}, expected ${def.expectExit}`), ...await def.checks(ran)];
  return { scenario: def.name, fixture: def.fixture, intent: def.intent, expectedExit: def.expectExit, exit, state: outcome?.state ?? null, stagesRequested: ran.stages, checks, passed: checks.every(c => c.passed) };
}

/** Builds each needed synthetic repository once, runs every named scenario (default: all), and removes its scratch space. */
export async function rehearse(options: { readonly scenarios?: readonly string[]; readonly keepScratch?: (directory: string) => void; readonly observe?: (scenario: string, ran: Ran) => void } = {}): Promise<RehearsalReport> {
  const wanted = options.scenarios ?? SCENARIO_NAMES;
  const unknown = wanted.filter(name => !SCENARIO_NAMES.includes(name));
  if (unknown.length > 0) throw new Error(`unknown-scenario: ${unknown.join(', ')}`);
  const selected = SCENARIOS.filter(s => wanted.includes(s.name));
  const scratch = mkdtempSync(path.join(tmpdir(), 'syzygy-rehearsal-'));
  try {
    const fixtures = new Map<FixtureName, RehearsalFixture>();
    for (const def of selected) if (!fixtures.has(def.fixture)) fixtures.set(def.fixture, buildFixture(def.fixture, scratch));
    const reports: ScenarioReport[] = [];
    for (const def of selected) reports.push(await runScenario(def, fixtures.get(def.fixture)!, scratch, options.observe === undefined ? undefined : ran => options.observe!(def.name, ran)));
    return {
      format: REHEARSAL_FORMAT, providerCallPerformed: false, network: 'loopback stub only',
      fixtures: [...fixtures.values()].map(({ name, files, oversizeFiles, commit }) => ({ name, files, oversizeFiles, commit })),
      scenarios: reports, passed: reports.length > 0 && reports.every(r => r.passed),
    };
  } finally {
    if (options.keepScratch === undefined) rmSync(scratch, { recursive: true, force: true });
    else options.keepScratch(scratch);
  }
}

/** The human summary: one line per scenario, then every failed check. */
export function formatRehearsal(report: RehearsalReport): string {
  const lines = [`Dossier rehearsal (${REHEARSAL_FORMAT}): ${report.passed ? 'PASS' : 'FAIL'}. Loopback stub only; no model, no network, no real repository.`,
    ...report.fixtures.map(f => `Fixture ${f.name}: ${f.files} files (${f.oversizeFiles} over 100,000 characters) at ${f.commit.slice(0, 12)}.`)];
  for (const s of report.scenarios) {
    lines.push(`${s.passed ? 'PASS' : 'FAIL'}  ${s.scenario.padEnd(24)} exit ${s.exit} (expected ${s.expectedExit})  ${s.checks.filter(c => c.passed).length}/${s.checks.length} checks`);
    for (const c of s.checks.filter(c => !c.passed)) lines.push(`      ${c.id}: ${c.detail}`);
  }
  return `${lines.join('\n')}\n`;
}
