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

/** Narrative connective tissue (C3-2): each movement frames the sections
 * that follow it. Ledes are framing about the document's own structure —
 * never a new positive claim about the observed project; anything factual
 * stays inside the cited claim sections. A movement whose anchor entity is
 * absent from the model simply does not render. */
interface Movement {
  readonly beforeEntityId: string;
  readonly heading: string;
  readonly lede: string;
}

const MOVEMENTS: readonly Movement[] = [
  {
    beforeEntityId: 'project:butlers',
    heading: 'What this capability is meant to be',
    lede: 'The reading opens with intent: the observed project, the one capability this POC follows, and the owner-approved requirement that governs it.',
  },
  {
    beforeEntityId: 'code:identity-resolution',
    heading: 'Where it takes shape in the repository',
    lede: 'From intent the reading moves to the mapped artifacts: the code file that realizes the capability and the test that defines its regression check.',
  },
  {
    beforeEntityId: 'work:whatsapp-single-event-normalization',
    heading: 'What has been demonstrated — and what remains Unknown',
    lede: 'The reading closes with the live questions: planned work, captured evidence, runtime satisfaction, and the code deliberately left unmapped. Where the model holds no evidence, the section below says Unknown in place rather than bridging the gap with prose.',
  },
];

function movementHeader(movement: Movement): string {
  return `<header class="movement" data-polaris-movement="${escapeHtml(movement.beforeEntityId)}">
    <h2>${escapeHtml(movement.heading)}</h2>
    <p class="movement-lede">${escapeHtml(movement.lede)}</p>
  </header>`;
}

function entitySection(entity: PocEntity): string {
  const heading = `<h3 id="polaris-${escapeHtml(entity.id)}">${escapeHtml(entity.title)}</h3>`;
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
      <h3 id="polaris-region-code-structure">Observed code structure</h3>
      <p class="unknown-disclosure" data-unknown-disclosure="region:code-structure">Unknown — ${escapeHtml(model.codeStructure.reason)}</p>
    </section>`;
  }
  const cs = model.codeStructure;
  return `<section class="claim-section" data-polaris-section="region:code-structure">
    <h3 id="polaris-region-code-structure">Observed code structure</h3>
    <p><span data-claim-provenance="region:code-structure">The configured project's code structure was inventoried at revision ${escapeHtml(cs.revision.slice(0, 12))}, covering ${cs.files.length} files.</span>
    <span class="citation">(<cite data-parity-field="provenance-source">git-ls-tree</cite>@<code data-parity-field="provenance-revision">${escapeHtml(cs.revision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

function workItemsSection(model: PocModel): string {
  if (model.workItems.kind === 'unknown') {
    return `<section class="claim-section" data-polaris-section="region:work-items">
      <h3 id="polaris-region-work-items">Observed work items</h3>
      <p class="unknown-disclosure" data-unknown-disclosure="region:work-items">Unknown — ${escapeHtml(model.workItems.reason)}</p>
    </section>`;
  }
  const wi = model.workItems;
  return `<section class="claim-section" data-polaris-section="region:work-items">
    <h3 id="polaris-region-work-items">Observed work items</h3>
    <p><span data-claim-provenance="region:work-items">${wi.items.length} work items under the registered prefix <code>${escapeHtml(wi.beadPrefix)}-</code> were read from the Beads Dolt database at revision ${escapeHtml(wi.doltRevision.slice(0, 12))}.</span>
    <span class="citation">(<cite data-parity-field="provenance-source">beads-dolt</cite>@<code data-parity-field="provenance-revision">${escapeHtml(wi.doltRevision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

const POLARIS_STYLE = `
  .claim-section { max-width: 74ch; margin: 0 auto 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
  .claim-section h3 { font-size: clamp(1.25rem, 2.4vw, 1.7rem); margin: 0 0 .8rem; }
  .claim-section p { font-size: 1.05rem; }
  .movement { max-width: 74ch; margin: 3.5rem auto 1.5rem; }
  .movement h2 { font-size: clamp(1.6rem, 3.2vw, 2.4rem); margin: 0 0 .6rem; }
  .movement-lede, .framing, .relationships-lede { font-size: 1.05rem; color: var(--muted); max-width: 74ch; }
  .framing { margin: 0 auto 1rem; }
  .citation { color: var(--muted); font-family: var(--font-mono); font-size: .82rem; }
  .unknown-disclosure { color: var(--unknown); border-left: 3px solid var(--unknown); padding-left: .9rem; }
  .relationships { max-width: 74ch; margin: 0 auto 3rem; }
  .relationships ul { padding-left: 1.2rem; }
  .relationships li { margin-bottom: .5rem; }
`;

export function renderPolarisPage(model: PocModel): string {
  const entitiesById = new Map(model.entities.map((entity) => [entity.id, entity]));
  const movementsByAnchor = new Map(MOVEMENTS.map((movement) => [movement.beforeEntityId, movement]));
  const sections = model.entities
    .map((entity) => {
      const movement = movementsByAnchor.get(entity.id);
      return `${movement === undefined ? '' : movementHeader(movement)}${entitySection(entity)}`;
    })
    .join('');
  const relationshipList = model.relationships
    .map((relationship) => relationshipBullet(relationship, entitiesById))
    .join('');

  // Honest arithmetic over the shared model, never a hand-written total.
  const claims = [...model.entities, ...model.relationships];
  const observedCount = claims.filter((claim) => claim.epistemic.label === 'Observed').length;
  const unknownCount = claims.length - observedCount;

  const body = `
    <p class="notice">Polaris is the long-form reading of the shared model: every positive claim below cites resolvable provenance; where the model holds no evidence, the section discloses Unknown in place rather than filling the gap with prose.</p>
    <p class="framing" data-polaris-framing>This document reads in three movements — what the capability is meant to be, where it takes shape, and what has actually been demonstrated — in that order because intent precedes realization and realization precedes evidence. Of the ${claims.length} entity and relationship claims it makes, ${observedCount} are Observed with citations and ${unknownCount} are disclosed Unknown.</p>
    ${sections}
    <header class="movement" data-polaris-movement="region:code-structure">
      <h2>The inventories behind the map</h2>
      <p class="movement-lede">Orrery and Trajectory render from these two observations; Polaris cites them here so every surface's counts trace to the same source.</p>
    </header>
    ${codeStructureSection(model)}
    ${workItemsSection(model)}
    <section class="relationships" data-polaris-section="relationships">
      <h2 id="polaris-relationships">How these connect</h2>
      <p class="relationships-lede">Each claim above stands alone. The links below state how far the evidence actually reaches between them — an Unknown link is disclosed as Unknown, never bridged by prose.</p>
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
