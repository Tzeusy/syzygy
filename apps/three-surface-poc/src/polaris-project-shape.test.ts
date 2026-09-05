import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel, ProjectShape, ProjectShapeClaim } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { DEEP_DIVE_MARKERS } from './test-deep-dive-markers.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_ROOT_ROW_1_LINE,
  PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE,
  PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE_WITHOUT_PRECEDENCE,
  PROJECT_SHAPE_FIXTURE_TEXTS,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITHOUT_PRECEDENCE,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
  REJECTING_AUTHORITY,
  SECRET_SENTINEL,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

// Hand-typed oracles (never imported from the renderer or the model).
const PROJECT_GROUPS = ['overview', 'boundaries', 'architecture', 'v1', 'catalog'] as const;
const ACCOUNT_KEYS = ['purpose', 'promises', 'refusals', 'architecture', 'v1-scope', 'v1-success'] as const;
const CATALOG_CLASSES = ['catalog-entry', 'roster-identity', 'design-contract', 'baseline-spec', 'craft-policy'] as const;
const ACCOUNT_GROUP: Readonly<Record<(typeof ACCOUNT_KEYS)[number], string>> = {
  purpose: 'overview',
  promises: 'overview',
  refusals: 'boundaries',
  architecture: 'architecture',
  'v1-scope': 'v1',
  'v1-success': 'v1',
};
const CLASS_GROUP: Readonly<Record<string, string>> = {
  principle: 'boundaries',
  'topology-component': 'architecture',
  'success-criterion': 'v1',
  'catalog-entry': 'catalog',
  'roster-identity': 'catalog',
  'design-contract': 'catalog',
  'baseline-spec': 'catalog',
  'craft-policy': 'catalog',
};

function observedModel(texts?: Readonly<Record<string, string>>): { model: PocModel; shape: Extract<ProjectShape, { kind: 'observed' }> } {
  const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(texts) } });
  if (model.projectShape.kind !== 'observed') throw new Error(`fixture shape is ${model.projectShape.kind}`);
  return { model, shape: model.projectShape };
}

/** The slice of the HTML between one group header and the next. */
function groupSlice(html: string, group: string): string {
  const start = html.indexOf(`data-polaris-group="${group}"`);
  expect(start).toBeGreaterThan(-1);
  const next = html.indexOf('data-polaris-group="', start + 1);
  return html.slice(start, next === -1 ? html.length : next);
}

function allShapeClaims(shape: ProjectShape): ProjectShapeClaim[] {
  if (shape.kind !== 'observed') return [shape.claim];
  return [
    shape.claim,
    ...shape.projectAccount.map((entry) => entry.claim),
    ...shape.sources.map((entry) => entry.claim),
    ...shape.items.map((entry) => entry.claim),
    ...Object.values(shape.classes).map((entry) => entry.claim),
    ...shape.facts.map((entry) => entry.claim),
  ];
}

function attribute(tag: string, name: string): string | undefined {
  return new RegExp(`${name}="([^"]*)"`).exec(tag)?.[1];
}

