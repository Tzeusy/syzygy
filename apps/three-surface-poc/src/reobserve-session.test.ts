import { PassThrough } from 'node:stream';

import { describe, expect, it } from 'vitest';

import type { PocModel } from '@syzygy/three-surface-poc-core';

import type { PocRuntimeCapture } from './production-reobserve.js';
import { createReobserveSession, type ReobserveSessionOptions } from './reobserve-session.js';

// syzygy-5oi3: the main.ts re-evaluation wiring, extracted and tested.
// Expected identities are literals.

function capture(revision: string, at: string): PocRuntimeCapture {
  return {
    repositoryRevision: revision,
    observerRevision: 'observer-a',
    workingTreeDigest: 'tree-a',
    evidence: {
      pinnedRevision: revision,
      pinnedCommitterInstant: '2026-10-01T00:00:00Z',
      observationInstant: at,
      probe: {
        claimId: 'claim:currency-probe',
        evaluationId: `evaluation:pwb-currency-probe:${at}`,
        evaluationInstant: at,
        epistemic: { label: 'Observed', tier: 'report-fact', challenge: 'unchallenged' },
        pinnedRevision: revision,
        currentRevision: revision,
        changedSources: 0,
        addedSources: 0,
      },
      currencyBounds: [],
    },
  };
}

function harness(overrides: Partial<ReobserveSessionOptions> = {}) {
  const builds: PocRuntimeCapture[] = [];
  let observeCalls = 0;
  let release: ((next: PocRuntimeCapture) => void) | undefined;
  const options: ReobserveSessionOptions = {
    capture: capture('head-a', '2026-10-04T01:00:00Z'),
    build: (c) => {
      builds.push(c);
      return {
        evaluation: { snapshot: `snap:${c.repositoryRevision}`, asOf: c.evidence.observationInstant, evidence: c.evidence },
        project: { revision: c.repositoryRevision },
        workItems: { kind: 'observed', doltRevision: `dolt:${builds.length}` },
      } as unknown as PocModel;
    },
    observe: () => { observeCalls += 1; return new Promise((resolve) => { release = resolve; }); },
    observeHorizon: () => ({ currentRevision: 'head-a', changedSources: 0, addedSources: 0 }),
    observeRevisionChange: () => ({ changedSources: 1, addedSources: 0 }),
    observeObservatory: () => ({ buildRevision: 'observer-a', currentRevision: 'observer-a', commitsSinceBuild: 0 }),
    now: () => '2026-10-04T02:00:00Z',
    ...overrides,
  };
  return { session: createReobserveSession(options), builds, observeCalls: () => observeCalls, release: (next: PocRuntimeCapture) => release?.(next) };
}

describe('re-evaluation session', () => {
  it('after a materialize, the served model, the latest re-evaluation and the next supersedes all name the rebuilt evaluation', async () => {
    const h = harness();
    expect(h.session.latest().evaluation).toBe('snap:head-a|observed:2026-10-04T01:00:00Z');
    h.session.afterMaterialized();
    expect(h.session.model().evaluation.asOf).toBe('2026-10-04T02:00:00Z');
    expect(h.session.latest()).toMatchObject({
      evaluation: 'snap:head-a|observed:2026-10-04T02:00:00Z',
      supersedes: 'snap:head-a|observed:2026-10-04T01:00:00Z',
      clocks: { butlersHead: 'head-a', doltRevision: 'dolt:2' },
      moved: { butlersHead: 'unchanged', doltRevision: 'moved' },
    });
    expect(h.session.model().evaluation.evidence.probe.evaluationId).toBe('evaluation:pwb-currency-probe:2026-10-04T02:00:00Z');
    const next = h.session.reobserve();
    h.release(capture('head-b', '2026-10-04T03:00:00Z'));
    const result = await next;
    expect(result).toMatchObject({ kind: 'reobserved', reevaluation: { evaluation: 'snap:head-b|observed:2026-10-04T03:00:00Z', supersedes: 'snap:head-a|observed:2026-10-04T02:00:00Z' } });
  });

  it('single-flights concurrent requests: one observation, one named re-evaluation, both callers get it', async () => {
    const h = harness();
    const first = h.session.reobserve();
    const second = h.session.reobserve();
    expect(first).toBe(second);
    h.release(capture('head-b', '2026-10-04T03:00:00Z'));
    const [a, b] = await Promise.all([first, second]);
    expect(h.observeCalls()).toBe(1);
    expect(a).toEqual(b);
    expect(a).toMatchObject({ kind: 'reobserved', reevaluation: { supersedes: 'snap:head-a|observed:2026-10-04T01:00:00Z' } });
    expect(h.session.latest().supersedes).toBe('snap:head-a|observed:2026-10-04T01:00:00Z');
  });

  it('a failed rebuild after materialize swaps nothing', () => {
    let calls = 0;
    const h = harness({ build: (c) => {
      calls += 1;
      if (calls > 1) throw new Error('build failed');
      return { evaluation: { snapshot: 'snap', asOf: c.evidence.observationInstant }, project: { revision: c.repositoryRevision }, workItems: { kind: 'unknown' } } as unknown as PocModel;
    } });
    const before = { model: h.session.model(), latest: h.session.latest() };
    expect(() => h.session.afterMaterialized()).toThrow('build failed');
    expect(h.session.model()).toBe(before.model);
    expect(h.session.latest()).toBe(before.latest);
  });

  it('re-observes again after a completed re-observation: a second observation, and the supersedes chain continues', async () => {
    const h = harness();
    const first = h.session.reobserve();
    h.release(capture('head-b', '2026-10-04T03:00:00Z'));
    await first;
    const second = h.session.reobserve();
    expect(second).not.toBe(first);
    expect(h.observeCalls()).toBe(2);
    h.release(capture('head-c', '2026-10-04T04:00:00Z'));
    expect(await second).toMatchObject({ kind: 'reobserved', reevaluation: { evaluation: 'snap:head-c|observed:2026-10-04T04:00:00Z', supersedes: 'snap:head-b|observed:2026-10-04T03:00:00Z' } });
    expect(h.session.latest().evaluation).toBe('snap:head-c|observed:2026-10-04T04:00:00Z');
  });

  it('a rebuild after materialize that cannot be named swaps nothing', () => {
    let reads = 0;
    const h = harness({ observeObservatory: () => {
      reads += 1;
      if (reads > 1) throw new Error('observatory unreadable');
      return { buildRevision: 'observer-a', currentRevision: 'observer-a', commitsSinceBuild: 0 };
    } });
    const before = { model: h.session.model(), latest: h.session.latest() };
    expect(() => h.session.afterMaterialized()).toThrow('observatory unreadable');
    expect(h.session.model()).toBe(before.model);
    expect(h.session.latest()).toBe(before.latest);
  });

  it('attaches the Enter console only when --watch is on', async () => {
    const off = harness();
    const offInput = new PassThrough();
    expect(off.session.startConsole(false, { input: offInput, output: new PassThrough() })).toBeUndefined();
    offInput.write('\n');
    offInput.end();
    expect(off.observeCalls()).toBe(0);

    const on = harness();
    const input = new PassThrough();
    const done = on.session.startConsole(true, { input, output: new PassThrough() });
    expect(done).toBeInstanceOf(Promise);
    input.write('\n');
    await new Promise<void>((resolve) => { input.once('end', resolve); input.end(); });
    for (let i = 0; i < 5 && on.observeCalls() === 0; i += 1) await Promise.resolve();
    expect(on.observeCalls()).toBe(1);
    on.release(capture('head-b', '2026-10-04T03:00:00Z'));
    await done;
  });
});
