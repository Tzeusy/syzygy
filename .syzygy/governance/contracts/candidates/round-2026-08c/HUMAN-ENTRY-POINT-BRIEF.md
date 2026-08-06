# The human entry point for a governed project — candidate design brief

> **Candidate design material. Binds nothing.** It proposes one fixed path,
> says what must be behind it, and states what Syzygy may and may not do about
> a repository whose front door does not point at it. User-observable
> behaviour routes to OpenSpec, which does not exist.

## The problem, in one sentence

A project can be registered with Syzygy, fully declared, perfectly traceable —
and a competent engineer who opens its repository can have **no idea any of
that exists.**

Registration is a relationship between an owner and Syzygy. It is not a sign
on the door.

## 1. One path, chosen

> **`.syzygy/intent/OVERVIEW.md` is the fixed, Syzygy-owned human entry point
> for every governed project.**

Not both this and a `README.md` beside it. Two default entry points is the
same defect as none: a reader who finds one cannot know whether the other
disagrees, and an author with two homes uses whichever is nearer.

**Why `OVERVIEW.md` and not `README.md`:**

- It **already exists and is already governed.** Syzygy's own overview lives
  there, it is a governed presentation artifact, and it is act 4's digest
  subject. The path has an owner and a ceremony; a new `README.md` would need
  both invented.
- `intent/` is a **schema-versioned governed namespace** under RFC3-18, which
  means the path is already inside a plane Syzygy may write to and whose
  contents are typed.
- **A `README.md` at that path would be read as a directory index**, because
  that is what a `README.md` in a directory is everywhere else. The entry
  point is not an index of `intent/`; it is the project's narrative front
  door, and it should not be named after a convention that says otherwise.

**What happens to a `README.md` under `.syzygy/intent/`:** nothing. It is not
created. If one ever exists it is a directory index for `intent/` and
explicitly **not** the entry point — the brief says so here so that the question is settled
before someone answers it by adding a file.

## 2. What the entry point must tell an unfamiliar engineer

Eight things. The list is short because a longer one is not read.

| # | The question | What answers it |
|---|---|---|
| 1 | **What is this project?** | The primary narrative (RFC7-6) — one, per project |
| 2 | **What does it promise, and what does it refuse?** | The project's own doctrine, or a plain statement that it declares none |
| 3 | **What shape is it in?** | The seven project-shape facets, rendered as seven independent answers with their Unknown reasons — never a badge |
| 4 | **Where do exact requirements live?** | The `openspec/**` plane, routed by capability |
| 5 | **Where does work live?** | The work plane, and the scheduler of record |
| 6 | **Where is the system map?** | The topology / map plane |
| 7 | **How do I ask the same questions programmatically?** | The semantic API endpoint that returns these exact facts, per RFC6-13's one-truth-two-consumers rule |
| 8 | **What is Unknown?** | Every facet's Unknown reasons, and the project's declared open questions |

**Row 7 is the one that is usually skipped and should not be.** An entry point
that a human can read and an agent cannot query is a second truth store with
extra steps. RFC6-13 and RFC6-14 already bind machine/human parity for query
answers; the entry point inherits that obligation rather than restating it.

**Row 3 is where the facets land.** The entry point is the only place a reader
meets all seven at once, and it is therefore the place where a composite badge
would be most tempting and most damaging. See
`PROJECT-SHAPE-FACETS-BRIEF.md`.

## 3. It is presentation, never authority

The entry point carries the same banner Syzygy's own overview carries:

> **Governed presentation, never authority.** This page explains; it decides
> nothing. Any clause it summarizes overrides it.

Concretely: nothing may cite the entry point. Not a claim, not a gap, not an
evaluation, not a mapping. RFC7-3's *"nothing cites the rendering"* already
binds this for narrative artifacts, and the entry point is one.

## 4. Root-repository discoverability — a finding, never a write

**Syzygy directly writes project content only under `openspec/**` and
`.syzygy/**`.** A project's root `README.md` is outside both. Syzygy may not
edit it, and this brief does not propose an exception. The two-root boundary
is not a rule with a discoverability carve-out; a carve-out is how a write
boundary stops being one.

So the gap is **rendered, not closed** — and it is rendered **once per declared
repository entry**, not once per project:

```text
for each repository entry declared under RFC3-6:
    front door links to the Syzygy project entry:
        yes / no / Unknown
```

**Per-repository is a correction, and the singular version was a real hole.**
RFC3-29 upholds *"One plane per repository; one root per Project … A repository
carries at most one `.syzygy/` plane, at its root."* RFC3-30 makes an observing
project's read of another repository **read-only**: *"A's direct-write universe
is A's own governance root's two namespaces and nothing else (VIS-5); A never
writes, migrates, or 'repairs' B's plane."*

So for a project with N repositories, **exactly one can hold an entry point,
and Syzygy may not create one in the other N−1.** A singular finding answers
for that one repository and says nothing about the rest — which means the
problem this brief opens with was *unsolved for every repository but one, and
the design could not even render that it was unsolved.* Review RD-2 found it.
The fix costs nothing: RFC3-6 already owns repository entries, this brief
already routed the finding there, and making the answer per-entry converts a
silent hole into a rendered one, which is the whole thesis.

