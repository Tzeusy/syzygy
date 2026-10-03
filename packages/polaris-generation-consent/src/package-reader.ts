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
 * act record carries a date, not an instant, so the record is in force from
 * the start of the next UTC day (fail-closed). A decisions file about the
 * package that is neither an act record nor the owner-answers direction is
 * unknown (a withdrawal form is not defined yet): the whole read is refused. */

export const DECISIONS_DIR = '.syzygy/governance/decisions';
export const INSTANCES_DIR = '.syzygy/governance/contracts/candidates/public-repo-admission/instances';
const ACT_FILE = /^PUBLIC-REPO-ADMISSION-[A-Z0-9-]+-ACT\.md$/;
const OWNER_ANSWERS = /^PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-\d{4}-\d{2}-\d{2}\.md$/;
const DAY_MS = 86_400_000;

export interface PackageReaderFs {
  readonly readdir: (dir: string) => Promise<readonly string[]>;
  readonly readFile: (file: string) => Promise<string>;
}
const nodeFs: PackageReaderFs = { readdir: dir => nodeReaddir(dir), readFile: file => nodeReadFile(file, 'utf8') };

const refuse = (): never => { throw new AdmissionRecordError('invalid-records'); };
const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const one = (text: string, re: RegExp): string => { const all = [...text.matchAll(re)]; return all.length === 1 ? all[0]![1]! : refuse(); };

interface Act { readonly type: 'observation' | 'egress'; readonly date: number; readonly artifact: string; readonly digest: string }

function parseAct(text: string): Act {
  const type = one(text, /^Act type: `(consent-observation|consent-egress)`$/gm);
  const date = one(text, /^Date: (\d{4}-\d{2}-\d{2})$/gm);
  const at = Date.parse(`${date}T00:00:00Z`);
  if (!Number.isSafeInteger(at)) refuse();
  const artifact = one(text, /^Artifact identity: `([^`\n]+)`$/gm);
  const digest = one(text, /^Exact digest \(SHA-256\): `([0-9a-f]{64})`$/gm);
  one(text, /^Project identity: `(project:syzygy)`$/gm);
  return { type: type === 'consent-observation' ? 'observation' : 'egress', date: at + DAY_MS, artifact, digest };
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
  if (!/^Proposed revocation state: active; supersedes no earlier consent$/m.test(text)) refuse();   // a successor form is not parsed: refuse rather than guess
  const base = { recordId, version, digest: act.digest, inForceAt, withdrawnAt: null, supersedes: null, project: 'project:syzygy' } as const;
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
        if (!name.startsWith('PUBLIC-REPO-ADMISSION-')) continue;
        if (OWNER_ANSWERS.test(name)) continue;
        if (!ACT_FILE.test(name)) refuse();
        let act: Act;
        try { act = parseAct(await fs.readFile(path.join(options.root, DECISIONS_DIR, name))); } catch { return refuse(); }
        const normalized = path.posix.normalize(act.artifact);
        if (normalized !== act.artifact || !normalized.startsWith(`${INSTANCES_DIR}/`) || normalized.includes('..')) refuse();
        let artifact: string;
        try { artifact = await fs.readFile(path.join(options.root, normalized)); } catch { return refuse(); }
        records.push(parseInstance(artifact, act, sha256(artifact) === act.digest ? act.date : null));
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
 * in-force polarity as the consent ports. A public-source policy record has no
 * act form in this package yet, so it is never satisfied here. */
export function createAdmissionRecordsPort(options: { readonly reader: AdmissionRecordReader; readonly now: () => number }): AdmissionRecordsPortLike {
  return {
    source: 'public-repo-admission act records (owner acts over the instance records)',
    check: async requirement => {
      if (requirement.kind === 'public-source-policy') return { satisfied: false, why: 'no record found: the public-source policy scope has no owner act form in the admission package' };
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
