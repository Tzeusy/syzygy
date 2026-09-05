import { escapeHtml, type Route, type RouteResponse } from '@syzygy/cap1-daemon';
import { PWB_RESOURCE_LIMITS, type PocEntity, type PocModel, type PocSurface, type PwbResourceLimits } from '@syzygy/three-surface-poc-core';

import { BROWSER_ORIGIN_REFUSAL, browserRequestAllowed } from './browser-origin.js';
import { epistemicText, exactTablesSection } from './exact-tables.js';
import { ORRERY_HUMAN_PATH, ORRERY_TAILNET_PATH, renderOrreryPage } from './orrery.js';
import { pageShell } from './page-shell.js';
import { POLARIS_HUMAN_PATH, POLARIS_TAILNET_PATH, renderPolarisPage, type PolarisRenderInputs } from './polaris.js';
import { mountPrefixForRequest, TAILNET_MOUNT_PREFIX } from './tailnet.js';
import { renderTrajectoryPage, TRAJECTORY_HUMAN_PATH, TRAJECTORY_TAILNET_PATH } from './trajectory.js';

export { BROWSER_ORIGIN_REFUSAL } from './browser-origin.js';

export const POC_HUMAN_PATH = '/' as const;
export const POC_MACHINE_PATH = '/api/poc' as const;

function surfacePanel(surface: PocSurface, model: PocModel): string {
  const entities = new Map(model.entities.map((entity) => [entity.id, entity]));
  const items = surface.entityIds
    .map((entityId) => entities.get(entityId))
    .filter((entity): entity is PocEntity => entity !== undefined)
    .map(
      (entity) => `
        <li class="surface-item" data-surface-entity="${escapeHtml(entity.id)}">
          <a href="#${escapeHtml(entity.id)}">${escapeHtml(entity.title)}</a>
          <span class="epistemic epistemic-${entity.epistemic.label.toLowerCase()}">${escapeHtml(entity.epistemic.label)}</span>
          <small>${escapeHtml(epistemicText(entity))}</small>
        </li>`,
    )
    .join('');

  return `
    <section class="surface surface-${surface.id}" id="${surface.id}" data-surface-id="${surface.id}">
      <div class="surface-kicker">${escapeHtml(surface.question)}</div>
      <h2>${escapeHtml(surface.title)}</h2>
      <ol class="surface-list">${items}</ol>
    </section>`;
}

const HOME_STYLE = `
  .surface-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 1rem; padding: 1rem 0 2rem; }
  .surface { min-width: 0; background: linear-gradient(145deg, #102126, var(--panel)); border: 1px solid var(--line); padding: clamp(1.2rem, 3vw, 2rem); box-shadow: 0 18px 45px #0008; }
  .surface-polaris { grid-column: span 7; }
  .surface-trajectory { grid-column: span 5; margin-top: 3rem; }
  .surface-orrery { grid-column: 2 / span 10; }
  .surface h2 { font-size: clamp(2rem, 4vw, 3.4rem); margin: .2rem 0 1rem; }
  .surface-kicker { color: var(--muted); font-size: .78rem; }
  .surface-list { padding: 0; margin: 0; list-style: none; counter-reset: item; }
  .surface-item { display: grid; grid-template-columns: minmax(11rem, 1fr) auto; gap: .4rem 1rem; padding: .8rem 0; border-top: 1px solid var(--line); }
  .surface-item small { grid-column: 1 / -1; color: var(--muted); }
  .tables { padding: 1rem 0 5rem; }
  .tables h2 { font-size: 2.4rem; margin-top: 3rem; }
  .provenance { list-style: none; padding: 0; margin: 0; display: grid; gap: .5rem; }
  .provenance li { display: grid; gap: .1rem; }
  .provenance code { overflow-wrap: anywhere; font-size: .72rem; color: #a9c0bf; }
  .provenance-none { color: var(--unknown); font-size: .8rem; }
  @media (max-width: 800px) { .surface-polaris, .surface-trajectory, .surface-orrery { grid-column: 1 / -1; margin-top: 0; } }
`;

export function renderPocPage(model: PocModel, mountPrefix = ''): string {
  const surfaces = model.surfaces.map((surface) => surfacePanel(surface, model)).join('');
  const body = `
    <p class="notice"><strong>POC, not product status.</strong> Desired, execution, and observed state remain distinct. Merge is not verification. Missing evidence is rendered Unknown.</p>
    <div class="surface-grid">${surfaces}</div>
    ${exactTablesSection(model)}`;

  return pageShell({
    title: 'Syzygy · Butlers proof of concept',
    current: 'home',
    eyebrow: `Syzygy · local experiment · Butlers ${model.project.revision.slice(0, 12)}`,
    heading: 'One capability. Three honest views.',
    lede: `${model.project.name} · ${model.entities.find((entity) => entity.id === model.capabilityId)?.title ?? model.capabilityId}`,
    extraStyle: HOME_STYLE,
    body,
    footer: `Evaluation <code>${escapeHtml(model.evaluation.snapshot)}</code> as of <code>${escapeHtml(model.evaluation.asOf)}</code>. Machine facts: authenticated <code>GET ${POC_MACHINE_PATH}</code>.`,
    escapeHtml,
    mountPrefix,
  });
}

// ---------------------------------------------------------------------
// Final-output ceilings (registry `resourceLimits.maxHumanResponseBytes` /
// `maxMachineResponseBytes`, `resourceLimitSemantics.breachResult`;
// PWB-REQ-006 as amended). The limit is measured against the final encoded
// HTTP body of each human HTML response and each authenticated machine
// JSON response. A breach emits only this bounded typed failure: the
// evaluation identity, the limit identity, its declared and observed
// values and the population counts. Nothing is truncated and no
// success-shaped model is served; readiness (PWB-REQ-021) is false.

