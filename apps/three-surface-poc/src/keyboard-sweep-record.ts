// Pure pieces of `polaris-keyboard-sweep-main.ts` (syzygy-buzg): its
// arguments, and the evaluation a swept page names. A sweep record names its
// subject's digest (each mount's sha256) and, read back from the same served
// bytes, the Butlers revision, the evaluation identity that page renders and
// the walkthrough evaluation identity PWB-REQ-021 records bind to (verification
// rule 11), so a reader can tell which evaluation was swept.

import { dirname, join } from 'node:path';

import type { AccessibilityReport } from './polaris-accessibility.js';

export const KEYBOARD_SWEEP_USAGE =
  'usage: npm run poc:keyboard-sweep -- --task <bead id> (--base-url http://127.0.0.1:<port> | --file <capture.html> [--file …]) [--date YYYY-MM-DD[-suffix]] [--out <record.json>]\n';

/** A bead id: `syzygy-1z3.30`, `syzygy-buzg`. */
const TASK_ID = /^[a-z][a-z0-9]*-[a-z0-9]+(?:\.[a-z0-9]+)*$/;

export interface KeyboardSweepArguments {
  readonly task: string;
  readonly baseUrl: string | undefined;
  readonly files: readonly string[];
  readonly date: string | undefined;
  readonly out: string | undefined;
}

/** The sweep's arguments, or why it refuses to run: the task is required, and exactly one of a daemon or captures. */
export function parseKeyboardSweepArguments(argv: readonly string[]): KeyboardSweepArguments | { readonly refused: string } {
  const valueOf = (name: string): string | undefined => {
    const index = argv.indexOf(name);
    return index === -1 ? undefined : argv[index + 1];
  };
  const files = argv.flatMap((value, index) => (value === '--file' && argv[index + 1] !== undefined ? [argv[index + 1] as string] : []));
  const task = valueOf('--task');
  if (task === undefined) return { refused: 'no --task: name the bead this sweep is evidence for' };
  if (!TASK_ID.test(task)) return { refused: `--task ${JSON.stringify(task)} is not a bead id` };
  const baseUrl = valueOf('--base-url');
  if ((baseUrl === undefined) === (files.length === 0)) return { refused: 'name exactly one of --base-url or --file' };
  return { task, baseUrl, files, date: valueOf('--date'), out: valueOf('--out') };
}

/** Where the record is written, and the one directory the sweep may create: `--out`'s own, else `docs/evidence` for the dated default. */
export function keyboardSweepOutput(parsed: Pick<KeyboardSweepArguments, 'date' | 'out'>, today: string): { readonly file: string; readonly directory: string } {
  const file = parsed.out ?? join('docs', 'evidence', `polaris-keyboard-sweep-${parsed.date ?? today}.json`);
  return { file, directory: dirname(file) };
}

export interface ServedEvaluationBinding {
  /** The Butlers revision the page says it was evaluated at (the currency probe's pinned revision). */
  readonly butlersRevision: string;
  /** `<snapshot>|observed:<asOf>`, the form `evaluationIdentity(model)` gives, from the page footer. */
  readonly evaluationIdentity: string;
  /** The identity a PWB-WALKTHROUGH-001 record binds to, `pwb-eval-…` — what the daemon prints as "Walkthrough evaluation identity", read from the readiness section's expected binding. */
  readonly walkthroughEvaluationIdentity: string;
}

const PINNED_REVISION = /\sdata-currency-probe-pinned="([^"]*)"/g;
const FOOTER = /<footer\b[^>]*>Evaluation <code>([^<]*)<\/code> as of <code>([^<]*)<\/code>/g;
const EXPECTED_WALKTHROUGH = /<code\b[^>]*\sdata-polaris-readiness-expected-evaluation(?:="[^"]*")?[^>]*>([^<]*)<\/code>/g;
/** The walkthrough judgment's identifier grammar (`walkthrough-judgment.ts`). */
const WALKTHROUGH_IDENTITY = /^[a-z0-9][a-z0-9-]*$/;

function unescapeHtml(text: string): string {
  return text.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&');
}

