# R-PWB-OPENING-INDEX-AMENDMENT-4 — fresh-context review, PWB opening-index amendment (PWB-REQ-010, P-98), round 4
Reviewed commit: 83b29c96775d9c2215292fa41e1599080f0b802c
Manifest SHA-256: fe0791ef8699083ad88871b2ed0a2a183fd5a8f469e99ae1306f45f9ed441867
Verdict: CONFIRM WITH EXCEPTIONS

Package: `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`
(manifest `PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt`). Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`, §"Round 4" governing. This
raw judges package A only. Finding 7 applies to both packages and is
repeated in the C raw. Prior raw: round 3
(`docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-3-RAW.md`, `REVISE`, at
`d6b3784f`). Repairs read: `ROUND-3-DISPOSITIONS.md` §"Repairs, 2026-10-14
(cycle 3)".

The head digest is the sha256 of the manifest file's bytes at the reviewed
commit. I computed it twice: `git show 83b29c96…:<path> | sha256sum`, and a
Python `hashlib` pass over the file in a clean clone. Both gave the same
value.

## Mechanics run (fresh clone at the reviewed commit)

[Observed] Everything below ran in a fresh `git clone`, checked out
detached at `83b29c96775d9c2215292fa41e1599080f0b802c`. I read each
check's output, not only its exit code. `git status --short` in the clone
was empty after the runs. My mutation script restored the builder
byte-for-byte; it checked this itself.

- `build_pwb_opening_index_amendment.py --check`: passes. Output: "11
  proposed subjects (2 patched); 17 requirements, 61 scenarios; structure,
  regeneration, contract coverage, sibling classification and
  pending-sibling composition (pairwise, and one result in every order)
  verify".
- `build_pwb_opening_index_amendment.py --selftest`: passes. Output:
  "position selftest: 4 fixtures fail closed with named findings" and "50
  structure mutants, … all fail closed on their own predicates".
- `build_pwb_accessible_name_amendment.py --check` and `--selftest`: both
  pass. Output: 58 scenarios and 27 structure mutants.
- `build_pwb_release_label_amendment.py --check`: passes. Output: "11
  proposed subjects (7 patched); 17 requirements, 60 scenarios; …
  pending-patch order verify".
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL;
  PASS". R6 still warns on the two behaviour-contract pins
  (`syzygy-2g0d`). That warning belongs to its own owner act.
- I also ran every `scripts/build_pwb_*amendment*.py --check`, 15 builders
  in all.
  - Pass (5): opening-index, accessible-name, release-label,
    registry-currency-briefing and truth-policy.
  - Fail (10): anchor-resolution, class-granular, container-shape-profile,
    dismissal-expiry, exact-source-render-mode, item-depth, machine-view,
    scoped-attributes, state1 and tree-framing. Each fails on a patch that
    no longer applies, or on a manifest that differs from regeneration.
  - Each failing package is signed, performed or declined. Each signed one
    has a sign-off or act record under `decisions/`, and scoped-attributes
    is declined (P-68, `PROJECT-STATUS.md:241`). [Inferred] Those builders
    fail by design once their patches are applied.
  - The engine's `PENDING_SIBLINGS` names exactly three packages:
    accessible-name, opening-index and release-label. All three pass.
- Independent byte check, by my own script, not the engine. I copied the
  PWB change directory and applied both patches with plain `git apply`:
  - all 11 of the 11 manifest rows hash to the proposed bytes;
  - only `GOVERNING-DEPENDENCIES.md` and `spec.md` differ from the tree;
  - the text before the requirements is identical, and the requirement
    population and order are identical;
  - PWB-REQ-010 is the only changed block;
  - a `difflib` opcode pass finds exactly 5 signed lines replaced or
    removed, and they are the builder's 5 `replaced` lines;
  - the `warrants:` block is identical;
  - PWB-REQ-010 goes from 2 scenarios to 7, and the whole proposed spec
    has 61 scenarios.
- Composition, by my own `git apply` loop. I applied the three pending spec
  patches (accessible-name, opening-index, release-label) to `spec.md` at
  this commit in all 6 orders. All 6 applied, none failed, and all gave 1
  result (sha256 `4b95e7d4bd64…`).
- What changed since round 3. `git diff --stat d6b3784f..83b29c96` over
  this package, its builder and the engine shows:
  - the spec patch, the dependency patch, the manifest, the prose and
    `REVIEW-BRIEF.md` (the §"Round 4" addition) changed;
  - `ROUND-3-DISPOSITIONS.md` is new;
  - the builder changed (+152/−28, the cycle-3 repair);
  - the engine changed by 3 lines in `235b71eb`, the P-86 sign-off commit,
    which moved class-granular from `PENDING_SIBLINGS` to
    `PERFORMED_SIBLINGS`. The brief's "which this cycle does not change"
    holds for the repair, but not for the reviewed range. The change is a
    classification move only. See finding 7.
- Rule-6 probes, my own, run through the engine's `spec_findings` over the
  proposed bytes. Baseline: zero findings.
  - Killed (6): the step-out list narrowed to closed `details` only;
    "outermost" → "innermost"; the Oracle's "carry the largest recomputed
    offset" dropped; the route-to-heading rule loosened; "`summary`, which
    counts" flipped; and "shares no code with the renderer" dropped.
  - Survived (6): see finding 4.
- Rule-6 mutants on `position_findings`, run in the clone, each followed by
  `--selftest`:
  - Killed (4): `copies == 0` → `copies == -1` (exit 1, though by a
    `ValueError` traceback, not a named finding); `copies > 1` →
    `copies > 2`; dropping the end-of-block guard (exit 1, by an
    `IndexError`); and replacing the extension test with `False`.
  - **Survived** (1): `old.count(line) != 1 or old.index(line) == 0` →
    `old.count(line) == 0`. See finding 5.
- Today's code, read at this commit. In `apps/three-surface-poc/src/polaris.ts`,
  the claim-strength legend is `<details id="polaris-claim-states" …>`
  (line 408), with no `open` attribute. Its first child is a `summary`
  (line 409), not a heading element. Two links route to
  `#polaris-claim-states` (lines 448 and 1844).

