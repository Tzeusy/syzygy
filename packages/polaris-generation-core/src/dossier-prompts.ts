/**
 * Dossier prompt templates: instruction text only. A dossier stage prompt is
 * the reviewed manifesto prompt for that stage, unchanged, followed by the
 * dossier rules, the stage's dossier guidance and a one-shot shape
 * illustration whose JSON passes `validateStage` for the stage's own schema
 * (`dossier-prompts.test.ts` proves it). The illustration is a fictional
 * project: it carries no target content, and the prompt says never to copy it.
 *
 * Nothing here selects a profile for a run or calls a provider; the pipeline
 * still sends `promptForStage(stage)` until it is given a profile seam.
 */

import { promptForStage, type GenerationStage } from './prompts.js';
import type { ProviderDraft, ProviderInventory, ProviderPlan, ProviderReview } from './provider-draft.js';

const dossierRules = `This run produces a dossier: an evidence-anchored account that takes a newcomer through a project's core ideas, its end-to-end workflows, the mechanisms underneath them, the advantages its maintainers claim and the trade-offs it accepts. The supplied reader questions and requested assets name those topics; a requested section asset's id is also its section id. Five rules hold at every stage:
1. Claim ledger. One claim per inventory entry or block, citing exactly the sources that support it. A claim no source supports is not written.
2. Workflow traces. Trace a workflow hop by hop across components: name each hop's entry point and what it hands to the next, and cite the source that shows each hand-off. Never bridge a hop no source shows; leave that hop unresolved with the missing evidence as its reason.
3. Mechanisms. Name each function, type, file, command or configuration key in backticks, spelled exactly as the source spells it, and say what it does in the source's terms.
4. Attribution. Report advantages and trade-offs as the maintainers state them ("The maintainers state that ..."), never as your own comparison or judgment. Never supply a benefit for a stated cost or a cost for a stated benefit; say which half no source states. A trade-off read from code rather than stated is labelled as inferred from the code.
5. Thin evidence stays Unknown. Where the sources do not answer a reader question, an unresolved entry, block or disposition naming the missing evidence is the correct answer; never fill the gap with a plausible general account.`;

const guidance: Record<GenerationStage, string> = {
  inventory: `Dossier inventory: build the claim ledger the later stages draw on. Record core ideas as thesis or purpose entries; each workflow hop as a capability entry naming its entry point and hand-off; each mechanism as a choice entry naming its identifier verbatim; each maintainer-stated advantage as an other entry written "The maintainers state that ..."; each trade-off as a qualification entry, attributed, or marked as inferred from the code; disagreements between sources as conflict entries. For a reader question the sources do not answer, add an entry citing the source nearest the question, with an unresolved disposition whose reason names the missing evidence.`,
  plan: `Dossier plan: plan one section per requested section asset, with that asset's id, in an order that lets each section build on the last. Say in each section's reason which reader question it answers and which inventory entries carry it. In the workflow section's reason, name the hops a flow diagram would draw and their sources; in the mechanisms section's reason, name the follow-up question a mechanism deep dive answers. A required section the inventory cannot support keeps an unresolved disposition naming the missing evidence.`,
  author: `Dossier draft: in the workflow section, give each hop its own child block, citing the source that shows the hand-off; draw the requested workflow diagram from those hops only, its labels taken from that text. In the mechanisms section and its deep dive, name identifiers verbatim in backticks and explain what each does. Write each advantage and trade-off as an attributed maintainer statement; where only one half of a trade-off is stated, say the other half is not stated. Record every reader question the sources leave open in unresolved.`,
  edit: `Dossier edit: never soften an attribution into the dossier's own voice, drop or respell a backticked identifier, merge two workflow hops into one block, or replace an unresolved gap with prose.`,
  fidelity: `Dossier review: also check that every advantage and trade-off is attributed to the maintainers and that its source states it; that each backticked identifier appears verbatim in a cited source; that each workflow hop's cited source shows that hand-off; and that no trade-off half is supplied without a source. Each failure is a finding on the block concerned.`,
  repair: `Dossier repair: a repair keeps every attribution, verbatim identifier and per-hop citation, and resolves an unsupported claim by removing it or marking it unresolved, never by rewording it to sound supported.`,
};

