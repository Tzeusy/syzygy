// Characterization of the Markdown fence recognizers (syzygy-bpyt.6.3, the DC-3 fence-rule finding).
//
// Four production readers decide which lines sit inside a fenced block, and they do not share one rule:
//   profile     maskMarkdownCodeContexts (markdown-code-context.ts): PWB-REQ-006 "Code-context profile", the spec's own rule.
//   links       indexLinkTargets (project-shape-manifest.ts, stripFences): the index-link grammar's fences and code spans.
//   extraction  extractClass (project-shape-extraction.ts, parseDoc): headings, list items and tables outside fences.
//   renderer    renderPolarisMarkdown (polaris-markdown.ts): the presentation of admitted text.
// A fifth, outsideFences in polaris-generation-consent, is private; docs/evidence/syzygy-bpyt-6-3/fence-probe.mjs measures it.
//
// This file pins what each reader does today, so that merging or "fixing" a rule is a visible decision and not an accident.
// It decides nothing: the readers differ on purpose or by silence, and the record
// docs/evidence/syzygy-bpyt-6-3/dc3-fence-rules-2026-10-25.json says, per reader, which clause governs it and where it departs.
// Changing a row below changes what a gate accepts or refuses, which needs the owner (GP-Q0), and the record changes with it.
//
// A row is one case: its lines, then one string per reader. A string has one letter for each place a probe line can be
// inserted (before line 0, before line 1, ... after the last): V the probe line is outside every fence the reader
// recognizes, H it is inside one, M the profile calls the whole text malformed (an unclosed fence or span, or a backtick
// fence whose info string holds a backtick), X the active-content gate excludes a source with a script element at that
// place, A it admits it. The *Crlf columns give the same text with CRLF after every line. Expected values are literals.
import { describe, expect, it } from 'vitest';
import { extractClass, indexLinkTargets, maskMarkdownCodeContexts, scanActiveContent } from '@syzygy/three-surface-poc-core';
import { renderPolarisMarkdown } from './polaris-markdown.js';

const B = '```';
const T = '~~~';
const PROBE = '## PROBE [p](probe.md)';
const PAYLOAD = '<script>x</script>';

interface FenceCase {
  readonly id: string;
  readonly lines: readonly string[];
  readonly profile: string;
  readonly links: string;
  readonly extraction: string;
  readonly renderer: string;
  readonly profileCrlf: string;
  readonly gate: string;
  readonly gateCrlf: string;
}

