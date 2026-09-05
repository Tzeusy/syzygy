import { createHash } from 'node:crypto';
import { readFileSync, statSync } from 'node:fs';
import { resolve } from 'node:path';

import { observeCodeStructure, type CodeStructureResult } from './code-structure.js';
import { observeWorkItems, type WorkItemsResult } from './work-items.js';
import { observeWorkerChange, type WorkerChangeResult, type WorkerChangeSeam } from './worker-change-observation.js';
import { projectOrrery, type OrreryProjection } from './orrery-projection.js';
import { projectTrajectory, type TrajectoryProjection } from './trajectory-projection.js';
import type { MaterializationRecord } from './materialization.js';
import type { BodyReadAuthorityEvaluation } from './body-read-authority.js';
import { gitRunnerFor, type GitRunner, type PwbResourceLimits } from './project-shape-observation.js';
import { buildProjectShape, unevaluatedProjectShape, type ProjectShape } from './project-shape-model.js';
import { deriveProposedWork, type ProposedWork } from './proposed-work.js';
import { evaluateWalkthroughJudgment, type WalkthroughJudgmentEvaluation, type WalkthroughJudgmentInputs } from './walkthrough-judgment.js';
import { evaluateWalkthroughReadiness, walkthroughEvaluationIdentity, type ReadinessPopulation, type ReadinessTraversal, type WalkthroughReadiness } from './walkthrough-readiness.js';
import {
  resolveTestArtifactVerification,
  type TestArtifactRecord,
  type TestArtifactVerificationResult,
} from './test-artifact-verification.js';

const RECENT_CLOSED_WINDOW = 50;
const BEAD_PREFIX = 'bu' as const;

// The bounded source seam an external Butlers worker fixes for the
// approved WhatsApp single-event sender-normalization gap — distinct
// from ARTIFACT_PATHS.code/test below, which map the broader identity
// capability this POC slice already renders on Polaris/Orrery.
const WORKER_CHANGE_SEAM: WorkerChangeSeam = {
  sourcePath: 'src/butlers/connectors/whatsapp_user_client.py',
  testPath: 'tests/connectors/test_whatsapp_user_client.py',
} as const;

// The intent this bounded seam's change and test evidence bind to, per
// syzygy-8e1's own governing-intent description — distinct from
// intent:req-switchboard-identity-001 below, which governs the separate
// capability:whatsapp-transport-identity code region. Exported so the
// Trajectory surface can name it on the one place this evidence is
// honestly scoped to: the worker-change badge, never the identity-
// resolution entity graph above.
export const WORKER_CHANGE_INTENT_ID = 'REQ-connector-base-spec-001' as const;

export type PocEpistemic =
  | { readonly label: 'Observed'; readonly basis: string }
  | { readonly label: 'Unknown'; readonly reason: string };

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
    readonly name: 'Butlers';
    readonly root: string;
    readonly revision: string;
  };
  readonly observerRevision: string;
  readonly capabilityId: 'capability:whatsapp-transport-identity';
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

export type WalkthroughJudgmentInputsFor = (binding: { readonly evaluationIdentity: string }) => WalkthroughJudgmentInputs;

export type WalkthroughReadinessPresentation =
  | { readonly kind: 'not-evaluated'; readonly detail: string }
  | { readonly kind: 'evaluated'; readonly readiness: WalkthroughReadiness };

export type WalkthroughJudgmentPresentation =
  | { readonly kind: 'not-evaluated'; readonly detail: string }
  | { readonly kind: 'evaluated'; readonly evaluation: WalkthroughJudgmentEvaluation };

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

export interface BuildButlersPocModelInput {
  readonly repoRoot: string;
  readonly repositoryRevision: string;
  readonly observerRevision: string;
  readonly evaluation: { readonly snapshot: string; readonly asOf: string };
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
    return { kind: 'unavailable', reason: `project shape ${projectShape.kind}: no same-evaluation source population` };
  }
  return {
    kind: 'observed',
    sources: projectShape.sources.map((source) => ({ path: source.path, admitted: source.record.outcome === 'classified' })),
    limitBreaches: projectShape.limitBreaches.length,
  };
}

