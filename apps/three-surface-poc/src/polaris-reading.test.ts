import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';

import { applyReadingPlan, projectReading, type ReadingPlan } from './polaris-reading.js';

const text = 'Process Model\n\nWorkers run with explicit approval.\n\nBackground examples.\n\nStorage Model\n\nRecords persist.';
const plan: ReadingPlan = {
  statementSha256: createHash('sha256').update(text).digest('hex'),
  passages: [{ start: 0, end: 13, heading: true }, { start: 15, end: 50 }, { start: 74, end: 87, heading: true }, { start: 89, end: 105 }],
};

describe('reviewed project reading', () => {
  it('preserves exact selected passages and the full declaration', () => {
    const result = applyReadingPlan(text, plan);
    expect(result).toEqual({ summary: '### Process Model\n\nWorkers run with explicit approval.\n\n### Storage Model\n\nRecords persist.', full: text, condensed: true });
  });

  it('retains the complete account after any source change, including a new unmarked qualification', () => {
    for (const changed of [text + '\n\nAccess requires further approval.', text.replace('explicit approval', 'no approval'), text.replace('Records persist.', 'Records persist only for one day.')]) {
      expect(applyReadingPlan(changed, plan)).toEqual({ summary: changed, full: changed, condensed: false });
    }
  });

  it('fails closed on empty, overlapping, out-of-bounds and partial-line selectors', () => {
    for (const passages of [[], [{ start: 0, end: 500 }], [{ start: 0, end: 12 }], [{ start: 1, end: 13 }], [{ start: 0, end: 13 }, { start: 0, end: 13 }]]) {
      const candidate = { ...plan, passages };
      expect(applyReadingPlan(text, candidate)).toEqual({ summary: text, full: text, condensed: false });
    }
    expect(applyReadingPlan(text, { ...plan, passages: [{ start: 0, end: 50, heading: true }] }).condensed).toBe(false);
  });

  it('never shortens unreviewed architecture or other account categories', () => {
    const declaration = 'Process Model\n\nWorkers share records.\n\nAccess requires explicit approval.\n\nStorage Model\n\nRecords persist.';
    for (const key of ['purpose', 'promises', 'refusals', 'v1-success', 'v1-scope', 'architecture']) {
      expect(projectReading(declaration, key)).toEqual({ summary: declaration, full: declaration, condensed: false });
    }
  });

  it('partitions the complete source into named guides and rejects gaps or duplicate identities', () => {
    const chapters = [{ id: 'process', start: 0, headingEnd: 13, end: 74 }, { id: 'storage', start: 74, headingEnd: 87, end: 105 }];
    const reading = applyReadingPlan(text, { ...plan, chapters });
    expect(reading.chapters).toEqual([
      { id: 'process', title: 'Process Model', body: 'Workers run with explicit approval.\n\nBackground examples.\n\n' },
      { id: 'storage', title: 'Storage Model', body: 'Records persist.' },
    ]);
    expect(reading.chapters?.map((chapter) => chapter.title + '\n\n' + chapter.body).join('')).toBe(text);
    for (const invalid of [chapters.slice(0, 1), [chapters[0]!, { ...chapters[1]!, start: 75 }], [chapters[0]!, { ...chapters[1]!, id: 'process' }]]) {
      expect(applyReadingPlan(text, { ...plan, chapters: invalid })).toEqual({ summary: text, full: text, condensed: false });
    }
  });

  it('requires relationship labels to come from complete retained explanations', () => {
    const source = 'Client calls tools.\n\nBroker routes work.';
    const relationshipPlan: ReadingPlan = { statementSha256: createHash('sha256').update(source).digest('hex'), passages: [{ start: 0, end: source.length, relationships: [
      { from: { start: 0, end: 6 }, to: { start: 13, end: 18 }, body: { start: 0, end: 19 } },
      { from: { start: 21, end: 27 }, to: { start: 35, end: 39 }, body: { start: 21, end: 40 } },
    ] }] };
    const result = applyReadingPlan(source, relationshipPlan);
    expect(result.summary).toContain('```relations');
    expect(result.summary).toContain('Client calls tools.');
    expect(result.summary).toContain('Broker routes work.');
    const missing = { ...relationshipPlan, passages: [{ ...relationshipPlan.passages[0]!, relationships: relationshipPlan.passages[0]!.relationships!.slice(0, 1) }] };
    expect(applyReadingPlan(source, missing)).toEqual({ summary: source, full: source, condensed: false });
    const rows = relationshipPlan.passages[0]!.relationships!;
    for (const first of [{ ...rows[0]!, body: { start: 0, end: 18 } }, { ...rows[0]!, from: { start: 21, end: 27 } }]) {
      const invalid = { ...relationshipPlan, passages: [{ ...relationshipPlan.passages[0]!, relationships: [first, rows[1]!] }] };
      expect(applyReadingPlan(source, invalid)).toEqual({ summary: source, full: source, condensed: false });
    }
  });

});
