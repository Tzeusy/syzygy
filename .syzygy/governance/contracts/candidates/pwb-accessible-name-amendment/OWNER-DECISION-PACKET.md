# Owner decision packet — PWB accessible-name amendment (PWB-REQ-016)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts six questions to the owner, and only the
> owner's answer binds anything (VIS-4).
> *(Marked 2026-10-14: eight questions now. The cycle-2 repair added
> Questions 7 and 8.)*

**Status: round 1 `REVISE`, repaired once, unconfirmed; owner decides.**
Drafted 2026-10-03 on bead `syzygy-u05.12` (pursuit move N12, slice C),
register row P-99. One fresh-context round covered this package and the
opening-index (P-98) package together and returned `REVISE`. Under the
coordinator's direction the findings were repaired once and no round 2 was
dispatched; `ROUND-1-DISPOSITIONS.md` beside this file says what each
finding changed. These bytes are not offered as cleared: you decide whether
to sign them, order a confirmation round first, or revise.
*(Marked 2026-10-14: "no round 2 was dispatched" is no longer true, and the
"order a confirmation round first" choice is spent. On your direction of
2026-10-14
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`) the
confirmation round ran over these bytes and returned `REVISE`, one revise
finding and six notes
(`docs/reviews/R-PWB-ACCESSIBLE-NAME-AMENDMENT-2-RAW.md` line 4). The bytes
are still not cleared; the findings are open and classified in
`ROUND-2-DISPOSITIONS.md` beside this file.)*
*(Marked 2026-10-14, later the same day: "the findings are open" is no
longer true. On your further direction that day, relayed by the lead
session, one more cycle ran.)* **Status now: round-2 findings repaired once
on 2026-10-14, unconfirmed pending round 3.** Every round-2 finding, notes
included, was repaired once (`ROUND-2-DISPOSITIONS.md` §"Repairs,
2026-10-14 (cycle 2)"). One fresh round 3 is briefed in
`../pwb-opening-index-amendment/REVIEW-BRIEF.md` §"Round 3": a notes-only
verdict clears the bytes it reads, and a `REVISE` comes back to you with
its findings. Two repairs needed your content choice and are put to you as
Questions 7 and 8.

## What you would be signing

One amendment to PWB-REQ-016, the requirement that Polaris works without
sight or a mouse. Read `SEMANTIC-DELTA.md` for the full account. In short:

- **Links that go to different places get different names.** A screen
  reader announces a link's name, not where it sits. If many links to
  different sources are all called the same thing, a reader who cannot see
  cannot tell them apart. After this, a repeated label carries the name of
  the item or source it belongs to. *(Marked 2026-10-14: no longer exact.
  In the repaired version every
  name that shares a visible label with a link going elsewhere starts with
  that label, and a link to an exact-source page then adds that source's
  file path. Other repeated labels, such as a toggle repeated per figure,
  must still differ but need not name an item (Question 7).)*
- **Headings do not skip levels.** One top heading, and no jump from a
  level-2 heading straight to a level-4 one, so the page's outline can be
  followed by ear.
- **Checked over every Polaris page.** Both checks run over every link,
  toggle and heading of every Polaris page served for a full Butlers
  evaluation, including each exact-source page, and say how many pages and
  elements they checked. Today's checker checks that names exist, not that
  they differ, and reads no heading levels.
- **Butlers' own headings are left as written.** Where an exact-source page
  shows a Butlers document verbatim, its headings are counted but not held
  to the heading rule, because Polaris may not rewrite them.
  *(Marked 2026-10-14: no longer in this version. The review found that an
  exact-source page shows a Butlers document as plain preformatted text,
  with no headings at all. Where Polaris does render Butlers' headings, on
  the entry page, it already sets their levels itself. So the exemption
  covered nothing, and now every heading is held to the rule
  (Question 8).)*

**What it touches besides PWB-REQ-016.** Only the regenerated dependency
file, whose one changed line is the specification digest. No other
requirement, capability row, contract-coverage row or warrant moves.

**What signing does not do.**

- **It starts no implementation.** A build needs a separate authorization.
- **It touches no other surface.** Trajectory, Orrery and the home page are
  governed by the Three-Surface POC specification (question 4).
- **It quotes no current figure.** [Unknown] How many links, toggles and
  headings Butlers' Polaris has today and how many names they share. The
  pursuit's figures came from an untracked capture and are not repeated
  here; they are measured on a fresh private-daemon capture at a named
  commit when this is built.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| Sign v1.0 (the repaired bytes are unconfirmed) | The patch is applied in the sign-off change by version tag (Scope A covers PWB specification deltas). PWB-REQ-016 gains the two checks, the population rule and two scenarios. |
| Decline | PWB-REQ-016 stays as signed: same-named links to different places stay lawful. |
| Revise | Name what to change; a new version gets a new review round. |
| **Order one confirmation round** (recommended) | One fresh-context round over the repaired bytes; a notes-only verdict clears them for signing. |

*(Marked 2026-10-14: the confirmation-round option is spent. Round 2 ran
and returned `REVISE`; on your direction the findings were repaired once
and round 3 is briefed. Until round 3 returns, this version is not offered
for signing, so Question 1 waits on round 3.)*

## Question 2 — which elements must have distinct names

| Option | Meaning |
|---|---|
| **Links, buttons, disclosure toggles and form controls** (recommended; this version) | Every element a keyboard reader can land on. The pursuit found toggles sharing names as well as links. |
| Links only | Smaller change to build; a reader still meets many toggles with one name and no way to tell them apart. |

## Question 3 — how strict the heading rule is

| Option | Meaning |
|---|---|
| **Exactly one top heading and no skipped level** (recommended; this version) | The common screen-reader convention. |
| No skipped level only | Allows several top headings. |

## Question 4 — slice D: the other surfaces (not drafted)

The bead also asked to run these checks against Trajectory, Orrery and the
home page. Those surfaces are governed by POC-REQ-061, "The accessibility
floor holds on every surface", in the separately signed Three-Surface POC
specification. An OpenSpec change covers one category and overlaps no other,
so that work cannot ride in a PWB package.

| Option | Meaning |
|---|---|
| **File a separate POC-REQ-061 bead** (recommended) | The coordinator files it; it starts with its own premise check against the POC specification. |
| Drop it | Only Polaris gets the checks. |

Slice B, offsets in the walkthrough record, belongs to the opening-index
package and is put to you there (its question 6).

## Question 5 — order against the other pending packages

The opening-index (P-98), anchor-resolution (P-96, PWB-REQ-014),
class-granular (P-86) and release-label (P-85) packages are pending over
the same signed specification. Their spec changes compose in any order —
all 120 orders of the five spec patches apply to one identical result,
re-derived 2026-10-03 (an earlier count of 24 orders over four patches
omitted P-96) — and P-85 and P-86 also share a design decision and a
capability row number. Each manifest is built over the current tree.
*(Marked 2026-10-14: the anchor-resolution package (P-96) is no longer
pending. You signed it v1.0 that day, so four spec patches remain
pending. This package was regenerated over the moved specification in the
cycle-2 repair.)*

| Option | Meaning |
|---|---|
| **Whichever is ready first lands first** (recommended) | The second is regenerated over the first's applied bytes and reviewed again before it is offered. |
| Sign with the opening index | Both are signed in one change; the second manifest is regenerated in that change and reviewed first. |

## Question 6 — which pages the checks cover

| Option | Meaning |
|---|---|
| **Every Polaris page at one evaluation** (recommended; this version) | The entry page and each exact-source page. A reader reaches the exact-source pages through the same links, so they are part of what a nonvisual reader must navigate. |
| The entry page only | A smaller build, but every other Polaris page stays unchecked. |

*(Added 2026-10-14: the repaired version also says where the page list
comes from. It is the entry page plus one exact-source page for each source
the machine answer lists, whether that page shows the source or refuses
it. The list never comes from the links Polaris draws.)*

## Question 7 — what a shared label must add (added 2026-10-14, cycle 2)

The round-1 repair said that the words a repeated label adds "name the item
or source by the identity PWB-REQ-014 renders for it". The round-2 review
found that nothing checked this, and that the identity was not pinned (raw
finding 1). This version says that any element sharing its visible label
with an element that goes elsewhere has a name that starts with that label.
Where it leads to an exact-source page, the name then includes that
source's file path, which the check takes from the machine answer.

| Option | Meaning |
|---|---|
| **The label first, plus the file path for exact-source links** (recommended; this version) | Checkable from outside the renderer. Other repeated labels, such as a toggle repeated per figure, must still differ but need not name an item. [Unknown] Whether the machine answer already carries every source's path was not checked; if not, the machine answer needs it too. |
| The label first, nothing more | Drops the path. Names still differ, but what they add is up to the renderer. |
| Name the item or source for every repeated label | Needs the specification to say which item or source each target belongs to. Not drafted. |

## Question 8 — whether any heading is exempt (added 2026-10-14, cycle 2)

The round-1 version exempted headings "inside a verbatim Butlers body". The
round-2 review found the exemption covered nothing: exact-source pages show
Butlers documents as preformatted text with no heading elements, and
Butlers' headings on the entry page get their levels from Polaris (raw
finding 4). This version exempts no heading.

| Option | Meaning |
|---|---|
| **No exemption** (recommended; this version) | Every heading Polaris renders is held to the rule. Polaris sets those levels already, so it can close a gap without changing a word of Butlers' text. |
| Exempt headings Polaris shows exactly as Butlers wrote them | Only matters if a future mode renders Butlers' headings at their own levels. Needs a way for the check to recognize those headings. Not drafted. |

**If unanswered,** nothing is signed and the package stays a candidate.
