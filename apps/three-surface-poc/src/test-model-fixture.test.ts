import { execFileSync } from 'node:child_process';
import { existsSync, mkdtempSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
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
      // Git state is per copy too: a stage, a commit and a new ref in one copy
      // reach neither a sibling nor the template a later copy comes from.
      const refs = git(second.repoRoot, ['for-each-ref', '--format=%(refname) %(objectname)']);
      const index = git(second.repoRoot, ['ls-files', '--stage']);
      git(first.repoRoot, ['add', 'README.md']);
      git(first.repoRoot, ['-c', 'commit.gpgsign=false', '-c', 'user.name=Writer', '-c', 'user.email=writer@example.invalid', 'commit', '-qm', 'write']);
      git(first.repoRoot, ['update-ref', 'refs/heads/written', 'HEAD']);
      expect(git(first.repoRoot, ['rev-parse', 'HEAD'])).not.toBe(first.revision);
      for (const copy of [second, fixtureRepoWithGit(cleanups)]) {
        expect(git(copy.repoRoot, ['rev-parse', 'HEAD'])).toBe(first.revision);
        expect(git(copy.repoRoot, ['for-each-ref', '--format=%(refname) %(objectname)'])).toBe(refs);
        expect(git(copy.repoRoot, ['ls-files', '--stage'])).toBe(index);
        expect(git(copy.repoRoot, ['status', '--porcelain'])).toBe('');
      }
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

describe('fixture repositories a caller never drains (syzygy-bpyt.4.10)', () => {
  const FIXTURE_PREFIX = 'syzygy-poc-surface-fixture-';
  const privateTmp: string[] = [];
  afterEach(() => {
    vi.restoreAllMocks();
    vi.unstubAllGlobals();
    vi.unstubAllEnvs();
    vi.resetModules();
    for (const directory of privateTmp.splice(0)) rmSync(directory, { recursive: true, force: true });
  });

  /** A fresh copy of the helper module that sees only this test's own TMPDIR, so the
   * directories it makes can be counted without another test file's. */
  async function freshHelper(): Promise<{ readonly helper: typeof import('./test-model-fixture.js'); readonly tmp: string }> {
    const tmp = mkdtempSync(join(tmpdir(), 'syzygy-fixture-leak-'));
    privateTmp.push(tmp);
    vi.stubEnv('TMPDIR', tmp);
    vi.resetModules();
    return { helper: await import('./test-model-fixture.js'), tmp };
  }
  const fixtureEntries = (tmp: string): string[] => readdirSync(tmp).filter((name) => name.startsWith(FIXTURE_PREFIX)).sort();

  it('removes the template and every copy through one end-of-file teardown, drained or not', async () => {
    const teardowns: (() => void)[] = [];
    vi.stubGlobal('syzygyAfterTestFile', (teardown: () => void) => { teardowns.push(teardown); });
    const { helper, tmp } = await freshHelper();
    const neverDrained: string[] = [];
    const drainedEarly: string[] = [];
    const kept = helper.fixtureRepoWithGit(neverDrained);
    const early = helper.fixtureRepoWithGit(drainedEarly);
    const alsoKept = helper.fixtureRepoWithGit(neverDrained);
    for (const directory of drainedEarly.splice(0)) rmSync(directory, { recursive: true, force: true });
    // Before the file ends: the template and the two copies the caller never drained.
    expect(fixtureEntries(tmp)).toHaveLength(3);
    expect(fixtureEntries(tmp).filter((name) => name.startsWith(`${FIXTURE_PREFIX}template-`))).toHaveLength(1);
    expect(existsSync(kept.repoRoot) && existsSync(alsoKept.repoRoot)).toBe(true);
    expect(existsSync(early.repoRoot)).toBe(false);
    expect(teardowns).toHaveLength(1);
    teardowns.splice(0).forEach((teardown) => teardown());
    expect(fixtureEntries(tmp)).toEqual([]);
    expect(neverDrained).toEqual([kept.repoRoot, alsoKept.repoRoot]);

    // The teardown leaves the helper ready for the next file: a new template, and a new teardown.
    const next = helper.fixtureRepoWithGit([]);
    expect(existsSync(next.repoRoot)).toBe(true);
    expect(fixtureEntries(tmp)).toHaveLength(2);
    expect(teardowns).toHaveLength(1);
    teardowns.splice(0).forEach((teardown) => teardown());
    expect(fixtureEntries(tmp)).toEqual([]);
  }, 30_000);

  it('outside Vitest registers one exit listener for the template and all copies', async () => {
    vi.stubGlobal('syzygyAfterTestFile', undefined);
    const exitListeners: (() => void)[] = [];
    vi.spyOn(process, 'once').mockImplementation(((event: string, listener: () => void) => {
      if (event === 'exit') exitListeners.push(listener);
      return process;
    }) as typeof process.once);
    const { helper, tmp } = await freshHelper();
    const copies = [helper.fixtureRepoWithGit([]), helper.fixtureRepoWithGit([]), helper.fixtureRepoWithGit([])];
    expect(fixtureEntries(tmp)).toHaveLength(4);
    expect(exitListeners).toHaveLength(1);
    exitListeners[0]?.();
    expect(copies.some((copy) => existsSync(copy.repoRoot))).toBe(false);
    expect(fixtureEntries(tmp)).toEqual([]);
  }, 30_000);
});
