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

describe('closed-pwb-code-context-v1 — vocabulary and empty input', () => {
  it('the malformation vocabulary is the policy notInert list minus the two non-context constructs', () => {
    expect([...MALFORMED_CODE_CONTEXTS]).toEqual(['unclosed-fence', 'unclosed-inline-span', 'backtick-fence-with-backtick-in-info-string']);
  });

  it('empty and context-free text mask to themselves', () => {
    expect(maskMarkdownCodeContexts('')).toEqual({ kind: 'masked', masked: '', fences: 0, spans: 0 });
    expect(masked('# Title\n\nplain\n')).toBe('# Title\n\nplain\n');
  });
});
