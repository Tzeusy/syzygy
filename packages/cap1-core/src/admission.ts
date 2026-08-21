import type { ProjectId, RepositoryId } from './identity.js';
import type { ConsentResolution } from './consent.js';

// Admission and observation authority — CAP1-REQ-015's admission limb
// and CAP1-REQ-016, under RFC5-3 (classification by credential presented,
// never network location) and RFC1-3 (no consent means no observation).
// Pure domain logic: no transport, no credential store, no clock.

export type Credential =
  | { readonly presented: true; readonly token: string }
  | { readonly presented: false };

export type AdmissionResult =
  | { readonly admitted: true; readonly clientClass: 'machine' }
  | { readonly admitted: false; readonly served: 'nothing' };

// Admits a machine client by credential presented — and by NOTHING else.
//
// The signature is the enforcement of RFC5-3's rule: this function takes
// no network-location parameter at all, so location cannot influence
// admission because it cannot reach the decision. Two calls with the
// same credential are the same call, whatever addresses they arrived
// from — the two-location oracle limb of CAP1-REQ-015 holds at this
// layer by construction, and its transport-level test is the daemon
// slice's.
//
// Classification here is Capability 1's deliberate stub: a credential is
// admissible iff it is presented and non-empty. The daemon slice brings
// the real credential store (RFC5-5/RFC5-6 mechanisms); what is fixed
// NOW, and may not be weakened there, is the polarity — no presented
// credential means refused, and a refused client is served no boundary
// fact ('nothing', CAP1-REQ-015 oracle limb (c)).
export function admitClient(credential: Credential): AdmissionResult {
  if (credential.presented && credential.token.length > 0) {
    return { admitted: true, clientClass: 'machine' };
  }
  return { admitted: false, served: 'nothing' };
}

export type ObservationAuthorization =
  | { readonly authorized: true; readonly repositoryId: RepositoryId; readonly consentRecordId: string }
  | {
      readonly authorized: false;
      // Refusal renders as the unconsented POLICY state, never as an
      // error (CAP1-REQ-012, RFC6-26) and never as the repository's
      // absence.
      readonly render: 'unconsented-policy-state';
      readonly basis:
        | 'no-consent-for-pair'
        | 'consent-not-for-this-project'
        | 'consent-not-for-this-repository';
    };

// Observation authority exists ONLY per consented (project, repository)
// pair (CAP1-REQ-016; RFC1-3, RFC3-30).
//
// The resolution the caller passes is already per-pair (resolveConsent
// never lets one project's record grant another project's access). This
// function re-checks BOTH coordinates of the pair against the record the
// resolution cites: a resolution obtained for project A presented while
// serving project B refuses, and a consent resolved for repository A
// presented with a request for repository B refuses — authority never
// travels across projects or from one repository to a sibling, even
// inside one project. The symmetric checks make caller confusion (a
// reused resolution) structurally unable to grant here.
export function authorizeObservation(
  consentResolution: ConsentResolution,
  requestedProjectId: ProjectId,
  requestedRepositoryId: RepositoryId,
): ObservationAuthorization {
  if (!consentResolution.consented) {
    return {
      authorized: false,
      render: 'unconsented-policy-state',
      basis: 'no-consent-for-pair',
    };
  }
  if (consentResolution.record.projectId !== requestedProjectId) {
    return {
      authorized: false,
      render: 'unconsented-policy-state',
      basis: 'consent-not-for-this-project',
    };
  }
  if (consentResolution.record.repositoryId !== requestedRepositoryId) {
    return {
      authorized: false,
      render: 'unconsented-policy-state',
      basis: 'consent-not-for-this-repository',
    };
  }
  return {
    authorized: true,
    repositoryId: requestedRepositoryId,
    consentRecordId: consentResolution.record.id,
  };
}
