import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel, ProjectShape, ProjectShapeClaim } from '@syzygy/three-surface-poc-core';

import { NarrativeRegistry, parseNarrativeScript } from './polaris-narrative.js';
import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET,
  REJECTING_AUTHORITY,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

// ---------------------------------------------------------------------------
// Hand-typed expectations (PWB-REQ-014). Nothing below imports a production
// vocabulary; the anchor rules are re-derived from the captured model JSON.
const ROLES = ['anchored-project-fact', 'non-normative-framing', 'epistemic-claim'] as const;
const TARGET_CLASSES = ['doctrine', 'contract', 'requirement', 'decision', 'evidence', 'work'] as const;
const MAX_ANCHORS = 6;
const PROVENANCE_CLASS: Record<string, string> = {
  'repository-file': 'evidence',
  'git-revision': 'evidence',
  'manual-mapping': 'evidence',
  'materialization-record': 'work',
  'test-artifact-record': 'evidence',
  'project-shape-source': 'evidence',
  'owner-act': 'decision',
};

type Variant = 'unevaluated' | 'rejected' | 'observed' | 'observed-with-secret' | 'observed-with-baseline';
const VARIANTS: readonly Variant[] = ['unevaluated', 'rejected', 'observed', 'observed-with-secret', 'observed-with-baseline'];

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
    case 'observed-with-baseline':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC) } });
  }
}

interface Unit { readonly tag: string; readonly attrs: string; readonly inner: string }

/** Every element carrying a copy role or a claim role, with its inner HTML. */
function narrativeUnits(html: string): Unit[] {
  const body = html.replace(/<style[\s\S]*?<\/style>/g, '').replace(/<script[\s\S]*?<\/script>/g, '');
  const tokens = [...body.matchAll(/<\/([A-Za-z][\w-]*)\s*>|<([A-Za-z][\w-]*)([^>]*)>/g)];
  const VOID = new Set(['br', 'hr', 'img', 'input', 'meta', 'link']);
  const units: Unit[] = [];
  const stack: { name: string; attrs: string; start: number; tracked: boolean }[] = [];
  for (const token of tokens) {
    if (token[1] !== undefined) {
      for (let depth = stack.length - 1; depth >= 0; depth -= 1) {
        const open = stack[depth] as { name: string; attrs: string; start: number; tracked: boolean };
        if (open.name === token[1]) {
          stack.splice(depth);
          if (open.tracked) units.push({ tag: open.name, attrs: open.attrs, inner: body.slice(open.start, token.index) });
          break;
        }
      }
      continue;
    }
    const name = token[2] as string;
    const attrs = token[3] as string;
    if (VOID.has(name)) continue;
    stack.push({ name, attrs, start: (token.index as number) + token[0].length, tracked: /data-copy-role=|data-claim-role=/.test(attrs) });
  }
  expect(stack.filter((open) => open.tracked)).toEqual([]);
  return units;
}

function attr(attrs: string, name: string): string | undefined {
  return new RegExp(`\\s${name}="([^"]*)"`).exec(attrs)?.[1];
}

function claimsOf(shape: ProjectShape): Map<string, ProjectShapeClaim> {
  const claims = new Map<string, ProjectShapeClaim>();
  claims.set(shape.claim.claimId, shape.claim);
  if (shape.kind !== 'observed') return claims;
  for (const group of [shape.projectAccount, shape.sources, shape.items, Object.values(shape.classes), shape.facts]) {
    for (const entry of group) claims.set(entry.claim.claimId, entry.claim);
  }
  return claims;
}

interface ExpectedAnchor { readonly cls: string; readonly target: string; readonly revision: string }

