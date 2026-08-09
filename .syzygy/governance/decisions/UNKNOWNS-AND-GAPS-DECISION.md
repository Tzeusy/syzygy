# Owner decision packet — `Unknown` versus `Gap` (P-36; supersedes round-08d packet 2)

> **This file decides nothing.** It is the current form of the
> Unknown-vs-Gap vocabulary question (previously round-2026-08d
> OWNER-DECISION-PACKETS.md packet 2), sharpened by review RD-16's
> **blocking finding 1**: the candidate term registry's T-20 (`Gap`) and
> T-31 (`Unknown`) entries classified the same case in opposite ways —
> the exact confusion this ruling exists to end. Queued as **P-36**.

## Question

Adopt the two-term rule:

```text
Unknown:
    available evidence does not support deciding whether desired state is
    satisfied

Gap:
    current admissible evidence establishes that desired state is absent,
    unsatisfied, or unrealized
```

Therefore:

```text
requirement + no verifying evidence        → Unknown
requirement + evidence of non-satisfaction → Gap
```

## Current authority

VIS-2 (adopted) defines the Unknown side: no evidence yields Unknown,
never green, never zero. `Gap` is defined **nowhere in force** — only in
the candidate term registry, whose two entries review RD-16 found in
conflict (the registry's candidate bytes have since been repaired to the
doctrine-consistent reading above, with the conflict disclosed in both
entries — a drafting posture this ruling ratifies or reverts).

## Why it is launch-critical

Capability 1's acceptance criteria will use both words: a facet with no
evidence renders `Unknown`; a facet whose evidence shows non-satisfaction
renders a `Gap`. The difference decides whether the next work is
**investigation** (resolve an Unknown) or **reconciliation** (close a
Gap). A spec authored before this ruling would fix the vocabulary by
implication — the exact "unresolved shape chosen by the first spec"
failure the launch standard forbids.

## Exact deltas that follow if approved (prepared, not applied)

1. Term registry: T-20/T-31 as repaired stand ratified; the disclosed
   conflict note collapses to a pointer at this decision.
2. Contracts: no clause text change required — the corpus's uses of
   Unknown already follow VIS-2; `Gap` appears in candidate text only
   descriptively. A sweep at ratification confirms this with a
   denominator (rule 9) before the no-change claim is relied on.
3. Future OpenSpec acceptance criteria use both words per the rule.

## Options

- **(a)** The two-term rule as stated.
- **(b)** Fold both into Unknown — conflates "we don't know" with "we
  know it's not met"; the difference that routes work is lost.
- **(c)** Other vocabulary — re-review of the registry.

## Recommendation

`[Inferred]` **(a)** — it is the distinction the three-state thesis
already implies, and doctrine's own example reads this way.

## Earliest required gate

**Before OpenSpec Capability 1 is authored** (its acceptance criteria use
both words).

## Independent work

Everything except OpenSpec authoring.
