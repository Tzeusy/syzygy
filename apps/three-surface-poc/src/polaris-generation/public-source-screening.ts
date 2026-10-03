// Public-source screening for the any-repo reader (`syzygy-vjqd`).
//
// The policy's `publicSourceScope` (package
// `contracts/candidates/public-source-screening-scope/`) says every base
// detector and the base active-content rule apply unchanged to every admitted
// public body, the base denied-path rules apply to every path, and a blob is
// `code-content` only when its final path segment ends with one of the scope's
// `sourceExtensions` (case-sensitive); every other blob is indeterminate and
// excluded unread. This module
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
// Version 2 of the scope (package `public-source-screening-scope-v2/`) adds
// the `project-documentation` class: a closed set of root, docs/doc and
// licenses paths (`project-documentation.ts`). Its policy is loaded by the
// version-2 act record when one exists, and the class maps only while the
// policy's `prerequisite` holds: the RFC5-14 amendment act is recorded and the
// installed RFC-0005 bytes hash to its argument and list the class. Otherwise
// every path the rule names stays indeterminate, as the prerequisite says, and
// the rest of the scope is unchanged. The class changes no screen: denied
// paths, detectors and the active-content rule run first on every document. A
// consent that does not list the class still permits no egress of it; the
// consent ports are not wired here.
//
// Policy residuals, not repairs: the detectors match literal forms only, so a
// secret encoded (base64, hex) or split across lines passes them. Not
// implemented here: the scope's run-profile and instruction-text rules.
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { compileDetectors, deniedPathReason, detectSecrets, scanActiveContent, type DeniedPathRules, type SecretDetector } from '@syzygy/three-surface-poc-core';

import { classifyDocumentation, parseDocumentationRule, type DocumentationRule } from './project-documentation.js';
import { excludedSourceId, newGenerationRunKey } from './run-key.js';
import { CorpusRefusal, readRepoCorpus, type CorpusScreen, type ReaderConfig, type RepoCorpus, type RepoCorpusPorts } from './repo-corpus.js';

const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
export const PUBLIC_SOURCE_POLICY_PATH = '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json';
export const PUBLIC_SOURCE_ACT_RECORD_PATH = '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md';
// The version-2 record (`scripts/record_public_source_screening_scope_v2_act.py`, lane-d2) supersedes version 1.
export const PUBLIC_SOURCE_V2_ACT_RECORD_PATH = '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md';
export const RFC5_CLASS_ACT_RECORD_PATH = '.syzygy/governance/decisions/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md';
export const RFC5_MODULE_PATH = '.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md';
const RFC5_CLASS_ROW = '| `project-documentation` |';
const ACT_IDENTITY = /^Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-\d{4}-\d{2}-\d{2}`$/mu;
const V2_ACT_IDENTITY = /^Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL-\d{4}-\d{2}-\d{2}`$/mu;
const RFC5_ACT_IDENTITY = /^Act identity: `RFC5-PROJECT-DOCUMENTATION-AMEND-\d{4}-\d{2}-\d{2}`$/mu;
const RECORDED_AT = /^Recorded at \(UTC\): (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$/gmu;
const EXACT_DIGEST = /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gmu;

/** The inputs the screen is loaded from; absent bytes are `undefined`. */
export interface PublicSourcePolicyActPort {
  readonly read: () => Promise<{
    readonly actRecord: string | undefined; readonly policy: Uint8Array | undefined;
    // Version 2: its act record, and the RFC5-14 class act with the installed module it names.
    readonly v2ActRecord?: string | undefined; readonly classActRecord?: string | undefined; readonly rfc5Module?: Uint8Array | undefined;
  }>;
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
      const [act, policy, v2Act, classAct, rfc5] = await Promise.all([PUBLIC_SOURCE_ACT_RECORD_PATH, PUBLIC_SOURCE_POLICY_PATH, PUBLIC_SOURCE_V2_ACT_RECORD_PATH, RFC5_CLASS_ACT_RECORD_PATH, RFC5_MODULE_PATH]
        .map(path => readOrAbsent(join(syzygyRoot, path))));
      return {
        actRecord: act?.toString('utf8'), policy: policy === undefined ? undefined : new Uint8Array(policy),
        v2ActRecord: v2Act?.toString('utf8'), classActRecord: classAct?.toString('utf8'), rfc5Module: rfc5 === undefined ? undefined : new Uint8Array(rfc5),
      };
    },
  };
}

