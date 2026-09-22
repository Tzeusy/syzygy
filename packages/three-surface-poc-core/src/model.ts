import { createHash } from 'node:crypto';
import { readFileSync, statSync } from 'node:fs';
import { resolve } from 'node:path';

import { observeCodeStructure, type CodeStructureResult } from './code-structure.js';
import { observeWorkItems, type WorkItemsResult } from './work-items.js';
import { observeWorkerChange, type WorkerChangeResult } from './worker-change-observation.js';
import { projectOrrery, type OrreryProjection } from './orrery-projection.js';
import { projectTrajectory, type TrajectoryProjection } from './trajectory-projection.js';
import type { MaterializationRecord } from './materialization.js';
import type { BodyReadAuthorityEvaluation } from './body-read-authority.js';
import { gitRunnerFor, type GitRunner, type PwbResourceLimits } from './project-shape-observation.js';
import { buildProjectShape, unevaluatedProjectShape, type ProjectShape } from './project-shape-model.js';
import { deriveProposedWork, type ProposedWork } from './proposed-work.js';
import {
  evaluateWalkthroughJudgment,
  type WalkthroughJudgmentEvaluation,
  type WalkthroughJudgmentInputs,
} from './walkthrough-judgment.js';
import {
  evaluateWalkthroughReadiness,
  walkthroughEvaluationIdentity,
  type ReadinessPopulation,
  type ReadinessTraversal,
  type WalkthroughReadiness,
} from './walkthrough-readiness.js';
import {
  resolveTestArtifactVerification,
  type TestArtifactRecord,
  type TestArtifactVerificationResult,
} from './test-artifact-verification.js';
import type { PocSeedEntity, PocSeedInput, PocSeedRelationship } from './poc-seeds.js';

const RECENT_CLOSED_WINDOW = 50;

export type PocEpistemic =
  { readonly label: 'Observed'; readonly basis: string } | { readonly label: 'Unknown'; readonly reason: string };

export interface PocProvenance {
  readonly kind:
    | 'repository-file'
    | 'git-revision'
    | 'manual-mapping'
    | 'materialization-record'
    | 'test-artifact-record'
    | 'project-shape-source'
    | 'owner-act';
  readonly source: string;
  readonly revision: string;
  readonly digest?: string | undefined;
}

export interface PocEntity {
  readonly id: string;
  readonly kind:
    | 'project'
    | 'capability'
    | 'intent'
    | 'work-item'
    | 'code-region'
    | 'test-definition'
    | 'test-evidence'
    | 'runtime'
    | 'unknown-region';
  readonly title: string;
  readonly detail: string;
  readonly epistemic: PocEpistemic;
  readonly provenance: readonly PocProvenance[];
}

export interface PocRelationship {
  readonly id: string;
  readonly kind: string;
  readonly from: string;
  readonly to: string;
  readonly statement: string;
  readonly epistemic: PocEpistemic;
  readonly provenance: readonly PocProvenance[];
}

export interface PocSurface {
  readonly id: 'polaris' | 'trajectory' | 'orrery';
  readonly title: string;
  readonly question: string;
  readonly entityIds: readonly string[];
  readonly relationshipIds: readonly string[];
}

