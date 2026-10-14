# R-PWB-OPENING-INDEX-AMENDMENT-2 — fresh-context review, PWB opening-index amendment (PWB-REQ-010), round 2
Reviewed commit: ae8c074066d8e6c511d8064b505e3f89e3f2b43d
Manifest SHA-256: 4cee1b0c8120448bdda6bba1047d7ad06f51b1a7a18fec12c0cb4cd07475e518
Verdict: REVISE

Package: `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`
(manifest `PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt`). The head digest above
is the sha256 of that file's bytes at the reviewed commit, computed with
`git show ae8c0740…:<path> | sha256sum` and matched by a second Python
hash over the clone's working file. Brief: `pwb-opening-index-amendment/REVIEW-BRIEF.md`.
This round covers both packages, as round 1 did. This raw judges package A
only. Round 1: `docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-1-RAW.md`
(`REVISE`, at `0241fb83`). Repairs: `ROUND-1-DISPOSITIONS.md`.

## Mechanics run (fresh clone at the reviewed commit)

[Observed] Run from the root of a `git clone` checked out detached at
`ae8c0740`. I read the output and the exit code of each:

- `build_pwb_opening_index_amendment.py --check`: exit 0. "11 proposed
  subjects (2 patched); 17 requirements, 53 scenarios; structure,
  regeneration, contract coverage, sibling classification and
  pending-sibling composition (pairwise, and one result in every order)
  verify".
- `build_pwb_opening_index_amendment.py --selftest`: exit 0. "23 structure
  mutants …". That is 5 shared engine mutants plus 18 declared in the
  builder. Each must produce a finding that starts with its own expected
  prefix (`pwb_requirement_amendment.py`, `selftest`).
- `build_pwb_accessible_name_amendment.py --check` and `--selftest`: exit 0.
- `build_pwb_class_granular_extraction_amendment.py --check`: exit 0.
  `build_pwb_release_label_amendment.py --check`: exit 0.
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL;
  PASS". The R6 WARN on the two stale behaviour-contract pins was there
  before this package.
- Independent byte check, my own script. I applied both patches to a copy
  of the change directory. All 11 manifest rows hash to the proposed bytes.
  Only `spec.md` and `GOVERNING-DEPENDENCIES.md` differ. The text before the
  requirements is identical, the requirement population and order are
  identical, and the only changed block is PWB-REQ-010. A line diff of that
  block shows exactly 5 signed lines changed. They are the 5 the builder
  lists as `replaced`, and each survives as the prefix of its extended
  line. The `warrants:` block is unchanged. `git diff c371339d ae8c0740`
  over the PWB and Three-Surface POC change directories is empty.
- Composition, by my own script rather than the engine's search: I applied
  the five pending spec patches on main (accessible-name, anchor-resolution,
  class-granular, opening-index, release-label) in all 120 orders with
  `git apply`. 120 of 120 applied, 0 failed, and all gave 1 result (sha256
  `937ed2e7…`).
- Impact-ledger census: I re-derived it with the ledger's own published
  regex over the 2,006 paths at `c371339d`. 99 files cite PWB-REQ-010, and
  every area count reproduces (31/20/25/5/6/1/3/6/1+1).
- Rule-6 probes over the proposed bytes through `spec_findings`:
  - Truncating the replaced Case line raises "replaced line lost its signed
    text". Round 1's engine gap is closed.
  - Dropping the accessible-name sentence fails, and so does dropping the
    `visibility: hidden` exclusion: both are pinned.
  - Two scenario edits return **no finding**: moving the scenario's
    stopping line to "precedes the first indexed target", and letting "the
    other eight rows" change targets. See findings 1 and 8.
- Citations: PWB spec lines 1934 and 1941–1945, RFC-0007 lines 134 and 162,
  and `CAPABILITY-COVERAGE.md` row 9 each say what the package quotes.
- No figure from the untracked capture appears in the package. A sweep for
  3,206, 9,403, 26,630, 10,173, 390 and 144 matched only digests.

Round-1 repairs, checked one by one:

- **1 (word method).** Repaired. The method now names its representation
  ("the document as the browser holds it after load"), lists its exclusions
  exhaustively, counts a closed `details`' `summary`, and fixes the offset
  base. Notes 2 and 3 remain.
