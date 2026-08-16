# Round-2026-08h — disposition register

> **The repair account, kept separate from the reviewers' bytes.** Raw
> review output lives beside this file and is never edited. Every finding
> is dispositioned `repaired` · `open` · `declined` — never "acknowledged",
> and nothing is dismissed by omission.
>
> **A repair session cannot confirm its own repairs.** Everything marked
> `repaired` here is repaired *in this session's judgement* and is not
> confirmed. Confirmation requires a fresh review of the repaired bytes.
>
> **In-flight owner work, deliberately excluded.** While this round ran,
> the owner's co-lead session ruled P-31, P-33, P-35, P-36, P-37, P-38,
> P-39 and P-40 in the working tree, uncommitted. Every review in this
> round is bound to frozen commit `918574c`, where those rulings do not
> yet exist, and every repair below states prerequisites (for example
> "rule P-40 first") as of that commit. When the rulings land, those
> prerequisite statements become satisfied, not wrong.

## RD-63 — the P-41 owner packet (`SPECIFICATION-ACCEPTANCE-DECISION.md`)

`VERDICT: REVISE` — 2 BLOCKING, 3 MATERIAL, 7 MINOR. Dispatched 2026-08-16
against frozen commit `918574c` (subject sha256 `effd5545…`); fresh
context; two-phase protocol (packet-only read, then verification against
cited references); same model family as the corpus authors, so it supports
repair and is not the formal launch administration. Raw bytes:
`RD-63-p41-spec-acceptance-packet-RAW.md`.

| # | Finding | Disposition |
|---|---|---|
| **F1** | *BLOCKING* — the packet states the subject "has had no fresh-context review"; it was reviewed as RD-51 and returned `REVISE` | **repaired.** The "Review state" section now names RD-51 at its round-08f path, copies the verdict word, states the repair was made by the session that read the verdict, and cites the register's disposition tally (15 / 4 in part / 1 open) instead of restating a severity count |
| **F2** | *BLOCKING* — RD-51 f14 (completeness against capability, deliberately open) is routed to P-41 by name and the packet hides it; arm (a) is costed as if it makes E5 `Met` | **repaired.** A "What stays open under every arm" paragraph discloses f14 and f15's open limbs; arm (a)'s benefit now states it does **not** make `E5` `Met`; the recommendation repeats the limit |
| **F3** | *MATERIAL* — the ordering constraint quotes deleted `CC-SPEC-1` text and gives a repaired defect as its live rationale | **repaired.** Re-grounded on the clause's own current bar — *"This clause may not be frozen before P-40 is ruled"* — with the amend-before-act consequence stated |
| **F4** | *MATERIAL* — "Independent work" says the review can be ordered now; the next-transaction section and two other records sequence it after P-40 | **repaired.** The "Independent work" section is deleted; the ordering constraint states why commissioning early spends a review on bytes a P-40 ruling then amends |
| **F5** | *MATERIAL* — the arms are not costed on comparable terms; (a)'s speed cost is unpriced | **repaired.** (a) now prices the full cycle (review, disposition, possible repair pass, freeze, act) and names elapsed time as the price (b) exists to avoid |
| **F6** | *MINOR* — (c) omits that a `Not met` E5 blocks any `READY` verdict | **repaired.** (c) quotes the §4 every-E-question conjunct and the never-deferrable rule (verified against instrument lines 538/633 this session) |
| **F7** | *MINOR* — "both confirmations survive" never names its referents | **repaired.** The digest table's prose now routes *retire*/*survive* to `PROCESS-GLOSSARY.md` |
| **F8** | *MINOR* — the exact next transaction is given only for the recommended arm | **repaired.** (b) and (c) each get a named transaction and record site |
| **F9** | *MINOR* — the digest-consequence section's warrant cites an untracked "owner charter §16" | **repaired.** The citation is dropped; the date stands alone |
| **F10** | *MINOR* — `## Question` is an instruction presupposing the answer | **repaired.** Rephrased as the three-route question |
| **F11** | *MINOR* — the joint-review rationale is half the register's, and P-44's inclusion makes it a three-subject review | **repaired.** Both independent coupling reasons stated; the review named as three-subject |
| **F12** | *MINOR* — "the precedent exists" overstates CC-TEST-2, whose own confirming act is unperformed | **repaired.** Qualified: precedent for the form, act 2 unperformed, no craft amendment yet completed the route end to end |

**Repaired: 12. Open: 0. Declined: 0.** All repairs are this session's
judgement and none is confirmed.

## RD-64 — the P-42 owner packet (`SHAPE-TO-SPEC-IMPACT-DECISION.md`)

`VERDICT: REVISE` — 2 BLOCKING, 3 MATERIAL, 6 MINOR. Dispatched 2026-08-16
against frozen commit `918574c` (subject sha256 `fff2466f…`), concurrently
with RD-63 and with no knowledge of it; fresh context; two-phase protocol;
same model family. Raw bytes: `RD-64-p42-impact-packet-RAW.md`.

