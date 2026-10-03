> # Record beside the package — not authority, binds nothing
>
> Dispositions the findings of the first fresh-context review of the PWB
> behaviour-contract re-pin (tree framing) package. It is not a package
> artifact: the manifest does not hash it and no builder reads it. It
> offers nothing and performs no act (VIS-4).

# Round 1 dispositions — PWB behaviour-contract re-pin (tree framing)

- **Reviewed commit:** `54f8b30837536e3bf90d445fe0048f0316fee41b`.
- **Verdict (raw line 4, the fourth non-blank line):** `REVISE`; seven
  findings, counted from the raw's finding headings: one `revise` (1) and
  six `note` (2–7).
- **Effect:** a `REVISE` round clears nothing. Every finding was repaired
  once, in the package prose and in the builder's selftest. The two patches
  and `PWB-EFFECT-REPIN-MANIFEST.txt` are unchanged, so both act arguments
  and the manifest file digest the raw names are the same. The prose and
  the builder changed, so the round's reading of them is retired (rule 10).
- **Stopping rule (set for bead `syzygy-2g0d` before the round):** on
  `REVISE`, repair once, dispatch no round 2, route to the owner. No round 2
  was dispatched; the repaired bytes are unconfirmed.

Reviewed record: docs/reviews/R-PWB-BEHAVIOR-CONTRACT-REPIN-TREE-FRAMING-RAW.md

## Dispositions

### 1 — the Signing path misstated the Scope A direction's condition (revise)

Repaired in `OWNER-DECISION-PACKET.md`, "Signing path". The packet now
quotes the direction's two sentences as worded, says what has landed
(commit `842b624f`, `scripts/record_versioned_signoff.py`) and what has
not (the gate still evaluates the registry role only from an exact-digest
record), and says the tag path is open in principle but not yet evaluable
by the gate. The words "that contract change" are gone.

### 2 — three builder predicates survived their own removal (note)

Two repaired in `scripts/build_pwb_behavior_contract_repin_tree_framing.py`:
fixtures "a second governingBehaviorContract object" and "--apply refuses a
package that does not verify" (37 fixtures). Rule 6, run after the repair:
replacing `if _count_contracts(new) != 1:` with `if False:`, and `apply()`'s
`if findings:` with `if False:`, each gives `37 fixtures, 1 failing`.

The third, the post-act "subject is not the proposed bytes" comparison, is
kept as written and not given a fixture. The reviewer's [Inferred] reading
is accepted: it cannot fire once the reverse apply and the predecessor
digest test pass. It is the same line the performed 2026-10-02 builder
carries.

### 3 — the ledger named one failing gate-test case; five fail (note)

Repaired in `IMPACT-LEDGER.md`: the `governance-inputs.test.ts` row now
states the reviewer's rehearsal result (five hermetic cases fail) and the
[Inferred] real-tree failure once the act change is committed. The figures
are the reviewer's, from the raw; the drafter did not re-run that suite.
At-adoption step 4 already covers them.

### 4 — the Normative reason did not use the template's test (note)

Repaired in `SEMANTIC-DELTA.md`: the reason now applies the template's
"may not comply now" test to the seven added PWB-REQ-014 scenarios.

### 5 — open question 2 understated what a version bump touches (note)

Repaired in `OWNER-DECISION-PACKET.md`, open question 2: it now names the
gate's `policyVersion` expectation, the two core constants, the two tests
that read the file, and four test files with hard-coded labels. The count
of four was re-derived by `git grep -l -F` for either label over the
`*.test.ts` files under `packages/` and `apps/` (the reviewer's list named
three of them plus a file that reads the label from the policy).

### 6 — RFC3-16(b) item 3 was not quoted in full (note)

Repaired in `OWNER-DECISION-PACKET.md`, "Signing path": item 3 is quoted
("the **exact content or revision digest** of the artifact as acted on"),
and the owner decision is stated as whether a tag is a "revision digest".

### 7 — the Recording section named no review-campaign row (note)

Handled at recording: the raw matches the `registry-currency` campaign
pattern, and `docs/README.md`'s "P-69/P-72 registry gate" row and the
partition count change in the commit that retains the raw. The brief is
not edited for this.
