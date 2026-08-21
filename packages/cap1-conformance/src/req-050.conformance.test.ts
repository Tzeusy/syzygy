import { describe, expect, it } from 'vitest';
import { computeDiscoverability, type RepositoryId } from '@syzygy/cap1-core';

// CAP1-REQ-050 — Per-repository discoverability in four-value vocabulary.
//
// Oracle: the closed four values are yes, no, not-applicable, Unknown.
// One finding per repository; values are verbatim strings compared
// against hard-coded literals.

const REPO_ID = 'repo-test-001' as RepositoryId;

describe('CAP1-REQ-050 — closed four-value discoverability vocabulary', () => {
  it('yes is a verbatim string value', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: true,
    });
    expect(finding.value).toBe('yes');
  });

  it('no is a verbatim string value', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: false,
    });
    expect(finding.value).toBe('no');
  });

  it('not-applicable is a verbatim string value', () => {
    const finding = computeDiscoverability(REPO_ID, 'observed-source', {
      state: 'undeclared',
    });
    expect(finding.value).toBe('not-applicable');
  });

  it('Unknown is a verbatim string value', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'uncaptured',
    });
    expect(finding.value).toBe('Unknown');
  });

  it('one finding per repository carries the repository ID', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: true,
    });
    expect(finding.repositoryId).toBe(REPO_ID);
  });
});
