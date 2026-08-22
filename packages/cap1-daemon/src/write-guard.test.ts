import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';

import { afterEach, beforeEach, describe, expect, it } from 'vitest';

import { authorizeRuntimeWrite, guardedWriteFile } from './write-guard.js';

// RT7 — runtime write-boundary normalization and traversal protection
// (CAP1-REQ-061; CAP1-REQ-023 and CAP1-REQ-053 context).
//
// Real temp directories, no mocks. Every traversal probe asserts BOTH
// the named failure literal AND that no byte landed (file provably
// absent after the refusal) — CAP1-REQ-061's oracle is an external
// filesystem comparison, so the tests check the filesystem, not the
// guard's self-report alone.
//
// Oracle independence: every expected failure name below is a
// hard-coded string literal, never imported from the vocabulary.

let root: string;

beforeEach(() => {
  root = fs.mkdtempSync(path.join(os.tmpdir(), 'cap1-write-guard-'));
});

afterEach(() => {
  fs.rmSync(root, { recursive: true, force: true });
});

function refusal(result: ReturnType<typeof authorizeRuntimeWrite>): {
  refusedBy: string;
  candidatePath: string;
} {
  if (result.authorized) {
    throw new Error('expected a refusal, got authorization');
  }
  return result;
}

describe('authorizeRuntimeWrite — traversal probes are refused by name', () => {
  it('refuses openspec/../README.md on the NORMALIZED path: it lands at the root, outside the governed plane', () => {
    // The recorded core defect: raw startsWith would pass this. The
    // guard judges the normalized path (README.md), which stays inside
    // the root but leaves the governed plane — so the refusal carries
    // core's existing governed-plane vocabulary, not traversal.
    const result = refusal(authorizeRuntimeWrite(root, 'openspec/../README.md'));
    expect(result.refusedBy).toBe('outside-governed-plane');
    expect(result.candidatePath).toBe('openspec/../README.md');
  });

  it('refuses ../outside.txt as traversal', () => {
    const result = refusal(authorizeRuntimeWrite(root, '../outside.txt'));
    expect(result.refusedBy).toBe('traversal');
  });

  it('refuses an absolute path outside the root as traversal', () => {
    const elsewhere = fs.mkdtempSync(path.join(os.tmpdir(), 'cap1-elsewhere-'));
    try {
      const probe = path.join(elsewhere, 'abs.txt');
      const result = refusal(authorizeRuntimeWrite(root, probe));
      expect(result.refusedBy).toBe('traversal');
    } finally {
      fs.rmSync(elsewhere, { recursive: true, force: true });
    }
  });

  it('refuses a/../../escape as traversal', () => {
    const result = refusal(authorizeRuntimeWrite(root, 'a/../../escape'));
    expect(result.refusedBy).toBe('traversal');
  });

  it('refuses dot-segment writes prefixed into openspec/ that escape the root as traversal', () => {
    const result = refusal(authorizeRuntimeWrite(root, 'openspec/../../intruder.md'));
    expect(result.refusedBy).toBe('traversal');
  });

  it('refuses dot-segment writes prefixed into .syzygy/ that land outside the governed plane', () => {
    // .syzygy/../.git/config normalizes to .git/config — inside the
    // root, outside the governed plane.
    const result = refusal(authorizeRuntimeWrite(root, '.syzygy/../.git/config'));
    expect(result.refusedBy).toBe('outside-governed-plane');
  });

  it('refuses a symlinked directory inside the root that points outside the root', () => {
    const outsideTarget = fs.mkdtempSync(path.join(os.tmpdir(), 'cap1-symlink-target-'));
    try {
      fs.mkdirSync(path.join(root, 'openspec'));
      fs.symlinkSync(outsideTarget, path.join(root, 'openspec', 'link'));
      const result = refusal(authorizeRuntimeWrite(root, 'openspec/link/evil.md'));
      expect(result.refusedBy).toBe('symlink-escape');
    } finally {
      fs.rmSync(outsideTarget, { recursive: true, force: true });
    }
  });

  it('refuses degenerate inputs: empty, whitespace, "."', () => {
    expect(refusal(authorizeRuntimeWrite(root, '')).refusedBy).toBe('degenerate-input');
    expect(refusal(authorizeRuntimeWrite(root, '   ')).refusedBy).toBe('degenerate-input');
    expect(refusal(authorizeRuntimeWrite(root, '.')).refusedBy).toBe('degenerate-input');
  });

  it('refuses a candidate that normalizes to the root itself as degenerate', () => {
    expect(refusal(authorizeRuntimeWrite(root, 'openspec/..')).refusedBy).toBe(
      'degenerate-input',
    );
  });

  it('refuses an in-root write outside the governed plane with the core vocabulary', () => {
    const result = refusal(authorizeRuntimeWrite(root, 'packages/cap1-core/src/hack.ts'));
    expect(result.refusedBy).toBe('outside-governed-plane');
  });
});

