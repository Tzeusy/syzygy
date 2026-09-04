/**
 * Polaris narrative claim blocks (PWB-REQ-014; RFC7-2, RFC7-3, RFC7-9).
 *
 * Every owner-visible narrative unit on Polaris carries exactly one claim
 * role plus the `presentation-artifact` and `non-citable` attributes. An
 * anchored block additionally carries a typed, revision-bound anchor set that
 * covers every claim it renders and contains no unused anchor. Blocks use
 * their own machine type — never the kernel claim tuple — and the whole
 * structure is a presentation artifact: deleting it leaves `/api/poc`
 * byte-identical, because nothing here is written back onto the model.
 */
import type {
  PocProvenance,
  ProjectShapeClaim,
  ProjectShapeSupport,
  ProposedWork,
} from '@syzygy/three-surface-poc-core';

export const NARRATIVE_CLAIM_ROLES = ['anchored-project-fact', 'non-normative-framing', 'epistemic-claim'] as const;
export type NarrativeClaimRole = (typeof NARRATIVE_CLAIM_ROLES)[number];

/** Closed anchor target classes (PWB-REQ-014). */
export const ANCHOR_TARGET_CLASSES = ['doctrine', 'contract', 'requirement', 'decision', 'evidence', 'work'] as const;
export type AnchorTargetClass = (typeof ANCHOR_TARGET_CLASSES)[number];

/** A reader must be able to tell which anchor supports which claim; beyond
 * this many anchors a block is ambiguous by construction. */
export const MAX_ANCHORS_PER_BLOCK = 6;

export interface CapturedTargetState {
  readonly label: string;
  readonly tier: string;
  readonly reason: string;
}

export interface NarrativeAnchor {
  readonly anchorId: string;
  readonly targetClass: AnchorTargetClass;
  /** Durable target identity — a registry identity, digest or revision;
   * never a label, a bare path or a line coordinate. */
  readonly targetId: string;
  readonly revision: string;
  /** Claim ids inside the block that this anchor supports. */
  readonly supports: readonly string[];
  /** The target's state as captured at render time; frozen, never re-read. */
  readonly captured: CapturedTargetState;
  /** Human locator (path[:line]) — display only, not identity. */
  readonly locator: string;
}

export interface NarrativeBlock {
  readonly kind: 'narrative-block';
  readonly blockId: string;
  readonly role: NarrativeClaimRole;
  readonly presentation: 'presentation-artifact';
  readonly citable: false;
  readonly claims: readonly string[];
  readonly anchors: readonly NarrativeAnchor[];
}

export interface PolarisNarrative {
  readonly kind: 'polaris-narrative';
  readonly presentation: 'presentation-artifact';
  readonly citable: false;
  readonly roles: readonly NarrativeClaimRole[];
  readonly anchorTargetClasses: readonly AnchorTargetClass[];
  readonly blocks: readonly NarrativeBlock[];
}

/** Personal view state (which on-demand blocks start open). It lives here,
 * outside the truth model, and changes only presentation. */
export interface PolarisViewState {
  readonly openCoverageCounts?: readonly string[];
}

export function claimRoleAttrs(role: NarrativeClaimRole): string {
  return ` data-claim-role="${role}" data-presentation-artifact data-non-citable`;
}

const PROVENANCE_CLASS: Readonly<Record<PocProvenance['kind'], AnchorTargetClass>> = {
  'repository-file': 'evidence',
  'git-revision': 'evidence',
  'manual-mapping': 'evidence',
  'materialization-record': 'work',
  'test-artifact-record': 'evidence',
  'project-shape-source': 'evidence',
  'owner-act': 'decision',
};

export interface AnchorInput {
  readonly targetClass: AnchorTargetClass;
  readonly targetId: string;
  readonly revision: string;
  readonly locator: string;
}

export function provenanceAnchor(item: PocProvenance): AnchorInput {
  return {
    targetClass: PROVENANCE_CLASS[item.kind],
    targetId: `${item.kind}:${item.digest ?? item.revision}`,
    revision: item.revision,
    locator: item.source,
  };
}

