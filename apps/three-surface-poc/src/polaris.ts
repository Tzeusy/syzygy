import { renderPolarisMarkdown } from './polaris-markdown.js';
import { projectReading, type ProjectReading } from './polaris-reading.js';
import { escapeHtml } from '@syzygy/cap1-daemon';
import {
  EXTRACTION_CLASSES,
  UNKNOWN_REASON_ROUTES,
  type AuthorityDisclosure,
  type Declaration,
  type Exclusion,
  type ExtractionClass,
  type ObservationDegradation,
  type PillarDiscovery,
  type PocEntity,
  type PocModel,
  type PocProvenance,
  type PocRelationship,
  type PrecedenceCitation,
  type PrecedenceDisclosure,
  type ProjectAccountKey,
  type ProjectAccountStatement,
  type ProjectShape,
  type ProjectShapeClaim,
  type ProjectShapeClassAggregate,
  type ProjectShapeFact,
  type ProjectShapeItem,
  type ProjectShapeSource,
  type ProjectShapeSupport,
  type ProposedWork,
  type ReasonCounts,
  type RootSummaryDisclosure,
} from '@syzygy/three-surface-poc-core';

import {
  DEFAULT_READING_MODE,
  DeepDiveLedger,
  currentIntentLeaf,
  deepDiveMachineForm,
  deriveCapabilityDeepDives,
  exclusiveWith,
  resolveVerbatim,
  type CapabilityDeepDive,
  type DeepDiveBand,
  type VerbatimLeafReader,
  type VerbatimResolution,
} from './capability-detail.js';
import { pageShell } from './page-shell.js';
import { copyAttr, copyText, roleAttr, type PolarisCopyId } from './polaris-copy.js';
import {
  NarrativeRegistry,
  artifactAnchor,
  capturedStateOf,
  narrativeScript,
  provenanceAnchor,
  supportAnchor,
  type AnchorInput,
  type AnchorTargetClass,
  type CapturedTargetState,
  type NarrativeAnchor,
  type PolarisViewState,
} from './polaris-narrative.js';
import { sourceRouteHref, sourceSlug } from './polaris-source.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';

export { sourceSlug };

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
  'v1',
  'architecture',
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
/** An anchored project fact: copy role project-fact, claim role anchored. */
const ANCHORED = roleAttr('project-fact', 'anchored-project-fact');

// ---------------------------------------------------------------------------
// Narrative blocks (PWB-REQ-014). One registry per render; the renderer is
// synchronous, so the active registry is module state for the duration of
// one `renderPolarisPage` call and cleared afterwards.

let activeRegistry: NarrativeRegistry | undefined;
let activeViewState: PolarisViewState = {};

/** The one page's link targets (PWB-REQ-011/016): the Unknown reasons the
 * gaps list enumerates and the source paths the sources table rows carry.
 * A reason or path outside these sets renders as text, never as a link to
 * nothing (RFC7-31's dangling-link floor). */
interface PageTargets {
  readonly gapReasons: ReadonlySet<string>;
  readonly sourcePaths: ReadonlySet<string>;
}
const NO_TARGETS: PageTargets = { gapReasons: new Set(), sourcePaths: new Set() };
let activeTargets: PageTargets = NO_TARGETS;
/** The mount the page is rendered under: the exact-source route links are
 * built relative to it. */
let activeMountPrefix = '';
/** The evaluation's exclusions and unavailable sources, so an Unknown's
 * route names its actual cause (PWB-LIVE-11): the detector, grammar or
 * observer failure that produced it — never a blanket policy change. */
let activeExclusions: readonly Exclusion[] = [];
let activeUnavailable: readonly { readonly path: string; readonly reason: string }[] = [];
/** Identities the exact-source route can serve: admitted baseline specs
 * whose body was classified and whose anchor is a blob at this revision. */
let activeExactSources: ReadonlySet<string> = new Set();

function gapId(reason: string): string {
  return `polaris-gap-${reason.replace(/[^A-Za-z0-9]+/g, '-')}`;
}

/** An Unknown reason as text, linked to its entry in the gaps list when the
 * page enumerates it there, so every reason mention reaches its route by
 * keyboard. */
function unknownReasonRef(reason: string): string {
  const span = `<span data-unknown-reason="${escapeHtml(reason)}">${escapeHtml(reason)}</span>`;
  return activeTargets.gapReasons.has(reason) ? `<a href="#${gapId(reason)}" data-gap-ref="${escapeHtml(reason)}">${span}</a>` : span;
}

/** A source location as text, linked to its row in the sources table when
 * the page carries that source. */
function sourceRef(path: string, text: string): string {
  return activeTargets.sourcePaths.has(path)
    ? `<a href="#polaris-source-${escapeHtml(sourceSlug(path))}" data-source-ref="${escapeHtml(path)}">${escapeHtml(text)}</a>`
    : escapeHtml(text);
}

/** A horizontally scrollable table region is a keyboard stop of its own
 * (tabindex 0) named by the heading above it, so a keyboard-only reader can
 * scroll a wide table without a pointer. */
function tableRegion(labelledBy: string, table: string, attrs = ''): string {
  return `<div class="table-scroll" role="region" tabindex="0" aria-labelledby="${escapeHtml(labelledBy)}"${attrs}>${table}</div>`;
}

function registry(): NarrativeRegistry {
  if (activeRegistry === undefined) throw new Error('renderPolarisPage is not active');
  return activeRegistry;
}

interface AnchoredClaim {
  readonly claimId: string;
  readonly anchors: readonly AnchorInput[];
  readonly captured: CapturedTargetState;
}

/** Registers one anchored block and returns the attributes for its element
 * plus the rendered anchor citations. Anchors are deduplicated by target so
 * a block never carries a surplus anchor; each keeps the claims it supports. */
function anchoredBlock(blockId: string, claims: readonly AnchoredClaim[]): { readonly attrs: string; readonly anchors: readonly NarrativeAnchor[] } {
  const merged = new Map<string, AnchorInput & { supports: string[]; captured: CapturedTargetState }>();
  for (const claim of claims) {
    for (const anchor of claim.anchors) {
      const key = `${anchor.targetClass}|${anchor.targetId}|${anchor.revision}|${anchor.locator}`;
      const existing = merged.get(key);
      if (existing === undefined) merged.set(key, { ...anchor, supports: [claim.claimId], captured: claim.captured });
      else if (!existing.supports.includes(claim.claimId)) existing.supports.push(claim.claimId);
    }
  }
  const block = registry().registerAnchored(blockId, claims.map((claim) => claim.claimId), [...merged.values()]);
  return { attrs: `${ANCHORED} data-narrative-block="${escapeHtml(blockId)}"`, anchors: block.anchors };
}

/** The human citation names its anchor by id only. The anchor record itself
 * (target class, durable target identity, revision, supported claims and the
 * captured label/tier/reason) lives once, frozen, in the page's narrative
 * script under that id — the machine form PWB-REQ-014 binds — and is not
 * restated on every `<cite>` (byte-ceiling trim, syzygy-1z3.27). */
function anchorAttrs(anchor: NarrativeAnchor): string {
  return ` data-anchor-id="${escapeHtml(anchor.anchorId)}"`;
}

function entityCaptured(epistemic: { readonly label: string; readonly reason?: string }): CapturedTargetState {
  return { label: epistemic.label, tier: epistemic.label === 'Observed' ? 'report-fact' : 'unstated', reason: epistemic.reason ?? 'none' };
}

function copy(id: PolarisCopyId): string {
  return escapeHtml(copyText(id));
}

function heading(level: 2 | 3 | 4, id: string, copyId: PolarisCopyId): string {
  return `<h${level} id="${escapeHtml(id)}"${copyAttr(copyId)}>${copy(copyId)}</h${level}>`;
}

// ---------------------------------------------------------------------------
// Capability-slice renderers (POC-REQ-030…032), unchanged in shape.

function provenanceCitations(provenance: readonly PocProvenance[], anchors: readonly NarrativeAnchor[]): string {
  if (provenance.length === 0) {
    return '';
  }
  const items = provenance
    .map(
      (item, index) =>
        `<cite data-parity-field="provenance-source"${anchorAttrs(anchors[index] as NarrativeAnchor)}>${escapeHtml(item.source)}</cite>@<code data-parity-field="provenance-revision">${escapeHtml(item.revision.slice(0, 12))}</code>`,
    )
    .join(', ');
  return ` <span class="citation">(${items})</span>`;
}

function entitySection(entity: PocEntity, blockAttrs = ` data-polaris-section="${escapeHtml(entity.id)}"`): string {
  const title = `<h3 id="polaris-${escapeHtml(entity.id)}"${FACT}>${escapeHtml(entity.title)}</h3>`;
  if (entity.epistemic.label === 'Observed') {
    const block = anchoredBlock(`block:${entity.id}`, [{ claimId: entity.id, anchors: entity.provenance.map(provenanceAnchor), captured: entityCaptured(entity.epistemic) }]);
    return `<section class="claim-section"${blockAttrs}>
      ${title}
      <p${block.attrs}><span data-claim-provenance="${escapeHtml(entity.id)}">${escapeHtml(entity.detail)}</span>${provenanceCitations(entity.provenance, block.anchors)}</p>
    </section>`;
  }
  return `<section class="claim-section"${blockAttrs}>
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
    const block = anchoredBlock(`block:${relationship.id}`, [{ claimId: relationship.id, anchors: relationship.provenance.map(provenanceAnchor), captured: entityCaptured(relationship.epistemic) }]);
    return `<li${block.attrs}><span data-claim-provenance="${escapeHtml(relationship.id)}">${escapeHtml(fromTitle)} → ${escapeHtml(toTitle)}: ${escapeHtml(relationship.statement)}</span>${provenanceCitations(relationship.provenance, block.anchors)}</li>`;
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
  const block = anchoredBlock('block:region:code-structure', [{
    claimId: 'region:code-structure',
    anchors: [{ targetClass: 'evidence', targetId: `git-tree:${cs.revision}`, revision: cs.revision, locator: 'git-ls-tree' }],
    captured: { label: 'Observed', tier: 'report-fact', reason: 'none' },
  }]);
  return `<section class="claim-section" data-polaris-section="region:code-structure">
    ${title}
    <p${block.attrs}><span data-claim-provenance="region:code-structure">The configured project's code structure was inventoried at revision ${escapeHtml(cs.revision.slice(0, 12))}, covering ${cs.files.length} files.</span>
    <span class="citation">(<cite data-parity-field="provenance-source"${anchorAttrs(block.anchors[0] as NarrativeAnchor)}>git-ls-tree</cite>@<code data-parity-field="provenance-revision">${escapeHtml(cs.revision.slice(0, 12))}</code>)</span></p>
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
  const block = anchoredBlock('block:region:work-items', [{
    claimId: 'region:work-items',
    anchors: [{ targetClass: 'work', targetId: `beads-dolt:${wi.doltRevision}`, revision: wi.doltRevision, locator: 'beads-dolt' }],
    captured: { label: 'Observed', tier: 'report-fact', reason: 'none' },
  }]);
  return `<section class="claim-section" data-polaris-section="region:work-items">
    ${title}
    <p${block.attrs}><span data-claim-provenance="region:work-items">${wi.items.length} work items under the registered prefix <code>${escapeHtml(wi.beadPrefix)}-</code> were read from the Beads Dolt database at revision ${escapeHtml(wi.doltRevision.slice(0, 12))}.</span>
    <span class="citation">(<cite data-parity-field="provenance-source"${anchorAttrs(block.anchors[0] as NarrativeAnchor)}>beads-dolt</cite>@<code data-parity-field="provenance-revision">${escapeHtml(wi.doltRevision.slice(0, 12))}</code>)</span></p>
  </section>`;
}

// ---------------------------------------------------------------------------
// Project-shape renderers (PWB-REQ-010/011; RFC7-15, RFC7-16).

/** The per-claim tuple RFC7-16 and PWB-REQ-007 require beside every claim:
 * label, tier, primary reason, secondary reasons, freshness, challenge state
 * and the evaluation it belongs to — as attributes so a sweep can compare
 * them field by field to the machine answer, and as text for the reader.
 * Absent tier or freshness renders as `unstated`, never as a default. */
function claimTuple(claim: ProjectShapeClaim): string {
  const tier = claim.epistemic.tier ?? 'unstated';
  const freshness = claim.epistemic.freshness ?? 'unstated';
  const epistemic = claim.epistemic;
  const primary = 'reasons' in epistemic ? epistemic.reasons.primary : 'basis' in epistemic ? epistemic.basis : 'none';
  const secondary = 'reasons' in epistemic ? epistemic.reasons.secondary : [];
  const reasonText = epistemic.label === 'Unknown'
    ? ` (${escapeHtml(primary)}${secondary.length === 0 ? '' : `; ${secondary.map(escapeHtml).join(', ')}`})`
    : '';
  return `<span class="claim-tuple" data-claim-id="${escapeHtml(claim.claimId)}" data-epistemic-label="${escapeHtml(epistemic.label)}" data-epistemic-tier="${escapeHtml(tier)}" data-epistemic-primary-reason="${escapeHtml(primary)}" data-epistemic-secondary-reasons="${escapeHtml(secondary.join(','))}" data-epistemic-freshness="${escapeHtml(freshness)}" data-challenge-state="${escapeHtml(claim.challenge)}" data-evaluation-id="${escapeHtml(claim.evaluationId)}" aria-describedby="polaris-claim-states-lede"${DISCLOSURE}>${escapeHtml(epistemic.label)}${reasonText} · ${escapeHtml(tier)} · ${escapeHtml(freshness)} · ${escapeHtml(claim.challenge)}</span>`;
}

