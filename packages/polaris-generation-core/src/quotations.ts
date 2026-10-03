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
 * quotation starts after QUOTATION_LEAD; since it may itself contain double
 * quotes, every later `"` is a candidate end, and the quotation matches when
 * some candidate's normalized text is a non-empty substring of a normalized
 * source: any contiguous span of one source, never words joined from two.
 * Text without the lead has nothing to check.
 */
export function quotationsMatch(text: string, sourceTexts: readonly string[]): boolean {
  const sources = sourceTexts.map(normalizeQuotation);
  for (let at = text.indexOf(QUOTATION_LEAD); at >= 0; at = text.indexOf(QUOTATION_LEAD, at + 1)) {
    const start = at + QUOTATION_LEAD.length;
    let matched = false;
    for (let end = text.lastIndexOf('"'); end >= start && !matched; end = text.lastIndexOf('"', end - 1)) {
      const quoted = normalizeQuotation(text.slice(start, end));
      matched = quoted.length > 0 && sources.some(source => source.includes(quoted));
    }
    if (!matched) return false;
  }
  return true;
}
