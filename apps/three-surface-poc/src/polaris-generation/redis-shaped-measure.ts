import { createHash } from 'node:crypto';

import { DEFAULT_DISCOVERY_BUDGET, DOSSIER_DISCOVERY_BUDGET, DOSSIER_READER_QUESTIONS, buildExcerpt, discoverAndSelect, quotableGenerationSources, type DiscoveryBudget, type DiscoveryResult, type GenerationSource } from '@syzygy/polaris-generation-core';

import { CORE_FILES, DESIGN_DOCS, buildRedisShapedFixture, redisShapedFiles, type RedisShapedFixture } from './redis-shaped-fixture.js';
import { readRepoCorpus, type RepoCorpus } from './repo-corpus.js';

const VENDORED = /^(?:deps|vendor|third_party)\//u;

const CODE_PATH = /\.(?:c|h)$/u;
const codeLines = (text: string): number => text.split('\n').filter(line => line !== '' && !/^[ /*[]/u.test(line)).length;
const mean = (values: readonly number[]): number => (values.length === 0 ? 0 : Math.round(values.reduce((a, b) => a + b, 0) / values.length));

function measureExcerpts(selected: readonly GenerationSource[], budget: DiscoveryBudget): RedisShapedMeasurement['excerpts'] {
  const first = new Map<string, GenerationSource>();
  for (const source of selected) if (!first.has(source.path)) first.set(source.path, source);
  const rows = [...first].sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)).map(([path, source]) => {
    const text = source.body ?? source.spans[0]?.text ?? '';
    const before = [...text].slice(0, budget.maxExcerptChars).join('');
    const after = buildExcerpt(path, text, source.segment?.start ?? 0, budget.maxExcerptChars);
    return { path, before, after };
  });
  const code = rows.filter(row => CODE_PATH.test(row.path));
  const byKind: Record<string, number> = {};
  for (const row of rows) byKind[row.after.kind] = (byKind[row.after.kind] ?? 0) + 1;
  const sample = rows.find(row => row.path === 'src/ae.c') ?? rows[0]!;
  return {
    files: rows.length, byKind, codeFiles: code.length,
    before: { meanChars: mean(rows.map(row => row.before.length)), codeFilesWithNoCodeLine: code.filter(row => codeLines(row.before) === 0).length,
      codeFilesLicenceOnly: code.filter(row => row.before.includes('Copyright') && codeLines(row.before) === 0).length },
    after: { meanChars: mean(rows.map(row => row.after.text.length)), codeFilesWithNoCodeLine: code.filter(row => codeLines(row.after.text) === 0).length,
      licenceCommentInExcerpt: code.filter(row => row.after.text.includes('Copyright')).length, meanCodeLines: mean(code.map(row => codeLines(row.after.text))), licenceRangeRecorded: code.filter(row => row.after.licenceSkipped !== null).length },
    coreMechanisms: Object.fromEntries(Object.entries(CORE_FILES).map(([role, paths]) => {
      const inRole = rows.filter(row => (paths as readonly string[]).includes(row.path));
      return [role, { files: inRole.length, beforeWithCodeLine: inRole.filter(row => codeLines(row.before) > 0).length, afterWithCodeLine: inRole.filter(row => codeLines(row.after.text) > 0).length }];
    })),
    sample: { path: sample.path, before: sample.before, after: sample.after.text, afterKind: sample.after.kind, afterRanges: sample.after.ranges, licenceSkipped: sample.after.licenceSkipped },
  };
}

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
  /** What the map call sees for each selected file: the old first-N-characters excerpt against the current one. */
  readonly excerpts: {
    readonly files: number;
    readonly byKind: Readonly<Record<string, number>>;
    readonly codeFiles: number;
    /** Code lines are non-empty lines that do not start with a space, `/`, `*` or `[`: declarations, defines, tags. */
    readonly before: { readonly meanChars: number; readonly codeFilesWithNoCodeLine: number; readonly codeFilesLicenceOnly: number };
    readonly after: { readonly meanChars: number; readonly codeFilesWithNoCodeLine: number; readonly licenceCommentInExcerpt: number; readonly meanCodeLines: number; readonly licenceRangeRecorded: number };
    readonly coreMechanisms: Readonly<Record<string, { readonly files: number; readonly beforeWithCodeLine: number; readonly afterWithCodeLine: number }>>;
    readonly sample: { readonly path: string; readonly before: string; readonly after: string; readonly afterKind: string; readonly afterRanges: readonly (readonly [number, number])[]; readonly licenceSkipped: readonly [number, number] | null };
  };
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
    excerpts: measureExcerpts(result.sources.filter(source => quotableIds.has(source.sourceId)), budget),
    accounting: { population: result.report.population.sources, candidateBlobs: result.report.population.candidateBlobs, deferredBlobs: result.report.deferred.length, deferredRows,
      deferredVendored: [...deferredPaths].filter(path => VENDORED.test(path)).length,
      closes: result.report.selected.blobs + result.report.deferred.length === result.report.population.candidateBlobs },
  } };
}

