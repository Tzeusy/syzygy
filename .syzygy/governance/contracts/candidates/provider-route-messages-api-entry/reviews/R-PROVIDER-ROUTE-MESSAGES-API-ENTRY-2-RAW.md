# R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-2 — independent review of the Messages API provider route entry, round 2
Reviewed commit: eafb02eea277ddf8517b436052218c1122ad2d73
Manifest SHA-256: 5da92fc4f5de0b9da0c5fd8b525465191da2d4b7b9c309086fa71eeeba085d01
Verdict: REVISE

Reviewer: fresh-context independent reviewer (Claude Opus 5.5), 2026-10-03.
I worked in a read-only detached worktree at the reviewed commit. Nothing
tracked was modified, no model provider was called, and no external
repository body was read. Below, `ENTRY` means
`proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-MESSAGES-API-CANDIDATE.json` in the
package directory.

## What was read and run

- **Package and registration.** Every file of the package at the reviewed
  commit, including `reviews/R-PROVIDER-ROUTE-MESSAGES-API-ENTRY-1-RAW.md` and
  `reviews/ROUND-1-DISPOSITIONS.md`. Also
  `scripts/build_provider_route_messages_api_entry.py` and the `MESSAGES_API_*`
  registration in `scripts/check_governance.py` (lines 1647-1651, 2399-2400,
  3108-3119).
- **Digests (`sha256sum`).**
  - The manifest file is `5da92fc4…`, equal to `--manifest-digest` and to the
    head line above.
  - The proposed JSON hashes to the manifest's one row.
  - The round-1 raw's head digest equals the manifest file at `b101829d`
    (`1e618026…`).
  - The committed round-1 raw is byte-identical to the reviewer's scratch
    original (same sha256).
