# R-PWB-SCOPED-ATTRIBUTES-DELTA-4 — raw reviewer output

Reviewed commit: `c2efa5196b92220be1073876e9f2400bc91ce43f`
(worktree `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/laneb`, branch `agent/syzygy-dov.17`)
Behavior manifest SHA-256 (computed this session by `sha256sum` over
`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`):
`66885051782236eb3ffce6991fc8589170b015d0363aa6bd5389b59f52f8f05b`
Date: 2026-09-14

Review class: fourth fresh-context semantic review of a normative delta
(CC-REV-4, CC-REV-6). Given the reviewed commit, the package's
`REVIEW-BRIEF.md` and the governing references, read-only. No file in the
worktree was created, edited or staged; `git status --porcelain` is empty at
the end of this review. All post-apply inspection was done in a scratch copy
under `.../scratchpad/rev4-apply`.

---

## 0. What I ran, and what it returned

Every figure below was produced this session against the reviewed commit.
Outputs are read, not exit codes (verification rule 4).

**Package mechanics**

| command | output |
|---|---|
| `python3 scripts/build_pwb_scoped_attributes_amendment.py --check` | `PWB scoped-attributes amendment manifest matches 11 proposed behavior subjects (3 patched, 8 unchanged); the contract patch applies to both identical RFC-0007 mirrors` |
| `... --selftest` | `selftest: closed population, byte drift, path order, subject drift, patch corruption, contract mirror drift and contract patch corruption fail closed` |
| `... --diff` | 248 stdout lines, four `diff --git` headers; stderr carries `note: the contract patch is applied to both mirrors: .syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md and .syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md` |
| `... ` (bare) | `refusing: regenerating the manifest changes the act argument; pass --write, then update every registered copy of the digest` (exit 2) |
| `... --apply` (no `--at-adoption`) | `refusing: --apply writes the proposed bytes into the tree and is the adoption step; pass --at-adoption in the change that records the act` (exit 2) |
| `python3 scripts/check_governance.py` | `32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted` |
| `python3 scripts/check_governance.py --selftest` | `255 fixtures, 0 failing — a check that cannot fail is not a check` |

**Manifest verified by script, independently of the builder** (verification
rule 3). `git archive HEAD` into a scratch tree; `git apply` of the three
behavior patches; `sha256sum` per row. All eleven manifest rows equal the
post-apply bytes, digit for digit. Against the unpatched tree exactly eight
rows match and three differ (`GOVERNING-DEPENDENCIES.md`, `design.md`,
`specs/polaris-project-wide-butlers-model/spec.md`) — the split the delta and
packet state. The `GOVERNING-DEPENDENCIES.md` patch's stated source digest
`723ec5b484f474aae6f34327de8ff8ba34abfb2e4023884e129ab53314a9129e` equals the
manifest's `spec.md` row, so the two are self-consistent. The manifest's
eleven subject paths are the same set as the performed 2026-09-05 amendment's
manifest (`pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`),
verified by sorted `diff`: no subject added or dropped.

**Post-apply generators.** In the scratch copy,
`build_polaris_project_wide_spec_dependencies.py --check` prints `Polaris
dependencies match regeneration — 17 requirement(s)` and
`build_polaris_project_wide_contract_coverage.py --check` prints `Polaris
consequence matrix matches regeneration — 324 clauses represented`. So the
patched `GOVERNING-DEPENDENCIES.md` bytes the manifest hashes *are* the exact
regeneration of the patched spec, not a hand edit.

**Baseline stability.** `git diff --name-only
a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d..HEAD` over the eleven behavior
subjects, `contracts/rfcs/RFC-0007/` and `contracts/candidates/rfcs/RFC-0007/`
returns nothing. `diff` of the accepted module against its candidate mirror is
empty before the patch; the path-rewritten patch applies cleanly to both and
they remain identical after. The delta's "applies at both / applies
identically to both mirrors" holds.

