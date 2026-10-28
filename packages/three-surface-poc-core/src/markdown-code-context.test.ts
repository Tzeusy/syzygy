// The policy's `closed-pwb-code-context-v1` profile, clause by clause
// (2026-09-05 policy amendment; PWB-REQ-006 as amended). Expected values are
// hand-typed literals.

import { describe, expect, it } from 'vitest';

import { MALFORMED_CODE_CONTEXTS, maskMarkdownCodeContexts } from './markdown-code-context.js';

function masked(text: string): string {
  const mask = maskMarkdownCodeContexts(text);
  if (mask.kind !== 'masked') throw new Error(`malformed: ${mask.reason}`);
  return mask.masked;
}

function malformed(text: string): { readonly reason: string; readonly line: number } {
  const mask = maskMarkdownCodeContexts(text);
  if (mask.kind !== 'malformed') throw new Error('expected a malformed context');
  return { reason: mask.reason, line: mask.line };
}

describe('closed-pwb-code-context-v1 — fenced code blocks', () => {
  it('a closed backtick fence is blanked, delimiters included, keeping every newline and length', () => {
    const text = 'before\n```html\n<div>\n```\nafter';
    expect(masked(text)).toBe('before\n       \n     \n   \nafter');
    expect(masked(text)).toHaveLength(text.length);
    expect(maskMarkdownCodeContexts(text)).toMatchObject({ fences: 1, spans: 0 });
  });

  it('an opener may be indented zero to three spaces; at four the backticks are inline runs, not a fence', () => {
    expect(masked('   ```\n<x>\n   ```')).toBe('      \n   \n      ');
    // Four spaces: no fence, so the two runs open and close one inline span
    // (fences: 0, spans: 1) — the profile has no indented-code context.
    expect(maskMarkdownCodeContexts('    ```\n<x>\n    ```')).toEqual({ kind: 'masked', masked: '       \n   \n       ', fences: 0, spans: 1 });
    expect(maskMarkdownCodeContexts('    ``` js\n<x>')).toMatchObject({ kind: 'malformed', reason: 'unclosed-inline-span', line: 1 });
  });

  it('tildes fence too, and a tilde opener info string may contain a backtick', () => {
    expect(masked('~~~ a`b\n<x>\n~~~')).toBe('       \n   \n   ');
  });

  it('a backtick opener info string with a backtick is malformed', () => {
    expect(malformed('```js `x`\n<x>\n```')).toEqual({ reason: 'backtick-fence-with-backtick-in-info-string', line: 1 });
  });

  it('a closer must repeat the opener character at least the opener length, then spaces only', () => {
    expect(masked('````\n```\n<x>\n````   ')).toBe('    \n   \n   \n       ');
    expect(malformed('````\n<x>\n```')).toEqual({ reason: 'unclosed-fence', line: 1 });
    expect(malformed('```\n<x>\n``` end')).toEqual({ reason: 'unclosed-fence', line: 1 });
    expect(malformed('```\n<x>\n~~~')).toEqual({ reason: 'unclosed-fence', line: 1 });
    expect(masked('```\n<x>\n`````')).toBe('   \n   \n     ');
  });

  it('the first qualifying closer ends the fence; text after it is scanned again', () => {
    expect(masked('```\n<a>\n```\n<b>\n```\n<c>\n```')).toBe('   \n   \n   \n<b>\n   \n   \n   ');
  });

  it('a fence opener line inside a fence is content, never a nested opener', () => {
    expect(masked('~~~\n```\n<x>\n~~~')).toBe('   \n   \n   \n   ');
  });

  it('an unclosed fence at end of text is malformed at its opener line', () => {
    expect(malformed('a\nb\n```\nnever')).toEqual({ reason: 'unclosed-fence', line: 3 });
  });
});

