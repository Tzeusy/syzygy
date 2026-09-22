// Synthetic second-project corpora — N8 slice 1 (syzygy-u05.8), released by
// the owner closing gate syzygy-dca.
//
// Three fixtures, each in a container shape the one consented Butlers
// repository does not use for the claim class it targets. They measure how
// general the unmodified PWB extraction pipeline
// (`project-shape-extraction.ts`) is beyond the one shape it was built
// against — never to make the pipeline pass. Zero egress: every corpus is a
// literal string constant compiled into this package; nothing here reads a
// real repository, requests a network resource, or grants new consent.
//
// Each `path` is a synthetic repository-relative path carrying the same
// basename Butlers' own source of that class uses (`vision.md`, `v1.md`,
// `README.md`), so that a class's extractor sees the shape difference in
// isolation from the basename gate. `synthetic-corpus-coverage.ts` also
// runs the other eight classes against each corpus, honestly, to measure
// the basename gate itself.

import type { ExtractionClass } from '../project-shape-manifest.js';

export interface SyntheticCorpusFixture {
  readonly id: string;
  // One line naming the shape and why it is realistic outside Butlers.
  readonly description: string;
  // The class this corpus's shape was authored to test.
  readonly targetClass: ExtractionClass;
  readonly shape: string;
  // A synthetic repository-relative path; only its basename is load-bearing
  // for the extraction dispatch in `project-shape-extraction.ts`.
  readonly path: string;
  readonly text: string;
}

// Principles as a plain unordered bullet list with no bold lead — common in
// project READMEs and charters. Butlers' `vision.md` uses a bold-led
// decimal ordered list under the same heading (`extractPrinciples`).
const PRINCIPLE_BULLET_LIST = [
  '# Aurora',
  '',
  '## Non-Negotiable Rules',
  '',
  '- Every claim must cite the source it came from.',
  '- Never silently drop a failing check.',
  '- Treat committed history as durable evidence, not a draft.',
  '',
].join('\n');

// Success criteria as a two-column pipe table — common in spec and PRD
// templates. Butlers' `vision.md`/`v1.md` use a bullet list under the same
// heading (`extractSuccessCriteria`).
const SUCCESS_CRITERION_TABLE = [
  '# Nimbus v1',
  '',
  '## Success Criteria',
  '',
  '| Criterion | Signal |',
  '| --- | --- |',
  '| Response latency | p95 under 400ms |',
  '| Data durability | zero silent loss across a restart |',
  '',
].join('\n');

// A craft/reading-order policy as numbered prose paragraphs naming one file
// per paragraph — common in onboarding docs. Butlers' `README.md` uses a
// "Reading Order" table with a `File` column (`extractCraftPolicies`).
const CRAFT_POLICY_PROSE = [
  '# Nimbus Craft and Care',
  '',
  '## Reading Order',
  '',
  'Start with principles.md, which sets the non-negotiable rules before',
  'anything else is read.',
  '',
  'Next, read review-checklist.md for the acceptance bar every change must',
  'clear.',
  '',
  'Finally, testing-standards.md closes the loop with the coverage floor',
  'this project holds itself to.',
  '',
].join('\n');

export const SYNTHETIC_CORPORA: readonly SyntheticCorpusFixture[] = [
  {
    id: 'principle-bullet-list',
    description: 'Principles as an unordered bullet list with no bold lead, a common charter shape outside Butlers.',
    targetClass: 'principle',
    shape: 'unordered bullet list, no bold lead',
    path: 'about/heart-and-soul/vision.md',
    text: PRINCIPLE_BULLET_LIST,
  },
  {
    id: 'success-criterion-table',
    description: 'Success criteria as a two-column pipe table, a common spec-template shape outside Butlers.',
    targetClass: 'success-criterion',
    shape: 'two-column pipe table',
    path: 'about/spec-and-spine/v1.md',
    text: SUCCESS_CRITERION_TABLE,
  },
  {
    id: 'craft-policy-prose',
    description: 'A reading-order policy as numbered prose paragraphs, a common onboarding-doc shape outside Butlers.',
    targetClass: 'craft-policy',
    shape: 'numbered prose paragraphs',
    path: 'about/craft-and-care/README.md',
    text: CRAFT_POLICY_PROSE,
  },
] as const;
