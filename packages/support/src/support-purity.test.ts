import { readdirSync, readFileSync } from 'node:fs';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';
import { FORBIDDEN, specifiersOf } from './purity.testkit.js';

// The package is a leaf that every importer inherits (the owner-act drafter's own purity test
// stops at `@syzygy/support`), so what it may import and name is pinned here, not left to the closure guard,
// which admits `node:fs` (syzygy-bpyt.6.3, review R-GP-IMPL-SUPPORT-LEAF-1 N3). Every source module under `src` is
// read, at any depth and with any JavaScript or TypeScript extension; the test files and the one testkit are test
// support (syzygy-bpyt.6.14, the PR 530 round-2 review's N9).
const SRC = new URL('./', import.meta.url);
const SOURCES = readdirSync(SRC, { recursive: true, encoding: 'utf8' })
  .filter((name) => /\.[cm]?[jt]sx?$/u.test(name) && !name.endsWith('.test.ts') && name !== 'purity.testkit.ts').sort();
const read = (name: string): string => readFileSync(new URL(name, SRC), 'utf8');

const ALLOWED_SPECIFIER = /^(?:node:crypto|\.\/[a-z0-9-]+\.js)$/u;
// Every name the package's code may use: its own declarations and parameters, the hash's `createHash().update().digest()`,
// and `Object`'s freeze walk. A global (`globalThis`, `process`, `console`, `fetch`, `WebSocket`, `performance`), another
// export of `node:crypto` (`randomBytes`) or a loader (`require`, `eval`, `Function`) is a name not on it.
const ALLOWED_IDENTIFIERS = new Set(['Object', 'T', 'Uint8Array', 'createHash', 'deepFreeze', 'digest', 'freeze', 'isFrozen', 'member', 'sha256', 'update', 'value', 'values']);

/** Every identifier a module's code names, sorted: declarations, references, property names and type names alike. Comments
 * and the contents of strings are not code. */
function identifiersOf(name: string, source: string): string[] {
  const names = new Set<string>();
  const visit = (node: ts.Node): void => {
    if (ts.isIdentifier(node) || ts.isPrivateIdentifier(node)) names.add(node.text);
    ts.forEachChild(node, visit);
  };
  visit(ts.createSourceFile(name, source, ts.ScriptTarget.Latest, false));
  return [...names].sort();
}

describe('@syzygy/support stays a pure leaf', () => {
  it('scans every source module under src, at any depth, not an empty list', () => {
    expect(SOURCES).toEqual(expect.arrayContaining(['deep-freeze.ts', 'index.ts', 'sha256.ts']));
  });

  it('names no module but node:crypto and a module beside it in any literal specifier of any source', () => {
    const imports = SOURCES.flatMap((file) => specifiersOf(read(file)).map((specifier) => ({ file, specifier })));
    expect(imports.filter(({ specifier }) => !ALLOWED_SPECIFIER.test(specifier))).toEqual([]);
    // The one external module is the hash.
    expect([...new Set(imports.map(({ specifier }) => specifier).filter((specifier) => !specifier.startsWith('./')))]).toEqual(['node:crypto']);
  });

  it('names no identifier outside its literal list in any source', () => {
    expect(SOURCES.flatMap((file) => identifiersOf(file, read(file)).filter((name) => !ALLOWED_IDENTIFIERS.has(name)).map((name) => `${file}: ${name}`))).toEqual([]);
  });

  it('names none of the forbidden tokens it shares with the owner-act drafter in any source', () => {
    for (const name of SOURCES) {
      const source = read(name);
      for (const forbidden of FORBIDDEN) expect(source, `${name} ${String(forbidden)}`).not.toMatch(forbidden);
    }
  });

  it('declares no dependency and references no project in its manifests', () => {
    const manifest = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')) as Record<string, unknown>;
    for (const key of ['dependencies', 'devDependencies', 'peerDependencies', 'optionalDependencies']) expect(manifest[key] ?? {}, key).toEqual({});
    const tsconfig = JSON.parse(readFileSync(new URL('../tsconfig.json', import.meta.url), 'utf8')) as Record<string, unknown>;
    expect(tsconfig['references'] ?? []).toEqual([]);
  });

  it('exports exactly the "." entry, index.js, so no other module is an entry', () => {
    const manifest = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')) as Record<string, unknown>;
    expect(manifest['exports']).toEqual({ '.': { types: './dist/index.d.ts', import: './dist/index.js', default: './dist/index.js' } });
  });
});

describe('the specifier reader this guard stands on', () => {
  // A guard whose reader misses a form passes over the form it was written for.
  const CASES: readonly (readonly [string, readonly string[]])[] = [
    ["import { createHash } from 'node:crypto';", ['node:crypto']],
    ['import { readFileSync } from "node:fs";', ['node:fs']],
    ["export { sha256 } from './sha256.js';", ['./sha256.js']],
    ["import 'node:http';", ['node:http']],
    ["const fs = await import('node:fs');", ['node:fs']],
    ["const fs = require('node:fs');", ['node:fs']],
    ["import type { X } from '@syzygy/cap1-core';", ['@syzygy/cap1-core']],
    ["// import { readFileSync } from 'node:fs';\nexport const a = 1;", []],
    ['export const a = 1;', []],
  ];
  it.each(CASES)('reads %j', (source, expected) => {
    expect(specifiersOf(source)).toEqual(expected);
  });
});

describe('the forbidden-token list both guards stand on', () => {
  // One form per token, each matched by that token alone, so a token dropped from the shared list fails its row.
  const CASES: readonly string[] = [
    'const m = require(name);', 'const m = await import(name);', 'await fetch(url);', 'writeFileSync(p, d);', 'appendFileSync(p, d);',
    'mkdirSync(p);', 'const h = process.env.HOME;', 'const t = new Date();', "import { readFileSync } from 'node:fs';",
  ];
  it.each(CASES)('refuses %j', (source) => {
    expect(FORBIDDEN.filter((forbidden) => forbidden.test(source))).toHaveLength(1);
  });
});

describe('the identifier reader the allowlist stands on', () => {
  const CASES: readonly (readonly [string, readonly string[]])[] = [
    ["const h = globalThis['process']; // console.log(h)", ['globalThis', 'h']],
    ['/** fetch(url) */\nexport const a = b.c?.(`${d}e`);', ['a', 'b', 'c', 'd']],
    ['class K { #p = 1; m<T>(v: T): T { return v; } }', ['#p', 'K', 'T', 'm', 'v']],
    ['import { randomBytes as r } from "node:crypto";', ['r', 'randomBytes']],
    ['const \\u0070rocess = 1;', ['process']],
  ];
  it.each(CASES)('reads %j', (source, expected) => {
    expect(identifiersOf('case.ts', source)).toEqual(expected);
  });
});
