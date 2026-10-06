import { execFileSync } from 'node:child_process';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import {
  readBoundedRegularFile,
  writeTestArtifactRecordFile,
  type TestArtifactRecord,
} from '@syzygy/three-surface-poc-core';

import { ingestTestArtifact, operatorInstructions } from './capture-test-artifact.js';

const USAGE = `syzygy POC — ingest one focused-pytest artifact the operator ran (operator tool, run manually)

Usage:
  npm run poc:capture-test-artifact -- print  --repo <butlers> --scope <test-path> --junit <path> --state-dir <path> [--python <bin>]
  npm run poc:capture-test-artifact -- ingest --repo <butlers> --scope <test-path> --junit <path> --state-dir <path> --commit <sha> --exit-code <n> [--python <bin>]

Syzygy never runs the observed project's tests (SEC-3, RFC5-18). "print"
prints the exact focused pytest command for you to run in your own shell,
and starts no process. "ingest" reads back only the JUnit file you hand it,
checks that the checkout is still at the commit you report, and stores safe,
structured metadata (command, reported exit status, ingest time, commit,
scope, digest) in the state directory, marked operator-reported. The JUnit
file must be a regular file of at most 4 MiB. No test body, secret, or raw
exception content is stored (AC5). The working tree is not checked for
uncommitted changes, and the run is never shown as Verified: an
operator-reported result caps at report-fact (RFC5-19).

"print" is for the owner or a human operator. An agent session must not run
the printed test command unless the owner has recorded a SEC-3 choice for
that run.
`;

export interface CaptureCliIo {
  readonly stdout: (text: string) => void;
  readonly stderr: (text: string) => void;
  readonly readFile: (path: string) => string;
  readonly resolveCommit: (repoRoot: string) => string;
  readonly writeRecord: (stateDir: string, record: TestArtifactRecord) => void;
  readonly now: () => string;
}

/** The only process this tool starts: `git rev-parse HEAD`, never the
 * observed project's code. */
function resolveCommitWithGit(repoRoot: string): string {
  return execFileSync('git', ['-C', repoRoot, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
}

export const REAL_IO: CaptureCliIo = {
  stdout: (text) => process.stdout.write(text),
  stderr: (text) => process.stderr.write(text),
  readFile: (path) => readBoundedRegularFile(path),
  resolveCommit: resolveCommitWithGit,
  writeRecord: writeTestArtifactRecordFile,
  now: () => new Date().toISOString(),
};

function parseFlags(argv: readonly string[]): Map<string, string> {
  const values = new Map<string, string>();
  for (let index = 0; index < argv.length; index++) {
    const flag = argv[index];
    if (flag === undefined || !flag.startsWith('--')) {
      throw new Error(`unexpected argument ${JSON.stringify(flag)}`);
    }
    const value = argv[index + 1];
    if (value === undefined || value.startsWith('--')) {
      throw new Error(`${flag} requires a value`);
    }
    values.set(flag, value);
    index++;
  }
  return values;
}

const COMMON = ['--repo', '--scope', '--junit', '--state-dir'] as const;
const REQUIRED: Readonly<Record<string, readonly string[]>> = {
  print: COMMON,
  ingest: [...COMMON, '--commit', '--exit-code'],
};

/** Returns the process exit code. */
export function runCaptureTestArtifactCli(argv: readonly string[], io: CaptureCliIo): number {
  if (argv.includes('--help') || argv.includes('-h')) {
    io.stdout(USAGE);
    return 0;
  }
  const [mode, ...rest] = argv;
  const required = mode === undefined ? undefined : REQUIRED[mode];
  if (required === undefined) {
    io.stderr(`capture-test-artifact: the first argument must be "print" or "ingest"\n\n${USAGE}`);
    return 1;
  }

  let values: Map<string, string>;
  try {
    values = parseFlags(rest);
  } catch (cause) {
    io.stderr(`capture-test-artifact: ${cause instanceof Error ? cause.message : String(cause)}\n\n${USAGE}`);
    return 1;
  }
  const missing = required.filter((flag) => !values.has(flag));
  if (missing.length > 0) {
    io.stderr(`capture-test-artifact: ${mode} needs ${missing.join(', ')}\n\n${USAGE}`);
    return 1;
  }

  const repoRoot = resolve(values.get('--repo') ?? '');
  const scope = values.get('--scope') ?? '';
  const junitPath = resolve(values.get('--junit') ?? '');
  const stateDir = resolve(values.get('--state-dir') ?? '');
  const python = values.get('--python') ?? 'python3';

  if (mode === 'print') {
    io.stdout(operatorInstructions({ repoRoot, scope, python, junitPath, stateDir }));
    return 0;
  }

  const result = ingestTestArtifact({
    repoRoot,
    scope,
    python,
    junitPath,
    reportedCommit: values.get('--commit') ?? '',
    reportedExitCode: values.get('--exit-code') ?? '',
    readFile: io.readFile,
    resolveCommit: io.resolveCommit,
    now: io.now,
  });
  if (result.kind === 'failed') {
    io.stderr(`capture-test-artifact: ${result.reason}\n`);
    return 1;
  }
  io.writeRecord(stateDir, result.record);
  io.stdout(
    `capture-test-artifact: ingested "${result.record.summary}" at commit ${result.record.repositoryCommit} (operator-reported exit ${result.record.exitCode})\n`,
  );
  return 0;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  process.exitCode = runCaptureTestArtifactCli(process.argv.slice(2), REAL_IO);
}
