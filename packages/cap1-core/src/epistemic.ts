import {
  EPISTEMIC_LABELS,
  type EpistemicLabel,
} from './vocabulary.js';
import type { UnknownReasonSet } from './facets.js';
import type { FreshnessState } from './staleness.js';

// Epistemic state on served facts, and the cited-basis rule — pure
// domain logic, no I/O, no clock. Behavior is bound by CAP1-REQ-045 and
// the cited contract clauses RFC6-14 (every claim instance in a machine
// answer carries its epistemic state verbatim: label + tier + Unknown
// reason + freshness; a machine answer never omits epistemic state),
// RFC7-33 (every distinction is carried as a machine-readable attribute
// on the rendered unit, served identically through the machine plane and
// preserved in plain-text renderings — a distinction available only to
// pixels does not survive), and RFC7-34 (recoverable without colour,
// position, or layout — by label, text, or structure).

// The six rendering tiers, closed at six (RFC2-25; RFC6-17 requires all
// six, never a subset). Spec-governed closed vocabulary; it lives here
// because vocabulary.ts is committed and S5's edits to committed modules
// are additive-re-export only.
export const RENDERING_TIERS = [
  'gate-backed',
  'report-fact',
  'asserted-by-worker',
  'reduced-fidelity',
  'declared-only',
  'suspended',
] as const;
export type RenderingTier = (typeof RENDERING_TIERS)[number];

// Labels bound by tuple position — a vocabulary reorder is a compile
// error here, so the spellings are imported, never restrung.
const OBSERVED: 'Observed' = EPISTEMIC_LABELS[0];
const INFERRED: 'Inferred' = EPISTEMIC_LABELS[1];
const UNKNOWN: 'Unknown' = EPISTEMIC_LABELS[2];

// One fact's epistemic state — a discriminated union over `label`, so
// an Unknown without its reason set is not constructible (RFC2-24:
// Unknown always carries its reason; the reasons travel primary +
// marked secondaries per RFC6-14) — with ONE exception: the deferred
// posture (SDR-36 rule 3; CAP1-REQ-036), whose serving coordinates are
// value `not evaluated`, basis `deferred`, label `Unknown`, and
// deliberately no reason from the closed twelve. That arm carries
// `basis: 'deferred'` instead, so the reasonless Unknown stays exactly
// as wide as the owner decision that licenses it. Tier and freshness
// travel where the fact carries them; their absence renders as absence,
// never as a favourable default.
export type EpistemicState =
  | {
      readonly label: typeof OBSERVED | typeof INFERRED;
      readonly tier?: RenderingTier | undefined;
      readonly freshness?: FreshnessState | undefined;
    }
  | {
      readonly label: typeof UNKNOWN;
      readonly reasons: UnknownReasonSet;
      readonly tier?: RenderingTier | undefined;
      readonly freshness?: FreshnessState | undefined;
    }
  | {
      readonly label: typeof UNKNOWN;
      readonly basis: 'deferred';
      readonly tier?: RenderingTier | undefined;
      readonly freshness?: FreshnessState | undefined;
    };

// One served fact: name, rendered value, and its epistemic state. The
// label is REQUIRED at the type level — there is no unlabeled-fact arm,
// because a fact served without its label has dropped part of its
// epistemic state (RFC6-14; CAP1-REQ-045's oracle: every fact carries a
// label).
export interface ServedFact {
  readonly name: string;
  readonly value: string;
  readonly epistemic: EpistemicState;
}

// The machine-readable marking that distinguishes inferred from
// observed: the label attribute itself, returned as text. It is an
// attribute ON the unit — not a colour, not a position, not a layout —
// so it survives serialization, plain-text export, and a reader who
// cannot see (RFC7-33/34; CAP1-REQ-045: distinguishable "machine-readably
// and without relying on colour, position, or layout"). Two facts equal
// in every rendered respect but label yield different markings.
export function epistemicMarking(state: EpistemicState): EpistemicLabel {
  return state.label;
}

// --- Cited basis: the owning authority, never a rendering of it -------

// The one admissible basis class: an owning authority with its
// governing normative revision (RFC6-19 class 4: the typed authority
// that answered, with the governing revision).
export interface OwningAuthorityBasis {
  readonly kind: 'owning-authority';
  readonly authority: string;
  readonly governingRevision: string;
}

// A generated presentation artifact offered as a basis — the class
// CAP1-REQ-045 prohibits as a source. It names the authority it
// renders, which is the lawful route.
export interface GeneratedPresentationCandidate {
  readonly kind: 'generated-presentation';
  readonly artifact: string;
  readonly rendersAuthority: string;
}

export type BasisCandidate = OwningAuthorityBasis | GeneratedPresentationCandidate;

// The admission result, fail-closed: there is no arm in which a
// generated presentation artifact becomes a cited basis. The refusal
// names the lawful route (cite the authority the artifact renders) but
// never silently substitutes it — substitution would hide the defect
// the falsifier names ("a status answer whose provenance names a
// generated page").
export type BasisAdmission =
  | { readonly cited: true; readonly basis: OwningAuthorityBasis }
  | {
      readonly cited: false;
      readonly refusal: 'generated-presentation-is-never-a-source';
      readonly artifact: string;
      readonly route: string;
    };

export function citeBasis(candidate: BasisCandidate): BasisAdmission {
  if (candidate.kind === 'generated-presentation') {
    return {
      cited: false,
      refusal: 'generated-presentation-is-never-a-source',
      artifact: candidate.artifact,
      route: `cite the owning authority the artifact renders: ${candidate.rendersAuthority}`,
    };
  }
  return { cited: true, basis: candidate };
}
