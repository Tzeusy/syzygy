# R-PWB-OPENING-INDEX-AMENDMENT-3 — fresh-context review, PWB opening-index amendment (PWB-REQ-010), round 3
Reviewed commit: d6b3784f5b7f09b27ffb41f57785282b7393c4d1
Manifest SHA-256: b091f9dcd646bbe25f3eaa2b8086463595ad76c8f328c4935ec8efcf5c2662e2
Verdict: REVISE

Package: `.syzygy/governance/contracts/candidates/pwb-opening-index-amendment/`
(manifest `PWB-OPENING-INDEX-AMENDMENT-MANIFEST.txt`). The head digest is the
sha256 of that file's bytes at the reviewed commit. I computed it with
`git show d6b3784f…:<path> | sha256sum` and confirmed it with a second
Python `hashlib` pass over the clean clone's working file. Brief:
`pwb-opening-index-amendment/REVIEW-BRIEF.md`, §"Round 3" governing. This
raw judges package A only. Findings 9 and 10 apply to both packages and are
repeated in the C raw. Prior raws: rounds 1 and 2
(`docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-2-RAW.md`, `REVISE`, at
`ae8c0740`). Repairs: `ROUND-2-DISPOSITIONS.md` §"Repairs, 2026-10-14
(cycle 2)".

## Mechanics run (fresh clone at the reviewed commit)

[Observed] Everything below ran from a fresh `git clone` checked out
detached at `d6b3784f`. The engine derives `ROOT` from `__file__`, so the
scripts read the clone. `git status --short` in the clone was empty after
every run. I read each check's output, not only its exit code.

- `build_pwb_opening_index_amendment.py --check`: passes. Output: "11
  proposed subjects (2 patched); 17 requirements, 54 scenarios; structure,
  regeneration, contract coverage, sibling classification and
  pending-sibling composition (pairwise, and one result in every order)
  verify".
- `build_pwb_opening_index_amendment.py --selftest`: passes. Output: "33
  structure mutants, … all fail closed on their own predicates". That
  matches the dispositions' 5 engine plus 28 builder mutants.
- `build_pwb_accessible_name_amendment.py --check` and `--selftest`: both
  pass. Output: 54 scenarios and 27 mutants.
- `build_pwb_class_granular_extraction_amendment.py --check`: passes. Output:
  "11 proposed subjects (5 patched); 17 requirements, 56 scenarios".
- `build_pwb_release_label_amendment.py --check`: **fails** (exit 1). Output:
  "GOVERNING-DEPENDENCIES.md.patch does not apply: error: patch failed: …
  GOVERNING-DEPENDENCIES.md:9". This is the stale dependency patch the
  dispatcher and the dispositions both describe. See finding 10.
- `check_governance.py`: "32 OK, 21 WARN, 0 FAIL (53 checks)".
- `check_spec_reconciliation.py --check`: "7 of 7 predicates without FAIL;
  PASS". R6 still warns on the two behaviour-contract pins. That warning
  belongs to its own owner act and is not this package's.
- Independent byte check, using my own script and not the engine. I copied
  the PWB change directory, then applied both patches with plain
  `git apply`:
  - all 11 of the 11 manifest rows hash to the proposed bytes;
  - only `GOVERNING-DEPENDENCIES.md` and `spec.md` differ;
  - the text before the requirements is identical, and the requirement
    population and order are identical;
  - PWB-REQ-010 is the only changed block;
  - a `difflib` opcode pass finds exactly 5 signed lines replaced or
    removed. They are the builder's 5 `replaced` lines, and each opens
    exactly one proposed line;
  - the `warrants:` block is identical;
  - PWB-REQ-010 goes from 2 scenarios to 4.
- Composition, by my own `git apply` loop. I applied the four pending spec
  patches (accessible-name, class-granular, opening-index, release-label)
  to `spec.md` at this commit in all 24 orders. All 24 applied, none failed,
  and all gave 1 result (sha256 `fa0522173b60…`).
