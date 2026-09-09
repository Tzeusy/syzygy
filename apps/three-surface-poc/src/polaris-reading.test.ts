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
});
