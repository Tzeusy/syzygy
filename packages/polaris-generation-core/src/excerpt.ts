/**
 * The excerpt a discovery map call sees for one file (REQ-polaris-generation-030).
 * Deterministic and literal: fixed line patterns, no parser, no model. The text is
 * file bytes only: whole source lines of the text it is handed (which the caller
 * takes from an admitted source), joined by a single "\n", never a line the
 * generator wrote. The kind, the quoted UTF-8 byte ranges and the skipped licence
 * range are metadata for the local run record and receipts; they are not part of
 * what is sent.
 *
 * Kinds (closed):
 *   head                 the first maxChars characters (the original behaviour)
 *   code-declarations    C-family: first top-level doc comment, then declaration lines
 *   code-after-licence   C-family, no declaration line found: opening text after the licence comment
 */

export const EXCERPT_KINDS = ['head', 'code-declarations', 'code-after-licence'] as const;
export type ExcerptKind = (typeof EXCERPT_KINDS)[number];
/** Byte ranges `[start, end)` of the blob the excerpt quotes, ascending and disjoint. */
export type ExcerptRange = readonly [number, number];
/** `licenceSkipped` is the byte range of the leading licence comment that was left out, or null. */
export interface Excerpt { readonly text: string; readonly kind: ExcerptKind; readonly ranges: readonly ExcerptRange[]; readonly licenceSkipped: ExcerptRange | null }

/** The doc comment may take at most this share of a code excerpt, in percent. */
export const DOC_COMMENT_SHARE_PERCENT = 40;
/** A declaration line longer than this is cut. */
export const DECLARATION_LINE_MAX = 160;
export const MAX_EXCERPT_RANGES = 512;

/** A leading comment is a licence block when it holds one of these, matched literally and case-sensitively. */
export const LICENCE_MARKERS = ['Copyright', 'SPDX-License-Identifier', 'Permission is hereby granted', 'Licensed under'] as const;
const C_FAMILY = ['.c', '.h', '.cc', '.cpp', '.cxx', '.hpp', '.hh', '.cu'] as const;
const HEADER_EXTENSIONS = ['.h', '.hpp', '.hh'] as const;

