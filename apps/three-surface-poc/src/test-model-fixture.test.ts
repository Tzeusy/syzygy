import { execFileSync, spawn } from 'node:child_process';
import { once } from 'node:events';
import { chmodSync, existsSync, mkdirSync, mkdtempSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
import type { PocModel } from '@syzygy/three-surface-poc-core';

import { fixtureRepoWithGit, frozenFixture, removeFixturesOfDeadProcesses, sharedFixtureModels } from './test-model-fixture.js';

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

describe('fixture directories a killed run left behind (syzygy-bpyt.4.10)', () => {
  const FIXTURE_PREFIX = 'syzygy-poc-surface-fixture-';
  const privateTmp: string[] = [];
  afterEach(() => {
    vi.restoreAllMocks();
    vi.unstubAllEnvs();
    vi.resetModules();
    for (const directory of privateTmp.splice(0)) rmSync(directory, { recursive: true, force: true });
  });

  function newTmp(): string {
    const tmp = mkdtempSync(join(tmpdir(), 'syzygy-fixture-sweep-'));
    privateTmp.push(tmp);
    return tmp;
  }
  /** The pid of a process that has run and been reaped, checked to answer ESRCH. */
  async function deadPid(): Promise<number> {
    const child = spawn(process.execPath, ['-e', '']);
    await once(child, 'exit');
    const pid = child.pid!;
    expect(() => process.kill(pid, 0)).toThrow(expect.objectContaining({ code: 'ESRCH' }));
    return pid;
  }
  const entries = (tmp: string): string[] => readdirSync(tmp).sort();
  const make = (tmp: string, ...names: string[]): void => {
    for (const name of names) {
      mkdirSync(join(tmp, name, 'repo'), { recursive: true });
      writeFileSync(join(tmp, name, 'repo', 'README.md'), '# left behind\n');
    }
  };

  it('removes the copy and the template of a process that is gone', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    make(tmp, `${FIXTURE_PREFIX}p${dead}-AbCdEf`, `${FIXTURE_PREFIX}template-p${dead}-AbCdEf`);
    removeFixturesOfDeadProcesses(tmp);
    expect(entries(tmp)).toEqual([]);
  });

  it('keeps the directories of a live process, the current one included', () => {
    const tmp = newTmp();
    const mine = [`${FIXTURE_PREFIX}p${process.pid}-AbCdEf`, `${FIXTURE_PREFIX}template-p${process.pid}-AbCdEf`];
    make(tmp, ...mine);
    removeFixturesOfDeadProcesses(tmp);
    expect(entries(tmp)).toEqual([...mine].sort());
  });

  it('keeps a name that carries no pid segment, whatever its suffix', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const kept = [
      `${FIXTURE_PREFIX}AbCdEf`, // made before pids were added
      `${FIXTURE_PREFIX}template-AbCdEf`,
      `${FIXTURE_PREFIX}p${dead}`, // pid with no hyphen after it
      `${FIXTURE_PREFIX}x-p${dead}-AbCdEf`, // pid segment not straight after the prefix
      `${FIXTURE_PREFIX}template-x-p${dead}-AbCdEf`,
      `other-fixture-p${dead}-AbCdEf`, // another prefix
      `copy-of-${FIXTURE_PREFIX}p${dead}-AbCdEf`, // the prefix inside a longer name
      `${FIXTURE_PREFIX.slice(0, -1)}p${dead}-AbCdEf`, // prefix without its last hyphen
    ];
    make(tmp, ...kept);
    removeFixturesOfDeadProcesses(tmp);
    expect(entries(tmp)).toEqual([...kept].sort());
  });

  it('keeps a directory whose pid fails with anything but ESRCH', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const denied = `${FIXTURE_PREFIX}p${dead}-AbCdEf`;
    const outOfRange = `${FIXTURE_PREFIX}template-p99999999999999999999-AbCdEf`;
    make(tmp, denied, outOfRange);
    const kill = process.kill.bind(process);
    vi.spyOn(process, 'kill').mockImplementation((pid, signal) => {
      if (pid === dead) throw Object.assign(new Error('operation not permitted'), { code: 'EPERM' });
      return kill(pid, signal);
    });
    removeFixturesOfDeadProcesses(tmp);
    expect(entries(tmp)).toEqual([denied, outOfRange].sort());
  });

  it('does not fail the run when a dead process\'s directory cannot be removed', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const stuck = `${FIXTURE_PREFIX}p${dead}-AbCdEf`;
    make(tmp, stuck, `${FIXTURE_PREFIX}template-p${dead}-AbCdEf`);
    chmodSync(join(tmp, stuck), 0o555);
    try {
      expect(() => removeFixturesOfDeadProcesses(tmp)).not.toThrow();
      // The other directory is still removed: one failure does not end the sweep.
      expect(entries(tmp)).not.toContain(`${FIXTURE_PREFIX}template-p${dead}-AbCdEf`);
    } finally {
      chmodSync(join(tmp, stuck), 0o755);
    }
  });

  it('names the template and each copy with the pid of the process that made them', async () => {
    const tmp = newTmp();
    vi.stubEnv('TMPDIR', tmp);
    vi.resetModules();
    const helper = await import('./test-model-fixture.js');
    const copies = [helper.fixtureRepoWithGit([]), helper.fixtureRepoWithGit([])];
    const names = entries(tmp);
    expect(names.filter((name) => new RegExp(`^${FIXTURE_PREFIX}template-p${process.pid}-[A-Za-z0-9]{6}$`).test(name))).toHaveLength(1);
    expect(names.filter((name) => new RegExp(`^${FIXTURE_PREFIX}p${process.pid}-[A-Za-z0-9]{6}$`).test(name))).toHaveLength(2);
    expect(names).toHaveLength(3);
    expect(copies.map((copy) => copy.repoRoot.startsWith(join(tmp, `${FIXTURE_PREFIX}p${process.pid}-`)))).toEqual([true, true]);
  }, 30_000);

  it('sweeps the dead before it makes the file\'s template, and keeps the live and the legacy', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const survivors = [`${FIXTURE_PREFIX}p${process.pid}-AbCdEf`, `${FIXTURE_PREFIX}AbCdEf`, `${FIXTURE_PREFIX}template-AbCdEf`];
    make(tmp, `${FIXTURE_PREFIX}p${dead}-AbCdEf`, `${FIXTURE_PREFIX}template-p${dead}-AbCdEf`, ...survivors);
    vi.stubEnv('TMPDIR', tmp);
    vi.resetModules();
    const helper = await import('./test-model-fixture.js');
    expect(entries(tmp)).toHaveLength(survivors.length + 2);
    const copy = helper.fixtureRepoWithGit([]);
    const after = entries(tmp);
    expect(after.filter((name) => name.includes(`p${dead}-`))).toEqual([]);
    expect(after).toEqual(expect.arrayContaining(survivors));
    expect(after).toHaveLength(survivors.length + 2);
    expect(existsSync(copy.repoRoot)).toBe(true);
  }, 30_000);
});
