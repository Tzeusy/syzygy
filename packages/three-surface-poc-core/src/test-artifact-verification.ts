import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

// A real, durable focused-pytest artifact, captured outside Syzygy by an
// external operator (POC-REQ / syzygy-0r9 AC1). Only safe, structured
// fields are ever ingested — never a test body, secret, or raw exception
// content (AC5). The raw JUnit artifact bytes are hashed for provenance;
// their content is never stored or re-derivable from this record.

export interface TestArtifactRecord {
  readonly command: readonly string[];
  readonly exitCode: number;
  readonly capturedAt: string;
  readonly repositoryCommit: string;
  readonly scope: string;
  readonly digest: string;
  readonly summary: string;
}

// --- File-backed record state --------------------------------------------
//
// Same posture as the materialization record: one JSON file under the
// daemon's own state directory (0700 dir, 0600 file). A corrupt or
// unreadable record is never treated as "no artifact ingested" — it
// throws, and callers must render that as a named Unknown rather than
// silently risking a false-negative that masks a tampered record.

export const TEST_ARTIFACT_RECORD_FILE_NAME = 'test-artifact-record.json' as const;
const TEST_ARTIFACT_STATE_DIR_MODE = 0o700;
const TEST_ARTIFACT_RECORD_FILE_MODE = 0o600;

export function testArtifactRecordPath(stateDir: string): string {
  return join(stateDir, TEST_ARTIFACT_RECORD_FILE_NAME);
}

function isStringArray(value: unknown): value is readonly string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === 'string');
}

function isTestArtifactRecord(value: unknown): value is TestArtifactRecord {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const record = value as Record<string, unknown>;
  return (
    isStringArray(record.command) &&
    typeof record.exitCode === 'number' &&
    typeof record.capturedAt === 'string' &&
    typeof record.repositoryCommit === 'string' &&
    typeof record.scope === 'string' &&
    typeof record.digest === 'string' &&
    typeof record.summary === 'string'
  );
}

/** Reads the record; returns `null` only when no file exists yet. Throws
 * on an unreadable or malformed file — never silently treats corruption
 * as "not yet ingested". */
export function readTestArtifactRecordFile(stateDir: string): TestArtifactRecord | null {
  const path = testArtifactRecordPath(stateDir);
  if (!existsSync(path)) {
    return null;
  }
  const raw = readFileSync(path, 'utf8');
  const parsed: unknown = JSON.parse(raw);
  if (!isTestArtifactRecord(parsed)) {
    throw new Error('test artifact record file is malformed');
  }
  return parsed;
}

export function writeTestArtifactRecordFile(stateDir: string, record: TestArtifactRecord): void {
  mkdirSync(stateDir, { recursive: true, mode: TEST_ARTIFACT_STATE_DIR_MODE });
  writeFileSync(testArtifactRecordPath(stateDir), JSON.stringify(record, null, 2), {
    encoding: 'utf8',
    mode: TEST_ARTIFACT_RECORD_FILE_MODE,
  });
}

export function clearTestArtifactRecordFile(stateDir: string): void {
  const path = testArtifactRecordPath(stateDir);
  if (existsSync(path)) {
    rmSync(path);
  }
}

// --- Building a safe record from a raw JUnit artifact ---------------------

export interface JUnitRootTotals {
  readonly tests: number;
  readonly failures: number;
  readonly errors: number;
  readonly skipped: number;
  readonly time: number | null;
}

// Matches only the exact `testsuite` tag (requiring whitespace right after
// the tag name) so it never matches the plural `testsuites` wrapper tag,
// which pytest emits with no totals of its own (`<testsuites name="pytest
// tests">`) around one or more real `<testsuite ...>` elements that do
// carry them.
const TESTSUITE_TAG_PATTERN = /<testsuite\s+([^>]*?)\/?>/i;
const TESTSUITES_TAG_PATTERN = /<testsuites\s+([^>]*?)\/?>/i;
const ATTR_PATTERN = /(\w+)="([^"]*)"/g;

function parseTagAttrs(tagBody: string): Map<string, string> {
  const attrs = new Map<string, string>();
  ATTR_PATTERN.lastIndex = 0;
  let attrMatch: RegExpExecArray | null;
  while ((attrMatch = ATTR_PATTERN.exec(tagBody)) !== null) {
    attrs.set(attrMatch[1] as string, attrMatch[2] as string);
  }
  return attrs;
}

function totalsFromAttrs(attrs: Map<string, string>): JUnitRootTotals | null {
  if (!attrs.has('tests')) {
    return null;
  }
  const tests = Number(attrs.get('tests'));
  if (!Number.isFinite(tests)) {
    return null;
  }
  const failures = Number(attrs.get('failures') ?? '0');
  const errors = Number(attrs.get('errors') ?? '0');
  const skipped = Number(attrs.get('skipped') ?? '0');
  const timeRaw = attrs.get('time');
  const time = timeRaw === undefined ? null : Number(timeRaw);
  return {
    tests,
    failures: Number.isFinite(failures) ? failures : 0,
    errors: Number.isFinite(errors) ? errors : 0,
    skipped: Number.isFinite(skipped) ? skipped : 0,
    time: time !== null && Number.isFinite(time) ? time : null,
  };
}

