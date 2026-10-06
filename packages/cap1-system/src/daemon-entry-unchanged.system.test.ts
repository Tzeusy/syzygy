// The daemon entry is unchanged by the `syzygy dossier` dispatch
// (syzygy-qkea.2, polaris-dossier S1). apps/syzygy/src/main.ts gained one
// guard: an exact first argument `dossier` hands argv to the dossier
// command family. Every other invocation must behave byte-for-byte as it
// did before that guard existed.
//
// The expected values below are literals captured from the BUILT entry at
// 55daf6ceafe9e3622653beb4110284729e82d911, the commit before the guard,
// by a capture script run outside this repository against that build; the
// PR that added this file shows the script and its output. Nothing here is
// computed by the code under test. Masking replaces only the bound port,
// the temporary base directory and the state directory.
//
// The one input whose behaviour changed is disclosed and asserted at the
// end: `syzygy dossier …` used to be refused as "unknown argument:
// dossier" (exit 1) and now reaches the dossier family.

import { spawn, spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readdirSync, realpathSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { REPO_ROOT, daemonEntry } from './harness.js';

const ENTRY = daemonEntry(REPO_ROOT);
const ENV = Object.fromEntries(Object.entries(process.env).filter(([key]) => !key.startsWith('SYZYGY_')));

const USAGE = `syzygy — Capability 1 local daemon

Usage: node apps/syzygy/dist/main.js [options]

Options:
  --root <dir>        observed repository root (env SYZYGY_OBSERVED_ROOT; default: cwd)
  --state-dir <dir>   daemon state directory (env SYZYGY_STATE_DIR;
                      default: <root>/.syzygy-daemon-state);
                      refused if inside <root>/openspec or <root>/.syzygy
  --port <n>          TCP port, 0 for ephemeral (env SYZYGY_PORT; default: 7477)
  --help              print this usage and exit
`;

const STARTUP = (root: string): string => `syzygy daemon listening at http://127.0.0.1:<PORT>/
observed root: ${root}
machine credential (minted) at: <STATE>/machine-credential.token
the credential value is never printed; read the file to authenticate machine requests.
syzygy daemon: SIGINT received, shutting down
`;

const cleanups: (() => void)[] = [];
afterEach(() => {
  for (const cleanup of cleanups.splice(0).reverse()) cleanup();
});

/** The capture's fixture: a root with a README and empty governed directories. */
function base(): { base: string; root: string } {
  const dir = realpathSync(mkdtempSync(path.join(tmpdir(), 'syz-entry-')));
  cleanups.push(() => rmSync(dir, { recursive: true, force: true }));
  const root = path.join(dir, 'root');
  mkdirSync(path.join(root, '.syzygy', 'governance', 'decisions'), { recursive: true });
  mkdirSync(path.join(root, '.syzygy', 'intent'), { recursive: true });
  mkdirSync(path.join(root, 'openspec'), { recursive: true });
  writeFileSync(path.join(root, 'README.md'), '# fixture readme\n');
  return { base: dir, root };
}

function sweep(dir: string, from = dir): string[] {
  return readdirSync(dir).sort().flatMap((name) => {
    const full = path.join(dir, name);
    const stats = statSync(full);
    const line = `${stats.isDirectory() ? 'd' : 'f'} ${(stats.mode & 0o777).toString(8)} ${path.relative(from, full)}`;
    return stats.isDirectory() ? [line, ...sweep(full, from)] : [line];
  });
}

function runSync(args: readonly string[], cwd: string): { status: number | null; stdout: string; stderr: string } {
  const result = spawnSync(process.execPath, [ENTRY, ...args], { cwd, env: ENV, encoding: 'utf8' });
  const mask = (text: string): string => text.split(cwd).join('<BASE>');
  return { status: result.status, stdout: mask(result.stdout), stderr: mask(result.stderr) };
}

async function runDaemon(args: readonly string[], cwd: string, env: Record<string, string>, stateDir: string): Promise<{
  exit: number | null; rootStatus: number; stdout: string; stderr: string; stateWhileRunning: string[]; stateAfterExit: string[];
}> {
  const child = spawn(process.execPath, [ENTRY, ...args], { cwd, env: { ...ENV, ...env }, stdio: ['ignore', 'pipe', 'pipe'] });
  let out = '';
  let err = '';
  child.stdout.setEncoding('utf8').on('data', (chunk: string) => { out += chunk; });
  child.stderr.setEncoding('utf8').on('data', (chunk: string) => { err += chunk; });
  const exited = new Promise<number | null>((resolve) => child.once('exit', resolve));
  const deadline = Date.now() + 30_000;
  let port: string | undefined;
  while ((port = /listening at http:\/\/127\.0\.0\.1:(\d+)\//.exec(out)?.[1]) === undefined) {
    if (Date.now() > deadline) {
      child.kill('SIGKILL');
      throw new Error(`daemon did not announce its address.\nstdout:\n${out}\nstderr:\n${err}`);
    }
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
  const rootStatus = (await fetch(`http://127.0.0.1:${port}/`)).status;
  const stateWhileRunning = sweep(stateDir);
  child.kill('SIGINT');
  const exit = await exited;
  const mask = (text: string): string => text.split(stateDir).join('<STATE>').replace(/127\.0\.0\.1:\d+/g, '127.0.0.1:<PORT>');
  return { exit, rootStatus, stdout: mask(out), stderr: mask(err), stateWhileRunning, stateAfterExit: sweep(stateDir) };
}

describe('daemon entry: every invocation but `dossier` is unchanged', () => {
  it.each([[['--help']], [['-h']], [['--help', 'dossier']]])('%j prints the usage and exits 0', (args) => {
    const { base: dir } = base();
    expect(runSync(args, dir)).toEqual({ status: 0, stdout: USAGE, stderr: '' });
  });

  it.each([
    [['--bogus'], 'unknown argument: --bogus'],
    [['--port', '0', 'dossier'], 'unknown argument: dossier'],
    [['Dossier'], 'unknown argument: Dossier'],
    [['--port'], '--port requires a value'],
    [['--port', '70000'], 'port must be an integer in [0, 65535]; got `70000`'],
  ])('%j is refused with exit 1 and the same message', (args, detail) => {
    const { base: dir } = base();
    expect(runSync(args, dir)).toEqual({ status: 1, stdout: '', stderr: `syzygy daemon: ${detail}\n\n${USAGE}` });
  });

  it('a state directory inside the governed plane is refused with the same message', () => {
    const { base: dir, root } = base();
    expect(runSync(['--root', root, '--state-dir', path.join(root, '.syzygy', 'x')], dir)).toEqual({
      status: 1,
      stdout: '',
      stderr: `syzygy daemon: state directory <BASE>/root/.syzygy/x lies inside the governed plane (<BASE>/root/.syzygy); choose a location outside openspec/ and .syzygy/\n\n${USAGE}`,
    });
  });

  it('with no arguments it serves from the working directory, writes the same state and shuts down the same way', async () => {
    const { root } = base();
    const result = await runDaemon([], root, { SYZYGY_PORT: '0' }, path.join(root, '.syzygy-daemon-state'));
    expect(result).toEqual({
      exit: 0,
      rootStatus: 200,
      stdout: STARTUP(root),
      stderr: '',
      stateWhileRunning: ['f 600 machine-credential.token'],
      stateAfterExit: ['f 600 machine-credential.token'],
    });
  });

  it('with explicit flags it serves, writes the same state and shuts down the same way', async () => {
    const { base: dir, root } = base();
    const stateDir = path.join(dir, 'state');
    const result = await runDaemon(['--root', root, '--state-dir', stateDir, '--port', '0'], dir, {}, stateDir);
    expect(result).toEqual({
      exit: 0,
      rootStatus: 200,
      stdout: STARTUP(root),
      stderr: '',
      stateWhileRunning: ['f 600 machine-credential.token'],
      stateAfterExit: ['f 600 machine-credential.token'],
    });
  });
});

describe('daemon entry: the one changed input, `dossier` as the first argument', () => {
  // Before: `syzygy daemon: unknown argument: dossier` and the daemon usage,
  // exit 1. After: the dossier family, which starts no daemon and writes
  // nothing in the working directory.
  it('`dossier` alone is a dossier usage error (exit 2), not the daemon\'s refusal', () => {
    const { base: dir } = base();
    const before = sweep(dir);
    const result = runSync(['dossier'], dir);
    expect(result.status).toBe(2);
    expect(result.stdout).toBe('');
    expect(result.stderr.startsWith('syzygy dossier: a command is required\n\nsyzygy dossier — operator-agent dossier runs\n')).toBe(true);
    expect(result.stderr).not.toContain('syzygy daemon');
    expect(sweep(dir)).toEqual(before);
  });

  it('`dossier status <missing>` is a dossier refusal (exit 1) and starts no daemon', () => {
    const { base: dir } = base();
    const before = sweep(dir);
    const result = runSync(['dossier', 'status', path.join(dir, 'absent')], dir);
    expect(result).toEqual({
      status: 1,
      stdout: '',
      stderr: 'command: status\noutcome: refused\nreason: run directory <BASE>/absent cannot be read (ENOENT)\n',
    });
    expect(sweep(dir)).toEqual(before);
  });
});
