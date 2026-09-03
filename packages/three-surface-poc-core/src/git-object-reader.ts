// Exact Git object reader — the PWB-REQ-006 read guard (task 2.3).
//
// This is the only door through which a phase B body may enter the POC.
// A path is read only when it is already a normalized repository-relative
// path (relative, NUL-free, no `.`/`..`/empty segments), its final segment
// passes the adopted secret policy's denied basename/prefix/suffix rules,
// the exact revision's tree lists a regular blob at that path (symlinks
// `120000`, submodules `160000` and trees are refused by mode, so the
// working tree is never consulted), and the declared resource limits are
// not breached. The reader then issues exactly one Git command, `cat-file
// blob <object-id>`, never a path-addressed read, verifies the returned
// bytes hash to the tree-named object id, and rejects NUL bytes, invalid
// UTF-8 and active content (raw HTML, scripts, SVG, event handlers,
// unsafe or entity-obfuscated URL schemes).
//
// Every attempt is ledgered by a body-free record: path, object id,
// outcome, byte count, sha256 content digest (hash, never body) and a
// closed reason. A refused, over-limit or active source stays counted —
// `readManifestSources` returns one result per manifest source, in
// manifest order, so the population never shrinks. The body itself is
// handed only to the caller's `consume` callback and is never stored on
// any record this module returns.
//
// The registry's resource limits are evaluation inputs: `evaluateLimit`
// is the one comparison every consumer uses (the reader for source count
// and bytes; the observer for index depth; later extraction/rendering for
// parse time and rendered bytes), so a breach is always the same shape.

import { createHash } from 'node:crypto';

import { type GitTreeEntry, type GitTreeIndex, normalizeRepositoryPath, posixBasename } from './git-tree.js';
import type { ManifestSource, ProjectShapeSourceManifest } from './project-shape-manifest.js';
import { type GitRunner, PWB_RESOURCE_LIMITS, type PwbResourceLimits, type ResourceLimitBreach, gitBlobObjectId } from './project-shape-observation.js';

// ---------------------------------------------------------------------
// Policy-bound path rules (copies of the act-bound secret policy's
// `sourceAdmission`; proven byte-equal in the test).

export const PWB_POLICY_IDENTITY = {
  policyId: 'polaris-butlers-project-shape-secrets',
  policyVersion: '1.0.0-candidate.4',
} as const;

export const PWB_DENIED_PATH_RULES = {
  basenames: ['.env', '.env.local', '.env.production', 'credentials.json', 'secrets.json', 'id_rsa', 'id_ed25519'],
  prefixes: ['.env.'],
  suffixes: ['.pem', '.key', '.p12', '.pfx'],
} as const;

export type DeniedPathRules = {
  readonly basenames: readonly string[];
  readonly prefixes: readonly string[];
  readonly suffixes: readonly string[];
};

// ---------------------------------------------------------------------
// Resource limits as evaluation inputs.

export function evaluateLimit(
  limits: PwbResourceLimits,
  limit: keyof PwbResourceLimits,
  observed: number,
  path?: string,
): ResourceLimitBreach | undefined {
  const declared = limits[limit];
  if (Number.isFinite(observed) && observed <= declared) return undefined;
  return path === undefined ? { limit, declared, observed } : { limit, declared, observed, path };
}

// ---------------------------------------------------------------------
// Read guard.

export const READ_REFUSAL_REASONS = [
  'path-escapes-repository', // absolute, NUL-bearing, empty, or `..` above the root
  'path-not-normalized', // contains `.`/`..`/empty segments or a trailing slash
  'denied-basename',
  'denied-prefix',
  'denied-suffix',
  'not-in-tree',
  'not-a-regular-blob', // symlink, submodule or tree entry
  'object-id-differs-from-tree',
] as const;
export type ReadRefusalReason = (typeof READ_REFUSAL_REASONS)[number];

export type ReadAdmission =
  | { readonly kind: 'admitted'; readonly entry: GitTreeEntry }
  | { readonly kind: 'refused'; readonly reason: ReadRefusalReason };

const REGULAR_BLOB_MODES: readonly string[] = ['100644', '100755'];
const OBJECT_ID = /^[0-9a-f]{40}$|^[0-9a-f]{64}$/;

