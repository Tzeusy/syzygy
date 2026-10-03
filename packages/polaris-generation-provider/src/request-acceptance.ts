/** Egress acceptance for a captured provider request.
 *
 * The Agent SDK's CLI subprocess adds bytes of its own that no option removes.
 * This module closes them into an allowlist: a captured request is accepted
 * only when every byte is either what the generator built or one of the
 * enumerated SDK-fixed fields below. It never states that the allowlist is
 * what an owner consented to; that is an act.
 */

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
}

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

/** Checks one captured request against the generator's bytes plus the closed
 * set of SDK-fixed fields. Returns every violation, never just the first. */
export function acceptCapturedRequest(captured: CapturedRequest, expected: ExpectedRequest): RequestAcceptance {
  const violations: string[] = [];
  const fail = (message: string): void => { violations.push(message); };
  if (captured.method !== 'POST' || !/^\/v1\/messages(\?beta=true)?$/.test(captured.url)) fail(`unexpected endpoint ${captured.method} ${captured.url}`);
  for (const name of Object.keys(captured.headers)) if (!ALLOWED_HEADERS.has(name)) fail(`unlisted header ${name}`);
  let body: unknown;
  try { body = JSON.parse(captured.body); } catch { return { accepted: false, violations: [...violations, 'body is not JSON'] }; }
  if (!isRecord(body)) return { accepted: false, violations: [...violations, 'body is not an object'] };
  const allowedKeys = ['max_tokens', 'messages', 'metadata', 'model', 'output_config', 'stream', 'system', 'tools'];
  for (const key of Object.keys(body)) if (!allowedKeys.includes(key)) fail(`unlisted body field ${key}`);
  for (const key of allowedKeys) if (!(key in body)) fail(`missing body field ${key}`);
  if (body.model !== expected.model) fail('model differs from the configured model');
  if (body.max_tokens !== expected.maxTokens) fail('max_tokens differs from the configured cap');
  if (body.stream !== true) fail('stream is not true');
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
  return captured.method === 'HEAD' && captured.url === '/api/hello' && captured.body === ''
    && Object.keys(captured.headers).every(name => PROBE_HEADERS.has(name));
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
