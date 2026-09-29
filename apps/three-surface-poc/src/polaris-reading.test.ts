import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';

import { applyReadingPlan, projectReading, type ReadingPlan } from './polaris-reading.js';
import { renderProjectReading } from './polaris.js';

const text = 'Process Model\n\nWorkers run with explicit approval.\n\nBackground examples.\n\nStorage Model\n\nRecords persist.';
const plan: ReadingPlan = {
  statementSha256: createHash('sha256').update(text).digest('hex'),
  passages: [{ start: 0, end: 13, heading: true }, { start: 15, end: 50 }, { start: 74, end: 87, heading: true }, { start: 89, end: 105 }],
};

describe('reviewed project reading', () => {
  it('preserves exact selected passages and the full declaration', () => {
    const result = applyReadingPlan(text, plan);
    expect(result).toEqual({ summary: '# Process Model\n\nWorkers run with explicit approval.\n\n# Storage Model\n\nRecords persist.', full: text, condensed: true });
  });

  it('retains the complete account after any source change, including a new unmarked qualification', () => {
    for (const changed of [text + '\n\nAccess requires further approval.', text.replace('explicit approval', 'no approval'), text.replace('Records persist.', 'Records persist only for one day.')]) {
      expect(applyReadingPlan(changed, plan)).toEqual({ summary: changed, full: changed, condensed: false, withdrawalReason: 'digest-mismatch' });
    }
  });

  it('announces why a reviewed selection was withdrawn while retaining the complete declaration', () => {
    const reading = applyReadingPlan(text + '\n\nChanged.', plan);
    expect(reading.withdrawalReason).toBe('digest-mismatch');
    const html = renderProjectReading(reading);
    expect(html).toContain('data-reading-withdrawal="digest-mismatch"');
    expect(html).toContain('Changed.');
  });

  it('fails closed on empty, overlapping, out-of-bounds and partial-line selectors', () => {
    expect(applyReadingPlan(text, { ...plan, passages: [] })).toEqual({ summary: text, full: text, condensed: false, withdrawalReason: 'no-passages' });
    for (const passages of [[{ start: 0, end: 500 }], [{ start: 0, end: 12 }], [{ start: 1, end: 13 }], [{ start: 0, end: 13 }, { start: 0, end: 13 }]]) {
      const candidate = { ...plan, passages };
      expect(applyReadingPlan(text, candidate)).toEqual({ summary: text, full: text, condensed: false, withdrawalReason: 'plan-malformed' });
    }
    expect(applyReadingPlan(text, { ...plan, passages: [{ start: 0, end: 50, heading: true }] })).toMatchObject({ condensed: false, withdrawalReason: 'plan-malformed' });
  });

  it('never shortens unreviewed architecture or other account categories', () => {
    const declaration = 'Process Model\n\nWorkers share records.\n\nAccess requires explicit approval.\n\nStorage Model\n\nRecords persist.';
    for (const key of ['purpose', 'promises', 'refusals', 'v1-success', 'v1-scope', 'architecture']) {
      const reading = projectReading(declaration, key);
      expect(reading).toMatchObject({ summary: declaration, full: declaration, condensed: false });
      if (reading.withdrawalReason !== undefined) expect(['digest-mismatch', 'no-passages', 'plan-malformed']).toContain(reading.withdrawalReason);
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
      expect(applyReadingPlan(text, { ...plan, chapters: invalid })).toEqual({ summary: text, full: text, condensed: false, withdrawalReason: 'plan-malformed' });
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
    expect(applyReadingPlan(source, missing)).toEqual({ summary: source, full: source, condensed: false, withdrawalReason: 'plan-malformed' });
    const rows = relationshipPlan.passages[0]!.relationships!;
    for (const first of [{ ...rows[0]!, body: { start: 0, end: 18 } }, { ...rows[0]!, from: { start: 21, end: 27 } }]) {
      const invalid = { ...relationshipPlan, passages: [{ ...relationshipPlan.passages[0]!, relationships: [first, rows[1]!] }] };
      expect(applyReadingPlan(source, invalid)).toEqual({ summary: source, full: source, condensed: false, withdrawalReason: 'plan-malformed' });
    }
  });

  it('binds diagram labels to retained evidence and removes diagrams on source drift or invalid metadata', () => {
    const source = 'Daemon spawns sessions.\n\nSessions call tools.';
    const figure = { id: 'runtime', title: 'Inside the runtime', nodes: [{ start: 0, end: 6 }, { start: 14, end: 22 }], evidence: [{ start: 0, end: 23 }] };
    const candidate: ReadingPlan = { statementSha256: createHash('sha256').update(source).digest('hex'), passages: [{ start: 0, end: source.length }], figures: [figure] };
    expect(applyReadingPlan(source, candidate).figures).toEqual([{ id: 'runtime', title: 'Inside the runtime', nodes: ['Daemon', 'sessions'], explanation: 'Daemon spawns sessions.' }]);
    for (const figures of [[{ ...figure, nodes: [{ start: 0, end: 6 }, { start: 25, end: 33 }] }], [figure, figure], [{ ...figure, evidence: [{ start: 0, end: 22 }] }], [{ ...figure, id: 'bad id' }]]) {
      expect(applyReadingPlan(source, { ...candidate, figures })).toEqual({ summary: source, full: source, condensed: false, withdrawalReason: 'plan-malformed' });
    }
    const changed = source + '\n\nOnly after approval.';
    expect(applyReadingPlan(changed, candidate)).toEqual({ summary: changed, full: changed, condensed: false, withdrawalReason: 'digest-mismatch' });
  });

});
