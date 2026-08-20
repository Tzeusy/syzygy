import { describe, expect, it } from 'vitest';
import {
  ANSWER_VALUES,
  DISCOVERABILITY_VALUES,
  FACET_NAMES,
  MISSION_READY_DEFERRED_POSTURE,
  UNKNOWN_REASONS,
  parseDeclarationSource,
} from '@syzygy/cap1-core';

// Expected spellings are written out literally in this file, never derived
// from the implementation — oracle independence (the spec's own rule).

describe('CAP1-REQ-030 — the seven answer names, exact and ordered', () => {
  it('serves exactly the seven owner-ratified names in order (SDR-36)', () => {
    expect([...FACET_NAMES]).toEqual([
      'Registered',
      'Shape present',
      'Human-understandable',
      'Observable',
      'Traceable',
      'Mission-ready',
      'Reconciled',
    ]);
  });
});

describe('CAP1-REQ-030/034 — the three-spelling answer domain (SDR-35)', () => {
  it('closes the value domain at satisfied / Gap / Unknown, verbatim', () => {
    expect([...ANSWER_VALUES]).toEqual(['satisfied', 'Gap', 'Unknown']);
  });
});

describe('RFC2-24 — twelve Unknown reasons, closed', () => {
  it('carries twelve distinct non-empty reason spellings', () => {
    expect(UNKNOWN_REASONS).toHaveLength(12);
    expect(new Set(UNKNOWN_REASONS).size).toBe(12);
    for (const reason of UNKNOWN_REASONS) {
      expect(typeof reason).toBe('string');
      expect(reason.length).toBeGreaterThan(0);
    }
  });

  it('spells each reason verbatim from the clause', () => {
    expect([...UNKNOWN_REASONS]).toEqual([
      'missing-declaration',
      'missing-evidence',
      'no-currency-bound-declared',
      'stale-beyond-currency-bound',
      'mapping-coverage-absent',
      'unconsented-source-or-provider',
      'excluded-content',
      'contradicted-pending-adjudication',
      'challenge-suspended',
      'source-uncaptured-or-unreachable',
      'reference-unresolvable',
      'execution-blocked',
    ]);
  });
});

describe('CAP1-REQ-050 — the four discoverability spellings', () => {
  it('closes the domain at yes / no / not-applicable / Unknown, verbatim', () => {
    expect([...DISCOVERABILITY_VALUES]).toEqual([
      'yes',
      'no',
      'not-applicable',
      'Unknown',
    ]);
  });
});

describe('CAP1-REQ-036 — the Mission-ready deferred posture', () => {
  it('serves the three coordinates verbatim (SDR-36 rule 3)', () => {
    expect(MISSION_READY_DEFERRED_POSTURE.value).toBe('not evaluated');
    expect(MISSION_READY_DEFERRED_POSTURE.basis).toBe('deferred');
    expect(MISSION_READY_DEFERRED_POSTURE.label).toBe('Unknown');
    expect(Object.keys(MISSION_READY_DEFERRED_POSTURE)).toHaveLength(3);
  });
});

describe('yaml-dialect — the pinned declaration dialect (RFC3-1)', () => {
  it('parses a simple valid document', () => {
    const result = parseDeclarationSource('project: demo\nrepositories:\n  - main\n');
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.value).toEqual({ project: 'demo', repositories: ['main'] });
    }
  });

  it('rejects duplicate keys', () => {
    const result = parseDeclarationSource('project: one\nproject: two\n');
    expect(result.ok).toBe(false);
    if (!result.ok) {
      expect(result.error.length).toBeGreaterThan(0);
    }
  });
});
