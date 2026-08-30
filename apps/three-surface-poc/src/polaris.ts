import { escapeHtml } from '@syzygy/cap1-daemon';
import type { PocEntity, PocModel, PocProvenance, PocRelationship } from '@syzygy/three-surface-poc-core';

import { pageShell } from './page-shell.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';

export const POLARIS_HUMAN_PATH = '/polaris' as const;
export const POLARIS_TAILNET_PATH = `${TAILNET_MOUNT_PREFIX}/polaris` as const;

function provenanceCitations(provenance: readonly PocProvenance[]): string {
  if (provenance.length === 0) {
    return '';
  }
  const items = provenance
    .map(
      (item) =>
        `<cite data-parity-field="provenance-source">${escapeHtml(item.source)}</cite>@<code data-parity-field="provenance-revision">${escapeHtml(item.revision.slice(0, 12))}</code>`,
    )
    .join(', ');
  return ` <span class="citation">(${items})</span>`;
}

function entitySection(entity: PocEntity): string {
  const heading = `<h2 id="polaris-${escapeHtml(entity.id)}">${escapeHtml(entity.title)}</h2>`;
  if (entity.epistemic.label === 'Observed') {
    return `<section class="claim-section" data-polaris-section="${escapeHtml(entity.id)}">
      ${heading}
      <p><span data-claim-provenance="${escapeHtml(entity.id)}">${escapeHtml(entity.detail)}</span>${provenanceCitations(entity.provenance)}</p>
    </section>`;
  }
  return `<section class="claim-section" data-polaris-section="${escapeHtml(entity.id)}">
    ${heading}
    <p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(entity.id)}">
      Unknown — ${escapeHtml(entity.epistemic.reason)}
    </p>
  </section>`;
}

function relationshipBullet(relationship: PocRelationship, entities: ReadonlyMap<string, PocEntity>): string {
  const fromTitle = entities.get(relationship.from)?.title ?? relationship.from;
  const toTitle = entities.get(relationship.to)?.title ?? relationship.to;
  if (relationship.epistemic.label === 'Observed') {
    return `<li><span data-claim-provenance="${escapeHtml(relationship.id)}">${escapeHtml(fromTitle)} → ${escapeHtml(toTitle)}: ${escapeHtml(relationship.statement)}</span>${provenanceCitations(relationship.provenance)}</li>`;
  }
  return `<li class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(relationship.id)}">${escapeHtml(fromTitle)} → ${escapeHtml(toTitle)}: Unknown — ${escapeHtml(relationship.epistemic.reason)}</li>`;
}

function codeStructureSection(model: PocModel): string {
  if (model.codeStructure.kind === 'unknown') {
    return `<section class="claim-section" data-polaris-section="region:code-structure">
      <h2 id="polaris-region-code-structure">Observed code structure</h2>
      <p class="unknown-disclosure" data-unknown-disclosure="region:code-structure">Unknown — ${escapeHtml(model.codeStructure.reason)}</p>
    </section>`;
  }
  const cs = model.codeStructure;
  return `<section class="claim-section" data-polaris-section="region:code-structure">
    <h2 id="polaris-region-code-structure">Observed code structure</h2>
    <p><span data-claim-provenance="region:code-structure">The configured project's code structure was inventoried at revision ${escapeHtml(cs.revision.slice(0, 12))}, covering ${cs.files.length} files.</span>
    <span class="citation">(<cite data-parity-field="provenance-source">git-ls-tree</cite>@<code data-parity-field="provenance-revision">${escapeHtml(cs.revision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

function workItemsSection(model: PocModel): string {
  if (model.workItems.kind === 'unknown') {
    return `<section class="claim-section" data-polaris-section="region:work-items">
      <h2 id="polaris-region-work-items">Observed work items</h2>
      <p class="unknown-disclosure" data-unknown-disclosure="region:work-items">Unknown — ${escapeHtml(model.workItems.reason)}</p>
    </section>`;
  }
  const wi = model.workItems;
  return `<section class="claim-section" data-polaris-section="region:work-items">
    <h2 id="polaris-region-work-items">Observed work items</h2>
    <p><span data-claim-provenance="region:work-items">${wi.items.length} work items under the registered prefix <code>${escapeHtml(wi.beadPrefix)}-</code> were read from the Beads Dolt database at revision ${escapeHtml(wi.doltRevision.slice(0, 12))}.</span>
    <span class="citation">(<cite data-parity-field="provenance-source">beads-dolt</cite>@<code data-parity-field="provenance-revision">${escapeHtml(wi.doltRevision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

const POLARIS_STYLE = `
  .claim-section { max-width: 74ch; margin: 0 auto 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
  .claim-section:first-of-type { border-top: none; }
  .claim-section h2 { font-size: clamp(1.6rem, 3.2vw, 2.4rem); margin: 0 0 .8rem; }
  .claim-section p { font-size: 1.05rem; }
  .citation { color: var(--muted); font-family: var(--font-mono); font-size: .82rem; }
  .unknown-disclosure { color: var(--unknown); border-left: 3px solid var(--unknown); padding-left: .9rem; }
  .relationships { max-width: 74ch; margin: 0 auto 3rem; }
  .relationships ul { padding-left: 1.2rem; }
  .relationships li { margin-bottom: .5rem; }
`;

export function renderPolarisPage(model: PocModel): string {
  const entitiesById = new Map(model.entities.map((entity) => [entity.id, entity]));
  const sections = model.entities.map((entity) => entitySection(entity)).join('');
  const relationshipList = model.relationships
    .map((relationship) => relationshipBullet(relationship, entitiesById))
    .join('');

  const body = `
    <p class="notice">Polaris is the long-form reading of the shared model: every positive claim below cites resolvable provenance; where the model holds no evidence, the section discloses Unknown in place rather than filling the gap with prose.</p>
    ${sections}
    ${codeStructureSection(model)}
    ${workItemsSection(model)}
    <section class="relationships" data-polaris-section="relationships">
      <h2 id="polaris-relationships">How these connect</h2>
      <ul>${relationshipList}</ul>
    </section>`;

  return pageShell({
    title: 'Polaris · Syzygy three-surface POC',
    current: 'polaris',
    eyebrow: `Polaris · Butlers ${model.project.revision.slice(0, 12)}`,
    heading: 'The long-form reading',
    lede: 'One capability, read as a paginated white paper — every claim cited, every gap disclosed.',
    extraStyle: POLARIS_STYLE,
    body,
    footer: `Evaluation <code>${escapeHtml(model.evaluation.snapshot)}</code> as of <code>${escapeHtml(model.evaluation.asOf)}</code>.`,
    escapeHtml,
  });
}
