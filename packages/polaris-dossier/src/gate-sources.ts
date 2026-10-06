import {
  REGISTRY_GIT_SOURCE_ACT_FORM, createPackageAdmissionRecordsPort, readDigestBoundActState, readPolicyActChain,
  type ConsentedRevision, type DigestBoundActForm, type PackageReaderFs,
} from '@syzygy/polaris-generation-consent';
import type { DrawerStatement } from './governed.js';

/** The records Syzygy's start gates read (REQ-polaris-generation-033, 036), each re-read on every call and never cached.
 *
 * Every source establishes "in force" by the act cross-check of RFC3-16(a): an owner-act record in its recorder's form whose argument
 * is the sha256 of the artifact's current bytes and whose instant is not after `now`; never by a status word or a file's presence
 * (R3-F8). The records lie in Syzygy's checkout, within the agent sessions' write reach, and every report says so. */

export type GateState =
  | { readonly state: 'ok'; readonly record: string }
  | { readonly state: 'absent'; readonly why: string }
  | { readonly state: 'refused'; readonly why: string };

export type ConsentAnswer = { readonly satisfied: true; readonly record: string } | { readonly satisfied: false; readonly why: string };

/** A per-project statement (SEC-2's explicit, recorded, per-project consent) as the gate needs it. No record of this kind is defined
 * yet (syzygy-qkea.14); a source implements this from whatever record and act the owner adopts. */
export interface ProviderStatementRecord {
  readonly recordId: string;
  readonly version: string;
  readonly digest: string;
  /** The model provider the statement names. */
  readonly provider: string;
  /** The content classes it may receive. */
  readonly contentClasses: readonly string[];
  readonly withdrawn: boolean;
  /** The owner act that put it in force, cross-checked under RFC3-16(a) by the source; null when none binds its bytes. */
  readonly act: { readonly identity: string; readonly inForceAt: number } | null;
}

export interface ProjectInputSource {
  readonly drawerFor: (repositoryId: string) => Promise<DrawerStatement>;
}
export interface ProviderStatementSource {
  readonly statementsFor: (repositoryId: string) => Promise<readonly ProviderStatementRecord[]>;
}

export interface GateSources {
  /** Where the records are read from, for the disclosure. */
  readonly recordsRoot: string;
  /** Repository ids of the observation consents in force whose `Upstream:` is exactly the URL. */
  readonly repositoryIdsFor: (url: string) => Promise<readonly string[]>;
  readonly consentedRevisionsFor: (repositoryId: string) => Promise<readonly ConsentedRevision[]>;
  readonly observationConsentFor: (repositoryId: string, revision: string) => Promise<ConsentAnswer>;
  readonly registryEntry: () => Promise<GateState>;
  /** The classification and screening policy that covers public sources: one policy file carries both (the public-source scope of
   * `project:syzygy`'s secret-classification policy), under one act chain. */
  readonly screeningPolicy: () => Promise<GateState>;
  readonly d9: () => Promise<GateState>;
  readonly rfc720Ruling: () => Promise<GateState>;
  readonly projectInput: ProjectInputSource;
  readonly providerStatements: ProviderStatementSource;
}

/** The implementation the source-acquisition registry entry must name for the dossier's reads (git-object-reader.ts). The adopted
 * entry version that names it is governance work (syzygy-qkea.14); until then the gate refuses. */
export const DOSSIER_READER_IMPLEMENTATION_ID = 'polaris-dossier/git-object-reader';

export const NO_PROJECT_INPUT: ProjectInputSource = Object.freeze({
  drawerFor: async (): Promise<DrawerStatement> => ({
    stated: false,
    why: 'no admitted project input record (REQ-polaris-generation-001) for this subject exists, so whether a kernel evidence drawer exists is not stated',
  }),
});
export const NO_PROVIDER_STATEMENTS: ProviderStatementSource = Object.freeze({ statementsFor: async () => [] });

/** No owner-act record binds a digest of D9's text: D9 was adopted by the owner's words recorded in the doctrine amendment log, and
 * its review notes say "D9 binds no act digest". Under RFC3-16(a) that is not an act cross-check, so D9 is not established in force
 * here, and no log row is read as one. A recorder's form goes here once an act exists. */
export const D9_ACT_FORM: DigestBoundActForm | null = null;
/** The owner direction POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05, item 1 (the RFC7-20 reading), binds no artifact digest either. */
export const RFC7_20_RULING_ACT_FORM: DigestBoundActForm | null = null;

const notEstablished = (what: string): GateState => ({
  state: 'absent',
  why: `no owner-act record binds a digest of ${what}, so the act cross-check of RFC3-16(a) cannot establish it in force; a status word, a log row or a file's presence is not read as one`,
});

