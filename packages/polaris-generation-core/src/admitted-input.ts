/**
 * Typed admitted-input seam (N8 slice 3, syzygy-u05.8; relates syzygy-mea).
 *
 * REQ-polaris-generation-030 ("Accounted unfamiliar-project discovery",
 * openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md:527)
 * requires the generator to "expose the selected project boundary and
 * audience, admitted source classes, ... inspected and selected material,
 * and reasons relevant material is excluded, unavailable, unresolved or
 * deferred by budget" before claiming source coverage. The later
 * GenerationSource seam in ./generation-source.ts binds material to its
 * repository/object/evaluation; this flat population remains a caller-side
 * selection and accounting boundary, never provider authority.
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
 * `selected` uses the `{ sourceId, text }` shape `validateStage` checks at
 * the provider-local validation seam. Callers must form validated
 * GenerationSource records before constructing a PipelineRequest.
 *
 * `validateStage` runs on a provider-local *reply*. `admitSourcePopulation`
 * fails closed before this flat selection is converted to bound sources,
 * applying `sourceSchema`'s own `sourceId` handle pattern and `text` upper
 * bound (imported from ./provider-draft.ts, not duplicated) before any
 * source is ever admitted.
 */

import { SOURCE_ID_MAX_LENGTH, SOURCE_ID_PATTERN, SOURCE_TEXT_MAX_LENGTH } from './provider-draft.js';

const sourceIdHandle = new RegExp(SOURCE_ID_PATTERN, 'u');

/** Why material a caller considered was not admitted. Mirrors
 * REQ-polaris-generation-030's own four non-selection reasons verbatim:
 * "excluded, unavailable, unresolved or deferred by budget". */
export type SourceExclusionReason = 'excluded' | 'unavailable' | 'unresolved' | 'deferred-by-budget';

/** One caller-selected flat source, before observation binding. */
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
  | 'empty-source-id' | 'empty-text' | 'empty-detail' | 'duplicate-source-id'
  | 'invalid-source-id' | 'text-too-long';

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
 *
 * Each `selected` source's `sourceId` must additionally match `sourceSchema`'s
 * own handle pattern (./provider-draft.ts's `SOURCE_ID_PATTERN`, length-bounded
 * by `SOURCE_ID_MAX_LENGTH`; the regex itself already requires at least one
 * character) and its `text` must not exceed `SOURCE_TEXT_MAX_LENGTH` -- the
 * same pattern and bound `validateStage` enforces against `context.sources`,
 * applied here before a source is converted to a GenerationSource. This flat
 * selection alone cannot reach `ports.generate`.
 */
export function admitSourcePopulation(
  selected: readonly AdmittedSource[],
  excluded: readonly ExcludedSource[] = [],
): SourcePopulation {
  const seen = new Set<string>();
  for (const source of selected) {
    if (source.sourceId.length === 0) throw new SourcePopulationError('empty-source-id');
    if ([...source.sourceId].length > SOURCE_ID_MAX_LENGTH || !sourceIdHandle.test(source.sourceId)) {
      throw new SourcePopulationError('invalid-source-id');
    }
    if (source.text.length === 0) throw new SourcePopulationError('empty-text');
    if ([...source.text].length > SOURCE_TEXT_MAX_LENGTH) throw new SourcePopulationError('text-too-long');
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

/** The caller-selected flat sources in original order. Each must separately
 * gain an observation-bound GenerationSource before a pipeline request. */
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
