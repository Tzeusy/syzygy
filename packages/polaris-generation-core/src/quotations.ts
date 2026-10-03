/**
 * The deterministic check behind the dossier profile's rule 4: a quotation in
 * the form `The project states: "…"` must match a cited source. A fidelity
 * reviewer's verdict is a model's judgment; this is code, run by the stage
 * validator on every inventory entry and draft block.
 *
 * Matching is exact after one normalization, applied to both the quotation
 * and the source: every run of whitespace (line breaks included) becomes one
 * space, and markdown emphasis and link syntax are dropped, keeping the link
 * text. Nothing else may differ.
 */

export const QUOTATION_LEAD = 'The project states: "';

/** The rule-4 normalization: link syntax to its text, emphasis markers dropped, whitespace runs to one space. */
export function normalizeQuotation(text: string): string {
  return text
    .replace(/(?<!!)\[([^\]]*)\]\([^)\s]*(?:\s+"[^"]*")?\)/gu, '$1')
    .replace(/(\*\*|__)(?=\S)([\s\S]*?\S)\1/gu, '$2')
    .replace(/(?<![\p{L}\p{N}*])\*(?=\S)([\s\S]*?\S)\*(?![\p{L}\p{N}*])/gu, '$1')
    .replace(/(?<![\p{L}\p{N}_])_(?=\S)([\s\S]*?\S)_(?![\p{L}\p{N}_])/gu, '$1')
    .replace(/\s+/gu, ' ')
    .trim();
}

/**
 * True when every quotation in `text` matches one of `sourceTexts`. A
 * quotation starts after QUOTATION_LEAD and, since it may itself contain
 * double quotes, ends at the last `"` before the next lead (or the end of the
 * text): the whole span must match, so a matching opening cannot carry an
 * unverified tail, and a `"` in prose after a quotation fails the check rather
 * than shortening it. A span matches when its normalized text is non-empty and
 * a substring of one normalized source: any contiguous span of one source,
 * never words joined from two. Text without the lead has nothing to check.
 */
export function quotationsMatch(text: string, sourceTexts: readonly string[]): boolean {
  const sources = sourceTexts.map(normalizeQuotation);
  for (let at = text.indexOf(QUOTATION_LEAD); at >= 0;) {
    const start = at + QUOTATION_LEAD.length;
    const next = text.indexOf(QUOTATION_LEAD, start);
    const end = text.lastIndexOf('"', (next < 0 ? text.length : next) - 1);
    if (end < start) return false;
    const quoted = normalizeQuotation(text.slice(start, end));
    if (quoted.length === 0 || !sources.some(source => source.includes(quoted))) return false;
    at = next;
  }
  return true;
}
