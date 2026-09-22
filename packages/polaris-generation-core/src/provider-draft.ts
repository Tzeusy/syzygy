import { types } from 'node:util';
import type { GenerationStage } from './prompts.js';

// Provider-local intermediate records only. These neither mint identities nor
// implement the authored asset bundle, source admission or semantic review.
// Coverage lists record what the reviewer claims to have checked; they cannot
// prove entailment or inventory completeness beyond the source denominator.
// Plain strings remain inert, including markup-looking text; renderers must
// escape them. This schema provides no executable markup or external link role.
type Schema = { type: 'object'; properties: Record<string, Schema>; required: string[]; additionalProperties: false }
  | { type: 'array'; items: Schema; minItems: number; maxItems: number; uniqueItems?: boolean }
  | { type: 'string'; minLength: number; maxLength: number; pattern?: string; enum?: string[] }
  | { oneOf: readonly Schema[] };
const text: Schema = { type: 'string', minLength: 1, maxLength: 8000 };
const handle: Schema = { type: 'string', minLength: 1, maxLength: 100, pattern: '^[A-Za-z0-9][A-Za-z0-9_.:-]*$' };
const list = (items: Schema, minItems = 0, maxItems = 200): Extract<Schema, { type: 'array' }> => ({ type: 'array', items, minItems, maxItems });
const object = (properties: Record<string, Schema>): Schema => ({ type: 'object', properties, required: Object.keys(properties), additionalProperties: false });
const refs: Schema = { ...list(handle, 1), uniqueItems: true };
const paragraph = object({ id: handle, text, sourceIds: refs });
const disposition: Schema = { oneOf: [
  object({ kind: { ...text, enum: ['produced'] }, assetIds: refs }),
  object({ kind: { ...text, enum: ['omitted'] }, reason: text, references: refs }),
  object({ kind: { ...text, enum: ['unresolved'] }, reason: text, references: refs }),
] };
const inventory = object({ entries: list(object({ id: handle, sourceIds: refs, statement: text, kind: { ...text, enum: ['purpose', 'beneficiary', 'thesis', 'capability', 'choice', 'term', 'qualification', 'conflict', 'other'] }, disposition }), 1) });
const plan = object({ sections: list(object({ id: handle, title: text, reason: text, sourceIds: refs, disposition }), 1, 30) });
const draft = object({
  title: text, introduction: paragraph,
  sections: list(object({ id: handle, title: text, paragraphs: list(paragraph, 1, 30), disposition }), 1, 30),
  diagrams: list(object({ id: handle, title: text, sectionId: handle,
    nodes: list(object({ id: handle, label: text, sourceIds: refs }), 1, 40),
    edges: list(object({ id: handle, from: handle, to: handle, label: text, sourceIds: refs }), 1, 80),
    disposition,
  }), 0, 20),
  deepDives: list(object({ id: handle, title: text, sectionId: handle, paragraphs: list(paragraph, 1, 30), disposition }), 0, 30),
  unresolved: list(object({ question: text, reason: text, references: refs }), 0, 100),
});
const inventoryCoverage = list(object({ entryId: handle, disposition: { ...text, enum: ['represented', 'justified-omission', 'unsupported', 'unresolved'] }, blockIds: list(handle, 0, 5000), reason: text }), 1, 5000);
const blockSupport = list(object({ blockId: handle, verdict: { ...text, enum: ['supported', 'anchor-does-not-support', 'unresolved'] }, sourceIds: list(handle, 0, 200), reason: text }), 1, 5000);
const fidelity = object({ inventoryCoverage, blockSupport,
  findings: list(object({ severity: { ...text, enum: ['blocking', 'advisory'] }, message: text, target: handle }), 0, 1000),
});
const schemas: Record<GenerationStage, Schema> = { inventory, plan, author: draft, edit: draft, repair: draft, fidelity };

export function stageSchema(stage: GenerationStage): { version: string; schema: Schema } {
  if (!Object.hasOwn(schemas, stage)) throw new Error('invalid-stage');
  return { version: `polaris-provider-${stage}-v1`, schema: structuredClone(schemas[stage]) };
}

