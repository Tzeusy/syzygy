import { createHash } from 'node:crypto';

import { SOURCE_ID_MAX_LENGTH, SOURCE_ID_PATTERN, SOURCE_TEXT_MAX_LENGTH } from './provider-draft.js';

/** A project-neutral, evaluation-bound Git observation, including material
 * that was counted but cannot be quoted. Offsets are UTF-8 byte offsets. */
export interface GenerationSource {
  readonly sourceId: string;
  readonly repositoryId: string;
  readonly revision: string;
  readonly path: string;
  /** Null only when the named tree entry is missing or is not a blob. */
  readonly objectId: string | null;
  readonly evaluationId: string;
  readonly classificationBasis: 'body' | 'path-only';
  /** Present only on one contiguous piece of a blob too long to quote whole.
   * `start`/`end` are UTF-8 byte offsets into the full blob; `body` and span
   * offsets are relative to the piece, anchors use the blob offsets. */
  readonly segment?: { readonly index: number; readonly count: number; readonly start: number; readonly end: number; readonly blobBytes: number };
  readonly exclusion: { readonly excluded: false } | { readonly excluded: true; readonly reason: GenerationExclusionReason };
  /** Present only for an admitted body. Never sent to a provider except in
   * the inventory envelope or a later explicitly cited span. */
  readonly body?: string;
  readonly spans: readonly { readonly anchorId: string; readonly start: number; readonly end: number; readonly text: string }[];
}

export type GenerationSourceFailure =
  | 'invalid-source' | 'duplicate-source' | 'duplicate-anchor' | 'invalid-anchor'
  | 'unquotable-source' | 'body-mismatch' | 'object-mismatch' | 'source-too-long' | 'invalid-segments';

export class GenerationSourceError extends Error {
  constructor(readonly code: GenerationSourceFailure) {
    super(`Generation source rejected: ${code}`);
    this.name = 'GenerationSourceError';
  }
}

const fail = (code: GenerationSourceFailure): never => { throw new GenerationSourceError(code); };
const handle = new RegExp(SOURCE_ID_PATTERN, 'u');

/** An excluded row's id is `s-` plus 24 hex digits; the shape is checked here, the keying belongs to the emitter. */
const OPAQUE_SOURCE_ID = /^s-[0-9a-f]{24}$/u;

export const GENERATION_EXCLUSION_REASONS = [
  'oversize-source-excluded',
  'body-not-retained-for-generation',
  'deferred-by-budget',
  'empty-file',
  'binary-or-non-utf8',
  'denied-path',
  'resource-limit',
  'contains-nul',
  'not-utf-8',
  'active-content',
  'unknown-extraction-class',
  'parse-failure',
  'secret-detector-match',
  'not-in-manifest',
  'missing-at-revision',
  'not-a-regular-blob',
  'not-in-tree',
  'path-escapes-repository',
  'path-not-normalized',
  'object-id-mismatch',
  'git-read-failed',
  'unclassified-exclusion',
] as const;
/** The closed set above; `validateGenerationSources` refuses any other reason. */
export type GenerationExclusionReason = typeof GENERATION_EXCLUSION_REASONS[number];

export const isGenerationExclusionReason = (value: unknown): value is GenerationExclusionReason =>
  typeof value === 'string' && (GENERATION_EXCLUSION_REASONS as readonly string[]).includes(value);
const hexObjectId = /^(?:[0-9a-f]{40}|[0-9a-f]{64})$/u;

export function generationSourceIdentity(source: Pick<GenerationSource, 'repositoryId' | 'revision' | 'path'> & { readonly objectId: string }): string {
  return `${source.repositoryId}@${source.revision}:${source.path}#${source.objectId}`;
}

export function generationAnchorId(source: Pick<GenerationSource, 'repositoryId' | 'revision' | 'path'> & { readonly objectId: string }, start: number, end: number): string {
  return `${generationSourceIdentity(source)}:${start}-${end}`;
}

export function gitBlobObjectId(body: string, algorithm: 'sha1' | 'sha256' = 'sha1'): string {
  const bytes = Buffer.from(body, 'utf8');
  return createHash(algorithm).update(`blob ${bytes.length}\0`).update(bytes).digest('hex');
}

