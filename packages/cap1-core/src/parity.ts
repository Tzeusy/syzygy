import type { EvaluationIdentity } from './identity.js';
import { deterministicLayer } from './evaluation.js';
import type { ServedFact } from './epistemic.js';
import { WHY_THIS_ANSWER } from './drawer.js';

// Human/machine parity — pure domain logic, no I/O, no clock. Behavior
// is bound by CAP1-REQ-041 and CAP1-REQ-043 and the cited contract
// clauses RFC6-13 (one truth, two consumers: no endpoint-only facts, no
// UI-only facts), RFC6-14 (label parity — every epistemic value travels
// verbatim), RFC6-22 (the equivalence definition: same evaluation, same
// declared filters, same facts, same epistemic states, over semantics
// never pixels), RFC6-23 (finer detail is a disclosed filter difference;
// contradiction is a defect, release-blocking, never resolved by
// preferring one rendering), and RFC6-21 (minimal display never
// subtracts facts).
//
// Parity is BY CONSTRUCTION here (the implementation plan's stated
// design): ONE fact model, serialized to the machine plane and rendered
// to the human view from the SAME source, so the two channels share
// their facts by construction. The comparison functions below are the
// independent oracle over that construction: they judge parity solely
// by comparing the two channels' outputs — never by either channel's
// claim, and never by the shared source's claim (neither carries one).

// --- The one fact model ----------------------------------------------

// The single source both channels serve from (RFC6-18: one fact set per
// (selection, evaluation, scenario context); RFC6-16: filters are
// declared scope, part of the answer's envelope).
export interface FactModel {
  readonly selection: string;
  readonly evaluation: EvaluationIdentity;
  readonly scenarioContext: string;
  readonly declaredFilters: Readonly<Record<string, string>>;
  readonly facts: readonly ServedFact[];
}

// The machine answer: the full fact set, verbatim, with the envelope.
export interface MachineAnswer {
  readonly channel: 'machine';
  readonly selection: string;
  readonly evaluation: EvaluationIdentity;
  readonly scenarioContext: string;
  readonly declaredFilters: Readonly<Record<string, string>>;
  readonly facts: readonly ServedFact[];
}

// One human-view section: presentation grouping only. The facts inside
// are the model's own fact objects — grouping assigns, it never edits.
export interface HumanSection {
  readonly heading: string;
  readonly facts: readonly ServedFact[];
}

// The human view: the same facts, grouped and ordered for reading, with
// the explanation reachable under its literal name (RFC6-18;
// CAP1-REQ-040). The epistemic state travels on each fact as a text
// attribute inside the sections — recoverable without colour, position,
// or layout (RFC7-33/34).
export interface HumanView {
  readonly channel: 'human';
  readonly selection: string;
  readonly evaluation: EvaluationIdentity;
  readonly scenarioContext: string;
  readonly declaredFilters: Readonly<Record<string, string>>;
  readonly sections: readonly HumanSection[];
  readonly explanationReachableAs: typeof WHY_THIS_ANSWER;
}

// A presentation spec: which facts to group under which headings, in
// what order. Presentation freedom is exactly this wide (RFC6-18:
// "ordering, grouping, progressive disclosure") — and no wider: a
// presentation cannot subtract a fact (see renderHuman) and cannot mint
// one (names not in the model match nothing).
export interface HumanPresentation {
  readonly sections: readonly {
    readonly heading: string;
    readonly factNames: readonly string[];
  }[];
}

// Serializes the model to the machine plane: every fact, verbatim, by
// reference — no copy step that could drift (RFC6-13).
export function serveMachine(model: FactModel): MachineAnswer {
  return {
    channel: 'machine',
    selection: model.selection,
    evaluation: model.evaluation,
    scenarioContext: model.scenarioContext,
    declaredFilters: model.declaredFilters,
    facts: model.facts,
  };
}

// The heading under which facts no presentation section claimed are
// rendered — so a partial presentation spec cannot subtract a fact.
export const FURTHER_FACTS_HEADING = 'Further facts' as const;

