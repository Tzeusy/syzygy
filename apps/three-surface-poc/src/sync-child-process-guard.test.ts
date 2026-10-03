import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));

// The root suite's test roots (vitest.config.ts `test.projects` include
// globs). A vitest worker answers its parent over an RPC with a fixed 60s
// timeout; a test that blocks the worker's event loop longer than that makes
// the pending `onTaskUpdate` call time out, and the run exits 1 with every
// test passed (syzygy-w90k). An install, a build or a documented command can
// run past 60s under load, so only short local tools may run synchronously.
const SUITE_ROOTS = [
  'apps/three-surface-poc/src/',
  'packages/polaris-generation-core/src/',
  'packages/cap1-conformance/src/',
  'packages/cap1-daemon/src/',
  'packages/three-surface-poc-core/src/',
];
const SHORT_COMMANDS = new Set(['git', 'mkfifo', 'bd']);
// Live-gated: skipped unless SYZYGY_POC_BUTLERS_REPO is set, so never in the
// default suite; it runs one focused pytest file against Butlers.
const EXEMPT = new Set(['packages/three-surface-poc-core/src/test-artifact-verification.live.test.ts:31']);
const SELF = 'apps/three-surface-poc/src/sync-child-process-guard.test.ts';
const SYNC_CALL = /\b(?:execFileSync|execSync|spawnSync)\s*\(\s*([^,)\n]*)/g;

function longSyncCalls(source: string): { line: number; command: string }[] {
  return [...source.matchAll(SYNC_CALL)]
    .map((match) => ({ line: source.slice(0, match.index).split('\n').length, command: match[1]!.trim() }))
    .filter(({ command }) => !SHORT_COMMANDS.has(command.replace(/^(['"`])(.*)\1$/, '$2')) || !/^['"`]/.test(command));
}

function suiteTestFiles(): string[] {
  return execFileSync('git', ['-C', REPO_ROOT, 'ls-files', '-z', '--cached', '--others', '--exclude-standard', '--', '*.test.ts'], { encoding: 'utf8' })
    .split('\0')
    .filter((path) => SUITE_ROOTS.some((root) => path.startsWith(root)));
}

describe('suite child processes and the vitest worker RPC', () => {
  it('runs only short local tools synchronously in a suite test file', () => {
    const files = suiteTestFiles();
    expect(files.length).toBeGreaterThan(100);
    expect(files).toContain(SELF);
    const offenders = files
      .filter((path) => path !== SELF)
      .flatMap((path) => longSyncCalls(readFileSync(join(REPO_ROOT, path), 'utf8')).map(({ line, command }) => `${path}:${line} ${command}`))
      .filter((offender) => !EXEMPT.has(offender.split(' ')[0]!));
    expect(offenders).toEqual([]);
  });

  it('flags an install, a build or a computed command and leaves async and short tools alone', () => {
    const commands = (source: string): string[] => longSyncCalls(source).map(({ command }) => command);
    expect(commands("execFileSync('npm', ['ci'])")).toEqual(["'npm'"]);
    expect(commands('execSync("npm run build:poc")')).toEqual(['"npm run build:poc"']);
    expect(commands('spawnSync(`npx`, [])')).toEqual(['`npx`']);
    expect(commands('execFileSync(documented[0]!, args)')).toEqual(['documented[0]!']);
    expect(commands('execFileSync(git, args)')).toEqual(['git']);
    expect(commands("await run('npm', ['ci'])")).toEqual([]);
    expect(commands("execFile('npm', ['ci'])")).toEqual([]);
    expect(commands("execFileSync('git', ['rev-parse', 'HEAD'])")).toEqual([]);
    expect(commands('spawnSync("mkfifo", [path])')).toEqual([]);
    expect(commands("execSync('git status')")).toEqual(["'git status'"]);
  });
});
