import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';

import { DOSSIER_READER_QUESTIONS, DOSSIER_REQUESTED_ASSETS, generationSourcesForBody, gitBlobObjectId, validateGenerationSources, validateRequestedAssets,
  type GenerationBudget, type GenerationSource, type GenerationStage, type PipelineRequest, type RequestedAsset } from '@syzygy/polaris-generation-core';

import { readGitBlobsBatch, type ReadGitBlobs } from '../git-blob-batch.js';

const sha256 = (value: string): string => createHash('sha256').update(value).digest('hex');
const git = (repoRoot: string, args: readonly string[]): Buffer => execFileSync('git', ['--no-optional-locks', '-C', repoRoot, ...args], { maxBuffer: 512_000_000 });
const BLOB_BATCH = 200;
const STAGES: readonly GenerationStage[] = ['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair'];

/** The trusted decision to look at one repository revision. The reader asks
 * before it touches the repository in any way, and only `allowed: true`
 * proceeds. A later lane backs this with real consent records. */
export interface CorpusAdmissionRequest { readonly repositoryId: string; readonly revision: string; readonly include: readonly string[]; readonly exclude: readonly string[] }
export type CorpusAdmissionDecision =
  | { readonly allowed: true; readonly permissionIdentity: string }
  | { readonly allowed: false; readonly reason: string };
export interface CorpusAdmissionPort { readonly decide: (request: CorpusAdmissionRequest) => Promise<CorpusAdmissionDecision> }

/** The default: no admission record, so no read. */
export const refusingAdmission: CorpusAdmissionPort = {
  decide: async () => ({ allowed: false, reason: 'no-admission-port: no observation consent record is wired' }),
};

export class CorpusRefusal extends Error {
  constructor(readonly reason: string) { super(`Corpus read refused: ${reason}`); this.name = 'CorpusRefusal'; }
}

export interface ReaderConfig {
  readonly repositoryId: string;
  readonly revision: string;
  readonly include: readonly string[];
  readonly exclude: readonly string[];
  readonly readerQuestions: readonly string[];
  readonly requestedAssets: readonly RequestedAsset[];
  readonly budget: GenerationBudget;
  readonly oversize: 'split' | 'exclude';
  readonly routes?: Readonly<Record<GenerationStage, string>>;
}

const CONFIG_KEYS = new Set(['repositoryId', 'revision', 'include', 'exclude', 'readerQuestions', 'requestedAssets', 'budget', 'oversize', 'routes', 'profile']);
const BUDGET_KEYS = ['maxCalls', 'maxInputBytes', 'maxOutputBytes', 'maxUsageUnits', 'maxElapsedMs', 'maxRepairCycles', 'accountingPolicy'] as const;
const strings = (value: unknown, what: string): string[] => {
  if (!Array.isArray(value) || value.some(item => typeof item !== 'string' || item.length === 0)) throw new Error(`config-invalid: ${what}`);
  return value as string[];
};

/** `profile: "dossier"` supplies the dossier reader questions and assets unless the config sets its own.
 * Strict parse: unknown keys, wrong types and an unset revision are refused. */
