// Live PWB-LIVE-02/03/05 regression. The authority evaluator runs before the
// first Butlers body read; unset SYZYGY_POC_BUTLERS_REPO keeps CI hermetic.

import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

import {
  PWB_REPOSITORY_ID,
  PWB_SECRET_POLICY,
  buildProjectShape,
  classifyPhaseASeed,
  compileDetectors,
  evaluateBodyReadAuthority,
  gitRunnerFor,
  observeProjectShapeSources,
} from '@syzygy/three-surface-poc-core';

import { loadBodyReadAuthorityInputs } from './governance-inputs.js';

const BUTLERS_REPO = process.env.SYZYGY_POC_BUTLERS_REPO;
const describeLive = BUTLERS_REPO === undefined ? describe.skip : describe;
const SYZYGY_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const BUTLERS_REVISION = 'a3dd1fe08a1d9a11b5e899e0ecf33f03d8eefc96';
const CAPTURED_AT = '2026-09-05T00:00:00Z';

function syzygyRevision(): string {
  return execFileSync('git', ['-C', SYZYGY_ROOT, 'rev-parse', 'HEAD^{commit}'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
}

describeLive('live Butlers project-shape discovery at the reviewed revision', () => {
  it('matches the independent five-root, seven-Heart, baseline and total populations', () => {
    const authority = evaluateBodyReadAuthority(loadBodyReadAuthorityInputs({
      repoRoot: SYZYGY_ROOT,
      governanceRevision: syzygyRevision(),
      evaluationId: 'evaluation:pwb-discovery-live-a3dd1fe',
      evaluationInstant: CAPTURED_AT,
    }));
    expect(authority.admits).toBe(true);
    const runGit = gitRunnerFor(BUTLERS_REPO as string);
    const detectors = compileDetectors(PWB_SECRET_POLICY);
    const observation = observeProjectShapeSources({
      repositoryId: PWB_REPOSITORY_ID,
      revision: BUTLERS_REVISION,
      capturedAt: CAPTURED_AT,
      runGit,
      authority,
      classifyPhaseA: (text) => classifyPhaseASeed(detectors, text),
    });
    expect(observation.kind).toBe('observed');
    if (observation.kind !== 'observed') return;
    expect(observation.revision).toBe(BUTLERS_REVISION);
    expect(observation.manifest.pillars.map((pillar) => [pillar.key, pillar.state, pillar.root])).toEqual([
      ['heart-and-soul', 'discovered', 'about/heart-and-soul'],
      ['legends-and-lore', 'discovered', 'about/legends-and-lore'],
      ['spec-and-spine', 'unknown', 'openspec'],
      // The current signed active-content policy excludes this index. The
      // root is still recognized and the dependent class remains Unknown.
      ['lay-and-land', 'unknown', 'about/lay-and-land'],
      ['craft-and-care', 'discovered', 'about/craft-and-care'],
    ]);
    expect({
      total: observation.sources.length,
      about: observation.sources.filter((source) => source.path.startsWith('about/')).length,
      baseline: observation.sources.filter((source) => /^openspec\/specs\/[^/]+\/spec\.md$/.test(source.path)).length,
      roster: observation.sources.filter((source) => /^roster\/[^/]+\/(?:butler\.toml|MANIFESTO\.md)$/.test(source.path)).length,
    }).toEqual({ total: 255, about: 48, baseline: 183, roster: 24 });
    expect(observation.sources.filter((source) => source.path.startsWith('about/heart-and-soul/')).map((source) => source.path)).toEqual([
      'about/heart-and-soul/README.md',
      'about/heart-and-soul/architecture.md',
      'about/heart-and-soul/design-language.md',
      'about/heart-and-soul/development.md',
      'about/heart-and-soul/security.md',
      'about/heart-and-soul/v1.md',
      'about/heart-and-soul/vision.md',
    ]);

    const shape = buildProjectShape({ authority, revision: BUTLERS_REVISION, capturedAt: CAPTURED_AT, runGit });
    expect(shape.kind).toBe('observed');
    if (shape.kind !== 'observed') return;
    expect(shape.counts.sources).toBe(255);
    expect(shape.counts.classification.classifiedByBasis).toEqual({ body: 46, 'path-only': 183 });
    expect(shape.counts.sourcesWithKnownItemDenominator).toBe(229);
    expect(shape.items.filter((item) => item.class === 'baseline-spec')).toHaveLength(183);
    expect(shape.classes['baseline-spec'].denominator).toEqual({ kind: 'known', value: 183 });
    expect(shape.sources.find((source) => source.path === 'about/heart-and-soul/vision.md')?.itemDenominator).toEqual({ kind: 'known', value: 15 });
    expect(shape.sources.find((source) => source.path === 'about/heart-and-soul/architecture.md')?.itemDenominator).toEqual({ kind: 'known', value: 1 });
    expect(shape.sources.find((source) => source.path === 'about/heart-and-soul/v1.md')?.itemDenominator).toMatchObject({
      kind: 'unknown',
      grammarFailure: { reason: 'ambiguous-leading-label', class: 'catalog-entry', line: 95 },
    });
    expect(shape.projectAccount.filter((entry) => entry.claim.epistemic.label === 'Observed')).toHaveLength(4);
    expect(shape.projectAccount.filter((entry) => entry.claim.epistemic.label === 'Unknown').map((entry) => entry.key)).toEqual(['v1-scope', 'v1-success']);
  });
});
