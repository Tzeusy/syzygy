> # Record beside the package — not authority, binds nothing
>
> Dispositions of the second fresh-context review of the Three-Surface POC
> vocabulary and epistemic-record amendment package (register row P-108).
> This record is not a package artifact: the manifest does not hash it and
> no builder reads it. It offers nothing, signs nothing and performs no act
> (VIS-4).

# Round 2 dispositions — Three-Surface POC vocabulary and epistemic-record amendment

- **Raw:** `docs/reviews/R-M9-POC-VOCABULARY-EPISTEMIC-AMENDMENT-2-RAW.md`,
  retained verbatim (CC-REV-6; compared byte for byte with the reviewer's
  scratch copy by sha256 before commit).
- **Reviewed commit (raw line 2):**
  `a4a864e657d586e783fb3f5febc1ad9a990a34bd`.
- **Manifest file digest (raw line 3):**
  `559a5ea12f109f1e00e155420f19d1b46cc02c294691b713e720ae9482c6feb3`.
  [Observed 2026-10-15] The dispatching lane computed the same value with
  `sha256sum` over the manifest file at that commit, independently of the
  reviewer, after `--check` passed there.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`. Seven notes (10–16),
  no revise and no blocking finding (raw line 315). [Observed 2026-10-15]
  Re-derived from the raw's seven `**Finding N — …** (severity)` headings
  (lines 128–261), every one `(note)`.
- **Round-1 findings.** The raw (lines 276–308) judges 1, 2, 4, 5, 6, 8 and
  9 closed; 3 closed as to the rule, with new repair text carrying note 10;
  7 closed as to pooling and partly closed as to its population (note 12).
- **Stopping rule applied.** `REVIEW-BRIEF.md` §"Round 2": a verdict with no
  revise-level finding clears the exact bytes it read, under the owner's
  2026-09-26 ruling (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
  §1). The bytes at the reviewed commit are cleared. Its notes are recorded
  here, and **the package is not edited**: no patch, manifest, prose file or
  builder byte changes. A clearance is not a sign-off; Questions 1 and 2 and
  D1–D4 stay the owner's.

## Notes

None is repaired. Each is classified for whoever next touches these bytes:
the owner's sign-off change, or a successor package if the owner revises.

| # | Note (short) | Classification |
|---:|---|---|
| 10 | The census's "seven headings name no requirement" repeats round 1's list; swept by identifier, 14 requirement-theme headings name none | Prose in `SEMANTIC-DELTA.md` only. The census table, its membership and its counts reproduce (raw lines 90–95). Carried: state the predicate and its count of 14, or list all 14, in any successor. |
| 11 | Unmarked "not recorded under `decisions/`" sentences in `SEMANTIC-DELTA.md` (lines 14–16, 58–59) and the packet's D4 (line 179) | Stale-sentence class. Both directions are recorded in `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`. Not marked here, because the cleared package is not edited. Disclosed to the signer in register row P-108; the sign-off change marks each at the sentence. Whether D4's "Record it" arm still has content is the owner's question. |
| 12 | "Observed total": "count" undefined and the recount procedure unstated; the population takes in label-agnostic totals | Specification wording. The covered RFC2-25 row claims no more than the oracle reads (raw lines 200–202). Carried to implementation planning and any successor: name a with/without differential of every served count, or enumerate the declared counts, and say whether a label-agnostic total leaves Inferred members out. |
| 13 | An empty or implementation-chosen marker population passes both rendering limbs at a reported zero | Bears on owner Question 2 (marked renderings only). The two unmarked-rendering Unknown rows carry every unmarked rendering, so no covered row overclaims. Put to the owner beside Question 2: with zero declared markers the rendering limbs decide nothing (VIS-2). |
| 14 | POC-REQ-014's "any other state" also reaches reason or tier entries, which the pairwise rule does not separate from Unknown | Predates the package (the signed "and their reasons"); the package narrows it. The delta's "decidable" holds over the three labels only. Carried to any successor: extend the rule to every declared entry, or say so. |
| 15 | The tier-Semantics Unknown row paraphrases where `ROUND-1-DISPOSITIONS.md` says "quoted", and omits `suspended`'s provenance-rendering limb | The row's head clause reaches the whole Semantics column, so the limb is Unknown in substance (raw lines 254–256). `ROUND-1-DISPOSITIONS.md` row 1's "quoted" is not accurate to the bytes; it is a record beside the package and keeps its text. Carried: quote the cells, or add "among other limbs", in any successor. |
| 16 | The finding-9 repair cites POC-REQ-020 for a property it does not decide; RFC6-13 is the closer anchor | Citation, not reliance (rule 5). No covered row claims the shared-model limb. Carried to any successor. |

**Residuals for the sign-off change.** The five residuals `SEMANTIC-DELTA.md`
lists are unchanged; notes 11 and 13 add two disclosures the signer should
see, both named in register row P-108.
