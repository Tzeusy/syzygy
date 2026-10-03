import { describe, expect, it, vi } from 'vitest';

import { clarify, DOSSIER_READER_QUESTIONS, DOSSIER_REQUESTED_ASSETS, dossierQuestionsFile, openQuestions, type ClarificationQuestion, type OwnerAnswer } from './dossier-profile.js';
import { generationSourcesForBody, gitBlobObjectId, type GenerationSource } from './generation-source.js';
import { validateRequestedAssets } from './provider-draft.js';
import { READER_QUESTION_TOPICS, validateReaderQuestions } from './reader-questions.js';

const file = (path: string): GenerationSource => generationSourcesForBody({ sourceId: `s-${path.replace(/[^A-Za-z0-9]/gu, '_')}`, repositoryId: 'repository:fixture',
  revision: 'a'.repeat(40), path, objectId: gitBlobObjectId('x\n'), evaluationId: 'e', body: 'x\n' })[0]!;
const deferredRow = (path: string): GenerationSource => { const { body: _b, spans: _s, ...rest } = file(path); return { ...rest, exclusion: { excluded: true, reason: 'deferred-by-budget' }, spans: [] }; };
const answer = (id: OwnerAnswer['id'], text: unknown = 'a purpose'): OwnerAnswer => ({ id, answer: text, attribution: 'owner', revision: 'r1', permittedDraftUse: true });

describe('dossier profile', () => {
  it('exports the five questions as {id, topics, text} matching the owner topics and the frozen file shape', () => {
    expect(DOSSIER_READER_QUESTIONS.map(question => question.id)).toEqual([...READER_QUESTION_TOPICS]);
    expect(DOSSIER_READER_QUESTIONS.every(question => question.topics.length === 1 && question.topics[0] === question.id)).toBe(true);
    const text = DOSSIER_READER_QUESTIONS.map(question => question.text).join(' ');
    for (const phrase of ['core ideas', 'end-to-end', 'mechanisms', 'maintainers themselves claim', 'trade-offs']) expect(text).toContain(phrase);
    const file = JSON.parse(dossierQuestionsFile());
    expect(file.format).toBe('polaris-reader-questions-v1');
    expect(validateReaderQuestions(file.questions)).toEqual(DOSSIER_READER_QUESTIONS);
  });

  it('requests one required section per question, with ids matching the topics', () => {
    expect(validateRequestedAssets([...DOSSIER_REQUESTED_ASSETS])).toHaveLength(DOSSIER_REQUESTED_ASSETS.length);
    expect(DOSSIER_REQUESTED_ASSETS.filter(asset => asset.required).map(asset => asset.id)).toEqual([...READER_QUESTION_TOPICS]);
  });
});

