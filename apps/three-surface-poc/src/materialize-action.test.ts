import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { createDaemon, type RunningDaemon } from '@syzygy/cap1-daemon';
import { readMaterializationRecordFile } from '@syzygy/three-surface-poc-core';

import {
  MATERIALIZE_HUMAN_PATH,
  materializeRoutes,
  renderMaterializePanel,
} from './materialize-action.js';
import { pocRoutes } from './routes.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { renderTrajectoryPage } from './trajectory.js';

const cleanups: string[] = [];
const running: RunningDaemon[] = [];

afterEach(async () => {
  for (const daemon of running.splice(0)) {
    await daemon.close().catch(() => undefined);
  }
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function tempDir(prefix: string): string {
  const directory = mkdtempSync(join(tmpdir(), prefix));
  cleanups.push(directory);
  return directory;
}

describe('renderMaterializePanel', () => {
  it('previews the exact packet and target repository read-only, before any trigger (AC1)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderMaterializePanel(model);
    expect(html).toContain('data-parity-field="materialize-target-repo"');
    expect(html).toContain(model.project.root);
    expect(html).toContain('REQ-switchboard-identity-001');
    expect(html).toContain('data-parity-field="materialize-status">Not yet materialized.');
    expect(html).toContain('<form method="POST" action="/trajectory/materialize">');
    expect(html).not.toMatch(/onclick=/);
  });

  it('is embedded on the Trajectory page', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderTrajectoryPage(model);
    expect(html).toContain('data-materialize-panel');
  });
});

describe('materializeRoutes', () => {
  async function startDaemon(options: {
    readonly stateDir: string;
    readonly onMaterialized?: () => void;
    readonly runQuery?: (repoRoot: string, sql: string) => string;
    readonly runCreate?: (repoRoot: string, packet: unknown, attribution: string) => string;
  }) {
    let model = buildFixtureModel(cleanups);
    const targetRepoRoot = model.project.root;
    const start = await createDaemon({
      stateDir: join(tempDir('syzygy-poc-materialize-daemon-'), 'state'),
      port: 0,
      routes: [
        ...pocRoutes(() => model),
        ...materializeRoutes({
          getModel: () => model,
          targetRepoRoot,
          stateDir: () => options.stateDir,
          onMaterialized: () => {
            options.onMaterialized?.();
          },
          ...(options.runQuery === undefined ? {} : { runQuery: options.runQuery }),
          ...(options.runCreate === undefined ? {} : { runCreate: options.runCreate }),
        }),
      ],
    });
    if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
    running.push(start.daemon);
    return `http://${start.daemon.host}:${start.daemon.port}`;
  }

  it('refuses a cross-origin POST the same way every other human route does (fail-closed)', async () => {
    const baseUrl = await startDaemon({
      stateDir: tempDir('syzygy-poc-materialize-state-'),
    });
    const response = await fetch(`${baseUrl}${MATERIALIZE_HUMAN_PATH}`, {
      method: 'POST',
      headers: { host: 'poc.attacker.invalid', origin: 'http://poc.attacker.invalid' },
    });
    expect(response.status).toBe(403);
  });

  it('creates exactly one Bead on trigger, persists the record, and calls onMaterialized (AC2)', async () => {
    const dir = tempDir('syzygy-poc-materialize-state-');
    let refreshed = 0;
    let createCalls = 0;
    const baseUrl = await startDaemon({
      stateDir: dir,
      onMaterialized: () => {
        refreshed += 1;
      },
      runQuery: (_repoRoot, sql) =>
        sql.includes('external_ref') ? JSON.stringify([]) : JSON.stringify([{ revision: 'dolt-rev-http' }]),
      runCreate: () => {
        createCalls += 1;
        return JSON.stringify({ id: 'bu-http-materialized1' });
      },
    });

    const response = await fetch(`${baseUrl}${MATERIALIZE_HUMAN_PATH}`, { method: 'POST' });
    expect(response.status).toBe(200);
    const html = await response.text();
    expect(html).toContain('bu-http-materialized1');
    expect(createCalls).toBe(1);
    expect(refreshed).toBe(1);
    expect(readMaterializationRecordFile(dir)?.beadId).toBe('bu-http-materialized1');
  });

  it('is idempotent over HTTP: a second POST reuses the same Bead without a second create (AC3)', async () => {
    const dir = tempDir('syzygy-poc-materialize-state-');
    let createCalls = 0;
    const baseUrl = await startDaemon({
      stateDir: dir,
      runQuery: (_repoRoot, sql) =>
        sql.includes('external_ref') ? JSON.stringify([]) : JSON.stringify([{ revision: 'dolt-rev-http' }]),
      runCreate: () => {
        createCalls += 1;
        return JSON.stringify({ id: 'bu-http-materialized1' });
      },
    });

    const first = await fetch(`${baseUrl}${MATERIALIZE_HUMAN_PATH}`, { method: 'POST' });
    const second = await fetch(`${baseUrl}${MATERIALIZE_HUMAN_PATH}`, { method: 'POST' });
    expect(first.status).toBe(200);
    expect(second.status).toBe(200);
    const secondHtml = await second.text();
    expect(secondHtml).toContain('Reused');
    expect(secondHtml).toContain('bu-http-materialized1');
    expect(createCalls).toBe(1);
  });

  it('renders a named failure over HTTP and leaves no partial record when bd is missing (AC5)', async () => {
    const dir = tempDir('syzygy-poc-materialize-state-');
    const baseUrl = await startDaemon({
      stateDir: dir,
      runQuery: () => {
        const error = new Error('spawn bd ENOENT') as NodeJS.ErrnoException;
        error.code = 'ENOENT';
        throw error;
      },
    });

    const response = await fetch(`${baseUrl}${MATERIALIZE_HUMAN_PATH}`, { method: 'POST' });
    expect(response.status).toBe(502);
    const html = await response.text();
    expect(html).toContain('bd CLI is not available');
    expect(readMaterializationRecordFile(dir)).toBeNull();
  });

  it('states the Bead exists when it was created but only the local record write failed, instead of the generic no-Bead suffix (AC5)', async () => {
    // A regular file at the state-dir path makes writeMaterializationRecordFile's
    // mkdirSync throw, simulating "the Bead mutation succeeded, only persisting
    // the local record failed" without needing to fake the filesystem module.
    const parent = tempDir('syzygy-poc-materialize-state-');
    const dir = join(parent, 'not-a-directory');
    writeFileSync(dir, 'occupied');

    const baseUrl = await startDaemon({
      stateDir: dir,
      runQuery: (_repoRoot, sql) =>
        sql.includes('external_ref') ? JSON.stringify([]) : JSON.stringify([{ revision: 'dolt-rev-http' }]),
      runCreate: () => JSON.stringify({ id: 'bu-http-created-unpersisted' }),
    });

    const response = await fetch(`${baseUrl}${MATERIALIZE_HUMAN_PATH}`, { method: 'POST' });
    expect(response.status).toBe(502);
    const html = await response.text();
    expect(html).toContain('bu-http-created-unpersisted');
    expect(html).toContain('exists in the configured Butlers repository');
    expect(html).not.toContain('No Bead was left in a partially-created state');
  });
});
