import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import type { ProviderDraft } from '@syzygy/polaris-generation-core';
import { renderDraftPreview } from './draft-preview.js';
import { runSyntheticProject, syntheticProjects } from './pipeline-demo.js';

export async function writeSyntheticPipelineDemo(destination: string): Promise<void> {
  await mkdir(destination, { recursive: true });
  const reports: unknown[] = [];
  const first = syntheticProjects[0]!;
  const cases = [...syntheticProjects, { ...first, id: `${first.id}-changed`, qualification: `${first.qualification} Outdoor care also depends on the season.` }];
  for (const project of cases) {
    const run = await runSyntheticProject(project);
    if (run.result.status !== 'awaiting-rendered-review') throw new Error(`Synthetic pipeline stopped: ${run.result.reason}`);
    const html = renderDraftPreview(run.result.draft as ProviderDraft, run.sources);
    await writeFile(resolve(destination, `${project.id}.html`), html, { flag: 'wx' });
    await writeFile(resolve(destination, `${project.id}.json`), JSON.stringify({ synthetic: true, ...run }, null, 2) + '\n', { flag: 'wx' });
    reports.push({ project: project.id, status: run.result.status, receipts: run.result.receipts });
  }
  await writeFile(resolve(destination, 'report.json'), JSON.stringify({
    kind: 'synthetic-pipeline-exercise', realProvider: false, realProjectProof: false,
    limitations: 'Scripted responses exercise concrete contracts, orchestration and rendering; no model judgment or production effect admission is claimed.',
    runs: reports,
  }, null, 2) + '\n', { flag: 'wx' });
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const args = process.argv.slice(2);
  if (args.length !== 2 || args[0] !== '--out' || !args[1]) {
    process.stderr.write('Usage: pipeline-demo-main --out <new-output-directory>\n');
    process.exitCode = 2;
  } else {
    writeSyntheticPipelineDemo(resolve(args[1])).then(
      () => process.stdout.write('Created three synthetic pipeline previews and their stage records. No real provider or project was used.\n'),
      () => { process.stderr.write('Synthetic pipeline demo failed; inspect tests and use a fresh output directory.\n'); process.exitCode = 1; },
    );
  }
}
