// PWB 2.7: the composed project-shape pipeline behind `PocModel.projectShape`.
//
// Oracle independence: the Git runner is a fixture answering exactly the
// commands the pipeline may issue; the expected population, items, claims and
// vocabularies are hand-typed here (the closed label/tier/reason/freshness
// lists are literal copies, compared against cap1-core, never imported from
// the module under test). No Butlers repository is touched; the gate test
// proves a non-admitting authority issues zero Git commands.

import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';

import { FRESHNESS_STATES, RENDERING_TIERS, UNKNOWN_REASONS } from '@syzygy/cap1-core';

import type { BodyReadAuthorityEvaluation } from './body-read-authority.js';
import type { GitTreeEntry } from './git-tree.js';
import type { Declaration, PrecedenceRule } from './project-shape-coverage.js';
import {
  CHALLENGE_STATES,
  PWB_REPOSITORY_ID,
  UNKNOWN_REASON_ROUTES,
  buildProjectShape,
  countReasons,
  itemClaim,
  ownerActProvenance,
  unevaluatedProjectShape,
  type ProjectShape,
  type ProjectShapeClaim,
} from './project-shape-model.js';

// ---------------------------------------------------------------------
// Hard-coded vocabularies (RFC2-24 / RFC2-25 / RFC2-10 / three labels).

const LABELS = ['Observed', 'Inferred', 'Unknown'] as const;
const TIERS = ['gate-backed', 'report-fact', 'asserted-by-worker', 'reduced-fidelity', 'declared-only', 'suspended'] as const;
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
const FRESHNESS = ['fresh', 'stale', 'broken', 'superseded'] as const;

// ---------------------------------------------------------------------
// Fixture repository: Butlers-shaped, not Butlers.

const COMMIT = '4'.repeat(40);
const COMMITTED_AT = '2026-08-15T10:00:00+00:00';
const CAPTURED_AT = '2026-09-04T09:00:00.000Z';
const SENTINEL = 'EXCLUDED-BODY-SENTINEL-7f3a';

const VISION = [
  '# Fixture',
  '',
  '## What Butlers Is',
  '',
  'A household of agents that keep promises.',
  '',
  '## What Success Looks Like',
  '',
  '- Every promise is visible.',
  '- Nothing is inferred silently.',
  '',
  '## What Butlers Is Not',
  '',
  'Not a chat toy.',
  '',
  '## Non-Negotiable Rules',
  '',
  '1. **Fail closed** — silence is Unknown.',
  '2. **Cite or stay quiet** — every claim carries a source.',
  '',
].join('\n');

const ARCHITECTURE = ['# Architecture', '', '## Runtime', '', 'One process.', ''].join('\n');

const V1 = [
  '# v1',
  '',
  '## What v1 Ships',
  '',
  'Ships text.',
  '',
  '### Core Infrastructure',
  '',
  '- **Bus** - the message bus',
  '',
  '### Staffers',
  '',
  '### Butlers',
  '',
  '- **Atlas** - maps',
  '- **Bishop** - moves',
  '',
  '### Modules',
  '',
  '### Connectors',
  '',
  '### Dashboard',
  '',
  '### Identity System',
  '',
  '### Situational Awareness',
  '',
  '### Observability',
  '',
  '## What v1 Defers',
  '',
  'Defers text.',
  '',
  '## Success Criteria',
  '',
  '1. Ships on time.',
  '',
].join('\n');

const LORE_README = ['# Lore', '', '## Index', '', '| Contract | Status |', '| --- | --- |', '| [RFC 0001](0001.md) | accepted |', ''].join('\n');
const COMPONENTS = ['# Components', '', '## 1 Runtime', '', '| Component | Role |', '|---|---|', '| **Daemon** | serves |', ''].join('\n');
const CRAFT_README = ['# Craft', '', '### Reading Order', '', '| Order | File |', '|---|---|', '| 1 | [Spec policy](policies/cc-spec.md) |', ''].join('\n');
const CRAFT_SECRET = ['# Craft', '', '### Reading Order', '', '| Order | File |', '|---|---|', '| 1 | [Spec policy](policies/cc-spec.md) |', '', `token AKIA${'A'.repeat(16)} ${SENTINEL}`, ''].join('\n');

const BASE_TEXTS: Readonly<Record<string, string>> = {
  'about/README.md': [
    '# Fixture',
    '',
    '[Heart and Soul](heart-and-soul/) · [Legends and Lore](legends-and-lore/) ·',
    '[Spec and Spine](spec-and-spine/) · [Lay and Land](lay-and-land/) · [Craft and Care](craft-and-care/)',
    '',
  ].join('\n'),
  'about/heart-and-soul/README.md': '- [Vision](vision.md)\n- [Architecture](architecture.md)\n- [v1](v1.md)\n',
  'about/heart-and-soul/vision.md': VISION,
  'about/heart-and-soul/architecture.md': ARCHITECTURE,
  'about/heart-and-soul/v1.md': V1,
  'about/legends-and-lore/README.md': LORE_README,
  'about/legends-and-lore/0001.md': '# RFC 0001\n',
  'about/spec-and-spine/README.md': 'Specs.\n',
  'about/lay-and-land/README.md': '[Components](components.md)\n',
  'about/lay-and-land/components.md': COMPONENTS,
  'about/craft-and-care/README.md': CRAFT_README,
  'about/craft-and-care/policies/cc-spec.md': '# Spec policy\n',
  'openspec/specs/alpha/spec.md': '# Alpha\n',
  'roster/atlas/butler.toml': '[butler]\nname = "atlas"\n',
  'roster/bishop/butler.toml': '[butler]\nname = "bishop"\n',
};

