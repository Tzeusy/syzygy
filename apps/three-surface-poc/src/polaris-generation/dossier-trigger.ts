import { execFileSync } from 'node:child_process';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import { clarify, DEFAULT_DISCOVERY_BUDGET, discoverAndSelect, DOSSIER_PROFILE_ID, DOSSIER_READER_QUESTIONS, DOSSIER_REQUESTED_ASSETS,
  type ClarificationRecord, type DiscoveryPorts, type DiscoveryReceipt, type DiscoveryReport, type GenerationBudget, type PipelineRequest, type ProviderDraft } from '@syzygy/polaris-generation-core';

import { buildPipelineRequest, readRepoCorpus, type CorpusAdmissionPort, type ReaderConfig, type RepoCorpus } from './repo-corpus.js';
import { renderDossierSite, writeDossierSite } from './dossier-site.js';

export interface GithubTarget { readonly owner: string; readonly repo: string; readonly ref?: string; readonly url: string; readonly repositoryId: string }

/** Public https://github.com/<owner>/<repo> only, optionally `/tree/<ref>`. No credentials, no other host. */
export function parseGithubUrl(input: string): GithubTarget {
  const match = /^https:\/\/github\.com\/([A-Za-z0-9][A-Za-z0-9-]{0,38})\/([A-Za-z0-9._-]{1,100}?)(?:\.git)?(?:\/tree\/([A-Za-z0-9._\/-]{1,200}))?\/?$/u.exec(input);
  if (match === null || match[2] === '.' || match[2] === '..' || (match[3] ?? '').split('/').some(part => part === '..')) throw new Error('invalid-github-url');
  const [, owner, repo, ref] = match as unknown as [string, string, string, string | undefined];
  return { owner, repo, ...(ref === undefined ? {} : { ref }), url: `https://github.com/${owner}/${repo}`, repositoryId: `github:${owner}:${repo.replace(/\./gu, '_')}` };
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

/** Metadata only: ref names and commit ids, never a repository body. */
export function gitLsRemote(url: string): string {
  return execFileSync('git', ['ls-remote', '--', url], { encoding: 'utf8', timeout: 30_000, maxBuffer: 16_000_000,
    env: { ...process.env, GIT_TERMINAL_PROMPT: '0', GIT_ALLOW_PROTOCOL: 'https' } });
}

export type AdmissionKind = 'observation-consent' | 'public-source-policy' | 'egress-consent';
export interface AdmissionRequirement { readonly kind: AdmissionKind; readonly repositoryId: string; readonly revision: string; readonly url: string; readonly needs: string }
export type AdmissionAnswer = { readonly satisfied: true; readonly record: string } | { readonly satisfied: false; readonly why: string };
export interface AdmissionRecordsPort {
  readonly source: string;
  readonly check: (requirement: AdmissionRequirement) => Promise<AdmissionAnswer>;
}
/** With no store wired, no record exists, and the report says so. */
export const noAdmissionRecords: AdmissionRecordsPort = {
  source: 'no record store is wired into this command',
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

export interface TriggerPorts {
  readonly lsRemote?: (url: string) => string;
  readonly records?: AdmissionRecordsPort;
  /** Fetches exactly the pinned commit into `dir`; only called once every record is satisfied. */
  readonly materialize?: (target: { readonly url: string; readonly revision: string; readonly dir: string }) => Promise<string>;
  readonly discovery?: Omit<DiscoveryPorts, 'permitted' | 'receipt'>;
  /** Durable sink for per-call discovery receipts; the run record also keeps them. */
  readonly discoveryReceipt?: (receipt: DiscoveryReceipt) => Promise<void>;
  /** Runs the six-stage pipeline; absent until a real generate port exists. */
  readonly runPipeline?: (request: PipelineRequest) => Promise<{ readonly status: 'draft'; readonly draft: ProviderDraft } | { readonly status: 'stopped'; readonly reason: string }>;
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
  | { readonly state: 'generation-unavailable' | 'generation-stopped' | 'complete'; readonly target: GithubTarget; readonly revision: string; readonly runDir: string; readonly detail: string };

const BUDGET: GenerationBudget = { maxCalls: 7, maxInputBytes: 8_000_000, maxOutputBytes: 1_000_000, maxUsageUnits: 1000, maxElapsedMs: 3_600_000, maxRepairCycles: 1, accountingPolicy: 'dossier-units-v1' };

/** Resolve, pin, check admission, and only then read. Stops at the first unmet gate. */
export async function runDossierTrigger(rawUrl: string, ports: TriggerPorts = {}): Promise<TriggerOutcome> {
  let target: GithubTarget;
  try { target = parseGithubUrl(rawUrl); } catch (error) { return { state: 'invalid-input', reason: error instanceof Error ? error.message : 'invalid' }; }
  let pinned: ReturnType<typeof pinRevision>;
  try { pinned = pinRevision((ports.lsRemote ?? gitLsRemote)(target.url), target.ref); }
  catch (error) { return { state: 'unresolved-revision', reason: error instanceof Error ? error.message : 'ls-remote-failed' }; }
  const records = ports.records ?? noAdmissionRecords;
  const checked = await Promise.all(admissionRequirements(target, pinned.revision).map(async requirement => ({ ...requirement, answer: await records.check(requirement) })));
  const missing = checked.filter(entry => !entry.answer.satisfied).length;
  if (missing > 0) return { state: 'admission-missing', target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, source: records.source, requirements: checked, missing };

  const runDir = ports.outDir ?? join(mkdtempSync(join(tmpdir(), 'syzygy-dossier-')), 'site');
  if (ports.materialize === undefined) return { state: 'generation-unavailable', target, revision: pinned.revision, runDir, detail: 'admission is satisfied but no checkout port is wired' };
  const checkout = await ports.materialize({ url: target.url, revision: pinned.revision, dir: mkdtempSync(join(tmpdir(), 'syzygy-dossier-src-')) });
  const permissionIdentity = checked.map(entry => (entry.answer as { record: string }).record).join('+');
  const admission: CorpusAdmissionPort = { decide: async () => ({ allowed: true, permissionIdentity }) };
  const config: ReaderConfig = { repositoryId: target.repositoryId, revision: pinned.revision, include: ports.include ?? ['**'], exclude: ports.exclude ?? [],
    readerQuestions: DOSSIER_READER_QUESTIONS, requestedAssets: DOSSIER_REQUESTED_ASSETS, budget: BUDGET, oversize: 'split' };
  const corpus: RepoCorpus = await readRepoCorpus(checkout, config, { admission });
  const discovery = await discoverAndSelect(corpus.sources, config.readerQuestions, DEFAULT_DISCOVERY_BUDGET, { permitted: async () => true, receipt: ports.discoveryReceipt ?? (async () => undefined), ...ports.discovery });
  const clarification: ClarificationRecord = await clarify({ sources: discovery.sources, mode: 'zero-interaction' });
  const record = { profile: DOSSIER_PROFILE_ID, target, revision: pinned.revision, resolvedRef: pinned.resolvedRef, permissionIdentity, corpusCount: corpus.count,
    discovery: discovery.report as DiscoveryReport, discoveryReceipts: discovery.receipts, clarification };
  const recordPage = { path: 'run-record.json', kind: 'run-record' as const, content: `${JSON.stringify(record, null, 2)}\n` };
  if (ports.runPipeline === undefined) {
    writeDossierSite(runDir, { pages: [recordPage] });
    return { state: 'generation-unavailable', target, revision: pinned.revision, runDir, detail: 'corpus, discovery and clarification recorded; no generate port is wired' };
  }
  const request = buildPipelineRequest({ ...corpus, sources: discovery.sources }, config, (ports.now ?? Date.now)());
  const result = await ports.runPipeline(request);
  if (result.status === 'stopped') {
    writeDossierSite(runDir, { pages: [recordPage] });
    return { state: 'generation-stopped', target, revision: pinned.revision, runDir, detail: result.reason };
  }
  const site = renderDossierSite(result.draft, discovery.sources);
  writeDossierSite(runDir, { pages: [...site.pages, recordPage] });
  return { state: 'complete', target, revision: pinned.revision, runDir, detail: `${site.pages.length} pages, ${site.sizeReport.totalBytes} bytes` };
}

/** Fetches only the pinned commit's objects into an empty repository. */
export async function gitMaterialize(target: { readonly url: string; readonly revision: string; readonly dir: string }, allowProtocol = 'https'): Promise<string> {
  const env = { ...process.env, GIT_TERMINAL_PROMPT: '0', GIT_ALLOW_PROTOCOL: allowProtocol };
  execFileSync('git', ['init', '-q', target.dir], { env });
  execFileSync('git', ['-C', target.dir, 'fetch', '-q', '--depth', '1', '--no-tags', '--', target.url, target.revision], { env, timeout: 300_000 });
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
