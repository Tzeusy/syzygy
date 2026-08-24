// RT6 system test 3 — credential enforcement observed from OUTSIDE the
// process: real HTTP against the spawned daemon. The refusal body is
// the named vocabulary verbatim (hard-coded literal), and the token
// file's mode is checked by the harness's own stat.

import { rmSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  readCredential,
  startDaemon,
  tempBase,
  writeCompleteFixture,
  type DaemonProcess,
} from './harness.js';

const cleanups: (() => Promise<void> | void)[] = [];

afterEach(async () => {
  for (const cleanup of cleanups.splice(0).reverse()) {
    await cleanup();
  }
});

async function startFixtureDaemon(): Promise<DaemonProcess> {
  const base = tempBase('syz-sys-cred-');
  cleanups.push(() => rmSync(base, { recursive: true, force: true }));
  const fixtureRoot = join(base, 'fixture');
  writeCompleteFixture(fixtureRoot);
  const daemon = await startDaemon({ fixtureRoot, stateDir: join(base, 'state') });
  cleanups.push(async () => {
    await daemon.stop();
  });
  return daemon;
}

describe('RT6 — credential enforcement from outside the process', () => {
  it.each([
    ['missing', undefined],
    ['scheme without separator', 'Bearer'],
    ['empty bearer token', 'Bearer '],
    ['wrong scheme', 'Basic x'],
    ['whitespace-only bearer token', 'Bearer    '],
    ['malformed scheme casing', `bearer ${'a'.repeat(64)}`],
    ['wrong-length bearer token', 'Bearer definitely-not-the-minted-token'],
    ['wrong bearer token', `Bearer ${'f'.repeat(64)}`],
  ])('refuses %s credentials with no facts served', async (_case, authorization) => {
    const daemon = await startFixtureDaemon();
    const response = await fetch(`${daemon.baseUrl}/api/project`, {
      ...(authorization === undefined ? {} : { headers: { authorization } }),
    });
    expect(response.status).toBe(401);
    expect(response.headers.get('content-type')).toBe('application/json');
    const body = await response.text();
    expect(body).toBe('{"admitted":false,"served":"nothing"}');
    expect(body).not.toContain('project-evaluated');
  });

  it('the correct token from the state-dir file admits: 200 with the evaluated body', async () => {
    const daemon = await startFixtureDaemon();
    const token = readCredential(daemon.credentialPath);
    const response = await fetch(`${daemon.baseUrl}/api/project`, {
      headers: { authorization: `Bearer ${token}` },
    });
    expect(response.status).toBe(200);
    const body = (await response.json()) as { kind: string };
    expect(body.kind).toBe('project-evaluated');
  });

  it('the token file is owner-only (mode 0600)', async () => {
    const daemon = await startFixtureDaemon();
    const stats = statSync(daemon.credentialPath);
    expect((stats.mode & 0o777).toString(8)).toBe('600');
  });

  it('the credential value is never printed to stdout', async () => {
    const daemon = await startFixtureDaemon();
    const token = readCredential(daemon.credentialPath);
    expect(token.length).toBeGreaterThan(0);
    expect(daemon.stdout()).not.toContain(token);
  });
});
