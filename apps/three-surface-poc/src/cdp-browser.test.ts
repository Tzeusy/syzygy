import { describe, expect, it } from 'vitest';

import { closeDisposableBrowser, removeBrowserProfile } from './cdp-browser.js';

describe('disposable browser shutdown', () => {
  it('closes an unresponsive protocol socket, kills the child, then removes its profile', async () => {
    const events: string[] = [];
    let onExit: (() => void) | undefined;
    let signalCode: NodeJS.Signals | null = null;
    let requestedTimeout: number | undefined;
    const connection = {
      close: () => { events.push('socket-closed'); },
      send: (_method: string, _params?: unknown, _sessionId?: string, timeoutMs?: number) => {
        events.push('protocol-close-requested');
        requestedTimeout = timeoutMs;
        return new Promise<never>((_resolve, reject) => setTimeout(() => reject(new Error('no acknowledgement')), timeoutMs ?? 0));
      },
    };
    const child: Parameters<typeof closeDisposableBrowser>[1] = {
      exitCode: null,
      get signalCode() { return signalCode; },
      once: (event, listener) => { expect(event).toBe('exit'); onExit = listener; },
      kill: (signal) => {
        events.push(signal);
        queueMicrotask(() => { signalCode = signal; onExit?.(); });
        return true;
      },
    };
    await closeDisposableBrowser(connection, child, '/tmp/private-browser-profile', {
      removeProfile: () => { events.push('profile-removed'); }, closeGraceMs: 5, profileProcesses: () => [],
    });
    expect(requestedTimeout).toBe(5);
    expect(events).toEqual(['protocol-close-requested', 'socket-closed', 'SIGKILL', 'profile-removed']);
  });

  it('lets an acknowledged close exit before removing the profile without a hard kill', async () => {
    const events: string[] = [];
    let onExit: (() => void) | undefined;
    let signalCode: NodeJS.Signals | null = null;
    const child: Parameters<typeof closeDisposableBrowser>[1] = {
      exitCode: null,
      get signalCode() { return signalCode; },
      once: (_event, listener) => { onExit = listener; },
      kill: () => { throw new Error('graceful child must not be killed'); },
    };
    const connection = {
      send: async () => {
        events.push('protocol-close-acknowledged');
        queueMicrotask(() => { signalCode = 'SIGTERM'; onExit?.(); events.push('child-exited'); });
        return {};
      },
      close: () => { events.push('socket-closed'); },
    };
    await closeDisposableBrowser(connection, child, '/tmp/private-browser-profile', {
      removeProfile: () => { events.push('profile-removed'); }, closeGraceMs: 100, profileProcesses: () => [],
    });
    expect(events).toEqual(['protocol-close-acknowledged', 'child-exited', 'socket-closed', 'profile-removed']);
  });

  it('cleans a child whose signal exit was already observed without waiting for a second exit event', async () => {
    const events: string[] = [];
    const child: Parameters<typeof closeDisposableBrowser>[1] = {
      exitCode: null,
      signalCode: 'SIGKILL',
      once: () => { throw new Error('exit already observed'); },
      kill: () => { throw new Error('child already exited'); },
    };
    await closeDisposableBrowser({ close: () => { events.push('socket-closed'); }, send: async () => ({}) }, child,
      '/tmp/private-browser-profile', { removeProfile: () => { events.push('profile-removed'); }, profileProcesses: () => [] });
    expect(events).toEqual(['socket-closed', 'profile-removed']);
  });

  it('waits for exact private profile users before removal and retains the profile on drain timeout', async () => {
    const events: string[] = [];
    const exited: Parameters<typeof closeDisposableBrowser>[1] = {
      exitCode: 0, signalCode: null,
      once: () => { throw new Error('child already exited'); },
      kill: () => { throw new Error('child already exited'); },
    };
    let scans = 0;
    const connection = { close: () => { events.push('socket-closed'); }, send: async () => ({}) };
    await closeDisposableBrowser(connection, exited, '/tmp/private-browser-profile', {
      closeGraceMs: 5, profileDrainMs: 100,
      profileProcesses: () => ++scans === 1 ? [123] : [],
      removeProfile: () => { events.push('profile-removed'); },
    });
    expect(scans).toBe(2);
    expect(events).toEqual(['socket-closed', 'profile-removed']);
    await expect(closeDisposableBrowser(connection, exited, '/tmp/private-browser-profile', {
      closeGraceMs: 5, profileDrainMs: 1,
      profileProcesses: () => [123],
      removeProfile: () => { events.push('wrong-removal'); },
    })).rejects.toThrow('private browser profile still held');
    expect(events).not.toContain('wrong-removal');
  });
});

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
