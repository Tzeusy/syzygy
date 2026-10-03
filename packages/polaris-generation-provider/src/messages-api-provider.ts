import Anthropic from '@anthropic-ai/sdk';
import type { PipelinePorts, ProviderReply } from '@syzygy/polaris-generation-core';
import type { CapturedRequest, RequestAcceptance } from './request-acceptance.js';

/** Version the capture test ran against; a bump re-runs it. */
export const PINNED_MESSAGES_SDK_VERSION = '0.131.0';

export type MessagesApiFailure = 'invalid-config' | 'aborted' | 'rate-limited' | 'provider-error' | 'no-output';
export class MessagesApiProviderError extends Error {
  constructor(readonly code: MessagesApiFailure, readonly attempts: number, readonly status: number | null = null) { super(code); }
}

export interface MessagesApiAttemptRecord {
  readonly attemptId: string;
  readonly try: number;
  readonly outcome: 'completed' | 'rate-limited' | 'overloaded' | 'failed' | 'aborted';
  readonly httpStatus: number | null;
  readonly usageUnits: number | null;
  readonly backoffMs: number;
}

export interface MessagesApiProviderConfig {
  readonly model: string;
  readonly apiKey: string;
  readonly baseUrl?: string;
  /** Profile-set Opus effort level, sent as output_config.effort. */
  readonly effort: 'low' | 'medium' | 'high' | 'xhigh' | 'max';
  /** Profile-set output cap; permit allowances can only lower it. */
  readonly maxOutputTokens: number;
  readonly retry?: { readonly maxAttempts: number; readonly baseDelayMs: number; readonly maxDelayMs: number; readonly budgetMs: number };
  readonly sleep?: (ms: number, signal: AbortSignal) => Promise<void>;
  readonly now?: () => number;
  readonly onAttempt?: (record: MessagesApiAttemptRecord) => void;
}

export interface MessagesApiProviderHandle {
  readonly generate: PipelinePorts['generate'];
  readonly attempts: () => readonly MessagesApiAttemptRecord[];
}

const DEFAULT_RETRY = { maxAttempts: 4, baseDelayMs: 2_000, maxDelayMs: 60_000, budgetMs: 180_000 };
const abortableSleep = (ms: number, signal: AbortSignal): Promise<void> => new Promise((resolve, reject) => {
  if (signal.aborted) { reject(new MessagesApiProviderError('aborted', 0)); return; }
  const timer = setTimeout(() => { signal.removeEventListener('abort', onAbort); resolve(); }, ms);
  const onAbort = (): void => { clearTimeout(timer); reject(new MessagesApiProviderError('aborted', 0)); };
  signal.addEventListener('abort', onAbort, { once: true });
});

/** The request body this route sends, and nothing else: the stage system
 * prompt, the stage input as the single user message, and profile-set limits. */
export function messagesApiBody(config: Pick<MessagesApiProviderConfig, 'model' | 'effort'>, system: string, input: string, maxTokens: number): Record<string, unknown> {
  return { model: config.model, max_tokens: maxTokens, system, messages: [{ role: 'user', content: input }], output_config: { effort: config.effort }, stream: true };
}

/** Messages API route (`@anthropic-ai/sdk`): no subprocess, no tools, no
 * ambient context. The SDK's own retry is off; this adapter owns retry and its receipts. */