export function parseReaderConfig(text: string, overrides: Partial<Pick<ReaderConfig, 'repositoryId' | 'revision'>> & { include?: readonly string[]; exclude?: readonly string[] } = {}): ReaderConfig {
  const raw = JSON.parse(text) as Record<string, unknown>;
  if (raw === null || typeof raw !== 'object' || Array.isArray(raw) || Object.keys(raw).some(key => !CONFIG_KEYS.has(key))) throw new Error('config-invalid: keys');
  const budget = raw.budget as Record<string, unknown>;
  if (budget === null || typeof budget !== 'object' || Object.keys(budget).length !== BUDGET_KEYS.length
    || BUDGET_KEYS.some(key => key === 'accountingPolicy' ? typeof budget[key] !== 'string' : !Number.isSafeInteger(budget[key]) || (budget[key] as number) < 0)) throw new Error('config-invalid: budget');
  if (raw.profile !== undefined && raw.profile !== 'dossier') throw new Error('config-invalid: profile');
  const dossier = raw.profile === 'dossier';
  const oversize = raw.oversize ?? 'split';
  if (oversize !== 'split' && oversize !== 'exclude') throw new Error('config-invalid: oversize');
  const routes = raw.routes as Record<string, unknown> | undefined;
  if (routes !== undefined && (typeof routes !== 'object' || routes === null || STAGES.some(stage => typeof routes[stage] !== 'string'))) throw new Error('config-invalid: routes');
  const config: ReaderConfig = {
    repositoryId: overrides.repositoryId ?? String(raw.repositoryId ?? ''),
    revision: overrides.revision ?? String(raw.revision ?? ''),
    include: overrides.include?.length ? overrides.include : strings(raw.include ?? ['**'], 'include'),
    exclude: overrides.exclude?.length ? overrides.exclude : strings(raw.exclude ?? [], 'exclude'),
    readerQuestions: dossier && raw.readerQuestions === undefined ? DOSSIER_READER_QUESTIONS : strings(raw.readerQuestions, 'readerQuestions'),
    requestedAssets: dossier && raw.requestedAssets === undefined ? DOSSIER_REQUESTED_ASSETS : raw.requestedAssets as RequestedAsset[], budget: budget as unknown as GenerationBudget,
    oversize, ...(routes === undefined ? {} : { routes: routes as unknown as Record<GenerationStage, string> }),
  };
  assertIdentity(config.repositoryId, config.revision);
  validateRequestedAssets(config.requestedAssets);
  return config;
}

function assertIdentity(repositoryId: string, revision: string): void {
  if (!/^[A-Za-z0-9:_-]+$/u.test(repositoryId)) throw new Error('invalid-repository-id');
  if (!/^(?:[0-9a-f]{40}|[0-9a-f]{64})$/u.test(revision)) throw new Error('invalid-pinned-commit');
}

/** `**` crosses directories, `**` + `/` may match none, `*` and `?` stay in one segment. */
export function globToRegExp(glob: string): RegExp {
  let out = '';
  for (let i = 0; i < glob.length; i++) {
    const c = glob[i]!;
    if (c === '*' && glob[i + 1] === '*') {
      if (glob[i + 2] === '/') { out += '(?:.*/)?'; i += 2; } else { out += '.*'; i += 1; }
    } else if (c === '*') out += '[^/]*';
    else if (c === '?') out += '[^/]';
    else out += c.replace(/[\\^$.|+()[\]{}]/gu, '\\$&');
  }
  return new RegExp(`^${out}$`, 'u');
}

export interface RepoCorpusCount {
  readonly listed: number;
  readonly notBlob: number;
  readonly outsideInclude: number;
  readonly excludedByGlob: number;
  readonly selected: number;
  readonly binaryOrNonUtf8: number;
  readonly oversizeFiles: number;
  readonly oversizeExcluded: number;
}
export interface RepoCorpus {
  readonly repositoryId: string;
  readonly revision: string;
  readonly permissionIdentity: string;
  readonly sources: readonly GenerationSource[];
  readonly count: RepoCorpusCount;
  readonly rawBytes: number;
  readonly identityDigest: string;
}

export interface RepoCorpusPorts { readonly admission?: CorpusAdmissionPort; readonly readBlobs?: ReadGitBlobs }

/** Reads exactly the named blobs of one pinned commit, after the admission
 * port says yes. Never the working tree, never another revision, never a
 * provider. Every tree entry is accounted for in `count`. */
