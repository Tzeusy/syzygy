import { createHash } from 'node:crypto';
import { readFile as nodeReadFile, readdir as nodeReaddir } from 'node:fs/promises';
import path from 'node:path';
import { AdmissionRecordError, COMMIT_OBJECT_ID, type AdmissionRecord, type AdmissionRecordReader } from './admission-record.js';
import { inForceRecords } from './consent-ports.js';

/** Reads admission records from the public-repo-admission package layout.
 *
 * A candidate instance record under `instances/**` binds nothing and is never
 * returned. A record exists only when an owner act record
 * (`.syzygy/governance/decisions/PUBLIC-REPO-ADMISSION-*-ACT.md`) names it by
 * path and digest. If the instance bytes no longer hash to the act's digest
 * the record comes back with `inForceAt: null` (the act bound other bytes). The
 * instant is the act record's `Recorded at (UTC)` line when it has one; a record
 * with only a date is in force from the start of the next UTC day (fail-closed). A decisions file about the
 * package that is neither an act record nor the owner-answers direction is
 * unknown (a withdrawal form is not defined yet): the whole read is refused. */

export const DECISIONS_DIR = '.syzygy/governance/decisions';
export const INSTANCES_DIR = '.syzygy/governance/contracts/candidates/public-repo-admission/instances';
export const EGRESS_V2_INSTANCE = '.syzygy/governance/contracts/candidates/public-egress-v2/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md';
/** A recorder's act form for an admission record: the one file it writes, its title, the identity it renders and the one instance it
 * binds (scripts/record_public_repo_admission_acts.py, scripts/record_public_egress_v2_act.py). The list is closed: a decisions file
 * about the package that is not one of these (or the pinned owner-answers direction) refuses the read, and an act whose type,
 * identity, title or artifact is not its form's is refused. */
export interface AdmissionActForm { readonly file: string; readonly title: string; readonly type: 'consent-observation' | 'consent-egress'; readonly identity: (date: string) => string; readonly artifact: string; readonly version: 1 | 2 }
export const ADMISSION_ACT_FORMS: readonly AdmissionActForm[] = Object.freeze(([
  { file: 'PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md', title: '# Owner act — psf/requests public-repository observation consent', type: 'consent-observation', identity: d => `PUBLIC-OBS-REQUESTS-${d}`, artifact: `${INSTANCES_DIR}/requests/OBSERVATION-CONSENT.md`, version: 1 },
  { file: 'PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md', title: '# Owner act — redis/redis public-repository observation consent', type: 'consent-observation', identity: d => `PUBLIC-OBS-REDIS-${d}`, artifact: `${INSTANCES_DIR}/redis/OBSERVATION-CONSENT.md`, version: 1 },
  { file: 'PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md', title: '# Owner act — public-target egress consent to Anthropic', type: 'consent-egress', identity: d => `PUBLIC-EGRESS-ANTHROPIC-${d}`, artifact: `${INSTANCES_DIR}/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`, version: 1 },
  { file: 'PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md', title: '# Owner act — public-target egress consent to Anthropic, version 2', type: 'consent-egress', identity: d => `PUBLIC-EGRESS-ANTHROPIC-V2-${d}`, artifact: EGRESS_V2_INSTANCE, version: 2 },
] as readonly AdmissionActForm[]).map(form => Object.freeze(form)));
/** The v2 record's revocation line, exactly: it replaces version 0.1.0-candidate.7 of the same record once its own act is in force (RFC5-13). */
const V2_REVOCATION = 'Proposed revocation state: active; supersedes version 0.1.0-candidate.7 of this record, if an act over that version is in force, from the effective instant of the act on this version (prospective, RFC5-13); with none in force it supersedes nothing';
const V2_SUPERSEDES = 'PUBLIC-EGRESS-anthropic@0.1.0-candidate.7';
/** The one plain owner direction in the package's name space, pinned by name and digest: it performs no act. Any other
 * file (or these bytes edited) is an unknown form and refuses the whole read. */