- Rule-6 probes, run through the engine's `spec_findings` over the proposed
  bytes:
  - Killed (each raised its required-phrase finding): "target's heading →
    any element", "index follows the narrative tree", "no-target placement
    dropped", and "total over the index only".
  - **Survived** (no finding): "are presentation measurements" → "are
    project claims"; "Words are counted by one declared method" → "by any
    method"; dropping the Case's absent-aggregate evaluation; dropping the
    Observable's index limb; widening the first scenario's WHEN to any
    evaluation; and replacing "measured on a fresh private-daemon capture
    …" with "estimated". See finding 9.
- Today's code, read at this commit. In `apps/three-surface-poc/src/polaris.ts`:
  - 14 lines open a `<details`;
  - the claim-strength legend is `<details id="polaris-claim-states">`
    (line 408), with no `open` attribute;
  - that legend is rendered at line 1845, near the head of the page.

Round-2 findings, checked one by one against the bytes, not only against
the mapping:

- **1 (scenario stopping line).** Repaired as mapped. The scenario's AND
  (`proposed/spec.md.patch:123-125`) now reads in the requirement's terms,
  and it is pinned. The killed mutant "scenario stopping line moved to the
  last indexed target" is in the selftest. The same repair cycle added
  sub-rules that the scenario does not carry. That is finding 1.
- **2 (row accessible-name sentence).** Repaired by dropping it. "Each row
  shows its declared row name" (`:23`) has an Oracle limb (`:86-87`), a
  Falsifier limb (`:102-103`) and a scenario THEN (`:120`), and all are
  pinned. It is checkable, with the caveat in finding 7. Packet Question 8
  states the drop fairly, including that signing A alone leaves another
  link free to share a row's words.
- **3 (offset with no counted word; unrendered row).** Repaired. The offset
  base is "counted words that precede the target's first element", and
  "Each row whose target is rendered SHALL show" (`:35-38`). The new
  sub-rules are finding 1 and finding 2.
- **4 (browser state).** Repaired. The viewport is declared and published
  (`:50-51`), and visibility is read per text node (`:56-57`). Both are
  pinned. The residual is finding 5.
- **5 (stopping line name and place).** Put to the owner as Question 9. See
  finding 3 on what the packet says the bytes guarantee.
- **6 (stale sentences).** Repaired. The ledger plans a counter over the
  document after load (`IMPACT-LEDGER.md:42-46`). The round-state sentences
  are marked and dated.
- **7 (recognizer independence).** Repaired. The permitted keys are named
  (`:93-97`) and pinned. The residual is finding 4.
- **8 (pinning; engine prefix check).** The two phrases the round-2 probes
  moved are now pinned, and both mutants are in the selftest. The
  builder's `position_findings` adds the positional check, and its mutant
  is killed. Residuals are in finding 9.
- **9 (sibling order).** At this commit the four pending spec patches
  compose in every order (above). The release-label lane remains open
  (finding 10).

Criterion 1 holds. The table declares every target, and offsets enter no
tuple, parity family, record or readiness arm (`:61-65`, pinned). Criterion
2 holds: only PWB-REQ-010 changes, both patches target PWB paths only, and
slices B and D are put to the owner as Questions 6 and 7. Criterion 4 holds
by the byte check above. The one revise finding is against criterion 3.

## Findings

**Finding 1 — The closed-`details` placement rule added in repair has an ambiguous scope, and on the reading the dispositions intend, the first scenario contradicts it** (revise)

[Observed] The anchor is `proposed/spec.md.patch:42-47`: "Where two targets
share the largest offset, the stopping line follows the one whose first
element comes later in document order. Where that element lies inside a
`details` element closed on first load, the line stands immediately after
the outermost such `details` element instead."

The antecedent of "that element" is the tie sentence's "first element". On
the text alone, the closed-`details` override can be read two ways:

- **Tie only.** Then a single largest-offset target inside a closed
  disclosure puts the line inside that disclosure, where a reader on
  arrival cannot see it.
- **General.** This is what `ROUND-2-DISPOSITIONS.md` row 3 says it
  settles: "a largest-offset target inside a closed `details` (the line
  stands after the outermost closed `details`)".

So the line's position is decidable only once a reader picks one reading.
The brief asks for exactly this test: whether the closed-`details` rule
leaves any line position undecidable.

On the intended (general) reading, the first new scenario contradicts the
requirement. Its WHEN is "an evaluation where every indexed target renders".
That does not exclude a rendered target inside a closed disclosure. Its AND
(`:123-125`) still asserts that "exactly one stopping line stands
immediately after the first element of the target whose offset is largest".
For that case, a conforming implementation puts the line after the outer
`details`, and so fails the scenario.

