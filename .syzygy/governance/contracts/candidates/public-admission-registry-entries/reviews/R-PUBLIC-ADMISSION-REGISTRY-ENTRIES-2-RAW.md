# R-PUBLIC-ADMISSION-REGISTRY-ENTRIES — fresh-context review, round 2
Reviewed commit: 7335d81cc7403fd31a5594d9882147c11dd563a0
Manifest SHA-256: 9bb8d937d6fe45982cc1cf30a083d2ee84bfc7ab2112eadabe52629d1e98ba34
Verdict: REVISE

Reviewer: fresh-context agent session, 2026-10-03. Read-only detached
worktree at the reviewed commit. The manifest digest above was printed by
`python3 scripts/build_public_admission_registry_entries.py --manifest-digest`
and equals `sha256sum` of the manifest file; both manifest rows equal
`sha256sum` of the two `proposed/` files. `PROVIDER-EGRESS-BYTES.md` was read
from `origin/agent/dossier-provider` at `420c60f91a7122cc0224a29ec41d4e9bb29d5ec8` (one commit touches
it). The egress record and the admission packet were read from
`origin/polaris/public-repo-admission` at `7704b4a575acf29de93e3872ff549a856e6395ec`; neither branch is an
ancestor of the reviewed commit, and no merged path exists in it. Severities
used: blocking and note only (both words the brief allows).

## Checks run

- `build_public_admission_registry_entries.py --check`: "public-admission
  registry entries: current", exit 0. `--selftest`: "selftest: 80 of 80
  predicates held", exit 0 (exit read from the script itself, not a pipe).
