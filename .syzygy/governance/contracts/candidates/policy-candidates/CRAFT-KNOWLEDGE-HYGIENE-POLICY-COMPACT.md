> **Candidate — binds nothing, and does not replace its sibling by itself.**
> A proposed **compaction** of `CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` from
> twenty-two rules to **ten**. Both versions are offered; the owner picks one
> at the `CONFIRM CRAFT AMENDMENT` act (item P-12). No digest is stated here —
> digests are generated at offer time, and an artifact edited after its act is
> an artifact with no act.
>
> **No identifier is renumbered.** Ten identifiers survive at their original
> numbers; twelve are **retired**, each absorbed into a named survivor. Eleven
> tracked files already cite these identifiers, so renumbering would silently
> repoint live citations — the migration map at the foot is how a retired
> citation still resolves.

# Knowledge hygiene — compacted candidate craft policy

Syzygy's craft cluster has a consistent spine: *a claim needs a retained
artifact; absence renders Unknown, never zero; no actor grants itself an
exemption.* The cluster applies that spine to product surfaces, tests,
provenance, dependencies and security. It has never applied it to **the
project's own governance documents**. That is the gap, and it is a narrower
claim than "here are twenty-two new rules": most of what follows is the
governance-lane application of an obligation the cluster already carries
elsewhere, and says so.

## Why compact at all

The twenty-two-rule version is not wrong; it is unmemorable. A policy about
keeping knowledge loadable that cannot itself be held in a reader's head has
refuted itself. Ten rules is the number at which a reviewer can check a change
against the whole policy without re-reading it.

Nothing was dropped. Every obligation in the long version survives in the
short one — the merges are of *rules that share an enforcement moment*, which
is why they were always read together.

## Scope and non-scope

**Scope.** How the project's own knowledge is kept true: where a fact lives,
how vocabulary enters, how normative text changes, what relation derived views
bear to their sources, what enters a reading path, and when size triggers
decomposition review. It reaches the **active governance lane** — doctrine,
contract modules, policy, topology, owner decisions, front-door files — and
every derived view over it.

**Non-scope.** What any rule should *say* (doctrine and the contracts own
that); the owner acceptance ceremony (the acceptance record owns it); the
content of the term registry (a sibling candidate, cited as a mechanism, never
as authority); enforcement tooling; code and runtime documentation once
implementation exists.

**Precedence**, unchanged from the cluster README: adopted doctrine and owner
rulings > this cluster > the canonical bar. Where an installed clause already
owns an obligation, this policy **cites it and does not restate it** — a
restated rule drifts and becomes the shadow authority CC-REV-3 forbids.

---

## The ten

### CC-KNOW-1 — A governance fact is stated at its one home, or cited; and every artifact states its non-scope

Every fact in an active governance artifact is either stated at the single
home the typed-authority table assigns it, or is a **citation naming that
home** — including in routers, indexes, status pages and front-door files,
which are the surfaces most tempted to paraphrase for convenience. Each
artifact states not only what it covers but **what it does not**: an artifact
that states only its scope invites readers to assume it covers the adjacent
thing. *Extends:* **CC-REV-3**. *Absorbs:* CC-KNOW-2.

*Violation:* a router paraphrasing a doctrine rule "so agents don't have to
open the file," after which agents obey the paraphrase and nothing re-points
them when the doctrine is amended. And: two contract modules each silent on a
neighbouring concern, each assuming the other owns it.

### CC-KNOW-3 — Active artifacts carry current obligations; superseded material leaves every reading path in the same change

An active artifact states what is required **now**; superseded wording, prior
revisions, negotiation narrative and rationale live in the historical lane,
reachable by citation. When material is superseded, retired or moved, **the
same logical change** removes it from every default reading path, index and
router. Retention is not the problem; reachability by a reader who does not
know it was superseded is. *Extends:* **CC-REV-2**. *Absorbs:* CC-KNOW-14.

*Violation:* a retired acceptance phrase still named as the binding
precondition by two tracked files a revision after its retirement — the
retirement was correct and the propagation never happened. [Observed]

### CC-KNOW-4 — Everything an active artifact rests on resolves in a fresh clone, verified there

Every active-lane artifact — **and every warrant it names as the basis of its
own authority** — resolves in a fresh public clone. A governance change is
done only when a clone can read the changed artifacts, resolve their
citations, and run the repository's checks without founder-local material,
**verified in that clone, not asserted from the working tree**. A basis that
resolves only on the founder machine is a recorded defect, not a convenience.
*Extends:* **CC-PROV-3**. *Absorbs:* CC-KNOW-15.

*Violation:* an approval record whose sole warrant is a git-excluded path, so
a clone reader can verify the change happened but not that it was authorized.
And: a policy adopting an external engineering bar "as read on" a date, by a
machine path — where the installed tree had since moved two commits and gained
two unapproved rules, with the drift rule unenforceable because nothing could
resolve the path. [Observed — both.]

### CC-KNOW-6 — Terms are scarce, and new vocabulary enters through the registry

