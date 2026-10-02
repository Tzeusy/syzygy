# R-POLARIS-UNDERSTANDING-DEPENDENCY-UNION-SUCCESSOR-1 — Polaris understanding dependency-union successor confirmation
Verdict: CONFIRM WITH EXCEPTIONS
Manifest-file SHA-256: 9c01c82d482aa79a5342ec650e7c284e4c90a900e38ea8166c8f7708599b34c8
Reviewed commit: 6a013e87cd7cf27127e4b6d5779dd3ceb6e02019

Package: `.syzygy/governance/contracts/candidates/polaris-understanding-dependency-union-successor/`
(PKG below), plus `scripts/build_polaris_dependency_unions.py` and the R7 case
`union-after-successor-act`. Method: `git archive` of the reviewed commit into a scratch
directory (no edits to the repository), and a local clone at that commit for the
rehearsal. The manifest digest above was computed by me with `sha256sum` over
`SUCCESSOR-MANIFEST.txt` at the reviewed commit; it equals the digest quoted in the
packet's phrase (the only 64-hex string in the packet).

## Findings

**Finding 1 — Regeneration is exact; the only change is `CC-REV-8` (criteria 1, 2)** (note)
[Observed] I recomputed the union of all warrants blocks in the amendment's `spec.md` with
an independent regex parser (not the builder's, not R7's). The class sets, rendered in the
signed file's format (class order with `primary` first, sorted, comma-joined, the
empty-class sentence for `topology`, one trailing blank line), equal the proposed file
byte for byte. The same method renders the base union and equals the signed base file
byte for byte. `diff` of the signed file against the proposed file shows one changed line:
`CC-SPEC-2, CC-SPEC-4` becomes `CC-REV-8, CC-SPEC-2, CC-SPEC-4`. Subject digest
315207c0… equals `SUCCESSOR.json`'s predecessor and the act-in-force row; the proposed
file hashes to e6067cf6…, equal to the manifest row. The addition belongs: REQ-polaris-generation-004
("Understandable reading depths") declares `policies: [CC-SPEC-2, CC-SPEC-4, CC-REV-8]`
at spec.md line 227 and its body cites CC-REV-8 (tree-form sentence, line 78);
CC-REV-8 is defined in `craft-and-care/review-and-documentation.md`. The spec's tree-form
amendment is commit af14aa6 of 2026-09-28, matching the packet's date. The 2026-09-29
readability act left spec.md bytes unchanged (predecessor equals successor), so the
union has been stale since then.

**Finding 2 — Editorial classification holds (criterion 6)** (note)
[Inferred] The proposed file is a derived artifact whose own header says it is review
routing, not authority. The change brings it into line with an unchanged source whose
obligation is already carried by the warrants block; no requirement, scenario or warrant
structure changes (the successor tool's structure check passes). No tracked code under
`scripts/`, `packages/` or `apps/` that I searched consumes the union as a permission;
consumers are the reconciliation R4/R7 and the dependency builders, which
only compare. One reading caveat for the owner, not a defect: the union drives review
routing, so adding `CC-REV-8` widens what a reviewer is routed to check. That is a routing
change in the correcting direction, and the packet states it as under-reporting.

**Finding 3 — Package is internally consistent (criterion 3)** (note)
[Observed] `readability_successor.py --all --check` reads `candidate-unperformed` for
this package and PASS for the other three; `--package ... --diff` shows the single line
above; the manifest equals the regeneration.

**Finding 4 — Builder reproduces both signed unions; `--check` and `--selftest` pass (criterion 4)** (note)
[Observed] `--check` prints the unperformed-successor note; `--selftest` reports 15
fixtures, 0 failing. The two renderer-fidelity fixtures are real evidence: they compare
the renderer's output with the signed bytes (base as signed; understanding with
`CC-REV-8` removed from the spec text), and the understanding one covers the
empty-class sentence, the trailing blank line and the `primary`-first order. My own
mutations of a scratch copy: (a) `sorted(union[cls])` replaced by `list(union[cls])` was
caught by three fixtures (unmutated copy, understanding fidelity, performed); (b) removing
the `sha256(actual) != predecessor` predicate was caught by "the understanding union
edited"; (c) changing the empty-class sentence was caught by the same three fixtures as (a).
Claims no mutant covers: the "spec carries no warrants block" and "unparsed warrant line"
errors have no fixture; the predecessor digest recorded in `SUCCESSOR.json` is never
itself mutated (only the installed file is); the "unterminated block" fixture mutates
the base spec only. None is on the path of the regeneration this act signs, hence note.

**Finding 5 — R7 case proves what it says (criterion 5)** (note)
[Observed] `check_spec_reconciliation.py --selftest`: 25 of 25 mutants killed, including
`union-after-successor-act` (expects R7 zero with R2 alone failing). I mutated the
proposed union two ways in a scratch copy. Dropping `CC-REV-8` from it makes the case
fail (the file then equals the signed one, so R2 does not fail as expected). Swapping it
for `CC-REV-9` makes the case fail with R7 non-zero. So the case is sensitive to both
halves. R2 failing and only R2 is consistent with R2's documented design in the script
header ("a later act over any subject fails R2 by design").

**Finding 6 — Recording prerequisites are stated accurately (criterion 7)** (note)
[Observed] I rehearsed the act in a clone at the reviewed commit (placeholder raw, pins
filled, `--record` with the packet phrase). Results: (1) `readability_successor.py
--all --check` then FAILs for `polaris-understanding-readability-successor` ("subject
differs from its successor row" on the union file), as stated; (2)
`record_polaris_understanding_adoption.py --check` then FAILs with "current subject drift"
on `design.md`, as stated; (3) `check_spec_reconciliation.py` R2 FAILs naming the union
file ("no longer hashes to its signed row"), as stated. Bead syzygy-xp95 describes the
same three failures and the digest pin `SUCCESSOR_TOOL_SHA` (it equals the current
sha256 of `readability_successor.py`, 88358478…). After the record, `check_governance.py`
reported 0 FAIL, and the contract index, dependency index, budget, active manifest, task
router, truth-policy, Polaris dependency/coverage builders and the bootstrap ledger and
transaction checks all passed, so I found no prerequisite beyond the stated ones. The
packet's own [Unknown] (further failures behind the adoption recorder's first) stands; I
could not see behind it. Separately, item 4 is a true statement of an unmet condition:
the builder is not yet in the battery or hosted workflow.

**Finding 7 — Signing path and authority claims (criteria 8, 9)** (note)
[Observed] Scope A's direction covers "the PWB specification deltas, the observer registry
entry and the contract successors queued behind them"; a Polaris generation amendment
file is none of these, so the phrase-and-digest path is correct. The packet's phrase
carries 9c01c82d…, the current manifest digest; a stale copy is detected (I altered it in
a scratch copy and `check_governance.py` CG-7d and CG-7e failed). The package files
carry "Candidate/Proposal, binds nothing" language; none claims authority it lacks.
Minor, not a defect: the new label is not registered in `check_governance.py`, but the
sibling readability successor packages follow the same pattern and CG-7d/7e did catch my
mutation, so the practical coverage is present.

## Disposition

Every finding is a note. The bytes reviewed are clean for the stated change; recording
remains blocked by syzygy-xp95 and the other disclosed prerequisites, which are correctly
stated. Whether to sign is out of scope for this review.