- **2 (stopping line).** Repaired in the requirement text and in the
  Oracle and Falsifier. Not repaired in the scenario: finding 1.
- **3 (recognizer).** Repaired in part, as dispositioned. Packet question 2
  puts the two narrower targets to the owner.
- **4 (copy roles).** Repaired, and packet question 5 puts the readings to
  the owner, so CC-SPEC-6 is honoured.
- **5 (register rows).** P-98 and P-99 exist (`PENDING-OWNER-DECISIONS.md:1156-1157`).
- **6 (pair-checking).** Repaired. Each builder on main lists the other
  four pending packages, and the 120-order claim reproduces.
- **7 (engine).** Repaired: the prefix check exists and fires. All nine
  table rows are pinned.
- **8 (row names).** Addressed by a new sentence, but that sentence is
  finding 2.

Criteria 1 (no verdict, no score) and 2 (scope) hold. Slices B and D are put
to the owner with clause reasoning (packet questions 6 and 7). The two
revise findings are against criterion 3.

## Findings

**Finding 1 — The new scenario still places the stopping line "after the last indexed target", which contradicts the repaired requirement** (revise)

Anchor: `proposed/spec.md.patch:39-41` and `:109-112`. The requirement text
reads: "Exactly one stopping line SHALL stand immediately after the first
element of the target whose offset is largest". The scenario reads: "**AND**
one stopping line follows the last indexed target, giving the largest row
offset and the page's word total".

Round-1 finding 2 was about exactly this phrase, and the repair left it in
the scenario. Read in index order, "the last indexed target" is row 9
(`v1-success`, the V1 statements). That is not the largest-offset target
whenever the capability catalog, the first exact-requirement link or the
legend comes later in document order. [Inferred] That is likely, since
PWB-REQ-010 puts the project statements before the catalogs. Read in
document order, "follows the target" means after its whole extent, not
immediately after its first element. On both readings the scenario
contradicts the requirement. [Observed] The builder does not pin the
scenario's wording, and my probe moving the line to "precedes the first
indexed target" produced no finding.

Criterion 3 requires scenarios that the requirement's text carries. Repair:
restate the scenario in the requirement's terms, and pin the phrase.

**Finding 2 — The row accessible-name sentence added in repair is a new obligation with no oracle limb, no falsifier limb and no scenario** (revise)

Anchor: `proposed/spec.md.patch:25-27`: "A row's accessible name names its
question, so it shares no name with a link to a different place
(PWB-REQ-016)." This was added for round-1 note 8. Criterion 3 says "Each
new obligation has an oracle limb, a falsifier limb and a scenario." The
gaps:

- The Oracle (`:77-81`) recomputes offsets, compares targets with the table
  and places the stopping line. It never reads a row's accessible name.
- The Falsifier (`:90-96`) names no row whose name fails to name its
  question, and no shared name.
- Neither scenario mentions names.

