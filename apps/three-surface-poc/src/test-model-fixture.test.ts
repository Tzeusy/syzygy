import { existsSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import type { PocModel } from '@syzygy/three-surface-poc-core';

import { frozenFixture, sharedFixtureModels } from './test-model-fixture.js';

describe('shared fixture models (syzygy-k66p)', () => {
  it('freezes every nested object and array, so a test that writes to a shared model throws', () => {
    const value = frozenFixture({ shape: { items: [{ state: 'observed' }] }, bytes: new Uint8Array([1, 2]) });
    expect(() => { (value.shape.items[0] as { state: string }).state = 'unknown'; }).toThrow(TypeError);
    expect(() => { (value.shape.items as { state: string }[]).push({ state: 'extra' }); }).toThrow(TypeError);
    expect(() => { (value as { shape: unknown }).shape = {}; }).toThrow(TypeError);
    expect(value.shape.items[0]?.state).toBe('observed');
    expect(Object.isFrozen(value.bytes)).toBe(false);
  });

  it('builds once, refuses a read before prepare, and removes its repositories', () => {
    let builds = 0;
    let directory = '';
    const shared = sharedFixtureModels<'only'>((cleanups) => {
      builds += 1;
      directory = mkdtempSync(join(tmpdir(), 'syzygy-k66p-shared-'));
      cleanups.push(directory);
      return { only: { marker: builds } as unknown as PocModel };
    });
    expect(() => shared.get('only')).toThrow('shared fixture models used before prepare');
    shared.prepare();
    shared.prepare();
    expect(builds).toBe(1);
    expect(shared.get('only')).toBe(shared.get('only'));
    expect(Object.isFrozen(shared.get('only'))).toBe(true);
    expect(existsSync(directory)).toBe(true);
    shared.remove();
    expect(existsSync(directory)).toBe(false);
    expect(() => shared.get('only')).toThrow('shared fixture models used before prepare');
  });
});
