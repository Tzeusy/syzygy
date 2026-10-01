# Review — RFC-0007 scoped-values contract successor (fresh-context, round 2 of the retained set)
Reviewed commit: 9b0dc778a74b94aa8e08f46d1ed1d4e0da234b38
Manifest SHA-256: 730f6acbf2ebef54ac713106f4965fb9a461c41bf3684f4af1c3a76944d7d2b0
Verdict: REVISE

Subject: `.syzygy/governance/contracts/candidates/rfc7-scoped-values-successor/`
at the commit above, read in a detached worktree (removed afterwards). I did
not open the earlier raw or the packet's round history. I judged the bytes
against `REVIEW-BRIEF.md` criteria 1-6.

## Verification run this session

- `sha256sum` of `CONTRACT-AMENDMENT-MANIFEST.txt` (the file) =
  `730f6acb...d7d2b0` (the head value above); this equals the phrase digest
  in `OWNER-DECISION-PACKET.md`.
- Manifest row `c1d760c3...ca72`: recomputed by applying the package patch
  (`patch -p1`) to the current module in a `git archive` copy; the result
  hashes to that value. The installed and candidate mirrors are byte-identical
  at HEAD (`cmp`). The package patch and the lane B contract patch differ
  only in the `a/`, `b/` and `diff --git` path prefixes (`diff` of the two
  files shows header lines only), and the builder's lane B check passes.
- `build_rfc7_scoped_values_successor.py --check`: pass. `--selftest`: 21
  fixtures, 0 failing. `record_rfc7_scoped_values_successor.py --selftest`:
  33 fixtures, 0 failing. `check_governance.py`: 31 OK, 21 WARN, 0 FAIL.
- Mutations in the archive copy: (M1) change "other than" to "including" in the
  package patch only: builder reports "lane B contract patch and this
  package's patch give different module bytes" (caught). (M2) delete the
  freshness-visible sentence from both patches without regenerating the
  manifest: "manifest differs from exact regeneration" (caught). Neither
  predicate judges meaning: with both patches and the manifest changed in
  step, the builder would pass any text, which is expected for a byte
  builder and is why findings 1-2 are matters for a reviewer.
- Criterion 6: recorder `FROZEN_MANIFEST_SHA`, `REVIEW`, `REVIEW_SHA` are
  `None` (`scripts/record_rfc7_scoped_values_successor.py:79-81`); the packet
  says "not yet offered" and "No implementation is authorized"
  (`OWNER-DECISION-PACKET.md:12-14, 46`); no scoped-values act record exists in
  `decisions/`; `check_governance.py:2143` states the package is deliberately
  not a chain link. Criterion 6 holds.
- Criterion 4: the patch hunk touches one parenthetical and inserts one
  paragraph; the builder's heading, front-matter and clause-lead checks pass.
  Criterion 2: the exclusion "other than `non-citable` /
  `presentation-artifact`" is in the paragraph and the sub-clause below it is
  unchanged. Both hold.

## Findings

**Finding 1 — the interactive-surface definition licenses a lossy copy and leaves RFC7-33's closing sentence contradicted** (revise)
Evidence: patch lines 14-16 define the interactive surface as "the HTML page
as rendered for a human reader", excluding only the RFC6-13/14 endpoints and
"any plain-text or exported rendering"; patch lines 33-35 then say "an agent
or reader who needs a unit apart from its scope takes it from them, not from
a copy of the page". RFC7-33's closing sentence (module line 217-219, left
unqualified and after the parenthetical) still says a distinction
"does not survive ... a copy-paste into an agent prompt". Brief criterion 1
requires that no reading lets a scope substitute for a unit's own attribute
"on a copy taken out of the surface". A unit copied out of the page (a
selected row, a quoted claim, a page save) loses a scope-carried label,
freshness or draft state, and the new paragraph tells the consumer that this
is acceptable and to go elsewhere. That is the exact loss VIS-1/VIS-2 and the
RFC7-33 closing sentence guard against: an Unknown or stale unit, or one in a
draft-bearing band, becomes unmarked in the agent's prompt, and the agent is
not told to go anywhere because nothing travels with the copy. Two further
gaps in the definition: (a) the test is audience ("for a human reader"), not
delivery, so the identical HTML fetched by an agent from the page's own URL
is on its face still "the interactive surface"; (b) "exported" is undefined,
so whether a saved or printed page is an exported rendering is open.
Suggested repair: define the surface by delivery (the HTML document served
to a browser), make "exported" include any copy, save, print or fetch taken
from it, and either qualify RFC7-33's closing sentence the same way the first
sentence is qualified or require that a copy of any single unit carries its
expanded values (for example, each unit's text label restates the value).

**Finding 2 — no precedence rule between a scope and a unit's own attribute, and omission reads as inheritance** (revise)
Evidence: patch lines 21-24: "A unit under a scope then carries the value by
expansion, under an inheritance rule the governing specification states
once". The contract says only that a scope must never carry a value that is
not every unit's value (patch line 24-25). It does not say that a unit's own
attribute prevails, that a unit carrying its own differing value voids the
scope, or that a unit whose attribute is missing is not filled from the
scope. Under the contract as written, a spec could lawfully say that the
scope wins, or that a unit with no evidence and therefore no attribute takes
the scope's positive value, which is the VIS-2 failure (no evidence reads as
Unknown, never as inherited green). Lane B's delta states the safe rule
(SEMANTIC-DELTA.md, "nearest enclosing scope ... a claim under no such scope
leaves the field absent", and the `scope-hidden` falsifier), so the safety
lives in the behavior amendment while the contract that is supposed to bound
that amendment does not require it. The package's own premise is that the
contract permission is the outer limit; as drafted, the limit is wider than
the use lane B makes of it. Suggested repair: add one sentence that a scope
never overrides or fills in for a unit's own attribute and that a unit
lacking the distinction under a scope is a mismatch the scope may not cover
(absence is not a value).

**Finding 3 — evaluation identity and RFC7-16: agreement holds but rests on an unstated reading** (note)
Evidence: patch line 19-21 says the permission "includes the evaluation
identity RFC7-16 requires", but RFC7-33's enumerated list (module lines
205-212) does not name evaluation identity; it is a RFC7-16 field
(`narrative-contract.md:348-355`, "with its evaluation identity", per
capability or major claim). The paragraph's reading (identity is a
distinction of RFC7-33's "every distinction this package draws") is
reasonable and matches the lane B delta, which relies on exactly this and
reserves patching RFC7-16 "should a reviewer read its per-claim floor as a
per-element floor" (SEMANTIC-DELTA.md lines 459-463). That reservation is
not discharged in the successor packet, which states neither that RFC7-16 is
unchanged nor that it was read. The freshness clause also cites RFC7-16 for
"stays visible on the page itself", which matches RFC7-16's "staleness is
visible on the narrative page itself". Everything lane B's delta relies on
(scope as one element, text on the scope element, claim identity never
carried) is stricter than what this paragraph permits, so no reliance
exceeds the permission. Suggested: say in the packet's "What it does not
change" that RFC7-16 is read, and left unchanged, as a per-unit floor met by
expansion.

**Finding 4 — parenthetical placement** (note)
Evidence: patch lines 9-10 put "(except as the interactive-surface paragraph
below permits)" after "attribute on the rendered unit" and before "served
identically through the machine-queryable endpoints ... and preserved in
plain-text or exported renderings". Read alone, the exception could be taken
to cover the whole sentence including the endpoints. The paragraph's own last
sentences exclude the endpoints, so the contract is coherent, but the
parenthetical could be bound to the first limb only. Note only.
