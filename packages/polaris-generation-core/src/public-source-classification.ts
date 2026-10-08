import { createHash } from 'node:crypto';

/** The public-source screening scope's `project-documentation` class (policy version 2, `publicSourceScope.contentClassification`,
 * the rule whose `class` is `project-documentation`; RFC5-14 as amended 2026-10-07), shared by the any-repo reader's screen and the
 * dossier's screen so the two cannot read the rule differently (`syzygy-2coz`; the rest of the screen is still copied, syzygy-qkea.17).
 *
 * Every parameter is read from the policy's bytes. The rule's prose is not: this module implements one reading of one text, so the
 * texts it implements are pinned by digest and any other text refuses the screen rather than being matched under a stale reading.
 *
 * Choices the rule text leaves open, each fail-closed:
 * - The rule's lists are compared, as given, against the ASCII-folded path. An entry that could never match a folded path (an A-Z
 *   letter, a '/' or a backslash), an extension that is not '.' plus at least one character, or an excluded token that contains a
 *   separator is malformed and refuses the screen.
 * - `rootStemNumericPrefix` is removed when present, so a name that starts with it is compared without it; when `optional` is false a
 *   name without it matches nothing.
 * - Where more than one of a rule's extensions fits a file name, the excluded-word test must pass with each one removed.
 * - The policy says no blob has two classes by extension and that a blob this rule matches is never code-content. The screen refuses a
 *   policy whose suffix and extension lists meet `sourceExtensions` (the statement would be false), and a path this rule matches is
 *   project-documentation whatever it ends with.
 * - A path matched by more than one path rule is not in the class ("exactly one"); if no code-content extension ends it, it is
 *   indeterminate. */

export type DocumentationPathRuleId = 'root-document' | 'docs-tree' | 'licenses-tree';
const PATH_RULE_IDS: readonly DocumentationPathRuleId[] = ['root-document', 'docs-tree', 'licenses-tree'];

/** sha256 of each rule text this module implements, UTF-8. */
const IMPLEMENTED_TEXTS = {
  rule: '99453acf1524976e5416fa4291d55aa6ad2530418efe802aac6a675748ddfe46',
  disjointFromSourceExtensions: '9dba52f576eced78b2fd95f4d1bb05afc2e401a57b49164edc998ae141872455',
  rootStemNumericPrefixNote: '720a1f94189844e4cc480ba6cf3d98eaf7bebbf91c4b2e8ed6046af0e6b11605',
  'root-document': 'c42e03ee183319bbc448e6cdd89aa731dca793e07c4da60e71c792921fa90981',
  'docs-tree': 'ad1eba9e457805b71fb69753181f055698f53e52b37188d7d5f5b79a0b5d1ce9',
  'licenses-tree': 'f73a27ee4f83cf2754e1037069453c2f32c16cf83e032518fca91013d378e2d2',
} as const;

/** The literal the docs-tree rule names for its build-file exclusion ("a name ending in .txt"); it is rule text, not a parameter. */
const TXT = '.txt';

