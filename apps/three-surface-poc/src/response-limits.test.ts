// Final-output ceilings: registry `resourceLimits.maxHumanResponseBytes`
// and `maxMachineResponseBytes` with `resourceLimitSemantics.breachResult`
// (registry amendment act, 2026-09-05) under PWB-REQ-006 as amended.
// A breach serves only a bounded typed failure; never a truncated page.

import { rmSync } from 'node:fs';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import type { RouteContext, RouteResponse } from '@syzygy/cap1-daemon';
import { PWB_RESOURCE_LIMITS, type PocModel, type PwbResourceLimits } from '@syzygy/three-surface-poc-core';

import { TAILNET_HOST } from './browser-origin.js';
import { renderOrreryPage, ORRERY_HUMAN_PATH } from './orrery.js';
import { renderPolarisPage, POLARIS_HUMAN_PATH } from './polaris.js';
import { boundedResponse, POC_HUMAN_PATH, POC_MACHINE_PATH, pocRoutes, renderPocPage, type ResponseLimitFailure } from './routes.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { renderTrajectoryPage, TRAJECTORY_HUMAN_PATH } from './trajectory.js';

const cleanups: string[] = [];
let model: PocModel;

beforeAll(() => {
  model = buildFixtureModel(cleanups);
});

afterAll(() => {
  for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true });
});

function context(path: string, headers: Record<string, string> = { host: '127.0.0.1:1' }): RouteContext {
  return { request: { method: 'GET', path, query: new URLSearchParams(), headers } };
}

function route(path: string, limits?: PwbResourceLimits): { handle(ctx: RouteContext): RouteResponse } {
  const found = pocRoutes(() => model, limits).find((candidate) => candidate.path === path);
  if (found === undefined) throw new Error(`no route at ${path}`);
  return {
    handle: (ctx) => {
      const response = found.handle(ctx);
      if (response instanceof Promise) throw new Error('POC routes answer synchronously');
      return response;
    },
  };
}

function bytes(body: string): number {
  return Buffer.byteLength(body, 'utf8');
}

function failureOf(body: string): ResponseLimitFailure {
  return JSON.parse(body) as ResponseLimitFailure;
}

describe('boundedResponse — the ceiling is measured on the final encoded body', () => {
  it('limit − 1 breaches, limit and limit + 1 serve, for each ceiling', () => {
    const body = 'héllo'; // 6 bytes, 5 code units: the ceiling counts bytes
    expect(bytes(body)).toBe(6);
    expect(body.length).toBe(5);
    for (const limit of ['maxHumanResponseBytes', 'maxMachineResponseBytes'] as const) {
      const at = (declared: number) => boundedResponse(model, { ...PWB_RESOURCE_LIMITS, [limit]: declared }, limit, 'text/plain', body);
      expect(at(5).status, `${limit} at 5`).toBe(503);
      expect(at(6), `${limit} at 6`).toEqual({ status: 200, contentType: 'text/plain', body });
      expect(at(7).status, `${limit} at 7`).toBe(200);
      const failure = failureOf(at(5).body);
      expect(failure).toEqual({
        served: 'nothing',
        failure: 'response-limit-breached',
        evaluation: model.evaluation,
        limit,
        declared: 5,
        observed: 6,
        population: failure.population,
        readiness: false,
      });
      expect(at(5).contentType).toBe('application/json');
      expect(at(5).body).not.toContain(body);
    }
  });

  it('the failure carries the counted population when the project shape is observed, else an Unknown reason', () => {
    const failure = failureOf(boundedResponse(model, { ...PWB_RESOURCE_LIMITS, maxMachineResponseBytes: 0 }, 'maxMachineResponseBytes', 'application/json', '{}').body);
    const shape = model.projectShape;
    if (shape.kind === 'observed') {
      expect(failure.population).toEqual({ kind: 'counted', sources: shape.counts.sources, items: shape.counts.items, facts: shape.counts.facts, exclusions: shape.counts.exclusions });
    } else {
      expect(failure.population).toEqual({ kind: 'unknown', reason: `project shape ${shape.kind}` });
    }
    const unknownShape = { ...model, projectShape: { ...model.projectShape, kind: 'unavailable' } } as unknown as PocModel;
    const unknown = failureOf(boundedResponse(unknownShape, { ...PWB_RESOURCE_LIMITS, maxHumanResponseBytes: 0 }, 'maxHumanResponseBytes', 'text/html', 'x').body);
    expect(unknown.population).toEqual({ kind: 'unknown', reason: 'project shape unavailable' });
  });
});

