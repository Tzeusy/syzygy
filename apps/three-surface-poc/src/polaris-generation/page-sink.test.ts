import { beforeAll, describe, expect, it } from 'vitest';
import { pageSinkCspFinding, type GenerationSource, type PipelineResult, type ProviderDraft } from '@syzygy/polaris-generation-core';
import { renderDossier } from './dossier-render.js';
import { renderDraftPreview } from './draft-preview.js';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';
import { syntheticGenerationSource } from './synthetic-source.js';

// syzygy-wsev / P-105 (owner act of 2026-10-08): the version-3 screening scope exempts a listed code-content body from the
// active-content scan only while every page that writes it meets the scope's renderCondition. This app's page sinks are the
// dossier renderer and the draft preview (public-source-screening.ts names this file); a canary body carrying markup, the
// `a<b && c>d` form the exemption exists for, and both quote kinds must leave each one entity-encoded, and every page must
// pass the policy half (`pageSinkCspFinding`).

const CANARY = 'int f(int a, int b, int c, int d) { return a<b && c>d; } /* <script>alert("x")</script> \'q\' */';
const ENCODED = 'int f(int a, int b, int c, int d) { return a&lt;b &amp;&amp; c&gt;d; } /* &lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt; &#39;q&#39; */';
const RAW_FRAGMENTS = ['<script>', 'a<b && c>d', 'alert("x")'];

type Success = Extract<PipelineResult, { status: 'awaiting-rendered-review' }>;
let run: { sources: readonly GenerationSource[]; result: Success };
let canarySources: GenerationSource[];
beforeAll(async () => {
  const synthetic = await runSyntheticProject(syntheticProjects[0]!);
  if (synthetic.result.status !== 'awaiting-rendered-review') throw new Error('synthetic pipeline stopped');
  run = { sources: synthetic.sources, result: synthetic.result };
  const revision = 'c'.repeat(40);
  canarySources = run.sources.map(source => syntheticGenerationSource('canary', revision, source.sourceId, CANARY));
});

describe('page sinks under the version-3 renderCondition', () => {
  it('the dossier renderer writes the canary body entity-encoded, never raw, on every page under the policy CSP', () => {
    expect(renderDossier.pageSinkContract).toBe('polaris/page-sink/escaped-text-under-csp/1');
    const { files } = renderDossier({ result: run.result, sources: canarySources });
    const pages = [...files.entries()].filter(([path]) => path.endsWith('.html'));
    expect(pages.length).toBeGreaterThan(0);
    expect(pages.some(([, html]) => html.includes(ENCODED))).toBe(true);
    for (const [path, html] of pages) {
      expect(pageSinkCspFinding(html), path).toBeNull();
      for (const fragment of RAW_FRAGMENTS) expect(html.includes(fragment), `${path}: ${fragment}`).toBe(false);
    }
  });

  it('the draft preview writes the canary body entity-encoded, never raw, under the policy CSP', () => {
    const html = renderDraftPreview(run.result.draft as ProviderDraft, canarySources);
    expect(html).toContain(ENCODED);
    expect(pageSinkCspFinding(html)).toBeNull();
    for (const fragment of RAW_FRAGMENTS) expect(html.includes(fragment), fragment).toBe(false);
  });
});
