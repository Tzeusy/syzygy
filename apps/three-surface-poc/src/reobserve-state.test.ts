import { describe, expect, it } from 'vitest';

import { createReobserveState } from './reobserve-state.js';

interface Capture { readonly asOf: string; readonly revision: string; readonly changed: number; }
interface Model { readonly asOf: string; readonly revision: string; readonly changed: number; }

describe('re-observation state transition', () => {
  it('reuses wall-clock capture, atomically swaps a successful build, and single-flights concurrent calls', async () => {
    let observeCalls = 0;
    let release!: (capture: Capture) => void;
    const pending = new Promise<Capture>((resolve) => { release = resolve; });
    const state = createReobserveState<Capture, Model>({
      capture: { asOf: '2026-09-22T00:00:00Z', revision: 'rev-a', changed: 0 },
      model: { asOf: '2026-09-22T00:00:00Z', revision: 'rev-a', changed: 0 },
      observe: async () => { observeCalls += 1; return pending; },
      build: (capture) => ({ ...capture }),
    });
    expect(state.get()).toEqual({ asOf: '2026-09-22T00:00:00Z', revision: 'rev-a', changed: 0 });
    const first = state.reobserve();
    const second = state.reobserve();
    expect(observeCalls).toBe(1);
    expect(state.get().revision).toBe('rev-a');
    release({ asOf: '2026-09-22T00:01:00Z', revision: 'rev-b', changed: 2 });
    const [a, b] = await Promise.all([first, second]);
    expect(a).toEqual({ kind: 'reobserved', model: { asOf: '2026-09-22T00:01:00Z', revision: 'rev-b', changed: 2 } });
    expect(b).toEqual(a);
    expect(state.get().revision).toBe('rev-b');
  });

  it('preserves the prior model and never fabricates zero drift when capture or build fails', async () => {
    const state = createReobserveState<Capture, Model>({
      capture: { asOf: '2026-09-22T00:00:00Z', revision: 'rev-a', changed: 4 },
      model: { asOf: '2026-09-22T00:00:00Z', revision: 'rev-a', changed: 4 },
      observe: async () => { throw new Error('git probe failed'); },
      build: (capture) => ({ ...capture }),
    });
    await expect(state.reobserve()).resolves.toEqual({ kind: 'failed', reason: 'git probe failed' });
    expect(state.get()).toEqual({ asOf: '2026-09-22T00:00:00Z', revision: 'rev-a', changed: 4 });
  });
});