export async function readRepoCorpus(repoRoot: string, config: Pick<ReaderConfig, 'repositoryId' | 'revision' | 'include' | 'exclude' | 'oversize'>, ports: RepoCorpusPorts = {}): Promise<RepoCorpus> {
  assertIdentity(config.repositoryId, config.revision);
  const decision = await (ports.admission ?? refusingAdmission).decide({ repositoryId: config.repositoryId, revision: config.revision, include: config.include, exclude: config.exclude });
  if (decision.allowed !== true) throw new CorpusRefusal(decision.allowed === false ? decision.reason : 'admission-undecided');
  const readBlobs = ports.readBlobs ?? readGitBlobsBatch;
  if (git(repoRoot, ['cat-file', '-t', config.revision]).toString('utf8').trim() !== 'commit') throw new Error('invalid-pinned-commit');
  const include = config.include.map(globToRegExp), exclude = config.exclude.map(globToRegExp);
  const records = git(repoRoot, ['ls-tree', '-r', '-z', '--full-tree', config.revision]).toString('utf8').split('\0').filter(Boolean).map(row => {
    const match = /^(\d{6}) (blob|tree|commit) ([0-9a-f]{40}|[0-9a-f]{64})\t(.+)$/u.exec(row);
    if (!match) throw new Error('invalid-git-tree-record');
    return { mode: match[1]!, type: match[2]!, objectId: match[3]!, path: match[4]! };
  });
  let notBlob = 0, outsideInclude = 0, excludedByGlob = 0, binaryOrNonUtf8 = 0, oversizeFiles = 0, oversizeExcluded = 0, rawBytes = 0;
  const chosen = records.filter(record => {
    if (record.type !== 'blob' || record.mode === '120000') { notBlob++; return false; }
    if (!include.some(re => re.test(record.path))) { outsideInclude++; return false; }
    if (exclude.some(re => re.test(record.path))) { excludedByGlob++; return false; }
    return true;
  }).sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : 0);
  const evaluationId = `corpus:${config.repositoryId}@${config.revision}`;
  const sources: GenerationSource[] = [];
  for (let at = 0; at < chosen.length; at += BLOB_BATCH) {
    const batch = chosen.slice(at, at + BLOB_BATCH);
    const blobs = readBlobs(repoRoot, batch.map(record => record.objectId));
    for (const record of batch) {
      const bytes = blobs.get(record.objectId);
      if (!(bytes instanceof Uint8Array)) throw bytes ?? new Error('corpus-blob-unread');
      rawBytes += bytes.length;
      const sourceId = `s-${sha256(record.path).slice(0, 24)}`;
      const base = { repositoryId: config.repositoryId, revision: config.revision, path: record.path, objectId: record.objectId, evaluationId, sourceId };
      let body: string | undefined;
      try { body = bytes.includes(0) ? undefined : new TextDecoder('utf-8', { fatal: true }).decode(bytes); } catch { body = undefined; }
      if (body === undefined) {
        binaryOrNonUtf8++;
        sources.push({ ...base, classificationBasis: 'body', exclusion: { excluded: true, reason: 'binary-or-non-utf8' }, spans: [] });
        continue;
      }
      if (gitBlobObjectId(body, record.objectId.length === 40 ? 'sha1' : 'sha256') !== record.objectId) throw new Error('corpus-object-mismatch');
      const made = generationSourcesForBody({ ...base, body, oversize: config.oversize });
      if ([...body].length > 100_000) { oversizeFiles++; if (config.oversize === 'exclude') oversizeExcluded++; }
      sources.push(...made);
    }
  }
  validateGenerationSources(sources);
  return { repositoryId: config.repositoryId, revision: config.revision, permissionIdentity: decision.permissionIdentity, sources,
    count: { listed: records.length, notBlob, outsideInclude, excludedByGlob, selected: chosen.length, binaryOrNonUtf8, oversizeFiles, oversizeExcluded },
    rawBytes, identityDigest: sha256(sources.map(source => `${source.path}\0${source.objectId}\0${source.sourceId}`).join('\n')) };
}

/** The request the pipeline would run; startedAt is the caller's clock. */
export function buildPipelineRequest(corpus: RepoCorpus, config: ReaderConfig, startedAt: number): PipelineRequest {
  const routes = config.routes ?? Object.fromEntries(STAGES.map(stage => [stage, `provider-${stage}`])) as Record<GenerationStage, string>;
  return { requestId: `repo-${corpus.identityDigest}`, projectId: corpus.repositoryId, snapshotId: corpus.identityDigest, routes, startedAt,
    budget: config.budget, sources: corpus.sources, readerQuestions: config.readerQuestions, requestedAssets: config.requestedAssets };
}
