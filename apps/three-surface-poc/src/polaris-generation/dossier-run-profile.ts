import { DEFAULT_DISCOVERY_BUDGET, PIPELINE_QUOTABLE_CAP, type DiscoveryBudget, type GenerationBudget, type GenerationStage } from '@syzygy/polaris-generation-core';
import { DOSSIER_UNITS_POLICY, MAX_OUTPUT_TOKENS, TOKENS_PER_UNIT } from '@syzygy/polaris-generation-provider';

/**
 * The poc:dossier run budget under the accounting policy `dossier-units-v1`
 * (1 unit = 1,000 tokens, rounded up per attempt; unknown usage counts at the
 * full ceiling its permit allowed). The egress record's owner packet tells the
 * owner this budget bounds what leaves the machine, so it lives in one constant
 * and one enforcement path: `discoveryBudgetFor`, `narrativeBudgetFor`,
 * `stageCeilingUnits` and the discovery ledger in dossier-generation.ts.
 *
 * [Inferred] Every figure is a proposal from the caps in code, with no measured
 * token count or price behind it: no provider call has ever been made. The four
 * `owner` values are the ones the owner is asked to adjust; the rest follow
 * from them or from the pipeline's shape.
 */
export interface DossierRunProfile {
  readonly accountingPolicy: typeof DOSSIER_UNITS_POLICY;
  readonly owner: {
    /** Discovery plus narrative, in units. */
    readonly runTotalUnits: number;
    /** The part of the run total discovery may use; the narrative gets the rest. */
    readonly discoveryUnits: number;
    /** Ceiling of one discovery call (map or reduce). */
    readonly discoveryCallUnits: number;
    /** Whole run, discovery included. */
    readonly wallClockMs: number;
  };
  /** Ceiling of one narrative attempt, by stage: 600 for the stages that carry the sources or a whole draft, 300 for the rest. */
  readonly stageCeilingUnits: Readonly<Record<GenerationStage, number>>;
  /** Output cap of one attempt, in tokens (64 units). */
  readonly maxOutputTokens: number;
  /** Largest reply one attempt may return, in bytes; must cover `maxOutputTokens` of ordinary text. */
  readonly maxAttemptOutputBytes: number;
  readonly maxNarrativeCalls: number;
  readonly maxRepairCycles: number;
  readonly maxNarrativeInputBytes: number;
  readonly model: string;
  readonly effort: 'low' | 'medium' | 'high' | 'xhigh' | 'max';
  readonly thinking: 'off' | 'adaptive';
}

export const DOSSIER_RUN_PROFILE: DossierRunProfile = Object.freeze({
  accountingPolicy: DOSSIER_UNITS_POLICY,
  owner: Object.freeze({ runTotalUnits: 4000, discoveryUnits: 1000, discoveryCallUnits: 40, wallClockMs: 7_200_000 }),
  // Seven calls: inventory, plan, author, edit, fidelity, repair, fidelity. 3 x 600 + 4 x 300 = 3,000.
  stageCeilingUnits: Object.freeze({ inventory: 600, plan: 300, author: 600, edit: 600, fidelity: 300, repair: 300 }),
  maxOutputTokens: MAX_OUTPUT_TOKENS,
  maxAttemptOutputBytes: 400_000,
  maxNarrativeCalls: 7,
  maxRepairCycles: 1,
  maxNarrativeInputBytes: 8_000_000,
  model: 'claude-opus-5-5',
  effort: 'high',
  thinking: 'off',
});

const whole = (value: number, minimum: number): boolean => Number.isSafeInteger(value) && value >= minimum;

