// Walkthrough-judgment loader (task 4.6): hermetic classification of what
// the governance tree holds for the scheduled cold-open walkthrough, and
// the real-tree evaluation. Reads only Syzygy's own tree; no Butlers
// repository is touched and no owner act is performed — the fixture pair
// below is written into a fake tree, never to disk.

import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

import { evaluateWalkthroughJudgment } from '@syzygy/three-surface-poc-core';

import { PWB_WALKTHROUGH_SCHEDULE as S, loadWalkthroughJudgmentInputs, pwbWalkthroughExpectations } from './walkthrough-inputs.js';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const EVALUATION_INSTANT = '2026-09-10T00:00:00Z';
const ACT_DATE = '2026-09-06';

function sha256(text: string): string {
  return createHash('sha256').update(text).digest('hex');
}

// The pair in the PWB-REQ-021/022 grammar, spelled here by hand against the
// production schedule rather than imported from the shared fixture.
function runRecordText(): string {
  return [
    '# Cold-open walkthrough execution record',
    '',
    `Record identity: \`${S.runRecordIdentity}\``,
    '',
    `Surface version: \`${S.surfaceVersion}\``,
    '',
    `Evaluation identity: \`${S.evaluationIdentity}\``,
    '',
    `Mode: \`${S.mode}\``,
    '',
    '## Traversed paths',
    '',
    '- `/polaris`',
    '',
    '## Answers',
    '',
    '1. (answer in the reader\'s own words).',
    '',
  ].join('\n');
}

function judgmentText(runDigest: string): string {
  return [
    '# Owner judgment — Polaris cold-open walkthrough',
    '',
    `Date: ${ACT_DATE}`,
    '',
    'Judging party: Tzeusy',
    '',
    `Verdict: \`${S.criterion}=met\``,
    '',
    `Run record: \`${S.runRecordIdentity}@${runDigest}\``,
    '',
    '## Rationale',
    '',
    `Reading \`${S.runRecordIdentity}\` against the Butlers intent tree, every prompt was answered without a surface-caused error.`,
    '',
  ].join('\n');
}

function actRecordText(judgmentDigest: string): string {
  return [
    '# Owner act — Polaris cold-open walkthrough judgment',
    '',
    `Date: ${ACT_DATE}`,
    '',
    'Owner: Tzeusy',
    '',
    `Act identity: \`${S.actIdentity}\``,
    '',
    `Act type: \`${S.actType}\``,
    '',
    'Project identity: `project:syzygy`',
    '',
    `Artifact identity: \`${S.judgmentPath}\``,
    '',
    `Exact digest (SHA-256): \`${judgmentDigest}\``,
    '',
    'Provenance state: `owner-adopted (bootstrap, uncorrelated)` — state (1),',
    'explicitly selected by performing the offered state-(1) phrase',
    '',
    'Supersession / revocation: none — this act supersedes no earlier act',
    '',
    'A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**',
    '',
    '## Ceremony',
    '',
    'The owner performed this one act by writing exactly:',
    '',
    '```text',
    `${S.phrasePrefix}: ${judgmentDigest}`,
    '```',
    '',
    'Frozen provenance:',
    '',
    '- reviewed subject: `48e0f5db645d1fb08e5e3a65c5e50dbcece40412`;',
    `- recording tag: \`${S.recordingTag}\`, on the commit carrying this act record.`,
    '',
    '## Effect',
    '',
    `The judgment is the owner's recorded judgment on the cold-open walkthrough \`${S.runRecordIdentity}\` against the criterion \`${S.criterion}\` (PWB-REQ-021). It authorizes nothing else.`,
    '',
  ].join('\n');
}

interface FakeTree {
  readonly files: Map<string, string>;
  readonly tags: Map<string, string>;
  readonly treePaths: Set<string>;
}