export interface PocModel {
  readonly schema: 'syzygy-three-surface-poc/v1';
  readonly evaluation: {
    /** Human-oriented composite identity,
     * `<snapshotLabel>|inputs:sha256:<inputsDigest>`. Machine consumers
     * should read `snapshotLabel` and `inputsDigest` directly instead of
     * splitting this string. */
    readonly snapshot: string;
    /** The evaluation's human label, without the input-digest suffix. */
    readonly snapshotLabel: string;
    /** SHA-256 hex digest of the canonical observation inputs. */
    readonly inputsDigest: string;
    readonly asOf: string;
  };
  readonly project: {
    readonly name: string;
    readonly root: string;
    readonly revision: string;
  };
  readonly observerRevision: string;
  readonly capabilityId: string;
  readonly entities: readonly PocEntity[];
  readonly relationships: readonly PocRelationship[];
  readonly surfaces: readonly PocSurface[];
  readonly codeStructure: CodeStructureResult;
  readonly workItems: WorkItemsResult;
  readonly workerChange: WorkerChangeResult;
  readonly testArtifactVerification: TestArtifactVerificationResult;
  readonly orrery: OrreryProjection;
  readonly trajectory: TrajectoryProjection;
  /** The confirmed materialized Bead id, or null when nothing has been
   * materialized (or the record could not be confirmed against the
   * live-observed work items). The typed source for renderers — never
   * re-derived from human-readable entity text. */
  readonly materializedBeadId: string | null;
  /** The project-wide Butlers shape (PWB): body-read authority disclosure,
   * revision-bound source population, items, coverage, contradictions and
   * the project account, every fact with its complete epistemic tuple.
   * `not-evaluated` when the builder was given no authority evaluation —
   * nothing is read then. */
  readonly projectShape: ProjectShape;
  /** PWB-REQ-013: the one followed OpenSpec change as a distinct type, with its lifecycle and the current authority it would amend. */
  readonly proposedWork: ProposedWork;
  /** PWB-REQ-021/022: the owner's cold-open walkthrough judgment as the
   * PWB-REQ-022 evaluator carried it — lawful (state (1) or (2), verdict
   * carried), unlawful (no verdict), absent (no pair) — or `not-evaluated`
   * when the builder was given no run-record/judgment pair. Never a score,
   * never evidence of success. */
  readonly walkthroughJudgment: WalkthroughJudgmentPresentation;
  /** PWB-REQ-021 (as amended 2026-09-05): whether the retained walkthrough
   * record is a ready answer population against this evaluation — the nine
   * identities, resolved anchors, same surface and evaluation, Polaris-only
   * traversal, no PWB-REQ-006 breach, resolvable cited authority. An
   * execution fact only: never a verdict, never a score, and independent
   * of the PWB-REQ-022 outcome. `not-evaluated` when the builder was given
   * no run record or no traversal predicate. */
  readonly walkthroughReadiness: WalkthroughReadinessPresentation;
}

export type WalkthroughJudgmentInputsFor = (binding: {
  readonly evaluationIdentity: string;
}) => WalkthroughJudgmentInputs;

export type WalkthroughReadinessPresentation =
  | { readonly kind: 'not-evaluated'; readonly detail: string }
  | { readonly kind: 'evaluated'; readonly readiness: WalkthroughReadiness };

export type WalkthroughJudgmentPresentation =
  | { readonly kind: 'not-evaluated'; readonly detail: string }
  | {
      readonly kind: 'evaluated';
      readonly evaluation: WalkthroughJudgmentEvaluation;
    };

/** The lawful inputs of the project-shape pipeline: the PWB-REQ-005
 * evaluation the daemon performed against Syzygy's governance tree, plus
 * an injectable byte-level Git runner for hermetic tests. No Git command
 * is issued unless the evaluation admits. */
export interface ProjectShapeModelInput {
  readonly authority: BodyReadAuthorityEvaluation;
  readonly runGit?: GitRunner;
  readonly repositoryId?: string;
  /** The PWB-REQ-006 envelope; absent → the registry's `PWB_RESOURCE_LIMITS`. */
  readonly resourceLimits?: PwbResourceLimits;
}

export interface BuildPocModelInput {
  readonly repoRoot: string;
  readonly repositoryRevision: string;
  readonly observerRevision: string;
  readonly evaluation: { readonly snapshot: string; readonly asOf: string };
  /** Explicit implementation-plane seeds. Omitted means no seeded graph. */
  readonly seeds?: PocSeedInput;
  readonly runGit?: (repoRoot: string, args: readonly string[]) => string;
  readonly runWorkItemQuery?: (repoRoot: string, sql: string) => string;
  readonly materializationRecord?: MaterializationRecord | null;
  readonly testArtifactRecord?: TestArtifactRecord | null;
  /** Absent → `projectShape.kind === 'not-evaluated'` (no read); the
   * optional detail says why no evaluation was supplied. */
  readonly projectShape?: ProjectShapeModelInput | undefined;
  readonly projectShapeDetail?: string;
  /** Absent → `walkthroughJudgment.kind === 'not-evaluated'`; the optional
   * detail says why no pair was supplied. A function receives the exact
   * evaluation identity of the shape this build observed
   * (`walkthroughEvaluationIdentity`) so the pair's expectations bind to
   * it rather than to a placeholder; if it throws, the judgment and
   * readiness stay `not-evaluated` with the failure named. */
  readonly walkthroughJudgment?: WalkthroughJudgmentInputs | WalkthroughJudgmentInputsFor | undefined;
  readonly walkthroughJudgmentDetail?: string;
  /** PWB-REQ-021 readiness needs the surface's own traversal predicate
   * (which routes are Polaris and its same-evaluation exact-source route);
   * the run record comes from `walkthroughJudgment` and the source
   * population from the built project shape. Absent →
   * `walkthroughReadiness.kind === 'not-evaluated'`. */
  readonly walkthroughReadiness?: { readonly traversal: ReadinessTraversal } | undefined;
}

