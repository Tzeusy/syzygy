import { spawnSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { authorRule, awaitRule } from './broker.js';
import { isLaunchedRun, launchFormRefusal, writeLaunchedMarker } from './launched.js';
import { bwrapArgs, viewFor, viewSha256, type ViewRole } from './session-view.js';

// Candidate REQ-polaris-generation-041/042 (prototype under POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14): each launched session reaches
// only what its role needs; the broker admits only the session's own commands; launch forms follow the run's kind.

const hasBwrap = spawnSync('bwrap', ['--ro-bind', '/', '/', '--', '/bin/true']).status === 0;

describe('session views', () => {
  let base: string;
  const dirs: Record<string, string> = {};
  beforeAll(() => {
    base = fs.mkdtempSync(path.join(os.tmpdir(), 'polaris-view-'));
    for (const name of ['clone', 'checkout', 'run', 'run/drafts', 'run.sessions/session-1', 'run.sessions/fidelity-1', 'run.sessions/design-1', 'home-author', 'home-inventory', 'home-fidelity', 'shim', 'sock']) {
      dirs[name] = path.join(base, name);
      fs.mkdirSync(dirs[name]!, { recursive: true });
    }
    fs.writeFileSync(path.join(dirs['clone']!, 'README.md'), 'clone');
    fs.writeFileSync(path.join(dirs['run']!, 'brief.md'), 'brief');
    fs.writeFileSync(path.join(dirs['run.sessions/fidelity-1']!, 'packet.json'), '{}');
  });
  afterAll(() => fs.rmSync(base, { recursive: true, force: true }));

  const inputs = (role: ViewRole) => ({
    role, clone: dirs['clone']!, runDir: dirs['run']!, sessionDir: role === 'author' ? dirs['run']! : role === 'inventory' ? dirs['run.sessions/session-1']! : dirs[`run.sessions/${role}-1`]!,
    agentHome: dirs[`home-${role === 'design' ? 'fidelity' : role}`]!, checkout: dirs['checkout']!, toolPaths: [], shimDir: dirs['shim']!, brokerSocket: path.join(dirs['sock']!, 'b.sock'), socketDir: dirs['sock']!,
  });

  /** Run a probe script in the role's view: one line per path, `r` readable, `w` writable, `-` absent. */
  const probe = (role: ViewRole, paths: readonly string[]): string[] => {
    const script = paths.map((p) => `if [ -e '${p}' ]; then if touch '${p}/.w' 2>/dev/null || { [ -f '${p}' ] && [ -w '${p}' ] && echo >> '${p}' 2>/dev/null; }; then echo w; else echo r; fi; else echo -; fi`).join('; ');
    const result = spawnSync('bwrap', [...bwrapArgs(viewFor(inputs(role))), '/bin/sh', '-c', script], { encoding: 'utf8' });
    expect(result.status, result.stderr).toBe(0);
    return result.stdout.trim().split('\n');
  };

  it.skipIf(!hasBwrap)('the inventory session sees the clone read-only and its own directory, never the run or another session', () => {
    expect(probe('inventory', [dirs['clone']!, dirs['run.sessions/session-1']!, dirs['run']!, path.join(dirs['run']!, 'brief.md'), dirs['run.sessions/fidelity-1']!, dirs['checkout']!]))
      .toEqual(['r', 'w', '-', '-', '-', 'r']);
  });

  it.skipIf(!hasBwrap)('a review session sees only its own directory and the checkout read-only', () => {
    expect(probe('fidelity', [dirs['run.sessions/fidelity-1']!, dirs['clone']!, dirs['run']!, dirs['run.sessions/session-1']!, dirs['run.sessions/design-1']!, dirs['checkout']!]))
      .toEqual(['w', '-', '-', '-', '-', 'r']);
  });

  it.skipIf(!hasBwrap)('the author writes only drafts/ and sees no helper session', () => {
    expect(probe('author', [dirs['run/drafts']!, dirs['run']!, dirs['clone']!, dirs['run.sessions/session-1']!, dirs['run.sessions/fidelity-1']!, dirs['checkout']!]))
      .toEqual(['w', 'r', 'r', '-', '-', 'r']);
  });

  it('a view is a pure function of its inputs, and its digest changes with them', () => {
    expect(viewSha256(viewFor(inputs('inventory')))).toBe(viewSha256(viewFor(inputs('inventory'))));
    expect(viewSha256(viewFor(inputs('inventory')))).not.toBe(viewSha256(viewFor(inputs('fidelity'))));
  });

  it('a view passes no environment but its own', () => {
    const args = bwrapArgs(viewFor(inputs('inventory')));
    expect(args).toContain('--clearenv');
    const set = args.flatMap((arg, i) => (arg === '--setenv' ? [args[i + 1]] : []));
    expect(set.sort()).toEqual(['CLAUDE_CONFIG_DIR', 'HOME', 'LANG', 'PATH', 'SYZYGY_BROKER_SOCKET', 'TERM']);
  });
});

describe('broker rules', () => {
  it('a helper may run only await on its own directory', () => {
    const rule = awaitRule('/s/run-x.sessions/session-1');
    expect(rule(['dossier', 'await', '/s/run-x.sessions/session-1/'])).toBeNull();
    expect(rule(['dossier', 'await', '/s/run-x.sessions/session-1/', '--submit', 'inventory.json', '--stdin'])).toBeNull();
    expect(rule(['dossier', 'await', '/s/run-x.sessions/fidelity-1/'])).not.toBeNull();
    expect(rule(['dossier', 'check', '/s/run-x'])).not.toBeNull();
    expect(rule(['dossier', 'await'])).not.toBeNull();
  });

  it('the author may run only check and status on its own run', () => {
    const rule = authorRule('/s/run-x');
    expect(rule(['dossier', 'check', '/s/run-x'])).toBeNull();
    expect(rule(['dossier', '--json', 'status', '/s/run-x'])).toBeNull();
    expect(rule(['dossier', 'check', '/s/run-y'])).not.toBeNull();
    for (const command of ['session-prompt', 'review-check', 'inventory-check', 'render', 'close', 'launch-form', 'allow-execution', 'await']) {
      expect(rule(['dossier', command, '/s/run-x'])).not.toBeNull();
    }
  });
});

describe('launch forms by kind of run', () => {
  let run: string;
  beforeAll(() => { run = fs.mkdtempSync(path.join(os.tmpdir(), 'polaris-launched-')); });
  afterAll(() => fs.rmSync(run, { recursive: true, force: true }));

  it('an operator-started run counts terminal and bang, never syzygy-launched', () => {
    expect(isLaunchedRun(run)).toBe(false);
    expect(launchFormRefusal(run, { value: 'terminal', declaredBy: 'operator', label: 'Inferred' })).toBeNull();
    expect(launchFormRefusal(run, { value: 'syzygy-launched', declaredBy: 'syzygy', label: 'Observed' })).not.toBeNull();
  });

  it('a launched run counts syzygy-launched, never a declared form', () => {
    writeLaunchedMarker(run, 'run-x', Date.now());
    expect(isLaunchedRun(run)).toBe(true);
    expect(launchFormRefusal(run, { value: 'syzygy-launched', declaredBy: 'syzygy', label: 'Observed' })).toBeNull();
    expect(launchFormRefusal(run, { value: 'terminal', declaredBy: 'operator', label: 'Inferred' })).not.toBeNull();
    expect(launchFormRefusal(run, { value: 'syzygy-launched', declaredBy: 'operator', label: 'Inferred' })).not.toBeNull();
  });
});
