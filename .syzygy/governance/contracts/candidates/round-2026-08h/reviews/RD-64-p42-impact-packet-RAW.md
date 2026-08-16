# RD-64 — fresh-context owner-decision-packet review of `SHAPE-TO-SPEC-IMPACT-DECISION.md` (P-42)

| | |
|---|---|
| Review ID | RD-64 |
| Date | 2026-08-16 |
| Frozen commit | `918574c` |
| Subject | `.syzygy/governance/decisions/SHAPE-TO-SPEC-IMPACT-DECISION.md` |
| Subject sha256 | `fff2466f8453fffc3e3b10aedee3f4ada8a9795047bf14fdf8f1e8acf0381c19` — **verified at the frozen worktree before reading** |
| Reviewer context | **Fresh context.** No prior knowledge of this corpus; no other review dispatched today was seen or sought. |
| Model family | **Same model family as the corpus authors.** This review is therefore correlated evidence, not independent evidence, per the repository's own posture on self-review. |
| Stance | Simulated owner ruling on P-42 from the bounded packet alone, then verification against the records the packet cites. |

---

## Phase 1 — the fresh-reader test

*Written after reading only the packet, and before opening any other file. Reproduced verbatim below; nothing in this section was revised after Phase 2.*

### 1. What is the question the owner is being asked to decide?

Whether — and on what terms — to give an owner to the *detection* step of
shape-to-spec propagation, so that launch-gate item `E6` can be answered by
citation instead of being unanswerable.

The packet frames the substantive question as: *"When a shape changes — a
contract clause, an owner decision, a craft policy — what finds the
specifications that change with it?"* and then localises the gap precisely:
steps 3 and 4 of the propagation path already have owners (`VIS-2`,
`CC-REV-2`), but *"step 2, the reverse-reference sweep, is carried by nothing
citable."* The candidate that would close it is `CC-IMPACT-1…7`, which
*"binds nothing today."*

So the decision is: adopt the candidate craft policy (after review, or
without review), or decline to adopt it and record that decision, or defer.

### 2. What are the options, and what does each cost?

Four, as stated:

- **(a) Review, then act.** Commission a fresh-context review of the repaired
  `CC-SPEC` + `CC-IMPACT` bytes *"as one combined subject"*, disposition the
  findings, then perform `CONFIRM CRAFT AMENDMENT` over the reviewed digest.
  Cost: *"one fresh-context review over the combined `CC-SPEC` + `CC-IMPACT`
  subject, its disposition pass, then the act. The review is the cost; the act
  is minutes."*
- **(b) Act without the review.** Cost: *"minutes, and a policy in force that
  no independent reader has checked. The known-open findings below travel into
  force with it"* — those being `RD-51 f14` (no clause tests a specification
  for completeness against its capability), `RD-51 f15` (*"applicable"* is
  undefined, circular home for the reviewed-N/A rule), and the fixture's two
  known defects.
- **(c) Launch knowingly without it.** Record that the first specification may
  be authored with no owned propagation rule and that `E6` is `Not met` by
  decision. Cost: *"one recorded decision. `E6` is permanently `Not met` until
  someone reopens it, and every future administration records it."*
- **(d) Defer.** Cost: *"zero now; `E6` unanswerable at the formal
  administration, with no reason on record."*

Recommendation is **(a)**, explicitly marked `[Inferred]`.

### 3. Which digests/confirmations would change under each option?

The packet is unusually crisp here, and its claim is a *negative* one:
*"**No contract module and no wave manifest.** `CC-IMPACT-*` is craft policy,
not a contract wave: neither Wave A's nor Wave B's manifest digest moves under
any option, and neither confirmation is retired."*

What does move: *"the **policy file's own digest, computed at the act** (the
`CC-TEST-2` precedent). Under (a) that digest is the reviewed one; under (b)
it is today's."*

By implication — and the packet does not say this in so many words — under
**(c)** and **(d)** no digest binds at all, because no act is performed. I had
to infer that; it is the obvious reading, but it is inference.