- **`yes`** — the root `README.md` (or the forge's configured front page)
  contains a resolvable link to `.syzygy/intent/OVERVIEW.md`.
- **`no`** — it was read, and contains no such link.
- **`Unknown`** — it could not be read at this evaluation. Not `no`. A root
  README Syzygy cannot see is not a root README without a link, and the
  distinction is exactly the missing-declaration-versus-failed-evidence rule
  the facet model turns on.

**When the answer is `no`, three things happen and a fourth does not:**

1. The gap **renders** — on the entry point itself, and in the Registered
   facet's detail.
2. Syzygy **proposes** the one-line link, as work or as a code-shaped proposal
   the owner can apply. A proposal is not a write.
3. The proposal states exactly what it would add and where, so that applying
   it is a five-second decision.
4. **Syzygy never writes it**, and never treats registration as evidence that
   a human could find the project. *Registered* and *discoverable* are
   different facts, and conflating them would make the whole facet model a
   badge again at its very first row.

**This finding is not a facet.** It is a *detail* of one, because promoting it
would make eight facets where seven is already at the edge of what a reader
holds at once. It is queryable in its own right.

**Which facet owns it is open, and review RD-2 argues the current answer is
wrong.** This brief placed it under **Registered**. RD-2's counter:

> That is a presentation argument applied to a placement decision.
> Discoverability is *about* whether a human can find the project —
> Human-understandable's exact subject, and RFC7-30's first clause is
> *"entering at the primary narrative"*, which presupposes the reader got
> there. Under Registered, a project renders `Registered: true` with
> `discoverable: no` buried in a drawer, while the facet a newcomer would
> actually consult about human comprehension is silent on whether a human can
> reach the door at all.

That is the stronger argument, and it is **recommended but not applied** —
which facet owns a finding is a design decision inside owner **packet 6**, and
applying it here would settle a question the packet exists to ask. Recorded
either way: the finding is per-repository, queryable, and never a write.

## 5. Registration is not certification

Stated once, plainly, meant to be quoted, and required to be human-visible on
the entry point **and** machine-queryable through the same API:

> **Registering a project grants a declared observation and governance
> relationship. It does not certify that the project is shaped,
> understandable, observable, traceable, Mission-ready, or reconciled.**

The sentence names the six other facets on purpose. A reader who has just seen
`Registered: true` is exactly the reader most likely to conclude something
stronger, and the correction belongs next to the claim rather than in a
footnote.

**"Machine-queryable" is not "attached", and an earlier revision of this
section confused them.** Review RD-2:

> An agent that queries the Registered facet gets `true` and nothing else.

RFC6-14 binds *labels* to travel with every machine answer; a prose disclaimer
is not a label, and no clause makes it accompany a `Registered: true` response.
A sentence a consumer must go and fetch separately is a sentence most consumers
will not fetch.

**So the requirement is stated as a field, not a paragraph:** the Registered
facet's answer carries a **required non-certification field** — the sentence
above, or a stable identifier resolving to it — in the same envelope as the
value, wherever that value is served. If the sentence is load-bearing it needs
a home that travels; if it is not load-bearing it should not be in this brief
at all.

**[Unknown]** which clause makes that field required. RFC6-14's parity rule
governs labels, not per-facet envelope fields, so this is a **specification
obligation on OpenSpec Capability 1** rather than a contract gap — recorded as
such, and not smuggled into RFC-0006 here.

## 6. What this costs, honestly

- **A fixed path is a commitment.** Every governed project acquires
  `.syzygy/intent/OVERVIEW.md` as a reserved name. Projects that already use
  `.syzygy/` for something else — there are none today, and there will be —
  inherit a collision.
- **The entry point can be stale**, and nothing here prevents that. Its facets
  are evaluation-stamped and degrade; its narrative is authored and does not.
  RFC7-11's broken-anchor rule catches anchors that stop resolving; it does
  not catch prose that has quietly stopped being true. **[Unknown]** how that
  is detected — it is the same problem as the Human-understandable facet's
  judged half, and it is not solved here.
- **A `no` on discoverability may sit forever.** Syzygy renders it and
  proposes the fix; nothing makes anyone apply it. That is the correct
  consequence of the write boundary and it should not be softened into a
  nudge that eventually becomes a write.
- **N−1 of a project's N repositories can never have an entry point, and this
  is the largest cost on the list.** RFC3-29 allows one `.syzygy/` plane per
  repository at its root, and RFC3-30 makes every other repository read-only
  to the observing project. The per-repository discoverability finding (§4)
  renders the hole; it does not close it, and nothing in this design can. An
  engineer opening observed-source repository #4 of 5 has no path in — the
  best available outcome is that the *project's* entry point can now say so,
  repository by repository, instead of answering for one and staying silent
  about four. **[Observed]**, and it went unlisted until review RD-2 named it.

## 7. Routing

| Piece | Home |
|---|---|
| The primary-narrative obligation | **RFC7-6** (candidate) — exists |
| Presentation is never authority | **RFC7-3**, **RFC7-4** (candidate) — exists |
| `intent/` as a governed, schema-versioned namespace | **RFC3-18** (candidate) — exists |
| The two-root write boundary | **VIS-6** (adopted); RFC3-1 (candidate) — exists |
| Machine/human parity for the entry point's facts | **RFC6-13**, **RFC6-14** (candidate) — exists |
| **The fixed path itself** | **missing** — no clause names `.syzygy/intent/OVERVIEW.md` as *the* entry point. Smallest home: RFC7-6, which already binds "at most one primary narrative" and would gain "and its rendered entry point lives at one fixed path" |
| **The discoverability finding** | **missing** — no clause defines it. Smallest home: RFC3-6, which owns repository entries |
| Everything observable | **OpenSpec Capability 1** — see `FIRST-OPENSPEC-SEQUENCE.md` |

**Two contract gaps, both small, and neither filled here.** They are one-line
additions to clauses that already exist, and adding them is a normative edit
to act 1's digest subject in the same pass that froze it for review. They are
recorded for the next pass rather than smuggled into this one.
