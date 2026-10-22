import { types } from 'node:util';
import { SOURCE_ID_MAX_LENGTH, SOURCE_ID_MIN_LENGTH, SOURCE_ID_PATTERN } from './source-model.js';

// One closed-schema checker and one handle, shared by the dossier draft model
// (draft-model.ts), the provider stage schemas (provider-draft.ts) and the
// rendered-design review (rendered-design.ts). A schema here admits plain
// strings only: markup-looking text stays inert, and renderers must escape it.
export type Schema = { type: 'object'; properties: Record<string, Schema>; required: string[]; additionalProperties: false }
  | { type: 'array'; items: Schema; minItems: number; maxItems: number; uniqueItems?: boolean }
  | { type: 'string'; minLength: number; maxLength: number; pattern?: string; enum?: string[] }
  | { type: 'boolean' }
  | { type: 'number'; minimum: number; maximum: number }
  | { oneOf: readonly Schema[] };

// The string parts declare their arm: importers spread an `enum` into them, and an imported const keeps its declared type.
export const text: Extract<Schema, { type: 'string' }> = { type: 'string', minLength: 1, maxLength: 8000 };
export const handle: Extract<Schema, { type: 'string' }> = { type: 'string', minLength: SOURCE_ID_MIN_LENGTH, maxLength: SOURCE_ID_MAX_LENGTH, pattern: SOURCE_ID_PATTERN };
export const list = (items: Schema, minItems = 0, maxItems = 200): Extract<Schema, { type: 'array' }> => ({ type: 'array', items, minItems, maxItems });
export const object = (properties: Record<string, Schema>): Schema => ({ type: 'object', properties, required: Object.keys(properties), additionalProperties: false });
export const refs: Schema = { ...list(handle, 1), uniqueItems: true };

export function check(schema: Schema, value: unknown): void {
  if ('oneOf' in schema) {
    for (const candidate of schema.oneOf) {
      try { check(candidate, value); return; } catch { /* try next closed arm */ }
    }
    throw new Error('invalid-disposition');
  }
  if (schema.type === 'string') {
    if (typeof value !== 'string' || [...value].length < schema.minLength || [...value].length > schema.maxLength
      || (schema.pattern && !new RegExp(schema.pattern, 'u').test(value))
      || (schema.enum && !schema.enum.includes(value))) throw new Error('invalid-string');
    return;
  }
  if (schema.type === 'boolean') {
    if (typeof value !== 'boolean') throw new Error('invalid-boolean');
    return;
  }
  if (schema.type === 'number') {
    // Written as an inclusion so NaN, which fails every comparison, is refused with the infinities.
    if (typeof value !== 'number' || !(value >= schema.minimum && value <= schema.maximum)) throw new Error('invalid-number');
    return;
  }
  if (typeof value !== 'object' || value === null || types.isProxy(value)) throw new Error('invalid-structure');
  const descriptors = Object.getOwnPropertyDescriptors(value);
  if (Reflect.ownKeys(descriptors).some(key => typeof key !== 'string' || !('value' in descriptors[key]!))) throw new Error('invalid-property');
  if (schema.type === 'array') {
    if (!Array.isArray(value) || value.length < schema.minItems || value.length > schema.maxItems
      || Object.keys(descriptors).length !== value.length + 1) throw new Error('invalid-array');
    for (let i = 0; i < value.length; i++) {
      if (!Object.hasOwn(descriptors, String(i))) throw new Error('invalid-array');
      check(schema.items, descriptors[String(i)]!.value);
    }
    if (schema.uniqueItems && new Set(value).size !== value.length) throw new Error('duplicate-reference');
    return;
  }
  if (Object.getPrototypeOf(value) !== Object.prototype && Object.getPrototypeOf(value) !== null) throw new Error('invalid-object');
  const keys = Object.keys(descriptors);
  if (keys.length !== schema.required.length || schema.required.some(key => !Object.hasOwn(descriptors, key))
    || keys.some(key => !Object.hasOwn(schema.properties, key) || !descriptors[key]!.enumerable)) throw new Error('invalid-fields');
  for (const key of keys) check(schema.properties[key]!, descriptors[key]!.value);
}
