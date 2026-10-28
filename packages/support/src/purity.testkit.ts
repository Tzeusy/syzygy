// Test support: the one module-specifier reader and the one forbidden-token list that two purity guards stand on, this package's
// own (support-purity.test.ts) and the owner-act drafter's (owner-act-drafter.test.ts), so the two cannot drift (syzygy-bpyt.6.14,
// the PR 530 round-2 review's N9). Test support only: no module of the package imports it.

/** Every module specifier of a source text, whatever the quote: `from` imports and re-exports, side-effect imports, `import()` and
 * `require()`. Comment lines are prose. A specifier that is not a string literal is not read. */
export function specifiersOf(source: string): string[] {
  const code = source.split('\n').filter((line) => !line.trimStart().startsWith('//')).join('\n');
  return [
    ...[...code.matchAll(/\b(?:import|export)\b[^;]*?\bfrom\s*['"`]([^'"`]+)['"`]/g)].map((match) => match[1]!),
    ...[...code.matchAll(/^\s*import\s*['"`]([^'"`]+)['"`]/gm)].map((match) => match[1]!),
    ...[...code.matchAll(/\b(?:import|require)\s*\(\s*['"`]([^'"`]+)['"`]/g)].map((match) => match[1]!),
  ];
}

/** Tokens a pure module names nowhere, comments included: a write, a process or clock read, `require()`, `import()`, `fetch()`,
 * and the file-system, network, child-process and OS modules. */
export const FORBIDDEN: readonly RegExp[] = [/\brequire\(/, /\bimport\(/, /\bfetch\(/, /\bwriteFile/, /\bappendFile/, /\bmkdir/, /\bprocess\./, /\bDate\b/, /\b(?:node:)?(?:fs|net|http|https|child_process|os)['"`]/];
