import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { join, posix } from 'node:path';
import { fileURLToPath } from 'node:url';

// Test support: which workspace modules an entry reaches, for the guards that keep a module off a path the `syzygy` CLI takes
// (island-boundary.test.ts, syzygy-bpyt.8.1, and polaris-dossier's subpath-imports.test.ts, syzygy-bpyt.8.34). An `@syzygy/*`
// specifier resolves through its package's `exports`, where `./dist/X.js` is `src/X.ts`. Each guard says which edges a module has.

export const ROOT = fileURLToPath(new URL('../../../', import.meta.url));

export interface ReachEdge { readonly from: string; readonly specifier: string; readonly to: string }

export const isFile = (path: string): boolean => existsSync(join(ROOT, path)) && statSync(join(ROOT, path)).isFile();
export const readModule = (path: string): string => readFileSync(join(ROOT, path), 'utf8');

const manifests = new Map<string, { dir: string; exports?: Record<string, unknown>; main?: string }>();
for (const parent of ['apps', 'packages']) {
  for (const name of readdirSync(join(ROOT, parent))) {
    const path = `${parent}/${name}/package.json`;
    if (!isFile(path)) continue;
    const manifest = JSON.parse(readModule(path)) as { name: string; exports?: Record<string, unknown>; main?: string };
    manifests.set(manifest.name, { dir: `${parent}/${name}`, ...manifest });
  }
}

/** The module a specifier names, null for one outside the workspace (`node:*`, a dependency), or undefined when it names none. */
export function resolve(from: string, specifier: string): string | null | undefined {
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

/** Every module `entry` reaches by the specifiers `specifiersOf` gives for each module, in the order it reaches them: every edge
 * between workspace modules, and any workspace specifier that names no module. */
export function reach(entry: string, specifiersOf: (module: string) => readonly string[]): { reachable: string[]; edges: ReachEdge[]; unresolved: Omit<ReachEdge, 'to'>[] } {
  const seen = new Set([entry]);
  const queue = [entry];
  const edges: ReachEdge[] = [];
  const unresolved: Omit<ReachEdge, 'to'>[] = [];
  for (let file = queue.shift(); file !== undefined; file = queue.shift()) {
    for (const specifier of specifiersOf(file)) {
      const to = resolve(file, specifier);
      if (to === null) continue;
      if (to === undefined) { unresolved.push({ from: file, specifier }); continue; }
      edges.push({ from: file, specifier, to });
      if (!seen.has(to)) { seen.add(to); queue.push(to); }
    }
  }
  return { reachable: [...seen].sort(), edges, unresolved };
}