This is the class of defect round 2 made revise-level (round-2 finding 1:
a scenario that places the line where the requirement does not). This
repair cycle introduced it, because the sub-rules were added and the
scenario was not touched. The case is not hypothetical in Polaris's
layout. [Observed] Today's claim-strength legend, one of the nine targets,
is itself a closed `<details>` whose first element is its `summary`
(`polaris.ts:408`). [Inferred] Other targets, such as the first
exact-requirement link, may sit inside the page's closed `population`,
`class-provenance` or `reading-citations` disclosures.
[Unknown] Which target has the largest offset on Butlers today.

The builder pins the sub-rule sentences and the scenario sentence
separately. Nothing checks that they agree.

Repair, for the owner's next direction: make the override's scope explicit
by naming "the target that sets the line" rather than "that element".
Then either qualify the scenario's AND ("…, or after the outermost closed
`details` containing it") or narrow its WHEN to a largest-offset target
outside any closed disclosure.

**Finding 2 — Three of the new placement and disclosure rules carry no scenario, and one carries no falsifier limb** (note)

[Observed] Criterion 3 asks each new obligation for an oracle limb, a
falsifier limb and a scenario. Four rules fall short:

- **No target rendered.** The line "stands immediately after the index and
  gives only the word total" (`:46-47`). The Oracle's "carry the largest
  recomputed offset" and the Falsifier's "its offset is not the largest"
  are both vacuous here. A line that shows "0" as an offset is not named
  as a failure, and no scenario covers the case.
- **Tie.** The tie-break (`:42-43`) has no scenario.
- **Unrendered row "SHALL say so".** The rule is at `:32-33`. The Falsifier
  (`:104`) names an unrendered row that "routes anywhere or shows an
  offset", but not one that fails to say its target is not rendered. Only
  the second scenario's THEN carries "says its target is not rendered".
- **Index first.** "The first reading level SHALL begin with an index"
  (`:6`) has no falsifier limb for an index that is present but not first.

Each rule is generically reachable through "where this requirement places
it" and "misplaced", so I class this as a note. The no-target case is the
nearest to a missing limb.

**Finding 3 — The packet and the delta tell the owner the stopping line's text is "the two numbers only" and its name is "never shown on the page"; the bytes say less** (note)

The packet says "Its text is the two numbers only" (`OWNER-DECISION-PACKET.md:50`)
and "the name is the specification's, never shown on the page" (`:178`).
The delta says "its text is the two numbers and nothing else, and
'stopping line' is the specification's name for it, never shown to a
reader" (`SEMANTIC-DELTA.md:156-158`).

[Observed] The bytes say the line shall "give that largest offset and the
page's word total, and nothing else about the index" (`:39-41`), plus the
verdict exclusion (`:63-65`). They do not forbid connecting words, and they
do not forbid the term "stopping line" from being shown. Whether a visible
label "Stopping line" counts as something "about the index" is a reading
question.

Question 9's recommended option rests its reason ("The line says nothing
about stopping") on this stronger property. So the question is fair only
if the owner knows the property is the packet's reading and not a pinned
clause. One added clause would make the packet's description true, for
example "its visible text is the two numbers and their unit". So would
softening the packet.

**Finding 4 — The recognizer's permitted keys are named, but the expected heading text is anchored nowhere outside the renderer** (note)

[Observed] Selectors may key "only on visible heading text, on claim
identities the machine answer serves and on the PWB-REQ-011 exact-source
route form" (`:93-97`). Nothing says what heading text each target's
heading must carry, or where the expected strings come from. An oracle
author can only copy them from the rendered page, so the expected strings
share the renderer's view. Round 2 suggested anchoring them to the RFC7-13
category names.

[Inferred] The claim-identity key can only be read through attributes the
renderer emits for claims in general (for example `data-claim-provenance`).
The "to mark an index target" qualifier makes that lawful. The
independence it buys is therefore partial, and the delta's "Why the
recognizer may not key on the renderer's markers" bullet does not say so.

**Finding 5 — An oracle-declared viewport makes the value the renderer must show depend on the oracle's choice** (note)

