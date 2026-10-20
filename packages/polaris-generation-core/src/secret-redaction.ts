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
 *   lines (zero length), or a scan past its bound (more than `MAX_MATCHES` matches or `MAX_MATCHED_UNITS` matched code units):
 *   excluded whole, as before;
 * - otherwise each line a match touches, and `guardLines` lines before and after it, is withheld; the retained text is the body with
 *   each withheld line emptied but its terminator kept (so line numbers do not move; a body whose retained text would re-split into
 *   other lines, a bare CR joining the next emptied line's LF, is excluded whole); every detector runs again over it, and any match
 *   excludes the body whole.
 *
 * Lines are split at LF, CRLF or CR, and a final terminator opens no line, as the generator counts lines (`lineCount`).
 *
 * Resource bound: whether each detector matches at all is decided by one ordinary search per detector, the version-3 screens' cost, and
 * every cause that needs no more (no match, a whole-artifact detector, a fragment, a class outside `redactedClasses`, the line pattern)
 * is decided before the every-offset scan, so a code-content body never pays that scan. The scan adds what an ordinary search skips:
 * the attempts at offsets inside or after a match. [Inferred] a failed attempt costs what a search's attempt at that offset costs, and
 * a successful one about its match's length; overlapping matches can each run to the end of the body (a body of `token=` repeated
 * scanned unbounded cost about MAX_MATCHES times its length), so the scan stops past `MAX_MATCHES` matches or `MAX_MATCHED_UNITS`
 * matched code units and the body is excluded whole. Not repaired here (the policy's own residuals): a secret no detector matches,
 * beyond the guard lines or continuing past them, is admitted; the whole body's digest and object id stay recorded and can check a
 * guess at a short withheld line. */

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
/** More matched UTF-16 code units than this, summed over every match, excludes the body whole: a successful attempt costs about its
 * match's length, and overlapping matches can each run to the end of the body. */
export const MAX_MATCHED_UNITS = 1_000_000;
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
/** A compiled matcher over the policy's detectors. */
export interface EveryOffsetMatcher {
  /** The ids of the detectors that match the text anywhere, in policy order: one ordinary left-to-right search per detector. A detector
   * makes a match from some offset exactly when such a search finds one, so this is the every-offset reading's "no match" test at the
   * cost of the version-3 screens' own search. */
  readonly matching: (text: string) => readonly string[];
  /** Every match from every start offset, overlapping matches included; `null` once the scan has found more than `MAX_MATCHES` matches
   * or more than `MAX_MATCHED_UNITS` matched UTF-16 code units in all, so the scan's work is bounded (`redactBody` then excludes the
   * body whole). */
  readonly every: (text: string) => readonly DetectorMatch[] | null;
}

/** Compiles the policy's detectors. Throws on a detector the policy's own compiler would also refuse (the screens compile the same list
 * with `compileDetectors` first). */
export function compileEveryOffsetMatcher(detectors: readonly RedactionDetector[]): EveryOffsetMatcher {
  type Budget = { matches: number; units: number };
  const spend = (budget: Budget, length: number): boolean => { budget.matches += 1; budget.units += length; return budget.matches <= MAX_MATCHES && budget.units <= MAX_MATCHED_UNITS; };
  const each = detectors.map((detector): { readonly any: (text: string) => boolean; readonly all: (text: string, out: DetectorMatch[], budget: Budget) => boolean } => {
    if (detector.kind === 'literal-fragment') {
      const values = [...detector.values];
      return {
        any: text => values.some(value => text.includes(value)),
        all: (text, out, budget) => {
          for (const value of values) {
            for (let at = text.indexOf(value); at !== -1; at = text.indexOf(value, at + 1)) {
              out.push({ detectorId: detector.id, start: at, end: at + value.length });
              if (!spend(budget, value.length)) return false;
            }
          }
          return true;
        },
      };
    }
    const flags = detector.flags.replace(/[gy]/gu, '');
    const search = new RegExp(detector.pattern, flags);
    // Sticky, without the global flag: `exec` then matches only at `lastIndex`, which is every offset in turn.
    const sticky = new RegExp(detector.pattern, `${flags}y`);
    return {
      any: text => search.test(text),
      all: (text, out, budget) => {
        for (let at = 0; at < text.length; at++) {
          sticky.lastIndex = at;
          const match = sticky.exec(text);
          if (match === null) continue;
          out.push({ detectorId: detector.id, start: match.index, end: match.index + match[0].length });
          if (!spend(budget, match[0].length)) return false;
        }
        return true;
      },
    };
  });
  return {
    matching: text => detectors.flatMap((detector, i) => (each[i]!.any(text) ? [detector.id] : [])),
    every: text => {
      const out: DetectorMatch[] = [], budget: Budget = { matches: 0, units: 0 };
      for (const run of each) if (!run.all(text, out, budget)) return null;
      return out;
    },
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
  | 'match-limit' | 'retained-lines-moved' | 'retained-text-matches';
export type RedactionOutcome =
  /** No detector matched: the body is admitted unredacted, as before. */
  | { readonly kind: 'clean' }
  /** Excluded whole, as before, for the cause named. */
  | { readonly kind: 'excluded'; readonly cause: WholeExclusionCause }
  /** Retained as redacted-span: `withheld` are the 1-based withheld line numbers, ascending; `retained` is the body with each withheld
   * line emptied and its terminator kept; `lines` is the body's line count, which every line of `retained` keeps its number within
   * (a withheld final line without a terminator empties to nothing, so `retained` alone can count one line fewer); `detectorIds` are
   * the ids of the detectors that matched, in policy order. */
  | { readonly kind: 'redacted'; readonly withheld: readonly number[]; readonly retained: string; readonly lines: number; readonly detectorIds: readonly string[] };

/** The rule over one body admitted under `contentClass`. `redaction` null (versions 1 to 3) excludes every matching body whole.
 *
 * The causes that need only whether a detector matches (and which) are decided first, by one ordinary search per detector; only a body
 * that can still be retained pays the every-offset scan, and that scan is bounded (`MAX_MATCHES`, `MAX_MATCHED_UNITS`). */
export function redactBody(body: string, contentClass: PublicSourceContentClass | undefined, matcher: EveryOffsetMatcher, redaction: SecretRedaction | null): RedactionOutcome {
  const matching = matcher.matching(body);
  if (matching.length === 0) return { kind: 'clean' };
  if (redaction === null) return { kind: 'excluded', cause: 'no-redaction-rule' };
  if (matching.some(id => redaction.wholeArtifactDetectors.includes(id))) return { kind: 'excluded', cause: 'whole-artifact-detector' };
  if (redaction.wholeArtifactFragments.some(fragment => body.includes(fragment))) return { kind: 'excluded', cause: 'key-header-fragment' };
  if (contentClass === undefined || !redaction.redactedClasses.includes(contentClass)) return { kind: 'excluded', cause: 'class-not-redacted' };
  const lines = bodyLines(body);
  if (lines.some(line => redaction.wholeArtifactLinePattern.test(withoutTerminator(line)))) return { kind: 'excluded', cause: 'key-header-line' };
  const found = matcher.every(body);
  if (found === null) return { kind: 'excluded', cause: 'match-limit' };
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
  const kept = lines.map((line, i) => (held.has(i + 1) ? line.slice(withoutTerminator(line).length) : line));
  const retained = kept.join('');
  // Line numbers never move: the retained text must split into exactly these lines. A kept line ending in a bare CR followed by an
  // emptied line whose terminator is LF would join into one CRLF line, so such a body is excluded whole. Only a withheld final line
  // without a terminator may vanish from the text (it empties to nothing); `lines` still counts it.
  const expected = kept.length > 0 && kept[kept.length - 1] === '' ? kept.slice(0, -1) : kept;
  const split = bodyLines(retained);
  if (split.length !== expected.length || split.some((line, i) => line !== expected[i])) return { kind: 'excluded', cause: 'retained-lines-moved' };
  if (matcher.matching(retained).length > 0) return { kind: 'excluded', cause: 'retained-text-matches' };
  const ids = [...new Set(found.map(match => match.detectorId))];
  return { kind: 'redacted', withheld: Object.freeze([...held].sort((a, b) => a - b)), retained, lines: lines.length, detectorIds: Object.freeze(ids) };
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