describe('Polaris project-level sequence (PWB-REQ-010)', () => {
  it('renders every project-account statement and every catalog item in its group when the shape is observed', () => {
    const { model, shape } = observedModel();
    const html = renderPolarisPage(model);

    for (const key of ACCOUNT_KEYS) {
      const statement = shape.projectAccount.find((entry) => entry.key === key);
      expect(statement).toBeDefined();
      const slice = groupSlice(html, ACCOUNT_GROUP[key]);
      expect(slice).toContain(`data-polaris-section="claim:project-account:${key}"`);
      if (statement?.statement !== undefined && statement.claim.epistemic.label === 'Observed') {
        expect(slice).toContain(`data-claim-provenance="claim:project-account:${key}"`);
        expect(slice).toContain(statement.statement.replace(/&/g, '&amp;'));
      }
    }

    // Every item of every classed group, in its group — denominator is the
    // model's item list, counted here independently of the renderer.
    let placed = 0;
    for (const item of shape.items) {
      const group = CLASS_GROUP[item.class];
      if (group === undefined) continue; // project-account-section items are the statements above
      const slice = groupSlice(html, group);
      if (slice.includes(`data-polaris-item="${item.claim.claimId}"`) && slice.includes(`<code>${item.key}</code>`)) placed += 1;
    }
    const classed = shape.items.filter((item) => item.class !== 'project-account-section').length;
    expect(classed).toBeGreaterThan(5);
    expect(placed).toBe(classed);

    // The catalog carries every catalog class as its own titled block.
    const catalog = groupSlice(html, 'catalog');
    for (const cls of CATALOG_CLASSES) {
      expect(catalog).toContain(`data-polaris-class="${cls}"`);
      expect(catalog).toContain(`data-polaris-section="claim:class:${cls}"`);
    }
  });

  it('renders every project group as Unknown in place, with reason and route, when no evaluation was supplied', () => {
    const model = buildFixtureModel(cleanups);
    expect(model.projectShape.kind).toBe('not-evaluated');
    const html = renderPolarisPage(model);

    for (const group of PROJECT_GROUPS) {
      const slice = groupSlice(html, group);
      expect(slice).toContain(`data-polaris-section="shape:${group}"`);
      expect(slice).toContain('data-unknown-disclosure="claim:project-shape"');
      expect(slice).toContain('data-unknown-reason="unconsented-source-or-provider"');
      expect(slice).toContain('Route: Record consent');
      expect(slice).not.toContain('data-claim-provenance="claim:');
    }
    expect(html).toContain('data-polaris-gap="unconsented-source-or-provider"');
  });

  it('renders every project group as Unknown with the gate refusal when the authority does not admit', () => {
    const model = buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: () => { throw new Error('no git call may follow a refusal'); } } });
    expect(model.projectShape.kind).toBe('not-admitted');
    const html = renderPolarisPage(model);
    for (const group of PROJECT_GROUPS) {
      const slice = groupSlice(html, group);
      expect(slice).toContain('data-unknown-disclosure="claim:project-shape"');
      expect(slice).toContain('The body-read gate refused');
      expect(slice).toContain('RFC3-16(a)');
    }
  });

  it('does not claim a complete or absent catalog when root discovery is Unknown', () => {
    const texts = {
      ...PROJECT_SHAPE_FIXTURE_TEXTS,
      'about/README.md': (PROJECT_SHAPE_FIXTURE_TEXTS['about/README.md'] as string).replace('[Heart and Soul](heart-and-soul/) · ', ''),
    };
    const { model } = observedModel(texts);
    const html = renderPolarisPage(model);
    expect(html).toContain('Source discovery is incomplete for this class.');
    expect(html).not.toContain('complete catalog above');
    expect(html).toContain('completeness follows its disclosed denominator');
  });

  it('keeps path-only identity counts distinct from body readability in the model and Polaris', () => {
    const { model, shape } = observedModel();
    expect(shape.counts.sources).toBe(15);
    expect(shape.counts.sourcesWithKnownItemDenominator).toBe(15);
    expect(shape.counts.classification.classifiedByBasis).toEqual({ body: 14, 'path-only': 1 });
    const html = renderPolarisPage(model);
    expect(html).toContain('14 of 15 source bodies readable; 1 path-only source identities;');
    expect(html).not.toContain('15 of 15 sources readable');
    const baselineRow = /data-polaris-source="claim:source:openspec\/specs\/alpha\/spec\.md"[\s\S]*?<\/tr>/.exec(html)?.[0] ?? '';
    expect(baselineRow).toContain('path-only · blob');
    expect(baselineRow).toContain('no body read');
    expect(baselineRow).not.toContain('body-classified');
  });
});

