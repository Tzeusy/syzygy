// N8 slice 1 (syzygy-u05.8) — the synthetic corpus coverage matrix runs the
// unmodified extraction pipeline in-process against three fixtures whose
// container shape Butlers does not use. Zero egress: everything here is a
// literal string constant already compiled into this package; no network
// call, no repository read, no new consent. Expected values are hard-coded
// literals (never imported from the module under test), and fixtures are
// resolved once in `beforeAll`, not at describe time.
//
// N8 slice 2 adds the `repairFor` narrowing tests below: the reviewer
// advisory on PR #63 found that the original classifier labeled every
// target-class failure 'code-path', which would mislabel a fixture whose
// own authoring is defective (a misnamed heading, say) as a pipeline
// generality gap. The narrowing tests exercise that with a deliberately
// broken ad hoc fixture, not by adding a fourth entry to `SYNTHETIC_CORPORA`
// — the "three synthetic corpora" population above stays exactly three.

import { beforeAll, describe, expect, it } from 'vitest';

import { EXTRACTION_CLASSES } from './project-shape-manifest.js';
import { SYNTHETIC_CORPORA, type SyntheticCorpusFixture } from './fixtures/synthetic-corpora.js';
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

// N8 slice 2 — narrow `repairFor` so a fixture-authoring defect on the
// corpus's own target class (a misnamed heading, a list item missing its
// bold lead) is never mislabeled 'code-path'. These fixtures are
// deliberately broken and local to this describe block; they are never
// added to the shared `SYNTHETIC_CORPORA` population above.
describe('N8 slice 2 — repairFor narrowing: a target-class fixture defect is not a code-path finding', () => {
  const MISNAMED_HEADING_FIXTURE: SyntheticCorpusFixture = {
    id: 'principle-misnamed-heading-defect',
    description: 'Deliberately broken fixture: the heading is misspelled, not misshaped.',
    targetClass: 'principle',
    shape: 'decimal list under a misspelled heading (fixture defect, not a shape gap)',
    path: 'about/heart-and-soul/vision.md',
    text: ['# Aurora', '', '## Non-Negotiable Rule', '', "1. **Every claim must cite the source it came from.**", ''].join('\n'),
  };

  const AMBIGUOUS_LABEL_FIXTURE: SyntheticCorpusFixture = {
    id: 'principle-ambiguous-leading-label-defect',
    description: 'Deliberately broken fixture: a correctly-shaped decimal list item with no bold lead at all.',
    targetClass: 'principle',
    shape: 'decimal list item missing its leading bold label (fixture defect, not a shape gap)',
    path: 'about/heart-and-soul/vision.md',
    text: ['# Aurora', '', '## Non-Negotiable Rules', '', '1. Every claim must cite the source it came from.', ''].join('\n'),
  };

  it('a misnamed heading on the target class fails "missing-heading" and is never labeled code-path', () => {
    const row = runSyntheticCorpusCoverage(MISNAMED_HEADING_FIXTURE);
    const cell = row.cells.find((candidate) => candidate.class === 'principle');
    expect(cell?.outcome).toBe('unknown');
    expect(cell?.failureReason).toBe('missing-heading');
    expect(cell?.failureDetail).toBe('Non-Negotiable Rules');
    expect(cell?.repairKind).toBeUndefined();
    expect(cell?.repairNote).toBeUndefined();
  });

  it('a decimal-list item with no bold lead fails "ambiguous-leading-label" and is never labeled code-path', () => {
    const row = runSyntheticCorpusCoverage(AMBIGUOUS_LABEL_FIXTURE);
    const cell = row.cells.find((candidate) => candidate.class === 'principle');
    expect(cell?.outcome).toBe('unknown');
    expect(cell?.failureReason).toBe('ambiguous-leading-label');
    expect(cell?.repairKind).toBeUndefined();
    expect(cell?.repairNote).toBeUndefined();
  });

  it('a genuine shape mismatch on the target class is still labeled code-path (the narrowing does not over-narrow)', () => {
    // Re-confirms the three real corpora's own target-class cells, whose
    // failures are 'malformed-list'/'malformed-row', keep 'code-path' after
    // the narrowing — same assertion as the three tests above, restated
    // here beside the negative cases so the boundary is visible in one place.
    for (const corpus of SYNTHETIC_CORPORA) {
      const row = runSyntheticCorpusCoverage(corpus);
      const cell = row.cells.find((candidate) => candidate.class === corpus.targetClass);
      expect(cell?.outcome).toBe('unknown');
      expect(['malformed-list', 'malformed-row']).toContain(cell?.failureReason);
      expect(cell?.repairKind).toBe('code-path');
    }
  });

  // Review of PR #73 (R-PWB-N8-SLICE2-REVIEW): the original two-reason
  // SHAPE_MISMATCH_REASONS set wrongly called a malformed roster.toml a
  // "fixture-authoring defect". `roster-identity` is the ninth extraction
  // class and the only TOML-shaped one (extractRosterIdentity,
  // project-shape-extraction.ts:548-575); a body admitted under
  // `roster/*/butler.toml` that carries no `[butler]` table is a genuine
  // container-shape mismatch, structurally identical to a bullet list where
  // a decimal list is expected. This fixture is deliberately broken (no
  // TOML table at all) and, like the fixtures above, is never added to
  // `SYNTHETIC_CORPORA`.
  const MALFORMED_TOML_FIXTURE: SyntheticCorpusFixture = {
    id: 'roster-identity-malformed-toml-shape-mismatch',
    description: 'Deliberately broken fixture: an admitted roster/*/butler.toml path whose body carries no [butler] TOML table at all (genuine shape mismatch, not a fixture defect).',
    targetClass: 'roster-identity',
    shape: 'plain key=value line with no TOML table header under an admitted roster/*/butler.toml path',
    path: 'roster/alice/butler.toml',
    text: ['name = "Alice"', ''].join('\n'),
  };

  it('a roster.toml body with no [butler] table fails "malformed-toml" and is labeled code-path, not a fixture defect', () => {
    const row = runSyntheticCorpusCoverage(MALFORMED_TOML_FIXTURE);
    const cell = row.cells.find((candidate) => candidate.class === 'roster-identity');
    expect(cell?.outcome).toBe('unknown');
    expect(cell?.failureReason).toBe('malformed-toml');
    expect(cell?.failureDetail).toBe('no [butler] table');
    expect(cell?.repairKind).toBe('code-path');
    expect(cell?.repairNote).toContain('roster-identity');
  });
});
