import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { join, posix } from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';

// syzygy-bpyt.8.1: the `syzygy` CLI never loads the parked provider island
// (parked, not deleted: owner packet Q8). Reachability is computed here, from
// the CLI entry, over every import edge TypeScript's preprocessor reports:
// static, type-only, re-export and dynamic with a literal specifier. An
// `@syzygy/*` specifier resolves through its package's `exports`, where
// `./dist/X.js` is `src/X.ts`. Nothing lists the reachable modules by hand;
// only the island is listed.

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const ENTRY = 'apps/syzygy/src/main.ts';
const ISLAND = [
  'packages/polaris-generation-core/src/admitted-input.ts',
  'packages/polaris-generation-core/src/discovery-provider.ts',
  'packages/polaris-generation-core/src/discovery.ts',
  'packages/polaris-generation-core/src/excerpt.ts',
  'packages/polaris-generation-core/src/pipeline.ts',
  'packages/polaris-generation-core/src/provider-draft.ts',
  'packages/polaris-generation-core/src/rendered-design.ts',
  'apps/three-surface-poc/src/polaris-generation/dossier-trigger.ts',
  'apps/three-surface-poc/src/polaris-generation/durable-lifecycle.ts',
  'apps/three-surface-poc/src/polaris-generation/generation-mutation-run-main.ts',
  'apps/three-surface-poc/src/polaris-generation/generation-mutation.ts',
  'apps/three-surface-poc/src/polaris-generation/pipeline-demo-main.ts',
  'apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts',
  'apps/three-surface-poc/src/polaris-generation/redis-shaped-fixture.ts',
  'apps/three-surface-poc/src/polaris-generation/redis-shaped-measure-main.ts',
  'apps/three-surface-poc/src/polaris-generation/redis-shaped-measure.ts',
  'apps/three-surface-poc/src/polaris-generation/repo-corpus-main.ts',
  'apps/three-surface-poc/src/polaris-generation/repo-corpus.ts',
  'apps/three-surface-poc/src/polaris-generation/self-corpus-main.ts',
  'apps/three-surface-poc/src/polaris-generation/self-corpus.ts',
];
// Reached, and its imports not followed. consent-ports.ts is parked egress
// code (owner packet Q8): it takes pipeline types and `digestCanonicalJson`
// from this package's root, which re-exports the island. The consent barrel
// re-exports it and package-reader.ts imports two of its helpers, and the
// screen and the gate sources reach both. Neither file is this bead's to
// change (package-reader.ts is syzygy-bpyt.8.4's), so the edge stands as a
// named residual; the last test fails once it no longer reaches the island.
const UNFOLLOWED = ['packages/polaris-generation-consent/src/consent-ports.ts'];

interface Edge { readonly from: string; readonly specifier: string; readonly to: string }

const isFile = (path: string): boolean => existsSync(join(ROOT, path)) && statSync(join(ROOT, path)).isFile();
const manifests = new Map<string, { dir: string; exports?: Record<string, unknown>; main?: string }>();
for (const parent of ['apps', 'packages']) {
  for (const name of readdirSync(join(ROOT, parent))) {
    const path = `${parent}/${name}/package.json`;
    if (!isFile(path)) continue;
    const manifest = JSON.parse(readFileSync(join(ROOT, path), 'utf8')) as { name: string; exports?: Record<string, unknown>; main?: string };
    manifests.set(manifest.name, { dir: `${parent}/${name}`, ...manifest });
  }
}

/** The module a specifier names, null for one outside the workspace (`node:*`, a dependency), or undefined when it names none. */
function resolve(from: string, specifier: string): string | null | undefined {
  if (specifier.startsWith('.')) {
    const base = posix.normalize(posix.join(posix.dirname(from), specifier));
    return [base.replace(/\.js$/u, '.ts'), `${base}.ts`, `${base}/index.ts`].find(isFile);
  }
  const named = /^(@syzygy\/[^/]+)(\/.*)?$/u.exec(specifier);
  if (named === null) return null;
  const manifest = manifests.get(named[1]!);
  if (manifest === undefined) return undefined;
  const subpath = named[2] === undefined ? '.' : `.${named[2]}`;
  let target = manifest.exports === undefined ? (subpath === '.' ? manifest.main : undefined) : manifest.exports[subpath];
  if (typeof target === 'object' && target !== null) target = (target as { import?: unknown; default?: unknown }).import ?? (target as { default?: unknown }).default;
  if (typeof target !== 'string' || !target.startsWith('./dist/')) return undefined;
  const module = posix.join(manifest.dir, target.replace(/^\.\/dist\//u, 'src/').replace(/\.js$/u, '.ts'));
  return isFile(module) ? module : undefined;
}

/** Every module the entry reaches, the edges from them into the island, and any workspace specifier that names no module. */
function reach(unfollowed: readonly string[]): { reachable: string[]; intoIsland: Edge[]; unresolved: Omit<Edge, 'to'>[] } {
  const island = new Set(ISLAND);
  const seen = new Set([ENTRY]);
  const queue = [ENTRY];
  const intoIsland: Edge[] = [];
  const unresolved: Omit<Edge, 'to'>[] = [];
  for (let file = queue.shift(); file !== undefined; file = queue.shift()) {
    if (unfollowed.includes(file)) continue;
    for (const { fileName: specifier } of ts.preProcessFile(readFileSync(join(ROOT, file), 'utf8'), true, true).importedFiles) {
      const to = resolve(file, specifier);
      if (to === null) continue;
      if (to === undefined) { unresolved.push({ from: file, specifier }); continue; }
      if (island.has(to) && !island.has(file)) intoIsland.push({ from: file, specifier, to });
      if (!seen.has(to)) { seen.add(to); queue.push(to); }
    }
  }
  return { reachable: [...seen].sort(), intoIsland, unresolved };
}

describe('the syzygy CLI and the parked provider island', () => {
  it('lists twenty island modules, each a file in the tree', () => {
    expect(new Set(ISLAND).size).toBe(20);
    expect(ISLAND.filter(path => !isFile(path))).toEqual([]);
  });

  it('resolves every workspace import the CLI reaches, dynamic ones included', () => {
    const { reachable, unresolved } = reach(UNFOLLOWED);
    expect(unresolved).toEqual([]);
    expect(reachable).toContain('apps/three-surface-poc/src/polaris-generation/dossier-site.ts');
    expect(reachable).toContain(UNFOLLOWED[0]);
  });

  it('reaches no island module from the CLI entry', () => {
    const { reachable, intoIsland } = reach(UNFOLLOWED);
    expect(intoIsland).toEqual([]);
    expect(reachable.filter(path => ISLAND.includes(path))).toEqual([]);
  });

  it('follows every edge but one, and that one still reaches the island', () => {
    const { intoIsland } = reach([]);
    expect(intoIsland.length).toBeGreaterThan(0);
  });
});
