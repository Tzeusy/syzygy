# R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-1 — Messages API provider route registry entry, round 1
Reviewed commit: b101829d1b6f345a166e8eeed8efb4e800544421
Manifest SHA-256: 1e6180268b10ee552a1ea32f052a90d57d905752c880da2886c62bf5c413416f
Verdict: REVISE

Reviewer: fresh-context independent reviewer (Claude Opus 5.5), 2026-10-03.
Read-only detached worktree at the reviewed commit. Nothing tracked was
modified; no model provider was called; no external repository was read.

## What was read and run

- Package at the reviewed commit: every file of
  `.syzygy/governance/contracts/candidates/provider-route-messages-api-entry/`,
  `scripts/build_provider_route_messages_api_entry.py`, and the
  `MESSAGES_API_*` registration in `scripts/check_governance.py`
  (lines 1643-1652, 2399-2403, 3114-3116).
- Digests by `sha256sum`: the manifest file equals the head line above and
  equals `--manifest-digest`; the proposed JSON hashes to the manifest's one
  row.
- `--check`: "messages-api provider route entry: current", exit 0.
  `--selftest`: "selftest: 105 of 105 predicates held", exit 0.
  `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- Rule-6 check of the impact ledger's CG-7e claim, in a scratch copy made by
  `git archive` (not the worktree): a one-character change to the manifest
  row turns check_governance to "30 OK, 21 WARN, 1 FAIL" with CG-7e failing;
  replacing the whole row with 64 `a` characters also fails CG-7e, and the
  builder's `--check` reports the manifest stale. The ledger's claim holds.
- PR #264 source: `origin/agent/dossier-messages-api` at
  `dd526b0c3d4de2c1add4288469e320c8c52af99b` (the PR head per `gh pr view`).
  The three blobs and the PROVIDER-EGRESS-BYTES.md blob the entry names are
  the blobs at that commit (`git ls-tree`): egress-gate.ts, request-acceptance.ts,
  messages-api-provider.ts and the doc all match.
- SDK: `@anthropic-ai/sdk` 0.131.0 tarball from the registry URL in
  `dd526b0c:package-lock.json`; its sha512 equals the lockfile `integrity`
  value. Read `client.js`, `internal/detect-platform.js`,
  `internal/utils/log.js`, `resources/messages/messages.js`.
- Loopback capture (no provider): the SDK 0.131.0 client constructed as the
  adapter constructs it (`apiKey`, `baseURL` = a local server, `maxRetries: 0`)
  and `messages.stream(...).finalMessage()` against a 127.0.0.1 server that
  answers 403, under Node v24.6.0. Captured headers, in order: host,
  connection: keep-alive, accept: application/json, user-agent: Anthropic/JS
  0.131.0, x-stainless-retry-count: 0, x-stainless-timeout: 600,
  x-stainless-lang: js, x-stainless-package-version: 0.131.0,
  x-stainless-os: Linux, x-stainless-arch: x64, x-stainless-runtime: node,
  x-stainless-runtime-version: v24.6.0, anthropic-version: 2023-06-01,
  x-api-key, content-type: application/json, x-stainless-helper-method:
  stream, accept-language: *, sec-fetch-mode: cors, accept-encoding: gzip,
  deflate, content-length. Body keys: model, max_tokens, system, messages,
  output_config, stream. Re-run with `ANTHROPIC_AUTH_TOKEN` and
  `ANTHROPIC_CUSTOM_HEADERS='x-stainless-timeout: hello-exfil'` set, and with
  `ANTHROPIC_LOG=debug` (results in Findings 1 and 2).
- Sibling: PR #255 head `d08f4400cd20a9babc38e30b5fa6197b696e96e2`,
  `public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json`
  and its OWNER-DECISION-PACKET.md.
- Egress record: `origin/polaris/public-repo-admission` (PR #215 head
  `8bcec86000234e7c07f90050c476619ae0fe658b`),
  `instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`; its blob at that
  head, at `7704b4a5…` and at `b17207ce…` equals the blob the entry pins.
- RFC4-1, RFC4-2, RFC4-3, RFC4-7, RFC4-9 in
  `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`.

## Acceptance criteria

1. **Seven RFC4-2 declarations — yes.** Item 1: `observerId`
   "polaris-provider-route-anthropic-messages-api", `implementationId`
   "polaris-generation/provider-messages-api" (JSON lines 9, 12). Item 2:
   `implementationVersion: null`, `contractVersion` (lines 13, 16; see Note 3).
   Item 3: ten `inputClasses` (32-73), each mapped in `snapshotInputMapping`
   (243-256). Item 4: five `outputFactClasses` with identity schemes (74-95).
   Item 5: `determinismByOutputClass` (257-263), scalar explained (325).
   Item 6: `failureStates` (182-218) within RFC2-23 and RFC2-24. Item 7:
   `typedAuthority.questions`, `writeSurface: []` (101-105). No default left
   silent, except the network destination (Finding 3).
2. **Substitute and nothing more — yes, with Finding 5.** Same subject,
   provider and `authorityType` "model-provider" as PR #255's entry, same
   `contractVersion`, same consumed ports; distinct observer id; the sibling's
   `routeSubstitution` names this route as the replacing substitute; the
   packet asks for exactly one (OWNER-DECISION-PACKET.md:12-15, 34-39).
3. **`requestBytes` equals what the route sends — no.** Endpoint, body
   fields and the literal set match the adapter's `LITERALS` and `SHAPES`
   (messages-api-provider.ts:185-195) and the capture. `x-stainless-timeout`
   is wrongly described (Finding 1); three headers are attributed to the SDK
   that Node's fetch sets (Note 1). Nothing unsent is claimed as fact.
4. **Egress record fit honest — partly.** The three wordings are real and
   correctly quoted from the record (lines 19, 100-103, 123-124), but the
   entry's own conclusion counts two (Finding 4). Retention "satisfied" does
   not hold under an ambient `ANTHROPIC_LOG` (Finding 2). No file claims "no
   new egress version" outright.
5. **Credential honest — mostly.** API key only; the name is labelled
   `[Inferred: …proposal]` (line 119) and in `unknowns` (178). Nothing in
   PR #264's source logs or persists the key: `MessagesApiProviderError`
   carries code, attempts and status (provider.ts:12-16); attempt records carry
   no credential (18-25); gate decisions carry method, url, reasons, status
   (egress-gate.ts:20-27); the SDK's debug logger redacts `x-api-key`
   (internal/utils/log.js:103-110). But the SDK reads other environment
   variables that change the credential headers (Finding 2).
6. **Runtime gate matches source — yes, with Finding 3 and Note 4.** Arm one
   try (egress-gate.ts:99), predicate then `permitted() === true` then upstream
   (66-77), 403 body otherwise (53-57), host and connection deleted (79-80),
   probe answered locally (67-70). Commit and blobs verified.
7. **Pinned profile fields right and labelled — yes, with Note 2.** Model,
   effort `high`, tools absent, thinking off or adaptive, and 64000 labelled
   "[Inferred proposal, an owner choice]" (JSON 286-290). The max_tokens
   formula matches provider.ts:104.
8. **Write surface honest — yes for writes; network destination not exact
   (Finding 3).** `writeSurface: []`, `runDirectoryWrites` and `networkAccess`
   are separate fields (105-110).
9. **Null version, unknowns, failure mappings honest — yes.** Vocabularies are
   within RFC2-23's six states and RFC2-24's twelve reasons; execution facts
   are not dressed as degradation states. The SDK-file-write Unknown could be
   narrowed (Note 6).
10. **Impact ledger honest — yes.** At `b97b77ed` (the reviewed commit's
    parent): 1,990 tracked files; Sweep 1 gives 8 and 22 files, 23 at the
    reviewed commit; Sweep 2 gives 0 lines, 0 lines, 0 files. No reader under
    `apps packages scripts` enumerates the directory: every hit that does not
    name the Butlers file is prose, a constant or a scope anchor
    (e.g. `apps/three-surface-poc/src/governance-inputs.ts:80,116`).
11. **No authority claimed; no 64-hex in Markdown — yes.** Sweep over the
    package for accepted/adopted/approved/signed off: three hits, none
    labelling this package (JSON 17 "the adopted Butlers observer entry", 143
    and 157 "the adapter is accepted only when"). Python `re` over the four
    `*.md`: 0, 0, 0, 0 64-hex tokens. `--check` and `--selftest` pass; the
    uncovered claims are named in Note 5.

## Findings

**Finding 1 — `x-stainless-timeout` is always sent, and the entry admits any value for it** (revise)
`proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json:311`
lists "x-stainless-timeout (optional; the adapter's predicate checks the name
only, not the value)". SDK 0.131.0 always sends it: `buildHeaders` sets
`'X-Stainless-Timeout': String(Math.trunc(timeout / 1000))`
(client.js:837), and `messages.create` passes `timeout: timeout ?? 600000`
(resources/messages/messages.js:38), so this route sends
`x-stainless-timeout: 600` on every request; the capture shows it. It is not
optional, and its value is listed nowhere, which contradicts the same entry's
`unlistedBytes` ("any byte, header or field not listed above fails the
acceptance check", line 323) and `acceptanceCheck` ("every other byte equal to
requestBytes … Any byte, header or field in neither fails", line 143). The
adapter's predicate does admit any value
(`OPTIONAL_SHAPES`, messages-api-provider.ts:195, 207). With
`ANTHROPIC_CUSTOM_HEADERS='x-stainless-timeout: hello-exfil'` the SDK sent
`x-stainless-timeout: hello-exfil`, which that predicate accepts and the gate
would forward. The Agent SDK route's predicate already pins it as a literal
(`literal('x-stainless-timeout', '600')`, request-acceptance.ts:81).
Clause: RFC4-2 item 7 (exact authority boundary), as the entry applies it to
the egress record's condition that a request carrying "any other byte, header
or field … is refused at the single egress check" (EGRESS-CONSENT-ANTHROPIC.md
lines 100-103); criterion 3. Repair: list `x-stainless-timeout: 600` as a
literal and say the implementation must enforce it.

**Finding 2 — The SDK reads environment variables the entry does not declare. One can put the request body in logs** (revise)
The entry says the credential is read from "one environment variable … the
caller … reads exactly this variable and no other" (JSON:119), that the
request carries no ambient context (140), and that retention is "satisfied"
(152). SDK 0.131.0 also reads, during construction or every request, with the
adapter's constructor arguments (`apiKey`, `baseURL`, `maxRetries` only,
provider.ts:99):
- `ANTHROPIC_AUTH_TOKEN` (client.js:81, because `authToken` is not passed):
  `authHeaders` then sends `Authorization: Bearer <token>` beside `X-Api-Key`
  (client.js:364, 374-376). Observed in the capture. The gate refuses the
  unlisted header, so this fails closed. Even so, a second credential reaches
  the loopback gate, and the route fails as `egress-refused` for a reason the
  entry never names.
- `ANTHROPIC_CUSTOM_HEADERS` (client.js:117-127) adds arbitrary headers. Any
  name the predicate checks by name only gets through (Finding 1).
- `ANTHROPIC_LOG` (client.js:110): at `debug` the SDK logs "sending
  request" with `options`, and `formatRequestDetails` deletes only
  `options.headers` (log.js:98-101). The request body therefore goes to the
  console, including `system` and the user message with source spans.
  Observed in the capture. The key itself is redacted. That breaks the egress
  record's retention line, "nothing is retained in git, logs or machine
  responses" (EGRESS-CONSENT-ANTHROPIC.md:31). The entry never mentions this
  path and calls retention satisfied.
Clause: RFC4-2 item 3 (declared inputs) and item 7. Also the egress record's
retention and "adds no context of its own" conditions, as the entry's
`egressRecordFit` reads them; criteria 4 and 5. Repair: declare the SDK's
environment inputs. Either state as route conditions that the client is built
with `authToken: null`, `logLevel: 'off'` (or an injected logger) and no
custom headers, or list them as `[Unknown]` with a failure mapping. A
later-version offering re-checks the result against the implementation.

**Finding 3 — The network destination is not exact, and the gate does not bind the upstream to it** (revise)
`networkAccess` says "the Anthropic API host, POST /v1/messages only"
(JSON:109) but gives no scheme or host. Gate rule (3) only requires that "an
explicit upstream is configured" (129, 131). In source the upstream is any URL
(`options.upstream.url`), and plain `http:` is accepted
(egress-gate.ts:77-82, 81). A misconfigured upstream would therefore receive
the body and the `x-api-key` header, in clear text if it is `http:`, while
every rule the entry states still holds. The egress record says "The route
sends nothing to any destination other than the provider"
(EGRESS-CONSENT-ANTHROPIC.md:125). Clause: RFC4-2 item 7 ("the exact write
surface" and, per the brief, network destinations under the right field);
criteria 6 and 8. Repair: name the destination literally (scheme, host and
path), and add a gate rule that the configured upstream equals it, with
anything else refused.

**Finding 4 — The fit conclusion counts two open wordings; the entry lists three** (revise)
`egressRecordFit.needsReading` has three items (JSON:154-158): the route name,
"fixed by the runtime", and "nothing else". `conclusion` says "two wordings
(the route name, 'nothing else') need the owner's reading" (159).
SEMANTIC-DELTA.md:57-64 and OWNER-DECISION-PACKET.md:43-47 say three. The
bytes the act would bind contradict themselves and drop the "fixed by the
runtime" reading from the summary sentence. Clause: criterion 4 ("The packet
and delta say it depends on the owner's reading of three wordings; is that
accurate?"). The delta and packet are accurate and the entry is not. Repair:
make the conclusion name all three.

**Finding 5 — The substitution gives a new role identity, where RFC4-9's substitution keeps the role identity** (revise)
RFC4-2 item 1 asks for "stable opaque identifiers for the observer role and
for the implementation realizing it (substrates are substitutable)". RFC4-9
says: "Replacing an implementation … is a registry event: the role identity
persists, a new implementation identity is registered". This entry's
`routeSubstitution.rule` (JSON:228) says "adopting it replaces that entry by
a successor version or entry under a new act". It carries a different role
identity (`observerId`, line 9) from the entry it would replace, and the
builder makes that compulsory (`observerId equals the sibling's` predicate,
build script:229-230). Two role identities for one authority leave RFC4-1's
"exactly one registered adapter" to the prose flag `onlyOneAdoptable`, which
nothing structural enforces. If PR #255's entry is adopted first, adopting
this one would be a replacement that does not follow RFC4-9's form. The
package never cites RFC4-9. Clause: RFC4-2 item 1, RFC4-9, RFC4-1; criterion
2. Repair: either share the role identity and differ only in
`implementationId`, or cite RFC4-9 and state why a separate role identity is
correct for this case. If PR #255 has been adopted by then, also state what
retires it.

