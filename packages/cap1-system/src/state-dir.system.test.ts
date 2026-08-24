// RT9 repair test (RTF-1) — the state-dir governed-plane startup check
// judged by SYMLINK REALITY, observed externally. The lexical check
// alone let an operator-supplied symlink (`ln -s <root>/.syzygy/x
// /tmp/sd; --state-dir /tmp/sd`) pass and land the credential write
// inside the governed plane via the link. Oracle here is external:
// the spawned process's exit code and stderr, plus the harness's own
// filesystem sweep of the fixture's governed tree — never the
// daemon's self-report.

import { spawn } from 'node:child_process';
import { chmodSync, existsSync, mkdirSync, rmSync, symlinkSync } from 'node:fs';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  daemonEntry,
  REPO_ROOT,
  snapshotTree,
  startDaemon,
  tempBase,
  writeCompleteFixture,
} from './harness.js';

const cleanups: (() => Promise<void> | void)[] = [];

afterEach(async () => {
  for (const cleanup of cleanups.splice(0).reverse()) {
    await cleanup();
  }
});

/** Spawn the built daemon and await exit: code, stdout, stderr. */
function runDaemonToExit(args: readonly string[]): Promise<{
  code: number | null;
  stdout: string;
  stderr: string;
}> {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [daemonEntry(REPO_ROOT), ...args], {
      stdio: ['ignore', 'pipe', 'pipe'],
    });
    let out = '';
    let err = '';
    child.stdout?.setEncoding('utf8');
    child.stderr?.setEncoding('utf8');
    child.stdout?.on('data', (chunk: string) => {
      out += chunk;
    });
    child.stderr?.on('data', (chunk: string) => {
      err += chunk;
    });
    const deadline = setTimeout(() => {
      child.kill('SIGKILL');
      reject(new Error(`daemon did not exit in time.\nstdout:\n${out}\nstderr:\n${err}`));
    }, 30_000);
    child.once('exit', (code) => {
      clearTimeout(deadline);
      resolve({ code, stdout: out, stderr: err });
    });
  });
}

function expectTreeUnchanged(
  before: ReturnType<typeof snapshotTree>,
  after: ReturnType<typeof snapshotTree>,
): void {
  const additions = [...after.keys()].filter((key) => !before.has(key));
  expect(additions).toEqual([]);
  const deletions = [...before.keys()].filter((key) => !after.has(key));
  expect(deletions).toEqual([]);
  const modified = [...before].flatMap(([key, record]) => {
    const afterRecord = after.get(key);
    return afterRecord === undefined ||
      afterRecord.sha256 !== record.sha256 ||
      afterRecord.mtimeMs !== record.mtimeMs
      ? [key]
      : [];
  });
  expect(modified).toEqual([]);
  expect(after.size).toBe(before.size);
}

