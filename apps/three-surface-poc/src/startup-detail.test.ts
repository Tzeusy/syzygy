import { describe, expect, it } from 'vitest';

import { daemonStartDetail, gitObservationDetail, unexpectedObservationDetail } from './startup-detail.js';

describe('startup diagnostics', () => {
  it('retains named credential and duplicate-route causes without echoing arbitrary detail', () => {
    expect(daemonStartDetail({ kind: 'credential-unprovisionable', detail: 'existing credential file is unreadable: /private/credential-secret' }))
      .toBe('existing credential file is unreadable');
    expect(daemonStartDetail({ kind: 'duplicate-route', detail: 'two routes registered for `GET /polaris`' }))
      .toBe('two routes registered for `GET /polaris`');
    expect(daemonStartDetail({ kind: 'duplicate-route', detail: 'two routes registered for `GET /credential-secret`?token=secret' }))
      .toBe('duplicate registered route (detail unavailable)');
  });

  it('retains safe bind and git failure codes and names unexpected observation classes', () => {
    expect(daemonStartDetail({ kind: 'bind-failed', detail: 'listen EADDRINUSE: address already in use 127.0.0.1:7478' }))
      .toBe('bind failed (EADDRINUSE)');
    expect(daemonStartDetail({ kind: 'bind-failed', detail: 'private path /credential-secret' }))
      .toBe('bind failed (detail unavailable)');
    expect(gitObservationDetail(Object.assign(new Error('private path /credential-secret'), { status: 128 })))
      .toBe('a required git revision could not be observed (git exit 128)');
    expect(gitObservationDetail(new Error('observer-checkout-dirty'))).toBe('POC runtime inputs have uncommitted changes');
    expect(unexpectedObservationDetail(new TypeError('credential-secret'))).toBe('unexpected observation failure (TypeError)');
  });
});
