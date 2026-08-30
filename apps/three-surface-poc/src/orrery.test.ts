import { rmSync } from 'node:fs';
import { afterEach, describe, expect, it } from 'vitest';

import { buildButlersPocModel } from '@syzygy/three-surface-poc-core';

import { renderOrreryPage } from './orrery.js';
import { buildFixtureModel, fixtureRepoWithGit } from './test-model-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function anchorIds(html: string): Set<string> {
  return new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1] as string));
}

describe('Orrery', () => {
  it('reconciles declared mapped and unmapped counts against the observed total (POC-REQ-051)', () => {
    const model = buildFixtureModel(cleanups);
    if (model.orrery.kind !== 'observed') throw new Error('unreachable');
    const html = renderOrreryPage(model);

    const scopeText = /data-parity-field="orrery-scope">([\s\S]*?)<\/p>/.exec(html)?.[1] ?? '';
    expect(scopeText).toContain(String(model.orrery.mappedFileCount));
    expect(scopeText).toContain(String(model.orrery.totalFileCount));
    const unmappedMatch = /data-parity-field="orrery-unmapped-count">(\d+)</.exec(html);
    expect(Number(unmappedMatch?.[1])).toBe(model.orrery.unmappedFileCount);
    expect(model.orrery.mappedFileCount + model.orrery.unmappedFileCount).toBe(
      model.orrery.totalFileCount,
    );
  });

  it('every entity-backed spatial region resolves to the same route the exact tables serve (POC-REQ-053)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderOrreryPage(model);
    const ids = anchorIds(html);

    // the JSON data island is the client's only source of entity ids; every
    // one of them must resolve against the exact-table anchors on this page
    const islandMatch = /<script type="application\/json" id="orrery-data">([\s\S]*?)<\/script>/.exec(
      html,
    );
    expect(islandMatch).not.toBeNull();
    const island = JSON.parse(islandMatch?.[1] ?? '{}') as {
      mappedRegions: readonly { id: string }[];
      unmappedRegionEntityId: string;
      unmappedFileCount: number;
    };
    let resolved = 0;
    const denominator = island.mappedRegions.length + (island.unmappedFileCount > 0 ? 1 : 0);
    for (const region of island.mappedRegions) {
      if (ids.has(region.id)) resolved += 1;
    }
    if (island.unmappedFileCount > 0 && ids.has(island.unmappedRegionEntityId)) {
      resolved += 1;
    }
    expect(resolved).toBe(denominator);
  });

  it('embeds the same facts the machine answer serves (POC-REQ-020 parity by construction)', () => {
    const model = buildFixtureModel(cleanups);
    if (model.orrery.kind !== 'observed') throw new Error('unreachable');
    const html = renderOrreryPage(model);
    const islandMatch = /<script type="application\/json" id="orrery-data">([\s\S]*?)<\/script>/.exec(
      html,
    );
    const island = JSON.parse(islandMatch?.[1] ?? '{}') as {
      mappedFileCount: number;
      unmappedFileCount: number;
      totalFileCount: number;
      revision: string;
    };
    expect(island.mappedFileCount).toBe(model.orrery.mappedFileCount);
    expect(island.unmappedFileCount).toBe(model.orrery.unmappedFileCount);
    expect(island.totalFileCount).toBe(model.orrery.totalFileCount);
    expect(island.revision).toBe(model.orrery.revision);
  });

  it('provides a no-script backstop and never a blank region (POC-REQ-022)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderOrreryPage(model);
    expect(html).toContain('<noscript>');
    expect(html).toContain('requires JavaScript');
    // the always-present exact tables are the no-script honest facts
    expect(html).toContain('id="entities"');
    expect(html).toContain('id="relationships"');
  });

  it('explains the block-height encoding with an on-page legend (C3-3)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderOrreryPage(model);
    expect(html).toContain(
      "District block height is proportional to the directory's total size in bytes",
    );
  });

  it('renders Unknown with a reason, never an empty-but-green map, when code structure fails (POC-REQ-003 rendering)', () => {
    const { repoRoot, revision } = fixtureRepoWithGit(cleanups);
    const model = buildButlersPocModel({
      repoRoot,
      repositoryRevision: '0000000000000000000000000000000000dead',
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@unreadable', asOf: '2026-08-30T12:00:00Z' },
    });
    expect(model.orrery.kind).toBe('unknown');
    const html = renderOrreryPage(model);
    expect(html).toContain('data-unknown-disclosure="region:code-structure"');
    expect(html).not.toContain('id="orrery-canvas"');
  });

  it('two renders of one observation produce identical layout-relevant data (POC-REQ-050)', () => {
    const model = buildFixtureModel(cleanups);
    const first = renderOrreryPage(model);
    const second = renderOrreryPage(model);
    expect(second).toBe(first);
  });
});