// The policy applies basename and prefix rules to the final segment and
// suffix rules to the complete final segment. Comparison is
// case-insensitive: that only ever denies more.
export function deniedPathReason(path: string, rules: DeniedPathRules = PWB_DENIED_PATH_RULES): 'denied-basename' | 'denied-prefix' | 'denied-suffix' | undefined {
  const segment = posixBasename(path).toLowerCase();
  if (rules.basenames.some((name) => name.toLowerCase() === segment)) return 'denied-basename';
  if (rules.prefixes.some((prefix) => segment.startsWith(prefix.toLowerCase()))) return 'denied-prefix';
  if (rules.suffixes.some((suffix) => segment.endsWith(suffix.toLowerCase()))) return 'denied-suffix';
  return undefined;
}

export function admitExactObjectRead(
  tree: GitTreeIndex,
  path: string,
  expectedObjectId?: string,
  rules: DeniedPathRules = PWB_DENIED_PATH_RULES,
): ReadAdmission {
  const normalized = normalizeRepositoryPath(path);
  if (normalized === undefined) return { kind: 'refused', reason: 'path-escapes-repository' };
  if (normalized !== path) return { kind: 'refused', reason: 'path-not-normalized' };
  const denied = deniedPathReason(path, rules);
  if (denied !== undefined) return { kind: 'refused', reason: denied };
  const entry = tree.entryAt(path);
  if (entry === undefined) return { kind: 'refused', reason: 'not-in-tree' };
  if (entry.type !== 'blob' || !REGULAR_BLOB_MODES.includes(entry.mode) || !OBJECT_ID.test(entry.objectId)) {
    return { kind: 'refused', reason: 'not-a-regular-blob' };
  }
  if (expectedObjectId !== undefined && expectedObjectId !== entry.objectId) return { kind: 'refused', reason: 'object-id-differs-from-tree' };
  return { kind: 'admitted', entry };
}

// ---------------------------------------------------------------------
// Active content.
//
// The closed set of forms PWB-REQ-006 forbids from ever reaching a sink.
// A match excludes the whole source; the finding names only the form and
// where it starts, never the matched bytes.

export const ACTIVE_CONTENT_FORMS = [
  'html-tag', // any raw HTML tag (CommonMark autolinks are not tags)
  'html-comment-or-declaration', // `<!-- -->`, `<!DOCTYPE …>`, `<![CDATA[`, `<?…?>`
  'script-element',
  'svg-element',
  'event-handler-attribute', // `onload=`, `onerror=` … inside a tag
  'unsafe-url-scheme', // javascript:, vbscript:, data:, file: as a link or attribute target
  'obfuscated-link-destination', // an HTML entity inside a Markdown link destination
] as const;
export type ActiveContentForm = (typeof ACTIVE_CONTENT_FORMS)[number];

export interface ActiveContentFinding {
  readonly form: ActiveContentForm;
  readonly line: number;
  readonly column: number;
}