/** The fictional sources every illustration cites. */
export const DOSSIER_ILLUSTRATION_SOURCES = [
  { sourceId: 'src-readme', text: 'Tidemark is an in-memory cache for session data. We chose a single-threaded event loop because it avoids lock contention. Eviction is approximate LRU, which costs some precision.' },
  { sourceId: 'src-server', text: 'handleSet parses the SET command, writes the key to the keyspace and calls maybeEvict when maxmemory is exceeded.' },
  { sourceId: 'src-evict', text: 'maybeEvict samples 5 keys and evicts the least recently used key in the sample.' },
] as const;

const produced = (...assetIds: string[]) => ({ kind: 'produced' as const, assetIds });

const inventoryIllustration: ProviderInventory = { entries: [
  { id: 'e-thesis', sourceIds: ['src-readme'], statement: 'Tidemark keeps session data in memory.', kind: 'thesis', disposition: produced('core-ideas') },
  { id: 'e-hop-1', sourceIds: ['src-server'], statement: 'A SET request enters at `handleSet`, which writes the key to the keyspace and hands off to `maybeEvict` when `maxmemory` is exceeded.', kind: 'capability', disposition: produced('end-to-end-workflows') },
  { id: 'e-evict', sourceIds: ['src-evict'], statement: '`maybeEvict` samples 5 keys and evicts the least recently used key in the sample.', kind: 'choice', disposition: produced('mechanisms') },
  { id: 'e-adv', sourceIds: ['src-readme'], statement: 'The maintainers state that the single-threaded event loop avoids lock contention.', kind: 'other', disposition: produced('maintainer-stated-advantages') },
  { id: 'e-cost', sourceIds: ['src-readme'], statement: 'The maintainers state that approximate LRU costs some precision.', kind: 'qualification', disposition: produced('trade-offs') },
  { id: 'e-read', sourceIds: ['src-server'], statement: 'How a read request is served.', kind: 'capability', disposition: { kind: 'unresolved', reason: 'No admitted source shows the read path.', references: ['src-server'] } },
] };

const sectionPlan = (id: string, title: string, reason: string, sourceIds: string[]) => ({ id, title, reason, sourceIds, disposition: produced(id) });
const planIllustration: ProviderPlan = { sections: [
  sectionPlan('core-ideas', 'What Tidemark is for', 'Answers the core-ideas question from e-thesis.', ['src-readme']),
  sectionPlan('end-to-end-workflows', 'How a write travels', 'Answers the workflow question from e-hop-1; a flow diagram draws handleSet to maybeEvict, both shown by src-server. The read path stays unresolved (e-read).', ['src-server']),
  sectionPlan('mechanisms', 'Sampled eviction', 'Answers the mechanisms question from e-evict; a deep dive answers why eviction samples instead of ordering every key.', ['src-evict']),
  sectionPlan('maintainer-stated-advantages', 'What the maintainers claim', 'Answers the advantages question from e-adv, attributed.', ['src-readme']),
  sectionPlan('trade-offs', 'What it gives up', 'Answers the trade-offs question from e-cost; what the cost buys is not stated.', ['src-readme']),
] };

