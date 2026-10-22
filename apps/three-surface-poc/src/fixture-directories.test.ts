import { spawn } from 'node:child_process';
import { once } from 'node:events';
import { chmodSync, existsSync, lstatSync, mkdirSync, mkdtempSync, readdirSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';

import { FIXTURE_PREFIX, removeFixturesOfDeadProcesses } from './fixture-directories.js';
import removeFixturesOfKilledRuns from './test-fixture-sweep.global-setup.js';

describe('fixture directories a killed run left behind (syzygy-bpyt.4.10)', () => {
  const privateTmp: string[] = [];
  afterEach(() => {
    vi.restoreAllMocks();
    vi.unstubAllEnvs();
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

  it('follows no symlink and removes no file: only a directory with a dead pid in its name goes', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const outside = join(tmp, 'outside');
    mkdirSync(join(outside, 'precious'), { recursive: true });
    writeFileSync(join(outside, 'precious', 'keep.txt'), 'not a fixture\n');
    const swept = join(tmp, 'swept');
    mkdirSync(swept);
    const link = `${FIXTURE_PREFIX}p${dead}-LinkTo`;
    const file = `${FIXTURE_PREFIX}template-p${dead}-AFile1`;
    symlinkSync(outside, join(swept, link));
    writeFileSync(join(swept, file), 'a file\n');
    make(swept, `${FIXTURE_PREFIX}p${dead}-AbCdEf`);
    removeFixturesOfDeadProcesses(swept);
    expect(entries(swept)).toEqual([file, link].sort());
    expect(lstatSync(join(swept, link)).isSymbolicLink()).toBe(true);
    expect(existsSync(join(outside, 'precious', 'keep.txt'))).toBe(true);
  });

  it('lists only the directory it is given: nothing beside it, nothing below a non-fixture entry', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const swept = join(tmp, 'swept');
    const beside = `${FIXTURE_PREFIX}p${dead}-Beside`;
    const below = join('somebody-elses', `${FIXTURE_PREFIX}p${dead}-Below`);
    mkdirSync(swept);
    make(tmp, beside);
    make(swept, below);
    removeFixturesOfDeadProcesses(swept);
    expect(existsSync(join(tmp, beside))).toBe(true);
    expect(existsSync(join(swept, below))).toBe(true);
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

  it('sweeps the temp directory the process runs under when the global setup runs, and keeps the live and the legacy', async () => {
    const tmp = newTmp();
    const dead = await deadPid();
    const survivors = [`${FIXTURE_PREFIX}p${process.pid}-AbCdEf`, `${FIXTURE_PREFIX}AbCdEf`, `${FIXTURE_PREFIX}template-AbCdEf`];
    make(tmp, `${FIXTURE_PREFIX}p${dead}-AbCdEf`, `${FIXTURE_PREFIX}template-p${dead}-AbCdEf`, ...survivors);
    vi.stubEnv('TMPDIR', tmp);
    removeFixturesOfKilledRuns();
    expect(entries(tmp)).toEqual([...survivors].sort());
  });

  it('is registered as a global setup of the app project and of no other project, so it runs once per run', async () => {
    const config = (await import(/* @vite-ignore */ new URL('../../../vitest.config.ts', import.meta.url).href)).default as {
      readonly test: { readonly globalSetup?: unknown; readonly projects: readonly { readonly test: { readonly name: string; readonly globalSetup?: readonly string[] } }[] };
    };
    const withSetup = config.test.projects.filter((project) => project.test.globalSetup !== undefined);
    expect(config.test.globalSetup).toBeUndefined();
    expect(withSetup.map((project) => project.test.name)).toEqual(['@syzygy/three-surface-poc-app']);
    const files = withSetup[0]?.test.globalSetup ?? [];
    expect(files).toHaveLength(1);
    expect(files[0]?.endsWith('/apps/three-surface-poc/src/test-fixture-sweep.global-setup.ts')).toBe(true);
  });
});
