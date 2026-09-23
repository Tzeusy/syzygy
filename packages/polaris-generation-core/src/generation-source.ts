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
  readonly exclusion: { readonly excluded: false } | { readonly excluded: true; readonly reason: string };
  /** Present only for an admitted body. Never sent to a provider except in
   * the inventory envelope or a later explicitly cited span. */
  readonly body?: string;
  readonly spans: readonly { readonly anchorId: string; readonly start: number; readonly end: number; readonly text: string }[];
}

export type GenerationSourceFailure =
  | 'invalid-source' | 'duplicate-source' | 'duplicate-anchor' | 'invalid-anchor'
  | 'unquotable-source' | 'body-mismatch' | 'object-mismatch' | 'source-too-long';

export class GenerationSourceError extends Error {
  constructor(readonly code: GenerationSourceFailure) {
    super(`Generation source rejected: ${code}`);
    this.name = 'GenerationSourceError';
  }
}

const fail = (code: GenerationSourceFailure): never => { throw new GenerationSourceError(code); };
const handle = new RegExp(SOURCE_ID_PATTERN, 'u');
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
  const sourceKeys = new Set(['sourceId', 'repositoryId', 'revision', 'path', 'objectId', 'evaluationId', 'classificationBasis', 'exclusion', 'body', 'spans']);
  const spanKeys = new Set(['anchorId', 'start', 'end', 'text']);
  const sourceIds = new Set<string>();
  const identities = new Set<string>();
  const anchorIds = new Set<string>();
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
    const identity = source.objectId === null
      ? `${source.repositoryId}@${source.revision}:${source.path}#unavailable`
      : generationSourceIdentity({ ...source, objectId: source.objectId });
    if (sourceIds.has(source.sourceId) || identities.has(identity)) fail('duplicate-source');
    sourceIds.add(source.sourceId);
    identities.add(identity);
    if (source.objectId === null && !source.exclusion.excluded) fail('invalid-source');
    if (source.classificationBasis === 'path-only' || source.exclusion.excluded) {
      if (source.body !== undefined || source.spans.length !== 0) fail('unquotable-source');
      if (source.exclusion.excluded && !source.exclusion.reason) fail('invalid-source');
      continue;
    }
    if (source.body === undefined && source.spans.length === 0) continue;
    const objectId = source.objectId;
    if (objectId === null) throw new GenerationSourceError('invalid-source');
    const body = source.body ?? (source.spans.length === 1 && source.spans[0]?.start === 0 ? source.spans[0].text : undefined);
    if (body === undefined) throw new GenerationSourceError('unquotable-source');
    const bytes = Buffer.from(body, 'utf8');
    if ([...body].length > SOURCE_TEXT_MAX_LENGTH) fail('source-too-long');
    if (gitBlobObjectId(body, objectId.length === 40 ? 'sha1' : 'sha256') !== objectId) fail('object-mismatch');
    for (const span of source.spans) {
      if (span === null || typeof span !== 'object' || Object.keys(span).some(key => !spanKeys.has(key))
        || typeof span.anchorId !== 'string' || typeof span.text !== 'string') fail('invalid-anchor');
      if (!Number.isSafeInteger(span.start) || !Number.isSafeInteger(span.end)
        || span.start < 0 || span.end <= span.start || span.end > bytes.length) fail('invalid-anchor');
      const slice = bytes.subarray(span.start, span.end);
      let decoded: string;
      try { decoded = new TextDecoder('utf-8', { fatal: true }).decode(slice); }
      catch { throw new GenerationSourceError('invalid-anchor'); }
      if (decoded !== span.text) fail('body-mismatch');
      if (span.anchorId !== generationAnchorId({ ...source, objectId }, span.start, span.end)) fail('invalid-anchor');
      if (anchorIds.has(span.anchorId)) fail('duplicate-anchor');
      anchorIds.add(span.anchorId);
    }
  }
  return value;
}

/** Only quotable source text crosses the provider boundary. The population
 * count remains available separately, including excluded and path-only rows. */
export function quotableGenerationSources(sources: readonly GenerationSource[]): readonly { readonly sourceId: string; readonly text: string }[] {
  validateGenerationSources(sources);
  return sources.flatMap(source => source.spans.length === 1 && source.spans[0]?.start === 0
    && source.spans[0]?.end === Buffer.byteLength(source.spans[0]?.text ?? '')
    ? [{ sourceId: source.sourceId, text: source.spans[0]!.text }] : []);
}