A new durable term is admitted only when no existing term covers it, its
distinction matters operationally, its owning authority and lifecycle are
clear, and a technically capable newcomer can explain it after one paragraph.
Vocabulary growth is not free: every term added is a term every future reader
must hold.

The term registry is the admission mechanism. A term used normatively without
a registry entry is unadmitted; a term that carries obligation while no clause
defines it is a **contract gap to report** — never a gap for a registry, index
or summary to fill, because a derived artifact supplying a definition
manufactures authority. Renaming or retiring a term across artifacts requires
a reviewed migration report *before* the sweep. (CC-REV-7 governs stable
identifiers; this governs words.) *Absorbs:* CC-KNOW-5.

*Violation:* a registry inventing a plausible definition for a term no clause
defines, which becomes operative by repetition.

### CC-KNOW-7 — Normative edits travel as semantic deltas; "editorial" is a claim; whole-file rewrites carry a mapping

A change to active-lane normative text is proposed as a semantic delta
recording current meaning, proposed meaning, change class, warrant, evidence
basis, terms moved, downstream impact, what explicitly does not change, the
migration plan, and the review class.

**"Editorial" and "no semantic change" are reviewable claims, never
exemptions** — the class is stated up front precisely so a reviewer can
contradict it, and class is determined by what changes in the obligation,
never by diff size. **Replacing an active normative file wholesale** requires
stated justification and an old→new mapping covering every stable identifier;
structural moves preserve identifiers. A full rewrite conceals which meanings
changed — that is its defect, independent of intent. *Extends:* **CC-BAR-7**.
*Absorbs:* CC-KNOW-8, CC-KNOW-10. Protocol: `NORMATIVE-CHANGE-WORKFLOW.md`,
`SEMANTIC-DELTA-TEMPLATE.md`.

*Violation:* a one-line edit labeled Editorial that swaps the precondition on
which a policy binds — one line, a different obligation. [Observed]

### CC-KNOW-9 — Material normative change gets fresh-context review, and the verdict word is copied

A material change to an active-lane artifact — **including candidate
governance material and this policy** — is reviewed by a session that neither
authored it nor holds the authoring context, and that receives the artifact,
its governing references and the acceptance criteria, not the author's
reasoning or a desired verdict.

Raw reviewer output is stored **verbatim and never edited**; a verdict word is
**copied exactly**, never re-labelled — `EXCEPTIONS` never becomes "pass with
findings". Where stored output trips a repository check, the checker is
allowlisted; changing the report destroys the evidence the allowlist exists to
protect. *Extends:* **CC-REV-1**, **CC-REV-4**.

*Violation:* an agent drafting a policy, re-reading it later in the same
session, and recording "reviewed" — self-review wearing a review's label.

### CC-KNOW-11 — Derived views are never authority, and current-state prose carries its as-of

Indexes, maps, manifests, routers, status pages and summaries are **derived**:
each is labeled derived, names its source, and regenerates **after** the
source is adopted — never in anticipation of an approval that has not
happened.

Prose asserting what is currently true carries its **as-of revision** and is
never the sole source for the fact it states; prefer a generated or queryable
view, because a current-state section that must be hand-edited whenever
reality changes is a known decay site. (CC-REV-5 governs epistemic labelling;
this governs currency.) *Absorbs:* CC-KNOW-12.

*Check:* `CG-27` in `scripts/check_governance.py` enforces a **floor** under
this rule's second paragraph over the default reading path — every claim about
current wave, gate or launch state either names the record that owns it, sits
under a leading banner that names it, or carries its own as-of date. It
enforces *less* than the clause (which requires both an as-of *and* a
non-sole source), and it never checks whether a claim is **true** — only
whether a reader who doubts it can tell where to go. It is advisory until this
policy is ruled (P-12). *(Added 2026-08-13, owner charter §11.4 — the rule
predates the check, and this line exists because the policy's own closing
section says a rule names its check where one exists.)*

*Violation:* a status file describing "the current gates" in three
hand-maintained places, two of them a revision behind, none saying as of when
it was true.

### CC-KNOW-13 — Context is compiled, not accumulated

A task loads the minimum artifact set needed for one correct decision, named
in advance as a packet, rather than a growing pile of everything read so far.
"Read the governance tree first" is not a context strategy.

*Violation:* an agent told to load the whole governance directory, which
spends its budget on material irrelevant to its decision and still misses the
one clause that governs it.

### CC-KNOW-17 — Every figure carries its derivation; completeness claims require the sweep; a new check's first result is a claim about the checker

Any quantitative claim in an active or governed-presentation artifact states
how it was computed. **Group totals are computed by script, never hand-summed;
digests are scripted, never hand-transcribed.** After a batch of edits, the
self-referential counts of *every file the batch touched* are re-verified.

**"All", "none", "zero", "100%"** may be written only if the exact sweep
described was run against current content **in the same session**; otherwise
enumerate what is known and state the remainder as unknown. A sweep returning
nothing supports a universal claim only when a second method agrees — a
silently-failing pattern and a genuinely empty corpus are indistinguishable
from the output.

