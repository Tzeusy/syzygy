/**
 * The dossier run profile and the REQ-polaris-generation-031 clarification
 * step. Project-neutral: nothing here names a repository. Pure; an owner
 * port is injected, and the zero-interaction mode never calls one, recording
 * instead the questions it would have asked and the limitation each leaves.
 */

import { createHash } from 'node:crypto';

import type { GenerationSource } from './generation-source.js';
import type { RequestedAsset } from './provider-draft.js';
import type { ReaderQuestion } from './reader-questions.js';

export const DOSSIER_PROFILE_ID = 'dossier-v1';
export const READER_QUESTIONS_FILE_FORMAT = 'polaris-reader-questions-v1';

/** What a dossier reader must come away able to answer. The advantage
 * question is deliberately about the maintainers' own claims: a dossier
 * reports what they say and where, never its own comparative judgment. */
export const DOSSIER_READER_QUESTIONS: readonly ReaderQuestion[] = [
  { id: 'core-ideas', topics: ['core-ideas'], text: 'What are this project\'s core ideas, stated so a newcomer could repeat them?' },
  { id: 'end-to-end-workflows', topics: ['end-to-end-workflows'], text: 'How does a user get from start to finish on the most important end-to-end workflows?' },
  { id: 'mechanisms', topics: ['mechanisms'], text: 'What mechanisms underneath make those workflows work, and where does each live?' },
  { id: 'maintainer-stated-advantages', topics: ['maintainer-stated-advantages'], text: 'What advantages over alternatives do the maintainers themselves claim, in which words and where?' },
  { id: 'trade-offs', topics: ['trade-offs'], text: 'What trade-offs, limits and costs does the design accept, and what does it give up for them?' },
];

/** The frozen questions file the dossier evaluator reads. */
export const dossierQuestionsFile = (): string =>
  `${JSON.stringify({ format: READER_QUESTIONS_FILE_FORMAT, questions: DOSSIER_READER_QUESTIONS }, null, 2)}\n`;

export const DOSSIER_REQUESTED_ASSETS: readonly RequestedAsset[] = [
  { id: 'core-ideas', kind: 'section', required: true },
  { id: 'end-to-end-workflows', kind: 'section', required: true },
  { id: 'mechanisms', kind: 'section', required: true },
  { id: 'maintainer-stated-advantages', kind: 'section', required: true },
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
  /** Digest of the material content (id, question, scope, reason): a changed scope is a new question. */
  readonly contentDigest: string;
}
export interface OwnerAnswer {
  readonly id: ClarificationQuestion['id'];
  readonly answer: unknown;
  readonly attribution: string;
  readonly revision: string;
  readonly permittedDraftUse: boolean;
}
/** What an earlier pass concluded about a question, keyed by id and content digest. */
export interface PriorDisposition {
  readonly id: ClarificationQuestion['id'];
  readonly contentDigest: string;
  readonly disposition: 'answered' | 'unknown' | 'deferred' | 'redacted';
  readonly answer?: string;
  readonly attribution?: string;
  readonly revision?: string;
}
export interface RecordedAnswer {
  readonly id: ClarificationQuestion['id'];
  readonly disposition: 'answered' | 'unknown' | 'redacted';
  /** Null when unknown or when the owner did not permit draft use. */
  readonly answer: string | null;
  readonly attribution: string;
  readonly revision: string;
  readonly permittedDraftUse: boolean;
  readonly contentDigest: string;
  readonly adopted: false;
  readonly reused: boolean;
}
export interface ClarificationInput {
  /** The population after discovery, including excluded and deferred rows. */
  readonly sources: readonly GenerationSource[];
  /** Earlier outcomes. An unchanged question is not asked again; a changed one is. */
  readonly prior?: readonly PriorDisposition[];
  readonly audienceDeclared?: boolean;
  readonly maxQuestions?: number;
  readonly mode: 'zero-interaction' | 'interactive';
  readonly ask?: (question: ClarificationQuestion) => Promise<OwnerAnswer>;
}
export interface ClarificationRecord {
  readonly mode: ClarificationInput['mode'];
  readonly wouldHaveAsked: readonly ClarificationQuestion[];
  readonly answers: readonly RecordedAnswer[];
  /** Consequential unknowns the account must carry, one sentence each. */
  readonly limitations: readonly string[];
  readonly suppressedAsRepeats: readonly string[];
  readonly suppressedByBudget: readonly string[];
  /** Questions asked again because their content changed since a deferral. */
  readonly reaskedAfterChange: readonly string[];
  readonly aborted?: { readonly id: string; readonly reason: string };
  /** Dispositions to hand to the next pass as `prior`. */
  readonly dispositions: readonly PriorDisposition[];
  /** Open questions with neither an owner answer nor a carried limitation; measured, expected 0. */
  readonly unaccountedQuestions: number;
}

const PURPOSE_DOC = /(^|\/)(readme|overview|about|intro(duction)?|manifesto|vision|why|philosophy)[^/]*$/iu;
const digestOf = (q: Omit<ClarificationQuestion, 'contentDigest'>): string =>
  createHash('sha256').update(JSON.stringify([q.id, q.question, q.scope, q.reason])).digest('hex');
const withDigest = (q: Omit<ClarificationQuestion, 'contentDigest'>): ClarificationQuestion => ({ ...q, contentDigest: digestOf(q) });

