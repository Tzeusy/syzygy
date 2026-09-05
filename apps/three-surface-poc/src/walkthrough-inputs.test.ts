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

import {
  PWB_WALKTHROUGH_SCHEDULE as S,
  loadWalkthroughJudgmentInputs,
  pwbReadinessTraversal,
  pwbSurfaceVersion,
  pwbWalkthroughExpectations,
  walkthroughJudgmentInputsFor,
} from './walkthrough-inputs.js';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const EVALUATION_INSTANT = '2026-09-10T00:00:00Z';
const ACT_DATE = '2026-09-06';
/** A binding as the daemon would derive it: the Polaris tree id at the
 * observer revision and the evaluation's observation-digest identity. */
const BINDING = { surfaceVersion: 'polaris@0123456789ab', evaluationIdentity: 'pwb-eval-0123456789abcdef01234567' } as const;
const SURFACE_TREE_ID = '0123456789abcdef0123456789abcdef01234567';

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
    `Surface version: \`${BINDING.surfaceVersion}\``,
    '',
    `Evaluation identity: \`${BINDING.evaluationIdentity}\``,
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
    binding: BINDING,
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
      throw new Error(`unexpected git ${args.join(' ')}`);
    },
    readGitBlob: (_root, object) => {
      const path = object.split(':').slice(1).join(':');
      const text = tree.files.get(path);
      if (text === undefined || !tree.treePaths.has(path)) throw new Error('missing tagged record');
      return new TextEncoder().encode(text);
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
    const expectations = pwbWalkthroughExpectations(EVALUATION_INSTANT, BINDING);
    expect(expectations.judgment.a1).toEqual({ kind: 'absent' });
    expect(expectations.judgment.scopeAnchors).toEqual(['PWB-WALKTHROUGH-001', 'polaris-cold-open-comprehension']);
    expect(expectations.otherActBoundArtifacts).toHaveLength(3);
  });

  it('carries no placeholder binding: surface version and evaluation identity come only from the bound evaluation', () => {
    expect(Object.keys(S)).not.toContain('surfaceVersion');
    expect(Object.keys(S)).not.toContain('evaluationIdentity');
    const expectations = pwbWalkthroughExpectations(EVALUATION_INSTANT, BINDING);
    expect(expectations.surfaceVersion).toBe(BINDING.surfaceVersion);
    expect(expectations.evaluationIdentity).toBe(BINDING.evaluationIdentity);
    expect(JSON.stringify(S)).not.toMatch(/0\.0\.0|not-yet-recorded/);
  });

  it('admits Polaris routes only (PWB-REQ-021 as amended): the page and its exact-source route, direct and mounted', () => {
    expect([...S.surfaceRoutes]).toEqual(['/polaris', '/butlers-syzygy/polaris', '/polaris/source', '/butlers-syzygy/polaris/source']);
    for (const other of ['/', '/trajectory', '/orrery', '/trajectory/materialize', '/api/poc']) {
      expect(S.surfaceRoutes as readonly string[]).not.toContain(other);
    }
  });
});

