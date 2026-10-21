import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, normalize } from 'node:path';
import { describe, expect, it } from 'vitest';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));

// The root suite's test roots are the vitest.config.ts `test.projects` include
// globs, read from the config so that a project added there is scanned here
// (syzygy-bpyt.4.1: a hand list had missed two of seven). A vitest worker
// answers its parent over an RPC with a fixed 60s
// timeout; a test that blocks the worker's event loop longer than that makes
// the pending `onTaskUpdate` call time out, and the run exits 1 with every
// test passed (syzygy-w90k). An install, a build or a documented command can
// run past 60s under load, so only short local tools may run synchronously,
// in a test file or in any module a test file imports (syzygy-3f5c).
const VITEST_CONFIG = 'vitest.config.ts';
const PROJECT_INCLUDE = /\binclude:\s*\[\s*'([^']+)'\s*\]/g;
const INCLUDE_KEY = /\binclude:/g;
const PROJECT_NAME = /\bname:\s*'/g;
// The config's aliases (a test that imports a workspace package runs its source).
const ALIAS = /'(@syzygy\/[^']+)':\s*fileURLToPath\(\s*new URL\('\.\/([^']+)'/g;
const ALIAS_KEY = /'@syzygy\/[^']+':/g;
const SHORT_COMMANDS = new Set(['git', 'mkfifo', 'bd', 'which', 'ss']);
// The long synchronous calls the scan finds and keeps, by module and
// command, each with why it cannot hold a worker near the 60s bound. An entry
// that matches no call fails, so none outlives its call. Syzygy runs no
// observed test suite (syzygy-hjuz: SEC-3, RFC5-18), so no entry may name one.
const LAUNCHER = 'the `syzygy polaris` launcher at run time; suite tests import only its pure helpers (blockingWhy, toolPathsFor), and no suite test calls runPolarisCli';
const EXEMPT: Readonly<Record<string, string>> = {
  "packages/polaris-dossier/src/polaris.ts 'tmux'": LAUNCHER,
  "packages/polaris-dossier/src/polaris.ts 'sh'": LAUNCHER,
  "packages/polaris-dossier/src/polaris.ts claudeExecutable(": LAUNCHER,
  "packages/polaris-dossier/src/session-view.ts 'bwrap'": 'viewProbeRefusal, called only by the launcher at run time; suite tests import only the pure view builders',
  "packages/polaris-generation-consent/src/recorder-fixtures.testkit.ts 'python3'":
    'renders an act through a repository recorder, cached per process. Measured 2026-10-21 over the dossier and consent projects at load 27 on 12 cores: 192 calls, p50 508 ms, max 2.5 s, at most 7.8 s summed within one test and 14.5 s outside tests in one file (syzygy-bpyt.4.1)',
};
const SELF = 'apps/three-surface-poc/src/sync-child-process-guard.test.ts';
const SYNC_FUNCTIONS = ['execFileSync', 'execSync', 'spawnSync'];
const MODULE_SPECIFIER = /(?:\bfrom|\bimport)\s*\(?\s*['"]([^'"]+)['"]/g;
const CHILD_PROCESS_LITERAL = /['"](?:node:)?child_process['"]/g;
// Each recognized way to bind child_process; any other mention fails closed.
const CHILD_PROCESS_BINDINGS = [
  /\bimport\s+(?:type\s+)?([^;'"]*?)\s+from\s+['"](?:node:)?child_process['"]/g,
  /\b(?:const|let|var)\s+([^=;]+?)\s*=\s*(?:await\s+import|require)\s*\(\s*['"](?:node:)?child_process['"]\s*\)/g,
];
// Mentions that bind no call here: a type query, and a vi.mock whose factory
// forwards to the real function, whose callers are scanned where they call.
const CHILD_PROCESS_NON_BINDINGS = [
  /\btypeof\s+import\s*\(\s*['"](?:node:)?child_process['"]\s*\)/g,
  /\bvi\s*\.\s*mock\s*\(\s*['"](?:node:)?child_process['"]/g,
];

interface SyncCall { readonly line: number; readonly command: string }
interface SuiteConfig { readonly roots: readonly string[]; readonly entries: Readonly<Record<string, string>> }

/** The test roots and workspace aliases of the root vitest config; any shape it does not recognize throws. */
function suiteConfig(config: string): SuiteConfig {
  const includes = [...config.matchAll(PROJECT_INCLUDE)].map((match) => match[1]!);
  const projects = config.match(PROJECT_NAME)?.length ?? 0;
  if (includes.length !== (config.match(INCLUDE_KEY)?.length ?? 0) || includes.length !== projects) {
    throw new Error(`${VITEST_CONFIG}: ${projects} projects but ${includes.length} recognized single-glob includes`);
  }
  const roots = includes.map((glob) => {
    const root = /^((?:apps|packages)\/[\w.-]+\/src\/)\*\*\/\*\.test\.ts$/.exec(glob)?.[1];
    if (root === undefined) throw new Error(`${VITEST_CONFIG}: unrecognized project include ${glob}`);
    return root;
  });
  const aliases = [...config.matchAll(ALIAS)];
  if (aliases.length !== (config.match(ALIAS_KEY)?.length ?? 0)) throw new Error(`${VITEST_CONFIG}: unrecognized @syzygy alias`);
  return { roots, entries: Object.fromEntries(aliases.map((match) => [match[1]!, match[2]!])) };
}

const lineOf = (source: string, index: number): number => source.slice(0, index).split('\n').length;
const escape = (name: string): string => name.replace(/[$]/g, '\\$');

/** Every synchronous child-process call in `source`, under whatever name it binds them. */
function syncCalls(source: string): SyncCall[] {
  const direct = new Set<string>();
  const namespaces = new Set<string>();
  const recognized = new Set<number>();
  const bindingSpans: [number, number][] = [];
  for (const pattern of CHILD_PROCESS_BINDINGS) {
    for (const match of source.matchAll(pattern)) {
      bindingSpans.push([match.index ?? 0, (match.index ?? 0) + match[0].length]);
      recognized.add((match.index ?? 0) + match[0].search(/['"](?:node:)?child_process['"]/));
      const clause = match[1]!.trim();
      const braces = /\{([^}]*)\}/.exec(clause);
      for (const spec of braces?.[1]?.split(',') ?? []) {
        const binding = /^(?:type\s+)?(\w+)(?:\s*(?:as|:)\s*(\w+))?$/.exec(spec.trim());
        if (binding !== null && !spec.trim().startsWith('type ') && SYNC_FUNCTIONS.includes(binding[1]!)) direct.add(binding[2] ?? binding[1]!);
      }
      const namespace = /\*\s+as\s+(\w+)/.exec(clause)?.[1] ?? (/^(\w+)\s*(?:,|$)/.exec(clause)?.[1]);
      if (namespace !== undefined && namespace !== 'type') namespaces.add(namespace);
    }
  }
  for (const pattern of CHILD_PROCESS_NON_BINDINGS) {
    for (const match of source.matchAll(pattern)) recognized.add((match.index ?? 0) + match[0].search(/['"](?:node:)?child_process['"]/));
  }
  const calls: SyncCall[] = [];
  // Fail closed on re-binding (syzygy-ty1x): outside its own binding, a sync
  // name may only be called, and a namespace only reached through
  // `.<name>`, a sync one only called. `const run = execFileSync`,
  // `const { execSync } = cp`, `cp['execSync']` and `const run =
  // cp.execFileSync` would otherwise call it under a name nothing follows.
  const insideBinding = (index: number): boolean => bindingSpans.some(([start, end]) => index >= start && index < end);
  for (const name of direct) {
    for (const match of source.matchAll(new RegExp(`(?<![\\w.$])${escape(name)}(?![\\w$])(?!\\s*\\()`, 'g'))) {
      if (!insideBinding(match.index ?? 0)) calls.push({ line: lineOf(source, match.index ?? 0), command: `<${name} re-bound>` });
    }
  }
  for (const name of namespaces) {
    for (const match of source.matchAll(new RegExp(`(?<![\\w.$])${escape(name)}(?![\\w$])(?:\\s*\\.\\s*(\\w+)(\\s*\\()?)?`, 'g'))) {
      if (insideBinding(match.index ?? 0)) continue;
      const member = match[1];
      if (member === undefined || (SYNC_FUNCTIONS.includes(member) && match[2] === undefined)) {
        calls.push({ line: lineOf(source, match.index ?? 0), command: `<${name}${member === undefined ? '' : `.${member}`} re-bound>` });
      }
    }
  }
  for (const literal of source.matchAll(CHILD_PROCESS_LITERAL)) {
    if (!recognized.has(literal.index ?? 0)) calls.push({ line: lineOf(source, literal.index ?? 0), command: '<unrecognized child_process binding>' });
  }
  const callees = [...[...direct].map(escape), ...[...namespaces].map((name) => `${escape(name)}\\s*\\.\\s*(?:${SYNC_FUNCTIONS.join('|')})`)];
  if (callees.length === 0) return calls;
  for (const match of source.matchAll(new RegExp(`(?<![\\w.$])(?:${callees.join('|')})\\s*\\(\\s*([^,)\\n]*)`, 'g'))) {
    calls.push({ line: lineOf(source, match.index ?? 0), command: match[1]!.trim() });
  }
  return calls.sort((a, b) => a.line - b.line);
}

/** The calls whose command is not a literal short local tool. */
function longSyncCalls(source: string): SyncCall[] {
  return syncCalls(source).filter(({ command }) => {
    const literal = /^(['"`])(.*)\1$/.exec(command);
    return literal === null || !SHORT_COMMANDS.has(literal[2]!);
  });
}

/** Every module a vitest worker loads for `tests`: the tests and their relative and workspace imports, transitively. */
function importClosure(tests: readonly string[], read: (path: string) => string | undefined, entries: SuiteConfig['entries']): string[] {
  const seen = new Set(tests);
  const pending = [...tests];
  while (pending.length > 0) {
    const path = pending.pop()!;
    for (const match of (read(path) ?? '').matchAll(MODULE_SPECIFIER)) {
      const specifier = match[1]!;
      const target = specifier.startsWith('.')
        ? normalize(join(dirname(path), specifier)).replace(/\.js$/, '.ts')
        : entries[specifier];
      for (const candidate of target === undefined ? [] : [target, `${target}.ts`, join(target, 'index.ts')]) {
        if (!seen.has(candidate) && read(candidate) !== undefined) {
          seen.add(candidate);
          pending.push(candidate);
          break;
        }
      }
    }
  }
  return [...seen].sort();
}

function trackedTypeScript(): Map<string, string> {
  const paths = execFileSync('git', ['-C', REPO_ROOT, 'ls-files', '-z', '--cached', '--others', '--exclude-standard', '--', '*.ts'], { encoding: 'utf8' }).split('\0').filter((path) => path !== '');
  const sources = new Map<string, string>();
  for (const path of paths) {
    try { sources.set(path, readFileSync(join(REPO_ROOT, path), 'utf8')); } catch { /* listed but deleted in the worktree */ }
  }
  return sources;
}

describe('suite child processes and the vitest worker RPC', () => {
  it('runs only short local tools synchronously in a suite test file or any module it imports', () => {
    const sources = trackedTypeScript();
    const { roots, entries } = suiteConfig(readFileSync(join(REPO_ROOT, VITEST_CONFIG), 'utf8'));
    const tests = [...sources.keys()].filter((path) => path.endsWith('.test.ts') && roots.some((root) => path.startsWith(root)));
    const modules = importClosure(tests, (path) => sources.get(path), entries);
    // Every project the config runs is scanned, and every alias resolves.
    expect(roots.length).toBeGreaterThanOrEqual(7);
    expect(roots).toEqual(expect.arrayContaining(['packages/polaris-dossier/src/', 'packages/polaris-generation-consent/src/']));
    for (const root of roots) expect(tests.some((path) => path.startsWith(root)), root).toBe(true);
    for (const entry of Object.values(entries)) expect(sources.has(entry), entry).toBe(true);
    expect(tests.length).toBeGreaterThan(100);
    expect(tests).toContain(SELF);
    expect(modules.length).toBeGreaterThan(tests.length + 100);
    expect(modules).toContain('apps/three-surface-poc/src/test-model-fixture.ts');
    expect(modules).toContain('packages/three-surface-poc-core/src/work-items.ts');
    const found = modules
      .filter((path) => path !== SELF)
      .flatMap((path) => longSyncCalls(sources.get(path)!).map(({ line, command }) => ({ at: `${path}:${line} ${command}`, key: `${path} ${command}` })));
    expect(found.filter(({ key }) => !Object.hasOwn(EXEMPT, key)).map(({ at }) => at)).toEqual([]);
    expect(Object.keys(EXEMPT).filter((key) => !found.some((call) => call.key === key))).toEqual([]);
  });

  it('flags an install, a build or a computed command and leaves async and short tools alone', () => {
    const named = "import { execFileSync, execSync, spawnSync, execFile } from 'node:child_process';\n";
    const commands = (body: string): string[] => longSyncCalls(named + body).map(({ command }) => command);
    expect(commands("execFileSync('npm', ['ci'])")).toEqual(["'npm'"]);
    expect(commands('execSync("npm run build:poc")')).toEqual(['"npm run build:poc"']);
    expect(commands('spawnSync(`npx`, [])')).toEqual(['`npx`']);
    expect(commands('execFileSync(documented[0]!, args)')).toEqual(['documented[0]!']);
    expect(commands('execFileSync(git, args)')).toEqual(['git']);
    expect(commands("await run('npm', ['ci'])")).toEqual([]);
    expect(commands("execFile('npm', ['ci'])")).toEqual([]);
    expect(commands("execFileSync('git', ['rev-parse', 'HEAD'])")).toEqual([]);
    expect(commands('spawnSync("mkfifo", [path])')).toEqual([]);
    expect(commands("execSync('git status')")).toEqual(["'git status'"]);
  });

  it('follows every way of binding the synchronous calls, and fails closed on a binding it does not recognize', () => {
    const commands = (source: string): string[] => longSyncCalls(source).map(({ command }) => command);
    expect(commands("import { execFileSync as run } from 'node:child_process';\nrun('npm', ['ci']);")).toEqual(["'npm'"]);
    expect(commands("import * as cp from 'child_process';\ncp.spawnSync('npm', ['ci']);")).toEqual(["'npm'"]);
    expect(commands("import cp from 'node:child_process';\ncp . execSync('npm ci');")).toEqual(["'npm ci'"]);
    expect(commands("const { execFileSync: sh } = await import('node:child_process');\nsh('npm', []);")).toEqual(["'npm'"]);
    expect(commands("const cp = require('child_process');\ncp.execFileSync('npm', []);")).toEqual(["'npm'"]);
    expect(commands("export { execFileSync } from 'node:child_process';")).toEqual(['<unrecognized child_process binding>']);
    expect(commands("vi.mock('node:child_process', async (importOriginal) => ({ ...(await importOriginal<typeof import('node:child_process')>()) }));")).toEqual([]);
    expect(commands("const loader = () => import('node:child_process');")).toEqual(['<unrecognized child_process binding>']);
    expect(commands("import { type ExecFileSyncOptions, execFile } from 'node:child_process';\nexecFile('npm', []);")).toEqual([]);
    expect(commands("import { execFileSync as run } from 'node:child_process';\nrun('git', ['status']);\nother.run('npm');")).toEqual([]);
  });

  it('fails closed when a sync function is re-bound to a name the scan does not follow (syzygy-ty1x)', () => {
    const commands = (source: string): string[] => longSyncCalls(source).map(({ command }) => command);
    const namespace = "import * as cp from 'node:child_process';\n";
    const named = "import { execFileSync } from 'node:child_process';\n";
    expect(commands(`${namespace}const { execSync } = cp;\nexecSync('npm ci');`)).toEqual(['<cp re-bound>']);
    expect(commands(`${namespace}const run = cp.execFileSync;\nrun('npm', []);`)).toEqual(['<cp.execFileSync re-bound>']);
    expect(commands(`${named}const run = execFileSync;\nrun('npm', []);`)).toEqual(['<execFileSync re-bound>']);
    expect(commands(`${namespace}cp['execSync']('npm ci');`)).toEqual(['<cp re-bound>']);
    expect(commands("const cp = require('child_process');\nconst sh = cp.spawnSync;")).toEqual(['<cp.spawnSync re-bound>']);
    expect(commands("import { execFileSync as run } from 'node:child_process';\nexport { run };")).toEqual(['<run re-bound>']);
    // Calls, async members and other objects' same-named members stay clean.
    expect(commands(`${namespace}cp.execFileSync('git', []);\ncp.spawn('npm', []);\nconst spawn = cp.spawn;\nother.cp = 1;`)).toEqual([]);
    expect(commands(`${named}execFileSync('git', ['status']);\nactual.execFileSync(file, args);\nconst passed = actual.execFileSync;\nconst o = { execFileSyncLike: 1 };`)).toEqual([]);
  });

  it('reads every project root and alias from the vitest config, and fails closed on a shape it does not recognize', () => {
    const project = (include: string): string => `{ extends: true, test: { name: 'p', include: [${include}] } },`;
    const alias = "'@syzygy/a': fileURLToPath(\n  new URL('./packages/a/src/index.ts', import.meta.url),\n),";
    expect(suiteConfig(`${alias}\n${project("'packages/a/src/**/*.test.ts'")}\n${project("'apps/b/src/**/*.test.ts'")}`)).toEqual({
      roots: ['packages/a/src/', 'apps/b/src/'],
      entries: { '@syzygy/a': 'packages/a/src/index.ts' },
    });
    expect(() => suiteConfig(project('"packages/a/src/**/*.test.ts"'))).toThrow(/recognized single-glob includes/);
    expect(() => suiteConfig(project("'packages/a/src/**/*.test.ts', 'packages/b/src/**/*.test.ts'"))).toThrow(/recognized single-glob includes/);
    expect(() => suiteConfig(project("'packages/a/**/*.spec.ts'"))).toThrow(/unrecognized project include/);
    expect(() => suiteConfig("{ name: 'p', include: ['packages/a/src/**/*.test.ts'] }, { name: 'q' }")).toThrow(/2 projects/);
    expect(() => suiteConfig("'@syzygy/a': path.join(root, 'a'),")).toThrow(/unrecognized @syzygy alias/);
  });

  it('scans a helper module a test imports, through relative and workspace imports', () => {
    const files: Record<string, string> = {
      'apps/x/src/a.test.ts': "import { helper } from './helpers/build.js';\nimport { core } from '@syzygy/three-surface-poc-core';",
      'apps/x/src/helpers/build.ts': "import { execFileSync as sh } from 'node:child_process';\nexport const helper = () => sh('npm', ['run', 'build']);",
      'packages/three-surface-poc-core/src/index.ts': "export * from './deep.js';",
      'packages/three-surface-poc-core/src/deep.ts': "import * as cp from 'node:child_process';\nexport const core = () => cp.execSync('npm ci');",
      'apps/x/src/unused.ts': "import { execFileSync } from 'node:child_process';\nexecFileSync('npm', []);",
    };
    const modules = importClosure(['apps/x/src/a.test.ts'], (path) => files[path], { '@syzygy/three-surface-poc-core': 'packages/three-surface-poc-core/src/index.ts' });
    expect(modules).toEqual(['apps/x/src/a.test.ts', 'apps/x/src/helpers/build.ts', 'packages/three-surface-poc-core/src/deep.ts', 'packages/three-surface-poc-core/src/index.ts']);
    expect(modules.flatMap((path) => longSyncCalls(files[path]!).map(({ line, command }) => `${path}:${line} ${command}`))).toEqual([
      "apps/x/src/helpers/build.ts:2 'npm'",
      "packages/three-surface-poc-core/src/deep.ts:2 'npm ci'",
    ]);
  });
});
