import { mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, relative, sep } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import type { EvaluationIdentity } from '@syzygy/cap1-core';

import { evaluateProject } from './pipeline.js';
import {
  createDaemon,
  minimalRootRoute,
  type Route,
  type RunningDaemon,
} from './server.js';

// RT3 — server tests over real sockets (port 0, 127.0.0.1) and real
// temp state dirs; no mocks. The load-bearing assertions:
//
// - admission runs BEFORE any machine-credentialed handler: a missing
//   or invalid credential gets the named refusal and the handler is
//   NEVER invoked (spy flag, not a mock);
// - refusal bodies are the core vocabulary verbatim — hard-coded
//   literal `{"admitted":false,"served":"nothing"}` (oracle
//   independence);
// - startup performs NO writes outside the state directory — judged by
//   a harness-external filesystem snapshot diff, never by the daemon's
//   own claims (the CAP1-REQ-023/053 oracle discipline applied to the
//   daemon's own boundary).

const cleanups: string[] = [];
const running: RunningDaemon[] = [];

function tempDir(prefix: string): string {
  const dir = mkdtempSync(join(tmpdir(), prefix));
  cleanups.push(dir);
  return dir;
}

afterEach(async () => {
  for (const daemon of running.splice(0)) {
    await daemon.close().catch(() => undefined);
  }
  for (const dir of cleanups.splice(0)) {
    rmSync(dir, { recursive: true, force: true });
  }
});

async function startDaemon(
  stateDir: string,
  routes: readonly Route[],
): Promise<RunningDaemon> {
  const start = await createDaemon({ stateDir, routes, port: 0 });
  if (!start.started) {
    throw new Error(`daemon failed to start: ${start.failure.kind}: ${start.failure.detail}`);
  }
  running.push(start.daemon);
  return start.daemon;
}

interface HandlerSpy {
  invoked: number;
  route: Route;
}

function machineRoute(path: string): HandlerSpy {
  const spy: HandlerSpy = {
    invoked: 0,
    route: {
      method: 'GET',
      path,
      credentialClass: 'machine-credentialed',
      handle() {
        spy.invoked += 1;
        return { status: 200, contentType: 'application/json', body: '{"served":"machine-facts"}' };
      },
    },
  };
  return spy;
}

/** Recursive file listing relative to `base` — the harness's own
 * external record of what exists, independent of the daemon. */
function snapshotFiles(base: string): readonly string[] {
  return readdirSync(base, { recursive: true, withFileTypes: false })
    .map((entry) => String(entry))
    .sort();
}

describe('RT3 — credential-classed admission at the transport', () => {
  it('a machine-credentialed route without a credential refuses, named, handler NOT invoked', async () => {
    const spy = machineRoute('/machine');
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), [spy.route]);

    const response = await fetch(`http://127.0.0.1:${daemon.port}/machine`);
    expect(response.status).toBe(401);
    // The named refusal, verbatim core vocabulary — hard-coded literal.
    expect(await response.json()).toEqual({ admitted: false, served: 'nothing' });
    expect(spy.invoked).toBe(0);
  });

  it('a wrong bearer token refuses, named, handler NOT invoked', async () => {
    const spy = machineRoute('/machine');
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), [spy.route]);

    const response = await fetch(`http://127.0.0.1:${daemon.port}/machine`, {
      headers: { authorization: `Bearer ${'f'.repeat(64)}` },
    });
    expect(response.status).toBe(401);
    expect(await response.json()).toEqual({ admitted: false, served: 'nothing' });
    expect(spy.invoked).toBe(0);
  });

  it('the correct bearer token (read from the credential file) admits and the handler runs', async () => {
    const spy = machineRoute('/machine');
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), [spy.route]);

    const token = readFileSync(daemon.credentialPath, 'utf8').trim();
    const response = await fetch(`http://127.0.0.1:${daemon.port}/machine`, {
      headers: { authorization: `Bearer ${token}` },
    });
    expect(response.status).toBe(200);
    expect(await response.json()).toEqual({ served: 'machine-facts' });
    expect(spy.invoked).toBe(1);
  });

  it('a human-open route serves without any credential', async () => {
    const route: Route = {
      method: 'GET',
      path: '/open',
      credentialClass: 'human-open',
      handle: () => ({ status: 200, contentType: 'text/plain', body: 'open' }),
    };
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), [route]);

    const response = await fetch(`http://127.0.0.1:${daemon.port}/open`);
    expect(response.status).toBe(200);
    expect(await response.text()).toBe('open');
  });

  it('an unknown route is an explicit named 404 body, never silence', async () => {
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), []);
    const response = await fetch(`http://127.0.0.1:${daemon.port}/nowhere`);
    expect(response.status).toBe(404);
    expect(await response.json()).toEqual({
      served: 'nothing',
      reason: 'unknown-route',
      method: 'GET',
      path: '/nowhere',
    });
  });

  it('binds 127.0.0.1 only', async () => {
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), []);
    expect(daemon.host).toBe('127.0.0.1');
    expect(daemon.port).toBeGreaterThan(0);
  });
});

describe('RT3 — credential stability across daemon restarts', () => {
  it('a restarted daemon reuses the same credential file and token', async () => {
    const stateDir = join(tempDir('rt3-srv-'), 'state');

    const first = await startDaemon(stateDir, []);
    expect(first.credentialProvision).toBe('minted');
    const token = readFileSync(first.credentialPath, 'utf8');
    await first.close();
    running.splice(running.indexOf(first), 1);

    const second = await startDaemon(stateDir, []);
    expect(second.credentialProvision).toBe('reused');
    expect(second.credentialPath).toBe(first.credentialPath);
    expect(readFileSync(second.credentialPath, 'utf8')).toBe(token);
  });
});

