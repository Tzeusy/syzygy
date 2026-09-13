# R-PWB-SCOPED-ATTRIBUTES-DELTA-3 — raw reviewer output

Reviewed commit: `4f41bcfd1904b5e059a61abb6b3c219f88ba10c8`
(worktree `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/laneb`, branch `agent/syzygy-dov.17`)
Behavior manifest SHA-256 (computed this session by `sha256sum`):
`fc644d010ebfb02351e5e84d2c382d004f5e4f96884959dc407656cb66a0ac9b`
Date: 2026-09-14

Review class: third fresh-context semantic review of a normative delta
(CC-REV-4, CC-REV-6). Reviewer was given the reviewed commit, the package's
`REVIEW-BRIEF.md` and the governing references, read-only. No file in the
worktree was created, edited or staged; `git status --short` is empty at the
end of this review. All post-apply inspection was done in scratch copies
under `.../scratchpad/laneb-r3-scratch` and `.../scratchpad/laneb-r3-mut`.

---

## 0. What I ran, and what it returned

Every figure below was produced this session against the reviewed commit.

**Package mechanics**

| command | output (read, not exit code) |
|---|---|
| `python3 scripts/build_pwb_scoped_attributes_amendment.py --check` | `PWB scoped-attributes amendment manifest matches 11 proposed behavior subjects (3 patched, 8 unchanged); the contract patch applies to both identical RFC-0007 mirrors` |
| `... --selftest` | `selftest: closed population, byte drift, path order, subject drift, patch corruption, contract mirror drift and contract patch corruption fail closed` |
| `... --diff` | 217 lines, four `diff --git` headers (the three behavior patches and the contract patch) |
| `python3 scripts/check_governance.py` | `32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted` |
| `python3 scripts/check_governance.py --selftest` | `255 fixtures, 0 failing` |

**Manifest verified by script, not by the builder.** I recomputed all eleven
rows independently: `git archive HEAD` into a scratch tree, applied the three
behavior patches with `git apply`, then `sha256sum` per row. All eleven rows
equal the post-apply bytes. Against the *unpatched* tree exactly 8 rows match
and 3 differ (`GOVERNING-DEPENDENCIES.md`, `design.md`,
`specs/polaris-project-wide-butlers-model/spec.md`), which is the split the
delta and packet state. The `GOVERNING-DEPENDENCIES.md` patch's stated source
digest `3db0a03ce74757eff0262d03d8c5ef1a3ce3fe20a6543138ff9d84cc3280ccf8`
equals the manifest's `spec.md` row, so the two are self-consistent.

**Baseline stability.** `git diff --name-only a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d..HEAD` over the eleven
behavior subjects, `contracts/rfcs/RFC-0007/` and
`contracts/candidates/rfcs/RFC-0007/` returns **nothing**. The delta's claim
that the patches apply at both the baseline and this commit holds.

**Mirror identity.** `diff` of `contracts/rfcs/RFC-0007/rendering-and-surface.md`
against `contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md` is empty
before the patch, and empty again after applying the patch (path-rewritten) to
both. The delta's "applies identically to both mirrors" holds.

**Fail-closed, by mutation (verification rule 6), in scratch copies**

- One byte changed in the manifest's first row → `--check` prints
  `PWB scoped-attributes amendment manifest does not verify: manifest differs
  from exact regeneration over the proposed bytes`.
- One byte changed in the packet's copy of the phrase argument →
  `check_governance.py` reports `FAIL CG-7d ... 57 quotations examined, 1
  finding` and `FAIL CG-7e ... 33 files examined, 1 finding`. The ledger's
  "a stale copy of its argument fails CG-7d and CG-7e before the act exists"
  is confirmed.
- Bare run → `refusing: regenerating the manifest changes the act argument;
  pass --write ...` (exit 2). `--apply` without `--at-adoption` → `refusing:
  --apply writes the proposed bytes into the tree and is the adoption step ...`
  (exit 2). Review 1 F20's disposition holds.

**The in-place trial the delta records under "Baseline".** Reproduced exactly:
with the spec, design and contract patches applied in a scratch copy,
`check_governance.py` reports `FAIL CG-7a ... 1 finding`, `FAIL CG-7h ... 9
findings`, `FAIL CG-18 ... 2 findings` (29 OK, 20 WARN, 3 FAIL), and
`python3 scripts/build_polaris_project_wide_contract_coverage.py --check`
still prints `Polaris consequence matrix matches regeneration — 324 clauses
represented`. `build_directive_register.py --check` prints
`FAIL: DIRECTIVE-REGISTER.md is stale; regenerate it`, and
`build_polaris_project_wide_spec_dependencies.py --check` prints
`Polaris dependencies match regeneration — 17 requirement(s)`. Every
[Observed] parenthetical in the delta and ledger about the post-apply battery
that I could test is accurate, with the one exception at F4 below.

