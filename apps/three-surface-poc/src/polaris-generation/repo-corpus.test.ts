import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterAll, afterEach, beforeAll, describe, expect, it, vi } from 'vitest';

import { quotableGenerationSources, validateGenerationSources } from '@syzygy/polaris-generation-core';

import { main } from './repo-corpus-main.js';
import { buildPipelineRequest, CorpusRefusal, globToRegExp, parseReaderConfig, readRepoCorpus, refusingAdmission, type CorpusAdmissionPort } from './repo-corpus.js';

const allow: CorpusAdmissionPort = { decide: async () => ({ allowed: true, permissionIdentity: 'fixture-consent-v1' }) };
const budget = { maxCalls: 7, maxInputBytes: 5_000_000, maxOutputBytes: 1_000_000, maxUsageUnits: 100, maxElapsedMs: 30_000, maxRepairCycles: 1, accountingPolicy: 'fixture-v1' };
const configText = (extra: Record<string, unknown> = {}): string => JSON.stringify({ repositoryId: 'repository:fixture', revision: 'a'.repeat(40), readerQuestions: ['What is it?'],
  requestedAssets: [{ id: 'overview', kind: 'section', required: true }], budget, ...extra });
const cleanups: string[] = [];
afterAll(() => rmSync(root, { recursive: true, force: true }));
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });

let root = '', commit = '';
const big = `${'int line_of_code = 42; /* padding */\n'.repeat(3000)}end\n`;
beforeAll(() => {
  root = mkdtempSync(join(tmpdir(), 'syzygy-repo-corpus-'));
  // removed in afterAll
  const run = (...args: string[]): string => execFileSync('git', ['-C', root, ...args], { encoding: 'utf8' }).trim();
  run('init', '-q'); run('config', 'user.email', 'f@example.invalid'); run('config', 'user.name', 'F');
  const files: Record<string, string | Buffer> = { 'src/a.c': 'int a(void) { return 1; }\n', 'src/big.c': big, 'docs/readme.md': '# Readme\n',
    'vendor/dep/x.c': 'VENDOR\n', 'assets/logo.bin': Buffer.from([0, 1, 2, 3]), 'assets/latin1.txt': Buffer.from([0xe9, 0x0a]) };
  for (const [path, body] of Object.entries(files)) { mkdirSync(dirname(join(root, path)), { recursive: true }); writeFileSync(join(root, path), body); }
  symlinkSync('a.c', join(root, 'src/link.c'));
  run('add', '-A'); run('commit', '-qm', 'fixture');
  commit = run('rev-parse', 'HEAD');
  writeFileSync(join(root, 'src/a.c'), 'LOCAL-EDIT-SENTINEL\n');
  writeFileSync(join(root, 'src/untracked.c'), 'UNTRACKED-SENTINEL\n');
});

const cfg = (extra: Partial<Parameters<typeof readRepoCorpus>[1]> = {}) => ({ repositoryId: 'repository:fixture', revision: commit, include: ['**'], exclude: ['vendor/**'], oversize: 'split' as const, ...extra });

describe('admission gate', () => {
  it('refuses by default before any git access', async () => {
    const readBlobs = vi.fn();
    await expect(readRepoCorpus('/nonexistent/never-touched', cfg(), { readBlobs })).rejects.toThrow(CorpusRefusal);
    await expect(readRepoCorpus('/nonexistent/never-touched', cfg(), { admission: refusingAdmission, readBlobs })).rejects.toThrow(/no-admission-port/);
    expect(readBlobs).not.toHaveBeenCalled();
  });

  it('refuses unless the port answers exactly allowed: true, and passes it the request', async () => {
    const decide = vi.fn(async () => ({ allowed: 'yes' }) as never);
    await expect(readRepoCorpus(root, cfg(), { admission: { decide } })).rejects.toThrow(CorpusRefusal);
    expect(decide).toHaveBeenCalledWith({ repositoryId: 'repository:fixture', revision: commit, include: ['**'], exclude: ['vendor/**'] });
  });
});

