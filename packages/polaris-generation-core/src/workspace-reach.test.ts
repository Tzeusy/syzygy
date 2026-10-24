import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { describe, expect, it } from 'vitest';
import { ROOT, resolve, resolveIn, type Manifest, type Workspace } from './workspace-reach.testkit.js';

// syzygy-bpyt.8.36 (the review of 8.34, N1): the resolver both reach guards share reads a specifier it cannot follow as Node would
// as naming no module, so their "resolves every" rows fail on it rather than passing it as outside the workspace. The tree holds no
// such specifier and no `imports` field today, so the forms that need one run against a workspace of two packages written here.

const BARREL = 'packages/polaris-dossier/src/index.ts';

/** Two packages: `@syzygy/app` with the given `imports`, and `@syzygy/lib` with the given `.` export over two modules. */
function workspace(imports: Record<string, unknown>, dot: unknown = './dist/index.js'): Workspace {
  const manifests: Manifest[] = [
    { name: '@syzygy/app', dir: 'apps/app', imports, main: './dist/main.js' },
    { name: '@syzygy/lib', dir: 'packages/lib', exports: { '.': dot, './argv': { types: './dist/argv.d.ts', import: './dist/argv.js' } } },
  ];
  const files = new Set(['apps/app/src/main.ts', 'apps/app/src/local.ts', 'packages/lib/src/index.ts', 'packages/lib/src/argv.ts']);
  return { manifests: new Map(manifests.map((manifest) => [manifest.name, manifest])), isFile: (path) => files.has(path) };
}

describe('the shared workspace resolver', () => {
  it('resolves a subpath export, a relative module and the barrel by name, and leaves a built-in and a dependency outside', () => {
    expect(resolve('apps/syzygy/src/main.ts', '@syzygy/polaris-dossier/argv')).toBe('packages/polaris-dossier/src/argv.ts');
    expect(resolve('packages/polaris-dossier/src/cli.ts', './argv.js')).toBe('packages/polaris-dossier/src/argv.ts');
    expect(resolve('apps/syzygy/src/main.ts', '@syzygy/polaris-dossier')).toBe(BARREL);
    expect(resolve('apps/syzygy/src/main.ts', 'node:fs')).toBeNull();
    expect(resolve('apps/syzygy/src/main.ts', 'typescript')).toBeNull();
  });

  it.each([
    ['an absolute path to the barrel', join(ROOT, BARREL)],
    ['a file: URL of the barrel', pathToFileURL(join(ROOT, BARREL)).href],
    ['a FILE: URL of the barrel', pathToFileURL(join(ROOT, BARREL)).href.replace(/^file:/u, 'FILE:')],
    ['a # alias its package does not declare', '#dossier'],
  ])('reads %s as naming no module', (_form, specifier) => {
    expect(resolve('apps/syzygy/src/main.ts', specifier)).toBeUndefined();
  });

  it.each([
    ['a package by name', { '#lib': '@syzygy/lib' }, 'packages/lib/src/index.ts'],
    ['a subpath by name', { '#argv': '@syzygy/lib/argv' }, 'packages/lib/src/argv.ts'],
    ['a module of its own package', { '#lib': './dist/local.js' }, 'apps/app/src/local.ts'],
    ['agreeing conditions', { '#lib': { types: './dist/local.d.ts', import: './dist/local.js', default: './dist/local.js' } }, 'apps/app/src/local.ts'],
  ])('follows a # alias its package declares for %s', (_form, imports, module) => {
    expect(resolveIn(workspace(imports), 'apps/app/src/main.ts', Object.keys(imports)[0]!)).toBe(module);
  });

  it.each([
    ['from a module of another package', { '#lib': '@syzygy/lib' }, 'packages/lib/src/argv.ts', '#lib'],
    ['whose target is another alias', { '#lib': '#other', '#other': '@syzygy/lib' }, 'apps/app/src/main.ts', '#lib'],
    ['whose target leaves its package', { '#lib': '../lib/dist/index.js' }, 'apps/app/src/main.ts', '#lib'],
    ['whose target is an absolute path', { '#lib': '/packages/lib/src/index.ts' }, 'apps/app/src/main.ts', '#lib'],
    ['whose conditions disagree', { '#lib': { node: '@syzygy/lib', import: './dist/local.js' } }, 'apps/app/src/main.ts', '#lib'],
    ['under a name its package does not declare', { '#lib': '@syzygy/lib' }, 'apps/app/src/main.ts', '#other'],
  ])('reads a # alias %s as naming no module', (_form, imports, from, specifier) => {
    expect(resolveIn(workspace(imports), from, specifier)).toBeUndefined();
  });

  it.each([
    ['node', { types: './dist/index.d.ts', node: './dist/index.js', import: './dist/argv.js' }],
    ['module-sync', { 'module-sync': './dist/index.js', import: './dist/argv.js' }],
    ['require', { import: './dist/argv.js', require: './dist/index.js' }],
    ['default', { import: './dist/argv.js', default: './dist/index.js' }],
    ['a nested', { import: { types: './dist/argv.d.ts', default: './dist/argv.js' } }],
  ])('reads an export whose %s condition names another target as naming no module', (_condition, dot) => {
    expect(resolveIn(workspace({}, dot), 'apps/app/src/main.ts', '@syzygy/lib')).toBeUndefined();
  });

  it('resolves an export whose conditions other than types all name one target', () => {
    expect(resolveIn(workspace({}, { types: './dist/argv.d.ts', import: './dist/argv.js', default: './dist/argv.js' }), 'apps/app/src/main.ts', '@syzygy/lib'))
      .toBe('packages/lib/src/argv.ts');
  });
});
