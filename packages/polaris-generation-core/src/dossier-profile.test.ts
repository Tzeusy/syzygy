import { describe, expect, it, vi } from 'vitest';

import { clarify, DOSSIER_READER_QUESTIONS, DOSSIER_REQUESTED_ASSETS, openQuestions, type OwnerAnswer } from './dossier-profile.js';
import { generationSourcesForBody, gitBlobObjectId, type GenerationSource } from './generation-source.js';
import { validateRequestedAssets } from './provider-draft.js';

const file = (path: string): GenerationSource => generationSourcesForBody({ sourceId: `s-${path.replace(/[^A-Za-z0-9]/gu, '_')}`, repositoryId: 'repository:fixture',
  revision: 'a'.repeat(40), path, objectId: gitBlobObjectId('x\n'), evaluationId: 'e', body: 'x\n' })[0]!;
const deferredRow = (path: string): GenerationSource => { const { body: _b, spans: _s, ...rest } = file(path); return { ...rest, exclusion: { excluded: true, reason: 'deferred-by-budget' }, spans: [] }; };
const answer = (id: OwnerAnswer['id'], text = 'a purpose'): OwnerAnswer => ({ id, answer: text, attribution: 'owner', revision: 'r1', permittedDraftUse: true });

describe('dossier profile', () => {
  it('covers the five reader questions and requests valid assets', () => {
    expect(DOSSIER_READER_QUESTIONS).toHaveLength(5);
    expect(DOSSIER_READER_QUESTIONS.join(' ')).toMatch(/core ideas/u);
    expect(DOSSIER_READER_QUESTIONS.join(' ')).toMatch(/end-to-end/u);
    expect(DOSSIER_READER_QUESTIONS.join(' ')).toMatch(/mechanisms/u);
    expect(DOSSIER_READER_QUESTIONS.join(' ')).toMatch(/maintainers themselves claim/u);
    expect(DOSSIER_READER_QUESTIONS.join(' ')).toMatch(/trade-offs/u);
    expect(validateRequestedAssets([...DOSSIER_REQUESTED_ASSETS])).toHaveLength(DOSSIER_REQUESTED_ASSETS.length);
    expect(DOSSIER_REQUESTED_ASSETS.filter(a => a.required)).toHaveLength(5);
  });
});

describe('REQ-031 clarification', () => {
  const mechanicsOnly = [file('src/server.c'), file('src/db.c')];

  it('finds purpose, audience and scope gaps from the population', () => {
    expect(openQuestions(mechanicsOnly).map(q => q.id)).toEqual(['purpose', 'audience']);
    expect(openQuestions([...mechanicsOnly, file('README.md')], true)).toEqual([]);
    expect(openQuestions([...mechanicsOnly, file('docs/overview.md'), deferredRow('src/x.c'), deferredRow('src/y.c')], true).map(q => q.id)).toEqual(['scope']);
    expect(openQuestions([file('README.md'), deferredRow('src/x.c')], true)[0]!.question).toContain('1 file(s)');
  });

  it('zero-interaction mode asks nothing, records what it would have asked, and fabricates no default', async () => {
    const ask = vi.fn();
    const record = await clarify({ sources: mechanicsOnly, mode: 'zero-interaction', ask });
    expect(ask).not.toHaveBeenCalled();
    expect(record.wouldHaveAsked.map(q => q.id)).toEqual(['purpose', 'audience']);
    expect(record.wouldHaveAsked[0]).toMatchObject({ scope: expect.any(String), reason: expect.any(String) });
    expect(record.limitations).toHaveLength(2);
    expect(record.limitations[0]).toContain('no mission is asserted');
    expect(record).toMatchObject({ answers: [], fabricatedDefaults: 0, mode: 'zero-interaction' });
  });

  it('stops at the question budget and does not repeat a deferred question', async () => {
    const sources = [...mechanicsOnly, deferredRow('src/x.c')];
    const record = await clarify({ sources, mode: 'zero-interaction', maxQuestions: 1, alreadyDeferred: ['purpose'] });
    expect(record.suppressedAsRepeats).toEqual(['purpose']);
    expect(record.wouldHaveAsked.map(q => q.id)).toEqual(['audience']);
    expect(record.suppressedByBudget).toEqual(['scope']);
    expect(record.limitations).toHaveLength(3);
  });

  it('records an owner answer with attribution without adopting it, and keeps a declined one as a limitation', async () => {
    const asked: string[] = [];
    const ask = async (q: { id: OwnerAnswer['id'] }): Promise<OwnerAnswer> => { asked.push(q.id); return q.id === 'purpose' ? answer('purpose') : { ...answer('audience'), answer: 'unknown' }; };
    const record = await clarify({ sources: mechanicsOnly, mode: 'interactive', ask });
    expect(asked).toEqual(['purpose', 'audience']);
    expect(record.answers).toEqual([{ ...answer('purpose'), adopted: false }, { ...answer('audience'), answer: 'unknown', adopted: false }]);
    expect(record.limitations).toEqual([expect.stringContaining('Intended reader')]);
    expect(record.wouldHaveAsked).toEqual([]);
  });

  it('refuses interactive mode without a port, a mismatched answer or an unattributed one', async () => {
    await expect(clarify({ sources: mechanicsOnly, mode: 'interactive' })).rejects.toThrow('owner-port');
    await expect(clarify({ sources: mechanicsOnly, mode: 'interactive', ask: async () => answer('audience') })).rejects.toThrow('invalid-owner-answer');
    await expect(clarify({ sources: mechanicsOnly, mode: 'interactive', ask: async q => ({ ...answer(q.id), attribution: '' }) })).rejects.toThrow('invalid-owner-answer');
    await expect(clarify({ sources: mechanicsOnly, mode: 'zero-interaction', maxQuestions: -1 })).rejects.toThrow('invalid-question-budget');
  });
});
