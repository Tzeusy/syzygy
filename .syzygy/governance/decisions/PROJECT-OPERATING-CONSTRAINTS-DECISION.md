# Owner decision packet — project operating constraints (P-35)

> **This file decides nothing.** It exists because the launch-gate pilot
> administration (2026-08-09, question A6) swept 281 tracked files and
> found **zero statements of the project's own resources** — every
> budget/capacity hit was about mission or context budgets inside the
> product design. The shape (V0-mandatory 3D map, machine endpoints,
> propagation proof, seven-class independent review) silently assumes a
> capacity no artifact states. Only the owner knows the real values.
> Queued as **P-35** in `PENDING-OWNER-DECISIONS.md`.

## Question

State (or approve honest `Unknown` for) the project's actual operating
constraints, so the shape's assumptions can be checked against them.

## What the owner is asked to fill in

Every row accepts a range or `Unknown`; **inventing a value is worse than
recording Unknown** (VIS-2 applied to the project itself). No row commits
the owner to anything — a stated constraint is a fact, not a promise.

| Constraint | Owner's statement |
|---|---|
| Number of human operators | 1 (the owner) |
| Engineering attention available (hours/week, honest range) | Unknown |
| Independent-review capacity (who besides Claude-family agents can review — other model families? humans? none?) | Claude-family agents plus the owner; occasional ad hoc ChatGPT/GPT-family review, no fixed cadence |
| Model/provider budget (monthly ceiling, or Unknown) | Unknown |
| Maximum concurrent workstreams the owner will supervise | Unknown |
| Target proving project(s) for V0 (doctrine says "the owner's other live projects"; name them or defer) | Unknown / deferred — not named at this sitting |
| Time horizon (what cadence of progress makes this worth continuing; explicitly NOT a deadline) | Steady progress, no fixed cadence — explicitly not a deadline |
| Scope-reduction triggers (what circumstance cuts V0 scope — e.g. "if independent-review capacity stays at zero for X months, the seven-class review bar is renegotiated as its own decision") | Owner's standing case-by-case judgment; any doctrine-level consequence is a request for a separate doctrine-amendment question, per the limit below, never enacted directly by this statement |

### The limit on a scope-reduction trigger

**A trigger may request a doctrine amendment. It may not enact one.** `V0`'s
mandatory content is fixed by adopted doctrine — `doctrine/v1.md` states that
*"the owner has mandated **3D** as V0's realization of the constitutional
spatial requirement"* — and doctrine changes only through a doctrine
amendment (VIS-4). A constraints statement is a record of **capacity**; if a
trigger would move, defer, or thin anything doctrine mandates at V0, the
lawful form is *"this circumstance opens a doctrine-amendment question"*,
carried to the owner as an amendment, and never a line in this table that
quietly makes it so.

*This limit is stated because the row's own former example broke it.* It read
"if X months pass without spec authoring, the 3D map moves to V1" — which is
exactly a doctrine-mandated V0 element being moved by a capacity statement.
*(Corrected 2026-08-13, owner charter §12.)*

## What is explicitly NOT being decided

**No date and no delivery commitment is being made.** The rows exist so
that A6 ("is the scope achievable with the resources the project actually
has — stated rather than implied?") becomes answerable, and so a reviewer
can check shape-vs-capacity honestly instead of assuming a team that does
not exist. A row answered `Unknown` keeps A6 honest too: the gate then
reports the mismatch as Unknown, never as covered.

## Options

- **(a)** Fill the table (ranges and Unknowns welcome) and approve it as
  the recorded operating-constraints statement.
- **(b)** Approve a minimal statement: "single-operator project;
  review capacity limited to LLM agents plus the owner; all other rows
  Unknown; scope-reduction trigger: owner's standing judgment."
- **(c)** Decline to state — A6 remains Not met at every administration,
  recorded as a knowing posture.

## Recommendation

`[Inferred]` **(a)**, falling back to (b) — even the minimal statement
converts A6 from "silently assumed" to "stated", which is all the gate
asks. (c) is honest but leaves the strongest known mismatch (independent
review capacity vs. CC-REV-1's seven change classes) permanently
undiscussed.

## Earliest required gate

Before the formal launch-gate administration (A6 and F5 read this file).

## Independent work

Everything proceeds; this blocks only the A6/F5 verdicts.

## Ruled 2026-08-16

Owner, via an adversarially-reviewed questionnaire packet, direct
conversational response — chose **(a)**: filled the full table above (see
"What the owner is asked to fill in") and approved it as the recorded
operating-constraints statement. No date or delivery commitment is made.
Full record: `PENDING-OWNER-DECISIONS.md` (row `P-35`, 2026-08-16 resolved
section) and the owner's local decision packet.
