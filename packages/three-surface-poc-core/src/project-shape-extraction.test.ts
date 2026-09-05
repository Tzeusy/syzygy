// PWB-REQ-002 — two independent extractors apply the literal grammar.
//
// The module under test is a line parser. The oracle below is a second,
// regex-only extractor written from the spec's "Reader definitions" without
// reading the module; the two must mint the same identities and the same
// per-class denominators over every fixture, and the module must yield no
// partial set on any malformed fixture.

import { describe, expect, it } from 'vitest';

import { EXTRACTION_CLASSES, type ExtractionClass } from './project-shape-manifest.js';
import {
  CATALOG_HEADINGS,
  EXTRACTION_FAILURES,
  PROJECT_ACCOUNT_KEYS,
  extractClass,
  extractSource,
  type ExtractedItem,
  type SourceExtraction,
} from './project-shape-extraction.js';
import { ParsePassBudgetExceeded, type ParsePassIdentity } from './resource-ledger.js';

// ---------------------------------------------------------------------
// Fixtures — hand-written in the literal grammar. Composed characters use
// NFD in the source (e.g. "é") so the NFC requirement is observable.

const VISION = [
  '# Butlers',
  '',
  'Intro paragraph mentioning ## What Butlers Is inline, which is not a heading.',
  '',
  '## What Butlers Is',
  '',
  'A household of agents that keep promises.',
  '',
  '### Detail',
  '',
  'Nested detail belongs to the purpose section.',
  '',
  '## What Success Looks Like',
  '',
  '- Every promise is visible.',
  '- Nothing is inferred silently.',
  '  - a nested bullet mints nothing',
  '',
  '  continuation text',
  '* Cafe\u0301 keeps its accent.',
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
  '```',
  '## Not A Heading',
  '3. **Fenced rule** — never counted.',
  '```',
  '',
  '3. **Cafe\u0301 rule** — composed key.',
  '',
  '## Appendix',
  '',
  '1. **Not a principle** — outside the rules section.',
  '',
].join('\n');

const ARCHITECTURE = ['# Architecture', '', 'Preamble.', '', '## Runtime', '', 'One process.', '', '## Storage', '', 'One database.', ''].join('\n');

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
  '- `scheduler` — the clock',
  '',
  '### Staffers',
  '',
  '- **Butler Prime** – the first staffer',
  '',
  '### Butlers',
  '',
  '### Modules',
  '',
  '- **Mail** - mail module',
  '',
  '### Connectors',
  '',
  '- `whatsapp` - connector',
  '',
  '### Dashboard',
  '',
  '### Identity System',
  '',
  '- **Identity** - resolution',
  '',
  '### Situational Awareness',
  '',
  '### Observability',
  '',
  '- **Tracing** - spans',
  '',
  '## What v1 Defers',
  '',
  'Defers text.',
  '',
  '## Success Criteria',
  '',
  '1. Ships on time.',
  '2. Stays honest.',
  '',
].join('\n');

const LORE_README = [
  '# Legends and Lore',
  '',
  '## Index',
  '',
  '| Contract | Status |',
  '| --- | --- |',
  '| [RFC 0001](0001.md) | accepted |',
  '| [RFC 0002](0002.md) | candidate |',
  '',
  '## Other',
  '',
  '| Contract | Status |',
  '|---|---|',
  '| [RFC 0099](0099.md) | not indexed |',
  '',
].join('\n');

const COMPONENTS = [
  '# Components',
  '',
  '## Overview',
  '',
  '| Name | Role |',
  '|---|---|',
  '| **Ignored** | no ordinal |',
  '',
  '## 1 Runtime',
  '',
  '| Component | Role |',
  '|---|---|',
  '| **Daemon** | serves |',
  '| **Store** | keeps |',
  '',
  '## 2a Adapters',
  '',
  'Prose.',
  '',
  '| Component | Role |',
  '|---|---|',
  '| **Daemon** | same label, other ordinal |',
  '',
  '## 12. Tools',
  '',
  '| Component | Role |',
  '|---|---|',
  '| **cli** | drives |',
  '',
  '## 3ab Not an ordinal',
  '',
  '| Component | Role |',
  '|---|---|',
  '| **Ghost** | never minted |',
  '',
].join('\n');

const CRAFT_README = [
  '# Craft and Care',
  '',
  '### Reading Order',
  '',
  '| Order | File | Why |',
  '|---|---|---|',
  '| 1 | [Spec policy](policies/cc-spec.md) | first |',
  '| 2 | [Impact](./cc-impact.md#top) | second |',
  '',
].join('\n');

const ROSTER = ['# comment', '', '[meta]', 'name = "not this one"', '', '[butler]', 'kind = "x"', 'name = "Alfred"  # trailing', ''].join('\n');

