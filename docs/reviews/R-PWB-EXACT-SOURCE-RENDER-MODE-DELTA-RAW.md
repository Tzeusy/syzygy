# Review — PWB exact-source render mode (round 1)
Reviewed commit: 08f980f746991b194d4d8dbfb5b6598087aa1e2d
Manifest SHA-256: 5796c1541a90a109c0259a079d2262883942d1f97ac36c733ecf2c0c28763433
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the package was not
read before this review began. Read-only throughout; every mutation
(`--selftest` aside) was performed in a `cp -r` scratch copy under the
session scratchpad, never in the reviewed worktree. Class: fresh-reader
semantic review of a normative delta (CC-REV-2, CC-REV-4, CC-REV-6). This is
round 1 — there is no prior disposition list to check.

---

## What I ran

1. Read AGENTS.md in full, then `REVIEW-BRIEF.md` (this package) as the
   instruction set — 12 numbered criteria plus a required-baseline list.
2. `sha256sum PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` →
   `5796c1541a90a109c0259a079d2262883942d1f97ac36c733ecf2c0c28763433`,
   matching `OWNER-DECISION-PACKET.md:156`'s printed argument. Computed, not
   transcribed (rule 3).
3. `python3 scripts/build_pwb_exact_source_render_mode_amendment.py --check`
   → "PWB exact-source render-mode amendment manifest matches 11 proposed
   behavior subjects (4 patched, 7 unchanged); the generated dependency file
   carries the proposed spec.md digest; on the scoped-attributes tree the 3
   semantic patches apply and the generated one collides as declared", exit
   0.
4. `... --selftest` → "selftest: closed population, byte drift, path order,
   subject drift, patch corruption, transcribed generated digest,
   wide-context lane collision and absent regeneration collision fail
   closed", exit 0 — eight named predicates, each a rule-6 fixture.
5. `... --diff`, saved to a scratch file; concatenated the four
   `proposed/*.patch` files in manifest order into a second scratch file;
   diffed the two — byte-identical. No hand-transcription in `--diff`
   (rule 3).
6. Scratch copy (`cp -r`): applied all four patches with
   `git apply --whitespace=nowarn`; all four applied clean. Read the
   patched `spec.md` PWB-REQ-011 block, `design.md` §8's two new
   paragraphs, `CAPABILITY-COVERAGE.md` row 10, and
   `GOVERNING-DEPENDENCIES.md`'s Source line as a fresh reader (criteria
   1–7, 9).
7. Withholding (criterion 1): tried to construct a reading that serves one
   of the 9 withheld sources — as a `whole-body` render of an excluded
   TOML manifest, as a served body behind a scroll anchor, and as a body
   reachable via the sweep's "admitted and excluded alike" request. All
   three fail on the same sentence: "A source whose record outcome is
   excluded SHALL NOT be served in any mode" is unconditional and
   independent of which mode a route would otherwise pick, and
   `design.md`'s new text (patched, lines 43–51 of the hunk) states the
   two populations — admitted-classified-blob vs. excluded — are disjoint
   by construction (record outcome), so no reading is available where a
   source is simultaneously excluded and admitted-as-blob.
8. Gate ordering (criterion 2): the patched clause reads "Every mode SHALL
   apply the same authority, exact-object, secret-detection and
   inert-content gates to the **complete transient body** before encoding
   any part of it." "Complete... before encoding any part" rules out a
   per-section reading — there is no section-scoped gate to fail
   partially; failure leaves the **whole** body Unknown. Cross-checked
   against `apps/three-surface-poc/src/verbatim-route.ts`'s existing
   refusal lines (`unconsented-source-or-provider`, several
   `excluded-content` returns) — the gates named in the clause match the
   gates already implemented; the amendment adds no new gate and removes
   none.
9. Re-ran both named generators over the fully-patched scratch tree
   (criterion e / criterion 9):
   `python3 scripts/build_polaris_project_wide_spec_dependencies.py` →
   regenerated `GOVERNING-DEPENDENCIES.md` byte-identical to
   `proposed/GOVERNING-DEPENDENCIES.md.patch`'s result (diff empty);
   `python3 scripts/build_polaris_project_wide_contract_coverage.py
   --check` → reports the same represented-clause count as the unpatched
   tree (no warrant list changed). Diffed the other 6 manifest-listed
   unchanged subjects (`.openspec.yaml`, `CONTRACT-COVERAGE.md`,
   `CONTRACT-COVERAGE-REPAIR-DELTA.md`, the three
   `contract-coverage-matrix/RFC-*.md` files, `proposal.md`) against the
   pre-patch worktree copies — all byte-identical.
