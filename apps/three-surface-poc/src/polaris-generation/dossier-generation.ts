import { createHash } from 'node:crypto';
import { closeSync, fsyncSync, mkdirSync, openSync, writeSync } from 'node:fs';
import path from 'node:path';

import {
  discoveryMapEnvelope, discoveryReduceEnvelope, parseDiscoveryMapReply, parseDiscoveryReduceReply, promptForStage, reviewVerdict, runGenerationPipeline, stageSchema, validateGenerationSources, validateStage,
  type DiscoveryBudget, type DiscoveryCall, type DiscoveryPorts, type DiscoveryReceipt, type DispatchPermit, type GenerationBudget, type GenerationSource, type GenerationStage,
  type PipelinePorts, type PipelineRequest, type PipelineResult, type PromptStage, type ProviderReply,
} from '@syzygy/polaris-generation-core';
import { createPackageAdmissionReader, withConsent, type AdmissionRecordReader, type ConsentAudit } from '@syzygy/polaris-generation-consent';
import { PROVIDER_ORIGIN, createAgentSdkGenerate, createMessagesApiGenerate, minimumUsageUnits } from '@syzygy/polaris-generation-provider';

import { createDurableLifecycle } from './durable-lifecycle.js';
import { DOSSIER_RUN_PROFILE, assertRunProfile, discoveryBudgetFor, narrativeBudgetFor, stageCeilingUnits, type DossierRunProfile } from './dossier-run-profile.js';
import { stageAuthorisedBy } from './dossier-stage-authority.js';
import type { WiredRecordsPort } from './dossier-records.js';
import { soundAnswer, type AdmissionRequirement, type GenerationOpenContext, type GenerationSession } from './dossier-trigger.js';

export type DossierRoute = 'agent-sdk' | 'messages-api';
export const DOSSIER_ROUTES: readonly DossierRoute[] = ['agent-sdk', 'messages-api'];
/** The route names a request carries; the consent ports map each to the provider id the egress record names. */
export const ROUTE_NAMES: Readonly<Record<DossierRoute, string>> = { 'agent-sdk': 'anthropic-agent-sdk', 'messages-api': 'anthropic-messages-api' };
const PROVIDER_ID = 'anthropic';
const CONSENTING_PROJECT = 'project:syzygy';
/** The class the screening scope gives the generator's own instruction text (instructionTextRule), and the class of every admitted body. */
const INSTRUCTION_CLASS = 'code-content';
const DISCOVERY_REPLY_BYTES = 100_000;

/** A failure to start generation that is a refusal to run, not a crash: the trigger reports it as `generation-unavailable`. */
export class GenerationUnavailable extends Error {
  constructor(readonly detail: string) { super(detail); this.name = 'GenerationUnavailable'; }
}

export interface ProviderAttempt { readonly attemptId: string; readonly try: number; readonly outcome: string; readonly httpStatus: number | null; readonly usageUnits: number | null; readonly backoffMs: number }
export interface ProviderHandle {
  readonly generate: PipelinePorts['generate'];
  readonly attempts: () => readonly ProviderAttempt[];
  readonly gateDecisions: () => readonly unknown[];
  readonly close: () => Promise<void>;
}
export interface ProviderBuild {
  readonly route: DossierRoute;
  /** Handed to the adapter and nowhere else; never written to a file or a log. */
  readonly apiKey: string;
  /** Private runtime state of the provider adapter; inside the run's state directory. */
  readonly runDir: string;
  readonly profile: DossierRunProfile;
  /** Asked by the gate for every request. */
  readonly permitted: (permit: DispatchPermit, stage: PromptStage) => Promise<boolean>;
}
export type ProviderFactory = (build: ProviderBuild) => ProviderHandle;

/** Production: the gate forwards to the provider origin and to nothing else. No parameter here can name another upstream. */
export const productionProviderFactory: ProviderFactory = build => {
  const { profile } = build;
  if (build.route === 'agent-sdk') {
    mkdirSync(build.runDir, { recursive: true, mode: 0o700 });
    return createAgentSdkGenerate({ runDir: build.runDir, model: profile.model, effort: profile.effort, thinking: profile.thinking, maxOutputTokens: profile.maxOutputTokens,
      auth: { apiKey: build.apiKey }, upstream: { url: PROVIDER_ORIGIN }, permitted: build.permitted });
  }
  return createMessagesApiGenerate({ model: profile.model, apiKey: build.apiKey, upstream: { url: PROVIDER_ORIGIN }, permitted: build.permitted,
    effort: profile.effort, thinking: profile.thinking, maxOutputTokens: profile.maxOutputTokens });
};