**Note 1 — Three listed headers come from Node's fetch, not the SDK** (note)
`accept-language: *`, `sec-fetch-mode: cors` and `accept-encoding` appear in
no SDK 0.131.0 `.js` file (grep: 0 files). Node's built-in fetch adds them.
The entry files them under `sdkFixed` ("the headers below", JSON:280), and
`runtimePin.note` says the literals depend on the SDK version (241). They also
depend on the Node version, which nothing pins (`x-stainless-runtime-version`
is only a shape). A change in Node fails closed, so no byte escapes. But the
attribution is wrong, and it bears on O2's "fixed by the runtime" reading:
these are the bytes on this route that a runtime actually fixes.

**Note 2 — The thinking and model pins are the entry's own; the source predicate does not enforce them** (note)
JSON:289 says an enabled `budget_tokens` form "is not a permitted
configuration … and the acceptance check refuses it". At `dd526b0c` the
adapter accepts `{ budgetTokens }` (provider.ts:29, 73, 84), and its predicate
compares the request against whatever is configured (212). The entry says so
("even though the adapter source accepts it") and presents its rules as what
the implementation will enforce (126). That is honest for a null-version
entry. The later version's offering must show the refusal in code, and must
show model `claude-opus-5-5` and effort `high` checked against literals
rather than against configuration.

