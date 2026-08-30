import { escapeHtml, type Route } from '@syzygy/cap1-daemon';
import type { PocEntity, PocModel, PocSurface } from '@syzygy/three-surface-poc-core';

import { BROWSER_ORIGIN_REFUSAL, browserRequestAllowed } from './browser-origin.js';
import { epistemicText, exactTablesSection } from './exact-tables.js';
import { ORRERY_HUMAN_PATH, ORRERY_TAILNET_PATH, renderOrreryPage } from './orrery.js';
import { pageShell } from './page-shell.js';
import { POLARIS_HUMAN_PATH, POLARIS_TAILNET_PATH, renderPolarisPage } from './polaris.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';
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

export function renderPocPage(model: PocModel): string {
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
  });
}

export function pocRoutes(getModel: () => PocModel): readonly Route[] {
  const humanHandle: Route['handle'] = ({ request }) =>
    browserRequestAllowed(request.headers)
      ? {
          status: 200,
          contentType: 'text/html; charset=utf-8',
          body: renderPocPage(getModel()),
        }
      : {
          status: 403,
          contentType: 'application/json',
          body: JSON.stringify(BROWSER_ORIGIN_REFUSAL),
        };
  const machineHandle: Route['handle'] = () => ({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify(getModel()),
  });

  function humanSurfaceRoutes(
    directPath: string,
    tailnetPath: string,
    render: (model: PocModel) => string,
  ): readonly Route[] {
    const handle: Route['handle'] = ({ request }) =>
      browserRequestAllowed(request.headers)
        ? { status: 200, contentType: 'text/html; charset=utf-8', body: render(getModel()) }
        : {
            status: 403,
            contentType: 'application/json',
            body: JSON.stringify(BROWSER_ORIGIN_REFUSAL),
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
    ...humanSurfaceRoutes(POLARIS_HUMAN_PATH, POLARIS_TAILNET_PATH, renderPolarisPage),
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
