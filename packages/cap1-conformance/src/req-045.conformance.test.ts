import { describe, expect, it } from 'vitest';
import {
  EPISTEMIC_LABELS,
  RENDERING_TIERS,
  canonicalTupleMultiset,
  citeBasis,
  compareRenderings,
  deterministicLayer,
  disclosureOf,
  epistemicMarking,
  renderHuman,
  serveMachine,
  type EvaluationIdentity,
  type FactModel,
  type ServedFact,
} from '@syzygy/cap1-core';

// CAP1-REQ-045 — Inferred is distinguishable from observed; generated
// presentation is never the source (invariant).
//
// Case: every served fact and every generated presentation artifact;
// sweep: enumerate served facts' labels and answers' cited bases in a
// fixture — denominator: the served fact and answer sets. Oracle: every
// fact carries a label; inferred facts carry a machine-readable marking
// distinct from observed; no cited basis is a presentation artifact.
// Oracle independence: labels and bases are inspectable output; the
// three-label rule is doctrine's. Falsifier: an LLM-derived value
// served without an Inferred marking, or a status answer whose
// provenance names a generated page.

const EVALUATION: EvaluationIdentity = {
  snapshot: 'snap-2026-08-21-e',
  asOf: '2026-08-21T00:00:00Z',
};

const OBSERVED_FACT: ServedFact = {
  name: 'repository-count',
  value: '2',
  epistemic: { label: 'Observed' },
};
// An LLM-derived value — Inferred by doctrine ("an LLM assertion is
// Inferred"), served with the asserted-by-worker tier.
const INFERRED_FACT: ServedFact = {
  name: 'summary-of-intent',
  value: 'the project appears to target governance visibility',
  epistemic: { label: 'Inferred', tier: 'asserted-by-worker' },
};

function model(facts: readonly ServedFact[]): FactModel {
  return {
    selection: 'project:prj-epistemic-45',
    evaluation: EVALUATION,
    scenarioContext: 'base',
    declaredFilters: {},
    facts,
  };
}

describe('CAP1-REQ-045 — inferred is distinguishable from observed; generated presentation is never the source', () => {
  it('canonical tuple multisets retain duplicate occurrence counts', () => {
    const counts = canonicalTupleMultiset(
      [
        { name: 'answer', value: 'same' },
        { name: 'answer', value: 'same' },
        { name: 'answer', value: 'different' },
      ],
      (fact) => `${fact.name}:${fact.value}`,
    );

    expect([...counts.entries()]).toEqual([
      ['answer:same', 2],
      ['answer:different', 1],
    ]);
  });

  it('the three-label vocabulary is closed and verbatim', () => {
    expect([...EPISTEMIC_LABELS]).toEqual(['Observed', 'Inferred', 'Unknown']);
  });

  it('the six rendering tiers are closed and verbatim (RFC2-25)', () => {
    expect([...RENDERING_TIERS]).toEqual([
      'gate-backed',
      'report-fact',
      'asserted-by-worker',
      'reduced-fidelity',
      'declared-only',
      'suspended',
    ]);
  });

  it('the inferred marking is a machine-readable text attribute, distinct from the observed one', () => {
    // Two facts identical in every rendered respect except label yield
    // different markings — and the marking is a returned string, not a
    // colour, position, or layout.
    const observed: ServedFact = { ...INFERRED_FACT, epistemic: { label: 'Observed' } };
    expect(epistemicMarking(INFERRED_FACT.epistemic)).toBe('Inferred');
    expect(epistemicMarking(observed.epistemic)).toBe('Observed');
    expect(epistemicMarking(INFERRED_FACT.epistemic)).not.toBe(
      epistemicMarking(observed.epistemic),
    );
  });

  it('scenario: the Inferred label travels verbatim to the machine answer and is recoverable non-visually in the human view', () => {
    const machine = serveMachine(model([OBSERVED_FACT, INFERRED_FACT]));
    const human = renderHuman(model([OBSERVED_FACT, INFERRED_FACT]));
    const machineFact = machine.facts.find((fact) => fact.name === 'summary-of-intent');
    expect(machineFact?.epistemic.label).toBe('Inferred');
    // Non-visual recoverability: the label is an attribute ON the unit
    // inside the view's structure — text, not styling.
    const humanFact = human.sections
      .flatMap((section) => section.facts)
      .find((fact) => fact.name === 'summary-of-intent');
    expect(humanFact?.epistemic.label).toBe('Inferred');
  });

  it('the marking survives plain-text serialization of the machine answer', () => {
    const serialized = deterministicLayer(serveMachine(model([INFERRED_FACT])));
    expect(serialized).toContain('"label":"Inferred"');
    expect(serialized).toContain('"tier":"asserted-by-worker"');
  });

  it('falsifier: an inferred value re-served as Observed is a cross-channel-detectable difference, not a cosmetic one', () => {
    // If any channel stripped the Inferred marking, the comparison
    // oracle would catch it as a label disagreement — the
    // indistinguishability the requirement prohibits cannot pass as
    // presentation.
    const honest = disclosureOf(serveMachine(model([INFERRED_FACT])));
    const stripped = disclosureOf(
      serveMachine(model([{ ...INFERRED_FACT, epistemic: { label: 'Observed', tier: 'asserted-by-worker' } }])),
    );
    const comparison = compareRenderings(honest, stripped);
    if (comparison.comparable !== true || comparison.verdict !== 'parity-defect') {
      throw new Error('the stripped marking must be detected');
    }
    expect(comparison.disagreements[0]).toMatchObject({
      factName: 'summary-of-intent',
      facet: 'label',
      inFirst: 'Inferred',
      inSecond: 'Observed',
    });
  });

  it('an owning authority is citable as a basis, with its governing revision', () => {
    const admission = citeBasis({
      kind: 'owning-authority',
      authority: 'openspec-change:project-registration-and-honest-shape-visibility',
      governingRevision: 'digest:spec-rev-7',
    });
    if (!admission.cited) throw new Error('the owning authority must be citable');
    expect(admission.basis.authority).toBe(
      'openspec-change:project-registration-and-honest-shape-visibility',
    );
    expect(admission.basis.governingRevision).toBe('digest:spec-rev-7');
  });

  it('falsifier: a generated presentation artifact offered as a source is refused, with the lawful route named', () => {
    const admission = citeBasis({
      kind: 'generated-presentation',
      artifact: 'rendered-status-page.html',
      rendersAuthority: 'openspec-change:project-registration-and-honest-shape-visibility',
    });
    expect(admission.cited).toBe(false);
    if (admission.cited) throw new Error('unreachable');
    expect(admission.refusal).toBe('generated-presentation-is-never-a-source');
    expect(admission.route).toBe(
      'cite the owning authority the artifact renders: openspec-change:project-registration-and-honest-shape-visibility',
    );
    // The refusal arm carries NO basis field — the generated page can
    // never leak through as a cited source.
    expect(Object.keys(admission).sort()).toEqual(['artifact', 'cited', 'refusal', 'route']);
  });

  it('sweep: every served fact of the fixture carries a label from the closed three', () => {
    const facts = [OBSERVED_FACT, INFERRED_FACT];
    // Denominator disclosed: the whole served-fact set of the fixture.
    expect(facts.length).toBe(2);
    for (const fact of facts) {
      expect(EPISTEMIC_LABELS.includes(fact.epistemic.label)).toBe(true);
    }
  });
});