### 4. What pre-work or review is still required before the owner may lawfully rule — and does the packet ask the owner to approve anything whose current review verdict is `REVISE` or that is unreviewed?

Pre-work required for **(a)**, in the packet's own order: commission one
fresh-context review of both files as a single subject *"given the artifacts,
their governing references and the acceptance criteria, and nothing else"*;
store raw output verbatim and disposition every finding `repaired` · `open` ·
`declined`; *"**freeze the bytes** and compute the digest"*; then perform the
act over that digest for both files. Plus the pre-act verification block
(`check_governance.py` and two `sha256sum`s).

On the second half of the question: **the packet discloses the unreviewed
status prominently and up front**, in a banner above the fold: *"**The subject
is unreviewed.** Its most recent repair has had no fresh-context review, and
this packet does not ask the owner to approve unrepaired or unreviewed bytes.
Read the options with that in front."* Option (b) is nevertheless *offered* —
but it is offered labelled, costed, and with the specific findings that would
travel with it enumerated, and it is explicitly not recommended, with a reason
grounded in the repository's own rule: *"a repair session cannot confirm its
own repairs, and the last hands on these clauses were the repair's."*

That is the correct handling. My one reservation as a fresh reader: the packet
never states **what verdict the prior review (`RD-51`) actually returned**. It
tells me two `RD-51` findings are open; it does not tell me whether `RD-51`
said `CONFIRM`, `REVISE`, or `EXCEPTIONS`. So I know the bytes are *unreviewed
since repair*, but I cannot tell from the packet whether the repair was
responding to a `REVISE` verdict or to advisory findings under a passing one.
That materially changes how much weight I put on (b) being unsafe.

### 5. What is the exact next transaction after a ruling?

Given clearly for two of the four options.

Under **(a)**: the four numbered steps above, terminating in *"perform
`CONFIRM CRAFT AMENDMENT` over that digest, for both files."* Under **(c)**:
*"one row in `SURFACE-DECISION-RECORD.md` stating that the first specification
may be authored with no owned propagation rule, and that `E6` is `Not met` by
decision."*

Under **(b)** the transaction is only implied — *"Perform the craft act over
the current bytes"* — with no statement of where it is recorded or whether the
same freeze/compute step applies. Under **(d)** there is by definition none.

There is also a hard coupling constraint stated before the steps: *"**Do not
rule `P-42` alone.** It is offered jointly with **`P-41`**"*, because
*"`CC-IMPACT-1`'s spec-level declaration is *generated* as the union of
`CC-SPEC-2`'s six fields — and adopting either without the other leaves a
dangling generation."*

### 6. Could you rule from this packet alone, without reading any review history? Where exactly did you get stuck or need outside knowledge?