/** Validates one closed source population before any stage can dispatch. */
export function validateGenerationSources(value: readonly GenerationSource[]): readonly GenerationSource[] {
  if (value.length === 0) fail('invalid-source');
  const sourceKeys = new Set(['sourceId', 'repositoryId', 'revision', 'path', 'objectId', 'evaluationId', 'classificationBasis', 'segment', 'exclusion', 'body', 'spans']);
  const spanKeys = new Set(['anchorId', 'start', 'end', 'text']);
  const sourceIds = new Set<string>();
  const identities = new Set<string>();
  const anchorIds = new Set<string>();
  const blobs = new Map<string, { whole: boolean; pieces: { index: number; count: number; start: number; end: number; blobBytes: number }[] }>();
  for (const source of value) {
    if (source === null || typeof source !== 'object' || Object.keys(source).some(key => !sourceKeys.has(key))
      || (Object.hasOwn(source, 'body') && source.body === undefined)
      || source.exclusion === null || typeof source.exclusion !== 'object'
      || Object.keys(source.exclusion).some(key => !['excluded', 'reason'].includes(key))
      || (source.exclusion.excluded === false && Object.hasOwn(source.exclusion, 'reason'))) fail('invalid-source');
    if (!handle.test(source.sourceId) || source.sourceId.length > SOURCE_ID_MAX_LENGTH
      || !/^[A-Za-z0-9:_-]+$/u.test(source.repositoryId) || !source.evaluationId || !/^(?:[0-9a-f]{40}|[0-9a-f]{64})$/u.test(source.revision)
      || (source.objectId !== null && !hexObjectId.test(source.objectId)) || source.path.startsWith('/')
      || source.path.split('/').some(part => part === '' || part === '.' || part === '..') || source.path.includes('\0')
      || source.path.includes('\\') || !['body', 'path-only'].includes(source.classificationBasis)
      || typeof source.exclusion?.excluded !== 'boolean' || !Array.isArray(source.spans)) fail('invalid-source');
    const segment = source.segment;
    if (segment !== undefined && (segment === null || typeof segment !== 'object'
      || Object.keys(segment).length !== 5 || ['index', 'count', 'start', 'end', 'blobBytes'].some(key => !Number.isSafeInteger((segment as Record<string, unknown>)[key]))
      || segment.count < 2 || segment.index < 0 || segment.index >= segment.count || segment.start < 0 || segment.end <= segment.start
      || source.objectId === null || source.exclusion.excluded || source.classificationBasis !== 'body')) fail('invalid-source');
    const blobIdentity = source.objectId === null
      ? `${source.repositoryId}@${source.revision}:${source.path}#unavailable`
      : generationSourceIdentity({ ...source, objectId: source.objectId });
    const identity = segment === undefined ? blobIdentity : `${blobIdentity}[${segment.start}-${segment.end}]`;
    const blob = blobs.get(blobIdentity) ?? { whole: false, pieces: [] };
    if (segment === undefined) blob.whole = true; else blob.pieces.push(segment);
    blobs.set(blobIdentity, blob);
    if (sourceIds.has(source.sourceId) || identities.has(identity)) fail('duplicate-source');
    sourceIds.add(source.sourceId);
    identities.add(identity);
    if (source.objectId === null && !source.exclusion.excluded) fail('invalid-source');
    if (source.classificationBasis === 'path-only' || source.exclusion.excluded) {
      if (source.body !== undefined || source.spans.length !== 0) fail('unquotable-source');
      if (source.exclusion.excluded && (!isGenerationExclusionReason(source.exclusion.reason) || !OPAQUE_SOURCE_ID.test(source.sourceId))) fail('invalid-source');
      continue;
    }
    if (source.body === undefined && source.spans.length === 0) continue;
    const objectId = source.objectId;
    if (objectId === null) throw new GenerationSourceError('invalid-source');
    const body = source.body ?? (source.spans.length === 1 && source.spans[0]?.start === 0 ? source.spans[0].text : undefined);
    if (body === undefined) throw new GenerationSourceError('unquotable-source');
    const bytes = Buffer.from(body, 'utf8');
    if ([...body].length > SOURCE_TEXT_MAX_LENGTH) fail('source-too-long');
    // A piece cannot hash to its blob; its contiguity is checked below and the
    // reader (and verifySources) bind the whole blob.
    if (segment !== undefined) { if (bytes.length !== segment.end - segment.start) fail('body-mismatch'); }
    else if (gitBlobObjectId(body, objectId.length === 40 ? 'sha1' : 'sha256') !== objectId) fail('object-mismatch');
    const anchorBase = segment?.start ?? 0;
    for (const span of source.spans) {
      if (span === null || typeof span !== 'object' || Object.keys(span).some(key => !spanKeys.has(key))
        || typeof span.anchorId !== 'string' || typeof span.text !== 'string') fail('invalid-anchor');
      if (!Number.isSafeInteger(span.start) || !Number.isSafeInteger(span.end)
        || span.start < 0 || span.end <= span.start || span.end > bytes.length) fail('invalid-anchor');
      const slice = bytes.subarray(span.start, span.end);
      let decoded: string;
      try { decoded = new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(slice); }
      catch { throw new GenerationSourceError('invalid-anchor'); }
      if (decoded !== span.text) fail('body-mismatch');
      if (span.anchorId !== generationAnchorId({ ...source, objectId }, anchorBase + span.start, anchorBase + span.end)) fail('invalid-anchor');
      if (anchorIds.has(span.anchorId)) fail('duplicate-anchor');
      anchorIds.add(span.anchorId);
    }
  }
  for (const blob of blobs.values()) {
    if (blob.pieces.length === 0) continue;
    const pieces = [...blob.pieces].sort((a, b) => a.index - b.index);
    // The last piece must reach the blob's declared size, so a consistently
    // truncated tail cannot validate.
    if (blob.whole || pieces.some((piece, i) => piece.index !== i || piece.count !== pieces.length || piece.blobBytes !== pieces[0]!.blobBytes
      || piece.start !== (i === 0 ? 0 : pieces[i - 1]!.end)) || pieces.at(-1)!.end !== pieces[0]!.blobBytes) fail('invalid-segments');
  }
  return value;
}

