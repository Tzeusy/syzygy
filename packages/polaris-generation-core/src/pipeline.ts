import { digestCanonicalJson, encodeCanonicalJson, type CanonicalJsonLimits } from './canonical-json.js';
import { parseBoundedJson } from './parse-json.js';
import { promptForStage, type GenerationStage } from './prompts.js';

export interface GenerationBudget {
  readonly maxCalls: number;
  readonly maxInputBytes: number;
  readonly maxOutputBytes: number;
  readonly maxUsageUnits: number;
  readonly maxElapsedMs: number;
  readonly maxRepairCycles: number;
  readonly accountingPolicy: string;
}

export interface PipelineRequest {
  readonly requestId: string;
  readonly projectId: string;
  readonly snapshotId: string;
  readonly providerRoute: string;
  readonly startedAt: number;
  readonly budget: GenerationBudget;
  readonly sources: unknown;
  readonly readerQuestions: unknown;
}

export interface AttemptInput {
  readonly requestId: string;
  readonly projectId: string;
  readonly snapshotId: string;
  readonly providerRoute: string;
  readonly stage: GenerationStage;
  readonly ordinal: number;
  readonly inputDigest: string;
  readonly inputBytes: number;
  readonly deadline: number;
  readonly budget: GenerationBudget;
}

export interface DispatchPermit {
  readonly attemptId: string;
  readonly maxUsageUnits: number;
  readonly maxOutputBytes: number;
}

export interface ProviderReply {
  readonly body: string;
  readonly model: string | null;
  readonly usageUnits: number | null;
}

export type AttemptOutcome =
  | { readonly kind: 'validated'; readonly outputDigest: string; readonly model: string | null; readonly usageUnits: number }
  | { readonly kind: 'invalid-output' | 'usage-uncertain' | 'effect-uncertain'; readonly usageUnits: number | null };

/** Effect ports are trusted implementations, never fields supplied by a model. */
export interface PipelinePorts {
  readonly now: () => number;
  /** Checks snapshot bytes against owning sources, screening and effective policy. */
  readonly verifySources: (request: PipelineRequest) => Promise<boolean>;
  /** Atomic durable reservation + exclusive dispatch admission, or refusal.
   * Owns original deadline, cumulative reservations, immutable request binding,
   * fresh scheduler observation, execution warrant and consent evaluation.
   * An already-dispatched identity MUST refuse; lease expiry cannot replay it.
   */
  readonly admit: (input: AttemptInput) => Promise<DispatchPermit | null>;
  /** Rechecks effect permission immediately before dispatch. */
  readonly permitted: (input: AttemptInput, permit: DispatchPermit) => Promise<boolean>;
  readonly releaseUnsent: (permit: DispatchPermit) => Promise<void>;
  readonly responseSchema: (stage: GenerationStage) => { readonly version: string; readonly schema: unknown };
  readonly generate: (input: {
    readonly permit: DispatchPermit;
    readonly stage: GenerationStage;
    readonly system: string;
    readonly input: string;
    readonly responseSchema: unknown;
    readonly signal: AbortSignal;
  }) => Promise<ProviderReply>;
  /** Closed schema, source-reference and screening validation. Throws on refusal.
   * Returns a validated data record, not an acceptance/permission assertion.
   */
  readonly validate: (stage: GenerationStage, value: unknown, context: Readonly<Record<string, unknown>>) => unknown;
  /** Durable, idempotent receipt; diagnostics contain no invalid output bodies. */
  readonly record: (permit: DispatchPermit, outcome: AttemptOutcome) => Promise<void>;
  /** Late receipts resolve the original reservation, even after a stopped run. */
  readonly lateReceipt: (permit: DispatchPermit, receipt: { readonly model: string | null; readonly usageUnits: number | null }) => Promise<void>;
  /** Trusted interpretation of the validated fidelity record, not provider flags. */
  readonly fidelity: (review: unknown) => { readonly blocking: boolean; readonly findings: unknown };
}

export interface StageReceipt {
  readonly stage: GenerationStage;
  readonly attemptId: string;
  readonly inputDigest: string;
  readonly outputDigest: string;
  readonly promptVersion: string;
}

export interface ValidatedStageOutput {
  readonly stage: GenerationStage;
  readonly value: unknown;
}

export type PipelineResult = {
  readonly status: 'awaiting-rendered-review';
  readonly draft: unknown;
  readonly inventory: unknown;
  readonly review: unknown;
  readonly receipts: readonly StageReceipt[];
  readonly artifacts: readonly ValidatedStageOutput[];
} | {
  readonly status: 'stopped';
  readonly reason: 'invalid-request' | 'source-refused' | 'admission-refused' | 'budget-exhausted' | 'cancelled' | 'deadline' | 'effect-uncertain' | 'invalid-output' | 'usage-uncertain' | 'repair-exhausted' | 'adapter-failure';
  readonly receipts: readonly StageReceipt[];
  readonly artifacts: readonly ValidatedStageOutput[];
};

