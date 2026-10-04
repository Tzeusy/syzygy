import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';

import { clarify, DOSSIER_DISCOVERY_BUDGET, DiscoveryRefusal, discoverAndSelect, DOSSIER_PROFILE_ID, DOSSIER_READER_QUESTIONS, DOSSIER_REQUESTED_ASSETS,
  type ClarificationRecord, type DiscoveryPorts, type DiscoveryReceipt, type DiscoveryReport, type GenerationBudget, type GenerationSource, type PipelineRequest, type PipelineResult } from '@syzygy/polaris-generation-core';

import { buildPipelineRequest, readRepoCorpus, type CorpusAdmissionPort, type ReaderConfig, type RepoCorpus } from './repo-corpus.js';
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
export interface ConsentedRevision { readonly label: string; readonly commitId: string }
/** Where the run's revision came from: a ref the URL named, or the one revision the observation consent admits. */
export type RevisionSource = { readonly from: 'url'; readonly ref?: string } | { readonly from: 'consent'; readonly label: string; readonly commitId: string };
export interface AdmissionRecordsPort {
  readonly source: string;
  /** The repository ids of every observation record whose `Upstream:` is exactly this canonical URL. The trigger never derives the id it admits under: it uses the one record's id, and refuses on zero or several. */
  readonly repositoryIdsFor: (url: string) => Promise<readonly string[]>;
  /** The revisions the in-force observation consent admits for this repository id: the consent's label (a tag or ref) and the commit object id it admits. Absent or empty means the consent names none, and a URL without a ref pins the default-branch tip as before. */
  readonly consentedRevisionsFor?: (repositoryId: string) => Promise<readonly ConsentedRevision[]>;
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

export interface TriggerPorts {
  readonly lsRemote?: (url: string) => string;
  readonly records?: AdmissionRecordsPort;
  /** Fetches exactly the pinned commit into `dir`; only called once every record is satisfied. */
  readonly materialize?: (target: { readonly url: string; readonly revision: string; readonly dir: string }) => Promise<string>;
  /** Model-assisted discovery. Each call is permitted only while the egress-consent record is still satisfied; there is no override. */
  readonly discovery?: Pick<DiscoveryPorts, 'map' | 'reduce'>;
  /** Durable sink for per-call discovery receipts; the run record also keeps them. */
  readonly discoveryReceipt?: (receipt: DiscoveryReceipt) => Promise<void>;
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

const BUDGET: GenerationBudget = { maxCalls: 7, maxInputBytes: 8_000_000, maxOutputBytes: 1_000_000, maxUsageUnits: 1000, maxElapsedMs: 3_600_000, maxRepairCycles: 1, accountingPolicy: 'dossier-units-v1' };

const CONSENT_LABEL = /^[A-Za-z0-9._\/-]{1,200}$/u;

/** A dense copy of the consented revisions as primitive strings, or undefined when the answer is not an array of well-formed entries (holes, non-objects, a non-string label, a commit id that is not 40 or 64 hex digits, a throwing getter). */
function snapshotConsented(answer: unknown): readonly ConsentedRevision[] | undefined {
  if (!Array.isArray(answer)) return undefined;
  const out: ConsentedRevision[] = [];
  try {
    const length = answer.length;
    for (let index = 0; index < length; index++) {
      if (!(index in answer)) return undefined;
      const entry: unknown = answer[index];
      if (entry === null || typeof entry !== 'object') return undefined;
      const { label, commitId } = entry as { label?: unknown; commitId?: unknown };
      if (typeof label !== 'string' || typeof commitId !== 'string' || !/^[0-9a-f]{40}$|^[0-9a-f]{64}$/u.test(commitId)) return undefined;
      out.push({ label, commitId });
    }
  } catch { return undefined; }
  return out;
}

/** Resolve, pin, check admission, and only then read. Stops at the first unmet gate. */
export async function runDossierTrigger(rawUrl: string, ports: TriggerPorts = {}): Promise<TriggerOutcome> {
  let target: GithubTarget;
  try { target = parseGithubUrl(rawUrl); } catch (error) { return { state: 'invalid-input', reason: error instanceof Error ? error.message : 'invalid' }; }
  let pinned: ReturnType<typeof pinRevision>, lsOutput: string;
  try { lsOutput = (ports.lsRemote ?? gitLsRemote)(target.url); pinned = pinRevision(lsOutput, target.ref); }
  catch (error) { return { state: 'unresolved-revision', reason: error instanceof Error ? error.message : 'ls-remote-failed' }; }
  let revisionSource: RevisionSource = target.ref === undefined ? { from: 'url' } : { from: 'url', ref: target.ref };
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
  const unmet = (why: string): TriggerOutcome => {
    const unmetRequirements = admissionRequirements(target, pinned.revision).map(requirement => ({ ...requirement, answer: { satisfied: false as const, why } }));
    return { state: 'admission-missing', target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, source: records.source, requirements: unmetRequirements, missing: unmetRequirements.length };
  };
  // The record store is untrusted: its property, its call, its array and each entry are read once, inside this block, and only primitive snapshots are used afterwards.
  let consentFn: AdmissionRecordsPort['consentedRevisionsFor'], consented: unknown, consultable = true;
  if (target.ref === undefined) {
    try { consentFn = records.consentedRevisionsFor; if (consentFn !== undefined) consented = await consentFn.call(records, sole); } catch { consultable = false; }
  }
  if (target.ref === undefined && (consentFn !== undefined || !consultable)) {
    // A bare URL runs at the revision the observation consent admits, when it admits exactly one; the tip of the default branch has no consent that names it.
    const revisions = consultable ? snapshotConsented(consented) : undefined;
    if (revisions === undefined) return unmet(`the record store gave a malformed list of consented revisions for ${sole}`);
    if (revisions.length > 1) {
      return unmet(`the observation consent admits ${revisions.length} revisions of ${target.url} (${revisions.map(entry => entry.label).join(', ')}); the URL names none, so none is chosen. Add /tree/<ref> to the URL to pick one`)
    }
    if (revisions.length === 1) {
      const only = revisions[0]!;
      if (!CONSENT_LABEL.test(only.label) || only.label.split('/').some(part => part === '..')) return unmet(`the consented revision label ${JSON.stringify(only.label)} is not a usable tag or ref name; add /tree/<ref> to the URL`)
      // The consent names this ref, so a ref the remote no longer lists is an unmet admission, not an unresolvable URL.
      try { pinned = pinRevision(lsOutput, only.label); }
      catch (error) { return unmet(`the consented revision ${only.label} cannot be resolved with git ls-remote (${error instanceof Error ? error.message : 'ls-remote-failed'}); nothing is read`); }
      if (pinned.revision !== only.commitId) {
        if (lsOutput.split('\n').some(line => line === `${only.commitId}\trefs/tags/${only.label}`)) {
          return unmet(`the consent records the tag object of ${only.label} (${only.commitId}), not the commit it peels to (${pinned.revision}); record the commit id. Nothing is read`);
        }
        return unmet(`the consented revision ${only.label} now resolves to ${pinned.revision}, but the consent admits ${only.commitId}; the ref has moved, so nothing is read`);
      }
      revisionSource = { from: 'consent', label: only.label, commitId: only.commitId };
    }
  }
  const requirements = admissionRequirements(target, pinned.revision);
  const checked = await Promise.all(requirements.map(async requirement => ({ ...requirement, answer: soundAnswer(await records.check(requirement)) })));
  const missing = checked.filter(entry => entry.answer.satisfied !== true).length;
  if (missing > 0) return { state: 'admission-missing', target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, source: records.source, requirements: checked, missing };

  const defaultOut = ports.outDir === undefined ? mkdtempSync(join(tmpdir(), 'syzygy-dossier-')) : undefined;
  const runDir = ports.outDir ?? join(defaultOut!, 'site');
  const checkoutDir = join(mkdtempSync(join(tmpdir(), 'syzygy-dossier-src-')), 'repo');
  try {
    // Refuse a misplaced run directory before the checkout, the reads or any provider call.
    // Limit: a directory created at runDir after this check (while the checkout and pipeline run) is caught by writeDossierRun, which throws run-directory-exists; the run is then lost, not recorded elsewhere.
    await checkDossierRunDestination(runDir);
    if (ports.materialize === undefined) return { state: 'generation-unavailable', target, revision: pinned.revision, runDir, detail: 'admission is satisfied but no checkout port is wired' };
    const checkout = await ports.materialize({ url: target.url, revision: pinned.revision, dir: checkoutDir });
    const permissionIdentity = checked.map(entry => (entry.answer as { record: string }).record).join('+');
    const admission: CorpusAdmissionPort = { decide: async () => ({ allowed: true, permissionIdentity }) };
    const config: ReaderConfig = { repositoryId: target.repositoryId, revision: pinned.revision, include: ports.include ?? ['**'], exclude: ports.exclude ?? [],
      readerQuestions: DOSSIER_READER_QUESTIONS, requestedAssets: DOSSIER_REQUESTED_ASSETS, budget: BUDGET, oversize: 'split' };
    const corpus: RepoCorpus = await readRepoCorpus(checkout, config, { admission });
    // A provider call is permitted only while the egress record that admitted this run still holds.
    const egress = requirements.find(requirement => requirement.kind === 'egress-consent')!;
    const permitted = async (): Promise<boolean> => soundAnswer(await records.check(egress)).satisfied === true;
    let discovery: Awaited<ReturnType<typeof discoverAndSelect>>;
    try {
      discovery = await discoverAndSelect(corpus.sources, config.readerQuestions.map(question => question.text), DOSSIER_DISCOVERY_BUDGET,
        { permitted, ...(ports.discovery?.map === undefined ? {} : { map: ports.discovery.map }), ...(ports.discovery?.reduce === undefined ? {} : { reduce: ports.discovery.reduce }),
          ...(ports.discoveryReceipt === undefined ? {} : { receipt: ports.discoveryReceipt }) });
    } catch (error) {
      if (!(error instanceof DiscoveryRefusal)) throw error;
      const refused = { profile: DOSSIER_PROFILE_ID, target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, revisionSource, permissionIdentity, corpusCount: corpus.count, discoveryRefusal: error.reason };
      const written = await writeDossierRun(runDir, new Map([['run-record.json', `${JSON.stringify(refused, null, 2)}\n`]]));
      return { state: 'generation-stopped', target, revision: pinned.revision, runDir: written, detail: `discovery-refused: ${error.reason}` };
    }
    const clarification: ClarificationRecord = await clarify({ sources: discovery.sources, mode: 'zero-interaction' });
    const record = { profile: DOSSIER_PROFILE_ID, target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, revisionSource, permissionIdentity, corpusCount: corpus.count,
      discovery: discovery.report as DiscoveryReport, discoveryReceipts: discovery.receipts, clarification };
    const recordFile = ['run-record.json', `${JSON.stringify(record, null, 2)}\n`] as const;
    if (ports.runPipeline === undefined) {
      const written = await writeDossierRun(runDir, new Map([recordFile]));
      return { state: 'generation-unavailable', target, revision: pinned.revision, runDir: written, detail: 'corpus, discovery and clarification recorded; no generate port is wired' };
    }
    const request = { ...buildPipelineRequest({ ...corpus, sources: discovery.sources }, config, (ports.now ?? Date.now)()), promptProfile: 'dossier' as const };
    const result = await ports.runPipeline(request);
    if (result.status === 'stopped') {
      // Render what the completed stages support; a renderer that cannot (no usable artifact) leaves the record alone.
      let partial: ReadonlyMap<string, string> | undefined;
      if (ports.render !== undefined) {
        try { partial = ports.render({ result, sources: discovery.sources }).files; }
        catch (error) { if (!(error instanceof Error) || error.name !== 'DossierRenderError') throw error; }
      }
      if (partial !== undefined && partial.has(recordFile[0])) throw new Error('renderer-collides-with-run-record');
      const written = await writeDossierRun(runDir, new Map([...(partial ?? []), recordFile]));
      return partial === undefined
        ? { state: 'generation-stopped', target, revision: pinned.revision, runDir: written, detail: result.reason }
        : { state: 'generation-stopped-partial', target, revision: pinned.revision, runDir: written, detail: `${result.reason}; ${partial.size} files rendered from ${result.artifacts.length} completed stage outputs` };
    }
    if (ports.render === undefined) {
      const written = await writeDossierRun(runDir, new Map([recordFile, ['pipeline-result.json', `${JSON.stringify(result, null, 2)}\n`]]));
      return { state: 'generation-unavailable', target, revision: pinned.revision, runDir: written, detail: 'the pipeline finished but no renderer is wired; the result is recorded unrendered' };
    }
    const rendered = ports.render({ result, sources: discovery.sources });
    if (rendered.files.has(recordFile[0])) throw new Error('renderer-collides-with-run-record');
    const written = await writeDossierRun(runDir, new Map([...rendered.files, recordFile]));
    return { state: 'complete', target, revision: pinned.revision, runDir: written, detail: `${rendered.files.size} files` };
  } finally {
    rmSync(dirname(checkoutDir), { recursive: true, force: true });
    if (defaultOut !== undefined && !existsSync(runDir)) rmSync(defaultOut, { recursive: true, force: true });
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
