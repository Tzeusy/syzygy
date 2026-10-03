# R-PUBLIC-ADMISSION-REGISTRY-ENTRIES — fresh-context review, round 3
Reviewed commit: 2ffebeb304c18944643ea5ee774332dd9ea6f02f
Manifest SHA-256: 53ff9f2fa22cb96add7ab1317b94075cc8fd096344463ca648c27a44963261c5
Verdict: REVISE

Reviewer: fresh-context agent session, 2026-10-03. Read-only detached
worktree at the reviewed commit. The manifest digest above was printed by
`python3 scripts/build_public_admission_registry_entries.py --manifest-digest`
and equals `sha256sum` of the manifest file; both manifest rows equal
`sha256sum` of the two `proposed/` files. `PROVIDER-EGRESS-BYTES.md` was read
as git objects from the local clone (`git cat-file`, `git ls-tree`, `git log
--all`) on the `agent/dossier-provider` history. The egress record and the
admission packet were read from `origin/polaris/public-repo-admission` at
`b17207ce7d2d5d314b683e111e4440886916cffe`; neither branch is an ancestor of
the reviewed commit and no merged path exists in it. Severities used:
revise and note (both words the brief allows).

## Checks run

- `build_public_admission_registry_entries.py --check`: "public-admission
  registry entries: current", exit 0. `--selftest` (run unpiped): "selftest:
  91 of 91 predicates held", exit 0.
