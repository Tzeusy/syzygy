import { escapeHtml } from '@syzygy/cap1-daemon';
import type { PocModel, WorkerChangeObserved } from '@syzygy/three-surface-poc-core';
import type { TrajectoryColumn, TrajectoryLaneItem } from '@syzygy/three-surface-poc-core';
import { WORKER_CHANGE_INTENT_ID, type TestArtifactVerificationResult } from '@syzygy/three-surface-poc-core';

import { MATERIALIZE_PANEL_STYLE, renderMaterializePanel } from './materialize-action.js';
import { pageShell } from './page-shell.js';
import { TAILNET_MOUNT_PREFIX } from './tailnet.js';

export const TRAJECTORY_HUMAN_PATH = '/trajectory' as const;
export const TRAJECTORY_TAILNET_PATH = `${TAILNET_MOUNT_PREFIX}/trajectory` as const;

const COLUMN_ORDER: readonly TrajectoryColumn[] = [
  'Backlog',
  'In Progress',
  'Blocked',
  'Deferred',
  'Pinned',
  'Hooked',
  'Done',
];

function timeOffsetPercent(
  instant: string,
  range: { readonly earliest: string; readonly latest: string },
): number {
  const earliestMs = Date.parse(range.earliest);
  const latestMs = Date.parse(range.latest);
  const span = latestMs - earliestMs;
  if (span <= 0) {
    return 0;
  }
  const clamped = Math.min(Math.max(Date.parse(instant) - earliestMs, 0), span);
  return (clamped / span) * 100;
}

function laneBar(
  item: TrajectoryLaneItem,
  range: { readonly earliest: string; readonly latest: string } | null,
): string {
  if (range === null) {
    return '';
  }
  const start = timeOffsetPercent(item.createdAt, range);
  const end = timeOffsetPercent(item.closedAt ?? item.updatedAt, range);
  const left = Math.min(start, end);
  const width = Math.max(end - start, 0.6);
  return `<div class="lane-track" aria-hidden="true"><div class="lane-bar" data-parity-field="time-lane" style="--lane-left:${left.toFixed(3)}%;--lane-width:${width.toFixed(3)}%"></div></div>`;
}

const WORKER_CHANGE_STATE_LABEL = {
  planned: 'Planned',
  active: 'Active',
  'changed-or-merged': 'Changed / merged',
} as const;

function verificationBadge(verification: TestArtifactVerificationResult): string {
  if (verification.kind === 'verified') {
    return `<span class="epistemic epistemic-observed" data-parity-field="worker-change-verification" title="A captured, passing focused-pytest artifact bound to commit ${escapeHtml(verification.record.repositoryCommit)} and the governing intent ${escapeHtml(WORKER_CHANGE_INTENT_ID)}.">Verification: Verified — ${escapeHtml(verification.record.summary)}</span>`;
  }
  return `<span class="epistemic epistemic-unknown" data-parity-field="worker-change-verification" title="${escapeHtml(verification.reason)}">Verification: Not verified</span>`;
}

function workerChangeBadge(
  workerChange: WorkerChangeObserved | null,
  verification: TestArtifactVerificationResult,
): string {
  if (workerChange === null) {
    return '';
  }
  const label = WORKER_CHANGE_STATE_LABEL[workerChange.state];
  const detail =
    workerChange.state === 'planned'
      ? 'No git activity observed yet on the bounded source seam.'
      : workerChange.commit === null
        ? ''
        : `<code class="wi-id">${escapeHtml(workerChange.commit.sha.slice(0, 12))}</code>${
            workerChange.commit.containingRef === null
              ? ''
              : ` on <code class="wi-id">${escapeHtml(workerChange.commit.containingRef)}</code>`
          }`;
  return `<div class="worker-change" data-parity-field="worker-change-state">
    <span class="wi-status">External worker: ${escapeHtml(label)}</span>
    ${detail === '' ? '' : `<span class="worker-change-detail">${detail}</span>`}
    ${verificationBadge(verification)}
  </div>`;
}

function itemCard(
  item: TrajectoryLaneItem,
  range: { readonly earliest: string; readonly latest: string } | null,
  workerChange: WorkerChangeObserved | null,
  testArtifactVerification: TestArtifactVerificationResult,
): string {
  return `<li class="wi-card" id="workitem-${escapeHtml(item.id)}" data-work-item-id="${escapeHtml(item.id)}">
    <a class="wi-title" href="#workitem-${escapeHtml(item.id)}" data-parity-field="work-item-title">${escapeHtml(item.title)}</a>
    <code class="wi-id" data-parity-field="work-item-id">${escapeHtml(item.id)}</code>
    <span class="wi-status" data-parity-field="work-item-status">${escapeHtml(item.status)}</span>
    <span class="epistemic epistemic-unknown" data-parity-field="work-item-verification" title="Activity is not verification: no test evidence has been ingested for this item.">Verification: Unknown</span>
    ${workerChangeBadge(workerChange, testArtifactVerification)}
    ${laneBar(item, range)}
  </li>`;
}

