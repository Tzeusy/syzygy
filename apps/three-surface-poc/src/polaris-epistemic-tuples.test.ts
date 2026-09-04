import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel, ProjectShape, ProjectShapeClaim } from '@syzygy/three-surface-poc-core';

import { denominatorText, reasonCountsBlock, renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
  REJECTING_AUTHORITY,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

// ---------------------------------------------------------------------------
// Hand-typed vocabularies (PWB-REQ-007 oracle independence: nothing here is
// imported from cap1-core or the POC core). RFC2-24 reasons verbatim.
const LABELS = ['Observed', 'Inferred', 'Unknown'] as const;
const TIERS = ['doctrine-statement', 'report-fact', 'derived-fact', 'inference', 'projection', 'suspended', 'unstated'] as const;
const REASONS = [
  'missing-declaration',
  'missing-evidence',
  'no-currency-bound-declared',
  'stale-beyond-currency-bound',
  'mapping-coverage-absent',
  'unconsented-source-or-provider',
  'excluded-content',
  'contradicted-pending-adjudication',
  'challenge-suspended',
  'source-uncaptured-or-unreachable',
  'reference-unresolvable',
  'execution-blocked',
] as const;
const FRESHNESS = ['fresh', 'stale', 'unknown-currency', 'no-bound', 'unstated'] as const;
const CHALLENGE = ['unchallenged'] as const;
/** Words an aggregate must never use about itself: headline status,
 * composite maturity, inferred success, trends or percentages. */
const STATUS_HEADLINES = /\b(healthy|unhealthy|passing|failing|maturity|score|on track|at risk|trend|trending|success rate)\b|\d+\s?%/i;

function attribute(tag: string, name: string): string | undefined {
  return new RegExp(`\\s${name}="([^"]*)"`).exec(tag)?.[1];
}

function textOf(html: string): string {
  return html.replace(/<style[\s\S]*?<\/style>/g, '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
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

type Variant = 'unevaluated' | 'rejected' | 'observed' | 'observed-with-secret';
const VARIANTS: readonly Variant[] = ['unevaluated', 'rejected', 'observed', 'observed-with-secret'];

function modelFor(variant: Variant): PocModel {
  switch (variant) {
    case 'unevaluated':
      return buildFixtureModel(cleanups);
    case 'rejected':
      return buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'observed':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'observed-with-secret':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET) } });
  }
}

const TUPLE_FIELDS = ['data-claim-id', 'data-epistemic-label', 'data-epistemic-tier', 'data-epistemic-primary-reason', 'data-epistemic-secondary-reasons', 'data-epistemic-freshness', 'data-challenge-state', 'data-evaluation-id'] as const;

