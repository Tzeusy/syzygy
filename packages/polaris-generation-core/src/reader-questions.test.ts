import { describe, expect, it } from 'vitest';

import { DOSSIER_READER_QUESTIONS } from './dossier-profile.js';
import { READER_QUESTION_TEXT_MAX, READER_QUESTIONS_MAX, ReaderQuestionsError, validateReaderQuestions } from './reader-questions.js';

const q = (over: Record<string, unknown> = {}) => ({ id: 'a', topics: ['mechanisms'], text: 'What?', ...over });

describe('reader questions', () => {
  it('accepts the dossier profile and a topic-less question', () => {
    expect(validateReaderQuestions(DOSSIER_READER_QUESTIONS)).toHaveLength(5);
    expect(validateReaderQuestions([q({ topics: [] })])).toHaveLength(1);
  });

  it('fails closed on every shape violation', () => {
    const bad: unknown[] = [undefined, null, 'text', [], ['bare string'], [null], [q({ extra: 1 })], [q({ id: '' })], [q({ id: 'has space' })], [q({ id: 7 })],
      [q(), q()], [q({ text: '' })], [q({ text: '   ' })], [q({ text: 5 })], [q({ text: 'x'.repeat(READER_QUESTION_TEXT_MAX + 1) })],
      [q({ topics: ['nope'] })], [q({ topics: 'mechanisms' })], [q({ topics: ['mechanisms', 'mechanisms'] })], [{ id: 'a', text: 'x' }],
      Array.from({ length: READER_QUESTIONS_MAX + 1 }, (_, i) => q({ id: `q${i}` }))];
    for (const value of bad) expect(() => validateReaderQuestions(value), JSON.stringify(value)?.slice(0, 60)).toThrow(ReaderQuestionsError);
  });

  it('accepts text at the bound and the maximum count', () => {
    expect(validateReaderQuestions([q({ text: 'x'.repeat(READER_QUESTION_TEXT_MAX) })])).toHaveLength(1);
    expect(validateReaderQuestions(Array.from({ length: READER_QUESTIONS_MAX }, (_, i) => q({ id: `q${i}` })))).toHaveLength(READER_QUESTIONS_MAX);
  });
});
