import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { describe, expect, it, vi } from 'vitest';

import { observeWorkItems } from './work-items.js';

function rowsResponse(rows: readonly Record<string, unknown>[]): string {
  return JSON.stringify(rows);
}

describe('work-items observer', () => {
  it('reads items via bd sql and stamps them with the Dolt revision read (POC-REQ-010)', () => {
    const calls: string[] = [];
    const runQuery = vi.fn((_repoRoot: string, sql: string) => {
      calls.push(sql);
      return rowsResponse([
        {
          revision: 'adpe9hi1llmdh05mr8aja5kagtu36eli',
          id: 'bu-000rb',
          title: 'Sample item',
          status: 'closed',
          issue_type: 'task',
          priority: 1,
          created_at: '2026-07-23T05:21:44Z',
          updated_at: '2026-07-24T01:25:16Z',
          closed_at: '2026-07-24T01:25:16Z',
        },
      ]);
    });

    const result = observeWorkItems({
      repoRoot: '/repo',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
      runQuery,
    });

    expect(result.kind).toBe('observed');
    if (result.kind !== 'observed') throw new Error('unreachable');
    expect(result.provenance).toEqual({
      kind: 'dolt-revision',
      source: 'Beads Dolt database (bu)',
      revision: 'adpe9hi1llmdh05mr8aja5kagtu36eli',
    });
    expect(result.items).toHaveLength(1);
    // The item takes the revision from the one record; it does not restate it.
    expect(Object.values(result.items[0] ?? {})).not.toContain('adpe9hi1llmdh05mr8aja5kagtu36eli');
    expect(calls[0]).toContain("dolt_hashof('HEAD')");
  });

  it('scopes the query to the registered bead-prefix and rejects out-of-prefix rows (POC-REQ-011)', () => {
    const runQuery = vi.fn((_repoRoot: string, sql: string) => {
      expect(sql).toContain("id LIKE 'bu-%'");
      return rowsResponse([
        {
          revision: 'rev1',
          id: 'other-1',
          title: 'wrong prefix',
          status: 'open',
          issue_type: 'task',
          priority: 1,
          created_at: '2026-08-30T00:00:00Z',
          updated_at: '2026-08-30T00:00:00Z',
          closed_at: null,
        },
      ]);
    });

    const result = observeWorkItems({
      repoRoot: '/repo',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
      runQuery,
    });
    expect(result.kind).toBe('unknown');
  });

  it('never touches the passive JSONL export or any derived file (POC-REQ-012)', () => {
    // Static prohibition: the module's own source is the population swept
    // (CC-SPEC oracle style) — it must import no filesystem API and name no
    // JSONL/export path, so its only possible work-item channel is the
    // injected/shelled SQL query.
    const modulePath = fileURLToPath(new URL('./work-items.ts', import.meta.url));
    const source = readFileSync(modulePath, 'utf8');
    expect(source).not.toMatch(/from ['"]node:fs['"]/);
    expect(source.toLowerCase()).not.toContain('.jsonl');
    expect(source.toLowerCase()).not.toContain('issues.export');

    const runQuery = vi.fn(
      () =>
        // deliberately disagrees with what a mutated export would say, to
        // prove the observer's only source is the injected query channel
        rowsResponse([
          {
            revision: 'rev-live',
            id: 'bu-divergent',
            title: 'from Dolt, not JSONL',
            status: 'in_progress',
            issue_type: 'task',
            priority: 2,
            created_at: '2026-08-30T00:00:00Z',
            updated_at: '2026-08-30T00:00:00Z',
            closed_at: null,
          },
        ]),
    );

    const result = observeWorkItems({
      repoRoot: '/repo',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
      runQuery,
    });

    expect(result.kind).toBe('observed');
    if (result.kind !== 'observed') throw new Error('unreachable');
    expect(result.items[0]?.status).toBe('in_progress');
  });

  it('renders Unknown with a named reason when the database is unreachable (POC-REQ-013)', () => {
    const runQuery = vi.fn(() => {
      throw new Error('connection refused');
    });
    const result = observeWorkItems({
      repoRoot: '/repo',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
      runQuery,
    });
    expect(result.kind).toBe('unknown');
    if (result.kind !== 'unknown') throw new Error('unreachable');
    expect(result.reason.length).toBeGreaterThan(0);
  });

  it('distinguishes an observed-empty result from Unknown', () => {
    const runQuery = vi.fn((_repoRoot: string, sql: string) =>
      sql.includes('WHERE id LIKE')
        ? rowsResponse([])
        : rowsResponse([{ revision: 'rev-empty' }]),
    );
    const result = observeWorkItems({
      repoRoot: '/repo',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
      runQuery,
    });
    expect(result.kind).toBe('observed');
    if (result.kind !== 'observed') throw new Error('unreachable');
    expect(result.items).toEqual([]);
    expect(result.provenance.revision).toBe('rev-empty');
  });

  it('rejects a malformed configured prefix rather than shelling an unsafe query', () => {
    const runQuery = vi.fn();
    const result = observeWorkItems({
      repoRoot: '/repo',
      beadPrefix: "bu'; DROP TABLE issues; --",
      capturedAt: '2026-08-30T00:00:00Z',
      runQuery,
    });
    expect(result.kind).toBe('unknown');
    expect(runQuery).not.toHaveBeenCalled();
  });

  describe('SEC-5: work-item titles are withheld, never read (owner answer 2026-10-20, syzygy-jytt)', () => {
    // Literals, typed here: RFC2-24's `excluded-content` route, and the
    // columns the observation may read.
    const WITHHELD = {
      label: 'Unknown',
      closedReason: 'excluded-content',
      resolutionRoutes: [{ reason: 'excluded-content', route: 'Policy change by the owner, or accept the exclusion', actor: 'owner', verb: 'decide', target: 'policy' }],
    };
    const ITEM_ROW = {
      revision: 'rev-t', id: 'bu-t1', status: 'open', issue_type: 'task', priority: 2,
      created_at: '2026-08-30T00:00:00Z', updated_at: '2026-08-30T01:00:00Z', closed_at: null,
    };

    function observe(rows: readonly Record<string, unknown>[], calls: string[] = []) {
      return observeWorkItems({
        repoRoot: '/repo',
        beadPrefix: 'bu',
        capturedAt: '2026-08-30T02:00:00Z',
        runQuery: (_root, sql) => {
          calls.push(sql);
          return sql.includes('WHERE id LIKE') ? rowsResponse(rows) : rowsResponse([{ revision: 'rev-empty' }]);
        },
      });
    }

    it('selects exactly the eight non-free-text columns, and never the title', () => {
      const calls: string[] = [];
      observe([ITEM_ROW], calls);
      const columns = /^SELECT (.*) FROM issues /.exec(calls[0] ?? '')?.[1]?.split(', ');
      expect(columns).toEqual(["dolt_hashof('HEAD') AS revision", 'id', 'status', 'issue_type', 'priority', 'created_at', 'updated_at', 'closed_at']);
      expect(calls[0]).not.toMatch(/\btitle\b/i);
    });

    it('admits a row with no title, and copies no title from a row that carries one', () => {
      const untitled = observe([ITEM_ROW]);
      expect(untitled.kind).toBe('observed');
      const titled = observe([{ ...ITEM_ROW, title: 'Unclassified free text qz7k' }]);
      if (titled.kind !== 'observed') throw new Error('unreachable');
      expect(Object.keys(titled.items[0] ?? {}).sort()).toEqual(['closedAt', 'createdAt', 'governedBy', 'id', 'issueType', 'priority', 'status', 'updatedAt']);
      expect(JSON.stringify(titled)).not.toContain('qz7k');
    });

    it('states the withheld title once on the observation, as excluded-content with its route', () => {
      const observed = observe([ITEM_ROW]);
      const empty = observe([]);
      if (observed.kind !== 'observed' || empty.kind !== 'observed') throw new Error('unreachable');
      expect(observed.titles).toEqual(WITHHELD);
      expect(empty.titles).toEqual(WITHHELD);
    });
  });

  it('exercises the real subprocess path against a repository with no Beads database', () => {
    const result = observeWorkItems({
      repoRoot: '/tmp',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });
});
