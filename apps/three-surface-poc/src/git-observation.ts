import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';

export interface GitObservation {
  readonly revision: string;
  readonly worktreeMetadataDigest: string;
  readonly clean: boolean;
}

function readGit(root: string, args: readonly string[]): string {
  return execFileSync('git', ['--no-optional-locks', '-C', root, ...args], {
    encoding: 'utf8',
    env: { ...process.env, GIT_OPTIONAL_LOCKS: '0' },
    stdio: ['ignore', 'pipe', 'ignore'],
  });
}

export function observeGitRepository(root: string): GitObservation {
  const revision = readGit(root, ['rev-parse', 'HEAD']).trim();
  const worktreeRecord = readGit(root, [
    'status',
    '--porcelain=v1',
    '-z',
    '--untracked-files=all',
  ]);
  return {
    revision,
    worktreeMetadataDigest: `sha256:${createHash('sha256').update(worktreeRecord).digest('hex')}`,
    clean: worktreeRecord.length === 0,
  };
}