**The three counts, re-derived by two methods (verification rules 2, 4, 9)**

Population: `git ls-files -z` at the reviewed commit = **1,228** tracked
files (four are PNGs and decode to no text; they match nothing and are
enumerated here rather than dropped silently).

| sweep | Python `re` over every tracked file | `git grep -l -F`, union | ledger |
|---|---|---|---|
| `PWB-REQ-0(?:07\|14)\b\|PWB-REQ-020\b` | 89 | 89 | 89 ✓ |
| `RFC7-33\b` | 78 | 78 | 78 ✓ |
| `rfcs/RFC-0007/rendering-and-surface.md` | 48 | 48 | 48 ✓ |

Set equality, not just cardinality: the two methods return *identical sets*
for all three sweeps (symmetric difference empty in every case).

At the baseline commit `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d`
(`git ls-tree -r`, **1,216** files) the PWB sweep returns **80**, and that set
is exactly the 80 rows of the ledger's "Every citing file" table. The 9 files
enumerated as additions at the draft commit are exactly the set difference
89 − 80, with no overlap with the table and no remainder in either direction.

Beyond the stated counts I checked the ledger's *contents*:

- Every one of the 240 per-file occurrence numbers in the 80-row table
  (007 / 014 / 020 columns) matches a fresh `re.findall` count at the
  baseline commit. **Zero mismatches.**
- The class table's twelve rows (6/3/1/8/9/1/5/23/17/3/3/1) sum to 80 and
  match the per-row class assignments exactly.
- The RFC7-33 class table's fifteen rows sum to 78 and match the 78-row file
  table's class assignments exactly.
- The path list is 48 distinct paths and equals the sweep set.

This is the most exactly re-derivable ledger I have checked in this corpus,
and reviews 1 F13 and 2 F1/F2 are discharged. One verification *sentence* in
it does not survive its own predicate — F3 below.

---

## Findings

### F1 — blocking — the 350 KB estimate is the residue of a model this package rejects, and says only that it is unmeasured

`OWNER-DECISION-PACKET.md:88-92`:

> Estimated saving on the pre-lane-A capture: about 350 KB (roughly 50 KB
> evaluation identity and 300 KB tuple fields; the 100 KB attribute share
> the funnel counted is no longer in scope) [Inferred — the funnel estimate
> minus its attribute share; the lane A page has not been measured with
> scopes, and the number is confirmed only by the implementation bead's
> measurement].

`SEMANTIC-DELTA.md:87-91` states the same derivation.

The subtrahend and the minuend both come from `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md:201-203`:

