import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import type { ProviderDraft } from '@syzygy/polaris-generation-core';

import { renderDraftPreview } from './draft-preview.js';
import { renderDossierSite, writeDossierSite } from './dossier-site.js';
import { syntheticGenerationSource } from './synthetic-source.js';

const revision = 'a'.repeat(40);
const sources = [syntheticGenerationSource('site', revision, 'purpose', 'Reduce recurring mental work.'),
  syntheticGenerationSource('site', revision, 'architecture', 'Planner schedules events in the calendar. <script>alert(1)</script>'),
  syntheticGenerationSource('site', revision, 'unused', 'Never cited & <b>raw</b>.')];
const para = (id: string, text: string, sourceIds: string[]) => ({ id, text, sourceIds, children: [] });
function fixture(): ProviderDraft {
  return {
    title: 'A quieter everyday', introduction: { id: 'intro', text: 'Let recurring work take care of itself.', sourceIds: ['purpose'] },
    sections: [
      { id: 'architecture', title: 'How the pieces connect', paragraphs: [{ ...para('overview', 'Requests reach the planner, then the calendar.', ['architecture']), children: [para('overview-mechanism', 'The planner schedules an event.', ['architecture'])] }], disposition: { kind: 'produced', assetIds: ['architecture'] } },
      { id: 'tradeoffs', title: 'What it gives up', paragraphs: [para('give-up', 'It does not plan across calendars.', ['purpose'])], disposition: { kind: 'produced', assetIds: ['tradeoffs'] } },
      { id: 'missing', title: 'Unsupported material', paragraphs: [], disposition: { kind: 'unresolved', reason: 'No source supports this.', references: ['purpose'] } },
    ],
    diagrams: [{ id: 'flow', title: 'From request to calendar', sectionId: 'architecture', kind: 'flow', relationship: 'How a request becomes an event',
      nodes: [{ id: 'planner', label: 'Planner', sourceIds: ['architecture'], epistemic: 'observed' }, { id: 'calendar', label: 'Calendar', sourceIds: ['architecture'], epistemic: 'inferred' }],
      edges: [{ id: 'schedules', from: 'planner', to: 'calendar', label: 'Schedules an event', sourceIds: ['architecture'], epistemic: 'observed' }], disposition: { kind: 'produced', assetIds: ['flow'] } }],
    deepDives: [{ id: 'calendar-detail', title: 'Inside the calendar', sectionId: 'architecture', paragraphs: [para('detail', 'The calendar records events.', ['architecture'])], disposition: { kind: 'produced', assetIds: ['calendar-detail'] } }],
    unresolved: [{ question: 'Who is it for?', reason: 'No audience was declared.', references: ['purpose'] }],
  };
}
const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });
const page = (site: ReturnType<typeof renderDossierSite>, path: string): string => site.pages.find(p => p.path === path)!.content;

