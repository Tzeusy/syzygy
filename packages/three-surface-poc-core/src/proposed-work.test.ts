import { describe, expect, it } from 'vitest';

import type { CodeStructureResult } from './code-structure.js';
import { unevaluatedProjectShape } from './project-shape-model.js';
import {
  baselineSpecPath,
  deriveCurrentAuthority,
  deriveLifecycle,
  deriveProposedWork,
  parseChangeDeltaPath,
} from './proposed-work.js';

const CHANGE = 'repair-whatsapp-identity-reconciliation';
const DELTA = `openspec/changes/${CHANGE}/specs/switchboard-identity/spec.md`;

function tree(paths: readonly string[]): CodeStructureResult {
  return { kind: 'observed', revision: 'a'.repeat(40), capturedAt: '2026-09-04T00:00:00Z', files: paths.map((path) => ({ path, sizeBytes: 1, digest: 'sha256:0', language: 'other', revision: 'a'.repeat(40) })) };
}

describe('proposed work (PWB-REQ-013)', () => {
  it('parses the change id and amended spec directory from a delta path, and nothing else', () => {
    expect(parseChangeDeltaPath(DELTA)).toEqual({ changeId: CHANGE, specKey: 'switchboard-identity' });
    expect(parseChangeDeltaPath('openspec/specs/switchboard-identity/spec.md')).toBeUndefined();
    expect(parseChangeDeltaPath(`openspec/changes/${CHANGE}/proposal.md`)).toBeUndefined();
    expect(parseChangeDeltaPath(`openspec/changes/archive/2026-01-01-${CHANGE}/specs/x/spec.md`)).toBeUndefined();
    expect(baselineSpecPath('switchboard-identity')).toBe('openspec/specs/switchboard-identity/spec.md');
  });

  it('reads the lifecycle state from tree paths only: active, archived, contradicted, absent, or Unknown without a tree', () => {
    const active = deriveLifecycle(CHANGE, tree([`openspec/changes/${CHANGE}/proposal.md`, DELTA, 'src/x.py']));
    expect(active).toMatchObject({ kind: 'observed', state: 'active', evidence: [`openspec/changes/${CHANGE}/proposal.md`, DELTA] });

    const archived = deriveLifecycle(CHANGE, tree([`openspec/changes/archive/2026-08-30-${CHANGE}/proposal.md`]));
    expect(archived).toMatchObject({ kind: 'observed', state: 'archived', evidence: [`openspec/changes/archive/2026-08-30-${CHANGE}/proposal.md`] });
    expect(deriveLifecycle(CHANGE, tree([`openspec/changes/archive/${CHANGE}/proposal.md`]))).toMatchObject({ kind: 'observed', state: 'archived' });

    const both = deriveLifecycle(CHANGE, tree([`openspec/changes/${CHANGE}/proposal.md`, `openspec/changes/archive/2026-08-30-${CHANGE}/proposal.md`]));
    expect(both.kind).toBe('unknown');
    expect(both.kind === 'unknown' ? both.reason : '').toContain('contradicted');

    const absent = deriveLifecycle(CHANGE, tree(['src/x.py', 'openspec/changes/other-change/proposal.md']));
    expect(absent.kind).toBe('unknown');
    expect(absent.kind === 'unknown' ? absent.reason : '').toContain('No OpenSpec change entry');

    // A change whose id is a prefix of another must not match the other.
    expect(deriveLifecycle('repair', tree([`openspec/changes/${CHANGE}/proposal.md`])).kind).toBe('unknown');

    const noTree = deriveLifecycle(CHANGE, { kind: 'unknown', reason: 'listing refused' });
    expect(noTree).toEqual({ kind: 'unknown', reason: "The tree listing was not observed (listing refused); the change's lifecycle state was not read." });
  });

  it('leaves the current authority Unknown with the shape\'s own reason and route when the shape was not observed', () => {
    const shape = unevaluatedProjectShape('no authority supplied');
    const current = deriveCurrentAuthority('switchboard-identity', shape);
    expect(current).toMatchObject({ kind: 'unknown', reason: 'unconsented-source-or-provider', route: 'Record consent' });
    expect(current.kind === 'unknown' ? current.detail : '').toContain('openspec/specs/switchboard-identity/spec.md');
  });

  it('refuses a delta path that is not an OpenSpec change delta', () => {
    expect(() =>
      deriveProposedWork({
        capabilityId: 'capability:x',
        proposal: { path: 'p.md', revision: 'r', digest: 'sha256:0' },
        delta: { path: 'openspec/specs/x/spec.md', revision: 'r', digest: 'sha256:0' },
        codeStructure: tree([]),
        projectShape: unevaluatedProjectShape('n/a'),
      }),
    ).toThrow(/not an OpenSpec change delta path/);
  });
});