describe('Polaris progressive depth (PWB-REQ-011; RFC7-16)', () => {
  it('keeps the claim identity and full epistemic tuple at every depth, matching the machine answer per claim', () => {
    const { model, shape } = observedModel();
    const html = renderPolarisPage(model);
    const machine = JSON.parse(JSON.stringify(model)) as PocModel;
    const claimsById = new Map(allShapeClaims(machine.projectShape).map((claim) => [claim.claimId, claim]));

    const tuples = [...html.matchAll(/<span class="claim-tuple"[^>]*>/g)].map((match) => match[0]);
    // Summary (whole shape) + detail (six statements, nine classes) + leaf
    // (classed items, sources, contradicted facts). Reconciled facts that
    // agree are counts already shown on their class; account-section items
    // are shown as the statements. Counted here from the model, not the HTML.
    const expectedTuples =
      1 +
      shape.projectAccount.length +
      Object.keys(shape.classes).length +
      shape.items.filter((item) => item.class !== 'project-account-section').length +
      shape.sources.length +
      shape.contradictions.length;
    expect(tuples.length).toBe(expectedTuples);
    expect(new Set(tuples.map((tuple) => attribute(tuple, 'data-claim-id'))).size).toBe(expectedTuples);
    let matched = 0;
    for (const tuple of tuples) {
      const claim = claimsById.get(attribute(tuple, 'data-claim-id') ?? '');
      if (claim === undefined) continue;
      const label = attribute(tuple, 'data-epistemic-label');
      const tier = attribute(tuple, 'data-epistemic-tier');
      const freshness = attribute(tuple, 'data-epistemic-freshness');
      const evaluation = attribute(tuple, 'data-evaluation-id');
      if (label === claim.epistemic.label && tier === (claim.epistemic.tier ?? 'unstated') && freshness === (claim.epistemic.freshness ?? 'unstated') && evaluation === claim.evaluationId) matched += 1;
    }
    expect(matched).toBe(tuples.length);
  });

  it('reaches the exact source from every observed statement and item: anchors link to a source row carrying the digest', () => {
    const { model, shape } = observedModel();
    const html = renderPolarisPage(model);

    const anchors = [...html.matchAll(/<a href="#(polaris-source-[^"]+)"><cite data-parity-field="shape-anchor"[^>]*>([^<]+)<\/cite><\/a>/g)];
    expect(anchors.length).toBeGreaterThan(0);
    const sourcePaths = new Set(shape.sources.map((source) => source.path));
    let resolved = 0;
    for (const anchor of anchors) {
      const target = anchor[1] as string;
      const path = (anchor[2] as string).replace(/:\d+$/, '');
      if (sourcePaths.has(path) && html.includes(`id="${target}"`)) resolved += 1;
    }
    expect(resolved).toBe(anchors.length);

    // Every observed account statement and item carries at least one anchor.
    const observedLeaves = [...shape.projectAccount, ...shape.items].filter((entry) => entry.claim.epistemic.label === 'Observed');
    expect(observedLeaves.length).toBeGreaterThan(0);
    for (const leaf of observedLeaves) {
      expect(leaf.claim.support.length).toBeGreaterThan(0);
      const first = leaf.claim.support[0] as { path: string; line?: number };
      const where = first.line === undefined ? first.path : `${first.path}:${first.line}`;
      expect(html).toMatch(new RegExp(`<cite data-parity-field="shape-anchor"[^>]*>${where.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}</cite>`));
    }

    // Every source row exposes its exact digest when a body was read.
    for (const source of shape.sources) {
      const row = new RegExp(`data-polaris-source="${source.claim.claimId.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&')}"[\\s\\S]*?</tr>`).exec(html)?.[0] ?? '';
      expect(row).not.toBe('');
      const digest = source.claim.support[0]?.contentDigest;
      if (digest !== undefined) expect(row).toContain(digest.replace(/^sha256:/, '').slice(0, 12));
    }

    // Every anchor digest shown beside a citation is the twelve-character
    // prefix of that source's exact digest in the machine answer.
    const digestBySource = new Map(
      shape.sources.flatMap((source) => {
        const digest = source.claim.support[0]?.contentDigest;
        return digest === undefined ? [] : [[source.path, digest.replace(/^sha256:/, '').slice(0, 12)] as const];
      }),
    );
    const anchorDigests = [
      ...html.matchAll(/<cite data-parity-field="shape-anchor"[^>]*>([^<]+)<\/cite><\/a>@<code data-parity-field="shape-anchor-digest">([^<]+)<\/code>/g),
    ];
    expect(anchorDigests.length).toBeGreaterThan(0);
    for (const shown of anchorDigests) {
      const path = (shown[1] as string).replace(/:\d+$/, '');
      expect(shown[2], `anchor digest for ${path}`).toBe(digestBySource.get(path));
    }
  });

  it('resolves every claim marker against the shared model when the shape is observed (POC-REQ-031 extended)', () => {
    const { model, shape } = observedModel();
    const html = renderPolarisPage(model);
    const resolvable = new Set<string>([
      ...model.entities.map((entity) => entity.id),
      ...model.relationships.map((relationship) => relationship.id),
      'region:code-structure',
      'region:work-items',
      model.proposedWork.id,
      `${model.proposedWork.id}/lifecycle`,
      ...DEEP_DIVE_MARKERS(model.capabilityId),
      ...allShapeClaims(shape).map((claim) => claim.claimId),
    ]);
    const markers = [...html.matchAll(/data-(?:claim-provenance|unknown-disclosure)="([^"]+)"/g)].map((match) => match[1] as string);
    expect(markers.length).toBeGreaterThan(30);
    let resolved = 0;
    for (const marker of markers) if (resolvable.has(marker)) resolved += 1;
    expect(resolved).toBe(markers.length);
  });

  it('discloses an excluded source as hash-not-body and its items as Unknown with a route, never the body', () => {
    const { model, shape } = observedModel(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET);
    expect(shape.exclusions.length).toBe(1);
    const html = renderPolarisPage(model);
    expect(html).not.toContain(SECRET_SENTINEL);
    expect(html).not.toContain('AKIA');
    expect(html).toContain('data-polaris-exclusion="about/craft-and-care/README.md"');
    expect(html).toContain('known-token-formats');
    const craft = shape.classes['craft-policy'];
    expect(craft.claim.epistemic.label).toBe('Unknown');
    const catalog = groupSlice(html, 'catalog');
    expect(catalog).toContain('data-unknown-disclosure="claim:class:craft-policy"');
    expect(catalog).toContain('data-unknown-reason="excluded-content"');
    expect(catalog).toContain('Route: Policy change by the owner, or accept the exclusion');
    expect(html).toContain('data-polaris-gap="excluded-content"');
  });
});

