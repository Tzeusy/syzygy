import type { ResourceHeadroom, ResourceHeadroomEntry, ResourceLimitObservation } from '@syzygy/three-surface-poc-core';

// The status-slot entry for the resource ledger (pursuit N3 slice 3,
// syzygy-u05.3): one span per machine tuple of `PocModel.resourceHeadroom`,
// keyed by the tuple's id, so the two channels compare per tuple. An
// unobserved value renders Unknown and its reason is stated once, never a
// zero (VIS-2). A presentation line, like the status line above it.

const LIMIT_LABEL: Readonly<Record<ResourceHeadroomEntry['limit'], string>> = {
  maxSources: 'sources',
  maxBytesPerSource: 'bytes per source',
  maxTotalBytes: 'total bytes',
  maxIndexDepth: 'index depth',
  maxParsePassesPerSource: 'parse passes per source',
  maxHumanResponseBytes: 'human response bytes',
  maxMachineResponseBytes: 'machine response bytes',
};

function attr(observation: ResourceLimitObservation): string {
  return observation.state === 'observed' ? String(observation.value) : 'unknown';
}

export function resourceHeadroomLine(headroom: ResourceHeadroom | null | undefined, escapeHtml: (value: string) => string): string {
  const open = '<p class="operability-resources" data-human-resources data-copy-role="epistemic-disclosure" data-claim-role="epistemic-claim" data-presentation-artifact data-non-citable>';
  if (headroom === null || headroom === undefined) return `${open}Resources: Unknown (not supplied)</p>`;
  const reasons: string[] = [];
  const note = (reason: string): string => {
    if (!reasons.includes(reason)) reasons.push(reason);
    return `Unknown (${reasons.indexOf(reason) + 1})`;
  };
  const entries = headroom.entries.map((entry) => {
    const text = entry.observed.state === 'observed' && entry.remaining.state === 'observed'
      ? `${LIMIT_LABEL[entry.limit]} ${entry.observed.value} of ${entry.declared}, ${entry.remaining.value} left`
      : `${LIMIT_LABEL[entry.limit]} ${note(entry.observed.state === 'unknown' ? entry.observed.reason : entry.remaining.state === 'unknown' ? entry.remaining.reason : '')} of ${entry.declared}`;
    return `<span data-resource-tuple="${escapeHtml(entry.id)}" data-declared="${entry.declared}" data-observed="${attr(entry.observed)}" data-remaining="${attr(entry.remaining)}">${escapeHtml(text)}</span>`;
  });
  const { cost } = headroom;
  const costSpan = cost.state === 'observed'
    ? `<span data-resource-tuple="${escapeHtml(cost.id)}" data-bodies-read="${cost.bodiesRead}" data-bytes="${cost.bytes}" data-parse-passes="${cost.parsePasses}" data-worst-source-passes="${cost.worstSourcePasses}">cost ${cost.bodiesRead} bodies, ${cost.bytes} bytes, ${cost.parsePasses} parse passes, worst source ${cost.worstSourcePasses} passes</span>`
    : `<span data-resource-tuple="${escapeHtml(cost.id)}" data-bodies-read="unknown" data-bytes="unknown" data-parse-passes="unknown" data-worst-source-passes="unknown">cost ${escapeHtml(note(cost.reason))}</span>`;
  const why = reasons.map((reason, index) => `(${index + 1}) ${escapeHtml(reason)}`).join('; ');
  return `${open}Resources: ${[...entries, costSpan].join('; ')}.${why === '' ? '' : ` Unknown because: ${why}.`}</p>`;
}