/** Which consequential questions the population leaves open, in priority order. */
export function openQuestions(sources: readonly GenerationSource[], audienceDeclared = false): readonly ClarificationQuestion[] {
  const quotable = sources.filter(source => !source.exclusion.excluded && source.spans.length > 0);
  const deferred = sources.filter(source => source.exclusion.excluded && source.exclusion.reason === 'deferred-by-budget');
  const out: ClarificationQuestion[] = [];
  if (!quotable.some(source => PURPOSE_DOC.test(source.path))) out.push(withDigest({ id: 'purpose',
    question: 'What is this project for, and who is it for?', scope: 'The purpose and beneficiary framing of every section.',
    reason: 'No selected source path looks like an overview, README or statement of purpose (a path test, not a reading of content).',
    limitation: 'Purpose and intended beneficiary were not established; no mission is asserted.' }));
  if (!audienceDeclared) out.push(withDigest({ id: 'audience', question: 'Who should this dossier be written for?',
    scope: 'Depth, vocabulary and which workflows are treated as primary.', reason: 'No intended reader was declared.',
    limitation: 'The intended reader was not declared and remains unestablished; no reader assumption is asserted.' }));
  if (deferred.length > 0) out.push(withDigest({ id: 'scope',
    question: `${deferred.length} file(s) did not fit the source budget. Continue with a limited account, or extend the budget?`,
    scope: 'Every claim about material in the deferred files.', reason: 'Selection was capped, so part of the repository is counted but unread.',
    limitation: `${deferred.length} file(s) were counted but not read; the account does not cover the whole repository.` }));
  return out;
}

const normalise = (answer: unknown): string | null =>
  typeof answer === 'string' && answer.trim().length > 0 && answer.trim() !== 'unknown' ? answer.trim() : null;

/** Applies the declared question budget and the no-repeat rule, then either
 * records the questions (zero-interaction) or puts them to the owner. An
 * answer is a recorded input, never an adoption; an empty or non-string
 * answer is `unknown`, and an answer not permitted for draft use is redacted
 * from the record, leaving only the limitation. */
export async function clarify(input: ClarificationInput): Promise<ClarificationRecord> {
  const max = input.maxQuestions ?? 3;
  if (!Number.isSafeInteger(max) || max < 0) throw new Error('invalid-question-budget');
  if (input.mode === 'interactive' && input.ask === undefined) throw new Error('interactive-clarification-needs-an-owner-port');
  const open = openQuestions(input.sources, input.audienceDeclared);
  const prior = new Map((input.prior ?? []).map(entry => [entry.id, entry]));
  const same = (question: ClarificationQuestion): PriorDisposition | undefined => {
    const earlier = prior.get(question.id);
    return earlier !== undefined && earlier.contentDigest === question.contentDigest ? earlier : undefined;
  };
  const answers: RecordedAnswer[] = [], unresolved: ClarificationQuestion[] = [], repeats: ClarificationQuestion[] = [], reasked: string[] = [];
  const fresh: ClarificationQuestion[] = [];
  for (const question of open) {
    const earlier = same(question);
    if (earlier === undefined) { if (prior.has(question.id)) reasked.push(question.id); fresh.push(question); continue; }
    if (earlier.disposition === 'answered' && earlier.answer !== undefined && earlier.attribution && earlier.revision) {
      answers.push({ id: question.id, disposition: 'answered', answer: earlier.answer, attribution: earlier.attribution, revision: earlier.revision,
        permittedDraftUse: true, contentDigest: question.contentDigest, adopted: false, reused: true });
    } else { repeats.push(question); unresolved.push(question); }
  }
  const asked = fresh.slice(0, max), overBudget = fresh.slice(max);
  unresolved.push(...overBudget);
  let aborted: ClarificationRecord['aborted'];
  if (input.mode === 'interactive') {
    for (const [index, question] of asked.entries()) {
      try {
        const reply = await input.ask!(question);
        if (reply === null || typeof reply !== 'object' || reply.id !== question.id || typeof reply.attribution !== 'string' || !reply.attribution
          || typeof reply.revision !== 'string' || !reply.revision || typeof reply.permittedDraftUse !== 'boolean') throw new Error('invalid-owner-answer');
        const text = normalise(reply.answer);
        const permitted = reply.permittedDraftUse && text !== null;
        answers.push({ id: question.id, disposition: text === null ? 'unknown' : reply.permittedDraftUse ? 'answered' : 'redacted', answer: permitted ? text : null,
          attribution: reply.attribution, revision: reply.revision, permittedDraftUse: reply.permittedDraftUse, contentDigest: question.contentDigest, adopted: false, reused: false });
        if (!permitted) unresolved.push(question);
      } catch (error) {
        aborted = { id: question.id, reason: (error instanceof Error ? error.message : 'owner-port-failed').slice(0, 200) };
        unresolved.push(...asked.slice(index));
        break;
      }
    }
  } else unresolved.push(...asked);
  const answeredIds = new Set(answers.filter(a => a.disposition === 'answered').map(a => a.id)), carried = new Set(unresolved.map(q => q.id));
  const dispositions: PriorDisposition[] = [
    ...answers.map((a): PriorDisposition => ({ id: a.id, contentDigest: a.contentDigest, disposition: a.disposition,
      ...(a.disposition === 'answered' ? { answer: a.answer!, attribution: a.attribution, revision: a.revision } : {}) })),
    ...unresolved.filter(q => !answers.some(a => a.id === q.id)).map((q): PriorDisposition => ({ id: q.id, contentDigest: q.contentDigest, disposition: 'deferred' })),
  ];
  return { mode: input.mode, wouldHaveAsked: input.mode === 'zero-interaction' ? asked : [], answers,
    limitations: unresolved.map(question => question.limitation), suppressedAsRepeats: repeats.map(q => q.id),
    suppressedByBudget: overBudget.map(q => q.id), reaskedAfterChange: reasked, ...(aborted === undefined ? {} : { aborted }), dispositions,
    unaccountedQuestions: open.filter(q => !answeredIds.has(q.id) && !carried.has(q.id)).length };
}
