import { mkdirSync, readdirSync } from 'node:fs';
import { isAbsolute, join } from 'node:path';
import { query as sdkQuery, type Options } from '@anthropic-ai/claude-agent-sdk';
import type { PipelinePorts, ProviderReply } from '@syzygy/polaris-generation-core';

type GenerateInput = Parameters<PipelinePorts['generate']>[0];

/** Every built-in tool name the CLI listed as deniable (CLI 2.1.288). `tools: []`
 * already removes them; this list is the belt to that brace. */
export const AGENT_SDK_BUILTIN_TOOLS: readonly string[] = [
  'Agent', 'Bash', 'ExitPlanMode', 'Read', 'Edit', 'Write', 'NotebookEdit', 'WebFetch', 'WebSearch', 'TodoWrite', 'TaskStop',
  'AskUserQuestion', 'Skill', 'EnterPlanMode', 'TaskCreate', 'TaskGet', 'TaskUpdate', 'TaskList', 'LSP', 'EnterWorktree',
  'ExitWorktree', 'SendMessage', 'Workflow', 'CronCreate', 'CronDelete', 'CronList', 'Monitor', 'Glob', 'Grep',
  'ListMcpResourcesTool', 'ReadMcpResourceTool', 'GetTask',
];

export type AgentSdkProviderFailure = 'invalid-config' | 'cwd-not-empty' | 'aborted' | 'rate-limited' | 'provider-error' | 'no-output' | 'transport-failed';

/** Messages are code-only: they never carry the request, the reply or a credential. */
export class AgentSdkProviderError extends Error {
  constructor(readonly code: AgentSdkProviderFailure, readonly attempts: number, readonly status: number | null = null) { super(code); }
}

export interface AgentSdkAttemptRecord {
  readonly attemptId: string;
  readonly try: number;
  readonly outcome: 'completed' | 'rate-limited' | 'overloaded' | 'failed' | 'aborted';
  readonly httpStatus: number | null;
  /** Token total as reported by the CLI for this try, or null when it reported none. */
  readonly usageUnits: number | null;
  readonly backoffMs: number;
}

export interface AgentSdkProviderConfig {
  /** Absolute, existing directory outside git. All runtime state of the CLI lives under it. */
  readonly runDir: string;
  readonly model: string;
  readonly effort?: 'low' | 'medium' | 'high' | 'xhigh' | 'max';
  /** The only credential admitted; no subscription login or inherited environment. */
  readonly auth: { readonly apiKey: string };
  /** Test and acceptance runs point this at a local capture endpoint. */
  readonly baseUrl?: string;
  /** 'text' sends no tool; 'schema-tool' lets the SDK add its StructuredOutput tool. */
  readonly outputMode?: 'text' | 'schema-tool';
  readonly retry?: { readonly maxAttempts: number; readonly baseDelayMs: number; readonly maxDelayMs: number; readonly budgetMs: number };
  /** Extra environment names for diagnostics (a recording proxy); never part of an accepted route. */
  readonly diagnosticEnv?: Readonly<Record<string, string>>;
  readonly sleep?: (ms: number, signal: AbortSignal) => Promise<void>;
  readonly now?: () => number;
  readonly onAttempt?: (record: AgentSdkAttemptRecord) => void;
  readonly query?: typeof sdkQuery;
}

export interface AgentSdkProviderHandle {
  readonly generate: PipelinePorts['generate'];
  /** Every try made so far, retries included, in order. */
  readonly attempts: () => readonly AgentSdkAttemptRecord[];
  /** Absolute path of the empty working directory handed to the CLI. */
  readonly cwd: string;
}

const DEFAULT_RETRY = { maxAttempts: 4, baseDelayMs: 2_000, maxDelayMs: 60_000, budgetMs: 180_000 };
const abortableSleep = (ms: number, signal: AbortSignal): Promise<void> => new Promise((resolve, reject) => {
  if (signal.aborted) { reject(new AgentSdkProviderError('aborted', 0)); return; }
  const timer = setTimeout(() => { signal.removeEventListener('abort', onAbort); resolve(); }, ms);
  const onAbort = (): void => { clearTimeout(timer); reject(new AgentSdkProviderError('aborted', 0)); };
  signal.addEventListener('abort', onAbort, { once: true });
});

