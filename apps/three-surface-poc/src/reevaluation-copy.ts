import type { ClockMovement, Reevaluation } from '@syzygy/three-surface-poc-core';

// Plain-text copy for one named re-evaluation result (syzygy-u05.2), shared
// by the re-observe result page, the --watch console and the status line.
// The two staleness limbs and the Dolt clock are always named separately:
// one never stands in for another, and an unread value is Unknown.

function prefix(value: string): string {
  return value.length > 12 ? `${value.slice(0, 12)}…` : value;
}

function movementLabel(movement: ClockMovement): string {
  return movement === 'unknown' ? 'movement Unknown' : movement;
}

export function projectLimbText(reevaluation: Reevaluation | null): string {
  if (reevaluation === null) return 'Unknown (not supplied)';
  const limb = reevaluation.limbs.observedProject;
  if (limb.kind === 'no-prior') return 'no prior evaluation this run';
  if (limb.kind === 'unknown') return `Unknown (${limb.reason})`;
  return `${limb.changedSources} changed, ${limb.addedSources} added since the superseded evaluation`;
}

export function observatoryLimbText(reevaluation: Reevaluation | null): string {
  if (reevaluation === null) return 'Unknown (not supplied)';
  const limb = reevaluation.limbs.observatory;
  if (limb.commitsSinceBuild === null) return `Unknown (commits since build ${prefix(limb.buildRevision)} unreadable)`;
  return `${limb.commitsSinceBuild} Syzygy commit${limb.commitsSinceBuild === 1 ? '' : 's'} since build ${prefix(limb.buildRevision)}`;
}

export function doltClockText(reevaluation: Reevaluation | null): string {
  if (reevaluation === null) return 'Unknown (not supplied)';
  const dolt = reevaluation.clocks.doltRevision;
  return dolt === null ? 'Unknown (work items not observed)' : `${prefix(dolt)} (${movementLabel(reevaluation.moved.doltRevision)})`;
}

/** The full result, one fact per line; used verbatim by --watch. */
export function reevaluationLines(reevaluation: Reevaluation): readonly string[] {
  const { clocks, moved } = reevaluation;
  return [
    `Evaluation: ${reevaluation.evaluation}`,
    `Supersedes: ${reevaluation.supersedes ?? 'none (first evaluation this run)'}`,
    `Butlers HEAD: ${clocks.butlersHead} (${movementLabel(moved.butlersHead)})`,
    `Working-tree digest: ${clocks.workingTreeDigest} (${movementLabel(moved.workingTreeDigest)})`,
    `Dolt revision: ${clocks.doltRevision ?? 'Unknown (work items not observed)'} (${movementLabel(moved.doltRevision)})`,
    `Observed-project limb: ${projectLimbText(reevaluation)}`,
    `Observatory limb: ${observatoryLimbText(reevaluation)}`,
  ];
}
