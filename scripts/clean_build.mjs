// Build TypeScript projects from nothing, so no output the build did not just write survives it (syzygy-bpyt.4.2). `tsc -b`
// alone keeps an output whose source is unchanged, however its bytes were altered since, and an output whose source is gone;
// `--force` rewrites the first and keeps the second. This removes the dist of every project `tsc -b` builds for the given ones
// (each named project and every project its tsconfig.json references, transitively), then runs `tsc -b` over them. Before it
// removes anything it refuses a project outside apps/* or packages/*, one with no tsconfig.json, one whose directory resolves
// outside the checkout, a tsconfig.json that is not plain JSON, one whose own compilerOptions do not set `outDir` `dist` and
// `tsBuildInfoFile` `dist/.tsbuildinfo` or that set `declarationDir` or `outFile`, and references that form a cycle. An option
// inherited through `extends` is not read.
//
// Usage, from the repository root: node scripts/clean_build.mjs <project directory>...
import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync, realpathSync, rmSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join, posix } from 'node:path';

const projects = process.argv.slice(2).map((project) => posix.normalize(project));
if (projects.length === 0) throw new Error('usage: node scripts/clean_build.mjs <project directory>...');

const built = new Set();
const visiting = [];
function visit(project) {
  if (built.has(project)) return;
  if (visiting.includes(project)) throw new Error(`${[...visiting, project].join(' -> ')}: project references form a cycle`);
  const path = join(project, 'tsconfig.json');
  if (!/^(?:apps|packages)\/[^/]+$/u.test(project) || !existsSync(path)) throw new Error(`${project}: not a workspace project with a tsconfig.json`);
  if (!realpathSync(project).startsWith(`${realpathSync('.')}/`)) throw new Error(`${project}: resolves outside the checkout`);
  let config;
  try { config = JSON.parse(readFileSync(path, 'utf8')); } catch { throw new Error(`${path}: not plain JSON`); }
  const options = config.compilerOptions ?? {};
  if (options.outDir !== 'dist' || options.tsBuildInfoFile !== 'dist/.tsbuildinfo' || 'declarationDir' in options || 'outFile' in options) {
    throw new Error(`${path}: its outputs and incremental state are not both under dist`);
  }
  visiting.push(project);
  for (const reference of config.references ?? []) visit(posix.normalize(posix.join(project, reference.path)));
  visiting.pop();
  built.add(project);
}
for (const project of projects) visit(project);

for (const project of built) rmSync(join(project, 'dist'), { recursive: true, force: true });
const tsc = createRequire(import.meta.url).resolve('typescript/bin/tsc');
process.exitCode = spawnSync(process.execPath, [tsc, '-b', ...projects], { stdio: 'inherit' }).status ?? 1;
