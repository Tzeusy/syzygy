# R-PUBLIC-ADMISSION-REGISTRY-ENTRIES — fresh-context review, round 1
Reviewed commit: 690e082dc44480dd249c6a55edda5c47c786c59c
Manifest SHA-256: c9f38104f6960197a51aa016ec95c2bac6e4081036e23932483f9fc44ec9b9db
Verdict: REVISE

Reviewer: fresh-context agent session, 2026-10-03. Read-only detached
worktree at the reviewed commit. Egress record and admission packet read from
`origin/polaris/public-repo-admission` at `108295996c0139bf2786f8be1208ed5b97148d67` (not an ancestor of the
reviewed commit; no merged path exists at the reviewed commit). The manifest
digest above was printed by
`python3 scripts/build_public_admission_registry_entries.py --manifest-digest`
and matches `sha256sum` of the manifest file; both row digests match
`sha256sum` of the two proposed files.

## Checks run

- `build_public_admission_registry_entries.py --check`: "public-admission
  registry entries: current", exit 0. `--selftest`: "17 of 17 predicates
  held", exit 0. `scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52
  checks)"; CG-7d WARN lists both new labels among subjects with zero
  quotations (expected for a candidate).
- Rule 6 on the ledger's CG-7e claim: in a scratch copy, the provider row's
  digest changed in one character; `check_governance.py` then reported
  "FAIL CG-7e act-argument copies enumerated and current — 68 files examined,
  2 findings". Claim holds for a one-character mutant.