interface Fixture {
  readonly path: string;
  readonly classes: readonly ExtractionClass[];
  readonly text: string;
}

const FIXTURES: readonly Fixture[] = [
  { path: 'heart-and-soul/vision.md', classes: ['project-account-section', 'principle', 'success-criterion'], text: VISION },
  { path: 'heart-and-soul/architecture.md', classes: ['project-account-section'], text: ARCHITECTURE },
  { path: 'heart-and-soul/v1.md', classes: ['project-account-section', 'success-criterion', 'catalog-entry'], text: V1 },
  { path: 'legends-and-lore/README.md', classes: ['design-contract'], text: LORE_README },
  { path: 'lay-and-land/components.md', classes: ['topology-component'], text: COMPONENTS },
  { path: 'craft-and-care/README.md', classes: ['craft-policy'], text: CRAFT_README },
  { path: 'roster/alfred/butler.toml', classes: ['roster-identity'], text: ROSTER },
  { path: 'openspec/specs/identity/spec.md', classes: ['baseline-spec'], text: '# spec\n' },
];

// ---------------------------------------------------------------------
// Oracle — a regex-only reading of the grammar, independent of the module.

const N = (s: string): string => s.normalize('NFC');

function stripFences(text: string): string {
  return text.replace(/^(```|~~~)[^\n]*\n[\s\S]*?^\1[ \t]*$/gm, '');
}

// Body of the H<level> heading with exact text: from the heading line to
// the next heading of level <= level.
function sectionBody(text: string, level: number, heading: string): string | undefined {
  const hashes = '#'.repeat(level);
  const src = stripFences(text);
  const re = new RegExp(`^${hashes} ${heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}[ \\t]*$`, 'm');
  const m = re.exec(src);
  if (!m) return undefined;
  const after = src.slice(m.index + m[0].length);
  const stop = new RegExp(`^#{1,${level}} `, 'm').exec(after);
  return stop ? after.slice(0, stop.index) : after;
}

function topLevelItems(body: string, marker: 'decimal' | 'bullet' | 'any'): string[] {
  const re = marker === 'decimal' ? /^\d+[.)] +(.+)$/gm : marker === 'bullet' ? /^[-*+] +(.+)$/gm : /^(?:\d+[.)]|[-*+]) +(.+)$/gm;
  return [...body.matchAll(re)].map((m) => N((m[1] as string).trim()));
}

function tableRowsAfter(body: string): string[][] | undefined {
  const m = /^\|.*\n\|?[ \t]*:?-+.*\n((?:\|.*\n?)*)/m.exec(body);
  if (!m) return undefined;
  return (m[1] as string)
    .split('\n')
    .filter((l) => l.startsWith('|'))
    .map((l) =>
      l
        .replace(/^\|/, '')
        .replace(/\|$/, '')
        .split('|')
        .map((c) => N(c.trim())),
    );
}