// Renders the model to the human view. Load-bearing property
// (CAP1-REQ-041; RFC6-21): every fact of the model appears in exactly
// one section, whatever the presentation says. A fact the presentation
// assigns goes to its first assigning section; every unassigned fact
// lands in a final "Further facts" section. There is no code path that
// drops a fact, and no code path that renders a fact absent from the
// model.
export function renderHuman(
  model: FactModel,
  presentation?: HumanPresentation,
): HumanView {
  const placedIndices = new Set<number>();
  const sections: HumanSection[] = [];

  for (const spec of presentation?.sections ?? []) {
    const facts: ServedFact[] = [];
    for (const name of spec.factNames) {
      for (let i = 0; i < model.facts.length; i++) {
        const fact = model.facts[i];
        if (fact !== undefined && !placedIndices.has(i) && fact.name === name) {
          placedIndices.add(i);
          facts.push(fact);
        }
      }
    }
    sections.push({ heading: spec.heading, facts });
  }

  const leftover = model.facts.filter((_, i) => !placedIndices.has(i));
  if (leftover.length > 0 || sections.length === 0) {
    sections.push({ heading: FURTHER_FACTS_HEADING, facts: leftover });
  }

  return {
    channel: 'human',
    selection: model.selection,
    evaluation: model.evaluation,
    scenarioContext: model.scenarioContext,
    declaredFilters: model.declaredFilters,
    sections,
    explanationReachableAs: WHY_THIS_ANSWER,
  };
}

// --- The independent parity oracle -----------------------------------

// A channel output's full disclosure, extracted from the OUTPUT ITSELF
// — the machine answer's fact list, or the human view's sections
// flattened. Never read back from the shared model: the oracle compares
// what each channel actually serves (CAP1-REQ-041 oracle independence:
// "judged by cross-channel comparison, not by either channel's
// self-description").
export function fullDisclosure(output: MachineAnswer | HumanView): readonly ServedFact[] {
  if (output.channel === 'machine') {
    return output.facts;
  }
  return output.sections.flatMap((section) => section.facts);
}

// One rendering's comparable disclosure: envelope + extracted facts.
// Deliberately carries NO self-description of parity — there is nothing
// here a comparison could consult except the served content.
export interface ChannelDisclosure {
  readonly selection: string;
  readonly evaluation: EvaluationIdentity;
  readonly scenarioContext: string;
  readonly declaredFilters: Readonly<Record<string, string>>;
  readonly facts: readonly ServedFact[];
}

export function disclosureOf(output: MachineAnswer | HumanView): ChannelDisclosure {
  return {
    selection: output.selection,
    evaluation: output.evaluation,
    scenarioContext: output.scenarioContext,
    declaredFilters: output.declaredFilters,
    facts: fullDisclosure(output),
  };
}

// The equivalence facets two renderings may not disagree on
// (CAP1-REQ-043: existence, label, reason, freshness state, value, and
// a count over one declared scope; RFC6-22/23 — tier is part of the
// epistemic-state tuple).
export type ParityFacet = 'existence' | 'value' | 'label' | 'reason' | 'freshness' | 'tier' | 'count';

// One disagreement: the fact, the facet, and BOTH channels' values —
// neither marked authoritative. There is deliberately no field naming a
// winner, a preferred channel, or a resolution: presentation precedence
// never resolves a parity disagreement (CAP1-REQ-043).
export interface ParityDisagreement {
  readonly factName: string;
  readonly facet: ParityFacet;
  readonly inFirst: string;
  readonly inSecond: string;
  /** The canonical semantic tuple when the disagreement is an occurrence count. */
  readonly tupleDigest?: string;
}

// The comparison result. Two renderings whose envelopes differ are not
// renderings of one (selection, evaluation, scenario context) — a
// declared filter difference is the one LAWFUL way two renderings may
// differ in content (disclosed aggregation/finer detail, RFC6-23),
// never a contradiction. Comparable renderings either agree on every
// facet (parity) or disagree — and a disagreement is a DEFECT that
// fails the parity requirements, rendering as a disagreement, whatever
// either rendering claims (CAP1-REQ-043's oracle: "any found
// disagreement is a failure of this requirement").
export type ParityComparison =
  | {
      readonly comparable: false;
      readonly basis:
        | 'different-selection'
        | 'different-evaluation'
        | 'different-scenario-context'
        | 'declared-filter-difference';
    }
  | { readonly comparable: true; readonly verdict: 'parity'; readonly comparedFacts: number }
  | {
      readonly comparable: true;
      readonly verdict: 'parity-defect';
      readonly renders: 'disagreement';
      readonly disagreements: readonly [ParityDisagreement, ...ParityDisagreement[]];
    };