/** Shape support: the registry's `git-tree-entry` identity when the source is
 * in the population, else the exact content digest. */
export function supportAnchor(support: ProjectShapeSupport, revision: string, targetClass: AnchorTargetClass = 'evidence'): AnchorInput | undefined {
  const targetId = support.sourceIdentity ?? (support.contentDigest === undefined ? undefined : `sha256:${support.contentDigest}`);
  if (targetId === undefined) return undefined;
  return {
    targetClass,
    targetId,
    revision,
    locator: support.line === undefined ? support.path : `${support.path}:${support.line}`,
  };
}

export function artifactAnchor(artifact: ProposedWork['proposal'], targetClass: AnchorTargetClass): AnchorInput {
  return { targetClass, targetId: artifact.digest, revision: artifact.revision, locator: artifact.path };
}

export function capturedStateOf(claim: ProjectShapeClaim): CapturedTargetState {
  const epistemic = claim.epistemic;
  const reason = 'reasons' in epistemic ? epistemic.reasons.primary : 'basis' in epistemic ? epistemic.basis : 'none';
  return { label: epistemic.label, tier: epistemic.tier ?? 'unstated', reason };
}

function deepFreeze<T>(value: T): T {
  if (value !== null && typeof value === 'object') {
    for (const inner of Object.values(value as Record<string, unknown>)) deepFreeze(inner);
    Object.freeze(value);
  }
  return value;
}

/** Collects the blocks one render emits. Blocks are cloned and deep-frozen at
 * registration: a later mutation of the model cannot rewrite a captured
 * target state (PWB-REQ-014 later-read mutation case). */
export class NarrativeRegistry {
  private readonly blocks: NarrativeBlock[] = [];
  private readonly seen = new Set<string>();

  registerAnchored(blockId: string, claims: readonly string[], anchors: readonly (AnchorInput & { readonly supports: readonly string[]; readonly captured: CapturedTargetState })[]): NarrativeBlock {
    if (this.seen.has(blockId)) throw new Error(`narrative block registered twice: ${blockId}`);
    for (const claimId of claims) if (claimId.includes('\t')) throw new Error(`claim id carries a tab: ${claimId}`);
    this.seen.add(blockId);
    const block: NarrativeBlock = deepFreeze({
      kind: 'narrative-block',
      blockId,
      role: 'anchored-project-fact',
      presentation: 'presentation-artifact',
      citable: false,
      claims: [...claims],
      anchors: anchors.map((anchor, index) => ({
        anchorId: `${blockId}#a${index + 1}`,
        targetClass: anchor.targetClass,
        targetId: anchor.targetId,
        revision: anchor.revision,
        supports: [...anchor.supports],
        captured: { ...anchor.captured },
        locator: anchor.locator,
      })),
    });
    this.blocks.push(block);
    return block;
  }

  narrative(): PolarisNarrative {
    return deepFreeze({
      kind: 'polaris-narrative',
      presentation: 'presentation-artifact',
      citable: false,
      roles: [...NARRATIVE_CLAIM_ROLES],
      anchorTargetClasses: [...ANCHOR_TARGET_CLASSES],
      blocks: [...this.blocks],
    });
  }
}

export const NARRATIVE_SCRIPT_ID = 'polaris-narrative';

/** The machine form of the presentation artifact, embedded in the page. It is
 * not `/api/poc` and never becomes part of it. */
export function narrativeScript(narrative: PolarisNarrative): string {
  const json = JSON.stringify(narrative).replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
  return `<script type="application/json" id="${NARRATIVE_SCRIPT_ID}" data-presentation-artifact data-non-citable>${json}</script>`;
}

export function parseNarrativeScript(html: string): PolarisNarrative {
  const match = new RegExp(`<script type="application/json" id="${NARRATIVE_SCRIPT_ID}"[^>]*>([\\s\\S]*?)</script>`).exec(html);
  if (match === null) throw new Error('narrative script absent');
  return JSON.parse(match[1] as string) as PolarisNarrative;
}
