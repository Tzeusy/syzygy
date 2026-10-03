import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { describe, expect, it } from 'vitest';

import { classifyDocumentation, parseDocumentationRule, type DocumentationRule } from './project-documentation.js';

// The builder's reference set, exported by `scripts/export_screening_scope_v2_parity.py`.
// Expected verdicts come from the Python reference reader, never from the module under test.
const REPO_ROOT = fileURLToPath(new URL('../../../../', import.meta.url));
const SNAPSHOT = fileURLToPath(new URL('./fixtures/screening-scope-v2-parity.json', import.meta.url));
const BUILDER = join(REPO_ROOT, 'scripts/build_public_source_screening_scope_v2.py');
type Row = [string, boolean[]];
interface ParitySet { readonly variantOrder: string[]; readonly rules: Record<string, Record<string, unknown>>; readonly fixtures: Row[]; readonly generated: Row[] }
const SET = JSON.parse(readFileSync(SNAPSHOT, 'utf8')) as ParitySet;
const VERSION = '1.3.0-public-source-candidate.1';

const parsed = (variant: string, rule: Record<string, unknown> = SET.rules[variant]!): DocumentationRule => {
  const result = parseDocumentationRule(rule, `${VERSION}.${variant}`);
  if (typeof result === 'string') throw new Error(result);
  return result;
};
const disagreements = (rows: readonly Row[]) => SET.variantOrder.flatMap((variant, index) => {
  const rule = parsed(variant);
  return rows.filter(([path, expected]) => classifyDocumentation(path, rule) !== expected[index]).map(([path]) => `${variant}: ${JSON.stringify(path)}`);
});

describe('project-documentation rule: parity with the builder reference reader', () => {
  it('carries all four variants and both populations', () => {
    expect(SET.variantOrder).toEqual(['none', 'manifesto', 'architecture', 'both']);
    expect(SET.fixtures.length).toBe(134);
    expect(SET.generated.length).toBe(4589);
    // Both verdicts occur in every variant, so neither a constant true nor a constant false passes.
    for (const index of [0, 1, 2, 3]) for (const rows of [SET.fixtures, SET.generated]) expect(new Set(rows.map(row => row[1][index]))).toEqual(new Set([true, false]));
  });

  it('agrees on every builder fixture in every variant', () => { expect(disagreements(SET.fixtures)).toEqual([]); });
  it('agrees on every generated path in every variant', () => { expect(disagreements(SET.generated)).toEqual([]); });

  // Live while #326's builder is on the tree: the snapshot must be what the builder exports now.
  it.skipIf(!existsSync(BUILDER))('the snapshot is the builder export (needs the #326 builder)', () => {
    const run = spawnSync('python3', [join(REPO_ROOT, 'scripts/export_screening_scope_v2_parity.py')], { cwd: REPO_ROOT, encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
    expect(run.status, run.stderr).toBe(0);
    expect(run.stdout).toBe(readFileSync(SNAPSHOT, 'utf8'));
  });
});

describe('project-documentation rule: reading the rule object', () => {
  const none = SET.rules.none!;
  const refusal = (rule: Record<string, unknown>, version = `${VERSION}.none`) => parseDocumentationRule(rule, version);

  it('reads each variant from its own row', () => {
    for (const variant of SET.variantOrder) expect(parsed(variant).variant).toBe(variant);
  });

  it('refuses a version naming no variant, or the wrong one', () => {
    expect(refusal(none, VERSION)).toBe('policyVersion names no screening-scope v2 variant');
    expect(refusal(none, `${VERSION}.manifesto`)).toBe('variant manifesto disagrees with the manifesto opt-in');
    expect(refusal(SET.rules.both!, `${VERSION}.architecture`)).toBe('variant architecture disagrees with the manifesto opt-in');
    // An opt-in word mapped at the root but still denied under docs is refused too.
    expect(refusal({ ...SET.rules.manifesto!, docExcludedTokens: [...(none.docExcludedTokens as string[])] }, `${VERSION}.manifesto`)).toBe('variant manifesto disagrees with the manifesto opt-in');
  });

  it('refuses path rules other than the three it implements', () => {
    const rules = none.pathRules as { id: string }[];
    expect(refusal({ ...none, pathRules: rules.slice(0, 2) })).toBe('pathRules are not root-document, docs-tree, licenses-tree');
    expect(refusal({ ...none, pathRules: [...rules, { id: 'nested-readme' }] })).toBe('pathRules are not root-document, docs-tree, licenses-tree');
    expect(refusal({ ...none, pathRules: [rules[1], rules[0], rules[2]] })).toBe('pathRules are not root-document, docs-tree, licenses-tree');
  });

  it('refuses an unreadable prefix', () => {
    const prefix = none.rootStemNumericPrefix as Record<string, unknown>;
    for (const broken of [{ ...prefix, digitCount: 0 }, { ...prefix, digitCount: 1.5 }, { ...prefix, digits: '' }, { ...prefix, digits: '٠١' }, { ...prefix, separator: '--' }, { ...prefix, separator: '‐' }])
      expect(refusal({ ...none, rootStemNumericPrefix: broken })).toBe('rootStemNumericPrefix unreadable');
    expect(refusal({ ...none, rootStemNumericPrefix: undefined })).toBe('rootStemNumericPrefix unreadable');
  });

  it('refuses each list when absent, empty, non-ASCII or not folded', () => {
    for (const name of ['rootStems', 'docTreeRoots', 'docTreeExtensions', 'docExcludedTokens', 'docTxtExcludedNames', 'docTxtExcludedPrefixes', 'licenseTreeRoots', 'licenseTreeSuffixes']) {
      for (const broken of [undefined, [], [''], ['Readme'], ['réadme'], 'readme']) expect(refusal({ ...none, [name]: broken })).toBe(`${name} unreadable`);
    }
    expect(refusal({ ...none, documentSuffixes: [] })).toBe('documentSuffixes unreadable');
    expect(refusal({ ...none, documentSuffixes: ['.MD'] })).toBe('documentSuffixes unreadable');
    for (const broken of [undefined, '', '‐'] as const) expect(refusal({ ...none, docTokenSeparators: broken })).toBe('docTokenSeparators unreadable');
  });

  it('reads the lists from the policy, not from constants', () => {
    const narrowed = parsed('none', { ...none, rootStems: ['readme'], docTreeRoots: ['guides'], licenseTreeRoots: ['legal'], docExcludedTokens: [...(none.docExcludedTokens as string[]), 'internal'] });
    expect(['README.md', 'guides/a.md', 'legal/x.txt'].map(path => classifyDocumentation(path, narrowed))).toEqual([true, true, true]);
    expect(['LICENSE', 'docs/a.md', 'licenses/x.txt', 'guides/internal-notes.md'].map(path => classifyDocumentation(path, narrowed))).toEqual([false, false, false, false]);
    const prefixed = parsed('none', { ...none, rootStemNumericPrefix: { digitCount: 3, digits: '01', separator: '_' } });
    expect(['101_README', '12-README', '102_README'].map(path => classifyDocumentation(path, prefixed))).toEqual([true, false, false]);
    const separated = parsed('none', { ...none, docTokenSeparators: '+' });
    expect(['docs/x+spec.md', 'docs/x-spec.md'].map(path => classifyDocumentation(path, separated))).toEqual([false, true]);
  });
});