describe('closed-pwb-code-context-v1 — inline code spans', () => {
  it('a closed span is blanked, delimiters included, in place', () => {
    expect(masked('use `<br>` here')).toBe('use        here');
    expect(masked('a ``<b>`` c')).toBe('a         c');
    expect(maskMarkdownCodeContexts('`a` `b`')).toMatchObject({ fences: 0, spans: 2 });
  });

  it('the closer is exactly the opener length; other runs are content', () => {
    expect(masked('``a ` b``')).toBe('         ');
    expect(malformed('`` a ` b')).toEqual({ reason: 'unclosed-inline-span', line: 1 });
    expect(malformed('` a `` b')).toEqual({ reason: 'unclosed-inline-span', line: 1 });
  });

  it('a backslash does not escape a delimiter', () => {
    expect(masked('`a\\` b')).toBe('     b');
    expect(malformed('\\`a')).toEqual({ reason: 'unclosed-inline-span', line: 1 });
  });

  it('a span may continue across a line break, keeping the newline', () => {
    expect(masked('x `a\nb` y')).toBe('x   \n   y');
  });

  it('an unclosed span is malformed at the line it opened', () => {
    expect(malformed('ok\ntext `open\nstill')).toEqual({ reason: 'unclosed-inline-span', line: 2 });
  });

  it('a fence opener line is recognized before an open inline span, which then never closes', () => {
    expect(malformed('a `b\n```\nc`\n```')).toEqual({ reason: 'unclosed-inline-span', line: 1 });
  });

  it('HTML code elements and indented code are ordinary text', () => {
    expect(masked('<code>&lt;x&gt;</code>')).toBe('<code>&lt;x&gt;</code>');
    expect(masked('p\n\n    <div>')).toBe('p\n\n    <div>');
  });
});

