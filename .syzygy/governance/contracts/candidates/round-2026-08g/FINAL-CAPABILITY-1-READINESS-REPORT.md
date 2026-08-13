# Capability 1 — final readiness, round-2026-08g

> **Supersedes `round-2026-08f/FINAL-CAPABILITY-1-READINESS-REPORT.md`**, which
> is banner-marked historical from this date. This report grades no artifact's
> content; it states, conjunct by conjunct, what the readiness standard asks
> and what is true. It performs no act and rules no queue row.

## No.

Syzygy is **not** ready to author Capability 1 in OpenSpec, and the answer is
not close. **Thirteen conjuncts; one is satisfied.** The other twelve are a
conjunction, so twelve `No` and one `Yes` is the same verdict as thirteen
`No` — the pass moved several conjuncts from *unprepared* to *prepared*,
which is real and is not the same thing as satisfied.

*(The round-08f report counted **eleven** conjuncts. The standard gained two —
default-path currency and bounded-packet comprehension — so the two reports'
denominators differ by design and neither is a correction of the other.)*

## The readiness standard, conjunct by conjunct

The column that matters is the third: what would change the state, and who
can do that.

| # | Conjunct | State, and what would change it | Owning record |
|---|---|---|---|
| 1 | `P-33` is ruled | **No.** Prepared, reviewed (RD-49, RD-54), and the only thing withholding the Wave A offer | `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md` |
| 2 | Wave A is lawfully **offered and accepted** | **No.** The *argument* is confirmed (`VERDICT: CONFIRM`, RD-31b) and no act has been performed. `P-33` alone withholds the offer | acceptance record §1 |
| 3 | Wave B is accepted **after** Wave A | **No.** Confirmed (RD-32c), unoffered, and it follows Wave A | acceptance record §1 |
| 4 | `P-31`, `P-36`, `P-37`, `P-38`, `P-39`, `P-40` are ruled | **No — none is ruled.** All six now have a bounded packet stating costs, digest consequences and the exact transaction; `P-31`'s was created this pass | `decisions/README.md` §3 |
| 5 | The specification-acceptance policy is **in force** | **No.** Candidate, rewritten this pass, **unreviewed**. Needs `P-40` ruled first, then a joint review with `P-42`, then its craft act (`P-41`) | `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` |
| 6 | The shape-to-spec impact policy is **in force** | **No.** Same state and the same joint review (`P-42`). Its bounded packet was created this pass | `policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` |
| 7 | The propagation fixture **passes** | **Yes — and it is the one conjunct that moved to satisfied.** `RD-59` administered fixture 2 blind, at the digest `CC-IMPACT-7` names, and it **passed** the answer key's three criteria. Two fixture defects it found are filed for a fixture 3, never an edit | `round-2026-08g/reviews/RD-59-blind-propagation-RAW.md` |
| 8 | Operating constraints are recorded | **No.** `P-35` open; all eight rows unstated. The packet now also states the limit a scope-reduction trigger may not cross | `decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md` |
| 9 | The launch-gate instrument is **owner-approved** | **No**, and the reason changed this pass. Four reviews across two versions have returned `REVISE` four times; v2.2 repaired the v2.1 pair and **has had no review at all**. The packet is repointed from v2.0 to v2.2 and now says this first | `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` |
| 10 | The formal structured administration returns **READY** | **No.** None has been run, under any version. The only administration on record is the 2026-08-09 pilot at v1.3: `GATE VERDICT: NOT READY`, with **all six of section E** Not met | `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` |
| 11 | The owner **separately authorizes** launch | **No.** Downstream of 10, and not reachable today | — |
| 12 | Default-path currency and hygiene **passes** | **No, but it is now measured rather than asserted.** `CG-27` checks that every default-path claim about wave, gate or launch state names the record that owns it; it found six live findings, all repaired, and is clean at this commit. It is **advisory** — its rule's home is candidate policy (`P-12`) | `scripts/check_governance.py` `CG-27` |
| 13 | Each owner decision is comprehensible from its **bounded packet** | **No — and this is the conjunct the pass moved furthest.** Every launch-critical decision now has a packet; `P-34`'s 1,280-word queue cell is 103 words; **six** packets gained a per-arm digest-consequence table, and three more carry one in the seven-part shape. What is missing is a **fresh reader confirming it**, and the last one (`RD-52`) returned `REVISE` on the page this pass superseded | `decisions/README.md` §3 |

