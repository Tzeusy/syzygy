// Walkthrough preflight (bead syzygy-1z3.24.6; PWB-LIVE-12): the mechanical
// readiness of one evaluation for the cold-open walkthrough — is what the
// reader will be asked about actually on the surface? Pure: it reads the
// model, the rendered Polaris page, the outcomes of the exact-source routes
// and one browser check, all supplied by the caller (the fresh-checkout
// demo reads nothing from Butlers itself).
//
// Four states stay separate by construction. This predicate is the first,
// preflight; the execution record (PWB-REQ-021 readiness), the owner's
// judgment (PWB-REQ-022) and the act's validity are the others, and nothing
// here reads or writes any of them. A failed preflight means the owner is
// not yet invited to walk; a passed preflight is no answer, no verdict and
// no score. Every limb below fails closed.

import {
  EXTRACTION_CLASSES,
  PROJECT_ACCOUNT_KEYS,
  type ExtractionClass,
  type PocModel,
  type ProjectShape,
  type ProjectShapeClaim,
} from '@syzygy/three-surface-poc-core';

import { currentIntentLeaf } from './capability-detail.js';
import { copyText } from './polaris-copy.js';

export const PREFLIGHT_LIMBS = [
  'account-statement-unbacked',
  'population-empty',
  'population-unreconciled',
  'exact-requirement-unreachable',
  'unknown-invisible',
  'claim-strength-unexplained',
  'source-path-unresolved',
  'browser-check-not-current',
] as const;
export type PreflightLimb = (typeof PREFLIGHT_LIMBS)[number];

/** The classes the six prompts ask the reader to reconcile against
 * (RFC7-30: principles, success criteria, the catalog, the topology). */
export const RECONCILED_CLASSES = ['principle', 'success-criterion', 'catalog-entry', 'topology-component'] as const satisfies readonly ExtractionClass[];

export type SourceRouteOutcome =
  | { readonly state: 'rendered'; readonly requirements: number }
  | { readonly state: 'not-rendered'; readonly reason: string }
  | { readonly state: 'unreachable'; readonly detail: string };

export type BrowserCheckInput =
  | { readonly kind: 'performed'; readonly commit: string; readonly variants: number; readonly violations: number }
  | { readonly kind: 'not-performed'; readonly detail: string };

export interface WalkthroughPreflightInputs {
  readonly model: PocModel;
  /** The rendered Polaris page, exactly as served. */
  readonly polarisHtml: string;
  /** What the exact-source route answered for each identity the page links. */
  readonly sourceRoutes: ReadonlyMap<string, SourceRouteOutcome>;
  readonly browserCheck: BrowserCheckInput;
}

export interface PreflightFinding {
  readonly limb: PreflightLimb;
  readonly detail: string;
}

export interface WalkthroughPreflight {
  readonly ready: boolean;
  readonly findings: readonly PreflightFinding[];
  /** Counts the evidence record carries; never a score. */
  readonly observed: {
    readonly accountStatementsBacked: number;
    readonly populations: Readonly<Record<(typeof RECONCILED_CLASSES)[number], { readonly modeled: number; readonly denominator: number | null; readonly rows: number }>>;
    readonly exactRequirement: { readonly identity: string | null; readonly requirements: number };
    readonly unknownsVisible: number;
    readonly unknownsMachine: number;
    readonly sourceRoutesLinked: number;
    readonly fragmentLinks: number;
    readonly claimTuples: number;
  };
}

type Observed = Extract<ProjectShape, { kind: 'observed' }>;

function decode(text: string): string {
  return text.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}