type StopReason = Extract<PipelineResult, { status: 'stopped' }>['reason'];
class PipelineStop extends Error {
  constructor(readonly reason: StopReason) { super(reason); }
}

const dataLimits = (bytes: number): CanonicalJsonLimits => ({ maxBytes: bytes, maxNodes: 100_000, maxDepth: 64 });

/** Runs the reusable editorial pipeline. This never awards rendered readiness or
 * authorship, and has no default provider, filesystem or live lifecycle adapter.
 */
export async function runGenerationPipeline(request: PipelineRequest, ports: PipelinePorts, signal: AbortSignal): Promise<PipelineResult> {
  const receipts: StageReceipt[] = [];
  const artifacts: ValidatedStageOutput[] = [];
  let calls = 0;
  let usage = 0;
  let inputBytes = 0;
  let outputBytes = 0;
  const stop: (reason: StopReason) => never = (reason) => { throw new PipelineStop(reason); };
  try {
    const b = request.budget;
    if (![request.requestId, request.projectId, request.snapshotId, request.providerRoute, b.accountingPolicy].every(x => typeof x === 'string' && x.length > 0)
      || ![b.maxCalls, b.maxInputBytes, b.maxOutputBytes, b.maxUsageUnits, b.maxElapsedMs].every(x => Number.isSafeInteger(x) && x > 0)
      || !Number.isSafeInteger(b.maxRepairCycles) || b.maxRepairCycles < 0
      || !Number.isSafeInteger(request.startedAt) || request.startedAt > ports.now()
      || !Number.isSafeInteger(request.startedAt + b.maxElapsedMs)) stop('invalid-request');
    // Detach caller-owned mutable inputs before the first asynchronous boundary.
    const frozen = JSON.parse(encodeCanonicalJson(request, dataLimits(b.maxInputBytes))) as PipelineRequest;
    const budget = frozen.budget;
    const deadline = frozen.startedAt + budget.maxElapsedMs;
    const check = (): void => {
      if (signal.aborted) stop('cancelled');
      if (ports.now() >= deadline) stop('deadline');
    };
    const bounded = async <T>(job: () => Promise<T>, allowExpired = false): Promise<T> => {
      if (!allowExpired) check();
      let timer: ReturnType<typeof setTimeout> | undefined;
      let cancel!: () => void;
      const interruption = new Promise<never>((_, reject) => {
        cancel = () => reject(new PipelineStop('cancelled'));
        const arm = (): void => {
          const remaining = deadline - ports.now();
          if (remaining <= 0) reject(new PipelineStop('deadline'));
          else timer = setTimeout(arm, Math.min(remaining, 2_147_483_647));
        };
        signal.addEventListener('abort', cancel, { once: true });
        arm();
        if (signal.aborted) cancel();
      });
      try { return await Promise.race([Promise.resolve().then(job), interruption]); }
      finally { clearTimeout(timer); signal.removeEventListener('abort', cancel); }
    };
    check();
    if (!await bounded(() => ports.verifySources(frozen))) stop('source-refused');
    const context: Record<string, unknown> = { sources: frozen.sources, readerQuestions: frozen.readerQuestions };
    const stage = async (name: GenerationStage, inputs: Readonly<Record<string, unknown>>): Promise<unknown> => {
      check();
      if (calls >= budget.maxCalls) stop('budget-exhausted');
      const prompt = promptForStage(name);
      const schema = ports.responseSchema(name);
      const envelope = { promptVersion: prompt.version, system: prompt.system, responseSchemaVersion: schema.version, responseSchema: schema.schema, inputs };
      const encoded = encodeCanonicalJson(envelope, dataLimits(budget.maxInputBytes));
      const size = Buffer.byteLength(encoded, 'utf8');
      if (inputBytes + size > budget.maxInputBytes || outputBytes >= budget.maxOutputBytes || usage >= budget.maxUsageUnits) stop('budget-exhausted');
      const input: AttemptInput = {
        requestId: frozen.requestId, projectId: frozen.projectId, snapshotId: frozen.snapshotId,
        providerRoute: frozen.providerRoute, stage: name, ordinal: calls,
        inputDigest: digestCanonicalJson(envelope, dataLimits(budget.maxInputBytes)).digest,
        inputBytes: size, deadline, budget,
      };
      const permit = await bounded(() => ports.admit(input));
      if (!permit) stop('admission-refused');
      if (!Number.isSafeInteger(permit.maxUsageUnits) || permit.maxUsageUnits <= 0 || permit.maxUsageUnits > budget.maxUsageUnits - usage
        || !Number.isSafeInteger(permit.maxOutputBytes) || permit.maxOutputBytes <= 0 || permit.maxOutputBytes > budget.maxOutputBytes - outputBytes) {
        await bounded(() => ports.releaseUnsent(permit), true);
        stop('budget-exhausted');
      }
      const permitted = await bounded(() => ports.permitted(input, permit));
      if (signal.aborted || ports.now() >= deadline || !permitted) {
        await bounded(() => ports.releaseUnsent(permit), true);
        check();
        stop('admission-refused');
      }
      // Admission is already durable. Any exception from this point is potentially sent.
      calls++;
      inputBytes += size;
      const controller = new AbortController();
      let timer: ReturnType<typeof setTimeout> | undefined;
      let interrupted = false;
      let interrupt!: (reason: StopReason) => void;
      const interruption = new Promise<never>((_, reject) => {
        interrupt = reason => { interrupted = true; controller.abort(); reject(new PipelineStop(reason)); };
      });
      const cancel = (): void => interrupt('cancelled');
      signal.addEventListener('abort', cancel, { once: true });
      const armDeadline = (): void => {
        const remaining = deadline - ports.now();
        if (remaining <= 0) interrupt('deadline');
        else timer = setTimeout(armDeadline, Math.min(remaining, 2_147_483_647));
      };
      armDeadline();
      const pending = Promise.resolve().then(() => {
        if (controller.signal.aborted) throw new PipelineStop(signal.aborted ? 'cancelled' : 'deadline');
        return ports.generate({ permit: permit, stage: name, system: prompt.system, input: encoded, responseSchema: JSON.parse(encoded).responseSchema, signal: controller.signal });
      });
      let reply: ProviderReply;
      try {
        reply = await Promise.race([pending, interruption]);
      } catch (error) {
        // The adapter owns durable late capture even if the caller stops awaiting.
        if (interrupted) void pending.then(r => ports.lateReceipt(permit, { model: r.model, usageUnits: r.usageUnits }), () => undefined).catch(() => undefined);
        await bounded(() => ports.record(permit, { kind: 'effect-uncertain', usageUnits: null }), true);
        if (error instanceof PipelineStop) throw error;
        stop('effect-uncertain');
      } finally {
        clearTimeout(timer);
        signal.removeEventListener('abort', cancel);
      }
      if (reply.usageUnits === null || !Number.isSafeInteger(reply.usageUnits) || reply.usageUnits < 0 || reply.usageUnits > permit.maxUsageUnits) {
        await bounded(() => ports.record(permit, { kind: 'usage-uncertain', usageUnits: null }), true);
        stop('usage-uncertain');
      }
      const actualUsage = reply.usageUnits;
      usage += actualUsage;
      let validated: unknown;
      let digest: string;
      try {
        const parsed = parseBoundedJson(reply.body, dataLimits(permit.maxOutputBytes));
        validated = ports.validate(name, parsed, context);
        const bytes = encodeCanonicalJson(validated, dataLimits(permit.maxOutputBytes));
        validated = JSON.parse(bytes);
        digest = digestCanonicalJson(validated, dataLimits(permit.maxOutputBytes)).digest;
        outputBytes += Buffer.byteLength(reply.body, 'utf8');
      } catch {
        await bounded(() => ports.record(permit, { kind: 'invalid-output', usageUnits: actualUsage }), true);
        stop('invalid-output');
      }
      await bounded(() => ports.record(permit, { kind: 'validated', outputDigest: digest, model: reply.model, usageUnits: actualUsage }), true);
      receipts.push({ stage: name, attemptId: permit.attemptId, inputDigest: input.inputDigest, outputDigest: digest, promptVersion: prompt.version });
      artifacts.push({ stage: name, value: validated });
      check();
      return validated;
    };
    context.inventory = await stage('inventory', { sources: context.sources, readerQuestions: context.readerQuestions });
    context.plan = await stage('plan', context);
    context.draft = await stage('author', context);
    context.draft = await stage('edit', context);
    let review = await stage('fidelity', context);
    let verdict = ports.fidelity(review);
    for (let repairs = 0; verdict.blocking; repairs++) {
      if (repairs >= budget.maxRepairCycles) stop('repair-exhausted');
      context.draft = await stage('repair', { ...context, findings: verdict.findings });
      review = await stage('fidelity', context);
      verdict = ports.fidelity(review);
    }
    check();
    return { status: 'awaiting-rendered-review', draft: context.draft, inventory: context.inventory, review, receipts, artifacts };
  } catch (error) {
    return { status: 'stopped', reason: error instanceof PipelineStop ? error.reason : 'adapter-failure', receipts, artifacts };
  }
}
