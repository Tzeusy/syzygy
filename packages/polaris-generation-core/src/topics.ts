/** The owner-level subjects a dossier answers, and the reader questions that name them. Leaf
 * declarations shared by the dossier evaluator, the reader-question validator and the dossier profile. */

export const READER_QUESTIONS_FORMAT = 'polaris-reader-questions-v1';
export const OWNER_TOPICS = ['core-ideas', 'end-to-end-workflows', 'mechanisms', 'maintainer-stated-advantages', 'trade-offs'] as const;
export type OwnerTopic = typeof OWNER_TOPICS[number];

export interface ReaderQuestion { readonly id: string; readonly topics: readonly OwnerTopic[]; readonly text: string }
