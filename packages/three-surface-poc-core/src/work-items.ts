import { execFileSync } from 'node:child_process';

export const WORK_ITEM_STATUSES = [
  'open',
  'in_progress',
  'blocked',
  'deferred',
  'pinned',
  'hooked',
  'closed',
] as const;

export type WorkItemStatus = (typeof WORK_ITEM_STATUSES)[number];

export interface WorkItemFact {
  readonly id: string;
  readonly title: string;
  readonly status: WorkItemStatus;
  readonly issueType: string;
  readonly priority: number;
  readonly createdAt: string;
  readonly updatedAt: string;
  readonly closedAt: string | null;
  readonly doltRevision: string;
}

export interface WorkItemsObserved {
  readonly kind: 'observed';
  readonly beadPrefix: string;
  readonly doltRevision: string;
  readonly capturedAt: string;
  readonly items: readonly WorkItemFact[];
}

export interface WorkItemsUnknown {
  readonly kind: 'unknown';
  readonly reason: string;
}

export type WorkItemsResult = WorkItemsObserved | WorkItemsUnknown;

export interface ObserveWorkItemsInput {
  readonly repoRoot: string;
  readonly beadPrefix: string;
  readonly capturedAt: string;
  readonly runQuery?: (repoRoot: string, sql: string) => string;
}

const PREFIX_PATTERN = /^[a-z][a-z0-9]{0,15}$/;

function defaultRunQuery(repoRoot: string, sql: string): string {
  return execFileSync(
    'bd',
    ['--readonly', '--json', '-C', repoRoot, 'sql', sql],
    { encoding: 'utf8', maxBuffer: 256 * 1024 * 1024, stdio: ['ignore', 'pipe', 'pipe'] },
  );
}

function isWorkItemStatus(value: unknown): value is WorkItemStatus {
  return typeof value === 'string' && (WORK_ITEM_STATUSES as readonly string[]).includes(value);
}

interface RawRow {
  readonly revision?: unknown;
  readonly id?: unknown;
  readonly title?: unknown;
  readonly status?: unknown;
  readonly issue_type?: unknown;
  readonly priority?: unknown;
  readonly created_at?: unknown;
  readonly updated_at?: unknown;
  readonly closed_at?: unknown;
}

/**
 * Reads work items exclusively through `bd sql` against the live Dolt
 * database (POC-REQ-010/012). This module never opens the passive JSONL
 * export or any file derived from it — it shells a single read-only SQL
 * statement and parses its stdout.
 */
export function observeWorkItems(input: ObserveWorkItemsInput): WorkItemsResult {
  if (!PREFIX_PATTERN.test(input.beadPrefix)) {
    return { kind: 'unknown', reason: `configured bead-prefix is not a valid identifier: ${input.beadPrefix}` };
  }
  const runQuery = input.runQuery ?? defaultRunQuery;
  const sql =
    `SELECT dolt_hashof('HEAD') AS revision, id, title, status, issue_type, priority, ` +
    `created_at, updated_at, closed_at FROM issues WHERE id LIKE '${input.beadPrefix}-%' ORDER BY id`;

  let stdout: string;
  try {
    stdout = runQuery(input.repoRoot, sql);
  } catch {
    return {
      kind: 'unknown',
      reason: 'the Beads Dolt database was unreachable or unreadable during work-item observation',
    };
  }

  let rows: unknown;
  try {
    rows = JSON.parse(stdout);
  } catch {
    return { kind: 'unknown', reason: 'work-item observation returned a non-JSON response' };
  }
  if (!Array.isArray(rows)) {
    return { kind: 'unknown', reason: 'work-item observation returned an unexpected shape' };
  }
  if (rows.length === 0) {
    // Zero items under the registered prefix is a legitimate observed-empty
    // result, distinct from Unknown (POC-REQ-013) — but the revision still
    // has to be captured from a live query rather than left unrecorded.
    let revisionOnly: string;
    try {
      revisionOnly = runQuery(input.repoRoot, "SELECT dolt_hashof('HEAD') AS revision");
    } catch {
      return {
        kind: 'unknown',
        reason: 'the Beads Dolt database was unreachable or unreadable during revision capture',
      };
    }
    let revisionRows: unknown;
    try {
      revisionRows = JSON.parse(revisionOnly);
    } catch {
      return { kind: 'unknown', reason: 'revision capture returned a non-JSON response' };
    }
    const revisionValue = Array.isArray(revisionRows)
      ? (revisionRows[0] as RawRow | undefined)?.revision
      : undefined;
    if (typeof revisionValue !== 'string') {
      return { kind: 'unknown', reason: 'revision capture returned an unexpected shape' };
    }
    return {
      kind: 'observed',
      beadPrefix: input.beadPrefix,
      doltRevision: revisionValue,
      capturedAt: input.capturedAt,
      items: [],
    };
  }

  const items: WorkItemFact[] = [];
  let doltRevision: string | undefined;
  for (const raw of rows as readonly RawRow[]) {
    if (
      typeof raw.revision !== 'string' ||
      typeof raw.id !== 'string' ||
      typeof raw.title !== 'string' ||
      !isWorkItemStatus(raw.status) ||
      typeof raw.issue_type !== 'string' ||
      typeof raw.priority !== 'number' ||
      typeof raw.created_at !== 'string' ||
      typeof raw.updated_at !== 'string'
    ) {
      return { kind: 'unknown', reason: 'work-item observation returned a malformed row' };
    }
    if (!raw.id.startsWith(`${input.beadPrefix}-`)) {
      return { kind: 'unknown', reason: 'work-item observation returned an out-of-prefix identifier' };
    }
    doltRevision ??= raw.revision;
    if (raw.revision !== doltRevision) {
      return { kind: 'unknown', reason: 'work-item observation spanned more than one Dolt revision' };
    }
    items.push({
      id: raw.id,
      title: raw.title,
      status: raw.status,
      issueType: raw.issue_type,
      priority: raw.priority,
      createdAt: raw.created_at,
      updatedAt: raw.updated_at,
      closedAt: typeof raw.closed_at === 'string' ? raw.closed_at : null,
      doltRevision,
    });
  }

  return {
    kind: 'observed',
    beadPrefix: input.beadPrefix,
    doltRevision: doltRevision as string,
    capturedAt: input.capturedAt,
    items,
  };
}
