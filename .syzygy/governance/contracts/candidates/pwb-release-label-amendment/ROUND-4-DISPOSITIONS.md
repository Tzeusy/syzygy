> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fourth fresh-context review of the PWB release-label
> amendment package (P-85). This record is not a package artifact: the
> manifest does not hash it and no builder reads it. It classifies each
> round-4 finding and repairs nothing: every finding is open for the owner.
> It offers nothing and performs no act (VIS-4).
> *(Marked 2026-10-14, cycle 3: "repairs nothing" and "every finding is
> open for the owner" describe the record as first written. On the owner's
> cycle-3 direction every finding was repaired once; the mapping is
> §"Repairs, 2026-10-14 (cycle 3)" at the end. The record still offers
> nothing and performs no act.)*

# Round 4 dispositions — PWB release-label amendment

Reviewed record: docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md

- **Reviewed commit (raw line 2):**
  `8acb0795562c548201e24eb6a20d8eddc66f04d1`, the merge of the cycle-2
  repair (#424).
- **Manifest file digest (raw line 3):**
  `73cca446620b99bc6626adcc2530817fb4ef2c55d6a428d20f16150077fbca61`.
  [Observed 2026-10-14] It re-derives from the manifest file's bytes at
  the reviewed commit, and the file is unchanged on the integration
  branch.
- **Verdict (raw line 4):** `REVISE`. One revise finding (1) and seven
  notes (2–8), no blocking finding (raw line 206).
- **Why the round ran.** The owner's direction of 2026-10-14 for a second
  cycle, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
  repair every finding, notes included, then one fresh review under the
  same stopping rule. The brief's §"Round 4" set that rule before the
  round: "Any other verdict sends the package to the owner with its
  findings open. No round 5 is dispatched without a new owner
  instruction."
- **Stopping rule applied.** So:
  - **The package is not repaired again.** The only edits after the round
    are dated status marks at the "unconfirmed pending round 4" sentences
    in the packet, the delta and `ROUND-3-DISPOSITIONS.md`, with the old
    text kept. `REVIEW-BRIEF.md` is not edited; its heading "Round 4
    (added 2026-10-14, cycle 2; not yet dispatched)" is no longer true,
    and this record carries the correction.
  - **No round 5 is dispatched** without a new owner direction.
  - **The bytes are not cleared** and this version is not offered for
    sign-off. This record recommends nothing on Q1–Q5.
  - *(Marked 2026-10-14, cycle 3: "The package is not repaired again" and
    "No round 5 is dispatched without a new owner direction" are
    superseded. The new direction came the same day: "One more cycle each"
    for P-85 and P-98, given by structured question in the lead session.
    Every round-4 finding, notes included, was repaired once; see the
    section at the end. Round-4 findings repaired once on 2026-10-14,
    unconfirmed pending round 5. This record dispatches nothing.)*
- **What the round confirmed.** Round-3 finding 2 and notes 3–7 are
  repaired; round-3 finding 1 is partly repaired (raw lines 59–67). Every
  check passes in a clone, the sibling builders pass, and criteria 3, 4, 5
  and 7 are met (raw lines 69–77).

## Dispositions

| # | Level | Finding (short) | Raw line | Disposition |
|---|---|---|---|---|
| 1 | revise | The provenance-stamp exception is decided by the implementation's own mark and a bare-id text shape, so a page that marks every naming of the revision as a stamp passes every decide-line; "lead with" has no observable; the falsifier has no limb for a naming presented as a stamp. The ledger itself prescribes wrapping prose namings (`polaris.ts` lines 1190, 1209) in stamps | 81 | **Open for the owner.** Raw's repair: make the stamp structural (only the revision element of a citation attached to an anchored claim, source, leaf or refusal, verified from the anchor records); a revision id in prose, a heading or the shape-identity section is never a stamp; the first naming on each page is a label unit with the label before the full id; add the falsifier limb. Or, if the owner prefers bare stamps in prose, a named choice, with the "cannot hide a naming" claim withdrawn. |
| 2 | note | The footer's evaluation identity (`polaris.ts` line 1881) shows the full observed revision on every page, matches no exception, and is missing from the ledger's inventory | 133 | **Open.** Name it in the inventory and say which treatment the text intends. |
| 3 | note | The status-line exception's warrant ("which the POC specification governs") is unanchored, since no POC requirement names the line; whether `data-human-status` is the mark is unstated | 146 | **Open.** Anchor or withdraw the warrant; say which mark. |
| 4 | note | The stability sweep is narrower than its falsifier limb and is blind to split text nodes | 151 | **Open.** Align the limb to the list or name the gap there; define the sweep over an element's whole text. |
| 5 | note | Construction records name test-3 conditions no fixture builds (unadmitted ancestry read, unreadable commit in a full clone, grafted object database) | 160 | **Open.** Add the fixtures or narrow test 3's observed population. |
| 6 | note | "Every Polaris page" has no stated population; the draft view carries no project-shape identity under PWB-REQ-020 | 177 | **Open.** Name the population, for example the human HTML routes under `/polaris`, excluding the PWB-REQ-020 machine and draft views. |
| 7 | note | Three load-bearing wordings are guarded only by the dependency digest; `lost_lines` can match a signed line to a later identical twin | 187 | **Open.** Add the three wordings to `REQUIRED_ONCE`; make `lost_lines` duplicate-safe. |
| 8 | note | The order check covers `spec.md` only; `design.md` (two decisions numbered 12) and `CAPABILITY-COVERAGE.md` (row 34 in both) collide with class-granular | 197 | **Open.** Already disclosed and routed to P-86's Q5 (whichever is signed second is regenerated and reviewed again). P-86's round 4 has since cleared, which does not resolve the collision. |

**Stale sentences outside the marked files.** Register row P-85 and
`docs/README.md`'s release-label row sit outside the package and are
updated directly.

## Repairs, 2026-10-14 (cycle 3)

Made under the owner's direction of 2026-10-14, given by structured
question in the lead session: "One more cycle each" for P-85 and P-98,
that is, repair every finding, notes included, then one fresh review under
the same stopping rule (a notes-only round clears its bytes; a `REVISE`
returns to the owner). The repair base is `main` at `7460aec8`.

**The base moved.** The class-granular extraction amendment (P-86) was
signed v1.0 at `235b71eb`. Under its Question 5 answer, "First ready lands
first", the package signed second is regenerated over the first's applied
bytes and reviewed again. [Observed 2026-10-14] At `7460aec8` this
builder's `--check` failed, because `CAPABILITY-COVERAGE.md.patch` no longer
applied. Worse, `design.md.patch` still applied, but `git apply` relocated
it after P-86's decision, leaving two decisions numbered `### 12.`. That is
the silent collision round-4 Note 8 described. The five authored patches
were rewritten over the signed bytes. Design decision 12 became 13 and
capability row 34 became 35, with totals 29 covered, 6 lawfully out of
scope, 0 Unknown, 35 in all. The two derived patches and the manifest were
regenerated with `--write`, never hand-edited.
`CONTRACT-COVERAGE.md.patch` and the repair-delta patch are byte-identical
to round 4's, so the contract-coverage totals are unchanged.

**Round-4 findings repaired once on 2026-10-14, unconfirmed pending round
5.** The dispositions above keep their **Open** marks: they describe the
round-4 bytes. None of these repairs is accepted until round 5 reads it.

Line numbers below are in `proposed/spec.md.patch` (`spec`) and
`scripts/build_pwb_release_label_amendment.py` (`builder`) at this commit.

| # | Finding | Repair |
|---|---|---|
| 1 | The provenance-stamp exception is decided by the implementation's own mark; "lead with" has no observable; no falsifier limb for a naming presented as a stamp (revise) | The raw's proposed repair, adopted (raw lines 124–129). **The stamp is structural** (spec 33–41). It is only the revision element of one citation. A citation is an element holding a cite and its stamp and no other letter or digit. The cite names, by identity, one anchor the machine narrative serves or one source record the machine answer serves, and the stamp's whole text must be that record's revision. "A revision id in a sentence, a heading or any other running text is therefore never a stamp." The excepted kinds are found by mark but decided by "what the checker reads … never the mark alone" (spec 30–32). The oracle reads the named record and the citation and "decides the kind from those alone" (spec 184–187). The decide-line requires the citation, the named served record and the matching revision (spec 216–219). Oracle independence: "No excepted element's kind is taken from its mark: the mark only finds it" (spec 241–242). **"The label leads" now has an observable** (spec 24–27): within each label unit the label precedes the full id, and on each page the first swept occurrence outside the status line lies in a label unit. The sweep reports document position (spec 182), with a decide-line (spec 212–214) and a falsifier limb (spec 248–250). **New falsifier limb** "a naming of the observed revision marked as a provenance stamp" (spec 253–255). The delta's claim that a stamp "cannot hide a naming" is withdrawn, marked at the sentence. The alternative the raw left to the owner, bare stamps in prose, is **Question 6** (recommended: only citations hold stamps). The ledger's "wraps its id in a marked stamp" is withdrawn at the sentence, with the occurrences re-sorted. |
| 2 | The footer's evaluation identity shows the full revision, fits no exception, and is missing from the inventory (note) | Treatment named: a fourth excepted kind, **an identity shown whole** (spec 42–46). Its whole text must equal the evaluation identity the machine answer serves, or the whole value of a served record's own `identity` field, and it must not be a revision's id alone. It has a decide-line (spec 220–222) and a falsifier limb (spec 256–257). It keeps RFC6-15's evaluation stamp and the signed Observable's identities visible, rather than reformatting them (delta, cycle-3 choice 3). The ledger inventory, re-measured at `7460aec8`, now names the footer on both page kinds (`polaris.ts` line 1881, `polaris-source.ts` line 140). It also names three occurrences round 4 did not: the exact-source route's source identity line (`polaris-source.ts` line 117, excepted as an identity), its eyebrow "Polaris · Butlers" plus the prefix (line 135, which must become the page's label unit under the lead rule), and the currency-probe band's full revision (`polaris.ts` line 466, running text). |
| 3 | The status-line exception's warrant is unanchored; whether `data-human-status` is the mark is unstated (note) | **Warrant withdrawn, not anchored:** no anchor exists. The exception now reads "No requirement of this specification or of the Three-Surface POC specification names that line; this requirement excepts it on Polaris and governs nothing else in it" (spec 51–54). [Observed at `7460aec8`] `operability`, `status line` and `page shell` return no hit in the POC spec. The delta's §"Scope: Polaris only", the design bullet and Question 5 are marked or updated to match: on Polaris the line is governed by neither specification. **The mark:** the delta says the existing `data-human-status` attribute (`page-shell.ts` line 55) [Inferred] can serve, so no change to `page-shell.ts` is needed. The requirement names no attribute, as the signed spec names none. |
| 4 | The stability sweep is narrower than its falsifier and blind to split text nodes (note) | Both halves. **Whole text:** the prohibition and the fifth sweep read a *block*, "the nearest enclosing paragraph, list item, table cell, heading, caption or summary element, read as its whole text" (spec 113–120). The sweep now says "a tag name and a term in different inline elements of one block are read together" (spec 205–209), so `<code>v1.0.23</code> unchanged` is found. **Limb aligned and gap named:** the five terms are in the requirement, "matched case-insensitively". The requirement says "The term list is closed: a paraphrase outside it is not decided by this requirement." The falsifier limb is now "a stability term in a label unit, the label record or a block holding a captured tag name" (spec 266–267). |
| 5 | Construction records name test-3 conditions no fixture builds (note) | **Fixtures added** (spec 146–149): a complete clone with a tag on an ancestor and none at the revision, observed three ways. In the first, the tag-set read is admitted and the ancestry read is not. In the second, one commit of the revision's history is made unreadable. In the third, a graft boundary is imposed on its object database. Each of test 3's three conditions now has a fixture. Test 3's observed population is unchanged. |
| 6 | "Every Polaris page" has no stated population (note) | **Population named** (spec 13–17): "the human HTML responses to `GET /polaris` and to every request of PWB-REQ-011's exact-source route, served or refused, in every mount form". The machine answer, PWB-REQ-020's derived machine views and generation draft view, and the response to a human re-observation request "are not Polaris pages". The re-observation exclusion is a named drafter choice (delta, cycle-3 choice 4). |
| 7 | Three load-bearing wordings guarded only by the dependency digest; `lost_lines` can match a later twin (note) | **Guards:** `REQUIRED_ONCE` gains 28 round-4 phrases (builder 186–222), including the new wordings of all three the raw named: the status-line exception, the stamp's purpose clause ("The cite names, by its identity, …"), and the closed term list. The reviewer's three mutants are now selftest mutants that fail on their own phrase predicates: "status-line exception widened", "stamp purpose clause deleted" and "stability terms narrowed" (builder 841–908). **Twins:** `lost_lines` was not changed. Its docstring (builder 444–453) gives the reason. Earliest-later matching is exact for the subsequence property, twins included. A deletion that leaves the signed lines a subsequence gives bytes identical to an insertions-only edit, so no byte check can tell the two apart. `--selftest` now checks `lost_lines` against an independent longest-common-subsequence count, over 4,000 seeded random texts drawn from three lines, one blank (builder 1029–1058). A new mutant, "signed blank line deleted", fails on the lost-line predicate. Rule 6 over the new selftest: an order-blind `lost_lines` substituted for the real one fails it. |
| 8 | The order check covers `spec.md` only; `design.md` and `CAPABILITY-COVERAGE.md` collide with class-granular (note) | **Resolved by regeneration:** P-86 is signed and this package now sits over its bytes as decision 13 and row 35. **Guarded for the future:** `companion_order_findings` (builder 653–686, called from `check` at 721) runs the all-orders search over each companion subject this package patches (`CAPABILITY-COVERAGE.md`, the repair delta, `design.md`, `proposal.md`) that a pending sibling also patches. Today neither pending sibling does: accessible-name and opening-index patch only `spec.md` and the derived dependency file. The capability rows (builder 475–477) and the design decisions (builder 519–523) must stay numbered 1..n in order, which catches the silent `### 12.` duplicate even when a patch applies. New selftests: "capability row number reused", "design decision number reused" and a colliding companion patch (builder 1061–1078). Rule 6: the colliding-patch selftest fails when the companion check is disabled. |

**Builder, besides Notes 7 and 8.** `ORDER_POPULATION` (builder 1081)
drops the class-granular package, which its sign-off moved to
`PERFORMED_SIBLINGS`. The one mutant that named a removed round-3 wording,
"provenance stamp unbounded", was re-targeted to the new text. The selftest now runs 54 structure mutants (37 before).
Requirement count 17; scenarios 60, which is 56 signed plus the same four
new ones.

**Checks run at this commit** (outputs read, not exit codes):

- `build_pwb_release_label_amendment.py --check`: "release-label candidate
  matches 11 proposed subjects (7 patched); 17 requirements, 60 scenarios;
  structure, regeneration, contract coverage, sibling classification and
  pending-patch order verify".
- `--selftest`: "54 structure mutants, patch drift, an unclassified
  sibling, the pending patch population, divergent and failing application
  orders, a colliding companion patch, and the lost-line guard against an
  independent subsequence count all fail closed on their own predicates".
- [Observed at `7460aec8`] Both pending sibling builders' `--check` fail
  before their order check. Each fails on its own derived
  `GOVERNING-DEPENDENCIES.md.patch`, made stale by P-86's sign-off, and is
  regenerated on its own branch.

**Left for the owner.** Finding 1's alternative is **Question 6**. Question
5 is unchanged in its options; its text now says the line is governed by
neither specification. The five drafter choices in the delta's §"Choices
the cycle-3 repair made" can be changed by answering Question 1 *Revise*.
