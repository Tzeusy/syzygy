import Anthropic from '@anthropic-ai/sdk';
import { VERSION as INSTALLED_MESSAGES_SDK_VERSION } from '@anthropic-ai/sdk/version';
import type { DispatchPermit, PipelinePorts, PromptStage, ProviderReply } from '@syzygy/polaris-generation-core';
import { ambientNetworkEnvironment, assertAllowedUpstream, parseRetryAfterMs, startEgressGate, type EgressGate, type EgressGateOptions, type GateDecision } from './egress-gate.js';
import { MAX_OUTPUT_TOKENS, countedUnits, outputTokenCap, tokenUnits } from './usage-units.js';
import type { CapturedRequest, RequestAcceptance } from './request-acceptance.js';

type GenerateInput = Parameters<PipelinePorts['generate']>[0];

/** Version the capture test ran against; a bump re-runs it and re-derives the header literals below. */
export const PINNED_MESSAGES_SDK_VERSION = '0.131.0';

export type MessagesApiFailure = 'unpinned-version' | 'ambient-environment' | 'incomplete' | 'invalid-config' | 'concurrent-call' | 'aborted' | 'deadline' | 'egress-refused' | 'rate-limited' | 'provider-error' | 'no-output' | 'budget-too-small';
export class MessagesApiProviderError extends Error {
  /** Tokens billed across the tries made so far; null when any try reported none. */
  spentUnits: number | null = 0;
  constructor(readonly code: MessagesApiFailure, readonly attempts: number, readonly status: number | null = null) { super(code); }
}

export interface MessagesApiAttemptRecord {
  readonly attemptId: string;
  readonly try: number;
  readonly outcome: 'completed' | 'rate-limited' | 'overloaded' | 'failed' | 'aborted' | 'refused';
  readonly httpStatus: number | null;
  readonly usageUnits: number | null;
  readonly backoffMs: number;
}

/** Profile-set thinking. `off` omits the field; `adaptive` sends `{"type":"adaptive"}`;
 * `{ budgetTokens }` sends `{"type":"enabled","budget_tokens":N}` (must be below max_tokens). */
export type MessagesThinking = 'off' | 'adaptive' | { readonly budgetTokens: number };

export interface MessagesApiProviderConfig {
  readonly model: string;
  readonly apiKey: string;
  /** The gate forwards here and nowhere else. Absent: every request is refused. */
  readonly upstream?: EgressGateOptions['upstream'];
  /** Consent switch, asked by the gate for every request (a discovery call names its discovery stage). Only `true` permits. */
  readonly permitted: (permit: DispatchPermit, stage: PromptStage) => Promise<boolean>;
  /** Gate option: drop the OS, architecture and runtime-version headers before forwarding (default false). */
  readonly stripFingerprint?: boolean;
  /** Test seam for the version check. */
  readonly pinnedVersion?: string;
  /** Profile-set Opus effort level, sent as output_config.effort. */
  readonly effort: 'low' | 'medium' | 'high' | 'xhigh' | 'max';
  readonly thinking?: MessagesThinking;
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
  readonly gateDecisions: () => readonly GateDecision[];
  readonly gateUrl: () => string | undefined;
  readonly close: () => Promise<void>;
}

const DEFAULT_RETRY = { maxAttempts: 4, baseDelayMs: 2_000, maxDelayMs: 60_000, budgetMs: 180_000 };
const abortableSleep = (ms: number, signal: AbortSignal): Promise<void> => new Promise((resolve, reject) => {
  if (signal.aborted) { reject(new MessagesApiProviderError('aborted', 0)); return; }
  const timer = setTimeout(() => { signal.removeEventListener('abort', onAbort); resolve(); }, ms);
  const onAbort = (): void => { clearTimeout(timer); reject(new MessagesApiProviderError('aborted', 0)); };
  signal.addEventListener('abort', onAbort, { once: true });
});

type BodyConfig = Pick<MessagesApiProviderConfig, 'model' | 'effort'> & { readonly thinking?: MessagesThinking };

/** The request body this route sends, and nothing else: the stage system
 * prompt, the stage input as the single user message, and profile-set limits. */
export function messagesApiBody(config: BodyConfig, system: string, input: string, maxTokens: number): Record<string, unknown> {
  const thinking = config.thinking ?? 'off';
  return {
    model: config.model, max_tokens: maxTokens, system, messages: [{ role: 'user', content: input }], output_config: { effort: config.effort },
    ...(thinking === 'off' ? {} : { thinking: thinking === 'adaptive' ? { type: 'adaptive' } : { type: 'enabled', budget_tokens: thinking.budgetTokens } }),
    stream: true,
  };
}

