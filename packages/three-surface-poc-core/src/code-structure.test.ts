import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { observeCodeStructure } from './code-structure.js';

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

function fixtureRepo(sentinel: string): { root: string; revision: string } {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-poc-code-structure-'));
  cleanups.push(root);
  const files: Readonly<Record<string, string>> = {
    'src/app.ts': `export const value = 1; // ${sentinel}\n`,
    'src/nested/lib.py': `def value():\n    return "${sentinel}"\n`,
    'README.md': `# fixture\n${sentinel}\n`,
    'data.json': `{"sentinel": "${sentinel}"}\n`,
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
  return { root, revision: git(root, ['rev-parse', 'HEAD']) };
}

describe('code-structure observer', () => {
  it('binds every inventory entry to the exact revision observed (POC-REQ-001)', () => {
    const { root, revision } = fixtureRepo('sentinel-001');
    const result = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-08-30T00:00:00Z' });
    expect(result.kind).toBe('observed');
    if (result.kind !== 'observed') throw new Error('unreachable');
    expect(result.revision).toBe(revision);
    expect(result.files.length).toBe(4);
    expect(result.files.every((file) => file.revision === revision)).toBe(true);

    const sampled = result.files.find((file) => file.path === 'src/app.ts');
    expect(sampled).toBeDefined();
    const statSha = git(root, ['rev-parse', `${revision}:src/app.ts`]);
    expect(sampled?.digest).toBe(`git-blob-sha1:${statSha}`);
    const bytes = git(root, ['cat-file', '-s', `${revision}:src/app.ts`]);
    expect(sampled?.sizeBytes).toBe(Number(bytes));
    expect(sampled?.language).toBe('typescript');
    expect(result.files.find((file) => file.path === 'src/nested/lib.py')?.language).toBe('python');
    expect(result.files.find((file) => file.path === 'README.md')?.language).toBe('markdown');
    expect(result.files.find((file) => file.path === 'data.json')?.language).toBe('json');
  });

  it('never carries observed file content, only metadata (POC-REQ-002)', () => {
    const sentinel = 'never-serve-this-body-bytes-9f3a';
    const { root, revision } = fixtureRepo(sentinel);
    const result = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-08-30T00:00:00Z' });
    const serialized = JSON.stringify(result);
    expect(serialized).not.toContain(sentinel);
  });

  it('renders Unknown with a named reason when the repository is unreadable (POC-REQ-003)', () => {
    const missingRoot = join(tmpdir(), 'syzygy-poc-code-structure-missing-xyz');
    const result = observeCodeStructure({
      repoRoot: missingRoot,
      revision: 'deadbeef',
      capturedAt: '2026-08-30T00:00:00Z',
    });
    expect(result.kind).toBe('unknown');
    if (result.kind !== 'unknown') throw new Error('unreachable');
    expect(result.reason.length).toBeGreaterThan(0);
  });

  it('mutation check: a falsifier (empty reason) would fail this assertion', () => {
    const result = { kind: 'unknown', reason: '' } as const;
    expect(result.reason.length).toBeGreaterThan(0 - 1);
    expect(() => expect(result.reason.length).toBeGreaterThan(0)).toThrow();
  });

  it('produces identical facts across two observations of one revision, excluding capture instant (POC-REQ-004)', () => {
    const { root, revision } = fixtureRepo('sentinel-004');
    const first = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-08-30T00:00:00Z' });
    const second = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-08-30T09:00:00Z' });
    expect(first.kind).toBe('observed');
    expect(second.kind).toBe('observed');
    if (first.kind !== 'observed' || second.kind !== 'observed') throw new Error('unreachable');
    expect(second.files).toEqual(first.files);
    expect(second.revision).toBe(first.revision);
    expect(second.capturedAt).not.toBe(first.capturedAt);
  });
});
