# `docs/` — the implementation plane's working documents

> **Not authority.** Nothing here adopts, accepts, or approves anything, and
> nothing here may be cited as a rule. Authority lives in `.syzygy/**`
> (doctrine, decisions, policies, contracts) and `openspec/**`
> (specifications); current state lives in `PROJECT-STATUS.md`. Where a page
> here disagrees with one of those, **the owning record wins and this page is
> stale** — report the disagreement rather than resolving it here.

`.syzygy/**` says what must be true and `openspec/**` says what the software
must do. This directory holds the third thing: the **implementation plane's**
own working record — how the work was planned, what was reviewed, and what
evidence a run actually produced. It is written by and for the people and
agents doing the building.

## What is here

| Path | What it is | Reader, and the question it answers |
|---|---|---|
| `CAPABILITY-1-IMPLEMENTATION-PLAN.md` | The Capability 1 build plan | An implementer: "what is the next lawful implementation step, and under which act?" |
| `PWB-IMPLEMENTATION-PLAN.md` | The Polaris project-wide Butlers-model build plan | Same, for the PWB pipeline |
| `THREE-SURFACE-POC.md` | How to run the bounded POC | Anyone: "how do I start this thing and see it?" |
| `reviews/` | The review corpus — raw reviewer output and its dispositions | A reviewer or repairer: "what did an independent reader find, and what happened to each finding?" |
| `evidence/` | Machine-produced run records (mutation sweeps, browser and fresh-checkout runs), as JSON | Anyone checking a claim: "what did that run actually output?" |
| `plans/` | Dated design notes for a single bead, written before the work | An implementer picking up that bead: "what shape was already decided, and by whom?" |
| `superpowers/plans/`, `superpowers/specs/` | Spent plans and designs from an external-harness convention, kept as evidence | Someone auditing a past change: "what was the plan the work was actually done against?" |