const encoder = new TextEncoder();

function sha1Blob(bytes: Uint8Array): string {
  return createHash('sha1').update(`blob ${bytes.byteLength}\0`).update(bytes).digest('hex');
}

function sha256(text: string): string {
  return `sha256:${createHash('sha256').update(text).digest('hex')}`;
}

interface Fixture {
  readonly texts: Readonly<Record<string, string>>;
  readonly failRevParse?: boolean;
  readonly failPhaseBLsTree?: boolean;
  readonly dropFromTree?: readonly string[];
}

function fixture(input: Fixture) {
  const bytes = new Map(Object.entries(input.texts).map(([path, text]) => [path, encoder.encode(text)]));
  const entries: GitTreeEntry[] = [...bytes.entries()]
    .filter(([path]) => !(input.dropFromTree ?? []).includes(path))
    .map(([path, body]) => ({ mode: '100644', type: 'blob', objectId: sha1Blob(body), sizeBytes: body.byteLength, path }));
  const byOid = new Map(entries.map((entry) => [entry.objectId, bytes.get(entry.path) as Uint8Array]));
  const listing = entries.map((e) => `${e.mode} ${e.type} ${e.objectId} ${String(e.sizeBytes).padStart(7)}\t${e.path}\x00`).join('');
  const calls: string[][] = [];
  let lsTreeCalls = 0;
  const runGit = (args: readonly string[]): Uint8Array => {
    calls.push([...args]);
    switch (args[0]) {
      case 'rev-parse':
        if (input.failRevParse === true) throw new Error('fatal: Needed a single revision');
        return encoder.encode(`${COMMIT}\n`);
      case 'show':
        return encoder.encode(`${COMMITTED_AT}\n`);
      case 'ls-tree':
        lsTreeCalls += 1;
        if (args[4] !== COMMIT) throw new Error(`fixture lists trees only at the resolved commit, not ${args[4] ?? ''}`);
        if (input.failPhaseBLsTree === true && lsTreeCalls === 2) throw new Error('fatal: not a tree object');
        return encoder.encode(listing);
      case 'cat-file': {
        const body = byOid.get(args[2] ?? '');
        if (body === undefined) throw new Error(`fixture has no object ${args[2] ?? ''}`);
        return body;
      }
      default:
        throw new Error(`unexpected git command ${args.join(' ')}`);
    }
  };
  return { runGit, calls, entries };
}

const ADMITTING: BodyReadAuthorityEvaluation = {
  evaluationId: 'evaluation:test-admitting',
  evaluationInstant: '2026-09-04T00:00:00Z',
  admits: true,
  authorizationMode: 'owner-trusted-bootstrap',
  consent: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:consent', artifactDigest: 'sha256:c'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  policy: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:policy', artifactDigest: 'sha256:p'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  registry: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:registry', artifactDigest: 'sha256:r'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  contradiction: undefined,
};

const REJECTING: BodyReadAuthorityEvaluation = {
  evaluationId: 'evaluation:test-rejecting',
  evaluationInstant: '2026-09-04T00:00:00Z',
  admits: false,
  authorizationMode: 'rejected',
  consent: { kind: 'absent', what: 'artifact-missing', artifactDigest: undefined },
  policy: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:policy', artifactDigest: 'sha256:p'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  registry: { kind: 'invalid', caseId: 'registry:phrase-mismatched', detail: 'wrong phrase', artifactDigest: 'sha256:r'.padEnd(71, '0'), claimedProvenance: 'state-1' },
  contradiction: { clause: 'RFC3-16(a)', definedTerm: 'authorization-bearing governance artifact', statement: 'No effective act.', failing: [] },
};

function build(input: Fixture & { authority?: BodyReadAuthorityEvaluation; rules?: readonly PrecedenceRule[]; stated?: readonly Declaration[]; revision?: string }) {
  const git = fixture(input);
  const shape = buildProjectShape({
    authority: input.authority ?? ADMITTING,
    revision: input.revision ?? 'main',
    capturedAt: CAPTURED_AT,
    runGit: git.runGit,
    ...(input.rules === undefined ? {} : { rules: input.rules }),
    ...(input.stated === undefined ? {} : { statedDeclarations: input.stated }),
  });
  return { shape, calls: git.calls, entries: git.entries };
}

function observed(input: Parameters<typeof build>[0]): Extract<ProjectShape, { kind: 'observed' }> {
  const { shape } = build(input);
  if (shape.kind !== 'observed') throw new Error(`expected observed, got ${shape.kind}`);
  return shape;
}

// Hand-typed: the complete population at the fixture revision, sorted.
const POPULATION = [
  'about/README.md',
  'about/craft-and-care/README.md',
  'about/craft-and-care/policies/cc-spec.md',
  'about/heart-and-soul/README.md',
  'about/heart-and-soul/architecture.md',
  'about/heart-and-soul/v1.md',
  'about/heart-and-soul/vision.md',
  'about/lay-and-land/README.md',
  'about/lay-and-land/components.md',
  'about/legends-and-lore/0001.md',
  'about/legends-and-lore/README.md',
  'about/spec-and-spine/README.md',
  'openspec/specs/alpha/spec.md',
  'roster/atlas/butler.toml',
  'roster/bishop/butler.toml',
] as const;

