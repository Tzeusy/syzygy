import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

import type { OwnerTopic, PipelineResult } from '@syzygy/polaris-generation-core';
import { renderDossier, type DossierRenderInput } from './dossier-render.js';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';

/**
 * The provider mode's rendered bytes, pinned. The operator-agent inputs
 * (`local`, syzygy-qkea.10) were added to `renderDossier` as an optional
 * field; this test holds every provider-mode file of every fixture run
 * byte-identical to the output captured before that change. The golden file
 * holds the sha256 of each file; the capture ran on the renderer as it stood
 * at commit 182d2688 (`SYZYGY_CAPTURE_PROVIDER_GOLDEN=1` rewrites it, and
 * only an intended provider-mode change may).
 */

const GOLDEN = new URL('./dossier-render-provider-golden.json', import.meta.url);
const sha256 = (text: string): string => createHash('sha256').update(text).digest('hex');

async function cases(): Promise<[string, DossierRenderInput][]> {
  const out: [string, DossierRenderInput][] = [];
  for (const project of syntheticProjects) {
    const complete = await runSyntheticProject(project);
    out.push([`${project.id}/complete`, { result: complete.result, sources: complete.sources }]);
    const topics: Record<string, OwnerTopic[]> = { how: ['mechanisms'], judgment: ['trade-offs'], 'component-depth': ['mechanisms'] };
    out.push([`${project.id}/topics`, { result: complete.result, sources: complete.sources, topics }]);
    for (const budget of [{ maxCalls: 1 }, { maxCalls: 2 }, { maxCalls: 4 }, { maxUsageUnits: 7 }]) {
      const stopped = await runSyntheticProject(project, budget);
      out.push([`${project.id}/stopped-${JSON.stringify(budget)}`, { result: stopped.result as PipelineResult, sources: stopped.sources, requestedAssets: stopped.requestedAssets }]);
    }
  }
  return out;
}

describe('provider-mode render output is unchanged by the operator-agent inputs', () => {
  it('renders every fixture run to the captured bytes, file by file', async () => {
    const rendered: Record<string, Record<string, string>> = {};
    for (const [name, input] of await cases()) {
      rendered[name] = Object.fromEntries([...renderDossier(input).files].map(([path, text]) => [path, sha256(text)]));
    }
    if (process.env['SYZYGY_CAPTURE_PROVIDER_GOLDEN'] === '1') writeFileSync(GOLDEN, `${JSON.stringify(rendered, null, 2)}\n`);
    const golden = JSON.parse(readFileSync(GOLDEN, 'utf8')) as Record<string, Record<string, string>>;
    expect(Object.keys(golden).length).toBe(syntheticProjects.length * 6);
    expect(rendered).toEqual(golden);
  });
});