Implementation *plans* live here. The **authorizing act** for any of that work
does not — it lives in `.syzygy/governance/decisions/`. A plan in this
directory is never permission; find the act first (`AGENTS.md`, "Where
authority lives").

## `reviews/` — the corpus, by campaign

Raw reviewer output is stored **verbatim and never edited** (CC-REV-6). Files
ending `-RAW.md` are that verbatim output; `-DISPOSITION.md` and `*-PACKET.md`
files are the synthesis over them. Correcting a RAW file is never the repair —
the repair is a new disposition that cites it.

| Campaign prefix | Files | Recorded | What was under review |
|---|---|---|---|
| `R-S2` … `R-S7` | 4 | 2026-08-21 → 08-22 | Capability 1 domain slices S2, S5, S6, S7 |
| `R-RT-*` | 2 | 2026-08-23 | The Capability 1 runtime vertical slice |
| `R-POC-*` | 8 | 2026-08-30 → 08-31 | The Three-Surface POC cycle, product and owner passes |
| `POLARIS-*`, `R-POLARIS-*` | 15 | 2026-08-31 | Polaris project-wide model, POC, observation, precondition, and its sign-off packet |
| `R-GENERAL-TRUSTED-*` | 24 | 2026-08-31 → 09-01 | The general trusted-bootstrap authorization transaction |
| `R-PWB-STATE1-*`, `R-PWB-EFFECT-*` | 17 | 2026-09-02 | The PWB state-(1) amendment and effect acts |
| `R-PWB-TRUTH-*`, `R-PWB-LIVE-*`, `*-pwb-live-*` | 16 | 2026-09-05 | PWB truth-policy amendment; the live exact-head packet and its finding-traceability index |

The seven rows partition the directory: 86 files on disk, 86 assigned, no
remainder [Observed — swept 2026-09-05; the grouping is by filename prefix
and the dates are `git log --diff-filter=A`]. These are
navigation figures, not measurement, and they go stale the moment a review
lands — re-derive rather than trusting the row.

## `plans/` and `superpowers/` — two homes, one role

Both hold plan-and-design notes; they are split by which harness wrote them,
not by what they are. Prefer `plans/` for anything new.

`superpowers/` is **path-pinned and must not be moved or renamed.** The
general trusted-bootstrap authorization's impact ledger classifies every path
under that prefix as spent historical evidence, and
`scripts/build_general_trusted_bootstrap_impact_ledger.py` hard-codes the
prefix string to do it. Relocating a file out of that directory would silently
re-classify it on the next regeneration.

**One of the four is not spent.** The ledger's classification is about where a
file sits, not about whether the work it plans is finished, and those two
answers have come apart. Read the table before treating any of these as
history — and read the `bd` issue, never the "REQUIRED SUB-SKILL" line at a
file's head, which addressed the worker of the day.

| File | Issue | State |
|---|---|---|
| `superpowers/plans/2026-08-24-cap1-runtime-hardening-followups.md` | epic `syzygy-u2a` | **Live.** The epic names it as its *approved implementation guidance* at commit `d11c07e`, and shapes its six implementation children on that file's Tasks 1–6. The epic is open (P1) and its human gate `syzygy-u2a.1` is blocked |
| `superpowers/specs/2026-08-23-cap1-runtime-hardening-followups-design.md` | `syzygy-ydr`, `syzygy-e84`, `syzygy-h84` | Spent. The design the plan above was written from |
| `superpowers/plans/2026-08-27-syzygy-vky-validator-hardening.md` | `syzygy-vky` (closed) | Spent |
| `plans/2026-08-26-syzygy-vky-validator-hardening-design.md` | `syzygy-vky` (closed) | Spent. The design for the same work as the row above — two files, one bead, split only by which harness wrote them. Neither is cited by anything |

[Observed — swept 2026-09-06: four files across the three directories; each
searched for `syzygy-*` identifiers in its own text, and each filename searched
across every tracked `.md` and `.py`. Two are cited, both by the general
trusted-bootstrap impact ledger; two are cited by nothing.]

## `evidence/` — run records

Each file is one run's machine output at a named commit, kept because a claim
elsewhere cites it. A mutation-run record is valid **only for the commit it
names** (`AGENTS.md` verification rule 7). Reading the file's own contents is
the check; the filename is not the evidence.

## The maintenance contract

This directory is governed by the adopted craft policy
`.syzygy/governance/policies/craft-and-care/review-and-documentation.md`. The
clauses that bind what you write here — cited, not restated:

- **CC-REV-2** — a change that moves a responsibility updates its
  documentation *in the same change*; it does not merge with the
  contradiction open.
- **CC-REV-3** — documentation **cites** authoritative artifacts, it never
  restates them normatively. A restated rule drifts and becomes a shadow
  authority. If you find the same question answered in two homes, surface the
  contradiction; do not silently pick a winner.
- **CC-REV-5** — substantive claims carry `[Observed]` (with a resolvable
  source), `[Inferred]`, or `[Unknown]`. Missing evidence renders Unknown,
  never Inferred.
- **CC-REV-6** — raw reviewer output is stored unchanged before synthesis, and
  every revise-severity finding is fixed or explicitly overruled with recorded
  rationale. Nothing is dropped.
- **CC-REV-7** — identifiers are stable: amend in place, retire rather than
  renumber.

In practice, for this directory: a page that no longer has a nameable reader
and a question it answers should be merged or removed, not left to rot; a page
that has gone stale is marked stale **with evidence at the stale sentence**,
never left silently standing behind a general "this page may be stale" banner.

## What does not belong here

- Implementation code (it belongs in `apps/**`, `packages/**`, `scripts/`).
- Anything normative — rules, acceptance, adoption, approval. Those are owner
  acts under `.syzygy/governance/` (VIS-4).
- A second copy of state `PROJECT-STATUS.md` already owns.
- Per-tool scratch conventions from an external harness. If a tool wants a
  directory of its own, it gets one outside `docs/`.
