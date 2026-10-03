import { execFileSync } from 'node:child_process';
import { chmodSync, existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterAll, afterEach, beforeAll, describe, expect, it, vi } from 'vitest';
import { quotableGenerationSources, type PipelineRequest, type PipelineResult, type ProviderDraft } from '@syzygy/polaris-generation-core';

import { main } from './dossier-main.js';
import { admissionRequirements, formatOutcome, gitLsRemote, gitMaterialize, noAdmissionRecords, parseGithubUrl, pinRevision, runDossierTrigger,
  type AdmissionRecordsPort, type TriggerPorts } from './dossier-trigger.js';

const SHA_A = 'a'.repeat(40), SHA_B = 'b'.repeat(40), SHA_C = 'c'.repeat(40);
const LS = `${SHA_A}\tHEAD\n${SHA_A}\trefs/heads/unstable\n${SHA_B}\trefs/tags/8.0.0\n${SHA_C}\trefs/tags/8.0.0^{}\n${SHA_B}\trefs/tags/light\n`;
const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });
const scratch = (): string => { const dir = mkdtempSync(join(tmpdir(), 'syzygy-trigger-')); cleanups.push(dir); return dir; };
const all: AdmissionRecordsPort = { source: 'fixture store', check: async r => ({ satisfied: true, record: `fixture/${r.kind}` }) };

describe('github url and revision pinning', () => {
  it('accepts public github urls and rejects everything else', () => {
    expect(parseGithubUrl('https://github.com/redis/redis')).toEqual({ owner: 'redis', repo: 'redis', url: 'https://github.com/redis/redis', repositoryId: 'github:redis:redis' });
    expect(parseGithubUrl('https://github.com/psf/requests.git/')).toMatchObject({ repo: 'requests', repositoryId: 'github:psf:requests' });
    expect(parseGithubUrl('https://github.com/redis/redis/tree/8.0.0')).toMatchObject({ ref: '8.0.0' });
    expect(parseGithubUrl('https://github.com/a/b.js').repositoryId).toBe('github:a:b_js');
    for (const bad of ['http://github.com/a/b', 'https://gitlab.com/a/b', 'https://user:pw@github.com/a/b', 'https://github.com/a', 'https://github.com/a/b/issues',
      'https://github.com/a/b/tree/../x', 'git@github.com:a/b.git', 'https://www.github.com/a/b', 'file:///tmp/x', 'https://github.com/a/b?x=1', 'https://github.com/-a/b', 'https://github.com/a/..']) {
      expect(() => parseGithubUrl(bad), bad).toThrow('invalid-github-url');
    }
  });

  it('pins HEAD, branches, lightweight tags and peels annotated tags to their commit', () => {
    expect(pinRevision(LS)).toEqual({ revision: SHA_A, resolvedRef: 'HEAD' });
    expect(pinRevision(LS, 'unstable')).toEqual({ revision: SHA_A, resolvedRef: 'refs/heads/unstable' });
    expect(pinRevision(LS, '8.0.0')).toEqual({ revision: SHA_C, resolvedRef: 'refs/tags/8.0.0' });
    expect(pinRevision(LS, 'light')).toEqual({ revision: SHA_B, resolvedRef: 'refs/tags/light' });
    expect(() => pinRevision(LS, 'nope')).toThrow('revision-not-found');
    expect(() => pinRevision(LS, SHA_A)).toThrow('unpinnable-revision');
    expect(() => pinRevision('garbage line\n')).toThrow('unreadable-ls-remote');
    expect(() => pinRevision('')).toThrow('revision-not-found');
  });
});