**Twelve `No`, one `Yes`.** Conjunct 7 is satisfied. Nothing else is.

## What actually changed this pass

Stated as movement, not as progress:

| | |
|---|---|
| **Capability 1's shape has one source** | Five views were hand-maintained and had to agree; they are now generated from `CAPABILITY-1-CHARTER.yaml`, with `--check` failing on drift. The charter names clause IDs and no authority homes, so a wrong home cannot be authored |
| **A fresh reader outlined the capability from the generated route** | `RD-60`, with every review, register and the decision queue withheld. It returned a full outline and found **three clauses the charter was missing** by trying to write requirements and running out of authority; a fourth was added on a reliance argument during disposition |
| **The propagation path was run, not just specified** | `RD-59`, blind, passed — while measuring that a contract-only sweep would have missed **4 of its 6** affected requirements |
| **CC-SPEC and CC-IMPACT were repaired as one model** | Six machine-readable warrant classes with one home; the impact policy's trigger set stated as a set identity rather than a second enumeration that could drift |
| **The launch packet's stop rule fired on itself** | One of its four bound digests had moved. Re-sealed, with the change stated as a reviewable claim and two re-runnable pieces of evidence |
| **`P-39`'s pre-decision measurement was run against current sources** | Upstream is `1.8.0`, not the `1.7.0` the lock records. Format delta measured from both published tarballs: **additive** — which inverted the packet's own recommendation rather than confirming it |
| **`AGENTS.md` is inside its band** | 1,498 → 1,200 authored words, and the review found the excess was restatement rather than procedure |

## What eight measurements found that reading would not have

`[Observed]`, each re-runnable:

1. A contract-only propagation sweep misses **4 of 6** affected requirements.
2. Two generator predicates were running, believed, and discriminating
   **nothing** — disabling either produced zero fixture failures.
3. A charter fixture had been passing **while testing nothing** since its
   mutation literal moved; so had a launch-gate fixture whose path another
   session untracked.
4. The queue's open-row predicate dropped an **open row** because that row's
   prose asks whether `**Executed.**` should be the convention.
5. All three limbs of that predicate had **zero independent coverage**,
   because two of them mask each other on the real corpus.
6. A repair that added a citation pushed a claim **outside** a check's window,
   silently shrinking the denominator from 17 to 16.
7. The formal launch packet bound a validator digest that had moved, and the
   sealed bytes' own selftest **fails at HEAD**.
8. The `P-34` packet asked the owner to approve **v2.0**, two versions after
   v2.0.

Six of the eight are defects in this session's own work or in checks this
repository trusted. That is the useful part.

## Clone and hosted CI

Green in a fresh public clone and in hosted CI at two consecutive commits.
The report is `round-2026-08g/FINAL-PUBLIC-CLONE-REPORT.md`, which names the
commits it is valid for. **No figures are restated here** — a count copied
into a status page is stale within two commits, twice measured.

## The plainest answer

**No.** Not one of the acts has been performed, not one of the launch-critical
decisions has been ruled, the specification standard the first spec would be
judged against is unreviewed, the instrument that would judge readiness has
never returned anything but `REVISE`, and no formal administration has ever
been run.

What is true instead: **every one of those is now prepared, bounded, and
costed.** An owner can sit down with `decisions/README.md`, open one packet
per decision, and see the question, the options, what each costs, which digest
moves, and the exact next transaction — without reading a review history.

That was the pass's actual goal. Readiness was never on the table.
