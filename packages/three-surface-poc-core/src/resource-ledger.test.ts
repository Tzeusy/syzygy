// The evaluation-wide resource ledger: registry `resourceLimits`,
// `parsePassIdentities` and `resourceLimitSemantics` as amended 2026-09-05
// (registry amendment act); PWB-REQ-006 as amended (truth-and-readiness
// amendment act). Expected pass identities and limit values are hand-typed
// literals — never imported from the module under test.

import { describe, expect, it } from 'vitest';

import { PWB_RESOURCE_LIMITS, type PwbResourceLimits } from './project-shape-observation.js';
import {
  PARSE_PASS_IDENTITIES,
  ParsePassBudgetExceeded,
  SECRET_DETECTOR_PASSES,
  createResourceLedger,
  isParsePassIdentity,
  type ParsePassIdentity,
} from './resource-ledger.js';

// Hand-typed from the amended registry entry.
const REGISTRY_PASSES = [
  'utf8-and-nul-validation',
  'secret-private-key-fragments',
  'secret-known-token-formats',
  'secret-credential-assignment',
  'secret-credential-bearing-url',
  'markdown-code-context-mask',
  'active-html-svg-script-handler',
  'unsafe-url-positions',
  'phase-a-link-discovery',
  'project-account-extraction',
  'declared-item-extraction',
  'fact-and-precedence-extraction',
] as const;

const OID_A = 'a'.repeat(40);
const OID_B = 'b'.repeat(40);

function limits(overrides: Partial<PwbResourceLimits>): PwbResourceLimits {
  return { ...PWB_RESOURCE_LIMITS, ...overrides };
}

describe('registry-bound pass identities', () => {
  it('the closed list is the registry list, in order', () => {
    expect([...PARSE_PASS_IDENTITIES]).toEqual([...REGISTRY_PASSES]);
    for (const pass of REGISTRY_PASSES) expect(isParsePassIdentity(pass)).toBe(true);
    expect(isParsePassIdentity('regex-scan')).toBe(false);
    expect(isParsePassIdentity('')).toBe(false);
  });

  it('every policy detector maps onto its own registry pass', () => {
    expect(SECRET_DETECTOR_PASSES).toEqual({
      'private-key-material': 'secret-private-key-fragments',
      'known-token-formats': 'secret-known-token-formats',
      'credential-assignment': 'secret-credential-assignment',
      'credential-bearing-url': 'secret-credential-bearing-url',
    });
  });

  it('every named pass is chargeable and counted under its own identity', () => {
    const ledger = createResourceLedger(limits({ maxParsePassesPerSource: 100 }));
    for (const pass of REGISTRY_PASSES) expect(ledger.chargePass('p', pass)).toBeUndefined();
    const summary = ledger.summary();
    expect(summary.parsePasses).toBe(12);
    expect(summary.sourcesTraversed).toBe(1);
    expect(summary.maxPassesOnOneSource).toBe(12);
    for (const pass of REGISTRY_PASSES) expect(summary.passesByIdentity[pass]).toBe(1);
  });

  it('an unregistered traversal is forbidden: it throws and charges nothing', () => {
    const ledger = createResourceLedger(PWB_RESOURCE_LIMITS);
    expect(() => ledger.chargePass('p', 'regex-scan' as ParsePassIdentity)).toThrow(/unregistered parse pass "regex-scan" on p: an unregistered traversal is forbidden/);
    expect(() => ledger.chargeFor('p')('' as ParsePassIdentity)).toThrow(/unregistered/);
    expect(ledger.passesFor('p')).toBe(0);
    expect(ledger.breaches).toEqual([]);
  });
});

