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

/** The version-3 scope's code-content exemption (`publicSourceScope.activeContent.codeContentExemption`, approved 2026-10-08, variant
 * `all`; package `contracts/candidates/public-source-screening-scope-v3/`), shared by both screens for the reason the class above is.
 *
 * Its rule lifts, for an exempt body only, the active-content scan, its success condition and the malformed-code-context exclusion;
 * every detector still runs, and a project-documentation body, or a code-content body whose extension the exemption does not list, is
 * scanned as before. Its `renderCondition` binds every page sink the body reaches: a consumer that cannot confirm it for a page scans
 * the body as before for that page (`pageSinkCspFinding` below checks the policy half; the dossier's `render.ts` applies it).
 *
 * As for the class rule, the texts are pinned by digest: the screen implements one reading of one text, and any other text (either
 * variant's `appliesTo` is accepted, the extension list deciding the variant) refuses the screen. */
const EXEMPTION_TEXTS = {
  appliesTo: ['d202ff90a058d968503ef1de9f1de6f13cb31d4217b6761dee2579e8fc0f97b4', '215d99e9b193efd3be87442cf55fec0b4c37d3482767917b0ddfacee987fcbca'],
  rule: 'b2d0ec79e84ac51239073b9c84040d92951400575c6204825d990681d0b4a41c',
  renderCondition: '2942af13a00058568faaf88e6a3abe9f43a9a1f0c056f1531fd2aff4797265a9',
  egress: '4ffff86212a31309259037674aa7d95f4458c2f460335ef12198ba7a453148fd',
} as const;
const EXEMPTION_KEYS = ['appliesTo', 'exemptExtensions', 'rule', 'renderCondition', 'egress'] as const;

export interface CodeContentExemption {
  /** The extensions whose code-content bodies skip the active-content scan, each one of `sourceExtensions`. */
  readonly exemptExtensions: readonly string[];
}
/** `exemption` is null when the scope declares none (versions 1 and 2). */
export type CodeContentExemptionRead = { readonly ok: true; readonly exemption: CodeContentExemption | null } | { readonly ok: false; readonly why: string };

/** Reads the exemption from a policy's `publicSourceScope`. Any malformed or unrecognised field refuses. */
export function readCodeContentExemption(scope: unknown, sourceExtensions: readonly string[]): CodeContentExemptionRead {
  const refuse = (why: string): CodeContentExemptionRead => ({ ok: false, why: `its code-content exemption ${why}` });
  const active = isObject(scope) ? scope['activeContent'] : undefined;
  if (!isObject(active) || !Object.hasOwn(active, 'codeContentExemption')) return { ok: true, exemption: null };
  const exemption = active['codeContentExemption'];
  if (!isObject(exemption)) return refuse('is not an object');
  const keys = Object.keys(exemption);
  if (keys.length !== EXEMPTION_KEYS.length || EXEMPTION_KEYS.some(key => !keys.includes(key))) return refuse(`carries the fields ${keys.join(', ')}, not exactly ${EXEMPTION_KEYS.join(', ')}`);
  const applies = exemption['appliesTo'];
  if (typeof applies !== 'string' || !(EXEMPTION_TEXTS.appliesTo as readonly string[]).includes(sha256(applies))) return refuse('appliesTo is not a text this screen implements');
  for (const key of ['rule', 'renderCondition', 'egress'] as const) {
    const value = exemption[key];
    if (typeof value !== 'string' || sha256(value) !== EXEMPTION_TEXTS[key]) return refuse(`${key} is not the text this screen implements`);
  }
  const extensions = exemption['exemptExtensions'];
  if (!Array.isArray(extensions) || extensions.length === 0 || new Set(extensions).size !== extensions.length
    || !extensions.every(entry => typeof entry === 'string' && sourceExtensions.includes(entry))) {
    return refuse('exemptExtensions is not a non-empty list of distinct sourceExtensions entries');
  }
  return { ok: true, exemption: Object.freeze({ exemptExtensions: Object.freeze([...extensions as string[]]) }) };
}

/** Whether a body at `repositoryPath`, admitted under `contentClass`, skips the active-content scan: the exemption is declared, the
 * class is code-content and the final path segment ends with one of its extensions, compared case-sensitively as `sourceExtensions` are.
 * A project-documentation body never does, whatever it ends with. */
