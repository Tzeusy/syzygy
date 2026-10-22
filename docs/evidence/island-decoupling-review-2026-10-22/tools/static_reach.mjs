// Independent static reachability sweep (rev-510). Usage: node static_reach.mjs <repo root> <out.json> [unfollowed path ...]
// Walks the TypeScript AST of every reached src .ts file from apps/syzygy/src/main.ts, resolves every module specifier with
// TypeScript's own NodeNext resolver (package exports, conditions, .js->.ts), maps workspace dist/*.d.ts|.js back to src/*.ts,
// and records: static, type-only, re-export, import-equals, dynamic import() (literal and non-literal), import types,
// require() calls, and process/worker spawns for manual review.
import { createRequire } from 'node:module';
import * as fs from 'node:fs';
import * as path from 'node:path';

const [root, out, ...unfollowedArg] = process.argv.slice(2);
const ROOT = fs.realpathSync(root);
const require = createRequire(path.join(ROOT, 'package.json'));
const ts = require('typescript');

const ENTRY = process.env.ENTRY ?? "apps/syzygy/src/main.ts";
const ISLAND = new Set([
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
]);
const unfollowed = new Set(unfollowedArg);
const options = { module: ts.ModuleKind.NodeNext, moduleResolution: ts.ModuleResolutionKind.NodeNext, allowJs: false };
const host = ts.sys;
const rel = (abs) => path.relative(ROOT, abs).split(path.sep).join('/');

function toSource(resolved) {
  const real = fs.realpathSync(resolved);
  const r = rel(real);
  if (r.startsWith('..') || r.includes('node_modules/')) return { external: r };
  let m = /^(.*)\/dist\/(.*)\.d\.ts$/u.exec(r) ?? /^(.*)\/dist\/(.*)\.js$/u.exec(r);
  if (m) {
    const src = `${m[1]}/src/${m[2]}.ts`;
    return fs.existsSync(path.join(ROOT, src)) ? { module: src } : { unmapped: r };
  }
  if (r.endsWith('.ts') && !r.endsWith('.d.ts')) return { module: r };
  return { unmapped: r };
}

function resolve(fromRel, specifier) {
  if (specifier.startsWith('node:')) return { builtin: specifier };
  const res = ts.resolveModuleName(specifier, path.join(ROOT, fromRel), options, host, undefined, undefined, ts.ModuleKind.ESNext);
  const file = res.resolvedModule?.resolvedFileName;
  if (file === undefined) {
    // Bare Node builtins without the node: prefix resolve to nothing in TS without @types lookups.
    try { if (require('node:module').isBuiltin(specifier)) return { builtin: specifier }; } catch {}
    return { unresolved: true };
  }
  return toSource(file);
}

