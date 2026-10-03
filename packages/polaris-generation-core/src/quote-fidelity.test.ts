import { describe, expect, it } from 'vitest';

import { QUOTE_LEAD_IN, checkBlockQuotes, normaliseForQuote, sourceTextById } from './quote-fidelity.js';

const SOURCES = sourceTextById([
  { sourceId: 'src-readme', text: 'Tidemark is an in-memory cache.\nWe chose a **single-threaded** event loop because it avoids\n  lock   contention. See [the design notes](docs/design.md) for _why_.\n' },
  { sourceId: 'src-code', text: '/**\n * maybeEvict samples 5 keys\n * and evicts the least recently used key.\n */\n// Never block the loop.\n# Setting: maxmemory\nint x = 1;\n' },
  { sourceId: 'src-nested', text: 'The docs say "never block" and then "stop" loudly; he said “quiet “inner” words” too.' },
]);
const block = (text: string, ...sourceIds: string[]) => ({ id: 'b1', text, sourceIds });
const kinds = (text: string, ...sourceIds: string[]): string[] => checkBlockQuotes(block(text, ...sourceIds), SOURCES).map(f => f.kind);

describe('normaliseForQuote', () => {
  it('drops comment leaders, link syntax and emphasis, and collapses every whitespace run', () => {
    expect(normaliseForQuote('/**\n * maybeEvict samples 5 keys\n * and evicts.\n */\n// Never block.\n# Setting')).toBe('maybeEvict samples 5 keys and evicts. Never block. Setting');
    expect(normaliseForQuote('See [the design notes](docs/design.md) and ![a diagram](x.png) and [ref][1]')).toBe('See the design notes and a diagram and ref');
    expect(normaliseForQuote('a **bold** and _em_ and *x*')).toBe('a bold and em and x');
    expect(normaliseForQuote('  one \t two\r\nthree\n\n four  ')).toBe('one two three four');
  });
});

describe('checkBlockQuotes', () => {
  it('passes a quote that is a substring of a cited source, whatever the whitespace, emphasis or link syntax', () => {
    expect(kinds('The project\'s sources state: "We chose a single-threaded event loop because it avoids lock contention."', 'src-readme')).toEqual([]);
    expect(kinds('It says "See the design notes for why."', 'src-readme')).toEqual([]);
    expect(kinds('The code says "maybeEvict samples 5 keys and evicts the least recently used key." and "Never block the loop."', 'src-code')).toEqual([]);
    expect(kinds('A comment: "Setting: maxmemory".', 'src-code')).toEqual([]);
    expect(kinds('He said “Tidemark is an in-memory cache.”', 'src-readme')).toEqual([]);
  });

  it('fails a quote that is not in any cited source, or only in an uncited one', () => {
    expect(kinds('"Tidemark is a distributed cache."', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"Tidemark IS an in-memory cache."', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"maybeEvict samples 5 keys"', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"maybeEvict samples 5 keys"', 'src-readme', 'src-code')).toEqual([]);
    // Two cited sources do not join: a quote spanning the end of one and the start of the next is in neither.
    expect(kinds('"for why. maybeEvict samples 5 keys"', 'src-readme', 'src-code')).toEqual(['quote-not-in-cited-sources']);
  });

  it('checks every quoted span in a block, not just the first', () => {
    expect(kinds('"Tidemark is an in-memory cache." but also "invented words".', 'src-readme')).toEqual(['quote-not-in-cited-sources']);
    expect(checkBlockQuotes(block('"invented one" and "invented two"', 'src-readme'), SOURCES).map(f => f.quote)).toEqual(['invented one', 'invented two']);
  });

  it('refuses a quote when the block cites no source, or cites only unknown ids', () => {
    expect(kinds('"Tidemark is an in-memory cache."')).toEqual(['quote-without-cited-source']);
    expect(kinds('"Tidemark is an in-memory cache."', 'src-unknown')).toEqual(['quote-without-cited-source']);
  });

  it('handles quotes that contain quotes, straight or curly', () => {
    expect(kinds('The docs say: "The docs say "never block" and then "stop" loudly".', 'src-nested')).toEqual([]);
    expect(kinds('The project\'s sources state: "The docs say "never block" and then "stop" loudly; he said “quiet “inner” words” too."', 'src-nested')).toEqual([]);
    expect(kinds('He said “quiet “inner” words”.', 'src-nested')).toEqual([]);
    expect(kinds('He said “quiet “invented” words”.', 'src-nested')).toEqual(['quote-not-in-cited-sources']);
    expect(kinds('"never block" and "stop" loudly', 'src-nested')).toEqual([]);
    expect(kinds('"never block" and "stop" loudly and "invented"', 'src-nested')).toEqual(['quote-not-in-cited-sources']);
  });

  it('fails an unterminated, empty or lead-in-only quote rather than skipping it', () => {
    expect(kinds('The text opens "Tidemark is an in-memory cache.', 'src-readme')).toEqual(['unterminated-quote']);
    expect(kinds('He said “Tidemark is an in-memory cache.', 'src-readme')).toEqual(['unterminated-quote']);
    expect(kinds('An empty "" quote.', 'src-readme')).toEqual(['empty-quote']);
    expect(kinds('A blank "  *  " quote.', 'src-readme')).toEqual(['empty-quote']);
    expect(kinds(`${QUOTE_LEAD_IN} Tidemark is an in-memory cache.`, 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(kinds(`${QUOTE_LEAD_IN} "Tidemark is an in-memory cache."`, 'src-readme')).toEqual([]);
    expect(kinds(`${QUOTE_LEAD_IN} "Tidemark is an in-memory cache." Later: ${QUOTE_LEAD_IN} that it is fast.`, 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(kinds(`${QUOTE_LEAD_IN} that it is fast. Later: ${QUOTE_LEAD_IN} "Tidemark is an in-memory cache."`, 'src-readme')).toEqual(['lead-in-without-quote']);
    expect(kinds(`${QUOTE_LEAD_IN}   “Tidemark is an in-memory cache.”`, 'src-readme')).toEqual([]);
  });

  it('leaves text without quotes alone, and does not treat an apostrophe as a quote', () => {
    expect(kinds('The project\'s cache avoids lock contention; it doesn\'t block.', 'src-readme')).toEqual([]);
    expect(kinds('No quotes at all.')).toEqual([]);
  });

  it('truncates a long reported quote and names the block', () => {
    const [finding] = checkBlockQuotes({ id: 'long-block', text: `"${'x'.repeat(500)}"`, sourceIds: ['src-readme'] }, SOURCES);
    expect(finding).toMatchObject({ blockId: 'long-block', kind: 'quote-not-in-cited-sources' });
    expect(finding!.quote).toHaveLength(200);
  });
});
