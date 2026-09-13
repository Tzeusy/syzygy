import { describe, expect, it } from 'vitest';
import { BoundedJsonError, parseBoundedJson } from './parse-json.js';

const limits = { maxBytes: 4096, maxNodes: 100, maxDepth: 20 };
const parse = (text: string) => parseBoundedJson(text, limits);

describe('bounded provider JSON parsing', () => {
  it('preserves complete JSON data with safe objects and decoded strings', () => {
    const parsed = parse(' \n{"a":[true,false,null,-0,1.25e2,"\\u00e9\\n\\\""],"b":{}}\t') as Record<string, unknown>;
    expect(Object.getPrototypeOf(parsed)).toBe(null);
    expect(parsed.a).toEqual([true, false, null, -0, 125, 'é\n"']);
    expect(Object.getPrototypeOf(parsed.b)).toBe(null);
    expect(parse('"\\ud800"')).toBe('\ud800');
  });

  it.each(['{"a":1,"a":2}', '{"a":1,"\\u0061":2}', '{"é":1,"\\u00e9":2}',
    '{"x":{"\\u0061":1,"a":2}}'])('rejects duplicate decoded keys: %s', (text) => {
    expect(() => parse(text)).toThrow('duplicate-key');
  });

  it.each(['__proto__', 'prototype', 'constructor', '\\u005f_proto__'])('rejects pollution keys: %s', (key) => {
    expect(() => parse(`{"${key}":{}}`)).toThrow('unsupported-property');
  });

  it.each(['', '```json\n{}\n```', '<html>{}</html>', '{} explanation', '{}{}', '[1,]', '{"x":1,}',
    '{x:1}', '{"x" 1}', '[1 2]', '01', '+1', '.1', '1.', '1e', 'NaN', 'undefined',
    'truefalse', '\u00a0null', '\ufeff{}', '"unterminated', '"\\x20"', '"\\u0x00"', '"raw\nline"',
    '/*comment*/null'])('rejects non-JSON grammar without recovery: %s', (text) => {
    expect(() => parse(text)).toThrow('invalid-json');
  });

  it('rejects nonfinite numbers and documents ordinary binary64 semantics', () => {
    expect(() => parse('1e400')).toThrow('nonfinite-number');
    expect(() => parse('-1e400')).toThrow('nonfinite-number');
    expect(parse('9007199254740993')).toBe(9007199254740992);
    expect(parse('1e-400')).toBe(0);
  });

  it('counts exact UTF-8 input bytes including whitespace and escape spelling', () => {
    expect(parseBoundedJson('"é"', { ...limits, maxBytes: 4 })).toBe('é');
    expect(() => parseBoundedJson('"é"', { ...limits, maxBytes: 3 })).toThrow('byte-limit');
    expect(() => parseBoundedJson('"\\u00e9"', { ...limits, maxBytes: 4 })).toThrow('byte-limit');
    expect(() => parseBoundedJson(' null ', { ...limits, maxBytes: 5 })).toThrow('byte-limit');
  });

  it('bounds value nodes and depth before descending', () => {
    expect(parseBoundedJson('{"a":[0]}', { ...limits, maxNodes: 3, maxDepth: 2 })).toEqual({ a: [0] });
    expect(() => parseBoundedJson('{"a":[0]}', { ...limits, maxNodes: 2 })).toThrow('node-limit');
    expect(() => parseBoundedJson('{"a":[0]}', { ...limits, maxDepth: 1 })).toThrow('depth-limit');
    expect(parseBoundedJson('{}', { ...limits, maxDepth: 0, maxNodes: 1 })).toEqual({});
    expect(() => parse('['.repeat(300) + '0' + ']'.repeat(300))).toThrow('depth-limit');
  });

  it('rejects invalid limits and non-string input without coercion', () => {
    for (const bad of [0, -1, NaN, Infinity, 0.5, Number.MAX_SAFE_INTEGER + 1]) {
      for (const key of ['maxBytes', 'maxNodes']) {
        expect(() => parseBoundedJson('null', { ...limits, [key]: bad })).toThrow('invalid-limits');
      }
    }
    for (const maxDepth of [-1, 257, NaN, Infinity, 0.5]) {
      expect(() => parseBoundedJson('null', { ...limits, maxDepth })).toThrow('invalid-limits');
    }
    let calls = 0;
    const input = { toString() { calls++; return '{}'; } };
    expect(() => parse(input as unknown as string)).toThrow('invalid-input');
    expect(calls).toBe(0);
  });

  it('returns content-free typed diagnostics', () => {
    try { parse('{"private-secret":1,"private-secret":2}'); }
    catch (error) {
      expect(error).toBeInstanceOf(BoundedJsonError);
      expect((error as BoundedJsonError).code).toBe('duplicate-key');
      expect(String(error)).not.toContain('private-secret');
      return;
    }
    throw new Error('Expected rejection');
  });
});
