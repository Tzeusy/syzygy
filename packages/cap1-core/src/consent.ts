import type { ProjectId, RepositoryId } from './identity.js';

// Consent as a recorded fact, never an assumption (CAP1-REQ-011).
//
// A consent record's subject is the pair (observing project, repository)
// — RFC3-7's observation-consent kind, per-pair and never global
// (RFC3-30). Identity here is the declared opaque identifier, never a
// URL, path, or branch (RFC3-6, RFC1-2): nothing in this module accepts
// or compares a locator. Pure domain logic: callers hand in the record
// set; no I/O, no clock.

export type GrantState = 'in-force' | 'withdrawn';

export interface ConsentRecord {
  // The record's own identifier — the declaration references records by
  // id (RFC3-7: referenced, never embedded).
  readonly id: string;
  // The consented pair. Consent is a property of exactly this
  // (project, repository) pair (RFC1-3, RFC3-7, RFC3-30); a record for
  // another project grants nothing here.
  readonly projectId: ProjectId;
  readonly repositoryId: RepositoryId;
  // What is consented — scope enumerates the consented acts (RFC3-7).
  readonly scope: string;
  // Who granted it — the record's stored attribution (RFC3-16(a)).
  readonly attribution: string;
  readonly grantState: GrantState;
}

// The two ways a pair can lack consent, kept distinct so a rendering can
// say which (REQ-011: consent state derives only from records — including
// the withdrawn state, which RFC2-23's "Consent withdrawn" row renders
// visibly rather than as mere absence).
export type ConsentAbsenceBasis = 'no-resolvable-in-force-record' | 'withdrawn';

export type ConsentResolution =
  | { readonly consented: true; readonly record: ConsentRecord }
  | { readonly consented: false; readonly basis: ConsentAbsenceBasis };

// Resolves the consent state for one (project, repository) pair from the
// record set, and from nothing else.
//
// The polarity is the load-bearing decision (CAP1-REQ-011; RFC3-7):
// consent exists ONLY when an in-force record for exactly this pair
// resolves. Absence of a resolvable in-force record IS absence of
// consent — never implied consent, never a default-open. A record whose
// projectId names a different project never grants access here, whatever
// its repositoryId (no cross-project bleed: CAP1-REQ-016, RFC3-30).
//
// Withdrawal defeats grant — the pair fails CLOSED on conflict. Records
// are append-only (RFC2-23 "Consent withdrawn": prior records remain,
// immutable, with the withdrawal visible), so grant-then-withdraw
// presents BOTH an in-force record and a withdrawn record for one pair;
// the record shape carries no ordering, so this layer cannot tell
// grant→withdraw from withdraw→regrant. It therefore refuses: ANY
// withdrawn record for the pair defeats EVERY in-force record for the
// pair, and the pair resolves unconsented with basis 'withdrawn'.
// Regrant-after-withdrawal consequently needs record-supersession
// semantics this layer does not define — a data-contract question
// routed onward, not guessed here.
//
// Deterministic: a pure function of (records, projectId, repositoryId).
// When several in-force records exist for one (withdrawal-free) pair,
// the first in record order resolves — record order is the caller's
// stable governance-plane order, so the resolution is reproducible per
// evaluation.
export function resolveConsent(
  records: readonly ConsentRecord[],
  projectId: ProjectId,
  repositoryId: RepositoryId,
): ConsentResolution {
  const forThisPair = records.filter(
    (record) => record.projectId === projectId && record.repositoryId === repositoryId,
  );

  // Withdrawal first: a withdrawn record for this exact pair renders the
  // pair unconsented whatever else the pair's record set holds — never
  // decided by list order, never in favor of access.
  if (forThisPair.some((record) => record.grantState === 'withdrawn')) {
    return { consented: false, basis: 'withdrawn' };
  }

  const inForce = forThisPair.find((record) => record.grantState === 'in-force');
  if (inForce !== undefined) {
    return { consented: true, record: inForce };
  }

  // No record for this pair resolves at all — absence of consent, kept
  // distinguishable from a visible withdrawal; neither is an error state.
  return { consented: false, basis: 'no-resolvable-in-force-record' };
}
