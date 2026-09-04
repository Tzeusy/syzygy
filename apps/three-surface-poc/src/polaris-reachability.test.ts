/**
 * PWB task 3.8 (PWB-REQ-011, PWB-REQ-016, PWB-REQ-020; RFC7-13, RFC7-31,
 * RFC7-34): exact sources, coverage populations, contradictions and Unknown
 * reasons stay reachable by keyboard and recoverable by text — never by
 * colour, position or layout alone.
 *
 * The oracle here is structural: it walks the rendered HTML with its own
 * tag scanner and CSS sweep, and compares link targets and marker multisets
 * to the machine answer (the serialized model), importing no rendering
 * code, no copy table and no marker constants. A browser-driven traversal
 * (focus order, accessibility tree) remains task 4.4's recorded gap.
 */
import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel, ProjectShape } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { ADMITTING_AUTHORITY, PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET, REJECTING_AUTHORITY, projectShapeFixtureGit } from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

// ---------------------------------------------------------------------------
// Hand-typed expectations. The four depths PWB-REQ-011 names, the catalog
// categories a reader starts from, and the colour-bearing classes each of
// which must also name its state in text.

const DEPTHS = ['Summary', 'Catalog', 'Detail', 'Exact source'] as const;
const GROUP_IDS = ['overview', 'boundaries', 'architecture', 'v1', 'catalog', 'capability-detail', 'evidence-and-gaps'] as const;
const CATALOG_CLASS_IDS = ['catalog-entry', 'roster-identity', 'design-contract', 'baseline-spec', 'craft-policy'] as const;
const ITEM_CLASS_IDS = [...CATALOG_CLASS_IDS, 'principle', 'topology-component', 'success-criterion'] as const;
const ACCOUNT_KEYS = ['purpose', 'promises', 'refusals', 'architecture', 'v1-scope', 'v1-success'] as const;
const EVIDENCE_IDS = ['sources', 'exclusions', 'contradictions', 'gaps'] as const;
/** A class the stylesheet colours, and the text every element carrying it
 * must contain so the state survives without colour. */
const COLOURED: readonly (readonly [string, RegExp])[] = [
  ['unknown-disclosure', /Unknown/],
  ['proposal', /Proposed change/],
  ['band', /Why this capability|Current intent, verbatim|What is observed/],
  ['claim-tuple', /Observed|Unknown|Inferred/],
];
/** A stated declaration that disagrees with the derived principle count, so
 * the observed page carries one contradiction with an exact-source anchor. */
const STATED_PRINCIPLE_COUNT = { fact: 'count:principle', value: '7', basis: 'stated-summary', anchors: [{ path: 'about/heart-and-soul/vision.md', line: 3 }] } as const;

type Variant = 'unevaluated' | 'rejected' | 'observed' | 'secret';

function modelFor(variant: Variant): PocModel {
  switch (variant) {
    case 'unevaluated':
      return buildFixtureModel(cleanups);
    case 'rejected':
      return buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'observed':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(), statedDeclarations: [STATED_PRINCIPLE_COUNT] } });
    case 'secret':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET) } });
  }
}

function observed(model: PocModel): Extract<ProjectShape, { kind: 'observed' }> {
  const shape = (JSON.parse(JSON.stringify(model)) as PocModel).projectShape;
  if (shape.kind !== 'observed') throw new Error(`expected an observed shape, got ${shape.kind}`);
  return shape;
}

// ---------------------------------------------------------------------------
// The oracle's own HTML tools: ids, hrefs, attribute reads, and a nesting-
// aware element extractor (start tag → matching end tag) that reads no
// production code.

function ids(html: string): Map<string, number> {
  const counts = new Map<string, number>();
  for (const match of html.matchAll(/\sid="([^"]+)"/g)) counts.set(match[1] as string, (counts.get(match[1] as string) ?? 0) + 1);
  return counts;
}

function internalHrefs(html: string): string[] {
  return [...html.matchAll(/\shref="#([^"]+)"/g)].map((match) => match[1] as string);
}

function attr(tag: string, name: string): string | undefined {
  return tag.match(new RegExp(`\\s${name}="([^"]*)"`))?.[1];
}

function classesOf(tag: string): readonly string[] {
  return (attr(tag, 'class') ?? '').split(/\s+/).filter((cls) => cls !== '');
}

