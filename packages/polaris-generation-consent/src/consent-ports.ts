import { digestCanonicalJson, type AdmissionDecision, type AttemptInput, type DispatchPermit, type GenerationSource, type PipelinePorts, type PipelineRequest } from '@syzygy/polaris-generation-core';
import { COMMIT_OBJECT_ID, type AdmissionRecord, type AdmissionRecordReader } from './admission-record.js';

/** The one Unknown every refusal here renders as (REQ-polaris-generation-001). */
export const UNCONSENTED = 'unconsented-source-or-provider' as const;

export type ConsentReason =
  | 'reader-failed' | 'provider-unmapped' | 'ambiguous-records' | 'record-missing' | 'not-in-force' | 'future-dated'
  | 'withdrawn' | 'revision-not-admitted' | 'repository-not-admitted' | 'class-unknown' | 'class-not-admitted' | 'audit-failed';

export interface ReliedRecord { readonly recordId: string; readonly version: string; readonly digest: string }

/** RFC5-15 audit record: identities and digests only, never source text. */
export interface ConsentAudit {
  readonly at: number;
  readonly phase: 'identity' | 'admit' | 'dispatch';
  readonly stage: AttemptInput['stage'];
  readonly providerRoute: string;
  readonly providerId: string | null;
  readonly decision: 'permitted' | 'refused';
  readonly unknown: typeof UNCONSENTED | null;
  readonly reasons: readonly ConsentReason[];
  readonly relied: readonly ReliedRecord[];
  readonly populationDigest: string;
}

export interface ConsentPortsOptions {
  readonly reader: AdmissionRecordReader;
  readonly now: () => number;
  /** The consenting project (`project:syzygy`), not the project being described. */
  readonly consentingProject: string;
  /** Provider route (as named in PipelineRequest.routes) to provider id. An unmapped route is refused. */
  readonly routeProviders: Readonly<Record<string, string>>;
  /** The request's own source population; `matches` binds the run to it. */
  readonly sources: readonly GenerationSource[];
  /** RFC5-14 class of one source, or null when it cannot be determined (refused). */
  readonly contentClassOf: (source: GenerationSource) => string | null;
  /** Class of the generator's own instruction text, which every request carries. */
  readonly instructionClass: string;
  /** Atomic durable reservation, run only after consent holds. */
  readonly reserve: PipelinePorts['admit'];
  /** Awaited before any permit; a failing audit refuses (fail closed). */
  readonly audit: (record: ConsentAudit) => Promise<void>;
}

export interface ConsentPorts {
  readonly permissionIdentity: PipelinePorts['permissionIdentity'];
  readonly admit: PipelinePorts['admit'];
  readonly permitted: PipelinePorts['permitted'];
  /** True only when the request carries exactly the source population these ports were built for. */
  readonly matches: (request: Pick<PipelineRequest, 'sources'>) => boolean;
}

const LIMITS = { maxBytes: 4_000_000, maxNodes: 200_000, maxDepth: 16 };
const sourceKey = (s: GenerationSource): Record<string, unknown> => ({ sourceId: s.sourceId, repositoryId: s.repositoryId, revision: s.revision, path: s.path, objectId: s.objectId, excluded: s.exclusion.excluded });
const populationDigest = (sources: readonly GenerationSource[]): string => digestCanonicalJson([...sources].map(sourceKey).sort((a, b) => String(a.sourceId).localeCompare(String(b.sourceId))), LIMITS).digest;
const ref = (r: AdmissionRecord): string => `${r.recordId}@${r.version}`;

type Evaluation = { readonly ok: true; readonly relied: readonly ReliedRecord[] } | { readonly ok: false; readonly reasons: readonly ConsentReason[]; readonly relied: readonly ReliedRecord[] };

type Dead = 'withdrawn' | 'future-dated' | 'not-in-force' | 'ambiguous-records';
const DEAD_PRIORITY: readonly Dead[] = ['withdrawn', 'ambiguous-records', 'future-dated', 'not-in-force'];

/** Records that are plainly effective at `now`, plus why each other record is dead.
 * Candidate, future-dated, withdrawn and superseded records never count; two
 * records claiming the same id and version with different bytes void both. */
function effective(records: readonly AdmissionRecord[], now: number): { readonly live: AdmissionRecord[]; readonly dead: ReadonlyMap<AdmissionRecord, Dead> } {
  const byRef = new Map<string, AdmissionRecord[]>();
  for (const r of records) byRef.set(ref(r), [...(byRef.get(ref(r)) ?? []), r]);
  const ambiguous = new Set([...byRef].filter(([, list]) => new Set(list.map(r => r.digest)).size > 1).map(([key]) => key));
  const dead = new Map<AdmissionRecord, Dead>();
  const live = records.filter(r => {
    const why: Dead | null = ambiguous.has(ref(r)) ? 'ambiguous-records'
      : r.withdrawnAt !== null ? 'withdrawn'            // dated or not: withdrawal defeats grant
      : r.inForceAt === null ? 'not-in-force'
      : r.inForceAt > now ? 'future-dated' : null;
    if (why !== null) dead.set(r, why);
    return why === null;
  });
  // A successor that took effect replaces its predecessor for good: withdrawing the successor leaves no grant, not the old one.
  const replaced = new Set(records.flatMap(r => r.supersedes === null || ambiguous.has(ref(r)) || r.inForceAt === null || r.inForceAt > now ? [] : [r.supersedes]));
  return { live: live.filter(r => !replaced.has(ref(r))), dead };
}

