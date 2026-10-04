/** Egress acceptance for a captured provider request.
 *
 * The Agent SDK's CLI subprocess adds bytes of its own that no option removes.
 * This module closes them into an allowlist: a captured request is accepted
 * only when every byte is either what the generator built or one of the
 * enumerated SDK-fixed fields below. It never states that the allowlist is
 * what an owner consented to; that is an act.
 */

/** Versions the literals below were observed against. A bump re-runs the capture
 * tests and re-derives every version-scoped literal in this file. */
export const PINNED_AGENT_SDK_VERSION = '0.3.288';
export const PINNED_CLAUDE_CODE_VERSION = '2.1.288';

/** Hard-coded by the CLI as the first system block; no option removes it. */
export const SDK_FIXED_IDENTITY = "You are a Claude agent, built on Anthropic's Claude Agent SDK.";
/** Hard-coded by the CLI (bare mode) as the description of the tool that outputFormat adds. */
export const SDK_FIXED_STRUCTURED_OUTPUT_DESCRIPTION = 'return the final response as structured JSON';

export interface CapturedRequest {
  readonly method: string;
  readonly url: string;
  readonly headers: Readonly<Record<string, string | string[] | undefined>>;
  readonly body: string;
}

export interface ExpectedRequest {
  readonly model: string;
  /** Exact generator system prompt. */
  readonly system: string;
  /** Exact generator input (the single user message). */
  readonly input: string;
  readonly effort: string;
  readonly maxTokens: number;
  /** Present only in schema-tool mode: the stage's response schema. */
  readonly responseSchema?: unknown;
  /** Profile-set. 'adaptive' adds the `thinking` and `context_management` fields and one anthropic-beta entry. */
  readonly thinking?: 'off' | 'adaptive';
  /** When given, x-api-key must equal it. */
  readonly apiKey?: string;
}

/** anthropic-beta as sent by CLI 2.1.288: version-scoped. */
export const AGENT_SDK_BETA_OFF = 'claude-code-20250219,interleaved-thinking-2025-05-14,thinking-token-count-2026-05-13,context-management-2025-06-27,prompt-caching-scope-2026-01-05,mid-conversation-system-2026-04-07,per-turn-control-2026-07-01,effort-2025-11-24';
export const AGENT_SDK_BETA_ADAPTIVE = `${AGENT_SDK_BETA_OFF},thinking-display-updates-2026-08-18`;
export const AGENT_SDK_ADAPTIVE_THINKING = { type: 'adaptive', display: 'updates' } as const;
export const AGENT_SDK_ADAPTIVE_CONTEXT_MANAGEMENT = { edits: [{ type: 'clear_thinking_20251015', keep: 'all' }] } as const;

export interface RequestAcceptance {
  readonly accepted: boolean;
  readonly violations: readonly string[];
}

const same = (a: unknown, b: unknown): boolean => JSON.stringify(a) === JSON.stringify(b);
const isRecord = (v: unknown): v is Record<string, unknown> => v !== null && typeof v === 'object' && !Array.isArray(v);
const EPHEMERAL = { type: 'ephemeral' };

/** Header names the CLI sends. Values that identify the machine or build
 * (user-agent, x-stainless-os/arch/runtime-version) are accepted by name only
 * and listed so the owner's egress record can name them. */
const ALLOWED_HEADERS: ReadonlySet<string> = new Set([
  'accept', 'accept-encoding', 'anthropic-beta', 'anthropic-dangerous-direct-browser-access', 'anthropic-version', 'connection',
  'content-length', 'content-type', 'host', 'user-agent', 'x-api-key', 'x-app', 'x-claude-code-session-id',
  'x-stainless-arch', 'x-stainless-lang', 'x-stainless-os', 'x-stainless-package-version', 'x-stainless-retry-count',
  'x-stainless-runtime', 'x-stainless-runtime-version', 'x-stainless-timeout',
]);

const SESSION_ID = /^[0-9a-f-]{36}$/;
/** Value-level header checks: literals for everything the CLI fixes, patterns
 * for what identifies the machine (listed in PROVIDER-EGRESS-BYTES.md). */
