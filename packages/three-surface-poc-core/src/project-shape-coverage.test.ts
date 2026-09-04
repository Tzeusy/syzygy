// PWB-REQ-002 / PWB-REQ-004 — coverage reconciles to D and conflicts are
// preserved; a winner exists only when Butlers' own cited rule decides.
//
// Every expectation below is hand-typed from the fixtures. The conflict and
// the precedence rule are supplied independently of the model (the spec's
// oracle-independence clause).

import { beforeAll, describe, expect, it } from 'vitest';

import { type ClassificationRecord, type FixedUnknown, PWB_SECRET_POLICY } from './content-classification.js';
import type { ObjectReadRecord } from './git-object-reader.js';
import {
  CONTRADICTED_REASON,
  COVERAGE_STATES,
  DECLARATION_BASES,
  RULE_REJECTIONS,
  buildProjectShapeCoverage,
  countFact,
  reconcileFact,
  type CoverageSourceInput,
  type Declaration,
  type PrecedenceRule,
  type ProjectShapeCoverage,
  type ReconciledFact,
} from './project-shape-coverage.js';
import { extractSource } from './project-shape-extraction.js';
import { EXTRACTION_CLASSES, type ExtractionClass, type ManifestSource } from './project-shape-manifest.js';

// RFC2-24's twelve, typed here by hand rather than imported (oracle
// independence for the reason vocabulary).
const RFC2_24 = [
  'missing-declaration',
  'missing-evidence',
  'no-currency-bound-declared',
  'stale-beyond-currency-bound',
  'mapping-coverage-absent',
  'unconsented-source-or-provider',
  'excluded-content',
  'contradicted-pending-adjudication',
  'challenge-suspended',
  'source-uncaptured-or-unreachable',
  'reference-unresolvable',
  'unsupported-source-or-format',
];

// ---------------------------------------------------------------------
// Fixture texts (the extraction grammar, minimal).

const VISION = [
  '## What Butlers Is',
  'Purpose.',
  '## What Success Looks Like',
  '- one',
  '- two',
  '## What Butlers Is Not',
  'Refusals.',
  '## Non-Negotiable Rules',
  '1. **A** — a',
  '2. **B** — b',
  '3. **C** — c',
  '',
].join('\n');

const V1 = [
  '## What v1 Ships',
  'Ships.',
  '### Core Infrastructure',
  '- **Bus** - bus',
  '### Staffers',
  '### Butlers',
  '- **Alpha** - one',
  '- **Beta** - two',
  '### Modules',
  '### Connectors',
  '### Dashboard',
  '### Identity System',
  '### Situational Awareness',
  '### Observability',
  '## What v1 Defers',
  'Defers.',
  '## Success Criteria',
  '1. done',
  '',
].join('\n');

const COMPONENTS_BAD = ['## Overview', '| A | B |', '|---|---|', '| **x** | y |', ''].join('\n');

const OID = 'a'.repeat(40);
const digestOf = (path: string): string => `sha256:${path.replace(/[^a-z0-9]/gi, '').padEnd(64, '0').slice(0, 64)}`;

function manifestSource(path: string, classes: readonly ExtractionClass[]): ManifestSource {
  // The rule and anchor are irrelevant to coverage; any well-formed value.
  return { path, rule: 'pillar-named-file', extractionClasses: classes, anchor: { kind: 'blob', mode: '100644', objectId: OID } };
}

const read = (path: string): ObjectReadRecord => ({ path, objectId: OID, outcome: 'read', bytes: 1, contentDigest: digestOf(path) });

function admitted(path: string, classes: readonly ExtractionClass[], text: string): CoverageSourceInput {
  const source = manifestSource(path, classes);
  const record: ClassificationRecord = {
    path,
    outcome: 'classified',
    contentDigest: digestOf(path),
    extractionClasses: classes,
    policyId: PWB_SECRET_POLICY.policyId,
    policyVersion: PWB_SECRET_POLICY.policyVersion,
    detectorsRun: PWB_SECRET_POLICY.detectors.length,
  };
  return { source, read: read(path), record, value: extractSource(source, text) };
}

