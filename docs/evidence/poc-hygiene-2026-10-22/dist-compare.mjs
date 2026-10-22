// Compare the emitted JavaScript of two built trees module by module, once
// comments and `export` are removed. Usage:
//   node dist-compare.mjs <base-tree> <head-tree> <out.json>
// Both trees need a built apps/three-surface-poc/dist. For every .js file under
// that dist in either tree (test files excluded) the file is parsed with the TypeScript compiler API
// (from the head tree's node_modules), `export` modifiers and local
// `export { ... }` lists are dropped, and the result is printed without
// comments. A file is `byte-identical` when the raw bytes match, `identical
// after normalisation` when only the normalised print matches, otherwise
// `differs`; a file present in one tree only is listed as added or removed.
// The record-reading modules are the head files whose emitted JS imports
// node:fs, node:fs/promises or node:child_process (any module that can read a
// governed record or observed text from disk or from git).
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
import { readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs';
import * as path from 'node:path';

const [base, head, out] = process.argv.slice(2).map((p) => path.resolve(p));
const ts = createRequire(path.join(head, 'package.json'))('typescript');
const DIST = 'apps/three-surface-poc/dist';

function walk(root) {
  const files = [];
  const visit = (dir) => {
    for (const name of readdirSync(dir)) {
      const full = path.join(dir, name);
      if (statSync(full).isDirectory()) visit(full);
      else if (name.endsWith('.js') && !name.endsWith('.test.js')) files.push(path.relative(root, full));
    }
  };
  visit(root);
  return files.sort();
}

function normalise(text, name) {
  const source = ts.createSourceFile(name, text, ts.ScriptTarget.Latest, true, ts.ScriptKind.JS);
  const transformer = (context) => (root) => {
    const visit = (node) => {
      if (ts.isExportDeclaration(node) && node.moduleSpecifier === undefined) return undefined;
      if (ts.canHaveModifiers(node)) {
        const modifiers = ts.getModifiers(node);
        if (modifiers?.some((m) => m.kind === ts.SyntaxKind.ExportKeyword)) {
          const kept = modifiers.filter((m) => m.kind !== ts.SyntaxKind.ExportKeyword);
          if (ts.isFunctionDeclaration(node)) return ts.factory.updateFunctionDeclaration(node, kept, node.asteriskToken, node.name, node.typeParameters, node.parameters, node.type, node.body);
          if (ts.isVariableStatement(node)) return ts.factory.updateVariableStatement(node, kept, node.declarationList);
          if (ts.isClassDeclaration(node)) return ts.factory.updateClassDeclaration(node, kept, node.name, node.typeParameters, node.heritageClauses, node.members);
          throw new Error(`unhandled exported node ${ts.SyntaxKind[node.kind]} in ${name}`);
        }
      }
      return ts.visitEachChild(node, visit, context);
    };
    return ts.visitNode(root, visit);
  };
  const result = ts.transform(source, [transformer]);
  const printer = ts.createPrinter({ removeComments: true, newLine: ts.NewLineKind.LineFeed });
  const printed = printer.printFile(result.transformed[0]);
  result.dispose();
  return printed;
}

const baseRoot = path.join(base, DIST);
const headRoot = path.join(head, DIST);
const baseFiles = new Set(walk(baseRoot));
const headFiles = new Set(walk(headRoot));
const common = [...headFiles].filter((f) => baseFiles.has(f));
const rows = [];
for (const file of common) {
  const b = readFileSync(path.join(baseRoot, file), 'utf8');
  const h = readFileSync(path.join(headRoot, file), 'utf8');
  const status = b === h ? 'byte-identical' : normalise(b, file) === normalise(h, file) ? 'identical after normalisation' : 'differs';
  const readsFiles = /from ['"]node:(?:fs|fs\/promises|child_process)['"]/.test(h);
  rows.push({ file, status, recordReading: readsFiles });
}
const tally = (list) => Object.fromEntries(['byte-identical', 'identical after normalisation', 'differs'].map((s) => [s, list.filter((r) => r.status === s).length]));
const record = {
  tool: 'dist-compare.mjs',
  toolSha256: createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex'),
  trees: { base, head },
  typescriptVersion: ts.version,
  population: `non-test .js files under ${DIST} in both trees (a stale file left in a dist that was not cleaned would show as present; build each tree from a clean dist)`,
  commonFiles: common.length,
  addedInHead: [...headFiles].filter((f) => !baseFiles.has(f)),
  removedInHead: [...baseFiles].filter((f) => !headFiles.has(f)),
  tally: tally(rows),
  differing: rows.filter((r) => r.status === 'differs').map((r) => r.file),
  recordReadingModules: {
    predicate: "emitted JS imports node:fs, node:fs/promises or node:child_process (regex /from ['\"]node:(?:fs|fs\\/promises|child_process)['\"]/)",
    count: rows.filter((r) => r.recordReading).length,
    tally: tally(rows.filter((r) => r.recordReading)),
    differing: rows.filter((r) => r.recordReading && r.status === 'differs').map((r) => r.file),
    files: rows.filter((r) => r.recordReading).map((r) => r.file),
  },
};
writeFileSync(out, JSON.stringify(record, null, 1) + '\n');
console.log(`common=${record.commonFiles} ${JSON.stringify(record.tally)} added=${record.addedInHead.length} removed=${record.removedInHead.length} recordReading=${record.recordReadingModules.count} ${JSON.stringify(record.recordReadingModules.tally)}`);
console.log('differs:', record.differing.join(', ') || '-');