> Saving on the capture: about 49.6 KB (evaluation id), about 300 KB (tuples
> of the rows whose tuple equals the table's), about 100 KB (flags); together
> roughly 450 KB and about a third of the per-item slope.

The 300 KB component is explicitly *per row* — "tuples of the rows whose
tuple equals the table's" — because the funnel's lane B design permitted a
member to override its scope. `POLARIS-M1-PAGE-SIZE-FUNNEL.md:186-188`:

> rendered once beside the table caption as "N of N items: Observed ·
> report-fact · fresh · unchallenged", with the per-row span kept only for
> rows whose tuple differs;

This package rejects that model. `proposed/design.md.patch` decision 9:

> Rejected: an inheritance rule known only to the renderer; scopes that carry
> a majority value with members overriding it (a population-level assertion
> false for a member, with no epistemic status of its own)

and `proposed/spec.md.patch` makes it a falsifier:

> a scope carries a field for which any claim under it has a different value
> in the machine answer (an over-asserting scope)

Under the strict rule a *single* differing claim removes the hoist for that
field across the whole scope; under the funnel's model that claim merely kept
its own span while every other row still saved. The two models do not produce
the same number over the same page, and the difference is one-directional:
the strict rule can only save less. The arithmetic 450 − 100 = 350 silently
carries the looser model's denominator forward.

This is not hypothetical for the observed subject. The known Butlers data
quirks at the measured head place whole-source Unknown items, a grammar
failure and withheld active content inside the item classes that the lane A
record counts (`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`,
`invariants/compactListClasses`: 87 / 6 / 32 / 192 / 7 = 324 items in five
classes). A single Unknown label inside the 192-item class disables the label
hoist for all 192 under the strict rule.

The [Inferred] labels are present and the packet does carry the conditional
"if the implementation bead measures materially less, (a) does not reach the
target either and the target question returns to you". But "unmeasured" and
"computed under a rule this package forbids" are different epistemic
statements, and only the first is disclosed. The owner is being asked to
choose direction, and the packet recommends (a) as "the only path that meets
the target you set without cutting items"; that recommendation rests on a
number whose provenance is misdescribed.

**Resolution:** state in the packet and the delta that the 300 KB component
was computed per row under the funnel's override model, that the strict rule
forbids that model and can only save less, and that the residual is therefore
an upper bound rather than a point estimate — or re-derive the component
under the strict rule (per *field per class*: a field is hoisted for a class
only if all its items share the value) from the retained lane A capture, and
label the new figure.

### F2 — blocking — the delta routes the reader to an unbannered funnel section and claims a staleness note that does not cover it

`SEMANTIC-DELTA.md:397-400`:

> - `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` §"Lane B" and §"Draft
>   semantic delta" — the sketch this delta finalizes and the saving estimate
>   [Inferred]; the funnel's superseded note says which parts this package
>   dropped.

The funnel's superseded note is at `POLARIS-M1-PAGE-SIZE-FUNNEL.md:236-245`,
under the heading `### Draft semantic delta — scoped epistemic attributes on
the human channel` (line 234). The *other* cited section, `### Lane B (spec
amendment; the 2026-09-05 shape)` at line 178, running to line 207, carries no
staleness mark of any kind — and it is the section that holds the 450 KB
breakdown F1 depends on. Two of its statements are contradicted by the
reviewed package:

- line 188, the per-row override quoted in F1, which decision 9 rejects;
- lines 198-199: "A build-time assertion fails the render if one page carries
  two distinct evaluation ids, so the hoist cannot go stale silently" — the
  prohibition review 1 F4 found undisclosed and the package removed
  ("Removed; evaluation identity follows the same rule as every field and
  nothing fails to render", `SEMANTIC-DELTA.md:506-507`).

And the note that does exist names only one drop: "the package leaves
PWB-REQ-014 unchanged and carries an RFC7-33 contract delta for the tuple
fields; the saving below is overstated by the attribute share for that
reason." It does not say the remaining saving is overstated for the *second*
reason, nor that the render assertion is gone. So the sentence at
`SEMANTIC-DELTA.md:399` is false as written about §"Lane B", and it is the
mechanism by which F1 stays invisible to a reader who follows the citation.

This is the corpus's own recorded failure mode: a banner that sits somewhere
on the page while a specific false sentence stands elsewhere, and a page that
restates state it does not own going stale silently.

**Resolution:** mark the two superseded sentences *at the sentences*, inside
§"Lane B", keeping the original text quoted and dated, and correct
`SEMANTIC-DELTA.md:399` to say which section carries the note and which parts
of §"Lane B" the package dropped.

### F3 — blocking — a verification sentence in the ledger returns six times its stated population

`IMPACT-LEDGER.md:198-201`:

> None quotes the paragraph the patch inserts (the paragraph is new);
> RFC7-33's opening sentence gains a parenthetical and no citer quotes that
> sentence in full, verified by `grep -F "on the rendered unit**, served
> identically"` over the same population, which returns only the module and
> its mirror.

I ran that exact command over that exact population. It returns **12** files,
not 2:

```
.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md
.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md
.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch
.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md
.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-60-capability-1-outline-exercise-RAW.md
.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md
docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json
docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json
docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json
docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json
docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json
docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md
```

Six of these are outside this package. The five `polaris-generator-rfc7-coverage-*`
records carry RFC7-33's **entire current clause text verbatim** in a
`sourceText` field, and `round-2026-08g/reviews/RD-60-capability-1-outline-exercise-RAW.md:58`
quotes the fragment inside a table row. So both halves of the sentence are
false: citers do quote the opening sentence in full, and the grep does not
return only the module and its mirror.

The *disposition* is unaffected — I checked, and no script reads those
records (`git grep -l -F polaris-generator-rfc7-coverage` returns only design
notes, sibling evidence, pursuit data and retained reviews, no `scripts/`,
`apps/`, `packages/` or workflow citer), and the ledger already classes them
correctly as "evidence record | 6 | frozen evidence; never edited" and
"retained review". The defect is the verification sentence itself. In a
ledger whose entire value is that its figures are re-derivable, a sentence
that does not survive its own stated predicate is worse than no sentence —
this is exactly the class of error reviews 1 F13 and 2 F1/F2 found, in the
one place this draft did not re-derive.

**Resolution:** replace the sentence with what the sweep actually returns —
twelve files, of which six are this package's own and six are frozen evidence
and retained reviews that quote the pre-amendment clause as history and are
never edited (CC-REV-6) — and say plainly that after a performed contract act
those six carry a superseded quotation, which is history, not drift.

### F4 — non-blocking — the register line shift is seventeen, not fifteen

`SEMANTIC-DELTA.md:455-457`:

> `ACTIVE-CONTRACT-MANIFEST.txt`
> (CG-7a, the module's digest row), `DIRECTIVE-REGISTER.md` (every
> RFC-0007 clause after the insert point moves by fifteen lines) and

The contract patch's hunk header is `@@ -209,13 +209,30 @@`, a net of +17
lines. Measured post-apply in a scratch copy: `RFC7-34` moves from line 241 to
line **258**, and `RFC7-33`'s own definition line stays at 205. So the figure
is wrong by two. The plan's substance (the register must be regenerated) is
right; only the number is wrong, and a reader who uses it to sanity-check a
regenerated register would reject a correct one.

**Resolution:** "moves by seventeen lines", or drop the number and keep
"moves".

### F5 — non-blocking — PWB-REQ-007's Oracle and Case bullets do not cover two of the three new falsifier limbs

The amended falsifier (`proposed/spec.md.patch`) adds three predicates:

> a claim's expanded value for any field differs from the value the machine
> answer carries for that claim (a scope value hiding a differing member), a
> scope carries a field for which any claim under it has a different value in
> the machine answer (an over-asserting scope), a scope value has no text on
> the scope element,

The amended Oracle bullet's decision sentence is:

> zero invalid, missing, folded or scope-hidden values decides.

`scope-hidden` is there; the **over-asserting scope** and the **missing scope
text** are not, in either the Oracle bullet or the unpatched Case (sweep),
which still reads "including fixtures for every admitted label, tier, reason,
freshness, challenge and sibling state plus out-of-vocabulary and
missing-currency cases" and mentions no scoped case at all. PWB-REQ-020 got
the symmetric treatment done properly — its Case gains "expanding scopes",
its Oracle gains its own expansion, and its Mutation proof names both new
mutant classes — so the asymmetry looks like an oversight rather than a
decision.

This matters under CC-TEST-6 (`policies/craft-and-care/testing-and-verification.md:121-130`):

> Every status-rendering or evidence-consuming feature ships tests for its
> no-data branches ... Happy-path-only coverage of an epistemic surface is a
> finding under canonical test-rigor rule 3, at elevated severity: for this
> product the failure mode of the empty branch is *lying*.

The first no-data branch this amendment creates is an Unknown claim under a
scope carrying a positive value, and PWB-REQ-007's Case requires no fixture
for it.

**Resolution:** extend PWB-REQ-007's Case (sweep) with scoped fixtures
including an Unknown member and an over-asserting scope, and extend the
Oracle's "decides" sentence to the full falsifier set.

### F6 — non-blocking — the P-68 register row is one review behind, and the section banner above it is not

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:194`, the P-68 row's
owning-record column:

> `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md` (review 1, REVISE) and
> the second review's raw when it lands

The second review's raw has landed:
`docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md` is tracked at this
commit and its nine findings are dispositioned at `SEMANTIC-DELTA.md:551-588`.
The row contradicts the 2026-09-14 banner twelve lines above it
(`PENDING-OWNER-DECISIONS.md:110-112`: "its first two fresh-context reviews
returned REVISE and the repaired draft awaits a third"), which is correct.

Two smaller inaccuracies in the same row: it describes the new falsifier as
"a `scope-hidden` falsifier", singular, where the package now carries
`scope-hidden`, `over-asserting-scope` and the scope-text predicate; and it
does not mention the non-visual text obligation the package added in round 3,
which is the change a reader of the row would most want to know about.

The row's arithmetic is sound: I re-derived the register counts under the
file's own stated corrected predicate (split on `## ` headings; first cell
`P-` followed by anything but a cell break) and get 5 acceptance-act rows and
**22** open rows, 27 in all, including `P-25(c)` — exactly what
`PENDING-OWNER-DECISIONS.md:113-115` claims.

**Resolution:** name the second raw in the row, and note the third is
outstanding; widen "a `scope-hidden` falsifier" to the three predicates.

### F7 — non-blocking — decision 9 puts an obligation on PWB-REQ-016's oracle that PWB-REQ-016 does not carry

`proposed/design.md.patch`, decision 9:

> the accessibility-tree oracle expands scopes like every other.

`SEMANTIC-DELTA.md:361-362` says the same: "PWB-REQ-016's oracle therefore
expands scopes like every other oracle, with its own statement of the rule".

PWB-REQ-016 is deliberately not patched (`SEMANTIC-DELTA.md:318-320`, and
criterion 6 requires it untouched), so its Oracle bullet still reads, whole:

> - **Oracle**: compare the complete interactive/path population to keyboard
>   and accessibility-tree traces, then apply PWB-REQ-021's prompt oracle.

`design.md` is a manifest row and is bound by the behavior act, so after
adoption the package contains a bound statement about how an unamended
requirement's oracle behaves, sourced nowhere in that requirement. The
package's own standard, applied to PWB-REQ-020, was to write expansion into
the clause rather than assert it beside the clause.

**Resolution:** either amend PWB-REQ-016's Oracle bullet (which makes it a
fourth patched subject and changes the manifest), or rewrite decision 9 and
the delta to say that the PWB-REQ-007 scope-text falsifier is what obliges
the accessibility checker, and that PWB-REQ-016's own oracle is unchanged.