/**
 * Reads only the attributes on one opening tag of a raw JUnit artifact
 * (the first `<testsuite>`, falling back to `<testsuites>` when only the
 * wrapper carries totals) — it never scans past that one tag, so a
 * `<testcase>` name, a `<failure>`/`<error>` message, or any other
 * test-body content is never parsed out of the raw artifact (AC5).
 */
export function parseJUnitRootTotals(rawXml: string): JUnitRootTotals | null {
  const suiteMatch = TESTSUITE_TAG_PATTERN.exec(rawXml);
  if (suiteMatch !== null) {
    const totals = totalsFromAttrs(parseTagAttrs(suiteMatch[1] ?? ''));
    if (totals !== null) {
      return totals;
    }
  }
  const suitesMatch = TESTSUITES_TAG_PATTERN.exec(rawXml);
  if (suitesMatch !== null) {
    const totals = totalsFromAttrs(parseTagAttrs(suitesMatch[1] ?? ''));
    if (totals !== null) {
      return totals;
    }
  }
  return null;
}

export function summarizeJUnitTotals(totals: JUnitRootTotals): string {
  const passed = totals.tests - totals.failures - totals.errors - totals.skipped;
  const timeText = totals.time === null ? '' : ` in ${totals.time}s`;
  return `${passed} passed, ${totals.failures} failed, ${totals.errors} errored, ${totals.skipped} skipped${timeText}`;
}

export interface BuildTestArtifactRecordInput {
  readonly rawJUnitXml: string;
  readonly command: readonly string[];
  readonly exitCode: number;
  readonly capturedAt: string;
  readonly repositoryCommit: string;
  readonly scope: string;
}

export type BuildTestArtifactRecordResult =
  | { readonly kind: 'built'; readonly record: TestArtifactRecord }
  | { readonly kind: 'unparseable'; readonly reason: string };

/** The one seam that ever reads raw JUnit artifact bytes. Everything past
 * this function operates only on the resulting safe {@link TestArtifactRecord}. */
export function buildTestArtifactRecordFromJUnit(
  input: BuildTestArtifactRecordInput,
): BuildTestArtifactRecordResult {
  const totals = parseJUnitRootTotals(input.rawJUnitXml);
  if (totals === null) {
    return {
      kind: 'unparseable',
      reason: 'the artifact does not contain a recognizable JUnit <testsuite> root element',
    };
  }
  const digest = `sha256:${createHash('sha256').update(input.rawJUnitXml, 'utf8').digest('hex')}`;
  return {
    kind: 'built',
    record: {
      command: input.command,
      exitCode: input.exitCode,
      capturedAt: input.capturedAt,
      repositoryCommit: input.repositoryCommit,
      scope: input.scope,
      digest,
      summary: summarizeJUnitTotals(totals),
    },
  };
}

// --- Verification -----------------------------------------------------

export type TestArtifactVerificationResult =
  | { readonly kind: 'unknown'; readonly reason: string }
  | { readonly kind: 'verified'; readonly record: TestArtifactRecord };

export interface ResolveTestArtifactVerificationInput {
  readonly record: TestArtifactRecord | null;
  readonly expectedScope: string;
  readonly observedCommit: string | null;
  readonly commitAuthoredAt: string | null;
  readonly evaluationAsOf: string;
}

/**
 * Verified appears only when a captured artifact passes and binds to the
 * exact observed changed-or-merged commit (AC3). Missing, mismatched,
 * failed, future-dated, or unreadable evidence renders Unknown — it never
 * upgrades a git-observed change into satisfaction on its own (AC4).
 */
export function resolveTestArtifactVerification(
  input: ResolveTestArtifactVerificationInput,
): TestArtifactVerificationResult {
  if (input.observedCommit === null) {
    return {
      kind: 'unknown',
      reason: 'no observed changed-or-merged commit exists to bind test evidence against',
    };
  }
  if (input.record === null) {
    return { kind: 'unknown', reason: 'no test artifact has been ingested for this evaluation' };
  }
  if (input.record.scope !== input.expectedScope) {
    return {
      kind: 'unknown',
      reason: `test artifact scope (${input.record.scope}) does not match the configured seam (${input.expectedScope})`,
    };
  }
  if (input.record.repositoryCommit !== input.observedCommit) {
    return {
      kind: 'unknown',
      reason: `test artifact commit (${input.record.repositoryCommit}) does not match the observed change commit (${input.observedCommit})`,
    };
  }
  if (input.record.exitCode !== 0) {
    return {
      kind: 'unknown',
      reason: `test artifact reports a non-zero exit status (${input.record.exitCode})`,
    };
  }
  const capturedAtMs = Date.parse(input.record.capturedAt);
  if (Number.isNaN(capturedAtMs)) {
    return { kind: 'unknown', reason: 'test artifact capture time is not a valid instant' };
  }
  const evaluationAsOfMs = Date.parse(input.evaluationAsOf);
  if (!Number.isNaN(evaluationAsOfMs) && capturedAtMs > evaluationAsOfMs) {
    return {
      kind: 'unknown',
      reason: 'test artifact capture time is after this evaluation (future-dated evidence is treated as stale)',
    };
  }
  if (input.commitAuthoredAt !== null) {
    const commitAuthoredAtMs = Date.parse(input.commitAuthoredAt);
    if (!Number.isNaN(commitAuthoredAtMs) && capturedAtMs < commitAuthoredAtMs) {
      return {
        kind: 'unknown',
        reason: 'test artifact was captured before the commit it claims to verify existed',
      };
    }
  }
  return { kind: 'verified', record: input.record };
}
