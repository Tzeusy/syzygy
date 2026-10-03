/**
 * The provider envelope for hierarchical discovery's map and reduce calls
 * (REQ-polaris-generation-030). Discovery takes structured inputs and expects
 * claims or a ranking back; this module builds what a generate port sends for
 * each call and parses what comes back. It never calls a provider and authors
 * no instruction text: the system prompt is `promptForStage(stage)` and the
 * reply schema is `stageSchema(stage)`, for the stages `discovery-map` and
 * `discovery-reduce`, so the two symbols the instruction-text rule names stay
 * the only source of it.
 *
 * The envelope has the pipeline stage envelope's five fields (promptVersion,
 * system, responseSchemaVersion, responseSchema, inputs). `inputs` is rebuilt
 * field by field from the request, so a caller's extra property never crosses
 * the boundary. The schema is fixed; which blob ids a reply may name is the
 * call's own business, checked by `validateDiscoveryReply`: a map reply only
 * its input's blob ids, a reduce reply only the blob ids its input's claims
 * name, at most `maxSelected`. Any breach refuses the whole reply.
 *
 * The request shapes match discovery.ts's `MapInput` and `ReduceInput`
 * structurally, so a discovery port can pass its input straight through.
 */

import { encodeCanonicalJson, type CanonicalJsonLimits } from './canonical-json.js';
import { parseBoundedJson } from './parse-json.js';
import { promptForStage, type DiscoveryStage } from './prompts.js';
import { stageSchema, validateDiscoveryReply } from './provider-draft.js';

export interface DiscoveryMapRequest {
  readonly subsystem: string;
  readonly readerQuestions: readonly string[];
  readonly items: readonly { readonly blobId: string; readonly path: string; readonly excerpt: string }[];
}
export interface DiscoveryReduceRequest {
  readonly readerQuestions: readonly string[];
  readonly maxSelected: number;
  readonly subsystems: readonly {
    readonly subsystem: string;
    readonly blobs: number;
    readonly claims: readonly { readonly blobId: string; readonly path: string; readonly claim: string; readonly relevance: number }[];
  }[];
}
export interface DiscoveryReplyClaim { readonly blobId: string; readonly claim: string; readonly relevance: number }
export interface DiscoveryEnvelope {
  readonly promptVersion: string;
  readonly system: string;
  readonly responseSchemaVersion: string;
  readonly responseSchema: Readonly<Record<string, unknown>>;
  readonly inputs: Readonly<Record<string, unknown>>;
}

export type DiscoveryProviderFailure = 'invalid-map-request' | 'invalid-reduce-request' | 'invalid-map-reply' | 'invalid-reduce-reply';
/** Diagnostics carry no request or reply content. */
export class DiscoveryProviderError extends Error {
  constructor(readonly code: DiscoveryProviderFailure) {
    super(`Discovery provider envelope refused: ${code}`);
    this.name = 'DiscoveryProviderError';
  }
}

/** Bounds for an encoded envelope and a parsed reply. */
export const DISCOVERY_JSON_LIMITS: CanonicalJsonLimits = { maxBytes: 4_000_000, maxNodes: 100_000, maxDepth: 16 };

const isRecord = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === 'object' && !Array.isArray(value)
  && [Object.prototype, null].includes(Object.getPrototypeOf(value) as object | null);
const isText = (value: unknown): value is string => typeof value === 'string' && value.length > 0;
const isQuestions = (value: unknown): value is string[] => Array.isArray(value) && value.length > 0 && value.every(isText);
const distinct = (values: readonly string[]): boolean => new Set(values).size === values.length;

function mapCandidates(request: DiscoveryMapRequest): string[] {
  const fail = (): never => { throw new DiscoveryProviderError('invalid-map-request'); };
  if (!isRecord(request) || !isText(request.subsystem) || !isQuestions(request.readerQuestions) || !Array.isArray(request.items) || request.items.length === 0) fail();
  for (const item of request.items) if (!isRecord(item) || !isText(item.blobId) || !isText(item.path) || typeof item.excerpt !== 'string') fail();
  const ids = request.items.map(item => item.blobId);
  if (!distinct(ids)) fail();
  return ids;
}

