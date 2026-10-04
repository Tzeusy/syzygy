import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';

import { PWB_DENIED_PATH_RULES, PWB_SECRET_POLICY } from '@syzygy/three-surface-poc-core';

import type { DossierRoute } from './dossier-generation.js';
import { ROUTE_ENTRIES } from './dossier-route-registry.js';
import type { PublicSourcePolicyActPort } from './public-source-screening.js';

const sha = (bytes: Uint8Array | string): string => createHash('sha256').update(bytes).digest('hex');
export const FIXTURE_EXTENSIONS = ['.c', '.js', '.py', '.ts', '.md', '.txt'];

/** A synthetic policy plus the act record that names its digest, shaped like the real public-source scope act. Never the real policy. */
export function fixturePolicyActPort(extensions: readonly string[] = FIXTURE_EXTENSIONS): PublicSourcePolicyActPort {
  const policy = new TextEncoder().encode(`${JSON.stringify({
    policyId: 'synthetic-public-source-policy', policyVersion: '9.9.0-fixture.1',
    sourceAdmission: { deniedPathBasenames: PWB_DENIED_PATH_RULES.basenames, deniedPathPrefixes: PWB_DENIED_PATH_RULES.prefixes, deniedPathSuffixes: PWB_DENIED_PATH_RULES.suffixes },
    detectors: PWB_SECRET_POLICY.detectors,
    publicSourceScope: { contentClassification: { rules: [{ class: 'code-structure', rule: 'paths' }, { class: 'code-content', sourceExtensions: extensions }] } },
  }, null, 2)}\n`);
  const actRecord = ['# Owner act — synthetic fixture', '',
    'Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-03`', '', 'Act type: `approve-policy`', '', 'Project identity: `project:syzygy`', '',
    'Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`', '', `Exact digest (SHA-256): \`${sha(policy)}\``, ''].join('\n');
  return { read: async () => ({ actRecord, policy }) };
}

/** A scratch Syzygy root holding a registry-entry act and its installed entry for one route, as the recorders leave them. */
export function fixtureRouteRoot(route: DossierRoute, over: { readonly installed?: string; readonly skipAct?: boolean; readonly date?: string; readonly instant?: string } = {}): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-route-root-'));
  const entry = ROUTE_ENTRIES[route];
  const bytes = `{"fixture":"${route}"}\n`;
  const put = (rel: string, body: string): void => { mkdirSync(dirname(join(root, rel)), { recursive: true }); writeFileSync(join(root, rel), body); };
  put(`.syzygy/governance/declarations/adapter-registry/${entry.entryFile}`, over.installed ?? bytes);
  if (over.skipAct !== true) {
    put(`.syzygy/governance/decisions/${entry.actFile}`, ['# Owner act — fixture', '', `Date: ${over.date ?? '2026-09-01'}`, '', ...(over.instant === undefined ? [] : [`Recorded at (UTC): ${over.instant}`, '']),
      'Owner: Tzeusy', '', 'Act identity: `PUBLIC-ADMISSION-REGISTRY-FIXTURE-2026-09-01`', '', 'Act type: `adopt-registry-entry`', '', 'Project identity: `project:syzygy`', '',
      `Artifact identity: \`${entry.candidatePath}\``, '', `Exact digest (SHA-256): \`${sha(bytes)}\``, ''].join('\n'));
  }
  return root;
}