/** The same-evaluation source population readiness resolves against: the
 * observed shape's complete source list (admitted = classified body) and
 * its PWB-REQ-006 breach count; `unavailable` when no shape was observed. */
function readinessPopulation(projectShape: ProjectShape): ReadinessPopulation {
  if (projectShape.kind !== 'observed') {
    return {
      kind: 'unavailable',
      reason: `project shape ${projectShape.kind}: no same-evaluation source population`,
    };
  }
  return {
    kind: 'observed',
    sources: projectShape.sources.map((source) => ({
      path: source.path,
      admitted: source.record.outcome === 'classified',
    })),
    limitBreaches: projectShape.limitBreaches.length,
  };
}

export class PocObservationError extends Error {
  constructor(
    readonly kind: 'required-artifact-missing' | 'required-artifact-semantic-mismatch' | 'required-artifact-unreadable',
    readonly artifactPath?: string,
  ) {
    super(artifactPath === undefined ? kind : `${kind}: ${artifactPath}`);
    this.name = 'PocObservationError';
  }
}

interface ObservedArtifact {
  readonly path: string;
  readonly digest: string;
}

function sha256(bytes: Uint8Array | string): string {
  return createHash('sha256').update(bytes).digest('hex');
}

function observeArtifact(
  repoRoot: string,
  artifactPath: string,
  requiredMarkers: readonly string[] = [],
): ObservedArtifact {
  const absolutePath = resolve(repoRoot, artifactPath);
  try {
    if (!statSync(absolutePath).isFile()) {
      throw new PocObservationError('required-artifact-unreadable', artifactPath);
    }
    const bytes = readFileSync(absolutePath);
    if (requiredMarkers.some((marker) => !bytes.includes(Buffer.from(marker, 'utf8')))) {
      throw new PocObservationError('required-artifact-semantic-mismatch', artifactPath);
    }
    return { path: artifactPath, digest: sha256(bytes) };
  } catch (cause) {
    if (cause instanceof PocObservationError) {
      throw cause;
    }
    if ((cause as NodeJS.ErrnoException).code === 'ENOENT') {
      throw new PocObservationError('required-artifact-missing', artifactPath);
    }
    throw new PocObservationError('required-artifact-unreadable', artifactPath);
  }
}

function fileProvenance(artifact: ObservedArtifact, repositoryRevision: string): PocProvenance {
  return {
    kind: 'repository-file',
    source: artifact.path,
    revision: repositoryRevision,
    digest: `sha256:${artifact.digest}`,
  };
}

function observed(basis: string): PocEpistemic {
  return { label: 'Observed', basis };
}

function unknown(reason: string): PocEpistemic {
  return { label: 'Unknown', reason };
}

interface MaterializationEpistemic {
  readonly epistemic: PocEpistemic;
  readonly beadId: string | null;
  /** From the record's origin field; null for pre-origin records, where
   * only "created or reused" can be honestly claimed. */
  readonly origin: 'created' | 'reused' | null;
  readonly provenance: readonly PocProvenance[];
}

/**
 * A materialization record is local, human-authored state — it becomes
 * an Observed claim only once the named Bead is confirmed present in
 * this same evaluation's live-observed work items, never from the
 * record file alone (VIS-2: a claim needs resolvable, current
 * provenance, not a memory of a past write).
 */