/** The complete subprocess environment. Nothing is inherited from process.env;
 * every name here is chosen, and all state paths point into the run directory. */
export function agentSdkEnvironment(config: Pick<AgentSdkProviderConfig, 'runDir' | 'auth' | 'baseUrl' | 'diagnosticEnv'>, maxOutputTokens: number): Record<string, string> {
  const dir = (name: string): string => join(config.runDir, name);
  return {
    HOME: dir('home'), CLAUDE_CONFIG_DIR: dir('config'), TMPDIR: dir('tmp'),
    XDG_CONFIG_HOME: dir('xdg-config'), XDG_CACHE_HOME: dir('xdg-cache'), XDG_DATA_HOME: dir('xdg-data'), XDG_STATE_HOME: dir('xdg-state'),
    ANTHROPIC_API_KEY: config.auth.apiKey,
    ...(config.baseUrl === undefined ? {} : { ANTHROPIC_BASE_URL: config.baseUrl }),
    DISABLE_TELEMETRY: '1', CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: '1', DISABLE_ERROR_REPORTING: '1', DISABLE_AUTOUPDATER: '1',
    // Bare mode, no attribution block, no thinking block, no CLI-side retry (this adapter owns retry and its receipts).
    CLAUDE_CODE_SIMPLE: '1', CLAUDE_CODE_ATTRIBUTION_HEADER: '0', CLAUDE_CODE_DISABLE_THINKING: '1', CLAUDE_CODE_MAX_RETRIES: '0',
    CLAUDE_CODE_DISABLE_AUTO_MEMORY: '1', CLAUDE_CODE_DISABLE_CLAUDE_MDS: '1',
    CLAUDE_CODE_MAX_OUTPUT_TOKENS: String(maxOutputTokens),
    ...config.diagnosticEnv,
  };
}

interface ResultLike {
  readonly subtype?: string; readonly is_error?: boolean; readonly api_error_status?: number | null;
  readonly result?: unknown; readonly structured_output?: unknown;
  readonly usage?: { readonly input_tokens?: unknown; readonly output_tokens?: unknown; readonly cache_creation_input_tokens?: unknown; readonly cache_read_input_tokens?: unknown };
}

/** Accounting policy 'agent-sdk-tokens-v1': usage units are input, cache-creation, cache-read and output tokens summed. */
const tokenUnits = (usage: ResultLike['usage']): number | null => {
  if (usage === undefined || usage === null) return null;
  const parts = [usage.input_tokens, usage.output_tokens, usage.cache_creation_input_tokens ?? 0, usage.cache_read_input_tokens ?? 0];
  return parts.every(p => typeof p === 'number' && Number.isSafeInteger(p) && p >= 0) ? (parts as number[]).reduce((a, b) => a + b, 0) : null;
};

