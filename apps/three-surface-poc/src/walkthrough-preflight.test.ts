// Walkthrough preflight (PWB-LIVE-12): the fixture evaluation that renders
// six backed account statements, four reconciled populations, a reachable
// exact requirement, visible Unknowns and the claim-state glossary is
// ready; then one counterexample per limb, each mutating one input — the
// model, the page bytes, a route outcome or the browser check — and each
// naming the one limb that must fail. Pure: no daemon, no Butlers.

import { createHash } from 'node:crypto';
import { rmSync } from 'node:fs';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import type { PocModel } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { resolveSourceRoute } from './polaris-source.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';
import { verbatimRouteReader } from './verbatim-route.js';
import {
  PREFLIGHT_LIMBS,
  evaluateWalkthroughPreflight,
  presentedShapeClaims,
  type BrowserCheckInput,
  type PreflightLimb,
  type SourceRouteOutcome,
  type WalkthroughPreflightInputs,
} from './walkthrough-preflight.js';

const cleanups: string[] = [];
afterAll(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

/** The baseline spec (an exact requirement to reach) and one excluded
 * source (a legitimate visible Unknown) in the same tree. */
const TEXTS: Readonly<Record<string, string>> = { ...PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC, ...PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET };

function sha1Blob(bytes: Uint8Array): string {
  return createHash('sha1').update(`blob ${bytes.byteLength}\0`).update(bytes).digest('hex');
}

function blobReaderFor(texts: Readonly<Record<string, string>>): (objectId: string) => Uint8Array | undefined {
  const encoder = new TextEncoder();
  const byOid = new Map(Object.values(texts).map((text) => {
    const body = encoder.encode(text);
    return [sha1Blob(body), body] as const;
  }));
  return (objectId) => byOid.get(objectId);
}

function browserCheckFor(model: PocModel): BrowserCheckInput {
  return { kind: 'performed', commit: model.observerRevision, variants: 3, violations: 0 };
}

/** Build the evaluation and answer its exact-source routes the way the
 * demo does against a live daemon, here through the route resolver. */
function inputsFor(texts: Readonly<Record<string, string>>): WalkthroughPreflightInputs {
  const model = buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(texts) } });
  const reader = verbatimRouteReader(model, blobReaderFor(texts));
  const polarisHtml = renderPolarisPage(model, '', {}, { verbatim: reader });
  const sourceRoutes = new Map<string, SourceRouteOutcome>();
  for (const identity of new Set(Array.from(polarisHtml.matchAll(/data-source-route="([^"]*)"/g), (match) => match[1] as string))) {
    const resolved = resolveSourceRoute(model, identity, reader);
    sourceRoutes.set(identity, resolved.kind === 'rendered' ? { state: 'rendered', requirements: resolved.resolution.requirements.length } : { state: 'not-rendered', reason: resolved.reason });
  }
  return { model, polarisHtml, sourceRoutes, browserCheck: browserCheckFor(model) };
}

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

type Observed = Extract<PocModel['projectShape'], { kind: 'observed' }>;

function observedOf(model: PocModel): Observed {
  if (model.projectShape.kind !== 'observed') throw new Error(model.projectShape.kind);
  return model.projectShape;
}

function withShape(model: PocModel, edit: (shape: Observed) => void): PocModel {
  const copy = clone(model);
  edit(observedOf(copy));
  return copy;
}

function replaceOnce(html: string, needle: string, replacement: string): string {
  const at = html.indexOf(needle);
  if (at < 0) throw new Error(`fixture page lacks ${needle}`);
  return `${html.slice(0, at)}${replacement}${html.slice(at + needle.length)}`;
}

let ready: WalkthroughPreflightInputs;
let currentIdentity: string;

beforeAll(() => {
  ready = inputsFor(TEXTS);
  const identity = evaluateWalkthroughPreflight(ready).observed.exactRequirement.identity;
  if (identity === null) throw new Error('fixture reaches no exact requirement');
  currentIdentity = identity;
});