// ---------------------------------------------------------------------------
// PWB-REQ-004 (as amended 2026-09-05): the root index's own declarations are
// disclosed — the seven layer rows, the two stated counts, and every
// disagreement a row decided — with both sides anchored to exact sources.
// Oracles below are hand-typed from the registry entry's observationGrammar.

const ROOT = 'about/README.md';
const V1 = 'about/heart-and-soul/v1.md';
const LAYER_ROWS: readonly (readonly [number, string, string, string])[] = [
  [1, 'Heart and Soul', 'Principles, scope boundaries, the 7 non-negotiable rules', 'about/heart-and-soul/'],
  [2, 'Legends and Lore', 'Wire contracts, state machines, data models, sanctioned rule exceptions', 'about/legends-and-lore/rfcs/'],
  [3, 'Spec and Spine', 'Feature behaviour, acceptance scenarios (WHEN/THEN), per-butler contracts', 'openspec/specs/'],
  [4, 'Craft and Care', 'Execution-quality standards, test scope, review gates, observability bar', 'about/craft-and-care/'],
  [5, 'Lay and Land', 'Topology snapshot — where components live, how they connect, stability levels', 'about/lay-and-land/'],
  [6, 'Roster config', 'Live butler identity: butler.toml, MANIFESTO.md, CLAUDE.md, skills, API routes', 'roster/{butler}/'],
  [7, 'Code', 'Runtime behaviour — executed source, migrations, tests', 'src/, alembic/, tests/'],
];