const UNREACHABLE: FixedUnknown = { failureState: 'sourceMissingOrUnreadable', degradationState: 'Source unreachable', unknownReason: 'source-uncaptured-or-unreachable' };
const EXCLUDED: FixedUnknown = { failureState: 'secretMatchedOrUnclassifiable', degradationState: 'Excluded content', unknownReason: 'excluded-content' };

function unavailable(path: string, classes: readonly ExtractionClass[]): CoverageSourceInput {
  const source = manifestSource(path, classes);
  return {
    source,
    read: { path, outcome: 'refused', bytes: 0, detail: 'missing-at-revision' },
    record: { path, outcome: 'unavailable', reason: 'missing-at-revision', unknown: UNREACHABLE },
  };
}

function excluded(path: string, classes: readonly ExtractionClass[]): CoverageSourceInput {
  const source = manifestSource(path, classes);
  return {
    source,
    read: read(path),
    record: {
      path,
      outcome: 'excluded',
      exclusion: {
        redactionClass: 'excluded-artifact',
        repositoryRelativePath: path,
        policyId: PWB_SECRET_POLICY.policyId,
        policyVersion: PWB_SECRET_POLICY.policyVersion,
        contentDigest: digestOf(path),
        detectorId: 'known-token-formats',
      },
      unknown: EXCLUDED,
    },
  };
}

function rosterSources(n: number): CoverageSourceInput[] {
  return Array.from({ length: n }, (_, i) => admitted(`roster/b${i + 1}/butler.toml`, ['roster-identity'], `[butler]\nname = "B${i + 1}"\n`));
}

const BASE: readonly CoverageSourceInput[] = [
  admitted('about/heart-and-soul/vision.md', ['project-account-section', 'principle', 'success-criterion'], VISION),
  admitted('about/heart-and-soul/v1.md', ['project-account-section', 'success-criterion', 'catalog-entry'], V1),
  unavailable('about/legends-and-lore/README.md', ['design-contract']),
  excluded('about/craft-and-care/README.md', ['craft-policy']),
  admitted('about/lay-and-land/components.md', ['topology-component'], COMPONENTS_BAD),
  ...rosterSources(9),
];

const SUMMARY_EIGHT: Declaration = {
  fact: countFact('roster-identity'),
  value: '8',
  basis: 'stated-summary',
  anchors: [{ path: 'about/README.md', line: 12 }],
};

const V1_RULE: PrecedenceRule = {
  id: 'v1-over-readme-counts',
  anchor: { path: 'about/heart-and-soul/v1.md', line: 3 },
  statement: 'Where the README summary and v1.md disagree on a count, v1.md is authoritative.',
  higher: { basis: 'derived-count' },
  lower: { path: 'about/README.md' },
  facts: [countFact('roster-identity')],
};

const build = (sources: readonly CoverageSourceInput[], extra: { rules?: PrecedenceRule[]; stated?: Declaration[] } = {}): ProjectShapeCoverage =>
  buildProjectShapeCoverage({
    sources,
    ...(extra.rules === undefined ? {} : { rules: extra.rules }),
    ...(extra.stated === undefined ? {} : { statedDeclarations: extra.stated }),
  });

const fact = (c: ProjectShapeCoverage, name: string): ReconciledFact => {
  const f = c.facts.find((x) => x.fact === name);
  if (f === undefined) throw new Error(`no fact ${name}`);
  return f;
};

// ---------------------------------------------------------------------

