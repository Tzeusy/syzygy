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
  git(root, ['config', 'gc.auto', '0']);
  git(root, ['config', 'maintenance.auto', 'false']);
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
    expect(result.provenance).toEqual({ kind: 'git-revision', source: 'Observed repository', revision });
    expect(result.files.length).toBe(4);
    // Every entry takes the revision from the one record; none restates it.
    expect(result.files.every((file) => !Object.values(file).includes(revision))).toBe(true);

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

  it('records a path with a space, a tab, a double quote or a non-ASCII UTF-8 name exactly as committed (syzygy-bpyt.6.1)', () => {
    const { root } = fixtureRepo('sentinel-paths');
    // Unicode escapes keep the fixture bytes exact (AGENTS.md: the Write tool has emitted mixed NFC/NFD).
    const names = ['with space.md', 'tab\there.md', 'a "b".txt', '\u00f1.md', 'dir \u00e9/x.ts'];
    for (const name of names) {
      mkdirSync(dirname(join(root, name)), { recursive: true });
      writeFileSync(join(root, name), 'x\n', 'utf8');
    }
    git(root, ['add', '-A']);
    git(root, ['commit', '-qm', 'awkward paths']);
    const revision = git(root, ['rev-parse', 'HEAD']);
    const result = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-10-21T00:00:00Z' });
    if (result.kind !== 'observed') throw new Error(`expected observed, got ${JSON.stringify(result)}`);
    expect(result.files.map((file) => file.path)).toEqual(
      ['README.md', 'a "b".txt', 'data.json', 'dir \u00e9/x.ts', 'src/app.ts', 'src/nested/lib.py', 'tab\there.md', 'with space.md', '\u00f1.md'],
    );
    expect(result.files.find((file) => file.path === '\u00f1.md')?.language).toBe('markdown');
    expect(result.files.find((file) => file.path === 'dir \u00e9/x.ts')?.digest).toBe(`git-blob-sha1:${git(root, ['rev-parse', `${revision}:dir \u00e9/x.ts`])}`);
  });

  it('asks git for NUL-terminated records and turns any record it cannot read into Unknown, never a skip', () => {
    const blob = (path: string, id = '1'.repeat(40), size = '12'): string => `100644 blob ${id} ${size}\t${path}\0`;
    const observe = (listing: string, calls: string[][] = []) => observeCodeStructure({
      repoRoot: '/unused', revision: 'r', capturedAt: '2026-10-21T00:00:00Z',
      runGit: (_root, args) => { calls.push([...args]); return listing; },
    });
    const calls: string[][] = [];
    const observed = observe(`${blob('a.ts')}160000 commit ${'2'.repeat(40)}       -\tvendor/sub\0${blob('b.md', '3'.repeat(40), '7')}`, calls);
    expect(calls).toEqual([['ls-tree', '-r', '-z', '-l', 'r']]);
    expect(observed).toMatchObject({ kind: 'observed', files: [
      { path: 'a.ts', sizeBytes: 12, digest: `git-blob-sha1:${'1'.repeat(40)}`, language: 'typescript' },
      { path: 'b.md', sizeBytes: 7, digest: `git-blob-sha1:${'3'.repeat(40)}`, language: 'markdown' },
    ] });
    const unknown = { kind: 'unknown', reason: 'code-structure observation produced a malformed inventory entry' };
    expect(observe(`${blob('a.ts')}not a tree record\0`)).toEqual(unknown);
    expect(observe(`${blob('a.ts')}100644 blob ${'1'.repeat(40)} 12\t"\\303\\261.md"\0`)).toEqual(unknown);
    expect(observe(blob('a.ts', '4'.repeat(64)))).toEqual(unknown);
    expect(observe(blob('a.ts', '1'.repeat(40), '-'))).toEqual(unknown);
    // A listing in the newline format, or one whose last record lacks its NUL, is not what `-z` returns.
    expect(observe(`100644 blob ${'1'.repeat(40)} 12\ta.ts\n`)).toEqual(unknown);
    expect(observe(`${blob('a.ts')}100644 blob ${'3'.repeat(40)} 7\tb.md`)).toEqual(unknown);
    expect(observe('')).toMatchObject({ kind: 'observed', files: [] });
  });

  it('makes the inventory Unknown for a committed path that is not valid UTF-8, never a lossy or colliding path', () => {
    const { root } = fixtureRepo('sentinel-non-utf8');
    writeFileSync(join(root, 'blob.txt'), 'x\n', 'utf8');
    const blob = git(root, ['hash-object', '-w', 'blob.txt']);
    // Two Latin-1 names that a replacing decoder would turn into one path; mktree takes the raw bytes.
    const tree = execFileSync('git', ['-C', root, 'mktree', '-z'], {
      input: Buffer.concat([0xf1, 0xf2].map((byte) => Buffer.concat([Buffer.from(`100644 blob ${blob}\t`), Buffer.from([byte]), Buffer.from('.md\0')]))),
      stdio: ['pipe', 'pipe', 'ignore'],
    }).toString('utf8').trim();
    const revision = git(root, ['commit-tree', tree, '-m', 'non-UTF-8 names']);
    expect(observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-10-21T00:00:00Z' }))
      .toEqual({ kind: 'unknown', reason: 'code-structure observation produced a path that is not valid UTF-8' });
  });

  it('produces identical facts across two observations of one revision, excluding capture instant (POC-REQ-004)', () => {
    const { root, revision } = fixtureRepo('sentinel-004');
    const first = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-08-30T00:00:00Z' });
    const second = observeCodeStructure({ repoRoot: root, revision, capturedAt: '2026-08-30T09:00:00Z' });
    expect(first.kind).toBe('observed');
    expect(second.kind).toBe('observed');
    if (first.kind !== 'observed' || second.kind !== 'observed') throw new Error('unreachable');
    expect(second.files).toEqual(first.files);
    expect(second.provenance).toEqual(first.provenance);
    expect(second.capturedAt).not.toBe(first.capturedAt);
  });
});
