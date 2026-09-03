// PWB mutation plan — pure source transformations for the PWB-REQ-005
// mutation-proof (rule 6: mutate the input and confirm the check fails,
// per predicate, before trusting it).
//
// Two mutation shapes:
//   * `disable-predicate`: a `// mutation-point: <case>` comment line
//     followed by an `if (<cond>) ...` line. The condition is wrapped as
//     `if (false && (<cond>))`, so the predicate can never fire. The
//     independent test must then fail on exactly that case's instances.
//   * `literal`: a named, hand-listed replacement of one exact source
//     fragment (state collapse, disclosure forcing, history rewrite, …).
//
// This module never touches the filesystem; the runner
// (`pwb-mutation-run-main.ts`) reads, mutates, tests and restores.

export interface PredicateMutation {
  readonly kind: 'disable-predicate';
  readonly id: string;
  readonly file: string;
  readonly caseName: string;
  readonly line: number;
}

export interface LiteralMutation {
  readonly kind: 'literal';
  readonly id: string;
  readonly file: string;
  readonly description: string;
  readonly from: string;
  readonly to: string;
  // Test full names (substrings) that MUST be among the failures.
  readonly mustFail: readonly string[];
}

export type Mutation = PredicateMutation | LiteralMutation;

export const CORE_SOURCE = 'packages/three-surface-poc-core/src/body-read-authority.ts';
export const OBSERVER_SOURCE = 'packages/three-surface-poc-core/src/project-shape-observer.ts';
export const DISCLOSURE_SOURCE = 'packages/three-surface-poc-core/src/authority-disclosure.ts';

const MARKER = /^\s*\/\/ mutation-point: ([a-z0-9-]+)(?: \|.*)?$/;

// The PWB-REQ-005 authorities; a common case's predicate is shared by all
// three, so disabling it must fail all three instances.
const AUTHORITIES = ['consent', 'policy', 'registry'] as const;

