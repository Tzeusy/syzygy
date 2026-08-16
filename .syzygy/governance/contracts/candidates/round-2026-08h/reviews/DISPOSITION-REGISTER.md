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

## RD-61 / RD-62 — launch-gate v2.2 policy and machinery

Dispatched 2026-08-16 against the same frozen commit, concurrently and
mutually blind. **In flight at this register's last update** — their rows
are added when the raw files land.
