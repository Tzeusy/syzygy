import { describe, expect, it } from 'vitest';
import { readDeclaration } from '@syzygy/cap1-core';

// CAP1-REQ-003 — Missing required information is visible.
//
// Case: the checker removes one required field from a valid declaration.
// Oracle: the output names the removed field; the expected name comes
// from RFC3-5's closed field set as written out in this file — never
// from the implementation (oracle independence). The sweep's denominator
// is the FULL required-field list from RFC3-5's table, written literally
// below (verification rule 9: a claim of absence needs a denominator).

// RFC3-5's closed top-level field set, verbatim from the table, in
// table order. Eight fields; RFC3-5 marks none optional.
const RFC3_5_FIELDS = [
  'schema_version',
  'project',
  'owner',
  'repositories',
  'consents',
  'declarations',
  'relations',
  'profiles',
] as const;

// A valid declaration authored as one block per top-level field, so the
// checker can remove exactly one field at a time.
const FIELD_BLOCKS: Record<(typeof RFC3_5_FIELDS)[number], string> = {
  schema_version: 'schema_version: "1"',
  project: 'project:\n  id: prj-opaque-7f3a\n  name: Orbital Mechanics',
  owner: 'owner: uniquosity@gmail.com',
  repositories:
    'repositories:\n  - id: repo-opaque-01\n    role: governance-root\n    consent: consent-record-01',
  consents: 'consents:\n  - consent-record-01',
  declarations: 'declarations:\n  spec_root: openspec/',
  relations: 'relations: []',
  profiles: 'profiles: []',
};

function sourceOmitting(omitted: string | null): string {
  return (
    RFC3_5_FIELDS.filter((field) => field !== omitted)
      .map((field) => FIELD_BLOCKS[field])
      .join('\n') + '\n'
  );
}

describe('CAP1-REQ-003 — missing required information is visible', () => {
  it('the sweep denominator is the full eight-field closed set from RFC3-5', () => {
    expect(RFC3_5_FIELDS).toHaveLength(8);
    expect(Object.keys(FIELD_BLOCKS)).toHaveLength(8);
  });

  it('the full declaration (nothing omitted) reads valid — the fixture is sound', () => {
    expect(readDeclaration(sourceOmitting(null)).ok).toBe(true);
  });

  for (const field of RFC3_5_FIELDS) {
    it(`scenario: omitting \`${field}\` yields a validation failure naming \`${field}\` as missing`, () => {
      const read = readDeclaration(sourceOmitting(field));
      expect(read.ok).toBe(false);
      if (!read.ok) {
        const naming = read.failures.filter(
          (f) => f.kind === 'missing-field' && f.field === field,
        );
        // The reader can enumerate what is missing from the served
        // output alone: the removed field is named, exactly once.
        expect(naming).toHaveLength(1);
      }
    });
  }

  it('multiple omissions are each named — enumeration from the output alone', () => {
    const read = readDeclaration(sourceOmitting('owner').replace('schema_version: "1"\n', ''));
    expect(read.ok).toBe(false);
    if (!read.ok) {
      const missing = read.failures
        .filter((f) => f.kind === 'missing-field')
        .map((f) => f.field)
        .sort();
      expect(missing).toEqual(['owner', 'schema_version']);
    }
  });

  it('falsifier: no generic failure naming nothing — every missing-field failure carries a field', () => {
    const read = readDeclaration(sourceOmitting('project'));
    expect(read.ok).toBe(false);
    if (!read.ok) {
      for (const failure of read.failures) {
        expect(failure.field).toBeTruthy();
      }
    }
  });
});
