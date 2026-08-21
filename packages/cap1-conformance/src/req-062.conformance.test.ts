import { describe, expect, it } from 'vitest';
import {
  assessCurrency,
  renderSuperseded,
  type CurrencyBoundDeclaration,
} from '@syzygy/cap1-core';

// CAP1-REQ-062 — Stale evidence cannot silently remain current or
// favourable (invariant).
//
// Case: every claim served for fixtures with (a) evidence older than
// its declared bound at the evaluation's as-of instant and (b) a claim
// class with no declared bound. Oracle: every out-of-bound claim serves
// `Unknown` reason #4 (`stale-beyond-currency-bound`); every
// unbounded-class claim serves `Unknown` reason #3
// (`no-currency-bound-declared`) — string comparison per claim, the
// expected spellings hard-coded below from RFC2-24, never imported from
// the implementation — and no served value differs between two reads of
// one evaluation at different wall-clock times. Falsifier: stale
// evidence supporting a favourable answer, an unbounded class rendering
// favourably, or an answer flipping with no new evaluation.

const DAY_MS = 24 * 60 * 60 * 1000;
const AS_OF = '2026-08-21T00:00:00Z';

const BOUNDS: readonly CurrencyBoundDeclaration[] = [
  { claimClass: 'shape-claims', maxAgeMs: 7 * DAY_MS },
];

// Fixture (a): claims whose evidence exceeds the declared 7-day bound
// at the as-of instant, and fixture (b): claims of a class with no
// declared bound. The served claim set per fixture is enumerated in
// full — the sweep's denominators.
const STALE_FIXTURE = [
  { claimClass: 'shape-claims', observedAt: '2026-08-01T00:00:00Z' }, // 20 days old
  { claimClass: 'shape-claims', observedAt: '2026-08-13T23:59:59Z' }, // just past 7 days
  { claimClass: 'shape-claims', observedAt: '2020-01-01T00:00:00Z' }, // years old
] as const;

const UNBOUNDED_FIXTURE = [
  { claimClass: 'undeclared-class', observedAt: '2026-08-20T23:59:00Z' }, // one minute old
  { claimClass: 'undeclared-class', observedAt: AS_OF }, // zero age
] as const;

describe('CAP1-REQ-062 — stale evidence cannot silently remain current or favourable', () => {
  it('scenario: evidence beyond its declared bound renders Unknown with reason `stale-beyond-currency-bound` — swept over the whole fixture', () => {
    expect(STALE_FIXTURE.length).toBe(3); // denominator disclosed
    for (const claim of STALE_FIXTURE) {
      const served = assessCurrency(claim.claimClass, { observedAt: claim.observedAt }, BOUNDS, AS_OF);
      expect(served.state).toBe('stale');
      if (served.state === 'stale') {
        // Expected spellings hard-coded from the closed vocabulary.
        expect(served.label).toBe('Unknown');
        expect(served.reason).toBe('stale-beyond-currency-bound');
        expect(served.freshness).toBe('stale');
      }
    }
  });

  it('a claim class with no declared currency bound renders Unknown with reason `no-currency-bound-declared` — however fresh the evidence', () => {
    expect(UNBOUNDED_FIXTURE.length).toBe(2); // denominator disclosed
    for (const claim of UNBOUNDED_FIXTURE) {
      const served = assessCurrency(claim.claimClass, { observedAt: claim.observedAt }, BOUNDS, AS_OF);
      expect(served.state).toBe('no-bound-declared');
      if (served.state === 'no-bound-declared') {
        expect(served.label).toBe('Unknown');
        expect(served.reason).toBe('no-currency-bound-declared');
      }
    }
  });

  it('evidence within its declared bound is current — the favourable arm exists and is reachable only through a declared, satisfied bound', () => {
    const served = assessCurrency('shape-claims', { observedAt: '2026-08-20T00:00:00Z' }, BOUNDS, AS_OF);
    expect(served.state).toBe('current');
    if (served.state === 'current') {
      expect(served.freshness).toBe('fresh');
      expect(served.evidenceAgeMs).toBe(DAY_MS);
      expect(served.boundMs).toBe(7 * DAY_MS);
    }
  });

  it('the bound is judged at the as-of instant: age exactly at the bound is current, one millisecond past it is stale', () => {
    // observedAt exactly 7 days before AS_OF.
    const atBound = assessCurrency('shape-claims', { observedAt: '2026-08-14T00:00:00Z' }, BOUNDS, AS_OF);
    expect(atBound.state).toBe('current');
    // One millisecond older.
    const pastBound = assessCurrency('shape-claims', { observedAt: '2026-08-13T23:59:59.999Z' }, BOUNDS, AS_OF);
    expect(pastBound.state).toBe('stale');
  });

  it('no served value differs between two reads of one evaluation — the whole claim set, repeated, is byte-identical', () => {
    const readAll = () =>
      JSON.stringify(
        [...STALE_FIXTURE, ...UNBOUNDED_FIXTURE].map((claim) =>
          assessCurrency(claim.claimClass, { observedAt: claim.observedAt }, BOUNDS, AS_OF),
        ),
      );
    // Two reads of the same identified evaluation (same as-of instant),
    // performed at different wall-clock moments of this test run: the
    // function takes no clock, so the answer can change only through a
    // new identified evaluation.
    const first = readAll();
    const second = readAll();
    expect(second).toBe(first);
  });

  it('staleness of a superseded observation is visible on the primary surface', () => {
    const record = { claimClass: 'shape-claims', observedAt: '2026-08-01T00:00:00Z', value: 'satisfied' };
    const rendered = renderSuperseded(record);
    expect(rendered.freshness).toBe('superseded');
    expect(rendered.visibleOn).toBe('primary-surface');
    // The record itself is carried untouched — immutable once recorded.
    expect(rendered.record).toBe(record);
  });

  it('falsifier: stale evidence never supports a current or favourable answer', () => {
    for (const claim of STALE_FIXTURE) {
      const served = assessCurrency(claim.claimClass, { observedAt: claim.observedAt }, BOUNDS, AS_OF);
      expect(served.state).not.toBe('current');
    }
  });

  it('falsifier: an unbounded claim class never renders favourably, even with zero-age evidence', () => {
    const served = assessCurrency('undeclared-class', { observedAt: AS_OF }, BOUNDS, AS_OF);
    expect(served.state).not.toBe('current');
  });

  it('falsifier: future-dated evidence cannot count as current — it is not in the evaluation\'s past at all', () => {
    // Evidence observed AFTER the as-of instant, within the bound by
    // absolute distance: the favourable arm must stay unreachable.
    const served = assessCurrency('shape-claims', { observedAt: '2026-08-22T00:00:00Z' }, BOUNDS, AS_OF);
    expect(served.state).not.toBe('current');
    expect(served.state).toBe('stale');
    if (served.state === 'stale') {
      expect(served.label).toBe('Unknown');
      expect(served.reason).toBe('stale-beyond-currency-bound');
      expect(served.basis).toBe('future-dated-instant');
    }
  });

  it('fail-closed: an unreadable evidence instant cannot count as current, and says so machine-readably', () => {
    const served = assessCurrency('shape-claims', { observedAt: 'not-an-instant' }, BOUNDS, AS_OF);
    expect(served.state).toBe('stale');
    if (served.state === 'stale') {
      expect(served.reason).toBe('stale-beyond-currency-bound');
      expect(served.basis).toBe('unreadable-instant');
    }
  });
});
