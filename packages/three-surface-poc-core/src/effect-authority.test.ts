import { describe, expect, it } from 'vitest';

import {
  BUTLERS_TRACKER_WRITE,
  dispatchAuthorization,
  effectAuthority,
  type Effect,
} from './effect-authority.js';

// Expected values are hard-coded literals, never imported from the module
// under test (oracle independence).
const OTHER: Effect = { id: 'synthetic-effect', surface: 'synthetic:surface' };

describe('effectAuthority', () => {
  it('forecloses the Butlers tracker write with citation P-71-Q5', () => {
    const verdict = dispatchAuthorization();
    expect(verdict.authorized).toBe(false);
    if (verdict.authorized || verdict.refusedBy !== 'foreclosed') throw new Error('expected foreclosed');
    expect(verdict.effect).toBe('butlers-tracker-write');
    expect(verdict.foreclosure.citation).toBe('P-71-Q5');
    expect(verdict.foreclosure.decisionPath).toBe(
      '.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md',
    );
  });

  it('keeps the foreclosure even when a registry entry names the write surface', () => {
    const verdict = effectAuthority({ writeSurface: ['butlers:.beads'] }, BUTLERS_TRACKER_WRITE);
    expect(verdict).toMatchObject({ authorized: false, refusedBy: 'foreclosed' });
  });

  it('refuses an effect the registry entry does not name', () => {
    expect(effectAuthority({ writeSurface: [] }, OTHER)).toMatchObject({
      authorized: false,
      effect: 'synthetic-effect',
      refusedBy: 'not-in-write-surface',
    });
    expect(effectAuthority({ writeSurface: ['synthetic:other'] }, OTHER)).toMatchObject({
      authorized: false,
      refusedBy: 'not-in-write-surface',
    });
  });

  it('refuses when no registry entry is supplied', () => {
    expect(effectAuthority(null, OTHER)).toMatchObject({
      authorized: false,
      refusedBy: 'registry-unavailable',
    });
  });

  it('refuses a malformed write surface', () => {
    for (const writeSurface of ['synthetic:surface', undefined, null, {}, [1], ['synthetic:surface', 2]]) {
      expect(effectAuthority({ writeSurface }, OTHER)).toMatchObject({
        authorized: false,
        refusedBy: 'write-surface-malformed',
      });
    }
  });

  it('authorizes only an unforeclosed effect the registry entry names', () => {
    expect(effectAuthority({ writeSurface: ['synthetic:surface'] }, OTHER)).toEqual({
      authorized: true,
      effect: 'synthetic-effect',
    });
  });
});
