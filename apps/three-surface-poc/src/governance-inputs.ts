// Governance-inputs loader — turns the Syzygy governance tree into the
// controlled inputs of `evaluateBodyReadAuthority` (PWB-REQ-005).
//
// This is the only module that knows WHERE the three PWB authority
// artifacts and their owner-act records live and WHAT the controlled
// expectations are. It reads Syzygy's own governance tree only — never a
// Butlers repository. Everything it returns is bytes/text plus git
// metadata; the evaluator decides validity.
//
// Expectations are hard-coded here, not read from the artifacts: PWB-REQ-005
// defines "wrong but present" as "semantically different from the
// controlled evaluation input", so the input must come from outside the
// artifacts being judged.

import { execFileSync } from 'node:child_process';
import { readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';

import {
  A1_CORRELATION_UNAVAILABLE,
  AUTHORITY_KINDS,
  supersessionTargetsOf,
  type ActRecordInput,
  type ArtifactInput,
  type AuthorityInput,
  type AuthorityKind,
  type BodyReadAuthorityExpectations,
  type BodyReadAuthorityInputs,
  type LifecycleInput,
  type RecordingTagResolution,
} from '@syzygy/three-surface-poc-core';

export const PWB_GOVERNANCE_ROOT = '.syzygy/governance';

// Paths relative to the repository root.
export const PWB_AUTHORITY_ARTIFACTS: Readonly<Record<AuthorityKind, string>> = {
  consent: '.syzygy/governance/decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md',
  policy: '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json',
  registry: '.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json',
};

export const PWB_ACT_RECORDS: Readonly<Record<AuthorityKind, string>> = {
  consent: '.syzygy/governance/decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md',
  policy: '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md',
  registry: '.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md',
};

// The controlled evaluation input for the one consented Butlers slice.
export function pwbAuthorityExpectations(evaluationInstant: string): BodyReadAuthorityExpectations {
  return {
    observingProject: 'project:syzygy',
    configuredRepository: 'repository:butlers-configured-poc',
    contentClass: 'declared-project-shape-text',
    owner: 'Tzeusy',
    governanceHome: '.syzygy/governance/declarations/adapter-registry',
    policyVersion: '1.0.0-candidate.4',
    evaluationInstant,
    // The PWB state-(1) amendment sign-off; earlier acts predate the
    // authority that makes state (1) acceptable for PWB-REQ-005.
    governingActInstant: '2026-09-02',
    authorities: {
      consent: {
        artifactPath: PWB_AUTHORITY_ARTIFACTS.consent,
        actIdentity: 'PWB-BUTLERS-OBSERVATION-CONSENT-2026-09-02',
        actType: 'consent-observation',
        phrasePrefix: 'CONSENT TO BUTLERS PROJECT-SHAPE OBSERVATION',
        recordingTag: 'pwb-consent-observation-signed-2026-09-02',
        scopeAnchors: ['project:syzygy', 'repository:butlers-configured-poc', 'declared-project-shape-text', 'read-only'],
        a1: { kind: 'absent' },
      },
      policy: {
        artifactPath: PWB_AUTHORITY_ARTIFACTS.policy,
        actIdentity: 'PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-2026-09-02',
        actType: 'approve-policy',
        phrasePrefix: 'APPROVE POLARIS BUTLERS SECRET-CLASSIFICATION POLICY',
        recordingTag: 'pwb-approve-policy-signed-2026-09-02',
        scopeAnchors: ['polaris-butlers-project-shape-secrets', 'project:syzygy'],
        a1: { kind: 'absent' },
      },
      registry: {
        artifactPath: PWB_AUTHORITY_ARTIFACTS.registry,
        actIdentity: 'PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-2026-09-02',
        actType: 'adopt-registry-entry',
        phrasePrefix: 'ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY',
        recordingTag: 'pwb-adopt-registry-entry-signed-2026-09-02',
        scopeAnchors: [
          'polaris-butlers-project-shape',
          '.syzygy/governance/declarations/adapter-registry',
          'project:syzygy',
          'read-only',
          'empty write surface',
        ],
        a1: { kind: 'absent' },
      },
    },
  };
}

export interface LoadGovernanceInputsOptions {
  // Syzygy repository root (the directory containing `.syzygy/`).
  readonly repoRoot: string;
  readonly evaluationId: string;
  readonly evaluationInstant: string;
  // Injectable for hermetic tests; defaults shell `git -C <repoRoot>`.
  readonly runGit?: (repoRoot: string, args: readonly string[]) => string;
  readonly readFile?: (absolutePath: string) => Uint8Array;
  readonly listDirectory?: (absolutePath: string) => readonly string[];
}

function defaultRunGit(repoRoot: string, args: readonly string[]): string {
  return execFileSync('git', ['--no-optional-locks', '-C', repoRoot, ...args], {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'ignore'],
  });
}

function readArtifact(read: (path: string) => Uint8Array, absolutePath: string): ArtifactInput {
  try {
    return { kind: 'present', bytes: read(absolutePath) };
  } catch (error) {
    const code = (error as { code?: string }).code;
    return code === 'ENOENT' ? { kind: 'missing' } : { kind: 'unreadable' };
  }
}

function readText(read: (path: string) => Uint8Array, absolutePath: string): string | undefined {
  try {
    return new TextDecoder('utf-8', { fatal: true }).decode(read(absolutePath));
  } catch {
    return undefined;
  }
}

