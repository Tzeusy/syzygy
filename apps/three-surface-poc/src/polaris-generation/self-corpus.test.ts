import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { proveSelfCorpus, readSelfCorpus } from './self-corpus.js';

const PINNED_MAIN = '133106eb0f2564f1cefddd19d11985f1b2619397';
const cleanups: string[] = [];
afterEach(() => { for (const path of cleanups.splice(0)) rmSync(path, { recursive: true, force: true }); });

describe('zero-egress Syzygy self-corpus proof', () => {
  it('reads only tracked blobs from the pinned commit and independently recounts its denominator', () => {
    const corpus = readSelfCorpus(process.cwd(), PINNED_MAIN);
    const names = execFileSync('git', ['ls-tree', '-r', '--name-only', PINNED_MAIN, '--',
      '.syzygy/governance/doctrine', '.syzygy/governance/decisions', '.syzygy/governance/contracts/rfcs'], { encoding: 'utf8' }).trim().split('\n');
    const selected = names.filter(path => /^\.syzygy\/governance\/(?:doctrine\/[^/]+|decisions\/.+|contracts\/rfcs\/RFC-[^/]+\/[^/]+)\.md$/u.test(path));
    expect(corpus.count.selected).toBe(selected.length);
    expect(corpus.count.selected).toBeGreaterThan(100);
    expect(corpus.count.excludedMarkdown).toBe(2);
    expect(corpus.sources.map(source => source.path).sort()).toEqual(selected.sort());
    expect(corpus.sources.every(source => source.body !== undefined && source.spans.length === 1)).toBe(true);
    expect(corpus.over100000Characters).toBe(0);
  });

  it('refuses a 1 MB corpus budget without truncation or a scripted send, then completes on sufficient budget and isolates one source perturbation', async () => {
    const report = await proveSelfCorpus(process.cwd(), PINNED_MAIN);
    expect(report.budgetExhausted).toMatchObject({ status: 'stopped', reason: 'budget-exhausted', scriptedCalls: 0 });
    expect(report.sufficient.status).toBe('awaiting-rendered-review');
    expect(report.sufficient.stageInputs.map(entry => entry.stage)).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity']);
    expect(report.sufficient.stageInputs[0]!.inputBytes).toBeGreaterThan(1_000_000);
    expect(report.sufficient.stageInputs.slice(1).every(entry => entry.inputBytes < report.sufficient.stageInputs[0]!.inputBytes)).toBe(true);
    expect(report.perturbation).toMatchObject({ changedBlockIds: ['intro'], unchangedBlockIds: ['account-paragraph'], changedCitationCount: 1, unchangedCitationCount: 1 });
    expect(report.realProviderCalls).toBe(0);
    expect(report.networkCalls).toBe(0);
    expect(report.realProjectProof).toBe(false);
    expect(report.unmetReq014).toContain('two separately admitted real projects');
  }, 30_000);

  it('does not read a local or untracked file even when it lies in the allowed-looking path', () => {
    const root = mkdtempSync(join(tmpdir(), 'syzygy-self-corpus-fixture-'));
    cleanups.push(root);
    execFileSync('git', ['init', '-q', root]);
    execFileSync('git', ['-C', root, 'config', 'user.email', 'fixture@example.invalid']);
    execFileSync('git', ['-C', root, 'config', 'user.name', 'Fixture']);
    const tracked = '.syzygy/governance/doctrine/vision.md';
    const untracked = '.syzygy/governance/doctrine/local.md';
    for (const [path, body] of [[tracked, '# Tracked vision\n'], [untracked, 'UNTRACKED-SENTINEL\n']] as const) {
      mkdirSync(dirname(join(root, path)), { recursive: true });
      writeFileSync(join(root, path), body);
    }
    execFileSync('git', ['-C', root, 'add', tracked]);
    execFileSync('git', ['-C', root, 'commit', '-qm', 'fixture']);
    const commit = execFileSync('git', ['-C', root, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
    writeFileSync(join(root, tracked), 'LOCAL-EDIT-SENTINEL\n');
    const corpus = readSelfCorpus(root, commit);
    expect(corpus.count.selected).toBe(1);
    expect(corpus.sources[0]?.body).toBe('# Tracked vision\n');
    expect(JSON.stringify(corpus)).not.toContain('UNTRACKED-SENTINEL');
    expect(JSON.stringify(corpus)).not.toContain('LOCAL-EDIT-SENTINEL');
  });
});
