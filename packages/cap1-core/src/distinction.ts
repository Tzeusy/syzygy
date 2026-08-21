import type { ServedFact } from './epistemic.js';
import type { ProposalRendering } from './proposal.js';
import type { AuthorityExposure } from './authority.js';
import type { DiscoverabilityFinding } from './discoverability.js';

// Machine-readable distinctions — pure domain logic, no I/O, no clock.
// Behavior is bound by CAP1-REQ-064 and the cited contract clauses
// RFC7-33 (every distinction is carried as a machine-readable attribute
// on the rendered unit, served identically through the machine plane
// and preserved in plain-text renderings) and RFC7-34 (recoverable
// without colour, position, or layout — by label, text, or structure).

export interface MachineReadableDistinction {
  readonly name: string;
  readonly value: string;
  readonly recoverableBy: 'text-attribute' | 'structure';
}

export const CAPABILITY_1_DISTINCTIONS = [
  'epistemic-label',
  'rendering-tier',
  'unknown-reason',
  'freshness-state',
  'consent-state',
  'adopted-vs-unadopted',
  'proposed-vs-current',
  'effective-status-vs-stamp',
  'discoverability-value',
] as const;
export type CapabilityDistinction = (typeof CAPABILITY_1_DISTINCTIONS)[number];

export function extractDistinctions(fact: ServedFact): readonly MachineReadableDistinction[] {
  const distinctions: MachineReadableDistinction[] = [];
  distinctions.push({
    name: 'epistemic-label',
    value: fact.epistemic.label,
    recoverableBy: 'text-attribute',
  });
  if (fact.epistemic.tier !== undefined) {
    distinctions.push({
      name: 'rendering-tier',
      value: fact.epistemic.tier,
      recoverableBy: 'text-attribute',
    });
  }
  if (fact.epistemic.label === 'Unknown' && 'reasons' in fact.epistemic) {
    distinctions.push({
      name: 'unknown-reason',
      value: fact.epistemic.reasons.primary,
      recoverableBy: 'text-attribute',
    });
  }
  if (fact.epistemic.freshness !== undefined) {
    distinctions.push({
      name: 'freshness-state',
      value: fact.epistemic.freshness,
      recoverableBy: 'text-attribute',
    });
  }
  return distinctions;
}

export function extractConsentDistinction(
  consentState: string,
): readonly MachineReadableDistinction[] {
  return [
    { name: 'consent-state', value: consentState, recoverableBy: 'text-attribute' },
  ];
}

export function extractProposalDistinctions(
  rendering: ProposalRendering,
): readonly MachineReadableDistinction[] {
  return [
    { name: 'proposed-vs-current', value: rendering.marking, recoverableBy: 'text-attribute' },
    { name: 'adopted-vs-unadopted', value: String(rendering.adopted), recoverableBy: 'text-attribute' },
  ];
}

export function extractAuthorityDistinctions(
  exposure: AuthorityExposure,
): readonly MachineReadableDistinction[] {
  const distinctions: MachineReadableDistinction[] = [
    { name: 'effective-status-vs-stamp', value: exposure.effectiveStatus, recoverableBy: 'text-attribute' },
  ];
  if (exposure.selfDeclaredStamp !== undefined) {
    distinctions.push({
      name: 'effective-status-vs-stamp',
      value: `stamp:${exposure.selfDeclaredStamp} vs effective:${exposure.effectiveStatus}`,
      recoverableBy: 'structure',
    });
  }
  return distinctions;
}

export function extractDiscoverabilityDistinctions(
  finding: DiscoverabilityFinding,
): readonly MachineReadableDistinction[] {
  return [
    { name: 'discoverability-value', value: finding.value, recoverableBy: 'text-attribute' },
  ];
}

export interface DistinctionSweep {
  readonly totalDistinctions: number;
  readonly coveredDistinctions: readonly CapabilityDistinction[];
  readonly missingDistinctions: readonly CapabilityDistinction[];
}

export function sweepDistinctions(
  factDistinctions: readonly MachineReadableDistinction[],
  proposalDistinctions: readonly MachineReadableDistinction[],
  authorityDistinctions: readonly MachineReadableDistinction[],
  discoverabilityDistinctions: readonly MachineReadableDistinction[],
  consentDistinctions?: readonly MachineReadableDistinction[],
): DistinctionSweep {
  const all = [
    ...factDistinctions,
    ...proposalDistinctions,
    ...authorityDistinctions,
    ...discoverabilityDistinctions,
    ...(consentDistinctions ?? []),
  ];
  const covered = new Set(all.map((d) => d.name));
  const coveredList = CAPABILITY_1_DISTINCTIONS.filter((d) => covered.has(d));
  const missingList = CAPABILITY_1_DISTINCTIONS.filter((d) => !covered.has(d));
  return {
    totalDistinctions: CAPABILITY_1_DISTINCTIONS.length,
    coveredDistinctions: coveredList,
    missingDistinctions: missingList,
  };
}
