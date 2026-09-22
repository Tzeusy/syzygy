/**
 * Typed admitted-input seam (N8 slice 3, syzygy-u05.8; relates syzygy-mea).
 *
 * REQ-polaris-generation-030 ("Accounted unfamiliar-project discovery",
 * openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md:527)
 * requires the generator to "expose the selected project boundary and
 * audience, admitted source classes, ... inspected and selected material,
 * and reasons relevant material is excluded, unavailable, unresolved or
 * deferred by budget" before claiming source coverage. Today's pipeline
 * front door (`PipelineRequest.sources` in ./pipeline.ts) carries that
 * material as `unknown` -- an untyped population with no produced
 * denominator, the gap the 2026-09-22 vision-pursuit dossier's L3-F1
 * names as "no front door means no denominator".
 *
 * This module is the pure port type that names the seam: a `SourcePopulation`
 * is every source a caller considered, partitioned into what was admitted
 * (`selected`, sent to the model) and what was not (`excluded`, kept for
 * accounting only and never sent). It performs no discovery of its own --
 * no repository walk, no filesystem or network read, no provider call -- it
 * only types and validates a population the caller already assembled.
 * Building the actual bounded-discovery behaviour REQ-030 describes (reading
 * a project to produce this population) is new observable generator
 * behaviour gated by syzygy-mea ("current PWB consent does not authorize
 * second-project reads or provider egress"; "must be reconciled and adopted
 * before new observable implementation") and is out of this seam's scope.
 *
 * `selected` uses the exact `{ sourceId, text }` shape `validateStage` in
 * ./provider-draft.ts already enforces at runtime against `context.sources`
 * (its `sourceSchema`); this module only gives that shape a name and a
 * static type at the front door, it does not change what that runtime
 * schema accepts.
 */

/** Why material a caller considered was not admitted. Mirrors
 * REQ-polaris-generation-030's own four non-selection reasons verbatim:
 * "excluded, unavailable, unresolved or deferred by budget". */
export type SourceExclusionReason = 'excluded' | 'unavailable' | 'unresolved' | 'deferred-by-budget';

/** One admitted source: inspected, selected, and sent to the model. */
export interface AdmittedSource {
  readonly sourceId: string;
  readonly text: string;
}

/** One considered-but-not-admitted source: never sent to the model. Its
 * content is not carried here -- only the accounting the owner needs to
 * see the denominator, per REQ-030's exposure requirement. */
export interface ExcludedSource {
  readonly sourceId: string;
  readonly reason: SourceExclusionReason;
  readonly detail: string;
}

/** The population a generation request may draw on: a produced denominator
 * (`selected.length + excluded.length`), not a hardcoded one. */
export interface SourcePopulation {
  readonly selected: readonly AdmittedSource[];
  readonly excluded: readonly ExcludedSource[];
}

export type SourcePopulationFailure =
  | 'empty-source-id' | 'empty-text' | 'empty-detail' | 'duplicate-source-id';

/** Diagnostics deliberately contain no source content or ids beyond the code. */
export class SourcePopulationError extends Error {
  constructor(readonly code: SourcePopulationFailure) {
    super(`Source population rejected: ${code}`);
    this.name = 'SourcePopulationError';
  }
}

/**
 * Admits a caller-assembled population as a typed `SourcePopulation`. Pure:
 * reads no source, performs no discovery, changes nothing about what the
 * caller already decided to select or exclude -- it only validates the two
 * lists are well-formed and carry no id twice across the whole population,
 * so the denominator (`sourcePopulationDenominator`) is trustworthy.
 */
export function admitSourcePopulation(
  selected: readonly AdmittedSource[],
  excluded: readonly ExcludedSource[] = [],
): SourcePopulation {
  const seen = new Set<string>();
  for (const source of selected) {
    if (source.sourceId.length === 0) throw new SourcePopulationError('empty-source-id');
    if (source.text.length === 0) throw new SourcePopulationError('empty-text');
    if (seen.has(source.sourceId)) throw new SourcePopulationError('duplicate-source-id');
    seen.add(source.sourceId);
  }
  for (const source of excluded) {
    if (source.sourceId.length === 0) throw new SourcePopulationError('empty-source-id');
    if (source.detail.length === 0) throw new SourcePopulationError('empty-detail');
    if (seen.has(source.sourceId)) throw new SourcePopulationError('duplicate-source-id');
    seen.add(source.sourceId);
  }
  return { selected, excluded };
}

/** The admitted sources, and only the admitted sources, in original order --
 * exactly what a pipeline front door may place on `PipelineRequest.sources`.
 * Excluded material never reaches this projection or the model. */
export function admittedSources(population: SourcePopulation): readonly AdmittedSource[] {
  return population.selected;
}

/** The produced denominator REQ-030 requires be exposed before claiming
 * source coverage: how many considered sources were admitted, how many were
 * not, and the total considered. Purely computed from the population. */
export function sourcePopulationDenominator(population: SourcePopulation): {
  readonly selected: number;
  readonly excluded: number;
  readonly total: number;
} {
  return {
    selected: population.selected.length,
    excluded: population.excluded.length,
    total: population.selected.length + population.excluded.length,
  };
}
