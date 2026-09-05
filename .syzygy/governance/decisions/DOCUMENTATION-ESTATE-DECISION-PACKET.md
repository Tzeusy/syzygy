# Owner decision packet — four questions about the written estate

> **Pending. This packet decides nothing and adopts nothing.** It states four
> questions, gives the evidence for each, recommends an answer, and says what
> happens if you say nothing. Register rows: **P-54 … P-57** in
> [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md). Answer all four
> in one reply, or any subset; none depends on another.
>
> Written 2026-09-05 during a documentation consolidation pass. Nothing in
> this packet is a change to any accepted artifact; each question exists
> precisely because the change it asks about would land on the governed plane,
> where only you may put it.

## Why these four, and why together

The repository holds roughly twelve megabytes of tracked prose, most of it the
closed record of work that is finished. A consolidation pass can safely repair
navigation, staleness, and duplicate homes on the implementation side without
asking you anything — and that part is done. Four items remained that an agent
may not decide, because each would write to, remove from, or restructure the
governed plane. They are gathered here rather than raised one at a time.

---

## P-54 — The OpenSpec config file is still the vendor's example

**What is there.** `openspec/config.yaml` is five useful bytes and twenty
lines of shipped-example comment. Its only live setting is
`schema: spec-driven`. Everything below that is the OpenSpec starter template,
including a commented-out example describing a TypeScript/React e-commerce
platform and an example rule capping proposals at five hundred words.

**Why it matters.** The commented `context:` block is described in the file
itself as text "shown to AI when creating artifacts." Left as the vendor's
example, it does nothing; filled in, it becomes standing instruction to every
agent that authors a specification here. That is a governed-plane authoring
input, so what goes in it is yours to write, not an agent's to guess.

**The arms.**

- **(a)** Write a real `context:` block — the stack, the two-plane rule, the
  epistemic-labelling requirement, and the fact that a proposal binds nothing
  until you sign it. An agent can draft it for your edit; you decide the
  bytes.
- **(b)** Delete the commented example lines, leaving `schema: spec-driven`
  alone, and rule that this project's context travels through `AGENTS.md` and
  the governed plane rather than a tool config.
- **(c)** Leave it exactly as it is.

**Recommendation: (b).** The project already has a well-maintained place where
an agent learns its context, and CC-REV-3 warns against a second home for the
same answer — a populated `context:` block would become one, invisible to
anyone not reading tool config. Deleting the example is the smaller change and
removes an e-commerce paragraph that has never described this project.

**Default if unanswered:** nothing changes; the file keeps the vendor example.

---

## P-55 — `openspec/specs/` and `openspec/changes/archive/` are both empty

**What is there.** Three change directories under `openspec/changes/`:
`project-registration-and-honest-shape-visibility` (adopted 2026-08-20),
`three-surface-poc-experience`, and `polaris-project-wide-butlers-model`. The
two directories the OpenSpec convention reserves for *settled* material —
`specs/` and `changes/archive/` — are empty, and have been since the tree was
created.

**Why it matters.** In the ordinary OpenSpec lifecycle a change is archived
once it lands, and the requirements it introduced come to rest in `specs/`,
which then reads as the current specification. Here, Capability 1 is adopted
and implemented, yet its requirements are still only reachable inside a
directory named `changes/`. A reader looking for "what does this system
specify today" finds an empty `specs/` and has to know to look somewhere that
sounds provisional.

**The arms.**

- **(a)** Adopt the lifecycle: archive the adopted change and materialize its
  requirements into `specs/`. This moves adopted bytes, so it is an act, and
  it needs its own review — an agent may prepare it, never perform it.
- **(b)** Rule that this project deliberately does not use the archive and
  spec-materialization steps: `changes/` is the permanent home, and
  `.syzygy/governance/` plus `PROJECT-STATUS.md` answer "what is specified
  today." Then the two empty directories get a one-line README saying they are
  intentionally unused, so their emptiness stops reading as an omission.
- **(c)** Defer, with the emptiness disclosed as a known gap.

**Recommendation: (b).** The lifecycle move buys navigation the governed plane
already provides, at the cost of relocating bytes you have accepted and bound
by digest. Saying plainly that the convention is not used is cheaper, is
honest, and removes the only thing an empty directory currently communicates,
which is that someone forgot.

**Default if unanswered:** both directories stay empty and unexplained.

---

