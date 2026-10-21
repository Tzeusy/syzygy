# Review — PWB M2 slice 5 implementation-continuation packet, round 3
Reviewed commit: 78d18444f8728762cdf3ed2ff28397c9030af4ef
Artifact SHA-256: 1449eadca4f5eca3b6dd731de4f01c0d373193d83a77446e5ea72389ad013c97
Verdict: CONFIRM WITH EXCEPTIONS

Scope: all five package files at `78d18444` (`OWNER-DECISION-PACKET.md` 688 lines, `IMPACT-LEDGER.md` 247, `REVIEW-BRIEF.md` 189, `ROUND-1-DISPOSITIONS.md` 261, `ROUND-2-DISPOSITIONS.md` 152), read from a scratch clone checked out detached at that commit. The digest above is `sha256sum` of the packet in that clone, run in this session; it equals the digest the coordinator gave. I re-read the brief's criteria 1–15, the round-1 and round-2 raws, the #489 record at `8c334f67` (unchanged: `git log --all` for that file shows only `9e63b856`, `e990c27e`, `8c334f67`; the branch `agent/syzygy-sin5` still contains `8c334f67`), and `bd show` (read-only) of `syzygy-dov.19`, `.2.2` (round 2), `.5.2`.

## Preconditions the coordinator asked me to verify

- **Twin commit.** `git diff --stat 04e86895 d7b2d7e5 -- .syzygy/governance/contracts/candidates/pwb-m2-slice5-implementation-continuation` is empty, and so is the same diff over `.syzygy docs/reviews docs/README.md scripts/check_docs_review_campaign_partition.py`. The only differences between the two commits are the rebase base (13 files under `packages/polaris-dossier`, `apps/` and `docs/evidence`, none in the package). So `d7b2d7e5` carries package bytes identical to the round-2 reviewed `04e86895`, as claimed. (`ROUND-2-DISPOSITIONS.md:11-14` says the twin also carries the same "raw" bytes; neither commit contains the round-2 raw, which `a4f09aa8` adds, so that word is empty rather than wrong.)
- **Round-2 raw retained byte-exact.** `cmp` between my round-2 file and `docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-2-RAW.md` at `78d18444` is silent (identical). `a4f09aa8` adds exactly that file (101 lines) and the `docs/README.md` row update.
- **HOLD note.** `bd show syzygy-dov.5.2` shows the 2026-10-21 lead note: "HOLD. syzygy-dov.19 is this bead's last open blocker, but performing the dov.19 continuation (PR #492) does not authorize the briefing route … the coordinator adds an explicit gate dependency before closing .19." Its dependency list is unchanged (`.18`, `.22`, `.5.1` closed; `.19` in progress), so the explicit gate dependency is the pending step, as the packet says.

## Instrument decision

Unchanged from rounds 1 and 2: a plain owner direction is the right instrument. [Inferred] Nothing in B1–B11, the round-2 additions included, changes a signed or act-bound byte, an accepted contract, a registry value or semantics sentence, consent or policy. The round-2 edits touch only the packet, ledger and brief (`git diff d7b2d7e5 78d18444` over the package: ledger +30/−, packet +100/−, brief +46/−, new `ROUND-2-DISPOSITIONS.md` +151; plus the README row and the raw).

## Round-2 finding 1 (the `syzygy-dov.5.2` effect), confirmed against the bytes

All four sub-claims of brief criterion 15 are in the bytes and true:
- **Last open blocker.** Packet `:665-680` (§"The briefing-route bead") says `dov.19` is the last open blocker of `syzygy-dov.5.2` and names the closed others (`.18`, `.22`, `.5.1`). `bd show syzygy-dov.5.2` agrees.
- **Nothing authorizes the route.** The paragraph cites B9, the exclusions, the machine-view act's separate-authorization sentence and #489's Bounds. I checked the act's sentence at `PWB-MACHINE-VIEW-AMENDMENT-ACT.md:85-87`: "the briefing member stays unservable until its ceiling is declared and the route is separately authorized" (the dispositions cite lines 86–88; the quoted words are present, locator ±1). #489's Bounds list "any briefing route (`syzygy-dov.5.2` …)" among what is not authorized.
- **Hold before closing.** The paragraph says the coordinator holds the bead by a dependency or a gating note before closing `.19`; the note exists (above).
- **2026-09-30 bar not lifted.** The paragraph quotes the direction's sentence ("remains gated on `syzygy-dov.19` and the further gates the 2026-09-21 rulings name", `OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md:98-101`, verified) and says the further gates stay open for that field.
- **Stale `dov.22` wording corrected.** Packet (§"What this direction would not authorize", the briefing-route bullet) and the ledger's briefing-route interaction row now say the route waits for its own separate authorization. `grep` for `wait for the machine` over the package returns nothing.
- **"Nothing else is unblocked"** is now "Nothing else is authorized" (`:662`), true while the bead graph would show `.5.2` ready; and the question itself (`:115-118`) says the reply authorizes no briefing route "although `syzygy-dov.19` is that bead's last open blocker too".

