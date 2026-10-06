import { types } from 'node:util';
import { UNKNOWN_REASONS } from '@syzygy/cap1-core';
import { DIAGRAM_KINDS, QUOTE_LEAD_IN, SOURCE_ID_MAX_LENGTH, SOURCE_ID_MIN_LENGTH, SOURCE_ID_PATTERN } from '@syzygy/polaris-generation-core';
import { EXECUTION_SCOPES } from './execution-flags.js';

/** The local-agent draft schema (REQ-polaris-generation-034; design "The local-agent draft schema").
 *
 * The provider pipeline's draft (title, introduction, sections, diagrams, deep dives, unresolved) with the design's three changes:
 * every claim cites `{path, startLine, endLine}` at the pinned revision instead of a source id; every claim block carries a label
 * (`inferred`, `unknown` with an RFC2-24 reason, or `non-normative`) and the citations its label requires; and four new top-level
 * parts, `understanding`, `discovery`, `clarifications` and `executions`. A claim resting on the agent's building or running of the
 * observed project is `inferred` with `basis: execution` and names the executions it rests on. There is no `observed` label anywhere:
 * an agent cannot label its own claim Observed, and Observed is reserved for a quotation Syzygy verifies.
 *
 * One schema is written per run, because it carries the run's pinned revision and its clarification-question limit; its version is
 * fixed here. The schema checks shape only. Unique identities, resolving references, quotations, paths and ranges at the pinned
 * revision, and the execution marking against the executions list are `check`'s, over the frozen revision. */

/** v2: an execution's `workingDirectory` is optional and it may state its `scope` (v1.1, N6). */
export const LOCAL_DRAFT_SCHEMA_VERSION = 'polaris-dossier-local-draft-v2';

/** The understanding record's items, in REQ-polaris-generation-002's order. */
export const UNDERSTANDING_ITEMS = Object.freeze([
  'purpose', 'beneficiary', 'proposition', 'capabilities', 'components', 'choices',
  'tradeOffs', 'limits', 'terminology', 'contradictions', 'openQuestions',
] as const);

export const CLARIFICATION_ANSWER_KINDS = Object.freeze(['free-text', 'selected-interpretation', 'leave-unknown', 'defer'] as const);

export type DraftSchema =
  | { readonly type: 'object'; readonly properties: Readonly<Record<string, DraftSchema>>; readonly required: readonly string[]; readonly additionalProperties: false }
  | { readonly type: 'array'; readonly items: DraftSchema; readonly minItems: number; readonly maxItems: number; readonly uniqueItems?: true; readonly description?: string }
  | { readonly type: 'string'; readonly minLength: number; readonly maxLength: number; readonly pattern?: string; readonly enum?: readonly string[] }
  | { readonly type: 'integer'; readonly minimum: number; readonly maximum: number }
  | { readonly oneOf: readonly DraftSchema[] }
  | { readonly $ref: `#/$defs/${string}` };

/** The schema and the named definitions its `$ref`s point at. */
export interface DraftSchemaWithDefs { readonly root: DraftSchema; readonly defs: Readonly<Record<string, DraftSchema>> }

const ref = (name: string): DraftSchema => ({ $ref: `#/$defs/${name}` });

const text: DraftSchema = { type: 'string', minLength: 1, maxLength: 8000 };
const one = (value: string): DraftSchema => ({ type: 'string', minLength: 1, maxLength: value.length, enum: [value] });
const choice = (values: readonly string[]): DraftSchema => ({ type: 'string', minLength: 1, maxLength: Math.max(...values.map((v) => v.length)), enum: values });
const handle: DraftSchema = { type: 'string', minLength: SOURCE_ID_MIN_LENGTH, maxLength: SOURCE_ID_MAX_LENGTH, pattern: SOURCE_ID_PATTERN };
const list = (items: DraftSchema, minItems: number, maxItems: number): DraftSchema => ({ type: 'array', items, minItems, maxItems });
const refs = (minItems: number, maxItems: number): DraftSchema => ({ type: 'array', items: handle, minItems, maxItems, uniqueItems: true });
const object = (properties: Record<string, DraftSchema>, optional: readonly string[] = []): DraftSchema =>
  ({ type: 'object', properties, required: Object.keys(properties).filter((key) => !optional.includes(key)), additionalProperties: false });