"Its question" is also undefined. PWB-REQ-021 gives identities
(`why`, `refusals-and-rule`, …), not question strings. RFC7-30's prompts are
prose, so two oracles could disagree about whether "purpose" or "why
Butlers exists" names the question. The "so it shares no name" clause is a
consequence the sentence asserts, not something the sentence guarantees.
Another link with the same words and a different target breaks it unless
PWB-REQ-016 as amended by C is also signed. Package A may be signed alone
(C's packet question 5).

Repair: declare each row's accessible name, or a rule that derives it, in
the table, and add oracle, falsifier and scenario limbs. Alternatively,
drop the sentence and leave distinctness to C.

**Finding 3 — An offset is undefined when the target has no counted word, and "each row SHALL show" has no exception for an unrendered row** (note)

Anchor: `:37-39` ("Each row SHALL show the word offset at which its target
begins: the number of counted words before the target's first counted
word") and `:34-35`. A target that is rendered but holds no counted word has
no first counted word. Examples: a target wholly inside a `details` closed
on load, or the first exact-requirement link if it sits inside one. The
offset is then undefined, the "largest offset" may not exist, and the
stopping line could sit inside a closed disclosure. The text says nothing
about that case. Separately, an unrendered row "SHALL say so and route
nowhere", yet the unqualified "Each row SHALL show the word offset" binds it
too. The second scenario ("the other eight rows keep their declared targets
and offsets") implies the `gaps` row has none. One clause would settle both.

**Finding 4 — The computed-style exclusions depend on a browser state the method does not fix** (note)

Anchor: `:42-51`. Exclusion by "computed `display: none` or
`visibility: hidden`" depends on the viewport and media features. A counter
at 640 px and one at 1280 px can disagree whenever CSS hides content behind
a media query. [Observed] At this commit the `@media` blocks in
`apps/three-surface-poc/src/polaris.ts` (opening at lines 1632, 1644, 1675 and
1683) change layout only
and hide nothing, so the gap is latent. A computed `visibility: hidden` can
also be overridden by a descendant set to `visible`. The rule says "inside
any element with" it, so that visible text is excluded. That is decidable
but probably not intended. Naming a viewport, or "the default viewport the
oracle declares", closes the first point.

**Finding 5 — The stopping line sits at the start of the last target's material, and its name invites a reader to stop there** (note)

Anchor: `:39-41` and `SEMANTIC-DELTA.md:138-140`. The repaired placement is
"immediately after the first element of the target whose offset is
largest". That is right after that target's heading, before its content.
The pursuit framed the gap as "a reader had no licence to stop"
(`SEMANTIC-DELTA.md:38-39`). A line called a stopping line, placed before
the last target's material, offers that licence at a point where the last
question's material has only begun. The text says only numbers, so
criterion 1 holds. The term and the placement together still risk the
reading RFC7-31 reserves to the owner, and they make VIS-3's plain account
harder. The packet's "one line after the last target"
(`OWNER-DECISION-PACKET.md:26-28`) repeats the ambiguity. The owner may want this named.

**Finding 6 — Two sentences went stale in the repair** (note)

- `IMPACT-LEDGER.md:43-44` still plans "A word counter over the served HTML
  for the index". The repaired method counts "the document as the browser
  holds it after load". Round-1 finding 1 turned on that difference, so the
  ledger points an implementer back at it.
- `SEMANTIC-DELTA.md:193-198`, `OWNER-DECISION-PACKET.md:9-14` and register
  row P-98 say "no round 2 was dispatched". That was true when they were
  written. This raw is a round 2, so those sentences go false when it lands.
  The next edit should mark them, dated, at the sentence (the CG-27 lesson).

These same two kinds of staleness occur in package C.

**Finding 7 — The recognizer that locates targets is "published with the oracle", but nothing says it is independent of the renderer's markup** (note)

Anchor: `:83-87`. Targets are "located by a recognizer whose selectors are
published with the oracle". If those selectors key on attributes the
renderer emits for the same purpose, the recognizer is the renderer's own
mapping by another name, which the Oracle limb (`:78-80`) forbids.
CC-SPEC-4's independence limb would be better served by naming what the
selectors may key on, such as heading text equal to the RFC7-13 category
name, or the model's claim identities. Round-1 note 3 was repaired in part,
and this is the remainder.

**Finding 8 — Pinning: the scenario phrases most at risk of drift are unpinned; the engine's prefix check accepts any line** (note, applies to both packages)

[Observed] Probes over the proposed bytes found two unpinned scenario
phrases: the stopping-line placement in the first scenario (finding 1), and
"**AND** the other eight rows keep their declared targets and offsets",
which I replaced with "may change targets". Neither raised a finding. In the
shared engine, the new replaced-line check (`pwb_requirement_amendment.py`,
`spec_findings`) asks whether any line in the whole block starts with the
signed stem. It does not ask that line to be the one in the replaced
line's position. The current bytes pass on the correct lines (my diff
above). A later `--write` could pass on the wrong one.

**Finding 9 — Sibling order was checked against main only; the repaired P-85 and P-86 remain for sign-off time** (note, applies to both packages)

As the dispatcher directed, I did not fetch the unmerged branches that hold
the repaired release-label (P-85) and class-granular (P-86) packages. On
main, both builders' `--check` pass, and they list opening-index,
accessible-name and anchor-resolution as pending siblings. All 120 orders
of the five patches give one result. What remains: the repaired P-85 and
P-86 patches have not been composed with this package. When either lands,
this builder's `--check` composes it live and will report it. The packet's
"whichever is signed second is regenerated … and reviewed again" covers the
manifest consequence.
