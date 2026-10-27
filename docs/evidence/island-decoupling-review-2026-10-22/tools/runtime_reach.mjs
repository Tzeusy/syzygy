// Runtime reachability (rev-510): load the compiled modules the CLI entry imports (static and both dynamic branches) under a
// load hook that records every file Node actually loads. Usage: node runtime_reach.mjs <repo root> <renderer dist path> [stub]
// With `stub`, the compiled consent-ports.js is replaced by a module exporting its five value names as undefined, which is the
// runtime analogue of "consent-ports.ts not followed".
import { registerHooks } from 'node:module';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';

const [root, renderer, stub] = process.argv.slice(2);
const ROOT = fs.realpathSync(root);
const loaded = new Set();
registerHooks({
  load(url, context, nextLoad) {
    if (url.startsWith('file:')) loaded.add(path.relative(ROOT, fs.realpathSync(fileURLToPath(url))).split(path.sep).join('/'));
    if (stub === 'stub' && url.endsWith('/packages/polaris-generation-consent/dist/consent-ports.js')) {
      return { format: 'module', shortCircuit: true,
        source: ['UNCONSENTED', 'inForceRecords', 'notInForceRecords', 'createConsentPorts', 'withConsent'].map(n => `export const ${n} = undefined;`).join('\n') };
    }
    return nextLoad(url, context);
  },
});
const ISLAND_DIST = [
  'packages/polaris-generation-core/dist/admitted-input.js', 'packages/polaris-generation-core/dist/discovery-provider.js',
  'packages/polaris-generation-core/dist/discovery.js', 'packages/polaris-generation-core/dist/excerpt.js',
  'packages/polaris-generation-core/dist/pipeline.js', 'packages/polaris-generation-core/dist/provider-draft.js',
  'packages/polaris-generation-core/dist/rendered-design.js',
  ...['dossier-trigger', 'durable-lifecycle', 'generation-mutation-run-main', 'generation-mutation', 'pipeline-demo-main', 'pipeline-demo',
    'redis-shaped-fixture', 'redis-shaped-measure-main', 'redis-shaped-measure', 'repo-corpus-main', 'repo-corpus', 'self-corpus-main', 'self-corpus']
    .map(n => `apps/three-surface-poc/dist/polaris-generation/${n}.js`),
];
for (const entry of ['packages/cap1-daemon/dist/index.js', 'packages/polaris-dossier/dist/index.js', renderer]) {
  await import(pathToFileURL(path.join(ROOT, entry)).href);
}
const inRepo = [...loaded].filter(p => !p.startsWith('..') && !p.includes('node_modules/')).sort();
const island = inRepo.filter(p => ISLAND_DIST.includes(p));
const extra = ['packages/polaris-generation-core/dist/index.js', 'packages/polaris-generation-core/dist/live.js', 'packages/polaris-generation-core/dist/prompts.js',
  'apps/three-surface-poc/dist/polaris-generation/dossier-render.js', 'apps/three-surface-poc/dist/polaris-generation/dossier-site.js',
  'packages/polaris-generation-consent/dist/consent-ports.js'];
console.log(JSON.stringify({ renderer, stub: stub === 'stub', loadedInRepo: inRepo.length, islandLoaded: island, watched: Object.fromEntries(extra.map(p => [p, inRepo.includes(p)])) }, null, 1));
