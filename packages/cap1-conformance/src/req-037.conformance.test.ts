import { describe, expect, it } from 'vitest';
import {
  computeReconciled,
  computeShapeAnswers,
  type EvaluationIdentity,
  type ProjectId,
  type ReconciliationFacts,
} from '@syzygy/cap1-core';

// CAP1-REQ-037 — Uncomputed reconciliation is Unknown (event-response).
//
// Case: a checker presents a project with merged work and no computed
// reconciliation, and queries `Reconciled`. Observable: the
// `Reconciled` answer and the work's reconciliation state in the fact
// set. Oracle: the answer is `Unknown`; the work's state reads as
// reconciliation evidence absent; no reason outside the twelve is
// minted; bounded — one answer, one state. Oracle independence: the
// fixture controls that no reconciliation was computed; expected
// renderings come from SDR-12/SDR-34 — the spellings are hard-coded
// below, never imported. Falsifier: merged work rendered as reconciled
// or the answer rendered favourable absent a computed reconciliation,
// or a minted thirteenth Unknown reason.

const TWELVE_REASONS = [
  'missing-declaration',
  'missing-evidence',
  'no-currency-bound-declared',
  'stale-beyond-currency-bound',
  'mapping-coverage-absent',
  'unconsented-source-or-provider',
  'excluded-content',
  'contradicted-pending-adjudication',
  'challenge-suspended',
  'source-uncaptured-or-unreachable',
  'reference-unresolvable',
  'execution-blocked',
] as const;

const PROJECT = 'prj-shape-037' as ProjectId;
const EVALUATION: EvaluationIdentity = { snapshot: 'snap-037', asOf: '2026-08-21T00:00:00Z' };

// Merged work exists; reconciliation has NOT been computed.
const UNCOMPUTED: ReconciliationFacts = {
  computed: false,
  mergedWork: [{ workId: 'pr-101' }, { workId: 'pr-102' }],
};

describe('CAP1-REQ-037 — uncomputed reconciliation is Unknown', () => {
  it('scenario/oracle: merged work with no computed reconciliation — `Reconciled` renders Unknown and each work item reads `reconciliation evidence absent`', () => {
    const set = computeShapeAnswers(PROJECT, EVALUATION, { reconciliation: UNCOMPUTED });
    const reconciled = set.answers[6];
    expect(reconciled.name).toBe('Reconciled');
    expect(reconciled.render.value).toBe('Unknown');
    // Both merged work items are disclosed as facts of the render, each
    // reading exactly the spec's phrase — hard-coded:
    const workFacts = reconciled.factSet.facts.filter((fact) =>
      fact.name.startsWith('merged-work:'),
    );
    expect(workFacts).toHaveLength(2); // denominator: the merged set
    for (const fact of workFacts) {
      expect(fact.value).toBe('reconciliation evidence absent');
    }
  });

  it('oracle: no reason outside the twelve is minted — the merged-but-unreconciled condition is a FACT of the render, bound to no thirteenth reason', () => {
    const answer = computeReconciled(UNCOMPUTED, `project:${PROJECT}`, EVALUATION);
    if (answer.render.value !== 'Unknown') throw new Error('fixture must render Unknown');
    const served = [answer.render.reasons.primary, ...answer.render.reasons.secondary];
    for (const reason of served) {
      expect(TWELVE_REASONS).toContain(reason);
    }
    // The disclosure phrase itself is never served as a reason:
    expect(served).not.toContain('reconciliation evidence absent');
    expect(served).not.toContain('merged-but-unreconciled');
  });

  it('falsifier: merged work is never rendered as reconciled, done, or green absent a computed reconciliation', () => {
    const answer = computeReconciled(UNCOMPUTED, `project:${PROJECT}`, EVALUATION);
    expect(answer.render.value).not.toBe('satisfied');
    for (const fact of answer.factSet.facts) {
      if (fact.name.startsWith('merged-work:')) {
        expect(fact.value).not.toMatch(/\b(reconciled|done|green)\b/i);
        expect(fact.value).toBe('reconciliation evidence absent');
      }
    }
  });

  it('falsifier: reconciliation input absent entirely — still Unknown, never favourable', () => {
    const answer = computeReconciled(undefined, `project:${PROJECT}`, EVALUATION);
    expect(answer.render.value).toBe('Unknown');
    if (answer.render.value === 'Unknown') {
      expect(TWELVE_REASONS).toContain(answer.render.reasons.primary);
    }
  });

  it('the favourable arm is reachable only through a computed reconciliation of the declared scope', () => {
    const computed = computeReconciled(
      {
        computed: true,
        outcome: 'satisfied',
        declaredScope: 'merged-work',
        mergedWork: [{ workId: 'pr-101' }],
      },
      `project:${PROJECT}`,
      EVALUATION,
    );
    expect(computed.render.value).toBe('satisfied');
    // And a computed reconciliation establishing divergence is Gap —
    // never silently favourable, never Unknown (CAP1-REQ-034):
    const diverged = computeReconciled(
      {
        computed: true,
        outcome: 'unsatisfied',
        declaredScope: 'merged-work',
        mergedWork: [{ workId: 'pr-101' }],
      },
      `project:${PROJECT}`,
      EVALUATION,
    );
    expect(diverged.render.value).toBe('Gap');
  });
});
