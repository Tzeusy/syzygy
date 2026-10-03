import { execFileSync } from 'node:child_process';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { isDossierPagePath, parseBoundedJson, type GenerationSource, type OwnerTopic, type PipelineResult } from '@syzygy/polaris-generation-core';
import { renderDossier } from './dossier-render.js';

const RUN_LIMITS = { maxBytes: 64_000_000, maxNodes: 2_000_000, maxDepth: 64 } as const;

/** True when `directory` lies inside a Git work tree. */
function insideGitWorkTree(directory: string): boolean {
  try {
    return execFileSync('git', ['-C', directory, 'rev-parse', '--is-inside-work-tree'], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim() === 'true';
  } catch {
    return false;
  }
}

/**
 * Writes a rendered dossier into a new run directory. The parent must exist and
 * lie outside every Git work tree (generated drafts are run output, never
 * tracked files); the directory itself must not exist, and no file is
 * overwritten.
 */
export async function writeDossierRun(destination: string, files: ReadonlyMap<string, string>): Promise<void> {
  const target = resolve(destination);
  if (insideGitWorkTree(dirname(target))) throw new Error('run-directory-inside-git-work-tree');
  await mkdir(target);
  for (const [path, content] of files) {
    if (!isDossierPagePath(path)) throw new Error('invalid-output-path');
    const file = join(target, path);
    await mkdir(dirname(file), { recursive: true });
    await writeFile(file, content, { flag: 'wx' });
  }
}

/** Reads a pipeline run record (`{ result, sources }`, as the synthetic demo writes it) and an optional topic map. */
export async function renderDossierRun(runFile: string, out: string, topicsFile?: string): Promise<void> {
  const run = parseBoundedJson(await readFile(resolve(runFile), 'utf8'), RUN_LIMITS) as { result?: PipelineResult; sources?: GenerationSource[] };
  if (run === null || typeof run !== 'object' || run.result === undefined || !Array.isArray(run.sources)) throw new Error('invalid-run-record');
  const topics = topicsFile === undefined ? undefined
    : parseBoundedJson(await readFile(resolve(topicsFile), 'utf8'), RUN_LIMITS) as Record<string, OwnerTopic[]>;
  const rendered = renderDossier({ result: run.result, sources: run.sources, ...(topics === undefined ? {} : { topics }) });
  await writeDossierRun(out, rendered.files);
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
      () => process.stdout.write(`Wrote the dossier to ${resolve(args[3]!)}. It is an unreviewed editorial draft.\n`),
      error => { process.stderr.write(`Dossier render refused: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; },
    );
  }
}
