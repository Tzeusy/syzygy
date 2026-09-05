// PWB-REQ-021 readiness on the one surface (as amended 2026-09-05): the
// production traversal predicate, the model seam, the Polaris block and
// its parity with the machine channel, and the separation from PWB-REQ-022.
//
// Oracle independence: the identities, arm names and state words are
// hand-typed; the human channel is read by a plain extractor over the
// served HTML and compared with the machine answer (`JSON.stringify(model)`
// parsed back) as multisets with denominators.
import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { PWB_RESOURCE_LIMITS, type PocModel } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { ADMITTING_AUTHORITY, PROJECT_SHAPE_FIXTURE_TEXTS, PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET, REJECTING_AUTHORITY, projectShapeFixtureGit } from './test-project-shape-fixture.js';
import { fixtureAnswers, walkthroughJudgmentFixture, type FixtureAnswer, type JudgmentFixtureState } from './test-walkthrough-judgment-fixture.js';
import { pwbReadinessTraversal } from './walkthrough-inputs.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

const IDENTITIES = ['why', 'promises', 'refusals-and-rule', 'capabilities-and-fit', 'exact-requirement', 'unknown-or-contradiction', 'claim-strength', 'architecture-and-groups', 'v1-success'];
const ROOT_EXACT_SOURCE = '/polaris#polaris-source-about-README-md';

function decode(text: string): string {
  return text.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}
function readinessSlice(html: string): string {
  const start = html.indexOf('<section class="claim-section" data-polaris-section="walkthrough-readiness"');
  expect(start).toBeGreaterThan(-1);
  const end = html.indexOf('</section>', start);
  return html.slice(start, end);
}
function attrValues(slice: string, attribute: string): string[] {
  return [...slice.matchAll(new RegExp(`\\s${attribute}="([^"]*)"`, 'g'))].map((match) => decode(match[1] as string));
}
function leafTexts(slice: string, attribute: string): string[] {
  return [...slice.matchAll(new RegExp(`<[a-z]+[^>]*\\s${attribute}(?:="[^"]*")?[^>]*>([^<]*)<`, 'g'))].map((match) => decode(match[1] as string));
}
function state(html: string): string {
  return attrValues(readinessSlice(html), 'data-polaris-readiness')[0] as string;
}

interface Scenario {
  readonly shape?: 'observed' | 'rejected';
  readonly judgment?: JudgmentFixtureState;
  readonly traversed?: readonly string[];
  readonly answers?: readonly FixtureAnswer[] | null;
}
function modelFor(scenario: Scenario): PocModel {
  return buildFixtureModel(cleanups, {
    ...(scenario.shape === undefined
      ? {}
      : { projectShape: { authority: scenario.shape === 'observed' ? ADMITTING_AUTHORITY : REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() } }),
    ...(scenario.judgment === undefined
      ? {}
      : {
          walkthroughJudgment: walkthroughJudgmentFixture(scenario.judgment, 'judgment-eval-0001', {
            ...(scenario.traversed === undefined ? {} : { traversed: scenario.traversed }),
            ...(scenario.answers === undefined ? {} : { answers: scenario.answers }),
          }),
        }),
  });
}
function readinessOf(model: PocModel): Extract<PocModel['walkthroughReadiness'], { kind: 'evaluated' }>['readiness'] {
  const machine = (JSON.parse(JSON.stringify(model)) as PocModel).walkthroughReadiness;
  if (machine.kind !== 'evaluated') throw new Error(`readiness ${machine.kind}`);
  return machine.readiness;
}
function armsOf(model: PocModel): string[] {
  const readiness = readinessOf(model);
  if (readiness.kind !== 'evaluated') throw new Error(readiness.kind);
  return [...new Set(readiness.findings.map((finding) => finding.arm))].sort();
}

