// The sweep plan must stay applicable to the sources it names: every
// literal fragment occurs exactly once in its subject, every group covers
// exactly one of the nine named classes and every class has a group, and
// the predicate subjects still expose their marker sites. This test never
// runs the mutations; the runner does, and its evidence file is the proof.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { describe, expect, it } from 'vitest';

import { applyLiteralMutation, listPredicateMutations } from './pwb-mutation.js';
import { SWEEP_CLASSES, SWEEP_GROUPS, groupSubjectFiles, judgmentExpectedFailures } from './pwb-mutation-sweep.js';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const read = (file: string): string => readFileSync(join(REPO_ROOT, file), 'utf8');

describe('PWB mutation sweep plan (task 4.2)', () => {
  it('names each of the nine classes exactly once, in the task order', () => {
    expect(SWEEP_GROUPS.map((group) => group.sweepClass)).toEqual([
      'source-denominator',
      'coverage-partition',
      'precedence-guard',
      'secret-sentinel',
      'capability-first-regression',
      'meta-copy-prohibition',
      'admission-invalid-cases',
      'judgment-invalid-cases',
      'parity-markers',
    ]);
    expect([...SWEEP_CLASSES]).toEqual(SWEEP_GROUPS.map((group) => group.sweepClass));
    expect(new Set(SWEEP_GROUPS.map((group) => group.id)).size).toBe(SWEEP_GROUPS.length);
  });

  it('every literal fragment occurs exactly once in its subject and changes it, with at least one must-fail test named', () => {
    const ids = new Set<string>();
    for (const group of SWEEP_GROUPS) {
      for (const mutation of group.literals) {
        expect(ids.has(mutation.id), `duplicate id ${mutation.id}`).toBe(false);
        ids.add(mutation.id);
        const source = read(mutation.file);
        expect(source.split(mutation.from).length - 1, `${mutation.id} occurrences`).toBe(1);
        expect(applyLiteralMutation(source, mutation)).not.toBe(source);
        expect(mutation.mustFail.length, `${mutation.id} must-fail`).toBeGreaterThan(0);
      }
    }
  });

  it('every group names existing test files that are not among its subjects', () => {
    for (const group of SWEEP_GROUPS) {
      expect(group.testFiles.length).toBeGreaterThan(0);
      for (const file of group.testFiles) {
        expect(file.endsWith('.test.ts')).toBe(true);
        expect(() => read(file)).not.toThrow();
      }
      for (const subject of groupSubjectFiles(group)) {
        expect(subject.endsWith('.test.ts')).toBe(false);
        expect(group.testFiles).not.toContain(subject);
      }
    }
  });

  it('the admission and judgment predicate subjects expose their marker sites (85 + 1 admission, 84 judgment cases + 1 history guard)', () => {
    const byGroup = Object.fromEntries(SWEEP_GROUPS.map((group) => [group.id, group]));
    const admission = byGroup['admission-invalid-cases'];
    const judgment = byGroup['judgment-invalid-cases'];
    expect(admission).toBeDefined();
    expect(judgment).toBeDefined();
    const admissionSites = (admission?.predicateSubjects ?? []).flatMap((s) => listPredicateMutations(s.file, read(s.file)));
    const judgmentSites = (judgment?.predicateSubjects ?? []).flatMap((s) => listPredicateMutations(s.file, read(s.file)));
    expect(admissionSites.length).toBe(86);
    expect(judgmentSites.length).toBe(85);
    expect(new Set(judgmentSites.map((s) => s.caseName)).size).toBe(85);
    expect(judgmentSites.filter((s) => s.caseName === 'history-append-only').length).toBe(1);
    const first = judgmentSites[0];
    expect(first).toBeDefined();
    if (first !== undefined) expect(judgmentExpectedFailures(first)).toEqual([` ${first.caseName}`]);
  });
});
