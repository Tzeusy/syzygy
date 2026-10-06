import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  buildOperatorReportedTestArtifactRecord,
  buildTestArtifactRecordFromJUnit,
  clearTestArtifactRecordFile,
  MAX_JUNIT_ARTIFACT_BYTES,
  parseJUnitRootTotals,
  readTestArtifactRecordFile,
  resolveTestArtifactVerification,
  writeTestArtifactRecordFile,
  type ObservedRunTestArtifactRecord,
  type OperatorReportedTestArtifactRecord,
} from './test-artifact-verification.js';

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function stateDir(): string {
  const dir = mkdtempSync(join(tmpdir(), 'syzygy-poc-test-artifact-'));
  cleanups.push(dir);
  return dir;
}

const PASSING_JUNIT = `<?xml version="1.0" encoding="utf-8"?>
<testsuites tests="3" failures="0" errors="0" skipped="0" time="0.421">
  <testsuite name="pytest" tests="3" failures="0" errors="0" skipped="0" time="0.421">
    <testcase classname="tests.connectors.test_whatsapp_user_client" name="test_mapped_lid" time="0.1">
      <system-out>this body content must never be indexed: SECRET-abc123</system-out>
    </testcase>
  </testsuite>
</testsuites>`;

const FAILING_JUNIT = `<?xml version="1.0" encoding="utf-8"?>
<testsuites tests="3" failures="1" errors="0" skipped="0" time="0.5">
  <testsuite name="pytest" tests="3" failures="1" errors="0" skipped="0" time="0.5">
    <testcase classname="tests.connectors.test_whatsapp_user_client" name="test_mapped_lid" time="0.1">
      <failure message="raw exception content that must never be indexed">Traceback...</failure>
    </testcase>
  </testsuite>
</testsuites>`;

// The real shape pytest 9.0.2 emits: the outer `<testsuites>` wrapper
// carries only `name`, never totals — all real numbers live on the
// nested `<testsuite>` tag. Captured against a real Butlers focused run
// (tests/connectors/test_whatsapp_user_client.py at commit c13894238)
// during this bead's manual end-to-end verification.
const REAL_PYTEST_JUNIT_SHAPE = `<?xml version="1.0" encoding="utf-8"?><testsuites name="pytest tests"><testsuite name="pytest" errors="0" failures="0" skipped="0" tests="83" time="14.727" timestamp="2026-08-30T15:40:16.644522+08:00" hostname="Tzeusy"><testcase classname="tests.connectors.test_whatsapp_user_client" name="test_single_event_envelope_contract" time="0.003" /></testsuite></testsuites>`;

describe('parseJUnitRootTotals', () => {
  it('reads only the outermost root-tag attributes', () => {
    const totals = parseJUnitRootTotals(PASSING_JUNIT);
    expect(totals).toEqual({ tests: 3, failures: 0, errors: 0, skipped: 0, time: 0.421 });
  });

  it('returns null for content with no testsuite root', () => {
    expect(parseJUnitRootTotals('<not-junit/>')).toBeNull();
  });

  it('falls back to the nested <testsuite> totals when the <testsuites> wrapper carries none (real pytest shape)', () => {
    const totals = parseJUnitRootTotals(REAL_PYTEST_JUNIT_SHAPE);
    expect(totals).toEqual({ tests: 83, failures: 0, errors: 0, skipped: 0, time: 14.727 });
  });

  it('matches the tag name in any ASCII case and keeps indices aligned past a non-ASCII character', () => {
    expect(parseJUnitRootTotals('İİ<TestSuite tests="2" failures="1">')).toEqual({ tests: 2, failures: 1, errors: 0, skipped: 0, time: null });
  });

  it('refuses input over the ceiling without scanning it', () => {
    const oversized = '<testsuite tests="1">'.padEnd(MAX_JUNIT_ARTIFACT_BYTES + 1, ' ');
    expect(parseJUnitRootTotals(oversized)).toBeNull();
  });

  // Round-1 finding 2: the old `/<testsuite\s+([^>]*?)\/?>/i` took 30.7 s
  // on 960 KB of unterminated tags, and `(\w+)="…"` is quadratic over a
  // long word run. Each crafted input below sits just under the ceiling.
  it.each([
    ['unterminated opening tags', '<testsuite a'],
    ['unterminated plural tags', '<testsuites a'],
    ['near-miss tag names', '<testsuitex '],
  ])('scans %s at the ceiling in linear time', (_label, unit) => {
    const crafted = unit.repeat(Math.floor(MAX_JUNIT_ARTIFACT_BYTES / unit.length));
    const started = performance.now();
    expect(parseJUnitRootTotals(crafted)).toBeNull();
    expect(performance.now() - started).toBeLessThan(2_000);
  });

  it('scans one tag body that is a single word run at the ceiling in linear time', () => {
    const crafted = `<testsuite ${'a'.repeat(MAX_JUNIT_ARTIFACT_BYTES - 32)} tests="1">`;
    const started = performance.now();
    expect(parseJUnitRootTotals(crafted)).toEqual({ tests: 1, failures: 0, errors: 0, skipped: 0, time: null });
    expect(performance.now() - started).toBeLessThan(2_000);
  });
});