describe('pwbSurfaceVersion', () => {
  it('is the Polaris source tree id at the observer revision, and nothing else moves it', () => {
    const calls: string[][] = [];
    const runGit = (_root: string, args: readonly string[]): string => {
      calls.push([...args]);
      return `${SURFACE_TREE_ID}\n`;
    };
    expect(pwbSurfaceVersion(runGit, '/fake/root', 'a'.repeat(40))).toBe('polaris@0123456789ab');
    expect(calls).toEqual([['rev-parse', `${'a'.repeat(40)}:apps/three-surface-poc/src`]]);
  });

  it('fails closed to polaris@unresolved when the tree cannot be resolved or is not a tree id', () => {
    expect(pwbSurfaceVersion(() => { throw new Error('bad revision'); }, '/fake/root', 'deadbeef')).toBe('polaris@unresolved');
    expect(pwbSurfaceVersion(() => 'fatal: not a tree\n', '/fake/root', 'deadbeef')).toBe('polaris@unresolved');
    expect(pwbSurfaceVersion(() => '', '/fake/root', 'deadbeef')).toBe('polaris@unresolved');
  });

  it('the real tree resolves to the surface tree at HEAD, and the record grammar accepts it', () => {
    const head = execFileSync('git', ['-C', REPO_ROOT, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
    const tree = execFileSync('git', ['-C', REPO_ROOT, 'rev-parse', `${head}:apps/three-surface-poc/src`], { encoding: 'utf8' }).trim();
    const runGit = (root: string, args: readonly string[]): string => execFileSync('git', ['-C', root, ...args], { encoding: 'utf8' });
    const version = pwbSurfaceVersion(runGit, REPO_ROOT, head);
    expect(version).toBe(`polaris@${tree.slice(0, 12)}`);
    expect(version).toMatch(/^[a-z][a-z0-9-]*@[0-9A-Za-z][0-9A-Za-z.+-]*$/);
  });
});

describe('walkthroughJudgmentInputsFor', () => {
  it('binds the loaded pair to the builder-supplied evaluation identity and the tree-derived surface version', () => {
    const tree = fakeTree();
    const root = '/fake/root';
    const relative = (absolute: string): string => absolute.slice(`${root}/`.length);
    const loader = walkthroughJudgmentInputsFor({
      repoRoot: root,
      evaluationId: 'eval-hermetic',
      evaluationInstant: EVALUATION_INSTANT,
      governanceRevision: 'b'.repeat(40),
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
        if (args[0] === 'rev-parse' && args[1] === `${'b'.repeat(40)}:apps/three-surface-poc/src`) return `${SURFACE_TREE_ID}\n`;
        if (args[0] === 'rev-parse') return `${'4'.repeat(40)}\n`;
        if (args[0] === 'ls-tree') return tree.treePaths.has(args[4] ?? '') ? `${args[4]}\n` : '';
        throw new Error(`unexpected git ${args.join(' ')}`);
      },
      readGitBlob: (_root, object) => {
        const path = object.split(':').slice(1).join(':');
        const text = tree.files.get(path);
        if (text === undefined) throw new Error('missing');
        return new TextEncoder().encode(text);
      },
    });
    const inputs = loader({ evaluationIdentity: BINDING.evaluationIdentity });
    expect(inputs.expectations.surfaceVersion).toBe(BINDING.surfaceVersion);
    expect(inputs.expectations.evaluationIdentity).toBe(BINDING.evaluationIdentity);
    expect(evaluateWalkthroughJudgment(inputs).outcome.kind).toBe('lawful');
    // Another evaluation identity: the same record no longer binds.
    const other = loader({ evaluationIdentity: 'pwb-eval-ffffffffffffffffffffffff' });
    expect(evaluateWalkthroughJudgment(other).outcome.kind).toBe('unlawful');
  });
});

describe('pwbReadinessTraversal', () => {
  const traversal = pwbReadinessTraversal();
  const population = ['openspec/specs/alpha/spec.md', 'heart-and-soul/README.md'];

  it('names the Polaris page routes and admits the exact-source route in every spelling of the same evaluation', () => {
    expect([...traversal.polarisRoutes]).toEqual(['/polaris', '/butlers-syzygy/polaris']);
    expect(traversal.isExactSourceRoute('/polaris#polaris-source-openspec-specs-alpha-spec-md', population)).toBe(true);
    expect(traversal.isExactSourceRoute('/butlers-syzygy/polaris#polaris-source-openspec-specs-alpha-spec-md', population)).toBe(true);
    expect(traversal.isExactSourceRoute('/polaris/source', population)).toBe(true);
    expect(traversal.isExactSourceRoute('/butlers-syzygy/polaris/source', population)).toBe(true);
    expect(traversal.isExactSourceRoute('/polaris/source?identity=source:openspec/specs/alpha/spec.md%23abc', population)).toBe(true);
    expect(traversal.isExactSourceRoute('/polaris/source?identity=source:openspec/specs/alpha/spec.md', population)).toBe(true);
  });

  it('rejects other surfaces, other evaluations\' sources and malformed identities', () => {
    expect(traversal.isExactSourceRoute('/trajectory', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris#polaris-source-lay-and-land-readme-md', population)).toBe(false);
    // A Polaris fragment on another surface is not a Polaris route.
    expect(traversal.isExactSourceRoute('/trajectory#polaris-source-openspec-specs-alpha-spec-md', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/#polaris-source-openspec-specs-alpha-spec-md', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris/source?identity=source:lay-and-land/README.md', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris/source?other=1', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris/source?identity=', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris/source#x', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris/sources', population)).toBe(false);
    expect(traversal.isExactSourceRoute('/polaris?identity=source:openspec/specs/alpha/spec.md', population)).toBe(false);
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
      binding: BINDING,
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
