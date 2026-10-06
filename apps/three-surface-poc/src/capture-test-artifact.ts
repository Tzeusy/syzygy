import {
  buildTestArtifactRecordFromJUnit,
  parseJUnitRootTotals,
  type TestArtifactRecord,
} from '@syzygy/three-surface-poc-core';

// Syzygy never runs the observed Butlers test suite (SEC-3, RFC5-18; owner
// direction REDIS-LOCAL-AGENT-SITTING-2026-10-07 item 4, `syzygy-4mbu`).
// This module only composes the focused pytest command for the operator to
// run themselves, and ingests the result file the operator hands back. It
// has no way to start a process: nothing here is given a runner, and
// `capture-test-artifact-main.ts` binds `child_process` for `git rev-parse`
// alone. `main.ts`, the running POC server, never imports either file.

export interface FocusedTestCommandInput {
  readonly repoRoot: string;
  readonly scope: string;
  readonly python: string;
}

/** The command recorded with the artifact: the focused pytest run, without
 * the JUnit output flag, whose path is the operator's choice. */
export function focusedTestCommand(input: FocusedTestCommandInput): readonly string[] {
  return [input.python, '-m', 'pytest', input.scope, '-q'];
}

const SHELL_SAFE = /^[A-Za-z0-9_./:=@%+,-]+$/;

/** POSIX shell quoting, for display only: Syzygy never hands this to a shell. */
export function shellQuote(word: string): string {
  return SHELL_SAFE.test(word) ? word : `'${word.replaceAll("'", `'\\''`)}'`;
}

export interface OperatorInstructionsInput extends FocusedTestCommandInput {
  readonly junitPath: string;
  readonly stateDir: string;
}

/** What the operator runs, in their own shell, and the ingest step after it. */
export function operatorInstructions(input: OperatorInstructionsInput): string {
  const run = [...focusedTestCommand(input), `--junitxml=${input.junitPath}`].map(shellQuote).join(' ');
  const ingest = [
    'npm', 'run', 'poc:capture-test-artifact', '--', 'ingest',
    '--repo', input.repoRoot, '--scope', input.scope, '--python', input.python,
    '--junit', input.junitPath, '--state-dir', input.stateDir,
    '--commit', '<the commit printed by step 1>', '--exit-code', '<the exit status printed by step 2>',
  ].map(shellQuote).join(' ');
  return [
    'Syzygy does not run this test suite. Run these yourself, in your own shell:',
    '',
    `  1. git -C ${shellQuote(input.repoRoot)} rev-parse HEAD`,
    `  2. cd ${shellQuote(input.repoRoot)} && ${run}; echo "exit $?"`,
    '',
    'Then hand the result back:',
    '',
    `  3. ${ingest}`,
    '',
  ].join('\n');
}

export interface IngestTestArtifactInput extends FocusedTestCommandInput {
  readonly junitPath: string;
  readonly reportedCommit: string;
  readonly reportedExitCode: string;
  readonly readFile: (path: string) => string;
  readonly resolveCommit: (repoRoot: string) => string;
  readonly now: () => string;
}

export type IngestTestArtifactResult =
  | { readonly kind: 'captured'; readonly record: TestArtifactRecord }
  | { readonly kind: 'failed'; readonly reason: string };

const FULL_COMMIT = /^[0-9a-f]{40}$/;
const EXIT_STATUS = /^(?:0|[1-9][0-9]{0,2})$/;

function describeFailure(cause: unknown, activity: string): string {
  return `${activity}: ${cause instanceof Error ? cause.message : String(cause)}`;
}

/** Ingests the JUnit file an operator produced by running
 * {@link operatorInstructions}. The operator reports the exit status and
 * the commit they ran at; the commit must still be the checkout's HEAD, so
 * a run at one commit is never recorded against another. A non-zero exit
 * status is recorded faithfully, never swallowed, so a genuine failure is
 * visible as "captured but failing". An exit status of 0 beside failing or
 * erroring tests is refused as an inconsistent report. */
export function ingestTestArtifact(input: IngestTestArtifactInput): IngestTestArtifactResult {
  if (!EXIT_STATUS.test(input.reportedExitCode) || Number(input.reportedExitCode) > 255) {
    return { kind: 'failed', reason: `the reported exit status ${JSON.stringify(input.reportedExitCode)} is not an integer from 0 to 255` };
  }
  const exitCode = Number(input.reportedExitCode);
  if (!FULL_COMMIT.test(input.reportedCommit)) {
    return { kind: 'failed', reason: `the reported commit ${JSON.stringify(input.reportedCommit)} is not a full 40-character commit id` };
  }

  let repositoryCommit: string;
  try {
    repositoryCommit = input.resolveCommit(input.repoRoot);
  } catch (cause) {
    return { kind: 'failed', reason: describeFailure(cause, 'the repository commit could not be resolved') };
  }
  if (repositoryCommit !== input.reportedCommit) {
    return {
      kind: 'failed',
      reason: `the checkout is at ${repositoryCommit}, not the reported ${input.reportedCommit}; run the tests again at the commit you ingest`,
    };
  }

  let rawJUnitXml: string;
  try {
    rawJUnitXml = input.readFile(input.junitPath);
  } catch (cause) {
    return { kind: 'failed', reason: describeFailure(cause, `the JUnit artifact at ${input.junitPath} could not be read`) };
  }

  const totals = parseJUnitRootTotals(rawJUnitXml);
  if (totals !== null && exitCode === 0 && totals.failures + totals.errors > 0) {
    return {
      kind: 'failed',
      reason: `the reported exit status is 0 but the artifact records ${totals.failures} failed and ${totals.errors} errored`,
    };
  }

  const built = buildTestArtifactRecordFromJUnit({
    rawJUnitXml,
    command: focusedTestCommand(input),
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
