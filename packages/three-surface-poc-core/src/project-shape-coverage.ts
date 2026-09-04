// PWB-REQ-002 / PWB-REQ-004 — coverage as data, contradictions preserved.
//
// Two populations. The source-path population comes from the manifest and
// never shrinks: every source is listed with either a known item
// denominator or an Unknown one carrying the classifier's fixed reason. The
// item population is the union of every admitted source's extracted items;
// each identity `(class, key)` appears exactly once in exactly one of the
// three states modeled / unknown / contradicted, so per class
// modeled + unknown + contradicted equals the declared count.
//
// Facts are reconciled from declarations. Two declarations of one fact that
// disagree — or two declarations of one item identity, whatever their
// values — are a conflict. A conflict is resolved only by a precedence rule
// that Butlers itself declares and that the model can cite by an anchor in
// the admitted source population; otherwise both declarations are retained
// and the fact is Unknown with reason `contradicted-pending-adjudication`
// (RFC2-24 verbatim). Nothing here ever drops a declaration.

import {
  type ClassifiedSource,
  type ClassificationRecord,
  type FixedUnknown,
  PWB_SECRET_POLICY,
  type SecretClassificationPolicy,
  parseFailureExclusion,
} from './content-classification.js';
import { EXTRACTION_CLASSES, type ExtractionClass, type ManifestSource } from './project-shape-manifest.js';
import type { ExtractedItem, ExtractionFailureRecord, SourceExtraction } from './project-shape-extraction.js';

// ---------------------------------------------------------------------
// Vocabulary.

export const COVERAGE_STATES = ['modeled', 'unknown', 'contradicted'] as const;
export type CoverageState = (typeof COVERAGE_STATES)[number];

// RFC2-24 reasons this module can emit, spelled verbatim.
export const CONTRADICTED_REASON = 'contradicted-pending-adjudication' as const;

export const DECLARATION_BASES = ['extracted-item', 'derived-count', 'stated-summary'] as const;
export type DeclarationBasis = (typeof DECLARATION_BASES)[number];

export interface DeclarationAnchor {
  readonly path: string;
  readonly line?: number;
  readonly contentDigest?: string;
}

export interface Declaration {
  // The fact declared: `item:<class>:<key>` for identities, `count:<class>`
  // for per-class counts, or a fixture-supplied fact name.
  readonly fact: string;
  readonly value: string;
  readonly basis: DeclarationBasis;
  readonly anchors: readonly DeclarationAnchor[];
}

// A precedence rule Butlers declares. `anchor` is where Butlers says it;
// the rule is applicable only when that path is in the admitted source
// population and exactly one declaration matches each side.
export type RuleSelector = { readonly path: string } | { readonly basis: DeclarationBasis };

export interface PrecedenceRule {
  readonly id: string;
  readonly anchor: DeclarationAnchor;
  // The rule's own words, as declared.
  readonly statement: string;
  readonly higher: RuleSelector;
  readonly lower: RuleSelector;
  // When present, the rule applies only to these facts.
  readonly facts?: readonly string[];
}

export const RULE_REJECTIONS = [
  'anchor-not-in-population',
  'fact-out-of-scope',
  'higher-side-unmatched',
  'lower-side-unmatched',
  'side-matched-more-than-once',
  'same-declaration-both-sides',
] as const;
export type RuleRejection = (typeof RULE_REJECTIONS)[number];

export interface PrecedenceCitation {
  readonly ruleId: string;
  readonly anchor: DeclarationAnchor;
  readonly statement: string;
}

export interface ConsideredRule {
  readonly ruleId: string;
  readonly outcome: 'applied' | RuleRejection;
}

export type ReconciledFact =
  | {
      readonly fact: string;
      readonly state: 'modeled';
      readonly value: string;
      readonly declarations: readonly Declaration[];
      // Present only when declarations disagreed and one rule decided.
      readonly disagreement?: {
        readonly effective: Declaration;
        readonly superseded: readonly Declaration[];
        readonly precedence: PrecedenceCitation;
      };
      readonly rulesConsidered: readonly ConsideredRule[];
    }
  | {
      readonly fact: string;
      readonly state: 'contradicted';
      readonly declarations: readonly Declaration[];
      readonly unknownReason: typeof CONTRADICTED_REASON;
      readonly rulesConsidered: readonly ConsideredRule[];
    }
  | {
      readonly fact: string;
      readonly state: 'unknown';
      readonly declarations: readonly Declaration[];
      readonly unknownReason: string;
      readonly rulesConsidered: readonly ConsideredRule[];
    };