**In-place trial reproduced.** With the spec, design and contract patches
applied in the scratch copy, `check_governance.py` returns `28 OK, 21 WARN, 3
FAIL`: `FAIL CG-7a … 1 finding`, `FAIL CG-7h … 9 findings`, `FAIL CG-18 … 2
findings`. This matches the delta's `[Observed]` parenthetical at
`SEMANTIC-DELTA.md:66-70` exactly, including all three finding counts.

**The four counts, re-derived by two methods (verification rules 2, 4, 9)**

Population: `git ls-files -z` at the reviewed commit = **1,231** tracked
files. Four are PNGs under `docs/evidence/` that decode to no text
(`orrery-height-repaired-narrow-2026-09-09.png`,
`orrery-height-repaired-wide-2026-09-09.png`,
`polaris-existing-orrery-narrow-2026-09-09.png`,
`polaris-existing-orrery-wide-2026-09-09.png`); they match nothing and are
enumerated here rather than dropped silently.

| sweep | Python `re` over `git ls-files` | `git grep -l -F`, union | ledger |
|---|---|---|---|
| `PWB-REQ-0(?:07\|14)\b\|PWB-REQ-020\b` | 93 | 93 | 93 ✓ |
| `RFC7-33\b` | 81 | 81 | 81 ✓ |
| literal `on the rendered unit**, served identically` | 12 | 12 | 12 ✓ |
| `rfcs/RFC-0007/rendering-and-surface.md` | 49 | 49 | 49 ✓ |

Set equality, not only cardinality: the two methods return **identical sets**
for all four sweeps (symmetric difference empty in every case).

At the baseline `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` (`git ls-tree -r`,
**1,216** files) the PWB sweep returns **80**, and 93 − 80 is exactly the
thirteen files the ledger enumerates at lines 34-46, with **no removals in
either direction** and no member the ledger omits.

Beyond the stated counts I re-derived the ledger's contents:

- the 80-row "Every citing file" table: all 240 per-file occurrence numbers
  (007 / 014 / 020) recomputed at the baseline by `re.findall` — **zero
  mismatches**;
- class table 1: twelve rows summing to 80, and the per-row class assignments
  recomputed from the table agree with the declared counts exactly;
- class table 2: fifteen rows summing to 81, and the 81-row file table's
  class assignments agree exactly, set-equal to the `RFC7-33` sweep;
- the twelve-member literal list and the forty-nine-member path list are each
  set-equal to my own sweep.

Review 3's F3 (the sweep sentence that returned six times its stated
population) is discharged: `IMPACT-LEDGER.md:187-192` now states what the
sweep returns and enumerates all twelve with what each member is.

**Quote fidelity (verification rule 8).** Of the twelve fenced blocks in
`SEMANTIC-DELTA.md`, three are verbatim substrings of the current governing
sources (PWB-REQ-007/020 bullets in `spec.md`; RFC7-33's opening paragraph in
`contracts/rfcs/RFC-0007/rendering-and-surface.md`; RFC7-16 in
`contracts/rfcs/RFC-0007/narrative-contract.md`), two are verbatim but for the
fence's trailing newline (PWB-REQ-016's first sentence; RFC7-34's first
sentence), and the remaining six are verbatim substrings of the **post-apply**
bytes in my scratch copy. No block is a paraphrase presented as a quotation —
with the single exception at F5 below, which is prose, not a fenced block.

**Estimator, re-run on the retained captures.** Input digests match the
evidence record and the lane A record, which carries the same two hashes in
its `captures.after` block:

- `polaris-tailnet.html` 1,484,487 bytes, sha256
  `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`
- `polaris-direct.html` 1,478,637 bytes, sha256
  `2fecdd01e1a2ff577567495796ea7e59ab89f1420be6033e23314d26442ea094`

