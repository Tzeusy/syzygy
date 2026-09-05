// PWB-REQ-021 readiness conformance (as amended 2026-09-05): the nine
// answer identities, the ten readiness arms, the sweep (every arm reported
// at once), the retained own-words text, and the separation from
// PWB-REQ-022 — readiness never mints `verdict-unlawful` and never changes
// the judgment evaluator's outcome.
//
// Oracle independence: the nine identities and ten arm names are hand-typed
// literals here; the one cross-check against the implementation compares
// the exported tuples against these literals, so an identity or arm added
// or dropped on either side fails.

import { describe, expect, it } from 'vitest';
import {
  ANSWER_IDENTITIES,
  READINESS_ARMS,
  evaluateWalkthroughJudgment,
  evaluateWalkthroughReadiness,
  parseAnswers,
  JUDGMENT_CORRELATION_UNAVAILABLE,
  type ReadinessPopulation,
  type ReadinessTraversal,
  type WalkthroughReadiness,
  type WalkthroughReadinessInputs,
} from './index.js';

const IDENTITIES = [
  'why',
  'promises',
  'refusals-and-rule',
  'capabilities-and-fit',
  'exact-requirement',
  'unknown-or-contradiction',
  'claim-strength',
  'architecture-and-groups',
  'v1-success',
] as const;
const ARMS = [
  'answer-missing',
  'answer-empty',
  'answer-duplicate',
  'answer-unrecognized',
  'anchor-unresolved',
  'surface-mismatch',
  'evaluation-mismatch',
  'path-outside-polaris',
  'resource-breach',
  'authority-unresolvable',
] as const;

const RUN_ID = 'PWB-WALKTHROUGH-2026-09-05';
const RUN_PATH = '.syzygy/governance/records/PWB-WALKTHROUGH-2026-09-05.md';
const SURFACE = 'polaris@0.3.0';
const EVALUATION = 'eval-0007';
const POLARIS = '/polaris';
const EXACT_SOURCE = '/polaris#polaris-source-about-README-md';
const ADMITTED = 'about/README.md';
const UNKNOWN_SOURCE = 'about/lay-and-land/v1.md';

const POPULATION: ReadinessPopulation = {
  kind: 'observed',
  sources: [
    { path: ADMITTED, admitted: true },
    { path: UNKNOWN_SOURCE, admitted: false },
  ],
  limitBreaches: 0,
};
const TRAVERSAL: ReadinessTraversal = {
  polarisRoutes: ['/polaris', '/tailnet/polaris'],
  isExactSourceRoute: (path, sourcePaths) => path === EXACT_SOURCE && sourcePaths.includes(ADMITTED),
};

interface AnswerSpec {
  readonly identity: string;
  readonly text?: string;
  readonly sources?: readonly string[];
  readonly authority?: string;
}

function defaultAnswers(): AnswerSpec[] {
  return IDENTITIES.map((identity, index) => ({
    identity,
    text: `Own words for ${identity} (${index + 1}).`,
    sources: [`\`${ADMITTED}:${index + 3}\``],
    ...(identity === 'exact-requirement' ? { authority: `\`${ADMITTED}\`` } : {}),
  }));
}

interface RunOverrides {
  readonly omit?: readonly string[];
  readonly set?: Readonly<Record<string, string>>;
  readonly paths?: readonly string[] | null;
  readonly answers?: readonly AnswerSpec[] | null;
}

function runRecordText(overrides: RunOverrides = {}): string {
  const head: [string, string][] = [
    ['Record identity:', `\`${RUN_ID}\``],
    ['Surface version:', `\`${SURFACE}\``],
    ['Evaluation identity:', `\`${EVALUATION}\``],
    ['Mode:', '`nonvisual-keyboard-only`'],
  ];
  const lines: string[] = ['# Cold-open walkthrough execution record', ''];
  for (const [label, value] of head) {
    if (overrides.omit?.includes(label)) continue;
    lines.push(`${label} ${overrides.set?.[label] ?? value}`, '');
  }
  if (overrides.paths !== null) {
    lines.push('## Traversed paths', '');
    for (const path of overrides.paths ?? [POLARIS, EXACT_SOURCE, POLARIS]) lines.push(`- \`${path}\``);
    lines.push('');
  }
  if (overrides.answers !== null) {
    lines.push('## Answers', '');
    for (const answer of overrides.answers ?? defaultAnswers()) {
      lines.push(`### ${answer.identity}`, '');
      if (answer.text !== undefined && answer.text !== '') lines.push(answer.text, '');
      if (answer.sources !== undefined) lines.push(`Sources: ${answer.sources.join(', ')}`);
      if (answer.authority !== undefined) lines.push(`Authority: ${answer.authority}`);
      lines.push('');
    }
  }
  lines.push('## Afterword', '', 'Nothing here is an answer.', '');
  return lines.join('\n');
}

