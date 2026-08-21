import type { EvaluationIdentity, ProjectId } from './identity.js';
import type { RegistrationResult } from './declaration.js';
import type { CoverageResult, RepositoryCoverage } from './coverage.js';
import {
  ANSWER_VALUES,
  FACET_NAMES,
  MISSION_READY_DEFERRED_POSTURE,
  UNKNOWN_REASONS,
  type FacetName,
  type MissionReadyDeferredPosture,
  type UnknownReason,
} from './vocabulary.js';

// The seven project-shape answers — pure domain logic, no I/O, no clock.
// Behavior is bound by CAP1-REQ-030…038 (the adopted spec's
// "Independent project-shape answers" group) and the cited contract
// clauses: RFC6-18 (one fact set per selection at one evaluation),
// RFC6-14 (label parity; an aggregate carries no epistemic state of its
// own; secondary Unknown annotations travel with the primary, marked as
// secondary), RFC2-24 (the closed twelve-reason vocabulary), RFC6-19
// (drawer content classes; the full REQ-040 drawer is the S5 slice —
// this module serves REQ-033's own observable: constituent facts,
// declared scope, producing evaluation), and RFC2-19(a) as ratified by
// SDR-34 (merged-but-unreconciled is a fact of the render, never a
// thirteenth Unknown reason).
//
// Independence is structural (CAP1-REQ-030/032): each facet has its own
// compute function whose signature admits only that facet's declared
// constituent facts. No function receives another answer's value, so an
// answer's value cannot be a function of another answer's value by
// construction. There is no rollup function in this module and none may
// be added (CAP1-REQ-031): the only cross-answer projection is
// `shapeAnswerComposition`, a members' composition listing that derives
// no scalar, colour, badge, percentage, or passing count.

// --- Closed spellings, bound by tuple position (never restrung) ------

// The seven facet names, verbatim from the vocabulary authored at
// CAP1-REQ-030 per SDR-36. Positional binding makes any reorder of the
// vocabulary a compile error here.
const REGISTERED: 'Registered' = FACET_NAMES[0];
const SHAPE_PRESENT: 'Shape present' = FACET_NAMES[1];
const HUMAN_UNDERSTANDABLE: 'Human-understandable' = FACET_NAMES[2];
const OBSERVABLE: 'Observable' = FACET_NAMES[3];
const TRACEABLE: 'Traceable' = FACET_NAMES[4];
const MISSION_READY: 'Mission-ready' = FACET_NAMES[5];
const RECONCILED: 'Reconciled' = FACET_NAMES[6];

// The three-spelling value domain under the two-term rule
// (CAP1-REQ-030/034; SDR-35), closed — `satisfied` verbatim.
const SATISFIED: 'satisfied' = ANSWER_VALUES[0];
const GAP: 'Gap' = ANSWER_VALUES[1];
const UNKNOWN: 'Unknown' = ANSWER_VALUES[2];

// Reasons taken from the closed vocabulary by position (RFC2-24).
const MISSING_DECLARATION: 'missing-declaration' = UNKNOWN_REASONS[0]; // reason #1
const MISSING_EVIDENCE: 'missing-evidence' = UNKNOWN_REASONS[1]; // reason #2

// CAP1-REQ-037 / SDR-34, ratifying the RFC2-19(a) exemption as written:
// merged-but-unreconciled work is disclosed as a FACT of the render with
// this phrase — deliberately NOT an Unknown reason, so the twelve stay
// closed at twelve.
export const MERGED_WORK_UNRECONCILED_STATE = 'reconciliation evidence absent';

// --- The answer shape ------------------------------------------------

// One constituent fact, served inline: name and rendered value. In this
// pure layer a fact "resolves" by being carried in full; the daemon
// slice adds resolvable links (RFC6-19 class 3).
export interface ConstituentFact {
  readonly name: string;
  readonly value: string;
}

// REQ-033's observable per answer: constituent facts, declared scope,
// producing evaluation — plus the stated basis, so the oracle "the
// served value's stated basis references only facts present in the set"
// is checkable from the served object alone. Every arm below carries
// this set: an answer whose constituent facts cannot be served is not a
// servable answer, so there is no factless arm at the type level.
export interface FacetFactSet {
  readonly scope: string;
  readonly evaluation: EvaluationIdentity;
  // Non-empty by construction: absence itself is disclosed as a fact
  // (VIS-2 — absence is a fact of the render, never a blank).
  readonly facts: readonly ConstituentFact[];
  // Names of the facts the served value rests on — always a subset of
  // `facts` names.
  readonly basis: readonly string[];
}