**Note 3 — `contractVersion` is the RFC-0004 digest from before the restyle** (note)
The value (JSON:16) equals the Butlers entry's value. Re-derived by
`sha256sum`, it matches `general-contract.md` at `ecf16fb9`, not the current
bytes installed by the adopted readability restyle `a9a08305` (2026-09-28).
The entry labels its source and says "re-derive by script before the
offering" (17). The drift is disclosed and inherited, and the re-derivation
the entry asks for will produce a different value today.

**Note 4 — Gate decision records are not strictly free of values** (note)
JSON:121 and 199 say gate decision records "name fields, never values".
`acceptMessagesApiRequest` emits `unexpected endpoint ${method} ${url}` and
`unlisted header ${name}` (provider.ts:201, 207), and `GateDecision` carries
`url` (egress-gate.ts:22). The key never appears, so the credential claim
holds. Only the "never values" wording overstates.

**Note 5 — Claims the selftest does not cover** (note)
The 105 mutants never touch:
- the header literal values beyond six substrings (`HEADERS_PRESENT`, build
  script:73-74). `anthropic-version`, `accept-language`, `sec-fetch-mode`,
  `x-stainless-helper-method`, `x-stainless-retry-count` and the
  `x-stainless-timeout` description are unchecked.
- the agreement between `needsReading` and `conclusion` (Finding 4).
- PR #264's commit and blobs (only the egress blob is checked, line 61).
- the content of `networkAccess`, which is checked only for length 1.
- the sibling cross-check, which is vacuous at this commit (the sibling file
  is not in the tree) and compares only subject, `authorityType` and
  `observerId`, not `contractVersion`.