- **Builder and governance check.**
  - `--check`: "messages-api provider route entry: current", exit 0.
  - `--selftest`: "selftest: 190 of 190 predicates held", exit 0.
  - `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- **PR #264 source.** `gh pr view 264` gives head
  `e76b692926d89342e7943ce0a2d7ef669a859b47`, the commit the entry pins.
  - `git rev-parse <commit>:<path>` for the three provenance files gives
    `fa8cdceb…`, `bb7f222f…` and `99d79e9d…`, equal to ENTRY lines 323, 327
    and 331.
  - I read `messages-api-provider.ts` and `egress-gate.ts` whole at that
    commit, and the adapter at `dd526b0c` (the round-1 commit) for the
    ambient guard.
- **SDK.** `@anthropic-ai/sdk-0.131.0.tgz` from the registry URL in
  `e76b6929:package-lock.json`. Its sha512 equals the lockfile `integrity`.
  - Read `client.js` (lines 70-170, 837, 912), `core/credentials.js`
    (250-305) and `resources/messages/messages.js` (29-38).
  - Enumerated every literal `readEnv('…')` call over all 261 `.js` files:
    24 distinct names, 0 non-literal calls.
- **Loopback capture (no provider).** Node v24.6.0. The SDK client was
  constructed exactly as the adapter constructs it at `e76b6929:115`:
  `apiKey`, `authToken: null`, `baseURL` set to a 127.0.0.1 server answering
  403, `defaultHeaders: {}`, `maxRetries: 0`. The request was
  `messages.stream(body, {signal}).finalMessage()`.
  - The clean run captured 20 headers.
  - Compared by script with the entry's `closedSet`: 0 captured outside it, 0
    listed but not captured, 0 literal mismatches, 0 shape mismatches. The
    host and content-length rules hold.
  - Body keys: max_tokens, messages, model, output_config, stream, system.
  - Re-run with `ANTHROPIC_AUTH_TOKEN=tok`: no `authorization` header, so
    `authToken: null` suppresses it.
  - Re-run with `ANTHROPIC_CUSTOM_HEADERS='x-stainless-timeout: hello'`:
    `x-stainless-timeout: hello` was sent, so `defaultHeaders: {}` does not
    suppress it. The entry does not claim it does.
- **Sibling entry.** PR #255 head `050ddcc2…`, its proposed Agent SDK entry.
  `findings_for` run with that real sibling document returns `[]`.
- **Egress record.** `EGRESS-CONSENT-ANTHROPIC.md` is blob `57f11a71…` at PR
  #215's head `8bcec860…`, at `7704b4a5…` and at `b17207ce…`, as the entry
  pins.
- **RFC4-9.** Taken from `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:231-235`.
- **Impact ledger sweeps.** Re-run at `b97b77ed` and at the reviewed commit.
- **The "fix list" claims.** Swept PR #258's body and comments, its review
  comments, `.beads/issues.jsonl` (370 lines) and the live `bd list --all
  --json` (438 issues).
- **My own rule-6 predicates.** Two new ones, in Finding 1 and Note 10.

## Acceptance criteria

1. **Seven RFC4-2 declarations — yes.**
   - Item 1: `observerId` / `implementationId`, ENTRY 9, 12.
   - Item 2: `implementationVersion: null`, `contractVersion`, ENTRY 13, 16.
   - Item 3: eleven `inputClasses`, ENTRY 32-77, each mapped at 293-306.
   - Item 4: five output classes, ENTRY 78-99.
   - Item 5: `determinismByOutputClass`, ENTRY 308-314.
   - Item 6: `failureStates`, ENTRY 228-264.
   - Item 7: `writeSurface: []`, `networkAccess`, ENTRY 109-114.

   No default is left silent.
2. **Substitute and nothing more — yes.**
   - The role identity is shared with PR #255's entry, whose `observerId` is
     `polaris-provider-route-anthropic-agent-sdk`.
   - The implementation identity is new: `polaris-generation/provider-messages-api`
     against #255's `polaris-generation/provider-agent-sdk`.
   - Subject, `authorityType` and `contractVersion` are equal to #255's.
   - The packet asks for exactly one entry (OWNER-DECISION-PACKET.md:12-15).
3. **`requestBytes` equals what the route sends — yes.**
   - The capture equals `closedSet`, literals and shapes by value (see above).
   - `x-stainless-timeout` is `String(Math.trunc(timeout / 1000))`
     (client.js:837) with `timeout ?? 600000` (messages.js:38), and the capture
     shows 600.
   - `accept-language`, `sec-fetch-mode` and `accept-encoding` are attributed
     to Node's fetch (ENTRY 354).
4. **Egress fit honest — mostly.**
   - The conclusion now counts three wordings (ENTRY 203), matching the three
     `needsReading` items (198-202), SEMANTIC-DELTA.md:82-86 and
     OWNER-DECISION-PACKET.md:50-57.
   - One residual inconsistency on retention remains (Note 6).
5. **Credential honest — yes.**
   - The variable name is labelled a proposal (ENTRY 123).
   - Nothing in the adapter or gate at `e76b6929` logs or persists the key.
     `MessagesApiProviderError` carries a code, attempts, a status and
     `spentUnits` (provider.ts:13-17). `GateDecision` carries method, url,
     reasons, status and `rejectedUnbilled` (egress-gate.ts:25-34).
6. **Runtime gate matches source — yes, honestly labelled.**
   - `refuse` returns 403 (egress-gate.ts:63-67).
   - The armed check is at line 76, the predicate at 82-83, the
     `permitted() === true` check at 85-86 and the upstream check at 87.
   - The gate deletes host and connection (90), applies the optional
     `stripFingerprint` (91) and answers the probe locally (77-79).
   - It forwards to any upstream, http or https (88, 92).
7. **Profile pins — yes.** ENTRY 357-361. The note-level points from round 1
   still stand: the adapter accepts `budgetTokens` (provider.ts:30, 98), and
   the entry says so.
8. **Write surface — yes.** ENTRY 109-110. The destination is now exact (ENTRY
   113).
9. **Null version, unknowns, failure vocabularies — yes, except one `unknowns`
   item that contradicts a pinned literal (Finding 1).** States and reasons sit
   within RFC2-23 and RFC2-24.
10. **Impact ledger — yes.**
    - At `b97b77ed`: 1,990 tracked files. Sweep 1 gives 8 and 22 files.
      Sweep 2 gives 0 lines, 0 lines and 0 files.
    - At the reviewed commit: 1,999 files and 23 for Sweep 1b. Sweep 2 gives
      2, 0 and 1. The 1 is `scripts/build_provider_route_messages_api_entry.py:38`,
      which is this package's own builder, as the ledger's "before this
      package" scope allows.
11. **Round-1 repairs — four hold. The re-freeze introduced one defect
    (Finding 1).** Each repair is checked below.
12. **Provenance pair and header table by value — yes.** One commit, three
    blobs, each re-derived. The entry's table equals the adapter's
    `LITERALS`/`SHAPES` (provider.ts:207-216) plus `x-stainless-timeout: 600`,
    which the adapter does not pin (Note 3).
13. **No authority claimed — yes.**
    - Python `re` swept the package for accepted/adopted/approved/signed off.
      The hits outside the brief and the raw are all conditional or refer to
      other things: ENTRY 17, 187, 201, 284; delta 44-45, 93; packet 25, 79;
      ledger 36; manifest 5; and the dispositions' "Accepted" for notes.
    - 64-hex tokens over the five `*.md` files at the package root and in
      `reviews/ROUND-1-DISPOSITIONS.md`: 0 each.
    - The claims the selftest leaves uncovered are listed in Note 10.

### Round-1 findings re-checked against the bytes

- **R1 Finding 1, `x-stainless-timeout` 600 — holds in the table.**
  - ENTRY 377 pins `"x-stainless-timeout": "600"`, and the builder compares
    the whole table by value (build script 226).
  - The source always sends 600: client.js:837, messages.js:38 and
    client.js:912 (`DEFAULT_TIMEOUT = 600000`). Re-observed in the capture.
  - The adapter at `e76b6929` still treats the header as name-only
    (`OPTIONAL_SHAPES`, provider.ts:217, 229). ENTRY 415 says so and says an
    implementation must enforce the literal. That label is honest.
  - **But ENTRY 226 still calls the value Unknown (Finding 1).**
- **R1 Finding 2, SDK environment inputs — holds.**
  - The `readEnv` enumeration gives 24 names: 20 `ANTHROPIC_*` names, plus
    `APPDATA`, `HOME`, `USERPROFILE` and `XDG_CONFIG_HOME`. The last four occur
    only in `getRootConfigPath` (core/credentials.js:255-288), in the
    credential and config chain.
  - That chain runs only when `this.apiKey == null && this.authToken == null`
    (client.js:148). The adapter passes a non-empty `apiKey` (provider.ts:97,
    115), so this route reads none of the four.
  - The entry names the five `ANTHROPIC_*` variables that matter and "any
    other ANTHROPIC_-prefixed variable" (ENTRY 142-175). That covers the other
    15 under the prefix rule, and no SDK environment input is missed.
  - The stated effects hold:
    - `ANTHROPIC_API_KEY` and `ANTHROPIC_BASE_URL` are unused when `apiKey`
      and `baseURL` are passed (client.js:71, 77-79).
    - `ANTHROPIC_AUTH_TOKEN` is suppressed by `authToken: null` (client.js:80-82,
      confirmed in the capture).
    - `ANTHROPIC_CUSTOM_HEADERS` merges into `defaultHeaders` even when `{}`
      is passed (client.js:117-127, confirmed in the capture).
    - `ANTHROPIC_LOG` is read because no `logLevel` is passed (client.js:110).
  - Enforcement: `refuseAmbientEnvironment` runs at construction and at first
    start (provider.ts:86-88, 94, 108). It is absent at `dd526b0c`, which
    builds the client at line 99 with `apiKey, baseURL, maxRetries` only.
    `constructorArguments` (ENTRY 176) equals provider.ts:115.
- **R1 Finding 3, upstream — holds.**
  - ENTRY 113 names `https://api.anthropic.com/v1/messages`, POST, and ENTRY
    138 adds the upstream-equality rule.
  - ENTRY 138 says the gate at the cited commit accepts any upstream,
    including http. That is true: egress-gate.ts:88 and 92 take
    `options.upstream.url` and choose `https` or `http` by its protocol, with
    no further check.
  - Because the rule is labelled as the entry's statement, it is honest. The
    "PR #258's fix list" provenance is unsupported (Note 2).
