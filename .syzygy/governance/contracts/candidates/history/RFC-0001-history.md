# RFC-0001 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
`../rfcs/RFC-0001-project-graph-identity-state-planes.md`. Full review corpus:
`_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0001-project-graph-identity-state-planes.md`.

Every `*(History: …)*` parenthetical below is copied **verbatim** from rev9.
Moved narrative is labeled as such.

---

## §2 (rev9) — Motivation and doctrine grounding

*(Moved narrative. The doctrine-grounding sentences and their `[Observed]`
citations survive compressed in the active file's §1; the closing dependency
sentence and the failure-mode essay moved here.)*

> Doctrine keeps three states semantically distinct — desired, observed
> implementation, execution — and rules that work is never proof intent is
> satisfied [Observed: vision.md, Thesis]. It mandates one shared kernel under
> three non-authoritative surfaces, map geography anchored to capability
> identity rather than file paths [Observed: architecture.md; v1.md], statuses
> computed only at identified evaluations (VIS-2, VIS-7), rebuildability with
> two closed exceptions (VIS-6), and a trust floor whose link rule requires
> every internal reference to resolve to an identified target [Observed:
> trust-and-evidence.md, floor]. None of that is achievable without a contract
> that fixes *what the entities are, what mints their identities, which plane
> every source-state assertion lives in, and which semantic class every
> relation edge carries*. Downstream RFCs (0002–0009) and all three surfaces
> depend on this vocabulary being closed and stable.
>
> [Inferred] The dominant failure mode this contract guards against is the
> **silent default**: an unruled identity question gets answered by whatever
> the first implementation does, and the answer becomes load-bearing before
> anyone examines it. The fresh-context review of the research corpus found
> exactly this class of defect (execution state unplaced, derived gaps
> self-warranting work) [Observed: REVIEW-01-KERNEL.md K-F1, K-F2]. This RFC
> states the defaults explicitly so they can be accepted or rejected, not
> inherited.

The rev9 §0 "Reader's summary" is superseded by the active file's §1 reader
map, which carries the same orientation in shorter form. No normative content
was in either.

---

## RFC1-2 — Repository role, not a separate governance-root entity

*(History: adjustment to SDR §4, which lists the two as separate concepts: both remain V0-core; only the node count changes.)*

Surfaced to the owner as rev9 §8 q5 (verbatim):

> 5. **RFC1-2 (governance root as a Repository role, not its own entity).**
>    Surfaced here for the same reason as q4, and sized honestly: it is the
>    *other* place this RFC adjusts owner-ratified text, and leaving one
>    surfaced and one inline is an asymmetry this section should not carry.
>    SDR §4 lists Repository and governance root as **two separate concepts**;
>    RFC1-2 collapses the second into a declared **role** on the first, so
>    V0-core has one node class where the SDR's listing implies two. **Why:** a
>    second entity splits repository identity from the consent record's subject
>    (RFC3-7 makes the consent subject a repository), and a split subject is how
>    a repository ends up consented in one identity and observed in another.
>    **What actually changes:** only the node count — both concepts remain
>    V0-core, the role is declared and rendered, and no rule elsewhere in this
>    RFC depends on the collapse. **The alternative** is to restore governance
>    root as its own entity and give it its own identity, accepting the split
>    consent subject and a `governs`-style edge to the repository. Confirm the
>    collapse, or restore the SDR's literal two?

Answer (verbatim):

> **ANSWERED at acceptance — B22.** The **substance stands** (governance root is a Repository role), and the **process is corrected**: any future divergence from owner-ratified text is a surfaced item, never an inline note. The asymmetry — one divergence surfaced, its sibling recorded inline — was the defect, in a section that promises genuine owner-visible choices only.

Backlink: active RFC1-2 retains the substance and cites B22.

---

## RFC1-18(b) — Contradiction identity, two levels

