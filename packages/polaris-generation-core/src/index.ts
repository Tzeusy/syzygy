export {
  CANONICAL_JSON_ENCODING,
  CanonicalJsonError,
  digestCanonicalJson,
  encodeCanonicalJson,
  type CanonicalJsonFailure,
  type CanonicalJsonLimits,
} from './canonical-json.js';

export { parseBoundedJson, BoundedJsonError } from './parse-json.js';
export { generationSourceIdentity, generationAnchorId, gitBlobObjectId, validateGenerationSources, quotableGenerationSources, generationSourcesForBody, segmentBody, GenerationSourceError, type BodyPiece, type BodySourceInput, type GenerationSource, type GenerationSourceFailure } from './generation-source.js';
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
export { promptForStage, type GenerationStage } from './prompts.js';
export { runGenerationPipeline, type PipelineRequest, type PipelinePorts, type PipelineResult, type GenerationBudget, type AdmissionDecision, type DispatchPermit, type AttemptInput, type AttemptOutcome, type InvalidOutputReason, type ProviderReply, type StageReceipt } from './pipeline.js';
export { SOURCE_TEXT_MAX_LENGTH, stageSchema, validateStage, validateDraftRecord, validateRequestedAssets, reviewVerdict, diagramToMermaid, DIAGRAM_KINDS } from './provider-draft.js';
export type { ProviderDraft, ProviderParagraph, ProviderBlock, ProviderDiagram, ProviderDiagramNode, ProviderDiagramEdge, DiagramKind, EpistemicMarking, RequestedAsset } from './provider-draft.js';
export { renderedDesignVerdict, renderedDesignSubjectDigest } from './rendered-design.js';
export type { RenderedDesignReview, RenderedDesignRelationship, RenderedDesignFinding, RenderedDesignRule, RenderedDesignVerdict, RelationshipJudgment, RelationshipSupport } from './rendered-design.js';
export {
  evaluateDossier, scanDossierPage, readerCost, fidelity, resolveQuote, runReaderTest, topicCoverage, scriptedAnswers, admittedSourcesDigest,
  parseDossierManifest, parseReaderQuestions, parsePageBudget, decodeHtmlText, isDossierPagePath,
  DossierEvaluationError, DOSSIER_FORMAT, READER_QUESTIONS_FORMAT, OWNER_TOPICS,
  type DossierManifest, type DossierEvaluationInput, type ReaderQuestion, type ReaderAnswer, type ReaderAnswerPort, type ReaderPortFactory, type ReaderLocation,
  type PageBudget, type BoundOutcome, type QuoteOutcome, type ScannedPage, type OwnerTopic,
} from './dossier-evaluation.js';
export { discoverAndSelect, reportFromReceipts, partitionSubsystems, heuristicScore, DiscoveryRefusal, DEFERRED_BY_BUDGET, PIPELINE_QUOTABLE_CAP, DEFAULT_DISCOVERY_BUDGET } from './discovery.js';
export type { DiscoveryBudget, DiscoveryCall, DiscoveryReceipt, MapReply, ReduceReply, DiscoveryClaim, DiscoveryPorts, DiscoveryReport, DiscoveryResult, MapInput, ReduceInput } from './discovery.js';