- **R1 Finding 4, three wordings — holds.**
  - ENTRY 203 says "three wordings", and `needsReading` has 3 items (ENTRY
    198-202).
  - The builder ties the count word to the list length (build script 326-328),
    with mutants for the count word, an added item and a removed item.
- **R1 Finding 5, RFC4-9 — holds.**
  - The clause reads: "**RFC4-9 — Substitution.** Replacing an
    implementation (a different VCS host, a different scheduler) is a registry
    event: the role identity persists, a new implementation identity is
    registered, and prior records keep resolving under the old one.
    Substitution never rewrites history and never migrates substrate-native
    aliases into the new substrate's namespace." (general-contract.md:231-235).
  - Compared by script after whitespace and `**` normalization, ENTRY 275 and
    SEMANTIC-DELTA.md:36-41 each equal that paragraph.
  - The role-versus-implementation form is followed. `observerId` is #255's,
    `implementationId` is new, and `ifTheOtherWasAdoptedFirst` (ENTRY 284)
    states the RFC4-9 replacement and that prior records keep resolving.
- **Round-1 notes 1-8.** Notes 1, 4, 5 and 7 are folded in as the
  dispositions say. Notes 2, 3, 6 and 8 are unchanged by design.
  Disposition-claim discrepancies are in Note 4.