## Round-3 findings, checked one by one against the bytes

- **1 (revise; closed-`details` scope; scenario conflict).** Repaired.
  - The rule now names its subject: "The target that sets the line is the
    rendered target whose offset is largest" (`proposed/spec.md.patch:45-47`).
  - The step-out applies to that target in every case, tie or not
    (`:47-53`).
  - The first scenario's AND now carries both places (`:144-149`).
  - A new scenario covers the closed-disclosure case (`:168-176`).
  - Agreement. I checked every scenario against the rule, and none
    contradicts it. Scenario 4's "so that no closed `details` element
    contains the line" follows from "outermost": a closed `details`
    holding the line would hold the stepped-out element too, so it would
    be a further-out candidate.
  - Residual: scenario 1 is weaker than the rule (finding 1).
- **2 (missing limbs).** Repaired as mapped. Each limb is present:
  - no target rendered: Case (`:89-90`), Oracle (`:104-105`), Falsifier
    (`:125-126`) and a scenario (`:178-184`);
  - tie: Case (`:87-88`) and a scenario (`:160-166`);
  - unrendered row silent: Falsifier (`:122-123`);
  - index first: Observable (`:93-94`) and Falsifier (`:119`).
- **3 (line text; name never shown).** Repaired by pinning both clauses
  (`:55-57`) and a Falsifier limb (`:127`). The repair raises a new
  question (finding 2).
- **4 (recognizer independence).** Partly repaired and disclosed.
  - The selectors and every heading string are published before the run
    (`:109-111`).
  - The delta states the independence is partial
    (`SEMANTIC-DELTA.md:231-244`).
  - [Observed] RFC7-13 names altitudes, not target headings
    (`narrative-contract.md:306-317`). So the raw's suggested anchor does
    not exist, as the dispositions say.
  - Question 12 is fair, and it recommends the version drafted.
- **5 (viewport).** Repaired. The rule is "the viewport width and height
  the page has when it loads", and "The offsets and total a page shows
  SHALL be those of that viewport" (`:60-63`). The ledger now says the
  counter runs in the page (`IMPACT-LEDGER.md:44-54`). Question 10 is fair
  and recommends the version drafted.
- **6 (inline first element).** Repaired by the step-out list (`:50-53`).
  Question 11 puts it to the owner and recommends the version drafted. Its
  "always between blocks" overclaims (finding 3).
- **7 (row-name match).** Repaired (`:23-26`, Falsifier `:120-121`).
- **8 (wrong question number).** Repaired (`SEMANTIC-DELTA.md:160-162`).
- **9 (pinning; positional check).** All six round-3 survivors are pinned
  and in the selftest. `position_findings` now returns a named finding on
  the four paths it names. The residuals are findings 4 and 5.
