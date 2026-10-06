import { BoundedJsonError, parseBoundedJson } from '@syzygy/polaris-generation-core';
import { validateRunConfig, type RunConfig, type RunConfigRefusal } from './run-config.js';

/** The run configuration as the run directory stores it (`run.json`).
 *
 * Each declared value is recorded with who declared it and its label: the operator declared it,
 * and Syzygy observed none of it, so every value is Inferred. The principal of the commands is the
 * operator, operator-declared; the commands hold no credential that authenticates to Syzygy, so the
 * credential identity is Unknown, never fabricated. No provider-reported model version exists in
 * this mode, and the record says so. */

export const RUN_RECORD_FORMAT = 'polaris-dossier-run/1' as const;
export const NO_PROVIDER_MODEL_VERSION = 'no provider-reported model version is available in the operator-agent mode';

export interface RecordedRunConfig {
  readonly format: typeof RUN_RECORD_FORMAT;
  readonly mode: 'operator-agent';
  readonly declared: RunConfig;
  readonly declaredBy: 'operator';
  readonly label: 'Inferred';
  readonly modelVersionProvider: typeof NO_PROVIDER_MODEL_VERSION;
  readonly principal: { readonly name: string; readonly declaredBy: 'operator'; readonly credentialIdentity: 'Unknown' };
}

export function recordRunConfig(config: RunConfig): RecordedRunConfig {
  return {
    format: RUN_RECORD_FORMAT,
    mode: 'operator-agent',
    declared: config,
    declaredBy: 'operator',
    label: 'Inferred',
    modelVersionProvider: NO_PROVIDER_MODEL_VERSION,
    principal: { name: config.operator, declaredBy: 'operator', credentialIdentity: 'Unknown' },
  };
}

/** The declared values in the input form `parseRunConfig` reads, so a stored record is re-validated
 * by the same rules that admitted it. */
function declaredInput(config: RunConfig): Record<string, unknown> {
  const input: Record<string, unknown> = {
    operator: config.operator, agentTool: config.agentTool, agentToolVersion: config.agentToolVersion,
    agentProvider: config.agentProvider, model: config.model, deadline: config.deadline.declared,
    maxRepairCycles: config.maxRepairCycles, maxQuestions: config.maxQuestions, audience: config.audience,
    operatorIsOwner: config.operatorIsOwner,
  };
  if (config.modelVersion !== null) input['modelVersion'] = config.modelVersion;
  if (config.agentTokenBudget !== null) input['agentTokenBudget'] = config.agentTokenBudget;
  if (config.agentTurnBudget !== null) input['agentTurnBudget'] = config.agentTurnBudget;
  return input;
}

export function encodeRunRecord(config: RunConfig): string {
  const record = recordRunConfig(config);
  return `${JSON.stringify({ ...record, declared: declaredInput(config) }, null, 2)}\n`;
}

export type ReadRunRecordResult =
  | { readonly ok: true; readonly record: RecordedRunConfig }
  | { readonly ok: false; readonly detail: string; readonly refusals?: readonly RunConfigRefusal[] };

const RECORD_JSON_LIMITS = Object.freeze({ maxBytes: 32_768, maxNodes: 128, maxDepth: 3 });
const RECORD_KEYS = ['declared', 'declaredBy', 'format', 'label', 'mode', 'modelVersionProvider', 'principal'];

/** Read a stored record back. The record lies within the agent sessions' write reach, so it is
 * re-validated in full; whatever it says stays Inferred. */
export function readRunRecord(text: string): ReadRunRecordResult {
  let document: unknown;
  try {
    document = parseBoundedJson(text, RECORD_JSON_LIMITS);
  } catch (cause) {
    return { ok: false, detail: `run.json is not one bounded JSON object (${cause instanceof BoundedJsonError ? cause.code : 'invalid-json'})` };
  }
  if (document === null || typeof document !== 'object' || Array.isArray(document)) {
    return { ok: false, detail: 'run.json is not a JSON object' };
  }
  const fields = document as Readonly<Record<string, unknown>>;
  const keys = Object.keys(fields).sort();
  if (keys.join(',') !== RECORD_KEYS.join(',')) {
    return { ok: false, detail: `run.json carries fields ${keys.join(', ')}; expected ${RECORD_KEYS.join(', ')}` };
  }
  if (fields['format'] !== RUN_RECORD_FORMAT || fields['mode'] !== 'operator-agent' || fields['declaredBy'] !== 'operator'
    || fields['label'] !== 'Inferred' || fields['modelVersionProvider'] !== NO_PROVIDER_MODEL_VERSION) {
    return { ok: false, detail: `run.json is not a ${RUN_RECORD_FORMAT} record of the operator-agent mode` };
  }
  const config = validateRunConfig(fields['declared']);
  if (!config.ok) return { ok: false, detail: 'run.json declares an invalid run configuration', refusals: config.refusals };
  const principal = fields['principal'] as Readonly<Record<string, unknown>> | null;
  if (principal === null || typeof principal !== 'object' || principal['name'] !== config.config.operator
    || principal['declaredBy'] !== 'operator' || principal['credentialIdentity'] !== 'Unknown'
    || Object.keys(principal).length !== 3) {
    return { ok: false, detail: 'run.json principal must be the declared operator, operator-declared, with credential identity Unknown' };
  }
  return { ok: true, record: recordRunConfig(config.config) };
}
