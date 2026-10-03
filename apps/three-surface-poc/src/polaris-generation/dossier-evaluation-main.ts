import { lstat, readFile, realpath, writeFile } from 'node:fs/promises';
import { resolve, sep } from 'node:path';
import { pathToFileURL } from 'node:url';

import {
  evaluateDossier, parseBoundedJson, parseDossierManifest, parsePageBudget, scriptedAnswers,
  type GenerationSource, type ReaderAnswer,
} from '@syzygy/polaris-generation-core';

/** Each dossier page and the sources file are bounded before parsing. */
const MAX_PAGE_BYTES = 8_000_000;
const SOURCES_LIMITS = { maxBytes: 64_000_000, maxNodes: 2_000_000, maxDepth: 16 } as const;
const ANSWERS_LIMITS = { maxBytes: 4_000_000, maxNodes: 200_000, maxDepth: 16 } as const;

export interface DossierEvaluationArgs {
  readonly dossier: string;
  readonly sources: string;
  readonly questions: string;
  readonly expectQuestionsSha256?: string;
  readonly budget?: string;
  /** Scripted answers only (`polaris-scripted-answers-v1`); no provider call exists here. */
  readonly answers?: string;
}

/** Reads one page, refusing a symlink or any path that resolves outside the run directory. */
async function readContained(root: string, relative: string): Promise<Uint8Array> {
  const path = resolve(root, relative);
  if ((await lstat(path)).isSymbolicLink()) throw new Error('page-is-symlink');
  const real = await realpath(path);
  if (!real.startsWith(root + sep)) throw new Error('page-outside-run-directory');
  const bytes = await readFile(real);
  if (bytes.length > MAX_PAGE_BYTES) throw new Error('page-too-large');
  return bytes;
}

export async function evaluateDossierDirectory(args: DossierEvaluationArgs, signal: AbortSignal) {
  const root = await realpath(resolve(args.dossier));
  const manifestText = new TextDecoder('utf-8', { fatal: true }).decode(await readContained(root, 'dossier.json'));
  const manifest = parseDossierManifest(manifestText);
  const pages = new Map<string, Uint8Array>();
  for (const page of manifest.pages) pages.set(page.path, await readContained(root, page.path));
  const sources = parseBoundedJson(await readFile(resolve(args.sources), 'utf8'), SOURCES_LIMITS) as GenerationSource[];
  if (!Array.isArray(sources)) throw new Error('sources-not-an-array');
  let answer;
  if (args.answers !== undefined) {
    const script = parseBoundedJson(await readFile(resolve(args.answers), 'utf8'), ANSWERS_LIMITS) as { format?: unknown; answers?: Record<string, ReaderAnswer> };
    if (script?.format !== 'polaris-scripted-answers-v1' || script.answers === null || typeof script.answers !== 'object') throw new Error('invalid-scripted-answers');
    answer = scriptedAnswers(script.answers);
  }
  return evaluateDossier({
    manifestText,
    pages,
    sources,
    questionsText: await readFile(resolve(args.questions), 'utf8'),
    ...(args.expectQuestionsSha256 === undefined ? {} : { expectedQuestionsSha256: args.expectQuestionsSha256 }),
    ...(args.budget === undefined ? {} : { budget: parsePageBudget(await readFile(resolve(args.budget), 'utf8')) }),
    ...(answer === undefined ? {} : { answer }),
  }, signal);
}

const USAGE = 'Usage: dossier-evaluation-main --dossier <run-dir> --sources <sources.json> --questions <questions.json> [--expect-questions-sha256 <hex>] [--budget <budget.json>] [--answers <scripted-answers.json>] [--out <new-report.json>]\n';
const FLAGS: Record<string, keyof DossierEvaluationArgs | 'out'> = {
  '--dossier': 'dossier', '--sources': 'sources', '--questions': 'questions', '--expect-questions-sha256': 'expectQuestionsSha256',
  '--budget': 'budget', '--answers': 'answers', '--out': 'out',
};

export function parseArgs(argv: readonly string[]): (DossierEvaluationArgs & { readonly out?: string }) | null {
  const out: Record<string, string> = {};
  for (let i = 0; i < argv.length; i += 2) {
    const key = FLAGS[argv[i]!];
    const value = argv[i + 1];
    if (key === undefined || value === undefined || value.startsWith('--') || key in out) return null;
    out[key] = value;
  }
  return out.dossier && out.sources && out.questions ? out as unknown as DossierEvaluationArgs & { out?: string } : null;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const args = parseArgs(process.argv.slice(2));
  if (args === null) {
    process.stderr.write(USAGE);
    process.exitCode = 2;
  } else {
    evaluateDossierDirectory(args, new AbortController().signal).then(
      async report => {
        const json = `${JSON.stringify(report, null, 2)}\n`;
        if (args.out === undefined) process.stdout.write(json);
        else await writeFile(resolve(args.out), json, { flag: 'wx' });
      },
      error => { process.stderr.write(`Dossier evaluation refused: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; },
    );
  }
}