function rootIndexSlice(html: string): string {
  const start = html.indexOf('data-polaris-section="shape:root-index"');
  expect(start).toBeGreaterThan(-1);
  const end = html.indexOf('data-polaris-section="shape:contradictions"', start);
  expect(end).toBeGreaterThan(start);
  return html.slice(start, end);
}

function sourceLink(path: string, line: number): string {
  return `<a href="#polaris-source-${path.replace(/[^A-Za-z0-9]+/g, '-')}" data-source-ref="${path}">${path}:${line}</a>`;
}

describe('Polaris root-index declarations (PWB-REQ-004 as amended)', () => {
  it('renders the seven admitted rows verbatim with their exact-source anchors, the stated counts, and the one decided fact with effective and superseded sides', () => {
    const { model, shape } = observedModel();
    const html = renderPolarisPage(model);
    const slice = rootIndexSlice(html);

    // The machine answer the section must agree with.
    expect(shape.precedence.kind).toBe('admitted');
    expect(shape.rootSummary.kind).toBe('emitted');
    const staffers = shape.facts.find((fact) => fact.fact.fact === 'catalog-count:Staffers');
    expect(staffers?.fact.state).toBe('modeled');
    if (staffers?.fact.state !== 'modeled') return;
    expect(staffers.fact.value).toBe('0');
    expect(staffers.fact.disagreement?.precedence.ruleId).toBe('layer:1');
    expect(shape.contradictions.map((fact) => fact.fact.fact)).not.toContain('catalog-count:Staffers');

    expect(slice).toContain('<h3 id="polaris-shape-root-index"');
    expect(slice).toContain(`data-polaris-precedence="7"`);
    expect(slice).toContain(`Precedence rows admitted:</span> 7 from ${sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_ROW_1_LINE - 2)}.`);
    for (const [ordinal, layer, owns, home] of LAYER_ROWS) {
      const row = new RegExp(`<tr data-polaris-precedence="layer:${ordinal}"[^>]*>([\\s\\S]*?)</tr>`).exec(slice)?.[1] ?? '';
      expect(row, `row ${ordinal}`).not.toBe('');
      const cells = [...row.matchAll(/<td>([\s\S]*?)<\/td>/g)].map((match) => match[1] as string);
      expect(cells.slice(0, 4)).toEqual([String(ordinal), layer, owns.replace(/&/g, '&amp;'), `<code>${home}</code>`]);
      expect(cells[4]).toBe(sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_ROW_1_LINE + ordinal - 1));
    }
    expect(slice.split('<tr data-polaris-precedence=').length - 1).toBe(7);

    expect(slice).toContain('data-polaris-stated-counts="2"');
    expect(slice).toContain(`<span data-polaris-stated-count="catalog-count:Staffers">catalog-count:Staffers = 1 (stated-summary, ${sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE)})</span>`);
    expect(slice).toContain(`<span data-polaris-stated-count="catalog-count:Butlers">catalog-count:Butlers = 2 (stated-summary, ${sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE)})</span>`);

    // Exactly one disagreement was decided: zero staffers (V1's heading) is
    // effective by row 1; the stated one is kept, superseded, with its anchor.
    expect(slice).toContain('data-polaris-decided-count="1"');
    const decided = /<li data-polaris-decided="([^"]+)"[^>]*>([\s\S]*?)<\/li>/.exec(slice);
    expect(decided?.[1]).toBe(staffers.claim.claimId);
    const v1Line = staffers.fact.disagreement?.effective.anchors[0]?.line as number;
    // Copy spans carry their role attributes; the words and anchors are exact.
    expect((decided?.[2] ?? '').replace(/<span data-copy-role="[^"]+"[^>]*>/g, '<span>')).toBe(
      `catalog-count:Staffers: <span>effective</span> 0 (derived-count, ${sourceLink(V1, v1Line)}) by layer:1 (Heart and Soul, ${sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_ROW_1_LINE)}); <span>superseded</span> 1 (stated-summary, ${sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE)}).`,
    );
    expect(decided?.[2]).toContain('data-copy-role="project-fact"');
    expect(decided?.[2]).toContain('data-copy-role="epistemic-disclosure"');
    // Butlers agreed (2 = 2): nothing decided, nothing contradicted.
    expect(slice).not.toContain('data-polaris-decided="claim:fact:catalog-count:Butlers"');
    // A decided fact is not a contradiction and carries no claim tuple here.
    expect(slice).not.toContain('class="claim-tuple"');
    expect(slice).not.toContain('data-polaris-fact=');
  });

  it('without the table: the stated staffer count is a contradiction with both anchors, the table is disclosed absent at its line, no row decides', () => {
    const { model, shape } = observedModel(PROJECT_SHAPE_FIXTURE_TEXTS_WITHOUT_PRECEDENCE);
    const html = renderPolarisPage(model);
    const slice = rootIndexSlice(html);
    expect(shape.precedence).toMatchObject({ kind: 'absent', reason: 'missing-heading', detail: 'Precedence Order When Layers Disagree' });
    expect(shape.contradictions.map((fact) => fact.fact.fact)).toEqual(['catalog-count:Staffers']);

    expect(slice).toContain('data-polaris-precedence="0"');
    expect(slice).toContain(`No precedence table is admitted from the root index:</span> missing-heading (Precedence Order When Layers Disagree) at ${sourceLink(ROOT, 1)}.`);
    expect(slice).toContain('data-polaris-stated-counts="2"');
    expect(slice).toContain(sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE_WITHOUT_PRECEDENCE));
    expect(slice).toContain('data-polaris-decided-count="0"');
    expect(slice).toContain('No disagreement between admitted declarations was decided by a row.');

    const contradictions = html.slice(html.indexOf('data-polaris-section="shape:contradictions"'));
    expect(contradictions).toContain('data-polaris-fact="claim:fact:catalog-count:Staffers"');
    expect(contradictions).toContain('catalog-count:Staffers: Unknown');
    expect(contradictions).toContain('contradicted-pending-adjudication');
    expect(contradictions).toContain(`1 (stated-summary, ${sourceLink(ROOT, PROJECT_SHAPE_FIXTURE_ROOT_SUMMARY_LINE_WITHOUT_PRECEDENCE)})`);
  });

  it('the bare root: both grammars disclosed absent, nothing decided, no contradiction minted from a summary that was never stated', () => {
    const texts = { ...PROJECT_SHAPE_FIXTURE_TEXTS, [ROOT]: (PROJECT_SHAPE_FIXTURE_TEXTS[ROOT] as string).split('\n### Precedence Order')[0] as string };
    const { model, shape } = observedModel(texts);
    const slice = rootIndexSlice(renderPolarisPage(model));
    expect(shape.rootSummary).toMatchObject({ kind: 'absent', reason: 'missing-heading' });
    expect(shape.facts.filter((fact) => fact.fact.fact.startsWith('catalog-count:')).every((fact) => fact.fact.declarations.length === 1)).toBe(true);
    expect(slice).toContain('data-polaris-precedence="0"');
    expect(slice).toContain('data-polaris-stated-counts="0"');
    expect(slice).toContain(`No stated summary count is admitted from the root index:</span> missing-heading (Key Architectural Facts) at ${sourceLink(ROOT, 1)}.`);
    expect(slice).toContain('data-polaris-decided-count="0"');
  });
});

