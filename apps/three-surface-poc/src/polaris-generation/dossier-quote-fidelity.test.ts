import { beforeAll, describe, expect, it } from 'vitest';

import { evaluateDossier, generationAnchorId, parseDossierManifest, segmentBody, type GenerationSource, type PipelineResult } from '@syzygy/polaris-generation-core';

import { renderDossier } from './dossier-render.js';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';

type Success = Extract<PipelineResult, { status: 'awaiting-rendered-review' }>;
let run: { sources: readonly GenerationSource[]; result: Success };
beforeAll(async () => {
  const synthetic = await runSyntheticProject(syntheticProjects[0]!);
  if (synthetic.result.status !== 'awaiting-rendered-review') throw new Error('synthetic pipeline stopped');
  run = { sources: synthetic.sources, result: synthetic.result };
});

const signal = new AbortController().signal;
const QUESTIONS = JSON.stringify({ format: 'polaris-reader-questions-v1', questions: [{ id: 'q1', topics: ['mechanisms'], text: 'How do the pieces connect?' }] });
type Intro = { text: string; sourceIds: string[] };
const evaluateWithIntro = async (text: (cited: string) => string) => {
  const draft = structuredClone(run.result.draft) as { introduction: Intro };
  const cited = run.sources.find(source => source.sourceId === draft.introduction.sourceIds[0])!.spans[0]!.text;
  draft.introduction.text = text(cited);
  const { files } = renderDossier({ sources: run.sources, result: { ...run.result, draft } });
  const manifest = parseDossierManifest(files.get('dossier.json')!);
  return evaluateDossier({ manifestText: files.get('dossier.json')!, pages: new Map(manifest.pages.map(page => [page.path, new TextEncoder().encode(files.get(page.path)!)])), sources: run.sources, questionsText: QUESTIONS }, signal);
};

