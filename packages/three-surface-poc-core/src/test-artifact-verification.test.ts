import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  buildTestArtifactRecordFromJUnit,
  clearTestArtifactRecordFile,
  parseJUnitRootTotals,
  readTestArtifactRecordFile,
  resolveTestArtifactVerification,
  writeTestArtifactRecordFile,
  type TestArtifactRecord,
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

function passingRecord(overrides: Partial<TestArtifactRecord> = {}): TestArtifactRecord {
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
});