// CAP1-REQ-035 / RFC6-14: when more than one Unknown condition applies,
// the primary renders with its secondaries beside it — all verbatim from
// the closed twelve, secondaries marked as secondary (the field IS the
// mark) and never folded into primary counts (the primary is exactly
// one, by type).
export interface UnknownReasonSet {
  readonly primary: UnknownReason;
  readonly secondary: readonly UnknownReason[];
}

// Composes the applicable conditions into primary + marked secondaries,
// first-applicable-first, duplicates removed. Requires at least one
// condition at the type level: a reasonless Unknown is not servable
// (RFC2-24 — Unknown always carries its reason).
export function composeUnknownReasons(
  applicable: readonly [UnknownReason, ...UnknownReason[]],
): UnknownReasonSet {
  const distinct = [...new Set(applicable)];
  return {
    primary: distinct[0] as UnknownReason,
    secondary: distinct.slice(1),
  };
}

// One facet's served value — a discriminated union over `value`, closed
// at the three SDR-35 spellings plus Mission-ready's deferred posture
// (CAP1-REQ-036: value `not evaluated`, basis `deferred`, epistemic
// label `Unknown`, verbatim). No other value is representable.
export type FacetRender =
  | { readonly value: typeof SATISFIED }
  | { readonly value: typeof GAP }
  | {
      readonly value: typeof UNKNOWN;
      readonly label: 'Unknown';
      readonly reasons: UnknownReasonSet;
    }
  | MissionReadyDeferredPosture;

export interface FacetAnswer {
  readonly name: FacetName;
  readonly render: FacetRender;
  readonly factSet: FacetFactSet;
}

// Exactly seven answers, in FACET_NAMES order — the tuple type makes a
// missing or extra answer a compile error (CAP1-REQ-030 oracle: count
// and name comparison, bounded at seven; CAP1-REQ-038: all seven remain
// served whatever their values).
export type ShapeAnswers = readonly [
  FacetAnswer,
  FacetAnswer,
  FacetAnswer,
  FacetAnswer,
  FacetAnswer,
  FacetAnswer,
  FacetAnswer,
];

// The served answer set. Its field set is deliberately three fields:
// identity, evaluation, and the seven members. NO field here is a
// function of two or more answers' values (CAP1-REQ-031) — no score, no
// badge, no colour, no percentage, no count of passing.
export interface ShapeAnswerSet {
  readonly projectId: ProjectId;
  readonly evaluation: EvaluationIdentity;
  readonly answers: ShapeAnswers;
}

// The one permitted aggregate rendering: a members' composition
// disclosure (CAP1-REQ-031: "an aggregate rendering over the answers
// carries no epistemic state of its own and SHALL disclose its members'
// composition instead"; RFC6-14). Each entry carries one member's own
// name and value; nothing is derived across members.
export interface AnswerCompositionEntry {
  readonly name: FacetName;
  readonly value: FacetRender['value'];
}

export function shapeAnswerComposition(
  set: ShapeAnswerSet,
): readonly AnswerCompositionEntry[] {
  return set.answers.map((answer) => ({
    name: answer.name,
    value: answer.render.value,
  }));
}

// --- Per-facet constituent-fact inputs -------------------------------

// Each facet's input type carries exactly the constituent facts
// CAP1-REQ-030 declares for it, supplied by the caller (the daemon
// slice; in conformance, the checker's fixture). `undefined` means the
// facts were never produced at this evaluation — absence of evidence,
// which renders Unknown with its reason (CAP1-REQ-034), never
// favourably and never as zero.

// Shape present: one declaration-referenced shape artifact and its
// resolution result at the evaluation. `resolution` values are
// implementation vocabulary (machine-readable discriminants), not spec
// spellings: 'resolved' (exists and resolves), 'missing' (resolution
// ran and established absence — current admissible evidence of
// non-satisfaction), 'unattempted' (no resolution evidence).
export interface ShapeReferenceResolution {
  readonly reference: string;
  readonly resolution: 'resolved' | 'missing' | 'unattempted';
}

