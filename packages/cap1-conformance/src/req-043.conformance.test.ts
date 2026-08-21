import { describe, expect, it } from 'vitest';
import {
  compareRenderings,
  type ChannelDisclosure,
  type EvaluationIdentity,
  type ServedFact,
} from '@syzygy/cap1-core';

// CAP1-REQ-043 — A parity disagreement is visible and fails;
// presentation precedence never resolves it (prohibition).
//
// Case: every pair of renderings over one (selection, evaluation,
// context); sweep: the requirement-041/042 comparisons — denominator:
// the compared pair set. Oracle: zero disagreements across the compared
// set; any found disagreement is a failure, whatever either rendering
// claims. Oracle independence: disagreement is a relation between two
// served outputs; no implementation judgment is consulted. Falsifier:
// two conforming-looking renderings disagreeing on one fact while the
// system treats one as authoritative presentation.

const EVALUATION: EvaluationIdentity = {
  snapshot: 'snap-2026-08-21-x',
  asOf: '2026-08-21T00:00:00Z',
};

function disclosure(facts: readonly ServedFact[]): ChannelDisclosure {
  return {
    selection: 'shape-answer:Traceable@prj-x',
    evaluation: EVALUATION,
    scenarioContext: 'base',
    declaredFilters: {},
    facts,
  };
}

const OBSERVED_FACT: ServedFact = {
  name: 'answer',
  value: 'satisfied',
  epistemic: { label: 'Observed' },
};

describe('CAP1-REQ-043 — a parity disagreement is visible and fails', () => {
  it('scenario: a label disagreement at one evaluation fails parity; neither value is silently preferred', () => {
    const human = disclosure([OBSERVED_FACT]);
    const machine = disclosure([
      { name: 'answer', value: 'satisfied', epistemic: { label: 'Inferred' } },
    ]);
    const comparison = compareRenderings(human, machine);
    if (comparison.comparable !== true || comparison.verdict !== 'parity-defect') {
      throw new Error('the disagreement must fail parity');
    }
    // The defect renders as a disagreement carrying BOTH values —
    // hard-coded spellings, neither marked authoritative.
    expect(comparison.renders).toBe('disagreement');
    expect(comparison.disagreements).toEqual([
      { factName: 'answer', facet: 'label', inFirst: 'Observed', inSecond: 'Inferred' },
    ]);
  });

  it('no presentation precedence: the defect result has no field naming a winner, and the verdict is symmetric', () => {
    const a = disclosure([OBSERVED_FACT]);
    const b = disclosure([
      { name: 'answer', value: 'Gap', epistemic: { label: 'Observed' } },
    ]);
    const forward = compareRenderings(a, b);
    const backward = compareRenderings(b, a);
    if (forward.comparable !== true || forward.verdict !== 'parity-defect') {
      throw new Error('forward must be a defect');
    }
    if (backward.comparable !== true || backward.verdict !== 'parity-defect') {
      throw new Error('backward must be a defect');
    }
    // The result's whole field set, enumerated: nothing names a
    // preferred rendering, a resolution, or an authoritative channel.
    expect(Object.keys(forward).sort()).toEqual([
      'comparable',
      'disagreements',
      'renders',
      'verdict',
    ]);
    // Order of arguments never turns a defect into agreement.
    expect(backward.verdict).toBe('parity-defect');
  });

  it("an entity-existence disagreement fails — a fact present in one rendering's disclosure, absent from the other", () => {
    const comparison = compareRenderings(disclosure([OBSERVED_FACT]), disclosure([]));
    if (comparison.comparable !== true || comparison.verdict !== 'parity-defect') {
      throw new Error('the omission must fail');
    }
    expect(
      comparison.disagreements.some(
        (disagreement) => disagreement.facet === 'existence' && disagreement.factName === 'answer',
      ),
    ).toBe(true);
  });

  it('a reason disagreement fails — carrying the primary alone drops the marked secondary', () => {
    const full = disclosure([
      {
        name: 'answer',
        value: 'Unknown',
        epistemic: {
          label: 'Unknown',
          reasons: { primary: 'missing-evidence', secondary: ['unconsented-source-or-provider'] },
        },
      },
    ]);
    const dropped = disclosure([
      {
        name: 'answer',
        value: 'Unknown',
        epistemic: { label: 'Unknown', reasons: { primary: 'missing-evidence', secondary: [] } },
      },
    ]);
    const comparison = compareRenderings(full, dropped);
    if (comparison.comparable !== true || comparison.verdict !== 'parity-defect') {
      throw new Error('the dropped secondary must fail');
    }
    expect(comparison.disagreements[0]).toEqual({
      factName: 'answer',
      facet: 'reason',
      inFirst: 'primary:missing-evidence; secondary:[unconsented-source-or-provider]',
      inSecond: 'primary:missing-evidence; secondary:[]',
    });
  });

  it('a freshness disagreement fails', () => {
    const fresh = disclosure([
      { name: 'answer', value: 'satisfied', epistemic: { label: 'Observed', freshness: 'fresh' } },
    ]);
    const stale = disclosure([
      { name: 'answer', value: 'satisfied', epistemic: { label: 'Observed', freshness: 'stale' } },
    ]);
    const comparison = compareRenderings(fresh, stale);
    if (comparison.comparable !== true || comparison.verdict !== 'parity-defect') {
      throw new Error('the freshness split must fail');
    }
    expect(comparison.disagreements[0]).toEqual({
      factName: 'answer',
      facet: 'freshness',
      inFirst: 'fresh',
      inSecond: 'stale',
    });
  });

  it('a count disagreement over one declared scope fails — even when name-keyed lookups would collapse it', () => {
    // The second rendering serves the same-named fact twice: every
    // per-name comparison agrees, so only the count facet can catch it.
    const comparison = compareRenderings(
      disclosure([OBSERVED_FACT]),
      disclosure([OBSERVED_FACT, OBSERVED_FACT]),
    );
    if (comparison.comparable !== true || comparison.verdict !== 'parity-defect') {
      throw new Error('the count split must fail');
    }
    expect(comparison.disagreements[0]).toEqual({
      factName: '(fact count over the declared scope)',
      facet: 'count',
      inFirst: '1',
      inSecond: '2',
    });
  });

  it('lawful: a disclosed filter difference is aggregation/finer detail, never a contradiction — and never silent parity', () => {
    const full = disclosure([OBSERVED_FACT]);
    const filtered: ChannelDisclosure = {
      ...disclosure([]),
      declaredFilters: { repository: 'repo-x-01' },
    };
    // Content differs, but the difference travels as a DECLARED filter
    // difference (RFC6-23): the pair is not an equivalent pair, so it
    // neither passes as parity nor fails as contradiction.
    expect(compareRenderings(full, filtered)).toEqual({
      comparable: false,
      basis: 'declared-filter-difference',
    });
  });

  it('two renderings at different evaluations are not one pair — no cross-evaluation contradiction is minted', () => {
    const later: ChannelDisclosure = {
      ...disclosure([OBSERVED_FACT]),
      evaluation: { snapshot: 'snap-2026-08-22-x', asOf: '2026-08-22T00:00:00Z' },
    };
    expect(compareRenderings(disclosure([]), later)).toEqual({
      comparable: false,
      basis: 'different-evaluation',
    });
  });

  it('agreement is judged from the served outputs alone — identical disclosures are parity with the compared count disclosed', () => {
    const comparison = compareRenderings(disclosure([OBSERVED_FACT]), disclosure([OBSERVED_FACT]));
    expect(comparison).toEqual({ comparable: true, verdict: 'parity', comparedFacts: 1 });
  });
});
