import { describe, expect, it, vi } from 'vitest';

import { DEFAULT_DISCOVERY_BUDGET, DEFERRED_BY_BUDGET, discoverAndSelect, DiscoveryRefusal, partitionSubsystems, type DiscoveryPorts } from './discovery.js';
import { generationSourcesForBody, gitBlobObjectId, quotableGenerationSources, validateGenerationSources, type GenerationSource } from './generation-source.js';

const make = (path: string, body: string, sourceId?: string): readonly GenerationSource[] =>
  generationSourcesForBody({ sourceId: sourceId ?? `s-${path.replace(/[^A-Za-z0-9]/gu, '_')}`.slice(0, 90), repositoryId: 'repository:fixture', revision: 'a'.repeat(40),
    path, objectId: gitBlobObjectId(body), evaluationId: 'evaluation:fixture', body });
const population = (files: number, subsystems = 25): GenerationSource[] => {
  const out: GenerationSource[] = [];
  for (let i = 0; i < files; i++) out.push(...make(`src/mod${i % subsystems}/file${i}.c`, `int f${i}(void) { return ${i}; }\n`));
  return out;
};
const budget = DEFAULT_DISCOVERY_BUDGET;
const allow = async () => true;
const Q = ['What are the core ideas?'];

describe('REQ-030 hierarchical budgeted discovery', () => {
  it('narrows 1,000 files under the 200 cap and keeps every file in the denominator', async () => {
    const sources = population(1000);
    const { sources: out, report } = await discoverAndSelect(sources, Q, budget, { permitted: allow });
    expect(out).toHaveLength(1000);
    expect(quotableGenerationSources(out).length).toBe(200);
    expect(out.filter(s => s.exclusion.excluded && s.exclusion.reason === DEFERRED_BY_BUDGET)).toHaveLength(800);
    expect(report).toMatchObject({ selected: { blobs: 200, sources: 200 }, rankingBasis: 'heuristic', mapCalls: 0 });
    expect(report.deferred).toHaveLength(800);
    expect(report.boundary).toContain('does not claim whole-repository coverage');
    expect(new Set(out.map(s => s.path)).size).toBe(1000);
    expect(validateGenerationSources(out)).toBe(out);
  });

  it('maps subsystems, reduces across them and selects by the model ranking', async () => {
    const sources = population(300, 6);
    const map = vi.fn(async (input: { items: readonly { blobId: string; path: string }[] }) => input.items.map(item => ({ blobId: item.blobId, claim: `claim ${item.path}`, relevance: item.path.endsWith('file7.c') ? 10 : 1 })));
    const target = sources.find(s => s.path.endsWith('/file7.c'))!;
    const reduce = vi.fn(async () => [target.sourceId, 'not-a-blob', target.sourceId]);
    const { sources: out, report } = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 1, maxGroupBlobs: 20, maxMapCalls: 100 }, { permitted: allow, map, reduce });
    expect(report).toMatchObject({ rankingBasis: 'model-reduce', reduceCalls: 1, droppedUnknownIds: 2, mapFailures: 0 });
    expect(report.mapCalls).toBe(report.subsystems);
    expect(quotableGenerationSources(out).map(q => q.sourceId)).toEqual([target.sourceId]);
    expect(report.ledger.find(entry => entry.blobId === target.sourceId)).toMatchObject({ relevance: 10, claim: 'claim src/mod1/file7.c' });
    for (const call of map.mock.calls) expect(call[0].items.length).toBeLessThanOrEqual(20);
  });

  it('drops malformed or foreign claims instead of ranking on them', async () => {
    const sources = population(6, 1);
    const [first, second, third, fourth] = sources;
    const map = async () => [
      { blobId: 'foreign-blob', claim: 'c', relevance: 5 }, { blobId: first!.sourceId, claim: 'c', relevance: 99 },
      { blobId: second!.sourceId, claim: '', relevance: 5 }, { blobId: third!.sourceId, claim: 'c', relevance: Number.NaN },
      { blobId: fourth!.sourceId, claim: 'fine', relevance: 3 }];
    const { report } = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 1 }, { permitted: allow, map });
    expect(report.droppedUnknownIds).toBe(4);
    expect(report.ledger.map(entry => entry.blobId)).toEqual([fourth!.sourceId]);
  });

  it('finds relevant material outside the conventional entry points', async () => {
    const sources = [...population(250, 5), ...make('internal/zz/q/r/s/obscure_notes.c', 'The real design lives here.\n')];
    const map = async (input: { items: readonly { blobId: string; path: string }[] }) => input.items.map(item => ({ blobId: item.blobId, claim: 'c', relevance: item.path.includes('obscure') ? 9 : 0 }));
    const without = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 3 }, { permitted: allow });
    const withMap = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 3, maxMapCalls: 100 }, { permitted: allow, map });
    expect(quotableGenerationSources(without.sources).map(q => q.sourceId)).not.toContain(sources.at(-1)!.sourceId);
    expect(quotableGenerationSources(withMap.sources).map(q => q.sourceId)).toContain(sources.at(-1)!.sourceId);
    expect(withMap.report.rankingBasis).toBe('model-map');
  });

  it('prefers documentation over tests and vendored code by the prior alone', async () => {
    const sources = [...make('vendor/x/a.c', 'v\n'), ...make('tests/t.c', 't\n'), ...make('docs/ARCHITECTURE.md', 'a\n'), ...make('README.md', 'r\n')];
    const { sources: out } = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 2 }, { permitted: allow });
    expect(quotableGenerationSources(out).map(q => q.sourceId).sort()).toEqual([sources[2]!.sourceId, sources[3]!.sourceId].sort());
  });

  it('records subsystems it had no map call for and counts failed calls without hiding them', async () => {
    const sources = population(120, 12);
    const map = vi.fn(async () => { throw new Error('boom'); });
    const { report } = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 2, maxGroupBlobs: 10 }, { permitted: allow, map });
    expect(report.mapCalls).toBe(2);
    expect(report.mapFailures).toBe(2);
    expect(report.unmappedSubsystems.length).toBe(report.subsystems);
    expect(report.rankingBasis).toBe('heuristic');
  });

  it('bounds excerpts and the claims handed to the reduce call', async () => {
    const long = 'x'.repeat(5000);
    const sources = [...make('a/one.md', long), ...population(200, 20)];
    const seen: number[] = [];
    const map = async (input: { items: readonly { blobId: string; excerpt: string }[] }) => { seen.push(...input.items.map(i => i.excerpt.length)); return input.items.map(i => ({ blobId: i.blobId, claim: 'c', relevance: 5 })); };
    let reduceClaims = 0;
    await discoverAndSelect(sources, Q, { ...budget, maxExcerptChars: 100, maxMapCalls: 100, maxReduceClaims: 30, maxGroupBlobs: 10 },
      { permitted: allow, map, reduce: async input => { reduceClaims = input.subsystems.reduce((n, s) => n + s.claims.length, 0); return []; } });
    expect(Math.max(...seen)).toBe(100);
    expect(reduceClaims).toBeLessThanOrEqual(30);
    expect(reduceClaims).toBeGreaterThan(0);
  });

  it('keeps the pieces of an oversize file together and bills each piece', async () => {
    const big = `${'int line_of_code = 42; /* padding */!\n'.repeat(3000)}end\n`;
    const bigPieces = make('src/big.c', big);
    expect(bigPieces.length).toBeGreaterThan(1);
    const sources = [...bigPieces, ...make('README.md', 'r\n'), ...make('docs/a.md', 'a\n')];
    const tight = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 2 }, { permitted: allow });
    expect(tight.sources.filter(s => s.path === 'src/big.c')).toHaveLength(1);
    expect(tight.sources.find(s => s.path === 'src/big.c')).toMatchObject({ exclusion: { excluded: true, reason: DEFERRED_BY_BUDGET } });
    expect(tight.sources.find(s => s.path === 'src/big.c')!.segment).toBeUndefined();
    expect(validateGenerationSources(tight.sources)).toHaveLength(3);
    const roomy = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 200 }, { permitted: allow });
    expect(roomy.sources).toEqual(sources);
    expect(roomy.report.deferred).toEqual([]);
  });

  it('refuses model calls without egress permission and an out-of-range cap', async () => {
    const map = vi.fn(async () => []);
    await expect(discoverAndSelect(population(5), Q, budget, { permitted: async () => false, map })).rejects.toThrow(DiscoveryRefusal);
    expect(map).not.toHaveBeenCalled();
    await expect(discoverAndSelect(population(5), Q, { ...budget, maxSelected: 201 }, { permitted: allow })).rejects.toThrow('invalid-budget');
    await expect(discoverAndSelect(population(5), Q, { ...budget, maxSelected: 0 }, { permitted: allow })).rejects.toThrow('invalid-budget');
  });

  it('passes through already-excluded rows untouched and partitions deterministically', async () => {
    const excluded: GenerationSource = { ...make('a/x.bin', 'b\n')[0]!, exclusion: { excluded: true, reason: 'binary-or-non-utf8' }, spans: [] };
    delete (excluded as { body?: string }).body;
    const sources = [excluded, ...population(10, 2)];
    const { sources: out, report } = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 3 }, { permitted: allow });
    expect(out[0]).toBe(excluded);
    expect(report.population).toEqual({ sources: 11, alreadyExcluded: 1, candidateBlobs: 10 });
    const groups = (n: number) => partitionSubsystems(population(n, 3).map(s => ({ blobId: s.sourceId, path: s.path, pieces: [s], heuristic: 0 })), 4).map(g => [g.name, g.blobs.length]);
    expect(groups(30)).toEqual(groups(30));
    expect(groups(30).every(([, n]) => (n as number) <= 4)).toBe(true);
    expect(groups(30).reduce((n, [, c]) => n + (c as number), 0)).toBe(30);
  });
});