// Human-understandable: one recorded fresh-reader comprehension
// walkthrough with its owner verdict (VIS-3's test class). Verdict
// spellings are implementation vocabulary.
export interface ComprehensionRecord {
  readonly recordId: string;
  readonly ownerVerdict: 'stands' | 'does-not-stand';
}

// Traceable: one rendered internal reference and whether it resolved to
// its identified target at the evaluation (the trust floor's link rule).
export interface LinkResolution {
  readonly link: string;
  readonly resolved: boolean;
}

// Reconciled: the reconciliation chain state where carried
// (CAP1-REQ-037), plus the merged work bearing on the scope.
export interface MergedWorkItem {
  readonly workId: string;
}

export type ReconciliationFacts =
  | {
      readonly computed: false;
      readonly mergedWork: readonly MergedWorkItem[];
    }
  | {
      readonly computed: true;
      readonly outcome: 'satisfied' | 'unsatisfied';
      readonly declaredScope: string;
      readonly mergedWork: readonly MergedWorkItem[];
    };

export interface ShapeAnswerInputs {
  readonly registration?: RegistrationResult | undefined;
  readonly shapeReferences?: readonly ShapeReferenceResolution[] | undefined;
  readonly comprehension?: readonly ComprehensionRecord[] | undefined;
  readonly coverage?: CoverageResult | undefined;
  readonly links?: readonly LinkResolution[] | undefined;
  readonly reconciliation?: ReconciliationFacts | undefined;
}

// --- Per-facet computation -------------------------------------------

function unknownRender(
  applicable: readonly [UnknownReason, ...UnknownReason[]],
): FacetRender {
  return { value: UNKNOWN, label: 'Unknown', reasons: composeUnknownReasons(applicable) };
}

// Registered — has this project's declaration been read and validated,
// yielding a registered project? Constituent facts: the declaration,
// its validation result, the governance-root designation (REQ-001–006).
// Registered reads as a RELATIONSHIP fact — under observation with a
// validated declaration — never an endorsement (CAP1-REQ-032).
export function computeRegistered(
  registration: RegistrationResult | undefined,
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  if (registration === undefined) {
    // No declaration was read at all: absence of the constituent fact,
    // disclosed as a fact of the render (CAP1-REQ-034).
    return {
      name: REGISTERED,
      render: unknownRender([MISSING_DECLARATION]),
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'declaration', value: 'absent — no declaration read at this evaluation' }],
        basis: ['declaration'],
      },
    };
  }
  if (registration.status === 'failed') {
    // A validation result establishing failure exists: current
    // admissible evidence of non-satisfaction — Gap, never Unknown
    // (CAP1-REQ-034's second scenario). Every named failure is a fact.
    const failureFacts = registration.failures.map((failure, i) => ({
      name: `validation-failure[${i}]`,
      value: failure.field === undefined ? failure.detail : `${failure.field}: ${failure.detail}`,
    }));
    return {
      name: REGISTERED,
      render: { value: GAP },
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'validation', value: 'failed' }, ...failureFacts],
        basis: ['validation'],
      },
    };
  }
  return {
    name: REGISTERED,
    render: { value: SATISFIED },
    factSet: {
      scope,
      evaluation,
      facts: [
        { name: 'declaration', value: `revision ${registration.facts.revision}` },
        { name: 'validation', value: registration.facts.validation },
        { name: 'root-designation', value: registration.facts.rootDesignation },
      ],
      basis: ['declaration', 'validation', 'root-designation'],
    },
  };
}

