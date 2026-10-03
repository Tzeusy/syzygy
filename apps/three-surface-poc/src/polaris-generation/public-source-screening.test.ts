import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';

import { excludedSourceId, runGenerationPipeline, stageSchema, validateGenerationSources, validateStage, reviewVerdict, type GenerationSource, type PipelinePorts, type PipelineResult } from '@syzygy/polaris-generation-core';
import { compileDetectors, detectSecrets, PWB_DENIED_PATH_RULES, PWB_SECRET_POLICY } from '@syzygy/three-surface-poc-core';

import { renderDossier } from './dossier-render.js';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';
import { checkoutPolicyActPort, loadPublicSourceScreen, readScreenedRepoCorpus, type PublicSourcePolicyActPort } from './public-source-screening.js';
import { buildPipelineRequest, CorpusRefusal, readRepoCorpus, type CorpusAdmissionPort, type ReaderConfig } from './repo-corpus.js';

// Every secret is assembled at runtime so no literal token sits in this file.
const SECRETS = {
  'private-key-material': `-----BEGIN ${'OPENSSH'} PRIVATE KEY-----\nAAAAsyntheticfixture\n`,
  'known-token-formats': `const id = "${'AK'}IA${'Q'.repeat(16)}";\n`,
  'credential-assignment': `db_${'pass'}word = "${'correcthorse'}-fixture"\n`,
  'credential-bearing-url': `const u = "https://alice:${'hunter2'}@example.invalid/";\n`,
} as const;
const SENTINEL = 'SCREEN-SENTINEL-7f3a';
const FILES: Record<string, string> = {
  'src/clean.c': `int answer(void) { return 42; } /* ${'clean-body-marker'} */\n`,
  'src/secret-key-material.txt': `${SENTINEL}\n${SECRETS['private-key-material']}`,
  'src/secret-token.js': `${SENTINEL}\n${SECRETS['known-token-formats']}`,
  'src/secret-assignment.py': `${SENTINEL}\n${SECRETS['credential-assignment']}`,
  'src/secret-url.ts': `${SENTINEL}\n${SECRETS['credential-bearing-url']}`,
  // A detector runs inside inert code contexts too.
  'docs/secret-fenced.md': `${SENTINEL}\n\`\`\`\n${SECRETS['private-key-material']}\`\`\`\n`,
  'docs/active-script.md': `${SENTINEL}\n<script>alert(1)</script>\n`,
  'docs/active-unclosed.md': `${SENTINEL}\n\`\`\`\nnever closed\n`,
  // An inert fence keeps markup inert: admitted.
  'docs/inert.md': '# Inert\n\n```html\n<b>shown as code</b>\n```\n',
  '.env': `${SENTINEL}\nX=1\n`,
  'certs/denied-server.pem': `${SENTINEL}\n`,
};
const WITHHELD = Object.keys(FILES).filter(path => FILES[path]!.includes(SENTINEL));
const allow: CorpusAdmissionPort = { decide: async () => ({ allowed: true, permissionIdentity: 'fixture-consent-v1' }) };
const budget = { maxCalls: 7, maxInputBytes: 5_000_000, maxOutputBytes: 1_000_000, maxUsageUnits: 100, maxElapsedMs: 30_000, maxRepairCycles: 1, accountingPolicy: 'fixture-v1' };

const policyBytes = (extra: Record<string, unknown> = { publicSourceScope: { purpose: 'synthetic fixture scope' } }): Uint8Array => new TextEncoder().encode(`${JSON.stringify({
  policyId: 'synthetic-public-source-policy', policyVersion: '9.9.0-fixture.1',
  sourceAdmission: { deniedPathBasenames: PWB_DENIED_PATH_RULES.basenames, deniedPathPrefixes: PWB_DENIED_PATH_RULES.prefixes, deniedPathSuffixes: PWB_DENIED_PATH_RULES.suffixes },
  detectors: PWB_SECRET_POLICY.detectors, ...extra,
}, null, 2)}\n`);
const sha = (bytes: Uint8Array): string => createHash('sha256').update(bytes).digest('hex');
const actRecord = (digest: string, overrides: { readonly identity?: string; readonly type?: string; readonly artifact?: string } = {}): string => [
  '# Owner act — synthetic fixture', '',
  overrides.identity ?? 'Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-APPROVAL-2026-10-03`', '',
  overrides.type ?? 'Act type: `approve-policy`', '',
  'Project identity: `project:syzygy`', '',
  overrides.artifact ?? 'Artifact identity: `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`', '',
  `Exact digest (SHA-256): \`${digest}\``, '',
].join('\n');
const port = (record: string | undefined, policy: Uint8Array | undefined): PublicSourcePolicyActPort => ({ read: async () => ({ actRecord: record, policy }) });
const goodPolicy = policyBytes();
const goodPort = port(actRecord(sha(goodPolicy)), goodPolicy);