describe('walkthrough preflight: the ready case', () => {
  it('is ready for the fixture evaluation, and its counts are the page’s', () => {
    const result = evaluateWalkthroughPreflight(ready);
    expect(result.findings).toEqual([]);
    expect(result.ready).toBe(true);
    expect(result.observed.accountStatementsBacked).toBe(6);
    expect(result.observed.populations).toEqual({
      principle: { modeled: 2, denominator: 2, rows: 2 },
      'success-criterion': { modeled: 3, denominator: 3, rows: 3 },
      'catalog-entry': { modeled: 3, denominator: 3, rows: 3 },
      'topology-component': { modeled: 1, denominator: 1, rows: 1 },
    });
    expect(result.observed.exactRequirement.requirements).toBe(2);
    expect(result.observed.unknownsVisible).toBe(3);
    expect(result.observed.unknownsMachine).toBe(3);
    expect(result.observed.sourceRoutesLinked).toBe(2);
    expect(result.observed.claimTuples).toBe(ready.polarisHtml.split('<span class="claim-tuple"').length - 1);
    // Never a verdict, a score or an owner answer.
    const json = JSON.stringify(result);
    for (const word of ['verdict', 'score', '"met"', 'answers']) expect(json).not.toContain(word);
  });

  it('owns exactly eight limbs', () => {
    expect([...PREFLIGHT_LIMBS]).toEqual([
      'account-statement-unbacked',
      'population-empty',
      'population-unreconciled',
      'exact-requirement-unreachable',
      'unknown-invisible',
      'claim-strength-unexplained',
      'source-path-unresolved',
      'browser-check-not-current',
    ]);
  });

  it('presents the same claims the parity oracle counts: every presented claim on the page, every page tuple a presented claim', () => {
    const presented = presentedShapeClaims(ready.model.projectShape);
    const ids = new Set(presented.map((claim) => claim.claimId));
    expect(ids.size).toBe(presented.length);
    const onPage = Array.from(ready.polarisHtml.matchAll(/data-claim-id="([^"]*)"/g), (match) => match[1] as string);
    // The current-authority citation re-renders the baseline-spec item's
    // tuple, so tuples may outnumber distinct ids; the sets are equal.
    expect(onPage.length).toBeGreaterThanOrEqual(presented.length);
    expect(new Set(onPage)).toEqual(ids);
  });
});