**Mostly yes — I could choose between (a), (c) and (d) on what is here.** The
gap is named, the candidate is named, the evidence for the candidate is
concrete and quantified (*"a contract-only sweep would have missed **4 of 6**
affected requirements"*), the recommendation is marked `[Inferred]`, and the
honest posture (c) is described as lawful rather than buried. That is a
genuinely rulable packet.

Where I got stuck, in descending order of how much it bothered me:

1. **Is `E6` launch-blocking?** Option (c) — "launch knowingly without it" —
   is only *available* if the launch gate permits launch with an item `Not
   met`. The packet asserts (c) is *"a lawful and honest posture"* but never
   tells me whether the gate's own rules allow a `Not met` E6 to pass. If they
   do not, (c) collapses into (d) with extra paperwork. I would have to open
   the launch-gate instrument to know whether I am allowed to pick (c).
2. **`P-41` has no path.** I am told not to rule P-42 alone and that P-41 is
   *"the specification-acceptance policy"*, but P-41's own packet is not cited
   by path. To honour the coupling I must go find it.
3. **The prior verdict is missing** (see §4). "Unreviewed since repair" and
   "reviewed `REVISE`, repaired, not re-reviewed" are different risk profiles
   and the packet does not distinguish them.
4. **`CONFIRM CRAFT AMENDMENT` is used as a known ceremony phrase** with no
   pointer to where it is defined, who may utter it, or what its argument is.
   A fresh owner would need the process vocabulary from outside the packet.
5. **The `CC-TEST-2` precedent is asserted, not shown.** I am asked to accept
   that binding-the-file's-own-digest-at-the-act is established practice on the
   strength of a parenthetical.
6. **Option (b) lacks a next transaction** (see §5).

None of these required me to read *review history* — which is the thing the
packet promises not to reproduce, and does not reproduce. They are pointer
gaps, not narrative gaps.

---

*Phase 2 begins below. Everything above was written before any other file was opened.*

## Phase 2 — verification against the cited records

Every row below was checked in the frozen worktree at `918574c`. "Packet
claim" quotes the packet; "Record" quotes the file the packet points at.

| # | Packet claim | Record checked | Result |
|---|---|---|---|
| 1 | *"`CC-IMPACT-1…7`"* exist as a clause set | `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` | **Confirmed** `[Observed]` — seven defined clauses, `CC-IMPACT-1` … `CC-IMPACT-7`, each a bolded normative clause. |
| 2 | *"`CC-IMPACT-2`, stated as a **set identity** with `CC-SPEC-2`'s six warrant classes rather than a second enumeration that could drift"* | `CC-IMPACT-2` | **Confirmed** `[Observed]` — *"**The identities that can trigger a sweep are exactly the identities that can warrant a requirement** — CC-SPEC-2's six classes, and no others"*, plus *"Stating the trigger set as an *identity* rather than as a second enumeration is deliberate: two lists drift, and the drift is silent."* |
| 3 | *"`CC-IMPACT-7`, naming its fixture by path and sha256"* | `CC-IMPACT-7` | **Confirmed** `[Observed]` — names `../round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md`, `sha256 685a71f7a52652a314f144ba1599982812921ede88220e69a0d5d327272ed4e0`, and a separate answer key. |
| 4 | *"`CC-IMPACT-1`'s spec-level declaration is *generated* as the union of `CC-SPEC-2`'s six fields"* | `CC-IMPACT-1` rule 1; `CC-SPEC-2` | **Confirmed** `[Observed]` — *"The specification-level declaration is the union of its requirements' CC-SPEC-2 declarations, generated — never hand-authored."* `CC-SPEC-2`'s closed set of six (`doctrine[] contracts[] policies[] decisions[] topology[] parent_requirements[]`) matches `CC-IMPACT-1`'s block field-for-field. |
| 5 | *"`CC-IMPACT-*` is **candidate craft policy**. It binds nothing today."* | policy §"Acceptance" | **Confirmed** `[Observed]` — *"Nothing in it binds today, and no verdict of the launch gate may cite it as in force until that act is performed."* |
| 6 | *"a candidate workflow whose own disclaimer says its sweeps *"do not exist as checks yet"*"* | `policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md:175` | **Confirmed** `[Observed]` — the phrase is present verbatim in that file's §"What this workflow does not do". |
| 7 | *"Launch-gate **E6** asks exactly this"* | `launch-gate-pre-specifications.md:408` | **Confirmed** `[Observed]` — E6 is *"Is there a defined propagation path for a shape change *after* specs exist — how affected specs are detected, who amends them, and how the interim disagreement is surfaced rather than hidden?"* The packet's framing of detection as the open half is faithful. |
| 8 | *"the graded blind run `RD-59`"* was *"**administered**, not merely specified, and it **passed**"* | `round-2026-08g/reviews/RD-59-blind-propagation-RAW.md`; `DISPOSITION-REGISTER.md` §RD-59 | **Confirmed** `[Observed]` — RD-59 banner: *"**Result** \| **PASS** on all three of the answer key's criteria."* Register: *"**Result: PASS**, against the answer key's three criteria"*, with all three graded `met`. |
| 9 | *"a contract-only sweep would have missed **4 of 6** affected requirements"* | `DISPOSITION-REGISTER.md` §RD-59 | **Confirmed** `[Observed]` — *"The sweep found **4 of its 6** affected requirements through `policies[]` and `decisions[]`, not through `contracts[]` … a 67 % miss."* The answer key states the same at its line 81. |
| 10 | *"finding two defects in the fixture itself"*, being *"one warrant class entirely unexercised; the clauses it exercises are not stated in it"* | `DISPOSITION-REGISTER.md` §"Two defects the run found in the fixture" | **Confirmed** `[Observed]` — (1) *"The fixture says the declaration has "six fields" and no requirement carries `topology[]`"*; (2) *"The fixture asks for a CC-IMPACT-2 sweep and CC-IMPACT-3 output without stating either clause."* Both descriptions are accurate. |
| 11 | *"It is **superseded by a fixture 3, never edited** — its digest binds a completed run."* | register; `FINAL-CAPABILITY-1-READINESS-REPORT.md:33`; filesystem sweep | **Confirmed with a caveat** `[Observed]` — the register says *"superseded by a fixture 3, never edited — **filed as work, not fixed here**"*. **No shape-to-spec fixture 3 exists** (`find . -iname '*FIXTURE*'` returns the round-08e fixture and fixture 2 only). The packet drops the disambiguating clause. See finding **m2**. |
| 12 | *"`RD-51 f14` — no clause tests a specification for **completeness** against its capability"* | `DISPOSITION-REGISTER.md` f14 row | **Confirmed** `[Observed]` — *"**14** \| *material* … **open, and deliberately.** No clause tests a specification for **completeness against its capability**."* |
| 13 | *"`RD-51 f15` — *"applicable"* is undefined, and the reviewed-N/A rule has a circular home"*, listed under *"Known open findings"* | register tally | **Partly contradicted** `[Observed]` — the register grades f15 **"repaired in part"** and tallies *"Repaired: 15. Repaired in part: 4 (f13, f15, f19 …). **Open: 1.** Declined: 0."* Only f14 is Open. See finding **m1**. |
| 14 | *"**No contract module and no wave manifest.** … neither Wave A's nor Wave B's manifest digest moves under any option, and neither confirmation is retired."* | `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` | **Confirmed** `[Observed]` — `grep` for `CC-IMPACT`/`CC-SPEC` over the acceptance record returns **zero** hits; the craft cluster is act 2 (`CC-TEST-2`), structurally separate from the contract-wave acts. |
| 15 | *"the **policy file's own digest, computed at the act** (the `CC-TEST-2` precedent)"* | acceptance record act 2; `craft-and-care/INSTALL-RECORD.md` | **Confirmed** `[Observed]` — act 2 is `CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090…`, a file-digest-at-act phrase, re-quoted twice as the bytes moved. The precedent is real and correctly characterised. |
| 16 | *"one row in `SURFACE-DECISION-RECORD.md`"* (option (c)'s transaction) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` | **Confirmed** `[Observed]` — the file exists at the stated path. |
| 17 | The verification block: `check_governance.py` and two `sha256sum` targets | `scripts/check_governance.py`; both policy-candidate paths | **Confirmed** `[Observed]` — script and both files exist at the quoted paths; the command is runnable from the repository root as stated. |
| 18 | *"Offered jointly with **`P-41`** … adopting either without the other leaves a dangling generation."* | policy §"Acceptance"; `PENDING-OWNER-DECISIONS.md` P-41/P-42; `decisions/README.md:67` | **Confirmed** `[Observed]` — the policy itself says accepting one without the other *"reintroduces the two blocking defects this amendment removed"*; both queue rows carry *"Offered jointly"*; the README packet table row reads *"offered jointly with P-41"*. |
| 19 | Provenance: *"`round-2026-08g/reviews/RD-51-*`"* | filesystem | **Contradicted** `[Observed]` — RD-51 is at `round-2026-08**f**/reviews/RD-51-spec-acceptance-and-impact-RAW.md`. `ls round-2026-08g/reviews/` contains no RD-51. See finding **M3**. |
| 20 | *"**The subject is unreviewed.** Its most recent repair has had no fresh-context review"* | register; `PROJECT-STATUS.md:59` | **Confirmed** `[Observed]` — register: *"the review has not been dispatched and **the bytes are not frozen**"*; status: *"The repaired bytes are **unreviewed**."* |
| 21 | Option (a) step 1: *"commission one fresh-context review of both files as a single subject"* — presented as immediately actionable | `DISPOSITION-REGISTER.md`; `PENDING-OWNER-DECISIONS.md` P-41; `CC-SPEC-1` | **Contradicted** `[Observed]` — *"Charter §9.8 sequences one combined fresh-context review **after P-40 is ruled**; P-40 is not ruled, so the review has not been dispatched."* `CC-SPEC-1`: *"**This clause may not be frozen before P-40 is ruled.**"* P-41 row: *"CC-SPEC-1 may not be frozen before **P-40** is ruled."* The packet contains **zero** occurrences of "P-40". See finding **B1**. |
| 22 | Option (c): *"Launch knowingly without it … `E6` is `Not met` by decision"*, described as *"a lawful and honest posture"* whose cost is *"one recorded decision"* | `launch-gate-pre-specifications.md` §4 | **Contradicted** `[Observed]` — READY requires *"every E question `Met` for the named launch target"*; READY-WITH-DEFERRALS repeats *"every E question `Met`"*; and §4 states outright: *"**The E, A–D, F1, F3 and F4 conjuncts are never deferrable**."* See finding **B2**. |
| 23 | Prior review verdict | `RD-51-…-RAW.md:21`; `SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md:414-416`; `PROJECT-STATUS.md:58` | **Omitted** `[Observed]` — RD-51's last line is `VERDICT: REVISE`; the delta records *"verdict `REVISE`"*; status records *"**Amended 2026-08-13** against RD-51 (`REVISE`)"*. The packet contains **zero** occurrences of "REVISE". See finding **M1**. |
| 24 | Known-open list completeness | policy §"What this rule set does not do"; register | **Incomplete** `[Observed]` — the subject policy declares of `"consumes its vocabulary"`: *"`[Unknown]` — the term is undefined, and its undefinedness decides real cases … the term itself remains an open finding against this file (RD-51's G section), not a closed one."* The packet contains **zero** occurrences of "vocabulary". See finding **M2**. |
| 25 | *"**No history chain** — the reviews are named once as provenance, not narrated."* | the packet, whole | **Confirmed** `[Observed]` — 1,042 words. RD-51, RD-59 and E6 are each named as provenance; no repair chain, no round-by-round narration, no verdict sequence is reproduced. This criterion is met cleanly. |
| 26 | Seven-part shape and `[Inferred]` marking | the packet, whole | **Confirmed** `[Observed]` — headed sections: Question, Current authority, Options, Recommended option, Costs, Which digest would change, Exact next transaction (plus Earliest required gate). *"`[Inferred]` **(a)**."* |

---

## Findings

| # | Severity | Finding |
|---|---|---|
| **B1** | **BLOCKING** | **The "exact next transaction" is not performable, and the prerequisite that blocks it is never named.** Option (a) instructs, in order: *"commission one fresh-context review of both files as a single subject"* … *"**freeze the bytes** and compute the digest"* … *"perform `CONFIRM CRAFT AMENDMENT` over that digest, **for both files**."* But the joint subject includes `CC-SPEC-1`, whose own text reads *"**This clause may not be frozen before P-40 is ruled.**"* The disposition register the packet's evidence rests on says *"Charter §9.8 sequences one combined fresh-context review **after P-40 is ruled**; P-40 is not ruled, so the review has not been dispatched and **the bytes are not frozen**."* P-41's queue row repeats it: *"CC-SPEC-1 may not be frozen before **P-40** is ruled."* The packet mentions P-40 **zero times**. An owner who rules (a) from this packet alone commissions a review the charter sequences later, and then freezes a clause its own policy forbids freezing. The packet simultaneously insists *"**Do not rule `P-42` alone**"* because of the P-41 coupling — while omitting the prerequisite that coupling drags in. `[Observed]` |
| **B2** | **BLOCKING** | **Option (c) cannot do what it is labelled as doing, and is priced as though it can.** It is headed *"Launch knowingly without it"* and costed at *"one recorded decision"*, with the consequence given as *"`E6` is permanently `Not met` until someone reopens it, and every future administration records it."* The launch instrument's §4 formula requires *"every E question `Met` for the named launch target"* for `READY FOR <LAUNCH_TARGET>`, repeats *"every E question `Met`"* inside `READY-WITH-DEFERRALS`, and states flatly: *"**The E, A–D, F1, F3 and F4 conjuncts are never deferrable** — each carries this section's own rationale for blocking."* Only F2 is owner-deferrable. So a recorded ruling that E6 is `Not met` by decision does not license a launch; it guarantees that **no** pass verdict — plain or with deferrals — can be returned. The packet's own recommendation section reinforces the wrong reading: *"(c) is a lawful and honest posture … and it is the right choice if the owner judges the review cost not worth paying before launch."* The honesty half is true; the "before launch" half is not available. This misstates the option set for the decision being ruled. `[Observed]` |
| **M1** | MATERIAL | **The prior verdict word `REVISE` is never stated.** The packet says *"The subject is unreviewed"* and names two findings, which is real disclosure — but a fresh owner cannot tell whether the repair answered advisory findings or a failing verdict. RD-51's raw bytes end `VERDICT: REVISE`; the semantic delta records *"verdict `REVISE`"*; `PROJECT-STATUS.md` records *"against RD-51 (`REVISE`)"*. The packet contains the word zero times, and never says RD-51 raised 20 findings of which 4 were blocking. Under the repository's own rule that *"verdict words are copied exactly"*, a packet that withholds the verdict word understates the risk attached to option (b) — which is precisely the option the owner is being asked to weigh. `[Observed]` |
| **M2** | MATERIAL | **The known-open list omits the open finding the subject policy declares against itself.** The packet's *"Known open findings that travel with (b)"* lists f14, f15 and the fixture defects. It omits the undefined term `"consumes its vocabulary"`, which the subject policy itself flags: *"`[Unknown]` — the term is undefined, and its undefinedness decides real cases … the term itself remains an open finding against this file (RD-51's G section), not a closed one."* This is not a peripheral gap: the phrase sits inside `CC-IMPACT-2`'s operative trigger — *"whose CC-IMPACT-1 declarations name the changed identity, **or whose requirements consume its vocabulary**"* — so an undefined term governs one of the two limbs of the sweep the whole policy exists to mandate. A list headed "known open findings" that omits the one the artifact declares on its own face is an incomplete denominator. `[Observed]` |
| **M3** | MATERIAL | **The provenance pointer to RD-51 is wrong.** The packet cites *"`round-2026-08g/reviews/RD-51-*`"*. RD-51 lives at `round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`; `round-2026-08g/reviews/` contains RD-54, RD-55, RD-56, RD-59, RD-60 and the disposition register, and no RD-51. Both the subject policy and the semantic delta cite the round-08f path correctly, so the packet is the only artifact carrying the wrong round. Since the packet's entire justification for not narrating the history is that *"the reviews are named once as provenance"*, the one naming needs to resolve. `[Observed]` |
| **m1** | MINOR | **f15 is listed as "open" where the register grades it "repaired in part".** The register's tally is explicit: *"Repaired: 15. Repaired in part: 4 (f13, f15, f19, and f7's sibling concern about undefined vocabulary consumption). **Open: 1.** Declined: 0."* Only f14 is Open. The packet's error is in the disclosure-safe direction — it over-reports risk rather than under-reporting it — but a derived status quoted outside its owning artifact is exactly what goes stale silently. `[Observed]` |
| **m2** | MINOR | **"It is superseded by a fixture 3" reads as accomplished; no fixture 3 exists.** The register's sentence is *"superseded by a fixture 3, never edited — **filed as work, not fixed here**"*, and the readiness report says *"filed **for** a fixture 3, never an edit"*. The packet keeps the present-tense clause and drops the disambiguator, so a fresh reader may conclude the two fixture defects have been superseded away. A filesystem sweep finds only the round-08e predecessor and fixture 2. `[Observed]` |
| **m3** | MINOR | **Option (b) has no exact next transaction.** (a) gets four ordered steps and (c) gets a named file and row; (b) gets only *"Perform the craft act over the current bytes"* — no statement of whether the freeze-and-compute step still applies, and no record named. Given (b) is the option the packet works hardest to warn against, leaving its mechanics unstated makes the warning harder to act on, not easier. `[Observed]` |
| **m4** | MINOR | **`CONFIRM CRAFT AMENDMENT` is used as a known phrase with no pointer, and no act row for P-42 exists yet.** The ceremony is real — acceptance-record act 2 is `CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090…` — but `PROCESS-GLOSSARY.md` does not define it and the packet cites nothing for it. The acceptance record's thirteen acts contain no `CC-IMPACT` or `CC-SPEC` row, so ruling (a) also requires minting a new act and phrase. P-41's queue row states this for its own act (*"phrase minted at the offering"*); this packet does not. `[Observed]` |
| **m5** | MINOR | **Digest consequences under (c) and (d) are left to inference.** The section is precise about (a) and (b) and silent on the other two. The obvious reading — no act, so no digest binds — is almost certainly right, but the packet's own discipline is that absence renders Unknown rather than assumed. `[Inferred]` |
| **m6** | MINOR | **P-44 is not mentioned.** `CC-IMPACT-6` names it — *"That amendment is offered separately … queued as **P-44**"* — and its queue row records that P-44's *"review is part of the combined CC-SPEC/CC-IMPACT review"*. Adopting `CC-IMPACT-6` changes nothing about lag lawfulness (it explicitly *"creates no alternative"*), so the omission is defensible; but an owner ruling P-42 is ruling on a clause that hard-points at an unruled sibling decision, and the packet's coupling section names only P-41. `[Observed]` |

