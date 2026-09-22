// N8 slice 1 (syzygy-u05.8) — the synthetic corpus coverage matrix runs the
// unmodified extraction pipeline in-process against three fixtures whose
// container shape Butlers does not use. Zero egress: everything here is a
// literal string constant already compiled into this package; no network
// call, no repository read, no new consent. Expected values are hard-coded
// literals (never imported from the module under test), and fixtures are
// resolved once in `beforeAll`, not at describe time.

import { beforeAll, describe, expect, it } from 'vitest';

import { EXTRACTION_CLASSES } from './project-shape-manifest.js';
import { SYNTHETIC_CORPORA } from './fixtures/synthetic-corpora.js';
import { runAllSyntheticCorpusCoverage, runSyntheticCorpusCoverage, type CorpusRow } from './synthetic-corpus-coverage.js';

describe('N8 slice 1 — synthetic corpus coverage matrix', () => {
  let rows: readonly CorpusRow[] = [];

  beforeAll(() => {
    rows = runAllSyntheticCorpusCoverage();
  });

  const rowFor = (id: string): CorpusRow => {
    const row = rows.find((candidate) => candidate.corpus.id === id);
    if (row === undefined) throw new Error(`no coverage row for corpus "${id}"`);
    return row;
  };

  it('produces exactly the three fixtures declared, each with all nine classes and no false zero', () => {
    expect(SYNTHETIC_CORPORA.map((corpus) => corpus.id)).toEqual(['principle-bullet-list', 'success-criterion-table', 'craft-policy-prose']);
    expect(rows).toHaveLength(3);
    for (const row of rows) {
      expect(row.cells.map((cell) => cell.class).sort()).toEqual([...EXTRACTION_CLASSES].sort());
      expect(row.denominator).toBe(9);
      expect(row.extractedCount + row.unknownCount).toBe(9);
      for (const cell of row.cells) {
        if (cell.outcome === 'unknown') {
          // An unextracted cell never carries a count: Unknown, not zero.
          expect(cell.count).toBeUndefined();
          expect(cell.denominator).toBeUndefined();
          expect(cell.failureReason).toBeDefined();
        } else {
          expect(cell.count).toBeDefined();
          expect(cell.count).toBe(cell.denominator);
        }
      }
    }
  });

  it('principle-bullet-list: an unordered, non-bold list is Unknown under "principle" — a code-path gap, not admission', () => {
    const row = rowFor('principle-bullet-list');
    const cell = row.cells.find((candidate) => candidate.class === 'principle');
    expect(cell?.outcome).toBe('unknown');
    expect(cell?.failureReason).toBe('malformed-list');
    expect(cell?.failureDetail).toBe('not a decimal-list item');
    expect(cell?.repairKind).toBe('code-path');
  });

  it('success-criterion-table: a pipe table is Unknown under "success-criterion" — a code-path gap, not admission', () => {
    const row = rowFor('success-criterion-table');
    const cell = row.cells.find((candidate) => candidate.class === 'success-criterion');
    expect(cell?.outcome).toBe('unknown');
    expect(cell?.failureReason).toBe('malformed-list');
    expect(cell?.failureDetail).toBe('no top-level list');
    expect(cell?.repairKind).toBe('code-path');
  });

  it('craft-policy-prose: numbered prose is Unknown under "craft-policy" — a code-path gap, not admission', () => {
    const row = rowFor('craft-policy-prose');
    const cell = row.cells.find((candidate) => candidate.class === 'craft-policy');
    expect(cell?.outcome).toBe('unknown');
    expect(cell?.failureReason).toBe('malformed-row');
    expect(cell?.failureDetail).toBe('no table');
    expect(cell?.repairKind).toBe('code-path');
  });

  it('every corpus reports unsupported-source (a profile-row gap) for the same six path-pattern classes', () => {
    const alwaysGated = ['baseline-spec', 'roster-identity', 'topology-component'] as const;
    for (const row of rows) {
      for (const cls of alwaysGated) {
        const cell = row.cells.find((candidate) => candidate.class === cls);
        expect(cell?.outcome).toBe('unknown');
        expect(cell?.failureReason).toBe('unsupported-source');
        expect(cell?.repairKind).toBe('profile-row');
      }
    }
  });

  it('a basename that coincidentally matches a class the corpus was not authored for fails on missing content, not on the shape being tested', () => {
    const row = rowFor('principle-bullet-list');
    const projectAccount = row.cells.find((candidate) => candidate.class === 'project-account-section');
    expect(projectAccount?.outcome).toBe('unknown');
    expect(projectAccount?.failureReason).toBe('missing-heading');
    expect(projectAccount?.failureDetail).toBe('What Butlers Is');
    // Not a generality finding for this class: no repair classification.
    expect(projectAccount?.repairKind).toBeUndefined();
  });

  it('running a single corpus through runSyntheticCorpusCoverage matches its row in the full run', () => {
    const single = runSyntheticCorpusCoverage(SYNTHETIC_CORPORA[0]!);
    const full = rowFor('principle-bullet-list');
    expect(single).toEqual(full);
  });
});