/** A repository path as `git ls-tree` names it: relative, no NUL. Whether it names a blob is `check`'s. */
const repoPath: DraftSchema = { type: 'string', minLength: 1, maxLength: 1024, pattern: '^[^/\\u0000][^\\u0000]*$' };
const line: DraftSchema = { type: 'integer', minimum: 1, maximum: 10_000_000 };
const citations = (minItems: number): DraftSchema => list(ref('citation'), minItems, 50);
const reason = ref('unknownReason');

/** The one form a quotation takes, stated in a brief and in its schema's `quotations` description alike. `check` and `inventory-check`
 * count only this form; quoted text without the lead-in is the agent's prose. */
const quotationForm = (field: string, holder: string): string => `Write each quotation in ${holder}'s \`${field}\` with the lead-in and straight double quotes, exactly: ${QUOTE_LEAD_IN} "Each command runs to completion before the next one starts." The ${holder.replace(/^an? /u, '')}'s \`quotations\` names, in order, the citation each such quotation is taken from. Quoted text without the lead-in is your prose, not a quotation: Syzygy does not verify it and never renders it as Observed.`;
export const QUOTATION_FORM = quotationForm('text', 'a block');
export const INVENTORY_QUOTATION_FORM = quotationForm('statement', 'an entry');

/** A session's identifier, as that session declares it (REQ-polaris-generation-035): the draft, the inventory and each verdict carry
 * their own, and Syzygy compares them, never trusting any as observed. */
export const SESSION_ID_PATTERN = '^[A-Za-z0-9][A-Za-z0-9._:-]*$';
const sessionId: DraftSchema = { type: 'string', minLength: 1, maxLength: 200, pattern: SESSION_ID_PATTERN };
/** The brief's sentence on `sessionId`, for the draft and the inventory alike. */
export const SESSION_ID_RULE = (subject: 'draft' | 'inventory'): string => `Put this session's own identifier in \`sessionId\` (letters, digits and \`._:-\`, starting with a letter or digit): the identifier your agent tool gives this session, or, where it shows none, one you choose now and keep for every revision. ${subject === 'draft' ? 'The inventory and review sessions declare theirs, and Syzygy refuses one that equals yours' : 'Syzygy refuses an inventory whose identifier equals the authoring session\'s'}; every identifier is a session's own declaration, labelled Inferred.`;

/** The four claim forms. `quotations` lists, in order, the citation each `The project states: "…"` span in `text` is taken from. */
function claimForms(extra: Record<string, DraftSchema>): DraftSchema {
  const quotations: DraftSchema = { type: 'array', items: handle, minItems: 0, maxItems: 20, uniqueItems: true, description: QUOTATION_FORM };
  return { oneOf: [
    object({ id: handle, label: one('inferred'), basis: one('source'), text, citations: citations(1), quotations, ...extra }),
    object({ id: handle, label: one('inferred'), basis: one('execution'), executionIds: refs(1, 20), text, citations: citations(1), quotations, ...extra }),
    object({ id: handle, label: one('unknown'), reason, text, citations: citations(0), ...extra }),
    object({ id: handle, label: one('non-normative'), text, ...extra }),
  ] };
}
// One level of nesting, as in the provider draft: the parent summarizes its children.
const disposition: DraftSchema = { oneOf: [
  object({ kind: one('produced'), assetIds: refs(1, 50) }),
  object({ kind: one('omitted'), reason: text, citations: citations(0) }),
  object({ kind: one('unresolved'), reason: text, citations: citations(0) }),
] };
const epistemic = choice(['inferred', 'unknown']);
const understandingItem: DraftSchema = { oneOf: [
  object({ id: handle, label: one('inferred'), statement: text, scope: text, citations: citations(1) }),
  object({ id: handle, label: one('unknown'), reason, statement: text, scope: text, citations: citations(0) }),
] };
const pathReason = object({ path: repoPath, reason: text });

/** Shared definitions, written once in the document and reached by `$ref`. */
const DEFS: Readonly<Record<string, DraftSchema>> = Object.freeze({
  citation: object({ id: handle, path: repoPath, startLine: line, endLine: line }),
  unknownReason: choice(UNKNOWN_REASONS),
  paragraph: claimForms({}),
  block: claimForms({ children: list(ref('paragraph'), 0, 12) }),
  disposition,
  understandingItem,
  pathReason,
});

export interface DraftSchemaParameters {
  /** The run's pinned revision; the draft must name it. */
  readonly pinnedRevision: string;
  /** The declared clarification-question limit. */
  readonly maxQuestions: number;
}

