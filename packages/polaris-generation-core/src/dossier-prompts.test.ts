import { createHash } from 'node:crypto';
import { describe, expect, it, vi } from 'vitest';
import { DISCOVERY_STAGE_ILLUSTRATIONS, DOSSIER_ILLUSTRATION_SOURCES, DOSSIER_STAGE_ILLUSTRATIONS, promptForStage, type GenerationStage, type PromptProfile } from './prompts.js';
import { validateStage, type ProviderDraft, type ProviderInventory } from './provider-draft.js';

const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

// Recipe replay, as in prompts.test.ts: an intentional edit needs a version
// decision and a new reviewed digest. These pin bytes; they are not LLM evals.
const recipes: [GenerationStage, string, string][] = [
  ['inventory', 'polaris-inventory-dossier-v1', 'c6a6be9c532812261542a65102c80a5da6d17cbaacbd492fa50d84f25e79c184'],
  ['plan', 'polaris-plan-dossier-v1', '244f333d0d185572000a208479de416d851152b05c5ebb54e1d43cbae774f055'],
  ['author', 'polaris-author-dossier-v1', '5234763e7ac7f8a957f632391b59d4baeb11c04dc315d10673f3f8bdd8e09ad4'],
  ['edit', 'polaris-edit-dossier-v1', '241cecfd0a88db18eeb0da68a63ca78d0b3b5ba3a006c6bddbf99853f3cba57b'],
  ['fidelity', 'polaris-fidelity-dossier-v1', '3b2d01b54e1d22256ca4a49e2ed932cc4878be8eb9c406a908c4660ade2e2ec9'],
  ['repair', 'polaris-repair-dossier-v1', '53d35431424e19925d4be9d93624753f53545d83ec3de63369ad3458e6e3a67c'],
];

// The dossier profile's requested assets (dossier-profile.ts on the profile
// branch), written out here so the illustrations are checked against literals.
const requestedAssets = [
  { id: 'core-ideas', kind: 'section', required: true },
  { id: 'end-to-end-workflows', kind: 'section', required: true },
  { id: 'mechanisms', kind: 'section', required: true },
  { id: 'maintainer-stated-advantages', kind: 'section', required: true },
  { id: 'trade-offs', kind: 'section', required: true },
  { id: 'workflow-diagram', kind: 'diagram', required: false },
  { id: 'mechanism-deep-dive', kind: 'deep-dive', required: false },
];
const sources = DOSSIER_ILLUSTRATION_SOURCES.map(source => ({ ...source }));
const illustration = (stage: GenerationStage): unknown => structuredClone(DOSSIER_STAGE_ILLUSTRATIONS[stage]);
// One context serves every stage: each validator reads only what it needs.
const context = (): Record<string, unknown> => ({ sources, requestedAssets, inventory: illustration('inventory'), plan: illustration('plan'), draft: illustration('author') });
const sourceText = (id: string): string => sources.find(source => source.sourceId === id)!.text;

