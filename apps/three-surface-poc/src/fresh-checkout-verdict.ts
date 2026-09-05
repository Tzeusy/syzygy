// Fresh-checkout verdict (bead syzygy-1z3.24.6; PWB-LIVE-14): the exit
// polarity of the fresh-checkout demonstration, as one pure function over
// every invariant the evidence record carries. Before this, the command
// recorded clone/head equality, the Butlers revision, authority admission,
// parity, limit breaches and the daemon's exit and then ignored all of them
// when choosing its exit code. Now every recorded falsifier moves the
// polarity: the command exits 0 only when every invariant holds, and the
// evidence names each one that did not.
//
// PWB-REQ-021 record readiness is recorded but deliberately not an
// invariant here: no run record exists until the owner has walked, so a
// `no-run-record` state is the expected pre-walk fact, not a defect. The
// walkthrough preflight (the mechanical readiness of the surface) is.

export const FRESH_CHECKOUT_INVARIANTS = [
  'clone-head-matches-source',
  'install',
  'build',
  'test',
  'machine-refused-without-credential',
  'machine-served-with-credential',
  'human-routes-served',
  'source-route-served',
  'butlers-revision-matches-model',
  'shape-observed',
  'authority-admits',
  'parity',
  'limit-breaches',
  'preflight-ready',
  'daemon-exit-clean',
  'evidence-written',
] as const;
export type FreshCheckoutInvariant = (typeof FRESH_CHECKOUT_INVARIANTS)[number];

/** PWB-REQ-020 parity as the sweep oracle states it: every rendered claim
 * tuple carries the machine claim's exact state (a claim may be cited in
 * more than one place, so tuples outnumber distinct ids); the machine
 * answer carries each claim once; every machine claim is rendered and
 * every rendered claim is in the machine answer. */
export interface FreshCheckoutParity {
  readonly humanClaimTuples: number;
  readonly humanDistinctClaimIds: number;
  readonly humanTuplesMismatchingMachine: number;
  readonly machinePresentedClaimIds: number;
  readonly machineDistinctClaimIds: number;
  readonly machineIdsAbsentFromHuman: number;
  readonly humanIdsAbsentFromMachine: number;
}

export interface FreshCheckoutInvariants {
  readonly cloneHeadMatchesSource: boolean;
  readonly installExitCode: number;
  readonly buildExitCode: number;
  readonly testExitCode: number;
  readonly refusedStatus: number;
  readonly machineStatus: number;
  /** Status of every human route fetched (`/`, `/polaris`, …); must be nonempty. */
  readonly humanRouteStatuses: readonly number[];
  readonly sourceRouteStatus: number;
  readonly daemonObservedRevision: string;
  readonly modelRevision: string;
  readonly shapeKind: string;
  /** `null` when no authority was evaluated at all. */
  readonly authorityAdmits: boolean | null;
  readonly parity: FreshCheckoutParity;
  readonly limitBreaches: number;
  readonly preflightReady: boolean;
  readonly daemonExitCode: number | null;
  readonly daemonStderr: string;
  readonly evidenceWritten: boolean;
}

export interface FreshCheckoutVerdict {
  readonly healthy: boolean;
  readonly failed: readonly FreshCheckoutInvariant[];
}

const HEX_REVISION = /^[0-9a-f]{40,64}$/;

/** Every invariant is checked; every failure is named. */
export function freshCheckoutVerdict(inputs: FreshCheckoutInvariants): FreshCheckoutVerdict {
  const failed: FreshCheckoutInvariant[] = [];
  const check = (name: FreshCheckoutInvariant, holds: boolean): void => {
    if (!holds) failed.push(name);
  };
  const parity = inputs.parity;
  check('clone-head-matches-source', inputs.cloneHeadMatchesSource);
  check('install', inputs.installExitCode === 0);
  check('build', inputs.buildExitCode === 0);
  check('test', inputs.testExitCode === 0);
  check('machine-refused-without-credential', inputs.refusedStatus === 401);
  check('machine-served-with-credential', inputs.machineStatus === 200);
  check('human-routes-served', inputs.humanRouteStatuses.length > 0 && inputs.humanRouteStatuses.every((status) => status === 200));
  check('source-route-served', inputs.sourceRouteStatus === 200);
  check('butlers-revision-matches-model', HEX_REVISION.test(inputs.daemonObservedRevision) && inputs.daemonObservedRevision === inputs.modelRevision);
  check('shape-observed', inputs.shapeKind === 'observed');
  check('authority-admits', inputs.authorityAdmits === true);
  check(
    'parity',
    parity.humanClaimTuples > 0
      && parity.humanTuplesMismatchingMachine === 0
      && parity.machinePresentedClaimIds === parity.machineDistinctClaimIds
      && parity.humanDistinctClaimIds === parity.machineDistinctClaimIds
      && parity.machineIdsAbsentFromHuman === 0
      && parity.humanIdsAbsentFromMachine === 0,
  );
  check('limit-breaches', inputs.limitBreaches === 0);
  check('preflight-ready', inputs.preflightReady);
  check('daemon-exit-clean', inputs.daemonExitCode === 0 && inputs.daemonStderr.trim() === '');
  check('evidence-written', inputs.evidenceWritten);
  return { healthy: failed.length === 0, failed };
}
