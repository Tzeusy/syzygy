/**
 * Hierarchical, budgeted discovery (REQ-polaris-generation-030). A repository
 * with thousands of files cannot cross the provider boundary whole, and the
 * pipeline refuses more than 200 quotable sources. This module narrows a
 * counted population to a bounded selection and accounts for the rest:
 *
 *   partition into subsystems -> map (claim ledger per subsystem, bounded
 *   excerpts) -> reduce (rank across subsystems) -> select under the cap.
 *
 * Every blob it does not select stays in the population as an excluded row
 * with reason `deferred-by-budget`, so the denominator never shrinks. It is
 * pure: the map and reduce calls are injected ports, and nothing here reads
 * a repository or calls a provider. A model ranking is an Inferred claim; the
 * report says which basis ordered the selection.
 */

import { digestCanonicalJson } from './canonical-json.js';
import type { GenerationSource } from './generation-source.js';

export const DEFERRED_BY_BUDGET = 'deferred-by-budget';
export const PIPELINE_QUOTABLE_CAP = 200;

export interface DiscoveryBudget {
  /** Quotable GenerationSources (pieces count one each) to keep; at most 200. */
  readonly maxSelected: number;
  readonly maxMapCalls: number;
  readonly maxExcerptChars: number;
  readonly maxGroupBlobs: number;
  /** Claims per subsystem handed to the reduce call. */
  readonly claimsPerGroup: number;
  readonly maxReduceClaims: number;
  /** Longer claim text is truncated to this many characters. */
  readonly maxClaimChars: number;
}

export const DEFAULT_DISCOVERY_BUDGET: DiscoveryBudget = {
  maxSelected: PIPELINE_QUOTABLE_CAP, maxMapCalls: 40, maxExcerptChars: 1500, maxGroupBlobs: 40, claimsPerGroup: 8, maxReduceClaims: 400, maxClaimChars: 400,
};

export interface DiscoveryClaim { readonly blobId: string; readonly claim: string; readonly relevance: number }
export interface MapInput {
  readonly subsystem: string;
  readonly readerQuestions: readonly string[];
  readonly items: readonly { readonly blobId: string; readonly path: string; readonly excerpt: string }[];
}
export interface ReduceInput {
  readonly readerQuestions: readonly string[];
  readonly maxSelected: number;
  readonly subsystems: readonly { readonly subsystem: string; readonly blobs: number; readonly claims: readonly (DiscoveryClaim & { readonly path: string })[] }[];
}
/** `dropped` is only for replay: a count the recording run already discarded. */
export interface MapReply { readonly claims: readonly DiscoveryClaim[]; readonly usageUnits: number | null; readonly dropped?: number }
export interface ReduceReply { readonly ranked: readonly string[]; readonly usageUnits: number | null; readonly dropped?: number }

/** One provider call, asked about before it is made. */
export interface DiscoveryCall { readonly kind: 'map' | 'reduce'; readonly subsystem?: string; readonly itemCount: number; readonly requestDigest: string }
/** The durable record of one call, shaped like a stage receipt: what was asked
 * (digest), what it cost, what happened, and the failure detail truncated. An
 * `accepted` receipt carries the validated reply, so a report can be rebuilt
 * from receipts alone (`reportFromReceipts`). A `dispatching` receipt is written
 * before the call, so a crash leaves evidence the call may have left the machine. */
export interface DiscoveryReceipt {
  readonly kind: 'map' | 'reduce';
  readonly ordinal: number;
  readonly subsystem?: string;
  readonly requestDigest: string;
  readonly itemCount: number;
  readonly outcome: 'dispatching' | 'accepted' | 'failed' | 'refused';
  readonly usageUnits: number | null;
  readonly dropped: number;
  readonly reply?: { readonly claims: readonly DiscoveryClaim[] } | { readonly ranked: readonly string[] };
  readonly detail?: string;
}
export interface DiscoveryPorts {
  /** Asked once per provider call; anything but `true` means the call is not made. */
  readonly permitted: (call: DiscoveryCall) => Promise<boolean>;
  readonly map?: (input: MapInput) => Promise<MapReply>;
  /** Blob ids in priority order; unknown ids are dropped and counted. */
  readonly reduce?: (input: ReduceInput) => Promise<ReduceReply>;
  /** Required with `map` or `reduce`; a rejection stops discovery. */
  readonly receipt?: (receipt: DiscoveryReceipt) => Promise<void>;
}

