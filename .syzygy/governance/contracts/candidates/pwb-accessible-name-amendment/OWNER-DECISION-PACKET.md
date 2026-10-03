# Owner decision packet — PWB accessible-name amendment (PWB-REQ-016)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts six questions to the owner, and only the
> owner's answer binds anything (VIS-4).

**Status: round 1 `REVISE`, repaired once, unconfirmed; owner decides.**
Drafted 2026-10-03 on bead `syzygy-u05.12` (pursuit move N12, slice C),
register row P-99. One fresh-context round covered this package and the
opening-index (P-98) package together and returned `REVISE`. Under the
coordinator's direction the findings were repaired once and no round 2 was
dispatched; `ROUND-1-DISPOSITIONS.md` beside this file says what each
finding changed. These bytes are not offered as cleared: you decide whether
to sign them, order a confirmation round first, or revise.

## What you would be signing

One amendment to PWB-REQ-016, the requirement that Polaris works without
sight or a mouse. Read `SEMANTIC-DELTA.md` for the full account. In short:

- **Links that go to different places get different names.** A screen
  reader announces a link's name, not where it sits. If many links to
  different sources are all called the same thing, a reader who cannot see
  cannot tell them apart. After this, a repeated label carries the name of
  the item or source it belongs to.
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

| Option | Meaning |
|---|---|
| **Whichever is ready first lands first** (recommended) | The second is regenerated over the first's applied bytes and reviewed again before it is offered. |
| Sign with the opening index | Both are signed in one change; the second manifest is regenerated in that change and reviewed first. |

## Question 6 — which pages the checks cover

| Option | Meaning |
|---|---|
| **Every Polaris page at one evaluation** (recommended; this version) | The entry page and each exact-source page. A reader reaches the exact-source pages through the same links, so they are part of what a nonvisual reader must navigate. |
| The entry page only | A smaller build, but every other Polaris page stays unchecked. |

**If unanswered,** nothing is signed and the package stays a candidate.
