import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { DEFAULT_DISCOVERY_BUDGET, DEFERRED_BY_BUDGET, discoverAndSelect, quotableGenerationSources } from '@syzygy/polaris-generation-core';

import { CORE_FILES, redisShapedFiles } from './redis-shaped-fixture.js';
import { main } from './redis-shaped-measure-main.js';
import { measureRedisShapedDiscovery } from './redis-shaped-measure.js';

let scratch = '', run: Awaited<ReturnType<typeof measureRedisShapedDiscovery>>;
beforeAll(async () => {
  scratch = mkdtempSync(join(tmpdir(), 'syzygy-redis-shaped-test-'));
  run = await measureRedisShapedDiscovery(join(scratch, 'repo'));
}, 120_000);
afterAll(() => rmSync(scratch, { recursive: true, force: true }));

const VENDORED = /^(?:deps|vendor|third_party)\//u;

describe('discovery on a synthetic tree shaped like a large C key-value server', () => {
  it('builds the shape the measurement is about, and says in its own README that it is synthetic', () => {
    const files = redisShapedFiles();
    const paths = [...files.keys()];
    expect(paths.filter(path => /^src\/[^/]+\.c$/u.test(path)).length).toBeGreaterThanOrEqual(150);
    expect(paths.filter(path => path.startsWith('deps/')).length).toBeGreaterThan(150);
    expect(paths.some(path => path.startsWith('tests/unit/')) && paths.some(path => path.startsWith('tests/integration/'))).toBe(true);
    for (const path of ['redis.conf', 'README.md', 'LICENSE.txt', '00-RELEASENOTES', 'modules/hello.c', 'utils/lru-test.sh']) expect(files.has(path), path).toBe(true);
    expect(files.get('README.md')).toContain('SYNTHETIC');
    expect(run.fixture.oversize.length).toBeGreaterThanOrEqual(3);
    expect(paths.length).toBeGreaterThan(400);
  });

  it('splits every oversize file into contiguous pieces that are all counted', () => {
    const { corpus, fixture } = run;
    expect(corpus.count.oversizeFiles).toBe(fixture.oversize.length);
    for (const path of fixture.oversize) {
      const pieces = corpus.sources.filter(source => source.path === path);
      expect(pieces.length, path).toBeGreaterThanOrEqual(2);
      expect(pieces.every(piece => piece.segment !== undefined && !piece.exclusion.excluded), path).toBe(true);
    }
    expect(corpus.sources.length).toBe(corpus.count.sourceRows);
    expect(corpus.count.sourceRows).toBe(fixture.files.size + fixture.oversize.length);
  });

  it('selects no vendored file while first-party files remain, and counts every vendored file as deferred', () => {
    const { measurement, result } = run;
    expect(measurement.selection.vendored).toBe(0);
    const vendoredCandidates = new Set(result.sources.filter(source => VENDORED.test(source.path)).map(source => source.path));
    expect(vendoredCandidates.size).toBeGreaterThan(150);
    const deferredPaths = new Set(result.report.deferred.map(entry => entry.path));
    for (const path of vendoredCandidates) expect(deferredPaths.has(path), path).toBe(true);
    expect(measurement.accounting.deferredVendored).toBe(vendoredCandidates.size);
  });

  it('selects the core mechanism files: event loop, persistence, replication and the data types', () => {
    for (const [role, paths] of Object.entries(CORE_FILES)) {
      expect(run.measurement.coreMechanisms[role]!.selected, role).toEqual([...paths]);
      expect(run.measurement.coreMechanisms[role]!.deferred, role).toEqual([]);
    }
  });

  it('closes the denominator: selected plus deferred is every candidate, and every deferred row keeps its path under an opaque id', () => {
    const { measurement, result, corpus } = run;
    expect(measurement.accounting.closes).toBe(true);
    // A deferred oversize file is one excluded row, not one per piece; its pieces are counted in the blob's single deferral.
    const piecesOf = (path: string): number => corpus.sources.filter(source => source.path === path).length;
    const collapsed = result.report.deferred.reduce((total, entry) => total + piecesOf(entry.path) - 1, 0);
    expect(result.sources).toHaveLength(corpus.sources.length - collapsed);
    expect(measurement.selection.selectedSources).toBeLessThanOrEqual(200);
    expect(quotableGenerationSources(result.sources)).toHaveLength(measurement.selection.selectedSources);
    const deferredRows = result.sources.filter(source => source.exclusion.excluded && source.exclusion.reason === DEFERRED_BY_BUDGET);
    expect(deferredRows).toHaveLength(measurement.accounting.deferredBlobs);
    expect(deferredRows.every(row => /^s-[0-9a-f]{24}$/u.test(row.sourceId) && row.spans.length === 0)).toBe(true);
    expect(measurement.accounting.deferredBlobs + measurement.selection.selectedBlobs).toBe(measurement.accounting.candidateBlobs);
    expect(result.report.boundary).toContain('does not claim whole-repository coverage');
  });

  it('keeps vendored files out of a much smaller selection too, and admits them once nothing first-party is left', async () => {
    const small = await discoverAndSelect(run.corpus.sources, ['q'], { ...DEFAULT_DISCOVERY_BUDGET, maxSelected: 30 }, { permitted: async () => true });
    expect(quotableGenerationSources(small.sources)).toHaveLength(30);
    expect(small.sources.filter(source => !source.exclusion.excluded && source.spans.length > 0 && VENDORED.test(source.path))).toEqual([]);
    const firstParty = run.corpus.sources.filter(source => !VENDORED.test(source.path)).length;
    const wide = await discoverAndSelect(run.corpus.sources.filter(source => !VENDORED.test(source.path) || source.path === 'deps/README.md'), ['q'], DEFAULT_DISCOVERY_BUDGET, { permitted: async () => true });
    expect(firstParty).toBeGreaterThan(200);
    expect(wide.report.selected.sources).toBeLessThanOrEqual(200);
  });

  it('writes the measurement through the command and refuses to overwrite it', async () => {
    const out = join(scratch, 'measurement.json');
    expect(await main(['--out', out])).toBe(0);
    const written = JSON.parse(readFileSync(out, 'utf8'));
    expect(written.selection.vendored).toBe(0);
    expect(written.accounting.closes).toBe(true);
    await expect(main(['--out', out])).rejects.toThrow();
    expect(await main(['--bogus'])).toBe(2);
  }, 120_000);
});
