// First reading, cause-correct routes and progressive disclosure
// (PWB-REQ-010, PWB-REQ-011, PWB-REQ-020 as amended; RFC7-13, RFC7-16):
// the page opens on Butlers itself, explains every claim state once and in
// place, routes each Unknown to its actual cause, and keeps the exhaustive
// populations complete behind native disclosures the keyboard opens.
//
// Bead syzygy-1z3.24.5 (PWB-LIVE-06, PWB-LIVE-11, PWB-LIVE-13).

import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { UNKNOWN_REASON_ROUTES, type PocModel, type ProjectShape } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_TEXTS,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
  REJECTING_AUTHORITY,
  SECRET_SENTINEL,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

type Observed = Extract<ProjectShape, { kind: 'observed' }>;

const ACTIVE_SENTINEL = 'ACTIVE-CONTENT-SENTINEL-2c9e';
/** The craft README carrying inert-looking but active markup. */
const TEXTS_WITH_ACTIVE_CONTENT: Readonly<Record<string, string>> = {
  ...PROJECT_SHAPE_FIXTURE_TEXTS,
  'about/craft-and-care/README.md': `${PROJECT_SHAPE_FIXTURE_TEXTS['about/craft-and-care/README.md'] as string}\n<script>${ACTIVE_SENTINEL}</script>\n`,
};

function observed(texts?: Readonly<Record<string, string>>): { model: PocModel; shape: Observed; html: string } {
  const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(texts) } });
  if (model.projectShape.kind !== 'observed') throw new Error(`fixture shape is ${model.projectShape.kind}`);
  return { model, shape: model.projectShape, html: renderPolarisPage(model) };
}

function decode(text: string): string {
  return text.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}

function textOf(html: string): string {
  return decode(html.replace(/<style[\s\S]*?<\/style>/g, '').replace(/<script[\s\S]*?<\/script>/g, '').replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ');
}

/** Every `<details>` element with its opening tag and inner HTML. */
function detailsOf(html: string): { tag: string; inner: string }[] {
  return [...html.matchAll(/<details([^>]*)>([\s\S]*?)<\/details>/g)].map((match) => ({ tag: match[1] as string, inner: match[2] as string }));
}

describe('Polaris first reading (PWB-REQ-010 as amended; PWB-LIVE-06)', () => {
  it('opens on Butlers: the heading names the project, the overview group and the claim-state disclosure precede the depth list, and no headline status appears', () => {
    for (const variant of [observed().html, observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET).html, renderPolarisPage(buildFixtureModel(cleanups)), renderPolarisPage(buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } }))]) {
      expect(variant).toMatch(/<h1[^>]*>Butlers<\/h1>/);
      expect(variant).toContain('Butlers in its own words');
      const overview = variant.indexOf('data-polaris-group="overview"');
      const states = variant.indexOf('id="polaris-claim-states"');
      const nav = variant.indexOf('data-polaris-depth-nav');
      const boundaries = variant.indexOf('data-polaris-group="boundaries"');
      expect(overview).toBeGreaterThan(-1);
      expect(states).toBeGreaterThan(overview);
      expect(nav).toBeGreaterThan(states);
      expect(boundaries).toBeGreaterThan(nav);
      // The notice links the reader to the state explanation before any
      // control: one link, one target, before the overview.
      const notice = variant.indexOf('href="#polaris-claim-states"');
      expect(notice).toBeGreaterThan(-1);
      expect(notice).toBeLessThan(overview);
      expect(textOf(variant)).not.toMatch(/\b(healthy|unhealthy|passing|failing|maturity|score|on track|at risk|trend|trending|success rate)\b|\d+\s?%/i);
    }
  });

  it('explains every tuple field once, in place: each label, tier, freshness and challenge value the page uses has its sentence, every tuple is described by the explanation, and the only strengthening routes are stated', () => {
    const { html } = observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET);
    const block = /<details id="polaris-claim-states"[^>]*>([\s\S]*?)<\/details>/.exec(html)?.[1];
    expect(block).toBeDefined();
    const states = textOf(block as string);
    // Hand-typed vocabulary (RFC2-25 tiers, RFC6-14 freshness, challenge).
    for (const term of ['Observed —', 'Inferred —', 'Unknown —', 'gate-backed —', 'report-fact —', 'reduced-fidelity —', 'asserted-by-worker —', 'declared-only —', 'suspended —', 'unstated —', 'fresh —', 'stale —', 'broken —', 'superseded —', 'unchallenged —']) {
      expect(states, term).toContain(term);
    }
    expect(states).toContain('report-fact becomes gate-backed only through a retained gate artifact bound to the exact revision');
    expect(states).toContain('an Unknown clears only by the route stated beside it');
    expect(states).toContain('Never green, never zero');
    // Every value a rendered tuple carries is one the explanation names.
    const used = (attribute: string): Set<string> => new Set([...html.matchAll(new RegExp(`${attribute}="([^"]*)"`, 'g'))].map((match) => match[1] as string));
    for (const tier of used('data-epistemic-tier')) expect(states, tier).toContain(`${tier} —`);
    for (const freshness of used('data-epistemic-freshness')) expect(states, freshness).toContain(`${freshness} —`);
    for (const challenge of used('data-challenge-state')) expect(states, challenge).toContain(`${challenge} —`);
    for (const label of used('data-epistemic-label')) expect(states, label).toContain(`${label} —`);
    // Each tuple is described by the one explanation, which exists once.
    const tuples = [...html.matchAll(/<span class="claim-tuple"[^>]*>/g)].map((match) => match[0]);
    expect(tuples.length).toBeGreaterThan(0);
    for (const tuple of tuples) expect(tuple).toContain('aria-describedby="polaris-claim-states-lede"');
    expect(html.split('id="polaris-claim-states-lede"').length - 1).toBe(1);
    expect(html.split('id="polaris-claim-states"').length - 1).toBe(1);
  });
});

