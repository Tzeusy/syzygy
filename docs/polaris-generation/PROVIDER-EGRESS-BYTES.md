# Provider egress bytes: Agent SDK route

Status: measurement of what the adapter in `packages/polaris-generation-provider`
sends. It is not an owner act and consents to nothing; it is the list an egress
record would have to name if the owner chooses this route.

Pin: `@anthropic-ai/claude-agent-sdk` 0.3.288 (exact, lockfile), which bundles
Claude Code CLI 2.1.288. The adapter refuses construction when the installed SDK
version differs (`unpinned-version`) and fails a call whose CLI announces another
version. A bump must re-run `agent-sdk-provider.test.ts` and
`egress-isolation.test.ts` and update this file in the same commit.

[Observed] against a local capture endpoint with a dummy key; no provider was
contacted. Ids are normalized below (`<hex64>`, `<uuid>`).

## Request `POST /v1/messages?beta=true` (text mode)

| Field | Origin | Bytes |
|---|---|---|
| `model` | profile-set | configured model |
| `system[0]` | **SDK-fixed** | `You are a Claude agent, built on Anthropic's Claude Agent SDK.` (`cache_control: ephemeral`) |
| `system[1]` | generator | exactly the stage `system` prompt (`cache_control: ephemeral`) |
| `messages[0]` | generator | one user text block, exactly the stage `input` envelope (`cache_control: ephemeral`) |
| `messages[1]` | **SDK-fixed** | `{"role":"system","content":[],"output_config":{"effort":"<effort>"}}` |
| `tools` | profile-set | `[]` |
| `metadata.user_id` | **SDK-fixed** | `{"device_id":"<hex64>","account_uuid":"","session_id":"<uuid>"}`; both ids random per run directory |
| `max_tokens` | profile-set | min(profile `maxOutputTokens`, permit output allowance, permit usage allowance) |
| `output_config.effort` | profile-set | the run profile's effort (`medium` by default) |
| `stream` | **SDK-fixed** | `true` |
| `thinking`, `context_management` | profile-set: `off` or `adaptive` | `off`: both absent. `adaptive`: see "Thinking profile values" |

Absent by construction (present with SDK defaults): the `# Environment` message
(cwd, OS, date), the billing-header system block, `thinking`,
`context_management`, and the `safeguards` block (cwd, home paths, deny rules,
git state; only in `permissionMode: auto`).

Schema-tool mode (opt-in) adds exactly one tool,
`{"name":"StructuredOutput","description":"return the final response as structured JSON","input_schema":<stage schema>}`,
which contradicts "no tools" in the consent template and needs the record to say so.

## Thinking profile values

The profile chooses `off` (default) or `adaptive`. The CLI maps any other
request (`enabled` with a budget, `display: omitted`) to the same adaptive bytes,
so only these two values are offered. [Observed] CLI 2.1.288, Opus 5.5.

| Value | Body adds | `anthropic-beta` adds |
|---|---|---|
| `off` | nothing | nothing |
| `adaptive` | `"thinking":{"type":"adaptive","display":"updates"}` and `"context_management":{"edits":[{"type":"clear_thinking_20251015","keep":"all"}]}` | `,thinking-display-updates-2026-08-18` |

`anthropic-beta` with `off` is exactly
`claude-code-20250219,interleaved-thinking-2025-05-14,thinking-token-count-2026-05-13,context-management-2025-06-27,prompt-caching-scope-2026-01-05,mid-conversation-system-2026-04-07,per-turn-control-2026-07-01,effort-2025-11-24`.
Thinking tokens bill as output tokens and are inside `max_tokens`.

## Headers (names and values enforced)

`user-agent: claude-cli/2.1.288 (external, sdk-ts, agent-sdk/0.3.288)`,
`x-claude-code-session-id` (same `<uuid>`), `x-stainless-os`, `x-stainless-arch`,
`x-stainless-runtime`, `x-stainless-runtime-version`, `x-stainless-package-version`,
`x-stainless-lang`, `x-stainless-retry-count`, `x-stainless-timeout`, `x-app: cli`,
`anthropic-version`, `anthropic-beta` (CLI feature betas), `anthropic-dangerous-direct-browser-access`,
`x-api-key`, plus transport headers. The platform headers identify the machine's OS,
CPU architecture and Node runtime version.

## Connectivity probe

After some failures the CLI sends `HEAD /api/hello` (user-agent `Bun/1.4.3`, no body)
to the API host. It carries no generator bytes; the capture predicate lists it as
the only non-message request allowed.

## What is not shown

[Unknown] whether the real API accepts the empty `role: system` message (only the
capture endpoint has seen it). [Unknown] traffic on paths this run did not take
(error handling beyond 429/529, long runs, login flows). `egress-isolation.test.ts`
shows one successful call names no socket address but the endpoint.

## What is gated, and what is only version-scoped

