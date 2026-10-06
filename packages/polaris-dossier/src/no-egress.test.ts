import { spawnSync } from 'node:child_process';
import * as fs from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { build } from 'esbuild';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { FULL_RUN_ROOT_ENV, REAL_ROOT, makeClone } from './full-run.testkit.js';

/** The no-egress proof (REQ-polaris-generation-033, scenario "No provider call and no egress record"; tasks "Prove no provider call and no
 * transmission"; syzygy-qkea.11). A full fixture run, every dossier command from preflight to close and status, runs in a child process
 * under strace, which records every network-class system call of that process and of every process it starts. The capture is the
 * operating system's account, not the run record. The run must create no Internet-family socket at all (AF_INET, AF_INET6), so it can
 * have resolved no name, called no provider and transmitted nothing off the host. A canary run that sends one loopback datagram first
 * shows the capture sees a transmission when one is made. Without strace, or where the host forbids tracing, the proof is skipped and
 * says so: it is never reported as passed. */

const STRACE = spawnSync('strace', ['-V'], { encoding: 'utf8' });
const HAVE_STRACE = STRACE.status === 0;
const INTERNET_FAMILY = /\bAF_INET6?\b/u;

let dir: string;
let bundle: string;
let clone: string;
let commit: string;
beforeAll(async () => {
  if (!HAVE_STRACE) return;
  dir = fs.realpathSync(fs.mkdtempSync(path.join(tmpdir(), 'dossier-no-egress-')));
  ({ clone, commit } = makeClone(path.join(dir, 'repo')));
  bundle = path.join(dir, 'driver.mjs');
  const src = (relative: string): string => path.join(REAL_ROOT, relative);
  await build({
    entryPoints: [path.join(REAL_ROOT, 'packages/polaris-dossier/test-support/no-egress-driver.ts')],
    bundle: true, platform: 'node', format: 'esm', target: 'node22', outfile: bundle, logLevel: 'silent',
    banner: { js: 'import { createRequire as __createRequire } from \'node:module\'; const require = __createRequire(import.meta.url);' },
    alias: {
      '@syzygy/polaris-generation-core': src('packages/polaris-generation-core/src/index.ts'),
      '@syzygy/polaris-generation-consent': src('packages/polaris-generation-consent/src/index.ts'),
      '@syzygy/polaris-dossier': src('packages/polaris-dossier/src/index.ts'),
      '@syzygy/cap1-core': src('packages/cap1-core/src/index.ts'),
      '@syzygy/cap1-daemon': src('packages/cap1-daemon/src/index.ts'),
      '@syzygy/three-surface-poc-core': src('packages/three-surface-poc-core/src/index.ts'),
    },
  });
}, 120_000);
afterAll(() => { if (dir !== undefined) fs.rmSync(dir, { recursive: true, force: true }); });

interface Capture { readonly status: number | null; readonly stdout: string; readonly stderr: string; readonly calls: readonly string[]; readonly tasks: number }

/** Run the driver under strace; every network-class call of the process tree, one per line, and how many tasks (processes and threads) made one. */
function captured(name: string, canary: boolean): Capture {
  const log = path.join(dir, `${name}.strace`);
  const stateRoot = path.join(dir, `${name}-state`);
  const result = spawnSync('strace', ['-f', '-qq', '-e', 'trace=%network,execve,clone,clone3,fork,vfork', '-e', 'signal=none', '-o', log, process.execPath, bundle, clone, commit, stateRoot, ...(canary ? ['canary'] : [])], {
    encoding: 'utf8', env: { PATH: process.env['PATH'] ?? '/usr/bin:/bin', HOME: dir, [FULL_RUN_ROOT_ENV]: REAL_ROOT }, timeout: 240_000,
  });
  const lines = fs.existsSync(log) ? fs.readFileSync(log, 'utf8').split('\n').filter((line) => line !== '') : [];
  const call = (line: string): string => line.replace(/^\d+\s+/u, '');
  const network = lines.map(call).filter((line) => !/^(execve|clone3?|v?fork)\(/u.test(line) && /^[a-z_0-9]+\(/u.test(line));
  return { status: result.status, stdout: result.stdout, stderr: result.stderr, calls: network, tasks: new Set(lines.map((line) => line.split(/\s+/u)[0])).size };
}

describe.skipIf(!HAVE_STRACE)('no provider call and no transmission (S10): an operating-system capture of a full fixture run', () => {
  it('creates no Internet-family socket over the whole run, from preflight to close', () => {
    const run = captured('run', false);
    expect(run.stderr).toBe('');
    expect(run.status).toBe(0);
    const summary = JSON.parse(run.stdout) as { run: string; steps: { command: string; exit: number }[] };
    expect(summary.steps.map((step) => step.command)).toEqual([
      'preflight', 'init', 'brief', 'check', 'session-prompt', 'inventory-check', 'launch-form', 'session-prompt', 'review-check', 'launch-form',
      'render', 'session-prompt', 'review-check', 'launch-form', 'render', 'close', 'status',
    ]);
    expect(summary.steps.every((step) => step.exit === 0)).toBe(true);
    expect(fs.existsSync(path.join(summary.run, 'record.json'))).toBe(true);
    expect(run.tasks).toBeGreaterThan(0);
    // The population: every network-class call the capture recorded, which is not empty (the runtime's own local sockets are in it).
    // None names an Internet address family.
    expect(run.calls.length).toBeGreaterThan(0);
    expect(run.calls.filter((line) => INTERNET_FAMILY.test(line))).toEqual([]);
    // One line in the test log saying the proof ran, and over what population.
    console.log(`no-egress proof ran under strace: ${run.calls.length} network-class calls, traced calls from ${run.tasks} task(s), 0 Internet-family`);
  }, 240_000);

  it('sees the canary: one loopback datagram sent before the same run is in the capture', () => {
    const run = captured('canary', true);
    expect(run.status).toBe(0);
    const internet = run.calls.filter((line) => INTERNET_FAMILY.test(line));
    expect(internet.some((line) => line.startsWith('socket(AF_INET'))).toBe(true);
    expect(internet.some((line) => /^(sendto|sendmsg)\(.*inet_addr\("127\.0\.0\.1"\)/u.test(line))).toBe(true);
  }, 240_000);
});

// Under CI the proof is required: node-ci installs strace, so its absence there is a failure, never a skip.
const IN_CI = process.env['CI'] === 'true';
describe.skipIf(HAVE_STRACE)('no provider call and no transmission (S10), without strace', () => {
  if (IN_CI) it('is required under CI, where strace is installed: its absence fails the proof', () => { expect.fail('strace is unavailable under CI=true, so the no-egress proof did not run'); });
  else it.skip('is not proved on this host: strace is unavailable, so the capture is skipped, never reported as passed', () => {});
});