export function localDraftSchema(parameters: DraftSchemaParameters): DraftSchemaWithDefs {
  if (!/^(?:[0-9a-f]{40}|[0-9a-f]{64})$/.test(parameters.pinnedRevision)) throw new Error('draft-schema: the pinned revision is not a commit identifier');
  if (!Number.isSafeInteger(parameters.maxQuestions) || parameters.maxQuestions < 0) throw new Error('draft-schema: the question limit is not a nonnegative integer');
  return { defs: DEFS, root: object({
    schemaVersion: one(LOCAL_DRAFT_SCHEMA_VERSION),
    pinnedRevision: one(parameters.pinnedRevision),
    sessionId,
    title: text,
    introduction: ref('paragraph'),
    understanding: object(Object.fromEntries(UNDERSTANDING_ITEMS.map((item) => [item, list(ref('understandingItem'), 1, 100)]))),
    sections: list(object({ id: handle, title: text, paragraphs: list(ref('block'), 1, 30), disposition: ref('disposition') }), 1, 30),
    diagrams: list(object({
      id: handle, title: text, sectionId: handle, kind: choice(DIAGRAM_KINDS), relationship: text,
      nodes: list(object({ id: handle, label: text, epistemic, citations: citations(1) }), 1, 40),
      edges: list(object({ id: handle, from: handle, to: handle, label: text, epistemic, citations: citations(1) }), 1, 80),
      disposition: ref('disposition'),
    }), 0, 20),
    deepDives: list(object({ id: handle, title: text, sectionId: handle, paragraphs: list(ref('block'), 1, 30), disposition: ref('disposition') }), 0, 30),
    unresolved: list(object({ id: handle, question: text, reason: text, citations: citations(0) }), 0, 100),
    discovery: object({
      inspected: list(repoPath, 0, 10_000),
      selected: list(ref('pathReason'), 0, 5_000),
      excluded: list(ref('pathReason'), 0, 5_000),
      // REQ-polaris-generation-036 names material the agent "could not resolve" beside what it excluded or deferred.
      unresolved: list(ref('pathReason'), 0, 5_000),
      deferred: list(ref('pathReason'), 0, 5_000),
      stoppingReason: text,
    }),
    clarifications: list(object({
      id: handle, question: text, evidence: citations(0), consequence: text, options: list(text, 0, 10),
      answer: text, answerKind: choice(CLARIFICATION_ANSWER_KINDS), attribution: one('operator'),
    }), 0, parameters.maxQuestions),
    // REQ-polaris-generation-033 (v1.1, N6): a command is admitted whether or not it carries its working directory and scope; where
    // execution was permitted, Syzygy flags one without them or outside the clone or scope (execution-flags.ts), and refuses nothing.
    executions: list(object({ id: handle, command: text, workingDirectory: text, scope: choice(EXECUTION_SCOPES), purpose: text }, ['workingDirectory', 'scope']), 0, 500),
  }) };
}

/** The schema as the JSON Schema document written to `draft.schema.json`. The internal form already uses JSON Schema's keywords. */
export function draftSchemaDocument(parameters: DraftSchemaParameters): Record<string, unknown> {
  const { root, defs } = localDraftSchema(parameters);
  return {
    $schema: 'https://json-schema.org/draft/2020-12/schema',
    $id: `urn:syzygy:polaris-dossier:${LOCAL_DRAFT_SCHEMA_VERSION}`,
    title: `Polaris dossier local-agent draft (${LOCAL_DRAFT_SCHEMA_VERSION})`,
    ...root,
    $defs: defs,
  };
}

/** The local-agent inventory schema (REQ-polaris-generation-035, 006). The inventory session prepares it from the clone without the
 * draft: entries of what the project states, in REQ-polaris-generation-006's kinds, each `inferred` with path and line-range citations
 * or `unknown` with an RFC2-24 reason, quotations in the one lead-in form, and its own account of what it covered. Syzygy checks its
 * quotations and citations as `check` checks a draft's; its completeness over the clone stays the session's self-report, Inferred. */
export const LOCAL_INVENTORY_SCHEMA_VERSION = 'polaris-dossier-local-inventory-v1';
export const INVENTORY_ENTRY_KINDS = Object.freeze(['purpose', 'beneficiary', 'thesis', 'capability', 'choice', 'term', 'qualification', 'conflict', 'other'] as const);