/** Refuses a profile whose figures contradict each other; every consumer calls this first. */
export function assertRunProfile(profile: DossierRunProfile): void {
  const { runTotalUnits, discoveryUnits, discoveryCallUnits, wallClockMs } = profile.owner;
  const stages = Object.values(profile.stageCeilingUnits);
  const ok = profile.accountingPolicy === DOSSIER_UNITS_POLICY
    && whole(runTotalUnits, 2) && whole(discoveryUnits, 0) && whole(discoveryCallUnits, 1) && whole(wallClockMs, 1)
    && discoveryUnits < runTotalUnits && discoveryUnits >= 2 * discoveryCallUnits
    && Object.keys(profile.stageCeilingUnits).length === 6 && stages.every(units => whole(units, 1))
    && whole(profile.maxOutputTokens, 1) && profile.maxOutputTokens <= MAX_OUTPUT_TOKENS && whole(profile.maxAttemptOutputBytes, 1)
    && whole(profile.maxNarrativeCalls, 1) && whole(profile.maxRepairCycles, 0) && whole(profile.maxNarrativeInputBytes, 1);
  if (!ok) throw new Error('invalid-run-profile');
  // The narrative share must hold the most expensive run the pipeline can make: one attempt per call, each at its stage ceiling.
  const order: readonly GenerationStage[] = ['inventory', 'plan', 'author', 'edit', 'fidelity', ...Array.from({ length: profile.maxRepairCycles }, () => ['repair', 'fidelity'] as const).flat()];
  const worst = order.reduce((sum, stage) => sum + profile.stageCeilingUnits[stage], 0);
  if (worst > narrativeUnits(profile)) throw new Error('invalid-run-profile: the narrative share cannot hold every stage at its ceiling');
}

export const narrativeUnits = (profile: DossierRunProfile): number => profile.owner.runTotalUnits - profile.owner.discoveryUnits;

/** Bytes a discovery call carries besides its items: the stage prompt twice (envelope and system message), the schema and the framing. */
export const DISCOVERY_FIXED_BYTES = 8000;
/** Per map item besides its excerpt: path (at most about 300 bytes), blob id and JSON framing. */
export const DISCOVERY_ITEM_OVERHEAD_BYTES = 400;
export const DISCOVERY_EXCERPT_CHARS = 800;
export const DISCOVERY_CLAIM_CHARS = 200;

/**
 * The discovery budget that fits the profile. A map call may carry
 * `maxGroupBlobs` excerpts and a reduce call `maxReduceClaims` claims, sized so
 * the largest ASCII request stays inside one call's unit ceiling (the adapters
 * refuse a request that cannot, and that group is then reported unmapped). Map
 * calls leave one call's worth of units for the reduce, so the discovery share
 * is never passed by calls issued.
 */
export function discoveryBudgetFor(profile: DossierRunProfile = DOSSIER_RUN_PROFILE): DiscoveryBudget {
  assertRunProfile(profile);
  const room = profile.owner.discoveryCallUnits * TOKENS_PER_UNIT - DISCOVERY_FIXED_BYTES;
  const groupBlobs = Math.floor(room / (DISCOVERY_EXCERPT_CHARS + DISCOVERY_ITEM_OVERHEAD_BYTES));
  const reduceClaims = Math.floor(room / (DISCOVERY_CLAIM_CHARS + DISCOVERY_ITEM_OVERHEAD_BYTES));
  if (groupBlobs < 1 || reduceClaims < 1) throw new Error('invalid-run-profile: a discovery call is too small to carry one item');
  const calls = Math.floor(profile.owner.discoveryUnits / profile.owner.discoveryCallUnits);
  return {
    maxSelected: PIPELINE_QUOTABLE_CAP,
    maxMapCalls: Math.min(DEFAULT_DISCOVERY_BUDGET.maxMapCalls, calls - 1),
    maxExcerptChars: DISCOVERY_EXCERPT_CHARS,
    maxGroupBlobs: Math.min(DEFAULT_DISCOVERY_BUDGET.maxGroupBlobs, groupBlobs),
    claimsPerGroup: DEFAULT_DISCOVERY_BUDGET.claimsPerGroup,
    maxReduceClaims: Math.min(DEFAULT_DISCOVERY_BUDGET.maxReduceClaims, reduceClaims),
    maxClaimChars: DISCOVERY_CLAIM_CHARS,
  };
}

/** The narrative's request budget; `elapsedMs` is what discovery already used of the run's wall clock. */
export function narrativeBudgetFor(profile: DossierRunProfile = DOSSIER_RUN_PROFILE, elapsedMs = 0): GenerationBudget {
  assertRunProfile(profile);
  return { maxCalls: profile.maxNarrativeCalls, maxInputBytes: profile.maxNarrativeInputBytes, maxOutputBytes: 2_000_000, maxUsageUnits: narrativeUnits(profile),
    maxElapsedMs: Math.max(0, profile.owner.wallClockMs - Math.max(0, elapsedMs)), maxRepairCycles: profile.maxRepairCycles, accountingPolicy: profile.accountingPolicy };
}

export const stageCeilingUnits = (profile: DossierRunProfile, stage: GenerationStage): number => profile.stageCeilingUnits[stage];
