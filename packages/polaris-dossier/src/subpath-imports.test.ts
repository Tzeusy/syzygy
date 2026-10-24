import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';

// syzygy-bpyt.8.2: the daemon entry statically imports two of this package's modules by subpath, `/argv` and `/state-directory`,
// and the barrel only inside its `dossier` and `polaris` branches. Each subpath module may import node: built-ins alone, so the daemon
// path can reach neither this package's barrel, another @syzygy package nor a third-party module through them. Every import edge
// TypeScript's preprocessor reports counts: static, type-only, re-export, `require` and dynamic with a literal specifier.
// syzygy-bpyt.8.5 (one leaf util) may move both modules; this guard moves with them.

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const PACKAGE = 'packages/polaris-dossier';
const ENTRY = 'apps/syzygy/src/main.ts';

/** Every specifier `text` imports, by any form. */
const importsOf = (text: string): string[] => ts.preProcessFile(text, true, true).importedFiles.map((file) => file.fileName);
const builtIn = (specifier: string): boolean => specifier.startsWith('node:');

/** The source module a subpath export names: `./dist/X.js` is `src/X.ts`. */
function moduleOf(subpath: string): string {
  const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, PACKAGE, 'package.json'), 'utf8')) as { exports: Record<string, { import: string }> };
  const target = manifest.exports[subpath]?.import ?? '';
  return path.posix.join(PACKAGE, target.replace(/^\.\/dist\//u, 'src/').replace(/\.js$/u, '.ts'));
}

describe('the subpaths the daemon entry imports', () => {
  it('are /argv and /state-directory, imported statically, and the barrel is not', () => {
    const source = ts.createSourceFile(ENTRY, fs.readFileSync(path.join(ROOT, ENTRY), 'utf8'), ts.ScriptTarget.Latest);
    const statics = source.statements.filter(ts.isImportDeclaration)
      .map((statement) => (statement.moduleSpecifier as ts.StringLiteral).text)
      .filter((specifier) => specifier.startsWith('@syzygy/polaris-dossier'));
    expect(statics).toEqual(['@syzygy/polaris-dossier/argv', '@syzygy/polaris-dossier/state-directory']);
  });

  it.each([
    ['./argv', 'packages/polaris-dossier/src/argv.ts'],
    ['./state-directory', 'packages/polaris-dossier/src/state-directory.ts'],
  ])('%s is %s, which imports node: built-ins alone', (subpath, module) => {
    expect(moduleOf(subpath)).toBe(module);
    const imports = importsOf(fs.readFileSync(path.join(ROOT, module), 'utf8'));
    expect(imports.length).toBeGreaterThan(0);
    expect(imports.filter((specifier) => !builtIn(specifier))).toEqual([]);
  });

  it.each([
    ["import { DOSSIER_USAGE } from './cli.js';", './cli.js'],
    ["import type { CliPorts } from './index.js';", './index.js'],
    ["export * from '@syzygy/cap1-core';", '@syzygy/cap1-core'],
    ["const lazy = await import('typescript');", 'typescript'],
    ["const fs = require('fs');", 'fs'],
  ])('the check sees a forbidden import in %s (its own mutant)', (line, specifier) => {
    expect(importsOf(`import * as path from 'node:path';\n${line}\n`).filter((found) => !builtIn(found))).toEqual([specifier]);
  });
});