describe('Polaris complete epistemic tuples (PWB-REQ-007; RFC2-24, RFC6-14, RFC7-16)', () => {
  it('renders every tuple with every field present, in vocabulary, and equal to the machine answer, over every shape state', () => {
    let totalTuples = 0;
    let unknownTuples = 0;
    for (const variant of VARIANTS) {
      const model = modelFor(variant);
      const html = renderPolarisPage(model);
      const machine = JSON.parse(JSON.stringify(model)) as PocModel;
      const claimsById = new Map(allShapeClaims(machine.projectShape).map((claim) => [claim.claimId, claim]));
      const tuples = [...html.matchAll(/<span class="claim-tuple"[^>]*>([^<]*)<\/span>/g)];
      expect(tuples.length).toBeGreaterThan(0);
      for (const match of tuples) {
        const tag = match[0];
        const text = match[1] as string;
        for (const field of TUPLE_FIELDS) expect(attribute(tag, field), `${variant}: ${field} absent on ${tag}`).toBeDefined();
        const label = attribute(tag, 'data-epistemic-label') as string;
        const tier = attribute(tag, 'data-epistemic-tier') as string;
        const primary = attribute(tag, 'data-epistemic-primary-reason') as string;
        const secondary = (attribute(tag, 'data-epistemic-secondary-reasons') as string).split(',').filter((reason) => reason !== '');
        const freshness = attribute(tag, 'data-epistemic-freshness') as string;
        const challenge = attribute(tag, 'data-challenge-state') as string;
        const evaluationId = attribute(tag, 'data-evaluation-id') as string;
        expect(LABELS).toContain(label);
        expect(TIERS).toContain(tier);
        expect(FRESHNESS).toContain(freshness);
        expect(CHALLENGE).toContain(challenge);
        expect(evaluationId).not.toBe('');
        if (label === 'Unknown') {
          unknownTuples += 1;
          expect(primary === 'deferred' || (REASONS as readonly string[]).includes(primary), `${variant}: reason ${primary}`).toBe(true);
          for (const reason of secondary) {
            expect(REASONS).toContain(reason);
            expect(reason).not.toBe(primary);
          }
          expect(text).toContain(`Unknown (${primary}`);
        } else {
          expect(primary).toBe('none');
          expect(secondary).toEqual([]);
        }
        // Text and attributes agree.
        expect(text).toContain(`· ${tier} · ${freshness} · ${challenge}`);
        // Machine answer carries the identical tuple.
        const claim = claimsById.get(attribute(tag, 'data-claim-id') as string);
        expect(claim, `${variant}: tuple for a claim not in the machine answer: ${tag}`).toBeDefined();
        if (claim === undefined) continue;
        expect(label).toBe(claim.epistemic.label);
        expect(tier).toBe(claim.epistemic.tier ?? 'unstated');
        expect(freshness).toBe(claim.epistemic.freshness ?? 'unstated');
        expect(challenge).toBe(claim.challenge);
        expect(evaluationId).toBe(claim.evaluationId);
        if ('reasons' in claim.epistemic) {
          expect(primary).toBe(claim.epistemic.reasons.primary);
          expect(secondary).toEqual([...claim.epistemic.reasons.secondary]);
          // Every carried reason has a route, and the primary's route is rendered beside the claim.
          const routes = new Map(claim.resolutionRoutes.map((route) => [route.reason, route.route]));
          for (const reason of [primary, ...secondary]) expect(routes.get(reason as never), `${variant}: no route for ${reason}`).toBeTruthy();
          expect(html).toContain(`data-unknown-reason="${primary}"`);
          expect(html).toContain(`Route: ${routes.get(primary as never) as string}`);
        }
        totalTuples += 1;
      }
    }
    expect(totalTuples).toBeGreaterThan(60);
    expect(unknownTuples).toBeGreaterThan(3);
  });

  it('discloses each aggregate as label, tier, freshness and separate primary/secondary reason counts, with coverage counts only on demand and no headline status', () => {
    for (const variant of ['observed', 'observed-with-secret'] as const) {
      const model = modelFor(variant);
      const html = renderPolarisPage(model);
      const machine = JSON.parse(JSON.stringify(model)) as PocModel;
      const shape = machine.projectShape;
      if (shape.kind !== 'observed') throw new Error('fixture must observe');
      let classesChecked = 0;
      for (const [cls, aggregate] of Object.entries(shape.classes)) {
        const start = html.indexOf(`data-polaris-section="claim:class:${cls}"`);
        expect(start, `${variant}: class ${cls} section`).toBeGreaterThan(-1);
        const end = html.indexOf('</section>', start);
        const section = html.slice(start, end);
        // The aggregate's own tuple, once.
        expect(section.split(`data-claim-id="claim:class:${cls}"`).length - 1).toBe(1);
        // Reason counts: exactly the machine's primary and secondary maps.
        const block = /<div class="reason-counts"[^>]*>([\s\S]*?)<\/div>/.exec(section)?.[1] ?? '';
        expect(block).not.toBe('');
        for (const which of ['primary', 'secondary'] as const) {
          const expected = Object.entries(aggregate.reasonCounts[which]).filter(([, count]) => (count ?? 0) > 0);
          const list = new RegExp(`<ul data-reason-counts-${which}="claim:class:${cls}"[^>]*>([\\s\\S]*?)</ul>`).exec(block)?.[1];
          if (expected.length === 0) {
            expect(list, `${variant}: ${cls} ${which} list rendered without members`).toBeUndefined();
            continue;
          }
          expect(list, `${variant}: ${cls} ${which} list missing`).toBeDefined();
          const rendered = [...(list as string).matchAll(/<li data-reason="([^"]+)" data-count="(\d+)">/g)].map((m) => [m[1], Number(m[2])] as const);
          expect(rendered.map(([reason]) => reason).sort()).toEqual(expected.map(([reason]) => reason).sort());
          for (const [reason, count] of rendered) {
            expect(count).toBe(aggregate.reasonCounts[which][reason as never]);
            expect(REASONS).toContain(reason);
            // The reason may be linked to its gaps-list entry (task 3.8); the
            // text and count beside it are what this oracle compares.
            expect((list as string)).toMatch(new RegExp(`data-unknown-reason="${reason}">${reason}</span>(</a>)?: ${count}\\. Route: `));
          }
        }
        if (Object.values(aggregate.reasonCounts.primary).every((count) => (count ?? 0) === 0) && Object.values(aggregate.reasonCounts.secondary).every((count) => (count ?? 0) === 0)) {
          expect(block).toContain('No member claim carries an Unknown reason.');
        }
        // Counts only on demand: inside <details>, never in the default text.
        const details = /<details class="coverage-counts"[^>]*>([\s\S]*?)<\/details>/.exec(section);
        expect(details, `${variant}: ${cls} on-demand counts`).not.toBeNull();
        const defaultText = textOf(section.replace(/<details[\s\S]*?<\/details>/g, '').replace(/<table[\s\S]*?<\/table>/g, ''));
        expect(defaultText).not.toMatch(/\b\d+ (declared|modeled|contradicted)\b/);
        expect(defaultText).not.toMatch(STATUS_HEADLINES);
        // Unknown is never folded into a total: the on-demand text keeps the
        // three states apart and they reconcile to the declared count.
        const countsText = textOf(details?.[1] ?? '');
        expect(countsText).toContain(`${aggregate.modeled} modeled, ${aggregate.unknown} Unknown, ${aggregate.contradicted} contradicted`);
        if (aggregate.denominator.kind === 'known') {
          expect(countsText).toContain(`${aggregate.denominator.value} declared`);
          expect(aggregate.modeled + aggregate.unknown + aggregate.contradicted).toBe(aggregate.denominator.value);
        } else {
          expect(countsText).toContain('denominator Unknown');
        }
        classesChecked += 1;
      }
      expect(classesChecked).toBe(9);
      // The whole-shape aggregate follows the same rule.
      const wholeStart = html.indexOf('data-polaris-section="claim:project-shape"');
      const whole = html.slice(wholeStart, html.indexOf('</section>', wholeStart));
      expect(whole).toContain('data-reason-counts="claim:project-shape"');
      expect(whole).toContain('data-coverage-counts="claim:project-shape"');
      expect(textOf(whole.replace(/<details[\s\S]*?<\/details>/g, ''))).not.toMatch(/\b\d+ (items|sources readable|modeled)\b/);
      // Nothing on the page claims a headline status, maturity, success rate or trend.
      expect(textOf(html)).not.toMatch(STATUS_HEADLINES);
    }
  });

  it('keeps the same semantic claim identity across two evaluation instances while the evaluation id differs', () => {
    const first = modelFor('observed');
    const second = modelFor('observed');
    const ids = (model: PocModel): string[] => allShapeClaims(model.projectShape).map((claim) => claim.claimId).sort();
    expect(ids(first)).toEqual(ids(second));
    const evaluationIds = (model: PocModel): Set<string> => new Set(allShapeClaims(model.projectShape).map((claim) => claim.evaluationId));
    expect(evaluationIds(first).size).toBe(1);
    expect(evaluationIds(second).size).toBe(1);
    const firstHtml = renderPolarisPage(first);
    const secondHtml = renderPolarisPage(second);
    const tupleIds = (html: string): string[] => [...html.matchAll(/<span class="claim-tuple" data-claim-id="([^"]+)"/g)].map((m) => m[1] as string).sort();
    expect(tupleIds(firstHtml)).toEqual(tupleIds(secondHtml));
    for (const evaluationId of evaluationIds(first)) expect(firstHtml).toContain(`data-evaluation-id="${evaluationId}"`);
  });

  it('keeps Unknown apart from modeled and secondary apart from primary at the exported seams (states the fixtures cannot reach)', () => {
    // Coverage counts: the three states are printed separately and never summed.
    expect(denominatorText({ denominator: { kind: 'known', value: 7 }, modeled: 4, unknown: 2, contradicted: 1, sourcesWithUnknownDenominator: 0 }))
      .toBe('7 declared; 4 modeled, 2 Unknown, 1 contradicted; 0 source(s) unreadable.');
    expect(denominatorText({ denominator: { kind: 'unknown', reasons: ['excluded-content'] }, modeled: 0, unknown: 0, contradicted: 0, sourcesWithUnknownDenominator: 1 }))
      .toBe('denominator Unknown (excluded-content); 0 modeled, 0 Unknown, 0 contradicted; 1 source(s) unreadable.');
    // Reason counts: primary and secondary lists are separate, each row routed.
    const html = reasonCountsBlock('claim:class:vision', {
      primary: { 'missing-declaration': 2, 'excluded-content': 1 },
      secondary: { 'stale-beyond-currency-bound': 1 },
    });
    expect(html).toContain('Primary Unknown reasons among members:');
    expect(html).toContain('Secondary Unknown reasons among members:');
    const primary = /<ul data-reason-counts-primary="claim:class:vision"[^>]*>([\s\S]*?)<\/ul>/.exec(html)?.[1] ?? '';
    const secondary = /<ul data-reason-counts-secondary="claim:class:vision"[^>]*>([\s\S]*?)<\/ul>/.exec(html)?.[1] ?? '';
    expect([...primary.matchAll(/data-reason="([^"]+)" data-count="(\d+)"/g)].map((m) => `${m[1]}=${m[2]}`)).toEqual(['missing-declaration=2', 'excluded-content=1']);
    expect([...secondary.matchAll(/data-reason="([^"]+)" data-count="(\d+)"/g)].map((m) => `${m[1]}=${m[2]}`)).toEqual(['stale-beyond-currency-bound=1']);
    expect(secondary).toContain('stale-beyond-currency-bound</span>: 1. Route: ');
    expect(html.split('data-reason-counts-primary=').length - 1).toBe(1);
    expect(html.split('data-reason-counts-secondary=').length - 1).toBe(1);
    expect(reasonCountsBlock('claim:class:vision', { primary: {}, secondary: {} })).toContain('No member claim carries an Unknown reason.');
  });
});
