import { describe, expect, it } from 'vitest';
import { renderedDesignSubjectDigest, renderedDesignVerdict } from './rendered-design.js';

// Fixtures are plain constants; expected values are hard-coded literals.
const node = (id: string, label: string) => ({ id, label, sourceIds: ['s1'], epistemic: 'observed' });
const figure = (id: string, disposition: Record<string, unknown>) => ({
  id, title: `Figure ${id}`, sectionId: 'section', kind: 'dependency', relationship: `Relationship drawn by ${id}`,
  nodes: [node(`${id}-a`, 'Store'), node(`${id}-b`, 'Reader')],
  edges: [{ id: `${id}-e`, from: `${id}-a`, to: `${id}-b`, label: 'Feeds', sourceIds: ['s1'], epistemic: 'observed' }],
  disposition,
});
const draft = {
  title: 'A manifesto',
  introduction: { id: 'intro', text: 'Why it exists.', sourceIds: ['s1'] },
  sections: [{ id: 'section', title: 'How it works', paragraphs: [{ id: 'body', text: 'The store feeds the reader.', sourceIds: ['s1'], children: [] }], disposition: { kind: 'produced', assetIds: ['section'] } }],
  diagrams: [
    figure('deps', { kind: 'produced', assetIds: ['deps'] }),
    figure('extra', { kind: 'produced', assetIds: ['extra'] }),
    figure('skipped', { kind: 'omitted', reason: 'Premises name the parts but not how they connect.', references: ['s1'] }),
    figure('pending', { kind: 'unresolved', reason: 'Renderer unavailable.', references: ['s1'] }),
  ],
  deepDives: [],
  unresolved: [],
};
// Canonical-JSON sha256 of `draft`, computed once outside this module (Python
// json.dumps(sort_keys=True, separators=(',', ':'))) and pinned here.
const DRAFT_DIGEST = 'ddefc70c06cb732f49e657d1299a8ee44cf8e6d1f34ba349c28f42f6d1816da4';

type Rel = Record<string, unknown>;
const rel = (id: string, fields: Rel = {}): Rel => ({
  id, description: `Dependency ${id} among the store, reader and writer`, sourceIds: ['s1'],
  judgment: 'diagram-clearer', support: 'supported', diagram: { kind: 'named', diagramId: 'deps' }, gaps: [], ...fields,
});
const review = (relationships: Rel[], extra: Rel = {}) => ({ draftDigest: DRAFT_DIGEST, relationships, findings: [], ...extra });
const rules = (value: unknown) => renderedDesignVerdict(value, draft).findings.map(f => [f.relationshipId, f.rule]);

