# Owner decision packet — OpenSpec form and version (P-39; supersedes round-08d packet 11)

> **This file decides nothing.** Current form of the OpenSpec
> medium/version question (previously round-2026-08d packet 11). Queued
> as **P-39**. The launch-gate pilot failed E1's *form* sub-verdict on
> exactly this: "the first changeset author chooses implicitly — an owner
> decision made by default." The first spec author must never pick the
> medium while writing the message.

## Question

Which OpenSpec distribution/version and artifact form does Capability 1
use?

## The exact options on the table (from the substrate lock, verified)

`GOVERNANCE-SUBSTRATE-LOCK.yaml` `openspec`: distribution
`npm: @fission-ai/openspec`, **installed CLI 1.3.1**, latest published at
lock time **1.7.0**, compatibility `[Unknown]` (nothing depends on
OpenSpec behavior yet — correct), nothing pinned ("Pin at the first
`openspec/` write").

- **(a) Pin the installed 1.3.1** and author against it; upgrade later as
  a recorded migration.
- **(b) Pin current upstream (1.7.0 at lock time; re-check at decision
  time)** — start current, no immediate migration debt; the 1.3.1→1.7.0
  format delta is `[Unknown]` until checked, so this option carries a
  pre-decision verification step: diff the changeset format between the
  two versions before pinning.
- **(c) Defer** — the E1 fail persists; the first author decides by
  default. Not compatible with the launch standard.

## What the decision records (all five, whichever option)

| Field | Content |
|---|---|
| **Version/distribution** | the chosen version, pinned in the substrate lock at decision time (digest/lock reference filled in) |
| **Artifact form** | OpenSpec changeset directories under `openspec/` per the pinned version's format; the th-projects `spec-format.md` contract (pinned at `f4cf1c7`) is the consumer shape the changesets must satisfy — referenced as workflow, never authority |
| **Stable identity expectations** | requirement IDs are stable forever once minted (the corpus's amend-in-place discipline extends to specs); RFC 0003/0004 own spec home and identity; whether OpenSpec identities survive edit/rename is recorded `[Unknown]` and is RFC 0004's adapter-contract obligation — the decision acknowledges, not resolves, it |
| **Adapter compatibility posture** | the OpenSpec CLI is a substitutable adapter beneath a non-substitutable artifact contract (doctrine's carve-out); a CLI version change is an adapter event, an artifact-format change is a contract event |
| **Migration posture** | version upgrades are recorded migrations with the artifact contract as the invariant; no silent regeneration of accepted specs |

## Recommendation

`[Inferred]` **(a)** with the upgrade path noted, **unless** the
pre-decision diff in (b) shows the 1.3.1 format is already superseded in
a way that would force an early migration — in which case (b). The
deciding fact (the format delta) should be checked at decision time,
not guessed now — and it is the one check in the launch-critical set
that needs material from **outside the clone** (two npm package
versions), so treat it as a **pre-sitting task** with cost `[Unknown]`
(network, registry availability), never a minutes-in-the-sitting step
*(qualified 2026-08-10, RD30-15)*.

## Earliest required gate

**Before the first OpenSpec changeset** — and Capability 1 is that
changeset, so before spec authoring begins.

## Independent work

Everything up to OpenSpec authoring.
