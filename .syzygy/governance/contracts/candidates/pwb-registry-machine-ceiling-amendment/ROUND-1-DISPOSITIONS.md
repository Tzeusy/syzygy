# Round 1 dispositions — P-114 machine-ceiling amendment

Reviewed record: `docs/reviews/R-PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-RAW.md`
(over `cd653f04`). Its verdict line reads `Verdict: REVISE` (raw line 4).
The raw has nine findings: five revise and four notes. Under the lane's
stopping rule every finding was repaired once on 2026-10-20, and one more
round is dispatched over the repaired bytes. These repairs are unconfirmed
until that round reports.

| # | Severity | Finding (short) | Repair |
|---|---|---|---|
| 1 | revise | The applied-state check refuses the gate state ask 2 prescribes, because its substring also matches the supersession target | `code_findings` parses `PWB_ACT_RECORDS`, `PWB_SUPERSEDED_ACT_RECORDS` and the registry authority object separately. Applied, the supersession target must equal act B's record. `_apply_fixture` now builds the prescribed state (all four pointers), and a mutant leaves the supersession target unmoved |
| 2 | revise | The growth attribution is labelled Observed, but the evidence record labels it Inferred | `SEMANTIC-DELTA.md` splits the paragraph: equal sizes at both commits stay [Observed]; "not code / not git tree" and the Dolt attribution are [Inferred]. The packet's paragraph is changed the same way |
| 3 | revise | The version precedent is cited selectively | The delta names the 2026-09-05 and `.18` bumps and the entry's own convention, argues the departure (value under an existing key; P-112's `1.3.0`; the scope anchor sites), states the cost, and the packet offers the owner the convention as an overrule |
| 4 | revise | Impact ledger: false sweep claim, an unnamed reader, scope of the dry run, evaluation identity | Method item 2 corrected (18 prose files, 7 outside, 3 real, listed in part A). New part A2 lists the readers of the entry's bytes, including the parity test and the evaluation identity. The dry run now covers both POC packages' full non-browser suites: 0 → 5 failures in 2 files |
| 5 | revise | Ask 2's "nothing else" does not match what the commit must edit, and item 4 is open-ended | Ask 2 gains item 5, which names the recorder, the `check_governance.py` registration and the CG-26 lines. Item 4 accepts only this package's manifest row, named explicitly. The ledger's B2 and B3 point at those items |
| 6 | note | "Fails closed" claims more than the builder enforces; substring predicates | The packet now rests the claim on the authorization's bounds and says `--check` is manual until it joins the battery. The predicates parse the constant's object with comments removed, accept either quote style, and check act identity and tag as well as the path. Mutants cover P3 (comment), P4 (double quotes) and P5 (identity or tag unmoved) |
| 7 | note | Selftest gaps | An out-of-context sibling edit is added, with the needle `MANIFEST.txt differs`. The data assertion is removed. The unreachable one-row predicate is removed. The docstring says `git apply --check` is defence in depth that no mutant isolates. 22 of 22 hold |
| 8 | note | "Sign without authorizing" leaves an unrecorded signature undefined | The packet adds "Asked together, recorded together": nothing is recorded until both answers exist in one exchange, and a lone sign-off lapses and is re-offered |
| 9 | note | The delta drops the evidence record's own disagreement | One clause added (394 vs 261 item-equivalents; changed or unrendered rows) |
