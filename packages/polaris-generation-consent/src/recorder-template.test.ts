import { describe, expect, it } from 'vitest';
import { SLOT, recorderTemplate, templateFields, type RecorderTemplate } from './recorder-template.js';

describe('a recorder template', () => {
  const t = recorderTemplate('# Act (v1.0) on {date}\n\nArgument: {sha}\n\nAgain on {date}.\n', { date: SLOT.date, sha: SLOT.sha256 });
  const record = `# Act (v1.0) on 2026-10-07\n\nArgument: ${'a'.repeat(64)}\n\nAgain on 2026-10-07.\n`;

  it('reads the slots of the text it renders, and renders them back byte for byte', () => {
    expect(templateFields(t, record)).toEqual({ date: '2026-10-07', sha: 'a'.repeat(64) });
    expect(t.render({ date: '2026-10-07', sha: 'a'.repeat(64) })).toBe(record);
  });
  it.each([
    ['text before it', `x${record}`],
    ['text after it', `${record}Withdrawn by this record.\n`],
    ['a repeated slot with another value', record.replace('Again on 2026-10-07', 'Again on 2026-10-08')],
    ['a literal metacharacter read as a pattern', record.replace('(v1.0)', '(v1x0)')],
    ['a slot outside its pattern', record.replace('a'.repeat(64), 'A'.repeat(64))],
  ])('reads nothing from %s', (_name, text) => {
    expect(t.fields(text)).toBeNull();
    expect(templateFields(t, text)).toBeNull();
  });
  it('reads a line slot only when it holds a non-space character and no line break', () => {
    const quote = recorderTemplate('Owner selection: {quote}\n', { quote: SLOT.line });
    expect(templateFields(quote, 'Owner selection: Extend Scope A\n')).toEqual({ quote: 'Extend Scope A' });
    for (const value of [' ', '\t', 'Extend\rScope A', '']) expect(templateFields(quote, `Owner selection: ${value}\n`), JSON.stringify(value)).toBeNull();
  });
  it('refuses a template slot with no pattern', () => {
    expect(() => recorderTemplate('{date} {other}', { date: SLOT.date })).toThrow('template slot {other} has no pattern');
  });
  it('counts slots only when they render back to the text, whatever the parse returned', () => {
    const lax: RecorderTemplate = { fields: () => ({ date: '2026-10-07' }), render: f => `on ${f['date']}\n` };
    expect(templateFields(lax, 'on 2026-10-07\n')).toEqual({ date: '2026-10-07' });
    expect(templateFields(lax, 'on 2026-10-07\nWithdrawn.\n')).toBeNull();
  });
});
