import { execFileSync } from 'node:child_process';
import { chmodSync, existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, beforeAll, describe, expect, it } from 'vitest';

import { readTestArtifactRecordFile } from '@syzygy/three-surface-poc-core';

import { REAL_IO, runCaptureTestArtifactCli, type CaptureCliIo } from './capture-test-artifact-main.js';

// syzygy-4mbu: the tool prints the focused pytest command and ingests the
// result; it never runs the observed project's code. Two independent
// checks hold that: a source check over both files, and a run of the real
// CLI whose "python" is a trap that leaves a file behind if anything runs it.

const SRC = fileURLToPath(new URL('.', import.meta.url));
const MAIN_SOURCE = 'capture-test-artifact-main.ts';
const MODULE_SOURCE = 'capture-test-artifact.ts';

const PASSING_JUNIT = '<testsuites tests="1" failures="0" errors="0" skipped="0" time="0.1"><testsuite tests="1" failures="0" errors="0" skipped="0" /></testsuites>';
const SCOPE = 'tests/test_a.py';

const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });

function scratch(): string {
  const dir = mkdtempSync(join(tmpdir(), 'syzygy-capture-cli-'));
  cleanups.push(dir);
  return dir;
}

interface Trap {
  readonly repo: string;
  readonly python: string;
  readonly sentinel: string;
  readonly commit: string;
}

/** A one-commit repository and an executable "python" that writes a
 * sentinel file when run. A repo-level hook would fire too if git ran one. */
function trap(): Trap {
  const root = scratch();
  const repo = join(root, 'repo');
  const sentinel = join(root, 'ran');
  const python = join(root, 'python');
  writeFileSync(python, `#!/bin/sh\necho "$@" > '${sentinel}'\n`);
  chmodSync(python, 0o755);
  execFileSync('git', ['init', '-q', repo]);
  writeFileSync(join(repo, 'a.txt'), 'a\n');
  execFileSync('git', ['-C', repo, 'add', 'a.txt']);
  execFileSync('git', ['-C', repo, '-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '-q', '-m', 'a']);
  const commit = execFileSync('git', ['-C', repo, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
  return { repo, python, sentinel, commit };
}

function captured(): { readonly io: CaptureCliIo; readonly out: string[]; readonly err: string[] } {
  const out: string[] = [];
  const err: string[] = [];
  return { io: { ...REAL_IO, stdout: (text) => { out.push(text); }, stderr: (text) => { err.push(text); } }, out, err };
}

describe('capture-test-artifact never starts the observed project (source check)', () => {
  let main = '';
  let module = '';
  beforeAll(() => {
    main = readFileSync(join(SRC, MAIN_SOURCE), 'utf8');
    module = readFileSync(join(SRC, MODULE_SOURCE), 'utf8');
  });

  // The one permitted binding, spelled in pieces so the suite's own
  // child-process guard does not read this file's patterns as calls.
  const RUN_GIT = ['execFile', 'Sync'].join('');
  const MODULE_LITERAL = /['"](?:node:)?child_process['"]/g;

  it('imports the process module only in the entry point, and only the git runner', () => {
    expect([...module.matchAll(MODULE_LITERAL)]).toHaveLength(0);
    expect([...main.matchAll(MODULE_LITERAL)]).toHaveLength(1);
    expect(main).toContain(`import { ${RUN_GIT} } from 'node:child_process';`);
  });

  it('names no other way to start a process', () => {
    const starters = new RegExp(String.raw`\b(?:spawn|spawnSync|execSync|exec|execFile|fork)\s*\(`);
    for (const source of [main, module]) {
      expect(source).not.toMatch(starters);
      expect(source).not.toMatch(/\bimport\s*\(/);
      expect(source).not.toMatch(/\brequire\s*\(/);
      expect(source).not.toMatch(/\bprocess\.binding\b|\bWorker\b|node:worker_threads|node:vm/);
    }
  });

  it('runs exactly one command, the literal git', () => {
    const calls = [...main.matchAll(new RegExp(String.raw`\b${RUN_GIT}\s*\(\s*([^,)]*)`, 'g'))].map((match) => match[1]?.trim());
    expect(calls).toEqual(["'git'"]);
  });
});

describe('capture-test-artifact never starts the observed project (run check)', () => {
  it('print writes the command for the operator and runs nothing', () => {
    const t = trap();
    const { io, out, err } = captured();
    const code = runCaptureTestArtifactCli(
      ['print', '--repo', t.repo, '--scope', SCOPE, '--junit', join(t.repo, '..', 'a.xml'), '--state-dir', join(t.repo, '..', 'state'), '--python', t.python],
      io,
    );
    expect({ code, err }).toEqual({ code: 0, err: [] });
    expect(out.join('')).toContain(`${t.python} -m pytest ${SCOPE} -q --junitxml=`);
    expect(existsSync(t.sentinel)).toBe(false);
  });

  it('ingest reads back the handed-in file, binds the current commit, and runs nothing', () => {
    const t = trap();
    const junit = join(t.repo, '..', 'a.xml');
    const state = join(t.repo, '..', 'state');
    writeFileSync(junit, PASSING_JUNIT);
    const { io, out, err } = captured();
    const code = runCaptureTestArtifactCli(
      ['ingest', '--repo', t.repo, '--scope', SCOPE, '--junit', junit, '--state-dir', state, '--python', t.python, '--commit', t.commit, '--exit-code', '0'],
      io,
    );
    expect({ code, err }).toEqual({ code: 0, err: [] });
    expect(out.join('')).toContain(`at commit ${t.commit} (exit 0)`);
    expect(readTestArtifactRecordFile(state)).toMatchObject({ repositoryCommit: t.commit, exitCode: 0, command: [t.python, '-m', 'pytest', SCOPE, '-q'] });
    expect(existsSync(t.sentinel)).toBe(false);
  });

  it('ingest refuses, writes nothing and runs nothing when the junit file was never produced', () => {
    const t = trap();
    const state = join(t.repo, '..', 'state');
    const { io, err } = captured();
    const code = runCaptureTestArtifactCli(
      ['ingest', '--repo', t.repo, '--scope', SCOPE, '--junit', join(t.repo, '..', 'missing.xml'), '--state-dir', state, '--python', t.python, '--commit', t.commit, '--exit-code', '0'],
      io,
    );
    expect(code).toBe(1);
    expect(err.join('')).toContain('could not be read');
    expect(readTestArtifactRecordFile(state)).toBeNull();
    expect(existsSync(t.sentinel)).toBe(false);
  });

  it.each([
    [['run', '--repo', '/r'], 'the first argument must be "print" or "ingest"'],
    [[], 'the first argument must be "print" or "ingest"'],
    [['ingest', '--repo', '/r', '--scope', 's', '--junit', '/j', '--state-dir', '/s'], 'ingest needs --commit, --exit-code'],
    [['print', '--repo', '/r', 'stray'], 'unexpected argument "stray"'],
  ])('refuses %j', (argv, message) => {
    const { io, err } = captured();
    expect(runCaptureTestArtifactCli(argv, io)).toBe(1);
    expect(err.join('')).toContain(message);
  });
});