const INVENTORY_DEFS: Readonly<Record<string, DraftSchema>> = Object.freeze({
  citation: DEFS['citation']!,
  unknownReason: DEFS['unknownReason']!,
  pathReason,
  entry: { oneOf: [
    object({ id: handle, kind: choice(INVENTORY_ENTRY_KINDS), label: one('inferred'), statement: text, citations: citations(1),
      quotations: { type: 'array', items: handle, minItems: 0, maxItems: 20, uniqueItems: true, description: INVENTORY_QUOTATION_FORM } }),
    object({ id: handle, kind: choice(INVENTORY_ENTRY_KINDS), label: one('unknown'), reason, statement: text, citations: citations(0) }),
  ] },
});

export function localInventorySchema(parameters: { readonly pinnedRevision: string }): DraftSchemaWithDefs {
  if (!/^(?:[0-9a-f]{40}|[0-9a-f]{64})$/.test(parameters.pinnedRevision)) throw new Error('draft-schema: the pinned revision is not a commit identifier');
  return { defs: INVENTORY_DEFS, root: object({
    schemaVersion: one(LOCAL_INVENTORY_SCHEMA_VERSION),
    pinnedRevision: one(parameters.pinnedRevision),
    sessionId,
    entries: list(ref('entry'), 1, 2000),
    coverage: object({
      inspected: list(repoPath, 0, 10_000),
      excluded: list(ref('pathReason'), 0, 5_000),
      deferred: list(ref('pathReason'), 0, 5_000),
      stoppingReason: text,
    }),
  }) };
}

/** The inventory schema as the JSON Schema document the inventory brief carries. */
export function inventorySchemaDocument(parameters: { readonly pinnedRevision: string }): Record<string, unknown> {
  const { root, defs } = localInventorySchema(parameters);
  return {
    $schema: 'https://json-schema.org/draft/2020-12/schema',
    $id: `urn:syzygy:polaris-dossier:${LOCAL_INVENTORY_SCHEMA_VERSION}`,
    title: `Polaris dossier local-agent inventory (${LOCAL_INVENTORY_SCHEMA_VERSION})`,
    ...root,
    $defs: defs,
  };
}

/** The local-agent fidelity verdict schema (REQ-polaris-generation-035, 006). The review session writes it from its packet alone: the
 * packet's digest, its own session identifier, coverage of every inventory entry by the draft, support of every claim block by the
 * packet's spans, the accuracy of every inventory entry against those spans, and every finding with its severity and its deficient
 * subject. A quotation in a `reason` or `message` takes the lead-in form and names, in `quotations`, the packet span it is taken from. */
export const LOCAL_FIDELITY_VERDICT_SCHEMA_VERSION = 'polaris-dossier-local-fidelity-verdict-v1';
export const DEFICIENT_SUBJECTS = Object.freeze(['discovery', 'understanding', 'clarification', 'argument', 'prose', 'asset', 'rendering'] as const);
export const VERDICT_QUOTATION_FORM = `Write each quotation in a \`reason\` or \`message\` with the lead-in and straight double quotes, exactly: ${QUOTE_LEAD_IN} "Each command runs to completion before the next one starts." The row's \`quotations\` names, in order, the packet span each such quotation is taken from. Quoted text without the lead-in is your prose, not a quotation.`;

export function localVerdictSchema(parameters: { readonly pinnedRevision: string }): DraftSchemaWithDefs {
  if (!/^(?:[0-9a-f]{40}|[0-9a-f]{64})$/.test(parameters.pinnedRevision)) throw new Error('draft-schema: the pinned revision is not a commit identifier');
  const quotations: DraftSchema = { type: 'array', items: handle, minItems: 0, maxItems: 20, uniqueItems: true, description: VERDICT_QUOTATION_FORM };
  return { defs: {}, root: object({
    schemaVersion: one(LOCAL_FIDELITY_VERDICT_SCHEMA_VERSION),
    pinnedRevision: one(parameters.pinnedRevision),
    packetSha256: { type: 'string', minLength: 64, maxLength: 64, pattern: '^[0-9a-f]{64}$' },
    sessionId,
    inventoryCoverage: list(object({
      entryId: handle, disposition: choice(['represented', 'justified-omission', 'unsupported', 'unresolved']), blockIds: refs(0, 5000), reason: text, quotations,
    }), 1, 5000),
    inventoryAccuracy: list(object({ entryId: handle, accuracy: choice(['accurate', 'inaccurate', 'unresolved']), spanIds: refs(0, 200), reason: text, quotations }), 1, 5000),
    blockSupport: list(object({
      blockId: handle, verdict: choice(['supported', 'anchor-does-not-support', 'unresolved']), spanIds: refs(0, 200), reason: text, quotations,
    }), 1, 5000),
    findings: list(object({ severity: choice(['blocking', 'advisory']), subject: choice(DEFICIENT_SUBJECTS), target: handle, message: text, quotations }), 0, 1000),
    readiness: choice(['ready', 'not-ready']),
  }) };
}

