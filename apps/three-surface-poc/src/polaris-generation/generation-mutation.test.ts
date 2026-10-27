// The generation mutation plan itself, one row per mutation, so a source edit
// that moves a guarded fragment fails here, on the PR that makes it, rather
// than in the scheduled generation-mutation gate, and every drifted mutation
// is reported by id in the same run. The runner stops at the first missing
// fragment; syzygy-kpbq found the scheduled gate red on every run from
// 2026-10-04 to 2026-10-27 after 5955f8c0 split the repair-cycle cap, with a
// second fragment (moved by 69995614) behind it.
//
// Each row checks the plan's shape, not that the mutation disables its guard:
// the file lies under packages/polaris-generation-core/src/ and is not a test,
// the fragment occurs exactly once there, the mutation changes the emitted
// JavaScript (so a fragment matched only in a comment, or a `to` that differs
// from `from` only in spacing, fails), and every must-fail name lies in an
// `it` or `test` title, or an `each` title template, of a file the runner
// runs. Whether the mutated guard is then caught is the gate's own run
// (generation-mutation-run-main.ts).

import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import ts from 'typescript';
import { describe, expect, it } from 'vitest';

import { GENERATION_LITERAL_MUTATIONS, applyLiteralMutation, type LiteralMutation } from './generation-mutation.js';

const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
const read = (file: string): string => readFileSync(join(REPO_ROOT, file), 'utf8');
const SUBJECT_ROOT = 'packages/polaris-generation-core/src/';
const RUNNER = 'apps/three-surface-poc/src/polaris-generation/generation-mutation-run-main.ts';
// The test files the runner runs (its TEST_FILES); a must-fail name is matched against their results only.
const RUNNER_TEST_FILES = [
  'packages/polaris-generation-core/src/canonical-json.test.ts',
  'packages/polaris-generation-core/src/parse-json.test.ts',
  'packages/polaris-generation-core/src/pipeline.test.ts',
  'packages/polaris-generation-core/src/provider-draft.test.ts',
];

const emit = (file: string, text: string): string =>
  ts.transpileModule(text, {
    fileName: file,
    compilerOptions: { removeComments: true, target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext },
  }).outputText;

// The literal titles of every `it(...)`, `test(...)`, `it.each(...)(...)` and
// `test.each(...)(...)` call in a test file; an `each` title keeps its `%s`.
const isTestCallee = (callee: ts.Expression): boolean =>
  (ts.isIdentifier(callee) && ['it', 'test'].includes(callee.text)) ||
  (ts.isCallExpression(callee) && ts.isPropertyAccessExpression(callee.expression) && callee.expression.name.text === 'each' &&
    ts.isIdentifier(callee.expression.expression) && ['it', 'test'].includes(callee.expression.expression.text));
function testTitles(file: string): string[] {
  const titles: string[] = [];
  const visit = (node: ts.Node): void => {
    if (ts.isCallExpression(node) && isTestCallee(node.expression)) {
      const [title] = node.arguments;
      if (title !== undefined && ts.isStringLiteralLike(title)) titles.push(title.text);
    }
    ts.forEachChild(node, visit);
  };
  visit(ts.createSourceFile(file, read(file), ts.ScriptTarget.Latest, true));
  return titles;
}

describe('generation mutation plan', () => {
  it('holds twelve mutations with distinct ids, and the runner runs the test files their must-fail names are read from', () => {
    expect(GENERATION_LITERAL_MUTATIONS.length).toBe(12);
    expect(new Set(GENERATION_LITERAL_MUTATIONS.map((mutation) => mutation.id)).size).toBe(GENERATION_LITERAL_MUTATIONS.length);
    const runner = read(RUNNER);
    for (const file of RUNNER_TEST_FILES) expect(runner, file).toContain(`'${file}'`);
  });

  it.each(GENERATION_LITERAL_MUTATIONS.map((mutation): [string, LiteralMutation] => [mutation.id, mutation]))(
    '%s: names a non-test file under polaris-generation-core/src, holds its fragment once there, changes the emit and names must-fail tests the runner runs',
    (id, mutation) => {
      expect(mutation.file.startsWith(SUBJECT_ROOT) && !mutation.file.endsWith('.test.ts'), `${id}: ${mutation.file} is a non-test file under ${SUBJECT_ROOT}`).toBe(true);
      const source = read(mutation.file);
      expect(source.split(mutation.from).length - 1, `${id}: occurrences of the fragment in ${mutation.file}`).toBe(1);
      expect(emit(mutation.file, applyLiteralMutation(source, mutation)), `${id}: the mutation changes the emitted JavaScript`).not.toBe(emit(mutation.file, source));
      expect(mutation.mustFail.length, `${id}: must-fail names`).toBeGreaterThan(0);
      const titles = RUNNER_TEST_FILES.flatMap(testTitles);
      for (const name of mutation.mustFail) expect(titles.some((title) => title.includes(name)), `${id}: must-fail "${name}" is in a test title`).toBe(true);
    },
  );
});
