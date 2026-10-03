/**
 * The dossier run profile and the REQ-polaris-generation-031 clarification
 * step. Project-neutral: nothing here names a repository. Pure; an owner
 * port is injected, and the zero-interaction mode never calls one, recording
 * instead the questions it would have asked and the limitation each leaves.
 */

import type { GenerationSource } from './generation-source.js';
import type { RequestedAsset } from './provider-draft.js';

export const DOSSIER_PROFILE_ID = 'dossier-v1';

/** What a dossier reader must come away able to answer. The advantage
 * question is deliberately about the maintainers' own claims: a dossier
 * reports what they say and where, never its own comparative judgment. */
export const DOSSIER_READER_QUESTIONS: readonly string[] = [
  'What are this project\'s core ideas, stated so a newcomer could repeat them?',
  'How does a user get from start to finish on the most important end-to-end workflows?',
  'What mechanisms underneath make those workflows work, and where does each live?',
  'What advantages over alternatives do the maintainers themselves claim, in which words and where?',
  'What trade-offs, limits and costs does the design accept, and what does it give up for them?',
];

export const DOSSIER_REQUESTED_ASSETS: readonly RequestedAsset[] = [
  { id: 'core-ideas', kind: 'section', required: true },
  { id: 'workflows', kind: 'section', required: true },
  { id: 'mechanisms', kind: 'section', required: true },
  { id: 'maintainer-claimed-advantages', kind: 'section', required: true },
  { id: 'trade-offs', kind: 'section', required: true },
  { id: 'workflow-diagram', kind: 'diagram', required: false },
  { id: 'mechanism-deep-dive', kind: 'deep-dive', required: false },
];

export interface ClarificationQuestion {
  readonly id: 'purpose' | 'audience' | 'scope';
  readonly question: string;
  /** What part of the account the answer would change. */
  readonly scope: string;
  readonly reason: string;
  /** Stated in the account when the question stays unanswered. */
  readonly limitation: string;
}
export interface OwnerAnswer {
  readonly id: ClarificationQuestion['id'];
  readonly answer: string | 'unknown';
  readonly attribution: string;
  readonly revision: string;
  readonly permittedDraftUse: boolean;
}
export interface ClarificationInput {
  /** The population after discovery, including excluded and deferred rows. */
  readonly sources: readonly GenerationSource[];
  /** Questions an earlier pass already put and the owner deferred. */
  readonly alreadyDeferred?: readonly string[];
  readonly audienceDeclared?: boolean;
  readonly maxQuestions?: number;
  readonly mode: 'zero-interaction' | 'interactive';
  readonly ask?: (question: ClarificationQuestion) => Promise<OwnerAnswer>;
}
export interface ClarificationRecord {
  readonly mode: ClarificationInput['mode'];
  readonly wouldHaveAsked: readonly ClarificationQuestion[];
  readonly answers: readonly (OwnerAnswer & { readonly adopted: false })[];
  /** Consequential unknowns the account must carry, one sentence each. */
  readonly limitations: readonly string[];
  readonly suppressedAsRepeats: readonly string[];
  readonly suppressedByBudget: readonly string[];
  readonly fabricatedDefaults: 0;
}

const PURPOSE_DOC = /(^|\/)(readme|overview|about|intro(duction)?|manifesto|vision|why|philosophy)[^/]*$/iu;

/** Which consequential questions the population leaves open, in priority order. */
export function openQuestions(sources: readonly GenerationSource[], audienceDeclared = false): readonly ClarificationQuestion[] {
  const quotable = sources.filter(source => !source.exclusion.excluded && source.spans.length > 0);
  const deferred = sources.filter(source => source.exclusion.excluded && source.exclusion.reason === 'deferred-by-budget');
  const out: ClarificationQuestion[] = [];
  if (!quotable.some(source => PURPOSE_DOC.test(source.path))) out.push({ id: 'purpose',
    question: 'What is this project for, and who is it for?', scope: 'The purpose and beneficiary framing of every section.',
    reason: 'The selected sources explain mechanics but include no overview, README or statement of purpose.',
    limitation: 'Purpose and intended beneficiary were not established; no mission is asserted.' });
  if (!audienceDeclared) out.push({ id: 'audience', question: 'Who should this dossier be written for?',
    scope: 'Depth, vocabulary and which workflows are treated as primary.', reason: 'No intended reader was declared.',
    limitation: 'Intended reader was not declared; the account assumes a technically capable newcomer.' });
  if (deferred.length > 0) out.push({ id: 'scope',
    question: `${deferred.length} file(s) did not fit the source budget. Continue with a limited account, or extend the budget?`,
    scope: 'Every claim about material in the deferred files.', reason: 'Selection was capped, so part of the repository is counted but unread.',
    limitation: `${deferred.length} file(s) were counted but not read; the account does not cover the whole repository.` });
  return out;
}

/** Applies the declared question budget and the no-repeat rule, then either
 * records the questions (zero-interaction) or puts them to the owner. An
 * answer is a recorded input, never an adoption. */
export async function clarify(input: ClarificationInput): Promise<ClarificationRecord> {
  const max = input.maxQuestions ?? 3;
  if (!Number.isSafeInteger(max) || max < 0) throw new Error('invalid-question-budget');
  if (input.mode === 'interactive' && input.ask === undefined) throw new Error('interactive-clarification-needs-an-owner-port');
  const open = openQuestions(input.sources, input.audienceDeclared);
  const deferredBefore = new Set(input.alreadyDeferred ?? []);
  const repeats = open.filter(question => deferredBefore.has(question.id));
  const fresh = open.filter(question => !deferredBefore.has(question.id));
  const asked = fresh.slice(0, max), overBudget = fresh.slice(max);
  const answers: ClarificationRecord['answers'][number][] = [];
  const unresolved: ClarificationQuestion[] = [...repeats, ...overBudget];
  if (input.mode === 'interactive') {
    for (const question of asked) {
      const reply = await input.ask!(question);
      if (reply.id !== question.id || !reply.attribution || !reply.revision) throw new Error('invalid-owner-answer');
      answers.push({ ...reply, adopted: false });
      if (reply.answer === 'unknown' || !reply.permittedDraftUse) unresolved.push(question);
    }
  } else unresolved.push(...asked);
  return { mode: input.mode, wouldHaveAsked: input.mode === 'zero-interaction' ? asked : [], answers,
    limitations: unresolved.map(question => question.limitation), suppressedAsRepeats: repeats.map(q => q.id),
    suppressedByBudget: overBudget.map(q => q.id), fabricatedDefaults: 0 };
}
