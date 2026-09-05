// Governance-inputs loader: hermetic classification of what the tree
// holds, and the real-tree evaluation of the three current PWB acts (the
// 2026-09-02 consent act and the 2026-09-05 policy and registry amendments).
//
// The real-tree test reads only Syzygy's own governance tree. It never
// touches a Butlers repository, and the reader it hands the observer is a
// counter, so no body is read whatever the outcome.

import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, describe, expect, it } from 'vitest';

import {
  discloseAuthority,
  evaluateBodyReadAuthority,
  observeProjectShape,
} from '@syzygy/three-surface-poc-core';

import {
  PWB_ACT_RECORDS,
  PWB_AUTHORITY_ARTIFACTS,
  PWB_SUPERSEDED_ACT_RECORDS,
  loadBodyReadAuthorityInputs,
  pwbAuthorityExpectations,
} from './governance-inputs.js';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const EVALUATION_INSTANT = '2026-09-06T00:00:00Z';
const CURRENT_COMMIT = 'f'.repeat(40);
const cleanups: string[] = [];

afterEach(() => {
  for (const root of cleanups.splice(0)) rmSync(root, { recursive: true, force: true });
});

function git(root: string, args: readonly string[]): string {
  return execFileSync('git', ['-C', root, ...args], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
}

function realGovernanceFixture(): string {
  const root = mkdtempSync(join(tmpdir(), 'syzygy-pwb-governance-'));
  cleanups.push(root);
  git(root, ['init', '-q']);
  git(root, ['config', 'user.email', 'pwb-test@example.invalid']);
  git(root, ['config', 'user.name', 'PWB Test']);
  for (const path of [...Object.values(PWB_AUTHORITY_ARTIFACTS), ...Object.values(PWB_ACT_RECORDS)]) {
    const target = join(root, path);
    mkdirSync(dirname(target), { recursive: true });
    writeFileSync(target, readFileSync(join(REPO_ROOT, path)));
  }
  git(root, ['add', '.']);
  git(root, ['commit', '-qm', 'governance fixture']);
  git(root, ['tag', 'pwb-consent-observation-signed-2026-09-02']);
  return root;
}

function sha256(bytes: Uint8Array): string {
  return createHash('sha256').update(bytes).digest('hex');
}

interface FakeTree {
  readonly files: Map<string, string>;
  readonly tags: Map<string, string>;
  readonly treePaths: Set<string>;
  readonly taggedRecords: Map<string, string>;
  failLifecycleList?: boolean;
  readonly unreadablePaths: Set<string>;
  readonly invalidUtf8Paths: Set<string>;
}

function fakeTree(): FakeTree {
  const files = new Map<string, string>();
  for (const kind of ['consent', 'policy', 'registry'] as const) {
    files.set(PWB_AUTHORITY_ARTIFACTS[kind], readFileSync(join(REPO_ROOT, PWB_AUTHORITY_ARTIFACTS[kind]), 'utf8'));
    files.set(PWB_ACT_RECORDS[kind], readFileSync(join(REPO_ROOT, PWB_ACT_RECORDS[kind]), 'utf8'));
  }
  const expectations = pwbAuthorityExpectations(EVALUATION_INSTANT);
  const tags = new Map<string, string>([
    [expectations.authorities.consent.recordingTag, '1'.repeat(40)],
    [expectations.authorities.policy.recordingTag, '2'.repeat(40)],
    [expectations.authorities.registry.recordingTag, '3'.repeat(40)],
  ]);
  const taggedRecords = new Map<string, string>();
  for (const kind of ['consent', 'policy', 'registry'] as const) {
    taggedRecords.set(`${tags.get(expectations.authorities[kind].recordingTag)}:${PWB_ACT_RECORDS[kind]}`, files.get(PWB_ACT_RECORDS[kind]) ?? '');
  }
  return { files, tags, treePaths: new Set(Object.values(PWB_ACT_RECORDS)), taggedRecords, unreadablePaths: new Set(), invalidUtf8Paths: new Set() };
}

function loaderFor(tree: FakeTree, fromGitTree = false) {
  const root = '/fake/root';
  const relative = (absolute: string): string => absolute.slice(`${root}/`.length);
  const bytesAt = (path: string): Uint8Array => {
    if (tree.unreadablePaths.has(path)) throw Object.assign(new Error('EACCES'), { code: 'EACCES' });
    if (tree.invalidUtf8Paths.has(path)) return new Uint8Array([0xff]);
    const text = tree.files.get(path);
    if (text === undefined) throw Object.assign(new Error('ENOENT'), { code: 'ENOENT' });
    return new TextEncoder().encode(text);
  };
  return loadBodyReadAuthorityInputs({
    repoRoot: root,
    evaluationId: 'eval-hermetic',
    evaluationInstant: EVALUATION_INSTANT,
    ...(fromGitTree ? { governanceRevision: 'HEAD' } : {
      readFile: (absolute: string) => bytesAt(relative(absolute)),
      listDirectory: (absolute: string) => {
        if (tree.failLifecycleList) throw new Error('list failed');
        const prefix = `${relative(absolute)}/`;
        return [...tree.files.keys()].filter((path) => path.startsWith(prefix)).map((path) => path.slice(prefix.length));
      },
    }),
    runGit: (_root, args) => {
      if (args[0] === 'rev-parse') {
        if (args[2] === 'HEAD^{commit}') return `${CURRENT_COMMIT}\n`;
        const tag = /^refs\/tags\/(.+)\^\{commit\}$/.exec(args[3] ?? '')?.[1] ?? '';
        const commit = tree.tags.get(tag);
        if (commit === undefined) throw new Error('unknown tag');
        return `${commit}\n`;
      }
      if (args[0] === 'ls-tree') {
        if (args.includes('-r')) return `${[...tree.files.keys()].join('\0')}\0`;
        const path = args[4] ?? '';
        return tree.treePaths.has(path) ? `${path}\n` : '';
      }
      throw new Error(`unexpected git ${args.join(' ')}`);
    },
    readGitBlob: (_root, object) => {
      const [commit, ...pathParts] = object.split(':');
      const path = pathParts.join(':');
      if (commit === CURRENT_COMMIT) return bytesAt(path);
      const text = tree.taggedRecords.get(object);
      if (text === undefined) throw new Error('missing tagged record');
      return new TextEncoder().encode(text);
    },
  });
}

describe('loadBodyReadAuthorityInputs (hermetic)', () => {
  it('loads the three artifacts and act records and resolves every recording tag', () => {
    const inputs = loaderFor(fakeTree());
    for (const kind of ['consent', 'policy', 'registry'] as const) {
      expect(inputs[kind].artifact.kind).toBe('present');
      expect(inputs[kind].actRecord.kind).toBe('owner-act-record');
      expect(inputs[kind].lifecycle).toEqual({});
      expect(inputs[kind].recordingTag.kind).toBe('resolved');
    }
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.admits).toBe(true);
    expect(evaluation.authorizationMode).toBe('owner-trusted-bootstrap');
  });

  it('classifies a missing act record with an existing tag as git-ref-only', () => {
    const tree = fakeTree();
    tree.files.delete(PWB_ACT_RECORDS.policy);
    const inputs = loaderFor(tree);
    expect(inputs.policy.actRecord).toEqual({ kind: 'git-ref-only', ref: 'pwb-approve-policy-signed-2026-09-05' });
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.policy.kind === 'invalid' && evaluation.policy.caseId).toBe('policy:git-ref-only');
  });

  it('classifies a missing act record with no tag but a stamped artifact as tree-attribution-only', () => {
    const tree = fakeTree();
    tree.files.delete(PWB_ACT_RECORDS.consent);
    tree.tags.delete('pwb-consent-observation-signed-2026-09-02');
    const inputs = loaderFor(tree);
    expect(inputs.consent.actRecord.kind).toBe('tree-attribution-only');
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.consent.kind === 'invalid' && evaluation.consent.caseId).toBe('consent:tree-attribution-only');
  });

  it('classifies a missing record, missing tag and missing artifact as absent', () => {
    const tree = fakeTree();
    tree.files.delete(PWB_ACT_RECORDS.registry);
    tree.files.delete(PWB_AUTHORITY_ARTIFACTS.registry);
    tree.tags.delete('pwb-adopt-registry-entry-signed-2026-09-05');
    const inputs = loaderFor(tree);
    expect(inputs.registry.artifact).toEqual({ kind: 'missing' });
    expect(inputs.registry.actRecord).toEqual({ kind: 'absent' });
  });

  it('leaves a tag unresolved when its commit does not carry the act record', () => {
    const tree = fakeTree();
    tree.taggedRecords.delete(`${'1'.repeat(40)}:${PWB_ACT_RECORDS.consent}`);
    const inputs = loaderFor(tree);
    expect(inputs.consent.recordingTag).toEqual({ kind: 'unresolved' });
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.consent.kind === 'invalid' && evaluation.consent.caseId).toBe('consent:recording-tag-mismatched');
  });

  it('rejects a current act record whose bytes drift from the exact recording-tag blob', () => {
    const tree = fakeTree();
    tree.files.set(PWB_ACT_RECORDS.consent, `${tree.files.get(PWB_ACT_RECORDS.consent) ?? ''}\ncoordinated drift`);
    const evaluation = evaluateBodyReadAuthority(loaderFor(tree, true));
    expect(evaluation.consent.kind === 'invalid' && evaluation.consent.caseId).toBe('consent:recording-tag-mismatched');
  });

  it.each(['list', 'read', 'decode'] as const)('fails closed when lifecycle %s fails', (failure) => {
    const tree = fakeTree();
    const other = '.syzygy/governance/decisions/OTHER.md';
    tree.files.set(other, '# Other decision\n');
    if (failure === 'list') tree.failLifecycleList = true;
    if (failure === 'read') tree.unreadablePaths.add(other);
    if (failure === 'decode') tree.invalidUtf8Paths.add(other);
    expect(() => loaderFor(tree)).toThrow();
  });

  it('aborts lifecycle loading on invalid UTF-8 from the exact governance Git tree', () => {
    const tree = fakeTree();
    const other = '.syzygy/governance/decisions/INVALID-UTF8.md';
    tree.files.set(other, '# placeholder');
    tree.invalidUtf8Paths.add(other);
    expect(() => loaderFor(tree, true)).toThrow();
  });

  it('preserves production Git blob bytes for tag comparison and lifecycle decoding', () => {
    const root = realGovernanceFixture();
    const consentRecord = join(root, PWB_ACT_RECORDS.consent);
    writeFileSync(consentRecord, `${readFileSync(consentRecord, 'utf8')}\ncurrent-tree drift\n`);
    git(root, ['add', '.']);
    git(root, ['commit', '-qm', 'drift current record']);

    const load = () => loadBodyReadAuthorityInputs({
      repoRoot: root,
      governanceRevision: git(root, ['rev-parse', 'HEAD']),
      evaluationId: 'eval-production-bytes',
      evaluationInstant: EVALUATION_INSTANT,
    });
    expect(load().consent.recordingTag).toEqual({ kind: 'unresolved' });

    const invalid = join(root, '.syzygy/governance/decisions/INVALID-UTF8.md');
    writeFileSync(invalid, new Uint8Array([0xff]));
    git(root, ['add', '.']);
    git(root, ['commit', '-qm', 'invalid lifecycle bytes']);
    expect(load).toThrow();
  });

  it('detects a later decision record that revokes or supersedes an act identity', () => {
    const tree = fakeTree();
    tree.files.set(
      '.syzygy/governance/decisions/PWB-LATER-REVOCATION-ACT.md',
      '# Later act\n\nAct identity: `PWB-LATER-2026-09-10`\n\nSupersession / revocation: revokes `PWB-BUTLERS-OBSERVATION-CONSENT-2026-09-02`\n',
    );
    tree.files.set(
      '.syzygy/governance/decisions/PWB-LATER-SUPERSESSION-ACT.md',
      '# Later act\n\nAct identity: `PWB-LATER-2026-09-11`\n\nSupersession / revocation: supersedes `PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-AMENDMENT-2026-09-05`\n',
    );
    const inputs = loaderFor(tree);
    expect(inputs.consent.lifecycle).toEqual({ revokedBy: '.syzygy/governance/decisions/PWB-LATER-REVOCATION-ACT.md' });
    expect(inputs.registry.lifecycle).toEqual({ supersededBy: '.syzygy/governance/decisions/PWB-LATER-SUPERSESSION-ACT.md' });
    expect(inputs.policy.lifecycle).toEqual({});
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.consent.kind === 'invalid' && evaluation.consent.caseId).toBe('consent:revoked');
    expect(evaluation.registry.kind === 'invalid' && evaluation.registry.caseId).toBe('registry:superseded');
  });

  it('detects a later amendment-form record that supersedes an act by its record path', () => {
    const tree = fakeTree();
    tree.files.set(
      '.syzygy/governance/decisions/PWB-LATER-POLICY-AMENDMENT-ACT.md',
      `# Later act\n\nAct identity: \`PWB-LATER-2026-09-12\`\n\nSupersession / revocation: this act supersedes, for the \`approve-policy\` role\nonly, the 2026-09-05 act recorded at \`${PWB_ACT_RECORDS.policy}\`. That\nrecord remains immutable history.\n`,
    );
    const inputs = loaderFor(tree);
    expect(inputs.policy.lifecycle).toEqual({ supersededBy: '.syzygy/governance/decisions/PWB-LATER-POLICY-AMENDMENT-ACT.md' });
    expect(inputs.consent.lifecycle).toEqual({});
    expect(inputs.registry.lifecycle).toEqual({});
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.policy.kind === 'invalid' && evaluation.policy.caseId).toBe('policy:superseded');
  });

  it('the current policy and registry acts name their superseded 2026-09-02 records; the superseded records are not the evaluated acts', () => {
    const tree = fakeTree();
    for (const kind of ['policy', 'registry'] as const) {
      const record = tree.files.get(PWB_ACT_RECORDS[kind]) ?? '';
      expect(record).toContain(`act recorded at \`${PWB_SUPERSEDED_ACT_RECORDS[kind]}\``);
      expect(PWB_ACT_RECORDS[kind]).not.toBe(PWB_SUPERSEDED_ACT_RECORDS[kind]);
    }
    // A current record rewritten to claim no supersession is a different act
    // from the one expected and fails closed on exactly that item.
    tree.files.set(
      PWB_ACT_RECORDS.policy,
      (tree.files.get(PWB_ACT_RECORDS.policy) ?? '').replace(/^Supersession \/ revocation:[\s\S]*?\n\n/m, 'Supersession / revocation: none — this act supersedes no earlier act\n\n'),
    );
    const evaluation = evaluateBodyReadAuthority(loaderFor(tree));
    expect(evaluation.policy.kind === 'invalid' && evaluation.policy.caseId).toBe('policy:supersession-target-wrong');
    expect(evaluation.registry.kind).toBe('valid');
  });

  it('an edited artifact breaks its act’s digest binding', () => {
    const tree = fakeTree();
    tree.files.set(PWB_AUTHORITY_ARTIFACTS.policy, `${tree.files.get(PWB_AUTHORITY_ARTIFACTS.policy) ?? ''}\n`);
    const evaluation = evaluateBodyReadAuthority(loaderFor(tree));
    expect(evaluation.policy.kind === 'invalid' && evaluation.policy.caseId).toBe('policy:exact-digest-wrong');
  });
});