describe('PWB-REQ-002 — the source population never shrinks and every class reconciles to D', () => {
  // Built lazily so a construction failure is a counted test failure.
  let c: ProjectShapeCoverage;
  beforeAll(() => {
    c = build(BASE);
  });

  it('lists every input source in order with a known or fixed-reason Unknown item denominator', () => {
    expect(c.sources.map((s) => s.path)).toEqual(BASE.map((s) => s.source.path));
    expect(c.counts).toMatchObject({ sources: 14, sourcesAdmitted: 11, sourcesWithUnknownDenominator: 3 });
    const byPath = new Map(c.sources.map((s) => [s.path, s]));
    expect(byPath.get('about/heart-and-soul/vision.md')?.itemDenominator).toEqual({ kind: 'known', value: 8 });
    expect(byPath.get('about/heart-and-soul/v1.md')?.itemDenominator).toEqual({ kind: 'known', value: 6 });
    expect(byPath.get('about/legends-and-lore/README.md')?.itemDenominator).toEqual({ kind: 'unknown', unknown: UNREACHABLE });
    expect(byPath.get('about/craft-and-care/README.md')?.itemDenominator).toEqual({ kind: 'unknown', unknown: EXCLUDED });
    expect(byPath.get('roster/b9/butler.toml')?.itemDenominator).toEqual({ kind: 'known', value: 1 });
  });

  it('a grammar failure becomes the parse-failure exclusion: Unknown denominator, hash kept, failure named, body absent', () => {
    const s = c.sources.find((x) => x.path === 'about/lay-and-land/components.md');
    expect(s?.itemDenominator).toEqual({
      kind: 'unknown',
      unknown: EXCLUDED,
      grammarFailure: { reason: 'missing-heading', class: 'topology-component', detail: 'H2 beginning with a decimal ordinal' },
    });
    expect(s?.record.outcome).toBe('excluded');
    if (s?.record.outcome === 'excluded') {
      expect(s.record.exclusion.exclusionReason).toBe('parse-failure');
      expect(s.record.exclusion.contentDigest).toBe(digestOf('about/lay-and-land/components.md'));
      expect(s.record.exclusion.redactionClass).toBe('unclassifiable-excluded');
    }
    expect(JSON.stringify(c)).not.toContain('| **x** |');
  });

  it('hand-typed per-class counts: modeled + unknown + contradicted equals declared, identities appear once', () => {
    const expected: Record<ExtractionClass, [declared: number, denominator: number | string[]]> = {
      'project-account-section': [5, 5],
      principle: [3, 3],
      'success-criterion': [3, 3],
      'catalog-entry': [3, 3],
      'design-contract': [0, ['source-uncaptured-or-unreachable']],
      'baseline-spec': [0, 0],
      'topology-component': [0, ['excluded-content']],
      'craft-policy': [0, ['excluded-content']],
      'roster-identity': [9, 9],
    };
    for (const cls of EXTRACTION_CLASSES) {
      const k = c.classes[cls];
      const [declared, denominator] = expected[cls];
      expect(k.class).toBe(cls);
      expect(k.declared).toBe(declared);
      expect(k.modeled + k.unknown + k.contradicted).toBe(declared);
      expect(k.denominator).toEqual(typeof denominator === 'number' ? { kind: 'known', value: denominator } : { kind: 'unknown', reasons: denominator });
      expect(k.sourcesWithUnknownDenominator).toBe(typeof denominator === 'number' ? 0 : 1);
    }
    const identities = c.items.map((i) => `${i.class} ${i.key}`);
    expect(new Set(identities).size).toBe(identities.length);
    expect(c.counts.items).toBe(23);
    expect(c.counts.modeled).toBe(23);
    expect(c.counts.contradicted).toBe(0);
  });

  it('each item is modeled with its anchor path, line and content digest', () => {
    const b = c.items.find((i) => i.class === 'principle' && i.key === 'B');
    expect(b).toEqual({
      class: 'principle',
      key: 'B',
      state: 'modeled',
      anchors: [{ path: 'about/heart-and-soul/vision.md', line: 10, contentDigest: digestOf('about/heart-and-soul/vision.md') }],
      statement: '**B** — b',
    });
  });

  it('a count over an Unknown denominator is Unknown with the source reason, never a number', () => {
    const f = fact(c, countFact('design-contract'));
    expect(f.state).toBe('unknown');
    if (f.state === 'unknown') {
      expect(f.unknownReason).toBe('source-uncaptured-or-unreachable');
      expect(f.declarations.map((d) => d.basis)).toEqual(['derived-count']);
    }
    const known = fact(c, countFact('principle'));
    expect(known.state).toBe('modeled');
    if (known.state === 'modeled') {
      expect(known.value).toBe('3');
      expect(known.disagreement).toBeUndefined();
      expect(known.declarations[0]?.anchors).toEqual([{ path: 'about/heart-and-soul/vision.md' }]);
    }
  });

  it('every state and reason is from the closed vocabularies', () => {
    for (const i of c.items) expect(COVERAGE_STATES).toContain(i.state);
    for (const f of c.facts) {
      expect(COVERAGE_STATES).toContain(f.state);
      if (f.state !== 'modeled') expect(RFC2_24).toContain(f.unknownReason);
      for (const d of f.declarations) expect(DECLARATION_BASES).toContain(d.basis);
    }
    expect(CONTRADICTED_REASON).toBe('contradicted-pending-adjudication');
  });

  it('an upstream discovery uncertainty makes only its dependent class denominator Unknown', () => {
    const c = buildProjectShapeCoverage({
      sources: BASE,
      discoveryUncertainties: [{ classes: ['baseline-spec'], unknown: UNREACHABLE }],
    });
    expect(c.classes['baseline-spec']).toMatchObject({
      declared: 0,
      discoveryUnknown: 1,
      denominator: { kind: 'unknown', reasons: ['source-uncaptured-or-unreachable'] },
    });
    expect(c.classes['roster-identity'].denominator).toEqual({ kind: 'known', value: 9 });
    expect(fact(c, countFact('baseline-spec')).state).toBe('unknown');
  });
});