describe('RT3 — startup write boundary (harness-external snapshot diff)', () => {
  it('daemon startup writes nothing outside the state directory', async () => {
    // One base dir holds a real fixture repository AND the state dir's
    // parent, so the diff's denominator covers both planes.
    const base = tempDir('rt3-srv-writes-');
    const repoRoot = join(base, 'repo');
    mkdirSync(join(repoRoot, '.syzygy'), { recursive: true });
    writeFileSync(
      join(repoRoot, '.syzygy', 'project.yaml'),
      'schema_version: "1"\n',
      'utf8',
    );
    const stateDir = join(base, 'daemon-state');

    const before = snapshotFiles(base);
    const evaluation: EvaluationIdentity = {
      snapshot: 'snap-rt3-writes',
      asOf: '2026-08-22T11:00:00Z',
    };
    const projectEvaluation = await evaluateProject(repoRoot, { evaluation });
    const daemon = await startDaemon(stateDir, [minimalRootRoute(projectEvaluation)]);
    // Exercise the pipeline-backed root route before judging writes.
    const response = await fetch(`http://127.0.0.1:${daemon.port}/`);
    expect(response.status).toBe(200);
    const after = snapshotFiles(base);

    const beforeSet = new Set(before);
    const added = after.filter((path) => !beforeSet.has(path));
    // Every added path lies under the state dir; nothing was removed.
    const statePrefix = relative(base, stateDir);
    expect(added.length).toBeGreaterThan(0);
    for (const path of added) {
      expect(
        path === statePrefix || path.startsWith(statePrefix + sep),
        `unexpected write outside the state dir: ${path}`,
      ).toBe(true);
    }
    const afterSet = new Set(after);
    expect(before.filter((path) => !afterSet.has(path))).toEqual([]);
  });
});

describe('RT3 — the minimal root route', () => {
  it('serves a plain served-facts statement for an evaluated project', async () => {
    const root = tempDir('rt3-srv-root-');
    const decisionsDir = join(root, '.syzygy', 'governance', 'decisions');
    mkdirSync(decisionsDir, { recursive: true });
    writeFileSync(
      join(root, '.syzygy', 'project.yaml'),
      [
        'schema_version: "1"',
        'project:',
        '  id: prj-rt3-root',
        '  name: RT3 Root Fixture',
        'owner: test-owner@example.com',
        'repositories:',
        '  - id: repo-governance-root',
        '    role: governance-root',
        '    consent: consent-gov-root',
        'consents:',
        '  - consent-gov-root',
        'declarations:',
        '  spec_root: openspec/',
        'relations: []',
        'profiles: []',
        '',
      ].join('\n'),
      'utf8',
    );
    writeFileSync(
      join(decisionsDir, 'consent-gov-root.yaml'),
      [
        'id: consent-gov-root',
        'project: prj-rt3-root',
        'repository: repo-governance-root',
        'scope: full',
        'attribution: test-owner',
        'grant_state: in-force',
        '',
      ].join('\n'),
      'utf8',
    );

    const evaluation: EvaluationIdentity = {
      snapshot: 'snap-rt3-root',
      asOf: '2026-08-22T12:00:00Z',
    };
    const projectEvaluation = await evaluateProject(root, { evaluation });
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), [
      minimalRootRoute(projectEvaluation),
    ]);

    const response = await fetch(`http://127.0.0.1:${daemon.port}/`);
    expect(response.status).toBe(200);
    expect(response.headers.get('content-type')).toContain('text/plain');
    const body = await response.text();
    expect(body).toContain('selection: project:prj-rt3-root');
    expect(body).toContain('evaluation: snap-rt3-root@2026-08-22T12:00:00Z');
    expect(body).toContain('- Registered: satisfied [Observed]');
    expect(body).toContain(
      '- Mission-ready: not evaluated [Unknown]',
    );
  });

  it('states a missing declaration honestly, with its verbatim reason', async () => {
    const emptyRoot = tempDir('rt3-srv-empty-');
    const evaluation: EvaluationIdentity = {
      snapshot: 'snap-rt3-missing',
      asOf: '2026-08-22T12:30:00Z',
    };
    const projectEvaluation = await evaluateProject(emptyRoot, { evaluation });
    const daemon = await startDaemon(join(tempDir('rt3-srv-'), 'state'), [
      minimalRootRoute(projectEvaluation),
    ]);

    const body = await (await fetch(`http://127.0.0.1:${daemon.port}/`)).text();
    expect(body).toContain('declaration: Unknown (reason: missing-declaration)');
  });
});

describe('RT3 — startup failure arms are named', () => {
  it('two routes on one (method, path) refuse to start, named', async () => {
    const route: Route = {
      method: 'GET',
      path: '/dup',
      credentialClass: 'human-open',
      handle: () => ({ status: 200, contentType: 'text/plain', body: '' }),
    };
    const start = await createDaemon({
      stateDir: join(tempDir('rt3-srv-'), 'state'),
      routes: [route, { ...route }],
      port: 0,
    });
    expect(start.started).toBe(false);
    if (!start.started) {
      expect(start.failure.kind).toBe('duplicate-route');
    }
  });

  it('an unprovisionable credential refuses to start, named', async () => {
    const stateDir = tempDir('rt3-srv-');
    writeFileSync(join(stateDir, 'machine-credential.token'), '', 'utf8');
    const start = await createDaemon({ stateDir, routes: [], port: 0 });
    expect(start.started).toBe(false);
    if (!start.started) {
      expect(start.failure.kind).toBe('credential-unprovisionable');
    }
  });
});