### What the packet does well, recorded so the verdict is not read as a rejection of the whole

`[Observed]` The seven-part shape is complete and the sections are correctly
populated. The recommendation is marked `[Inferred]` exactly as required. The
no-history-chain constraint is met cleanly — 1,042 words, reviews named once,
no narration. The unreviewed status is disclosed **above the fold**, in a
banner, in bold, with the instruction *"Read the options with that in
front"* — which is stronger handling than the acceptance criteria demand. The
trade-offs are genuinely preserved rather than smoothed: option (b) is
offered with its cost stated as *"a policy in force that no independent
reader has checked"* and the findings that travel with it enumerated, and (c)
is described as *"lawful and honest"* rather than buried. The self-critical
reasoning is real — *"this repository's own rule is that a repair session
cannot confirm its own repairs, and the last hands on these clauses were the
repair's."* Every substantive evidentiary claim I could check about the
candidate itself (rows 1–5, 8–10, 14, 15, 18) verified **exact**, including
the two quantitative ones. The defects below are pointer and scope defects,
not fabrication.

---

## Confirmation — every file opened

Phase 1 (before writing the Phase 1 answers): **one file.**

1. `.syzygy/governance/decisions/SHAPE-TO-SPEC-IMPACT-DECISION.md` — the subject, digest-verified at `fff2466f…0381c19` before reading.