/** PWB-REQ-007: an aggregate discloses its members' primary and secondary
 * Unknown reason counts separately, each with its route — never a headline
 * status, a maturity or a success. */
export function reasonCountsBlock(claimId: string, counts: ReasonCounts): string {
  const list = (which: 'primary' | 'secondary', entries: Readonly<Partial<Record<string, number>>>): string => {
    const rows = Object.entries(entries).filter((entry): entry is [string, number] => typeof entry[1] === 'number' && entry[1] > 0);
    if (rows.length === 0) return '';
    return `<p${DISCLOSURE}>${copy(which === 'primary' ? 'label.primary-reasons' : 'label.secondary-reasons')}</p>
      <ul data-reason-counts-${which}="${escapeHtml(claimId)}"${DISCLOSURE}>${rows
        .map(([reason, count]) => `<li data-reason="${escapeHtml(reason)}" data-count="${count}">${unknownReasonRef(reason)}: ${count}. <details class="reason-remedies"><summary${copyAttr('label.source-remedies')}>${copy('label.source-remedies')}</summary><p>${copy('label.route')} ${reasonRouteHtml(reason)}</p></details></li>`)
        .join('')}</ul>`;
  };
  const primary = list('primary', counts.primary);
  const secondary = list('secondary', counts.secondary);
  const body = primary === '' && secondary === ''
    ? `<p${copyAttr('sentence.no-member-unknowns')}>${copy('sentence.no-member-unknowns')}</p>`
    : `${primary}${secondary}`;
  return `<div class="reason-counts" data-reason-counts="${escapeHtml(claimId)}">${body}</div>`;
}

/** Coverage counts stay available on demand, never as the default view. */
function onDemandCounts(claimId: string, text: string): string {
  const open = activeViewState.openCoverageCounts?.includes(claimId) === true ? ' open' : '';
  return `<details class="coverage-counts" data-coverage-counts="${escapeHtml(claimId)}"${open}><summary${copyAttr('label.coverage-counts')}>${copy('label.coverage-counts')}</summary><p${FACT}>${text}</p></details>`;
}

/** The claim-state glossary (PWB-REQ-007; RFC2-25): every field of the
 * tuple beside each claim, in ordinary words, and the only routes that
 * strengthen a claim. One disclosure, once, described-by from every tuple. */
function claimStatesBlock(): string {
  const sentence = (id: PolarisCopyId): string => `<p${copyAttr(id)}>${copy(id)}</p>`;
  const group = (labelId: PolarisCopyId, ids: readonly PolarisCopyId[]): string =>
    `<p${copyAttr(labelId)}>${copy(labelId)}</p><ul>${ids.map((id) => `<li${copyAttr(id)}>${copy(id)}</li>`).join('')}</ul>`;
  return `<details id="polaris-claim-states" class="claim-states" data-polaris-claim-states>
    <summary${copyAttr('label.claim-states')}>${copy('label.claim-states')}</summary>
    <p class="lede" id="polaris-claim-states-lede"${copyAttr('states.lede')}>${copy('states.lede')}</p>
    ${sentence('states.observed')}
    ${sentence('states.inferred')}
    ${sentence('states.unknown')}
    ${group('states.tier', ['states.tier.gate-backed', 'states.tier.report-fact', 'states.tier.reduced-fidelity', 'states.tier.asserted-by-worker', 'states.tier.declared-only', 'states.tier.suspended', 'states.tier.unstated'])}
    ${group('states.freshness', ['states.freshness.fresh', 'states.freshness.stale', 'states.freshness.broken', 'states.freshness.superseded'])}
    ${group('states.challenge', ['states.challenge.unchallenged'])}
    ${sentence('states.strengthen')}
  </details>`;
}

/** Progressive disclosure (PWB-REQ-011): an exhaustive population stays
 * complete on the page, behind one native disclosure whose control names
 * the population and its count. Nothing is hidden by style; the reader
 * opens it by keyboard. The sources table is not wrapped: its rows are
 * fragment targets, and Chrome restarts sequential focus at the first
 * focusable of a `<details>` after navigating to a target inside it, so a
 * reader who follows a citation could not continue past the row. The
 * sources table is routed instead — the last depth, reached by the depth
 * list and by citations. */
function population(kind: 'items' | 'exclusions', key: string, count: number, labelId: PolarisCopyId, inner: string): string {
  return `<details class="population" data-polaris-${kind}="${escapeHtml(key)}"><summary${copyAttr(labelId)}>${copy(labelId)} (${count})</summary>${inner}</details>`;
}

/** The exact-source route link for one admitted baseline spec identity. */
function exactTextLink(identity: string): string {
  return `<a href="${escapeHtml(sourceRouteHref(activeMountPrefix, identity))}"${copyAttr('label.exact-text')}>${copy('label.exact-text')}</a>`;
}

function tupleLine(claim: ProjectShapeClaim): string {
  return `<p class="tuple-line"${DISCLOSURE}>${claimTuple(claim)}</p>`;
}

function shortDigest(digest: string): string {
  return digest.replace(/^sha256:/, '').slice(0, 12);
}

/** Exact-source citations: path, line and the exact content digest of the
 * bytes the claim was read from, each linked to its source row below. */
function supportCitations(support: readonly ProjectShapeSupport[], anchors: readonly NarrativeAnchor[]): string {
  if (support.length === 0) {
    return '';
  }
  const items = support
    .map((anchor, index) => {
      const where = anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`;
      const digest = anchor.contentDigest === undefined ? '' : `@<code data-parity-field="shape-anchor-digest">${escapeHtml(shortDigest(anchor.contentDigest))}</code>`;
      return `<a href="#polaris-source-${escapeHtml(sourceSlug(anchor.path))}"><cite data-parity-field="shape-anchor"${anchorAttrs(anchors[index] as NarrativeAnchor)}>${escapeHtml(where)}</cite></a>${digest}`;
    })
    .join(', ');
  return ` <span class="citation">(${items})</span>`;
}

/** One anchored block for one Observed shape claim: its support anchors,
 * bound to the evaluated revision, with the claim's own captured state. */
function shapeClaimBlock(claim: ProjectShapeClaim, revision: string, targetClass: AnchorTargetClass = 'evidence', blockId = `block:${claim.claimId}`): { readonly attrs: string; readonly anchors: readonly NarrativeAnchor[] } {
  const anchors = claim.support.map((support) => supportAnchor(support, revision, targetClass)).filter((anchor): anchor is AnchorInput => anchor !== undefined);
  return anchoredBlock(blockId, [{ claimId: claim.claimId, anchors, captured: capturedStateOf(claim) }]);
}

/** The cause-correct route for one exclusion: what produced it and what,
 * in Butlers or by the owner, resolves it. A parse failure is a repair in
 * Butlers or an owner gate on the grammar, never a policy change; a detector
 * match is a rotation in Butlers or an owner change to that detector. */
function excludedCauseRoute(exclusion: Exclusion): string {
  const path = exclusion.repositoryRelativePath;
  if (exclusion.detectorId !== undefined) {
    return `${path} matched the ${exclusion.detectorId} detector: rotate and remove the matched text in Butlers, then a new snapshot; or an owner policy change to that detector`;
  }
  switch (exclusion.exclusionReason) {
    case 'parse-failure':
      return `${path} does not parse under the declared grammar${exclusion.detail === undefined ? '' : ` (${exclusion.detail})`}: repair the row in Butlers, then a new snapshot; or an owner gate amending the grammar. No policy change is involved`;
    case 'active-content':
      return `${path} carries active content${exclusion.detail === undefined ? '' : ` (${exclusion.detail} marker(s))`}: remove it in Butlers, then a new snapshot; or an owner policy change admitting it`;
    case 'resource-limit':
      return `${path} exceeds a declared resource limit: reduce the source in Butlers, then a new snapshot; or an owner act raising the limit`;
    case 'denied-path':
      return `${path} is a denied path: only an owner policy change admits it`;
    case 'contains-nul':
    case 'not-utf-8':
      return `${path} is not UTF-8 text: make it text in Butlers, then a new snapshot`;
    case 'unknown-extraction-class':
      return `${path} names no registered extraction class: an owner registry change, then a new snapshot`;
    default:
      return `${path}: ${UNKNOWN_REASON_ROUTES['excluded-content']}`;
  }
}

function unavailableCauseRoute(source: { readonly path: string; readonly reason: string }): string {
  return `${source.path} was not captured (${source.reason}): repair the observer or the source in Butlers, then a new snapshot`;
}

/** The routes by cause for one reason over a set of paths: the exclusions
 * or uncaptured sources among them, or all of the evaluation's when the
 * claim's support does not name one. Undefined when the evaluation records
 * no cause of that kind. */
function causeRoutes(reason: string, paths: ReadonlySet<string> | undefined): readonly string[] | undefined {
  if (reason === 'excluded-content') {
    const own = paths === undefined ? [] : activeExclusions.filter((exclusion) => paths.has(exclusion.repositoryRelativePath));
    const matched = own.length > 0 ? own : activeExclusions;
    return matched.length === 0 ? undefined : [...new Set(matched.map(excludedCauseRoute))];
  }
  if (reason === 'source-uncaptured-or-unreachable') {
    const own = paths === undefined ? [] : activeUnavailable.filter((source) => paths.has(source.path));
    const matched = own.length > 0 ? own : activeUnavailable;
    return matched.length === 0 ? undefined : [...new Set(matched.map(unavailableCauseRoute))];
  }
  return undefined;
}

function routeOf(claim: ProjectShapeClaim, reason: string): string {
  const causes = causeRoutes(reason, new Set(claim.support.map((support) => support.path)));
  if (causes !== undefined) return causes.join('; ');
  const route = claim.resolutionRoutes.find((entry) => entry.reason === reason)?.route;
  return route ?? UNKNOWN_REASON_ROUTES[reason as keyof typeof UNKNOWN_REASON_ROUTES] ?? copyText('label.no-route');
}

/** The route text of one reason in a list keyed by reason (gaps, reason
 * counts): the generic route, then the evaluation's causes when it records
 * any, so the reader reaches the actual cause without leaving the list. */
function reasonRouteHtml(reason: string): string {
  const generic = UNKNOWN_REASON_ROUTES[reason as keyof typeof UNKNOWN_REASON_ROUTES] ?? copyText('label.no-route');
  const causes = causeRoutes(reason, undefined);
  return causes === undefined
    ? `${escapeHtml(generic)}.`
    : `${escapeHtml(generic)}. <span${copyAttr('label.by-cause')}>${copy('label.by-cause')}</span> ${escapeHtml(causes.join('; '))}.`;
}

function unknownRoutes(claim: ProjectShapeClaim, prefix: string): string {
  if (!('reasons' in claim.epistemic)) {
    return `<p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(claim.claimId)}"${DISCLOSURE}>${prefix}${copy('label.unknown')} — ${copy('label.deferred')}.</p>`;
  }
  const { primary, secondary } = claim.epistemic.reasons;
  const secondaryLine = secondary.length === 0
    ? ''
    : `<br><small>${copy('label.also')} ${secondary.map((reason) => `${escapeHtml(reason)} (${copy('label.route').toLowerCase()} ${escapeHtml(routeOf(claim, reason))})`).join('; ')}</small>`;
  return `<div class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(claim.claimId)}"${DISCLOSURE}><p>${prefix.startsWith('Declared by ') ? '' : prefix}${copy('label.unknown')} — ${unknownReasonRef(primary)}.</p><details class="unknown-source-details"><summary${copyAttr('label.source-remedies')}>${copy('label.source-remedies')}</summary><p>${prefix.startsWith('Declared by ') ? prefix : ''}${copy('label.route')} ${escapeHtml(routeOf(claim, primary))}.${secondaryLine}</p></details></div>`;
}

export function renderProjectReading(reading: ProjectReading, anchorId?: string): string {
  const label = reading.condensed ? `<p class="excerpt-label"${copyAttr('label.selected-passages')}>${copy('label.selected-passages')}</p>` : '';
  const chapters = reading.chapters;
  const full = chapters !== undefined
    ? `<section class="component-library"><h4${copyAttr('label.component-guides')}>${copy('label.component-guides')}</h4><button type="button" class="expand-declaration" aria-expanded="false"${copyAttr('label.full-account')}>${copy('label.full-account')}</button><div class="component-guides">${chapters.map((chapter) => `<section id="polaris-guide-${escapeHtml(chapter.id)}" data-component-guide><details><summary>${escapeHtml(chapter.title)}</summary><div class="reading-prose">${renderPolarisMarkdown(chapter.body, anchorId)}</div></details></section>`).join('')}</div></section>`
    : reading.condensed ? `<details class="full-account"><summary${copyAttr('label.full-account')}>${copy('label.full-account')}</summary><div class="reading-prose">${renderPolarisMarkdown(reading.full, anchorId)}</div></details>` : '';
  return `${label}<div class="reading-prose">${renderPolarisMarkdown(reading.summary, anchorId)}</div>${full}`;
}

