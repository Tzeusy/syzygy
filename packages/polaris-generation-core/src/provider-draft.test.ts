import { describe, expect, it } from 'vitest';
import { stageSchema, validateStage, reviewVerdict } from './provider-draft.js';

const sources = [{ sourceId: 's1', text: 'Purpose and architecture' }, { sourceId: 's2', text: 'A material qualification' }];
const inventory = { entries: [
  { id: 'i1', sourceIds: ['s1'], statement: 'Purpose', kind: 'purpose' },
  { id: 'i2', sourceIds: ['s2'], statement: 'Qualification', kind: 'qualification' },
] };
const plan = { sections: [{ id: 'section', title: 'How it works', reason: 'Explain relationships', sourceIds: ['s1', 's2'] }] };
const paragraph = (id: string) => ({ id, text: 'Supported explanation', sourceIds: ['s1'] });
const draft = { title: 'A manifesto', introduction: paragraph('intro'),
  sections: [{ id: 'section', title: 'How it works', paragraphs: [paragraph('body')] }],
  diagrams: [{ id: 'diagram', title: 'Architecture', sectionId: 'section', nodes: [
    { id: 'n1', label: 'Input', sourceIds: ['s1'] }, { id: 'n2', label: 'Output', sourceIds: ['s1'] },
  ], edges: [{ id: 'e1', from: 'n1', to: 'n2', label: 'Supplies', sourceIds: ['s1'] }] }],
  deepDives: [{ id: 'detail', title: 'Why this choice?', sectionId: 'section', paragraphs: [paragraph('detail-body')] }],
};
const review = { inventoryIds: ['i1', 'i2'], blockIds: ['intro', 'body', 'n1', 'n2', 'e1', 'detail-body'], findings: [] };
const context = { sources, inventory, plan, draft };

describe('provider-local intermediate validation', () => {
  it('accepts the complete staged path with serializable isolated schemas and outputs', () => {
    for (const [stage, value] of [['inventory', inventory], ['plan', plan], ['author', draft], ['edit', draft], ['repair', draft], ['fidelity', review]] as const) {
      expect(validateStage(stage, value, context)).toEqual(value);
      expect(validateStage(stage, value, context)).not.toBe(value);
      expect(JSON.parse(JSON.stringify(stageSchema(stage)))).toEqual(stageSchema(stage));
    }
    const schema = stageSchema('author');
    schema.schema = stageSchema('inventory').schema;
    expect(stageSchema('author')).not.toEqual(schema);
  });

  it('refuses missing admitted sources, unknown support and duplicate local identities', () => {
    expect(() => validateStage('inventory', { entries: inventory.entries.slice(0, 1) }, context)).toThrow('incomplete-coverage');
    expect(() => validateStage('inventory', { entries: [...inventory.entries, inventory.entries[0]] }, context)).toThrow('duplicate-handle');
    expect(() => validateStage('author', { ...draft, introduction: { ...draft.introduction, sourceIds: ['unknown'] } }, context)).toThrow('unknown-source');
  });

  it('refuses dangling diagram endpoints, deep-dive parents and duplicate draft handles', () => {
    const bad = structuredClone(draft);
    bad.diagrams[0]!.edges[0]!.to = 'missing';
    expect(() => validateStage('author', bad, context)).toThrow('unknown-node');
    bad.diagrams[0]!.edges[0]!.to = 'n2';
    bad.deepDives[0]!.sectionId = 'missing';
    expect(() => validateStage('author', bad, context)).toThrow('unknown-section');
    bad.deepDives[0]!.sectionId = 'section';
    bad.introduction.id = 'n1';
    expect(() => validateStage('author', bad, context)).toThrow('duplicate-handle');
  });

  it('requires declared review coverage of inventory and every claim-bearing block', () => {
    expect(() => validateStage('fidelity', { ...review, inventoryIds: ['i1'] }, context)).toThrow('incomplete-coverage');
    for (const omitted of review.blockIds) {
      expect(() => validateStage('fidelity', { ...review, blockIds: review.blockIds.filter(id => id !== omitted) }, context)).toThrow('incomplete-coverage');
    }
    expect(() => validateStage('fidelity', { ...review, findings: [{ severity: 'blocking', message: 'Bad', target: 'missing' }] }, context)).toThrow('unknown-finding-target');
    expect(reviewVerdict({ ...review, findings: [{ severity: 'blocking', message: 'Lost qualification', target: 'i2' }] }).blocking).toBe(true);
    expect(reviewVerdict(review).blocking).toBe(false); // Declared coverage, not semantic proof.
  });

  it.each(['<script>alert(1)</script>', 'https://outside.test', 'x < y > z'])('preserves inert text for escaped rendering', title => {
    expect(validateStage('author', { ...draft, title }, context)).toEqual({ ...draft, title });
  });

  it('rejects extras, accessors and sparse arrays without executing hooks', () => {
    expect(() => validateStage('author', { ...draft, approved: true }, context)).toThrow('invalid-fields');
    let called = false;
    const bad = { ...draft };
    Object.defineProperty(bad, 'title', { get() { called = true; return 'bad'; }, enumerable: true });
    expect(() => validateStage('author', bad, context)).toThrow('invalid-property');
    expect(called).toBe(false);
    expect(() => validateStage('inventory', { entries: new Array(2) }, context)).toThrow('invalid-array');
  });
});