*(History: new sub-clause; deliberate adjustment — SDR-2 rules two-level identity for claims and gaps only, and this extends the same treatment to Contradiction, which RFC1-25's `scoped_to` row and RFC1-31 already assumed.)*

Surfaced to the owner as rev9 §8 q4 (verbatim):

> 4. **RFC1-18(b) (two-level identity extended to Contradiction).** SDR-2
>    scopes durable-plus-instance identity to **claims and gaps**; RFC1-18(b)
>    extends the same treatment to Contradiction so that a changed cited-claim
>    set mints a new durable identity citing its predecessor, and a successor
>    renders **un-adjudicated with the predecessor's adjudication cited**
>    rather than silently inheriting it. This is a deliberate extension of an
>    owner ruling, taken because the alternative — no durable contradiction
>    identity — makes an `adjudicates` Decision either unbindable or silently
>    carried across a membership change, and RFC1-12 forbids the heuristic
>    that silent carry-over would require. Confirm the extension, or rule that
>    Contradiction stays instance-only and adjudication is re-requested on
>    every membership change. *(A consequence the owner should see: this also
>    gave RFC1-25's `succeeds` relation a derived form for Contradiction
>    successors, since no declaration act exists to carry that edge — the
>    relation was previously Desired/declared only.)*

Answer (verbatim):

> **ANSWERED at acceptance — B3.** **Extended.** Durable identity = (declared scope, canonically ordered set of the cited claims' durable identities); a changed set mints a new durable identity citing its predecessor via `succeeds`. An adjudication binds exactly the identity it named, so a **successor renders un-adjudicated with the predecessor's adjudication cited** — a visible inheritance question, never a silent carry-over. The re-adjudication tax is accepted deliberately.

Backlink: active RFC1-18(b) carries the rule and cites B3; the derived form of
`succeeds` for Contradiction successors is in the active RFC1-25 table.

---

## RFC1-22 — State planes and the act-assignment rule

*(Reworded at the rev8 rework, item 4 — the earlier "every fact" phrasing collided with RFC1-25's recorded edges; the model is two-dimensional: assertions carry planes, relations carry semantic classes that cite plane inputs.)*

---

## RFC1-25 — Relation vocabulary, semantic class list

*(History: restated at the rev8 rework, item 4)* — the closed semantic-class
vocabulary bullet list was made explicit at that rework; it is retained
verbatim in the active file.

---

## RFC1-25(c) — Cardinality of `placed_in`

*(History: added after review 8, finding ML-R8 — see the review dispositions.)*

---

## RFC1-25(d) — Typed relation identity

*(History: added at the rev7 rework — directive item B5 of `_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`, not owner decision B5 — completing RFC1-25(b): the twelve-pair invariant said the senses must not conflate, but left their *identity* carried by display spellings that differ by one character or not at all. Reworked at rev7 review 9, finding S3.)*

⚠ Provenance caution (repo-wide): the rev7 rework directive's item IDs (A1–A6,
B1–B6, C1–C4) collide with owner-decision IDs. "Directive item B5" above is
**not** owner decision B5.

Also removed from the active clause at the rev10 compaction, as pure
cross-reference narrative: "(RFC1-25's closed class vocabulary, restated there
at the rev8 rework)" — the class vocabulary citation survives; the rework note
is here. And the phrase "the class vocabulary is its own closed set naming
derivation" was compressed; the closure it restates is stated normatively in
RFC1-22 and in RFC1-25's class list.

---

## RFC1-25(a)/(b) — the two owner-minted relations and the four-sense invariant

The minting decisions (A6 `declared-dependency`, A7 `placed_in`) and the
spelling decision (B20) are recorded in the active file. Their owner-facing
question was rev9 §8 q6 (verbatim):

> 6. **A declared dependency relation (RFC1-25/RFC1-26) — the third side of a
>    decision already before you.** RFC1-25 closes `depends_on` to two endpoint
>    pairs, both non-declared: observed code→code and execution-class work→work.
>    The portfolio profile then declares a Project→Project dependency
>    (RFC 0003's `depends-on`, RFC3-14) which is **Desired/declared** — a
>    third state class, at a fourth endpoint pair, lawful under RFC1-7 but
>    outside this table. It was renamed post-draft away from `depends-on`
>    precisely so no reader takes it for this relation, and RFC1-25's
>    anti-conflation rule was widened to cover all three senses. **What is still
>    the owner's:** whether a *declared* dependency relation belongs in the
>    kernel vocabulary at all, or stays a profile relation. It is put here
>    rather than in RFC 0003 because the subject is this table's closure, not
>    the plane's shape. **A consequence worth seeing:** RFC9-9 rests part of its
>    legend rule on there being no declared dependency relation at V0 — true of
>    capabilities, topology entries and code elements, which is what it says,
>    but no longer the whole picture now that a declared dependency exists at
>    *project* scope. If a kernel-level declared relation is directed, RFC9-9's
>    legend and edge-channel rules need a corresponding pass. **Note this is one
>    decision seen from three sides:** RFC 0003 §7 defers the cross-project
>    relation *type vocabulary* to a portfolio-profile RFC, RFC 0009 §8 q5
>    reports the missing declared relation as a foundation defect, and this question
>    asks whether the kernel should carry one.

Answer (verbatim):

> **ANSWERED at acceptance — A6.** Yes: `declared-dependency` (Capability→Capability, Topology entry→Topology entry, Desired/declared) is **minted in the core vocabulary** by owner amendment — see RFC1-25 and RFC1-25(a). Separately A7 mints `placed_in`, and B20 reverted the portfolio relation's name to `depends-on`; RFC1-25(b) carries the resulting four-sense checkable invariant.

Open follow-on recorded by the question and **not** closed by A6: whether
RFC9-9's legend and edge-channel rules need a corresponding pass now that a
kernel-level declared dependency relation exists. That is RFC 0009 work.

---

## RFC1-29 — Materialization

The active clause's parenthetical "(violation case 10 unchanged)" refers to
the rev9 phrasing: "violation case 10 (one plan item materialized twice) is
unchanged". Case 10 is retained verbatim in the active file's §4.

---

## §6 (rev9) — Alternatives considered *(moved wholesale)*

### 6.1 The approved-but-unmaterialized plan item (the SDR §5 q1 options)

> - **(i) Dedicated pre-materialization plan-item entity.** Rejected. Its
>   content — what to do, why, under whose approval, exclusive with what —
>   duplicates the Proposal machinery (identity, review, adoption gate,
>   exclusivity group) node for node: a second store of "what we intend to
>   do," the exact merge-rejectable class the research corpus's
>   non-duplication test names, and a standing lockstep-drift risk with no
>   offsetting semantic gain. [Inferred]
> - **(ii) Approved plan as a kind/state of Proposal — chosen (RFC1-28).**
>   Honors the second-source prohibition by sequencing authority instead of
>   duplicating it: one entity, one identity, one authority for its state at
>   every instant (`.syzygy/work/**` before the materialization record, the
>   scheduler after — exactly SDR-7's split). Approval act, exclusivity
>   group, and provenance chain come free from machinery already required.
> - **(iii) Scheduler-native epic fallback.** Rejected. It contradicts
>   SDR-7 (the scheduler owns lifecycle only *after* materialization); it
>   moves approved-but-unexecuted intent into an external authority reached
>   only through an adapter, so approval state would live outside the
>   governed plane and be lost at offboarding; and it makes the owner's
>   approval act invisible to VIS-6 rebuildability.

Alternative (i) is the one load-bearing for reading a live clause; the active
file's §6 keeps a one-sentence statement of it with a pointer here.

### 6.2 Other roads not taken

> - **Governance root as its own entity** (SDR §4's literal listing) — made
>   a Repository role instead (RFC1-2): a second entity splits repository
>   identity and the consent subject.
> - **Aligned as a first-class edge** — rejected for the Claim predicate
>   (RFC1-8): a bare edge is unchallengeable and unscoped.
> - **Doctrine-claim and Contract kernel entities at V0** — deferred to the
>   presentation profile (RFC1-6); SDR §4 omits them.
> - **Automatic judgment transfer across splits/merges** — rejected
>   (RFC1-12); a heuristic would silently decide a governance question.
> - **Per-evaluation-only claim identity** — rejected by SDR-2; it orphans
>   challenges and dismissals at every re-evaluation.

---

## Compaction record (rev10)

Source: rev9 file at 9,534 words (`wc -w`), digest recorded in
`CURRENT-RFC-DIGESTS.md` / acceptance-record §3 as `34f930c5…`. Compacted
active file: see `../03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` for the corpus
figures and `../matrix-rows/RFC-0001-rows.md` for per-clause outcomes.

No clause was retired, merged, or renumbered. No obligation was removed. The
compaction moved: rev9 §6 wholesale, rev9 §2's failure-mode narrative, all
`*(History: …)*` parentheticals, and the three **answered** §8 questions (q4
B3, q5 B22, q6 A6/A7) with their verbatim answers. Everything else was
compressed in place or retained verbatim.
