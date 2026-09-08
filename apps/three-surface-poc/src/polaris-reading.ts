import { createHash } from 'node:crypto';

import { ARCHITECTURE_READING_PLAN } from './polaris-reading-plan.js';

export interface ProjectReading {
  readonly summary: string;
  readonly full: string;
  readonly condensed: boolean;
}

export interface ReadingPlan {
  readonly statementSha256: string;
  readonly passages: readonly { readonly start: number; readonly end: number; readonly heading?: boolean }[];
}

/** A reviewed selection is valid only for the exact declaration it was read against.
 * No lexical heuristic decides whether a later paragraph is safe to omit. */
export function applyReadingPlan(text: string, plan: ReadingPlan): ProjectReading {
  const full = { summary: text, full: text, condensed: false };
  if (createHash('sha256').update(text, 'utf8').digest('hex') !== plan.statementSha256 || plan.passages.length === 0) return full;
  let previousEnd = 0;
  for (const passage of plan.passages) {
    const { start, end } = passage;
    if (!Number.isInteger(start) || !Number.isInteger(end) || start < previousEnd || end <= start || end > text.length) return full;
    if ((start !== 0 && text[start - 1] !== '\n') || (end !== text.length && text[end] !== '\n')) return full;
    if (passage.heading === true && text.slice(start, end).includes('\n')) return full;
    previousEnd = end;
  }
  const summary = plan.passages.map(({ start, end, heading }) => `${heading === true ? '### ' : ''}${text.slice(start, end)}`).join('\n\n');
  return { summary, full: text, condensed: true };
}

export function projectReading(text: string, key: string): ProjectReading {
  return key === 'architecture'
    ? applyReadingPlan(text, ARCHITECTURE_READING_PLAN)
    : { summary: text, full: text, condensed: false };
}
