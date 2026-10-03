import { describe, expect, it } from 'vitest';

import { claimStateDelta, claimStateDeltaBand, claimStatesOf, type ClaimState, type DeltaEvaluation } from './claim-state-delta.js';
import type { ChallengeState } from './project-shape-model.js';

// M12 slice 2 (syzygy-dov.12.1). Expected values are hard-coded literals.
const OBSERVED: ClaimState = { epistemic: { label: 'Observed', tier: 'report-fact', freshness: 'fresh' }, challenge: 'unchallenged' };
const UNKNOWN: ClaimState = { epistemic: { label: 'Unknown', reasons: { primary: 'missing-evidence', secondary: [] }, tier: 'report-fact' }, challenge: 'unchallenged' } as unknown as ClaimState;
const CHALLENGED: ClaimState = { ...OBSERVED, challenge: 'challenged' as ChallengeState };
const PREVIOUS: DeltaEvaluation = { identity: 'snap-a|observed:2026-10-01T00:00:00Z', snapshotLabel: 'snap-a', inputsDigest: 'digest-a', asOf: '2026-10-01T00:00:00Z' };
const CURRENT: DeltaEvaluation = { identity: 'snap-b|observed:2026-10-02T00:00:00Z', snapshotLabel: 'snap-b', inputsDigest: 'digest-b', asOf: '2026-10-02T00:00:00Z' };

function states(entries: readonly (readonly [string, ClaimState])[]) {
  return claimStatesOf(entries.map(([claimId, state]) => ({ claimId, ...state }))).states;
}

describe('claim-state delta', () => {
  it('names both evaluations and reports added, removed, tuple-changed and unchanged over one denominator', () => {
    const delta = claimStateDelta(
      { evaluation: PREVIOUS, states: states([['claim:gone', OBSERVED], ['claim:moved', UNKNOWN], ['claim:same', OBSERVED], ['claim:challenged', OBSERVED]]) },
      { evaluation: CURRENT, states: states([['claim:new', OBSERVED], ['claim:moved', OBSERVED], ['claim:same', OBSERVED], ['claim:challenged', CHALLENGED], ['claim:same', OBSERVED]]) },
    );
    expect(delta).toEqual({
      claimId: 'claim:claim-state-delta',
      evaluation: 'snap-b|observed:2026-10-02T00:00:00Z',
      previousEvaluation: { identity: 'snap-a|observed:2026-10-01T00:00:00Z', snapshotLabel: 'snap-a', inputsDigest: 'digest-a', asOf: '2026-10-01T00:00:00Z' },
      currentEvaluation: { identity: 'snap-b|observed:2026-10-02T00:00:00Z', snapshotLabel: 'snap-b', inputsDigest: 'digest-b', asOf: '2026-10-02T00:00:00Z' },
      added: ['claim:new'],
      removed: ['claim:gone'],
      tupleChanged: [
        { claimId: 'claim:challenged', before: OBSERVED, after: CHALLENGED },
        { claimId: 'claim:moved', before: UNKNOWN, after: OBSERVED },
      ],
      unchanged: 1,
      denominator: { previous: 4, current: 4, union: 5 },
    });
  });

  it('counts a repeated identity once per occurrence and refuses an unequal repeat', () => {
    expect(claimStatesOf([{ claimId: 'claim:x', ...OBSERVED }, { claimId: 'claim:x', ...OBSERVED }])).toMatchObject({ claimCount: 2, identityCount: 1 });
    expect(() => claimStatesOf([{ claimId: 'claim:x', ...OBSERVED }, { claimId: 'claim:x', ...UNKNOWN }])).toThrow('claim claim:x occurs twice with different states');
  });

  it('refuses a delta of one evaluation against itself', () => {
    expect(() => claimStateDelta({ evaluation: CURRENT, states: new Map() }, { evaluation: CURRENT, states: new Map() })).toThrow('a delta needs two evaluations');
  });

  it('caps the band at its declared row count and counts the remainder (cap + N)', () => {
    const previous = states(Array.from({ length: 30 }, (_, i) => [`claim:p${String(i).padStart(2, '0')}`, UNKNOWN] as const));
    const current = states(Array.from({ length: 30 }, (_, i) => [`claim:p${String(i).padStart(2, '0')}`, OBSERVED] as const));
    const delta = claimStateDelta({ evaluation: PREVIOUS, states: previous }, { evaluation: CURRENT, states: current });
    const band = claimStateDeltaBand(delta, 25);
    expect(band.rows).toHaveLength(25);
    expect(band.remainder).toBe(5);
    expect(band.rows[24]).toMatchObject({ kind: 'tuple-changed', change: { claimId: 'claim:p24' } });
    expect(claimStateDeltaBand(delta, 30).remainder).toBe(0);
  });
});