// Shape present — do the shape artifacts the declaration references
// exist and resolve at the evaluation? Constituent facts: the
// declaration's `declarations` references and their resolution results.
export function computeShapePresent(
  references: readonly ShapeReferenceResolution[] | undefined,
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  if (references === undefined) {
    // The reference list comes from the declaration; with no validated
    // declaration to supply it, the constituent facts are absent.
    return {
      name: SHAPE_PRESENT,
      render: unknownRender([MISSING_DECLARATION]),
      factSet: {
        scope,
        evaluation,
        facts: [
          {
            name: 'declarations-references',
            value: 'absent — no validated declaration supplies the reference list',
          },
        ],
        basis: ['declarations-references'],
      },
    };
  }

  const facts = references.map((entry) => ({
    name: `reference:${entry.reference}`,
    value: entry.resolution,
  }));
  const missing = references.filter((entry) => entry.resolution === 'missing');
  const unattempted = references.filter((entry) => entry.resolution === 'unattempted');

  if (missing.length > 0) {
    // Resolution ran and established absence: evidence of
    // non-satisfaction — Gap (CAP1-REQ-034).
    return {
      name: SHAPE_PRESENT,
      render: { value: GAP },
      factSet: {
        scope,
        evaluation,
        facts,
        basis: missing.map((entry) => `reference:${entry.reference}`),
      },
    };
  }
  if (unattempted.length > 0) {
    // No resolution evidence for at least one reference: Unknown, never
    // favourable (CAP1-REQ-034).
    return {
      name: SHAPE_PRESENT,
      render: unknownRender([MISSING_EVIDENCE]),
      factSet: {
        scope,
        evaluation,
        facts,
        basis: unattempted.map((entry) => `reference:${entry.reference}`),
      },
    };
  }
  if (references.length === 0) {
    // The enumeration ran and found zero references: evidence exists
    // and its denominator is zero — vacuously satisfied over an empty
    // set, with the denominator itself visible (the coverage module's
    // documented precedent for an empty declared set).
    return {
      name: SHAPE_PRESENT,
      render: { value: SATISFIED },
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'declarations-references', value: 'zero references declared (denominator 0)' }],
        basis: ['declarations-references'],
      },
    };
  }
  return {
    name: SHAPE_PRESENT,
    render: { value: SATISFIED },
    factSet: {
      scope,
      evaluation,
      facts,
      basis: facts.map((fact) => fact.name),
    },
  };
}

// Human-understandable — does recorded fresh-reader comprehension
// evidence exist and stand (VIS-3's test class)? With no records the
// answer is Unknown — the expected initial render (CAP1-REQ-030's own
// words).
export function computeHumanUnderstandable(
  records: readonly ComprehensionRecord[] | undefined,
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  if (records === undefined || records.length === 0) {
    return {
      name: HUMAN_UNDERSTANDABLE,
      render: unknownRender([MISSING_EVIDENCE]),
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'comprehension-records', value: 'none recorded' }],
        basis: ['comprehension-records'],
      },
    };
  }
  const facts = records.map((record) => ({
    name: `comprehension-record:${record.recordId}`,
    value: `owner verdict: ${record.ownerVerdict}`,
  }));
  const failing = records.filter((record) => record.ownerVerdict === 'does-not-stand');
  if (failing.length > 0) {
    // A recorded owner verdict establishes non-satisfaction — Gap.
    return {
      name: HUMAN_UNDERSTANDABLE,
      render: { value: GAP },
      factSet: {
        scope,
        evaluation,
        facts,
        basis: failing.map((record) => `comprehension-record:${record.recordId}`),
      },
    };
  }
  return {
    name: HUMAN_UNDERSTANDABLE,
    render: { value: SATISFIED },
    factSet: { scope, evaluation, facts, basis: facts.map((fact) => fact.name) },
  };
}

function repositoryFact(entry: RepositoryCoverage): ConstituentFact {
  const name = `repository:${entry.repositoryId}`;
  switch (entry.state) {
    case 'observed':
      return {
        name,
        value: `observed; consent ${entry.consent.recordId} in-force; captured scope ${entry.capturedScope}`,
      };
    case 'unconsented':
      return {
        name,
        value: `unconsented (${entry.basis}); resolution route: ${entry.resolutionRoute}`,
      };
    case 'capture-failed':
      return { name, value: `capture failed — ${entry.reason}` };
    case 'stale':
      return { name, value: `stale — ${entry.reason}` };
    case 'degraded-partial':
      return {
        name,
        value: `partial capture — captured ${entry.capturedScope} of ${entry.declaredScope}; remainder Unknown (${entry.uncaptured.reason})`,
      };
  }
}

