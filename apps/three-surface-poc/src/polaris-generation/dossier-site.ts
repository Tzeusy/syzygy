import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readdirSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';

import type { GenerationSource, ProviderDraft } from '@syzygy/polaris-generation-core';
import { DESIGN_TOKENS_CSS } from '../design-tokens.js';

import { createDraftParts, escapeHtml, PREVIEW_CSS, type DraftPreviewOptions } from './draft-preview.js';

/** A caller-supplied definition. The provider draft has no glossary field
 * yet, so nothing here is invented: with no entries the page says so. */
export interface GlossaryEntry { readonly term: string; readonly definition: string; readonly sourceIds: readonly string[] }
export interface DossierSiteOptions extends DraftPreviewOptions { readonly glossary?: readonly GlossaryEntry[] }

export interface SitePage {
  readonly path: string;
  readonly content: string;
  readonly kind: 'entry' | 'section' | 'deep-dive' | 'glossary' | 'sources' | 'source' | 'size-report' | 'size-report-data';
}
export interface PageSize { readonly path: string; readonly kind: SitePage['kind']; readonly bytes: number; readonly words: number; readonly sha256: string }
export interface SizeReport {
  readonly pages: readonly PageSize[];
  readonly totalBytes: number;
  readonly totalWords: number;
  /** What a reader loads before choosing where to go next. */
  readonly firstLevel: { readonly path: string; readonly bytes: number; readonly words: number };
  readonly largest: { readonly path: string; readonly bytes: number };
  readonly counts: { readonly sections: number; readonly deepDives: number; readonly diagrams: number; readonly sourcesCounted: number; readonly sourcesCited: number; readonly sourcesNotCited: number };
  readonly excludes: string;
}
export interface DossierSite { readonly pages: readonly SitePage[]; readonly sizeReport: SizeReport }

