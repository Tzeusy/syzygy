import { existsSync, readFileSync } from 'node:fs';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { beforeAll, describe, expect, it } from 'vitest';

// syzygy-hjuz: the live verification test is skipped in the default suite,
// so its own assertions cannot guard it. This hermetic check reads its
// source, and every core module it reaches through its imports, and holds
// them to the owner's syzygy-4mbu direction: the test ingests a JUnit file
// the operator produced and runs no observed code (SEC-3, RFC5-18). Read off
// the TypeScript syntax tree, so a comment or string never counts and a
// bracket, alias or the built-in module table does not slip past a word
// match (#383 round 1, finding 3).
//
// Residual: a static guard against future edits cannot be complete.
// JavaScript reaches the global object and the module table by too many
// routes (#383 round 2 found `.constructor.constructor`). This check refuses
// every route found so far, as names, member names and literal keys, across
// the whole closure. It refuses computed member access with a key it cannot
// read in the live test only: the modules the test imports index arrays and
// records by variable keys at 89 sites, so a key built at run time (the
// string "constructor" assembled from pieces) inside one of them is not
// caught here. The test is skipped in the default suite and runs only
// when an operator sets SYZYGY_POC_BUTLERS_REPO; a new route has to be
// spelled where a reviewer sees it, but the check does not prove that no
// route exists.

const SRC = dirname(fileURLToPath(import.meta.url));
const LIVE = 'test-artifact-verification.live.test.ts';
// Spelled in pieces so the suite's child-process guard does not read this
// file's patterns as calls.
const RUN_GIT = ['execFile', 'Sync'].join('');
const PROCESS_MODULE = ['node:child', 'process'].join('_');

/** The only commands any module in the closure may start: git, and the
 * beads tool the work-item reader queries. Neither is observed code. */
const COMMANDS = new Set(['git', 'bd']);

/** Identifiers that reach a process starter or arbitrary code indirectly.
 * `process.dlopen` and `process.binding` are refused by the member list
 * below, so a parameter that happens to be named `binding` is not. */
const FORBIDDEN_IDENTIFIERS = new Set(['getBuiltinModule', 'globalThis', 'global', 'eval', 'Function', 'require', 'Worker', 'Reflect']);

/** #383 round 2, finding 1: every object's `.constructor.constructor` is
 * `Function`, so `process.stdout.constructor.constructor('return this')()`
 * reached the global object with no forbidden word in it. These names may
 * not appear as an identifier, a member name or a literal key, and the
 * reflection calls that fetch a member by a computed name are refused too. */
const FORBIDDEN_MEMBER_NAMES = new Set([
  'constructor', 'prototype', '__proto__',
  'getPrototypeOf', 'setPrototypeOf', 'getOwnPropertyDescriptor', 'getOwnPropertyDescriptors', 'getOwnPropertyNames', 'defineProperty', 'Proxy',
]);

/** A computed key the check can read: a plain string or number literal. */
function isLiteralKey(node: ts.Expression): boolean {
  return ts.isStringLiteral(node) || ts.isNumericLiteral(node);
}

/** Workspace packages in the closure, followed into their sources. */
const WORKSPACE_PACKAGES: Readonly<Record<string, string>> = {
  '@syzygy/cap1-core': '../../cap1-core/src/index.ts',
};

/** The only members of `process` the closure may touch. */
const PROCESS_MEMBERS = new Set(['env', 'stdout', 'stderr', 'argv', 'exitCode', 'pid', 'platform', 'cwd']);

/** Packages the closure may import without being followed. `yaml` is the
 * one third-party dependency (cap1-core's YAML dialect); the check stops at
 * workspace sources and does not read installed packages. */
const ALLOWED_PACKAGES = new Set([PROCESS_MODULE, 'node:fs', 'node:path', 'node:crypto', 'node:os', 'node:url', 'vitest', 'yaml']);

interface Violation {
  readonly file: string;
  readonly reason: string;
}