describe('Polaris cause-correct routes (PWB-REQ-020 as amended; PWB-LIVE-11)', () => {
  it('routes a detector exclusion to the detector and the rotation, beside every claim it makes Unknown and beneath the generic route at the gap entry; the body stays withheld', () => {
    const { shape, html } = observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET);
    const exclusion = shape.exclusions[0];
    expect(exclusion?.detectorId).toBe('known-token-formats');
    const cause = 'about/craft-and-care/README.md matched the known-token-formats detector: rotate and remove the matched text in Butlers, then a new snapshot; or an owner policy change to that detector';
    const text = textOf(html);
    expect(text).toContain(`Route: ${cause}`);
    // Every excluded-content Unknown on the page carries the cause route.
    const disclosures = [...html.matchAll(/<p class="unknown-disclosure" data-unknown-disclosure="([^"]+)"[^>]*>([\s\S]*?)<\/p>/g)]
      .filter((match) => (match[2] as string).includes('excluded-content'));
    expect(disclosures.length).toBeGreaterThan(0);
    for (const disclosure of disclosures) expect(decode(disclosure[2] as string), disclosure[1]).toContain(cause);
    // The gap entry keeps the generic route (the tuples oracle) and adds the
    // cause beneath it, labelled.
    const gap = /<li id="[^"]*" data-polaris-gap="excluded-content">([\s\S]*?)<\/li>/.exec(html)?.[1];
    expect(gap).toBeDefined();
    expect(decode(gap as string)).toContain(`Route: ${UNKNOWN_REASON_ROUTES['excluded-content']}`);
    expect(gap).toContain('>By cause:</span>');
    expect(decode(gap as string)).toContain(cause);
    expect(html).not.toContain(SECRET_SENTINEL);
    expect(html).not.toContain('AKIA');
  });

  it('routes an active-content exclusion to removal, not to a policy change, and never renders the marker', () => {
    const { shape, html } = observed(TEXTS_WITH_ACTIVE_CONTENT);
    const exclusion = shape.exclusions.find((entry) => entry.repositoryRelativePath === 'about/craft-and-care/README.md');
    expect(exclusion?.exclusionReason).toBe('active-content');
    expect(exclusion?.detectorId).toBeUndefined();
    const text = textOf(html);
    expect(text).toMatch(/about\/craft-and-care\/README\.md carries active content \(\d+ marker\(s\)\): remove it in Butlers, then a new snapshot; or an owner policy change admitting it/);
    expect(exclusion?.detail).toMatch(/^\d+$/);
    expect(html).not.toContain(ACTIVE_SENTINEL);
    expect(html).not.toContain('<script>ACTIVE');
    // The craft-policy class is Unknown for this cause, with the cause route
    // in place; the detector wording belongs to the other cause only.
    const craft = /<section class="claim-section" data-polaris-section="claim:class:craft-policy"[\s\S]*?<\/section>/.exec(html)?.[0];
    expect(craft).toBeDefined();
    expect(decode(craft as string)).toContain('carries active content');
    expect(craft).not.toContain('detector');
  });

  it('keeps the generic route where no cause is recorded: a clean tree routes each reason by the shared table alone', () => {
    const { shape, html } = observed();
    expect(shape.exclusions.length).toBe(0);
    expect(html).not.toContain('>By cause:</span>');
    for (const gap of html.matchAll(/data-polaris-gap="([^"]+)"/g)) {
      const reason = gap[1] as keyof typeof UNKNOWN_REASON_ROUTES;
      expect(textOf(html), reason).toContain(`Route: ${UNKNOWN_REASON_ROUTES[reason]}`);
    }
  });
});

