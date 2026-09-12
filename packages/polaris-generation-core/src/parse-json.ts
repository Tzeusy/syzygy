import type { CanonicalJsonLimits } from './canonical-json.js';

export type BoundedJsonFailure =
  | 'invalid-limits' | 'invalid-input' | 'invalid-json' | 'duplicate-key'
  | 'unsupported-property' | 'nonfinite-number' | 'byte-limit' | 'node-limit' | 'depth-limit';

/** Diagnostics contain neither provider content nor property names. */
export class BoundedJsonError extends Error {
  constructor(readonly code: BoundedJsonFailure) {
    super(`Bounded JSON rejected: ${code}`);
    this.name = 'BoundedJsonError';
  }
}

/**
 * Parses one complete JSON value; markdown fences and surrounding prose fail.
 * Numbers use ECMAScript JSON number semantics (including binary64 rounding),
 * but overflow to infinity fails. Schema validation must constrain numeric IDs.
 * Root depth is zero; nodes count values, not object keys, as in the encoder.
 */
export function parseBoundedJson(text: string, limits: CanonicalJsonLimits): unknown {
  const reject = (code: BoundedJsonFailure): never => { throw new BoundedJsonError(code); };
  if (!limits || ![limits.maxBytes, limits.maxNodes].every((n) => Number.isSafeInteger(n) && n > 0)
    || !Number.isSafeInteger(limits.maxDepth) || limits.maxDepth < 0 || limits.maxDepth > 256) {
    reject('invalid-limits');
  }
  if (typeof text !== 'string') reject('invalid-input');
  if (text.length > limits.maxBytes || Buffer.byteLength(text, 'utf8') > limits.maxBytes) reject('byte-limit');
  let cursor = 0;
  let nodes = 0;
  const whitespace = (): void => {
    while (text[cursor] === ' ' || text[cursor] === '\t' || text[cursor] === '\r' || text[cursor] === '\n') cursor++;
  };
  const string = (): string => {
    const start = cursor++;
    while (cursor < text.length) {
      const character = text[cursor++]!;
      if (character === '"') {
        try { return JSON.parse(text.slice(start, cursor)) as string; }
        catch { return reject('invalid-json'); }
      }
      if (character.charCodeAt(0) < 32) reject('invalid-json');
      if (character === '\\') {
        const escape = text[cursor++];
        if (escape === 'u') {
          if (!/^[0-9a-fA-F]{4}$/.test(text.slice(cursor, cursor + 4))) reject('invalid-json');
          cursor += 4;
        } else if (escape === undefined || !'"\\/bfnrt'.includes(escape)) reject('invalid-json');
      }
    }
    return reject('invalid-json');
  };
  const number = /-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/y;
  const value = (depth: number): unknown => {
    if (depth > limits.maxDepth) reject('depth-limit');
    if (++nodes > limits.maxNodes) reject('node-limit');
    whitespace();
    const character = text[cursor];
    if (character === '"') return string();
    if (character === '[' || character === '{') {
      const array = character === '[';
      const close = array ? ']' : '}';
      const items: unknown[] = [];
      const object: Record<string, unknown> = Object.create(null) as Record<string, unknown>;
      cursor++;
      whitespace();
      if (text[cursor] === close) { cursor++; return array ? items : object; }
      while (true) {
        if (array) items.push(value(depth + 1));
        else {
          if (text[cursor] !== '"') reject('invalid-json');
          const key = string();
          if (['__proto__', 'prototype', 'constructor'].includes(key)) reject('unsupported-property');
          if (Object.hasOwn(object, key)) reject('duplicate-key');
          whitespace();
          if (text[cursor++] !== ':') reject('invalid-json');
          object[key] = value(depth + 1);
        }
        whitespace();
        if (text[cursor] === close) { cursor++; return array ? items : object; }
        if (text[cursor++] !== ',') reject('invalid-json');
        whitespace();
      }
    }
    for (const [literal, primitive] of [['true', true], ['false', false], ['null', null]] as const) {
      if (text.startsWith(literal, cursor)) { cursor += literal.length; return primitive; }
    }
    number.lastIndex = cursor;
    const match = number.exec(text);
    if (!match) return reject('invalid-json');
    cursor = number.lastIndex;
    const parsed = Number(match[0]);
    if (!Number.isFinite(parsed)) reject('nonfinite-number');
    return parsed;
  };
  const parsed = value(0);
  whitespace();
  if (cursor !== text.length) reject('invalid-json');
  return parsed;
}
