// Live PWB-LIVE-02/03/05 regression, re-pinned to the gen-2 reconciliation
// head (PWB-RECON-08). The authority evaluator runs before the first Butlers
// body read; unset SYZYGY_POC_BUTLERS_REPO keeps CI hermetic. The expected
// populations are hand-typed from `git ls-tree -r -z ec8b1f6` and the
// retained gen-2 demo record, never from this pipeline's output.

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
const BUTLERS_REVISION = 'ec8b1f6cd529a976700a1360acfac1efc29f9762';
const CAPTURED_AT = '2026-09-06T04:00:00Z';

function syzygyRevision(): string {
  return execFileSync('git', ['-C', SYZYGY_ROOT, 'rev-parse', 'HEAD^{commit}'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
}

describeLive('live Butlers project-shape discovery at the reviewed revision', () => {
  it('matches the independent five-root, seven-Heart, baseline and total populations', () => {
    const authority = evaluateBodyReadAuthority(loadBodyReadAuthorityInputs({
      repoRoot: SYZYGY_ROOT,
      governanceRevision: syzygyRevision(),
      evaluationId: 'evaluation:pwb-discovery-live-ec8b1f6',
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
    expect(observation.manifest.pillars.find((pillar) => pillar.key === 'spec-and-spine')).toMatchObject({ reason: 'index-missing-at-revision', indexPath: 'openspec/README.md' });
    expect(observation.manifest.pillars.map((pillar) => [pillar.key, pillar.state, pillar.root])).toEqual([
      ['heart-and-soul', 'discovered', 'about/heart-and-soul'],
      ['legends-and-lore', 'discovered', 'about/legends-and-lore'],
      // `openspec/` carries no README index at this revision (index-missing-at-revision).
      ['spec-and-spine', 'unknown', 'openspec'],
      // Discovered again at this head: the index no longer carries the active
      // content that excluded it at a3dd1fe.
      ['lay-and-land', 'discovered', 'about/lay-and-land'],
      ['craft-and-care', 'discovered', 'about/craft-and-care'],
    ]);
    expect({
      total: observation.sources.length,
      about: observation.sources.filter((source) => source.path.startsWith('about/')).length,
      baseline: observation.sources.filter((source) => /^openspec\/specs\/[^/]+\/spec\.md$/.test(source.path)).length,
      roster: observation.sources.filter((source) => /^roster\/[^/]+\/(?:butler\.toml|MANIFESTO\.md)$/.test(source.path)).length,
    }).toEqual({ total: 270, about: 59, baseline: 185, roster: 26 });
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
    expect(shape.counts.sources).toBe(270);
    expect(shape.counts.classification.classifiedByBasis).toEqual({ body: 74, 'path-only': 185 });
    expect(shape.counts.sourcesWithKnownItemDenominator).toBe(259);
    expect(shape.items.filter((item) => item.class === 'baseline-spec')).toHaveLength(185);
    expect(shape.classes['baseline-spec'].denominator).toEqual({ kind: 'known', value: 185 });
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
