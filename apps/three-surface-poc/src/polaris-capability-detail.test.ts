import { createHash } from 'node:crypto';
import { readdirSync, readFileSync, rmSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel, ProposedWork } from '@syzygy/three-surface-poc-core';

import { deriveCapabilityDeepDives, resolveVerbatim, type CapabilityDeepDive, type VerbatimLeaf } from './capability-detail.js';
import { parseNarrativeScript } from './polaris-narrative.js';
import { renderCapabilityDeepDive, renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

// ---------------------------------------------------------------------------
// Hand-typed expectations (PWB-REQ-015; RFC7-17). Nothing below is imported
// from the renderer or the capability-detail module's constants.

const BANDS = ['argument', 'contract', 'reality'] as const;
const AUTHORITY_CLASS: Readonly<Record<(typeof BANDS)[number], string>> = {
  argument: 'authored-non-normative',
  contract: 'referenced-verbatim',
  reality: 'kernel-computed',
};
const STATUS_HEADLINES = /\b(healthy|unhealthy|passing|failing|maturity|score|on track|at risk|trend|trending|success rate|approved|accepted|adopted)\b|\d+\s?%/i;
const CHANGE_ID = 'repair-whatsapp-identity-reconciliation';
// The fixture repository's own baseline-spec bytes: captured OpenSpec state,
// restated from the fixture table, never read back from Polaris.
const BASELINE_TEXT = PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC[PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH] as string;

type Variant = 'unevaluated' | 'draft' | 'adopted';

function modelFor(variant: Variant): PocModel {
  switch (variant) {
    case 'unevaluated':
      return buildFixtureModel(cleanups);
    case 'draft':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'adopted':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC) } });
  }
}

function deepDiveSlice(html: string): string {
  const start = html.indexOf('<section class="deep-dive"');
  const end = html.indexOf('data-polaris-group="evidence-and-gaps"', start);
  expect(start).toBeGreaterThan(-1);
  expect(end).toBeGreaterThan(start);
  return html.slice(start, end);
}

function attr(attrs: string, name: string): string[] {
  return [...attrs.matchAll(new RegExp(`\\s${name}="([^"]*)"`, 'g'))].map((match) => match[1] as string);
}

interface SectionRecord {
  readonly id: string;
  readonly band: string | undefined;
  readonly bandAttributeCount: number;
  readonly authorityClass: string | undefined;
  readonly enclosingBand: string | undefined;
  readonly depth: number;
  readonly attrs: string;
  readonly inner: string;
}

/** Every `<section>` in the fragment with its band attributes and the band
 * of its nearest enclosing section, by a stack walk over the markup. */
function sections(fragment: string): SectionRecord[] {
  const out: SectionRecord[] = [];
  const stack: { band: string | undefined; start: number; record: number }[] = [];
  const tags = fragment.matchAll(/<(\/?)section\b([^>]*)>/g);
  for (const tag of tags) {
    if (tag[1] === '/') {
      const frame = stack.pop();
      if (frame === undefined) throw new Error('unbalanced </section>');
      const record = out[frame.record] as SectionRecord;
      out[frame.record] = { ...record, inner: fragment.slice(frame.start, tag.index) };
      continue;
    }
    const attrs = tag[2] as string;
    const bands = attr(attrs, 'data-band');
    const record: SectionRecord = {
      id: attr(attrs, 'data-polaris-section')[0] ?? attr(attrs, 'data-capability-deep-dive')[0] ?? '',
      band: bands[0],
      bandAttributeCount: bands.length,
      authorityClass: attr(attrs, 'data-authority-class')[0],
      enclosingBand: stack[stack.length - 1]?.band,
      depth: stack.length,
      attrs,
      inner: '',
    };
    out.push(record);
    stack.push({ band: bands[0] ?? stack[stack.length - 1]?.band, start: (tag.index as number) + tag[0].length, record: out.length - 1 });
  }
  if (stack.length !== 0) throw new Error(`unclosed <section>: ${stack.length}`);
  return out;
}

function unescapeHtml(text: string): string {
  return text.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}