describe('quotation marks inside a cited block (deterministic fidelity)', () => {
  it('reports every cited block as verbatim when the page quotes nothing, and when it quotes its source', async () => {
    const plain = await evaluateWithIntro(() => 'A plain sentence with no quotation marks.');
    expect(plain.fidelity.inBlockQuotes).toMatchObject({ failures: [], quotesChecked: 0, outcome: 'no-quotes' });
    expect(plain.fidelity.inBlockQuotes.denominator).toBeGreaterThan(3);
    const quoted = await evaluateWithIntro(cited => `The project's sources state: "${cited.slice(0, 30).replace(/"/gu, '')}"`);
    expect(quoted.fidelity.inBlockQuotes).toMatchObject({ failures: [], quotesChecked: 1, outcome: 'all-verbatim' });
  });

  it('reports a quotation absent from the cited source as a failure on that claim, never silently', async () => {
    const report = await evaluateWithIntro(() => 'The project\'s sources state: "words no source contains anywhere"');
    expect(report.fidelity.inBlockQuotes.outcome).toBe('failures');
    expect(report.fidelity.inBlockQuotes.failures).toEqual([{ page: 'index.html', claimId: 'opening', kind: 'quote-not-in-cited-sources', quote: 'words no source contains anywhere' }]);
  });

  it('reports a lead-in with no quotation, an unterminated one, and a different cited source holding the text', async () => {
    const lead = await evaluateWithIntro(() => 'The project\'s sources state: that it is fast.');
    expect(lead.fidelity.inBlockQuotes.failures.map(f => f.kind)).toEqual(['lead-in-without-quote']);
    const open = await evaluateWithIntro(() => 'The text says "never closed');
    expect(open.fidelity.inBlockQuotes.failures.map(f => f.kind)).toEqual(['unterminated-quote']);
    const other = run.sources.find(source => source.sourceId !== (run.result.draft as { introduction: Intro }).introduction.sourceIds[0])!.spans[0]!.text;
    const wrongSource = await evaluateWithIntro(() => `"${other.slice(0, 25).replace(/"/gu, '')}"`);
    expect(wrongSource.fidelity.inBlockQuotes.failures.map(f => f.kind)).toEqual(['quote-not-in-cited-sources']);
  });
  it('checks only claims that name a source: an unresolved question may carry quotation marks, and a page with no cited claim is unknown, not verbatim', async () => {
    const draft = structuredClone(run.result.draft) as { unresolved: unknown[] };
    draft.unresolved.push({ question: 'What does "the spec" mean here?', reason: 'Not stated.', references: [run.sources[0]!.sourceId] });
    const { files } = renderDossier({ sources: run.sources, result: { ...run.result, draft } });
    expect(files.get('index.html')).toContain('What does &quot;the spec&quot; mean here?');
    const manifest = parseDossierManifest(files.get('dossier.json')!);
    const evaluate = (transform: (html: string) => string) => evaluateDossier({ manifestText: files.get('dossier.json')!,
      pages: new Map(manifest.pages.map(page => [page.path, new TextEncoder().encode(transform(files.get(page.path)!))])), sources: run.sources, questionsText: QUESTIONS }, signal);
    expect((await evaluate(html => html)).fidelity.inBlockQuotes).toMatchObject({ failures: [], quotesChecked: 0, outcome: 'no-quotes' });
    const uncited = await evaluate(html => html.replaceAll('aria-label="Read source', 'aria-label="Source'));
    expect(uncited.fidelity.inBlockQuotes).toEqual({ denominator: 0, quotesChecked: 0, failures: [], outcome: 'unknown' });
  });

  it('renders a misquoting block as Unknown with the reason even though the reviewer called it supported', () => {
    const draft = structuredClone(run.result.draft) as { introduction: Intro };
    draft.introduction.text = 'The project\'s sources state: "words no source contains anywhere"';
    const supported = (run.result.review as { blockSupport: { blockId: string; verdict: string }[] }).blockSupport.find(row => row.blockId === 'opening');
    expect(supported?.verdict).toBe('supported');
    const html = renderDossier({ sources: run.sources, result: { ...run.result, draft, quoteFindings: [{ blockId: 'opening', kind: 'quote-not-in-cited-sources', quote: 'words no source contains anywhere' }] } }).files.get('index.html')!;
    const opening = html.match(/<p data-claim-id="opening"[^>]*>/u)![0];
    expect(opening).toContain('data-epistemic="unknown"');
    expect(html).toContain('Quotation not verified against the cited sources (quote-not-in-cited-sources).');
    const untouched = html.match(/data-claim-id="(?!opening")[^"]*" data-epistemic="inferred"/u);
    expect(untouched).not.toBeNull();
  });

  it('flags the same block when the result carries no record of the finding, by checking the draft itself', () => {
    const draft = structuredClone(run.result.draft) as { introduction: Intro };
    draft.introduction.text = 'The project\'s sources state: "words no source contains anywhere"';
    const html = renderDossier({ sources: run.sources, result: { ...run.result, draft, quoteFindings: [] } }).files.get('index.html')!;
    expect(html.match(/<p data-claim-id="opening"[^>]*>/u)![0]).toContain('data-epistemic="unknown"');
  });

  it('leaves a verbatim block as the reviewer judged it', () => {
    const html = renderDossier({ sources: run.sources, result: run.result }).files.get('index.html')!;
    expect(html.match(/<p data-claim-id="opening"[^>]*>/u)![0]).toContain('data-epistemic="inferred"');
    expect(html).not.toContain('Quotation not verified');
  });

  it('honours a recorded finding on a block the fresh check would not flag', () => {
    const html = renderDossier({ sources: run.sources, result: { ...run.result, quoteFindings: [{ blockId: 'opening', kind: 'quote-not-in-cited-sources', quote: 'recorded by the pipeline' }] } }).files.get('index.html')!;
    expect(html.match(/<p data-claim-id="opening"[^>]*>/u)![0]).toContain('data-epistemic="unknown"');
    expect(html).toContain('Quotation not verified against the cited sources');
  });

  it('evaluates a quotation that crosses a piece boundary of a split source against the whole file', async () => {
    const draft = structuredClone(run.result.draft) as { introduction: Intro };
    const id = draft.introduction.sourceIds[0]!;
    const original = run.sources.find(source => source.sourceId === id)!;
    const body = original.spans[0]!.text;
    const cut = segmentBody(body, Math.floor(body.length / 2));
    expect(cut.length).toBeGreaterThan(1);
    const crossing = body.slice(cut[0]!.text.length - 12, cut[0]!.text.length + 12).replace(/\s+/gu, ' ').trim().split(' ').slice(1, -1).join(' ');
    expect(crossing.length).toBeGreaterThan(3);
    draft.introduction.text = `The project's sources state: "${crossing.replace(/"/gu, '')}"`;
    const { files } = renderDossier({ sources: run.sources, result: { ...run.result, draft } });
    const pieces = cut.map((piece, index) => ({ ...original, sourceId: `${id}-p${index + 1}`, body: piece.text,
      segment: { index, count: cut.length, start: piece.start, end: piece.end, blobBytes: Buffer.byteLength(body) },
      spans: [{ anchorId: generationAnchorId(original, piece.start, piece.end), start: 0, end: piece.end - piece.start, text: piece.text }] }));
    const sources = [...run.sources.filter(source => source.sourceId !== id), ...pieces];
    const manifest = parseDossierManifest(files.get('dossier.json')!);
    const pages = new Map(manifest.pages.map(page => [page.path, new TextEncoder().encode(files.get(page.path)!.replaceAll(`Read source ${id}"`, `Read source ${id}-p1"`))]));
    const report = await evaluateDossier({ manifestText: files.get('dossier.json')!, pages, sources, questionsText: QUESTIONS }, signal);
    expect(report.fidelity.inBlockQuotes).toMatchObject({ failures: [], outcome: 'all-verbatim' });
  });
});
