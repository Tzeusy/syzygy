import { createHash } from 'node:crypto';

import { digestCanonicalJson } from './canonical-json.js';
import { parseBoundedJson } from './parse-json.js';
import { validateGenerationSources, type GenerationSource } from './generation-source.js';
import { checkBlockQuotes, sourceTextById } from './quote-fidelity.js';

/**
 * Evaluation harness for a generated static Polaris dossier (TRACKER G5,
 * gap #10). Pure: the caller supplies the dossier's bytes, the admitted
 * sources, the frozen reader questions and an answer port. It measures and
 * records; it never grades a reader's answer, awards acceptance or calls a
 * model. Absent evidence is reported as Unknown, never as a pass (VIS-2).
 *
 * Input format (`polaris-dossier-v1`), agreed with the multi-page output
 * (gap #8):
 * - `dossier.json`: `{ format, title, entryPage, pages: [{ path, depth }] }`.
 *   The entry page is the only page at depth 0.
 * - Page markup, read from the bytes, never from the manifest:
 *   `data-reading-level="n"` (0 is the first reading level);
 *   `<section id data-topics="…">` names the owner topics a section claims to
 *   answer; `data-claim-id` with `data-epistemic="observed|inferred|unknown"`;
 *   `data-quote-source`, `data-quote-start`, `data-quote-end` (UTF-8 byte
 *   offsets into the admitted body) on an element whose decoded text is
 *   exactly those bytes.
 */

export const DOSSIER_FORMAT = 'polaris-dossier-v1';
export const READER_QUESTIONS_FORMAT = 'polaris-reader-questions-v1';
export const OWNER_TOPICS = ['core-ideas', 'end-to-end-workflows', 'mechanisms', 'maintainer-stated-advantages', 'trade-offs'] as const;
export type OwnerTopic = typeof OWNER_TOPICS[number];
const EPISTEMIC = ['observed', 'inferred', 'unknown'] as const;
type Epistemic = typeof EPISTEMIC[number];

const JSON_LIMITS = { maxBytes: 4_000_000, maxNodes: 200_000, maxDepth: 32 } as const;

export class DossierEvaluationError extends Error {
  constructor(readonly code: 'invalid-manifest' | 'invalid-questions' | 'questions-not-frozen' | 'missing-page' | 'invalid-answer') {
    super(`Dossier evaluation refused: ${code}`);
    this.name = 'DossierEvaluationError';
  }
}

export interface DossierManifest {
  readonly format: typeof DOSSIER_FORMAT;
  readonly title: string;
  readonly entryPage: string;
  readonly pages: readonly { readonly path: string; readonly depth: number }[];
}

export interface ReaderQuestion { readonly id: string; readonly topics: readonly OwnerTopic[]; readonly text: string }

const isRecord = (value: unknown): value is Record<string, unknown> => value !== null && typeof value === 'object' && !Array.isArray(value);
const onlyKeys = (value: Record<string, unknown>, keys: readonly string[]): boolean => Object.keys(value).every(key => keys.includes(key));
const handle = /^[A-Za-z0-9][A-Za-z0-9_.:-]{0,99}$/u;

/** A relative POSIX path inside the run directory: no root, no `.` or `..`, no backslash. */
export function isDossierPagePath(path: unknown): path is string {
  return typeof path === 'string' && path.length > 0 && path.length <= 300 && !path.startsWith('/') && !path.includes('\\') && !path.includes('\0')
    && path.split('/').every(part => part !== '' && part !== '.' && part !== '..');
}

export function parseDossierManifest(text: string): DossierManifest {
  const fail = (): never => { throw new DossierEvaluationError('invalid-manifest'); };
  let value: unknown;
  try { value = parseBoundedJson(text, JSON_LIMITS); } catch { return fail(); }
  if (!isRecord(value) || !onlyKeys(value, ['format', 'title', 'entryPage', 'pages']) || value.format !== DOSSIER_FORMAT
    || typeof value.title !== 'string' || !value.title.trim() || !isDossierPagePath(value.entryPage) || !Array.isArray(value.pages) || value.pages.length === 0) fail();
  const record = value as Record<string, unknown> & { pages: unknown[] };
  const seen = new Set<string>();
  const pages = record.pages.map(page => {
    if (!isRecord(page) || !onlyKeys(page, ['path', 'depth']) || !isDossierPagePath(page.path)
      || !Number.isSafeInteger(page.depth) || (page.depth as number) < 0 || seen.has(page.path)) fail();
    const entry = page as { path: string; depth: number };
    seen.add(entry.path);
    return { path: entry.path, depth: entry.depth };
  });
  const atZero = pages.filter(page => page.depth === 0);
  if (atZero.length !== 1 || atZero[0]!.path !== record.entryPage) fail();
  return { format: DOSSIER_FORMAT, title: record.title as string, entryPage: record.entryPage as string, pages };
}