/** The verdict schema as the JSON Schema document the fidelity packet carries. */
export function verdictSchemaDocument(parameters: { readonly pinnedRevision: string }): Record<string, unknown> {
  const { root } = localVerdictSchema(parameters);
  return {
    $schema: 'https://json-schema.org/draft/2020-12/schema',
    $id: `urn:syzygy:polaris-dossier:${LOCAL_FIDELITY_VERDICT_SCHEMA_VERSION}`,
    title: `Polaris dossier local-agent fidelity verdict (${LOCAL_FIDELITY_VERDICT_SCHEMA_VERSION})`,
    ...root,
  };
}

/** The local-agent rendered-design verdict schema (REQ-polaris-generation-035, 006). The design review session writes it from its packet
 * alone: the packet's digest, its own session identifier, a judgement of every HTML page of the render, and every finding with its
 * severity, its deficient subject and the page it concerns. It quotes nothing: no span of the design packet verifies a quotation. */
export const LOCAL_DESIGN_VERDICT_SCHEMA_VERSION = 'polaris-dossier-local-design-verdict-v1';
export const DESIGN_PAGE_VERDICTS = Object.freeze(['acceptable', 'deficient', 'unresolved'] as const);

export function localDesignVerdictSchema(parameters: { readonly pinnedRevision: string }): DraftSchemaWithDefs {
  if (!/^(?:[0-9a-f]{40}|[0-9a-f]{64})$/.test(parameters.pinnedRevision)) throw new Error('draft-schema: the pinned revision is not a commit identifier');
  return { defs: {}, root: object({
    schemaVersion: one(LOCAL_DESIGN_VERDICT_SCHEMA_VERSION),
    pinnedRevision: one(parameters.pinnedRevision),
    packetSha256: { type: 'string', minLength: 64, maxLength: 64, pattern: '^[0-9a-f]{64}$' },
    sessionId,
    pageReview: list(object({ page: repoPath, verdict: choice(DESIGN_PAGE_VERDICTS), reason: text }), 1, 20_000),
    findings: list(object({ severity: choice(['blocking', 'advisory']), subject: choice(DEFICIENT_SUBJECTS), page: repoPath, message: text }), 0, 1000),
    readiness: choice(['ready', 'not-ready']),
  }) };
}

/** The design verdict schema as the JSON Schema document the design packet carries. */
export function designVerdictSchemaDocument(parameters: { readonly pinnedRevision: string }): Record<string, unknown> {
  const { root } = localDesignVerdictSchema(parameters);
  return {
    $schema: 'https://json-schema.org/draft/2020-12/schema',
    $id: `urn:syzygy:polaris-dossier:${LOCAL_DESIGN_VERDICT_SCHEMA_VERSION}`,
    title: `Polaris dossier local-agent rendered-design verdict (${LOCAL_DESIGN_VERDICT_SCHEMA_VERSION})`,
    ...root,
  };
}

export interface DraftSchemaError { readonly path: string; readonly detail: string }

const MAX_ERRORS = 50;

/** Check a parsed draft against the schema; every error names the JSON path to repair. Only own, enumerable data properties of plain
 * objects and arrays count; a proxy, accessor or symbol key is refused. */
export function checkDraftShape(schema: DraftSchemaWithDefs, value: unknown): readonly DraftSchemaError[] {
  const errors: DraftSchemaError[] = [];
  visit(schema.defs, schema.root, value, '$', errors);
  return errors.slice(0, MAX_ERRORS);
}

function resolve(defs: DraftSchemaWithDefs['defs'], schema: DraftSchema): DraftSchema {
  if (!('$ref' in schema)) return schema;
  const name = schema.$ref.slice('#/$defs/'.length);
  if (!Object.hasOwn(defs, name)) throw new Error(`draft-schema: no definition ${name}`);
  return defs[name]!;
}