describe('buildTestArtifactRecordFromJUnit', () => {
  it('produces a safe record that never contains the raw artifact body (AC5)', () => {
    const result = buildTestArtifactRecordFromJUnit({
      rawJUnitXml: PASSING_JUNIT,
      command: ['python3', '-m', 'pytest', 'tests/connectors/test_whatsapp_user_client.py', '-q'],
      exitCode: 0,
      capturedAt: '2026-08-30T08:00:00Z',
      repositoryCommit: 'c13894238989d3bebb24094730992970b31fe546',
      scope: 'tests/connectors/test_whatsapp_user_client.py',
    });
    expect(result.kind).toBe('built');
    if (result.kind !== 'built') throw new Error('unreachable');
    expect(result.record.summary).toBe('3 passed, 0 failed, 0 errored, 0 skipped in 0.421s');
    expect(result.record.digest).toMatch(/^sha256:[0-9a-f]{64}$/);

    const serialized = JSON.stringify(result.record);
    expect(serialized).not.toContain('SECRET-abc123');
    expect(serialized).not.toContain('system-out');
  });

  it('rejects an artifact with no recognizable JUnit root', () => {
    const result = buildTestArtifactRecordFromJUnit({
      rawJUnitXml: 'not xml at all',
      command: ['pytest'],
      exitCode: 0,
      capturedAt: '2026-08-30T08:00:00Z',
      repositoryCommit: 'abc',
      scope: 'tests/x.py',
    });
    expect(result.kind).toBe('unparseable');
  });
});

const OBSERVED_COMMIT = 'c13894238989d3bebb24094730992970b31fe546';
const SCOPE = 'tests/connectors/test_whatsapp_user_client.py';

function passingRecord(overrides: Partial<ObservedRunTestArtifactRecord> = {}): ObservedRunTestArtifactRecord {
  return {
    command: ['python3', '-m', 'pytest', SCOPE, '-q'],
    exitCode: 0,
    capturedAt: '2026-08-30T08:00:00Z',
    repositoryCommit: OBSERVED_COMMIT,
    scope: SCOPE,
    digest: 'sha256:' + '0'.repeat(64),
    summary: '3 passed, 0 failed, 0 errored, 0 skipped in 0.42s',
    ...overrides,
  };
}

function reportedRecord(overrides: Partial<OperatorReportedTestArtifactRecord> = {}): OperatorReportedTestArtifactRecord {
  return {
    provenance: 'operator-reported',
    command: ['python3', '-m', 'pytest', SCOPE, '-q'],
    exitCode: 0,
    ingestedAt: '2026-08-30T08:00:00Z',
    repositoryCommit: OBSERVED_COMMIT,
    scope: SCOPE,
    digest: 'sha256:' + '0'.repeat(64),
    summary: '3 passed, 0 failed, 0 errored, 0 skipped in 0.42s',
    ...overrides,
  };
}