describe('maxParsePassesPerSource — one budget per source, wall-clock never an input', () => {
  it('limit − 1 and limit pass; limit + 1 breaches and is recorded once per crossing', () => {
    const ledger = createResourceLedger(limits({ maxParsePassesPerSource: 3 }));
    expect(ledger.chargePass('p', 'utf8-and-nul-validation')).toBeUndefined();
    expect(ledger.chargePass('p', 'markdown-code-context-mask')).toBeUndefined();
    expect(ledger.passesFor('p')).toBe(2);
    expect(ledger.chargePass('p', 'unsafe-url-positions')).toBeUndefined();
    expect(ledger.passesFor('p')).toBe(3);
    expect(ledger.breaches).toEqual([]);
    expect(ledger.chargePass('p', 'phase-a-link-discovery')).toEqual({ limit: 'maxParsePassesPerSource', declared: 3, observed: 4, path: 'p' });
    expect(ledger.breaches).toEqual([{ limit: 'maxParsePassesPerSource', declared: 3, observed: 4, path: 'p' }]);
  });

  it('repeating a pass counts again', () => {
    const ledger = createResourceLedger(limits({ maxParsePassesPerSource: 2 }));
    expect(ledger.chargePass('p', 'secret-known-token-formats')).toBeUndefined();
    expect(ledger.chargePass('p', 'secret-known-token-formats')).toBeUndefined();
    expect(ledger.chargePass('p', 'secret-known-token-formats')).toMatchObject({ limit: 'maxParsePassesPerSource', observed: 3 });
    // The refused traversal never ran: it is a breach, not a performed pass.
    expect(ledger.summary().passesByIdentity['secret-known-token-formats']).toBe(2);
    expect(ledger.passesFor('p')).toBe(2);
    expect(ledger.chargePass('p', 'secret-known-token-formats')).toMatchObject({ observed: 3 });
    expect(ledger.breaches).toHaveLength(2);
  });

  it('budgets are per source: a second path starts at zero', () => {
    const ledger = createResourceLedger(limits({ maxParsePassesPerSource: 1 }));
    expect(ledger.chargePass('a', 'utf8-and-nul-validation')).toBeUndefined();
    expect(ledger.chargePass('b', 'utf8-and-nul-validation')).toBeUndefined();
    expect(ledger.chargePass('a', 'utf8-and-nul-validation')).toBeDefined();
    expect(ledger.passesFor('b')).toBe(1);
    expect(ledger.summary().sourcesTraversed).toBe(2);
  });

  it('chargeFor throws ParsePassBudgetExceeded carrying the breach and the pass that never ran', () => {
    const ledger = createResourceLedger(limits({ maxParsePassesPerSource: 1 }));
    const charge = ledger.chargeFor('p');
    charge('utf8-and-nul-validation');
    let caught: unknown;
    try {
      charge('active-html-svg-script-handler');
    } catch (error) {
      caught = error;
    }
    expect(caught).toBeInstanceOf(ParsePassBudgetExceeded);
    const error = caught as ParsePassBudgetExceeded;
    expect(error.name).toBe('ParsePassBudgetExceeded');
    expect(error.pass).toBe('active-html-svg-script-handler');
    expect(error.breach).toEqual({ limit: 'maxParsePassesPerSource', declared: 1, observed: 2, path: 'p' });
    expect(error.message).toBe('parse pass budget exceeded on p at active-html-svg-script-handler: 2 > 1');
  });
});

