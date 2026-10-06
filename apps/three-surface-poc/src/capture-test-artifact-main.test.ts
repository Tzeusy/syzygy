import { execFileSync } from 'node:child_process';
import { chmodSync, existsSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { afterEach, beforeAll, describe, expect, it } from 'vitest';

import { MAX_JUNIT_ARTIFACT_BYTES, readTestArtifactRecordFile } from '@syzygy/three-surface-poc-core';

import { REAL_IO, readBoundedRegularFile, runCaptureTestArtifactCli, type CaptureCliIo } from './capture-test-artifact-main.js';

// syzygy-4mbu: the tool prints the focused pytest command and ingests the
// result; it never runs the observed project's code. Two independent
// checks hold that: a source check over both files and the core module they
// call, and a run of the real CLI whose "python" is a trap that leaves a
// file behind if anything runs it.

const SRC = fileURLToPath(new URL('.', import.meta.url));
const MAIN_SOURCE = 'capture-test-artifact-main.ts';
const MODULE_SOURCE = 'capture-test-artifact.ts';
const CORE_SOURCE = 'test-artifact-verification.ts';
const CORE_PATH = fileURLToPath(new URL('../../../packages/three-surface-poc-core/src/test-artifact-verification.ts', import.meta.url));

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

// The one permitted binding, spelled in pieces so the suite's own
// child-process guard does not read this file's patterns as calls.
const RUN_GIT = ['execFile', 'Sync'].join('');
const MODULE_LITERAL = /['"](?:node:)?child_process['"]/g;

/** Every module each checked file may import. Anything else — a worker,
 * `vm`, `module`, another core file — fails the check. */
const ALLOWED_IMPORTS: Readonly<Record<string, readonly string[]>> = {
  [MAIN_SOURCE]: [['node:child', 'process'].join('_'), 'node:fs', 'node:path', 'node:url', '@syzygy/three-surface-poc-core', './capture-test-artifact.js'],
  [MODULE_SOURCE]: ['@syzygy/three-surface-poc-core'],
  [CORE_SOURCE]: ['node:crypto', 'node:fs', 'node:path'],
};

/** The only members of `process` the tool may touch: writing its output,
 * reading its arguments and setting its exit code. */
const PROCESS_MEMBERS = new Set(['stdout', 'stderr', 'argv', 'exitCode']);

/** Identifiers that reach a process starter or arbitrary code indirectly:
 * the built-in module table, native addons, the old binding, the global
 * object, and evaluation of a string. */
const FORBIDDEN_IDENTIFIERS = new Set(['getBuiltinModule', 'dlopen', 'binding', 'globalThis', 'global', 'eval', 'Function', 'require', 'Worker', 'Reflect']);

/** Reasons the source cannot be trusted to start nothing, read off the
 * TypeScript syntax tree so a comment or a string never counts and a
 * bracket or alias does not slip past a word match. */
function sourceViolations(fileName: string, text: string): string[] {
  const violations: string[] = [];
  const file = ts.createSourceFile(fileName, text, ts.ScriptTarget.Latest, true);
  const allowed = ALLOWED_IMPORTS[fileName] ?? [];
  const visit = (node: ts.Node): void => {
    if (ts.isImportDeclaration(node) || ts.isExportDeclaration(node)) {
      const specifier = node.moduleSpecifier;
      if (specifier !== undefined && ts.isStringLiteral(specifier) && !allowed.includes(specifier.text)) {
        violations.push(`imports ${specifier.text}`);
      }
    }
    if (ts.isCallExpression(node) && node.expression.kind === ts.SyntaxKind.ImportKeyword) {
      violations.push('dynamic import()');
    }
    if (ts.isIdentifier(node)) {
      if (FORBIDDEN_IDENTIFIERS.has(node.text)) violations.push(`names ${node.text}`);
      if (node.text === 'process') {
        const parent = node.parent;
        const member = ts.isPropertyAccessExpression(parent) && parent.expression === node ? parent.name.text : null;
        if (member === null || !PROCESS_MEMBERS.has(member)) violations.push(`uses process other than process.{${[...PROCESS_MEMBERS].join(',')}}`);
      }
    }
    if (ts.isElementAccessExpression(node) && ts.isIdentifier(node.expression) && node.expression.text === 'process') {
      violations.push('bracket access on process');
    }
    ts.forEachChild(node, visit);
  };
  visit(file);
  return violations;
}

/** The named imports `fileText` takes from the core package. */
function coreImports(fileName: string, fileText: string): string[] {
  const file = ts.createSourceFile(fileName, fileText, ts.ScriptTarget.Latest, true);
  const names: string[] = [];
  for (const statement of file.statements) {
    if (!ts.isImportDeclaration(statement) || !ts.isStringLiteral(statement.moduleSpecifier)) continue;
    if (statement.moduleSpecifier.text !== '@syzygy/three-surface-poc-core') continue;
    const bindings = statement.importClause?.namedBindings;
    if (bindings !== undefined && ts.isNamedImports(bindings)) names.push(...bindings.elements.map((element) => element.name.text));
  }
  return names;
}

/** The names `fileText` exports from its own top-level declarations. */
function ownExports(fileName: string, fileText: string): Set<string> {
  const file = ts.createSourceFile(fileName, fileText, ts.ScriptTarget.Latest, true);
  const names = new Set<string>();
  for (const statement of file.statements) {
    const exported = ts.canHaveModifiers(statement) && (ts.getModifiers(statement) ?? []).some((modifier) => modifier.kind === ts.SyntaxKind.ExportKeyword);
    if (!exported) continue;
    if (ts.isVariableStatement(statement)) {
      for (const declaration of statement.declarationList.declarations) if (ts.isIdentifier(declaration.name)) names.add(declaration.name.text);
    } else if ((ts.isFunctionDeclaration(statement) || ts.isInterfaceDeclaration(statement) || ts.isTypeAliasDeclaration(statement)) && statement.name !== undefined) {
      names.add(statement.name.text);
    }
  }
  return names;
}

describe('capture-test-artifact never starts the observed project (source check)', () => {
  const sources = new Map<string, string>();
  beforeAll(() => {
    sources.set(MAIN_SOURCE, readFileSync(join(SRC, MAIN_SOURCE), 'utf8'));
    sources.set(MODULE_SOURCE, readFileSync(join(SRC, MODULE_SOURCE), 'utf8'));
    sources.set(CORE_SOURCE, readFileSync(CORE_PATH, 'utf8'));
  });
  const text = (name: string): string => sources.get(name) ?? '';

  it('imports the process module only in the entry point, and only the git runner', () => {
    expect([...text(MODULE_SOURCE).matchAll(MODULE_LITERAL)]).toHaveLength(0);
    expect([...text(CORE_SOURCE).matchAll(MODULE_LITERAL)]).toHaveLength(0);
    expect([...text(MAIN_SOURCE).matchAll(MODULE_LITERAL)]).toHaveLength(1);
    expect(text(MAIN_SOURCE)).toContain(`import { ${RUN_GIT} } from 'node:child_process';`);
  });

  it('names no other way to start a process, in the tool or the core module it calls', () => {
    const starters = new RegExp(String.raw`\b(?:spawn|spawnSync|execSync|exec|execFile|fork)\s*\(`);
    const indirect = /getBuiltinModule|\bdlopen\b|process\s*\[|globalThis|\beval\s*\(|\bFunction\s*\(|\bimport\s*\(|\brequire\s*\(|\bprocess\.binding\b|\bWorker\b|node:worker_threads|node:vm|node:module/;
    for (const name of [MAIN_SOURCE, MODULE_SOURCE, CORE_SOURCE]) {
      expect(text(name), name).not.toMatch(starters);
      expect(text(name), name).not.toMatch(indirect);
      expect(sourceViolations(name, text(name)), name).toEqual([]);
    }
  });

  // Round-1 finding 3: a getBuiltinModule spawn with no type annotation
  // passed every word check. Each of these must be caught by the tree check.
  it.each([
    ["(process as unknown as { getBuiltinModule(n: string): unknown }).getBuiltinModule('x');", 'names getBuiltinModule'],
    ["const p = process; p.stdout.write('');", 'uses process other than'],
    ["process['getBuilt' + 'inModule']('x');", 'bracket access on process'],
    ["globalThis.process.stdout.write('');", 'names globalThis'],
    ["new Function('return 1')();", 'names Function'],
    ["eval('1');", 'names eval'],
    ["process.dlopen({}, 'x');", 'names dlopen'],
    ["void import('node:fs');", 'dynamic import()'],
    ["import { Worker } from 'node:worker_threads';", 'imports node:worker_threads'],
  ])('the tree check refuses %s', (fragment, violation) => {
    const violations = sourceViolations(MODULE_SOURCE, `${text(MODULE_SOURCE)}\n${fragment}\n`);
    expect(violations.some((entry) => entry.startsWith(violation)), violations.join('; ')).toBe(true);
  });

  it('calls into the core package only through the module the check covers', () => {
    const exported = ownExports(CORE_SOURCE, text(CORE_SOURCE));
    const used = [...coreImports(MAIN_SOURCE, text(MAIN_SOURCE)), ...coreImports(MODULE_SOURCE, text(MODULE_SOURCE))];
    expect(used.length).toBeGreaterThan(0);
    expect(used.filter((name) => !exported.has(name))).toEqual([]);
  });

  it('runs exactly one command, the literal git', () => {
    const calls = [...text(MAIN_SOURCE).matchAll(new RegExp(String.raw`\b${RUN_GIT}\s*\(\s*([^,)]*)`, 'g'))].map((match) => match[1]?.trim());
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
    expect(out.join('')).toContain(`at commit ${t.commit} (operator-reported exit 0)`);
    expect(readTestArtifactRecordFile(state)).toMatchObject({
      provenance: 'operator-reported', repositoryCommit: t.commit, exitCode: 0, command: [t.python, '-m', 'pytest', SCOPE, '-q'],
    });
    expect(existsSync(t.sentinel)).toBe(false);
  });

  // Round-1 finding 2: the handed-in bytes come from running observed code.
  function ingestFile(t: Trap, junit: string): { readonly code: number; readonly err: string; readonly state: string } {
    const state = join(t.repo, '..', 'state');
    const { io, err } = captured();
    const code = runCaptureTestArtifactCli(
      ['ingest', '--repo', t.repo, '--scope', SCOPE, '--junit', junit, '--state-dir', state, '--python', t.python, '--commit', t.commit, '--exit-code', '0'],
      io,
    );
    return { code, err: err.join(''), state };
  }

  it('refuses a FIFO without opening it, so a pipe nobody writes cannot hang the ingest', () => {
    const t = trap();
    const fifo = join(t.repo, '..', 'a.xml');
    execFileSync('mkfifo', [fifo]);
    const started = Date.now();
    const result = ingestFile(t, fifo);
    expect(Date.now() - started).toBeLessThan(5_000);
    expect(result.code).toBe(1);
    expect(result.err).toContain('it is not a regular file');
    expect(readTestArtifactRecordFile(result.state)).toBeNull();
  });

  it('refuses a symlink, even to a well-formed result file', () => {
    const t = trap();
    const real = join(t.repo, '..', 'real.xml');
    const link = join(t.repo, '..', 'a.xml');
    writeFileSync(real, PASSING_JUNIT);
    symlinkSync(real, link);
    const result = ingestFile(t, link);
    expect(result.code).toBe(1);
    expect(result.err).toContain('it is not a regular file');
  });

  it('refuses a file over the ceiling before reading it', () => {
    const t = trap();
    const junit = join(t.repo, '..', 'a.xml');
    writeFileSync(junit, PASSING_JUNIT.padEnd(MAX_JUNIT_ARTIFACT_BYTES + 1, ' '));
    const result = ingestFile(t, junit);
    expect(result.code).toBe(1);
    expect(result.err).toContain(`it is ${MAX_JUNIT_ARTIFACT_BYTES + 1} bytes, over the ${MAX_JUNIT_ARTIFACT_BYTES}-byte ceiling`);
    expect(readTestArtifactRecordFile(result.state)).toBeNull();
  });

  it('reads a file at exactly the ceiling', () => {
    const dir = scratch();
    const path = join(dir, 'a.xml');
    writeFileSync(path, 'x'.repeat(64));
    expect(readBoundedRegularFile(path, 64)).toHaveLength(64);
    expect(() => readBoundedRegularFile(path, 63)).toThrow('it is 64 bytes, over the 63-byte ceiling');
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
