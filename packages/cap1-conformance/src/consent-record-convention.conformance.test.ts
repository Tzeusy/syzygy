import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import { afterEach, describe, expect, it } from 'vitest';

import { loadConsentReference, resolveConsentReferencePath } from '@syzygy/cap1-daemon';

// Pins the consent-record on-disk convention (RT2; CAP1-REQ-010…016;
// RFC3-6/7) as a spec-carried behavior: a consent reference resolves to
// EXACTLY ONE location, `<decisionsDir>/<reference>.yaml`. Discovered gap
// (syzygy-a08): the convention lived only as a code comment and the
// `CONSENT_RECORD_EXTENSION` constant in consent-loading.ts, with no
// conformance test pinning it.
//
// Oracle independence: every expected path and extension below is a
// hard-coded string literal built with `join`, never the module's own
// `CONSENT_RECORD_EXTENSION` constant or its internal join call — so a
// change to the convention's shape (join order, separator, extension)
// falsifies this file, not just the implementation's own unit tests.

let tempDirs: string[] = [];

function decisionsDir(): string {
  const dir = mkdtempSync(join(tmpdir(), 'syzygy-a08-consent-convention-'));
  tempDirs.push(dir);
  return dir;
}

afterEach(() => {
  for (const dir of tempDirs) {
    rmSync(dir, { recursive: true, force: true });
  }
  tempDirs = [];
});

describe('consent-record on-disk convention — <decisionsDir>/<reference>.yaml', () => {
  it('normal resolution: a bare reference resolves to exactly <decisionsDir>/<reference>.yaml', () => {
    const dir = decisionsDir();
    const resolution = resolveConsentReferencePath(dir, 'consent-alpha');
    expect(resolution.ok).toBe(true);
    if (resolution.ok) {
      // Literal oracle: dir joined with the literal reference name plus
      // the literal ".yaml" extension — not the implementation's constant.
      expect(resolution.path).toBe(join(dir, 'consent-alpha.yaml'));
    }
  });

  it('traversal attempt: a reference naming ".." or containing a traversal segment is refused before any filesystem access', () => {
    const dir = decisionsDir();
    for (const reference of ['..', '.']) {
      const resolution = resolveConsentReferencePath(dir, reference);
      expect(resolution.ok).toBe(false);
      if (!resolution.ok) {
        expect(resolution.failure.kind).toBe('reference-unresolvable');
        expect(resolution.failure.reference).toBe(reference);
      }
    }
  });

  it('traversal attempt: a reference shaped like an escape path never reaches a file outside decisionsDir', () => {
    const dir = decisionsDir();
    const outside = decisionsDir();
    writeFileSync(join(outside, 'consent-secret.yaml'), 'id: consent-secret\n', 'utf8');

    // The only way to spell a path pointing at the sibling directory is
    // with a path separator — which is refused outright as not a bare
    // record name, so the escape is never attempted at the filesystem.
    const escapeReference = `../${outside.split('/').pop()}/consent-secret`;
    const resolution = resolveConsentReferencePath(dir, escapeReference);
    expect(resolution.ok).toBe(false);
    if (!resolution.ok) {
      expect(resolution.failure.kind).toBe('reference-unresolvable');
      expect(resolution.failure.detail).toBe(
        'reference contains a path separator; a consent reference is a bare record name',
      );
    }

    const load = loadConsentReference(dir, escapeReference);
    expect(load.ok).toBe(false);
  });

  it('missing extension: a file written without the .yaml extension is not found by its bare name', () => {
    const dir = decisionsDir();
    // Written at exactly the reference name, deliberately WITHOUT the
    // ".yaml" suffix the convention requires.
    writeFileSync(join(dir, 'consent-bare'), 'id: consent-bare\n', 'utf8');

    const load = loadConsentReference(dir, 'consent-bare');
    expect(load.ok).toBe(false);
    if (!load.ok) {
      expect(load.failure.kind).toBe('reference-unresolvable');
      // The failure names the exact location the convention looked at —
      // the extensionless file on disk is never treated as a match.
      expect(load.failure.detail).toContain('consent-bare.yaml');
    }
  });

  it('missing extension: the resolved path always carries the literal .yaml suffix, even for a reference that already ends in .yaml', () => {
    const dir = decisionsDir();
    const resolution = resolveConsentReferencePath(dir, 'consent-alpha.yaml');
    expect(resolution.ok).toBe(true);
    if (resolution.ok) {
      // The convention appends the extension unconditionally; it does not
      // detect or strip an extension already present in the reference.
      expect(resolution.path).toBe(join(dir, 'consent-alpha.yaml.yaml'));
    }
  });

  it('reference containing path separators: forward slash, backslash, and an absolute-looking reference are all refused', () => {
    const dir = decisionsDir();
    for (const reference of ['a/b', 'a\\b', '/etc/passwd', 'sub/consent-alpha']) {
      const resolution = resolveConsentReferencePath(dir, reference);
      expect(resolution.ok).toBe(false);
      if (!resolution.ok) {
        expect(resolution.failure.kind).toBe('reference-unresolvable');
        expect(resolution.failure.detail).toBe(
          'reference contains a path separator; a consent reference is a bare record name',
        );
      }
    }
  });

  it('a real record loaded through the convention round-trips: written at the exact resolved path, found by its bare reference', () => {
    const dir = decisionsDir();
    const path = join(dir, 'consent-roundtrip.yaml');
    writeFileSync(
      path,
      [
        'id: consent-roundtrip',
        'project: prj-a08',
        'repository: repo-a08',
        'scope: observe',
        'attribution: owner',
        'grant_state: in-force',
        '',
      ].join('\n'),
      'utf8',
    );

    const load = loadConsentReference(dir, 'consent-roundtrip');
    expect(load.ok).toBe(true);
    if (load.ok) {
      expect(load.path).toBe(path);
    }
  });
});
