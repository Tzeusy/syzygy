import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, statSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { createDaemon, type RunningDaemon } from '@syzygy/cap1-daemon';
import { BUTLERS_POC_SEEDS, buildPocModel, buildResponseIdentity, type PocModel } from '@syzygy/three-surface-poc-core';

import { POC_MACHINE_PATH, pocRoutes, renderPocPage } from './routes.js';
import { ADMITTING_AUTHORITY, projectShapeFixtureGit } from './test-project-shape-fixture.js';
import { buildFixtureModel } from './test-model-fixture.js';

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
  return buildPocModel({
    seeds: BUTLERS_POC_SEEDS,
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

function decodeHtmlText(text: string): string {
  return text
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>')
    .replaceAll('&quot;', '"')
    .replaceAll('&#39;', "'")
    .replaceAll('&amp;', '&');
}

function visibleField(row: string, field: string): string {
  const match = new RegExp(`data-parity-field="${field}"[^>]*>([^<]*)</`).exec(row);
  if (match?.[1] === undefined) {
    throw new Error(`visible parity field missing: ${field}`);
  }
  return decodeHtmlText(match[1]);
}

function visibleProvenance(row: string): PocModel['entities'][number]['provenance'] {
  return [...row.matchAll(/<li data-parity-provenance>([\s\S]*?)<\/li>/g)].map(
    (match) => {
      const item = match[1] ?? '';
      const digestMatch = /data-parity-field="provenance-digest">([^<]*)</.exec(item);
      return {
        kind: visibleField(item, 'provenance-kind') as
          | 'repository-file'
          | 'git-revision'
          | 'manual-mapping',
        source: visibleField(item, 'provenance-source'),
        revision: visibleField(item, 'provenance-revision'),
        ...(digestMatch?.[1] === undefined
          ? {}
          : { digest: decodeHtmlText(digestMatch[1]) }),
      };
    },
  );
}

function visibleEpistemic(row: string): PocModel['entities'][number]['epistemic'] {
  const label = visibleField(row, 'epistemic-label');
  const explanation = visibleField(row, 'epistemic-explanation');
  return label === 'Observed'
    ? { label: 'Observed', basis: explanation }
    : { label: 'Unknown', reason: explanation };
}

function visibleParityTuples(html: string): string[] {
  const entityRows = [
    ...html.matchAll(/<tr[^>]*data-entity-id="[^"]+"[^>]*>([\s\S]*?)<\/tr>/g),
  ].map((match) => {
    const row = match[1] ?? '';
    return JSON.stringify([
      'entity',
      visibleField(row, 'entity-id'),
      visibleField(row, 'entity-kind'),
      visibleField(row, 'entity-title'),
      visibleField(row, 'entity-detail'),
      visibleEpistemic(row),
      visibleProvenance(row),
    ]);
  });
  const relationshipRows = [
    ...html.matchAll(
      /<tr[^>]*data-relationship-id="[^"]+"[^>]*>([\s\S]*?)<\/tr>/g,
    ),
  ].map((match) => {
    const row = match[1] ?? '';
    return JSON.stringify([
      'relationship',
      visibleField(row, 'relationship-id'),
      visibleField(row, 'relationship-kind'),
      visibleField(row, 'relationship-from'),
      visibleField(row, 'relationship-to'),
      visibleField(row, 'relationship-statement'),
      visibleEpistemic(row),
      visibleProvenance(row),
    ]);
  });
  return [...entityRows, ...relationshipRows].sort();
}

// Independent wire oracle for responseIdentity: deliberately separate from
// the core walker's path grammar and canonicalJson implementation.
function independentCanonicalJson(value: unknown): string {
  const canonicalize = (candidate: unknown): unknown => {
    if (Array.isArray(candidate)) return candidate.map(canonicalize);
    if (candidate !== null && typeof candidate === 'object') {
      const record = candidate as Record<string, unknown>;
      return Object.fromEntries(
        Object.keys(record)
          .filter((key) => record[key] !== undefined)
          .sort()
          .map((key) => [key, canonicalize(record[key])]),
      );
    }
    return candidate;
  };
  return JSON.stringify(canonicalize(value));
}

function independentDeletePath(root: Record<string, unknown>, path: string): boolean {
  const segments = path.split('.').map((raw) => ({
    key: raw.endsWith('[]') ? raw.slice(0, -2) : raw,
    all: raw.endsWith('[]'),
  }));
  const remove = (value: unknown, index: number): boolean => {
    if (value === null || typeof value !== 'object' || Array.isArray(value)) return false;
    const record = value as Record<string, unknown>;
    const segment = segments[index];
    if (segment === undefined || !(segment.key in record)) return false;
    if (index === segments.length - 1) {
      delete record[segment.key];
      return true;
    }
    const child = record[segment.key];
    if (segment.all) {
      if (!Array.isArray(child)) throw new Error(`independent path ${path} expected an array`);
      return child.reduce((found, member) => remove(member, index + 1) || found, false);
    }
    return remove(child, index + 1);
  };
  return remove(root, 0);
}

function independentResponseKey(body: Record<string, unknown>): string {
  const identity = body.responseIdentity as { contentKey?: string; readonly excludes: readonly string[] };
  delete identity.contentKey;
  for (const path of identity.excludes) independentDeletePath(body, path);
  return `sha256:${createHash('sha256').update(independentCanonicalJson(body)).digest('hex')}`;
}

async function startPoc(model: PocModel): Promise<{
  readonly daemon: RunningDaemon;
  readonly token: string;
  readonly stateDir: string;
}> {
  const stateDir = join(tempDir('syzygy-poc-route-state-'), 'state');
  const start = await createDaemon({
    stateDir,
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
    stateDir,
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
    expect(wireModel.responseIdentity).toEqual(model.responseIdentity);
    expect(visibleParityTuples(html)).toEqual(parityTuples(wireModel));
  });

  it('recomputes the authenticated served-body contentKey with an independent walker and canonicalizer', async () => {
    const model = modelFixture();
    const { daemon, token } = await startPoc(model);
    const response = await fetch(`http://${daemon.host}:${daemon.port}${POC_MACHINE_PATH}`, {
      headers: { authorization: `Bearer ${token}` },
    });
    expect(response.status).toBe(200);
    const served = JSON.parse(await response.text()) as Record<string, unknown>;
    const declared = (served.responseIdentity as { readonly excludes: readonly string[] }).excludes;
    expect(declared).toHaveLength(25);
    expect(independentResponseKey(served)).toBe(
      (JSON.parse(JSON.stringify(model)) as PocModel).responseIdentity.contentKey,
    );
  });

  it('keeps GET read-only and byte-identical under five sequential and concurrent requests', async () => {
    const model = modelFixture();
    const { daemon, token, stateDir } = await startPoc(model);
    const marker = join(stateDir, 'read-only-marker.txt');
    writeFileSync(marker, 'GET must not mutate state\n', 'utf8');
    const before = readFileSync(marker);
    const beforeMtime = statSync(marker).mtimeMs;
    const url = `http://${daemon.host}:${daemon.port}${POC_MACHINE_PATH}`;
    const expectedBody = JSON.stringify(model);
    const fetchMachine = async () => (await fetch(url, { headers: { authorization: `Bearer ${token}` } })).text();
    const sequential = await Promise.all([fetchMachine(), fetchMachine(), fetchMachine(), fetchMachine(), fetchMachine()]);
    const concurrent = await Promise.all([fetchMachine(), fetchMachine(), fetchMachine(), fetchMachine(), fetchMachine()]);
    expect(new Set([...sequential, ...concurrent]).size).toBe(1);
    expect(sequential[0]).toBe(expectedBody);
    expect(readFileSync(marker)).toEqual(before);
    expect(statSync(marker).mtimeMs).toBe(beforeMtime);
  });

  it('recomputes response identity when dispatch or mayNot content changes', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    if (model.dispatch === null) throw new Error('fixture should carry the packet');
    const dispatched = JSON.parse(JSON.stringify(model)) as any;
    dispatched.dispatch = {
      dispatchState: 'dispatched',
      packet: model.dispatch.packet,
      beadId: 'bu-response-identity',
      createdAt: '2026-09-23T00:00:00Z',
    };
    dispatched.responseIdentity = { ...model.responseIdentity, contentKey: '' };
    expect(buildResponseIdentity(dispatched).contentKey).not.toBe(model.responseIdentity.contentKey);

    const constrained = JSON.parse(JSON.stringify(model)) as any;
    if (constrained.projectShape.kind === 'not-evaluated') throw new Error('fixture should carry authority');
    constrained.projectShape.authority.mayNot = constrained.projectShape.authority.mayNot.map((row: any, index: number) => index === 0 ? { ...row, statement: `${row.statement} extra constraint` } : row);
    constrained.responseIdentity = { ...model.responseIdentity, contentKey: '' };
    expect(buildResponseIdentity(constrained).contentKey).not.toBe(model.responseIdentity.contentKey);
  });

  it('projects the same mayNot tuples in human Polaris and authenticated machine JSON', async () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    const { daemon, token } = await startPoc(model);
    const html = await (await fetch(`http://${daemon.host}:${daemon.port}/polaris`)).text();
    const machine = JSON.parse(await (await fetch(`http://${daemon.host}:${daemon.port}${POC_MACHINE_PATH}`, { headers: { authorization: `Bearer ${token}` } })).text()) as PocModel;
    if (machine.projectShape.kind === 'not-evaluated') throw new Error('fixture should carry authority');
    const human = [...html.matchAll(/<li[^>]*data-authority-may-not-id="([^"]+)"[^>]*>([\s\S]*?)<\/li>/g)].map((match) => {
      const row = match[2] ?? '';
      const statement = /data-parity-field="authority-may-not-statement">([^<]*)</.exec(row)?.[1] ?? '';
      const act = /data-parity-field="authority-may-not-act">([^<]*)</.exec(row)?.[1] ?? '';
      const digest = /data-parity-field="authority-may-not-digest">([^<]*)</.exec(row)?.[1];
      return [match[1], decodeHtmlText(statement), decodeHtmlText(act), digest === undefined ? undefined : decodeHtmlText(digest)];
    });
    expect(human).toEqual(machine.projectShape.authority.mayNot.map((row) => [row.id, row.statement, row.actIdentity, row.artifactDigest]));
  });

  it('escapes observed text before rendering it into HTML', () => {
    const model = modelFixture();
    const injected: PocModel = {
      ...model,
      dispatch: model.dispatch,
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

  it('keeps empty-seed human and machine responses in parity', async () => {
    const seeded = modelFixture();
    const empty: PocModel = {
      ...seeded,
      dispatch: null,
      project: { ...seeded.project, name: 'Unknown project' },
      capabilityId: 'capability:unknown',
      entities: [],
      relationships: [],
      surfaces: [],
      trajectory: { kind: 'unknown', reason: 'No seed-backed work-item graph was supplied to this evaluation.' },
      orrery: { kind: 'unknown', reason: 'No seed-backed capability-to-path mappings were supplied to this evaluation.' },
    };
    const { daemon, token } = await startPoc(empty);
    const baseUrl = `http://${daemon.host}:${daemon.port}`;
    const html = await (await fetch(`${baseUrl}/`)).text();
    const machineResponse = await fetch(`${baseUrl}${POC_MACHINE_PATH}`, { headers: { authorization: `Bearer ${token}` } });
    expect(machineResponse.status).toBe(200);
    const wireModel = (await machineResponse.json()) as PocModel;
    expect(wireModel).toEqual(empty);
    expect(visibleParityTuples(html)).toEqual(parityTuples(wireModel));
  });
});
