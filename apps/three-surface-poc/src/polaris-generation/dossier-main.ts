import { resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

import { DOSSIER_REQUESTED_ASSETS } from '@syzygy/polaris-generation-core';

import { DOSSIER_ROUTES, openGeneration, type DossierRoute, type ProviderFactory } from './dossier-generation.js';
import { renderDossier } from './dossier-render.js';
import { createWiredRecordsPort } from './dossier-records.js';
import { routeInForce } from './dossier-route-registry.js';
import { formatOutcome, gitMaterialize, runDossierTrigger, type TriggerPorts } from './dossier-trigger.js';

const EXIT: Record<string, number> = { complete: 0, 'invalid-input': 2, 'unresolved-revision': 4, 'admission-missing': 3, 'generation-unavailable': 5, 'generation-stopped': 6, 'generation-stopped-partial': 7 };
const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
/** The only place the provider credential is read. */
export const CREDENTIAL_VARIABLE = 'SYZYGY_POLARIS_PROVIDER_API_KEY';
const USAGE = 'Usage: poc:dossier -- <https://github.com/owner/repo[/tree/ref]> --route agent-sdk|messages-api [--out <dir>] [--json]\n';

/** Test seams. None can name an upstream: the provider factory receives the credential and the route and builds what it likes, and production's names exactly one origin. */
export interface MainDeps {
  readonly root?: string;
  readonly now?: () => number;
  readonly env?: Record<string, string | undefined>;
  readonly providerFactory?: ProviderFactory;
  readonly stdout?: (text: string) => void;
  readonly stderr?: (text: string) => void;
}

/** `poc:dossier -- <github-url> --route agent-sdk|messages-api [--out <dir>] [--json]`. The route has no default: the owner chooses it. */
export async function main(argv: readonly string[], ports: TriggerPorts = {}, deps: MainDeps = {}): Promise<number> {
  const env = deps.env ?? process.env;
  // Read once, then removed from the environment so no child process or later reader can inherit it.
  const apiKey = env[CREDENTIAL_VARIABLE];
  delete env[CREDENTIAL_VARIABLE];
  const out = deps.stdout ?? ((text: string) => { process.stdout.write(text); });
  const err = deps.stderr ?? ((text: string) => { process.stderr.write(text); });
  const root = deps.root ?? REPO_ROOT, now = deps.now ?? Date.now;

  let json = false, outDir: string | undefined, route: string | undefined;
  const positional: string[] = [];
  const args = [...argv];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i]!;
    if (arg === '--json') json = true;
    else if (arg === '--out' || arg === '--route') {
      const value = args[++i];
      if (value === undefined || value === '' || value.startsWith('--')) { err(USAGE); return 2; }
      if (arg === '--out') outDir = value; else route = value;
    } else if (arg.startsWith('--')) { err(USAGE); return 2; }
    else positional.push(arg);
  }
  if (positional.length !== 1) { err(USAGE); return 2; }
  if (route === undefined || !(DOSSIER_ROUTES as readonly string[]).includes(route)) { err(`The provider route must be chosen: --route agent-sdk or --route messages-api.\n${USAGE}`); return 2; }

  const records = ports.records ?? createWiredRecordsPort({ root, now });
  // Fail closed before any network use: the chosen route must be an adopted registry entry.
  const registered = await routeInForce(route as DossierRoute, { root, now });
  if (!registered.inForce) {
    out(json ? `${JSON.stringify({ state: 'generation-unavailable', detail: `route-not-in-force: ${registered.why}` }, null, 2)}\n` : `GENERATION-UNAVAILABLE: the provider route is not in force (${registered.why}). Nothing was fetched, read or sent.\n`);
    return EXIT['generation-unavailable']!;
  }

  // Production passes no ports, so generation is always the provider-backed session. A caller that injects its own pipeline (tests) replaces it whole.
  const generation = ports.runPipeline !== undefined || ports.openGeneration !== undefined ? {}
    : { openGeneration: openGeneration({ route: route as DossierRoute, apiKey: apiKey ?? '', root, now, ...(deps.providerFactory === undefined ? {} : { providerFactory: deps.providerFactory }) }) };
  const outcome = await runDossierTrigger(positional[0]!, {
    materialize: gitMaterialize, render: ({ result, sources }) => renderDossier({ result, sources, requestedAssets: DOSSIER_REQUESTED_ASSETS }),
    records, ...generation, now, ...ports, ...(outDir ? { outDir: resolve(outDir) } : {}),
  });
  out(json ? `${JSON.stringify(outcome, null, 2)}\n` : formatOutcome(outcome));
  return EXIT[outcome.state] ?? 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main(process.argv.slice(2)).then(code => { process.exitCode = code; }, error => { process.stderr.write(`dossier trigger failed: ${error instanceof Error ? error.message : 'unknown'}\n`); process.exitCode = 1; });
}
