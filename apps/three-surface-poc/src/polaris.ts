import { escapeHtml } from '@syzygy/cap1-daemon';
import {
  EXTRACTION_CLASSES,
  UNKNOWN_REASON_ROUTES,
  type Exclusion,
  type ExtractionClass,
  type PocEntity,
  type PocModel,
  type PocProvenance,
  type PocRelationship,
  type ProjectAccountKey,
  type ProjectAccountStatement,
  type ProjectShape,
  type ProjectShapeClaim,
  type ProjectShapeFact,
  type ProjectShapeItem,
  type ProjectShapeSource,
  type ProjectShapeSupport,
} from '@syzygy/three-surface-poc-core';

import { pageShell } from './page-shell.js';
import { copyAttr, copyText, roleAttr, type PolarisCopyId } from './polaris-copy.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';

export const POLARIS_HUMAN_PATH = '/polaris' as const;
export const POLARIS_TAILNET_PATH = `${TAILNET_MOUNT_PREFIX}/polaris` as const;

/**
 * The project-level sequence Polaris opens with (PWB-REQ-010; RFC7-1,
 * RFC7-13). The project's own account — purpose, promises, refusals,
 * architecture, V1 — comes first, then the complete catalog, and only then
 * the one capability this POC follows in depth, then the evidence behind
 * every claim and the gaps. Each group is rendered exactly once, in this
 * order, whatever the shape's epistemic state; an unobserved shape renders
 * every project group as Unknown in place with its reason and route
 * (RFC7-15), never as an empty group.
 *
 * Every owner-visible string comes from `polaris-copy.ts` or from the
 * shared model, and the element carrying it declares one `data-copy-role`
 * (PWB-REQ-012). There is no connective prose about the surface itself.
 */
export const POLARIS_GROUPS = [
  'overview',
  'boundaries',
  'architecture',
  'v1',
  'catalog',
  'capability-detail',
  'evidence-and-gaps',
] as const;
export type PolarisGroup = (typeof POLARIS_GROUPS)[number];

const CATALOG_CLASSES: readonly ExtractionClass[] = [
  'catalog-entry',
  'roster-identity',
  'design-contract',
  'baseline-spec',
  'craft-policy',
];

const FACT = roleAttr('project-fact');
const DISCLOSURE = roleAttr('epistemic-disclosure');

function copy(id: PolarisCopyId): string {
  return escapeHtml(copyText(id));
}

function heading(level: 2 | 3, id: string, copyId: PolarisCopyId): string {
  return `<h${level} id="${escapeHtml(id)}"${copyAttr(copyId)}>${copy(copyId)}</h${level}>`;
}

// ---------------------------------------------------------------------------
// Capability-slice renderers (POC-REQ-030…032), unchanged in shape.

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
  const title = `<h3 id="polaris-${escapeHtml(entity.id)}"${FACT}>${escapeHtml(entity.title)}</h3>`;
  if (entity.epistemic.label === 'Observed') {
    return `<section class="claim-section" data-polaris-section="${escapeHtml(entity.id)}">
      ${title}
      <p${FACT}><span data-claim-provenance="${escapeHtml(entity.id)}">${escapeHtml(entity.detail)}</span>${provenanceCitations(entity.provenance)}</p>
    </section>`;
  }
  return `<section class="claim-section" data-polaris-section="${escapeHtml(entity.id)}">
    ${title}
    <p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(entity.id)}"${DISCLOSURE}>
      ${copy('label.unknown')} — ${escapeHtml(entity.epistemic.reason)}
    </p>
  </section>`;
}

