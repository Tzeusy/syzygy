// Markdown code-context mask — the policy's `closed-pwb-code-context-v1`
// profile (2026-09-05 policy amendment, `activeContentClassification.
// markdownProfile`; PWB-REQ-006 as amended by the truth-and-readiness
// amendment).
//
// The mask exists for one consumer: active-content detection. Bytes wholly
// inside a syntactically closed inline code span or fenced code block are
// inert Markdown contexts — markup-like examples there never alone exclude
// a source and are never interpreted as markup or a link. Secret detectors
// never see the mask: they scan the complete transient text (the policy's
// `precedence` clause and PWB-REQ-006 "the context mask SHALL affect only
// active-content detection, never secret scans").
//
// The profile is UTF-8 line-oriented and closed:
//
//   fenced opener  zero to three spaces, then at least three identical
//                  backticks or tildes; a backtick opener's info string
//                  contains no backtick (else malformed);
//   fenced closer  zero to three spaces, the opener character repeated at
//                  least the opener length, then spaces only; the first
//                  qualifying closer ends the fence;
//   inline opener  outside a fence, a run of one or more backticks;
//   inline closer  the next run of exactly the opener length; runs of a
//                  different length are content and a backslash does not
//                  escape a delimiter;
//   precedence     fenced context is recognized before inline context;
//   not inert      indented code, HTML `<code>` elements and every other
//                  construct — they are ordinary text to the scan.
//
// An unclosed fence, an unclosed inline span or a backtick fence whose
// info string contains a backtick is a malformed context; the policy's
// `malformedContextAction` is exclude-whole-artifact, which the reader
// reports as its own active-content form. This module decides only the
// mask and the malformation reason; it retains nothing.

export const MALFORMED_CODE_CONTEXTS = [
  'unclosed-fence',
  'unclosed-inline-span',
  'backtick-fence-with-backtick-in-info-string',
] as const;
export type MalformedCodeContext = (typeof MALFORMED_CODE_CONTEXTS)[number];

export type CodeContextMask =
  | {
      readonly kind: 'masked';
      // `text` with every byte inside a closed code context (delimiters
      // included) replaced by a space; newlines are kept, so every
      // line/column position of the masked text equals the original's.
      readonly masked: string;
      readonly fences: number;
      readonly spans: number;
    }
  | {
      readonly kind: 'malformed';
      readonly reason: MalformedCodeContext;
      // 1-based line where the malformed context opened.
      readonly line: number;
    };

const FENCE_OPENER = /^ {0,3}(`{3,}|~{3,})(.*)$/;

function fenceCloser(line: string, char: string, length: number): boolean {
  const match = /^ {0,3}(`{3,}|~{3,}) *$/.exec(line);
  if (match === null) return false;
  const run = match[1] ?? '';
  return run[0] === char && run.length >= length;
}

// Replaces every character except `\n` by a space, so positions survive.
function blank(segment: string): string {
  return segment.replace(/[^\n]/g, ' ');
}

export function maskMarkdownCodeContexts(text: string): CodeContextMask {
  const lines = text.split('\n');
  const out: string[] = [];
  let fences = 0;
  let spans = 0;
  let fence: { readonly char: string; readonly length: number; readonly line: number } | undefined;
  let span: { readonly length: number; readonly line: number } | undefined;
  // Lines of the open fence so far; blanked as a whole when it closes.
  let pending: string[] = [];

  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index] ?? '';
    const lineNumber = index + 1;

    if (fence !== undefined) {
      pending.push(line);
      if (fenceCloser(line, fence.char, fence.length)) {
        out.push(...pending.map(blank));
        pending = [];
        fence = undefined;
        fences += 1;
      }
      continue;
    }

    // Fenced context is recognized before inline context: a fence opener
    // line is a fence even while an inline span is open, which leaves that
    // span unclosed (malformed) rather than swallowing the fence.
    const opener = FENCE_OPENER.exec(line);
    if (opener !== null) {
      if (span !== undefined) return { kind: 'malformed', reason: 'unclosed-inline-span', line: span.line };
      const run = opener[1] ?? '';
      const info = opener[2] ?? '';
      if (run[0] === '`' && info.includes('`')) {
        return { kind: 'malformed', reason: 'backtick-fence-with-backtick-in-info-string', line: lineNumber };
      }
      fence = { char: run[0] ?? '`', length: run.length, line: lineNumber };
      pending = [line];
      continue;
    }

    // Inline scan over this line, continuing an open span from a previous
    // line if any.
    let cursor = 0;
    let rendered = '';
    while (cursor < line.length) {
      if (line[cursor] !== '`') {
        rendered += span === undefined ? line[cursor] : ' ';
        cursor += 1;
        continue;
      }
      let end = cursor;
      while (end < line.length && line[end] === '`') end += 1;
      const runLength = end - cursor;
      if (span === undefined) {
        span = { length: runLength, line: lineNumber };
        rendered += ' '.repeat(runLength);
      } else if (runLength === span.length) {
        span = undefined;
        spans += 1;
        rendered += ' '.repeat(runLength);
      } else {
        rendered += ' '.repeat(runLength);
      }
      cursor = end;
    }
    out.push(rendered);
  }

  if (fence !== undefined) return { kind: 'malformed', reason: 'unclosed-fence', line: fence.line };
  if (span !== undefined) return { kind: 'malformed', reason: 'unclosed-inline-span', line: span.line };
  return { kind: 'masked', masked: out.join('\n'), fences, spans };
}
