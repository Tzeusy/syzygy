import { createHash } from 'node:crypto';

import type { PublicSourceContentClass } from './public-source-classification.js';

/** The public-source screening scope's `secretRedaction` (policy version 4, approved 2026-10-20, variant `span`; RFC5-17's
 * `redacted-span`), shared by the any-repo reader's screen and the dossier's screen so the two cannot read the rule differently.
 *
 * As for the class rule and the code-content exemption, every text this module implements is pinned by digest: the screen implements
 * one reading of one text, and any other text refuses the screen. The parameters (`redactedClasses`, `wholeArtifactDetectors`,
 * `wholeArtifactFragments`, `guardLines`) are read from the bytes; the line pattern is pinned with the rule text, because the rule says
 * how it is applied (to each line without its terminator, so a JavaScript `RegExp` without the `m` flag is run once per line, never
 * once over the body, where `^` would anchor only the first line).
 *
 * The reading, in the rule's order:
 * - every detector's matches are every match it makes from every start offset (a sticky regular expression tried at each UTF-16 offset;
 *   a literal at each `indexOf` hit), overlapping matches included;
 * - no match: the body is admitted unredacted (`clean`), as before;
 * - a match from a `wholeArtifactDetectors` detector, any `wholeArtifactFragments` entry anywhere in the body (exact, case-sensitive),
 *   any line matching the line pattern, a class outside `redactedClasses` (code-content included), a match that cannot be placed on
 *   lines (zero length), or more than `MAX_MATCHES` matches: excluded whole, as before;
 * - otherwise each line a match touches, and `guardLines` lines before and after it, is withheld; the retained text is the body with
 *   each withheld line emptied but its terminator kept (so line numbers do not move); every detector runs again over it, and any match
 *   excludes the body whole.
 *
 * Lines are split at LF, CRLF or CR, and a final terminator opens no line, as the generator counts lines (`lineCount`).
 *
 * Resource bound [Inferred]: the every-offset scan makes the same per-offset attempts a whole-body search makes on a body that does not
 * match, so it adds no worst case the version-3 screens did not already have; `MAX_MATCHES` bounds the match set, and a body past it is
 * excluded whole. Not repaired here (the policy's own residuals): a secret no detector matches, beyond the guard lines or continuing past
 * them, is admitted; the whole body's digest and object id stay recorded and can check a guess at a short withheld line. */

const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const isObject = (value: unknown): value is Readonly<Record<string, unknown>> => value !== null && typeof value === 'object' && !Array.isArray(value);

/** sha256 of each text this module implements, UTF-8 (the version-4 bytes approved 2026-10-20). */
const REDACTION_TEXTS = {
  appliesTo: 'd2db3aa87aebba3b42a72a5ff1c435cb3a6bb61288b5ffb0076f68d62891503e',
  wholeArtifactLinePattern: '63f957c57bc1565c86a7ad614469755172102540a0d19b4df3dcd1854b4fefa0',
  rule: '2ef91873fead23d281dd7f627907374be428165ce6c5825fb6419fec08c85c74',
  withheldLines: '9878b9d7a10057981508f7cc9b36bcab649116a52b07ea0e35842030764efd82',
  citedSpanRule: '1d583b499faa94320e106774a5b7e1804fb757e33d34c1b0680ef217b9d495c6',
  provenance: '361eb887bca9149b771b66b0891d71adb5626b3178df48502696144a8b9e0dc1',
  unchanged: '74f0bc88dc1c99324bcfdbc554234c011b0131627adb9eb37d9c34792ea79bdb',
  consequence: 'fbccac9121d61a3cf617a26dfc4b54f378753a22b9c5b7f431ba13447ffb6566',
} as const;
const REDACTION_KEYS = ['appliesTo', 'redactedClasses', 'redactionClass', 'wholeArtifactDetectors', 'wholeArtifactLinePattern', 'wholeArtifactFragments',
  'guardLines', 'rule', 'withheldLines', 'citedSpanRule', 'provenance', 'unchanged', 'consequence'] as const;
const KNOWN_CLASSES: readonly PublicSourceContentClass[] = ['project-documentation', 'code-content'];
/** More matches than this excludes the body whole: the match set is held in memory and each match is placed on lines. */
export const MAX_MATCHES = 10_000;
const MAX_GUARD_LINES = 100;

export interface SecretRedaction {
  readonly redactedClasses: readonly PublicSourceContentClass[];
  readonly wholeArtifactDetectors: readonly string[];
  /** Applied to each line without its terminator; never to the body as a whole. */
  readonly wholeArtifactLinePattern: RegExp;
  readonly wholeArtifactFragments: readonly string[];
  readonly guardLines: number;
}
/** `redaction` is null when the scope declares none (versions 1 to 3). */
export type SecretRedactionRead = { readonly ok: true; readonly redaction: SecretRedaction | null } | { readonly ok: false; readonly why: string };

/** Reads `secretRedaction` from a policy's `publicSourceScope`. `detectorIds` are the policy's detector ids; a whole-artifact detector
 * that names none of them refuses. Any malformed or unrecognised field refuses. */
