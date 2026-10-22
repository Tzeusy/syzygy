// The package root: everything in live.ts, and the parked provider island beside it (parked, not deleted). A module the
// `syzygy` CLI reaches imports `@syzygy/polaris-generation-core/live` instead.
export * from './live.js';
export {
  admitSourcePopulation,
  admittedSources,
  sourcePopulationDenominator,
  SourcePopulationError,
  type AdmittedSource,
  type ExcludedSource,
  type SourceExclusionReason,
  type SourcePopulation,
  type SourcePopulationFailure,
} from './admitted-input.js';
export {
  discoveryMapEnvelope, discoveryReduceEnvelope, parseDiscoveryMapReply, parseDiscoveryReduceReply, DiscoveryProviderError, DISCOVERY_JSON_LIMITS,
  type DiscoveryMapRequest, type DiscoveryReduceRequest, type DiscoveryReplyClaim, type DiscoveryEnvelope, type DiscoveryProviderFailure,
} from './discovery-provider.js';
export { runGenerationPipeline, type PipelineRequest, type PipelinePorts, type PipelineResult, type GenerationBudget, type AdmissionDecision, type DispatchPermit, type AttemptInput, type AttemptOutcome, type InvalidOutputReason, type ProviderReply, type StageReceipt } from './pipeline.js';
export { stageSchema, validateStage, validateDiscoveryReply, DISCOVERY_CLAIM_MAX_LENGTH, DISCOVERY_RELEVANCE_MAX } from './provider-draft.js';
export type { ProviderDraft, ProviderParagraph, ProviderBlock, ProviderDiagram, ProviderDiagramNode, ProviderDiagramEdge } from './provider-draft.js';
export { renderedDesignVerdict, renderedDesignSubjectDigest } from './rendered-design.js';
export type { RenderedDesignReview, RenderedDesignRelationship, RenderedDesignFinding, RenderedDesignRule, RenderedDesignVerdict, RelationshipJudgment, RelationshipSupport } from './rendered-design.js';
export { buildExcerpt, EXCERPT_KINDS, LICENCE_MARKERS } from './excerpt.js';
export type { Excerpt, ExcerptKind, ExcerptRange } from './excerpt.js';
export { discoverAndSelect, reportFromReceipts, partitionSubsystems, heuristicScore, DiscoveryRefusal, DEFERRED_BY_BUDGET, PIPELINE_QUOTABLE_CAP, DEFAULT_DISCOVERY_BUDGET, DOSSIER_DISCOVERY_BUDGET, DOSSIER_MAX_SELECTED_BYTES } from './discovery.js';
export type { DiscoveryBudget, DiscoveryCall, DiscoveryReceipt, MapReply, ReduceReply, DiscoveryClaim, DiscoveryPorts, ExcerptAudit, DiscoveryReport, DiscoveryResult, MapInput, ReduceInput } from './discovery.js';
