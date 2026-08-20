import { describe, expect, it } from 'vitest';
import { designateRoots } from '@syzygy/cap1-core';
import type { RepositoryId, RootCandidate } from '@syzygy/cap1-core';

// CAP1-REQ-006 — Governance-root count violations surface; they are
// never repaired.
//
// Case: two repositories declaring the same project identity (two
// roots), and separately a project with no declaration (zero roots).
// Oracle: the two-root case serves a contradiction and no single chosen
// root; the zero-root case serves Unknown with the verbatim reason.
// Expected outcomes come from RFC1-1's stated rule, written literally
// here — never from the implementation's resolution logic.

const repoA = 'repo-opaque-01' as RepositoryId;
const repoB = 'repo-opaque-02' as RepositoryId;

function candidate(id: RepositoryId, hasDeclaration: boolean): RootCandidate {
  return { repositoryId: id, hasDeclaration };
}

describe('CAP1-REQ-006 — root-count violations surface, never repaired', () => {
  it('exactly one declaring repository is designated the root', () => {
    const result = designateRoots([candidate(repoA, true), candidate(repoB, false)]);
    expect(result.status).toBe('designated');
    if (result.status === 'designated') {
      expect(result.root).toBe(repoA);
    }
  });

  it('scenario: two governance roots — a contradiction routed to the owner, no winner picked', () => {
    const result = designateRoots([candidate(repoA, true), candidate(repoB, true)]);
    expect(result.status).toBe('contradiction');
    if (result.status === 'contradiction') {
      expect(result.kind).toBe('multiple-roots');
      expect(result.roots).toContain(repoA);
      expect(result.roots).toContain(repoB);
      expect(result.routedTo).toBe('owner');
    }
    // No repository is served as the chosen root: the contradiction arm
    // carries no `root` member at all.
    expect('root' in result).toBe(false);
  });

  it('scenario: zero governance roots — Unknown with reason `missing-declaration` at the workspace level', () => {
    const result = designateRoots([candidate(repoA, false), candidate(repoB, false)]);
    expect(result.status).toBe('unknown');
    if (result.status === 'unknown') {
      expect(result.scope).toBe('workspace');
      // Verbatim from the closed twelve-reason vocabulary (RFC2-24).
      expect(result.reason).toBe('missing-declaration');
    }
    // Never dropped, never rendered as an empty project, never a minted
    // contradiction (RFC1-1's zero-roots rule).
    expect(result.status).not.toBe('contradiction');
  });

  it('an empty candidate set is the zero-root case, not an error and not silence', () => {
    const result = designateRoots([]);
    expect(result.status).toBe('unknown');
    if (result.status === 'unknown') {
      expect(result.reason).toBe('missing-declaration');
    }
  });

  it('falsifier: two roots are never resolved by any precedence — ordering changes nothing', () => {
    // Freshest-file or first-found precedence would make the outcome
    // order-sensitive or pick a winner; assert neither occurs.
    const forward = designateRoots([candidate(repoA, true), candidate(repoB, true)]);
    const reversed = designateRoots([candidate(repoB, true), candidate(repoA, true)]);
    expect(forward.status).toBe('contradiction');
    expect(reversed.status).toBe('contradiction');
    if (forward.status === 'contradiction' && reversed.status === 'contradiction') {
      expect([...forward.roots].sort()).toEqual([...reversed.roots].sort());
      expect(forward.roots).toHaveLength(2);
      expect(reversed.roots).toHaveLength(2);
    }
  });

  it('the three candidate counts produce three distinct result shapes', () => {
    const zero = designateRoots([candidate(repoA, false)]);
    const one = designateRoots([candidate(repoA, true)]);
    const two = designateRoots([candidate(repoA, true), candidate(repoB, true)]);
    expect(new Set([zero.status, one.status, two.status]).size).toBe(3);
  });
});
