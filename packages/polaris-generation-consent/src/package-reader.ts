import { createHash } from 'node:crypto';
import { readFile as nodeReadFile, readdir as nodeReaddir } from 'node:fs/promises';
import path from 'node:path';
import { AdmissionRecordError, COMMIT_OBJECT_ID, type AdmissionRecord, type AdmissionRecordReader } from './admission-record.js';
import { inForceRecords } from './consent-ports.js';

/** Reads admission records from the public-repo-admission package layout.
 *
 * A candidate instance record under `instances/**` binds nothing and is never
 * returned. A record exists only when an owner act record in the closed list
 * `ADMISSION_ACT_FORMS` names it by path and digest. If the instance bytes no
 * longer hash to the act's digest the record comes back with `inForceAt: null`
 * (the act bound other bytes). The instant is the act record's one
 * `Recorded at (UTC)` line; a record without it is unreadable and refuses the
 * read. Every field is read from prose only: a line inside a code fence never
 * counts, and a field that appears only there (or that differs between the whole
 * file and its prose) refuses the read. Every file under the decisions directory,
 * at any depth, is looked at: one that is outside the closed list and the pins
 * but names an admission artifact, act identity or record id (a withdrawal in
 * any spelling) refuses the whole read. */

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

/** The text with every fenced code block and every HTML comment blanked (a fence opens and closes on a line of three or more
 * backticks or tildes, up to three spaces in; an unclosed fence or comment runs to the end). Line count is kept. */
