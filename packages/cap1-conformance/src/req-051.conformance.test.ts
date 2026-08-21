import { describe, expect, it } from 'vitest';
import { computeDiscoverability, type RepositoryId } from '@syzygy/cap1-core';

// CAP1-REQ-051 — yes/no require evidence; missing = Unknown with reason.
//
// Oracle: captured-linking → yes; captured-not-linking → no;
// uncaptured → Unknown with 'source-uncaptured-or-unreachable';
// unconsented → Unknown with 'unconsented-source-or-provider'.
// Expected reason strings are hard-coded literals.

const REPO_ID = 'repo-test-051' as RepositoryId;

describe('CAP1-REQ-051 — evidence-backed findings', () => {
  it('captured README linking to entry → yes', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: true,
    });
    expect(finding.value).toBe('yes');
    expect(finding.epistemic.label).toBe('Observed');
  });

  it('captured README not linking to entry → no', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'captured',
      linksToEntry: false,
    });
    expect(finding.value).toBe('no');
    expect(finding.epistemic.label).toBe('Observed');
  });

  it('uncaptured source → Unknown with source-uncaptured-or-unreachable', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'uncaptured',
    });
    expect(finding.value).toBe('Unknown');
    expect(finding.epistemic.label).toBe('Unknown');
    expect('reasons' in finding.epistemic).toBe(true);
    if ('reasons' in finding.epistemic) {
      expect(finding.epistemic.reasons.primary).toBe('source-uncaptured-or-unreachable');
    }
  });

  it('unconsented source → Unknown with unconsented-source-or-provider', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'unconsented',
    });
    expect(finding.value).toBe('Unknown');
    expect(finding.epistemic.label).toBe('Unknown');
    expect('reasons' in finding.epistemic).toBe(true);
    if ('reasons' in finding.epistemic) {
      expect(finding.epistemic.reasons.primary).toBe('unconsented-source-or-provider');
    }
  });

  it('undeclared → Unknown with missing-declaration', () => {
    const finding = computeDiscoverability(REPO_ID, 'governance-root', {
      state: 'undeclared',
    });
    expect(finding.value).toBe('Unknown');
    expect(finding.epistemic.label).toBe('Unknown');
    expect('reasons' in finding.epistemic).toBe(true);
    if ('reasons' in finding.epistemic) {
      expect(finding.epistemic.reasons.primary).toBe('missing-declaration');
    }
  });
});