let root = '', commit = '', emptyRoot = '', emptyCommit = '';
const scratch: string[] = [];
const fixtureRepo = (files: Record<string, string>): { root: string; commit: string } => {
  const dir = mkdtempSync(join(tmpdir(), 'syzygy-public-screen-'));
  scratch.push(dir);
  const run = (...args: string[]): string => execFileSync('git', ['-C', dir, ...args], { encoding: 'utf8' }).trim();
  run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
  for (const [path, body] of Object.entries(files)) { mkdirSync(dirname(join(dir, path)), { recursive: true }); writeFileSync(join(dir, path), body); }
  run('add', '-A'); run('commit', '-q', '--allow-empty', '-m', 'fixture');
  return { root: dir, commit: run('rev-parse', 'HEAD') };
};
beforeAll(() => {
  ({ root, commit } = fixtureRepo(FILES));
  ({ root: emptyRoot, commit: emptyCommit } = fixtureRepo({}));
});
afterAll(() => { for (const dir of scratch) rmSync(dir, { recursive: true, force: true }); });

const cfg = (revision = commit) => ({ repositoryId: 'repository:fixture', revision, include: ['**'], exclude: [], oversize: 'split' as const });
const leaks = (text: string): string[] => [SENTINEL, ...Object.values(SECRETS).map(secret => secret.trim()), ...WITHHELD].filter(needle => text.includes(needle));

describe('synthetic secrets of each detector class', () => {
  it('each fixture matches exactly its own detector, so each class is exercised alone', () => {
    for (const [id, text] of Object.entries(SECRETS)) {
      const hits = PWB_SECRET_POLICY.detectors.filter(detector => detectSecrets(compileDetectors({ detectors: [detector] }), text) !== undefined).map(detector => detector.id);
      expect(hits).toEqual([id]);
    }
  });

  it('withholds every secret, active-content and denied-path blob and admits the rest', async () => {
    const corpus = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort });
    expect(corpus.count).toMatchObject({ listed: 11, selected: 11, deniedPath: 2, secretDetectorMatches: 5, activeContent: 2, sourceRows: 11 });
    const reasons = corpus.sources.filter(source => source.exclusion.excluded).map(source => source.exclusion.excluded ? source.exclusion.reason : '').sort();
    expect(reasons).toEqual(['active-content', 'active-content', 'denied-path', 'denied-path',
      'secret-detector-match', 'secret-detector-match', 'secret-detector-match', 'secret-detector-match', 'secret-detector-match']);
    expect(corpus.sources.filter(source => !source.exclusion.excluded).map(source => source.path).sort()).toEqual(['docs/inert.md', 'src/clean.c']);
    validateGenerationSources(corpus.sources);
  });

  it('a withheld row carries an opaque per-run id and no path, object id or body', async () => {
    const key = Buffer.alloc(32, 7);
    const a = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort, runKey: key });
    const b = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort, runKey: key });
    const c = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort, runKey: Buffer.alloc(32, 8) });
    const ids = (corpus: typeof a) => corpus.sources.filter(source => source.exclusion.excluded).map(source => source.sourceId).sort();
    expect(ids(a)).toEqual(ids(b));
    expect(ids(a).filter(id => ids(c).includes(id))).toEqual([]);
    const plain = await readRepoCorpus(root, cfg(), { admission: allow });
    expect(ids(a).filter(id => plain.sources.some(source => source.sourceId === id))).toEqual([]);
    for (const source of a.sources.filter(row => row.exclusion.excluded)) {
      expect(source).toEqual({ repositoryId: 'repository:fixture', revision: commit, path: `withheld/${source.sourceId}`, objectId: null,
        evaluationId: `corpus:repository:fixture@${commit}`, sourceId: source.sourceId, classificationBasis: 'body', exclusion: source.exclusion, spans: [] });
      expect(source.sourceId).toMatch(/^s-[0-9a-f]{24}$/u);
    }
  });

  it('a denied path is withheld without its blob being read', async () => {
    const read: string[][] = [];
    const { readGitBlobsBatch } = await import('../git-blob-batch.js');
    await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort, readBlobs: (repo, objects) => { read.push([...objects]); return readGitBlobsBatch(repo, objects); } });
    const deniedIds = ['.env', 'certs/denied-server.pem'].map(path => execFileSync('git', ['-C', root, 'rev-parse', `${commit}:${path}`], { encoding: 'utf8' }).trim());
    expect(read.flat().filter(id => deniedIds.includes(id))).toEqual([]);
    expect(read.flat()).toHaveLength(9);
  });

  it('one run key keys the withheld rows and an ordinary excluded row alike (syzygy-75ds)', async () => {
    const key = Buffer.alloc(32, 9);
    const { readGitBlobsBatch } = await import('../git-blob-batch.js');
    const cleanId = execFileSync('git', ['-C', root, 'rev-parse', `${commit}:src/clean.c`], { encoding: 'utf8' }).trim();
    const corpus = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort, runKey: key,
      readBlobs: (repo, objects) => new Map([...readGitBlobsBatch(repo, objects)].map(([id, bytes]) => [id, id === cleanId ? new Uint8Array([0]) : bytes])) });
    expect(corpus.sources.find(source => source.path === 'src/clean.c')).toMatchObject({ sourceId: excludedSourceId(key, 'src/clean.c'), exclusion: { excluded: true, reason: 'binary-or-non-utf8' } });
  });
});

