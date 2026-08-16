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

## The pre-decision measurement, run 2026-08-13

*Owner charter §12 directs steps 1–3 (inspect installed, inspect current
upstream, compare format and migration differences) to be run **at decision
time from current official sources**, not read out of an older packet. This
section is that run. It is **evidence only**: it makes no choice, pins
nothing, and edits no lock — steps 4 and 5 are the owner's (VIS-4).*

**Step 1 — installed.** `openspec --version` → **`1.3.1`**; `npm ls -g` →
`@fission-ai/openspec@1.3.1` at
`/home/tze/.nvm/versions/node/v24.6.0/bin/openspec`. Matches the lock.

**Step 2 — current upstream.** `npm view @fission-ai/openspec` →
`dist-tags.latest = ` **`1.8.0`**, published `2026-08-05`. Intermediate
publishes: `1.6.0` (2026-07-10), `1.7.0` (2026-07-29). Installed `1.3.1`
dates from `2026-04-21`.

> **The lock's figure is stale by one release** — it records `1.7.0` as
> latest; upstream is `1.8.0`. Exactly the failure charter §12 warns about.
> Recorded here, **not corrected in the lock**: the lock is a record whose
> substrate rows are re-measured at pin time, and pinning is the owner's act.

**Step 3 — the format delta**, measured by unpacking both published tarballs
and diffing what actually governs a changeset — the `spec-driven` schema tree
inside each package, not the release notes.

| Artefact | sha256 |
|---|---|
| `fission-ai-openspec-1.3.1.tgz` | `381fd3513983bd9f6b2be05218a70d38bbc33598c9816f2dd5ac8e8f13a20eb0` |
| `fission-ai-openspec-1.8.0.tgz` | `e6f049442659eba493a130220faecfc4cb7b001b300af069ae5d535e744348c4` |
| `1.3.1` `spec-driven` schema | `9b82d32d3fdb270090aad4a1b28a25b56a973cd76b195370cbe7b53b218d958c` |
| `1.8.0` `spec-driven` schema | `7004a6a4d82fbab6d2e5e0e5f178db4e612fa57d7e012ce275fcce9f76a61af6` |

**The load-bearing structure is unchanged.** [Observed] The delta-operation
vocabulary (`ADDED` / `MODIFIED` / `REMOVED` / `RENAMED Requirements`) and the
format block — `### Requirement:`, SHALL/MUST, `#### Scenario:` with WHEN/THEN,
the *"Scenarios MUST use exactly 4 hashtags"* rule, and *"every requirement
MUST have at least one scenario"* — are **byte-identical** across the two
versions. The schema file set has the same five members; **no file was
removed**.

Four additive changes, each with a consequence for Capability 1:

| Change in 1.8.0 | Consequence |
|---|---|
| **`## Purpose` section** in the spec template — new capabilities only, 50+ characters or `validate --strict` calls it too brief; forbidden on a delta for an existing capability | Capability 1 is a new capability, so it would carry one. Omitting it leaves the archived main spec holding a literal `TBD … Update Purpose after archive` placeholder |
| **Zero-delta changes rejected.** `openspec validate` refuses a change with no deltas unless the change's **`.openspec.yaml`** sets `skip_specs: true` | A new per-change config file exists in 1.8.0 and does not in 1.3.1. This is the only *structural* addition to a changeset directory |
| **Capability path widened** from `specs/<capability>/` to `specs/<capability-path>/`, permitting nesting (`identity/user-auth`), with *"do not move or rename the capability"* stated | Bears directly on RFC 0003/0004's spec-home and identity questions. It widens what a home may be; it does not settle whether an identity survives a rename |
| Substantially expanded guidance on **what belongs in a spec** — observable behaviour, inputs/outputs/errors, external constraints; *"if the implementation can change without changing externally visible behaviour, it likely does not belong in the spec"* | Independent of Syzygy's own CC-SPEC candidate and consistent with it. Convergence, not authority |

**What this does not settle.** The packet's `[Unknown]` on whether OpenSpec
identities survive edit or rename is **still Unknown**: 1.8.0 adds *"do not
move or rename the capability"* as an instruction to an author, which is a
prohibition, not a statement of what the tool does if one happens. That
remains RFC 0004's adapter-contract obligation.

**What it means for the recommendation below.** The condition the old
recommendation attached to option (b) — *"unless the pre-decision diff shows
the 1.3.1 format is already superseded in a way that would force an early
migration"* — has now been checked and the answer is **no**: the delta is
additive, and nothing authored against 1.3.1's structure becomes invalid under
1.8.0. What 1.3.1 *lacks* is the `## Purpose` convention and the
`skip_specs` marker, so a spec authored under 1.3.1 and later validated under
1.8.0 would take a `--strict` Purpose finding. That is a small, known,
one-file migration — not a format break. The owner still chooses.

## Options

*(These sat unheaded under the substrate-lock section until the measurement
above was inserted between them; the heading is new, the options are not.)*

- **(a) Pin the installed 1.3.1** and author against it; upgrade later as
  a recorded migration.
- **(b) Pin current upstream — `1.8.0` as measured 2026-08-13**, not the
  `1.7.0` the lock records — start current, no immediate migration debt. The
  pre-decision verification step this option carried has been **run** (see the
  measurement above): the `1.3.1`→`1.8.0` delta is additive, and the option's
  `[Unknown]` on the format is now `[Observed]`. Re-measure at the sitting if
  more time has passed; upstream published three releases in four months.
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

`[Inferred]` **(b)**, changed from (a) on 2026-08-13 by the measurement
above, and the reasoning is what the owner should disagree with if they
disagree at all.

The old recommendation was (a) *unless* the format delta turned out to force
an early migration. That was the right shape while the delta was `[Unknown]`:
pin what is installed, defer the unknown. The delta has now been measured and
it is **additive** — which removes the argument for (a) rather than
strengthening it. Authoring against `1.3.1` now means authoring against a
version four months and three releases behind, then taking the `## Purpose`
migration anyway at the first upgrade. (b) pays the same small cost once,
sooner, with the current tool.

(a) remains entirely lawful and is the better choice if the owner wants the
authoring environment frozen at bytes already on the machine — `1.8.0` would
have to be installed, and *"it works on this laptop today"* is a real
argument. (c) remains not compatible with the launch standard.

**The pre-sitting cost is now paid.** This check was the one launch-critical
item needing material from outside the clone, with cost `[Unknown]` for
network and registry availability *(qualified 2026-08-10, RD30-15)*. It ran in
one pass. What remains for the sitting is the choice itself and the lock
edit — both owner acts.

## Earliest required gate

**Before the first OpenSpec changeset** — and Capability 1 is that
changeset, so before spec authoring begins.

## Independent work

Everything up to OpenSpec authoring.

## Ruled 2026-08-16

Owner, via an adversarially-reviewed questionnaire packet, direct
conversational response — chose **(b)**, pinned at **1.9.0** (refreshed
from this packet's measured 1.8.0: upstream published again and the owner
had already upgraded before answering; the additive-delta claim was
independently re-verified against 1.9.0 this session — see
`GOVERNANCE-SUBSTRATE-LOCK.yaml`'s `openspec.compatibility` field for the
one correction that surfaced during that re-verification). Recorded in
`GOVERNANCE-SUBSTRATE-LOCK.yaml`'s `openspec` block. Full record:
`PENDING-OWNER-DECISIONS.md` (row `P-39`, 2026-08-16 resolved section) and
the owner's local decision packet.