function check(schema: Schema, value: unknown): void {
  if ('oneOf' in schema) {
    for (const candidate of schema.oneOf) {
      try { check(candidate, value); return; } catch { /* try next closed arm */ }
    }
    throw new Error('invalid-disposition');
  }
  if (schema.type === 'string') {
    if (typeof value !== 'string' || [...value].length < schema.minLength || [...value].length > schema.maxLength
      || (schema.pattern && !new RegExp(schema.pattern, 'u').test(value))
      || (schema.enum && !schema.enum.includes(value))) throw new Error('invalid-string');
    return;
  }
  if (typeof value !== 'object' || value === null || types.isProxy(value)) throw new Error('invalid-structure');
  const descriptors = Object.getOwnPropertyDescriptors(value);
  if (Reflect.ownKeys(descriptors).some(key => typeof key !== 'string' || !('value' in descriptors[key]!))) throw new Error('invalid-property');
  if (schema.type === 'array') {
    if (!Array.isArray(value) || value.length < schema.minItems || value.length > schema.maxItems
      || Object.keys(descriptors).length !== value.length + 1) throw new Error('invalid-array');
    for (let i = 0; i < value.length; i++) {
      if (!Object.hasOwn(descriptors, String(i))) throw new Error('invalid-array');
      check(schema.items, descriptors[String(i)]!.value);
    }
    if (schema.uniqueItems && new Set(value).size !== value.length) throw new Error('duplicate-reference');
    return;
  }
  if (Object.getPrototypeOf(value) !== Object.prototype && Object.getPrototypeOf(value) !== null) throw new Error('invalid-object');
  const keys = Object.keys(descriptors);
  if (keys.length !== schema.required.length || schema.required.some(key => !Object.hasOwn(descriptors, key))
    || keys.some(key => !Object.hasOwn(schema.properties, key) || !descriptors[key]!.enumerable)) throw new Error('invalid-fields');
  for (const key of keys) check(schema.properties[key]!, descriptors[key]!.value);
}

export interface ProviderParagraph { id: string; text: string; sourceIds: string[] }
export type AssetDisposition =
  | { kind: 'produced'; assetIds: string[] }
  | { kind: 'omitted'; reason: string; references: string[] }
  | { kind: 'unresolved'; reason: string; references: string[] };
export interface ProviderInventory { entries: { id: string; sourceIds: string[]; statement: string; kind: 'purpose' | 'beneficiary' | 'thesis' | 'capability' | 'choice' | 'term' | 'qualification' | 'conflict' | 'other'; disposition: AssetDisposition }[] }
export interface ProviderPlan { sections: { id: string; title: string; reason: string; sourceIds: string[]; disposition: AssetDisposition }[] }
export interface ProviderDraft {
  title: string;
  introduction: ProviderParagraph;
  sections: { id: string; title: string; paragraphs: ProviderParagraph[]; disposition: AssetDisposition }[];
  diagrams: { id: string; title: string; sectionId: string;
    nodes: { id: string; label: string; sourceIds: string[] }[];
    edges: { id: string; from: string; to: string; label: string; sourceIds: string[] }[]; disposition: AssetDisposition }[];
  deepDives: { id: string; title: string; sectionId: string; paragraphs: ProviderParagraph[]; disposition: AssetDisposition }[];
  unresolved: { question: string; reason: string; references: string[] }[];
}
export interface ProviderInventoryCoverage { entryId: string; disposition: 'represented' | 'justified-omission' | 'unsupported' | 'unresolved'; blockIds: string[]; reason: string }
export interface ProviderBlockSupport { blockId: string; verdict: 'supported' | 'anchor-does-not-support' | 'unresolved'; sourceIds: string[]; reason: string }
export interface ProviderReview { inventoryCoverage: ProviderInventoryCoverage[]; blockSupport: ProviderBlockSupport[]; findings: { severity: 'blocking' | 'advisory'; message: string; target: string }[] }

function unique(values: string[]): Set<string> {
  const set = new Set(values);
  if (set.size !== values.length) throw new Error('duplicate-handle');
  return set;
}
function same(actual: string[], expected: Set<string>): void {
  const set = unique(actual);
  if (set.size !== expected.size || [...set].some(id => !expected.has(id))) throw new Error('incomplete-coverage');
}
function references(value: unknown, sources: Set<string>): void {
  if (Array.isArray(value)) {
    for (const child of value) references(child, sources);
  } else if (value !== null && typeof value === 'object') {
    const record = value as Record<string, unknown>;
    if (Array.isArray(record.sourceIds) && record.sourceIds.some(id => !sources.has(id))) throw new Error('unknown-source');
    for (const child of Object.values(record)) references(child, sources);
  }
}
function draftHandles(value: ProviderDraft): { all: Set<string>; blocks: Set<string> } {
  const blocks = [value.introduction, ...value.sections.flatMap(s => s.paragraphs),
    ...value.diagrams.flatMap(d => [...d.nodes, ...d.edges]),
    ...value.deepDives.flatMap(d => d.paragraphs)].map(b => b.id);
  return { blocks: unique(blocks), all: unique([...blocks, ...value.sections.map(s => s.id),
    ...value.diagrams.map(d => d.id), ...value.deepDives.map(d => d.id)]) };
}

