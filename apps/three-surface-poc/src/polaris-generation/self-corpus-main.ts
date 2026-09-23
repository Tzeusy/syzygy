import { realpathSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { proveSelfCorpus } from './self-corpus.js';

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const args = process.argv.slice(2);
  if (args.length !== 4 || args[0] !== '--repo' || args[2] !== '--revision' || !args[1] || !args[3]) {
    process.stderr.write('Usage: self-corpus-main --repo <Syzygy-checkout> --revision <pinned-commit>\n');
    process.exitCode = 2;
  } else {
    proveSelfCorpus(realpathSync(resolve(args[1])), args[3]).then(
      report => process.stdout.write(`${JSON.stringify(report, null, 2)}\n`),
      error => { process.stderr.write(`Synthetic self-corpus proof refused: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; },
    );
  }
}
