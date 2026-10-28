import { join, relative, sep } from 'node:path';
import { pathToFileURL } from 'node:url';
import { describe, expect, it } from 'vitest';
import { ROOT, entryModules } from './workspace-reach.testkit.js';

// syzygy-bpyt.46 (the PR 545 round-1 review's item 3): the root vitest.config.ts maps workspace specifiers to source modules by hand,
// so a test that imports one runs the module the map names, not necessarily the one Node loads. Each alias is pinned here to the src
// module its package's own entry names (`entryModules`, which the S10 no-egress bundle also aliases by), and the entries the map leaves
// out, which a test then loads from the package's built dist through node_modules, are a literal list.
const CONFIG = (await import(pathToFileURL(join(ROOT, 'vitest.config.ts')).href)) as { default: { resolve: { alias: Record<string, string> } } };
const ALIASES = Object.fromEntries(Object.entries(CONFIG.default.resolve.alias).map(([specifier, target]) => [specifier, relative(ROOT, target).split(sep).join('/')]));

describe('the root vitest.config.ts aliases', () => {
  it("alias each specifier to the src module its package's entry names", () => {
    const entries = entryModules();
    expect(Object.fromEntries(Object.keys(ALIASES).map((specifier) => [specifier, entries[specifier]]))).toEqual(ALIASES);
  });

  it('leave exactly these entries to their built dist', () => {
    expect(Object.keys(entryModules()).filter((specifier) => !(specifier in ALIASES)).sort()).toEqual([
      '@syzygy/app', '@syzygy/polaris-dossier/argv', '@syzygy/polaris-dossier/state-directory', '@syzygy/three-surface-poc-app',
      '@syzygy/three-surface-poc-app/dossier-render', '@syzygy/three-surface-poc-app/dossier-site',
    ]);
  });
});