- `scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- Sweep 1 at the reviewed commit (1,982 tracked files):
  `git grep -l -F adapter-registry -- apps packages` 8 files;
  `-- apps packages scripts` 23 files. Matches the ledger's "22 files at the
  drafting base; 23 with this package's builder".
- Sweep 2 / criterion 6, two methods: `git grep -n -F provider-agent-sdk --
  apps packages scripts` 0 lines; `git grep -l -E` for
  `@anthropic-ai|claude-agent-sdk|claude_agent_sdk|import anthropic|from anthropic`
  0 files; a Python `re` pass over all 387 tracked files under apps, packages
  and scripts, 0 hits.
- Criterion 10, 64-hex tokens per package file (Python `re`, bounded): the
  four Markdown files 0 each; manifest 2 (its rows); each proposed JSON 1 (the
  copied `contractVersion`); the round-1 raw 1 (its own head, a retained raw).
  Authority words (`accepted|adopted|approved|signed off`) outside `reviews/`:
  6 hits, each a reference to the adopted Butlers entry or specification, the
  proposed provenance-state literal, the brief's criterion text, or the
  conditional "the adapter is accepted only when". No file labels anything in
  this package accepted, adopted, approved or signed off.
- Builder blind spots, by direct mutation of `findings_for` input (not
  selftest fixtures): appending "and all tags and full history" after the
  fetch colon returns no finding; replacing `routeConditions.acceptanceCheck`
  with "any byte passes" and `routeConditions.source` with
  "PUBLIC-EGRESS-anthropic, any version" returns no finding.

## Criteria

1. Seven declarations: present in both entries. Identity (`observerId`,
   `implementationId`), versions (`implementationVersion: null`,
   `contractVersion`), inputs (`inputClasses`, now with
   `runtime-version-and-configuration` and `owner-sign-in-credential`),
   outputs (`outputFactClasses`, now with `model-identity`), determinism
   (`determinismByOutputClass` per class), failure states (`failureStates`),
   authority boundary (`typedAuthority`). Defaults left silent: the RFC2-1
   mapping omits item 11 and several input classes (Finding 7); pipeline stop
   reasons `adapter-failure`, `cancelled` and `deadline` are unmapped
   (Finding 9).
2. Provider entry versus egress record: tools, telemetry, state location and
   fallback match the record's Conditions. The acceptance check widens the
   record (Finding 1). The ambient-context condition admits model-visible
   context the record's own Conditions bullet says the route does not add
   (Finding 4, an open owner ruling under packet O4).
3. Write surface: honest. `writeSurfaceArgument` names the egress consent as
   the explicit authority for the dispatch effect; `runDirectoryWrites` and
   `networkAccess` are split accurately; the credential write is [Unknown] and
   blocks offering. Holds against RFC4-2 item 7.
4. Fetch versus observation consent: matches and refuses more; `--no-tags`
   and `--no-recurse-submodules` are now declared and the `tags` and
   `submodules` fields state the refusal. The builder's fetch predicate is
   still prefix-only (Finding 8).
5. Determinism: nothing labels generated prose Observed (provider
   `determinism`: "never an Observed claim"). Per-class field correct; the
   scalar `determinismClass` remains (Finding 6).
6. `implementationVersion: null` and `unknowns`: honest; SDK sweep 0. One
   Observed-labelled list item misattributes origin (Finding 2).
7. Failure mappings: every name is in RFC2-23/RFC2-24. Uncertain dispatch is
   now an execution fact, uncertain usage Missing quantity, runtime
   misconfiguration `execution-blocked`, absent consent a refusal. Defensible;
   two notes (Finding 9).
8. Signing path: Scope A judged not to cover these entries, labelled
   [Inferred] (`OWNER-DECISION-PACKET.md:36`); option selection at manifest
   rows is the 2026-10-02 re-pin form. Sound. The packet now says these rows
   are not usable entries.
9. Impact ledger: counts re-derived exactly; no reader enumerates the
   registry directory. Honest.
10. Authority: none claimed; `--check` and `--selftest` pass; uncovered claims
    named in Finding 8.
11. Resource limits labelled "[Inferred] proposed values ... none is
    measured"; every declared limit now has semantics in the JSON. The packet
    still names a removed limit (Finding 3).
12. Round-1 repairs: see the table below. Two repairs introduced new defects
    (Findings 1, 3) and one is partial (Finding 6).
13. Provider entry versus `PROVIDER-EGRESS-BYTES.md` for 0.3.288 / 2.1.288:
    the generator-built parts, the SDK-fixed parts, the probe, the pin and
    the [Unknown] items match. One origin is misstated (Finding 2), and the
    list the acceptance check depends on is not in the signed bytes and is
    not pinned (Finding 1).

### Round-1 findings, one by one

| R1 | Disposition at the reviewed commit |
|---|---|
| 1 (blocking) | Resolved in substance: `readAuthority` (provider json:104) now states the runtime-added bytes, labelled [Observed, capture endpoint, no provider contacted], and drops "only the request the generator built". New defects in the repair: Findings 1 and 2 |
| 2 | Resolved: `toolInvocationNote` (json:116) names StructuredOutput and keeps it off by default; `unknowns` (json:139-146) lists the empty system message, untaken paths and the credential; `acceptanceCheck` separates envelope from content. The acceptance predicate's referent is Finding 1 |
| 3 | Resolved: `usageUncertain` → Missing quantity (json:165-169); `dispatchUncertain` an execution fact (json:170); `DEGRADATION` now holds six states (builder:40-41). Reason choice: Finding 9 |
| 4 | Resolved: `consentWithdrawn` plus `admissionFailureMapping.missingConsent` "no withdrawal event is invented" (provider json:148-151, 174) |
| 5 | Resolved: `revisionMissingAtUpstream` → Source unreachable; `revisionNotAdmitted` refused before fetch with reason 6 (git json:142-150) |
| 6 | Partially resolved: `determinismByOutputClass` added (git json:164-170); scalar `determinismClass: "capture"` kept (git json:88). Finding 6 |
| 7 | Resolved in the JSON: `maxIndexDepth` removed, `maxTreeEntries` defined, oversize blob "never chunked" (git json:108-123). The packet was not updated: Finding 3 |
| 8 | Resolved: `supersession` in both entries; `SEMANTIC-DELTA.md:71-79`; `OWNER-DECISION-PACKET.md:18-24` |
| 9 | Resolved: runtime and credential inputs (provider json:65-72), `model-identity` output (json:87-90), credential write [Unknown] (json:106) |
| 10 | Resolved: `writeSurfaceArgument` (provider json:115) |
| 11 | Resolved: tools now cover "the runtime or the provider's side" (json:120); source names record ID and version (json:119); garbled sentence gone. Version pin residual: Finding 5 |
| 12 | Resolved as stated: a mutant per `REQUIRED` key per entry (22) and per `ROUTE_KEYS` key (6); not-JSON and expected-2 mutants added. Residual blind spots: Finding 8 |
| 13 | Resolved: `REVIEW-BRIEF.md:18` names the four symbols, which exist at `scripts/check_governance.py:1647-1653, 3110` |
| 14 | Resolved: `SEMANTIC-DELTA.md:15` "018 (Source: RFC4-19)" |
| 15 | Resolved: git json:95, 104-105 |
| 16 | Resolved: `routeSubstitution` (provider json:181) |
| 17 | Resolved: `runtimeCannotMeetRouteConditions` → `execution-blocked` (provider json:156-160) |
| 18 | Resolved as a stated, labelled mapping; incomplete: Finding 7 |

## Findings

**Finding 1 — The acceptance check admits bytes the egress record refuses, and its list lives outside the signed bytes, unpinned** (blocking)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:124`: "every other byte inside the runtime-fixed or profile-set lists of
PROVIDER-EGRESS-BYTES.md for the pinned versions; any byte in neither list
fails". The egress record (`EGRESS-CONSENT-ANTHROPIC.md:100-103` at the
admission branch head) admits less: "Beyond these fields, the route adds only
the bytes that its registered provider execution route entry lists as fixed
by the runtime. A request carrying any other byte, header or field, or a
field outside the table, is refused at the single egress check." Two defects:
(a) `PROVIDER-EGRESS-BYTES.md` classes `model`, `tools`, `max_tokens`,
`output_config.effort` and `thinking` as **profile-set**, not SDK-fixed
(lines 20, 25, 27, 28, 30); none is a row of the egress record's generated
table (lines 72-92), so the egress check refuses them while the entry's
acceptance admits them. The entry says of itself (json:119) that it "cannot
widen" the record; its predicate does. (b) The egress record delegates the
runtime-fixed list to what "its registered ... entry lists", but this entry
lists those bytes only by reference to a file that is not in the reviewed
tree, sits on an unmerged branch, and is named by PR number with no commit,
path or digest. Its own summary (json:104) is not that list: it names headers
only as "platform headers that identify the machine's OS, CPU architecture
and Node runtime version", omitting `x-api-key`, `x-claude-code-session-id`,
`anthropic-beta`, `anthropic-dangerous-direct-browser-access`, `x-app` and the
`user-agent` value (`PROVIDER-EGRESS-BYTES.md:43-48`). An owner act over these
bytes would bind a predicate whose admitted set can change without the bound
bytes changing (AGENTS.md verification rules 10 and 11). Violates RFC4-2 item
7 (the authority boundary must be exact) and criterion 2. Repair: either
carry the runtime-fixed and profile-set lists in the entry for the pinned
versions, or pin the referenced file by commit and path (a 40-hex commit or a
digest may sit in the JSON); and either drop profile-set bytes from the
acceptance or state that the egress record must name them in a further
version before this entry can be offered.

