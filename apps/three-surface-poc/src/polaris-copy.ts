/**
 * Every fixed owner-visible Polaris string, with exactly one role from the
 * closed PWB-REQ-012 set. The renderer takes text from this table and
 * marks the element that carries it with `data-copy-role`; the human output
 * exposes the role through that attribute and the machine side is this
 * table itself. Templated sentences (a count, a reason, a path) are not
 * rows — their carrying element still declares the role, and the oracle in
 * `polaris-copy.test.ts` sweeps the rendered text, not this table.
 */
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
  { id: 'shell.lede', role: 'scope-instruction', kind: 'lede', text: 'Purpose, promises, boundaries, architecture and V1 first; then the catalog; then one capability in depth.' },
  { id: 'notice', role: 'epistemic-disclosure', kind: 'notice', text: 'Every positive claim below cites its source. Where evidence is absent, Unknown is stated in place with its route to resolution.' },

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

  { id: 'capability.scope', role: 'scope-instruction', kind: 'sentence', text: "This is one capability within the complete catalog above, not the project's declared shape. Its claims keep their own provenance and epistemic state." },

  { id: 'evidence.observation', role: 'project-fact', kind: 'heading', text: 'Project-shape observation' },
  { id: 'evidence.sources', role: 'project-fact', kind: 'heading', text: 'Project-shape sources' },
  { id: 'evidence.exclusions', role: 'project-fact', kind: 'heading', text: 'Excluded bodies' },
  { id: 'evidence.contradictions', role: 'project-fact', kind: 'heading', text: 'Contradicted facts' },
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
export function roleAttr(role: CopyRole): string {
  return ` data-copy-role="${role}"`;
}

/** Attribute for the element carrying a table row: its role. */
export function copyAttr(id: PolarisCopyId): string {
  return roleAttr(copyRow(id).role);
}
