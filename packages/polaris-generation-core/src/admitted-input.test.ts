import { describe, expect, it } from 'vitest';
import {
  admitSourcePopulation, admittedSources, sourcePopulationDenominator, SourcePopulationError,
  type AdmittedSource, type ExcludedSource,
} from './admitted-input.js';

// Hard-coded, not imported from provider-draft.ts's SOURCE_TEXT_MAX_LENGTH: this
// literal is the independent expectation that admitted-input.ts's bound must
// match sourceSchema's, not a tautology against the shared constant itself.
const SOURCE_TEXT_UPPER_BOUND = 100_000;

const selected: AdmittedSource[] = [
  { sourceId: 'purpose', text: 'Reduce recurring mental labor.' },
  { sourceId: 'mechanism', text: 'Observations feed a plan.' },
];
const excluded: ExcludedSource[] = [
  { sourceId: 'appendix', reason: 'unavailable', detail: 'Denied by classification.' },
  { sourceId: 'draft-notes', reason: 'deferred-by-budget', detail: 'Research budget exhausted before this file.' },
];

describe('admitted-input source population', () => {
  it('admits a population with only selected sources and an empty exclusion list', () => {
    const population = admitSourcePopulation(selected);
    expect(population).toEqual({ selected, excluded: [] });
    expect(sourcePopulationDenominator(population)).toEqual({ selected: 2, excluded: 0, total: 2 });
  });

  it('admits a mixed population and produces the full denominator', () => {
    const population = admitSourcePopulation(selected, excluded);
    expect(sourcePopulationDenominator(population)).toEqual({ selected: 2, excluded: 2, total: 4 });
  });

  it('projects exactly and only the admitted sources, in order, never the excluded ones', () => {
    const population = admitSourcePopulation(selected, excluded);
    const projected = admittedSources(population);
    expect(projected).toEqual(selected);
    expect(projected.map(s => s.sourceId)).toEqual(['purpose', 'mechanism']);
    expect(projected.some(s => excluded.some(e => e.sourceId === s.sourceId))).toBe(false);
  });

  it('rejects a source id repeated within the selected list', () => {
    expect(() => admitSourcePopulation([...selected, { sourceId: 'purpose', text: 'Second copy.' }]))
      .toThrow(SourcePopulationError);
    try {
      admitSourcePopulation([...selected, { sourceId: 'purpose', text: 'Second copy.' }]);
    } catch (error) {
      expect(error).toBeInstanceOf(SourcePopulationError);
      expect((error as SourcePopulationError).code).toBe('duplicate-source-id');
    }
  });

  it('rejects a source id repeated across the selected and excluded lists', () => {
    expect(() => admitSourcePopulation(selected, [...excluded, { sourceId: 'purpose', reason: 'excluded', detail: 'Also excluded.' }]))
      .toThrow(SourcePopulationError);
  });

  it('rejects an empty source id in either list', () => {
    expect(() => admitSourcePopulation([{ sourceId: '', text: 'x' }])).toThrow(SourcePopulationError);
    expect(() => admitSourcePopulation(selected, [{ sourceId: '', reason: 'excluded', detail: 'x' }])).toThrow(SourcePopulationError);
  });

  it('rejects an empty text on a selected source', () => {
    expect(() => admitSourcePopulation([{ sourceId: 'x', text: '' }])).toThrow(SourcePopulationError);
  });

  it('rejects an empty detail on an excluded source', () => {
    expect(() => admitSourcePopulation(selected, [{ sourceId: 'x', reason: 'unresolved', detail: '' }])).toThrow(SourcePopulationError);
  });

  it('rejects a selected sourceId containing whitespace, matching sourceSchema\'s handle pattern', () => {
    expect(() => admitSourcePopulation([{ sourceId: 'has space', text: 'x' }])).toThrow(SourcePopulationError);
    try {
      admitSourcePopulation([{ sourceId: 'has space', text: 'x' }]);
    } catch (error) {
      expect((error as SourcePopulationError).code).toBe('invalid-source-id');
    }
  });

  it('rejects a pattern-invalid selected sourceId whose first character the handle pattern forbids', () => {
    // sourceSchema's handle pattern is ^[A-Za-z0-9][A-Za-z0-9_.:-]*$: a leading
    // underscore is a legal later character but never a legal first one.
    expect(() => admitSourcePopulation([{ sourceId: '_leading-underscore', text: 'x' }])).toThrow(SourcePopulationError);
    try {
      admitSourcePopulation([{ sourceId: '_leading-underscore', text: 'x' }]);
    } catch (error) {
      expect((error as SourcePopulationError).code).toBe('invalid-source-id');
    }
  });

  it('accepts a selected sourceId exactly at the handle length bound and rejects one character over it', () => {
    const atBound = admitSourcePopulation([{ sourceId: 'x'.repeat(100), text: 'x' }]);
    expect(sourcePopulationDenominator(atBound)).toEqual({ selected: 1, excluded: 0, total: 1 });
    try {
      admitSourcePopulation([{ sourceId: 'x'.repeat(101), text: 'x' }]);
      throw new Error('expected throw');
    } catch (error) {
      expect((error as SourcePopulationError).code).toBe('invalid-source-id');
    }
  });

  it('accepts a selected source text exactly at the upper bound and rejects one character over it', () => {
    const atBound = admitSourcePopulation([{ sourceId: 'x', text: 'a'.repeat(SOURCE_TEXT_UPPER_BOUND) }]);
    expect(sourcePopulationDenominator(atBound)).toEqual({ selected: 1, excluded: 0, total: 1 });
    expect(() => admitSourcePopulation([{ sourceId: 'x', text: 'a'.repeat(SOURCE_TEXT_UPPER_BOUND + 1) }])).toThrow(SourcePopulationError);
    try {
      admitSourcePopulation([{ sourceId: 'x', text: 'a'.repeat(SOURCE_TEXT_UPPER_BOUND + 1) }]);
    } catch (error) {
      expect((error as SourcePopulationError).code).toBe('text-too-long');
    }
  });

  it('reports the exact failure code for each rejection kind', () => {
    const codes: Record<string, unknown> = {};
    for (const [label, thunk] of [
      ['empty-source-id', () => admitSourcePopulation([{ sourceId: '', text: 'x' }])],
      ['empty-text', () => admitSourcePopulation([{ sourceId: 'x', text: '' }])],
      ['empty-detail', () => admitSourcePopulation(selected, [{ sourceId: 'x', reason: 'unresolved', detail: '' }])],
      ['duplicate-source-id', () => admitSourcePopulation([...selected, selected[0]!])],
      ['invalid-source-id', () => admitSourcePopulation([{ sourceId: 'has space', text: 'x' }])],
      ['text-too-long', () => admitSourcePopulation([{ sourceId: 'x', text: 'a'.repeat(SOURCE_TEXT_UPPER_BOUND + 1) }])],
    ] as const) {
      try { thunk(); throw new Error('expected throw'); }
      catch (error) { codes[label] = (error as SourcePopulationError).code; }
    }
    expect(codes).toEqual({
      'empty-source-id': 'empty-source-id',
      'empty-text': 'empty-text',
      'empty-detail': 'empty-detail',
      'duplicate-source-id': 'duplicate-source-id',
      'invalid-source-id': 'invalid-source-id',
      'text-too-long': 'text-too-long',
    });
  });
});
