import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';

import { clarify, DOSSIER_DISCOVERY_BUDGET, DiscoveryRefusal, discoverAndSelect, DOSSIER_PROFILE_ID, DOSSIER_READER_QUESTIONS, DOSSIER_REQUESTED_ASSETS,
  type ClarificationRecord, type DiscoveryBudget, type DiscoveryCall, type DiscoveryPorts, type DiscoveryReceipt, type DiscoveryReport, type GenerationBudget, type GenerationSource, type GenerationStage,
  type PipelineRequest, type PipelineResult } from '@syzygy/polaris-generation-core';

import { buildPipelineRequest, CorpusRefusal, type CorpusAdmissionPort, type ReaderConfig, type RepoCorpus } from './repo-corpus.js';
import { DOSSIER_RUN_PROFILE, narrativeBudgetFor } from './dossier-run-profile.js';
import { readScreenedRepoCorpus, type PublicSourcePolicyActPort } from './public-source-screening.js';
import { checkDossierRunDestination, writeDossierRun } from './dossier-render-main.js';
import { ISOLATED_GIT_FLAGS, minimalGitEnv } from './isolated-git.js';

/** `repositoryId` is only a label (a collision-free spelling of owner and repo) when parsed; `runDossierTrigger` replaces it with the id the matching observation record carries before any requirement is built. */
export interface GithubTarget { readonly owner: string; readonly repo: string; readonly ref?: string; readonly url: string; readonly repositoryId: string }

/** Public https://github.com/<owner>/<repo> only, optionally `/tree/<ref>`. No credentials, no other host. */
export function parseGithubUrl(input: string): GithubTarget {
  const match = /^https:\/\/github\.com\/([A-Za-z0-9][A-Za-z0-9-]{0,38})\/([A-Za-z0-9._-]{1,100}?)(?:\.git)?(?:\/tree\/([A-Za-z0-9._\/-]{1,200}))?\/?$/u.exec(input);
  if (match === null || match[2] === '.' || match[2] === '..' || (match[3] ?? '').split('/').some(part => part === '..')) throw new Error('invalid-github-url');
  const [, owner, repo, ref] = match as unknown as [string, string, string, string | undefined];
  return { owner, repo, ...(ref === undefined ? {} : { ref }), url: `https://github.com/${owner}/${repo}`, repositoryId: `github:${owner}:${repo.replace(/[_.]/gu, ch => (ch === '_' ? '__' : '_d'))}` };
}

/** Picks the commit for a ref (or HEAD) from `git ls-remote` output. An annotated tag resolves to the commit it peels to. */
export function pinRevision(lsRemoteOutput: string, ref?: string): { readonly revision: string; readonly resolvedRef: string } {
  const rows = lsRemoteOutput.split('\n').filter(Boolean).map(line => {
    const m = /^([0-9a-f]{40}|[0-9a-f]{64})\t(\S+)$/u.exec(line);
    if (m === null) throw new Error('unreadable-ls-remote');
    return { sha: m[1]!, name: m[2]! };
  });
  const find = (name: string): string | undefined => rows.find(row => row.name === name)?.sha;
  const candidates = ref === undefined ? ['HEAD'] : [`refs/tags/${ref}^{}`, `refs/tags/${ref}`, `refs/heads/${ref}`];
  for (const name of candidates) { const sha = find(name); if (sha !== undefined) return { revision: sha, resolvedRef: name.replace(/\^\{\}$/u, '') }; }
  if (ref !== undefined && /^[0-9a-f]{40}$/u.test(ref)) throw new Error('unpinnable-revision: a bare commit cannot be confirmed by ls-remote');
  throw new Error('revision-not-found');
}

/** Metadata only: ref names and commit ids, never a repository body. Runs with a minimal environment. */
export function gitLsRemote(url: string, allowProtocol = 'https'): string {
  const home = mkdtempSync(join(tmpdir(), 'syzygy-lsremote-'));
  try {
    return execFileSync('git', [...ISOLATED_GIT_FLAGS, ...fileOverride(allowProtocol), 'ls-remote', '--', url], { encoding: 'utf8', timeout: 30_000, maxBuffer: 16_000_000,
      env: minimalGitEnv(home, allowProtocol), cwd: home });
  } finally { rmSync(home, { recursive: true, force: true }); }
}