describe('dossier stage prompts', () => {
  it.each(recipes)('pins the %s dossier prompt bytes', (stage, version, digest) => {
    const prompt = promptForStage(stage, 'dossier');
    expect(prompt.version).toBe(version);
    expect(sha256(prompt.system)).toBe(digest);
    // Base prompt (< 4 KiB) plus rules, guidance and one illustration; a draft
    // illustration is the largest. A prompt past 16 KiB needs a decision.
    expect(Buffer.byteLength(prompt.system, 'utf8')).toBeLessThan(16_384);
  });

  it.each(recipes)('extends the reviewed %s manifesto prompt without changing it', (stage) => {
    const base = promptForStage(stage).system;
    const prompt = promptForStage(stage, 'dossier').system;
    expect(prompt.startsWith(`${base}\n\n`)).toBe(true);
    expect(prompt.length).toBeGreaterThan(base.length + 2);
  });

  it.each(recipes)('ends the %s prompt with the illustration it was tested with', (stage) => {
    const lines = promptForStage(stage, 'dossier').system.split('\n');
    expect(lines.at(-2)).toMatch(/^Shape illustration for a fictional project\. Copy its structure, never its content/u);
    expect(JSON.parse(lines.at(-1)!)).toEqual(illustration(stage));
  });

  it.each(recipes)('states the five dossier rules in the %s prompt', (stage) => {
    const prompt = promptForStage(stage, 'dossier').system;
    for (const rule of ['1. Claim ledger.', '2. Workflow traces.', '3. Mechanisms.', '4. Attribution.', '5. Thin evidence stays Unknown.']) {
      expect(prompt).toContain(`\n${rule} `);
    }
  });

  it('gives every stage its own dossier guidance', () => {
    const heads = recipes.map(([stage]) => promptForStage(stage, 'dossier').system.split('\n').at(-4)!);
    expect(new Set(heads).size).toBe(recipes.length);
    for (const head of heads) expect(head).toMatch(/^Dossier (inventory|plan|draft|edit|review|repair): /u);
  });

  it.each(['unknown', 'Dossier', 'constructor', '__proto__'])('refuses unsupported profile %s', (profile) => {
    expect(() => promptForStage('author', profile as PromptProfile)).toThrow('unknown-prompt-profile');
  });

  it('keeps the manifesto profile the default', () => {
    expect(promptForStage('author', 'manifesto')).toEqual(promptForStage('author'));
  });

  it.each(['unknown', 'constructor', '__proto__'])('refuses unsupported stage %s', (stage) => {
    expect(() => promptForStage(stage as GenerationStage, 'dossier')).toThrow('unknown-generation-stage');
  });
});

describe('dossier stage illustrations pass the stage validators', () => {
  it.each(recipes)('validates the %s illustration', (stage) => {
    expect(validateStage(stage, illustration(stage), context())).toEqual(illustration(stage));
  });

  it('shares one draft illustration across author, edit and repair', () => {
    expect(DOSSIER_STAGE_ILLUSTRATIONS.edit).toBe(DOSSIER_STAGE_ILLUSTRATIONS.author);
    expect(DOSSIER_STAGE_ILLUSTRATIONS.repair).toBe(DOSSIER_STAGE_ILLUSTRATIONS.author);
  });

  it('produces every requested asset in the draft', () => {
    const draft = illustration('author') as ProviderDraft;
    const produced = new Set([...draft.sections, ...draft.diagrams, ...draft.deepDives].filter(asset => asset.disposition.kind === 'produced').map(asset => asset.id));
    expect([...produced].sort()).toEqual(requestedAssets.map(asset => asset.id).sort());
  });
});

