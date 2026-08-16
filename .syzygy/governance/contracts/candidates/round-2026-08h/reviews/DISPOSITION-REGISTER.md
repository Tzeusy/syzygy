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

## RD-65 — launch-gate policy semantics at v2.3

`VERDICT: REVISE` — 0 BLOCKING, 3 MATERIAL, 2 MINOR. Dispatched 2026-08-16
against frozen commit `494acab` (subject sha256 `3e65aaa3…`, all four
digests verified), concurrently with RD-66 and mutually blind; fresh
context; same model family as the corpus authors, so it supports repair
and is not the formal launch administration. Raw bytes:
`RD-65-launch-policy-v2.3-RAW.md`.

The commissioned answers first: the v2.2→v2.3 differential found **nothing
weakened** (§1, §3, §6, §7, §8 byte-identical by span digest; a 31-case
differential battery found no record that fails under v2.2 and passes under
v2.3, and one that becomes stricter); **six of RD-61's eleven findings are
repaired outright** (f2, f3, f4, f6, m1, m4), the five hardest verified by
rebuilding each attack and watching it fail. The new findings are that
three clauses v2.3 *newly wrote* make false claims about the instrument
itself — the same defect class this round exists to close.

> **Dispositioned `repaired (v2.4)` after the owner ruled arm (c).** These
> were first recorded `open` (the fourth `REVISE` was the owner's to weigh,
> per arm (c), not this session's to absorb). On 2026-08-16 the owner ruled
> **arm (c)** — a structural v2.4 repair — so the findings are now repaired
> in v2.4, in this session's judgement and **not confirmed**: RD-67/RD-68
> re-review the v2.4 bytes. The account is
> `round-2026-08h/LAUNCH-GATE-v2.4-SEMANTIC-DELTA.md`.

| # | Finding | Disposition |
|---|---|---|
| **1** | *MATERIAL* — the RD-61 f5 repair relocated the same-family obligation onto the generated report and justified it with *"the trend log's family reading runs through the reports its rows link"*; §6 is byte-identical, its nine columns link nothing, so the trend log carries no family signal at all | **repaired (v2.4)** — add a `Report`/`Same family` column to §6 and `trend_row()` so the asserted link exists, or narrow §2's parenthetical to claim only that the disclosure lives in the record and the report and *not* the trend log |
| **2** | *MATERIAL* — §4's replacement for RD-61 m2 asserts the row/formula outcome is *"never of the environment"*; one byte-identical record yields `NOT READY` with git and `READY-WITH-DEFERRALS` without it, because an uncheckable `SDR-n` warrant is added to `resolved_deferrals` anyway — permissive, against VIS-2. Eligibility contains it (no formal `READY FOR` reachable this way) | **repaired (v2.4)** — treat an uncheckable citation as unresolved (do not add to `resolved_deferrals` on the git-unavailable branch), or delete the *"and never of the environment"* clause |
| **3** | *MATERIAL* — the RD-61 f1 repair bound the schema to `HEAD` while the instrument and every other identity input stay bound to the record's named commit; v2.3's own new ancestry rule guarantees `HEAD` is the later of the two, so a **committed** enum widening at `HEAD` produces an eligible record carrying `Met (with caveats)` and a `READY FOR` gate result at any ancestor commit. Narrower than the working-tree hole it replaced, and the precondition is now itself an auditable governance violation | **repaired (v2.4)** — read the schema at `rec["repository_commit"]` as the instrument is read, keeping the `HEAD`-drift check as a separate warning; or carry a `schema_sha256` field so the binding is recorded rather than recomputed |
| **4** | *MINOR* — §4 says *"any other owner deferral"* is an `LA-11` error; for F5/F6 (the 2 of 39 roster rows that are neither F2 nor `NEVER_DEFERRABLE`) the check that actually fires is `LA-12`. Outcome claim is correct; only the identifier is wrong | **repaired (v2.4)** — say `LA-12`, or "a validation error" without naming a check |
| **5** | *MINOR* — §4 line 529 still says an ineligible administration deposits `NONE — not eligible`; the RD-61 m3 repair changed the emitted string to `NONE — \`formal: false\`; …`, so the words *"not eligible"* are gone and §4 specifies the column twice, contradictorily | **repaired (v2.4)** — restate line 529 as "deposits the gate result — `NONE` followed by the limbs it failed" |

**Repaired (v2.4): 5. Open: 0. Declined: 0.** All repairs are this session's
judgement and are not confirmed — RD-67 re-reviews the v2.4 bytes.

## RD-66 — launch-gate schema, validator and renderer at v2.3

`VERDICT: REVISE` — 1 BLOCKING, 3 MATERIAL, 2 MINOR. Dispatched 2026-08-16
against the same frozen commit `494acab`, concurrently with RD-65 and with
no knowledge of it; fresh context; same model family. Raw bytes:
`RD-66-launch-machinery-v2.3-RAW.md`.

The commissioned answers first: **8 of RD-62's 13 findings cleanly
repaired** (f2, f4, f5, f6, f7, f8, f9, f11, f13), each verified to fail
when its repair is reverted; 4 partially repaired (f1, f3, f10, f12); a
16-reversion battery caught 14, and the 2 undetected were verified as
non-defects (one redundant branch, one with no witness at this commit)
rather than assumed. Selftests confirmed at **119** and **34**, zero
failing, no skips. The three security-relevant reversions the commission
named (Cf/Cc strip, LA-2 ancestry, schema-from-committed-bytes) each
demonstrably caught. The new findings are that the *class property* v2.3
claims for its sanitizers and lexicons is still enumerated, not structural
— "the third consecutive pass to do exactly that on exactly this
mechanism" (RD-56 f2 → RD-62 f1 → v2.3).

> **Dispositioned `repaired (v2.4)` after the owner ruled arm (c)**, as with
> RD-65. RD-66's finding 1 is BLOCKING and is the RD-47 f2 / RD-56 f2 /
> RD-62 f1 forgery at an unnamed site; the v2.4 repair closes it *and* the
> class, by making the renderer's forgery sweep mechanical (every string
> leaf), so the next unnamed site fails the suite rather than the next
> review. Repairs are this session's judgement and are not confirmed.

