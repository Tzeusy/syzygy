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
| Number of human operators | *[unstated — believed 1 (the owner); confirm]* |
| Engineering attention available (hours/week, honest range) | *[unstated]* |
| Independent-review capacity (who besides Claude-family agents can review — other model families? humans? none?) | *[unstated — the assurance-independence question F5 turns on this]* |
| Model/provider budget (monthly ceiling, or Unknown) | *[unstated]* |
| Maximum concurrent workstreams the owner will supervise | *[unstated]* |
| Target proving project(s) for V0 (doctrine says "the owner's other live projects"; name them or defer) | *[unstated]* |
| Time horizon (what cadence of progress makes this worth continuing; explicitly NOT a deadline) | *[unstated]* |
| Scope-reduction triggers (what circumstance cuts V0 scope — e.g. "if X months pass without spec authoring, the 3D map moves to V1") | *[unstated]* |

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