export class PocObservationError extends Error {
  constructor(
    readonly kind:
      | 'required-artifact-missing'
      | 'required-artifact-semantic-mismatch'
      | 'required-artifact-unreadable',
    readonly artifactPath?: string,
  ) {
    super(artifactPath === undefined ? kind : `${kind}: ${artifactPath}`);
    this.name = 'PocObservationError';
  }
}

export const ARTIFACT_PATHS = {
  design: 'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md',
  proposal: 'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md',
  requirement:
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md',
  code: 'src/butlers/identity.py',
  test: 'tests/core/test_identity.py',
} as const;

const INTENT_MARKERS = {
  design: ['Approved for implementation'],
  proposal: ['owner approved the design and end-to-end implementation on 2026-08-24'],
  requirement: [
    'REQ-switchboard-identity-001',
    'whatsapp_user_client',
    'whatsapp_jid',
  ],
} as const;

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

function fileProvenance(
  artifact: ObservedArtifact,
  repositoryRevision: string,
): PocProvenance {
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
    return { epistemic: unknown('No POC work item has been materialized.'), beadId: null, origin: null, provenance: [] };
  }
  if (workItems.kind === 'unknown') {
    return {
      epistemic: unknown(
        'A materialization record exists but work items could not be observed to confirm it.',
      ),
      beadId: null,
      origin: null,
      provenance: [],
    };
  }
  const found = workItems.items.find((item) => item.id === record.beadId);
  if (found === undefined) {
    return {
      epistemic: unknown(
        'A materialization record names a Bead that was not found among the observed work items.',
      ),
      beadId: null,
      origin: null,
      provenance: [],
    };
  }
  return {
    epistemic: observed(
      `The materialized Bead ${found.id} was confirmed present in the observed work items.`,
    ),
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

export function buildButlersPocModel(input: BuildButlersPocModelInput): PocModel {
  const repoRoot = resolve(input.repoRoot);
  const design = observeArtifact(repoRoot, ARTIFACT_PATHS.design, INTENT_MARKERS.design);
  const proposal = observeArtifact(repoRoot, ARTIFACT_PATHS.proposal, INTENT_MARKERS.proposal);
  const requirement = observeArtifact(
    repoRoot,
    ARTIFACT_PATHS.requirement,
    INTENT_MARKERS.requirement,
  );
  const code = observeArtifact(repoRoot, ARTIFACT_PATHS.code);
  const test = observeArtifact(repoRoot, ARTIFACT_PATHS.test);
  const mappingDigest = sha256(JSON.stringify({ ARTIFACT_PATHS, INTENT_MARKERS }));
  const inputDigest = sha256(
    JSON.stringify({
      repoRoot,
      repositoryRevision: input.repositoryRevision,
      observerRevision: input.observerRevision,
      artifacts: [design, proposal, requirement, code, test],
      mappingDigest,
    }),
  );
  const mappingProvenance: PocProvenance = {
    kind: 'manual-mapping',
    source: 'packages/three-surface-poc-core/src/model.ts#ARTIFACT_PATHS',
    revision: input.observerRevision,
    digest: `sha256:${mappingDigest}`,
  };
  const gitProvenance: PocProvenance = {
    kind: 'git-revision',
    source: 'Butlers repository',
    revision: input.repositoryRevision,
  };

  const codeStructure = observeCodeStructure({
    repoRoot,
    revision: input.repositoryRevision,
    capturedAt: input.evaluation.asOf,
    ...(input.runGit === undefined ? {} : { runGit: input.runGit }),
  });
  const workItems = observeWorkItems({
    repoRoot,
    beadPrefix: BEAD_PREFIX,
    capturedAt: input.evaluation.asOf,
    ...(input.runWorkItemQuery === undefined ? {} : { runQuery: input.runWorkItemQuery }),
  });
  const materialization = resolveMaterializationEpistemic(
    input.materializationRecord ?? null,
    workItems,
  );
  const workerChange = observeWorkerChange({
    repoRoot,
    beadId: materialization.beadId,
    seam: WORKER_CHANGE_SEAM,
    capturedAt: input.evaluation.asOf,
    ...(input.runGit === undefined ? {} : { runGit: input.runGit }),
  });
  const observedChangeCommit =
    workerChange.kind === 'observed' && workerChange.state === 'changed-or-merged' && workerChange.commit !== null
      ? workerChange.commit.sha
      : null;
  const observedChangeCommitAuthoredAt =
    workerChange.kind === 'observed' && workerChange.commit !== null ? workerChange.commit.authoredAt : null;
  const testArtifactVerification = resolveTestArtifactVerification({
    record: input.testArtifactRecord ?? null,
    expectedScope: WORKER_CHANGE_SEAM.testPath,
    observedCommit: observedChangeCommit,
    commitAuthoredAt: observedChangeCommitAuthoredAt,
    evaluationAsOf: input.evaluation.asOf,
  });

  const entities: readonly PocEntity[] = [
    {
      id: 'project:butlers',
      kind: 'project',
      title: 'Butlers',
      detail: 'The one configured external proving project.',
      epistemic: observed('Git reported the configured repository revision.'),
      provenance: [gitProvenance],
    },
    {
      id: 'capability:whatsapp-transport-identity',
      kind: 'capability',
      title: 'WhatsApp transport identity normalization',
      detail:
        'Preserve transport metadata while resolving identity through canonical WhatsApp JIDs.',
      epistemic: observed('Validated intent markers name this capability and record approval.'),
      provenance: [
        fileProvenance(design, input.repositoryRevision),
        fileProvenance(requirement, input.repositoryRevision),
      ],
    },
    {
      id: 'intent:req-switchboard-identity-001',
      kind: 'intent',
      title: 'REQ-switchboard-identity-001',
      detail: 'The selected intent revision records owner approval for implementation.',
      epistemic: observed('Required approval, identifier, and relationship markers were validated.'),
      provenance: [
        fileProvenance(design, input.repositoryRevision),
        fileProvenance(proposal, input.repositoryRevision),
        fileProvenance(requirement, input.repositoryRevision),
      ],
    },
    {
      id: 'code:identity-resolution',
      kind: 'code-region',
      title: 'Identity resolution code region',
      detail: `The manually mapped code file at ${ARTIFACT_PATHS.code} implements sender-identity resolution.`,
      epistemic: observed('The manually mapped code file was captured and hashed.'),
      provenance: [fileProvenance(code, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'test:identity-regression-definition',
      kind: 'test-definition',
      title: 'Identity regression test definition',
      detail: `The manually mapped test file at ${ARTIFACT_PATHS.test} defines the identity regression check.`,
      epistemic: observed('The manually mapped test file was captured and hashed.'),
      provenance: [fileProvenance(test, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'work:whatsapp-single-event-normalization',
      kind: 'work-item',
      title: 'Single-event sender normalization work',
      detail:
        materialization.beadId === null
          ? 'Planned demonstration work has not been materialized.'
          : `Materialized as Beads item ${materialization.beadId}.`,
      epistemic: materialization.epistemic,
      provenance: materialization.provenance,
    },
    {
      id: 'evidence:focused-pytest',
      kind: 'test-evidence',
      title: 'Focused pytest evidence',
      detail: 'A test definition is not a captured test run.',
      epistemic: unknown('No test artifact has been captured for this evaluation.'),
      provenance: [],
    },
    {
      id: 'runtime:live-satisfaction',
      kind: 'runtime',
      title: 'Live runtime satisfaction',
      detail: 'Repository state does not establish deployment or runtime health.',
      epistemic: unknown('No current runtime observation was supplied.'),
      provenance: [],
    },
    {
      id: 'region:unmapped-code',
      kind: 'unknown-region',
      title: 'Unmapped Butlers code',
      detail: 'Everything outside the two manually mapped files is outside this slice.',
      epistemic: unknown('The first slice does not enumerate or map the remaining code.'),
      provenance: [],
    },
  ];

  const relationships: readonly PocRelationship[] = [
    {
      id: 'relationship:project-to-capability',
      kind: 'contains',
      from: 'project:butlers',
      to: 'capability:whatsapp-transport-identity',
      statement: 'Butlers declares the selected capability.',
      epistemic: observed('The selected requirement is present in the configured repository.'),
      provenance: [fileProvenance(requirement, input.repositoryRevision)],
    },
    {
      id: 'relationship:capability-to-intent',
      kind: 'governed-by',
      from: 'capability:whatsapp-transport-identity',
      to: 'intent:req-switchboard-identity-001',
      statement: 'The capability is governed by the selected intent revision.',
      epistemic: observed('The relationship is declared by the bounded POC mapping.'),
      provenance: [fileProvenance(requirement, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'relationship:capability-to-code',
      kind: 'mapped-to',
      from: 'capability:whatsapp-transport-identity',
      to: 'code:identity-resolution',
      statement: 'The POC manually maps the capability to this code region.',
      epistemic: observed('The mapping and mapped file are both identified.'),
      provenance: [fileProvenance(code, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'relationship:capability-to-test-definition',
      kind: 'mapped-to',
      from: 'capability:whatsapp-transport-identity',
      to: 'test:identity-regression-definition',
      statement: 'The POC manually maps the capability to this test definition.',
      epistemic: observed('The mapping and mapped file are both identified.'),
      provenance: [fileProvenance(test, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'relationship:intent-to-work',
      kind: 'materializes-as',
      from: 'intent:req-switchboard-identity-001',
      to: 'work:whatsapp-single-event-normalization',
      statement: 'Approved intent materializes as a work item.',
      epistemic:
        materialization.beadId === null
          ? unknown('The human-triggered materialization step has not run.')
          : observed(
              `The human-triggered materialization step ${
                materialization.origin === 'created'
                  ? 'created'
                  : materialization.origin === 'reused'
                    ? 'reused the existing'
                    : 'created or reused'
              } Beads item ${materialization.beadId}.`,
            ),
      provenance: materialization.provenance,
    },
    {
      id: 'relationship:work-to-code',
      kind: 'changes',
      from: 'work:whatsapp-single-event-normalization',
      to: 'code:identity-resolution',
      statement: 'The work item changes the mapped code region.',
      epistemic: unknown('No materialized work item or worker change was supplied.'),
      provenance: [],
    },
    {
      id: 'relationship:code-to-evidence',
      kind: 'verified-by',
      from: 'code:identity-resolution',
      to: 'evidence:focused-pytest',
      statement: 'A captured test artifact verifies the code against intent.',
      epistemic: unknown('No test artifact has been captured for this evaluation.'),
      provenance: [],
    },
    {
      id: 'relationship:code-to-runtime',
      kind: 'satisfies-at-runtime',
      from: 'code:identity-resolution',
      to: 'runtime:live-satisfaction',
      statement: 'The mapped code satisfies the intent in the live runtime.',
      epistemic: unknown('No current runtime observation was supplied.'),
      provenance: [],
    },
    {
      id: 'relationship:capability-to-unmapped-region',
      kind: 'coverage-unknown',
      from: 'capability:whatsapp-transport-identity',
      to: 'region:unmapped-code',
      statement: 'Other code may relate to this capability.',
      epistemic: unknown('The bounded POC mapping makes no claim about other code.'),
      provenance: [],
    },
  ];

  const orreryProjection = projectOrrery(codeStructure, [
    {
      id: 'code:identity-resolution',
      path: ARTIFACT_PATHS.code,
      capabilityId: 'capability:whatsapp-transport-identity',
    },
  ]);
  const trajectoryProjection = projectTrajectory(workItems, {
    recentClosedWindow: RECENT_CLOSED_WINDOW,
  });
  const projectShape: ProjectShape =
    input.projectShape === undefined
      ? unevaluatedProjectShape(input.projectShapeDetail ?? 'No body-read authority evaluation was supplied to this evaluation; no project-shape source was read.')
      : buildProjectShape({
          authority: input.projectShape.authority,
          revision: input.repositoryRevision,
          capturedAt: input.evaluation.asOf,
          runGit: input.projectShape.runGit ?? gitRunnerFor(repoRoot),
          ...(input.projectShape.repositoryId === undefined ? {} : { repositoryId: input.projectShape.repositoryId }),
          ...(input.projectShape.resourceLimits === undefined ? {} : { resourceLimits: input.projectShape.resourceLimits }),
        });
  // The pair's expectations bind to the exact evaluation this build
  // observed; a loader that fails leaves both states `not-evaluated`.
  let walkthroughInputs: WalkthroughJudgmentInputs | undefined;
  let walkthroughDetail = input.walkthroughJudgmentDetail;
  if (typeof input.walkthroughJudgment === 'function') {
    try {
      walkthroughInputs = input.walkthroughJudgment({ evaluationIdentity: walkthroughEvaluationIdentity(projectShape) });
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
          detail: walkthroughDetail ?? 'No cold-open walkthrough run record and judgment pair was supplied to this evaluation; no judgment was evaluated.',
        }
      : { kind: 'evaluated', evaluation: evaluateWalkthroughJudgment(walkthroughInputs) };
  const walkthroughReadiness: WalkthroughReadinessPresentation =
    walkthroughInputs === undefined
      ? { kind: 'not-evaluated', detail: walkthroughDetail ?? 'No cold-open walkthrough run record was supplied to this evaluation; no answer population was assessed.' }
      : input.walkthroughReadiness === undefined
        ? { kind: 'not-evaluated', detail: 'No Polaris traversal predicate was supplied to this evaluation; readiness cannot tell Polaris routes from others.' }
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
  const proposedWork = deriveProposedWork({
    capabilityId: 'capability:whatsapp-transport-identity',
    proposal: { path: proposal.path, revision: input.repositoryRevision, digest: `sha256:${proposal.digest}` },
    delta: { path: requirement.path, revision: input.repositoryRevision, digest: `sha256:${requirement.digest}` },
    codeStructure,
    projectShape,
  });

  return {
    schema: 'syzygy-three-surface-poc/v1',
    evaluation: {
      snapshot: `${input.evaluation.snapshot}|inputs:sha256:${inputDigest}`,
      snapshotLabel: input.evaluation.snapshot,
      inputsDigest: inputDigest,
      asOf: input.evaluation.asOf,
    },
    project: { name: 'Butlers', root: repoRoot, revision: input.repositoryRevision },
    observerRevision: input.observerRevision,
    capabilityId: 'capability:whatsapp-transport-identity',
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
    surfaces: [
      {
        id: 'polaris',
        title: 'Polaris',
        question: 'What is this capability supposed to be?',
        entityIds: [
          'project:butlers',
          'capability:whatsapp-transport-identity',
          'intent:req-switchboard-identity-001',
          'runtime:live-satisfaction',
        ],
        relationshipIds: [
          'relationship:project-to-capability',
          'relationship:capability-to-intent',
          'relationship:code-to-runtime',
        ],
      },
      {
        id: 'trajectory',
        title: 'Trajectory',
        question: 'What work and verification exist?',
        entityIds: [
          'intent:req-switchboard-identity-001',
          'work:whatsapp-single-event-normalization',
          'code:identity-resolution',
          'evidence:focused-pytest',
        ],
        relationshipIds: [
          'relationship:intent-to-work',
          'relationship:work-to-code',
          'relationship:code-to-evidence',
        ],
      },
      {
        id: 'orrery',
        title: 'Orrery',
        question: 'Where do intent, work, code, tests, and Unknown regions live?',
        entityIds: entities.map((entity) => entity.id),
        relationshipIds: relationships.map((relationship) => relationship.id),
      },
    ],
  };
}