describe('Polaris progressive disclosure (PWB-REQ-011 as amended; PWB-LIVE-13)', () => {
  it('keeps each item population and the exclusions complete behind a native disclosure whose control names the count, leaves the sources table open for fragment navigation, and hides nothing by style', () => {
    const { shape, html } = observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET);
    const populations = detailsOf(html).filter((details) => details.tag.includes('class="population"'));
    const itemPopulations = populations.filter((details) => details.tag.includes('data-polaris-items='));
    const exclusionPopulations = populations.filter((details) => details.tag.includes('data-polaris-exclusions='));
    // One disclosure per catalog class that declares items, each summary
    // naming exactly the model's item count for that class, every row
    // inside. The project-account sections are the overview's own prose,
    // not a catalog population.
    const classesWithItems = new Set(shape.items.map((item) => item.class).filter((cls) => cls !== 'project-account-section'));
    expect(new Set(itemPopulations.map((details) => /data-polaris-items="([^"]+)"/.exec(details.tag)?.[1]))).toEqual(classesWithItems);
    for (const details of itemPopulations) {
      const cls = /data-polaris-items="([^"]+)"/.exec(details.tag)?.[1];
      const count = shape.items.filter((item) => item.class === cls).length;
      expect(details.inner).toContain(`>Show items (${count})</summary>`);
      expect(details.inner.split('<tr data-polaris-item="').length - 1).toBe(count);
    }
    expect(exclusionPopulations.length).toBe(1);
    expect(exclusionPopulations[0]?.inner).toContain(`>Show exclusions (${shape.exclusions.length})</summary>`);
    expect(exclusionPopulations[0]?.inner.split('data-polaris-exclusion="').length).toBe(shape.exclusions.length + 1);
    // The sources table is not inside any disclosure: Chrome restarts
    // sequential focus at a details' first focusable after fragment
    // navigation into it, which would strand a reader who followed a
    // citation to a source row.
    const sources = html.indexOf('id="polaris-shape-sources"');
    expect(sources).toBeGreaterThan(-1);
    for (const details of detailsOf(html)) expect(details.inner).not.toContain('id="polaris-shape-sources"');
    for (const source of shape.sources) {
      const row = html.indexOf(`id="polaris-source-${source.path.replace(/[^A-Za-z0-9]+/g, '-')}"`);
      expect(row, source.path).toBeGreaterThan(sources);
    }
    // No fragment target sits inside a disclosure: a reader who follows a
    // link always lands where sequential focus continues.
    const targets = new Set([...html.matchAll(/href="#([^"]+)"/g)].map((match) => match[1] as string));
    for (const details of detailsOf(html)) {
      for (const id of details.inner.matchAll(/ id="([^"]+)"/g)) {
        expect(targets.has(id[1] as string), `${id[1]} is a fragment target inside a disclosure`).toBe(false);
      }
    }
    expect(html).not.toMatch(/display:\s*none|visibility:\s*hidden|aria-hidden="true"/);
  });

  it('reaches at least one requirement and one scenario verbatim from a first reading without treating Polaris as authority: the current-authority citation routes to the exact text and names the owning artifact', () => {
    const { html } = observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC);
    const detail = html.slice(html.indexOf('data-polaris-group="capability-detail"'), html.indexOf('data-polaris-group="evidence-and-gaps"'));
    const links = [...detail.matchAll(/<a href="([^"]+)" data-source-route="([^"]+)"[^>]*>Exact text<\/a>/g)];
    expect(links.length).toBeGreaterThan(0);
    for (const link of links) {
      expect(decode(link[1] as string)).toContain('/polaris/source?identity=');
      expect(decode(link[2] as string)).toContain('openspec/specs/');
    }
    // No requirement text is copied onto the page itself: the page cites and
    // routes, the route renders (PWB-REQ-011 non-goal: no copied source).
    expect(html).not.toContain('The switchboard SHALL resolve the sender');
    expect(html).not.toContain('PURPOSE-PROSE-NEVER-RENDERED');
  });
});
