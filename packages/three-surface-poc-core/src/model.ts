export type PocEpistemic =
  | { readonly label: 'Observed'; readonly basis: string }
  | { readonly label: 'Unknown'; readonly reason: string };

export interface PocProvenance {
  readonly kind: 'repository-file' | 'git-revision' | 'manual-mapping';
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
  readonly evaluation: { readonly snapshot: string; readonly asOf: string };
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
}

export interface BuildButlersPocModelInput {
  readonly repoRoot: string;
  readonly repositoryRevision: string;
  readonly observerRevision: string;
  readonly evaluation: { readonly snapshot: string; readonly asOf: string };
}

export class PocObservationError extends Error {
  constructor(
    readonly kind:
      | 'required-artifact-missing'
      | 'required-artifact-unreadable',
    readonly artifactPath?: string,
  ) {
    super(artifactPath === undefined ? kind : `${kind}: ${artifactPath}`);
    this.name = 'PocObservationError';
  }
}

const ARTIFACT_PATHS = {
  design: 'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md',
  proposal: 'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md',
  requirement:
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md',
  code: 'src/butlers/identity.py',
  test: 'tests/core/test_identity.py',
} as const;

interface ObservedArtifact {
  readonly path: string;
  readonly digest: string;
}

function sha256(bytes: Uint8Array | string): string {
  return createHash('sha256').update(bytes).digest('hex');
}

function observeArtifact(repoRoot: string, artifactPath: string): ObservedArtifact {
  const absolutePath = resolve(repoRoot, artifactPath);
  try {
    if (!statSync(absolutePath).isFile()) {
      throw new PocObservationError('required-artifact-unreadable', artifactPath);
    }
    return { path: artifactPath, digest: sha256(readFileSync(absolutePath)) };
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

export function buildButlersPocModel(input: BuildButlersPocModelInput): PocModel {
  const repoRoot = resolve(input.repoRoot);
  const design = observeArtifact(repoRoot, ARTIFACT_PATHS.design);
  const proposal = observeArtifact(repoRoot, ARTIFACT_PATHS.proposal);
  const requirement = observeArtifact(repoRoot, ARTIFACT_PATHS.requirement);
  const code = observeArtifact(repoRoot, ARTIFACT_PATHS.code);
  const test = observeArtifact(repoRoot, ARTIFACT_PATHS.test);
  const mappingProvenance: PocProvenance = {
    kind: 'manual-mapping',
    source: 'packages/three-surface-poc-core/src/model.ts#ARTIFACT_PATHS',
    revision: input.observerRevision,
    digest: `sha256:${sha256(JSON.stringify(ARTIFACT_PATHS))}`,
  };
  const gitProvenance: PocProvenance = {
    kind: 'git-revision',
    source: 'Butlers repository',
    revision: input.repositoryRevision,
  };

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
      epistemic: observed('The selected capability is named by the approved intent artifact.'),
      provenance: [
        fileProvenance(design, input.repositoryRevision),
        fileProvenance(requirement, input.repositoryRevision),
      ],
    },
    {
      id: 'intent:req-switchboard-identity-001',
      kind: 'intent',
      title: 'REQ-switchboard-identity-001',
      detail: 'The active approved intent revision selected for this POC.',
      epistemic: observed('The selected intent artifacts were read and hashed.'),
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
      detail: ARTIFACT_PATHS.code,
      epistemic: observed('The manually mapped code file exists at the observed revision.'),
      provenance: [fileProvenance(code, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'test:identity-regression-definition',
      kind: 'test-definition',
      title: 'Identity regression test definition',
      detail: ARTIFACT_PATHS.test,
      epistemic: observed('The manually mapped test file exists at the observed revision.'),
      provenance: [fileProvenance(test, input.repositoryRevision), mappingProvenance],
    },
    {
      id: 'work:whatsapp-single-event-normalization',
      kind: 'work-item',
      title: 'Single-event sender normalization work',
      detail: 'Planned demonstration work has not been materialized.',
      epistemic: unknown('No POC work item has been materialized.'),
      provenance: [],
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
      epistemic: unknown('The human-triggered materialization step has not run.'),
      provenance: [],
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

  return {
    schema: 'syzygy-three-surface-poc/v1',
    evaluation: input.evaluation,
    project: { name: 'Butlers', root: repoRoot, revision: input.repositoryRevision },
    observerRevision: input.observerRevision,
    capabilityId: 'capability:whatsapp-transport-identity',
    entities,
    relationships,
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
import { createHash } from 'node:crypto';
import { readFileSync, statSync } from 'node:fs';
import { resolve } from 'node:path';