export function parseReaderQuestions(text: string): readonly ReaderQuestion[] {
  const fail = (): never => { throw new DossierEvaluationError('invalid-questions'); };
  let value: unknown;
  try { value = parseBoundedJson(text, JSON_LIMITS); } catch { return fail(); }
  if (!isRecord(value) || !onlyKeys(value, ['format', 'questions']) || value.format !== READER_QUESTIONS_FORMAT
    || !Array.isArray(value.questions) || value.questions.length === 0) fail();
  const seen = new Set<string>();
  return (value as { questions: unknown[] }).questions.map(question => {
    if (!isRecord(question) || !onlyKeys(question, ['id', 'topics', 'text']) || typeof question.id !== 'string' || !handle.test(question.id)
      || seen.has(question.id) || typeof question.text !== 'string' || !question.text.trim() || !Array.isArray(question.topics)
      || question.topics.some(topic => !(OWNER_TOPICS as readonly unknown[]).includes(topic)) || new Set(question.topics).size !== question.topics.length) fail();
    const entry = question as { id: string; topics: OwnerTopic[]; text: string };
    seen.add(entry.id);
    return { id: entry.id, topics: [...entry.topics], text: entry.text };
  });
}

// ---------------------------------------------------------------------------
// Page scanning. A small tag scanner, not a general HTML parser: generated
// dossier pages are well-formed, and anything it cannot read is a finding.

// One string, not a list of literals: the response-ceiling check (C3) flags a
// quoted two-letter element name as a content-coding token.
const VOID = new Set('area base br col embed hr img input link meta source track wbr'.split(' '));
const RAW_TEXT = new Set(['script', 'style', 'textarea', 'title']);
const NAMED_ENTITIES: Record<string, string> = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' };

/** Decodes the entities a renderer's `escape` emits plus numeric references; any other named entity stays literal. */
export function decodeHtmlText(text: string): string {
  return text.replace(/&(?:#(\d{1,7})|#[xX]([0-9a-fA-F]{1,6})|([A-Za-z]+));/gu, (match, decimal: string | undefined, hex: string | undefined, name: string | undefined) => {
    if (name !== undefined) return NAMED_ENTITIES[name] ?? match;
    const code = decimal !== undefined ? Number.parseInt(decimal, 10) : Number.parseInt(hex!, 16);
    return code <= 0x10ffff && !(code >= 0xd800 && code <= 0xdfff) ? String.fromCodePoint(code) : match;
  });
}

const countWords = (text: string): number => text.match(/\S+/gu)?.length ?? 0;

