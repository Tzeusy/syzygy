/**
 * Deterministic quote fidelity. A generated block may quote its sources, and
 * a quotation is a claim about bytes: every quoted span must be a substring of
 * one of the sources the block cites, after a normalisation applied identically
 * to the quote and to the source. A model review cannot waive this; a failure
 * is a blocking finding on the block, which therefore renders Unknown or does
 * not render as supported (it never passes silently).
 *
 * Normalisation, in order, on both sides:
 *   1. comment leaders at line starts (block-comment open and close marks, a
 *      bare star, double slash, hash) are dropped;
 *   2. markdown links and images keep their text and lose url and brackets;
 *   3. markdown emphasis characters `*` and `_` are dropped;
 *   4. every whitespace run, line breaks included, becomes one space; ends trimmed.
 * Straight (`"`) and curly (`“ ”`) double quotes delimit a quote. A straight-
 * quoted span that itself contains straight quotes is resolved by taking the
 * longest reading, from its opening quote to a later quote that ends a word
 * or sentence, whose normalised text occurs in a cited source; curly quotes
 * nest by depth. A quote that has no verifying reading is a failure.
 */

/** The lead-in lane-p's prompt rule asks for before a verbatim quotation. */
export const QUOTE_LEAD_IN = "The project's sources state:";

export type QuoteFindingKind = 'quote-not-in-cited-sources' | 'unterminated-quote' | 'empty-quote' | 'quote-without-cited-source' | 'lead-in-without-quote';
export interface QuoteFinding {
  readonly blockId: string;
  readonly kind: QuoteFindingKind;
  /** The quoted text as written (at most 200 characters); empty for a lead-in with no quote. */
  readonly quote: string;
}
export interface QuoteBlock { readonly id: string; readonly text: string; readonly sourceIds: readonly string[] }

const LEADER = /^[ \t]*(?:\/\*+|\*+\/|\*+(?=[ \t]|$)|\/\/+|#+)[ \t]?/u;

/** The comparison form of a quote or a source; see the file comment. */
export function normaliseForQuote(text: string): string {
  const unleadered = text.split(/\r\n|\r|\n/u).map(line => line.replace(LEADER, '')).join('\n');
  const unlinked = unleadered.replace(/!?\[([^\]\n]*)\]\([^)\n]*\)/gu, '$1').replace(/!?\[([^\]\n]*)\]\[[^\]\n]*\]/gu, '$1');
  return unlinked.replace(/[*_]/gu, '').replace(/\s+/gu, ' ').trim();
}

const OPEN_CURLY = '“', CLOSE_CURLY = '”';
const BOUNDARY_AFTER = /^$|^[\s.,;:!?)\]}—–-]/u;
const clip = (text: string): string => (text.length > 200 ? text.slice(0, 200) : text);

interface Span { readonly inner: string; readonly end: number; readonly candidates: readonly string[] }

/** Where the quote opened at `open` could end: one candidate per plausible closing quote, longest first. */
function straightCandidates(text: string, open: number): { inner: string; end: number }[] {
  const out: { inner: string; end: number }[] = [];
  for (let j = open + 1; j < text.length; j++) {
    if (text[j] !== '"') continue;
    if (BOUNDARY_AFTER.test(text.slice(j + 1, j + 2))) out.push({ inner: text.slice(open + 1, j), end: j });
  }
  return out.reverse();
}

function curlySpan(text: string, open: number): { inner: string; end: number } | undefined {
  let depth = 0;
  for (let j = open; j < text.length; j++) {
    if (text[j] === OPEN_CURLY) depth++;
    else if (text[j] === CLOSE_CURLY && --depth === 0) return { inner: text.slice(open + 1, j), end: j };
  }
  return undefined;
}

/** Every quoted span of `text`, with the reading that verifies against `haystacks` when one exists. */
function quotedSpans(text: string, verifies: (inner: string) => boolean): { inner: string; ok: boolean; terminated: boolean; end: number }[] {
  const out: { inner: string; ok: boolean; terminated: boolean; end: number }[] = [];
  for (let i = 0; i < text.length; i++) {
    const c = text[i]!;
    if (c === OPEN_CURLY) {
      const span = curlySpan(text, i);
      if (span === undefined) { out.push({ inner: text.slice(i + 1), ok: false, terminated: false, end: text.length }); break; }
      out.push({ inner: span.inner, ok: verifies(span.inner), terminated: true, end: span.end });
      i = span.end;
    } else if (c === '"') {
      const candidates = straightCandidates(text, i);
      if (candidates.length === 0) { out.push({ inner: text.slice(i + 1), ok: false, terminated: false, end: text.length }); break; }
      const verified = candidates.find(candidate => verifies(candidate.inner));
      const chosen = verified ?? candidates[candidates.length - 1]!;
      out.push({ inner: chosen.inner, ok: verified !== undefined, terminated: true, end: chosen.end });
      i = chosen.end;
    }
  }
  return out;
}

