import type { DispatchPermit } from '@syzygy/polaris-generation-core';

/** Accounting policy `dossier-units-v1`: one unit is 1,000 tokens (input, cache-creation, cache-read and output
 * summed), rounded up per attempt. A reply whose usage is unknown or malformed counts at the full ceiling its permit
 * allowed, never at zero. */
export const DOSSIER_UNITS_POLICY = 'dossier-units-v1';
export const TOKENS_PER_UNIT = 1000;
/** The output cap of one attempt when the profile sets none (tokens). */
export const MAX_OUTPUT_TOKENS = 64_000;

export const unitsForTokens = (tokens: number): number => Math.ceil(tokens / TOKENS_PER_UNIT);

/** Tokens never outnumber bytes, so a request of `requestBytes` bytes (system plus input) is at most that many input
 * tokens. The smallest ceiling that leaves room for one output token. */
export const minimumUsageUnits = (requestBytes: number): number => {
  if (!Number.isSafeInteger(requestBytes) || requestBytes < 0) throw new RangeError('minimumUsageUnits: bytes must be a non-negative safe integer');
  return Math.ceil((requestBytes + 1) / TOKENS_PER_UNIT);
};

/** `max_tokens` for one attempt, so that input plus output cannot exceed the permit's unit ceiling; null when no room is left. */
export function outputTokenCap(permit: Pick<DispatchPermit, 'maxUsageUnits' | 'maxOutputBytes'>, system: string, input: string, configured: number): number | null {
  const requestBytes = Buffer.byteLength(system, 'utf8') + Buffer.byteLength(input, 'utf8');
  const room = permit.maxUsageUnits * TOKENS_PER_UNIT - requestBytes;
  const cap = Math.min(permit.maxOutputBytes, MAX_OUTPUT_TOKENS, configured, room);
  return Number.isSafeInteger(cap) && cap >= 1 ? cap : null;
}

/** Units for one usage object; null when any part is missing or malformed. */
export function tokenUnits(parts: readonly unknown[]): number | null {
  if (!parts.every(p => typeof p === 'number' && Number.isSafeInteger(p) && p >= 0)) return null;
  return unitsForTokens((parts as number[]).reduce((a, b) => a + b, 0));
}

/** What a call counts as: its known units, or the full ceiling when any try's billing is unknown. */
export const countedUnits = (known: number | null, permit: Pick<DispatchPermit, 'maxUsageUnits'>): number => known ?? permit.maxUsageUnits;