// Serializes one fact's Unknown-reason state verbatim for comparison:
// the primary plus its marked secondaries (RFC6-14 — a rendering
// carrying the primary alone has dropped part of the epistemic state).
function reasonFacet(fact: ServedFact): string {
  if (fact.epistemic.label !== 'Unknown') {
    return 'none';
  }
  if (!('reasons' in fact.epistemic)) {
    // The deferred posture's reasonless Unknown (SDR-36 rule 3): its
    // basis is the comparable state, verbatim.
    return 'basis:deferred';
  }
  const { primary, secondary } = fact.epistemic.reasons;
  return `primary:${primary}; secondary:[${secondary.join(', ')}]`;
}

function facetPairs(a: ServedFact, b: ServedFact): readonly {
  readonly facet: ParityFacet;
  readonly inFirst: string;
  readonly inSecond: string;
}[] {
  return [
    { facet: 'value', inFirst: a.value, inSecond: b.value },
    { facet: 'label', inFirst: a.epistemic.label, inSecond: b.epistemic.label },
    { facet: 'reason', inFirst: reasonFacet(a), inSecond: reasonFacet(b) },
    {
      facet: 'freshness',
      inFirst: a.epistemic.freshness ?? 'absent',
      inSecond: b.epistemic.freshness ?? 'absent',
    },
    {
      facet: 'tier',
      inFirst: a.epistemic.tier ?? 'absent',
      inSecond: b.epistemic.tier ?? 'absent',
    },
  ];
}

// Counts complete canonical tuples without treating any tuple field as a
// uniqueness key. The returned map is deliberately generic so downstream
// projections can share the same multiplicity-preserving comparison seam.
export function canonicalTupleMultiset<T>(
  values: readonly T[],
  canonicalize: (value: T) => string,
): ReadonlyMap<string, number> {
  const counts = new Map<string, number>();
  for (const value of values) {
    const key = canonicalize(value);
    counts.set(key, (counts.get(key) ?? 0) + 1);
  }
  return counts;
}

// A fact's semantic tuple excludes only presentation/channel formatting. The
// full epistemic state remains in the key, including Unknown reasons, basis,
// freshness, and tier.
function canonicalFactTuple(fact: ServedFact): string {
  return deterministicLayer({
    name: fact.name,
    value: fact.value,
    epistemic: {
      label: fact.epistemic.label,
      reasons: 'reasons' in fact.epistemic ? fact.epistemic.reasons : undefined,
      basis: 'basis' in fact.epistemic ? fact.epistemic.basis : undefined,
      freshness: fact.epistemic.freshness,
      tier: fact.epistemic.tier,
    },
  });
}

function factsByName(facts: readonly ServedFact[]): Map<string, ServedFact[]> {
  const grouped = new Map<string, ServedFact[]>();
  for (const fact of facts) {
    const named = grouped.get(fact.name);
    if (named === undefined) {
      grouped.set(fact.name, [fact]);
    } else {
      named.push(fact);
    }
  }
  return grouped;
}

