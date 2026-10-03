# Round 1 dispositions — D7 doctrine amendment packet

> **Candidate — binds nothing.** The drafter's record of how each round-1
> finding was handled. A disposition is not a confirmation: no reviewer has
> read the repaired bytes.

**Round:** 1, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md`, retained verbatim.
**Reviewed commit:** `fc46ec4169a19109631832f5f1783210955fea25`.
**Package digest reviewed:**
`de326819b0a76c3fc3b5996dde2ee3d4d2c3e86e3dc5a2235e733d4dbb7f42ea`.
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 17 — six revise-level (1–6) and eleven notes (7–17), per the
raw's own closing count.

**Stopping rule** (set in `REVIEW-BRIEF.md` before the round): one round;
each finding repaired once and recorded here; no round 2. The repaired
bytes go to the owner as **repaired and unconfirmed**.

Every repair below was re-derived from the source file, not copied from the
raw: line numbers, clause text and counts were re-read or re-run at
`66d42d09` (the doctrine and contract bytes are unchanged at the reviewed
commit).

| # | Level | Finding (short) | Repair |
|---|---|---|---|
| 1 | revise | The delta says Normative; packet §7 said "clarifies"; arm B records the class as existing meaning — incompatible | §7 rewritten: D7 is Normative; "inside VIS-4's bounds" answers only whether VIS-4's mechanism is needed. Arm B now says plainly that choosing it is the owner ruling the change Clarifying, contrary to the packet, and that the packet recommends against it. The delta's class paragraph says the same. |
| 2 | revise | Under "beyond", arm B is unavailable outright, not "available with an RFC" | Q1 and §7 now say: on "beyond", arm A needs an accepted adjudication RFC and a redraft, arm B is unavailable, arm C remains. §7 adds that VIS-4 defines its adjudication RFC for the spec-adoption gate, so whether one can serve a trigger question is [Unknown]. |
| 3 | revise | The text's heading stipulates the Q2 answer (the RC-7 F10 defect); Q2 came after Q1 | The heading is now reason-stating in the style the owner designated in ruling P-24: "delegates no decision, and is for that reason inside VIS-4's stated bounds rather than an exception to them". The bounds question is now Q1, answered before the arm (Q2); §1 opens with an "Order of rulings" note that the text is lawful only after Q1 "inside". |
| 4 | revise | RFC2 binds the page-open trigger, not only the hook; `reconciliation-chain.md` 155–157 missed | Verified at `66d42d09`: lines 155–157 read as the raw quotes. The architecture insertion now ends "relaxes no contract that requires a deliberately triggered pass"; §2 gains a Contracts row; §4 gains an RFC2 merge-chain row; §0 and §6 item 1 state that D7 alone does not make unprompted re-observation of a repository with merges lawful. The ledger gains the row and states its predicate is not complete. The class was not narrowed further: the RFC2 amendment is named as the separate step. |
| 5 | revise | Text narrower than §2's table: no file watcher, no reprioritize, no self-set trigger, notify undefined | Text now reads "A clock or watcher Syzygy owns is never a trigger: no timer, schedule, poller, file or event watcher, or wake Syzygy sets for itself" and "never notifies anyone, dispatches or reprioritizes work, adopts, or sets its own next trigger". §2's table was aligned to the text row by row. |
| 6 | revise | "a new identified evaluation" lets model output be held | Text now reads "a new identified evaluation of observed state, or data rebuildable from its inputs (VIS-6), and never model output". §2 lists model output as unlawful; §6 item 3 (the rehearsal) follows it. |
| 7 | note | The text bounds writes, egress, execution but not reads | "read" added to the text's path list and to §2's Paths row. |
| 8 | note | "Stage a draft" overstates P-71 Q3 arm (b)'s width | §3's row now says D7 holds the draft, which arm (b) did not, that this persistence is wider than arm (b), and that it rests on VIS-6's projection rule, not on P-71. |
| 9 | note | The "hold" row's precedent is nominal | §3's row now names VIS-6's projection rule as the footing and cites P-79 Q4 only for where such state lives. |
| 10 | note | §1.3 described D3 by rev1's parenthetical, not the designated wording | §1.3 now quotes the P-24 ruling's designation and describes the reason-stating wording in D3 §6. The composition conclusion is unchanged. |
| 11 | note | §7 attributed D3's reading to the D4 ruling | §7 now cites D3 lines 37–39 for the reading (re-read: line 38 "delegation of the always-human decision") and the D4 ruling for the mission ruling only. |
| 12 | note | Sweep gaps: a wrapped "not autonomous"; no "autonomous behavior" form; derived-reader sweep too narrow | Ledger §1a: wrap-tolerant re-run, 95 files and 348 occurrences, two wrap hits (`vision.md` 86–87, row added; one historical raw). §1b: `autonomous\s+behaviou?r` over 212 authority files, 10 hits, each listed and dispositioned, and the guard tied to that population in packet §4. §4: reader sweep widened to 417 files under `apps/`, `packages/`, `scripts/`, 11 readers, each classified. |
| 13 | note | The delta said VIS-4 was cited by the text when it was not | After repair 3 the text does cite VIS-4 (its stated bounds); the delta's Stable IDs line now lists VIS-4, VIS-5, VIS-6, SEC-2 and SEC-3, which is what the repaired text cites. |
| 14 | note | Departure from N14's "amend VIS-4" not disclosed | Packet §0 gains a "Departure from the pursuit's wording" paragraph with the reason. |
| 15 | note | The architecture text was "verbatim" yet "rewrapped on application" | §1.2 now gives the resulting paragraph as exact bytes (first five lines unchanged, sixth extended), and §9 applies "the exact bytes shown". Checked by script: the five lines equal the anchor's. |
| 16 | note | D3 is in the parent directory, not "this directory" | Corrected in the Identifier paragraph. |
| 17 | note | E3 is a governance gate, not a capability prerequisite; its rationale was asserted | E3 withdrawn in place, keeping its number, with the reason: a human opening a live view requests what it shows. Arm C's sentence about E3 was removed. |

**What was not changed.** The change class (Normative), the four-effect
class itself, the strict hook test (Q3), the entry criteria E1, E2, E4–E6,
and the decision to keep entry criteria off doctrine. No finding asked for
those to move.