**Note 6 — The SDK file-write Unknown can be narrowed** (note)
JSON:106, 177. In SDK 0.131.0 file writes sit in the credential cache
(`lib/credentials/types.js:186-194`), `tools/agent-toolset/skills.js` and
`tools/memory/node.js`. The credential chain is skipped when `apiKey` is set
(client.js:148), and this route uses no tool helper. The Unknown is
honest. A source citation could replace it once the gate-run isolation test
covers file writes.

**Note 7 — The act form names no phrase, while the checker registers one** (note)
OWNER-DECISION-PACKET.md:23-28 proposes an option selection "at the manifest
row" and names no phrase. `check_governance.py:1649-1652` registers "ADOPT
POLARIS MESSAGES API PROVIDER EXECUTION ROUTE REGISTRY ENTRY". The recorder
is out of scope. The act and recorder must state which form binds.

**Note 8 — Owner questions O1–O4 are open choices, not defects** (note)
O1 (which route), O2 (the reading of the three egress record wordings), O3
(the environment variable name) and O4 (the profile pins and the 64000
ceiling) are each presented as open. Each is labelled `[Inferred]` or as a
recommendation, and no signed bytes assume an answer. Each is a note only.
Findings 1-4 are factual corrections within the entry's bytes and do not
decide any of them. Finding 4 changes how O2 is summarised, not its answer.

## Verdict

REVISE. Five findings are revise-severity: the always-sent and unconstrained
`x-stainless-timeout`, the undeclared SDK environment inputs (one of which
logs request bodies), the unpinned upstream destination, the two-versus-three
contradiction inside the entry, and the role-identity form of the
substitution. Each changes bytes the act would bind. Notes 1-8 need no change
before re-review, but Notes 1 and 5 could be folded into the same revision.
Any edit retires this review (rule 10).