// Compares two renderings of what should be one (selection, evaluation,
// scenario context). The judgment consults ONLY the two disclosures —
// no implementation state, no self-report, no shared-source claim
// exists to consult (oracle independence, CAP1-REQ-043: "disagreement
// is a relation between two served outputs; no implementation judgment
// is consulted"). Symmetric up to the first/second labels.
export function compareRenderings(
  first: ChannelDisclosure,
  second: ChannelDisclosure,
): ParityComparison {
  if (first.selection !== second.selection) {
    return { comparable: false, basis: 'different-selection' };
  }
  if (
    first.evaluation.snapshot !== second.evaluation.snapshot ||
    first.evaluation.asOf !== second.evaluation.asOf
  ) {
    return { comparable: false, basis: 'different-evaluation' };
  }
  if (first.scenarioContext !== second.scenarioContext) {
    return { comparable: false, basis: 'different-scenario-context' };
  }
  if (deterministicLayer(first.declaredFilters) !== deterministicLayer(second.declaredFilters)) {
    // The lawful difference: disclosed filters differ, so the two are
    // an aggregation/finer-detail pair, not an equivalent pair
    // (RFC6-23). Their content difference is a filter difference, never
    // a contradiction — and never silently treated as parity either.
    return { comparable: false, basis: 'declared-filter-difference' };
  }

  const disagreements: ParityDisagreement[] = [];
  const firstByName = factsByName(first.facts);
  const secondByName = factsByName(second.facts);
  const names = [...new Set([...firstByName.keys(), ...secondByName.keys()])].sort();

  // Preserve the existing per-facet diagnostics where each name identifies
  // exactly one fact in each channel. Duplicate names are intentionally not
  // paired by position or by last-write-wins lookup; their complete tuples
  // are diagnosed below.
  for (const name of names) {
    const factsInFirst = firstByName.get(name) ?? [];
    const factsInSecond = secondByName.get(name) ?? [];
    if (factsInFirst.length === 1 && factsInSecond.length === 1) {
      const factInFirst = factsInFirst[0];
      const factInSecond = factsInSecond[0];
      if (factInFirst === undefined || factInSecond === undefined) {
        throw new Error('fact grouping lost a unique fact');
      }
      for (const pair of facetPairs(factInFirst, factInSecond)) {
        if (pair.inFirst !== pair.inSecond) {
          disagreements.push({ factName: name, ...pair });
        }
      }
    } else if (factsInFirst.length === 1 && factsInSecond.length === 0) {
      disagreements.push({
        factName: name,
        facet: 'existence',
        inFirst: 'present',
        inSecond: 'absent',
      });
    } else if (factsInFirst.length === 0 && factsInSecond.length === 1) {
      disagreements.push({
        factName: name,
        facet: 'existence',
        inFirst: 'absent',
        inSecond: 'present',
      });
    }
  }

  const firstTuples = canonicalTupleMultiset(first.facts, canonicalFactTuple);
  const secondTuples = canonicalTupleMultiset(second.facts, canonicalFactTuple);
  const tupleDigests = [
    ...new Set([...firstTuples.keys(), ...secondTuples.keys()]),
  ].sort();
  for (const tupleDigest of tupleDigests) {
    const inFirst = firstTuples.get(tupleDigest) ?? 0;
    const inSecond = secondTuples.get(tupleDigest) ?? 0;
    if (inFirst === inSecond) {
      continue;
    }

    const fact =
      first.facts.find((candidate) => canonicalFactTuple(candidate) === tupleDigest) ??
      second.facts.find((candidate) => canonicalFactTuple(candidate) === tupleDigest);
    if (fact === undefined) {
      throw new Error('tuple grouping lost a mismatched fact');
    }
    const factsWithNameInFirst = firstByName.get(fact.name) ?? [];
    const factsWithNameInSecond = secondByName.get(fact.name) ?? [];
    // A unique-name difference already has the source-compatible, focused
    // diagnostics above. Tuple counts are reserved for duplicate names so
    // neither occurrence is silently selected or paired.
    if (factsWithNameInFirst.length <= 1 && factsWithNameInSecond.length <= 1) {
      continue;
    }
    disagreements.push({
      factName: fact.name,
      facet: 'count',
      inFirst: String(inFirst),
      inSecond: String(inSecond),
      tupleDigest,
    });
  }

  if (disagreements.length === 0) {
    return { comparable: true, verdict: 'parity', comparedFacts: first.facts.length };
  }
  const [head, ...rest] = disagreements as [ParityDisagreement, ...ParityDisagreement[]];
  return {
    comparable: true,
    verdict: 'parity-defect',
    renders: 'disagreement',
    disagreements: [head, ...rest],
  };
}
