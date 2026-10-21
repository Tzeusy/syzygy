/** Test support: replace one `node:fs` function for every module that imports `node:fs`, then restore it. A module's namespace import
 * reads the CommonJS module's bindings, which `syncBuiltinESMExports` refreshes, so a replacement installed there is what the code under
 * test calls (R-GP-IMPL-LAUNCHED-MARKER-2, R2-N1 and R2-N4). */
import * as fs from 'node:fs';
import { createRequire, syncBuiltinESMExports } from 'node:module';
import * as path from 'node:path';

interface Patchable {
  openSync: typeof fs.openSync;
  fstatSync: typeof fs.fstatSync;
  readSync: typeof fs.readSync;
}

const cjsFs = createRequire(import.meta.url)('node:fs') as Patchable;

/** Install `replace(original)` as `node:fs`'s `name`; the returned function puts the original back. */
export function patchFs<K extends keyof Patchable>(name: K, replace: (original: Patchable[K]) => Patchable[K]): () => void {
  const original = cjsFs[name];
  cjsFs[name] = replace(original);
  syncBuiltinESMExports();
  return () => {
    cjsFs[name] = original;
    syncBuiltinESMExports();
  };
}

/** How many times `act` opens `file` through `fs.openSync`, counting opens that fail. */
export async function opensOf(file: string, act: () => Promise<unknown>): Promise<number> {
  let opens = 0;
  const restore = patchFs('openSync', (openSync) => ((target: fs.PathLike, ...rest: unknown[]) => {
    if (path.resolve(String(target)) === path.resolve(file)) opens += 1;
    return (openSync as (...args: unknown[]) => number)(target, ...rest);
  }) as typeof fs.openSync);
  try {
    await act();
  } finally {
    restore();
  }
  return opens;
}
