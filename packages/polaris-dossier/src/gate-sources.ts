import {
  LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM, createPackageAdmissionRecordsPort, readDigestBoundActState, readPolicyActChain, readVersionedSignoffState,
  type ActState, type ConsentedRevision, type DigestBoundAct, type DigestBoundActForm, type PackageReaderFs, type VersionedSignoffForm,
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

/** A per-project statement (SEC-2's explicit, recorded, per-project consent) as the gate needs it. The package source reads it from
 * the agent-provider records of the local-agent sitting and their acts (`STATEMENT_FORMS`). */
export interface ProviderStatementRecord {
  readonly recordId: string;
  readonly version: string;
  readonly digest: string;
  /** The agent tool the statement names, as the run configuration writes it (`AGENT_TOOLS`): consent is to one tool with one provider. */
  readonly agentTool: string;
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
  /** Why no observation consent in force names the URL, for a refusal's reason only (R-POLARIS-DOSSIER-S3-GATES-1 finding 4). */
  readonly consentAbsenceFor?: (url: string) => Promise<string>;
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

/** The implementation the source-acquisition registry entry must name for the dossier's reads (git-object-reader.ts): the local-agent
 * entry, signed off by version tag (`LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM`), names it with implementation version 1.0.0. */
export const DOSSIER_READER_IMPLEMENTATION_ID = 'polaris-dossier/git-object-reader';

const UNSTATED_WHY = 'no admitted project input record (REQ-polaris-generation-001) for this subject exists, so whether a kernel evidence drawer exists is not stated';
export const NO_PROJECT_INPUT: ProjectInputSource = Object.freeze({
  drawerFor: async (): Promise<DrawerStatement> => ({ stated: false, why: UNSTATED_WHY }),
});
export const NO_PROVIDER_STATEMENTS: ProviderStatementSource = Object.freeze({ statementsFor: async () => [] });

/** The local-agent sitting's records (scripts/build_dossier_local_agent_acts.py) and the acts over them, each a dedicated decisions
 * record written by scripts/record_dossier_local_agent_acts.py: `DOSSIER-LOCAL-AGENT-<stem>-ACT.md`, titled `# Owner act — <title>`,
 * identity `<identity stem>-<date>`, binding the record's exact bytes. */
const SITTING_INSTANCES = '.syzygy/governance/contracts/candidates/dossier-local-agent-acts/instances';
const sittingForm = (stem: string, title: string, type: string, identityStem: string, artifact: string, scope: string, more: { readonly bound?: readonly string[]; readonly stems?: readonly string[] } = {}): DigestBoundActForm => Object.freeze({
  file: `DOSSIER-LOCAL-AGENT-${stem}-ACT.md`,
  title: `# Owner act — ${title}`,
  type,
  identity: (date: string) => `${identityStem}-${date}`,
  artifact: `${SITTING_INSTANCES}/${artifact}`,
  stems: Object.freeze([`dossier-local-agent-${stem.toLowerCase()}`, identityStem.toLowerCase(), ...(more.stems ?? [])]),
  scope,
  ...(more.bound === undefined ? {} : { bound: Object.freeze([...more.bound]) }),
});

/** D9 was adopted by the owner's words, logged in the doctrine amendment log with no digest, which RFC3-16(a) does not read as an
 * act. Its in-force record binds the whole-file bytes of `security.md` and `v1.md`, and the act binds the record: D9 counts only
 * while the act binds the record's bytes and both files still hash to the record's rows. */
export const D9_ACT_FORM: DigestBoundActForm = sittingForm('D9-IN-FORCE', 'D9 in force for operator-agent runs', 'bind-exact-bytes',
  'D9-IN-FORCE-OPERATOR-AGENT', 'in-force/D9-IN-FORCE-RECORD.md', 'REQ-polaris-generation-033\'s execution rule only',
  { bound: ['.syzygy/governance/doctrine/security.md', '.syzygy/governance/doctrine/v1.md'] });
/** Item 1 of the owner direction POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05 (the RFC7-20 reading), in force the same way over the
 * direction file's bytes. */
export const RFC7_20_RULING_ACT_FORM: DigestBoundActForm = sittingForm('RFC7-20-READING-IN-FORCE', 'the owner\'s RFC7-20 reading in force for operator-agent runs',
  'bind-exact-bytes', 'RFC7-20-READING-IN-FORCE-OPERATOR-AGENT', 'in-force/RFC7-20-READING-IN-FORCE-RECORD.md',
  'item 1 of the direction, for REQ-polaris-generation-033\'s draft-layer rule only', { bound: ['.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md'] });
/** Row 3: the project-input statement that no kernel evidence drawer exists, per repository id. */
export const DRAWER_FORMS: Readonly<Record<string, DigestBoundActForm>> = Object.freeze({
  'redis-redis': sittingForm('REDIS-NO-EVIDENCE-DRAWER', 'no kernel evidence drawer for redis/redis', 'state-project-input', 'NO-EVIDENCE-DRAWER-REDIS', 'redis/NO-EVIDENCE-DRAWER-STATEMENT.md',
    'the drawer half of REQ-polaris-generation-033\'s governed predicate for this one repository'),
});
/** Rows 3a and 3b: the per-project agent-provider statements, per repository id, each naming the tool (its run-configuration id and
 * the name its record's `Agent tool:` line opens with) and the provider it consents to. A statement's record says it is withdrawn by
 * "a later owner act naming this record", so the sweep reads its Record ID and its Subject as well as the act's own stems. */
export interface StatementForm { readonly agentTool: string; readonly toolName: string; readonly provider: string; readonly recordId: string; readonly form: DigestBoundActForm }
const statementForm = (agentTool: string, toolName: string, provider: string, providerName: string, repositoryId: string, stem: string, identityStem: string, artifact: string): StatementForm => {
  const recordId = `AGENT-PROVIDER-${repositoryId}-${provider}`;
  return Object.freeze({
    agentTool, toolName, provider, recordId,
    form: sittingForm(stem, `agent-provider statement for ${repositoryId.replace('-', '/')}: ${toolName} with ${providerName}`, 'consent-agent-provider', identityStem, artifact,
      'operator-agent runs over this one repository with this one tool and provider',
      { stems: [recordId.toLowerCase(), `project:syzygy, repository:${repositoryId}, agent-provider:${provider}`] }),
  });
};
export const STATEMENT_FORMS: Readonly<Record<string, readonly StatementForm[]>> = Object.freeze({
  'redis-redis': Object.freeze([
    statementForm('claude-code', 'Claude Code', 'anthropic', 'Anthropic', 'redis-redis', 'REDIS-AGENT-ANTHROPIC', 'AGENT-PROVIDER-REDIS-ANTHROPIC', 'redis/AGENT-PROVIDER-STATEMENT-ANTHROPIC.md'),
    statementForm('codex', 'Codex', 'openai', 'OpenAI', 'redis-redis', 'REDIS-AGENT-OPENAI', 'AGENT-PROVIDER-REDIS-OPENAI', 'redis/AGENT-PROVIDER-STATEMENT-OPENAI.md'),
  ]),
});

const notEstablished = (what: string): GateState => ({
  state: 'absent',
  why: `no owner-act record binds a digest of ${what}, so the act cross-check of RFC3-16(a) cannot establish it in force; a status word, a log row or a file's presence is not read as one`,
});

/** The record's one `<label>: \`value\`` field, or null when it has none or several. */
const field = (text: string, label: string): string | null => {
  const all = [...text.matchAll(new RegExp(`^${label}: \`([^\`\\n]+)\`$`, 'gm'))];
  return all.length === 1 ? all[0]![1]! : null;
};

/** The drawer statement an in-force act puts in the project input for `repositoryId`. Unstated, with the reader's reason, unless the
 * act binds the record's bytes, is in force and the record states no drawer for exactly this subject. */
function drawerStatement(state: ActState<DigestBoundAct>, repositoryId: string): DrawerStatement {
  if (state.state === 'absent' && state.why.startsWith('no owner-act record ')) return { stated: false, why: UNSTATED_WHY };
  if (state.state !== 'ok') return { stated: false, why: `the project-input statement for this subject is not in force: ${state.why}` };
  const text = state.artifactText, recordId = field(text, 'Record ID'), version = field(text, 'Record version');
  const states = text.split('\n').filter(line => line.startsWith('Statement: ')).join('\n') === 'Statement: no kernel evidence drawer (RFC-0006 §3.5) exists for this';
  if (recordId === null || version === null || field(text, 'Subject') !== `(project:syzygy, repository:${repositoryId})` || !states) {
    return { stated: false, why: `the record ${state.act.identity} binds does not state, for exactly this subject, that no kernel evidence drawer exists` };
  }
  return { stated: true, drawer: 'absent', record: `${recordId}@${version}` };
}

/** One provider statement as the gate reads it; null when no act is recorded or in force yet, so an unrecorded statement is no
 * statement at all. A record whose act does not bind it, or whose bytes do not name exactly this subject, tool and provider,
 * carries `act: null`; one that another decisions file names (a withdrawal, or a form the reader does not define) is withdrawn. */
function providerStatement(state: ActState<DigestBoundAct>, repositoryId: string, s: StatementForm): ProviderStatementRecord | null {
  if (state.state === 'absent') return null;
  const { agentTool, provider, recordId } = s;
  const unbound: ProviderStatementRecord = { recordId, version: 'unestablished', digest: '', agentTool, provider, contentClasses: [], withdrawn: false, act: null };
  if (state.state === 'refused' && state.namedBy !== undefined) return { ...unbound, withdrawn: true };
  if (state.state !== 'ok') return unbound;
  const text = state.artifactText, version = field(text, 'Record version');
  const lines = text.split('\n'), at = lines.findIndex(line => line.startsWith('Content classes the provider may receive'));
  const classes: string[] = [];
  for (const line of at < 0 ? [] : lines.slice(at + 2)) {
    const m = /^- `([a-z-]+)`$/.exec(line);
    if (m === null) break;
    classes.push(m[1]!);
  }
  const tools = lines.filter(line => line.startsWith('Agent tool: '));
  if (field(text, 'Record ID') !== recordId || version === null || field(text, 'Subject') !== `(project:syzygy, repository:${repositoryId}, agent-provider:${provider})`
    || tools.length !== 1 || !tools[0]!.startsWith(`Agent tool: ${s.toolName}, `)) return unbound;
  return { recordId, version, digest: state.artifactDigest, agentTool, provider, contentClasses: classes, withdrawn: false, act: { identity: state.act.identity, inForceAt: state.act.recordedAt } };
}

/** The statement gate: exactly one in-force statement for the subject that names the run's declared `agentTool` with its `provider`,
 * and at least one content class. A statement for the same provider under another tool, or the same tool with another provider, is
 * no consent to this pair (SEC-2: the record consents to one tool with one provider). */
export function providerStatementGate(records: readonly ProviderStatementRecord[], agentTool: string, provider: string, now: number): GateState {
  const pair = `the agent tool ${agentTool} with the provider ${provider}`;
  const named = records.filter(r => r.agentTool === agentTool && r.provider === provider);
  const live = named.filter(r => !r.withdrawn && r.act !== null && r.act.inForceAt <= now && r.contentClasses.length > 0);
  if (live.length === 1) return { state: 'ok', record: `${live[0]!.recordId}@${live[0]!.version}` };
  if (live.length > 1) return { state: 'refused', why: `${live.length} in-force per-project statements name ${pair}; which one governs is ambiguous` };
  if (named.length === 0) {
    const others = records.filter(r => r.agentTool === agentTool || r.provider === provider).map(r => `${r.recordId}@${r.version} names ${r.agentTool} with ${r.provider}`);
    return { state: 'absent', why: `no per-project statement names the operator's agent tool ${agentTool} with the provider ${provider}${others.length === 0 ? '' : ` (${others.join('; ')})`}` };
  }
  const why = named.map(r => `${r.recordId}@${r.version} ${r.withdrawn ? 'is withdrawn' : r.act === null ? 'has no owner act binding its bytes' : r.act.inForceAt > now ? 'is not in force yet' : 'names no content class'}`);
  return { state: 'absent', why: `no per-project statement naming ${pair} is in force: ${why.join('; ')}` };
}

export interface PackageGateSourceOptions {
  readonly root: string;
  readonly now: () => number;
  readonly fs?: PackageReaderFs;
  readonly projectInput?: ProjectInputSource;
  readonly providerStatements?: ProviderStatementSource;
  readonly registryForm?: VersionedSignoffForm;
  readonly d9Form?: DigestBoundActForm | null;
  readonly rfc720Form?: DigestBoundActForm | null;
}

/** The gate sources over one Syzygy checkout, every one an act cross-check through the consent package's readers: the observation
 * consents, the policy chain, the registry entry's version-tagged sign-off, D9 and the RFC7-20 reading, and the drawer and provider
 * statements of the local-agent sitting. With no act recorded each states nothing: D9 and the reading are not established, the
 * drawer is unstated and no statement exists. `projectInput` and `providerStatements` replace the package sources (tests). */
export function createPackageGateSources(options: PackageGateSourceOptions): GateSources {
  const fsOption = options.fs === undefined ? {} : { fs: options.fs };
  const port = createPackageAdmissionRecordsPort({ root: options.root, now: options.now, ...fsOption });
  const read = (form: DigestBoundActForm) => readDigestBoundActState({ root: options.root, now: options.now(), form, ...fsOption });
  const crossCheck = async (form: DigestBoundActForm | null | undefined, what: string): Promise<GateState> => {
    if (form === null || form === undefined) return notEstablished(what);
    const state = await read(form);
    if (state.state === 'absent' && state.why.startsWith('no owner-act record ')) return notEstablished(what);
    return state.state === 'ok' ? { state: 'ok', record: state.act.identity } : { state: state.state, why: state.why };
  };
  const projectInput: ProjectInputSource = {
    drawerFor: async repositoryId => {
      const form = Object.hasOwn(DRAWER_FORMS, repositoryId) ? DRAWER_FORMS[repositoryId]! : null;
      return form === null ? NO_PROJECT_INPUT.drawerFor(repositoryId) : drawerStatement(await read(form), repositoryId);
    },
  };
  const providerStatements: ProviderStatementSource = {
    statementsFor: async repositoryId => {
      const forms = Object.hasOwn(STATEMENT_FORMS, repositoryId) ? STATEMENT_FORMS[repositoryId]! : [];
      const found = await Promise.all(forms.map(async s => providerStatement(await read(s.form), repositoryId, s)));
      return found.filter((r): r is ProviderStatementRecord => r !== null);
    },
  };
  return {
    recordsRoot: options.root,
    repositoryIdsFor: url => port.repositoryIdsFor(url),
    ...(port.consentAbsenceFor === undefined ? {} : { consentAbsenceFor: port.consentAbsenceFor }),
    consentedRevisionsFor: repositoryId => port.consentedRevisionsFor(repositoryId),
    observationConsentFor: async (repositoryId, revision) => {
      const answer = await port.check({ kind: 'observation-consent', repositoryId, revision });
      return answer.satisfied ? { satisfied: true, record: answer.record } : { satisfied: false, why: answer.why };
    },
    registryEntry: async () => {
      const state = await readVersionedSignoffState({ root: options.root, now: options.now(), form: options.registryForm ?? LOCAL_AGENT_GIT_SOURCE_SIGNOFF_FORM, ...fsOption });
      if (state.state !== 'ok') return { state: state.state, why: state.why };
      return registryEntryUsable(state.artifactText, state.act.identity);
    },
    screeningPolicy: async () => {
      const state = await readPolicyActChain({ root: options.root, now: options.now(), ...fsOption });
      return state.state === 'ok' ? { state: 'ok', record: state.final.identity } : state;
    },
    d9: () => crossCheck(options.d9Form === undefined ? D9_ACT_FORM : options.d9Form, 'the D9 text (SEC-3 amendment)'),
    rfc720Ruling: () => crossCheck(options.rfc720Form === undefined ? RFC7_20_RULING_ACT_FORM : options.rfc720Form, 'the RFC7-20 reading (POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05, item 1)'),
    projectInput: options.projectInput ?? projectInput,
    providerStatements: options.providerStatements ?? providerStatements,
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