describe('trigger stops at the first unmet gate', () => {
  it('with no records wired, names every missing record and reads and fetches nothing', async () => {
    const lsRemote = vi.fn(() => LS), materialize = vi.fn(), runPipeline = vi.fn();
    const outcome = await runDossierTrigger('https://github.com/redis/redis/tree/8.0.0', { lsRemote, materialize, runPipeline });
    expect(lsRemote).toHaveBeenCalledWith('https://github.com/redis/redis');
    expect(materialize).not.toHaveBeenCalled();
    expect(runPipeline).not.toHaveBeenCalled();
    expect(outcome).toMatchObject({ state: 'admission-missing', revision: SHA_C, missing: 3, source: noAdmissionRecords.source });
    const text = formatOutcome(outcome);
    for (const kind of ['observation-consent', 'public-source-policy', 'egress-consent']) expect(text).toContain(`MISSING  ${kind}`);
    expect(text).toContain(`revision ${SHA_C}`);
    expect(text).toContain('STOPPED: 3 of 3 admission record(s) missing. No repository body was read and no provider was called.');
  });

  it('asks each requirement about the pinned revision, and one unmet record still stops', async () => {
    const asked: string[] = [];
    const records: AdmissionRecordsPort = { source: 'partial store', check: async r => { asked.push(`${r.kind}@${r.revision}`); return r.kind === 'egress-consent' ? { satisfied: false, why: 'no egress record' } : { satisfied: true, record: `r/${r.kind}` }; } };
    const materialize = vi.fn();
    const outcome = await runDossierTrigger('https://github.com/redis/redis', { lsRemote: () => LS, records, materialize });
    expect(asked.sort()).toEqual([`egress-consent@${SHA_A}`, `observation-consent@${SHA_A}`, `public-source-policy@${SHA_A}`]);
    expect(outcome).toMatchObject({ state: 'admission-missing', missing: 1 });
    expect(formatOutcome(outcome)).toContain('OK       observation-consent: r/observation-consent');
    expect(formatOutcome(outcome)).toContain('STOPPED: 1 of 3');
    expect(materialize).not.toHaveBeenCalled();
    expect(admissionRequirements(parseGithubUrl('https://github.com/a/b'), SHA_A).map(r => r.needs).join(' ')).toContain(SHA_A);
  });

  it('refuses a bad url or an unresolvable revision before consulting any record', async () => {
    const records = { source: 's', check: vi.fn() };
    expect(await runDossierTrigger('https://example.com/a/b', { records })).toMatchObject({ state: 'invalid-input' });
    expect(await runDossierTrigger('https://github.com/a/b', { records, lsRemote: () => { throw new Error('network down'); } })).toMatchObject({ state: 'unresolved-revision', reason: 'network down' });
    expect(await runDossierTrigger('https://github.com/a/b/tree/zz', { records, lsRemote: () => LS })).toMatchObject({ state: 'unresolved-revision', reason: 'revision-not-found' });
    expect(records.check).not.toHaveBeenCalled();
  });
});