### F8 — non-blocking — RFC7-16 is warranted on and asserted satisfied, never quoted (verification rule 8)

`SEMANTIC-DELTA.md:380` warrants on RFC7-16 ("evaluation identity on every
claim, restored by expansion") and `SEMANTIC-DELTA.md:305-308` lists it under
"What explicitly does NOT change". PWB-REQ-007's own warrant block names it
(`spec.md` yaml, `contracts: [... RFC6-14, RFC6-17, RFC7-16, RFC7-33]`). The
clause is never quoted anywhere in the package, and the amendment's
lawfulness against it is asserted, not argued.

The clause text (`contracts/rfcs/RFC-0007/narrative-contract.md:316-324`):

> **RFC7-16 — Status in the narrative: minimal by default (SDR-17).** Every
> rendered status is kernel-computed at an identified evaluation and carries
> the label + tier + reason + freshness vocabulary **verbatim** (RFC6-14);
> ... Default density is minimal: per capability or major claim, one
> epistemic state — **its label with its RFC2-25 tier**, and its freshness —
> with its evaluation identity and a drawer/Trajectory handoff;

On my reading this survives: "carries the vocabulary verbatim" is a fidelity
requirement pointing at RFC6-14's closed vocabulary, not a locus requirement,
and "default density is minimal ... no metric walls, trends, counts" is a
ceiling. RFC7-33 was the locus clause, and it is patched. But that is a
reviewer's reading of a clause the package never put on the page, and
"per ... major claim, one epistemic state — its label with its RFC2-25 tier,
and its freshness — with its evaluation identity" is close enough to a
per-claim floor that it deserves the same treatment PWB-REQ-016 and RFC7-34
got in round 3. The cost of being wrong here is a CC-REV-2 violation at the
contract act (`policies/craft-and-care/review-and-documentation.md:52-58`:
"A change that invalidates any authoritative artifact updates **every**
invalidated authoritative artifact in the same logical change"), and the
funnel's conflict check — which asserted the same thing at
`POLARIS-M1-PAGE-SIZE-FUNNEL.md:132-133` — has a demonstrated false negative
on exactly this question: it missed RFC7-33 entirely, which is review 1 F1.

I also checked the other two warranted contract clauses and they are clean:
RFC6-22 (`RFC-0006-cross-surface-selection-query-drawer.md:390-402`) says
"Equivalence is over *semantics and query results*, never over pixels", and
RFC6-23 (lines 404-413) forbids disagreement; expansion before comparison
satisfies both.

**Resolution:** quote RFC7-16 in the delta as PWB-REQ-016 and RFC7-34 are
quoted, and state why a scope-carried field does not violate it — or patch it
alongside RFC7-33.

### F9 — non-blocking — the contract permission is broader than the spec change it exists to make lawful

Criterion 5 asks whether the RFC7-33 patch is "the smallest change that makes
the spec text lawful". The inserted paragraph reads:

> On the interactive human surface only, a distinction other than
> `non-citable` / `presentation-artifact` whose value is the same for every
> unit under one enclosing element MAY be carried once on that element

RFC7-33's enumeration is much wider than the epistemic tuple PWB-REQ-007
needs: "claim-block kind (anchored / non-normative / labeled), the narrative
claim-block **type name** (below), band membership and its authority class,
curated-versus-computed provenance, adopted versus unadopted, editorial-draft
state, proposal-context membership, review state, RFC7-11(a)'s
**target-changed** state, label + tier + reason + freshness". The permission
as drafted reaches all of them minus two. It is a permission on an accepted
contract module governing every surface, granted by a package whose only
consumer is one spec's tuple fields.

There is a real guard — the paragraph requires "an inheritance rule the
governing specification states once and every oracle restates independently",
so no surface can take the permission without a spec clause of its own — and
the breadth is inferable from the packet's "excluding the `non-citable` /
`presentation-artifact` distinctions". But inferable is not stated, and the
delta's change class says only "the contract clause gains one permission
paragraph for the interactive surface", which reads narrower than the
paragraph is.

**Resolution:** either narrow the paragraph to the distinctions a governing
specification designates for scoping, or say in the delta's change class and
the packet that the permission reaches every RFC7-33 distinction except the
two named, so the owner is ruling on that breadth knowingly.

### F10 — non-blocking — the Unknown resolution route has no stated locus under scoping

PWB-REQ-007's unamended prose requires:

> Unknown reasons SHALL use RFC2-24 values verbatim and expose their
> resolution routes.

and the amended falsifier keeps "a reason has no route". The amendment makes
"exactly one primary reason" a scopeable tuple field, but says nothing about
the route attached to it. A route is a per-claim navigable target, not a
value: two Unknown claims can share the reason `no-current-evidence` and
still resolve through different sources. If the reason hoists to the scope
and the route does not, one field is split across two carriers with no rule
saying so; if the route hoists too, two claims are given one resolution
target.

Nothing in the amended text decides it, and the criterion-2 floor ("no field
is dropped from any claim in any channel") is stated over *fields*, which is
where the ambiguity lives.

**Resolution:** one sentence in the amended paragraph — the resolution route
stays on the claim even where its reason is scope-carried — plus the matching
falsifier limb.

### F11 — non-blocking — PWB-REQ-007 gains an RFC7-34 obligation without gaining RFC7-34 as a warrant

`SEMANTIC-DELTA.md:372` says "RFC7-34 is added to the warrant list below",
and it is, in the delta's own Warrant section. PWB-REQ-007's warrant block in
`spec.md` is unchanged and does not name RFC7-34 or PWB-REQ-016, although the
new paragraph cites PWB-REQ-016 in its text and the scope-text falsifier is
the RFC7-34 obligation made concrete. I confirmed post-apply that
`build_polaris_project_wide_spec_dependencies.py --check` passes
(`Polaris dependencies match regeneration — 17 requirement(s)`) and that
`GOVERNING-DEPENDENCIES.md` still reports "17 requirement(s), 96 distinct
authorities" — because the warrants did not change. So the generated routing
table will not route a reader from RFC7-34 to PWB-REQ-007, which is the one
requirement that now carries a non-visual obligation in its falsifier.

The delta's "No warrant list changes" (`SEMANTIC-DELTA.md:28`) is accurate
about the patches; the question is whether it should be.

**Resolution:** add `RFC7-34` to PWB-REQ-007's `contracts:` warrant list and
regenerate `GOVERNING-DEPENDENCIES.md` (the builder already regenerates it and
the manifest row follows), or say in the delta why an obligation can live in a
requirement whose warrant list does not name its governing clause.

### F12 — non-blocking — the non-visual case is argued for linear reading only; anchored arrival is not addressed

The package's §"Non-visual recoverability" is a genuine improvement and its
central argument holds against the quoted clauses. RFC7-34
(`rendering-and-surface.md:241-243`):

> Every such distinction is recoverable **without colour, position, or
> layout** — by label, text, or structure;

Containment is structure, which RFC7-34 admits by name, and the scope's own
text is the label. PWB-REQ-016's first sentence
(`spec.md`, PWB-REQ-016) requires recovery "by text", and the scope text
supplies it. I judge criterion 10 met on the clause text.

What the section does not examine is arrival that is not linear. Polaris's
exact-source routes and per-claim anchors are a first-class navigation mode
(PWB-REQ-011), and a reader — sighted or not — who arrives at a claim's
anchor lands *inside* the scope, after its text. Under the current clauses
that reader gets the complete tuple on the claim's own element; after the
amendment they get the unscoped fields only, and must know to navigate
outward. The delta's sentence "a reader without vision meets each value once
where a sighted reader does" (`proposed/spec.md.patch`) is true of a reader
who reads the table from its caption and false of a reader who arrives at a
row. The packet's risk paragraph discloses the raw-HTML reader and the
screen-reader reader, not this one.

This is channel-neutral rather than a non-visual-specific regression, which
is why I do not raise it against criterion 10 — but it is a real change in
what a deep link delivers, and the owner is not told.

**Resolution:** one sentence in the packet's risk paragraph, and a note in
decision 9 that a scoped value is recovered by navigating to the enclosing
scope when a claim is reached by anchor rather than by reading.

### F13 — editorial — the packet labels its Inferred estimates and not its Observed measurements

`OWNER-DECISION-PACKET.md` carries three `[Inferred]` labels and zero
`[Observed]`, while stating measured figures throughout: "the Polaris page
went from 2,132,656 to 1,478,637 bytes (direct) and from 2,138,506 to
1,484,487 bytes (tailnet mount)" (lines 34-36), "about 612 KB of headroom"
and "78,637 / 84,487 bytes over" (lines 37-39), and option (b)'s whole
argument at lines 126-130 ("The lane A page sits about 612 KB under the
response ceiling, and the pending Butlers repairs add at most 443 KB, so a
working target of the ceiling minus that margin holds without any spec or
contract change").

I verified each: 2,097,152 − 1,484,487 = 612,665; 1,478,637 − 1,400,000 =
78,637; 1,484,487 − 1,400,000 = 84,487; 1,484,487 + 443,000 = 1,927,487,
inside the ceiling. The per-item figure is right too — the lane A record's
`perItemCost/afterCompactListEntry` is `count` 324, `meanBytes` 1486, and its
`followUp/laneB` names the 1,000-byte target, matching `SEMANTIC-DELTA.md:79-81`.
Every number is correct and sourced; they are simply unlabeled in the one
artifact written for the owner, where option (b) turns entirely on an
arithmetic claim carrying no label at all.

**Resolution:** label the measured figures `[Observed, <record>]` in the
packet as the delta does at its line 72.

### F14 — editorial — one patched line breaks the corpus's 78-column wrap

`proposed/design.md.patch` produces `design.md:295` at 102 characters:

> not have — beside its unchanged `collapsed` and `duplicated` falsifiers. PWB-REQ-014's non-authority

It is the only line the three behavior patches add that exceeds 78 columns
(checked by `awk length` over the patched regions of `design.md`, `spec.md`
and the contract module; the two long lines in `spec.md` at 484 and 498 and
the warrant line at 515 are pre-existing). It contains no code span, so it
does not risk the wrapped-citation failure mode, but it should be reflowed
before the bytes are frozen by an act.

**Resolution:** reflow decision 9's paragraph at 78 columns.

### F15 — editorial — two small structural points

- `IMPACT-LEDGER.md:41-42`: the nine-item enumeration of additions ends and
  `## Classes` begins with no blank line between them. It renders as a
  heading under CommonMark, so nothing is lost, but every other section in
  the file has the blank line.
- `proposed/contract/RFC-0007-rendering-and-surface.md.patch` carries only the
  `contracts/rfcs/` path in its `diff --git` header, and `--diff` prints it
  that way. A reader of `--diff` alone sees three behavior files and one
  contract file, not the two mirrors the builder actually checks. The delta
  says so in prose (`SEMANTIC-DELTA.md:250-251`); the artifact does not.

---

## Criteria, judged

| # | criterion | judgment |
|---|---|---|
| 1 | Contract: rule stated once, complete, no undetected divergence | **Met.** Stated once in PWB-REQ-007; nearest-enclosing, absent-is-a-falsifier, strict precondition, no claim identity, machine never inherits. I walked the nesting, override and multiplicity cases and found no rendering where an expanded tuple differs from the machine tuple without `scope-hidden` or `over-asserting-scope` firing. Strictness makes nested override unusable rather than ambiguous, which is the safe direction. |
| 2 | Unknown never stands in, folds, or drops | **Met** on the amended text; F10 is an unresolved locus question about the route attached to an Unknown reason, not a hole in the floor. |
| 3 | Independent oracles, own statement of the rule, finite falsifier, mutation class, both denominators | **Met** for PWB-REQ-020, whose Case, Oracle, Oracle-independence, Mutation proof and Falsifier all change coherently and keep "report both channel denominators for every run". Partially met for PWB-REQ-007 — see F5. |
| 4 | Parity: one tuple per claim, multiplicity, `collapsed`/`duplicated` intact | **Met.** Both clauses say the scope element contributes no tuple or marker after expansion; a collapsed pair still shows as `missing` against the machine multiset; the two old falsifier words keep their meanings and the delta's guardrail (parity is per tuple, never per id) is unaffected. |
| 5 | Contract delta smallest, both mirrors, non-citability intact, binds only by its own act | **Partially met.** Mirrors verified identical before and after; non-citability sub-clause untouched and explicitly excluded by name; "binds only by a separate contract act" stated in the delta, the packet, the P-68 row and the ledger's merge boundary. The opener's parenthetical is consistent — it attaches to "attribute on the rendered unit" and leaves the endpoint/export clause unqualified, which the inserted paragraph then restates — so the opener is no longer a false universal. Not smallest: F9. Possibly not sufficient: F8. |
| 6 | Unchanged boundaries, "does NOT change" list accurate | **Met, with F7 and F11.** Post-apply the spec still has the same 17 requirements with only line offsets moved; only PWB-REQ-007 and PWB-REQ-020 change; PWB-REQ-014's text, anchors, and PWB-REQ-011/015/016/021/022 are untouched; the machine-answer and tuple-vocabulary claims hold against the patch bytes. |
| 7 | Package mechanics, fail-closed, cannot bind by merge, seen by checks and CI | **Met.** All verified above by script and by mutation. The registry entry (`ACCEPTANCE-PHRASE-REGISTRY.yaml:44-49`), the existence-gated activation (`check_governance.py:2297-2313`, matching the truth-amendment precedent at 2316-2326), the successor-chain link (1585-1592), the two CI steps (`governance-docs.yml:112-116`) and the two battery lines are all in place, and CG-26 passes, so the battery and the workflow are one list. |
| 8 | Comprehension without author context | **Not met** — F1 and F2. I could restate the rule, the risks, the two-act path and the one choice from the package alone. I could not have discovered, from the package, that the headline saving was computed under a model the package rejects. |
| 9 | Owner packet: one decision, phrase present but not offered, silence performs nothing | **Met.** One direction question with (a)/(b)/(c), a stated default, "Silence, a partial answer, a commit or a merge performs nothing", "If you reply with this phrase now, no recorder exists that would accept it, and nothing is performed", and no authorization of any implementation. A scan for binding or accepting language across the four prose files returns nothing. |
| 10 | Non-visual recoverability against the quoted clauses | **Met** on the clause text, as argued at F12; the requirement is in the amended clause with its own falsifier, and `polaris-accessibility.ts` is marked **must** in the ledger. F12 is a disclosure gap, not a clause failure. |

## Dispositions from rounds 1 and 2, checked against these bytes

All twenty from review 1 and all nine from review 2 hold as recorded, with
two qualifications. Review 1 F13 and review 2 F1/F2 (the counts) are fully
discharged — I re-derived every figure by two methods and every enumeration
member-by-member. Review 1 F5 and F4, review 2 F4, F5, F7 and F8 are each
verifiable in the current bytes. The qualifications: review 2 F5's repair
named the three regenerated artifacts correctly but got the line shift wrong
(F4 above), and review 2 F3's repair is complete for the clause reading but
left decision 9 asserting an obligation on an unamended requirement's oracle
(F7 above).

## One note on the brief

`REVIEW-BRIEF.md:76` asks for "one exact verdict (`CONFIRM` or `REVISE`)".
The instruction under which I am working offers three, including
`CONFIRM WITH EXCEPTIONS`. I have used the three-valued set and state here
that under the package's own two-valued set my verdict would be `REVISE`,
so that no later reader has to infer which set I was answering in.

---

Verdict: REVISE

This draft is, mechanically, the best-verified package I have seen in this
corpus: every one of the three sweeps reproduces to the file under two
independent methods, the 240 per-file occurrence counts in the ledger are
exact, the manifest hashes the post-apply bytes of all eleven subjects when
computed without the builder, the mirrors are byte-identical before and
after, the builder and the governance checks fail closed under live mutation
of both the manifest and the packet's digest copy, and the in-place trial the
delta records reproduces finding-for-finding. The amended rule itself is
sound: strict inheritance admits no divergence between an expanded tuple and
a machine tuple without a named falsifier firing, Unknown cannot hide behind
a scope, the parity multiset keeps one tuple per claim, the RFC7-33 opener's
parenthetical is consistent with both the inserted paragraph and the
non-citability sub-clause, and nothing in the package binds, authorizes or
labels anything accepted. I return REVISE on three findings, and the first
two are one fault: the single number the owner's choice turns on — 350 KB —
is the residue of the funnel's per-row override model, which this package
explicitly rejects and replaces with a rule that can only save less, and the
delta's citation sends the reader to a funnel section that still states that
rejected model with no staleness mark while claiming a note covers it. The
package labels the estimate "unmeasured" when it is also "computed under a
superseded model", and an owner weighing (a) against (b) on that margin is
entitled to both facts. F3 is smaller in consequence but sits at the heart of
what this ledger is for: a verification sentence whose own stated grep
returns twelve files where it claims two. None of the three requires
rethinking the amendment — they are a re-derivation, two sentences and a set
of staleness marks — and the remaining twelve findings are refinements of an
argument that, on the clauses as written, holds.
