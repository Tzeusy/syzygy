// Proposed material versus current state — pure domain logic. Behavior
// is bound by CAP1-REQ-063 and the cited contract clauses RFC1-27 (a
// Proposal is the single entity for every unadopted delta; every
// proposal declares an exclusivity group; competing proposals never
// collapse into a fictitious consensus) and RFC1-22 (the Proposed state
// plane: never desired, never observed; may not anchor the map).

// The five proposal kinds, verbatim from RFC1-27 (a)–(e), closed.
export const PROPOSAL_KINDS = [
  'governance-delta',
  'spec-delta',
  'code-change-set',
  'generated-code-shaped-artifact',
  'execution-intent',
] as const;
export type ProposalKind = (typeof PROPOSAL_KINDS)[number];

// An unadopted delta. The plane is fixed at the type level: a Proposal
// IS Proposed-plane material (RFC1-22) and nothing constructible here
// can claim another plane.
export interface Proposal {
  readonly id: string;
  readonly kind: ProposalKind;
  // What the proposal would change — a drafted declaration repair, a
  // drafted entry, a proposed repository-entry link (CAP1-REQ-063's
  // named examples all fit here as subjects).
  readonly subject: string;
  // RFC1-27: every proposal declares an exclusivity group.
  readonly exclusivityGroup: string;
  readonly plane: 'proposed';
}

// The rendering of one proposal: unmistakably distinct, machine-readably
// (CAP1-REQ-063). The distinction is carried as attributes on the
// rendered unit itself — `marking`, `plane`, `adopted`,
// `statusAuthority` — so it is recoverable without colour, position, or
// layout (CAP1-REQ-064's rule applied to this distinction).
export interface ProposalRendering {
  readonly proposalId: string;
  readonly kind: ProposalKind;
  readonly subject: string;
  readonly exclusivityGroup: string;
  readonly marking: 'proposed';
  readonly plane: 'proposed';
  readonly adopted: false;
  // A proposal carries NO status authority: it can neither set nor
  // improve any status value (CAP1-REQ-063).
  readonly statusAuthority: 'none';
}

export function renderProposal(proposal: Proposal): ProposalRendering {
  return {
    proposalId: proposal.id,
    kind: proposal.kind,
    subject: proposal.subject,
    exclusivityGroup: proposal.exclusivityGroup,
    marking: 'proposed',
    plane: 'proposed',
    adopted: false,
    statusAuthority: 'none',
  };
}

// The combined rendering of current state alongside open proposals.
export interface StateRendering<T> {
  readonly current: T;
  readonly proposed: readonly ProposalRendering[];
}

// Renders current state with proposals BESIDE it, never merged into it.
//
// The load-bearing property (CAP1-REQ-063): `current` is the caller's
// value, returned by reference, untouched — this function has no code
// path that reads a proposal while producing `current`, so a status
// value is identical with and without any open proposal, and proposed
// material turns nothing favourable. Proposals render ONLY inside
// `proposed`, each carrying the proposed marking.
//
// Competing proposals are rendered as N distinct candidate entries —
// never unioned, never collapsed into a consensus (RFC1-27); which
// pairs may not co-render as one projection is the exclusivity group's
// job, carried machine-readably on every rendering.
export function renderState<T>(
  current: T,
  proposals: readonly Proposal[],
): StateRendering<T> {
  return {
    current,
    proposed: proposals.map(renderProposal),
  };
}