export const RESPONSE_LIMIT_FAILURE = 'response-limit-breached' as const;
export const RESPONSE_LIMIT_STATUS = 503 as const;

export type ResponseLimitIdentity = 'maxHumanResponseBytes' | 'maxMachineResponseBytes';

export interface ResponseLimitFailure {
  readonly served: 'nothing';
  readonly failure: typeof RESPONSE_LIMIT_FAILURE;
  readonly evaluation: PocModel['evaluation'];
  readonly limit: ResponseLimitIdentity;
  readonly declared: number;
  readonly observed: number;
  readonly population:
    | { readonly kind: 'counted'; readonly sources: number; readonly items: number; readonly facts: number; readonly exclusions: number }
    | { readonly kind: 'unknown'; readonly reason: string };
  readonly readiness: false;
}

function populationOf(model: PocModel): ResponseLimitFailure['population'] {
  const shape = model.projectShape;
  if (shape.kind !== 'observed') return { kind: 'unknown', reason: `project shape ${shape.kind}` };
  return { kind: 'counted', sources: shape.counts.sources, items: shape.counts.items, facts: shape.counts.facts, exclusions: shape.counts.exclusions };
}

export function responseLimitFailure(model: PocModel, limit: ResponseLimitIdentity, declared: number, observed: number): ResponseLimitFailure {
  return { served: 'nothing', failure: RESPONSE_LIMIT_FAILURE, evaluation: model.evaluation, limit, declared, observed, population: populationOf(model), readiness: false };
}

// Serves `body` only when its UTF-8 encoding fits the named ceiling.
export function boundedResponse(model: PocModel, limits: PwbResourceLimits, limit: ResponseLimitIdentity, contentType: string, body: string): RouteResponse {
  const observed = Buffer.byteLength(body, 'utf8');
  const declared = limits[limit];
  if (observed <= declared) return { status: 200, contentType, body };
  return { status: RESPONSE_LIMIT_STATUS, contentType: 'application/json', body: JSON.stringify(responseLimitFailure(model, limit, declared, observed)) };
}

/** Render-time inputs for Polaris only (PWB-REQ-011's transient verbatim
 * route): derived per request from the model being rendered, never stored.
 * Absent → Polaris renders with no verbatim reader, so requirement text is
 * disclosed as outside the consented class. */
export type PolarisRenderInputsFor = (model: PocModel) => PolarisRenderInputs;

export function pocRoutes(getModel: () => PocModel, limits: PwbResourceLimits = PWB_RESOURCE_LIMITS, polarisInputs?: PolarisRenderInputsFor): readonly Route[] {
  const html = (model: PocModel, body: string): RouteResponse => boundedResponse(model, limits, 'maxHumanResponseBytes', 'text/html; charset=utf-8', body);
  const humanHandle: Route['handle'] = ({ request }) => {
    if (!browserRequestAllowed(request.headers)) {
      return { status: 403, contentType: 'application/json', body: JSON.stringify(BROWSER_ORIGIN_REFUSAL) };
    }
    const model = getModel();
    return html(model, renderPocPage(model, mountPrefixForRequest(request.headers)));
  };
  const machineHandle: Route['handle'] = () => {
    const model = getModel();
    return boundedResponse(model, limits, 'maxMachineResponseBytes', 'application/json', JSON.stringify(model));
  };

  function humanSurfaceRoutes(
    directPath: string,
    tailnetPath: string,
    render: (model: PocModel, mountPrefix: string) => string,
  ): readonly Route[] {
    const handle: Route['handle'] = ({ request }) => {
      if (!browserRequestAllowed(request.headers)) {
        return { status: 403, contentType: 'application/json', body: JSON.stringify(BROWSER_ORIGIN_REFUSAL) };
      }
      const model = getModel();
      return html(model, render(model, mountPrefixForRequest(request.headers)));
    };
    return [
      { method: 'GET', path: directPath, credentialClass: 'human-open', handle },
      { method: 'GET', path: tailnetPath, credentialClass: 'human-open', handle },
    ];
  }

  return [
    { method: 'GET', path: POC_HUMAN_PATH, credentialClass: 'human-open', handle: humanHandle },
    {
      method: 'GET',
      path: TAILNET_MOUNT_PREFIX,
      credentialClass: 'human-open',
      handle: humanHandle,
    },
    {
      method: 'GET',
      path: `${TAILNET_MOUNT_PREFIX}/`,
      credentialClass: 'human-open',
      handle: humanHandle,
    },
    ...humanSurfaceRoutes(POLARIS_HUMAN_PATH, POLARIS_TAILNET_PATH, (model, mountPrefix) => renderPolarisPage(model, mountPrefix, {}, polarisInputs === undefined ? {} : polarisInputs(model))),
    ...humanSurfaceRoutes(TRAJECTORY_HUMAN_PATH, TRAJECTORY_TAILNET_PATH, renderTrajectoryPage),
    ...humanSurfaceRoutes(ORRERY_HUMAN_PATH, ORRERY_TAILNET_PATH, renderOrreryPage),
    {
      method: 'GET',
      path: POC_MACHINE_PATH,
      credentialClass: 'machine-credentialed',
      handle: machineHandle,
    },
    {
      method: 'GET',
      path: `${TAILNET_MOUNT_PREFIX}${POC_MACHINE_PATH}`,
      credentialClass: 'machine-credentialed',
      handle: machineHandle,
    },
  ];
}
