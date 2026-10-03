// Public-source screening for the any-repo reader (`syzygy-vjqd`).
//
// The policy's `publicSourceScope` (package
// `contracts/candidates/public-source-screening-scope/`) says every base
// detector and the base active-content rule apply unchanged to every admitted
// public body, and the base denied-path rules apply to every path. This module
// loads that policy by the owner act that approves it — the dedicated record
// `scripts/record_public_source_screening_scope_act.py` writes — never through
// the Butlers governance-inputs pin, and refuses the run when the record is
// absent, malformed or names a digest the policy bytes do not hash to.
//
// The screen reuses the PWB modules unforked: `compileDetectors` /
// `detectSecrets` over the policy's own detector strings, `scanActiveContent`,
// and `deniedPathReason` over the policy's own path lists. A withheld row
// carries a per-run HMAC id and no path, object id or body (the scope's
// `targetMetadataRule`), so nothing about it leaves the process.
//
// Not implemented here, and reported rather than assumed: the scope's
// extension-based `code-content` rule (every other blob indeterminate and
// excluded) and its run-profile and instruction-text rules.
import { createHash, createHmac, randomBytes } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { compileDetectors, deniedPathReason, detectSecrets, scanActiveContent, type DeniedPathRules, type SecretDetector } from '@syzygy/three-surface-poc-core';

import { CorpusRefusal, readRepoCorpus, type CorpusScreen, type ReaderConfig, type RepoCorpus, type RepoCorpusPorts } from './repo-corpus.js';

const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
export const PUBLIC_SOURCE_POLICY_PATH = '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json';
export const PUBLIC_SOURCE_ACT_RECORD_PATH = '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md';
const ACT_IDENTITY = /^Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-\d{4}-\d{2}-\d{2}`$/mu;
const EXACT_DIGEST = /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gmu;

/** The two inputs the screen is loaded from; absent bytes are `undefined`. */
export interface PublicSourcePolicyActPort {
  readonly read: () => Promise<{ readonly actRecord: string | undefined; readonly policy: Uint8Array | undefined }>;
}

const readOrAbsent = async (path: string): Promise<Buffer | undefined> => {
  try { return await readFile(path); } catch (error) {
    if ((error as NodeJS.ErrnoException).code === 'ENOENT') return undefined;
    throw error;
  }
};

/** Reads the act record and the policy from a Syzygy checkout (default: this one). */
export function checkoutPolicyActPort(syzygyRoot: string = REPO_ROOT): PublicSourcePolicyActPort {
  return {
    read: async () => {
      const [act, policy] = await Promise.all([readOrAbsent(join(syzygyRoot, PUBLIC_SOURCE_ACT_RECORD_PATH)), readOrAbsent(join(syzygyRoot, PUBLIC_SOURCE_POLICY_PATH))]);
      return { actRecord: act?.toString('utf8'), policy: policy === undefined ? undefined : new Uint8Array(policy) };
    },
  };
}

export interface PublicSourceScreen extends CorpusScreen {
  readonly policyId: string;
  readonly policyVersion: string;
  readonly policySha256: string;
}

function refuse(why: string): never { throw new CorpusRefusal(`public-source-policy: ${why}`); }
const stringList = (value: unknown): value is readonly string[] => Array.isArray(value) && value.every(item => typeof item === 'string' && item.length > 0);

/** Verifies the act record against the policy bytes and builds the screen. Any gap refuses. */
export async function loadPublicSourceScreen(port: PublicSourcePolicyActPort = checkoutPolicyActPort(), runKey: Uint8Array = randomBytes(32)): Promise<PublicSourceScreen> {
  if (runKey.byteLength < 32) refuse('run key shorter than 32 bytes');
  const { actRecord, policy } = await port.read();
  if (actRecord === undefined) refuse(`no act record at ${PUBLIC_SOURCE_ACT_RECORD_PATH}`);
  if (policy === undefined) refuse(`no policy at ${PUBLIC_SOURCE_POLICY_PATH}`);
  const act = actRecord!;
  if (!ACT_IDENTITY.test(act) || !act.includes('\nAct type: `approve-policy`\n') || !act.includes(`\nArtifact identity: \`${PUBLIC_SOURCE_POLICY_PATH}\`\n`)
    || !act.includes('\nProject identity: `project:syzygy`\n')) refuse('act record is not the public-source scope approve-policy act');
  const digests = [...act.matchAll(EXACT_DIGEST)].map(match => match[1]!);
  if (digests.length !== 1) refuse('act record does not name exactly one exact digest');
  const policySha256 = createHash('sha256').update(policy!).digest('hex');
  if (policySha256 !== digests[0]) refuse('policy bytes do not hash to the act argument');
  let doc: Record<string, unknown>;
  try { doc = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(policy!)) as Record<string, unknown>; } catch { return refuse('policy is not UTF-8 JSON'); }
  const scope = doc.publicSourceScope, admission = doc.sourceAdmission as Record<string, unknown> | undefined;
  if (scope === null || typeof scope !== 'object' || Array.isArray(scope)) refuse('policy carries no publicSourceScope');
  if (typeof doc.policyId !== 'string' || typeof doc.policyVersion !== 'string') refuse('policy identity unreadable');
  if (admission === null || typeof admission !== 'object' || !stringList(admission.deniedPathBasenames) || !stringList(admission.deniedPathPrefixes)
    || !stringList(admission.deniedPathSuffixes)) refuse('policy denied-path rules unreadable');
  const rules: DeniedPathRules = { basenames: admission!.deniedPathBasenames as string[], prefixes: admission!.deniedPathPrefixes as string[], suffixes: admission!.deniedPathSuffixes as string[] };
  let detectors: ReturnType<typeof compileDetectors>;
  try { detectors = compileDetectors({ detectors: doc.detectors as readonly SecretDetector[] }); } catch (error) { return refuse(`detectors: ${error instanceof Error ? error.message : 'invalid'}`); }
  const key = Buffer.from(runKey);
  return {
    policyId: doc.policyId as string, policyVersion: doc.policyVersion as string, policySha256,
    deniedPath: path => deniedPathReason(path, rules) !== undefined,
    // Detectors scan the raw text (inert code contexts included), then the active-content scan.
    screenBody: body => detectSecrets(detectors, body) !== undefined ? 'secret-detector-match' : scanActiveContent(body).length > 0 ? 'active-content' : undefined,
    opaqueId: identity => `s-${createHmac('sha256', key).update(identity).digest('hex').slice(0, 24)}`,
  };
}

/** The any-repo reader with the public-source screen in force: the policy act
 * is verified before the admission port is asked or the repository touched. */
export async function readScreenedRepoCorpus(repoRoot: string, config: Pick<ReaderConfig, 'repositoryId' | 'revision' | 'include' | 'exclude' | 'oversize'>,
  ports: Omit<RepoCorpusPorts, 'screen'> & { readonly policyAct?: PublicSourcePolicyActPort; readonly runKey?: Uint8Array } = {}): Promise<RepoCorpus> {
  const screen = await loadPublicSourceScreen(ports.policyAct, ports.runKey);
  return readRepoCorpus(repoRoot, config, { ...(ports.admission === undefined ? {} : { admission: ports.admission }), ...(ports.readBlobs === undefined ? {} : { readBlobs: ports.readBlobs }), screen });
}
