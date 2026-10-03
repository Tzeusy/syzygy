# Round 1 dispositions — Three-Surface POC governing-intent amendment

> **Candidate — binds nothing.** This record says how each round-1 finding
> was handled. It is not itself reviewed.

**Raw review:** `docs/reviews/R-N10-POC-GOVERNING-INTENT-1-RAW.md`, stored
verbatim (CC-REV-6).

**Reviewed bytes:** commit `5fca4450b3a481ec5b9784ba71ed392befddd563`; the
raw's head carries the package digest computed as `REVIEW-BRIEF.md` defines
it.

**Verdict, copied from the raw (line 4):** `Verdict: REVISE`

**Findings:** 12 — seven `revise` (1–7) and five `note` (8–12), counted from
the raw's twelve `**Finding N - <title>** (<class>)` headings.

**Stopping rule, set before the round by the coordinator's dispatch:** one
fresh-context round; on `REVISE`, one repair and no round 2. Every finding
below was repaired once. **The repaired bytes are not cleared**: no reviewer
has read them, so this version is not offered for sign-off. The owner decides
whether a confirmation round comes first (register row P-100).

## Dispositions

| # | Class | Finding (raw title) | Disposition |
|---|---|---|---|
| 1 | revise | The Scope's reason is not enforced by the oracle or falsifier | **Repaired.** The oracle now requires the reason `source-uncaptured-or-unreachable` and the route RFC2-24 gives it on every item; the falsifier fails any other reason or route. |
| 2 | revise | The edge arm is unreachable and undefined | **Repaired by removal.** POC-REQ-014 now defines no edge: every item is Unknown under this specification, and the *Scope* says an edge and its input need a further amendment. `SEMANTIC-DELTA.md` §"What the delta says" gives the reason (an arm no oracle can reach). |
| 3 | revise | The recommended option's consequences are understated in the owner packet | **Repaired.** Question 1's recommended row now lists a specification amendment, sign-off and an implementation authorization, and every row's "needs" column says what comes before building. |
| 4 | revise | New covered rows overclaim, and newly mapped clauses have unlisted limbs | **Repaired.** The RFC8-23 covered row is narrowed to counted, filterable, never green and its route; "never pooled", "never an ingest rejection", the substrate-edit annotation and the orphaned-work limb each have an Unknown amendment row. RFC8-22 gains an Unknown row for downstream degradation. The RFC4-15 row now says "the work-item title, the only free text the POC reads". |
| 5 | revise | B2 rationales for RFC8-21 and RFC8-24 contradict the delta | **Repaired.** RFC8-24 moves to Part A with a covered row (Trajectory renders `source-uncaptured-or-unreachable` with its route) and an Unknown row (the other four reasons and the retention-event limb). RFC8-21 stays in Part B2 unedited; the delta says why its signed rationale is still true. Totals re-derived: 77 / 27 / 220; Part A 118 rows, 97 covered, 21 Unknown. |
| 6 | revise | The ROUND-1-DISPOSITIONS.md the packet and P-100 point to does not exist | **Repaired.** This file lands in the same change as the repair. |
| 7 | revise | The owner packet is not yet plain enough for Question 2 | **Repaired.** Question 2 now explains the 2026-10-02 short signing route in plain words, and Question 1's table explains consent, secret scanning and the read list. Question 3's "Drop it" row says what is lost. |
| 8 | note | Reason choice is acceptable but its weighing is incomplete; route mismatch undisclosed | **Repaired.** The delta weighs reasons #2, #5 and #7 and discloses the two routes. Trajectory states RFC8-23's resolution beside the count, quoted against RFC2-24's "fact of the render" sentence. |
| 9 | note | Blanket "SHALL NOT be labelled orphaned work" can collide with RFC8-23 | **Repaired.** The requirement now says no Unknown marker replaces or hides an orphaned-work Contradiction where one is rendered. |
| 10 | note | Form and means of the check | **Repaired.** Each "never" sentence is now an invariant over every served item; the case names a fixture work-item database or an injected work-item read; the observable names the narrowed board's item list. The denominator limit is disclosed in the delta and carried as RFC8-23's Unknown ingest row. |
| 11 | note | "Reads nine columns" omits the materializer's external_ref predicate | **Repaired.** The delta and the packet now describe the `findByExternalRef` filter and say it returns only `id`. |
| 12 | note | Items confirmed without exception | No action. |

## Re-checks after the repair

[Observed] Over the repaired bytes:

- all four patches pass `git apply --check` against the signed bytes;
- `scripts/build_three_surface_poc_spec_dependencies.py` over the proposed
  `spec.md` reproduces the proposed `GOVERNING-DEPENDENCIES.md`, and
  `--check` passes at 25 requirements and 88 distinct authorities;
- the matrix totals were recomputed by a Python sweep and confirmed by
  `grep -c -F` over the Part A section;
- applied after the identity amendment's (P-84) patches, all four still fail
  to apply, so the ledger's overlap claim stands.
