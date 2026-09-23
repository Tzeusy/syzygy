import { spawn } from 'node:child_process';
import { createServer } from 'node:net';
import { mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { inspectPocPort, listenerPidFromSs, restartOnePocListener, RestartRefusal, type PocListener } from './restart.js';

const fixture = resolve('apps/three-surface-poc/src/test-fixtures/restart-listener.mjs');
const roots: string[] = [];
const pids: number[] = [];

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

async function startedFixture(slow = false): Promise<{ root: string; repo: string; stateDir: string; port: number; pid: number }> {
  const root = scratch();
  const repo = join(root, 'repo');
  const stateDir = join(root, 'state');
  mkdirSync(repo);
  writeFileSync(join(repo, 'revision'), 'old-revision');
  if (slow) writeFileSync(join(repo, 'slow-stop'), 'yes');
  const port = await freePort();
  const child = spawn(process.execPath, [fixture, '--repo', repo, '--state-dir', stateDir, '--port', String(port)], {
    cwd: process.cwd(), stdio: 'ignore',
  });
  if (child.pid === undefined) throw new Error('fixture process missing');
  pids.push(child.pid);
  expect(await readRevision(port)).toBe('old-revision');
  return { root, repo, stateDir, port, pid: child.pid };
}

afterEach(async () => {
  for (const pid of pids.splice(0)) {
    try { process.kill(pid, 'SIGTERM'); } catch { /* already stopped */ }
  }
  await new Promise(resolveWait => setTimeout(resolveWait, 300));
  for (const root of roots.splice(0)) rmSync(root, { recursive: true, force: true });
});

describe('one-listener POC restart on private fixture sockets', () => {
  it('waits through one vanished post-SIGTERM identity, then starts exactly one successor after socket absence', async () => {
    const f = await startedFixture(true);
    const credentialBefore = readFileSync(join(f.stateDir, 'machine-credential.token'));
    writeFileSync(join(f.repo, 'revision'), 'new-revision');
    expect(await readRevision(f.port)).toBe('old-revision');
    let inspections = 0;
    const result = await restartOnePocListener({
      port: f.port, expectedScript: fixture, timeoutMs: 5000,
      inspect: port => {
        inspections += 1;
        if (inspections === 3) throw new RestartRefusal('listener-identity-unreadable');
        return inspectPocPort(port);
      },
    });
    pids.push(result.newPid);
    expect(inspections).toBeGreaterThan(3);
    expect(result.oldPid).toBe(f.pid);
    expect(result.newPid).not.toBe(f.pid);
    expect(await readRevision(f.port)).toBe('new-revision');
    expect(readFileSync(join(f.stateDir, 'machine-credential.token'))).toEqual(credentialBefore);
    expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
  }, 15_000);

  it('refuses an unreadable identity before SIGTERM and leaves the old listener serving', async () => {
    const f = await startedFixture();
    let inspections = 0;
    await expect(restartOnePocListener({
      port: f.port, expectedScript: fixture, timeoutMs: 1000,
      inspect: port => {
        inspections += 1;
        if (inspections === 2) throw new RestartRefusal('listener-identity-unreadable');
        return inspectPocPort(port);
      },
    })).rejects.toMatchObject({ code: 'listener-identity-unreadable' });
    expect(inspections).toBe(2);
    expect(await readRevision(f.port)).toBe('old-revision');
  });

  it('times out with no successor while post-SIGTERM identity stays unreadable', async () => {
    const f = await startedFixture();
    let inspections = 0;
    await expect(restartOnePocListener({
      port: f.port, expectedScript: fixture, timeoutMs: 150,
      inspect: port => {
        inspections += 1;
        if (inspections > 2) throw new RestartRefusal('listener-identity-unreadable');
        return inspectPocPort(port);
      },
    })).rejects.toMatchObject({ code: 'listener-close-timeout' });
    expect(inspections).toBeGreaterThan(2);
    await expect(fetch(`http://127.0.0.1:${f.port}/`)).rejects.toThrow();
    expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
  });

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
    const f = await startedFixture(true);
    await expect(restartOnePocListener({ port: f.port, expectedScript: fixture, timeoutMs: 100 }))
      .rejects.toMatchObject({ code: 'listener-close-timeout' });
    await new Promise(resolveWait => setTimeout(resolveWait, 350));
    expect(readdirSync(f.stateDir)).toEqual(['machine-credential.token']);
  });

  it('reports a failed successor and lets a concurrent loser fail before signaling', async () => {
    const failed = await startedFixture();
    writeFileSync(join(failed.repo, 'fail-next'), 'yes');
    await expect(restartOnePocListener({ port: failed.port, expectedScript: fixture, timeoutMs: 3000 }))
      .rejects.toMatchObject({ code: 'successor-failed' });
    const concurrent = await startedFixture(true);
    const first = restartOnePocListener({ port: concurrent.port, expectedScript: fixture, timeoutMs: 5000 });
    await new Promise(resolveWait => setTimeout(resolveWait, 25));
    await expect(restartOnePocListener({ port: concurrent.port, expectedScript: fixture, timeoutMs: 5000 }))
      .rejects.toMatchObject({ code: 'restart-already-in-progress' });
    const winner = await first;
    pids.push(winner.newPid);
    expect(await readRevision(concurrent.port)).toBe('old-revision');
    expect(readdirSync(concurrent.stateDir)).toEqual(['machine-credential.token']);
  }, 20_000);
});
