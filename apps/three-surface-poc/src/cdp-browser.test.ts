import { describe, expect, it } from 'vitest';

import { removeBrowserProfile } from './cdp-browser.js';

describe('browser profile cleanup', () => {
  it('retries transient ENOTEMPTY failures and succeeds within the bound', () => {
    let attempts = 0;
    removeBrowserProfile('/tmp/syzygy-browser-profile', {
      remove: () => {
        attempts += 1;
        if (attempts < 3) throw Object.assign(new Error('profile still changing'), { code: 'ENOTEMPTY' });
      },
    });
    expect(attempts).toBe(3);
  });

  it('does not retry a permanent profile cleanup failure', () => {
    let attempts = 0;
    expect(() => removeBrowserProfile('/tmp/syzygy-browser-profile', {
      maxAttempts: 2,
      remove: () => {
        attempts += 1;
        throw Object.assign(new Error('profile permission denied'), { code: 'EACCES' });
      },
    })).toThrow('profile permission denied');
    expect(attempts).toBe(1);
  });

  it('preserves a retryable failure at the exact total-call bound', () => {
    let attempts = 0;
    const failure = Object.assign(new Error('profile remains busy'), { code: 'ENOTEMPTY' });
    expect(() => removeBrowserProfile('/tmp/syzygy-browser-profile', {
      maxAttempts: 2,
      remove: () => {
        attempts += 1;
        throw failure;
      },
    })).toThrow(failure);
    expect(attempts).toBe(2);
  });

  it('stays bounded across repeated transient profile cleanup races', () => {
    const runs = 128;
    let totalAttempts = 0;
    for (let run = 0; run < runs; run += 1) {
      const transientFailures = run % 4;
      let attempts = 0;
      removeBrowserProfile(`/tmp/syzygy-browser-profile-${run}`, {
        remove: () => {
          attempts += 1;
          totalAttempts += 1;
          if (attempts <= transientFailures) throw Object.assign(new Error('profile still changing'), { code: 'ENOTEMPTY' });
        },
      });
      expect(attempts).toBe(transientFailures + 1);
    }
    expect(totalAttempts).toBe(320);
  });
});