| # | Finding | Disposition |
|---|---|---|
| **B1** | *BLOCKING* — the "exact next transaction" is not performable: the joint subject includes `CC-SPEC-1`, which may not be frozen before P-40 is ruled, and the packet mentions P-40 zero times | **repaired.** "Rule `P-40`" is now step 1 of arm (a), and the coupling paragraph states that ruling jointly with P-41 drags in P-41's prerequisite |
| **B2** | *BLOCKING* — option (c) is labelled "Launch knowingly without it" and priced as one recorded decision; the §4 formula makes every E question `Met` a non-deferrable conjunct of any `READY` verdict | **repaired.** (c) is relabelled "Decline the rule, and record it"; the option, its cost row, and the recommendation each state that (c) forecloses a `READY` verdict under the instrument as written and pairs with amending the gate (P-34), not launching past it. Instrument quotes verified at lines 538/626/633 this session |
| **M1** | *MATERIAL* — the prior verdict word `REVISE` is never stated | **repaired.** The banner copies `VERDICT: REVISE` exactly and cites the register's disposition tally |
| **M2** | *MATERIAL* — the known-open list omits the undefined term *"consumes its vocabulary"* that the subject policy flags against itself | **repaired.** Added as its own bullet, naming the trigger limb it governs |
| **M3** | *MATERIAL* — the RD-51 provenance pointer names round-08g; RD-51 lives in round-08f | **repaired.** Full round-08f path in the provenance row |
| **m1** | *MINOR* — f15 listed as "open" where the register grades it "repaired in part" | **repaired.** Both f14 and f15 now carry the register's exact grade |
| **m2** | *MINOR* — "superseded by a fixture 3" reads as accomplished; no fixture 3 exists | **repaired.** Stated as "filed as work, not done", with today's fixture population named |
| **m3** | *MINOR* — option (b) has no exact next transaction | **repaired.** (b) gets its freeze-compute-act-record transaction |
| **m4** | *MINOR* — `CONFIRM CRAFT AMENDMENT` used with no pointer, and no act row exists for these policies | **repaired.** Step 5 states no act row exists yet and names act 2 as the phrase precedent |
| **m5** | *MINOR* — digest consequences under (c) and (d) left to inference | **repaired.** Stated: no act, so no digest binds, and that absence is the recorded state |
| **m6** | *MINOR* — the `CC-IMPACT-6` → P-44 coupling is unmentioned | **repaired.** Disclosed as a non-blocking coupling in the transaction section |

**Repaired: 11. Open: 0. Declined: 0.** All repairs are this session's
judgement and none is confirmed.

## RD-61 — launch-gate policy semantics at v2.2

`VERDICT: REVISE` — 1 BLOCKING, 5 MATERIAL, 5 MINOR. Dispatched 2026-08-16
against frozen commit `918574c`, concurrently with RD-62 and mutually
blind; fresh context; same model family as the corpus authors, so it
supports repair and is not the formal launch administration. Raw bytes:
`RD-61-launch-policy-v2.2-RAW.md`.

Before the findings, the commissioned answers: **all ten RD-55 findings
verified closed** (one partially, recorded as m3/m4), the v2.1→v2.2
differential found **nothing weakened**, and an 814-site injection sweep
found zero leaks. The new findings are in the v2.2 additions themselves.

| # | Finding | Disposition |
|---|---|---|
| **f1** | *BLOCKING* — §5 says "committed schema"; the tool compares paths and reads the working tree. An audit-clean in-place enum widening admits a §2-forbidden verdict word into an eligible `READY FOR` record | **repaired.** The schema is read from `git show HEAD:`; working-tree drift is its own `LA-1` error; the reviewer's exact attack is a fixture, asserted in both directions and mutation-tested |
| **f2** | *MATERIAL* — `repository_commit` anchored to nothing reachable; an off-branch commit with a rewritten §8 validates clean | **repaired.** Ancestor-of-`HEAD` required (`LA-2`); §2 states the rule; fixtured with a real dangling commit |
| **f3** | *MATERIAL* — the `SDR-n` branch resolves a narrative mention in `HISTORY.md`, a file the path branch refuses by name | **repaired.** `_sdr_exists` resolves only `SURFACE-DECISION-RECORD.md`'s `**SDR-n**` rows; §5 states it |
| **f4** | *MATERIAL* — `routing_authority: " "` switches `LA-3b` off from inside the record | **repaired.** Empty-after-normalization is its own error; the fixture's mutation test caught its first expectation passing for the wrong reason |
| **f5** | *MATERIAL* — §2 obliges a trend-row disclosure §6's fixed table cannot carry and the generator cannot emit | **repaired as a semantic correction.** The obligation moved to the record and the generated report; argued in place in §2 and in the v2.3 delta |
| **f6** | *MATERIAL* — `--prior` still reads outside the repository and zeroes the New-findings column | **repaired.** Same containment as the record path, plus declared-identity equality on both paths |
| **m1** | *MINOR* — "not rendered at all" false of `--allow-invalid` | **repaired.** §5 scoped to the default invocation, naming the stamp |
| **m2** | *MINOR* — "a function of the rows and nothing else" false of E3/F2 | **repaired.** Scoped to the record's own content |
| **m3** | *MINOR* — the `NONE` trend cell names no limb; a fourth literal is unreachable rather than removed | **repaired.** `gate_result` is the one `NONE — <limbs>` string on every surface; the literal is gone |
| **m4** | *MINOR* — the v2.1 changelog entry's unscoped "stated nowhere else" | **repaired.** Annotated in place with the scoped form |
| **m5** | *MINOR* — §4's "any other owner deferral" contradicts "exactly one substitution"; two LA-12 branches unreachable, zero coverage | **repaired.** Prose aligned to the formula; the two branches removed with the construction argument in place, their unreachability independently verified by RD-62 |

