import { describe, expect, it } from 'vitest';
import { CanonicalJsonError, digestCanonicalJson, encodeCanonicalJson } from './canonical-json.js';

const limits = { maxBytes: 4096, maxNodes: 100, maxDepth: 20 };
const encode = (value: unknown) => encodeCanonicalJson(value, limits);

describe('canonical JSON record bytes', () => {
  it('binds sorted object keys but preserves list order, Unicode and primitive spelling', () => {
    const first = { z: [true, null, -0, 'é\n'], a: { y: 2, x: 1 } };
    const second = { a: { x: 1, y: 2 }, z: [true, null, 0, 'é\n'] };
    expect(encode(first)).toBe('{"a":{"x":1,"y":2},"z":[true,null,0,"é\\n"]}');
    expect(digestCanonicalJson(first, limits)).toEqual(digestCanonicalJson(second, limits));
    expect(digestCanonicalJson([1, 2], limits)).not.toEqual(digestCanonicalJson([2, 1], limits));
    expect(encode('é')).not.toBe(encode('e\u0301'));
  });

  it('uses exact SHA-256 UTF-8 bytes and declares the encoding', () => {
    expect(digestCanonicalJson({}, limits)).toEqual({
      encoding: 'polaris-json-v1', algorithm: 'sha256',
      digest: '44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a',
    });
    expect(encode('\ud800')).toBe('"\\ud800"');
  });

  it.each([undefined, NaN, Infinity, -Infinity, 1n, Symbol('x'), () => 1])(
    'rejects non-JSON primitives without silent omission', (value) => {
      expect(() => encode(value)).toThrow(CanonicalJsonError);
      expect(() => encode({ nested: value })).toThrow(CanonicalJsonError);
    },
  );

  it('accepts shared data but rejects cyclic data', () => {
    const shared = { x: 1 };
    expect(encode([shared, shared])).toBe('[{"x":1},{"x":1}]');
    const cycle: unknown[] = [];
    cycle.push(cycle);
    expect(() => encode(cycle)).toThrow('cycle');
  });

  it('refuses custom objects, accessors and proxies without running their hooks', () => {
    let calls = 0;
    const accessor = Object.defineProperty({}, 'secret', { enumerable: true, get() { calls++; return 'secret'; } });
    const proxy = new Proxy({}, { ownKeys() { calls++; return []; } });
    for (const value of [new Date(), new Map(), Object.create({}), accessor, proxy,
      { toJSON() { calls++; return {}; } }]) {
      expect(() => encode(value)).toThrow(CanonicalJsonError);
    }
    expect(calls).toBe(0);
  });

  it('rejects hidden, symbol and pollution keys rather than erasing them', () => {
    const hidden = Object.defineProperty({}, 'secret', { value: 1 });
    for (const value of [hidden, { [Symbol()]: 1 }, JSON.parse('{"__proto__":{}}'),
      { constructor: 'x' }, { prototype: 'x' }]) {
      expect(() => encode(value)).toThrow('unsupported-property');
    }
    expect(encode(Object.assign(Object.create(null), { a: 1 }))).toBe('{"a":1}');
  });

  it('rejects sparse arrays and extra array properties', () => {
    const extra = Object.assign([1], { extra: true });
    for (const value of [Array(2), extra, Object.assign([1], { [Symbol()]: true })]) {
      expect(() => encode(value)).toThrow('unsupported-property');
    }
  });

  it('enforces byte, node and depth bounds exactly without truncation', () => {
    expect(encodeCanonicalJson('é', { ...limits, maxBytes: 4 })).toBe('"é"');
    expect(() => encodeCanonicalJson('é', { ...limits, maxBytes: 3 })).toThrow('byte-limit');
    expect(encodeCanonicalJson([1], { ...limits, maxNodes: 2, maxDepth: 1 })).toBe('[1]');
    expect(() => encodeCanonicalJson([1], { ...limits, maxNodes: 1 })).toThrow('node-limit');
    expect(() => encodeCanonicalJson([1], { ...limits, maxDepth: 0 })).toThrow('depth-limit');
    expect(() => encodeCanonicalJson({ long: 1 }, { ...limits, maxBytes: 5 })).toThrow('byte-limit');
  });

  it('rejects unlimited, fractional and unsupported bound policies', () => {
    for (const value of [0, -1, Infinity, NaN, 0.5, Number.MAX_SAFE_INTEGER + 1]) {
      expect(() => encodeCanonicalJson(null, { ...limits, maxBytes: value })).toThrow('invalid-limits');
      expect(() => encodeCanonicalJson(null, { ...limits, maxNodes: value })).toThrow('invalid-limits');
    }
    expect(() => encodeCanonicalJson(null, { ...limits, maxDepth: 257 })).toThrow('invalid-limits');
  });
});