describe('PWB-REQ-004 — two declarations disagree about one fact', () => {
  const count = countFact('roster-identity');

  it('without a rule: both values and sources shown, no winner, Unknown with the RFC2-24 reason', () => {
    const c = build(BASE, { stated: [SUMMARY_EIGHT] });
    const f = fact(c, count);
    expect(f.state).toBe('contradicted');
    if (f.state !== 'contradicted') return;
    expect(f.unknownReason).toBe('contradicted-pending-adjudication');
    expect(f.declarations.map((d) => d.value)).toEqual(['9', '8']);
    expect(f.declarations[1]).toBe(SUMMARY_EIGHT);
    expect(f.declarations[0]?.anchors).toHaveLength(9);
    expect(f.rulesConsidered).toEqual([]);
    expect(c.contradictions).toEqual([f]);
    expect(c.counts.contradictedFacts).toBe(1);
    expect(c.counts.rulesApplied).toBe(0);
    // A contradicted count does not disturb the item states.
    expect(c.classes['roster-identity']).toMatchObject({ declared: 9, modeled: 9, contradicted: 0 });
  });

  it('with an applicable Butlers rule: the effective value names the rule, its anchor and its words; the loser stays visible', () => {
    const c = build(BASE, { stated: [SUMMARY_EIGHT], rules: [V1_RULE] });
    const f = fact(c, count);
    expect(f.state).toBe('modeled');
    if (f.state !== 'modeled') return;
    expect(f.value).toBe('9');
    expect(f.declarations.map((d) => d.value)).toEqual(['9', '8']);
    expect(f.disagreement?.effective.basis).toBe('derived-count');
    expect(f.disagreement?.superseded).toEqual([SUMMARY_EIGHT]);
    expect(f.disagreement?.precedence).toEqual({ ruleId: 'v1-over-readme-counts', anchor: { path: 'about/heart-and-soul/v1.md', line: 3 }, statement: V1_RULE.statement });
    expect(f.rulesConsidered).toEqual([{ ruleId: 'v1-over-readme-counts', outcome: 'applied' }]);
    expect(c.contradictions).toEqual([]);
    expect(c.counts.rulesDeclared).toBe(1);
    expect(c.counts.rulesApplied).toBe(1);
  });

  it('agreement between a summary and the derived count is modeled without a disagreement, both anchors kept', () => {
    const c = build(BASE, { stated: [{ ...SUMMARY_EIGHT, value: '9' }] });
    const f = fact(c, count);
    expect(f.state).toBe('modeled');
    if (f.state === 'modeled') {
      expect(f.disagreement).toBeUndefined();
      expect(f.declarations).toHaveLength(2);
    }
  });

  it('a summary about a class with an Unknown denominator stays Unknown and is retained', () => {
    const c = build(BASE, { stated: [{ ...SUMMARY_EIGHT, fact: countFact('design-contract'), value: '11' }], rules: [V1_RULE] });
    const f = fact(c, countFact('design-contract'));
    expect(f.state).toBe('unknown');
    if (f.state === 'unknown') expect(f.declarations.map((d) => d.value)).toEqual(['0', '11']);
  });

  const rejected = (rule: PrecedenceRule, outcome: string, sources: readonly CoverageSourceInput[] = BASE, stated: Declaration[] = [SUMMARY_EIGHT]): void => {
    const c = build(sources, { stated, rules: [rule] });
    const f = fact(c, count);
    expect(f.state).toBe('contradicted');
    expect(f.rulesConsidered).toEqual([{ ruleId: rule.id, outcome }]);
    expect(RULE_REJECTIONS).toContain(outcome);
  };

  it('a rule cited from a path outside the admitted population decides nothing', () => {
    rejected({ ...V1_RULE, anchor: { path: 'about/README.md', line: 1 } }, 'anchor-not-in-population');
    rejected({ ...V1_RULE, anchor: { path: 'about/legends-and-lore/README.md' } }, 'anchor-not-in-population');
    rejected({ ...V1_RULE, anchor: { path: 'about/lay-and-land/components.md' } }, 'anchor-not-in-population');
  });

  it('a rule scoped to other facts decides nothing', () => {
    rejected({ ...V1_RULE, facts: [countFact('principle')] }, 'fact-out-of-scope');
  });

  it('a rule whose sides do not each match exactly one declaration decides nothing', () => {
    rejected({ ...V1_RULE, higher: { path: 'nowhere.md' } }, 'higher-side-unmatched');
    rejected({ ...V1_RULE, lower: { path: 'nowhere.md' } }, 'lower-side-unmatched');
    rejected({ ...V1_RULE, higher: { basis: 'derived-count' }, lower: { basis: 'derived-count' } }, 'same-declaration-both-sides');
    rejected({ ...V1_RULE, lower: { basis: 'stated-summary' } }, 'side-matched-more-than-once', BASE, [SUMMARY_EIGHT, { ...SUMMARY_EIGHT, value: '7', anchors: [{ path: 'about/README.md', line: 40 }] }]);
  });

  it('two applicable rules that disagree on the winner decide nothing', () => {
    const reverse: PrecedenceRule = { ...V1_RULE, id: 'readme-over-v1', higher: { path: 'about/README.md' }, lower: { basis: 'derived-count' } };
    const c = build(BASE, { stated: [SUMMARY_EIGHT], rules: [V1_RULE, reverse] });
    const f = fact(c, count);
    expect(f.state).toBe('contradicted');
    expect(f.rulesConsidered).toEqual([
      { ruleId: 'v1-over-readme-counts', outcome: 'applied' },
      { ruleId: 'readme-over-v1', outcome: 'applied' },
    ]);
    expect(c.counts.rulesApplied).toBe(0);
  });

  it('two applicable rules that agree name the first', () => {
    const twin: PrecedenceRule = { ...V1_RULE, id: 'twin' };
    const f = fact(build(BASE, { stated: [SUMMARY_EIGHT], rules: [V1_RULE, twin] }), count);
    expect(f.state).toBe('modeled');
    if (f.state === 'modeled') expect(f.disagreement?.precedence.ruleId).toBe('v1-over-readme-counts');
  });

  it('a stated fact this module derives nothing for is reconciled on its own', () => {
    const a: Declaration = { fact: 'butler-count-in-prose', value: '8', basis: 'stated-summary', anchors: [{ path: 'about/README.md', line: 1 }] };
    const b: Declaration = { ...a, value: '9', anchors: [{ path: 'about/heart-and-soul/vision.md', line: 2 }] };
    const c = build(BASE, { stated: [a, b] });
    const f = fact(c, 'butler-count-in-prose');
    expect(f.state).toBe('contradicted');
    expect(f.declarations).toEqual([a, b]);
    const alone = fact(build(BASE, { stated: [a] }), 'butler-count-in-prose');
    expect(alone.state).toBe('modeled');
  });

  it('no declaration is ever dropped', () => {
    const stated = [SUMMARY_EIGHT, { ...SUMMARY_EIGHT, fact: countFact('principle'), value: '3' }, { ...SUMMARY_EIGHT, fact: 'x', value: 'y' }];
    const c = build(BASE, { stated, rules: [V1_RULE] });
    const all = c.facts.flatMap((f) => f.declarations);
    for (const d of stated) expect(all).toContain(d);
  });
});