**Repaired: 11. Open: 0. Declined: 0.** All repairs are this session's
judgement; the repaired bytes were re-dispatched for review in this round
(RD-65/RD-66) rather than left as the round-08g gap was.

## RD-62 — launch-gate schema, validator and renderer at v2.2

`VERDICT: REVISE` — 1 BLOCKING, 6 MATERIAL, 6 MINOR. Dispatched 2026-08-16
against the same frozen commit `918574c`, concurrently with RD-61 and with
no knowledge of it; fresh context; same model family. Raw bytes:
`RD-62-launch-machinery-v2.2-RAW.md`. Its f5 and RD-61's f1 are the same
defect, found independently — the second consecutive round in which the
two blind reviews converged on one hole.

RD-56's substance was verified closed (both BLOCKING repairs reproduced
and held; its 20-file warrant sweep re-run at 22 files), with the
deliberately-open f11 checked against its disclosed-limit statement.

| # | Finding | Disposition |
|---|---|---|
| **f1** | *BLOCKING* — `_cell`/`_quoted` neutralize `\n` but not `\r`; the RD-47 f2 forgery reproduces verbatim in a clean record's report | **repaired.** One vertical-whitespace class at every neutralizer; `_quoted` uses `splitlines()`; three `\r` forgery fixtures, verified to fail against the reverted code |
| **f2** | *MATERIAL* — `--prior` launders the New-findings column from anywhere on the filesystem | **repaired** with RD-61 f6 |
| **f3** | *MATERIAL* — the file read is never checked to be the declared `prior_record` identity | **repaired.** Loaded-file commit equality on both paths (`LA-15`), fixtured in a scratch repository |
| **f4** | *MATERIAL* — an escaping declared prior collapses to "declares no prior" | **repaired.** `Unknown`, never absence; fixture asserts both the error and the column |
| **f5** | *MATERIAL* — the schema is the one identity neither digest-bound nor commit-resolved | **repaired** — the same repair as RD-61 f1 |
| **f6** | *MATERIAL* — "record valid" and exit 0 for a record the tool just said is not fully validated | **repaired.** CLI prints NOT-fully-validated and exits 2; the renderer exits 2 after writing its UNVERIFIED-stamped report |
| **f7** | *MATERIAL* — 49 reversions, 7 undetected; the `fresh_context` limb of the blocking repair has no discriminating fixture | **repaired.** Fixtures for the five live gaps (fresh-context limb, `_is_ancestor` against an existing commit, `--prior` equality, E4 case-index run); the two dead branches are removed (LA-12) or kept with the reviewer's own dead-code argument beside them (LA-4's extra-row branch, whose fixture already says so) |
| **f8** | *MINOR* — the false-witness fixture is still green under a restored fail-open | **repaired.** Renamed to the property it tests, with the coverage note beside it |
| **f9** | *MINOR* — "one list, both branches" states a property the code does not have | **repaired.** The identifier branch is scoped to the owning record — stricter than any list — and the comment now says what is true |
| **f10** | *MINOR* — placeholder coverage 6 of 43; `"none"` is a lawful counterexample; `falsification_summary` unchecked | **repaired in the named fields.** `counterexample` and `falsification_summary` run the lexicon. Coverage of all 43 free-text sites is not widened wholesale — the lexicon is a substance check for fields a verdict rests on, not a censor; recorded as a disclosed scope |
| **f11** | *MINOR* — `^…$` under `re.search` admits trailing newlines | **repaired.** `fullmatch`, with the audit refusing unanchored patterns so the semantics cannot fork |
| **f12** | *MINOR* — the invisible-character repair is an enumeration of five code points | **repaired.** Stripped by Unicode category (`Cf`/`Cc`), fixtured with characters from both classes |
| **f13** | *MINOR* — `--check` misdiagnoses a git-less environment as an edit | **repaired.** That state reports `Unknown(git unavailable)` with its own exit status |

**Repaired: 13. Open: 0. Declined: 0.** One scope note (f10) is disclosed
above rather than silently narrowed. All repairs are this session's
judgement; the repaired bytes are under review as RD-65/RD-66.

The repair account is `round-2026-08h/LAUNCH-GATE-v2.3-SEMANTIC-DELTA.md`,
which also names what did not change (the schema is byte-identical) and
the six hand-run mutation tests.
