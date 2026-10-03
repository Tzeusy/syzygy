import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { renderDossier } from './dossier-render.js';
import { formatOutcome, gitMaterialize, runDossierTrigger, type TriggerPorts } from './dossier-trigger.js';

const EXIT: Record<string, number> = { complete: 0, 'invalid-input': 2, 'unresolved-revision': 4, 'admission-missing': 3, 'generation-unavailable': 5, 'generation-stopped': 6 };

/** `poc:dossier -- <github-url> [--out <dir>] [--json]`. */
export async function main(argv: readonly string[], ports: TriggerPorts = {}): Promise<number> {
  const args = [...argv];
  const json = args.includes('--json');
  const flagless = args.filter(arg => arg !== '--json');
  const outAt = flagless.indexOf('--out');
  const out = outAt >= 0 ? flagless[outAt + 1] : undefined;
  const positional = flagless.filter((arg, i) => !(outAt >= 0 && (i === outAt || i === outAt + 1)));
  if (positional.length !== 1 || (outAt >= 0 && !out)) { process.stderr.write('Usage: poc:dossier -- <https://github.com/owner/repo[/tree/ref]> [--out <dir>] [--json]\n'); return 2; }
  const outcome = await runDossierTrigger(positional[0]!, { materialize: gitMaterialize, render: ({ result, sources }) => renderDossier({ result, sources }), ...ports, ...(out ? { outDir: resolve(out) } : {}) });
  process.stdout.write(json ? `${JSON.stringify(outcome, null, 2)}\n` : formatOutcome(outcome));
  return EXIT[outcome.state] ?? 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main(process.argv.slice(2)).then(code => { process.exitCode = code; }, error => { process.stderr.write(`dossier trigger failed: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; });
}