// syzygy-bpyt.16, ruled on syzygy-bpyt.1.14 ("Arm (a) + bare CR"): CRLF, a bare CR and LF each end one line, and the mask keeps every
// terminator where it stands. A CRLF or CR text then gets exactly the decision its LF form gets. The expected values below are
// hand-typed literals; the one test that compares a rendering with another says so.
describe('closed-pwb-code-context-v1 — CRLF, CR and LF each end one line', () => {
  const ENDS: readonly (readonly [string, string])[] = [['LF', '\n'], ['CRLF', '\r\n'], ['CR', '\r']];
  const SCRIPT = '<script>x</script>';
  const lines = (...parts: readonly string[]) => (end: string): string => parts.map((part) => part + end).join('');
  // Every character that is not a line terminator becomes a dot: equal skeletons mean the same length and each CR and LF at its offset.
  const skeleton = (text: string): string => text.replace(/[^\r\n]/g, '.');

  it.each(ENDS)('%s: a backtick opener whose info string holds a backtick is malformed at its own line', (_name, end) => {
    expect(malformed(['# T', '```a`b', SCRIPT, '```'].join(end))).toEqual({ reason: 'backtick-fence-with-backtick-in-info-string', line: 2 });
  });

  // A line number counts each terminator once: a mask that read CRLF as two line ends would report 5 here, and 7 for the last text.
  it.each(ENDS)('%s: the reported line counts each line end once', (_name, end) => {
    expect(malformed(['a', 'b', '```', 'never'].join(end))).toEqual({ reason: 'unclosed-fence', line: 3 });
    expect(malformed(['ok', 'text `open', 'still'].join(end))).toEqual({ reason: 'unclosed-inline-span', line: 2 });
    expect(malformed(['a', '', '', '```a`b'].join(end))).toEqual({ reason: 'backtick-fence-with-backtick-in-info-string', line: 4 });
  });

  it('mixed terminators: each one ends one line, whichever kind it is', () => {
    expect(malformed('a\r\nb\n```\rnever')).toEqual({ reason: 'unclosed-fence', line: 3 });
    expect(malformed('a\r\n\r\n\r\n```')).toEqual({ reason: 'unclosed-fence', line: 4 });
    expect(malformed('a\r\rb\n\n`open\r\n')).toEqual({ reason: 'unclosed-inline-span', line: 5 });
    // An LF opener with a CRLF closer, and the other way round: the fence closes at the first qualifying closer either way.
    expect(masked('```\n<x>\r\n```\r\nafter')).toBe('   \n   \r\n   \r\nafter');
    expect(masked('```\r\n<x>\n```\nafter')).toBe('   \r\n   \n   \nafter');
  });

  it('the mask keeps the length and every CR and LF at its offset (a CR is never blanked, joined to LF or dropped)', () => {
    const text = 'a\r\n```\r\nx\ry\n```\rb\r\n';
    expect(maskMarkdownCodeContexts(text)).toEqual({ kind: 'masked', masked: 'a\r\n   \r\n \r \n   \rb\r\n', fences: 1, spans: 0 });
    expect(masked('x `a\rb` y')).toBe('x   \r   y');
    expect(masked('x `a\r\nb` y')).toBe('x   \r\n   y');
    expect(masked('`a`\r\r\n\n')).toBe('   \r\r\n\n');
  });

  it.each(ENDS)('%s: a fence closed on the last line, with no final line end, is closed', (_name, end) => {
    expect(masked(['```', '<x>', '```'].join(end))).toBe(['   ', '   ', '   '].join(end));
    expect(maskMarkdownCodeContexts(['~~~', '<x>', '~~~'].join(end))).toMatchObject({ kind: 'masked', fences: 1, spans: 0 });
  });

  it.each(ENDS)('%s: a tilde fence, a closer with trailing spaces and a span across lines', (_name, end) => {
    expect(masked(lines('~~~', '<x>', '~~~', 'after')(end))).toBe(lines('   ', '   ', '   ', 'after')(end));
    expect(masked(lines('```', '<x>', '```   ', 'after')(end))).toBe(lines('   ', '   ', '      ', 'after')(end));
    expect(masked(lines('x `a', 'b` y')(end))).toBe(lines('x   ', '   y')(end));
  });

  // "- ```" is not a fence opener (a list marker precedes the run), so its run opens an inline span, and the fence-shaped line two
  // lines on is recognized before inline context and leaves that span unclosed.
  it.each(ENDS)('%s: a backtick run after a list marker opens an inline span that a later fence-shaped line leaves unclosed', (_name, end) => {
    expect(malformed(lines('- ```', '  <x>', '  ```', 'after')(end))).toEqual({ reason: 'unclosed-inline-span', line: 1 });
  });

  // The two shapes of the fail-open class named by the review of syzygy-bpyt.6.3 (N2): two tilde fences that each show a lone
  // backtick-fence line, and a closer-shaped line followed by text. Each is excluded (or malformed) on LF; CRLF read them as admitted.
  it.each(ENDS)('%s: a script element between two tilde fences that each show a backtick-fence line is outside every context', (_name, end) => {
    const text = lines('~~~', '```', '~~~', SCRIPT, '~~~', '```', '~~~')(end);
    expect(maskMarkdownCodeContexts(text)).toEqual({ kind: 'masked', masked: lines('   ', '   ', '   ', SCRIPT, '   ', '   ', '   ')(end), fences: 2, spans: 0 });
  });

  it.each(ENDS)('%s: a closer followed by text does not close, so the fence is unclosed', (_name, end) => {
    expect(malformed(lines('```', SCRIPT, '``` text')(end))).toEqual({ reason: 'unclosed-fence', line: 1 });
    expect(malformed(lines('```', 'code', '```\t', 'after')(end))).toEqual({ reason: 'unclosed-fence', line: 1 });
    expect(malformed(lines('```', 'code', '    ```', 'after')(end))).toEqual({ reason: 'unclosed-fence', line: 1 });
  });

  // Only CR and LF end a line, which leaves every LF reading as it was (syzygy-bpyt.1.14): U+2028, U+2029 and U+0085 are line
  // content, blanked inside a span like any other character. A line end widened to them would keep them in the mask.
  it('U+2028, U+2029 and U+0085 are line content, not line ends', () => {
    for (const separator of ['\u2028', '\u2029', '\u0085']) expect(masked(`a \`b${separator}c\` d`), JSON.stringify(separator)).toBe('a       d');
  });

  // The same three at a fence position: a closer followed by a separator is a closer followed by text, so the fence stays unclosed.
  it('U+2028, U+2029 and U+0085 after a closing fence are line content: the fence stays unclosed', () => {
    for (const separator of ['\u2028', '\u2029', '\u0085']) expect(malformed(['```', 'x', '```' + separator].join('\n')), JSON.stringify(separator)).toEqual({ reason: 'unclosed-fence', line: 1 });
  });

  // Every other UTF-16 code unit is line content too, so a line end widened past the three above (VT, FF, or U+001C to U+001E as
  // Python's str.splitlines reads them) fails here; the failure lists, in hex, each unit the mask kept as a line end.
  it('no code unit but CR and LF ends a line', () => {
    const kept: string[] = [];
    for (let unit = 0; unit <= 0xffff; unit += 1) {
      if (unit === 0x0a || unit === 0x0d || unit === 0x60) continue;
      const mask = maskMarkdownCodeContexts(`a \`b${String.fromCharCode(unit)}c\` d`);
      if (mask.kind !== 'masked' || mask.masked !== 'a       d') kept.push(unit.toString(16));
    }
    expect(kept).toEqual([]);
  });

  // This test compares a rendering with another, so it proves equality, not correctness: the literals above and the fixtures at the
  // call sites pin the values.
  it('a CRLF or CR text gets the structure its LF form gets, for every case here', () => {
    const CASES: readonly (readonly string[])[] = [
      ['```', SCRIPT, '```', 'after'],
      ['```', 'code', '```\t', SCRIPT],
      ['- ```', SCRIPT, '  ```'],
      ['~~~ a`b', SCRIPT, '~~~'],
      ['```', 'use ``` here', '```', SCRIPT],
      ['````', '`````', SCRIPT],
      ['a `b', '```', SCRIPT, '```', 'c` d'],
      ['~~~', SCRIPT],
      ['```a`b', SCRIPT, '```'],
      ['~~~', '```', '~~~', SCRIPT, '~~~', '```', '~~~'],
      ['> ```', SCRIPT, '> ```'],
      ['```', 'a', '```', 'mid', '~~~', 'b', '~~~', 'end'],
    ];
    for (const parts of CASES) {
      const lf = maskMarkdownCodeContexts(lines(...parts)('\n'));
      for (const [name, end] of ENDS) {
        const text = lines(...parts)(end);
        const got = maskMarkdownCodeContexts(text);
        expect(got.kind, `${name} ${parts.join('|')}`).toBe(lf.kind);
        if (lf.kind === 'malformed' && got.kind === 'malformed') expect({ reason: got.reason, line: got.line }, `${name} ${parts.join('|')}`).toEqual({ reason: lf.reason, line: lf.line });
        if (lf.kind === 'masked' && got.kind === 'masked') {
          expect(got.masked, `${name} ${parts.join('|')}`).toBe(lf.masked.replace(/\n/g, end));
          expect([got.fences, got.spans]).toEqual([lf.fences, lf.spans]);
          expect(skeleton(got.masked)).toBe(skeleton(text));
        }
      }
    }
  });
});

