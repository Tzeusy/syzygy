import { generationAnchorId, gitBlobObjectId, type GenerationSource } from '@syzygy/polaris-generation-core';

/** Fixture-only source construction. No project read or provider authority. */
export function syntheticGenerationSource(projectId: string, revision: string, sourceId: string, body: string): GenerationSource {
  const base = { repositoryId: `synthetic:${projectId}`, revision, path: `synthetic/${sourceId}.md`, objectId: gitBlobObjectId(body) };
  const end = Buffer.byteLength(body);
  return { ...base, sourceId, evaluationId: `synthetic-evaluation:${projectId}:${revision}`,
    classificationBasis: 'body', exclusion: { excluded: false }, body,
    spans: [{ anchorId: generationAnchorId(base, 0, end), start: 0, end, text: body }] };
}