`python3 scripts/estimate_pwb_scoped_attributes_saving.py` reproduces the
record **field for field** on both captures and both modes: container mode
713 tuples, 10 scopes, attributeBytesRemoved 167,615, textBytesRemoved
25,397, scopeBytesAdded 3,464, netSavingBytes **189,548**; section mode
186,463; `hoistedPerField` identical (409/409/409/713/713/713/713). The
population cross-check holds by a second method: a regex count of
`<span class="claim-tuple"` and of `data-claim-id=` each returns 713 on both
captures, equal to the lane A record's figure. All seven tuple attributes are
present on all 713 spans, so no removal is fabricated against an absent
attribute. The projection arithmetic checks: 1,484,487 − 189,548 = 1,294,939;
1,400,000 − 1,294,939 = 105,061; 2,097,152 − 1,484,487 = 612,665; 1,478,637 −
1,400,000 = 78,637; 1,484,487 + 443,000 = 1,927,487, inside the ceiling by
169,665, and after the estimate 359,213.

**Wiring.** `ACCEPTANCE-PHRASE-REGISTRY.yaml:44-49` carries the phrase with
the manifest as subject and a note saying it is not offered;
`check_governance.py:2297-2313` carries the existence-gated activation beside
the truth-amendment precedent at 2316-2326; `governance-docs.yml:112-116`
carries the `--check` and `--selftest` steps; `PROJECT-STATUS.md:252-253`
carries the same two lines, and CG-26 passes (`28 published, 28 hosted, 28
shared`), so battery and workflow are one list.

**Boundaries.** Post-apply, the spec still has the same seventeen requirement
identifiers and exactly two of them differ from the current bytes:
**PWB-REQ-007** and **PWB-REQ-020**. PWB-REQ-011/014/015/016/021/022 are
byte-identical. The delta's "What explicitly does NOT change" list is accurate
against the patches. A sweep of the four package prose files for binding,
authorizing or accepting language returns one hit,
`OWNER-DECISION-PACKET.md:50` ("Both findings are accepted"), which is about
review findings, not about any artifact's status. Nothing in the package binds
anything, authorizes an implementation, or labels anything accepted.

---

## Judgments the brief asks for, before the findings

**The rule against criterion 1.** I walked the flat, nested, override,
empty-scope and multiplicity cases. Strict inheritance admits no rendering in
which a claim's expanded tuple differs from its machine tuple without a named
falsifier firing: a member that carries its own differing value defeats the
scope's precondition and fires `over-asserting-scope`; a scope value standing
over a differing member fires `scope-hidden`; a field carried by no enclosing
scope and not by the claim is "absent after expansion"; nested scopes cannot
disagree, because an outer scope carrying a field requires every claim beneath
it — including the inner scope's — to hold that value. Claim identity is
excluded by name, and both amended clauses say a scope contributes no tuple or
marker of its own after expansion, which keeps PWB-REQ-020's `collapsed` and
`duplicated` meanings and the per-tuple parity invariant intact. **Met.**

