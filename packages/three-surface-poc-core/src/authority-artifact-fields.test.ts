import { describe, expect, it } from 'vitest';

import { parseConsentArtifact, parsePolicyArtifact, parseRegistryArtifact } from './authority-artifact-fields.js';

// The decoding step of the three PWB-REQ-005 artifact parsers (syzygy-bpyt.6.3): bytes that are not well-formed UTF-8
// are undecodable, never replaced and parsed. Expected values are typed here, not read back from the parsers.
const enc = new TextEncoder();
const BOM = [0xef, 0xbb, 0xbf];
const withBytes = (text: string, ...extra: number[]): Uint8Array => Uint8Array.from([...enc.encode(text), ...extra]);
const withBom = (text: string): Uint8Array => Uint8Array.from([...BOM, ...enc.encode(text)]);

const CONSENT = 'Subject: `(project:syzygy, repository:butlers)`\nObservation content class: `declared-project-shape-text`\n';
const POLICY = '{"policyOwningProject":"project:syzygy","policyVersion":"4"}';
const NOT_UTF8: ReadonlyArray<readonly [string, number[]]> = [
  ['a lone continuation byte', [0x80]],
  ['a truncated sequence', [0xe2, 0x82]],
  ['an overlong encoding', [0xc0, 0x80]],
  ['an encoded surrogate', [0xed, 0xa0, 0x80]],
];

describe('parseConsentArtifact decoding', () => {
  it('reads well-formed text, with or without a leading byte-order mark (the parser trims every line, so the mark cannot change the result)', () => {
    const parsed = { kind: 'parsed', fields: {
      observingProject: { kind: 'present', value: 'project:syzygy' },
      configuredRepository: { kind: 'present', value: 'repository:butlers' },
      contentClass: { kind: 'present', value: 'declared-project-shape-text' },
    } };
    expect(parseConsentArtifact(enc.encode(CONSENT))).toEqual(parsed);
    expect(parseConsentArtifact(withBom(CONSENT))).toEqual(parsed);
  });

  it('refuses bytes that are not UTF-8 instead of parsing a replaced text', () => {
    for (const [label, bad] of NOT_UTF8) {
      expect(parseConsentArtifact(withBytes(CONSENT, ...bad)), label).toEqual({ kind: 'undecodable', detail: 'not strict UTF-8' });
    }
  });
});

describe('parsePolicyArtifact and parseRegistryArtifact decoding', () => {
  it('parse well-formed JSON, with or without a leading byte-order mark', () => {
    const policy = { kind: 'parsed', fields: { policyOwningProject: { kind: 'present', value: 'project:syzygy' }, policyVersion: { kind: 'present', value: '4' } } };
    expect(parsePolicyArtifact(enc.encode(POLICY))).toEqual(policy);
    expect(parsePolicyArtifact(withBom(POLICY))).toEqual(policy);
    const registry = parseRegistryArtifact(withBom('{"governanceHome":"h","project":"project:syzygy"}'));
    expect(registry).toMatchObject({ kind: 'parsed', fields: { governanceHome: { kind: 'present', value: 'h' }, project: { kind: 'present', value: 'project:syzygy' } } });
  });

  it('refuse bytes that are not UTF-8, naming the decoding and not the JSON', () => {
    for (const [label, bad] of NOT_UTF8) {
      expect(parsePolicyArtifact(withBytes(POLICY, ...bad)), `policy, ${label}`).toEqual({ kind: 'undecodable', detail: 'not strict UTF-8' });
      expect(parseRegistryArtifact(withBytes('{}', ...bad)), `registry, ${label}`).toEqual({ kind: 'undecodable', detail: 'not strict UTF-8' });
    }
  });

  it('tell valid UTF-8 that is not JSON from bytes that are not UTF-8', () => {
    expect(parsePolicyArtifact(enc.encode('not json'))).toEqual({ kind: 'undecodable', detail: 'not JSON' });
    expect(parseRegistryArtifact(enc.encode('['))).toEqual({ kind: 'undecodable', detail: 'not JSON' });
  });
});