- **10 (composition).** At this commit all three pending builders' `--check`
  pass, and my own loop composes the three spec patches (above).

Criterion 1 holds:
- the table declares every target;
- "No run, reader or model decides a row's target" is pinned;
- offsets enter no tuple, parity family, record or readiness arm
  (`:72-76`, pinned).

Criterion 2 holds: only PWB-REQ-010 changes, and slices B and D remain
packet Questions 6 and 7. Criterion 4 holds by the byte check above.
Criterion 6 holds by the mechanics above. Every finding below is a note.

## Findings

**Finding 1 — The first scenario's AND is a disjunction weaker than the rule, and two new obligations have only generic limbs** (note)

[Observed] The rule fixes one place
(`proposed/spec.md.patch:47-53`). If an element qualifies, the line goes
after the outermost such element; only if none does is it "immediately
after that first element".

Scenario 1's AND (`:144-147`) accepts either "immediately after that
target's first element, or after the outermost closed `details`, `p`,
heading, `ul`, `ol`, `dl` or `table` element containing it". Its second
limb also drops "immediately".

So a renderer that never steps out of a `p`, `ul` or `table` satisfies
scenario 1, and fails the rule. That is not a contradiction, because
nothing the rule requires fails the scenario. But the scenario does not
discriminate the round-3 finding-6 repair.

Two new obligations have no Case limb, no dedicated scenario, and only the
generic "where this requirement places it" and "misplaced" limbs:
- the step-out of a `p`, heading, `ul`, `ol`, `dl` or `table`. The Case
  (`:85-90`) names the closed-`details` evaluation only;
- the load-time viewport rule (`:60-63`).

A third, "The stopping line's visible text is its numbers and their unit,
and nothing else", has a Falsifier limb (`:127`) but no Oracle limb and no
scenario.

Round 3 classed the same pattern as a note (its finding 2), and I do too.
A repair would be one more Case evaluation, for a target whose first
element lies inside a `p` or list, and a scenario that pins the single
place.

**Finding 2 — "Its numbers and their unit, and nothing else" leaves separators undecided, and on the strict reading the line cannot say which number is which** (note)

[Observed] The line gives two numbers: the largest offset and the page's
word total (`:42-44`). Its visible text is "its numbers and their unit,
and nothing else" (`:55-56`). The Falsifier fails "the stopping line shows
any text beyond its numbers and their unit" (`:127`).

Neither clause says whether a separator is "text". Take "1,980 / 5,210
words", "1,980 of 5,210 words" or "1,980 words · 5,210 words". Two
good-faith oracles can disagree on each. On the strict reading, only
"1,980 words 5,210 words" or similar conforms.

[Inferred] That reading leaves an unfamiliar reader, sighted or using a
screen reader, with an unlabelled pair of numbers. It is a VIS-3 cost the
packet does not name. The clause came from round 3's own suggested repair
("its visible text is the two numbers and their unit"), so it is not the
repairer's invention.

This is the same class as round-3 finding 7, an open match rule on a
visible-text check, which was a note. A repair would say what may join the
two numbers, for example "joined by `of`" or "a separator character", or
put the choice to the owner beside Question 9.

**Finding 3 — Three prose sentences go beyond the bytes after the cycle-3 repair** (note)

[Observed]
- **"Before that target's material, not after it."** The packet says the
  line "comes before that target's material, not after it"
  (`OWNER-DECISION-PACKET.md:69-70`). The delta says "The line therefore
  stands before that target's material, not after it"
  (`SEMANTIC-DELTA.md:184`).
  - Under the step-out, that is no longer true in general. When the target
    that sets the line is the claim-strength legend, the target *is* the
    closed `details`. The line then stands after the whole legend, which
    is all of that target's material.
  - When the first element is a link inside a `table`, the line follows
    the table.
  - The packet's cycle-3 mark (`:78-82`) adds the step-out but does not
    retract the sentence. The delta sentence is unmarked.
  - Question 9's recommended reason still holds, because the place is
    still fixed mechanically. But "before the material" is the packet's
    plain-language account of it.