export interface ProjectDocumentationRule {
  readonly rootStemNumericPrefix: { readonly digitCount: number; readonly digits: string; readonly separator: string; readonly optional: boolean };
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

/** `rule` is null when the policy has no project-documentation rule (version 1). */
export type ProjectDocumentationRead = { readonly ok: true; readonly rule: ProjectDocumentationRule | null } | { readonly ok: false; readonly why: string };

const isObject = (value: unknown): value is Readonly<Record<string, unknown>> => value !== null && typeof value === 'object' && !Array.isArray(value);
const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
// Never matchable against a folded path: an A-Z letter (folded away), a separator of segments, or a backslash (matches nothing).
const unmatchable = (entry: string): boolean => /[A-Z/\\]/u.test(entry);
const names = (value: unknown, minimum: number, valid: (entry: string) => boolean): value is readonly string[] =>
  Array.isArray(value) && value.length >= minimum && value.every(entry => typeof entry === 'string' && !unmatchable(entry) && valid(entry))
  && new Set(value).size === value.length;
const nonEmpty = (entry: string): boolean => entry.length > 0;
const extension = (entry: string): boolean => entry.length > 1 && entry.startsWith('.');
const segment = (entry: string): boolean => entry.length > 0 && entry !== '.' && entry !== '..';

/** Reads the project-documentation rule from a policy's content-classification rules. Any malformed field refuses. */
export function readProjectDocumentationRule(rules: readonly unknown[], sourceExtensions: readonly string[]): ProjectDocumentationRead {
  const refuse = (why: string): ProjectDocumentationRead => ({ ok: false, why: `its project-documentation rule ${why}` });
  const found = rules.filter(rule => isObject(rule) && rule['class'] === 'project-documentation');
  if (found.length === 0) return { ok: true, rule: null };
  if (found.length > 1) return refuse('appears more than once');
  const rule = found[0] as Readonly<Record<string, unknown>>;
  if (typeof rule['rule'] !== 'string' || sha256(rule['rule']) !== IMPLEMENTED_TEXTS.rule) return refuse('text is not the text this screen implements');
  if (typeof rule['disjointFromSourceExtensions'] !== 'string' || sha256(rule['disjointFromSourceExtensions']) !== IMPLEMENTED_TEXTS.disjointFromSourceExtensions) {
    return refuse('disjointness statement is not the text this screen implements');
  }
  const pathRules = rule['pathRules'];
  if (!Array.isArray(pathRules) || pathRules.length !== PATH_RULE_IDS.length
    || !pathRules.every((pathRule: unknown, index) => isObject(pathRule) && pathRule['id'] === PATH_RULE_IDS[index] && typeof pathRule['rule'] === 'string'
      && sha256(pathRule['rule']) === IMPLEMENTED_TEXTS[PATH_RULE_IDS[index]!])) {
    return refuse('path rules are not the three this screen implements (root-document, docs-tree, licenses-tree, in that order and text)');
  }
  const prefix = rule['rootStemNumericPrefix'];
  if (!isObject(prefix) || !Number.isSafeInteger(prefix['digitCount']) || (prefix['digitCount'] as number) < 1
    || typeof prefix['digits'] !== 'string' || !/^[\x21-\x7e]+$/u.test(prefix['digits']) || unmatchable(prefix['digits']) || new Set(prefix['digits']).size !== prefix['digits'].length
    || typeof prefix['separator'] !== 'string' || !/^[\x21-\x7e]+$/u.test(prefix['separator']) || unmatchable(prefix['separator'])
    || typeof prefix['optional'] !== 'boolean' || typeof prefix['note'] !== 'string' || sha256(prefix['note']) !== IMPLEMENTED_TEXTS.rootStemNumericPrefixNote) {
    return refuse('rootStemNumericPrefix is unreadable');
  }
  const separators = rule['docTokenSeparators'];
  if (typeof separators !== 'string' || separators.length === 0 || unmatchable(separators)) return refuse('docTokenSeparators is unreadable');
  const lists: [string, number, (entry: string) => boolean][] = [
    ['rootStems', 1, nonEmpty], ['documentSuffixes', 1, entry => entry === '' || extension(entry)], ['docTreeRoots', 1, segment],
    ['docTreeExtensions', 1, extension], ['docExcludedTokens', 0, entry => entry.length > 0 && ![...separators].some(sep => entry.includes(sep))],
    ['docTxtExcludedNames', 0, nonEmpty], ['docTxtExcludedPrefixes', 0, nonEmpty], ['licenseTreeRoots', 1, segment], ['licenseTreeSuffixes', 1, extension],
  ];
  for (const [field, minimum, valid] of lists) if (!names(rule[field], minimum, valid)) return refuse(`${field} is unreadable`);
  const read = rule as unknown as ProjectDocumentationRule;
  const overlap = [...read.documentSuffixes, ...read.docTreeExtensions, ...read.licenseTreeSuffixes].filter(entry => sourceExtensions.includes(entry));
  if (overlap.length > 0) return refuse(`meets sourceExtensions (${overlap.join(', ')}), which the policy says it never does`);
  return {
    ok: true,
    rule: Object.freeze({
      rootStemNumericPrefix: Object.freeze({ digitCount: prefix['digitCount'] as number, digits: prefix['digits'], separator: prefix['separator'], optional: prefix['optional'] }),
      rootStems: Object.freeze([...read.rootStems]), documentSuffixes: Object.freeze([...read.documentSuffixes]), docTreeRoots: Object.freeze([...read.docTreeRoots]),
      docTreeExtensions: Object.freeze([...read.docTreeExtensions]), docExcludedTokens: Object.freeze([...read.docExcludedTokens]), docTokenSeparators: separators,
      docTxtExcludedNames: Object.freeze([...read.docTxtExcludedNames]), docTxtExcludedPrefixes: Object.freeze([...read.docTxtExcludedPrefixes]),
      licenseTreeRoots: Object.freeze([...read.licenseTreeRoots]), licenseTreeSuffixes: Object.freeze([...read.licenseTreeSuffixes]),
    }),
  };
}

const fold = (text: string): string => text.replace(/[A-Z]/gu, letter => letter.toLowerCase());

function hasExcludedWord(name: string, rule: ProjectDocumentationRule): boolean {
  let word = '';
  for (const character of `${name}${rule.docTokenSeparators[0]}`) {
    if (!rule.docTokenSeparators.includes(character)) { word += character; continue; }
    if (rule.docExcludedTokens.includes(word)) return true;
    word = '';
  }
  return false;
}

/** The names left once each fitting extension is removed (the name must be longer than the extension), or none when none fits. */
const stemsWithout = (name: string, extensions: readonly string[]): string[] =>
  extensions.filter(entry => name.length > entry.length && name.endsWith(entry)).map(entry => name.slice(0, name.length - entry.length));

function rootDocument(segments: readonly string[], rule: ProjectDocumentationRule): boolean {
  if (segments.length !== 1) return false;
  const { digitCount, digits, separator, optional } = rule.rootStemNumericPrefix;
  let name = segments[0]!;
  const head = name.slice(0, digitCount);
  const present = head.length === digitCount && [...head].every(character => digits.includes(character)) && name.startsWith(separator, digitCount);
  if (present) name = name.slice(digitCount + separator.length);
  else if (!optional) return false;
  return rule.documentSuffixes.some(suffix => name.endsWith(suffix) && rule.rootStems.includes(name.slice(0, name.length - suffix.length)));
}

function docsTree(segments: readonly string[], rule: ProjectDocumentationRule): boolean {
  if (segments.length < 2 || !rule.docTreeRoots.includes(segments[0]!)) return false;
  const name = segments.at(-1)!;
  const stems = stemsWithout(name, rule.docTreeExtensions);
  if (stems.length === 0) return false;
  if (segments.slice(1, -1).some(directory => hasExcludedWord(directory, rule)) || stems.some(stem => hasExcludedWord(stem, rule))) return false;
  return !(name.endsWith(TXT) && (rule.docTxtExcludedNames.includes(name) || rule.docTxtExcludedPrefixes.some(prefix => name.startsWith(prefix))));
}

function licensesTree(segments: readonly string[], rule: ProjectDocumentationRule): boolean {
  if (segments.length !== 2 || !rule.licenseTreeRoots.includes(segments[0]!)) return false;
  const stems = stemsWithout(segments[1]!, rule.licenseTreeSuffixes);
  return stems.length > 0 && !stems.some(stem => hasExcludedWord(stem, rule));
}

/** The path rules that match a repository-relative path; a path with an empty, '.' or '..' segment, a backslash or a leading or
 * trailing '/' matches none. */
export function documentationPathRules(repositoryPath: string, rule: ProjectDocumentationRule): DocumentationPathRuleId[] {
  const folded = fold(repositoryPath);
  if (folded.includes('\\')) return [];
  const segments = folded.split('/');
  if (segments.some(part => part === '' || part === '.' || part === '..')) return [];
  return PATH_RULE_IDS.filter(id => (id === 'root-document' ? rootDocument : id === 'docs-tree' ? docsTree : licensesTree)(segments, rule));
}

export type PublicSourceContentClass = 'project-documentation' | 'code-content';

/** The class a public-source blob's body is admitted under, or undefined when it is indeterminate. `documentation` is null when the
 * project-documentation class is not classified: the policy has no such rule, or the in-force RFC-0005 vocabulary cannot be confirmed
 * to list the class (the scope's `prerequisite`). */
export function publicSourceContentClass(repositoryPath: string, sourceExtensions: readonly string[], documentation: ProjectDocumentationRule | null): PublicSourceContentClass | undefined {
  if (documentation !== null && documentationPathRules(repositoryPath, documentation).length === 1) return 'project-documentation';
  const name = repositoryPath.split('/').at(-1) ?? '';
  return sourceExtensions.some(entry => name.endsWith(entry)) ? 'code-content' : undefined;
}