/** The client reads ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, ANTHROPIC_CUSTOM_HEADERS and
 * profile variables from the process environment. None may be set, nor the Node TLS and proxy variables
 * (syzygy-yqtg): ambient state must not
 * redirect, re-authenticate or add headers to this route. */
function refuseAmbientEnvironment(tries = 0): void {
  if (Object.keys(process.env).some(name => name.startsWith('ANTHROPIC_')) || ambientNetworkEnvironment().length > 0) throw new MessagesApiProviderError('ambient-environment', tries);
}

/** Messages API route (`@anthropic-ai/sdk`): no subprocess, no tools, no
 * ambient context. The client points at the loopback egress gate, never a provider. */
export function createMessagesApiGenerate(config: MessagesApiProviderConfig): MessagesApiProviderHandle {
  if (INSTALLED_MESSAGES_SDK_VERSION !== (config.pinnedVersion ?? PINNED_MESSAGES_SDK_VERSION)) throw new MessagesApiProviderError('unpinned-version', 0);
  refuseAmbientEnvironment();
  if (config.upstream !== undefined) { try { assertAllowedUpstream(config.upstream.url, config.upstream.loopbackForTests); } catch { throw new MessagesApiProviderError('invalid-config', 0); } }
  const retry = config.retry ?? DEFAULT_RETRY;
  const budgetTokens = typeof config.thinking === 'object' ? config.thinking.budgetTokens : undefined;
  if (config.model.length === 0 || config.apiKey.length === 0 || !Number.isSafeInteger(config.maxOutputTokens) || config.maxOutputTokens <= 0
    || (budgetTokens !== undefined && !(Number.isSafeInteger(budgetTokens) && budgetTokens >= 1024 && budgetTokens < config.maxOutputTokens))
    || ![retry.maxAttempts, retry.baseDelayMs, retry.maxDelayMs, retry.budgetMs].every(x => Number.isSafeInteger(x) && x >= 0) || retry.maxAttempts < 1) throw new MessagesApiProviderError('invalid-config', 0);
  const sleep = config.sleep ?? abortableSleep;
  const now = config.now ?? Date.now;
  const attempts: MessagesApiAttemptRecord[] = [];
  const record = (entry: MessagesApiAttemptRecord): void => { attempts.push(entry); config.onAttempt?.(entry); };
  const slot: { current: { permit: DispatchPermit; stage: PromptStage } | null } = { current: null };
  let gateRef: EgressGate | undefined;
  let started: Promise<{ gate: EgressGate; client: Anthropic }> | undefined;
  const start = (): NonNullable<typeof started> => started ??= (async () => {
    refuseAmbientEnvironment();
    const gate = await startEgressGate({
      ...(config.upstream === undefined ? {} : { upstream: config.upstream }),
      permitted: async () => (slot.current === null ? false : config.permitted(slot.current.permit, slot.current.stage)),
      ...(config.stripFingerprint === undefined ? {} : { stripFingerprint: config.stripFingerprint }),
    });
    gateRef = gate;
    return { gate, client: new Anthropic({ apiKey: config.apiKey, authToken: null, baseURL: gate.url, defaultHeaders: {}, maxRetries: 0 }) };
  })();

  const generate: PipelinePorts['generate'] = async input => {
    const { gate, client } = await start().catch(error => { started = undefined; throw error; });
    const maxTokens = outputTokenCap(input.permit, input.system, input.input, Math.min(config.maxOutputTokens, MAX_OUTPUT_TOKENS));
    if (maxTokens === null) throw new MessagesApiProviderError('budget-too-small', 0);   // nothing was armed or sent
    const expected = { model: config.model, system: input.system, input: input.input, effort: config.effort, maxTokens, apiKey: config.apiKey, ...(config.thinking === undefined ? {} : { thinking: config.thinking }) };
    const begun = now();
    const id = input.permit.attemptId;
    let total: number | null = 0;
    const fail = (code: MessagesApiFailure, n: number, status: number | null = null): MessagesApiProviderError => {
      const error = new MessagesApiProviderError(code, n, status);
      error.spentUnits = total;
      return error;
    };
    for (let n = 1; ; n++) {
      if (input.signal.aborted) throw fail('aborted', n - 1);
      try { refuseAmbientEnvironment(n - 1); } catch (error) { if (error instanceof MessagesApiProviderError) throw fail('ambient-environment', n - 1); throw error; }   // every try, not only the first
      const remaining = retry.budgetMs - (now() - begun);
      if (remaining <= 0) throw fail('deadline', n - 1);
      if (!gate.arm(captured => acceptMessagesApiRequest(captured, expected))) throw fail('concurrent-call', n - 1);
      slot.current = { permit: input.permit, stage: input.stage };
      const before = gate.decisions.length;
      const controller = new AbortController();
      const forward = (): void => controller.abort();
      let timedOut = false;
      const timer = setTimeout(() => { timedOut = true; controller.abort(); }, remaining);
      input.signal.addEventListener('abort', forward, { once: true });
      let units: number | null = null;
      try {
        const message = await client.messages.stream(messagesApiBody(config, input.system, input.input, maxTokens) as unknown as Anthropic.MessageStreamParams, { signal: controller.signal }).finalMessage();
        const u = message.usage;
        units = tokenUnits([u.input_tokens, u.output_tokens, u.cache_creation_input_tokens ?? 0, u.cache_read_input_tokens ?? 0]);
        total = total === null || units === null ? null : total + units;
        if (message.stop_reason !== 'end_turn') {
          record({ attemptId: id, try: n, outcome: 'failed', httpStatus: null, usageUnits: units, backoffMs: 0 });
          throw fail('incomplete', n);
        }
        const text = message.content.flatMap(block => (block.type === 'text' ? [block.text] : [])).join('');
        // Thinking blocks are the profile's own doing; any other block (a tool call) is not output.
        if (message.content.some(block => block.type !== 'text' && block.type !== 'thinking' && block.type !== 'redacted_thinking') || text.length === 0) {
          record({ attemptId: id, try: n, outcome: 'failed', httpStatus: null, usageUnits: units, backoffMs: 0 });
          throw fail('no-output', n);
        }
        record({ attemptId: id, try: n, outcome: 'completed', httpStatus: null, usageUnits: units, backoffMs: 0 });
        return { body: text, model: message.model, usageUnits: countedUnits(total, input.permit) } satisfies ProviderReply;
      } catch (error) {
        if (error instanceof MessagesApiProviderError) throw error;
        total = null;   // the try's billing is unknown unless a 429/529 below says otherwise
        if (input.signal.aborted) { record({ attemptId: id, try: n, outcome: 'aborted', httpStatus: null, usageUnits: null, backoffMs: 0 }); throw fail('aborted', n); }
        if (timedOut) { record({ attemptId: id, try: n, outcome: 'aborted', httpStatus: null, usageUnits: null, backoffMs: 0 }); throw fail('deadline', n); }
        const refused = gate.decisions.slice(before).some(d => d.decision === 'refused');
        if (refused) { record({ attemptId: id, try: n, outcome: 'refused', httpStatus: 403, usageUnits: null, backoffMs: 0 }); throw fail('egress-refused', n, 403); }
        const status = error instanceof Anthropic.APIError && typeof error.status === 'number' ? error.status : null;
        if (status === 429 || status === 529) {
          // Unbilled only on the provider's documented error body, read by the gate; a bare status is not evidence.
          const unbilledTry = gate.takeRejectedUnbilled();
          total = unbilledTry ? prior(attempts, id, n) : null;
          const header = error instanceof Anthropic.APIError ? error.headers?.get('retry-after') : undefined;
          const hinted = Math.max(parseRetryAfterMs(header, Date.now()) ?? 0, gate.takeRetryAfterMs() ?? 0);
          const delay = Math.max(Math.min(retry.maxDelayMs, retry.baseDelayMs * 2 ** (n - 1)), hinted);
          // A try whose billing is unknown has used the call's whole ceiling: no further try is made.
          const more = total !== null && n < retry.maxAttempts && now() - begun + delay <= retry.budgetMs;
          record({ attemptId: id, try: n, outcome: status === 429 ? 'rate-limited' : 'overloaded', httpStatus: status, usageUnits: unbilledTry ? 0 : null, backoffMs: more ? delay : 0 });
          if (!more) throw fail('rate-limited', n, status);
          await sleep(delay, input.signal);
          continue;
        }
        record({ attemptId: id, try: n, outcome: 'failed', httpStatus: status, usageUnits: null, backoffMs: 0 });
        throw fail('provider-error', n, status);
      } finally {
        clearTimeout(timer); input.signal.removeEventListener('abort', forward); gate.disarm(); slot.current = null;
      }
    }
  };
  return {
    generate, attempts: () => attempts, gateUrl: () => gateRef?.url,
    gateDecisions: () => (gateRef === undefined ? [] : [...gateRef.decisions]),
    close: async () => { if (gateRef !== undefined) await gateRef.close(); },
  };
}