**Finding 2 — An [Observed] list attributes `max_tokens` (and `cache_control`) to the runtime** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:104`: "[Observed, capture endpoint, no provider contacted] the
runtime-fixed additions are listed in PROVIDER-EGRESS-BYTES.md (PR #258): ...
max_tokens, stream, cache_control, ...". The measurement says `max_tokens` is
"profile-set | min(profile `maxOutputTokens`, permit output allowance, permit
usage allowance)" (`PROVIDER-EGRESS-BYTES.md:27`), so it is set by the
profile and the dispatch permit, not by the runtime. `cache_control` is
attached to the generator's own parts as well (`:22-23`), which bears on the
"byte for byte" comparison of generator-built parts in json:124. Criterion
13. Also: `runtimePin.note` (json:186) labels the adapter's refusal behaviour
[Observed]; the source states it as the adapter's design (`:8-10`) outside
its [Observed] paragraph (`:13`), and the adapter is unmerged; [Inferred] fits.

**Finding 3 — The packet asks the owner to confirm a limit the entry no longer declares** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/OWNER-DECISION-PACKET.md:59`: O2 "... 65,536 tree entries and index depth 16". Round-1
Finding 7's repair removed `maxIndexDepth` from the entry (git json:108-115
declares five limits; the builder's own mutant at
`scripts/build_public_admission_registry_entries.py:233` uses
`maxIndexDepth=16` as the "limit without semantics" fault). A new defect
introduced by the repair. The owner's answer to O2 would name bytes the act
argument does not carry. Fix before offering, or disposition so the owner is
told.

