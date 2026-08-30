import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { buildButlersPocModel } from './model.js';

const cleanups: string[] = [];

afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function git(root: string, args: readonly string[]): string {
  return execFileSync('git', ['-C', root, ...args], {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'ignore'],
  }).trim();
}

function butlersFixtureWithGit(): { repoRoot: string; revision: string } {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-poc-model-obs-'));
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

describe('shared model observation wiring', () => {
  it('folds code-structure and work-item observations into the one shared model', () => {
    const { repoRoot, revision } = butlersFixtureWithGit();
    const runWorkItemQuery = (_repoRoot: string, sql: string): string =>
      sql.includes('WHERE id LIKE')
        ? JSON.stringify([
            {
              revision: 'dolt-rev-fixture',
              id: 'bu-1',
              title: 'fixture item',
              status: 'open',
              issue_type: 'task',
              priority: 1,
              created_at: '2026-08-30T00:00:00Z',
              updated_at: '2026-08-30T00:00:00Z',
              closed_at: null,
            },
          ])
        : JSON.stringify([{ revision: 'dolt-rev-fixture' }]);

    const model = buildButlersPocModel({
      repoRoot,
      repositoryRevision: revision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@fixture', asOf: '2026-08-30T12:00:00Z' },
      runWorkItemQuery,
    });

    expect(model.codeStructure.kind).toBe('observed');
    if (model.codeStructure.kind !== 'observed') throw new Error('unreachable');
    expect(model.codeStructure.revision).toBe(revision);
    expect(model.codeStructure.files.some((file) => file.path === 'src/butlers/identity.py')).toBe(true);

    expect(model.workItems.kind).toBe('observed');
    if (model.workItems.kind !== 'observed') throw new Error('unreachable');
    expect(model.workItems.doltRevision).toBe('dolt-rev-fixture');
    expect(model.workItems.items).toHaveLength(1);

    expect(model.orrery.kind).toBe('observed');
    if (model.orrery.kind !== 'observed') throw new Error('unreachable');
    expect(model.orrery.mappedFileCount + model.orrery.unmappedFileCount).toBe(
      model.orrery.totalFileCount,
    );
    expect(model.orrery.mappedRegions.map((region) => region.id)).toContain(
      'code:identity-resolution',
    );

    expect(model.trajectory.kind).toBe('observed');
    if (model.trajectory.kind !== 'observed') throw new Error('unreachable');
    expect(model.trajectory.rendered.map((item) => item.id)).toContain('bu-1');

    // Full wire parity: the machine answer is exactly the model's own object
    // graph — no separate derivation path.
    expect(JSON.parse(JSON.stringify(model))).toEqual(model);
  });

  it('renders code-structure and work-item regions Unknown when their sources fail while the required intent artifacts remain present', () => {
    const { repoRoot, revision } = butlersFixtureWithGit();
    // Break git's ability to read the named revision without touching the
    // intent artifacts the earlier fail-closed checks require.
    const model = buildButlersPocModel({
      repoRoot,
      repositoryRevision: '0000000000000000000000000000000000dead',
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@unreadable-rev', asOf: '2026-08-30T12:00:00Z' },
      runWorkItemQuery: () => {
        throw new Error('connection refused');
      },
    });
    expect(model.codeStructure.kind).toBe('unknown');
    expect(model.workItems.kind).toBe('unknown');
    expect(model.orrery.kind).toBe('unknown');
    expect(model.trajectory.kind).toBe('unknown');
  });
});