function localTagsPresent(): boolean {
  try {
    const out = execFileSync('git', ['-C', REPO_ROOT, 'tag', '--list', 'pwb-*-signed-*'], { encoding: 'utf8' });
    const present = new Set(out.split('\n').map((line) => line.trim()));
    const expected = pwbAuthorityExpectations(EVALUATION_INSTANT).authorities;
    return (['consent', 'policy', 'registry'] as const).every((kind) => present.has(expected[kind].recordingTag));
  } catch {
    return false;
  }
}

describe('loadBodyReadAuthorityInputs (real Syzygy governance tree)', () => {
  it('evaluates the three real current PWB acts without reading any body', () => {
    const governanceRevision = execFileSync('git', ['-C', REPO_ROOT, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
    const inputs = loadBodyReadAuthorityInputs({
      repoRoot: REPO_ROOT,
      governanceRevision,
      evaluationId: 'eval-real-tree',
      evaluationInstant: EVALUATION_INSTANT,
    });
    // Digest binding is recomputed from the real bytes, never transcribed.
    for (const kind of ['consent', 'policy', 'registry'] as const) {
      const artifact = inputs[kind].artifact;
      expect(artifact.kind).toBe('present');
      if (artifact.kind !== 'present') continue;
      const record = inputs[kind].actRecord;
      expect(record.kind).toBe('owner-act-record');
      if (record.kind !== 'owner-act-record') continue;
      expect(record.text).toContain(`Exact digest (SHA-256): \`${sha256(artifact.bytes)}\``);
    }

    const evaluation = evaluateBodyReadAuthority(inputs);
    let reads = 0;
    const observed = observeProjectShape({
      authority: evaluation,
      read: () => {
        reads += 1;
        return 'would-read';
      },
    });
    const disclosure = discloseAuthority(evaluation);

    if (localTagsPresent()) {
      // Full checkout with the three recording tags: every act is a valid
      // state-(1) act; nothing is independently verified.
      expect(evaluation.admits).toBe(true);
      expect(evaluation.authorizationMode).toBe('owner-trusted-bootstrap');
      for (const kind of ['consent', 'policy', 'registry'] as const) {
        expect(evaluation[kind].kind).toBe('valid');
        expect(evaluation[kind].kind === 'valid' && evaluation[kind].provenance).toBe('state-1');
      }
      expect(observed.kind).toBe('admitted');
      expect(reads).toBe(1);
      for (const entry of disclosure.authorities) {
        expect(entry.state).toBe('owner-adopted (bootstrap, uncorrelated)');
        expect(entry.independentlyVerified).toBe(false);
        expect(entry.disclosure).toBe(
          "Owner-trusted only; same-tree forgeable from Syzygy's perspective. Digest detects drift, not authorship or attendance.",
        );
      }
    } else {
      // Shallow/untagged checkout (hosted CI): the recording tags cannot be
      // resolved, so every act fails closed on exactly that case.
      expect(evaluation.admits).toBe(false);
      for (const kind of ['consent', 'policy', 'registry'] as const) {
        expect(evaluation[kind].kind === 'invalid' && evaluation[kind].caseId).toBe(`${kind}:recording-tag-mismatched`);
      }
      expect(observed.kind).toBe('unknown');
      expect(reads).toBe(0);
    }
    expect(disclosure.authorities.every((entry) => entry.independentlyVerified === false)).toBe(true);
  });
});
