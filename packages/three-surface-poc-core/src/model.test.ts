import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  buildButlersPocModel,
  PocObservationError,
  type PocEntity,
  type PocRelationship,
} from './model.js';
import type { TestArtifactRecord } from './test-artifact-verification.js';

const cleanups: string[] = [];

afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function butlersFixture(): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-poc-butlers-'));
  cleanups.push(root);
  const files: Readonly<Record<string, string>> = {
    'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md':
      '# WhatsApp identity design\nStatus: Approved for implementation\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md':
      '# Repair WhatsApp identity reconciliation\n- Sign-off: owner approved the design and end-to-end implementation on 2026-08-24.\nowner-approved-intent-marker\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md':
      '# switchboard identity\nREQ-switchboard-identity-001\nwhatsapp_user_client -> whatsapp_jid\n',
    'src/butlers/identity.py': 'def canonical_identity():\n    return "private-source-marker"\n',
    'tests/core/test_identity.py': 'def test_identity():\n    assert "private-test-marker"\n',
  };
  for (const [relativePath, contents] of Object.entries(files)) {
    const absolutePath = join(root, relativePath);
    mkdirSync(dirname(absolutePath), { recursive: true });
    writeFileSync(absolutePath, contents, 'utf8');
  }
  return root;
}

function byId<T extends PocEntity | PocRelationship>(items: readonly T[]): Map<string, T> {
  return new Map(items.map((item) => [item.id, item]));
}

function git(root: string, args: readonly string[]): string {
  return execFileSync('git', ['-C', root, ...args], {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'ignore'],
  }).trim();
}

const WORKER_CHANGE_SOURCE_PATH = 'src/butlers/connectors/whatsapp_user_client.py';
const WORKER_CHANGE_TEST_PATH = 'tests/connectors/test_whatsapp_user_client.py';

/** The same five required artifacts as {@link butlersFixture}, but as a
 * real committed git repository with a simulated fetched `origin/main`,
 * plus the bounded worker-change seam files — everything the test-artifact
 * verification wiring needs to observe a real changed-or-merged commit. */
function butlersGitFixture(): {
  readonly repoRoot: string;
  readonly changedCommit: string;
  readonly changedCommitAuthoredAt: string;
} {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-poc-butlers-git-'));
  cleanups.push(root);
  const files: Readonly<Record<string, string>> = {
    'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md':
      '# WhatsApp identity design\nStatus: Approved for implementation\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md':
      '# Repair WhatsApp identity reconciliation\n- Sign-off: owner approved the design and end-to-end implementation on 2026-08-24.\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md':
      '# switchboard identity\nREQ-switchboard-identity-001\nwhatsapp_user_client -> whatsapp_jid\n',
    'src/butlers/identity.py': 'def canonical_identity():\n    return "id"\n',
    'tests/core/test_identity.py': 'def test_identity():\n    assert True\n',
    [WORKER_CHANGE_SOURCE_PATH]: 'x = 1\n',
    [WORKER_CHANGE_TEST_PATH]: 'def test_normalization(): pass\n',
  };
  for (const [relativePath, contents] of Object.entries(files)) {
    const absolutePath = join(root, relativePath);
    mkdirSync(dirname(absolutePath), { recursive: true });
    writeFileSync(absolutePath, contents, 'utf8');
  }
  git(root, ['init', '-q', '-b', 'main']);
  git(root, ['config', 'user.email', 'poc-test@example.invalid']);
  git(root, ['config', 'user.name', 'POC Test']);
  git(root, ['add', '-A']);
  git(root, ['commit', '-qm', 'base']);
  writeFileSync(join(root, WORKER_CHANGE_SOURCE_PATH), 'x = 2\n', 'utf8');
  git(root, ['add', '-A']);
  git(root, ['commit', '-qm', 'fix(whatsapp): normalize single-event sender [bu-artifact-1]']);
  const changedCommit = git(root, ['rev-parse', 'HEAD']);
  const changedCommitAuthoredAt = git(root, ['log', '-1', '--format=%aI', changedCommit]);
  git(root, ['update-ref', 'refs/remotes/origin/main', changedCommit]);
  git(root, ['symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main']);
  return { repoRoot: root, changedCommit, changedCommitAuthoredAt };
}