export function createMessagesApiGenerate(config: MessagesApiProviderConfig): MessagesApiProviderHandle {
  const retry = config.retry ?? DEFAULT_RETRY;
  if (config.model.length === 0 || config.apiKey.length === 0 || !Number.isSafeInteger(config.maxOutputTokens) || config.maxOutputTokens <= 0
    || ![retry.maxAttempts, retry.baseDelayMs, retry.maxDelayMs, retry.budgetMs].every(x => Number.isSafeInteger(x) && x >= 0) || retry.maxAttempts < 1) throw new MessagesApiProviderError('invalid-config', 0);
  const sleep = config.sleep ?? abortableSleep;
  const now = config.now ?? Date.now;
  const client = new Anthropic({ apiKey: config.apiKey, ...(config.baseUrl === undefined ? {} : { baseURL: config.baseUrl }), maxRetries: 0 });
  const attempts: MessagesApiAttemptRecord[] = [];
  const record = (entry: MessagesApiAttemptRecord): void => { attempts.push(entry); config.onAttempt?.(entry); };

  const generate: PipelinePorts['generate'] = async input => {
    const maxTokens = Math.max(1, Math.min(input.permit.maxOutputBytes, input.permit.maxUsageUnits, config.maxOutputTokens));
    const started = now();
    const id = input.permit.attemptId;
    for (let n = 1; ; n++) {
      if (input.signal.aborted) throw new MessagesApiProviderError('aborted', n - 1);
      try {
        const message = await client.messages.stream(messagesApiBody(config, input.system, input.input, maxTokens) as unknown as Anthropic.MessageStreamParams, { signal: input.signal }).finalMessage();
        const u = message.usage;
        const parts = [u.input_tokens, u.output_tokens, u.cache_creation_input_tokens ?? 0, u.cache_read_input_tokens ?? 0];
        const units = parts.every(p => Number.isSafeInteger(p) && p >= 0) ? parts.reduce((a, b) => a + b, 0) : null;
        const text = message.content.flatMap(block => (block.type === 'text' ? [block.text] : [])).join('');
        if (message.content.some(block => block.type !== 'text') || text.length === 0) { record({ attemptId: id, try: n, outcome: 'failed', httpStatus: null, usageUnits: units, backoffMs: 0 }); throw new MessagesApiProviderError('no-output', n); }
        record({ attemptId: id, try: n, outcome: 'completed', httpStatus: null, usageUnits: units, backoffMs: 0 });
        return { body: text, model: message.model, usageUnits: units } satisfies ProviderReply;
      } catch (error) {
        if (error instanceof MessagesApiProviderError) throw error;
        if (input.signal.aborted) { record({ attemptId: id, try: n, outcome: 'aborted', httpStatus: null, usageUnits: null, backoffMs: 0 }); throw new MessagesApiProviderError('aborted', n); }
        const status = error instanceof Anthropic.APIError && typeof error.status === 'number' ? error.status : null;
        if (status === 429 || status === 529) {
          const delay = Math.min(retry.maxDelayMs, retry.baseDelayMs * 2 ** (n - 1));
          const more = n < retry.maxAttempts && now() - started + delay <= retry.budgetMs;
          record({ attemptId: id, try: n, outcome: status === 429 ? 'rate-limited' : 'overloaded', httpStatus: status, usageUnits: 0, backoffMs: more ? delay : 0 });
          if (!more) throw new MessagesApiProviderError('rate-limited', n, status);
          await sleep(delay, input.signal);
          continue;
        }
        record({ attemptId: id, try: n, outcome: 'failed', httpStatus: status, usageUnits: null, backoffMs: 0 });
        throw new MessagesApiProviderError('provider-error', n, status);
      }
    }
  };
  return { generate, attempts: () => attempts };
}

const HEADERS: ReadonlySet<string> = new Set(['accept', 'accept-encoding', 'anthropic-version', 'connection', 'content-length', 'content-type', 'host', 'user-agent', 'x-api-key', 'x-stainless-arch', 'x-stainless-lang', 'x-stainless-os', 'x-stainless-package-version', 'x-stainless-retry-count', 'x-stainless-runtime', 'x-stainless-runtime-version', 'x-stainless-timeout', 'x-stainless-helper-method', 'accept-language', 'sec-fetch-mode']);

/** Accepts a captured request only if its body is exactly the generator's bytes
 * plus profile-set limits: key order aside, nothing may be added or changed. */
export function acceptMessagesApiRequest(captured: CapturedRequest, expected: { readonly model: string; readonly system: string; readonly input: string; readonly effort: string; readonly maxTokens: number }): RequestAcceptance {
  const violations: string[] = [];
  if (captured.method !== 'POST' || captured.url !== '/v1/messages') violations.push(`unexpected endpoint ${captured.method} ${captured.url}`);
  for (const name of Object.keys(captured.headers)) if (!HEADERS.has(name)) violations.push(`unlisted header ${name}`);
  let body: unknown;
  try { body = JSON.parse(captured.body); } catch { return { accepted: false, violations: [...violations, 'body is not JSON'] }; }
  const want = messagesApiBody({ model: expected.model, effort: expected.effort as MessagesApiProviderConfig['effort'] }, expected.system, expected.input, expected.maxTokens);
  const got = body as Record<string, unknown>;
  if (got === null || typeof got !== 'object' || Array.isArray(got)) return { accepted: false, violations: [...violations, 'body is not an object'] };
  for (const key of Object.keys(got)) if (!(key in want)) violations.push(`unlisted body field ${key}`);
  for (const key of Object.keys(want)) if (JSON.stringify(got[key]) !== JSON.stringify(want[key])) violations.push(`body field ${key} differs from the generator and profile`);
  return { accepted: violations.length === 0, violations };
}
