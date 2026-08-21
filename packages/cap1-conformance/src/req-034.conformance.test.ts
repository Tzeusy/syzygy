import { describe, expect, it } from 'vitest';
import {
  computeShapeAnswers,
  readDeclaration,
  registerProject,
  type EvaluationIdentity,
  type ProjectId,
  type ShapeAnswerInputs,
} from '@syzygy/cap1-core';

// CAP1-REQ-034 — Missing evidence yields Unknown; non-satisfaction
// yields Gap; absence is never zero (invariant).
//
// Case (scope of quantification): every served shape answer and
// constituent claim over fixtures with (a) no evidence and (b) evidence
// of non-satisfaction; counterexample schema: a no-evidence claim
// served favourable or zero, or a non-satisfaction claim served
// `Unknown`. Sweep: enumerate served values over both fixtures —
// denominator: the served claim set per fixture. Oracle: fixture (a)
// values are all `Unknown` with a reason from the closed vocabulary;
// fixture (b) values are `Gap`. Oracle independence: the fixtures
// control what evidence exists; expected labels come from SDR-35 and
// VIS-2 — the spellings are hard-coded below, never imported.
// Falsifier: a favourable or zero value served where no evidence
// exists, or `Unknown` served where evidence establishes
// non-satisfaction.

// The closed twelve-reason vocabulary, hard-coded verbatim from RFC2-24
// for the membership oracle.
const TWELVE_REASONS = [
  'missing-declaration',
  'missing-evidence',
  'no-currency-bound-declared',
  'stale-beyond-currency-bound',
  'mapping-coverage-absent',
  'unconsented-source-or-provider',
  'excluded-content',
  'contradicted-pending-adjudication',
  'challenge-suspended',
  'source-uncaptured-or-unreachable',
  'reference-unresolvable',
  'execution-blocked',
] as const;

const PROJECT = 'prj-shape-034' as ProjectId;
const EVALUATION: EvaluationIdentity = { snapshot: 'snap-034', asOf: '2026-08-21T00:00:00Z' };

// Fixture (a): no evidence anywhere — every input absent.
const NO_EVIDENCE: ShapeAnswerInputs = {};

// An invalid declaration: a read that yields named validation failures
// — current admissible evidence that "read and validated" is not
// satisfied.
const INVALID_SOURCE = `
schema_version: "1"
project:
  id: prj-shape-034
  name: Gap Fixture
`;

// Fixture (b): current admissible evidence of non-satisfaction, per
// facet where the adopted requirements give the facet a
// non-satisfaction arm. The two facets absent here are excluded by the
// spec's own text, not skipped silently: `Observable`'s non-observation
// conditions are Unknown-labelled states with reasons by CAP1-REQ-012
// and CAP1-REQ-013's own closed vocabulary (unconsented is a standing
// policy state; a capture failure is absence of observation, not
// established non-satisfaction), and `Mission-ready` renders only its
// deferred posture while its contracts are unaccepted (CAP1-REQ-036).
const NON_SATISFACTION: ShapeAnswerInputs = {
  registration: registerProject(readDeclaration(INVALID_SOURCE), 'rev-1'),
  shapeReferences: [{ reference: 'declarations/spec_root', resolution: 'missing' }],
  comprehension: [{ recordId: 'walkthrough-1', ownerVerdict: 'does-not-stand' }],
  coverage: undefined,
  links: [{ link: 'overview->spec', resolved: false }],
  reconciliation: {
    computed: true,
    outcome: 'unsatisfied',
    declaredScope: 'merged-work',
    mergedWork: [{ workId: 'w1' }],
  },
};

// The five facet indices with a non-satisfaction arm (see comment
// above): Registered, Shape present, Human-understandable, Traceable,
// Reconciled.
const GAP_INDICES = [0, 1, 2, 4, 6] as const;

