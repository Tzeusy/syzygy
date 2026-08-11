# The Capability 1 route — what it routes to, and how that was checked

> **Report on a generated artifact. Not authority, and not permission.**
> The route itself lives in the generated
> `../TASK-ROUTER.md` under *"Author Capability 1 — Project registration
> and honest shape visibility"*, written by
> `../scripts/build_task_router.py`. Where this report and the router
> disagree, regenerate the router; where the router and a clause disagree,
> the clause wins.
>
> **Authoring remains forbidden.** The route exists so the rules are
> reachable *before* the owner's launch decision, not so a specification
> can be written. `openspec/` does not exist and may not be created.

## What the route names

| The charter's requirement (§11) | The clause the route names | Module |
|---|---|---|
| project identity and governance root | `RFC1-1`, `RFC1-4` | `rfcs/RFC-0001-project-graph-identity-state-planes.md` |
| project declaration | `RFC3-4` — *location is designation* | `rfcs/RFC-0003/manifests-and-namespace.md` |
| consent and repository coverage | `RFC3-7` — consent records as governance acts | same |
| Unknown reason vocabulary | `RFC2-24` — twelve reasons, closed | `rfcs/RFC-0002/rendering-vocabularies.md` |
| shared human/machine answer facts | `RFC7-33` — every distinction, machine-readable | `rfcs/RFC-0007/rendering-and-surface.md` |
| fixed human entry | `RFC7-39` | same |
| repository discoverability | `RFC7-40` | same |
| anti-rollup semantics | `RFC8-18` — independent measures, never a composite | `rfcs/RFC-0008/state-vocabulary-and-cost.md` |
| absence is Unknown, never zero | `RFC8-19` | same |
| VIS-2, VIS-4, VIS-5 | routed as doctrine | `doctrine/vision.md` |
| the in-force specification-acceptance rules | **none are in force** — see omissions | — |

Every clause ID above is **existence-checked at generation**: the generator
fails if the identifier is not defined in the module the route names. That
is not a claim in this report; it is a condition of the router being
generatable at all.

## The four things the route must do, and how each was verified

**1. Exclude deferred Mission/Context-selection contracts.** Verified two
ways. By construction: no RFC-0010 or RFC-0011 module appears in the route's
clause map or load set. And mechanically, by the generator's own computed
dependency line, which reads module front matter rather than the route's
prose:

```text
Declared contract dependencies (from module front matter, computed):
RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006, RFC-0009
```

**RFC-0010 and RFC-0011 are absent from the transitive closure**, computed
from the modules themselves. A hand-written assurance that the route avoids
the deferred waves would have been a claim; this is a measurement.
`[Observed]`

*Note the honest residue:* the closure names **RFC-0009**, a Wave B module,
and RFC-0004/0005/0006 — all inside Waves A+B, so the launch prerequisite
holds. It is wider than the five modules a reader loads, because
`depends_on` is a module-level declaration and the route is a reading list.
The route's Load line is what to read; the dependency line is what those
modules declare they rest on.

**2. Name every owner decision still blocking.** The route names ten —
`P-33, P-31, P-36, P-37, P-38, P-39, P-40, P-41, P-34, P-35` — and the
generator **verifies each has an open row** in
`../../../decisions/PENDING-OWNER-DECISIONS.md`, failing generation if one
does not. A decision named here but absent from the queue would be a
decision nobody tracks; the check refuses it. `[Observed]`

**3. Record explicit omissions.** Three, each stating what is left out and
why: the deferred Mission/Context contracts; the two **candidate** craft
policies (CC-SPEC-1…10 and CC-IMPACT-1…7), which are routed as
prerequisites and deliberately **not** listed under Craft because neither is
in force; and the facet vocabulary, which is routed to no clause at all
because it appears in **zero** of the 30 Waves A+B modules and P-37 decides
where it belongs.

**4. Be generated from current metadata, with a mutation-tested regression
fixture.** The route is generated; `--check` proves the committed file
matches regeneration. Three new mutation fixtures cover it, and each was
run and observed to fail the check when applied:

```text
Capability 1 route: an unqueued blocking decision detected
Capability 1 route: a clause routed to the wrong module detected
Capability 1 route: a deferred-wave module in the load set detected
```

Generator selftest after the addition: **9 fixtures, 0 failing.**
`[Observed]`

## What the route deliberately does not give an author

- **Permission.** Ten owner decisions are open, and the first spec cannot
  lawfully be written until the owner's launch decision, which is itself
  downstream of a formal administration that has not been run.
- **A facet vocabulary.** P-37 owns it. The route says so rather than
  quietly routing to a plausible clause.
- **Acceptance criteria for the spec itself.** CC-SPEC-1…10 are candidate.
  Until the craft act, spec acceptance has no in-force standard — which is
  launch-gate E5's exact question, and the route does not paper over it.

## The exercise this route was built for

Charter §11 requires a fresh agent, given **only** this route and the
bounded owner-ratified inputs, to produce a **specification outline only**.
That exercise is prepared at `CAPABILITY-1-SPEC-OUTLINE-EXERCISE.md` and
**has not been run** — the authoring session could not spawn a fresh-context
agent. Its result is `[Unknown]`, and the readiness report says so rather
than reporting the route as proven end to end.