export function readSecretRedaction(scope: unknown, detectorIds: readonly string[]): SecretRedactionRead {
  const refuse = (why: string): SecretRedactionRead => ({ ok: false, why: `its secret redaction ${why}` });
  if (!isObject(scope) || !Object.hasOwn(scope, 'secretRedaction')) return { ok: true, redaction: null };
  const red = scope['secretRedaction'];
  if (!isObject(red)) return refuse('is not an object');
  const keys = Object.keys(red);
  if (keys.length !== REDACTION_KEYS.length || REDACTION_KEYS.some(key => !keys.includes(key))) return refuse(`carries the fields ${keys.join(', ')}, not exactly ${REDACTION_KEYS.join(', ')}`);
  for (const key of Object.keys(REDACTION_TEXTS) as (keyof typeof REDACTION_TEXTS)[]) {
    const value = red[key];
    if (typeof value !== 'string' || sha256(value) !== REDACTION_TEXTS[key]) return refuse(`${key} is not the text this screen implements`);
  }
  if (red['redactionClass'] !== 'redacted-span') return refuse('redactionClass is not redacted-span');
  const distinctStrings = (value: unknown): value is readonly string[] => Array.isArray(value) && value.length > 0 && new Set(value).size === value.length
    && value.every(entry => typeof entry === 'string' && entry.length > 0);
  const classes = red['redactedClasses'];
  if (!distinctStrings(classes) || !classes.every(entry => (KNOWN_CLASSES as readonly string[]).includes(entry))) return refuse('redactedClasses is not a non-empty list of distinct known classes');
  const whole = red['wholeArtifactDetectors'];
  if (!distinctStrings(whole) || !whole.every(id => detectorIds.includes(id))) return refuse('wholeArtifactDetectors is not a non-empty list of distinct detector ids of this policy');
  const fragments = red['wholeArtifactFragments'];
  if (!distinctStrings(fragments)) return refuse('wholeArtifactFragments is not a non-empty list of distinct non-empty strings');
  const guard = red['guardLines'];
  if (typeof guard !== 'number' || !Number.isSafeInteger(guard) || guard < 1 || guard > MAX_GUARD_LINES) return refuse(`guardLines is not an integer from 1 to ${MAX_GUARD_LINES}`);
  let pattern: RegExp;
  try { pattern = new RegExp(red['wholeArtifactLinePattern'] as string, 'u'); } catch { return refuse('wholeArtifactLinePattern does not compile'); }
  return { ok: true, redaction: Object.freeze({
    redactedClasses: Object.freeze([...classes]) as readonly PublicSourceContentClass[], wholeArtifactDetectors: Object.freeze([...whole]),
    wholeArtifactLinePattern: pattern, wholeArtifactFragments: Object.freeze([...fragments]), guardLines: guard,
  }) };
}

/** A detector as the policy declares it (`@syzygy/three-surface-poc-core`'s `SecretDetector`). */
export type RedactionDetector =
  | { readonly id: string; readonly kind: 'literal-fragment'; readonly values: readonly string[] }
  | { readonly id: string; readonly kind: 'regular-expression'; readonly pattern: string; readonly flags: string };
export interface DetectorMatch { readonly detectorId: string; readonly start: number; readonly end: number }
/** A compiled every-offset matcher; `limit` stops the scan once more than that many matches are found. */
export type EveryOffsetMatcher = (text: string, limit: number) => readonly DetectorMatch[];

/** Compiles the policy's detectors for every match from every start offset. Throws on a detector the policy's own compiler would also
 * refuse (the screens compile the same list with `compileDetectors` first). */
export function compileEveryOffsetMatcher(detectors: readonly RedactionDetector[]): EveryOffsetMatcher {
  const each = detectors.map((detector): ((text: string, out: DetectorMatch[], limit: number) => void) => {
    if (detector.kind === 'literal-fragment') {
      const values = [...detector.values];
      return (text, out, limit) => {
        for (const value of values) {
          for (let at = text.indexOf(value); at !== -1 && out.length <= limit; at = text.indexOf(value, at + 1)) out.push({ detectorId: detector.id, start: at, end: at + value.length });
        }
      };
    }
    // Sticky, without the global flag: `exec` then matches only at `lastIndex`, which is every offset in turn.
    const sticky = new RegExp(detector.pattern, `${detector.flags.replace(/[gy]/gu, '')}y`);
    return (text, out, limit) => {
      for (let at = 0; at < text.length && out.length <= limit; at++) {
        sticky.lastIndex = at;
        const match = sticky.exec(text);
        if (match !== null) out.push({ detectorId: detector.id, start: match.index, end: match.index + match[0].length });
      }
    };
  });
  return (text, limit) => {
    const out: DetectorMatch[] = [];
    for (const run of each) { run(text, out, limit); if (out.length > limit) break; }
    return out;
  };
}

