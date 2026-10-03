import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { GENERATION_EXCLUSION_REASONS, generationAnchorId, gitBlobObjectId, type GenerationSource } from '@syzygy/polaris-generation-core';
import { EXCLUSION_REASONS, UNAVAILABLE_REASONS, type ClassificationRecord } from '@syzygy/three-surface-poc-core';

import { buildFixtureModel } from '../test-model-fixture.js';
import { ADMITTING_AUTHORITY, projectShapeFixtureGit } from '../test-project-shape-fixture.js';
import { generationExclusionReason, generationSourceRoute, generationSourcesFromPocModel } from './source-adapter.js';

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
    const { body: _body, ...withoutBody } = source;
    expect(generationSourceRoute({ ...withoutBody, exclusion: { excluded: true, reason: 'active-content' }, spans: [] })).toBeUndefined();
  });

  it('maps every closed PWB withholding reason onto the generation set, never passing a free sentence through', () => {
    const unknown = { failureState: 'secretMatchedOrUnclassifiable', degradationState: 'd', unknownReason: 'A free sentence the classifier wrote.' } as never;
    const exclusion = (exclusionReason?: string) => ({ redactionClass: 'secret', repositoryRelativePath: 'a', policyId: 'p', policyVersion: '1', ...(exclusionReason === undefined ? {} : { exclusionReason }) });
    const excluded = (exclusionReason?: string) => ({ path: 'a', outcome: 'excluded', exclusion: exclusion(exclusionReason), unknown }) as unknown as ClassificationRecord;
    const unavailable = (reason: string) => ({ path: 'a', outcome: 'unavailable', reason, unknown }) as unknown as ClassificationRecord;
    for (const reason of EXCLUSION_REASONS) expect(generationExclusionReason(excluded(reason))).toBe(reason);
    for (const reason of UNAVAILABLE_REASONS) expect(generationExclusionReason(unavailable(reason))).toBe(reason);
    expect(generationExclusionReason(excluded())).toBe('policy-excluded');
    expect(generationExclusionReason(excluded('a-new-reason'))).toBe('unclassified-exclusion');
    expect(generationExclusionReason(unavailable('a-new-reason'))).toBe('unclassified-exclusion');
    for (const reason of [...EXCLUSION_REASONS, ...UNAVAILABLE_REASONS, 'body-not-retained-for-generation', 'oversize-source-excluded']) expect(GENERATION_EXCLUSION_REASONS).toContain(reason);
  });

  it('projects only listed reasons and opaque ids for every excluded source of the observed population', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    const excluded = generationSourcesFromPocModel(model).filter(source => source.exclusion.excluded);
    expect(excluded.length).toBeGreaterThan(0);
    for (const source of excluded) {
      expect(GENERATION_EXCLUSION_REASONS).toContain((source.exclusion as { reason: string }).reason);
      expect(source.sourceId).toMatch(/^s-[0-9a-f]{24}$/u);
      expect(source.sourceId).not.toContain(source.path);
    }
  });

  it('projects each record outcome with a listed reason through the population projection', () => {
    const unknown = { failureState: 'secretMatchedOrUnclassifiable', degradationState: 'd', unknownReason: 'A free sentence the classifier wrote.' };
    const row = (path: string, record: object, anchor: object = { kind: 'blob', objectId: 'a'.repeat(40) }) => ({ identity: `id:${path}`, path, anchor, claim: { evaluationId: 'e' }, record: { path, ...record } });
    const model = { projectShape: { kind: 'observed', identity: { repositoryId: 'repository:fixture', revision: 'b'.repeat(40) }, sources: [
      row('a.md', { outcome: 'excluded', exclusion: { exclusionReason: 'active-content' }, unknown }),
      row('b.md', { outcome: 'excluded', exclusion: {}, unknown }),
      row('c.md', { outcome: 'unavailable', reason: 'not-in-tree', unknown }, { kind: 'none' }),
      row('d.md', { outcome: 'classified', basis: 'body' }),
      row('e.md', { outcome: 'classified', basis: 'path-only' }),
    ] } } as unknown as Parameters<typeof generationSourcesFromPocModel>[0];
    const byPath = new Map(generationSourcesFromPocModel(model).map(source => [source.path, source.exclusion]));
    expect(byPath.get('a.md')).toEqual({ excluded: true, reason: 'active-content' });
    expect(byPath.get('b.md')).toEqual({ excluded: true, reason: 'policy-excluded' });
    expect(byPath.get('c.md')).toEqual({ excluded: true, reason: 'not-in-tree' });
    expect(byPath.get('d.md')).toEqual({ excluded: true, reason: 'body-not-retained-for-generation' });
    expect(byPath.get('e.md')).toEqual({ excluded: false });
  });
});
