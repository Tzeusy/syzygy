import type { RepositoryId } from './identity.js';
import type { RepositoryRole } from './declaration.js';
import type { EpistemicState } from './epistemic.js';
import type { Proposal } from './proposal.js';
import { renderState, type StateRendering } from './proposal.js';
import { DISCOVERABILITY_VALUES, type DiscoverabilityValue } from './vocabulary.js';
import { HUMAN_ENTRY_PATH } from './entry.js';

// Repository discoverability — pure domain logic, no I/O, no clock.
// Behavior is bound by CAP1-REQ-050…053 and the cited contract clauses
// RFC7-40 (per-repository discoverability in four-value vocabulary),
// RFC7-41 (yes/no require evidence; missing = Unknown with reason),
// RFC7-42 (not-applicable only for repositories with no governance
// root), and RFC7-43 (may propose link; never writes README; proposal
// renders as proposed).

// The evidence from a repository's README (CAP1-REQ-051).
export type ReadmeEvidence =
  | { readonly state: 'captured'; readonly linksToEntry: boolean }
  | { readonly state: 'uncaptured' }
  | { readonly state: 'unconsented' }
  | { readonly state: 'undeclared' };

// One repository's discoverability finding (CAP1-REQ-050).
export interface DiscoverabilityFinding {
  readonly repositoryId: RepositoryId;
  readonly value: DiscoverabilityValue;
  readonly epistemic: EpistemicState;
  readonly basis?: string;
}

// Computes discoverability for one repository (CAP1-REQ-050…052).
// Checks applicability FIRST (REQ-052), then evidence (REQ-051).
export function computeDiscoverability(
  repositoryId: RepositoryId,
  role: RepositoryRole,
  evidence: ReadmeEvidence,
): DiscoverabilityFinding {
  if (role === 'observed-source') {
    return {
      repositoryId,
      value: 'not-applicable',
      epistemic: { label: 'Observed' },
      basis: 'no-governance-root',
    };
  }

  switch (evidence.state) {
    case 'captured':
      return {
        repositoryId,
        value: evidence.linksToEntry ? 'yes' : 'no',
        epistemic: { label: 'Observed' },
      };
    case 'uncaptured':
      return {
        repositoryId,
        value: 'Unknown',
        epistemic: {
          label: 'Unknown',
          reasons: {
            primary: 'source-uncaptured-or-unreachable',
            secondary: [],
          },
        },
        basis: 'source-uncaptured-or-unreachable',
      };
    case 'unconsented':
      return {
        repositoryId,
        value: 'Unknown',
        epistemic: {
          label: 'Unknown',
          reasons: {
            primary: 'unconsented-source-or-provider',
            secondary: [],
          },
        },
        basis: 'unconsented-source-or-provider',
      };
    case 'undeclared':
      return {
        repositoryId,
        value: 'Unknown',
        epistemic: {
          label: 'Unknown',
          reasons: {
            primary: 'missing-declaration',
            secondary: [],
          },
        },
        basis: 'missing-declaration',
      };
  }
}

// Proposes a README entry link without writing it (CAP1-REQ-053).
export function proposeEntryLink(
  repositoryId: RepositoryId,
  entryPath: typeof HUMAN_ENTRY_PATH,
): Proposal {
  return {
    id: `propose-entry-link-${repositoryId}`,
    kind: 'code-change-set',
    subject: `Add link to ${entryPath} in repository ${repositoryId} README`,
    exclusivityGroup: `entry-link-${repositoryId}`,
    plane: 'proposed',
  };
}

// A finding with an optional proposal rendered beside it (CAP1-REQ-053).
export type DiscoverabilityWithProposal = StateRendering<DiscoverabilityFinding>;

// The finding value is UNCHANGED by the proposal's existence
// (CAP1-REQ-053). The proposal renders beside it as proposed material.
export function computeDiscoverabilityWithProposal(
  finding: DiscoverabilityFinding,
  proposal: Proposal | undefined,
): DiscoverabilityWithProposal {
  return renderState(finding, proposal !== undefined ? [proposal] : []);
}