// Hand-typed: every declared identity, in source-path order then document
// order, keyed by the P2.5 grammar (positional keys for criteria and
// components, basenames for policies and specs).
const IDENTITIES = [
  ['craft-policy', 'cc-spec.md'],
  ['project-account-section', 'architecture'],
  ['project-account-section', 'v1-scope'],
  ['project-account-section', 'v1-success'],
  ['success-criterion', 'v1:1'],
  ['catalog-entry', 'Bus'],
  ['catalog-entry', 'Atlas'],
  ['catalog-entry', 'Bishop'],
  ['project-account-section', 'purpose'],
  ['project-account-section', 'promises'],
  ['project-account-section', 'refusals'],
  ['principle', 'Fail closed'],
  ['principle', 'Cite or stay quiet'],
  ['success-criterion', 'vision:1'],
  ['success-criterion', 'vision:2'],
  ['topology-component', '1:Daemon'],
  ['design-contract', 'RFC 0001'],
  ['baseline-spec', 'alpha'],
  ['roster-identity', 'atlas'],
  ['roster-identity', 'bishop'],
] as const;

function isValidClaim(claim: ProjectShapeClaim): void {
  expect(LABELS).toContain(claim.epistemic.label);
  if (claim.epistemic.tier !== undefined) expect(TIERS).toContain(claim.epistemic.tier);
  expect(FRESHNESS).toContain(claim.epistemic.freshness);
  expect(claim.challenge).toBe('unchallenged');
  expect(claim.claimId).toMatch(/^claim:/);
  expect(claim.evaluationId).not.toBe('');
  if (claim.epistemic.label === 'Unknown') {
    expect('reasons' in claim.epistemic).toBe(true);
    if ('reasons' in claim.epistemic) {
      expect(REASONS).toContain(claim.epistemic.reasons.primary);
      for (const reason of claim.epistemic.reasons.secondary) expect(REASONS).toContain(reason);
      expect(claim.resolutionRoutes.map((route) => route.reason)).toEqual([claim.epistemic.reasons.primary, ...claim.epistemic.reasons.secondary]);
      for (const route of claim.resolutionRoutes) expect(route.route.length).toBeGreaterThan(0);
    }
  } else {
    expect(claim.resolutionRoutes).toEqual([]);
  }
}

function allClaims(shape: Extract<ProjectShape, { kind: 'observed' }>): readonly ProjectShapeClaim[] {
  return [
    shape.claim,
    ...shape.sources.map((s) => s.claim),
    ...shape.items.map((i) => i.claim),
    ...Object.values(shape.classes).map((c) => c.claim),
    ...shape.facts.map((f) => f.claim),
    ...shape.projectAccount.map((p) => p.claim),
  ];
}

// ---------------------------------------------------------------------

describe('vocabularies are cap1-core verbatim', () => {
  it('routes cover exactly the twelve RFC2-24 reasons, and the hard-coded lists match cap1-core', () => {
    expect(Object.keys(UNKNOWN_REASON_ROUTES).sort()).toEqual([...REASONS].sort());
    expect([...UNKNOWN_REASONS]).toEqual([...REASONS]);
    expect([...RENDERING_TIERS]).toEqual([...TIERS]);
    expect([...FRESHNESS_STATES]).toEqual([...FRESHNESS]);
    expect([...CHALLENGE_STATES]).toEqual(['unchallenged']);
    expect(PWB_REPOSITORY_ID).toBe('repository:butlers-configured-poc');
  });
});

describe('the gate comes first', () => {
  it('a non-admitting authority issues zero Git commands and renders every admission reason', () => {
    const { shape, calls } = build({ texts: BASE_TEXTS, authority: REJECTING });
    expect(calls).toEqual([]);
    expect(shape.kind).toBe('not-admitted');
    if (shape.kind !== 'not-admitted') return;
    expect(shape.reason).toBe('unconsented-source-or-provider');
    expect(shape.secondaryReasons).toEqual(['source-uncaptured-or-unreachable']);
    expect(shape.authority.admits).toBe(false);
    expect(shape.authority.authorities.map((a) => [a.authority, a.state])).toEqual([
      ['consent', 'absent'],
      ['policy', 'owner-adopted (bootstrap, uncorrelated)'],
      ['registry', 'invalid act'],
    ]);
    expect(shape.authority.authorities.every((a) => a.independentlyVerified === false)).toBe(true);
    expect(shape.contradiction.clause).toBe('RFC3-16(a)');
    isValidClaim(shape.claim);
    expect(shape.claim.epistemic).toEqual({
      label: 'Unknown',
      reasons: { primary: 'unconsented-source-or-provider', secondary: ['source-uncaptured-or-unreachable'] },
      freshness: 'fresh',
    });
    expect(shape.claim.evaluationId).toBe('evaluation:test-rejecting');
  });

  it('no evaluation at all is Unknown as unconsented, with the supplied detail', () => {
    const shape = unevaluatedProjectShape('daemon could not load the governance tree');
    expect(shape.kind).toBe('not-evaluated');
    expect(shape.authority).toBeUndefined();
    if (shape.kind !== 'not-evaluated') return;
    expect(shape.detail).toBe('daemon could not load the governance tree');
    isValidClaim(shape.claim);
    expect(shape.claim.epistemic.label).toBe('Unknown');
    expect(shape.claim.resolutionRoutes).toEqual([{ reason: 'unconsented-source-or-provider', route: 'Record consent' }]);
  });
});

