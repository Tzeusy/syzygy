import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';

export interface GitObservation {
  readonly revision: string;
  readonly worktreeMetadataDigest: string;
  readonly clean: boolean;
  readonly changedPaths: readonly string[];
}

function readGit(root: string, args: readonly string[]): string {
  return execFileSync('git', ['--no-optional-locks', '-C', root, ...args], {
    encoding: 'utf8',
    env: { ...process.env, GIT_OPTIONAL_LOCKS: '0' },
    stdio: ['ignore', 'pipe', 'ignore'],
  });
}

function nulSeparatedPaths(record: string): readonly string[] {
  return record.split('\0').filter((candidate) => candidate !== '');
}

export function observeGitRepository(root: string): GitObservation {
  const revision = readGit(root, ['rev-parse', 'HEAD']).trim();
  const worktreeRecord = readGit(root, [
    'status',
    '--porcelain=v1',
    '-z',
    '--untracked-files=all',
  ]);
  const changedPaths = [
    ...nulSeparatedPaths(
      readGit(root, ['diff', '--no-renames', '--name-only', '-z', 'HEAD', '--']),
    ),
    ...nulSeparatedPaths(
      readGit(root, ['ls-files', '--others', '--exclude-standard', '-z']),
    ),
  ];
  return {
    revision,
    worktreeMetadataDigest: `sha256:${createHash('sha256').update(worktreeRecord).digest('hex')}`,
    clean: worktreeRecord.length === 0,
    changedPaths: [...new Set(changedPaths)].sort(),
  };
}

export function pocObserverInputsAreClean(
  observation: Pick<GitObservation, 'changedPaths'>,
): boolean {
  const exactInputs = new Set(['package.json', 'package-lock.json', 'tsconfig.base.json']);
  const inputPrefixes = [
    'apps/three-surface-poc/',
    'packages/three-surface-poc-core/',
    'packages/cap1-daemon/',
    'packages/cap1-core/',
  ];
  return observation.changedPaths.every(
    (changedPath) =>
      !exactInputs.has(changedPath) &&
      inputPrefixes.every((prefix) => !changedPath.startsWith(prefix)),
  );
}
