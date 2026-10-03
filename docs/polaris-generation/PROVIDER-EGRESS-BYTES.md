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
| `thinking` | profile-set, fixed off | absent (`CLAUDE_CODE_DISABLE_THINKING=1`); enabling it adds `thinking` and `context_management` and is not supported |

Absent by construction (present with SDK defaults): the `# Environment` message
(cwd, OS, date), the billing-header system block, `thinking`,
`context_management`, and the `safeguards` block (cwd, home paths, deny rules,
git state; only in `permissionMode: auto`).

Schema-tool mode (opt-in) adds exactly one tool,
`{"name":"StructuredOutput","description":"return the final response as structured JSON","input_schema":<stage schema>}`,
which contradicts "no tools" in the consent template and needs the record to say so.

## Headers (names enforced; values listed so a record can name them)

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
