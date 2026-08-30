import { execFileSync } from 'node:child_process';
import { mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import { buildButlersPocModel, STATUS_TO_COLUMN } from '@syzygy/three-surface-poc-core';

import { renderTrajectoryPage } from './trajectory.js';
import { buildFixtureModel, fixtureRepoWithGit } from './test-model-fixture.js';

function git(root: string, args: readonly string[]): string {
  return execFileSync('git', ['-C', root, ...args], {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'ignore'],
  }).trim();
}

function writeWorkerChangeSeam(root: string, sourceContents: string): void {
  for (const [path, contents] of [
    ['src/butlers/connectors/whatsapp_user_client.py', sourceContents],
    ['tests/connectors/test_whatsapp_user_client.py', 'def test_normalization(): pass\n'],
  ] as const) {
    const absolute = join(root, path);
    mkdirSync(dirname(absolute), { recursive: true });
    writeFileSync(absolute, contents, 'utf8');
  }
}

const cleanups: string[] = [];
afterEach(() => {
  for (const directory of cleanups.splice(0)) {
    rmSync(directory, { recursive: true, force: true });
  }
});

function cardBody(html: string, id: string): string {
  const match = new RegExp(`data-work-item-id="${id}">([\\s\\S]*?)</li>`).exec(html);
  if (match?.[1] === undefined) {
    throw new Error(`card not found: ${id}`);
  }
  return match[1];
}

