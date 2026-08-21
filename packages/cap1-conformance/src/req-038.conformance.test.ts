import { describe, expect, it } from 'vitest';
import {
  computeShapeAnswers,
  readDeclaration,
  registerProject,
  type EvaluationIdentity,
  type ProjectId,
  type ShapeAnswerInputs,
} from '@syzygy/cap1-core';

// CAP1-REQ-038 — A negative or Unknown answer never erases the others
// (state projection/query).
//
// Case: a checker constructs a project with one `Gap`, several
// `Unknown`s, and one satisfied answer, and queries the set.
// Observable: the served answer set. Oracle: all seven answers present
// with their independent values; count and per-answer comparison;
// bounded: seven entries. Oracle independence: the fixture defines the
// expected values per answer — hard-coded below. Falsifier: an answer
// omitted or blanked because a sibling is negative or Unknown.

const PROJECT = 'prj-shape-038' as ProjectId;
const EVALUATION: EvaluationIdentity = { snapshot: 'snap-038', asOf: '2026-08-21T00:00:00Z' };

const SOURCE = `
schema_version: "1"
project:
  id: prj-shape-038
  name: Mixed Fixture
owner: uniquosity@gmail.com
repositories:
  - id: repo-main
    role: governance-root
    consent: consent-1
consents:
  - consent-1
declarations:
  spec_root: openspec/
relations: []
profiles: []
`;

// The mixed fixture: Registered satisfied; Traceable Gap; Shape
// present, Human-understandable, Observable, Reconciled Unknown;
// Mission-ready its deferred posture.
function mixedInputs(): ShapeAnswerInputs {
  const read = readDeclaration(SOURCE);
  if (!read.ok) throw new Error('fixture must be valid');
  return {
    registration: registerProject(read, 'rev-1'), // -> satisfied
    shapeReferences: undefined, // -> Unknown
    comprehension: undefined, // -> Unknown
    coverage: undefined, // -> Unknown
    links: [{ link: 'overview->spec', resolved: false }], // -> Gap
    reconciliation: undefined, // -> Unknown
  };
}

// The fixture-defined expectation per answer, in CAP1-REQ-030's order —
// hard-coded (oracle independence).
const EXPECTED: readonly { name: string; value: string }[] = [
  { name: 'Registered', value: 'satisfied' },
  { name: 'Shape present', value: 'Unknown' },
  { name: 'Human-understandable', value: 'Unknown' },
  { name: 'Observable', value: 'Unknown' },
  { name: 'Traceable', value: 'Gap' },
  { name: 'Mission-ready', value: 'not evaluated' },
  { name: 'Reconciled', value: 'Unknown' },
];

describe('CAP1-REQ-038 — a negative or Unknown answer never erases the others', () => {
  it('scenario/oracle: one Gap, several Unknowns, one satisfied — all seven answers served, each with its own value; count and per-answer comparison', () => {
    const set = computeShapeAnswers(PROJECT, EVALUATION, mixedInputs());
    expect(set.answers).toHaveLength(7); // bounded: seven entries
    const served = set.answers.map((answer) => ({
      name: answer.name,
      value: answer.render.value,
    }));
    expect(served).toEqual(EXPECTED);
  });

  it('falsifier: no answer is omitted because a sibling is negative or Unknown — the name set is identical across the mixed set and an all-Unknown set', () => {
    const mixed = computeShapeAnswers(PROJECT, EVALUATION, mixedInputs());
    const bare = computeShapeAnswers(PROJECT, EVALUATION, {});
    expect(mixed.answers.map((answer) => answer.name)).toEqual(
      bare.answers.map((answer) => answer.name),
    );
    expect(bare.answers).toHaveLength(7);
  });

  it('falsifier: no answer is blanked — every served answer in the mixed set carries a non-empty value and a non-empty fact set; sweep over all seven', () => {
    const set = computeShapeAnswers(PROJECT, EVALUATION, mixedInputs());
    expect(set.answers).toHaveLength(7); // denominator disclosed
    for (const answer of set.answers) {
      expect(typeof answer.render.value, answer.name).toBe('string');
      expect(answer.render.value.length, answer.name).toBeGreaterThan(0);
      expect(answer.factSet.facts.length, answer.name).toBeGreaterThan(0);
    }
  });

  it('falsifier: the Gap does not degrade the satisfied sibling\'s rendering — Registered\'s render and facts are byte-identical with and without the sibling Gap', () => {
    const withGap = computeShapeAnswers(PROJECT, EVALUATION, mixedInputs());
    const withoutGap = computeShapeAnswers(PROJECT, EVALUATION, {
      ...mixedInputs(),
      links: [{ link: 'overview->spec', resolved: true }],
    });
    expect(JSON.stringify(withGap.answers[0])).toBe(JSON.stringify(withoutGap.answers[0]));
  });
});
