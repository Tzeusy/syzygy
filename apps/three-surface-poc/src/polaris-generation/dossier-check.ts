import { DOSSIER_MAX_SELECTED_BYTES, type GenerationStage } from '@syzygy/polaris-generation-core';
import { minimumUsageUnits } from '@syzygy/polaris-generation-provider';

import { DOSSIER_RUN_PROFILE, assertRunProfile, discoveryBudgetFor, narrativeUnits, type DossierRunProfile } from './dossier-run-profile.js';
import { resolveAdmission, type AdmissionAnswer, type AdmissionRequirement, type GithubTarget, type RevisionSource, type TriggerOutcome, type TriggerPorts } from './dossier-trigger.js';

/** The arithmetic of the run profile, derived from it and from nothing measured. */
export interface BudgetArithmetic {
  readonly accountingPolicy: string;
  readonly runTotalUnits: number;
  readonly discoveryUnits: number;
  readonly narrativeUnits: number;
  readonly discoveryCallUnits: number;
  readonly maxDiscoveryCalls: number;
  readonly maxMapCalls: number;
  readonly stageCeilingUnits: Readonly<Record<GenerationStage, number>>;
  /** Inventory, plan, author, edit and fidelity, each at its ceiling. */
  readonly baseStagesAtCeilingUnits: number;
  readonly narrativeHeadroomUnits: number;
  /** A repair plus the fidelity review that follows it, both at their ceilings. */
  readonly repairCycleAtCeilingUnits: number;
  readonly repairCyclesAffordable: number;
  readonly maxRepairCycles: number;
  readonly wallClockMs: number;
  readonly maxSelectedBytes: number;
  /** The least units a source-carrying request needs for a selection of `maxSelectedBytes`, against the smallest source-carrying stage ceiling. */
  readonly fullSelectionMinimumUnits: number;
  readonly smallestSourceStageCeilingUnits: number;
  readonly fullSelectionFits: boolean;
}

export function budgetArithmetic(profile: DossierRunProfile = DOSSIER_RUN_PROFILE): BudgetArithmetic {
  assertRunProfile(profile);
  const stages = profile.stageCeilingUnits;
  const base = stages.inventory + stages.plan + stages.author + stages.edit + stages.fidelity;
  const narrative = narrativeUnits(profile);
  const headroom = narrative - base;
  const cycle = stages.repair + stages.fidelity;
  const sourceCeiling = Math.min(stages.inventory, stages.author, stages.edit, stages.fidelity);
  const minimum = minimumUsageUnits(DOSSIER_MAX_SELECTED_BYTES);
  return {
    accountingPolicy: profile.accountingPolicy, runTotalUnits: profile.owner.runTotalUnits, discoveryUnits: profile.owner.discoveryUnits, narrativeUnits: narrative,
    discoveryCallUnits: profile.owner.discoveryCallUnits, maxDiscoveryCalls: Math.floor(profile.owner.discoveryUnits / profile.owner.discoveryCallUnits), maxMapCalls: discoveryBudgetFor(profile).maxMapCalls,
    stageCeilingUnits: stages, baseStagesAtCeilingUnits: base, narrativeHeadroomUnits: headroom, repairCycleAtCeilingUnits: cycle,
    repairCyclesAffordable: Math.min(profile.maxRepairCycles, Math.max(0, Math.floor(headroom / cycle))), maxRepairCycles: profile.maxRepairCycles,
    wallClockMs: profile.owner.wallClockMs, maxSelectedBytes: DOSSIER_MAX_SELECTED_BYTES, fullSelectionMinimumUnits: minimum, smallestSourceStageCeilingUnits: sourceCeiling, fullSelectionFits: minimum <= sourceCeiling,
  };
}

export type CheckOutcome =
  | TriggerOutcome
  | { readonly state: 'check-ready'; readonly target: GithubTarget; readonly revision: string; readonly resolvedRef: string; readonly revisionSource: RevisionSource; readonly source: string;
      readonly requirements: readonly (AdmissionRequirement & { readonly answer: AdmissionAnswer })[]; readonly budget: BudgetArithmetic };

/** `--check`: every gate a real run passes before it reads, and nothing after them. Spawns only `git ls-remote`; opens no generation, checks out nothing and reads no repository object. */
export async function checkDossier(rawUrl: string, ports: Pick<TriggerPorts, 'lsRemote' | 'records'> = {}, profile: DossierRunProfile = DOSSIER_RUN_PROFILE): Promise<CheckOutcome> {
  const resolved = await resolveAdmission(rawUrl, ports);
  if ('state' in resolved) return resolved;
  return { state: 'check-ready', target: resolved.target, revision: resolved.pinned.revision, resolvedRef: resolved.pinned.resolvedRef, revisionSource: resolved.revisionSource, source: resolved.records.source,
    requirements: resolved.checked, budget: budgetArithmetic(profile) };
}

const hours = (ms: number): string => `${Math.round(ms / 360_000) / 10} h`;

export function formatBudget(b: BudgetArithmetic): string[] {
  const s = b.stageCeilingUnits;
  return [
    `Budget (${b.accountingPolicy}; 1 unit = 1,000 tokens; derived from the profile, no measured cost behind it):`,
    `  run total ${b.runTotalUnits} = discovery ${b.discoveryUnits} + narrative ${b.narrativeUnits}; wall clock ${hours(b.wallClockMs)}`,
    `  discovery: ${b.maxDiscoveryCalls} calls of at most ${b.discoveryCallUnits} units (at most ${b.maxMapCalls} map calls, the rest reduce)`,
    `  stage ceilings: inventory ${s.inventory}, plan ${s.plan}, author ${s.author}, edit ${s.edit}, fidelity ${s.fidelity}, repair ${s.repair}`,
    `  base stages at ceiling ${b.baseStagesAtCeilingUnits} of ${b.narrativeUnits}; headroom ${b.narrativeHeadroomUnits}`,
    `  one repair cycle (repair + fidelity) at ceiling ${b.repairCycleAtCeilingUnits}; ${b.repairCyclesAffordable} of ${b.maxRepairCycles} cycles affordable`,
    `  source selection cap ${b.maxSelectedBytes} bytes needs at least ${b.fullSelectionMinimumUnits} units per source-carrying request; smallest such ceiling ${b.smallestSourceStageCeilingUnits}: ${b.fullSelectionFits ? 'fits' : 'DOES NOT FIT'}`,
  ];
}

export function formatCheck(outcome: CheckOutcome): string {
  if (outcome.state !== 'check-ready') return '';
  return [`Check ${outcome.target.url} (${outcome.target.repositoryId})`,
    `Pinned ${outcome.resolvedRef} -> ${outcome.revision} (git ls-remote: metadata only)`,
    outcome.revisionSource.from === 'consent' ? `Revision source: the observation consent admits ${outcome.revisionSource.label} (${outcome.revisionSource.commitId})` : `Revision source: the URL${outcome.revisionSource.ref === undefined ? ' (default branch tip)' : ` (${outcome.revisionSource.ref})`}`,
    `Admission records consulted: ${outcome.source}`,
    ...outcome.requirements.map(r => `  OK       ${r.kind}: ${(r.answer as { record: string }).record}`),
    ...formatBudget(outcome.budget),
    'READY: every gate before a read is satisfied. Nothing was read and no provider was called.', ''].join('\n');
}
