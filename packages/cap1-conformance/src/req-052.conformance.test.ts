import { describe, expect, it } from 'vitest';
import { computeDiscoverability, type RepositoryId } from '@syzygy/cap1-core';

// CAP1-REQ-052 — not-applicable only for repositories with no governance root.
//
// Oracle: observed-source → not-applicable; governance-root must never
// get not-applicable. Falsifier: not-applicable on governance-root, or
// no on observed-source.

const REPO_ID = 'repo-test-052' as RepositoryId;

describe('CAP1-REQ-052 — not-applicable only for observed-source', () => {
  it('observed-source gets not-applicable regardless of evidence', () => {
    const finding = computeDiscoverability(REPO_ID, 'observed-source', {
      state: 'captured',
      linksToEntry: true,
    });
    expect(finding.value).toBe('not-applicable');
    expect(finding.basis).toBe('no-governance-root');
  });

  it('observed-source with uncaptured evidence still gets not-applicable', () => {
    const finding = computeDiscoverability(REPO_ID, 'observed-source', {
      state: 'uncaptured',
    });
    expect(finding.value).toBe('not-applicable');
  });

  it('falsifier: governance-root never gets not-applicable (captured linking)', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: true,
    });
    expect(finding.value).not.toBe('not-applicable');
  });

  it('falsifier: governance-root never gets not-applicable (uncaptured)', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'uncaptured',
    });
    expect(finding.value).not.toBe('not-applicable');
  });

  it('falsifier: observed-source never gets no', () => {
    const finding = computeDiscoverability(REPO_ID, 'observed-source', {
      state: 'captured',
      linksToEntry: false,
    });
    expect(finding.value).not.toBe('no');
  });
});
