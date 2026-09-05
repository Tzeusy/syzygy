// The authenticated machine presentation envelope (PWB-REQ-014; RFC7-2,
// RFC7-3): `/api/poc/polaris` serves the narrative registry the human page
// was rendered from — the same block, anchor and band multisets — marked a
// non-citable presentation artifact, behind the machine bearer, bounded by
// the machine response ceiling. `/api/poc` is unchanged by it.
//
// Bead syzygy-1z3.24.5 (PWB-LIVE-13).

import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { createDaemon, type RunningDaemon } from '@syzygy/cap1-daemon';
import { PWB_RESOURCE_LIMITS, type PocModel } from '@syzygy/three-surface-poc-core';

import { POLARIS_HUMAN_PATH } from './polaris.js';
import { parseNarrativeScript, type PolarisNarrative } from './polaris-narrative.js';
import { POC_MACHINE_PATH, POLARIS_PRESENTATION_KIND, POLARIS_PRESENTATION_PATH, pocRoutes, type PolarisPresentationEnvelope } from './routes.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { ADMITTING_AUTHORITY, PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET, projectShapeFixtureGit } from './test-project-shape-fixture.js';

const cleanups: string[] = [];
const running: RunningDaemon[] = [];

afterEach(async () => {
  for (const daemon of running.splice(0)) await daemon.close().catch(() => undefined);
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

async function startPoc(model: PocModel, limits = PWB_RESOURCE_LIMITS): Promise<{ readonly baseUrl: string; readonly token: string }> {
  const stateDir = mkdtempSync(join(tmpdir(), 'syzygy-poc-presentation-'));
  cleanups.push(stateDir);
  const start = await createDaemon({ stateDir: join(stateDir, 'state'), routes: pocRoutes(() => model, limits), port: 0 });
  if (!start.started) throw new Error(`daemon failed to start: ${start.failure.kind}`);
  running.push(start.daemon);
  return { baseUrl: `http://${start.daemon.host}:${start.daemon.port}`, token: readFileSync(start.daemon.credentialPath, 'utf8').trim() };
}

function sortedMultiset(values: readonly string[]): string[] {
  return [...values].sort();
}

function multisets(narrative: PolarisNarrative): { blocks: string[]; anchors: string[]; bands: string[] } {
  return {
    blocks: sortedMultiset(narrative.blocks.map((block) => `${block.blockId}\t${block.role}`)),
    anchors: sortedMultiset(narrative.blocks.flatMap((block) => block.anchors.map((anchor) => `${anchor.anchorId}\t${anchor.targetClass}\t${anchor.targetId}\t${anchor.revision}\t${anchor.captured.label}\t${anchor.captured.tier}\t${anchor.captured.reason}`))),
    bands: sortedMultiset(narrative.blocks.map((block) => block.role)),
  };
}

describe('Polaris machine presentation envelope (PWB-REQ-014; RFC7-2, RFC7-3)', () => {
  it('refuses without the bearer and, with it, serves the same block, anchor and band multisets the human page carries, marked non-citable', async () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET) } });
    expect(model.projectShape.kind).toBe('observed');
    const { baseUrl, token } = await startPoc(model);

    const refused = await fetch(`${baseUrl}${POLARIS_PRESENTATION_PATH}`);
    expect(refused.status).toBe(401);
    expect(await refused.json()).toEqual({ admitted: false, served: 'nothing' });

    const admitted = await fetch(`${baseUrl}${POLARIS_PRESENTATION_PATH}`, { headers: { authorization: `Bearer ${token}` } });
    expect(admitted.status).toBe(200);
    expect(admitted.headers.get('content-type')).toBe('application/json');
    const envelope = (await admitted.json()) as PolarisPresentationEnvelope;
    expect(envelope).toMatchObject({ kind: POLARIS_PRESENTATION_KIND, version: 1, presentation: 'presentation-artifact', citable: false });
    expect(envelope.kind).toBe('polaris-presentation');
    expect(envelope.evaluation).toEqual(model.evaluation);
    expect(envelope.project).toEqual({ revision: model.project.revision });

    const humanHtml = await (await fetch(`${baseUrl}${POLARIS_HUMAN_PATH}`)).text();
    const fromPage = parseNarrativeScript(humanHtml);
    expect(fromPage.blocks.length).toBeGreaterThan(0);
    expect(envelope.narrative).toEqual(fromPage);
    expect(multisets(envelope.narrative)).toEqual(multisets(fromPage));
    // The registry carries the anchored blocks; every block is anchored and
    // every anchor is revision-bound to the evaluated shape.
    expect(multisets(fromPage).anchors.length).toBeGreaterThan(0);
    for (const block of envelope.narrative.blocks) {
      expect(block).toMatchObject({ kind: 'narrative-block', presentation: 'presentation-artifact', citable: false });
      expect(block.anchors.length).toBeGreaterThan(0);
    }

    // The tailnet mount serves the identical envelope; the truth endpoint is
    // unchanged: no narrative, the model as before.
    const tailnet = await fetch(`${baseUrl}${TAILNET_MOUNT_PREFIX}${POLARIS_PRESENTATION_PATH}`, { headers: { authorization: `Bearer ${token}` } });
    expect(tailnet.status).toBe(200);
    expect(await tailnet.json()).toEqual(envelope);
    const truth = (await (await fetch(`${baseUrl}${POC_MACHINE_PATH}`, { headers: { authorization: `Bearer ${token}` } })).json()) as PocModel & { narrative?: unknown };
    expect(truth).toEqual(model);
    expect(truth.narrative).toBeUndefined();
  });

  it('fails closed under the machine ceiling with a typed failure and no partial envelope', async () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    const { baseUrl, token } = await startPoc(model, { ...PWB_RESOURCE_LIMITS, maxMachineResponseBytes: 64 });
    const bounded = await fetch(`${baseUrl}${POLARIS_PRESENTATION_PATH}`, { headers: { authorization: `Bearer ${token}` } });
    expect(bounded.status).toBe(503);
    const body = await bounded.text();
    expect(JSON.parse(body)).toMatchObject({ served: 'nothing', failure: 'response-limit-breached', limit: 'maxMachineResponseBytes', declared: 64 });
    expect(body).not.toContain('"narrative"');
  });
});
