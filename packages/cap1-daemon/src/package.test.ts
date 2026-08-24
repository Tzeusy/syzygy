import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

import * as daemon from '@syzygy/cap1-daemon';

interface PackageManifest {
  readonly exports?: {
    readonly '.': string | {
      readonly types?: string;
      readonly import?: string;
      readonly default?: string;
    };
  };
}

const manifest = JSON.parse(
  readFileSync(new URL('../package.json', import.meta.url), 'utf8'),
) as PackageManifest;

describe('cap1-daemon package', () => {
  it('is importable with built runtime and declaration entries', () => {
    expect(daemon).toBeDefined();
    expect(manifest.exports?.['.']).toEqual({
      types: './dist/index.d.ts',
      import: './dist/index.js',
      default: './dist/index.js',
    });
  });
});
