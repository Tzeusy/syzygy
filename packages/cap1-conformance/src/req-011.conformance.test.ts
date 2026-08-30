import { describe, expect, it } from 'vitest';
import {
  computeCoverage,
  readDeclaration,
  resolveConsent,
  type ConsentRecord,
  type ObservationOutcome,
  type ProjectDeclaration,
  type ProjectId,
  type RepositoryId,
} from '@syzygy/cap1-core';

// CAP1-REQ-011 — Consent is a visible recorded fact, never an
// assumption.
//
// Sweep (the requirement's own case): for each declared (project,
// repository) pair, join the served coverage state to the consent
// records — denominator: the declared pair count. Oracle: every pair
// served as observed joins to an in-force consent record; every pair
// without one is served as unconsented. Oracle independence: the consent
// records are the checker's own fixture artifacts; the oracle joins
// against them directly, never consulting the implementation's consent
// logic.

const PROJECT = 'prj-consent-b2' as ProjectId;

const SOURCE = `
schema_version: "1"
project:
  id: prj-consent-b2
  name: Consent Fixture
owner: uniquosity@gmail.com
repositories:
  - id: repo-inforce
    role: governance-root
    consent: consent-inforce
  - id: repo-withdrawn
    role: observed-source
    consent: consent-withdrawn
  - id: repo-recordless
    role: observed-source
    consent: consent-missing
consents:
  - consent-inforce
  - consent-withdrawn
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

const IN_FORCE: ConsentRecord = {
  id: 'consent-inforce',
  projectId: PROJECT,
  repositoryId: 'repo-inforce' as RepositoryId,
  scope: 'observe',
  attribution: 'owner',
  grantState: 'in-force',
};

const WITHDRAWN: ConsentRecord = {
  id: 'consent-withdrawn',
  projectId: PROJECT,
  repositoryId: 'repo-withdrawn' as RepositoryId,
  scope: 'observe',
  attribution: 'owner',
  grantState: 'withdrawn',
};

const CONSENTS: ConsentRecord[] = [IN_FORCE, WITHDRAWN];

// Every repository has a capture outcome — so any repository that
// renders unconsented does so on consent grounds alone.
const OBSERVATIONS: ObservationOutcome[] = (
  ['repo-inforce', 'repo-withdrawn', 'repo-recordless'] as const
).map((id) => ({
  repositoryId: id as RepositoryId,
  outcome: 'captured',
  capturedScope: 'full-tree',
}));

describe('CAP1-REQ-011 — consent is a visible recorded fact, never an assumption', () => {
  it('scenario: consent state joins to a record — the served state cites the record with scope, attribution, and grant state', () => {
    const resolution = resolveConsent(CONSENTS, PROJECT, 'repo-inforce' as RepositoryId);
    expect(resolution.consented).toBe(true);
    if (resolution.consented) {
      expect(resolution.record.id).toBe('consent-inforce');
      expect(resolution.record.scope).toBe('observe');
      expect(resolution.record.attribution).toBe('owner');
      expect(resolution.record.grantState).toBe('in-force');
    }
    // And the coverage answer renders that record's facts, citing it.
    const result = computeCoverage(declaration(), CONSENTS, OBSERVATIONS);
    const observed = result.repositories.find((e) => e.state === 'observed');
    expect(observed).toBeDefined();
    if (observed?.state === 'observed') {
      expect(observed.consent.recordId).toBe('consent-inforce');
      expect(observed.consent.scope).toBe('observe');
      expect(observed.consent.attribution).toBe('owner');
      expect(observed.consent.grantState).toBe('in-force');
    }
  });

  it('absence of a resolvable in-force record renders as absence of consent — never implied consent', () => {
    const resolution = resolveConsent(CONSENTS, PROJECT, 'repo-recordless' as RepositoryId);
    expect(resolution.consented).toBe(false);
    if (!resolution.consented) {
      expect(resolution.basis).toBe('no-resolvable-in-force-record');
    }
  });

  it('a withdrawn record is not consent — and the withdrawal is distinguishable from record absence', () => {
    const resolution = resolveConsent(CONSENTS, PROJECT, 'repo-withdrawn' as RepositoryId);
    expect(resolution.consented).toBe(false);
    if (!resolution.consented) {
      expect(resolution.basis).toBe('withdrawn');
    }
  });

  it('sweep over every declared pair: observed ⇔ joins to an in-force record; no record ⇒ unconsented — denominator = declared pair count', () => {
    const decl = declaration();
    const result = computeCoverage(decl, CONSENTS, OBSERVATIONS);
    expect(result.repositories).toHaveLength(decl.repositories.length); // denominator

    for (const entry of result.repositories) {
      // The join is against the checker's own record set, not the
      // implementation's consent logic.
      const inForce = CONSENTS.find(
        (record) =>
          record.projectId === PROJECT &&
          record.repositoryId === entry.repositoryId &&
          record.grantState === 'in-force',
      );
      if (entry.state === 'observed' || entry.state === 'degraded-partial') {
        expect(inForce).toBeDefined();
        expect(entry.consent.recordId).toBe(inForce?.id);
      } else {
        expect(inForce).toBeUndefined();
        expect(entry.state).toBe('unconsented');
      }
    }
  });

  it('falsifier: a repository is never observed (no content served) without an in-force record, even when a capture outcome exists', () => {
    // Both repo-withdrawn and repo-recordless HAVE captured outcomes in
    // the fixture; neither may surface any captured content.
    const result = computeCoverage(declaration(), CONSENTS, OBSERVATIONS);
    for (const id of ['repo-withdrawn', 'repo-recordless']) {
      const entry = result.repositories.find((e) => e.repositoryId === (id as RepositoryId));
      expect(entry?.state).toBe('unconsented');
      expect(entry !== undefined && 'capturedScope' in entry).toBe(false);
    }
  });

  it('falsifier: absence of consent is never absence of the repository', () => {
    const result = computeCoverage(declaration(), CONSENTS, OBSERVATIONS);
    expect(
      result.repositories.some((e) => e.repositoryId === ('repo-recordless' as RepositoryId)),
    ).toBe(true);
  });
});

// R-S2 non-blocking finding #4: a consented-but-capture-failed/stale
// repository's in-force record was never cited, and a withdrawn pair
// never named WHICH withdrawal record defeated it. This fixture pairs a
// consented repository with each of 'unreachable' and 'stale' outcomes,
// so both failure states carry an in-force record to cite.

const CITATION_PROJECT = 'prj-citation-blo' as ProjectId;

const CITATION_SOURCE = `
schema_version: "1"
project:
  id: prj-citation-blo
  name: Citation Fixture
