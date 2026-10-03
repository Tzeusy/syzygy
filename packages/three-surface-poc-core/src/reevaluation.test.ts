import { describe, expect, it } from 'vitest';

import { describeReevaluation, type EvaluatedClocks } from './reevaluation.js';

// Expected values are literals (syzygy-u05.2).
const OBSERVATORY = { buildRevision: 'syzygy-build', currentRevision: 'syzygy-build', commitsSinceBuild: 0 };
const FIRST: EvaluatedClocks = { evaluation: 'evaluation:one', clocks: { butlersHead: 'head-a', workingTreeDigest: 'tree-a', doltRevision: 'dolt-a' } };
const SECOND: EvaluatedClocks = { evaluation: 'evaluation:two', clocks: { butlersHead: 'head-b', workingTreeDigest: 'tree-a', doltRevision: null } };
const THIRD: EvaluatedClocks = { evaluation: 'evaluation:three', clocks: { butlersHead: 'head-b', workingTreeDigest: 'tree-c', doltRevision: 'dolt-c' } };

describe('a named re-evaluation result (pursuit N2)', () => {
  it('re-evaluates twice: two distinct identities, each naming the one it supersedes, the first result unchanged', () => {
    const initial = describeReevaluation({ prior: null, next: FIRST, projectChange: null, observatory: OBSERVATORY });
    const snapshot = JSON.stringify(initial);
    const once = describeReevaluation({ prior: FIRST, next: SECOND, projectChange: { changedSources: 3, addedSources: 1 }, observatory: { ...OBSERVATORY, currentRevision: 'syzygy-later', commitsSinceBuild: 2 } });
    const twice = describeReevaluation({ prior: SECOND, next: THIRD, projectChange: null, observatory: { ...OBSERVATORY, commitsSinceBuild: null, currentRevision: null } });
    expect([initial.evaluation, once.evaluation, twice.evaluation]).toEqual(['evaluation:one', 'evaluation:two', 'evaluation:three']);
    expect([initial.supersedes, once.supersedes, twice.supersedes]).toEqual([null, 'evaluation:one', 'evaluation:two']);
    expect(JSON.stringify(initial)).toBe(snapshot);
    expect(Object.isFrozen(initial) && Object.isFrozen(initial.clocks) && Object.isFrozen(initial.limbs.observatory)).toBe(true);
    expect(initial).toEqual({
      evaluation: 'evaluation:one', supersedes: null,
      clocks: { butlersHead: 'head-a', workingTreeDigest: 'tree-a', doltRevision: 'dolt-a' },
      moved: { butlersHead: 'unknown', workingTreeDigest: 'unknown', doltRevision: 'unknown' },
      limbs: { observedProject: { kind: 'no-prior' }, observatory: { buildRevision: 'syzygy-build', currentRevision: 'syzygy-build', commitsSinceBuild: 0 } },
    });
    expect(once.moved).toEqual({ butlersHead: 'moved', workingTreeDigest: 'unchanged', doltRevision: 'unknown' });
    expect(once.limbs).toEqual({
      observedProject: { kind: 'compared', changedSources: 3, addedSources: 1 },
      observatory: { buildRevision: 'syzygy-build', currentRevision: 'syzygy-later', commitsSinceBuild: 2 },
    });
    expect(twice.moved).toEqual({ butlersHead: 'unchanged', workingTreeDigest: 'moved', doltRevision: 'unknown' });
    expect(twice.limbs.observedProject).toEqual({ kind: 'unknown', reason: 'the revision comparison could not be read' });
    expect(twice.limbs.observatory.commitsSinceBuild).toBeNull();
  });

  it('never reuses an identity: a re-evaluation naming its prior identity is refused', () => {
    expect(() => describeReevaluation({ prior: FIRST, next: { ...SECOND, evaluation: 'evaluation:one' }, projectChange: null, observatory: OBSERVATORY }))
      .toThrow('a re-evaluation must mint a new identity; evaluation:one is the prior one');
  });

  it('reads the Dolt clock unchanged only when both sides observed it', () => {
    const same = describeReevaluation({ prior: THIRD, next: { evaluation: 'evaluation:four', clocks: THIRD.clocks }, projectChange: { changedSources: 0, addedSources: 0 }, observatory: OBSERVATORY });
    expect(same.moved).toEqual({ butlersHead: 'unchanged', workingTreeDigest: 'unchanged', doltRevision: 'unchanged' });
  });
});