function inputs(text: string | undefined, partial: Partial<WalkthroughReadinessInputs> = {}): WalkthroughReadinessInputs {
  return {
    runRecord: {
      path: RUN_PATH,
      artifact: text === undefined ? { kind: 'missing' } : { kind: 'present', bytes: new TextEncoder().encode(text) },
    },
    expectations: { surfaceVersion: SURFACE, evaluationIdentity: EVALUATION },
    traversal: TRAVERSAL,
    population: POPULATION,
    ...partial,
  };
}

function evaluated(result: WalkthroughReadiness): Extract<WalkthroughReadiness, { kind: 'evaluated' }> {
  if (result.kind !== 'evaluated') throw new Error(`expected evaluated, got ${result.kind}`);
  return result;
}
function arms(result: WalkthroughReadiness): string[] {
  return [...new Set(evaluated(result).findings.map((finding) => finding.arm))].sort();
}

describe('PWB-REQ-021 closed vocabularies', () => {
  it('owns exactly the nine answer identities, in the requirement order', () => {
    expect([...ANSWER_IDENTITIES]).toEqual([...IDENTITIES]);
  });
  it('owns exactly the ten readiness arms', () => {
    expect([...READINESS_ARMS]).toEqual([...ARMS]);
  });
});

describe('PWB-REQ-021 readiness: the ready case', () => {
  it('is ready when all nine answers are present, anchored, same-evaluation, Polaris-only and unbreached', () => {
    const result = evaluated(evaluateWalkthroughReadiness(inputs(runRecordText())));
    expect(result.ready).toBe(true);
    expect(result.findings).toEqual([]);
    expect(result.answers.map((answer) => answer.identity)).toEqual([...IDENTITIES]);
    expect(result.surfaceVersion).toBe(SURFACE);
    expect(result.evaluationIdentity).toBe(EVALUATION);
    expect(result.traversedPaths).toEqual([POLARIS, EXACT_SOURCE, POLARIS]);
  });

  it('retains the owner words verbatim and never reads them (a nonsense answer is still ready)', () => {
    const answers = defaultAnswers().map((answer) => (answer.identity === 'why' ? { ...answer, text: 'lorem ipsum 42 !!' } : answer));
    const result = evaluated(evaluateWalkthroughReadiness(inputs(runRecordText({ answers }))));
    expect(result.ready).toBe(true);
    expect(result.answers[0]?.text).toBe('lorem ipsum 42 !!');
    expect(result.answers[0]?.anchors).toEqual([{ path: ADMITTED, line: 3, resolved: true }]);
  });

  it('an anchor into an Unknown (not admitted) source still resolves — the reader saw the source', () => {
    const answers = defaultAnswers().map((answer) => (answer.identity === 'why' ? { ...answer, sources: [`\`${UNKNOWN_SOURCE}:1\``] } : answer));
    const result = evaluated(evaluateWalkthroughReadiness(inputs(runRecordText({ answers }))));
    expect(result.ready).toBe(true);
  });

  it('an answer with no Sources line and no Authority line is still an answer', () => {
    const answers = defaultAnswers().map((answer) => ({ identity: answer.identity, text: answer.text }));
    expect(evaluated(evaluateWalkthroughReadiness(inputs(runRecordText({ answers })))).ready).toBe(true);
  });
});