**PWB-REQ-016 and RFC7-34.** Quoted at their defined locations
(`DIRECTIVE-REGISTER.md` routes RFC7-34 to
`.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:241;
PWB-REQ-016 is in the PWB spec). RFC7-34: "Every such distinction is
recoverable **without colour, position, or layout** — by label, text, or
structure". PWB-REQ-016: "Every project distinction and summary-to-source path
SHALL be recoverable by text and operable by keyboard without relying on
color, position or layout." The amended PWB-REQ-007 requires the scope to
state every value it carries **as text on the scope element, in reading order
before the claims under it**, with "a scope value has no text on the scope
element" as a falsifier limb. Text at the scope satisfies PWB-REQ-016's "by
text"; containment satisfies RFC7-34's "structure", which the clause admits by
name; reading order is document order, which is neither position nor layout in
the clauses' sense. PWB-REQ-016's own Oracle bullet ("compare the complete
interactive/path population to keyboard and accessibility-tree traces, then
apply PWB-REQ-021's prompt oracle") and its Falsifier ("a color/layout-only
distinction, …") are unpatched and unchanged in meaning, and the delta is
correct that what obliges the accessibility checker is PWB-REQ-007's own
scope-text falsifier. **Met, and PWB-REQ-016's oracle is untouched.**

**RFC7-16.** Quoted verbatim in the delta from
`contracts/rfcs/RFC-0007/narrative-contract.md`:316. The argument is sound.
"carries the label + tier + reason + freshness vocabulary **verbatim**
(RFC6-14)" is fidelity to a closed vocabulary, not a locus rule — a scope
states the same closed words and expansion returns them. "per capability or
major claim, one epistemic state … with its evaluation identity" is a
completeness floor per claim, which expansion restores and "absent after
expansion" enforces. "Default density is minimal … no metric walls, trends,
counts" is a ceiling on what is shown, which stating a shared value once
respects rather than strains. The locus clause is RFC7-33, and it is the one
patched. The delta also states the fallback plainly (patch RFC7-16 beside
RFC7-33 in the same contract act if a reviewer reads its floor as per-element),
which is the honest disposal of a residual reading. **Sound.**

**CC-REV-2 and the two-act path.** CC-REV-2 is a *merge invariant*: "no merge
may leave mainline with an invalidated authoritative artifact still asserting
the old truth". Merging this candidate leaves nothing invalidated — the
manifest hashes bytes not in the tree, `--apply` refuses without
`--at-adoption`, and no script applies the contract patch. Between a performed
contract act and a performed behavior act, RFC7-33 carries an unused
permission while PWB-REQ-007 still forbids scoping; a permission nobody takes
is not an artifact asserting an old truth, and the package says exactly that
(`SEMANTIC-DELTA.md:570-572`, `OWNER-DECISION-PACKET.md:191-193`). **Sound.**

**The RFC7-33 opener's parenthetical.** The patch inserts "(except as the
interactive-surface paragraph below permits)" after "**machine-readable
attribute on the rendered unit**" and before "served identically through the
machine-queryable endpoints". So the exception qualifies the *locus* only and
leaves the endpoint/export obligation unqualified — which the inserted
paragraph then restates ("The machine-queryable endpoints and every plain-text
or exported rendering carry every distinction on the unit itself, unchanged by
this paragraph"). The inserted paragraph excludes `non-citable` /
`presentation-artifact` by name, so the "Non-citability travels, on every
rendering" sub-clause stands in full and is untouched by the patch (verified
byte-identical post-apply). **Consistent.** The breadth disclosure is accurate
and is now stated in two places rather than left inferable — the delta's change
class at lines 43-48 and `OWNER-DECISION-PACKET.md:75-80` both say the
permission reaches every RFC7-33 distinction except the two named, not only
the tuple fields, and the packet says "You are ruling on that breadth."

**The estimator against the rule it claims to implement.** The estimator is a
fair, mildly conservative model of one lawful implementation under the strict
rule, and its headline is not inflated by any modelling choice I could find
that exceeds ~1 KB on 189,548. It never permits a member to override a scope
(a field hoists only when `len({values}) == 1` over the members), it requires
more than one member, and it charges one scope-marker attribute, the hoisted
attributes once and a caption element per hoisting scope. It is conservative
in that it assigns each tuple to exactly one scope and never hoists a field
shared across a whole section to the section (the section mode it also reports
saves *less*, 186,463, because its coarser grouping loses hoists). Three
modelling gaps are small and are recorded as F3 and F4 below. Two properties I
checked and found clean: all seven attributes are physically present on all
713 spans, so nothing is charged against an absent attribute; and the page
carries exactly one distinct `data-evaluation-id`, so the evaluation-identity
hoist (50,623 of the 167,615 attribute bytes) is genuinely lawful under the
strict precondition rather than an artefact of grouping.

**Dispositions from reviews 1–3, checked against these bytes.** All twenty from
review 1, all nine from review 2 and all fifteen from review 3 hold as recorded
against the current bytes. Specifically for review 3: F1 re-derived (190 KB
figure, retained script, retained capture digests, funnel figure described as
an upper bound in the delta, packet, decision 9 and the P-68 row); F2 three
sentence-level marks now sit inside the funnel's §"Lane B" at lines 190-195,
209-212 and 218-223, each dated 2026-09-14, each keeping the original text in
place above it, and the delta's evidence bullet names which section carries
which mark; F3 repaired as described above; F4 "seventeen lines" now stated
and confirmed by the hunk header `@@ -209,13 +209,30 @@` (net +17); F5 the
Case gains five scoped fixtures and the Oracle's deciding sentence names every
limb; F6 the P-68 row names all three raws, says a fourth is outstanding, and
names the three predicates and the scope-text obligation; F7 decision 9 and the
delta now say PWB-REQ-007's scope-text falsifier obliges the checker and
PWB-REQ-016's oracle is unchanged; F8 RFC7-16 quoted and argued; F9 breadth
disclosed; F10 the route stays on the claim with a falsifier limb; F11
`RFC7-34` added to PWB-REQ-007's `contracts:` list with
`GOVERNING-DEPENDENCIES.md` regenerated and its `RFC7-34` row now reading
`PWB-REQ-007, PWB-REQ-016`; F12 anchored arrival addressed in the delta,
decision 9 and the packet's risk paragraph; F13 the packet's measured figures
now labeled `[Observed, …]` including option (b)'s arithmetic; F14 decision 9
reflowed (zero added lines over 78 columns in the design patch); F15 the blank
line is present before `## Classes` and `--diff` now names both mirror paths on
stderr; and the brief's verdict set is now three-valued.

---

## Findings

All six are non-blocking or editorial. None touches the rule, the manifest,
the counts or the owner's choice.

### F1 — non-blocking — PWB-REQ-007's own opening SHALL keeps an unmarked universal, the defect the package repaired in RFC7-33's opener

Post-apply, `spec.md:443-446` still reads, unchanged:

> Every project entity and project-fact claim SHALL have a stable semantic Claim
> identity plus an evaluation instance, be challengeable with resolvable support, and carry the
> closed label, tier, exactly one primary reason, zero or more closed secondary
> reasons, freshness, challenge state and evaluation identity that govern it.

and the new paragraph at `spec.md:453` creates the exception to it:

> In the human view, a tuple field whose value is the same for every claim
> under one enclosing scope MAY be carried once on that scope instead of on
> each claim.

This is the same shape review 2's F7 found in RFC7-33's opening sentence — an
unqualified universal above an exception — and the package repaired it *there*
by adding "(except as the interactive-surface paragraph below permits)" so
that "a reader who quotes only the opener (verification rule 8) sees that an
exception exists" (`SEMANTIC-DELTA.md:277-279`). The identical repair was not
applied to PWB-REQ-007's own opener. It is compounded by the delta's
presentation: §"Current meaning" at line 113 quotes only "the observable,
oracle, independence and falsifier bullets", so a reader of the delta never
sees the SHALL the new paragraph qualifies.

The reading is resolvable — the paragraph is inside the same requirement, and
the amended falsifier is stated over values "after expansion" — so this is a
clarity defect, not a hole. But the package's own standard, applied one clause
away, is higher.

**Resolution:** add a parenthetical or a "carried on the claim or by expansion
under the paragraph below" qualifier to PWB-REQ-007's opening SHALL in
`proposed/spec.md.patch` (it is a manifest subject, so the manifest and the
`GOVERNING-DEPENDENCIES.md` source digest follow), and quote the opening prose
in §"Current meaning" beside the bullets.

### F2 — non-blocking — three places route the implementation to one new mutant class where the amended PWB-REQ-020 mandates two

The amended PWB-REQ-020 Mutation proof (`proposed/spec.md.patch:125-129`)
requires both:

> changed, collapsed, wrong-evaluation, scope-hidden (a scope value that
> hides one member's differing value) and over-asserting-scope marker (a
> scope value one member does not have, the member carrying its own)

Three places in the package name only the first:

- `IMPACT-LEDGER.md:56` — "the sweep gains the scope-hidden mutant class";
- `IMPACT-LEDGER.md:182` — `pwb-mutation-sweep.ts` "gains the `scope-hidden`
  mutant per marker class … beside missing/duplicated/changed/collapsed/
  wrong-evaluation";
- `SEMANTIC-DELTA.md:566` — migration step 5: "the `scope-hidden` mutant class
  and a measurement in the lane A shape".

`design.md`'s decision 9 and the packet both name the pair correctly, so this
is drift between the clause and the package's own implementation route, not a
disagreement about the rule. It matters because the ledger's implementation-site
list and migration step 5 are what an implementation bead is scoped from: a
bead built from them would ship half the mutation obligation and the clause
would be unsatisfied at the first sweep. This is review 1 F5's defect class
(design prose naming the wrong falsifier) surviving in two other artifacts.

**Resolution:** name `over-asserting-scope` beside `scope-hidden` at all three
sites.

### F3 — non-blocking — the estimate's headline scope mode is stated as "nearest enclosing table or list" while 26 of the 713 tuples are hoisted onto a page-level pseudo-scope

`docs/evidence/pwb-laneb-strict-scope-estimate-2026-09-14.json:112`:

> "scopeMode": "container (nearest enclosing table or list)",

`scripts/estimate_pwb_scoped_attributes_saving.py:99` falls back to the string
`"body"` when a tuple has no `table`/`ul`/`ol`/`dl` ancestor, and that group is
then hoisted like any other. I instrumented the estimator: the container-mode
grouping is nine real containers plus one `body` group of **26** members, which
hoists `secondary-reasons`, `freshness`, `challenge-state` and
`evaluation-id` and contributes **4,930** of the 189,548 bytes (2.6 %). The
containers-only figure is **184,618**.

Those 26 claims are not contiguous — they are the claims that sit outside every
table and list, scattered across sections — so the implied scope element is the
page body, and "a scope SHALL state every value it carries as text … in reading
order before the claims under it" would put that text at the top of the page,
before unrelated content. Whether that is a scope a reasonable implementation
would build is a judgment the owner is not given, because the record's headline
does not say the group exists. The record's `"scopes": 10` reads as ten tables
or lists.

The consequence is 2.6 % of the headline and does not move the owner's
decision (184,618 still leaves the tailnet form at 1,299,869, about 100 KB
under the target).

**Resolution:** state in the record's headline, or in a `note`, that 26 of the
713 tuples fall under no table or list and are modelled under a single
page-level scope worth 4,930 bytes, and give the containers-only figure beside
the headline.

### F4 — non-blocking — the estimator charges scope text only for the four visible fields, where the amended rule says "every value it carries"

`scripts/estimate_pwb_scoped_attributes_saving.py:117`:

```
text_once = " · ".join(value[f] for f in FIELDS if f in TEXT_FIELDS and f in hoist)
```

`TEXT_FIELDS` is label, tier, freshness and challenge state. A scope that
hoists `data-epistemic-primary-reason`, `data-epistemic-secondary-reasons` or
`data-evaluation-id` is charged its attribute bytes but no text bytes, while
the amended PWB-REQ-007 says "A scope SHALL state **every value it carries** as
text on the scope element" and makes "a scope value has no text on the scope
element" a falsifier limb. The estimator therefore models a page that would fire
its own package's falsifier at every scope.

I costed it: adding the hoisted non-visible values as text (value plus a short
separator, per scope) is **606 bytes** across the ten scopes, 0.3 % of the
headline. The empty-valued case is the interesting one —
`data-epistemic-secondary-reasons` is `""` on all 713 spans, so its hoist
removes 25,668 bytes while carrying a value that has no text at all; an
implementation would have to write something like "no secondary reasons" once
per scope, which is tens of bytes, not thousands. So the direction of the error
is against the package (the estimate is ~0.3 % optimistic) and the magnitude is
immaterial.

**Resolution:** either charge the text for every hoisted field, or say in the
script's docstring and the record that the caption text is modelled for the
four visible fields only and that the omission is bounded at ~600 bytes.

### F5 — editorial — CC-REV-2 is paraphrased inside quotation marks

`SEMANTIC-DELTA.md:468-469`:

> so CC-REV-2 ("invalidated accepted contracts must be updated
> in the same logical change") is why the contract patch travels in this
> package

The clause at its defined location
(`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:52-58,
per `DIRECTIVE-REGISTER.md`:89) reads:

> A change that invalidates any authoritative artifact updates **every**
> invalidated authoritative artifact in the same logical change: behavioral
> specs (`openspec/`), declared topology, accepted contracts, and the policies
> in this cluster.

`grep -c -F` for the quoted string over that policy file returns **0**. The
paraphrase is faithful in substance and narrower in scope than the clause
(which reaches specs, topology and policies too), but it is the only place in
the package where quotation marks carry text that is not the source's, and the
artifact is one a behavior act would bind. The rest of the package quotes
scrupulously — every other quotation I tested is verbatim.

**Resolution:** quote the clause, or drop the quotation marks and paraphrase in
the delta's own voice.

### F6 — editorial — two small consistency points

- `SEMANTIC-DELTA.md:41-42` and `:466` say the change adds "one falsifier
  class" and that "the falsifier set grows by one class", while `:507` says
  "**scope-hidden** and **over-asserting-scope** name the new falsifier and
  mutant classes" (two) and PWB-REQ-007's amended falsifier gains four new
  limbs (scope-hidden, over-asserting-scope, no-scope-text, scope-carried
  reason without a route on the claim). In a delta whose change class exists to
  enumerate every change, the singular understates — review 1's F17 was the
  same complaint against the same section.
- `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`:197-198, inside §"Lane B", still
  states a third design element the package rejects, with no sentence-level
  mark: "`data-presentation-artifact` and `data-non-citable`, on the section
  that contains only presentation units." PWB-REQ-014 is not amended by this
  package (review 1 F1), so that bullet is superseded in the same way as the
  two bullets marked above and below it. The 450 KB mark at lines 218-223
  mentions in passing that "the 100 KB flag share left scope when PWB-REQ-014
  was dropped from the package", which discloses the consequence but not the
  design statement, and it sits five lines away from the bullet. Given the
  corpus's own lesson that a nearby note does not cover a specific standing
  sentence, the bullet should carry its own mark.

**Resolution:** say "two falsifier and mutant classes" (or enumerate the four
limbs) in both places; add a fourth sentence-level superseded mark at the
PWB-REQ-014 bullet in §"Lane B", dated and keeping the text.

---

## Criteria, judged

| # | criterion | judgment |
|---|---|---|
| 1 | Contract: rule stated once, complete, no undetected divergence | **Met.** Stated once in PWB-REQ-007; nearest-enclosing; absent is a falsifier; strict precondition over the machine answer; claim identity excluded; machine never inherits. No case I could construct diverges without `scope-hidden` or `over-asserting-scope` firing. F1 is a clarity defect against the requirement's own opener, not a hole. |
| 2 | Unknown never stands in, folds, or drops | **Met.** A scope carries a field only when every claim under it has that value in the machine answer, so a positive scope cannot cover an Unknown member; the Case now carries that exact fixture; the route stays on the claim with its own falsifier limb; "absent after expansion" forbids dropping a field in any channel. |
| 3 | Independent oracles, own statement of the rule, finite falsifier, mutation class, both denominators | **Met.** Both clauses' Oracle-independence bullets say the expansion is the checker's own and import no rendering code; PWB-REQ-007's deciding sentence now names every limb and its Case carries five scoped fixtures; PWB-REQ-020's Mutation proof names both new classes and keeps "report both channel denominators for every run". F2 is drift in the package's implementation route, not in the clauses. |
| 4 | Parity: one tuple per claim, multiplicity, `collapsed`/`duplicated` intact | **Met.** Both clauses say the scope contributes no tuple or marker of its own after expansion; expansion precedes comparison; the two old falsifier words keep their meanings; the per-tuple (never per-id) parity invariant is unaffected. |
| 5 | Contract delta smallest, both mirrors, non-citability intact, binds only by its own act | **Met with the breadth disclosed.** Mirrors verified identical before and after; the sub-clause is byte-identical post-apply and excluded by name; the opener's parenthetical qualifies only the locus; "binds only by a separate contract act" is stated in the delta, the packet, the ledger's merge boundary and the P-68 row. It is deliberately *not* the smallest — review 3 F9's breadth is now stated rather than narrowed, and the packet puts that choice to the owner explicitly, which is the lawful disposal. |
| 6 | Unchanged boundaries, "does NOT change" list accurate | **Met.** Exactly two of seventeen requirements change post-apply; PWB-REQ-011/014/015/016/021/022 byte-identical; the machine-answer, tuple-vocabulary, RFC7-16 and anchor claims all hold against the patch bytes; one warrant list changes and the delta says so. |
| 7 | Package mechanics, fail-closed, cannot bind by merge, seen by checks and CI | **Met.** Manifest recomputed without the builder, all eleven rows exact; `--check`, `--selftest`, bare-run and `--apply` refusals all read; registry, activation, workflow and battery all present and CG-26 green; the merge boundary holds. |
| 8 | Comprehension without author context | **Met.** From the package alone I could restate the rule, its two new falsifier classes, the saving and how it was derived, the risks (raw-HTML reader, screen-reader reader, deep-link arrival), the two-act path and the one choice. The headline figure's provenance — the defect that failed this criterion in round 3 — is now derivable end to end from a retained script over hash-named retained captures. |
| 9 | Owner packet: one decision, phrase present but not offered, silence performs nothing | **Met.** One direction question with (a)/(b)/(c) and a stated default; "Silence, a partial answer, a commit or a merge performs nothing"; "If you reply with this phrase now, no recorder exists that would accept it, and nothing is performed"; no implementation authorized. |
| 10 | Non-visual recoverability against the quoted clauses | **Met.** Argued above against the quoted PWB-REQ-016 and RFC7-34; the obligation is in the amended clause with its own falsifier; `polaris-accessibility.ts` is marked **must** in the ledger; anchored arrival is disclosed in three places. |
| 11 | Saving figure derived under the package's own rule, from a named capture, by a retained script, labeled, funnel figure marked superseded | **Met.** Reproduced field for field this session from captures whose digests match both the evidence record and the previously reviewed lane A record; labeled `[Inferred]` in the record, the delta, the packet, decision 9 and the P-68 row; three sentence-level marks in the funnel's §"Lane B", dated and text-preserving. F3 and F4 are precision gaps in the model's disclosure, bounded at about 2.9 % combined and in the conservative direction for F4. |

---

Verdict: CONFIRM WITH EXCEPTIONS

Every blocking finding of the third review is discharged against these bytes,
and discharged by re-derivation rather than by assertion: the headline saving
is no longer the residue of a rejected model but a figure I reproduced field
for field this session by re-running the retained script over captures whose
digests match both the evidence record and the lane A record it descends from;
the funnel's §"Lane B" now carries dated sentence-level marks at the two
statements the package contradicts, with the original text kept; and the
ledger's twelve-file sweep sentence states what its own predicate returns. The
mechanical work is exact and I could find no figure in it that does not
reproduce — four sweeps agreeing set-for-set under two independent methods over
1,231 tracked files, 240 per-file occurrence counts with zero mismatches, two
class tables summing and partitioning correctly, eleven manifest rows equal to
the post-apply bytes when computed without the builder, both RFC-0007 mirrors
identical before and after, the generated dependency and coverage artifacts
regenerating exactly from the patched spec, and the in-place trial reproducing
all three FAIL families with all three finding counts. The rule itself holds
against the clauses as written: strict inheritance admits no divergence without
a named falsifier, Unknown cannot hide behind a scope, the parity multiset keeps
one tuple per claim, the scope-text obligation answers PWB-REQ-016 and RFC7-34
without touching PWB-REQ-016's oracle, the RFC7-16 argument is sound and its
residual reading is disposed of honestly, the RFC7-33 opener's parenthetical
qualifies only the locus and leaves the non-citability sub-clause whole, and
nothing in the package binds, authorizes or labels anything accepted. My six
exceptions are all repairs of the package's own standard rather than of its
substance: one unmarked universal in PWB-REQ-007's opener that the package
already knew to mark in RFC7-33's, three places routing an implementation to
one new mutant class where the clause mandates two, two bounded disclosure gaps
in the estimator's model worth about 2.9 % of a figure that does not move the
owner's choice at either value, a paraphrase inside quotation marks, and two
counting and marking inconsistencies. None requires rethinking the amendment;
F2 is the one I would repair before an implementation bead is scoped, because
the ledger and migration step are what such a bead would be written from.
