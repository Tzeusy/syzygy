# R-PWB-OPENING-INDEX-AMENDMENT-1 — fresh-context review, PWB opening-index amendment (PWB-REQ-010), round 1
Reviewed commit: 0241fb835471af3a2ea23119959bdfa34ef14464
Manifest SHA-256: f39ba85671c3c428f0798fe9ecf752d09d54bf1a1217e3569b744c646b85c2eb
Verdict: REVISE

Package: `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`
(manifest `PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt`; the head digest above is
the sha256 of that file's bytes at the reviewed commit, computed by
`git show <commit>:<path> | sha256sum`). Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`. Reviewed in one round with the
accessible-name package; this raw judges package A only.

## Mechanics run (fresh clone at the reviewed commit)

[Observed] All from the clone root, exit codes and output read:

- `build_pwb_opening_index_amendment.py --check` — exit 0: "opening-index
  candidate matches 11 proposed subjects (2 patched); 17 requirements, 53
  scenarios; structure, regeneration, contract coverage, sibling
  classification and pending-sibling composition verify".
- `build_pwb_opening_index_amendment.py --selftest` — exit 0: "18 structure
  mutants, declaration tampering, patch drift, drifted composition and an
  unclassified sibling all fail closed on their own predicates". Each mutant's
  expected finding prefix is a predicate-specific string
  (`pwb_requirement_amendment.py:497`), so the per-predicate claim holds for
  the 18 declared mutants.
- `build_pwb_accessible_name_amendment.py --check` / `--selftest` — exit 0.
- `build_pwb_class_granular_extraction_amendment.py --check` — exit 0;
  `build_pwb_release_label_amendment.py --check` — exit 0.
- `check_governance.py` — "31 OK, 21 WARN, 0 FAIL (52 checks)".
- `check_spec_reconciliation.py --check` — "7 of 7 predicates without FAIL;
  PASS" (R6 WARN on the two stale behaviour-contract pins, pre-existing).
- Composition, independently: all 24 application orders of the four pending
  spec patches (class-granular, release-label, opening-index, accessible-name)
  apply with `git apply` and yield one identical result; all 12 ordered pairs
  apply.
- `git diff c371339d 0241fb83 -- openspec` is empty: no signed byte changes.
  Reading the patch, each of the five `replaced` lines survives as the prefix
  of its extended limb, and the warrants block is untouched.
- Impact-ledger census re-derived with the ledger's own published regex over
  the 2,006 paths at `c371339d`: 99 files cite PWB-REQ-010, and every area
  count in the table (31/20/25/5/6/1/3/6/1+1) reproduces.
- The index table's identity column equals PWB-REQ-021's nine identities in
  order (spec `PWB-REQ-021`, "Nine answers" limb), checked by eye and by the
  builder's `index_findings`.

Acceptance criterion 1 (no verdict, no score) and criterion 2 (scope) are met
as drafted: the patch says the index, offsets and stopping line "carry no
epistemic tuple, enter no PWB-REQ-020 parity family and no PWB-REQ-021 record
or readiness arm, and SHALL NOT state or imply that any prompt is, or can be,
answered" (`proposed/spec.md.patch:39-44`), targets are declared by a table,
and slices B and D are put to the owner with clause reasoning (packet
questions 6 and 7). The two revise findings are against criterion 3.

## Findings

**Finding 1 — The word-counting method is not a judgment-free procedure, and its `details` exclusion drops visible text** (revise)

Anchor: `proposed/spec.md.patch:34-38` and `:62-65`. The method reads: "a
word is a maximal run of non-whitespace characters in a rendered text node,
counted in document order from the start of the body, excluding the content
of `script` and `style` elements and of every `details` element closed on
first load." The oracle "applies the declared method to the served HTML".

CC-SPEC-4 requires an oracle that decides "by a stated procedure that
terminates in bounded effort, without judgment". Two independent counters
can apply this text in good faith and disagree, which makes the falsifier
limb "an offset or total differs from the independent count" undecidable:

- "rendered text node" is undefined: whether text under `hidden`,
  `display:none`, `aria-hidden`, `noscript`, `template` or visually-hidden
  skip-link styling counts is not stated.
- "the content of every `details` element closed on first load" includes its
  `<summary>`, whose text is on screen when the element is closed. That
  contradicts the delta's own rationale, "Counting it would make the offsets
  describe a page no reader sees on arrival" (`SEMANTIC-DELTA.md:116-119`):
  the visible toggle labels are part of what a reader sees.
- "served HTML" versus "closed on first load": the second is a runtime DOM
  state; served bytes and the post-script DOM can differ.
- "the word offset at which its target begins" does not say whether the
  offset is the count of words before the target's first element or the
  index of its first word (0- versus 1-based).

Repair direction: state the population over a named representation (served
HTML parsed without scripts, or the post-load DOM), list the excluded
elements and attributes exhaustively, say whether a closed `details`'
`summary` counts, and fix the offset base.

**Finding 2 — The stopping line has no falsifier limb for presence, uniqueness or placement, and its placement is ambiguous** (revise)

Anchor: `proposed/spec.md.patch:31-33` ("One stopping line SHALL follow the
last indexed target in document order and give the largest row offset and
the page's word total, and nothing else about the index"), the Observable at
`:58-59` ("followed by one stopping line"), and the Falsifier at `:71-79`.

The brief's criterion 3 requires "Each new obligation has an oracle limb, a
falsifier limb and a scenario." The Falsifier names only "the stopping line
states or implies that a prompt is answered" and the generic "an offset or
total differs from the independent count". It names no falsifying observation
for a missing stopping line, a second one, one placed elsewhere, or one whose
"largest row offset" is not the largest. The Oracle limb likewise checks
offsets and targets, not the line's position. "Follow the last indexed
target" is also ambiguous: after the first element of that target, which is
where its offset is measured, or after the target's whole extent, such as the
end of the capability catalog? Those are different positions on the page, and
nothing decides between them.

**Finding 3 — Index targets are prose descriptions; the independent oracle has no stated way to locate them** (note)

Anchor: `proposed/spec.md.patch:13-21` and `:64-65` ("each row's target is
compared with this requirement's table, never with the renderer's own
mapping"). Targets such as "the purpose statements", "the capability
catalog" and "the legend naming each epistemic label, tier and freshness
state" have no machine identity, and "routes to the first element of its
target" (`:23-24`) does not say which element is first: the group heading,
the first statement or the first anchored claim. [Inferred] The existing
oracle's "entity references against an independently enumerated
project-level fact set" can probably carry most rows. "The legend" and "the
first link, in document order, to an exact requirement's text" need a stated
recognizer. Separately, two targets are narrower than the identities they
index. `unknown-or-contradiction` routes only to "the opening Unknown
aggregate", so an evaluation with a contradiction and no Unknown shows that
row as not rendered. `refusals-and-rule` routes to "the non-goal statements",
while RFC7-30 asks the reader to name a non-goal "and reach its rule text"
(`rendering-and-surface.md:138-139`). Neither is a verdict problem, but the
owner may want to see them before signing.

**Finding 4 — Copy-role and narrative-unit fit of the new strings is asserted, not reconciled with PWB-REQ-012 and PWB-REQ-014** (note)

Anchor: `proposed/spec.md.patch:24-26` ("each offset and the stopping line is
a `scope-instruction` string; all of them obey PWB-REQ-012"). PWB-REQ-012's
Falsifier names "an extra scope/action instruction", and its text allows "At
most one entry `scope-instruction`" for the POC bound. Ten new
`scope-instruction` strings at the entry will need an implementer to argue
that limit applies only to POC-bound statements. That argument is reasonable,
but the amendment does not make it. The "says so" text of an unrendered row
(`:27-28`) is assigned no role. PWB-REQ-014 requires every owner-visible
narrative unit to carry "exactly one claim role", and its tree form makes
PWB-REQ-010's categories the top-level groups. Neither the delta nor the
ledger says whether the index is a narrative unit or a group, or sits outside
both. Packet question 5 surfaces the PWB-REQ-012 choice but not this
PWB-REQ-014 interplay.

**Finding 5 — The register rows P-98 and P-99 do not exist at the reviewed commit, though the package says P-98 "is added by this change"** (note)

Anchor: `IMPACT-LEDGER.md:22` ("P-98 is added by this change"),
`SEMANTIC-DELTA.md:8`, `OWNER-DECISION-PACKET.md:8`. [Observed] At
`0241fb83` a fixed-string search for `P-98` and `P-99` over
`.syzygy/governance/decisions/` returns nothing. The register's last rows are
P-85, P-86 and P-95. The commit touches no file under `decisions/`. The
sentence is false for the bytes reviewed. Applies to both packages.

**Finding 6 — Pair-checking and "do not overlap" claims overstate what was checked** (note)

Anchor: `IMPACT-LEDGER.md:60-61` ("All four spec patches touch different
requirements and compose in either order; this package's builder checks each
pair") and `OWNER-DECISION-PACKET.md:121-122` ("Their changes do not overlap
and compose in any order"). `composition_findings`
(`scripts/pwb_requirement_amendment.py:383-408`) checks only this package
against each other pending sibling: 3 of the 6 unordered pairs. The
class-granular and release-label builders' `--check` output names no
composition check. The packet's "do not overlap" is false for P-85 against
P-86: their own builders say "both add design decision 12 and capability row
34". [Observed] My own run applied all 24 orders of the four spec patches to
one identical result, so the spec-composition conclusion holds. Only the
attribution and the "no overlap" wording are wrong. Applies to both packages.

**Finding 7 — Engine blind spots: replaced lines may lose signed text, and most table targets and new limbs are unpinned** (note)

Anchor: `scripts/pwb_requirement_amendment.py:283` and the builder's
`required_once` (`scripts/build_pwb_opening_index_amendment.py:51-75`). The
lost-line check exempts each `replaced` line by membership. It never asks
that the signed text survive as a prefix of the new limb. [Observed] Probes
over the proposed bytes returned no finding from `spec_findings` in three
cases:

- the `why` row's target changed to "the capability catalog";
- the new Case limb removed, with the signed "  more capability deep dives."
  restored;
- in the accessible-name package, the signed falsifier words "or failed
  cold-open path" deleted from a replaced line.

Only two of the nine table targets are `required_once` phrases. I checked by
hand that the five replaced lines survive as prefixes in this version, so
criterion 4 holds for these bytes. The gap would let a later `--write`
regeneration drift without failing. The engine docstring says the selftest
covers "a sample of the required phrases, not each one", so this is disclosed
for phrases but not for the replaced-line exemption. Applies to both
packages.

**Finding 8 — If both packages are signed, the index rows may trip the distinct-name check** (note)

Anchor: `pwb-accessible-name-amendment/IMPACT-LEDGER.md:50-52` ("the index
rows are links and fall under this package's distinct-name check").
[Inferred] An index row named "capabilities" or "architecture" routes to
"the first element of its target". Any other link with the same accessible
name that routes to the group heading has a different target, so under
package C both need different names. The collision is disclosed but its
consequence is not, and neither package says which string yields. Applies to
both packages.