const TRAJECTORY_STYLE = `
  .scope-statement { max-width: 78ch; }
  .board { display: grid; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); gap: 1rem; padding: 1.5rem 0 3rem; }
  .board-column { background: linear-gradient(145deg, #102126, var(--panel)); border: 1px solid var(--line); padding: 1rem; min-width: 0; }
  .board-column h2 { font-size: 1.1rem; margin: 0 0 .8rem; }
  .board-column .count { color: var(--muted); font-family: var(--font-mono); font-size: .78rem; }
  .wi-list { list-style: none; padding: 0; margin: 0; display: grid; gap: .7rem; }
  .wi-card { background: #091416; border: 1px solid var(--line); padding: .6rem .7rem; display: grid; gap: .3rem; position: relative; }
  .wi-title { display: block; font-family: var(--font-mono); font-size: .82rem; color: var(--ink); text-decoration: none; }
  .wi-title:hover, .wi-title:focus-visible { color: var(--cyan); }
  .wi-id { color: var(--muted); font-size: .7rem; }
  .wi-status { font-family: var(--font-mono); font-size: .7rem; color: var(--muted); text-transform: uppercase; }
  .lane-track { position: relative; height: .35rem; background: #1a2c30; margin-top: .3rem; }
  .lane-bar { position: absolute; top: 0; height: 100%; left: var(--lane-left); width: var(--lane-width); background: var(--cyan); }
  .worker-change { display: grid; gap: .2rem; padding-top: .2rem; border-top: 1px dashed var(--line); }
  .worker-change-detail { font-size: .72rem; color: var(--muted); }
  ${MATERIALIZE_PANEL_STYLE}
`;

export function renderTrajectoryPage(model: PocModel): string {
  const trajectory = model.trajectory;
  const workerChange = model.workerChange.kind === 'observed' ? model.workerChange : null;
  let body: string;
  if (trajectory.kind === 'unknown') {
    body = `<p class="unavailable-notice" data-unknown-disclosure="region:work-items">Unknown — ${escapeHtml(trajectory.reason)}. This is a distinct state from an observed-empty board: no board is rendered because the work-item region could not be observed.</p>`;
  } else {
    const byColumn = new Map<TrajectoryColumn, TrajectoryLaneItem[]>();
    for (const column of COLUMN_ORDER) {
      byColumn.set(column, []);
    }
    for (const item of trajectory.rendered) {
      byColumn.get(item.column)?.push(item);
    }
    const columns = COLUMN_ORDER.map((column) => {
      const items = byColumn.get(column) ?? [];
      return `<section class="board-column" aria-label="${escapeHtml(column)} column">
        <h2>${escapeHtml(column)} <span class="count">(${items.length})</span></h2>
        <ol class="wi-list">${items
          .map((item) =>
            itemCard(
              item,
              trajectory.timeRange,
              workerChange !== null && workerChange.beadId === item.id ? workerChange : null,
              model.testArtifactVerification,
            ),
          )
          .join('')}</ol>
      </section>`;
    }).join('');

    body = `
      <p class="scope-statement notice" data-parity-field="trajectory-scope">
        Rendering ${trajectory.renderedCount} of ${trajectory.totalCount} observed work items (${trajectory.selectionRule});
        <span data-parity-field="trajectory-excluded-count">${trajectory.excludedCount}</span> items are outside this selection and not shown.
      </p>
      <div class="board" role="list" aria-label="Work-item board by status column">${columns}</div>`;
  }

  body += renderMaterializePanel(model);

  return pageShell({
    title: 'Trajectory · Syzygy three-surface POC',
    current: 'trajectory',
    eyebrow: `Trajectory · Butlers ${model.project.revision.slice(0, 12)}`,
    heading: 'Work and time, observed',
    lede: 'A board over the registered Beads Dolt database, columns from a declared status mapping, time from recorded instants only.',
    extraStyle: TRAJECTORY_STYLE,
    body,
    footer:
      trajectory.kind === 'observed'
        ? `Beads Dolt revision <code>${escapeHtml(trajectory.doltRevision)}</code>.`
        : 'Work-item region: Unknown.',
    escapeHtml,
  });
}