owner: uniquosity@gmail.com
repositories:
  - id: repo-capture-failed
    role: observed-source
    consent: consent-capture-failed
  - id: repo-stale
    role: observed-source
    consent: consent-stale
consents:
  - consent-capture-failed
  - consent-stale
declarations:
  spec_root: openspec/
relations: []
profiles: []
`;

function citationDeclaration(): ProjectDeclaration {
  const read = readDeclaration(CITATION_SOURCE);
  if (!read.ok) throw new Error('fixture must be valid');
  return read.declaration;
}

const CAPTURE_FAILED_RECORD: ConsentRecord = {
  id: 'consent-capture-failed',
  projectId: CITATION_PROJECT,
  repositoryId: 'repo-capture-failed' as RepositoryId,
  scope: 'observe',
  attribution: 'owner',
  grantState: 'in-force',
};

const STALE_RECORD: ConsentRecord = {
  id: 'consent-stale',
  projectId: CITATION_PROJECT,
  repositoryId: 'repo-stale' as RepositoryId,
  scope: 'observe',
  attribution: 'owner',
  grantState: 'in-force',
};

const CITATION_CONSENTS: ConsentRecord[] = [CAPTURE_FAILED_RECORD, STALE_RECORD];

const CITATION_OBSERVATIONS: ObservationOutcome[] = [
  { repositoryId: 'repo-capture-failed' as RepositoryId, outcome: 'unreachable' },
  { repositoryId: 'repo-stale' as RepositoryId, outcome: 'stale' },
];

describe('CAP1-REQ-011 R-S2 finding #4 — capture-failed and stale cite their in-force record', () => {
  it('consented + capture-failed cites the in-force record that stands behind the failed capture', () => {
    const result = computeCoverage(citationDeclaration(), CITATION_CONSENTS, CITATION_OBSERVATIONS);
    const entry = result.repositories.find(
      (e) => e.repositoryId === ('repo-capture-failed' as RepositoryId),
    );
    expect(entry?.state).toBe('capture-failed');
    if (entry?.state === 'capture-failed') {
      expect(entry.consent.recordId).toBe('consent-capture-failed');
      expect(entry.consent.scope).toBe('observe');
      expect(entry.consent.attribution).toBe('owner');
      expect(entry.consent.grantState).toBe('in-force');
    }
  });

  it('consented + stale cites the in-force record that stands behind the stale capture', () => {
    const result = computeCoverage(citationDeclaration(), CITATION_CONSENTS, CITATION_OBSERVATIONS);
    const entry = result.repositories.find((e) => e.repositoryId === ('repo-stale' as RepositoryId));
    expect(entry?.state).toBe('stale');
    if (entry?.state === 'stale') {
      expect(entry.consent.recordId).toBe('consent-stale');
      expect(entry.consent.scope).toBe('observe');
      expect(entry.consent.attribution).toBe('owner');
      expect(entry.consent.grantState).toBe('in-force');
    }
  });
});

// Conflict fixture: ONE pair carrying BOTH an in-force grant and a
// withdrawal. Records are append-only (RFC2-23 "Consent withdrawn":
// prior records remain, immutable, with the withdrawal visible), so
// grant-then-withdraw presents exactly this record set — and the record
// shape carries no ordering, so resolution may not decide the conflict
// by list position. The falsifier pins the fail-closed answer:
// withdrawal defeats grant, in EITHER list order.

const CONFLICT_PROJECT = 'prj-conflict-b2' as ProjectId;
const CONFLICT_REPO = 'repo-conflict' as RepositoryId;

const CONFLICT_SOURCE = `
schema_version: "1"
project:
  id: prj-conflict-b2
  name: Conflict Fixture