function oracle(fixture: Fixture): ReadonlyMap<ExtractionClass, readonly string[]> {
  const out = new Map<ExtractionClass, string[]>();
  const base = fixture.path.split('/').pop() as string;
  for (const cls of fixture.classes) {
    const keys: string[] = [];
    switch (cls) {
      case 'project-account-section': {
        if (base === 'vision.md') keys.push('purpose', 'promises', 'refusals');
        if (base === 'architecture.md' && /^## /m.test(stripFences(fixture.text))) keys.push('architecture');
        if (base === 'v1.md') keys.push('v1-scope', 'v1-success');
        break;
      }
      case 'principle': {
        const body = sectionBody(fixture.text, 2, 'Non-Negotiable Rules') as string;
        for (const item of topLevelItems(body, 'decimal')) keys.push(N((/^\*\*(.+?)\*\*/.exec(item) as RegExpExecArray)[1] as string));
        break;
      }
      case 'success-criterion': {
        const prefix = base === 'vision.md' ? 'vision' : 'v1';
        const body = sectionBody(fixture.text, 2, prefix === 'vision' ? 'What Success Looks Like' : 'Success Criteria') as string;
        topLevelItems(body, 'any').forEach((_, i) => keys.push(`${prefix}:${i + 1}`));
        break;
      }
      case 'catalog-entry': {
        for (const h of CATALOG_HEADINGS) {
          const body = sectionBody(fixture.text, 3, h) as string;
          for (const item of topLevelItems(body, 'bullet')) {
            const m = /^(?:\*\*(.+?)\*\*|`(.+?)`) *[-–—]/.exec(item) as RegExpExecArray;
            keys.push(N((m[1] ?? m[2]) as string));
          }
        }
        break;
      }
      case 'design-contract': {
        const rows = tableRowsAfter(sectionBody(fixture.text, 2, 'Index') as string) as string[][];
        for (const row of rows) keys.push(N((/^\[(.+?)\]\(/.exec(row[0] as string) as RegExpExecArray)[1] as string));
        break;
      }
      case 'baseline-spec':
        keys.push((/^openspec\/specs\/([^/]+)\/spec\.md$/.exec(fixture.path) as RegExpExecArray)[1] as string);
        break;
      case 'topology-component': {
        const src = stripFences(fixture.text);
        for (const m of src.matchAll(/^## (\d+[a-z]?)\b[^\n]*\n([\s\S]*?)(?=^## |(?![\s\S]))/gm)) {
          const ordinal = m[1] as string;
          const body = m[2] as string;
          for (const table of body.matchAll(/^\|.*\n\|?[ \t]*:?-+.*\n((?:\|.*\n?)*)/gm)) {
            for (const line of (table[1] as string).split('\n').filter((l) => l.startsWith('|'))) {
              const first = (line.replace(/^\|/, '').split('|')[0] as string).trim();
              keys.push(`${ordinal}:${N((/^\*\*(.+)\*\*$/.exec(first) as RegExpExecArray)[1] as string)}`);
            }
          }
        }
        break;
      }
      case 'craft-policy': {
        const src = stripFences(fixture.text);
        const m = /^#{1,6} Reading Order[ \t]*$/m.exec(src) as RegExpExecArray;
        const body = src.slice(m.index + m[0].length);
        const header = (/^\|(.*)\|?$/m.exec(body) as RegExpExecArray)[1] as string;
        const column = header.split('|').map((c) => c.trim()).indexOf('File');
        for (const row of tableRowsAfter(body) as string[][]) {
          const target = (/\]\(([^)#\s]+)/.exec(row[column] as string) as RegExpExecArray)[1] as string;
          keys.push(N(target.split('/').pop() as string));
        }
        break;
      }
      case 'roster-identity': {
        const table = /^\[butler\][^\n]*\n((?:(?!^\[)[^\n]*\n?)*)/m.exec(fixture.text) as RegExpExecArray;
        const name = /^name *= *"([^"]*)"/m.exec(table[1] as string) as RegExpExecArray;
        if ((name[1] as string).length > 0) keys.push((/^roster\/([^/]+)\/butler\.toml$/.exec(fixture.path) as RegExpExecArray)[1] as string);
        break;
      }
    }
    out.set(cls, keys);
  }
  return out;
}

// ---------------------------------------------------------------------

const extracted = (f: Fixture): SourceExtraction & { kind: 'extracted' } => {
  const r = extractSource({ path: f.path, extractionClasses: f.classes }, f.text);
  if (r.kind !== 'extracted') throw new Error(`${f.path}: ${JSON.stringify(r.kind === 'unknown' ? r.failure : r.breach)}`);
  return r;
};

const keysOf = (r: SourceExtraction & { kind: 'extracted' }, cls: ExtractionClass): string[] =>
  r.items.filter((i) => i.class === cls).map((i) => i.key);

describe('PWB-REQ-002 — two independent extractors agree on every fixture', () => {
  for (const fixture of FIXTURES) {
    it(`${fixture.path} mints the oracle's identities and denominators`, () => {
      const result = extracted(fixture);
      const expected = oracle(fixture);
      expect(result.classes).toEqual(fixture.classes);
      for (const cls of fixture.classes) {
        expect(keysOf(result, cls)).toEqual(expected.get(cls));
        expect(result.denominators[cls]).toBe((expected.get(cls) as string[]).length);
      }
      // Every item's class is one the manifest assigned to this source.
      expect(result.items.every((i) => fixture.classes.includes(i.class))).toBe(true);
      // Identity is (class, key); anchors are the source path and a line.
      for (const item of result.items) {
        expect(item.path).toBe(fixture.path);
        expect(item.line).toBeGreaterThanOrEqual(1);
        expect(item.key).toBe(item.key.normalize('NFC'));
        expect(item.key.length).toBeGreaterThan(0);
      }
    });
  }

  it('the six project-account keys are minted exactly once across the three account files', () => {
    const keys = FIXTURES.filter((f) => f.classes.includes('project-account-section')).flatMap((f) => keysOf(extracted(f), 'project-account-section'));
    expect([...keys].sort()).toEqual([...PROJECT_ACCOUNT_KEYS].sort());
  });

  it('hand-typed expectations pin the grammar on the vision fixture', () => {
    const r = extracted(FIXTURES[0] as Fixture);
    expect(keysOf(r, 'principle')).toEqual(['Fail closed', 'Cite or stay quiet', 'Café rule']);
    expect(keysOf(r, 'success-criterion')).toEqual(['vision:1', 'vision:2', 'vision:3']);
    expect(r.denominators).toEqual({ 'project-account-section': 3, principle: 3, 'success-criterion': 3 });
    const purpose = r.items.find((i) => i.key === 'purpose') as ExtractedItem;
    expect(purpose.line).toBe(5);
    expect(purpose.statement).toBe('A household of agents that keep promises.\n\n### Detail\n\nNested detail belongs to the purpose section.');
    const third = r.items.find((i) => i.key === 'vision:3') as ExtractedItem;
    expect(third.statement).toBe('Café keeps its accent.');
  });

  it('hand-typed expectations pin the grammar on the v1, lore, components, craft and roster fixtures', () => {
    const v1 = extracted(FIXTURES[2] as Fixture);
    expect(keysOf(v1, 'catalog-entry')).toEqual(['Bus', 'scheduler', 'Butler Prime', 'Mail', 'whatsapp', 'Identity', 'Tracing']);
    expect(v1.items.filter((i) => i.class === 'catalog-entry').map((i) => i.context)).toEqual([
      'Core Infrastructure',
      'Core Infrastructure',
      'Staffers',
      'Modules',
      'Connectors',
      'Identity System',
      'Observability',
    ]);
    expect(keysOf(v1, 'success-criterion')).toEqual(['v1:1', 'v1:2']);
    const scope = v1.items.find((i) => i.key === 'v1-scope') as ExtractedItem;
    expect(scope.statement?.startsWith('What v1 Ships\n\nShips text.')).toBe(true);
    expect(scope.statement?.endsWith('What v1 Defers\n\nDefers text.')).toBe(true);
    expect(keysOf(extracted(FIXTURES[3] as Fixture), 'design-contract')).toEqual(['RFC 0001', 'RFC 0002']);
    expect(keysOf(extracted(FIXTURES[4] as Fixture), 'topology-component')).toEqual(['1:Daemon', '1:Store', '2a:Daemon', '12:cli']);
    expect(keysOf(extracted(FIXTURES[5] as Fixture), 'craft-policy')).toEqual(['cc-spec.md', 'cc-impact.md']);
    const roster = extracted(FIXTURES[6] as Fixture);
    expect(roster.items).toEqual([{ class: 'roster-identity', key: 'alfred', path: 'roster/alfred/butler.toml', line: 8, context: 'Alfred' }]);
    const arch = extracted(FIXTURES[1] as Fixture);
    expect((arch.items[0] as ExtractedItem).statement).toBe('Runtime\n\nOne process.\n\nStorage\n\nOne database.');
  });

  it('never emits HTML or body text beyond the declared statement', () => {
    for (const fixture of FIXTURES) {
      const json = JSON.stringify(extracted(fixture));
      expect(json).not.toMatch(/<[a-z]/i);
      expect(json).not.toContain('"text"');
    }
  });

  it('preserves every indented continuation line of a principle declaration', () => {
    const text = VISION.replace('1. **Fail closed** — silence is Unknown.', '1. **Fail closed** — silence is Unknown.\n   The declaration continues here.\n   And remains complete.');
    const result = extractClass('principle', 'heart-and-soul/vision.md', text);
    expect(result.kind).toBe('items');
    if (result.kind === 'items') expect(result.items[0]?.statement).toBe('**Fail closed** — silence is Unknown.\nThe declaration continues here.\nAnd remains complete.');
  });

  it.each([
    ['success-criterion' as const, 'heart-and-soul/vision.md', VISION.replace('- Every promise is visible.', '- Every promise is visible.\n  Including its wrapped qualification.'), 'Every promise is visible.\nIncluding its wrapped qualification.'],
    ['catalog-entry' as const, 'heart-and-soul/v1.md', V1.replace('- **Mail** - mail module', '- **Mail** - mail module\n  with its complete declared boundary.'), '**Mail** - mail module\nwith its complete declared boundary.'],
    ['principle' as const, 'heart-and-soul/vision.md', VISION.replace('1. **Fail closed** — silence is Unknown.', '1. **Fail\n   closed** — silence is Unknown.'), '**Fail\nclosed** — silence is Unknown.'],
    ['catalog-entry' as const, 'heart-and-soul/v1.md', V1.replace('- **Mail** - mail module', '- **Mail**\n  - mail module'), '**Mail**\n- mail module'],
  ])('preserves multiline %s declarations without minting a second item', (cls, path, text, expected) => {
    const result = extractClass(cls, path, text);
    expect(result.kind).toBe('items');
    if (result.kind === 'items') expect(result.items.find((item) => item.statement === expected)).toBeDefined();
  });
});

// ---------------------------------------------------------------------
// Malformed fixtures: the whole source is Unknown, never a partial set.

interface Malformed {
  readonly name: string;
  readonly path: string;
  readonly classes: readonly ExtractionClass[];
  readonly text: string;
  readonly reason: (typeof EXTRACTION_FAILURES)[number];
  readonly class: ExtractionClass;
  readonly line?: number;
  readonly detail?: string;
}

const MALFORMED: readonly Malformed[] = [
  {
    name: 'vision without the refusals heading',
    path: 'heart-and-soul/vision.md',
    classes: ['project-account-section', 'principle', 'success-criterion'],
    text: VISION.replace('## What Butlers Is Not', '## What Butlers Is not'),
    reason: 'missing-heading',
    class: 'project-account-section',
    detail: 'What Butlers Is Not',
  },
  {
    name: 'vision with the purpose heading twice',
    path: 'heart-and-soul/vision.md',
    classes: ['project-account-section'],
    text: `${VISION}\n## What Butlers Is\n\nagain\n`,
    reason: 'duplicate-key',
    class: 'project-account-section',
    detail: 'What Butlers Is',
  },
  {
    name: 'vision whose purpose heading is an H3',
    path: 'heart-and-soul/vision.md',
    classes: ['project-account-section'],
    text: VISION.replace('## What Butlers Is\n', '### What Butlers Is\n'),
    reason: 'missing-heading',
    class: 'project-account-section',
  },
  {
    name: 'a bullet among the decimal principles',
    path: 'heart-and-soul/vision.md',
    classes: ['principle'],
    text: VISION.replace('2. **Cite or stay quiet**', '- **Cite or stay quiet**'),
    reason: 'malformed-list',
    class: 'principle',
    line: 29,
  },
  {
    name: 'a principle without a leading bold phrase',
    path: 'heart-and-soul/vision.md',
    classes: ['principle'],
    text: VISION.replace('2. **Cite or stay quiet**', '2. Cite or stay quiet'),
    reason: 'ambiguous-leading-label',
    class: 'principle',
    line: 29,
  },
  {
    name: 'two principles with the same bold phrase',
    path: 'heart-and-soul/vision.md',
    classes: ['principle'],
    text: VISION.replace('**Cite or stay quiet**', '**Fail closed**'),
    reason: 'duplicate-key',
    class: 'principle',
    detail: 'Fail closed',
  },
  {
    name: 'a rules section with no list',
    path: 'heart-and-soul/vision.md',
    classes: ['principle'],
    text: VISION.replace(/## Non-Negotiable Rules[\s\S]*?## Appendix/, '## Non-Negotiable Rules\n\nprose only\n\n## Appendix'),
    reason: 'malformed-list',
    class: 'principle',
  },
  {
    name: 'success section with no list items',
    path: 'heart-and-soul/v1.md',
    classes: ['success-criterion'],
    text: V1.replace('1. Ships on time.\n2. Stays honest.\n', ''),
    reason: 'malformed-list',
    class: 'success-criterion',
  },
  {
    name: 'architecture with no H2 at all',
    path: 'heart-and-soul/architecture.md',
    classes: ['project-account-section'],
    text: ARCHITECTURE.replace(/^## /gm, '### '),
    reason: 'missing-heading',
    class: 'project-account-section',
    detail: 'any H2',
  },
  {
    name: 'v1 without the What v1 Defers heading',
    path: 'heart-and-soul/v1.md',
    classes: ['project-account-section'],
    text: V1.replace('## What v1 Defers', '## What v1 defers'),
    reason: 'missing-heading',
    class: 'project-account-section',
    detail: 'What v1 Defers',
  },
  {
    name: 'v1 without the Dashboard catalog heading',
    path: 'heart-and-soul/v1.md',
    classes: ['catalog-entry'],
    text: V1.replace('### Dashboard\n', ''),
    reason: 'missing-heading',
    class: 'catalog-entry',
    detail: 'Dashboard',
  },
  {
    name: 'a catalog entry without a leading bold or code span',
    path: 'heart-and-soul/v1.md',
    classes: ['catalog-entry'],
    text: V1.replace('- **Mail** - mail module', '- Mail - mail module'),
    reason: 'ambiguous-leading-label',
    class: 'catalog-entry',
  },
  {
    name: 'a catalog entry whose label is not followed by a dash',
    path: 'heart-and-soul/v1.md',
    classes: ['catalog-entry'],
    text: V1.replace('- **Mail** - mail module', '- **Mail** mail module'),
    reason: 'ambiguous-leading-label',
    class: 'catalog-entry',
  },
  {
    name: 'a decimal item in a catalog',
    path: 'heart-and-soul/v1.md',
    classes: ['catalog-entry'],
    text: V1.replace('- **Mail** - mail module', '1. **Mail** - mail module'),
    reason: 'malformed-list',
    class: 'catalog-entry',
  },
  {
    name: 'the same catalog key under two headings',
    path: 'heart-and-soul/v1.md',
    classes: ['catalog-entry'],
    text: V1.replace('- **Tracing** - spans', '- **Bus** - spans'),
    reason: 'duplicate-key',
    class: 'catalog-entry',
    detail: 'Bus',
  },
  {
    name: 'lore README without the Index heading',
    path: 'legends-and-lore/README.md',
    classes: ['design-contract'],
    text: LORE_README.replace('## Index', '## Indexes'),
    reason: 'missing-heading',
    class: 'design-contract',
  },
  {
    name: 'lore Index whose first column is not a link',
    path: 'legends-and-lore/README.md',
    classes: ['design-contract'],
    text: LORE_README.replace('| [RFC 0002](0002.md) |', '| RFC 0002 |'),
    reason: 'malformed-row',
    class: 'design-contract',
    line: 8,
  },
  {
    name: 'lore Index row with a missing column',
    path: 'legends-and-lore/README.md',
    classes: ['design-contract'],
    text: LORE_README.replace('| [RFC 0002](0002.md) | candidate |', '| [RFC 0002](0002.md) |'),
    reason: 'malformed-row',
    class: 'design-contract',
    line: 8,
  },
  {
    name: 'lore Index with no table',
    path: 'legends-and-lore/README.md',
    classes: ['design-contract'],
    text: LORE_README.replace(/\| Contract \| Status \|\n\| --- \| --- \|\n(\| \[RFC 000[12]\][^\n]*\n){2}/, 'prose\n'),
    reason: 'malformed-row',
    class: 'design-contract',
  },
  {
    name: 'lore Index whose linked contract repeats',
    path: 'legends-and-lore/README.md',
    classes: ['design-contract'],
    text: LORE_README.replace('[RFC 0002](0002.md)', '[RFC 0001](0002.md)'),
    reason: 'duplicate-key',
    class: 'design-contract',
  },
  {
    name: 'components without any ordinal H2',
    path: 'lay-and-land/components.md',
    classes: ['topology-component'],
    text: COMPONENTS.replace(/^## \d+[a-z]?\.? /gm, '## '),
    reason: 'missing-heading',
    class: 'topology-component',
  },
  {
    name: 'a component row whose first column is not entirely bold',
    path: 'lay-and-land/components.md',
    classes: ['topology-component'],
    text: COMPONENTS.replace('| **Store** |', '| **Store** (legacy) |'),
    reason: 'malformed-row',
    class: 'topology-component',
    line: 14,
  },
  {
    name: 'a component row with a missing column',
    path: 'lay-and-land/components.md',
    classes: ['topology-component'],
    text: COMPONENTS.replace('| **Store** | keeps |', '| **Store** |'),
    reason: 'malformed-row',
    class: 'topology-component',
    line: 14,
    detail: 'column count',
  },
  {
    name: 'the same component label twice under one ordinal',
    path: 'lay-and-land/components.md',
    classes: ['topology-component'],
    text: COMPONENTS.replace('| **Store** |', '| **Daemon** |'),
    reason: 'duplicate-key',
    class: 'topology-component',
    detail: '1:Daemon',
  },
  {
    name: 'craft README without the Reading Order heading',
    path: 'craft-and-care/README.md',
    classes: ['craft-policy'],
    text: CRAFT_README.replace('### Reading Order', '### Reading order'),
    reason: 'missing-heading',
    class: 'craft-policy',
  },
  {
    name: 'craft Reading Order table without a File column',
    path: 'craft-and-care/README.md',
    classes: ['craft-policy'],
    text: CRAFT_README.replace('| Order | File | Why |', '| Order | Path | Why |'),
    reason: 'malformed-row',
    class: 'craft-policy',
    line: 5,
    detail: 'no File column',
  },
  {
    name: 'craft Reading Order row whose File cell is not a link',
    path: 'craft-and-care/README.md',
    classes: ['craft-policy'],
    text: CRAFT_README.replace('[Impact](./cc-impact.md#top)', 'cc-impact.md'),
    reason: 'malformed-row',
    class: 'craft-policy',
    line: 8,
  },
  {
    name: 'craft Reading Order with two links to one basename',
    path: 'craft-and-care/README.md',
    classes: ['craft-policy'],
    text: CRAFT_README.replace('(./cc-impact.md#top)', '(other/cc-spec.md)'),
    reason: 'duplicate-key',
    class: 'craft-policy',
    detail: 'cc-spec.md',
  },
  {
    name: 'roster TOML without a [butler] table',
    path: 'roster/alfred/butler.toml',
    classes: ['roster-identity'],
    text: ROSTER.replace('[butler]', '[staff]'),
    reason: 'malformed-toml',
    class: 'roster-identity',
  },
  {
    name: 'roster TOML with an empty name',
    path: 'roster/alfred/butler.toml',
    classes: ['roster-identity'],
    text: ROSTER.replace('name = "Alfred"', 'name = ""'),
    reason: 'malformed-toml',
    class: 'roster-identity',
    line: 8,
  },
  {
    name: 'roster TOML whose [butler] table has no name',
    path: 'roster/alfred/butler.toml',
    classes: ['roster-identity'],
    text: ROSTER.replace('name = "Alfred"  # trailing', 'title = "Alfred"'),
    reason: 'malformed-toml',
    class: 'roster-identity',
  },
  {
    name: 'roster TOML with the name repeated',
    path: 'roster/alfred/butler.toml',
    classes: ['roster-identity'],
    text: `${ROSTER}name = "Bruce"\n`,
    reason: 'malformed-toml',
    class: 'roster-identity',
  },
  {
    name: 'roster TOML with two [butler] tables',
    path: 'roster/alfred/butler.toml',
    classes: ['roster-identity'],
    text: `${ROSTER}\n[butler]\n`,
    reason: 'malformed-toml',
    class: 'roster-identity',
  },
  {
    name: 'a baseline-spec path with two directories',
    path: 'openspec/specs/a/b/spec.md',
    classes: ['baseline-spec'],
    text: '',
    reason: 'unsupported-source',
    class: 'baseline-spec',
  },
  {
    name: 'a roster path that is not butler.toml',
    path: 'roster/alfred/other.toml',
    classes: ['roster-identity'],
    text: ROSTER,
    reason: 'unsupported-source',
    class: 'roster-identity',
  },
  {
    name: 'a class the grammar names for another file',
    path: 'heart-and-soul/architecture.md',
    classes: ['project-account-section', 'principle'],
    text: ARCHITECTURE,
    reason: 'unsupported-source',
    class: 'principle',
  },
];

describe('PWB-REQ-002 — any grammar failure makes the whole source Unknown', () => {
  for (const m of MALFORMED) {
    it(`${m.name} → ${m.reason}`, () => {
      const r = extractSource({ path: m.path, extractionClasses: m.classes }, m.text);
      expect(r.kind).toBe('unknown');
      if (r.kind !== 'unknown') return;
      expect(r.path).toBe(m.path);
      expect(r.classes).toEqual(m.classes);
      expect(r.failure.reason).toBe(m.reason);
      expect(r.failure.class).toBe(m.class);
      if (m.line !== undefined) expect(r.failure.line).toBe(m.line);
      if (m.detail !== undefined) expect(r.failure.detail).toBe(m.detail);
      // No partial set: nothing item-shaped survives on the Unknown arm.
      expect('items' in r).toBe(false);
      expect('denominators' in r).toBe(false);
      expect(EXTRACTION_FAILURES).toContain(r.failure.reason);
    });
  }

  it('a failing class withholds the items of the classes that succeeded', () => {
    // principle fails; project-account-section and success-criterion would succeed alone.
    const text = VISION.replace('2. **Cite or stay quiet**', '2. Cite or stay quiet');
    expect(extractClass('project-account-section', 'heart-and-soul/vision.md', text).kind).toBe('items');
    expect(extractClass('success-criterion', 'heart-and-soul/vision.md', text).kind).toBe('items');
    const r = extractSource({ path: 'heart-and-soul/vision.md', extractionClasses: ['project-account-section', 'principle', 'success-criterion'] }, text);
    expect(r.kind).toBe('unknown');
  });

  it('the fixture set exercises every closed failure reason', () => {
    const seen = new Set(MALFORMED.map((m) => m.reason));
    for (const reason of EXTRACTION_FAILURES) expect(seen.has(reason)).toBe(true);
  });

  it('a source with no extraction classes extracts nothing and is not Unknown', () => {
    expect(extractSource({ path: 'README.md', extractionClasses: [] }, '# root\n')).toEqual({
      kind: 'extracted',
      path: 'README.md',
      classes: [],
      items: [],
      denominators: {},
    });
  });
});

// ---------------------------------------------------------------------
// Literalness: exact headings, exact levels, exact depth, NFC only.

describe('PWB-REQ-002 — the grammar is literal', () => {
  const vision = (text: string): SourceExtraction => extractSource({ path: 'heart-and-soul/vision.md', extractionClasses: ['principle', 'success-criterion'] }, text);

  it('heading matches are exact: no case folding, no trailing punctuation rewriting', () => {
    expect(vision(VISION.replace('## Non-Negotiable Rules', '## non-negotiable rules')).kind).toBe('unknown');
    expect(vision(VISION.replace('## Non-Negotiable Rules', '## Non-Negotiable Rules:')).kind).toBe('unknown');
    // Trailing closing hashes and surrounding whitespace are ATX syntax, not text.
    expect(vision(VISION.replace('## Non-Negotiable Rules', '##   Non-Negotiable Rules ##')).kind).toBe('extracted');
  });

  it('keys are NFC-normalized and nothing else', () => {
    const r = extracted(FIXTURES[0] as Fixture);
    const keys = keysOf(r, 'principle');
    expect(keys[2]).toBe('Caf\u00e9 rule');
    expect((keys[2] as string).length).toBe(9);
    expect(VISION).toContain('Cafe\u0301 rule');
    expect(keys).not.toContain('fail closed');
  });

  it('fenced code never mints headings or items', () => {
    const r = extracted(FIXTURES[0] as Fixture);
    expect(keysOf(r, 'principle')).not.toContain('Fenced rule');
    expect(r.items.some((i) => i.statement?.includes('Not A Heading') && i.key !== 'purpose')).toBe(false);
  });

  it('only top-level list items mint; nested and indented lines do not', () => {
    const r = extracted(FIXTURES[0] as Fixture);
    expect(r.denominators['success-criterion']).toBe(3);
    const withNested = VISION.replace('  - a nested bullet mints nothing', '  - a nested bullet mints nothing\n    - deeper still\n\t- tab-indented');
    const n = vision(withNested);
    expect(n.kind).toBe('extracted');
    if (n.kind === 'extracted') expect(n.denominators['success-criterion']).toBe(3);
  });

  it('inline heading-like text in a paragraph is not a heading', () => {
    const r = extractSource({ path: 'heart-and-soul/vision.md', extractionClasses: ['project-account-section'] }, VISION);
    expect(r.kind).toBe('extracted');
    if (r.kind === 'extracted') expect((r.items.find((i) => i.key === 'purpose') as ExtractedItem).line).toBe(5);
  });

  it('CRLF line endings parse the same as LF', () => {
    const lf = extracted(FIXTURES[2] as Fixture);
    const crlf = extractSource({ path: 'heart-and-soul/v1.md', extractionClasses: (FIXTURES[2] as Fixture).classes }, V1.replace(/\n/g, '\r\n'));
    expect(crlf.kind).toBe('extracted');
    if (crlf.kind === 'extracted') {
      expect(crlf.items.map((i) => [i.class, i.key, i.line])).toEqual(lf.items.map((i) => [i.class, i.key, i.line]));
    }
  });

  it('table cells honour escaped pipes and the delimiter row is required', () => {
    const escaped = LORE_README.replace('| [RFC 0002](0002.md) | candidate |', '| [RFC 0002](0002.md) | a \\| b |');
    const r = extractSource({ path: 'legends-and-lore/README.md', extractionClasses: ['design-contract'] }, escaped);
    expect(r.kind).toBe('extracted');
    const noDelimiter = LORE_README.replace('| --- | --- |\n', '');
    expect(extractSource({ path: 'legends-and-lore/README.md', extractionClasses: ['design-contract'] }, noDelimiter).kind).toBe('unknown');
  });

  it('the class vocabulary dispatch covers exactly the manifest classes', () => {
    for (const cls of EXTRACTION_CLASSES) {
      const r = extractClass(cls, 'nowhere/else.txt', '');
      expect(r.kind).toBe('failed');
      if (r.kind === 'failed') expect(r.failure.class).toBe(cls);
    }
    expect(extractClass('not-a-class' as ExtractionClass, 'x', '').kind).toBe('failed');
  });
});

// ---------------------------------------------------------------------
// Extraction charges one registry pass per class (registry amendment
// 2026-09-05: `project-account-extraction`, `declared-item-extraction`;
// PWB-REQ-006 as amended).

describe('PWB-REQ-006 (amended) — extraction charges one registry pass per class', () => {
  const source = { path: 'heart-and-soul/vision.md', extractionClasses: ['project-account-section', 'principle', 'success-criterion'] as const };

  it('charges project-account-extraction for the account section and declared-item-extraction for every item class, in class order', () => {
    const charged: ParsePassIdentity[] = [];
    const r = extractSource(source, VISION, (pass) => {
      charged.push(pass);
    });
    expect(r.kind).toBe('extracted');
    expect(charged).toEqual(['project-account-extraction', 'declared-item-extraction', 'declared-item-extraction']);
  });

  it('a spent budget yields over-limit naming the class whose traversal never ran, with no partial items', () => {
    const breach = { limit: 'maxParsePassesPerSource' as const, declared: 5, observed: 6, path: source.path };
    let calls = 0;
    const r = extractSource(source, VISION, (pass) => {
      calls += 1;
      if (calls === 2) throw new ParsePassBudgetExceeded(breach, pass);
    });
    expect(r).toEqual({ kind: 'over-limit', path: source.path, classes: [...source.extractionClasses], class: 'principle', breach });
    expect('items' in r).toBe(false);
    expect(calls).toBe(2);
  });

  it('an unregistered traversal is not caught: the forbidden call propagates', () => {
    expect(() =>
      extractSource(source, VISION, () => {
        throw new Error('unregistered parse pass');
      }),
    ).toThrow('unregistered parse pass');
  });

  it('with no charge the extraction is unchanged', () => {
    expect(extractSource(source, VISION)).toEqual(extractSource(source, VISION, () => undefined));
  });
});
