import { describe, expect, it } from 'vitest';
import { normaliseForQuote } from './quote-fidelity.js';
import { leadInQuotations, lineCount, locateQuote, normaliseTracked } from './quote-locate.js';

// syzygy-qkea.7 (S6): a quotation located in a file after the quote check's normalisation, with its byte range (design "Byte ranges from a
// normalised match"). Every expected range is found here by a plain byte search for a literal raw span of the fixture text, never from
// the module under test.

const bytesOf = (raw: string, span: string, from = 0): [number, number] => {
  const buffer = Buffer.from(raw, 'utf8');
  const at = buffer.indexOf(Buffer.from(span, 'utf8'), from);
  if (at < 0) throw new Error(`fixture: ${span} not in the raw text`);
  return [at, at + Buffer.byteLength(span, 'utf8')];
};
const locate = (raw: string, quote: string, start: number, end: number) => locateQuote(raw, normaliseTracked(raw), quote, start, end);

describe('the tracked normalisation', () => {
  it.each([
    ['comment leaders and closers', '/* The server\n * accepts **connections**.\n */\n// one thread\n# shell too\n'],
    ['links, images, entities and escapes', 'See [the guide](https://example.invalid/x) and ![logo][ref]; a &amp; b &#x41;&#66; &bogus; \\*not\\* `code`.'],
    ['emphasis at word edges only', '**bold** and _em_ but active_expire and *p stay; __both__ *x*'],
    ['curly quotes, ellipsis and whitespace', '“quoted” it’s…  done\t\tnow\n\n\nend  '],
    ['CR LF and lone CR', '// first\r\n// second\rthird\r\n'],
    ['a line separator is not a line break', 'a // not a leader b'],
    ['a byte-order mark and astral characters', '﻿// \u{1F600} smile &#128512; done'],
    ['nothing but whitespace', '  \n\t '],
    ['empty', ''],
  ])('produces exactly normaliseForQuote for %s', (_name, raw) => {
    const tracked = normaliseTracked(raw);
    expect(tracked.text).toBe(normaliseForQuote(raw));
    expect(tracked.start).toHaveLength(tracked.text.length);
    for (let i = 0; i < tracked.text.length; i++) {
      expect(tracked.start[i]).toBeLessThan(tracked.end[i]!);
      if (i > 0) expect(tracked.start[i]).toBeGreaterThanOrEqual(tracked.start[i - 1]!);
    }
  });
});

const SOURCE = [
  '/* Kestrel keeps every key in memory.',          // 1
  ' * Each command **runs to completion** before',  // 2
  ' * the next one starts. */',                      // 3
  'int main(void) { return 0; }',                   // 4
  '// Café über: snapshots are written periodically.', // 5
  '// Redis-compatible clients connect.',           // 6
  '',
].join('\n');

describe('locating a quotation', () => {
  it('finds an exact span and gives its byte range', () => {
    expect(locate(SOURCE, 'Kestrel keeps every key in memory.', 1, 1)).toEqual({ found: true, byteStart: bytesOf(SOURCE, 'Kestrel')[0], byteEnd: bytesOf(SOURCE, 'memory.')[1] });
  });

  it('matches across comment leaders and emphasis, and the range runs from the first raw character to the last', () => {
    expect(locate(SOURCE, 'Each command runs to completion before the next one starts.', 2, 3)).toEqual({
      found: true, byteStart: bytesOf(SOURCE, 'Each command')[0], byteEnd: bytesOf(SOURCE, 'one starts.')[1],
    });
  });

  it('counts bytes, not characters, after multibyte text', () => {
    expect(locate(SOURCE, 'snapshots are written periodically.', 5, 5)).toEqual({ found: true, byteStart: bytesOf(SOURCE, 'snapshots')[0], byteEnd: bytesOf(SOURCE, 'periodically.')[1] });
  });

  it.each<[string, string, number, number, string]>([
    ['an altered quotation', 'Kestrel keeps every key on disk.', 1, 1, 'quotation-not-in-cited-file'],
    ['a joined quotation', 'Kestrel keeps every key in memory. Redis-compatible clients connect.', 1, 6, 'quotation-not-in-cited-file'],
    ['an elided quotation', 'Kestrel keeps ... in memory.', 1, 1, 'quotation-elided'],
    ['a quotation found only outside its cited range', 'snapshots are written periodically.', 1, 4, 'quotation-outside-range'],
    ['a quotation straddling the end of its range', 'Each command runs to completion before the next one starts.', 2, 2, 'quotation-outside-range'],
    ['a piece of a word', 'edis-compatible', 1, 6, 'quotation-not-in-cited-file'],
    ['an empty quotation', ' `` ', 1, 6, 'quotation-empty'],
    ['a range past the end of the text', 'Kestrel keeps every key in memory.', 7, 9, 'quotation-outside-range'],
  ])('refuses %s', (_name, quote, start, end, kind) => {
    expect(locate(SOURCE, quote, start, end)).toEqual({ found: false, kind });
  });

  it('keeps the raw origin of text a step carries over: a quotation inside a link\'s text spans only that text', () => {
    const raw = 'See [the guide](https://example.invalid/a) and \\*stars\\* now.\n';
    expect(locate(raw, 'the guide', 1, 1)).toEqual({ found: true, byteStart: bytesOf(raw, 'the guide')[0], byteEnd: bytesOf(raw, 'the guide')[1] });
    expect(locate(raw, 'stars', 1, 1)).toEqual({ found: true, byteStart: bytesOf(raw, 'stars')[0], byteEnd: bytesOf(raw, 'stars')[1] });
  });

  it('takes the first occurrence inside the range when the span repeats', () => {
    const raw = 'alpha beta\nalpha beta\nalpha beta\n';
    const second = bytesOf(raw, 'alpha beta', 1);
    expect(locate(raw, 'alpha beta', 2, 3)).toEqual({ found: true, byteStart: second[0], byteEnd: second[1] });
  });

  it('keeps a byte-order mark in the byte count', () => {
    const raw = '﻿hello world\n';
    expect(locate(raw, 'hello world', 1, 1)).toEqual({ found: true, byteStart: 3, byteEnd: 14 });
  });

  it('measures lines with CR LF, CR and a final terminator', () => {
    expect([lineCount(''), lineCount('a'), lineCount('a\n'), lineCount('a\r\nb'), lineCount('a\rb\r\n'), lineCount('\n\n')]).toEqual([0, 1, 1, 2, 2, 2]);
    expect(locate('one\r\ntwo three\r\n', 'two three', 2, 2)).toEqual({ found: true, byteStart: 5, byteEnd: 14 });
  });
});

describe('the quotations a block carries', () => {
  it('reads each lead-in quotation, its closing quote the last before the next lead-in', () => {
    expect(leadInQuotations('The project states: "a "b" c" and so. The project states:  "d" end')).toEqual([
      { terminated: true, inner: 'a "b" c' }, { terminated: true, inner: 'd' },
    ]);
  });

  it('reports a lead-in with no straight quote and a quotation never closed, and ignores quotes without a lead-in', () => {
    expect(leadInQuotations('The project states: “x”. Then "prose". The project states: "open')).toEqual([
      { terminated: false, kind: 'lead-in-without-quote' }, { terminated: false, kind: 'quotation-unterminated' },
    ]);
    expect(leadInQuotations('They call it "fast".')).toEqual([]);
  });
});