/** Billing known so far for this call: the sum over earlier tries, null if any was unknown. */
function prior(attempts: readonly MessagesApiAttemptRecord[], attemptId: string, upTo: number): number | null {
  let sum = 0;
  for (const a of attempts) {
    if (a.attemptId !== attemptId || a.try >= upTo) continue;
    if (a.usageUnits === null) return null;
    sum += a.usageUnits;
  }
  return sum;
}

const SHAPES: Readonly<Record<string, RegExp>> = {
  'x-stainless-os': /^[A-Za-z]{1,16}$/, 'x-stainless-arch': /^[a-z0-9_]{1,16}$/, 'x-stainless-runtime-version': /^v\d{1,3}\.\d{1,3}\.\d{1,3}$/,
  'accept-encoding': /^[a-z, ]{1,40}$/, host: /^127\.0\.0\.1:\d{1,5}$/,
};
/** Header literals observed with @anthropic-ai/sdk 0.131.0 (version-scoped). */
const LITERALS: Readonly<Record<string, string>> = {
  accept: 'application/json', 'content-type': 'application/json', 'anthropic-version': '2023-06-01', 'user-agent': `Anthropic/JS ${PINNED_MESSAGES_SDK_VERSION}`,
  'x-stainless-lang': 'js', 'x-stainless-package-version': PINNED_MESSAGES_SDK_VERSION, 'x-stainless-retry-count': '0', 'x-stainless-runtime': 'node',
  'x-stainless-helper-method': 'stream', 'accept-language': '*', 'sec-fetch-mode': 'cors',
  'x-stainless-timeout': '600', connection: 'keep-alive',
};
const OPTIONAL_SHAPES: ReadonlySet<string> = new Set<string>();

