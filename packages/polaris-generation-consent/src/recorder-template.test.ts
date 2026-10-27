import vm from 'node:vm';
import { beforeAll, describe, expect, it } from 'vitest';
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

/** The line slot before syzygy-bpyt.8.17, held as a literal to compare against: the same lines, read once per non-space character. */
const AMBIGUOUS_LINE = '[^\\r\\n]*\\S[^\\r\\n]*';
/** `run()`, stopped by a throw once it has run `ms` milliseconds: V8 interrupts a regular expression that is still backtracking. */
const within = <T>(ms: number, run: () => T): T => vm.runInNewContext('run()', { run }, { timeout: ms }) as T;
/** Every sequence of `alphabet`'s members up to `max` long. */
function sequences(alphabet: readonly string[], max: number): string[] {
  const all = [''];
  let layer = [''];
  for (let n = 1; n <= max; n += 1) {
    layer = layer.flatMap(prefix => alphabet.map(c => prefix + c));
    for (const s of layer) all.push(s);
  }
  return all;
}
/** A seeded generator (mulberry32), so a failing case replays. */
function seeded(seed: number): () => number {
  let a = seed;
  return () => {
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const pick = <T>(rnd: () => number, from: readonly T[]): T => from[Math.floor(rnd() * from.length)]!;

describe('the line slot (syzygy-bpyt.8.17)', () => {
  const whole = (pattern: string) => new RegExp(`^(?:${pattern})$`, 'u');
  /** The texts the two patterns judge differently, as JSON strings; the ambiguous pattern runs under a timeout. */
  const disagreements = (texts: readonly string[]): string[] => {
    const fresh = whole(SLOT.line), ambiguous = whole(AMBIGUOUS_LINE);
    const before = within(20_000, () => texts.map(text => ambiguous.test(text)));
    return texts.filter((text, i) => fresh.test(text) !== before[i]).map(text => JSON.stringify(text));
  };
  // Every space but CR and LF, as the engine reads `\s` under the `u` flag (built here, so a throw fails the tests).
  let blanks: string[] = [];
  beforeAll(() => {
    blanks = [];
    for (let c = 0; c <= 0xffff; c += 1) if (c !== 0x0a && c !== 0x0d && /^\s$/u.test(String.fromCharCode(c))) blanks.push(String.fromCharCode(c));
  });

  it('accepts exactly the lines the ambiguous pattern accepts, over every string of up to four of sixteen characters', () => {
    // Breaks (CR, LF), spaces of each kind (`\s` but not a break: tab, VT, FF, NBSP, the line and paragraph separators, the ideographic
    // space, ZWNBSP) and non-spaces (NEL and ZWSP are not `\s`; an astral character and a lone surrogate are one code point each).
    const alphabet = ['x', ' ', '\t', '\v', '\f', '\r', '\n', '\u0085', '\u00a0', '\u200b', '\u2028', '\u2029', '\u3000', '\ufeff', '\u{1F600}', '\ud800'];
    const texts = sequences(alphabet, 4);
    expect(texts).toHaveLength(69_905);
    expect(disagreements(texts)).toEqual([]);
    // A line is break-free with a non-space: 14^n - 9^n of the strings of n characters, 33,990 in all.
    expect(texts.filter(text => whole(SLOT.line).test(text))).toHaveLength(33_990);
  });
  it('accepts exactly the lines the ambiguous pattern accepts, over every string of up to eight of a non-space, a space and both breaks', () => {
    const texts = sequences(['x', ' ', '\r', '\n'], 8);
    expect(disagreements(texts)).toEqual([]);
    expect(texts.filter(text => whole(SLOT.line).test(text))).toHaveLength(502);   // 2^n - 1 of the strings of n characters
  });
  it('accepts exactly the lines the ambiguous pattern accepts, over long random strings of every space the engine knows', () => {
    expect(blanks.length).toBeGreaterThan(20);
    const rnd = seeded(817), others = ['x', '\u00e9', '"', '|', '\u0085', '\u200b', '\u{1F600}', '\ud800', '\udc00'];
    const texts = Array.from({ length: 4000 }, () => {
      const solid = rnd() ** 3, length = Math.floor(rnd() * 160);
      return Array.from({ length }, () => {
        const r = rnd();
        return r < 0.004 ? pick(rnd, ['\r', '\n']) : r < solid ? pick(rnd, others) : pick(rnd, blanks);
      }).join('');
    });
    const accepted = texts.filter(text => whole(SLOT.line).test(text)).length;
    expect(accepted).toBeGreaterThan(400);
    expect(accepted).toBeLessThan(3600);
    expect(disagreements(texts)).toEqual([]);
  });
  it('reads the same slots as the ambiguous pattern from records that fill several slots, repeat one, or fail', () => {
    // Slots that meet on one line (split by a space, a tab, an ideographic space, or nothing) can be cut more than one way: both patterns
    // must cut them the same way, and a repeated slot must read back the same text.
    const templates = ['Owner selection: {a}\n', '{a} {b}\n', '{a}{b}', '| "{a}" | "{b}" |\nAgain: {a}\n', 'x: {a}\ny: {b}\nz: {c}\nEND\n', '{a}\u3000{b}\t{c}'];
    const rnd = seeded(8017), chars = ['x', 'y', ' ', ' ', '\t', '\u3000', '\u00a0', '"', '|'], edits = [...chars, '\r', '\n', ''];
    const value = () => Array.from({ length: 1 + Math.floor(rnd() * 8) }, () => pick(rnd, chars)).join('');
    let matched = 0, refused = 0;
    for (const source of templates) {
      const slots = (pattern: string) => Object.fromEntries(['a', 'b', 'c'].map(slot => [slot, pattern]));
      const fresh = recorderTemplate(source, slots(SLOT.line)), ambiguous = recorderTemplate(source, slots(AMBIGUOUS_LINE));
      const texts = Array.from({ length: 1500 }, () => {
        let text = fresh.render({ a: value(), b: value(), c: value() });
        // Half the texts are edited once or twice: a character inserted, or one replaced by a character or by nothing.
        for (let n = rnd() < 0.5 ? 0 : 1 + Math.floor(rnd() * 2); n > 0; n -= 1) {
          const at = Math.floor(rnd() * (text.length + 1));
          text = text.slice(0, at) + pick(rnd, edits) + text.slice(at + (rnd() < 0.5 ? 0 : 1));
        }
        return text;
      });
      const read = (t: RecorderTemplate, text: string) => JSON.stringify([t.fields(text), templateFields(t, text)]);
      const before = within(20_000, () => texts.map(text => read(ambiguous, text)));
      const differ = texts.flatMap((text, i) => (read(fresh, text) === before[i] ? [] : [`${JSON.stringify(source)} ${JSON.stringify(text)}: ${before[i]} became ${read(fresh, text)}`]));
      expect(differ).toEqual([]);
      for (const text of texts) if (templateFields(fresh, text) === null) refused += 1; else matched += 1;
    }
    expect(matched).toBeGreaterThan(1000);
    expect(refused).toBeGreaterThan(1000);
  });
  it('refuses a record that fails after four long line slots within a second', () => {
    // A long line of non-spaces gave the ambiguous pattern one way per character, multiplied across the slots before the failing
    // literal: on this record it ran for minutes (syzygy-bpyt.8.17 timing record). This pattern reads it in about a millisecond.
    const t = recorderTemplate('a: {a}\nb: {b}\nc: {c}\nd: {d}\nEND\n', { a: SLOT.line, b: SLOT.line, c: SLOT.line, d: SLOT.line });
    const record = ['a', 'b', 'c', 'd'].map(slot => `${slot}: ${'x'.repeat(160)}\n`).join('');
    expect(within(1000, () => templateFields(t, `${record}END\n`))).toEqual({ a: 'x'.repeat(160), b: 'x'.repeat(160), c: 'x'.repeat(160), d: 'x'.repeat(160) });
    expect(within(1000, () => templateFields(t, `${record}END!\n`))).toBeNull();
  });
});