describe('any-repo reader', () => {
  it('accounts for every tree entry and reads only the pinned commit', async () => {
    const corpus = await readRepoCorpus(root, cfg(), { admission: allow });
    expect(corpus.count).toEqual({ listed: 7, notBlob: 1, outsideInclude: 0, excludedByGlob: 1, selected: 5, binaryOrNonUtf8: 2, oversizeFiles: 1, oversizeExcluded: 0 });
    const text = JSON.stringify(corpus);
    for (const sentinel of ['LOCAL-EDIT-SENTINEL', 'UNTRACKED-SENTINEL', 'VENDOR']) expect(text).not.toContain(sentinel);
    expect(corpus.permissionIdentity).toBe('fixture-consent-v1');
    expect(corpus.sources.filter(s => s.exclusion.excluded).map(s => [s.path, s.exclusion])).toEqual([
      ['assets/latin1.txt', { excluded: true, reason: 'binary-or-non-utf8' }], ['assets/logo.bin', { excluded: true, reason: 'binary-or-non-utf8' }]]);
    expect(corpus.sources.find(s => s.path === 'src/a.c')!.body).toBe('int a(void) { return 1; }\n');
    expect(validateGenerationSources(corpus.sources)).toBe(corpus.sources);
  });

  it('splits an oversize file into pieces, or excludes it with a reason', async () => {
    const split = await readRepoCorpus(root, cfg(), { admission: allow });
    const pieces = split.sources.filter(s => s.path === 'src/big.c');
    expect(pieces.length).toBeGreaterThan(1);
    expect(pieces.map(p => p.body).join('')).toBe(big);
    const excluded = await readRepoCorpus(root, cfg({ oversize: 'exclude' }), { admission: allow });
    expect(excluded.sources.filter(s => s.path === 'src/big.c')).toMatchObject([{ exclusion: { excluded: true, reason: 'oversize-source-excluded' } }]);
    expect(excluded.count.oversizeExcluded).toBe(1);
    expect(quotableGenerationSources(excluded.sources).map(q => q.sourceId)).not.toContain(pieces[0]!.sourceId);
  });

  it('applies include then exclude globs and counts what each removed', async () => {
    const corpus = await readRepoCorpus(root, cfg({ include: ['src/*.c', 'docs/**'], exclude: ['src/big.c'] }), { admission: allow });
    expect(corpus.sources.map(s => s.path)).toEqual(['docs/readme.md', 'src/a.c']);
    expect(corpus.count).toMatchObject({ listed: 7, outsideInclude: 3, excludedByGlob: 1, notBlob: 1, selected: 2 });
  });

  it('refuses an unpinned or unknown revision', async () => {
    await expect(readRepoCorpus(root, cfg({ revision: 'main' }), { admission: allow })).rejects.toThrow('invalid-pinned-commit');
    await expect(readRepoCorpus(root, cfg({ revision: '0'.repeat(40) }), { admission: allow })).rejects.toThrow();
    await expect(readRepoCorpus(root, cfg({ repositoryId: 'bad id!' }), { admission: allow })).rejects.toThrow('invalid-repository-id');
  });

  it('is deterministic for one commit', async () => {
    const a = await readRepoCorpus(root, cfg(), { admission: allow }), b = await readRepoCorpus(root, cfg(), { admission: allow });
    expect(a.identityDigest).toBe(b.identityDigest);
  });
});

describe('globs and config', () => {
  it('matches ** across directories, * within one, and ? for one character', () => {
    expect(globToRegExp('**/*.c').test('a.c')).toBe(true);
    expect(globToRegExp('**/*.c').test('x/y/a.c')).toBe(true);
    expect(globToRegExp('src/*.c').test('src/deep/a.c')).toBe(false);
    expect(globToRegExp('src/**').test('src/deep/a.c')).toBe(true);
    expect(globToRegExp('a?.c').test('ab.c')).toBe(true);
    expect(globToRegExp('a?.c').test('a/.c')).toBe(false);
    expect(globToRegExp('a.c').test('abc')).toBe(false);
  });

  it('parses a strict config and lets flags override identity and globs', () => {
    const parsed = parseReaderConfig(configText(), { revision: 'b'.repeat(40), include: ['x/**'] });
    expect(parsed).toMatchObject({ repositoryId: 'repository:fixture', revision: 'b'.repeat(40), include: ['x/**'], exclude: [], oversize: 'split' });
    expect(() => parseReaderConfig(configText({ extra: 1 }))).toThrow('config-invalid');
    expect(() => parseReaderConfig(configText({ budget: { ...budget, maxCalls: -1 } }))).toThrow('config-invalid: budget');
    expect(() => parseReaderConfig(configText({ oversize: 'truncate' }))).toThrow('config-invalid: oversize');
    expect(() => parseReaderConfig(configText({ requestedAssets: [{ id: 'x' }] }))).toThrow();
    expect(() => parseReaderConfig(configText({ revision: 'main' }))).toThrow('invalid-pinned-commit');
  });

  it('builds a pipeline request carrying the config questions, assets and budget', async () => {
    const config = parseReaderConfig(configText({ revision: commit }));
    const corpus = await readRepoCorpus(root, config, { admission: allow });
    const request = buildPipelineRequest(corpus, config, 1);
    expect(request).toMatchObject({ projectId: 'repository:fixture', readerQuestions: ['What is it?'], budget, snapshotId: corpus.identityDigest });
    expect(request.routes.author).toBe('provider-author');
    expect(request.sources).toBe(corpus.sources);
  });
});

describe('cli', () => {
  it('exits 1 with the refusal under the default port and 0 with an allowing port', async () => {
    const dir = mkdtempSync(join(tmpdir(), 'syzygy-repo-cli-'));
    cleanups.push(dir);
    writeFileSync(join(dir, 'c.json'), configText({ revision: commit }));
    const err = vi.spyOn(process.stderr, 'write').mockReturnValue(true), out = vi.spyOn(process.stdout, 'write').mockReturnValue(true);
    try {
      expect(await main(['--repo', root, '--config', join(dir, 'c.json')])).toBe(1);
      expect(String(err.mock.calls.at(-1)![0])).toContain('Corpus read refused');
      expect(await main(['--repo', root, '--config', join(dir, 'c.json'), '--exclude', 'vendor/**'], allow)).toBe(0);
      const report = JSON.parse(String(out.mock.calls.at(-1)![0]));
      expect(report).toMatchObject({ realProviderCalls: 0, count: { selected: 5 } });
      expect(JSON.stringify(report)).not.toContain('int a(void)');
      expect(await main(['--repo', root])).toBe(2);
    } finally { err.mockRestore(); out.mockRestore(); }
  });
});
