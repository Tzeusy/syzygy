import { describe, expect, it } from 'vitest';
import {
  computeShapeAnswers,
  shapeAnswerComposition,
  type EvaluationIdentity,
  type ProjectId,
  type ShapeAnswerInputs,
  type ShapeAnswerSet,
} from '@syzygy/cap1-core';

// CAP1-REQ-031 — No combined score, badge, colour, percentage, or
// passing count (prohibition).
//
// Case (scope of quantification): every rendering and machine answer
// that presents more than one shape answer; counterexample schema: a
// served value derived from two or more answers' values. Sweep:
// enumerate the served project-level fields for a fixture project and
// check that none is a function of multiple facet values — denominator:
// the served field set. Oracle: no served field aggregates facet values
// into one number, colour, badge, or count-of-passing; bounded by the
// served field set. Oracle independence: the check runs against the
// served output's own declared derivations (field-by-field diff under a
// facet flip), not implementation intent. Falsifier: a served "5/7
// green", a project health colour, or any single indicator whose value
// changes when one facet flips while it claims to summarize them.

const PROJECT = 'prj-shape-031' as ProjectId;
const EVALUATION: EvaluationIdentity = { snapshot: 'snap-031', asOf: '2026-08-21T00:00:00Z' };

// A fixture with a Gap and several Unknown values (the requirement's
// scenario): Traceable Gap; Shape present / Human-understandable /
// Observable / Reconciled Unknown; Registered absent too — all Unknown
// except the Gap. No registration input at all keeps this minimal.
const MIXED_INPUTS: ShapeAnswerInputs = {
  registration: undefined,
  shapeReferences: undefined,
  comprehension: undefined,
  coverage: undefined,
  links: [{ link: 'a->b', resolved: false }],
  reconciliation: undefined,
};

function serve(inputs: ShapeAnswerInputs): ShapeAnswerSet {
  return computeShapeAnswers(PROJECT, EVALUATION, inputs);
}

// Every leaf value in a served object, with its path — the sweep's
// population.
function leaves(value: unknown, path: string): { path: string; leaf: unknown }[] {
  if (Array.isArray(value)) {
    return value.flatMap((entry, i) => leaves(entry, `${path}[${i}]`));
  }
  if (typeof value === 'object' && value !== null) {
    return Object.entries(value).flatMap(([key, entry]) => leaves(entry, `${path}.${key}`));
  }
  return [{ path, leaf: value }];
}

describe('CAP1-REQ-031 — no combined score, badge, colour, percentage, or passing count', () => {
  it('sweep: the served project-level field set is exactly {projectId, evaluation, answers} — no aggregate field exists; denominator disclosed', () => {
    const set = serve(MIXED_INPUTS);
    const fields = Object.keys(set).sort();
    expect(fields).toHaveLength(3); // denominator: the served field set
    expect(fields).toEqual(['answers', 'evaluation', 'projectId']);
  });

  it('sweep: no served leaf anywhere in the answer set is a number, a percentage, a fraction, or a colour word — the whole serialization, denominator disclosed', () => {
    const set = serve(MIXED_INPUTS);
    const population = leaves(set, '$');
    expect(population.length).toBeGreaterThan(10); // denominator visible
    for (const { path, leaf } of population) {
      // No numeric leaf at all: no score, no percentage, no count.
      expect(typeof leaf, path).not.toBe('number');
      if (typeof leaf === 'string') {
        expect(leaf, path).not.toMatch(/^\d+\s*\/\s*\d+/); // "5/7"
        expect(leaf, path).not.toMatch(/\d+\s*%/); // percentage
        expect(leaf, path).not.toMatch(/^(green|red|amber|yellow)$/i); // health colour
      }
    }
  });

  it('oracle: no served field is a function of multiple facet values — under a one-facet flip, only that facet\'s own entry changes', () => {
    const baseline = serve(MIXED_INPUTS);
    // Flip one facet (Traceable: Gap -> satisfied).
    const flipped = serve({ ...MIXED_INPUTS, links: [{ link: 'a->b', resolved: true }] });
    // Top-level: projectId and evaluation are facet-independent.
    expect(JSON.stringify(flipped.projectId)).toBe(JSON.stringify(baseline.projectId));
    expect(JSON.stringify(flipped.evaluation)).toBe(JSON.stringify(baseline.evaluation));
    // Within answers: exactly the flipped facet's entry differs. A
    // single indicator summarizing the seven would have to live in a
    // field that changes on this flip — there is none.
    for (let i = 0; i < 7; i += 1) {
      const same = JSON.stringify(flipped.answers[i]) === JSON.stringify(baseline.answers[i]);
      expect(same, `answers[${i}]`).toBe(i !== 4);
    }
  });

  it('the aggregate rendering discloses its members\' composition instead — one entry per member, nothing derived across members', () => {
    const set = serve(MIXED_INPUTS);
    const composition = shapeAnswerComposition(set);
    expect(composition).toHaveLength(7);
    // Each entry is one member's own (name, value) — and flipping one
    // member changes exactly that member's entry, nothing else.
    const flipped = shapeAnswerComposition(
      serve({ ...MIXED_INPUTS, links: [{ link: 'a->b', resolved: true }] }),
    );
    for (let i = 0; i < 7; i += 1) {
      const same = JSON.stringify(flipped[i]) === JSON.stringify(composition[i]);
      expect(same, `composition[${i}]`).toBe(i !== 4);
    }
    // The composition carries no epistemic state of its own and no
    // count-of-passing: it is a list of seven, not a scalar.
    expect(Array.isArray(composition)).toBe(true);
    for (const entry of composition) {
      expect(Object.keys(entry).sort()).toEqual(['name', 'value']);
    }
  });

  it('scenario: with a Gap and several Unknowns, no served field summarizes them', () => {
    const set = serve(MIXED_INPUTS);
    const values = set.answers.map((answer) => answer.render.value);
    expect(values).toContain('Gap');
    expect(values.filter((value) => value === 'Unknown').length).toBeGreaterThan(1);
    // The full serialization never contains a passing count or badge
    // over the mixed membership.
    const serialized = JSON.stringify(set);
    expect(serialized).not.toMatch(/\d+\s*\/\s*7/);
    expect(serialized).not.toMatch(/"(score|badge|colour|color|percent|percentage|passing)"/i);
  });
});
