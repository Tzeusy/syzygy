import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';

// syzygy-bpyt.8.2: the daemon entry statically imports two of this package's modules by subpath, `/argv` and `/state-directory`,
// and the barrel only inside its `dossier` and `polaris` branches. Each subpath module imports exactly the node: built-ins listed
// below, so the daemon path can reach neither this package's barrel, another @syzygy package nor a third-party module through them,
// and no built-in that loads code (node:module) slips in. Every import edge counts, wherever it stands: static, type-only, re-export,
// `import =`, `require`, a type-position `import()` and dynamic with a literal specifier (syzygy-bpyt.8.32, the review of 8.2, N2).
// syzygy-bpyt.8.5 (one leaf util) may move both modules; this guard moves with them.

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PACKAGE = 'packages/polaris-dossier';
const ENTRY = 'apps/syzygy/src/main.ts';

interface Edge {
  readonly specifier: string;
  /** `<form> '<specifier>' <where>`, where is the nearest enclosing `if` branch, or outside any if. */
  readonly edge: string;
}

/** Every import edge of `text`, found twice: by TypeScript's preprocessor and by a walk of the syntax tree. It throws unless the two
 * agree, so a form one of them misses (the preprocessor misses `export * as ns from`) fails the check instead of passing unseen. */
function edgesOf(text: string): Edge[] {
  const source = ts.createSourceFile('module.ts', text, ts.ScriptTarget.Latest, true);
  const edges: Edge[] = [];
  const where = (node: ts.Node): string => {
    for (let child = node, parent = node.parent; parent !== undefined; child = parent, parent = parent.parent) {
      if (ts.isIfStatement(parent) && child === parent.thenStatement) return `inside if (${parent.expression.getText(source)})`;
      if (ts.isIfStatement(parent) && child === parent.elseStatement) return `inside the else of if (${parent.expression.getText(source)})`;
    }
    return 'outside any if';
  };
  const add = (form: string, literal: ts.Node): void => {
    if (ts.isStringLiteralLike(literal)) edges.push({ specifier: literal.text, edge: `${form} '${literal.text}' ${where(literal)}` });
  };
  const visit = (node: ts.Node): void => {
    if (ts.isImportDeclaration(node)) add(node.importClause?.isTypeOnly ? 'import type' : 'import', node.moduleSpecifier);
    else if (ts.isExportDeclaration(node) && node.moduleSpecifier !== undefined) add('export from', node.moduleSpecifier);
    else if (ts.isImportEqualsDeclaration(node) && ts.isExternalModuleReference(node.moduleReference)) add('import =', node.moduleReference.expression);
    else if (ts.isCallExpression(node) && node.expression.kind === ts.SyntaxKind.ImportKeyword && node.arguments[0]) add('dynamic import', node.arguments[0]);
    else if (ts.isCallExpression(node) && ts.isIdentifier(node.expression) && node.expression.text === 'require' && node.arguments[0]) add('require', node.arguments[0]);
    else if (ts.isImportTypeNode(node) && ts.isLiteralTypeNode(node.argument)) add('type-position import', node.argument.literal);
    ts.forEachChild(node, visit);
  };
  visit(source);
  const walked = edges.map((edge) => edge.specifier).sort();
  const reported = ts.preProcessFile(text, true, true).importedFiles.map((file) => file.fileName).sort();
  if (JSON.stringify(walked) !== JSON.stringify(reported)) throw new Error(`the preprocessor and the syntax walk disagree: ${JSON.stringify({ walked, reported })}`);
  return edges;
}
const importsOf = (text: string): string[] => edgesOf(text).map((edge) => edge.specifier);
/** The edges of `text` into this package, by its name or by a relative path. */
const entryEdgesOf = (text: string): string[] => edgesOf(text).filter((edge) => edge.specifier.includes('polaris-dossier')).map((edge) => edge.edge);

/** The source module a subpath export names: `./dist/X.js` is `src/X.ts`. */
function moduleOf(subpath: string): string {
  const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, PACKAGE, 'package.json'), 'utf8')) as { exports: Record<string, { import: string }> };
  const target = manifest.exports[subpath]?.import ?? '';
  return path.posix.join(PACKAGE, target.replace(/^\.\/dist\//u, 'src/').replace(/\.js$/u, '.ts'));
}

describe('the subpaths the daemon entry imports', () => {
  it('are /argv and /state-directory, imported statically, and the barrel only dynamically inside the dossier and polaris branches', () => {
    expect(entryEdgesOf(fs.readFileSync(path.join(ROOT, ENTRY), 'utf8'))).toEqual([
      "import '@syzygy/polaris-dossier/argv' outside any if",
      "import '@syzygy/polaris-dossier/state-directory' outside any if",
      "dynamic import '@syzygy/polaris-dossier' inside if (argv[0] === 'dossier')",
      "dynamic import '@syzygy/polaris-dossier' inside if (argv[0] === 'polaris')",
    ]);
  });

  it.each([
    ['./argv', 'packages/polaris-dossier/src/argv.ts', ['node:util']],
    ['./state-directory', 'packages/polaris-dossier/src/state-directory.ts', ['node:crypto', 'node:fs', 'node:path']],
  ])('%s is %s, which imports exactly %j', (subpath, module, imports) => {
    expect(moduleOf(subpath)).toBe(module);
    expect(importsOf(fs.readFileSync(path.join(ROOT, module), 'utf8'))).toEqual(imports);
  });

  it.each([
    ["import { DOSSIER_USAGE } from './cli.js';", './cli.js'],
    ["import type { CliPorts } from './index.js';", './index.js'],
    ["export * from '@syzygy/cap1-core';", '@syzygy/cap1-core'],
    ["const lazy = await import('typescript');", 'typescript'],
    ["const fs = require('fs');", 'fs'],
    ["import { createRequire } from 'node:module';", 'node:module'],
  ])('the check sees the import in %s (its own mutant)', (line, specifier) => {
    expect(importsOf(`import * as path from 'node:path';\n${line}\n`)).toEqual(['node:path', specifier]);
  });

  it.each([
    ["export { runDossierCli } from '@syzygy/polaris-dossier';", "export from '@syzygy/polaris-dossier' outside any if"],
    ["import type { CliPorts } from '@syzygy/polaris-dossier';", "import type '@syzygy/polaris-dossier' outside any if"],
    ["const lazy = await import('@syzygy/polaris-dossier');", "dynamic import '@syzygy/polaris-dossier' outside any if"],
    ["type Barrel = typeof import('@syzygy/polaris-dossier');", "type-position import '@syzygy/polaris-dossier' outside any if"],
    ["if (argv[0] !== 'dossier') require('@syzygy/polaris-dossier');", "require '@syzygy/polaris-dossier' inside if (argv[0] !== 'dossier')"],
    ["if (argv[0] === 'dossier') {} else await import('@syzygy/polaris-dossier');", "dynamic import '@syzygy/polaris-dossier' inside the else of if (argv[0] === 'dossier')"],
    ["import cli = require('../../../packages/polaris-dossier/src/cli.js');", "import = '../../../packages/polaris-dossier/src/cli.js' outside any if"],
  ])('the entry check sees %s (its own mutant)', (line, edge) => {
    expect(entryEdgesOf(`import * as path from 'node:path';\n${line}\n`)).toEqual([edge]);
  });

  it('fails on a form the preprocessor misses rather than passing it unseen', () => {
    expect(() => edgesOf("export * as dossier from '@syzygy/polaris-dossier';\n")).toThrow(
      'the preprocessor and the syntax walk disagree: {"walked":["@syzygy/polaris-dossier"],"reported":[]}',
    );
  });
});
