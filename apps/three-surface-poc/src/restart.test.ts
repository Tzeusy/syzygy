import { spawn } from 'node:child_process';
import { createServer } from 'node:net';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { afterAll, afterEach, describe, expect, it } from 'vitest';

import { inspectPocPort, listenerPidFromSs, restartOnePocListener, RestartRefusal, type PocListener } from './restart.js';

const fixture = resolve('apps/three-surface-poc/src/test-fixtures/restart-listener.mjs');
const roots: string[] = [];
const pids: number[] = [];
const cleanupObservations: number[][] = [];

function scratch(): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-private-restart-'));
  roots.push(root);
  return root;
}

async function freePort(): Promise<number> {
  const server = createServer();
  await new Promise<void>(resolveListen => server.listen(0, '127.0.0.1', resolveListen));
  const address = server.address();
  if (address === null || typeof address === 'string') throw new Error('test port missing');
  await new Promise<void>(resolveClose => server.close(() => resolveClose()));
  return address.port;
}

async function readRevision(port: number, timeoutMs = 5000): Promise<string> {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    try {
      const response = await fetch(`http://127.0.0.1:${port}/`);
      if (response.ok) return response.text();
    } catch { /* fixture has not bound yet */ }
    await new Promise(resolveWait => setTimeout(resolveWait, 25));
  }
  throw new Error('private fixture listener did not start');
}

async function waitForMarker(marker: string, timeoutMs = 5000): Promise<void> {
  const deadline = Date.now() + timeoutMs;
  while (!existsSync(marker)) {
    if (Date.now() >= deadline) throw new Error(`private fixture did not write ${marker}`);
    await new Promise(resolveWait => setTimeout(resolveWait, 10));
  }
}

async function startedFixture(mode: 'normal' | 'slow' | 'held' = 'normal'): Promise<{ root: string; repo: string; stateDir: string; port: number; pid: number }> {
  const root = scratch();
  const repo = join(root, 'repo');
  const stateDir = join(root, 'state');
  mkdirSync(repo);
  writeFileSync(join(repo, 'revision'), 'old-revision');
  if (mode === 'slow') writeFileSync(join(repo, 'slow-stop'), 'yes');
  if (mode === 'held') writeFileSync(join(repo, 'hold-stop'), 'yes');
  const port = await freePort();
  const child = spawn(process.execPath, [fixture, '--repo', repo, '--state-dir', stateDir, '--port', String(port)], {
    cwd: process.cwd(), stdio: 'ignore',
  });
  if (child.pid === undefined) throw new Error('fixture process missing');
  pids.push(child.pid);
  expect(await readRevision(port)).toBe('old-revision');
  return { root, repo, stateDir, port, pid: child.pid };
}

function exactPrivateFixturePids(): number[] {
  const matches: number[] = [];
  for (const entry of readdirSync('/proc')) {
    if (!/^\d+$/.test(entry)) continue;
    try {
      const argv = readFileSync(`/proc/${entry}/cmdline`, 'utf8').split('\0').filter(Boolean);
      if (argv[1] !== fixture) continue;
      const repoIndex = argv.indexOf('--repo');
      const stateIndex = argv.indexOf('--state-dir');
      const repo = repoIndex >= 0 ? argv[repoIndex + 1] : undefined;
      const stateDir = stateIndex >= 0 ? argv[stateIndex + 1] : undefined;
      if (repo === undefined || stateDir === undefined) continue;
      if (roots.some(root => repo === join(root, 'repo') && stateDir === join(root, 'state'))) matches.push(Number(entry));
    } catch {
      // A process can disappear while /proc is being enumerated. Unknown
      // rows are never signaled; only an exact argv/repo/state match is safe.
    }
  }
  return matches;
}

afterEach(async () => {
  for (const root of roots) {
    const repo = join(root, 'repo');
    const release = join(repo, 'release-stop');
    if (existsSync(join(repo, 'hold-stop')) && !existsSync(release)) writeFileSync(release, 'release');
  }
  const deadline = Date.now() + 5000;
  let remaining: number[] = [];
  while (true) {
    remaining = exactPrivateFixturePids();
    if (remaining.length === 0) break;
    for (const pid of remaining) {
      try { process.kill(pid, 'SIGTERM'); }
      catch (error) { if ((error as NodeJS.ErrnoException).code !== 'ESRCH') throw error; }
    }
    if (Date.now() >= deadline) throw new Error(`private fixture processes did not drain: ${remaining.join(',')}`);
    await new Promise(resolveWait => setTimeout(resolveWait, 25));
  }
  cleanupObservations.push(remaining);
  pids.splice(0);
  for (const root of roots.splice(0)) rmSync(root, { recursive: true, force: true });
});