function fakeTree(): FakeTree {
  const run = runRecordText();
  const judgment = judgmentText(sha256(run));
  const files = new Map<string, string>([
    [S.runRecordPath, run],
    [S.judgmentPath, judgment],
    [S.judgmentActRecordPath, actRecordText(sha256(judgment))],
  ]);
  return { files, tags: new Map([[S.recordingTag, '4'.repeat(40)]]), treePaths: new Set([S.judgmentActRecordPath]) };
}

function loaderFor(tree: FakeTree) {
  const root = '/fake/root';
  const relative = (absolute: string): string => absolute.slice(`${root}/`.length);
  return loadWalkthroughJudgmentInputs({
    repoRoot: root,
    evaluationId: 'eval-hermetic',
    evaluationInstant: EVALUATION_INSTANT,
    readFile: (absolute) => {
      const text = tree.files.get(relative(absolute));
      if (text === undefined) throw Object.assign(new Error('ENOENT'), { code: 'ENOENT' });
      return new TextEncoder().encode(text);
    },
    listDirectory: (absolute) => {
      const prefix = `${relative(absolute)}/`;
      return [...tree.files.keys()].filter((path) => path.startsWith(prefix)).map((path) => path.slice(prefix.length));
    },
    runGit: (_root, args) => {
      if (args[0] === 'rev-parse') {
        const tag = /^refs\/tags\/(.+)\^\{commit\}$/.exec(args[3] ?? '')?.[1] ?? '';
        const commit = tree.tags.get(tag);
        if (commit === undefined) throw new Error('unknown tag');
        return `${commit}\n`;
      }
      if (args[0] === 'ls-tree') {
        const path = args[4] ?? '';
        return tree.treePaths.has(path) ? `${path}\n` : '';
      }
      if (args[0] === 'show') {
        const path = (args[1] ?? '').split(':').slice(1).join(':');
        const text = tree.files.get(path);
        if (text === undefined || !tree.treePaths.has(path)) throw new Error('missing tagged record');
        return text;
      }
      throw new Error(`unexpected git ${args.join(' ')}`);
    },
  });
}

describe('the scheduled walkthrough', () => {
  it('names both governance homes and the fixed act vocabulary', () => {
    expect(S.runRecordPath.startsWith('.syzygy/governance/records/')).toBe(true);
    expect(S.judgmentPath.startsWith('.syzygy/governance/decisions/')).toBe(true);
    expect(S.judgmentActRecordPath.startsWith('.syzygy/governance/decisions/')).toBe(true);
    expect(S.runRecordIdentity).toBe('PWB-WALKTHROUGH-001');
    expect(S.mode).toBe('nonvisual-keyboard-only');
    expect(S.phrasePrefix).toBe('ADOPT POLARIS COLD-OPEN WALKTHROUGH JUDGMENT');
    const expectations = pwbWalkthroughExpectations(EVALUATION_INSTANT);
    expect(expectations.judgment.a1).toEqual({ kind: 'absent' });
    expect(expectations.judgment.scopeAnchors).toEqual(['PWB-WALKTHROUGH-001', 'polaris-cold-open-comprehension']);
    expect(expectations.otherActBoundArtifacts).toHaveLength(3);
  });
});