| # | Finding | Disposition |
|---|---|---|
| **1** | *BLOCKING* — `_new_findings_cell` interpolates `prior_record.path` with no sanitizer; a record that validates with **zero errors, exit 0, no `--allow-invalid`** renders a document-level forged `GATE VERDICT: READY FOR …` and a second `## Computed figures` section above the real ones (confirmed under `pandoc -f gfm`). The RD-47 f2 forgery at the one free-text site none of the 34 renderer fixtures cover | **repaired (v2.4)** — `_new_findings_cell` returns `_inline(p)`. **Durable fix (root cause of four findings): a fixture that drives the forgery through *every* schema-declared string field mechanically, and an assertion over the sanitizer-coverage sweep itself — so the next unnamed site fails the suite, not the next review** |
| **2** | *MATERIAL* — the Cf/Cc category strip excludes `Mn`; `U+034F` (the exact code point and the exact `("Cf","Mn")` fix RD-62 f12 handed over — the repair substituted `Cc` for `Mn`) defeats the placeholder lexicon, converting a wholly unfalsified record (no falsification attempt, empty G1 critic answer, empty falsification summary) into an **eligible `READY FOR …`** with zero errors | **repaired (v2.4)** — strip `Mn` as well as `Cf`/`Cc` (RD-62's original hand-over was `("Cf","Mn")`; the correct set is at least `Cf`, `Cc`, `Mn`), and correct the docstring's false completeness claim |
| **3** | *MATERIAL* — `instrument.path` is chosen by the untrusted record, so the entire §8 binding (launch target, waves, E4 cases, routing authority) anchors to a record-selected path; a decoy instrument at a second repository path yields an eligible `READY FOR <attacker target>`. Latent, not live at `494acab` (1 of 451 `.md` files parses), but a stale in-tree copy of the instrument would bind superseded parameters silently | **repaired (v2.4)** — `INSTRUMENT_NAME` as a module constant beside `SCHEMA_NAME`, with `instrument.path` checked equal, or a schema `const` |
| **4** | *MATERIAL* — the prior record is the one cited path resolved against the filesystem, not the commit; an untracked, never-committed two-key file inside the repository zeroes §6's New-findings column (3→0) with zero errors, falsifying the trend log F1 rests on. Verdict unchanged, so MATERIAL not BLOCKING | **repaired (v2.4)** — read the prior through `_git_show(commit_or_HEAD, rel)` as every other cited path is read, so an uncommitted prior is `Unknown`, not authoritative |
| **5** | *MINOR* — `_unrenderable` interpolates `Path(record_path).name` raw; a record file named with newlines, plus `--allow-invalid`, puts a document-level `GATE VERDICT: READY FOR everything` in the report, exit 0 | **repaired (v2.4)** — `_inline(Path(record_path).name)` at renderer:123 |
| **6** | *MINOR* — `render … --allow-invalid` on a record with N validation errors exits 0; RD-62 f6's "the return code is a surface too" was applied to the validator and the git-unavailable render, not this sibling | **repaired (v2.4)** — non-zero exit on the `--allow-invalid` write path when the record did not validate |

**Repaired (v2.4): 6. Open: 0. Declined: 0.** All repairs are this session's
judgement and are not confirmed — RD-68 re-reviews the v2.4 bytes.

## Round note — the fourth `REVISE`, the owner's arm (c), and the v2.4 repair

The v2.3 review pair (RD-65/RD-66) returned `REVISE` and `REVISE`. Counting
the pairs run against v2.0 (RD-47/RD-48), v2.1 (RD-55/RD-56), v2.2
(RD-61/RD-62) and now v2.3, that is **eight fresh-context reviews and eight
`REVISE` verdicts across four versions** — the fourth consecutive `REVISE`
pair.

Two facts make this round different from "another narrower round":

1. **RD-66 finding 1 is BLOCKING and is the same forgery class** the tool
   has closed twice before (RD-47 f2 → RD-56 f2 → RD-62 f1), reproduced at
   a site no prior review named. RD-66 diagnoses the mechanism directly:
   each pass repairs the *instances* its reviewers named and restates the
   result as a *class property*, so the next review finds the class at a
   new address. RD-65 finding 3 is the same shape — RD-61 f1's eligible
   `READY FOR` outcome surviving at the schema's new `HEAD` binding.
2. The P-34 packet's arm (c) anticipated exactly this: *"If it returns
   `REVISE` a fourth time, that is itself the answer to whether this
   instrument converges, and it should be weighed against arm (a) rather
   than absorbed as another round."*

This session therefore did **not** repair unilaterally. It recorded the
findings `open`, updated the P-34 packet to make the fourth-`REVISE` fork
legible, and put the choice — (a) approve v2.3 as-read, (c) authorize a
structural v2.4, (d) decline — to the owner under VIS-4.

**The owner ruled arm (c) on 2026-08-16.** v2.4 is that structural repair.
The eleven findings are now `repaired (v2.4)` above — this session's
judgement, unconfirmed — and the fix is aimed at the class, not only the
instances: the renderer's forgery suite now walks **every string leaf** of a
populated record (both `\n` and `\r` spellings), so the next unnamed field
fails the suite rather than the next review. The account is
`round-2026-08h/LAUNCH-GATE-v2.4-SEMANTIC-DELTA.md`; the v2.4 bytes go back
under fresh review as **RD-67** (policy) and **RD-68** (machinery). Tracked
as `syzygy-6j8`, which stays open until that pair reports and the owner
rules P-34's approve/decline.