[Observed] The count is taken "at the one viewport width and height the
oracle declares" (`:50-51`). This makes any single oracle run decidable.
But the SHALL on the renderer ("SHALL show the word offset") is then
defined only relative to a viewport that the requirement does not fix.

A renderer that computes offsets on the server, or at one assumed width, is
correct at some oracle viewports and not at others whenever a media query
hides text. [Observed at round 2, and not re-measured here] Today's
`@media` blocks hide nothing, so the gap is latent.

[Inferred] In practice the requirement pushes the implementation to compute
offsets in the page after load. Two plans miss this:
- `IMPACT-LEDGER.md:42-46` plans "a word counter … for the index" without
  saying where it runs;
- the AGENTS note on script-created elements says such a counter must be
  enumerated post-script.

Either fix the viewport in the requirement, or say in the ledger that the
displayed offsets are computed in the page.

**Finding 6 — "Immediately after the first element" of an inline target places the line mid-flow** (note)

[Inferred] The `exact-requirement` target is "the first link, in document
order, to an exact requirement's text". Its first element is that `a`.
"Immediately after" it, the line would sit inside a sentence, a list item
or a table cell. Inside a `ul` or a `tr` it would be invalid HTML.

The text is decidable. Whether the owner wants the line there is a
presentation question that Question 9 does not mention.

**Finding 7 — "Shows its declared row name" leaves the match rule open** (note)

[Observed] The row shows both a name and an offset (`:23`, `:35`). The
Oracle compares "each row's name" with the table (`:86-87`). The text does
not say:
- how the name is separated from the offset in the row's text;
- whether the match is exact, or by substring;
- whether the match is case-sensitive ("V1 success" against "V1 Success").

Two good-faith oracles could disagree on a row such as "Purpose · 412
words". One phrase would settle it, for example "the row's text begins
with its declared row name, exactly".

**Finding 8 — A cross-reference in the delta names the wrong packet question** (note)

[Observed] `SEMANTIC-DELTA.md:133` says that putting offsets in the
walkthrough record "is slice B, not drafted (owner packet, question 4)".
Slice B is packet Question 6. Question 4 asks whether the offsets are
machine-readable. The sentence was already present at `ae8c0740` (line 123
there), so rounds 1 and 2 missed it. It is a pre-existing error, not one
introduced by the repair.

**Finding 9 — Pinning residuals and the positional check (applies to both packages)** (note)

[Observed] The positional check and the two probed phrases are pinned, and
their mutants are killed. My survivors are listed under Mechanics. Two of
them change meaning silently:
- "are presentation measurements" → "are project claims" (the following
  pinned sentence still says they carry no tuple, so the requirement would
  contradict itself);
- "one declared method" → "any method".

On the positional check (`position_findings`, identical in both builders):

- It fails closed. If a predecessor line is edited away, the check reports
  it as "not unique" even when the line is absent. The message misleads,
  but the outcome is a finding.
- If a signed replaced line is no longer in the current block (for
  example, after a sibling sign-off rewrites that requirement),
  `old.index(line)` raises `ValueError`. `--check` then exits non-zero
  with a traceback instead of a finding. That still fails closed, but it
  names nothing.
- The function is duplicated verbatim in two builders rather than living
  in the engine. The dispositions justify this by the concurrent P-85 and
  P-86 lanes. The next engine edit should absorb it.

**Finding 10 — Composition with the release-label lane is verified only for its spec patch as it stands at this commit (applies to both packages)** (note)

[Observed] What I could verify at `d6b3784f`:

- this builder's `--check` composes all four pending spec patches pairwise
  and in every order;
- my own loop reproduces that: 24 of 24 orders apply, with 1 result;
- the class-granular (P-86) builder's `--check` passes.

What I could not verify:

- The release-label (P-85) builder's `--check` fails on its stale
  `GOVERNING-DEPENDENCIES.md.patch`. So I could not check its full proposed
  subject set, its manifest or its coverage regeneration at this commit.
- Whether the spec patch its lane regenerates will be byte-identical to
  the one composed here. [Unknown]

This package's `--check` composes whatever spec patch lands, live. The
packet's "whichever is signed second is regenerated … and reviewed again"
covers the manifest consequence. Re-run this builder's `--check` once P-85
lands.
