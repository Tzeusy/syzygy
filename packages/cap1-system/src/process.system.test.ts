// RT6 system test 5 — process reality: the daemon is a real child
// process that serves while alive, exits 0 on SIGINT, and leaves the
// port refusing connections afterward. Observed entirely from outside.

import { rmSync } from 'node:fs';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { startDaemon, tempBase, writeCompleteFixture } from './harness.js';

const cleanups: (() => Promise<void> | void)[] = [];

afterEach(async () => {
  for (const cleanup of cleanups.splice(0).reverse()) {
    await cleanup();
  }
});

describe('RT6 — process reality', () => {
  it('SIGINT exits 0 and the port then refuses connections', async () => {
    const base = tempBase('syz-sys-proc-');
    cleanups.push(() => rmSync(base, { recursive: true, force: true }));
    const fixtureRoot = join(base, 'fixture');
    writeCompleteFixture(fixtureRoot);

    const daemon = await startDaemon({ fixtureRoot, stateDir: join(base, 'state') });

    // Alive: the port answers.
    expect((await fetch(`${daemon.baseUrl}/`)).status).toBe(200);

    // SIGINT: clean shutdown, exit code 0, announced on stdout.
    const exitCode = await daemon.stop();
    expect(exitCode).toBe(0);
    expect(daemon.stdout()).toContain('SIGINT received, shutting down');

    // Dead: the same port now refuses connections — the connection
    // error itself is the assertion.
    await expect(fetch(`${daemon.baseUrl}/`)).rejects.toThrow();
  });
});