function resolveMaterializationEpistemic(
  record: MaterializationRecord | null,
  workItems: WorkItemsResult,
): MaterializationEpistemic {
  if (record === null) {
    return {
      epistemic: unknown('No POC work item has been materialized.'),
      beadId: null,
      origin: null,
      provenance: [],
    };
  }
  if (workItems.kind === 'unknown') {
    return {
      epistemic: unknown('A materialization record exists but work items could not be observed to confirm it.'),
      beadId: null,
      origin: null,
      provenance: [],
    };
  }
  const found = workItems.items.find((item) => item.id === record.beadId);
  if (found === undefined) {
    return {
      epistemic: unknown('A materialization record names a Bead that was not found among the observed work items.'),
      beadId: null,
      origin: null,
      provenance: [],
    };
  }
  return {
    epistemic: observed(`The materialized Bead ${found.id} was confirmed present in the observed work items.`),
    beadId: found.id,
    origin: record.origin ?? null,
    provenance: [
      {
        kind: 'materialization-record',
        source: `Beads (${workItems.beadPrefix}) — ${found.id}`,
        revision: workItems.doltRevision,
      },
    ],
  };
}

interface SeedObservationContext {
  readonly artifacts: Readonly<Record<'design' | 'proposal' | 'requirement' | 'code' | 'test', ObservedArtifact>>;
  readonly mappingProvenance: PocProvenance;
  readonly gitProvenance: PocProvenance;
  readonly materialization: MaterializationEpistemic;
}

function renderSeedText(text: string, seeds: PocSeedInput): string {
  return text.replace(
    /\{(projectName|codePath|testPath)\}/g,
    (_match, key: 'projectName' | 'codePath' | 'testPath') => {
      if (key === 'projectName') return seeds.project.displayName;
      if (key === 'codePath') return seeds.artifacts.code;
      return seeds.artifacts.test;
    },
  );
}

function entityFromSeed(seed: PocSeedEntity, seeds: PocSeedInput, context: SeedObservationContext): PocEntity {
  const title = renderSeedText(seed.title, seeds);
  const detail = renderSeedText(seed.detail, seeds);
  switch (seed.role) {
    case 'project':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: observed('Git reported the configured repository revision.'),
        provenance: [context.gitProvenance],
      };
    case 'capability':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: observed('Validated intent markers name this capability and record approval.'),
        provenance: [
          fileProvenance(context.artifacts.design, context.gitProvenance.revision),
          fileProvenance(context.artifacts.requirement, context.gitProvenance.revision),
        ],
      };
    case 'intent':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: observed('Required approval, identifier, and relationship markers were validated.'),
        provenance: [
          fileProvenance(context.artifacts.design, context.gitProvenance.revision),
          fileProvenance(context.artifacts.proposal, context.gitProvenance.revision),
          fileProvenance(context.artifacts.requirement, context.gitProvenance.revision),
        ],
      };
    case 'code':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: observed('The manually mapped code file was captured and hashed.'),
        provenance: [fileProvenance(context.artifacts.code, context.gitProvenance.revision), context.mappingProvenance],
      };
    case 'test-definition':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: observed('The manually mapped test file was captured and hashed.'),
        provenance: [fileProvenance(context.artifacts.test, context.gitProvenance.revision), context.mappingProvenance],
      };
    case 'work':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail:
          context.materialization.beadId === null
            ? detail
            : `Materialized as Beads item ${context.materialization.beadId}.`,
        epistemic: context.materialization.epistemic,
        provenance: context.materialization.provenance,
      };
    case 'test-evidence':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: unknown('No test artifact has been captured for this evaluation.'),
        provenance: [],
      };
    case 'runtime':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: unknown('No current runtime observation was supplied.'),
        provenance: [],
      };
    case 'unknown-region':
      return {
        id: seed.id,
        kind: seed.kind,
        title,
        detail,
        epistemic: unknown('The first slice does not enumerate or map the remaining code.'),
        provenance: [],
      };
  }
}

