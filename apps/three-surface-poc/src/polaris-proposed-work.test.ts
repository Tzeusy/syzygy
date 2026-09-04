import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import type { PocModel } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import {
  ADMITTING_AUTHORITY,
  PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC,
  projectShapeFixtureGit,
} from './test-project-shape-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

// Expected identities come from the OpenSpec artifacts the fixture repository
// commits (test-model-fixture.ts), restated by hand — never from Polaris or
// from the model's proposedWork field.
const CHANGE_ID = 'repair-whatsapp-identity-reconciliation';
const PROPOSED_IDENTITIES = [
  CHANGE_ID,
  `openspec/changes/${CHANGE_ID}/proposal.md`,
  `openspec/changes/${CHANGE_ID}/specs/switchboard-identity/spec.md`,
] as const;
const CURRENT_AUTHORITY = 'openspec/specs/switchboard-identity/spec.md';

type Variant = 'unevaluated' | 'observed-without-baseline' | 'observed-with-baseline';

function modelFor(variant: Variant): PocModel {
  switch (variant) {
    case 'unevaluated':
      return buildFixtureModel(cleanups);
    case 'observed-without-baseline':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() } });
    case 'observed-with-baseline':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit(PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC) } });
  }
}

function slices(page: string): { projectLevel: string; detail: string; evidence: string } {
  // The PWB-REQ-014 machine form (an application/json script) is not
  // rendered narrative; it names every block on the page and is excluded here.
  const html = page.replace(/<script type="application\/json"[^>]*>[\s\S]*?<\/script>/g, '');
  const main = html.indexOf('<main');
  const detailStart = html.indexOf('data-polaris-group="capability-detail"');
  const evidenceStart = html.indexOf('data-polaris-group="evidence-and-gaps"');
  expect(main).toBeGreaterThan(-1);
  expect(detailStart).toBeGreaterThan(main);
  expect(evidenceStart).toBeGreaterThan(detailStart);
  return {
    projectLevel: html.slice(main, detailStart),
    detail: html.slice(detailStart, evidenceStart),
    evidence: html.slice(evidenceStart),
  };
}

function count(haystack: string, needle: string): number {
  return haystack.split(needle).length - 1;
}

