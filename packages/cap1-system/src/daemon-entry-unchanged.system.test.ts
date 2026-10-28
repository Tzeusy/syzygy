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
import { mkdirSync, mkdtempSync, readFileSync, readdirSync, realpathSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import * as path from 'node:path';
import { pathToFileURL } from 'node:url';
import ts from 'typescript';
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

// No invocation runSync makes may start a daemon. If one wrongly does, SYZYGY_PORT=0 keeps it off the default port 7477 and the
// timeout ends it, so the row fails instead of blocking the worker: spawnSync is synchronous, so the suite's own timeout cannot
// fire (syzygy-bpyt.4.22). SIGKILL, because the daemon handles SIGTERM as a graceful shutdown. The governed-plane row runs
// without the variable, as captured: it is the one row that reaches port resolution with no --port, so it pins that the
// default resolves to a valid port. A regression that wrongly admitted that argv could hold 7477 until the timeout.
const RUN_SYNC_TIMEOUT_MS = 20_000;

function runSync(args: readonly string[], cwd: string, portEnv: Record<string, string> = { SYZYGY_PORT: '0' }): { status: number | null; stdout: string; stderr: string } {
  const result = spawnSync(process.execPath, [ENTRY, ...args], {
    cwd, env: { ...ENV, ...portEnv }, encoding: 'utf8', timeout: RUN_SYNC_TIMEOUT_MS, killSignal: 'SIGKILL',
  });
  if (result.error) throw new Error(`${JSON.stringify(args)}: ${result.error.message} (timeout ${RUN_SYNC_TIMEOUT_MS} ms)`);
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
    expect(runSync(['--root', root, '--state-dir', path.join(root, '.syzygy', 'x')], dir, {})).toEqual({
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

  // syzygy-qkea.10: the composition root injects the multi-page dossier
  // renderer into `render`, importing the POC app only on this branch. A
  // missing run is refused at the run, which `render` reaches only once a
  // renderer is wired (with none it refuses at stage `renderer` first).
  it('`dossier render <missing>` reaches the run with the renderer injected, and starts no daemon', () => {
    const { base: dir } = base();
    const before = sweep(dir);
    const result = runSync(['dossier', 'render', path.join(dir, 'absent'), '--json'], dir);
    expect(result.status).toBe(1);
    expect(JSON.parse(result.stdout)).toMatchObject({ command: 'render', outcome: 'refused', stage: 'run' });
    expect(result.stderr).not.toContain('syzygy daemon');
    expect(sweep(dir)).toEqual(before);
  });

  // A load hook preloaded into the built entry logs every module it loads from the POC app. The daemon path, served and
  // shut down, asked for its usage and refused an argument, logs none; `dossier render`, which injects the renderer, logs
  // the renderer's module, so the hook does see the POC app when it loads. This pins behavior, not where main.ts spells
  // its imports (syzygy-bpyt.4.5).
  it('the daemon path never loads the POC app, and the `dossier render` branch does', async () => {
    const { base: dir, root } = base();
    const stateDir = path.join(dir, 'state'), log = path.join(dir, 'poc-loads.txt'), hook = path.join(dir, 'poc-load-hook.mjs');
    const app = `${pathToFileURL(realpathSync(path.join(REPO_ROOT, 'apps', 'three-surface-poc'))).href}/`;
    writeFileSync(log, '');
    writeFileSync(hook, [
      "import { appendFileSync } from 'node:fs';",
      "import { registerHooks } from 'node:module';",
      'registerHooks({ load(url, context, nextLoad) {',
      '  if (url.startsWith(process.env.POC_APP_URL)) appendFileSync(process.env.POC_LOAD_LOG, `${url}\\n`);',
      '  return nextLoad(url, context);',
      '} });',
    ].join('\n'));
    const hooked = { NODE_OPTIONS: `--import=${pathToFileURL(hook).href}`, POC_APP_URL: app, POC_LOAD_LOG: log };
    const served = await runDaemon(['--root', root, '--state-dir', stateDir, '--port', '0'], dir, hooked, stateDir);
    expect(served).toMatchObject({ exit: 0, rootStatus: 200, stderr: '' });
    expect(runSync(['--help'], dir, { SYZYGY_PORT: '0', ...hooked })).toMatchObject({ status: 0, stderr: '' });
    expect(runSync(['--bogus'], dir, { SYZYGY_PORT: '0', ...hooked })).toMatchObject({ status: 1 });
    expect(readFileSync(log, 'utf8')).toBe('');
    const rendered = runSync(['dossier', 'render', path.join(dir, 'absent'), '--json'], dir, { SYZYGY_PORT: '0', ...hooked });
    expect(JSON.parse(rendered.stdout)).toMatchObject({ command: 'render', outcome: 'refused', stage: 'run' });
    expect(readFileSync(log, 'utf8').split('\n')).toContain(`${app}dist/polaris-generation/dossier-site.js`);
  });

  // The kept part of the old text pin. A load the row above never reaches (on a start failure, in main()'s close-failure
  // callback, at a request-time entry read, or behind a variable or a runtime hook the row does not set) shows only in the
  // text, and only in main.ts: a load in http-host's close-failure branch reaches neither row. The branches are found
  // by syntax, so a close that shares its line, sits at another indentation or carries an `else` cannot widen them: each is
  // the one `if` in main(), or in an else chain there, on `argv[0] === 'dossier'` or `'polaris'`. An else would run on every
  // other argv, so the only one allowed is the other branch. Both end before the daemon path, and every mention of the POC
  // app in main.ts lies inside one of their blocks.
  it('every mention of the POC app in main.ts lies inside the `dossier` or the `polaris` branch, whose only else is the other, before the daemon path', () => {
    const text = readFileSync(path.join(REPO_ROOT, 'apps/syzygy/src/main.ts'), 'utf8');
    const source = ts.createSourceFile('main.ts', text, ts.ScriptTarget.Latest, true);
    const main = source.statements.find((statement): statement is ts.FunctionDeclaration => ts.isFunctionDeclaration(statement) && statement.name?.text === 'main');
    const body = main?.body?.statements ?? [];
    const chain = (statement: ts.Statement): ts.IfStatement[] =>
      ts.isIfStatement(statement) ? [statement, ...(statement.elseStatement === undefined ? [] : chain(statement.elseStatement))] : [];
    const ifs = body.flatMap(chain);
    const found = ['dossier', 'polaris'].map((name) => ifs.filter((statement) => statement.expression.getText(source) === `argv[0] === '${name}'`));
    expect(found.map((branches) => branches.length)).toEqual([1, 1]);
    const branches = found.map((matches) => matches[0]!);
    const daemon = body.find((statement) => statement.getText(source).startsWith('let parsed = parseCli('));
    expect(daemon).toBeDefined();
    for (const branch of branches) {
      expect(branch.elseStatement === undefined || branches.includes(branch.elseStatement as ts.IfStatement)).toBe(true);
      expect(branch.getEnd()).toBeLessThanOrEqual(daemon!.getStart(source));
    }
    const blocks = branches.map((branch) => [branch.thenStatement.getStart(source), branch.thenStatement.getEnd()] as const);
    const mentions: number[] = [];
    for (let at = text.indexOf('three-surface-poc-app'); at !== -1; at = text.indexOf('three-surface-poc-app', at + 1)) mentions.push(at);
    expect(mentions.length).toBeGreaterThan(0);
    const lineAt = (at: number): string => text.slice(text.lastIndexOf('\n', at) + 1, text.indexOf('\n', at));
    expect(mentions.filter((at) => !blocks.some(([start, end]) => at > start && at < end)).map(lineAt)).toEqual([]);
  });

  // Restored from the base byte for byte (syzygy-bpyt.4.5, round 3's stopping rule). The two rows above pass a then-block
  // that loads the POC app and then falls through, re-enters main(), breaks out of a label or schedules a callback
  // (rev-532c's Y1-Y5); this pin fails each, since each adds a line naming the app. Its known false refusals, which the
  // rows above pass: a comment naming the app in the dossier branch, the renderer bound under another name, the two
  // branches swapped, the dossier import in a nested function and the polaris import in a nested try.
  // The `polaris` branch (prototype, POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14) injects the same renderer the same way.
  it('the daemon path never loads the POC app: each import is dynamic and inside the `dossier` or `polaris` branch', () => {
    const main = readFileSync(path.join(REPO_ROOT, 'apps/syzygy/src/main.ts'), 'utf8');
    const line = "    const { renderLocalDossier } = await import('@syzygy/three-surface-poc-app/dossier-site');";
    const mentions = main.split('\n').filter((text) => text.includes('three-surface-poc-app'));
    expect(mentions).toEqual([line, line]);
    const daemon = main.indexOf('let parsed = parseCli(');
    const first = main.indexOf(line), second = main.indexOf(line, first + 1);
    const dossier = main.indexOf("if (argv[0] === 'dossier') {"), polaris = main.indexOf("if (argv[0] === 'polaris') {");
    expect(dossier).toBeGreaterThan(-1);
    expect(polaris).toBeGreaterThan(dossier);
    expect(first).toBeGreaterThan(dossier);
    expect(first).toBeLessThan(polaris);
    expect(second).toBeGreaterThan(polaris);
    expect(second).toBeLessThan(daemon);
  });
});