function relationshipBullet(relationship: PocRelationship, entities: ReadonlyMap<string, PocEntity>): string {
  const fromTitle = entities.get(relationship.from)?.title ?? relationship.from;
  const toTitle = entities.get(relationship.to)?.title ?? relationship.to;
  if (relationship.epistemic.label === 'Observed') {
    return `<li${FACT}><span data-claim-provenance="${escapeHtml(relationship.id)}">${escapeHtml(fromTitle)} → ${escapeHtml(toTitle)}: ${escapeHtml(relationship.statement)}</span>${provenanceCitations(relationship.provenance)}</li>`;
  }
  return `<li class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(relationship.id)}"${DISCLOSURE}>${escapeHtml(fromTitle)} → ${escapeHtml(toTitle)}: ${copy('label.unknown')} — ${escapeHtml(relationship.epistemic.reason)}</li>`;
}

function codeStructureSection(model: PocModel): string {
  const title = heading(3, 'polaris-region-code-structure', 'evidence.code-structure');
  if (model.codeStructure.kind === 'unknown') {
    return `<section class="claim-section" data-polaris-section="region:code-structure">
      ${title}
      <p class="unknown-disclosure" data-unknown-disclosure="region:code-structure"${DISCLOSURE}>${copy('label.unknown')} — ${escapeHtml(model.codeStructure.reason)}</p>
    </section>`;
  }
  const cs = model.codeStructure;
  return `<section class="claim-section" data-polaris-section="region:code-structure">
    ${title}
    <p${FACT}><span data-claim-provenance="region:code-structure">The configured project's code structure was inventoried at revision ${escapeHtml(cs.revision.slice(0, 12))}, covering ${cs.files.length} files.</span>
    <span class="citation">(<cite data-parity-field="provenance-source">git-ls-tree</cite>@<code data-parity-field="provenance-revision">${escapeHtml(cs.revision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

function workItemsSection(model: PocModel): string {
  const title = heading(3, 'polaris-region-work-items', 'evidence.work-items');
  if (model.workItems.kind === 'unknown') {
    return `<section class="claim-section" data-polaris-section="region:work-items">
      ${title}
      <p class="unknown-disclosure" data-unknown-disclosure="region:work-items"${DISCLOSURE}>${copy('label.unknown')} — ${escapeHtml(model.workItems.reason)}</p>
    </section>`;
  }
  const wi = model.workItems;
  return `<section class="claim-section" data-polaris-section="region:work-items">
    ${title}
    <p${FACT}><span data-claim-provenance="region:work-items">${wi.items.length} work items under the registered prefix <code>${escapeHtml(wi.beadPrefix)}-</code> were read from the Beads Dolt database at revision ${escapeHtml(wi.doltRevision.slice(0, 12))}.</span>
    <span class="citation">(<cite data-parity-field="provenance-source">beads-dolt</cite>@<code data-parity-field="provenance-revision">${escapeHtml(wi.doltRevision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

// ---------------------------------------------------------------------------
// Project-shape renderers (PWB-REQ-010/011; RFC7-15, RFC7-16).

/** The per-claim tuple RFC7-16 requires beside every claim: label, tier,
 * freshness and the evaluation it belongs to — as attributes so a sweep can
 * compare them to the machine answer, and as text for the reader. */
function claimTuple(claim: ProjectShapeClaim): string {
  const tier = claim.epistemic.tier ?? 'unstated';
  const freshness = claim.epistemic.freshness ?? 'unstated';
  return `<span class="claim-tuple" data-claim-id="${escapeHtml(claim.claimId)}" data-epistemic-label="${escapeHtml(claim.epistemic.label)}" data-epistemic-tier="${escapeHtml(tier)}" data-epistemic-freshness="${escapeHtml(freshness)}" data-evaluation-id="${escapeHtml(claim.evaluationId)}"${DISCLOSURE}>${escapeHtml(claim.epistemic.label)} · ${escapeHtml(tier)} · ${escapeHtml(freshness)}</span>`;
}

function tupleLine(claim: ProjectShapeClaim): string {
  return `<p class="tuple-line"${DISCLOSURE}>${claimTuple(claim)}</p>`;
}

function shortDigest(digest: string): string {
  return digest.replace(/^sha256:/, '').slice(0, 12);
}

function sourceSlug(path: string): string {
  return path.replace(/[^A-Za-z0-9]+/g, '-');
}

/** Exact-source citations: path, line and the exact content digest of the
 * bytes the claim was read from, each linked to its source row below. */
function supportCitations(support: readonly ProjectShapeSupport[]): string {
  if (support.length === 0) {
    return '';
  }
  const items = support
    .map((anchor) => {
      const where = anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`;
      const digest = anchor.contentDigest === undefined ? '' : `@<code data-parity-field="shape-anchor-digest">${escapeHtml(shortDigest(anchor.contentDigest))}</code>`;
      return `<a href="#polaris-source-${escapeHtml(sourceSlug(anchor.path))}"><cite data-parity-field="shape-anchor">${escapeHtml(where)}</cite></a>${digest}`;
    })
    .join(', ');
  return ` <span class="citation"${FACT}>(${items})</span>`;
}

function routeOf(claim: ProjectShapeClaim, reason: string): string {
  const route = claim.resolutionRoutes.find((entry) => entry.reason === reason)?.route;
  return route ?? UNKNOWN_REASON_ROUTES[reason as keyof typeof UNKNOWN_REASON_ROUTES] ?? copyText('label.no-route');
}

function unknownRoutes(claim: ProjectShapeClaim, prefix: string): string {
  if (!('reasons' in claim.epistemic)) {
    return `<p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(claim.claimId)}"${DISCLOSURE}>${prefix}${copy('label.unknown')} — ${copy('label.deferred')}.</p>`;
  }
  const { primary, secondary } = claim.epistemic.reasons;
  const secondaryLine = secondary.length === 0
    ? ''
    : `<br><small>${copy('label.also')} ${secondary.map((reason) => `${escapeHtml(reason)} (${copy('label.route').toLowerCase()} ${escapeHtml(routeOf(claim, reason))})`).join('; ')}</small>`;
  return `<p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(claim.claimId)}"${DISCLOSURE}>${prefix}${copy('label.unknown')} — <span data-unknown-reason="${escapeHtml(primary)}">${escapeHtml(primary)}</span>. ${copy('label.route')} ${escapeHtml(routeOf(claim, primary))}.${secondaryLine}</p>`;
}

function accountStatement(statement: ProjectAccountStatement): string {
  const body = statement.claim.epistemic.label === 'Observed' && statement.statement !== undefined
    ? `<p${FACT}><span data-claim-provenance="${escapeHtml(statement.claim.claimId)}">${escapeHtml(statement.statement)}</span>${supportCitations(statement.claim.support)}</p>`
    : unknownRoutes(statement.claim, '');
  return `<section class="claim-section" data-polaris-section="${escapeHtml(statement.claim.claimId)}">
    ${heading(3, `polaris-account-${statement.key}`, `account.${statement.key}`)}
    ${body}
    ${tupleLine(statement.claim)}
  </section>`;
}

function itemRow(item: ProjectShapeItem): string {
  const statement = item.claim.epistemic.label === 'Observed'
    ? `<span data-claim-provenance="${escapeHtml(item.claim.claimId)}">${escapeHtml(item.statement ?? item.key)}</span>${supportCitations(item.claim.support)}`
    : unknownRoutes(item.claim, '');
  return `<tr data-polaris-item="${escapeHtml(item.claim.claimId)}">
    <td${FACT}><code>${escapeHtml(item.key)}</code></td>
    <td${FACT}>${statement}</td>
    <td${DISCLOSURE}>${claimTuple(item.claim)}</td>
  </tr>`;
}

function denominatorText(shape: Extract<ProjectShape, { kind: 'observed' }>, cls: ExtractionClass): string {
  const aggregate = shape.classes[cls];
  const denominator = aggregate.denominator.kind === 'known'
    ? `${aggregate.denominator.value} declared`
    : `denominator Unknown (${aggregate.denominator.reasons.join(', ')})`;
  return `${denominator}; ${aggregate.modeled} modeled, ${aggregate.unknown} Unknown, ${aggregate.contradicted} contradicted; ${aggregate.sourcesWithUnknownDenominator} source(s) unreadable.`;
}

function classBlock(shape: Extract<ProjectShape, { kind: 'observed' }>, cls: ExtractionClass, withItems: boolean): string {
  const aggregate = shape.classes[cls];
  const items = shape.items.filter((item) => item.class === cls);
  const table = !withItems
    ? ''
    : items.length === 0
      ? `<p${copyAttr('sentence.no-items')}><small>${copy('sentence.no-items')}</small></p>`
      : `<div class="table-scroll"><table>
        <thead><tr><th scope="col"${copyAttr('table.key')}>${copy('table.key')}</th><th scope="col"${copyAttr('table.declared')}>${copy('table.declared')}</th><th scope="col"${copyAttr('table.epistemic-state')}>${copy('table.epistemic-state')}</th></tr></thead>
        <tbody>${items.map(itemRow).join('')}</tbody>
      </table></div>`;
  const summary = aggregate.claim.epistemic.label === 'Observed'
    ? `<p${FACT}><span data-claim-provenance="${escapeHtml(aggregate.claim.claimId)}">${escapeHtml(denominatorText(shape, cls))}</span></p>`
    : `${unknownRoutes(aggregate.claim, `${escapeHtml(denominatorText(shape, cls))} `)}`;
  return `<section class="claim-section" data-polaris-section="${escapeHtml(aggregate.claim.claimId)}" data-polaris-class="${escapeHtml(cls)}">
    ${heading(3, `polaris-class-${cls}`, `class.${cls}`)}
    ${summary}
    ${tupleLine(aggregate.claim)}
    ${table}
  </section>`;
}

function accountByKey(shape: Extract<ProjectShape, { kind: 'observed' }>, key: ProjectAccountKey): string {
  const statement = shape.projectAccount.find((entry) => entry.key === key);
  if (statement === undefined) {
    // The model always carries all six keys; an absent one is a defect in
    // the model, disclosed as such rather than hidden.
    return `<section class="claim-section" data-polaris-section="claim:project-account:${escapeHtml(key)}">
      ${heading(3, `polaris-account-${key}`, `account.${key}`)}
      <p class="unknown-disclosure" data-unknown-disclosure="claim:project-account:${escapeHtml(key)}"${DISCLOSURE}>${copy('label.unknown')} — ${copy('sentence.missing-statement')}</p>
    </section>`;
  }
  return accountStatement(statement);
}

function shapeUnknownBlock(shape: Exclude<ProjectShape, { kind: 'observed' }>, group: PolarisGroup): string {
  let detail: string;
  switch (shape.kind) {
    case 'not-evaluated':
      detail = `<p${DISCLOSURE}><small>${copy('sentence.not-evaluated')} ${escapeHtml(shape.detail)}</small></p>`;
      break;
    case 'not-admitted':
      detail = `<p${DISCLOSURE}><small>${copy('sentence.gate-refused')} (${escapeHtml(shape.reason)}${shape.secondaryReasons.length === 0 ? '' : `; ${copy('label.also').toLowerCase()} ${escapeHtml(shape.secondaryReasons.join(', '))}`}). ${escapeHtml(shape.contradiction.clause)}: ${escapeHtml(shape.contradiction.statement)}</small></p>`;
      break;
    case 'observation-failed':
      detail = `<p${DISCLOSURE}><small>${copy('sentence.observer-failed')}${shape.failure.failureState === undefined ? '' : ` (${escapeHtml(shape.failure.failureState)})`}: ${escapeHtml(shape.failure.detail)}</small></p>`;
      break;
  }
  return `<section class="claim-section" data-polaris-section="shape:${escapeHtml(group)}">
    ${unknownRoutes(shape.claim, '')}
    ${detail}
    ${tupleLine(shape.claim)}
  </section>`;
}

function anchorText(anchor: ProjectShapeSource['anchor']): string {
  switch (anchor.kind) {
    case 'blob':
      return `blob ${anchor.objectId.slice(0, 12)}`;
    case 'not-a-blob':
      return `${anchor.type} (mode ${anchor.mode})`;
    case 'missing-at-revision':
      return 'missing at revision';
  }
}

function sourceRow(source: ProjectShapeSource, index: number): string {
  const outcome = source.record.outcome;
  const digest = source.claim.support[0]?.contentDigest;
  const denominator = source.itemDenominator.kind === 'known'
    ? `${source.itemDenominator.value} item(s)`
    : `${copyText('label.unknown')} — ${source.itemDenominator.unknown.unknownReason}`;
  return `<tr id="polaris-source-${escapeHtml(sourceSlug(source.path))}" data-polaris-source="${escapeHtml(source.claim.claimId)}"${FACT}>
    <td>${index + 1}</td>
    <td><code data-parity-field="shape-source-path">${escapeHtml(source.path)}</code><br><small>${escapeHtml(source.identity)}</small></td>
    <td>${escapeHtml(source.rule)}${source.pillar === undefined ? '' : ` · ${escapeHtml(source.pillar)}`}</td>
    <td>${escapeHtml(outcome)} · ${escapeHtml(anchorText(source.anchor))}</td>
    <td>${digest === undefined ? `<small${copyAttr('sentence.no-body-read')}>${copy('sentence.no-body-read')}</small>` : `<code data-parity-field="shape-source-digest">${escapeHtml(shortDigest(digest))}</code>`}</td>
    <td>${source.claim.epistemic.label === 'Observed' ? `<span data-claim-provenance="${escapeHtml(source.claim.claimId)}">${escapeHtml(denominator)}</span>` : unknownRoutes(source.claim, '')}<br>${claimTuple(source.claim)}</td>
  </tr>`;
}

function exclusionItem(exclusion: Exclusion): string {
  const why = exclusion.detectorId ?? exclusion.exclusionReason ?? 'unspecified';
  const digest = exclusion.contentDigest === undefined ? 'never opened' : `digest ${shortDigest(exclusion.contentDigest)}`;
  return `<li data-polaris-exclusion="${escapeHtml(exclusion.repositoryRelativePath)}"${DISCLOSURE}><code>${escapeHtml(exclusion.repositoryRelativePath)}</code> — ${escapeHtml(exclusion.redactionClass)} by ${escapeHtml(why)}${exclusion.detail === undefined ? '' : ` (${escapeHtml(exclusion.detail)})`}; ${escapeHtml(digest)}; policy ${escapeHtml(exclusion.policyId)} ${escapeHtml(exclusion.policyVersion)}. ${copy('sentence.body-withheld')}</li>`;
}

function factItem(fact: ProjectShapeFact): string {
  const declarations = fact.fact.declarations
    .map((declaration) => `${escapeHtml(declaration.value)} (${escapeHtml(declaration.basis)}, ${declaration.anchors.map((anchor) => escapeHtml(anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`)).join(', ')})`)
    .join('; ');
  return `<li data-polaris-fact="${escapeHtml(fact.claim.claimId)}"${DISCLOSURE}>${unknownRoutes(fact.claim, `${escapeHtml(fact.fact.fact)}: `)}<small>${copy('label.declarations-kept')} ${declarations}.</small><br>${claimTuple(fact.claim)}</li>`;
}

/** The Unknown reasons across every shape claim, counted and routed, with
 * `missing-declaration` foremost (RFC7-15) and `unconsented` next. */
function gapsList(claims: readonly ProjectShapeClaim[]): string {
  const counts = new Map<string, number>();
  for (const claim of claims) {
    if ('reasons' in claim.epistemic) {
      const reason = claim.epistemic.reasons.primary;
      counts.set(reason, (counts.get(reason) ?? 0) + 1);
    }
  }
  if (counts.size === 0) {
    return `<p data-polaris-gaps="none"${copyAttr('sentence.no-gaps')}>${copy('sentence.no-gaps')}</p>`;
  }
  const foremost = ['missing-declaration', 'unconsented-source-or-provider'];
  const ordered = [...counts.entries()].sort((a, b) => {
    const ai = foremost.indexOf(a[0]);
    const bi = foremost.indexOf(b[0]);
    if (ai !== bi) return (ai === -1 ? foremost.length : ai) - (bi === -1 ? foremost.length : bi);
    return b[1] - a[1] || a[0].localeCompare(b[0]);
  });
  return `<ul data-polaris-gaps="${counts.size}"${DISCLOSURE}>${ordered
    .map(([reason, count]) => `<li data-polaris-gap="${escapeHtml(reason)}"><span data-unknown-reason="${escapeHtml(reason)}">${escapeHtml(reason)}</span>: ${count} claim(s). ${copy('label.route')} ${escapeHtml(UNKNOWN_REASON_ROUTES[reason as keyof typeof UNKNOWN_REASON_ROUTES] ?? copyText('label.no-route'))}.</li>`)
    .join('')}</ul>`;
}

function shapeClaims(shape: ProjectShape): readonly ProjectShapeClaim[] {
  if (shape.kind !== 'observed') return [shape.claim];
  return [
    shape.claim,
    ...shape.projectAccount.map((entry) => entry.claim),
    ...shape.sources.map((entry) => entry.claim),
    ...shape.items.map((entry) => entry.claim),
    ...EXTRACTION_CLASSES.map((cls) => shape.classes[cls].claim),
    ...shape.facts.map((entry) => entry.claim),
  ];
}

function shapeEvidence(shape: ProjectShape): string {
  if (shape.kind !== 'observed') {
    return `<section class="claim-section" data-polaris-section="shape:evidence">
      ${heading(3, 'polaris-shape-sources', 'evidence.sources')}
      ${unknownRoutes(shape.claim, `${copy('sentence.no-source-read')} `)}
      ${tupleLine(shape.claim)}
    </section>
    <section class="claim-section" data-polaris-section="shape:gaps">
      ${heading(3, 'polaris-shape-gaps', 'evidence.gaps')}
      ${gapsList(shapeClaims(shape))}
    </section>`;
  }
  const identity = shape.identity;
  const counts = `${shape.counts.sourcesAdmitted} of ${shape.counts.sources} sources readable; ${shape.counts.items} items (${shape.counts.modeled} modeled, ${shape.counts.unknown} Unknown, ${shape.counts.contradicted} contradicted); ${shape.counts.facts} facts (${shape.counts.contradictedFacts} contradicted); ${shape.counts.exclusions} exclusion(s).`;
  const whole = shape.claim.epistemic.label === 'Observed'
    ? `<p${FACT}><span data-claim-provenance="${escapeHtml(shape.claim.claimId)}">${escapeHtml(counts)}</span></p>`
    : unknownRoutes(shape.claim, `${escapeHtml(counts)} `);
  return `<section class="claim-section" data-polaris-section="${escapeHtml(shape.claim.claimId)}">
    ${heading(3, 'polaris-shape-identity', 'evidence.observation')}
    ${whole}
    ${tupleLine(shape.claim)}
    <p${FACT}><small>Revision <code data-parity-field="shape-revision">${escapeHtml(identity.revision.slice(0, 12))}</code> (requested <code>${escapeHtml(identity.requestedRevision)}</code>), committed <code>${escapeHtml(identity.sourceClaimedInstant.instant)}</code>, captured <code>${escapeHtml(identity.capturedAt)}</code> by <code>${escapeHtml(identity.observer.observerId)}</code> ${escapeHtml(identity.observer.observerVersion)} under policy <code>${escapeHtml(identity.policy.policyId)}</code> ${escapeHtml(identity.policy.policyVersion)}; manifest <code data-parity-field="shape-manifest-digest">${escapeHtml(shortDigest(identity.manifestDigest))}</code>, observation <code data-parity-field="shape-observation-digest">${escapeHtml(shortDigest(identity.observationDigest))}</code>.</small></p>
    <p${DISCLOSURE}><small>${copy('label.authority')} ${shape.authority.authorities.map((entry) => `${escapeHtml(entry.authority)} — ${escapeHtml(entry.state)}`).join('; ')} (${escapeHtml(shape.authority.authorizationMode)}).</small></p>
  </section>
  <section class="claim-section wide" data-polaris-section="shape:sources">
    ${heading(3, 'polaris-shape-sources', 'evidence.sources')}
    <div class="table-scroll"><table>
      <thead><tr>${(['table.index', 'table.source', 'table.rule', 'table.outcome', 'table.digest', 'table.items'] as const).map((id) => `<th scope="col"${copyAttr(id)}>${copy(id)}</th>`).join('')}</tr></thead>
      <tbody>${shape.sources.map(sourceRow).join('')}</tbody>
    </table></div>
  </section>
  <section class="claim-section" data-polaris-section="shape:exclusions">
    ${heading(3, 'polaris-shape-exclusions', 'evidence.exclusions')}
    ${shape.exclusions.length === 0 ? `<p data-polaris-exclusions="0"${copyAttr('sentence.no-exclusions')}>${copy('sentence.no-exclusions')}</p>` : `<ul data-polaris-exclusions="${shape.exclusions.length}">${shape.exclusions.map(exclusionItem).join('')}</ul>`}
    ${shape.limitBreaches.length === 0 ? '' : `<p${FACT}><small>${copy('label.limit-breaches')} ${shape.limitBreaches.map((breach) => `${escapeHtml(breach.limit)} ${breach.observed} &gt; ${breach.declared}${breach.path === undefined ? '' : ` (${escapeHtml(breach.path)})`}`).join('; ')}.</small></p>`}
  </section>
  <section class="claim-section" data-polaris-section="shape:contradictions">
    ${heading(3, 'polaris-shape-contradictions', 'evidence.contradictions')}
    ${shape.contradictions.length === 0 ? `<p data-polaris-contradictions="0"${copyAttr('sentence.no-contradictions')}>${copy('sentence.no-contradictions')}</p>` : `<ul data-polaris-contradictions="${shape.contradictions.length}">${shape.contradictions.map(factItem).join('')}</ul>`}
  </section>
  <section class="claim-section" data-polaris-section="shape:gaps">
    ${heading(3, 'polaris-shape-gaps', 'evidence.gaps')}
    ${gapsList(shapeClaims(shape))}
  </section>`;
}

// ---------------------------------------------------------------------------

function groupHeader(group: PolarisGroup): string {
  return `<header class="group" data-polaris-group="${escapeHtml(group)}">
    ${heading(2, `polaris-group-${group}`, `group.${group}`)}
  </header>`;
}

function projectGroupBody(shape: ProjectShape, group: Exclude<PolarisGroup, 'capability-detail' | 'evidence-and-gaps'>): string {
  if (shape.kind !== 'observed') {
    return shapeUnknownBlock(shape, group);
  }
  switch (group) {
    case 'overview':
      return `${accountByKey(shape, 'purpose')}${accountByKey(shape, 'promises')}${classBlock(shape, 'project-account-section', false)}`;
    case 'boundaries':
      return `${accountByKey(shape, 'refusals')}${classBlock(shape, 'principle', true)}`;
    case 'architecture':
      return `${accountByKey(shape, 'architecture')}${classBlock(shape, 'topology-component', true)}`;
    case 'v1':
      return `${accountByKey(shape, 'v1-scope')}${accountByKey(shape, 'v1-success')}${classBlock(shape, 'success-criterion', true)}`;
    case 'catalog':
      return CATALOG_CLASSES.map((cls) => classBlock(shape, cls, true)).join('');
  }
}

const POLARIS_STYLE = `
  .claim-section { max-width: 74ch; margin: 0 auto 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
  .claim-section.wide { max-width: 100ch; }
  .claim-section h3 { font-size: clamp(1.25rem, 2.4vw, 1.7rem); margin: 0 0 .8rem; }
  .claim-section p { font-size: 1.05rem; }
  .group { max-width: 74ch; margin: 3.5rem auto 1.5rem; }
  .group h2 { font-size: clamp(1.6rem, 3.2vw, 2.4rem); margin: 0 0 .6rem; }
  .scope-instruction, .relationships-lede { font-size: 1.05rem; color: var(--muted); max-width: 74ch; }
  .scope-instruction { margin: 0 auto 1rem; }
  .citation { color: var(--muted); font-family: var(--font-mono); font-size: .82rem; }
  .citation a { color: inherit; }
  .claim-tuple { font-family: var(--font-mono); font-size: .78rem; color: var(--muted); letter-spacing: .04em; }
  .tuple-line { margin-top: -.4rem; }
  .unknown-disclosure { color: var(--unknown); border-left: 3px solid var(--unknown); padding-left: .9rem; }
  .table-scroll { overflow-x: auto; }
  .relationships { max-width: 74ch; margin: 0 auto 3rem; }
  .relationships ul { padding-left: 1.2rem; }
  .relationships li { margin-bottom: .5rem; }
`;

export function renderPolarisPage(model: PocModel, mountPrefix = ''): string {
  const shape = model.projectShape;
  const entitiesById = new Map(model.entities.map((entity) => [entity.id, entity]));
  const capabilitySections = model.entities.map(entitySection).join('');
  const relationshipList = model.relationships
    .map((relationship) => relationshipBullet(relationship, entitiesById))
    .join('');

  const body = `
    <p class="notice"${copyAttr('notice')}>${copy('notice')}</p>
    ${groupHeader('overview')}
    ${projectGroupBody(shape, 'overview')}
    ${groupHeader('boundaries')}
    ${projectGroupBody(shape, 'boundaries')}
    ${groupHeader('architecture')}
    ${projectGroupBody(shape, 'architecture')}
    ${groupHeader('v1')}
    ${projectGroupBody(shape, 'v1')}
    ${groupHeader('catalog')}
    ${projectGroupBody(shape, 'catalog')}
    ${groupHeader('capability-detail')}
    <p class="scope-instruction" data-polaris-capability-scope data-scope="poc-bound"${copyAttr('capability.scope')}>${copy('capability.scope')}</p>
    ${capabilitySections}
    ${groupHeader('evidence-and-gaps')}
    ${shapeEvidence(shape)}
    ${codeStructureSection(model)}
    ${workItemsSection(model)}
    <section class="relationships" data-polaris-section="relationships">
      ${heading(3, 'polaris-relationships', 'evidence.relationships')}
      <p class="relationships-lede"${copyAttr('evidence.relationships-lede')}>${copy('evidence.relationships-lede')}</p>
      <ul>${relationshipList}</ul>
    </section>`;

  return pageShell({
    title: 'Polaris · Syzygy three-surface POC',
    current: 'polaris',
    eyebrow: `Polaris · Butlers ${model.project.revision.slice(0, 12)}`,
    heading: copyText('shell.heading'),
    lede: copyText('shell.lede'),
    extraStyle: POLARIS_STYLE,
    body,
    footer: `Evaluation <code>${escapeHtml(model.evaluation.snapshot)}</code> as of <code>${escapeHtml(model.evaluation.asOf)}</code>.`,
    escapeHtml,
    mountPrefix,
  });
}
