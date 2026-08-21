import { describe, expect, it } from 'vitest';
import { renderEntry, type AuthorityCitation, type EntryContent } from '@syzygy/cap1-core';

// CAP1-REQ-021 — Entry routes to authority, never itself authority.
//
// Oracle: every rendering carries nonCitable: true and artifactClass:
// 'presentation-artifact'. No claim may source the entry.

const AUTHORITY: AuthorityCitation = {
  identifier: 'VIS-1',
  kind: 'doctrine',
};

describe('CAP1-REQ-021 — entry routes to authority, never itself authority', () => {
  it('a present entry renders with nonCitable: true', () => {
    const content: EntryContent = { state: 'present', text: 'Hello' };
    const rendering = renderEntry(content, [AUTHORITY]);
    expect(rendering.nonCitable).toBe(true);
  });

  it('a present entry renders with artifactClass presentation-artifact', () => {
    const content: EntryContent = { state: 'present', text: 'Hello' };
    const rendering = renderEntry(content, [AUTHORITY]);
    expect(rendering.artifactClass).toBe('presentation-artifact');
  });

  it('an absent entry still carries non-citable attributes', () => {
    const content: EntryContent = { state: 'absent' };
    const rendering = renderEntry(content, [AUTHORITY]);
    expect(rendering.nonCitable).toBe(true);
    expect(rendering.artifactClass).toBe('presentation-artifact');
  });

  it('authority citations are carried on the rendering', () => {
    const content: EntryContent = { state: 'present', text: 'Hello' };
    const rendering = renderEntry(content, [AUTHORITY]);
    expect(rendering.authorities).toContainEqual(AUTHORITY);
  });

  it('falsifier: no rendering lacks the non-citable marking', () => {
    const states: EntryContent[] = [
      { state: 'present', text: 'Hello' },
      { state: 'absent' },
      { state: 'unreadable', reason: 'permission denied' },
      { state: 'stale', authorityText: 'A', entryText: 'B' },
      {
        state: 'contradictory',
        authorityText: 'A',
        entryText: 'B',
        authorityId: 'VIS-1',
      },
    ];
    for (const content of states) {
      const rendering = renderEntry(content, [AUTHORITY]);
      expect(rendering.nonCitable).toBe(true);
      expect(rendering.artifactClass).toBe('presentation-artifact');
    }
  });
});