export function createAgentSdkGenerate(config: AgentSdkProviderConfig): AgentSdkProviderHandle {
  if (!isAbsolute(config.runDir) || config.model.length === 0 || config.auth.apiKey.length === 0) throw new AgentSdkProviderError('invalid-config', 0);
  const retry = config.retry ?? DEFAULT_RETRY;
  if (![retry.maxAttempts, retry.baseDelayMs, retry.maxDelayMs, retry.budgetMs].every(x => Number.isSafeInteger(x) && x >= 0) || retry.maxAttempts < 1) throw new AgentSdkProviderError('invalid-config', 0);
  const query = config.query ?? sdkQuery;
  const sleep = config.sleep ?? abortableSleep;
  const now = config.now ?? Date.now;
  const mode = config.outputMode ?? 'text';
  const effort = config.effort ?? 'medium';
  for (const name of ['cwd', 'home', 'config', 'tmp', 'xdg-config', 'xdg-cache', 'xdg-data', 'xdg-state']) mkdirSync(join(config.runDir, name), { recursive: true });
  const cwd = join(config.runDir, 'cwd');
  const attempts: AgentSdkAttemptRecord[] = [];
  const record = (entry: AgentSdkAttemptRecord): void => { attempts.push(entry); config.onAttempt?.(entry); };

  const generate: PipelinePorts['generate'] = async (input: GenerateInput): Promise<ProviderReply> => {
    // A non-empty working directory means something other than this adapter wrote there.
    if (readdirSync(cwd).length !== 0) throw new AgentSdkProviderError('cwd-not-empty', 0);
    const maxTokens = Math.max(1, Math.min(input.permit.maxOutputBytes, input.permit.maxUsageUnits));
    const started = now();
    let totalUnits: number | null = 0;
    for (let n = 1; ; n++) {
      if (input.signal.aborted) throw new AgentSdkProviderError('aborted', n - 1);
      const controller = new AbortController();
      const forward = (): void => controller.abort();
      input.signal.addEventListener('abort', forward, { once: true });
      let result: ResultLike | undefined;
      let model: string | null = null;
      const options: Options = {
        systemPrompt: input.system, settingSources: [], mcpServers: {}, strictMcpConfig: true, tools: [], allowedTools: [],
        disallowedTools: [...AGENT_SDK_BUILTIN_TOOLS], cwd, env: agentSdkEnvironment(config, maxTokens), model: config.model, effort,
        maxTurns: 1, persistSession: false, permissionMode: 'default', abortController: controller,
        ...(mode === 'schema-tool' ? { outputFormat: { type: 'json_schema' as const, schema: input.responseSchema as Record<string, unknown> } } : {}),
      };
      const q = query({ prompt: input.input, options });
      try {
        for await (const message of q) {
          const m = message as { type?: string; message?: { model?: unknown } };
          if (m.type === 'assistant' && typeof m.message?.model === 'string' && m.message.model !== '<synthetic>') model = m.message.model;
          if (m.type === 'result') result = message as unknown as ResultLike;
        }
      } catch { /* the result message, if any, was already read; absence is handled below */ }
      finally { input.signal.removeEventListener('abort', forward); q.close(); }
      const units = result === undefined ? null : tokenUnits(result.usage);
      if (input.signal.aborted) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'aborted', httpStatus: null, usageUnits: units, backoffMs: 0 }); throw new AgentSdkProviderError('aborted', n); }
      totalUnits = totalUnits === null || units === null ? null : totalUnits + units;
      if (result === undefined) { record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: null, usageUnits: null, backoffMs: 0 }); throw new AgentSdkProviderError('transport-failed', n); }
      const status = typeof result.api_error_status === 'number' ? result.api_error_status : null;
      if (result.is_error === true && (status === 429 || status === 529)) {
        const delay = Math.min(retry.maxDelayMs, retry.baseDelayMs * 2 ** (n - 1));
        const more = n < retry.maxAttempts && now() - started + delay <= retry.budgetMs;
        record({ attemptId: input.permit.attemptId, try: n, outcome: status === 429 ? 'rate-limited' : 'overloaded', httpStatus: status, usageUnits: units, backoffMs: more ? delay : 0 });
        if (!more) throw new AgentSdkProviderError('rate-limited', n, status);
        await sleep(delay, input.signal);
        continue;
      }
      if (result.is_error === true || result.subtype !== 'success') {
        record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: status, usageUnits: units, backoffMs: 0 });
        throw new AgentSdkProviderError('provider-error', n, status);
      }
      const body = mode === 'schema-tool' ? (result.structured_output === undefined ? undefined : JSON.stringify(result.structured_output)) : result.result;
      if (typeof body !== 'string') {
        record({ attemptId: input.permit.attemptId, try: n, outcome: 'failed', httpStatus: status, usageUnits: units, backoffMs: 0 });
        throw new AgentSdkProviderError('no-output', n);
      }
      record({ attemptId: input.permit.attemptId, try: n, outcome: 'completed', httpStatus: status, usageUnits: units, backoffMs: 0 });
      return { body, model, usageUnits: totalUnits };
    }
  };
  return { generate, attempts: () => attempts, cwd };
}