function reduceCandidates(request: DiscoveryReduceRequest): string[] {
  const fail = (): never => { throw new DiscoveryProviderError('invalid-reduce-request'); };
  if (!isRecord(request) || !isQuestions(request.readerQuestions) || !Number.isSafeInteger(request.maxSelected) || request.maxSelected < 1
    || !Array.isArray(request.subsystems)) fail();
  for (const entry of request.subsystems) {
    if (!isRecord(entry) || !isText(entry.subsystem) || !Number.isSafeInteger(entry.blobs) || entry.blobs < 0 || !Array.isArray(entry.claims)) fail();
    for (const claim of entry.claims) {
      if (!isRecord(claim) || !isText(claim.blobId) || !isText(claim.path) || typeof claim.claim !== 'string'
        || typeof claim.relevance !== 'number' || !Number.isFinite(claim.relevance)) fail();
    }
  }
  const ids = request.subsystems.flatMap(entry => entry.claims.map(claim => claim.blobId));
  if (ids.length === 0 || !distinct(ids)) fail();
  return ids;
}

function envelopeFor(stage: DiscoveryStage, inputs: Record<string, unknown>): { readonly envelope: DiscoveryEnvelope; readonly input: string } {
  const prompt = promptForStage(stage);
  const schema = stageSchema(stage);
  const envelope: DiscoveryEnvelope = { promptVersion: prompt.version, system: prompt.system, responseSchemaVersion: schema.version, responseSchema: schema.schema, inputs };
  return { envelope, input: encodeCanonicalJson(envelope, DISCOVERY_JSON_LIMITS) };
}

/** The envelope a map call sends, and its canonical encoding (the user message). */
export function discoveryMapEnvelope(request: DiscoveryMapRequest): { readonly envelope: DiscoveryEnvelope; readonly input: string } {
  mapCandidates(request);
  return envelopeFor('discovery-map', {
    subsystem: request.subsystem, readerQuestions: [...request.readerQuestions],
    items: request.items.map(item => ({ blobId: item.blobId, path: item.path, excerpt: item.excerpt })),
  });
}

/** The envelope a reduce call sends, and its canonical encoding (the user message). */
export function discoveryReduceEnvelope(request: DiscoveryReduceRequest): { readonly envelope: DiscoveryEnvelope; readonly input: string } {
  reduceCandidates(request);
  return envelopeFor('discovery-reduce', {
    readerQuestions: [...request.readerQuestions], maxSelected: request.maxSelected,
    subsystems: request.subsystems.map(entry => ({ subsystem: entry.subsystem, blobs: entry.blobs,
      claims: entry.claims.map(claim => ({ blobId: claim.blobId, path: claim.path, claim: claim.claim, relevance: claim.relevance })) })),
  });
}

/** One reply body, parsed and validated against its own call; any breach refuses all of it. */
function parseReply(stage: DiscoveryStage, body: string, call: { readonly candidateIds: readonly string[]; readonly maxSelected?: number }, code: DiscoveryProviderFailure): unknown {
  try { return validateDiscoveryReply(stage, parseBoundedJson(body, DISCOVERY_JSON_LIMITS), call); }
  catch { throw new DiscoveryProviderError(code); }
}

/**
 * Parses a map reply body against its request: exactly `{claims: [...]}`, each
 * claim exactly `{blobId, claim, relevance}`, a blobId from the request's items
 * at most once, a claim of 1..400 code points and a relevance in 0..10.
 */
export function parseDiscoveryMapReply(request: DiscoveryMapRequest, body: string): { readonly claims: readonly DiscoveryReplyClaim[] } {
  const value = parseReply('discovery-map', body, { candidateIds: mapCandidates(request) }, 'invalid-map-reply') as { claims: DiscoveryReplyClaim[] };
  return { claims: value.claims.map(claim => ({ blobId: claim.blobId, claim: claim.claim, relevance: claim.relevance })) };
}

/**
 * Parses a reduce reply body against its request: exactly `{ranked: [...]}`,
 * each id one the request's claims name, at most once, at most `maxSelected`.
 */
export function parseDiscoveryReduceReply(request: DiscoveryReduceRequest, body: string): { readonly ranked: readonly string[] } {
  const value = parseReply('discovery-reduce', body, { candidateIds: reduceCandidates(request), maxSelected: request.maxSelected }, 'invalid-reduce-reply') as { ranked: string[] };
  return { ranked: [...value.ranked] };
}