describe('guardedWriteFile — refuses WITHOUT writing; writes only on authorization', () => {
  it('openspec/../README.md: named refusal and the root README is provably absent', () => {
    const result = refusal(guardedWriteFile(root, 'openspec/../README.md', 'intrusion'));
    expect(result.refusedBy).toBe('outside-governed-plane');
    expect(fs.existsSync(path.join(root, 'README.md'))).toBe(false);
  });

  it('../outside.txt: named refusal and nothing landed outside the root', () => {
    const result = refusal(guardedWriteFile(root, '../outside.txt', 'intrusion'));
    expect(result.refusedBy).toBe('traversal');
    expect(fs.existsSync(path.resolve(root, '../outside.txt'))).toBe(false);
  });

  it('absolute path outside the root: named refusal and the target is provably absent', () => {
    const elsewhere = fs.mkdtempSync(path.join(os.tmpdir(), 'cap1-elsewhere-'));
    try {
      const probe = path.join(elsewhere, 'abs.txt');
      const result = refusal(guardedWriteFile(root, probe, 'intrusion'));
      expect(result.refusedBy).toBe('traversal');
      expect(fs.existsSync(probe)).toBe(false);
      // Second method for the absence claim: enumerate the directory.
      expect(fs.readdirSync(elsewhere)).toEqual([]);
    } finally {
      fs.rmSync(elsewhere, { recursive: true, force: true });
    }
  });

  it('a/../../escape: named refusal and the escape target is provably absent', () => {
    const result = refusal(guardedWriteFile(root, 'a/../../escape', 'intrusion'));
    expect(result.refusedBy).toBe('traversal');
    expect(fs.existsSync(path.resolve(root, '..', 'escape'))).toBe(false);
    expect(fs.existsSync(path.join(root, 'a'))).toBe(false);
  });

  it('symlink escape: named refusal and the outside target directory stays empty', () => {
    const outsideTarget = fs.mkdtempSync(path.join(os.tmpdir(), 'cap1-symlink-target-'));
    try {
      fs.mkdirSync(path.join(root, 'openspec'));
      fs.symlinkSync(outsideTarget, path.join(root, 'openspec', 'link'));
      const result = refusal(guardedWriteFile(root, 'openspec/link/evil.md', 'intrusion'));
      expect(result.refusedBy).toBe('symlink-escape');
      expect(fs.existsSync(path.join(outsideTarget, 'evil.md'))).toBe(false);
      expect(fs.readdirSync(outsideTarget)).toEqual([]);
    } finally {
      fs.rmSync(outsideTarget, { recursive: true, force: true });
    }
  });

  it('dot-segment probe into .syzygy/ landing at .git: named refusal and .git stays absent', () => {
    const result = refusal(guardedWriteFile(root, '.syzygy/../.git/config', 'intrusion'));
    expect(result.refusedBy).toBe('outside-governed-plane');
    expect(fs.existsSync(path.join(root, '.git'))).toBe(false);
  });

  it('dot-segment probe into openspec/ escaping the root: named refusal, nothing written anywhere', () => {
    const result = refusal(guardedWriteFile(root, 'openspec/../../intruder.md', 'intrusion'));
    expect(result.refusedBy).toBe('traversal');
    expect(fs.existsSync(path.resolve(root, '..', 'intruder.md'))).toBe(false);
    expect(fs.readdirSync(root)).toEqual([]);
  });

  it('degenerate input: named refusal and the root stays empty', () => {
    const result = refusal(guardedWriteFile(root, '', 'intrusion'));
    expect(result.refusedBy).toBe('degenerate-input');
    expect(fs.readdirSync(root)).toEqual([]);
  });
});

describe('guardedWriteFile — legitimate in-boundary writes succeed', () => {
  it('writes into openspec/** and reports the authorization', () => {
    const result = guardedWriteFile(
      root,
      'openspec/changes/probe/notes.md',
      'proposal body',
    );
    expect(result.authorized).toBe(true);
    if (result.authorized) {
      expect(result.namespace).toBe('openspec/');
      expect(result.relativePath).toBe('openspec/changes/probe/notes.md');
      expect(result.absolutePath).toBe(
        path.join(root, 'openspec', 'changes', 'probe', 'notes.md'),
      );
    }
    expect(
      fs.readFileSync(path.join(root, 'openspec', 'changes', 'probe', 'notes.md'), 'utf8'),
    ).toBe('proposal body');
  });

  it('writes into .syzygy/** and reports the authorization', () => {
    const result = guardedWriteFile(root, '.syzygy/state/entry.md', 'entry body');
    expect(result.authorized).toBe(true);
    if (result.authorized) {
      expect(result.namespace).toBe('.syzygy/');
      expect(result.relativePath).toBe('.syzygy/state/entry.md');
    }
    expect(fs.readFileSync(path.join(root, '.syzygy', 'state', 'entry.md'), 'utf8')).toBe(
      'entry body',
    );
  });

  it('a dot-segment path that NORMALIZES into the governed plane is authorized (judgment is on the normalized path)', () => {
    // foo/../openspec/x.md normalizes to openspec/x.md — byte-identical
    // in effect to the legitimate governed write, so it is admitted.
    const result = guardedWriteFile(root, 'foo/../openspec/x.md', 'body');
    expect(result.authorized).toBe(true);
    if (result.authorized) {
      expect(result.relativePath).toBe('openspec/x.md');
    }
    expect(fs.readFileSync(path.join(root, 'openspec', 'x.md'), 'utf8')).toBe('body');
    expect(fs.existsSync(path.join(root, 'foo'))).toBe(false);
  });

  it('authorizeRuntimeWrite alone performs no write', () => {
    const result = authorizeRuntimeWrite(root, 'openspec/only-a-decision.md');
    expect(result.authorized).toBe(true);
    expect(fs.readdirSync(root)).toEqual([]);
  });
});