const leaf = (id: string, text: string, ...sourceIds: string[]) => ({ id, text, sourceIds });
const block = (id: string, text: string, sourceIds: string[], children: ReturnType<typeof leaf>[] = []) => ({ id, text, sourceIds, children });
const section = (id: string, title: string, paragraphs: ReturnType<typeof block>[]) => ({ id, title, paragraphs, disposition: produced(id) });
const draftIllustration: ProviderDraft = {
  title: 'Tidemark: an in-memory session cache',
  introduction: leaf('intro', 'Tidemark is an in-memory cache for session data.', 'src-readme'),
  sections: [
    section('core-ideas', 'What Tidemark is for', [block('b-core', 'Tidemark keeps session data in memory.', ['src-readme'])]),
    section('end-to-end-workflows', 'How a write travels', [block('b-flow', 'A write passes through two hops: `handleSet` stores the key, then `maybeEvict` frees memory when `maxmemory` is exceeded.', ['src-server'], [
      leaf('b-flow-1', '`handleSet` parses the SET command and writes the key to the keyspace.', 'src-server'),
      leaf('b-flow-2', 'When `maxmemory` is exceeded, `handleSet` calls `maybeEvict`.', 'src-server'),
    ])]),
    section('mechanisms', 'Sampled eviction', [block('b-mech', '`maybeEvict` samples 5 keys and evicts the least recently used key in the sample.', ['src-evict'])]),
    section('maintainer-stated-advantages', 'What the maintainers claim', [block('b-adv', 'The maintainers state that the single-threaded event loop avoids lock contention.', ['src-readme'])]),
    section('trade-offs', 'What it gives up', [block('b-cost', 'The maintainers state that approximate LRU costs some precision; what it buys in return is not stated in the sources.', ['src-readme'])]),
  ],
  diagrams: [{ id: 'workflow-diagram', title: 'A write, hop by hop', sectionId: 'end-to-end-workflows', kind: 'flow', relationship: 'Which function hands a SET request to which.',
    nodes: [{ id: 'n-set', label: 'handleSet', sourceIds: ['src-server'], epistemic: 'observed' }, { id: 'n-evict', label: 'maybeEvict', sourceIds: ['src-server'], epistemic: 'observed' }],
    edges: [{ id: 'g-calls', from: 'n-set', to: 'n-evict', label: 'calls', sourceIds: ['src-server'], epistemic: 'observed' }],
    disposition: produced('workflow-diagram') }],
  deepDives: [{ id: 'mechanism-deep-dive', title: 'Which keys can eviction remove?', sectionId: 'mechanisms', paragraphs: [
    block('b-dive', 'Only a key in the 5-key sample can be evicted on a pass: `maybeEvict` compares recency within the sample, not across the keyspace.', ['src-evict']),
  ], disposition: produced('mechanism-deep-dive') }],
  unresolved: [{ question: 'How is a read request served?', reason: 'No admitted source shows the read path.', references: ['src-server'] }],
};

const supported = (blockId: string, ...sourceIds: string[]) => ({ blockId, verdict: 'supported' as const, sourceIds, reason: 'The cited source states this.' });
const represented = (entryId: string, ...blockIds: string[]) => ({ entryId, disposition: 'represented' as const, blockIds, reason: 'Represented.' });
const reviewIllustration: ProviderReview = {
  inventoryCoverage: [
    represented('e-thesis', 'b-core'), represented('e-hop-1', 'b-flow', 'b-flow-1', 'b-flow-2'), represented('e-evict', 'b-mech', 'b-dive'),
    represented('e-adv', 'b-adv'), represented('e-cost', 'b-cost'),
    { entryId: 'e-read', disposition: 'unresolved', blockIds: [], reason: 'No admitted source shows the read path; the draft lists it as unresolved.' },
  ],
  blockSupport: [
    supported('intro', 'src-readme'), supported('b-core', 'src-readme'), supported('b-flow', 'src-server'), supported('b-flow-1', 'src-server'),
    supported('b-flow-2', 'src-server'), supported('b-mech', 'src-evict'), supported('b-adv', 'src-readme'), supported('b-cost', 'src-readme'),
    supported('n-set', 'src-server'), supported('n-evict', 'src-server'), supported('g-calls', 'src-server'),
    { blockId: 'b-dive', verdict: 'supported', sourceIds: ['src-evict'], reason: 'Follows from sampling as src-evict states it.' },
  ],
  findings: [{ severity: 'advisory', message: 'The trade-off states a cost and, correctly, no benefit; no source states what approximate LRU buys.', target: 'b-cost' }],
};

/** One illustration per stage; edit and repair return the author's shape. */
export const DOSSIER_STAGE_ILLUSTRATIONS: Readonly<Record<GenerationStage, unknown>> = {
  inventory: inventoryIllustration, plan: planIllustration, author: draftIllustration, edit: draftIllustration, fidelity: reviewIllustration, repair: draftIllustration,
};

/** Shared with the discovery prompts (discovery-provider.ts). */
export const ILLUSTRATION_HEADING = 'Shape illustration for a fictional project. Copy its structure, never its content, handles or claims; your output follows the supplied schema and sources:';

export function dossierPromptForStage(stage: GenerationStage): { version: string; system: string } {
  const base = promptForStage(stage);
  return {
    version: `polaris-${stage}-dossier-v1`,
    system: `${base.system}\n\n${dossierRules}\n\n${guidance[stage]}\n\n${ILLUSTRATION_HEADING}\n${JSON.stringify(DOSSIER_STAGE_ILLUSTRATIONS[stage])}`,
  };
}
