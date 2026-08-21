import { describe, expect, it } from 'vitest';
import {
  HUMAN_ENTRY_PATH,
  serveEntryRoute,
  type ProjectId,
} from '@syzygy/cap1-core';

// CAP1-REQ-020 — One fixed Syzygy-owned entry path.
//
// Oracle: the served entry path is compared against the checker-authored
// literal string. Expected values are hard-coded here, never imported
// from vocabulary modules.

describe('CAP1-REQ-020 — one fixed Syzygy-owned entry path', () => {
  it('the fixed entry path is .syzygy/intent/OVERVIEW.md', () => {
    expect(HUMAN_ENTRY_PATH).toBe('.syzygy/intent/OVERVIEW.md');
  });

  it('serveEntryRoute returns the fixed path for any project', () => {
    const route = serveEntryRoute('prj-test-001' as ProjectId);
    expect(route.path).toBe('.syzygy/intent/OVERVIEW.md');
  });

  it('the route path is a publication location, never an identity', () => {
    const route = serveEntryRoute('prj-test-001' as ProjectId);
    expect(route.isIdentity).toBe(false);
  });

  it('no second entry path exists — the constant is the only one', () => {
    const routeA = serveEntryRoute('prj-alpha' as ProjectId);
    const routeB = serveEntryRoute('prj-beta' as ProjectId);
    expect(routeA.path).toBe(routeB.path);
    expect(routeA.path).toBe('.syzygy/intent/OVERVIEW.md');
  });
});
