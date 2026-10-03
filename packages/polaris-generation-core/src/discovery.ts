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
}

export const DEFAULT_DISCOVERY_BUDGET: DiscoveryBudget = {
  maxSelected: PIPELINE_QUOTABLE_CAP, maxMapCalls: 40, maxExcerptChars: 1500, maxGroupBlobs: 40, claimsPerGroup: 8, maxReduceClaims: 400,
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
export interface DiscoveryPorts {
  /** The same egress decision the pipeline uses; false means no call at all. */
  readonly permitted: () => Promise<boolean>;
  readonly map?: (input: MapInput) => Promise<readonly DiscoveryClaim[]>;
  /** Blob ids in priority order; unknown ids are dropped and counted. */
  readonly reduce?: (input: ReduceInput) => Promise<readonly string[]>;
}

export interface DiscoveryReport {
  readonly boundary: string;
  readonly population: { readonly sources: number; readonly alreadyExcluded: number; readonly candidateBlobs: number };
  readonly subsystems: number;
  readonly mapCalls: number;
  readonly mapFailures: number;
  readonly unmappedSubsystems: readonly string[];
  readonly reduceCalls: number;
  readonly rankingBasis: 'model-reduce' | 'model-map' | 'heuristic';
  readonly droppedUnknownIds: number;
  readonly selected: { readonly blobs: number; readonly sources: number };
  readonly deferred: readonly { readonly blobId: string; readonly path: string; readonly detail: string }[];
  readonly ledger: readonly (DiscoveryClaim & { readonly path: string })[];
}
export interface DiscoveryResult { readonly sources: readonly GenerationSource[]; readonly report: DiscoveryReport }

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

export async function discoverAndSelect(
  sources: readonly GenerationSource[], readerQuestions: readonly string[], budget: DiscoveryBudget, ports: DiscoveryPorts, signal: AbortSignal = new AbortController().signal,
): Promise<DiscoveryResult> {
  if (!Number.isSafeInteger(budget.maxSelected) || budget.maxSelected < 1 || budget.maxSelected > PIPELINE_QUOTABLE_CAP
    || [budget.maxMapCalls, budget.maxExcerptChars, budget.claimsPerGroup, budget.maxReduceClaims].some(n => !Number.isSafeInteger(n) || n < 0)) throw new DiscoveryRefusal('invalid-budget');
  const blobs = candidateBlobs(sources);
  const groups = partitionSubsystems(blobs, budget.maxGroupBlobs);
  const usesModel = ports.map !== undefined || ports.reduce !== undefined;
  if (usesModel && !await ports.permitted()) throw new DiscoveryRefusal('egress-not-permitted');

  const byId = new Map(blobs.map(blob => [blob.blobId, blob]));
  const claims = new Map<string, DiscoveryClaim>();
  const unmapped: string[] = [];
  let mapCalls = 0, mapFailures = 0, reduceCalls = 0, dropped = 0;
  // Larger and more promising subsystems are mapped first when calls run short.
  const mapOrder = [...groups].sort((a, b) => Math.max(...b.blobs.map(x => x.heuristic)) - Math.max(...a.blobs.map(x => x.heuristic)) || (a.name < b.name ? -1 : 1));
  for (const group of mapOrder) {
    if (ports.map === undefined || mapCalls >= budget.maxMapCalls) { unmapped.push(group.name); continue; }
    if (signal.aborted) throw new DiscoveryRefusal('cancelled');
    mapCalls++;
    try {
      const reply = await ports.map({ subsystem: group.name, readerQuestions, items: group.blobs.map(blob => ({ blobId: blob.blobId, path: blob.path,
        excerpt: [...(blob.pieces[0]!.body ?? blob.pieces[0]!.spans[0]?.text ?? '')].slice(0, budget.maxExcerptChars).join('') })) });
      for (const claim of reply) {
        const known = group.blobs.some(blob => blob.blobId === claim.blobId);
        if (!known || !Number.isFinite(claim.relevance) || claim.relevance < 0 || claim.relevance > 10 || typeof claim.claim !== 'string' || claim.claim.length === 0) { dropped++; continue; }
        const prior = claims.get(claim.blobId);
        if (prior === undefined || claim.relevance > prior.relevance) claims.set(claim.blobId, claim);
      }
    } catch { mapFailures++; unmapped.push(group.name); }
  }

  const ledgerFor = (blob: Blob): (DiscoveryClaim & { path: string }) | undefined => { const c = claims.get(blob.blobId); return c && { ...c, path: blob.path }; };
  let rankedIds: string[] = [];
  let basis: DiscoveryReport['rankingBasis'] = 'heuristic';
  if (ports.reduce !== undefined && claims.size > 0 && !signal.aborted) {
    const perGroup = Math.max(1, Math.min(budget.claimsPerGroup, Math.floor(budget.maxReduceClaims / Math.max(1, groups.length))));
    const subsystems = groups.map(group => ({ subsystem: group.name, blobs: group.blobs.length,
      claims: group.blobs.map(ledgerFor).filter((c): c is DiscoveryClaim & { path: string } => c !== undefined)
        .sort((a, b) => b.relevance - a.relevance || (a.path < b.path ? -1 : 1)).slice(0, perGroup) })).filter(entry => entry.claims.length > 0);
    reduceCalls++;
    const reply = await ports.reduce({ readerQuestions, maxSelected: budget.maxSelected, subsystems });
    const seen = new Set<string>();
    for (const id of reply) { if (!byId.has(id) || seen.has(id)) { dropped++; continue; } seen.add(id); rankedIds.push(id); }
    basis = rankedIds.length > 0 ? 'model-reduce' : 'model-map';
  } else if (claims.size > 0) basis = 'model-map';
  // Whatever the reduce did not rank follows by map relevance, then the prior.
  const rest = blobs.filter(blob => !rankedIds.includes(blob.blobId)).sort((a, b) =>
    (claims.get(b.blobId)?.relevance ?? -1) - (claims.get(a.blobId)?.relevance ?? -1) || compareBlobs(a, b));
  const order = [...rankedIds.map(id => byId.get(id)!), ...rest];

  const chosen = new Set<string>();
  let used = 0;
  for (const blob of order) {
    if (used + blob.pieces.length > budget.maxSelected) continue;
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
    deferred.push({ blobId: id, path: source.path, detail: `${byId.get(id)!.pieces.length} quotable source(s) did not fit the selection cap of ${budget.maxSelected}` });
  }
  const alreadyExcluded = sources.filter(s => s.exclusion.excluded || s.spans.length === 0).length;
  return { sources: out, report: {
    boundary: deferred.length === 0 && unmapped.length === 0 ? 'every candidate file was selected' : 'deferred files were counted but not read into the account; the account does not claim whole-repository coverage',
    population: { sources: sources.length, alreadyExcluded, candidateBlobs: blobs.length }, subsystems: groups.length, mapCalls, mapFailures,
    unmappedSubsystems: unmapped.sort(), reduceCalls, rankingBasis: basis, droppedUnknownIds: dropped,
    selected: { blobs: chosen.size, sources: used }, deferred,
    ledger: order.filter(blob => chosen.has(blob.blobId)).map(ledgerFor).filter((c): c is DiscoveryClaim & { path: string } => c !== undefined) } };
}
