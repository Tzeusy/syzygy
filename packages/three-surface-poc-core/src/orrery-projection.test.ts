import { describe, expect, it } from 'vitest';

import type { CodeStructureObserved } from './code-structure.js';
import { projectOrrery } from './orrery-projection.js';

function structureFixture(): CodeStructureObserved {
  return {
    kind: 'observed',
    revision: 'rev-1',
    capturedAt: '2026-08-30T00:00:00Z',
    files: [
      { path: 'apps/a.ts', sizeBytes: 10, digest: 'git-blob-sha1:1', language: 'typescript', revision: 'rev-1' },
      { path: 'apps/b.py', sizeBytes: 20, digest: 'git-blob-sha1:2', language: 'python', revision: 'rev-1' },
      { path: 'src/butlers/identity.py', sizeBytes: 30, digest: 'git-blob-sha1:3', language: 'python', revision: 'rev-1' },
      { path: 'README.md', sizeBytes: 5, digest: 'git-blob-sha1:4', language: 'markdown', revision: 'rev-1' },
    ],
  };
}

describe('Orrery projection', () => {
  it('groups by directory structure and declared mappings only, reconciling mapped+unmapped=total (POC-REQ-050/051/052)', () => {
    const structure = structureFixture();
    const projection = projectOrrery(structure, [
      { id: 'code:identity-resolution', path: 'src/butlers/identity.py', capabilityId: 'capability:whatsapp-transport-identity' },
    ]);
    expect(projection.kind).toBe('observed');
    if (projection.kind !== 'observed') throw new Error('unreachable');
    expect(projection.totalFileCount).toBe(4);
    expect(projection.mappedFileCount).toBe(1);
    expect(projection.unmappedFileCount).toBe(3);
    expect(projection.mappedFileCount + projection.unmappedFileCount).toBe(projection.totalFileCount);
    expect(projection.mappedRegions).toEqual([
      { id: 'code:identity-resolution', path: 'src/butlers/identity.py', capabilityId: 'capability:whatsapp-transport-identity', sizeBytes: 30 },
    ]);
    const districtPaths = projection.districts.map((district) => district.path).sort();
    expect(districtPaths).toEqual(['(root)', 'apps', 'src']);
  });

  it('produces identical layout assignments across two renders of one observation (POC-REQ-050)', () => {
    const structure = structureFixture();
    const first = projectOrrery(structure, []);
    const second = projectOrrery(structure, []);
    expect(second).toEqual(first);
  });

  it('propagates Unknown from the structure observation (POC-REQ-003 pass-through)', () => {
    const projection = projectOrrery({ kind: 'unknown', reason: 'repo unreadable' }, []);
    expect(projection).toEqual({ kind: 'unknown', reason: 'repo unreadable' });
  });

  it('mutation check: a falsifier reconciliation would be caught', () => {
    const projection = projectOrrery(structureFixture(), []);
    if (projection.kind !== 'observed') throw new Error('unreachable');
    const falsified = { ...projection, unmappedFileCount: projection.unmappedFileCount + 1 };
    expect(falsified.mappedFileCount + falsified.unmappedFileCount).not.toBe(falsified.totalFileCount);
  });
});