function evaluate(records: readonly AdmissionRecord[], now: number, o: ConsentPortsOptions, providerId: string | null): Evaluation {
  if (providerId === null) return { ok: false, reasons: ['provider-unmapped'], relied: [] };
  const scoped = records.filter(r => r.project === o.consentingProject);
  const { live, dead } = effective(scoped, now);
  const reasons = new Set<ConsentReason>();
  const relied = new Map<string, ReliedRecord>();
  const rely = (r: AdmissionRecord): void => { relied.set(ref(r), { recordId: r.recordId, version: r.version, digest: r.digest }); };
  // Why a needed grant is absent: the strongest reason among dead records that would have matched it.
  const missing = (matches: (r: AdmissionRecord) => boolean): void => {
    const why = new Set([...dead].filter(([r]) => matches(r)).map(([, d]) => d));
    reasons.add(DEAD_PRIORITY.find(d => why.has(d)) ?? 'record-missing');
  };
  // Observation: every source in the population was read, so each (repository, revision) needs a commit-id grant.
  for (const s of o.sources) {
    const here = (r: AdmissionRecord): boolean => r.class === 'observation' && r.repositoryId === s.repositoryId;
    const grants = live.filter(here);
    if (grants.length === 0) { missing(here); continue; }
    const granted = COMMIT_OBJECT_ID.test(s.revision) ? grants.filter(r => r.admittedRevisions.includes(s.revision)) : [];
    if (granted.length === 0) { reasons.add('revision-not-admitted'); continue; }
    granted.forEach(rely);
  }
  // Egress: one record per (project, provider); it must list each repository and class of what could be sent.
  const forProvider = (r: AdmissionRecord): boolean => r.class === 'egress' && r.providerId === providerId;
  const egress = live.filter(forProvider);
  if (egress.length === 0) missing(forProvider);
  else if (egress.length > 1) reasons.add('ambiguous-records');
  else {
    const record = egress[0]!;
    rely(record);
    if (!record.contentClasses.includes(o.instructionClass)) reasons.add('class-not-admitted');
    for (const s of o.sources) {
      if (s.exclusion.excluded) continue;   // bodies of excluded sources never leave
      if (!record.admittedRepositories.includes(s.repositoryId)) { reasons.add('repository-not-admitted'); continue; }
      const cls = o.contentClassOf(s);
      if (cls === null) reasons.add('class-unknown');
      else if (!record.contentClasses.includes(cls)) reasons.add('class-not-admitted');
    }
  }
  const list = [...relied.values()].sort((a, b) => `${a.recordId}@${a.version}`.localeCompare(`${b.recordId}@${b.version}`));
  return reasons.size === 0 ? { ok: true, relied: list } : { ok: false, reasons: [...reasons].sort(), relied: list };
}

/** Consent-backed `permissionIdentity`, `admit` and `permitted`. Each check
 * reads the records afresh; none caches a positive answer. */
export function createConsentPorts(options: ConsentPortsOptions): ConsentPorts {
  const population = populationDigest(options.sources);
  const check = async (input: Pick<AttemptInput, 'stage' | 'providerRoute'>, phase: ConsentAudit['phase']): Promise<Evaluation> => {
    const providerId = Object.hasOwn(options.routeProviders, input.providerRoute) ? options.routeProviders[input.providerRoute]! : null;
    let evaluation: Evaluation;
    try { evaluation = evaluate(await options.reader.read(), options.now(), options, providerId); }
    catch { evaluation = { ok: false, reasons: ['reader-failed'], relied: [] }; }
    const audit: ConsentAudit = { at: options.now(), phase, stage: input.stage, providerRoute: input.providerRoute, providerId,
      decision: evaluation.ok ? 'permitted' : 'refused', unknown: evaluation.ok ? null : UNCONSENTED, reasons: evaluation.ok ? [] : evaluation.reasons, relied: evaluation.relied, populationDigest: population };
    try { await options.audit(audit); }
    catch { return { ok: false, reasons: [...(evaluation.ok ? [] : evaluation.reasons), 'audit-failed'], relied: evaluation.relied }; }
    return evaluation;
  };
  const identityOf = (e: Evaluation & { ok: true }, input: Pick<AttemptInput, 'providerRoute'>): string =>
    digestCanonicalJson({ consentingProject: options.consentingProject, providerRoute: input.providerRoute, population, relied: e.relied }, LIMITS).digest;
  return {
    // The empty string is the pipeline's refusal signal for a missing identity (stop: admission-refused).
    permissionIdentity: async input => { const e = await check(input, 'identity'); return e.ok ? identityOf(e, input) : ''; },
    admit: async (input: AttemptInput): Promise<AdmissionDecision> => {
      const e = await check(input, 'admit');
      if (!e.ok) return { kind: 'refused', reason: 'permission-withdrawn' };
      if (identityOf(e, input) !== input.permissionDigest) return { kind: 'refused', reason: 'identity-mismatch' };
      return options.reserve(input);
    },
    permitted: async (input: AttemptInput, _permit: DispatchPermit): Promise<boolean> => {
      const e = await check(input, 'dispatch');
      return e.ok && identityOf(e, input) === input.permissionDigest;
    },
    matches: request => { try { return populationDigest(request.sources) === population; } catch { return false; } },
  };
}
