import { describe, expect, it } from 'vitest';

import { focusedTestCommand, ingestTestArtifact, operatorInstructions, shellQuote } from './capture-test-artifact.js';

const PASSING_JUNIT = `<?xml version="1.0"?>
<testsuites tests="2" failures="0" errors="0" skipped="0" time="0.1">
  <testsuite name="pytest" tests="2" failures="0" errors="0" skipped="0" time="0.1" />
</testsuites>`;

const FAILING_JUNIT = `<?xml version="1.0"?>
<testsuites tests="2" failures="1" errors="0" skipped="0" time="0.1">
  <testsuite name="pytest" tests="2" failures="1" errors="0" skipped="0" time="0.1" />
</testsuites>`;

const SCOPE = 'tests/connectors/test_whatsapp_user_client.py';
const COMMIT = 'c13894238989d3bebb24094730992970b31fe546';
const OTHER_COMMIT = 'd13894238989d3bebb24094730992970b31fe546';

const BASE = {
  repoRoot: '/butlers',
  scope: SCOPE,
  python: 'python3',
  junitPath: '/tmp/artifact.xml',
  reportedCommit: COMMIT,
  reportedExitCode: '0',
  readFile: () => Buffer.from(PASSING_JUNIT),
  resolveCommit: () => COMMIT,
  now: () => '2026-08-30T08:00:00Z',
};

describe('focusedTestCommand and operatorInstructions', () => {
  it('records the focused pytest command without the operator-chosen output flag', () => {
    expect(focusedTestCommand({ repoRoot: '/butlers', scope: SCOPE, python: '.venv/bin/python' })).toEqual([
      '.venv/bin/python', '-m', 'pytest', SCOPE, '-q',
    ]);
  });

  it('prints the exact command, the commit step and the ingest step, and says Syzygy does not run it', () => {
    const text = operatorInstructions({
      repoRoot: '/home/op/butlers', scope: SCOPE, python: '.venv/bin/python', junitPath: '/tmp/out dir/a.xml', stateDir: '/tmp/state',
    });
    expect(text).toContain('Syzygy does not run this test suite.');
    expect(text).toContain('1. git -C /home/op/butlers rev-parse HEAD');
    expect(text).toContain(
      `2. cd /home/op/butlers && .venv/bin/python -m pytest ${SCOPE} -q '--junitxml=/tmp/out dir/a.xml'; echo "exit $?"`,
    );
    expect(text).toContain(
      "3. npm run poc:capture-test-artifact -- ingest --repo /home/op/butlers --scope " +
        `${SCOPE} --python .venv/bin/python --junit '/tmp/out dir/a.xml' --state-dir /tmp/state`,
    );
  });

  it('quotes a word carrying shell syntax so the printed line cannot run anything else', () => {
    expect(shellQuote("x'; rm -rf ~; echo '")).toBe(`'x'\\''; rm -rf ~; echo '\\'''`);
    expect(shellQuote('$(id)')).toBe(`'$(id)'`);
    expect(shellQuote('tests/a.py')).toBe('tests/a.py');
  });
});

