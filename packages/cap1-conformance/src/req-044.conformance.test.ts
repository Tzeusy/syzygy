import { describe, expect, it } from 'vitest';
import {
  aggregate,
  deterministicLayer,
  explainAnswer,
  type ServedFact,
} from '@syzygy/cap1-core';

// CAP1-REQ-044 — A missing explanation is never replaced by an
// optimistic summary (prohibition).
//
// Case: every served answer whose explanation cannot be computed, and
// every served aggregate; sweep: for a fixture with an uncomputable
// explanation, enumerate the served values and aggregates —
// denominator: the enumerated set. Oracle: absent explanation renders
// Unknown-with-reason; every aggregate carries count and
// per-label/per-reason composition and expands. Oracle independence:
// the fixture controls the absence; the composition obligation is the
// accepted contract's (RFC6-17). Falsifier: a green or favourable
// summary over facts that are absent, or an aggregate hiding its
// Unknowns.

// The fixture's aggregable members: several Unknown answers plus mixed
// company.
const UNKNOWN_MISSING: ServedFact = {
  name: 'answer:Human-understandable',
  value: 'Unknown',
  epistemic: { label: 'Unknown', reasons: { primary: 'missing-evidence', secondary: [] } },
};
const UNKNOWN_UNCONSENTED: ServedFact = {
  name: 'answer:Observable',
  value: 'Unknown',
  epistemic: {
    label: 'Unknown',
    reasons: { primary: 'unconsented-source-or-provider', secondary: ['missing-evidence'] },
  },
};
const UNKNOWN_DEFERRED: ServedFact = {
  name: 'answer:Mission-ready',
  value: 'not evaluated',
  epistemic: { label: 'Unknown', basis: 'deferred' },
};
const OBSERVED_SATISFIED: ServedFact = {
  name: 'answer:Registered',
  value: 'satisfied',
  epistemic: { label: 'Observed', tier: 'gate-backed', freshness: 'fresh' },
};

describe('CAP1-REQ-044 — a missing explanation is never replaced by an optimistic summary', () => {
  it('an uncomputable explanation renders the unavailability: Unknown with its reason, byte for byte', () => {
    const serving = explainAnswer(undefined);
    // The whole served object, hard-coded: nothing summary-shaped can
    // hide in an unchecked field.
    expect(deterministicLayer(serving)).toBe(
      '{"label":"Unknown","reasons":{"primary":"missing-evidence","secondary":[]},"served":false,"value":"Unknown"}',
    );
  });

  it('the unavailable arm carries a caller-supplied reason verbatim', () => {
    const serving = explainAnswer(undefined, ['execution-blocked']);
    if (serving.served) throw new Error('must not serve');
    expect(serving.value).toBe('Unknown');
    expect(serving.reasons.primary).toBe('execution-blocked');
  });

  it('falsifier: the unavailable arm has no field that could carry a summary, default, or aggregate', () => {
    const serving = explainAnswer(undefined);
    // The full key set, enumerated — no summary field, no factSet, no
    // favourable spelling anywhere.
    expect(Object.keys(serving).sort()).toEqual(['label', 'reasons', 'served', 'value']);
    if (serving.served) throw new Error('must not serve');
    expect(serving.value).not.toBe('satisfied');
  });

  it('scenario: several Unknown answers aggregate with membership count, per-reason composition, and expansion to members', () => {
    const rendering = aggregate([UNKNOWN_MISSING, UNKNOWN_UNCONSENTED, UNKNOWN_DEFERRED]);
    expect(rendering.composition.membershipCount).toBe(3);
    // Per-PRIMARY-reason composition (RFC6-17): one member contributes
    // exactly one; the deferred posture contributes none.
    expect(rendering.composition.byPrimaryReason).toEqual([
      { reason: 'missing-evidence', count: 1 },
      { reason: 'unconsented-source-or-provider', count: 1 },
    ]);
    // Expansion to members: the members themselves are served.
    expect(rendering.members).toEqual([UNKNOWN_MISSING, UNKNOWN_UNCONSENTED, UNKNOWN_DEFERRED]);
  });

  it('an aggregate never hides its Unknowns — all three labels are disclosed with computed counts', () => {
    const rendering = aggregate([OBSERVED_SATISFIED, UNKNOWN_MISSING, UNKNOWN_UNCONSENTED]);
    expect(rendering.composition.byLabel).toEqual([
      { label: 'Observed', count: 1 },
      { label: 'Inferred', count: 0 },
      { label: 'Unknown', count: 2 },
    ]);
  });

  it('secondary Unknown annotations are disclosed separately, never folded into the primary counts', () => {
    const rendering = aggregate([UNKNOWN_UNCONSENTED]);
    // The primary count sees ONLY the primary; the secondary travels in
    // its own disclosure (RFC6-14/17 — folding them would let two
    // conforming surfaces disagree on reason totals).
    expect(rendering.composition.byPrimaryReason).toEqual([
      { reason: 'unconsented-source-or-provider', count: 1 },
    ]);
    expect(rendering.composition.secondaryReasons).toEqual([
      { reason: 'missing-evidence', count: 1 },
    ]);
  });

  it('the aggregate carries no epistemic state of its own — its whole field set is composition and members', () => {
    const rendering = aggregate([UNKNOWN_MISSING, OBSERVED_SATISFIED]);
    expect(Object.keys(rendering).sort()).toEqual(['composition', 'members']);
    expect(Object.keys(rendering.composition).sort()).toEqual([
      'byFreshness',
      'byLabel',
      'byPrimaryReason',
      'byTier',
      'membershipCount',
      'secondaryReasons',
    ]);
  });

  it('tier and freshness composition travel where members carry them', () => {
    const rendering = aggregate([OBSERVED_SATISFIED, UNKNOWN_MISSING]);
    expect(rendering.composition.byTier).toEqual([{ tier: 'gate-backed', count: 1 }]);
    expect(rendering.composition.byFreshness).toEqual([{ freshness: 'fresh', count: 1 }]);
  });

  it('an empty aggregate disclosed its zero denominator — never a favourable blank', () => {
    const rendering = aggregate([]);
    expect(rendering.composition.membershipCount).toBe(0);
    expect(rendering.composition.byLabel).toEqual([
      { label: 'Observed', count: 0 },
      { label: 'Inferred', count: 0 },
      { label: 'Unknown', count: 0 },
    ]);
    expect(rendering.members).toEqual([]);
  });
});
