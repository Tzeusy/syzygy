import { readdirSync, readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

// The package is a leaf that every importer inherits (the owner-act drafter's own purity test
// stops at `@syzygy/support`), so what it may import is pinned here, not left to the closure guard,
// which admits `node:fs` (syzygy-bpyt.6.3, review R-GP-IMPL-SUPPORT-LEAF-1 N3).
const SRC = new URL('./', import.meta.url);
const SOURCES = readdirSync(SRC).filter((name) => name.endsWith('.ts') && !name.endsWith('.test.ts')).sort();

const ALLOWED_SPECIFIER = /^(?:node:crypto|\.\/[a-z0-9-]+\.js)$/u;
// The owner-act drafter's forbidden list (owner-act-drafter.test.ts), applied to every file of the package.
const FORBIDDEN = [/\brequire\(/, /\bimport\(/, /\bfetch\(/, /\bwriteFile/, /\bappendFile/, /\bmkdir/, /\bprocess\./, /\bDate\b/, /\b(?:node:)?(?:fs|net|http|https|child_process|os)['"`]/];

/** Every module specifier of a source text, whatever the quote: `from` imports and re-exports, side-effect imports, `import()` and `require()`. */
function specifiersOf(source: string): string[] {
  const code = source.split('\n').filter((line) => !line.trimStart().startsWith('//')).join('\n');
  return [
    ...[...code.matchAll(/\b(?:import|export)\b[^;]*?\bfrom\s*['"`]([^'"`]+)['"`]/g)].map((match) => match[1]!),
    ...[...code.matchAll(/^\s*import\s*['"`]([^'"`]+)['"`]/gm)].map((match) => match[1]!),
    ...[...code.matchAll(/\b(?:import|require)\s*\(\s*['"`]([^'"`]+)['"`]/g)].map((match) => match[1]!),
  ];
}

describe('@syzygy/support stays a pure leaf', () => {
  it('scans the package sources, not an empty list', () => {
    expect(SOURCES).toEqual(expect.arrayContaining(['deep-freeze.ts', 'index.ts', 'sha256.ts']));
  });

  it('imports only node:crypto and its own modules, so no file read, no workspace package and no network', () => {
    const imports = SOURCES.flatMap((file) => specifiersOf(readFileSync(new URL(file, SRC), 'utf8')).map((specifier) => ({ file, specifier })));
    expect(imports.filter(({ specifier }) => !ALLOWED_SPECIFIER.test(specifier))).toEqual([]);
    // The one external module is the hash.
    expect([...new Set(imports.map(({ specifier }) => specifier).filter((specifier) => !specifier.startsWith('./')))]).toEqual(['node:crypto']);
  });

  it('names no write, process, clock, network or file-system token in any source', () => {
    for (const name of SOURCES) {
      const source = readFileSync(new URL(name, SRC), 'utf8');
      for (const forbidden of FORBIDDEN) expect(source, `${name} ${String(forbidden)}`).not.toMatch(forbidden);
    }
  });

  it('declares no dependency and references no project in its manifests', () => {
    const manifest = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')) as Record<string, unknown>;
    for (const key of ['dependencies', 'devDependencies', 'peerDependencies', 'optionalDependencies']) expect(manifest[key] ?? {}, key).toEqual({});
    const tsconfig = JSON.parse(readFileSync(new URL('../tsconfig.json', import.meta.url), 'utf8')) as Record<string, unknown>;
    expect(tsconfig['references'] ?? []).toEqual([]);
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
