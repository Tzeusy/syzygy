import { describe, expect, it } from 'vitest';
import { projectReading } from './polaris-reading.js';

describe('projectReading', () => {
  it('keeps short account categories and V1 scope intact', () => {
    const text = '### Scope\n\n- A complete declaration.\n\nDeferrals\n\nNot available.';
    for (const key of ['purpose', 'promises', 'refusals', 'v1-success', 'v1-scope']) {
      expect(projectReading(text, key)).toEqual({ summary: text, full: text, condensed: false });
    }
  });

  it('retains introduced lists, explanatory closure and unmarked exceptions', () => {
    const intro = 'The issue has these causes:\n\n- First cause.\n- Second cause.\n\nSeparate processes solve the issue.\n\nHowever, shared reads remain permitted.';
    const text = `Process Model\n\n${intro}\n\n**Why this helps:**\n\nRoutine operation becomes simpler.\n\nStorage Model\n\nRecords persist.`;
    const result = projectReading(text, 'architecture');
    expect(result.summary).toContain(intro);
    expect(result.summary).not.toContain('Routine operation becomes simpler.');
    expect(result.full).toBe(text);
    expect(result.condensed).toBe(true);
  });

  it('keeps qualifications in otherwise omittable rationale', () => {
    const text = 'Process Model\n\nWorkers run.\n\n**Why this helps:**\n\nShared access is useful.\n\nAn exception requires approval.\n\nStorage Model\n\nRecords persist.';
    expect(projectReading(text, 'architecture').summary).toContain('An exception requires approval.');
  });

  it('keeps fenced blocks intact, including blank lines and heading-like text', () => {
    const fence = '```\nStep One\n\nStep Two\n```';
    const text = `Process Model\n\nThe sequence follows:\n\n${fence}\n\nStorage Model\n\nRecords persist.`;
    expect(projectReading(text, 'architecture').summary).toContain(fence);
  });

  it('retains caution-only sections and falls back when boundaries are ambiguous', () => {
    const text = 'Overview\n\nWorkers run.\n\nCautions\n\n- Never share writes.\n- Retain records.';
    expect(projectReading(text, 'architecture').summary).toContain('- Never share writes.\n- Retain records.');
    const ambiguous = 'Workers run.\n\nAn unmarked exception follows.';
    expect(projectReading(ambiguous, 'architecture')).toEqual({ summary: ambiguous, full: ambiguous, condensed: false });
  });
});