/** Independent re-derivation of each claim's anchor set from the model. */
function expectedAnchors(model: PocModel, claimId: string, blockId: string): ExpectedAnchor[] {
  const shape = model.projectShape;
  const revision = shape.kind === 'observed' ? shape.identity.revision : '';
  const entity = model.entities.find((candidate) => candidate.id === claimId);
  const relationship = model.relationships.find((candidate) => candidate.id === claimId);
  const provenance = entity?.provenance ?? relationship?.provenance;
  if (provenance !== undefined) {
    return provenance.map((item) => ({ cls: PROVENANCE_CLASS[item.kind] as string, target: `${item.kind}:${item.digest ?? item.revision}`, revision: item.revision }));
  }
  if (claimId === 'region:code-structure' && model.codeStructure.kind === 'observed') {
    return [{ cls: 'evidence', target: `git-tree:${model.codeStructure.revision}`, revision: model.codeStructure.revision }];
  }
  if (claimId === 'region:work-items' && model.workItems.kind === 'observed') {
    return [{ cls: 'work', target: `beads-dolt:${model.workItems.doltRevision}`, revision: model.workItems.doltRevision }];
  }
  // A proposal is never an anchored block (PWB-REQ-015: non-anchorable); the
  // capability-detail test asserts its absence from the anchor population.
  if (claimId === model.proposedWork.id) throw new Error(`proposal registered as an anchored block: ${claimId}`);
  if (claimId === 'claim:project-shape') return [{ cls: 'evidence', target: `git-tree:${revision}`, revision }];
  const claim = claimsOf(shape).get(claimId);
  if (claim === undefined) throw new Error(`no oracle for ${claimId}`);
  // The same baseline-spec item is cited as evidence in the catalog and as
  // the current requirement beside the proposal.
  const cls = blockId.endsWith('/current-authority') ? 'requirement' : 'evidence';
  return claim.support.map((support) => ({ cls, target: support.sourceIdentity ?? `sha256:${support.contentDigest as string}`, revision }));
}

const sortKey = (anchor: ExpectedAnchor): string => `${anchor.cls}|${anchor.target}|${anchor.revision}`;