/** Findings for one block: every quoted span must occur, normalised, in a source the block cites. */
export function checkBlockQuotes(block: QuoteBlock, sourceText: ReadonlyMap<string, string>, leadIn: string = QUOTE_LEAD_IN): QuoteFinding[] {
  const findings: QuoteFinding[] = [];
  const cited = [...new Set(block.sourceIds)].map(id => sourceText.get(id)).filter((text): text is string => text !== undefined).map(normaliseForQuote);
  const verifies = (inner: string): boolean => {
    const wanted = normaliseForQuote(inner);
    return wanted.length > 0 && cited.some(source => source.includes(wanted));
  };
  const spans = quotedSpans(block.text, verifies);
  for (const span of spans) {
    if (!span.terminated) findings.push({ blockId: block.id, kind: 'unterminated-quote', quote: clip(span.inner) });
    else if (normaliseForQuote(span.inner).length === 0) findings.push({ blockId: block.id, kind: 'empty-quote', quote: clip(span.inner) });
    else if (cited.length === 0) findings.push({ blockId: block.id, kind: 'quote-without-cited-source', quote: clip(span.inner) });
    else if (!span.ok) findings.push({ blockId: block.id, kind: 'quote-not-in-cited-sources', quote: clip(span.inner) });
  }
  // A lead-in promises a verbatim quotation; one with no quote after it promises bytes it does not show.
  for (let at = block.text.indexOf(leadIn); at !== -1; at = block.text.indexOf(leadIn, at + leadIn.length)) {
    const rest = block.text.slice(at + leadIn.length);
    if (!/^\s*["“]/u.test(rest)) findings.push({ blockId: block.id, kind: 'lead-in-without-quote', quote: '' });
  }
  return findings;
}

/** The text of every quotable source, by id, for `checkBlockQuotes`. */
export function sourceTextById(sources: readonly { readonly sourceId: string; readonly text: string }[]): ReadonlyMap<string, string> {
  return new Map(sources.map(source => [source.sourceId, source.text]));
}

/** Every block of a draft: any object with a string id, a string text and a sourceIds list (introduction, section and deep-dive blocks and their children). */
export function draftBlocks(draft: unknown): QuoteBlock[] {
  const out: QuoteBlock[] = [];
  const walk = (node: unknown, depth: number): void => {
    if (depth > 12 || node === null || typeof node !== 'object') return;
    if (Array.isArray(node)) { for (const item of node) walk(item, depth + 1); return; }
    const record = node as Record<string, unknown>;
    if (typeof record.id === 'string' && typeof record.text === 'string' && Array.isArray(record.sourceIds) && record.sourceIds.every(id => typeof id === 'string')) {
      out.push({ id: record.id, text: record.text, sourceIds: record.sourceIds as string[] });
    }
    for (const value of Object.values(record)) walk(value, depth + 1);
  };
  walk(draft, 0);
  return out;
}

/** Quote findings for a whole draft against the quotable sources. */
export function checkDraftQuotes(draft: unknown, sources: readonly { readonly sourceId: string; readonly text: string }[]): QuoteFinding[] {
  const byId = sourceTextById(sources);
  return draftBlocks(draft).flatMap(block => checkBlockQuotes(block, byId));
}

/** The review finding a quote failure becomes, in the shape the repair stage and the reviewer already use. */
export function quoteFindingAsReviewFinding(finding: QuoteFinding): { severity: 'blocking'; message: string; target: string } {
  const what: Record<QuoteFindingKind, string> = {
    'quote-not-in-cited-sources': 'is not found, after normalisation, in any source this block cites',
    'unterminated-quote': 'opens a quotation that is never closed',
    'empty-quote': 'is an empty quotation',
    'quote-without-cited-source': 'quotes text but cites no source',
    'lead-in-without-quote': 'announces a verbatim quotation and gives none',
  };
  return { severity: 'blocking', message: `Quotation ${finding.quote === '' ? '' : `"${finding.quote}" `}${what[finding.kind]} (${finding.kind}). Quote only text the cited sources contain, or state the point in your own words without quotation marks.`, target: finding.blockId };
}
