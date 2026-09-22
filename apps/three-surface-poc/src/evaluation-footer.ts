import type { PocModel } from '@syzygy/three-surface-poc-core';

/**
 * The composite evaluation identity and as-of instant Polaris already
 * renders in its footer (`Evaluation <snapshot> as of <asOf>`,
 * apps/three-surface-poc/src/polaris.ts, reused here verbatim — never
 * recomputed). Trajectory and Orrery print the same line so a reader can
 * tell all three surfaces were computed together (N4; L6-F4, RFC6-15).
 */
export function compositeEvaluationLine(model: PocModel, escapeHtml: (value: string) => string): string {
  return `Evaluation <code>${escapeHtml(model.evaluation.snapshot)}</code> as of <code>${escapeHtml(model.evaluation.asOf)}</code>.`;
}

export interface SubstrateSkewCheck {
  /** What this comparison is of, e.g. "this surface's work-item capture
   * instant". Rendered only when `observed !== expected`. */
  readonly label: string;
  readonly observed: string;
  readonly expected: string;
}

export interface SubstrateFooterInput {
  readonly model: PocModel;
  readonly escapeHtml: (value: string) => string;
  /** What this surface's own substrate revision is a revision of, e.g.
   * "the observed code structure (git tree)". */
  readonly revisionOf: string;
  /** The surface's own substrate revision, or `null` when this surface's
   * projection carries no observed revision to name. */
  readonly revision: string | null;
  /** Comparisons against the composite evaluation's own identity. A
   * surface with no comparable anchor passes an empty array — an absent
   * check is never rendered as "no skew"; it is simply not asserted. Any
   * entry whose `observed` differs from `expected` renders as explicit
   * skew, never silently folded into the identity line above (N4: "if a
   * surface answers at a different evaluation than the others, render
   * that skew explicitly"). Unreachable on the current `buildPocModel` path
   * as of this writing — every instant and revision there derives from one
   * shared input, so `observed === expected` always — and is exercised only
   * by spread-overridden test fixtures; the check stays wired defensively
   * for the day a surface's substrate is captured independently. */
  readonly skewChecks: readonly SubstrateSkewCheck[];
}

/**
 * The composite evaluation identity, the as-of instant, and what this
 * surface's own substrate revision is a revision of — reusing Polaris's
 * identity line rather than inventing a second computation. Renders any
 * detected skew between this surface's own substrate and the composite
 * evaluation's own project revision / as-of instant explicitly, rather
 * than presenting the two pages as answering at the same evaluation when
 * they do not.
 */
export function substrateEvaluationFooter(input: SubstrateFooterInput): string {
  const { model, escapeHtml, revisionOf, revision, skewChecks } = input;
  const evaluationLine = compositeEvaluationLine(model, escapeHtml);
  if (revision === null) {
    return `${evaluationLine} ${revisionOf}: Unknown — this surface has no observed substrate revision to name.`;
  }
  const revisionLine = `This surface's revision <code data-parity-field="surface-substrate-revision">${escapeHtml(revision)}</code> is a revision of ${revisionOf}.`;
  const skewed = skewChecks.filter((check) => check.observed !== check.expected);
  const skewLine =
    skewed.length === 0
      ? ''
      : ` <strong data-parity-field="evaluation-skew">Skew</strong>: this surface answers at a different evaluation than the composite identity above names — ${skewed
          .map(
            (check) =>
              `${escapeHtml(check.label)} is <code>${escapeHtml(check.observed)}</code>, not <code>${escapeHtml(check.expected)}</code>`,
          )
          .join('; ')}.`;
  return `${evaluationLine} ${revisionLine}${skewLine}`;
}
