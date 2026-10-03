// The screening-scope v2 `project-documentation` path rule (package
// `contracts/candidates/public-source-screening-scope-v2/`).
//
// A literal port of the builder's reference reader,
// `classify_documentation` in `scripts/build_public_source_screening_scope_v2.py`;
// `project-documentation.parity.test.ts` runs the builder's fixtures and a
// generated path set through both. Per the delta's TS-parity notes: only A-Z
// fold to a-z, digits are the listed characters compared as code points (no
// Unicode-aware class), and names split into whole words at each listed
// separator. Every list comes from the policy's rule object, never from here.

/** The rule object as the policy carries it, after `parseDocumentationRule`. */
export interface DocumentationRule {
  readonly variant: DocumentationVariant;
  readonly prefix: { readonly digitCount: number; readonly digits: string; readonly separator: string };
  readonly rootStems: readonly string[];
  readonly documentSuffixes: readonly string[];
  readonly docTreeRoots: readonly string[];
  readonly docTreeExtensions: readonly string[];
  readonly docExcludedTokens: readonly string[];
  readonly docTokenSeparators: string;
  readonly docTxtExcludedNames: readonly string[];
  readonly docTxtExcludedPrefixes: readonly string[];
  readonly licenseTreeRoots: readonly string[];
  readonly licenseTreeSuffixes: readonly string[];
}

/** The four manifest rows; `policyVersion` ends with `.<variant>`. */
export const DOCUMENTATION_VARIANTS = ['none', 'manifesto', 'architecture', 'both'] as const;
export type DocumentationVariant = typeof DOCUMENTATION_VARIANTS[number];
const PATH_RULE_IDS = ['root-document', 'docs-tree', 'licenses-tree'];
// The opt-in words of each variant: mapped at the root and lifted from the docs denylist.
const OPT_INS: Readonly<Record<DocumentationVariant, readonly string[]>> = { none: [], manifesto: ['manifesto'], architecture: ['architecture'], both: ['architecture', 'manifesto'] };
const OPT_IN_WORDS: Readonly<Record<string, readonly string[]>> = { architecture: ['architecture', 'architectures'], manifesto: ['manifesto', 'manifestos'] };

const ascii = (value: string): boolean => /^[\x20-\x7e]*$/u.test(value);
const words = (value: unknown, allowEmpty = false): value is readonly string[] =>
  Array.isArray(value) && value.length > 0 && value.every(item => typeof item === 'string' && (allowEmpty || item.length > 0) && ascii(item) && item === item.toLowerCase());

/** Reads the rule object; a string is the reason it cannot be read (the caller refuses). */
export function parseDocumentationRule(rule: Record<string, unknown>, policyVersion: string): DocumentationRule | string {
  const variant = DOCUMENTATION_VARIANTS.find(name => policyVersion.endsWith(`.${name}`));
  if (variant === undefined) return 'policyVersion names no screening-scope v2 variant';
  const ids = Array.isArray(rule.pathRules) ? rule.pathRules.map(entry => (entry as Record<string, unknown> | null)?.id) : [];
  if (ids.length !== PATH_RULE_IDS.length || ids.some((id, index) => id !== PATH_RULE_IDS[index])) return 'pathRules are not root-document, docs-tree, licenses-tree';
  const prefix = rule.rootStemNumericPrefix as Record<string, unknown> | undefined;
  if (prefix === null || typeof prefix !== 'object' || !Number.isInteger(prefix.digitCount) || (prefix.digitCount as number) < 1 || typeof prefix.digits !== 'string'
    || prefix.digits.length === 0 || !ascii(prefix.digits) || typeof prefix.separator !== 'string' || prefix.separator.length !== 1 || !ascii(prefix.separator)) return 'rootStemNumericPrefix unreadable';
  const lists = ['rootStems', 'docTreeRoots', 'docTreeExtensions', 'docExcludedTokens', 'docTxtExcludedNames', 'docTxtExcludedPrefixes', 'licenseTreeRoots', 'licenseTreeSuffixes'] as const;
  for (const name of lists) if (!words(rule[name])) return `${name} unreadable`;
  if (!words(rule.documentSuffixes, true)) return 'documentSuffixes unreadable';
  if (typeof rule.docTokenSeparators !== 'string' || rule.docTokenSeparators.length === 0 || !ascii(rule.docTokenSeparators)) return 'docTokenSeparators unreadable';
  const stems = rule.rootStems as readonly string[], denied = rule.docExcludedTokens as readonly string[];
  // The variant suffix and the opt-in words must agree, or the bytes say two things.
  for (const [optIn, optInWords] of Object.entries(OPT_IN_WORDS)) {
    const added = OPT_INS[variant].includes(optIn);
    if (stems.includes(optIn) !== added || optInWords.some(word => denied.includes(word) === added)) return `variant ${variant} disagrees with the ${optIn} opt-in`;
  }
  return {
    variant, prefix: { digitCount: prefix.digitCount as number, digits: prefix.digits, separator: prefix.separator }, rootStems: stems,
    documentSuffixes: rule.documentSuffixes as readonly string[], docTreeRoots: rule.docTreeRoots as readonly string[], docTreeExtensions: rule.docTreeExtensions as readonly string[],
    docExcludedTokens: denied, docTokenSeparators: rule.docTokenSeparators, docTxtExcludedNames: rule.docTxtExcludedNames as readonly string[],
    docTxtExcludedPrefixes: rule.docTxtExcludedPrefixes as readonly string[], licenseTreeRoots: rule.licenseTreeRoots as readonly string[], licenseTreeSuffixes: rule.licenseTreeSuffixes as readonly string[],
  };
}