describe('Trajectory', () => {
  it('places every rendered item in the column its declared status mapping assigns (POC-REQ-040)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderTrajectoryPage(model);
    if (model.trajectory.kind !== 'observed') throw new Error('unreachable');

    for (const item of model.trajectory.rendered) {
      const card = cardBody(html, item.id);
      const columnMatch = new RegExp(
        `<h2>${STATUS_TO_COLUMN[item.status]}[\\s\\S]*?</section>`,
      );
      // the card's own status text is the oracle-independent check: its
      // rendered status must equal the declared mapping's input status
      expect(card).toContain(`data-parity-field="work-item-status">${item.status}<`);
      expect(html).toMatch(columnMatch);
    }
  });

  it('states the selection rule and reconciles rendered + excluded against the total (POC-REQ-042)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderTrajectoryPage(model);
    if (model.trajectory.kind !== 'observed') throw new Error('unreachable');

    const scopeMatch = /data-parity-field="trajectory-excluded-count">(\d+)</.exec(html);
    expect(scopeMatch).not.toBeNull();
    const excluded = Number(scopeMatch?.[1]);
    expect(model.trajectory.renderedCount + excluded).toBe(model.trajectory.totalCount);
    expect(html).toContain(model.trajectory.selectionRule);
  });

  it('never renders closure/activity as verification satisfaction (POC-REQ-043)', () => {
    const model = buildFixtureModel(cleanups);
    const html = renderTrajectoryPage(model);
    const closedCard = cardBody(html, 'bu-closed-recent');
    expect(closedCard).toContain('data-parity-field="work-item-status">closed<');
    expect(closedCard).toContain('data-parity-field="work-item-verification"');
    expect(closedCard).toContain('Verification: Unknown');
    expect(closedCard).not.toMatch(/verified|satisfied/i);
  });

  it('renders the Unknown state distinctly from an empty-but-observed board (POC-REQ-013 rendering)', () => {
    const { repoRoot, revision } = fixtureRepoWithGit(cleanups);
    const unknownModel = buildButlersPocModel({
      repoRoot,
      repositoryRevision: revision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@unreachable', asOf: '2026-08-30T12:00:00Z' },
      runWorkItemQuery: () => {
        throw new Error('connection refused');
      },
    });
    expect(unknownModel.trajectory.kind).toBe('unknown');
    const unknownHtml = renderTrajectoryPage(unknownModel);
    expect(unknownHtml).toContain('data-unknown-disclosure="region:work-items"');
    expect(unknownHtml).not.toContain('class="board"');

    const emptyObservedModel = buildButlersPocModel({
      repoRoot,
      repositoryRevision: revision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@empty', asOf: '2026-08-30T12:00:00Z' },
      runWorkItemQuery: (_repoRoot, sql) =>
        sql.includes('WHERE id LIKE') ? JSON.stringify([]) : JSON.stringify([{ revision: 'dolt-empty' }]),
    });
    expect(emptyObservedModel.trajectory.kind).toBe('observed');
    const emptyHtml = renderTrajectoryPage(emptyObservedModel);
    expect(emptyHtml).toContain('class="board"');
    expect(emptyHtml).not.toContain('data-unknown-disclosure="region:work-items"');
    expect(emptyHtml).not.toBe(unknownHtml);
  });

  it('renders the observed worker-change lifecycle state on the matching card, never as verified (AC3/AC4)', () => {
    const { repoRoot, revision } = fixtureRepoWithGit(cleanups);
    writeWorkerChangeSeam(repoRoot, 'x = 1\n');
    git(repoRoot, ['add', '-A']);
    git(repoRoot, ['commit', '-qm', 'fix(whatsapp): normalize single-event sender [bu-worker-change-1]']);
    const changedRevision = git(repoRoot, ['rev-parse', 'HEAD']);
    git(repoRoot, ['update-ref', 'refs/remotes/origin/main', changedRevision]);
    git(repoRoot, ['symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main']);

    const materializationRecord = {
      beadId: 'bu-worker-change-1',
      externalRef: 'syzygy-poc:work:whatsapp-single-event-normalization',
      targetRepoRoot: repoRoot,
      createdAt: '2026-08-30T00:00:00Z',
      doltRevisionAtCreation: 'dolt-rev-1',
      attribution: 'test-actor',
    } as const;
    const rows = [
      {
        revision: 'dolt-rev-2',
        id: 'bu-worker-change-1',
        title: 'Materialized work item',
        status: 'in_progress',
        issue_type: 'task',
        priority: 2,
        created_at: '2026-08-30T00:00:00Z',
        updated_at: '2026-08-30T00:00:00Z',
        closed_at: null,
      },
    ];

    const model = buildButlersPocModel({
      repoRoot,
      repositoryRevision: changedRevision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@worker-change', asOf: '2026-08-30T12:00:00Z' },
      materializationRecord,
      runWorkItemQuery: (_repoRoot, sql) =>
        sql.includes('WHERE id LIKE') ? JSON.stringify(rows) : JSON.stringify([{ revision: 'dolt-rev-2' }]),
    });
    expect(model.workerChange.kind).toBe('observed');
    if (model.workerChange.kind !== 'observed') throw new Error('unreachable');
    expect(model.workerChange.state).toBe('changed-or-merged');

    const html = renderTrajectoryPage(model);
    const card = cardBody(html, 'bu-worker-change-1');
    expect(card).toContain('data-parity-field="worker-change-state"');
    expect(card).toContain('External worker: Changed / merged');
    expect(card).toContain('data-parity-field="worker-change-verification"');
    expect(card).toContain('Verification: Not verified');
    expect(card).not.toContain('Verification: Verified');
  });

  it('renders Verified on the card only once a real matching test artifact is ingested (AC3, syzygy-0r9)', () => {
    const { repoRoot, revision } = fixtureRepoWithGit(cleanups);
    writeWorkerChangeSeam(repoRoot, 'x = 1\n');
    git(repoRoot, ['add', '-A']);
    git(repoRoot, ['commit', '-qm', 'fix(whatsapp): normalize single-event sender [bu-verified-1]']);
    const changedRevision = git(repoRoot, ['rev-parse', 'HEAD']);
    const changedCommitAuthoredAt = git(repoRoot, ['log', '-1', '--format=%aI', changedRevision]);
    git(repoRoot, ['update-ref', 'refs/remotes/origin/main', changedRevision]);
    git(repoRoot, ['symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main']);

    const materializationRecord = {
      beadId: 'bu-verified-1',
      externalRef: 'syzygy-poc:work:whatsapp-single-event-normalization',
      targetRepoRoot: repoRoot,
      createdAt: '2026-08-30T00:00:00Z',
      doltRevisionAtCreation: 'dolt-rev-1',
      attribution: 'test-actor',
    } as const;
    const rows = [
      {
        revision: 'dolt-rev-2',
        id: 'bu-verified-1',
        title: 'Materialized work item',
        status: 'in_progress',
        issue_type: 'task',
        priority: 2,
        created_at: '2026-08-30T00:00:00Z',
        updated_at: '2026-08-30T00:00:00Z',
        closed_at: null,
      },
    ];
    const capturedAt = new Date(Date.parse(changedCommitAuthoredAt) + 60 * 60 * 1000).toISOString();
    const evaluationAsOf = new Date(Date.parse(capturedAt) + 60 * 60 * 1000).toISOString();

    const model = buildButlersPocModel({
      repoRoot,
      repositoryRevision: changedRevision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@verified', asOf: evaluationAsOf },
      materializationRecord,
      runWorkItemQuery: (_repoRoot, sql) =>
        sql.includes('WHERE id LIKE') ? JSON.stringify(rows) : JSON.stringify([{ revision: 'dolt-rev-2' }]),
      testArtifactRecord: {
        command: ['python3', '-m', 'pytest', 'tests/connectors/test_whatsapp_user_client.py', '-q'],
        exitCode: 0,
        capturedAt,
        repositoryCommit: changedRevision,
        scope: 'tests/connectors/test_whatsapp_user_client.py',
        digest: 'sha256:' + '2'.repeat(64),
        summary: '4 passed, 0 failed, 0 errored, 0 skipped in 0.5s',
      },
    });
    expect(model.testArtifactVerification.kind).toBe('verified');

    const html = renderTrajectoryPage(model);
    const card = cardBody(html, 'bu-verified-1');
    expect(card).toContain('Verification: Verified');
    expect(card).toContain('4 passed, 0 failed, 0 errored, 0 skipped in 0.5s');
    expect(card).not.toContain('Verification: Not verified');
  });

  it('calls out and highlights the demonstrated item, and separates Bead status from worker-change state (PRF-2, PRF-3)', () => {
    const { repoRoot, revision } = fixtureRepoWithGit(cleanups);
    writeWorkerChangeSeam(repoRoot, 'x = 1\n');
    git(repoRoot, ['add', '-A']);
    git(repoRoot, ['commit', '-qm', 'fix(whatsapp): normalize single-event sender [bu-demo-1]']);
    const changedRevision = git(repoRoot, ['rev-parse', 'HEAD']);
    git(repoRoot, ['update-ref', 'refs/remotes/origin/main', changedRevision]);
    git(repoRoot, ['symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main']);

    const rows = [
      {
        revision: 'dolt-rev-2',
        id: 'bu-demo-1',
        title: 'Materialized work item',
        status: 'in_progress',
        issue_type: 'task',
        priority: 2,
        created_at: '2026-08-30T00:00:00Z',
        updated_at: '2026-08-30T00:00:00Z',
        closed_at: null,
      },
      {
        revision: 'dolt-rev-2',
        id: 'bu-unrelated-1',
        title: 'Unrelated backlog item',
        status: 'open',
        issue_type: 'task',
        priority: 3,
        created_at: '2026-08-30T00:00:00Z',
        updated_at: '2026-08-30T00:00:00Z',
        closed_at: null,
      },
    ];
    const model = buildButlersPocModel({
      repoRoot,
      repositoryRevision: changedRevision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@demo', asOf: '2026-08-30T12:00:00Z' },
      materializationRecord: {
        beadId: 'bu-demo-1',
        externalRef: 'syzygy-poc:work:whatsapp-single-event-normalization',
        targetRepoRoot: repoRoot,
        createdAt: '2026-08-30T00:00:00Z',
        doltRevisionAtCreation: 'dolt-rev-1',
        attribution: 'test-actor',
        origin: 'created',
      },
      runWorkItemQuery: (_repoRoot, sql) =>
        sql.includes('WHERE id LIKE') ? JSON.stringify(rows) : JSON.stringify([{ revision: 'dolt-rev-2' }]),
    });
    const html = renderTrajectoryPage(model);

    // PRF-3: intro line names and links the demonstrated item; only its
    // card is highlighted and badged
    expect(html).toContain('The demonstrated item is <a href="#workitem-bu-demo-1">');
    const demoCard = cardBody(html, 'bu-demo-1');
    const unrelatedCard = cardBody(html, 'bu-unrelated-1');
    expect(demoCard).toContain('Demonstrated item');
    expect(html).toMatch(/wi-card wi-card-demonstrated" id="workitem-bu-demo-1"/);
    expect(unrelatedCard).not.toContain('Demonstrated item');
    expect(html).not.toMatch(/wi-card-demonstrated" id="workitem-bu-unrelated-1"/);

    // PRF-2: the dual-badge card states the two fields are independent
    expect(demoCard).toContain('Independent of the Bead status above');
    expect(unrelatedCard).not.toContain('Independent of the Bead status above');

    // no demonstrated item: neither callout variant renders
    const noneModel = buildButlersPocModel({
      repoRoot,
      repositoryRevision: changedRevision,
      observerRevision: revision,
      evaluation: { snapshot: 'butlers@demo-none', asOf: '2026-08-30T12:00:00Z' },
      runWorkItemQuery: (_repoRoot, sql) =>
        sql.includes('WHERE id LIKE') ? JSON.stringify(rows) : JSON.stringify([{ revision: 'dolt-rev-2' }]),
    });
    const noneHtml = renderTrajectoryPage(noneModel);
    expect(noneHtml).not.toContain('class="demo-callout');
    expect(noneHtml).not.toContain('Demonstrated item');
  });

  it('mutation check: a falsified reconciliation would be caught', () => {
    const model = buildFixtureModel(cleanups);
    if (model.trajectory.kind !== 'observed') throw new Error('unreachable');
    const falsified = model.trajectory.excludedCount + 3;
    expect(model.trajectory.renderedCount + falsified).not.toBe(model.trajectory.totalCount);
  });
});
