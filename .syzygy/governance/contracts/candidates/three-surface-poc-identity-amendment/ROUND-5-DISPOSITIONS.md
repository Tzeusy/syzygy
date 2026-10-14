> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fifth fresh-context review of the Three-Surface POC
> identity amendment package. This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It offers nothing and
> performs no act (VIS-4).

# Round 5 dispositions — Three-Surface POC identity amendment

- **Reviewed commit (raw line 2):**
  `e7fd5301daf1c52a8e8ddab08cb1e50ddf4169d8`, the head of
  `candidate/p84-round4-repairs` (draft PR #413).
- **Manifest file digest (raw line 3):**
  `998215c3aad0483f9862432cddfec6e1b263cd69dc5803e6b9c3a1e1f69b391c`.
  [Observed 2026-10-14] The manifest file hashes to the same value after the
  branch was rebased onto `main` and landed with this record, and the
  builder's `--check` passes there.
- **Verdict (raw line 4):** `REVISE`. One revise finding (33) and five
  notes (34–38), with no blocking finding (raw line 352).
- **Stopping rule applied.** The owner's direction of 2026-10-14
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`):
  one repair and one review per packet; anything still `REVISE` goes to the
  owner with its findings, not into another loop. Round 4's findings were
  repaired once and round 5 is the one review. Round 5 is not notes-only.
  So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the sentences that said round 5 was pending.
  - **No round 6 is dispatched.**
  - **The review has not cleared.** This version is not offered for
    sign-off. It goes to the owner as register row P-84, with the six
    findings below open.
  - This record recommends nothing on Questions 1 and 2.

Reviewed record: docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-5-RAW.md

## Round-4 repairs, as the reviewer judged them

Raw lines 137–174: findings 27, 28, 29, 31 and 32 repaired; 26 partly
repaired (its remainder is finding 33); 30 repaired for every probe round 4
reported, with new repair text partly unguarded (finding 37).

## Findings, open

### 33 — POC-REQ-054 attributes elements, not machine-answer records, to subjects (revise)

**Open.** Raw line 178. The repair widened the sweep population to
machine-answer records, but the oracle-independence attribution rule, the
ownership test and the equality limb still speak of elements only, while
the RFC6-3 and RFC6-1 covered rows and `SEMANTIC-DELTA.md` §1 say records
are attributed too. Criteria 2 and 3 are not met. The raw's repair: extend
the three sentences to "each element and record … by the source record it
renders or answers for", with a required phrase, or narrow both covered
rows and add an Unknown row for the machine-answer limb.

### 34 — POC-REQ-054's first scenario states a narrower denominator than its sweep (note)

**Open.** Raw line 236. Use one denominator phrase in the sweep and the
scenario.

### 35 — "never green" is read as visual distinctness; RFC2-25's table uses "green" as a positive status (note)

**Open.** Raw line 247. The covered row rests on a reading; the raw
suggests an `[Inferred]` tag on the row or a sentence in the delta.

### 36 — the ownership procedure's key term is not defined per source (note)

**Open.** Raw line 264. A sentence saying the per-source identifier field
is fixed by the slice that lands the form would close it.

### 37 — the round-4 repair text is partly outside the builder's phrase guards (note)

**Open.** Raw line 283. Seven of the reviewer's ten probes survived the
structure gate; the manifest digest freezes the reviewed bytes, and
criterion 5 is met.

### 38 — the sibling-package regeneration step sits in the ledger, not in the delta's residual list (note)

**Open.** Raw line 299. A fifth residual line in the delta would put it
where the signing change will look.
