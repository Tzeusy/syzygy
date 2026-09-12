import { describe, expect, it } from 'vitest';
import type { ProviderDraft } from '@syzygy/polaris-generation-core';
import { renderDraftPreview } from './draft-preview.js';

function fixture(): ProviderDraft {
  return {
    title: 'A quieter everyday', introduction: { id: 'intro', text: 'Let recurring work take care of itself.', sourceIds: ['purpose'] },
    sections: [{ id: 'architecture', title: 'How the pieces connect', paragraphs: [{ id: 'overview', text: 'Requests reach the planner, then the calendar.', sourceIds: ['architecture'] }] }],
    diagrams: [{ id: 'flow', title: 'From request to calendar', sectionId: 'architecture', nodes: [
      { id: 'planner', label: 'Planner', sourceIds: ['architecture'] }, { id: 'calendar', label: 'Calendar', sourceIds: ['architecture'] },
    ], edges: [{ id: 'schedules', from: 'planner', to: 'calendar', label: 'Schedules an event', sourceIds: ['architecture'] }] }],
    deepDives: [{ id: 'calendar-detail', title: 'Inside the calendar', sectionId: 'architecture', paragraphs: [{ id: 'detail', text: 'The calendar records scheduled events.', sourceIds: ['architecture'] }] }],
  };
}
const sources = [{ sourceId: 'purpose', text: 'Reduce recurring mental work.' }, { sourceId: 'architecture', text: 'Planner schedules events in the calendar.' }];

describe('intermediate draft preview', () => {
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
    d.diagrams[0]!.nodes.push({ id: 'archive', label: 'Archive', sourceIds: ['architecture'] });
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
    d.diagrams[0]!.title = hostile;
    d.diagrams[0]!.nodes[0]!.label = hostile;
    d.diagrams[0]!.edges[0]!.label = hostile;
    d.deepDives[0]!.title = hostile;
    d.deepDives[0]!.paragraphs[0]!.text = hostile;
    const html = renderDraftPreview(d, sources.map(s => ({ ...s, text: hostile })));
    expect(html).toContain('&lt;script src=&quot;https://evil.test/a&quot;&gt;');
    expect(html).not.toMatch(/<(?:script|img|iframe|link|object|embed)\b/i);
    expect(html).not.toMatch(/\shref="(?!#)|\ssrc="/i);
    expect(html).toContain("default-src 'none'");
    expect(html).not.toContain('@import');
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
});