describe('buildOperatorReportedTestArtifactRecord', () => {
  const input = {
    command: ['python3', '-m', 'pytest', SCOPE, '-q'],
    reportedExitCode: 0,
    ingestedAt: '2026-08-30T08:00:00Z',
    repositoryCommit: OBSERVED_COMMIT,
    scope: SCOPE,
  };

  it('marks the record operator-reported, with an ingest time and no capture time', () => {
    const result = buildOperatorReportedTestArtifactRecord({ ...input, rawJUnitXml: PASSING_JUNIT });
    expect(result.kind).toBe('built');
    if (result.kind !== 'built') throw new Error('unreachable');
    expect(result.record.provenance).toBe('operator-reported');
    expect(result.record.ingestedAt).toBe('2026-08-30T08:00:00Z');
    expect('capturedAt' in result.record).toBe(false);
    expect(JSON.stringify(result.record)).not.toContain('SECRET-abc123');
  });

  it('refuses status 0 beside a failure, and beside zero tests', () => {
    expect(buildOperatorReportedTestArtifactRecord({ ...input, rawJUnitXml: FAILING_JUNIT }).kind).toBe('inconsistent');
    expect(buildOperatorReportedTestArtifactRecord({ ...input, rawJUnitXml: '<testsuite tests="0">' }).kind).toBe('inconsistent');
    expect(buildOperatorReportedTestArtifactRecord({ ...input, reportedExitCode: 5, rawJUnitXml: '<testsuite tests="0">' }).kind).toBe('built');
  });
});