/** Accepts a captured request only if its body is exactly the generator's bytes
 * plus profile-set limits and every header name and value is listed. */
export function acceptMessagesApiRequest(captured: CapturedRequest, expected: { readonly model: string; readonly system: string; readonly input: string; readonly effort: string; readonly maxTokens: number; readonly thinking?: MessagesThinking; readonly apiKey?: string }): RequestAcceptance {
  const violations: string[] = [];
  if (captured.method !== 'POST' || captured.url !== '/v1/messages') violations.push(`unexpected endpoint ${captured.method} ${captured.url}`);
  for (const [name, value] of Object.entries(captured.headers)) {
    if (name in LITERALS) { if (value !== LITERALS[name]) violations.push(`header ${name} is not the pinned literal`); }
    else if (name in SHAPES) { if (typeof value !== 'string' || !SHAPES[name]!.test(value)) violations.push(`header ${name} is not a listed shape`); }
    else if (name === 'content-length') { if (value !== String(Buffer.byteLength(captured.body))) violations.push('header content-length does not match the body'); }
    else if (name === 'x-api-key') { if (typeof value !== 'string' || value.length === 0 || (expected.apiKey !== undefined && value !== expected.apiKey)) violations.push('header x-api-key is not the configured credential'); }
    else if (!OPTIONAL_SHAPES.has(name)) violations.push(`unlisted header ${name}`);
  }
  for (const name of Object.keys(LITERALS)) if (!(name in captured.headers)) violations.push(`header ${name} missing`);
  let body: unknown;
  try { body = JSON.parse(captured.body); } catch { return { accepted: false, violations: [...violations, 'body is not JSON'] }; }
  const want = messagesApiBody({ model: expected.model, effort: expected.effort as MessagesApiProviderConfig['effort'], ...(expected.thinking === undefined ? {} : { thinking: expected.thinking }) }, expected.system, expected.input, expected.maxTokens);
  const got = body as Record<string, unknown>;
  if (got === null || typeof got !== 'object' || Array.isArray(got)) return { accepted: false, violations: [...violations, 'body is not an object'] };
  for (const key of Object.keys(got)) if (!(key in want)) violations.push(`unlisted body field ${key}`);
  for (const key of Object.keys(want)) if (JSON.stringify(got[key]) !== JSON.stringify(want[key])) violations.push(`body field ${key} differs from the generator and profile`);
  return { accepted: violations.length === 0, violations };
}
