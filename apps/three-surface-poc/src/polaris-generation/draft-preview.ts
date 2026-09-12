import { DESIGN_TOKENS_CSS } from '../design-tokens.js';

import type { ProviderDraft } from '@syzygy/polaris-generation-core';
type Paragraph = ProviderDraft['introduction'];
type Diagram = ProviderDraft['diagrams'][number];

const escape = (value: string): string => value.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!);

/** Intermediate editorial preview only; no adoption, source admission or review verdict. */
export function renderDraftPreview(draft: ProviderDraft, sources: readonly { sourceId: string; text: string }[]): string {
  const sourceIndex = new Map(sources.map((source, index) => [source.sourceId, index]));
  if (sourceIndex.size !== sources.length) throw new Error('duplicate-source');
  const handles = new Set<string>();
  const register = (id: string): void => {
    if (handles.has(id)) throw new Error('duplicate-draft-handle');
    handles.add(id);
  };
  const refs = (ids: readonly string[]): string => {
    if (!ids.length) throw new Error('missing-source-reference');
    return `<span class="sources">${ids.map(id => {
      const index = sourceIndex.get(id);
      if (index === undefined) throw new Error('unknown-source');
      return `<a href="#source-${index}" aria-label="Read source ${index + 1}">[${index + 1}]</a>`;
    }).join(' ')}</span>`;
  };
  const paragraph = (p: Paragraph): string => {
    register(p.id);
    return `<p>${escape(p.text)} ${refs(p.sourceIds)}</p>`;
  };
  const sectionIds = new Set(draft.sections.map(s => s.id));
  for (const item of [...draft.diagrams, ...draft.deepDives]) {
    if (!sectionIds.has(item.sectionId)) throw new Error('unknown-section');
  }
  const diagram = (d: Diagram, index: number): string => {
    register(d.id);
    const nodes = new Map(d.nodes.map(node => [node.id, node]));
    d.nodes.forEach(node => register(node.id));
    const label = (text: string, x: number, top: number): string => {
        const short = text.length > 54 ? `${text.slice(0, 51)}…` : text;
        const chunks = short.match(/.{1,27}/gu) ?? [''];
        return `<text x="${x}" y="${top}" text-anchor="middle">${chunks.map((chunk, i) => `<tspan x="${x}" dy="${i ? 20 : 0}">${escape(chunk)}</tspan>`).join('')}</text>`;
      };
    const rows = d.edges.map((edge, row) => {
      register(edge.id);
      const from = nodes.get(edge.from);
      const to = nodes.get(edge.to);
      if (!from || !to) throw new Error('unknown-node');
      const y = 24 + row * 116;
      return `<g><rect x="16" y="${y}" width="220" height="64" rx="8"/><rect x="564" y="${y}" width="220" height="64" rx="8"/><path d="M 244 ${y + 38} H 552" marker-end="url(#arrow-${index})"/>${label(from.label, 126, y + 26)}${label(to.label, 674, y + 26)}${label(edge.label, 400, y + 6)}</g>`;
    }).join('');
    const connected = new Set(d.edges.flatMap(edge => [edge.from, edge.to]));
    const isolated = d.nodes.filter(node => !connected.has(node.id));
    const isolatedRows = isolated.map((node, row) => {
      const y = 24 + (d.edges.length + row) * 116;
      return `<g><rect x="16" y="${y}" width="220" height="64" rx="8"/>${label(node.label, 126, y + 26)}<text x="270" y="${y + 38}">No relationship supplied</text></g>`;
    }).join('');
    const nodeList = d.nodes.map(n => `<li>${escape(n.label)}${connected.has(n.id) ? '' : ' — No relationship supplied'} ${refs(n.sourceIds)}</li>`).join('');
    const edgeList = d.edges.map(e => `<li>${escape(nodes.get(e.from)!.label)} → ${escape(nodes.get(e.to)!.label)}: ${escape(e.label)} ${refs(e.sourceIds)}</li>`).join('');
    return `<figure><figcaption id="diagram-title-${index}">${escape(d.title)}</figcaption><div class="diagram-scroll"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 ${Math.max(120, (d.edges.length + isolated.length) * 116 + 24)}" role="img" aria-labelledby="diagram-title-${index}" aria-describedby="diagram-text-${index}"><defs><marker id="arrow-${index}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z"/></marker></defs>${rows}${isolatedRows}</svg></div><details id="diagram-text-${index}"><summary>Read every component and relationship</summary><ul>${nodeList}</ul><ol>${edgeList}</ol></details></figure>`;
  };
  const intro = paragraph(draft.introduction);
  const sections = draft.sections.map((section, index) => {
    register(section.id);
    return `<section id="section-${index}" aria-labelledby="heading-${index}"><span class="eyebrow">${String(index + 1).padStart(2, '0')}</span><h2 id="heading-${index}">${escape(section.title)}</h2>${section.paragraphs.map(paragraph).join('')}${draft.diagrams.map((d, i) => d.sectionId === section.id ? diagram(d, i) : '').join('')}${draft.deepDives.map((d, i) => {
      if (d.sectionId !== section.id) return '';
      register(d.id);
      return `<div class="deep-dive" id="deep-dive-${i}"><details><summary>Explore: ${escape(d.title)}</summary>${d.paragraphs.map(paragraph).join('')}</details></div>`;
    }).join('')}</section>`;
  }).join('');
  const contents = `<ol><li><a href="#manifesto">Introduction</a></li>${draft.sections.map((s, i) => `<li><a href="#section-${i}">${escape(s.title)}</a></li>`).join('')}<li><a href="#sources">Exact source text</a></li></ol>`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"><title>${escape(draft.title)} — draft preview</title><style>${DESIGN_TOKENS_CSS}
*{box-sizing:border-box}body{margin:0;background:var(--void);color:var(--ink);font-family:var(--font-serif);line-height:1.7}a{color:var(--cyan);text-underline-offset:.2em}a:focus-visible,summary:focus-visible{outline:3px solid var(--focus);outline-offset:5px}.skip{position:absolute;left:1rem;top:-5rem}.skip:focus{top:1rem;background:var(--panel);padding:1rem;z-index:2}.pipeline-notice{padding:.65rem 2rem;border-bottom:1px solid var(--line);font: .8rem/1.5 var(--font-mono);color:var(--amber)}.layout{display:grid;grid-template-columns:220px minmax(0,1fr);gap:4vw;max-width:1600px;margin:auto;padding:3rem 4vw}.contents{align-self:start;position:sticky;top:2rem;font: .9rem/1.5 var(--font-mono);max-height:90vh;overflow:auto}.mobile-contents{display:none}.contents ol{padding-left:1.5rem}.contents li{margin:.85rem 0}.contents a{text-decoration:none}main{min-width:0}header{padding:1rem 0 3rem;border-bottom:1px solid var(--line)}h1{font-weight:400;font-size:clamp(2.8rem,5vw,5.5rem);line-height:1.08;letter-spacing:-.04em;margin:.4em 0;overflow-wrap:anywhere}h2{font-size:clamp(1.8rem,3vw,3rem);font-weight:400;line-height:1.2;margin:.4rem 0 1.5rem}p{max-width:76ch;font-size:1.1rem;white-space:pre-wrap;overflow-wrap:anywhere}header p{font-size:1.4rem;max-width:60ch;}section{padding:3rem 0;border-bottom:1px solid var(--line);scroll-margin-top:1rem}.eyebrow{font:.8rem var(--font-mono);color:var(--muted)}.sources{font:.75rem var(--font-mono);white-space:normal}.sources a{display:inline-block;padding:.1rem .15rem}figure{margin:2.5rem 0;padding:1.5rem;background:var(--panel);border:1px solid var(--line)}figcaption{font-size:1.3rem;margin-bottom:1rem}.diagram-scroll{overflow:auto}svg{display:block;width:100%;min-width:650px}svg rect{fill:var(--panel-raised);stroke:var(--line)}svg text{fill:var(--ink);font:15px var(--font-mono)}svg path{fill:none;stroke:var(--cyan);stroke-width:2}svg marker path{fill:var(--cyan);stroke:none}summary{cursor:pointer;color:var(--cyan);padding:.75rem 0}details li{overflow-wrap:anywhere}.deep-dive{padding:.5rem 1.2rem;border-left:2px solid var(--cyan);margin:1.5rem 0;background:var(--panel)}.exact-source{white-space:pre-wrap;overflow-wrap:anywhere;font: .9rem/1.6 var(--font-mono);max-width:90ch}.source-item{padding:1.25rem 0;border-top:1px solid var(--line);scroll-margin-top:1rem}@media(max-width:800px){.desktop-contents{display:none}.mobile-contents{display:block}.layout{display:block;padding:1.5rem}.contents{position:static;max-height:none;border-bottom:1px solid var(--line);padding-bottom:1rem}.contents ol{display:flex;gap:1rem 2rem;flex-wrap:wrap}.contents li{margin:.25rem 0}figure{padding:1rem}section{padding:2rem 0}}
</style></head><body><a class="skip" href="#manifesto">Skip to manifesto</a><div class="pipeline-notice">Pipeline draft preview — not reviewed or adopted</div><div class="layout"><nav class="contents desktop-contents" aria-label="Manifesto sections"><span class="eyebrow">In this manifesto</span>${contents}</nav><details class="contents mobile-contents"><summary>In this manifesto</summary><nav aria-label="Manifesto sections">${contents}</nav></details><main id="manifesto"><header><span class="eyebrow">Polaris · Editorial draft</span><h1>${escape(draft.title)}</h1>${intro}</header>${sections}<section id="sources"><h2>Exact source text</h2><p>These supplied excerpts support the draft’s references. Reference presence does not establish fidelity or approval.</p>${sources.map((s, i) => `<article class="source-item" id="source-${i}"><h3>Source ${i + 1} · ${escape(s.sourceId)}</h3><div class="exact-source">${escape(s.text)}</div></article>`).join('')}</section></main></div></body></html>`;
}