/** The statement gate: exactly one in-force statement for the subject that names `provider` and at least one content class. */
export function providerStatementGate(records: readonly ProviderStatementRecord[], provider: string, now: number): GateState {
  const named = records.filter(r => r.provider === provider);
  const live = named.filter(r => !r.withdrawn && r.act !== null && r.act.inForceAt <= now && r.contentClasses.length > 0);
  if (live.length === 1) return { state: 'ok', record: `${live[0]!.recordId}@${live[0]!.version}` };
  if (live.length > 1) return { state: 'refused', why: `${live.length} in-force per-project statements name the provider ${provider}; which one governs is ambiguous` };
  if (named.length === 0) return { state: 'absent', why: `no per-project statement names the operator's agent provider ${provider}` };
  const why = named.map(r => `${r.recordId}@${r.version} ${r.withdrawn ? 'is withdrawn' : r.act === null ? 'has no owner act binding its bytes' : r.act.inForceAt > now ? 'is not in force yet' : 'names no content class'}`);
  return { state: 'absent', why: `no per-project statement naming ${provider} is in force: ${why.join('; ')}` };
}

export interface PackageGateSourceOptions {
  readonly root: string;
  readonly now: () => number;
  readonly fs?: PackageReaderFs;
  readonly projectInput?: ProjectInputSource;
  readonly providerStatements?: ProviderStatementSource;
  readonly registryForm?: DigestBoundActForm;
  readonly d9Form?: DigestBoundActForm | null;
  readonly rfc720Form?: DigestBoundActForm | null;
}

/** The gate sources over one Syzygy checkout: the consent package's readers for the observation consents, the policy chain and the
 * registry entry act; D9 and the RFC7-20 ruling through the same cross-check once a form exists; the drawer and the statement through
 * their injectable sources, which in production state nothing and hold nothing. */
export function createPackageGateSources(options: PackageGateSourceOptions): GateSources {
  const fsOption = options.fs === undefined ? {} : { fs: options.fs };
  const port = createPackageAdmissionRecordsPort({ root: options.root, now: options.now, ...fsOption });
  const crossCheck = async (form: DigestBoundActForm | null | undefined, what: string): Promise<GateState> => {
    if (form === null || form === undefined) return notEstablished(what);
    const state = await readDigestBoundActState({ root: options.root, now: options.now(), form, ...fsOption });
    return state.state === 'ok' ? { state: 'ok', record: state.act.identity } : state;
  };
  return {
    recordsRoot: options.root,
    repositoryIdsFor: url => port.repositoryIdsFor(url),
    consentedRevisionsFor: repositoryId => port.consentedRevisionsFor(repositoryId),
    observationConsentFor: async (repositoryId, revision) => {
      const answer = await port.check({ kind: 'observation-consent', repositoryId, revision });
      return answer.satisfied ? { satisfied: true, record: answer.record } : { satisfied: false, why: answer.why };
    },
    registryEntry: async () => {
      const state = await readDigestBoundActState({ root: options.root, now: options.now(), form: options.registryForm ?? REGISTRY_GIT_SOURCE_ACT_FORM, ...fsOption });
      if (state.state !== 'ok') return state;
      return registryEntryUsable(state.artifactText, state.act.identity);
    },
    screeningPolicy: async () => {
      const state = await readPolicyActChain({ root: options.root, now: options.now(), ...fsOption });
      return state.state === 'ok' ? { state: 'ok', record: state.final.identity } : state;
    },
    d9: () => crossCheck(options.d9Form === undefined ? D9_ACT_FORM : options.d9Form, 'the D9 text (SEC-3 amendment)'),
    rfc720Ruling: () => crossCheck(options.rfc720Form === undefined ? RFC7_20_RULING_ACT_FORM : options.rfc720Form, 'the RFC7-20 reading (POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05, item 1)'),
    projectInput: options.projectInput ?? NO_PROJECT_INPUT,
    providerStatements: options.providerStatements ?? NO_PROVIDER_STATEMENTS,
  };
}

/** A registry entry the act binds still admits no read unless it names the dossier's reader with a known implementation version
 * (RFC4-3 admits no output from an entry whose implementation version is Unknown). */
export function registryEntryUsable(entryText: string, actIdentity: string): GateState {
  let document: unknown;
  try {
    document = JSON.parse(entryText);
  } catch {
    return { state: 'refused', why: `the registry entry bound by ${actIdentity} is not JSON` };
  }
  const entries = (document as { entries?: unknown } | null)?.entries;
  if (!Array.isArray(entries) || entries.length !== 1 || entries[0] === null || typeof entries[0] !== 'object') {
    return { state: 'refused', why: `the registry entry file bound by ${actIdentity} does not hold exactly one entry` };
  }
  const entry = entries[0] as { implementationId?: unknown; implementationVersion?: unknown };
  if (entry.implementationId !== DOSSIER_READER_IMPLEMENTATION_ID) {
    return { state: 'refused', why: `the registry entry bound by ${actIdentity} names the implementation ${JSON.stringify(entry.implementationId)}, not ${DOSSIER_READER_IMPLEMENTATION_ID}` };
  }
  if (typeof entry.implementationVersion !== 'string' || entry.implementationVersion.trim() === '') {
    return { state: 'refused', why: `the registry entry bound by ${actIdentity} has no implementation version (Unknown), so RFC4-3 admits no output from it` };
  }
  return { state: 'ok', record: actIdentity };
}

export const RECORDS_WITHIN_REACH = 'the consent, registry, policy and statement records the gates read lie in Syzygy\'s checkout, which the agent sessions can write; Syzygy re-reads and re-checks them at every step, and cannot rule out that a session changed them';