function accountStatement(statement: ProjectAccountStatement, revision: string): string {
  const body = statement.claim.epistemic.label === 'Observed' && statement.statement !== undefined
    ? ((): string => {
        const block = shapeClaimBlock(statement.claim, revision);
        const reading = projectReading(statement.statement, statement.key);
        return `<div class="account-reading"${block.attrs}><div data-claim-provenance="${escapeHtml(statement.claim.claimId)}">${renderProjectReading(reading, block.anchors.length === 1 ? block.anchors[0]!.anchorId : undefined)}</div><details class="reading-citations"><summary${copyAttr('label.source-notes')}>${copy('label.source-notes')}</summary>${supportCitations(statement.claim.support, block.anchors)}</details></div>`;
      })()
    : unknownRoutes(statement.claim, '');
  return `<section class="claim-section" data-polaris-section="${escapeHtml(statement.claim.claimId)}">
    ${heading(3, `polaris-account-${statement.key}`, `account.${statement.key}`)}
    ${body}
    ${tupleLine(statement.claim)}
  </section>`;
}

function itemRow(item: ProjectShapeItem, revision: string): string {
  const block = item.claim.epistemic.label === 'Observed' ? shapeClaimBlock(item.claim, revision) : undefined;
  const identity = item.claim.support[0]?.sourceIdentity;
  const exact = block !== undefined && item.class === 'baseline-spec' && identity !== undefined && activeExactSources.has(identity) ? ` ${exactTextLink(identity)}` : '';
  const statement = block !== undefined
    ? `<div class="reading-prose" data-claim-provenance="${escapeHtml(item.claim.claimId)}">${renderPolarisMarkdown(item.statement ?? item.key)}</div>${supportCitations(item.claim.support, block.anchors)}${exact}`
    : unknownRoutes(item.claim, '');
  // The key cell takes the table region's role (declared once on the region,
  // classBlock); the tuple cell holds only the tuple span, which declares its
  // own. The declared cell is the row's one narrative unit.
  return `<tr data-polaris-item="${escapeHtml(item.claim.claimId)}"><td><code>${escapeHtml(item.key)}</code></td><td${block?.attrs ?? FACT}>${statement}</td><td>${claimTuple(item.claim)}</td></tr>`;
}

export function denominatorText(aggregate: Pick<ProjectShapeClassAggregate, 'denominator' | 'modeled' | 'unknown' | 'contradicted' | 'sourcesWithUnknownDenominator'>): string {
  const denominator = aggregate.denominator.kind === 'known'
    ? `${aggregate.denominator.value} declared`
    : `denominator Unknown (${aggregate.denominator.reasons.join(', ')})`;
  return `${denominator}; ${aggregate.modeled} modeled, ${aggregate.unknown} Unknown, ${aggregate.contradicted} contradicted; ${aggregate.sourcesWithUnknownDenominator} source(s) unreadable.`;
}

/** The aggregate's statement: which admitted sources declare this class —
 * a fact about the sources, not a count wall or a status. */
function classStatement(shape: Extract<ProjectShape, { kind: 'observed' }>, cls: ExtractionClass): string {
  const aggregate = shape.classes[cls];
  const declaring = shape.sources.filter((source) => source.extractionClasses.includes(cls)).map((source) => source.path);
  if (declaring.length === 0 && aggregate.denominator.kind === 'unknown') return 'Source discovery is incomplete for this class.';
  return declaring.length === 0 ? 'No admitted source declares this class.' : `Declared by ${declaring.join(', ')}.`;
}

function capabilityGuide(shape: Extract<ProjectShape, { kind: 'observed' }>): string {
  const groups = new Map<string, ProjectShapeItem[]>();
  for (const item of shape.items.filter((item) => item.class === 'catalog-entry')) {
    const context = item.context ?? copyText('class.catalog-entry');
    const group = groups.get(context) ?? [];
    group.push(item);
    groups.set(context, group);
  }
  const practicalOrder = ['Butlers', 'Staffers', 'Dashboard', 'Connectors'];
  const rank = (context: string): number => { const index = practicalOrder.indexOf(context); return index < 0 ? practicalOrder.length : index; };
  const entries = [...groups.entries()].sort(([a], [b]) => rank(a) - rank(b));
  return `<section class="capability-guide" id="polaris-capability-guide">
    <p class="guide-intro"${copyAttr('label.guide-intro')}>${copy('label.guide-intro')} <a href="#polaris-class-catalog-entry"${copyAttr('label.complete-catalog')}>${copy('label.complete-catalog')}</a></p>
    <div class="guide-grid">${entries.map(([context, members]) => {
      const example = members.find((item) => item.claim.epistemic.label === 'Observed' && item.statement !== undefined);
      if (example === undefined) return `<section class="guide-entry"><h4${FACT}>${escapeHtml(context)}</h4><p${SCOPE}>${copy('label.complete-catalog')}</p></section>`;
      const block = shapeClaimBlock(example.claim, shape.identity.revision, 'evidence', `guide:${example.claim.claimId}`);
      return `<section class="guide-entry"><h4${FACT}>${escapeHtml(context)}</h4><div${block.attrs}><div class="reading-prose" data-claim-provenance="${escapeHtml(example.claim.claimId)}">${renderPolarisMarkdown(example.statement as string)}</div><details class="reading-citations"><summary${copyAttr('label.source-notes')}>${copy('label.source-notes')}</summary>${supportCitations(example.claim.support, block.anchors)}</details></div><details class="guide-state"><summary${DISCLOSURE}>${escapeHtml(example.claim.epistemic.label)}</summary>${claimTuple(example.claim)}</details></section>`;
    }).join('')}</div>
  </section>`;
}

function classBlock(shape: Extract<ProjectShape, { kind: 'observed' }>, cls: ExtractionClass, withItems: boolean): string {
  const aggregate = shape.classes[cls];
  const items = shape.items.filter((item) => item.class === cls);
  const table = !withItems
    ? ''
    : items.length === 0
      ? `<p${copyAttr('sentence.no-items')}><small>${copy('sentence.no-items')}</small></p>`
      : population('items', cls, items.length, 'label.show-items', tableRegion(`polaris-class-${cls}`, `<table><thead><tr><th scope="col"${copyAttr('table.key')}>${copy('table.key')}</th><th scope="col"${copyAttr('table.declared')}>${copy('table.declared')}</th><th scope="col"${copyAttr('table.epistemic-state')}>${copy('table.epistemic-state')}</th></tr></thead><tbody>${items.map((item) => itemRow(item, shape.identity.revision)).join('')}</tbody></table>`, FACT));
  const summary = aggregate.claim.epistemic.label === 'Observed'
    ? ((): string => {
        const block = shapeClaimBlock(aggregate.claim, shape.identity.revision);
        const contexts = cls === 'catalog-entry' ? [...new Set(items.map((item) => item.context).filter((context): context is string => context !== undefined))] : [];
        const guide = contexts.length === 0 ? '' : `<ul class="catalog-contexts">${contexts.map((context) => `<li>${escapeHtml(context)}</li>`).join('')}</ul>`;
        return `<details class="class-provenance"><summary${copyAttr('label.source-notes')}>${copy('label.source-notes')}</summary><div${block.attrs}><div data-claim-provenance="${escapeHtml(aggregate.claim.claimId)}">${guide}<p>${escapeHtml(classStatement(shape, cls))}</p></div>${supportCitations(aggregate.claim.support, block.anchors)}</div></details>`;
      })()
    : unknownRoutes(aggregate.claim, `${escapeHtml(classStatement(shape, cls))} `);
  return `<section class="claim-section" data-polaris-section="${escapeHtml(aggregate.claim.claimId)}" data-polaris-class="${escapeHtml(cls)}">
    ${heading(3, `polaris-class-${cls}`, `class.${cls}`)}
    ${summary}
    ${tupleLine(aggregate.claim)}
    ${reasonCountsBlock(aggregate.claim.claimId, aggregate.reasonCounts)}
    ${onDemandCounts(aggregate.claim.claimId, escapeHtml(denominatorText(aggregate)))}
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
  return accountStatement(statement, shape.identity.revision);
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
    ${shape.authority === undefined || group !== 'overview' ? '' : authorityLine(shape.authority)}
    ${tupleLine(shape.claim)}
  </section>`;
}

/** PWB-REQ-005/020: every body-read authority's state, the authorization
 * mode and the evaluation the states belong to, each as its own parity
 * marker so the human channel keeps one marker per authority (multiplicity)
 * and names the evaluation it was disclosed at. */
/** The cause-correct route for one Unknown pillar (PWB-RECON-02): what
 * phase A could not find and what, in Butlers or by owner gate, would
 * resolve it. Exhaustive over the closed reason set by type. */
function pillarRoute(pillar: Extract<PillarDiscovery, { state: 'unknown' }>): string {
  const home = pillar.root === undefined ? 'its home' : pillar.root;
  const index = pillar.indexPath === undefined ? 'its index' : pillar.indexPath;
  switch (pillar.reason) {
    case 'root-index-missing-at-revision':
      return 'the root index is absent at this revision, so no pillar home is named: restore it in Butlers, then a new snapshot';
    case 'root-index-unavailable':
      return `the root index could not be read${pillar.detail === undefined ? '' : ` (${pillar.detail})`}: restore its body in Butlers, then a new snapshot`;
    case 'not-named-in-root-index':
      return 'the root index names no home for this pillar: add its link in Butlers, then a new snapshot; or an owner gate amending the pillar set';
    case 'named-root-ambiguous':
      return 'the root index names more than one home for this pillar: keep exactly one in Butlers, then a new snapshot';
    case 'root-missing-at-revision':
      return `the named home ${home} is absent at this revision: create it in Butlers, then a new snapshot`;
    case 'index-missing-at-revision':
      return `the home ${home} carries no index at ${index} at this revision: add that index in Butlers, then a new snapshot; or an owner gate amending the discovery rule. No policy change is involved`;
    case 'index-unavailable':
      return `the index ${index} could not be read${pillar.detail === undefined ? '' : ` (${pillar.detail})`}: restore its body in Butlers, then a new snapshot`;
  }
}

/** One marker per pillar with its discovery state; an Unknown pillar adds
 * its reason marker and the route, a discovered one its index and count. */
function discoveryLine(discovery: readonly PillarDiscovery[]): string {
  const entries = discovery
    .map((pillar) => {
      const state = `<span data-parity-field="shape-pillar-state" data-pillar="${escapeHtml(pillar.key)}">${escapeHtml(pillar.key)} — ${escapeHtml(pillar.state)}</span>`;
      if (pillar.state === 'discovered') return `${state} (${escapeHtml(pillar.indexPath)}, ${pillar.namedSources} named)`;
      return `${state} (<span data-parity-field="shape-pillar-reason" data-pillar="${escapeHtml(pillar.key)}">${escapeHtml(pillar.reason)}</span>; ${copy('label.route').toLowerCase()} ${escapeHtml(pillarRoute(pillar))})`;
    })
    .join('; ');
  return `<p${DISCLOSURE} data-shape-discovery><small>${copy('label.discovery')} ${entries}.</small></p>`;
}

/** The observation's degradation state, or the sentence that none was
 * recorded — never silence in either case. */
function degradationLine(degradation: ObservationDegradation | undefined): string {
  if (degradation === undefined) return `<p data-shape-degradation="none"${copyAttr('sentence.no-degradation')}><small>${copy('sentence.no-degradation')}</small></p>`;
  return `<p${DISCLOSURE} data-shape-degradation="${escapeHtml(degradation.failureState)}"><small>${copy('label.degradation')} <span data-parity-field="shape-degradation-state">${escapeHtml(degradation.degradationState)}</span> (${escapeHtml(degradation.failureState)}; ${escapeHtml(degradation.detail)}).</small></p>`;
}

function authorityLine(authority: AuthorityDisclosure): string {
  // PWB-REQ-005 on the human surface (PWB-RECON-01): every authority's
  // state and, beside it, its exact disclosure sentence — state (1) renders
  // the quoted sentence verbatim, the machine answer carries the same
  // string, and the parity sweep compares the two per authority.
  const entries = authority.authorities
    .map((entry) => `<span data-parity-field="authority-state" data-authority="${escapeHtml(entry.authority)}">${escapeHtml(entry.authority)} — ${escapeHtml(entry.state)}</span> (<span data-parity-field="authority-disclosure" data-authority="${escapeHtml(entry.authority)}">${escapeHtml(entry.disclosure)}</span>)`)
    .join('; ');
  return `<p${DISCLOSURE} data-authority-evaluation><small>${copy('label.authority')} ${entries} (<span data-parity-field="authority-mode">${escapeHtml(authority.authorizationMode)}</span>), ${copy('label.evaluated-as')} <code data-parity-field="authority-evaluation-id">${escapeHtml(authority.evaluationId)}</code>.</small></p>`;
}

