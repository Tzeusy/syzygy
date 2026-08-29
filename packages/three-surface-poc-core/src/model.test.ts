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
      '# Repair WhatsApp identity reconciliation\nowner-approved-intent-marker\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md':
      '# switchboard identity\nREQ-switchboard-identity-001\n',
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
});