- `scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".
- Sweep 1 (1,983 tracked files): `git grep -l -F adapter-registry -- apps
  packages` 8 files; `-- apps packages scripts` 23 files. Matches the
  ledger (`IMPACT-LEDGER.md:10-11`).
- Sweep 2 / criterion 6, two methods: `git grep -l -E
  '@anthropic-ai|claude-agent-sdk|claude_agent_sdk|import anthropic|from anthropic'
  -- apps packages scripts` 0 files; `git grep -n -F provider-agent-sdk` over
  the same trees 0 lines; a Python `re` pass over all 387 tracked files under
  apps, packages and scripts, 0 hits.
- Criterion 10, standalone 64-hex tokens per package file (Python `re`): the
  four Markdown files 0 each; manifest 2 (its rows); each proposed JSON 1 (the
  copied `contractVersion`); each retained raw 1 (its own head). Authority
  words outside `reviews/`: the packet's two `owner-adopted` provenance-state
  literals, the brief's criterion text, the provider JSON's "adopted Butlers
  observer entry" and "the adapter is accepted only when", the git JSON's
  "the adopted Butlers observer entry" (json:17). No file labels anything in this
  package accepted, adopted, approved or signed off.
- Provenance pin, by `git` objects: `git rev-parse
  420c60f91a7122cc0224a29ec41d4e9bb29d5ec8:docs/polaris-generation/PROVIDER-EGRESS-BYTES.md`
  is blob `2ca77ab5f042ffeb8952fbad7c3a3a2825f7ff60`; blob
  `2e7d176e668417bf9842be8b11703f5fe2cc39ca` is the file at the next commit,
  `1e94713ae6a638771f81f71ea523c0a66ed9ddc5` (Finding 2).
- Builder blind spots, by direct mutation of `findings_for` input: appending
  "Any header value is also admitted." to `acceptanceCheck`, appending
  `cookie: anything` to `requestBytes.headers`, setting
  `routeFixedByThisEntry.model` to "any model" and `.thinking` to "adaptive"
  each return no finding (Finding 6).

## Criteria

1. Seven RFC4-2 declarations: present in both entries. Identity
   (`observerId`, `implementationId`), versions (`implementationVersion:
   null`, `contractVersion`), inputs (`inputClasses`), outputs
   (`outputFactClasses`), determinism (`determinismByOutputClass`, scalar
   explained by `determinismClassNote`), failure states (`failureStates`,
   `admissionFailureMapping`), authority boundary (`typedAuthority`). No
   default left silent that round 2 named: item 11 and every input class are
   now mapped; `adapter-failure`, `cancelled` and `deadline` are mapped.
2. Provider entry versus egress record: tools, telemetry, state location and
   fallback match the record's Conditions; the pinned model is narrower than
   the record's "The model is recorded per run, not fixed here"
   (`EGRESS-CONSENT-ANTHROPIC.md:21`). The ambient-context divergence is
   disclosed and routed to O4 (Finding 4). The acceptance check is closed in
   form but `requestBytes` is open in header values (Finding 1).
3. Write surface: honest; unchanged from round 2 and still holds against
   RFC4-2 item 7. The credential write remains [Unknown] and blocks offering.
4. Fetch versus observation consent: `typedAuthority.fetch` (git json:95) is
   now checked for exact equality with `FETCH_FULL` (builder:50-53, 158-160);
   `--no-tags` and `--no-recurse-submodules` declared; refuses more than the
   consent grants. Holds.
5. Determinism: nothing labels generated prose Observed (provider json:97).
   Per-class field governs; scalar explained in both entries. Holds.
6. `implementationVersion: null` and `unknowns`: honest; SDK sweep 0. One
   [Observed] label spans pinned, unobserved values (Finding 3).
7. Failure mappings: every name in RFC2-23/RFC2-24; usage reason argued
   (json:168); adapter failure, cancellation and deadline mapped
   (json:172-177). Defensible.
8. Signing path: unchanged; Scope A judged not to cover these entries,
   [Inferred] (`OWNER-DECISION-PACKET.md:36`); manifest-row form matches the
   2026-10-02 re-pin. Sound.
9. Impact ledger: counts re-derived exactly. Honest.
10. Authority: none claimed; `--check` and `--selftest` pass; uncovered
    claims named in Finding 6.
11. Resource limits: labelled "[Inferred] proposed values ... none is
    measured" (git json:109); every declared limit has semantics
    (json:116-123); the packet's O2 now names exactly the five declared
    limits (`OWNER-DECISION-PACKET.md:57-59`). Holds.
12. Repairs: see the table below. Round-2 F1 is partially resolved
    (Findings 1, 2); two owner-facing pages carry stale sentences introduced
    or left by the repair (Finding 5).
13. Provider entry versus `PROVIDER-EGRESS-BYTES.md` at commit `420c60f9`:
    the generator-built parts, runtime-fixed body fields, absent-by-construction
    list, header names, probe and [Unknown] items match that version
    (the `thinking` sentence at json:238 is that version's line 30, not the
    cited blob's). The entry does not carry the header values the later blob
    enforces as literals (Finding 1), and the cited blob is not at the cited
    commit (Finding 2).

### Round-2 findings, one by one

| R2 | Disposition at the reviewed commit |
|---|---|
| 1 (blocking) | Partially resolved. (a) Profile-set fields are now pinned inline in `routeFixedByThisEntry` (json:234-241) and the acceptance check says it "admits no profile-set byte beyond the values this entry pins" (json:124). (b) The list is now inline (`requestBytes`, json:215-270) and the external file is "provenance only" (json:216). Residuals: header values and "transport headers" are not fixed by the bound bytes (Finding 1); the provenance pin does not resolve (Finding 2); the claim that pinning yields "the form the egress record admits" (json:240) is a reading of the egress record (Finding 4) |
| 2 | Resolved: `runtimePin.note` now [Inferred] (json:192); cache_control attributed to the generator's parts as runtime-attached (json:114, 225-226); `max_tokens` moved to `routeFixedByThisEntry` as a ceiling. Residual label scope: Finding 3 |
| 3 | Resolved: O2 lists five limits and says the index-depth limit was removed (`OWNER-DECISION-PACKET.md:57-59`) |
| 4 | Resolved: O4 says accepting needs an egress record version (`OWNER-DECISION-PACKET.md:79`); entry `ambientContext` says the same (json:121); delta names the divergence (`SEMANTIC-DELTA.md:52-55`). New stale sentence in O4: Finding 5 |
| 5 | Resolved as a stated plan: the offering pins the record "by the digest of its own manifest row" (json:119); the admission package carries a manifest row for `EGRESS-CONSENT-ANTHROPIC.md` |
| 6 | Resolved: `determinismClassNote` in both entries (provider json:271, git json:182), checked by the builder (builder:106-107) |
| 7 | Resolved: all 10 provider and all 8 git input classes mapped, item 11 used for consents, scope and entries (provider json:194-207, git json:162-173); builder enforces coverage (builder:108-113) |
| 8 | Resolved as stated: exact fetch equality, egress-source regex requiring a version, acceptance words, pinned-field and request-bytes mutants. Residual presence-only checks: Finding 6 |
| 9 | Resolved: reason 2 argued (json:168); `adapterFailureAtReachableEndpoint` and `cancelledOrDeadline` (json:172-177) |
| 10 | Resolved: `OWNER-DECISION-PACKET.md:92` "Round 1 returned REVISE and round 2 REVISE" |

Round-1 findings: the round-2 table disposed each; no round-3 edit reopens
any. Round-1 F1/F2's "by reference to `PROVIDER-EGRESS-BYTES.md`" is now
superseded by the inline list, whose residuals are Findings 1 and 2.

## Findings

**Finding 1 — `requestBytes` fixes header names but not header values, and admits an open "transport headers" class** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:242-258`
lists `anthropic-version`, `anthropic-beta (CLI feature betas)`,
`x-stainless-lang`, `x-stainless-package-version`, `x-stainless-retry-count`,
`x-stainless-timeout`, `anthropic-dangerous-direct-browser-access` and
`x-claude-code-session-id` by name only, and ends with "transport headers".
The acceptance check (json:124) requires "every other byte equal to
requestBytes: ... the headers list" and "Any byte, header or field in neither
fails". For a header named without a value there is no byte to be equal to,
so the bound text either admits any value or cannot be met; "transport
headers" admits an unenumerated set of names. `anthropic-beta` is not inert:
its value switches provider-side features (the measurement's own line 53 at
blob `2e7d176e…` lists eight betas, including `context-management-2025-06-27`
and `mid-conversation-system-2026-04-07`, and line 50 adds a ninth for
adaptive thinking). That blob says header values are "enforced as literals"
and that machine-identifying values are "checked by shape only"; the entry
carries neither the literals nor the shapes. This is the residue of round-2
Finding 1(b): which header bytes the route may carry is decided by the
adapter's literal table, not by the bytes an act would bind (AGENTS.md rules
10 and 11). Violates RFC4-2 item 7 (exact authority boundary) and criterion 2;
`requestBytes.status` (json:216) and `readAuthority` (json:104, "listed in
full") overstate. Repair: carry each fixed header value for the pinned
versions inline (at least `anthropic-version`, the exact `anthropic-beta`
string with thinking off, `x-stainless-lang`, `-package-version`,
`-retry-count`, `-timeout`, `anthropic-dangerous-direct-browser-access`,
`x-app`), the equality rules for `x-api-key` and `x-claude-code-session-id`,
the shape rule for the OS/arch/runtime-version headers, and an enumerated
transport-header set.

**Finding 2 — The provenance pin names a blob that is not at the named commit** (revise)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:217`:
"PROVIDER-EGRESS-BYTES.md on the branch of PR #258, blob
2e7d176e668417bf9842be8b11703f5fe2cc39ca at commit
420c60f91a7122cc0224a29ec41d4e9bb29d5ec8". At that commit the file is blob
`2ca77ab5f042ffeb8952fbad7c3a3a2825f7ff60`; blob `2e7d176e…` is the file at
`1e94713ae6a638771f81f71ea523c0a66ed9ddc5`, the next commit, which rewrote
the `thinking` row to "profile-set: `off` or `adaptive`", added the exact
`anthropic-beta` value and changed the header heading to "names and values
enforced". The entry's own content follows the earlier version (json:238
reproduces `2ca77ab5` line 30, "absent (`CLAUDE_CODE_DISABLE_THINKING=1`) ...
not supported"). An [Observed] record whose subject and digest disagree
cannot be re-checked against the bytes it describes (AGENTS.md rule 11), and
the brief's F1 repair claim ("a blob and commit named", `REVIEW-BRIEF.md:47-48`)
does not hold as stated. Repair: name one consistent (commit, blob) pair and
make the inline bytes agree with that version; the later blob is the one
whose header literals Finding 1 needs.

**Finding 3 — An [Observed] label spans pinned values no capture showed** (note)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json:104`:
"[Observed, capture endpoint, no provider contacted] the additions are listed
in full in requestBytes: ... the pinned model, the max_tokens ceiling, ...".
The model `claude-opus-5-5`, effort `high` and the 64000 ceiling are this
entry's choices (json:235-239, the ceiling itself "[Inferred proposal]"), and
the measurement's default effort is `medium`; they are not runtime additions
and were not observed in that form. "Listed in full" is also false while
Finding 1 stands. Split the sentence: observed runtime additions, then the
entry's pinned values without the Observed label. Criterion 13.

**Finding 4 — The entry and the egress record still contradict each other; routed to O4, with one entry sentence assuming a reading** (note; open owner ruling)
The egress record admits beyond its table "only the bytes that its
registered provider execution route entry lists as fixed by the runtime" and
refuses "a field outside the table"
(`EGRESS-CONSENT-ANTHROPIC.md:100-103` at `b17207ce`), and its Conditions say
the route "adds no context of its own" and the adapter is accepted only when
a captured request shows "the system prompt and messages the generator built
and nothing else" (`:117-124`). The entry admits a runtime-fixed system
prefix and empty system message (json:121, 229-230) and the fields `model`,
`tools`, `max_tokens`, `output_config.effort`, none of which is a table row
and none of which is fixed by the runtime. These contradict. The packet
presents the choice as open: O4 (`OWNER-DECISION-PACKET.md:72-81`) recommends
accepting the envelope and says acceptance "needs a version of the egress
record" whose Conditions no longer say "adds no context" or "nothing else",
and the admission package lists Route A versus Route B under "Open before an
offering ... none is written into a signed record as pending". No signed
byte enables a dispatch on an assumed answer: the entry itself says accepting
the envelope needs a further egress record version (json:121), and these rows
enable nothing (json:186). This is therefore a note, not a blocker. Two
residues to repair with Finding 1: json:240 states as fact that pinning the
profile fields makes them "bytes it lists as fixed, the form the egress
record admits" — the record says "fixed by the runtime", so this is a reading
and should be [Inferred]; and O4 names only the context divergence, so it
should also tell the owner that the further egress version must admit the
pinned `model`, `tools`, `max_tokens` and effort fields (the record's "a
field outside the table, is refused" excludes them on either route).

**Finding 5 — Two owner-facing sentences are stale after the repair** (note)
(a) `.syzygy/governance/contracts/candidates/public-admission-registry-entries/OWNER-DECISION-PACKET.md:76-77`:
"The entry lists these by reference to `PROVIDER-EGRESS-BYTES.md` (PR #258)",
contradicted by the same item's line 79 ("carries the runtime-fixed byte list
inline") and by json:216 ("cited as provenance only"). A new defect
introduced by the F1 repair. (b)
`.syzygy/governance/contracts/candidates/public-admission-registry-entries/SEMANTIC-DELTA.md:5-6`:
"Round 1 returned REVISE ...; this is the round-2 repair." Round 2 also
returned REVISE (`reviews/R-PUBLIC-ADMISSION-REGISTRY-ENTRIES-2-RAW.md:4`) and
these are the round-3 bytes (`REVIEW-BRIEF.md:5`). Criterion 12.

**Finding 6 — Selftest residuals (criterion 10)** (note)
`scripts/build_public_admission_registry_entries.py:131-139`: the acceptance
check is three substrings (`ACCEPTANCE`, builder:55), so text appended after
them widens it unseen; `requestBytes.headers` and `runtimeFixed` are checked
for presence only, so an added header passes; `routeFixedByThisEntry` keys are
checked for presence, not value, so `model: "any model"` or `thinking:
"adaptive"` passes; the provenance (commit, blob) pair is not checked against
git (Finding 2 passed `--check`). All four mutations above returned no
finding. These are claims the selftest covers with no mutant, named as the
criterion asks. The CG-7e residual for a wholesale digest swap is the known
one.

## Open owner rulings, not counted as blocking

- O1 (one shared acquisition adapter), O2 (limit values), O3 (route
  unknowns) and O4 (accept the runtime envelope, route A versus B) are
  presented as open; no signed byte assumes an answer that enables an effect.
- Finding 4 sits under O4 and is a note.
- Findings 1 and 2 are not owner choices: they are exactness and provenance
  defects in the row bytes, and either alone keeps the verdict at REVISE.
