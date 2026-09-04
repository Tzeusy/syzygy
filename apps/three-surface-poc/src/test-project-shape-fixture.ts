import { createHash } from 'node:crypto';

import type { BodyReadAuthorityEvaluation, GitRunner } from '@syzygy/three-surface-poc-core';

/**
 * An in-memory Butlers-shaped tree for surface tests that need the shared
 * model's `projectShape` to be `observed`. The texts follow the P2.5
 * grammar exactly (heading text, column-0 anchors, one declaration per
 * identity); `SECRET_SENTINEL` marks a body that the secret policy must
 * exclude so a rendering test can prove hash-not-body.
 */
export const PROJECT_SHAPE_FIXTURE_COMMIT = '4'.repeat(40);
export const PROJECT_SHAPE_FIXTURE_COMMITTED_AT = '2026-08-15T10:00:00+00:00';
export const SECRET_SENTINEL = 'EXCLUDED-BODY-SENTINEL-7f3a';

const VISION = [
  '# Fixture',
  '',
  '## What Butlers Is',
  '',
  'A household of agents that keep promises.',
  '',
  '## What Success Looks Like',
  '',
  '- Every promise is visible.',
  '- Nothing is inferred silently.',
  '',
  '## What Butlers Is Not',
  '',
  'Not a chat toy.',
  '',
  '## Non-Negotiable Rules',
  '',
  '1. **Fail closed** — silence is Unknown.',
  '2. **Cite or stay quiet** — every claim carries a source.',
  '',
].join('\n');

const ARCHITECTURE = ['# Architecture', '', '## Runtime', '', 'One process.', ''].join('\n');

const V1 = [
  '# v1',
  '',
  '## What v1 Ships',
  '',
  'Ships text.',
  '',
  '### Core Infrastructure',
  '',
  '- **Bus** - the message bus',
  '',
  '### Staffers',
  '',
  '### Butlers',
  '',
  '- **Atlas** - maps',
  '- **Bishop** - moves',
  '',
  '### Modules',
  '',
  '### Connectors',
  '',
  '### Dashboard',
  '',
  '### Identity System',
  '',
  '### Situational Awareness',
  '',
  '### Observability',
  '',
  '## What v1 Defers',
  '',
  'Defers text.',
  '',
  '## Success Criteria',
  '',
  '1. Ships on time.',
  '',
].join('\n');

const CRAFT_README = ['# Craft', '', '### Reading Order', '', '| Order | File |', '|---|---|', '| 1 | [Spec policy](policies/cc-spec.md) |', ''].join('\n');

export const PROJECT_SHAPE_FIXTURE_TEXTS: Readonly<Record<string, string>> = {
  'about/README.md': [
    '# Fixture',
    '',
    '[Heart and Soul](heart-and-soul/) · [Legends and Lore](legends-and-lore/) ·',
    '[Spec and Spine](spec-and-spine/) · [Lay and Land](lay-and-land/) · [Craft and Care](craft-and-care/)',
    '',
  ].join('\n'),
  'about/heart-and-soul/README.md': '- [Vision](vision.md)\n- [Architecture](architecture.md)\n- [v1](v1.md)\n',
  'about/heart-and-soul/vision.md': VISION,
  'about/heart-and-soul/architecture.md': ARCHITECTURE,
  'about/heart-and-soul/v1.md': V1,
  'about/legends-and-lore/README.md': ['# Lore', '', '## Index', '', '| Contract | Status |', '| --- | --- |', '| [RFC 0001](0001.md) | accepted |', ''].join('\n'),
  'about/legends-and-lore/0001.md': '# RFC 0001\n',
  'about/spec-and-spine/README.md': 'Specs.\n',
  'about/lay-and-land/README.md': '[Components](components.md)\n',
  'about/lay-and-land/components.md': ['# Components', '', '## 1 Runtime', '', '| Component | Role |', '|---|---|', '| **Daemon** | serves |', ''].join('\n'),
  'about/craft-and-care/README.md': CRAFT_README,
  'about/craft-and-care/policies/cc-spec.md': '# Spec policy\n',
  'openspec/specs/alpha/spec.md': '# Alpha\n',
  'roster/atlas/butler.toml': '[butler]\nname = "atlas"\n',
  'roster/bishop/butler.toml': '[butler]\nname = "bishop"\n',
};

/** The same tree with the craft index carrying a secret-shaped token: the
 * policy excludes that body, so its craft-policy items are Unknown. */
