import { describe, expect, it, vi } from 'vitest';

import { launchAfterPwbRepositoryBinding } from './launcher.js';

describe('executable POC launcher repository boundary', () => {
  it('a wrong locator reaches neither repository observation nor body reads', async () => {
    const observeRepository = vi.fn();
    const readBody = vi.fn();

    const result = await launchAfterPwbRepositoryBinding(
      '/other/butlers',
      () => ({ kind: 'rejected', reason: 'locator-mismatched' }),
      async () => {
        observeRepository();
        readBody();
      },
    );

    expect(result).toEqual({ kind: 'rejected', reason: 'locator-mismatched' });
    expect(observeRepository).not.toHaveBeenCalled();
    expect(readBody).not.toHaveBeenCalled();
  });
});
