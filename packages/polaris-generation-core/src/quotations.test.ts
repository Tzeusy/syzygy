import { describe, expect, it } from 'vitest';
import { DOSSIER_ILLUSTRATION_SOURCES, DOSSIER_STAGE_ILLUSTRATIONS, type GenerationStage } from './prompts.js';
import { validateDossierStage } from './dossier-validation.js';
import { normalizeQuotation, quotationsMatch } from './quotations.js';
import type { ProviderDraft, ProviderInventory } from './provider-draft.js';

const quote = (text: string): string => `The project states: "${text}"`;

describe('normalizeQuotation', () => {
  it.each([
    ['collapses whitespace runs, line breaks included', 'Pages  render\n\tin\r\nparallel ', 'Pages render in parallel'],
    ['keeps link text and drops the target', 'See [the guide](https://example.test/guide "Guide") first.', 'See the guide first.'],
    ['drops strong emphasis', 'It is **fast** and __small__.', 'It is fast and small.'],
    ['drops emphasis', 'It is *fast* and _small_.', 'It is fast and small.'],
    ['keeps intraword underscores', 'Set max_memory_policy to noeviction.', 'Set max_memory_policy to noeviction.'],
    ['keeps arithmetic asterisks', 'It takes 2*3*4 steps.', 'It takes 2*3*4 steps.'],
    ['keeps an image', '![logo](logo.png)', '![logo](logo.png)'],
    ['changes nothing else', 'Case, "quotes" and punctuation; stay!', 'Case, "quotes" and punctuation; stay!'],
  ])('%s', (_name, input, expected) => {
    expect(normalizeQuotation(input)).toBe(expected);
  });
});

describe('quotationsMatch', () => {
  const source = 'Brindle is **fast**.\nIt reads [the content directory](docs/content.md) and calls it "the tree".';

  it.each([
    ['an exact quotation', quote('Brindle is **fast**.')],
    ['a quotation across the source line break', quote('Brindle is fast. It reads the content directory')],
    ['a quotation with the link syntax kept', quote('It reads [the content directory](docs/content.md)')],
    ['a quotation that itself contains double quotes', quote('and calls it "the tree".')],
    ['two quotations in one text', `${quote('Brindle is fast.')} Also, ${quote('It reads the content directory')}`],
    ['text with no quotation', 'Brindle reads the content directory.'],
  ])('accepts %s', (_name, text) => {
    expect(quotationsMatch(text, [source])).toBe(true);
  });

  it.each([
    ['a changed word', quote('Brindle is quick.')],
    ['a changed case', quote('brindle is fast.')],
    ['dropped punctuation', quote('Brindle is fast It reads')],
    ['an added word', quote('Brindle is very fast.')],
    ['an empty quotation', quote('')],
    ['an unterminated quotation', 'The project states: "Brindle is fast.'],
    ['a second quotation that does not match', `${quote('Brindle is fast.')} Also, ${quote('It writes the tree.')}`],
    ['a quotation spliced from two places', quote('Brindle is fast. It calls it "the tree".')],
  ])('refuses %s', (_name, text) => {
    expect(quotationsMatch(text, [source])).toBe(false);
  });

  it('matches within one source, never across two', () => {
    expect(quotationsMatch(quote('one two'), ['one', 'two'])).toBe(false);
    expect(quotationsMatch(quote('two'), ['one', 'two'])).toBe(true);
  });
});

describe('validateDossierStage', () => {
  const sources = DOSSIER_ILLUSTRATION_SOURCES.map(source => ({ ...source }));
  const requestedAssets = [
    { id: 'core-ideas', kind: 'section', required: true }, { id: 'end-to-end-workflows', kind: 'section', required: true },
    { id: 'mechanisms', kind: 'section', required: true }, { id: 'maintainer-stated-advantages', kind: 'section', required: true },
    { id: 'trade-offs', kind: 'section', required: true }, { id: 'workflow-diagram', kind: 'diagram', required: false },
    { id: 'mechanism-deep-dive', kind: 'deep-dive', required: false },
  ];
  const illustration = <T>(stage: GenerationStage): T => structuredClone(DOSSIER_STAGE_ILLUSTRATIONS[stage]) as T;
  const context = (draft: unknown = illustration('author')): Record<string, unknown> => ({ sources, requestedAssets, inventory: illustration('inventory'), plan: illustration('plan'), draft });
  const misquote = quote('Pages render in worker threads.');

  it('refuses an inventory entry whose quotation its cited source does not hold', () => {
    const inventory = illustration<ProviderInventory>('inventory');
    inventory.entries.find(entry => entry.id === 'e-adv')!.statement = misquote;
    expect(() => validateDossierStage('inventory', inventory, context())).toThrow('unverified-quotation');
  });

  it('refuses a quotation whose words are in a source the claim does not cite', () => {
    const inventory = illustration<ProviderInventory>('inventory');
    inventory.entries.find(entry => entry.id === 'e-adv')!.sourceIds = ['src-build'];
    expect(() => validateDossierStage('inventory', inventory, context())).toThrow('unverified-quotation');
  });

  const placements: [string, (draft: ProviderDraft) => void][] = [
    ['the introduction', draft => { draft.introduction.text = misquote; draft.introduction.sourceIds = ['src-readme']; }],
    ['a section block', draft => { draft.sections[3]!.paragraphs[0]!.text = misquote; }],
    ['a child block', draft => { draft.sections[1]!.paragraphs[0]!.children[0]!.text = misquote; }],
    ['a deep-dive block', draft => { draft.deepDives[0]!.paragraphs[0]!.text = misquote; }],
  ];

  it.each(placements)('refuses a misquotation in %s at author, edit and repair', (_name, place) => {
    const draft = illustration<ProviderDraft>('author');
    place(draft);
    for (const stage of ['author', 'edit', 'repair'] as const) expect(() => validateDossierStage(stage, draft, context()), stage).toThrow('unverified-quotation');
  });

  it.each(placements)('refuses a fidelity review of a draft with a misquotation in %s', (_name, place) => {
    const draft = illustration<ProviderDraft>('author');
    place(draft);
    expect(() => validateDossierStage('fidelity', illustration('fidelity'), context(draft))).toThrow('unverified-quotation');
  });

  it('leaves the plan to validateStage', () => {
    expect(validateDossierStage('plan', illustration('plan'), context())).toEqual(illustration('plan'));
  });

  it('runs validateStage first', () => {
    const inventory = illustration<ProviderInventory>('inventory');
    (inventory.entries[0] as Record<string, unknown>).extra = 'x';
    expect(() => validateDossierStage('inventory', inventory, context())).toThrow('invalid-fields');
  });

  it('is exported from the package entry point with the quotation check', async () => {
    const entry = await import('./index.js') as Record<string, unknown>;
    expect(entry.validateDossierStage).toBe(validateDossierStage);
    expect(entry.quotationsMatch).toBe(quotationsMatch);
    expect(entry.normalizeQuotation).toBe(normalizeQuotation);
  });
});