describe('pocRoutes — every human HTML sink is bounded by maxHumanResponseBytes', () => {
  const pages: readonly (readonly [string, (m: PocModel, prefix: string) => string])[] = [
    [POC_HUMAN_PATH, (m, p) => renderPocPage(m, p)],
    [POLARIS_HUMAN_PATH, renderPolarisPage],
    [TRAJECTORY_HUMAN_PATH, renderTrajectoryPage],
    [ORRERY_HUMAN_PATH, renderOrreryPage],
  ];

  it.each(pages)('%s: limit − 1 fails closed, limit and limit + 1 serve the page', (path, render) => {
    const size = bytes(render(model, ''));
    expect(size).toBeGreaterThan(0);
    const at = (declared: number) => route(path, { ...PWB_RESOURCE_LIMITS, maxHumanResponseBytes: declared }).handle(context(path));
    const under = at(size - 1);
    expect(under.status).toBe(503);
    expect(under.contentType).toBe('application/json');
    expect(failureOf(under.body)).toMatchObject({ served: 'nothing', failure: 'response-limit-breached', limit: 'maxHumanResponseBytes', declared: size - 1, observed: size, readiness: false });
    expect(under.body).not.toContain('<html');
    expect(at(size)).toEqual({ status: 200, contentType: 'text/html; charset=utf-8', body: render(model, '') });
    expect(at(size + 1).status).toBe(200);
  });

  it('the tailnet mount (selected by Host) is measured on its own rendered body', () => {
    const path = `${TAILNET_MOUNT_PREFIX}/`;
    const size = bytes(renderPocPage(model, TAILNET_MOUNT_PREFIX));
    expect(size).not.toBe(bytes(renderPocPage(model, '')));
    const at = (declared: number) => route(path, { ...PWB_RESOURCE_LIMITS, maxHumanResponseBytes: declared }).handle(context(path, { host: TAILNET_HOST }));
    expect(at(size - 1).status).toBe(503);
    expect(at(size).status).toBe(200);
  });

  it('an origin refusal still comes first and is never measured against the page ceiling', () => {
    const refused = route(POC_HUMAN_PATH, { ...PWB_RESOURCE_LIMITS, maxHumanResponseBytes: 0 }).handle(context(POC_HUMAN_PATH, { host: 'poc.attacker.invalid' }));
    expect(refused.status).toBe(403);
  });
});

describe('pocRoutes — the machine JSON sink is bounded by maxMachineResponseBytes', () => {
  it.each([POC_MACHINE_PATH, `${TAILNET_MOUNT_PREFIX}${POC_MACHINE_PATH}`])('%s: limit − 1 fails closed, limit and limit + 1 serve the model', (path) => {
    const body = JSON.stringify(model);
    const size = bytes(body);
    const at = (declared: number) => route(path, { ...PWB_RESOURCE_LIMITS, maxMachineResponseBytes: declared }).handle(context(path, {}));
    const under = at(size - 1);
    expect(under.status).toBe(503);
    expect(bytes(under.body)).toBeLessThan(size);
    expect(failureOf(under.body)).toMatchObject({ served: 'nothing', limit: 'maxMachineResponseBytes', declared: size - 1, observed: size, evaluation: model.evaluation, readiness: false });
    expect(under.body).not.toContain('"surfaces"');
    expect(at(size)).toEqual({ status: 200, contentType: 'application/json', body });
    expect(at(size + 1).status).toBe(200);
  });

  it('the human ceiling does not bound the machine sink and vice versa', () => {
    const humanOnly = { ...PWB_RESOURCE_LIMITS, maxHumanResponseBytes: 0 };
    expect(route(POC_MACHINE_PATH, humanOnly).handle(context(POC_MACHINE_PATH, {})).status).toBe(200);
    const machineOnly = { ...PWB_RESOURCE_LIMITS, maxMachineResponseBytes: 0 };
    expect(route(POC_HUMAN_PATH, machineOnly).handle(context(POC_HUMAN_PATH)).status).toBe(200);
  });

  it('the registry values are the default ceilings', () => {
    expect(PWB_RESOURCE_LIMITS.maxHumanResponseBytes).toBe(2097152);
    expect(PWB_RESOURCE_LIMITS.maxMachineResponseBytes).toBe(8388608);
    expect(route(POC_HUMAN_PATH).handle(context(POC_HUMAN_PATH)).status).toBe(200);
    expect(route(POC_MACHINE_PATH).handle(context(POC_MACHINE_PATH, {})).status).toBe(200);
  });
});
