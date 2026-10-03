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
