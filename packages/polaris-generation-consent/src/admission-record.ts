/** The machine-readable face of a public-repo admission record (observation or
 * egress consent, RFC5-12). The records themselves are owner acts; this file
 * only fixes the shape a trusted reader must return, so the ports can fail
 * closed on anything that is not plainly in force. */

export type AdmissionClass = 'observation' | 'egress';

export interface AdmissionRecord {
  /** e.g. `PUBLIC-OBS-REDIS-2026-10-03` or `PUBLIC-EGRESS-anthropic`. */
  readonly recordId: string;
  readonly version: string;
  readonly class: AdmissionClass;
  /** The consenting project, e.g. `project:syzygy`. */
  readonly project: string;
  /** Observation: the repository read. Egress: null. */
  readonly repositoryId: string | null;
  /** Egress: the provider. Observation: null. */
  readonly providerId: string | null;
  /** SHA-256 of the exact record bytes the owner act bound. */
  readonly digest: string;
  /** Instant (epoch ms) the owner act took effect; null while still a candidate. */
  readonly inForceAt: number | null;
  /** Any withdrawal marker, dated or not; a withdrawal defeats the grant. */
  readonly withdrawnAt: number | null;
  /** `recordId@version` of the record this one replaces, if any. */
  readonly supersedes: string | null;
  /** Observation: full commit object ids; a tag or branch name never counts. */
  readonly admittedRevisions: readonly string[];
  /** Egress: repository ids whose content may be sent. */
  readonly admittedRepositories: readonly string[];
  /** Egress: the closed RFC5-14 content-class vocabulary admitted. */
  readonly contentClasses: readonly string[];
}

/** Trusted source of records, read fresh on every check. It is never a caller approval flag. */
export interface AdmissionRecordReader {
  readonly read: () => Promise<readonly AdmissionRecord[]>;
}

export class AdmissionRecordError extends Error {
  constructor(readonly code: 'invalid-records') { super(code); this.name = 'AdmissionRecordError'; }
}

const KEYS = ['recordId', 'version', 'class', 'project', 'repositoryId', 'providerId', 'digest', 'inForceAt', 'withdrawnAt', 'supersedes', 'admittedRevisions', 'admittedRepositories', 'contentClasses'];
const isText = (v: unknown): v is string => typeof v === 'string' && v.length > 0 && v.length <= 256;
const isNullableText = (v: unknown): v is string | null => v === null || isText(v);
const isInstant = (v: unknown): v is number | null => v === null || (typeof v === 'number' && Number.isSafeInteger(v) && v >= 0);
const isTextList = (v: unknown): v is string[] => Array.isArray(v) && v.length <= 1000 && v.every(isText);
export const COMMIT_OBJECT_ID = /^(?:[0-9a-f]{40}|[0-9a-f]{64})$/;

/** Validates untrusted JSON (for example a future in-force records index) into
 * records. Unknown keys, wrong shapes and records whose class contradicts their
 * subject fields are rejected as a whole: a partly readable index is not read. */
export function parseAdmissionRecords(value: unknown): readonly AdmissionRecord[] {
  if (!Array.isArray(value) || value.length > 10_000) throw new AdmissionRecordError('invalid-records');
  return value.map(item => {
    if (item === null || typeof item !== 'object' || Array.isArray(item)) throw new AdmissionRecordError('invalid-records');
    const r = item as Record<string, unknown>;
    if (Object.keys(r).length !== KEYS.length || !KEYS.every(key => key in r)) throw new AdmissionRecordError('invalid-records');
    const ok = isText(r.recordId) && isText(r.version) && (r.class === 'observation' || r.class === 'egress') && isText(r.project)
      && isNullableText(r.repositoryId) && isNullableText(r.providerId) && typeof r.digest === 'string' && /^[0-9a-f]{64}$/.test(r.digest)
      && isInstant(r.inForceAt) && isInstant(r.withdrawnAt) && isNullableText(r.supersedes)
      && isTextList(r.admittedRevisions) && isTextList(r.admittedRepositories) && isTextList(r.contentClasses);
    if (!ok) throw new AdmissionRecordError('invalid-records');
    const record = r as unknown as AdmissionRecord;
    const observation = record.class === 'observation';
    const shapeOk = observation
      ? record.repositoryId !== null && record.providerId === null && record.admittedRepositories.length === 0 && record.contentClasses.length === 0
      : record.providerId !== null && record.repositoryId === null && record.admittedRevisions.length === 0;
    if (!shapeOk) throw new AdmissionRecordError('invalid-records');
    return Object.freeze({ ...record, admittedRevisions: Object.freeze([...record.admittedRevisions]), admittedRepositories: Object.freeze([...record.admittedRepositories]), contentClasses: Object.freeze([...record.contentClasses]) });
  });
}
