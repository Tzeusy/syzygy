# Owner decision packet — PWB opening-index amendment (PWB-REQ-010)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts seven questions to the owner, and only the
> owner's answer binds anything (VIS-4).

**Status: round 1 `REVISE`, repaired once, unconfirmed; owner decides.**
Drafted 2026-10-03 on bead `syzygy-u05.12` (pursuit move N12, slice A),
register row P-98. One fresh-context round covered this package and the
accessible-name (P-99) package together and returned `REVISE`. Under the coordinator's
direction the findings were repaired once and no round 2 was dispatched;
`ROUND-1-DISPOSITIONS.md` beside this file says what each finding changed.
These bytes are not offered as cleared: you decide whether to sign them,
order a confirmation round first, or revise.

## What you would be signing

One amendment to PWB-REQ-010, the requirement that Polaris opens with the
whole project. Read `SEMANTIC-DELTA.md` for the full account. In short:

- **A nine-row index at the top.** One row per walkthrough question (why,
  promises, non-goals, capabilities, exact requirements, gaps, claim
  strength, architecture, V1 success), each linking to a target the
  specification names. If a target is missing, its row says so and links
  nowhere.
- **How far in each one starts.** Each row shows the word at which its
  target begins, and one line after the last target gives the largest of
  those numbers and the page's total. Words are counted one stated way, so
  anyone can recount them.
- **Never a verdict.** The index does not say a question is answered, is
  not a claim, and stays out of the walkthrough record. Whether the page
  makes Butlers understandable stays your judgment (RFC7-31).

**What it touches besides PWB-REQ-010.** Only the regenerated dependency
file, whose one changed line is the specification digest. No other
requirement, capability row, contract-coverage row or warrant moves.

**What signing does not do.**

- **It starts no implementation.** A build needs a separate authorization.
- **It reads nothing new.** No Butlers body is read beyond the consented
  class.
- **It quotes no current figure.** [Unknown] Where the nine targets begin on
  Butlers' Polaris today, and how long it is. The pursuit's figures came
  from an untracked capture and are not repeated here; they are measured on
  a fresh private-daemon capture at a named commit when this is built.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| Sign v1.0 (the repaired bytes are unconfirmed) | The patch is applied in the sign-off change by version tag (Scope A covers PWB specification deltas). PWB-REQ-010 gains the index, the offsets and two scenarios. |
| Decline | PWB-REQ-010 stays as signed: no index, and nothing tells a reader where the project material ends. |
| Revise | Name what to change; a new version gets a new review round. |
| **Order one confirmation round** (recommended) | One fresh-context round over the repaired bytes; a notes-only verdict clears them for signing. |

## Question 2 — what the rows are keyed to

| Option | Meaning |
|---|---|
| **The nine walkthrough identities of PWB-REQ-021** (recommended; this version) | The rows are the questions the cold-open walkthrough asks, in its order. |
| The project categories PWB-REQ-010 lists | The rows follow the order the opening already uses (purpose, promises, non-goals, architecture, V1 scope, success criteria). Simpler, but "where exactness lives", "one Unknown" and "claim strength" would have no row. |

Two targets in this version are narrower than their questions, and the
review asked that you see them: the `gaps` row goes only to the opening
Unknown aggregate, so a project with a contradiction and no Unknown shows
that row as not rendered; and the non-goals row goes to the non-goal
statements, while RFC7-30 also asks the reader to reach a non-goal's rule
text. Widening either is a revision.

## Question 3 — how words are counted

| Option | Meaning |
|---|---|
| **Words in the flow on arrival** (recommended; this version) | Text inside a collapsed disclosure is left out until opened, but its visible toggle label counts; hidden text and the index itself are left out. The numbers describe the page a reader actually sees first. |
| Every word, collapsed or not | Larger numbers that describe a page nobody reads in one pass. |

## Question 4 — should the offsets also be machine-readable?

| Option | Meaning |
|---|---|
| **No, human surface only** (recommended; this version) | The offsets describe the rendered page, not Butlers, so they stay out of the machine answer and out of the PWB-REQ-020 parity sweep. |
| Yes | The machine answer carries them too. That makes them a new parity family and needs a further amendment to PWB-REQ-020. |

## Question 5 — what kind of copy the numbers are

PWB-REQ-012 requires every Polaris string to carry exactly one of four roles.

| Option | Meaning |
|---|---|
| **Row names are action labels; the offsets and the stopping line are scope instructions; an unrendered row's text is an epistemic disclosure** (recommended; this version) | The numbers tell a reader how much there is to read, which is what a scope instruction does. This version reads PWB-REQ-012's limit of one entry scope instruction as covering only the statement of the POC bound, and places the index before PWB-REQ-014's narrative tree, outside its units. Both readings are yours to confirm. |
| A new role | Needs an amendment to PWB-REQ-012's closed set. |

## Question 6 — slice B: offsets in the walkthrough record (not drafted)

The bead also asked to record, in the PWB-REQ-021 walkthrough record, the
word at which each answer was reached.

- **What the clauses allow.** PWB-REQ-021 already says the record SHALL
  "retain every path used to answer them", and that readiness and the nine
  answers SHALL "remain execution facts, never a verdict or proof of
  comprehension" (PWB spec, lines 1934 and 1941–1943 at `c371339d`). The word at which *you* found an answer is a fact about your
  path, so recording it would be lawful as an execution fact.
- **Why it was not drafted.** It is a separate amendment to PWB-REQ-021,
  and only your own run produces the number, so no machine could fill it in
  before you walk through. It also risks reading as a reach score, which
  RFC7-31 forbids ("never a score").

| Option | Meaning |
|---|---|
| **Leave it for now** (recommended) | Slice A's index gives the declared targets' offsets. Revisit after your first walkthrough. |
| Draft it as an optional PWB-REQ-021 amendment | A new package with its own review round. |

## Question 7 — slice D: accessibility on the other surfaces (not drafted)

The bead also asked to run the checks against Trajectory, Orrery and the
home page.

- **Why it is not here.** Those surfaces are governed by POC-REQ-061, "The
  accessibility floor holds on every surface", in the separately signed
  Three-Surface POC specification. An OpenSpec change covers one category
  and overlaps no other, so that work cannot ride in a PWB package.

| Option | Meaning |
|---|---|
| **File a separate POC-REQ-061 bead** (recommended) | The coordinator files it; it starts with its own premise check against the POC specification. |
| Drop it | Only Polaris gets the checks in slice C. |

## Order against the other pending packages

The accessible-name (P-99), anchor-resolution (P-96, PWB-REQ-014),
class-granular (P-86) and release-label (P-85) packages are pending over
the same signed specification. Their spec changes compose in any order —
all 120 orders of the five spec patches apply to one identical result,
re-derived 2026-10-03 (an earlier count of 24 orders over four patches
omitted P-96) — and P-85 and P-86 also share a design decision and a
capability row number. Each manifest is built over the current tree, so
whichever is signed second is regenerated and reviewed again first.

**Interaction with the P-95 re-pin.** Signing this package moves PWB
`spec.md` again. The behaviour-contract pins that P-95's re-pin acts would
write (registry entry and secret-classification policy, re-pinned to the
tree-framing sign-off) would then be stale once more, and R6 would report
them Unknown until a further re-pin. If P-95 is performed first, signing
this package re-stales it; if this package is signed first, P-95's acts
must be regenerated against the new `spec.md` before they are performed.

**If unanswered,** nothing is signed and the package stays a candidate.
