import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

import { beforeAll, describe, expect, it } from 'vitest';

import { bodyLines, compileEveryOffsetMatcher, readSecretRedaction, redactBody, retainedWithMarkers, spanTouchesWithheld, type RedactionDetector, type SecretRedaction } from './secret-redaction.js';

const ROOT = fileURLToPath(new URL('../../../', import.meta.url));
const POLICY_PATH = '.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json';

interface BuilderFixtures {
  readonly body: readonly { readonly name: string; readonly body: string; readonly expected: readonly number[] | null; readonly oracle: readonly number[] | null }[];
  readonly whole: readonly { readonly name: string; readonly path: string; readonly body: string; readonly oracle: readonly number[] | null }[];
}

/** The version-4 builder's own body and whole-file fixtures, each with its stated expectation and the builder's reference oracle
 * (`withheld_lines`) run over the policy on disk: the impact ledger requires the builder's fixtures to run through the TypeScript screens,
 * because the oracle runs the patterns in Python `re`. */
function builderFixtures(): BuilderFixtures {
  const py = `import json, sys; sys.path.insert(0, 'scripts'); import build_public_source_screening_scope_v4 as b
policy = open(str(b.ROOT / b.POLICY)).read()
srt = lambda s: None if s is None else sorted(s)
print(json.dumps({'body': [{'name': n, 'body': body, 'expected': srt(w), 'oracle': srt(b.withheld_lines(body, policy))} for n, body, w in b.BODY_FIXTURES],
  'whole': [{'name': n, 'path': p, 'body': body, 'oracle': srt(b.withheld_lines(body, policy, p))} for n, p, body in b.WHOLE_FIXTURES]}))`;
  const run = spawnSync('python3', ['-c', py], { cwd: ROOT, encoding: 'utf8' });
  if (run.status !== 0) throw new Error(`builder fixtures failed: ${run.stderr}`);
  return JSON.parse(run.stdout) as BuilderFixtures;
}

const policyDoc = (): Record<string, unknown> => JSON.parse(readFileSync(`${ROOT}${POLICY_PATH}`, 'utf8')) as Record<string, unknown>;
const scopeOf = (doc: Record<string, unknown>): Record<string, unknown> => doc['publicSourceScope'] as Record<string, unknown>;
const idsOf = (doc: Record<string, unknown>): string[] => (doc['detectors'] as { id: string }[]).map(d => d.id);
const TOKEN = 'tok' + 'en=' + 'abcdefgh12345678';

