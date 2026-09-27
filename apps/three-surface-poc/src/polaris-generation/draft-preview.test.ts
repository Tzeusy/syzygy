import { describe, expect, it } from 'vitest';
import type { ProviderDraft } from '@syzygy/polaris-generation-core';
import { renderDraftPreview } from './draft-preview.js';
import { assertInertSvg } from './svg-inert.js';
import { syntheticGenerationSource } from './synthetic-source.js';

function fixture(): ProviderDraft {
  return {
    title: 'A quieter everyday', introduction: { id: 'intro', text: 'Let recurring work take care of itself.', sourceIds: ['purpose'] },
    sections: [{ id: 'architecture', title: 'How the pieces connect', paragraphs: [{ id: 'overview', text: 'Requests reach the planner, then the calendar.', sourceIds: ['architecture'],
      children: [{ id: 'overview-mechanism', text: 'The planner schedules an event in the calendar.', sourceIds: ['architecture'] }] }], disposition: { kind: 'produced', assetIds: ['architecture'] } }],
    diagrams: [{ id: 'flow', title: 'From request to calendar', sectionId: 'architecture', kind: 'flow', relationship: 'How a request becomes a calendar event', nodes: [
      { id: 'planner', label: 'Planner', sourceIds: ['architecture'], epistemic: 'observed' }, { id: 'calendar', label: 'Calendar', sourceIds: ['architecture'], epistemic: 'observed' },
    ], edges: [{ id: 'schedules', from: 'planner', to: 'calendar', label: 'Schedules an event', sourceIds: ['architecture'], epistemic: 'observed' }], disposition: { kind: 'produced', assetIds: ['flow'] } }],
    deepDives: [{ id: 'calendar-detail', title: 'Inside the calendar', sectionId: 'architecture', paragraphs: [{ id: 'detail', text: 'The calendar records scheduled events.', sourceIds: ['architecture'], children: [] }], disposition: { kind: 'produced', assetIds: ['calendar-detail'] } }],
    unresolved: [],
  };
}
const revision = 'a'.repeat(40);
const sources = [syntheticGenerationSource('preview', revision, 'purpose', 'Reduce recurring mental work.'),
  syntheticGenerationSource('preview', revision, 'architecture', 'Planner schedules events in the calendar.')];