// A tag name must be followed by whitespace, `/>` or `>`, so CommonMark
// autolinks (`<https://…>`, `<me@…>`) never match: `:` and `@` end them.
const HTML_TAG = /<\/?([A-Za-z][A-Za-z0-9-]*)(?:\s[^<>]*)?\/?>/g;
const HTML_DECLARATION = /<(?:!--|!\[CDATA\[|![A-Za-z]|\?)/g;
const EVENT_HANDLER = /<[A-Za-z][^<>]*\son[a-z]+\s*=/gi;
// `scheme:` where a URL starts: a Markdown link/image destination, a
// reference definition, an attribute value, or an autolink. Whitespace and
// control characters inside the scheme are tolerated the way browsers
// tolerate them.
const UNSAFE_SCHEME = '(?:j\\s*a\\s*v\\s*a\\s*s\\s*c\\s*r\\s*i\\s*p\\s*t|v\\s*b\\s*s\\s*c\\s*r\\s*i\\s*p\\s*t|d\\s*a\\s*t\\s*a|f\\s*i\\s*l\\s*e)\\s*:';
const UNSAFE_URL = new RegExp(`(?:\\]\\(\\s*<?|\\]:\\s*<?|=\\s*["']?\\s*|<)\\s*${UNSAFE_SCHEME}`, 'gi');
const OBFUSCATED_DESTINATION = /\]\(\s*<?[^)\s]*&(?:#\d+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);/g;

function positionOf(text: string, index: number): { readonly line: number; readonly column: number } {
  let line = 1;
  let lineStart = 0;
  for (let i = 0; i < index; i += 1) {
    if (text.charCodeAt(i) === 10) {
      line += 1;
      lineStart = i + 1;
    }
  }
  return { line, column: index - lineStart + 1 };
}

export function scanActiveContent(text: string): readonly ActiveContentFinding[] {
  const findings: ActiveContentFinding[] = [];
  const found = new Set<string>();
  const add = (form: ActiveContentForm, index: number): void => {
    const key = `${form}@${index}`;
    if (found.has(key)) return;
    found.add(key);
    findings.push({ form, ...positionOf(text, index) });
  };
  for (const match of text.matchAll(HTML_TAG)) {
    const name = (match[1] ?? '').toLowerCase();
    add(name === 'script' ? 'script-element' : name === 'svg' ? 'svg-element' : 'html-tag', match.index);
  }
  for (const match of text.matchAll(HTML_DECLARATION)) add('html-comment-or-declaration', match.index);
  for (const match of text.matchAll(EVENT_HANDLER)) add('event-handler-attribute', match.index);
  for (const match of text.matchAll(UNSAFE_URL)) add('unsafe-url-scheme', match.index);
  for (const match of text.matchAll(OBFUSCATED_DESTINATION)) add('obfuscated-link-destination', match.index);
  return findings.sort((a, b) => a.line - b.line || a.column - b.column || a.form.localeCompare(b.form));
}

// ---------------------------------------------------------------------
// Reader.

export const OBJECT_READ_OUTCOMES = [
  'read',
  'refused',
  'over-limit',
  'git-read-failed',
  'object-id-mismatch',
  'contains-nul',
  'not-utf-8',
  'active-content',
] as const;
export type ObjectReadOutcome = (typeof OBJECT_READ_OUTCOMES)[number];

// Body-free. `detail` is always a closed reason or limit name, never bytes
// of the source.
export interface ObjectReadRecord {
  readonly path: string;
  readonly objectId?: string;
  readonly outcome: ObjectReadOutcome;
  readonly bytes: number;
  // `sha256:<hex>` of the exact bytes Git returned (hash-not-body).
  readonly contentDigest?: string;
  readonly detail?: string;
  readonly activeContent?: readonly ActiveContentFinding[];
}

export type ExactObjectRead =
  | { readonly kind: 'text'; readonly text: string; readonly record: ObjectReadRecord }
  | { readonly kind: 'unavailable'; readonly record: ObjectReadRecord };

export interface ExactObjectReader {
  readonly read: (path: string, expectedObjectId?: string) => ExactObjectRead;
  // Every attempt, in order, body-free.
  readonly records: readonly ObjectReadRecord[];
  readonly breaches: readonly ResourceLimitBreach[];
  readonly limits: PwbResourceLimits;
  readonly attempted: () => number;
  readonly totalBytes: () => number;
}

export interface ExactObjectReaderInput {
  readonly runGit: GitRunner;
  readonly tree: GitTreeIndex;
  readonly resourceLimits?: PwbResourceLimits;
  readonly deniedPathRules?: DeniedPathRules;
}

const STRICT_UTF8 = new TextDecoder('utf-8', { fatal: true });

function decodeUtf8(bytes: Uint8Array): string | undefined {
  try {
    return STRICT_UTF8.decode(bytes);
  } catch {
    return undefined;
  }
}

export function contentDigestOf(bytes: Uint8Array): string {
  return `sha256:${createHash('sha256').update(bytes).digest('hex')}`;
}

export function createExactObjectReader(input: ExactObjectReaderInput): ExactObjectReader {
  const limits = input.resourceLimits ?? PWB_RESOURCE_LIMITS;
  const rules = input.deniedPathRules ?? PWB_DENIED_PATH_RULES;
  const records: ObjectReadRecord[] = [];
  const breaches: ResourceLimitBreach[] = [];
  let attempted = 0;
  let totalBytes = 0;

  const unavailable = (record: ObjectReadRecord): ExactObjectRead => {
    records.push(record);
    return { kind: 'unavailable', record };
  };

  const read = (path: string, expectedObjectId?: string): ExactObjectRead => {
    attempted += 1;
    const countBreach = evaluateLimit(limits, 'maxSources', attempted, path);
    if (countBreach !== undefined) {
      breaches.push(countBreach);
      return unavailable({ path, outcome: 'over-limit', bytes: 0, detail: 'maxSources' });
    }
    const admission = admitExactObjectRead(input.tree, path, expectedObjectId, rules);
    if (admission.kind === 'refused') return unavailable({ path, outcome: 'refused', bytes: 0, detail: admission.reason });
    const { objectId, sizeBytes } = admission.entry;
    const objectFormat = objectId.length === 64 ? 'sha256' : 'sha1';

    if (sizeBytes !== undefined) {
      const perSource = evaluateLimit(limits, 'maxBytesPerSource', sizeBytes, path);
      if (perSource !== undefined) {
        breaches.push(perSource);
        return unavailable({ path, objectId, outcome: 'over-limit', bytes: 0, detail: 'maxBytesPerSource' });
      }
      const total = evaluateLimit(limits, 'maxTotalBytes', totalBytes + sizeBytes, path);
      if (total !== undefined) {
        breaches.push(total);
        return unavailable({ path, objectId, outcome: 'over-limit', bytes: 0, detail: 'maxTotalBytes' });
      }
    }

    let bytes: Uint8Array;
    try {
      bytes = input.runGit(['cat-file', 'blob', objectId]);
    } catch (error) {
      const detail = error instanceof Error ? error.message : String(error);
      return unavailable({ path, objectId, outcome: 'git-read-failed', bytes: 0, detail });
    }
    const contentDigest = contentDigestOf(bytes);
    const taken = { path, objectId, bytes: bytes.byteLength, contentDigest };

    // Sizes the listing did not declare are bounded after the read; the
    // bytes are dropped without being decoded.
    if (sizeBytes === undefined) {
      const perSource = evaluateLimit(limits, 'maxBytesPerSource', bytes.byteLength, path);
      if (perSource !== undefined) {
        breaches.push(perSource);
        return unavailable({ ...taken, outcome: 'over-limit', detail: 'maxBytesPerSource' });
      }
      const total = evaluateLimit(limits, 'maxTotalBytes', totalBytes + bytes.byteLength, path);
      if (total !== undefined) {
        breaches.push(total);
        return unavailable({ ...taken, outcome: 'over-limit', detail: 'maxTotalBytes' });
      }
    }
    totalBytes += bytes.byteLength;

    if (gitBlobObjectId(bytes, objectFormat) !== objectId) return unavailable({ ...taken, outcome: 'object-id-mismatch' });
    if (bytes.includes(0)) return unavailable({ ...taken, outcome: 'contains-nul' });
    const text = decodeUtf8(bytes);
    if (text === undefined) return unavailable({ ...taken, outcome: 'not-utf-8' });
    const activeContent = scanActiveContent(text);
    if (activeContent.length > 0) return unavailable({ ...taken, outcome: 'active-content', activeContent });
    const record: ObjectReadRecord = { ...taken, outcome: 'read' };
    records.push(record);
    return { kind: 'text', text, record };
  };

  return {
    read,
    records,
    breaches,
    limits,
    attempted: () => attempted,
    totalBytes: () => totalBytes,
  };
}

// ---------------------------------------------------------------------
// Phase B population read — one result per manifest source, in manifest
// order; the body reaches only `consume` and is not retained here.

export interface SourceReadResult<T> {
  readonly source: ManifestSource;
  readonly record: ObjectReadRecord;
  readonly value?: T;
}

export function readManifestSources<T>(
  manifest: Pick<ProjectShapeSourceManifest, 'sources'>,
  reader: ExactObjectReader,
  consume: (source: ManifestSource, text: string) => T,
): readonly SourceReadResult<T>[] {
  return manifest.sources.map((source) => {
    if (source.anchor.kind !== 'blob') {
      const record: ObjectReadRecord = {
        path: source.path,
        outcome: 'refused',
        bytes: 0,
        detail: source.anchor.kind === 'missing-at-revision' ? 'missing-at-revision' : 'not-a-regular-blob',
      };
      return { source, record };
    }
    const read = reader.read(source.path, source.anchor.objectId);
    if (read.kind === 'unavailable') return { source, record: read.record };
    return { source, record: read.record, value: consume(source, read.text) };
  });
}