function attributes(source: string): Map<string, string> {
  const out = new Map<string, string>();
  for (const match of source.matchAll(/([^\s=/>"']+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"']+)))?/gu)) {
    out.set(match[1]!.toLowerCase(), decodeHtmlText(match[2] ?? match[3] ?? match[4] ?? ''));
  }
  return out;
}

export interface ScannedSection { readonly id: string | null; readonly topics: readonly string[] }
export interface ScannedClaim {
  readonly id: string;
  readonly epistemic: string | null;
  readonly hasQuote: boolean;
  /** The claim element's text as a reader sees it (entities decoded, tags removed). */
  readonly text: string;
  /** Source ids named by `Read source <id>` anchors inside the claim, in page order. */
  readonly citedSourceIds: readonly string[];
}
export interface ScannedQuote { readonly sourceId: string | null; readonly start: string | null; readonly end: string | null; readonly text: string }
export interface ScannedPage {
  readonly bytes: number;
  /** Words by reading level; `unlabelled` holds body text under no marked level. */
  readonly words: { readonly byLevel: Readonly<Record<string, number>>; readonly unlabelled: number };
  /** UTF-8 bytes from the start of the file through the close of the last level-0 element; null when the page marks none. */
  readonly bytesThroughFirstLevel: number | null;
  readonly sections: readonly ScannedSection[];
  readonly ids: ReadonlySet<string>;
  readonly claims: readonly ScannedClaim[];
  readonly quotes: readonly ScannedQuote[];
  readonly findings: readonly string[];
}

interface Open { readonly name: string; readonly level: string | null; readonly quote: { text: string } | null; readonly claim: { hasQuote: boolean; text: string; citedSourceIds: string[] } | null }

export function scanDossierPage(html: string): ScannedPage {
  const byLevel: Record<string, number> = {};
  let unlabelled = 0;
  let lastLevelZeroClose: number | null = null;
  const sections: ScannedSection[] = [];
  const ids = new Set<string>();
  const claims: { id: string; epistemic: string | null; hasQuote: boolean; text: string; citedSourceIds: string[] }[] = [];
  const quotes: (ScannedQuote & { text: string })[] = [];
  const findings: string[] = [];
  const stack: Open[] = [];
  const level = (): string | null => {
    for (let i = stack.length - 1; i >= 0; i--) if (stack[i]!.level !== null) return stack[i]!.level;
    return null;
  };
  const text = (raw: string): void => {
    // HTML input-stream preprocessing: a reader's DOM has LF where the bytes have
    // CRLF or a lone CR, so a source CR survives only as a character reference.
    const decoded = decodeHtmlText(raw.replace(/\r\n?/gu, '\n'));
    for (const open of stack) { if (open.quote !== null) open.quote.text += decoded; if (open.claim !== null) open.claim.text += decoded; }
    const words = countWords(decoded);
    if (words === 0) return;
    const current = level();
    if (current === null) unlabelled += words;
    else byLevel[current] = (byLevel[current] ?? 0) + words;
  };
  const token = /<!--[\s\S]*?-->|<!\[CDATA\[[\s\S]*?\]\]>|<![^>]*>|<\/\s*([A-Za-z][\w-]*)\s*>|<([A-Za-z][\w-]*)((?:"[^"]*"|'[^']*'|[^'">])*)>/gu;
  let cursor = 0;
  let match: RegExpExecArray | null;
  while ((match = token.exec(html)) !== null) {
    text(html.slice(cursor, match.index));
    cursor = token.lastIndex;
    if (match[1] !== undefined) {
      const name = match[1].toLowerCase();
      const at = stack.map(open => open.name).lastIndexOf(name);
      if (at === -1) { findings.push(`unmatched-close:${name}`); continue; }
      if (at !== stack.length - 1) findings.push(`implicit-close:${stack.slice(at + 1).map(open => open.name).join(',')}`);
      for (const closed of stack.splice(at)) {
        if (closed.level === '0') lastLevelZeroClose = Buffer.byteLength(html.slice(0, cursor), 'utf8');
      }
      continue;
    }
    if (match[2] === undefined) continue;
    const name = match[2].toLowerCase();
    const attrs = attributes(match[3] ?? '');
    const id = attrs.get('id');
    if (id !== undefined) {
      if (ids.has(id)) findings.push(`duplicate-id:${id}`);
      ids.add(id);
    }
    if (name === 'section') {
      const topics = (attrs.get('data-topics') ?? '').split(/\s+/u).filter(Boolean);
      for (const topic of topics) if (!(OWNER_TOPICS as readonly string[]).includes(topic)) findings.push(`unknown-topic:${topic}`);
      sections.push({ id: id ?? null, topics });
      if (id === undefined) findings.push('section-without-id');
    }
    const claimId = attrs.get('data-claim-id');
    let claim: { id: string; epistemic: string | null; hasQuote: boolean; text: string; citedSourceIds: string[] } | null = null;
    if (claimId !== undefined) {
      claim = { id: claimId, epistemic: attrs.has('data-epistemic') ? attrs.get('data-epistemic')! : null, hasQuote: false, text: '', citedSourceIds: [] };
      claims.push(claim);
    }
    const cited = name === 'a' ? /^Read source (.+)$/u.exec(attrs.get('aria-label') ?? '') : null;
    if (cited !== null) for (const open of stack) if (open.claim !== null) open.claim.citedSourceIds.push(cited[1]!);
    let quote: { text: string } | null = null;
    if (attrs.has('data-quote-source') || attrs.has('data-quote-start') || attrs.has('data-quote-end')) {
      for (const open of stack) if (open.claim !== null) open.claim.hasQuote = true;
      if (claim !== null) claim.hasQuote = true;
      const record = { sourceId: attrs.get('data-quote-source') ?? null, start: attrs.get('data-quote-start') ?? null, end: attrs.get('data-quote-end') ?? null, text: '' };
      quotes.push(record);
      quote = record;
    }
    let readingLevel: string | null = null;
    if (attrs.has('data-reading-level')) {
      const value = attrs.get('data-reading-level')!;
      if (/^(?:0|[1-9]\d{0,2})$/u.test(value)) readingLevel = value;
      else findings.push(`invalid-reading-level:${value}`);
    }
    const selfClosing = (match[3] ?? '').trimEnd().endsWith('/');
    if (VOID.has(name) || selfClosing) continue;
    if (RAW_TEXT.has(name)) {
      const close = new RegExp(`</${name}\\s*>`, 'giu');
      close.lastIndex = cursor;
      const end = close.exec(html);
      const body = html.slice(cursor, end === null ? html.length : end.index);
      // Script, style and title text is not page reading; a textarea's is.
      if (name === 'textarea') { stack.push({ name, level: readingLevel, quote, claim }); text(body); stack.pop(); }
      cursor = end === null ? html.length : close.lastIndex;
      token.lastIndex = cursor;
      if (end === null) findings.push(`unclosed:${name}`);
      continue;
    }
    stack.push({ name, level: readingLevel, quote, claim });
  }
  text(html.slice(cursor));
  if (stack.some(open => open.name !== 'html' && open.name !== 'body')) findings.push(`unclosed:${stack.map(open => open.name).join(',')}`);
  return {
    bytes: Buffer.byteLength(html, 'utf8'),
    words: { byLevel, unlabelled },
    bytesThroughFirstLevel: lastLevelZeroClose,
    sections, ids, claims, quotes, findings,
  };
}

// ---------------------------------------------------------------------------
// (a) Reader cost.

export interface PageBudget {
  readonly maxFirstLevelWords?: number;
  readonly maxFirstLevelBytes?: number;
  readonly maxPageBytes?: number;
  readonly maxTotalBytes?: number;
}
export type BoundOutcome = { readonly bound: number; readonly observed: number; readonly outcome: 'within' | 'over' }
  | { readonly outcome: 'unknown'; readonly reason: 'no-budget-declared' | 'not-measurable' };

export function parsePageBudget(text: string): PageBudget {
  let value: unknown;
  try { value = parseBoundedJson(text, JSON_LIMITS); } catch { throw new DossierEvaluationError('invalid-manifest'); }
  const keys = ['maxFirstLevelWords', 'maxFirstLevelBytes', 'maxPageBytes', 'maxTotalBytes'];
  if (!isRecord(value) || !onlyKeys(value, keys) || Object.values(value).some(bound => !Number.isSafeInteger(bound) || (bound as number) <= 0)) {
    throw new DossierEvaluationError('invalid-manifest');
  }
  return value as PageBudget;
}

function bound(limit: number | undefined, observed: number | null): BoundOutcome {
  if (limit === undefined) return { outcome: 'unknown', reason: 'no-budget-declared' };
  if (observed === null) return { outcome: 'unknown', reason: 'not-measurable' };
  return { bound: limit, observed, outcome: observed <= limit ? 'within' : 'over' };
}

export function readerCost(manifest: DossierManifest, scanned: ReadonlyMap<string, ScannedPage>, budget: PageBudget = {}) {
  const entry = scanned.get(manifest.entryPage)!;
  const firstLevelWords = entry.words.byLevel['0'] ?? null;
  const pages = manifest.pages.map(page => {
    const scan = scanned.get(page.path)!;
    return { path: page.path, depth: page.depth, bytes: scan.bytes, wordsByReadingLevel: scan.words.byLevel, unlabelledWords: scan.words.unlabelled, pageBudget: bound(budget.maxPageBytes, scan.bytes) };
  });
  const depths = [...new Set(manifest.pages.map(page => page.depth))].sort((a, b) => a - b);
  const sum = (values: number[]): number => values.reduce((total, value) => total + value, 0);
  const totalBytes = sum(pages.map(page => page.bytes));
  return {
    firstReadingLevel: {
      page: manifest.entryPage,
      entryPageBytes: entry.bytes,
      bytesThroughFirstLevel: entry.bytesThroughFirstLevel,
      // Null, not zero, when the entry page marks no level-0 content (VIS-2).
      words: firstLevelWords,
      wordBudget: bound(budget.maxFirstLevelWords, firstLevelWords),
      byteBudget: bound(budget.maxFirstLevelBytes, entry.bytesThroughFirstLevel),
    },
    perPageDepth: depths.map(depth => {
      const atDepth = pages.filter(page => page.depth === depth);
      return { depth, pages: atDepth.length, bytes: sum(atDepth.map(page => page.bytes)), words: sum(atDepth.map(page => sum(Object.values(page.wordsByReadingLevel)) + page.unlabelledWords)) };
    }),
    perReadingLevel: Object.fromEntries([...new Set(pages.flatMap(page => Object.keys(page.wordsByReadingLevel)))].sort((a, b) => Number(a) - Number(b))
      .map(level => [level, sum(pages.map(page => page.wordsByReadingLevel[level] ?? 0))])),
    unlabelledWords: sum(pages.map(page => page.unlabelledWords)),
    pages,
    totalBytes,
    totalBudget: bound(budget.maxTotalBytes, totalBytes),
  };
}

// ---------------------------------------------------------------------------
// (b) Fidelity: quotes resolve exactly to admitted bytes; every claim is labelled.

export type QuoteOutcome = 'exact' | 'text-mismatch' | 'unknown-source' | 'unquotable-source' | 'invalid-offsets' | 'out-of-range' | 'crosses-piece-boundary' | 'not-utf8-boundary';

function admittedBody(source: GenerationSource): string | null {
  if (source.exclusion.excluded || source.classificationBasis !== 'body') return null;
  if (source.body !== undefined) return source.body;
  const only = source.spans.length === 1 ? source.spans[0]! : undefined;
  return only !== undefined && only.start === 0 ? only.text : null;
}

/** Quote offsets are blob-absolute UTF-8 byte offsets, the same base as the
 * anchors: a piece of a segmented blob resolves them by subtracting its
 * `segment.start`, and a quote must lie wholly inside the named piece. */
export function resolveQuote(quote: ScannedQuote, sources: ReadonlyMap<string, GenerationSource>): QuoteOutcome {
  const source = quote.sourceId === null ? undefined : sources.get(quote.sourceId);
  if (source === undefined) return 'unknown-source';
  const body = admittedBody(source);
  if (body === null) return 'unquotable-source';
  if (quote.start === null || quote.end === null || !/^(?:0|[1-9]\d{0,9})$/u.test(quote.start) || !/^(?:0|[1-9]\d{0,9})$/u.test(quote.end)) return 'invalid-offsets';
  const start = Number(quote.start);
  const end = Number(quote.end);
  const bytes = Buffer.from(body, 'utf8');
  if (end <= start) return 'invalid-offsets';
  const base = source.segment?.start ?? 0;
  if (source.segment !== undefined && (start < base || end > source.segment.end)) {
    return start < source.segment.end && end > base ? 'crosses-piece-boundary' : 'out-of-range';
  }
  if (end - base > bytes.length) return 'out-of-range';
  let decoded: string;
  try { decoded = new TextDecoder('utf-8', { fatal: true }).decode(bytes.subarray(start - base, end - base)); }
  catch { return 'not-utf8-boundary'; }
  return decoded === quote.text ? 'exact' : 'text-mismatch';
}

export function fidelity(manifest: DossierManifest, scanned: ReadonlyMap<string, ScannedPage>, sources: readonly GenerationSource[]) {
  validateGenerationSources(sources);
  const index = new Map(sources.map(source => [source.sourceId, source]));
  const quotes = manifest.pages.flatMap(page => scanned.get(page.path)!.quotes.map(quote => ({
    page: page.path, sourceId: quote.sourceId, start: quote.start, end: quote.end, outcome: resolveQuote(quote, index),
  })));
  const claimIds = new Map<string, number>();
  const claims = manifest.pages.flatMap(page => scanned.get(page.path)!.claims.map(claim => {
    claimIds.set(claim.id, (claimIds.get(claim.id) ?? 0) + 1);
    const label = claim.epistemic === null ? 'missing-label' as const
      : (EPISTEMIC as readonly string[]).includes(claim.epistemic) ? claim.epistemic as Epistemic : 'invalid-label' as const;
    return { page: page.path, claimId: claim.id, label, hasQuote: claim.hasQuote };
  }));
  // Quotation marks inside a cited block: every quoted span must occur, normalised, in a source that block cites. A claim naming no source is not a block.
  const sourceText = sourceTextById(sources.filter(source => !source.exclusion.excluded && source.spans.length === 1).map(source => ({ sourceId: source.sourceId, text: source.spans[0]!.text })));
  const checkedBlocks = manifest.pages.flatMap(page => scanned.get(page.path)!.claims.filter(claim => claim.citedSourceIds.length > 0).map(claim => ({ page: page.path, claim })));
  const quoteFailures = checkedBlocks.flatMap(({ page, claim }) => checkBlockQuotes({ id: claim.id, text: claim.text, sourceIds: claim.citedSourceIds }, sourceText)
    .map(finding => ({ page, claimId: finding.blockId, kind: finding.kind, quote: finding.quote })));
  const failedQuotes = quotes.filter(quote => quote.outcome !== 'exact');
  const unlabelled = claims.filter(claim => claim.label === 'missing-label' || claim.label === 'invalid-label');
  const duplicateClaimIds = [...claimIds].filter(([, count]) => count > 1).map(([id]) => id).sort();
  const outcome = <T extends string>(population: number, failures: number, pass: T): T | 'failures' | 'unknown' =>
    failures > 0 ? 'failures' : population === 0 ? 'unknown' : pass;
  return {
    quotes: { denominator: quotes.length, exact: quotes.length - failedQuotes.length, failures: failedQuotes.map(({ page, sourceId, start, end, outcome: result }) => ({ page, sourceId, start, end, outcome: result })), outcome: outcome(quotes.length, failedQuotes.length, 'all-resolved') },
    inBlockQuotes: { denominator: checkedBlocks.length, failures: quoteFailures,
      outcome: quoteFailures.length > 0 ? 'failures' as const : checkedBlocks.length === 0 ? 'unknown' as const : 'all-verbatim' as const },
    claims: {
      denominator: claims.length,
      labelled: claims.length - unlabelled.length,
      byLabel: Object.fromEntries(EPISTEMIC.map(label => [label, claims.filter(claim => claim.label === label).length])),
      // A label is checked for presence and vocabulary only. An Observed claim
      // carrying no quote of its own has no exact-source check behind it here.
      observedWithoutQuote: claims.filter(claim => claim.label === 'observed' && !claim.hasQuote).map(({ page, claimId }) => ({ page, claimId })),
      unlabelled: unlabelled.map(({ page, claimId, label }) => ({ page, claimId, label })),
      duplicateClaimIds,
      outcome: outcome(claims.length, unlabelled.length + duplicateClaimIds.length, 'all-labelled'),
    },
  };
}

// ---------------------------------------------------------------------------
// (c) Reader test scaffolding. A fresh reader per question sees the question
// text and the page bytes only: no topics, sources, manifest or prior answers.

export interface ReaderLocation { readonly page: string; readonly sectionId: string }
export type ReaderAnswer =
  | { readonly kind: 'answered'; readonly text: string; readonly citations: readonly ReaderLocation[]; readonly attemptedPaths: readonly string[] }
  | { readonly kind: 'cannot-answer'; readonly reason: string; readonly attemptedPaths: readonly string[] };
export interface ReaderAnswerPort {
  answer(input: { readonly question: { readonly id: string; readonly text: string }; readonly pages: readonly { readonly path: string; readonly html: string }[] }, signal: AbortSignal): Promise<ReaderAnswer>;
}

/** Creates one fresh reader per question. `kind` and `subjectSha256` bind the
 * report to what answered: a scripted citation never reads as reader evidence. */
export interface ReaderPortFactory {
  readonly kind: 'scripted';
  readonly subjectSha256: string;
  create(): ReaderAnswerPort;
}

/** The only answer implementation: answers fixed in advance, keyed by question id. */
export function scriptedAnswers(script: Readonly<Record<string, ReaderAnswer>>): ReaderPortFactory {
  const frozen = structuredClone(script);
  return {
    kind: 'scripted',
    subjectSha256: digestCanonicalJson(frozen, JSON_LIMITS).digest,
    create: () => ({
      async answer({ question }) {
        const scripted = frozen[question.id];
        return scripted === undefined ? { kind: 'cannot-answer', reason: 'no scripted answer', attemptedPaths: [] } : structuredClone(scripted);
      },
    }),
  };
}

function checkAnswer(value: unknown): ReaderAnswer {
  const fail = (): never => { throw new DossierEvaluationError('invalid-answer'); };
  if (!isRecord(value) || !Array.isArray(value.attemptedPaths) || value.attemptedPaths.some(path => typeof path !== 'string')) fail();
  const answer = value as Record<string, unknown>;
  if (answer.kind === 'answered') {
    if (!onlyKeys(answer, ['kind', 'text', 'citations', 'attemptedPaths']) || typeof answer.text !== 'string' || !Array.isArray(answer.citations)
      || answer.citations.some(citation => !isRecord(citation) || !onlyKeys(citation, ['page', 'sectionId']) || typeof citation.page !== 'string' || typeof citation.sectionId !== 'string')) fail();
  } else if (answer.kind === 'cannot-answer') {
    if (!onlyKeys(answer, ['kind', 'reason', 'attemptedPaths']) || typeof answer.reason !== 'string') fail();
  } else fail();
  return value as ReaderAnswer;
}

export async function runReaderTest(questions: readonly ReaderQuestion[], manifest: DossierManifest, pages: ReadonlyMap<string, string>,
  scanned: ReadonlyMap<string, ScannedPage>, readers: ReaderPortFactory, signal: AbortSignal) {
  const pageInput = manifest.pages.map(page => ({ path: page.path, html: pages.get(page.path)! }));
  const results = [];
  for (const question of questions) {
    signal.throwIfAborted();
    const answer = checkAnswer(await readers.create().answer({ question: { id: question.id, text: question.text }, pages: pageInput.map(page => ({ ...page })) }, signal));
    const citations = answer.kind === 'answered' ? answer.citations.map(citation => ({
      ...citation,
      resolves: scanned.get(citation.page)?.sections.some(section => section.id === citation.sectionId) ?? false,
    })) : [];
    results.push({
      questionId: question.id,
      topics: question.topics,
      readerPort: readers.kind,
      kind: answer.kind,
      ...(answer.kind === 'answered' ? { text: answer.text } : { reason: answer.reason }),
      citations,
      attemptedPaths: answer.attemptedPaths.map(path => ({ path, known: scanned.has(path) })),
      // Recorded, never graded here: accuracy and comprehension are a later, separate judgement.
      accuracy: 'not-evaluated' as const,
    });
  }
  return results;
}

// ---------------------------------------------------------------------------
// (d) Coverage per owner topic.

type ReaderResult = Awaited<ReturnType<typeof runReaderTest>>[number];

export function topicCoverage(manifest: DossierManifest, scanned: ReadonlyMap<string, ScannedPage>, questions: readonly ReaderQuestion[], reader: readonly ReaderResult[] | null) {
  return OWNER_TOPICS.map(topic => {
    const declared = manifest.pages.flatMap(page => scanned.get(page.path)!.sections
      .filter(section => section.topics.includes(topic) && section.id !== null)
      .map(section => ({ page: page.path, sectionId: section.id! })));
    const asked = questions.filter(question => question.topics.includes(topic)).map(question => question.id);
    const answeredFrom = reader === null ? [] : reader
      .filter(result => result.topics.includes(topic) && result.kind === 'answered')
      .flatMap(result => result.citations.filter(citation => citation.resolves).map(citation => ({ questionId: result.questionId, page: citation.page, sectionId: citation.sectionId })));
    // A page's own declaration is the generator's assertion. A resolved answer
    // citation names where an answer was found; from a scripted port it is a
    // fixture, never reader evidence, and no citation is graded here.
    const status = answeredFrom.length > 0 ? 'scripted-answer-cited' as const : declared.length > 0 ? 'declared-only' as const : 'unknown' as const;
    return { topic, status, ...(answeredFrom.length > 0 ? { readerPort: 'scripted' as const, accuracy: 'not-evaluated' as const } : {}), declaredBy: declared, questions: asked, answerCitations: answeredFrom };
  });
}

// ---------------------------------------------------------------------------
// The whole evaluation over one dossier.

export interface DossierEvaluationInput {
  readonly manifestText: string;
  /** Raw page bytes by manifest path; every manifest page must be present. */
  readonly pages: ReadonlyMap<string, Uint8Array>;
  readonly sources: readonly GenerationSource[];
  readonly questionsText: string;
  /** When set, the questions file must hash to this digest: the freeze. */
  readonly expectedQuestionsSha256?: string;
  readonly budget?: PageBudget;
  /** Absent: the reader test is not run and every topic stays declared-only or Unknown. */
  readonly readers?: ReaderPortFactory;
}

const sha256 = (bytes: Uint8Array | string): string => createHash('sha256').update(bytes).digest('hex');

/** Canonical digest over the admitted population: each source's identity,
 * segment, exclusion and a SHA-256 of its body, in source-id order. */
export function admittedSourcesDigest(sources: readonly GenerationSource[]): { readonly count: number; readonly sha256: string } {
  const rows = [...sources].sort((a, b) => (a.sourceId < b.sourceId ? -1 : a.sourceId > b.sourceId ? 1 : 0)).map(source => ({
    sourceId: source.sourceId, repositoryId: source.repositoryId, revision: source.revision, path: source.path, objectId: source.objectId,
    segment: source.segment === undefined ? null : { ...source.segment }, exclusion: { ...source.exclusion },
    bodySha256: source.body === undefined ? null : sha256(source.body),
  }));
  return { count: rows.length, sha256: digestCanonicalJson(rows, { maxBytes: 64_000_000, maxNodes: 4_000_000, maxDepth: 8 }).digest };
}

export async function evaluateDossier(input: DossierEvaluationInput, signal: AbortSignal) {
  const manifest = parseDossierManifest(input.manifestText);
  const questions = parseReaderQuestions(input.questionsText);
  const questionsSha256 = sha256(input.questionsText);
  if (input.expectedQuestionsSha256 !== undefined && input.expectedQuestionsSha256 !== questionsSha256) throw new DossierEvaluationError('questions-not-frozen');
  const html = new Map<string, string>();
  const scanned = new Map<string, ScannedPage>();
  for (const page of manifest.pages) {
    const bytes = input.pages.get(page.path);
    if (bytes === undefined) throw new DossierEvaluationError('missing-page');
    const text = new TextDecoder('utf-8', { fatal: false }).decode(bytes);
    html.set(page.path, text);
    scanned.set(page.path, scanDossierPage(text));
  }
  const reader = input.readers === undefined ? null : await runReaderTest(questions, manifest, html, scanned, input.readers, signal);
  return {
    format: 'polaris-dossier-evaluation-v1',
    subject: {
      manifestSha256: sha256(input.manifestText),
      pages: manifest.pages.map(page => ({ path: page.path, sha256: sha256(input.pages.get(page.path)!) })),
      questionsSha256,
      sources: admittedSourcesDigest(input.sources),
      budgetSha256: input.budget === undefined ? null : digestCanonicalJson({ ...input.budget }, JSON_LIMITS).digest,
      readers: input.readers === undefined ? null : { kind: input.readers.kind, subjectSha256: input.readers.subjectSha256 },
    },
    title: manifest.title,
    scanFindings: manifest.pages.flatMap(page => scanned.get(page.path)!.findings.map(finding => ({ page: page.path, finding }))),
    readerCost: readerCost(manifest, scanned, input.budget),
    fidelity: fidelity(manifest, scanned, input.sources),
    readerTest: reader === null ? { run: false as const, reason: 'no answer port supplied' } : { run: true as const, readerPort: input.readers!.kind, results: reader },
    coverage: topicCoverage(manifest, scanned, questions, reader),
    providerCallPerformed: false,
  };
}