describe('intermediate draft preview', () => {
  it('binds citation hrefs to source anchors, independent of list position', () => {
    const hrefs = (html: string): string[] => [...html.matchAll(/class="sources">([^<]*<a[^>]*>[^<]*<\/a>[^<]*)<\/span>/g)]
      .flatMap(match => [...match[1]!.matchAll(/href="([^"]+)"/g)].map(link => link[1]!));
    const before = hrefs(renderDraftPreview(fixture(), sources));
    const shuffled = hrefs(renderDraftPreview(fixture(), [...sources].reverse()));
    expect(before).toEqual(shuffled);
    expect(before.length).toBeGreaterThan(3);
    expect(before.every(href => href.startsWith('#source-') && !/#source-\d+$/.test(href))).toBe(true);
    const changed = syntheticGenerationSource('preview', revision, 'purpose', 'Reduce recurring mental work, with a new qualification.');
    const after = hrefs(renderDraftPreview(fixture(), [changed, sources[1]!]));
    expect(after[0]).not.toBe(before[0]);
    expect(after.slice(1)).toEqual(before.slice(1));
  });

  it('counts path-only sources without giving them a citation or fabricated text', () => {
    const { body: _body, ...withoutBody } = sources[0]!;
    const pathOnly = { ...withoutBody, sourceId: 'unread', path: 'synthetic/unread.md', classificationBasis: 'path-only' as const, spans: [] };
    const html = renderDraftPreview(fixture(), [...sources, pathOnly]);
    expect(html).toContain('synthetic/unread.md');
    expect(html).toContain('path-only; body not read');
    const forged = fixture();
    forged.introduction.sourceIds = ['unread'];
    expect(() => renderDraftPreview(forged, [...sources, pathOnly])).toThrow('unquotable-source');
    expect(() => renderDraftPreview(fixture(), [{ ...pathOnly, spans: sources[0]!.spans }])).toThrow('unquotable-source');
  });

  it('refuses a source whose anchor is not bound to its object and offsets', () => {
    expect(() => renderDraftPreview(fixture(), [{ ...sources[0]!, spans: [{ ...sources[0]!.spans[0]!, anchorId: 'source-0' }] }, sources[1]!]))
      .toThrow('invalid-anchor');
  });

  it('renders navigation, actual directed SVG, textual relationships, optional deep dives and exact sources', () => {
    const html = renderDraftPreview(fixture(), sources);
    expect(html).toContain('Pipeline draft preview — not reviewed or adopted');
    expect(html).toContain('marker-end="url(#arrow-0)"');
    expect(html).toContain('Planner → Calendar: Schedules an event');
    expect(html).toContain('<div class="deep-dive" id="deep-dive-0"><details>');
    expect(html).toContain('Explore: Inside the calendar');
    expect(html).toContain('Planner schedules events in the calendar.');
    const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);
    expect(new Set(ids).size).toBe(ids.length);
    for (const match of html.matchAll(/href="#([^"]+)"/g)) expect(ids).toContain(match[1]);
    for (const match of html.matchAll(/aria-(?:labelledby|describedby)="([^"]+)"/g)) expect(ids).toContain(match[1]);
  });

  it('keeps mobile navigation collapsed and shows isolated nodes without inventing relationships', () => {
    const d = fixture();
    d.diagrams[0]!.nodes.push({ id: 'archive', label: 'Archive', sourceIds: ['architecture'], epistemic: 'observed' });
    const html = renderDraftPreview(d, sources);
    expect(html).toContain('<details class="contents mobile-contents"><summary>In this manifesto</summary>');
    expect(html).toContain('.desktop-contents{display:none}.mobile-contents{display:block}');
    expect(html).toContain('class="pipeline-notice"');
    const svg = html.match(/<svg[\s\S]*?<\/svg>/)![0];
    expect(svg).toContain('Archive</tspan>');
    expect(svg).toContain('No relationship supplied</text>');
    expect(svg.match(/marker-end=/g)).toHaveLength(1);
    expect(html).toContain('Archive — No relationship supplied');
  });

  it('escapes hostile text in every generated text surface and never creates external resource requests', () => {
    const d = fixture();
    const hostile = '<script src="https://evil.test/a">alert(1)</script><img src=x onerror=boom>&';
    d.title = hostile;
    d.introduction.text = hostile;
    d.sections[0]!.title = hostile;
    d.sections[0]!.paragraphs[0]!.text = hostile;
    d.sections[0]!.paragraphs[0]!.children[0]!.text = hostile;
    d.diagrams[0]!.relationship = hostile;
    d.diagrams[0]!.title = hostile;
    d.diagrams[0]!.nodes[0]!.label = hostile;
    d.diagrams[0]!.edges[0]!.label = hostile;
    d.deepDives[0]!.title = hostile;
    d.deepDives[0]!.paragraphs[0]!.text = hostile;
    const html = renderDraftPreview(d, sources.map(s => syntheticGenerationSource('preview', revision, s.sourceId, hostile)));
    expect(html).toContain('&lt;script src=&quot;https://evil.test/a&quot;&gt;');
    expect(html).not.toMatch(/<(?:script|img|iframe|link|object|embed)\b/i);
    expect(html).not.toMatch(/\shref="(?!#)|\ssrc="/i);
    expect(html).toContain("default-src 'none'");
    expect(html).not.toContain('@import');
    expect(html).toContain('<svg xmlns="http://www.w3.org/2000/svg"');
  });

  it('refuses missing sources including diagram and deep dive support', () => {
    for (const target of ['intro', 'node', 'edge', 'deep'] as const) {
      const d = fixture();
      const p = target === 'intro' ? d.introduction : target === 'node' ? d.diagrams[0]!.nodes[0]! : target === 'edge' ? d.diagrams[0]!.edges[0]! : d.deepDives[0]!.paragraphs[0]!;
      p.sourceIds = ['missing'];
      expect(() => renderDraftPreview(d, sources)).toThrow('unknown-source');
    }
    expect(() => renderDraftPreview(fixture(), [...sources, sources[0]!])).toThrow('duplicate-source');
  });

  it('refuses unresolved section and node references instead of silently omitting assets', () => {
    const d = fixture();
    d.deepDives[0]!.sectionId = 'missing';
    expect(() => renderDraftPreview(d, sources)).toThrow('unknown-section');
    const n = fixture();
    n.diagrams[0]!.edges[0]!.to = 'missing';
    expect(() => renderDraftPreview(n, sources)).toThrow('unknown-node');
    const duplicate = fixture();
    duplicate.sections[0]!.id = 'intro';
    duplicate.diagrams = [];
    duplicate.deepDives = [];
    expect(() => renderDraftPreview(duplicate, sources)).toThrow('duplicate-draft-handle');
  });

  it('localizes unresolved asset absence with its reason and references', () => {
    const d = fixture();
    d.diagrams[0]!.disposition = { kind: 'unresolved', reason: 'renderer capability unavailable', references: ['architecture'] };
    d.unresolved = [{ question: 'How does the relationship work?', reason: 'renderer capability unavailable', references: ['architecture'] }];
    const html = renderDraftPreview(d, sources);
    expect(html).toContain('data-asset-disposition="unresolved"');
    expect(html).toContain('renderer capability unavailable');
    expect(html).toContain('architecture');
    expect(html).not.toContain('marker-end="url(#arrow-0)"');
  });

  it('localizes an unresolved section without presenting its draft body as produced', () => {
    const d = fixture();
    d.sections[0]!.disposition = { kind: 'unresolved', reason: 'No authoring basis', references: ['architecture'] };
    const html = renderDraftPreview(d, sources);
    expect(html).toContain('id="section-0"');
    expect(html).toContain('data-asset-disposition="unresolved"');
    expect(html).toContain('No authoring basis');
    expect(html).toContain('architecture');
    expect(html).not.toContain('Requests reach the planner, then the calendar.');
    expect(html).not.toContain('marker-end="url(#arrow-0)"');
  });
  it('renders a tree block as a paragraph with its children nested beneath, each with its refs', () => {
    const html = renderDraftPreview(fixture(), sources);
    expect(html).toMatch(/<p>Requests reach the planner, then the calendar\. <span class="sources"><a href="#source-[0-9a-f]{24}" aria-label="Read source architecture">\[architecture\]<\/a><\/span><\/p><ul class="block-children"><li>The planner schedules an event in the calendar\. <span class="sources"><a href="#source-[0-9a-f]{24}" aria-label="Read source architecture">\[architecture\]<\/a><\/span><\/li><\/ul>/u);
    expect(html).toContain('<p>The calendar records scheduled events. <span class="sources">');
    expect(html.match(/class="block-children"/g)).toHaveLength(1);
    const clash = fixture();
    clash.sections[0]!.paragraphs[0]!.children[0]!.id = 'detail';
    expect(() => renderDraftPreview(clash, sources)).toThrow('duplicate-draft-handle');
    const missing = fixture();
    missing.sections[0]!.paragraphs[0]!.children[0]!.sourceIds = ['missing'];
    expect(() => renderDraftPreview(missing, sources)).toThrow('unknown-source');
  });

  it('carries every epistemic marking into the SVG classes, the text equivalent and the declarative source', () => {
    const d = fixture();
    d.diagrams[0]!.nodes[1]!.epistemic = 'unknown';
    d.diagrams[0]!.edges[0]!.epistemic = 'inferred';
    const html = renderDraftPreview(d, sources);
    const svg = html.match(/<svg[\s\S]*?<\/svg>/u)![0];
    expect(svg).toContain('<g class="node observed"><title>Planner (observed)</title>');
    expect(svg).toContain('<g class="node unknown"><title>Calendar (unknown)</title>');
    expect(svg).toContain('>Calendar ?</tspan>');
    expect(svg).toContain('<g class="edge inferred"><title>Schedules an event (inferred)</title>');
    expect(html).toContain('<li>Planner <span class="marking observed">[Observed]</span>');
    expect(html).toContain('<li>Calendar <span class="marking unknown">[Unknown]</span>');
    expect(html).toContain('<li>Planner → Calendar: Schedules an event <span class="marking inferred">[Inferred]</span>');
    expect(html).toContain('<details class="diagram-source"><summary>Declarative source (Mermaid)</summary><pre>flowchart LR\n  n0[&quot;Planner&quot;]\n  n1[&quot;Calendar #40;unknown#41;&quot;]\n  n0 -.-&gt;|&quot;Schedules an event&quot;| n1\n  class n1 unknown\n  classDef inferred stroke-dasharray:6 4\n  classDef unknown stroke-dasharray:2 4\n</pre></details></details>');
    expect(html).toContain('<li><span class="legend-line inferred" aria-hidden="true"></span>Dashed: inferred</li>');
    expect(html).toContain('<p class="diagram-relationship"><span class="eyebrow">flow</span> How a request becomes a calendar event</p>');
    expect(html).toContain('svg .inferred>path,svg .inferred>rect{stroke-dasharray:6 4}svg .unknown>path,svg .unknown>rect{stroke-dasharray:2 4}');
  });

  it('never emits an SVG the inert boundary refuses, and localizes the asset as unresolved instead', () => {
    const seen: string[] = [];
    const accepted = renderDraftPreview(fixture(), sources, undefined, { assertSvg: svg => { seen.push(svg); } });
    expect(seen).toHaveLength(1);
    expect(accepted).toContain(seen[0]);
    const refused = renderDraftPreview(fixture(), sources, undefined, { assertSvg: () => { throw new Error('unsafe-svg'); } });
    expect(refused).not.toContain('<svg');
    expect(refused).not.toContain('marker-end');
    expect(refused).not.toContain('diagram-text-0');
    expect(refused).toContain('<aside class="unresolved-asset" data-asset-disposition="unresolved" id="unresolved-flow"><strong>flow</strong>: diagram could not be rendered inertly <span class="asset-references">(architecture)</span></aside>');
    expect(refused).toContain('Requests reach the planner, then the calendar.');
    expect(() => renderDraftPreview(fixture(), sources, undefined, { assertSvg: () => { throw new Error('unsafe-svg'); } })).not.toThrow();
  });

  it('passes every diagram it renders through the real inert boundary', () => {
    const d = fixture();
    d.diagrams[0]!.nodes.push({ id: 'archive', label: 'Archive "&" <x>', sourceIds: ['architecture'], epistemic: 'inferred' });
    d.diagrams[0]!.edges.push({ id: 'loop', from: 'calendar', to: 'planner', label: 'Reports back', sourceIds: ['architecture'], epistemic: 'unknown' });
    d.diagrams[0]!.edges.push({ id: 'self', from: 'calendar', to: 'calendar', label: 'Reschedules', sourceIds: ['architecture'], epistemic: 'observed' });
    const html = renderDraftPreview(d, sources);
    const svg = html.match(/<svg[\s\S]*?<\/svg>/u)![0];
    expect(() => assertInertSvg(svg)).not.toThrow();
    expect(svg.match(/marker-end=/g)).toHaveLength(3);
    expect(svg).toContain('Archive &quot;&amp;&quot; &lt;x&gt;');
  });
});