describe('PWB-REQ-004 — a duplicate item identity across sources is a contradiction', () => {
  const twin = admitted('legacy/v1.md', ['catalog-entry'], V1.replace('- **Alpha** - one', '- **Alpha** - one, restated'));
  const sources = [...BASE, twin];

  it('the identity appears once, contradicted, with both anchors and no statement chosen', () => {
    const c = build(sources);
    const alpha = c.items.filter((i) => i.class === 'catalog-entry' && i.key === 'Alpha');
    expect(alpha).toHaveLength(1);
    expect(alpha[0]).toMatchObject({ state: 'contradicted', unknownReason: 'contradicted-pending-adjudication', statement: '**Alpha** - one' });
    expect(alpha[0]?.anchors.map((a) => a.path)).toEqual(['about/heart-and-soul/v1.md', 'legacy/v1.md']);
    expect(alpha[0]?.precedence).toBeUndefined();
    // The twin restates every catalog entry, so all three identities are contradicted.
    expect(c.classes['catalog-entry']).toMatchObject({ declared: 3, modeled: 0, contradicted: 3, unknown: 0 });
    expect(c.counts.contradicted).toBe(3);
    expect(c.counts.contradictedFacts).toBe(3);
  });

  it('equal statements are still a contradiction: the identity was declared twice', () => {
    const same = admitted('legacy/v1.md', ['catalog-entry'], V1);
    const c = build([...BASE, same]);
    expect(c.items.find((i) => i.class === 'catalog-entry' && i.key === 'Bus')?.state).toBe('contradicted');
  });

  it('a cited Butlers rule selects the effective statement and keeps the other anchor', () => {
    const rule: PrecedenceRule = {
      id: 'about-over-legacy',
      anchor: { path: 'about/heart-and-soul/vision.md', line: 1 },
      statement: 'The about tree supersedes legacy copies.',
      higher: { path: 'about/heart-and-soul/v1.md' },
      lower: { path: 'legacy/v1.md' },
    };
    const c = build(sources, { rules: [rule] });
    const alpha = c.items.find((i) => i.class === 'catalog-entry' && i.key === 'Alpha');
    expect(alpha).toMatchObject({ state: 'modeled', statement: '**Alpha** - one', precedence: { ruleId: 'about-over-legacy' } });
    expect(alpha?.anchors).toHaveLength(2);
    expect(c.classes['catalog-entry']).toMatchObject({ declared: 3, modeled: 3, contradicted: 0 });
    const reversed = build(sources, { rules: [{ ...rule, higher: rule.lower, lower: rule.higher }] });
    expect(reversed.items.find((i) => i.key === 'Alpha')?.statement).toBe('**Alpha** - one, restated');
  });
});

describe('reconcileFact', () => {
  const population = new Set(['a.md']);
  const d = (value: string, path: string): Declaration => ({ fact: 'f', value, basis: 'stated-summary', anchors: [{ path }] });

  it('refuses an empty declaration set', () => {
    expect(() => reconcileFact('f', [], { rules: [], population }, false)).toThrow(/no declarations/);
  });

  it('identity facts conflict on duplication, value facts only on disagreement', () => {
    expect(reconcileFact('f', [d('1', 'a.md'), d('1', 'b.md')], { rules: [], population }, false).state).toBe('modeled');
    expect(reconcileFact('f', [d('1', 'a.md'), d('1', 'b.md')], { rules: [], population }, true).state).toBe('contradicted');
    expect(reconcileFact('f', [d('1', 'a.md'), d('2', 'b.md')], { rules: [], population }, false).state).toBe('contradicted');
  });
});
