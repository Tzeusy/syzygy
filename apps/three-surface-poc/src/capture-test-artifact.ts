import {
  buildOperatorReportedTestArtifactRecord,
  type OperatorReportedTestArtifactRecord,
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
    'For the owner or a human operator. An agent session must not run step 2',
    'unless the owner has recorded a SEC-3 choice for that run.',
    '',
    `  1. git -C ${shellQuote(input.repoRoot)} rev-parse HEAD`,
    `  2. cd ${shellQuote(input.repoRoot)} && ${run}; echo "exit $?"`,
    '',
    'Then hand the result back, at the same commit, without switching the',
    'checkout in between:',
    '',
    `  3. ${ingest}`,
    '',
    'Syzygy checks that HEAD is still the reported commit when it ingests the',
    'file. It does not check the working tree for uncommitted changes, and it',
    'records the exit status and the run as your report: the result is shown',
    'as operator-reported (report-fact), never as Verified.',
    '',
  ].join('\n');
}

export interface IngestTestArtifactInput extends FocusedTestCommandInput {
  readonly junitPath: string;
  readonly reportedCommit: string;
  readonly reportedExitCode: string;
  /** The file's bytes, undecoded: the record's digest is taken over them. */
  readonly readFile: (path: string) => Uint8Array;
  readonly resolveCommit: (repoRoot: string) => string;
  readonly now: () => string;
}

export type IngestTestArtifactResult =
  | { readonly kind: 'captured'; readonly record: OperatorReportedTestArtifactRecord }
  | { readonly kind: 'failed'; readonly reason: string };

const FULL_COMMIT = /^[0-9a-f]{40}$/;
const EXIT_STATUS = /^(?:0|[1-9][0-9]{0,2})$/;

function describeFailure(cause: unknown, activity: string): string {
  return `${activity}: ${cause instanceof Error ? cause.message : String(cause)}`;
}

/** Ingests the JUnit file an operator produced by running
 * {@link operatorInstructions}. The operator reports the exit status and
 * the commit they ran at; the commit must still be the checkout's HEAD when
 * the file is ingested, so a run reported at one commit is never recorded
 * against another. Neither a checkout switched away and back between the
 * run and the ingest nor a dirty working tree is detected: the record is
 * marked operator-reported and never renders as Verified (RFC5-19). A
 * non-zero exit status is recorded faithfully, never swallowed, so a genuine
 * failure is visible as "reported but failing". An exit status of 0 beside
 * failing or erroring tests, or beside zero tests, is refused as an
 * inconsistent report. `readFile` must refuse anything but a bounded
 * regular file (`readBoundedRegularFile` in the CLI). */
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

  let rawJUnit: Uint8Array;
  try {
    rawJUnit = input.readFile(input.junitPath);
  } catch (cause) {
    return { kind: 'failed', reason: describeFailure(cause, `the JUnit artifact at ${input.junitPath} could not be read`) };
  }

  const built = buildOperatorReportedTestArtifactRecord({
    rawJUnit,
    command: focusedTestCommand(input),
    reportedExitCode: exitCode,
    ingestedAt: input.now(),
    repositoryCommit,
    scope: input.scope,
  });
  if (built.kind !== 'built') {
    return { kind: 'failed', reason: built.reason };
  }
  return { kind: 'captured', record: built.record };
}