Phase 2:

2. `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` (full)
3. `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` (CC-SPEC-1, CC-SPEC-2 regions)
4. `.syzygy/governance/contracts/candidates/round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md` (verdict line only)
5. `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-59-blind-propagation-RAW.md` (head and tail)
6. `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/DISPOSITION-REGISTER.md` (RD-51 tally and RD-59 sections)
7. `.syzygy/governance/contracts/candidates/round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md` (grep hits; warrant section)
8. `.syzygy/governance/contracts/candidates/round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md` (grep hits)
9. `.syzygy/governance/contracts/candidates/round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` (supersession line)
10. `.syzygy/governance/contracts/candidates/round-2026-08g/FINAL-CAPABILITY-1-READINESS-REPORT.md` (fixture-3 line)
11. `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` (P-40, P-41, P-42, P-43, P-44 rows)
12. `.syzygy/governance/decisions/README.md` (packet table)
13. `launch-gate-pre-specifications.md` (E6; §4 verdict vocabulary, READY and READY-WITH-DEFERRALS formulas, qualifications)
14. `PROCESS-GLOSSARY.md` (grep for the craft-amendment ceremony — no definition present)
15. `PROJECT-STATUS.md` (CC-SPEC / CC-IMPACT candidate rows)
16. `.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (act rows; CC-IMPACT/CC-SPEC sweep)
17. `.syzygy/governance/policies/craft-and-care/INSTALL-RECORD.md` (CC-TEST-2 precedent)
18. `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` (the disclaimer line)
19. `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md` (existence only)
20. `scripts/check_governance.py` (existence only)

I did not open, and was not shown, any other review dispatched on 2026-08-16.
No `.syzygy/governance/decisions/launch-gate/HISTORY.md`, no `_bootstrap/`
material, and no `PROCESS-LESSONS.md` were consulted. Nothing in the frozen
worktree was edited; all commands were read-only (`sha256sum`, `grep`, `find`,
`ls`, `sed -n`, `wc`).

**Method limits.** `[Unknown]` — I verified the packet's claims against the
records it names and the launch instrument. I did **not** independently
re-administer the propagation fixture, re-derive any digest other than the
subject's, or run `check_governance.py`. My reading of the §4 formula is a
reading of the instrument's stated text; I did not run the validator to
confirm the implemented predicate agrees with it. Same model family as the
corpus authors — this review is correlated evidence, not independent
evidence.

---

## Acceptance criteria, judged

| Criterion | Verdict |
|---|---|
| States the question | **Met** — *"When a **shape** changes … what finds the specifications that change with it?"* |
| States current authority | **Met** — a table naming the candidate, the trigger set, the blind exercise, what already has an owner, the joint offer and the provenance |
| 2–4 options | **Met** — four |
| Recommended option marked `[Inferred]` | **Met** — *"`[Inferred]` **(a)**."* |
| States costs | **Met in form, defective in substance** — (c)'s cost omits that it forecloses every pass verdict (**B2**) |
| States digest consequences | **Met** — and verified accurate; (c)/(d) left implicit (**m5**) |
| States pre-work required | **NOT MET** — the P-40 prerequisite that gates the whole (a) sequence is absent (**B1**) |
| States review still required | **Met** — the unreviewed status is disclosed in a banner, though without the verdict word (**M1**) |
| States the exact next transaction | **NOT MET** — (a)'s is unperformable as written (**B1**); (b)'s is absent (**m3**) |
| Does NOT reproduce the complete review history | **Met** — cleanly |
| Does not ask approval of unrepaired `REVISE` subjects without saying so | **Partially met** — it says "unreviewed" and names open findings, and explicitly disclaims asking; but it never states the verdict was `REVISE`, and its open list is incomplete (**M1**, **M2**) |
| Comprehensible from the packet alone | **NOT MET** — an owner ruling from this packet alone cannot see that (a) is gated on P-40, or that (c) forecloses the gate |

---

**Findings: 2 BLOCKING, 3 MATERIAL, 6 MINOR.**

The packet is well-built in shape, honest in posture, and accurate in every
claim it makes about the candidate itself. It fails on what it leaves out:
the sequencing prerequisite that makes its recommended transaction
unperformable today, and the gate rule that makes its fallback option
something other than what its label promises. Both are omissions an owner
would discover only after ruling.

VERDICT: REVISE
