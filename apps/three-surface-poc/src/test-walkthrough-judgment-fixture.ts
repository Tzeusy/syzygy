// Test fixture: one lawful cold-open walkthrough pair (run record, judgment,
// owner act record) in the PWB-REQ-021/022 grammar, plus the knobs the
// app-level tests need to reach every presentation state. Never a real
// owner act: identities, dates and digests are fixture values, and the
// judgment evaluator is what decides lawfulness.
import { createHash } from 'node:crypto';

import {
  JUDGMENT_CORRELATION_UNAVAILABLE,
  type JudgmentCorrelator,
  type WalkthroughJudgmentExpectations,
  type WalkthroughJudgmentInputs,
} from '@syzygy/three-surface-poc-core';

export const JUDGMENT_FIXTURE = {
  owner: 'Tzeusy',
  project: 'project:syzygy',
  criterion: 'polaris-cold-open-comprehension',
  runId: 'PWB-WALKTHROUGH-2026-09-05',
  runPath: '.syzygy/governance/records/PWB-WALKTHROUGH-2026-09-05.md',
  judgmentPath: '.syzygy/governance/decisions/PWB-COLD-OPEN-WALKTHROUGH-JUDGMENT-2026-09-05.md',
  surface: 'polaris@0.3.0',
  evaluation: 'eval-0007',
  mode: 'nonvisual-keyboard-only',
  routes: ['/', '/polaris', '/trajectory', '/orrery', '/entry'],
  // Deliberately repeats a path: multiplicity must survive both channels.
  traversed: ['/polaris', '/entry', '/polaris'],
  evaluationInstant: '2026-09-06T10:00:00Z',
  governingActDate: '2026-09-02',
  actDate: '2026-09-05',
  a1Identity: 'a1:audit-record-0042',
  actIdentity: 'PWB-WALKTHROUGH-JUDGMENT-2026-09-05',
  actType: 'adopt-walkthrough-judgment',
  phrasePrefix: 'ADOPT POLARIS COLD-OPEN WALKTHROUGH JUDGMENT',
  recordingTag: 'pwb-adopt-walkthrough-judgment-signed-2026-09-05',
  rationale: 'Reading `PWB-WALKTHROUGH-2026-09-05` against the Butlers intent tree, every RFC7-30 prompt was answered without a surface-caused error.',
} as const;

const F = JUDGMENT_FIXTURE;

function sha256(text: string): string {
  return createHash('sha256').update(text).digest('hex');
}
function bytes(text: string): Uint8Array {
  return new TextEncoder().encode(text);
}

export function fixtureRunRecordText(): string {
  return [
    '# Cold-open walkthrough execution record',
    '',
    `Record identity: \`${F.runId}\``,
    '',
    `Surface version: \`${F.surface}\``,
    '',
    `Evaluation identity: \`${F.evaluation}\``,
    '',
    `Mode: \`${F.mode}\``,
    '',
    'Recorded by: the recording session, 2026-09-05',
    '',
    '## Traversed paths',
    '',
    ...F.traversed.map((path) => `- \`${path}\``),
    '',
    '## Answers',
    '',
    "1. Why Butlers exists: (answer in the reader's own words).",
    '2. One current Unknown or contradiction: (answer).',
    '',
  ].join('\n');
}

export function fixtureJudgmentText(runDigest: string, verdict: 'met' | 'not-met' = 'met', judgingParty: string = F.owner): string {
  return [
    '# Owner judgment — Polaris cold-open walkthrough',
    '',
    `Date: ${F.actDate}`,
    '',
    `Judging party: ${judgingParty}`,
    '',
    `Verdict: \`${F.criterion}=${verdict}\``,
    '',
    `Run record: \`${F.runId}@${runDigest}\``,
    '',
    '## Rationale',
    '',
    F.rationale,
    '',
  ].join('\n');
}

