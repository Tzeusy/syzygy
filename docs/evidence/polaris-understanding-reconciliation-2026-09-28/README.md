# Understanding-amendment digest reconciliation

This is a technical evidence package for the owner's existing 2026-09-28
[tree-form adoption](../../../.syzygy/governance/decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md).
It performs no owner act. The owner record separately owns implementation
permission and the SVG ruling.

CC-SPEC-10 says: “Lawful adoption under VIS-4 is recorded at the exact digest,
and the record quotes what was adopted at which digest.” The technical
supplement records the source/blob correspondence; independent review must
judge whether that correspondence satisfies the clause. Review is Inferred,
while the owner source and Git blobs are Observed. Missing proof is Unknown.

## The two source links

- The original eight-row manifest, dedicated act, and embedded aggregate block
  are checked against the historical commit. Their bytes are preserved.
- The owner record identifies REQ-004 “as merged with this record.” The adoption
  commit identifies the full spec blob. Only that requirement differs; seven
  other manifest rows remain checked against current bytes. Two counting
  methods independently compose 31/177 historically and 31/182 after adoption.
- `proof.json` enumerates every subject, preserved owner source and four raw
  reviews, the changed requirement and the five added scenarios. It is
  evidence, never a replacement act.

## Freeze, review, record

1. C1 contains `review-inputs.json`, the complete technical-record template,
   proof, checker, and exact final documentation patch. No completed technical
   record exists at this stage. The two nearby documentation caveats retain
   observed owner adoption and disclose unresolved digest reconciliation.
2. A fresh reviewer inspects C1 and its governing references, tests the checker,
   and decides whether the exact owner-to-subject correspondence satisfies
   CC-SPEC-10. Store their complete, unchanged output as `REVIEW-RAW.md` in C2.
   The raw must contain exactly one total `Verdict:` header, with complete value
   `PASS` only when confirming, and exactly one total `Reviewed commit:` header:
   `Reviewed commit: <full C1 SHA>` line, and one `- \`path\`: \`sha256\`` line
   for every path in `review-inputs.json` plus that manifest itself. Those
   hashes are scripted; the raw is outside its own reviewed population.
3. After confirmation, `--render-reconciliation` writes a new technical record
   exclusively. It replaces only the template's C2 raw-digest placeholder and
   verifies the actual local recording date. Apply `final-documentation.patch`
   and run `--check`, then commit both in C3. Git provides the atomic boundary.
4. A fresh confirmation checks C3, unchanged source/spec bytes and the canonical
   battery in a clean clone of that exact commit. No result may be described as
   current after a relevant input changes without another review.

The C2 raw pins C1 and each reviewed input. The technical record pins that raw
and the candidate proof. The checker requires the retained raw after C1 and,
once committed, the technical record after C2. The documentation after-image
is checked at C3; later unrelated status-page edits do not rewrite this evidence.
The checker remains subject to review retirement; its fixed two-source recount
does not depend on the generic counter that other amendments may extend.

## Commands

```sh
python3 scripts/record_polaris_understanding_adoption.py --candidate-check
python3 scripts/record_polaris_understanding_adoption.py --selftest
python3 scripts/record_polaris_understanding_adoption.py --check
```

`--candidate-check` applies before C3; it reports unresolved technical recording.
`--check` fails until the retained review and exact technical record exist.
Selftests use in-memory mutations and scratch documentation copies, never edits
to governed inputs. Their `RULE6-WITNESSES` output records the tested commit,
path, old/new fragments, and specific refusal for every mutant. Retain that
output alongside the exact-head validation report. The legacy original recorder
selftests still exercise its owner-instruction and duplicate-act guards.

The existing CG-7e owner-act registration still verifies the unchanged historical
manifest, dedicated act and aggregate block. The retained raw reviews quote the
performed CC-SPEC policy digest as a reviewed input, so their exact path/hash
lines have explicit historical-copy registrations. A stale line fails even if a
correct digest appears elsewhere. This is evidence registration, never an act.
The shared governance checker is frozen through C3; its C3 bytes remain checked
as history so later unrelated checker changes need not rewrite this record.
The candidate battery remains unchanged; the final reviewed patch adds the two
passing commands to both local and hosted lists and derives their count from
those actual lists.
