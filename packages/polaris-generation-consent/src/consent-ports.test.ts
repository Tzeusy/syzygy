import { describe, expect, it } from 'vitest';
import { generationAnchorId, gitBlobObjectId, runGenerationPipeline, type AdmissionDecision, type AttemptInput, type GenerationSource, type PipelinePorts, type PipelineRequest } from '@syzygy/polaris-generation-core';
import { AdmissionRecordError, parseAdmissionRecords, type AdmissionRecord } from './admission-record.js';
import { UNCONSENTED, createConsentPorts, type ConsentAudit, type ConsentPortsOptions, type ConsentReason } from './consent-ports.js';

const NOW = 1_800_000_000_000;
const REDIS_REV = 'a'.repeat(40);
const REQ_REV = 'b'.repeat(40);
const hex = (c: string): string => c.repeat(64);

const source = (repositoryId: string, revision: string, id: string, excluded = false): GenerationSource => {
  const body = `Body of ${id}.`;
  const base = { repositoryId, revision, path: `${id}.md`, objectId: gitBlobObjectId(body) };
  const end = Buffer.byteLength(body);
  return excluded
    ? { ...base, sourceId: id, evaluationId: 'evaluation:fixture', classificationBasis: 'path-only', exclusion: { excluded: true, reason: 'secret' }, spans: [] }
    : { ...base, sourceId: id, evaluationId: 'evaluation:fixture', classificationBasis: 'body', exclusion: { excluded: false }, body, spans: [{ anchorId: generationAnchorId(base, 0, end), start: 0, end, text: body }] };
};

const obs = (over: Partial<AdmissionRecord> = {}): AdmissionRecord => ({
  recordId: 'PUBLIC-OBS-REDIS-2026-10-03', version: '1', class: 'observation', project: 'project:syzygy', repositoryId: 'redis-redis', providerId: null, digest: hex('1'),
  inForceAt: NOW - 1000, withdrawnAt: null, supersedes: null, admittedRevisions: [REDIS_REV], admittedRepositories: [], contentClasses: [], ...over,
});
const egress = (over: Partial<AdmissionRecord> = {}): AdmissionRecord => ({
  recordId: 'PUBLIC-EGRESS-anthropic', version: '2', class: 'egress', project: 'project:syzygy', repositoryId: null, providerId: 'anthropic', digest: hex('2'),
  inForceAt: NOW - 1000, withdrawnAt: null, supersedes: null, admittedRevisions: [], admittedRepositories: ['redis-redis'], contentClasses: ['code-content', 'governance-text'], ...over,
});

function rig(records: AdmissionRecord[], extra: Partial<ConsentPortsOptions> = {}) {
  const state = { records, now: NOW, reads: 0, reserved: [] as AttemptInput[], audits: [] as ConsentAudit[], failAudit: false, failRead: false };
  const sources = [source('redis-redis', REDIS_REV, 'readme'), source('redis-redis', REDIS_REV, 'hidden', true)];
  const options: ConsentPortsOptions = {
    reader: { read: async () => { state.reads++; if (state.failRead) throw new Error('boom'); return state.records; } },
    now: () => state.now, consentingProject: 'project:syzygy', routeProviders: { 'agent-sdk': 'anthropic' }, sources,
    contentClassOf: s => (s.path.endsWith('.md') ? 'governance-text' : null), instructionClass: 'code-content',
    reserve: async (input): Promise<AdmissionDecision> => { state.reserved.push(input); return { kind: 'reserved', permit: { attemptId: `${input.requestId}:${input.ordinal}`, maxUsageUnits: 10, maxOutputBytes: 1000 } }; },
    audit: async record => { if (state.failAudit) throw new Error('audit down'); state.audits.push(record); },
    ...extra,
  };
  return { state, options, ports: createConsentPorts(options), sources };
}
const attempt = (over: Partial<Omit<AttemptInput, 'permissionDigest' | 'bindingDigest'>> = {}): Omit<AttemptInput, 'permissionDigest' | 'bindingDigest'> => ({
  requestId: 'r1', projectId: 'redis', snapshotId: 's1', providerRoute: 'agent-sdk', stage: 'inventory', ordinal: 0, inputDigest: hex('9'), inputBytes: 10, deadline: NOW + 1e6,
  budget: { maxCalls: 10, maxInputBytes: 1e6, maxOutputBytes: 1e5, maxUsageUnits: 1e5, maxElapsedMs: 1e6, maxRepairCycles: 0, accountingPolicy: 'p' }, ...over,
});
const full = (base: Omit<AttemptInput, 'permissionDigest' | 'bindingDigest'>, permissionDigest: string): AttemptInput => ({ ...base, permissionDigest, bindingDigest: hex('7') });
const permit = { attemptId: 'a', maxUsageUnits: 1, maxOutputBytes: 1 };

