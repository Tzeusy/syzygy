// Fresh-checkout exit polarity (PWB-LIVE-14): every recorded invariant
// flips the verdict on its own. The healthy input is spelled out by hand;
// each case mutates exactly one field and names the one invariant that
// must fail — a table, so a new invariant without a row is a visible gap
// (the sweep at the end checks the table covers the exported list).

import { describe, expect, it } from 'vitest';

import { FRESH_CHECKOUT_INVARIANTS, freshCheckoutVerdict, type FreshCheckoutInvariant, type FreshCheckoutInvariants } from './fresh-checkout-verdict.js';

const REVISION = 'a'.repeat(40);

function healthy(): FreshCheckoutInvariants {
  return {
    cloneHeadMatchesSource: true,
    installExitCode: 0,
    buildExitCode: 0,
    testExitCode: 0,
    refusedStatus: 401,
    machineStatus: 200,
    humanRouteStatuses: [200, 200, 200, 200],
    sourceRouteStatus: 200,
    daemonObservedRevision: REVISION,
    modelRevision: REVISION,
    shapeKind: 'observed',
    authorityAdmits: true,
    parity: { humanClaimTuples: 390, humanDistinctClaimIds: 389, humanTuplesMismatchingMachine: 0, machinePresentedClaimIds: 389, machineDistinctClaimIds: 389, machineIdsAbsentFromHuman: 0, humanIdsAbsentFromMachine: 0 },
    limitBreaches: 0,
    preflightReady: true,
    daemonExitCode: 0,
    daemonStderr: '',
    evidenceWritten: true,
  };
}

const COUNTEREXAMPLES: readonly { readonly name: string; readonly invariant: FreshCheckoutInvariant; readonly mutate: (base: FreshCheckoutInvariants) => FreshCheckoutInvariants }[] = [
  { name: 'clone head differs from the source head', invariant: 'clone-head-matches-source', mutate: (b) => ({ ...b, cloneHeadMatchesSource: false }) },
  { name: 'npm ci failed', invariant: 'install', mutate: (b) => ({ ...b, installExitCode: 1 }) },
  { name: 'build failed', invariant: 'build', mutate: (b) => ({ ...b, buildExitCode: 2 }) },
  { name: 'tests failed', invariant: 'test', mutate: (b) => ({ ...b, testExitCode: 1 }) },
  { name: 'machine endpoint served without a credential', invariant: 'machine-refused-without-credential', mutate: (b) => ({ ...b, refusedStatus: 200 }) },
  { name: 'machine endpoint refused with a status other than 401', invariant: 'machine-refused-without-credential', mutate: (b) => ({ ...b, refusedStatus: 403 }) },
  { name: 'machine endpoint refused the credential', invariant: 'machine-served-with-credential', mutate: (b) => ({ ...b, machineStatus: 403 }) },
  { name: 'one human route failed', invariant: 'human-routes-served', mutate: (b) => ({ ...b, humanRouteStatuses: [200, 500, 200, 200] }) },
  { name: 'no human route was fetched at all', invariant: 'human-routes-served', mutate: (b) => ({ ...b, humanRouteStatuses: [] }) },
  { name: 'the exact-source route failed', invariant: 'source-route-served', mutate: (b) => ({ ...b, sourceRouteStatus: 404 }) },
  { name: 'the daemon observed a different Butlers revision than the model carries', invariant: 'butlers-revision-matches-model', mutate: (b) => ({ ...b, daemonObservedRevision: 'b'.repeat(40) }) },
  { name: 'the observed revision is not a revision', invariant: 'butlers-revision-matches-model', mutate: (b) => ({ ...b, daemonObservedRevision: 'unknown', modelRevision: 'unknown' }) },
  { name: 'the shape was not observed', invariant: 'shape-observed', mutate: (b) => ({ ...b, shapeKind: 'not-admitted' }) },
  { name: 'the authority refused', invariant: 'authority-admits', mutate: (b) => ({ ...b, authorityAdmits: false }) },
  { name: 'no authority was evaluated', invariant: 'authority-admits', mutate: (b) => ({ ...b, authorityAdmits: null }) },
  { name: 'a rendered tuple whose state differs from the machine claim', invariant: 'parity', mutate: (b) => ({ ...b, parity: { ...b.parity, humanTuplesMismatchingMachine: 1 } }) },
  { name: 'the page presents fewer distinct claims than the machine answer', invariant: 'parity', mutate: (b) => ({ ...b, parity: { ...b.parity, humanDistinctClaimIds: 388 } }) },
  { name: 'a duplicate machine claim id', invariant: 'parity', mutate: (b) => ({ ...b, parity: { ...b.parity, machinePresentedClaimIds: 390 } }) },
  { name: 'a machine id absent from the page', invariant: 'parity', mutate: (b) => ({ ...b, parity: { ...b.parity, machineIdsAbsentFromHuman: 1 } }) },
  { name: 'a human id absent from the machine answer', invariant: 'parity', mutate: (b) => ({ ...b, parity: { ...b.parity, humanIdsAbsentFromMachine: 1 } }) },
  { name: 'both channels empty', invariant: 'parity', mutate: (b) => ({ ...b, parity: { humanClaimTuples: 0, humanDistinctClaimIds: 0, humanTuplesMismatchingMachine: 0, machinePresentedClaimIds: 0, machineDistinctClaimIds: 0, machineIdsAbsentFromHuman: 0, humanIdsAbsentFromMachine: 0 } }) },
  { name: 'a limit breach', invariant: 'limit-breaches', mutate: (b) => ({ ...b, limitBreaches: 1 }) },
  { name: 'the preflight is not ready', invariant: 'preflight-ready', mutate: (b) => ({ ...b, preflightReady: false }) },
  { name: 'the daemon exited nonzero', invariant: 'daemon-exit-clean', mutate: (b) => ({ ...b, daemonExitCode: 1 }) },
  { name: 'the daemon was killed (no exit code)', invariant: 'daemon-exit-clean', mutate: (b) => ({ ...b, daemonExitCode: null }) },
  { name: 'the daemon wrote to stderr', invariant: 'daemon-exit-clean', mutate: (b) => ({ ...b, daemonStderr: 'syzygy POC: observation failed\n' }) },
  { name: 'the evidence record was not written', invariant: 'evidence-written', mutate: (b) => ({ ...b, evidenceWritten: false }) },
];

describe('freshCheckoutVerdict', () => {
  it('is healthy only when every invariant holds', () => {
    expect(freshCheckoutVerdict(healthy())).toEqual({ healthy: true, failed: [] });
  });

  for (const example of COUNTEREXAMPLES) {
    it(`${example.name} → ${example.invariant} fails, and nothing else`, () => {
      const verdict = freshCheckoutVerdict(example.mutate(healthy()));
      expect(verdict.healthy).toBe(false);
      expect(verdict.failed).toEqual([example.invariant]);
    });
  }

  it('reports every failed invariant at once, in the exported order', () => {
    const verdict = freshCheckoutVerdict({ ...healthy(), cloneHeadMatchesSource: false, limitBreaches: 2, evidenceWritten: false });
    expect(verdict.failed).toEqual(['clone-head-matches-source', 'limit-breaches', 'evidence-written']);
  });

  it('the counterexample table covers every exported invariant', () => {
    const covered = new Set(COUNTEREXAMPLES.map((example) => example.invariant));
    expect([...FRESH_CHECKOUT_INVARIANTS].filter((invariant) => !covered.has(invariant))).toEqual([]);
    expect(FRESH_CHECKOUT_INVARIANTS).toHaveLength(16);
  });
});