describe('PWB-REQ-021 readiness traversal (production predicate)', () => {
  const traversal = pwbReadinessTraversal();
  const sources = Object.keys(PROJECT_SHAPE_FIXTURE_TEXTS);
  it('admits Polaris itself, direct and through the tailnet mount, and nothing else as a bare route', () => {
    expect(traversal.polarisRoutes).toEqual(['/polaris', '/butlers-syzygy/polaris']);
    for (const other of ['/', '/trajectory', '/orrery', '/trajectory/materialize', '/polaris/', '/api/poc']) {
      expect(traversal.polarisRoutes).not.toContain(other);
      expect(traversal.isExactSourceRoute(other, sources)).toBe(false);
    }
  });
  it('admits an exact-source fragment only on a Polaris route and only for a source of this evaluation', () => {
    expect(traversal.isExactSourceRoute(ROOT_EXACT_SOURCE, sources)).toBe(true);
    expect(traversal.isExactSourceRoute('/butlers-syzygy/polaris#polaris-source-about-heart-and-soul-vision-md', sources)).toBe(true);
    expect(traversal.isExactSourceRoute('/polaris#polaris-source-about-elsewhere-md', sources)).toBe(false);
    expect(traversal.isExactSourceRoute(ROOT_EXACT_SOURCE, [])).toBe(false);
    expect(traversal.isExactSourceRoute('/trajectory#polaris-source-about-README-md', sources)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris#polaris-fact-about-README-md', sources)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris#', sources)).toBe(false);
  });
});

describe('PWB-REQ-021 readiness on Polaris', () => {
  it('is ready for a Polaris-only record whose nine answers anchor into the observed shape, and the judgment stays its own fact', () => {
    const model = modelFor({ shape: 'observed', judgment: 'lawful-state-1', traversed: ['/polaris', ROOT_EXACT_SOURCE] });
    const readiness = readinessOf(model);
    expect(readiness.kind).toBe('evaluated');
    expect(readiness.ready).toBe(true);
    // The exact-source fragment is outside PWB-REQ-022's route population, so
    // the judgment is unlawful while readiness is true: the two never merge.
    expect(model.walkthroughJudgment.kind === 'evaluated' && model.walkthroughJudgment.evaluation.outcome.kind).toBe('unlawful');
    const html = renderPolarisPage(model);
    const slice = readinessSlice(html);
    expect(state(html)).toBe('ready');
    expect(leafTexts(slice, 'data-polaris-readiness-state')).toEqual(['ready']);
    expect(attrValues(slice, 'data-polaris-answer')).toEqual(IDENTITIES);
    expect(attrValues(slice, 'data-polaris-readiness-arm')).toEqual([]);
    expect(leafTexts(slice, 'data-polaris-readiness-traversed')).toEqual(['/polaris', ROOT_EXACT_SOURCE]);
    expect(leafTexts(slice, 'data-polaris-readiness-surface')).toEqual(['polaris@0.3.0']);
    expect(leafTexts(slice, 'data-polaris-readiness-evaluation')).toEqual(['eval-0007']);
    // The binding a record must name, from the machine channel, verbatim.
    const expected = readinessOf(model).expected;
    expect(leafTexts(slice, 'data-polaris-readiness-expected-surface')).toEqual([expected.surfaceVersion]);
    expect(leafTexts(slice, 'data-polaris-readiness-expected-evaluation')).toEqual([expected.evaluationIdentity]);
    // The block carries no verdict value, no criterion result and no score.
    const text = slice.replace(/<[^>]+>/g, ' ');
    expect(text).not.toMatch(/=met\b|=not-met\b|verdict-unlawful|\bscore:|\d+\s?%|\bhealthy\b|\bpassing\b/i);
  });

  it('is ready and lawful together for a `/polaris`-only record', () => {
    const model = modelFor({ shape: 'observed', judgment: 'lawful-state-1', traversed: ['/polaris'] });
    expect(readinessOf(model).ready).toBe(true);
    expect(model.walkthroughJudgment.kind === 'evaluated' && model.walkthroughJudgment.evaluation.outcome.kind).toBe('lawful');
  });

  it('an excluded source anchors but is no authority: the population carries the evaluation\u2019s own admission', () => {
    const excluded = 'about/craft-and-care/README.md';
    const answers: FixtureAnswer[] = fixtureAnswers().map((answer) => (answer.identity === 'exact-requirement' ? { ...answer, sources: [`${excluded}:1`], authority: excluded } : answer));
    const model = buildFixtureModel(cleanups, {
      projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET) },
      walkthroughJudgment: walkthroughJudgmentFixture('lawful-state-1', 'judgment-eval-0001', { traversed: ['/polaris'], answers }),
    });
    expect(model.projectShape.kind === 'observed' && model.projectShape.sources.find((source) => source.path === excluded)?.record.outcome).toBe('excluded');
    const readiness = readinessOf(model);
    if (readiness.kind !== 'evaluated') throw new Error(readiness.kind);
    expect(readiness.findings.map((finding) => finding.arm)).toEqual(['authority-unresolvable']);
    const exact = readiness.answers.find((answer) => answer.identity === 'exact-requirement');
    expect(exact?.anchors).toEqual([{ path: excluded, line: 1, resolved: true }]);
    expect(exact?.authority).toEqual({ path: excluded, resolved: false });
  });

  it('keeps human and machine channels in parity: answers, own words, anchors, authority, findings', () => {
    const answers: FixtureAnswer[] = fixtureAnswers().map((answer) =>
      answer.identity === 'why'
        ? { ...answer, text: 'Own <words> & "quotes" — kept verbatim.', sources: ['about/README.md:2', 'about/heart-and-soul/vision.md:1', 'about/nowhere.md:9'] }
        : answer.identity === 'promises'
          ? { ...answer, text: '' }
          : answer,
    );
    const model = modelFor({ shape: 'observed', judgment: 'lawful-state-1', traversed: ['/polaris', '/orrery'], answers });
    const readiness = readinessOf(model);
    if (readiness.kind !== 'evaluated') throw new Error(readiness.kind);
    expect(readiness.ready).toBe(false);
    const html = renderPolarisPage(model);
    const slice = readinessSlice(html);
    expect(state(html)).toBe('not-ready');
    const humanArms = attrValues(slice, 'data-polaris-readiness-arm').sort();
    const machineArms = readiness.findings.map((finding) => finding.arm).sort();
    expect(humanArms).toEqual(machineArms);
    expect(machineArms).toEqual(['anchor-unresolved', 'answer-empty', 'path-outside-polaris']);
    expect(leafTexts(slice, 'data-polaris-readiness-finding')).toEqual(readiness.findings.map((finding) => finding.detail));
    expect(attrValues(slice, 'data-polaris-answer')).toEqual(readiness.answers.map((answer) => answer.identity));
    expect(leafTexts(slice, 'data-polaris-answer-text')).toEqual(readiness.answers.map((answer) => answer.text));
    expect(readiness.answers[0]?.text).toBe('Own <words> & "quotes" — kept verbatim.');
    const humanAnchors = attrValues(slice, 'data-polaris-answer-anchor');
    const machineAnchors = readiness.answers.flatMap((answer) => answer.anchors.map((anchor) => `${anchor.path}:${anchor.line}`));
    expect(humanAnchors).toEqual(machineAnchors);
    expect(humanAnchors).toHaveLength(11);
    expect(attrValues(slice, 'data-polaris-anchor-resolved')).toEqual(readiness.answers.flatMap((answer) => answer.anchors.map((anchor) => (anchor.resolved ? 'yes' : 'no'))));
    expect(attrValues(slice, 'data-polaris-anchor-resolved').filter((value) => value === 'no')).toEqual(['no']);
    expect(attrValues(slice, 'data-polaris-answer-authority')).toEqual(['about/README.md']);
    expect(attrValues(slice, 'data-polaris-authority-resolved')).toEqual(['yes']);
    // Own words carry the disclosure role, never the project-fact role.
    const answersBlock = slice.slice(slice.indexOf('data-polaris-answers'));
    expect(answersBlock).not.toContain('data-copy-role="project-fact"');
    expect(answersBlock).not.toContain('data-claim-role="anchored-project-fact"');
  });

  it('the default fixture record (through `/entry`) is not ready for path-outside-polaris even when the judgment is lawful', () => {
    const model = modelFor({ shape: 'observed', judgment: 'lawful-state-1' });
    expect(armsOf(model)).toEqual(['path-outside-polaris']);
    expect(model.walkthroughJudgment.kind === 'evaluated' && model.walkthroughJudgment.evaluation.outcome.kind).toBe('lawful');
    expect(state(renderPolarisPage(model))).toBe('not-ready');
  });

  it('without an observed shape nothing resolves: anchors, the cited authority and the exact-source route', () => {
    for (const shape of [undefined, 'rejected'] as const) {
      const model = modelFor({ ...(shape === undefined ? {} : { shape }), judgment: 'lawful-state-1', traversed: ['/polaris', ROOT_EXACT_SOURCE] });
      expect(armsOf(model)).toEqual(['anchor-unresolved', 'authority-unresolvable', 'path-outside-polaris']);
    }
  });

  it('a resource breach in the evaluation makes readiness false', () => {
    // Deliberately tiny envelope: the fixture tree breaches it.
    const model = buildFixtureModelWithBreach();
    expect(armsOf(model)).toContain('resource-breach');
  });

  it('an unlawful judgment does not make readiness false, and a not-ready record does not make the judgment unlawful', () => {
    const unlawful = modelFor({ shape: 'observed', judgment: 'unlawful', traversed: ['/polaris'] });
    expect(readinessOf(unlawful).ready).toBe(true);
    expect(unlawful.walkthroughJudgment.kind === 'evaluated' && unlawful.walkthroughJudgment.evaluation.outcome.kind).toBe('unlawful');
    const notReady = modelFor({ shape: 'observed', judgment: 'lawful-state-1', traversed: ['/polaris'], answers: null });
    expect(armsOf(notReady)).toEqual(['answer-missing']);
    expect(notReady.walkthroughJudgment.kind === 'evaluated' && notReady.walkthroughJudgment.evaluation.outcome.kind).toBe('lawful');
    expect(JSON.stringify(notReady.walkthroughReadiness)).not.toContain('verdict-unlawful');
  });

  it('renders no-run-record and not-evaluated as their own states, never as not-ready', () => {
    // When the record names another surface than the evaluation expects, the
    // page shows both: the record's under the readiness marker, the expected
    // one under the expected marker — never one for the other.
    const fixture = walkthroughJudgmentFixture('lawful-state-1', 'judgment-eval-0001', { traversed: ['/polaris'] });
    const mismatched = buildFixtureModel(cleanups, {
      projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() },
      walkthroughJudgment: { ...fixture, expectations: { ...fixture.expectations, surfaceVersion: 'polaris@0.9.9' } },
    });
    const mismatchedSlice = readinessSlice(renderPolarisPage(mismatched));
    expect(leafTexts(mismatchedSlice, 'data-polaris-readiness-surface')).toEqual(['polaris@0.3.0']);
    expect(leafTexts(mismatchedSlice, 'data-polaris-readiness-expected-surface')).toEqual(['polaris@0.9.9']);
    const absent = modelFor({ shape: 'observed', judgment: 'absent-run-record' });
    expect(absent.walkthroughReadiness.kind === 'evaluated' && absent.walkthroughReadiness.readiness.kind).toBe('no-run-record');
    const absentHtml = renderPolarisPage(absent);
    expect(state(absentHtml)).toBe('no-run-record');
    // Even with no record, the page says which binding a record must name.
    const absentSlice = readinessSlice(absentHtml);
    const expected = absent.walkthroughReadiness.kind === 'evaluated' ? absent.walkthroughReadiness.readiness.expected : undefined;
    expect(leafTexts(absentSlice, 'data-polaris-readiness-expected-surface')).toEqual([expected?.surfaceVersion]);
    expect(leafTexts(absentSlice, 'data-polaris-readiness-expected-evaluation')).toEqual([expected?.evaluationIdentity]);
    const none = modelFor({ shape: 'observed' });
    expect(none.walkthroughReadiness.kind).toBe('not-evaluated');
    const html = renderPolarisPage(none);
    expect(state(html)).toBe('not-evaluated');
    expect(readinessSlice(html)).not.toContain('data-polaris-answer');
  });
});

function buildFixtureModelWithBreach(): PocModel {
  // A 64-byte evaluation-wide body budget: the fixture tree breaches it in
  // phase B, the breached sources stay counted-and-Unknown, and the model
  // carries the breaches the readiness population reads.
  const model = buildFixtureModel(cleanups, {
    projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(), resourceLimits: { ...PWB_RESOURCE_LIMITS, maxTotalBytes: 64 } },
    walkthroughJudgment: walkthroughJudgmentFixture('lawful-state-1', 'judgment-eval-0001', { traversed: ['/polaris'] }),
  });
  if (model.projectShape.kind !== 'observed') throw new Error(`fixture: ${model.projectShape.kind}`);
  expect(model.projectShape.limitBreaches.length).toBeGreaterThan(0);
  return model;
}