describe('with every record satisfied', () => {
  let repo = '', commit = '';
  beforeAll(() => {
    repo = mkdtempSync(join(tmpdir(), 'syzygy-trigger-repo-'));
    const run = (...a: string[]): string => execFileSync('git', ['-C', repo, ...a], { encoding: 'utf8' }).trim();
    run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
    for (const [p, body] of Object.entries({ 'README.md': '# Fixture\nIt does a thing.\n', 'src/core.c': 'int core(void) { return 1; }\n', 'bin/blob': 'x' })) {
      mkdirSync(dirname(join(repo, p)), { recursive: true }); writeFileSync(join(repo, p), body);
    }
    run('add', '-A'); run('commit', '-qm', 'fixture'); commit = run('rev-parse', 'HEAD');
  });
  afterAll(() => rmSync(repo, { recursive: true, force: true }));
  const ls = () => `${commit}\tHEAD\n`;
  const draftFor = (request: PipelineRequest): ProviderDraft => {
    const [first, second] = quotableGenerationSources(request.sources);
    const a = first!.sourceId, b = second!.sourceId;
    const p = (id: string, ids: string[]) => ({ id, text: `Claim ${id}.`, sourceIds: ids, children: [] });
    return { title: 'Fixture dossier', introduction: p('intro', [a]), sections: [{ id: 'core-ideas', title: 'Core ideas', paragraphs: [p('ci', [b])], disposition: { kind: 'produced', assetIds: ['core-ideas'] } }],
      diagrams: [], deepDives: [], unresolved: [] };
  };
  const finished = (request: PipelineRequest): PipelineResult => ({ status: 'awaiting-rendered-review', draft: draftFor(request), inventory: null, review: null, receipts: [], artifacts: [] });
  const stoppedResult: PipelineResult = { status: 'stopped', reason: 'budget-exhausted', receipts: [], artifacts: [] };
  const render: NonNullable<TriggerPorts['render']> = ({ result, sources }) => ({ files: new Map([['index.html', `<p>${result.status} ${sources.length}</p>`], ['pages/core.html', '<p>core</p>']]) });
  const base = (extra: TriggerPorts = {}): TriggerPorts => ({ lsRemote: ls, records: all, materialize: async () => repo, ...extra });


  it('reads the pinned commit, discovers, clarifies and writes the site and a run record outside git', async () => {
    const out = join(scratch(), 'run');
    let seen: PipelineRequest | undefined;
    const outcome = await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out, render, runPipeline: async request => { seen = request; return finished(request); } }));
    expect(outcome).toMatchObject({ state: 'complete', revision: commit, detail: '2 files' });
    expect(readdirSync(out).sort()).toEqual(['index.html', 'pages', 'run-record.json']);
    expect(readFileSync(join(out, 'pages/core.html'), 'utf8')).toBe('<p>core</p>');
    expect(seen).toMatchObject({ projectId: 'github:fixture:repo', readerQuestions: expect.arrayContaining([expect.objectContaining({ id: 'core-ideas', topics: ['core-ideas'] })]) });
    const record = JSON.parse(readFileSync(join(out, 'run-record.json'), 'utf8'));
    expect(record).toMatchObject({ profile: 'dossier-v1', revision: commit, permissionIdentity: 'fixture/observation-consent+fixture/public-source-policy+fixture/egress-consent',
      corpusCount: { selected: 3 }, clarification: { mode: 'zero-interaction', unaccountedQuestions: 0 } });
    expect(record.clarification.wouldHaveAsked.map((q: { id: string }) => q.id)).toEqual(['audience']);
  });

  it('gives model-assisted discovery a receipt sink and keeps every receipt in the run record', async () => {
    const out = join(scratch(), 'run');
    const sunk: string[] = [];
    const outcome = await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out, discoveryReceipt: async r => { sunk.push(r.outcome); },
      discovery: { map: async input => ({ usageUnits: 1, claims: input.items.map(i => ({ blobId: i.blobId, claim: 'c', relevance: 5 })) }) } }));
    expect(outcome.state).toBe('generation-unavailable');
    const record = JSON.parse(readFileSync(join(out, 'run-record.json'), 'utf8'));
    expect(sunk).toEqual(['dispatching', 'accepted']);
    expect(record.discoveryReceipts.map((r: { outcome: string }) => r.outcome)).toEqual(['dispatching', 'accepted']);
    expect(record.discovery).toMatchObject({ mapCalls: 1, rankingBasis: 'model-map' });
  });

  it('records the corpus and stops honestly when no generate port exists or the pipeline stops', async () => {
    const out = join(scratch(), 'run');
    const unavailable = await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out }));
    expect(unavailable).toMatchObject({ state: 'generation-unavailable', runDir: out });
    expect(readdirSync(out)).toEqual(['run-record.json']);
    const out2 = join(scratch(), 'run');
    const stopped = await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out2, runPipeline: async () => stoppedResult }));
    expect(stopped).toMatchObject({ state: 'generation-stopped', detail: 'budget-exhausted' });
    expect(readdirSync(out2)).toEqual(['run-record.json']);
  });

  it('records an unrendered result when no renderer is wired, and refuses a renderer that collides with the run record', async () => {
    const out = join(scratch(), 'run');
    const outcome = await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out, runPipeline: async request => finished(request) }));
    expect(outcome).toMatchObject({ state: 'generation-unavailable', detail: expect.stringContaining('no renderer') });
    expect(readdirSync(out).sort()).toEqual(['pipeline-result.json', 'run-record.json']);
    const clash = join(scratch(), 'run');
    await expect(runDossierTrigger('https://github.com/fixture/repo', base({ outDir: clash, runPipeline: async request => finished(request),
      render: () => ({ files: new Map([['run-record.json', '{}']]) }) }))).rejects.toThrow('renderer-collides-with-run-record');
    expect(existsSync(clash)).toBe(false);
  });

  it('permits a discovery call only while the egress record still holds, and drops the calls otherwise', async () => {
    const map = vi.fn(async (input: { readonly readerQuestions: readonly string[]; readonly items: readonly { readonly blobId: string }[] }) => ({ usageUnits: 1, claims: input.items.map(i => ({ blobId: i.blobId, claim: 'c', relevance: 5 })) }));
    let checks = 0;
    const flipping: AdmissionRecordsPort = { source: 'flipping store', check: async r => (r.kind === 'egress-consent' && ++checks > 1 ? { satisfied: false, why: 'withdrawn' } : { satisfied: true, record: `fixture/${r.kind}` }) };
    const out = join(scratch(), 'run');
    await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out, records: flipping, discoveryReceipt: async () => undefined, discovery: { map } }));
    expect(map).not.toHaveBeenCalled();
    expect(JSON.parse(readFileSync(join(out, 'run-record.json'), 'utf8')).discovery.refusedCalls).toBeGreaterThan(0);
    const allowed = vi.fn(map);
    await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: join(scratch(), 'run'), discoveryReceipt: async () => undefined, discovery: { map: allowed } }));
    expect(allowed).toHaveBeenCalled();
    expect(allowed.mock.calls[0]![0].readerQuestions).toEqual(expect.arrayContaining([expect.stringContaining('core ideas')]));
  });

  it('removes its scratch checkout and an unused default run directory, even when the run fails', async () => {
    const before = () => readdirSync(tmpdir()).filter(name => name.startsWith('syzygy-dossier-'));
    const baseline = new Set(before());
    await expect(runDossierTrigger('https://github.com/fixture/repo', base({ materialize: async () => { throw new Error('fetch failed'); } }))).rejects.toThrow('fetch failed');
    await runDossierTrigger('https://github.com/fixture/repo', { lsRemote: ls, records: all });
    expect(before().filter(name => !baseline.has(name))).toEqual([]);
  });

  it('refuses a nonexistent output path under a git work tree and creates nothing', async () => {
    for (const rel of ['no/such/run', 'run']) {
      const target = join(repo, rel);
      await expect(runDossierTrigger('https://github.com/fixture/repo', base({ outDir: target }))).rejects.toThrow();
      expect(existsSync(join(repo, rel.split('/')[0]!))).toBe(false);
    }
  });

  it('wants a receipt sink whenever model discovery is wired, and lets no discovery port override the permission check', async () => {
    const map = async (input: { readonly items: readonly { readonly blobId: string }[] }) => ({ usageUnits: 1, claims: input.items.map(i => ({ blobId: i.blobId, claim: 'c', relevance: 5 })) });
    await expect(runDossierTrigger('https://github.com/fixture/repo', base({ outDir: join(scratch(), 'run'), discovery: { map } }))).rejects.toThrow('model-ports-need-a-receipt-port');
    const called = vi.fn(map);
    const withheld: AdmissionRecordsPort = { source: 's', check: (() => { let n = 0; return async (r: { kind: string }) => (r.kind === 'egress-consent' && ++n > 1 ? { satisfied: false as const, why: 'withdrawn' } : { satisfied: true as const, record: `r/${r.kind}` }); })() };
    await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: join(scratch(), 'run'), records: withheld, discoveryReceipt: async () => undefined,
      discovery: { map: called, permitted: async () => true } as never }));
    expect(called).not.toHaveBeenCalled();
  });

  it('refuses to write the run into a git work tree', async () => {
    const inside = join(repo, 'run');
    await expect(runDossierTrigger('https://github.com/fixture/repo', base({ outDir: inside }))).rejects.toThrow('run-directory-inside-git-work-tree');
    expect(existsSync(inside)).toBe(false);
  });

  it('fetches only the pinned commit objects into a bare, template-free repository, and refuses a non-https url by default', async () => {
    const dir = join(scratch(), 'src');
    expect(await gitMaterialize({ url: repo, revision: commit, dir }, 'file')).toBe(dir);
    expect(execFileSync('git', ['-C', dir, 'cat-file', '-t', commit], { encoding: 'utf8' }).trim()).toBe('commit');
    expect(execFileSync('git', ['-C', dir, 'rev-parse', '--is-bare-repository'], { encoding: 'utf8' }).trim()).toBe('true');
    expect(existsSync(join(dir, 'hooks'))).toBe(false);
    await expect(gitMaterialize({ url: repo, revision: commit, dir: join(scratch(), 'src2') })).rejects.toThrow();
  });

  describe('a poisoned caller environment', () => {
    it('reads the pinned fixture through the whole trigger while GIT_DIR and object variables point at another repository', async () => {
      const other = mkdtempSync(join(tmpdir(), 'syzygy-trigger-other-')); cleanups.push(other);
      execFileSync('git', ['-C', other, 'init', '-q']); writeFileSync(join(other, 'OTHER.md'), 'OTHER REPO\n');
      execFileSync('git', ['-C', other, 'add', '-A']); execFileSync('git', ['-C', other, '-c', 'user.email=o@example.invalid', '-c', 'user.name=O', 'commit', '-qm', 'o']);
      const saved = { ...process.env };
      Object.assign(process.env, { GIT_DIR: join(other, '.git'), GIT_OBJECT_DIRECTORY: join(other, 'nowhere'), GIT_ALTERNATE_OBJECT_DIRECTORIES: join(other, '.git', 'objects') });
      try {
        const out = join(scratch(), 'run');
        const outcome = await runDossierTrigger('https://github.com/fixture/repo', base({ outDir: out }));
        expect(outcome.state).toBe('generation-unavailable');
        const record = JSON.parse(readFileSync(join(out, 'run-record.json'), 'utf8'));
        expect(record.corpusCount).toMatchObject({ selected: 3 });
        expect(JSON.stringify(record)).not.toContain('OTHER');
      } finally { for (const key of Object.keys(process.env)) if (!(key in saved)) delete process.env[key]; Object.assign(process.env, saved); }
    });

    const saved = { ...process.env };
    afterEach(() => { for (const key of Object.keys(process.env)) if (!(key in saved)) delete process.env[key]; Object.assign(process.env, saved); });
    const poison = (): string => {
      const dir = scratch(), marker = join(dir, 'ran');
      for (const name of ['git-upload-pack', 'git-remote-https', 'askpass', 'ssh']) { writeFileSync(join(dir, name), `#!/bin/sh\necho ${name} >> ${marker}\nexit 1\n`); chmodSync(join(dir, name), 0o755); }
      Object.assign(process.env, { GIT_EXEC_PATH: dir, GIT_SSH_COMMAND: join(dir, 'ssh'), GIT_ASKPASS: join(dir, 'askpass'), GIT_PROXY_COMMAND: join(dir, 'ssh'),
        GIT_DIR: join(dir, 'nowhere'), GIT_WORK_TREE: dir, GIT_CONFIG_COUNT: '1', GIT_CONFIG_KEY_0: 'core.sshCommand', GIT_CONFIG_VALUE_0: join(dir, 'ssh'), GIT_CONFIG_PARAMETERS: `'core.sshCommand=${join(dir, 'ssh')}'` });
      return marker;
    };

    it('does not steer materialize: the fetch still succeeds and no poisoned program runs', async () => {
      const marker = poison();
      const dir = join(scratch(), 'src');
      await gitMaterialize({ url: repo, revision: commit, dir }, 'file');
      expect(execFileSync('git', ['-C', dir, 'cat-file', '-t', commit], { encoding: 'utf8', env: { PATH: process.env.PATH!, HOME: scratch() } }).trim()).toBe('commit');
      expect(existsSync(marker)).toBe(false);
    });

    it('does not steer ls-remote', () => {
      const marker = poison();
      expect(gitLsRemote(repo, 'file')).toContain(commit);
      expect(existsSync(marker)).toBe(false);
    });
  });
});

