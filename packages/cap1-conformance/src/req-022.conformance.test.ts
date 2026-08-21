import { describe, expect, it } from 'vitest';
import { assessEntry, type AuthorityCitation, type EntryContent } from '@syzygy/cap1-core';

// CAP1-REQ-022 — Missing/unreadable/stale/contradictory entry renders honestly.
//
// Oracle: absent → finding; unreadable → unknown-with-reason;
// contradictory → disagreement-disclosed with authority winning.
// Expected values are hard-coded string literals.

const AUTHORITY: AuthorityCitation = {
  identifier: 'VIS-1',
  kind: 'doctrine',
};

describe('CAP1-REQ-022 — honest entry rendering', () => {
  it('present content assesses as available', () => {
    const content: EntryContent = { state: 'present', text: 'Hello' };
    const assessment = assessEntry(content, [AUTHORITY]);
    expect(assessment.kind).toBe('available');
  });

  it('absent content is a FINDING, not an Unknown', () => {
    const content: EntryContent = { state: 'absent' };
    const assessment = assessEntry(content, [AUTHORITY]);
    expect(assessment.kind).toBe('finding');
  });

  it('unreadable content is Unknown with the reason disclosed', () => {
    const content: EntryContent = {
      state: 'unreadable',
      reason: 'permission denied',
    };
    const assessment = assessEntry(content, [AUTHORITY]);
    expect(assessment.kind).toBe('unknown-with-reason');
    if (assessment.kind === 'unknown-with-reason') {
      expect(assessment.reason).toBe('permission denied');
    }
  });

  it('stale content is a disagreement-disclosed with authority winning', () => {
    const content: EntryContent = {
      state: 'stale',
      authorityText: 'Authority says X',
      entryText: 'Entry says Y',
    };
    const assessment = assessEntry(content, [AUTHORITY]);
    expect(assessment.kind).toBe('disagreement-disclosed');
    if (assessment.kind === 'disagreement-disclosed') {
      expect(assessment.authorityWins).toBe(true);
      expect(assessment.authorityText).toBe('Authority says X');
      expect(assessment.entryText).toBe('Entry says Y');
    }
  });

  it('contradictory content discloses disagreement with authority ID', () => {
    const content: EntryContent = {
      state: 'contradictory',
      authorityText: 'Authority says A',
      entryText: 'Entry says B',
      authorityId: 'SEC-3',
    };
    const assessment = assessEntry(content, [AUTHORITY]);
    expect(assessment.kind).toBe('disagreement-disclosed');
    if (assessment.kind === 'disagreement-disclosed') {
      expect(assessment.authorityWins).toBe(true);
      expect(assessment.authorityId).toBe('SEC-3');
    }
  });
});
