import type { WorkItemFact, WorkItemsResult, WorkItemStatus } from './work-items.js';

export const STATUS_TO_COLUMN = {
  open: 'Backlog',
  in_progress: 'In Progress',
  blocked: 'Blocked',
  deferred: 'Deferred',
  pinned: 'Pinned',
  hooked: 'Hooked',
  closed: 'Done',
} as const satisfies Record<WorkItemStatus, string>;

export type TrajectoryColumn = (typeof STATUS_TO_COLUMN)[WorkItemStatus];

export interface TrajectoryLaneItem {
  readonly id: string;
  readonly title: string;
  readonly status: WorkItemStatus;
  readonly column: TrajectoryColumn;
  readonly createdAt: string;
  readonly updatedAt: string;
  readonly closedAt: string | null;
  readonly verification: 'unknown';
}

export interface TrajectoryProjectionObserved {
  readonly kind: 'observed';
  readonly doltRevision: string;
  readonly selectionRule: string;
  readonly rendered: readonly TrajectoryLaneItem[];
  readonly renderedCount: number;
  readonly excludedCount: number;
  readonly totalCount: number;
  readonly timeRange: { readonly earliest: string; readonly latest: string } | null;
}

export interface TrajectoryProjectionUnknown {
  readonly kind: 'unknown';
  readonly reason: string;
}

export type TrajectoryProjection = TrajectoryProjectionObserved | TrajectoryProjectionUnknown;

export interface ProjectTrajectoryOptions {
  readonly recentClosedWindow: number;
}

function laneItem(item: WorkItemFact): TrajectoryLaneItem {
  return {
    id: item.id,
    title: item.title,
    status: item.status,
    column: STATUS_TO_COLUMN[item.status],
    createdAt: item.createdAt,
    updatedAt: item.updatedAt,
    closedAt: item.closedAt,
    // No verification/test-evidence source is ingested by this POC slice;
    // closure or merge activity is never rendered as satisfaction
    // (POC-REQ-043) — the field is always the disclosed Unknown.
    verification: 'unknown',
  };
}

/**
 * Deterministic per observation (POC-REQ-041): every temporal value comes
 * from `item.createdAt/updatedAt/closedAt`, never a render-time clock.
 * Selection is input-ordered (sorted by id) so two renders of one
 * observation select and order identically.
 */
export function projectTrajectory(
  workItems: WorkItemsResult,
  options: ProjectTrajectoryOptions,
): TrajectoryProjection {
  if (workItems.kind === 'unknown') {
    return { kind: 'unknown', reason: workItems.reason };
  }

  const sorted = [...workItems.items].sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
  const open = sorted.filter((item) => item.status !== 'closed');
  const closed = sorted
    .filter((item) => item.status === 'closed')
    .sort((a, b) => {
      const byClosed = (b.closedAt ?? '').localeCompare(a.closedAt ?? '');
      return byClosed !== 0 ? byClosed : a.id < b.id ? -1 : a.id > b.id ? 1 : 0;
    })
    .slice(0, options.recentClosedWindow);

  const renderedIds = new Set<string>([...open.map((item) => item.id), ...closed.map((item) => item.id)]);
  const rendered = sorted.filter((item) => renderedIds.has(item.id)).map(laneItem);

  const instants = rendered.flatMap((item) =>
    [item.createdAt, item.updatedAt, item.closedAt ?? undefined].filter(
      (value): value is string => value !== undefined,
    ),
  );
  const timeRange =
    instants.length === 0
      ? null
      : {
          earliest: instants.reduce((min, value) => (value < min ? value : min)),
          latest: instants.reduce((max, value) => (value > max ? value : max)),
        };

  return {
    kind: 'observed',
    doltRevision: workItems.doltRevision,
    selectionRule: `all non-closed items, plus the ${options.recentClosedWindow} most recently closed items`,
    rendered,
    renderedCount: rendered.length,
    excludedCount: workItems.items.length - rendered.length,
    totalCount: workItems.items.length,
    timeRange,
  };
}