export function fixtureActRecordText(digest: string, state: 'state-1' | 'state-2' = 'state-1'): string {
  const provenance =
    state === 'state-2'
      ? '`Syzygy-verified` — state (2), correlated through the A1 audit record'
      : '`owner-adopted (bootstrap, uncorrelated)` — state (1),\nexplicitly selected by performing the offered state-(1) phrase';
  const a1 = state === 'state-2' ? `\`${F.a1Identity}\`` : '**explicitly absent**';
  return [
    '# Owner act — Polaris cold-open walkthrough judgment',
    '',
    `Date: ${F.actDate}`,
    '',
    `Owner: ${F.owner}`,
    '',
    `Act identity: \`${F.actIdentity}\``,
    '',
    `Act type: \`${F.actType}\``,
    '',
    `Project identity: \`${F.project}\``,
    '',
    `Artifact identity: \`${F.judgmentPath}\``,
    '',
    `Exact digest (SHA-256): \`${digest}\``,
    '',
    `Provenance state: ${provenance}`,
    '',
    'Supersession / revocation: none — this act supersedes no earlier act',
    '',
    `A1 audit-record identity (RFC3-16(b) item 9): ${a1}`,
    '',
    '## Ceremony',
    '',
    'The owner performed this one act by writing exactly:',
    '',
    '```text',
    `${F.phrasePrefix}: ${digest}`,
    '```',
    '',
    'Frozen provenance:',
    '',
    '- reviewed subject: `48e0f5db645d1fb08e5e3a65c5e50dbcece40412`;',
    `- recording tag: \`${F.recordingTag}\`, on the commit carrying this act record.`,
    '',
    '## Effect',
    '',
    `The judgment below is the owner's recorded judgment on the cold-open`,
    `walkthrough \`${F.runId}\` against the criterion`,
    `\`${F.criterion}\` (PWB-REQ-021). It authorizes nothing else.`,
    '',
    '## What this act does not authorize',
    '',
    'Nothing beyond its own authority.',
    '',
  ].join('\n');
}

export function fixtureJudgmentExpectations(a1: 'absent' | 'identity' = 'absent'): WalkthroughJudgmentExpectations {
  return {
    observingProject: F.project,
    owner: F.owner,
    evaluationInstant: F.evaluationInstant,
    governingActInstant: F.governingActDate,
    criterion: F.criterion,
    runRecordIdentity: F.runId,
    surfaceVersion: F.surface,
    evaluationIdentity: F.evaluation,
    mode: F.mode,
    surfaceRoutes: F.routes,
    judgment: {
      artifactPath: F.judgmentPath,
      actIdentity: F.actIdentity,
      actType: F.actType,
      phrasePrefix: F.phrasePrefix,
      recordingTag: F.recordingTag,
      scopeAnchors: [F.runId, F.criterion],
      a1: a1 === 'identity' ? { kind: 'identity', identity: F.a1Identity } : { kind: 'absent' },
    },
    otherActBoundArtifacts: [
      '.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md',
      '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json',
    ],
  };
}

export type JudgmentFixtureState = 'lawful-state-1' | 'lawful-state-2' | 'unlawful' | 'absent-run-record' | 'absent-judgment';

/** One evaluator input per presentation state. `unlawful` names a wrong
 * judging party (case `judging-party-wrong`); `lawful-state-2` pairs a
 * state-(2) act record with a correlator that succeeds. */
export function walkthroughJudgmentFixture(state: JudgmentFixtureState, evaluationId = 'judgment-eval-0001'): WalkthroughJudgmentInputs {
  const runText = fixtureRunRecordText();
  const runDigest = sha256(runText);
  const judgmentText = fixtureJudgmentText(runDigest, 'met', state === 'unlawful' ? 'Somebody Else' : F.owner);
  const judgmentDigest = sha256(judgmentText);
  const actState = state === 'lawful-state-2' ? 'state-2' : 'state-1';
  const correlate: JudgmentCorrelator = state === 'lawful-state-2' ? () => 'succeeded' : JUDGMENT_CORRELATION_UNAVAILABLE;
  return {
    evaluationId,
    runRecord: {
      path: F.runPath,
      artifact: state === 'absent-run-record' ? { kind: 'missing' } : { kind: 'present', bytes: bytes(runText) },
    },
    judgment: {
      path: F.judgmentPath,
      artifact: state === 'absent-judgment' ? { kind: 'missing' } : { kind: 'present', bytes: bytes(judgmentText) },
      actRecord: { kind: 'owner-act-record', text: fixtureActRecordText(judgmentDigest, actState) },
      lifecycle: {},
      recordingTag: { kind: 'resolved', commit: '45fce03ac7929649def093f4563d6e5e98cbff5c' },
    },
    expectations: fixtureJudgmentExpectations(state === 'lawful-state-2' ? 'identity' : 'absent'),
    correlate,
  };
}
