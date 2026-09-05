// Parser classification: present / missing / malformed per field, and the
// parser's promise to hold no notion of validity (a wrong value is present).

import { describe, expect, it } from 'vitest';

import { parseOwnerActRecord, supersessionTargetsOf } from './owner-act-record.js';

const DIGEST = 'a'.repeat(64);

const RECORD = `# Owner act — example

Date: 2026-09-02

Owner: Tzeusy

Act identity: \`PWB-EXAMPLE-ACT-2026-09-02\`

Act type: \`consent-observation\`

Project identity: \`project:syzygy\`

Artifact identity: \`.syzygy/governance/decisions/EXAMPLE.md\`

Exact digest (SHA-256): \`${DIGEST}\`

Provenance state: \`owner-adopted (bootstrap, uncorrelated)\` — state (1),
explicitly selected by performing the offered state-(1) phrase

Supersession / revocation: none — this act supersedes no earlier act and is
revoked only by a later exact owner act naming it

A1 audit-record identity (RFC3-16(b) item 9): **explicitly absent**

## Ceremony

The owner performed this one act by writing exactly:

\`\`\`text
CONSENT TO EXAMPLE: ${DIGEST}
\`\`\`

Frozen provenance:

- reviewed subject: \`48e0f5db645d1fb08e5e3a65c5e50dbcece40412\`;
- recording tag: \`pwb-example-signed-2026-09-02\`, on the commit carrying this act record.

## Effect

The scope of this act is the pair (\`project:syzygy\`, \`repository:example\`).

## What this act does not authorize

Nothing else.
`;

