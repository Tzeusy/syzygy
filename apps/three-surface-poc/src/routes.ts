import { escapeHtml, type Route } from '@syzygy/cap1-daemon';
import type {
  PocEntity,
  PocModel,
  PocRelationship,
  PocSurface,
} from '@syzygy/three-surface-poc-core';

export const POC_HUMAN_PATH = '/' as const;
export const POC_MACHINE_PATH = '/api/poc' as const;
export const BROWSER_ORIGIN_REFUSAL = {
  served: 'nothing',
  reason: 'browser-origin-refused',
} as const;

function singleHeader(
  value: string | readonly string[] | undefined,
): string | undefined {
  return typeof value === 'string' ? value : undefined;
}

function browserRequestAllowed(
  headers: Readonly<Record<string, string | readonly string[] | undefined>>,
): boolean {
  const host = singleHeader(headers['host']);
  if (host === undefined || !/^(?:127\.0\.0\.1|localhost):[0-9]+$/.test(host)) {
    return false;
  }
  const origin = singleHeader(headers['origin']);
  return origin === undefined || origin === `http://${host}`;
}

function epistemicText(
  item: Pick<PocEntity | PocRelationship, 'epistemic'>,
): string {
  return item.epistemic.label === 'Observed'
    ? item.epistemic.basis
    : item.epistemic.reason;
}

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

function provenanceList(item: PocEntity | PocRelationship): string {
  if (item.provenance.length === 0) {
    return '<span class="provenance-none">No positive provenance; this relationship remains Unknown.</span>';
  }
  return `<ul class="provenance">${item.provenance
    .map(
      (provenance) => `<li data-parity-provenance>
        <span data-parity-field="provenance-kind">${escapeHtml(provenance.kind)}</span>
        <code data-parity-field="provenance-source">${escapeHtml(provenance.source)}</code>
        <code data-parity-field="provenance-revision">${escapeHtml(provenance.revision)}</code>
        ${provenance.digest === undefined ? '' : `<code data-parity-field="provenance-digest">${escapeHtml(provenance.digest)}</code>`}
      </li>`,
    )
    .join('')}</ul>`;
}

function entityRows(model: PocModel): string {
  return model.entities
    .map(
      (entity) => `<tr id="${escapeHtml(entity.id)}" data-entity-id="${escapeHtml(entity.id)}">
        <td><span class="kind" data-parity-field="entity-kind">${escapeHtml(entity.kind)}</span></td>
        <td><code data-parity-field="entity-id">${escapeHtml(entity.id)}</code><br><strong data-parity-field="entity-title">${escapeHtml(entity.title)}</strong><br><small data-parity-field="entity-detail">${escapeHtml(entity.detail)}</small></td>
        <td><span class="epistemic epistemic-${entity.epistemic.label.toLowerCase()}" data-parity-field="epistemic-label">${escapeHtml(entity.epistemic.label)}</span><br><small data-parity-field="epistemic-explanation">${escapeHtml(epistemicText(entity))}</small></td>
        <td>${provenanceList(entity)}</td>
      </tr>`,
    )
    .join('');
}

function relationshipRows(model: PocModel): string {
  return model.relationships
    .map(
      (relationship) => `<tr id="${escapeHtml(relationship.id)}" data-relationship-id="${escapeHtml(relationship.id)}">
        <td><span class="kind" data-parity-field="relationship-kind">${escapeHtml(relationship.kind)}</span></td>
        <td><code data-parity-field="relationship-id">${escapeHtml(relationship.id)}</code><br><a data-parity-field="relationship-from" href="#${escapeHtml(relationship.from)}">${escapeHtml(relationship.from)}</a><br>→ <a data-parity-field="relationship-to" href="#${escapeHtml(relationship.to)}">${escapeHtml(relationship.to)}</a></td>
        <td><span data-parity-field="relationship-statement">${escapeHtml(relationship.statement)}</span></td>
        <td><span class="epistemic epistemic-${relationship.epistemic.label.toLowerCase()}" data-parity-field="epistemic-label">${escapeHtml(relationship.epistemic.label)}</span><br><small data-parity-field="epistemic-explanation">${escapeHtml(epistemicText(relationship))}</small></td>
        <td>${provenanceList(relationship)}</td>
      </tr>`,
    )
    .join('');
}

