// Public-source screening for the any-repo reader (`syzygy-vjqd`).
//
// The policy's `publicSourceScope` (package
// `contracts/candidates/public-source-screening-scope/`) says every base
// detector and the base active-content rule apply unchanged to every admitted
// public body, the base denied-path rules apply to every path, and a blob is
// `project-documentation` when exactly one of that rule's path rules matches
// it (version 2; classified only while the RFC5-14 class amendment act is in
// force and unwithdrawn at the port's clock, the scope's `prerequisite`), else `code-content` only when its
// final path segment ends with one of the scope's `sourceExtensions`
// (case-sensitive); every other blob is indeterminate and excluded unread.
// The class decision is `@syzygy/polaris-generation-core`'s
// `publicSourceContentClass`, shared with the dossier's screen. This module
// loads that policy by the owner act that approves it — the dedicated record
// `scripts/record_public_source_screening_scope_act.py` writes — never through
// the Butlers governance-inputs pin, and refuses the run when the record is
// absent, malformed or names a digest the policy bytes do not hash to.
//
// The screen reuses the PWB modules unforked: `compileDetectors` /
// `detectSecrets` over the policy's own detector strings (run over every path
// as well as every body), `scanActiveContent`, and `deniedPathReason` over the
// policy's own path lists. Every excluded row carries a per-run HMAC id and no
// path, object id or body (the scope's `targetMetadataRule`), so nothing about
// it leaves the process.
//
// Policy residuals, not repairs: the detectors match literal forms only, so a
// secret encoded (base64, hex) or split across lines passes them; and the
// project-documentation rule folds ASCII A-Z only and splits words only at
// its `docTokenSeparators`, as its text says, so a Unicode look-alike of a
// withheld word (`docs/ｄesign.md`), a word joined by a tab
// (`docs/a\tb.md`) or one that runs on into other characters
// (`docs/rfc0001.md`) is admitted as project-documentation, its body still
// screened. Not implemented here: the scope's run-profile and
// instruction-text rules. Admitting a body is not consent to send it:
// `contentClass` names its class for whoever gates egress by consent; this
// reader has no production caller that hands its corpus on.
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { readClassActState } from '@syzygy/polaris-generation-consent';
import { publicSourceContentClass, readProjectDocumentationRule, type PublicSourceContentClass } from '@syzygy/polaris-generation-core';
import { compileDetectors, deniedPathReason, detectSecrets, scanActiveContent, type DeniedPathRules, type SecretDetector } from '@syzygy/three-surface-poc-core';

import { excludedSourceId, newGenerationRunKey } from './run-key.js';
import { CorpusRefusal, readRepoCorpus, type CorpusScreen, type ReaderConfig, type RepoCorpus, type RepoCorpusPorts } from './repo-corpus.js';