/** Each violation in one file, and the relative modules it imports. */
function scan(file: string, text: string): { readonly violations: Violation[]; readonly imports: string[] } {
  const violations: Violation[] = [];
  const imports: string[] = [];
  const add = (reason: string): void => { violations.push({ file, reason }); };
  const source = ts.createSourceFile(file, text, ts.ScriptTarget.Latest, true);
  const visit = (node: ts.Node): void => {
    if ((ts.isImportDeclaration(node) || ts.isExportDeclaration(node)) && node.moduleSpecifier !== undefined && ts.isStringLiteral(node.moduleSpecifier)) {
      const specifier = node.moduleSpecifier.text;
      if (specifier.startsWith('./') || specifier.startsWith('../')) imports.push(specifier);
      else if (WORKSPACE_PACKAGES[specifier] !== undefined) imports.push(specifier);
      else if (!ALLOWED_PACKAGES.has(specifier)) add(`imports ${specifier}`);
      if (specifier === PROCESS_MODULE && ts.isImportDeclaration(node)) {
        const bindings = node.importClause?.namedBindings;
        const names = bindings !== undefined && ts.isNamedImports(bindings) ? bindings.elements.map((element) => element.getText()) : ['<not named>'];
        if (names.some((name) => name !== RUN_GIT) || node.importClause?.name !== undefined) add(`binds ${names.join(', ')} from the process module`);
      }
    }
    if (ts.isCallExpression(node)) {
      if (node.expression.kind === ts.SyntaxKind.ImportKeyword) add('dynamic import()');
      if (ts.isIdentifier(node.expression) && node.expression.text === RUN_GIT) {
        const command = node.arguments[0];
        if (command === undefined || !ts.isStringLiteral(command) || !COMMANDS.has(command.text)) {
          add(`starts ${command?.getText() ?? 'nothing'}, not a literal ${[...COMMANDS].join(' or ')}`);
        }
      }
    }
    if (ts.isIdentifier(node) || ts.isStringLiteral(node) || ts.isNoSubstitutionTemplateLiteral(node)) {
      if (FORBIDDEN_MEMBER_NAMES.has(node.text)) add(`reaches ${node.text}`);
    }
    if (file === LIVE) {
      // The live test only: the modules it imports index arrays and
      // records by variable keys at 89 sites (counted 2026-10-07), which
      // this check does not rewrite. See the residual in the header.
      if (ts.isElementAccessExpression(node) && !isLiteralKey(node.argumentExpression)) add('computed access with a non-literal key');
      if (ts.isComputedPropertyName(node) && !isLiteralKey(node.expression)) add('computed property name with a non-literal key');
    }
    // #383 round 3, note 1: the git runner reached through `.call`, `.apply`
    // or an alias starts any command. Outside its import it may appear only
    // as the callee of a direct call, whose command the rule above checks.
    if (ts.isIdentifier(node) && node.text === RUN_GIT && !ts.isImportSpecifier(node.parent)) {
      const call = node.parent;
      if (!ts.isCallExpression(call) || call.expression !== node) add(`uses ${RUN_GIT} other than as a direct call`);
    }
    if (ts.isIdentifier(node)) {
      if (FORBIDDEN_IDENTIFIERS.has(node.text)) add(`names ${node.text}`);
      if (node.text === 'process') {
        const parent = node.parent;
        const member = ts.isPropertyAccessExpression(parent) && parent.expression === node ? parent.name.text : null;
        if (member === null || !PROCESS_MEMBERS.has(member)) add('uses process other than a listed member');
      }
    }
    ts.forEachChild(node, visit);
  };
  visit(source);
  return { violations, imports };
}

/** The live test and every core module reachable through its relative
 * imports, with each one's violations. */
function closure(seed: string, extra: Readonly<Record<string, string>> = {}): { readonly files: string[]; readonly violations: Violation[] } {
  const seen = new Set<string>();
  const violations: Violation[] = [];
  const queue = [seed];
  while (queue.length > 0) {
    const file = queue.shift() as string;
    if (seen.has(file)) continue;
    seen.add(file);
    const text = (extra[file] ?? '') + readFileSync(join(SRC, file), 'utf8');
    const result = scan(file, text);
    violations.push(...result.violations);
    for (const specifier of result.imports) {
      const workspace = WORKSPACE_PACKAGES[specifier];
      const target = workspace !== undefined ? resolve(SRC, workspace) : resolve(SRC, dirname(file), specifier.replace(/\.js$/, '.ts'));
      const name = relative(SRC, target);
      if (!existsSync(target)) violations.push({ file, reason: `imports ${specifier}, which is not a source file` });
      else queue.push(name);
    }
  }
  return { files: [...seen].sort(), violations };
}