/** What one provider call counted for, whatever the provider reported. Content-free. */
export interface MeteredCall { readonly phase: 'discovery' | 'narrative'; readonly stage: PromptStage; readonly ceilingUnits: number; readonly countedUnits: number; readonly usageUnknown: boolean }

const digest = (text: string): string => createHash('sha256').update(text, 'utf8').digest('hex');
const spentOf = (error: unknown): number | null => (typeof (error as { spentUnits?: unknown } | null)?.spentUnits === 'number' ? (error as { spentUnits: number }).spentUnits : null);

function appendDurable(file: string, value: unknown): void {
  const fd = openSync(file, 'a', 0o600);
  try { writeSync(fd, `${JSON.stringify(value)}\n`); fsyncSync(fd); } finally { closeSync(fd); }
}

export interface OpenGenerationOptions {
  readonly route: DossierRoute;
  readonly apiKey: string;
  /** The Syzygy checkout whose decisions the readers consult. */
  readonly root: string;
  readonly now?: () => number;
  readonly profile?: DossierRunProfile;
  readonly providerFactory?: ProviderFactory;
  readonly reader?: AdmissionRecordReader;
}

/**
 * Builds the one provider handle of a run and everything that sits on it: the
 * egress gate (through the factory), discovery's map and reduce calls, the
 * durable lifecycle with the consent ports, the budgets and the accounting.
 * Called by the trigger after every admission record is satisfied and before
 * any repository object is fetched.
 */