describe('excluded bodies never leave the process', () => {
  it('no secret, path or body reaches the provider port, its receipts, the run record or a rendered page', async () => {
    const corpus = await readScreenedRepoCorpus(root, cfg(), { admission: allow, policyAct: goodPort });
    const config: ReaderConfig = { ...cfg(), readerQuestions: [{ id: 'core-ideas', topics: ['core-ideas'], text: 'What is it?' }], requestedAssets: [{ id: 'overview', kind: 'section', required: true }], budget };
    const request = buildPipelineRequest(corpus, config, 1_000);
    const sent: string[] = [], receipts: unknown[] = [];
    let ordinal = 0;
    const ports: PipelinePorts = {
      now: () => 1_000, verifySources: async () => true, permissionIdentity: async () => 'fixture-permission',
      admit: async () => ({ kind: 'reserved', permit: { attemptId: `a${ordinal++}`, maxUsageUnits: 5, maxOutputBytes: 10_000 } }),
      permitted: async () => true, releaseUnsent: async () => undefined, responseSchema: stageSchema, validate: validateStage, fidelity: reviewVerdict,
      // The stubbed provider: it records every byte offered and answers nothing usable, so the run stops after one call.
      generate: async input => { sent.push(input.system, input.input); return { body: '{}', model: 'stub', usageUnits: 1 }; },
      record: async (permit, outcome) => { receipts.push({ permit, outcome }); },
      lateReceipt: async () => undefined,
    };
    const result: PipelineResult = await runGenerationPipeline(request, ports, new AbortController().signal);
    expect(sent.length).toBeGreaterThan(0);
    expect(sent.join('\n')).toContain('clean-body-marker');
    expect(leaks(sent.join('\n'))).toEqual([]);
    expect(leaks(JSON.stringify(receipts))).toEqual([]);
    expect(leaks(JSON.stringify(result))).toEqual([]);
    // The run record the trigger writes, and the full request with its sources.
    expect(leaks(JSON.stringify({ permissionIdentity: corpus.permissionIdentity, corpusCount: corpus.count, request }))).toEqual([]);
    const synthetic = await runSyntheticProject(syntheticProjects[0]!);
    if (synthetic.result.status !== 'awaiting-rendered-review') throw new Error('synthetic pipeline stopped');
    const withheld: GenerationSource[] = corpus.sources.filter(source => source.exclusion.excluded);
    const { files } = renderDossier({ result: synthetic.result, sources: [...synthetic.sources, ...withheld] });
    const pages = [...files.values()].join('\n');
    for (const source of withheld) expect(pages).toContain(source.sourceId);
    expect(leaks(pages)).toEqual([]);
  });
});

