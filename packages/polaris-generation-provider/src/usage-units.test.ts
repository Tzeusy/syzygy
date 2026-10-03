import { describe, expect, it } from 'vitest';
import { DOSSIER_UNITS_POLICY, MAX_OUTPUT_TOKENS, TOKENS_PER_UNIT, countedUnits, minimumUsageUnits, outputTokenCap, tokenUnits, unitsForTokens } from './usage-units.js';

describe('dossier-units-v1', () => {
  it('names itself and fixes the unit at 1,000 tokens', () => {
    expect(DOSSIER_UNITS_POLICY).toBe('dossier-units-v1');
    expect(TOKENS_PER_UNIT).toBe(1000);
    expect(MAX_OUTPUT_TOKENS).toBe(64_000);
  });

  it('rounds each attempt up, so nothing is ever counted below the spend', () => {
    expect([0, 1, 999, 1000, 1001, 2500, 64_000].map(unitsForTokens)).toEqual([0, 1, 1, 1, 2, 3, 64]);
    expect(tokenUnits([400, 600, 0, 0])).toBe(1);
    expect(tokenUnits([400, 601, 0, 0])).toBe(2);
    expect(tokenUnits([1, 0, 999, 0])).toBe(1);
    expect(tokenUnits([1, 0, 1000, 0])).toBe(2);
  });

  it('reads a missing or malformed part as unknown, never as zero', () => {
    for (const parts of [[undefined, 1, 0, 0], [1, null, 0, 0], [1.5, 1, 0, 0], [-1, 1, 0, 0], ['3', 1, 0, 0], [Number.NaN, 1, 0, 0], [Number.MAX_SAFE_INTEGER + 1, 1, 0, 0]]) expect(tokenUnits(parts)).toBeNull();
  });

  it('counts an unknown at the full ceiling and a known value as it is', () => {
    expect(countedUnits(null, { maxUsageUnits: 40 })).toBe(40);
    expect(countedUnits(0, { maxUsageUnits: 40 })).toBe(0);
    expect(countedUnits(7, { maxUsageUnits: 40 })).toBe(7);
  });

  it('minimumUsageUnits leaves room for exactly one output token', () => {
    expect(minimumUsageUnits(0)).toBe(1);
    expect(minimumUsageUnits(998)).toBe(1);
    expect(minimumUsageUnits(999)).toBe(1);      // 999 input + 1 output = 1,000
    expect(minimumUsageUnits(1000)).toBe(2);
    expect(minimumUsageUnits(2_999_999)).toBe(3000);
    for (const bad of [-1, 1.5, Number.NaN, Number.POSITIVE_INFINITY]) expect(() => minimumUsageUnits(bad)).toThrow(RangeError);
  });

  it('caps output so input plus output cannot pass the unit ceiling', () => {
    const permit = { maxUsageUnits: 10, maxOutputBytes: 1_000_000 };
    const system = 'x'.repeat(100), input = 'y'.repeat(900);
    expect(outputTokenCap(permit, system, input, 64_000)).toBe(10_000 - 1000);
    expect(outputTokenCap({ maxUsageUnits: 100, maxOutputBytes: 1_000_000 }, system, input, 64_000)).toBe(64_000);
    expect(outputTokenCap({ maxUsageUnits: 100, maxOutputBytes: 321 }, system, input, 64_000)).toBe(321);
    expect(outputTokenCap({ maxUsageUnits: 100, maxOutputBytes: 1_000_000 }, system, input, 500)).toBe(500);
    // bytes, not characters: a two-byte letter counts twice
    expect(outputTokenCap({ maxUsageUnits: 1, maxOutputBytes: 1_000_000 }, 'é'.repeat(100), 'é'.repeat(300), 64_000)).toBe(1000 - 800);
  });

  it('refuses when no output token fits', () => {
    expect(outputTokenCap({ maxUsageUnits: 1, maxOutputBytes: 1_000_000 }, 'x'.repeat(500), 'y'.repeat(500), 64_000)).toBeNull();   // room 0
    expect(outputTokenCap({ maxUsageUnits: 1, maxOutputBytes: 1_000_000 }, 'x'.repeat(500), 'y'.repeat(499), 64_000)).toBe(1);
    expect(outputTokenCap({ maxUsageUnits: 1, maxOutputBytes: 1_000_000 }, 'x'.repeat(2000), '', 64_000)).toBeNull();
    expect(outputTokenCap({ maxUsageUnits: 5, maxOutputBytes: 0 }, 'x', 'y', 64_000)).toBeNull();
  });

  it('minimumUsageUnits and outputTokenCap agree on the edge', () => {
    for (const bytes of [0, 1, 998, 999, 1000, 1999, 2000, 123_456]) {
      const units = minimumUsageUnits(bytes);
      expect(outputTokenCap({ maxUsageUnits: units, maxOutputBytes: 1_000_000 }, 'x'.repeat(bytes), '', 64_000), `at ${units}`).not.toBeNull();
      if (units > 1) expect(outputTokenCap({ maxUsageUnits: units - 1, maxOutputBytes: 1_000_000 }, 'x'.repeat(bytes), '', 64_000), `below ${units}`).toBeNull();
    }
  });
});