describe('observation failures stay Unknown with the registry reason', () => {
  it('rev-parse failure is gitCaptureFailed', () => {
    const { shape } = build({ texts: BASE_TEXTS, failRevParse: true });
    expect(shape.kind).toBe('observation-failed');
    if (shape.kind !== 'observation-failed') return;
    expect(shape.failure.failureState).toBe('gitCaptureFailed');
    expect(shape.failure.reason).toBe('source-uncaptured-or-unreachable');
    expect(shape.failure.detail).toContain('rev-parse');
    expect(shape.authority.admits).toBe(true);
    isValidClaim(shape.claim);
  });

  it('phase B tree listing failure is gitCaptureFailed too', () => {
    const { shape } = build({ texts: BASE_TEXTS, failPhaseBLsTree: true });
    expect(shape.kind).toBe('observation-failed');
    if (shape.kind !== 'observation-failed') return;
    expect(shape.failure.failureState).toBe('gitCaptureFailed');
    expect(shape.failure.detail).toContain('ls-tree');
  });

  it('an option-shaped revision is refused before any Git command', () => {
    const { shape, calls } = build({ texts: BASE_TEXTS, revision: '--output=x' });
    expect(calls).toEqual([]);
    expect(shape.kind).toBe('observation-failed');
    if (shape.kind !== 'observation-failed') return;
    expect(shape.failure.failureState).toBeUndefined();
    expect(shape.failure.reason).toBe('source-uncaptured-or-unreachable');
  });
});

