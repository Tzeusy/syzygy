import type { EvaluationId, EvaluationIdentity } from './identity.js';

// Evaluation identity, answer stamps, and deterministic-layer equality —
// pure functions, no I/O, no clock. Behavior is bound by CAP1-REQ-042
// (with CAP1-REQ-005's determinism from S1) and the cited contract
// clauses RFC2-3 (evaluation identity is the pair (source snapshot,
// as-of instant) and nothing else), RFC6-7 (resolution is deterministic
// per evaluation), and RFC6-15 (every answer is evaluation-stamped;
// an answer that cannot name its evaluation is not an answer).

// Canonical evaluation id for one identified evaluation. RFC2-3: the
// identity is the PAIR — no kind, purpose, or run tag may be a third
// component, so nothing else enters this string. The '@' join is
// implementation formatting, not spec vocabulary; the identity-bearing
// content is exactly the two coordinates.
export function evaluationId(identity: EvaluationIdentity): EvaluationId {
  return `${identity.snapshot}@${identity.asOf}` as EvaluationId;
}

// An answer that names the evaluation it was computed at. The stamp is
// REQUIRED at the type level: there is no unstamped-answer arm, because
// an answer that cannot name its evaluation is not an answer (RFC6-15;
// CAP1-REQ-042).
export interface StampedAnswer<T> {
  readonly evaluation: EvaluationIdentity;
  readonly answer: T;
}

// The equivalence coordinates of one query (CAP1-REQ-042): same
// selection, same evaluation identity, same declared filters, same
// scenario context ⇒ equivalent queries. Filters are a plain record so
// key order is presentation, never meaning — canonicalization below
// erases it.
export interface QueryEnvelope {
  readonly selection: string;
  readonly evaluation: EvaluationIdentity;
  readonly filters: Readonly<Record<string, string>>;
  readonly scenarioContext: string;
}

// Canonical serialization of a value's deterministic layer: recursively
// key-sorted JSON, so two structurally equal answers serialize to equal
// bytes whatever property order they were built in. Display formatting
// is exactly what this excludes (RFC2-3: "only display formatting is
// excluded"). Undefined-valued properties are absent from JSON output,
// matching structural equality.
export function deterministicLayer(value: unknown): string {
  return JSON.stringify(sortKeys(value));
}

function sortKeys(value: unknown): unknown {
  if (Array.isArray(value)) {
    return value.map(sortKeys);
  }
  if (typeof value === 'object' && value !== null) {
    const record = value as Record<string, unknown>;
    const sorted: Record<string, unknown> = {};
    for (const key of Object.keys(record).sort()) {
      sorted[key] = sortKeys(record[key]);
    }
    return sorted;
  }
  return value;
}

// The canonical key of a query envelope: two envelopes are EQUIVALENT
// queries (CAP1-REQ-042's quantifier) exactly when their keys are equal
// bytes. Built on the same canonicalization, so filter-record key order
// never distinguishes two equivalent queries.
export function queryKey(envelope: QueryEnvelope): string {
  return deterministicLayer({
    selection: envelope.selection,
    evaluation: envelope.evaluation,
    filters: envelope.filters,
    scenarioContext: envelope.scenarioContext,
  });
}

// Runs one query and stamps its answer with the envelope's evaluation
// identity — the stamp is the envelope's own coordinate, never a clock
// read (RFC2-3: the as-of instant is an explicit input, never ambient
// wall-clock). Determinism is the compute function's obligation
// (RFC6-7); this layer guarantees the stamp travels with every answer
// (RFC6-15) and that the compute sees only the envelope.
export function runQuery<T>(
  envelope: QueryEnvelope,
  compute: (envelope: QueryEnvelope) => T,
): StampedAnswer<T> {
  return {
    evaluation: envelope.evaluation,
    answer: compute(envelope),
  };
}

// Deterministic-layer agreement between two stamped answers: same
// evaluation identity AND byte-equal deterministic layers. Judged by
// comparison of the two answers — never by either answer's own claim
// of determinism (CAP1-REQ-042 oracle independence).
export function answersAgree<T>(a: StampedAnswer<T>, b: StampedAnswer<T>): boolean {
  return (
    a.evaluation.snapshot === b.evaluation.snapshot &&
    a.evaluation.asOf === b.evaluation.asOf &&
    deterministicLayer(a.answer) === deterministicLayer(b.answer)
  );
}