export function validateStage(stage: GenerationStage, value: unknown, context: Record<string, unknown>): unknown {
  check(stageSchema(stage).schema, value);
  const sourceSchema = list(object({ sourceId: handle, text: { type: 'string', minLength: 1, maxLength: 100000 } }), 1);
  check(sourceSchema, context.sources);
  const sources = unique((context.sources as { sourceId: string; text: string }[]).map(s => s.sourceId));
  references(value, sources);
  if (stage === 'inventory') {
    const data = value as ProviderInventory;
    unique(data.entries.map((entry) => entry.id));
    same([...new Set<string>(data.entries.flatMap((entry) => entry.sourceIds))], sources);
  } else if (stage === 'plan') {
    const data = value as ProviderPlan;
    validateStage('inventory', context.inventory, { sources: context.sources });
    unique(data.sections.map((section) => section.id));
  } else if (stage === 'fidelity') {
    const data = value as ProviderReview;
    validateStage('inventory', context.inventory, { sources: context.sources });
    validateStage('author', context.draft, { sources: context.sources, plan: context.plan });
    const inv = context.inventory as ProviderInventory;
    const handles = draftHandles(context.draft as ProviderDraft);
    same(data.inventoryCoverage.map((row) => row.entryId), unique(inv.entries.map((entry) => entry.id)));
    same(data.blockSupport.map((row) => row.blockId), handles.blocks);
    if (data.inventoryCoverage.some((row) => row.disposition !== 'represented' && row.reason.length === 0)) throw new Error('missing-coverage-reason');
    if (data.inventoryCoverage.some((row) => row.disposition !== 'represented' && row.blockIds.length > 0)) throw new Error('invalid-coverage-blocks');
    if (data.blockSupport.some((row) => row.verdict !== 'supported' && row.reason.length === 0)) throw new Error('missing-support-reason');
    const targets = new Set([...sources, ...handles.all, ...data.inventoryCoverage.map((row) => row.entryId), ...data.blockSupport.map((row) => row.blockId)]);
    if (data.findings.some((finding) => !targets.has(finding.target))) throw new Error('unknown-finding-target');
  } else {
    const data = value as ProviderDraft;
    check(plan, context.plan);
    references(context.plan, sources);
    draftHandles(data);
    const handles = draftHandles(data);
    const planned = (context.plan as ProviderPlan).sections.flatMap((section) => section.disposition.kind === 'produced' ? section.disposition.assetIds : []);
    const produced = [
      ...planned,
      ...data.sections.flatMap((section) => section.disposition.kind === 'produced' ? section.disposition.assetIds : []),
      ...data.diagrams.flatMap((asset) => asset.disposition.kind === 'produced' ? asset.disposition.assetIds : []),
      ...data.deepDives.flatMap((asset) => asset.disposition.kind === 'produced' ? asset.disposition.assetIds : []),
    ];
    if (produced.some((id) => !handles.all.has(id))) throw new Error('unknown-asset');
    const sections = unique(data.sections.map((s) => s.id));
    same([...sections], unique((context.plan as ProviderPlan).sections.map((s) => s.id)));
    for (const diagram of data.diagrams) {
      if (!sections.has(diagram.sectionId)) throw new Error('unknown-section');
      const nodes = new Set(diagram.nodes.map((n) => n.id));
      if (diagram.edges.some((e) => !nodes.has(e.from) || !nodes.has(e.to))) throw new Error('unknown-node');
    }
    if (data.deepDives.some((d) => !sections.has(d.sectionId))) throw new Error('unknown-section');
  }
  return structuredClone(value);
}

export function reviewVerdict(review: unknown): { blocking: boolean; findings: unknown[] } {
  check(fidelity, review);
  const findings = (review as ProviderReview).findings;
  const data = review as ProviderReview;
  const coverageBlocking = data.inventoryCoverage.some((row) => row.disposition !== 'represented' && row.disposition !== 'justified-omission');
  const supportBlocking = data.blockSupport.some((row) => row.verdict !== 'supported');
  return { blocking: coverageBlocking || supportBlocking || findings.some((finding) => finding.severity === 'blocking'), findings: structuredClone(findings) };
}