- **"Always between blocks."** Question 11's recommended option says the
  line "is always visible on arrival and always between blocks"
  (`OWNER-DECISION-PACKET.md:251`). The bytes step out only of the listed
  elements.
  - A first element directly inside a `div`, `section`, `blockquote`,
    `figcaption` or an open `details`'s `summary` still gets "immediately
    after that first element" (`:52-53`), which is mid-flow.
  - A line after a closed `details` that sits under a `hidden` ancestor
    is not visible either.
  - [Unknown] Where the first exact-requirement link sits in today's
    page.
  - The option is still the drafted version and is recommended. Only its
    description overclaims.
- **"Two scenarios."** Question 1's sign row still says PWB-REQ-010 "gains
  the index, the offsets and two scenarios" (`OWNER-DECISION-PACKET.md:105`).
  It gains five. The delta's matching sentence was marked in cycle 3
  (`SEMANTIC-DELTA.md:69-72`), and this one was not. This is the row the
  owner would choose.
- **In-place edit, minor.** `IMPACT-LEDGER.md:44` replaced "at a declared
  viewport" in place. Its dated note explains the change, but it does not
  quote the old words.

**Finding 4 — Six scenario clauses added or relied on in cycle 3 are unpinned** (note)

[Observed] Each of these probes, through the engine's `spec_findings`,
gave zero findings:
- scenario 4's WHEN, "inside a `details` element closed on first load" →
  "anywhere";
- scenario 4's AND, "the line gives the largest offset and the page's word
  total", dropped;
- scenario 3's WHEN, "two rendered targets share the largest offset" →
  "any evaluation";
- scenario 3's AND, "giving the shared offset and the page's word total" →
  "for some target";
- scenario 5's WHEN, "no indexed target is rendered" → "some indexed
  target is not rendered";
- scenario 2's WHEN, the absent opening Unknown aggregate → "any target is
  absent". This one predates cycle 3.

The builder pins these scenarios' headings and THEN clauses only. The
dispositions say "a mutant … for the tie scenario". That mutant drops the
heading, which the probes above do not touch.

**Finding 5 — One sub-predicate pair of the positional check has no fixture** (note)

[Observed] In `position_findings`
(`scripts/build_pwb_opening_index_amendment.py:65`), the first guard is
`old.count(line) != 1 or old.index(line) == 0`. Fixture 1 exercises only
the count-zero case.

Rewriting the guard to `old.count(line) == 0` survives `--selftest`. Two
paths therefore have no fixture:
- a replaced line that occurs twice in the signed block;
- a replaced line that is the block's first line. Here
  `old.index(line) - 1` is −1, so `before` silently becomes the block's
  *last* line.

Both are unreachable at today's signed block, so the check still fails
closed in practice. Two more fixtures would close the gap.

Separately, the `copies == -1` mutant the dispositions cite is killed by a
`ValueError` traceback (`'pred' is not in list`), not by the fixture's
named finding. It fails closed, as claimed, but not by the predicate.

**Finding 6 — Rows must route into a closed disclosure where a target lies inside one; the repository's own guardrail warns against that** (note)

[Observed] "Each row routes to the first element of its target"
(`:26-28`). The Case now includes "the target that sets the stopping line
begins inside a `details` element closed on first load" (`:88-89`). So the
requirement makes a row's route a fragment target inside a closed
`details`.

The AGENTS guardrail says: "Never put a fragment target … inside a
`<details>`: after navigating to it Chrome restarts Tab at the details'
first focusable, stranding keyboard readers." [Inferred] This bears on
PWB-REQ-016's keyboard path. No round raised it, and the packet does not
mention it.

This is a presentation consequence for the implementation or a later
owner question, not a defect in the decidability of the bytes.

**Finding 7 — Composition and sibling state at this commit (applies to both packages)** (note)

[Observed] At `83b29c96` the engine's `PENDING_SIBLINGS` is exactly
accessible-name, opening-index and release-label. All three builders'
`--check` pass, and all 6 application orders of the three spec patches
give one result.

The class-granular builder's `--check` now fails on its own
`CAPABILITY-COVERAGE.md.patch`. That is consistent with P-86 being signed
and applied in `235b71eb`: the other signed siblings' builders fail the
same way. It is not in the round-4 battery.

The engine changed by 3 lines in that sign-off commit. The change moves
class-granular from pending to performed and is no repair. Two
dispositions records still state the round-3-era composition and are not
wrong for their dates:
- A's `ROUND-3-DISPOSITIONS.md` §"Composition at the integration branch";
- C's equivalent, which says "all four pending PWB builders' `--check`
  pass".

Re-run each pending builder's `--check` after the next sibling sign-off,
as the packets already say.
