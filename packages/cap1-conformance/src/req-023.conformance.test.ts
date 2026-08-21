import { describe, expect, it } from 'vitest';
import {
  GOVERNED_WRITE_NAMESPACES,
  isInsideGovernedPlane,
  HUMAN_ENTRY_PATH,
  serveEntryRoute,
  renderEntry,
  assessEntry,
  type ProjectId,
} from '@syzygy/cap1-core';

// CAP1-REQ-023 — Entry behavior writes nothing outside the governed plane.
//
// Oracle: isInsideGovernedPlane correctly classifies paths; the entry
// module exports no function that takes a write callback or returns a
// write instruction outside the plane.

describe('CAP1-REQ-023 — write boundary', () => {
  it('governed namespaces are openspec/ and .syzygy/', () => {
    expect(GOVERNED_WRITE_NAMESPACES[0]).toBe('openspec/');
    expect(GOVERNED_WRITE_NAMESPACES[1]).toBe('.syzygy/');
    expect(GOVERNED_WRITE_NAMESPACES.length).toBe(2);
  });

  it('paths inside .syzygy/ are inside the governed plane', () => {
    expect(isInsideGovernedPlane('.syzygy/intent/OVERVIEW.md')).toBe(true);
    expect(isInsideGovernedPlane('.syzygy/governance/doctrine/VIS.md')).toBe(true);
  });

  it('paths inside openspec/ are inside the governed plane', () => {
    expect(isInsideGovernedPlane('openspec/changes/my-change/spec.md')).toBe(true);
  });

  it('paths outside both namespaces are outside the governed plane', () => {
    expect(isInsideGovernedPlane('packages/cap1-core/src/entry.ts')).toBe(false);
    expect(isInsideGovernedPlane('README.md')).toBe(false);
    expect(isInsideGovernedPlane('apps/web/index.ts')).toBe(false);
  });

  it('the entry path itself is inside the governed plane', () => {
    expect(isInsideGovernedPlane(HUMAN_ENTRY_PATH)).toBe(true);
  });

  it('entry functions return data, never write instructions', () => {
    const route = serveEntryRoute('prj-test' as ProjectId);
    expect(typeof route.path).toBe('string');
    expect(typeof route.isIdentity).toBe('boolean');

    const rendering = renderEntry({ state: 'present', text: 'Hi' }, []);
    expect(typeof rendering.nonCitable).toBe('boolean');
    expect(typeof rendering.artifactClass).toBe('string');

    const assessment = assessEntry({ state: 'absent' }, []);
    expect(typeof assessment.kind).toBe('string');
  });
});
