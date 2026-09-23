import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { generationAnchorId, gitBlobObjectId, type GenerationSource } from '@syzygy/polaris-generation-core';

import { buildFixtureModel } from '../test-model-fixture.js';
import { ADMITTING_AUTHORITY, projectShapeFixtureGit } from '../test-project-shape-fixture.js';
import { generationSourceRoute, generationSourcesFromPocModel } from './source-adapter.js';

const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });

describe('PWB-to-generator projection', () => {
  it('retains every observed source identity but never manufactures a body or anchor from the PWB model', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    if (model.projectShape.kind !== 'observed') throw new Error('shape not observed');
    const projected = generationSourcesFromPocModel(model);
    expect(projected).toHaveLength(model.projectShape.sources.length);
    expect(projected.every(source => source.spans.length === 0 && source.body === undefined)).toBe(true);
    const pathOnly = model.projectShape.sources.find(source => source.record.outcome === 'classified' && source.record.basis === 'path-only');
    expect(pathOnly).toBeDefined();
    expect(projected.find(source => source.path === pathOnly?.path)?.classificationBasis).toBe('path-only');
    expect(projected.every(source => generationSourceRoute(source) === undefined)).toBe(true);
  });

  it('uses the existing source route encoding for a blob-backed, admitted anchor', () => {
    const body = 'One declared source.';
    const base = { repositoryId: 'repository:fixture', revision: 'a'.repeat(40), path: 'intent/one.md', objectId: gitBlobObjectId(body) };
    const source: GenerationSource = { ...base, sourceId: 'one', evaluationId: 'evaluation:fixture', classificationBasis: 'body', exclusion: { excluded: false }, body,
      spans: [{ anchorId: generationAnchorId(base, 0, Buffer.byteLength(body)), start: 0, end: Buffer.byteLength(body), text: body }] };
    expect(generationSourceRoute(source)).toBe(`/polaris/source?identity=repository%3Afixture%40${'a'.repeat(40)}%3Aintent%2Fone.md%23${base.objectId}`);
    expect(generationSourceRoute(source, '/butlers-syzygy')).toBe(`/butlers-syzygy/polaris/source?identity=repository%3Afixture%40${'a'.repeat(40)}%3Aintent%2Fone.md%23${base.objectId}`);
    expect(generationSourceRoute({ ...source, exclusion: { excluded: true, reason: 'excluded-content' }, body: undefined, spans: [] })).toBeUndefined();
  });
});