describe('parseOwnerActRecord', () => {
  it('extracts every labelled field of a well-formed record as present', () => {
    const parsed = parseOwnerActRecord(RECORD);
    expect(parsed.actInstant).toEqual({ kind: 'present', value: '2026-09-02' });
    expect(parsed.owner).toEqual({ kind: 'present', value: 'Tzeusy' });
    expect(parsed.actIdentity).toEqual({ kind: 'present', value: 'PWB-EXAMPLE-ACT-2026-09-02' });
    expect(parsed.actType).toEqual({ kind: 'present', value: 'consent-observation' });
    expect(parsed.projectIdentity).toEqual({ kind: 'present', value: 'project:syzygy' });
    expect(parsed.artifactIdentity).toEqual({ kind: 'present', value: '.syzygy/governance/decisions/EXAMPLE.md' });
    expect(parsed.exactDigest).toEqual({ kind: 'present', value: DIGEST });
    expect(parsed.provenanceState).toEqual({
      kind: 'present',
      value: { label: 'owner-adopted (bootstrap, uncorrelated)', explicitSelection: true },
    });
    expect(parsed.supersession).toEqual({ kind: 'present', value: { relation: 'none' } });
    expect(parsed.a1).toEqual({ kind: 'present', value: { absent: true } });
    expect(parsed.expires).toEqual({ kind: 'missing' });
    expect(parsed.ceremonyPhrase).toEqual({ kind: 'present', value: `CONSENT TO EXAMPLE: ${DIGEST}` });
    expect(parsed.recordingTag).toEqual({ kind: 'present', value: 'pwb-example-signed-2026-09-02' });
    expect(parsed.scope.kind).toBe('present');
    expect(parsed.scope.kind === 'present' && parsed.scope.value).toContain('repository:example');
    expect(parsed.scope.kind === 'present' && parsed.scope.value).not.toContain('Nothing else');
  });

  it('reports an absent label as missing, never as malformed or present', () => {
    const parsed = parseOwnerActRecord(RECORD.replace(/^Act type: .*\n\n/m, ''));
    expect(parsed.actType).toEqual({ kind: 'missing' });
  });

  it('reports a label whose value does not fit its syntactic form as malformed, keeping the raw text', () => {
    const parsed = parseOwnerActRecord(
      RECORD.replace('Act type: `consent-observation`', 'Act type: consent observation (unquoted)'),
    );
    expect(parsed.actType).toEqual({ kind: 'malformed', raw: 'consent observation (unquoted)' });
  });

  it('reports a wrong-but-well-formed value as present (validity is not the parser’s concern)', () => {
    const parsed = parseOwnerActRecord(RECORD.replace('`project:syzygy`\n\nArtifact', '`project:other`\n\nArtifact'));
    expect(parsed.projectIdentity).toEqual({ kind: 'present', value: 'project:other' });
  });

  it('distinguishes a state-(1) label without explicit selection from one with it', () => {
    const parsed = parseOwnerActRecord(
      RECORD.replace(' — state (1),\nexplicitly selected by performing the offered state-(1) phrase', ' — state (1)'),
    );
    expect(parsed.provenanceState).toEqual({
      kind: 'present',
      value: { label: 'owner-adopted (bootstrap, uncorrelated)', explicitSelection: false },
    });
  });

  it('parses a present A1 identity, a supersession target and an expiry', () => {
    const text = RECORD.replace('**explicitly absent**', '`a1:record-1`')
      .replace('none — this act supersedes no earlier act and is\nrevoked only by a later exact owner act naming it', 'supersedes `PWB-OLD-ACT-2026-08-01`')
      .replace('Owner: Tzeusy\n', 'Owner: Tzeusy\n\nExpires: 2026-12-31\n');
    const parsed = parseOwnerActRecord(text);
    expect(parsed.a1).toEqual({ kind: 'present', value: { absent: false, identity: 'a1:record-1' } });
    expect(parsed.supersession).toEqual({
      kind: 'present',
      value: { relation: 'supersedes', target: 'PWB-OLD-ACT-2026-08-01' },
    });
    expect(parsed.expires).toEqual({ kind: 'present', value: '2026-12-31' });
    expect(supersessionTargetsOf(text)).toEqual([{ relation: 'supersedes', target: 'PWB-OLD-ACT-2026-08-01' }]);
    expect(supersessionTargetsOf(RECORD)).toEqual([]);
  });

  it('parses the role-scoped amendment supersession form and reports its target as the record path', () => {
    const text = RECORD.replace(
      'none — this act supersedes no earlier act and is\nrevoked only by a later exact owner act naming it',
      'this act supersedes, for the `approve-policy` role\nonly, the 2026-09-02 act recorded at `.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`. That\nrecord, its digest, its tag and the bytes it bound remain immutable history.',
    );
    const parsed = parseOwnerActRecord(text);
    expect(parsed.supersession).toEqual({
      kind: 'present',
      value: { relation: 'supersedes', target: '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md', role: 'approve-policy' },
    });
    expect(supersessionTargetsOf(text)).toEqual([{ relation: 'supersedes', target: '.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md' }]);
    for (const malformed of [
      'this act supersedes the 2026-09-02 act recorded at `.syzygy/governance/decisions/X.md`.',
      'this act supersedes, for the `approve-policy` role only, the 2026-09-02 act recorded at X.',
      'this act supersedes, for the `approve-policy` role only, the earlier act recorded at `X.md`.',
    ]) {
      const broken = RECORD.replace('none — this act supersedes no earlier act and is\nrevoked only by a later exact owner act naming it', malformed);
      expect(parseOwnerActRecord(broken).supersession.kind, malformed).toBe('malformed');
    }
  });

  it('reports a missing or multi-line ceremony phrase and a missing Effect section', () => {
    const noPhrase = parseOwnerActRecord(RECORD.replace(/```text\n[^\n]*\n```\n/, ''));
    expect(noPhrase.ceremonyPhrase).toEqual({ kind: 'missing' });
    const twoLines = parseOwnerActRecord(RECORD.replace(`CONSENT TO EXAMPLE: ${DIGEST}`, 'line one\nline two'));
    expect(twoLines.ceremonyPhrase.kind).toBe('malformed');
    const noEffect = parseOwnerActRecord(RECORD.replace(/## Effect\n[\s\S]*?(?=## What)/, ''));
    expect(noEffect.scope).toEqual({ kind: 'missing' });
    const emptyEffect = parseOwnerActRecord(RECORD.replace(/## Effect\n[\s\S]*?(?=## What)/, '## Effect\n\n'));
    expect(emptyEffect.scope.kind).toBe('malformed');
  });

  it('returns every field missing for unrelated text', () => {
    const parsed = parseOwnerActRecord('# Not an act\n\nJust prose.\n');
    for (const field of Object.values(parsed)) expect(field.kind).toBe('missing');
  });
});
