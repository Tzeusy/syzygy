# Contract readability restyle — binding-review notes

> **Status:** a sibling record to the owner decision packet. The packet is
> left as reviewed; these corrections to it come from the binding review
> ([`R-TREE-STYLE-CONTRACT-PACKAGE-1-RAW.md`](../../../../../docs/reviews/R-TREE-STYLE-CONTRACT-PACKAGE-1-RAW.md),
> `CONFIRM WITH EXCEPTIONS`, notes only). None touches the manifest or the
> act argument.

- **N1. One "found, not changed" citation points at the wrong clause.** The
  bar on placement by observed coupling is RFC9-9 (with RFC9-14's closed
  input tuple enforcing it), not RFC9-17, which bars metric-driven churn.
  RFC 0009 §7 case 3's citation of RFC9-11/16 is still loose.
- **N2. Two items are loosely worded.**
  - RFC9-45's "closed at twelve" is correct today (RFC2-24 holds twelve
    reasons); the concern is a count restated outside the clause that owns
    it.
  - RFC 0007's body marks all three letters of RFC7-2 and RFC7-9; only the
    qualified form "RFC7-2(a)" appears solely in the front matter and the
    closing line.
- **N3. "Every link and code span" is stated more absolutely than the
  evidence.** The modules have no Markdown links. Every original code span
  survives, in order, in 28 of 29 files; `RFC-0004/named-adapters.md`'s
  non-normative §0 swaps the order of `gate-backed` and `report-fact`. New
  spans appear in 16 files, mostly in reader maps and captions.

## From the tooling confirmation review

These notes come from
[`R-TREE-STYLE-TOOLING-2-RAW.md`](../../../../../docs/reviews/R-TREE-STYLE-TOOLING-2-RAW.md),
`CONFIRM WITH EXCEPTIONS`, notes only.

- **The adoption change must also regenerate two views (N3).** After the
  recorder and `--apply --at-adoption` run, CG-7a fails on 29
  `ACTIVE-CONTRACT-MANIFEST.txt` rows and CG-18 fails on the 10
  context-selection fixtures. Neither view is digest-cited, so the adoption
  commit regenerates them:
  - `build_active_manifest.py`;
  - the fixture remeasure;
  - the budget report and the generated contract indexes.

  Run the full PROJECT-STATUS battery before merging it.
- **Adopting the restyle forecloses the no-signal link as the chain stands
  (N7).** Chain order is adoption order. A no-signal act recorded after this
  one fails CG-7h until the chain is reordered and that package is rebuilt
  over the restyled bytes. No no-signal package exists today, so the effect
  is only prospective.
- **The recorder's pins are enforced only when the recorder runs (N1).** The
  merge-time CG-26 integration adds its `--check` to the battery. Hand-written
  act records would pass CG-7h without the recorder.
- **The rule-6 evidence names `2fd8082` (N4).** That is the pre-rebase twin of
  `80ec3c0`. The three scripts are byte-identical between the two commits, so
  the record re-runs at either.
- **Open, tracked as beads:**
  - N2: ordering acts by first aggregate line can be bypassed by inserting a
    record mid-file.
  - N5: the packet-copy registration has no selftest.