function encode(text: string): string {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function attrValues(html: string, attribute: string): string[] {
  return Array.from(html.matchAll(new RegExp(`${attribute}="([^"]*)"`, 'g')), (match) => decode(match[1] as string));
}

function count(html: string, literal: string): number {
  return html.split(literal).length - 1;
}

/** The project-shape claims Polaris presents as claim tuples: the same rule
 * the parity oracle applies (reconciled facts fold into their account
 * statements and project-account-section items into the account itself;
 * only contradictions render as their own claims). */
export function presentedShapeClaims(shape: ProjectShape): readonly ProjectShapeClaim[] {
  if (shape.kind !== 'observed') return [shape.claim];
  return [
    shape.claim,
    ...shape.sources.map((source) => source.claim),
    ...shape.items.filter((item) => item.class !== 'project-account-section').map((item) => item.claim),
    ...EXTRACTION_CLASSES.map((cls) => shape.classes[cls].claim),
    ...shape.contradictions.map((fact) => fact.claim),
    ...shape.projectAccount.map((statement) => statement.claim),
  ];
}

function accountStatements(shape: Observed, html: string): { readonly failures: string[]; readonly backed: number } {
  const failures: string[] = [];
  let backed = 0;
  for (const key of PROJECT_ACCOUNT_KEYS) {
    const statement = shape.projectAccount.find((entry) => entry.key === key);
    const claimId = `claim:project-account:${key}`;
    if (statement === undefined) {
      failures.push(`${key}: no statement in the model`);
      continue;
    }
    const problems: string[] = [];
    if (statement.claim.epistemic.label !== 'Observed') problems.push(`label ${statement.claim.epistemic.label}`);
    if ((statement.statement ?? '').trim() === '') problems.push('empty statement');
    if (statement.anchors.length === 0) problems.push('no source anchor');
    if (count(html, `data-claim-id="${encode(claimId)}"`) !== 1) problems.push('not rendered exactly once as a claim tuple');
    if (problems.length === 0) backed += 1;
    else failures.push(`${key}: ${problems.join(', ')}`);
  }
  return { failures, backed };
}

function populations(shape: Observed, html: string): { readonly empty: string[]; readonly unreconciled: string[]; readonly summary: WalkthroughPreflight['observed']['populations'] } {
  const empty: string[] = [];
  const unreconciled: string[] = [];
  const summary: Record<string, { modeled: number; denominator: number | null; rows: number }> = {};
  for (const cls of RECONCILED_CLASSES) {
    const aggregate = shape.classes[cls];
    const items = shape.items.filter((item) => item.class === cls);
    let rows = 0;
    const missingRows: string[] = [];
    for (const item of items) {
      const occurrences = count(html, `data-polaris-item="${encode(item.claim.claimId)}"`);
      if (occurrences === 1) rows += 1;
      else missingRows.push(`${item.claim.claimId} ×${occurrences}`);
    }
    summary[cls] = { modeled: aggregate.modeled, denominator: aggregate.denominator.kind === 'known' ? aggregate.denominator.value : null, rows };
    if (aggregate.modeled === 0) empty.push(`${cls}: 0 modeled`);
    if (aggregate.denominator.kind !== 'known') {
      unreconciled.push(`${cls}: denominator Unknown (${aggregate.denominator.reasons.join(', ')})`);
    } else if (aggregate.modeled + aggregate.unknown + aggregate.contradicted !== aggregate.denominator.value) {
      unreconciled.push(`${cls}: ${aggregate.modeled} modeled + ${aggregate.unknown} Unknown + ${aggregate.contradicted} contradicted ≠ ${aggregate.denominator.value} declared`);
    }
    if (missingRows.length > 0) unreconciled.push(`${cls}: item rows not rendered exactly once: ${missingRows.join('; ')}`);
  }
  return { empty, unreconciled, summary: summary as WalkthroughPreflight['observed']['populations'] };
}

function exactRequirement(model: PocModel, shape: Observed, html: string, routes: ReadonlyMap<string, SourceRouteOutcome>): { readonly failure: string | undefined; readonly identity: string | null; readonly requirements: number } {
  const authority = model.proposedWork.currentAuthority;
  if (authority.kind !== 'baseline-spec') return { failure: `current authority is ${authority.kind} (${authority.reason}); no baseline spec to reach`, identity: null, requirements: 0 };
  const leaf = currentIntentLeaf(authority, shape.identity.revision);
  if (leaf === undefined) return { failure: `baseline spec ${authority.path} carries no captured identity`, identity: null, requirements: 0 };
  const problems: string[] = [];
  const renderedOnPage = count(html, 'data-verbatim="rendered"');
  const requirementsOnPage = count(html, 'data-verbatim-requirement="');
  if (renderedOnPage < 1) problems.push('no verbatim block rendered on the page');
  if (requirementsOnPage < 1) problems.push('no requirement rendered on the page');
  if (count(html, `data-source-route="${encode(leaf.identity)}"`) < 1) problems.push('the page does not link the exact-source route for the current requirement');
  const route = routes.get(leaf.identity);
  let requirements = 0;
  if (route === undefined) problems.push('the exact-source route was not checked');
  else if (route.state !== 'rendered') problems.push(`the exact-source route answered ${route.state}${route.state === 'not-rendered' ? ` (${route.reason})` : ` (${route.detail})`}`);
  else if (route.requirements < 1) problems.push('the exact-source route rendered no requirement');
  else requirements = route.requirements;
  return { failure: problems.length === 0 ? undefined : `${authority.path}: ${problems.join('; ')}`, identity: leaf.identity, requirements };
}

function unknowns(shape: ProjectShape, html: string): { readonly failure: string | undefined; readonly visible: number; readonly machine: number } {
  const machineUnknowns = presentedShapeClaims(shape).filter((claim) => claim.epistemic.label === 'Unknown');
  const visible = count(html, 'data-epistemic-label="Unknown"');
  const problems: string[] = [];
  if (visible < 1) problems.push('no Unknown is visible on the page');
  if (visible !== machineUnknowns.length) problems.push(`${visible} visible vs ${machineUnknowns.length} in the model`);
  for (const claim of machineUnknowns) {
    // A deferred Unknown states no reason by design; every other Unknown
    // must carry its primary reason (RFC2-24).
    const epistemic = claim.epistemic;
    if (epistemic.label === 'Unknown' && !('basis' in epistemic) && (epistemic.reasons.primary as string) === '') problems.push(`${claim.claimId}: no primary reason`);
    if (claim.resolutionRoutes.length === 0) problems.push(`${claim.claimId}: no resolution route`);
  }
  return { failure: problems.length === 0 ? undefined : problems.join('; '), visible, machine: machineUnknowns.length };
}

function claimStrength(shape: ProjectShape, html: string): { readonly failure: string | undefined; readonly tuples: number } {
  const problems: string[] = [];
  const opens = count(html, '<details id="polaris-claim-states"');
  if (opens !== 1) problems.push(`${opens} claim-state glossaries (need exactly one)`);
  if (count(html, 'id="polaris-claim-states-lede"') !== 1) problems.push('the glossary lede is not present exactly once');
  const start = html.indexOf('<details id="polaris-claim-states"');
  const end = start < 0 ? -1 : html.indexOf('</details>', start);
  const block = start < 0 || end < 0 ? '' : decode(html.slice(start, end));
  const terms = new Set<string>();
  for (const claim of presentedShapeClaims(shape)) {
    terms.add(claim.epistemic.label);
    if (claim.epistemic.tier !== undefined) terms.add(claim.epistemic.tier);
    if (claim.epistemic.freshness !== undefined) terms.add(claim.epistemic.freshness);
    terms.add(claim.challenge);
  }
  for (const term of [...terms].sort()) {
    if (!block.includes(`${term} —`)) problems.push(`the glossary does not explain "${term}"`);
  }
  if (!block.includes(copyText('states.strengthen'))) problems.push('the glossary does not say how a claim is strengthened');
  const tuples = Array.from(html.matchAll(/<span class="claim-tuple"[^>]*>/g), (match) => match[0]);
  const undescribed = tuples.filter((tuple) => !tuple.includes('aria-describedby="polaris-claim-states-lede"')).length;
  if (undescribed > 0) problems.push(`${undescribed} claim tuple(s) are not described by the glossary`);
  return { failure: problems.length === 0 ? undefined : problems.join('; '), tuples: tuples.length };
}

function sourcePaths(html: string, routes: ReadonlyMap<string, SourceRouteOutcome>): { readonly failure: string | undefined; readonly linked: number; readonly fragments: number } {
  const problems: string[] = [];
  const identities = [...new Set(attrValues(html, 'data-source-route'))];
  for (const identity of identities) {
    const route = routes.get(identity);
    if (route === undefined) problems.push(`${identity}: route not checked`);
    else if (route.state === 'unreachable') problems.push(`${identity}: unreachable (${route.detail})`);
    else if (route.state === 'not-rendered' && route.reason.trim() === '') problems.push(`${identity}: not rendered and no reason stated`);
    else if (route.state === 'rendered' && route.requirements < 1) problems.push(`${identity}: rendered nothing`);
  }
  const ids = new Set(attrValues(html, 'id'));
  const fragments = Array.from(html.matchAll(/href="#([^"]*)"/g), (match) => decode(match[1] as string));
  const dangling = [...new Set(fragments.filter((fragment) => fragment !== '' && !ids.has(fragment)))];
  if (dangling.length > 0) problems.push(`dangling internal links: ${dangling.join(', ')}`);
  return { failure: problems.length === 0 ? undefined : problems.join('; '), linked: identities.length, fragments: fragments.length };
}

function browserCheck(model: PocModel, input: BrowserCheckInput): string | undefined {
  if (input.kind === 'not-performed') return `not performed: ${input.detail}`;
  const problems: string[] = [];
  if (input.commit !== model.observerRevision) problems.push(`checked ${input.commit.slice(0, 12)}, serving ${model.observerRevision.slice(0, 12)}`);
  if (input.variants < 1) problems.push('no variant exercised');
  if (input.violations !== 0) problems.push(`${input.violations} violation(s)`);
  return problems.length === 0 ? undefined : problems.join('; ');
}

const EMPTY_POPULATIONS = Object.fromEntries(RECONCILED_CLASSES.map((cls) => [cls, { modeled: 0, denominator: null, rows: 0 }])) as WalkthroughPreflight['observed']['populations'];

/** Every limb is evaluated and every failure reported at once. */
export function evaluateWalkthroughPreflight(inputs: WalkthroughPreflightInputs): WalkthroughPreflight {
  const { model, polarisHtml: html, sourceRoutes } = inputs;
  const shape = model.projectShape;
  const findings: PreflightFinding[] = [];
  const add = (limb: PreflightLimb, detail: string | undefined): void => {
    if (detail !== undefined) findings.push({ limb, detail });
  };
  let accountBacked = 0;
  let populationSummary = EMPTY_POPULATIONS;
  let exact: { identity: string | null; requirements: number } = { identity: null, requirements: 0 };
  if (shape.kind !== 'observed') {
    const detail = `no observed project shape (${shape.kind})`;
    add('account-statement-unbacked', detail);
    add('population-empty', detail);
    add('population-unreconciled', detail);
    add('exact-requirement-unreachable', detail);
  } else {
    const account = accountStatements(shape, html);
    accountBacked = account.backed;
    add('account-statement-unbacked', account.failures.length === 0 ? undefined : account.failures.join('; '));
    const population = populations(shape, html);
    populationSummary = population.summary;
    add('population-empty', population.empty.length === 0 ? undefined : population.empty.join('; '));
    add('population-unreconciled', population.unreconciled.length === 0 ? undefined : population.unreconciled.join('; '));
    const requirement = exactRequirement(model, shape, html, sourceRoutes);
    exact = { identity: requirement.identity, requirements: requirement.requirements };
    add('exact-requirement-unreachable', requirement.failure);
  }
  const unknown = unknowns(shape, html);
  add('unknown-invisible', unknown.failure);
  const strength = claimStrength(shape, html);
  add('claim-strength-unexplained', strength.failure);
  const paths = sourcePaths(html, sourceRoutes);
  add('source-path-unresolved', paths.failure);
  add('browser-check-not-current', browserCheck(model, inputs.browserCheck));
  return {
    ready: findings.length === 0,
    findings,
    observed: {
      accountStatementsBacked: accountBacked,
      populations: populationSummary,
      exactRequirement: exact,
      unknownsVisible: unknown.visible,
      unknownsMachine: unknown.machine,
      sourceRoutesLinked: paths.linked,
      fragmentLinks: paths.fragments,
      claimTuples: strength.tuples,
    },
  };
}
