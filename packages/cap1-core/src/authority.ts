// Owning authority and effective status — pure domain logic, no I/O,
// no clock. Behavior is bound by CAP1-REQ-046 and the cited contract
// clauses RFC3-16 (lifecycle status: a self-declaration inside content,
// an effective status outside it; a tree-resident stamp is never
// self-authenticating; effective status is read from the owner-act
// record binding the artifact's exact immutable content digest; the two
// must be readable apart, and where they disagree the effective status
// governs and the disagreement renders as a disclosed fact; an artifact
// with no owner-act record has effective status unadopted whatever its
// stamp claims), RFC3-16(a) (the owner-act provenance predicate),
// RFC3-16(c) (a record's verification state is two-valued — owner-adopted
// bootstrap or Syzygy-verified — never conflated), and RFC6-13/14 (both
// values travel through the machine plane with full fidelity).

// The owning authority of an answer or artifact, with the governing
// normative revision (RFC6-19 class 4; CAP1-REQ-046: "the artifact's
// owning authority and governing revision").
export interface AuthorityReference {
  readonly authority: string;
  readonly governingRevision: string;
}

// A governance artifact as presented for status derivation. The stamp
// is UNTRUSTED CONTENT — a claim by whoever wrote the file, not proof
// of anything (RFC3-16) — so it is an arbitrary string here, never a
// closed vocabulary this module would lend credence to.
export interface GovernanceArtifactRef {
  readonly artifactId: string;
  // The exact immutable content digest of the artifact's bytes.
  readonly digest: string;
  readonly selfDeclaredStamp: string;
  readonly owningAuthority: AuthorityReference;
}

// An owner-act record. It binds an act to an artifact's EXACT digest
// (RFC3-16(b) item 3): a record naming any other digest binds nothing —
// an edit after the act breaks the digest and thereby the act. The
// record's own verification state is two-valued per RFC3-16(c). Acts
// are closed at the two adoptable-class outcomes Capability 1 serves.
export interface OwnerActRecord {
  readonly recordId: string;
  readonly artifactDigest: string;
  readonly act: 'adopted' | 'accepted';
  readonly provenanceState: 'owner-adopted-bootstrap' | 'syzygy-verified';
}

// The derived effective status: unadopted, or the recorded act's
// outcome. `unadopted` is the fail-closed floor — nothing in this
// module can derive a favourable status except an owner-act record at
// the exact digest.
export type EffectiveStatus = 'unadopted' | 'adopted' | 'accepted';

// What the effective status rests on — the record (with its two-valued
// provenance state carried, never conflated) or the disclosed absence
// of one.
export type EffectiveBasis =
  | {
      readonly recordId: string;
      readonly provenanceState: OwnerActRecord['provenanceState'];
    }
  | 'no-owner-act-record-at-this-digest';

// The served exposure. Stamp and effective status are two SEPARATE
// named fields by construction — there is no merged field, and no code
// path below writes one value into the other's field (CAP1-REQ-046
// falsifier: "stamp and effective status merged into one
// indistinguishable field").
export interface AuthorityExposure {
  readonly artifactId: string;
  readonly owningAuthority: AuthorityReference;
  // The self-declared lifecycle stamp, served as what it is: untrusted
  // content, readable apart from the effective status.
  readonly selfDeclaredStamp: string;
  // Derived from the owner-act record ONLY — never from the stamp.
  readonly effectiveStatus: EffectiveStatus;
  readonly effectiveBasis: EffectiveBasis;
  // Where stamp and effective status disagree, the disagreement is a
  // disclosed fact of the render — never silently reconciled in either
  // direction (RFC3-16). `undefined` means the two spellings agree.
  readonly disagreement:
    | {
        readonly disclosed: true;
        readonly stamp: string;
        readonly effectiveStatus: EffectiveStatus;
      }
    | undefined;
  // Which of the two governs the artifact's force. Constant by clause:
  // the effective status governs, always (RFC3-16) — the field exists
  // so the rule itself travels machine-readably with every exposure.
  readonly governs: 'effective-status';
}

// Derives the effective status of one artifact from the owner-act
// record set. Deterministic: a pure function of (artifact, records).
//
// - A record binds only at the artifact's EXACT digest; digest
//   comparison is byte equality of the digest strings.
// - With no record at that digest the artifact is effectively
//   unadopted, whatever its stamp claims (RFC3-16's effect rule for the
//   stamped-but-unverifiable case; CAP1-REQ-046's scenario).
// - With several records at one digest, the LAST in the list governs —
//   owner-act records are appended, never edited, so list order is
//   record order.
// - Disagreement is disclosed whenever the stamp's spelling differs
//   from the effective status — including the lawful draft-stamped,
//   effectively-accepted case (the self-declaration is read as the
//   state at authoring time, RFC3-16). Over-disclosure is lawful;
//   silence is not.
export function deriveEffectiveStatus(
  artifact: GovernanceArtifactRef,
  records: readonly OwnerActRecord[],
): AuthorityExposure {
  const binding = records.filter((record) => record.artifactDigest === artifact.digest);
  const governing = binding.length > 0 ? binding[binding.length - 1] : undefined;

  const effectiveStatus: EffectiveStatus =
    governing === undefined ? 'unadopted' : governing.act;
  const effectiveBasis: EffectiveBasis =
    governing === undefined
      ? 'no-owner-act-record-at-this-digest'
      : { recordId: governing.recordId, provenanceState: governing.provenanceState };

  return {
    artifactId: artifact.artifactId,
    owningAuthority: artifact.owningAuthority,
    selfDeclaredStamp: artifact.selfDeclaredStamp,
    effectiveStatus,
    effectiveBasis,
    disagreement:
      artifact.selfDeclaredStamp === effectiveStatus
        ? undefined
        : {
            disclosed: true,
            stamp: artifact.selfDeclaredStamp,
            effectiveStatus,
          },
    governs: 'effective-status',
  };
}

// True only when the derived effective status carries force. The answer
// layer consults THIS — never the stamp — so an answer resting on a
// stamped-but-unrecorded artifact treats it as unadopted
// (CAP1-REQ-046's scenario: "the answer treats the artifact as
// unadopted").
export function artifactInForce(exposure: AuthorityExposure): boolean {
  return exposure.effectiveStatus !== 'unadopted';
}