**A validation check's first result against a new corpus is a hypothesis about
the checker** until at least one hit is confirmed by reading the source, and a
passing check proves nothing until it has been shown able to fail. Every check
reports its **denominator** and the **class it covers**: a truthful count over
the wrong population is still the wrong answer, and a zero-count check reports
WARN, never PASS. *Absorbs:* CC-KNOW-16, CC-KNOW-18.

*Violation:* a dependency index reporting twenty asymmetric edges at every
generation while its own drift check reported clean — because regenerating a
knowingly-broken graph reproduces the same knowingly-broken file. [Observed]

### CC-BUDGET-1 — Budgets are decomposition triggers over the active lane, and waivers expire

| Artifact | Budget trigger |
|---|---:|
| Root README | 1,200 words |
| AGENTS | 1,500 words |
| Active RFC module | 4,000 words |
| Exceptional active module | focused decomposition review above 5,000 words |
| Default context packet | 5,000–15,000 tokens |
| Context packet above 20,000 tokens | justification or task decomposition |

Crossing a budget triggers a **decomposition review, not a failure**: an
artifact over budget is not thereby invalid, and one under budget is not
thereby well-formed. The review asks whether an honest split exists; "none
does" is a lawful outcome, recorded rather than hidden.

A **waiver** records artifact, reason, scope, reviewer, and an expiry or
revisit trigger; the verifier prints the recorded justification alongside the
breach rather than passing silently. A waiver with no expiry is a permanent
exception pretending to be temporary.

**Budgets bound the active lane only.** Historical, evidence and scratch lanes
carry none; what is budgeted is what enters a default reading path. Retained
history may grow without limit. *Absorbs:* CC-BUDGET-2, CC-BUDGET-3,
CC-BUDGET-4.

*Violation:* a module split into two files just under the trigger, sharing a
preamble and always read together — the number is satisfied and the reader's
load is unchanged. And: deleting review evidence to bring a directory "under
budget", trading a real record for a number that never applied to it.

---

## Migration map — twenty-two to ten

**No identifier is renumbered.** A retired identifier stays resolvable: it
names the rule that absorbed it.

| Original | Status | Where its obligation lives now |
|---|---|---|
| CC-KNOW-1 | **survives** | CC-KNOW-1 |
| CC-KNOW-2 | retired | CC-KNOW-1, second sentence (non-scope) |
| CC-KNOW-3 | **survives** | CC-KNOW-3 |
| CC-KNOW-4 | **survives** | CC-KNOW-4 |
| CC-KNOW-5 | retired | CC-KNOW-6, first paragraph (scarcity) |
| CC-KNOW-6 | **survives** | CC-KNOW-6 |
| CC-KNOW-7 | **survives** | CC-KNOW-7 |
| CC-KNOW-8 | retired | CC-KNOW-7, second paragraph (editorial is a claim) |
| CC-KNOW-9 | **survives** | CC-KNOW-9 |
| CC-KNOW-10 | retired | CC-KNOW-7, second paragraph (whole-file mapping) |
| CC-KNOW-11 | **survives** | CC-KNOW-11 |
| CC-KNOW-12 | retired | CC-KNOW-11, second paragraph (as-of currency) |
| CC-KNOW-13 | **survives** | CC-KNOW-13 |
| CC-KNOW-14 | retired | CC-KNOW-3, second sentence (same-logical-change) |
| CC-KNOW-15 | retired | CC-KNOW-4, second sentence (verified in the clone) |
| CC-KNOW-16 | retired | CC-KNOW-17, second paragraph (completeness sweeps) |
| CC-KNOW-17 | **survives** | CC-KNOW-17 |
| CC-KNOW-18 | retired | CC-KNOW-17, third paragraph (checker hypothesis) |
| CC-BUDGET-1 | **survives** | CC-BUDGET-1 |
| CC-BUDGET-2 | retired | CC-BUDGET-1, second paragraph (trigger not law) |
| CC-BUDGET-3 | retired | CC-BUDGET-1, third paragraph (waiver expiry) |
| CC-BUDGET-4 | retired | CC-BUDGET-1, fourth paragraph (active lane only) |

**Ten survive, twelve retire, none is renumbered, none is dropped.** The
eleven tracked files citing the original identifiers continue to resolve
through this table.

## One obligation this version adds

CC-KNOW-9's second paragraph — **raw reviewer output is stored verbatim, the
verdict word is copied exactly, and a check is allowlisted rather than the
report edited** — is new. It was repository practice and a standing rule in
the agent operating procedure, and it was not in the long version. It is
listed here rather than folded in silently, because a compaction that quietly
grows is not a compaction.

## What this policy still does not do

- **Almost no rule here is script-checked.** These are obligations on people
  and agents, not validations. Where a check exists it is named in the rule —
  which today is `CC-KNOW-11` alone, and there the check is a floor under the
  clause rather than the clause. *(Corrected 2026-08-13: this sentence read
  "No rule here is script-checked", which stopped being true the moment CG-27
  shipped.)*
- **It does not say what any rule should say.** Doctrine and the contracts own
  that.
- **It binds nothing until its own owner act.** Item P-12.