describe('walkthrough preflight: one counterexample per limb', () => {
  // `also`: limbs the same mutation legitimately trips as well (a class
  // with nothing modeled no longer reconciles to its declared denominator;
  // a route that rendered nothing is also an unresolved source path).
  const cases: readonly { readonly name: string; readonly limb: PreflightLimb; readonly also?: readonly PreflightLimb[]; readonly mutate: (base: WalkthroughPreflightInputs) => WalkthroughPreflightInputs }[] = [
    {
      name: 'an account statement with no source anchor',
      limb: 'account-statement-unbacked',
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => { (shape.projectAccount[0] as unknown as { anchors: unknown[] }).anchors = []; }) }),
    },
    {
      name: 'an account statement the model holds as Inferred',
      limb: 'account-statement-unbacked',
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => { (shape.projectAccount[0] as unknown as { claim: { epistemic: { label: string } } }).claim.epistemic.label = 'Inferred'; }) }),
    },
    {
      name: 'an account statement rendered nowhere on the page',
      limb: 'account-statement-unbacked',
      mutate: (b) => ({ ...b, polarisHtml: replaceOnce(b.polarisHtml, 'data-claim-id="claim:project-account:purpose"', 'data-claim-id="claim:project-account:purpose-gone"') }),
    },
    {
      name: 'an empty statement',
      limb: 'account-statement-unbacked',
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => { (shape.projectAccount[1] as { statement: string }).statement = '   '; }) }),
    },
    {
      name: 'a reconciled class with nothing modeled',
      limb: 'population-empty',
      also: ['population-unreconciled'],
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => { (shape.classes['topology-component'] as { modeled: number }).modeled = 0; }) }),
    },
    {
      name: 'a class whose counts do not add up to its denominator',
      limb: 'population-unreconciled',
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => { (shape.classes.principle.denominator as { value: number }).value = 3; }) }),
    },
    {
      name: 'a class whose denominator is Unknown',
      limb: 'population-unreconciled',
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => { (shape.classes['catalog-entry'] as { denominator: unknown }).denominator = { kind: 'unknown', reasons: ['excluded-content'] }; }) }),
    },
    {
      name: 'an item row missing from the page',
      limb: 'population-unreconciled',
      mutate: (b) => {
        const item = observedOf(b.model).items.find((candidate) => candidate.class === 'success-criterion');
        if (item === undefined) throw new Error('no success criterion');
        return { ...b, polarisHtml: replaceOnce(b.polarisHtml, `data-polaris-item="${item.claim.claimId}"`, 'data-polaris-item="gone"') };
      },
    },
    {
      name: 'the current authority is not a baseline spec',
      limb: 'exact-requirement-unreachable',
      mutate: (b) => {
        const copy = clone(b.model);
        (copy.proposedWork as { currentAuthority: unknown }).currentAuthority = { kind: 'unknown', reason: 'missing-declaration', route: 'declare it', detail: 'no spec' };
        return { ...b, model: copy };
      },
    },
    {
      name: 'the page renders the requirement as not-rendered',
      limb: 'exact-requirement-unreachable',
      mutate: (b) => ({ ...b, polarisHtml: b.polarisHtml.split('data-verbatim="rendered"').join('data-verbatim="not-rendered"') }),
    },
    {
      name: 'the exact-source route for the current requirement rendered nothing',
      limb: 'exact-requirement-unreachable',
      also: ['source-path-unresolved'],
      mutate: (b) => ({ ...b, sourceRoutes: new Map([...b.sourceRoutes, [currentIdentity, { state: 'rendered', requirements: 0 } as const]]) }),
    },
    {
      name: 'the exact-source route for the current requirement was never checked',
      limb: 'exact-requirement-unreachable',
      also: ['source-path-unresolved'],
      mutate: (b) => ({ ...b, sourceRoutes: new Map([...b.sourceRoutes].filter(([identity]) => identity !== currentIdentity)) }),
    },
    {
      name: 'the exact-source route answered not-rendered for the current requirement',
      limb: 'exact-requirement-unreachable',
      mutate: (b) => ({ ...b, sourceRoutes: new Map([...b.sourceRoutes, [currentIdentity, { state: 'not-rendered', reason: 'excluded-content' } as const]]) }),
    },
    {
      name: 'no Unknown anywhere (an evaluation with nothing excluded)',
      limb: 'unknown-invisible',
      mutate: () => inputsFor(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC),
    },
    {
      name: 'an Unknown the page shows as Observed',
      limb: 'unknown-invisible',
      mutate: (b) => ({ ...b, polarisHtml: replaceOnce(b.polarisHtml, 'data-epistemic-label="Unknown"', 'data-epistemic-label="Observed"') }),
    },
    {
      name: 'an Unknown with no resolution route',
      limb: 'unknown-invisible',
      mutate: (b) => ({ ...b, model: withShape(b.model, (shape) => {
        const unknown = shape.sources.find((source) => source.claim.epistemic.label === 'Unknown');
        if (unknown === undefined) throw new Error('no Unknown source');
        (unknown.claim as unknown as { resolutionRoutes: unknown[] }).resolutionRoutes = [];
      }) }),
    },
    {
      name: 'a claim tuple not described by the glossary',
      limb: 'claim-strength-unexplained',
      mutate: (b) => ({ ...b, polarisHtml: replaceOnce(b.polarisHtml, ' aria-describedby="polaris-claim-states-lede"', '') }),
    },
    {
      name: 'the glossary lacks the strengthening sentence',
      limb: 'claim-strength-unexplained',
      mutate: (b) => ({ ...b, polarisHtml: replaceOnce(b.polarisHtml, 'To strengthen a claim:', 'To weaken a claim:') }),
    },
    {
      name: 'the glossary does not explain a tier the page uses',
      limb: 'claim-strength-unexplained',
      mutate: (b) => ({ ...b, polarisHtml: replaceOnce(b.polarisHtml, 'report-fact —', 'report-fact:') }),
    },
    {
      name: 'a linked exact-source route that was unreachable',
      limb: 'source-path-unresolved',
      mutate: (b) => ({ ...b, sourceRoutes: new Map([...b.sourceRoutes].map(([identity, outcome]) => [identity, identity === currentIdentity ? outcome : { state: 'unreachable', detail: 'HTTP 500' } as const])) }),
    },
    {
      name: 'a linked exact-source route that was never checked',
      limb: 'source-path-unresolved',
      mutate: (b) => ({ ...b, sourceRoutes: new Map([...b.sourceRoutes].filter(([identity]) => identity === currentIdentity)) }),
    },
    {
      name: 'a dangling internal link',
      limb: 'source-path-unresolved',
      mutate: (b) => ({ ...b, polarisHtml: `${b.polarisHtml}<a href="#polaris-nowhere">nowhere</a>` }),
    },
    {
      name: 'no browser check performed',
      limb: 'browser-check-not-current',
      mutate: (b) => ({ ...b, browserCheck: { kind: 'not-performed', detail: 'no browser' } }),
    },
    {
      name: 'a browser check of another commit',
      limb: 'browser-check-not-current',
      mutate: (b) => ({ ...b, browserCheck: { kind: 'performed', commit: 'f'.repeat(40), variants: 3, violations: 0 } }),
    },
    {
      name: 'a browser check with a violation',
      limb: 'browser-check-not-current',
      mutate: (b) => ({ ...b, browserCheck: { kind: 'performed', commit: b.model.observerRevision, variants: 3, violations: 1 } }),
    },
    {
      name: 'a browser check that exercised no variant',
      limb: 'browser-check-not-current',
      mutate: (b) => ({ ...b, browserCheck: { kind: 'performed', commit: b.model.observerRevision, variants: 0, violations: 0 } }),
    },
  ];

  for (const example of cases) {
    it(`${example.name} → ${example.limb}${example.also === undefined ? ', and nothing else' : ` (and ${example.also.join(', ')})`}`, () => {
      const result = evaluateWalkthroughPreflight(example.mutate(ready));
      expect(result.ready).toBe(false);
      const limbs = result.findings.map((finding) => finding.limb);
      expect(limbs[0]).toBe(example.limb);
      expect([...limbs].sort()).toEqual([example.limb, ...(example.also ?? [])].sort());
      for (const finding of result.findings) expect(finding.detail).not.toBe('');
    });
  }

  it('covers every limb with at least one counterexample', () => {
    const covered = new Set(cases.map((example) => example.limb));
    expect([...PREFLIGHT_LIMBS].filter((limb) => !covered.has(limb))).toEqual([]);
  });

  it('an unobserved shape fails every shape-bound limb at once and hides nothing', () => {
    const copy = clone(ready.model);
    (copy as { projectShape: unknown }).projectShape = { kind: 'not-evaluated', authority: undefined, detail: 'no authority', claim: observedOf(ready.model).claim };
    const result = evaluateWalkthroughPreflight({ ...ready, model: copy });
    expect(result.ready).toBe(false);
    const limbs = result.findings.map((finding) => finding.limb);
    for (const limb of ['account-statement-unbacked', 'population-empty', 'population-unreconciled', 'exact-requirement-unreachable']) expect(limbs).toContain(limb);
  });
});
