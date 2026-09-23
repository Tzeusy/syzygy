import { execFileSync } from 'node:child_process';
import { mkdtempSync, readdirSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';

const cleanups: string[] = [];
afterEach(() => { for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true }); });

describe('concrete source-to-draft pipeline exercise', () => {
  it('runs the same engine and schemas over two synthetic domains with prose, diagrams and component depth', async () => {
    const runs = await Promise.all(syntheticProjects.map(runSyntheticProject));
    for (const run of runs) {
      expect(run.result.status).toBe('awaiting-rendered-review');
      if (run.result.status !== 'awaiting-rendered-review') throw Error(run.result.reason);
      expect(run.result.receipts.map(r => r.stage)).toEqual(['inventory', 'plan', 'author', 'edit', 'fidelity']);
      expect(run.result.draft).toMatchObject({ diagrams: [{ edges: [{ label: 'feeds' }] }], deepDives: [{ id: 'component-depth' }] });
    }
    expect(runs[0]!.result.receipts.map(r => r.promptVersion)).toEqual(runs[1]!.result.receipts.map(r => r.promptVersion));
  });

  it('binds changed source meaning to fresh inventory, draft and fidelity inputs', async () => {
    const first = syntheticProjects[0]!;
    const a = await runSyntheticProject(first);
    const b = await runSyntheticProject({ ...first, qualification: `${first.qualification} Winter care has different timing.` });
    expect(a.result.status).toBe('awaiting-rendered-review');
    expect(b.result.status).toBe('awaiting-rendered-review');
    for (const stage of ['inventory', 'author', 'fidelity']) {
      expect(a.result.receipts.find(r => r.stage === stage)?.inputDigest).not.toBe(b.result.receipts.find(r => r.stage === stage)?.inputDigest);
    }
    expect(a.result.receipts.find(r => r.stage === 'author')?.outputDigest).not.toBe(b.result.receipts.find(r => r.stage === 'author')?.outputDigest);
  });

  it('runs the README command after a clean install and requires exactly seven synthetic output files', () => {
    const readme = readFileSync(join(process.cwd(), 'packages/polaris-generation-core/README.md'), 'utf8');
    expect(JSON.parse(readFileSync(join(process.cwd(), 'package.json'), 'utf8')).scripts['build:poc']).toContain('packages/polaris-generation-core');
    const commands = /```sh\n(npm ci)\n(npm run poc:generator-demo -- --out [^\n]+)\n```/.exec(readme);
    if (commands?.[1] === undefined || commands[2] === undefined) throw new Error('README install onramp missing');
    const scratch = mkdtempSync(join(tmpdir(), 'syzygy-generator-onramp-'));
    cleanups.push(scratch);
    const checkout = join(scratch, 'checkout');
    const output = join(scratch, 'outputs');
    execFileSync('git', ['clone', '--quiet', '--local', '--no-hardlinks', process.cwd(), checkout], { timeout: 30_000 });
    const argv = commands[2].split(' ');
    expect(argv.slice(0, 5)).toEqual(['npm', 'run', 'poc:generator-demo', '--', '--out']);
    const documented = [argv[0]!, ...argv.slice(1, -1), output];
    try {
      execFileSync(documented[0]!, documented.slice(1), { cwd: checkout, timeout: 30_000, stdio: 'pipe' });
      throw new Error('missing install unexpectedly succeeded');
    } catch (error) {
      if (error instanceof Error && error.message === 'missing install unexpectedly succeeded') throw error;
      expect((error as { stderr?: Buffer }).stderr?.toString()).toContain('npm ci');
    }
    execFileSync('npm', commands[1].split(' ').slice(1), { cwd: checkout, timeout: 120_000, stdio: 'pipe' });
    execFileSync('npm', ['run', 'build:poc', '--silent'], { cwd: checkout, timeout: 120_000, stdio: 'pipe' });
    execFileSync(documented[0]!, documented.slice(1), { cwd: checkout, timeout: 120_000, stdio: 'pipe' });
    expect(readdirSync(output).sort()).toEqual(['archive.html', 'archive.json', 'garden-changed.html', 'garden-changed.json', 'garden.html', 'garden.json', 'report.json']);
  }, 180_000);

  it('repeats the complete SEC-2 operator boundary at every prompt-handling site', () => {
    const boundary = 'This kit grants no source access, provider egress, authorship adoption or release.';
    for (const file of ['docs/polaris-generation/README.md', 'docs/polaris-generation/AUTHORING.md', 'docs/polaris-generation/ARTIFACTS-AND-TOOLS.md']) {
      expect(readFileSync(join(process.cwd(), file), 'utf8'), file).toContain(boundary);
    }
  });
});
