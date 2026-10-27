// The generation mutation plan itself: every literal fragment occurs exactly
// once in its current source, so a source edit that moves a guarded fragment
// fails here, on the PR that makes it, rather than in the scheduled
// generation-mutation gate. The runner stops at the first missing fragment;
// syzygy-kpbq found the gate red for 23 runs after 5955f8c0 split the
// repair-cycle cap, with a second fragment (moved by 69995614) behind it.

import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

import { GENERATION_LITERAL_MUTATIONS, applyLiteralMutation } from './generation-mutation.js';

const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
const read = (file: string): string => readFileSync(join(REPO_ROOT, file), 'utf8');

describe('generation mutation plan', () => {
  it('every literal mutation fragment occurs exactly once in its current source and names a must-fail test', () => {
    expect(GENERATION_LITERAL_MUTATIONS.length).toBe(12);
    for (const mutation of GENERATION_LITERAL_MUTATIONS) {
      const source = read(mutation.file);
      expect(source.split(mutation.from).length - 1, mutation.id).toBe(1);
      expect(applyLiteralMutation(source, mutation)).not.toBe(source);
      expect(mutation.mustFail.length).toBeGreaterThan(0);
    }
    expect(new Set(GENERATION_LITERAL_MUTATIONS.map((mutation) => mutation.id)).size).toBe(GENERATION_LITERAL_MUTATIONS.length);
  });
});