describe('an admitted, fully readable fixture', () => {
  const shape = observed({ texts: BASE_TEXTS });

  it('binds identity: revision, both instants, scope, observer, policy, manifest and observation digests', () => {
    expect(shape.identity.repositoryId).toBe('repository:butlers-configured-poc');
    expect(shape.identity.requestedRevision).toBe('main');
    expect(shape.identity.revision).toBe(COMMIT);
    expect(shape.identity.capturedAt).toBe(CAPTURED_AT);
    expect(shape.identity.sourceClaimedInstant).toEqual({ kind: 'git-committer-instant', instant: COMMITTED_AT });
    expect(shape.identity.sourceClaimedInstant.instant).not.toBe(shape.identity.capturedAt);
    expect(shape.identity.scope).toEqual({ repositoryId: 'repository:butlers-configured-poc', contentClass: 'declared-project-shape-text', phase: 'A' });
    expect(shape.identity.observer.observerId).toBe('polaris-butlers-project-shape');
    expect(shape.identity.policy).toEqual({ policyId: 'polaris-butlers-project-shape-secrets', policyVersion: '1.1.0-candidate.1' });
    expect(shape.identity.manifestDigest).toMatch(/^sha256:[0-9a-f]{64}$/);
    expect(shape.identity.observationDigest).toMatch(/^sha256:[0-9a-f]{64}$/);
    expect(shape.identity.deterministicInputs.authority).toEqual({
      kind: 'evaluated',
      evaluationId: 'evaluation:test-admitting',
      consent: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:consent', artifactDigest: 'sha256:c'.padEnd(71, '0') },
      policy: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:policy', artifactDigest: 'sha256:p'.padEnd(71, '0') },
      registry: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:registry', artifactDigest: 'sha256:r'.padEnd(71, '0') },
    });
    expect(shape.authority.admits).toBe(true);
    expect(shape.authority.authorities.map((a) => a.state)).toEqual(Array(3).fill('owner-adopted (bootstrap, uncorrelated)'));
    expect(shape.authority.authorities.map((a) => a.disclosure)).toEqual(
      Array(3).fill("Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance."),
    );
  });

  it('carries the complete source population with stamps, identities and Observed claims', () => {
    expect(shape.sources.map((s) => s.path).sort()).toEqual([...POPULATION]);
    expect(shape.counts.sources).toBe(15);
    expect(shape.counts.sourcesWithKnownItemDenominator).toBe(15);
    expect(shape.counts.sourcesWithUnknownDenominator).toBe(0);
    for (const source of shape.sources) {
      expect(source.identity).toBe(`repository:butlers-configured-poc@${COMMIT}:${source.path}#${source.anchor.kind === 'blob' ? source.anchor.objectId : '?'}`);
      expect(source.stamp).toEqual({
        sourceIdentity: source.identity,
        scope: shape.identity.scope,
        capturedAt: CAPTURED_AT,
        observerId: 'polaris-butlers-project-shape',
        observerVersion: '1.1.0-candidate.1',
      });
      expect(source.itemDenominator.kind).toBe('known');
      expect(source.claim.epistemic).toEqual({ label: 'Observed', tier: 'report-fact', freshness: 'fresh' });
      expect(source.claim.support).toEqual([{
        path: source.path,
        sourceIdentity: source.identity,
        ...(source.rule === 'baseline-spec-tree' ? {} : { contentDigest: sha256(BASE_TEXTS[source.path] as string) }),
      }]);
    }
    const vision = shape.sources.find((s) => s.path === 'about/heart-and-soul/vision.md');
    expect(vision?.itemDenominator).toEqual({ kind: 'known', value: 7 });
    expect(vision?.rule).toBe('pillar-named-file');
    expect(vision?.pillar).toBe('heart-and-soul');
    expect(vision?.declaredBy).toBe('about/heart-and-soul/README.md');
  });

  it('accounts for every declared identity, all modeled', () => {
    expect(shape.items.map((i) => [i.class, i.key])).toEqual(IDENTITIES.map((pair) => [...pair]));
    expect(shape.counts.items).toBe(20);
    expect(shape.counts.modeled).toBe(20);
    expect(shape.counts.unknown).toBe(0);
    expect(shape.counts.contradicted).toBe(0);
    expect(shape.contradictions).toEqual([]);
    expect(shape.exclusions).toEqual([]);
    expect(shape.degradation).toBeUndefined();
    expect(shape.limitBreaches).toEqual([]);
    for (const item of shape.items) {
      expect(item.state).toBe('modeled');
      expect(item.claim.claimId).toBe(`claim:item:${item.class}:${item.key}`);
      expect(item.claim.epistemic).toEqual({ label: 'Observed', tier: 'report-fact', freshness: 'fresh' });
      expect(item.claim.support.length).toBeGreaterThan(0);
      for (const support of item.claim.support) expect(support.sourceIdentity).toMatch(/^repository:butlers-configured-poc@/);
    }
    const principle = shape.items.find((i) => i.class === 'principle' && i.key === 'Fail closed');
    expect(principle?.statement).toBe('**Fail closed** — silence is Unknown.');
    expect(principle?.claim.support).toEqual([
      { path: 'about/heart-and-soul/vision.md', line: 18, contentDigest: sha256(VISION), sourceIdentity: `repository:butlers-configured-poc@${COMMIT}:about/heart-and-soul/vision.md#${sha1Blob(encoder.encode(VISION))}` },
    ]);
  });

  it('renders the six project-account statements with their sections and claims', () => {
    expect(shape.projectAccount.map((p) => p.key)).toEqual(['purpose', 'promises', 'refusals', 'architecture', 'v1-scope', 'v1-success']);
    const byKey = new Map(shape.projectAccount.map((p) => [p.key, p]));
    expect(byKey.get('purpose')?.statement).toBe('A household of agents that keep promises.');
    expect(byKey.get('refusals')?.statement).toBe('Not a chat toy.');
    expect(byKey.get('architecture')?.statement).toBe('Runtime\n\nOne process.');
    expect(byKey.get('architecture')?.anchors).toEqual([{ path: 'about/heart-and-soul/architecture.md', line: 3, contentDigest: sha256(ARCHITECTURE) }]);
    for (const statement of shape.projectAccount) {
      expect(statement.claim.claimId).toBe(`claim:project-account:${statement.key}`);
      expect(statement.claim.epistemic.label).toBe('Observed');
    }
  });

  it('aggregates per class with known denominators, Observed claims and zero reason counts', () => {
    const table = Object.values(shape.classes).map((c) => [c.class, c.denominator, c.declared, c.claim.epistemic.label]);
    expect(table).toEqual([
      ['project-account-section', { kind: 'known', value: 6 }, 6, 'Observed'],
      ['principle', { kind: 'known', value: 2 }, 2, 'Observed'],
      ['success-criterion', { kind: 'known', value: 3 }, 3, 'Observed'],
      ['catalog-entry', { kind: 'known', value: 3 }, 3, 'Observed'],
      ['design-contract', { kind: 'known', value: 1 }, 1, 'Observed'],
      ['baseline-spec', { kind: 'known', value: 1 }, 1, 'Observed'],
      ['topology-component', { kind: 'known', value: 1 }, 1, 'Observed'],
      ['craft-policy', { kind: 'known', value: 1 }, 1, 'Observed'],
      ['roster-identity', { kind: 'known', value: 2 }, 2, 'Observed'],
    ]);
    for (const aggregate of Object.values(shape.classes)) {
      expect(aggregate.reasonCounts).toEqual({ primary: {}, secondary: {} });
      expect(aggregate.claim.claimId).toBe(`claim:class:${aggregate.class}`);
    }
    expect(shape.counts.facts).toBe(20 + 9);
    expect(shape.claim.epistemic).toEqual({ label: 'Observed', tier: 'report-fact', freshness: 'fresh' });
  });

  it('every claim is a complete tuple from the closed vocabularies', () => {
    const claims = allClaims(shape);
    expect(claims.length).toBe(1 + 15 + 20 + 9 + 29 + 6);
    for (const entry of claims) isValidClaim(entry);
    expect(new Set(claims.map((c) => c.evaluationId))).toEqual(new Set(['evaluation:test-admitting']));
  });

  it('is JSON-stable and deterministic across two runs', () => {
    const again = observed({ texts: BASE_TEXTS });
    expect(again).toEqual(shape);
    expect(JSON.parse(JSON.stringify(shape))).toEqual(JSON.parse(JSON.stringify(again)));
    expect(again.identity.observationDigest).toBe(shape.identity.observationDigest);
  });

  it('exposes owner-act provenance per authority in triple order', () => {
    expect(ownerActProvenance(shape.authority)).toEqual([
      { kind: 'owner-act', source: 'act:consent', revision: 'owner-adopted (bootstrap, uncorrelated)', digest: 'sha256:c'.padEnd(71, '0') },
      { kind: 'owner-act', source: 'act:policy', revision: 'owner-adopted (bootstrap, uncorrelated)', digest: 'sha256:p'.padEnd(71, '0') },
      { kind: 'owner-act', source: 'act:registry', revision: 'owner-adopted (bootstrap, uncorrelated)', digest: 'sha256:r'.padEnd(71, '0') },
    ]);
  });
});