describe('Polaris narrative claim blocks (PWB-REQ-014; RFC7-2, RFC7-3, RFC7-9)', () => {
  it('classifies every narrative unit with exactly one role and marks it a non-citable presentation artifact', () => {
    let anchored = 0;
    for (const variant of VARIANTS) {
      const html = renderPolarisPage(modelFor(variant));
      const units = narrativeUnits(html);
      expect(units.length).toBeGreaterThan(40);
      for (const unit of units) {
        const roles = [...unit.attrs.matchAll(/\sdata-claim-role="([^"]*)"/g)].map((m) => m[1]);
        expect(roles, `${variant}: <${unit.tag}${unit.attrs}>`).toHaveLength(1);
        expect(ROLES).toContain(roles[0]);
        expect(unit.attrs).toMatch(/\sdata-presentation-artifact(\s|$)/);
        expect(unit.attrs).toMatch(/\sdata-non-citable(\s|$)/);
        if (roles[0] === 'anchored-project-fact') {
          anchored += 1;
          expect(attr(unit.attrs, 'data-narrative-block')).toBeDefined();
          expect(unit.inner).toContain('data-claim-provenance=');
        } else {
          // Only anchored blocks state project facts with provenance.
          expect(unit.inner.split('data-claim-provenance=').length - 1, `${variant}: provenance outside an anchored block: <${unit.tag}${unit.attrs}>`).toBe(0 + (unit.inner.match(/data-claim-role="anchored-project-fact"/g)?.length ?? 0) * 0 + countNested(unit.inner));
        }
        if (roles[0] === 'epistemic-claim') expect(unit.attrs).toContain('data-copy-role="epistemic-disclosure"');
      }
    }
    expect(anchored).toBeGreaterThan(40);
  });

  it('gives every anchored block a typed, revision-bound anchor set that exactly covers its claims (no uncovered claim, no surplus anchor) and captures target state', () => {
    let blocks = 0;
    for (const variant of VARIANTS) {
      const model = modelFor(variant);
      const html = renderPolarisPage(model);
      const machine = JSON.parse(JSON.stringify(model)) as PocModel;
      const narrative = parseNarrativeScript(html);
      expect(narrative.kind).toBe('polaris-narrative');
      expect(narrative.citable).toBe(false);
      expect(narrative.presentation).toBe('presentation-artifact');
      const blockIds = narrative.blocks.map((block) => block.blockId);
      expect(new Set(blockIds).size).toBe(blockIds.length);
      const units = narrativeUnits(html).filter((unit) => attr(unit.attrs, 'data-claim-role') === 'anchored-project-fact');
      expect(units.map((unit) => attr(unit.attrs, 'data-narrative-block')).sort()).toEqual([...blockIds].sort());
      const claims = claimsOf(machine.projectShape);
      for (const unit of units) {
        const blockId = attr(unit.attrs, 'data-narrative-block') as string;
        const block = narrative.blocks.find((candidate) => candidate.blockId === blockId);
        if (block === undefined) throw new Error(blockId);
        expect(block.kind).toBe('narrative-block');
        expect(block.role).toBe('anchored-project-fact');
        expect(block.citable).toBe(false);
        expect(block.presentation).toBe('presentation-artifact');
        // Distinct machine type: none of the kernel claim tuple's fields.
        for (const field of ['claimId', 'epistemic', 'resolutionRoutes', 'challenge', 'evaluationId']) expect(block).not.toHaveProperty(field);
        // Claims in the block are exactly the provenance spans it renders.
        const rendered = [...unit.inner.matchAll(/data-claim-provenance="([^"]+)"/g)].map((m) => m[1] as string);
        expect([...block.claims].sort()).toEqual([...new Set(rendered)].sort());
        // Anchor set: exact covering and minimality against the independent oracle.
        const expected = block.claims.flatMap((claimId) => expectedAnchors(machine, claimId, blockId)).map(sortKey).sort();
        const actual = block.anchors.map((anchor) => sortKey({ cls: anchor.targetClass, target: anchor.targetId, revision: anchor.revision })).sort();
        expect(actual, `${variant}: ${blockId}`).toEqual([...new Set(expected)].sort());
        expect(block.anchors.length).toBeGreaterThan(0);
        expect(block.anchors.length).toBeLessThanOrEqual(MAX_ANCHORS);
        // Human form: each anchor is rendered inside the block, naming its claims.
        for (const anchor of block.anchors) {
          expect(TARGET_CLASSES).toContain(anchor.targetClass);
          expect(anchor.supports.length).toBeGreaterThan(0);
          for (const supported of anchor.supports) expect(block.claims).toContain(supported);
          expect(anchor.revision).not.toBe('');
          // Durable identity: never a bare path, label or coordinate.
          expect(anchor.targetId).toMatch(/^(sha256:[0-9a-f]{64}|git-tree:[0-9a-f]{40}|beads-dolt:.+|[a-z-]+:(sha256:[0-9a-f]{64}|.+)|[^/\s]+@[0-9a-f]{40}:.+#.+)$/);
          expect(anchor.targetId).not.toMatch(/\.[a-z]+:\d+$/); // never path:line
          const cite = new RegExp(`<cite[^>]*data-anchor-id="${anchor.anchorId.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"[^>]*>`).exec(unit.inner)?.[0];
          expect(cite, `${variant}: anchor ${anchor.anchorId} not rendered in its block`).toBeDefined();
          expect(attr(cite as string, 'data-anchor-class')).toBe(anchor.targetClass);
          expect(attr(cite as string, 'data-anchor-target')).toBe(anchor.targetId);
          expect((attr(cite as string, 'data-anchor-for') as string).split('\t')).toEqual([...anchor.supports]);
          // Captured target state equals the machine claim's state at capture.
          const claim = claims.get(anchor.supports[0] as string);
          if (claim !== undefined) {
            expect(anchor.captured.label).toBe(claim.epistemic.label);
            expect(anchor.captured.tier).toBe(claim.epistemic.tier ?? 'unstated');
            expect(anchor.captured.reason).toBe('reasons' in claim.epistemic ? claim.epistemic.reasons.primary : 'none');
          } else {
            expect(anchor.captured.label).toBe('Observed');
          }
          expect(attr(cite as string, 'data-anchor-label')).toBe(anchor.captured.label);
        }
        const citesInBlock = unit.inner.match(/data-anchor-id="/g)?.length ?? 0;
        expect(citesInBlock, `${variant}: ${blockId} renders a cite that is not in its anchor set`).toBe(block.anchors.length);
        blocks += 1;
      }
    }
    expect(blocks).toBeGreaterThan(60);
  });

  it('freezes captured target state: a later mutation of the model cannot rewrite an anchor', () => {
    const model = modelFor('observed');
    const html = renderPolarisPage(model);
    const before = parseNarrativeScript(html);
    const shape = model.projectShape;
    if (shape.kind !== 'observed') throw new Error('fixture must observe');
    const source = shape.sources[0] as { claim: { epistemic: { tier?: string } } };
    (source.claim.epistemic as { tier?: string }).tier = 'derived-fact';
    // The already-rendered artifact is unchanged; a fresh render reflects the
    // later-read state as a *new* capture, never by rewriting the old one.
    expect(parseNarrativeScript(html)).toEqual(before);
    const after = parseNarrativeScript(renderPolarisPage(model));
    const sourceBlock = (n: typeof before): string | undefined => n.blocks.find((block) => block.blockId === `block:${shape.sources[0]?.claim.claimId ?? ''}`)?.anchors[0]?.captured.tier;
    expect(sourceBlock(before)).toBe('report-fact');
    expect(sourceBlock(after)).toBe('derived-fact');
  });

  it('clones and freezes anchors at registration so the caller cannot rewrite a captured state afterwards', () => {
    const registry = new NarrativeRegistry();
    const captured = { label: 'Observed', tier: 'report-fact', reason: 'none' };
    const supports = ['claim:x'];
    const block = registry.registerAnchored('block:x', ['claim:x'], [{ targetClass: 'evidence', targetId: 'sha256:' + 'a'.repeat(64), revision: 'r', locator: 'p', supports, captured }]);
    expect(Object.isFrozen(block)).toBe(true);
    expect(Object.isFrozen(block.anchors)).toBe(true);
    expect(Object.isFrozen(block.anchors[0])).toBe(true);
    expect(Object.isFrozen(block.anchors[0]?.captured)).toBe(true);
    expect(() => { (block.anchors[0] as { captured: { label: string } }).captured.label = 'Inferred'; }).toThrow();
    // The caller's own objects were copied, not adopted.
    expect(Object.isFrozen(captured)).toBe(false);
    captured.label = 'Inferred';
    supports.push('claim:y');
    expect(block.anchors[0]?.captured.label).toBe('Observed');
    expect(block.anchors[0]?.supports).toEqual(['claim:x']);
    expect(registry.narrative().blocks[0]?.anchors[0]?.captured.label).toBe('Observed');
    expect(() => registry.registerAnchored('block:x', [], [])).toThrow(/twice/);
  });

  it('keeps personal view state and the presentation artifact outside the truth model', () => {
    const model = modelFor('observed');
    const truthBefore = JSON.stringify(model);
    const plain = renderPolarisPage(model);
    const withView = renderPolarisPage(model, '', { openCoverageCounts: ['claim:class:principle', 'claim:project-shape'] });
    expect(JSON.stringify(model)).toBe(truthBefore);
    expect(withView).not.toBe(plain);
    expect(withView.replace(/<details class="coverage-counts" data-coverage-counts="[^"]+" open>/g, (m) => m.replace(' open', ''))).toBe(plain);
    expect(withView.match(/<details class="coverage-counts"[^>]* open>/g)?.length).toBe(2);
    expect(parseNarrativeScript(withView)).toEqual(parseNarrativeScript(plain));
    // Deleting Polaris presentation leaves truth unchanged: the model carries
    // no narrative, role, anchor or view field at all.
    expect(truthBefore).not.toMatch(/"(narrative|blocks|claimRole|anchorId|targetClass|viewState|openCoverageCounts|presentation|citable)"/);
  });
});

function countNested(inner: string): number {
  // Provenance spans inside a *nested* anchored block are that block's, not
  // the enclosing framing unit's.
  let total = 0;
  for (const nested of inner.matchAll(/<(p|li|td|tr)([^>]*data-claim-role="anchored-project-fact"[^>]*)>([\s\S]*?)<\/\1>/g)) {
    total += nested[3]?.match(/data-claim-provenance=/g)?.length ?? 0;
  }
  return total;
}