describe('multi-page dossier site', () => {
  const site = renderDossierSite(fixture(), sources);

  it('emits an entry page, a page per section and deep dive, glossary, sources and size report', () => {
    expect(site.pages.map(p => p.path).filter(p => !p.startsWith('source-'))).toEqual(['index.html', 'section-01-how-the-pieces-connect.html', 'section-02-what-it-gives-up.html',
      'section-03-unsupported-material.html', 'deep-dive-01-inside-the-calendar.html', 'glossary.html', 'sources.html', 'size-report.html', 'size-report.json']);
    expect(site.pages.filter(p => p.kind === 'source')).toHaveLength(2);
  });

  it('puts each section answer on the entry page and the full section, diagram and deep-dive link on its page', () => {
    const entry = page(site, 'index.html');
    expect(entry).toContain('Requests reach the planner, then the calendar.');
    expect(entry).not.toContain('The planner schedules an event.');
    expect(entry).toContain('href="section-01-how-the-pieces-connect.html"');
    expect(entry).toContain('Who is it for?');
    const section = page(site, 'section-01-how-the-pieces-connect.html');
    expect(section).toContain('The planner schedules an event.');
    expect(section).toContain('marker-end="url(#arrow-0)"');
    expect(section).toContain('href="deep-dive-01-inside-the-calendar.html"');
    expect(page(site, 'deep-dive-01-inside-the-calendar.html')).toContain('>Return to the section</a>');
    expect(section).toContain('rel="next"');
    expect(section).not.toContain('rel="prev"');
    expect(page(site, 'section-02-what-it-gives-up.html')).toContain('rel="prev"');
    expect(page(site, 'section-03-unsupported-material.html')).toContain('No source supports this.');
  });

  it('links every citation to the exact cited text and lists uncited and unquotable sources honestly', () => {
    const hrefs = [...site.pages.filter(p => p.kind !== 'source').flatMap(p => [...p.content.matchAll(/class="sources"><a href="([^"]+)"/gu)].map(m => m[1]!))];
    expect(hrefs.length).toBeGreaterThan(5);
    const byFile = new Map(site.pages.map(p => [p.path, p.content]));
    for (const href of hrefs) {
      const [file, anchor] = href.split('#');
      expect(byFile.get(file!)).toContain(`id="${anchor}"`);
    }
    expect(page(site, 'sources.html')).toContain('quotable, not cited');
    expect(site.pages.some(p => p.content.includes('Never cited'))).toBe(false);
    expect(site.pages.filter(p => p.kind === 'source').map(p => p.content).join('')).toContain('Planner schedules events in the calendar. &lt;script&gt;alert(1)&lt;/script&gt;');
  });

  it('is a static site under the strict CSP: no script, no external reference, no unescaped source markup', () => {
    for (const p of site.pages.filter(x => x.path.endsWith('.html'))) {
      expect(p.content).toContain(`content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"`);
      expect(p.content).not.toMatch(/<script|<iframe|<link |<img |https?:\/\/(?!www\.w3\.org\/2000\/svg)/iu);
      for (const href of [...p.content.matchAll(/href="([^"#]+)/gu)].map(m => m[1]!)) expect(site.pages.map(x => x.path)).toContain(href);
    }
  });

  it('reports sizes that match the bytes and words of what it emitted, and counts the denominator', () => {
    const report = site.sizeReport;
    const counted = site.pages.filter(p => !p.path.startsWith('size-report'));
    expect(report.pages.map(p => p.path)).toEqual(counted.map(p => p.path));
    expect(report.totalBytes).toBe(counted.reduce((n, p) => n + Buffer.byteLength(p.content), 0));
    expect(report.firstLevel.bytes).toBe(Buffer.byteLength(page(site, 'index.html')));
    expect(report.firstLevel.words).toBeGreaterThan(10);
    expect(report.firstLevel.bytes).toBeLessThan(report.totalBytes);
    expect(report.counts).toEqual({ sections: 3, deepDives: 1, diagrams: 1, sourcesCounted: 3, sourcesCited: 2, sourcesNotCited: 1 });
    expect(JSON.parse(page(site, 'size-report.json')).totalBytes).toBe(report.totalBytes);
    expect(page(site, 'size-report.html')).toContain(`${report.totalBytes} bytes`);
  });

  it('builds a glossary from supplied definitions plus an index of diagram names, and never invents either', () => {
    const glossary = page(site, 'glossary.html');
    expect(glossary).toContain('No term definitions were produced');
    expect(glossary).toContain('Planner');
    expect(glossary).toContain('an index of names, not definitions');
    const defined = renderDossierSite(fixture(), sources, { glossary: [{ term: 'Planner', definition: 'Chooses when an event runs.', sourceIds: ['architecture'] }] });
    expect(page(defined, 'glossary.html')).toContain('Chooses when an event runs.');
    expect(() => renderDossierSite(fixture(), sources, { glossary: [{ term: 'X', definition: 'y', sourceIds: ['nope'] }] })).toThrow('unknown-source');
    const bare = fixture(); bare.diagrams = [];
    expect(page(renderDossierSite(bare, sources), 'glossary.html')).toContain('No glossary was produced');
  });

  it('keeps the single-page preview unchanged by sharing its renderers', () => {
    const html = renderDraftPreview(fixture(), sources);
    expect(html).toContain('Pipeline draft preview — not reviewed or adopted');
    expect(html).toContain('<div class="deep-dive" id="deep-dive-0"><details>');
  });

  it('renders nothing attached to a section that is itself unresolved', () => {
    const draft = fixture(); draft.diagrams[0]!.sectionId = 'missing';
    const odd = renderDossierSite(draft, sources);
    expect(page(odd, 'section-03-unsupported-material.html')).not.toContain('<svg');
    expect(odd.pages.some(p => p.content.includes('<svg'))).toBe(false);
    expect(page(odd, 'glossary.html')).toContain('No glossary was produced');
  });

  it('refuses a duplicate handle across pages and a deep dive of an unknown section', () => {
    const dup = fixture(); dup.deepDives[0]!.paragraphs[0]!.id = 'overview';
    expect(() => renderDossierSite(dup, sources)).toThrow('duplicate-draft-handle');
    const lost = fixture(); lost.deepDives[0]!.sectionId = 'nowhere';
    expect(() => renderDossierSite(lost, sources)).toThrow('unknown-section');
  });
});

describe('writing the run directory', () => {
  const site = renderDossierSite(fixture(), sources);
  const scratch = (): string => { const dir = mkdtempSync(join(tmpdir(), 'syzygy-dossier-run-')); cleanups.push(dir); return dir; };

  it('writes every page into a fresh directory outside git', () => {
    const dir = join(scratch(), 'run-1');
    expect(writeDossierSite(dir, site)).toMatchObject({ written: site.pages.length });
    expect(readdirSync(dir).sort()).toEqual(site.pages.map(p => p.path).sort());
    expect(readFileSync(join(dir, 'index.html'), 'utf8')).toBe(site.pages[0]!.content);
  });

  it('refuses a directory inside a git work tree, a non-empty directory and an unsafe page name', () => {
    const repo = scratch();
    execFileSync('git', ['init', '-q', repo]);
    expect(() => writeDossierSite(join(repo, 'out'), site)).toThrow('run-directory-inside-git-work-tree');
    expect(existsSync(join(repo, 'out'))).toBe(false);
    const full = scratch(); writeFileSync(join(full, 'keep.txt'), 'x');
    expect(() => writeDossierSite(full, site)).toThrow('run-directory-not-empty');
    const nested = join(scratch(), 'a'); mkdirSync(nested);
    expect(() => writeDossierSite(nested, { ...site, pages: [{ ...site.pages[0]!, path: '../escape.html' }] })).toThrow('unsafe-page-name');
    expect(() => writeDossierSite(nested, { ...site, pages: [site.pages[0]!, site.pages[0]!] })).toThrow('duplicate-page-name');
  });
});