export interface PublicSourceScreen extends CorpusScreen {
  readonly policyId: string;
  readonly policyVersion: string;
  readonly policySha256: string;
  /** Whether the policy maps `project-documentation`, and whether its prerequisite holds. */
  readonly projectDocumentation: 'not-in-policy' | 'mapped' | 'prerequisite-unmet';
  /** The class a path is placed in after the path screens; `undefined` is indeterminate. */
  readonly classifyPath: (path: string) => 'code-content' | 'project-documentation' | undefined;
}

function refuse(why: string): never { throw new CorpusRefusal(`public-source-policy: ${why}`); }
const stringList = (value: unknown): value is readonly string[] => Array.isArray(value) && value.every(item => typeof item === 'string' && item.length > 0);
const sha256 = (bytes: Uint8Array): string => createHash('sha256').update(bytes).digest('hex');

// The one exact digest of an act record of the given identity, type and artifact; a string when it is not one.
function actArgument(record: string, identity: RegExp, type: string, artifact: string): { readonly digest: string } | string {
  if (!identity.test(record) || !record.includes(`\nAct type: \`${type}\`\n`) || !record.includes(`\nArtifact identity: \`${artifact}\`\n`)
    || !record.includes('\nProject identity: `project:syzygy`\n')) return 'not-the-act';
  const digests = [...record.matchAll(EXACT_DIGEST)].map(match => match[1]!);
  return digests.length === 1 ? { digest: digests[0]! } : 'digest-count';
}

// The policy's prerequisite: the class act is recorded and the installed module is its argument and lists the class.
function classActInForce(record: string | undefined, module: Uint8Array | undefined): boolean {
  if (record === undefined || module === undefined) return false;
  const argument = actArgument(record, RFC5_ACT_IDENTITY, 'contract-amendment', RFC5_MODULE_PATH);
  return typeof argument !== 'string' && sha256(module) === argument.digest && Buffer.from(module).toString('utf8').includes(RFC5_CLASS_ROW);
}

