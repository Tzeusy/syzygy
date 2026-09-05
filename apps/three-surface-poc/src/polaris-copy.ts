/**
 * Every fixed owner-visible Polaris string, with exactly one role from the
 * closed PWB-REQ-012 set. The renderer takes text from this table and
 * marks the element that carries it with `data-copy-role`; the human output
 * exposes the role through that attribute and the machine side is this
 * table itself. Templated sentences (a count, a reason, a path) are not
 * rows — their carrying element still declares the role, and the oracle in
 * `polaris-copy.test.ts` sweeps the rendered text, not this table.
 */
import { claimRoleAttrs, type NarrativeClaimRole } from './polaris-narrative.js';

export const COPY_ROLES = ['project-fact', 'epistemic-disclosure', 'action-label', 'scope-instruction'] as const;
export type CopyRole = (typeof COPY_ROLES)[number];

export const COPY_KINDS = ['heading', 'lede', 'notice', 'sentence', 'label'] as const;
export type CopyKind = (typeof COPY_KINDS)[number];

export interface PolarisCopyRow {
  readonly id: string;
  readonly role: CopyRole;
  readonly kind: CopyKind;
  readonly text: string;
}

export const POLARIS_COPY = [
  { id: 'shell.heading', role: 'project-fact', kind: 'heading', text: 'Butlers, as it declares itself' },
  { id: 'shell.lede', role: 'scope-instruction', kind: 'lede', text: 'Purpose, promises, boundaries, architecture and V1 first; then the project catalog; then one capability in depth.' },
  { id: 'notice', role: 'epistemic-disclosure', kind: 'notice', text: 'Every positive claim below cites its source. Where evidence is absent, Unknown is stated in place with its route to resolution.' },

  { id: 'depth.label', role: 'scope-instruction', kind: 'label', text: 'Depths, from summary to exact source:' },
  { id: 'depth.summary', role: 'scope-instruction', kind: 'label', text: 'Summary' },
  { id: 'depth.catalog', role: 'scope-instruction', kind: 'label', text: 'Catalog' },
  { id: 'depth.detail', role: 'scope-instruction', kind: 'label', text: 'Detail' },
  { id: 'depth.source', role: 'scope-instruction', kind: 'label', text: 'Exact source' },

  { id: 'group.overview', role: 'project-fact', kind: 'heading', text: 'What Butlers is' },
  { id: 'group.boundaries', role: 'project-fact', kind: 'heading', text: 'What Butlers is not' },
  { id: 'group.architecture', role: 'project-fact', kind: 'heading', text: 'How Butlers is built' },
  { id: 'group.v1', role: 'project-fact', kind: 'heading', text: 'What V1 ships' },
  { id: 'group.catalog', role: 'project-fact', kind: 'heading', text: 'Project catalog' },
  { id: 'group.capability-detail', role: 'project-fact', kind: 'heading', text: 'One capability in depth' },
  { id: 'group.evidence-and-gaps', role: 'project-fact', kind: 'heading', text: 'Evidence and gaps' },

  { id: 'account.purpose', role: 'project-fact', kind: 'heading', text: 'Purpose' },
  { id: 'account.promises', role: 'project-fact', kind: 'heading', text: 'Promises' },
  { id: 'account.refusals', role: 'project-fact', kind: 'heading', text: 'Refusals' },
  { id: 'account.architecture', role: 'project-fact', kind: 'heading', text: 'Architecture' },
  { id: 'account.v1-scope', role: 'project-fact', kind: 'heading', text: 'V1 scope' },
  { id: 'account.v1-success', role: 'project-fact', kind: 'heading', text: 'V1 success' },

  { id: 'class.project-account-section', role: 'project-fact', kind: 'heading', text: 'Project account' },
  { id: 'class.principle', role: 'project-fact', kind: 'heading', text: 'Non-negotiable rules' },
  { id: 'class.success-criterion', role: 'project-fact', kind: 'heading', text: 'Success criteria' },
  { id: 'class.catalog-entry', role: 'project-fact', kind: 'heading', text: 'Declared projects' },
  { id: 'class.design-contract', role: 'project-fact', kind: 'heading', text: 'Design contracts' },
  { id: 'class.baseline-spec', role: 'project-fact', kind: 'heading', text: 'Baseline specs' },
  { id: 'class.topology-component', role: 'project-fact', kind: 'heading', text: 'Components' },
  { id: 'class.craft-policy', role: 'project-fact', kind: 'heading', text: 'Craft policies' },
  { id: 'class.roster-identity', role: 'project-fact', kind: 'heading', text: 'Roster identities' },

  { id: 'capability.scope', role: 'scope-instruction', kind: 'sentence', text: "This is one capability within the project catalog above; completeness follows its disclosed denominator. Its claims keep their own provenance and state." },

  { id: 'proposed.heading', role: 'project-fact', kind: 'heading', text: 'Proposed OpenSpec change' },
  { id: 'label.proposed', role: 'epistemic-disclosure', kind: 'label', text: 'Proposed change — not current authority.' },
  { id: 'proposed.current', role: 'project-fact', kind: 'heading', text: 'Current authority' },
  { id: 'proposed.change', role: 'project-fact', kind: 'heading', text: 'The proposal' },
  { id: 'band.argument', role: 'project-fact', kind: 'heading', text: 'Why this capability' },
  { id: 'band.argument-lede', role: 'scope-instruction', kind: 'lede', text: 'Framing only. This band binds nothing and anchors nothing.' },
  { id: 'label.thesis', role: 'project-fact', kind: 'label', text: 'Capability' },
  { id: 'label.why', role: 'project-fact', kind: 'label', text: 'Why it exists' },
  { id: 'label.related', role: 'project-fact', kind: 'label', text: 'Related' },
  { id: 'sentence.no-intent-declared', role: 'project-fact', kind: 'sentence', text: 'No intent entity names this capability.' },
  { id: 'band.contract', role: 'project-fact', kind: 'heading', text: 'Current intent, verbatim' },
  { id: 'band.contract-lede', role: 'scope-instruction', kind: 'lede', text: 'The current requirement, its governing doctrine and non-goals, and every proposal beside it.' },
  { id: 'contract.verbatim-lede', role: 'scope-instruction', kind: 'lede', text: 'Requirement and scenario text appears byte-for-byte from its owning artifact, or not at all.' },
  { id: 'label.requirement-text', role: 'project-fact', kind: 'heading', text: 'Requirement and scenario text' },
  { id: 'label.doctrine', role: 'project-fact', kind: 'heading', text: 'Governing doctrine' },
  { id: 'label.non-goals', role: 'project-fact', kind: 'heading', text: 'Declared non-goals' },
  { id: 'label.adoption', role: 'project-fact', kind: 'label', text: 'Adoption:' },
  { id: 'adoption.adopted', role: 'project-fact', kind: 'label', text: 'adopted' },
  { id: 'adoption.draft', role: 'project-fact', kind: 'label', text: 'draft, unadopted' },
  { id: 'label.candidate-future', role: 'project-fact', kind: 'label', text: 'One candidate future' },
  { id: 'label.exclusive-with', role: 'project-fact', kind: 'label', text: 'exclusive with' },
  { id: 'sentence.separate-futures', role: 'project-fact', kind: 'sentence', text: 'Competing proposals stay separate; nothing merges them.' },
  { id: 'sentence.no-competitor', role: 'project-fact', kind: 'sentence', text: 'no declared competitor.' },
  { id: 'sentence.exclusivity-not-captured', role: 'project-fact', kind: 'sentence', text: 'no exclusivity declaration was captured, so it is treated as its own future.' },
  { id: 'band.reality', role: 'project-fact', kind: 'heading', text: 'What is observed' },
  { id: 'band.reality-lede', role: 'scope-instruction', kind: 'lede', text: 'Every claim here comes from the shared model with its own provenance and epistemic state.' },
  { id: 'label.mode', role: 'scope-instruction', kind: 'label', text: 'Mode:' },
  { id: 'sentence.base-mode', role: 'scope-instruction', kind: 'sentence', text: 'current intent with observed reality. No proposal is applied.' },
  { id: 'label.lifecycle', role: 'project-fact', kind: 'label', text: 'Lifecycle:' },
  { id: 'label.amends', role: 'project-fact', kind: 'label', text: 'amends' },

  { id: 'label.coverage-counts', role: 'action-label', kind: 'label', text: 'Coverage counts' },
  { id: 'label.primary-reasons', role: 'epistemic-disclosure', kind: 'label', text: 'Primary Unknown reasons among members:' },
  { id: 'label.secondary-reasons', role: 'epistemic-disclosure', kind: 'label', text: 'Secondary Unknown reasons among members:' },
  { id: 'sentence.no-member-unknowns', role: 'epistemic-disclosure', kind: 'sentence', text: 'No member claim carries an Unknown reason.' },

  { id: 'evidence.observation', role: 'project-fact', kind: 'heading', text: 'Project-shape observation' },
  { id: 'evidence.sources', role: 'project-fact', kind: 'heading', text: 'Project-shape sources' },
  { id: 'evidence.exclusions', role: 'project-fact', kind: 'heading', text: 'Excluded bodies' },
  { id: 'evidence.contradictions', role: 'project-fact', kind: 'heading', text: 'Contradicted facts' },
  // PWB-REQ-004 (as amended): the root index's own declarations and every
  // disagreement one of its rows decided.
  { id: 'evidence.root-index', role: 'project-fact', kind: 'heading', text: 'Root index declarations' },
  { id: 'label.precedence-rows', role: 'project-fact', kind: 'label', text: 'Precedence rows admitted:' },
  { id: 'sentence.no-precedence', role: 'epistemic-disclosure', kind: 'sentence', text: 'No precedence table is admitted from the root index:' },
  { id: 'label.stated-counts', role: 'project-fact', kind: 'label', text: 'Stated counts:' },
  { id: 'sentence.no-stated-counts', role: 'epistemic-disclosure', kind: 'sentence', text: 'No stated summary count is admitted from the root index:' },
  { id: 'label.decided', role: 'project-fact', kind: 'label', text: 'Decided by a row:' },
  { id: 'sentence.no-decided', role: 'project-fact', kind: 'sentence', text: 'No disagreement between admitted declarations was decided by a row.' },
  { id: 'label.effective', role: 'project-fact', kind: 'label', text: 'effective' },
  { id: 'label.superseded', role: 'epistemic-disclosure', kind: 'label', text: 'superseded' },
  { id: 'table.layer', role: 'project-fact', kind: 'label', text: 'Layer' },
  { id: 'table.owns', role: 'project-fact', kind: 'label', text: 'Owns' },
  { id: 'table.home', role: 'project-fact', kind: 'label', text: 'Home' },
  { id: 'table.declared-at', role: 'project-fact', kind: 'label', text: 'Declared at' },
  { id: 'evidence.gaps', role: 'epistemic-disclosure', kind: 'heading', text: 'Unknown, by reason' },
  { id: 'evidence.code-structure', role: 'project-fact', kind: 'heading', text: 'Observed code structure' },
  { id: 'evidence.work-items', role: 'project-fact', kind: 'heading', text: 'Observed work items' },
  { id: 'evidence.relationships', role: 'project-fact', kind: 'heading', text: "How the capability's claims connect" },
  { id: 'evidence.relationships-lede', role: 'epistemic-disclosure', kind: 'lede', text: 'Each claim above stands alone; the links below say how far the evidence reaches between them.' },

  { id: 'table.key', role: 'project-fact', kind: 'label', text: 'Key' },
  { id: 'table.declared', role: 'project-fact', kind: 'label', text: 'Declared' },
  { id: 'table.epistemic-state', role: 'epistemic-disclosure', kind: 'label', text: 'Epistemic state' },
  { id: 'table.index', role: 'project-fact', kind: 'label', text: '#' },
  { id: 'table.source', role: 'project-fact', kind: 'label', text: 'Source' },
  { id: 'table.rule', role: 'project-fact', kind: 'label', text: 'Rule' },
  { id: 'table.outcome', role: 'project-fact', kind: 'label', text: 'Outcome' },
  { id: 'table.digest', role: 'project-fact', kind: 'label', text: 'Digest' },
  { id: 'table.items', role: 'project-fact', kind: 'label', text: 'Items' },

  { id: 'sentence.no-items', role: 'project-fact', kind: 'sentence', text: 'No items of this class were declared by any admitted source.' },
  { id: 'sentence.no-exclusions', role: 'project-fact', kind: 'sentence', text: 'No source body was excluded by the secret policy or a limit.' },
  { id: 'sentence.no-contradictions', role: 'project-fact', kind: 'sentence', text: 'No two admitted declarations disagree.' },
  { id: 'sentence.no-gaps', role: 'epistemic-disclosure', kind: 'sentence', text: 'Every project-shape claim above is Observed; no Unknown remains in the shape.' },
  { id: 'sentence.body-withheld', role: 'epistemic-disclosure', kind: 'sentence', text: 'The body is not shown anywhere.' },
  { id: 'sentence.no-body-read', role: 'epistemic-disclosure', kind: 'sentence', text: 'no body read' },
  { id: 'sentence.no-source-read', role: 'epistemic-disclosure', kind: 'sentence', text: 'No project-shape source was read.' },
  { id: 'sentence.not-evaluated', role: 'epistemic-disclosure', kind: 'sentence', text: 'No body-read authority evaluation reached this evaluation:' },
  { id: 'sentence.gate-refused', role: 'epistemic-disclosure', kind: 'sentence', text: 'The body-read gate refused' },
  { id: 'sentence.observer-failed', role: 'epistemic-disclosure', kind: 'sentence', text: 'The observer failed before any shape fact was read' },
  { id: 'sentence.missing-statement', role: 'epistemic-disclosure', kind: 'sentence', text: 'the shared model carries no statement for this key.' },
  { id: 'label.unknown', role: 'epistemic-disclosure', kind: 'label', text: 'Unknown' },
  { id: 'label.route', role: 'epistemic-disclosure', kind: 'label', text: 'Route:' },
  { id: 'label.also', role: 'epistemic-disclosure', kind: 'label', text: 'Also:' },
  { id: 'label.declarations-kept', role: 'epistemic-disclosure', kind: 'label', text: 'Declarations kept:' },
  { id: 'label.limit-breaches', role: 'project-fact', kind: 'label', text: 'Limit breaches:' },
  { id: 'label.authority', role: 'epistemic-disclosure', kind: 'label', text: 'Authority:' },
  { id: 'label.deferred', role: 'epistemic-disclosure', kind: 'label', text: 'deferred' },
  { id: 'label.no-route', role: 'epistemic-disclosure', kind: 'label', text: 'No route declared' },
  { id: 'label.evaluated-as', role: 'epistemic-disclosure', kind: 'label', text: 'evaluated as' },
  // PWB-REQ-021/022: the owner's cold-open walkthrough judgment, as carried.
  { id: 'evidence.walkthrough', role: 'epistemic-disclosure', kind: 'heading', text: 'Owner cold-open walkthrough judgment' },
  { id: 'sentence.judgment-not-evaluated', role: 'epistemic-disclosure', kind: 'sentence', text: 'No walkthrough run record and judgment pair reached this evaluation:' },
  { id: 'sentence.judgment-absent', role: 'epistemic-disclosure', kind: 'sentence', text: 'No owner judgment is carried' },
  { id: 'sentence.judgment-unlawful', role: 'epistemic-disclosure', kind: 'sentence', text: 'The recorded judgment is not lawful, so no verdict is carried:' },
  { id: 'label.judgment-evaluation', role: 'epistemic-disclosure', kind: 'label', text: 'Judgment evaluation' },
  { id: 'label.at', role: 'epistemic-disclosure', kind: 'label', text: 'at' },
  { id: 'label.outcome', role: 'epistemic-disclosure', kind: 'label', text: 'outcome' },
  { id: 'label.criterion', role: 'epistemic-disclosure', kind: 'label', text: '— criterion' },
  { id: 'label.contradiction', role: 'epistemic-disclosure', kind: 'label', text: 'Contradiction:' },
  { id: 'label.run-record', role: 'epistemic-disclosure', kind: 'label', text: 'Run record' },
  { id: 'label.judgment-digest', role: 'epistemic-disclosure', kind: 'label', text: 'judgment digest' },
  { id: 'label.verdict', role: 'epistemic-disclosure', kind: 'label', text: 'Verdict' },
  { id: 'label.judged-by', role: 'epistemic-disclosure', kind: 'label', text: 'judged by' },
  { id: 'label.independently-verified', role: 'epistemic-disclosure', kind: 'label', text: 'independently verified:' },
  { id: 'label.act', role: 'epistemic-disclosure', kind: 'label', text: 'Act' },
  { id: 'label.traversed', role: 'epistemic-disclosure', kind: 'label', text: 'traversed' },
  { id: 'label.rationale', role: 'epistemic-disclosure', kind: 'label', text: 'Rationale:' },
  // PWB-REQ-021 (amended 2026-09-05): readiness of the retained walkthrough
  // record — an execution fact, never a verdict or a score.
  { id: 'evidence.walkthrough-readiness', role: 'epistemic-disclosure', kind: 'heading', text: 'Walkthrough record readiness' },
  { id: 'sentence.readiness-not-evaluated', role: 'epistemic-disclosure', kind: 'sentence', text: 'Readiness was not assessed:' },
  { id: 'sentence.readiness-no-run-record', role: 'epistemic-disclosure', kind: 'sentence', text: 'No walkthrough run record to assess:' },
  { id: 'label.readiness', role: 'epistemic-disclosure', kind: 'label', text: 'Readiness:' },
  { id: 'sentence.readiness-execution-fact', role: 'epistemic-disclosure', kind: 'sentence', text: 'An execution fact about the record, not a verdict and not a score.' },
  { id: 'label.surface-version', role: 'epistemic-disclosure', kind: 'label', text: 'surface' },
  { id: 'label.evaluation-identity', role: 'epistemic-disclosure', kind: 'label', text: 'evaluation' },
  { id: 'label.readiness-findings', role: 'epistemic-disclosure', kind: 'label', text: 'Why not ready:' },
  { id: 'label.answers', role: 'epistemic-disclosure', kind: 'label', text: 'Recorded answers, in the owner’s words, unjudged:' },
  { id: 'label.sources', role: 'epistemic-disclosure', kind: 'label', text: 'Sources:' },
  { id: 'label.cited-authority', role: 'epistemic-disclosure', kind: 'label', text: 'Cited authority:' },
] as const satisfies readonly PolarisCopyRow[];