export function listPredicateMutations(file: string, source: string): readonly PredicateMutation[] {
  const lines = source.split('\n');
  const found: PredicateMutation[] = [];
  lines.forEach((line, index) => {
    const marker = MARKER.exec(line);
    if (marker === null) return;
    const next = lines[index + 1] ?? '';
    if (!/^\s*if \(/.test(next)) return;
    const caseName = marker[1] ?? '';
    found.push({ kind: 'disable-predicate', id: `${file}#${caseName}`, file, caseName, line: index + 2 });
  });
  return found;
}

// Test-name substrings a predicate mutation must fail: each instance of
// the case in the hand-typed table. Authority-specific cases (`consent:`,
// `policy:`, `registry:` prefixed markers are not used; specific cases
// are unprefixed but unique to one authority) resolve to one instance.
export function expectedFailuresForPredicate(mutation: PredicateMutation, specificCaseIds: readonly string[]): readonly string[] {
  if (mutation.caseName === 'gate') return ['PWB-REQ-005 invalid cases (195)'];
  const specific = specificCaseIds.filter((id) => id.endsWith(`:${mutation.caseName}`));
  if (specific.length === 1) return [`${specific[0]} →`];
  return AUTHORITIES.map((authority) => `${authority}:${mutation.caseName} →`);
}

// Wrap the condition of the `if (` on `mutation.line` as `false && (…)`.
export function applyPredicateMutation(source: string, mutation: PredicateMutation): string {
  const lines = source.split('\n');
  const index = mutation.line - 1;
  const line = lines[index];
  if (line === undefined) throw new Error(`${mutation.id}: line ${mutation.line} does not exist`);
  const open = line.indexOf('if (');
  if (open < 0) throw new Error(`${mutation.id}: line ${mutation.line} is not an if statement`);
  const start = open + 'if ('.length;
  let depth = 1;
  let end = -1;
  for (let cursor = start; cursor < line.length; cursor += 1) {
    const char = line[cursor];
    if (char === '(') depth += 1;
    else if (char === ')') {
      depth -= 1;
      if (depth === 0) {
        end = cursor;
        break;
      }
    }
  }
  if (end < 0) throw new Error(`${mutation.id}: unbalanced condition on line ${mutation.line}`);
  const condition = line.slice(start, end);
  lines[index] = `${line.slice(0, start)}false && (${condition})${line.slice(end)}`;
  return lines.join('\n');
}

export function applyLiteralMutation(source: string, mutation: LiteralMutation): string {
  const occurrences = source.split(mutation.from).length - 1;
  if (occurrences !== 1) {
    throw new Error(`${mutation.id}: expected exactly one occurrence of the fragment, found ${occurrences}`);
  }
  return source.replace(mutation.from, mutation.to);
}

export function applyMutation(source: string, mutation: Mutation): string {
  return mutation.kind === 'disable-predicate'
    ? applyPredicateMutation(source, mutation)
    : applyLiteralMutation(source, mutation);
}

const STATE_1_SENTENCE =
  "Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance.";

// Hand-listed semantic mutations beyond single-predicate disabling.
export const LITERAL_MUTATIONS: readonly LiteralMutation[] = [
  {
    kind: 'literal',
    id: 'exact-state-collapse',
    file: CORE_SOURCE,
    description: 'a valid state-(2) act is recorded as state (1): exact state is not preserved',
    from: 'const provenance: ProvenanceLabel = claimed;',
    to: "const provenance: ProvenanceLabel = 'state-1';",
    mustFail: ['valid triple state-2/state-2/state-2', 'valid triple state-1/state-1/state-2', 'later correlation renders state (2)'],
  },
  {
    kind: 'literal',
    id: 'exact-state-inflate',
    file: CORE_SOURCE,
    description: 'a valid state-(1) act is recorded as state (2): state (1) claims independent verification',
    from: 'const provenance: ProvenanceLabel = claimed;',
    to: "const provenance: ProvenanceLabel = 'state-2';",
    mustFail: ['valid triple state-1/state-1/state-1', 'evaluates the three real 2026-09-02 PWB acts'],
  },
  {
    kind: 'literal',
    id: 'failed-correlation-downgrades-to-state-1',
    file: CORE_SOURCE,
    description: 'a failed A1 correlation falls back to state (1) instead of invalidating the act',
    from: "if (correlation === 'failed') return invalid('state-2-correlation-failed', 'claimed state (2) but A1 correlation failed; no fallback to state (1)');",
    to: "if (correlation === 'failed') claimed = 'state-1';",
    mustFail: ['consent:state-2-correlation-failed →', 'policy:state-2-correlation-failed →', 'registry:state-2-correlation-failed →', 'does not downgrade to state (1)'],
  },
  {
    kind: 'literal',
    id: 'admits-always',
    file: CORE_SOURCE,
    description: 'the evaluation admits regardless of the three states',
    from: 'const admits = valid.length === AUTHORITY_KINDS.length;',
    to: 'const admits = true;',
    mustFail: ['consent:project-identity-missing →', 'registry:write-surface-wrong →', 'a missing consent artifact yields zero reads'],
  },
  {
    kind: 'literal',
    id: 'contradiction-suppressed',
    file: CORE_SOURCE,
    description: 'a non-admitting evaluation records no RFC3-16(a) contradiction',
    from: 'contradiction: admits ? undefined : contradictionFor(states),',
    to: 'contradiction: undefined,',
    mustFail: ['consent:project-identity-missing →', 'registry:write-surface-wrong →'],
  },
  {
    kind: 'literal',
    id: 'history-rewrite-on-later-correlation',
    file: CORE_SOURCE,
    description: 'appending a later evaluation rewrites earlier entries to the later consent state',
    from: 'return Object.freeze([...history, deepFreeze(evaluation)]);',
    to: 'return Object.freeze([...history.map((earlier) => ({ ...earlier, consent: evaluation.consent })), deepFreeze(evaluation)]);',
    mustFail: ['later correlation renders state (2)'],
  },
  {
    kind: 'literal',
    id: 'history-duplicate-accepted',
    file: CORE_SOURCE,
    description: 'a duplicate evaluation id is appended instead of rejected',
    from: 'if (earlier.evaluationId === evaluation.evaluationId) {',
    to: 'if (false && earlier.evaluationId === evaluation.evaluationId) {',
    mustFail: ['later correlation renders state (2)'],
  },
  {
    kind: 'literal',
    id: 'disclosure-independently-verified-forced',
    file: DISCLOSURE_SOURCE,
    description: 'every valid act is disclosed as independently verified',
    from: "independentlyVerified: state.provenance === 'state-2',",
    to: 'independentlyVerified: true,',
    mustFail: ['valid triple state-1/state-1/state-1', 'evaluates the three real 2026-09-02 PWB acts'],
  },
  {
    kind: 'literal',
    id: 'disclosure-state-1-label-inflated',
    file: DISCLOSURE_SOURCE,
    description: 'a state-(1) act is labelled with the state-(2) label',
    from: "state: state.provenance === 'state-2' ? STATE_2_LABEL : STATE_1_LABEL,",
    to: 'state: STATE_2_LABEL,',
    mustFail: ['valid triple state-1/state-1/state-1', 'evaluates the three real 2026-09-02 PWB acts'],
  },
  {
    kind: 'literal',
    id: 'state-1-sentence-altered',
    file: DISCLOSURE_SOURCE,
    description: 'the exact state-(1) sentence is altered',
    from: STATE_1_SENTENCE,
    to: 'Owner-trusted and verified; digest proves authorship.',
    mustFail: ['the state-(1) disclosure constant is exactly the PWB-REQ-005 sentence', 'valid triple state-1/state-1/state-1'],
  },
  {
    kind: 'literal',
    id: 'invalid-act-disclosed-as-verified',
    file: DISCLOSURE_SOURCE,
    description: 'an invalid act is disclosed as independently verified',
    from: "      state: 'invalid act',\n      independentlyVerified: false,",
    to: "      state: 'invalid act',\n      independentlyVerified: true,",
    mustFail: ['consent:project-identity-missing →'],
  },
];