const WORK_ITEM_ROWS = [
  {
    revision: 'dolt-rev-artifact',
    id: 'bu-artifact-1',
    title: 'Materialized work item',
    status: 'in_progress',
    issue_type: 'task',
    priority: 2,
    created_at: '2026-08-30T00:00:00Z',
    updated_at: '2026-08-30T00:00:00Z',
    closed_at: null,
  },
];

function runWorkItemQueryFixture(_repoRoot: string, sql: string): string {
  return sql.includes('WHERE id LIKE')
    ? JSON.stringify(WORK_ITEM_ROWS)
    : JSON.stringify([{ revision: 'dolt-rev-artifact' }]);
}

const MATERIALIZATION_RECORD_FIXTURE = {
  beadId: 'bu-artifact-1',
  externalRef: 'syzygy-poc:work:whatsapp-single-event-normalization',
  targetRepoRoot: '',
  createdAt: '2026-08-30T00:00:00Z',
  doltRevisionAtCreation: 'dolt-rev-artifact',
  attribution: 'test-actor',
} as const;

function passingTestArtifactRecord(
  commit: string,
  capturedAt: string,
  overrides: Partial<TestArtifactRecord> = {},
): TestArtifactRecord {
  return {
    command: ['python3', '-m', 'pytest', WORKER_CHANGE_TEST_PATH, '-q'],
    exitCode: 0,
    capturedAt,
    repositoryCommit: commit,
    scope: WORKER_CHANGE_TEST_PATH,
    digest: 'sha256:' + '1'.repeat(64),
    summary: '3 passed, 0 failed, 0 errored, 0 skipped in 0.42s',
    ...overrides,
  };
}

