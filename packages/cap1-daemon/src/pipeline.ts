import { join } from 'node:path';

import {
  computeCoverage,
  computeShapeAnswers,
  registerProject,
  type CoverageResult,
  type EvaluationIdentity,
  type FactModel,
  type NamedValidationFailure,
  type ObservationOutcome,
  type ProjectId,
  type RegistrationResult,
  type ServedFact,
  type ShapeAnswerSet,
} from '@syzygy/cap1-core';

import {
  loadConsentReferences,
  type ConsentLoadReport,
} from './consent-loading.js';
import {
  observeDeclaration,
  observeRepositorySnapshot,
  type DeclarationObservation,
} from './observation.js';

// RT3 — the daemon's observation → consent → evaluation pipeline.
//
// `evaluateProject` assembles, over a REAL observed repository, exactly
// the composition the integration conformance test
// (req-integration.conformance.test.ts) establishes as the end-to-end
// FactModel assembly: observeDeclaration → readDeclaration (inside the
// observation) → registerProject → loadConsentReferences →
// observeRepositorySnapshot → computeCoverage → computeShapeAnswers →
// FactModel. Every domain decision stays in the unchanged core; every
// disk fact arrives ONLY through the Wave 1 adapters (observation.ts,
// consent-loading.ts). Nothing here re-implements a rule, and nothing
// here invents a fact.
//
// Polarity: no evidence yields Unknown, never green; failures flow
// through as NAMED values — the declaration observation's named arms,
// core's named validation failures, and the consent loader's named
// failures all travel on the result, never thrown away and never
// collapsed (VIS-2; CAP1-REQ-012's Unknown-as-policy-state polarity is
// core's, reached by feeding core only what was actually observed).
//
// Determinism: a function of (disk state, deps). The evaluation
// identity — snapshot and as-of instant — is the CALLER's injected
// coordinate (RFC2-3: never ambient wall-clock); no clock is read here.

// Where the consent decisions home lives inside an observed governed
// repository (RFC3-7: consent records are governance acts under the
// governance decisions home, referenced from the declaration).
export const CONSENT_DECISIONS_RELATIVE_PATH = '.syzygy/governance/decisions' as const;

// The scenario context every daemon-served FactModel carries
// (CAP1-REQ-042's equivalence coordinate; one spelling, fixed here).
export const DAEMON_SCENARIO_CONTEXT = 'daemon-runtime' as const;

export interface PipelineDependencies {
  // The evaluation identity every answer is stamped with — the pair
  // (source snapshot, as-of instant), supplied by the composition root
  // (RFC2-3; RFC6-15). Injected so the pipeline holds no clock.
  readonly evaluation: EvaluationIdentity;
  // On-disk root per declared repository id. Default: every declared
  // `governance-root` repository maps to the observed root — the
  // declaring repository IS the governance root (RFC3-4: designation by
  // the declaration file's location). A declared repository with no
  // entry here is simply NOT observed: it gets no fabricated outcome,
  // so core renders its consented arm `capture-failed` (reason
  // `source-uncaptured-or-unreachable`) — fail-closed, never green.
  readonly repositoryRoots?: Readonly<Record<string, string>> | undefined;
}

// The pipeline result — a discriminated union over `kind`, every arm
// carrying its named evidence. No arm discards a failure.
export type ProjectEvaluation =
  | {
      readonly kind: 'project-evaluated';
      readonly projectId: ProjectId;
      // The one FactModel both channels (RT4 machine, RT5 human) serve
      // from — the same shape the integration conformance test builds.
      readonly model: FactModel;
      readonly answers: ShapeAnswerSet;
      readonly registration: RegistrationResult;
      readonly coverage: CoverageResult;
      // Named consent-load failures ride here, verbatim; a failed
      // reference contributed no record, so its pair already renders
      // unconsented in `coverage` by core's own absence polarity.
      readonly consent: ConsentLoadReport;
      readonly observations: readonly ObservationOutcome[];
      readonly declarationObservation: Extract<
        DeclarationObservation,
        { kind: 'declaration-read' }
      >;
    }
  | {
      // The declaration was read but did not validate: registration is
      // core's named-failure arm; there is no validated project id, so
      // no answer set is minted for a project that never registered.
      readonly kind: 'declaration-invalid';
      readonly declarationObservation: Extract<
        DeclarationObservation,
        { kind: 'declaration-read' }
      >;
      readonly registration: Extract<RegistrationResult, { status: 'failed' }>;
      readonly failures: readonly NamedValidationFailure[];
    }
  | {
      // Nothing was read: the observation's own named arm — missing
      // declaration (evidence of absence) or unreachable (absence of
      // evidence), each already carrying its Unknown reason verbatim.
      readonly kind: 'no-declaration-observed';
      readonly declarationObservation: Extract<
        DeclarationObservation,
        { kind: 'declaration-missing' | 'declaration-unreachable' }
      >;
    };