function headerValueProblems(captured: CapturedRequest, expected: ExpectedRequest): string[] {
  const problems: string[] = [];
  const h = captured.headers;
  const one = (name: string): string | undefined => { const v = h[name]; return typeof v === 'string' ? v : undefined; };
  const literal = (name: string, want: string): void => { if (one(name) !== want) problems.push(`header ${name} is not the pinned literal`); };
  const pattern = (name: string, re: RegExp): void => { const v = one(name); if (v === undefined || !re.test(v)) problems.push(`header ${name} is not a listed shape`); };
  literal('accept', 'application/json'); literal('content-type', 'application/json'); literal('anthropic-version', '2023-06-01');
  literal('anthropic-dangerous-direct-browser-access', 'true'); literal('x-app', 'cli');
  literal('user-agent', `claude-cli/${PINNED_CLAUDE_CODE_VERSION} (external, sdk-ts, agent-sdk/${PINNED_AGENT_SDK_VERSION})`);
  literal('anthropic-beta', expected.thinking === 'adaptive' ? AGENT_SDK_BETA_ADAPTIVE : AGENT_SDK_BETA_OFF);
  literal('x-stainless-lang', 'js'); literal('x-stainless-retry-count', '0'); literal('x-stainless-timeout', '600'); literal('connection', 'keep-alive');
  literal('x-stainless-package-version', '0.128.0'); literal('x-stainless-runtime', 'node');
  pattern('x-stainless-os', /^[A-Za-z]{1,16}$/); pattern('x-stainless-arch', /^[a-z0-9_]{1,16}$/); pattern('x-stainless-runtime-version', /^v\d{1,3}\.\d{1,3}\.\d{1,3}$/);
  pattern('accept-encoding', /^[a-z, ]{1,40}$/); pattern('host', /^127\.0\.0\.1:\d{1,5}$/);
  if (one('content-length') !== String(Buffer.byteLength(captured.body))) problems.push('header content-length does not match the body');
  const key = one('x-api-key');
  if (key === undefined || (expected.apiKey !== undefined && key !== expected.apiKey)) problems.push('header x-api-key is not the configured credential');
  let sessionId: string | undefined;
  try { const user = JSON.parse((JSON.parse(captured.body) as { metadata: { user_id: string } }).metadata.user_id) as { session_id?: string }; sessionId = user.session_id; } catch { /* reported by the body check */ }
  const header = one('x-claude-code-session-id');
  if (header === undefined || !SESSION_ID.test(header) || (sessionId !== undefined && header !== sessionId)) problems.push('header x-claude-code-session-id does not match metadata.session_id');
  return problems;
}

/** Checks one captured request against the generator's bytes plus the closed
 * set of SDK-fixed fields. Returns every violation, never just the first. */
