import { describe, expect, it } from 'vitest';
import { readDeclaration, registerProject } from '@syzygy/cap1-core';

// CAP1-REQ-001 — A valid declaration registers exactly one project.
//
// Case: the checker authors a valid declaration and triggers an
// evaluation over it. Oracle: the served project identifier and root
// designation are compared against the declaration the checker authored
// — equality decides; expected values come from this file, never from
// anything the implementation computed (oracle independence).

const DECLARED_PROJECT_ID = 'prj-opaque-7f3a';
const DECLARED_DISPLAY_NAME = 'Orbital Mechanics';

const VALID_SOURCE = `
schema_version: "1"
project:
  id: ${DECLARED_PROJECT_ID}
  name: ${DECLARED_DISPLAY_NAME}
owner: uniquosity@gmail.com
repositories:
  - id: repo-opaque-01
    role: governance-root
    consent: consent-record-01
consents:
  - consent-record-01
declarations:
  spec_root: openspec/
relations: []
profiles: []
`;

describe('CAP1-REQ-001 — valid declaration registers exactly one project', () => {
  it('reads the checker-authored valid declaration without failure', () => {
    const read = readDeclaration(VALID_SOURCE);
    expect(read.ok).toBe(true);
  });

  it('produces exactly one registered project carrying the declared identifier', () => {
    const result = registerProject(readDeclaration(VALID_SOURCE), 'rev-1');
    // Exactly one: the result is a single registration with a single
    // facts object — never zero, never a collection of two.
    expect(result.status).toBe('registered');
    if (result.status === 'registered') {
      expect(result.facts.projectId).toBe(DECLARED_PROJECT_ID);
      expect(result.facts.displayName).toBe(DECLARED_DISPLAY_NAME);
    }
  });

  it('designates the governance root by the file location, never a field value (RFC3-4)', () => {
    const result = registerProject(readDeclaration(VALID_SOURCE), 'rev-1');
    expect(result.status).toBe('registered');
    if (result.status === 'registered') {
      expect(result.facts.rootDesignation).toBe('declared-location');
    }
  });

  it('falsifier: identity never differs from the declared identifier', () => {
    // A registration whose identity differs from the declared opaque
    // identifier would falsify the requirement; assert it does not occur
    // for a second, independently authored declaration.
    const otherId = 'prj-opaque-99zz';
    const source = VALID_SOURCE.replace(DECLARED_PROJECT_ID, otherId);
    const result = registerProject(readDeclaration(source), 'rev-1');
    expect(result.status).toBe('registered');
    if (result.status === 'registered') {
      expect(result.facts.projectId).toBe(otherId);
      expect(result.facts.projectId).not.toBe(DECLARED_PROJECT_ID);
    }
  });
});