export function openGeneration(options: OpenGenerationOptions): (context: GenerationOpenContext) => Promise<GenerationSession> {
  const profile = options.profile ?? DOSSIER_RUN_PROFILE;
  return async context => {
    assertRunProfile(profile);
    if (typeof options.apiKey !== 'string' || options.apiKey.length === 0) throw new GenerationUnavailable('credential-missing: SYZYGY_POLARIS_PROVIDER_API_KEY is not set');
    const records = context.records as WiredRecordsPort;
    if (typeof records.inForceEgress !== 'function') throw new GenerationUnavailable('records-port-cannot-name-the-egress-record');
    const now = options.now ?? Date.now;
    const stateDir = `${context.runDir}.state`;
    try { mkdirSync(stateDir, { mode: 0o700 }); } catch { throw new GenerationUnavailable('state-directory-unavailable'); }
    const egress: AdmissionRequirement = context.egress;

    /** The single check behind every request: the egress record that admitted this run is in force now AND the digest of its exact bytes authorises this stage. */
    const authorise = async (stage: PromptStage): Promise<boolean> => {
      try {
        if (soundAnswer(await records.check(egress)).satisfied !== true) return false;
        const inForce = await records.inForceEgress(egress);
        return inForce !== null && stageAuthorisedBy(inForce.digest, stage);
      } catch { return false; }
    };

    const handle = (options.providerFactory ?? productionProviderFactory)({
      route: options.route, apiKey: options.apiKey, runDir: path.join(stateDir, 'provider'), profile,
      permitted: async (_permit, stage) => authorise(stage),
    });

    const calls: MeteredCall[] = [];
    let discoverySpent = 0;
    const metered = (phase: MeteredCall['phase'], stage: PromptStage): PipelinePorts['generate'] => async input => {
      let counted = input.permit.maxUsageUnits, unknown = true;
      try {
        const reply: ProviderReply = await handle.generate(input);
        if (typeof reply.usageUnits === 'number' && Number.isSafeInteger(reply.usageUnits) && reply.usageUnits >= 0) { counted = reply.usageUnits; unknown = false; }
        return reply;
      } catch (error) {
        const spent = spentOf(error);
        if (spent !== null) { counted = spent; unknown = false; }
        throw error;
      } finally {
        calls.push({ phase, stage, ceilingUnits: input.permit.maxUsageUnits, countedUnits: counted, usageUnknown: unknown });
        if (phase === 'discovery') discoverySpent += counted;
      }
    };

    // ---- discovery -------------------------------------------------------
    const callUnits = profile.owner.discoveryCallUnits;
    let ordinal = 0;
    const dispatchDiscovery = async (stage: 'discovery-map' | 'discovery-reduce', envelope: { system: string; responseSchema: unknown }, encoded: string, signal: AbortSignal): Promise<ProviderReply> => {
      const permit: DispatchPermit = { attemptId: `discovery-${ordinal++}-${digest(encoded).slice(0, 16)}`, maxUsageUnits: callUnits, maxOutputBytes: DISCOVERY_REPLY_BYTES };
      // The two discovery stages are not pipeline stages; the adapters only pass the name on to `permitted`.
      return metered('discovery', stage)({ permit, stage: stage as unknown as GenerationStage, system: envelope.system, input: encoded, responseSchema: envelope.responseSchema, signal });
    };
    const discovery: Pick<DiscoveryPorts, 'map' | 'reduce'> = {
      map: async (input, signal) => {
        const { envelope, input: encoded } = discoveryMapEnvelope(input);
        const reply = await dispatchDiscovery('discovery-map', envelope, encoded, signal);
        return { claims: parseDiscoveryMapReply(input, reply.body).claims, usageUnits: reply.usageUnits };
      },
      reduce: async (input, signal) => {
        const { envelope, input: encoded } = discoveryReduceEnvelope(input);
        const reply = await dispatchDiscovery('discovery-reduce', envelope, encoded, signal);
        return { ranked: parseDiscoveryReduceReply(input, reply.body).ranked, usageUnits: reply.usageUnits };
      },
    };
    const receiptFile = path.join(stateDir, 'discovery-receipts.jsonl');
    const discoveryReceipt = async (receipt: DiscoveryReceipt): Promise<void> => { appendDurable(receiptFile, receipt); };
    /** Asked before each call: the discovery share must still hold one more call at its ceiling, and the record must authorise the stage. */
    const discoveryPermitted = async (call: DiscoveryCall): Promise<boolean> =>
      discoverySpent + callUnits <= profile.owner.discoveryUnits && await authorise(call.kind === 'map' ? 'discovery-map' : 'discovery-reduce');

    // ---- narrative -------------------------------------------------------
    const reader = options.reader ?? createPackageAdmissionReader({ root: options.root });
    const routes = Object.fromEntries((['inventory', 'plan', 'author', 'edit', 'fidelity', 'repair'] as const).map(stage => [stage, ROUTE_NAMES[options.route]])) as Record<GenerationStage, string>;
    const auditFile = path.join(stateDir, 'consent-audit.jsonl');
    const narrativeGenerate: PipelinePorts['generate'] = input => metered('narrative', input.stage)(input);

    const runPipeline = async (request: PipelineRequest, signal: AbortSignal): Promise<PipelineResult> => {
      const base = createDurableLifecycle({
        stateDir: path.join(stateDir, 'narrative'),
        permissionIdentity: async () => '',   // replaced by the consent ports; alone it refuses
        verifySources: async frozen => { try { validateGenerationSources(frozen.sources); return true; } catch { return false; } },
        permitted: async () => true,          // replaced below: consent first, then the stage authority
        responseSchema: stageSchema, validate: validateStage, fidelity: reviewVerdict,
        generate: narrativeGenerate,
        maxAttemptUsageUnits: stage => stageCeilingUnits(profile, stage),
        maxAttemptOutputBytes: profile.maxAttemptOutputBytes,
        // The provider counts bytes of system and input; the envelope already holds the system text once, the system message sends it again.
        minimumAttemptUsageUnits: input => minimumUsageUnits(input.inputBytes + Buffer.byteLength(promptForStage(input.stage).system, 'utf8')),
        now,
      });
      const consented = withConsent(base, {
        reader, now, consentingProject: CONSENTING_PROJECT, routeProviders: { [ROUTE_NAMES[options.route]]: PROVIDER_ID },
        sources: request.sources, contentClassOf: (source: GenerationSource) => (source.classificationBasis === 'body' ? INSTRUCTION_CLASS : null), instructionClass: INSTRUCTION_CLASS,
        audit: async (record: ConsentAudit) => { appendDurable(auditFile, record); },
      });
      const ports: PipelinePorts = {
        ...consented,
        // The consent ports replaced the base check; the stage authority is the second half of the same question.
        permitted: async (input, permit) => (await consented.permitted(input, permit)) === true && await authorise(input.stage),
      };
      return runGenerationPipeline(request, ports, signal);
    };

    return {
      discovery, discoveryReceipt, discoveryPermitted,
      discoveryBudget: discoveryBudgetFor(profile),
      narrativeBudget: (elapsedMs: number): GenerationBudget => narrativeBudgetFor(profile, elapsedMs),
      wallClockMs: profile.owner.wallClockMs,
      routes,
      runPipeline,
      record: () => ({
        accountingPolicy: profile.accountingPolicy, route: options.route, routeName: ROUTE_NAMES[options.route], model: profile.model, effort: profile.effort, thinking: profile.thinking,
        budget: { ...profile.owner, narrativeUnits: profile.owner.runTotalUnits - profile.owner.discoveryUnits },
        spend: { discoveryCountedUnits: discoverySpent, narrativeCountedUnits: calls.filter(call => call.phase === 'narrative').reduce((sum, call) => sum + call.countedUnits, 0) },
        calls, attempts: handle.attempts(), gateDecisions: handle.gateDecisions(), stateDir,
      }),
      close: async () => { await handle.close(); },
    };
  };
}

export { type DiscoveryBudget };