**Gated at runtime.** The adapter never points its client at a provider. It
points at an in-process loopback egress gate (`egress-gate.ts`), which forwards a
request only when all hold: the current try armed an acceptance predicate and the
exact request satisfies it (body fields and header *values* against the literals
and shapes above, including `x-api-key` equal to the configured credential and
`x-claude-code-session-id` equal to `metadata.session_id`); the injected consent
`permitted()` returns exactly `true` now (asked again for every request, retries
included); and an explicit `upstream` is configured. Otherwise it answers 403 and
no byte leaves. `HEAD /api/hello` is answered by the gate and never forwarded. One
try is armed at a time. The upstream host is the only destination the gate
connects to.

**Version-scoped, not gated.** The literals (`anthropic-beta`, `user-agent`,
`x-stainless-*`, `x-app`, the identity system block, the empty system envelope)
were observed against SDK 0.3.288 and CLI 2.1.288 and are enforced as literals,
so a CLI upgrade makes requests fail closed until this file and the predicate are
re-derived. The gate sees only HTTP to its own port: anything the CLI process
does outside that port (other sockets, files) is bounded by the environment, the
run directory and the isolation test, not by the gate. Values that identify the
machine (OS, architecture, Node runtime version) are checked by shape only, and
they are sent.

## Machine fingerprint and the strip option

Both routes send `x-stainless-os`, `x-stainless-arch` and `x-stainless-runtime-version`
(for example the OS name, CPU architecture and Node version of this machine), and the
Agent SDK route's `user-agent` names the CLI and SDK versions. The provider does not
need the three platform headers to answer. The gate has a `stripFingerprint` option
(adapter config, default **false**) that deletes exactly those three after the
request passed the allowlist and before forwarding. Default off keeps the forwarded
bytes identical to the accepted bytes; whether the egress record should require
stripping is an owner choice, recorded here as open. With strip on, an upstream
capture no longer satisfies the Agent SDK predicate (it requires the headers); the
gate's own check is the one that applies.

## Rejected requests and billing

A 429 or 529 try counts as unbilled (usage 0) only when the gate read the
provider's documented error body (`type: error` with `rate_limit_error` or
`overloaded_error`) from the upstream response. The Agent SDK CLI's own synthetic
zero usage is not evidence. Without that evidence the try's usage is unknown
(null), and so is the call's total.


## Gate rules added after re-review of the first gate

- One forward per armed try: the try is claimed before consent is awaited, so a second request in the same try, sequential or simultaneous, is refused with `try already forwarded one request`. The connectivity probe does not spend the try.
- The upstream is pinned in code: exactly `https://api.anthropic.com` (no credentials, no port). Anything else makes `startEgressGate` throw, plain http to a remote host included. A loopback address (a local capture endpoint) is accepted only with the `LOOPBACK_FOR_TESTS` token, which is not exported from the package index, so production wiring cannot reach it: a local listener could otherwise forward anywhere.
- Any 3xx from the upstream is answered 502 and never followed; `Location` is not passed on.
- The gate's own `Host` header is not forwarded. The listener binds 127.0.0.1.
- `x-stainless-timeout` must equal `600` and `connection` must equal `keep-alive` (values, not just names).

### Gate hardening after the second review

- After `permitted()` answers, the gate forwards only if the same arming is still current and the caller is still connected (the close handler is attached before the await); otherwise the request is refused with `try ended while consent was being asked`.
- The gate refuses to start, and refuses to forward, while any of `NODE_TLS_REJECT_UNAUTHORIZED`, `NODE_EXTRA_CA_CERTS`, `NODE_USE_ENV_PROXY`, `NODE_USE_SYSTEM_CA`, `NODE_OPTIONS`, `SSL_CERT_FILE`, `SSL_CERT_DIR`, `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY` or their lower-case forms is set in the forwarding process. It refuses the same way while `process.execArgv` carries `--use-system-ca`, `--use-openssl-ca` or any `--tls-*` flag. `ANTHROPIC_*` is not a gate variable (the gate sends the request's own key header); the Messages route still refuses it when it builds its client.
- Upstream requests use a pinned `https.Agent` (`rejectUnauthorized: true`, TLS 1.2 minimum, no keep-alive). A self-signed upstream is not reached.
- If the upstream drops mid-body, the caller's response is destroyed (an error), not left hanging.
- `createAgentSdkGenerate` validates `upstream` at construction.
- No proxy variable reaches the CLI subprocess. The `diagnosticEnv` option, which passed `HTTP(S)_PROXY` through, is removed, and a config that still names it is refused. A recording proxy received the request body and API key before the gate saw it. The child environment carries `NO_PROXY=*` and `no_proxy=*`.
- `LOOPBACK_FOR_TESTS` may appear only in the gate module, tests and testkits; a test scans `packages/`, `apps/` and `scripts/` for it.
