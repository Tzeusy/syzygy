import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { DISCOVERY_STAGE_ILLUSTRATIONS, DOSSIER_ILLUSTRATION_SOURCES, DOSSIER_STAGE_ILLUSTRATIONS, promptForStage, type GenerationStage, type PromptProfile } from './prompts.js';
import { validateStage, type ProviderDraft, type ProviderInventory } from './provider-draft.js';
import { validateDossierStage } from './dossier-validation.js';
import { QUOTATION_LEAD, quotationsMatch } from './quotations.js';

const sha256 = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');

// Recipe replay, as in prompts.test.ts: an intentional edit needs a version
// decision and a new reviewed digest. These pin bytes; they are not LLM evals.
const recipes: [GenerationStage, string, string][] = [
  ['inventory', 'polaris-inventory-dossier-v2', '4f7545be152d6e0ff400c6f01a6c98b80545926069564019e700f3b584cb4fde'],
  ['plan', 'polaris-plan-dossier-v2', 'af42468b33f9369ac5c0b5e9b99cfe244573f7bb8b122f9363c8ff2b01dc9cc2'],
  ['author', 'polaris-author-dossier-v2', '9d06cdb7fbc421e0b242bdb1cd2c50dd035c160fe2db5dce691d739c50b0e7c0'],
  ['edit', 'polaris-edit-dossier-v2', '4ca9b8e146605785b4221b815130c016070e8ae43902e36be2bf06210bf59bdf'],
  ['fidelity', 'polaris-fidelity-dossier-v2', 'cf287a42fa24e14d29f8913dcfb51a939d8bb0481bc36df691547c0710520322'],
  ['repair', 'polaris-repair-dossier-v2', 'a751d6cedb1549151f59c47cdff18bc204c011d515c6cf5b53ebf02c0aa85d52'],
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

  // The dossier base is the reviewed manifesto prompt with exactly these
  // manifesto-only phrases replaced; every other byte is unchanged.
  const substitutions: [string, string][] = [
    ['You are producing one stage of a project-neutral Polaris manifesto pipeline.', 'You are producing one stage of a project-neutral Polaris dossier pipeline.'],
    [' Generated content is editorial draft, not adopted intent.', ' Generated content is an editorial draft.'],
  ];
  const stageSubstitutions: Partial<Record<GenerationStage, [string, string]>> = {
    inventory: ['Do not draft or plan the manifesto,', 'Do not draft or plan the dossier,'],
    author: ['Write a coherent, concise manifesto following', 'Write a coherent, concise dossier following'],
    fidelity: [", accept the author's self-assessment as evidence, or grant owner approval.", " or accept the author's self-assessment as evidence."],
  };

  it.each(recipes)('derives the %s dossier base from the reviewed manifesto prompt by named substitutions only', (stage) => {
    let base = promptForStage(stage).system;
    for (const [from, to] of [...substitutions, ...(stageSubstitutions[stage] === undefined ? [] : [stageSubstitutions[stage]!])]) {
      expect(base.split(from).length, from).toBe(2);
      base = base.replace(from, () => to);
    }
    const prompt = promptForStage(stage, 'dossier').system;
    expect(prompt.startsWith(`${base}\n\n`)).toBe(true);
    for (const phrase of ['manifesto', 'adopted intent', 'owner approval']) expect(prompt, phrase).not.toContain(phrase);
  });

  it.each(recipes)('ends the %s prompt with the illustration it was tested with', (stage) => {
    const lines = promptForStage(stage, 'dossier').system.split('\n');
    expect(lines.at(-2)).toMatch(/^Shape illustration for a fictional project\. Copy its structure, never its content/u);
    expect(JSON.parse(lines.at(-1)!)).toEqual(illustration(stage));
  });

  it.each(recipes)('states the seven dossier rules in the %s prompt', (stage) => {
    const prompt = promptForStage(stage, 'dossier').system;
    for (const rule of ['1. Claim ledger.', '2. Workflow traces.', '3. Mechanisms.', '4. Stated advantages and trade-offs.', '5. Comparisons.', '6. Marked inference.', '7. Thin evidence stays Unknown.']) {
      expect(prompt).toContain(`\n${rule} `);
    }
    expect(prompt).toContain(' Where these dossier rules and the instructions above differ, the dossier rules govern. ');
    // The asset id maintainer-stated-advantages is the profile's; only the illustration line carries it.
    expect(prompt.split('\n').slice(0, -1).join('\n')).not.toContain('maintainer');
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
    expect(validateDossierStage(stage, illustration(stage), context())).toEqual(illustration(stage));
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

describe('the embedded illustrations are fixed at module load', () => {
  const before = recipes.map(([stage]) => promptForStage(stage, 'dossier').system);
  const discoveryBefore = (['discovery-map', 'discovery-reduce'] as const).map(stage => promptForStage(stage).system);

  it('deep-freezes every exported illustration and source', () => {
    const frozen = (value: unknown): boolean => value === null || typeof value !== 'object'
      || (Object.isFrozen(value) && Object.values(value).every(frozen));
    expect(frozen(DOSSIER_STAGE_ILLUSTRATIONS)).toBe(true);
    expect(frozen(DOSSIER_ILLUSTRATION_SOURCES)).toBe(true);
    expect(frozen(DISCOVERY_STAGE_ILLUSTRATIONS)).toBe(true);
  });

  it('refuses every mutation an importer could attempt, and the prompts stay byte-identical', () => {
    const attempts: (() => void)[] = [
      () => { (DOSSIER_STAGE_ILLUSTRATIONS as Record<string, unknown>).author = {}; },
      () => { ((DOSSIER_STAGE_ILLUSTRATIONS.author as ProviderDraft).introduction as { text: string }).text = 'changed'; },
      () => { ((DOSSIER_STAGE_ILLUSTRATIONS.inventory as ProviderInventory).entries as unknown[]).push({}); },
      () => { (DOSSIER_ILLUSTRATION_SOURCES[0] as { text: string }).text = 'changed'; },
      () => { (DISCOVERY_STAGE_ILLUSTRATIONS as Record<string, unknown>)['discovery-map'] = {}; },
      () => { ((DISCOVERY_STAGE_ILLUSTRATIONS['discovery-map'] as { claims: { claim: string }[] }).claims[0]!).claim = 'changed'; },
    ];
    for (const attempt of attempts) expect(attempt).toThrow(TypeError);
    expect(recipes.map(([stage]) => promptForStage(stage, 'dossier').system)).toEqual(before);
    expect((['discovery-map', 'discovery-reduce'] as const).map(stage => promptForStage(stage).system)).toEqual(discoveryBefore);
  });

  it('keeps the illustrations out of the package entry point', async () => {
    const entry = await import('./index.js') as Record<string, unknown>;
    for (const name of ['DOSSIER_STAGE_ILLUSTRATIONS', 'DOSSIER_ILLUSTRATION_SOURCES', 'DISCOVERY_STAGE_ILLUSTRATIONS']) expect(entry[name], name).toBeUndefined();
    expect(entry.promptForStage).toBe(promptForStage);
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

  // Rule 4: "The project states:" then one or two sentences in double quotes, matching a cited source.
  const quoted = (claim: { text: string; sourceIds: readonly string[] }): void => {
    expect(claim.text.startsWith(QUOTATION_LEAD), claim.text).toBe(true);
    expect(quotationsMatch(claim.text, claim.sourceIds.map(sourceText)), claim.text).toBe(true);
  };

  it('quotes every advantage and trade-off verbatim from a cited source', () => {
    for (const id of ['maintainer-stated-advantages', 'trade-offs']) {
      const section = draft.sections.find(candidate => candidate.id === id)!;
      const stated = section.paragraphs.filter(block => !block.text.startsWith('Inferred: '));
      expect(stated.length).toBe(1);
      for (const block of stated) quoted(block);
    }
    const inventory = illustration('inventory') as ProviderInventory;
    const stated = inventory.entries.filter(entry => ['other', 'qualification'].includes(entry.kind) && !entry.statement.startsWith('Inferred: '));
    expect(stated.length).toBe(2);
    for (const entry of stated) quoted({ text: entry.statement, sourceIds: entry.sourceIds });
  });

  it('marks the two inferential blocks Inferred: and no other', () => {
    const inferred = blocks.filter(block => block.text.startsWith('Inferred: '));
    expect(inferred.map(block => block.id)).toEqual(['b-cost-inferred', 'b-dive']);
    expect(blocks.filter(block => block.text.includes('Inferred'))).toEqual(inferred);
  });

  it('gives an unstated mechanism-level cost its own Inferred: block, citing the mechanism and never quoting', () => {
    const [stated, inferred] = draft.sections.find(candidate => candidate.id === 'trade-offs')!.paragraphs;
    expect(stated!.text.startsWith(QUOTATION_LEAD)).toBe(true);
    expect(inferred!.text.startsWith('Inferred: ')).toBe(true);
    expect(inferred!.text).not.toContain(QUOTATION_LEAD);
    expect(inferred!.sourceIds).toEqual(['src-cache']);
    const inventory = illustration('inventory') as ProviderInventory;
    const entries = inventory.entries.filter(entry => entry.statement.startsWith('Inferred: '));
    expect(entries.map(entry => [entry.id, entry.kind, entry.sourceIds])).toEqual([['e-cost-inferred', 'qualification', ['src-cache']]]);
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
});