// Folds A-Z to a-z and nothing else (no long s, no Kelvin sign, no dotted I).
const asciiFold = (path: string): string => path.replace(/[A-Z]/gu, letter => letter.toLowerCase());

// Code points, as the reference reader indexes them.
const hasNumericPrefix = (name: readonly string[], prefix: DocumentationRule['prefix']): boolean =>
  name.length > prefix.digitCount && name.slice(0, prefix.digitCount).every(point => prefix.digits.includes(point)) && name[prefix.digitCount] === prefix.separator;

// Splits at each separator character, keeping empty words, as `tokens` does.
function tokens(segment: string, separators: string): string[] {
  const out: string[] = [];
  let current = '';
  for (const point of segment) {
    if (separators.includes(point)) { out.push(current); current = ''; } else current += point;
  }
  return [...out, current];
}

const deniedWord = (segment: string, rule: DocumentationRule): boolean => tokens(segment, rule.docTokenSeparators).some(word => rule.docExcludedTokens.includes(word));

const endsLonger = (name: string, suffix: string): boolean => name.endsWith(suffix) && name.length > suffix.length;

/** True when the path is `project-documentation` under the rule. */
export function classifyDocumentation(path: string, rule: DocumentationRule): boolean {
  const folded = asciiFold(path);
  if (folded === '' || folded.startsWith('/') || folded.endsWith('/') || folded.includes('//') || folded.includes('\\')) return false;
  const parts = folded.split('/');
  if (parts.some(segment => segment === '' || segment === '.' || segment === '..')) return false;
  const name = parts.at(-1)!;
  if (parts.length === 1) {
    const points = Array.from(name);
    const candidates = hasNumericPrefix(points, rule.prefix) ? [name, points.slice(rule.prefix.digitCount + 1).join('')] : [name];
    return candidates.some(candidate => rule.documentSuffixes.some(suffix => candidate.endsWith(suffix) && rule.rootStems.includes(candidate.slice(0, candidate.length - suffix.length))));
  }
  const extension = rule.docTreeExtensions.find(suffix => endsLonger(name, suffix));
  if (rule.docTreeRoots.includes(parts[0]!) && extension !== undefined) {
    const named = [...parts.slice(1, -1), name.slice(0, name.length - extension.length)];
    if (named.some(segment => deniedWord(segment, rule))) return false;
    if (name.endsWith('.txt') && (rule.docTxtExcludedNames.includes(name) || rule.docTxtExcludedPrefixes.some(prefix => name.startsWith(prefix)))) return false;
    return true;
  }
  const suffix = rule.licenseTreeSuffixes.find(candidate => endsLonger(name, candidate));
  if (parts.length !== 2 || !rule.licenseTreeRoots.includes(parts[0]!) || suffix === undefined) return false;
  // The licenses file name, without its suffix, is held to the same whole-word denylist.
  return !deniedWord(name.slice(0, name.length - suffix.length), rule);
}
