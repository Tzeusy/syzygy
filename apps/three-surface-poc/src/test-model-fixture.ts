import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';

import { buildButlersPocModel, type PocModel, type ProjectShapeModelInput } from '@syzygy/three-surface-poc-core';

function git(root: string, args: readonly string[]): string {
  return execFileSync('git', ['-C', root, ...args], {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'ignore'],
  }).trim();
}

export interface FixtureRepo {
  readonly repoRoot: string;
  readonly revision: string;
}

/**
 * A committed fixture repository carrying the five artifacts the intent
 * graph requires, plus enough extra tree shape for code-structure and
 * work-item projections to have something real to group.
 */
export function fixtureRepoWithGit(cleanups: string[]): FixtureRepo {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-poc-surface-fixture-'));
  cleanups.push(root);
  const files: Readonly<Record<string, string>> = {
    'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md':
      '# design\nStatus: Approved for implementation\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md':
      '# proposal\n- Sign-off: owner approved the design and end-to-end implementation on 2026-08-24.\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md':
      '# REQ-switchboard-identity-001\nwhatsapp_user_client -> whatsapp_jid\n',
    'src/butlers/identity.py': 'def canonical_identity(): pass\n',
    'tests/core/test_identity.py': 'def test_identity(): pass\n',
    'apps/other/thing.ts': 'export const x = 1;\n',
    'apps/other/thing2.py': 'x = 1\n',
    'README.md': '# fixture repo\n',
  };
  for (const [relativePath, contents] of Object.entries(files)) {
    const absolutePath = join(root, relativePath);
    mkdirSync(dirname(absolutePath), { recursive: true });
    writeFileSync(absolutePath, contents, 'utf8');
  }
  git(root, ['init', '-q']);
  git(root, ['config', 'user.email', 'poc-test@example.invalid']);
  git(root, ['config', 'user.name', 'POC Test']);
  git(root, ['add', '-A']);
  git(root, ['commit', '-qm', 'fixture']);
  return { repoRoot: root, revision: git(root, ['rev-parse', 'HEAD']) };
}

function workItemRow(
  id: string,
  status: string,
  createdAt: string,
  updatedAt: string,
  closedAt: string | null,
  revision: string,
): Record<string, unknown> {
  return {
    revision,
    id,
    title: `fixture item ${id}`,
    status,
    issue_type: 'task',
    priority: 1,
    created_at: createdAt,
    updated_at: updatedAt,
    closed_at: closedAt,
  };
}

/** Builds one shared model with real, observed code-structure and
 * work-item regions, using an injected work-item query so the fixture
 * needs no live Dolt server. */
export interface FixtureModelOptions {
  /** Supplied → the model's `projectShape` is built through the P1 gate and
   * the injected runner; absent → `not-evaluated`, as the pre-PWB fixture. */
  readonly projectShape?: ProjectShapeModelInput;
}

export function buildFixtureModel(cleanups: string[], options: FixtureModelOptions = {}): PocModel {
  const { repoRoot, revision } = fixtureRepoWithGit(cleanups);
  const doltRevision = 'dolt-fixture-revision';
  const rows = [
    workItemRow('bu-open1', 'open', '2026-08-01T00:00:00Z', '2026-08-02T00:00:00Z', null, doltRevision),
    workItemRow(
      'bu-progress1',
      'in_progress',
      '2026-08-03T00:00:00Z',
      '2026-08-04T00:00:00Z',
      null,
      doltRevision,
    ),
    workItemRow(
      'bu-blocked1',
      'blocked',
      '2026-08-05T00:00:00Z',
      '2026-08-05T12:00:00Z',
      null,
      doltRevision,
    ),
    workItemRow(
      'bu-closed-recent',
      'closed',
      '2026-08-06T00:00:00Z',
      '2026-08-07T00:00:00Z',
      '2026-08-07T00:00:00Z',
      doltRevision,
    ),
    workItemRow(
      'bu-closed-old',
      'closed',
      '2026-07-01T00:00:00Z',
      '2026-07-02T00:00:00Z',
      '2026-07-02T00:00:00Z',
      doltRevision,
    ),
  ];

  return buildButlersPocModel({
    repoRoot,
    repositoryRevision: revision,
    observerRevision: revision,
    evaluation: { snapshot: 'butlers@fixture', asOf: '2026-08-30T12:00:00Z' },
    runWorkItemQuery: (_repoRoot, sql) =>
      sql.includes('WHERE id LIKE') ? JSON.stringify(rows) : JSON.stringify([{ revision: doltRevision }]),
    ...(options.projectShape === undefined ? {} : { projectShape: options.projectShape }),
  });
}
