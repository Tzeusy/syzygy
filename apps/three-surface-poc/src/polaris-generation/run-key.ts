import { createHmac, randomBytes } from 'node:crypto';

/** A fresh 32-byte key for one run. It keys excluded-source ids only and is
 * never serialised or logged, so those ids cannot be confirmed from a path list
 * and differ between runs. */
export const newGenerationRunKey = (): Buffer => randomBytes(32);

/** HMAC-SHA256 of an identity input under the run key, as lowercase hex. */
export const keyedDigest = (runKey: Buffer, input: string): string => createHmac('sha256', runKey).update(input).digest('hex');

/** `s-` plus 24 hex digits of the keyed digest: stable within a key, opaque across keys. */
export const excludedSourceId = (runKey: Buffer, input: string): string => `s-${keyedDigest(runKey, input).slice(0, 24)}`;