describe('dossier illustrations obey their own rules', () => {
  const draft = illustration('author') as ProviderDraft;
  const blocks = [draft.introduction, ...[...draft.sections, ...draft.deepDives].flatMap(owner => owner.paragraphs.flatMap(block => [block, ...block.children]))];

  it('spells every backticked identifier as a cited source spells it', () => {
    const inventory = illustration('inventory') as ProviderInventory;
    const claims = [...blocks.map(block => ({ text: block.text, sourceIds: block.sourceIds })), ...inventory.entries.map(entry => ({ text: entry.statement, sourceIds: entry.sourceIds }))];
    const identifiers = claims.flatMap(claim => [...claim.text.matchAll(/`([^`]+)`/gu)].map(match => ({ name: match[1]!, sourceIds: claim.sourceIds })));
    expect(identifiers.length).toBeGreaterThanOrEqual(8);
    for (const { name, sourceIds } of identifiers) expect(sourceIds.some(id => sourceText(id).includes(name)), name).toBe(true);
  });

  it('attributes every advantage and trade-off to the maintainers', () => {
    for (const id of ['maintainer-stated-advantages', 'trade-offs']) {
      const section = draft.sections.find(candidate => candidate.id === id)!;
      for (const block of section.paragraphs) expect(block.text.startsWith('The maintainers state that ')).toBe(true);
    }
  });

  it('states which half of a trade-off no source states', () => {
    const block = draft.sections.find(candidate => candidate.id === 'trade-offs')!.paragraphs[0]!;
    expect(block.text).toContain('is not stated in the sources');
  });

  it('traces the workflow one hop per child block and draws only those hops', () => {
    const flow = draft.sections.find(candidate => candidate.id === 'end-to-end-workflows')!.paragraphs[0]!;
    expect(flow.children.length).toBe(2);
    const diagram = draft.diagrams[0]!;
    expect(diagram.kind).toBe('flow');
    expect(diagram.sectionId).toBe('end-to-end-workflows');
    for (const element of [...diagram.nodes, ...diagram.edges]) expect(element.sourceIds.every(id => flow.sourceIds.includes(id))).toBe(true);
  });

  it('keeps thin evidence unresolved in the inventory, the draft and the review', () => {
    const inventory = illustration('inventory') as ProviderInventory;
    expect(inventory.entries.filter(entry => entry.disposition.kind === 'unresolved').length).toBe(1);
    expect(draft.unresolved.length).toBe(1);
    const review = illustration('fidelity') as { inventoryCoverage: { disposition: string }[] };
    expect(review.inventoryCoverage.filter(row => row.disposition === 'unresolved').length).toBe(1);
  });
  it('freezes the illustration exports and serializes them once, so no edit can change a prompt under an unchanged version', () => {
    const stages: [GenerationStage | 'discovery-map' | 'discovery-reduce', PromptProfile][] = [['inventory', 'dossier'], ['plan', 'dossier'], ['author', 'dossier'], ['edit', 'dossier'],
      ['fidelity', 'dossier'], ['repair', 'dossier'], ['discovery-map', 'dossier'], ['discovery-reduce', 'dossier']];
    const digests = () => stages.map(([stage, profile]) => { const prompt = promptForStage(stage, profile); return `${prompt.version}:${sha256(prompt.system)}`; });
    const before = digests();
    const edits: (() => void)[] = [
      () => { (DOSSIER_STAGE_ILLUSTRATIONS as Record<string, unknown>).inventory = {}; },
      () => { delete (DOSSIER_STAGE_ILLUSTRATIONS as Record<string, unknown>).plan; },
      () => { ((DOSSIER_STAGE_ILLUSTRATIONS.inventory as { entries: unknown[] }).entries).push({ id: 'injected' }); },
      () => { ((DOSSIER_STAGE_ILLUSTRATIONS.author as { title: string }).title) = 'injected'; },
      () => { ((DOSSIER_STAGE_ILLUSTRATIONS.fidelity as { findings: unknown[] }).findings).length = 0; },
      () => { (DISCOVERY_STAGE_ILLUSTRATIONS as Record<string, unknown>)['discovery-map'] = {}; },
      () => { ((DISCOVERY_STAGE_ILLUSTRATIONS['discovery-reduce'] as { ranked: string[] }).ranked).push('injected'); },
      () => { ((DISCOVERY_STAGE_ILLUSTRATIONS['discovery-map'] as { claims: { claim: string }[] }).claims[0]!.claim) = 'injected'; },
      () => { (DOSSIER_ILLUSTRATION_SOURCES as unknown as { text: string }[])[0]!.text = 'injected'; },
      () => { (DOSSIER_ILLUSTRATION_SOURCES as unknown as unknown[]).push({ sourceId: 'x', text: 'y' }); },
    ];
    const stringify = vi.spyOn(JSON, 'stringify');
    try { digests(); expect(stringify).not.toHaveBeenCalled(); } finally { stringify.mockRestore(); }
    for (const [index, edit] of edits.entries()) expect(edit, `edit ${index}`).toThrow(TypeError);
    expect(digests()).toEqual(before);
    expect(JSON.stringify(DOSSIER_STAGE_ILLUSTRATIONS.inventory)).not.toContain('injected');
    for (const value of [DOSSIER_STAGE_ILLUSTRATIONS, DISCOVERY_STAGE_ILLUSTRATIONS, DOSSIER_ILLUSTRATION_SOURCES, DOSSIER_STAGE_ILLUSTRATIONS.author, DOSSIER_STAGE_ILLUSTRATIONS.fidelity]) {
      expect(Object.isFrozen(value)).toBe(true);
    }
  });
});