describe('PWB-REQ-021 readiness arms (each makes readiness false)', () => {
  it('answer-missing: one identity absent', () => {
    const answers = defaultAnswers().filter((answer) => answer.identity !== 'v1-success');
    const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers })));
    expect(arms(result)).toEqual(['answer-missing']);
    expect(evaluated(result).findings[0]?.detail).toContain('v1-success');
  });

  it('answer-missing: no `## Answers` section at all lists all nine', () => {
    const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers: null })));
    expect(arms(result)).toEqual(['answer-missing']);
    expect(evaluated(result).findings).toHaveLength(9);
  });

  it('answer-empty: a heading with only citations under it', () => {
    const answers = defaultAnswers().map((answer) => (answer.identity === 'promises' ? { ...answer, text: '' } : answer));
    const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers })));
    expect(arms(result)).toEqual(['answer-empty']);
  });

  it('answer-duplicate: the same identity twice', () => {
    const answers = [...defaultAnswers(), { identity: 'why', text: 'Again.' }];
    const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers })));
    expect(arms(result)).toEqual(['answer-duplicate']);
  });

  it('answer-unrecognized: a heading naming no PWB-REQ-021 identity', () => {
    const answers = [...defaultAnswers(), { identity: 'favourite-colour', text: 'Blue.' }];
    const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers })));
    expect(arms(result)).toEqual(['answer-unrecognized']);
  });

  it('anchor-unresolved: a path outside the same-evaluation population', () => {
    const answers = defaultAnswers().map((answer) => (answer.identity === 'why' ? { ...answer, sources: ['`about/elsewhere.md:4`'] } : answer));
    expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText({ answers }))))).toEqual(['anchor-unresolved']);
  });

  it('anchor-unresolved: a malformed anchor (no line, or line 0)', () => {
    for (const raw of ['`about/README.md`', '`about/README.md:0`', 'about/README.md:4']) {
      const answers = defaultAnswers().map((answer) => (answer.identity === 'why' ? { ...answer, sources: [raw] } : answer));
      expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText({ answers }))))).toEqual(['anchor-unresolved']);
    }
  });

  it('anchor-unresolved: nothing resolves when the evaluation observed no shape (and the exact-source route has no sources to point at)', () => {
    const result = evaluateWalkthroughReadiness(inputs(runRecordText(), { population: { kind: 'unavailable', reason: 'authority rejected' } }));
    // Every default answer anchors once; the authority also fails; the
    // exact-source traversal names a source this evaluation does not have.
    expect(arms(result)).toEqual(['anchor-unresolved', 'authority-unresolvable', 'path-outside-polaris']);
    expect(evaluated(result).findings.filter((finding) => finding.arm === 'anchor-unresolved')).toHaveLength(9);
    expect(evaluated(result).findings[0]?.detail).toContain('authority rejected');
  });

  it('surface-mismatch: another surface version, or none', () => {
    expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText({ set: { 'Surface version:': '`polaris@0.2.9`' } }))))).toEqual(['surface-mismatch']);
    expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText({ omit: ['Surface version:'] }))))).toEqual(['surface-mismatch']);
  });

  it('evaluation-mismatch: another evaluation identity, or none', () => {
    expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText({ set: { 'Evaluation identity:': '`eval-0006`' } }))))).toEqual(['evaluation-mismatch']);
    expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText({ omit: ['Evaluation identity:'] }))))).toEqual(['evaluation-mismatch']);
  });

  it('path-outside-polaris: a traversal through another surface or a foreign exact-source route', () => {
    for (const path of ['/trajectory', '/orrery', '/', '/polaris#polaris-source-not-in-this-evaluation']) {
      const result = evaluateWalkthroughReadiness(inputs(runRecordText({ paths: [POLARIS, path] })));
      expect(arms(result)).toEqual(['path-outside-polaris']);
      expect(evaluated(result).findings[0]?.detail).toContain(path);
    }
  });

  it('path-outside-polaris: the exact-source predicate is the surface’s, not a spelling rule', () => {
    const traversal: ReadinessTraversal = { polarisRoutes: [POLARIS], isExactSourceRoute: () => false };
    expect(arms(evaluateWalkthroughReadiness(inputs(runRecordText(), { traversal })))).toEqual(['path-outside-polaris']);
  });

  it('resource-breach: any PWB-REQ-006 breach in the evaluation', () => {
    const population: ReadinessPopulation = { ...POPULATION, limitBreaches: 1 };
    const result = evaluateWalkthroughReadiness(inputs(runRecordText(), { population }));
    expect(arms(result)).toEqual(['resource-breach']);
    expect(evaluated(result).findings[0]?.detail).toContain('1 PWB-REQ-006');
  });

  it('authority-unresolvable: a cited authority that is not admitted, absent, or not a backticked path', () => {
    const cases: [string, string][] = [
      [`\`${UNKNOWN_SOURCE}\``, 'is not admitted in this evaluation (Unknown)'],
      ['`about/elsewhere.md`', 'names no source in this evaluation'],
      ['about/README.md', 'is not a backticked path'],
    ];
    for (const [authority, why] of cases) {
      const answers = defaultAnswers().map((answer) => (answer.identity === 'exact-requirement' ? { ...answer, authority } : answer));
      const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers })));
      expect(arms(result)).toEqual(['authority-unresolvable']);
      // Each cause is disclosed as its own reason, not folded into a lookup miss.
      expect(evaluated(result).findings[0]?.detail).toContain(why);
    }
  });

  it('sweeps: every arm is reported at once, not the first failure', () => {
    const answers = [
      ...defaultAnswers()
        .filter((answer) => answer.identity !== 'v1-success')
        .map((answer) =>
          answer.identity === 'why'
            ? { ...answer, text: '', sources: ['`about/elsewhere.md:1`'] }
            : answer.identity === 'exact-requirement'
              ? { ...answer, authority: '`about/elsewhere.md`' }
              : answer,
        ),
      { identity: 'promises', text: 'Again.' },
      { identity: 'extra', text: 'Extra.' },
    ];
    const result = evaluateWalkthroughReadiness(
      inputs(runRecordText({ answers, paths: ['/orrery'], set: { 'Surface version:': '`polaris@0.1.0`', 'Evaluation identity:': '`eval-0001`' } }), {
        population: { ...POPULATION, limitBreaches: 2 },
      }),
    );
    expect(arms(result)).toEqual([...ARMS].sort());
    expect(evaluated(result).ready).toBe(false);
  });
});

