import { writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

import { SCENARIO_NAMES, formatRehearsal, rehearse } from './dossier-rehearsal.testkit.js';

const USAGE = `Usage: poc:dossier-rehearsal [-- [--scenario <name>]... [--report <file.json>] [--keep]]\nScenarios: ${SCENARIO_NAMES.join(', ')}\n`;

/** `poc:dossier-rehearsal`: exit 0 when every check of every selected scenario passes, 1 when any fails, 2 on bad arguments. Model-free and network-free. */
export async function main(argv: readonly string[], out: (text: string) => void = t => { process.stdout.write(t); }, err: (text: string) => void = t => { process.stderr.write(t); }): Promise<number> {
  const scenarios: string[] = [];
  let report: string | undefined, keep = false;
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i]!, value = argv[i + 1];
    if (arg === '--keep') { keep = true; continue; }
    if ((arg === '--scenario' || arg === '--report') && value !== undefined && !value.startsWith('--')) {
      if (arg === '--scenario') scenarios.push(value); else report = value;
      i++;
    } else { err(USAGE); return 2; }
  }
  if (scenarios.some(name => !SCENARIO_NAMES.includes(name))) { err(USAGE); return 2; }
  const result = await rehearse({ ...(scenarios.length === 0 ? {} : { scenarios }), ...(keep ? { keepScratch: (dir: string) => out(`Scratch space kept at ${dir}\n`) } : {}) });
  if (report !== undefined) writeFileSync(resolve(report), `${JSON.stringify(result, null, 2)}\n`);
  out(formatRehearsal(result));
  return result.passed ? 0 : 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main(process.argv.slice(2)).then(code => { process.exitCode = code; }, error => { process.stderr.write(`dossier rehearsal failed: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; });
}
