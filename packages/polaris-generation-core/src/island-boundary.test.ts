import ts from 'typescript';
import { describe, expect, it } from 'vitest';
import { isFile, reach as reachBy, readModule, type ReachEdge } from './workspace-reach.testkit.js';

// syzygy-bpyt.8.1: the `syzygy` CLI never loads the parked provider island
// (parked, not deleted: owner packet Q8). Reachability is computed here, from
// the CLI entry, over every import edge TypeScript's preprocessor reports:
// static, type-only, re-export and dynamic with a literal specifier. An
// `@syzygy/*` specifier resolves through its package's `exports`, where
// `./dist/X.js` is `src/X.ts` (workspace-reach.testkit.ts, which the dossier's
// daemon-path guard shares since syzygy-bpyt.8.34). Nothing lists the
// reachable modules by hand; only the island is listed.

const ENTRY = 'apps/syzygy/src/main.ts';
const ISLAND = [
  'packages/polaris-generation-core/src/admitted-input.ts',
  'packages/polaris-generation-core/src/discovery-provider.ts',
  'packages/polaris-generation-core/src/discovery.ts',
  'packages/polaris-generation-core/src/excerpt.ts',
  'packages/polaris-generation-core/src/pipeline.ts',
  'packages/polaris-generation-core/src/provider-draft.ts',
  'packages/polaris-generation-core/src/rendered-design.ts',
  'apps/three-surface-poc/src/polaris-generation/dossier-trigger.ts',
  'apps/three-surface-poc/src/polaris-generation/durable-lifecycle.ts',
  'apps/three-surface-poc/src/polaris-generation/generation-mutation-run-main.ts',
  'apps/three-surface-poc/src/polaris-generation/generation-mutation.ts',
  'apps/three-surface-poc/src/polaris-generation/pipeline-demo-main.ts',
  'apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts',
  'apps/three-surface-poc/src/polaris-generation/redis-shaped-fixture.ts',
  'apps/three-surface-poc/src/polaris-generation/redis-shaped-measure-main.ts',
  'apps/three-surface-poc/src/polaris-generation/redis-shaped-measure.ts',
  'apps/three-surface-poc/src/polaris-generation/repo-corpus-main.ts',
  'apps/three-surface-poc/src/polaris-generation/repo-corpus.ts',
  'apps/three-surface-poc/src/polaris-generation/self-corpus-main.ts',
  'apps/three-surface-poc/src/polaris-generation/self-corpus.ts',
];
/** Every module `entry` reaches, the edges from them into the island, and any workspace specifier that names no module. */
function reach(entry: string): { reachable: string[]; intoIsland: ReachEdge[]; unresolved: Omit<ReachEdge, 'to'>[] } {
  const island = new Set(ISLAND);
  const { reachable, edges, unresolved } = reachBy(entry, (file) => ts.preProcessFile(readModule(file), true, true).importedFiles.map((imported) => imported.fileName));
  return { reachable, intoIsland: edges.filter((edge) => island.has(edge.to) && !island.has(edge.from)), unresolved };
}

describe('the syzygy CLI and the parked provider island', () => {
  it('lists twenty island modules, each a file in the tree', () => {
    expect(new Set(ISLAND).size).toBe(20);
    expect(ISLAND.filter(path => !isFile(path))).toEqual([]);
  });

  it('resolves every workspace import the CLI reaches, dynamic ones included', () => {
    const { reachable, unresolved } = reach(ENTRY);
    expect(unresolved.map(edge => `${edge.from} imports ${edge.specifier}`)).toEqual([]);
    expect(reachable).toContain('apps/three-surface-poc/src/polaris-generation/dossier-site.ts');
    expect(reachable).toContain('packages/polaris-generation-consent/src/in-force.ts');
  });

  it('reaches no island module from the CLI entry', () => {
    const { reachable, intoIsland } = reach(ENTRY);
    expect(intoIsland.map(edge => `${edge.from} imports ${edge.specifier} (${edge.to})`)).toEqual([]);
    expect(reachable.filter(path => ISLAND.includes(path))).toEqual([]);
  });

  // The consent package root re-exports consent-ports.ts, parked egress code
  // that imports this package's root, so a module the CLI reaches takes
  // consent names from `@syzygy/polaris-generation-consent/live`
  // (syzygy-bpyt.8.19). The same walk from that root finds the island, which
  // also shows the walk sees an edge into it.
  it('reaches the island from the consent package root, which the CLI does not import', () => {
    expect(reach('packages/polaris-generation-consent/src/index.ts').intoIsland.length).toBeGreaterThan(0);
  });
});