/** The evaluation one served Polaris page renders, read from its own bytes; refused unless each part appears exactly once. */
export function servedEvaluationBinding(html: string): ServedEvaluationBinding | { readonly refused: string } {
  const pinned = [...html.matchAll(PINNED_REVISION)];
  if (pinned.length !== 1) return { refused: `expected one currency-probe pinned revision, found ${pinned.length}` };
  const butlersRevision = unescapeHtml(pinned[0]![1]!);
  if (!/^[0-9a-f]{40}$/.test(butlersRevision)) return { refused: `pinned revision ${JSON.stringify(butlersRevision)} is not a full commit id` };
  const footers = [...html.matchAll(FOOTER)];
  if (footers.length !== 1) return { refused: `expected one evaluation footer, found ${footers.length}` };
  const snapshot = unescapeHtml(footers[0]![1]!);
  const asOf = unescapeHtml(footers[0]![2]!);
  if (snapshot === '' || asOf === '') return { refused: 'the evaluation footer names no snapshot or instant' };
  const walkthrough = [...html.matchAll(EXPECTED_WALKTHROUGH)];
  if (walkthrough.length !== 1) return { refused: `expected one walkthrough evaluation identity, found ${walkthrough.length}` };
  const walkthroughEvaluationIdentity = unescapeHtml(walkthrough[0]![1]!);
  if (!WALKTHROUGH_IDENTITY.test(walkthroughEvaluationIdentity)) return { refused: `walkthrough evaluation identity ${JSON.stringify(walkthroughEvaluationIdentity)} is not an identifier` };
  return { butlersRevision, evaluationIdentity: `${snapshot}|observed:${asOf}`, walkthroughEvaluationIdentity };
}

/** The one evaluation every swept page renders, or why the sweep refuses: a page naming none, or two pages disagreeing. */
export function sweptEvaluation(pages: readonly { readonly mount: string; readonly html: string }[]): ServedEvaluationBinding | { readonly refused: string } {
  let first: { readonly mount: string; readonly binding: ServedEvaluationBinding } | undefined;
  for (const { mount, html } of pages) {
    const binding = servedEvaluationBinding(html);
    if ('refused' in binding) return { refused: `${mount}: the page names no evaluation to record (${binding.refused})` };
    if (first === undefined) first = { mount, binding };
    else if (binding.butlersRevision !== first.binding.butlersRevision || binding.evaluationIdentity !== first.binding.evaluationIdentity) {
      return { refused: `${mount} renders evaluation ${binding.evaluationIdentity} at ${binding.butlersRevision}, not ${first.mount}'s ${first.binding.evaluationIdentity} at ${first.binding.butlersRevision}` };
    } else if (binding.walkthroughEvaluationIdentity !== first.binding.walkthroughEvaluationIdentity) {
      return { refused: `${mount} renders walkthrough evaluation ${binding.walkthroughEvaluationIdentity}, not ${first.mount}'s ${first.binding.walkthroughEvaluationIdentity}` };
    }
  }
  return first === undefined ? { refused: 'no page to sweep' } : first.binding;
}

export interface KeyboardSweep {
  readonly mount: string;
  readonly measuredOn: Readonly<Record<string, unknown>>;
  readonly bytes: number;
  readonly sha256: string;
  readonly report: AccessibilityReport;
}

export function violationsByKind(report: AccessibilityReport): Record<string, number> {
  const kinds: Record<string, number> = {};
  for (const violation of report.violations) kinds[violation.kind] = (kinds[violation.kind] ?? 0) + 1;
  return kinds;
}

/** The sweep's evidence record: the bead, the evaluation swept, and per mount the served digest and what the browser found. */
export function keyboardSweepEvidence(input: {
  readonly task: string;
  readonly evaluation: ServedEvaluationBinding;
  readonly capturedAt: string;
  readonly syzygyHead: string;
  readonly surfaceVersion: string;
  readonly browser: { readonly executable: string; readonly version: string };
  readonly sweeps: readonly KeyboardSweep[];
}): Record<string, unknown> {
  return {
    task: input.task,
    requirement: ['PWB-REQ-016'],
    butlersRevision: input.evaluation.butlersRevision,
    evaluationIdentity: input.evaluation.evaluationIdentity,
    walkthroughEvaluationIdentity: input.evaluation.walkthroughEvaluationIdentity,
    evaluationReadFrom: "each swept page: the currency probe's pinned revision, the footer's snapshot and as-of instant, and the walkthrough readiness section's expected evaluation identity, equal on every mount (keyboard-sweep-record.ts)",
    capturedAt: input.capturedAt,
    syzygyHead: input.syzygyHead,
    surfaceVersion: input.surfaceVersion,
    browser: input.browser,
    method: 'checkPolarisAccessibility over each served body, retained in a private temporary directory and opened as a file URL; fragment activations stay in-document, so the served bytes are the whole input',
    mounts: input.sweeps.map((sweep) => ({
      mount: sweep.mount,
      measuredOn: sweep.measuredOn,
      bytes: sweep.bytes,
      sha256: sweep.sha256,
      population: sweep.report.focusTrace.population,
      reached: sweep.report.focusTrace.reached,
      activations: sweep.report.activations.length,
      disclosures: sweep.report.disclosures,
      contrastMeasured: sweep.report.contrast.measured,
      violations: sweep.report.violations.length,
      violationsByKind: violationsByKind(sweep.report),
      firstViolations: sweep.report.violations.slice(0, 5),
    })),
    totals: { mounts: input.sweeps.length, violations: input.sweeps.reduce((sum, sweep) => sum + sweep.report.violations.length, 0) },
  };
}