export interface DiscoveryReport {
  readonly boundary: string;
  readonly population: { readonly sources: number; readonly alreadyExcluded: number; readonly candidateBlobs: number };
  readonly subsystems: number;
  readonly mapCalls: number;
  readonly mapFailures: number;
  readonly refusedCalls: number;
  readonly unmappedSubsystems: readonly string[];
  readonly reduceCalls: number;
  readonly reduceFailures: number;
  readonly rankingBasis: 'model-reduce' | 'model-map' | 'heuristic';
  readonly basisNote: string;
  readonly droppedUnknownIds: number;
  readonly selected: { readonly blobs: number; readonly sources: number };
  readonly deferred: readonly { readonly blobId: string; readonly path: string; readonly detail: string }[];
  readonly ledger: readonly (DiscoveryClaim & { readonly path: string })[];
}
export interface DiscoveryResult { readonly sources: readonly GenerationSource[]; readonly report: DiscoveryReport; readonly receipts: readonly DiscoveryReceipt[] }

export class DiscoveryRefusal extends Error {
  constructor(readonly reason: string) { super(`Discovery refused: ${reason}`); this.name = 'DiscoveryRefusal'; }
}

interface Blob { readonly blobId: string; readonly path: string; readonly pieces: readonly GenerationSource[]; heuristic: number }

const pieceBase = (source: GenerationSource): string =>
  source.segment === undefined ? source.sourceId : source.sourceId.replace(/-p[0-9]+$/u, '');

/** Quotable pieces of one file travel together: a partial set would break
 * contiguity, and the whole file is the unit a reader cites. */
function candidateBlobs(sources: readonly GenerationSource[]): Blob[] {
  const byId = new Map<string, GenerationSource[]>();
  for (const source of sources) {
    if (source.exclusion.excluded || source.spans.length === 0) continue;
    const id = pieceBase(source);
    byId.set(id, [...(byId.get(id) ?? []), source]);
  }
  return [...byId].map(([blobId, pieces]) => ({ blobId, path: pieces[0]!.path, pieces, heuristic: heuristicScore(pieces[0]!.path, pieces) }));
}

/** Path-and-size prior used as the fallback ranking and as the tie-break. */
export function heuristicScore(path: string, pieces: readonly GenerationSource[]): number {
  const parts = path.split('/'), name = (parts.at(-1) ?? '').toLowerCase();
  let score = 0;
  if (/^(readme|overview|architecture|design|concepts?|internals?|contributing|index)(\.|$)/u.test(name)) score += 50;
  if (parts.slice(0, -1).some(part => /^(docs?|documentation|design|architecture)$/iu.test(part))) score += 30;
  if (/\.(md|rst|txt|adoc)$/u.test(name)) score += 10;
  if (parts.slice(0, -1).some(part => /^(tests?|__tests__|spec|fixtures?|examples?)$/iu.test(part)) || /\.(test|spec)\./u.test(name)) score -= 20;
  if (parts.slice(0, -1).some(part => /^(vendor|third_party|deps|node_modules|dist|build)$/iu.test(part))) score -= 40;
  return score - 2 * (parts.length - 1) - pieces.length;
}

/** Subsystems by leading path segments, refined until each holds at most
 * `maxGroupBlobs` files; a flat directory beyond the cap is chunked in path
 * order (`dir#2`). Deterministic for one population. */
