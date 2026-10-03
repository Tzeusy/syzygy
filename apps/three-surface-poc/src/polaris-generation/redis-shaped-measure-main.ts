import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { measureRedisShapedDiscovery } from './redis-shaped-measure.js';

/** `poc:redis-shaped-discovery [--out <file>]`: builds the synthetic fixture in a scratch directory, measures heuristic discovery, prints or writes the measurement. No real repository is read and no provider is called. */
export async function main(argv: readonly string[]): Promise<number> {
  const outAt = argv.indexOf('--out');
  if (argv.length !== 0 && !(argv.length === 2 && outAt === 0 && argv[1]! !== '')) { process.stderr.write('Usage: poc:redis-shaped-discovery [--out <file>]\n'); return 2; }
  const scratch = mkdtempSync(join(tmpdir(), 'syzygy-redis-shaped-'));
  try {
    const { measurement } = await measureRedisShapedDiscovery(join(scratch, 'repo'));
    const text = `${JSON.stringify(measurement, null, 2)}\n`;
    if (outAt === 0) writeFileSync(resolve(argv[1]!), text, { flag: 'wx' }); else process.stdout.write(text);
    return 0;
  } finally { rmSync(scratch, { recursive: true, force: true }); }
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main(process.argv.slice(2)).then(code => { process.exitCode = code; }, error => { process.stderr.write(`redis-shaped discovery failed: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; });
}