describe('command', () => {
  let repo = '', commit = '';
  beforeAll(() => {
    repo = mkdtempSync(join(tmpdir(), 'syzygy-trigger-cmd-'));
    const run = (...a: string[]): string => execFileSync('git', ['-C', repo, ...a], { encoding: 'utf8' }).trim();
    run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
    writeFileSync(join(repo, 'README.md'), '# Fixture\nIt does a thing.\n'); writeFileSync(join(repo, 'a.c'), 'int a;\n');
    run('add', '-A'); run('commit', '-qm', 'fixture'); commit = run('rev-parse', 'HEAD');
  });
  afterAll(() => rmSync(repo, { recursive: true, force: true }));
  const finishedFor = (request: PipelineRequest): PipelineResult => {
    const [first] = quotableGenerationSources(request.sources);
    const p = { id: 'intro', text: 'Claim.', sourceIds: [first!.sourceId], children: [] };
    return { status: 'awaiting-rendered-review', draft: { title: 't', introduction: p, sections: [], diagrams: [], deepDives: [], unresolved: [] }, inventory: null, review: null, receipts: [], artifacts: [] };
  };
  const wired = (extra: TriggerPorts = {}): TriggerPorts => ({ lsRemote: () => `${commit}\tHEAD\n`, records: all, materialize: async () => repo, ...extra });

  it('renders with the polaris-dossier-v1 renderer by default: a malformed finished result is refused by it, not written', async () => {
    const out = vi.spyOn(process.stdout, 'write').mockReturnValue(true);
    try {
      const dest = join(scratch(), 'site');
      await expect(main(['https://github.com/a/b', '--out', dest], wired({ runPipeline: async () => ({ status: 'awaiting-rendered-review', draft: {}, inventory: null, review: null, receipts: [], artifacts: [] }) }))).rejects.toThrow();
      expect(existsSync(dest)).toBe(false);
    } finally { out.mockRestore(); }
  });

  it('exits 0 and writes to --out on a complete run, 5 when generation is unavailable, 6 when the pipeline stops', async () => {
    const out = vi.spyOn(process.stdout, 'write').mockReturnValue(true);
    try {
      const dest = join(scratch(), 'site');
      const render: NonNullable<TriggerPorts['render']> = () => ({ files: new Map([['index.html', '<p>x</p>']]) });
      expect(await main(['https://github.com/a/b', '--out', dest], wired({ render, runPipeline: async request => finishedFor(request) }))).toBe(0);
      expect(readdirSync(dest).sort()).toEqual(['index.html', 'run-record.json']);
      expect(String(out.mock.calls.at(-1)![0])).toContain(`Run directory: ${dest}`);
      const dest5 = join(scratch(), 'site');
      expect(await main(['https://github.com/a/b', '--out', dest5], wired())).toBe(5);
      expect(readdirSync(dest5)).toEqual(['run-record.json']);
      const dest6 = join(scratch(), 'site');
      expect(await main(['https://github.com/a/b', '--out', dest6, '--json'], wired({ runPipeline: async () => ({ status: 'stopped', reason: 'cancelled', receipts: [], artifacts: [] }) }))).toBe(6);
      expect(JSON.parse(String(out.mock.calls.at(-1)![0]))).toMatchObject({ state: 'generation-stopped', detail: 'cancelled', runDir: dest6 });
    } finally { out.mockRestore(); }
  });

  it('exits 2 on usage, 3 when records are missing (text and json), and prints what is missing', async () => {
    const out = vi.spyOn(process.stdout, 'write').mockReturnValue(true), err = vi.spyOn(process.stderr, 'write').mockReturnValue(true);
    try {
      expect(await main([])).toBe(2);
      expect(await main(['https://github.com/a/b', 'extra'])).toBe(2);
      expect(await main(['https://github.com/a/b', '--out'])).toBe(2);
      expect(await main(['https://nope.example/a/b'])).toBe(2);
      expect(await main(['https://github.com/a/b'], { lsRemote: () => LS })).toBe(3);
      expect(String(out.mock.calls.at(-1)![0])).toContain('MISSING  observation-consent');
      expect(await main(['https://github.com/a/b', '--json'], { lsRemote: () => LS })).toBe(3);
      expect(JSON.parse(String(out.mock.calls.at(-1)![0]))).toMatchObject({ state: 'admission-missing', missing: 3 });
      expect(await main(['https://github.com/a/b'], { lsRemote: () => { throw new Error('x'); } })).toBe(4);
    } finally { out.mockRestore(); err.mockRestore(); }
  });
});
