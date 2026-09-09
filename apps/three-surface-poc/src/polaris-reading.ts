import { createHash } from 'node:crypto';

import { ARCHITECTURE_READING_PLAN, V1_READING_PLAN } from './polaris-reading-plan.js';

export interface ReadingChapter {
  readonly id: string;
  readonly title: string;
  readonly body: string;
}

export interface ProjectReading {
  readonly summary: string;
  readonly full: string;
  readonly condensed: boolean;
  readonly chapters?: readonly ReadingChapter[];
}

export interface SourceSpan { readonly start: number; readonly end: number }
export interface ReadingPassage extends SourceSpan {
  readonly heading?: boolean;
  readonly format?: 'flow';
  readonly relationships?: readonly { readonly from: SourceSpan; readonly to: SourceSpan; readonly body: SourceSpan }[];
}

export interface ReadingPlan {
  readonly statementSha256: string;
  readonly chapters?: readonly { readonly id: string; readonly start: number; readonly headingEnd: number; readonly end: number }[];
  readonly passages: readonly ReadingPassage[];
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
    if (passage.format === 'flow' && !/^```\n[^\n]+\n```$/.test(text.slice(start, end))) return full;
    if (passage.relationships !== undefined) {
      if (passage.heading || passage.format || passage.relationships.length === 0 || passage.relationships.length > 8) return full;
      let bodyEnd = start;
      for (const relationship of passage.relationships) {
        const { body, from, to } = relationship;
        if (![body.start, body.end, from.start, from.end, to.start, to.end].every(Number.isInteger)
          || body.start < bodyEnd || body.end <= body.start || body.end > end
          || text.slice(bodyEnd, body.start).trim() !== ''
          || from.start < body.start || from.end <= from.start || from.end > body.end
          || to.start < body.start || to.end <= to.start || to.end > body.end) return full;
        bodyEnd = body.end;
      }
      if (text.slice(bodyEnd, end).trim() !== '') return full;
    }
    previousEnd = end;
  }
  let chapters: readonly ReadingChapter[] | undefined;
  if (plan.chapters !== undefined) {
    if (plan.chapters.length === 0 || plan.chapters.length > 24) return full;
    let end = 0;
    const ids = new Set<string>();
    for (const chapter of plan.chapters) {
      if (!/^[a-z][a-z0-9-]{0,63}$/.test(chapter.id) || ids.has(chapter.id)
        || ![chapter.start, chapter.headingEnd, chapter.end].every(Number.isInteger)
        || chapter.start !== end || chapter.headingEnd <= chapter.start
        || chapter.end <= chapter.headingEnd + 2 || chapter.end > text.length
        || (chapter.start !== 0 && text.slice(chapter.start - 2, chapter.start) !== '\n\n')
        || text.slice(chapter.start, chapter.headingEnd).trim() === ''
        || text.slice(chapter.start, chapter.headingEnd).includes('\n')
        || text.slice(chapter.headingEnd, chapter.headingEnd + 2) !== '\n\n') return full;
      ids.add(chapter.id);
      end = chapter.end;
    }
    if (end !== text.length) return full;
    chapters = plan.chapters.map(({ id, start, headingEnd, end }) => ({ id,
      title: text.slice(start, headingEnd), body: text.slice(headingEnd + 2, end) }));
  }
  const summary = plan.passages.map(({ start, end, heading, format, relationships }) => {
    const passage = text.slice(start, end);
    if (relationships !== undefined) return '```relations\n' + JSON.stringify(relationships.map(({ from, to, body }) => ({
      from: text.slice(from.start, from.end), to: text.slice(to.start, to.end), description: text.slice(body.start, body.end),
    }))) + '\n```';
    return format === 'flow' ? passage.replace(/^```\n/, '```flow\n') : `${heading === true ? '### ' : ''}${passage}`;
  }).join('\n\n');
  return { summary, full: text, condensed: true, ...(chapters === undefined ? {} : { chapters }) };
}

export function projectReading(text: string, key: string): ProjectReading {
  return key === 'architecture'
    ? applyReadingPlan(text, ARCHITECTURE_READING_PLAN)
    : key === 'v1-scope'
      ? applyReadingPlan(text, V1_READING_PLAN)
      : { summary: text, full: text, condensed: false };
}
