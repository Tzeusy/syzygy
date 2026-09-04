import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel, ProjectShape, ProjectShapeClaim } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
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

    const anchors = [...html.matchAll(/<a href="#(polaris-source-[^"]+)"><cite data-parity-field="shape-anchor">([^<]+)<\/cite><\/a>/g)];
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
      expect(html).toContain(`<cite data-parity-field="shape-anchor">${where}</cite>`);
    }

    // Every source row exposes its exact digest when a body was read.
    for (const source of shape.sources) {
      const row = new RegExp(`data-polaris-source="${source.claim.claimId.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&')}"[\\s\\S]*?</tr>`).exec(html)?.[0] ?? '';
      expect(row).not.toBe('');
      const digest = source.claim.support[0]?.contentDigest;
      if (digest !== undefined) expect(row).toContain(digest.replace(/^sha256:/, '').slice(0, 12));
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
