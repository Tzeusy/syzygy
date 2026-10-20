# P-100 restoration review disposition

[Observed] The independent fresh-process source review is retained unchanged
at `docs/reviews/R-IMPL-P100-RESTORATION-1-RAW.md`. The companion
`p100-restoration-review-binding-2026-10-21.json` identifies its twelve source
subjects, commit, base and raw digest. Its actual assessment is **“Ready to
merge? Yes, conditional on required verification gates.”** It identified no
Critical or Important source finding and one Minor finding.

[Inferred] The Minor finding is retained without a source change: the exact
checkbox-tag assertion can reject harmless markup changes. This restoration
preserves the existing implementation; the independent browser tests also
exercise the narrowing behavior, including keyboard activation. Removing
that assertion can accompany later test maintenance. This disposition does
not treat the serialized tag as the behavioral oracle.

[Observed] The source review's verification limits remain on record. Separate
current results cover 144 focused tests, both browser cases, the 252/250/2
selection fixture, one passing mutation baseline and nineteen rejected
mutants. The restoration evidence retains the first inconclusive M03
attempt separately. Private API verification over the complete served
population and both host forms is recorded in
`p100-governing-intent-restoration-2026-10-21.json`; human private probes
establish status and size only. The full committed-tree clone and hosted
checks remain separate pre-merge gates. Nothing here is a release verdict.

[Observed] The old M4 route comparison is marked historical at its sentence,
with a fresh twelve-row census and both comparison methods in
`p100-route-literal-census-2026-10-21.json`. The original comparison and
earlier review raws remain preserved. The other six differing route strings
are unchanged.