describe('the live verification test, and every module it imports, runs no observed code', () => {
  let source = '';
  beforeAll(() => {
    source = readFileSync(join(SRC, LIVE), 'utf8');
  });

  it('reaches the model, its observers and the verification module, and no file in that closure can start anything but git or bd', () => {
    const { files, violations } = closure(LIVE);
    // Denominator: the closure must actually include the modules that hold
    // process starts, or the check proves nothing about them.
    for (const expected of [LIVE, 'model.ts', 'test-artifact-verification.ts', 'worker-change-observation.ts', 'work-items.ts', 'code-structure.ts', '../../cap1-core/src/index.ts']) {
      expect(files).toContain(expected);
    }
    expect(violations).toEqual([]);
  });

  // #383 round 1, finding 3: each of these evaded a word check or could.
  it.each([
    ["(process as unknown as { getBuiltinModule(n: string): unknown }).getBuiltinModule('x');", 'names getBuiltinModule'],
    ["const p = process; void p;", 'uses process other than a listed member'],
    ["process['getBuilt' + 'inModule'];", 'uses process other than a listed member'],
    ["globalThis.process.env.X;", 'names globalThis'],
    ["new Function('return 1')();", 'names Function'],
    ["eval('1');", 'names eval'],
    ["process.dlopen({}, 'x');", 'uses process other than a listed member'],
    ["void import('node:fs');", 'dynamic import()'],
    [`${RUN_GIT}('python3', ['-m', 'pytest']);`, 'starts '],
    [`const cmd = 'git'; ${RUN_GIT}(cmd, []);`, 'starts '],
    ["import { Worker } from 'node:worker_threads';", 'imports node:worker_threads'],
    // #383 round 2, finding 1: the reviewer's evasion and its respellings.
    ["const g = (process.stdout.constructor as unknown as { constructor: (s: string) => () => Record<string, unknown> }).constructor('return this.process')();", 'reaches constructor'],
    ["const g: Record<string, unknown> = {}; g[['get', 'Builtin', 'Module'].join('')];", 'computed access with a non-literal key'],
    ["const k = 'x'; const o: Record<string, unknown> = {}; o[k];", 'computed access with a non-literal key'],
    ["process.stdout['constructor'];", 'reaches constructor'],
    ["const { constructor: c } = process.stdout;", 'reaches constructor'],
    ["const k = 'x'; const { [k]: c } = process.stdout as unknown as Record<string, unknown>;", 'computed property name with a non-literal key'],
    ["Object.getPrototypeOf(process.stdout);", 'reaches getPrototypeOf'],
    ["Object.getOwnPropertyDescriptor(process.stdout, 'x');", 'reaches getOwnPropertyDescriptor'],
    ["({}).__proto__;", 'reaches __proto__'],
    ["(() => 0).prototype;", 'reaches prototype'],
    // #383 round 3, note 1: the permitted binding, reached without a direct call.
    [`${RUN_GIT}.call(null, 'sh', []);`, `uses ${RUN_GIT} other than as a direct call`],
    [`${RUN_GIT}.apply(null, ['sh', []]);`, `uses ${RUN_GIT} other than as a direct call`],
    [`const r = ${RUN_GIT}; r('sh');`, `uses ${RUN_GIT} other than as a direct call`],
  ])('the tree check refuses %s', (fragment, violation) => {
    const { violations } = closure(LIVE, { [LIVE]: `${fragment}\n` });
    expect(violations.some((entry) => entry.file === LIVE && entry.reason.startsWith(violation)), JSON.stringify(violations)).toBe(true);
  });

  it('reads the operator-reported result named by the environment, through the bounded reader', () => {
    for (const name of ['SYZYGY_POC_BUTLERS_JUNIT', 'SYZYGY_POC_BUTLERS_JUNIT_COMMIT', 'SYZYGY_POC_BUTLERS_JUNIT_EXIT']) {
      expect(source).toContain(`process.env.${name};`);
    }
    expect(source).toContain('const rawJUnit = readBoundedRegularFile(JUNIT);');
    expect(source).not.toMatch(/\breadFileSync\b/);
  });

  // #383 round 1, finding 1: the commit, exit status and run are the
  // operator's report, so the live composition must resolve to report-fact.
  it('builds an operator-reported record and expects report-fact, never Verified', () => {
    expect(source).toContain('buildOperatorReportedTestArtifactRecord({');
    expect(source).not.toMatch(/buildTestArtifactRecordFromJUnit|capturedAt:/);
    expect(source).toContain("kind: 'reported',\n        tier: 'report-fact',");
    expect(source).not.toContain("toBe('verified')");
  });
});
