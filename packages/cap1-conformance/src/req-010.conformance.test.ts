import { describe, expect, it } from 'vitest';
import {
  computeCoverage,
  readDeclaration,
  type ConsentRecord,
  type ObservationOutcome,
  type ProjectDeclaration,
  type ProjectId,
  type RepositoryId,
} from '@syzygy/cap1-core';

// CAP1-REQ-010 — Every declared repository has an explicit coverage
// result.
//
// Case: the checker declares N repositories (some consented and
// reachable, some not) and queries coverage. Oracle: the answer contains
// exactly N results, one per declared repository, each carrying an
// observed-or-why-not value — N is the declaration's own count. Oracle
// independence: N and the per-repository conditions come from this
// fixture, not from anything the implementation computed.

const PROJECT = 'prj-cov-a1' as ProjectId;

// Three repositories declared: one consented and reachable, one
// unconsented, one consented but with no observation outcome at all.
const SOURCE = `
schema_version: "1"
project:
  id: prj-cov-a1
  name: Coverage Fixture
owner: uniquosity@gmail.com
repositories:
  - id: repo-observed
    role: governance-root
    consent: consent-r1
  - id: repo-unconsented
    role: observed-source
    consent: consent-r2
  - id: repo-never-captured
    role: observed-source
    consent: consent-r3
consents:
  - consent-r1
  - consent-r3
declarations:
  spec_root: openspec/
relations: []
profiles: []
`;

function declaration(): ProjectDeclaration {
  const read = readDeclaration(SOURCE);
  if (!read.ok) throw new Error('fixture must be valid');
  return read.declaration;
}

const CONSENTS: ConsentRecord[] = [
  {
    id: 'consent-r1',
    projectId: PROJECT,
    repositoryId: 'repo-observed' as RepositoryId,
    scope: 'observe',
    attribution: 'owner',
    grantState: 'in-force',
  },
  // repo-unconsented deliberately has NO record.
  {
    id: 'consent-r3',
    projectId: PROJECT,
    repositoryId: 'repo-never-captured' as RepositoryId,
    scope: 'observe',
    attribution: 'owner',
    grantState: 'in-force',
  },
];

const OBSERVATIONS: ObservationOutcome[] = [
  {
    repositoryId: 'repo-observed' as RepositoryId,
    outcome: 'captured',
    capturedScope: 'full-tree',
  },
  // repo-never-captured deliberately has NO outcome.
];

describe('CAP1-REQ-010 — every declared repository has an explicit coverage result', () => {
  it('oracle: exactly N results, one per declared repository, N = the declared count', () => {
    const decl = declaration();
    const result = computeCoverage(decl, CONSENTS, OBSERVATIONS);
    // Denominator asserted against the declaration's own count.
    expect(result.repositories).toHaveLength(decl.repositories.length);
    expect(result.repositories).toHaveLength(3);
    const served = result.repositories.map((entry) => entry.repositoryId);
    const declared = decl.repositories.map((entry) => entry.id);
    expect(served).toEqual(declared);
  });

  it('oracle: every result carries an observed-or-why-not value', () => {
    const result = computeCoverage(declaration(), CONSENTS, OBSERVATIONS);
    for (const entry of result.repositories) {
      if (entry.state === 'observed') {
        expect(entry.capturedScope.length).toBeGreaterThan(0);
      } else if (entry.state === 'degraded-partial') {
        expect(entry.capturedScope.length).toBeGreaterThan(0);
        expect(entry.uncaptured.reason.length).toBeGreaterThan(0);
      } else {
        // Every not-observed state names why not.
        expect(entry.label).toBe('Unknown');
        expect(entry.reason.length).toBeGreaterThan(0);
      }
    }
  });

  it('scenario: three declared, one unconsented — the unconsented one carries its explicit not-observed result rather than being omitted', () => {
    const result = computeCoverage(declaration(), CONSENTS, OBSERVATIONS);
    const unconsented = result.repositories.find(
      (entry) => entry.repositoryId === ('repo-unconsented' as RepositoryId),
    );
    expect(unconsented).toBeDefined();
    expect(unconsented?.state).toBe('unconsented');
  });

  it('falsifier: a repository with no observation outcome is not silently absent — it renders an explicit capture failure', () => {
    const result = computeCoverage(declaration(), CONSENTS, OBSERVATIONS);
    const never = result.repositories.find(
      (entry) => entry.repositoryId === ('repo-never-captured' as RepositoryId),
    );
    expect(never).toBeDefined();
    expect(never?.state).toBe('capture-failed');
  });

  it('falsifier: the coverage answer count never differs from the declaration count', () => {
    // Same declaration queried with zero consents and zero observations:
    // still exactly N explicit results.
    const decl = declaration();
    const bare = computeCoverage(decl, [], []);
    expect(bare.repositories).toHaveLength(decl.repositories.length);
  });
});
