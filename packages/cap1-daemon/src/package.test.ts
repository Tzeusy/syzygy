import { describe, expect, it } from 'vitest';

import * as daemon from './index.js';

describe('cap1-daemon package', () => {
  it('is importable', () => {
    expect(daemon).toBeDefined();
  });
});