export function codeContentExempt(repositoryPath: string, contentClass: PublicSourceContentClass | undefined, exemption: CodeContentExemption | null): boolean {
  if (exemption === null || contentClass !== 'code-content') return false;
  const name = repositoryPath.split('/').at(-1) ?? '';
  return exemption.exemptExtensions.some(entry => name.endsWith(entry));
}

/** What a page renderer declares (as its `pageSinkContract` property) when it writes every byte of a source body or span it puts on a
 * page as text, each of `& < > " '` as a character reference, never parsed as Markdown or HTML and never minting a link, element,
 * attribute, script or handler: the encoding half of `renderCondition`. The declaration is the renderer's; its own tests must fail if a
 * page path stops encoding. A consumer reads it together with `pageSinkCspFinding` on every page drawn. */
export const PAGE_SINK_CONTRACT = 'polaris/page-sink/escaped-text-under-csp/1';

/** Directives a later declaration lets override `default-src` for script or plugin fetches; `renderCondition` forbids each. */
const FORBIDDEN_DIRECTIVES = ['script-src', 'script-src-elem', 'script-src-attr', 'object-src'] as const;
const CSP_META = /<meta\s[^>]*http-equiv\s*=\s*(["'])\s*content-security-policy(?:-report-only)?\s*\1[^>]*>/giu;
const decodeAttribute = (value: string): string =>
  value.replace(/&(?:#39|#x27|apos);/giu, '\'').replace(/&(?:#34|#x22|quot);/giu, '"').replace(/&(?:#38|#x26|amp);/giu, '&');

/** Why an HTML page does not meet the policy half of `renderCondition`, or null when it does: exactly one enforced
 * Content-Security-Policy `<meta>` (no Report-Only one) in `<head>`, before `<title>`, `<body` and any other element but the charset
 * and viewport metas; a `default-src` whose source list is exactly `'none'`; and none of `script-src`, `script-src-elem`,
 * `script-src-attr` or `object-src`. The encoding half (every body byte written as text, `& < > " '` as character references) is the
 * renderer's, confirmed by its own tests; this checks only what one page's bytes can show. */
export function pageSinkCspFinding(html: string): string | null {
  const metas = [...html.matchAll(CSP_META)];
  if (metas.length !== 1) return `the page carries ${metas.length} Content-Security-Policy meta elements, not exactly one`;
  const meta = metas[0]!;
  if (/content-security-policy-report-only/iu.test(meta[0])) return 'the page\'s Content-Security-Policy is Report-Only, which enforces nothing';
  const before = html.slice(0, meta.index);
  const head = /^<!doctype html>\s*<html(?:\s[^>]*)?>\s*<head>\s*/iu.exec(before);
  const rest = head === null ? null : before.slice(head[0].length).replace(/<meta\s+charset\s*=\s*"[^"<>]*"\s*\/?>\s*/iu, '').replace(/<meta\s+name\s*=\s*"viewport"\s+content\s*=\s*"[^"<>]*"\s*\/?>\s*/iu, '');
  if (rest !== '') return 'the page\'s Content-Security-Policy is not delivered first in <head>, before every other element but the charset and viewport metas';
  const content = /\scontent\s*=\s*"([^"]*)"/iu.exec(meta[0]) ?? /\scontent\s*=\s*'([^']*)'/iu.exec(meta[0]);
  if (content === null) return 'the page\'s Content-Security-Policy meta carries no content attribute';
  const directives = decodeAttribute(content[1]!).split(';').map(part => part.trim()).filter(part => part !== '').map(part => part.split(/\s+/u));
  const named = (name: string) => directives.filter(([directive]) => directive!.toLowerCase() === name);
  const defaults = named('default-src');
  if (defaults.length !== 1 || defaults[0]!.length !== 2 || defaults[0]![1]!.toLowerCase() !== '\'none\'') return 'the page\'s default-src source list is not exactly \'none\'';
  const forbidden = FORBIDDEN_DIRECTIVES.filter(name => named(name).length > 0);
  if (forbidden.length > 0) return `the page's Content-Security-Policy carries ${forbidden.join(', ')}, which may override default-src for script or plugins`;
  return null;
}
