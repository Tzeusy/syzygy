# Round 2026-08f — launch gate v2.0 and the first Capability 1 packet, 2026-08-11 → 08-17

> **A closed round's process records. Never authority.** Nothing in this
> directory binds anything, adopts anything or accepts anything, and no file
> in it may be cited as a rule. It records how one pass of work was scoped,
> reviewed and disposed, so the round's judgments can be audited instead of
> trusted. What is in force is `PROJECT-STATUS.md` and
> `../../../decisions/ACCEPTANCE-ACT-RECORD.md`; what a clause says is found by
> identifier in the repository-root `DIRECTIVE-REGISTER.md`.
>
> **Where this page and an owning record disagree, the owning record wins and
> this page is stale.** The round in context, beside the other ten:
> [`../ROUND-ESTATE.md`](../ROUND-ESTATE.md).

## What this round settled
The launch gate's v2.0 rewrite, the first Capability 1 owner decision packet,
and a dry-run administration fixture that let the gate be exercised before any
real administration existed.

## Where that settlement lives now
The v2.0 content is in the repository-root `launch-gate-pre-specifications.md`. The decision
packet was overtaken on 2026-08-13 by the next round's decision index, and the
P-33 analysis here by the next round's re-derivation — **read
`round-2026-08g/`, not these two files**, for either question.

## What a later reader will trip over
**`fixtures/DRY-RUN-ADMINISTRATION.json` is a live CI input and must not be
moved, renamed or deleted.** `.github/workflows/governance-docs.yml` invokes
`validate_launch_administration.py` against it at line 127 and
`render_launch_administration.py --check` against it at line 130, both by full
path [Observed — read from the workflow, 2026-09-06]. Nothing about sitting in
a closed round's directory makes a file inert.

## The shape of this directory
20 tracked files. 8 of them sit under `reviews/`, stored **verbatim and never
edited** (CC-REV-6) — correcting a raw review is never the repair. 9 of the 20
are named by no other tracked file [Observed — 2026-09-06, every basename
searched as a literal across all tracked non-round files; method and the
per-round figures are in `../ROUND-ESTATE.md`]. That is a citation count, not
a judgment about whether a file has served its purpose.

This directory's first-commit date is not a fence around its contents: a round
directory can take a file long after the round closed, and one of them did
(`round-2026-08g`, seventeen days later). Read a file's own head, not the
directory's date.

**Nothing here may be deleted or relocated by an agent.** These files sit in
the governed plane; disposing of them is an owner decision, queued in
`../../../decisions/DOCUMENTATION-ESTATE-DECISION-PACKET.md`.