export interface DossierCapMeasurement {
  readonly selectedBytes: number;
  readonly selectedBlobs: number;
  readonly partialBlobs: number;
  /** Core-mechanism files with at least one piece read, of the 18 the fixture names. */
  readonly coreRead: number;
  readonly coreReadBytes: number;
  readonly designDocsRead: number;
  /** Quotable text read, by class: design documents, other prose, source files, configuration, tests, vendored, release notes, build files. */
  readonly bytesByClass: Readonly<Record<string, number>>;
}

const classOf = (path: string): string => {
  if (VENDORED.test(path)) return 'vendored';
  if (/^tests?\//u.test(path)) return 'tests';
  if (/\.(?:conf|cfg|ini|toml|ya?ml|json)$/u.test(path)) return 'configuration';
  if (/(?:^|\/)(?:Makefile|CMakeLists\.txt)$|\.(?:mk|cmake)$/u.test(path)) return 'build';
  if (/release-?notes|changelog|changes|history|news/iu.test(path)) return 'release-notes';
  if ((DESIGN_DOCS as readonly string[]).includes(path)) return 'design-docs';
  if (/\.(?:md|rst|txt|adoc)$/u.test(path)) return 'other-prose';
  return 'source';
};

/** Heuristic-only discovery (no model) on the design-prose variant of the fixture under the dossier budget, and what it read, by class. */
export async function measureDossierCapSelection(dir: string): Promise<DossierCapMeasurement> {
  const fixture = buildRedisShapedFixture(dir, { designProse: true });
  const corpus = await readRepoCorpus(dir, { repositoryId: 'repository:synthetic-kv-server', revision: fixture.commit, include: ['**'], exclude: [], oversize: 'split' },
    { admission: { decide: async () => ({ allowed: true, permissionIdentity: 'synthetic-fixture-consent-v1' }) } });
  const result = await discoverAndSelect(corpus.sources, DOSSIER_READER_QUESTIONS.map(question => question.text), DOSSIER_DISCOVERY_BUDGET, { permitted: async () => true });
  const bytesByClass: Record<string, number> = {};
  const read = new Map<string, number>();
  for (const source of result.sources) {
    if (source.exclusion.excluded || source.spans.length === 0) continue;
    const bytes = source.spans.reduce((n, span) => n + Buffer.byteLength(span.text, 'utf8'), 0);
    read.set(source.path, (read.get(source.path) ?? 0) + bytes);
    bytesByClass[classOf(source.path)] = (bytesByClass[classOf(source.path)] ?? 0) + bytes;
  }
  const core = Object.values(CORE_FILES).flat() as string[];
  return { selectedBytes: result.report.bytes.selected, selectedBlobs: result.report.selected.blobs, partialBlobs: result.report.partialBlobs, coreRead: core.filter(path => read.has(path)).length,
    coreReadBytes: core.reduce((n, path) => n + (read.get(path) ?? 0), 0), designDocsRead: DESIGN_DOCS.filter(path => read.has(path)).length, bytesByClass };
}
