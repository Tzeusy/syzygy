// Build TypeScript projects from nothing, so no output the build did not just write survives it (syzygy-bpyt.4.2). `tsc -b`
// alone keeps an output whose source is unchanged, however its bytes were altered since, and an output whose source is gone;
// `--force` rewrites the first and keeps the second. This removes the dist of every project `tsc -b` builds for the given ones
// (each named project and every project its tsconfig.json references, transitively), where each keeps its outputs and its
// incremental state, then runs `tsc -b` over them. A project it cannot read that way is refused before anything is removed.
//
// Usage, from the repository root: node scripts/clean_build.mjs <project directory>...
import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync, rmSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join, posix } from 'node:path';

const projects = process.argv.slice(2).map((project) => posix.normalize(project));
if (projects.length === 0) throw new Error('usage: node scripts/clean_build.mjs <project directory>...');

const built = new Set();
function visit(project) {
  if (built.has(project)) return;
  const path = join(project, 'tsconfig.json');
  if (!/^(?:apps|packages)\/[^/]+$/u.test(project) || !existsSync(path)) throw new Error(`${project}: not a workspace project with a tsconfig.json`);
  const config = JSON.parse(readFileSync(path, 'utf8'));
  if (config.compilerOptions?.outDir !== 'dist' || config.compilerOptions?.tsBuildInfoFile !== 'dist/.tsbuildinfo') {
    throw new Error(`${path}: its outputs and incremental state are not both under dist`);
  }
  built.add(project);
  for (const reference of config.references ?? []) visit(posix.normalize(posix.join(project, reference.path)));
}
for (const project of projects) visit(project);

for (const project of built) rmSync(join(project, 'dist'), { recursive: true, force: true });
const tsc = createRequire(import.meta.url).resolve('typescript/bin/tsc');
process.exitCode = spawnSync(process.execPath, [tsc, '-b', ...projects], { stdio: 'inherit' }).status ?? 1;
