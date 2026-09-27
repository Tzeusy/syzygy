import { digestCanonicalJson } from './canonical-json.js';
import { checkClosedSchema, schemaParts, validateDraftRecord, type ClosedSchema, type ProviderDraft } from './provider-draft.js';

/**
 * Rendered-design review record and its trusted verdict (REQ-polaris-generation-004
 * "Relationship that needs a diagram has none" / "Partly supported diagram";
 * REQ-polaris-generation-006 readiness and retired evidence).
 *
 * Phase A mechanics only. The generation pipeline still never awards rendered
 * readiness; this is the verdict a later rendered-review stage consumes. Nothing
 * here dispatches a reviewer, renders a page or judges clarity: the independent
 * reviewer's enumeration and judgments are the input, and this module computes
 * which of them block from that enumeration alone, never from reviewer-set flags.
 *
 * The link between a relationship and a figure is the review's own `diagram`
 * arm: the reviewer names the one draft diagram it judged to draw that
 * relationship. A relationship is satisfied only through that name, and a
 * diagram named by two diagram-clearer relationships satisfies neither, so the
 * number of other figures in the draft never matters (unrelated extra figures
 * cannot stand in).
 */

const { text, handle, list, object, refs } = schemaParts;
const kind = (value: string): ClosedSchema => ({ ...text, enum: [value] } as ClosedSchema);

const relationshipDiagram: ClosedSchema = { oneOf: [
  object({ kind: kind('named'), diagramId: handle }),
  object({ kind: kind('none') }),
] };
const relationship = object({
  id: handle,
  description: text,
  sourceIds: refs,
  judgment: { ...text, enum: ['diagram-clearer', 'prose-sufficient'] } as ClosedSchema,
  support: { ...text, enum: ['supported', 'partly-supported', 'unsupported'] } as ClosedSchema,
  diagram: relationshipDiagram,
  gaps: list(object({ element: text, reason: text }), 0, 40),
});
const renderedDesignReview = object({
  draftDigest: { type: 'string', minLength: 64, maxLength: 64, pattern: '^[0-9a-f]{64}$' },
  relationships: list(relationship, 0, 200),
  findings: list(object({ severity: { ...text, enum: ['blocking', 'advisory'] } as ClosedSchema, message: text, target: handle }), 0, 1000),
});

export type RelationshipJudgment = 'diagram-clearer' | 'prose-sufficient';
/** `unsupported` with `diagram-clearer` is the spec's undrawable relationship. */
export type RelationshipSupport = 'supported' | 'partly-supported' | 'unsupported';
export interface RenderedDesignRelationship {
  id: string;
  description: string;
  /** The admitted premises the reviewer cites for the relationship itself. */
  sourceIds: string[];
  judgment: RelationshipJudgment;
  support: RelationshipSupport;
  diagram: { kind: 'named'; diagramId: string } | { kind: 'none' };
  /** Unsupported elements disclosed beside a partly supported diagram. */
  gaps: { element: string; reason: string }[];
}
export interface RenderedDesignReview {
  /** Canonical-JSON sha256 of the exact draft reviewed; any revision retires the review. */
  draftDigest: string;
  relationships: RenderedDesignRelationship[];
  findings: { severity: 'blocking' | 'advisory'; message: string; target: string }[];
}
export type RenderedDesignRule =
  | 'missing-diagram'
  | 'diagram-not-produced'
  | 'diagram-claimed-by-another-relationship'
  | 'undisclosed-gap'
  | 'undrawable-without-recorded-omission'
  | 'unsupported-relationship-drawn';
export interface RenderedDesignFinding {
  rule: RenderedDesignRule;
  relationshipId: string;
  /** The enumerated relationship that produced the finding, retained verbatim. */
  enumeration: RenderedDesignRelationship;
}
export interface RenderedDesignVerdict {
  blocking: boolean;
  /** True when the review was bound to other draft bytes: it confirms nothing here. */
  retired: boolean;
  findings: RenderedDesignFinding[];
  reviewerFindings: RenderedDesignReview['findings'];
  enumeration: RenderedDesignRelationship[];
}

const DRAFT_DIGEST_LIMITS = { maxBytes: 4_000_000, maxNodes: 100_000, maxDepth: 64 } as const;

/** The digest a rendered-design review must carry in `draftDigest` for `draft`. */
export function renderedDesignSubjectDigest(draft: unknown): string {
  return digestCanonicalJson(validateDraftRecord(draft), DRAFT_DIGEST_LIMITS).digest;
}

function relationshipRule(item: RenderedDesignRelationship, draft: ProviderDraft, shared: Set<string>): RenderedDesignRule | null {
  if (item.judgment === 'prose-sufficient') return null;
  const named = item.diagram.kind === 'named' ? item.diagram.diagramId : null;
  const figure = named === null ? undefined : draft.diagrams.find(diagram => diagram.id === named);
  if (item.support === 'unsupported') {
    if (figure?.disposition.kind === 'produced') return 'unsupported-relationship-drawn';
    if (figure?.disposition.kind !== 'omitted') return 'undrawable-without-recorded-omission';
    if (shared.has(figure.id)) return 'diagram-claimed-by-another-relationship';
    return null;
  }
  if (figure === undefined) return 'missing-diagram';
  if (shared.has(figure.id)) return 'diagram-claimed-by-another-relationship';
  if (figure.disposition.kind !== 'produced') return 'diagram-not-produced';
  if (item.support === 'partly-supported' && item.gaps.length === 0) return 'undisclosed-gap';
  return null;
}

/**
 * Validates the review record and the draft, then derives blocking findings from
 * the enumeration. A missing or malformed record throws (never "not blocking");
 * an explicit, valid empty enumeration blocks nothing by itself.
 */
export function renderedDesignVerdict(review: unknown, draft: unknown): RenderedDesignVerdict {
  checkClosedSchema(renderedDesignReview, review);
  const data = structuredClone(review as RenderedDesignReview);
  const subject = validateDraftRecord(draft);
  const ids = data.relationships.map(item => item.id);
  if (new Set(ids).size !== ids.length) throw new Error('duplicate-handle');
  if (data.relationships.some(item => item.gaps.length > 0 && item.support !== 'partly-supported')) throw new Error('gap-without-partial-support');
  const targets = new Set([...ids, ...subject.sections.map(s => s.id), ...subject.diagrams.map(d => d.id)]);
  if (data.findings.some(finding => !targets.has(finding.target))) throw new Error('unknown-finding-target');

  const claims = new Map<string, number>();
  for (const item of data.relationships) {
    if (item.judgment === 'diagram-clearer' && item.diagram.kind === 'named') {
      claims.set(item.diagram.diagramId, (claims.get(item.diagram.diagramId) ?? 0) + 1);
    }
  }
  const shared = new Set([...claims].flatMap(([id, count]) => count > 1 ? [id] : []));
  const findings: RenderedDesignFinding[] = data.relationships.flatMap(item => {
    const rule = relationshipRule(item, subject, shared);
    return rule === null ? [] : [{ rule, relationshipId: item.id, enumeration: structuredClone(item) }];
  });
  const retired = data.draftDigest !== digestCanonicalJson(subject, DRAFT_DIGEST_LIMITS).digest;
  return {
    blocking: retired || findings.length > 0 || data.findings.some(finding => finding.severity === 'blocking'),
    retired,
    findings,
    reviewerFindings: data.findings,
    enumeration: data.relationships,
  };
}