10. Composability, the declared collision (criterion d, criterion 8): in a
    fresh scratch copy, applied
    `pwb-scoped-attributes-amendment/proposed/spec.md.patch` first, then
    this package's four patches, with both GNU `patch -p1` and strict
    `git apply --whitespace=nowarn`, and the reverse order, in four
    separate throwaway trees (`compose-forward`, `compose-reverse`,
    `compose-forward2`, `compose-reverse2`). All four combinations apply
    every hunk with no rejects and converge on the identical final
    `spec.md` digest
    (`5b2d451ceca0b1cd51baafd8ff48fa1058927905682503f2cd4b0e0a0d1208c0`)
    and an identical, now-stale `GOVERNING-DEPENDENCIES.md` Source line —
    exactly one generated line disagrees with what a regeneration would
    write, as `IMPACT-LEDGER.md:106-114` claims. Mutation test (rule 6):
    deleted `proposed/GOVERNING-DEPENDENCIES.md.patch` in a scratch copy
    of this package and re-ran `--check` → **FAIL**, naming the missing
    patch and stating "the declared regeneration collision cannot be
    tested". The collision assertion fails closed when its own evidence
    is removed.
11. Composability, a narrower case the ledger does not test (beyond the
    literal ask; became F3): repeated step 10 applying **only** lane B's
    `spec.md.patch` — not its `GOVERNING-DEPENDENCIES.md.patch` or
    `contract/RFC-0007-rendering-and-surface.md.patch` — alongside this
    package's four patches, both tool chains, both orders. All four
    combinations again apply clean with no rejection at the patch-tool
    level, but `GOVERNING-DEPENDENCIES.md`'s Source line is left at
    whichever amendment's digest applied last, silently wrong for the
    other's spec.md content, and neither package's `--check` exercises
    this partial-landing shape (each only tests the sibling's **full**
    patch set).
