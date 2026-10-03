import { describe, expect, it } from 'vitest';

import type { ProjectShape } from './project-shape-model.js';
import { PWB_RESOURCE_LIMITS } from './project-shape-observation.js';
import { resourceHeadroom } from './resource-headroom.js';
import { createResourceLedger } from './resource-ledger.js';

// Pursuit N3 slice 3 (syzygy-u05.3). Expected values are literals.
const OID_A = 'a'.repeat(40);
const OID_B = 'b'.repeat(40);
const CEILING_REASON = "the final-response ceiling is enforced entirely outside this ledger, by routes.ts's boundedResponse, which never charges a ResourceLedger";

function observedShape(): ProjectShape {
  const ledger = createResourceLedger(PWB_RESOURCE_LIMITS);
  ledger.declareSourcePopulation(3);
  ledger.chargeBody('a', OID_A, 5);
  ledger.chargeBody('b', OID_B, 7);
  ledger.chargePass('a', 'utf8-and-nul-validation');
  ledger.chargePass('a', 'markdown-code-context-mask');
  ledger.chargePass('b', 'utf8-and-nul-validation');
  return { kind: 'observed', resourceUse: ledger.summary() } as unknown as ProjectShape;
}

describe('resource headroom block', () => {
  it('projects all seven limits and the cost record, one id per tuple, from an observed ledger', () => {
    expect(resourceHeadroom(observedShape())).toEqual({
      entries: [
        { id: 'resource-headroom:maxSources', limit: 'maxSources', declared: 512, observed: { state: 'observed', value: 3 }, remaining: { state: 'observed', value: 509 } },
        { id: 'resource-headroom:maxBytesPerSource', limit: 'maxBytesPerSource', declared: 1048576, observed: { state: 'observed', value: 7 }, remaining: { state: 'observed', value: 1048569 } },
        { id: 'resource-headroom:maxTotalBytes', limit: 'maxTotalBytes', declared: 16777216, observed: { state: 'observed', value: 12 }, remaining: { state: 'observed', value: 16777204 } },
        { id: 'resource-headroom:maxIndexDepth', limit: 'maxIndexDepth', declared: 4, observed: { state: 'observed', value: 3 }, remaining: { state: 'observed', value: 1 } },
        { id: 'resource-headroom:maxParsePassesPerSource', limit: 'maxParsePassesPerSource', declared: 16, observed: { state: 'observed', value: 2 }, remaining: { state: 'observed', value: 14 } },
        { id: 'resource-headroom:maxHumanResponseBytes', limit: 'maxHumanResponseBytes', declared: 2097152, observed: { state: 'unknown', reason: CEILING_REASON }, remaining: { state: 'unknown', reason: CEILING_REASON } },
        { id: 'resource-headroom:maxMachineResponseBytes', limit: 'maxMachineResponseBytes', declared: 8388608, observed: { state: 'unknown', reason: CEILING_REASON }, remaining: { state: 'unknown', reason: CEILING_REASON } },
      ],
      cost: { id: 'resource-cost', state: 'observed', bodiesRead: 2, bytes: 12, parsePasses: 3, worstSourcePasses: 2 },
    });
  });

  it('renders every observed value and the cost Unknown when no ledger ran, never zero; declared limits stay the registry\'s', () => {
    const unknown = { state: 'unknown', reason: 'no resource ledger ran: the project shape is not-evaluated' };
    const block = resourceHeadroom({ kind: 'not-evaluated' } as unknown as ProjectShape);
    expect(block.cost).toEqual({ id: 'resource-cost', state: 'unknown', reason: 'no resource ledger ran: the project shape is not-evaluated' });
    expect(block.entries.map((entry) => [entry.id, entry.declared])).toEqual([
      ['resource-headroom:maxSources', 512],
      ['resource-headroom:maxBytesPerSource', 1048576],
      ['resource-headroom:maxTotalBytes', 16777216],
      ['resource-headroom:maxIndexDepth', 4],
      ['resource-headroom:maxParsePassesPerSource', 16],
      ['resource-headroom:maxHumanResponseBytes', 2097152],
      ['resource-headroom:maxMachineResponseBytes', 8388608],
    ]);
    for (const entry of block.entries) {
      expect(entry.observed).toEqual(unknown);
      expect(entry.remaining).toEqual(unknown);
    }
  });

  it('uses the evaluation\'s own declared envelope when one was supplied', () => {
    const block = resourceHeadroom({ kind: 'not-admitted' } as unknown as ProjectShape, { ...PWB_RESOURCE_LIMITS, maxSources: 7 });
    expect(block.entries[0]).toMatchObject({ id: 'resource-headroom:maxSources', declared: 7, observed: { state: 'unknown', reason: 'no resource ledger ran: the project shape is not-admitted' } });
  });
});
