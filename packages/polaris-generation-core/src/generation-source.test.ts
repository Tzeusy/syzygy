import { describe, expect, it } from 'vitest';

import { generationAnchorId, generationSourceIdentity, gitBlobObjectId, quotableGenerationSources, validateGenerationSources, type GenerationSource } from './generation-source.js';

const body = 'A supported purpose.\n';
const base = { repositoryId: 'repository:fixture', revision: 'a'.repeat(40), path: 'intent/purpose.md', objectId: gitBlobObjectId(body) };
const source = (): GenerationSource => ({
  ...base, sourceId: 'purpose', evaluationId: 'evaluation:fixture', classificationBasis: 'body', exclusion: { excluded: false }, body,
  spans: [{ anchorId: generationAnchorId(base, 0, Buffer.byteLength(body)), start: 0, end: Buffer.byteLength(body), text: body }],
});

describe('evaluation-bound generation sources', () => {
  it('keeps source and anchor identities stable under source reorder', () => {
    const first = source();
    const secondBody = 'Another declaration.\n';
    const secondBase = { ...base, path: 'intent/other.md', objectId: gitBlobObjectId(secondBody) };
    const second: GenerationSource = { ...first, ...secondBase, sourceId: 'other', body: secondBody,
      spans: [{ anchorId: generationAnchorId(secondBase, 0, Buffer.byteLength(secondBody)), start: 0, end: Buffer.byteLength(secondBody), text: secondBody }] };
    expect(validateGenerationSources([first, second])).toHaveLength(2);
    expect(validateGenerationSources([second, first]).map(entry => generationSourceIdentity({ ...entry, objectId: entry.objectId as string })).sort())
      .toEqual([generationSourceIdentity(base), generationSourceIdentity(secondBase)].sort());
    expect(quotableGenerationSources([first, second])).toEqual([{ sourceId: 'purpose', text: body }, { sourceId: 'other', text: secondBody }]);
  });

  it('counts path-only, excluded and unavailable sources while withholding their bytes and anchors', () => {
    const quoted = source();
    const { body: _body, ...withoutBody } = quoted;
    const pathOnly: GenerationSource = { ...withoutBody, sourceId: 'path-only', path: 'intent/path-only.md', classificationBasis: 'path-only', spans: [] };
    const excluded: GenerationSource = { ...withoutBody, sourceId: 'excluded', path: 'intent/secret.md', exclusion: { excluded: true, reason: 'excluded-content' }, spans: [] };
    const unavailable: GenerationSource = { ...withoutBody, sourceId: 'unavailable', path: 'intent/missing.md', objectId: null, exclusion: { excluded: true, reason: 'source-unavailable' }, spans: [] };
    const population = [quoted, pathOnly, excluded, unavailable];
    expect(validateGenerationSources(population)).toHaveLength(4);
    expect(quotableGenerationSources(population)).toEqual([{ sourceId: 'purpose', text: body }]);
    expect(() => validateGenerationSources([{ ...pathOnly, spans: quoted.spans }])).toThrow('unquotable-source');
    expect(() => validateGenerationSources([{ ...excluded, body }])).toThrow('unquotable-source');
    expect(() => validateGenerationSources([{ ...quoted, extra: 'unreviewed' } as GenerationSource])).toThrow('invalid-source');
  });

  it('rejects forged object binding, offset drift, duplicate anchors and unknown-byte spans', () => {
    const valid = source();
    expect(() => validateGenerationSources([{ ...valid, objectId: 'b'.repeat(40) }])).toThrow('object-mismatch');
    expect(() => validateGenerationSources([{ ...valid, spans: [{ ...valid.spans[0]!, end: 2 }] }])).toThrow('body-mismatch');
    expect(() => validateGenerationSources([{ ...valid, spans: [valid.spans[0]!, valid.spans[0]!] }])).toThrow('duplicate-anchor');
    expect(() => validateGenerationSources([{ ...valid, spans: [{ ...valid.spans[0]!, anchorId: 'unowned' }] }])).toThrow('invalid-anchor');
  });

  it('binds a changed blob to only its own identity', () => {
    const first = source();
    const changed = `${body}One qualification.\n`;
    const changedBase = { ...base, objectId: gitBlobObjectId(changed) };
    const next: GenerationSource = { ...first, objectId: changedBase.objectId, body: changed,
      spans: [{ anchorId: generationAnchorId(changedBase, 0, Buffer.byteLength(changed)), start: 0, end: Buffer.byteLength(changed), text: changed }] };
    expect(validateGenerationSources([next])).toHaveLength(1);
    expect(generationSourceIdentity(changedBase)).not.toBe(generationSourceIdentity(base));
    expect(next.spans[0]?.anchorId).not.toBe(first.spans[0]?.anchorId);
  });
});
