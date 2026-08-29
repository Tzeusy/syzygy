import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { createDaemon, type RunningDaemon } from '@syzygy/cap1-daemon';
import { buildButlersPocModel, type PocModel } from '@syzygy/three-surface-poc-core';

import { POC_MACHINE_PATH, pocRoutes, renderPocPage } from './routes.js';

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

function modelFixture(): PocModel {
  const repoRoot = tempDir('syzygy-poc-route-butlers-');
  const files: Readonly<Record<string, string>> = {
    'docs/superpowers/specs/2026-08-24-whatsapp-identity-reconciliation-design.md':
      '# design\nStatus: Approved for implementation\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/proposal.md':
      '# proposal\n- Sign-off: owner approved the design and end-to-end implementation on 2026-08-24.\n',
    'openspec/changes/repair-whatsapp-identity-reconciliation/specs/switchboard-identity/spec.md':
      '# REQ-switchboard-identity-001\nwhatsapp_user_client -> whatsapp_jid\n',
    'src/butlers/identity.py': 'def canonical_identity(): pass\n',
    'tests/core/test_identity.py': 'def test_identity(): pass\n',
  };
  for (const [relativePath, contents] of Object.entries(files)) {
    const absolutePath = join(repoRoot, relativePath);
    mkdirSync(dirname(absolutePath), { recursive: true });
    writeFileSync(absolutePath, contents, 'utf8');
  }
  return buildButlersPocModel({
    repoRoot,
    repositoryRevision: 'c13894238989d3bebb24094730992970b31fe546',
    observerRevision: 'bfdb7963e4ff5628d0d1ec0f59e831d7e8209abe',
    evaluation: { snapshot: 'butlers@c1389423', asOf: '2026-08-29T12:00:00Z' },
  });
}

function idsFromHtml(html: string, attribute: string): string[] {
  return [...html.matchAll(new RegExp(`(?:\\s|<)${attribute}="([^"]+)"`, 'g'))]
    .map((match) => match[1])
    .filter((value): value is string => value !== undefined);
}

function parityTuples(model: PocModel): string[] {
  return [
    ...model.entities.map((entity) =>
      JSON.stringify([
        'entity',
        entity.id,
        entity.kind,
        entity.title,
        entity.detail,
        entity.epistemic,
        entity.provenance,
      ]),
    ),
    ...model.relationships.map((relationship) =>
      JSON.stringify([
        'relationship',
        relationship.id,
        relationship.kind,
        relationship.from,
        relationship.to,
        relationship.statement,
        relationship.epistemic,
        relationship.provenance,
      ]),
    ),
  ].sort();
}

async function startPoc(model: PocModel): Promise<{
  readonly daemon: RunningDaemon;
  readonly token: string;
}> {
  const start = await createDaemon({
    stateDir: join(tempDir('syzygy-poc-route-state-'), 'state'),
    routes: pocRoutes(() => model),
    port: 0,
  });
  if (!start.started) {
    throw new Error(`daemon failed to start: ${start.failure.kind}`);
  }
  running.push(start.daemon);
  return {
    daemon: start.daemon,
    token: readFileSync(start.daemon.credentialPath, 'utf8').trim(),
  };
}

describe('three-surface POC routes', () => {
  it('serves one model through human and authenticated machine views', async () => {
    const model = modelFixture();
    const { daemon, token } = await startPoc(model);
    const baseUrl = `http://${daemon.host}:${daemon.port}`;

    const humanResponse = await fetch(`${baseUrl}/`);
    expect(humanResponse.status).toBe(200);
    expect(humanResponse.headers.get('content-type')).toBe('text/html; charset=utf-8');
    const html = await humanResponse.text();
    expect(html).toContain('<h2>Polaris</h2>');
    expect(html).toContain('<h2>Trajectory</h2>');
    expect(html).toContain('<h2>Orrery</h2>');
    expect(html).toContain('No POC work item has been materialized.');
    expect(html).toContain('No test artifact has been captured for this evaluation.');
    expect(html).toContain('No current runtime observation was supplied.');

    expect(new Set(idsFromHtml(html, 'data-entity-id'))).toEqual(
      new Set(model.entities.map((entity) => entity.id)),
    );
    expect(new Set(idsFromHtml(html, 'data-relationship-id'))).toEqual(
      new Set(model.relationships.map((relationship) => relationship.id)),
    );
    const targetIds = new Set(idsFromHtml(html, 'id'));
    for (const href of idsFromHtml(html, 'href')) {
      if (href.startsWith('#')) {
        expect(targetIds.has(href.slice(1))).toBe(true);
      }
    }

    const sameOrigin = await fetch(`${baseUrl}/`, { headers: { origin: baseUrl } });
    expect(sameOrigin.status).toBe(200);
    const rebound = await fetch(`${baseUrl}/`, {
      headers: {
        host: 'poc.attacker.invalid',
        origin: 'http://poc.attacker.invalid',
      },
    });
    expect(rebound.status).toBe(403);
    expect(await rebound.json()).toEqual({
      served: 'nothing',
      reason: 'browser-origin-refused',
    });

    const refused = await fetch(`${baseUrl}${POC_MACHINE_PATH}`);
    expect(refused.status).toBe(401);
    expect(await refused.json()).toEqual({ admitted: false, served: 'nothing' });

    const machineResponse = await fetch(`${baseUrl}${POC_MACHINE_PATH}`, {
      headers: { authorization: `Bearer ${token}` },
    });
    expect(machineResponse.status).toBe(200);
    expect(machineResponse.headers.get('content-type')).toBe('application/json');
    const wireModel = (await machineResponse.json()) as PocModel;
    expect(wireModel).toEqual(model);
    const humanTuples = idsFromHtml(html, 'data-parity-tuple')
      .map((tuple) => decodeURIComponent(tuple))
      .sort();
    expect(humanTuples).toEqual(parityTuples(wireModel));
  });

  it('escapes observed text before rendering it into HTML', () => {
    const model = modelFixture();
    const injected: PocModel = {
      ...model,
      entities: model.entities.map((entity, index) =>
        index === 0
          ? { ...entity, title: '<script>alert("title")</script>', detail: '<img src=x>' }
          : entity,
      ),
    };

    const html = renderPocPage(injected);
    expect(html).not.toContain('<script>alert("title")</script>');
    expect(html).not.toContain('<img src=x>');
    expect(html).toContain('&lt;script&gt;alert(&quot;title&quot;)&lt;/script&gt;');
    expect(html).toContain('&lt;img src=x&gt;');
  });
});
