import { describe, expect, it } from 'vitest';

import { browserRequestAllowed } from './browser-origin.js';

// syzygy-bpyt.7.14: a browser request is allowed with no Origin or with
// exactly the host's own origin. An origin that only begins with it, or
// that it only begins with, names another port or another host.
describe('browserRequestAllowed — the Origin is compared whole', () => {
  it('allows no Origin and the exact origin of each allowed host', () => {
    expect(browserRequestAllowed({ host: '127.0.0.1:7478' })).toBe(true);
    expect(browserRequestAllowed({ host: '127.0.0.1:7478', origin: 'http://127.0.0.1:7478' })).toBe(true);
    expect(browserRequestAllowed({ host: 'localhost:7478', origin: 'http://localhost:7478' })).toBe(true);
    expect(browserRequestAllowed({ host: 'tzeusy.parrot-hen.ts.net', origin: 'https://tzeusy.parrot-hen.ts.net' })).toBe(true);
  });

  it('refuses an origin that only begins with the host origin', () => {
    expect(browserRequestAllowed({ host: '127.0.0.1:7478', origin: 'http://127.0.0.1:74789' })).toBe(false);
    expect(browserRequestAllowed({ host: 'localhost:7478', origin: 'http://localhost:7478.attacker.invalid' })).toBe(false);
    expect(browserRequestAllowed({ host: 'tzeusy.parrot-hen.ts.net', origin: 'https://tzeusy.parrot-hen.ts.net.attacker.invalid' })).toBe(false);
  });

  it('refuses an origin that the host origin only begins with', () => {
    expect(browserRequestAllowed({ host: '127.0.0.1:7478', origin: 'http://127.0.0.1:747' })).toBe(false);
    expect(browserRequestAllowed({ host: '127.0.0.1:7478', origin: 'http://127.0.0.1' })).toBe(false);
    expect(browserRequestAllowed({ host: 'tzeusy.parrot-hen.ts.net', origin: 'https://tzeusy.parrot-hen.ts' })).toBe(false);
  });
});
