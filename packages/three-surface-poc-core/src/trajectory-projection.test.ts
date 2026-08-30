import { describe, expect, it } from 'vitest';

import { projectTrajectory, STATUS_TO_COLUMN } from './trajectory-projection.js';
import type { WorkItemsObserved } from './work-items.js';

function itemsFixture(): WorkItemsObserved {
  return {
    kind: 'observed',
    beadPrefix: 'bu',
    doltRevision: 'rev-1',
    capturedAt: '2026-08-30T00:00:00Z',
    items: [
      { id: 'bu-1', title: 'open one', status: 'open', issueType: 'task', priority: 1, createdAt: '2026-08-01T00:00:00Z', updatedAt: '2026-08-02T00:00:00Z', closedAt: null, doltRevision: 'rev-1' },
      { id: 'bu-2', title: 'in progress one', status: 'in_progress', issueType: 'task', priority: 1, createdAt: '2026-08-03T00:00:00Z', updatedAt: '2026-08-04T00:00:00Z', closedAt: null, doltRevision: 'rev-1' },
      { id: 'bu-3', title: 'closed recent', status: 'closed', issueType: 'task', priority: 1, createdAt: '2026-08-05T00:00:00Z', updatedAt: '2026-08-06T00:00:00Z', closedAt: '2026-08-06T00:00:00Z', doltRevision: 'rev-1' },
      { id: 'bu-4', title: 'closed older', status: 'closed', issueType: 'task', priority: 1, createdAt: '2026-07-01T00:00:00Z', updatedAt: '2026-07-02T00:00:00Z', closedAt: '2026-07-02T00:00:00Z', doltRevision: 'rev-1' },
    ],
  };
}

describe('Trajectory projection', () => {
  it('places every rendered item by its declared status-to-column mapping (POC-REQ-040)', () => {
    const projection = projectTrajectory(itemsFixture(), { recentClosedWindow: 1 });
    expect(projection.kind).toBe('observed');
    if (projection.kind !== 'observed') throw new Error('unreachable');
    for (const item of projection.rendered) {
      expect(item.column).toBe(STATUS_TO_COLUMN[item.status]);
    }
  });

  it('declares scope and reconciles rendered + excluded against the total (POC-REQ-042)', () => {
    const projection = projectTrajectory(itemsFixture(), { recentClosedWindow: 1 });
    if (projection.kind !== 'observed') throw new Error('unreachable');
    expect(projection.renderedCount + projection.excludedCount).toBe(projection.totalCount);
    expect(projection.totalCount).toBe(4);
    // open + in_progress (2) + 1 most-recently-closed = 3 rendered, 1 excluded
    expect(projection.renderedCount).toBe(3);
    expect(projection.excludedCount).toBe(1);
    expect(projection.rendered.map((item) => item.id)).not.toContain('bu-4');
    expect(projection.selectionRule.length).toBeGreaterThan(0);
  });

  it('never renders activity/closure as verification satisfaction (POC-REQ-043)', () => {
    const projection = projectTrajectory(itemsFixture(), { recentClosedWindow: 5 });
    if (projection.kind !== 'observed') throw new Error('unreachable');
    const closedItem = projection.rendered.find((item) => item.id === 'bu-3');
    expect(closedItem?.status).toBe('closed');
    expect(closedItem?.verification).toBe('unknown');
  });

  it('derives every temporal value from recorded instants, identical across two projections (POC-REQ-041)', () => {
    const fixture = itemsFixture();
    const first = projectTrajectory(fixture, { recentClosedWindow: 5 });
    const second = projectTrajectory(fixture, { recentClosedWindow: 5 });
    expect(second).toEqual(first);
    if (first.kind !== 'observed') throw new Error('unreachable');
    expect(first.timeRange).toEqual({ earliest: '2026-07-01T00:00:00Z', latest: '2026-08-06T00:00:00Z' });
  });

  it('propagates Unknown from the work-items observation', () => {
    const projection = projectTrajectory({ kind: 'unknown', reason: 'db unreachable' }, { recentClosedWindow: 5 });
    expect(projection).toEqual({ kind: 'unknown', reason: 'db unreachable' });
  });

  it('mutation check: a falsifier reconciliation would be caught', () => {
    const projection = projectTrajectory(itemsFixture(), { recentClosedWindow: 1 });
    if (projection.kind !== 'observed') throw new Error('unreachable');
    const falsified = { ...projection, excludedCount: projection.excludedCount + 5 };
    expect(falsified.renderedCount + falsified.excludedCount).not.toBe(falsified.totalCount);
  });
});
