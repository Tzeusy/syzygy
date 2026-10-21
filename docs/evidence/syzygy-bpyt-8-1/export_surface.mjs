// syzygy-bpyt.8.1 (class 6): the export names of each entry the change touches, before and after, by TypeScript's checker. The
// consent census: package-reader.ts's names from './consent-ports.js' must be a subset of consent-ports.ts's exports in each tree,
// and the consent barrel must export the same names in both (the consent package is left untouched; syzygy-bpyt.8.19).
// Usage: node export_surface.mjs <old tree> <new tree>   (prints JSON)
import { execFileSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { createRequire } from 'node:module';

const ENTRIES = [
  'packages/polaris-generation-core/src/index.ts', 'packages/polaris-generation-core/src/live.ts',
  'apps/three-surface-poc/src/polaris-generation/dossier-render.ts', 'apps/three-surface-poc/src/polaris-generation/dossier-site.ts',
  'packages/polaris-generation-consent/src/consent-ports.ts', 'packages/polaris-generation-consent/src/index.ts',
];
const MANIFESTS = ['packages/polaris-generation-core/package.json', 'apps/three-surface-poc/package.json', 'packages/polaris-generation-consent/package.json'];
const READER = 'packages/polaris-generation-consent/src/package-reader.ts', PORTS = 'packages/polaris-generation-consent/src/consent-ports.ts';
/** The names one file imports from one relative specifier, by its syntax tree. */
function importedNames(ts, tree, file, specifier) {
  const source = ts.createSourceFile(file, fs.readFileSync(path.join(tree, file), 'utf8'), ts.ScriptTarget.ES2022, true);
  return source.statements.filter((s) => ts.isImportDeclaration(s) && s.moduleSpecifier.text === specifier)
    .flatMap((s) => s.importClause?.namedBindings?.elements?.map((e) => (e.propertyName ?? e.name).text) ?? []).sort();
}
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
    readerImportsFromPorts: importedNames(ts, tree, READER, './consent-ports.js'),
  };
}
const [before, after] = process.argv.slice(2).map((tree) => surface(path.resolve(tree)));
const delta = Object.fromEntries(ENTRIES.map((f) => {
  const a = new Set(before.modules[f] ?? []), b = new Set(after.modules[f] ?? []);
  return [f, { before: before.modules[f]?.length ?? null, after: after.modules[f]?.length ?? null, added: [...b].filter((n) => !a.has(n)), removed: [...a].filter((n) => !b.has(n)) }];
}));
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const consentCensus = Object.fromEntries([['before', before], ['after', after]].map(([side, s]) => [side, {
  commit: s.commit, readerImportsFromPorts: s.readerImportsFromPorts,
  missingFromPorts: s.readerImportsFromPorts.filter((n) => !s.modules[PORTS].includes(n)),
}]));
consentCensus.barrelExportsUnchanged = same(before.modules['packages/polaris-generation-consent/src/index.ts'], after.modules['packages/polaris-generation-consent/src/index.ts']);
consentCensus.portsExportsUnchanged = same(before.modules[PORTS], after.modules[PORTS]);
consentCensus.packageExportsUnchanged = same(before.packageExports['packages/polaris-generation-consent/package.json'], after.packageExports['packages/polaris-generation-consent/package.json']);
console.log(JSON.stringify({ format: 'syzygy-bpyt-8-1-export-surface/2', before, after, delta, consentCensus }, null, 2));