describe('faults never shrink the population (PWB-REQ-003)', () => {
  it('a secret-bearing index is excluded hash-not-body before child derivation; its class denominator and the project shape go Unknown', () => {
    const texts = { ...BASE_TEXTS, 'about/craft-and-care/README.md': CRAFT_SECRET };
    const shape = observed({ texts });
    expect(shape.sources.map((s) => s.path).sort()).toEqual(POPULATION.filter((path) => path !== 'about/craft-and-care/policies/cc-spec.md'));
    const craft = shape.sources.find((s) => s.path === 'about/craft-and-care/README.md');
    expect(craft?.itemDenominator.kind).toBe('unknown');
    expect(craft?.record.outcome).toBe('excluded');
    expect(craft?.claim.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'excluded-content', secondary: [] }, freshness: 'fresh' });
    expect(craft?.claim.support).toEqual([
      { path: 'about/craft-and-care/README.md', sourceIdentity: `repository:butlers-configured-poc@${COMMIT}:about/craft-and-care/README.md#${sha1Blob(encoder.encode(CRAFT_SECRET))}`, contentDigest: sha256(CRAFT_SECRET) },
    ]);
    expect(shape.classes['craft-policy'].reasonCounts).toEqual({ primary: { 'excluded-content': 1 }, secondary: {} });
    expect(craft?.claim.resolutionRoutes).toEqual([{ reason: 'excluded-content', route: 'Policy change by the owner, or accept the exclusion' }]);
    expect(shape.exclusions).toEqual([
      {
        redactionClass: 'excluded-artifact',
        repositoryRelativePath: 'about/craft-and-care/README.md',
        policyId: 'polaris-butlers-project-shape-secrets',
        policyVersion: '1.1.0-candidate.1',
        contentDigest: sha256(CRAFT_SECRET),
        detectorId: 'known-token-formats',
      },
    ]);
    expect(shape.counts.exclusions).toBe(1);
    expect(shape.classes['craft-policy'].denominator).toEqual({ kind: 'unknown', reasons: ['excluded-content'] });
    expect(shape.classes['craft-policy'].claim.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'excluded-content', secondary: [] }, freshness: 'fresh' });
    expect(shape.items.some((i) => i.class === 'craft-policy')).toBe(false);
    expect(shape.counts.items).toBe(19);
    expect(shape.degradation).toMatchObject({ failureState: 'secretMatchedOrUnclassifiable', unknownReason: 'excluded-content' });
    expect(shape.claim.epistemic).toEqual({
      label: 'Unknown',
      reasons: { primary: 'excluded-content', secondary: [] },
      freshness: 'fresh',
    });
    expect(JSON.stringify(shape)).not.toContain(SENTINEL);
    expect(JSON.stringify(shape)).not.toContain('AKIA');
    for (const entry of allClaims(shape)) isValidClaim(entry);
  });

  it('an undiscovered Heart and Soul root poisons all dependent denominators and account statements without claiming absence', () => {
    const texts = { ...BASE_TEXTS, 'about/README.md': (BASE_TEXTS['about/README.md'] as string).replace('[Heart and Soul](heart-and-soul/) · ', '') };
    const shape = observed({ texts });
    for (const cls of ['project-account-section', 'principle', 'success-criterion', 'catalog-entry'] as const) {
      expect(shape.classes[cls].denominator).toEqual({ kind: 'unknown', reasons: ['source-uncaptured-or-unreachable'] });
      expect(shape.classes[cls].claim.epistemic.label).toBe('Unknown');
      expect(shape.classes[cls].declared).toBe(0);
    }
    expect(shape.projectAccount.every((entry) => entry.claim.epistemic.label === 'Unknown')).toBe(true);
    expect(shape.projectAccount.map((entry) => 'reasons' in entry.claim.epistemic ? entry.claim.epistemic.reasons.primary : '')).toEqual(Array(6).fill('source-uncaptured-or-unreachable'));
    expect(shape.claim.epistemic.label).toBe('Unknown');
  });

  it('a missing pillar index poisons its dependent class even when no class source entered the manifest', () => {
    const shape = observed({ texts: BASE_TEXTS, dropFromTree: ['about/legends-and-lore/README.md'] });
    expect(shape.classes['design-contract']).toMatchObject({ declared: 0, discoveryUnknown: 1, denominator: { kind: 'unknown', reasons: ['source-uncaptured-or-unreachable'] } });
    expect(shape.classes['design-contract'].claim.epistemic.label).toBe('Unknown');
  });

  it('derives baseline identities from exact tree paths without opening or admitting their bodies', () => {
    const sentinel = `token AKIA${'Z'.repeat(16)}`;
    const texts = { ...BASE_TEXTS, 'openspec/specs/alpha/spec.md': sentinel };
    const { shape, calls, entries } = build({ texts });
    expect(shape.kind).toBe('observed');
    if (shape.kind !== 'observed') return;
    const baselineOid = entries.find((entry) => entry.path === 'openspec/specs/alpha/spec.md')?.objectId;
    expect(calls).not.toContainEqual(['cat-file', 'blob', baselineOid]);
    expect(shape.items.find((item) => item.class === 'baseline-spec' && item.key === 'alpha')?.claim.epistemic.label).toBe('Observed');
    expect(shape.classes['baseline-spec'].denominator).toEqual({ kind: 'known', value: 1 });
    expect(shape.sources.find((source) => source.path === 'openspec/specs/alpha/spec.md')?.record).toMatchObject({ outcome: 'classified', basis: 'path-only', detectorsRun: 0 });
    expect(JSON.stringify(shape)).not.toContain(sentinel);
  });

  it('a named-but-absent source stays counted as Unknown and its account statement is Unknown with the same reason', () => {
    const shape = observed({ texts: BASE_TEXTS, dropFromTree: ['about/heart-and-soul/architecture.md'] });
    expect(shape.sources.map((s) => s.path).sort()).toEqual([...POPULATION]);
    const architecture = shape.sources.find((s) => s.path === 'about/heart-and-soul/architecture.md');
    expect(architecture?.anchor).toEqual({ kind: 'missing-at-revision' });
    expect(architecture?.record.outcome).toBe('unavailable');
    expect(architecture?.claim.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'source-uncaptured-or-unreachable', secondary: [] }, freshness: 'fresh' });
    expect(architecture?.claim.support).toEqual([{ path: 'about/heart-and-soul/architecture.md', sourceIdentity: `repository:butlers-configured-poc@${COMMIT}:about/heart-and-soul/architecture.md#missing` }]);
    const statement = shape.projectAccount.find((p) => p.key === 'architecture');
    expect(statement?.statement).toBeUndefined();
    expect(statement?.anchors).toEqual([]);
    expect(statement?.claim.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'source-uncaptured-or-unreachable', secondary: [] }, freshness: 'fresh' });
    expect(shape.classes['project-account-section'].denominator).toEqual({ kind: 'unknown', reasons: ['source-uncaptured-or-unreachable'] });
    expect(shape.classes['project-account-section'].declared).toBe(5);
    expect(shape.classes['project-account-section'].reasonCounts).toEqual({ primary: { 'source-uncaptured-or-unreachable': 1 }, secondary: {} });
    expect(shape.degradation?.failureState).toBe('someSourcesUncapturedOrOverLimit');
    expect(shape.claim.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'source-uncaptured-or-unreachable', secondary: [] }, freshness: 'fresh' });
    for (const entry of allClaims(shape)) isValidClaim(entry);
  });

  it('combined faults keep one primary reason and deduplicated secondaries on the whole-shape claim', () => {
    const texts = {
      ...BASE_TEXTS,
      'about/craft-and-care/README.md': CRAFT_SECRET,
      'openspec/specs/alpha/spec.md': `# Alpha\n\npassword = "hunter2-${SENTINEL}"\n`,
    };
    const shape = observed({ texts, dropFromTree: ['about/heart-and-soul/architecture.md', 'about/heart-and-soul/v1.md'] });
    expect(shape.sources.length).toBe(14);
    expect(shape.exclusions.map((e) => e.repositoryRelativePath)).toEqual(['about/craft-and-care/README.md']);
    expect(shape.sources.filter((s) => s.claim.epistemic.label === 'Unknown').map((s) => [s.path, (s.claim.epistemic as { reasons: { primary: string } }).reasons.primary])).toEqual([
      ['about/craft-and-care/README.md', 'excluded-content'],
      ['about/heart-and-soul/architecture.md', 'source-uncaptured-or-unreachable'],
      ['about/heart-and-soul/v1.md', 'source-uncaptured-or-unreachable'],
    ]);
    expect(shape.claim.epistemic).toEqual({
      label: 'Unknown',
      reasons: { primary: 'excluded-content', secondary: ['source-uncaptured-or-unreachable'] },
      freshness: 'fresh',
    });
    expect(shape.claim.resolutionRoutes).toEqual([
      { reason: 'excluded-content', route: 'Policy change by the owner, or accept the exclusion' },
      { reason: 'source-uncaptured-or-unreachable', route: 'Repair the observer or source; new snapshot' },
    ]);
    expect(JSON.stringify(shape)).not.toContain(SENTINEL);
    for (const entry of allClaims(shape)) isValidClaim(entry);
  });

  it('a grammar failure leaves the source counted with a parse-failure exclusion and an Unknown denominator', () => {
    const texts = { ...BASE_TEXTS, 'about/lay-and-land/components.md': '# Components\n\n## 1 Runtime\n\n| Component | Role |\n|---|---|\n| **Daemon** |\n' };
    const shape = observed({ texts });
    const components = shape.sources.find((s) => s.path === 'about/lay-and-land/components.md');
    expect(components?.record.outcome).toBe('excluded');
    expect(components?.itemDenominator.kind).toBe('unknown');
    if (components?.itemDenominator.kind === 'unknown') {
      expect(components.itemDenominator.grammarFailure).toEqual({ reason: 'malformed-row', class: 'topology-component', line: 7, detail: 'column count' });
    }
    expect(components?.claim.epistemic.label).toBe('Unknown');
    expect(shape.classes['topology-component'].denominator.kind).toBe('unknown');
    expect(shape.sources.length).toBe(15);
    expect(shape.exclusions.map((entry) => entry.repositoryRelativePath)).toContain('about/lay-and-land/components.md');
    expect(shape.counts.classification).toEqual({
      sources: 15,
      classified: 14,
      classifiedByBasis: { body: 13, 'path-only': 1 },
      excluded: 1,
      unavailable: 0,
      byRedactionClass: { 'excluded-artifact': 0, 'unclassifiable-excluded': 1 },
    });
    expect(shape.counts.classification.classified + shape.counts.classification.excluded + shape.counts.classification.unavailable).toBe(shape.counts.sources);
  });
});

