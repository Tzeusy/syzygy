// PWB-REQ-002 / PWB-REQ-004 (as amended 2026-09-05) — coverage reconciles
// to D and conflicts are preserved; a winner exists only when a layer row of
// the root index's own precedence table decides.
//
// Every expectation below is hand-typed from the fixtures. The conflict (a
// root summary stating eight butlers against nine declared) and the seven
// registry rows are spelled out here, never imported (the spec's
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
  type LayerRule,
  type ProjectShapeCoverage,
  type ReconciledFact,
} from './project-shape-coverage.js';
import { extractSource } from './project-shape-extraction.js';
import { EXTRACTION_CLASSES, type ExtractionClass, type ManifestSource, type SourceRule } from './project-shape-manifest.js';

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
  '- **Gamma** - three',
  '- **Delta** - four',
  '- **Epsilon** - five',
  '- **Zeta** - six',
  '- **Eta** - seven',
  '- **Theta** - eight',
  '- **Iota** - nine',
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

// The root index as Butlers writes it: the seven-row precedence table under
// its H3 (Layer bold, Home in code spans, wrapped continuation) and the
// summary stating eight butlers where v1.md declares nine.
const ROOT_TABLE = [
  '### Precedence Order When Layers Disagree',
  '',
  '| # | Layer | Owns | Home |',
  '|---|-------|------|------|',
  '| 1 | **Heart and Soul** | Principles, scope boundaries, the 7 non-negotiable rules | `about/heart-and-soul/` |',
  '| 2 | **Legends and Lore** | Wire contracts, state machines, data models, sanctioned rule exceptions | `about/legends-and-lore/rfcs/` |',
  '| 3 | **Spec and Spine** | Feature behaviour, acceptance scenarios (WHEN/THEN), per-butler contracts | `openspec/specs/` |',
  '| 4 | **Craft and Care** | Execution-quality standards, test scope, review gates, observability bar | `about/craft-and-care/` |',
  '| 5 | **Lay and Land** | Topology snapshot \u2014 where components live, how they connect, stability levels | `about/lay-and-land/` |',
  '| 6 | **Roster config** | Live butler identity: `butler.toml`, `MANIFESTO.md`, `CLAUDE.md`, skills, API routes | `roster/{butler}/` |',
  '| 7 | **Code** | Runtime behaviour \u2014 executed source, migrations, tests | `src/`, `alembic/`, `tests/` |',
];
const ROOT_SUMMARY = [
  '## Key Architectural Facts',
  '',
  '- **11 daemons** \u2014 3 staffers (Switchboard, Messenger, QA) + 8 domain',
  '  butlers, each a FastMCP server on its own port.',
  '- **One database** \u2014 shared.',
];
const ROOT = ['# Butlers', '', ...ROOT_TABLE, '', ...ROOT_SUMMARY, ''].join('\n');
const ROOT_NO_TABLE = ['# Butlers', '', ...ROOT_SUMMARY, ''].join('\n');
const ROOT_TABLE_ONLY = ['# Butlers', '', ...ROOT_TABLE, ''].join('\n');
const ROOT_PATH = 'about/README.md';
// 1-based lines in ROOT: the table header and its rows, the summary item.
const TABLE_LINE = 5;
const ROW_LINE = (ordinal: number): number => TABLE_LINE + 1 + ordinal;
const SUMMARY_ITEM_LINE = 17;

const OID = 'a'.repeat(40);
const digestOf = (path: string): string => `sha256:${path.replace(/[^a-z0-9]/gi, '').padEnd(64, '0').slice(0, 64)}`;

function manifestSource(path: string, classes: readonly ExtractionClass[], rule: SourceRule = 'pillar-named-file'): ManifestSource {
  // The anchor is irrelevant to coverage; any well-formed value. Only the
  // root-index rule matters: it selects the root grammar.
  return { path, rule, extractionClasses: classes, anchor: { kind: 'blob', mode: '100644', objectId: OID } };
}