const OWNER_ANSWERS_FILE = 'PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md';
const OWNER_ANSWERS_SHA256 = '549a746e108d06581ac7e0a653023692f7f7664075c81e5502918322feb5145c';
const DAY_MS = 86_400_000;

export interface PackageReaderFs {
  readonly readdir: (dir: string) => Promise<readonly string[]>;
  readonly readFile: (file: string) => Promise<string>;
}
const nodeFs: PackageReaderFs = { readdir: dir => nodeReaddir(dir), readFile: file => nodeReadFile(file, 'utf8') };

const refuse = (): never => { throw new AdmissionRecordError('invalid-records'); };
const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const one = (text: string, re: RegExp): string => { const all = [...text.matchAll(re)]; return all.length === 1 ? all[0]![1]! : refuse(); };

interface Act { readonly type: 'observation' | 'egress'; readonly inForce: number; readonly artifact: string; readonly digest: string; readonly version: 1 | 2 }

function parseAct(text: string, form: AdmissionActForm): Act {
  if (!text.startsWith(`${form.title}\n`)) refuse();
  const type = one(text, /^Act type: `(consent-observation|consent-egress)`$/gm);
  const date = one(text, /^Date: (\d{4}-\d{2}-\d{2})$/gm);
  const at = Date.parse(`${date}T00:00:00Z`);
  if (!Number.isSafeInteger(at) || new Date(at).toISOString().slice(0, 10) !== date) refuse();
  if (type !== form.type || one(text, /^Act identity: `([^`\n]+)`$/gm) !== form.identity(date)) refuse();
  const artifact = one(text, /^Artifact identity: `([^`\n]+)`$/gm);
  if (artifact !== form.artifact) refuse();
  const digest = one(text, /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gm);
  one(text, /^Project identity: `(project:syzygy)`$/gm);
  return { type: type === 'consent-observation' ? 'observation' : 'egress', inForce: actInstant(text, date, at), artifact, digest, version: form.version };
}

/** The act's effective instant: the `Recorded at (UTC)` line when the record has exactly one (whole seconds, same
 * calendar day as `Date:`), else the start of the next UTC day (a date alone is not an instant: fail-closed). */
function actInstant(text: string, date: string, startOfDay: number): number {
  const prose = outsideFences(text);
  const loose = [...prose.matchAll(/^\s*recorded at\b/gim)];
  // A date-only record may carry no such line at all; one that carries it only inside a fence is not date-only, it is unreadable.
  if (loose.length === 0) return /^\s*recorded at\b/im.test(text) ? refuse() : startOfDay + DAY_MS;
  const lines = [...prose.matchAll(/^Recorded at \(UTC\): (\S+)$/gm)];
  if (loose.length !== 1 || lines.length !== 1) return refuse();   // any other spelling, indentation or repeat is not an instant
  const m = /^(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}:\d{2}Z$/.exec(lines[0]![1]!);
  const at = m === null ? NaN : Date.parse(lines[0]![1]!);
  if (m === null || m[1] !== date || !Number.isSafeInteger(at) || new Date(at).toISOString().slice(0, 19) + 'Z' !== lines[0]![1]) return refuse();
  return at;
}

/** The text with every fenced code block blanked (a fence opens and closes on a line of three or more backticks or tildes, up to
 * three spaces in; an unclosed fence runs to the end). Line count is kept. */
function outsideFences(text: string): string {
  let open: string | null = null;
  return text.split('\n').map(line => {
    const m = /^ {0,3}(`{3,}|~{3,})/.exec(line);
    if (open === null) { if (m !== null) { open = m[1]![0]!; return ''; } return line; }
    if (m !== null && m[1]![0] === open) open = null;
    return '';
  }).join('\n');
}

function bullets(text: string, heading: RegExp): string[] {
  const start = text.search(heading);
  if (start < 0) return refuse();
  const lines = text.slice(start).split('\n').slice(1);
  const out: string[] = [];
  for (const line of lines.slice(lines.findIndex(l => l.startsWith('- ')))) {
    if (!line.startsWith('- ')) break;
    out.push(line.slice(2));
  }
  return out;
}

function parseInstance(text: string, act: Act, inForceAt: number | null): AdmissionRecord {
  const recordId = one(text, /^Record ID: `([^`\n]+)`$/gm);
  const version = one(text, /^Record version: `([^`\n]+)`$/gm);
  const subject = one(text, /^Subject: `([^`\n]+)`$/gm);
  // The revocation line is exactly the form's (the first versions supersede nothing; version 2 supersedes version 1 of its record): any other successor form is refused rather than guessed.
  const revocations = [...text.matchAll(/^Proposed revocation state: .*$/gm)].map(m => m[0]);
  if (revocations.length !== 1 || revocations[0] !== (act.version === 2 ? V2_REVOCATION : 'Proposed revocation state: active; supersedes no earlier consent')) refuse();
  if (act.version === 2 && (act.type !== 'egress' || recordId !== 'PUBLIC-EGRESS-anthropic' || version !== '0.2.0-candidate.1')) refuse();
  const base = { recordId, version, digest: act.digest, inForceAt, withdrawnAt: null, supersedes: act.version === 2 ? V2_SUPERSEDES : null, project: 'project:syzygy' } as const;
  if (act.type === 'observation') {
    const m = /^\(project:syzygy, repository:([a-z0-9][a-z0-9-]*)\)$/.exec(subject) ?? refuse();
    const revisions = [...text.matchAll(/^\| `[^`\n]+` \| `([0-9a-f]+)` \|$/gm)].map(r => r![1]!);
    if (revisions.length === 0 || !revisions.every(id => COMMIT_OBJECT_ID.test(id))) refuse();
    return Object.freeze({ ...base, class: 'observation', repositoryId: m![1]!, providerId: null, admittedRevisions: Object.freeze(revisions), admittedRepositories: Object.freeze([]), contentClasses: Object.freeze([]) });
  }
  const m = /^\(project:syzygy, provider:([a-z0-9][a-z0-9-]*)\)$/.exec(subject) ?? refuse();
  const repositories = [...text.matchAll(/^- `\(project:syzygy, repository:([a-z0-9][a-z0-9-]*)\)`$/gm)].map(r => r![1]!);
  const classes = bullets(text, /^Permitted content classes/m).map(line => /^`([a-z-]+)`$/.exec(line)?.[1] ?? refuse());
  if (repositories.length === 0 || classes.length === 0) refuse();
  return Object.freeze({ ...base, class: 'egress', repositoryId: null, providerId: m![1]!, admittedRevisions: Object.freeze([]), admittedRepositories: Object.freeze(repositories), contentClasses: Object.freeze(classes) });
}

export function createPackageAdmissionReader(options: { readonly root: string; readonly fs?: PackageReaderFs }): AdmissionRecordReader {
  const fs = options.fs ?? nodeFs;
  return {
    read: async () => {
      let names: readonly string[];
      try { names = await fs.readdir(path.join(options.root, DECISIONS_DIR)); } catch { return refuse(); }
      const records: AdmissionRecord[] = [];
      for (const name of [...names].sort()) {
        if (!name.startsWith('PUBLIC-REPO-ADMISSION-') && !name.startsWith('PUBLIC-EGRESS-V2-')) continue;
        if (name === OWNER_ANSWERS_FILE) {
          let direction: string;
          try { direction = await fs.readFile(path.join(options.root, DECISIONS_DIR, name)); } catch { return refuse(); }
          if (sha256(direction) !== OWNER_ANSWERS_SHA256) refuse();
          continue;
        }
        const form = ADMISSION_ACT_FORMS.find(f => f.file === name);
        if (form === undefined) refuse();
        let act: Act;
        try { act = parseAct(await fs.readFile(path.join(options.root, DECISIONS_DIR, name)), form!); } catch { return refuse(); }
        let artifact: string;
        try { artifact = await fs.readFile(path.join(options.root, act.artifact)); } catch { return refuse(); }
        records.push(parseInstance(artifact, act, sha256(artifact) === act.digest ? act.inForce : null));
      }
      return Object.freeze(records);
    },
  };
}

/** The public-source screening-scope policy (an `approve-policy` act over the
 * policy file). It counts only while the policy file's current bytes hash to the
 * act's digest AND declare a `publicSourceScope` object: the 2026-09 policy acts
 * approved the Butlers-only policy and satisfy nothing here. The act record's
 * file name is not keyed on: every decisions record naming the policy path is
 * read, and one that names it without a readable act form refuses the read. */
export const POLICY_PATH = '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json';
export interface PolicyActRecord { readonly actIdentity: string; readonly digest: string; readonly inForceAt: number }
export interface PolicyActReader { readonly read: () => Promise<readonly PolicyActRecord[]> }

/** A recorder's act form for the screening-scope policy: the one file it writes, the title and the identity it renders
 * (`scripts/record_public_source_screening_scope_act.py`). The list is closed; a later recorder (scope v2) is registered here by
 * a reviewed change, never discovered. */
export interface PolicyActForm { readonly file: string; readonly title: string; readonly identity: (date: string) => string }
export const POLICY_ACT_FORMS: readonly PolicyActForm[] = Object.freeze([Object.freeze({
  file: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md',
  title: '# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope)',
  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-${date}`,
})]);
export const POLICY_ACT_FILE = POLICY_ACT_FORMS[0]!.file;
/** Earlier acts that name the same policy file for its Butlers-only content, pinned by name and digest: they bind other bytes
 * and count for nothing here, and an edited copy (a forged withdrawal, say) refuses the read. */
const HISTORICAL_POLICY_ACTS: ReadonlyMap<string, string> = new Map([
  ['PWB-SECRET-CLASSIFICATION-POLICY-ACT.md', 'e02c0e6fbe408c4aac7d60f86e116bc8d4b79672a0c3a4dd4d6cf1a9f6bf59bb'],
  ['PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md', 'e766803dafcfbf0c5d40fdc499af7a83239864afd2a09696a7d7a21f81618a0a'],
  ['PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md', '178fcd57c4afde5ff457e6928a73089a2567f02ff8ef95d7efe05234f88e9988'],
]);

export function createPackagePolicyReader(options: { readonly root: string; readonly fs?: PackageReaderFs }): PolicyActReader {
  const fs = options.fs ?? nodeFs;
  return {
    read: async () => {
      let policy: string;
      let names: readonly string[];
      try { policy = await fs.readFile(path.join(options.root, POLICY_PATH)); names = await fs.readdir(path.join(options.root, DECISIONS_DIR)); } catch { return refuse(); }
      let scope: unknown;
      try { scope = (JSON.parse(policy) as { publicSourceScope?: unknown }).publicSourceScope; } catch { return refuse(); }
      const naming = `Artifact identity: \`${POLICY_PATH}\``;
      const records: PolicyActRecord[] = [];
      for (const name of [...names].sort()) {
        if (!name.endsWith('.md')) continue;
        let text: string;
        try { text = await fs.readFile(path.join(options.root, DECISIONS_DIR, name)); } catch { return refuse(); }
        const names_it = text.split('\n').some(line => line === naming);
        const form = POLICY_ACT_FORMS.find(f => f.file === name);
        if (form === undefined) {
          // Another record that names the policy as its artifact is a known historical act (by digest) or an unknown form: refuse the unknown.
          const pinned = HISTORICAL_POLICY_ACTS.get(name);
          if (pinned !== undefined) { if (sha256(text) !== pinned) refuse(); continue; }
          if (names_it) refuse();
          continue;
        }
        if (!text.startsWith(`${form.title}\n`) || !names_it) refuse();
        const act = { type: one(text, /^Act type: `([a-z-]+)`$/gm), identity: one(text, /^Act identity: `([^`\n]+)`$/gm), digest: one(text, /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gm), date: one(text, /^Date: (\d{4}-\d{2}-\d{2})$/gm) };
        one(text, /^Project identity: `(project:syzygy)`$/gm);
        one(text, /^Provenance state: `(owner-adopted \(bootstrap, uncorrelated\))`/gm);
        if (act.type !== 'approve-policy' || act.identity !== form.identity(act.date)) refuse();
        const at = Date.parse(`${act.date}T00:00:00Z`);
        if (!Number.isSafeInteger(at)) refuse();
        const inForceAt = actInstant(text, act.date, at);
        // The act binds the policy bytes it names: stale bytes or a policy that declares no public-source scope do not count.
        if (act.digest !== sha256(policy) || scope === null || typeof scope !== 'object' || Array.isArray(scope)) continue;
        records.push(Object.freeze({ actIdentity: act.identity, digest: act.digest, inForceAt }));
      }
      return Object.freeze(records);
    },
  };
}

/** Structurally the poc:dossier trigger's `AdmissionRecordsPort`. */
export interface AdmissionRequirementLike { readonly kind: 'observation-consent' | 'public-source-policy' | 'egress-consent'; readonly repositoryId: string; readonly revision: string }
export type AdmissionAnswerLike = { readonly satisfied: true; readonly record: string } | { readonly satisfied: false; readonly why: string };
export interface AdmissionRecordsPortLike {
  readonly source: string;
  readonly check: (requirement: AdmissionRequirementLike & Record<string, unknown>) => Promise<AdmissionAnswerLike>;
}

/** Answers each requirement from the reader, fresh on every call, with the same
 * in-force polarity as the consent ports. The public-source policy requirement
 * needs the `policy` reader and is otherwise never satisfied. */
/** Both readers over one checkout, as the dossier trigger wires them. */
export function createPackageAdmissionRecordsPort(options: { readonly root: string; readonly now: () => number; readonly fs?: PackageReaderFs }): AdmissionRecordsPortLike {
  const fsOption = options.fs === undefined ? {} : { fs: options.fs };
  return createAdmissionRecordsPort({ reader: createPackageAdmissionReader({ root: options.root, ...fsOption }), policy: createPackagePolicyReader({ root: options.root, ...fsOption }), now: options.now });
}

export function createAdmissionRecordsPort(options: { readonly reader: AdmissionRecordReader; readonly policy?: PolicyActReader; readonly now: () => number }): AdmissionRecordsPortLike {
  return {
    source: 'public-repo-admission act records (owner acts over the instance records)',
    check: async requirement => {
      if (requirement.kind === 'public-source-policy') {
        if (options.policy === undefined) return { satisfied: false, why: 'no record found: no policy act reader is wired' };
        try {
          const now = options.now();
          const hit = (await options.policy.read()).find(r => r.inForceAt <= now);
          return hit === undefined ? { satisfied: false, why: 'no record found: no owner approve-policy act covers the current public-source screening scope' } : { satisfied: true, record: hit.actIdentity };
        } catch { return { satisfied: false, why: 'no record found: the policy act records could not be read' }; }
      }
      let live: readonly AdmissionRecord[];
      try { live = inForceRecords(await options.reader.read(), options.now()); } catch { return { satisfied: false, why: 'no record found: the admission act records could not be read' }; }
      const hit = requirement.kind === 'observation-consent'
        ? live.find(r => r.class === 'observation' && r.repositoryId === requirement.repositoryId && r.admittedRevisions.includes(requirement.revision))
        : live.find(r => r.class === 'egress' && r.providerId === 'anthropic' && r.admittedRepositories.includes(requirement.repositoryId));
      return hit === undefined
        ? { satisfied: false, why: `no record found: no owner act puts a ${requirement.kind} for ${requirement.repositoryId} in force${requirement.kind === 'observation-consent' ? ` at revision ${requirement.revision}` : ''}` }
        : { satisfied: true, record: `${hit.recordId}@${hit.version}` };
    },
  };
}