const fileOverride = (allowProtocol: string): readonly string[] => (allowProtocol === 'file' ? ['-c', 'protocol.file.allow=always'] : []);

export type AdmissionKind = 'observation-consent' | 'public-source-policy' | 'egress-consent';
export interface AdmissionRequirement { readonly kind: AdmissionKind; readonly repositoryId: string; readonly revision: string; readonly url: string; readonly needs: string }
export type AdmissionAnswer = { readonly satisfied: true; readonly record: string } | { readonly satisfied: false; readonly why: string };
export interface AdmissionRecordsPort {
  readonly source: string;
  /** The repository ids of every observation record whose `Upstream:` is exactly this canonical URL. The trigger never derives the id it admits under: it uses the one record's id, and refuses on zero or several. */
  readonly repositoryIdsFor: (url: string) => Promise<readonly string[]>;
  readonly check: (requirement: AdmissionRequirement) => Promise<AdmissionAnswer>;
}
/** With no store wired, no record exists, and the report says so. */
export const noAdmissionRecords: AdmissionRecordsPort = {
  source: 'no record store is wired into this command',
  repositoryIdsFor: async () => [],
  check: async () => ({ satisfied: false, why: 'no record found: no admission record store is wired' }),
};

export function admissionRequirements(target: GithubTarget, revision: string): readonly AdmissionRequirement[] {
  const base = { repositoryId: target.repositoryId, revision, url: target.url };
  return [
    { ...base, kind: 'observation-consent', needs: `Observation consent for ${target.repositoryId} covering revision ${revision}: permission to read its snapshot objects, shallow, without execution or writes` },
    { ...base, kind: 'public-source-policy', needs: `Screening, secret and classification policy scope that covers ${target.repositoryId}` },
    { ...base, kind: 'egress-consent', needs: `Provider egress consent listing ${target.repositoryId} as a source whose text may leave the machine` },
  ];
}

/** A satisfied answer is exactly `satisfied: true` with a non-empty record string; any other shape from a record store is an unmet gate, never a pass. */
export function soundAnswer(answer: unknown): AdmissionAnswer {
  const a = answer as { satisfied?: unknown; record?: unknown; why?: unknown } | null;
  if (a === null || typeof a !== 'object') return { satisfied: false, why: 'malformed admission answer: not an object' };
  if (a.satisfied === true) {
    return typeof a.record === 'string' && a.record.trim().length > 0 ? { satisfied: true, record: a.record } : { satisfied: false, why: 'malformed admission answer: satisfied without a record' };
  }
  return { satisfied: false, why: a.satisfied === false && typeof a.why === 'string' ? a.why : 'malformed admission answer: satisfied is not a boolean' };
}

/** What the generation session needs to know about the run it serves. */
export interface GenerationOpenContext {
  readonly target: GithubTarget;
  readonly revision: string;
  /** The run directory the trigger will write; it does not exist yet. */
  readonly runDir: string;
  /** The egress requirement that admitted this run. */
  readonly egress: AdmissionRequirement;
  readonly records: AdmissionRecordsPort;
}
/** Provider-backed generation for one run: opened after every admission record is satisfied and before any repository object is fetched. */
export interface GenerationSession {
  readonly discovery: Pick<DiscoveryPorts, 'map' | 'reduce'>;
  readonly discoveryReceipt: (receipt: DiscoveryReceipt) => Promise<void>;
  /** Asked before each discovery call, besides the egress record: the discovery share and the stage authority. */
  readonly discoveryPermitted: (call: DiscoveryCall) => Promise<boolean>;
  readonly discoveryBudget: DiscoveryBudget;
  /** The narrative's budget after discovery used `elapsedMs` of the run's wall clock. */
  readonly narrativeBudget: (elapsedMs: number) => GenerationBudget;
  readonly wallClockMs: number;
  readonly routes: Readonly<Record<GenerationStage, string>>;
  readonly runPipeline: (request: PipelineRequest, signal: AbortSignal) => Promise<PipelineResult>;
  /** Content-free accounting for the run record: budget, calls, counted units, attempts, gate decisions. */
  readonly record: () => unknown;
  readonly close: () => Promise<void>;
}