export type ItemDenominator =
  | { readonly kind: 'known'; readonly value: number }
  | { readonly kind: 'unknown'; readonly unknown: FixedUnknown; readonly grammarFailure?: ExtractionFailureRecord };

export interface SourceCoverage {
  readonly path: string;
  readonly extractionClasses: readonly ExtractionClass[];
  readonly itemDenominator: ItemDenominator;
  // The classification record that governs this source (the parse-failure
  // exclusion when the grammar failed).
  readonly record: ClassificationRecord;
}

export interface ItemCoverage {
  readonly class: ExtractionClass;
  readonly key: string;
  readonly state: CoverageState;
  readonly anchors: readonly DeclarationAnchor[];
  readonly statement?: string;
  readonly context?: string;
  readonly precedence?: PrecedenceCitation;
  readonly unknownReason?: string;
}

export interface ClassCoverage {
  readonly class: ExtractionClass;
  // Items declared by admitted sources (the known part of D).
  readonly declared: number;
  readonly modeled: number;
  readonly unknown: number;
  readonly contradicted: number;
  // Sources assigned this class whose item denominator is Unknown.
  readonly sourcesWithUnknownDenominator: number;
  // Root/index discovery failures that prevent this class denominator from
  // being complete even when no class source was discovered.
  readonly discoveryUnknown: number;
  // D itself: known only when every source of the class was readable.
  readonly denominator: { readonly kind: 'known'; readonly value: number } | { readonly kind: 'unknown'; readonly reasons: readonly string[] };
}

export interface ProjectShapeCoverage {
  readonly sources: readonly SourceCoverage[];
  readonly items: readonly ItemCoverage[];
  readonly classes: Readonly<Record<ExtractionClass, ClassCoverage>>;
  readonly facts: readonly ReconciledFact[];
  readonly contradictions: readonly ReconciledFact[];
  readonly counts: {
    readonly sources: number;
    readonly sourcesWithKnownItemDenominator: number;
    readonly sourcesWithUnknownDenominator: number;
    readonly items: number;
    readonly modeled: number;
    readonly unknown: number;
    readonly contradicted: number;
    readonly facts: number;
    readonly contradictedFacts: number;
    readonly rulesDeclared: number;
    readonly rulesApplied: number;
  };
}

// ---------------------------------------------------------------------
// Reconciliation.

function selects(selector: RuleSelector, declaration: Declaration): boolean {
  if ('path' in selector) return declaration.anchors.some((a) => a.path === selector.path);
  return declaration.basis === selector.basis;
}

function considerRule(
  rule: PrecedenceRule,
  fact: string,
  declarations: readonly Declaration[],
  population: ReadonlySet<string>,
): { readonly outcome: 'applied'; readonly winner: Declaration } | { readonly outcome: RuleRejection } {
  if (!population.has(rule.anchor.path)) return { outcome: 'anchor-not-in-population' };
  if (rule.facts !== undefined && !rule.facts.includes(fact)) return { outcome: 'fact-out-of-scope' };
  const higher = declarations.filter((d) => selects(rule.higher, d));
  const lower = declarations.filter((d) => selects(rule.lower, d));
  if (higher.length === 0) return { outcome: 'higher-side-unmatched' };
  if (lower.length === 0) return { outcome: 'lower-side-unmatched' };
  if (higher.length > 1 || lower.length > 1) return { outcome: 'side-matched-more-than-once' };
  if (higher[0] === lower[0]) return { outcome: 'same-declaration-both-sides' };
  return { outcome: 'applied', winner: higher[0] as Declaration };
}

export interface ReconcileInput {
  readonly rules: readonly PrecedenceRule[];
  // Paths of the admitted source population a rule may be cited from.
  readonly population: ReadonlySet<string>;
}