describe('the policy act gate fails closed', () => {
  const refusal = async (policyAct: PublicSourcePolicyActPort): Promise<string> => {
    let touched = false;
    const watching: CorpusAdmissionPort = { decide: async request => { touched = true; return allow.decide(request); } };
    const error = await readScreenedRepoCorpus(root, cfg(), { admission: watching, policyAct }).then(() => undefined, (caught: unknown) => caught);
    expect(error).toBeInstanceOf(CorpusRefusal);
    expect(touched).toBe(false);
    return (error as CorpusRefusal).reason;
  };
  it('refuses with no act record', async () => { expect(await refusal(port(undefined, goodPolicy))).toMatch(/^public-source-policy: no act record/u); });
  it('refuses with no policy', async () => { expect(await refusal(port(actRecord(sha(goodPolicy)), undefined))).toMatch(/^public-source-policy: no policy/u); });
  it('refuses when the policy does not hash to the act argument', async () => {
    expect(await refusal(port(actRecord(sha(goodPolicy)), policyBytes({ publicSourceScope: { purpose: 'other bytes' } })))).toBe('public-source-policy: policy bytes do not hash to the act argument');
  });
  it('refuses an act record of another act', async () => {
    const digest = sha(goodPolicy);
    for (const overrides of [{ identity: 'Act identity: `PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-2026-10-02`' }, { type: 'Act type: `approve-registry-entry`' }, { artifact: 'Artifact identity: `other.json`' }]) {
      expect(await refusal(port(actRecord(digest, overrides), goodPolicy))).toBe('public-source-policy: act record is not the public-source scope approve-policy act');
    }
  });
  it('refuses a record naming two digests', async () => {
    expect(await refusal(port(`${actRecord(sha(goodPolicy))}Exact digest (SHA-256): \`${'0'.repeat(64)}\`\n`, goodPolicy))).toBe('public-source-policy: act record does not name exactly one exact digest');
  });
  it('refuses approved bytes without a publicSourceScope', async () => {
    const bare = policyBytes({});
    expect(await refusal(port(actRecord(sha(bare)), bare))).toBe('public-source-policy: policy carries no publicSourceScope');
  });
  it('refuses a policy whose detectors or denied paths cannot be read', async () => {
    const noDetectors = policyBytes({ publicSourceScope: {}, detectors: [] });
    expect(await refusal(port(actRecord(sha(noDetectors)), noDetectors))).toMatch(/^public-source-policy: detectors: /u);
    // Each of the three lists, missing alone, refuses.
    for (const missing of ['deniedPathBasenames', 'deniedPathPrefixes', 'deniedPathSuffixes']) {
      const lists: Record<string, readonly string[]> = { deniedPathBasenames: ['.env'], deniedPathPrefixes: ['.env.'], deniedPathSuffixes: ['.pem'] };
      delete lists[missing];
      const noDenied = policyBytes({ publicSourceScope: {}, sourceAdmission: lists });
      expect(await refusal(port(actRecord(sha(noDenied)), noDenied))).toBe('public-source-policy: policy denied-path rules unreadable');
    }
  });
  it('refuses a short run key', async () => {
    await expect(loadPublicSourceScreen(goodPort, new Uint8Array(16))).rejects.toThrow('run key shorter than 32 bytes');
  });
  it('the default port reads this checkout: no act record refuses, a performed one loads the policy it names', async () => {
    const repo = new URL('../../../../', import.meta.url);
    const record = await import('node:fs').then(fs => fs.existsSync(new URL('.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md', repo)));
    if (!record) await expect(loadPublicSourceScreen(checkoutPolicyActPort())).rejects.toThrow(/^Corpus read refused: public-source-policy: no act record/u);
    else expect((await loadPublicSourceScreen(checkoutPolicyActPort())).policyId).toBe('polaris-butlers-project-shape-secrets');
  });
});

describe('an empty corpus', () => {
  it('a commit with no blobs is refused by the population validator, never read as an empty success', async () => {
    await expect(readScreenedRepoCorpus(emptyRoot, cfg(emptyCommit), { admission: allow, policyAct: goodPort })).rejects.toThrow('Generation source rejected: invalid-source');
  });

  it('a corpus screened down to nothing admitted makes no provider call', async () => {
    const only = fixtureRepo({ 'src/secret-token.js': FILES['src/secret-token.js']!, 'docs/active-script.md': FILES['docs/active-script.md']! });
    const corpus = await readScreenedRepoCorpus(only.root, cfg(only.commit), { admission: allow, policyAct: goodPort });
    expect(corpus.count).toMatchObject({ selected: 2, secretDetectorMatches: 1, activeContent: 1, sourceRows: 2 });
    const request = buildPipelineRequest(corpus, { ...cfg(only.commit), readerQuestions: [{ id: 'core-ideas', topics: ['core-ideas'], text: 'What is it?' }], requestedAssets: [{ id: 'overview', kind: 'section', required: true }], budget }, 1_000);
    let calls = 0;
    const refuseAll = async (): Promise<never> => { calls++; throw new Error('unreachable'); };
    const result = await runGenerationPipeline(request, { now: () => 1_000, verifySources: async () => true, permissionIdentity: refuseAll, admit: refuseAll, permitted: refuseAll,
      releaseUnsent: refuseAll, responseSchema: stageSchema, validate: validateStage, fidelity: reviewVerdict, generate: refuseAll, record: refuseAll, lateReceipt: refuseAll }, new AbortController().signal);
    expect(result).toMatchObject({ status: 'stopped', reason: 'source-refused' });
    expect(calls).toBe(0);
  });
});
