import { execFileSync } from 'node:child_process';
import {
  mkdirSync,
  mkdtempSync,
  readFileSync,
  renameSync,
  rmSync,
  statSync,
  writeFileSync,
} from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, describe, expect, it } from 'vitest';

import {
  observeGitRepository,
  PWB_APPROVED_REPOSITORY_LOCATOR,
  pocObserverInputsAreClean,
  resolvePwbRepositoryBinding,
} from './git-observation.js';

const cleanups: string[] = [];
const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));

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

function repositoryWithFile(relativePath: string): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-poc-git-'));
  cleanups.push(root);
  const absolutePath = join(root, relativePath);
  mkdirSync(dirname(absolutePath), { recursive: true });
  writeFileSync(absolutePath, 'export const value = 1;\n', 'utf8');
  git(root, ['init', '-q']);
  git(root, ['config', 'user.email', 'poc-test@example.invalid']);
  git(root, ['config', 'user.name', 'POC Test']);
  git(root, ['add', relativePath]);
  git(root, ['commit', '-qm', 'fixture']);
  return root;
}

describe('read-only Git observation', () => {
  it('binds only the approved resolved locator and its exact Git common directory', () => {
    const result = resolvePwbRepositoryBinding('/configured/butlers-link', {
      approvedLocator: '/approved/butlers',
      realpath: (path) => path === '/configured/butlers-link' ? '/approved/butlers' : path,
      runGit: () => '/approved/butlers/.git\n',
    });
    expect(result).toEqual({ kind: 'bound', locator: '/approved/butlers', gitCommonDirectory: '/approved/butlers/.git' });
  });

  it('keeps the approved locator byte-equal to the act-bound consent mapping', () => {
    const consent = readFileSync(join(REPO_ROOT, '.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md'), 'utf8');
    expect(consent).toContain(`Current locator: \`${PWB_APPROVED_REPOSITORY_LOCATOR}\` (configuration, not repository`);
  });

  it('rejects a second Butlers-shaped repository before any repository observation', () => {
    let gitCalls = 0;
    const result = resolvePwbRepositoryBinding('/other/butlers', {
      approvedLocator: '/approved/butlers',
      realpath: (path) => path,
      runGit: () => {
        gitCalls += 1;
        return '/other/butlers/.git\n';
      },
    });
    expect(result).toEqual({ kind: 'rejected', reason: 'locator-mismatched' });
    expect(gitCalls).toBe(0);
  });

  it('rejects a mismatched Git common directory', () => {
    const result = resolvePwbRepositoryBinding('/approved/butlers', {
      approvedLocator: '/approved/butlers',
      realpath: (path) => path,
      runGit: () => '/other/object-database\n',
    });
    expect(result).toEqual({ kind: 'rejected', reason: 'git-common-directory-mismatched' });
  });

  it('allows unrelated dirty files while protecting POC runtime inputs', () => {
    expect(pocObserverInputsAreClean({ changedPaths: ['.gitignore'] })).toBe(true);
    expect(
      pocObserverInputsAreClean({
        changedPaths: ['apps/three-surface-poc/src/main.ts'],
      }),
    ).toBe(false);
    expect(
      pocObserverInputsAreClean({
        changedPaths: ['packages/three-surface-poc-core/src/model.ts'],
      }),
    ).toBe(false);
    expect(
      pocObserverInputsAreClean({ changedPaths: ['packages/cap1-daemon/src/server.ts'] }),
    ).toBe(false);
    expect(pocObserverInputsAreClean({ changedPaths: ['package.json'] })).toBe(false);
  });

  it('identifies clean and dirty states without refreshing the index', () => {
    const root = repositoryWithFile('src/example.ts');

    const indexPath = join(root, '.git', 'index');
    const before = statSync(indexPath, { bigint: true }).mtimeNs;
    const clean = observeGitRepository(root);
    const afterClean = statSync(indexPath, { bigint: true }).mtimeNs;
    expect(clean.clean).toBe(true);
    expect(clean.changedPaths).toEqual([]);
    expect(clean.revision).toMatch(/^[0-9a-f]{40}$/);
    expect(clean.worktreeMetadataDigest).toMatch(/^sha256:[0-9a-f]{64}$/);
    expect(afterClean).toBe(before);

    writeFileSync(join(root, 'src', 'example.ts'), 'export const value = 2;\n', 'utf8');
    const dirty = observeGitRepository(root);
    const afterDirty = statSync(indexPath, { bigint: true }).mtimeNs;
    expect(dirty.clean).toBe(false);
    expect(dirty.changedPaths).toEqual(['src/example.ts']);
    expect(dirty.worktreeMetadataDigest).not.toBe(clean.worktreeMetadataDigest);
    expect(afterDirty).toBe(before);
  });

  it('retains a protected source path when it is renamed out', () => {
    const protectedPath = 'apps/three-surface-poc/src/main.ts';
    for (const staged of [true, false]) {
      const root = repositoryWithFile(protectedPath);
      mkdirSync(join(root, 'notes'), { recursive: true });
      if (staged) {
        git(root, ['mv', protectedPath, 'notes/main.ts']);
      } else {
        renameSync(join(root, protectedPath), join(root, 'notes/main.ts'));
      }

      const observation = observeGitRepository(root);
      expect(observation.changedPaths).toContain(protectedPath);
      expect(pocObserverInputsAreClean(observation)).toBe(false);
    }
  });
});