- Sweep 1 (rule 9): `git grep -l -F adapter-registry` at `dbf8ed19` (the
  reviewed commit's parent): 8 files under apps+packages, 22 under
  apps+packages+scripts; 1,973 tracked files at that commit. Ledger figures
  re-derived exactly. At the reviewed commit the scripts figure is 23 (the
  new builder). Every code reader names the Butlers file by path; the only
  `list(...)` in `governance-inputs.ts`/`walkthrough-inputs.ts` is
  `list(decisionsDir)` (governance-inputs.ts:355). No reader enumerates the
  registry directory.
- Sweep 2 / criterion 6 (two methods): `git grep -c -F provider-agent-sdk --
  apps packages scripts` returns nothing; `git grep -l -E` for
  `@anthropic-ai|claude-agent-sdk|claude_agent_sdk|import anthropic|from
  anthropic` returns 0 files; an independent Python `re` pass over all 387
  tracked files under apps, packages and scripts returns 0 hits; no
  package.json under the root, apps or packages names anthropic or claude.
- Criterion 10 sweep: 64-hex tokens per package file (Python `re`, bounded):
  4 Markdown files 0 each; manifest 2 (its rows); each proposed JSON 1 (the
  copied `contractVersion`). The words accept/adopt/approv/signed over every
  package file: every hit is either a reference to the act-bound Butlers entry
  (its current SHA-256 appears in
  `PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md` and
  `ACCEPTANCE-ACT-RECORD.md`), a negative or pending label, or the brief's
  own criterion text. No file labels anything in this package accepted,
  adopted, approved or signed off.

## Criteria

1. Seven declarations: present by key in both entries (identity, versions,
   inputs, outputs, determinism, failure states, authority boundary), with
   the defects in Findings 6, 9 and 18. Default left silent: no RFC2-1
   snapshot-input mapping (Finding 18).
2. Provider entry vs egress record: tools, ambient context, telemetry, state
   location, acceptance and fallback restated; slightly narrower than the
   egress on provider-side tools (Finding 11). Not wider on its face; but its
   own authority sentence claims more than the observed route does
   (Findings 1, 2).
3. Write surface: the three-way split is accurate for the Git entry; for the
   provider entry it is defensible but unargued (Finding 10).
4. Fetch vs observation consent: matches ("snapshot objects ... only", one
   commit per `git fetch --depth=1 <upstream> <commit>`, no working tree, no
   ancestors, no submodules) and refuses more ("a fetch of any other object,
   ref or history is refused"). Tag handling unstated (Finding 15).
5. Determinism: nothing labels generated prose Observed (provider json:85
   "never an Observed claim"). The Git entry's machine field is wrong per
   output class (Finding 6).
6. `implementationVersion: null` and `implementationStatus` honest; SDK
   import sweep 0 (above). The `unknowns` list and `readAuthority` are not
   honest against the observed route (Findings 1, 2).
7. Failure mappings: all names are inside RFC2-23/RFC2-24, but three
   mappings misroute (Findings 3, 4, 5); one note (Finding 17).
8. Signing path: Scope A judged not to cover these entries, labelled
   [Inferred] (packet:32); sound — the direction names "the observer
   registry entry" in the singular, beside the PWB deltas (Scope A
   direction:30-34). Option selection at manifest rows is the re-pin act's
   form (Ceremony, lines 39-57). But the rows offered are not the bytes that
   could ever take effect (Finding 8).
9. Impact ledger: counts re-derived exactly; honest.
10. Authority: none claimed; checks pass; selftest gaps named (Finding 12).
11. Resource limits labelled "[Inferred] proposed values ... none is
    measured" (git json:105) and in packet O2. Passes; two limits have no
    semantics (Finding 7).

## Findings

**Finding 1 — Provider entry declares the route transmits only the generator's request; the observed route sends more** (blocking)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:90`: "readAuthority": "none: the route reads no source. It transmits
only the request the generator built, after the single egress check
(RFC5-15), and receives one reply". [Inferred — from the lane-v capture facts
on Agent SDK 0.3.288 / CLI 2.1.288 relayed in this review's instructions; this
reviewer did not re-run the capture, and no capture record exists in the tree
at the reviewed commit.] The route adds a fixed system prefix ("You are a
Claude agent, built on Anthropic's Claude Agent SDK."), `metadata.user_id`
carrying `device_id`, `account_uuid` and `session_id`, an
`output_config` effort message, `max_tokens`, `stream` and
`cache_control`; it sends platform headers (`user-agent`,
`x-stainless-*`) and sometimes a body-less `HEAD /api/hello` probe, which is
a second transmission, not "one reply". The authority-boundary declaration an
owner would sign is false. Violates RFC4-2 item 7 (`.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:96`, "which
typed-authority question(s) it answers") and VIS-2 (an unverified assertion
stated as fact). Repair: state what the route is observed to add, label it,
and say which part is generator-built content.

**Finding 2 — Route conditions are restated as enforceable while the observed route contradicts three of them, and `unknowns` names none** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:101` ("every tool the runtime offers is disabled"), `:97`
(`"toolInvocation": []`), `:102` (no "environment summary"; the runtime's
fixed system prefix is model-visible context the generator did not build) and
`:105` ("a captured request shows the system prompt and messages the
generator built and nothing else"). The observed route fails the acceptance
predicate as worded (Finding 1's envelope). `outputFormat` adds a
`StructuredOutput` tool, while the port passes `responseSchema` to
`generate` (`packages/polaris-generation-core/src/pipeline.ts:110-116`) and
G2 plans "structured output for `responseSchema`"
(`docs/polaris-generation/TRACKER.md:116-117`), so the planned adapter
would invoke a tool. `unknowns` (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:113-117`) still says only "whether
the Agent SDK ... can disable tools, ambient context and telemetry". The
capability check and the egress record are out of scope; this entry's own
bytes are not. Repair: list the known divergences as Observed (with their
evidence record) and either say how the acceptance check separates
runtime envelope from content, or state that the route as observed cannot
pass it. Criterion 2 and 6; RFC4-2 item 7; VIS-2.

