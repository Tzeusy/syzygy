import { readFileSync, realpathSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { CorpusRefusal, parseReaderConfig, readRepoCorpus, refusingAdmission, type CorpusAdmissionPort } from './repo-corpus.js';

const USAGE = 'Usage: repo-corpus-main --repo <checkout> --config <file.json> [--revision <commit>] [--repository-id <id>] [--include <glob>]... [--exclude <glob>]...\n';

/** Prints the corpus accounting (never a body). The admission port defaults
 * to refusing; a later lane injects one backed by consent records. */
export async function main(argv: readonly string[], admission: CorpusAdmissionPort = refusingAdmission): Promise<number> {
  const flags = new Map<string, string[]>();
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i], value = argv[i + 1];
    if (!key || !['--repo', '--config', '--revision', '--repository-id', '--include', '--exclude'].includes(key) || !value) { process.stderr.write(USAGE); return 2; }
    flags.set(key, [...(flags.get(key) ?? []), value]);
  }
  const one = (key: string): string | undefined => flags.get(key)?.[0];
  if (!one('--repo') || !one('--config')) { process.stderr.write(USAGE); return 2; }
  try {
    const config = parseReaderConfig(readFileSync(one('--config')!, 'utf8'), {
      ...(one('--revision') ? { revision: one('--revision')! } : {}), ...(one('--repository-id') ? { repositoryId: one('--repository-id')! } : {}),
      include: flags.get('--include') ?? [], exclude: flags.get('--exclude') ?? [] });
    const corpus = await readRepoCorpus(realpathSync(resolve(one('--repo')!)), config, { admission });
    process.stdout.write(`${JSON.stringify({ repositoryId: corpus.repositoryId, revision: corpus.revision, count: corpus.count,
      sources: corpus.sources.length, rawBytes: corpus.rawBytes, identityDigest: corpus.identityDigest, realProviderCalls: 0 }, null, 2)}\n`);
    return 0;
  } catch (error) {
    process.stderr.write(`${error instanceof CorpusRefusal ? error.message : `Corpus reader failed: ${error instanceof Error ? error.message : 'unknown'}`}\n`);
    return 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main(process.argv.slice(2)).then(code => { process.exitCode = code; });
}