describe('PWB-REQ-021 readiness: record availability and separation from PWB-REQ-022', () => {
  it('no run record → no-run-record, not ready, never a verdict', () => {
    const result = evaluateWalkthroughReadiness(inputs(undefined));
    expect(result.kind).toBe('no-run-record');
    expect(result.ready).toBe(false);
    expect(JSON.stringify(result)).not.toContain('verdict');
  });

  it('a non-UTF-8 record is no-run-record', () => {
    const base = inputs(runRecordText());
    const result = evaluateWalkthroughReadiness({ ...base, runRecord: { path: RUN_PATH, artifact: { kind: 'present', bytes: new Uint8Array([0xff, 0xfe, 0x41]) } } });
    expect(result.kind).toBe('no-run-record');
  });

  it('readiness output never carries verdict-unlawful, a verdict, or a score', () => {
    const result = evaluateWalkthroughReadiness(inputs(runRecordText({ answers: null, paths: ['/orrery'] })));
    const json = JSON.stringify(result);
    expect(json).not.toContain('verdict');
    expect(json).not.toContain('score');
    expect(json).not.toContain('met');
  });

  it('a not-ready record leaves the PWB-REQ-022 judgment evaluator’s reading of the run record unchanged', () => {
    // The judgment evaluator parses the same record; the Answers section is
    // not one of its fields, so a broken answer population changes nothing
    // it reports about the run record.
    const ready = runRecordText();
    const notReady = runRecordText({ answers: [{ identity: 'nonsense', text: '' }] });
    const judge = (text: string) =>
      evaluateWalkthroughJudgment({
        evaluationId: 'judgment-eval-0001',
        runRecord: { path: RUN_PATH, artifact: { kind: 'present', bytes: new TextEncoder().encode(text) } },
        judgment: {
          path: '.syzygy/governance/decisions/J.md',
          artifact: { kind: 'missing' },
          actRecord: { path: '.syzygy/governance/decisions/J-ACT.md', artifact: { kind: 'missing' } },
        },
        expectations: {
          owner: 'Tzeusy',
          project: 'project:syzygy',
          criterion: 'polaris-cold-open-comprehension',
          runRecordIdentity: RUN_ID,
          surfaceVersion: SURFACE,
          evaluationIdentity: EVALUATION,
          mode: 'nonvisual-keyboard-only',
          surfaceRoutes: ['/', '/polaris'],
          evaluationInstant: '2026-09-06T10:00:00Z',
          act: {
            actIdentity: 'X',
            actType: 'adopt-walkthrough-judgment',
            phrasePrefix: 'ADOPT',
            recordingTag: 'tag',
            title: 't',
            effect: 'e',
            scopeAnchors: [],
          },
          governingActDate: '2026-09-02',
        } as never,
        correlate: JUDGMENT_CORRELATION_UNAVAILABLE,
      } as never);
    const strip = (value: unknown): string => JSON.stringify(value).replaceAll(/"(runRecordDigest|digest)":"[0-9a-f]+"/g, '"$1":"x"').replaceAll(/sha256:[0-9a-f]+/g, 'sha256:x');
    expect(strip(judge(notReady))).toBe(strip(judge(ready)));
    expect(evaluated(evaluateWalkthroughReadiness(inputs(notReady))).ready).toBe(false);
  });
});

describe('answers grammar', () => {
  it('returns undefined without a `## Answers` section and ends at the next `## ` heading', () => {
    expect(parseAnswers('# Record\n\n## Traversed paths\n\n- `/polaris`\n')).toBeUndefined();
    const parsed = parseAnswers('## Answers\n\n### why\n\nBecause.\n\n## Afterword\n\n### not-an-answer\n\nNo.\n');
    expect(parsed?.map((answer) => answer.identity)).toEqual(['why']);
  });
  it('separates own words from Sources and Authority lines', () => {
    const parsed = parseAnswers('## Answers\n\n### why\n\nFirst line.\n\nSecond line.\n\nSources: `a/b.md:3`, `c.md:10`\nAuthority: `a/b.md`\n');
    expect(parsed?.[0]?.text).toBe('First line.\n\nSecond line.');
    expect(parsed?.[0]?.anchors.map((anchor) => [anchor.path, anchor.line])).toEqual([
      ['a/b.md', 3],
      ['c.md', 10],
    ]);
    expect(parsed?.[0]?.authority?.path).toBe('a/b.md');
  });
});
