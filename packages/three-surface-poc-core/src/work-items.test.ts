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
    expect(result.doltRevision).toBe('adpe9hi1llmdh05mr8aja5kagtu36eli');
    expect(result.items).toHaveLength(1);
    expect(result.items[0]?.doltRevision).toBe('adpe9hi1llmdh05mr8aja5kagtu36eli');
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
    expect(result.doltRevision).toBe('rev-empty');
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

  it('exercises the real subprocess path against a repository with no Beads database', () => {
    const result = observeWorkItems({
      repoRoot: '/tmp',
      beadPrefix: 'bu',
      capturedAt: '2026-08-30T00:00:00Z',
    });
    expect(result.kind).toBe('unknown');
  });
});