// The Unknown reason one not-fully-observed repository contributes.
function repositoryReason(entry: RepositoryCoverage): UnknownReason | undefined {
  switch (entry.state) {
    case 'observed':
      return undefined;
    case 'unconsented':
    case 'capture-failed':
    case 'stale':
      return entry.reason;
    case 'degraded-partial':
      // The uncaptured remainder is Unknown with reason #10.
      return entry.uncaptured.reason;
  }
}

// Observable — may Syzygy observe the declared sources, and did current
// observation succeed? Constituent facts: the coverage boundary and
// consent states (REQ-010–016). Every non-observation condition in the
// coverage layer is an Unknown state carrying its reason (unconsented is
// a standing POLICY state, REQ-012; a capture failure is absence of
// successful observation, not established non-satisfaction) — so a
// not-fully-observed project renders Unknown with ALL applicable
// reasons, primary plus marked secondaries (CAP1-REQ-035), never Gap
// from this layer and never favourable.
export function computeObservable(
  coverage: CoverageResult | undefined,
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  if (coverage === undefined) {
    return {
      name: OBSERVABLE,
      render: unknownRender([MISSING_EVIDENCE]),
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'coverage', value: 'not computed at this evaluation' }],
        basis: ['coverage'],
      },
    };
  }
  if (coverage.repositories.length === 0) {
    return {
      name: OBSERVABLE,
      render: { value: SATISFIED },
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'coverage', value: 'zero repositories declared (denominator 0)' }],
        basis: ['coverage'],
      },
    };
  }

  const facts = coverage.repositories.map(repositoryFact);
  const notObserved = coverage.repositories.filter(
    (entry) => repositoryReason(entry) !== undefined,
  );
  if (notObserved.length === 0) {
    return {
      name: OBSERVABLE,
      render: { value: SATISFIED },
      factSet: { scope, evaluation, facts, basis: facts.map((fact) => fact.name) },
    };
  }
  // All applicable conditions, in declaration order — one never hides
  // the others (CAP1-REQ-035).
  const reasons = notObserved.map((entry) => repositoryReason(entry) as UnknownReason);
  // notObserved.length > 0 was just checked, so the list is non-empty;
  // the head/rest split re-establishes that at the type level without a
  // cast across the tuple boundary.
  const [firstReason, ...restReasons] = reasons as [UnknownReason, ...UnknownReason[]];
  return {
    name: OBSERVABLE,
    render: unknownRender([firstReason, ...restReasons]),
    factSet: {
      scope,
      evaluation,
      facts,
      basis: notObserved.map((entry) => `repository:${entry.repositoryId}`),
    },
  };
}

// Traceable — do the project's rendered internal references resolve to
// their identified targets? Constituent facts: link-resolution results
// over the served surfaces at the evaluation (the trust floor's link
// rule).
export function computeTraceable(
  links: readonly LinkResolution[] | undefined,
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  if (links === undefined) {
    return {
      name: TRACEABLE,
      render: unknownRender([MISSING_EVIDENCE]),
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'link-resolution', value: 'not computed at this evaluation' }],
        basis: ['link-resolution'],
      },
    };
  }
  if (links.length === 0) {
    return {
      name: TRACEABLE,
      render: { value: SATISFIED },
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'link-resolution', value: 'zero rendered internal references (denominator 0)' }],
        basis: ['link-resolution'],
      },
    };
  }
  const facts = links.map((entry) => ({
    name: `link:${entry.link}`,
    value: entry.resolved ? 'resolves to its identified target' : 'does not resolve',
  }));
  const unresolved = links.filter((entry) => !entry.resolved);
  if (unresolved.length > 0) {
    // A resolution run establishing a dangling rendered reference is
    // evidence of non-satisfaction — Gap.
    return {
      name: TRACEABLE,
      render: { value: GAP },
      factSet: {
        scope,
        evaluation,
        facts,
        basis: unresolved.map((entry) => `link:${entry.link}`),
      },
    };
  }
  return {
    name: TRACEABLE,
    render: { value: SATISFIED },
    factSet: { scope, evaluation, facts, basis: facts.map((fact) => fact.name) },
  };
}

