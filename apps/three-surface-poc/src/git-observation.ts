import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { realpathSync } from 'node:fs';
import { join, resolve } from 'node:path';

export const PWB_APPROVED_REPOSITORY_LOCATOR = '/home/tze/GitHub/butlers';

export type PwbRepositoryBinding =
  | { readonly kind: 'bound'; readonly locator: string; readonly gitCommonDirectory: string }
  | { readonly kind: 'rejected'; readonly reason: 'locator-mismatched' | 'git-common-directory-mismatched' | 'binding-unreadable' };

export interface ResolvePwbRepositoryBindingOptions {
  readonly approvedLocator?: string;
  readonly realpath?: (path: string) => string;
  readonly runGit?: (root: string, args: readonly string[]) => string;
}

export interface GitObservation {
  readonly revision: string;
  readonly committerInstant: string;
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

export function resolvePwbRepositoryBinding(
  configuredLocator: string,
  options: ResolvePwbRepositoryBindingOptions = {},
): PwbRepositoryBinding {
  const realpath = options.realpath ?? realpathSync;
  const runGit = options.runGit ?? readGit;
  try {
    const approvedLocator = realpath(resolve(options.approvedLocator ?? PWB_APPROVED_REPOSITORY_LOCATOR));
    const locator = realpath(resolve(configuredLocator));
    if (locator !== approvedLocator) return { kind: 'rejected', reason: 'locator-mismatched' };
    const gitCommonDirectory = realpath(
      resolve(locator, runGit(locator, ['rev-parse', '--path-format=absolute', '--git-common-dir']).trim()),
    );
    const approvedGitCommonDirectory = realpath(join(approvedLocator, '.git'));
    if (gitCommonDirectory !== approvedGitCommonDirectory) {
      return { kind: 'rejected', reason: 'git-common-directory-mismatched' };
    }
    return { kind: 'bound', locator, gitCommonDirectory };
  } catch {
    return { kind: 'rejected', reason: 'binding-unreadable' };
  }
}

function nulSeparatedPaths(record: string): readonly string[] {
  return record.split('\0').filter((candidate) => candidate !== '');
}

export function observeGitRepository(root: string): GitObservation {
  const revision = readGit(root, ['rev-parse', 'HEAD']).trim();
  const committerInstant = readGit(root, ['show', '-s', '--format=%cI', revision]).trim();
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
    committerInstant,
    worktreeMetadataDigest: `sha256:${createHash('sha256').update(worktreeRecord).digest('hex')}`,
    clean: worktreeRecord.length === 0,
    changedPaths: [...new Set(changedPaths)].sort(),
  };
}

export interface GitHorizonObservation {
  readonly pinnedRevision: string;
  readonly currentRevision: string;
  readonly currentCommitterInstant: string;
  readonly changedSources: number;
  readonly addedSources: number;
}

export interface ObserveGitHorizonOptions {
  readonly runGit?: (root: string, args: readonly string[]) => string;
}

/** Compare revision metadata only; no source body is opened. */
export function observeGitHorizon(
  root: string,
  pinnedRevision: string,
  options: ObserveGitHorizonOptions = {},
): GitHorizonObservation {
  const runGit = options.runGit ?? readGit;
  const currentRevision = runGit(root, ['rev-parse', 'HEAD']).trim();
  const currentCommitterInstant = runGit(root, ['show', '-s', '--format=%cI', currentRevision]).trim();
  if (currentRevision === pinnedRevision) {
    return { pinnedRevision, currentRevision, currentCommitterInstant, changedSources: 0, addedSources: 0 };
  }
  const diff = runGit(root, ['diff', '--name-status', '--no-renames', '-z', `${pinnedRevision}..${currentRevision}`]);
  const entries = diff.split('\0').filter((entry) => entry !== '');
  let changedSources = 0;
  let addedSources = 0;
  const records = entries.some((entry) => entry.includes('\t'))
    ? entries
    : entries.filter((_entry, index) => index % 2 === 0);
  for (const entry of records) {
    const tab = entry.indexOf('\t');
    const status = tab < 0 ? entry : entry.slice(0, tab);
    if (status.startsWith('A')) addedSources += 1;
    else changedSources += 1;
  }
  return { pinnedRevision, currentRevision, currentCommitterInstant, changedSources, addedSources };
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
