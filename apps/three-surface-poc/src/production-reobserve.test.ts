import { execFileSync } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import type { PocEvaluationEvidence, PocModel } from '@syzygy/three-surface-poc-core';
import { afterEach, describe, expect, it, vi } from 'vitest';

import { createReobserveState } from './reobserve-state.js';
import { buildPocEvaluationEvidence, buildProductionPocModel, type PocRuntimeCapture } from './production-reobserve.js';
import { renderPolarisPage } from './polaris.js';
import { fixtureRepoWithGit } from './test-model-fixture.js';

const cleanups: string[] = [];
afterEach(() => {
  vi.useRealTimers();
  for (const directory of cleanups.splice(0)) rmSync(directory, { recursive: true, force: true });
});

const observerRoot = process.cwd();
const observerRevision = execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();

function capture(
  repositoryRevision: string,
  asOf: string,
  changedSources: number,
  workingTreeDigest = 'working-tree-a',
): PocRuntimeCapture {
  const evidence: PocEvaluationEvidence = {
    pinnedRevision: repositoryRevision,
    pinnedCommitterInstant: '2026-08-24T00:00:00Z',
    observationInstant: asOf,
    probe: {
      claimId: 'claim:currency-probe',
      evaluationId: `evaluation:pwb-currency-probe:${asOf}`,
      evaluationInstant: asOf,
      epistemic: { label: 'Observed', tier: 'report-fact', challenge: 'unchallenged' },
      pinnedRevision: repositoryRevision,
      currentRevision: repositoryRevision,
      changedSources,
      addedSources: 0,
    },
    currencyBounds: [],
  };
  return {
    repositoryRevision,
    observerRevision,
    workingTreeDigest,
    evidence,
  };
}

function workItemQuery(_repoRoot: string, sql: string): string {
  return sql.includes('WHERE id LIKE') ? JSON.stringify([]) : JSON.stringify([{ revision: 'dolt-fixture-revision' }]);
}

function build(repoRoot: string, stateDir: string, nextCapture: PocRuntimeCapture): PocModel {
  return buildProductionPocModel({
    capture: nextCapture,
    repoRoot,
    stateDir,
    observerRoot,
    runWorkItemQuery: workItemQuery,
  });
}

describe('production-owned capture-to-model re-observation seam', () => {
  it('keeps the production probe identity bound to the captured observation instant', () => {
    const evidence = buildPocEvaluationEvidence(
      '2026-09-23T00:00:00Z',
      'revision-pinned',
      '2026-08-24T00:00:00Z',
      { currentRevision: 'revision-current', changedSources: 2, addedSources: 1 },
    );
    expect(evidence.probe.evaluationId).toBe('evaluation:pwb-currency-probe:2026-09-23T00:00:00Z');
    expect(evidence.probe.evaluationInstant).toBe(evidence.observationInstant);
    expect(evidence.probe.currentRevision).toBe('revision-current');
  });

  it('keeps served bytes and asOf stable when the same capture is rebuilt across wall-clock instants', () => {
    const fixture = fixtureRepoWithGit(cleanups);
    const stateDir = mkdtempSync(join(tmpdir(), 'syzygy-production-reobserve-state-'));
    cleanups.push(stateDir);
    const observed = capture(fixture.revision, '2026-08-30T12:00:00Z', 0);
    vi.useFakeTimers();
    vi.setSystemTime(new Date('2026-09-22T00:00:00Z'));
    const first = build(fixture.repoRoot, stateDir, observed);
    vi.setSystemTime(new Date('2026-09-23T00:00:00Z'));
    const second = build(fixture.repoRoot, stateDir, observed);
    expect(second).toEqual(first);
    expect(second.evaluation.asOf).toBe('2026-08-30T12:00:00Z');
    expect(renderPolarisPage(second)).toBe(renderPolarisPage(first));
  });

  it('uses the production builder for an atomic successful swap with identity advancement and one in-flight observation', async () => {
    const fixture = fixtureRepoWithGit(cleanups);
    const stateDir = mkdtempSync(join(tmpdir(), 'syzygy-production-reobserve-state-'));
    cleanups.push(stateDir);
    const initialCapture = capture(fixture.revision, '2026-08-30T12:00:00Z', 0);
    const nextCapture = capture(fixture.revision, '2026-09-23T00:00:00Z', 3, 'working-tree-b');
    const initialModel = build(fixture.repoRoot, stateDir, initialCapture);
    let observeCalls = 0;
    let release!: (next: PocRuntimeCapture) => void;
    const pending = new Promise<PocRuntimeCapture>((resolve) => { release = resolve; });
    const state = createReobserveState<PocRuntimeCapture, PocModel>({
      capture: initialCapture,
      model: initialModel,
      observe: async () => { observeCalls += 1; return pending; },
      build: (next) => build(fixture.repoRoot, stateDir, next),
    });
    const first = state.reobserve();
    const second = state.reobserve();
    expect(observeCalls).toBe(1);
    expect(state.get().evaluation.asOf).toBe('2026-08-30T12:00:00Z');
    release(nextCapture);
    const [a, b] = await Promise.all([first, second]);
    expect(a).toEqual(b);
    expect(a.kind).toBe('reobserved');
    if (a.kind !== 'reobserved') throw new Error('expected successful production re-observation');
    expect(a.model.evaluation.asOf).toBe('2026-09-23T00:00:00Z');
    expect(a.model.evaluation.snapshot).not.toBe(initialModel.evaluation.snapshot);
    expect(a.model.evaluation.evidence.probe.evaluationId).toBe(nextCapture.evidence.probe.evaluationId);
    expect(a.model.evaluation.evidence.probe.changedSources).toBe(3);
    expect(state.get()).toBe(a.model);
    expect(state.getCapture()).toBe(nextCapture);
  });

  it('retains the prior production model and non-zero drift when the production build fails', async () => {
    const fixture = fixtureRepoWithGit(cleanups);
    const stateDir = mkdtempSync(join(tmpdir(), 'syzygy-production-reobserve-state-'));
    cleanups.push(stateDir);
    const initialCapture = capture(fixture.revision, '2026-08-30T12:00:00Z', 7);
    const nextCapture = capture(fixture.revision, '2026-09-23T00:00:00Z', 0, 'working-tree-b');
    const initialModel = build(fixture.repoRoot, stateDir, initialCapture);
    const state = createReobserveState<PocRuntimeCapture, PocModel>({
      capture: initialCapture,
      model: initialModel,
      observe: async () => nextCapture,
      build: (next) => {
        build(fixture.repoRoot, stateDir, next);
        throw new Error('production model build failed');
      },
    });
    await expect(state.reobserve()).resolves.toEqual({ kind: 'failed', reason: 'production model build failed' });
    expect(state.get()).toBe(initialModel);
    expect(state.getCapture()).toBe(initialCapture);
    expect(state.get().evaluation.evidence.probe.changedSources).toBe(7);
  });
});