// Mission-ready — deferred (CAP1-REQ-036). While the governing Context
// and Mission contracts remain unaccepted — which, within Capability 1,
// they do by the authorization act's own scope — the answer renders
// ONLY its deferred posture: value `not evaluated`, basis `deferred`,
// epistemic label `Unknown`, each verbatim (SDR-36 rule 3). The facet
// takes NO evaluation input: its semantics are deliberately not defined
// by the specification, so there is nothing to compute — and the
// satisfied/Gap/score arms are unreachable by construction.
export function computeMissionReady(
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  return {
    name: MISSION_READY,
    render: MISSION_READY_DEFERRED_POSTURE,
    factSet: {
      scope,
      evaluation,
      facts: [
        {
          name: 'mission-contracts',
          value: 'unaccepted — posture deferred (SDR-36 rule 3)',
        },
      ],
      basis: ['mission-contracts'],
    },
  };
}

// Reconciled — has reconciliation of merged work against intent been
// computed and satisfied for the declared scope? Uncomputed
// reconciliation is Unknown (CAP1-REQ-037; SDR-12), and merged work
// renders as reconciliation evidence absent — a fact of the render,
// bound to NO thirteenth reason (SDR-34; RFC2-19(a) as written).
export function computeReconciled(
  reconciliation: ReconciliationFacts | undefined,
  scope: string,
  evaluation: EvaluationIdentity,
): FacetAnswer {
  if (reconciliation === undefined) {
    return {
      name: RECONCILED,
      render: unknownRender([MISSING_EVIDENCE]),
      factSet: {
        scope,
        evaluation,
        facts: [{ name: 'reconciliation', value: 'not computed at this evaluation' }],
        basis: ['reconciliation'],
      },
    };
  }
  if (!reconciliation.computed) {
    // Merged-but-unreconciled: never reconciled, never done, never
    // green (SDR-12) — each work item's state is a served fact reading
    // `reconciliation evidence absent`, and the answer's reason stays
    // inside the twelve.
    const workFacts = reconciliation.mergedWork.map((item) => ({
      name: `merged-work:${item.workId}`,
      value: MERGED_WORK_UNRECONCILED_STATE,
    }));
    return {
      name: RECONCILED,
      render: unknownRender([MISSING_EVIDENCE]),
      factSet: {
        scope,
        evaluation,
        facts: [
          { name: 'reconciliation', value: 'not computed for the declared scope' },
          ...workFacts,
        ],
        basis: ['reconciliation'],
      },
    };
  }
  const workFacts = reconciliation.mergedWork.map((item) => ({
    name: `merged-work:${item.workId}`,
    value: `covered by computed reconciliation (${reconciliation.outcome})`,
  }));
  const facts = [
    {
      name: 'reconciliation',
      value: `computed — ${reconciliation.outcome} for scope ${reconciliation.declaredScope}`,
    },
    ...workFacts,
  ];
  if (reconciliation.outcome === 'unsatisfied') {
    // A computed reconciliation establishing divergence is evidence of
    // non-satisfaction — Gap.
    return {
      name: RECONCILED,
      render: { value: GAP },
      factSet: { scope, evaluation, facts, basis: ['reconciliation'] },
    };
  }
  return {
    name: RECONCILED,
    render: { value: SATISFIED },
    factSet: { scope, evaluation, facts, basis: ['reconciliation'] },
  };
}

// --- The answer set --------------------------------------------------

// Computes the seven answers for one project at one identified
// evaluation. Each answer is computed independently from its own
// declared constituent facts (CAP1-REQ-030): the per-facet functions
// above never see another facet's input or value. Deterministic: a pure
// function of (projectId, evaluation, inputs) — no clock, no I/O; the
// evaluation identity is the caller's coordinate (CAP1-REQ-042's stamp
// travels on the set).
export function computeShapeAnswers(
  projectId: ProjectId,
  evaluation: EvaluationIdentity,
  inputs: ShapeAnswerInputs,
): ShapeAnswerSet {
  const scope = `project:${projectId}`;
  return {
    projectId,
    evaluation,
    answers: [
      computeRegistered(inputs.registration, scope, evaluation),
      computeShapePresent(inputs.shapeReferences, scope, evaluation),
      computeHumanUnderstandable(inputs.comprehension, scope, evaluation),
      computeObservable(inputs.coverage, scope, evaluation),
      computeTraceable(inputs.links, scope, evaluation),
      computeMissionReady(scope, evaluation),
      computeReconciled(inputs.reconciliation, scope, evaluation),
    ],
  };
}
