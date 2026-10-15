> # Record beside the package — not authority, binds nothing
>
> Dispositions of the first fresh-context review of the Three-Surface POC
> vocabulary and epistemic-record amendment package (register row P-108).
> This record is not a package artifact: the manifest does not hash it and
> no builder reads it. It offers nothing and performs no act (VIS-4).
>
> **Status, 2026-10-15: round-1 findings repaired once on 2026-10-15,
> unconfirmed pending round 2.** Every finding below, notes included, was
> repaired once; see "Repairs, 2026-10-15". Round 2 is briefed in
> `REVIEW-BRIEF.md` §"Round 2" and has not run.

# Round 1 dispositions — Three-Surface POC vocabulary and epistemic-record amendment

- **Raw:** docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md,
  committed verbatim by a separate records lane (left out of code span so
  the path check does not ask it to exist before that lane lands).
- **Reviewed commit (raw line 2):**
  `6d3923f365bca6e4458200ac0f75381655ef5bb6`.
- **Manifest file digest (raw line 3):**
  `03069d521ae3280f2abf8525950d74e3a128cec1db140218efa3372791a75cba`. The
  repairs below regenerate the manifest, so the current file no longer
  hashes to it (verification rule 10: the round reviewed those bytes, not
  these).
- **Verdict (raw line 4):** `REVISE`. Two revise findings (1, 2) and seven
  notes (3–9), with no blocking finding (raw line 297).