// Reconciles every declaration of one fact. `identity` marks facts whose
// duplicate declaration is itself a conflict even when the values agree.
export function reconcileFact(fact: string, declarations: readonly Declaration[], input: ReconcileInput, identity: boolean): ReconciledFact {
  if (declarations.length === 0) throw new Error(`reconcileFact: ${fact} has no declarations`);
  const values = new Set(declarations.map((d) => d.value));
  const conflict = declarations.length > 1 && (identity || values.size > 1);
  if (!conflict) {
    return { fact, state: 'modeled', value: (declarations[0] as Declaration).value, declarations, rulesConsidered: [] };
  }
  const rulesConsidered: ConsideredRule[] = [];
  const winners: { rule: PrecedenceRule; winner: Declaration }[] = [];
  for (const rule of input.rules) {
    const result = considerRule(rule, fact, declarations, input.population);
    rulesConsidered.push({ ruleId: rule.id, outcome: result.outcome });
    if (result.outcome === 'applied') winners.push({ rule, winner: result.winner });
  }
  // Exactly one rule must decide, and if several apply they must agree on
  // the winner; otherwise no rule decides.
  const distinctWinners = new Set(winners.map((w) => w.winner));
  if (winners.length === 0 || distinctWinners.size !== 1) {
    return { fact, state: 'contradicted', declarations, unknownReason: CONTRADICTED_REASON, rulesConsidered };
  }
  const { rule, winner } = winners[0] as { rule: PrecedenceRule; winner: Declaration };
  return {
    fact,
    state: 'modeled',
    value: winner.value,
    declarations,
    disagreement: {
      effective: winner,
      superseded: declarations.filter((d) => d !== winner),
      precedence: { ruleId: rule.id, anchor: rule.anchor, statement: rule.statement },
    },
    rulesConsidered,
  };
}

// ---------------------------------------------------------------------
// Coverage.

export type CoverageSourceInput = ClassifiedSource<SourceExtraction>;

export interface CoverageInput {
  readonly sources: readonly CoverageSourceInput[];
  readonly rules?: readonly PrecedenceRule[];
  // Declarations supplied from outside the extraction grammar — a stated
  // summary count, for instance. Fixtures in tests; empty in production
  // until Butlers is observed to declare one.
  readonly statedDeclarations?: readonly Declaration[];
  readonly policy?: SecretClassificationPolicy;
  readonly discoveryUncertainties?: readonly {
    readonly classes: readonly ExtractionClass[];
    readonly unknown: FixedUnknown;
  }[];
}

const itemFact = (item: Pick<ExtractedItem, 'class' | 'key'>): string => `item:${item.class}:${item.key}`;
export const countFact = (cls: ExtractionClass): string => `count:${cls}`;

function sourceCoverage(entry: CoverageSourceInput, policy: SecretClassificationPolicy): SourceCoverage {
  const { record, source } = entry;
  const extractionClasses = source.extractionClasses;
  if (record.outcome !== 'classified') {
    return { path: source.path, extractionClasses, itemDenominator: { kind: 'unknown', unknown: record.unknown }, record };
  }
  const value = entry.value;
  if (value === undefined || value.kind === 'unknown') {
    const excluded = parseFailureExclusion(policy, record);
    return {
      path: source.path,
      extractionClasses,
      itemDenominator: { kind: 'unknown', unknown: excluded.unknown, ...(value === undefined ? {} : { grammarFailure: value.failure }) },
      record: excluded,
    };
  }
  return { path: source.path, extractionClasses, itemDenominator: { kind: 'known', value: value.items.length }, record };
}

function anchorOf(item: ExtractedItem, contentDigest: string | undefined): DeclarationAnchor {
  return { path: item.path, line: item.line, ...(contentDigest === undefined ? {} : { contentDigest }) };
}