function relationshipFromSeed(
  seed: PocSeedRelationship,
  seeds: PocSeedInput,
  context: SeedObservationContext,
): PocRelationship {
  const statement = renderSeedText(seed.statement, seeds);
  switch (seed.role) {
    case 'project-to-capability':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: observed('The selected requirement is present in the configured repository.'),
        provenance: [fileProvenance(context.artifacts.requirement, context.gitProvenance.revision)],
      };
    case 'capability-to-intent':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: observed('The relationship is declared by the bounded POC mapping.'),
        provenance: [
          fileProvenance(context.artifacts.requirement, context.gitProvenance.revision),
          context.mappingProvenance,
        ],
      };
    case 'capability-to-code':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: observed('The mapping and mapped file are both identified.'),
        provenance: [fileProvenance(context.artifacts.code, context.gitProvenance.revision), context.mappingProvenance],
      };
    case 'capability-to-test-definition':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: observed('The mapping and mapped file are both identified.'),
        provenance: [fileProvenance(context.artifacts.test, context.gitProvenance.revision), context.mappingProvenance],
      };
    case 'intent-to-work':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic:
          context.materialization.beadId === null
            ? unknown('The human-triggered materialization step has not run.')
            : observed(
                `The human-triggered materialization step ${context.materialization.origin === 'created' ? 'created' : context.materialization.origin === 'reused' ? 'reused the existing' : 'created or reused'} Beads item ${context.materialization.beadId}.`,
              ),
        provenance: context.materialization.provenance,
      };
    case 'work-to-code':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: unknown('No materialized work item or worker change was supplied.'),
        provenance: [],
      };
    case 'code-to-evidence':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: unknown('No test artifact has been captured for this evaluation.'),
        provenance: [],
      };
    case 'code-to-runtime':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: unknown('No current runtime observation was supplied.'),
        provenance: [],
      };
    case 'capability-to-unmapped-region':
      return {
        id: seed.id,
        kind: seed.kind,
        from: seed.from,
        to: seed.to,
        statement,
        epistemic: unknown('The bounded POC mapping makes no claim about other code.'),
        provenance: [],
      };
  }
}

function capabilityIdFromSeeds(seeds: PocSeedInput): string {
  return seeds.entities.find((entity) => entity.role === 'capability')?.id ?? 'capability:unknown';
}

function snapshotLabelFor(input: BuildPocModelInput, seeds: PocSeedInput | undefined): string {
  if (seeds === undefined) return input.evaluation.snapshot;
  return input.evaluation.snapshot.replace(/^(?:butlers|Butlers)(?=[:@|])/, seeds.project.repositoryId);
}

function emptyProposedWork(input: BuildPocModelInput): ProposedWork {
  const artifact = {
    path: '',
    revision: input.repositoryRevision,
    digest: 'sha256:',
  };
  return {
    kind: 'proposed-work',
    id: 'proposed-work:unknown',
    changeId: 'unknown',
    capabilityId: 'capability:unknown',
    specKey: 'unknown',
    proposal: artifact,
    delta: artifact,
    lifecycle: {
      kind: 'unknown',
      reason: 'No seeded proposed-work artifacts were supplied to this evaluation.',
    },
    currentAuthority: {
      kind: 'unknown',
      reason: 'No seeded proposed-work artifacts were supplied to this evaluation.',
      route: 'Supply an implementation-plane seed set, then create a new evaluation.',
      detail: 'The proposed-work graph was not evaluated because no seed set was supplied.',
    },
  };
}

