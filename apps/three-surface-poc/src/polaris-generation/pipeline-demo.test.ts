import { mkdtempSync, readdirSync, readFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';
import { writeSyntheticPipelineDemo } from './pipeline-demo-main.js';

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

  it('reads the documented clean-install onramp and requires exactly seven synthetic output files', async () => {
    const readme = readFileSync(join(process.cwd(), 'packages/polaris-generation-core/README.md'), 'utf8');
    const command = readme.match(/npm ci\n(npm run poc:generator-demo -- --out [^\n]+)/)?.[1];
    expect(command).toBe('npm run poc:generator-demo -- --out /tmp/polaris-generator-demo-new');
    const output = mkdtempSync(join(process.cwd(), '.tmp-generator-onramp-'));
    cleanups.push(output);
    await writeSyntheticPipelineDemo(output);
    expect(readdirSync(output).sort()).toEqual(['archive.html', 'archive.json', 'garden-changed.html', 'garden-changed.json', 'garden.html', 'garden.json', 'report.json']);
  });

  it('repeats the complete SEC-2 operator boundary at every prompt-handling site', () => {
    const boundary = 'This kit grants no source access, provider egress, authorship adoption or release.';
    for (const file of ['docs/polaris-generation/README.md', 'docs/polaris-generation/AUTHORING.md', 'docs/polaris-generation/ARTIFACTS-AND-TOOLS.md']) {
      expect(readFileSync(join(process.cwd(), file), 'utf8'), file).toContain(boundary);
    }
  });
});
