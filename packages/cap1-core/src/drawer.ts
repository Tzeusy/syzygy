import type { EvaluationIdentity } from './identity.js';
import {
  EPISTEMIC_LABELS,
  UNKNOWN_REASONS,
  type EpistemicLabel,
  type UnknownReason,
} from './vocabulary.js';
import { composeUnknownReasons, type UnknownReasonSet } from './facets.js';
import type { CoverageBoundary } from './coverage.js';
import type { FreshnessState } from './staleness.js';
import type { EpistemicState, RenderingTier } from './epistemic.js';
import type { AuthorityReference } from './authority.js';

// The "Why this answer?" explanation fact set and honest aggregation —
// pure domain logic, no I/O, no clock. Behavior is bound by CAP1-REQ-040
// and CAP1-REQ-044 and the cited contract clauses RFC6-18 (one drawer,
// one fact set per (selection, evaluation, scenario context); its
// public-facing name is "Why this answer?"; the full set is reachable
// from every surface and the human and machine paths receive the same
// facts), RFC6-19 (the drawer content classes — the closed class list
// this module's type mirrors; no field outside it is invented),
// RFC6-17 (any aggregate discloses its membership count and epistemic
// composition and supports expansion; per-Unknown-reason counts are over
// primary reasons only, with secondary annotations disclosed separately
// and never folded in), and RFC6-14 (an aggregate carries no epistemic
// state of its own — no aggregate-level label, tier, reason, or
// freshness).

// The literal public-facing name of the one fact set (RFC6-18;
// CAP1-REQ-040: "reachable from the human view under a literal name").
export const WHY_THIS_ANSWER = 'Why this answer?' as const;

// The six state planes, closed (RFC1-22's assignment; RFC6-19 class 1's
// "state plane each rendered fact belongs to").
export const STATE_PLANES = [
  'desired',
  'proposed',
  'observed',
  'inferred',
  'execution',
  'historical',
] as const;
export type StatePlane = (typeof STATE_PLANES)[number];

// The reconciliation chain state, values per RFC2-18 as read at the
// producing evaluation (RFC6-19 class 8(i)): an uncomputed
// reconciliation renders Unknown, never green.
export type ChainState =
  | 'merged'
  | 'reconciliation-pending'
  | `reconciled@${string}`
  | 'unsatisfied'
  | 'contradiction-raised'
  | `Unknown(${string})`;

// One open challenge, with its RFC2-13 lifecycle state carried never
// flattened (RFC6-19 class 6): `submitted` renders challenge-pending and
// suspends nothing; `admitted` suspends the claim.
export interface ChallengeDisclosure {
  readonly challengeId: string;
  readonly lifecycle: 'submitted' | 'admitted';
}

// One contradiction pending adjudication (RFC6-19 class 6).
export interface ContradictionDisclosure {
  readonly subject: string;
  readonly state: 'pending-adjudication';
}

// One related work item's normalized work state (RFC6-19 class 8(ii)):
// RFC8-12 is informative until RFC 0008 is accepted, so `normalizedState`
// is optional and its absence renders as absence — nothing is
// substituted for it. Never folded into the chain state, and never
// rendered as proof of satisfaction (work is never proof).
export interface RelatedWorkDisclosure {
  readonly workId: string;
  readonly normalizedState?: string | undefined;
}

// The explanation fact set for one answer, one per (selection,
// evaluation, scenario context) — CAP1-REQ-040's closed class list,
// mirrored field for field. Each class field is optional because the
// requirement scopes them "where applicable and warranted by the
// accepted drawer contract (RFC6-19)"; the three envelope coordinates
// and the evaluation identity are always present. NO other field
// exists on this type: a field outside the accepted contract's classes
// would be an invented fact (the requirement's own prohibition), and
// EXPLANATION_CLASSES below is the closed enumeration a per-class
// presence sweep runs over.
export interface ExplanationFactSet {
  readonly selection: string;
  readonly evaluation: EvaluationIdentity;
  readonly scenarioContext: string;
  // 1. Owning authority and its governing revision (RFC6-19 class 4).
  readonly owningAuthority?: AuthorityReference | undefined;
  // 2. Source or evidence revision (RFC6-19 class 3's evidence–revision
  //    binding).
  readonly sourceRevision?: string | undefined;
  // 3. State category — the state plane (RFC6-19 class 1; RFC1-22).
  readonly statePlane?: StatePlane | undefined;
  // 4. Evidence classification: label, tier, Unknown reason, freshness
  //    (RFC6-19 class 2, verbatim vocabulary).
  readonly evidenceClassification?: EpistemicState | undefined;
  // 5. Freshness of the governing claims (RFC2-10).
  readonly freshness?: FreshnessState | undefined;
  // 6. The Unknown reason or reasons — primary + marked secondaries
  //    (RFC2-24; RFC6-14).
  readonly unknownReasons?: UnknownReasonSet | undefined;
  // 7. The coverage and consent boundary (RFC6-19 class 7 — the union
  //    of executed coverage records and declared captured scopes;
  //    consent state travels inside the records).
  readonly coverageAndConsentBoundary?: CoverageBoundary | undefined;
  // 8. Active challenge state (RFC6-19 class 6; RFC2-13).
  readonly challengeState?: readonly ChallengeDisclosure[] | undefined;
  // 9. Active contradiction state (RFC6-19 class 6).
  readonly contradictionState?: readonly ContradictionDisclosure[] | undefined;
  // 10. Related work state (RFC6-19 class 8(ii)).
  readonly relatedWorkState?: readonly RelatedWorkDisclosure[] | undefined;
  // 11. Reconciliation state — the chain state (RFC6-19 class 8(i);
  //     RFC2-18).
  readonly reconciliationState?: ChainState | undefined;
}