describe('resolveTestArtifactVerification', () => {
  it('renders Verified when the artifact passes and binds to the observed commit (AC3)', () => {
    const result = resolveTestArtifactVerification({
      record: passingRecord(),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: '2026-08-30T07:00:00Z',
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('verified');
  });

  it('renders Unknown when no artifact has been ingested (AC4)', () => {
    const result = resolveTestArtifactVerification({
      record: null,
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });

  it('renders Unknown when there is no observed commit to bind against', () => {
    const result = resolveTestArtifactVerification({
      record: passingRecord(),
      expectedScope: SCOPE,
      observedCommit: null,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });

  it('renders Unknown on a commit mismatch — a stale or wrong-change artifact (AC4)', () => {
    const result = resolveTestArtifactVerification({
      record: passingRecord({ repositoryCommit: 'deadbeef' }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
    if (result.kind !== 'unknown') throw new Error('unreachable');
    expect(result.reason).toContain('does not match the observed change commit');
  });

  it('renders Unknown on a scope mismatch', () => {
    const result = resolveTestArtifactVerification({
      record: passingRecord({ scope: 'tests/unrelated/test_x.py' }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });

  it('renders Unknown on a failing artifact — a fix must never be shown verified by a failing run (AC4)', () => {
    const failing = buildTestArtifactRecordFromJUnit({
      rawJUnitXml: FAILING_JUNIT,
      command: ['python3', '-m', 'pytest', SCOPE, '-q'],
      exitCode: 1,
      capturedAt: '2026-08-30T08:00:00Z',
      repositoryCommit: OBSERVED_COMMIT,
      scope: SCOPE,
    });
    if (failing.kind !== 'built') throw new Error('unreachable');
    const result = resolveTestArtifactVerification({
      record: failing.record,
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });

  it('renders Unknown on a future-dated capture (fail-closed staleness)', () => {
    const result = resolveTestArtifactVerification({
      record: passingRecord({ capturedAt: '2026-09-01T00:00:00Z' }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
    if (result.kind !== 'unknown') throw new Error('unreachable');
    expect(result.reason).toContain('future-dated');
  });

  it('renders Unknown when capture predates the commit it claims to verify', () => {
    const result = resolveTestArtifactVerification({
      record: passingRecord({ capturedAt: '2026-08-30T06:00:00Z' }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: '2026-08-30T07:00:00Z',
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
    if (result.kind !== 'unknown') throw new Error('unreachable');
    expect(result.reason).toContain('before the commit');
  });

  it('never renders an operator-reported run as Verified: it caps at report-fact with its disclosure (RFC5-19)', () => {
    const result = resolveTestArtifactVerification({
      record: reportedRecord(),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: '2026-08-30T07:00:00Z',
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('reported');
    if (result.kind !== 'reported') throw new Error('unreachable');
    expect(result.tier).toBe('report-fact');
    expect(result.disclosure).toContain('Reported by the operator, not verified by Syzygy.');
    expect(result.disclosure).toContain('the working tree\'s state is not checked');
    expect(result.disclosure).toContain('RFC5-19: "an artifact of unverifiable origin caps at report-fact however retained, well-formed, and revision-bound it is."');
  });

  it('checks an operator-reported record against its ingest time, and says so', () => {
    const before = resolveTestArtifactVerification({
      record: reportedRecord({ ingestedAt: '2026-08-30T06:00:00Z' }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: '2026-08-30T07:00:00Z',
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(before).toEqual({ kind: 'unknown', reason: 'test artifact was ingested before the commit it claims to verify existed' });
    const future = resolveTestArtifactVerification({
      record: reportedRecord({ ingestedAt: '2026-09-01T00:00:00Z' }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(future).toEqual({ kind: 'unknown', reason: 'test artifact ingest time is after this evaluation (future-dated evidence is treated as stale)' });
  });

  it('keeps an operator-reported non-zero exit status Unknown', () => {
    const result = resolveTestArtifactVerification({
      record: reportedRecord({ exitCode: 1 }),
      expectedScope: SCOPE,
      observedCommit: OBSERVED_COMMIT,
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });

  it('mutation check: a falsified verification would be caught', () => {
    // Prove the assertion is load-bearing (rule 6): a broken resolver that
    // always says "verified" would pass none of the negative cases above,
    // but this positive-path assertion alone must fail if verification is
    // computed against the wrong commit.
    const result = resolveTestArtifactVerification({
      record: passingRecord({ repositoryCommit: OBSERVED_COMMIT }),
      expectedScope: SCOPE,
      observedCommit: 'a-different-commit',
      commitAuthoredAt: null,
      evaluationAsOf: '2026-08-30T12:00:00Z',
    });
    expect(result.kind).not.toBe('verified');
  });
});

describe('test-artifact record file state', () => {
  it('round-trips a written record and treats absence as null, never as a false negative', () => {
    const dir = stateDir();
    expect(readTestArtifactRecordFile(dir)).toBeNull();
    const record = passingRecord();
    writeTestArtifactRecordFile(dir, record);
    expect(readTestArtifactRecordFile(dir)).toEqual(record);
    clearTestArtifactRecordFile(dir);
    expect(readTestArtifactRecordFile(dir)).toBeNull();
  });

  it('throws on a malformed record rather than silently treating it as uningested', () => {
    const dir = stateDir();
    writeTestArtifactRecordFile(dir, passingRecord());
    const path = join(dir, 'test-artifact-record.json');
    writeFileSync(path, '{"not":"a record"}', 'utf8');
    expect(() => readTestArtifactRecordFile(dir)).toThrow();
  });

  it('round-trips an operator-reported record and refuses one that mixes the two timings', () => {
    const dir = stateDir();
    writeTestArtifactRecordFile(dir, reportedRecord());
    expect(readTestArtifactRecordFile(dir)).toEqual(reportedRecord());
    const path = join(dir, 'test-artifact-record.json');
    // An operator-reported record carrying a capture time would let the
    // ingest instant pass for the run's; one without provenance but with an
    // ingest time would shed the mark.
    writeFileSync(path, JSON.stringify({ ...reportedRecord(), capturedAt: '2026-08-30T08:00:00Z' }), 'utf8');
    expect(() => readTestArtifactRecordFile(dir)).toThrow('malformed');
    const { provenance: _dropped, ...unmarked } = reportedRecord();
    writeFileSync(path, JSON.stringify(unmarked), 'utf8');
    expect(() => readTestArtifactRecordFile(dir)).toThrow('malformed');
  });
});