- **Stopping rule applied.** The round-1 rule in `REVIEW-BRIEF.md` sent a
  `REVISE` back to the owner with no repair. The owner's direction of
  2026-10-15, "One cycle" [Observed: as relayed by the lead session; not
  recorded under `decisions/`], is one repair and one fresh review under
  the same rule. So the package was repaired once, below, and round 2 is
  briefed; a `REVISE` in round 2 goes back to the owner with no further
  repair. The repair lane dispatched no review and signed or recorded
  nothing.
  *(Marked 2026-10-15, records lane: "not recorded under `decisions/`" is
  no longer true. The direction, and "Park, redraft narrower" before it,
  are recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`.)*

## Repairs, 2026-10-15

Each finding, its level as the raw labels it, and the repair. The repaired
bytes are the four regenerated patches under `proposed/` (written through
the scratch-apply-and-diff route, never applied in the tree), the manifest
regenerated with the builder's `--write`, the builder's guards, and the
three prose files. [Observed 2026-10-15] After the repairs `--check` reads
26 requirements and Part A 78 clauses over 147 rows (105 covered, 42
Unknown); an independent counter importing nothing from the builder
returns the same figures, and 25 amendment-marked rows, 18 of them Unknown.
`--selftest` reports 82 structure mutants (69 before).

| # | Level | Finding (short) | Repair |
|---:|---|---|---|
| 1 | revise | RFC2-25's Semantics column listed as an Unknown limb for `asserted-by-worker` only | `CONTRACT-COVERAGE.md.patch`: a new RFC2-25 Unknown amendment row, "A record carries a tier only where that tier's Semantics column holds", naming each of the five other tiers' Semantics cell (quoted from `RFC-0002/rendering-vocabularies.md`'s RFC2-25 table) with the justification that POC-REQ-060's oracle validates membership and nesting only. Guarded in `UNKNOWN_ROWS`, with the mutant "tier Semantics row dropped". `SEMANTIC-DELTA.md` §2 "RFC2-25, limb by limb" says so. |
| 2 | revise | "every rendering" in POC-REQ-055 and in POC-REQ-060's Inferred limb has no population or denominator | `spec.md.patch`: POC-REQ-055's obligation, Scope, sweep, observable, oracle, falsifier and scenario now reach "every rendered element that marks the relationship", an element marking it when it carries the served `id` in one of the surfaces' declared relationship markers; the complete marker population is the counted, reported denominator (POC-REQ-020's form), and an unmarked rendering is stated to be outside the sweep. POC-REQ-060's Inferred limb reads the same way through declared record markers, with that marker population as the denominator. `CONTRACT-COVERAGE.md.patch`: the covered RFC1-26 disclosure row and the RFC2-25 "never green" row are narrowed to the marked elements, and two Unknown rows carry the unmarked renderings (one under RFC1-26, one under RFC2-25). Eight guards and eight mutants added (four phrase guards in the spec, two coverage-row phrases, two Unknown rows). The other option the reviewer named is owner Question 2 in `OWNER-DECISION-PACKET.md`, with the marked population recommended. |
| 3 | note | the census's stated placement rule ("by the requirement its heading names") is not the rule that produced the table | `SEMANTIC-DELTA.md` §"Findings census": the rule now reads "by the requirement its body addresses", and the seven heading-less placements (3, 4, 6, 7, 35, 36, 41) are listed. The table and its counts are unchanged. |
| 4 | note | 060 requires Inferred to differ from Observed only, leaving POC-REQ-014's encoding arm satisfiable only by an unstated choice; "the legend" against "the declared table" | `spec.md.patch`: POC-REQ-060 requires "The declared token/encoding table SHALL give Observed, Inferred and Unknown three pairwise distinct entries", its oracle adds a pairwise comparison and its falsifier "a declared table giving two of the three labels one entry"; the Inferred limb now names "the declared table's Inferred entry", and "the legend" is gone from the spec patch and the RFC2-25 row. Two guards and two mutants. `SEMANTIC-DELTA.md` §2 "POC-REQ-014" re-judges the arm as decidable. |
| 5 | note | the delta's and packet's reason for dropping "claim" says the specification defines none, false since P-100 | `SEMANTIC-DELTA.md` §2 change 1 now names both kinds of claim the specification serves, quoting the signed RFC2-24 and RFC8-24 rows for the governing-intent claim and its place in `workItems`; `OWNER-DECISION-PACKET.md` corrects its sentence with a dated mark. The proposed bytes needed no change. |
| 6 | note | the reader-note sentence "its `Group` line does" reads as placing POC-REQ-055 in Orrery, and a guard froze it | `spec.md.patch`: "its number range does not place it in the Orrery group; its `Group` line places it in *Cross-cutting experience*." `READER_NOTE_PHRASES` and the mutant "reader-notes placement sentence dropped" now check the new wording. |
| 7 | note | "every Observed total" has no population; the Unknown recount pools ids across the two lists | `spec.md.patch`: POC-REQ-060's Scope defines "An Observed total is every count the machine answer serves, except a count the machine answer declares to be of Inferred records"; each recount "must equal the count served with it"; the scenario reads "changes no Observed total the machine answer serves"; the Unknown sets are "keyed by the list it is served in and the identifier the machine answer serves it under". The RFC2-25 "never a status input" row names the same population. Two guards updated, one added, one mutant added. |
| 8 | note | doctrine's separate-layer and VIS-7-exclusion limbs missing from the stated narrowing | `SEMANTIC-DELTA.md` §2 "A narrowing of doctrine's Inferred, stated" gains a paragraph quoting `trust-and-evidence.md` lines 111–116 and deferring both limbs to the production constructor's own act; the packet's "What round 1 changed" says so in one sentence. |
| 9 | note | 060 binds "in the shared model" but its oracle reads only the machine answer | `spec.md.patch`: POC-REQ-060's Scope adds "The shared model's records are observed through the machine answer, which serves the shared model's fact set (POC-REQ-020); no check reads the shared model directly." One guard and one mutant. |

**Owner questions added.** One: `OWNER-DECISION-PACKET.md` Question 2,
which renderings the flag and the Inferred encoding must reach (marked
renderings only, recommended and carried by this version; or every
rendering). No other repair needed an owner choice. No ruling is recorded.

**Not changed.** POC-REQ-014's block, every other signed requirement, the
RFC1-26 closure row and the signed POC-REQ-060 scenario are byte-identical,
as the builder checks. The census table's membership and counts, the
deferred scope and the five residuals are unchanged.

## Recorded beside the raw, 2026-10-15 (cycle-3 records lane)

Reviewed record: docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-1-RAW.md

[Observed 2026-10-15] The raw is now retained verbatim under
`docs/reviews/` (compared byte for byte with the dispatching session's
copy). Its head digest re-derives from the manifest file's bytes at the
reviewed commit `6d3923f3`. The finding count was re-derived by script
from its `**Finding N — …** (severity)` headings: findings 1 and 2
`(revise)`, 3–9 `(note)`, matching raw line 297. This section adds no
disposition; the table above maps every finding.
