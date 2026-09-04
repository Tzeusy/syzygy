// Walkthrough-judgment inputs (task 4.6, PWB-REQ-021/022).
//
// The daemon evaluates the cold-open walkthrough pair — execution record
// under `.syzygy/governance/records/`, owner judgment under
// `.syzygy/governance/decisions/` with its owner act record — from the
// Syzygy governance tree on every model build, the way the three body-read
// authorities are. The controlled expectations live here, never in the
// artifacts. Until the recording session writes the run record the pair is
// absent and the evaluation is `absent` (Unknown, never met) — no verdict is
// invented, and nothing here performs an owner act.

import { readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';

import {
  JUDGMENT_CORRELATION_UNAVAILABLE,
  type ActRecordInput,
  type WalkthroughJudgmentExpectations,
  type WalkthroughJudgmentInputs,
} from '@syzygy/three-surface-poc-core';

import {
  actIdentityOf,
  classifyMissingRecord,
  defaultRunGit,
  gitTreeReaders,
  lifecycleFor,
  readArtifact,
  readText,
  resolveRecordingTag,
  type LoadGovernanceInputsOptions,
} from './governance-inputs.js';

/** The one scheduled walkthrough. Identities are serial, not dated, so the
 * record and act may be performed on whatever day the owner chooses.
 * `evaluationIdentity` is the slug the recording session assigns to the
 * evaluation the owner traversed (the daemon's own evaluation id carries
 * colons and is not a run-record identity); it is fixed when the run
 * record is written and before the judgment packet is frozen. */
export const PWB_WALKTHROUGH_SCHEDULE = {
  criterion: 'polaris-cold-open-comprehension',
  runRecordIdentity: 'PWB-WALKTHROUGH-001',
  runRecordPath: '.syzygy/governance/records/PWB-WALKTHROUGH-001.md',
  judgmentPath: '.syzygy/governance/decisions/PWB-COLD-OPEN-WALKTHROUGH-JUDGMENT-001.md',
  judgmentActRecordPath: '.syzygy/governance/decisions/PWB-COLD-OPEN-WALKTHROUGH-JUDGMENT-ACT.md',
  surfaceVersion: 'polaris@0.0.0',
  evaluationIdentity: 'not-yet-recorded',
  mode: 'nonvisual-keyboard-only',
  surfaceRoutes: ['/', '/polaris', '/trajectory', '/orrery', '/trajectory/materialize'],
  actIdentity: 'PWB-COLD-OPEN-WALKTHROUGH-JUDGMENT-001',
  actType: 'adopt-walkthrough-judgment',
  phrasePrefix: 'ADOPT POLARIS COLD-OPEN WALKTHROUGH JUDGMENT',
  recordingTag: 'pwb-adopt-walkthrough-judgment-signed-001',
} as const;

// The other act-bound artifacts a judgment act could be mis-paired to.
const OTHER_ACT_BOUND_ARTIFACTS = [
  '.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md',
  '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json',
  '.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json',
] as const;

/** The controlled evaluation input for the scheduled walkthrough. */
export function pwbWalkthroughExpectations(evaluationInstant: string): WalkthroughJudgmentExpectations {
  const s = PWB_WALKTHROUGH_SCHEDULE;
  return {
    observingProject: 'project:syzygy',
    owner: 'Tzeusy',
    evaluationInstant,
    // The PWB state-(1) amendment sign-off; PWB-REQ-022 accepts state (1)
    // only from that act onward.
    governingActInstant: '2026-09-02',
    criterion: s.criterion,
    runRecordIdentity: s.runRecordIdentity,
    surfaceVersion: s.surfaceVersion,
    evaluationIdentity: s.evaluationIdentity,
    mode: s.mode,
    surfaceRoutes: [...s.surfaceRoutes],
    judgment: {
      artifactPath: s.judgmentPath,
      actIdentity: s.actIdentity,
      actType: s.actType,
      phrasePrefix: s.phrasePrefix,
      recordingTag: s.recordingTag,
      scopeAnchors: [s.runRecordIdentity, s.criterion],
      a1: { kind: 'absent' },
    },
    otherActBoundArtifacts: [...OTHER_ACT_BOUND_ARTIFACTS],
  };
}

export function loadWalkthroughJudgmentInputs(options: LoadGovernanceInputsOptions): WalkthroughJudgmentInputs {
  const runGit = options.runGit ?? defaultRunGit;
  const repoRoot = resolve(options.repoRoot);
  const tree = options.governanceRevision === undefined
    ? undefined
    : gitTreeReaders(runGit, repoRoot, options.governanceRevision);
  const read = options.readFile ?? tree?.read ?? ((path: string) => new Uint8Array(readFileSync(path)));
  const list = options.listDirectory ?? tree?.list ?? ((path: string) => readdirSync(path));
  const s = PWB_WALKTHROUGH_SCHEDULE;
  const expectations = pwbWalkthroughExpectations(options.evaluationInstant);

  const runArtifact = readArtifact(read, join(repoRoot, s.runRecordPath));
  const judgmentArtifact = readArtifact(read, join(repoRoot, s.judgmentPath));
  const recordText = readText(read, join(repoRoot, s.judgmentActRecordPath));
  const actRecord: ActRecordInput =
    recordText === undefined
      ? classifyMissingRecord(runGit, repoRoot, s.recordingTag, judgmentArtifact)
      : { kind: 'owner-act-record', text: recordText };

  return {
    evaluationId: options.evaluationId,
    runRecord: { path: s.runRecordPath, artifact: runArtifact },
    judgment: {
      path: s.judgmentPath,
      artifact: judgmentArtifact,
      actRecord,
      lifecycle: lifecycleFor(read, list, repoRoot, s.judgmentActRecordPath, recordText === undefined ? undefined : actIdentityOf(recordText)),
      recordingTag: resolveRecordingTag(runGit, repoRoot, s.recordingTag, s.judgmentActRecordPath, recordText),
    },
    expectations,
    correlate: JUDGMENT_CORRELATION_UNAVAILABLE,
  };
}