const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
export const PUBLIC_SOURCE_POLICY_PATH = '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json';
export const PUBLIC_SOURCE_ACT_RECORD_PATH = '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md';
const ACT_IDENTITY = /^Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-\d{4}-\d{2}-\d{2}`$/mu;
const EXACT_DIGEST = /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gmu;

/** The inputs the screen is loaded from; absent bytes are `undefined`. `classActInForce` only decides whether the project-documentation
 * class is classified: true only when the RFC5-14 class amendment act is in force at the port's clock; leaving it out leaves that class's
 * paths indeterminate. */
export interface PublicSourcePolicyActPort {
  readonly read: () => Promise<{ readonly actRecord: string | undefined; readonly policy: Uint8Array | undefined; readonly classActInForce?: boolean }>;
}

const readOrAbsent = async (path: string): Promise<Buffer | undefined> => {
  try { return await readFile(path); } catch (error) {
    if ((error as NodeJS.ErrnoException).code === 'ENOENT') return undefined;
    throw error;
  }
};

/** Reads the act record and the policy from a Syzygy checkout (default: this one), and decides the class prerequisite there at `now()`
 * with the dossier's own strict reader (`readClassActState`): the RFC5-14 act must be recorded in the recorder's form, bind the
 * installed RFC-0005 module's bytes, have taken effect by `now()`, and be named by no other decisions file (a withdrawal). */
export function checkoutPolicyActPort(syzygyRoot: string = REPO_ROOT, now: () => number = Date.now): PublicSourcePolicyActPort {
  return {
    read: async () => {
      const [act, policy] = await Promise.all([PUBLIC_SOURCE_ACT_RECORD_PATH, PUBLIC_SOURCE_POLICY_PATH].map(path => readOrAbsent(join(syzygyRoot, path))));
      const classAct = await readClassActState({ root: syzygyRoot, now: now() });
      return { actRecord: act?.toString('utf8'), policy: policy === undefined ? undefined : new Uint8Array(policy), classActInForce: classAct.state === 'ok' };
    },
  };
}

export interface PublicSourceScreen extends CorpusScreen {
  readonly policyId: string;
  readonly policyVersion: string;
  readonly policySha256: string;
  /** Whether the policy's project-documentation class is classified: it has the rule and the RFC5-14 class act is in force. */
  readonly projectDocumentation: boolean;
  /** The content class `screenPath` admits a path under, or undefined when it excludes the path. Whoever hands an admitted body to an
   * agent or a provider gates it by the classes the consent for that pair lists; screening is not that consent. */
  readonly contentClass: (path: string) => PublicSourceContentClass | undefined;
}

function refuse(why: string): never { throw new CorpusRefusal(`public-source-policy: ${why}`); }
const stringList = (value: unknown): value is readonly string[] => Array.isArray(value) && value.every(item => typeof item === 'string' && item.length > 0);

/** Verifies the act record against the policy bytes and builds the screen. Any gap refuses. */
export async function loadPublicSourceScreen(port: PublicSourcePolicyActPort = checkoutPolicyActPort(), runKey: Uint8Array = newGenerationRunKey()): Promise<PublicSourceScreen> {
  if (runKey.byteLength < 32) refuse('run key shorter than 32 bytes');
  const { actRecord, policy, classActInForce } = await port.read();
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
  const classification = (scope as Record<string, unknown>).contentClassification as Record<string, unknown> | undefined;
  const codeContent = Array.isArray(classification?.rules) ? classification.rules.filter((rule: unknown) => (rule as Record<string, unknown> | null)?.class === 'code-content') : [];
  const extensions = (codeContent[0] as Record<string, unknown> | undefined)?.sourceExtensions;
  if (codeContent.length !== 1 || !stringList(extensions) || extensions.length === 0 || extensions.some(extension => !/^\.[^/\s]+$/u.test(extension) || extension.includes('..'))) refuse('policy sourceExtensions unreadable');
  const sourceExtensions = extensions as readonly string[];
  const documentationRead = readProjectDocumentationRule(classification!.rules as readonly unknown[], sourceExtensions);
  if (!documentationRead.ok) refuse(`policy ${documentationRead.why.replace(/^its /u, '')}`);
  // The scope's prerequisite: the class is classified only while the in-force RFC-0005 vocabulary lists it.
  const documentation = classActInForce === true ? documentationRead.rule : null;
  const rules: DeniedPathRules = { basenames: admission!.deniedPathBasenames as string[], prefixes: admission!.deniedPathPrefixes as string[], suffixes: admission!.deniedPathSuffixes as string[] };
  let detectors: ReturnType<typeof compileDetectors>;
  try { detectors = compileDetectors({ detectors: doc.detectors as readonly SecretDetector[] }); } catch (error) { return refuse(`detectors: ${error instanceof Error ? error.message : 'invalid'}`); }
  const key = Buffer.from(runKey);
  // Unread: denied path, then a detector match anywhere in the path, then a path in neither project-documentation nor code-content.
  const screenPath = (path: string) => deniedPathReason(path, rules) !== undefined ? 'denied-path' as const
    : detectSecrets(detectors, path) !== undefined ? 'secret-detector-match' as const
      : publicSourceContentClass(path, sourceExtensions, documentation) !== undefined ? undefined : 'unknown-extraction-class' as const;
  return {
    policyId: doc.policyId as string, policyVersion: doc.policyVersion as string, policySha256, projectDocumentation: documentation !== null,
    screenPath,
    contentClass: path => screenPath(path) === undefined ? publicSourceContentClass(path, sourceExtensions, documentation) : undefined,
    // Detectors scan the raw text (inert code contexts included), then the active-content scan.
    screenBody: body => detectSecrets(detectors, body) !== undefined ? 'secret-detector-match' : scanActiveContent(body).length > 0 ? 'active-content' : undefined,
    opaqueId: identity => excludedSourceId(key, identity),
  };
}

/** The any-repo reader with the public-source screen in force: the policy act
 * is verified before the admission port is asked or the repository touched. */
export async function readScreenedRepoCorpus(repoRoot: string, config: Pick<ReaderConfig, 'repositoryId' | 'revision' | 'include' | 'exclude' | 'oversize'>,
  ports: Omit<RepoCorpusPorts, 'screen'> & { readonly policyAct?: PublicSourcePolicyActPort; readonly runKey?: Buffer } = {}): Promise<RepoCorpus> {
  const runKey = ports.runKey ?? newGenerationRunKey();
  const screen = await loadPublicSourceScreen(ports.policyAct, runKey);
  return readRepoCorpus(repoRoot, config, { ...(ports.admission === undefined ? {} : { admission: ports.admission }), ...(ports.readBlobs === undefined ? {} : { readBlobs: ports.readBlobs }), screen, runKey });
}