/** The same tree plus the baseline spec the followed OpenSpec change amends,
 * so `proposedWork.currentAuthority` resolves to an Observed shape item. */
export const PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH = 'openspec/specs/switchboard-identity/spec.md';
export const PROJECT_SHAPE_FIXTURE_TEXTS_WITH_BASELINE_SPEC: Readonly<Record<string, string>> = {
  ...PROJECT_SHAPE_FIXTURE_TEXTS,
  [PROJECT_SHAPE_FIXTURE_BASELINE_SPEC_PATH]: '# Switchboard identity\n',
};

export const PROJECT_SHAPE_FIXTURE_TEXTS_WITH_SECRET: Readonly<Record<string, string>> = {
  ...PROJECT_SHAPE_FIXTURE_TEXTS,
  'about/craft-and-care/README.md': `${CRAFT_README}\ntoken AKIA${'A'.repeat(16)} ${SECRET_SENTINEL}\n`,
};

const encoder = new TextEncoder();

function sha1Blob(bytes: Uint8Array): string {
  return createHash('sha1').update(`blob ${bytes.byteLength}\0`).update(bytes).digest('hex');
}

/** A byte-level Git runner over the fixture texts: resolves every revision
 * to the fixture commit, lists the tree only at that commit and serves
 * blobs by object id. Anything else throws. */
export function projectShapeFixtureGit(texts: Readonly<Record<string, string>> = PROJECT_SHAPE_FIXTURE_TEXTS): GitRunner {
  const entries = Object.entries(texts).map(([path, text]) => {
    const body = encoder.encode(text);
    return { path, body, objectId: sha1Blob(body) };
  });
  const byOid = new Map(entries.map((entry) => [entry.objectId, entry.body]));
  const listing = entries.map((e) => `100644 blob ${e.objectId} ${String(e.body.byteLength).padStart(7)}\t${e.path}\x00`).join('');
  return (args: readonly string[]): Uint8Array => {
    switch (args[0]) {
      case 'rev-parse':
        return encoder.encode(`${PROJECT_SHAPE_FIXTURE_COMMIT}\n`);
      case 'show':
        return encoder.encode(`${PROJECT_SHAPE_FIXTURE_COMMITTED_AT}\n`);
      case 'ls-tree':
        if (args[4] !== PROJECT_SHAPE_FIXTURE_COMMIT) throw new Error(`fixture lists trees only at the resolved commit, not ${args[4] ?? ''}`);
        return encoder.encode(listing);
      case 'cat-file': {
        const body = byOid.get(args[2] ?? '');
        if (body === undefined) throw new Error(`fixture has no object ${args[2] ?? ''}`);
        return body;
      }
      default:
        throw new Error(`unexpected git command ${args.join(' ')}`);
    }
  };
}

/** A valid state-(1) evaluation of all three effect acts, for tests only. */
export const ADMITTING_AUTHORITY: BodyReadAuthorityEvaluation = {
  evaluationId: 'evaluation:test-admitting',
  evaluationInstant: '2026-09-04T00:00:00Z',
  admits: true,
  authorizationMode: 'owner-trusted-bootstrap',
  consent: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:consent', artifactDigest: 'sha256:c'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  policy: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:policy', artifactDigest: 'sha256:p'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  registry: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:registry', artifactDigest: 'sha256:r'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  contradiction: undefined,
};

/** An evaluation whose consent act is absent: the gate refuses. */
export const REJECTING_AUTHORITY: BodyReadAuthorityEvaluation = {
  evaluationId: 'evaluation:test-rejecting',
  evaluationInstant: '2026-09-04T00:00:00Z',
  admits: false,
  authorizationMode: 'rejected',
  consent: { kind: 'absent', what: 'artifact-missing', artifactDigest: undefined },
  policy: { kind: 'valid', provenance: 'state-1', actIdentity: 'act:policy', artifactDigest: 'sha256:p'.padEnd(71, '0'), actInstant: '2026-09-02T00:00:00Z' },
  registry: { kind: 'invalid', caseId: 'registry:phrase-mismatched', detail: 'wrong phrase', artifactDigest: 'sha256:r'.padEnd(71, '0'), claimedProvenance: 'state-1' },
  contradiction: { clause: 'RFC3-16(a)', definedTerm: 'authorization-bearing governance artifact', statement: 'No effective act.', failing: [] },
};
