import type { PromptStage } from '@syzygy/polaris-generation-core';

/**
 * Which provider stages an in-force egress record authorises, by the SHA-256 of
 * the record's exact bytes (the argument of the owner act that put it in force;
 * the admission reader only reports a record whose bytes still hash to it).
 *
 * A record's request table lists the stages it covers. The first egress version
 * lists the six narrative stages; the second also lists the two discovery
 * stages. Wiring cannot read the table out of the record, so the stage list is
 * pinned here by digest, and a digest that is not in this map authorises
 * nothing: an unknown, edited or future record opens no stage (fail closed).
 *
 * The digests are the manifest rows of the two packages; a test re-reads both
 * manifests and the candidate bytes, so editing a record without updating this
 * map fails the build. `scripts/install_redis_sitting.py` is asked to check the
 * same equality against the performed act records.
 */
export const NARRATIVE_STAGES = ['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair'] as const satisfies readonly PromptStage[];
export const DISCOVERY_STAGES = ['discovery-map', 'discovery-reduce'] as const satisfies readonly PromptStage[];

/** Row of `public-repo-admission/PUBLIC-REPO-ADMISSION-MANIFEST.txt`: egress version 0.1.0-candidate.7. */
export const EGRESS_V1_DIGEST = 'cbae0a845b1086e1371906536f8b96d742317ad87fb3967362687b083adaf073';
/** Row of `public-egress-v2/PUBLIC-EGRESS-V2-MANIFEST.txt`: egress version 0.2.0-candidate.1 (act pending, sitting row 8). */
export const EGRESS_V2_DIGEST = '2a97b98f0e707b39ee06bdc8f9e0d1f8cd351bddd2a09312c9c4a7302b2bbf3e';

export const EGRESS_STAGE_AUTHORITY: ReadonlyMap<string, readonly PromptStage[]> = new Map<string, readonly PromptStage[]>([
  [EGRESS_V1_DIGEST, Object.freeze([...NARRATIVE_STAGES])],
  [EGRESS_V2_DIGEST, Object.freeze([...NARRATIVE_STAGES, ...DISCOVERY_STAGES])],
]);

/** The stages the record with this digest authorises; none for an unknown digest or for no record. */
export function stagesAuthorisedBy(digest: string | null | undefined): readonly PromptStage[] {
  return typeof digest === 'string' ? EGRESS_STAGE_AUTHORITY.get(digest) ?? [] : [];
}

export const stageAuthorisedBy = (digest: string | null | undefined, stage: PromptStage): boolean => stagesAuthorisedBy(digest).includes(stage);