function tagExists(runGit: LoadGovernanceInputsOptions['runGit'] & {}, repoRoot: string, tag: string): string | undefined {
  try {
    const commit = runGit(repoRoot, ['rev-parse', '--verify', '--quiet', `refs/tags/${tag}^{commit}`]).trim();
    return /^[0-9a-f]{40}$/.test(commit) ? commit : undefined;
  } catch {
    return undefined;
  }
}

// A recording tag resolves only if it names a commit whose tree carries
// the act record at the recorded path.
function resolveRecordingTag(
  runGit: LoadGovernanceInputsOptions['runGit'] & {},
  repoRoot: string,
  tag: string,
  recordPath: string,
): RecordingTagResolution {
  const commit = tagExists(runGit, repoRoot, tag);
  if (commit === undefined) return { kind: 'unresolved' };
  try {
    const listing = runGit(repoRoot, ['ls-tree', '--name-only', commit, '--', recordPath]);
    return listing.split('\n').map((line) => line.trim()).includes(recordPath)
      ? { kind: 'resolved', commit }
      : { kind: 'unresolved' };
  } catch {
    return { kind: 'unresolved' };
  }
}

// What stands in for an act record when the record file is absent: a git
// tag alone, an artifact status stamp alone, or nothing. Each is one of
// PWB-REQ-005's non-substitutes and is rejected by the evaluator.
function classifyMissingRecord(
  runGit: LoadGovernanceInputsOptions['runGit'] & {},
  repoRoot: string,
  tag: string,
  artifact: ArtifactInput,
): ActRecordInput {
  if (tagExists(runGit, repoRoot, tag) !== undefined) return { kind: 'git-ref-only', ref: tag };
  if (artifact.kind === 'present') {
    const text = new TextDecoder('utf-8').decode(artifact.bytes);
    const stamp = /^(Status|"status"):\s*(.+)$/m.exec(text);
    if (stamp !== null) return { kind: 'tree-attribution-only', stamp: stamp[0] };
  }
  return { kind: 'absent' };
}

// Every decisions/*.md other than the act's own record is scanned for a
// later act that supersedes or revokes this act identity.
function lifecycleFor(
  read: (path: string) => Uint8Array,
  list: (path: string) => readonly string[],
  repoRoot: string,
  ownRecordPath: string,
  actIdentity: string | undefined,
): LifecycleInput {
  if (actIdentity === undefined) return {};
  const decisionsDir = join(repoRoot, PWB_GOVERNANCE_ROOT, 'decisions');
  let names: readonly string[];
  try {
    names = list(decisionsDir);
  } catch {
    return {};
  }
  let supersededBy: string | undefined;
  let revokedBy: string | undefined;
  for (const name of names) {
    if (!name.endsWith('.md')) continue;
    const relative = `${PWB_GOVERNANCE_ROOT}/decisions/${name}`;
    if (relative === ownRecordPath) continue;
    const text = readText(read, join(decisionsDir, name));
    if (text === undefined) continue;
    for (const entry of supersessionTargetsOf(text)) {
      if (entry.target !== actIdentity) continue;
      if (entry.relation === 'supersedes') supersededBy ??= relative;
      else revokedBy ??= relative;
    }
  }
  return { ...(supersededBy === undefined ? {} : { supersededBy }), ...(revokedBy === undefined ? {} : { revokedBy }) };
}

function actIdentityOf(text: string): string | undefined {
  const match = /^Act identity: `([^`]+)`\s*$/m.exec(text);
  return match?.[1];
}

export function loadBodyReadAuthorityInputs(options: LoadGovernanceInputsOptions): BodyReadAuthorityInputs {
  const runGit = options.runGit ?? defaultRunGit;
  const read = options.readFile ?? ((path: string) => new Uint8Array(readFileSync(path)));
  const list = options.listDirectory ?? ((path: string) => readdirSync(path));
  const repoRoot = resolve(options.repoRoot);
  const expectations = pwbAuthorityExpectations(options.evaluationInstant);

  const load = (kind: AuthorityKind): AuthorityInput => {
    const artifactPath = PWB_AUTHORITY_ARTIFACTS[kind];
    const recordPath = PWB_ACT_RECORDS[kind];
    const tag = expectations.authorities[kind].recordingTag;
    const artifact = readArtifact(read, join(repoRoot, artifactPath));
    const recordText = readText(read, join(repoRoot, recordPath));
    const actRecord: ActRecordInput =
      recordText === undefined
        ? classifyMissingRecord(runGit, repoRoot, tag, artifact)
        : { kind: 'owner-act-record', text: recordText };
    return {
      artifact,
      actRecord,
      lifecycle: lifecycleFor(read, list, repoRoot, recordPath, recordText === undefined ? undefined : actIdentityOf(recordText)),
      recordingTag: resolveRecordingTag(runGit, repoRoot, tag, recordPath),
    };
  };

  const [consent, policy, registry] = AUTHORITY_KINDS.map(load) as [AuthorityInput, AuthorityInput, AuthorityInput];
  return {
    evaluationId: options.evaluationId,
    consent,
    policy,
    registry,
    expectations,
    correlate: A1_CORRELATION_UNAVAILABLE,
  };
}

// Shared with the walkthrough-judgment loader (task 4.6): the same
// artifact/act-record/tag/lifecycle classification, so a judgment act is
// read under exactly the rules the three body-read authorities are.
export { classifyMissingRecord, lifecycleFor, actIdentityOf, defaultRunGit, readArtifact, readText, resolveRecordingTag };