describe('consent-backed ports', () => {
  it('permits when an observation record and an egress record are in force, auditing what was relied on', async () => {
    const { ports, state } = rig([obs(), egress()]);
    const identity = await ports.permissionIdentity(attempt());
    expect(identity).toMatch(/^[0-9a-f]{64}$/);
    const input = full(attempt(), identity);
    expect((await ports.admit(input)).kind).toBe('reserved');
    expect(await ports.permitted(input, permit)).toBe(true);
    expect(state.audits.map(a => [a.phase, a.decision, a.unknown])).toEqual([['identity', 'permitted', null], ['admit', 'permitted', null], ['dispatch', 'permitted', null]]);
    expect(state.audits[0]!.relied).toEqual([{ recordId: 'PUBLIC-EGRESS-anthropic', version: '2', digest: hex('2') }, { recordId: 'PUBLIC-OBS-REDIS-2026-10-03', version: '1', digest: hex('1') }]);
    expect(JSON.stringify(state.audits)).not.toContain('Body of');   // identities only, no source text
    expect(state.reads).toBe(3);                                       // read afresh each check
  });

  it('changes the permission identity when a relied-on record changes version or digest', async () => {
    const a = await rig([obs(), egress()]).ports.permissionIdentity(attempt());
    expect(await rig([obs(), egress({ version: '3' })]).ports.permissionIdentity(attempt())).not.toBe(a);
    expect(await rig([obs(), egress({ digest: hex('8') })]).ports.permissionIdentity(attempt())).not.toBe(a);
    expect(await rig([obs(), egress()]).ports.permissionIdentity(attempt({ providerRoute: 'agent-sdk' }))).toBe(a);
  });

  const refusals: [string, () => AdmissionRecord[], ConsentReason, Partial<ConsentPortsOptions>?][] = [
    ['no records at all', () => [], 'record-missing'],
    ['observation record missing', () => [egress()], 'record-missing'],
    ['egress record missing', () => [obs()], 'record-missing'],
    ['observation still a candidate', () => [obs({ inForceAt: null }), egress()], 'not-in-force'],
    ['egress still a candidate', () => [obs(), egress({ inForceAt: null })], 'not-in-force'],
    ['future-dated observation', () => [obs({ inForceAt: NOW + 1 }), egress()], 'future-dated'],
    ['future-dated egress', () => [obs(), egress({ inForceAt: NOW + 1 })], 'future-dated'],
    ['withdrawn observation', () => [obs({ withdrawnAt: NOW - 5 }), egress()], 'withdrawn'],
    ['withdrawn egress', () => [obs(), egress({ withdrawnAt: NOW - 5 })], 'withdrawn'],
    ['future-dated withdrawal still defeats the grant', () => [obs(), egress({ withdrawnAt: NOW + 5 })], 'withdrawn'],
    ['revision is a tag label', () => [obs({ admittedRevisions: ['8.10.2'] }), egress()], 'revision-not-admitted'],
    ['revision not admitted', () => [obs({ admittedRevisions: [REQ_REV] }), egress()], 'revision-not-admitted'],
    ['repository not in egress scope', () => [obs(), egress({ admittedRepositories: ['psf-requests'] })], 'repository-not-admitted'],
    ['content class not admitted', () => [obs(), egress({ contentClasses: ['code-content'] })], 'class-not-admitted'],
    ['instruction class not admitted', () => [obs(), egress({ contentClasses: ['governance-text'] })], 'class-not-admitted'],
    ['content class undeterminable', () => [obs(), egress()], 'class-unknown', { contentClassOf: () => null }],
    ['route has no provider', () => [obs(), egress()], 'provider-unmapped', { routeProviders: {} }],
    ['egress for another provider only', () => [obs(), egress({ providerId: 'other' })], 'record-missing'],
    ['consent of another project', () => [obs({ project: 'project:other' }), egress()], 'record-missing'],
    ['same id and version with two digests', () => [obs(), obs({ digest: hex('3') }), egress()], 'ambiguous-records'],
    ['two live egress records for one provider', () => [obs(), egress(), egress({ recordId: 'PUBLIC-EGRESS-anthropic-b' })], 'ambiguous-records'],
  ];
  for (const [name, records, reason, extra] of refusals) {
    it(`refuses at every port: ${name}`, async () => {
      const { ports, state } = rig(records(), extra);
      expect(await ports.permissionIdentity(attempt())).toBe('');
      expect((await ports.admit(full(attempt(), hex('5')))).kind).toBe('refused');
      expect(await ports.permitted(full(attempt(), hex('5')), permit)).toBe(false);
      expect(state.reserved).toEqual([]);
      expect(state.audits.every(a => a.decision === 'refused' && a.unknown === UNCONSENTED && a.reasons.includes(reason))).toBe(true);
      expect(state.audits).toHaveLength(3);
    });
  }

  it('a superseded version never counts, even when the successor omits the revision', async () => {
    const old = obs({ version: '1' });
    const next = obs({ version: '2', supersedes: 'PUBLIC-OBS-REDIS-2026-10-03@1', admittedRevisions: [REQ_REV], digest: hex('4') });
    expect(await rig([old, next, egress()]).ports.permissionIdentity(attempt())).toBe('');
    const okNext = obs({ version: '2', supersedes: 'PUBLIC-OBS-REDIS-2026-10-03@1', admittedRevisions: [REDIS_REV], digest: hex('4') });
    expect(await rig([old, okNext, egress()]).ports.permissionIdentity(attempt())).not.toBe('');
    // A successor that took effect and was then withdrawn leaves no grant; the old version is not resurrected.
    const withdrawnNext = obs({ version: '2', supersedes: 'PUBLIC-OBS-REDIS-2026-10-03@1', digest: hex('4'), withdrawnAt: NOW - 1 });
    expect(await rig([old, withdrawnNext, egress()]).ports.permissionIdentity(attempt())).toBe('');
    // A future-dated successor has not replaced anything yet.
    const futureNext = obs({ version: '2', supersedes: 'PUBLIC-OBS-REDIS-2026-10-03@1', digest: hex('4'), inForceAt: NOW + 10 });
    expect(await rig([old, futureNext, egress()]).ports.permissionIdentity(attempt())).not.toBe('');
  });

  it('does not accept a tag label as a revision even when the record lists the same label', async () => {
    const { options } = rig([obs({ admittedRevisions: ['8.10.2'] }), egress()]);
    const tagged = createConsentPorts({ ...options, sources: [source('redis-redis', '8.10.2', 'readme')] });
    expect(await tagged.permissionIdentity(attempt())).toBe('');
  });

  it('is not refused by dead records that no source or provider route depends on', async () => {
    const stray = [obs({ recordId: 'PUBLIC-OBS-OTHER', repositoryId: 'other-repo', withdrawnAt: NOW - 1, admittedRevisions: ['c'.repeat(40)] }), egress({ recordId: 'PUBLIC-EGRESS-other', providerId: 'other', inForceAt: null })];
    expect(await rig([obs(), egress(), ...stray]).ports.permissionIdentity(attempt())).not.toBe('');
  });

  it('requires observation consent for excluded sources but not an egress class', async () => {
    const { options } = rig([obs(), egress()]);
    const ports = createConsentPorts({ ...options, contentClassOf: s => (s.exclusion.excluded ? null : 'governance-text') });
    expect(await ports.permissionIdentity(attempt())).not.toBe('');
    const hidden = source('redis-redis', 'c'.repeat(40), 'hidden', true);
    const other = createConsentPorts({ ...options, sources: [...options.sources, hidden] });
    expect(await other.permissionIdentity(attempt())).toBe('');
  });

  it('fails closed when the reader or the audit sink fails', async () => {
    const a = rig([obs(), egress()]); a.state.failRead = true;
    expect(await a.ports.permissionIdentity(attempt())).toBe('');
    expect(a.state.audits[0]!.reasons).toEqual(['reader-failed']);
    const b = rig([obs(), egress()]); b.state.failAudit = true;
    expect(await b.ports.permissionIdentity(attempt())).toBe('');
    expect(await b.ports.permitted(full(attempt(), hex('5')), permit)).toBe(false);
  });

  it('refuses admit when permission is withdrawn after the identity was issued, without reserving', async () => {
    const { ports, state } = rig([obs(), egress()]);
    const identity = await ports.permissionIdentity(attempt());
    state.records = [obs(), egress({ withdrawnAt: NOW })];
    expect(await ports.admit(full(attempt(), identity))).toEqual({ kind: 'refused', reason: 'permission-withdrawn' });
    expect(state.reserved).toEqual([]);
  });

  it('refuses admit and dispatch when the effective records changed even though still in force', async () => {
    const { ports, state } = rig([obs(), egress()]);
    const identity = await ports.permissionIdentity(attempt());
    state.records = [obs(), egress({ version: '3', digest: hex('6'), supersedes: 'PUBLIC-EGRESS-anthropic@2' }), egress()];
    expect(await ports.admit(full(attempt(), identity))).toEqual({ kind: 'refused', reason: 'identity-mismatch' });
    expect(await ports.permitted(full(attempt(), identity), permit)).toBe(false);
  });

  it('refuses dispatch when permission is withdrawn between admit and send', async () => {
    const { ports, state } = rig([obs(), egress()]);
    const input = full(attempt(), await ports.permissionIdentity(attempt()));
    expect((await ports.admit(input)).kind).toBe('reserved');
    state.records = [obs({ withdrawnAt: NOW }), egress()];
    expect(await ports.permitted(input, permit)).toBe(false);
  });

  it('matches only the exact source population', () => {
    const { ports, sources } = rig([obs(), egress()]);
    expect(ports.matches({ sources })).toBe(true);
    expect(ports.matches({ sources: [...sources].reverse() })).toBe(true);
    expect(ports.matches({ sources: sources.slice(0, 1) })).toBe(false);
    expect(ports.matches({ sources: [source('redis-redis', 'c'.repeat(40), 'readme'), sources[1]!] })).toBe(false);
    expect(ports.matches({ sources: [] })).toBe(false);
  });
});

