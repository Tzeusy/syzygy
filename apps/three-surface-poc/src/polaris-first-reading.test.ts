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
  it('opens on Butlers: the heading names the project, the compact contents precede the overview and the state explanation follows it, and no headline status appears', () => {
    for (const variant of [observed().html, observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET).html, renderPolarisPage(buildFixtureModel(cleanups)), renderPolarisPage(buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } }))]) {
      expect(variant).toMatch(/<h1[^>]*>Butlers<\/h1>/);
      expect(variant).toContain('Less to remember. More room to live.');
      const overview = variant.indexOf('data-polaris-group="overview"');
      const states = variant.indexOf('id="polaris-claim-states"');
      const nav = variant.indexOf('data-polaris-depth-nav');
      const boundaries = variant.indexOf('data-polaris-group="boundaries"');
      expect(overview).toBeGreaterThan(-1);
      expect(states).toBeGreaterThan(overview);
      expect(nav).toBeLessThan(overview);
      expect(boundaries).toBeGreaterThan(states);
      // The source-backed project introduction precedes the reading aids.
      // The notice still routes to the complete state explanation.
      const notice = variant.indexOf('href="#polaris-claim-states"');
      expect(notice).toBeGreaterThan(-1);
      expect(notice).toBeGreaterThan(overview);
      expect(notice).toBeLessThan(states);
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

describe('Polaris capability reading', () => {
  it('introduces declared groups with complete member examples before the architecture', () => {
    const { shape, html } = observed();
    const start = html.indexOf('id="polaris-capability-guide"');
    const end = html.indexOf('data-polaris-section="claim:project-account:v1-scope"');
    expect(start).toBeGreaterThan(-1);
    expect(end).toBeGreaterThan(start);
    expect(end).toBeLessThan(html.indexOf('data-polaris-group="architecture"'));
    const guide = html.slice(start, end);
    expect(guide).toContain('Declared capability groups, with examples where available.');
    expect(guide).toContain('href="#polaris-class-catalog-entry"');
    const declared = shape.items.filter((item) => item.class === 'catalog-entry');
    const contexts = [...new Set(declared.map((item) => item.context))];
    expect(contexts.length).toBeGreaterThan(0);
    for (const context of contexts) {
      if (context !== undefined) expect(textOf(guide)).toContain(context);
    }
    const examples = [...guide.matchAll(/data-claim-provenance="([^"]+)"/g)].map((match) => match[1]);
    expect(examples.length).toBe(contexts.length);
    for (const id of examples) {
      const item = declared.find((item) => item.claim.claimId === id);
      expect(item).toBeDefined();
      expect(textOf(guide)).toContain((item?.statement ?? '').replace(/\*\*|`/g, '').replace(/\s+/g, ' ').trim());
    }
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
    const disclosures = [...html.matchAll(/<div class="unknown-disclosure" data-unknown-disclosure="([^"]+)"[^>]*>([\s\S]*?)<\/div>/g)]
      .filter((match) => (match[2] as string).includes('excluded-content'));
    expect(disclosures.length).toBeGreaterThan(0);
    for (const disclosure of disclosures) {
      expect(decode(disclosure[2] as string), disclosure[1]).toContain(cause);
      expect(disclosure[2]).toContain('<details class="unknown-source-details">');
      expect(disclosure[2]).not.toContain('<details class="unknown-source-details" open');
    }
    // The gap entry keeps the generic route (the tuples oracle) and adds the
    // cause beneath it, labelled.
    const gap = /<li id="[^"]*" data-polaris-gap="excluded-content">([\s\S]*?)<\/li>/.exec(html)?.[1];
    expect(gap).toBeDefined();
    expect(decode(gap as string)).toContain(`Route: ${UNKNOWN_REASON_ROUTES['excluded-content']}`);
    expect(gap).toContain('>By cause:</span>');
    expect(decode(gap as string)).toContain(cause);
    expect(html).not.toContain(SECRET_SENTINEL);
    const reasonBlocks = [...html.matchAll(/<ul data-reason-counts-(?:primary|secondary)="[^"]+"[^>]*>([\s\S]*?)<\/ul>/g)];
    expect(reasonBlocks.length).toBeGreaterThan(0);
    for (const block of reasonBlocks) {
      expect(block[1]).toContain('<details class="reason-remedies">');
      expect(block[1]).not.toContain('<details class="reason-remedies" open');
    }
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

  it('lists two or more causes as separate items after the paragraph, never inside it, (an unordered list in the gap entry, an ordered list in every reason-counts detail)', () => {
    const second = 'about/heart-and-soul/vision.md';
    const texts = {
      ...TEXTS_WITH_ACTIVE_CONTENT,
      [second]: `${PROJECT_SHAPE_FIXTURE_TEXTS[second] as string}\n<script>${ACTIVE_SENTINEL}</script>\n`,
    };
    const { shape, html } = observed(texts);
    const paths = shape.exclusions.filter((entry) => entry.exclusionReason === 'active-content').map((entry) => entry.repositoryRelativePath);
    expect(paths).toEqual(expect.arrayContaining(['about/craft-and-care/README.md', second]));
    const lists = [...html.matchAll(/<ol class="cause-routes">([\s\S]*?)<\/ol>/g)];
    expect(lists.length).toBeGreaterThan(0);
    for (const list of lists) {
      const items = [...(list[1] as string).matchAll(/<li>([\s\S]*?)<\/li>/g)].map((item) => decode(item[1] as string));
      expect(items.length).toBe(2);
      expect(items.some((item) => item.startsWith(`${second} carries active content`))).toBe(true);
      expect(items.some((item) => item.startsWith('about/craft-and-care/README.md carries active content'))).toBe(true);
    }
    const gap = /data-polaris-gap="excluded-content">([\s\S]*?)(?=<li id=|<\/ul>)/.exec(html)?.[1] ?? '';
    expect(gap).toContain('>By cause:</span><ul data-polaris-gap-causes="2">');
    expect(gap.split('<li>').length - 1).toBe(2);
    const details = [...html.matchAll(/<details class="reason-remedies">([\s\S]*?)<\/details>/g)].map((match) => match[1] as string);
    const withCauses = details.filter((detail) => detail.includes('cause-routes'));
    expect(withCauses.length).toBeGreaterThan(0);
    for (const detail of withCauses) {
      // The paragraph closes before the list: no block element sits inside a <p>.
      expect(detail).toMatch(/<p>Route: [^<]*(?:<span[^>]*>By cause:<\/span>)<\/p><ol class="cause-routes">/);
    }
    for (const paragraph of html.matchAll(/<p\b[^>]*>([\s\S]*?)<\/p>/g)) expect(paragraph[1]).not.toMatch(/<(?:ol|ul|div|details)\b/);
    expect(html).not.toContain(ACTIVE_SENTINEL);
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
    const sourceDisclosures = detailsOf(html).filter((details) => details.tag.includes('class="class-provenance"'));
    const observedClasses = Object.values(shape.classes).filter((aggregate) => aggregate.claim.epistemic.label === 'Observed');
    expect(sourceDisclosures.length).toBe(observedClasses.length);
    for (const aggregate of observedClasses) {
      const disclosure = sourceDisclosures.find((entry) => entry.inner.includes(`data-claim-provenance="${aggregate.claim.claimId}"`));
      expect(disclosure).toBeDefined();
      expect(disclosure?.tag).not.toMatch(/\sopen(?:\s|$)/);
    }
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
      expect(details.inner).toContain(`>Show items (${count}) — ${cls}</summary>`);
      // A row is a table row or, for a statement-less class, a list entry.
      expect(details.inner.match(/<(?:tr|li) data-polaris-item="/g)?.length ?? 0).toBe(count);
    }
    expect(exclusionPopulations.length).toBe(1);
    expect(exclusionPopulations[0]?.inner).toContain(`>Show exclusions (${shape.exclusions.length}) — ${shape.claim.claimId}</summary>`);
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
    const links = [...detail.matchAll(/<a href="([^"]+)"[^>]*>Exact text — ([^<]+)<\/a>/g)];
    expect(links.length).toBeGreaterThan(0);
    for (const link of links) {
      expect(decode(link[1] as string)).toContain('/polaris/source?identity=');
      expect(decodeURIComponent(decode(link[1] as string).split('identity=')[1] as string)).toContain('openspec/specs/');
      expect(decode(link[2] as string)).toContain('openspec/specs/');
    }
    // No requirement text is copied onto the page itself: the page cites and
    // routes, the route renders (PWB-REQ-011 non-goal: no copied source).
    expect(html).not.toContain('The switchboard SHALL resolve the sender');
    expect(html).not.toContain('PURPOSE-PROSE-NEVER-RENDERED');
  });
});

// Bead syzygy-u05.4 slice 1 (pursuit 2026-09-22 N4, finding S2-F1): the
// reading layout opens <main> with the legend, so the tuple's definition
// precedes its first use instead of following every claim from the footer.
describe('Polaris legend precedes the first claim tuple (syzygy-u05.4)', () => {
  it('renders one legend and the state-plane line at the top of <main>, before the first data-epistemic element, and none in the footer', () => {
    const { html } = observed();
    const page = html.replace(/<style[\s\S]*?<\/style>/g, '').replace(/<script[\s\S]*?<\/script>/g, '');
    expect(page.match(/class="legend"/g)?.length).toBe(1);
    expect(page.match(/data-surface-state-legend/g)?.length).toBe(1);
    const main = page.indexOf('<main id="main-content">');
    const legend = page.indexOf('class="legend"');
    const stateLine = page.indexOf('data-surface-state-legend');
    const firstTuple = page.search(/<[a-z][^>]*\sdata-epistemic-[a-z-]+=/);
    expect(main).toBeGreaterThan(-1);
    expect(firstTuple).toBeGreaterThan(-1);
    expect(legend).toBeGreaterThan(main);
    expect(stateLine).toBeGreaterThan(legend);
    expect(stateLine).toBeLessThan(firstTuple);
    const footer = /<footer[^>]*>([\s\S]*?)<\/footer>/.exec(page)?.[1] ?? '';
    expect(footer).not.toContain('class="legend"');
    expect(footer).not.toContain('data-surface-state-legend');
  });
});

// Bead syzygy-u05.4 slice 2 (pursuit 2026-09-22 N4; S1-F1, S1-M3, S4-F4,
// S4-F5). Expected counts and claim ids are typed from the fixture, beside
// the model figures they must also equal.
describe('Polaris opening gloss, proof strip and gap entries (syzygy-u05.4)', () => {
  const variants = (): readonly { name: string; html: string }[] => [
    { name: 'observed', html: observed().html },
    { name: 'secret', html: observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET).html },
    { name: 'unevaluated', html: renderPolarisPage(buildFixtureModel(cleanups)) },
    { name: 'rejected', html: renderPolarisPage(buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } })) },
  ];

  it('glosses every value of the first claim tuple before that tuple renders', () => {
    for (const { name, html } of variants()) {
      const tuple = /<span class="claim-tuple"([^>]*)>/.exec(html);
      expect(tuple, name).not.toBeNull();
      const attrs = (tuple as RegExpExecArray)[1] as string;
      const value = (attribute: string): string | undefined => new RegExp(`\\s${attribute}="([^"]*)"`).exec(attrs)?.[1];
      const gloss = /<div class="tuple-gloss" data-polaris-tuple-gloss="([^"]+)"[^>]*>([\s\S]*?)<\/div>/.exec(html);
      expect(gloss, name).not.toBeNull();
      const [whole, claimId, inner] = gloss as RegExpExecArray;
      expect(html.indexOf(whole), name).toBeLessThan((tuple as RegExpExecArray).index);
      expect(claimId, name).toBe(value('data-claim-id'));
      const text = textOf(inner as string);
      const used = [value('data-epistemic-label'), value('data-epistemic-tier'), value('data-epistemic-freshness'), value('data-challenge-state')].filter((entry): entry is string => entry !== undefined);
      expect(used.length, name).toBeGreaterThanOrEqual(3);
      for (const entry of used) expect(text, `${name}: ${entry}`).toContain(`${entry} —`);
      expect(inner, name).toContain('href="#polaris-claim-states"');
    }
  });

  it('puts the proof strip between Purpose and Promises with counts equal to the model and the rendered sources, and routes Unknown without a number', () => {
    for (const [texts, expected] of [[undefined, { sources: 15, items: 20, facts: 44 }], [PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET, { sources: 14, items: 19, facts: 43 }]] as const) {
      const { shape, html } = observed(texts);
      const strip = /<p class="proof-strip"[^>]*>([\s\S]*?)<\/p>/.exec(html);
      expect(strip).not.toBeNull();
      const at = (strip as RegExpExecArray).index;
      expect(at).toBeGreaterThan(html.indexOf('data-polaris-section="claim:project-account:purpose"'));
      expect(at).toBeLessThan(html.indexOf('data-polaris-section="claim:project-account:promises"'));
      const counts = Object.fromEntries([...(strip as RegExpExecArray)[0].matchAll(/data-proof-count="([a-z]+)" data-count="(\d+)">(\d+) /g)].map((match) => {
        expect(match[2]).toBe(match[3]);
        return [match[1], Number(match[2])];
      }));
      expect(counts).toEqual(expected);
      expect(counts).toEqual({ sources: shape.sources.length, items: shape.items.length, facts: shape.facts.length });
      expect(counts['sources']).toBe([...html.matchAll(/\sdata-polaris-source="/g)].length);
      expect(counts).toEqual({ sources: shape.counts.sources, items: shape.counts.items, facts: shape.counts.facts });
      const route = /<a href="#([^"]+)" data-proof-unknown-route[^>]*>([^<]*)<\/a>/.exec((strip as RegExpExecArray)[1] as string);
      expect(route).not.toBeNull();
      expect(html).toContain(`id="${(route as RegExpExecArray)[1]}"`);
      expect((route as RegExpExecArray)[2]).not.toMatch(/\d/);
      for (const target of (strip as RegExpExecArray)[1]?.matchAll(/href="#([^"]+)"/g) ?? []) expect(html).toContain(`id="${target[1]}"`);
    }
  });

  it('makes every claim a gap entry counts findable: its tuples on the page plus the folded members it names', () => {
    const { html } = observed(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET);
    // A gap entry runs to the next entry or the end of its section; its
    // cause list nests <li>s, so no lazy </li> match bounds it.
    const section = /data-polaris-section="shape:gaps"[\s\S]*?<\/section>/.exec(html)?.[0] as string;
    expect([...section.matchAll(/data-polaris-gap="([^"]+)"/g)].map((gap) => gap[1])).toEqual(['excluded-content']);
    const inner = section.slice(section.indexOf('data-polaris-gap="excluded-content"'));
    const stated = Number(/: (\d+) claim\(s\)/.exec(inner)?.[1]);
    expect(stated).toBe(4);
    const shown = new Set([...html.matchAll(/<span class="claim-tuple" data-claim-id="([^"]+)"[^>]*data-epistemic-primary-reason="excluded-content"/g)].map((match) => match[1]));
    const folded = [...(/<span data-polaris-gap-folded="(\d+)">([\s\S]*?)<\/span>/.exec(inner)?.[2] ?? '').matchAll(/<code>([^<]+)<\/code>/g)].map((match) => match[1]);
    expect(folded).toEqual(['claim:fact:count:craft-policy']);
    for (const id of folded) expect(shown.has(id)).toBe(false);
    expect(shown.size + folded.length).toBe(stated);
  });

  it('lists each recorded cause of a gap as its own item', () => {
    const texts = {
      ...PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
      'about/legends-and-lore/0001.md': '# RFC 0001\n<script>x</script>\n',
    };
    const { shape, html } = observed(texts);
    const entry = /<li id="[^"]*" data-polaris-gap="excluded-content">([\s\S]*?)<\/ul>/.exec(html)?.[1] as string;
    expect(entry).toContain('>By cause:</span><ul data-polaris-gap-causes="2">');
    const items = [...entry.split('data-polaris-gap-causes')[1]?.matchAll(/<li>([\s\S]*?)<\/li>/g) ?? []].map((match) => decode(match[1] as string));
    expect(items.length).toBe(2);
    expect(shape.exclusions.length).toBe(2);
    for (const path of ['about/craft-and-care/README.md', 'about/legends-and-lore/0001.md']) {
      expect(items.filter((item) => item.startsWith(`${path} `)).length, path).toBe(1);
    }
  });
});