export type PolarisCopyId = (typeof POLARIS_COPY)[number]['id'];

const BY_ID: ReadonlyMap<string, PolarisCopyRow> = new Map(POLARIS_COPY.map((row) => [row.id, row]));

export function copyRow(id: PolarisCopyId): PolarisCopyRow {
  const row = BY_ID.get(id);
  if (row === undefined) throw new Error(`no Polaris copy row ${id}`);
  return row;
}

export function copyText(id: PolarisCopyId): string {
  return copyRow(id).text;
}

/** The attribute the human output exposes the role through. */
/** Default claim role per copy role (PWB-REQ-014): disclosures are
 * epistemic claims; everything else is non-normative framing unless a
 * renderer marks the unit as an anchored project fact. */
export const DEFAULT_CLAIM_ROLE: Readonly<Record<CopyRole, NarrativeClaimRole>> = {
  'project-fact': 'non-normative-framing',
  'epistemic-disclosure': 'epistemic-claim',
  'action-label': 'non-normative-framing',
  'scope-instruction': 'non-normative-framing',
};

export function roleAttr(role: CopyRole, claimRole: NarrativeClaimRole = DEFAULT_CLAIM_ROLE[role]): string {
  return ` data-copy-role="${role}"${claimRoleAttrs(claimRole)}`;
}

/** Attribute for the element carrying a table row: its role. */
export function copyAttr(id: PolarisCopyId): string {
  return roleAttr(copyRow(id).role);
}