/** A body's lines, each with its terminator; a final terminator ends the last line and opens none. */
export function bodyLines(body: string): readonly string[] {
  const out: string[] = [];
  let start = 0;
  for (let i = 0; i < body.length; i++) {
    const c = body[i];
    if (c !== '\n' && c !== '\r') continue;
    if (c === '\r' && body[i + 1] === '\n') i++;
    out.push(body.slice(start, i + 1));
    start = i + 1;
  }
  if (start < body.length) out.push(body.slice(start));
  return out;
}
const withoutTerminator = (line: string): string => line.replace(/(?:\r\n|\r|\n)$/u, '');

export type WholeExclusionCause = 'no-redaction-rule' | 'whole-artifact-detector' | 'key-header-fragment' | 'key-header-line' | 'class-not-redacted' | 'unplaceable-match'
  | 'match-limit' | 'retained-text-matches';
export type RedactionOutcome =
  /** No detector matched: the body is admitted unredacted, as before. */
  | { readonly kind: 'clean' }
  /** Excluded whole, as before, for the cause named. */
  | { readonly kind: 'excluded'; readonly cause: WholeExclusionCause }
  /** Retained as redacted-span: `withheld` are the 1-based withheld line numbers, ascending; `retained` is the body with each withheld
   * line emptied and its terminator kept; `detectorIds` are the ids of the detectors that matched, in policy order. */
  | { readonly kind: 'redacted'; readonly withheld: readonly number[]; readonly retained: string; readonly detectorIds: readonly string[] };

/** The rule over one body admitted under `contentClass`. `redaction` null (versions 1 to 3) excludes every matching body whole. */
export function redactBody(body: string, contentClass: PublicSourceContentClass | undefined, matcher: EveryOffsetMatcher, redaction: SecretRedaction | null): RedactionOutcome {
  const found = matcher(body, MAX_MATCHES);
  if (found.length === 0) return { kind: 'clean' };
  if (redaction === null) return { kind: 'excluded', cause: 'no-redaction-rule' };
  if (found.length > MAX_MATCHES) return { kind: 'excluded', cause: 'match-limit' };
  if (found.some(match => redaction.wholeArtifactDetectors.includes(match.detectorId))) return { kind: 'excluded', cause: 'whole-artifact-detector' };
  if (redaction.wholeArtifactFragments.some(fragment => body.includes(fragment))) return { kind: 'excluded', cause: 'key-header-fragment' };
  if (contentClass === undefined || !redaction.redactedClasses.includes(contentClass)) return { kind: 'excluded', cause: 'class-not-redacted' };
  const lines = bodyLines(body);
  if (lines.some(line => redaction.wholeArtifactLinePattern.test(withoutTerminator(line)))) return { kind: 'excluded', cause: 'key-header-line' };
  if (found.some(match => match.end <= match.start)) return { kind: 'excluded', cause: 'unplaceable-match' };
  const starts: number[] = [];
  let at = 0;
  for (const line of lines) { starts.push(at); at += line.length; }
  /** The 1-based line holding the character at `offset`. */
  const lineOf = (offset: number): number => {
    let lo = 0, hi = starts.length - 1;
    while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (starts[mid]! <= offset) lo = mid; else hi = mid - 1; }
    return lo + 1;
  };
  const held = new Set<number>();
  for (const match of found) {
    const first = lineOf(match.start), last = lineOf(match.end - 1);
    for (let n = first - redaction.guardLines; n <= last + redaction.guardLines; n++) if (n >= 1 && n <= lines.length) held.add(n);
  }
  const retained = lines.map((line, i) => (held.has(i + 1) ? line.slice(withoutTerminator(line).length) : line)).join('');
  if (matcher(retained, 0).length > 0) return { kind: 'excluded', cause: 'retained-text-matches' };
  const ids = [...new Set(found.map(match => match.detectorId))];
  return { kind: 'redacted', withheld: Object.freeze([...held].sort((a, b) => a - b)), retained, detectorIds: Object.freeze(ids) };
}

/** Whether the inclusive 1-based line range `[startLine, endLine]` includes a withheld line: such a span is withheld whole. */
export function spanTouchesWithheld(withheld: readonly number[], startLine: number, endLine: number): boolean {
  return withheld.some(line => line >= startLine && line <= endLine);
}

/** The marker that replaces one run of consecutive withheld lines wherever a retained body is shown or carried: it names the redaction
 * and the body's total withheld-line count (`secretRedaction.withheldLines`). */
export const redactionMarker = (total: number): string => `[redacted-span: ${total} withheld line(s) in this file]`;

/** The retained body as it may be shown or carried: each run of consecutive withheld lines becomes one marker line (with the run's
 * last terminator, or none at the end of a body without one). */
export function retainedWithMarkers(retained: string, withheld: readonly number[]): string {
  const lines = bodyLines(retained), held = new Set(withheld), marker = redactionMarker(withheld.length);
  const out: string[] = [];
  for (let i = 0; i < lines.length; i++) {
    if (!held.has(i + 1)) { out.push(lines[i]!); continue; }
    let j = i;
    while (j + 1 < lines.length && held.has(j + 2)) j++;
    out.push(marker + lines[j]!);
    i = j;
  }
  return out.join('');
}