// The closed class-field enumeration, for the per-class presence check
// (CAP1-REQ-040's oracle: "per-class presence check. Bounded: one fact
// set"). Evaluation identity is the twelfth listed class; it is a
// required field above, so the sweep below reports it present on every
// well-formed set.
export const EXPLANATION_CLASSES = [
  'owningAuthority',
  'sourceRevision',
  'statePlane',
  'evidenceClassification',
  'evaluation',
  'freshness',
  'unknownReasons',
  'coverageAndConsentBoundary',
  'challengeState',
  'contradictionState',
  'relatedWorkState',
  'reconciliationState',
] as const;
export type ExplanationClass = (typeof EXPLANATION_CLASSES)[number];

// Which of the closed classes this fact set carries. The sweep runs
// over EXPLANATION_CLASSES and nothing else — a field outside the
// enumeration is unreachable by construction of the type.
export function presentClasses(factSet: ExplanationFactSet): readonly ExplanationClass[] {
  return EXPLANATION_CLASSES.filter((cls) => factSet[cls] !== undefined);
}

// Every internal reference the fact set carries, enumerated so a
// checker can follow each one (CAP1-REQ-040's oracle: "each internal
// reference in it resolves ... resolvability is checked by following
// references"). External URLs are not minted here; everything listed is
// internal and must resolve (RFC6-20).
export function internalReferences(factSet: ExplanationFactSet): readonly string[] {
  const references: string[] = [];
  if (factSet.owningAuthority !== undefined) {
    references.push(factSet.owningAuthority.authority);
    references.push(factSet.owningAuthority.governingRevision);
  }
  if (factSet.sourceRevision !== undefined) {
    references.push(factSet.sourceRevision);
  }
  if (factSet.coverageAndConsentBoundary !== undefined) {
    for (const record of factSet.coverageAndConsentBoundary.records) {
      references.push(record.repositoryId);
      if (record.state === 'observed') {
        references.push(record.consent.recordId);
      }
    }
  }
  if (factSet.challengeState !== undefined) {
    for (const challenge of factSet.challengeState) {
      references.push(challenge.challengeId);
    }
  }
  if (factSet.relatedWorkState !== undefined) {
    for (const item of factSet.relatedWorkState) {
      references.push(item.workId);
    }
  }
  return references;
}

// Follows every internal reference through the caller's resolver and
// reports the remainder by name — fail-visible, never a boolean that
// swallows its denominator (verification rule 9: a claim of absence
// needs a sweep with a denominator).
export interface ReferenceResolution {
  readonly references: readonly string[];
  readonly unresolved: readonly string[];
  readonly allResolve: boolean;
}

export function resolveExplanationReferences(
  factSet: ExplanationFactSet,
  resolve: (reference: string) => boolean,
): ReferenceResolution {
  const references = internalReferences(factSet);
  const unresolved = references.filter((reference) => !resolve(reference));
  return { references, unresolved, allResolve: unresolved.length === 0 };
}

// --- Serving the explanation (CAP1-REQ-040 / CAP1-REQ-044) -----------

const MISSING_EVIDENCE: 'missing-evidence' = UNKNOWN_REASONS[1]; // reason #2
const UNKNOWN_LABEL: 'Unknown' = EPISTEMIC_LABELS[2];

// The serving result, a discriminated union over `served`. The
// unavailable arm's shape is deliberately incapable of carrying a
// summary, default, or aggregate: its only value field is the literal
// `Unknown` with its reasons (CAP1-REQ-044: "never a summary, default,
// or aggregate that reads more favourably than the missing facts would
// support"). No favourable spelling is representable in that arm.
export type ExplanationServing =
  | {
      readonly served: true;
      // The literal human-view name (RFC6-18); the fact set itself is
      // what the machine plane serves, in full (RFC6-13).
      readonly name: typeof WHY_THIS_ANSWER;
      readonly factSet: ExplanationFactSet;
    }
  | {
      readonly served: false;
      readonly value: typeof UNKNOWN_LABEL;
      readonly label: typeof UNKNOWN_LABEL;
      readonly reasons: UnknownReasonSet;
    };

