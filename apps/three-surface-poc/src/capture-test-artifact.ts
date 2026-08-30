import { buildTestArtifactRecordFromJUnit, type TestArtifactRecord } from '@syzygy/three-surface-poc-core';

// This module never runs the observed Butlers test suite itself — it only
// orchestrates a command an external operator supplies (SEC-3: Syzygy's own
// daemon runtime never executes observed code). `main.ts` — the running
// POC server — never imports this file; it is a separate, manually
// invoked capture step (see `capture-test-artifact-main.ts`).

export interface CaptureTestArtifactInput {
  readonly repoRoot: string;
  readonly scope: string;
  readonly command: readonly string[];
  readonly junitPath: string;
  readonly runCommand: (command: readonly string[], junitPath: string) => number;
  readonly readFile: (path: string) => string;
  readonly resolveCommit: (repoRoot: string) => string;
  readonly now: () => string;
}

export type CaptureTestArtifactResult =
  | { readonly kind: 'captured'; readonly record: TestArtifactRecord }
  | { readonly kind: 'failed'; readonly reason: string };

function describeFailure(cause: unknown, activity: string): string {
  return `${activity}: ${cause instanceof Error ? cause.message : String(cause)}`;
}

/** Runs the configured focused command, reads back the raw JUnit artifact
 * it produced, and builds the safe {@link TestArtifactRecord} from it.
 * A non-zero exit status is captured faithfully, never swallowed — the
 * resulting record still gets ingested so a genuine failure is visible
 * as "captured but failing", never silently dropped. */
export function captureTestArtifact(input: CaptureTestArtifactInput): CaptureTestArtifactResult {
  let exitCode: number;
  try {
    exitCode = input.runCommand(input.command, input.junitPath);
  } catch (cause) {
    return { kind: 'failed', reason: describeFailure(cause, 'the focused test command could not be run') };
  }

  let rawJUnitXml: string;
  try {
    rawJUnitXml = input.readFile(input.junitPath);
  } catch (cause) {
    return {
      kind: 'failed',
      reason: describeFailure(cause, `the JUnit artifact at ${input.junitPath} could not be read`),
    };
  }

  let repositoryCommit: string;
  try {
    repositoryCommit = input.resolveCommit(input.repoRoot);
  } catch (cause) {
    return { kind: 'failed', reason: describeFailure(cause, 'the repository commit could not be resolved') };
  }

  const built = buildTestArtifactRecordFromJUnit({
    rawJUnitXml,
    command: input.command,
    exitCode,
    capturedAt: input.now(),
    repositoryCommit,
    scope: input.scope,
  });
  if (built.kind === 'unparseable') {
    return { kind: 'failed', reason: built.reason };
  }
  return { kind: 'captured', record: built.record };
}