function verbatimOf(fragment: string): string | undefined {
  const match = /<pre class="verbatim" data-verbatim-text[^>]*>([\s\S]*?)<\/pre>/.exec(fragment);
  return match === null ? undefined : unescapeHtml(match[1] as string);
}

function secondProposal(first: ProposedWork): ProposedWork {
  const changeId = 'replace-whatsapp-identity-with-phone-only';
  return {
    ...first,
    id: `proposed-work:${changeId}`,
    changeId,
    proposal: { ...first.proposal, path: `openspec/changes/${changeId}/proposal.md`, digest: `sha256:${'b'.repeat(64)}` },
    delta: { ...first.delta, path: `openspec/changes/${changeId}/specs/switchboard-identity/spec.md`, digest: `sha256:${'c'.repeat(64)}` },
    lifecycle: { kind: 'observed', state: 'active', evidence: [`openspec/changes/${changeId}/proposal.md`], basis: 'fixture' },
  };
}

describe('Polaris capability deep dive bands (PWB-REQ-015; RFC7-17)', () => {
  it('renders exactly the three bands in order, every block under exactly one band and class, in Base mode with observed reality, over every shape state', () => {
    for (const variant of ['unevaluated', 'draft', 'adopted'] as const) {
      const model = modelFor(variant);
      const html = renderPolarisPage(model);
      const dive = deepDiveSlice(html);
      expect(dive).toContain('data-reading-mode="Base"');
      expect(dive).toContain('data-reading-mode-value="Base"');
      const all = sections(dive);
      const root = all[0] as SectionRecord;
      expect(root.id).toBe(model.capabilityId);
      expect(root.band).toBeUndefined();
      // The band sections are the root's direct children, in the fixed order.
      const bandSections = all.filter((section) => section.depth === 1);
      expect(bandSections.map((section) => section.band)).toEqual([...BANDS]);
      for (const section of bandSections) expect(section.authorityClass).toBe(AUTHORITY_CLASS[section.band as (typeof BANDS)[number]]);
      // Every block below the root carries exactly one band attribute, one
      // class, and never straddles: its band is its enclosing band.
      const blocks = all.slice(1);
      expect(blocks.length).toBeGreaterThan(12);
      for (const block of blocks) {
        expect(block.bandAttributeCount, block.attrs).toBe(1);
        expect(BANDS as readonly string[]).toContain(block.band);
        expect(block.authorityClass).toBe(AUTHORITY_CLASS[block.band as (typeof BANDS)[number]]);
        if (block.depth > 1) expect(block.band, block.attrs).toBe(block.enclosingBand);
      }
      // The machine form names the same block population, band by band.
      const narrative = parseNarrativeScript(html);
      expect(narrative.deepDives).toHaveLength(1);
      const form = narrative.deepDives[0] as (typeof narrative.deepDives)[number];
      expect(form.capabilityId).toBe(model.capabilityId);
      expect(form.readingMode).toBe('Base');
      expect(form.bands.map((band) => band.band)).toEqual([...BANDS]);
      for (const band of form.bands) {
        expect(band.authorityClass).toBe(AUTHORITY_CLASS[band.band]);
        const rendered = blocks.filter((block) => block.band === band.band).map((block) => block.id).sort();
        expect([...band.blockIds].sort()).toEqual(rendered);
      }
      // Base mode includes observed reality: every entity of the slice is a
      // reality-band block, and the relationships list sits there too.
      const reality = blocks.filter((block) => block.band === 'reality');
      for (const entity of model.entities) expect(reality.some((block) => block.id === entity.id), entity.id).toBe(true);
      expect(reality.some((block) => block.id === 'relationships')).toBe(true);
      expect(html.indexOf('data-polaris-group="capability-detail"')).toBeLessThan(html.indexOf('<section class="deep-dive"'));
    }
  });

  it('marks the argument band non-normative: framing only, no anchored block, no anchor, no tuple, no status headline', () => {
    const html = renderPolarisPage(modelFor('adopted'));
    const argument = sections(deepDiveSlice(html)).find((section) => section.depth === 1 && section.band === 'argument') as SectionRecord;
    const roles = [...argument.inner.matchAll(/data-claim-role="([^"]+)"/g)].map((match) => match[1]);
    expect(roles.length).toBeGreaterThan(3);
    expect(new Set(roles)).toEqual(new Set(['non-normative-framing']));
    expect(argument.inner).not.toContain('data-narrative-block');
    expect(argument.inner).not.toContain('data-anchor-');
    expect(argument.inner).not.toContain('claim-tuple');
    expect(argument.inner).not.toContain('data-unknown-disclosure');
    expect(argument.inner.replace(/<[^>]+>/g, ' ')).not.toMatch(STATUS_HEADLINES);
    // It points at the motivating intent and the project overview; it restates neither.
    expect(argument.inner).toContain('data-argument-ref="intent:req-switchboard-identity-001"');
    expect(argument.inner).toContain('data-argument-ref="group:overview"');
  });

  it('renders requirement text only byte-for-byte from the owning artifact at render, or Unknown with its reason; stores nothing', () => {
    const model = modelFor('adopted');
    const before = JSON.stringify(model);
    // Production: no reader, so the leaf identity is captured and the text is
    // disclosed as outside the consented content class.
    const bare = renderPolarisPage(model);
    const bareDive = deepDiveSlice(bare);
    expect(bareDive).toContain('data-contract-part="requirement-text"');
    expect(bareDive).toContain('data-verbatim="not-rendered"');
    expect(bareDive).not.toContain('data-verbatim-text');
    expect(bareDive).toContain('data-unknown-reason="unconsented-source-or-provider"');
    const bareForm = parseNarrativeScript(bare).deepDives[0];
    expect(bareForm?.intent.verbatim).toBe('not-rendered');
    expect(bareForm?.intent.reason).toBe('unconsented-source-or-provider');
    const machine = JSON.parse(before) as PocModel;
    if (machine.proposedWork.currentAuthority.kind !== 'baseline-spec') throw new Error('fixture: baseline spec not observed');
    const leafIdentity = machine.proposedWork.currentAuthority.claim.support[0]?.sourceIdentity as string;
    expect(leafIdentity).toMatch(/#[0-9a-f]{40}$/);
    // The leaf is bound to the shape's observed revision (the identity's own `@<revision>`).
    const shapeRevision = machine.projectShape.kind === 'observed' ? machine.projectShape.identity.revision : '';
    expect(leafIdentity).toContain(`@${shapeRevision}:`);
    expect(bareForm?.intent.leaf).toEqual({ path: PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH, revision: shapeRevision, identity: leafIdentity });

    // With the owning artifact's bytes offered at render: exact bytes, exact identity.
    const reads: VerbatimLeaf[] = [];
    const reader = (leaf: VerbatimLeaf): Uint8Array | undefined => {
      reads.push(leaf);
      return leaf.path === PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH ? new TextEncoder().encode(BASELINE_TEXT) : undefined;
    };
    const rendered = renderPolarisPage(model, '', {}, { verbatim: reader });
    const renderedDive = deepDiveSlice(rendered);
    expect(reads).toEqual([{ path: PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH, revision: shapeRevision, identity: leafIdentity }]);
    expect(renderedDive).toContain('data-verbatim="rendered"');
    expect(renderedDive).toContain(`data-verbatim-identity="${leafIdentity}"`);
    expect(verbatimOf(renderedDive)).toBe(BASELINE_TEXT);
    expect(parseNarrativeScript(rendered).deepDives[0]?.intent.verbatim).toBe('rendered');
    // The bytes appear exactly once on the page — the verbatim block — and
    // never in the machine form: no reorganized second copy.
    expect(rendered.split(BASELINE_TEXT.trim()).length - 1).toBe(1);
    expect(/<script type="application\/json"[^>]*>[\s\S]*?<\/script>/.exec(rendered)?.[0]).not.toContain(BASELINE_TEXT.trim());
    // The text sits inside the current-authority part, before the proposal.
    const textAt = renderedDive.indexOf('data-verbatim-text');
    expect(textAt).toBeGreaterThan(renderedDive.indexOf('data-proposed-work-part="current-authority"'));
    expect(textAt).toBeLessThan(renderedDive.indexOf('data-proposed-work-part="proposal"'));

    // Fail closed: bytes that do not hash to the captured identity are not
    // rendered, and nothing of them reaches the page; an unreadable leaf is Unknown.
    const forged = 'FORGED-REQUIREMENT-TEXT-' + BASELINE_TEXT;
    const forgedPage = renderPolarisPage(model, '', {}, { verbatim: () => new TextEncoder().encode(forged) });
    expect(forgedPage).not.toContain('FORGED-REQUIREMENT-TEXT');
    expect(deepDiveSlice(forgedPage)).toContain('data-unknown-reason="reference-unresolvable"');
    expect(deepDiveSlice(forgedPage)).toContain('data-verbatim="not-rendered"');
    const unreadable = renderPolarisPage(model, '', {}, { verbatim: () => undefined });
    expect(deepDiveSlice(unreadable)).toContain('data-unknown-reason="source-uncaptured-or-unreachable"');
    const binary = renderPolarisPage(model, '', {}, { verbatim: () => new Uint8Array([0xff, 0xfe, 0x00]) });
    expect(deepDiveSlice(binary)).toContain('data-verbatim="not-rendered"');

    // Nothing was stored: the model is byte-identical after every render, the
    // machine answer never carries the text, and the bare render never did.
    expect(JSON.stringify(model)).toBe(before);
    expect(before).not.toContain(BASELINE_TEXT.trim());
    expect(bare).not.toContain(BASELINE_TEXT.trim());

    // Governing doctrine and non-goals: no declared link, so Unknown with a
    // reason and route, never a restated or summarized text.
    for (const part of ['doctrine', 'non-goals'] as const) {
      const section = sections(renderedDive).find((candidate) => candidate.attrs.includes(`data-contract-part="${part}"`)) as SectionRecord;
      expect(section.band).toBe('contract');
      expect(section.inner).toContain('data-unknown-reason="missing-declaration"');
      expect(section.inner).toContain('Route:');
      expect(section.inner).not.toContain('data-verbatim-text');
    }
    // When the shape is not observed the same parts carry the shape's reason.
    const unevaluated = deepDiveSlice(renderPolarisPage(modelFor('unevaluated')));
    const doctrine = sections(unevaluated).find((candidate) => candidate.attrs.includes('data-contract-part="doctrine"')) as SectionRecord;
    expect(doctrine.inner).toContain('data-unknown-reason="unconsented-source-or-provider"');
    expect(unevaluated).toContain('data-verbatim="not-rendered"');
    expect(unevaluated).not.toContain('data-verbatim-text');
  });

  it('keeps a draft capability unadopted and an adopted one adopted, from the observed tree, in both channels', () => {
    const draftModel = modelFor('draft');
    const draft = deepDiveSlice(renderPolarisPage(draftModel));
    expect(draft).toContain('data-capability-adoption="draft"');
    expect(draft).toContain('data-capability-adoption-state="draft"');
    expect(draft).not.toContain('data-capability-adoption-state="adopted"');
    expect(draft).not.toContain('data-parity-field="current-authority-path"');
    expect(draft).toContain('data-unknown-reason="missing-declaration"');
    expect(parseNarrativeScript(renderPolarisPage(draftModel)).deepDives[0]?.adoption).toBe('draft');
    // Oracle: the machine answer's own current-authority lookup.
    expect(draftModel.proposedWork.currentAuthority.kind).toBe('unknown');

    const adoptedModel = modelFor('adopted');
    const adopted = deepDiveSlice(renderPolarisPage(adoptedModel));
    expect(adopted).toContain('data-capability-adoption="adopted"');
    expect(adopted).toContain('data-capability-adoption-state="adopted"');
    expect(adoptedModel.proposedWork.currentAuthority.kind).toBe('baseline-spec');

    const unevaluated = deepDiveSlice(renderPolarisPage(modelFor('unevaluated')));
    expect(unevaluated).toContain('data-capability-adoption="unknown"');
    expect(unevaluated).not.toContain('data-capability-adoption-state=');
  });

  it('renders every proposal adjacent to the current intent, visibly distinct, non-anchorable and non-status-bearing; competing proposals stay separate futures', () => {
    const model = modelFor('adopted');
    const html = renderPolarisPage(model);
    const dive = deepDiveSlice(html);
    const machine = JSON.parse(JSON.stringify(model)) as PocModel;
    const proposal = sections(dive).find((section) => section.attrs.includes('data-proposed-work-part="proposal"')) as SectionRecord;
    expect(proposal.band).toBe('contract');
    expect(proposal.attrs).toContain(`data-candidate-future="${CHANGE_ID}"`);
    expect(proposal.attrs).toContain('data-anchorable="false"');
    expect(proposal.attrs).toContain('data-status-bearing="false"');
    expect(proposal.attrs).toContain('data-exclusive-with=""');
    expect(proposal.inner).toContain('Proposed change — not current authority.');
    for (const forbidden of ['data-anchor-', 'data-narrative-block', 'claim-tuple', 'data-epistemic-label', 'data-claim-provenance']) {
      expect(proposal.inner, forbidden).not.toContain(forbidden);
    }
    expect(proposal.inner.replace(/<[^>]+>/g, ' ')).not.toMatch(STATUS_HEADLINES);
    // Its artifacts are cited by digest but are no anchor target anywhere.
    const digests = [machine.proposedWork.proposal.digest, machine.proposedWork.delta.digest];
    for (const digest of digests) {
      expect(proposal.inner).toContain(`data-proposal-artifact="${digest}"`);
      expect(html).not.toContain(`data-anchor-target="${digest}"`);
    }
    const narrative = parseNarrativeScript(html);
    for (const block of narrative.blocks) {
      expect(block.claims).not.toContain(machine.proposedWork.id);
      for (const anchor of block.anchors) expect(digests).not.toContain(anchor.targetId);
    }
    const form = narrative.deepDives[0];
    expect(form?.proposals).toEqual([{ changeId: CHANGE_ID, exclusiveWith: [], anchorable: false, statusBearing: false }]);
    expect(form?.exclusivityBasis).toBe('not-captured');
    // The current intent precedes it inside the same block.
    const proposedWork = sections(dive).find((section) => section.id === `contract:${model.capabilityId}/proposed-work`) as SectionRecord;
    expect(proposedWork.inner.indexOf('data-proposed-work-part="current-authority"')).toBeLessThan(proposedWork.inner.indexOf('data-proposed-work-part="proposal"'));

    // Sweep case: a draft capability with two incompatible proposals. The dive
    // is the model's, with the second proposal and its exclusivity declared as
    // captured OpenSpec state would declare them.
    const draftModel = modelFor('draft');
    const base = deriveCapabilityDeepDives(draftModel)[0] as CapabilityDeepDive;
    const first = draftModel.proposedWork;
    const second = secondProposal(first);
    const competing: CapabilityDeepDive = {
      ...base,
      proposals: [first, second],
      exclusivity: [{ group: 'switchboard-identity-futures', changeIds: [first.changeId, second.changeId] }],
      exclusivityBasis: 'declared',
    };
    const { html: fragment, narrative: fragmentNarrative } = renderCapabilityDeepDive(competing, draftModel);
    expect(fragment).toContain('data-capability-adoption="draft"');
    const futures = sections(fragment).filter((section) => section.attrs.includes('data-candidate-future='));
    expect(futures.map((section) => attr(section.attrs, 'data-candidate-future')[0])).toEqual([first.changeId, second.changeId]);
    for (const [index, future] of futures.entries()) {
      const other = index === 0 ? second.changeId : first.changeId;
      const own = index === 0 ? first.changeId : second.changeId;
      expect(attr(future.attrs, 'data-exclusive-with')).toEqual([other]);
      expect(future.attrs).toContain('data-anchorable="false"');
      expect(future.inner).toContain(`data-parity-field="proposal-change-id">${own}<`);
      expect(future.inner).not.toContain(`data-parity-field="proposal-change-id">${other}<`);
      expect(future.inner).toContain(`data-exclusive-change="${other}"`);
      expect(future.inner).toContain('Competing proposals stay separate');
      expect(future.inner).not.toContain('data-anchor-');
    }
    // Never collapsed: no block names both change ids as its own, and the
    // machine form keeps two futures each exclusive with the other.
    const own = (text: string): string[] => [...text.matchAll(/data-parity-field="proposal-change-id">([^<]+)</g)].map((match) => match[1] as string);
    for (const section of sections(fragment)) {
      if (section.attrs.includes('data-candidate-future=')) expect(own(section.inner)).toHaveLength(1);
    }
    const dives = fragmentNarrative.deepDives[0];
    expect(dives?.proposals).toEqual([
      { changeId: first.changeId, exclusiveWith: [second.changeId], anchorable: false, statusBearing: false },
      { changeId: second.changeId, exclusiveWith: [first.changeId], anchorable: false, statusBearing: false },
    ]);
    expect(dives?.exclusivityBasis).toBe('declared');
    expect(dives?.adoption).toBe('draft');
    for (const block of fragmentNarrative.blocks) {
      for (const anchor of block.anchors) expect([second.proposal.digest, second.delta.digest, first.proposal.digest, first.delta.digest]).not.toContain(anchor.targetId);
    }
    // The second proposal's identity is not in the model: the fragment came from the dive, not from truth.
    expect(JSON.stringify(draftModel)).not.toContain(second.changeId);
  });

  it('seam: verbatim resolution accepts only bytes that hash to the captured identity', () => {
    const bytes = new TextEncoder().encode('# leaf\n');
    const gitIdentity = 'butlers@rev:openspec/specs/x/spec.md#' + 'a'.repeat(40);
    expect(resolveVerbatim({ path: 'p', revision: 'r', identity: gitIdentity }, undefined).kind).toBe('not-rendered');
    const mismatch = resolveVerbatim({ path: 'p', revision: 'r', identity: gitIdentity }, () => bytes);
    expect(mismatch).toMatchObject({ kind: 'not-rendered', reason: 'reference-unresolvable' });
    const noDigest = resolveVerbatim({ path: 'p', revision: 'r', identity: 'no-digest-here' }, () => bytes);
    expect(noDigest).toMatchObject({ kind: 'not-rendered', reason: 'reference-unresolvable' });
    const sha = createHash('sha256').update(bytes).digest('hex');
    const ok = resolveVerbatim({ path: 'p', revision: 'r', identity: `sha256:${sha}` }, () => bytes);
    expect(ok).toEqual({ kind: 'rendered', identity: `sha256:${sha}`, text: '# leaf\n' });
    const nul = resolveVerbatim({ path: 'p', revision: 'r', identity: `sha256:${createHash('sha256').update(new Uint8Array([0x41, 0x00])).digest('hex')}` }, () => new Uint8Array([0x41, 0x00]));
    expect(nul).toMatchObject({ kind: 'not-rendered', reason: 'excluded-content' });
  });

  it('static-source sweep: no implementation source stores a normative requirement, scenario, doctrine or non-goal copy', () => {
    const roots = ['apps', 'packages'].map((root) => join(process.cwd(), root));
    const files: string[] = [];
    const walk = (directory: string): void => {
      for (const entry of readdirSync(directory)) {
        const path = join(directory, entry);
        if (entry === 'node_modules' || entry === 'dist') continue;
        if (statSync(path).isDirectory()) walk(path);
        else if (/\.ts$/.test(entry) && !/\.test\.ts$/.test(entry) && !/^test-/.test(entry)) files.push(path);
      }
    };
    for (const root of roots) walk(root);
    expect(files.length).toBeGreaterThan(60);
    // A normative copy is requirement/scenario grammar or a doctrine/non-goal
    // heading inside a string or template literal (comments are prose about
    // the rules, not copies of an owning artifact's text).
    const NORMATIVE = /\bSHALL\b|\*\*(?:WHEN|THEN|AND)\*\*|#{2,4}\s+(?:Requirement|Scenario):|\bNon-Goals\b/;
    const offenders: string[] = [];
    for (const file of files) {
      const source = readFileSync(file, 'utf8').replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '');
      const literals = [...source.matchAll(/'(?:[^'\\\n]|\\.)*'|"(?:[^"\\\n]|\\.)*"|`(?:[^`\\]|\\.)*`/g)].map((match) => match[0]);
      if (literals.some((literal) => NORMATIVE.test(literal))) offenders.push(file.slice(process.cwd().length + 1));
      expect(source).not.toContain(BASELINE_TEXT);
    }
    expect(offenders).toEqual([]);
  });
});
