import { describe, expect, it } from 'vitest';
import {
  artifactInForce,
  deriveEffectiveStatus,
  type GovernanceArtifactRef,
  type OwnerActRecord,
} from '@syzygy/cap1-core';

// CAP1-REQ-046 — Owning authority and effective status are exposed,
// stamp and record readable apart (state projection/query).
//
// Case: a checker presents an artifact whose stamp says `accepted` with
// no owner-act record, and queries an answer resting on it. Oracle: the
// served effective status is unadopted; both values are separately
// readable in the fact set. Bounded: one artifact, one fact set. Oracle
// independence: the fixture controls the stamp and the absence of a
// record; the rule is RFC3-16's. Falsifier: a stamped-but-unrecorded
// artifact served as effectively accepted, or stamp and effective
// status merged into one indistinguishable field.

const DIGEST = 'sha256:0f2e6c1a9b3d5e7f';

function artifact(stamp: string): GovernanceArtifactRef {
  return {
    artifactId: 'policy:governance/policies/example-policy.md',
    digest: DIGEST,
    selfDeclaredStamp: stamp,
    owningAuthority: {
      authority: 'governance/policies/example-policy.md',
      governingRevision: DIGEST,
    },
  };
}

const RECORD: OwnerActRecord = {
  recordId: 'act-record-17',
  artifactDigest: DIGEST,
  act: 'accepted',
  provenanceState: 'owner-adopted-bootstrap',
};

describe('CAP1-REQ-046 — stamp is not status; owning authority and effective status exposed', () => {
  it('scenario: a stamp claiming `accepted` with no owner-act record serves effective status unadopted, both readable apart', () => {
    const exposure = deriveEffectiveStatus(artifact('accepted'), []);
    // Hard-coded spellings: the served effective status is unadopted
    // whatever the stamp claims...
    expect(exposure.effectiveStatus).toBe('unadopted');
    // ...the untrusted stamp stays separately readable...
    expect(exposure.selfDeclaredStamp).toBe('accepted');
    // ...the disagreement renders as a disclosed fact...
    expect(exposure.disagreement).toEqual({
      disclosed: true,
      stamp: 'accepted',
      effectiveStatus: 'unadopted',
    });
    // ...the effective status governs...
    expect(exposure.governs).toBe('effective-status');
    expect(exposure.effectiveBasis).toBe('no-owner-act-record-at-this-digest');
    // ...and the answer treats the artifact as unadopted.
    expect(artifactInForce(exposure)).toBe(false);
  });

  it('falsifier: stamp and effective status are never merged — both fields exist on every exposure, independently valued', () => {
    const exposure = deriveEffectiveStatus(artifact('accepted'), []);
    const keys = Object.keys(exposure);
    expect(keys).toContain('selfDeclaredStamp');
    expect(keys).toContain('effectiveStatus');
    expect(exposure.selfDeclaredStamp).not.toBe(exposure.effectiveStatus);
  });

  it('an owner-act record at the exact digest makes the artifact effectively accepted, carrying the record and its two-valued provenance', () => {
    const exposure = deriveEffectiveStatus(artifact('accepted'), [RECORD]);
    expect(exposure.effectiveStatus).toBe('accepted');
    expect(exposure.effectiveBasis).toEqual({
      recordId: 'act-record-17',
      provenanceState: 'owner-adopted-bootstrap',
    });
    // Stamp and effective agree here — no disagreement is minted.
    expect(exposure.disagreement).toBeUndefined();
    expect(artifactInForce(exposure)).toBe(true);
  });

  it('a draft-stamped artifact whose exact digest carries a record is effectively accepted, with the disagreement disclosed', () => {
    const exposure = deriveEffectiveStatus(artifact('draft'), [RECORD]);
    expect(exposure.effectiveStatus).toBe('accepted');
    expect(exposure.selfDeclaredStamp).toBe('draft');
    // The self-declaration reads as authoring-time state; the
    // difference is disclosed, never silently reconciled (RFC3-16).
    expect(exposure.disagreement).toEqual({
      disclosed: true,
      stamp: 'draft',
      effectiveStatus: 'accepted',
    });
  });

  it('falsifier: a record naming a different digest binds nothing — an edit after the act destroys it', () => {
    const editedArtifact: GovernanceArtifactRef = {
      ...artifact('accepted'),
      digest: 'sha256:EDITED-after-the-act',
    };
    const exposure = deriveEffectiveStatus(editedArtifact, [RECORD]);
    expect(exposure.effectiveStatus).toBe('unadopted');
    expect(exposure.effectiveBasis).toBe('no-owner-act-record-at-this-digest');
    expect(artifactInForce(exposure)).toBe(false);
  });

  it('the owning authority and governing revision are exposed on every answer resting on the artifact', () => {
    const exposure = deriveEffectiveStatus(artifact('accepted'), [RECORD]);
    expect(exposure.owningAuthority).toEqual({
      authority: 'governance/policies/example-policy.md',
      governingRevision: DIGEST,
    });
    expect(exposure.artifactId).toBe('policy:governance/policies/example-policy.md');
  });

  it('with several records at one digest, the last appended governs — records are appended, never edited', () => {
    const adopted: OwnerActRecord = {
      recordId: 'act-record-16',
      artifactDigest: DIGEST,
      act: 'adopted',
      provenanceState: 'owner-adopted-bootstrap',
    };
    const exposure = deriveEffectiveStatus(artifact('accepted'), [adopted, RECORD]);
    expect(exposure.effectiveStatus).toBe('accepted');
    expect(exposure.effectiveBasis).toEqual({
      recordId: 'act-record-17',
      provenanceState: 'owner-adopted-bootstrap',
    });
  });

  it('the syzygy-verified provenance state travels unconflated', () => {
    const verified: OwnerActRecord = { ...RECORD, provenanceState: 'syzygy-verified' };
    const exposure = deriveEffectiveStatus(artifact('accepted'), [verified]);
    expect(exposure.effectiveBasis).toEqual({
      recordId: 'act-record-17',
      provenanceState: 'syzygy-verified',
    });
  });

  it('an empty stamp is still readable apart, and force still derives from the record set alone', () => {
    const exposure = deriveEffectiveStatus(artifact(''), []);
    expect(exposure.selfDeclaredStamp).toBe('');
    expect(exposure.effectiveStatus).toBe('unadopted');
    expect(exposure.disagreement).toEqual({
      disclosed: true,
      stamp: '',
      effectiveStatus: 'unadopted',
    });
  });
});