/** PWB-REQ-021/022 on the one surface: the owner's cold-open walkthrough
 * judgment exactly as the evaluator carried it. Every state, label,
 * disclosure sentence, digest and traversed path is its own parity marker;
 * a lawful verdict is recorded human judgment — presented under the
 * epistemic-disclosure role, never as a project fact or a score. */
function walkthroughJudgmentSection(model: PocModel): string {
  const judgment = model.walkthroughJudgment;
  const head = heading(3, 'polaris-walkthrough-judgment', 'evidence.walkthrough');
  if (judgment.kind === 'not-evaluated') {
    return `<section class="claim-section" data-polaris-section="walkthrough-judgment" data-judgment-state="not-evaluated">
    ${head}
    <p${DISCLOSURE}><small>${copy('sentence.judgment-not-evaluated')} <span data-parity-field="judgment-detail">${escapeHtml(judgment.detail)}</span></small></p>
  </section>`;
  }
  const { evaluation } = judgment;
  const outcome = evaluation.outcome;
  const evaluated = `<p${DISCLOSURE}><small>${copy('label.judgment-evaluation')} <code data-parity-field="judgment-evaluation-id">${escapeHtml(evaluation.evaluationId)}</code> ${copy('label.at')} <code data-parity-field="judgment-evaluation-instant">${escapeHtml(evaluation.evaluationInstant)}</code>; ${copy('label.outcome')} <span data-parity-field="judgment-kind">${escapeHtml(outcome.kind)}</span>.</small></p>`;
  let body: string;
  switch (outcome.kind) {
    case 'absent':
      body = `<p${DISCLOSURE}><small>${copy('sentence.judgment-absent')} (<span data-parity-field="judgment-absent-what">${escapeHtml(outcome.what)}</span>): <span data-parity-field="judgment-detail">${escapeHtml(outcome.detail)}</span> ${copy('label.criterion')} <span data-parity-field="judgment-criterion">${escapeHtml(outcome.criterion)}</span>.</small></p>`;
      break;
    case 'unlawful':
      body = `<p${DISCLOSURE}><small>${copy('sentence.judgment-unlawful')} <code data-parity-field="judgment-recorded">${escapeHtml(outcome.recorded)}</code> (<code data-parity-field="judgment-case">${escapeHtml(outcome.caseId)}</code>): <span data-parity-field="judgment-detail">${escapeHtml(outcome.detail)}</span> ${copy('label.criterion')} <span data-parity-field="judgment-criterion">${escapeHtml(outcome.criterion)}</span>. ${copy('label.contradiction')} <span data-parity-field="judgment-contradiction">${escapeHtml(outcome.contradiction.clause)}</span> — ${escapeHtml(outcome.contradiction.statement)}</small></p>
    <p${DISCLOSURE}><small>${copy('label.run-record')} <code data-parity-field="judgment-run-record-digest">${escapeHtml(shortDigest(outcome.runRecordDigest))}</code>; ${copy('label.judgment-digest')} <code data-parity-field="judgment-digest">${escapeHtml(shortDigest(outcome.judgmentDigest))}</code>.</small></p>`;
      break;
    case 'lawful':
      body = `<p${DISCLOSURE}><small>${copy('label.verdict')} <code data-parity-field="judgment-verdict">${escapeHtml(`${outcome.verdict.criterion}=${outcome.verdict.value}`)}</code>, ${copy('label.judged-by')} <span data-parity-field="judgment-judging-party">${escapeHtml(outcome.verdict.judgingParty)}</span>; <span data-parity-field="judgment-evidence-kind">${escapeHtml(outcome.evidenceKind)}</span>; <span data-parity-field="judgment-state-label">${escapeHtml(outcome.stateLabel)}</span>; ${copy('label.independently-verified')} <span data-parity-field="judgment-independently-verified">${outcome.independentlyVerified ? 'yes' : 'no'}</span>. <q data-parity-field="judgment-disclosure">${escapeHtml(outcome.disclosure)}</q></small></p>
    <p${DISCLOSURE}><small>${copy('label.act')} <code data-parity-field="judgment-act">${escapeHtml(outcome.actIdentity)}</code> ${copy('label.at')} <code data-parity-field="judgment-act-instant">${escapeHtml(outcome.actInstant)}</code>; ${copy('label.judgment-digest')} <code data-parity-field="judgment-digest">${escapeHtml(shortDigest(outcome.judgmentDigest))}</code>.</small></p>
    <p${DISCLOSURE}><small>${copy('label.run-record')} <code data-parity-field="judgment-run-record">${escapeHtml(`${outcome.runRecord.identity}@${shortDigest(outcome.runRecord.digest)}`)}</code>, <span data-parity-field="judgment-mode">${escapeHtml(outcome.runRecord.mode)}</span>, <code data-parity-field="judgment-surface-version">${escapeHtml(outcome.runRecord.surfaceVersion)}</code>, <code data-parity-field="judgment-run-evaluation-identity">${escapeHtml(outcome.runRecord.evaluationIdentity)}</code>; ${copy('label.traversed')} ${outcome.runRecord.traversedPaths.map((path) => `<code data-parity-field="judgment-traversed-path">${escapeHtml(path)}</code>`).join(', ')}.</small></p>
    <p${DISCLOSURE}><small>${copy('label.rationale')} <span data-parity-field="judgment-rationale">${escapeHtml(outcome.verdict.rationale)}</span></small></p>`;
      break;
  }
  return `<section class="claim-section" data-polaris-section="walkthrough-judgment" data-judgment-state="${escapeHtml(outcome.kind)}">
    ${head}
    ${evaluated}
    ${body}
  </section>`;
}

/** PWB-REQ-021 (as amended 2026-09-05): whether the retained walkthrough
 * record is a ready answer population against this evaluation. Every
 * finding, every retained answer and every anchor is its own
 * `data-polaris-readiness*` marker (the machine channel carries the same
 * value under `walkthroughReadiness`); the owner's words are shown verbatim
 * under the disclosure role — an execution fact, never a verdict or score,
 * and separate from the judgment above. */
