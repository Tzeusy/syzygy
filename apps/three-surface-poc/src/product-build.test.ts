import { execFileSync } from 'node:child_process';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';

import { ROOT, readModule, resolve } from '../../../packages/polaris-generation-core/src/workspace-reach.testkit.js';

// syzygy-bpyt.4.2: `npm run build` emits the product and no test, and `npm run typecheck` is the one program that reads the
// tests. TypeScript emits every module a project's `include` names and every module one of those imports, whatever `exclude`
// says, so a build emits no test only while each project excludes its tests and no module it builds imports one.

const TEST = /\.test\.ts$/u;
const tracked = execFileSync('git', ['-C', ROOT, 'ls-files', '-z', '--', 'apps', 'packages'], { encoding: 'utf8' }).split('\0').filter((path) => path !== '');
const manifest = JSON.parse(readModule('package.json')) as { readonly scripts: Readonly<Record<string, string>> };
const projects = tracked.filter((path) => /^(?:apps|packages)\/[^/]+\/tsconfig\.json$/u.test(path)).map((path) => path.slice(0, -'/tsconfig.json'.length));

describe('the product build', () => {
  it('builds every workspace project with a tsconfig, each excluding its tests', () => {
    const built = /^tsc -b ((?:(?:apps|packages)\/[\w.-]+ ?)+)$/u.exec(manifest.scripts['build'] ?? '')?.[1]?.trim().split(' ');
    expect(built?.slice().sort()).toEqual(projects.slice().sort());
    expect(projects.length).toBeGreaterThanOrEqual(10);
    for (const project of projects) {
      const config = JSON.parse(readModule(`${project}/tsconfig.json`)) as Record<string, unknown>;
      expect([config['include'], config['exclude']], project).toEqual([['src'], ['src/**/*.test.ts']]);
    }
  });

  it('imports no test from any module it builds', () => {
    const modules = tracked.filter((path) => projects.some((project) => path.startsWith(`${project}/src/`)) && /\.ts$/u.test(path) && !TEST.test(path));
    expect(modules.length).toBeGreaterThan(200);
    const edges = modules.flatMap((from) => ts.preProcessFile(readModule(from), true, true).importedFiles.map(({ fileName }) => ({ from, to: resolve(from, fileName) })));
    expect(edges.length).toBeGreaterThan(1000);
    expect(edges.filter(({ to }) => typeof to === 'string' && TEST.test(to)).map(({ from, to }) => `${from} imports ${to}`)).toEqual([]);
  });
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