describe('closed-pwb-code-context-v1 — vocabulary and empty input', () => {
  it('the malformation vocabulary is the policy notInert list minus the two non-context constructs', () => {
    expect([...MALFORMED_CODE_CONTEXTS]).toEqual(['unclosed-fence', 'unclosed-inline-span', 'backtick-fence-with-backtick-in-info-string']);
  });

  it('empty and context-free text mask to themselves', () => {
    expect(maskMarkdownCodeContexts('')).toEqual({ kind: 'masked', masked: '', fences: 0, spans: 0 });
    expect(masked('# Title\n\nplain\n')).toBe('# Title\n\nplain\n');
  });
});

// GP-B2 Q1 (syzygy-bpyt.1.18): the closed fence is blanked line by line, not by one spread call whose argument count is the fence's line
// count. A call that spreads 125,285 lines or more overflows the stack on node 24 with the default stack, whatever the line end.
describe('a very long closed fence', () => {
  const LONG_ENDS: readonly (readonly [string, string])[] = [['LF', '\n'], ['CRLF', '\r\n'], ['CR', '\r']];
  const LINES = 200_000;

  it.each(LONG_ENDS)('%s: 200,000 lines are blanked, every line end and the text after the fence kept', (_name, end) => {
    const text = `\`\`\`${end}${`x${end}`.repeat(LINES)}\`\`\`${end}after`;
    const got = maskMarkdownCodeContexts(text);
    expect(got.kind).toBe('masked');
    if (got.kind !== 'masked') return;
    expect([got.fences, got.spans]).toEqual([1, 0]);
    // Booleans, not toBe: a failing diff of a 600 KB string is unreadable.
    expect(got.masked === `   ${end}${` ${end}`.repeat(LINES)}   ${end}after`).toBe(true);
  });

  it.each(LONG_ENDS)('%s: a script element inside the fence is blanked, and the line after the fence keeps its own', (_name, end) => {
    const text = `\`\`\`${end}<script>${end}${`x${end}`.repeat(LINES)}\`\`\`${end}<script>`;
    const got = maskMarkdownCodeContexts(text);
    expect(got.kind).toBe('masked');
    if (got.kind !== 'masked') return;
    expect(got.masked.endsWith(`${end}<script>`)).toBe(true);
    expect(got.masked.slice(0, got.masked.length - 8).trim()).toBe('');
  });

  it.each(LONG_ENDS)('%s: the same lines left unclosed are still malformed at the opener', (_name, end) => {
    const text = `\`\`\`${end}${`x${end}`.repeat(LINES)}`;
    expect(malformed(text)).toEqual({ reason: 'unclosed-fence', line: 1 });
  });
});