**Finding 3 — Uncertain usage and dispatch mapped to Partial snapshot** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:131-135` maps `usageOrDispatchUncertain` to "Partial snapshot". RFC2-23
defines Partial snapshot as "Some minimum inputs (RFC2-1) captured, others
not" (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:97`) and gives absent tokens their own state, "Missing quantity
| Cost/tokens/measures absent | **Unknown, never zero**" (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:99`).
`openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md:74`: "Missing cost/token quantity | Missing quantity"; `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md:76-79`:
"Budget exhaustion, rejected editorial output, unsupported assets and
uncertain dispatch are distinct execution/editorial facts, not new
degradation vocabulary." Against the pipeline's stop reasons
(`pipeline.ts:159`; `effect-uncertain` at :338-340, `usage-uncertain` at
:346-347): `usage-uncertain` is Missing quantity; `effect-uncertain` is an
execution fact routed through the claim-reason predicate, like the entry's
own `budgetExhaustedOrRejectedOutput` (:136). The builder cannot accept the
repair: `DEGRADATION` (`scripts/build_public_admission_registry_entries.py:39-40`)
holds five states and omits "Missing quantity", and the delta justifies the
five as "reuse the Butlers entry's five states" (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/SEMANTIC-DELTA.md:86-88`).
Violates RFC4-2 item 6 and RFC2-23.

**Finding 4 — Provider entry maps missing consent to Consent withdrawn** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:119-122`: `consentMissingOrWithdrawn` → "Consent withdrawn". `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md:76-77`:
"Absent consent refuses effects under the existing permission predicate
without inventing a withdrawal event." The Git entry gets this right
(`consentWithdrawn` at `.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:137-140`, `missingConsent` only in
`admissionFailureMapping` at :143). Repair: split as the Git entry does.

**Finding 5 — A non-admitted revision is routed as unreachable rather than unconsented** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:125-128`: `revisionMissingOrNotAdmitted` → "Source unreachable",
`source-uncaptured-or-unreachable`. A revision the observation consent does
not list is outside the grant; RFC2-24 separates reasons by resolution route:
#6 `unconsented-source-or-provider` "Record consent" (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:135`) versus #10
"Repair the observer/source" (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:139`). Conflating them routes the owner to
repair a fetch when the remedy is a consent version. Repair: missing at the
upstream → Source unreachable; not admitted → refused before fetch with #6.

**Finding 6 — Git entry's `determinismClass` labels derivations as capture** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:88-89`: `"determinismClass": "capture"` for the entry while the prose
says tree listing, blob reads and span derivation are
derivation-deterministic, and `source-reference`, `source-span` and
`content-exclusion` (:72-82) are such derivations. RFC4-2 item 5 is "per
output class" (`.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:88`); `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md:45` "Each output classified". A consumer
reading the machine field treats re-derivable facts as re-capturable. Repair:
a per-class determinism field.

**Finding 7 — Two proposed limits have no semantics, and one limit's semantics is an undecided alternative** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:109-111` declares `maxTreeEntries` and `maxIndexDepth`;
`resourceLimitSemantics` (:113-119) defines neither, and "index depth" has
no referent in a generic Git acquisition (the Butlers precedent's index
traversal does not exist here). `:115`: a larger blob "is excluded with a
recorded reason, or chunked into spans by the reader" — signed bytes would
leave the behaviour open, and chunking admits bytes past `maxBytesPerSource`.
The precedent defines every limit it declares. Criterion 11's labelling
itself passes.

**Finding 8 — The rows offered for the acts are not bytes that could ever admit output** (revise)
Both entries carry `"implementationVersion": null` (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:13`, `.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:13`) and
`governingBehaviorContract.version` "Unknown: pinned by the offering step"
(`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:20`, `.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:20`). Pinning changes the bytes, the row and the act
argument, and retires this review (rule 10); filling the implementation
version (required before output is admissible, RFC4-3, `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:109-111`) does
the same. `.syzygy/governance/contracts/candidates/public-admission-registry-entries/SEMANTIC-DELTA.md:65-67` says "A signed entry therefore enables
nothing until code lands and the generator's consent-backed ports (gap G3)
consult it", which implies code landing suffices; `.syzygy/governance/contracts/candidates/public-admission-registry-entries/OWNER-DECISION-PACKET.md:24-31`
describes signing "at the manifest rows" of this manifest without saying
these rows will be replaced before any offering. Repair: state that each
usable entry is a later version needing its own review and act, and what
signing these bytes would buy, if anything.

**Finding 9 — Provider entry omits configuration and version dependencies and a model-identity output** (revise)
`openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md:43`: Inputs "including policy/configuration/version dependencies". The
runtime (SDK and CLI) version and its configuration change the request bytes
(Finding 1's prefix and envelope), and the route reads the owner's sign-in
credential, yet `inputClasses` (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:32-65`) lists none of them. The egress
record says "The model is recorded per run" and the port carries `model` on
`lateReceipt` (`pipeline.ts:129`); `outputFactClasses` (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:66-83`) has no
model-identity class. `runDirectoryWrites` calls the run directory "the only
local write" (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:92`); whether a signed-in runtime refreshes its credential
outside it is [Unknown] and unlisted. RFC4-2 items 3 and 4; RFC4-3.

**Finding 10 — The provider dispatch is an effect, but `writeSurface: []` is not argued** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:91,94`. The pipeline treats a dispatch as an effect
(`permitted` "Rechecks effect permission immediately before dispatch",
`pipeline.ts:106`; `effect-uncertain`), and transmitted content is retained
by the provider under the account's terms. Treating it as network access
authorized by the egress consent rather than as a write is defensible under
RFC4-2 item 7 ("empty unless explicitly authorized"), but the entry should
say that the egress consent is the explicit authority for that effect.

**Finding 11 — Tool condition narrower than the egress text; source unpinned; garbled sentence** (note)
Egress: "invokes no tools on the provider's or its runtime's side". `.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:101`
covers only "every tool the runtime offers", omitting provider-side tools,
and reads "the model sees only the request carries" (missing a word).
`routeConditions.source` (`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:100`) names "instances/egress-anthropic" with no
record ID or version, though that record is versioned per target
(`0.1.0-candidate.7` at `108295996c0139bf2786f8be1208ed5b97148d67`).

**Finding 12 — Selftest coverage gaps (criterion 10)** (note)
Predicates with no mutant: "not exactly one entry", "not JSON", "expected 2
proposed entries"; 10 of 11 `REQUIRED` keys (only `failureStates` is
dropped); 5 of 6 `ROUTE_KEYS` (only `telemetry`); `status` is mutated only on
the provider entry and `adoptionStatus` only on the Git entry. Claims the
builder does not check at all: that route conditions do not widen the egress
record (key presence only); the fetch predicate is a substring test, so a
fetch string adding "and all tags" passes; the provider entry's
`workingTreeRead` and both `networkAccess` arrays are unchecked. The ledger's
CG-7e claim holds for a one-character mutant (above); a wholesale digest
swap is the known CG-7e residual.

**Finding 13 — Brief names a symbol prefix that does not exist** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/REVIEW-BRIEF.md:18`: `PUBLIC_ADMISSION_REGISTRY_*`. The registration is
`PUBLIC_REGISTRY_DIR`, `PUBLIC_REGISTRY_MANIFEST`, `PUBLIC_REGISTRY_ACTS`
(`scripts/check_governance.py:1647-1653`) and
`_activate_public_registry_manifest_copy_registry`. Reviewed under those
names.

**Finding 14 — REQ-polaris-generation-018 miscredited to RFC4-2** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/SEMANTIC-DELTA.md:13-15`: "REQ-polaris-generation-017 and 018 (Source:
RFC4-2)". `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md:962`:
"Source: RFC4-19".

**Finding 15 — Fetch does not declare tag and submodule refusal flags** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:94` gives `git fetch --depth=1 <upstream> <commit>`. An annotated tag
object is outside the consent's object set (commit, trees, blobs). Whether
Git's tag auto-following applies to this URL-plus-object-id form is
[Unknown] to this reviewer; declaring `--no-tags` and
`--no-recurse-submodules` makes the refusal mechanical rather than
dependent on defaults.

**Finding 16 — "A different route is a new registry event" sits awkwardly with RFC4-1** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:106`. RFC4-1: "Every external authority is reached through exactly one
registered adapter per project" (`.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:73-75`). A different route to
Anthropic would replace this entry (substitution), not join it.

**Finding 17 — Runtime that cannot be configured maps to Observer failed** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:123-126`. A run that does not start because its environment cannot
meet the conditions matches RFC2-24 #12 `execution-blocked` ("an environment
the profile could not satisfy", `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:141`) better than #10; an unreachable
endpoint stays #10. Consider splitting.

**Finding 18 — No RFC2-1 snapshot-input mapping** (note)
RFC4-2 item 3: inputs "each mapped to the snapshot minimum-input list
(RFC2-1)" (`.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:84-85`); `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md:43` "their snapshot-input mapping". Neither
entry maps its `inputClasses`. The installed Butlers precedent has the same
gap, so this is inherited rather than new.