describe('rendered-design review verdict (REQ-polaris-generation-004/006)', () => {
  it('binds the review to the exact draft bytes by canonical digest', () => {
    expect(renderedDesignSubjectDigest(draft)).toBe(DRAFT_DIGEST);
  });

  it('a supported, diagram-clearer relationship with its named produced diagram does not block', () => {
    expect(renderedDesignVerdict(review([rel('r1')]), draft)).toEqual({
      blocking: false, retired: false, findings: [], reviewerFindings: [], enumeration: [rel('r1')],
    });
  });

  it('a prose-sufficient relationship needs no diagram', () => {
    const verdict = renderedDesignVerdict(review([rel('r1', { judgment: 'prose-sufficient', diagram: { kind: 'none' } })]), draft);
    expect(verdict.blocking).toBe(false);
    expect(verdict.findings).toEqual([]);
  });

  it('a diagram-clearer supported relationship with no diagram blocks and retains its enumeration', () => {
    const enumerated = rel('r-new', { diagram: { kind: 'none' } });
    const verdict = renderedDesignVerdict(review([enumerated]), draft);
    expect(verdict.blocking).toBe(true);
    expect(verdict.findings).toEqual([{ rule: 'missing-diagram', relationshipId: 'r-new', enumeration: enumerated }]);
    expect(verdict.enumeration).toEqual([enumerated]);
  });

  it('the finding stands even though no draft diagram ever proposed the relationship', () => {
    // No draft diagram's `relationship` text mentions r-new; the reviewer's enumeration alone raises it.
    expect(rules(review([rel('r-new', { diagram: { kind: 'named', diagramId: 'never-drawn' } })]))).toEqual([['r-new', 'missing-diagram']]);
  });

  it('unrelated extra figures cannot stand in: many produced diagrams, none named, still blocks', () => {
    expect(draft.diagrams.filter(d => d.disposition.kind === 'produced').length).toBe(2);
    expect(rules(review([rel('r1', { diagram: { kind: 'none' } })]))).toEqual([['r1', 'missing-diagram']]);
  });

  it('a diagram named by another diagram-clearer relationship satisfies neither', () => {
    expect(rules(review([rel('r1'), rel('r2')]))).toEqual([
      ['r1', 'diagram-claimed-by-another-relationship'],
      ['r2', 'diagram-claimed-by-another-relationship'],
    ]);
    expect(rules(review([rel('r1'), rel('r2', { diagram: { kind: 'named', diagramId: 'extra' } })]))).toEqual([]);
    const omitted = { support: 'unsupported', diagram: { kind: 'named', diagramId: 'skipped' } };
    expect(rules(review([rel('u1', omitted), rel('u2', omitted)]))).toEqual([
      ['u1', 'diagram-claimed-by-another-relationship'],
      ['u2', 'diagram-claimed-by-another-relationship'],
    ]);
  });

  it('a named diagram that is not produced blocks a supported relationship', () => {
    expect(rules(review([rel('r1', { diagram: { kind: 'named', diagramId: 'pending' } })]))).toEqual([['r1', 'diagram-not-produced']]);
  });

  it('an undrawable relationship takes a recorded omission instead', () => {
    const undrawable = { support: 'unsupported', diagram: { kind: 'named', diagramId: 'skipped' } };
    expect(renderedDesignVerdict(review([rel('r1', undrawable)]), draft).blocking).toBe(false);
    expect(rules(review([rel('r1', { support: 'unsupported', diagram: { kind: 'none' } })]))).toEqual([['r1', 'undrawable-without-recorded-omission']]);
    expect(rules(review([rel('r1', { support: 'unsupported', diagram: { kind: 'named', diagramId: 'pending' } })]))).toEqual([['r1', 'undrawable-without-recorded-omission']]);
  });

  it('an unsupported relationship is never drawn', () => {
    expect(rules(review([rel('r1', { support: 'unsupported' })]))).toEqual([['r1', 'unsupported-relationship-drawn']]);
  });

  it('a partly supported diagram blocks unless its gap is recorded', () => {
    expect(rules(review([rel('r1', { support: 'partly-supported' })]))).toEqual([['r1', 'undisclosed-gap']]);
    const disclosed = rel('r1', { support: 'partly-supported', gaps: [{ element: 'Writer', reason: 'No premise names the writer.' }] });
    expect(renderedDesignVerdict(review([disclosed]), draft).blocking).toBe(false);
  });

  it('a prose-sufficient relationship drawn in a produced figure still obeys the drawing rules', () => {
    const prose = (fields: Rel) => rel('p1', { judgment: 'prose-sufficient', ...fields });
    expect(rules(review([prose({ support: 'unsupported' })]))).toEqual([['p1', 'unsupported-relationship-drawn']]);
    expect(rules(review([rel('r1'), prose({ support: 'unsupported' })]))).toEqual([['p1', 'unsupported-relationship-drawn']]);
    expect(rules(review([prose({ support: 'partly-supported' })]))).toEqual([['p1', 'undisclosed-gap']]);
    expect(rules(review([prose({ support: 'partly-supported', gaps: [{ element: 'Writer', reason: 'No premise names it.' }] })]))).toEqual([]);
    expect(rules(review([prose({ support: 'unsupported', diagram: { kind: 'named', diagramId: 'skipped' } })]))).toEqual([]);
  });

  it('a prose-sufficient claim on a figure does not make it shared with the diagram-clearer relationship it draws', () => {
    expect(rules(review([rel('r1'), rel('p1', { judgment: 'prose-sufficient' })]))).toEqual([]);
  });

  it('an explicit empty enumeration is a valid record that blocks nothing by itself', () => {
    expect(renderedDesignVerdict(review([]), draft)).toEqual({ blocking: false, retired: false, findings: [], reviewerFindings: [], enumeration: [] });
  });

  it('a missing or malformed record fails closed', () => {
    expect(() => renderedDesignVerdict(undefined, draft)).toThrow('invalid-structure');
    expect(() => renderedDesignVerdict(null, draft)).toThrow('invalid-structure');
    expect(() => renderedDesignVerdict({ draftDigest: DRAFT_DIGEST, findings: [] }, draft)).toThrow('invalid-fields');
    expect(() => renderedDesignVerdict(review([rel('r1', { judgment: 'obvious' })]), draft)).toThrow('invalid-string');
    expect(() => renderedDesignVerdict(review([rel('r1', { diagram: null })]), draft)).toThrow('invalid-disposition');
    expect(() => renderedDesignVerdict(review([rel('r1', { blocking: false })]), draft)).toThrow('invalid-fields');
    expect(() => renderedDesignVerdict(review([rel('r1')]), undefined)).toThrow('invalid-structure');
  });

  it('duplicate relationship ids are invalid', () => {
    expect(() => renderedDesignVerdict(review([rel('r1'), rel('r1', { judgment: 'prose-sufficient' })]), draft)).toThrow('duplicate-handle');
  });

  it('a gap outside a partly supported relationship is invalid', () => {
    expect(() => renderedDesignVerdict(review([rel('r1', { gaps: [{ element: 'Writer', reason: 'Absent.' }] })]), draft)).toThrow('gap-without-partial-support');
  });

  it('a review bound to other draft bytes is retired and blocks', () => {
    const revised = { ...draft, title: 'A revised manifesto' };
    const verdict = renderedDesignVerdict(review([rel('r1')]), revised);
    expect(verdict.retired).toBe(true);
    expect(verdict.blocking).toBe(true);
  });

  it('reviewer blocking findings add to the verdict; advisory ones do not; targets must exist', () => {
    const advisory = { severity: 'advisory', message: 'Legend could be larger.', target: 'deps' };
    const blocking = { severity: 'blocking', message: 'Hierarchy buries the thesis.', target: 'section' };
    expect(renderedDesignVerdict(review([], { findings: [advisory] }), draft).blocking).toBe(false);
    expect(renderedDesignVerdict(review([], { findings: [blocking] }), draft).blocking).toBe(true);
    expect(() => renderedDesignVerdict(review([], { findings: [{ ...advisory, target: 'nowhere' }] }), draft)).toThrow('unknown-finding-target');
  });
});
