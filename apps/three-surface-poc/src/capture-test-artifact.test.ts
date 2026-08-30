import { describe, expect, it } from 'vitest';

import { captureTestArtifact } from './capture-test-artifact.js';

const PASSING_JUNIT = `<?xml version="1.0"?>
<testsuites tests="2" failures="0" errors="0" skipped="0" time="0.1">
  <testsuite name="pytest" tests="2" failures="0" errors="0" skipped="0" time="0.1" />
</testsuites>`;

const SCOPE = 'tests/connectors/test_whatsapp_user_client.py';
const COMMAND = ['python3', '-m', 'pytest', SCOPE, '-q'] as const;

describe('captureTestArtifact', () => {
  it('builds a safe record from a real command run, capture, and commit resolution', () => {
    const result = captureTestArtifact({
      repoRoot: '/butlers',
      scope: SCOPE,
      command: COMMAND,
      junitPath: '/tmp/artifact.xml',
      runCommand: () => 0,
      readFile: () => PASSING_JUNIT,
      resolveCommit: () => 'c13894238989d3bebb24094730992970b31fe546',
      now: () => '2026-08-30T08:00:00Z',
    });
    expect(result.kind).toBe('captured');
    if (result.kind !== 'captured') throw new Error('unreachable');
    expect(result.record).toEqual({
      command: COMMAND,
      exitCode: 0,
      capturedAt: '2026-08-30T08:00:00Z',
      repositoryCommit: 'c13894238989d3bebb24094730992970b31fe546',
      scope: SCOPE,
      digest: expect.stringMatching(/^sha256:[0-9a-f]{64}$/) as unknown as string,
      summary: '2 passed, 0 failed, 0 errored, 0 skipped in 0.1s',
    });
  });

  it('captures a non-zero exit status faithfully rather than swallowing it', () => {
    const result = captureTestArtifact({
      repoRoot: '/butlers',
      scope: SCOPE,
      command: COMMAND,
      junitPath: '/tmp/artifact.xml',
      runCommand: () => 1,
      readFile: () => PASSING_JUNIT,
      resolveCommit: () => 'c1389423',
      now: () => '2026-08-30T08:00:00Z',
    });
    expect(result.kind).toBe('captured');
    if (result.kind !== 'captured') throw new Error('unreachable');
    expect(result.record.exitCode).toBe(1);
  });

  it('fails when the command cannot be run', () => {
    const result = captureTestArtifact({
      repoRoot: '/butlers',
      scope: SCOPE,
      command: COMMAND,
      junitPath: '/tmp/artifact.xml',
      runCommand: () => {
        throw new Error('spawn ENOENT');
      },
      readFile: () => PASSING_JUNIT,
      resolveCommit: () => 'c1389423',
      now: () => '2026-08-30T08:00:00Z',
    });
    expect(result.kind).toBe('failed');
  });

  it('fails when the produced artifact cannot be read', () => {
    const result = captureTestArtifact({
      repoRoot: '/butlers',
      scope: SCOPE,
      command: COMMAND,
      junitPath: '/tmp/artifact.xml',
      runCommand: () => 0,
      readFile: () => {
        throw new Error('ENOENT');
      },
      resolveCommit: () => 'c1389423',
      now: () => '2026-08-30T08:00:00Z',
    });
    expect(result.kind).toBe('failed');
  });

  it('fails when the artifact has no recognizable JUnit root', () => {
    const result = captureTestArtifact({
      repoRoot: '/butlers',
      scope: SCOPE,
      command: COMMAND,
      junitPath: '/tmp/artifact.xml',
      runCommand: () => 0,
      readFile: () => 'not junit xml',
      resolveCommit: () => 'c1389423',
      now: () => '2026-08-30T08:00:00Z',
    });
    expect(result.kind).toBe('failed');
  });
});