## Round-2 notes, dispositions confirmed

- **Note 2 (B11, criterion 6): disclosed honestly, not smoothed.** The question now says, in the owner's text, "Once you confirm the 2026-10-20 direction drafted in PR #489, this reply is what releases those two uses, and it is one reply: slice 5 cannot be given without them" (`:115-118`, wrapped across lines). `ROUND-2-DISPOSITIONS.md:67-74` records the departure plainly: criterion 6 "is not met literally and must not later be read as met". It states the reason B11 is kept unsplit (an `[Inferred]` drafter's judgement, `:75-79`) and the owner's way out (decline and say so). The record section keeps "Nothing else is authorized, except the B11 uses, which also need the 2026-10-20 direction confirmed". That is a faithful disclosure; I found nothing in the three files that reads B11 as within criterion 6's letter. Residual: the bead `syzygy-dov.19` still carries the unamended criterion 6; see note 5 below.
- **Note 3 (routing).** The RFC6-14.r1, RFC7-16.r1 and RFC7-33.r1 cells now name the not-evaluated shape's claim; "Five further rows" adds RFC1-18.r2 (`CONTRACT-COVERAGE-REPAIR-DELTA.md:42`, `unknown-uncovered`; RFC1-18 `RFC-0001-…md:405-407` lists "freshness state") and RFC6-14.r2 (`:52`, `covered:PWB-REQ-007`), with the reading labelled `[Inferred]`. The count "Five" matches the list (RFC2-25.r1, RFC2-9.r1, RFC2-10.r1, RFC1-18.r2, RFC6-14.r2). See note 3 below for the one cell left unchanged.
- **Note 4 ("the only two").** B5 now says "the two aggregate claims", and adds an `[Observed]` paragraph naming `gapReasonCounts`/`gapsList` at `polaris.ts:1070-1105`, rendered at 1192 and 1239 (re-read; all four locators exact). The ledger gains a consumer row citing 1815 (the page-targets use, verified at `:1815`). The claim that a claim in the arm reaches the list as a primary-reason count with its route is correct from `gapReasonCounts` (`:1070-1079`, primary reasons only).
- **Note 5 (Review section).** Rewritten (§"Review", from `:680`) to a sentence that is true before and after any round: rounds, raws and dispositions live in sibling records; the first raw is named; the brief names the reviewing round; "The reply is offered only once a round has cleared them." No residual "No review has run on these bytes".
- **Note 6 (consent-refused `stale`).** B4 now labels it `[Inferred]` and states the result and the reason the drafter accepts it (`:252-258`); the ledger's effects list it (ledger "Effects to expect"); B10 adds the fixture (`:353-355`). Consistent with B4's stale arm for an already-Unknown claim (the gate's reason stays primary).
- **Note 7 (broken/superseded counts).** B5 `[Inferred]` rule and B7's added sentence are present, B10 adds the check. See note 2 below for a residual about the machine channel.
- **Note 8 (O1).** No change; still correct. Reading (i) is a lawful reading, the lead may decide it, (ii) is the owner's.

## Findings (all notes)

**1. Note — B7's marker for `stale` will be false in the common case once slice 5 lands — [Observed]**

B7 (`OWNER-DECISION-PACKET.md:328-332`) says a value slice 5 makes reachable "loses its marker without a separate copy edit". The marker mechanism drops the marker only when some claim carries the value (`used(entry)`, `polaris.ts:403-407`). The `stale` marker text is "Not reachable at this evaluation: no claim freshness is judged against a currency bound; declare the bound and route freshness through the currency assessor." (`design-tokens.ts:91-92`). After slice 5 every claim is judged against a bound, so on an evaluation where the judge returns no `stale`, the legend would still print that sentence and it would be false. The `fresh`, `broken` and `superseded` markers (`design-tokens.ts:89-96`) stay true. B7's stated purpose ("keeps every freshness legend sentence either reachable or marked unreachable with its reason") already requires the `stale` reason to be rewritten, so this is an over-short clause, not an unauthorized behavior: the implementer must edit `design-tokens.ts:92` (an implementation file), and the copy oracle should assert the new reason. Not a repair for the packet; worth carrying to the dispositions and to B10's legend check.

**2. Note — B5's "never a bare `0`" has no stated machine-channel form — [Inferred]**

B5 (`:291-296`) renders the `broken` and `superseded` counts "with the same unreachable marker and reason that B7 keeps on the legend, never as a bare `0`". B6 requires the same counts in both channels. A JSON count field cannot carry both a number and a marker without a chosen representation, and the packet does not say which; a machine answer that carries `0` while the page carries the marker would break the PWB-REQ-020 parity the packet promises, and an invented sentinel would be what B4 forbids for freshness. The implementer must pick a typed form and the parity family (B6) must check it. State the form or leave it to the implementation lane under B6.

**3. Note — gap-table cell for RFC6-14.r3 was not updated with its three siblings — [Observed]**

Round 2's repair added the not-evaluated shape's claim to the "What stays Unknown" cells of RFC6-14.r1, RFC7-16.r1 and RFC7-33.r1 (`:442`, `:445`, `:446`). The RFC6-14.r3 cell (machine tuple completeness, `:443`) still reads "Whether an absent freshness value plus the disclosure is 'the complete epistemic tuple'". The not-evaluated claim's machine tuple also lacks freshness and carries no arm disclosure, so the cell is slightly narrower than the other three. Nothing needs building differently; the build claims no conformance on RFC6-14.r3 either way.

**4. Note — the packet header still says "repaired after review round 1" — [Observed]**

`:13` reads "Date drafted: 2026-10-21; repaired after review round 1 the same day." The bytes were also repaired after round 2. It is a harmless history statement, but it is review history inside the packet, which the Review section now says is kept in sibling records. Deleting the clause would retire this review, so leave it and note it in `ROUND-3-DISPOSITIONS.md`.

**5. Note — bead state still to be aligned (coordinator steps, not packet bytes) — [Observed]**

(a) The explicit gate dependency on `syzygy-dov.5.2` is still to be added before `.19` closes; only the HOLD note exists. (b) `syzygy-dov.5.2`'s title still reads "blocked on the machine-view delta and the registry act", both done; the note supersedes it for a reader but the title is stale. (c) The bead `syzygy-dov.19` carries the unamended acceptance criterion 6; the departure is recorded in `ROUND-2-DISPOSITIONS.md:67-74`. A short comment on `.19` pointing to that disposition would keep a later reader from taking criterion 6 as met literally.

## Checked with no finding

- **Gate readback (criterion 1).** Re-run for this commit's tree (registry entry and spec unchanged by the round-2 edits). Registry entry in the tree: 13 `currencyBounds` rows, 7 `currencyBoundSemantics` keys; equal to the three recording tags under sorted-key JSON in round 2, and the package edits touch no governed byte (`git diff d7b2d7e5 78d18444 --stat`: only the package, `docs/README.md` and the raw). The gate-table paragraphs (`:72-92`) are unchanged since the round-2 review and still state that P-69 prepared gates and performed no continuation (`:77-78`).
- **Quotation fidelity (criterion 2).** The new quotes are exact: the machine-view act sentence (above), the 2026-09-30 direction sentence, the RFC1-18 field list, the scenario's "omits its primary reason count or hides its route" limb (`spec.md:1054-1055`) as cited at `:285-288`, and the gap-list locators. `scripts/check_quotations.py` at the commit: 33 quotations examined in 15 of 906 `.md` files, 0 findings; none of the 33 is in this package, so it stands in for nothing (rule 4).
- **Built behavior (criterion 4).** The added limbs do not add to or drop from the signed scenario: the consent-refused result keeps the gate's reason primary and adds a secondary, as the stale arm does; no fifth value or sentinel is minted for freshness; the aggregate rules are untouched except the count-rendering clause (note 2).
- **Five gaps (criterion 5).** Unchanged rows, quoted from `CONTRACT-COVERAGE-REPAIR-DELTA.md`; the build still claims no conformance on the arm; RFC1-18.r2 and RFC6-14.r2 are now routed.
- **Exclusions, wording and default (criteria 7, 8).** The question's exclusion list is intact after the inserted sentences (wider repository or content class, consent, write, egress, observed-code execution, deployment, release, recovery, mission, autonomy, multi-user), `maxBriefingResponseBytes` and `governingBehaviorContract` stay unread (B9), the exact reply line is unchanged, and the default text is unchanged.
- **Overlap with #489 (criterion 9).** Still accurate at `8c334f67`; the question now says outright that the reply is what releases the two uses once #489 is confirmed.
- **Impact sweep (criterion 10).** The baseline `29e036f4` and the ledger's published predicates are unchanged since round 2 (7 patterns, 2,939 files, 4 decode skips, reproduced then); the round-2 ledger additions are a consumer row and two effects, whose locators I re-read.
- **Precedent fidelity (criterion 11).** No manifest, digest, recorder, acceptance-record row or registration. `git grep -l -F pwb-m2-slice5-implementation-continuation` at the commit returns the packet itself and `docs/README.md` only; no manifest, `.txt`, `.yaml`, `.json` or script names the package, as `ROUND-2-DISPOSITIONS.md:51-53` says.
- **Hygiene (criterion 12).** No odd-backtick line over 1,528 non-fence lines in the five files; the only 12-or-more-hex tokens are the full 40-hex reviewed commits in the two dispositions (commits, not digests); no observed-repository path in a code span; every banner explicit. `check_governance.py --scope tracked`: 2,949 files, 0 FAIL, 0 lines naming this package. `check_docs_review_campaign_partition.py` with the clone as working directory: `total=488 assigned=488 unmatched=0 overlaps=0`, `M2 slice 5 continuation packet 2`; the README row and its "488 files, 488 assigned" sentence agree.
- **Authority boundary (criterion 13).** Nothing signs, adopts, records, unblocks (in authority terms) or says slice 5 may be built now; the briefing-route paragraph states the opposite for `.5.2`.
- **Earlier dispositions (criterion 14).** Round-2 dispositions match the packet, ledger and brief on every point above. Figures re-derived rather than copied: the `.5.2` dependency states, the gap-list locators, the three authority kinds (`body-read-authority.ts:47`), the machine-view act sentence, the zero-manifest-citers claim. I found no copied figure.

## Commands actually run, with denominators

- `sha256sum` of the packet in the clone at `78d18444`; `git log --oneline -8`; `git diff --stat` for `04e86895`↔`d7b2d7e5` (package path, then `.syzygy docs/reviews docs/README.md` and the partition script) and `d7b2d7e5`↔`78d18444` (full stat); `git show --stat a4f09aa8`; `cmp` of the round-2 raw (101 lines) against the retained copy.
- `git diff d7b2d7e5 78d18444` over the packet, ledger, brief and README; `Read` of `ROUND-2-DISPOSITIONS.md` and the packet's changed regions.
- `bd show` (read-only) of `syzygy-dov.5.2` and `syzygy-dov.19`.
- `git grep` for `unblock|dov\.22|wait for the machine` over the package; `git grep -l -F` for the package path over the tree (2 files); `FRESHNESS_ENCODING|unreachable` over `apps/three-surface-poc/src` non-tests; reads of `design-tokens.ts:80-102`, `polaris.ts` legend block.
- `check_governance.py --scope tracked` (2,949 files; 0 FAIL; grep for the package: 0), `check_quotations.py` (33 quotations; 0 findings), `check_docs_review_campaign_partition.py` (488 assigned, 0 unmatched, 0 overlaps), a line-wrap and hex-token scan over the five files (1,528 non-fence lines).
- `git log --all` and `git branch -a --contains 8c334f67` to confirm the #489 head is unchanged.

## Owner-only decision still preventing these bytes from being offered

None beyond the reply itself. Under the declared stopping rule this round has notes only, so it clears these bytes. Per the repair-review loop ruling, the notes go to `ROUND-3-DISPOSITIONS.md`, a sibling record, without editing the packet; if the lead chooses to repair note 3 or note 4 in the packet instead, that retires this confirmation (rule 10). The coordinator steps in note 5 are bead bookkeeping to do before closing `syzygy-dov.19`.

Verdict: CONFIRM WITH EXCEPTIONS