// Item-level contradiction (`state: 'contradicted'` on an ItemCoverage) is
// unreachable through the P2.5 grammar: every identity has exactly one
// declaring source, and a duplicate key inside a source is a grammar failure.
// The model still renders that state as Unknown/suspended because the coverage
// type admits it; only the count-fact contradiction below is reachable.
describe('contradictions are disclosed, resolved only by a cited rule (PWB-REQ-004)', () => {
  const stated: Declaration = {
    fact: 'count:roster-identity',
    value: '3',
    basis: 'stated-summary',
    anchors: [{ path: 'about/README.md', line: 9 }],
  };
  const rule: PrecedenceRule = {
    id: 'rule:roster-wins',
    anchor: { path: 'about/heart-and-soul/v1.md', line: 3 },
    statement: 'The roster tree is authoritative over summaries.',
    higher: { basis: 'derived-count' },
    lower: { path: 'about/README.md' },
    facts: ['count:roster-identity'],
  };

  it('a stated summary disagreeing with the derived count is contradicted, both anchors kept, tier suspended', () => {
    const shape = observed({ texts: BASE_TEXTS, stated: [stated] });
    expect(shape.contradictions.map((c) => c.fact.fact)).toEqual(['count:roster-identity']);
    const [contradiction] = shape.contradictions;
    expect(contradiction?.fact.state).toBe('contradicted');
    expect(contradiction?.fact.declarations.map((d) => d.value).sort()).toEqual(['2', '3']);
    expect(contradiction?.claim.epistemic).toEqual({
      label: 'Unknown',
      reasons: { primary: 'contradicted-pending-adjudication', secondary: [] },
      tier: 'suspended',
      freshness: 'fresh',
    });
    expect(contradiction?.claim.resolutionRoutes).toEqual([{ reason: 'contradicted-pending-adjudication', route: 'Owner adjudication' }]);
    expect(contradiction?.claim.support.map((s) => s.path).sort()).toEqual(['about/README.md', 'roster/atlas/butler.toml', 'roster/bishop/butler.toml']);
    expect(shape.counts.contradictedFacts).toBe(1);
    expect(shape.counts.rulesDeclared).toBe(0);
    // Every source is Observed, yet the shape is not: the contradiction is
    // a member Unknown, so the whole-shape claim carries it.
    expect(shape.sources.every((s) => s.claim.epistemic.label === 'Observed')).toBe(true);
    expect(shape.claim.epistemic).toEqual({
      label: 'Unknown',
      reasons: { primary: 'contradicted-pending-adjudication', secondary: [] },
      freshness: 'fresh',
    });
  });

  it('with a cited Butlers rule the fact is modeled and the citation travels', () => {
    const shape = observed({ texts: BASE_TEXTS, stated: [stated], rules: [rule] });
    expect(shape.contradictions).toEqual([]);
    const fact = shape.facts.find((f) => f.fact.fact === 'count:roster-identity');
    expect(fact?.fact.state).toBe('modeled');
    if (fact?.fact.state === 'modeled') {
      expect(fact.fact.value).toBe('2');
      expect(fact.fact.disagreement?.precedence.ruleId).toBe('rule:roster-wins');
    }
    expect(fact?.claim.epistemic).toEqual({ label: 'Observed', tier: 'report-fact', freshness: 'fresh' });
    expect(shape.counts.rulesApplied).toBe(1);
  });
});

