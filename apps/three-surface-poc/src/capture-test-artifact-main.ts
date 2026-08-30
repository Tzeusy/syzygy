import { execFileSync, spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import { writeTestArtifactRecordFile } from '@syzygy/three-surface-poc-core';

import { captureTestArtifact } from './capture-test-artifact.js';

const USAGE = `syzygy POC — capture one real focused-pytest artifact (operator tool, run manually)

Usage: npm run poc:capture-test-artifact -- --repo <absolute-path-to-butlers> --scope <test-path> --state-dir <path> [--python <bin>]

This runs the focused pytest command directly against the given Butlers
checkout (never through the running POC daemon — see AGENTS.md "Syzygy
executing observed code") and ingests only safe, structured metadata
(command, exit status, capture time, commit, scope, digest) into the
configured state directory. No test body, secret, or raw exception
content is stored (AC5).
`;

function parseArgs(argv: readonly string[]): Map<string, string> {
  const values = new Map<string, string>();
  for (let index = 0; index < argv.length; index++) {
    const flag = argv[index];
    if (flag === undefined || !flag.startsWith('--')) {
      continue;
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

function main(): void {
  if (process.argv.includes('--help') || process.argv.includes('-h')) {
    process.stdout.write(USAGE);
    return;
  }

  let values: Map<string, string>;
  try {
    values = parseArgs(process.argv.slice(2));
  } catch (cause) {
    process.stderr.write(`capture-test-artifact: ${cause instanceof Error ? cause.message : String(cause)}\n\n${USAGE}`);
    process.exitCode = 1;
    return;
  }

  const repoArg = values.get('--repo');
  const scope = values.get('--scope');
  const stateDirArg = values.get('--state-dir');
  const python = values.get('--python') ?? 'python3';
  if (repoArg === undefined || scope === undefined || stateDirArg === undefined) {
    process.stderr.write(`capture-test-artifact: --repo, --scope, and --state-dir are all required\n\n${USAGE}`);
    process.exitCode = 1;
    return;
  }
  const repoRoot = resolve(repoArg);
  const stateDir = resolve(stateDirArg);

  const junitDir = mkdtempSync(join(tmpdir(), 'syzygy-poc-capture-'));
  const junitPath = join(junitDir, 'artifact.xml');
  const command = [python, '-m', 'pytest', scope, '-q'] as const;

  try {
    const result = captureTestArtifact({
      repoRoot,
      scope,
      command,
      junitPath,
      runCommand: (baseCommand, artifactPath) => {
        const [bin, ...rest] = baseCommand;
        if (bin === undefined) {
          throw new Error('empty command');
        }
        const proc = spawnSync(bin, [...rest, `--junitxml=${artifactPath}`], {
          cwd: repoRoot,
          encoding: 'utf8',
        });
        if (proc.error) {
          throw proc.error;
        }
        if (proc.status === null) {
          throw new Error(`the focused test command was terminated by signal ${proc.signal ?? 'unknown'}`);
        }
        return proc.status;
      },
      readFile: (path) => readFileSync(path, 'utf8'),
      resolveCommit: (root) => execFileSync('git', ['-C', root, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim(),
      now: () => new Date().toISOString(),
    });

    if (result.kind === 'failed') {
      process.stderr.write(`capture-test-artifact: ${result.reason}\n`);
      process.exitCode = 1;
      return;
    }

    writeTestArtifactRecordFile(stateDir, result.record);
    process.stdout.write(
      `capture-test-artifact: ingested "${result.record.summary}" at commit ${result.record.repositoryCommit} (exit ${result.record.exitCode})\n`,
    );
  } finally {
    rmSync(junitDir, { recursive: true, force: true });
  }
}

main();