function outsideFences(text: string): string {
  let open: string | null = null;
  const unfenced = text.split('\n').map(line => {
    const m = /^ {0,3}(`{3,}|~{3,})/.exec(line);
    if (open === null) { if (m !== null) { open = m[1]![0]!; return ''; } return line; }
    if (m !== null && m[1]![0] === open) open = null;
    return '';
  }).join('\n');
  return unfenced.replace(/<!--[\s\S]*?(?:-->|$)/g, comment => comment.replace(/[^\n]/g, ''));
}
/** The one capture of `re` in the prose. Refuses when it is absent, repeated, or counts differently once fences are ignored (a field
 * that is partly or wholly inside a fence is not a field). */
const one = (text: string, re: RegExp): string => {
  const all = [...text.matchAll(re)], prose = [...outsideFences(text).matchAll(re)];
  return all.length === 1 && prose.length === 1 ? prose[0]![1]! : refuse();
};
/** Unicode-folded, case-folded, dash-folded: the spelling a reader compares names and field values in. */
const fold = (value: string): string => value.normalize('NFKC').replace(/[\u2010-\u2015\u2212\uFE58\uFE63\uFF0D]/gu, '-').toLowerCase();

async function walk(fs: PackageReaderFs, dir: string, prefix = '', depth = 0, found: string[] = []): Promise<string[]> {
  if (depth > 6) return refuse();
  let names: readonly string[];
  try { names = await fs.readdir(dir); } catch { return refuse(); }
  for (const name of [...names].sort()) {
    let children: readonly string[] | null = null;
    try { children = await fs.readdir(path.join(dir, name)); } catch { children = null; }   // a file, not a directory
    if (children !== null) await walk(fs, path.join(dir, name), `${prefix}${name}/`, depth + 1, found); else found.push(`${prefix}${name}`);
    if (found.length > 5000) return refuse();
  }
  return found;
}

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
  return { type: type === 'consent-observation' ? 'observation' : 'egress', inForce: actInstant(text, date), artifact, digest, version: form.version };
}

/** The act's effective instant: its one `Recorded at (UTC)` line (whole seconds, the same calendar day as `Date:`). The recorders
 * always write it; a record without one, or with a second or oddly spelled one, is unreadable. */
function actInstant(text: string, date: string, label = 'Recorded at \\(UTC\\)', loose = /^\s*recorded at\b/gim): number {
  const prose = outsideFences(text);
  if ([...text.matchAll(loose)].length !== 1 || [...prose.matchAll(loose)].length !== 1) return refuse();   // absent, repeated, or only in a fence
  const value = one(text, new RegExp(`^${label}: (\\S+)$`, 'gm'));
  const m = /^(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}:\d{2}Z$/.exec(value);
  const at = m === null ? NaN : Date.parse(value);
  if (m === null || m[1] !== date || !Number.isSafeInteger(at) || new Date(at).toISOString().slice(0, 19) + 'Z' !== value) return refuse();
  return at;
}

/** The act's one `Supersession / revocation:` field with its wrapped continuation lines (up to the next blank line) joined by a space;
 * '' when the act has none. A repeated field, or one that counts differently once fences and comments are ignored, refuses. */
function supersessionText(text: string): string {
  const re = /^Supersession \/ revocation:/gm;
  const lines = outsideFences(text).split('\n'), at = lines.map((line, i) => (re.test(line) ? i : -1)).filter(i => i >= 0);
  re.lastIndex = 0;
  if (at.length > 1 || [...text.matchAll(re)].length !== at.length) return refuse();
  if (at.length === 0) return '';
  const out: string[] = [];
  for (const line of lines.slice(at[0])) { if (line.trim() === '') break; out.push(line.trim()); }
  return out.join(' ');
}

/** What the strict readers return for one act record: the recorder's head fields, parsed from prose only. */
export interface ParsedAct { readonly file: string; readonly identity: string; readonly type: string; readonly artifact: string; readonly project: string; readonly digest: string; readonly date: string; readonly recordedAt: number; readonly supersession: string; readonly text: string }

function bullets(source: string, heading: RegExp): string[] {
  const text = outsideFences(source);
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

/** The lines of the section that starts at the one heading equal to `heading`, up to the next `## ` heading (prose only). */
function section(source: string, heading: string): string[] {
  const lines = outsideFences(source).split('\n');
  const at = lines.map((line, i) => (line === heading ? i : -1)).filter(i => i >= 0);
  if (at.length !== 1 || source.split('\n').filter(line => line === heading).length !== 1) return refuse();
  const rest = lines.slice(at[0]! + 1), end = rest.findIndex(line => line.startsWith('## '));
  return end < 0 ? rest : rest.slice(0, end);
}

function parseInstance(text: string, act: Act, inForceAt: number | null): AdmissionRecord {
  const recordId = one(text, /^Record ID: `([^`\n]+)`$/gm);
  const version = one(text, /^Record version: `([^`\n]+)`$/gm);
  const subject = one(text, /^Subject: `([^`\n]+)`$/gm);
  // The revocation line is exactly the form's (the first versions supersede nothing; version 2 supersedes version 1 of its record): any other successor form is refused rather than guessed.
  const revocation = one(text, /^(Proposed revocation state: .*)$/gm);
  if (revocation !== (act.version === 2 ? V2_REVOCATION : 'Proposed revocation state: active; supersedes no earlier consent')) refuse();
  if (act.version === 2 && (act.type !== 'egress' || recordId !== 'PUBLIC-EGRESS-anthropic' || version !== '0.2.0-candidate.1')) refuse();
  // Supersession follows the act's instant, not the bytes: a successor whose bytes later drift still replaced its predecessor.
  const base = { recordId, version, digest: act.digest, inForceAt, withdrawnAt: null, supersedes: act.version === 2 ? V2_SUPERSEDES : null, supersessionAt: act.version === 2 ? act.inForce : null, project: 'project:syzygy' } as const;
  if (act.type === 'observation') {
    const m = /^\(project:syzygy, repository:([a-z0-9][a-z0-9-]*)\)$/.exec(subject) ?? refuse();
    // Only the rows of the admitted-revisions table count: the one header, its separator, then consecutive rows.
    one(text, /^(\| Label \| Commit object id \|)$/gm);
    const lines = outsideFences(text).split('\n'), head = lines.indexOf('| Label | Commit object id |');
    if (lines[head + 1] !== '|---|---|') refuse();
    const revisions: string[] = [], labels: string[] = [];
    for (const line of lines.slice(head + 2)) {
      const row = /^\| `([^`\n]+)` \| `([0-9a-f]+)` \|$/.exec(line);
      if (row === null) break;
      labels.push(row[1]!); revisions.push(row[2]!);
    }
    // A label names one commit and a commit has one label: a duplicate of either is ambiguous, so the table is unreadable.
    if (revisions.length === 0 || !revisions.every(id => COMMIT_OBJECT_ID.test(id)) || new Set(labels).size !== labels.length || new Set(revisions).size !== revisions.length) refuse();
    return Object.freeze({ ...base, class: 'observation', repositoryId: m![1]!, providerId: null, admittedRevisions: Object.freeze(revisions), revisionLabels: Object.freeze(labels), admittedRepositories: Object.freeze([]), contentClasses: Object.freeze([]) });
  }
  const m = /^\(project:syzygy, provider:([a-z0-9][a-z0-9-]*)\)$/.exec(subject) ?? refuse();
  // Only the Scope section lists admitted repositories: a bullet naming one elsewhere ("not admitted", an example) is not a grant.
  const repositories = section(text, '## Scope').map(line => /^- `\(project:syzygy, repository:([a-z0-9][a-z0-9-]*)\)`$/.exec(line)?.[1]).filter((id): id is string => id !== undefined);
  const classes = bullets(text, /^Permitted content classes/m).map(line => /^`([a-z-]+)`$/.exec(line)?.[1] ?? refuse());
  if (repositories.length === 0 || classes.length === 0 || new Set(repositories).size !== repositories.length) refuse();
  return Object.freeze({ ...base, class: 'egress', repositoryId: null, providerId: m![1]!, admittedRevisions: Object.freeze([]), revisionLabels: Object.freeze([]), admittedRepositories: Object.freeze(repositories), contentClasses: Object.freeze(classes) });
}

/** The RFC5-14 content-class amendment that version 2's `project-documentation` class depends on (scripts/record_rfc5_project_documentation_act.py):
 * the act record exists in the form the recorder writes, and the installed module hashes to its digest. */
const CLASS_ACT_FILE = 'RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md';
const CLASS_MODULE = '.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md';
const CLASS_TITLE = '# Owner act — RFC5-14 project-documentation content-class amendment';
async function checkClassAct(fs: PackageReaderFs, root: string, files: ReadonlySet<string>, v2At: number): Promise<void> {
  if (!files.has(CLASS_ACT_FILE)) return refuse();
  const hit = await readClassAct(fs, root);
  // The amendment took effect no later than the egress act that relies on it.
  if (hit === null || hit.act.recordedAt > v2At) refuse();
}

/** A decisions file that is outside the closed list and the pins yet names an admission artifact, an act identity or a record id,
 * in any case, spelling or directory, is a withdrawal (or a forgery) in a form this reader does not define. Naming means the folded
 * text of the whole file, prose or not. The one exemption is the aggregate acceptance record the recorders append to: it names every
 * act in tables and headings by design, so only its field lines count. */
const ADMISSION_STEMS = ['public-repo-admission', 'public-egress-v2', 'public-obs-', 'public-egress-anthropic', 'public-egress-'];
const ADMISSION_PATHS = [INSTANCES_DIR, EGRESS_V2_INSTANCE, '.syzygy/governance/contracts/candidates/public-repo-admission/', '.syzygy/governance/contracts/candidates/public-egress-v2/'].map(fold);
const AGGREGATE_RECORD = 'ACCEPTANCE-ACT-RECORD.md';
function namesAdmission(rel: string, text: string): boolean {
  const folded = fold(text);
  if (ADMISSION_STEMS.some(stem => fold(rel).includes(stem))) return true;
  if (rel !== AGGREGATE_RECORD && (ADMISSION_STEMS.some(stem => folded.includes(stem)) || ADMISSION_PATHS.some(p => folded.includes(p)))) return true;
  for (const line of folded.split('\n')) {
    const field = /^\s*(?:[-*>]\s*)?\**\s*(artifact\s+identity|act\s+identity|record\s+id|subject)\s*\**\s*:\s*(.*)$/u.exec(line);
    if (field === null) continue;
    const value = field[2]!;
    if (ADMISSION_PATHS.some(p => value.includes(p)) || ADMISSION_STEMS.some(stem => value.includes(stem))) return true;
  }
  return false;
}

export function createPackageAdmissionReader(options: { readonly root: string; readonly fs?: PackageReaderFs }): AdmissionRecordReader {
  const fs = options.fs ?? nodeFs;
  return {
    read: async () => {
      const files = await walk(fs, path.join(options.root, DECISIONS_DIR));
      const top = new Set(files.filter(f => !f.includes('/')));
      const records: AdmissionRecord[] = [];
      let v2At: number | null = null, v1At: number | null = null;
      for (const rel of files) {
        const known = rel === OWNER_ANSWERS_FILE ? 'pin' : ADMISSION_ACT_FORMS.some(f => f.file === rel) ? 'act' : 'other';
        let text: string;
        try { text = await fs.readFile(path.join(options.root, DECISIONS_DIR, rel)); } catch { return refuse(); }
        if (known === 'pin') { if (sha256(text) !== OWNER_ANSWERS_SHA256) refuse(); continue; }
        if (known === 'other') { if (namesAdmission(rel, text)) refuse(); continue; }
        const form = ADMISSION_ACT_FORMS.find(f => f.file === rel)!;
        let act: Act;
        try { act = parseAct(text, form); } catch { return refuse(); }
        let artifact: string;
        try { artifact = await fs.readFile(path.join(options.root, act.artifact)); } catch { return refuse(); }
        records.push(parseInstance(artifact, act, sha256(artifact) === act.digest ? act.inForce : null));
        if (act.version === 2) v2At = act.inForce; else if (act.type === 'egress') v1At = act.inForce;
      }
      if (v2At !== null) await checkClassAct(fs, options.root, top, v2At);
      // Version 2 replaces version 1 only when its act took effect strictly later: the same instant, or version 2 first, is ambiguous (compared on the acts' instants, whatever the bytes now are).
      if (v2At !== null && v1At !== null && v2At <= v1At) return refuse();
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
}), Object.freeze({
  // scripts/record_public_source_screening_scope_v2_act.py: it supersedes the act above for the same role; only the one whose digest
  // is the current policy bytes counts, so the first goes quiet once the policy carries version 2.
  file: 'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md',
  title: '# Owner act — Polaris Butlers secret-classification policy approval (public-source screening scope, version 2)',
  identity: (date: string) => `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-APPROVAL-${date}`,
})]);
export const POLICY_ACT_FILE = POLICY_ACT_FORMS[0]!.file;
/** Earlier acts that name the same policy file for its Butlers-only content, pinned by name and digest: they bind other bytes
 * and count for nothing here, and an edited copy (a forged withdrawal, say) refuses the read. */
const HISTORICAL_POLICY_ACTS: ReadonlyMap<string, string> = new Map([
  ['PWB-SECRET-CLASSIFICATION-POLICY-ACT.md', 'e02c0e6fbe408c4aac7d60f86e116bc8d4b79672a0c3a4dd4d6cf1a9f6bf59bb'],
  ['PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md', 'e766803dafcfbf0c5d40fdc499af7a83239864afd2a09696a7d7a21f81618a0a'],
  ['PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md', '178fcd57c4afde5ff457e6928a73089a2567f02ff8ef95d7efe05234f88e9988'],
]);

const POLICY_STEM = 'pwb-secret-classification-policy';
const SCOPE_STEM = 'public-source-scope';
/** A decisions file names the policy when a field line (any case, spacing, dash spelling) carries its path, or an act identity of its family,
 * or when its name or (outside the aggregate acceptance record) its text carries the public-source-scope stem of the acts' identities and file names. */
function namesPolicy(rel: string, text: string): boolean {
  const path = fold(POLICY_PATH), folded = fold(text);
  if (fold(rel).includes(SCOPE_STEM) || (rel !== AGGREGATE_RECORD && folded.includes(SCOPE_STEM))) return true;
  for (const line of folded.split('\n')) {
    const field = /^\s*(?:[-*]\s*)?\**\s*(artifact\s+identity|act\s+identity)\s*\**\s*:\s*(.*)$/u.exec(line);
    if (field !== null && (field[2]!.includes(path) || (field[1]!.startsWith('act') && field[2]!.includes(POLICY_STEM)))) return true;
  }
  return fold(rel).includes(POLICY_STEM) && /withdraw|revok/u.test(fold(rel));
}

function parsePolicyAct(text: string, form: PolicyActForm): ParsedAct {
  if (!text.startsWith(`${form.title}\n`) || one(text, /^Artifact identity: `([^`\n]+)`$/gm) !== POLICY_PATH) refuse();
  const act = { type: one(text, /^Act type: `([a-z-]+)`$/gm), identity: one(text, /^Act identity: `([^`\n]+)`$/gm), digest: one(text, /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gm), date: one(text, /^Date: (\d{4}-\d{2}-\d{2})$/gm) };
  const project = one(text, /^Project identity: `(project:syzygy)`$/gm);
  one(text, /^Provenance state: `(owner-adopted \(bootstrap, uncorrelated\))`/gm);
  if (act.type !== 'approve-policy' || act.identity !== form.identity(act.date)) refuse();
  const at = Date.parse(`${act.date}T00:00:00Z`);
  if (!Number.isSafeInteger(at) || new Date(at).toISOString().slice(0, 10) !== act.date) refuse();
  return { file: form.file, identity: act.identity, type: act.type, artifact: POLICY_PATH, project, digest: act.digest, date: act.date, recordedAt: actInstant(text, act.date), supersession: supersessionText(text), text };
}

/** The policy, its declared scope, and the recorder acts over it (version 1, version 2), every decisions file swept. The chain is
 * strict: version 2 needs version 1, took effect strictly later, binds other bytes, and its supersession text names version 1's
 * record path and argument. */
async function readPolicyActs(fs: PackageReaderFs, root: string): Promise<{ readonly policy: string; readonly scope: unknown; readonly v1: ParsedAct | null; readonly v2: ParsedAct | null }> {
  let policy: string;
  try { policy = await fs.readFile(path.join(root, POLICY_PATH)); } catch { return refuse(); }
  const files = await walk(fs, path.join(root, DECISIONS_DIR));
  let scope: unknown;
  try { scope = (JSON.parse(policy) as { publicSourceScope?: unknown }).publicSourceScope; } catch { return refuse(); }
  const parsed: Array<ParsedAct | null> = POLICY_ACT_FORMS.map(() => null);
  for (const rel of files) {
    let text: string;
    try { text = await fs.readFile(path.join(root, DECISIONS_DIR, rel)); } catch { return refuse(); }
    const at = POLICY_ACT_FORMS.findIndex(f => f.file === rel);
    if (at < 0) {
      // Another record that names the policy is a known historical act (by name and digest) or an unknown form: refuse the unknown.
      const pinned = HISTORICAL_POLICY_ACTS.get(rel);
      if (pinned !== undefined) { if (sha256(text) !== pinned) refuse(); continue; }
      if (namesPolicy(rel, text)) refuse();
      continue;
    }
    parsed[at] = parsePolicyAct(text, POLICY_ACT_FORMS[at]!);
  }
  const [v1, v2] = parsed;
  if (v1 === null || v1 === undefined || v2 === null || v2 === undefined) { if (v2 !== null && v2 !== undefined) refuse(); return { policy, scope, v1: v1 ?? null, v2: null }; }
  if (v2.recordedAt <= v1.recordedAt || v2.digest === v1.digest || !v2.supersession.includes(`\`${v1.digest}\``) || !v2.supersession.includes(`${DECISIONS_DIR}/${v1.file}`)) refuse();
  return { policy, scope, v1, v2 };
}

export function createPackagePolicyReader(options: { readonly root: string; readonly fs?: PackageReaderFs }): PolicyActReader {
  const fs = options.fs ?? nodeFs;
  return {
    read: async () => {
      const { policy, scope, v1, v2 } = await readPolicyActs(fs, options.root);
      const records: PolicyActRecord[] = [];
      for (const act of [v1, v2]) {
        // The act binds the policy bytes it names: stale bytes or a policy that declares no public-source scope do not count.
        if (act === null || act.digest !== sha256(policy) || scope === null || typeof scope !== 'object' || Array.isArray(scope)) continue;
        records.push(Object.freeze({ actIdentity: act.identity, digest: act.digest, inForceAt: act.recordedAt }));
      }
      return Object.freeze(records);
    },
  };
}

/** The result of a strict act read: the parsed record(s), or why there are none. `absent` (no record) and `refused` (a bad form, a
 * withdrawal-naming file, or bytes that no longer match) both mean "not in force"; they are told apart for the report only. */
export type ActState<T> = ({ readonly state: 'ok' } & T) | { readonly state: 'absent'; readonly why: string } | { readonly state: 'refused'; readonly why: string };
export interface StrictReadOptions { readonly root: string; readonly fs?: PackageReaderFs }
async function strict<T>(read: () => Promise<ActState<T>>): Promise<ActState<T>> {
  try { return await read(); } catch (error) { if (error instanceof AdmissionRecordError) return { state: 'refused', why: error.message }; throw error; }
}

/** The screening-scope policy act chain. `ok` only when the final act (version 2 if recorded, else version 1) binds exactly the
 * on-disk policy bytes. */
export type PolicyActChain = { readonly v1: ParsedAct | null; readonly v2: ParsedAct | null; readonly final: ParsedAct; readonly policyDigest: string };
export function readPolicyActChain(options: StrictReadOptions): Promise<ActState<PolicyActChain>> {
  return strict<PolicyActChain>(async () => {
    const { policy, v1, v2 } = await readPolicyActs(options.fs ?? nodeFs, options.root);
    const final = v2 ?? v1;
    if (final === null) return { state: 'absent', why: 'no screening-scope policy act is recorded' };
    const policyDigest = sha256(policy);
    if (final.digest !== policyDigest) return { state: 'refused', why: 'the policy bytes differ from the final act\'s argument' };
    return { state: 'ok', v1, v2, final, policyDigest };
  });
}

const CLASS_STEM = 'rfc5-project-documentation';
function namesClassAct(rel: string, text: string): boolean {
  const folded = fold(text);
  return fold(rel).includes(CLASS_STEM) || (rel !== AGGREGATE_RECORD && (folded.includes(CLASS_STEM) || folded.includes(fold(CLASS_MODULE)))) || folded.split('\n').some(line => {
    const field = /^\s*(?:[-*>]\s*)?\**\s*(artifact\s+identity|act\s+identity)\s*\**\s*:\s*(.*)$/u.exec(line);
    return field !== null && (field[2]!.includes(fold(CLASS_MODULE)) || field[2]!.includes(CLASS_STEM));
  });
}
async function readClassAct(fs: PackageReaderFs, root: string): Promise<{ readonly act: ParsedAct; readonly moduleDigest: string } | null> {
  const files = await walk(fs, path.join(root, DECISIONS_DIR));
  let found: string | null = null;
  for (const rel of files) {
    let text: string;
    try { text = await fs.readFile(path.join(root, DECISIONS_DIR, rel)); } catch { return refuse(); }
    if (rel === CLASS_ACT_FILE) { found = text; continue; }
    if (namesClassAct(rel, text)) refuse();
  }
  if (found === null) return null;
  let module: string;
  try { module = await fs.readFile(path.join(root, CLASS_MODULE)); } catch { return refuse(); }
  const text = found;
  if (!text.startsWith(CLASS_TITLE + '\n')) refuse();
  const date = one(text, /^Date: (\d{4}-\d{2}-\d{2})$/gm), identity = one(text, /^Act identity: `([^`\n]+)`$/gm), type = one(text, /^Act type: `([^`\n]+)`$/gm);
  const artifact = one(text, /^Artifact identity: `([^`\n]+)`$/gm), project = one(text, /^Project identity: `(project:syzygy)`$/gm), digest = one(text, /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gm);
  if (identity !== `RFC5-PROJECT-DOCUMENTATION-AMEND-${date}` || type !== 'contract-amendment' || artifact !== CLASS_MODULE || digest !== sha256(module)) refuse();
  return { act: { file: CLASS_ACT_FILE, identity, type, artifact, project, digest, date, recordedAt: actInstant(text, date, 'Act instant', /^\s*act instant\b/gim), supersession: supersessionText(text), text }, moduleDigest: sha256(module) };
}
/** The RFC5-14 project-documentation class amendment act: `ok` when the recorder's record exists in form and its argument is the
 * sha256 of the installed RFC-0005 module; `absent` when none is recorded; `refused` for any bad form, a file elsewhere in the
 * decisions tree that names it, or an installed module that no longer matches. */
export type ClassActRead = { readonly act: ParsedAct; readonly moduleDigest: string };
export function readClassActState(options: StrictReadOptions): Promise<ActState<ClassActRead>> {
  return strict<ClassActRead>(async () => {
    const hit = await readClassAct(options.fs ?? nodeFs, options.root);
    return hit === null ? { state: 'absent', why: 'no class amendment act is recorded' } : { state: 'ok', ...hit };
  });
}

/** The in-force egress record to Anthropic at `now` (version 2 replaces version 1 from its act's instant), with its listed content classes
 * and the repositories its Scope section admits. */
export type InForceEgress = { readonly recordId: string; readonly version: string; readonly digest: string; readonly contentClasses: readonly string[]; readonly admittedRepositories: readonly string[] };
export function readInForceEgress(options: StrictReadOptions & { readonly now: number }): Promise<ActState<InForceEgress>> {
  return strict<InForceEgress>(async () => {
    const live = inForceRecords(await createPackageAdmissionReader(options).read(), options.now).filter(r => r.class === 'egress' && r.providerId === 'anthropic');
    if (live.length === 0) return { state: 'absent', why: 'no egress record is in force' };
    if (live.length > 1) return { state: 'refused', why: 'more than one egress record is in force' };
    const [r] = live;
    return { state: 'ok', recordId: r!.recordId, version: r!.version, digest: r!.digest, contentClasses: r!.contentClasses, admittedRepositories: r!.admittedRepositories };
  });
}

/** Structurally the poc:dossier trigger's `AdmissionRecordsPort`. */
export interface AdmissionRequirementLike { readonly kind: 'observation-consent' | 'public-source-policy' | 'egress-consent'; readonly repositoryId: string; readonly revision: string }
export interface ConsentedRevision { readonly label: string; readonly commitId: string }
export type AdmissionAnswerLike = { readonly satisfied: true; readonly record: string } | { readonly satisfied: false; readonly why: string };
export interface AdmissionRecordsPortLike {
  readonly source: string;
  readonly check: (requirement: AdmissionRequirementLike & Record<string, unknown>) => Promise<AdmissionAnswerLike>;
  /** The owner's consented revisions for a repository id: label and full commit id, from the observation records in force now. Fails closed to
   * an empty list when records cannot be read, or when labels and commits are not one-to-one across the records in force. */
  readonly consentedRevisionsFor: (repositoryId: string) => Promise<readonly ConsentedRevision[]>;
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
    consentedRevisionsFor: async repositoryId => {
      let live: readonly AdmissionRecord[];
      try { live = inForceRecords(await options.reader.read(), options.now()); } catch { return []; }
      const byLabel = new Map<string, string>(), byCommit = new Map<string, string>();
      for (const r of live) {
        if (r.class !== 'observation' || r.repositoryId !== repositoryId) continue;
        for (const [i, commitId] of r.admittedRevisions.entries()) {
          const label = r.revisionLabels[i]!;
          if ((byLabel.get(label) ?? commitId) !== commitId || (byCommit.get(commitId) ?? label) !== label) return [];   // one label, two commits (or the reverse) across records
          byLabel.set(label, commitId); byCommit.set(commitId, label);
        }
      }
      return Object.freeze([...byLabel].map(([label, commitId]) => Object.freeze({ label, commitId })));
    },
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