describe('CAP1-REQ-034 — missing evidence yields Unknown; non-satisfaction yields Gap; absence is never zero', () => {
  it('scenario/sweep (a): with no verifying evidence, every answer renders Unknown with a reason from the closed vocabulary — never favourable, never zero; denominator: all seven', () => {
    const set = computeShapeAnswers(PROJECT, EVALUATION, NO_EVIDENCE);
    expect(set.answers).toHaveLength(7); // denominator disclosed
    for (const answer of set.answers) {
      // Never favourable:
      expect(answer.render.value, answer.name).not.toBe('satisfied');
      // Never Gap either — no evidence establishes non-satisfaction:
      expect(answer.render.value, answer.name).not.toBe('Gap');
      if (answer.name === 'Mission-ready') {
        // The deferred posture: epistemically Unknown, never favourable
        // (its own oracle is CAP1-REQ-036's).
        expect(answer.render.value).toBe('not evaluated');
      } else {
        expect(answer.render.value, answer.name).toBe('Unknown');
        if (answer.render.value === 'Unknown') {
          expect(TWELVE_REASONS, answer.name).toContain(answer.render.reasons.primary);
          for (const secondary of answer.render.reasons.secondary) {
            expect(TWELVE_REASONS, answer.name).toContain(secondary);
          }
        }
      }
    }
  });

  it('sweep (a): no absent quantity is served as zero — no numeric leaf exists anywhere in the no-evidence answer set', () => {
    const set = computeShapeAnswers(PROJECT, EVALUATION, NO_EVIDENCE);
    const scan = (value: unknown, path: string): void => {
      if (Array.isArray(value)) {
        value.forEach((entry, i) => scan(entry, `${path}[${i}]`));
      } else if (typeof value === 'object' && value !== null) {
        for (const [key, entry] of Object.entries(value)) scan(entry, `${path}.${key}`);
      } else {
        expect(typeof value, path).not.toBe('number');
      }
    };
    scan(set, '$');
  });

  it('scenario/sweep (b): current admissible evidence of non-satisfaction renders Gap, never Unknown — denominator: the five facets the spec gives a non-satisfaction arm', () => {
    const set = computeShapeAnswers(PROJECT, EVALUATION, NON_SATISFACTION);
    expect(GAP_INDICES).toHaveLength(5); // denominator disclosed
    for (const i of GAP_INDICES) {
      const answer = set.answers[i];
      expect(answer.render.value, answer.name).toBe('Gap');
      expect(answer.render.value, answer.name).not.toBe('Unknown');
    }
  });

  it('the two are never interchanged: fixture (a) serves zero Gap values; fixture (b)\'s evidenced facets serve zero Unknown values', () => {
    const noEvidence = computeShapeAnswers(PROJECT, EVALUATION, NO_EVIDENCE);
    expect(noEvidence.answers.filter((answer) => answer.render.value === 'Gap')).toHaveLength(0);
    const nonSatisfaction = computeShapeAnswers(PROJECT, EVALUATION, NON_SATISFACTION);
    const evidenced = GAP_INDICES.map((i) => nonSatisfaction.answers[i]);
    expect(evidenced.filter((answer) => answer.render.value === 'Unknown')).toHaveLength(0);
  });

  it('falsifier: a Gap value never carries an Unknown reason set, and an Unknown value always carries one', () => {
    const noEvidence = computeShapeAnswers(PROJECT, EVALUATION, NO_EVIDENCE);
    const nonSatisfaction = computeShapeAnswers(PROJECT, EVALUATION, NON_SATISFACTION);
    for (const answer of [...noEvidence.answers, ...nonSatisfaction.answers]) {
      if (answer.render.value === 'Unknown') {
        expect(answer.render.reasons.primary.length, answer.name).toBeGreaterThan(0);
      } else {
        // No reasons field travels on satisfied/Gap/deferred renders —
        // Gap is established non-satisfaction, not a reasoned Unknown.
        expect('reasons' in answer.render, answer.name).toBe(false);
      }
    }
  });
});
