import type { EvaluationIdentity } from './identity.js';
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
// their facts by construction. The independent oracle over that
// construction (parity-oracle.ts, exported from the `testing` entry only)
// judges parity solely by comparing the two channels' outputs — never by
// either channel's claim, and never by the shared source's claim
// (neither carries one).

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