describe('claim helpers at the seam the coverage types define', () => {
  const identities = new Map([['a.md', 'repository:x@1:a.md#0']]);
  const anchors = [{ path: 'a.md', line: 4 }];

  it('renders the three item states: modeled Observed, contradicted suspended, unknown with its reason', () => {
    const modeled = itemClaim({ class: 'principle', key: 'k', state: 'modeled', anchors }, identities, 'evaluation:x');
    expect(modeled.epistemic).toEqual({ label: 'Observed', tier: 'report-fact', freshness: 'fresh' });
    expect(modeled.support).toEqual([{ path: 'a.md', line: 4, sourceIdentity: 'repository:x@1:a.md#0' }]);
    const contradicted = itemClaim({ class: 'principle', key: 'k', state: 'contradicted', anchors, unknownReason: 'contradicted-pending-adjudication' }, identities, 'evaluation:x');
    expect(contradicted.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'contradicted-pending-adjudication', secondary: [] }, tier: 'suspended', freshness: 'fresh' });
    const unknown = itemClaim({ class: 'principle', key: 'k', state: 'unknown', anchors, unknownReason: 'excluded-content' }, identities, 'evaluation:x');
    expect(unknown.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'excluded-content', secondary: [] }, freshness: 'fresh' });
    const bare = itemClaim({ class: 'principle', key: 'k', state: 'unknown', anchors }, identities, 'evaluation:x');
    expect(bare.epistemic).toEqual({ label: 'Unknown', reasons: { primary: 'source-uncaptured-or-unreachable', secondary: [] }, freshness: 'fresh' });
    expect(bare.claimId).toBe('claim:item:principle:k');
    for (const entry of [modeled, contradicted, unknown, bare]) isValidClaim(entry);
  });

  it('counts primary and secondary reasons separately and skips non-Unknown claims', () => {
    const base = { claimId: 'claim:x', evaluationId: 'evaluation:x', resolutionRoutes: [], challenge: 'unchallenged' as const, support: [] };
    const counts = countReasons([
      { ...base, epistemic: { label: 'Observed', tier: 'report-fact', freshness: 'fresh' } },
      { ...base, epistemic: { label: 'Unknown', reasons: { primary: 'excluded-content', secondary: ['missing-evidence', 'excluded-content'] }, freshness: 'fresh' } },
      { ...base, epistemic: { label: 'Unknown', reasons: { primary: 'missing-evidence', secondary: [] }, freshness: 'fresh' } },
    ]);
    expect(counts).toEqual({ primary: { 'excluded-content': 1, 'missing-evidence': 1 }, secondary: { 'missing-evidence': 1, 'excluded-content': 1 } });
  });
});