export function buildProjectShapeCoverage(input: CoverageInput): ProjectShapeCoverage {
  const policy = input.policy ?? PWB_SECRET_POLICY;
  const rules = input.rules ?? [];
  const sources = input.sources.map((entry) => sourceCoverage(entry, policy));

  // Admitted items with their anchors, in source order.
  const admitted: { readonly item: ExtractedItem; readonly anchor: DeclarationAnchor }[] = [];
  for (const entry of input.sources) {
    if (entry.record.outcome !== 'classified' || entry.value === undefined || entry.value.kind !== 'extracted') continue;
    for (const item of entry.value.items) admitted.push({ item, anchor: anchorOf(item, entry.record.contentDigest) });
  }
  const population = new Set(sources.filter((s) => s.itemDenominator.kind === 'known').map((s) => s.path));
  const reconcile: ReconcileInput = { rules, population };

  // Item identities: one fact per (class, key); a duplicate declaration of
  // an identity is a conflict whatever its statement says.
  const byIdentity = new Map<string, { readonly item: ExtractedItem; readonly anchor: DeclarationAnchor }[]>();
  for (const a of admitted) {
    const fact = itemFact(a.item);
    const list = byIdentity.get(fact);
    if (list === undefined) byIdentity.set(fact, [a]);
    else list.push(a);
  }
  const items: ItemCoverage[] = [];
  const facts: ReconciledFact[] = [];
  for (const [fact, entries] of byIdentity) {
    const declarations: Declaration[] = entries.map((e) => ({
      fact,
      value: e.item.statement ?? e.item.context ?? e.item.key,
      basis: 'extracted-item',
      anchors: [e.anchor],
    }));
    const reconciled = reconcileFact(fact, declarations, reconcile, true);
    facts.push(reconciled);
    const first = (entries[0] as { item: ExtractedItem }).item;
    const effective =
      reconciled.state === 'modeled' && reconciled.disagreement !== undefined
        ? (entries.find((e) => e.anchor === (reconciled.disagreement as { effective: Declaration }).effective.anchors[0]) as { item: ExtractedItem }).item
        : first;
    items.push({
      class: first.class,
      key: first.key,
      state: reconciled.state,
      anchors: entries.map((e) => e.anchor),
      ...(effective.statement === undefined ? {} : { statement: effective.statement }),
      ...(effective.context === undefined ? {} : { context: effective.context }),
      ...(reconciled.state === 'modeled' && reconciled.disagreement !== undefined ? { precedence: reconciled.disagreement.precedence } : {}),
      ...(reconciled.state === 'contradicted' ? { unknownReason: reconciled.unknownReason } : {}),
    });
  }

  // Per-class coverage and the derived count facts.
  const stated = input.statedDeclarations ?? [];
  const classes = {} as Record<ExtractionClass, ClassCoverage>;
  for (const cls of EXTRACTION_CLASSES) {
    const ofClass = items.filter((i) => i.class === cls);
    const unknownSources = sources.filter((s) => s.extractionClasses.includes(cls) && s.itemDenominator.kind === 'unknown');
    const discoveryUnknowns = (input.discoveryUncertainties ?? []).filter((entry) => entry.classes.includes(cls));
    const reasons = [...new Set([
      ...unknownSources.map((s) => (s.itemDenominator as { unknown: FixedUnknown }).unknown.unknownReason),
      ...discoveryUnknowns.map((entry) => entry.unknown.unknownReason),
    ])];
    const declared = ofClass.length;
    const count = (state: CoverageState): number => ofClass.filter((i) => i.state === state).length;
    classes[cls] = {
      class: cls,
      declared,
      modeled: count('modeled'),
      unknown: count('unknown'),
      contradicted: count('contradicted'),
      sourcesWithUnknownDenominator: unknownSources.length,
      discoveryUnknown: discoveryUnknowns.length,
      denominator: reasons.length === 0 ? { kind: 'known', value: declared } : { kind: 'unknown', reasons },
    };
    const fact = countFact(cls);
    const derived: Declaration = {
      fact,
      value: String(declared),
      basis: 'derived-count',
      anchors: sources.filter((s) => s.extractionClasses.includes(cls) && s.itemDenominator.kind === 'known').map((s) => ({ path: s.path })),
    };
    const declarations = [derived, ...stated.filter((d) => d.fact === fact)];
    if (reasons.length > 0) {
      // A count over an Unknown denominator is itself Unknown, whatever a
      // summary states; every declaration is retained.
      facts.push({ fact, state: 'unknown', declarations, unknownReason: reasons[0] as string, rulesConsidered: [] });
      continue;
    }
    facts.push(reconcileFact(fact, declarations, reconcile, false));
  }

  // Stated declarations about facts this module derives nothing for.
  const otherFacts = new Map<string, Declaration[]>();
  for (const d of stated) {
    if (d.fact.startsWith('count:') && (EXTRACTION_CLASSES as readonly string[]).includes(d.fact.slice('count:'.length))) continue;
    const list = otherFacts.get(d.fact);
    if (list === undefined) otherFacts.set(d.fact, [d]);
    else list.push(d);
  }
  for (const [fact, declarations] of otherFacts) facts.push(reconcileFact(fact, declarations, reconcile, false));

  const contradictions = facts.filter((f) => f.state === 'contradicted');
  const rulesApplied = new Set(facts.flatMap((f) => (f.state === 'modeled' && f.disagreement !== undefined ? [f.disagreement.precedence.ruleId] : []))).size;
  return {
    sources,
    items,
    classes,
    facts,
    contradictions,
    counts: {
      sources: sources.length,
      sourcesWithKnownItemDenominator: population.size,
      sourcesWithUnknownDenominator: sources.length - population.size,
      items: items.length,
      modeled: items.filter((i) => i.state === 'modeled').length,
      unknown: items.filter((i) => i.state === 'unknown').length,
      contradicted: items.filter((i) => i.state === 'contradicted').length,
      facts: facts.length,
      contradictedFacts: contradictions.length,
      rulesDeclared: rules.length,
      rulesApplied,
    },
  };
}
