import { execFileSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, beforeAll, describe, expect, it } from 'vitest';

import {
  evaluateDossier, generationAnchorId, parseDossierManifest, scanDossierPage,
  type GenerationSource, type PipelineResult,
} from '@syzygy/polaris-generation-core';
import { renderDossier, sourceRoute } from './dossier-render.js';
import { writeDossierRun } from './dossier-render-main.js';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';

type Success = Extract<PipelineResult, { status: 'awaiting-rendered-review' }>;
let run: { sources: readonly GenerationSource[]; result: Success };
beforeAll(async () => {
  const synthetic = await runSyntheticProject(syntheticProjects[0]!);
  if (synthetic.result.status !== 'awaiting-rendered-review') throw new Error('synthetic pipeline stopped');
  run = { sources: synthetic.sources, result: synthetic.result };
});

const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });

const CSP = `<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">`;
const signal = new AbortController().signal;
const QUESTIONS = JSON.stringify({ format: 'polaris-reader-questions-v1', questions: [{ id: 'q1', topics: ['mechanisms'], text: 'How do the pieces connect?' }] });
const evaluate = (files: ReadonlyMap<string, string>, sources: readonly GenerationSource[]) => {
  const manifest = parseDossierManifest(files.get('dossier.json')!);
  return evaluateDossier({
    manifestText: files.get('dossier.json')!,
    pages: new Map(manifest.pages.map(page => [page.path, new TextEncoder().encode(files.get(page.path)!)])),
    sources, questionsText: QUESTIONS,
  }, signal);
};
const withReview = (mutate: (review: { blockSupport: { blockId: string; verdict: string }[] }) => void): Success => {
  const review = structuredClone(run.result.review) as { blockSupport: { blockId: string; verdict: string }[] };
  mutate(review);
  return { ...run.result, review };
};

describe('multi-page dossier render', () => {
  it('round-trips through the evaluation harness with every quote exact and every claim labelled', async () => {
    const { files } = renderDossier(run);
    const report = await evaluate(files, run.sources);
    expect(report.fidelity.quotes).toMatchObject({ denominator: 3, exact: 3, failures: [], outcome: 'all-resolved' });
    // opening, mechanism-text, mechanism-detail-0, qualification-text, depth-text (Inferred);
    // diagram nodes left and right and edge connection keep their Observed marking.
    expect(report.fidelity.claims).toMatchObject({ denominator: 8, labelled: 8, byLabel: { observed: 3, inferred: 5, unknown: 0 }, duplicateClaimIds: [], outcome: 'all-resolved' });
    expect(report.scanFindings).toEqual([]);
  });

  it('writes the entry, deep-dive, contents, glossary and per-source pages, each under the preview CSP and script-free', () => {
    const { files, manifest } = renderDossier(run);
    expect(manifest.pages.map(page => [page.path, page.depth]).filter(([path]) => !String(path).startsWith('sources/') || path === 'sources/index.html')).toEqual([
      ['index.html', 0], ['deep-dives/component-depth.html', 1], ['contents.html', 1], ['glossary.html', 1], ['sources/index.html', 1],
    ]);
    expect(manifest.pages.filter(page => page.path !== 'sources/index.html' && page.path.startsWith('sources/')).map(page => page.depth)).toEqual([2, 2, 2]);
    expect([...files.keys()].sort()).toEqual([...manifest.pages.map(page => page.path), 'dossier.json', 'size-report.json'].sort());
    for (const page of manifest.pages) {
      const html = files.get(page.path)!;
      expect(html.split(CSP)).toHaveLength(2);
      expect(html).not.toMatch(/<script|\son[a-z]+=|javascript:/iu);
    }
  });

  it('resolves every internal link to a written page and an id on it', () => {
    const { files, manifest } = renderDossier(run);
    const ids = new Map(manifest.pages.map(page => [page.path, scanDossierPage(files.get(page.path)!).ids]));
    let links = 0;
    for (const page of manifest.pages) {
      for (const [, raw] of files.get(page.path)!.matchAll(/href="([^"]*)"/gu)) {
        links++;
        const [target, fragment] = raw!.split('#');
        const resolved = target === '' ? page.path : new URL(target!, `file:///run/${page.path}`).pathname.slice('/run/'.length);
        expect(ids.has(resolved), `${page.path} -> ${raw}`).toBe(true);
        if (fragment !== undefined) expect(ids.get(resolved)!.has(fragment), `${page.path} -> ${raw}`).toBe(true);
      }
    }
    expect(links).toBeGreaterThan(40);
  });

  it('labels a block the review did not judge supported as Unknown', async () => {
    const result = withReview(review => { review.blockSupport.find(row => row.blockId === 'qualification-text')!.verdict = 'unresolved'; });
    const { files } = renderDossier({ result, sources: run.sources });
    expect(files.get('index.html')).toContain('data-claim-id="qualification-text" data-epistemic="unknown"');
    expect((await evaluate(files, run.sources)).fidelity.claims.byLabel).toEqual({ observed: 3, inferred: 4, unknown: 1 });
  });

  it('renders inventory terms as Inferred glossary claims and an empty glossary as such', async () => {
    const empty = renderDossier(run).files.get('glossary.html')!;
    expect(empty).toContain('The inventory recorded no terms, so this glossary is empty.');
    const inventory = structuredClone(run.result.inventory) as { entries: object[] };
    inventory.entries.push({ id: 'seasonal-plan', kind: 'term', statement: 'The plan that turns observations into tasks.', sourceIds: ['mechanism'], disposition: { kind: 'produced', assetIds: [] } });
    const { files } = renderDossier({ result: { ...run.result, inventory }, sources: run.sources });
    expect(files.get('glossary.html')).toContain('data-claim-id="glossary:seasonal-plan" data-epistemic="inferred"');
    const report = await evaluate(files, run.sources);
    expect(report.fidelity.claims.denominator).toBe(9);
    expect(report.fidelity.claims.outcome).toBe('all-resolved');
  });

  it('declares owner topics only where the run profile maps them, and refuses an unknown topic', async () => {
    const { files } = renderDossier({ ...run, topics: { how: ['mechanisms'], judgment: ['trade-offs'], 'component-depth': ['mechanisms'] } });
    const coverage = (await evaluate(files, run.sources)).coverage;
    expect(coverage.map(row => [row.topic, row.status])).toEqual([
      ['core-ideas', 'unknown'], ['end-to-end-workflows', 'unknown'], ['mechanisms', 'declared-only'],
      ['maintainer-stated-advantages', 'unknown'], ['trade-offs', 'declared-only'],
    ]);
    expect(coverage[2]!.declaredBy).toEqual([{ page: 'index.html', sectionId: 'section-how' }, { page: 'deep-dives/component-depth.html', sectionId: 'deep-dive-component-depth' }]);
    expect(() => renderDossier({ ...run, topics: { how: ['marketing' as never] } })).toThrow('unknown-topic');
  });

  it('refuses a stopped run and a citation of a source with no admitted text', () => {
    expect(() => renderDossier({ result: { status: 'stopped', reason: 'cancelled', receipts: [], artifacts: [] }, sources: run.sources })).toThrow('not-renderable');
    const { body: _body, ...rest } = run.sources[0]!;
    const pathOnly: GenerationSource = { ...rest, classificationBasis: 'path-only', spans: [] };
    expect(() => renderDossier({ result: run.result, sources: [pathOnly, ...run.sources.slice(1)] })).toThrow('unquotable-source');
  });

  it('writes the size report from the rendered bytes', () => {
    const { files } = renderDossier(run);
    const report = JSON.parse(files.get('size-report.json')!);
    expect(report.format).toBe('polaris-dossier-size-report-v1');
    expect(report.firstReadingLevel.page).toBe('index.html');
    expect(report.firstReadingLevel.entryPageBytes).toBe(Buffer.byteLength(files.get('index.html')!));
    expect(report.firstReadingLevel.words).toBeGreaterThan(0);
    expect(report.totalBudget).toEqual({ outcome: 'unknown', reason: 'no-budget-declared' });
  });
});

