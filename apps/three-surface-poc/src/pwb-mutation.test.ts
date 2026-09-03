// The mutation plan itself: every marked predicate is found, each
// mutation changes exactly one line, and the literal fragments exist
// exactly once in the current sources.

import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

import { INVALID_CASE_IDS } from '@syzygy/three-surface-poc-core';

import {
  CORE_SOURCE,
  LITERAL_MUTATIONS,
  OBSERVER_SOURCE,
  applyLiteralMutation,
  applyPredicateMutation,
  expectedFailuresForPredicate,
  listPredicateMutations,
} from './pwb-mutation.js';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const read = (file: string): string => readFileSync(join(REPO_ROOT, file), 'utf8');

describe('pwb mutation plan', () => {
  it('finds 85 predicate sites in the evaluator (55 common + 30 specific) and the observer gate', () => {
    const core = listPredicateMutations(CORE_SOURCE, read(CORE_SOURCE));
    expect(core.length).toBe(85);
    expect(new Set(core.map((mutation) => mutation.caseName)).size).toBe(85);
    const observer = listPredicateMutations(OBSERVER_SOURCE, read(OBSERVER_SOURCE));
    expect(observer.map((mutation) => mutation.caseName)).toEqual(['gate']);
  });

  it('every predicate site expands to exactly its instances in the 195-case vocabulary, covering all 195', () => {
    const core = listPredicateMutations(CORE_SOURCE, read(CORE_SOURCE));
    const covered = new Set<string>();
    for (const mutation of core) {
      const instances = expectedFailuresForPredicate(mutation, INVALID_CASE_IDS).map((name) => name.replace(/ →$/, ''));
      expect(instances.length === 1 || instances.length === 3).toBe(true);
      for (const id of instances) {
        expect(INVALID_CASE_IDS).toContain(id);
        expect(covered.has(id)).toBe(false);
        covered.add(id);
      }
    }
    expect(covered.size).toBe(195);
  });

  it('a predicate mutation changes exactly one line and wraps the whole condition', () => {
    const source = read(CORE_SOURCE);
    const [first] = listPredicateMutations(CORE_SOURCE, source);
    expect(first).toBeDefined();
    if (first === undefined) return;
    const mutated = applyPredicateMutation(source, first);
    const before = source.split('\n');
    const after = mutated.split('\n');
    expect(after.length).toBe(before.length);
    const changed = before.map((line, index) => (line === after[index] ? -1 : index)).filter((index) => index >= 0);
    expect(changed).toEqual([first.line - 1]);
    expect(after[first.line - 1]).toMatch(/if \(false && \(.+\)\) return/);
  });

  it('a predicate with nested parentheses is wrapped at the matching close paren', () => {
    const source = '// mutation-point: sample\nif (a(b(c)) && d(e)) return x;\n';
    const [mutation] = listPredicateMutations('f.ts', source);
    expect(mutation).toBeDefined();
    if (mutation === undefined) return;
    expect(applyPredicateMutation(source, mutation)).toBe('// mutation-point: sample\nif (false && (a(b(c)) && d(e))) return x;\n');
  });

  it('every literal mutation fragment occurs exactly once in its current source and names a must-fail test', () => {
    for (const mutation of LITERAL_MUTATIONS) {
      const source = read(mutation.file);
      expect(source.split(mutation.from).length - 1, mutation.id).toBe(1);
      expect(applyLiteralMutation(source, mutation)).not.toBe(source);
      expect(mutation.mustFail.length).toBeGreaterThan(0);
    }
    expect(new Set(LITERAL_MUTATIONS.map((mutation) => mutation.id)).size).toBe(LITERAL_MUTATIONS.length);
  });
});
