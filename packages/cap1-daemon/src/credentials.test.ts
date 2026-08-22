import { mkdtempSync, readFileSync, rmSync, statSync, symlinkSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  authorizeStateWrite,
  credentialFromAuthorizationHeader,
  ensureCredential,
  verifyCredential,
  CREDENTIAL_FILE_NAME,
} from './credentials.js';

// RT3 — credential lifecycle tests. Real temp dirs, real files; no
// mocks. Refusal expectations are HARD-CODED literals (oracle
// independence): the named refusal is `{ admitted: false, served:
// 'nothing' }` — the spelling comes from the adopted admission
// vocabulary, not from importing the implementation's constant.

const cleanups: string[] = [];

function tempDir(): string {
  const dir = mkdtempSync(join(tmpdir(), 'rt3-cred-'));
  cleanups.push(dir);
  return dir;
}

afterEach(() => {
  for (const dir of cleanups.splice(0)) {
    rmSync(dir, { recursive: true, force: true });
  }
});

describe('RT3 — credential provisioning', () => {
  it('first start mints a random token, persisted with mode 0600', () => {
    const stateDir = join(tempDir(), 'state');
    const provision = ensureCredential(stateDir);

    expect(provision.kind).toBe('minted');
    if (provision.kind !== 'minted') return;
    expect(provision.path).toBe(join(stateDir, 'machine-credential.token'));
    expect(provision.token).toMatch(/^[0-9a-f]{64}$/);

    const mode = statSync(provision.path).mode & 0o777;
    expect(mode).toBe(0o600);
    expect(readFileSync(provision.path, 'utf8')).toBe(provision.token);
  });

  it('restart reuses the persisted token unchanged', () => {
    const stateDir = join(tempDir(), 'state');
    const first = ensureCredential(stateDir);
    const second = ensureCredential(stateDir);

    expect(first.kind).toBe('minted');
    expect(second.kind).toBe('reused');
    if (first.kind === 'unprovisionable' || second.kind === 'unprovisionable') return;
    expect(second.token).toBe(first.token);
    expect(second.path).toBe(first.path);
  });

  it('an existing empty credential file is a named failure, never a silent re-mint', () => {
    const stateDir = tempDir();
    writeFileSync(join(stateDir, CREDENTIAL_FILE_NAME), '', 'utf8');

    const provision = ensureCredential(stateDir);
    expect(provision.kind).toBe('unprovisionable');
    if (provision.kind !== 'unprovisionable') return;
    expect(provision.detail).toContain('empty');
  });

  it('two distinct state dirs mint distinct tokens', () => {
    const a = ensureCredential(join(tempDir(), 'a'));
    const b = ensureCredential(join(tempDir(), 'b'));
    if (a.kind === 'unprovisionable' || b.kind === 'unprovisionable') {
      throw new Error('expected both provisions to succeed');
    }
    expect(a.token).not.toBe(b.token);
  });
});

describe('RT3 — state-write boundary', () => {
  it('authorizes a plain file name inside the state dir', () => {
    const stateDir = tempDir();
    const decision = authorizeStateWrite(stateDir, 'daemon.state');
    expect(decision.authorized).toBe(true);
    if (decision.authorized) {
      expect(decision.absolutePath).toBe(join(stateDir, 'daemon.state'));
    }
  });

  it('refuses traversal out of the state dir, named', () => {
    const decision = authorizeStateWrite(tempDir(), '../escape.txt');
    expect(decision.authorized).toBe(false);
    if (!decision.authorized) {
      expect(decision.refusedBy).toBe('traversal');
    }
  });

  it('refuses empty and self-naming candidates, named', () => {
    const stateDir = tempDir();
    for (const candidate of ['', '.', '  ']) {
      const decision = authorizeStateWrite(stateDir, candidate);
      expect(decision.authorized).toBe(false);
      if (!decision.authorized) {
        expect(decision.refusedBy).toBe('degenerate-input');
      }
    }
  });

  it('refuses a symlink escape, named', () => {
    const base = tempDir();
    const stateDir = join(base, 'state');
    const outside = join(base, 'outside');
    mkdirSync(stateDir, { recursive: true });
    mkdirSync(outside, { recursive: true });
    symlinkSync(outside, join(stateDir, 'link'));

    const decision = authorizeStateWrite(stateDir, 'link/escape.txt');
    expect(decision.authorized).toBe(false);
    if (!decision.authorized) {
      expect(decision.refusedBy).toBe('symlink-escape');
    }
  });
});

describe('RT3 — credential verification through core admission', () => {
  const TOKEN = 'a'.repeat(64);

  it('a correct bearer header is admitted as a machine client', () => {
    const credential = credentialFromAuthorizationHeader(`Bearer ${TOKEN}`);
    const result = verifyCredential(TOKEN, credential);
    expect(result).toEqual({ admitted: true, clientClass: 'machine' });
  });

  it('a wrong token refuses with the named vocabulary, never a bare string', () => {
    const credential = credentialFromAuthorizationHeader(`Bearer ${'b'.repeat(64)}`);
    const result = verifyCredential(TOKEN, credential);
    expect(result).toEqual({ admitted: false, served: 'nothing' });
  });

  it('a missing header is a non-presented credential and refuses, named', () => {
    const credential = credentialFromAuthorizationHeader(undefined);
    expect(credential).toEqual({ presented: false });
    expect(verifyCredential(TOKEN, credential)).toEqual({
      admitted: false,
      served: 'nothing',
    });
  });

  it('non-Bearer and empty-token headers refuse, named', () => {
    for (const header of ['Basic dXNlcg==', 'Bearer', 'Bearer ', `bearer ${TOKEN}`, TOKEN]) {
      const credential = credentialFromAuthorizationHeader(header);
      expect(verifyCredential(TOKEN, credential)).toEqual({
        admitted: false,
        served: 'nothing',
      });
    }
  });
});
