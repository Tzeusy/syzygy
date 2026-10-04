import { mkdirSync, readFileSync, readdirSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, isAbsolute, join } from 'node:path';
import { query as sdkQuery, type Options } from '@anthropic-ai/claude-agent-sdk';
import type { DispatchPermit, PipelinePorts, PromptStage, ProviderReply } from '@syzygy/polaris-generation-core';
import { assertAllowedUpstream, startEgressGate, type EgressGate, type EgressGateOptions } from './egress-gate.js';
import { MAX_OUTPUT_TOKENS, countedUnits, outputTokenCap, tokenUnits } from './usage-units.js';
import { PINNED_AGENT_SDK_VERSION, PINNED_CLAUDE_CODE_VERSION, acceptCapturedRequest, type ExpectedRequest } from './request-acceptance.js';

export { PINNED_AGENT_SDK_VERSION, PINNED_CLAUDE_CODE_VERSION };

type GenerateInput = Parameters<PipelinePorts['generate']>[0];

/** Every built-in tool name the CLI listed as deniable (CLI 2.1.288). `tools: []`
 * already removes them; this list is the belt to that brace. */
export const AGENT_SDK_BUILTIN_TOOLS: readonly string[] = [
  'Agent', 'Bash', 'ExitPlanMode', 'Read', 'Edit', 'Write', 'NotebookEdit', 'WebFetch', 'WebSearch', 'TodoWrite', 'TaskStop',
  'AskUserQuestion', 'Skill', 'EnterPlanMode', 'TaskCreate', 'TaskGet', 'TaskUpdate', 'TaskList', 'LSP', 'EnterWorktree',
  'ExitWorktree', 'SendMessage', 'Workflow', 'CronCreate', 'CronDelete', 'CronList', 'Monitor', 'Glob', 'Grep',
  'ListMcpResourcesTool', 'ReadMcpResourceTool', 'GetTask',
];

export type AgentSdkProviderFailure = 'unpinned-version' | 'invalid-config' | 'cwd-not-empty' | 'concurrent-call' | 'aborted' | 'deadline'
  | 'egress-refused' | 'rate-limited' | 'provider-error' | 'no-output' | 'transport-failed' | 'budget-too-small';

/** Messages are code-only: they never carry the request, the reply or a credential. */
export class AgentSdkProviderError extends Error {
  /** Tokens billed across the tries made so far; null when any try reported none. */
  spentUnits: number | null = 0;
  constructor(readonly code: AgentSdkProviderFailure, readonly attempts: number, readonly status: number | null = null) { super(code); }
}

export interface AgentSdkAttemptRecord {
  readonly attemptId: string;
  readonly try: number;
  readonly outcome: 'completed' | 'rate-limited' | 'overloaded' | 'failed' | 'aborted' | 'refused';
  readonly httpStatus: number | null;
  /** Token total as reported by the CLI for this try, or null when it reported none. */
  readonly usageUnits: number | null;
  readonly backoffMs: number;
}

/** What the profile may choose for thinking. 'adaptive' adds the bytes listed in PROVIDER-EGRESS-BYTES.md. */
export type ThinkingProfile = 'off' | 'adaptive';
const DIAGNOSTIC_ENV_KEYS: ReadonlySet<string> = new Set(['HTTP_PROXY', 'HTTPS_PROXY', 'NO_PROXY']);

export interface AgentSdkProviderConfig {
  /** Absolute, existing directory outside git. All runtime state of the CLI lives under it. */
  readonly runDir: string;
  readonly model: string;
  /** Profile-set: the run profile's Opus effort level. */
  readonly effort?: 'low' | 'medium' | 'high' | 'xhigh' | 'max';
  /** Profile-set: 'off' (default) or 'adaptive'. */
  readonly thinking?: ThinkingProfile;
  /** Profile-set: output token cap; the permit's allowances can only lower it. */
  readonly maxOutputTokens?: number;
  /** The only credential admitted; no subscription login or inherited environment. */
  readonly auth: { readonly apiKey: string };
  /** The egress gate forwards here and nowhere else. Absent: every request is refused (tests that only probe the gate). */
  readonly upstream?: EgressGateOptions['upstream'];
  /** Consent switch, asked by the gate for every request (a discovery call names its discovery stage). Only `true` permits. */
  readonly permitted: (permit: DispatchPermit, stage: PromptStage) => Promise<boolean>;
  /** Gate option: drop the OS, architecture and runtime-version headers before forwarding (default false). */
  readonly stripFingerprint?: boolean;
  /** 'text' sends no tool; 'schema-tool' lets the SDK add its StructuredOutput tool. */
  readonly outputMode?: 'text' | 'schema-tool';
  readonly retry?: { readonly maxAttempts: number; readonly baseDelayMs: number; readonly maxDelayMs: number; readonly budgetMs: number };
  /** Proxy variables only (HTTP_PROXY, HTTPS_PROXY, NO_PROXY); anything else is refused. */
  readonly diagnosticEnv?: Readonly<Record<string, string>>;
  /** Test seam for the version check; production uses the pinned constants. */
  readonly pin?: { readonly sdk: string; readonly cli: string };
  readonly sleep?: (ms: number, signal: AbortSignal) => Promise<void>;
  readonly now?: () => number;
  readonly onAttempt?: (record: AgentSdkAttemptRecord) => void;
  readonly query?: typeof sdkQuery;
}