export interface BodyPiece { readonly start: number; readonly end: number; readonly text: string }

/** Splits an over-long body into pieces of at most `maxChars` characters,
 * preferring the last line break in the final fifth of a piece and never
 * cutting inside a code point. Offsets are UTF-8 bytes into `body`. */
export function segmentBody(body: string, maxChars: number = SOURCE_TEXT_MAX_LENGTH): readonly BodyPiece[] {
  if (!Number.isSafeInteger(maxChars) || maxChars < 1) throw new GenerationSourceError('invalid-source');
  const chars = [...body];
  const pieces: BodyPiece[] = [];
  let at = 0, byte = 0;
  while (at < chars.length) {
    let stop = Math.min(chars.length, at + maxChars);
    if (stop < chars.length) {
      for (let i = stop; i > at + Math.floor(maxChars * 0.8); i--) if (chars[i - 1] === '\n') { stop = i; break; }
    }
    const text = chars.slice(at, stop).join('');
    const length = Buffer.byteLength(text, 'utf8');
    pieces.push({ start: byte, end: byte + length, text });
    byte += length;
    at = stop;
  }
  return pieces;
}

export interface BodySourceInput {
  readonly sourceId: string;
  readonly repositoryId: string;
  readonly revision: string;
  readonly path: string;
  readonly objectId: string;
  readonly evaluationId: string;
  readonly body: string;
  /** What to do with a body over the quotable limit; default `split`. */
  readonly oversize?: 'split' | 'exclude';
}

/** One verified blob body as sources: whole when it fits, otherwise
 * contiguous pieces (`<sourceId>-p1`...) or one excluded row with a reason.
 * The caller has already checked the body against `objectId`. */
export function generationSourcesForBody(input: BodySourceInput): readonly GenerationSource[] {
  const { body, sourceId, oversize = 'split', ...base } = input;
  const bytes = Buffer.byteLength(body, 'utf8');
  if ([...body].length <= SOURCE_TEXT_MAX_LENGTH) {
    return [{ ...base, sourceId, classificationBasis: 'body', exclusion: { excluded: false }, body,
      spans: [{ anchorId: generationAnchorId(base, 0, bytes), start: 0, end: bytes, text: body }] }];
  }
  if (oversize === 'exclude') {
    return [{ ...base, sourceId, classificationBasis: 'body', exclusion: { excluded: true, reason: 'oversize-source-excluded' }, spans: [] }];
  }
  const pieces = segmentBody(body);
  return pieces.map((piece, index) => ({ ...base, sourceId: `${sourceId}-p${index + 1}`, classificationBasis: 'body' as const,
    segment: { index, count: pieces.length, start: piece.start, end: piece.end, blobBytes: bytes }, exclusion: { excluded: false as const }, body: piece.text,
    spans: [{ anchorId: generationAnchorId(base, piece.start, piece.end), start: 0, end: piece.end - piece.start, text: piece.text }] }));
}

/** Only quotable source text crosses the provider boundary. The population
 * count remains available separately, including excluded and path-only rows. */
export function quotableGenerationSources(sources: readonly GenerationSource[]): readonly { readonly sourceId: string; readonly text: string }[] {
  validateGenerationSources(sources);
  return sources.flatMap(source => source.spans.length === 1 && source.spans[0]?.start === 0
    && source.spans[0]?.end === Buffer.byteLength(source.spans[0]?.text ?? '')
    ? [{ sourceId: source.sourceId, text: source.spans[0]!.text }] : []);
}
