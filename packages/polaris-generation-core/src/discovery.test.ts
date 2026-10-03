import { randomBytes } from 'node:crypto';
import { describe, expect, it, vi } from 'vitest';

import { DEFAULT_DISCOVERY_BUDGET, DEFERRED_BY_BUDGET, MAP_CLAIMS_PER_ITEM, discoverAndSelect, DiscoveryRefusal, partitionSubsystems, reportFromReceipts, type DiscoveryPorts, type DiscoveryReceipt } from './discovery.js';
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
/** One key for a live run and its replay, so the keyed deferred ids compare equal. */
const RUN_KEY = randomBytes(32);
const allow = async () => true;
type Item = { readonly blobId: string; readonly path: string; readonly excerpt: string };
const mapOf = (relevance: (item: Item) => number) => async (input: { items: readonly Item[] }) => ({
  claims: input.items.map(item => ({ blobId: item.blobId, claim: `claim ${item.path}`, relevance: relevance(item) })), usageUnits: 1 });
const model = (extra: Partial<DiscoveryPorts> = {}): DiscoveryPorts & { receipts: DiscoveryReceipt[] } => {
  const receipts: DiscoveryReceipt[] = [];
  return { permitted: allow, receipt: async r => { receipts.push(r); }, runKey: RUN_KEY, ...extra, receipts };
};
const Q = ['What are the core ideas?'];

