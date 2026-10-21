import { createHash } from 'node:crypto';
import { existsSync, mkdtempSync, realpathSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { PassThrough, Writable } from 'node:stream';

import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import type { DaemonOptions, DaemonStart } from '@syzygy/cap1-daemon';
import { PocObservationError, type PocModel } from '@syzygy/three-surface-poc-core';

import type { GitObservation } from './git-observation.js';
import { pocObserverInputsAreClean } from './git-observation.js';
import { main, type PocIo, type PocMainDeps } from './main.js';

// syzygy-bpyt.5.5: `main(argv, io)` is the entry point; the script that
// `npm run poc` starts only supplies the real process as `io`. This is the
// one behavior gate: it drives main with fake io and fake collaborators
// (no repository is read, no socket is opened) and pins what the operator
// sees, the exit code, and the order in which the gate, the observation and
// the daemon are reached. Expected strings are literals.

const NOW = '2026-10-22T09:00:00.000Z';
const OBSERVER_ROOT = '/observer/syzygy';

let repoRoot: string;
let scratch: string;

beforeAll(() => {
  scratch = realpathSync(mkdtempSync(join(tmpdir(), 'poc-main-test-')));
  repoRoot = scratch;
});
afterAll(() => { rmSync(scratch, { recursive: true, force: true }); });

function sink(onText: (text: string) => void): Writable {
  return new Writable({ write(chunk, _encoding, callback) { onText(String(chunk)); callback(); } });
}

function fakeIo() {
  let stdout = '';
  let stderr = '';
  const listeners = new Map<string, () => void>();
  const stdin = new PassThrough();
  const io: PocIo = {
    stdout: sink((text) => { stdout += text; }),
    stderr: sink((text) => { stderr += text; }),
    stdin,
    cwd: () => OBSERVER_ROOT,
    now: () => NOW,
    onSignal: (signal, listener) => { listeners.set(signal, listener); },
  };
  return {
    io,
    stdin,
    out: () => stdout,
    err: () => stderr,
    registered: () => listeners.size,
    signal: (name: 'SIGINT' | 'SIGTERM') => listeners.get(name)?.(),
  };
}

function observation(revision: string, changedPaths: readonly string[] = []): GitObservation {
  return {
    revision,
    committerInstant: '2026-10-20T00:00:00+00:00',
    worktreeMetadataDigest: `tree-of-${revision}`,
    clean: changedPaths.length === 0,
    changedPaths,
  };
}

function lightModel(revision: string, readiness: unknown): PocModel {
  return {
    evaluation: { snapshot: `snap:${revision}`, asOf: NOW },
    project: { revision },
    workItems: { kind: 'observed', provenance: { kind: 'dolt-revision', source: 'Beads Dolt database (bu)', revision: `dolt:${revision}` } },
    walkthroughReadiness: readiness,
  } as unknown as PocModel;
}

const NOT_EVALUATED = { kind: 'not-evaluated' };
const EVALUATED = { kind: 'evaluated', readiness: { expected: { surfaceVersion: 'surface-version-literal', evaluationIdentity: 'evaluation-identity-literal' } } };

interface Harness {
  readonly deps: PocMainDeps;
  readonly calls: string[];
  readonly daemonOptions: () => DaemonOptions | undefined;
  readonly closes: () => number;
  /** Replaces what the observer checkout reports from the next read on. */
  readonly setObserver: (next: GitObservation) => void;
}

function harness(overrides: Partial<PocMainDeps> = {}, options: { observer?: GitObservation; readiness?: unknown; start?: DaemonStart } = {}): Harness {
  const calls: string[] = [];
  let daemonOptions: DaemonOptions | undefined;
  let closes = 0;
  let builds = 0;
  let observer = options.observer ?? observation('observer-rev');
  const deps: PocMainDeps = {
    resolveBinding: (locator) => { calls.push(`bind ${locator}`); return { kind: 'bound', locator, gitCommonDirectory: join(locator, '.git') }; },
    observeGitRepository: (root) => {
      calls.push(`observe ${root}`);
      return root === OBSERVER_ROOT ? observer : observation('butlers-rev');
    },
    observeGitHorizon: (root, pinned) => {
      calls.push(`horizon ${root} ${pinned}`);
      return { pinnedRevision: pinned, currentRevision: pinned, currentCommitterInstant: '2026-10-20T00:00:00+00:00', changedSources: 0, addedSources: 0 };
    },
    observeRevisionChange: () => ({ changedSources: 1, addedSources: 0 }),
    observeObservatoryDrift: (root, build) => {
      calls.push(`observatory ${root} ${build}`);
      return { buildRevision: build, currentRevision: build, commitsSinceBuild: 0 };
    },
    pocObserverInputsAreClean,
    buildProductionPocModel: (input) => {
      builds += 1;
      calls.push(`model ${builds} ${input.capture.repositoryRevision} ${input.repoRoot} ${input.observerRoot} ${input.capture.evidence.observationInstant}`);
      return lightModel(`${input.capture.repositoryRevision}-build-${builds}`, options.readiness ?? NOT_EVALUATED);
    },
    createDaemon: async (daemonStartOptions) => {
      daemonOptions = daemonStartOptions;
      calls.push('daemon');
      return options.start ?? {
        started: true,
        daemon: {
          host: '127.0.0.1',
          port: 7478,
          credentialPath: '/state/machine-credential.token',
          credentialProvision: 'minted',
          close: async () => { closes += 1; },
        },
      };
    },
    ...overrides,
  };
  return { deps, calls, daemonOptions: () => daemonOptions, closes: () => closes, setObserver: (next) => { observer = next; } };
}

async function started(run: Promise<number>, fake: ReturnType<typeof fakeIo>): Promise<void> {
  const first = await Promise.race([run.then(() => 'finished' as const), (async () => { while (fake.registered() < 2) await new Promise((resolve) => setTimeout(resolve, 5)); return 'serving' as const; })()]);
  expect(first).toBe('serving');
}

describe('main(argv, io): early exits', () => {
  it('prints the usage on --help and exits 0 without touching a collaborator', async () => {
    const fake = fakeIo();
    const h = harness();
    expect(await main(['--help'], fake.io, h.deps)).toBe(0);
    expect(fake.out()).toContain('Usage: npm run poc -- --repo <absolute-path-to-butlers> [options]');
    expect(fake.out()).toContain('--watch             re-observe each time Enter is pressed on this console, and only then');
    expect(fake.err()).toBe('');
    expect(h.calls).toEqual([]);
  });

  it('refuses an unknown argument with the usage on stderr and exits 1', async () => {
    const fake = fakeIo();
    const h = harness();
    expect(await main(['--frobnicate'], fake.io, h.deps)).toBe(1);
    expect(fake.out()).toBe('');
    expect(fake.err()).toMatch(/^syzygy POC: .+\n\nsyzygy three-surface POC \(local, non-release\)\n/);
    expect(h.calls).toEqual([]);
  });

  it('refuses a repository path that cannot be resolved before the gate is consulted', async () => {
    const fake = fakeIo();
    const h = harness();
    expect(await main(['--repo', join(scratch, 'does', 'not', 'exist')], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: configured repository is not readable\n');
    expect(h.calls).toEqual([]);
  });
});

describe('main(argv, io): the P1 authority gate', () => {
  it('a rejected binding exits 1 and reaches no observation, model, daemon or state directory', async () => {
    const fake = fakeIo();
    const stateDir = join(scratch, 'never-created-state');
    const h = harness({ resolveBinding: (locator) => { h.calls.push(`bind ${locator}`); return { kind: 'rejected', reason: 'locator-mismatched' }; } });
    expect(await main(['--repo', repoRoot, '--state-dir', stateDir], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: configured repository authority rejected (locator-mismatched)\n');
    expect(fake.out()).toBe('');
    expect(h.calls).toEqual([`bind ${repoRoot}`]);
    expect(existsSync(stateDir)).toBe(false);
  });

  it('the shipped collaborators reject a directory that is not the registered repository', async () => {
    const fake = fakeIo();
    expect(await main(['--repo', repoRoot], fake.io)).toBe(1);
    expect(fake.err()).toMatch(/^syzygy POC: configured repository authority rejected \((locator-mismatched|binding-unreadable)\)\n$/);
    expect(fake.out()).toBe('');
  });
});

describe('main(argv, io): startup refusals after the gate', () => {
  it('names a dirty observer checkout and starts no daemon', async () => {
    const fake = fakeIo();
    const h = harness({}, { observer: observation('observer-rev', ['apps/three-surface-poc/src/main.ts']) });
    expect(await main(['--repo', repoRoot], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: POC runtime inputs have uncommitted changes\n');
    expect(h.calls).toEqual([`bind ${repoRoot}`, `observe ${repoRoot}`, `observe ${OBSERVER_ROOT}`]);
  });

  it('names a git failure with its exit status, never its message', async () => {
    const fake = fakeIo();
    const h = harness({ observeGitRepository: () => { throw Object.assign(new Error('fatal: secret path'), { status: 128 }); } });
    expect(await main(['--repo', repoRoot], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: a required git revision could not be observed (git exit 128)\n');
  });

  it('lets a horizon failure at startup reject, as the script it replaced did', async () => {
    const fake = fakeIo();
    const h = harness({ observeGitHorizon: () => { throw new Error('horizon exploded'); } });
    await expect(main(['--repo', repoRoot], fake.io, h.deps)).rejects.toThrow('horizon exploded');
    expect(fake.err()).toBe('');
  });

  it('reports a model failure by its observation kind and exits 1', async () => {
    const fake = fakeIo();
    const h = harness({ buildProductionPocModel: () => { throw new PocObservationError('required-artifact-missing', 'a/b.md', 'gone'); } });
    expect(await main(['--repo', repoRoot], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: observation failed (required-artifact-missing): a/b.md: gone\n');
  });

  it('reports an unexpected failure by its class only', async () => {
    const fake = fakeIo();
    const h = harness({ buildProductionPocModel: () => { throw new TypeError('/private/path leaked'); } });
    expect(await main(['--repo', repoRoot], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: observation failed (unexpected observation failure (TypeError))\n');
  });

  it('reports a daemon that did not start with its named kind and exits 1', async () => {
    const fake = fakeIo();
    const h = harness({}, { start: { started: false, failure: { kind: 'duplicate-route', detail: 'two routes registered for `GET /polaris`' } } });
    expect(await main(['--repo', repoRoot], fake.io, h.deps)).toBe(1);
    expect(fake.err()).toBe('syzygy POC: daemon did not start (duplicate-route: two routes registered for `GET /polaris`)\n');
    expect(fake.out()).toBe('');
  });
});

describe('main(argv, io): serving', () => {
  it('prints the banner, registers the three route groups, and closes once on the first signal', async () => {
    const fake = fakeIo();
    const h = harness({}, { readiness: EVALUATED });
    const stateDir = join(scratch, 'state');
    const run = main(['--repo', repoRoot, '--state-dir', stateDir, '--port', '0'], fake.io, h.deps);
    await started(run, fake);

    expect(fake.out()).toBe([
      'Syzygy Three-Surface POC: http://127.0.0.1:7478/',
      `Observed repository: ${repoRoot}`,
      'Observed revision: butlers-rev',
      'Walkthrough surface version: surface-version-literal',
      'Walkthrough evaluation identity: evaluation-identity-literal',
      'Machine endpoint: http://127.0.0.1:7478/api/poc',
      'Machine credential (minted) at: /state/machine-credential.token',
      'Credential value is never printed. POC is local, experimental, and non-release.',
      '',
    ].join('\n'));
    expect(h.daemonOptions()?.stateDir).toBe(stateDir);
    expect(h.daemonOptions()?.port).toBe(0);
    const routes = (h.daemonOptions()?.routes ?? []).map((route) => `${route.method} ${route.path}`);
    for (const expected of ['GET /polaris', 'GET /trajectory', 'GET /orrery', 'GET /api/poc', 'POST /trajectory/materialize', 'POST /polaris/reobserve']) {
      expect(routes).toContain(expected);
    }
    expect(h.calls).toEqual([
      `bind ${repoRoot}`,
      `observe ${repoRoot}`,
      `observe ${OBSERVER_ROOT}`,
      `horizon ${repoRoot} butlers-rev`,
      `model 1 butlers-rev ${repoRoot} ${OBSERVER_ROOT} ${NOW}`,
      `observatory ${OBSERVER_ROOT} observer-rev`,
      'daemon',
    ]);

    fake.signal('SIGINT');
    expect(await run).toBe(0);
    fake.signal('SIGTERM');
    expect(h.closes()).toBe(1);
    expect(fake.out().endsWith('syzygy POC: SIGINT received, shutting down\n')).toBe(true);
    expect(fake.out().split('received, shutting down').length - 1).toBe(1);
    expect(fake.err()).toBe('');
  });

  it('prints no walkthrough binding while readiness is not evaluated', async () => {
    const fake = fakeIo();
    const h = harness();
    const run = main(['--repo', repoRoot, '--state-dir', join(scratch, 'state')], fake.io, h.deps);
    await started(run, fake);
    expect(fake.out()).not.toContain('Walkthrough');
    expect(h.daemonOptions()?.port).toBe(7478);
    fake.signal('SIGTERM');
    expect(await run).toBe(0);
    expect(fake.out().endsWith('syzygy POC: SIGTERM received, shutting down\n')).toBe(true);
  });

  it('defaults the state directory to a per-repository directory under the OS temp directory', async () => {
    const fake = fakeIo();
    const h = harness();
    const run = main(['--repo', repoRoot, '--port', '0'], fake.io, h.deps);
    await started(run, fake);
    const digest = createHash('sha256').update(repoRoot).digest('hex').slice(0, 16);
    expect(h.daemonOptions()?.stateDir).toBe(join(tmpdir(), 'syzygy-three-surface-poc', digest));
    fake.signal('SIGINT');
    await run;
  });

  it('attaches the Enter console to io only with --watch, and a dirty re-observation keeps the prior evaluation', async () => {
    const fake = fakeIo();
    const h = harness();
    const run = main(['--repo', repoRoot, '--state-dir', join(scratch, 'state'), '--port', '0', '--watch'], fake.io, h.deps);
    await started(run, fake);
    expect(fake.out()).toContain('Press Enter to re-observe. Nothing re-observes on its own;');
    const before = fake.out().length;
    // The next observer read reports a runtime input changed.
    h.setObserver(observation('observer-rev', ['packages/cap1-daemon/src/server.ts']));
    fake.stdin.write('\n');
    await new Promise((resolve) => setTimeout(resolve, 100));
    const added = fake.out().slice(before);
    expect(added).toContain('Re-observing…\n');
    expect(added).toContain('Re-observation unavailable: Unknown — POC runtime inputs are dirty; re-observation was refused. The prior complete evaluation remains served.\n');
    fake.signal('SIGINT');
    expect(await run).toBe(0);
  });

  it('prints no console prompt and ignores Enter without --watch', async () => {
    const fake = fakeIo();
    const h = harness();
    const run = main(['--repo', repoRoot, '--state-dir', join(scratch, 'state'), '--port', '0'], fake.io, h.deps);
    await started(run, fake);
    const before = fake.out();
    expect(before).not.toContain('Press Enter');
    fake.stdin.write('\n');
    await new Promise((resolve) => setTimeout(resolve, 50));
    expect(fake.out()).toBe(before);
    fake.signal('SIGINT');
    await run;
  });
});
