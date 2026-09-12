import { describe, expect, it } from 'vitest';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';

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
});