export interface TriggerPorts {
  readonly lsRemote?: (url: string) => string;
  readonly records?: AdmissionRecordsPort;
  /** Fetches exactly the pinned commit into `dir`; only called once every record is satisfied. */
  readonly materialize?: (target: { readonly url: string; readonly revision: string; readonly dir: string }) => Promise<string>;
  /** Model-assisted discovery. Each call is permitted only while the egress-consent record is still satisfied; there is no override. */
  readonly discovery?: Pick<DiscoveryPorts, 'map' | 'reduce'>;
  /** Durable sink for per-call discovery receipts; the run record also keeps them. */
  readonly discoveryReceipt?: (receipt: DiscoveryReceipt) => Promise<void>;
  /** Opens provider-backed generation for the run. Throws an error named `GenerationUnavailable` (with a `detail`) to refuse; the trigger then reads and sends nothing. When present it replaces `discovery`, `discoveryReceipt` and `runPipeline`. */
  readonly openGeneration?: (context: GenerationOpenContext) => Promise<GenerationSession>;
  /** The public-source policy act the screened read verifies; absent: this checkout's own record. */
  readonly policyAct?: PublicSourcePolicyActPort;
  /** Runs the six-stage pipeline; absent until a real generate port exists. */
  readonly runPipeline?: (request: PipelineRequest) => Promise<PipelineResult>;
  /** Turns a finished pipeline result into the dossier's files (path -> content); the polaris-dossier-v1 renderer is injected here. */
  readonly render?: (input: { readonly result: PipelineResult; readonly sources: readonly GenerationSource[] }) => { readonly files: ReadonlyMap<string, string> };
  readonly now?: () => number;
  readonly outDir?: string;
  readonly include?: readonly string[];
  readonly exclude?: readonly string[];
}
export type TriggerOutcome =
  | { readonly state: 'invalid-input'; readonly reason: string }
  | { readonly state: 'unresolved-revision'; readonly reason: string }
  | { readonly state: 'admission-missing'; readonly target: GithubTarget; readonly revision: string; readonly resolvedRef: string; readonly source: string;
      readonly requirements: readonly (AdmissionRequirement & { readonly answer: AdmissionAnswer })[]; readonly missing: number }
  | { readonly state: 'generation-unavailable' | 'generation-stopped' | 'generation-stopped-partial' | 'complete'; readonly target: GithubTarget; readonly revision: string; readonly runDir: string; readonly detail: string };

/** The narrative budget when no provider session supplies one: the agreed profile (2 h wall clock, units, calls derived from the repair cycles). */
const BUDGET: GenerationBudget = narrativeBudgetFor(DOSSIER_RUN_PROFILE);

