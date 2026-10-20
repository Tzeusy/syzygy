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
  /** Independently observed work items, when available without a seed graph. */
  readonly observedItemCount?: number;
}

export type TrajectoryProjection = TrajectoryProjectionObserved | TrajectoryProjectionUnknown;

export interface ProjectTrajectoryOptions {
  readonly nonClosedLimit: number;
  readonly recentClosedWindow: number;
}

function byId(a: WorkItemFact, b: WorkItemFact): number {
  return a.id < b.id ? -1 : a.id > b.id ? 1 : 0;
}

/** Missing or invalid recorded times rank last; never infer one from another field. */
function newestFirst(a: string | null, b: string | null): number {
  const aTime = Date.parse(a ?? '');
  const bTime = Date.parse(b ?? '');
  const aRank = Number.isNaN(aTime) ? -Infinity : aTime;
  const bRank = Number.isNaN(bTime) ? -Infinity : bTime;
  return aRank === bRank ? 0 : aRank > bRank ? -1 : 1;
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
 * Both populations are capped, ranked by their recorded update/closure
 * times and then id. Cards keep ascending id order within each column.
 */
export function projectTrajectory(
  workItems: WorkItemsResult,
  options: ProjectTrajectoryOptions,
): TrajectoryProjection {
  if (workItems.kind === 'unknown') {
    return { kind: 'unknown', reason: workItems.reason };
  }

  const sorted = [...workItems.items].sort(byId);
  const open = sorted
    .filter((item) => item.status !== 'closed')
    .sort((a, b) => newestFirst(a.updatedAt, b.updatedAt) || byId(a, b))
    .slice(0, options.nonClosedLimit);
  const closed = sorted
    .filter((item) => item.status === 'closed')
    .sort((a, b) => newestFirst(a.closedAt, b.closedAt) || byId(a, b))
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
    doltRevision: workItems.provenance.revision,
    selectionRule: `up to ${options.nonClosedLimit} most recently updated non-closed items, plus up to ${options.recentClosedWindow} most recently closed items; missing or invalid times last, timestamp ties and card order by ascending item id`,
    rendered,
    renderedCount: rendered.length,
    excludedCount: workItems.items.length - rendered.length,
    totalCount: workItems.items.length,
    timeRange,
  };
}