describe('Polaris proposed work stays subordinate to current truth (PWB-REQ-013)', () => {
  it('keeps every proposed identity out of the project-level groups and the evidence group, in every shape state', () => {
    for (const variant of ['unevaluated', 'observed-without-baseline', 'observed-with-baseline'] as const) {
      const html = renderPolarisPage(modelFor(variant));
      const { projectLevel, detail, evidence } = slices(html);
      for (const identity of PROPOSED_IDENTITIES) {
        expect(projectLevel, `${variant}: ${identity} in project level`).not.toContain(identity);
        expect(evidence, `${variant}: ${identity} in evidence`).not.toContain(identity);
        expect(detail, `${variant}: ${identity} missing from detail`).toContain(identity);
      }
      // The project account, when observed, is built from the shape's sources,
      // none of which is an OpenSpec change.
      expect(projectLevel).not.toContain('openspec/changes/');
      expect(evidence).not.toContain('openspec/changes/');
    }
  });

  it('renders the proposal exactly once, inside capability detail, labeled, with the current authority adjacent and first', () => {
    for (const variant of ['unevaluated', 'observed-without-baseline', 'observed-with-baseline'] as const) {
      const model = modelFor(variant);
      const html = renderPolarisPage(model);
      const { detail } = slices(html);
      const marker = `data-polaris-section="contract:${model.capabilityId}/proposed-work"`;
      expect(count(html, marker)).toBe(1);
      expect(count(detail, marker)).toBe(1);
      const start = detail.indexOf(marker);
      const end = detail.indexOf('data-contract-part="doctrine"', start);
      expect(end).toBeGreaterThan(start);
      const section = detail.slice(start, end);
      // Visibly labeled as a proposal, with the change id and lifecycle state as data.
      expect(section).toContain(`data-proposal-change="${CHANGE_ID}"`);
      expect(section).toContain('data-proposal-lifecycle="active"');
      expect(section).toContain('data-proposal-label');
      expect(section).toContain('Proposed change — not current authority.');
      expect(section).toContain('data-proposal-lifecycle-state="active"');
      // Current authority precedes the proposal within the same section.
      const current = section.indexOf('data-proposed-work-part="current-authority"');
      const proposal = section.indexOf('data-proposed-work-part="proposal"');
      expect(current).toBeGreaterThan(-1);
      expect(proposal).toBeGreaterThan(current);
      expect(section).toContain(`data-parity-field="proposal-change-id">${CHANGE_ID}<`);
      expect(section).toContain(`amends <code>${CURRENT_AUTHORITY}</code>`);
      // The capability's argument band comes before the proposal, so the
      // proposal never leads the detail (PWB-REQ-015 puts it in the contract band).
      expect(detail.indexOf('data-band="argument"')).toBeLessThan(start);
      expect(detail.indexOf('data-band="argument"')).toBeGreaterThan(-1);
    }
  });

  it('shows the current authority as the shape\'s own baseline-spec claim when observed, and Unknown with its reason and route otherwise', () => {
    const unevaluated = renderPolarisPage(modelFor('unevaluated'));
    const currentOf = (html: string): string => {
      const start = html.indexOf('data-proposed-work-part="current-authority"');
      return html.slice(start, html.indexOf('data-contract-part="requirement-text"', start));
    };
    expect(currentOf(unevaluated)).toContain('data-unknown-reason="unconsented-source-or-provider"');
    expect(currentOf(unevaluated)).toContain('Route: Record consent');
    expect(currentOf(unevaluated)).not.toContain('data-parity-field="current-authority-path"');

    const without = renderPolarisPage(modelFor('observed-without-baseline'));
    expect(currentOf(without)).toContain('data-unknown-reason="missing-declaration"');
    expect(currentOf(without)).toContain(CURRENT_AUTHORITY);
    expect(currentOf(without)).not.toContain('data-parity-field="current-authority-path"');

    const model = modelFor('observed-with-baseline');
    const html = renderPolarisPage(model);
    const current = currentOf(html);
    expect(current).toContain(`data-parity-field="current-authority-path">${CURRENT_AUTHORITY}<`);
    expect(current).not.toContain('data-unknown-disclosure=');
    // Same identity and tuple as the catalog's baseline-spec item (PWB-REQ-011).
    const machine = JSON.parse(JSON.stringify(model)) as PocModel;
    expect(machine.proposedWork.currentAuthority.kind).toBe('baseline-spec');
    if (machine.proposedWork.currentAuthority.kind !== 'baseline-spec') throw new Error('unreachable');
    const claimId = machine.proposedWork.currentAuthority.claim.claimId;
    expect(claimId).toBe('claim:item:baseline-spec:switchboard-identity');
    expect(current).toContain(`data-claim-id="${claimId}"`);
    expect(current).toContain(`data-claim-provenance="${claimId}"`);
    const { projectLevel } = slices(html);
    expect(projectLevel).toContain(`data-polaris-item="${claimId}"`);
    const tuple = (fragment: string): string | undefined => new RegExp(`<span class="claim-tuple" data-claim-id="${claimId}"[^>]*>([^<]*)<`).exec(fragment)?.[1];
    expect(tuple(current)).toBeDefined();
    expect(tuple(current)).toBe(tuple(projectLevel));
    expect(tuple(current)).toBe(`Observed · ${machine.proposedWork.currentAuthority.claim.epistemic.tier ?? 'unstated'} · ${machine.proposedWork.currentAuthority.claim.epistemic.freshness ?? 'unstated'} · ${machine.proposedWork.currentAuthority.claim.challenge}`);
  });

  it('carries the same identities and lifecycle in the machine answer as in the human attributes', () => {
    const model = modelFor('observed-with-baseline');
    const machine = JSON.parse(JSON.stringify(model)) as PocModel;
    expect(machine.proposedWork.kind).toBe('proposed-work');
    expect(machine.proposedWork.changeId).toBe(CHANGE_ID);
    expect(machine.proposedWork.specKey).toBe('switchboard-identity');
    expect(machine.proposedWork.proposal.path).toBe(PROPOSED_IDENTITIES[1]);
    expect(machine.proposedWork.delta.path).toBe(PROPOSED_IDENTITIES[2]);
    expect(machine.proposedWork.lifecycle).toMatchObject({ kind: 'observed', state: 'active' });
    if (machine.proposedWork.lifecycle.kind !== 'observed') throw new Error('unreachable');
    expect(machine.proposedWork.lifecycle.evidence).toEqual(expect.arrayContaining([PROPOSED_IDENTITIES[1], PROPOSED_IDENTITIES[2]]));
    for (const path of machine.proposedWork.lifecycle.evidence) expect(path.startsWith(`openspec/changes/${CHANGE_ID}/`)).toBe(true);
    const html = renderPolarisPage(model);
    expect(html).toContain(`data-proposal-lifecycle="${machine.proposedWork.lifecycle.state}"`);
    expect(html).toContain(`data-proposal-capability="${machine.proposedWork.capabilityId}"`);
    expect(machine.proposedWork.capabilityId).toBe(machine.capabilityId);
  });
});