describe('REQ-030 hierarchical budgeted discovery', () => {
  it('narrows 1,000 files under the 200 cap and keeps every file in the denominator', async () => {
    const sources = population(1000);
    const { sources: out, report, receipts } = await discoverAndSelect(sources, Q, budget, { permitted: allow });
    expect(out).toHaveLength(1000);
    expect(quotableGenerationSources(out).length).toBe(200);
    expect(out.filter(s => s.exclusion.excluded && s.exclusion.reason === DEFERRED_BY_BUDGET)).toHaveLength(800);
    expect(report).toMatchObject({ selected: { blobs: 200, sources: 200 }, rankingBasis: 'heuristic', mapCalls: 0 });
    expect(report.deferred).toHaveLength(800);
    expect(report.deferred[0]!.detail).toContain('ranked below the selection cut');
    expect(report.boundary).toContain('does not claim whole-repository coverage');
    expect(report.basisNote).toContain('prior only');
    expect(receipts).toEqual([]);
    expect(new Set(out.map(s => s.path)).size).toBe(1000);
    expect(validateGenerationSources(out)).toBe(out);
  });

  it('says every candidate blob was selected only when none was deferred', async () => {
    expect((await discoverAndSelect(population(3), Q, budget, { permitted: allow })).report.boundary).toBe('every candidate blob was selected');
  });

  it('maps subsystems, reduces across them and selects by the model ranking', async () => {
    const sources = population(300, 6);
    const map = vi.fn(mapOf(item => item.path.endsWith('file7.c') ? 10 : 1));
    const target = sources.find(s => s.path.endsWith('/file7.c'))!;
    const reduce = vi.fn(async () => ({ ranked: [target.sourceId, 'not-a-blob', target.sourceId], usageUnits: 3 }));
    const ports = model({ map, reduce });
    const { sources: out, report } = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 1, maxGroupBlobs: 20, maxMapCalls: 100 }, ports);
    expect(report).toMatchObject({ rankingBasis: 'model-reduce', reduceCalls: 1, droppedUnknownIds: 2, mapFailures: 0, reduceFailures: 0 });
    expect(report.basisNote).toContain('Inferred');
    expect(report.mapCalls).toBe(report.subsystems);
    expect(quotableGenerationSources(out).map(q => q.sourceId)).toEqual([target.sourceId]);
    expect(report.ledger.find(entry => entry.blobId === target.sourceId)).toMatchObject({ relevance: 10, claim: 'claim src/mod1/file7.c' });
    for (const call of map.mock.calls) expect(call[0].items.length).toBeLessThanOrEqual(20);
  });

  it('finds relevant material outside the conventional entry points', async () => {
    const sources = [...population(250, 5), ...make('internal/zz/q/r/s/obscure_notes.c', 'The real design lives here.\n')];
    const without = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 3 }, { permitted: allow });
    const withMap = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 3, maxMapCalls: 100 }, model({ map: mapOf(item => item.path.includes('obscure') ? 9 : 0) }));
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
    const map = vi.fn(async () => { throw new Error('boom'); });
    const ports = model({ map });
    const { report } = await discoverAndSelect(population(120, 12), Q, { ...budget, maxMapCalls: 2, maxGroupBlobs: 10 }, ports);
    expect(report).toMatchObject({ mapCalls: 2, mapFailures: 2, rankingBasis: 'heuristic' });
    expect(report.unmappedSubsystems.length).toBe(report.subsystems);
    expect(ports.receipts.filter(r => r.outcome === 'failed').map(r => r.detail)).toEqual(['boom', 'boom']);
  });

  it('drops malformed or foreign claims instead of ranking on them, and keeps none of a rejected reply', async () => {
    const sources = population(6, 1);
    const [first, second, third, fourth] = sources;
    const map = async () => ({ usageUnits: 1, claims: [
      { blobId: 'foreign-blob', claim: 'c', relevance: 5 }, { blobId: first!.sourceId, claim: 'c', relevance: 99 }, null as never, { blobId: 7 as never, claim: 'c', relevance: 1 },
      { blobId: second!.sourceId, claim: '', relevance: 5 }, { blobId: third!.sourceId, claim: 'c', relevance: Number.NaN },
      { blobId: fourth!.sourceId, claim: 'fine', relevance: 3 }] });
    const { report } = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 1 }, model({ map }));
    expect(report.droppedUnknownIds).toBe(6);
    expect(report.ledger.map(entry => entry.blobId)).toEqual([fourth!.sourceId]);
    const rejected = model({ map: async () => ({ claims: 'nope' }) as never });
    const result = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 1 }, rejected);
    expect(result.report).toMatchObject({ mapFailures: 1, rankingBasis: 'heuristic', ledger: [] });
    expect(rejected.receipts.at(-1)).toMatchObject({ outcome: 'failed', detail: 'invalid-map-reply' });
  });

  it('truncates a claim to maxClaimChars', async () => {
    const sources = population(2, 1);
    const long = 'x'.repeat(5000);
    const { report } = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxClaimChars: 40 }, model({
      map: async input => ({ usageUnits: null, claims: input.items.map(i => ({ blobId: i.blobId, claim: long, relevance: 5 })) }) }));
    expect(report.ledger.every(entry => entry.claim.length === 40)).toBe(true);
    expect(report.ledger.length).toBe(2);
  });

  it('bounds excerpts and the claims handed to the reduce call', async () => {
    const sources = [...make('a/one.md', 'x'.repeat(5000)), ...population(200, 20)];
    const seen: number[] = [];
    let reduceClaims = 0;
    await discoverAndSelect(sources, Q, { ...budget, maxExcerptChars: 100, maxMapCalls: 100, maxReduceClaims: 30, maxGroupBlobs: 10 }, model({
      map: async input => { seen.push(...input.items.map(i => i.excerpt.length)); return mapOf(() => 5)(input); },
      reduce: async input => { reduceClaims = input.subsystems.reduce((n, s) => n + s.claims.length, 0); return { ranked: [], usageUnits: null }; } }));
    expect(Math.max(...seen)).toBe(100);
    expect(reduceClaims).toBeLessThanOrEqual(30);
    expect(reduceClaims).toBeGreaterThan(0);
  });

  it('falls back to map relevance when the reduce throws, returns null, or returns a string, and counts it', async () => {
    const sources = population(40, 4);
    const target = sources.find(s => s.path.endsWith('file9.c'))!;
    for (const reduce of [async () => { throw new Error('reduce down'); }, async () => null, async () => ({ ranked: 'abc', usageUnits: 1 }), async () => ({ ranked: [1, 2], usageUnits: 1 })]) {
      const ports = model({ map: mapOf(item => item.path.endsWith('file9.c') ? 9 : 1), reduce: reduce as never });
      const { report, sources: out } = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 1, maxMapCalls: 10 }, ports);
      expect(report).toMatchObject({ reduceCalls: 1, reduceFailures: 1, rankingBasis: 'model-map' });
      expect(quotableGenerationSources(out).map(q => q.sourceId)).toEqual([target.sourceId]);
      expect(ports.receipts.at(-1)).toMatchObject({ kind: 'reduce', outcome: 'failed' });
    }
    for (const ranked of ['abc', [1, 2], null, undefined]) {
      const ports = model({ map: mapOf(() => 5), reduce: (async () => ({ ranked, usageUnits: 1 })) as never });
      await discoverAndSelect(sources, Q, { ...budget, maxSelected: 1, maxMapCalls: 10 }, ports);
      expect(ports.receipts.at(-1), String(ranked)).toMatchObject({ kind: 'reduce', outcome: 'failed', detail: 'invalid-reduce-reply' });
    }
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
    expect(tight.report.selected).toEqual({ blobs: 2, sources: 2 });
    expect(validateGenerationSources(tight.sources)).toHaveLength(3);
    const roomy = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 200 }, { permitted: allow });
    expect(roomy.sources).toEqual(sources);
    expect(roomy.report.deferred).toEqual([]);
    expect(roomy.report.selected).toEqual({ blobs: 3, sources: bigPieces.length + 2 });
  });

  it('says "did not fit" only for a multi-piece blob skipped for the remaining cap', async () => {
    const big = `${'int line_of_code = 42; /* padding */!\n'.repeat(3000)}end\n`;
    const sources = [...make('README.md', 'r\n'), ...make('src/big.c', big), ...make('docs/z.md', 'z\n')];
    const { report } = await discoverAndSelect(sources, Q, { ...budget, maxSelected: 2 }, { permitted: allow });
    const bigRow = report.deferred.find(d => d.path === 'src/big.c')!;
    expect(bigRow.detail).toContain('did not fit');
    expect(report.deferred.every(d => d.path === 'src/big.c' || d.detail.includes('ranked below'))).toBe(true);
  });

  it('asks permission per provider call with a request digest, and a refused call is not made', async () => {
    const asked: string[] = [];
    const map = vi.fn(mapOf(() => 5));
    const ports = model({ map, permitted: async call => { asked.push(`${call.kind}:${call.subsystem ?? ''}:${call.itemCount}:${call.requestDigest.length}`); return call.subsystem !== 'src/mod0'; } });
    const { report } = await discoverAndSelect(population(40, 2), Q, { ...budget, maxMapCalls: 10, maxGroupBlobs: 20 }, ports);
    expect(asked.length).toBe(2);
    expect(asked.every(entry => entry.endsWith(':64'))).toBe(true);
    expect(map).toHaveBeenCalledTimes(1);
    expect(report.refusedCalls).toBe(1);
    expect(ports.receipts.filter(r => r.outcome === 'refused')).toHaveLength(1);
    expect(report.unmappedSubsystems).toEqual(['src/mod0']);
  });

  it('treats any permission answer other than true as a refusal', async () => {
    for (const answer of [1, 'yes', {}, undefined]) {
      const map = vi.fn(mapOf(() => 5));
      await discoverAndSelect(population(5), Q, budget, model({ map, permitted: (async () => answer) as never }));
      expect(map).not.toHaveBeenCalled();
    }
  });

  it('writes a dispatching receipt before each call and an outcome after, with digests that differ per request', async () => {
    const order: string[] = [];
    const ports = model({ map: async input => { order.push('call'); return mapOf(() => 5)(input); }, receipt: async r => { order.push(r.outcome); } });
    const { receipts } = await discoverAndSelect(population(40, 4), Q, { ...budget, maxMapCalls: 10, maxGroupBlobs: 20 }, ports);
    expect(order.slice(0, 3)).toEqual(['dispatching', 'call', 'accepted']);
    expect(new Set(receipts.filter(r => r.outcome === 'accepted').map(r => r.requestDigest)).size).toBe(receipts.filter(r => r.outcome === 'accepted').length);
    expect(receipts.filter(r => r.outcome === 'dispatching')).toHaveLength(receipts.filter(r => r.outcome === 'accepted').length);
  });

  it('stops when a receipt cannot be written, and when model ports have no receipt port', async () => {
    await expect(discoverAndSelect(population(5), Q, budget, { permitted: allow, map: mapOf(() => 1), receipt: async () => { throw new Error('disk'); } })).rejects.toThrow('receipt-write-failed');
    await expect(discoverAndSelect(population(5), Q, budget, { permitted: allow, map: mapOf(() => 1) })).rejects.toThrow('model-ports-need-a-receipt-port');
  });

  it('truncates failure detail and rebuilds an identical report from receipts alone', async () => {
    const sources = population(120, 6);
    let n = 0, asks = 0;
    const map = async (input: { items: readonly Item[] }) => {
      if (n++ === 1) throw new Error('x'.repeat(900));
      return { usageUnits: 2, claims: [...input.items.map(item => ({ blobId: item.blobId, claim: 'c', relevance: item.path.endsWith('3.c') ? 8 : 2 })), { blobId: 'foreign', claim: 'c', relevance: 1 }] };
    };
    const ports = model({ map, reduce: async () => ({ ranked: ['foreign', ...sources.slice(5, 9).map(s => s.sourceId)], usageUnits: 4 }), permitted: async () => ++asks !== 3 });
    const budgetHere = { ...budget, maxSelected: 10, maxMapCalls: 6, maxGroupBlobs: 10 };
    const live = await discoverAndSelect(sources, Q, budgetHere, ports);
    expect(live.receipts.find(r => r.outcome === 'failed')!.detail).toHaveLength(200);
    const replay = await reportFromReceipts(sources, Q, budgetHere, JSON.parse(JSON.stringify(live.receipts)), RUN_KEY);
    expect(replay.report).toEqual(live.report);
    expect(replay.sources).toEqual(live.sources);
    expect(live.report.mapFailures).toBeGreaterThan(0);
    expect(live.report.refusedCalls).toBeGreaterThan(0);
    expect(live.report.droppedUnknownIds).toBeGreaterThan(0);
  });

  const liveRun = async (ports: DiscoveryPorts & { receipts: DiscoveryReceipt[] }, sources = population(120, 6), questions = Q) => {
    const budgetHere = { ...budget, maxSelected: 10, maxMapCalls: 6, maxGroupBlobs: 10 };
    const live = await discoverAndSelect(sources, questions, budgetHere, ports);
    return { live, budgetHere, sources, saved: JSON.parse(JSON.stringify(ports.receipts)) as DiscoveryReceipt[] };
  };

  it('replays a map-only run and a no-port run to the live report, installing only the port kinds the receipts hold', async () => {
    const mapOnly = await liveRun(model({ map: mapOf(item => (item.path.endsWith('3.c') ? 8 : 2)) }));
    expect(mapOnly.live.report).toMatchObject({ rankingBasis: 'model-map', reduceCalls: 0, reduceFailures: 0 });
    const replayMap = await reportFromReceipts(mapOnly.sources, Q, mapOnly.budgetHere, mapOnly.saved, RUN_KEY);
    expect(replayMap.report).toEqual(mapOnly.live.report);
    expect(replayMap.sources).toEqual(mapOnly.live.sources);
    const none = await liveRun(model());
    expect(none.saved).toEqual([]);
    const replayNone = await reportFromReceipts(none.sources, Q, none.budgetHere, none.saved, RUN_KEY);
    expect(replayNone.report).toEqual(none.live.report);
    expect(replayNone.sources).toEqual(none.live.sources);
    expect(none.live.report).toMatchObject({ rankingBasis: 'heuristic', mapCalls: 0, reduceCalls: 0, refusedCalls: 0 });
  });

  it('fails a replay whose population or reader question differs from the recorded run', async () => {
    const run = await liveRun(model({ map: mapOf(() => 5), reduce: async () => ({ ranked: [], usageUnits: 1 }) }));
    await expect(reportFromReceipts(run.sources, Q, run.budgetHere, run.saved)).resolves.toBeDefined();
    await expect(reportFromReceipts(run.sources, ['A different question?'], run.budgetHere, run.saved)).rejects.toThrow('receipt-request-mismatch');
    const changed = [...run.sources.slice(1), ...make('src/mod0/changed.c', 'int changed(void) { return 1; }\n')];
    await expect(reportFromReceipts(changed, Q, run.budgetHere, run.saved)).rejects.toThrow('receipt-request-mismatch');
    await expect(reportFromReceipts(run.sources, Q, run.budgetHere, run.saved.filter(receipt => receipt.kind !== 'map' || receipt.ordinal !== 0))).rejects.toThrow('receipt-missing-for-call');
    const itemCountOnly = run.saved.map(receipt => (receipt.ordinal === 0 ? { ...receipt, itemCount: receipt.itemCount + 1 } : receipt));
    await expect(reportFromReceipts(run.sources, Q, run.budgetHere, itemCountOnly)).rejects.toThrow('receipt-request-mismatch');
  });

  it('keeps only a non-negative safe integer as usage, ignores a live reply\'s own dropped count, and cuts an overlong reply', async () => {
    const sources = population(6, 1);
    const usages = [-1, 1.5, Number.NaN, Number.POSITIVE_INFINITY, 2 ** 60, '3', null, undefined, 0, 7];
    const seen: (number | null)[] = [];
    for (const usageUnits of usages) {
      const ports = model({ map: async input => ({ ...(await mapOf(() => 5)(input)), usageUnits }) as never });
      await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 2 }, ports);
      seen.push(ports.receipts.find(receipt => receipt.outcome === 'accepted')!.usageUnits);
    }
    expect(seen).toEqual([null, null, null, null, null, null, null, null, 0, 7]);
    const lying = model({ map: async input => ({ ...(await mapOf(() => 5)(input)), dropped: 999 }) as never, reduce: async () => ({ ranked: [], usageUnits: 1, dropped: 500 }) as never });
    const { report } = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 2 }, lying);
    expect(report.droppedUnknownIds).toBe(0);
    expect(lying.receipts.every(receipt => receipt.dropped === 0)).toBe(true);
    const flood = model({ map: async input => ({ usageUnits: 1, claims: Array.from({ length: 40 }, (_, i) => ({ blobId: input.items[i % input.items.length]!.blobId, claim: 'c', relevance: 5 })) }) });
    const cut = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 2 }, flood);
    expect(cut.report.droppedUnknownIds).toBe(40 - 6 * MAP_CLAIMS_PER_ITEM);
    expect((flood.receipts.find(receipt => receipt.outcome === 'accepted')!.reply as { claims: unknown[] }).claims).toHaveLength(6 * MAP_CLAIMS_PER_ITEM);
    const floodRank = model({ map: mapOf(() => 5), reduce: async () => ({ ranked: Array.from({ length: 60 }, () => sources[0]!.sourceId), usageUnits: 1 }) });
    const ranked = await discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 2 }, floodRank);
    expect((floodRank.receipts.find(receipt => receipt.kind === 'reduce' && receipt.outcome === 'accepted')!.reply as { ranked: string[] }).ranked).toEqual([sources[0]!.sourceId]);
    expect(ranked.report.droppedUnknownIds).toBe(59);
    // A replay does honour the recorded drop count.
    const replay = await reportFromReceipts(sources, Q, { ...budget, maxMapCalls: 5, maxSelected: 2 }, JSON.parse(JSON.stringify(floodRank.receipts)), RUN_KEY);
    expect(replay.report).toEqual(ranked.report);
  });

  it('hands every port call the abort signal of the run', async () => {
    const controller = new AbortController();
    const signals: AbortSignal[] = [];
    const ports = model({ map: async (input, signal) => { signals.push(signal); return mapOf(() => 5)(input); }, reduce: async (_input, signal) => { signals.push(signal); return { ranked: [], usageUnits: 1 }; } });
    await discoverAndSelect(population(6, 1), Q, { ...budget, maxMapCalls: 5 }, ports, controller.signal);
    expect(signals).toHaveLength(2);
    expect(signals.every(signal => signal === controller.signal)).toBe(true);
    const mid = new AbortController();
    let observed = false;
    await expect(discoverAndSelect(population(6, 1), Q, budget, model({ map: async (input, signal) => { mid.abort(); observed = signal.aborted; return mapOf(() => 5)(input); } }), mid.signal)).rejects.toThrow('cancelled');
    expect(observed).toBe(true);
  });

  it('cancels between and during calls, including before the reduce', async () => {
    const sources = population(40, 4);
    const controller = new AbortController();
    let calls = 0;
    const map = async (input: { items: readonly Item[] }) => { if (++calls === 2) controller.abort(); return mapOf(() => 5)(input); };
    await expect(discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 10, maxGroupBlobs: 10 }, model({ map }), controller.signal)).rejects.toThrow('cancelled');
    const late = new AbortController();
    const reduce = vi.fn(async () => ({ ranked: [], usageUnits: null }));
    await expect(discoverAndSelect(sources, Q, { ...budget, maxMapCalls: 1, maxGroupBlobs: 100 }, model({ map: async input => { late.abort(); return mapOf(() => 5)(input); }, reduce }), late.signal)).rejects.toThrow('cancelled');
    expect(reduce).not.toHaveBeenCalled();
    const hang = new AbortController();
    const pending = discoverAndSelect(sources, Q, budget, model({ map: () => new Promise<never>(() => undefined) }), hang.signal);
    setTimeout(() => hang.abort(), 20);
    await expect(pending).rejects.toThrow('cancelled');
  });

  it('never calls a port once the signal is already aborted', async () => {
    const done = new AbortController(); done.abort();
    const map = vi.fn(mapOf(() => 1)), permitted = vi.fn(async () => true);
    await expect(discoverAndSelect(population(10), Q, budget, model({ map, permitted }), done.signal)).rejects.toThrow('cancelled');
    expect(map).not.toHaveBeenCalled();
    expect(permitted).not.toHaveBeenCalled();
  });

  it('rejects an out-of-range budget', async () => {
    await expect(discoverAndSelect(population(5), Q, { ...budget, maxSelected: 201 }, { permitted: allow })).rejects.toThrow('invalid-budget');
    await expect(discoverAndSelect(population(5), Q, { ...budget, maxSelected: 0 }, { permitted: allow })).rejects.toThrow('invalid-budget');
    await expect(discoverAndSelect(population(5), Q, { ...budget, maxClaimChars: 0 }, { permitted: allow })).rejects.toThrow('invalid-budget');
    await expect(discoverAndSelect(population(5), Q, budget, { permitted: allow })).resolves.toBeDefined();
    expect(DiscoveryRefusal.name).toBe('DiscoveryRefusal');
  });

  it('passes already-excluded rows through untouched and partitions deterministically', async () => {
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

describe('deferred-by-budget ids (syzygy-75ds)', () => {
  const deferredIds = async (runKey?: Buffer) => {
    const out = (await discoverAndSelect(population(5), Q, { ...budget, maxSelected: 2 }, { permitted: allow, ...(runKey === undefined ? {} : { runKey }) })).sources;
    return out.filter(source => source.exclusion.excluded && (source.exclusion as { reason: string }).reason === DEFERRED_BY_BUDGET).map(source => source.sourceId);
  };
  it('carry a keyed opaque id: valid, stable within a key, different across keys', async () => {
    const key = randomBytes(32);
    const a = await deferredIds(key);
    expect(a.length).toBeGreaterThan(0);
    for (const id of a) expect(id).toMatch(/^s-[0-9a-f]{24}$/u);
    expect(await deferredIds(key)).toEqual(a);
    expect(await deferredIds(randomBytes(32))).not.toEqual(a);
  });
});
