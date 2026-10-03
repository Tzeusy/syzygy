/**
 * The stage validator for the dossier profile: `validateStage`, then the
 * rule-4 quotation check in code (quotations.ts). An inventory entry or draft
 * block that quotes the project must match one of the sources it cites, or the
 * whole stage output is refused, as any other validation failure is. This sits
 * beside provider-draft.ts rather than in it, so that module keeps importing
 * nothing but node:util and types.
 */

import { validateStage, type ProviderDraft, type ProviderInventory } from './provider-draft.js';
import type { GenerationStage } from './prompts.js';
import { quotationsMatch } from './quotations.js';

interface Claim { readonly text: string; readonly sourceIds: readonly string[] }

function draftClaims(draft: ProviderDraft): Claim[] {
  const tree = (blocks: ProviderDraft['sections'][number]['paragraphs']): Claim[] => blocks.flatMap(block => [block, ...block.children]);
  return [draft.introduction, ...draft.sections.flatMap(section => tree(section.paragraphs)), ...draft.deepDives.flatMap(dive => tree(dive.paragraphs))];
}

/** `validateStage` for the dossier profile, plus the deterministic quotation check. Throws `unverified-quotation`. */
export function validateDossierStage(stage: GenerationStage, value: unknown, context: Record<string, unknown>): unknown {
  const validated = validateStage(stage, value, context);
  const texts = new Map((context.sources as { sourceId: string; text: string }[]).map(source => [source.sourceId, source.text]));
  const claims = stage === 'inventory' ? (validated as ProviderInventory).entries.map(entry => ({ text: entry.statement, sourceIds: entry.sourceIds }))
    : stage === 'author' || stage === 'edit' || stage === 'repair' ? draftClaims(validated as ProviderDraft)
    : stage === 'fidelity' ? draftClaims(context.draft as ProviderDraft) : [];
  for (const claim of claims) {
    if (!quotationsMatch(claim.text, claim.sourceIds.map(id => texts.get(id) ?? ''))) throw new Error('unverified-quotation');
  }
  return validated;
}
