// The Polaris shape/judgment variants the task-4.4 accessibility checks
// walk, shared by the gated browser test and the evidence CLI. Each variant
// renders the full page (project summary, catalogs, capability detail and
// exact-source rows) from the in-memory fixtures — no Butlers repository is
// read — and names the in-page targets a keyboard reader must reach.
import { createHash } from 'node:crypto';

import type { PocModel } from '@syzygy/three-surface-poc-core';

import { renderPolarisPage } from './polaris.js';
import { buildFixtureModel } from './test-model-fixture.js';
import { ADMITTING_AUTHORITY, PROJECT_SHAPE_FIXTURE_TEXTS, REJECTING_AUTHORITY, projectShapeFixtureGit } from './test-project-shape-fixture.js';
import { walkthroughJudgmentFixture } from './test-walkthrough-judgment-fixture.js';

export interface AccessibilityVariant {
  readonly id: string;
  readonly shape: 'not-evaluated' | 'not-admitted' | 'observation-failed' | 'observed' | 'observed-degraded';
  readonly judgment: 'not-evaluated' | 'lawful-state-1' | 'unlawful';
}

export const ACCESSIBILITY_VARIANTS: readonly AccessibilityVariant[] = [
  { id: 'observed', shape: 'observed', judgment: 'not-evaluated' },
  { id: 'observed-lawful-state-1', shape: 'observed', judgment: 'lawful-state-1' },
  { id: 'observed-degraded-unlawful', shape: 'observed-degraded', judgment: 'unlawful' },
  { id: 'not-admitted', shape: 'not-admitted', judgment: 'not-evaluated' },
  { id: 'observation-failed', shape: 'observation-failed', judgment: 'not-evaluated' },
  { id: 'not-evaluated', shape: 'not-evaluated', judgment: 'not-evaluated' },
];

const DEGRADED_SOURCE = 'about/heart-and-soul/vision.md';

function blobObjectId(text: string): string {
  const body = new TextEncoder().encode(text);
  return createHash('sha1').update(`blob ${body.byteLength}\0`).update(body).digest('hex');
}

function modelFor(variant: AccessibilityVariant, cleanups: string[]): PocModel {
  const judgment = variant.judgment === 'not-evaluated' ? {} : { walkthroughJudgment: walkthroughJudgmentFixture(variant.judgment) };
  switch (variant.shape) {
    case 'not-evaluated':
      return buildFixtureModel(cleanups, judgment);
    case 'not-admitted':
      return buildFixtureModel(cleanups, { projectShape: { authority: REJECTING_AUTHORITY, runGit: projectShapeFixtureGit() }, ...judgment });
    case 'observation-failed': {
      const inner = projectShapeFixtureGit();
      const failing = (args: readonly string[]): Uint8Array => {
        if (args[0] === 'ls-tree') throw new Error('fixture: tree listing refused');
        return inner(args);
      };
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: failing }, ...judgment });
    }
    case 'observed':
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: projectShapeFixtureGit() }, ...judgment });
    case 'observed-degraded': {
      // Refuse one phase-B body read so that source stays Unknown and the
      // gap / reason-count regions render.
      const inner = projectShapeFixtureGit();
      const refused = blobObjectId(PROJECT_SHAPE_FIXTURE_TEXTS[DEGRADED_SOURCE] as string);
      const refusing = (args: readonly string[]): Uint8Array => {
        if (args[0] === 'cat-file' && args[2] === refused) throw new Error('fixture: body read refused');
        return inner(args);
      };
      return buildFixtureModel(cleanups, { projectShape: { authority: ADMITTING_AUTHORITY, runGit: refusing }, ...judgment });
    }
  }
}

export interface RenderedVariant {
  readonly html: string;
  /** In-page ids a keyboard reader must be able to reach through a link. */
  readonly expectedTargets: readonly string[];
}

/** Renders one variant's Polaris page and lists its required targets. */
export function renderVariant(variant: AccessibilityVariant, cleanups: string[]): RenderedVariant {
  const model = modelFor(variant, cleanups);
  const html = renderPolarisPage(model);
  // Every rendered group and capability deep dive must be reachable by a
  // link: the expectation comes from the ids present, not from the links.
  const expectedTargets = ['main-content', ...Array.from(html.matchAll(/ id="(polaris-group-[a-z-]+|polaris-deep-dive-[^"]+)"/g), (m) => m[1] as string)];
  return { html, expectedTargets: [...new Set(expectedTargets)] };
}
