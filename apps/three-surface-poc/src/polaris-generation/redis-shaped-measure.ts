import { createHash } from 'node:crypto';

import { DEFAULT_DISCOVERY_BUDGET, DOSSIER_READER_QUESTIONS, discoverAndSelect, quotableGenerationSources, type DiscoveryBudget, type DiscoveryResult } from '@syzygy/polaris-generation-core';

import { CORE_FILES, buildRedisShapedFixture, redisShapedFiles, type RedisShapedFixture } from './redis-shaped-fixture.js';
import { readRepoCorpus, type RepoCorpus } from './repo-corpus.js';

const VENDORED = /^(?:deps|vendor|third_party)\//u;

export interface RedisShapedMeasurement {
  /** `sha256` is over every path and body in sorted order (path, NUL, body, NUL), so a changed fixture is a changed subject. */
  readonly fixture: { readonly files: number; readonly oversizeFiles: readonly string[]; readonly sha256: string };
  readonly corpus: { readonly sourceRows: number; readonly quotableRows: number; readonly oversizeFiles: number; readonly oversizePieces: Readonly<Record<string, number>> };
  readonly selection: {
    readonly selectedBlobs: number;
    readonly selectedSources: number;
    readonly rankingBasis: string;
    readonly byTopDirectory: Readonly<Record<string, number>>;
    readonly vendored: number;
    readonly srcFiles: number;
  };
  readonly coreMechanisms: Readonly<Record<string, { readonly selected: readonly string[]; readonly deferred: readonly string[] }>>;
  readonly accounting: {
    readonly population: number;
    readonly candidateBlobs: number;
    readonly deferredBlobs: number;
    readonly deferredRows: number;
    readonly deferredVendored: number;
    readonly closes: boolean;
  };
}

/** Builds the synthetic fixture in `dir`, reads it with the dossier profile's reader questions and a pinned commit, and runs heuristic discovery under the default budget. */
export async function measureRedisShapedDiscovery(dir: string, budget: DiscoveryBudget = DEFAULT_DISCOVERY_BUDGET): Promise<{ measurement: RedisShapedMeasurement; fixture: RedisShapedFixture; corpus: RepoCorpus; result: DiscoveryResult }> {
  const fixture = buildRedisShapedFixture(dir);
  const corpus = await readRepoCorpus(dir, { repositoryId: 'repository:synthetic-kv-server', revision: fixture.commit, include: ['**'], exclude: [], oversize: 'split' },
    { admission: { decide: async () => ({ allowed: true, permissionIdentity: 'synthetic-fixture-consent-v1' }) } });
  const result = await discoverAndSelect(corpus.sources, DOSSIER_READER_QUESTIONS.map(question => question.text), budget, { permitted: async () => true });
  const quotableIds = new Set(quotableGenerationSources(result.sources).map(source => source.sourceId));
  const selectedPaths = new Set(result.sources.filter(source => quotableIds.has(source.sourceId)).map(source => source.path));
  const deferredPaths = new Set(result.report.deferred.map(entry => entry.path));
  const byTopDirectory: Record<string, number> = {};
  for (const path of selectedPaths) { const top = path.includes('/') ? path.split('/')[0]! : '(root)'; byTopDirectory[top] = (byTopDirectory[top] ?? 0) + 1; }
  const oversizePieces: Record<string, number> = {};
  for (const path of fixture.oversize) oversizePieces[path] = corpus.sources.filter(source => source.path === path).length;
  const deferredRows = result.sources.filter(source => source.exclusion.excluded && source.exclusion.reason === 'deferred-by-budget').length;
  return { fixture, corpus, result, measurement: {
    fixture: { files: fixture.files.size, oversizeFiles: fixture.oversize,
      sha256: [...redisShapedFiles()].sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)).reduce((hash, [path, text]) => hash.update(`${path}\0${text}\0`), createHash('sha256')).digest('hex') },
    corpus: { sourceRows: corpus.sources.length, quotableRows: quotableGenerationSources(corpus.sources).length, oversizeFiles: corpus.count.oversizeFiles, oversizePieces },
    selection: { selectedBlobs: result.report.selected.blobs, selectedSources: result.report.selected.sources, rankingBasis: result.report.rankingBasis, byTopDirectory,
      vendored: [...selectedPaths].filter(path => VENDORED.test(path)).length, srcFiles: [...selectedPaths].filter(path => path.startsWith('src/')).length },
    coreMechanisms: Object.fromEntries(Object.entries(CORE_FILES).map(([role, paths]) => [role, { selected: paths.filter(path => selectedPaths.has(path)), deferred: paths.filter(path => deferredPaths.has(path)) }])),
    accounting: { population: result.report.population.sources, candidateBlobs: result.report.population.candidateBlobs, deferredBlobs: result.report.deferred.length, deferredRows,
      deferredVendored: [...deferredPaths].filter(path => VENDORED.test(path)).length,
      closes: result.report.selected.blobs + result.report.deferred.length === result.report.population.candidateBlobs },
  } };
}