const CSP = "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'";
const EXTRA_CSS = '.site-nav{display:flex;flex-wrap:wrap;gap:.5rem 1.5rem;padding:.75rem 4vw;border-bottom:1px solid var(--line);font:.85rem var(--font-mono)}.site-nav a{text-decoration:none}.section-card{padding:1.5rem 0;border-top:1px solid var(--line)}.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:3rem;font:.9rem var(--font-mono)}table{border-collapse:collapse;font:.85rem var(--font-mono)}td,th{border:1px solid var(--line);padding:.35rem .7rem;text-align:left}dt{font-weight:700;margin-top:1rem}';
const sha256 = (value: string): string => createHash('sha256').update(value).digest('hex');
const slug = (title: string): string => title.toLowerCase().replace(/[^a-z0-9]+/gu, '-').replace(/^-+|-+$/gu, '').slice(0, 40) || 'untitled';
const two = (n: number): string => String(n + 1).padStart(2, '0');
const textOf = (html: string): string => html.replace(/<style[\s\S]*?<\/style>/gu, ' ').replace(/<[^>]+>/gu, ' ').replace(/&[a-z#0-9]+;/giu, ' ');
const wordCount = (html: string): number => textOf(html).split(/\s+/u).filter(Boolean).length;
const sourcePage = (sourceId: string): string => `source-${sourceId.replace(/[^A-Za-z0-9_.-]/gu, '_').toLowerCase()}-${sha256(sourceId).slice(0, 8)}.html`;

/** A multi-page static site: an entry page with the answer to each section,
 * a page per section and deep dive, a glossary, exact cited source text, and
 * a size report. Every page carries the same strict CSP and no script. */
export function renderDossierSite(draft: ProviderDraft, sources: readonly GenerationSource[], options: DossierSiteOptions = {}): DossierSite {
  const cited = new Map<string, GenerationSource>();
  let parts!: ReturnType<typeof createDraftParts>;
  parts = createDraftParts(draft, sources, (source, anchorId) => { cited.set(source.sourceId, source); return `${sourcePage(source.sourceId)}#${parts.localAnchor(anchorId)}`; }, options);
  const { paragraph, block, blockParts, diagram, refs, register, localAnchor } = parts;

  const sectionFile = draft.sections.map((s, i) => `section-${two(i)}-${slug(s.title)}.html`);
  const deepFile = draft.deepDives.map((d, i) => `deep-dive-${two(i)}-${slug(d.title)}.html`);
  const sectionIndex = new Map(draft.sections.map((s, i) => [s.id, i]));
  const introHtml = paragraph(draft.introduction);

  interface Rendered { blocks: string[]; leads: string[]; diagrams: string; deepLinks: string }
  const rendered = draft.sections.map((section, index): Rendered => {
    register(section.id);
    if (section.disposition.kind !== 'produced') return { blocks: [], leads: [], diagrams: '', deepLinks: '' };
    const split = section.paragraphs.map(blockParts);
    return { blocks: split.map(p => p.lead + p.children), leads: split.map(p => p.lead),
      diagrams: draft.diagrams.map((d, i) => d.sectionId === section.id ? diagram(d, i) : '').join(''),
      deepLinks: draft.deepDives.map((d, i) => d.sectionId === section.id
        ? `<p class="deep-dive"><a href="${deepFile[i]}">Explore: ${escapeHtml(d.title)}</a></p>` : '').join('') };
  });
  const sectionBody = (index: number): string => {
    const section = draft.sections[index]!;
    return section.disposition.kind === 'produced' ? '' : dispositionHtml(section.id, section.disposition);
  };
  const dispositionHtml = (id: string, disposition: Exclude<ProviderDraft['sections'][number]['disposition'], { kind: 'produced' }>): string =>
    `<aside class="unresolved-asset" data-asset-disposition="${disposition.kind}" id="unresolved-${escapeHtml(id)}"><strong>${escapeHtml(id)}</strong>: ${escapeHtml(disposition.reason)} <span class="asset-references">(${escapeHtml(disposition.references.join(', '))})</span></aside>`;
  const deepHtml = draft.deepDives.map((d) => {
    register(d.id);
    return d.disposition.kind !== 'produced' ? dispositionHtml(d.id, d.disposition) : d.paragraphs.map(block).join('');
  });

  const head = (title: string): string => `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="${CSP}"><title>${escapeHtml(title)} — dossier draft</title><style>${DESIGN_TOKENS_CSS}\n${PREVIEW_CSS}${EXTRA_CSS}\n</style></head><body>`;
  const siteNav = '<nav class="site-nav" aria-label="Dossier"><a href="index.html">Home</a><a href="index.html#contents">Contents</a><a href="glossary.html">Glossary</a><a href="sources.html">Sources</a><a href="size-report.html">Size report</a></nav>';
  const notice = '<div class="pipeline-notice">Pipeline draft — not reviewed or adopted</div>';
  const page = (title: string, body: string): string => `${head(title)}${notice}${siteNav}<div class="layout"><main>${body}</main></div></body></html>`;
  const pager = (index: number): string => `<div class="pager">${index > 0 ? `<a href="${sectionFile[index - 1]}" rel="prev">← ${escapeHtml(draft.sections[index - 1]!.title)}</a>` : '<span></span>'}${index < draft.sections.length - 1 ? `<a href="${sectionFile[index + 1]}" rel="next">${escapeHtml(draft.sections[index + 1]!.title)} →</a>` : '<span></span>'}</div>`;

  const pages: SitePage[] = [];
  const contentsList = `<ol><li><a href="index.html">Introduction</a></li>${draft.sections.map((s, i) => `<li><a href="${sectionFile[i]}">${escapeHtml(s.title)}</a>${draft.deepDives.some(d => d.sectionId === s.id) ? `<ul>${draft.deepDives.map((d, j) => d.sectionId === s.id ? `<li><a href="${deepFile[j]}">${escapeHtml(d.title)}</a></li>` : '').join('')}</ul>` : ''}</li>`).join('')}<li><a href="glossary.html">Glossary</a></li><li><a href="sources.html">Sources</a></li><li><a href="size-report.html">Size report</a></li></ol>`;
  const unresolved = draft.unresolved.map(item => `<aside class="unresolved-asset" data-asset-disposition="unresolved"><strong>${escapeHtml(item.question)}</strong>: ${escapeHtml(item.reason)} <span class="asset-references">(${escapeHtml(item.references.join(', '))})</span></aside>`).join('');
  const cards = draft.sections.map((s, i) => `<article class="section-card"><span class="eyebrow">${two(i)}</span><h2><a href="${sectionFile[i]}">${escapeHtml(s.title)}</a></h2>${rendered[i]!.leads[0] ?? sectionBody(i)}<p><a href="${sectionFile[i]}">Read the full section (${rendered[i]!.blocks.length} block${rendered[i]!.blocks.length === 1 ? '' : 's'}, ${draft.diagrams.filter(d => d.sectionId === s.id).length} diagram(s), ${draft.deepDives.filter(d => d.sectionId === s.id).length} deep dive(s))</a></p></article>`).join('');
  pages.push({ path: 'index.html', kind: 'entry', content: `${head(draft.title)}${notice}${siteNav}<div class="layout"><nav class="contents" id="contents" aria-label="Contents"><span class="eyebrow">Contents</span>${contentsList}</nav><main id="manifesto"><header><span class="eyebrow">Polaris · Dossier draft</span><h1>${escapeHtml(draft.title)}</h1>${introHtml}${unresolved}</header>${cards}</main></div></body></html>` });
  draft.sections.forEach((s, i) => pages.push({ path: sectionFile[i]!, kind: 'section', content: page(s.title,
    `<header><span class="eyebrow">${two(i)} · <a href="index.html">${escapeHtml(draft.title)}</a></span><h1>${escapeHtml(s.title)}</h1></header>${rendered[i]!.blocks.join('') || sectionBody(i)}${rendered[i]!.diagrams}${rendered[i]!.deepLinks}${pager(i)}`) }));
  draft.deepDives.forEach((d, i) => {
    const parent = sectionIndex.get(d.sectionId)!;
    pages.push({ path: deepFile[i]!, kind: 'deep-dive', content: page(d.title,
      `<header><span class="eyebrow">Deep dive · <a href="${sectionFile[parent]}">Back to ${escapeHtml(draft.sections[parent]!.title)}</a></span><h1>${escapeHtml(d.title)}</h1></header>${deepHtml[i]}<p><a href="${sectionFile[parent]}">Return to the section</a></p>`) });
  });

  const glossary = options.glossary ?? [];
  const components = new Map<string, { label: string; markings: Set<string>; sourceIds: Set<string> }>();
  for (const d of draft.diagrams) if (d.disposition.kind === 'produced' && draft.sections[sectionIndex.get(d.sectionId)!]!.disposition.kind === 'produced') for (const node of d.nodes) {
    const key = node.label.toLowerCase();
    const entry = components.get(key) ?? { label: node.label, markings: new Set<string>(), sourceIds: new Set<string>() };
    entry.markings.add(node.epistemic);
    node.sourceIds.forEach(id => entry.sourceIds.add(id));
    components.set(key, entry);
  }
  const glossaryHtml = (glossary.length === 0 && components.size === 0 ? '<p>No glossary was produced for this run, and no diagram names a component.</p>' : '')
    + (glossary.length === 0 ? '<p>No term definitions were produced for this run.</p>' : `<dl>${[...glossary].sort((a, b) => a.term.localeCompare(b.term)).map(e => `<dt>${escapeHtml(e.term)}</dt><dd>${escapeHtml(e.definition)} ${refs(e.sourceIds)}</dd>`).join('')}</dl>`)
    + (components.size === 0 ? '' : `<h2>Named components</h2><p>Names that appear in the diagrams. This is an index of names, not definitions.</p><ul>${[...components.values()].sort((a, b) => a.label.localeCompare(b.label)).map(c => `<li>${escapeHtml(c.label)} <span class="marking">[${[...c.markings].sort().join(', ')}]</span> ${refs([...c.sourceIds])}</li>`).join('')}</ul>`);
  pages.push({ path: 'glossary.html', kind: 'glossary', content: page('Glossary', `<header><span class="eyebrow"><a href="index.html">${escapeHtml(draft.title)}</a></span><h1>Glossary</h1></header>${glossaryHtml}`) });

  const quotable = (s: GenerationSource): boolean => !s.exclusion.excluded && s.classificationBasis === 'body' && s.spans.length === 1;
  const sourceRows = sources.map(source => {
    const status = cited.has(source.sourceId) ? `<a href="${sourcePage(source.sourceId)}">cited: exact text</a>` : quotable(source) ? 'quotable, not cited' : escapeHtml(`counted, not quotable: ${source.exclusion.excluded ? source.exclusion.reason : source.classificationBasis}`);
    return `<tr><td>${escapeHtml(source.path)}${source.segment ? ` (piece ${source.segment.index + 1} of ${source.segment.count})` : ''}</td><td>${status}</td></tr>`;
  }).join('');
  pages.push({ path: 'sources.html', kind: 'sources', content: page('Sources', `<header><span class="eyebrow"><a href="index.html">${escapeHtml(draft.title)}</a></span><h1>Sources</h1></header><p>Every counted source and what the dossier does with it. Citation presence does not establish fidelity or approval.</p><table><thead><tr><th>Path</th><th>Status</th></tr></thead><tbody>${sourceRows}</tbody></table>`) });
  for (const source of cited.values()) {
    const span = source.spans[0]!;
    pages.push({ path: sourcePage(source.sourceId), kind: 'source', content: page(source.path,
      `<header><span class="eyebrow"><a href="sources.html">Sources</a></span><h1>${escapeHtml(source.path)}</h1></header><article class="source-item" id="${localAnchor(span.anchorId)}"><p class="eyebrow">${escapeHtml(source.sourceId)}${source.segment ? ` · bytes ${source.segment.start}–${source.segment.end} of the file` : ''}</p><div class="exact-source">${escapeHtml(span.text)}</div></article>`) });
  }

  const sized = (p: SitePage): PageSize => ({ path: p.path, kind: p.kind, bytes: Buffer.byteLength(p.content, 'utf8'), words: p.path.endsWith('.json') ? 0 : wordCount(p.content), sha256: sha256(p.content) });
  const sizes = pages.map(sized);
  const entry = sizes[0]!, largest = sizes.reduce((a, b) => b.bytes > a.bytes ? b : a);
  const sizeReport: SizeReport = { pages: sizes, totalBytes: sizes.reduce((n, p) => n + p.bytes, 0), totalWords: sizes.reduce((n, p) => n + p.words, 0),
    firstLevel: { path: entry.path, bytes: entry.bytes, words: entry.words }, largest: { path: largest.path, bytes: largest.bytes },
    counts: { sections: draft.sections.length, deepDives: draft.deepDives.length, diagrams: draft.diagrams.length, sourcesCounted: sources.length, sourcesCited: cited.size, sourcesNotCited: sources.length - cited.size },
    excludes: 'size-report.html and size-report.json are not counted in these figures' };
  pages.push({ path: 'size-report.html', kind: 'size-report', content: page('Size report',
    `<header><span class="eyebrow"><a href="index.html">${escapeHtml(draft.title)}</a></span><h1>Size report</h1></header><p>First level (entry page): ${entry.bytes} bytes, ${entry.words} words. All pages: ${sizeReport.totalBytes} bytes, ${sizeReport.totalWords} words in ${sizes.length} pages. Largest: ${escapeHtml(largest.path)} (${largest.bytes} bytes). ${escapeHtml(sizeReport.excludes)}. Words are counted over visible text with styles and tags removed; no budget is applied here.</p><table><thead><tr><th>Page</th><th>Kind</th><th>Bytes</th><th>Words</th></tr></thead><tbody>${sizes.map(p => `<tr><td>${escapeHtml(p.path)}</td><td>${p.kind}</td><td>${p.bytes}</td><td>${p.words}</td></tr>`).join('')}</tbody></table>`) });
  pages.push({ path: 'size-report.json', kind: 'size-report-data', content: `${JSON.stringify(sizeReport, null, 2)}\n` });
  return { pages, sizeReport };
}

const SAFE_NAME = /^[a-z0-9][a-z0-9._-]*$/u;

/** Writes the site into a fresh directory that is not inside a git work tree. */
export function writeDossierSite(runDir: string, site: DossierSite): { readonly written: number; readonly bytes: number } {
  const target = resolve(runDir);
  for (let at = target; ; at = dirname(at)) {
    if (existsSync(join(at, '.git'))) throw new Error('run-directory-inside-git-work-tree');
    if (dirname(at) === at) break;
  }
  if (existsSync(target) && readdirSync(target).length > 0) throw new Error('run-directory-not-empty');
  for (const page of site.pages) if (!SAFE_NAME.test(page.path)) throw new Error('unsafe-page-name');
  if (new Set(site.pages.map(page => page.path)).size !== site.pages.length) throw new Error('duplicate-page-name');
  mkdirSync(target, { recursive: true });
  let bytes = 0;
  for (const page of site.pages) { writeFileSync(join(target, page.path), page.content, { flag: 'wx' }); bytes += Buffer.byteLength(page.content); }
  return { written: site.pages.length, bytes };
}