function visit(defs: DraftSchemaWithDefs['defs'], reference: DraftSchema, value: unknown, at: string, errors: DraftSchemaError[]): void {
  if (errors.length >= MAX_ERRORS) return;
  const schema = resolve(defs, reference);
  if ('$ref' in schema) throw new Error('draft-schema: a definition is itself a reference');
  if ('oneOf' in schema) {
    const attempts = schema.oneOf.map((arm) => { const found: DraftSchemaError[] = []; visit(defs, arm, value, at, found); return { arm: resolve(defs, arm), found }; });
    if (attempts.some((attempt) => attempt.found.length === 0)) return;
    // Report against the form the value names by its single-valued fields (label, basis, kind), or say it names none.
    const named = attempts.filter((attempt) => discriminatorsMatch(attempt.arm, value));
    if (named.length === 1) { errors.push(...named[0]!.found); return; }
    errors.push({ path: at, detail: `matches none of the permitted forms (${schema.oneOf.map(describeForm).join('; ')})` });
    return;
  }
  if (schema.type === 'string') {
    if (typeof value !== 'string') { errors.push({ path: at, detail: 'must be a string' }); return; }
    const length = [...value].length;
    if (length < schema.minLength || length > schema.maxLength) errors.push({ path: at, detail: `must be ${schema.minLength} to ${schema.maxLength} characters; is ${length}` });
    else if (schema.enum && !schema.enum.includes(value)) errors.push({ path: at, detail: `must be one of ${schema.enum.join(', ')}` });
    else if (schema.pattern && !new RegExp(schema.pattern, 'u').test(value)) errors.push({ path: at, detail: `must match ${schema.pattern}` });
    return;
  }
  if (schema.type === 'integer') {
    if (typeof value !== 'number' || !Number.isSafeInteger(value) || value < schema.minimum || value > schema.maximum) {
      errors.push({ path: at, detail: `must be an integer from ${schema.minimum} to ${schema.maximum}` });
    }
    return;
  }
  if (typeof value !== 'object' || value === null || types.isProxy(value)) { errors.push({ path: at, detail: `must be ${schema.type === 'array' ? 'an array' : 'an object'}` }); return; }
  const descriptors = Object.getOwnPropertyDescriptors(value);
  if (Reflect.ownKeys(descriptors).some((key) => typeof key !== 'string' || !('value' in descriptors[key]!))) { errors.push({ path: at, detail: 'carries a symbol key or an accessor' }); return; }
  if (schema.type === 'array') {
    if (!Array.isArray(value) || Object.keys(descriptors).length !== value.length + 1) { errors.push({ path: at, detail: 'must be an array' }); return; }
    if (value.length < schema.minItems || value.length > schema.maxItems) errors.push({ path: at, detail: `must hold ${schema.minItems} to ${schema.maxItems} items; holds ${value.length}` });
    for (let i = 0; i < value.length && errors.length < MAX_ERRORS; i++) visit(defs, schema.items, descriptors[String(i)]!.value, `${at}[${i}]`, errors);
    if (schema.uniqueItems && new Set(value).size !== value.length) errors.push({ path: at, detail: 'must not repeat an item' });
    return;
  }
  if (Array.isArray(value) || (Object.getPrototypeOf(value) !== Object.prototype && Object.getPrototypeOf(value) !== null)) { errors.push({ path: at, detail: 'must be an object' }); return; }
  for (const key of Object.keys(descriptors)) {
    if (!Object.hasOwn(schema.properties, key)) errors.push({ path: `${at}.${key}`, detail: 'is not a field of this form' });
    else if (!descriptors[key]!.enumerable) errors.push({ path: `${at}.${key}`, detail: 'is not enumerable' });
  }
  for (const key of Object.keys(schema.properties)) {
    if (Object.hasOwn(descriptors, key)) visit(defs, schema.properties[key]!, descriptors[key]!.value, `${at}.${key}`, errors);
    else if (schema.required.includes(key)) errors.push({ path: `${at}.${key}`, detail: 'is required' });
  }
}

function singleValued(arm: DraftSchema): [string, string][] {
  if (!('type' in arm) || arm.type !== 'object') return [];
  return Object.entries(arm.properties).flatMap(([key, field]) =>
    'type' in field && field.type === 'string' && field.enum?.length === 1 ? [[key, field.enum[0]!] as [string, string]] : []);
}

function discriminatorsMatch(arm: DraftSchema, value: unknown): boolean {
  if (typeof value !== 'object' || value === null || Array.isArray(value) || types.isProxy(value)) return false;
  const fixed = singleValued(arm);
  return fixed.length > 0 && fixed.every(([key, expected]) => {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    return descriptor !== undefined && 'value' in descriptor && descriptor.value === expected;
  });
}

function describeForm(arm: DraftSchema): string {
  const fixed = singleValued(arm);
  return fixed.length > 0 ? fixed.map(([key, expected]) => `${key} ${expected}`).join(', ') : 'unnamed';
}
