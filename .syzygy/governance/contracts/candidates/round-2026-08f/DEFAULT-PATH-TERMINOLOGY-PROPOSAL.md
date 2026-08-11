# Default-path terminology — measured, and mostly *not* changed

> **Proposal and measurement. Nothing here amends adopted doctrine**, and
> the one doctrine change it drafts is deliberately **not applied** (VIS-4).
> Written under owner charter §6.5: *"Prepare the smallest lawful changes to
> ensure ordinary language leads."* The operative word is **smallest**.

## What the charter asked for

```text
actuator   → agent and work-execution tools
kernel     → shared project model
surface    → view, where the technical distinction is unnecessary
workspace  → portfolio workspace, defined inline
```

## What is actually on the default path — measured

Case-insensitive whole-word counts, run this session over the
`DEFAULT_ROUTE_SET`:

| File | `actuator` | `kernel` | `surface` | `workspace` |
|---|---|---|---|---|
| `README.md` | 0 | 1 | 6 | 2 |
| `AGENTS.md` | 0 | 0 | 2 | 0 |
| `.syzygy/intent/OVERVIEW.md` | 0 | 2 | 13 | 2 |
| `PROJECT-STATUS.md` | 0 | 0 | 3 | 0 |
| `.syzygy/governance/doctrine/README.md` | 1 | 1 | 2 | 0 |
| `contracts/candidates/TASK-ROUTER.md` (generated) | 0 | 2 | 8 | 0 |

And in **adopted doctrine**, which no pass may edit:

| File | `actuator` | `kernel` | `surface` |
|---|---|---|---|
| `doctrine/architecture.md` | 0 | 6 | 13 |
| `doctrine/vision.md` | 3 | 0 | 6 |
| `doctrine/v1.md` | 1 | 0 | 9 |
| `doctrine/trust-and-evidence.md` | 0 | 0 | 3 |
| `doctrine/security.md` | 0 | 0 | 2 |
| `doctrine/README.md` | 1 | 1 | 2 |

`[Observed]`

## What was changed, and it is three sentences

1. **`kernel`** — `README.md` already led with *"projections over one shared
   project model (the kernel, in the technical contracts)"*; it now reads
   **"views over one shared project model (called the *kernel* in the
   technical contracts)"**. The ordinary phrase leads; the coined term is
   parenthetical, defined at first use. `OVERVIEW.md` already did this.
2. **`workspace`** — `README.md`'s "workspace-level operator domain" now
   reads **"the level of a portfolio workspace — the set of projects one
   operator runs, above any single project"**, defined inline where it first
   appears. `OVERVIEW.md` already defined it inline.
3. **`actuator`** — appears **zero** times on the default reading path
   outside doctrine. Nothing to change.

## What was deliberately *not* changed, and why

**`surface` → `view` was not swept.** It is the largest count and the
smallest gain, and the sweep would make the corpus worse in a specific,
checkable way:

- Adopted doctrine uses `surface` **35 times across five files**. It cannot
  be edited without an owner act.
- If the presentation layer says *view* while doctrine says *surface*, the
  overview asserts a vocabulary its source does not use — which is exactly
  what launch-gate **D4** tests ("do the entry/summary documents make no
  claim their sources don't") and **C1** tests (a lower artifact restating a
  higher rule with drifted meaning).
- A rename that improves **D3** (invented vocabulary minimal and
  defined-before-use) by breaking **D4** and **C1** is not an improvement;
  it moves a finding rather than closing one.

The lawful order is the reverse: doctrine changes first, presentation
follows. The draft below exists so that order is available to the owner —
not so this pass can shortcut it.

**`TASK-ROUTER.md` was not edited.** It is generated
(`contracts/candidates/scripts/build_task_router.py`). Editing a generated
file is drift that the next regeneration erases; if its vocabulary changes,
the generator changes.

## Drafted, NOT applied — a narrow editorial doctrine amendment

> **This is a draft. It has not been applied, offered, or queued as an act.
> Adopted doctrine is unchanged.** If the owner wants ordinary language to
> lead in doctrine too, this is the smallest shape that would do it.

```text
Amendment (editorial, D-editorial-1): vocabulary leads with ordinary language

For each of the three coined terms below, doctrine's FIRST use in each file
gains a parenthetical gloss, and no other occurrence changes:

    surface   → "surface (a view over the shared project model)"
    kernel    → "kernel (the shared project model)"
    actuator  → "actuator (an agent, or a work-execution tool)"

Nothing else moves. No rule's meaning changes, no clause is renumbered, no
term is retired, and no occurrence beyond each file's first is touched.
```

**Why an editorial amendment is still an amendment.** This repository's own
rule is that "editorial" and "no semantic change" are *reviewable claims*,
not exemptions (`NORMATIVE-CHANGE-WORKFLOW`). A gloss that got a term wrong
would change meaning while claiming not to. So even this draft would travel
as a semantic delta with a fresh-context review, and it is deliberately
scoped to first-use glosses — the smallest change whose "no semantic
change" claim is easy to check.

**Its cost, stated:** an amendment to adopted doctrine invalidates nothing
in the contract corpus (contracts cite doctrine by rule ID, not by wording),
so no wave confirmation is retired by it. Its cost is one owner act and one
review, and its benefit is that the presentation layer could then say *view*
without asserting something its source does not.

## Recommendation

`[Inferred]` — take the three applied changes as the terminology work of
this pass, and leave `surface` alone until and unless the owner wants the
doctrine amendment. The term registry (`policy-candidates/TERM-REGISTRY.md`,
candidate, P-16) remains where a full vocabulary ruling belongs; this file
is not a competing registry and mints no term.