export interface AgentSdkProviderHandle {
  readonly generate: PipelinePorts['generate'];
  /** Every try made so far, retries included, in order. */
  readonly attempts: () => readonly AgentSdkAttemptRecord[];
  /** Gate decisions so far, in order (content-free). */
  readonly gateDecisions: () => readonly import('./egress-gate.js').GateDecision[];
  /** Loopback URL of the gate once started (diagnostics and isolation tests). */
  readonly gateUrl: () => string | undefined;
  /** Absolute path of the empty working directory handed to the CLI. */
  readonly cwd: string;
  /** Stops the loopback gate. */
  readonly close: () => Promise<void>;
}

const DEFAULT_RETRY = { maxAttempts: 4, baseDelayMs: 2_000, maxDelayMs: 60_000, budgetMs: 180_000 };
const abortableSleep = (ms: number, signal: AbortSignal): Promise<void> => new Promise((resolve, reject) => {
  if (signal.aborted) { reject(new AgentSdkProviderError('aborted', 0)); return; }
  const timer = setTimeout(() => { signal.removeEventListener('abort', onAbort); resolve(); }, ms);
  const onAbort = (): void => { clearTimeout(timer); reject(new AgentSdkProviderError('aborted', 0)); };
  signal.addEventListener('abort', onAbort, { once: true });
});

/** The complete subprocess environment. Nothing is inherited from process.env;
 * every name here is chosen, and all state paths point into the run directory.
 * `gateUrl` is the adapter's own loopback egress gate, never a provider. */
export function agentSdkEnvironment(config: Pick<AgentSdkProviderConfig, 'runDir' | 'auth' | 'diagnosticEnv'>, gateUrl: string, maxOutputTokens: number): Record<string, string> {
  const dir = (name: string): string => join(config.runDir, name);
  const base: Record<string, string> = {
    HOME: dir('home'), CLAUDE_CONFIG_DIR: dir('config'), TMPDIR: dir('tmp'),
    XDG_CONFIG_HOME: dir('xdg-config'), XDG_CACHE_HOME: dir('xdg-cache'), XDG_DATA_HOME: dir('xdg-data'), XDG_STATE_HOME: dir('xdg-state'),
    ANTHROPIC_API_KEY: config.auth.apiKey, ANTHROPIC_BASE_URL: gateUrl,
    DISABLE_TELEMETRY: '1', CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: '1', DISABLE_ERROR_REPORTING: '1', DISABLE_AUTOUPDATER: '1',
    // Bare mode, no attribution block, no CLI-side retry (this adapter owns retry and its receipts).
    CLAUDE_CODE_SIMPLE: '1', CLAUDE_CODE_ATTRIBUTION_HEADER: '0', CLAUDE_CODE_MAX_RETRIES: '0',
    CLAUDE_CODE_DISABLE_AUTO_MEMORY: '1', CLAUDE_CODE_DISABLE_CLAUDE_MDS: '1',
    CLAUDE_CODE_MAX_OUTPUT_TOKENS: String(maxOutputTokens),
  };
  for (const [key, value] of Object.entries(config.diagnosticEnv ?? {})) {
    if (!DIAGNOSTIC_ENV_KEYS.has(key) || key in base) throw new AgentSdkProviderError('invalid-config', 0);
    base[key] = value;
  }
  return base;
}

interface ResultLike {
  readonly subtype?: string; readonly is_error?: boolean; readonly api_error_status?: number | null;
  readonly result?: unknown; readonly structured_output?: unknown;
  readonly usage?: { readonly input_tokens?: unknown; readonly output_tokens?: unknown; readonly cache_creation_input_tokens?: unknown; readonly cache_read_input_tokens?: unknown };
}

/** Accounting policy `dossier-units-v1` (usage-units.ts): input, cache-creation, cache-read and output tokens summed, in 1,000-token units rounded up. */
const usageUnitsOf = (usage: ResultLike['usage']): number | null => (usage === undefined || usage === null ? null
  : tokenUnits([usage.input_tokens, usage.output_tokens, usage.cache_creation_input_tokens ?? 0, usage.cache_read_input_tokens ?? 0]));