export function renderPocPage(model: PocModel): string {
  const surfaces = model.surfaces.map((surface) => surfacePanel(surface, model)).join('');
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Syzygy · Butlers proof of concept</title>
  <style>
    :root { color-scheme: dark; --ink: #dfe9e7; --muted: #8ca3a4; --void: #071012; --panel: #0c181b; --line: #294248; --cyan: #78e1d1; --amber: #f1b85b; --unknown: #f3c56f; }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { margin: 0; color: var(--ink); background: radial-gradient(circle at 15% 0%, #173238 0, transparent 34rem), var(--void); font-family: Georgia, 'Times New Roman', serif; line-height: 1.5; }
    a { color: var(--cyan); text-underline-offset: .22em; }
    a:focus-visible { outline: 3px solid var(--amber); outline-offset: 4px; }
    code, .kind, .epistemic, .surface-kicker, .eyebrow, nav { font-family: 'Courier New', ui-monospace, monospace; }
    header, main, footer { width: min(1180px, calc(100% - 2rem)); margin-inline: auto; }
    header { padding: 4.5rem 0 2.5rem; }
    .eyebrow { color: var(--cyan); letter-spacing: .15em; text-transform: uppercase; font-size: .77rem; }
    h1 { max-width: 15ch; font-size: clamp(2.7rem, 7vw, 6.4rem); line-height: .9; letter-spacing: -.045em; margin: .5rem 0 1.5rem; }
    .lede { max-width: 70ch; font-size: 1.16rem; color: #bfd0d0; }
    .notice { border-left: 3px solid var(--amber); padding: .85rem 1rem; background: #1b211c; color: #f6dfb5; max-width: 78ch; }
    nav { position: sticky; top: 0; z-index: 2; background: color-mix(in srgb, var(--void) 92%, transparent); border-block: 1px solid var(--line); backdrop-filter: blur(10px); }
    nav ul { width: min(1180px, calc(100% - 2rem)); margin: 0 auto; padding: .8rem 0; display: flex; gap: 1.25rem; list-style: none; overflow-x: auto; }
    .surface-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 1rem; padding: 2rem 0; }
    .surface { min-width: 0; background: linear-gradient(145deg, #102126, var(--panel)); border: 1px solid var(--line); padding: clamp(1.2rem, 3vw, 2rem); box-shadow: 0 18px 45px #0008; }
    .surface-polaris { grid-column: span 7; }
    .surface-trajectory { grid-column: span 5; margin-top: 3rem; }
    .surface-orrery { grid-column: 2 / span 10; }
    .surface h2 { font-size: clamp(2rem, 4vw, 3.4rem); margin: .2rem 0 1rem; }
    .surface-kicker { color: var(--muted); font-size: .78rem; }
    .surface-list { padding: 0; margin: 0; list-style: none; counter-reset: item; }
    .surface-item { display: grid; grid-template-columns: minmax(11rem, 1fr) auto; gap: .4rem 1rem; padding: .8rem 0; border-top: 1px solid var(--line); }
    .surface-item small { grid-column: 1 / -1; color: var(--muted); }
    .epistemic { display: inline-block; padding: .08rem .45rem; border: 1px solid currentColor; font-size: .74rem; letter-spacing: .05em; text-transform: uppercase; }
    .epistemic-observed { color: var(--cyan); }
    .epistemic-unknown { color: var(--unknown); background: #3d2f1322; }
    .tables { padding: 2rem 0 5rem; }
    .tables h2 { font-size: 2.4rem; margin-top: 3rem; }
    .table-wrap { overflow-x: auto; border: 1px solid var(--line); }
    table { width: 100%; border-collapse: collapse; background: #091416; font-size: .92rem; }
    th, td { text-align: left; vertical-align: top; padding: .85rem; border-bottom: 1px solid var(--line); }
    th { color: var(--muted); font-family: 'Courier New', ui-monospace, monospace; font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; }
    tr:target { background: #1e383b; outline: 2px solid var(--cyan); outline-offset: -2px; }
    .kind { color: #9fc0c2; font-size: .74rem; }
    small { color: var(--muted); }
    .provenance { list-style: none; padding: 0; margin: 0; display: grid; gap: .5rem; }
    .provenance li { display: grid; gap: .1rem; }
    .provenance code { overflow-wrap: anywhere; font-size: .72rem; color: #a9c0bf; }
    .provenance-none { color: var(--unknown); font-size: .8rem; }
    footer { padding: 2rem 0 4rem; border-top: 1px solid var(--line); color: var(--muted); }
    @media (max-width: 800px) { .surface-polaris, .surface-trajectory, .surface-orrery { grid-column: 1 / -1; margin-top: 0; } h1 { line-height: 1; } }
    @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
  </style>
</head>
<body>
  <header>
    <div class="eyebrow">Syzygy · local experiment · Butlers ${escapeHtml(model.project.revision.slice(0, 12))}</div>
    <h1>One capability. Three honest views.</h1>
    <p class="lede">${escapeHtml(model.project.name)} · ${escapeHtml(model.entities.find((entity) => entity.id === model.capabilityId)?.title ?? model.capabilityId)}</p>
    <p class="notice"><strong>POC, not product status.</strong> Desired, execution, and observed state remain distinct. Merge is not verification. Missing evidence is rendered Unknown.</p>
  </header>
  <nav aria-label="POC sections"><ul>
    <li><a href="#polaris">Polaris</a></li><li><a href="#trajectory">Trajectory</a></li><li><a href="#orrery">Orrery</a></li><li><a href="#entities">Exact entities</a></li><li><a href="#relationships">Exact relationships</a></li>
  </ul></nav>
  <main>
    <div class="surface-grid">${surfaces}</div>
    <section class="tables" aria-label="Exact graph tables">
      <h2 id="entities">Exact entities</h2>
      <div class="table-wrap"><table><thead><tr><th>Kind</th><th>Entity</th><th>Epistemic state</th><th>Provenance</th></tr></thead><tbody>${entityRows(model)}</tbody></table></div>
      <h2 id="relationships">Exact relationships</h2>
      <div class="table-wrap"><table><thead><tr><th>Kind</th><th>Path</th><th>Claim</th><th>Epistemic state</th><th>Provenance</th></tr></thead><tbody>${relationshipRows(model)}</tbody></table></div>
    </section>
  </main>
  <footer>Evaluation <code>${escapeHtml(model.evaluation.snapshot)}</code> as of <code>${escapeHtml(model.evaluation.asOf)}</code>. Machine facts: authenticated <code>GET ${POC_MACHINE_PATH}</code>.</footer>
</body>
</html>`;
}

export function pocRoutes(getModel: () => PocModel): readonly Route[] {
  return [
    {
      method: 'GET',
      path: POC_HUMAN_PATH,
      credentialClass: 'human-open',
      handle: ({ request }) =>
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
            },
    },
    {
      method: 'GET',
      path: POC_MACHINE_PATH,
      credentialClass: 'machine-credentialed',
      handle: () => ({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify(getModel()),
      }),
    },
  ];
}