export function buildPocModel(input: BuildPocModelInput): PocModel {
  const repoRoot = resolve(input.repoRoot);
  const seeds = input.seeds;
  const seedArtifacts =
    seeds === undefined
      ? undefined
      : {
          design: observeArtifact(repoRoot, seeds.artifacts.design, seeds.intentMarkers.design),
          proposal: observeArtifact(repoRoot, seeds.artifacts.proposal, seeds.intentMarkers.proposal),
          requirement: observeArtifact(repoRoot, seeds.artifacts.requirement, seeds.intentMarkers.requirement),
          code: observeArtifact(repoRoot, seeds.artifacts.code),
          test: observeArtifact(repoRoot, seeds.artifacts.test),
        };
  const mappingDigest =
    seeds === undefined
      ? undefined
      : sha256(
          JSON.stringify({
            ARTIFACT_PATHS: seeds.artifacts,
            INTENT_MARKERS: seeds.intentMarkers,
          }),
        );
  const inputDigest = sha256(
    JSON.stringify({
      repoRoot,
      repositoryRevision: input.repositoryRevision,
      observerRevision: input.observerRevision,
      artifacts:
        seedArtifacts === undefined
          ? []
          : [
              seedArtifacts.design,
              seedArtifacts.proposal,
              seedArtifacts.requirement,
              seedArtifacts.code,
              seedArtifacts.test,
            ],
      mappingDigest,
    }),
  );
  const mappingProvenance: PocProvenance | undefined =
    mappingDigest === undefined
      ? undefined
      : {
          kind: 'manual-mapping',
          source: 'packages/three-surface-poc-core/src/model.ts#ARTIFACT_PATHS',
          revision: input.observerRevision,
          digest: `sha256:${mappingDigest}`,
        };
  const gitProvenance: PocProvenance = {
    kind: 'git-revision',
    source: seeds?.project.provenanceSource ?? 'Observed repository',
    revision: input.repositoryRevision,
  };

  const codeStructure = observeCodeStructure({
    repoRoot,
    revision: input.repositoryRevision,
    capturedAt: input.evaluation.asOf,
    ...(input.runGit === undefined ? {} : { runGit: input.runGit }),
  });
  const workItems =
    seeds === undefined
      ? {
          kind: 'unknown' as const,
          reason: 'No seed-backed work-item prefix was supplied to this evaluation.',
        }
      : observeWorkItems({
          repoRoot,
          beadPrefix: seeds.beadPrefix,
          capturedAt: input.evaluation.asOf,
          ...(input.runWorkItemQuery === undefined ? {} : { runQuery: input.runWorkItemQuery }),
        });
  const materialization = resolveMaterializationEpistemic(input.materializationRecord ?? null, workItems);
  const workerChange =
    seeds === undefined
      ? {
          kind: 'unknown' as const,
          reason: 'No seed-backed worker-change seam was supplied to this evaluation.',
        }
      : observeWorkerChange({
          repoRoot,
          beadId: materialization.beadId,
          seam: seeds.workerChangeSeam,
          capturedAt: input.evaluation.asOf,
          ...(input.runGit === undefined ? {} : { runGit: input.runGit }),
        });
  const observedChangeCommit =
    workerChange.kind === 'observed' && workerChange.state === 'changed-or-merged' && workerChange.commit !== null
      ? workerChange.commit.sha
      : null;
  const observedChangeCommitAuthoredAt =
    workerChange.kind === 'observed' && workerChange.commit !== null ? workerChange.commit.authoredAt : null;
  const testArtifactVerification =
    seeds === undefined
      ? {
          kind: 'unknown' as const,
          reason: 'No seed-backed test-artifact scope was supplied to this evaluation.',
        }
      : resolveTestArtifactVerification({
          record: input.testArtifactRecord ?? null,
          expectedScope: seeds.workerChangeSeam.testPath,
          observedCommit: observedChangeCommit,
          commitAuthoredAt: observedChangeCommitAuthoredAt,
          evaluationAsOf: input.evaluation.asOf,
        });

  const context: SeedObservationContext | undefined =
    seeds === undefined || seedArtifacts === undefined || mappingProvenance === undefined
      ? undefined
      : {
          artifacts: seedArtifacts,
          mappingProvenance,
          gitProvenance,
          materialization,
        };
  const entities: readonly PocEntity[] =
    seeds === undefined || context === undefined
      ? []
      : seeds.entities.map((seed) => entityFromSeed(seed, seeds, context));
  const relationships: readonly PocRelationship[] =
    seeds === undefined || context === undefined
      ? []
      : seeds.relationships.map((seed) => relationshipFromSeed(seed, seeds, context));

  const orreryProjection =
    seeds === undefined
      ? {
          kind: 'unknown' as const,
          reason: 'No seed-backed capability-to-path mappings were supplied to this evaluation.',
          observedFileCount: codeStructure.kind === 'observed' ? codeStructure.files.length : 0,
          mappedFileCount: 0,
          unmappedFileCount: codeStructure.kind === 'observed' ? codeStructure.files.length : 0,
          totalFileCount: codeStructure.kind === 'observed' ? codeStructure.files.length : 0,
        }
      : projectOrrery(codeStructure, seeds.orreryMappings);
  const trajectoryProjection =
    seeds === undefined
      ? {
          kind: 'unknown' as const,
          reason: 'No seed-backed work-item graph was supplied to this evaluation.',
          observedItemCount: workItems.kind === 'observed' ? workItems.items.length : 0,
        }
      : projectTrajectory(workItems, {
          recentClosedWindow: RECENT_CLOSED_WINDOW,
        });
  const projectShape: ProjectShape =
    input.projectShape === undefined
      ? unevaluatedProjectShape(
          input.projectShapeDetail ??
            'No body-read authority evaluation was supplied to this evaluation; no project-shape source was read.',
        )
      : buildProjectShape({
          authority: input.projectShape.authority,
          revision: input.repositoryRevision,
          capturedAt: input.evaluation.asOf,
          runGit: input.projectShape.runGit ?? gitRunnerFor(repoRoot),
          ...(input.projectShape.repositoryId === undefined ? {} : { repositoryId: input.projectShape.repositoryId }),
          ...(input.projectShape.resourceLimits === undefined
            ? {}
            : { resourceLimits: input.projectShape.resourceLimits }),
        });
  // The pair's expectations bind to the exact evaluation this build
  // observed; a loader that fails leaves both states `not-evaluated`.
  let walkthroughInputs: WalkthroughJudgmentInputs | undefined;
  let walkthroughDetail = input.walkthroughJudgmentDetail;
  if (typeof input.walkthroughJudgment === 'function') {
    try {
      walkthroughInputs = input.walkthroughJudgment({
        evaluationIdentity: walkthroughEvaluationIdentity(projectShape),
      });
    } catch (error: unknown) {
      walkthroughDetail = `Walkthrough-judgment inputs could not be loaded: ${error instanceof Error ? error.message : String(error)}`;
    }
  } else {
    walkthroughInputs = input.walkthroughJudgment;
  }
  const walkthroughJudgment: WalkthroughJudgmentPresentation =
    walkthroughInputs === undefined
      ? {
          kind: 'not-evaluated',
          detail:
            walkthroughDetail ??
            'No cold-open walkthrough run record and judgment pair was supplied to this evaluation; no judgment was evaluated.',
        }
      : {
          kind: 'evaluated',
          evaluation: evaluateWalkthroughJudgment(walkthroughInputs),
        };
  const walkthroughReadiness: WalkthroughReadinessPresentation =
    walkthroughInputs === undefined
      ? {
          kind: 'not-evaluated',
          detail:
            walkthroughDetail ??
            'No cold-open walkthrough run record was supplied to this evaluation; no answer population was assessed.',
        }
      : input.walkthroughReadiness === undefined
        ? {
            kind: 'not-evaluated',
            detail:
              'No Polaris traversal predicate was supplied to this evaluation; readiness cannot tell Polaris routes from others.',
          }
        : {
            kind: 'evaluated',
            readiness: evaluateWalkthroughReadiness({
              runRecord: walkthroughInputs.runRecord,
              expectations: {
                surfaceVersion: walkthroughInputs.expectations.surfaceVersion,
                evaluationIdentity: walkthroughInputs.expectations.evaluationIdentity,
              },
              traversal: input.walkthroughReadiness.traversal,
              population: readinessPopulation(projectShape),
            }),
          };
  const capabilityId = seeds === undefined ? 'capability:unknown' : capabilityIdFromSeeds(seeds);
  const proposedWork =
    seeds === undefined || seedArtifacts === undefined
      ? emptyProposedWork(input)
      : deriveProposedWork({
          capabilityId,
          proposal: {
            path: seedArtifacts.proposal.path,
            revision: input.repositoryRevision,
            digest: `sha256:${seedArtifacts.proposal.digest}`,
          },
          delta: {
            path: seedArtifacts.requirement.path,
            revision: input.repositoryRevision,
            digest: `sha256:${seedArtifacts.requirement.digest}`,
          },
          codeStructure,
          projectShape,
        });
  const snapshotLabel = snapshotLabelFor(input, seeds);

  return {
    schema: 'syzygy-three-surface-poc/v1',
    evaluation: {
      snapshot: `${snapshotLabel}|inputs:sha256:${inputDigest}`,
      snapshotLabel,
      inputsDigest: inputDigest,
      asOf: input.evaluation.asOf,
    },
    project: {
      name: seeds?.project.displayName ?? 'Unknown project',
      root: repoRoot,
      revision: input.repositoryRevision,
    },
    observerRevision: input.observerRevision,
    capabilityId,
    entities,
    relationships,
    codeStructure,
    workItems,
    workerChange,
    testArtifactVerification,
    orrery: orreryProjection,
    trajectory: trajectoryProjection,
    materializedBeadId: materialization.beadId,
    projectShape,
    proposedWork,
    walkthroughJudgment,
    walkthroughReadiness,
    surfaces:
      seeds === undefined
        ? []
        : seeds.surfaces.map((surface) =>
            surface.id === 'orrery'
              ? {
                  ...surface,
                  entityIds: entities.map((entity) => entity.id),
                  relationshipIds: relationships.map((relationship) => relationship.id),
                }
              : surface,
          ),
  };
}
