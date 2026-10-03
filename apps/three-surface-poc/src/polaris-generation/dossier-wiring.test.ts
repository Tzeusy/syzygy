import { createHash } from 'node:crypto';
import { existsSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { createMessagesApiGenerate } from '@syzygy/polaris-generation-provider';
import { LOOPBACK_FOR_TESTS, startCaptureEndpoint, type CaptureEndpoint } from '@syzygy/polaris-generation-provider/testing';

import { GenerationUnavailable, openGeneration, type ProviderFactory } from './dossier-generation.js';
import { DOSSIER_RUN_PROFILE, stageCeilingUnits } from './dossier-run-profile.js';
import { EGRESS_STAGE_AUTHORITY, EGRESS_V1_DIGEST, EGRESS_V2_DIGEST, NARRATIVE_STAGES, stageAuthorisedBy, stagesAuthorisedBy } from './dossier-stage-authority.js';
import type { WiredRecordsPort } from './dossier-records.js';
import type { GenerationOpenContext, GenerationSession } from './dossier-trigger.js';

const REPO_ROOT = path.resolve(__dirname, '../../../..');
const SECRET = 'sk-test-wiring-0123456789abcdef';
const sha = (bytes: Buffer): string => createHash('sha256').update(bytes).digest('hex');

const requirement = { kind: 'egress-consent', repositoryId: 'redis-redis', commit: 'a'.repeat(40) } as unknown as GenerationOpenContext['egress'];
const recordsFor = (digest: string | null, satisfied = true): WiredRecordsPort => ({
  source: 'test', check: async () => ({ satisfied, record: 'EGRESS@1' }) as never, repositoryIdsFor: async () => ['redis-redis'],
  inForceEgress: async () => (digest === null ? null : { record: 'EGRESS@1', digest }),
});

describe('stage authority map', () => {
  it('v1 authorises the six narrative stages only, v2 adds the two discovery stages, an unknown digest nothing', () => {
    expect([...stagesAuthorisedBy(EGRESS_V1_DIGEST)]).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair']);
    expect([...stagesAuthorisedBy(EGRESS_V2_DIGEST)]).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair', 'discovery-map', 'discovery-reduce']);
    expect(stageAuthorisedBy(EGRESS_V1_DIGEST, 'discovery-map')).toBe(false);
    expect(stageAuthorisedBy('0'.repeat(64), 'inventory')).toBe(false);
    expect(stageAuthorisedBy(null, 'inventory')).toBe(false);
    expect(stageAuthorisedBy(undefined, 'discovery-reduce')).toBe(false);
    expect([...EGRESS_STAGE_AUTHORITY.keys()].sort()).toEqual([EGRESS_V1_DIGEST, EGRESS_V2_DIGEST].sort());
  });

  it('keys equal the SHA-256 of the installed instance bytes and the manifest rows (drift test)', () => {
    const base = path.join(REPO_ROOT, '.syzygy/governance/contracts/candidates');
    for (const [dir, manifest, digest] of [['public-repo-admission', 'PUBLIC-REPO-ADMISSION-MANIFEST.txt', EGRESS_V1_DIGEST], ['public-egress-v2', 'PUBLIC-EGRESS-V2-MANIFEST.txt', EGRESS_V2_DIGEST]] as const) {
      const rows = readFileSync(path.join(base, dir, manifest), 'utf8').split('\n').filter(line => line.includes('/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md'));
      expect(rows).toHaveLength(1);
      const [rowDigest, file] = rows[0]!.split(/\s+/);
      expect(rowDigest).toBe(digest);
      expect(sha(readFileSync(path.join(REPO_ROOT, file!)))).toBe(digest);
    }
  });
});

describe('run profile', () => {
  it('narrative stage ceilings never sum past the narrative share', () => {
    const p = DOSSIER_RUN_PROFILE;
    const ceilings = { inventory: 1, plan: 1, author: 1, edit: 1, fidelity: 2, repair: 1 };
    const worst = Object.entries(ceilings).reduce((sum, [stage, n]) => sum + n * stageCeilingUnits(p, stage as never), 0);
    expect(worst).toBeLessThanOrEqual(p.owner.runTotalUnits - p.owner.discoveryUnits);
    expect(p.owner.discoveryUnits + (p.owner.runTotalUnits - p.owner.discoveryUnits)).toBe(4000);
    expect(p.owner.discoveryCallUnits).toBe(40);
  });
});

describe('openGeneration against a loopback provider', () => {
  let upstream: CaptureEndpoint | undefined;
  const dirs: string[] = [];
  const sessions: GenerationSession[] = [];
  afterEach(async () => {
    for (const s of sessions.splice(0)) await s.close();
    await upstream?.close(); upstream = undefined;
    for (const d of dirs.splice(0)) rmSync(d, { recursive: true, force: true });
  });

  const loopbackFactory = (url: string): ProviderFactory => build => createMessagesApiGenerate({
    model: build.profile.model, apiKey: build.apiKey, upstream: { url, loopbackForTests: LOOPBACK_FOR_TESTS }, permitted: build.permitted,
    effort: build.profile.effort, thinking: build.profile.thinking, maxOutputTokens: build.profile.maxOutputTokens,
  });

  async function open(digest: string | null, apiKey = SECRET): Promise<{ session: GenerationSession; runDir: string }> {
    upstream ??= await startCaptureEndpoint({ kind: 'text', text: '{"claims":[]}', inputTokens: 1000, outputTokens: 39000 });
    const parent = mkdtempSync(path.join(tmpdir(), 'wiring-'));
    dirs.push(parent);
    const runDir = path.join(parent, 'run');
    const context: GenerationOpenContext = { target: { owner: 'redis', repo: 'redis' } as never, revision: 'a'.repeat(40), runDir, egress: requirement, records: recordsFor(digest) };
    const session = await openGeneration({ route: 'messages-api', apiKey, root: REPO_ROOT, providerFactory: loopbackFactory(upstream.url) })(context);
    sessions.push(session);
    return { session, runDir };
  }

  const mapInput = (n: number) => ({ subsystem: `s${n}`, readerQuestions: ['What is it?'], items: [{ blobId: `b${n}`, path: `src/f${n}.c`, excerpt: 'int main(void) { return 0; }' }] });

  it('fails closed with no credential, before the state directory or any request exists', async () => {
    upstream = await startCaptureEndpoint();
    const parent = mkdtempSync(path.join(tmpdir(), 'wiring-')); dirs.push(parent);
    const runDir = path.join(parent, 'run');
    const context: GenerationOpenContext = { target: { owner: 'redis', repo: 'redis' } as never, revision: 'a'.repeat(40), runDir, egress: requirement, records: recordsFor(EGRESS_V2_DIGEST) };
    await expect(openGeneration({ route: 'messages-api', apiKey: '', root: REPO_ROOT, providerFactory: loopbackFactory(upstream.url) })(context)).rejects.toBeInstanceOf(GenerationUnavailable);
    expect(existsSync(`${runDir}.state`)).toBe(false);
    expect(upstream.requests).toHaveLength(0);
  });

  it('under egress v1 discovery is refused before any request; under an unknown digest every stage is', async () => {
    const v1 = await open(EGRESS_V1_DIGEST);
    expect(await v1.session.discoveryPermitted({ kind: 'map', itemCount: 1, requestDigest: 'x' })).toBe(false);
    expect(await v1.session.discoveryPermitted({ kind: 'reduce', itemCount: 1, requestDigest: 'x' })).toBe(false);
    await expect(v1.session.discovery.map!(mapInput(0), new AbortController().signal)).rejects.toBeDefined();
    const unknown = await open('f'.repeat(64));
    await expect(unknown.session.discovery.map!(mapInput(1), new AbortController().signal)).rejects.toBeDefined();
    expect(upstream!.messages()).toHaveLength(0);
  });

  it('a run cannot send more discovery calls than the discovery share allows', async () => {
    const { session } = await open(EGRESS_V2_DIGEST);
    const signal = new AbortController().signal;
    let sent = 0;
    // Every reply reports 40 units (1k in, 39k out): the share of 1000 holds 25 such calls.
    for (let n = 0; n < 60; n++) {
      const call = { kind: 'map' as const, itemCount: 1, requestDigest: String(n) };
      if (!(await session.discoveryPermitted(call))) break;
      await session.discovery.map!(mapInput(n), signal); sent++;
    }
    expect(sent).toBe(25);
    expect(upstream!.messages()).toHaveLength(25);
    const record = session.record() as { spend: { discoveryCountedUnits: number } };
    expect(record.spend.discoveryCountedUnits).toBe(1000);
    expect(await session.discoveryPermitted({ kind: 'reduce', itemCount: 1, requestDigest: 'r' })).toBe(false);
  });

  it('unknown usage counts at the full call ceiling', async () => {
    upstream = await startCaptureEndpoint({ kind: 'text', text: '{"claims":[]}', noUsage: true });
    const { session } = await open(EGRESS_V2_DIGEST);
    const signal = new AbortController().signal;
    let sent = 0;
    for (let n = 0; n < 60; n++) {
      if (!(await session.discoveryPermitted({ kind: 'map', itemCount: 1, requestDigest: String(n) }))) break;
      await session.discovery.map!(mapInput(n), signal).catch(() => undefined); sent++;
    }
    expect(sent).toBeLessThanOrEqual(25);
    const record = session.record() as { spend: { discoveryCountedUnits: number } };
    expect(record.spend.discoveryCountedUnits).toBeLessThanOrEqual(1000);
  });

  it('the credential reaches the adapter only: it is in no state file and not in the record', async () => {
    const { session, runDir } = await open(EGRESS_V2_DIGEST);
    await session.discovery.map!(mapInput(0), new AbortController().signal);
    expect(JSON.stringify(session.record())).not.toContain(SECRET);
    const walk = (dir: string): string[] => readdirSync(dir).flatMap(e => { const f = path.join(dir, e); return statSync(f).isDirectory() ? walk(f) : [f]; });
    for (const file of walk(`${runDir}.state`)) expect(readFileSync(file, 'utf8')).not.toContain(SECRET);
  });
});
