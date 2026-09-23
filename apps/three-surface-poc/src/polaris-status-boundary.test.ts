import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';

const CLAUSE = 'The current operator path calls no real model or provider.';

describe('Polaris generator operator/status boundary', () => {
  it.each([
    'docs/polaris-generation/README.md',
    'PROJECT-STATUS.md',
  ])('%s retains the exact no-model-called clause once', file => {
    const text = readFileSync(join(process.cwd(), file), 'utf8').replace(/\s+/g, ' ');
    expect(text.split(CLAUSE).length - 1).toBe(1);
  });
});