/** Resolve, pin, check admission, and only then read. Stops at the first unmet gate. */
export async function runDossierTrigger(rawUrl: string, ports: TriggerPorts = {}): Promise<TriggerOutcome> {
  let target: GithubTarget;
  try { target = parseGithubUrl(rawUrl); } catch (error) { return { state: 'invalid-input', reason: error instanceof Error ? error.message : 'invalid' }; }
  let pinned: ReturnType<typeof pinRevision>;
  try { pinned = pinRevision((ports.lsRemote ?? gitLsRemote)(target.url), target.ref); }
  catch (error) { return { state: 'unresolved-revision', reason: error instanceof Error ? error.message : 'ls-remote-failed' }; }
  const records = ports.records ?? noAdmissionRecords;
  const idPattern = /^[A-Za-z0-9:_-]+$/u;
  // The port must answer an array of exactly one valid id; anything else (none, several, duplicates, a malformed element, a non-array, a throw) is an unmet gate.
  let answer: unknown;
  try { answer = await records.repositoryIdsFor(target.url); } catch { answer = undefined; }
  const sole = Array.isArray(answer) && answer.length === 1 && typeof answer[0] === 'string' && idPattern.test(answer[0]) ? answer[0] : undefined;
  if (sole === undefined) {
    const why = !Array.isArray(answer) ? `the record store gave a malformed answer for ${target.url}`
      : answer.length === 0 ? `no observation record names ${target.url} as its Upstream`
      : answer.length > 1 ? `${answer.length} observation records name ${target.url} as their Upstream; the repository identity is ambiguous`
      : `the record store gave a malformed repository id for ${target.url}`;
    const requirements = admissionRequirements(target, pinned.revision).map(requirement => ({ ...requirement, answer: { satisfied: false as const, why } }));
    return { state: 'admission-missing', target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, source: records.source, requirements, missing: requirements.length };
  }
  target = { ...target, repositoryId: sole };
  const requirements = admissionRequirements(target, pinned.revision);
  const checked = await Promise.all(requirements.map(async requirement => ({ ...requirement, answer: soundAnswer(await records.check(requirement)) })));
  const missing = checked.filter(entry => entry.answer.satisfied !== true).length;
  if (missing > 0) return { state: 'admission-missing', target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, source: records.source, requirements: checked, missing };

  const defaultOut = ports.outDir === undefined ? mkdtempSync(join(tmpdir(), 'syzygy-dossier-')) : undefined;
  const runDir = ports.outDir ?? join(defaultOut!, 'site');
  const checkoutDir = join(mkdtempSync(join(tmpdir(), 'syzygy-dossier-src-')), 'repo');
  let session: GenerationSession | undefined;
  const runStartedAt = (ports.now ?? Date.now)();
  try {
    // Refuse a misplaced run directory before the checkout, the reads or any provider call.
    // Limit: a directory created at runDir after this check (while the checkout and pipeline run) is caught by writeDossierRun, which throws run-directory-exists; the run is then lost, not recorded elsewhere.
    await checkDossierRunDestination(runDir);
    if (ports.materialize === undefined) return { state: 'generation-unavailable', target, revision: pinned.revision, runDir, detail: 'admission is satisfied but no checkout port is wired' };
    // A provider-backed run is opened (credential, gate, state directory) before anything is fetched: a run that cannot generate reads nothing.
    const egress = requirements.find(requirement => requirement.kind === 'egress-consent')!;
    if (ports.openGeneration !== undefined) {
      try { session = await ports.openGeneration({ target, revision: pinned.revision, runDir, egress, records }); }
      catch (error) {
        if (error instanceof Error && error.name === 'GenerationUnavailable') return { state: 'generation-unavailable', target, revision: pinned.revision, runDir, detail: (error as { detail?: string }).detail ?? error.message };
        throw error;
      }
    }
    const checkout = await ports.materialize({ url: target.url, revision: pinned.revision, dir: checkoutDir });
    const permissionIdentity = checked.map(entry => (entry.answer as { record: string }).record).join('+');
    const admission: CorpusAdmissionPort = { decide: async () => ({ allowed: true, permissionIdentity }) };
    const config: ReaderConfig = { repositoryId: target.repositoryId, revision: pinned.revision, include: ports.include ?? ['**'], exclude: ports.exclude ?? [],
      readerQuestions: DOSSIER_READER_QUESTIONS, requestedAssets: DOSSIER_REQUESTED_ASSETS, budget: BUDGET, oversize: 'split',
      ...(session === undefined ? {} : { routes: session.routes }) };
    // Every blob is screened against the public-source policy before any of it is carried further; a missing or unverifiable policy act refuses the read.
    let corpus: RepoCorpus;
    try { corpus = await readScreenedRepoCorpus(checkout, config, { admission, ...(ports.policyAct === undefined ? {} : { policyAct: ports.policyAct }) }); }
    catch (error) {
      if (!(error instanceof CorpusRefusal)) throw error;
      return { state: 'generation-unavailable', target, revision: pinned.revision, runDir, detail: `corpus-refused: ${error.message}` };
    }
    // A provider call is permitted only while the egress record that admitted this run still holds (and, with a session, its stage and budget limits).
    const permitted = async (call: DiscoveryCall): Promise<boolean> => soundAnswer(await records.check(egress)).satisfied === true && (session === undefined || await session.discoveryPermitted(call));
    const discoveryPorts = session?.discovery ?? ports.discovery, receiptSink = session?.discoveryReceipt ?? ports.discoveryReceipt;
    const wall = new AbortController();
    const wallTimer = session === undefined ? undefined : setTimeout(() => wall.abort(), session.wallClockMs);
    let discovery: Awaited<ReturnType<typeof discoverAndSelect>>;
    try {
      discovery = await discoverAndSelect(corpus.sources, config.readerQuestions.map(question => question.text), session?.discoveryBudget ?? DOSSIER_DISCOVERY_BUDGET,
        { permitted, ...(discoveryPorts?.map === undefined ? {} : { map: discoveryPorts.map }), ...(discoveryPorts?.reduce === undefined ? {} : { reduce: discoveryPorts.reduce }),
          ...(receiptSink === undefined ? {} : { receipt: receiptSink }) }, wall.signal);
    } catch (error) {
      if (!(error instanceof DiscoveryRefusal)) throw error;
      const refused = { profile: DOSSIER_PROFILE_ID, target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, permissionIdentity, corpusCount: corpus.count, discoveryRefusal: error.reason,
        ...(session === undefined ? {} : { generation: session.record() }) };
      const written = await writeDossierRun(runDir, new Map([['run-record.json', `${JSON.stringify(refused, null, 2)}\n`]]));
      return { state: 'generation-stopped', target, revision: pinned.revision, runDir: written, detail: `discovery-refused: ${error.reason}` };
    }
    finally { if (wallTimer !== undefined) clearTimeout(wallTimer); }
    const clarification: ClarificationRecord = await clarify({ sources: discovery.sources, mode: 'zero-interaction' });
    const record = { profile: DOSSIER_PROFILE_ID, target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, permissionIdentity, corpusCount: corpus.count,
      discovery: discovery.report as DiscoveryReport, discoveryReceipts: discovery.receipts, clarification };
    // Written last, so the accounting of the narrative is in it.
    const recordFile = (): readonly [string, string] => ['run-record.json', `${JSON.stringify({ ...record, ...(session === undefined ? {} : { generation: session.record() }) }, null, 2)}\n`];
    const runPipeline = session === undefined ? ports.runPipeline : (request: PipelineRequest) => session!.runPipeline(request, new AbortController().signal);
    if (runPipeline === undefined) {
      const written = await writeDossierRun(runDir, new Map([recordFile()]));
      return { state: 'generation-unavailable', target, revision: pinned.revision, runDir: written, detail: 'corpus, discovery and clarification recorded; no generate port is wired' };
    }
    const startedAt = (ports.now ?? Date.now)();
    // The wall clock covers the whole run: what discovery used is gone from the narrative's allowance.
    const budget = session === undefined ? config.budget : session.narrativeBudget(startedAt - runStartedAt);
    if (budget.maxElapsedMs <= 0) {
      const written = await writeDossierRun(runDir, new Map([recordFile()]));
      return { state: 'generation-stopped', target, revision: pinned.revision, runDir: written, detail: 'wall-clock-exhausted: discovery used the whole run allowance' };
    }
    const request = { ...buildPipelineRequest({ ...corpus, sources: discovery.sources }, { ...config, budget }, startedAt), promptProfile: 'dossier' as const };
    const result = await runPipeline(request);
    if (result.status === 'stopped') {
      // Render what the completed stages support; a renderer that cannot (no usable artifact) leaves the record alone.
      let partial: ReadonlyMap<string, string> | undefined;
      if (ports.render !== undefined) {
        try { partial = ports.render({ result, sources: discovery.sources }).files; }
        catch (error) { if (!(error instanceof Error) || error.name !== 'DossierRenderError') throw error; }
      }
      if (partial !== undefined && partial.has(recordFile()[0])) throw new Error('renderer-collides-with-run-record');
      const written = await writeDossierRun(runDir, new Map([...(partial ?? []), recordFile()]));
      return partial === undefined
        ? { state: 'generation-stopped', target, revision: pinned.revision, runDir: written, detail: result.reason }
        : { state: 'generation-stopped-partial', target, revision: pinned.revision, runDir: written, detail: `${result.reason}; ${partial.size} files rendered from ${result.artifacts.length} completed stage outputs` };
    }
    if (ports.render === undefined) {
      const written = await writeDossierRun(runDir, new Map([recordFile(), ['pipeline-result.json', `${JSON.stringify(result, null, 2)}\n`]]));
      return { state: 'generation-unavailable', target, revision: pinned.revision, runDir: written, detail: 'the pipeline finished but no renderer is wired; the result is recorded unrendered' };
    }
    const rendered = ports.render({ result, sources: discovery.sources });
    if (rendered.files.has(recordFile()[0])) throw new Error('renderer-collides-with-run-record');
    const written = await writeDossierRun(runDir, new Map([...rendered.files, recordFile()]));
    return { state: 'complete', target, revision: pinned.revision, runDir: written, detail: `${rendered.files.size} files` };
  } finally {
    rmSync(dirname(checkoutDir), { recursive: true, force: true });
    // A run that opened generation keeps its state directory (journals, receipts, consent audit) even when no run directory was written.
    if (session !== undefined) await session.close();
    else if (defaultOut !== undefined && !existsSync(runDir)) rmSync(defaultOut, { recursive: true, force: true });
  }
}

