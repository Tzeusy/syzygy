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
});
