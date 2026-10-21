// syzygy-bpyt.8.1 AC3: what the `syzygy` CLI reaches in one committed tree, over every import edge TypeScript's preprocessor
// reports (static, type-only, re-export, dynamic with a literal specifier); `@syzygy/*` resolves through each package's `exports`,
// `./dist/X.js` read as `src/X.ts`. Independent of island-boundary.test.ts, which computes the same closure in its own code.
// Usage: node reach_sweep.mjs <tree>   (prints JSON; the tree must be a clean git checkout, and its commit is recorded)
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { createRequire } from 'node:module';

const ROOT = path.resolve(process.argv[2]);
const git = (...args) => execFileSync('git', ['-C', ROOT, ...args], { encoding: 'utf8' }).trim();
const ts = createRequire(path.join(ROOT, 'package.json'))('typescript');
const ENTRY = 'apps/syzygy/src/main.ts';
const CORE_ROOT = 'packages/polaris-generation-core/src/index.ts';
const CONSENT_PORTS = 'packages/polaris-generation-consent/src/consent-ports.ts';
const ISLAND = [
  ...['admitted-input', 'discovery', 'discovery-provider', 'excerpt', 'pipeline', 'provider-draft', 'rendered-design']
    .map((m) => `packages/polaris-generation-core/src/${m}.ts`),
  ...['dossier-trigger', 'durable-lifecycle', 'generation-mutation', 'generation-mutation-run-main', 'pipeline-demo', 'pipeline-demo-main',
    'redis-shaped-fixture', 'redis-shaped-measure', 'redis-shaped-measure-main', 'repo-corpus', 'repo-corpus-main', 'self-corpus', 'self-corpus-main',
  ].map((m) => `apps/three-surface-poc/src/polaris-generation/${m}.ts`),
];

const isFile = (p) => fs.existsSync(path.join(ROOT, p)) && fs.statSync(path.join(ROOT, p)).isFile();
const packages = new Map();
for (const dir of ['packages', 'apps']) {
  for (const name of fs.readdirSync(path.join(ROOT, dir))) {
    const manifest = path.join(dir, name, 'package.json');
    if (isFile(manifest)) {
      const parsed = JSON.parse(fs.readFileSync(path.join(ROOT, manifest), 'utf8'));
      packages.set(parsed.name, { dir: `${dir}/${name}`, manifest: parsed });
    }
  }
}
function resolve(from, spec) {
  if (spec.startsWith('.')) {
    const base = path.posix.normalize(path.posix.join(path.posix.dirname(from), spec));
    return [base.replace(/\.js$/u, '.ts'), `${base}.ts`, `${base}/index.ts`].find(isFile) ?? { unresolved: spec };
  }
  const m = /^(@syzygy\/[^/]+)(\/.*)?$/u.exec(spec);
  if (!m) return null;
  const pkg = packages.get(m[1]);
  if (!pkg) return { unresolved: spec };
  const sub = m[2] ? `.${m[2]}` : '.';
  const exp = pkg.manifest.exports;
  let target = exp ? exp[sub] : (sub === '.' ? pkg.manifest.main : undefined);
  if (target && typeof target === 'object') target = target.import ?? target.default;
  if (typeof target !== 'string') return { unresolved: spec };
  const file = path.posix.join(pkg.dir, target.replace(/^\.\/dist\//u, 'src/').replace(/\.js$/u, '.ts'));
  return isFile(file) ? file : { unresolved: spec };
}

function closure(unfollowed) {
  const edges = new Map();
  const unresolved = [];
  const seen = new Set([ENTRY]);
  const queue = [ENTRY];
  while (queue.length) {
    const file = queue.shift();
    if (unfollowed.includes(file)) { edges.set(file, []); continue; }
    const out = [];
    for (const { fileName } of ts.preProcessFile(fs.readFileSync(path.join(ROOT, file), 'utf8'), true, true).importedFiles) {
      const r = resolve(file, fileName);
      if (r === null) continue;
      if (typeof r === 'object') { unresolved.push({ file, specifier: r.unresolved }); continue; }
      out.push({ specifier: fileName, to: r });
      if (!seen.has(r)) { seen.add(r); queue.push(r); }
    }
    edges.set(file, out);
  }
  const island = new Set(ISLAND);
  const reachable = [...seen].sort();
  const edgesIntoIsland = [];
  const coreRootImporters = [];
  for (const [file, out] of edges) {
    for (const e of out) {
      if (!island.has(file) && island.has(e.to)) edgesIntoIsland.push({ from: file, specifier: e.specifier, to: e.to });
      if (e.to === CORE_ROOT && !coreRootImporters.includes(file)) coreRootImporters.push(file);
    }
  }
  return {
    unfollowed, reachableCount: reachable.length, reachable,
    reachableIsland: reachable.filter((f) => island.has(f)),
    coreRootImporters: coreRootImporters.sort(),
    edgesIntoIsland, unresolved,
  };
}

const clean = git('status', '--porcelain', '--untracked-files=no') === '';
const self = fs.readFileSync(new URL(import.meta.url), 'utf8');
console.log(JSON.stringify({
  format: 'syzygy-bpyt-8-1-reach/1',
  commit: git('rev-parse', 'HEAD'), trackedTreeClean: clean,
  sweepSha256: createHash('sha256').update(self, 'utf8').digest('hex'),
  entry: ENTRY, island: ISLAND, islandCount: ISLAND.length,
  everyEdge: closure([]),
  consentPortsUnfollowed: closure([CONSENT_PORTS]),
}, null, 2));