function walkthroughReadinessSection(model: PocModel): string {
  const readiness = model.walkthroughReadiness;
  const head = heading(3, 'polaris-walkthrough-readiness', 'evidence.walkthrough-readiness');
  if (readiness.kind === 'not-evaluated') {
    return `<section class="claim-section" data-polaris-section="walkthrough-readiness" data-polaris-readiness="not-evaluated">
    ${head}
    <p${DISCLOSURE}><small>${copy('sentence.readiness-not-evaluated')} <span data-polaris-readiness-detail>${escapeHtml(readiness.detail)}</span></small></p>
  </section>`;
  }
  const r = readiness.readiness;
  // The exact binding a record must name for this evaluation — shown in
  // every state so the recording session copies it, never invents it.
  const expected = `<p${DISCLOSURE}><small>${copy('label.expected-binding')} ${copy('label.surface-version')} <code data-polaris-readiness-expected-surface>${escapeHtml(r.expected.surfaceVersion)}</code>; ${copy('label.evaluation-identity')} <code data-polaris-readiness-expected-evaluation>${escapeHtml(r.expected.evaluationIdentity)}</code>.</small></p>`;
  if (r.kind === 'no-run-record') {
    return `<section class="claim-section" data-polaris-section="walkthrough-readiness" data-polaris-readiness="no-run-record">
    ${head}
    <p${DISCLOSURE}><small>${copy('sentence.readiness-no-run-record')} <span data-polaris-readiness-detail>${escapeHtml(r.detail)}</span></small></p>
    ${expected}
  </section>`;
  }
  const state = r.ready ? 'ready' : 'not-ready';
  const findings = r.findings.length === 0
    ? ''
    : `<p${DISCLOSURE}><small>${copy('label.readiness-findings')}</small></p>
    <ul${DISCLOSURE}>${r.findings.map((finding) => `<li data-polaris-readiness-arm="${escapeHtml(finding.arm)}"><small><code>${escapeHtml(finding.arm)}</code> — <span data-polaris-readiness-finding>${escapeHtml(finding.detail)}</span></small></li>`).join('')}</ul>`;
  const traversed = r.traversedPaths.map((path) => `<code data-polaris-readiness-traversed>${escapeHtml(path)}</code>`).join(', ');
  const answers = r.answers.length === 0
    ? ''
    : `<p${DISCLOSURE}><small>${copy('label.answers')}</small></p>
    <ol${DISCLOSURE} data-polaris-answers>${r.answers.map((answer) => {
      const anchors = answer.anchors.length === 0
        ? ''
        : `<br><small>${copy('label.sources')} ${answer.anchors.map((anchor) => `<code data-polaris-answer-anchor="${escapeHtml(anchor.path)}:${anchor.line}" data-polaris-anchor-resolved="${anchor.resolved ? 'yes' : 'no'}">${escapeHtml(`${anchor.path}:${anchor.line}`)}</code>`).join(', ')}</small>`;
      const authority = answer.authority === undefined
        ? ''
        : `<br><small>${copy('label.cited-authority')} <code data-polaris-answer-authority="${escapeHtml(answer.authority.path)}" data-polaris-authority-resolved="${answer.authority.resolved ? 'yes' : 'no'}">${escapeHtml(answer.authority.path)}</code></small>`;
      return `<li data-polaris-answer="${escapeHtml(answer.identity)}"><code>${escapeHtml(answer.identity)}</code><blockquote data-polaris-answer-text>${escapeHtml(answer.text)}</blockquote>${anchors}${authority}</li>`;
    }).join('')}</ol>`;
  return `<section class="claim-section" data-polaris-section="walkthrough-readiness" data-polaris-readiness="${state}">
    ${head}
    <p${DISCLOSURE}><small>${copy('label.readiness')} <span data-polaris-readiness-state>${state}</span>. ${copy('sentence.readiness-execution-fact')} ${copy('label.surface-version')} <code data-polaris-readiness-surface>${escapeHtml(r.surfaceVersion ?? '')}</code>; ${copy('label.evaluation-identity')} <code data-polaris-readiness-evaluation>${escapeHtml(r.evaluationIdentity ?? '')}</code>; ${traversed === '' ? '' : `${copy('label.traversed')} ${traversed}.`}</small></p>
    ${expected}
    ${findings}
    ${answers}
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

function sourceRow(source: ProjectShapeSource, index: number, revision: string): string {
  const outcome = source.record.outcome === 'classified'
    ? source.record.basis === 'path-only' ? 'path-only' : 'body-classified'
    : source.record.outcome;
  const block = source.claim.epistemic.label === 'Observed' ? shapeClaimBlock(source.claim, revision) : undefined;
  const identityCell = block === undefined
    ? `<small>${escapeHtml(source.identity)}</small>`
    : `<small><cite data-parity-field="shape-source-identity"${anchorAttrs(block.anchors[0] as NarrativeAnchor)}>${escapeHtml(source.identity)}</cite></small>`;
  const digest = source.claim.support[0]?.contentDigest;
  const denominator = source.itemDenominator.kind === 'known'
    ? `${source.itemDenominator.value} item(s)`
    : `${copyText('label.unknown')} — ${source.itemDenominator.unknown.unknownReason}`;
  const record = `<details class="source-record"><summary${copyAttr('label.source-record')}>${copy('label.source-record')}</summary>
    ${identityCell}
    <dl><dt>${copy('table.rule')}</dt><dd>${escapeHtml(source.rule)}${source.pillar === undefined ? '' : ` · ${escapeHtml(source.pillar)}`}</dd>
    <dt>${copy('table.outcome')}</dt><dd>${escapeHtml(outcome)} · ${escapeHtml(anchorText(source.anchor))}</dd>
    <dt>${copy('table.digest')}</dt><dd>${digest === undefined ? `<small${copyAttr('sentence.no-body-read')}>${copy('sentence.no-body-read')}</small>` : `<code data-parity-field="shape-source-digest">${escapeHtml(shortDigest(digest))}</code>`}</dd></dl>
  </details>`;
  return `<tr id="polaris-source-${escapeHtml(sourceSlug(source.path))}" data-polaris-source="${escapeHtml(source.claim.claimId)}"${block?.attrs ?? FACT}><td>${index + 1}</td><td><code data-parity-field="shape-source-path">${escapeHtml(source.path)}</code>${activeExactSources.has(source.identity) ? `<br>${exactTextLink(source.identity)}` : ''}${record}</td><td>${source.claim.epistemic.label === 'Observed' ? `<span data-claim-provenance="${escapeHtml(source.claim.claimId)}">${escapeHtml(denominator)}</span>` : unknownRoutes(source.claim, '')}<br>${claimTuple(source.claim)}</td></tr>`;
}

function exclusionItem(exclusion: Exclusion): string {
  const why = exclusion.detectorId ?? exclusion.exclusionReason ?? 'unspecified';
  const digest = exclusion.contentDigest === undefined ? 'never opened' : `digest ${shortDigest(exclusion.contentDigest)}`;
  return `<li data-polaris-exclusion="${escapeHtml(exclusion.repositoryRelativePath)}"${DISCLOSURE}><code>${escapeHtml(exclusion.repositoryRelativePath)}</code> — ${escapeHtml(exclusion.redactionClass)} by ${escapeHtml(why)}${exclusion.detail === undefined ? '' : ` (${escapeHtml(exclusion.detail)})`}; ${escapeHtml(digest)}; policy ${escapeHtml(exclusion.policyId)} ${escapeHtml(exclusion.policyVersion)}. ${copy('sentence.body-withheld')}</li>`;
}

function factItem(fact: ProjectShapeFact): string {
  const declarations = fact.fact.declarations
    .map((declaration) => `${escapeHtml(declaration.value)} (${escapeHtml(declaration.basis)}, ${declaration.anchors.map((anchor) => sourceRef(anchor.path, anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`)).join(', ')})`)
    .join('; ');
  return `<li id="polaris-fact-${escapeHtml(sourceSlug(fact.claim.claimId))}" data-polaris-fact="${escapeHtml(fact.claim.claimId)}"${DISCLOSURE}>${unknownRoutes(fact.claim, `${escapeHtml(fact.fact.fact)}: `)}<small>${copy('label.declarations-kept')} ${declarations}.</small><br>${claimTuple(fact.claim)}</li>`;
}

// ---------------------------------------------------------------------------
// The root index's own declarations (PWB-REQ-004 as amended; registry
// `observationGrammar`). Disclosed whether or not any fact needed them: the
// seven layer rows as admitted (or why the table is absent), the two stated
// summary counts (or why they are absent), and every disagreement one row
// decided, with the effective and superseded declarations both kept. A
// decided fact is already counted on its family's class or account
// statement, so it carries no claim tuple of its own here.

function declarationText(declaration: Declaration): string {
  const anchors = declaration.anchors.map((anchor) => sourceRef(anchor.path, anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`)).join(', ');
  return `${escapeHtml(declaration.value)} (${escapeHtml(declaration.basis)}, ${anchors})`;
}

function anchorRef(anchor: { readonly path: string; readonly line?: number }): string {
  return sourceRef(anchor.path, anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`);
}

function absenceText(disclosure: Extract<PrecedenceDisclosure | RootSummaryDisclosure, { kind: 'absent' | 'unknown' }>): string {
  if (disclosure.kind === 'unknown') return escapeHtml(disclosure.reason);
  const where = anchorRef(disclosure.line === undefined ? disclosure.anchor : { path: disclosure.anchor.path, line: disclosure.line });
  return `${escapeHtml(disclosure.reason)}${disclosure.detail === undefined ? '' : ` (${escapeHtml(disclosure.detail)})`} at ${where}`;
}

function precedenceBlock(precedence: PrecedenceDisclosure): string {
  if (precedence.kind !== 'admitted') {
    return `<p data-polaris-precedence="0"${DISCLOSURE}><span${copyAttr('sentence.no-precedence')}>${copy('sentence.no-precedence')}</span> ${absenceText(precedence)}.</p>`;
  }
  const rows = precedence.rules
    .map((rule) => `<tr data-polaris-precedence="${escapeHtml(rule.id)}"${FACT}><td>${rule.ordinal}</td><td>${escapeHtml(rule.layer)}</td><td>${escapeHtml(rule.owns)}</td><td><code>${escapeHtml(rule.home)}</code></td><td>${anchorRef(rule.anchor)}</td></tr>`)
    .join('');
  return `<p data-polaris-precedence="${precedence.rules.length}"${FACT}><small><span${copyAttr('label.precedence-rows')}>${copy('label.precedence-rows')}</span> ${precedence.rules.length} from ${anchorRef(precedence.anchor)}.</small></p>
    ${tableRegion('polaris-shape-root-index', `<table>
      <thead><tr>${(['table.index', 'table.layer', 'table.owns', 'table.home', 'table.declared-at'] as const).map((id) => `<th scope="col"${copyAttr(id)}>${copy(id)}</th>`).join('')}</tr></thead>
      <tbody>${rows}</tbody>
    </table>`)}`;
}

function rootSummaryBlock(summary: RootSummaryDisclosure): string {
  if (summary.kind !== 'emitted') {
    return `<p data-polaris-stated-counts="0"${DISCLOSURE}><span${copyAttr('sentence.no-stated-counts')}>${copy('sentence.no-stated-counts')}</span> ${absenceText(summary)}.</p>`;
  }
  const counts = summary.declarations.map((declaration) => `<span data-polaris-stated-count="${escapeHtml(declaration.fact)}">${escapeHtml(declaration.fact)} = ${declarationText(declaration)}</span>`).join('; ');
  return `<p data-polaris-stated-counts="${summary.declarations.length}"${FACT}><small><span${copyAttr('label.stated-counts')}>${copy('label.stated-counts')}</span> ${counts}.</small></p>`;
}

function citationText(citation: PrecedenceCitation): string {
  return `${escapeHtml(citation.ruleId)} (${escapeHtml(citation.layer)}, ${anchorRef(citation.anchor)})`;
}

function decidedItem(fact: ProjectShapeFact): string {
  if (fact.fact.state !== 'modeled' || fact.fact.disagreement === undefined) return '';
  const disagreement = fact.fact.disagreement;
  return `<li data-polaris-decided="${escapeHtml(fact.claim.claimId)}"${FACT}>${escapeHtml(fact.fact.fact)}: <span${copyAttr('label.effective')}>${copy('label.effective')}</span> ${declarationText(disagreement.effective)} by ${citationText(disagreement.precedence)}; <span${copyAttr('label.superseded')}>${copy('label.superseded')}</span> ${disagreement.superseded.map(declarationText).join('; ')}.</li>`;
}

function rootIndexSection(shape: Extract<ProjectShape, { kind: 'observed' }>): string {
  const decided = shape.facts.filter((fact) => fact.fact.state === 'modeled' && fact.fact.disagreement !== undefined);
  return `<section class="claim-section wide" data-polaris-section="shape:root-index">
    ${heading(3, 'polaris-shape-root-index', 'evidence.root-index')}
    ${precedenceBlock(shape.precedence)}
    ${rootSummaryBlock(shape.rootSummary)}
    ${decided.length === 0
      ? `<p data-polaris-decided-count="0"${copyAttr('sentence.no-decided')}>${copy('sentence.no-decided')}</p>`
      : `<p${FACT}><small${copyAttr('label.decided')}>${copy('label.decided')}</small></p><ul data-polaris-decided-count="${decided.length}">${decided.map(decidedItem).join('')}</ul>`}
  </section>`;
}

/** The Unknown reasons across every shape claim, counted and routed, with
 * `missing-declaration` foremost (RFC7-15) and `unconsented` next. */
function gapReasonCounts(claims: readonly ProjectShapeClaim[]): ReadonlyMap<string, number> {
  const counts = new Map<string, number>();
  for (const claim of claims) {
    if ('reasons' in claim.epistemic) {
      const reason = claim.epistemic.reasons.primary;
      counts.set(reason, (counts.get(reason) ?? 0) + 1);
    }
  }
  return counts;
}

function gapsList(claims: readonly ProjectShapeClaim[]): string {
  const counts = gapReasonCounts(claims);
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
    .map(([reason, count]) => `<li id="${gapId(reason)}" data-polaris-gap="${escapeHtml(reason)}"><span data-unknown-reason="${escapeHtml(reason)}">${escapeHtml(reason)}</span>: ${count} claim(s). ${copy('label.route')} ${reasonRouteHtml(reason)}</li>`)
    .join('')}</ul>`;
}

function countReasonsOf(claims: readonly ProjectShapeClaim[]): ReasonCounts {
  const primary: Record<string, number> = {};
  const secondary: Record<string, number> = {};
  for (const member of claims) {
    if (!('reasons' in member.epistemic)) continue;
    primary[member.epistemic.reasons.primary] = (primary[member.epistemic.reasons.primary] ?? 0) + 1;
    for (const reason of member.epistemic.reasons.secondary) secondary[reason] = (secondary[reason] ?? 0) + 1;
  }
  return { primary, secondary } as ReasonCounts;
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
  const counts = `${shape.counts.classification.classifiedByBasis.body} of ${shape.counts.sources} source bodies readable; ${shape.counts.classification.classifiedByBasis['path-only']} path-only source identities; ${shape.counts.items} items (${shape.counts.modeled} modeled, ${shape.counts.unknown} Unknown, ${shape.counts.contradicted} contradicted); ${shape.counts.facts} facts (${shape.counts.contradictedFacts} contradicted); ${shape.counts.exclusions} exclusion(s).`;
  const statement = `Declared project shape of ${identity.repositoryId} at revision ${identity.revision.slice(0, 12)}.`;
  const whole = shape.claim.epistemic.label === 'Observed'
    ? ((): string => {
        // The whole shape is anchored to the one evaluated tree; each source is
        // anchored individually in the sources table below.
        const block = anchoredBlock('block:claim:project-shape', [{
          claimId: shape.claim.claimId,
          anchors: [{ targetClass: 'evidence', targetId: `git-tree:${identity.revision}`, revision: identity.revision, locator: 'git-ls-tree' }],
          captured: capturedStateOf(shape.claim),
        }]);
        return `<p${block.attrs}><span data-claim-provenance="${escapeHtml(shape.claim.claimId)}">${escapeHtml(statement)}</span> <span class="citation">(<cite data-parity-field="shape-tree"${anchorAttrs(block.anchors[0] as NarrativeAnchor)}>git-ls-tree</cite>@<code data-parity-field="provenance-revision">${escapeHtml(identity.revision.slice(0, 12))}</code>)</span></p>`;
      })()
    : unknownRoutes(shape.claim, `${escapeHtml(statement)} `);
  return `<section class="claim-section" data-polaris-section="${escapeHtml(shape.claim.claimId)}">
    ${heading(3, 'polaris-shape-identity', 'evidence.observation')}
    ${whole}
    ${tupleLine(shape.claim)}
    ${reasonCountsBlock(shape.claim.claimId, countReasonsOf(shapeClaims(shape).slice(1)))}
    ${onDemandCounts(shape.claim.claimId, escapeHtml(counts))}
    <p${FACT}><small>Revision <code data-parity-field="shape-revision">${escapeHtml(identity.revision.slice(0, 12))}</code> (requested <code>${escapeHtml(identity.requestedRevision)}</code>), committed <code>${escapeHtml(identity.sourceClaimedInstant.instant)}</code>, captured <code>${escapeHtml(identity.capturedAt)}</code> by <code>${escapeHtml(identity.observer.observerId)}</code> ${escapeHtml(identity.observer.observerVersion)} under policy <code>${escapeHtml(identity.policy.policyId)}</code> ${escapeHtml(identity.policy.policyVersion)}; manifest <code data-parity-field="shape-manifest-digest">${escapeHtml(shortDigest(identity.manifestDigest))}</code>, observation <code data-parity-field="shape-observation-digest">${escapeHtml(shortDigest(identity.observationDigest))}</code>.</small></p>
    ${authorityLine(shape.authority)}
    ${discoveryLine(shape.discovery)}
    ${degradationLine(shape.degradation)}
  </section>
  <section class="claim-section wide" data-polaris-section="shape:sources">
    ${heading(3, 'polaris-shape-sources', 'evidence.sources')}
    <p${copyAttr('label.browse-source-records')}>${copy('label.browse-source-records')}</p>
    ${tableRegion('polaris-shape-sources', `<table><thead><tr>${(['table.index', 'table.source', 'table.items'] as const).map((id) => `<th scope="col"${copyAttr(id)}>${copy(id)}</th>`).join('')}</tr></thead><tbody>${shape.sources.map((source, index) => sourceRow(source, index, shape.identity.revision)).join('')}</tbody></table>`, ' data-source-index')}
  </section>
  <section class="claim-section" data-polaris-section="shape:exclusions">
    ${heading(3, 'polaris-shape-exclusions', 'evidence.exclusions')}
    ${shape.exclusions.length === 0 ? `<p data-polaris-exclusions="0"${copyAttr('sentence.no-exclusions')}>${copy('sentence.no-exclusions')}</p>` : population('exclusions', shape.claim.claimId, shape.exclusions.length, 'label.show-exclusions', `<ul data-polaris-exclusions="${shape.exclusions.length}">${shape.exclusions.map(exclusionItem).join('')}</ul>`)}
    ${shape.limitBreaches.length === 0 ? '' : `<p${FACT}><small>${copy('label.limit-breaches')} ${shape.limitBreaches.map((breach) => `${escapeHtml(breach.limit)} ${breach.observed} &gt; ${breach.declared}${breach.path === undefined ? '' : ` (${escapeHtml(breach.path)})`}`).join('; ')}.</small></p>`}
  </section>
  ${rootIndexSection(shape)}
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
// Capability deep dive (PWB-REQ-015; RFC7-17): argument, contract, reality.
// Proposed work (PWB-REQ-013) renders inside the contract band beside the
// current intent, as separate candidate futures that anchor nothing.

const SCOPE = roleAttr('scope-instruction');

function artifactCitation(artifact: ProposedWork['proposal']): string {
  return `<cite data-parity-field="provenance-source" data-proposal-artifact="${escapeHtml(artifact.digest)}">${escapeHtml(artifact.path)}</cite>@<code data-parity-field="provenance-revision">${escapeHtml(artifact.revision.slice(0, 12))}</code>`;
}

function unknownLine(marker: string, reason: string, route: string, detail: string): string {
  return `<p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(marker)}"${DISCLOSURE}>${copy('label.unknown')} — ${unknownReasonRef(reason)}. ${copy('label.route')} ${escapeHtml(route)}.<br><small>${escapeHtml(detail)}</small></p>`;
}

function verbatimSlot(dive: CapabilityDeepDive, resolution: VerbatimResolution | undefined, ledger: DeepDiveLedger): string {
  const marker = `${dive.capabilityId}/requirement-text`;
  const attrs = ledger.block('contract', `contract:${dive.capabilityId}/requirement-text`);
  const body = ((): string => {
    if (resolution === undefined) {
      const intent = dive.currentIntent;
      return intent.kind === 'unknown'
        ? unknownLine(marker, intent.reason, intent.route, intent.detail)
        : unknownLine(marker, 'reference-unresolvable', UNKNOWN_REASON_ROUTES['reference-unresolvable'], `The baseline spec ${intent.path} carries no captured identity to verify text against.`);
    }
    if (resolution.kind === 'not-rendered') return unknownLine(marker, resolution.reason, resolution.route, resolution.detail);
    // One block per selected requirement (PWB-REQ-011 as amended): the
    // requirement heading and its scenarios, byte-for-byte; nothing else of
    // the owning artifact reaches the page.
    return resolution.requirements
      .map((requirement) => `<pre class="verbatim" data-verbatim-text data-verbatim-requirement="${escapeHtml(requirement.title)}" data-verbatim-identity="${escapeHtml(resolution.identity)}"${roleAttr('project-fact', 'anchored-project-fact')}>${escapeHtml(requirement.text)}</pre>`)
      .join('\n');
  })();
  return `<section class="claim-section" data-contract-part="requirement-text" data-verbatim="${resolution?.kind === 'rendered' ? 'rendered' : 'not-rendered'}"${attrs}>
      ${heading(4, `polaris-${dive.capabilityId}-requirement-text`, 'label.requirement-text')}
      <p class="lede"${copyAttr('contract.verbatim-lede')}>${copy('contract.verbatim-lede')}</p>
      ${body}
    </section>`;
}

function currentIntentPart(dive: CapabilityDeepDive, revision: string, resolution: VerbatimResolution | undefined, ledger: DeepDiveLedger): string {
  const current = dive.currentIntent;
  const identity = current.kind === 'baseline-spec'
    ? ((): string => {
        const block = anchoredBlock(`block:${dive.capabilityId}/current-authority`, [{
          claimId: current.claim.claimId,
          anchors: current.claim.support.map((support) => supportAnchor(support, revision, 'requirement')).filter((anchor): anchor is AnchorInput => anchor !== undefined),
          captured: capturedStateOf(current.claim),
        }]);
        return `<p${block.attrs}><span data-claim-provenance="${escapeHtml(current.claim.claimId)}"><code data-parity-field="current-authority-path">${escapeHtml(current.path)}</code></span>${supportCitations(current.claim.support, block.anchors)}${((): string => { const leaf = currentIntentLeaf(current, revision); return leaf !== undefined && activeExactSources.has(leaf.identity) ? ` ${exactTextLink(leaf.identity)}` : ''; })()}</p>
      ${tupleLine(current.claim)}`;
      })()
    : unknownLine(`${dive.capabilityId}/current-authority`, current.reason, current.route, current.detail);
  const adoption = dive.adoption.kind === 'unknown'
    ? unknownLine(`${dive.capabilityId}/adoption`, dive.adoption.reason, dive.adoption.route, dive.adoption.detail)
    : `<p${FACT}>${copy('label.adoption')} <span data-capability-adoption-state="${dive.adoption.kind}">${copy(dive.adoption.kind === 'adopted' ? 'adoption.adopted' : 'adoption.draft')}</span> — ${escapeHtml(dive.adoption.basis)}</p>`;
  return `<section class="claim-section" data-proposed-work-part="current-authority"${ledger.block('contract', `contract:${dive.capabilityId}/current-authority`)}>
      ${heading(4, `polaris-${dive.capabilityId}-current`, 'proposed.current')}
      ${identity}
      ${adoption}
    </section>
    ${verbatimSlot(dive, resolution, ledger)}`;
}

/** One proposal: adjacent to the current intent, labeled, non-anchorable and
 * non-status-bearing. It registers no narrative block and carries no anchor. */
function proposalPart(dive: CapabilityDeepDive, work: ProposedWork, ledger: DeepDiveLedger): string {
  const exclusive = exclusiveWith(dive, work.changeId);
  const lifecycle = work.lifecycle.kind === 'observed'
    ? `<p${FACT}>${copy('label.lifecycle')} <span data-proposal-lifecycle-state="${escapeHtml(work.lifecycle.state)}">${escapeHtml(work.lifecycle.state)}</span> — ${escapeHtml(work.lifecycle.basis)}</p>`
    : `<p class="unknown-disclosure" data-unknown-disclosure="${escapeHtml(work.id)}/lifecycle"${DISCLOSURE}>${copy('label.lifecycle')} ${copy('label.unknown')} — ${escapeHtml(work.lifecycle.reason)}</p>`;
  const futures = exclusive.length === 0
    ? `<p${FACT}>${copy('label.candidate-future')} — ${copy(dive.exclusivityBasis === 'declared' ? 'sentence.no-competitor' : 'sentence.exclusivity-not-captured')}</p>`
    : `<p${FACT}>${copy('label.candidate-future')} — ${copy('label.exclusive-with')} ${exclusive.map((other) => `<code data-exclusive-change="${escapeHtml(other)}">${escapeHtml(other)}</code>`).join(', ')}. ${copy('sentence.separate-futures')}</p>`;
  const attrs = ledger.block('contract', `contract:${dive.capabilityId}/proposal:${work.changeId}`);
  return `<section class="claim-section proposal" data-proposed-work-part="proposal" data-candidate-future="${escapeHtml(work.changeId)}" data-exclusive-with="${escapeHtml(exclusive.join('\t'))}" data-anchorable="false" data-status-bearing="false"${attrs}>
      ${heading(4, `polaris-proposed-${work.changeId}`, 'proposed.change')}
      <p class="proposal-label" data-proposal-label${copyAttr('label.proposed')}>${copy('label.proposed')}</p>
      <p${FACT}><span data-proposal-identity="${escapeHtml(work.id)}"><code data-parity-field="proposal-change-id">${escapeHtml(work.changeId)}</code> ${copy('label.amends')} <code>openspec/specs/${escapeHtml(work.specKey)}/spec.md</code>.</span> <span class="citation">(${artifactCitation(work.proposal)}, ${artifactCitation(work.delta)})</span></p>
      ${lifecycle}
      ${futures}
    </section>`;
}

function proposedWorkSection(dive: CapabilityDeepDive, revision: string, resolution: VerbatimResolution | undefined, ledger: DeepDiveLedger): string {
  const changeIds = dive.proposals.map((work) => work.changeId);
  const lifecycles = dive.proposals.map((work) => (work.lifecycle.kind === 'observed' ? work.lifecycle.state : 'unknown'));
  const single = dive.proposals.length === 1 ? ` data-proposal-change="${escapeHtml(changeIds[0] as string)}" data-proposal-lifecycle="${escapeHtml(lifecycles[0] as string)}"` : '';
  return `<section class="claim-section"${ledger.block('contract', `contract:${dive.capabilityId}/proposed-work`)} data-proposal-changes="${escapeHtml(changeIds.join('\t'))}" data-proposal-count="${dive.proposals.length}"${single} data-proposal-capability="${escapeHtml(dive.capabilityId)}" data-exclusivity-basis="${dive.exclusivityBasis}">
    ${heading(3, `polaris-${dive.capabilityId}-proposed-work`, 'proposed.heading')}
    <div class="adjacent">
      ${currentIntentPart(dive, revision, resolution, ledger)}
      ${dive.proposals.map((work) => proposalPart(dive, work, ledger)).join('')}
    </div>
  </section>`;
}

function undeclaredContractPart(dive: CapabilityDeepDive, part: 'doctrine' | 'non-goals', shape: ProjectShape, ledger: DeepDiveLedger): string {
  const reason = shape.kind === 'observed'
    ? 'missing-declaration'
    : ('reasons' in shape.claim.epistemic ? shape.claim.epistemic.reasons.primary : 'unconsented-source-or-provider');
  const detail = shape.kind === 'observed'
    ? `The consented sources declare no ${part === 'doctrine' ? 'doctrine' : 'non-goal'} link for ${dive.capabilityId}; none is restated here.`
    : `The project shape is ${shape.kind}; no declaration was read.`;
  return `<section class="claim-section" data-contract-part="${part}"${ledger.block('contract', `contract:${dive.capabilityId}/${part}`)}>
      ${heading(4, `polaris-${dive.capabilityId}-${part}`, part === 'doctrine' ? 'label.doctrine' : 'label.non-goals')}
      ${unknownLine(`${dive.capabilityId}/${part}`, reason, UNKNOWN_REASON_ROUTES[reason as keyof typeof UNKNOWN_REASON_ROUTES] ?? 'No route recorded', detail)}
    </section>`;
}

function bandHeader(band: DeepDiveBand, dive: CapabilityDeepDive): string {
  return `${heading(3, `polaris-${dive.capabilityId}-band-${band}`, `band.${band}`)}
    <p class="lede"${copyAttr(`band.${band}-lede`)}>${copy(`band.${band}-lede`)}</p>`;
}

function entityLink(entity: PocEntity): string {
  return `<a href="#polaris-${escapeHtml(entity.id)}" data-argument-ref="${escapeHtml(entity.id)}">${escapeHtml(entity.title)}</a>`;
}

function argumentBand(dive: CapabilityDeepDive, ledger: DeepDiveLedger): string {
  const intents = dive.related.filter((entity) => entity.kind === 'intent');
  const why = intents.length === 0
    ? `<p${FACT}>${copy('label.why')} — ${copy('sentence.no-intent-declared')}</p>`
    : `<p${FACT}>${copy('label.why')} — ${intents.map(entityLink).join(', ')}. <a href="#polaris-group-overview" data-argument-ref="group:overview">${copy('group.overview')}</a>.</p>`;
  return `<section class="band"${ledger.block('argument', `argument:${dive.capabilityId}`)}>
      ${bandHeader('argument', dive)}
      <p${FACT}>${copy('label.thesis')} — ${escapeHtml(dive.capability.title)}.</p>
      ${why}
      <p${FACT}>${copy('label.related')} — ${dive.related.filter((entity) => entity.kind !== 'intent' && entity.kind !== 'project').map(entityLink).join(', ')}.</p>
    </section>`;
}

function contractBand(dive: CapabilityDeepDive, model: PocModel, revision: string, resolution: VerbatimResolution | undefined, ledger: DeepDiveLedger): string {
  return `<section class="band"${ledger.block('contract', `contract:${dive.capabilityId}`)}>
      ${bandHeader('contract', dive)}
      ${proposedWorkSection(dive, revision, resolution, ledger)}
      ${undeclaredContractPart(dive, 'doctrine', model.projectShape, ledger)}
      ${undeclaredContractPart(dive, 'non-goals', model.projectShape, ledger)}
    </section>`;
}

function realityBand(dive: CapabilityDeepDive, model: PocModel, ledger: DeepDiveLedger): string {
  const entitiesById = new Map(model.entities.map((entity) => [entity.id, entity]));
  const sections = model.entities
    .filter((entity) => entity.id === dive.capabilityId || dive.related.some((related) => related.id === entity.id))
    .map((entity) => entitySection(entity, ledger.block('reality', entity.id)))
    .join('');
  const relationshipList = dive.relationships.map((relationship) => relationshipBullet(relationship, entitiesById)).join('');
  return `<section class="band"${ledger.block('reality', `reality:${dive.capabilityId}`)}>
      ${bandHeader('reality', dive)}
      ${sections}
      <section class="relationships"${ledger.block('reality', 'relationships')}>
        ${heading(3, 'polaris-relationships', 'evidence.relationships')}
        <p class="relationships-lede"${copyAttr('evidence.relationships-lede')}>${copy('evidence.relationships-lede')}</p>
        <ul>${relationshipList}</ul>
      </section>
    </section>`;
}

/** One capability deep dive: the three bands in order, Base mode, every
 * block under exactly one band, the machine form registered beside the
 * narrative. Verbatim text is resolved here, at render, and never stored. */
function capabilityDeepDive(dive: CapabilityDeepDive, model: PocModel, revision: string, verbatim: VerbatimLeafReader | undefined): string {
  const ledger = new DeepDiveLedger(escapeHtml);
  const leaf = currentIntentLeaf(dive.currentIntent, revision);
  const resolution = leaf === undefined ? undefined : resolveVerbatim(leaf, verbatim);
  const bands = `${argumentBand(dive, ledger)}${contractBand(dive, model, revision, resolution, ledger)}${realityBand(dive, model, ledger)}`;
  registry().registerDeepDive(deepDiveMachineForm(dive, ledger, { ...(leaf === undefined ? {} : { leaf }), ...(resolution === undefined ? {} : { resolution }) }));
  return `<section class="deep-dive" id="polaris-deep-dive-${escapeHtml(sourceSlug(dive.capabilityId))}" data-capability-deep-dive="${escapeHtml(dive.capabilityId)}" data-reading-mode="${DEFAULT_READING_MODE}" data-capability-adoption="${dive.adoption.kind}">
      <p${SCOPE}>${copy('label.mode')} <span data-reading-mode-value="${DEFAULT_READING_MODE}">${DEFAULT_READING_MODE}</span> — ${copy('sentence.base-mode')}</p>
      ${bands}
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
      return `${capabilityGuide(shape)}${accountByKey(shape, 'v1-scope')}${accountByKey(shape, 'v1-success')}${classBlock(shape, 'success-criterion', true)}`;
    case 'catalog':
      return CATALOG_CLASSES.map((cls) => classBlock(shape, cls, true)).join('');
  }
}

const SECTION_NAV_SCRIPT = `<script>
(() => {
  const drawer = document.querySelector('.reading-sidebar .contents-list');
  if (!drawer) return;
  const wide = matchMedia('(min-width: 1000px)');
  const adapt = () => { drawer.open = wide.matches; };
  adapt();
  wide.addEventListener('change', adapt);
  document.querySelector('.reading-sidebar').addEventListener('click', (event) => {
    if (event.target instanceof Element && event.target.closest('a') && !wide.matches) drawer.open = false;
  });
  document.addEventListener('DOMContentLoaded', () => {
    const openGuide = (hash) => {
      let id;
      try { id = decodeURIComponent(hash.slice(1)); } catch { return; }
      const guide = document.getElementById(id);
      if (guide && guide.matches('[data-component-guide]')) guide.querySelector('details').open = true;
    };
    document.addEventListener('click', (event) => {
      const link = event.target instanceof Element ? event.target.closest('a[href^="#polaris-guide-"]') : null;
      if (link) openGuide(link.hash);
    });
    addEventListener('hashchange', () => openGuide(location.hash));
    openGuide(location.hash);
    for (const library of document.querySelectorAll('.component-library')) {
      const button = library.querySelector('.expand-declaration');
      const sections = Array.from(library.querySelectorAll('[data-component-guide] > details'));
      button.addEventListener('click', () => {
        const open = !sections.every((section) => section.open);
        for (const section of sections) section.open = open;
        button.setAttribute('aria-expanded', String(open));
      });
      library.addEventListener('toggle', () => button.setAttribute('aria-expanded', String(sections.every((section) => section.open))), true);
    }
    const headings = Array.from(document.querySelectorAll('h2[id^="polaris-group-"]'));
    const links = Array.from(drawer.querySelectorAll('a'));
    let queued = false;
    const update = () => {
      queued = false;
      let active = headings[0];
      for (const heading of headings) {
        if (heading.getBoundingClientRect().top <= 160) active = heading;
      }
      for (const link of links) {
        if (active && link.hash === '#' + active.id) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    };
    addEventListener('scroll', () => {
      if (!queued) { queued = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  });
})();
</script>`;

const POLARIS_STYLE = `
  html { scroll-behavior: auto; }
  .band { max-width: 74ch; margin: 0 auto 2rem; padding: 0.5rem 0 0; border-left: 3px solid var(--line); padding-left: 1rem; }
  .band[data-band="argument"] { border-left-style: dotted; }
  .band[data-band="contract"] { border-left-style: double; }
  .verbatim { white-space: pre-wrap; border: 1px solid var(--line); padding: 0.75rem; overflow-x: auto; }
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
  .reason-counts { font-size: .95rem; }
  .reason-counts ul { padding-left: 1.2rem; }
  .coverage-counts { margin: .6rem 0 1rem; }
  .coverage-counts summary { cursor: pointer; color: var(--muted); font-size: .9rem; }
  .population { margin: .6rem 0 1rem; }
  .population summary, .claim-states summary { cursor: pointer; color: var(--muted); font-size: .95rem; }
  .claim-states { max-width: 74ch; margin: 0 auto 2rem; padding: .5rem 1rem; border: 1px dashed var(--line); font-size: .95rem; }
  .claim-states ul { padding-left: 1.2rem; }
  .unknown-disclosure { color: var(--unknown); border-left: 3px solid var(--unknown); padding-left: .9rem; }
  .table-scroll { overflow-x: auto; }
  .depth-nav { max-width: 74ch; margin: 0 auto 2rem; font-size: .95rem; }
  .depth-nav p { margin: 0 0 .3rem; }
  .depth-nav ol { margin: 0; padding-left: 1.4rem; }
  .depth-nav li { margin-bottom: .3rem; }
  .relationships { max-width: 74ch; margin: 0 auto 3rem; }
  .relationships ul { padding-left: 1.2rem; }
  .relationships li { margin-bottom: .5rem; }
  .proposal { border-left: 4px solid var(--unknown); padding-left: 1rem; }
  .proposal-label { font-family: var(--font-mono); font-size: .85rem; letter-spacing: .04em; text-transform: uppercase; color: var(--unknown); }
  .proposal .adjacent { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr)); }
  .proposal h4 { margin: 0 0 .5rem; font-size: 1.05rem; }

  header { width: min(74ch, calc(100% - 2rem)); padding: 2.8rem 0 1rem; }
  header h1 { font-size: clamp(3.5rem, 7vw, 5.5rem); line-height: 1; margin-block: .7rem 1.4rem; }
  header .lede { max-width: 48ch; font-size: 1.25rem; line-height: 1.6; }
  main > .legend { max-width: 74ch; margin: 1.25rem auto 2rem; gap: .5rem 1rem; }
  main > .notice { max-width: 74ch; margin: 0 auto 2rem; background: transparent; border-left: 1px solid var(--line); font-size: .9rem; color: var(--muted); }
  .group { margin-top: 4rem; padding: 1.5rem 0 0; border-top: 1px solid var(--line); }
  .group h2 { font-size: clamp(2rem, 4vw, 3rem); line-height: 1.15; letter-spacing: -.025em; }
  .claim-section { border: 0; margin-bottom: 2.5rem; padding-top: .7rem; }
  .claim-section h3 { font-size: 1.05rem; color: var(--muted); font-weight: normal; letter-spacing: .02em; }
  .reading-prose { max-width: 66ch; font-size: 1.12rem; line-height: 1.75; overflow-wrap: anywhere; }
  .reading-prose p { font-size: inherit; margin: 0 0 1.2em; }
  .reading-prose h4, .reading-prose h5, .reading-prose h6 { font-size: 1.3rem; line-height: 1.3; margin: 2rem 0 .8rem; color: var(--ink); }
  .reading-prose ul, .reading-prose ol { padding-left: 1.4rem; margin: .5rem 0 1.5rem; }
  .reading-prose li { margin-bottom: .7rem; padding-left: .2rem; }
  .reading-prose li p { margin-bottom: .3rem; }
  .reading-prose strong { font-weight: bold; color: var(--ink); }
  .reading-prose code { font-size: .84em; color: var(--cyan); }
  .reading-prose pre { max-width: 100%; overflow-x: auto; padding: 1rem; background: var(--panel); line-height: 1.5; }
  .reading-prose blockquote { border-left: 2px solid var(--cyan); margin: 1rem 0; padding-left: 1.3rem; font-size: 1.2em; }
  .markdown-table { overflow-x: auto; margin-block: 1.5rem; }
  main, footer { overflow-wrap: anywhere; }
  :target { scroll-margin-top: 5rem; }
  .reading-citations { margin-block: .5rem; font-size: .85rem; }
  .class-provenance { font-size: .85rem; margin-block: .7rem; }
  .class-provenance > summary { cursor: pointer; color: var(--muted); }
  .reading-citations > summary { cursor: pointer; color: var(--muted); }
  .excerpt-label { color: var(--muted); font-size: .85rem !important; }
  main > .group:first-of-type { margin-top: 1rem; }
  .reading-citations .citation { font-size: .72rem; overflow-wrap: anywhere; }
  .tuple-line { margin-top: .7rem; }
  .claim-tuple { letter-spacing: 0; font-size: .72rem; }
  .full-account { border-left: 1px solid var(--line); padding: .6rem 0 .6rem 1.2rem; margin: 1.5rem 0; }
  .full-account > summary { cursor: pointer; color: var(--cyan); }
  .full-account[open] > summary { margin-bottom: 1.3rem; }
  .depth-nav { position: static; border: 0; background: transparent; backdrop-filter: none; padding: 0; font-family: var(--font-serif); }
  .contents-list { border-block: 1px solid var(--line); padding: 1rem 0; }
  .contents-list > summary { cursor: pointer; color: var(--cyan); font-size: 1rem; }
  .contents-list ol { margin: 1rem 0 0; padding-left: 1.4rem; }
  .contents-list li { margin: .75rem 0; line-height: 1.7; }
  .guide-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem 2rem; }
  .capability-guide { max-width: 74ch; margin: 1.5rem auto 3rem; }
  .guide-entry { border-top: 1px solid var(--line); padding-top: 1rem; }
  .guide-entry h4 { font-size: 1.35rem; margin: 0 0 .75rem; }
  .guide-entry .reading-prose { font-size: 1rem; line-height: 1.6; }
  .guide-intro { color: var(--muted); }
  .guide-state { color: var(--muted); font-size: .75rem; }
  .guide-state > summary, .unknown-source-details > summary { cursor: pointer; }
  .unknown-disclosure > p { margin: 0 0 .5rem; }
  .unknown-source-details, .reason-remedies { font-size: .9rem; }
  .reason-remedies > summary { cursor: pointer; color: var(--muted); }
  .quick-links { display: flex; gap: 1.5rem; margin: 0 0 .5rem; font-size: .95rem; }
  .catalog-contexts { columns: 2; column-gap: 2.5rem; padding-left: 1.2rem; font-size: 1.15rem; line-height: 1.5; }
  .catalog-contexts li { break-inside: avoid; margin-bottom: .8rem; }
  .population { border-block: 1px solid var(--line); padding: .75rem 0; }
  .population > summary { font-size: 1rem; color: var(--cyan); }
  .population[open] > summary { margin-bottom: 1rem; }
  [data-source-index] { max-height: min(70vh, 30rem); overflow: auto; }
  [data-source-index] td:first-child { white-space: nowrap; }
  .source-record { margin-top: .45rem; }
  .source-record dt { font-weight: 600; margin-top: .45rem; }
  .source-record dd { margin-left: 0; }
  .population .reading-prose { font-size: 1rem; min-width: 22ch; }
  .population .reading-prose p:last-child { margin-bottom: 0; }
  .claim-states { border: 0; border-left: 1px solid var(--line); padding: .3rem 1rem; }
  .reading-layout { display: grid; grid-template-columns: 14rem minmax(0, 1fr); grid-template-areas: "sidebar header" "sidebar content" "sidebar footer"; column-gap: clamp(2rem, 4vw, 4rem); max-width: 96rem; padding-inline: clamp(1rem, 3vw, 3rem); margin-inline: auto; }
  .reading-sidebar { grid-area: sidebar; position: sticky; top: 5rem; align-self: start; max-height: calc(100vh - 6rem); overflow: auto; margin-top: 3rem; padding-right: .75rem; }
  .reading-layout > header { grid-area: header; }
  .reading-layout > main { grid-area: content; }
  .reading-layout > footer { grid-area: footer; }
  .reading-layout > header, .reading-layout > main, .reading-layout > footer { min-width: 0; width: 100%; margin-inline: 0; }
  .reading-layout .group, .reading-layout .claim-section, .reading-layout .band, .reading-layout .relationships, .reading-layout .capability-guide, .reading-layout .scope-instruction, .reading-layout .claim-states { max-width: 91ch; margin-left: 0; }
  .reading-layout .claim-section.wide { max-width: none; }
  .reading-prose { max-width: 74ch; }
  .reading-prose .source-flow { display: grid; grid-template-columns: repeat(var(--flow-columns), minmax(0, 1fr)); gap: 1.3rem; list-style: none; padding: 1.25rem 0; margin: 1.5rem 0; }
  .source-flow li { position: relative; min-width: 0; padding: 0; margin: 0; }
  .flow-node { display: block; height: 100%; border: 1px solid var(--line); border-top: 2px solid var(--cyan); background: var(--panel); padding: .75rem .5rem; font: .85rem var(--font-mono); text-transform: capitalize; }
  .flow-arrow { position: absolute; top: 50%; right: -1.3rem; width: 1.3rem; text-align: center; transform: translateY(-50%); font-size: 0; }
  .flow-arrow::after { content: '→'; font-size: 1.2rem; color: var(--muted); }
  .reading-prose .source-flow[data-flow-long] { grid-template-columns: 1fr; }
  .source-flow[data-flow-long] .flow-arrow { top: auto; right: calc(50% - .65rem); bottom: -1.3rem; height: 1.3rem; transform: none; }
  .source-flow[data-flow-long] .flow-arrow::after { content: '↓'; }
  @media (max-width: 800px) {
    .reading-prose .source-flow { grid-template-columns: 1fr; }
    .source-flow .flow-arrow { top: auto; right: calc(50% - .65rem); bottom: -1.3rem; height: 1.3rem; transform: none; }
    .source-flow .flow-arrow::after { content: '↓'; }
  }
  .source-relationships { display: grid; gap: 1rem; margin-block: 1.5rem; }
  .source-relationship { border: 1px solid var(--line); background: var(--panel); padding: 1.25rem; }
  .relationship-nodes { display: grid; grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr); align-items: center; gap: 1rem; font-size: 1rem; }
  .relationship-nodes > strong { padding: .6rem; border-bottom: 2px solid var(--line); }
  .relationship-arrow { color: var(--muted); font-size: 1.5rem; }
  .relationship-description { margin-top: 1rem; font-size: .95rem; }
  .relationship-description p:last-child { margin-bottom: 0; }
  .component-library { margin-block: 2rem; }
  .component-library > h4 { font-size: 1.4rem; margin-bottom: .75rem; }
  .expand-declaration { background: transparent; border: 1px solid var(--line); color: var(--cyan); padding: .6rem .9rem; cursor: pointer; margin-bottom: 1rem; font: inherit; }
  .component-guides { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }
  [data-component-guide] { min-width: 0; border: 1px solid var(--line); background: var(--panel); padding: 1rem; }
  [data-component-guide]:has(details[open]) { grid-column: 1 / -1; }
  [data-component-guide] summary { cursor: pointer; font-size: 1.1rem; line-height: 1.5; }
  [data-component-guide] details[open] > summary { margin-bottom: 1.5rem; }


  .reading-sidebar .quick-links { flex-wrap: wrap; gap: .6rem 1rem; }
  .reading-sidebar .contents-list { border-top: 0; }
  .reading-sidebar .contents-list ol, .reading-sidebar .contents-list ul { list-style: none; padding: 0; }
  .reading-sidebar .contents-list > ol > li { margin: 1.25rem 0; }
  .reading-sidebar .contents-list ul { margin: .4rem 0 0; }
  .reading-sidebar .contents-list ul li { margin: .15rem 0; line-height: 1.4; }
  .depth-group-label { color: var(--muted); font: .7rem var(--font-mono); text-transform: uppercase; letter-spacing: .08em; }
  .reading-sidebar .contents-list a { display: block; padding: .35rem .5rem; border-left: 2px solid transparent; text-decoration: none; }
  .reading-sidebar .contents-list a[aria-current="location"] { color: var(--ink); border-color: var(--cyan); background: var(--panel); }
  @media (max-width: 999px) {
    .reading-layout { display: block; padding-inline: 1rem; }
    .reading-sidebar { position: static; max-height: none; margin-top: 1rem; padding: 0; }
    .reading-sidebar .depth-nav { max-width: none; margin-bottom: 0; }
    .reading-sidebar .contents-list { border-block: 1px solid var(--line); }
    .reading-sidebar .contents-list > ol { columns: 2; column-gap: 2rem; }
    .reading-sidebar .contents-list > ol > li { break-inside: avoid; }
  }
  @media (max-width: 640px) {
    header { padding-top: 2.5rem; }
    .reading-sidebar .contents-list > ol { columns: 1; }
    .catalog-contexts { columns: 1; }
    .component-guides { grid-template-columns: 1fr; }
    .guide-grid { grid-template-columns: 1fr; }
    .site-nav ul { gap: 1rem; font-size: .85rem; }
    .reading-prose { font-size: 1.05rem; }
    .group { margin-top: 3rem; }
  }
`;

/** Seam for the PWB-REQ-015 sweep: one deep dive rendered on its own with a
 * fresh registry, so a fixture dive (draft capability, competing proposals)
 * can be exercised without a model that carries it. Returns the fragment and
 * the machine form the page would embed. */
export function renderCapabilityDeepDive(dive: CapabilityDeepDive, model: PocModel, inputs: PolarisRenderInputs = {}): { readonly html: string; readonly narrative: ReturnType<NarrativeRegistry['narrative']> } {
  if (activeRegistry !== undefined) throw new Error('renderPolarisPage re-entered');
  activeRegistry = new NarrativeRegistry();
  try {
    const shape = model.projectShape;
    const html = capabilityDeepDive(dive, model, shape.kind === 'observed' ? shape.identity.revision : '', inputs.verbatim);
    return { html, narrative: activeRegistry.narrative() };
  } finally {
    activeRegistry = undefined;
  }
}

/** Render-time inputs that are not truth: a verbatim reader for the current
 * requirement leaf (production passes none — the leaf lies outside the
 * consented content class, and the page says so). */
export interface PolarisRenderInputs {
  readonly verbatim?: VerbatimLeafReader;
}

/** The presentation artifact and its machine form, from one capture: the
 * human page and the envelope `/api/poc/polaris` serves derive from the
 * same registry, so their block, anchor and band multisets are one. */
export function renderPolarisPresentation(model: PocModel, mountPrefix = '', viewState: PolarisViewState = {}, inputs: PolarisRenderInputs = {}): { readonly html: string; readonly narrative: ReturnType<NarrativeRegistry['narrative']> } {
  if (activeRegistry !== undefined) throw new Error('renderPolarisPage re-entered');
  activeRegistry = new NarrativeRegistry();
  activeViewState = viewState;
  try {
    const html = renderPolarisBody(model, mountPrefix, activeRegistry, inputs);
    return { html, narrative: activeRegistry.narrative() };
  } finally {
    activeRegistry = undefined;
    activeViewState = {};
    activeTargets = NO_TARGETS;
    activeMountPrefix = '';
    activeExclusions = [];
    activeUnavailable = [];
    activeExactSources = new Set();
  }
}

export function renderPolarisPage(model: PocModel, mountPrefix = '', viewState: PolarisViewState = {}, inputs: PolarisRenderInputs = {}): string {
  return renderPolarisPresentation(model, mountPrefix, viewState, inputs).html;
}

/** The four depths PWB-REQ-011 names — summary, catalog, detail, exact
 * source — as one list of native links in document order, so a keyboard-
 * only reader descends by text alone. Every target is an id the same render
 * emits; a level lists only what this shape state renders. */
function depthNav(shape: ProjectShape, dives: readonly CapabilityDeepDive[]): string {
  const observed = shape.kind === 'observed';
  const revision = observed ? shape.identity.revision : '';
  const architecture = observed ? shape.projectAccount.find((statement) => statement.key === 'architecture' && statement.claim.epistemic.label === 'Observed')?.statement : undefined;
  const chapters = architecture === undefined ? [] : projectReading(architecture, 'architecture').chapters ?? [];
  const link = (id: string, copyId: PolarisCopyId): string => `<a href="#${escapeHtml(id)}"${copyAttr(copyId)}>${copy(copyId)}</a>`;
  const levels: readonly (readonly [PolarisCopyId, readonly string[]])[] = [
    ['depth.summary', [link('polaris-group-overview', 'group.overview'), link('polaris-group-boundaries', 'group.boundaries'), link('polaris-group-v1', 'group.v1'), link('polaris-group-architecture', 'group.architecture')]],
    ['depth.catalog', [link('polaris-group-catalog', 'group.catalog'), ...(observed ? CATALOG_CLASSES.map((cls) => link(`polaris-class-${cls}`, `class.${cls}`)) : [])]],
    ['depth.detail', [...chapters.map((chapter) => `<a href="#polaris-guide-${escapeHtml(chapter.id)}"${FACT}>${escapeHtml(chapter.title)}</a>`), link('polaris-group-capability-detail', 'group.capability-detail'), ...dives.map((dive) => `<a href="#polaris-deep-dive-${escapeHtml(sourceSlug(dive.capabilityId))}" data-depth-dive="${escapeHtml(dive.capabilityId)}"${FACT}>${escapeHtml(dive.capability.title)}</a>`)]],
    ['depth.source', [
      link('polaris-group-evidence-and-gaps', 'group.evidence-and-gaps'),
      link('polaris-shape-sources', 'evidence.sources'),
      ...(observed ? [link('polaris-shape-exclusions', 'evidence.exclusions'), link('polaris-shape-root-index', 'evidence.root-index'), link('polaris-shape-contradictions', 'evidence.contradictions')] : []),
      link('polaris-shape-gaps', 'evidence.gaps'),
      ...dives.flatMap((dive) => {
        const leaf = currentIntentLeaf(dive.currentIntent, revision);
        return leaf !== undefined && activeExactSources.has(leaf.identity)
          ? [`<a href="${escapeHtml(sourceRouteHref(activeMountPrefix, leaf.identity))}" data-depth-source="${escapeHtml(dive.capabilityId)}"${copyAttr('label.exact-text')}>${copy('label.exact-text')}</a>`]
          : [];
      }),
    ]],
  ];
  return `<nav class="depth-nav" data-polaris-depth-nav aria-labelledby="polaris-depth-label"><p class="quick-links"${SCOPE}><a href="#polaris-group-v1"${copyAttr('label.capabilities')}>${copy('label.capabilities')}</a>${observed ? ` <a href="#polaris-account-purpose"${copyAttr('label.terminology')}>${copy('label.terminology')}</a>` : ''}</p>
    <details class="contents-list"><summary id="polaris-depth-label"${SCOPE}>${copy('depth.label')}</summary>
    <ol>${levels.map(([copyId, links], index) => `<li data-depth-level="${index + 1}"${SCOPE}><span class="depth-group-label"${copyAttr(copyId)}>${copy(copyId)}</span><ul>${links.map((item) => `<li>${item}</li>`).join('')}</ul></li>`).join('')}</ol></details>
  </nav>`;
}

function pageTargets(shape: ProjectShape): PageTargets {
  return {
    gapReasons: new Set(gapReasonCounts(shapeClaims(shape)).keys()),
    sourcePaths: new Set(shape.kind === 'observed' ? shape.sources.map((source) => source.path) : []),
  };
}

/** Identities the exact-source route serves for this shape: the reader's
 * own admission gates restated as a set (an admitted baseline spec whose
 * identity was classified — path-only, its body is read only at render —
 * and whose anchor is a blob), so the page links only where the route can
 * resolve. */
export function exactSourceIdentities(shape: ProjectShape): ReadonlySet<string> {
  if (shape.kind !== 'observed') return new Set();
  return new Set(shape.sources
    .filter((source) => source.rule === 'baseline-spec-tree' && source.record.outcome === 'classified' && source.anchor.kind === 'blob')
    .map((source) => source.identity));
}

function renderPolarisBody(model: PocModel, mountPrefix: string, narrative: NarrativeRegistry, inputs: PolarisRenderInputs): string {
  const shape = model.projectShape;
  const revision = shape.kind === 'observed' ? shape.identity.revision : '';
  activeTargets = pageTargets(shape);
  activeMountPrefix = mountPrefix;
  activeExclusions = shape.kind === 'observed' ? shape.exclusions : [];
  activeUnavailable = shape.kind === 'observed'
    ? shape.sources.flatMap((source) => (source.record.outcome === 'unavailable' ? [{ path: source.path, reason: source.record.reason }] : []))
    : [];
  activeExactSources = exactSourceIdentities(shape);
  const dives = deriveCapabilityDeepDives(model);
  const deepDives = dives
    .map((dive) => capabilityDeepDive(dive, model, revision, inputs.verbatim))
    .join('');

  const body = `
    ${groupHeader('overview')}
    ${projectGroupBody(shape, 'overview')}
    <p class="notice"${copyAttr('notice')}>${copy('notice')} <a href="#polaris-claim-states"${copyAttr('label.claim-states')}>${copy('label.claim-states')}</a></p>
    ${claimStatesBlock()}
    ${groupHeader('boundaries')}
    ${projectGroupBody(shape, 'boundaries')}
    ${groupHeader('v1')}
    ${projectGroupBody(shape, 'v1')}
    ${groupHeader('architecture')}
    ${projectGroupBody(shape, 'architecture')}
    ${groupHeader('catalog')}
    ${projectGroupBody(shape, 'catalog')}
    ${groupHeader('capability-detail')}
    <p class="scope-instruction" data-polaris-capability-scope data-scope="poc-bound"${copyAttr('capability.scope')}>${copy('capability.scope')}</p>
    ${deepDives}
    ${groupHeader('evidence-and-gaps')}
    ${shapeEvidence(shape)}
    ${walkthroughJudgmentSection(model)}
    ${walkthroughReadinessSection(model)}
    ${codeStructureSection(model)}
    ${workItemsSection(model)}`;
  // The machine form of the presentation artifact precedes every group so no
  // group slice carries it; it is computed after the body registered its blocks.
  const bodyWithNarrative = `${narrativeScript(narrative.narrative())}${body}`;

  return pageShell({
    title: 'Polaris · Syzygy three-surface POC',
    current: 'polaris',
    eyebrow: 'Polaris · Project manifesto',
    readingLayout: true,
    heading: copyText('shell.heading'),
    lede: copyText('shell.lede'),
    extraStyle: POLARIS_STYLE,
    body: bodyWithNarrative,
    sidebar: depthNav(shape, dives) + SECTION_NAV_SCRIPT,
    footer: `Evaluation <code>${escapeHtml(model.evaluation.snapshot)}</code> as of <code>${escapeHtml(model.evaluation.asOf)}</code>.`,
    escapeHtml,
    mountPrefix,
  });
}