describe('REQ-031 clarification', () => {
  const mechanicsOnly = [file('src/server.c'), file('src/db.c')];

  it('finds purpose, audience and scope gaps from the population, each with a content digest', () => {
    expect(openQuestions(mechanicsOnly).map(q => q.id)).toEqual(['purpose', 'audience']);
    expect(openQuestions([...mechanicsOnly, file('README.md')], true)).toEqual([]);
    const scope = openQuestions([...mechanicsOnly, file('docs/overview.md'), deferredRow('src/x.c'), deferredRow('src/y.c')], true);
    expect(scope.map(q => q.id)).toEqual(['scope']);
    expect(scope[0]!.contentDigest).toMatch(/^[0-9a-f]{64}$/u);
    expect(openQuestions([file('README.md'), deferredRow('src/x.c')], true)[0]!.question).toContain('1 file(s)');
  });

  it('zero-interaction mode asks nothing, records what it would have asked, and accounts for every question', async () => {
    const ask = vi.fn();
    const record = await clarify({ sources: mechanicsOnly, mode: 'zero-interaction', ask });
    expect(ask).not.toHaveBeenCalled();
    expect(record.wouldHaveAsked.map(q => q.id)).toEqual(['purpose', 'audience']);
    expect(record.wouldHaveAsked[0]).toMatchObject({ scope: expect.any(String), reason: expect.any(String) });
    expect(record.limitations).toHaveLength(2);
    expect(record.limitations[0]).toContain('no mission is asserted');
    expect(record.limitations[1]).toContain('remains unestablished');
    expect(record).toMatchObject({ answers: [], unaccountedQuestions: 0, mode: 'zero-interaction' });
  });

  it('measures unaccounted questions rather than asserting zero', async () => {
    const record = await clarify({ sources: mechanicsOnly, mode: 'zero-interaction' });
    const open = openQuestions(mechanicsOnly);
    expect(record.limitations.length + record.answers.length).toBe(open.length);
    expect(record.unaccountedQuestions).toBe(0);
  });

  it('stops at the question budget and does not repeat an unchanged deferred question', async () => {
    const sources = [...mechanicsOnly, deferredRow('src/x.c')];
    const [purpose] = openQuestions(sources);
    const record = await clarify({ sources, mode: 'zero-interaction', maxQuestions: 1, prior: [{ id: 'purpose', contentDigest: purpose!.contentDigest, disposition: 'deferred' }] });
    expect(record.suppressedAsRepeats).toEqual(['purpose']);
    expect(record.wouldHaveAsked.map(q => q.id)).toEqual(['audience']);
    expect(record.suppressedByBudget).toEqual(['scope']);
    expect(record.limitations).toHaveLength(3);
  });

  it('asks a deferred question again when its material content changed', async () => {
    const before = [...mechanicsOnly, deferredRow('src/x.c')];
    const after = [...mechanicsOnly, deferredRow('src/x.c'), deferredRow('src/y.c')];
    const scopeBefore = openQuestions(before).find(q => q.id === 'scope')!;
    const record = await clarify({ sources: after, mode: 'zero-interaction', maxQuestions: 5, prior: [{ id: 'scope', contentDigest: scopeBefore.contentDigest, disposition: 'deferred' }] });
    expect(record.reaskedAfterChange).toEqual(['scope']);
    expect(record.wouldHaveAsked.map(q => q.id)).toContain('scope');
    expect(record.suppressedAsRepeats).toEqual([]);
  });

  it('reuses an unchanged answered question without asking and records it as reused', async () => {
    const [purpose] = openQuestions(mechanicsOnly);
    const ask = vi.fn(async (q: ClarificationQuestion) => answer(q.id as 'audience', 'engineers'));
    const record = await clarify({ sources: mechanicsOnly, mode: 'interactive', ask,
      prior: [{ id: 'purpose', contentDigest: purpose!.contentDigest, disposition: 'answered', answer: 'cache', attribution: 'owner', revision: 'r0' }] });
    expect(ask.mock.calls.map(call => call[0].id)).toEqual(['audience']);
    expect(record.answers[0]).toMatchObject({ id: 'purpose', answer: 'cache', reused: true, adopted: false });
    expect(record.limitations).toEqual([]);
    expect(record.dispositions.map(d => `${d.id}:${d.disposition}`)).toEqual(['purpose:answered', 'audience:answered']);
  });

  it('records an owner answer with attribution without adopting it, and keeps a declined one as a limitation', async () => {
    const asked: string[] = [];
    const ask = async (q: { id: OwnerAnswer['id'] }): Promise<OwnerAnswer> => { asked.push(q.id); return q.id === 'purpose' ? answer('purpose') : answer('audience', 'unknown'); };
    const record = await clarify({ sources: mechanicsOnly, mode: 'interactive', ask });
    expect(asked).toEqual(['purpose', 'audience']);
    expect(record.answers).toMatchObject([{ id: 'purpose', disposition: 'answered', answer: 'a purpose', adopted: false }, { id: 'audience', disposition: 'unknown', answer: null }]);
    expect(record.limitations).toEqual([expect.stringContaining('intended reader')]);
    expect(record.wouldHaveAsked).toEqual([]);
  });

  it('treats an empty, blank or non-string answer as unknown, never as resolving the question', async () => {
    for (const text of ['', '   ', 42, null, undefined, {}, '  unknown ']) {
      const record = await clarify({ sources: [...mechanicsOnly, file('README.md')], mode: 'interactive', maxQuestions: 1, ask: async q => ({ ...answer(q.id), answer: text }) });
      expect(record.answers[0], String(text)).toMatchObject({ id: 'audience', disposition: 'unknown', answer: null });
      expect(record.limitations).toHaveLength(1);
    }
    const trimmed = await clarify({ sources: [...mechanicsOnly, file('README.md')], mode: 'interactive', ask: async q => answer(q.id, '  engineers  ') });
    expect(trimmed.answers[0]).toMatchObject({ answer: 'engineers', disposition: 'answered' });
  });

  it('redacts an answer the owner did not permit for draft use and keeps only the limitation', async () => {
    const record = await clarify({ sources: [...mechanicsOnly, file('README.md')], mode: 'interactive', ask: async q => ({ ...answer(q.id, 'SECRET-AUDIENCE'), permittedDraftUse: false }) });
    expect(record.answers[0]).toMatchObject({ id: 'audience', disposition: 'redacted', answer: null, permittedDraftUse: false });
    expect(JSON.stringify(record)).not.toContain('SECRET-AUDIENCE');
    expect(record.limitations).toHaveLength(1);
    expect(record.dispositions[0]).toMatchObject({ disposition: 'redacted' });
    expect(record.dispositions[0]).not.toHaveProperty('answer');
  });

  it('keeps earlier answers when a later reply is bad, and carries the rest as limitations', async () => {
    let n = 0;
    const record = await clarify({ sources: mechanicsOnly, mode: 'interactive', maxQuestions: 3,
      ask: async q => (n++ === 0 ? answer(q.id) : { ...answer(q.id), attribution: '' }) });
    expect(record.answers).toHaveLength(1);
    expect(record.answers[0]).toMatchObject({ id: 'purpose', answer: 'a purpose' });
    expect(record.aborted).toEqual({ id: 'audience', reason: 'invalid-owner-answer' });
    expect(record.limitations).toEqual([expect.stringContaining('intended reader')]);
    const thrown = await clarify({ sources: mechanicsOnly, mode: 'interactive', ask: async () => { throw new Error('port down'); } });
    expect(thrown.aborted).toEqual({ id: 'purpose', reason: 'port down' });
    expect(thrown.limitations).toHaveLength(2);
    expect(thrown.unaccountedQuestions).toBe(0);
  });

  it('rejects a reply whose permittedDraftUse is not a boolean', async () => {
    const record = await clarify({ sources: mechanicsOnly, mode: 'interactive', ask: async q => ({ ...answer(q.id), permittedDraftUse: 'yes' as unknown as boolean }) });
    expect(record.answers).toEqual([]);
    expect(record.aborted).toEqual({ id: 'purpose', reason: 'invalid-owner-answer' });
  });

  it('refuses interactive mode without a port, a mismatched id and a bad budget', async () => {
    await expect(clarify({ sources: mechanicsOnly, mode: 'interactive' })).rejects.toThrow('owner-port');
    const mismatch = await clarify({ sources: mechanicsOnly, mode: 'interactive', ask: async () => answer('scope') });
    expect(mismatch.aborted).toMatchObject({ id: 'purpose', reason: 'invalid-owner-answer' });
    await expect(clarify({ sources: mechanicsOnly, mode: 'zero-interaction', maxQuestions: -1 })).rejects.toThrow('invalid-question-budget');
  });
});