/** Fetches only the pinned commit's objects into an empty bare repository (no work tree, no template hooks). */
export async function gitMaterialize(target: { readonly url: string; readonly revision: string; readonly dir: string }, allowProtocol = 'https'): Promise<string> {
  const home = mkdtempSync(join(tmpdir(), 'syzygy-materialize-home-'));
  const env = minimalGitEnv(home, allowProtocol);
  try {
    mkdirSync(dirname(target.dir), { recursive: true });
    execFileSync('git', [...ISOLATED_GIT_FLAGS, 'init', '-q', '--bare', '--template=', target.dir], { env, cwd: home });
    execFileSync('git', [...ISOLATED_GIT_FLAGS, ...fileOverride(allowProtocol), '-C', target.dir, 'fetch', '-q', '--depth', '1', '--no-tags', '--', target.url, target.revision], { env, cwd: home, timeout: 300_000 });
  } finally { rmSync(home, { recursive: true, force: true }); }
  return target.dir;
}

export function formatOutcome(outcome: TriggerOutcome): string {
  switch (outcome.state) {
    case 'invalid-input': return `Not a supported URL (${outcome.reason}). Expected https://github.com/<owner>/<repo>[/tree/<ref>].\n`;
    case 'unresolved-revision': return `Could not pin a revision with git ls-remote (${outcome.reason}). Nothing was read.\n`;
    case 'admission-missing': return [`Target ${outcome.target.url} (${outcome.target.repositoryId})`, `Pinned ${outcome.resolvedRef} -> ${outcome.revision} (git ls-remote: metadata only)`,
      `Admission records consulted: ${outcome.source}`, ...outcome.requirements.map(r => r.answer.satisfied ? `  OK       ${r.kind}: ${r.answer.record}` : `  MISSING  ${r.kind}: ${r.needs}\n           (${r.answer.why})`),
      `STOPPED: ${outcome.missing} of ${outcome.requirements.length} admission record(s) missing. No repository body was read and no provider was called.`, ''].join('\n');
    default: return `${outcome.state.toUpperCase()}: ${outcome.target.url} @ ${outcome.revision}\n${outcome.detail}\nRun directory: ${outcome.runDir}\n`;
  }
}