owner: uniquosity@gmail.com
repositories:
  - id: repo-conflict
    role: governance-root
    consent: consent-conflict-grant
consents:
  - consent-conflict-grant
  - consent-conflict-withdrawal
declarations:
  spec_root: openspec/
relations: []
profiles: []
`;

function conflictDeclaration(): ProjectDeclaration {
  const read = readDeclaration(CONFLICT_SOURCE);
  if (!read.ok) throw new Error('fixture must be valid');
  return read.declaration;
}

const CONFLICT_GRANT: ConsentRecord = {
  id: 'consent-conflict-grant',
  projectId: CONFLICT_PROJECT,
  repositoryId: CONFLICT_REPO,
  scope: 'observe',
  attribution: 'owner',
  grantState: 'in-force',
};

const CONFLICT_WITHDRAWAL: ConsentRecord = {
  id: 'consent-conflict-withdrawal',
  projectId: CONFLICT_PROJECT,
  repositoryId: CONFLICT_REPO,
  scope: 'observe',
  attribution: 'owner',
  grantState: 'withdrawn',
};

// Content WAS captured — so only the consent decision stands between the
// conflicted pair and its content being served.
const CONFLICT_OBSERVATIONS: ObservationOutcome[] = [
  { repositoryId: CONFLICT_REPO, outcome: 'captured', capturedScope: 'full-tree' },
];

describe('CAP1-REQ-011 falsifier — a pair holding both a grant and a withdrawal resolves closed', () => {
  it('in-force listed FIRST, withdrawal after: the withdrawal still defeats the grant — and names the withdrawal record', () => {
    const resolution = resolveConsent(
      [CONFLICT_GRANT, CONFLICT_WITHDRAWAL],
      CONFLICT_PROJECT,
      CONFLICT_REPO,
    );
    expect(resolution.consented).toBe(false);
    if (!resolution.consented) {
      expect(resolution.basis).toBe('withdrawn');
      if (resolution.basis === 'withdrawn') {
        expect(resolution.withdrawnRecord.id).toBe('consent-conflict-withdrawal');
      }
    }
  });

  it('withdrawal listed FIRST, in-force after: same answer, same cited record — list order never decides the conflict or its citation', () => {
    const resolution = resolveConsent(
      [CONFLICT_WITHDRAWAL, CONFLICT_GRANT],
      CONFLICT_PROJECT,
      CONFLICT_REPO,
    );
    expect(resolution.consented).toBe(false);
    if (!resolution.consented) {
      expect(resolution.basis).toBe('withdrawn');
      if (resolution.basis === 'withdrawn') {
        expect(resolution.withdrawnRecord.id).toBe('consent-conflict-withdrawal');
      }
    }
  });

  it('coverage over the conflicted pair renders unconsented with the verbatim reason, citing the withdrawal record — no captured content surfaces, in either record order', () => {
    for (const records of [
      [CONFLICT_GRANT, CONFLICT_WITHDRAWAL],
      [CONFLICT_WITHDRAWAL, CONFLICT_GRANT],
    ]) {
      const result = computeCoverage(conflictDeclaration(), records, CONFLICT_OBSERVATIONS);
      const entry = result.repositories.find((e) => e.repositoryId === CONFLICT_REPO);
      expect(entry?.state).toBe('unconsented');
      if (entry?.state === 'unconsented') {
        // Verbatim spelling hard-coded — the oracle never consults the
        // implementation's vocabulary module.
        expect(entry.reason).toBe('unconsented-source-or-provider');
        expect(entry.basis).toBe('withdrawn');
        // R-S2 finding #4: the withdrawal record IS the one cited —
        // never the in-force record it defeated, whatever list order.
        if (entry.basis === 'withdrawn') {
          expect(entry.consent.recordId).toBe('consent-conflict-withdrawal');
          expect(entry.consent.grantState).toBe('withdrawn');
        }
      }
      expect(entry !== undefined && 'capturedScope' in entry).toBe(false);
      expect(JSON.stringify(entry)).not.toContain('full-tree');
    }
  });
});
