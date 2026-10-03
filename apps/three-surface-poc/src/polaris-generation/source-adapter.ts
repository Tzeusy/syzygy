import { createHash } from 'node:crypto';

import { generationSourceIdentity, isGenerationExclusionReason, validateGenerationSources, type GenerationExclusionReason, type GenerationSource } from '@syzygy/polaris-generation-core';
import type { ClassificationRecord, PocModel } from '@syzygy/three-surface-poc-core';

import { sourceRouteHref } from '../polaris-source.js';

/** Maps a PWB withholding onto the closed generation set. The classifier's own
 * `unknownReason` is a free sentence and is never passed through: an excluded
 * record maps by its closed `exclusionReason` (a detector match with none is
 * `policy-excluded`), an unavailable one by its closed `reason`, and anything
 * outside the set fails closed to `unclassified-exclusion`. */
export function generationExclusionReason(record: ClassificationRecord): GenerationExclusionReason {
  const candidate = record.outcome === 'excluded' ? (record.exclusion.exclusionReason ?? 'policy-excluded')
    : record.outcome === 'unavailable' ? record.reason : 'unclassified-exclusion';
  return isGenerationExclusionReason(candidate) ? candidate : 'unclassified-exclusion';
}

/** Projects the already observed PWB source population without re-reading a
 * repository. PWB intentionally retains no source bodies after extraction;
 * its source rows are countable here but cannot be quoted by the generator. */
export function generationSourcesFromPocModel(model: PocModel): readonly GenerationSource[] {
  const shape = model.projectShape;
  if (shape.kind !== 'observed') return [];
  const sources = shape.sources.map((source): GenerationSource => {
    const sourceId = `s-${createHash('sha256').update(source.identity).digest('hex').slice(0, 24)}`;
    const objectId = source.anchor.kind === 'blob' ? source.anchor.objectId : null;
    const exclusion: GenerationSource['exclusion'] = source.record.outcome === 'excluded'
      ? { excluded: true as const, reason: generationExclusionReason(source.record) }
      : source.record.outcome === 'unavailable'
        ? { excluded: true as const, reason: generationExclusionReason(source.record) }
        : source.record.basis === 'body'
          ? { excluded: true as const, reason: 'body-not-retained-for-generation' }
          : { excluded: false as const };
    return {
      sourceId, repositoryId: shape.identity.repositoryId, revision: shape.identity.revision,
      path: source.path, objectId, evaluationId: source.claim.evaluationId,
      classificationBasis: source.record.outcome === 'classified' ? source.record.basis : 'body',
      exclusion, spans: [],
    };
  });
  return validateGenerationSources(sources);
}

/** Reuse the existing exact-source route encoding; only a blob-backed source
 * from the current PWB population may be offered a route. */
export function generationSourceRoute(source: GenerationSource, mountPrefix = ''): string | undefined {
  if (source.objectId === null || source.exclusion.excluded || source.spans.length === 0) return undefined;
  return sourceRouteHref(mountPrefix, generationSourceIdentity({ ...source, objectId: source.objectId }));
}
