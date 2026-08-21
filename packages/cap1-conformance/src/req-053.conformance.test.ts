import { describe, expect, it } from 'vitest';
import {
  computeDiscoverability,
  computeDiscoverabilityWithProposal,
  proposeEntryLink,
  HUMAN_ENTRY_PATH,
  isInsideGovernedPlane,
  type RepositoryId,
} from '@syzygy/cap1-core';

// CAP1-REQ-053 — Proposal beside finding; finding unchanged; proposal
// carries proposed marking; no write outside plane.
//
// Oracle: the finding value is identical with and without a proposal.
// The proposal renders as proposed material, never as current state.

const REPO_ID = 'repo-test-053' as RepositoryId;

describe('CAP1-REQ-053 — proposal beside finding', () => {
  it('a proposal carries kind code-change-set and plane proposed', () => {
    const proposal = proposeEntryLink(REPO_ID, HUMAN_ENTRY_PATH);
    expect(proposal.kind).toBe('code-change-set');
    expect(proposal.plane).toBe('proposed');
  });

  it('finding value is unchanged by the proposal', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: false,
    });
    const withProposal = computeDiscoverabilityWithProposal(
      finding,
      proposeEntryLink(REPO_ID, HUMAN_ENTRY_PATH),
    );
    expect(withProposal.current.value).toBe('no');
    expect(withProposal.current).toBe(finding);
  });

  it('proposal renders beside the finding as proposed', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: false,
    });
    const proposal = proposeEntryLink(REPO_ID, HUMAN_ENTRY_PATH);
    const withProposal = computeDiscoverabilityWithProposal(finding, proposal);
    expect(withProposal.proposed.length).toBe(1);
    expect(withProposal.proposed[0]!.marking).toBe('proposed');
    expect(withProposal.proposed[0]!.plane).toBe('proposed');
    expect(withProposal.proposed[0]!.adopted).toBe(false);
  });

  it('without a proposal, the proposed array is empty', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: true,
    });
    const withProposal = computeDiscoverabilityWithProposal(finding, undefined);
    expect(withProposal.proposed.length).toBe(0);
    expect(withProposal.current).toBe(finding);
  });

  it('the entry path is inside the governed plane — no write outside', () => {
    expect(isInsideGovernedPlane(HUMAN_ENTRY_PATH)).toBe(true);
  });
});
