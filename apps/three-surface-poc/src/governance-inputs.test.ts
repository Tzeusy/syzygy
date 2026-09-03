// Governance-inputs loader: hermetic classification of what the tree
// holds, and the real-tree evaluation of the three 2026-09-02 PWB acts.
//
// The real-tree test reads only Syzygy's own governance tree. It never
// touches a Butlers repository, and the reader it hands the observer is a
// counter, so no body is read whatever the outcome.

import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

import {
  discloseAuthority,
  evaluateBodyReadAuthority,
  observeProjectShape,
} from '@syzygy/three-surface-poc-core';

import {
  PWB_ACT_RECORDS,
  PWB_AUTHORITY_ARTIFACTS,
  loadBodyReadAuthorityInputs,
  pwbAuthorityExpectations,
} from './governance-inputs.js';

const REPO_ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const EVALUATION_INSTANT = '2026-09-03T00:00:00Z';

function sha256(bytes: Uint8Array): string {
  return createHash('sha256').update(bytes).digest('hex');
}

interface FakeTree {
  readonly files: Map<string, string>;
  readonly tags: Map<string, string>;
  readonly treePaths: Set<string>;
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
  return { files, tags, treePaths: new Set(Object.values(PWB_ACT_RECORDS)) };
}

function loaderFor(tree: FakeTree) {
  const root = '/fake/root';
  const relative = (absolute: string): string => absolute.slice(`${root}/`.length);
  return loadBodyReadAuthorityInputs({
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
      throw new Error(`unexpected git ${args.join(' ')}`);
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
    expect(inputs.policy.actRecord).toEqual({ kind: 'git-ref-only', ref: 'pwb-approve-policy-signed-2026-09-02' });
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
    tree.tags.delete('pwb-adopt-registry-entry-signed-2026-09-02');
    const inputs = loaderFor(tree);
    expect(inputs.registry.artifact).toEqual({ kind: 'missing' });
    expect(inputs.registry.actRecord).toEqual({ kind: 'absent' });
  });

  it('leaves a tag unresolved when its commit does not carry the act record', () => {
    const tree = fakeTree();
    tree.treePaths.delete(PWB_ACT_RECORDS.consent);
    const inputs = loaderFor(tree);
    expect(inputs.consent.recordingTag).toEqual({ kind: 'unresolved' });
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.consent.kind === 'invalid' && evaluation.consent.caseId).toBe('consent:recording-tag-mismatched');
  });

  it('detects a later decision record that revokes or supersedes an act identity', () => {
    const tree = fakeTree();
    tree.files.set(
      '.syzygy/governance/decisions/PWB-LATER-REVOCATION-ACT.md',
      '# Later act\n\nAct identity: `PWB-LATER-2026-09-10`\n\nSupersession / revocation: revokes `PWB-BUTLERS-OBSERVATION-CONSENT-2026-09-02`\n',
    );
    tree.files.set(
      '.syzygy/governance/decisions/PWB-LATER-SUPERSESSION-ACT.md',
      '# Later act\n\nAct identity: `PWB-LATER-2026-09-11`\n\nSupersession / revocation: supersedes `PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-2026-09-02`\n',
    );
    const inputs = loaderFor(tree);
    expect(inputs.consent.lifecycle).toEqual({ revokedBy: '.syzygy/governance/decisions/PWB-LATER-REVOCATION-ACT.md' });
    expect(inputs.registry.lifecycle).toEqual({ supersededBy: '.syzygy/governance/decisions/PWB-LATER-SUPERSESSION-ACT.md' });
    expect(inputs.policy.lifecycle).toEqual({});
    const evaluation = evaluateBodyReadAuthority(inputs);
    expect(evaluation.consent.kind === 'invalid' && evaluation.consent.caseId).toBe('consent:revoked');
    expect(evaluation.registry.kind === 'invalid' && evaluation.registry.caseId).toBe('registry:superseded');
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
    const out = execFileSync('git', ['-C', REPO_ROOT, 'tag', '--list', 'pwb-*-signed-2026-09-02'], { encoding: 'utf8' });
    const present = new Set(out.split('\n').map((line) => line.trim()));
    const expected = pwbAuthorityExpectations(EVALUATION_INSTANT).authorities;
    return (['consent', 'policy', 'registry'] as const).every((kind) => present.has(expected[kind].recordingTag));
  } catch {
    return false;
  }
}

describe('loadBodyReadAuthorityInputs (real Syzygy governance tree)', () => {
  it('evaluates the three real 2026-09-02 PWB acts without reading any body', () => {
    const inputs = loadBodyReadAuthorityInputs({
      repoRoot: REPO_ROOT,
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