## Findings

**Finding 1 — The entry pins `x-stainless-timeout: 600` as Observed and also lists its value as Unknown. The re-freeze introduced the Unknown and the repair left it** (blocking)

- ENTRY 226, in `unknowns`, says: "[Unknown] the x-stainless-timeout and
  connection values: the cited predicate checks their names only".
- The same bytes pin the value as a literal (ENTRY 377). They also state it
  as an observation: "[Observed, reviewer capture of SDK 0.131.0 at round 1]
  the SDK always sends x-stainless-timeout … so the value is the literal 600
  and not optional" (ENTRY 415).
- The value is not Unknown. It is 600 by source (client.js:837,
  messages.js:38) and by capture (both rounds).
- What is true of the cited predicate is an observation, not an Unknown: it
  admits any value (provider.ts:217, 229). ENTRY 415 already says that.
- History of the item:
  - It was absent at `b101829d`.
  - It was added by the re-freeze `7bbe1479` (at line 182 there).
  - It was carried into `eafb02ee` alongside the Finding 1 repair.

The act would therefore bind two contradictory epistemic labels for one byte.
An owner reading `unknowns` would be told the timeout value is unknown, and an
implementer may take the Unknown as licence to leave it unenforced. This is
the same class of defect as round 1's Finding 4: a self-contradiction inside
the act-bound bytes.

Violated clauses:
- VIS-2 / AGENTS.md epistemic discipline: a value with evidence is not
  Unknown, and one claim carries one label.
- RFC4-2 item 7, the exact boundary, as the entry applies it at ENTRY 187 and
  425.
- Criteria 9 and 11 ("did any introduce a defect").

