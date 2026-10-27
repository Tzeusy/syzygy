import { execFile, execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { promisify } from 'node:util';
import ts from 'typescript';
import { afterEach, describe, expect, it } from 'vitest';

import { ROOT, readModule, resolve } from '../../../packages/polaris-generation-core/src/workspace-reach.testkit.js';

// syzygy-bpyt.4.2: `npm run build` emits the product and no test, and `npm run typecheck` is the one program that reads the
// tests. TypeScript emits every module a project's `include` names and every module one of those imports, whatever `exclude`
// says, so a build emits no test only while each project excludes its tests and no module it builds imports one. A tool runs
// over a dist the build has just written whole: scripts/clean_build.mjs removes every dist `tsc -b` will build before it builds,
// where `tsc -b --force` kept an output whose source was gone and `tsc -b` alone also kept one altered since it was written.

const TEST = /\.test\.ts$/u;
const tracked = execFileSync('git', ['-C', ROOT, 'ls-files', '-z', '--', 'apps', 'packages'], { encoding: 'utf8' }).split('\0').filter((path) => path !== '');
const manifest = JSON.parse(readModule('package.json')) as { readonly scripts: Readonly<Record<string, string>> };
const projects = tracked.filter((path) => /^(?:apps|packages)\/[^/]+\/tsconfig\.json$/u.test(path)).map((path) => path.slice(0, -'/tsconfig.json'.length));
const CLEAN_BUILD = 'node scripts/clean_build.mjs';
const projectsOf = (script: string | undefined): string[] | undefined =>
  new RegExp(`^${CLEAN_BUILD} ((?:(?:apps|packages)/[\\w.-]+ ?)+)$`, 'u').exec(script ?? '')?.[1]?.trim().split(' ');
// Child processes run async (syzygy-w90k): a synchronous block over 60s starves vitest's worker RPC.
const run = promisify(execFile);
const cleanups: string[] = [];
afterEach(() => { for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true }); });

describe('the product build', () => {
  it('builds every workspace project with a tsconfig, each excluding its tests and keeping its outputs under dist', () => {
    expect(projectsOf(manifest.scripts['build'])?.slice().sort()).toEqual(projects.slice().sort());
    expect(projects.length).toBeGreaterThanOrEqual(10);
    for (const project of projects) {
      const config = JSON.parse(readModule(`${project}/tsconfig.json`)) as { readonly include?: unknown; readonly exclude?: unknown; readonly compilerOptions?: Record<string, unknown> };
      expect([config.include, config.exclude], project).toEqual([['src'], ['src/**/*.test.ts']]);
      expect(config.compilerOptions, project).toMatchObject({ rootDir: 'src', outDir: 'dist', tsBuildInfoFile: 'dist/.tsbuildinfo' });
    }
  });

  it('builds through the clean build alone, before every tool that runs a built module', () => {
    const scripts = Object.entries(manifest.scripts);
    expect(scripts.filter(([, script]) => /--force|\btsc\b/u.test(script)).map(([name]) => name)).toEqual(['typecheck']);
    expect(projectsOf(manifest.scripts['build:poc'])?.every((project) => projects.includes(project))).toBe(true);
    // A tool runs a built module only after one of the two builds, in the same script. poc:restart replaces a running listener
    // with an identical successor from the dist that listener runs, so it builds nothing.
    const tools = scripts.filter(([, script]) => /\bnode (?:apps|packages)\/[^ ]+\/dist\//u.test(script)).map(([name, script]) => ({ name, script }));
    expect(tools.length).toBeGreaterThanOrEqual(16);
    expect(tools.filter(({ script }) => !/^(?:node scripts\/check_generator_install\.mjs && )?npm run build(?::poc)? --silent && node /u.test(script)).map(({ name }) => name))
      .toEqual(['poc:restart']);
  });

  it('imports no test from any module it builds', () => {
    const modules = tracked.filter((path) => projects.some((project) => path.startsWith(`${project}/src/`)) && /\.ts$/u.test(path) && !TEST.test(path));
    expect(modules.length).toBeGreaterThan(200);
    const edges = modules.flatMap((from) => ts.preProcessFile(readModule(from), true, true).importedFiles.map(({ fileName }) => ({ from, to: resolve(from, fileName) })));
    expect(edges.length).toBeGreaterThan(1000);
    expect(edges.filter(({ to }) => typeof to === 'string' && TEST.test(to)).map(({ from, to }) => `${from} imports ${to}`)).toEqual([]);
  });
});

// Two one-file projects, b referencing a, and c, which neither names, in a scratch tree; the script runs from the scratch root.
function scratchTree(): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-clean-build-'));
  cleanups.push(root);
  const project = (name: string, references: readonly string[], compilerOptions: Record<string, unknown> = {}): void => {
    mkdirSync(join(root, 'packages', name, 'src'), { recursive: true });
    writeFileSync(join(root, 'packages', name, 'src', `${name}.ts`), `export const ${name} = '${name}';\n`);
    writeFileSync(join(root, 'packages', name, 'tsconfig.json'), JSON.stringify({
      compilerOptions: { composite: true, target: 'ES2022', module: 'ES2022', moduleResolution: 'bundler', types: [], rootDir: 'src', outDir: 'dist', tsBuildInfoFile: 'dist/.tsbuildinfo', ...compilerOptions },
      include: ['src'], references: references.map((path) => ({ path })),
    }));
  };
  project('a', []);
  project('b', ['../a']);
  project('c', []);
  return root;
}
const cleanBuild = (root: string, ...projects: string[]) => run(process.execPath, [join(ROOT, 'scripts/clean_build.mjs'), ...projects], { cwd: root });
const plant = (root: string, path: string, text: string): void => { mkdirSync(dirname(join(root, path)), { recursive: true }); writeFileSync(join(root, path), text); };