/** Verifies the act record against the policy bytes and builds the screen. Any gap refuses. */
export async function loadPublicSourceScreen(port: PublicSourcePolicyActPort = checkoutPolicyActPort(), runKey: Uint8Array = newGenerationRunKey()): Promise<PublicSourceScreen> {
  if (runKey.byteLength < 32) refuse('run key shorter than 32 bytes');
  const { actRecord, policy, v2ActRecord, classActRecord, rfc5Module } = await port.read();
  // The version-2 act supersedes the version-1 act for this policy: read it whenever it exists.
  const v2 = v2ActRecord !== undefined;
  // A v2 record supersedes a v1 record, so v2 without v1 refuses.
  if (actRecord === undefined) refuse(`no act record at ${PUBLIC_SOURCE_ACT_RECORD_PATH}`);
  if (policy === undefined) refuse(`no policy at ${PUBLIC_SOURCE_POLICY_PATH}`);
  const argument = actArgument(v2 ? v2ActRecord : actRecord!, v2 ? V2_ACT_IDENTITY : ACT_IDENTITY, 'approve-policy', PUBLIC_SOURCE_POLICY_PATH);
  if (argument === 'not-the-act') refuse(`act record is not the public-source scope${v2 ? ' v2' : ''} approve-policy act`);
  if (argument === 'digest-count') refuse('act record does not name exactly one exact digest');
  const policySha256 = sha256(policy!);
  if (policySha256 !== (argument as { digest: string }).digest) refuse('policy bytes do not hash to the act argument');
  // The v2 record names the v1 record it supersedes; the line is required, not parsed.
  if (v2 && !v2ActRecord.split('\n').some(line => line.startsWith('Supersession / revocation: ') && line.includes(`\`${PUBLIC_SOURCE_ACT_RECORD_PATH}\``)))
    refuse('v2 act record names no superseded v1 record');
  // The pair the records state, as the sitting installer (`policy_acts`) refuses it: the v1 record
  // is the v1 act, its argument differs from and is named by the v2 record, and v2 is recorded after it.
  if (v2) {
    const v1 = actArgument(actRecord!, ACT_IDENTITY, 'approve-policy', PUBLIC_SOURCE_POLICY_PATH);
    if (typeof v1 === 'string') refuse('the superseded v1 record is not the public-source scope approve-policy act');
    const v1Digest = (v1 as { digest: string }).digest;
    if (v1Digest === policySha256) refuse('the v2 act carries the v1 act argument');
    if (!v2ActRecord.includes(v1Digest)) refuse('the v2 act record does not name the v1 argument it supersedes');
    const [v1At, v2At] = [actRecord!, v2ActRecord].map(text => [...text.matchAll(RECORDED_AT)].map(match => match[1]!));
    if (v1At!.length !== 1 || v2At!.length !== 1) refuse('an act record does not carry exactly one recorded instant');
    if (v2At![0]! <= v1At![0]!) refuse('the v2 act is not recorded after the v1 act');
  }
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
  const documentation = (classification!.rules as unknown[]).filter(rule => (rule as Record<string, unknown> | null)?.class === 'project-documentation');
  if (documentation.length > 1) refuse('policy carries more than one project-documentation rule');
  if (documentation.length !== (v2 ? 1 : 0)) refuse(v2 ? 'the v2 act approves a policy without the project-documentation rule' : 'a project-documentation rule needs the v2 act');
  let documentationRule: DocumentationRule | undefined;
  if (v2) {
    const prerequisite = (scope as Record<string, unknown>).prerequisite as Record<string, unknown> | undefined;
    if (!Array.isArray(classification!.classesClassified) || !classification!.classesClassified.includes('project-documentation')) refuse('classesClassified does not list project-documentation');
    if (prerequisite === null || typeof prerequisite !== 'object' || typeof prerequisite.rule !== 'string') refuse('policy carries no readable prerequisite');
    const rule = parseDocumentationRule(documentation[0] as Record<string, unknown>, doc.policyVersion as string);
    if (typeof rule === 'string') refuse(`project-documentation rule: ${rule}`);
    documentationRule = rule as DocumentationRule;
  }
  const projectDocumentation = documentationRule === undefined ? 'not-in-policy' : classActInForce(classActRecord, rfc5Module) ? 'mapped' : 'prerequisite-unmet';
  const mapped = projectDocumentation === 'mapped' ? documentationRule : undefined;
  // A path is classified only when exactly one class places it.
  const classifyPath = (path: string): 'code-content' | 'project-documentation' | undefined => {
    const code = sourceExtensions.some(extension => (path.split('/').at(-1) ?? '').endsWith(extension));
    const prose = mapped !== undefined && classifyDocumentation(path, mapped);
    return code === prose ? undefined : code ? 'code-content' : 'project-documentation';
  };
  const rules: DeniedPathRules = { basenames: admission!.deniedPathBasenames as string[], prefixes: admission!.deniedPathPrefixes as string[], suffixes: admission!.deniedPathSuffixes as string[] };
  let detectors: ReturnType<typeof compileDetectors>;
  try { detectors = compileDetectors({ detectors: doc.detectors as readonly SecretDetector[] }); } catch (error) { return refuse(`detectors: ${error instanceof Error ? error.message : 'invalid'}`); }
  const key = Buffer.from(runKey);
  return {
    policyId: doc.policyId as string, policyVersion: doc.policyVersion as string, policySha256, projectDocumentation, classifyPath,
    // Unread: denied path, then a detector match anywhere in the path, then a path no class places.
    screenPath: path => deniedPathReason(path, rules) !== undefined ? 'denied-path'
      : detectSecrets(detectors, path) !== undefined ? 'secret-detector-match'
        : classifyPath(path) !== undefined ? undefined : 'unknown-extraction-class',
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
