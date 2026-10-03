# Owner decision packet — PWB accessible-name amendment (PWB-REQ-016)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts five questions to the owner, and only the
> owner's answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 on bead `syzygy-u05.12` (pursuit move N12,
slice C), register row P-99. One fresh-context review round covers this
package and the opening-index package (P-98) together; its verdict and what
it found are in `ROUND-1-DISPOSITIONS.md` beside this file once the round
has run. Until then these bytes are unreviewed.

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
- **Checked over the whole page.** Both checks run over every link, toggle
  and heading of a full Butlers page and say how many they checked. Today's
  checker checks that names exist, not that they differ, and reads no
  heading levels.

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
| **Sign v1.0** (recommended if the round clears it) | The patch is applied in the sign-off change by version tag (Scope A covers PWB specification deltas). PWB-REQ-016 gains the two checks, the population rule and two scenarios. |
| Decline | PWB-REQ-016 stays as signed: same-named links to different places stay lawful. |
| Revise | Name what to change; a new version gets a new review round. |

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

The opening-index (P-98), class-granular (P-86) and release-label (P-85)
packages are pending over the same signed specification. Their changes do
not overlap and compose in any order, but each manifest is built over the
current tree.

| Option | Meaning |
|---|---|
| **Whichever is ready first lands first** (recommended) | The second is regenerated over the first's applied bytes and reviewed again before it is offered. |
| Sign with the opening index | Both are signed in one change; the second manifest is regenerated in that change and reviewed first. |

**If unanswered,** nothing is signed and the package stays a candidate.