describe('RTF-1 — state-dir governed-plane check resolves symlink reality', () => {
  it('refuses (nonzero exit, named refusal) a --state-dir symlink whose REAL target lies inside .syzygy/, and writes nothing there', async () => {
    const base = tempBase('syz-sys-sd-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);

    // The attack from the finding: a symlink OUTSIDE the fixture whose
    // real target is a directory INSIDE the fixture's .syzygy/. The
    // lexical path (base/sd) is outside the governed plane; only
    // symlink reality reveals the real landing spot.
    const governedTarget = join(fixtureRoot, '.syzygy', 'sneaky-state');
    mkdirSync(governedTarget, { recursive: true });
    const linkPath = join(base, 'sd');
    symlinkSync(governedTarget, linkPath);

    // BEFORE: the harness's own external record of the governed tree.
    const before = snapshotTree(join(fixtureRoot, '.syzygy'));
    expect(before.size).toBeGreaterThan(0);

    const result = await runDaemonToExit([
      '--root',
      fixtureRoot,
      '--state-dir',
      linkPath,
      '--port',
      '0',
    ]);

    // The process EXITS nonzero with the named refusal on stderr,
    // mentioning the REAL location inside the governed plane.
    expect(result.code).not.toBe(0);
    expect(result.code).toBe(1);
    expect(result.stderr).toContain('inside the governed plane');
    expect(result.stderr).toContain(governedTarget);
    // It never announced an address — it refused before serving.
    expect(result.stdout).not.toContain('listening at');

    // AFTER (harness-external): nothing was written inside .syzygy/ —
    // no additions, no deletions, no modifications, full denominator.
    const after = snapshotTree(join(fixtureRoot, '.syzygy'));
    expectTreeUnchanged(before, after);
  });

  it('refuses a dangling --state-dir symlink whose intended target lies inside .syzygy/, before writes or a listener', async () => {
    const base = tempBase('syz-sys-sd-dangling-in-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);

    const governedTarget = join(fixtureRoot, '.syzygy', 'not-created-state');
    const linkPath = join(base, 'state-link');
    symlinkSync(governedTarget, linkPath);
    expect(existsSync(governedTarget)).toBe(false);
    const before = snapshotTree(join(fixtureRoot, '.syzygy'));

    const result = await runDaemonToExit([
      '--root',
      fixtureRoot,
      '--state-dir',
      linkPath,
      '--port',
      '0',
    ]);

    expect(result.code).toBe(1);
    expect(result.stderr).toContain('inside the governed plane');
    expect(result.stderr).toContain(governedTarget);
    expect(result.stdout).not.toContain('listening at');
    expect(existsSync(governedTarget)).toBe(false);
    expectTreeUnchanged(before, snapshotTree(join(fixtureRoot, '.syzygy')));
  });

  it('still starts and serves through a --state-dir symlink whose real target is OUTSIDE the governed plane', async () => {
    const base = tempBase('syz-sys-sd-ok-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);

    // A legitimate symlinked state dir: real target is a benign temp
    // directory outside the fixture entirely.
    const benignTarget = join(base, 'real-state');
    mkdirSync(benignTarget, { recursive: true });
    const linkPath = join(base, 'state-link');
    symlinkSync(benignTarget, linkPath);

    const daemon = await startDaemon({ fixtureRoot, stateDir: linkPath });
    cleanups.push(async () => {
      await daemon.stop();
    });

    // It serves: the human page answers 200.
    expect((await fetch(`${daemon.baseUrl}/`)).status).toBe(200);
    expect(await daemon.stop()).toBe(0);
  });

  it('keeps a dangling benign outside target credential-unprovisionable, with no listener or writes', async () => {
    const base = tempBase('syz-sys-sd-dangling-out-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);

    const benignTarget = join(base, 'not-created', 'state');
    const linkPath = join(base, 'state-link');
    symlinkSync(benignTarget, linkPath);
    const before = snapshotTree(base);

    const result = await runDaemonToExit([
      '--root',
      fixtureRoot,
      '--state-dir',
      linkPath,
      '--port',
      '0',
    ]);

    expect(result.code).toBe(1);
    expect(result.stderr).toContain('credential-unprovisionable');
    expect(result.stderr).not.toContain('inside the governed plane');
    expect(result.stdout).not.toContain('listening at');
    expect(existsSync(benignTarget)).toBe(false);
    expectTreeUnchanged(before, snapshotTree(base));
  });

  it('rejects a state-dir symlink loop as named invalid before writes or a listener', async () => {
    const base = tempBase('syz-sys-sd-loop-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);
    const first = join(base, 'state-a');
    const second = join(base, 'state-b');
    symlinkSync(second, first);
    symlinkSync(first, second);
    const before = snapshotTree(base);

    const result = await runDaemonToExit([
      '--root',
      fixtureRoot,
      '--state-dir',
      first,
      '--port',
      '0',
    ]);

    expect(result.code).toBe(1);
    expect(result.stderr).toContain('symlink-loop');
    expect(result.stdout).not.toContain('listening at');
    expectTreeUnchanged(before, snapshotTree(base));
  });

  it('rejects an unreadable state-dir path as named invalid before writes or a listener', async () => {
    const base = tempBase('syz-sys-sd-unreadable-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);
    const blocked = join(base, 'blocked');
    mkdirSync(blocked, { mode: 0o700 });
    const stateDir = join(blocked, 'state');
    chmodSync(blocked, 0o000);
    cleanups.push(() => chmodSync(blocked, 0o700));
    const before = snapshotTree(base);

    const result = await runDaemonToExit([
      '--root',
      fixtureRoot,
      '--state-dir',
      stateDir,
      '--port',
      '0',
    ]);

    expect(result.code).toBe(1);
    expect(result.stderr).toContain('path-unreadable');
    expect(result.stdout).not.toContain('listening at');
    expectTreeUnchanged(before, snapshotTree(base));
  });
});