describe('loadWalkthroughJudgmentInputs (hermetic)', () => {
  it('loads a complete pair and evaluates it lawful in state (1)', () => {
    const inputs = loaderFor(fakeTree());
    expect(inputs.runRecord.artifact.kind).toBe('present');
    expect(inputs.judgment.artifact.kind).toBe('present');
    expect(inputs.judgment.actRecord.kind).toBe('owner-act-record');
    expect(inputs.judgment.lifecycle).toEqual({});
    expect(inputs.judgment.recordingTag).toEqual({ kind: 'resolved', commit: '4'.repeat(40) });
    const outcome = evaluateWalkthroughJudgment(inputs).outcome;
    expect(outcome.kind).toBe('lawful');
    expect(outcome.kind === 'lawful' && outcome.stateLabel).toBe('owner-adopted (bootstrap, uncorrelated)');
    expect(outcome.kind === 'lawful' && outcome.independentlyVerified).toBe(false);
    expect(outcome.kind === 'lawful' && outcome.verdict.value).toBe('met');
  });

  it('a missing run record is the absent no-run-record case', () => {
    const tree = fakeTree();
    tree.files.delete(S.runRecordPath);
    const outcome = evaluateWalkthroughJudgment(loaderFor(tree)).outcome;
    expect(outcome.kind === 'absent' && outcome.what).toBe('no-run-record');
    expect(outcome.criterion).toBe('unknown-never-met');
    expect(outcome.verdict).toBeUndefined();
  });

  it('a missing judgment is the absent no-judgment case', () => {
    const tree = fakeTree();
    tree.files.delete(S.judgmentPath);
    const outcome = evaluateWalkthroughJudgment(loaderFor(tree)).outcome;
    expect(outcome.kind === 'absent' && outcome.what).toBe('no-judgment');
  });

  it('a judgment whose act record is missing but tagged is git-ref-only, hence unlawful', () => {
    const tree = fakeTree();
    tree.files.delete(S.judgmentActRecordPath);
    const inputs = loaderFor(tree);
    expect(inputs.judgment.actRecord).toEqual({ kind: 'git-ref-only', ref: S.recordingTag });
    const outcome = evaluateWalkthroughJudgment(inputs).outcome;
    expect(outcome.kind).toBe('unlawful');
    expect(outcome.kind === 'unlawful' && outcome.recorded).toBe('verdict-unlawful');
  });

  it('a judgment whose act record and tag are both missing carries no act, hence absent', () => {
    const tree = fakeTree();
    tree.files.delete(S.judgmentActRecordPath);
    tree.tags.delete(S.recordingTag);
    const inputs = loaderFor(tree);
    expect(inputs.judgment.actRecord).toEqual({ kind: 'absent' });
    const outcome = evaluateWalkthroughJudgment(inputs).outcome;
    expect(outcome.kind === 'absent' && outcome.what).toBe('no-judgment');
  });

  it('an unresolved recording tag on a present act record is unlawful, never lawful', () => {
    const tree = fakeTree();
    tree.tags.delete(S.recordingTag);
    const inputs = loaderFor(tree);
    expect(inputs.judgment.recordingTag).toEqual({ kind: 'unresolved' });
    expect(evaluateWalkthroughJudgment(inputs).outcome.kind).toBe('unlawful');
  });

  it('a later decision superseding the act identity is reported in the lifecycle', () => {
    const tree = fakeTree();
    tree.files.set('.syzygy/governance/decisions/LATER-ACT.md', `# Later act\n\nAct identity: \`LATER-ACT-001\`\n\nSupersession / revocation: supersedes \`${S.actIdentity}\`\n`);
    const inputs = loaderFor(tree);
    expect(inputs.judgment.lifecycle.supersededBy).toBe('.syzygy/governance/decisions/LATER-ACT.md');
    expect(evaluateWalkthroughJudgment(inputs).outcome.kind).toBe('unlawful');
  });
});

describe('loadWalkthroughJudgmentInputs (real tree)', () => {
  it('evaluates the current tree honestly: no run record has been written yet, so the judgment is absent', () => {
    const governanceRevision = execFileSync('git', ['-C', REPO_ROOT, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
    const inputs = loadWalkthroughJudgmentInputs({
      repoRoot: REPO_ROOT,
      governanceRevision,
      evaluationId: 'eval-real',
      evaluationInstant: new Date().toISOString(),
    });
    const outcome = evaluateWalkthroughJudgment(inputs).outcome;
    if (existsSync(join(REPO_ROOT, S.runRecordPath))) {
      // Once the recording session has written the record this test must
      // be re-pinned to the recorded state; until then it must not pass by
      // accident.
      expect(outcome.kind).not.toBe('absent');
    } else {
      expect(outcome.kind === 'absent' && outcome.what).toBe('no-run-record');
      expect(outcome.criterion).toBe('unknown-never-met');
    }
  });
});
