import { spawnSync } from 'node:child_process';
import { lstat, mkdir, mkdtemp, readFile, realpath, rename, rm, writeFile } from 'node:fs/promises';
import { basename, dirname, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { isDossierPagePath, parseBoundedJson, type GenerationSource, type OwnerTopic, type PipelineResult } from '@syzygy/polaris-generation-core';
import { renderDossier } from './dossier-render.js';

const RUN_LIMITS = { maxBytes: 64_000_000, maxNodes: 2_000_000, maxDepth: 64 } as const;

/**
 * Passes only when Git itself says `directory` is not in a repository. Any
 * other result — inside a work tree, inside a `.git` directory, Git missing,
 * a dubious-ownership refusal, any other error — refuses (fail closed). Git
 * runs with no user or system configuration and none of the caller's `GIT_*`
 * variables, so neither can point it elsewhere.
 */
function assertOutsideGit(directory: string, path: string | undefined): void {
  const result = spawnSync('git', ['-C', directory, 'rev-parse', '--is-inside-work-tree'], {
    encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'],
    env: { PATH: path ?? '', LC_ALL: 'C', GIT_CONFIG_GLOBAL: '/dev/null', GIT_CONFIG_NOSYSTEM: '1' },
  });
  if (result.error !== undefined) throw new Error('git-unavailable');
  if (result.status === 128 && /^fatal: not a git repository/mu.test(result.stderr)) return;
  throw new Error('run-directory-inside-git-work-tree');
}

/**
 * Writes a rendered dossier into a new run directory. The parent must exist;
 * it is resolved through every symlink, and the real parent must lie outside
 * every Git work tree (generated drafts are run output, never tracked files).
 * The directory itself must not exist. Every file is written into a fresh
 * sibling temporary directory, which is renamed into place only when all of
 * them are written, so a refused or failed write leaves no run directory.
 * Returns the real path written, which is the path that was checked.
 * Limit: `git rev-parse` stops searching at a filesystem boundary (the
 * cleared environment leaves GIT_DISCOVERY_ACROSS_FILESYSTEM unset), so a
 * parent on a separate mount inside a work tree reads as outside Git.
 */
export async function writeDossierRun(destination: string, files: ReadonlyMap<string, string>, env: { readonly PATH?: string } = process.env): Promise<string> {
  for (const path of files.keys()) if (!isDossierPagePath(path)) throw new Error('invalid-output-path');
  const parent = await realpath(dirname(resolve(destination)));
  assertOutsideGit(parent, env.PATH);
  const target = join(parent, basename(resolve(destination)));
  const absent = async (): Promise<void> => {
    if (await lstat(target).then(() => true, (error: NodeJS.ErrnoException) => { if (error.code === 'ENOENT') return false; throw error; })) throw new Error('run-directory-exists');
  };
  await absent();
  const staging = await mkdtemp(join(parent, `.${basename(target)}.partial-`));
  try {
    for (const [path, content] of files) {
      const file = join(staging, path);
      await mkdir(dirname(file), { recursive: true });
      await writeFile(file, content, { flag: 'wx' });
    }
    // rename() would replace an empty directory created since the first check.
    await absent();
    await rename(staging, target);
    return target;
  } catch (error) {
    await rm(staging, { recursive: true, force: true });
    throw error;
  }
}

/** Reads a pipeline run record (`{ result, sources }`, as the synthetic demo writes it) and an optional topic map. */
export async function renderDossierRun(runFile: string, out: string, topicsFile?: string): Promise<string> {
  const run = parseBoundedJson(await readFile(resolve(runFile), 'utf8'), RUN_LIMITS) as { result?: PipelineResult; sources?: GenerationSource[] };
  if (run === null || typeof run !== 'object' || run.result === undefined || !Array.isArray(run.sources)) throw new Error('invalid-run-record');
  const topics = topicsFile === undefined ? undefined
    : parseBoundedJson(await readFile(resolve(topicsFile), 'utf8'), RUN_LIMITS) as Record<string, OwnerTopic[]>;
  const rendered = renderDossier({ result: run.result, sources: run.sources, ...(topics === undefined ? {} : { topics }) });
  return writeDossierRun(out, rendered.files);
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const args = process.argv.slice(2);
  const valid = (args.length === 4 || args.length === 6) && args[0] === '--run' && args[2] === '--out' && (args.length === 4 || args[4] === '--topics')
    && args.every((arg, index) => index % 2 === 0 || (arg !== '' && !arg.startsWith('--')));
  if (!valid) {
    process.stderr.write('Usage: dossier-render-main --run <pipeline-run.json> --out <new-run-directory-outside-git> [--topics <topics.json>]\n');
    process.exitCode = 2;
  } else {
    renderDossierRun(args[1]!, args[3]!, args[5]).then(
      written => process.stdout.write(`Wrote the dossier to ${written}. It is an unreviewed editorial draft.\n`),
      error => { process.stderr.write(`Dossier render refused: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; },
    );
  }
}
