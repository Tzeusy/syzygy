import type { EpistemicState } from '@syzygy/cap1-core';

import { canonicalJson } from './project-shape-manifest.js';
import type { ChallengeState, ProjectShape, ProjectShapeClaim } from './project-shape-model.js';

// The claim-state delta between two evaluations (M12 slice 2,
// syzygy-dov.12.1; P-79 Q3 and Q6). A claim of the current evaluation about
// two evaluations: it names both evaluation identities, compares the
// retained per-claim state (epistemic tuple and challenge state, field by
// field) and is never a freshness value — no wall clock is read here. Pure.

export interface ClaimState {
  readonly epistemic: EpistemicState;
  readonly challenge: ChallengeState;
}

export interface ClaimStates {
  readonly states: ReadonlyMap<string, ClaimState>;
  /** Claim objects, a repeated identity counted each time it occurs. */
  readonly claimCount: number;
  /** Distinct claim identities. */
  readonly identityCount: number;
}

/** Every claim the project shape carries with its own tuple. */
export function projectShapeClaims(shape: ProjectShape): readonly ProjectShapeClaim[] {
  if (shape.kind !== 'observed') return [shape.claim];
  return [
    shape.claim,
    ...shape.projectAccount.map((entry) => entry.claim),
    ...shape.sources.map((entry) => entry.claim),
    ...shape.items.map((entry) => entry.claim),
    ...Object.values(shape.classes).map((aggregate) => aggregate.claim),
    ...shape.facts.map((entry) => entry.claim),
  ];
}

function stateKey(state: ClaimState): string {
  return canonicalJson({ epistemic: state.epistemic, challenge: state.challenge });
}

/** Collapse claims to one state per identity. A repeated identity must carry
 * an equal state; an unequal repeat is refused, never silently collapsed. */
export function claimStatesOf(claims: readonly Pick<ProjectShapeClaim, 'claimId' | 'epistemic' | 'challenge'>[]): ClaimStates {
  const states = new Map<string, ClaimState>();
  for (const claim of claims) {
    const state: ClaimState = { epistemic: claim.epistemic, challenge: claim.challenge };
    const prior = states.get(claim.claimId);
    if (prior !== undefined && stateKey(prior) !== stateKey(state)) {
      throw new Error(`claim ${claim.claimId} occurs twice with different states`);
    }
    states.set(claim.claimId, state);
  }
  return { states, claimCount: claims.length, identityCount: states.size };
}

export interface DeltaEvaluation {
  /** The evaluation identity (snapshot plus observation instant). */
  readonly identity: string;
  readonly snapshotLabel: string;
  readonly inputsDigest: string;
  readonly asOf: string;
}

export interface ClaimStateChange {
  readonly claimId: string;
  readonly before: ClaimState;
  readonly after: ClaimState;
}

export interface ClaimStateDelta {
  readonly claimId: 'claim:claim-state-delta';
  /** The delta is a claim of the current evaluation. */
  readonly evaluation: string;
  readonly previousEvaluation: DeltaEvaluation;
  readonly currentEvaluation: DeltaEvaluation;
  readonly added: readonly string[];
  readonly removed: readonly string[];
  readonly tupleChanged: readonly ClaimStateChange[];
  readonly unchanged: number;
  readonly denominator: { readonly previous: number; readonly current: number; readonly union: number };
}

export function claimStateDelta(
  previous: { readonly evaluation: DeltaEvaluation; readonly states: ReadonlyMap<string, ClaimState> },
  current: { readonly evaluation: DeltaEvaluation; readonly states: ReadonlyMap<string, ClaimState> },
): ClaimStateDelta {
  if (previous.evaluation.identity === current.evaluation.identity) {
    throw new Error(`a delta needs two evaluations; both are ${current.evaluation.identity}`);
  }
  const added: string[] = [];
  const removed: string[] = [];
  const tupleChanged: ClaimStateChange[] = [];
  let unchanged = 0;
  for (const [claimId, after] of current.states) {
    const before = previous.states.get(claimId);
    if (before === undefined) added.push(claimId);
    else if (stateKey(before) !== stateKey(after)) tupleChanged.push({ claimId, before, after });
    else unchanged += 1;
  }
  for (const claimId of previous.states.keys()) if (!current.states.has(claimId)) removed.push(claimId);
  const byId = (a: string, b: string): number => (a < b ? -1 : a > b ? 1 : 0);
  return {
    claimId: 'claim:claim-state-delta',
    evaluation: current.evaluation.identity,
    previousEvaluation: previous.evaluation,
    currentEvaluation: current.evaluation,
    added: added.sort(byId),
    removed: removed.sort(byId),
    tupleChanged: tupleChanged.sort((a, b) => byId(a.claimId, b.claimId)),
    unchanged,
    denominator: { previous: previous.states.size, current: current.states.size, union: current.states.size + removed.length },
  };
}

/** The declared row cap of the rendered band (P-79 Q3). */
export const CLAIM_STATE_DELTA_BAND_CAP = 25;

export type ClaimStateDeltaRow =
  | { readonly kind: 'tuple-changed'; readonly change: ClaimStateChange }
  | { readonly kind: 'added'; readonly claimId: string }
  | { readonly kind: 'removed'; readonly claimId: string };

/** The band's rows, capped; the remainder is counted, never dropped. */
export function claimStateDeltaBand(delta: ClaimStateDelta, cap: number = CLAIM_STATE_DELTA_BAND_CAP): { readonly rows: readonly ClaimStateDeltaRow[]; readonly remainder: number } {
  const all: ClaimStateDeltaRow[] = [
    ...delta.tupleChanged.map((change) => ({ kind: 'tuple-changed' as const, change })),
    ...delta.added.map((claimId) => ({ kind: 'added' as const, claimId })),
    ...delta.removed.map((claimId) => ({ kind: 'removed' as const, claimId })),
  ];
  return { rows: all.slice(0, cap), remainder: Math.max(0, all.length - cap) };
}
