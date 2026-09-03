// Authority disclosure — the ONE place the per-authority state text and
// the exact state-(1) sentence are rendered (PWB-REQ-005: every human
// and machine rendering of the authorization basis exposes each
// authority's exact state; only state (2) may be called independently
// verified; state (1) renders exactly the quoted sentence).
//
// Polaris, the home page and `/api/poc` all carry these strings from
// this module, so human/machine parity for the authorization basis is
// by construction rather than by comparison.

import {
  AUTHORITY_KINDS,
  STATE_1_LABEL,
  STATE_2_LABEL,
  type AuthorityKind,
  type AuthorityState,
  type BodyReadAuthorityEvaluation,
} from './body-read-authority.js';

// Quoted verbatim from PWB-REQ-005.
export const STATE_1_DISCLOSURE =
  "Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance." as const;

export const STATE_2_DISCLOSURE =
  'Independently verified: the owner act correlates with an A1 audit record kept outside this tree.' as const;

export interface AuthorityStateDisclosure {
  readonly authority: AuthorityKind;
  // RFC3-16(c)'s label for a valid act, or the non-valid kind.
  readonly state: typeof STATE_1_LABEL | typeof STATE_2_LABEL | 'invalid act' | 'absent';
  // True ONLY for state (2). Nothing else may claim independent verification.
  readonly independentlyVerified: boolean;
  readonly disclosure: string;
  readonly actIdentity: string | undefined;
  readonly artifactDigest: string | undefined;
  readonly invalidCase: string | undefined;
}

export interface AuthorityDisclosure {
  readonly evaluationId: string;
  readonly evaluationInstant: string;
  readonly admits: boolean;
  readonly authorizationMode: BodyReadAuthorityEvaluation['authorizationMode'];
  readonly authorities: readonly AuthorityStateDisclosure[];
  readonly contradiction: string | undefined;
}

export function discloseAuthorityState(authority: AuthorityKind, state: AuthorityState): AuthorityStateDisclosure {
  if (state.kind === 'valid') {
    return {
      authority,
      state: state.provenance === 'state-2' ? STATE_2_LABEL : STATE_1_LABEL,
      independentlyVerified: state.provenance === 'state-2',
      disclosure: state.provenance === 'state-2' ? STATE_2_DISCLOSURE : STATE_1_DISCLOSURE,
      actIdentity: state.actIdentity,
      artifactDigest: state.artifactDigest,
      invalidCase: undefined,
    };
  }
  if (state.kind === 'invalid') {
    return {
      authority,
      state: 'invalid act',
      independentlyVerified: false,
      disclosure: `Invalid owner act (${state.caseId}): ${state.detail}. No authority is in force; the artifact and its act remain visible.`,
      actIdentity: undefined,
      artifactDigest: state.artifactDigest,
      invalidCase: state.caseId,
    };
  }
  return {
    authority,
    state: 'absent',
    independentlyVerified: false,
    disclosure: `No owner act in force (${state.what}).`,
    actIdentity: undefined,
    artifactDigest: state.artifactDigest,
    invalidCase: undefined,
  };
}

export function discloseAuthority(evaluation: BodyReadAuthorityEvaluation): AuthorityDisclosure {
  return {
    evaluationId: evaluation.evaluationId,
    evaluationInstant: evaluation.evaluationInstant,
    admits: evaluation.admits,
    authorizationMode: evaluation.authorizationMode,
    authorities: AUTHORITY_KINDS.map((kind) => discloseAuthorityState(kind, evaluation[kind])),
    contradiction: evaluation.contradiction?.statement,
  };
}