describe('maxTotalBytes — one cumulative counter across both phases', () => {
  it('limit − 1 and limit fit; limit + 1 breaches and is not counted', () => {
    for (const [size, fits] of [
      [9, true],
      [10, true],
      [11, false],
    ] as const) {
      const ledger = createResourceLedger(limits({ maxTotalBytes: 10 }));
      const breach = ledger.chargeBody('p', OID_A, size);
      if (fits) {
        expect(breach, String(size)).toBeUndefined();
        expect(ledger.totalBytes()).toBe(size);
        expect(ledger.counted('p', OID_A)).toBe(true);
      } else {
        expect(breach).toEqual({ limit: 'maxTotalBytes', declared: 10, observed: 11, path: 'p' });
        expect(ledger.totalBytes()).toBe(0);
        expect(ledger.counted('p', OID_A)).toBe(false);
        expect(ledger.breaches).toEqual([breach]);
      }
    }
  });

  it('the counter accumulates and never resets: the body that would cross is refused, a later smaller one may fit', () => {
    const ledger = createResourceLedger(limits({ maxTotalBytes: 10 }));
    expect(ledger.chargeBody('a', OID_A, 6)).toBeUndefined();
    expect(ledger.chargeBody('b', OID_B, 5)).toMatchObject({ limit: 'maxTotalBytes', observed: 11, path: 'b' });
    expect(ledger.chargeBody('c', OID_B, 4)).toBeUndefined();
    expect(ledger.totalBytes()).toBe(10);
    expect(ledger.summary().bodiesCounted).toBe(2);
  });

  it('one (path, object id) body counts once, however many times it is charged', () => {
    const ledger = createResourceLedger(limits({ maxTotalBytes: 10 }));
    expect(ledger.chargeBody('p', OID_A, 7)).toBeUndefined();
    expect(ledger.chargeBody('p', OID_A, 7)).toBeUndefined();
    expect(ledger.projectBody('p', OID_A, 7)).toBeUndefined();
    expect(ledger.totalBytes()).toBe(7);
    expect(ledger.summary().bodiesCounted).toBe(1);
    expect(ledger.breaches).toEqual([]);
  });

  it('the same object at a different path, or a different object at the same path, is another body', () => {
    const ledger = createResourceLedger(limits({ maxTotalBytes: 100 }));
    ledger.chargeBody('p', OID_A, 7);
    ledger.chargeBody('q', OID_A, 7);
    ledger.chargeBody('p', OID_B, 7);
    expect(ledger.totalBytes()).toBe(21);
    expect(ledger.summary().bodiesCounted).toBe(3);
  });

  it('projectBody evaluates a declared size without counting it', () => {
    const ledger = createResourceLedger(limits({ maxTotalBytes: 10 }));
    expect(ledger.projectBody('p', OID_A, 10)).toBeUndefined();
    expect(ledger.totalBytes()).toBe(0);
    expect(ledger.projectBody('p', OID_A, 11)).toEqual({ limit: 'maxTotalBytes', declared: 10, observed: 11, path: 'p' });
    expect(ledger.breaches).toHaveLength(1);
  });
});

describe('transient phase-A bodies', () => {
  it('a remembered body is recalled by (path, object id) until release', () => {
    const ledger = createResourceLedger(PWB_RESOURCE_LIMITS);
    const body = { bytes: new Uint8Array([104, 105]), text: 'hi' };
    ledger.remember('p', OID_A, body);
    expect(ledger.recall('p', OID_A)).toBe(body);
    expect(ledger.recall('p', OID_B)).toBeUndefined();
    expect(ledger.recall('q', OID_A)).toBeUndefined();
    ledger.release();
    expect(ledger.recall('p', OID_A)).toBeUndefined();
  });
});

describe('summary and breach order', () => {
  it('the summary is a snapshot with every identity present and breaches in occurrence order', () => {
    const ledger = createResourceLedger(limits({ maxTotalBytes: 1, maxParsePassesPerSource: 1 }));
    ledger.recordBreach({ limit: 'maxSources', declared: 1, observed: 2, path: 'x' });
    ledger.chargeBody('p', OID_A, 2);
    ledger.chargePass('p', 'utf8-and-nul-validation');
    ledger.chargePass('p', 'utf8-and-nul-validation');
    const summary = ledger.summary();
    expect(summary.breaches.map((b) => b.limit)).toEqual(['maxSources', 'maxTotalBytes', 'maxParsePassesPerSource']);
    expect(Object.keys(summary.passesByIdentity)).toEqual([...REGISTRY_PASSES]);
    expect(summary).toMatchObject({ bodiesCounted: 0, totalBytes: 0, parsePasses: 1, sourcesTraversed: 1, maxPassesOnOneSource: 1 });
    ledger.chargePass('q', 'phase-a-link-discovery');
    expect(summary.parsePasses).toBe(1);
    expect(ledger.limits).toEqual(limits({ maxTotalBytes: 1, maxParsePassesPerSource: 1 }));
  });
});