const DEFINE_LINE = /^#[ \t]*define[ \t]+[A-Za-z_][A-Za-z0-9_]*/u;
const TAG_LINE = /^(?:typedef[ \t]+)?(?:struct|enum|union)\b[^;()]*\{?[ \t]*$/u;
const FUNCTION_LINE = /^[A-Za-z_][A-Za-z0-9_ \t*]*[A-Za-z0-9_*][ \t]*\(/u;
const NOT_A_FUNCTION = /^(?:if|for|while|switch|return|else|do|case|goto|typedef|sizeof|define|include|extern)\b/u;

const extensionOf = (name: string): string => { const dot = name.lastIndexOf('.'); return dot <= 0 ? '' : name.slice(dot).toLowerCase(); };

/** Code-point-safe prefix of at most `max` characters. */
function cut(text: string, max: number): string {
  if (text.length <= max) return text;
  return [...text].slice(0, max).join('');
}

interface Line { readonly text: string; readonly start: number; readonly end: number }

/** Lines with UTF-8 byte offsets of their first and last byte + 1 (a trailing carriage return is not part of the text). */
function splitLines(body: string): Line[] {
  const out: Line[] = [];
  let byte = 0;
  for (const raw of body.split('\n')) {
    const text = raw.endsWith('\r') ? raw.slice(0, -1) : raw;
    const textBytes = Buffer.byteLength(text, 'utf8');
    out.push({ text, start: byte, end: byte + textBytes });
    byte += Buffer.byteLength(raw, 'utf8') + 1;
  }
  return out;
}

const hasMarker = (lines: readonly Line[]): boolean => lines.some(line => LICENCE_MARKERS.some(marker => line.text.includes(marker)));

/** Index just past a comment block that begins at `from` (a `/*` block up to its closing line, or a run of `//` lines), or -1. */
function commentEnd(lines: readonly Line[], from: number): number {
  const first = (lines[from]?.text ?? '').replace(/^\uFEFF/u, '');
  if (first.startsWith('/*')) {
    for (let j = from; j < lines.length; j++) if (lines[j]!.text.includes('*/')) return j + 1;
    return -1;
  }
  if (first.startsWith('//')) {
    let j = from;
    while (j < lines.length && lines[j]!.text.startsWith('//')) j++;
    return j;
  }
  return -1;
}

/** Skips blank lines and any run of leading comment blocks that carry a licence marker. Returns the first line kept. */
function skipLicence(lines: readonly Line[]): { readonly next: number; readonly skipped: ExcerptRange | null } {
  let i = 0, skipped: [number, number] | null = null;
  for (;;) {
    while (i < lines.length && lines[i]!.text.trim() === '') i++;
    const end = i < lines.length ? commentEnd(lines, i) : -1;
    if (end === -1 || !hasMarker(lines.slice(i, end))) return { next: i, skipped };
    skipped = [skipped?.[0] ?? lines[i]!.start, lines[end - 1]!.end];
    i = end;
  }
}

function mergeRanges(ranges: ExcerptRange[]): ExcerptRange[] {
  const out: [number, number][] = [];
  for (const [start, end] of ranges) {
    const last = out.at(-1);
    if (last !== undefined && start - last[1] <= 1) last[1] = end; else out.push([start, end]);
  }
  return out;
}

function codeExcerpt(path: string, body: string, base: number, maxChars: number): Excerpt | undefined {
  const lines = splitLines(body);
  const { next, skipped } = skipLicence(lines);
  const segments: { text: string; start: number; end: number }[] = [];
  let used = 0;
  /** Adds one whole source line (cut at the line limit) if it fits with its separator. */
  const add = (line: Line, limit: number = maxChars): boolean => {
    const text = cut(line.text, DECLARATION_LINE_MAX);
    const cost = text.length + (segments.length > 0 ? 1 : 0);
    if (used + cost > limit) return false;
    segments.push({ text, start: line.start, end: line.start + Buffer.byteLength(text, 'utf8') });
    used += cost;
    return true;
  };
  const isHeaderFile = (HEADER_EXTENSIONS as readonly string[]).includes(extensionOf(path.split('/').at(-1) ?? ''));
  let docTaken = false, structural = 0, declarations = 0;
  for (let i = next; i < lines.length && used < maxChars; i++) {
    const line = lines[i]!;
    if (!docTaken && structural === 0 && (line.text.startsWith('/*') || line.text.startsWith('//'))) {
      const end = commentEnd(lines, i);
      if (end !== -1) {
        docTaken = true;
        if (!hasMarker(lines.slice(i, end))) {
          const docLimit = Math.min(maxChars, Math.floor(maxChars * DOC_COMMENT_SHARE_PERCENT / 100));
          for (let j = i; j < end && add(lines[j]!, docLimit); j++);
        }
        i = end - 1;
        continue;
      }
    }
    const t = line.text;
    if (t === '') continue; // every pattern below is anchored at column zero, so indented lines, braces and comments never match
    const before = t.split('(')[0] ?? '';
    const isFunction = FUNCTION_LINE.test(t) && !NOT_A_FUNCTION.test(t)
      && /\s/u.test(before.trim()) && (isHeaderFile || !t.trimEnd().endsWith(';'));
    const isTag = TAG_LINE.test(t);
    if (!(DEFINE_LINE.test(t) || isTag || isFunction)) continue;
    if (!add(line)) break;
    declarations++;
    if (isTag || isFunction) structural++;
  }
  let kind: ExcerptKind = 'code-declarations';
  if (declarations === 0) {
    if (skipped === null) return undefined;
    segments.length = 0;
    used = 0;
    for (let i = next; i < lines.length; i++) {
      if (lines[i]!.text === '') continue;
      if (!add(lines[i]!)) break;
    }
    if (segments.length === 0) return undefined;
    kind = 'code-after-licence';
  }
  return {
    text: segments.map(segment => segment.text).join('\n'), kind,
    ranges: mergeRanges(segments.map((segment): ExcerptRange => [base + segment.start, base + segment.end])).slice(0, MAX_EXCERPT_RANGES),
    licenceSkipped: skipped === null ? null : [base + skipped[0], base + skipped[1]],
  };
}

/**
 * The excerpt for one file. `text` is the admitted text of the file's first quotable
 * piece; `base` is that piece's UTF-8 byte offset in the blob (0 for a whole file).
 * `maxChars` is the discovery budget's `maxExcerptChars`, the bound for every kind.
 */
export function buildExcerpt(path: string, text: string, base: number, maxChars: number): Excerpt {
  const name = path.split('/').at(-1) ?? '';
  if ((C_FAMILY as readonly string[]).includes(extensionOf(name))) {
    const code = codeExcerpt(path, text, base, maxChars);
    if (code !== undefined) return code;
  }
  const head = cut(text, maxChars);
  return { text: head, kind: 'head', ranges: head === '' ? [] : [[base, base + Buffer.byteLength(head, 'utf8')]], licenceSkipped: null };
}