const CASES: readonly FenceCase[] = [
  { id: 'backtick-col0', lines: [B, 'x', B], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'backtick-indent1', lines: [' ```', 'x', ' ```'], profile: 'VHHV', links: 'VHHV', extraction: 'VVVV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'backtick-indent2', lines: ['  ```', 'x', '  ```'], profile: 'VHHV', links: 'VHHV', extraction: 'VVVV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'backtick-indent3', lines: ['   ```', 'x', '   ```'], profile: 'VHHV', links: 'VHHV', extraction: 'VVVV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'backtick-indent4', lines: ['    ```', 'x', '    ```'], profile: 'VHHV', links: 'VVVV', extraction: 'VVVV', renderer: 'VVVV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'backtick-tab', lines: ['\t```', 'x', '\t```'], profile: 'VHHV', links: 'VHHV', extraction: 'VVVV', renderer: 'VVVV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'tilde-col0', lines: [T, 'x', T], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VVVV', gate: 'XAAX', gateCrlf: 'XXXX' },
  { id: 'tilde-indent3', lines: ['   ~~~', 'x', '   ~~~'], profile: 'VHHV', links: 'VHHV', extraction: 'VVVV', renderer: 'VHHV', profileCrlf: 'VVVV', gate: 'XAAX', gateCrlf: 'XXXX' },
  { id: 'tilde-indent4', lines: ['    ~~~', 'x', '    ~~~'], profile: 'VVVV', links: 'VVVV', extraction: 'VVVV', renderer: 'VVVV', profileCrlf: 'VVVV', gate: 'XXXX', gateCrlf: 'XXXX' },
  { id: 'opener-four-closer-three', lines: ['````', 'x', B, 'y', '````'], profile: 'VHHHHV', links: 'VHHHHV', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'VHHHHV', gate: 'XAAAAX', gateCrlf: 'XAAAAX' },
  { id: 'closer-longer', lines: [B, 'x', '````'], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'MMMM', gate: 'XAAX', gateCrlf: 'XXXX' },
  { id: 'closer-indent1', lines: [B, 'x', ' ```', 'y'], profile: 'VHHVV', links: 'VHHVV', extraction: 'VHHHH', renderer: 'VHHVV', profileCrlf: 'VHHVV', gate: 'XAAXX', gateCrlf: 'XAAXX' },
  { id: 'closer-indent3', lines: [B, 'x', '   ```', 'y'], profile: 'VHHVV', links: 'VHHVV', extraction: 'VHHHH', renderer: 'VHHVV', profileCrlf: 'VHHVV', gate: 'XAAXX', gateCrlf: 'XAAXX' },
  { id: 'closer-indent4', lines: [B, 'x', '    ```', 'y', B], profile: 'VHHHHV', links: 'VHHHHV', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'MMMMMM', gate: 'XAAAAX', gateCrlf: 'XXXXXX' },
  { id: 'closer-trailing-space', lines: [B, 'x', '``` '], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'closer-trailing-tab', lines: [B, 'x', '```\t'], profile: 'MMMM', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XXXX', gateCrlf: 'XAAX' },
  { id: 'closer-trailing-tab-then-closer', lines: [B, 'x', '```\t', 'y', B], profile: 'VHHHHV', links: 'VHHVVH', extraction: 'VHHVVH', renderer: 'VHHVVH', profileCrlf: 'MMMMMM', gate: 'XAAAAX', gateCrlf: 'XXXXXX' },
  { id: 'closer-with-info', lines: [B, 'x', '```js', 'y', B], profile: 'VHHHHV', links: 'VHHVVH', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'MMMMMM', gate: 'XAAAAX', gateCrlf: 'XXXXXX' },
  { id: 'closer-longer-with-info', lines: [B, '````js', 'y', B], profile: 'VHHHV', links: 'VHVVH', extraction: 'VHHHV', renderer: 'VHHHV', profileCrlf: 'VHHHV', gate: 'XAAAX', gateCrlf: 'XAAAX' },
  { id: 'closer-with-text', lines: [B, 'x', '``` text', 'y', B], profile: 'VHHHHV', links: 'VHHVVH', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'MMMMMM', gate: 'XAAAAX', gateCrlf: 'XXXXXX' },
  { id: 'closer-other-char', lines: [B, 'x', T, 'y', B], profile: 'VHHHHV', links: 'VHHHHV', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'VHHHHV', gate: 'XAAAAX', gateCrlf: 'XAAAAX' },
  { id: 'tilde-fence-backtick-line', lines: [T, 'x', B, 'y', T], profile: 'VHHHHV', links: 'VHHHHV', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'MMMMMM', gate: 'XAAAAX', gateCrlf: 'XXXXXX' },
  { id: 'tilde-opener-four-closer-three', lines: ['~~~~', 'x', T, 'y', '~~~~'], profile: 'VHHHHV', links: 'VHHHHV', extraction: 'VHHHHV', renderer: 'VHHHHV', profileCrlf: 'VVVVVV', gate: 'XAAAAX', gateCrlf: 'XXXXXX' },
  { id: 'info-string', lines: ['```js', 'x', B], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'info-string-space', lines: ['``` js', 'x', B], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'backtick-info-with-backtick', lines: ['```a`b', 'x', B], profile: 'MMMM', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'VHHV', gate: 'XXXX', gateCrlf: 'XAAX' },
  { id: 'tilde-info-with-backtick', lines: ['~~~a`b', 'x', T], profile: 'VHHV', links: 'VHHV', extraction: 'VHHV', renderer: 'VHHV', profileCrlf: 'MMMM', gate: 'XAAX', gateCrlf: 'XXXX' },
  { id: 'unclosed', lines: [B, 'x'], profile: 'MMM', links: 'VHH', extraction: 'VHH', renderer: 'VHH', profileCrlf: 'MMM', gate: 'XXX', gateCrlf: 'XXX' },
  { id: 'empty-fence', lines: [B, B], profile: 'VHV', links: 'VHV', extraction: 'VHV', renderer: 'VHV', profileCrlf: 'VHV', gate: 'XAX', gateCrlf: 'XAX' },
  { id: 'two-backticks', lines: ['``', 'x', '``'], profile: 'VHHV', links: 'VVVV', extraction: 'VVVV', renderer: 'VVVV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'blockquote', lines: ['> ```', '> x', '> ```'], profile: 'VHHV', links: 'VVVV', extraction: 'VVVV', renderer: 'VVVV', profileCrlf: 'VHHV', gate: 'XAAX', gateCrlf: 'XAAX' },
  { id: 'list-item', lines: ['- ```', '  x', '  ```'], profile: 'MMMM', links: 'VVVH', extraction: 'VVVV', renderer: 'VVVV', profileCrlf: 'VHHV', gate: 'XXXX', gateCrlf: 'XAAX' },
  { id: 'two-fences', lines: [B, 'x', B, T, 'y', T], profile: 'VHHVHHV', links: 'VHHVHHV', extraction: 'VHHVHHV', renderer: 'VHHVHHV', profileCrlf: 'VHHVVVV', gate: 'XAAXAAX', gateCrlf: 'XAAXXXX' },
];

// Inline code spans on one line, for the two readers that have a rule for them: V the link is outside a span, H inside one,
// M the profile calls the text malformed.
const INLINE_SPANS: readonly { readonly id: string; readonly line: string; readonly profile: string; readonly links: string }[] = [
  { id: 'no-span', line: 'see [p](probe.md)', profile: 'V', links: 'V' },
  { id: 'inside-span', line: '`[p](probe.md)`', profile: 'H', links: 'H' },
  { id: 'inside-double-span', line: '``[p](probe.md)``', profile: 'H', links: 'V' },
  { id: 'unclosed-span', line: '` [p](probe.md)', profile: 'M', links: 'V' },
  { id: 'link-between-spans', line: '`a` [p](probe.md) `b`', profile: 'V', links: 'V' },
  { id: 'double-span-with-inner-backtick-before-link', line: '`` a ` b `` [p](probe.md)', profile: 'V', links: 'V' },
  { id: 'double-span-with-inner-backtick-around-link', line: '``[p](probe.md) ` ``', profile: 'H', links: 'V' },
  { id: 'backslash-before-delimiters', line: '\\`[p](probe.md)\\`', profile: 'H', links: 'H' },
];

const joined = (lines: readonly string[], eol: string): string => lines.map((line) => line + eol).join('');
const atLine = (text: string, k: number): boolean => (text.split('\n')[k] ?? '').replace(/\r$/, '') === PROBE;

type Read = (text: string, k: number) => string;
const readers: Readonly<Record<'profile' | 'links' | 'extraction' | 'renderer', Read>> = {
  profile: (text, k) => {
    const mask = maskMarkdownCodeContexts(text);
    return mask.kind === 'malformed' ? 'M' : atLine(mask.masked, k) ? 'V' : 'H';
  },
  links: (text) => (indexLinkTargets(text).includes('probe.md') ? 'V' : 'H'),
  extraction: (text) => {
    const result = extractClass('project-account-section', 'architecture.md', text);
    return result.kind === 'items' && result.items.some((item) => (item.statement ?? '').includes('PROBE')) ? 'V' : 'H';
  },
  renderer: (text) => (renderPolarisMarkdown(text).includes('<h4>PROBE') ? 'V' : 'H'),
};
const gate: Read = (text) => (scanActiveContent(text).length > 0 ? 'X' : 'A');

function vector(read: Read, insert: string, lines: readonly string[], eol: string): string {
  let out = '';
  for (let k = 0; k <= lines.length; k += 1) out += read(joined([...lines.slice(0, k), insert, ...lines.slice(k)], eol), k);
  return out;
}

describe('Markdown fence recognizers: what each reader treats as inside a fence', () => {
  it.each(CASES)('$id', (c) => {
    const read = {
      profile: vector(readers.profile, PROBE, c.lines, '\n'),
      links: vector(readers.links, PROBE, c.lines, '\n'),
      extraction: vector(readers.extraction, PROBE, c.lines, '\n'),
      renderer: vector(readers.renderer, PROBE, c.lines, '\n'),
      profileCrlf: vector(readers.profile, PROBE, c.lines, '\r\n'),
      gate: vector(gate, PAYLOAD, c.lines, '\n'),
      gateCrlf: vector(gate, PAYLOAD, c.lines, '\r\n'),
    };
    for (const key of ['profile', 'links', 'extraction', 'renderer', 'profileCrlf', 'gate', 'gateCrlf'] as const) expect(read[key], `${c.id} ${key}`).toBe(c[key]);
  });

  it('the cases cover the population this file claims: 33 cases, 152 insertion places per reader', () => {
    expect(CASES).toHaveLength(33);
    expect(new Set(CASES.map((c) => c.id)).size).toBe(33);
    expect(CASES.reduce((n, c) => n + c.lines.length + 1, 0)).toBe(152);
    for (const c of CASES) for (const key of ['profile', 'links', 'extraction', 'renderer', 'profileCrlf', 'gate', 'gateCrlf'] as const) expect(c[key], `${c.id} ${key}`).toHaveLength(c.lines.length + 1);
  });

  it('links, extraction and the renderer read CRLF exactly as they read LF; only the profile does not', () => {
    for (const c of CASES) {
      for (const name of ['links', 'extraction', 'renderer'] as const) {
        expect(vector(readers[name], PROBE, c.lines, '\r\n'), `${c.id} ${name}`).toBe(c[name]);
      }
    }
    expect(CASES.filter((c) => c.profileCrlf !== c.profile).map((c) => c.id)).toHaveLength(14);
  });

  it.each(INLINE_SPANS)('inline span: $id', (c) => {
    const mask = maskMarkdownCodeContexts(c.line);
    const profile = mask.kind === 'malformed' ? 'M' : mask.masked.includes('[p](probe.md)') ? 'V' : 'H';
    expect({ profile, links: indexLinkTargets(c.line).includes('probe.md') ? 'V' : 'H' }).toEqual({ profile: c.profile, links: c.links });
  });

  // The renderer also uses its fence rule where the vector cannot see it: to end a paragraph, and to find the fragment's root heading.
  it('renderer: a fence line indented three spaces ends a paragraph, one indented four spaces does not', () => {
    expect(renderPolarisMarkdown('text\n   ' + B + '\nx\n   ' + B)).toBe('<p>text</p>\n<pre><code>x</code></pre>');
    expect(renderPolarisMarkdown('text\n    ' + B + '\nx')).toBe('<p>text\n    ' + B + '\nx</p>');
  });

  it('renderer: a closed fence does not hide the heading after it from the fragment root', () => {
    expect(renderPolarisMarkdown('### A\n\n' + B + '\nx\n' + B + '\n\n# B')).toBe('<h4>A</h4>\n<pre><code>x</code></pre>\n<h4>B</h4>');
  });

  // A gap, recorded and not decided: a line "```a`b" is a fence opener whether the CR counts as part of the line or as its
  // terminator, and a backtick opener's info text may hold no backtick, so the LF text is malformed and excluded. The opener
  // regex ends in `(.*)$`, `.` does not match CR, and the CRLF text is read as an inline span that hides the script element.
  // Changing this changes what a gate accepts; it needs the owner (GP-Q0) and this test changes with the decision.
  it('GAP: a CRLF source is admitted where the same LF source is excluded as a malformed code context', () => {
    const body = '```a`b\n<script>alert(1)</script>\n```\n';
    expect(scanActiveContent(body).map((f) => f.form)).toEqual(['malformed-code-context']);
    expect(scanActiveContent(body.replace(/\n/g, '\r\n'))).toEqual([]);
  });
});
