import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import path from 'node:path';

import { DECISIONS_DIR } from '@syzygy/polaris-generation-consent';

import type { DossierRoute } from './dossier-generation.js';

/**
 * The provider execution route must be a registry entry the owner adopted: an
 * `adopt-registry-entry` act record whose digest is the SHA-256 of the entry
 * installed in the adapter-registry home. The two routes are substitutes
 * (RFC4-1): the Agent SDK entry, or the Messages API entry. A route with no
 * such record, a record that does not name the installed bytes, or a record
 * dated after now is not in force and the run does not start.
 */
const REGISTRY_HOME = '.syzygy/governance/declarations/adapter-registry';
const CANDIDATES = '.syzygy/governance/contracts/candidates';

interface RouteEntry { readonly actFile: string; readonly entryFile: string; readonly candidatePath: string }
export const ROUTE_ENTRIES: Readonly<Record<DossierRoute, RouteEntry>> = {
  'agent-sdk': { actFile: 'PUBLIC-ADMISSION-REGISTRY-PROVIDER-ROUTE-ACT.md', entryFile: 'POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json',
    candidatePath: `${CANDIDATES}/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json` },
  'messages-api': { actFile: 'PUBLIC-ADMISSION-REGISTRY-MESSAGES-API-ROUTE-ACT.md', entryFile: 'POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json',
    candidatePath: `${CANDIDATES}/provider-route-messages-api-entry/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json` },
};

export type RouteInForce = { readonly inForce: true; readonly record: string; readonly digest: string } | { readonly inForce: false; readonly why: string };
export interface RouteRegistryFs { readonly readFile: (file: string) => Promise<Buffer> }
const nodeFs: RouteRegistryFs = { readFile: file => readFile(file) };

const only = (text: string, re: RegExp): string | undefined => { const all = [...text.matchAll(re)]; return all.length === 1 ? all[0]![1] : undefined; };

export async function routeInForce(route: DossierRoute, options: { readonly root: string; readonly now: () => number; readonly fs?: RouteRegistryFs }): Promise<RouteInForce> {
  const fs = options.fs ?? nodeFs;
  const entry = ROUTE_ENTRIES[route];
  const none = (why: string): RouteInForce => ({ inForce: false, why: `${route}: ${why}` });
  let act: string, installed: Buffer;
  try { act = (await fs.readFile(path.join(options.root, DECISIONS_DIR, entry.actFile))).toString('utf8'); } catch { return none(`no owner act record ${entry.actFile}`); }
  try { installed = await fs.readFile(path.join(options.root, REGISTRY_HOME, entry.entryFile)); } catch { return none(`the entry ${entry.entryFile} is not installed in the adapter-registry home`); }
  const date = only(act, /^Date: (\d{4}-\d{2}-\d{2})$/gm), identity = only(act, /^Act identity: `([^`\n]+)`$/gm);
  const instantLine = only(act, /^Recorded at \(UTC\): (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$/gm);
  const type = only(act, /^Act type: `([^`\n]+)`$/gm), artifact = only(act, /^Artifact identity: `([^`\n]+)`$/gm);
  const argument = only(act, /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gm), project = only(act, /^Project identity: `([^`\n]+)`$/gm);
  if (date === undefined || identity === undefined || type !== 'adopt-registry-entry' || artifact !== entry.candidatePath || argument === undefined || project !== 'project:syzygy') return none('the act record is not the entry\'s adopt-registry-entry act');
  if (createHash('sha256').update(installed).digest('hex') !== argument) return none('the installed entry is not the bytes the act names');
  // The instant the act took effect: its recorded instant, else the start of the day after its date (a date alone is not an instant).
  const effective = instantLine === undefined ? Date.parse(`${date}T00:00:00Z`) + 86_400_000 : Date.parse(instantLine);
  if (!Number.isSafeInteger(effective)) return none('the act record carries no readable instant');
  if (effective > options.now()) return none('the act takes effect in the future');
  return { inForce: true, record: identity, digest: argument };
}