// Serves one answer's explanation. An available fact set is served
// whole under the literal name; an unavailable one renders the
// unavailability — Unknown with its reason — and nothing else.
export function explainAnswer(
  factSet: ExplanationFactSet | undefined,
  unavailableReasons: readonly [UnknownReason, ...UnknownReason[]] = [MISSING_EVIDENCE],
): ExplanationServing {
  if (factSet === undefined) {
    return {
      served: false,
      value: UNKNOWN_LABEL,
      label: UNKNOWN_LABEL,
      reasons: composeUnknownReasons(unavailableReasons),
    };
  }
  return { served: true, name: WHY_THIS_ANSWER, factSet };
}

// --- Honest aggregation (CAP1-REQ-044; RFC6-17; RFC6-14) -------------

// What an aggregate member must carry to be aggregable: its epistemic
// state. Anything with an `epistemic` field (a ServedFact, an answer
// wrapper) qualifies.
export interface AggregateMember {
  readonly epistemic: EpistemicState;
}

export interface LabelCount {
  readonly label: EpistemicLabel;
  readonly count: number;
}
export interface ReasonCount {
  readonly reason: UnknownReason;
  readonly count: number;
}
export interface TierCount {
  readonly tier: RenderingTier;
  readonly count: number;
}
export interface FreshnessCount {
  readonly freshness: FreshnessState;
  readonly count: number;
}

// The disclosed composition (RFC6-17). All three labels are listed with
// computed counts over the disclosed denominator — an Unknown can never
// be hidden by omission, and a zero here is a computed claim over
// `membershipCount` members, never an assumption. Per-Unknown-reason
// counts are over PRIMARY reasons only — one member contributes exactly
// one — with secondary annotations disclosed separately and never
// folded in (RFC6-17's explicit rule; otherwise two conforming surfaces
// could disagree on reason totals, which RFC6-23 classes as a defect).
export interface AggregateComposition {
  readonly membershipCount: number;
  readonly byLabel: readonly LabelCount[];
  readonly byPrimaryReason: readonly ReasonCount[];
  readonly secondaryReasons: readonly ReasonCount[];
  readonly byTier: readonly TierCount[];
  readonly byFreshness: readonly FreshnessCount[];
}

// The aggregate rendering. Its field set is deliberately two fields:
// the composition and the members (expansion support, CAP1-REQ-044's
// oracle: "every aggregate carries count and per-label/per-reason
// composition and expands"). There is NO aggregate-level label, tier,
// reason, or freshness field — an aggregate carries no epistemic state
// of its own (RFC6-14), and none is representable here.
export interface AggregateRendering<T extends AggregateMember> {
  readonly composition: AggregateComposition;
  readonly members: readonly T[];
}

function countBy<K extends string>(keys: readonly K[]): readonly { key: K; count: number }[] {
  const counts = new Map<K, number>();
  for (const key of keys) {
    counts.set(key, (counts.get(key) ?? 0) + 1);
  }
  return [...counts.entries()].map(([key, count]) => ({ key, count }));
}

export function aggregate<T extends AggregateMember>(
  members: readonly T[],
): AggregateRendering<T> {
  const primaryReasons: UnknownReason[] = [];
  const secondaryReasons: UnknownReason[] = [];
  for (const member of members) {
    // A deferred-posture Unknown (SDR-36 rule 3) carries no reason from
    // the closed twelve — it counts toward the Unknown label and adds
    // nothing to the reason counts, which stay honest to their own
    // denominator.
    if (member.epistemic.label === 'Unknown' && 'reasons' in member.epistemic) {
      primaryReasons.push(member.epistemic.reasons.primary);
      secondaryReasons.push(...member.epistemic.reasons.secondary);
    }
  }
  return {
    composition: {
      membershipCount: members.length,
      byLabel: EPISTEMIC_LABELS.map((label) => ({
        label,
        count: members.filter((member) => member.epistemic.label === label).length,
      })),
      byPrimaryReason: countBy(primaryReasons).map(({ key, count }) => ({ reason: key, count })),
      secondaryReasons: countBy(secondaryReasons).map(({ key, count }) => ({ reason: key, count })),
      byTier: countBy(
        members.flatMap((member) =>
          member.epistemic.tier !== undefined ? [member.epistemic.tier] : [],
        ),
      ).map(({ key, count }) => ({ tier: key, count })),
      byFreshness: countBy(
        members.flatMap((member) =>
          member.epistemic.freshness !== undefined ? [member.epistemic.freshness] : [],
        ),
      ).map(({ key, count }) => ({ freshness: key, count })),
    },
    members,
  };
}
