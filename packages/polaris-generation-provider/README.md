# Polaris generation provider

The Claude Agent SDK adapter behind `PipelinePorts.generate`. It lives apart from
`polaris-generation-core` so the core carries no SDK dependency. It grants no
read, egress or write: a real call still needs the egress consent act.

- **`createAgentSdkGenerate(config)`** returns `{ generate, attempts, cwd }`.
  One single-turn CLI call per try; the stage `system` is the custom system
  prompt and the stage `input` is the only user message.
- **Closed environment.** `agentSdkEnvironment` names every variable; nothing is
  inherited from `process.env`, and no proxy variable is ever passed (`NO_PROXY=*` in both spellings). Every state path (home, config, tmp, XDG) is
  inside the run directory, and the working directory is an empty
  `<runDir>/cwd` that the adapter refuses to use if anything else wrote there.
- **Runtime egress gate.** The CLI's `ANTHROPIC_BASE_URL` is always an in-process
  loopback gate that runs the acceptance predicate (body fields and header
  values) on every request and forwards only if the injected consent
  `permitted()` is exactly `true` and an explicit `upstream` is configured.
  Otherwise it refuses and nothing leaves. `HEAD /api/hello` is answered locally.
  See `docs/polaris-generation/PROVIDER-EGRESS-BYTES.md` for what is gated and
  what is only version-scoped.
- **No tools, settings, memory, MCP or skills.** `tools: []`, every built-in
  also in `disallowedTools`, `settingSources: []`, `mcpServers: {}`, bare mode,
  no session persistence, `permissionMode: 'default'`.
- **Retry.** The CLI's own retry is off. This adapter retries only HTTP 429 and
  529, with capped exponential backoff or the upstream's `Retry-After` (whichever
  is longer), inside a run budget that also bounds each try's deadline, and reports every
  try (`attempts()` / `onAttempt`), including its status, token usage and
  backoff. Any other failure is thrown, carrying the tokens spent (`spentUnits`, null when unknown); the pipeline records it as
  effect-uncertain.
- **Usage.** Accounting policy `agent-sdk-tokens-v1`: input, cache-creation,
  cache-read and output tokens summed over all tries. A try that reports no
  usage makes the total `null`, which the pipeline stops on as usage-uncertain.
- **Output.** Default `text` mode sends no tool. `schema-tool` mode lets the SDK
  add its `StructuredOutput` tool carrying the stage schema; that is a tool in
  the request and needs the egress record to say so.

## What the request still carries

The CLI adds bytes no option removes. `acceptCapturedRequest` allowlists them
and rejects everything else: the identity system block
`You are a Claude agent, built on Anthropic's Claude Agent SDK.`, random
`device_id` and `session_id` in `metadata`, an empty `role: system` message,
`max_tokens` / `output_config.effort` / `stream`, `cache_control` markers, and
headers that name the platform (`user-agent`, `x-stainless-os/arch/runtime`).
After some failures it also sends a body-less `HEAD /api/hello` to the API host.

## Evidence that nothing else leaves

`egress-isolation.test.ts` runs the adapter in a network namespace that has only
loopback, under `strace`, and fails on any socket address other than the capture
endpoint. A positive control shows the rig would see a stray attempt. It covers
the paths one run takes; it does not prove other paths (long runs, login flows,
error handling beyond 429/529) never reach another host. Skipped, and reported
as skipped, where `strace` or unprivileged namespaces are unavailable.