export function acceptCapturedRequest(captured: CapturedRequest, expected: ExpectedRequest): RequestAcceptance {
  const violations: string[] = [];
  const fail = (message: string): void => { violations.push(message); };
  if (captured.method !== 'POST' || !/^\/v1\/messages(\?beta=true)?$/.test(captured.url)) fail(`unexpected endpoint ${captured.method} ${captured.url}`);
  for (const name of Object.keys(captured.headers)) if (!ALLOWED_HEADERS.has(name)) fail(`unlisted header ${name}`);
  for (const problem of headerValueProblems(captured, expected)) fail(problem);
  let body: unknown;
  try { body = JSON.parse(captured.body); } catch { return { accepted: false, violations: [...violations, 'body is not JSON'] }; }
  if (!isRecord(body)) return { accepted: false, violations: [...violations, 'body is not an object'] };
  const adaptive = expected.thinking === 'adaptive';
  const allowedKeys = ['max_tokens', 'messages', 'metadata', 'model', 'output_config', 'stream', 'system', 'tools', ...(adaptive ? ['thinking', 'context_management'] : [])];
  for (const key of Object.keys(body)) if (!allowedKeys.includes(key)) fail(`unlisted body field ${key}`);
  for (const key of allowedKeys) if (!(key in body)) fail(`missing body field ${key}`);
  if (body.model !== expected.model) fail('model differs from the configured model');
  if (body.max_tokens !== expected.maxTokens) fail('max_tokens differs from the configured cap');
  if (body.stream !== true) fail('stream is not true');
  if (adaptive && !same(body.thinking, AGENT_SDK_ADAPTIVE_THINKING)) fail('thinking is not the adaptive profile bytes');
  if (adaptive && !same(body.context_management, AGENT_SDK_ADAPTIVE_CONTEXT_MANAGEMENT)) fail('context_management is not the adaptive profile bytes');
  if (!same(body.output_config, { effort: expected.effort })) fail('output_config is not exactly the pinned effort');

  // system: SDK identity, then exactly the generator's system prompt.
  const system = body.system;
  if (!Array.isArray(system) || system.length !== 2
    || !same(system[0], { type: 'text', text: SDK_FIXED_IDENTITY, cache_control: EPHEMERAL })
    || !same(system[1], { type: 'text', text: expected.system, cache_control: EPHEMERAL })) fail('system is not the SDK identity plus the generator system prompt');

  // messages: the generator input, then the CLI's empty system envelope.
  const messages = body.messages;
  if (!Array.isArray(messages) || messages.length !== 2
    || !same(messages[0], { role: 'user', content: [{ type: 'text', text: expected.input, cache_control: EPHEMERAL }] })
    || !same(messages[1], { role: 'system', content: [], output_config: { effort: expected.effort } })) fail('messages are not the generator input plus the SDK empty system envelope');

  // tools: none, or exactly the schema tool in schema-tool mode.
  if (expected.responseSchema === undefined) {
    if (!same(body.tools, [])) fail('tools is not empty');
  } else if (!same(body.tools, [{ name: 'StructuredOutput', description: SDK_FIXED_STRUCTURED_OUTPUT_DESCRIPTION, input_schema: expected.responseSchema }])) {
    fail('tools is not exactly the StructuredOutput schema tool');
  }

  // metadata: SDK ids only, random per run directory.
  const metadata = body.metadata;
  let idsOk = false;
  if (isRecord(metadata) && Object.keys(metadata).join() === 'user_id' && typeof metadata.user_id === 'string') {
    try {
      const ids = JSON.parse(metadata.user_id) as unknown;
      idsOk = isRecord(ids) && Object.keys(ids).join() === 'device_id,account_uuid,session_id'
        && typeof ids.device_id === 'string' && /^[0-9a-f]{64}$/.test(ids.device_id)
        && ids.account_uuid === ''
        && typeof ids.session_id === 'string' && /^[0-9a-f-]{36}$/.test(ids.session_id);
    } catch { idsOk = false; }
  }
  if (!idsOk) fail('metadata is not the SDK device and session identifiers');
  return { accepted: violations.length === 0, violations };
}

const PROBE_HEADERS: ReadonlySet<string> = new Set(['accept', 'accept-encoding', 'connection', 'host', 'user-agent']);

/** The CLI's body-less connectivity check (`HEAD /api/hello`, user-agent Bun/…)
 * seen on the API host after some failures. It carries no generator bytes. */
export function isConnectivityProbe(captured: CapturedRequest): boolean {
  const h = captured.headers;
  return captured.method === 'HEAD' && captured.url === '/api/hello' && captured.body === ''
    && Object.keys(h).every(name => PROBE_HEADERS.has(name))
    && h['user-agent'] === 'Bun/1.4.3' && h.accept === '*/*';
}

/** Accepts a whole capture: each request is a listed probe or an accepted
 * message request, and at least one message request exists. */
export function acceptCapturedTraffic(requests: readonly CapturedRequest[], expected: ExpectedRequest): RequestAcceptance {
  const violations: string[] = [];
  let messages = 0;
  requests.forEach((captured, index) => {
    if (isConnectivityProbe(captured)) return;
    messages++;
    for (const violation of acceptCapturedRequest(captured, expected).violations) violations.push(`request ${index}: ${violation}`);
  });
  if (messages === 0) violations.push('no message request captured');
  return { accepted: violations.length === 0, violations };
}