const read = (path: string): ObjectReadRecord => ({ path, objectId: OID, outcome: 'read', bytes: 1, contentDigest: digestOf(path) });

function admitted(path: string, classes: readonly ExtractionClass[], text: string, rule?: SourceRule): CoverageSourceInput {
  const source = manifestSource(path, classes, rule);
  const record: ClassificationRecord = {
    path,
    outcome: 'classified',
    contentDigest: digestOf(path),
    extractionClasses: classes,
    policyId: PWB_SECRET_POLICY.policyId,
    policyVersion: PWB_SECRET_POLICY.policyVersion,
    detectorsRun: PWB_SECRET_POLICY.detectors.length,
    basis: 'body',
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

function excluded(path: string, classes: readonly ExtractionClass[], rule?: SourceRule): CoverageSourceInput {
  const source = manifestSource(path, classes, rule);
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
  return Array.from({ length: n }, (_, i) => admitted(`roster/b${i + 1}/butler.toml`, ['roster-identity'], `[butler]\nname = "b${i + 1}"\n`));
}

const root = (text: string): CoverageSourceInput => admitted(ROOT_PATH, [], text, 'root-index');

const BASE: readonly CoverageSourceInput[] = [
  admitted('about/heart-and-soul/vision.md', ['project-account-section', 'principle', 'success-criterion'], VISION),
  admitted('about/heart-and-soul/v1.md', ['project-account-section', 'success-criterion', 'catalog-entry'], V1),
  unavailable('about/legends-and-lore/README.md', ['design-contract']),
  excluded('about/craft-and-care/README.md', ['craft-policy']),
  admitted('about/lay-and-land/components.md', ['topology-component'], COMPONENTS_BAD),
  ...rosterSources(9),
];

const BUTLERS = 'catalog-count:Butlers';
const STAFFERS = 'catalog-count:Staffers';
const V1_PATH = 'about/heart-and-soul/v1.md';
const V1_BUTLERS_HEADING_LINE = 6;
const V1_STAFFERS_HEADING_LINE = 5;

// The summary's eight, as coverage must spell it: stated, anchored at the
// root's list item, digest of the root.
const SUMMARY_EIGHT: Declaration = {
  fact: BUTLERS,
  value: '8',
  basis: 'stated-summary',
  anchors: [{ path: ROOT_PATH, line: SUMMARY_ITEM_LINE, contentDigest: digestOf(ROOT_PATH) }],
};
const DERIVED_NINE: Declaration = {
  fact: BUTLERS,
  value: '9',
  basis: 'derived-count',
  anchors: [{ path: V1_PATH, line: V1_BUTLERS_HEADING_LINE, contentDigest: digestOf(V1_PATH) }],
};

// The seven registry rows, hand-typed (the registry's `precedence.rows`).
const ROWS: readonly [number, string, string, string][] = [
  [1, 'Heart and Soul', 'Principles, scope boundaries, the 7 non-negotiable rules', 'about/heart-and-soul/'],
  [2, 'Legends and Lore', 'Wire contracts, state machines, data models, sanctioned rule exceptions', 'about/legends-and-lore/rfcs/'],
  [3, 'Spec and Spine', 'Feature behaviour, acceptance scenarios (WHEN/THEN), per-butler contracts', 'openspec/specs/'],
  [4, 'Craft and Care', 'Execution-quality standards, test scope, review gates, observability bar', 'about/craft-and-care/'],
  [5, 'Lay and Land', 'Topology snapshot \u2014 where components live, how they connect, stability levels', 'about/lay-and-land/'],
  [6, 'Roster config', 'Live butler identity: butler.toml, MANIFESTO.md, CLAUDE.md, skills, API routes', 'roster/{butler}/'],
  [7, 'Code', 'Runtime behaviour \u2014 executed source, migrations, tests', 'src/, alembic/, tests/'],
];
const layerRule = (ordinal: number, anchorPath = ROOT_PATH): LayerRule => {
  const [o, layer, owns, home] = ROWS[ordinal - 1] as [number, string, string, string];
  return { id: `layer:${o}`, ordinal: o as LayerRule['ordinal'], layer, owns, home, anchor: { path: anchorPath, line: ROW_LINE(o), contentDigest: digestOf(ROOT_PATH) } };
};
const ALL_RULES: readonly LayerRule[] = ROWS.map(([o]) => layerRule(o));

const build = (sources: readonly CoverageSourceInput[]): ProjectShapeCoverage => buildProjectShapeCoverage({ sources });

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
    expect(c.counts).toMatchObject({ sources: 14, sourcesWithKnownItemDenominator: 11, sourcesWithUnknownDenominator: 3 });
    const byPath = new Map(c.sources.map((s) => [s.path, s]));
    expect(byPath.get('about/heart-and-soul/vision.md')?.itemDenominator).toEqual({ kind: 'known', value: 8 });
    expect(byPath.get('about/heart-and-soul/v1.md')?.itemDenominator).toEqual({ kind: 'known', value: 13 });
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
      'catalog-entry': [10, 10],
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
    expect(c.counts.items).toBe(30);
    expect(c.counts.modeled).toBe(30);
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
      expect(known.declarations[0]?.anchors).toEqual([{ path: 'about/heart-and-soul/vision.md', contentDigest: digestOf('about/heart-and-soul/vision.md') }]);
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

describe('PWB-REQ-004 — the root index declares the grammar facts and the layer rules', () => {
  let c: ProjectShapeCoverage;
  beforeAll(() => {
    c = build([root(ROOT), ...BASE]);
  });

  it('the root has zero item classes yet is an admitted source in the population', () => {
    expect(c.sources[0]).toMatchObject({ path: ROOT_PATH, extractionClasses: [], itemDenominator: { kind: 'known', value: 0 } });
    expect(c.counts).toMatchObject({ sources: 15, sourcesWithKnownItemDenominator: 12, sourcesWithUnknownDenominator: 3 });
  });

  it('the seven rows are admitted verbatim, anchored at their lines, ids layer:1..7', () => {
    expect(c.precedence).toEqual({ kind: 'admitted', anchor: { path: ROOT_PATH, line: TABLE_LINE, contentDigest: digestOf(ROOT_PATH) }, rules: ALL_RULES });
    expect(c.counts.rulesDeclared).toBe(7);
  });

  it('the summary emits exactly the two stated counts, nothing for the other bullet', () => {
    expect(c.rootSummary).toEqual({
      kind: 'emitted',
      anchor: { path: ROOT_PATH, line: SUMMARY_ITEM_LINE, contentDigest: digestOf(ROOT_PATH) },
      declarations: [{ ...SUMMARY_EIGHT, fact: STAFFERS, value: '3' }, SUMMARY_EIGHT],
    });
    expect(JSON.stringify(c.facts)).not.toContain('One database');
  });

  it('nine derived catalog counts, each anchored at its V1 heading; the project-account facts carry their statements', () => {
    const catalog = c.facts.filter((f) => f.fact.startsWith('catalog-count:'));
    expect(catalog.map((f) => f.fact)).toEqual([
      'catalog-count:Core Infrastructure',
      'catalog-count:Staffers',
      'catalog-count:Butlers',
      'catalog-count:Modules',
      'catalog-count:Connectors',
      'catalog-count:Dashboard',
      'catalog-count:Identity System',
      'catalog-count:Situational Awareness',
      'catalog-count:Observability',
    ]);
    const core = fact(c, 'catalog-count:Core Infrastructure');
    expect(core).toEqual({
      fact: 'catalog-count:Core Infrastructure',
      state: 'modeled',
      value: '1',
      declarations: [{ fact: 'catalog-count:Core Infrastructure', value: '1', basis: 'derived-count', anchors: [{ path: V1_PATH, line: 3, contentDigest: digestOf(V1_PATH) }] }],
      rulesConsidered: [],
    });
    // Staffers: v1.md declares none, the summary states three; row 1 owns
    // the family, so the derived zero is effective and the three is kept.
    const staffers = fact(c, STAFFERS);
    expect(staffers.state).toBe('modeled');
    expect(staffers.declarations.map((d) => [d.basis, d.value, d.anchors[0]?.line])).toEqual([['derived-count', '0', V1_STAFFERS_HEADING_LINE], ['stated-summary', '3', SUMMARY_ITEM_LINE]]);
    if (staffers.state === 'modeled') expect(staffers.disagreement).toMatchObject({ effective: { value: '0' }, superseded: [{ value: '3' }], precedence: { ruleId: 'layer:1' } });
    const purpose = fact(c, 'project-account:purpose');
    expect(purpose).toMatchObject({ state: 'modeled', value: 'Purpose.', declarations: [{ basis: 'extracted-item', anchors: [{ path: 'about/heart-and-soul/vision.md', line: 1 }] }] });
    expect(c.facts.filter((f) => f.fact.startsWith('project-account:')).map((f) => f.fact)).toEqual(['project-account:purpose', 'project-account:promises', 'project-account:refusals', 'project-account:v1-scope', 'project-account:v1-success']);
    // 30 identities, 9 class counts, 9 catalog counts, 5 project-account facts.
    expect(c.counts.facts).toBe(30 + 9 + 9 + 5);
  });

  it('every fact of the root grammar names a family the registry owns; nothing else is minted', () => {
    const families = new Set(c.facts.map((f) => f.fact.split(':')[0]));
    expect([...families].sort()).toEqual(['catalog-count', 'count', 'item', 'project-account']);
  });
});

describe('PWB-REQ-004 — eight stated against nine declared (catalog-count:Butlers)', () => {
  it('with the table: nine is effective by row 1, eight is superseded with its anchor, every row outcome is visible', () => {
    const c = build([root(ROOT), ...BASE]);
    const f = fact(c, BUTLERS);
    expect(f.state).toBe('modeled');
    if (f.state !== 'modeled') return;
    expect(f.value).toBe('9');
    expect(f.declarations).toEqual([DERIVED_NINE, SUMMARY_EIGHT]);
    expect(f.disagreement).toEqual({
      effective: DERIVED_NINE,
      superseded: [SUMMARY_EIGHT],
      precedence: {
        ruleId: 'layer:1',
        ordinal: 1,
        layer: 'Heart and Soul',
        anchor: { path: ROOT_PATH, line: ROW_LINE(1), contentDigest: digestOf(ROOT_PATH) },
        statement: '| 1 | Heart and Soul | Principles, scope boundaries, the 7 non-negotiable rules | about/heart-and-soul/ |',
      },
    });
    expect(f.rulesConsidered).toEqual([
      { ruleId: 'layer:1', outcome: 'applied' },
      { ruleId: 'layer:2', outcome: 'fact-out-of-scope' },
      { ruleId: 'layer:3', outcome: 'fact-out-of-scope' },
      { ruleId: 'layer:4', outcome: 'fact-out-of-scope' },
      { ruleId: 'layer:5', outcome: 'fact-out-of-scope' },
      { ruleId: 'layer:6', outcome: 'fact-out-of-scope' },
      { ruleId: 'layer:7', outcome: 'fact-out-of-scope' },
    ]);
    expect(c.contradictions).toEqual([]);
    expect(c.counts.rulesApplied).toBe(1);
  });

  it('without a rule: both values and sources shown, no winner, Unknown with the RFC2-24 reason', () => {
    const c = build([root(ROOT_NO_TABLE), ...BASE]);
    const f = fact(c, BUTLERS);
    expect(f.state).toBe('contradicted');
    if (f.state !== 'contradicted') return;
    expect(f.unknownReason).toBe('contradicted-pending-adjudication');
    // The summary item sits on line 5 once the table is gone.
    expect(f.declarations).toEqual([DERIVED_NINE, { ...SUMMARY_EIGHT, anchors: [{ path: ROOT_PATH, line: 5, contentDigest: digestOf(ROOT_PATH) }] }]);
    expect(f.rulesConsidered).toEqual([]);
    expect(c.contradictions.map((x) => x.fact)).toEqual([STAFFERS, BUTLERS]);
    expect(c.counts.contradictedFacts).toBe(2);
    expect(c.counts).toMatchObject({ rulesDeclared: 0, rulesApplied: 0 });
    expect(c.precedence).toEqual({ kind: 'absent', anchor: { path: ROOT_PATH, line: 1, contentDigest: digestOf(ROOT_PATH) }, reason: 'missing-heading', detail: 'Precedence Order When Layers Disagree' });
    // A contradicted count does not disturb the item states.
    expect(c.classes['catalog-entry']).toMatchObject({ declared: 10, modeled: 10, contradicted: 0 });
  });

  it('without a summary: nine alone is modeled, no disagreement, and the summary is disclosed absent', () => {
    const c = build([root(ROOT_TABLE_ONLY), ...BASE]);
    const f = fact(c, BUTLERS);
    expect(f).toEqual({ fact: BUTLERS, state: 'modeled', value: '9', declarations: [DERIVED_NINE], rulesConsidered: [] });
    expect(c.rootSummary).toMatchObject({ kind: 'absent', reason: 'missing-heading' });
    expect(c.counts.rulesDeclared).toBe(7);
  });

  it('a stale summary never silently replaces V1: agreement is modeled with both anchors kept', () => {
    const c = build([root(ROOT.replace('+ 8 domain', '+ 9 domain')), ...BASE]);
    const f = fact(c, BUTLERS);
    expect(f.state).toBe('modeled');
    if (f.state === 'modeled') {
      expect(f.disagreement).toBeUndefined();
      expect(f.declarations.map((d) => d.value)).toEqual(['9', '9']);
    }
  });

  it('a summary about a class with an Unknown denominator stays Unknown and is retained', () => {
    const v1Excluded = BASE.map((s) => (s.source.path === V1_PATH ? excluded(V1_PATH, s.source.extractionClasses) : s));
    const c = build([root(ROOT), ...v1Excluded]);
    const f = fact(c, BUTLERS);
    expect(f.state).toBe('unknown');
    if (f.state === 'unknown') {
      expect(f.unknownReason).toBe('excluded-content');
      expect(f.declarations).toEqual([SUMMARY_EIGHT]);
    }
  });

  it('the root outside the admitted population declares no rule and no summary', () => {
    const c = build([excluded(ROOT_PATH, [], 'root-index'), ...BASE]);
    expect(c.precedence).toEqual({ kind: 'unknown', reason: 'excluded-content' });
    expect(c.rootSummary).toEqual({ kind: 'unknown', reason: 'excluded-content' });
    expect(fact(c, BUTLERS).declarations).toEqual([DERIVED_NINE]);
    const none = build(BASE);
    expect(none.precedence).toEqual({ kind: 'unknown', reason: 'no root index in the manifest' });
  });

  it('no declaration is ever dropped', () => {
    const c = build([root(ROOT), ...BASE]);
    const all = c.facts.flatMap((f) => f.declarations);
    expect(all).toContainEqual(SUMMARY_EIGHT);
    expect(all).toContainEqual({ ...SUMMARY_EIGHT, fact: STAFFERS, value: '3' });
  });
});

describe('PWB-REQ-004 — a layer rule decides only under the registry conditions', () => {
  const population = new Set([ROOT_PATH, V1_PATH, 'about/heart-and-soul/vision.md', 'roster/b1/butler.toml', 'roster/b2/butler.toml']);
  const rosterKeys = new Set(['b1', 'b2']);
  const input = (rules: readonly LayerRule[]) => ({ rules, population, rosterKeys });
  const rejected = (rule: LayerRule, factName: string, declarations: readonly Declaration[], outcome: string, pop = population): void => {
    const f = reconcileFact(factName, declarations, { rules: [rule], population: pop, rosterKeys }, false);
    expect(f.state).toBe('contradicted');
    expect(f.rulesConsidered).toEqual([{ ruleId: rule.id, outcome }]);
    expect(RULE_REJECTIONS).toContain(outcome);
  };

  it('a rule cited from a path outside the admitted population decides nothing', () => {
    rejected(layerRule(1, 'about/legends-and-lore/README.md'), BUTLERS, [DERIVED_NINE, SUMMARY_EIGHT], 'anchor-not-in-population');
    rejected(layerRule(1), BUTLERS, [DERIVED_NINE, SUMMARY_EIGHT], 'anchor-not-in-population', new Set([V1_PATH]));
  });

  it('a row that does not own the fact family decides nothing', () => {
    for (const ordinal of [2, 3, 4, 5, 6, 7]) rejected(layerRule(ordinal), BUTLERS, [DERIVED_NINE, SUMMARY_EIGHT], 'fact-out-of-scope');
    rejected(layerRule(1), 'count:roster-identity', [DERIVED_NINE, SUMMARY_EIGHT], 'fact-out-of-scope');
    rejected(layerRule(1), 'butler-count-in-prose', [DERIVED_NINE, SUMMARY_EIGHT], 'fact-out-of-scope');
  });

  it('row 7 is inert: it never selects', () => {
    const d = (path: string, value: string): Declaration => ({ fact: 'count:baseline-spec', value, basis: 'derived-count', anchors: [{ path }] });
    rejected({ ...layerRule(7), ordinal: 3 as LayerRule['ordinal'], id: 'layer:3' }, 'count:baseline-spec', [d('src/a.py', '1'), d('openspec/specs/x.md', '2')], 'home-inert');
  });

  it('a home with no admitted source under it is not applied', () => {
    rejected(layerRule(3), 'count:baseline-spec', [
      { fact: 'count:baseline-spec', value: '1', basis: 'derived-count', anchors: [{ path: 'openspec/specs/a.md' }] },
      { fact: 'count:baseline-spec', value: '2', basis: 'stated-summary', anchors: [{ path: ROOT_PATH }] },
    ], 'home-not-applied');
  });

  it('row 6 expands only to declared roster keys; a roster path with no declared key is not a home', () => {
    const fact6 = 'count:roster-identity';
    const stated: Declaration = { fact: fact6, value: '8', basis: 'stated-summary', anchors: [{ path: ROOT_PATH }] };
    const derived: Declaration = { fact: fact6, value: '2', basis: 'derived-count', anchors: [{ path: 'roster/b1/butler.toml' }, { path: 'roster/b2/butler.toml' }] };
    const decided = reconcileFact(fact6, [derived, stated], input([layerRule(6)]), false);
    expect(decided.state).toBe('modeled');
    if (decided.state === 'modeled') expect(decided.disagreement?.precedence.ruleId).toBe('layer:6');
    const undeclared = reconcileFact(fact6, [derived, stated], { rules: [layerRule(6)], population, rosterKeys: new Set(['zeta']) }, false);
    expect(undeclared.state).toBe('contradicted');
    expect(undeclared.rulesConsidered).toEqual([{ ruleId: 'layer:6', outcome: 'home-not-applied' }]);
    const partial: Declaration = { ...derived, anchors: [{ path: 'roster/b1/butler.toml' }, { path: 'roster/zeta/butler.toml' }] };
    expect(reconcileFact(fact6, [partial, stated], input([layerRule(6)]), false).rulesConsidered).toEqual([{ ruleId: 'layer:6', outcome: 'no-declaration-under-home' }]);
  });

  it('no declaration under the applied home, or more than one, decides nothing', () => {
    rejected(layerRule(1), BUTLERS, [SUMMARY_EIGHT, { ...SUMMARY_EIGHT, value: '7', anchors: [{ path: ROOT_PATH, line: 40 }] }], 'no-declaration-under-home');
    rejected(layerRule(1), BUTLERS, [DERIVED_NINE, { ...DERIVED_NINE, value: '8', anchors: [{ path: 'about/heart-and-soul/vision.md', line: 1 }] }], 'more-than-one-declaration-under-home');
  });

  it('two applicable rules that disagree on the winner decide nothing', () => {
    // Two ordinal-1 rows (never admitted from one table; reconcileFact must
    // still refuse a split decision) with different homes.
    const a = layerRule(1);
    const b: LayerRule = { ...a, id: 'layer:1b', home: 'roster/{butler}/' };
    const stated6: Declaration = { ...SUMMARY_EIGHT, anchors: [{ path: 'roster/b1/butler.toml' }] };
    const f = reconcileFact(BUTLERS, [DERIVED_NINE, stated6], input([a, b]), false);
    expect(f.state).toBe('contradicted');
    expect(f.rulesConsidered).toEqual([
      { ruleId: 'layer:1', outcome: 'applied' },
      { ruleId: 'layer:1b', outcome: 'applied' },
    ]);
  });

  it('two applicable rules that agree name the first', () => {
    const twin: LayerRule = { ...layerRule(1), id: 'twin' };
    const f = reconcileFact(BUTLERS, [DERIVED_NINE, SUMMARY_EIGHT], input([layerRule(1), twin]), false);
    expect(f.state).toBe('modeled');
    if (f.state === 'modeled') expect(f.disagreement?.precedence.ruleId).toBe('layer:1');
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
    // The twin restates every catalog entry, so all ten identities are contradicted.
    expect(c.classes['catalog-entry']).toMatchObject({ declared: 10, modeled: 0, contradicted: 10, unknown: 0 });
    expect(c.counts.contradicted).toBe(10);
    // The two sources' derived catalog counts agree, so only the identities are contradicted.
    expect(c.counts.contradictedFacts).toBe(10);
  });

  it('equal statements are still a contradiction: the identity was declared twice', () => {
    const same = admitted('legacy/v1.md', ['catalog-entry'], V1);
    const c = build([...BASE, same]);
    expect(c.items.find((i) => i.class === 'catalog-entry' && i.key === 'Bus')?.state).toBe('contradicted');
  });

  it('row 1 selects the declaration under its home and keeps the legacy anchor; two under the home select nothing', () => {
    const c = build([root(ROOT), ...sources]);
    const alpha = c.items.find((i) => i.class === 'catalog-entry' && i.key === 'Alpha');
    expect(alpha).toMatchObject({ state: 'modeled', statement: '**Alpha** - one', precedence: { ruleId: 'layer:1', ordinal: 1 } });
    expect(alpha?.anchors).toHaveLength(2);
    expect(c.classes['catalog-entry']).toMatchObject({ declared: 10, modeled: 10, contradicted: 0 });
    const both = build([root(ROOT), ...BASE, admitted('about/heart-and-soul/legacy/v1.md', ['catalog-entry'], V1)]);
    const alphaBoth = both.items.find((i) => i.class === 'catalog-entry' && i.key === 'Alpha');
    expect(alphaBoth?.state).toBe('contradicted');
    expect(fact(both, 'item:catalog-entry:Alpha').rulesConsidered[0]).toEqual({ ruleId: 'layer:1', outcome: 'more-than-one-declaration-under-home' });
  });
});

describe('reconcileFact', () => {
  const population = new Set(['a.md']);
  const empty = { rules: [], population, rosterKeys: new Set<string>() };
  const d = (value: string, path: string): Declaration => ({ fact: 'f', value, basis: 'stated-summary', anchors: [{ path }] });

  it('refuses an empty declaration set', () => {
    expect(() => reconcileFact('f', [], empty, false)).toThrow(/no declarations/);
  });

  it('identity facts conflict on duplication, value facts only on disagreement', () => {
    expect(reconcileFact('f', [d('1', 'a.md'), d('1', 'b.md')], empty, false).state).toBe('modeled');
    expect(reconcileFact('f', [d('1', 'a.md'), d('1', 'b.md')], empty, true).state).toBe('contradicted');
    expect(reconcileFact('f', [d('1', 'a.md'), d('2', 'b.md')], empty, false).state).toBe('contradicted');
  });
});
