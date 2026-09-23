// N3 slice 4 (bead syzygy-u05.3): the population block every retained
// page-size evidence record carries. Expected values are hand-typed
// literals, never imported from the module under test; fixtures are built
// in beforeAll per AGENTS.md ("a mutation that throws at describe time
// reports zero tests and scores as survived -- build fixtures in
// beforeAll").

import { beforeAll, describe, expect, it } from 'vitest';

import { derivePopulationBlock, modelItemCount, renderedClaimIdCount, type ProjectShapePopulationView } from './evidence-population.js';

describe('modelItemCount', () => {
  let observedFew: ProjectShapePopulationView;
  let observedMany: ProjectShapePopulationView;
  let notEvaluated: ProjectShapePopulationView;
  let notAdmitted: ProjectShapePopulationView;
  let observationFailed: ProjectShapePopulationView;
  let observedNoCounts: ProjectShapePopulationView;

  beforeAll(() => {
    observedFew = { kind: 'observed', counts: { items: 3 } };
    observedMany = { kind: 'observed', counts: { items: 415 } };
    notEvaluated = { kind: 'not-evaluated' };
    notAdmitted = { kind: 'not-admitted' };
    observationFailed = { kind: 'observation-failed' };
    // Defensive: an observed shape is always built with counts by the real
    // pipeline, but the view type declares counts optional -- exercise the
    // absent case explicitly rather than assuming it cannot occur.
    observedNoCounts = { kind: 'observed' };
  });

  it('reads counts.items on an observed shape', () => {
    expect(modelItemCount(observedFew)).toBe(3);
    expect(modelItemCount(observedMany)).toBe(415);
  });

  it('is zero for every non-observed shape kind, never a placeholder for "not measured"', () => {
    expect(modelItemCount(notEvaluated)).toBe(0);
    expect(modelItemCount(notAdmitted)).toBe(0);
    expect(modelItemCount(observationFailed)).toBe(0);
  });

  it('is zero when an observed shape carries no counts', () => {
    expect(modelItemCount(observedNoCounts)).toBe(0);
  });
});

describe('renderedClaimIdCount', () => {
  let pageWithDuplicates: string;
  let pageWithEscapedIds: string;
  let pageWithNoClaims: string;
  let pageWithMixedEncodingOfSameId: string;

  beforeAll(() => {
    pageWithDuplicates = [
      '<section>',
      '<span class="claim-tuple" data-claim-id="claim:item:catalog-entry:Atlas" data-epistemic-label="Observed">Observed</span>',
      '<span class="claim-tuple" data-claim-id="claim:item:catalog-entry:Bishop" data-epistemic-label="Observed">Observed</span>',
      // The same claim id rendered a second time (a repeated tuple, as the
      // lane-a record's own invariants script expects for compact classes).
      '<span class="claim-tuple" data-claim-id="claim:item:catalog-entry:Atlas" data-epistemic-label="Observed">Observed</span>',
      '</section>',
    ].join('\n');
    pageWithEscapedIds = '<span class="claim-tuple" data-claim-id="claim:fact:a &amp; b" data-epistemic-label="Unknown"></span>';
    pageWithNoClaims = '<main><p>No claim tuples on this page.</p></main>';
    // The same underlying claim id, rendered once with its ampersand
    // HTML-entity-escaped and once plain. A single-occurrence fixture (like
    // pageWithEscapedIds above) cannot tell a correct decode from a deleted
    // one, since a lone id's Set size is 1 either way -- this is the rule-6
    // survivor the review found (deleting the `&amp;` -> `&` step in
    // decodeHtmlAttr). With decoding intact both attribute values decode to
    // the same string, so the distinct count is 1; without it the two raw
    // attribute strings differ and the count becomes 2.
    pageWithMixedEncodingOfSameId = [
      '<span class="claim-tuple" data-claim-id="claim:fact:a &amp; b" data-epistemic-label="Unknown"></span>',
      '<span class="claim-tuple" data-claim-id="claim:fact:a & b" data-epistemic-label="Unknown"></span>',
    ].join('\n');
  });

  it('counts distinct claim ids once each, regardless of how many times a claim renders', () => {
    expect(renderedClaimIdCount(pageWithDuplicates)).toBe(2);
  });

  it('decodes HTML entities before counting, so an escaped id is not double-counted as a distinct value', () => {
    expect(renderedClaimIdCount(pageWithEscapedIds)).toBe(1);
  });

  it('decodes an entity-escaped and a plain rendering of the same id to one distinct value', () => {
    expect(renderedClaimIdCount(pageWithMixedEncodingOfSameId)).toBe(1);
  });

  it('is zero on a page with no claim tuples', () => {
    expect(renderedClaimIdCount(pageWithNoClaims)).toBe(0);
  });
});

describe('derivePopulationBlock', () => {
  let html: string;
  let projectShape: ProjectShapePopulationView;

  beforeAll(() => {
    html = [
      '<span class="claim-tuple" data-claim-id="claim:item:catalog-entry:Atlas"></span>',
      '<span class="claim-tuple" data-claim-id="claim:item:catalog-entry:Bishop"></span>',
    ].join('\n');
    projectShape = { kind: 'observed', counts: { items: 2 } };
  });

  it('assembles the three-field block from the model, the page and the caller-supplied revision', () => {
    expect(
      derivePopulationBlock({
        projectShape,
        polarisHtml: html,
        butlersRevision: '2e3bac97790b4bd8906dcac63eadb5642a0bb1ac',
      }),
    ).toEqual({
      itemCount: 2,
      claimIdCount: 2,
      butlersRevision: '2e3bac97790b4bd8906dcac63eadb5642a0bb1ac',
    });
  });

  it('never invents a Butlers revision: it is carried through verbatim, including an explicit Unknown', () => {
    expect(
      derivePopulationBlock({
        projectShape: { kind: 'not-evaluated' },
        polarisHtml: '',
        butlersRevision: 'unknown: no same-evaluation revision',
      }),
    ).toEqual({
      itemCount: 0,
      claimIdCount: 0,
      butlersRevision: 'unknown: no same-evaluation revision',
    });
  });
});
