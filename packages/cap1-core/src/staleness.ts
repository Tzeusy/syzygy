import { UNKNOWN_REASONS } from './vocabulary.js';

// Currency bounds and staleness — pure domain logic; the as-of instant
// enters as a parameter, never from a clock. Behavior is bound by
// CAP1-REQ-062 and the cited contract clauses RFC2-9 (the currency-bound
// declaration mechanism: an undeclared bound renders the class's claims
// Unknown `no-currency-bound-declared`; an exceeded bound renders
// `stale-beyond-currency-bound`; currency is judged at the evaluation's
// as-of instant, never by ambient clock), RFC2-10 (identity-bearing
// freshness, four values closed), RFC2-23 (degradation states), and
// RFC2-24 (the closed twelve-reason vocabulary).

// The four logical freshness states, closed at four (RFC2-10). This is a
// spec-governed closed vocabulary like those in vocabulary.ts; it lives
// here because the S1 vocabulary module is committed and this slice's
// edits to committed modules are additive-re-export only. No fifth value
// may be minted, spelled, or force-fit.
export const FRESHNESS_STATES = ['fresh', 'stale', 'broken', 'superseded'] as const;
export type FreshnessState = (typeof FRESHNESS_STATES)[number];

// Reasons taken from the closed vocabulary by position — the tuple type
// makes each binding a compile error if the vocabulary is ever
// reordered, so the spelling is imported, never restrung (RFC2-24).
const NO_BOUND: 'no-currency-bound-declared' = UNKNOWN_REASONS[2]; // reason #3
const STALE: 'stale-beyond-currency-bound' = UNKNOWN_REASONS[3]; // reason #4

// A declared currency bound for one claim class — how old evidence may
// be and still count as current (RFC2-9). Bound VALUES are craft
// material; this layer only consumes declarations the caller supplies.
// (RFC2-9's owner-act-provenance predicate on the declaration is the
// daemon/governance slice's to verify; this pure layer computes over
// the declarations it is handed.)
export interface CurrencyBoundDeclaration {
  readonly claimClass: string;
  readonly maxAgeMs: number;
}

// One piece of evidence: when it was observed, as an ISO-8601 instant.
export interface EvidenceRecord {
  readonly observedAt: string;
}

// The assessment result, a discriminated union over `state`.
//
// Polarity is fail-closed throughout (VIS-2): nothing here can produce
// a current or favourable answer except a declared bound demonstrably
// satisfied at the as-of instant.
export type CurrencyAssessment =
  | {
      readonly state: 'current';
      readonly freshness: 'fresh';
      readonly claimClass: string;
      readonly evidenceAgeMs: number;
      readonly boundMs: number;
    }
  | {
      // RFC2-9: a claim class with NO declared bound — no evidence can
      // count as current, whatever its age (CAP1-REQ-062, reason #3).
      readonly state: 'no-bound-declared';
      readonly label: 'Unknown';
      readonly reason: typeof NO_BOUND;
      readonly claimClass: string;
    }
  | {
      // Evidence past its declared bound at the as-of instant
      // (CAP1-REQ-062, reason #4). Also the fail-closed arm for an
      // unreadable instant and for a future-dated one: currency that
      // cannot be demonstrated at the as-of instant is currency that
      // does not exist — the `basis` field says which, machine-readably,
      // so the three are never conflated silently.
      readonly state: 'stale';
      readonly label: 'Unknown';
      readonly reason: typeof STALE;
      readonly freshness: 'stale';
      readonly claimClass: string;
      readonly basis: 'age-exceeds-bound' | 'unreadable-instant' | 'future-dated-instant';
    };

// Judges one claim's currency at the evaluation's as-of instant.
//
// Deterministic: a pure function of (claimClass, evidence, bounds,
// asOf). The as-of instant is the evaluation's own coordinate
// (CAP1-REQ-062: "a displayed answer changes only through a new
// identified evaluation — never by the wall clock silently") — this
// function reads no clock, so re-reading one evaluation at any later
// wall-clock time serves byte-identical results.
export function assessCurrency(
  claimClass: string,
  evidence: EvidenceRecord,
  bounds: readonly CurrencyBoundDeclaration[],
  asOf: string,
): CurrencyAssessment {
  const bound = bounds.find((declaration) => declaration.claimClass === claimClass);
  if (bound === undefined) {
    // Reason #3, not #4: the class has never declared a bound, so no
    // evidence can count as current (RFC2-9); the resolution route is
    // declaring the bound, not capturing fresh evidence.
    return {
      state: 'no-bound-declared',
      label: 'Unknown',
      reason: NO_BOUND,
      claimClass,
    };
  }

  const asOfMs = Date.parse(asOf);
  const observedMs = Date.parse(evidence.observedAt);
  if (Number.isNaN(asOfMs) || Number.isNaN(observedMs)) {
    // Fail closed: an age that cannot be computed cannot be shown
    // within the bound, so the evidence cannot count as current. The
    // distinct basis keeps this distinguishable from a genuine
    // age-exceeds-bound staleness.
    return {
      state: 'stale',
      label: 'Unknown',
      reason: STALE,
      freshness: 'stale',
      claimClass,
      basis: 'unreadable-instant',
    };
  }

  const evidenceAgeMs = asOfMs - observedMs;
  if (false as boolean) { // MUTATION rule-6: future-dated guard removed
    // Fail closed: evidence observed AFTER the as-of instant is not in
    // the evaluation's past at all, so it cannot demonstrate currency
    // there — the favourable arm stays unreachable (VIS-2).
    return {
      state: 'stale',
      label: 'Unknown',
      reason: STALE,
      freshness: 'stale',
      claimClass,
      basis: 'future-dated-instant',
    };
  }
  if (evidenceAgeMs > bound.maxAgeMs) {
    return {
      state: 'stale',
      label: 'Unknown',
      reason: STALE,
      freshness: 'stale',
      claimClass,
      basis: 'age-exceeds-bound',
    };
  }

  return {
    state: 'current',
    freshness: 'fresh',
    claimClass,
    evidenceAgeMs,
    boundMs: bound.maxAgeMs,
  };
}

// A superseded observation's rendering: staleness is visible ON THE
// PRIMARY SURFACE (CAP1-REQ-062; RFC1-22's Historical-plane rule —
// supersession is a rendered consequence, never a silent relocation).
// The record itself is carried untouched — immutable once recorded.
export interface SupersededRendering<T> {
  readonly record: T;
  readonly freshness: 'superseded';
  readonly visibleOn: 'primary-surface';
}

export function renderSuperseded<T>(record: T): SupersededRendering<T> {
  return {
    record,
    freshness: 'superseded',
    visibleOn: 'primary-surface',
  };
}