afterAll(() => {
  expect(cleanupObservations.every((remaining) => remaining.length === 0)).toBe(true);
});

describe('one-listener POC restart on private fixture sockets', () => {
  it('waits through one vanished post-SIGTERM identity, then starts exactly one successor after socket absence', async () => {
    const f = await startedFixture('slow');
    const credentialBefore = readFileSync(join(f.stateDir, 'machine-credential.token'));
    writeFileSync(join(f.repo, 'revision'), 'new-revision');
    expect(await readRevision(f.port)).toBe('old-revision');
    let inspections = 0;
    const result = await restartOnePocListener({
      port: f.port, expectedScript: fixture, timeoutMs: 5000,
      inspect: port => {
        inspections += 1;
        if (inspections === 3) throw new RestartRefusal('listener-identity-unreadable');
        if (inspections === 4) throw new RestartRefusal('listener-identity-incomplete');
        return inspectPocPort(port);
      },
    });
    pids.push(result.newPid);
    expect(inspections).toBeGreaterThan(4);
    expect(result.oldPid).toBe(f.pid);
    expect(result.newPid).not.toBe(f.pid);
    expect(await readRevision(f.port)).toBe('new-revision');
    expect(readFileSync(join(f.stateDir, 'machine-credential.token'))).toEqual(credentialBefore);
    expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
  }, 15_000);

  it.each(['listener-identity-unreadable', 'listener-identity-incomplete'])(
    'refuses a %s identity before SIGTERM and leaves the old listener serving', async code => {
      const f = await startedFixture();
      let inspections = 0;
      await expect(restartOnePocListener({
        port: f.port, expectedScript: fixture, timeoutMs: 1000,
        inspect: port => {
          inspections += 1;
          if (inspections === 2) throw new RestartRefusal(code);
          return inspectPocPort(port);
        },
      })).rejects.toMatchObject({ code });
      expect(inspections).toBe(2);
      expect(await readRevision(f.port)).toBe('old-revision');
    },
  );

  it.each(['listener-identity-unreadable', 'listener-identity-incomplete'])(
    'times out with no successor while post-SIGTERM identity stays %s', async code => {
      const f = await startedFixture();
      let inspections = 0;
      await expect(restartOnePocListener({
        port: f.port, expectedScript: fixture, timeoutMs: 150,
        inspect: port => {
          inspections += 1;
          if (inspections > 2) throw new RestartRefusal(code);
          return inspectPocPort(port);
        },
      })).rejects.toMatchObject({ code: 'listener-close-timeout' });
      expect(inspections).toBeGreaterThan(2);
      await expect(fetch(`http://127.0.0.1:${f.port}/`)).rejects.toThrow();
      expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
    },
  );

  it.each(['listener-owner-mismatch', 'listener-changed-after-signal'])(
    'hard-refuses %s after SIGTERM without spawning a successor', async code => {
      const f = await startedFixture('slow');
      const credentialBefore = readFileSync(join(f.stateDir, 'machine-credential.token'));
      let inspections = 0;
      await expect(restartOnePocListener({
        port: f.port, expectedScript: fixture, timeoutMs: 1000,
        inspect: port => {
          inspections += 1;
          if (inspections === 3) {
            if (code === 'listener-owner-mismatch') throw new RestartRefusal(code);
            const current = inspectPocPort(port);
            if (current === null) throw new Error('private listener closed before changed-identity inspection');
            return { ...current, started: `${current.started}-changed` };
          }
          return inspectPocPort(port);
        },
      })).rejects.toMatchObject({ code });
      expect(inspections).toBe(3);
      expect(readFileSync(join(f.stateDir, 'machine-credential.token'))).toEqual(credentialBefore);
      expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
    },
  );

  it('closes one listener, reuses credential bytes and state dir, and serves only the new fixture revision', async () => {
    const f = await startedFixture();
    const credentialPath = join(f.stateDir, 'machine-credential.token');
    const credentialBefore = readFileSync(credentialPath);
    writeFileSync(join(f.repo, 'revision'), 'new-revision');
    expect(await readRevision(f.port)).toBe('old-revision');
    const result = await restartOnePocListener({ port: f.port, expectedScript: fixture, expectedCwd: process.cwd(), timeoutMs: 5000 });
    pids.push(result.newPid);
    expect(result.oldPid).toBe(f.pid);
    expect(result.newPid).not.toBe(f.pid);
    expect(result.stateDir).toBe(f.stateDir);
    expect(await readRevision(f.port)).toBe('new-revision');
    expect(readFileSync(credentialPath)).toEqual(credentialBefore);
    expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
  }, 15_000);

  it('refuses an absent listener and ambiguous owner rows without signaling anyone', async () => {
    const port = await freePort();
    await expect(restartOnePocListener({ port, expectedScript: fixture, timeoutMs: 1000 })).rejects.toMatchObject({ code: 'listener-absent' });
    const row = `LISTEN 0 511 127.0.0.1:${port} 0.0.0.0:* users:(("node",pid=123,fd=9))`;
    expect(() => listenerPidFromSs(`${row}\n${row}`, port)).toThrow('multiple-listeners');
    expect(() => listenerPidFromSs(row.replace('pid=123', 'fd=123'), port)).toThrow('listener-owner-ambiguous');
  });

  it('refuses a listener generation changed between inspection and SIGTERM', async () => {
    const f = await startedFixture();
    const argv = [process.execPath, fixture, '--repo', f.repo, '--state-dir', f.stateDir, '--port', String(f.port)];
    const first: PocListener = { pid: f.pid, started: '1', argv, cwd: process.cwd() };
    const second: PocListener = { ...first, started: '2' };
    let calls = 0;
    await expect(restartOnePocListener({ port: f.port, expectedScript: fixture, timeoutMs: 1000, inspect: () => ++calls === 1 ? first : second }))
      .rejects.toMatchObject({ code: 'listener-changed-before-signal' });
    expect(await readRevision(f.port)).toBe('old-revision');
  });

  it('times out without SIGKILL or spawning a successor when SIGTERM close is slow', async () => {
    const f = await startedFixture('slow');
    await expect(restartOnePocListener({ port: f.port, expectedScript: fixture, timeoutMs: 100 }))
      .rejects.toMatchObject({ code: 'listener-close-timeout' });
    await new Promise(resolveWait => setTimeout(resolveWait, 350));
    expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
  });

  it('discovers an unreturned successor after a post-spawn identity refusal', async () => {
    const f = await startedFixture();
    let successorPid: number | undefined;
    await expect(restartOnePocListener({
      port: f.port, expectedScript: fixture, timeoutMs: 5000,
      inspect: port => {
        const current = inspectPocPort(port);
        if (current === null || current.pid === f.pid) return current;
        successorPid = current.pid;
        return { ...current, argv: [...current.argv, '--unexpected-successor-argument'] };
      },
    })).rejects.toMatchObject({ code: 'successor-identity-mismatch' });
    expect(successorPid).toBeDefined();
    expect(exactPrivateFixturePids()).toContain(successorPid);
  });

  it('reports a failed successor and lets a concurrent loser fail before signaling', async () => {
    const failed = await startedFixture();
    writeFileSync(join(failed.repo, 'fail-next'), 'yes');
    await expect(restartOnePocListener({ port: failed.port, expectedScript: fixture, timeoutMs: 3000 }))
      .rejects.toMatchObject({ code: 'successor-failed' });
    const concurrent = await startedFixture('held');
    writeFileSync(join(concurrent.repo, 'revision'), 'new-revision');
    const first = restartOnePocListener({ port: concurrent.port, expectedScript: fixture, timeoutMs: 10_000 })
      .then(result => ({ kind: 'succeeded' as const, result }), error => ({ kind: 'failed' as const, error }));
    let winner: Awaited<ReturnType<typeof restartOnePocListener>> | undefined;
    try {
      await waitForMarker(join(concurrent.repo, 'shutdown-started'));
      writeFileSync(join(concurrent.repo, 'hold-probe'), 'probe');
      await waitForMarker(join(concurrent.repo, 'hold-ack'));
      expect(await readRevision(concurrent.port)).toBe('old-revision');
      const second = await restartOnePocListener({ port: concurrent.port, expectedScript: fixture, timeoutMs: 5000 })
        .then(result => { pids.push(result.newPid); return { kind: 'succeeded' as const, result }; },
          error => ({ kind: 'refused' as const, error }));
      expect(second.kind).toBe('refused');
      if (second.kind === 'refused') expect(second.error).toMatchObject({ code: 'restart-already-in-progress' });
      expect(await readRevision(concurrent.port)).toBe('old-revision');
    } finally {
      writeFileSync(join(concurrent.repo, 'release-stop'), 'release');
      const outcome = await first;
      if (outcome.kind === 'failed') throw outcome.error;
      winner = outcome.result;
      pids.push(winner.newPid);
    }
    expect(winner.oldPid).toBe(concurrent.pid);
    expect(winner.newPid).not.toBe(concurrent.pid);
    expect(await readRevision(concurrent.port)).toBe('new-revision');
    expect(readdirSync(concurrent.stateDir)).toEqual(['machine-credential.token']);
  }, 20_000);
});