describe('ingestTestArtifact', () => {
  it('builds a safe record from the operator-run artifact at the reported, current commit', () => {
    const result = ingestTestArtifact(BASE);
    expect(result.kind).toBe('captured');
    if (result.kind !== 'captured') throw new Error('unreachable');
    expect(result.record).toEqual({
      provenance: 'operator-reported',
      command: ['python3', '-m', 'pytest', SCOPE, '-q'],
      exitCode: 0,
      ingestedAt: '2026-08-30T08:00:00Z',
      repositoryCommit: COMMIT,
      scope: SCOPE,
      digest: expect.stringMatching(/^sha256:[0-9a-f]{64}$/) as unknown as string,
      summary: '2 passed, 0 failed, 0 errored, 0 skipped in 0.1s',
    });
  });

  it('records a non-zero exit status faithfully rather than swallowing it', () => {
    const result = ingestTestArtifact({ ...BASE, reportedExitCode: '1', readFile: () => Buffer.from(FAILING_JUNIT) });
    expect(result.kind).toBe('captured');
    if (result.kind !== 'captured') throw new Error('unreachable');
    expect(result.record.exitCode).toBe(1);
  });

  it('refuses when the checkout is no longer at the reported commit', () => {
    const result = ingestTestArtifact({ ...BASE, resolveCommit: () => OTHER_COMMIT });
    expect(result).toEqual({
      kind: 'failed',
      reason: `the checkout is at ${OTHER_COMMIT}, not the reported ${COMMIT}; run the tests again at the commit you ingest`,
    });
  });

  it('refuses a reported exit status of 0 beside failing tests', () => {
    const result = ingestTestArtifact({ ...BASE, readFile: () => Buffer.from(FAILING_JUNIT) });
    expect(result).toEqual({
      kind: 'failed',
      reason: 'exit status 0 was reported, but the result file records 1 failed and 0 errored',
    });
  });

  it('refuses a reported exit status of 0 beside a run that collected no tests', () => {
    const empty = '<testsuites><testsuite name="pytest" tests="0" failures="0" errors="0" skipped="0" /></testsuites>';
    const result = ingestTestArtifact({ ...BASE, readFile: () => Buffer.from(empty) });
    expect(result).toEqual({
      kind: 'failed',
      reason: 'exit status 0 was reported, but the result file records zero tests; a run that collected nothing verifies nothing',
    });
  });

  // `failures="-1" errors="1"` summed to zero and slipped past the status-0
  // check; `failures="x"` read as zero (round-1 note 4).
  it.each([
    ['a negative count', 'tests="2" failures="-1" errors="1"'],
    ['a non-numeric count', 'tests="2" failures="x"'],
    ['a fractional count', 'tests="2" failures="0.5"'],
    ['counts above the total', 'tests="1" failures="1" errors="1"'],
  ])('refuses %s as unreadable rather than reading it as zero', (_label, attrs) => {
    const result = ingestTestArtifact({ ...BASE, readFile: () => Buffer.from(`<testsuite name="pytest" ${attrs}>`) });
    expect(result.kind).toBe('failed');
    if (result.kind !== 'failed') throw new Error('unreachable');
    expect(result.reason).toContain('non-negative integer counts');
  });

  it('prints, for an agent session, that step 2 needs the owner\'s recorded SEC-3 choice, and that the tree is not checked', () => {
    const text = operatorInstructions({ repoRoot: '/r', scope: SCOPE, python: 'python3', junitPath: '/j.xml', stateDir: '/s' });
    expect(text).toContain('For the owner or a human operator. An agent session must not run step 2\nunless the owner has recorded a SEC-3 choice for that run.');
    expect(text).toContain('It does not check the working tree for uncommitted changes');
    expect(text).toContain('as operator-reported (report-fact), never as Verified.');
  });

  it.each(['', '-1', '256', '1.0', '01', 'zero'])('refuses the reported exit status %j', (code) => {
    const result = ingestTestArtifact({ ...BASE, reportedExitCode: code });
    expect(result.kind).toBe('failed');
    if (result.kind !== 'failed') throw new Error('unreachable');
    expect(result.reason).toContain('is not an integer from 0 to 255');
  });

  it.each(['c1389423', COMMIT.toUpperCase(), `${COMMIT}0`])('refuses the reported commit %j', (commit) => {
    const result = ingestTestArtifact({ ...BASE, reportedCommit: commit });
    expect(result.kind).toBe('failed');
    if (result.kind !== 'failed') throw new Error('unreachable');
    expect(result.reason).toContain('is not a full 40-character commit id');
  });

  it('fails when the commit cannot be resolved', () => {
    const result = ingestTestArtifact({ ...BASE, resolveCommit: () => { throw new Error('not a git repository'); } });
    expect(result).toEqual({ kind: 'failed', reason: 'the repository commit could not be resolved: not a git repository' });
  });

  it('fails when the handed-back artifact cannot be read', () => {
    const result = ingestTestArtifact({ ...BASE, readFile: () => { throw new Error('ENOENT'); } });
    expect(result).toEqual({ kind: 'failed', reason: 'the JUnit artifact at /tmp/artifact.xml could not be read: ENOENT' });
  });

  it('fails when the artifact has no recognizable JUnit root', () => {
    const result = ingestTestArtifact({ ...BASE, readFile: () => Buffer.from('not junit xml') });
    expect(result.kind).toBe('failed');
  });
});