Neither the builder nor the selftest checks this. My predicate P-B ("no
`unknowns` item marks as Unknown the value of a header pinned in
`pinnedLiterals`") fails on the reviewed bytes, naming `x-stainless-timeout`.
It passes once the item is narrowed to "the connection value", so it
discriminates (Note 10).

Repair: narrow ENTRY 226 to `connection` only, or restate it as the observed
fact that the cited predicate does not check the timeout value. Then add P-B or
an equivalent to the builder.

**Note 1 — `implementationStatus` still names the round-1 head** (note)

ENTRY 14 says the adapter is on "PR #264, stacked on PR #258, head
dd526b0c3d4de2c1add4288469e320c8c52af99b at drafting". Since the re-freeze the
entry pins `e76b6929` (ENTRY 130, 319), which is PR #264's head today. "At
drafting" keeps the sentence technically true. But the act-bound bytes now name
two different heads of one PR, and only one is the provenance.

**Note 2 — Two "[Inferred] on a fix list" claims have no findable source, and one describes code already present** (note)

- **The upstream rule.** ENTRY 138 and SEMANTIC-DELTA.md:63-64 say the
  upstream rule "is on PR #258's fix list ('upstream https') [Inferred]".
  - I swept PR #258's body and issue comments and its review comments (0
    review comments mention "upstream"). I swept `.beads/issues.jsonl` (370
    lines) with Python `re` for `upstream https|upstream.{0,40}https` and
    `fix list`: 0 lines.
  - I swept the live bead list (438 issues) for beads naming both "upstream"
    and "https": 1 hit, `syzygy-w7c` (PR #16, PWB), which is unrelated.
  - PR #258's body mentions only "an explicit `upstream` is set". The quoted
    phrase has no locatable origin.
- **The ambient guard.** ENTRY 177 says the guard "is on PR #264's fix list
  [Inferred]". In the same sentence it says, correctly, that the guard is
  [Observed] at the pinned commit. The guard is PR #264's commit `c2305b19`,
  already in that branch, so no fix list is involved.

Both are labelled Inferred, so neither is presented as fact. Still, an
[Inferred] provenance with no basis invites false reliance. The builder
requires the token "[Inferred]" in `enforcement` (build script 317), which the
second phrase may exist to satisfy.

**Note 3 — The provenance label says the table is the adapter's; one row is not** (note)

ENTRY 318 says "this entry only copies the values. The header literals and
shapes below are those of acceptMessagesApiRequest … at this commit".
`x-stainless-timeout: 600` is not in that function's `LITERALS`
(provider.ts:212-216). It comes from the round-1 reviewer's capture and the
SDK source. ENTRY 415 discloses this, so the defect is only that line 318
overstates.

**Note 4 — The dispositions misdescribe two points** (note)

- ROUND-1-DISPOSITIONS.md:36-38 says the entry "labels the enforcement
  [Inferred] pending the offering's re-check". ENTRY 177 labels the guard
  [Observed]. The only [Inferred] is the fix-list clause (Note 2).
- ROUND-1-DISPOSITIONS.md:43-44 repeats the unsupported PR #258 fix-list
  claim.
- The dispositions also do not mention the `unknowns` item that contradicts
  the Finding 1 repair (Finding 1).

The dispositions are not act-bound, but they are the record a later round
relies on.

**Note 5 — The packet says no review round has run** (note)

OWNER-DECISION-PACKET.md:85 says "No round has run". Round 1 ran, with verdict
REVISE, and its raw is retained in `reviews/` beside the packet. The brief
(lines 4-6) states the round history correctly. Per AGENTS.md, staleness should
be corrected at the sentence.

**Note 6 — Retention is "satisfied" unconditionally in one list and conditionally in two other places** (note)

- `fitsWithoutNewVersion` keeps "retention in the run directory: satisfied;
  there is no runtime state to keep" (ENTRY 196, unchanged since `b101829d`).
- `retentionCondition` (ENTRY 204) says "[Inferred] satisfied while
  ANTHROPIC_LOG is unset", and `ambientContext` (ENTRY 184) says the same.
- With the guard present (provider.ts:94, 108), the unconditional form holds
  in practice. The entry nonetheless treats enforcement as pending re-check
  (ENTRY 177), so its two statements of one condition differ.

**Note 7 — The `failureStates` note has a misplaced clause** (note)

ENTRY 240 ends "…not an observer error, and no degradation state is invented,
or an ANTHROPIC_-prefixed environment variable set in the process". The
appended clause belongs in the list of causes at the start of the sentence.
Meaning is recoverable, but it reads as a repair spliced onto the end.

**Note 8 — RFC4-9 is quoted but not listed as a cited ID** (note)

- SEMANTIC-DELTA.md:13-14 lists the IDs the entry cites: RFC4-1, 4-2, 4-3,
  RFC2-23, 2-24, RFC3-16(a), RFC5-15, 5-16. RFC4-9 is missing, although the
  entry and the delta now quote and rely on it.
- REVIEW-BRIEF.md:25-27 also omits RFC4-9 from the governing references,
  though criterion 11 asks for it.

**Note 9 — Node's own environment inputs to the forwarded TLS connection are undeclared** (note)

[Inferred, from Node's documented behaviour, not exercised here] The gate
forwards with `node:https` (egress-gate.ts:2, 92-93). Variables such as
`NODE_TLS_REJECT_UNAUTHORIZED=0` and `NODE_EXTRA_CA_CERTS`, and on Node 24
`NODE_USE_ENV_PROXY` with `HTTPS_PROXY`, can weaken certificate validation for,
or reroute, the one forwarded request carrying `x-api-key`. The adapter's guard
covers only the `ANTHROPIC_` prefix.

This lies outside round 1's SDK-scoped Finding 2, and `sdkEnvironmentInputs`
is correctly titled for the SDK. It is a candidate for the offering's
isolation conditions, beside the [Unknown: Node versions] that ENTRY 354
already records.

**Note 10 — Claims the 190-predicate selftest does not cover, and this reviewer's rule-6 run** (note)

The builder has no mutant for:
- (a) agreement between `unknowns` and `pinnedLiterals` (Finding 1);
- (b) `implementationStatus` naming the same commit as `provenance.commit`
  (Note 1);
- (c) `fitsWithoutNewVersion` retention against `retentionCondition` (Note 6);
- (d) `constructorArguments` against the adapter source;
- (e) the egress-record fit content beyond counting.

The `enforcement` predicate checks only that the tokens "ambient-environment"
and "[Inferred]" are present.

My rule-6 run (script in the reviewer's scratch, `r2-rule6.py`; nothing
tracked touched):
- **P-A.** Every key and literal value of `new Anthropic({...})` at
  `e76b6929:provider.ts` is named in `constructorArguments`, and no key is
  named that the source does not pass.
  - On the reviewed bytes it holds (`[]`).
  - Mutant 1 deletes "authToken null, " from the entry. It fails, with "entry
    omits constructor key authToken" and "entry omits value authToken null".
  - Mutant 2 deletes `authToken: null, ` from the source. It fails, with
    "entry names authToken the source does not pass".
  - Mutant 3 appends "and logLevel off" to the entry. It fails, with "entry
    names logLevel the source does not pass".
  - All three mutants are caught.
- **P-B** (Finding 1) fails on the reviewed bytes. After narrowing ENTRY 226
  to "the connection value" it holds (`[]`).

## Verdict

REVISE. One blocking finding: the act-bound entry calls the
`x-stainless-timeout` value Unknown (ENTRY 226) while pinning it as an
observed literal (ENTRY 377, 415). The re-freeze `7bbe1479` introduced that
contradiction and the round-1 repair left it. Every other round-1 finding is
repaired, and each holds against the SDK 0.131.0 source, PR #264 at
`e76b6929` and a loopback capture:
- the 600 literal;
- the SDK environment inputs with a fail-closed posture, and a guard present
  at the pinned commit;
- the exact https destination, honestly labelled as not enforced by the gate
  at that commit;
- the three-wording count;
- the RFC4-9 quote and the role-versus-implementation form.

Notes 1-10 need no change before re-review, though Notes 1-3, 5 and 7 touch
the same bytes and could be folded into the one repair. Any edit retires this
review (rule 10).