describe('source routes', () => {
  const blob = { repositoryId: 'project:kv', revision: 'c'.repeat(40), path: 'src/big.c', objectId: 'd'.repeat(40) };
  const piece = (start: number, end: number) => ({ spans: [{ anchorId: generationAnchorId(blob, start, end), start: 0, end: end - start, text: 'x'.repeat(end - start) }] });

  it('gives two pieces of one blob two routes, though they share a source identity', () => {
    const first = sourceRoute(piece(0, 100));
    const second = sourceRoute(piece(100, 180));
    expect(first).not.toBe(second);
    expect(first).toMatch(/^sources\/[0-9a-f]{24}\.html$/u);
  });

  it('keeps a route stable under reordering and moves it when the bytes change', () => {
    const before = run.sources.map(sourceRoute);
    const reordered = renderDossier({ ...run, sources: [...run.sources].reverse() }).manifest.pages.map(page => page.path).filter(path => path !== 'sources/index.html' && path.startsWith('sources/'));
    expect(new Set(reordered)).toEqual(new Set(before));
    expect(new Set(before).size).toBe(run.sources.length);
    expect(sourceRoute(piece(0, 101))).not.toBe(sourceRoute(piece(0, 100)));
  });
});

describe('run directory', () => {
  it('writes every file into a new directory outside Git and refuses to reuse one', async () => {
    const parent = mkdtempSync(join(tmpdir(), 'syzygy-dossier-run-'));
    cleanups.push(parent);
    const { files } = renderDossier(run);
    const out = join(parent, 'garden');
    await writeDossierRun(out, files);
    for (const [path, content] of files) expect(readFileSync(join(out, path), 'utf8')).toBe(content);
    await expect(writeDossierRun(out, files)).rejects.toThrow();
  });

  it('refuses a run directory inside a Git work tree', async () => {
    const parent = mkdtempSync(join(tmpdir(), 'syzygy-dossier-git-'));
    cleanups.push(parent);
    execFileSync('git', ['init', '-q', parent]);
    await expect(writeDossierRun(join(parent, 'run'), renderDossier(run).files)).rejects.toThrow('run-directory-inside-git-work-tree');
    expect(existsSync(join(parent, 'run'))).toBe(false);
  });
});