// Maps a shape-answer set onto served facts — the integration
// conformance test's own mapping, reproduced as the one runtime
// serialization (label parity: the epistemic label travels verbatim
// from the render arm; RFC6-14).
export function factsFromAnswers(answers: ShapeAnswerSet): readonly ServedFact[] {
  return answers.answers.map((answer): ServedFact => {
    const render = answer.render;
    if (render.value === 'Unknown' && 'reasons' in render) {
      return {
        name: answer.name,
        value: render.value,
        epistemic: { label: 'Unknown', reasons: render.reasons },
      };
    }
    if (render.value === 'not evaluated' && 'basis' in render) {
      return {
        name: answer.name,
        value: render.value,
        epistemic: { label: 'Unknown', basis: 'deferred' },
      };
    }
    return {
      name: answer.name,
      value: render.value,
      epistemic: { label: 'Observed' },
    };
  });
}

// Default repository-roots map: the observed root stands for each
// declared governance-root repository, nothing else (see
// PipelineDependencies.repositoryRoots).
function defaultRepositoryRoots(
  observedRootDir: string,
  repositories: readonly { readonly id: string; readonly role: string }[],
): Readonly<Record<string, string>> {
  const roots: Record<string, string> = {};
  for (const entry of repositories) {
    if (entry.role === 'governance-root') {
      roots[entry.id] = observedRootDir;
    }
  }
  return roots;
}

/**
 * Evaluate the project declared at `observedRootDir` — the daemon's one
 * pipeline from disk to FactModel. See the module comment for the
 * composition, polarity, and determinism contract.
 */
export async function evaluateProject(
  observedRootDir: string,
  deps: PipelineDependencies,
): Promise<ProjectEvaluation> {
  const declarationObservation = await observeDeclaration(observedRootDir);

  if (declarationObservation.kind !== 'declaration-read') {
    return { kind: 'no-declaration-observed', declarationObservation };
  }

  const read = declarationObservation.result;
  const registration = registerProject(read, deps.evaluation.snapshot);

  if (!read.ok || registration.status === 'failed') {
    // `registration.status === 'failed'` exactly when `!read.ok`
    // (registerProject's own contract); both checks appear so the
    // narrowing is type-level, not an assumption.
    const failed =
      registration.status === 'failed'
        ? registration
        : /* unreachable by registerProject's contract */ undefined;
    if (failed === undefined) {
      throw new Error(
        'registerProject returned registered for a failed read — core contract violated',
      );
    }
    return {
      kind: 'declaration-invalid',
      declarationObservation,
      registration: failed,
      failures: failed.failures,
    };
  }

  const declaration = read.declaration;
  const projectId = declaration.project.id;

  // Consent: every declared reference, loaded from its exact location
  // under the governance decisions home. Failures are named and kept;
  // only loaded records feed the core.
  const consent = loadConsentReferences(
    join(observedRootDir, CONSENT_DECISIONS_RELATIVE_PATH),
    declaration.consents,
  );

  // Observation: one real snapshot per declared repository with a known
  // on-disk root, in declaration order. Repositories without a known
  // root contribute NO outcome (see PipelineDependencies).
  const roots = deps.repositoryRoots ?? defaultRepositoryRoots(
    observedRootDir,
    declaration.repositories,
  );
  const observations: ObservationOutcome[] = [];
  for (const entry of declaration.repositories) {
    const root = roots[entry.id];
    if (root !== undefined) {
      observations.push(await observeRepositorySnapshot(entry.id, root));
    }
  }

  const coverage = computeCoverage(declaration, consent.records, observations);
  const answers = computeShapeAnswers(projectId, deps.evaluation, {
    registration,
    coverage,
  });

  const model: FactModel = {
    selection: `project:${projectId}`,
    evaluation: deps.evaluation,
    scenarioContext: DAEMON_SCENARIO_CONTEXT,
    declaredFilters: {},
    facts: factsFromAnswers(answers),
  };

  return {
    kind: 'project-evaluated',
    projectId,
    model,
    answers,
    registration,
    coverage,
    consent,
    observations,
    declarationObservation,
  };
}