interface Element {
  readonly tag: string;
  readonly open: string;
  readonly inner: string;
  readonly start: number;
}

/** Every element whose start tag satisfies `accept`, with its inner HTML
 * found by counting nested same-name tags. */
function elements(html: string, accept: (tag: string, open: string) => boolean): Element[] {
  const found: Element[] = [];
  const tagRe = /<(\/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>/g;
  const opens: { tag: string; open: string; start: number; depth: number }[] = [];
  const depth = new Map<string, number>();
  for (const match of html.matchAll(tagRe)) {
    const closing = match[1] === '/';
    const tag = (match[2] as string).toLowerCase();
    const open = match[0];
    const selfClosing = open.endsWith('/>') || ['br', 'hr', 'meta', 'link', 'img', 'input'].includes(tag);
    if (closing) {
      const current = (depth.get(tag) ?? 1) - 1;
      depth.set(tag, current);
      for (let index = opens.length - 1; index >= 0; index -= 1) {
        const candidate = opens[index] as { tag: string; open: string; start: number; depth: number };
        if (candidate.tag === tag && candidate.depth === current) {
          found.push({ tag, open: candidate.open, inner: html.slice(candidate.start + candidate.open.length, match.index), start: candidate.start });
          opens.splice(index, 1);
          break;
        }
      }
      continue;
    }
    if (selfClosing) continue;
    const current = depth.get(tag) ?? 0;
    if (accept(tag, open)) opens.push({ tag, open, start: match.index as number, depth: current });
    depth.set(tag, current + 1);
  }
  return found.sort((a, b) => a.start - b.start);
}

function text(fragment: string): string {
  return fragment.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<[^>]+>/g, ' ').replace(/&[a-z#0-9]+;/g, ' ').replace(/\s+/g, ' ').trim();
}

function styles(html: string): string {
  return [...html.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map((match) => match[1] as string).join('\n');
}

function depthNav(html: string): Element {
  const nav = elements(html, (tag, open) => tag === 'nav' && classesOf(open).includes('depth-nav'));
  expect(nav.length).toBe(1);
  return nav[0] as Element;
}

function multiset(values: readonly string[]): Map<string, number> {
  const counts = new Map<string, number>();
  for (const value of values) counts.set(value, (counts.get(value) ?? 0) + 1);
  return counts;
}

/** Primary Unknown reasons across every shape claim, counted by the oracle
 * from the machine answer alone. */
function machineGapCounts(shape: ProjectShape): Map<string, number> {
  const claims = shape.kind !== 'observed'
    ? [shape.claim]
    : [shape.claim, ...shape.projectAccount.map((e) => e.claim), ...shape.sources.map((e) => e.claim), ...shape.items.map((e) => e.claim), ...Object.values(shape.classes).map((e) => e.claim), ...shape.facts.map((e) => e.claim)];
  const counts = new Map<string, number>();
  for (const claim of claims) {
    const epistemic = claim.epistemic as { reasons?: { primary: string } };
    if (epistemic.reasons !== undefined) counts.set(epistemic.reasons.primary, (counts.get(epistemic.reasons.primary) ?? 0) + 1);
  }
  return counts;
}

const VARIANTS: readonly Variant[] = ['unevaluated', 'rejected', 'observed', 'secret'];

describe('Polaris keyboard and text reachability (PWB-REQ-011, PWB-REQ-016; RFC7-13, RFC7-31, RFC7-34)', () => {
  it('resolves every internal link to exactly one id in every shape state (no dangling link on any path)', () => {
    for (const variant of VARIANTS) {
      const html = renderPolarisPage(modelFor(variant));
      const idCounts = ids(html);
      const hrefs = internalHrefs(html);
      expect(hrefs.length, variant).toBeGreaterThan(20);
      const dangling = hrefs.filter((target) => idCounts.get(target) !== 1);
      expect(dangling, `${variant}: ${hrefs.length} links`).toEqual([]);
      const duplicates = [...idCounts.entries()].filter(([, count]) => count > 1).map(([id]) => id);
      expect(duplicates, variant).toEqual([]);
    }
  });

  it('lists the four depths as native links in document order, reaching every group, catalog class, capability deep dive and evidence heading the state renders', () => {
    for (const variant of VARIANTS) {
      const model = modelFor(variant);
      const html = renderPolarisPage(model);
      const nav = depthNav(html);
      const levels = elements(nav.inner, (tag, open) => tag === 'li' && attr(open, 'data-depth-level') !== undefined);
      expect(levels.map((level) => attr(level.open, 'data-depth-level'))).toEqual(['1', '2', '3', '4']);
      for (const [index, level] of levels.entries()) expect(text(level.inner).startsWith(DEPTHS[index] as string), `${variant} level ${index + 1}`).toBe(true);

      // Nothing but native links carries the traversal; the nav itself is a
      // labelled landmark, not a colour or a position.
      expect(nav.open).toMatch(/aria-labelledby="polaris-depth-label"/);
      expect(html).toContain('id="polaris-depth-label"');
      expect(nav.inner).not.toMatch(/onclick|role="button"|tabindex/);

      // Document order: every target sits after the nav, in the nav's order.
      const targets = internalHrefs(nav.inner);
      const positions = targets.map((target) => html.indexOf(` id="${target}"`));
      expect(positions.every((position) => position > nav.start)).toBe(true);
      for (let index = 1; index < positions.length; index += 1) expect(positions[index], `${variant}: ${targets[index]} after ${targets[index - 1]}`).toBeGreaterThan(positions[index - 1] as number);

      // Coverage of the population the state renders.
      const expected = new Set<string>([...GROUP_IDS.map((group) => `polaris-group-${group}`)]);
      const observedShape = model.projectShape.kind === 'observed';
      if (observedShape) for (const cls of CATALOG_CLASS_IDS) expected.add(`polaris-class-${cls}`);
      for (const entity of model.entities) if (entity.kind === 'capability') expected.add(`polaris-deep-dive-${entity.id.replace(/[^A-Za-z0-9]+/g, '-')}`);
      for (const part of EVIDENCE_IDS) if (observedShape || part === 'sources' || part === 'gaps') expected.add(`polaris-shape-${part}`);
      expect(new Set(targets)).toEqual(expected);
      expect(targets.length).toBe(expected.size);
    }
  });

  it('follows every catalog category from the depth list to an item row to an exact source row whose identity equals the machine answer (PWB-REQ-011 sweep)', () => {
    const model = modelFor('observed');
    const shape = observed(model);
    const html = renderPolarisPage(model);
    const idCounts = ids(html);
    const sourceByPath = new Map(shape.sources.map((source) => [source.path, source]));
    const itemById = new Map(shape.items.map((item) => [item.claim.claimId, item]));
    let paths = 0;
    const expectedPaths = shape.items.filter((item) => item.class !== 'project-account-section' && item.claim.epistemic.label === 'Observed').length
      + shape.projectAccount.filter((entry) => entry.claim.epistemic.label === 'Observed').length;

    const followToSource = (fragment: string, claimId: string, supportPaths: readonly string[]): void => {
      const citations = [...fragment.matchAll(/<a href="#(polaris-source-[^"]+)"><cite[^>]*>([^<]+)<\/cite><\/a>/g)];
      expect(citations.length, claimId).toBeGreaterThan(0);
      for (const citation of citations) {
        const target = citation[1] as string;
        expect(idCounts.get(target), `${claimId} → ${target}`).toBe(1);
        const row = elements(html, (tag, open) => tag === 'tr' && attr(open, 'id') === target)[0] as Element;
        const path = (citation[2] as string).replace(/:\d+$/, '');
        expect(supportPaths).toContain(path);
        const source = sourceByPath.get(path);
        expect(source, path).toBeDefined();
        // The row states the exact identity the machine answer holds, and its
        // claim id is the source's own.
        expect(text(row.inner)).toContain((source as { identity: string }).identity);
        expect(attr(row.open, 'data-polaris-source')).toBe((source as { claim: { claimId: string } }).claim.claimId);
      }
      paths += 1;
    };

    for (const cls of ITEM_CLASS_IDS) {
      const section = elements(html, (tag, open) => tag === 'section' && attr(open, 'data-polaris-class') === cls)[0];
      expect(section, cls).toBeDefined();
      expect(idCounts.get(`polaris-class-${cls}`)).toBe(1);
      const rows = elements((section as Element).inner, (tag, open) => tag === 'tr' && attr(open, 'data-polaris-item') !== undefined);
      const expectedRows = shape.items.filter((item) => item.class === cls);
      expect(rows.length, cls).toBe(expectedRows.length);
      for (const row of rows) {
        const item = itemById.get(attr(row.open, 'data-polaris-item') as string);
        expect(item).toBeDefined();
        if ((item as { claim: { epistemic: { label: string } } }).claim.epistemic.label !== 'Observed') continue;
        followToSource(row.inner, (item as { claim: { claimId: string } }).claim.claimId, (item as { claim: { support: readonly { path: string }[] } }).claim.support.map((support) => support.path));
      }
    }
    for (const key of ACCOUNT_KEYS) {
      const statement = shape.projectAccount.find((entry) => entry.key === key);
      expect(statement, key).toBeDefined();
      const section = elements(html, (tag, open) => tag === 'section' && attr(open, 'data-polaris-section') === (statement as { claim: { claimId: string } }).claim.claimId)[0];
      expect(section, key).toBeDefined();
      if ((statement as { claim: { epistemic: { label: string } } }).claim.epistemic.label !== 'Observed') continue;
      followToSource((section as Element).inner, key, (statement as { claim: { support: readonly { path: string }[] } }).claim.support.map((support) => support.path));
    }
    expect(expectedPaths).toBeGreaterThan(10);
    expect(paths).toBe(expectedPaths);
  });

  it('gives every contradiction and every Unknown reason a text entry with an id, links each reason mention to its gaps entry and each contradicted declaration to its exact source, matching the machine multisets (PWB-REQ-020)', () => {
    for (const variant of ['observed', 'secret', 'rejected'] as const) {
      const model = modelFor(variant);
      const machine = (JSON.parse(JSON.stringify(model)) as PocModel).projectShape;
      const html = renderPolarisPage(model);
      const idCounts = ids(html);

      // Gaps: one entry per primary reason, named in text with its count and
      // route; the multiset equals the oracle's own count from the model.
      const gaps = elements(html, (tag, open) => tag === 'li' && attr(open, 'data-polaris-gap') !== undefined);
      const rendered = new Map(gaps.map((gap) => [attr(gap.open, 'data-polaris-gap') as string, Number(text(gap.inner).match(/: (\d+) claim/)?.[1])]));
      expect(rendered, variant).toEqual(machineGapCounts(machine));
      expect(gaps.length, variant).toBeGreaterThan(0);
      for (const gap of gaps) {
        const reason = attr(gap.open, 'data-polaris-gap') as string;
        expect(attr(gap.open, 'id')).toBe(`polaris-gap-${reason.replace(/[^A-Za-z0-9]+/g, '-')}`);
        expect(text(gap.inner)).toMatch(new RegExp(`^${reason} ?: \\d+ claim\\(s\\)\\. Route: .+`));
      }
      // Every other mention of a listed reason is a link to that entry; the
      // entry itself is the one unlinked mention.
      for (const reason of rendered.keys()) {
        const mentions = [...html.matchAll(new RegExp(`data-unknown-reason="${reason}"`, 'g'))].length;
        const linked = [...html.matchAll(new RegExp(`<a href="#polaris-gap-${reason.replace(/[^A-Za-z0-9]+/g, '-')}" data-gap-ref="${reason}"><span data-unknown-reason="${reason}">`, 'g'))].length;
        expect(linked, `${variant} ${reason}`).toBe(mentions - 1);
        expect(idCounts.get(`polaris-gap-${reason.replace(/[^A-Za-z0-9]+/g, '-')}`)).toBe(1);
      }
      // A reason the gaps list does not enumerate is text, never a link.
      for (const match of html.matchAll(/<a href="#polaris-gap-[^"]+" data-gap-ref="([^"]+)">/g)) expect(rendered.has(match[1] as string), `${variant} ${match[1]}`).toBe(true);

      // Contradictions: one entry per contradicted fact with an id, the fact
      // named in text, every kept declaration's source linked to its row.
      const facts = elements(html, (tag, open) => tag === 'li' && attr(open, 'data-polaris-fact') !== undefined);
      const machineFacts = machine.kind === 'observed' ? machine.contradictions : [];
      expect(multiset(facts.map((fact) => attr(fact.open, 'data-polaris-fact') as string))).toEqual(multiset(machineFacts.map((fact) => fact.claim.claimId)));
      if (variant === 'observed') expect(facts.length).toBe(1);
      for (const entry of facts) {
        const fact = machineFacts.find((candidate) => candidate.claim.claimId === attr(entry.open, 'data-polaris-fact')) as (typeof machineFacts)[number];
        expect(attr(entry.open, 'id')).toBe(`polaris-fact-${fact.claim.claimId.replace(/[^A-Za-z0-9]+/g, '-')}`);
        expect(text(entry.inner)).toContain(`${fact.fact.fact}: Unknown`);
        expect(text(entry.inner)).toContain('contradicted-pending-adjudication');
        const anchors = fact.fact.declarations.flatMap((declaration) => declaration.anchors.map((anchor) => anchor.line === undefined ? anchor.path : `${anchor.path}:${anchor.line}`));
        const links = [...entry.inner.matchAll(/<a href="#(polaris-source-[^"]+)" data-source-ref="([^"]+)">([^<]+)<\/a>/g)];
        expect(links.map((link) => link[3])).toEqual(anchors);
        for (const link of links) {
          expect(idCounts.get(link[1] as string)).toBe(1);
          expect(machine.kind === 'observed' && machine.sources.some((source) => source.path === link[2])).toBe(true);
        }
        for (const declaration of fact.fact.declarations) expect(text(entry.inner)).toContain(`${declaration.value} (${declaration.basis}`);
      }
    }
  });

  it('carries no pointer-only or layout-only affordance: native controls, named keyboard-scrollable table regions, visible focus, no reordering or hiding rules', () => {
    for (const variant of VARIANTS) {
      const html = renderPolarisPage(modelFor(variant));
      const idCounts = ids(html);
      expect(html).not.toMatch(/\son(click|keydown|keyup|mouse\w+|touch\w+)=/);
      expect(html).not.toMatch(/role="button"|<button/);
      for (const match of html.matchAll(/\stabindex="([^"]*)"/g)) expect(match[1]).toBe('0');
      // Every horizontally scrollable region is a focusable landmark named by
      // a heading the page renders.
      const regions = elements(html, (tag, open) => tag === 'div' && classesOf(open).includes('table-scroll'));
      if (variant === 'observed' || variant === 'secret') expect(regions.length).toBeGreaterThan(5);
      for (const region of regions) {
        expect(attr(region.open, 'role')).toBe('region');
        expect(attr(region.open, 'tabindex')).toBe('0');
        const label = attr(region.open, 'aria-labelledby') as string;
        expect(idCounts.get(label), label).toBe(1);
        expect(html).toMatch(new RegExp(`<h[2-4] id="${label}"`));
        expect(region.inner.startsWith('<table>')).toBe(true);
      }
      const css = styles(html);
      expect(css).toMatch(/\[tabindex\]:focus-visible/);
      expect(css).toMatch(/:focus-visible\s*\{[^}]*outline:\s*\d/);
      const withoutSkipLink = css.replace(/\.skip-link[^{]*\{[^}]*\}/g, '');
      expect(withoutSkipLink).not.toMatch(/outline\s*:\s*(none|0)\b/);
      expect(withoutSkipLink).not.toMatch(/display\s*:\s*none/);
      expect(withoutSkipLink).not.toMatch(/visibility\s*:\s*hidden/);
      expect(withoutSkipLink).not.toMatch(/position\s*:\s*(absolute|fixed)/);
      expect(withoutSkipLink).not.toMatch(/\bfloat\s*:/);
      expect(withoutSkipLink).not.toMatch(/(^|[;{\s])order\s*:/);
      expect(withoutSkipLink).not.toMatch(/flex-direction\s*:\s*(row|column)-reverse/);
    }
  });

  it('names every coloured state in text: each element of a colour-bearing class carries the words that state means', () => {
    for (const variant of VARIANTS) {
      const html = renderPolarisPage(modelFor(variant));
      const css = styles(html);
      let checked = 0;
      for (const [cls, words] of COLOURED) {
        expect(css, cls).toMatch(new RegExp(`\\.${cls}[^{]*\\{[^}]*(color|border)`));
        const found = elements(html, (tag, open) => tag !== 'style' && classesOf(open).includes(cls));
        expect(found.length, `${variant} ${cls}`).toBeGreaterThan(0);
        for (const element of found) {
          expect(text(element.inner), `${variant} ${cls}: ${text(element.inner).slice(0, 80)}`).toMatch(words);
          checked += 1;
        }
      }
      expect(checked).toBeGreaterThan(20);
    }
  });
});