describe('through the pipeline', () => {
  const harness = (records: AdmissionRecord[]) => {
    const r = rig(records);
    const sent: string[] = [];
    let n = 0;
    const base: PipelinePorts = {
      now: () => NOW, verifySources: async request => r.ports.matches(request),
      ...r.ports, releaseUnsent: async () => undefined,
      responseSchema: () => ({ version: 'v1', schema: {} }),
      generate: async input => { sent.push(input.stage); return { body: JSON.stringify({ stage: input.stage }), model: 'm', usageUnits: 1 }; },
      validate: (stage, value) => { if ((value as { stage?: string }).stage !== stage) throw Error('schema'); return value; },
      record: async () => undefined, lateReceipt: async () => undefined, fidelity: () => ({ blocking: false, findings: [] }),
    };
    const ports: PipelinePorts = { ...base, admit: async input => { const d = await r.ports.admit(input); return d.kind === 'refused' ? d : { kind: 'reserved', permit: { attemptId: `a${n++}`, maxUsageUnits: 10, maxOutputBytes: 1000 } }; } };
    const request: PipelineRequest = {
      requestId: 'r1', projectId: 'redis', snapshotId: 's1', startedAt: NOW,
      routes: { inventory: 'agent-sdk', plan: 'agent-sdk', author: 'agent-sdk', edit: 'agent-sdk', fidelity: 'agent-sdk', repair: 'agent-sdk' },
      budget: { maxCalls: 10, maxInputBytes: 200_000, maxOutputBytes: 20_000, maxUsageUnits: 100, maxElapsedMs: 10_000, maxRepairCycles: 0, accountingPolicy: 'p' },
      sources: r.sources, readerQuestions: ['Why?'], requestedAssets: [],
    };
    return { r, ports, request, sent };
  };

  it('runs to rendered review when consent holds and sends nothing when it does not', async () => {
    const ok = harness([obs(), egress()]);
    expect((await runGenerationPipeline(ok.request, ok.ports, new AbortController().signal)).status).toBe('awaiting-rendered-review');
    expect(ok.sent).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity']);
    const none = harness([obs()]);
    expect(await runGenerationPipeline(none.request, none.ports, new AbortController().signal)).toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    expect(none.sent).toEqual([]);
  });

  it('stops at the next stage when consent is withdrawn mid-run', async () => {
    const h = harness([obs(), egress()]);
    const generate = h.ports.generate;
    const ports: PipelinePorts = { ...h.ports, generate: async input => { const reply = await generate(input); h.r.state.records = [obs(), egress({ withdrawnAt: NOW })]; return reply; } };
    expect(await runGenerationPipeline(h.request, ports, new AbortController().signal)).toMatchObject({ status: 'stopped', reason: 'admission-refused' });
    expect(h.sent).toEqual(['inventory']);
  });

  it('refuses a request whose sources differ from the population the ports were built for', async () => {
    const h = harness([obs(), egress()]);
    const result = await runGenerationPipeline({ ...h.request, sources: h.r.sources.slice(0, 1) }, h.ports, new AbortController().signal);
    expect(result).toMatchObject({ status: 'stopped', reason: 'source-refused' });
    expect(h.sent).toEqual([]);
  });
});