**Finding 4 — The entry admits model-visible runtime context that the egress record's Conditions say the route does not add** (note; open owner ruling)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:121`: "The runtime-fixed system prefix and empty system message
are model-visible context the generator did not build". Egress record
`EGRESS-CONSENT-ANTHROPIC.md:117-124`: "The route ... adds no context of its
own ... The adapter is accepted only when a captured request shows the system
prompt and messages the generator built and nothing else." The record is
internally divided (its line 100 permits runtime-fixed bytes the entry
lists). `OWNER-DECISION-PACKET.md:72-81` presents this as O4 ("accept the
listed envelope for this route"), an open owner ruling; the entry's
`ambientContext` discloses rather than hides the bytes. Not blocking. The
packet should add that accepting O4 also needs an egress record version whose
Conditions bullet no longer says "adds no context of its own" and "nothing
else", or the two signed records contradict each other.
`SEMANTIC-DELTA.md:51` ("restate the egress record's conditions") overstates
for the same reason. Separately, `docs/polaris-generation/TRACKER.md:116-122`
still plans G2 with "structured output for `responseSchema`" and acceptance
"nothing but what the generator built"; the tracker is not authority, but G2
as planned would use the schema mode the entry keeps off.

**Finding 5 — The egress record's version does not identify its bytes** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:119` pins "version 0.1.0-candidate.7 at drafting". The record carries
`Record version: 0.1.0-candidate.7` at both `108295996c0139bf2786f8be1208ed5b97148d67` and `7704b4a575acf29de93e3872ff549a856e6395ec`,
whose bytes differ (title, Scope, generated table). The entry already says
"the offering step re-pins the version in force", and the egress package is
out of scope; noted so the re-pin binds a digest, not a version string.

**Finding 6 — Git entry keeps a scalar `determinismClass: "capture"`** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json:88` beside `determinismByOutputClass` (:164-170), where four
of five classes are derivation-deterministic. RFC4-2 item 5 is per output
class (`.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md:88`). The prose (:163) says the per-class field "is the
machine form", but a consumer reading the shape precedent's key still reads
"capture" for re-derivable facts. Kept, presumably, for the Butlers shape and
the builder's `CLASSES` check; say so in the entry or drop it.

**Finding 7 — The RFC2-1 mapping omits item 11 and several input classes** (note)
Provider json:188 maps request inputs to items 7 and 8 and replies to item 6;
git json:162 maps revision, screening scope, registry entry and limits. Not
mapped: the owner-act records establishing effective status of the consents,
screening scope and the entry itself (RFC2-1 item 11,
`.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md:103-110`), and the input classes
`admitted-source-bundle`, `egress-consent`, `run-and-attempt-identity`,
`run-budget`, `owner-sign-in-credential` (provider) and
`observation-consent`, `git-tree-entry`, `git-blob` (git). RFC4-2 item 3
asks for each declared input to be mapped. Labelled [Inferred] and inherited
from the Butlers precedent; not blocking.

**Finding 8 — Selftest residuals (criterion 10)** (note)
`scripts/build_public_admission_registry_entries.py:131`: the fetch
predicate is prefix plus substring, so text after the colon widens it
unseen ("and all tags and full history" returns no finding; run above).
`:114`: the egress-source check is two substrings with no mutant for a
missing version, and "any version" passes. `routeConditions` values,
`acceptanceCheck` content, `readAuthority` and the provider entry's envelope
list are checked for presence only (`acceptanceCheck` = "any byte passes"
returns no finding). The CG-7e residual for a wholesale digest swap is the
known one. These are claims the selftest covers with no mutant, named as the
criterion asks.

**Finding 9 — Two failure-mapping notes** (note)
(a) `usageUncertain` carries `source-uncaptured-or-unreachable` (provider
json:167). RFC2-23's Missing quantity row names no reason; RFC2-24 #10 is "a
deterministic input ... not captured", while unreported usage is an absent
evidence quantity, which reads closer to #2 `missing-evidence`
(`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:131, 139`). [Inferred]; defensible either way, worth one
sentence of argument. (b) The pipeline's stop reasons
(`packages/polaris-generation-core/src/pipeline.ts:159`) include
`adapter-failure`, `cancelled` and `deadline`; the entry maps
`routeUnreachable` only. An adapter error at a reachable endpoint (malformed
stream, 5xx) is Observer failed / #10 by RFC4-4; say so, and name cancellation
and deadline as execution facts like budget exhaustion.

**Finding 10 — The packet says no review has run** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/OWNER-DECISION-PACKET.md:92`: "None has run." Round 1 ran and returned REVISE
(`reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-1-RAW.md:4`); the delta and
brief say so (`SEMANTIC-DELTA.md:5-6`, `REVIEW-BRIEF.md:5`). Stale on the
owner-facing page.

## Open owner rulings, not counted as blocking

- O1 (one shared acquisition adapter), O2 (limit values), O3 (route unknowns)
  and O4 (accept the runtime envelope) are presented as open, and no signed
  byte assumes an answer except where Finding 1 says so: the acceptance
  predicate's admission of profile-set bytes is not part of O4 and is in the
  row bytes.
- Finding 4 sits under O4 and is not blocking.
