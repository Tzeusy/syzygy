// Closed vocabularies. Every spelling below is a conformance item carried
// verbatim from the adopted specification and its governing contracts;
// changing any spelling here without the spec's amendment path (CC-REV-2)
// is a defect, not a refactor.

// The seven project-shape answer names, exact and ordered (CAP1-REQ-030,
// vocabulary authored there per SDR-36).
export const FACET_NAMES = [
  'Registered',
  'Shape present',
  'Human-understandable',
  'Observable',
  'Traceable',
  'Mission-ready',
  'Reconciled',
] as const;
export type FacetName = (typeof FACET_NAMES)[number];

// The three-spelling answer domain under the two-term rule
// (CAP1-REQ-030/034; SDR-35): `satisfied` / `Gap` / `Unknown`, closed.
export const ANSWER_VALUES = ['satisfied', 'Gap', 'Unknown'] as const;
export type AnswerValue = (typeof ANSWER_VALUES)[number];

// The twelve Unknown reasons, closed at twelve by owner decision A5
// (RFC2-24, rendering-vocabularies.md). Order and spelling are the
// clause's own; no thirteenth reason may be minted.
export const UNKNOWN_REASONS = [
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
export type UnknownReason = (typeof UNKNOWN_REASONS)[number];

// The four-value per-repository discoverability domain (CAP1-REQ-050;
// RFC7-40), carried verbatim on every rendering and machine answer.
export const DISCOVERABILITY_VALUES = [
  'yes',
  'no',
  'not-applicable',
  'Unknown',
] as const;
export type DiscoverabilityValue = (typeof DISCOVERABILITY_VALUES)[number];

// Mission-ready's deferred posture: three served coordinates, each
// verbatim (CAP1-REQ-036; SDR-36 rule 3). While the Mission contracts
// remain unaccepted this is the only thing the facet renders.
export const MISSION_READY_DEFERRED_POSTURE = {
  value: 'not evaluated',
  basis: 'deferred',
  label: 'Unknown',
} as const;
export type MissionReadyDeferredPosture = typeof MISSION_READY_DEFERRED_POSTURE;

// The three epistemic labels — exclusive and exhaustive (doctrine's
// three-label rule; VIS-2).
export const EPISTEMIC_LABELS = ['Observed', 'Inferred', 'Unknown'] as const;
export type EpistemicLabel = (typeof EPISTEMIC_LABELS)[number];
