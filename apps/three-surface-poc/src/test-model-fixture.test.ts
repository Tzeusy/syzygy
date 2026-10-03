import { execFileSync } from 'node:child_process';
import { existsSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import type { PocModel } from '@syzygy/three-surface-poc-core';

import { fixtureRepoWithGit, frozenFixture, sharedFixtureModels } from './test-model-fixture.js';

describe('fixture repositories (syzygy-jsyi)', () => {
  const git = (root: string, args: readonly string[]): string => execFileSync('git', ['-C', root, ...args], { encoding: 'utf8' }).trim();

  it('gives each call its own clean copy at the revision a fresh pinned commit mints, and keeps a write in its own copy', () => {
    const cleanups: string[] = [];
    try {
      const first = fixtureRepoWithGit(cleanups);
      const second = fixtureRepoWithGit(cleanups);
      expect(first.repoRoot).not.toBe(second.repoRoot);
      expect(cleanups).toEqual([first.repoRoot, second.repoRoot]);
      // Committed by hand from the same eight files, author and pinned instants.
      expect([first.revision, second.revision]).toEqual(['1f892687d53c829f9c2a4ee99bccccb23d6158df', '1f892687d53c829f9c2a4ee99bccccb23d6158df']);
      expect(git(first.repoRoot, ['rev-parse', 'HEAD'])).toBe(first.revision);
      expect(git(first.repoRoot, ['status', '--porcelain'])).toBe('');
      writeFileSync(join(first.repoRoot, 'README.md'), 'changed\n');
      expect(git(first.repoRoot, ['status', '--porcelain'])).toBe('M README.md');
      expect(git(second.repoRoot, ['status', '--porcelain'])).toBe('');
      rmSync(first.repoRoot, { recursive: true, force: true });
      const third = fixtureRepoWithGit(cleanups);
      expect(git(third.repoRoot, ['rev-parse', 'HEAD'])).toBe(third.revision);
      expect(git(third.repoRoot, ['status', '--porcelain'])).toBe('');
    } finally {
      for (const directory of cleanups) rmSync(directory, { recursive: true, force: true });
    }
  });
});

describe('shared fixture models (syzygy-k66p)', () => {
  it('freezes every nested object and array, so a test that writes to a shared model throws', () => {
    const value = frozenFixture({ shape: { items: [{ state: 'observed' }] }, bytes: new Uint8Array([1, 2]) });
    expect(() => { (value.shape.items[0] as { state: string }).state = 'unknown'; }).toThrow(TypeError);
    expect(() => { (value.shape.items as { state: string }[]).push({ state: 'extra' }); }).toThrow(TypeError);
    expect(() => { (value as { shape: unknown }).shape = {}; }).toThrow(TypeError);
    expect(value.shape.items[0]?.state).toBe('observed');
    expect(Object.isFrozen(value.bytes)).toBe(false);
  });

  it('builds once, refuses a read before prepare, and removes its repositories', () => {
    let builds = 0;
    let directory = '';
    const shared = sharedFixtureModels<'only'>((cleanups) => {
      builds += 1;
      directory = mkdtempSync(join(tmpdir(), 'syzygy-k66p-shared-'));
      cleanups.push(directory);
      return { only: { marker: builds } as unknown as PocModel };
    });
    expect(() => shared.get('only')).toThrow('shared fixture models used before prepare');
    shared.prepare();
    shared.prepare();
    expect(builds).toBe(1);
    expect(shared.get('only')).toBe(shared.get('only'));
    expect(Object.isFrozen(shared.get('only'))).toBe(true);
    expect(existsSync(directory)).toBe(true);
    shared.remove();
    expect(existsSync(directory)).toBe(false);
    expect(() => shared.get('only')).toThrow('shared fixture models used before prepare');
  });
});