function edgesOf(fileRel) {
  const text = fs.readFileSync(path.join(ROOT, fileRel), 'utf8');
  const sf = ts.createSourceFile(fileRel, text, ts.ScriptTarget.Latest, true, ts.ScriptKind.TS);
  const edges = [];
  const notes = [];
  const lit = (n) => n && (ts.isStringLiteral(n) || ts.isNoSubstitutionTemplateLiteral(n)) ? n.text : null;
  const line = (n) => sf.getLineAndCharacterOfPosition(n.getStart(sf)).line + 1;
  function visit(n) {
    if (ts.isImportDeclaration(n)) {
      const typeOnly = !!n.importClause?.isTypeOnly || (n.importClause && !n.importClause.name && n.importClause.namedBindings && ts.isNamedImports(n.importClause.namedBindings) && n.importClause.namedBindings.elements.length > 0 && n.importClause.namedBindings.elements.every(e => e.isTypeOnly));
      edges.push({ kind: typeOnly ? 'import-type' : 'import', specifier: lit(n.moduleSpecifier), line: line(n) });
    } else if (ts.isExportDeclaration(n) && n.moduleSpecifier) {
      const typeOnly = n.isTypeOnly || (n.exportClause && ts.isNamedExports(n.exportClause) && n.exportClause.elements.length > 0 && n.exportClause.elements.every(e => e.isTypeOnly));
      edges.push({ kind: typeOnly ? 're-export-type' : (n.exportClause ? 're-export' : 'export-star'), specifier: lit(n.moduleSpecifier), line: line(n) });
    } else if (ts.isImportEqualsDeclaration(n) && ts.isExternalModuleReference(n.moduleReference)) {
      edges.push({ kind: 'import-equals', specifier: lit(n.moduleReference.expression), line: line(n) });
    } else if (ts.isImportTypeNode(n)) {
      const arg = n.argument && ts.isLiteralTypeNode(n.argument) ? lit(n.argument.literal) : null;
      edges.push({ kind: 'import-type-node', specifier: arg, line: line(n) });
    } else if (ts.isCallExpression(n)) {
      if (n.expression.kind === ts.SyntaxKind.ImportKeyword) {
        const s = lit(n.arguments[0]);
        if (s === null) notes.push({ kind: 'dynamic-import-non-literal', line: line(n), text: n.getText(sf).slice(0, 160) });
        else edges.push({ kind: 'dynamic-import', specifier: s, line: line(n) });
      } else if (ts.isIdentifier(n.expression) && n.expression.text === 'require') {
        const s = lit(n.arguments[0]);
        notes.push({ kind: 'require-call', line: line(n), text: n.getText(sf).slice(0, 160) });
        if (s !== null) edges.push({ kind: 'require', specifier: s, line: line(n) });
      } else {
        const callee = n.expression.getText(sf);
        if (/(^|\.)(fork|spawn|spawnSync|execFile|execFileSync|exec|execSync)$/u.test(callee)) notes.push({ kind: 'process-spawn', line: line(n), text: n.getText(sf).slice(0, 200) });
      }
    } else if (ts.isNewExpression(n) && /Worker$/u.test(n.expression.getText(sf))) {
      notes.push({ kind: 'worker', line: line(n), text: n.getText(sf).slice(0, 200) });
    } else if (ts.isPropertyAccessExpression(n) && n.getText(sf) === 'import.meta.resolve') {
      notes.push({ kind: 'import-meta-resolve', line: line(n), text: n.parent.getText(sf).slice(0, 160) });
    }
    ts.forEachChild(n, visit);
  }
  visit(sf);
  return { edges, notes };
}

const seen = new Set([ENTRY]);
const queue = [ENTRY];
const allEdges = [];
const notes = [];
const problems = [];
while (queue.length > 0) {
  const file = queue.shift();
  if (unfollowed.has(file)) continue;
  const { edges, notes: n } = edgesOf(file);
  for (const note of n) notes.push({ file, ...note });
  for (const e of edges) {
    if (e.specifier === null) { problems.push({ file, ...e, problem: 'non-literal specifier' }); continue; }
    const r = resolve(file, e.specifier);
    const rec = { from: file, ...e, ...r };
    allEdges.push(rec);
    if (r.unresolved || r.unmapped) problems.push({ ...rec, problem: r.unresolved ? 'unresolved' : 'unmapped' });
    if (r.module && !seen.has(r.module)) { seen.add(r.module); queue.push(r.module); }
  }
}
const reached = [...seen].sort();
const islandReached = reached.filter(m => ISLAND.has(m));
const intoIsland = allEdges.filter(e => e.module && ISLAND.has(e.module) && !ISLAND.has(e.from));
const rootImporters = allEdges.filter(e => e.module === 'packages/polaris-generation-core/src/index.ts').map(e => `${e.from}:${e.line} ${e.kind} ${e.specifier}`);
const summary = { root: ROOT, unfollowed: [...unfollowed], reached: reached.length, edges: allEdges.length, islandReached, intoIsland: intoIsland.map(e => `${e.from}:${e.line} ${e.kind} ${e.specifier} -> ${e.module}`), rootImporters, problems, notes };
fs.writeFileSync(out, JSON.stringify({ summary, reachedModules: reached, edges: allEdges }, null, 2));
console.log(JSON.stringify({ reached: reached.length, edges: allEdges.length, islandReached: islandReached.length, intoIsland: intoIsland.length, rootImporters: rootImporters.length, problems: problems.length, notes: notes.length }));