export function partitionSubsystems(blobs: readonly Blob[], maxGroupBlobs: number): { readonly name: string; readonly blobs: readonly Blob[] }[] {
  if (!Number.isSafeInteger(maxGroupBlobs) || maxGroupBlobs < 1) throw new DiscoveryRefusal('invalid-budget');
  const out: { name: string; blobs: Blob[] }[] = [];
  const split = (items: Blob[], depth: number, prefix: string): void => {
    const direct: Blob[] = [], children = new Map<string, Blob[]>();
    for (const item of items) {
      const parts = item.path.split('/');
      if (parts.length - 1 <= depth) direct.push(item);
      else children.set(parts[depth]!, [...(children.get(parts[depth]!) ?? []), item]);
    }
    if (items.length <= maxGroupBlobs || children.size === 0) {
      const sorted = [...items].sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : 0);
      for (let at = 0; at < sorted.length; at += maxGroupBlobs) {
        out.push({ name: `${prefix || '.'}${sorted.length > maxGroupBlobs ? `#${at / maxGroupBlobs + 1}` : ''}`, blobs: sorted.slice(at, at + maxGroupBlobs) });
      }
      return;
    }
    if (direct.length > 0) split(direct, depth, prefix);
    for (const [segment, group] of [...children].sort(([a], [b]) => a < b ? -1 : 1)) split(group, depth + 1, prefix ? `${prefix}/${segment}` : segment);
  };
  split([...blobs], 0, '');
  return out;
}

const compareBlobs = (a: Blob, b: Blob): number => b.heuristic - a.heuristic || (a.path < b.path ? -1 : a.path > b.path ? 1 : 0);

const DIGEST_LIMITS = { maxBytes: 50_000_000, maxNodes: 2_000_000, maxDepth: 16 } as const;
const isObject = (value: unknown): value is Record<string, unknown> => value !== null && typeof value === 'object' && !Array.isArray(value);

export async function discoverAndSelect(
  sources: readonly GenerationSource[], readerQuestions: readonly string[], budget: DiscoveryBudget, ports: DiscoveryPorts, signal: AbortSignal = new AbortController().signal,
): Promise<DiscoveryResult> {
  if (!Number.isSafeInteger(budget.maxSelected) || budget.maxSelected < 1 || budget.maxSelected > PIPELINE_QUOTABLE_CAP
    || [budget.maxMapCalls, budget.maxExcerptChars, budget.claimsPerGroup, budget.maxReduceClaims].some(n => !Number.isSafeInteger(n) || n < 0)
    || !Number.isSafeInteger(budget.maxClaimChars) || budget.maxClaimChars < 1) throw new DiscoveryRefusal('invalid-budget');
  if ((ports.map !== undefined || ports.reduce !== undefined) && ports.receipt === undefined) throw new DiscoveryRefusal('model-ports-need-a-receipt-port');
  const blobs = candidateBlobs(sources);
  const groups = partitionSubsystems(blobs, budget.maxGroupBlobs);

  const byId = new Map(blobs.map(blob => [blob.blobId, blob]));
  const claims = new Map<string, DiscoveryClaim>();
  const unmapped: string[] = [];
  const receipts: DiscoveryReceipt[] = [];
  let mapCalls = 0, mapFailures = 0, refusedCalls = 0, reduceCalls = 0, reduceFailures = 0, dropped = 0, ordinal = 0;

  const aborted = new Promise<never>((_, reject) => {
    const stop = (): void => reject(new DiscoveryRefusal('cancelled'));
    if (signal.aborted) stop(); else signal.addEventListener('abort', stop, { once: true });
  });
  aborted.catch(() => undefined);
  const raced = <T>(job: Promise<T>): Promise<T> => Promise.race([job, aborted]);
  const emit = async (receipt: DiscoveryReceipt): Promise<void> => {
    receipts.push(receipt);
    try { await ports.receipt!(receipt); } catch { throw new DiscoveryRefusal('receipt-write-failed'); }
  };

  /** One provider call: ask, write a dispatching receipt, call, validate, write the outcome. */
  const providerCall = async <In, Raw, Valid extends { readonly usageUnits: number | null; readonly dropped: number; readonly reply: NonNullable<DiscoveryReceipt['reply']> }>(
    kind: 'map' | 'reduce', subsystem: string | undefined, input: In, itemCount: number, invoke: (input: In) => Promise<Raw>, validate: (raw: Raw) => Valid,
  ): Promise<Valid | undefined> => {
    if (signal.aborted) throw new DiscoveryRefusal('cancelled');
    const call: DiscoveryCall = { kind, ...(subsystem === undefined ? {} : { subsystem }), itemCount, requestDigest: digestCanonicalJson(input, DIGEST_LIMITS).digest };
    const shared = { kind, ordinal: ordinal++, ...(subsystem === undefined ? {} : { subsystem }), requestDigest: call.requestDigest, itemCount };
    let allowed = false;
    try { allowed = await raced(ports.permitted(call)) === true; } catch (error) { if (error instanceof DiscoveryRefusal) throw error; }
    if (!allowed) { refusedCalls++; await emit({ ...shared, outcome: 'refused', usageUnits: null, dropped: 0 }); return undefined; }
    await emit({ ...shared, outcome: 'dispatching', usageUnits: null, dropped: 0 });
    try {
      const valid = validate(await raced(invoke(input)));
      await emit({ ...shared, outcome: 'accepted', usageUnits: valid.usageUnits, dropped: valid.dropped, reply: valid.reply });
      return valid;
    } catch (error) {
      const detail = (error instanceof Error ? error.message : String(error)).slice(0, 200);
      if (error instanceof DiscoveryRefusal && error.reason === 'receipt-write-failed') throw error;
      await emit({ ...shared, outcome: 'failed', usageUnits: null, dropped: 0, detail });
      if (error instanceof DiscoveryRefusal) throw error;
      return undefined;
    }
  };

  // Larger and more promising subsystems are mapped first when calls run short.
  const mapOrder = [...groups].sort((a, b) => Math.max(...b.blobs.map(x => x.heuristic)) - Math.max(...a.blobs.map(x => x.heuristic)) || (a.name < b.name ? -1 : 1));
  for (const group of mapOrder) {
    if (ports.map === undefined || mapCalls >= budget.maxMapCalls) { unmapped.push(group.name); continue; }
    mapCalls++;
    const known = new Set(group.blobs.map(blob => blob.blobId));
    const input: MapInput = { subsystem: group.name, readerQuestions, items: group.blobs.map(blob => ({ blobId: blob.blobId, path: blob.path,
      excerpt: [...(blob.pieces[0]!.body ?? blob.pieces[0]!.spans[0]?.text ?? '')].slice(0, budget.maxExcerptChars).join('') })) };
    // The whole reply is validated before any claim reaches the ledger.
    const outcome = await providerCall('map', group.name, input, input.items.length, ports.map, (raw: unknown) => {
      if (!isObject(raw) || !Array.isArray(raw.claims)) throw new Error('invalid-map-reply');
      const accepted: DiscoveryClaim[] = [];
      let discarded = typeof raw.dropped === 'number' && Number.isSafeInteger(raw.dropped) && raw.dropped > 0 ? raw.dropped : 0;
      for (const claim of raw.claims as unknown[]) {
        if (!isObject(claim) || typeof claim.blobId !== 'string' || !known.has(claim.blobId) || typeof claim.relevance !== 'number' || !Number.isFinite(claim.relevance)
          || claim.relevance < 0 || claim.relevance > 10 || typeof claim.claim !== 'string' || claim.claim.length === 0) { discarded++; continue; }
        accepted.push({ blobId: claim.blobId, relevance: claim.relevance, claim: [...claim.claim].slice(0, budget.maxClaimChars).join('') });
      }
      return { usageUnits: typeof raw.usageUnits === 'number' ? raw.usageUnits : null, dropped: discarded, reply: { claims: accepted } };
    });
    if (outcome === undefined) { mapFailures++; unmapped.push(group.name); continue; }
    dropped += outcome.dropped;
    for (const claim of (outcome.reply as { claims: DiscoveryClaim[] }).claims) {
      const prior = claims.get(claim.blobId);
      if (prior === undefined || claim.relevance > prior.relevance) claims.set(claim.blobId, claim);
    }
  }

  const ledgerFor = (blob: Blob): (DiscoveryClaim & { path: string }) | undefined => { const c = claims.get(blob.blobId); return c && { ...c, path: blob.path }; };
  const rankedIds: string[] = [];
  let basis: DiscoveryReport['rankingBasis'] = claims.size > 0 ? 'model-map' : 'heuristic';
  if (ports.reduce !== undefined && claims.size > 0) {
    const perGroup = Math.max(1, Math.min(budget.claimsPerGroup, Math.floor(budget.maxReduceClaims / Math.max(1, groups.length))));
    const subsystems = groups.map(group => ({ subsystem: group.name, blobs: group.blobs.length,
      claims: group.blobs.map(ledgerFor).filter((c): c is DiscoveryClaim & { path: string } => c !== undefined)
        .sort((a, b) => b.relevance - a.relevance || (a.path < b.path ? -1 : 1)).slice(0, perGroup) })).filter(entry => entry.claims.length > 0);
    reduceCalls++;
    const input: ReduceInput = { readerQuestions, maxSelected: budget.maxSelected, subsystems };
    const outcome = await providerCall('reduce', undefined, input, subsystems.reduce((n, s) => n + s.claims.length, 0), ports.reduce, (raw: unknown) => {
      if (!isObject(raw) || !Array.isArray(raw.ranked) || raw.ranked.some(id => typeof id !== 'string')) throw new Error('invalid-reduce-reply');
      const ranked: string[] = [], seen = new Set<string>();
      let discarded = typeof raw.dropped === 'number' && Number.isSafeInteger(raw.dropped) && raw.dropped > 0 ? raw.dropped : 0;
      for (const id of raw.ranked as string[]) { if (!byId.has(id) || seen.has(id)) { discarded++; continue; } seen.add(id); ranked.push(id); }
      return { usageUnits: typeof raw.usageUnits === 'number' ? raw.usageUnits : null, dropped: discarded, reply: { ranked } };
    });
    if (outcome === undefined) reduceFailures++;
    else {
      dropped += outcome.dropped;
      rankedIds.push(...(outcome.reply as { ranked: string[] }).ranked);
      if (rankedIds.length > 0) basis = 'model-reduce';
    }
  }
  // Whatever the reduce did not rank follows by map relevance, then the prior.
  const ranked = new Set(rankedIds);
  const rest = blobs.filter(blob => !ranked.has(blob.blobId)).sort((a, b) =>
    (claims.get(b.blobId)?.relevance ?? -1) - (claims.get(a.blobId)?.relevance ?? -1) || compareBlobs(a, b));
  const order = [...rankedIds.map(id => byId.get(id)!), ...rest];

  const chosen = new Set<string>(), noFit = new Set<string>();
  let used = 0;
  for (const blob of order) {
    if (used + blob.pieces.length > budget.maxSelected) { noFit.add(blob.blobId); continue; }
    chosen.add(blob.blobId);
    used += blob.pieces.length;
  }
  const deferred: DiscoveryReport['deferred'][number][] = [];
  const emitted = new Set<string>();
  const out: GenerationSource[] = [];
  for (const source of sources) {
    if (source.exclusion.excluded || source.spans.length === 0) { out.push(source); continue; }
    const id = pieceBase(source);
    if (chosen.has(id)) { out.push(source); continue; }
    if (emitted.has(id)) continue;
    emitted.add(id);
    const { body: _body, segment: _segment, spans: _spans, ...bound } = source;
    out.push({ ...bound, sourceId: id, exclusion: { excluded: true, reason: DEFERRED_BY_BUDGET }, spans: [] });
    const pieces = byId.get(id)!.pieces.length;
    deferred.push({ blobId: id, path: source.path, detail: noFit.has(id) && pieces > 1 && used + pieces > budget.maxSelected
      ? `${pieces} quotable sources did not fit the remaining selection cap of ${budget.maxSelected}`
      : `ranked below the selection cut for a cap of ${budget.maxSelected} quotable sources` });
  }
  const alreadyExcluded = sources.filter(s => s.exclusion.excluded || s.spans.length === 0).length;
  return { receipts, sources: out, report: {
    boundary: deferred.length === 0 ? 'every candidate blob was selected' : 'deferred blobs were counted but not read into the account; the account does not claim whole-repository coverage',
    population: { sources: sources.length, alreadyExcluded, candidateBlobs: blobs.length }, subsystems: groups.length, mapCalls, mapFailures, refusedCalls,
    unmappedSubsystems: unmapped.sort(), reduceCalls, reduceFailures, rankingBasis: basis,
    basisNote: basis === 'heuristic' ? 'Ordered by a path-and-size prior only; no model reply was accepted.'
      : 'A model ranking is an Inferred claim. Blobs with no accepted map claim rank below every blob that has one.',
    droppedUnknownIds: dropped, selected: { blobs: chosen.size, sources: used }, deferred,
    ledger: order.filter(blob => chosen.has(blob.blobId)).map(ledgerFor).filter((c): c is DiscoveryClaim & { path: string } => c !== undefined) } };
}

/** Rebuilds a report from the population and the receipts alone, by replaying
 * each recorded reply. A call without an accepted receipt replays as a refusal
 * or a failure, exactly as it was recorded. */
export async function reportFromReceipts(
  sources: readonly GenerationSource[], readerQuestions: readonly string[], budget: DiscoveryBudget, receipts: readonly DiscoveryReceipt[],
): Promise<DiscoveryResult> {
  const last = new Map<string, DiscoveryReceipt>();
  for (const receipt of receipts) last.set(`${receipt.kind}:${receipt.subsystem ?? ''}`, receipt);
  const find = (kind: 'map' | 'reduce', subsystem?: string): DiscoveryReceipt | undefined => last.get(`${kind}:${subsystem ?? ''}`);
  return discoverAndSelect(sources, readerQuestions, budget, {
    permitted: async call => find(call.kind, call.subsystem)?.outcome !== 'refused' && find(call.kind, call.subsystem) !== undefined,
    map: async input => {
      const receipt = find('map', input.subsystem);
      if (receipt?.outcome !== 'accepted') throw new Error(`recorded ${receipt?.outcome ?? 'missing'}`);
      return { claims: (receipt.reply as { claims: DiscoveryClaim[] }).claims, usageUnits: receipt.usageUnits, dropped: receipt.dropped };
    },
    reduce: async () => {
      const receipt = find('reduce');
      if (receipt?.outcome !== 'accepted') throw new Error(`recorded ${receipt?.outcome ?? 'missing'}`);
      return { ranked: (receipt.reply as { ranked: string[] }).ranked, usageUnits: receipt.usageUnits, dropped: receipt.dropped };
    },
    receipt: async () => undefined,
  });
}
