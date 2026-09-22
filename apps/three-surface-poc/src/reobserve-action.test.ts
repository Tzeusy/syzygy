import { afterEach, describe, expect, it } from 'vitest';
import type { RouteContext } from '@syzygy/cap1-daemon';

import { reobserveRoutes, REOBSERVE_HUMAN_PATH, type ReobserveResult } from './reobserve-action.js';

const cleanup: (() => void)[] = [];
afterEach(() => {
  for (const close of cleanup.splice(0)) close();
});

function route() {
  const candidate = reobserveRoutes({ reobserve: async () => ({ kind: 'reobserved', evaluation: 'evaluation:new' }) }).find((item) => item.path === REOBSERVE_HUMAN_PATH);
  if (candidate === undefined) throw new Error('reobserve route missing');
  return candidate;
}

function context(headers: Record<string, string> = {}): RouteContext {
  return { request: { method: 'POST', path: REOBSERVE_HUMAN_PATH, query: new URLSearchParams(), headers } };
}

describe('human-triggered re-observation route', () => {
  it('single-flights concurrent requests and swaps only after a complete success', async () => {
    let calls = 0;
    let release!: (result: ReobserveResult) => void;
    const pending = new Promise<ReobserveResult>((resolve) => { release = resolve; });
    const candidate = reobserveRoutes({ reobserve: async () => { calls += 1; return pending; } }).find((item) => item.path === REOBSERVE_HUMAN_PATH);
    if (candidate === undefined) throw new Error('reobserve route missing');
    const first = candidate.handle(context({ host: '127.0.0.1:1' }));
    const second = candidate.handle(context({ host: '127.0.0.1:1' }));
    release({ kind: 'reobserved', evaluation: 'evaluation:complete' });
    const [a, b] = await Promise.all([first, second]);
    expect(calls).toBe(1);
    expect(a).toMatchObject({ status: 200 });
    expect(b).toMatchObject({ status: 200 });
    expect(a.body).toContain('evaluation:complete');
  });

  it('preserves a named failure and refuses cross-origin requests', async () => {
    const candidate = reobserveRoutes({ reobserve: async () => ({ kind: 'failed', reason: 'observation refused' }) }).find((item) => item.path === REOBSERVE_HUMAN_PATH);
    if (candidate === undefined) throw new Error('reobserve route missing');
    const failure = await candidate.handle(context({ host: '127.0.0.1:1' }));
    expect(failure).toMatchObject({ status: 502 });
    expect(failure.body).toContain('observation refused');
    const refused = await candidate.handle(context({ host: 'poc.attacker.invalid', origin: 'http://poc.attacker.invalid' }));
    expect(refused).toMatchObject({ status: 403 });
  });
});