12. `python3 scripts/check_governance.py`, full run, on the present-package
    worktree → 32 OK, 20 WARN, 0 FAIL (52 checks); CG-7d "58 quotations
    examined, 0 findings"; CG-7e "34 files examined, 0 findings". Repeated
    in a scratch copy with
    `.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/`
    deleted → same 32 OK, 20 WARN, 0 FAIL — the registration does not
    break on package absence (criterion g's third clause).
13. Rule-6 mutation directly on the new registration: in a scratch copy,
    replaced `OWNER-DECISION-PACKET.md:156`'s 64-hex digest with 64 zeros
    and re-ran `check_governance.py` → **FAIL** on both CG-7d and CG-7e,
    each naming `OWNER-DECISION-PACKET.md` and stating the manifest hashes
    to `5796c1541a90…` while the quoted phrase does not match — the
    underlying mechanism the new code activates is proven to fail closed.
14. Searched for a **dedicated, automated** `--selftest` fixture covering
    this specific registration (criterion g's second clause):
    `grep -n "_selftest_pwb_act_copy_registry" scripts/check_governance.py`
    lists every call site (lines 6190, 6194, 6202, 6206, 6214, 6217, 6225,
    6228, plus the effect/amendment variants further down). The call sites
    cover `PWB_STATE1` (default), `PWB_TRUTH_AMENDMENT_LABEL`, the
    `POLARIS_GENERATOR_APPROVAL_ACTS` loop and `POLARIS_UNDERSTANDING_LABEL`
    — none passes `PWB_RENDER_MODE_LABEL` or `PWB_SCOPED_AMENDMENT_LABEL`.
    `grep -n "PWB_RENDER_MODE_LABEL\|PWB_SCOPED_AMENDMENT_LABEL"
    scripts/check_governance.py` confirms both names occur only in their
    definitions, `_act_subjects()`, `ACT_DIGEST_COPY_FILES` and their
    `_activate_*` functions — never inside the selftest battery. → F2.
15. `git diff a4a3451 08f980f -- scripts/check_governance.py` — read all 44
    added lines. Confirmed the AGENTS.md "Governance recorders" pattern:
    the label is registered in `_act_subjects()` guarded by
    `if not any(label == PWB_RENDER_MODE_LABEL ...)` (idempotent), the
    packet copy is added to `ACT_DIGEST_COPY_FILES` unconditionally, and
    `_activate_pwb_render_mode_act_copy_registry()` is existence-gated on
    `os.path.isfile(... PWB_RENDER_MODE_ACT ...)` before requiring the
    aggregate-record copy — matching the sibling
    `_activate_pwb_scoped_amendment_act_copy_registry()` byte-for-byte in
    shape. The docstring at the diff's `+#:` lines explicitly states why
    it is **not** added to `PWB_SUCCESSOR_CHAIN` yet (two candidate
    successors, owner sets performance order); confirmed
    `PWB_SUCCESSOR_CHAIN` (`grep -n PWB_SUCCESSOR_CHAIN
    scripts/check_governance.py`) indeed omits `PWB_RENDER_MODE`.
16. Change class (criterion 4, criterion c): located RFC2-26 via
    `DIRECTIVE-REGISTER.md` at
    `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`.
    Quoted in `SEMANTIC-DELTA.md` and verified byte-exact against the
    source file:
    > No user-observable implementation consequence... may be scheduled
    > solely from this RFC. Before implementation, every observable
    > consequence either maps to an approved OpenSpec requirement and
    > scenario... or carries a reviewed N/A judgment proving it purely
    > structural with no independently testable behavior.
    Read the adopted PWB-REQ-011 scenario at `spec.md:632-677` (pre-patch)
    — its only scenario maps a baseline `openspec/specs/*/spec.md`
    object; no scenario or Case/Observable language reaches a
    non-baseline source. `SEMANTIC-DELTA-TEMPLATE.md`'s Normative test
    ("someone who complied before may not comply now, or the reverse")
    applies directly: an implementation that refuses every non-baseline
    source today complies with the adopted text; after this amendment the
    same behavior would not comply. The argument holds **independent of**
    the exact served-count figure (see F1) — it rests on the population
    shift (refused → some served), which is true regardless of whether
    that population is stated as 77, 269, or left uncounted.
17. Owner rulings (criterion b): read
    `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
    P-81 (line 69, arm A) reads: "Q1 yes for the 77 non-baseline sources
    with a render mode, never for the 9 withheld... gated behind a
    CC-REV-2 scenario to PWB-REQ-011...; Q2 a scroll anchor with the whole
    spec still served...; Q3 one legend sentence in `POLARIS_COPY`
    [explicitly not in this package]; **Q4 machine figures Observed, sums
    Inferred**, the 417-minus-415 delta Unknown; Q5 draft the PWB-REQ-015
    delta only [not this package]." Every clause of arm A that is this
    package's job (Q1, Q2 minus the legend sentence, the render-mode
    scenario) is present; Q3 and Q5 are correctly absent — grepped the
    four patches and `SEMANTIC-DELTA.md` for `POLARIS_COPY` and
    `PWB-REQ-015`: zero hits in either. P-71 (line 58) Q5's "no write into
    an observed repository" is honored — the package edits nothing under
    `openspec/` on this commit (CG-7h binds current bytes to the last
    performed act; the manifest hashes post-apply bytes, applied only in
    a scratch copy by `--apply --at-adoption`, never run against the
    worktree in this review) and no patch touches implementation code.
    P-82 (line 70) is a separate PWB-REQ-002 delta "sequenced behind lane
    B's open manifest" — grepped for `PWB-REQ-002` across the package:
    zero hits; not absorbed.
18. Anchors (criterion 5): `spec.md:776` — "labels, file paths and
    coordinates SHALL never serve as anchor identity" (PWB-REQ-014,
    unpatched by this package). The proposed clause: "an anchor is
    presentation only, SHALL NOT remove, narrow or reorder what the route
    serves without it, and SHALL NOT enter, replace or qualify any
    source, claim or narrative anchor identity." A scroll anchor is a
    coordinate; the proposed text keeps it out of the anchor-identity
    class by its own words, consistent with PWB-REQ-014 needing no
    amendment.
19. Parity (criterion 6): the proposed Oracle/Oracle-independence text
    adds "each source's served mode, or its refusal reason, is
    recoverable in both channels" and "the served/refused partition and
    every expected body come from the evaluation's own source records,
    never from the route's output" — a falsifiable, per-rendered-tuple
    obligation living inside PWB-REQ-011 rather than editing
    PWB-REQ-020's text, matching the brief's framing. Checked against the
    AGENTS.md guardrail "PWB-REQ-020 parity is per tuple, never per id" —
    the added text says "per rendered tuple," not per id; consistent.
20. Vocabulary closure (criterion 7): the set is stated as
    `` `requirement-sections`, `whole-body` `` and immediately followed by
    "The set is closed: a third mode would be a third reading unit, which
    is a new specification question, not a rendering detail" (`design.md`
    hunk). The Falsifier bullet adds "a served mode is outside the closed
    set or wrong for its source class" and the final sentence of the
    invariant paragraph requires "Each served route's mode, source
    identity and each refusal's reason SHALL be recoverable, per rendered
    tuple, from the same evaluation in the machine answer" — closed in
    text, not merely labeled closed, and machine-recoverable.
21. Coverage (criterion 9, confirmed in scratch copy): patched
    `CAPABILITY-COVERAGE.md` — 31 rows total, row 10 restated exactly as
    `SEMANTIC-DELTA.md` quotes it, totals line unchanged: "25 covered, 6
    lawfully out of scope, 0 Unknown/unresolved; 31 total." Diffed every
    other row against the pre-patch file — no other row's text moved.
22. `governingBehaviorContract.version` pins (criterion f):
    `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
    line 18 and
    `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`
    line 25 both pin
    `"sha256:42d073cdeaf7fa7940c5e822b05213267ec1d0064faaaad092f21d264b76a2b1"`
    — the **current, pre-amendment** spec.md digest (matches
    `GOVERNING-DEPENDENCIES.md`'s unpatched Source line). Neither file is
    a row of `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (checked all 11 rows —
    neither path appears), consistent with `IMPACT-LEDGER.md`'s framing
    that this package does not patch them and their staleness is assigned
    to the sequenced registry act.
23. Served-count provenance (criterion h): `grep -n -F "269"` over
    `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md` and
    `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json` —
    **zero hits** in either. The funnel doc's own named methods (Python
    `re` sweep, `Counter` over per-rule tokens, a machine
    `projectShape.sources` walk) produce 278 total, 192 currently served,
    77 non-baseline admitted and 9 withheld — each independently
    `[Observed]`-labeled where it is first stated. `269` never appears as
    a script or capture output anywhere in the package or its cited
    evidence; it is arithmetic (192 + 77) performed in prose. → F1.
24. Owner packet (criterion 12): `OWNER-DECISION-PACKET.md:156` prints the
    phrase `SIGN OFF PWB EXACT-SOURCE RENDER-MODE AMENDMENT:
    5796c1541a90…`; line 160 states it is "**not offered** in this
    packet: no fresh-context review has been run on these bytes yet. If
    you reply with this phrase now, no recorder exists that would accept
    it, and nothing is performed." Consistent with step 12's
    `check_governance.py` run: `PWB_RENDER_MODE_ACT` does not exist on
    disk, so `_activate_pwb_render_mode_act_copy_registry()` is a no-op
    and only the static packet-copy registration is live.
25. Comprehension (criterion 11): restated without re-reading author
    material — the delta lets the exact-source route serve 77 sources it
    refuses today, in a `whole-body` mode, while the 9 withheld sources
    stay refused in both modes and every existing gate still runs on the
    complete body first; the owner's one choice is whether to sign off
    the behavior manifest, which the packet explicitly does not yet
    offer for acceptance. Restatable without author context.

---

## Findings

### F1 — revise. The "269" served-count figure is stated as bare fact in the normative-classification argument, unlabeled, in direct tension with the owner ruling's own instruction that this figure be labeled Inferred.

*Anchor:* `SEMANTIC-DELTA.md:366`.
*Rests on:* verification rule 9 (absence-of-derivation claims need a
sweep — none exists, see step 23); VIS-2 / the epistemic-labeling
discipline (every substantive claim `[Observed]`, `[Inferred]` or
`[Unknown]`); and directly, P-81 (M14) Q4 in
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:69` — the exact ruling
this package implements — which rules "machine figures Observed, **sums
Inferred**".

`SEMANTIC-DELTA.md:366`, inside the Normative change-class argument:

> ...a route that returns a body where it previously returned a refusal is
> independently testable behavior, and the observable population moves
> from 192 served to **269 served** out of 278.

No hedge, no label. `192` and `77` (the two addends) are each independently
`[Observed]` at their own sites in `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md`
and `IMPACT-LEDGER.md`, but `269` is their sum, computed in prose, and never
appears as the output of any named script or retained capture (step 23). The
package's own `OWNER-DECISION-PACKET.md:106` gets this right for the same
number: "Served sources move from 192 of 278 to **269 of 278** `[Inferred —
a sum of...]`". `SEMANTIC-DELTA.md` — the document the review criteria
direct the reviewer to for the change-class argument itself — carries the
unlabeled version, and it is the version load-bearing for criterion 4/16's
judgment.

This does not change the verdict on the Normative classification: the
argument holds on the population-shift fact alone (refused → some served),
independent of the exact count (step 16). But P-81 Q4 is a specific,
named owner instruction about exactly this arithmetic, and the package
fails it in the one document whose whole job is to carry the classification
argument the owner will rely on.

*Resolution:* label `SEMANTIC-DELTA.md:366`'s figure `[Inferred — 192 + 77,
see OWNER-DECISION-PACKET.md]` or equivalent, matching the packet's own
treatment. One sentence.

### F2 — revise. The new `PWB_RENDER_MODE_LABEL` registration in `check_governance.py` has no dedicated, automated `--selftest` fixture; rule 6 is satisfied only by this review's manual mutation, not by the repository's own regression battery.

*Anchor:* `scripts/check_governance.py:6190-6228` (the
`_selftest_pwb_act_copy_registry` call sites); the registration itself at
lines 2028-2033, 2240-2241, 2348-2354 (per `git diff a4a3451 08f980f --
scripts/check_governance.py`).
*Rests on:* AGENTS.md verification rule 6, "Mutate the input and confirm
the check fails, per predicate, before trusting it (`--selftest` holds the
fixtures)" — the parenthetical states where the fixtures are expected to
live; AGENTS.md's "Governance recorders" section, which requires
`--selftest` to include a rule-6 fixture for each new act phrase's
registration (criterion g, second clause, names this explicitly).

Step 14 enumerates every `_selftest_pwb_act_copy_registry(...)` call: the
default (`PWB_STATE1`) case, `PWB_TRUTH_AMENDMENT_LABEL`, a loop over
`POLARIS_GENERATOR_APPROVAL_ACTS`, and `POLARIS_UNDERSTANDING_LABEL`. Neither
`PWB_RENDER_MODE_LABEL` nor its immediate predecessor,
`PWB_SCOPED_AMENDMENT_LABEL`, is passed as the `link` argument anywhere.
`--selftest`'s 0-failing, eight-predicate report (step 4) is real and
correctly exercises the *general* copy-registry mechanism, but it does not
exercise **this package's own label** — which is exactly the CG-7d/CG-7e
surface a future edit to `OWNER-DECISION-PACKET.md` or to the constants
block could silently break. Step 13's manual mutation proves the mechanism
works today; it does not make that proof reproducible by the next session's
`--selftest` run, and rule 7 (battery valid only for the commit it ran
against) means today's manual proof expires at the next edit.

This finding is not new to this commit — `PWB_SCOPED_AMENDMENT_LABEL` has
carried the identical gap since it was registered, and the round-2 review
of that package (`docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md`)
did not raise it as a finding. I raise it here because this commit adds a
second, structurally identical instance of the same uncovered surface, and
criterion g asks specifically whether `--selftest` includes a rule-6
fixture for the new registration — it does not.

*Resolution:* add two call sites mirroring lines 6202-6210 (the
`PWB_TRUTH_AMENDMENT_LABEL` pattern): a `render_mode_link` tuple
`(PWB_RENDER_MODE_LABEL, PWB_RENDER_MODE_SUBJECT, PWB_RENDER_MODE_ACT,
_activate_pwb_render_mode_act_copy_registry)` with `"valid"` and
`"missing-aggregate"` cases. A single follow-up patch could add both this
label and `PWB_SCOPED_AMENDMENT_LABEL`'s missing pair in one change.

### F3 — note. The package's disclosed composability collision covers only the sibling's full patch set; a partial landing of lane B (its `spec.md.patch` alone) is not tool-rejected and is not covered by either package's `--check`.

*Anchor:* `IMPACT-LEDGER.md:106-114` ("Merge and effect boundary" —
"the scoped-attributes candidate... amends the same specification. Its
`GOVERNING-DEPENDENCIES.md` patch and this one both rewrite the single line
that carries the specification's sha256, so they cannot both apply.").
*Rests on:* verification rule 9 (an absence claim — "exactly one line
collides" — needs its scope stated); the same "Merge and effect boundary"
section is what criterion 8/d directs the reviewer to test.

Step 11: applying only `pwb-scoped-attributes-amendment/proposed/spec.md.patch`
(without its own `GOVERNING-DEPENDENCIES.md.patch` or contract patch)
alongside this package's four patches produces no `git apply` or GNU
`patch` rejection in any of four tool/order combinations, and leaves
`GOVERNING-DEPENDENCIES.md` holding whichever amendment's digest applied
last — silently wrong for the other amendment's actual `spec.md` content,
since regeneration never runs in this path. Neither this package's
`--check` (tests the sibling's full three-file set landing first, per
step 3/10) nor a plausible companion check in the sibling package
exercises a partial landing. This is a realistic shape: nothing prevents
someone from cherry-picking lane B's specification patch alone before its
package is otherwise ready.

This does not implicate this package's own claim, which is scoped and
accurate to "the scoped-attributes candidate" as a whole landing — I could
not construct a reading of `IMPACT-LEDGER.md`'s sentence that claims
coverage of a partial lane-B landing. It is a gap in what governance
tooling *catches*, not a false statement in what this package *says*.

*Resolution:* none owed by this package specifically; worth a shared note
in `ROUND-ESTATE.md`-adjacent process guidance, or a `--check` extension
that also asserts `GOVERNING-DEPENDENCIES.md`'s digest line matches a
fresh regeneration of whatever `spec.md` is actually on disk, independent
of which patch set produced it.

---

## Why CONFIRM WITH EXCEPTIONS

The mechanics are sound and independently reproduced: the manifest hashes
exactly the post-apply bytes of all 11 subjects, `--diff` matches the raw
patches byte-for-byte, `--check` and `--selftest` both fail closed under
mutation (steps 10, 13), the 7 unchanged subjects survive a fresh
regeneration of both named generators, and `check_governance.py` neither
breaks nor silently passes when the package directory is deleted. The
`check_governance.py` registration follows the AGENTS.md "Governance
recorders" pattern exactly, and the sign-off phrase is correctly printed as
not-offered. The substance holds on every criterion 1-12: the withholding
invariant is unconditional and textually airtight (step 7), the gates run
on the complete transient body before any encoding (step 8), no wider
content class is reached (step 6/design.md §8), the render-mode vocabulary
is closed in the text itself (step 20), scroll anchors stay out of the
PWB-REQ-014 anchor-identity class (step 18), parity is stated per rendered
tuple (step 19), and the package draws neither the PWB-REQ-002 nor the
`POLARIS_COPY` legend delta P-82 and P-81 Q3 reserve elsewhere (step 17).

Three findings keep it short of CONFIRM. F1 is a one-sentence label fix,
but it fails a specific, named owner instruction (P-81 Q4, "sums
Inferred") inside the one document whose job is to carry the normative
argument the owner reads to judge criterion 4 — the same defect class
AGENTS.md already records for this corpus (an unlabeled or wrong figure in
the artifact the owner is sent to for the claim). F2 is real and
reproducible today only by hand; the repository's own regression battery
does not yet prove it, which is what rule 6 asks for. F3 is disclosure,
not a defect in this package's bytes, but worth recording because the
sibling collision story a reader takes away from `IMPACT-LEDGER.md` is
narrower than "the two packages cannot silently disagree" — they can, in
the partial-landing case, and nothing catches it today.

None of the three touches the specification text's substance or the
withholding/gating invariants. I expect a short round 2, or the owner may
judge F1 and F2 minor enough to accept alongside a repair note.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016rwoqL9MW8v8nLyhQC7iY5