## P-56 — A spent owner prompt sits at the repository root

**What is there.** `syzygy_begin_specification_stage_capability1_prompt.md`,
about nine hundred lines, at the top level of the repository. It is the prompt
that opened the Capability 1 specification stage. That stage is finished:
Capability 1 is adopted and implemented.

**Why it matters.** It is not junk — the Capability 1 specification-authoring
decision record cites it, and cites it *by its location*, calling it
"(repository root)." So it is evidence for a recorded decision, and moving it
silently would break that citation. But the repository root is the first thing
a newcomer sees, and it currently carries a spent working prompt beside the
README, the licence, and the status page.

**The arms.**

- **(a)** Move it into the historical tree (alongside the other spent
  round material) and amend the one citing sentence in the decision record to
  name the new path. The decision record is not digest-bound; the amendment
  is a single-line path correction with no semantic content.
- **(b)** Leave it at the root, and add one line to its head saying it is
  spent, what it opened, and that it is kept at the root because a decision
  record cites it there.
- **(c)** Leave it entirely as is.

**Recommendation: (b).** It is cheap, it breaks no citation, and it fixes the
actual defect, which is that nothing on the page tells a reader the prompt has
already been answered. (a) is also lawful and tidier, but it edits a decision
record to buy a tidier root listing, and the trade seems the wrong way round.

**Default if unanswered:** the file stays at the root, unmarked.

---

## P-57 — `openspec/` has no door

**What is there.** No index at any level of `openspec/`. A reader arriving at
the directory sees `config.yaml`, `changes/`, `specs/`, and three change
directories whose names do not say which one is adopted, which is a bounded
non-release experiment, and which is a later repair to that experiment. One of
the three proposals also lacks the "Candidate specification" banner the other
two carry, so its status is invisible at its head — and it cannot be given
one: every byte of `polaris-project-wide-butlers-model/` is bound by the PWB
truth-and-readiness amendment performed 2026-09-05, and its `proposal.md`
still hashes to the manifest row that act's argument covers. Adding a banner
there would break a performed act's argument.

**Why it matters.** This is the same defect that was just repaired in `docs/`
and in the contract tree: authority exists and is correct, but nothing routes
a reader to it, so people navigate by guessing at directory names. The
difference is that `openspec/` is the governed plane, so an agent adding a
page there is exactly the kind of quiet governed-plane authorship the two-plane
rule exists to prevent — even when the page is pure navigation.

**The arms.**

- **(a)** Authorize an agent to write a top-level README under `openspec/` as navigation only:
  which change is adopted and under which act, which are candidate, what the
  empty directories mean (see P-55), and a banner saying the page is never
  authority. Owner review before it lands.
- **(b)** Rule that the governed plane takes no navigation pages, and route
  readers to `openspec/` from `PROJECT-STATUS.md` and `AGENTS.md` instead —
  both of which are outside the plane and already own current state.
- **(c)** Leave `openspec/` without a door.

**Recommendation: (a), with (b) as a close second.** The tree has three
sibling directories in three different states, and that is more than a
one-line pointer from elsewhere can carry honestly. But if you would rather
the governed plane stay free of agent-authored pages as a matter of principle,
(b) costs little: the same information can live in `PROJECT-STATUS.md`, which
is already the page that owns which acts are in force.

This also makes an index the *only* lawful place to disclose that third
change's status. Its head cannot carry a banner without breaking the act, so
if the answer is (b), the routing sentence in `PROJECT-STATUS.md` has to say
which of the three is bound and by which act — a pointer alone will not do.

**Default if unanswered:** `openspec/` keeps no index, and the status of the
three sibling changes stays legible only to a reader who already knows the act
record.

---

## What was repaired without asking

For contrast, so the boundary of this packet is legible. All of the following
were done in the same pass, on the implementation plane or as pure disclosure
repair, and none needed an act:

- The candidate contract package's front page claimed no owner act had ever
  been performed over any of it, and that the accepted home did not exist.
  Both had been false since 2026-08-17. Repaired, with the superseded
  paragraph kept and dated rather than deleted.
- `docs/` had no index at any level and cited no maintenance contract. It now
  has one, and it cites CC-REV-2/3/5/6/7 rather than restating them.
- The historical index listed five of eleven closed rounds. It now lists all
  eleven, and resolves the twelve filenames that occur in more than one round
  — three of which begin with `FINAL-` and are not final.
