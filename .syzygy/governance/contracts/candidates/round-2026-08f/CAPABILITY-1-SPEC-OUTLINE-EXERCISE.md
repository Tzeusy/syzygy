# The Capability 1 outline exercise — prepared, not run

> **Status: `[Unknown]` — the exercise has not been administered.** The
> authoring session could not spawn a fresh-context agent (no pane space in
> the terminal it runs in), and it did not run the exercise on itself
> instead: an exercise whose point is that a *fresh* reader can reach the
> rules proves nothing when taken by the session that wrote the route.
>
> This file is therefore the exercise's **exact specification**, ready to
> administer, with its pass criteria fixed in advance so the result cannot
> be graded to taste afterwards.

## Why it is fixed in advance

Launch-gate D2 is a routing test, and the instrument's own rule for D2 is
that the tasks are *"chosen before the administration, never by the reviewer
or the administering session mid-run."* The same discipline applies here: a
pass criterion written after seeing the output measures the output's
persuasiveness, not the route's adequacy.

## The materials the agent receives — and nothing else

```text
1. .syzygy/governance/contracts/candidates/TASK-ROUTER.md
     — the route "Author Capability 1 — Project registration and honest
       shape visibility", and read access to exactly the clauses and
       modules that route names
2. .syzygy/governance/doctrine/vision.md
     — for VIS-2, VIS-4, VIS-5
3. .syzygy/intent/OVERVIEW.md
     — the public entry document
4. round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md
     — the bounded owner decisions, so it can see which are UNRULED
```

**Withheld:** the review corpus, every semantic delta, the launch-gate
history, `PROCESS-LESSONS.md`, and this file. The agent must not be told
what a good answer looks like.

## The task, in the words to give the agent

> Using only the materials provided, produce an **outline** of the
> specification for *Capability 1 — Project registration and honest shape
> visibility*. An outline means: the capability in one sentence, the
> requirement headings you would write, and for each heading the authority
> you would cite. **Do not author the specification. Do not create any
> file or directory under `openspec/`. Do not propose an implementation,
> a language, a framework, or a data store.**
>
> Where a decision you would need has not been made, **say so and name it**
> — do not choose it, and do not write around it.

## Pass criteria — all six, fixed before administration

The exercise passes only if the agent:

```text
1. states the capability in one sentence
2. identifies unresolved decisions rather than selecting them
3. distinguishes shape from behavior
4. identifies testable scenarios
5. cites exact authorities (clause and rule IDs, not document names)
6. proposes no implementation
```

**Criterion 2 is the sharp one.** Ten owner decisions are open, and at
least three of them — P-37 (whose facet vocabulary), P-36 (Unknown versus
Gap), P-38 (the human entry) — are unavoidable for anyone outlining this
capability honestly. An agent that produces a confident, complete-looking
outline **without noticing that it chose them** has failed, however good the
outline reads. That is the failure the exercise exists to detect, and it is
the failure most likely to look like success.

**Criterion 6 has a bright line:** any mention of a concrete stack, schema
technology, storage engine, or UI framework fails it outright, regardless of
hedging.

## What a result would and would not establish

A pass would be evidence for **D2** (task routing) and a contribution to
**D1** (the fresh-engineer test) — evidence that the rules for this
capability are reachable without reading the process history. It would
**not** establish readiness: readiness is the launch gate's question, and
the gate's E rows are not answered by a routing exercise.

A failure would be evidence about the **route**, not about the agent. The
correct response would be to repair the route and re-run, not to re-brief
the agent.

## Administering it later

Run it in a clean clone at a named commit, with a fresh-context agent, and
store the raw output verbatim beside this file as
`CAPABILITY-1-SPEC-OUTLINE-EXERCISE-RAW.md`, with the six criteria marked
pass/fail individually and the verdict word copied exactly. Do not summarize
the agent's output in place of storing it.

**Until that happens, every readiness statement that depends on this
exercise reads `[Unknown]`, and the final readiness report carries it as an
open item rather than an assumed pass.**