describe('parseAdmissionRecords', () => {
  const good = (): unknown[] => [obs(), egress()];
  it('accepts well-formed records and freezes them', () => {
    const records = parseAdmissionRecords(good());
    expect(records).toHaveLength(2);
    expect(Object.isFrozen(records[0])).toBe(true);
  });
  it('rejects the whole index on any malformed member', () => {
    const bad: [string, (r: Record<string, unknown>) => void][] = [
      ['unknown key', r => { r.extra = 1; }], ['missing key', r => { delete r.digest; }], ['short digest', r => { r.digest = 'abc'; }],
      ['bad class', r => { r.class = 'other'; }], ['non-integer instant', r => { r.inForceAt = 1.5; }], ['string instant', r => { r.withdrawnAt = '2026'; }],
      ['observation with provider', r => { r.providerId = 'anthropic'; }], ['observation without repository', r => { r.repositoryId = null; }],
    ];
    for (const [name, edit] of bad) {
      const list = good() as Record<string, unknown>[];
      edit(list[0]!);
      expect(() => parseAdmissionRecords(list), name).toThrow(AdmissionRecordError);
    }
    const egressBad = good() as Record<string, unknown>[];
    egressBad[1]!.repositoryId = 'x';
    expect(() => parseAdmissionRecords(egressBad)).toThrow(AdmissionRecordError);
    expect(() => parseAdmissionRecords({})).toThrow(AdmissionRecordError);
    expect(() => parseAdmissionRecords([null])).toThrow(AdmissionRecordError);
  });
});