export function createAgentSdkGenerate(config: AgentSdkProviderConfig): AgentSdkProviderHandle {
  if (!isAbsolute(config.runDir) || config.model.length === 0 || config.auth.apiKey.length === 0) throw new AgentSdkProviderError('invalid-config', 0);
  const retry = config.retry ?? DEFAULT_RETRY;
  if (![retry.maxAttempts, retry.baseDelayMs, retry.maxDelayMs, retry.budgetMs].every(x => Number.isSafeInteger(x) && x >= 0) || retry.maxAttempts < 1) throw new AgentSdkProviderError('invalid-config', 0);
  const pin = config.pin ?? { sdk: PINNED_AGENT_SDK_VERSION, cli: PINNED_CLAUDE_CODE_VERSION };
  const installed = (JSON.parse(readFileSync(join(dirname(createRequire(import.meta.url).resolve('@anthropic-ai/claude-agent-sdk')), 'package.json'), 'utf8')) as { version?: string }).version;
  if (installed !== pin.sdk) throw new AgentSdkProviderError('unpinned-version', 0);
  if (config.maxOutputTokens !== undefined && !(Number.isSafeInteger(config.maxOutputTokens) && config.maxOutputTokens > 0)) throw new AgentSdkProviderError('invalid-config', 0);
  agentSdkEnvironment(config, 'http://127.0.0.1:1', 1);   // validates diagnosticEnv at construction
  if (config.upstream !== undefined) { try { assertAllowedUpstream(config.upstream.url, config.upstream.loopbackForTests); } catch { throw new AgentSdkProviderError('invalid-config', 0); } }
  const query = config.query ?? sdkQuery;
  const sleep = config.sleep ?? abortableSleep;
  const now = config.now ?? Date.now;
  const mode = config.outputMode ?? 'text';
  const effort = config.effort ?? 'medium';
  const thinking: ThinkingProfile = config.thinking ?? 'off';
  for (const name of ['cwd', 'home', 'config', 'tmp', 'xdg-config', 'xdg-cache', 'xdg-data', 'xdg-state']) mkdirSync(join(config.runDir, name), { recursive: true });
  const cwd = join(config.runDir, 'cwd');
  const attempts: AgentSdkAttemptRecord[] = [];
  const record = (entry: AgentSdkAttemptRecord): void => { attempts.push(entry); config.onAttempt?.(entry); };
  let gateRef: EgressGate | undefined;
  let gatePromise: Promise<{ gate: EgressGate; permit: { current: { permit: DispatchPermit; stage: PromptStage } | null } }> | undefined;
  const gateFor = (): NonNullable<typeof gatePromise> => gatePromise ??= (async () => {
    const permit: { current: { permit: DispatchPermit; stage: PromptStage } | null } = { current: null };
    const gate = await startEgressGate({
      ...(config.upstream === undefined ? {} : { upstream: config.upstream }),
      permitted: async () => (permit.current === null ? false : config.permitted(permit.current.permit, permit.current.stage)),
      ...(config.stripFingerprint === undefined ? {} : { stripFingerprint: config.stripFingerprint }),
    });
    gateRef = gate;
    return { gate, permit };
  })();

  const generate: PipelinePorts['generate'] = async (input: GenerateInput): Promise<ProviderReply> => {
    // A non-empty working directory means something other than this adapter wrote there.
    if (readdirSync(cwd).length !== 0) throw new AgentSdkProviderError('cwd-not-empty', 0);
    const { gate, permit: slot } = await gateFor();
    const maxTokens = outputTokenCap(input.permit, input.system, input.input, config.maxOutputTokens ?? MAX_OUTPUT_TOKENS);
    if (maxTokens === null) throw new AgentSdkProviderError('budget-too-small', 0);   // nothing was armed or sent
    const expected: ExpectedRequest = { model: config.model, system: input.system, input: input.input, effort, maxTokens, thinking, apiKey: config.auth.apiKey,
      ...(mode === 'schema-tool' ? { responseSchema: input.responseSchema } : {}) };
    const started = now();
    let totalUnits: number | null = 0;
    const fail = (code: AgentSdkProviderFailure, n: number, status: number | null = null): AgentSdkProviderError => {
      const error = new AgentSdkProviderError(code, n, status);
      error.spentUnits = totalUnits;
      return error;
    };
    for (let n = 1; ; n++) {
      if (input.signal.aborted) throw fail('aborted', n - 1);
      const remaining = retry.budgetMs - (now() - started);
      if (remaining <= 0) throw fail('deadline', n - 1);
      if (!gate.arm(captured => acceptCapturedRequest(captured, expected))) throw fail('concurrent-call', n - 1);
      slot.current = { permit: input.permit, stage: input.stage };
      const decisionsBefore = gate.decisions.length;
      const controller = new AbortController();
      const forward = (): void => controller.abort();
      let timedOut = false;
      const timer = setTimeout(() => { timedOut = true; controller.abort(); }, remaining);
      input.signal.addEventListener('abort', forward, { once: true });
      let result: ResultLike | undefined;
      let model: string | null = null;
      let versionMismatch = false;
      let q: ReturnType<typeof sdkQuery> | undefined;
      try {
        const options: Options = {
          systemPrompt: input.system, settingSources: [], mcpServers: {}, strictMcpConfig: true, tools: [], allowedTools: [],
          disallowedTools: [...AGENT_SDK_BUILTIN_TOOLS], cwd, env: agentSdkEnvironment(config, gate.url, maxTokens), model: config.model, effort,
          thinking: thinking === 'adaptive' ? { type: 'adaptive' } : { type: 'disabled' },
          maxTurns: 1, persistSession: false, permissionMode: 'default', abortController: controller,
          ...(mode === 'schema-tool' ? { outputFormat: { type: 'json_schema' as const, schema: input.responseSchema as Record<string, unknown> } } : {}),
        };
        q = query({ prompt: input.input, options });
        for await (const message of q) {
          const m = message as { type?: string; message?: { model?: unknown } };
          if (m.type === 'system' && (message as { subtype?: string }).subtype === 'init' && (message as { claude_code_version?: string }).claude_code_version !== pin.cli) { versionMismatch = true; controller.abort(); }
          if (m.type === 'assistant' && typeof m.message?.model === 'string' && m.message.model !== '<synthetic>') model = m.message.model;
          if (m.type === 'result') result = message as unknown as ResultLike;
        }
      } catch { /* the result message, if any, was already read; absence is handled below */ }
      finally { clearTimeout(timer); input.signal.removeEventListener('abort', forward); q?.close(); gate.disarm(); slot.current = null; }
      const refusedHere = gate.decisions.slice(decisionsBefore).filter(d => d.decision === 'refused');
      const rejectedStatus = result?.is_error === true && (result.api_error_status === 429 || result.api_error_status === 529);
      // A rejected request counts as unbilled only on the provider's own error body, seen by the gate; the CLI's synthetic zero usage is not evidence.
      const units = result === undefined ? null : rejectedStatus ? (gate.takeRejectedUnbilled() ? 0 : null) : usageUnitsOf(result.usage);
      totalUnits = totalUnits === null || units === null ? null : totalUnits + units;
      if (input.signal.aborted) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'aborted', httpStatus: null, usageUnits: units, backoffMs: 0 }); throw fail('aborted', n); }
      if (timedOut) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'aborted', httpStatus: null, usageUnits: units, backoffMs: 0 }); throw fail('deadline', n); }
      if (versionMismatch) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: null, usageUnits: null, backoffMs: 0 }); throw fail('unpinned-version', n); }
      if (refusedHere.length > 0) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'refused', httpStatus: 403, usageUnits: units, backoffMs: 0 }); throw fail('egress-refused', n, 403); }
      if (result === undefined) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: null, usageUnits: null, backoffMs: 0 }); throw fail('transport-failed', n); }
      const status = typeof result.api_error_status === 'number' ? result.api_error_status : null;
      if (result.is_error === true && (status === 429 || status === 529)) {
        const delay = Math.max(Math.min(retry.maxDelayMs, retry.baseDelayMs * 2 ** (n - 1)), gate.takeRetryAfterMs() ?? 0);
        // A try whose billing is unknown has used the call's whole ceiling: no further try is made.
        const more = totalUnits !== null && n < retry.maxAttempts && now() - started + delay <= retry.budgetMs;
        record({ attemptId: input.permit.attemptId, try: n, outcome: status === 429 ? 'rate-limited' : 'overloaded', httpStatus: status, usageUnits: units, backoffMs: more ? delay : 0 });
        if (!more) throw fail('rate-limited', n, status);
        await sleep(delay, input.signal);
        continue;
      }
      if (result.is_error === true || result.subtype !== 'success') {
        record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: status, usageUnits: units, backoffMs: 0 });
        throw fail('provider-error', n, status);
      }
      const body = mode === 'schema-tool' ? (result.structured_output === undefined ? undefined : JSON.stringify(result.structured_output)) : result.result;
      if (typeof body !== 'string') {
        record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: status, usageUnits: units, backoffMs: 0 });
        throw fail('no-output', n);
      }
      record({ attemptId: input.permit.attemptId, try: n, outcome: 'completed', httpStatus: status, usageUnits: units, backoffMs: 0 });
      return { body, model, usageUnits: countedUnits(totalUnits, input.permit) };
    }
  };
  return {
    generate, attempts: () => attempts, cwd, gateUrl: () => gateRef?.url,
    gateDecisions: () => (gateRef === undefined ? [] : [...gateRef.decisions]),
    close: async () => { if (gateRef !== undefined) await gateRef.close(); },
  };
}