describe('the clean build', () => {
  it('leaves no output it did not just write in any project it builds, and leaves other projects alone', async () => {
    const root = scratchTree();
    await cleanBuild(root, 'packages/b');
    const fresh = readFileSync(join(root, 'packages/b/dist/b.js'), 'utf8');
    expect(fresh).toContain("export const b = 'b';");
    expect(existsSync(join(root, 'packages/a/dist/a.js'))).toBe(true);
    plant(root, 'packages/b/dist/b.js', 'throw new Error("poisoned output");\n');
    plant(root, 'packages/a/dist/removed-source.js', 'throw new Error("stale output");\n');
    rmSync(join(root, 'packages/a/dist/a.js'));
    plant(root, 'packages/c/dist/c.js', 'not built here\n');
    await cleanBuild(root, 'packages/b');
    expect(readFileSync(join(root, 'packages/b/dist/b.js'), 'utf8')).toBe(fresh);
    expect(existsSync(join(root, 'packages/a/dist/removed-source.js'))).toBe(false);
    expect(existsSync(join(root, 'packages/a/dist/a.js'))).toBe(true);
    expect(readFileSync(join(root, 'packages/c/dist/c.js'), 'utf8')).toBe('not built here\n');
  }, 60_000);

  it.each([
    ['names no project', [], '', 'usage:'],
    ['names a directory with no tsconfig.json', ['packages/d'], '', 'packages/d: not a workspace project'],
    ['names a path outside the workspaces', ['scripts'], '', 'scripts: not a workspace project'],
    ['reaches a project whose outputs leave dist', ['packages/b'], 'out', 'packages/a/tsconfig.json: its outputs and incremental state are not both under dist'],
  ])('refuses, removing nothing, when it %s', async (_case, projects, outDir, reason) => {
    const root = scratchTree();
    if (outDir !== '') writeFileSync(join(root, 'packages/a/tsconfig.json'), readFileSync(join(root, 'packages/a/tsconfig.json'), 'utf8').replace('"outDir":"dist"', `"outDir":"${outDir}"`));
    plant(root, 'packages/b/dist/b.js', 'kept\n');
    await expect(cleanBuild(root, ...projects)).rejects.toMatchObject({ stderr: expect.stringContaining(reason) });
    expect(readFileSync(join(root, 'packages/b/dist/b.js'), 'utf8')).toBe('kept\n');
  }, 30_000);
});

describe('the typecheck', () => {
  it('reads every module of every workspace, tests among them, from source and emits nothing', () => {
    const config = JSON.parse(readModule('tsconfig.json')) as { readonly compilerOptions: Record<string, unknown>; readonly include: readonly string[] };
    expect(manifest.scripts['typecheck']).toBe('tsc -p tsconfig.json');
    expect(config.include).toEqual(['apps/*/src', 'packages/*/src', 'packages/*/test-support']);
    expect(config.compilerOptions).toMatchObject({ noEmit: true, customConditions: ['source'] });
    const outside = tracked.filter((path) => /\.[cm]?tsx?$/u.test(path) && !/^(?:apps|packages)\/[^/]+\/(?:src|test-support)\//u.test(path));
    expect(outside).toEqual(['packages/cap1-system/vitest.config.ts']);
  });
});