describe('secretRedaction (policy version 4): the builder fixtures through the TypeScript reading', () => {
  let fixtures: BuilderFixtures;
  let redaction: SecretRedaction;
  let matcher: ReturnType<typeof compileEveryOffsetMatcher>;
  beforeAll(() => {
    fixtures = builderFixtures();
    const doc = policyDoc();
    const read = readSecretRedaction(scopeOf(doc), idsOf(doc));
    if (!read.ok || read.redaction === null) throw new Error('the policy on disk declares no readable secretRedaction');
    redaction = read.redaction;
    matcher = compileEveryOffsetMatcher(doc['detectors'] as RedactionDetector[]);
  });

  it('reads the parameters of the approved bytes', () => {
    expect(redaction.redactedClasses).toEqual(['project-documentation']);
    expect(redaction.wholeArtifactDetectors).toEqual(['private-key-material', 'known-token-formats']);
    expect(redaction.wholeArtifactFragments).toEqual(['-----BEGIN ', '---- BEGIN ', 'LS0tLS1CRUdJT', 'LS0tLSBCRUdJT']);
    expect(redaction.guardLines).toBe(1);
  });

  it('holds sixteen body fixtures and three whole-file fixtures, and the oracle agrees with each stated expectation', () => {
    expect(fixtures.body).toHaveLength(16);
    expect(fixtures.whole).toHaveLength(3);
    for (const fixture of fixtures.body) expect(fixture.oracle, fixture.name).toEqual(fixture.expected);
    for (const fixture of fixtures.whole) expect(fixture.oracle, fixture.name).toBeNull();
  });

  it('withholds exactly the oracle\'s lines for every body fixture, as project documentation', () => {
    for (const fixture of fixtures.body) {
      const got = redactBody(fixture.body, 'project-documentation', matcher, redaction);
      const withheld = got.kind === 'redacted' ? got.withheld : got.kind === 'clean' ? [] : null;
      expect(withheld, fixture.name).toEqual(fixture.expected);
    }
  });

  it('excludes every whole-file fixture whole: code content, an unclassified path and a nested README', () => {
    const classes = { 'src/config.py': 'code-content', 'redis.conf': undefined, 'src/README.md': undefined } as const;
    for (const fixture of fixtures.whole) {
      expect(redactBody(fixture.body, classes[fixture.path as keyof typeof classes], matcher, redaction).kind, fixture.name).toBe('excluded');
    }
  });

  it('keeps every non-withheld line byte for byte and empties each withheld line, keeping its terminator', () => {
    const body = `a\r\nb\r\nc ${TOKEN}\r\nd\r\ne\r\n`;
    const got = redactBody(body, 'project-documentation', matcher, redaction);
    expect(got).toEqual({ kind: 'redacted', withheld: [2, 3, 4], retained: 'a\r\n\r\n\r\n\r\ne\r\n', detectorIds: ['credential-assignment'] });
    expect(bodyLines(got.kind === 'redacted' ? got.retained : '')).toHaveLength(bodyLines(body).length);
  });

  it('applies the line pattern to each line, not to the body: a six-dash header on line 3 excludes the body (round-4 note 5)', () => {
    // Neither fragment is present ("------BEGIN-" has no space after BEGIN), so only a per-line reading of the pattern catches it.
    const body = `[b](https://x/y?${TOKEN})\n\n------BEGIN-KEY\nAAAA\n`;
    expect(redaction.wholeArtifactFragments.some(fragment => body.includes(fragment))).toBe(false);
    expect(redactBody(body, 'project-documentation', matcher, redaction)).toEqual({ kind: 'excluded', cause: 'key-header-line' });
  });

  it('compares each fragment anywhere in the body, mid-line included (round-4 note 5)', () => {
    const body = `[b](https://x/y?${TOKEN})\n\nsee "x-----BEGIN EC KEY" here\n`;
    expect(redactBody(body, 'project-documentation', matcher, redaction)).toEqual({ kind: 'excluded', cause: 'key-header-fragment' });
  });

  it('admits a body no detector matches unredacted, whatever it holds', () => {
    expect(redactBody('-----BEGIN CERTIFICATE-----\nMIIB\n', 'project-documentation', matcher, redaction)).toEqual({ kind: 'clean' });
  });

  it('excludes every matching body whole when the scope declares no redaction (versions 1 to 3)', () => {
    expect(redactBody(`a\n${TOKEN}\nb\n`, 'project-documentation', matcher, null)).toEqual({ kind: 'excluded', cause: 'no-redaction-rule' });
  });

  it('marks one marker per run of withheld lines, naming the total', () => {
    expect(retainedWithMarkers('a\n\n\nd\n\n', [2, 3, 5])).toBe('a\n[redacted-span: 3 withheld line(s) in this file]\nd\n[redacted-span: 3 withheld line(s) in this file]\n');
    expect(spanTouchesWithheld([2, 3], 3, 9)).toBe(true);
    expect(spanTouchesWithheld([2, 3], 4, 9)).toBe(false);
    expect(spanTouchesWithheld([2, 3], 1, 1)).toBe(false);
  });
});

describe('readSecretRedaction refuses what it does not implement', () => {
  const read = (mutate: (red: Record<string, unknown>) => void) => {
    const doc = policyDoc();
    const red = structuredClone(scopeOf(doc)['secretRedaction']) as Record<string, unknown>;
    mutate(red);
    return readSecretRedaction({ ...scopeOf(doc), secretRedaction: red }, idsOf(doc));
  };
  it('reads null for a scope without the object', () => {
    expect(readSecretRedaction({ activeContent: {} }, ['a'])).toEqual({ ok: true, redaction: null });
  });
  it.each<[string, (red: Record<string, unknown>) => void]>([
    ['an edited rule text', red => { red['rule'] = `${String(red['rule'])} `; }],
    ['an edited cited-span rule', red => { red['citedSpanRule'] = 'a span shows its surviving lines'; }],
    ['another line pattern', red => { red['wholeArtifactLinePattern'] = '^-----BEGIN '; }],
    ['an extra field', red => { red['extra'] = 1; }],
    ['a missing field', red => { delete red['guardLines']; }],
    ['another redaction class', red => { red['redactionClass'] = 'excluded-artifact'; }],
    ['an unknown redacted class', red => { red['redactedClasses'] = ['governance-text']; }],
    ['a whole-artifact detector naming no detector', red => { red['wholeArtifactDetectors'] = ['no-such-detector']; }],
    ['an empty fragment list', red => { red['wholeArtifactFragments'] = []; }],
    ['a zero guard', red => { red['guardLines'] = 0; }],
    ['a fractional guard', red => { red['guardLines'] = 1.5; }],
  ])('refuses %s', (_name, mutate) => {
    expect(read(mutate).ok).toBe(false);
  });
});
