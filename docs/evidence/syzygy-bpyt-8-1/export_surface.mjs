// syzygy-bpyt.8.1 (class 6): the export names of each entry the change touches, before and after, by TypeScript's checker.
// Usage: node export_surface.mjs <old tree> <new tree>   (prints JSON)
import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { createRequire } from 'node:module';

const ENTRIES = [
  'packages/polaris-generation-core/src/index.ts', 'packages/polaris-generation-core/src/live.ts',
  'apps/three-surface-poc/src/polaris-generation/dossier-render.ts', 'apps/three-surface-poc/src/polaris-generation/dossier-site.ts',
];
const MANIFESTS = ['packages/polaris-generation-core/package.json', 'apps/three-surface-poc/package.json'];
function surface(tree) {
  const ts = createRequire(path.join(tree, 'package.json'))('typescript');
  const present = ENTRIES.filter((f) => fs.existsSync(path.join(tree, f)));
  const program = ts.createProgram(present.map((f) => path.join(tree, f)), { module: ts.ModuleKind.NodeNext, moduleResolution: ts.ModuleResolutionKind.NodeNext,
    target: ts.ScriptTarget.ES2022, noEmit: true, skipLibCheck: true });
  const checker = program.getTypeChecker();
  return {
    commit: execFileSync('git', ['-C', tree, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim(),
    modules: Object.fromEntries(present.map((f) => [f, checker.getExportsOfModule(checker.getSymbolAtLocation(program.getSourceFile(path.join(tree, f)))).map((s) => s.name).sort()])),
    packageExports: Object.fromEntries(MANIFESTS.map((m) => [m, JSON.parse(fs.readFileSync(path.join(tree, m), 'utf8')).exports])),
  };
}
const [before, after] = process.argv.slice(2).map((tree) => surface(path.resolve(tree)));
const delta = Object.fromEntries(ENTRIES.map((f) => {
  const a = new Set(before.modules[f] ?? []), b = new Set(after.modules[f] ?? []);
  return [f, { before: before.modules[f]?.length ?? null, after: after.modules[f]?.length ?? null, added: [...b].filter((n) => !a.has(n)), removed: [...a].filter((n) => !b.has(n)) }];
}));
console.log(JSON.stringify({ format: 'syzygy-bpyt-8-1-export-surface/1', before, after, delta }, null, 2));
