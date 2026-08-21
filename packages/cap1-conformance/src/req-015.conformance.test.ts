import { describe, expect, it } from 'vitest';
import {
  admitClient,
  computeCoverage,
  coverageBoundary,
  readDeclaration,
  type ConsentRecord,
  type Credential,
  type ObservationOutcome,
  type ProjectDeclaration,
  type ProjectId,
  type RepositoryId,
} from '@syzygy/cap1-core';

// CAP1-REQ-015 — One coverage boundary, retrievable identically by human
// and machine.
//
// What this file claims, and what it does NOT claim:
//
// Claimed here (pure layer): the boundary object is one deterministic
// value per (project, evaluation) input set — two computations are
// deeply equal — and it is the union of executed coverage records and
// declared captured scopes (RFC6-19 class 7); admission refuses a
// credential-less caller and serves it nothing; and admission's
// SIGNATURE excludes network location entirely (RFC5-3 by construction).
//
// DEFERRED to daemon-level tests — these oracle limbs stay OPEN, not
// silently satisfied:
//   (a) the dual-channel limb: retrieving the boundary through the real
//       human view and the real machine plane and comparing the two
//       served fact sets;
//   (b) the two-network-location limb: presenting one admissible
//       credential from two distinct network locations over real
//       transport and observing one admission outcome.
// This layer has no transport, so those limbs cannot be honestly tested
// here; the daemon slice owns them.

const PROJECT = 'prj-boundary-f6' as ProjectId;

const SOURCE = `
schema_version: "1"
project:
  id: prj-boundary-f6
  name: Boundary Fixture
owner: uniquosity@gmail.com
repositories:
  - id: repo-full
    role: governance-root
    consent: consent-f
  - id: repo-partial
    role: observed-source
    consent: consent-p
  - id: repo-unconsented
    role: observed-source
    consent: consent-x
consents:
  - consent-f
  - consent-p
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
    id: 'consent-f',
    projectId: PROJECT,
    repositoryId: 'repo-full' as RepositoryId,
    scope: 'observe',
    attribution: 'owner',
    grantState: 'in-force',
  },
  {
    id: 'consent-p',
    projectId: PROJECT,
    repositoryId: 'repo-partial' as RepositoryId,
    scope: 'observe',
    attribution: 'owner',
    grantState: 'in-force',
  },
];

const OBSERVATIONS: ObservationOutcome[] = [
  {
    repositoryId: 'repo-full' as RepositoryId,
    outcome: 'captured',
    capturedScope: 'full-tree',
  },
  {
    repositoryId: 'repo-partial' as RepositoryId,
    outcome: 'captured-partial',
    capturedScope: 'src/ only',
    declaredScope: 'full-tree',
  },
];

describe('CAP1-REQ-015 — one coverage boundary, retrievable identically by human and machine', () => {
  it('one boundary per (project, evaluation) input set, deterministic: two computations are deeply equal', () => {
    const first = coverageBoundary(computeCoverage(declaration(), CONSENTS, OBSERVATIONS));
    const second = coverageBoundary(computeCoverage(declaration(), CONSENTS, OBSERVATIONS));
    // Same records, same declared scopes, same consent states — equality
    // judged by comparison of the two independently computed values,
    // not by either computation's claim.
    expect(second).toEqual(first);
    expect(JSON.stringify(second)).toBe(JSON.stringify(first));
    expect(first.projectId).toBe(PROJECT);
  });

  it('the boundary is the union of executed coverage records and declared captured scopes', () => {
    const decl = declaration();
    const boundary = coverageBoundary(computeCoverage(decl, CONSENTS, OBSERVATIONS));
    // Every declared repository's executed coverage record is present —
    // including the unconsented one, whose consent state is itself a
    // boundary fact.
    expect(boundary.records).toHaveLength(decl.repositories.length);
    // The declared captured scopes: one per capture that declared one.
    expect(boundary.declaredCapturedScopes).toEqual([
      { repositoryId: 'repo-full', capturedScope: 'full-tree' },
      { repositoryId: 'repo-partial', capturedScope: 'src/ only' },
    ]);
  });

  it('oracle limb (c): a credential-less machine retrieval is refused and served no boundary fact', () => {
    const refused = admitClient({ presented: false });
    expect(refused.admitted).toBe(false);
    if (!refused.admitted) {
      expect(refused.served).toBe('nothing');
    }
    // An empty credential is not a credential.
    const empty = admitClient({ presented: true, token: '' });
    expect(empty.admitted).toBe(false);
  });

  it('an admissible credential admits, as a machine client', () => {
    const admitted = admitClient({ presented: true, token: 'cred-abc' });
    expect(admitted.admitted).toBe(true);
    if (admitted.admitted) {
      expect(admitted.clientClass).toBe('machine');
    }
  });

  it('RFC5-3 by construction: admission takes the credential and nothing else — no location parameter exists to influence it', () => {
    // The function's arity is the enforcement: exactly one parameter,
    // the credential. Network location cannot reach the decision.
    expect(admitClient.length).toBe(1);
    // And the credential type itself carries no location field.
    const credential: Credential = { presented: true, token: 'cred-abc' };
    expect(Object.keys(credential).sort()).toEqual(['presented', 'token']);
    // The dual-channel and two-location oracle limbs are daemon-level
    // tests, deferred to the daemon slice — see the header note. They
    // are NOT claimed by this file.
  });
});