describe('three-surface Butlers POC model', () => {
  it('builds one deterministic provenance-backed graph with honest Unknowns', () => {
    const repoRoot = butlersFixture();
    const input = {
      repoRoot,
      repositoryRevision: 'c13894238989d3bebb24094730992970b31fe546',
      observerRevision: 'bfdb7963e4ff5628d0d1ec0f59e831d7e8209abe',
      evaluation: {
        snapshot: 'butlers@c1389423',
        asOf: '2026-08-29T12:00:00Z',
      },
    } as const;

    const first = buildButlersPocModel(input);
    const second = buildButlersPocModel(input);

    expect(second).toEqual(first);
    expect(first.evaluation.snapshot).toMatch(
      /^butlers@c1389423\|inputs:sha256:[0-9a-f]{64}$/,
    );
    expect(first.project.name).toBe('Butlers');
    expect(first.capabilityId).toBe('capability:whatsapp-transport-identity');
    expect(first.surfaces.map((surface) => surface.id)).toEqual([
      'polaris',
      'trajectory',
      'orrery',
    ]);

    const entities = byId(first.entities);
    expect(entities.get('intent:req-switchboard-identity-001')?.epistemic.label).toBe(
      'Observed',
    );
    expect(
      entities
        .get('intent:req-switchboard-identity-001')
        ?.provenance.map((provenance) => provenance.source),
    ).toEqual([
      'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md',
      'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md',
      'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md',
    ]);
    expect(entities.get('work:whatsapp-single-event-normalization')?.epistemic).toEqual({
      label: 'Unknown',
      reason: 'No POC work item has been materialized.',
    });
    expect(entities.get('evidence:focused-pytest')?.epistemic).toEqual({
      label: 'Unknown',
      reason: 'No test artifact has been captured for this evaluation.',
    });
    expect(entities.get('runtime:live-satisfaction')?.epistemic).toEqual({
      label: 'Unknown',
      reason: 'No current runtime observation was supplied.',
    });
    expect(entities.get('region:unmapped-code')?.epistemic.label).toBe('Unknown');

    const relationships = byId(first.relationships);
    expect(relationships.get('relationship:intent-to-work')?.epistemic.label).toBe('Unknown');
    expect(relationships.get('relationship:code-to-evidence')?.epistemic.label).toBe(
      'Unknown',
    );
    expect(relationships.get('relationship:code-to-runtime')?.epistemic.label).toBe(
      'Unknown',
    );

    const positiveClaims = [...first.entities, ...first.relationships].filter(
      (item) => item.epistemic.label === 'Observed',
    );
    expect(positiveClaims.length).toBeGreaterThan(0);
    expect(positiveClaims.every((item) => item.provenance.length > 0)).toBe(true);

    const serialized = JSON.stringify(first);
    expect(serialized).not.toContain('private-source-marker');
    expect(serialized).not.toContain('private-test-marker');
    expect(serialized).not.toContain('owner-approved-intent-marker');

    writeFileSync(
      join(repoRoot, 'src/butlers/identity.py'),
      'def canonical_identity():\n    return "changed-working-tree-bytes"\n',
      'utf8',
    );
    const changedBytes = buildButlersPocModel(input);
    expect(changedBytes.evaluation.snapshot).not.toBe(first.evaluation.snapshot);
  });

  it('shows the materialized work item Observed only once the recorded Bead is confirmed present (AC4)', () => {
    const repoRoot = butlersFixture();
    const baseInput = {
      repoRoot,
      repositoryRevision: 'c13894238989d3bebb24094730992970b31fe546',
      observerRevision: 'bfdb7963e4ff5628d0d1ec0f59e831d7e8209abe',
      evaluation: { snapshot: 'butlers@c1389423', asOf: '2026-08-29T12:00:00Z' },
    } as const;
    const materializationRecord = {
      beadId: 'bu-materialized1',
      externalRef: 'syzygy-poc:work:whatsapp-single-event-normalization',
      targetRepoRoot: repoRoot,
      createdAt: '2026-08-30T00:00:00Z',
      doltRevisionAtCreation: 'dolt-rev-1',
      attribution: 'test-actor',
    } as const;

    const confirmedRows = [
      {
        revision: 'dolt-rev-2',
        id: 'bu-materialized1',
        title: 'Single-event WhatsApp sender normalization (Syzygy POC materialization)',
        status: 'open',
        issue_type: 'task',
        priority: 2,
        created_at: '2026-08-30T00:00:00Z',
        updated_at: '2026-08-30T00:00:00Z',
        closed_at: null,
      },
    ];

    const confirmed = buildButlersPocModel({
      ...baseInput,
      materializationRecord,
      runWorkItemQuery: (_repoRoot, sql) =>
        sql.includes('WHERE id LIKE') ? JSON.stringify(confirmedRows) : JSON.stringify([{ revision: 'dolt-rev-2' }]),
    });
    const confirmedEntities = byId(confirmed.entities);
    expect(confirmedEntities.get('work:whatsapp-single-event-normalization')?.epistemic.label).toBe(
      'Observed',
    );
    expect(
      confirmedEntities.get('work:whatsapp-single-event-normalization')?.detail,
    ).toContain('bu-materialized1');
    expect(
      confirmedEntities.get('work:whatsapp-single-event-normalization')?.provenance,
    ).toHaveLength(1);
    const confirmedRelationships = byId(confirmed.relationships);
    expect(confirmedRelationships.get('relationship:intent-to-work')?.epistemic.label).toBe(
      'Observed',
    );
    // the untouched follow-on relationship stays Unknown — this bead
    // materializes the Bead, not a code/test change
    expect(confirmedRelationships.get('relationship:work-to-code')?.epistemic.label).toBe(
      'Unknown',
    );

    // a record naming a Bead that is NOT present in the live-observed
    // work items must never be rendered as Observed (VIS-2, fail-closed)
    const stale = buildButlersPocModel({
      ...baseInput,
      materializationRecord,
      runWorkItemQuery: (_repoRoot, sql) => (sql.includes('WHERE id LIKE') ? JSON.stringify([]) : JSON.stringify([{ revision: 'dolt-rev-3' }])),
    });
    const staleEntities = byId(stale.entities);
    expect(staleEntities.get('work:whatsapp-single-event-normalization')?.epistemic.label).toBe(
      'Unknown',
    );

    // no record at all: unchanged from the pre-existing default behaviour
    const none = buildButlersPocModel(baseInput);
    const noneEntities = byId(none.entities);
    expect(noneEntities.get('work:whatsapp-single-event-normalization')?.epistemic).toEqual({
      label: 'Unknown',
      reason: 'No POC work item has been materialized.',
    });
  });

  it('fails closed when a required mapped artifact is absent', () => {
    const repoRoot = butlersFixture();
    rmSync(join(repoRoot, 'tests/core/test_identity.py'));

    expect(() =>
      buildButlersPocModel({
        repoRoot,
        repositoryRevision: 'c13894238989d3bebb24094730992970b31fe546',
        observerRevision: 'bfdb7963e4ff5628d0d1ec0f59e831d7e8209abe',
        evaluation: {
          snapshot: 'butlers@c1389423',
          asOf: '2026-08-29T12:00:00Z',
        },
      }),
    ).toThrowError(
      expect.objectContaining<Partial<PocObservationError>>({
        kind: 'required-artifact-missing',
        artifactPath: 'tests/core/test_identity.py',
      }),
    );
  });

  it('fails closed when the selected intent no longer carries its approval contract', () => {
    const mutations = [
      {
        path: 'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md',
        contents: '# WhatsApp identity design\nStatus: Draft\n',
      },
      {
        path: 'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md',
        contents: '# proposal without owner sign-off\n',
      },
      {
        path: 'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md',
        contents: '# unrelated requirement\n',
      },
    ] as const;

    for (const mutation of mutations) {
      const repoRoot = butlersFixture();
      writeFileSync(join(repoRoot, mutation.path), mutation.contents, 'utf8');
      expect(() =>
        buildButlersPocModel({
          repoRoot,
          repositoryRevision: 'c13894238989d3bebb24094730992970b31fe546',
          observerRevision: 'bfdb7963e4ff5628d0d1ec0f59e831d7e8209abe',
          evaluation: {
            snapshot: 'butlers@c1389423',
            asOf: '2026-08-29T12:00:00Z',
          },
        }),
      ).toThrowError(
        expect.objectContaining({
          kind: 'required-artifact-semantic-mismatch',
          artifactPath: mutation.path,
        }),
      );
    }
  });

  it('shows Verified only once a real, ingested test artifact binds to the observed changed commit (AC3, syzygy-0r9)', () => {
    const { repoRoot, changedCommit, changedCommitAuthoredAt } = butlersGitFixture();
    const capturedAt = new Date(Date.parse(changedCommitAuthoredAt) + 60 * 60 * 1000).toISOString();
    const evaluationAsOf = new Date(Date.parse(capturedAt) + 60 * 60 * 1000).toISOString();
    const baseInput = {
      repoRoot,
      repositoryRevision: changedCommit,
      observerRevision: changedCommit,
      evaluation: { snapshot: 'butlers@artifact', asOf: evaluationAsOf },
      materializationRecord: { ...MATERIALIZATION_RECORD_FIXTURE, targetRepoRoot: repoRoot },
      runWorkItemQuery: runWorkItemQueryFixture,
    } as const;

    const withoutArtifact = buildButlersPocModel(baseInput);
    expect(withoutArtifact.workerChange.kind).toBe('observed');
    if (withoutArtifact.workerChange.kind !== 'observed') throw new Error('unreachable');
    expect(withoutArtifact.workerChange.state).toBe('changed-or-merged');
    expect(withoutArtifact.testArtifactVerification.kind).toBe('unknown');

    // The identity-resolution entity graph (a different capability, a
    // different code file) must never be perturbed by this seam's
    // verification — it stays Unknown throughout this test regardless of
    // whether the worker-change seam's own evidence is verified.
    const identityEntities = byId(withoutArtifact.entities);
    expect(identityEntities.get('evidence:focused-pytest')?.epistemic.label).toBe('Unknown');

    const verified = buildButlersPocModel({
      ...baseInput,
      testArtifactRecord: passingTestArtifactRecord(changedCommit, capturedAt),
    });
    expect(verified.testArtifactVerification.kind).toBe('verified');
    if (verified.testArtifactVerification.kind !== 'verified') throw new Error('unreachable');
    expect(verified.testArtifactVerification.record.repositoryCommit).toBe(changedCommit);
    // still untouched — this is the honest boundary between the two
    // capabilities sharing this bounded POC model.
    expect(byId(verified.entities).get('evidence:focused-pytest')?.epistemic.label).toBe('Unknown');

    // The serialized model must never leak raw test body content — only
    // the safe numeric summary and commit (AC5).
    const serialized = JSON.stringify(verified);
    expect(serialized).not.toContain('Traceback');

    // Mismatch/failure case (AC4, AC6): a passing artifact bound to a
    // different commit must never render Verified.
    const mismatched = buildButlersPocModel({
      ...baseInput,
      testArtifactRecord: passingTestArtifactRecord('a-different-commit-entirely', capturedAt),
    });
    expect(mismatched.testArtifactVerification.kind).toBe('unknown');

    // A failing exit status must never be shown Verified even when the
    // commit and scope both match (AC4).
    const failed = buildButlersPocModel({
      ...baseInput,
      testArtifactRecord: passingTestArtifactRecord(changedCommit, capturedAt, { exitCode: 1 }),
    });
    expect(failed.testArtifactVerification.kind).toBe('unknown');
  });
});
