# RFC-0006 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
`../rfcs/RFC-0006-cross-surface-selection-query-drawer.md`. Full review
corpus: `_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`.

---

## Document-level

**Reader's summary (rev9 §0).** The rev9 file opened with a seven-bullet
plain-language summary ("This RFC makes 'one kernel, three surfaces' checkable
from outside…"). It carried no normative content — every property it named is
a clause — and was compressed at rev10 into the §0 reader map. Two phrasings
worth keeping as reading aids:

> "Machines see exactly what humans see. Endpoints answer from the same fact
> set the UI renders, with epistemic labels verbatim — an agent must be
> exactly as unable to mistake Unknown for success as the owner is."

> "'Observed ×30' is honest only when you can also see that all 30 are
> reduced-fidelity, 12 are stale, and 3 are dismissed by decision."

**§1 Summary (rev9).** Compressed at rev10; the enumeration it carried
(selection reference over RFC 0001 identities, closed outcome set, URL
identity semantics, label parity, the SDR-27 equivalence definition, scenario
context) survives as the clauses themselves, and the §0 map points at each.

**Provenance note (rev9 §Serves).** RFC 0006 refines the research selection
contract SC-1…SC-9 from
`_bootstrap/drafts/surface-shaping/03-SHARED-KERNEL-BRIEF.md` §4 — a
non-authoritative input, superseded where this RFC differs. SC-numbers cited
in active clauses (SC-1, SC-2, SC-4, SC-5, SC-7, SC-8, SC-9) refer to that
brief.

---

## RFC6-2

Rev9 carried a refinement parenthetical, extracted at rev10:

> *(Refinement of SC-1, which named only Capability and Requirement as
> everywhere-selectable: the total-resolution obligation below makes the
> narrower list unnecessary.)*

Backlink: RFC6-2 in the active contract still binds "every V0-core entity
(RFC1-5) is selectable"; the widening from SC-1's two-entity list is recorded
here, not in the clause.

---

## RFC6-14

Rev9 closed the `challenge-pending` paragraph with its justification,
extracted at rev10:

> …it travels **beside** them, because a claim whose surface render discloses
> a pending challenge and whose machine answer does not is exactly the
> divergence RFC6-13 forbids.

The obligation itself (parity for `challenge-pending`, never displacing label
/ tier / reason / freshness) is unchanged in the active clause.

---

## RFC6-17

Rev9 recorded the amendment history of the tier enumeration inside the clause;
extracted at rev10 (obligation — **all six** RFC2-25 tiers plus the three
sibling surface states — unchanged in the active clause):

> **All six**, not a subset: the enumeration previously omitted `gate-backed`
> and `asserted-by-worker`, and the second omission mattered — it is the one
> tier whose parent label is Inferred, and "Inferred ×8" that does not
> disclose that all eight are worker assertions with no retained artifact is
> precisely the laundering this clause exists to prevent. An aggregation
> obligation narrower than the equivalence obligation over the same objects
> would let those labels be dropped at the moment elements merge, which is
> exactly where doctrine requires staleness to stay visible on the primary
> surface rather than in drill-down. "Unknown ×40" is honest exactly because
> the 40 is disclosed and expandable.

The active clause keeps the `asserted-by-worker` point as its canonical
example and states the width rule directly ("exactly as wide as the
equivalence obligation").

---

## RFC6-19 (content class 6, challenge and contradiction state)

Rev9 justification, extracted at rev10 — the rule (every open challenge
travels with its RFC2-13 lifecycle state; `submitted` belongs to the fact set
exactly as `admitted` does) is unchanged:

> …and a fact set that flattened them would let a surface read a pending
> challenge as a live suspension or the reverse.

Origin: added at the rev8 review round, which found the drawer fact set silent
on `submitted` challenges while RFC2-13 required them rendered — a
surface-renders-what-the-fact-set-lacks divergence under RFC6-18.

---

## RFC6-24

Rev9 History parenthetical on the **Base** scenario name, copied verbatim:

> *(History: renamed from `Current` at the rev7 rework — directive item B6 of
> `_bootstrap/rfc-phase/REV7-REWORK-DIRECTIVE.md`, not owner decision B6 —
> semantics unchanged: the old name collided with the evidence-currency and
> freshness vocabulary — "current" evidence is a staleness claim, and a
> scenario name must never read as one. `Base` is the corpus's own word:
> Proposed is (base evaluation, proposal set), and every proposed scene "names
> its base". It is distinct from the *layout baseline* (RFC9-14), which is a
> layout input, never a scenario.)*

The active clause retains the Base/layout-baseline distinction as a live
interpretive rule and the non-default-revision marker obligation; only the
rename narrative moved here.

Doctrine amendment **D1** (map historical scope) is cited in the active
Historical bullet. Full amendment text and ratification record:
`.syzygy/governance/doctrine/` amendment log (ratified 2026-08-01, applied to
`architecture.md` at commit `84d4a88`).

---

## RFC6-28

Rev9 History parenthetical, copied verbatim:

> *(History: added at the rev8 rework — the fresh-context final review found
> this RFC outside the phase rule its three consumer surfaces carry, leaving
> the most directly user-observable cross-surface contract schedulable from
> RFC prose alone.)*

The clause body — the binding phase rule, its coverage-matrix deliverable, and
the "creates no OpenSpec content now" boundary — is retained at full strength
in the active contract, shape-parallel with RFC7-38, RFC8-32, and RFC9-52.

---

## §5 Integration — the RFC 0002 defect narrative

Rev9 recorded a defect against RFC 0002 in the Integration section; extracted
verbatim at rev10 (the active file keeps the mapping and the owner decision in
one sentence):

> **Defect noted against RFC 0002:** RFC2-24 has no Unknown reason for a
> **captured source whose internal anchor no longer resolves** (RFC1-15's
> degrade case — e.g. an OpenSpec requirement reference broken by edit).
> Reason #10 (`source-uncaptured-or-unreachable`) presumes the source was
> never captured; the diagnosis and resolution route differ (repair the
> reference/adapter anchor vs capture the source). This RFC maps the case to
> outcome `unresolvable` (RFC6-5) and routes the vocabulary question to
> acceptance (§8 q3) rather than inventing a reason RFC2-24 closed against.
> *[Update, post-draft: RFC 0002 has since added reason **#11
> `reference-unresolvable`** citing this defect among its four drivers. The
> defect stands as recorded; it is answered unless the owner strikes #11 at
> acceptance, in which case §8 q3 is live again.]*

Owner decision **A5** subsequently retained #11 (see §8 q3 below), closing the
conditional.

---

## §6 Alternatives considered (moved wholesale)

Three of these remain load-bearing for reading live clauses and are summarized
in one sentence each in the active §6, pointing here.

- **Surface-local selection IDs with kernel mapping tables.** Rejected: every
  mapping table is a second identity authority that can drift, and the trust
  floor's link rule would then depend on a join. One identity space makes
  divergence structurally impossible. *(Live clause: RFC6-1.)*
- **Silent redirect from retired identities to successors.** Rejected
  (RFC6-11): a merge/split is a governance event; auto-following asserts an
  equivalence no one adopted — the same error class as RFC1-12's rejected
  judgment transfer. *(Load-bearing.)*
- **Evaluation-pinned URLs only.** Rejected: it makes "the current state of X"
  — the owner's most common selection — unlinkable. Two temporalities with
  mandatory stamping (RFC6-10) keep both honest.
- **Per-surface drawers with a shared minimum.** Rejected (RFC6-18): the
  "extras" become facts one surface has and another lacks — exactly the fork
  SC-4 forbids — and agents cannot know which drawer they got.
- **A `not-applicable` Unknown reason.** Rejected (RFC6-6): RFC2-24 is a
  closed claim-status vocabulary; navigation outcomes stamped as Unknown
  reasons corrupt Unknown counts and mis-route resolution. *(Load-bearing.)*
- **Label-bearing URLs (slugs as identity).** Rejected (RFC6-9): slugs break
  on rename or demand a redirect registry — a second identity store. Labels
  may decorate a URL only if ignored by resolution. *(Load-bearing.)*

---

## §8 q3 — answered, moved from the active file

Question as posed in rev9:

> 3. **Dangling-reference vocabulary (Integration defect).** Should RFC2-24 be
>    amended with a `reference-unresolvable` reason (or #10's condition
>    broadened) so RFC6's `unresolvable` outcome has a claim-status
>    counterpart when a broken anchor degrades a claim? This RFC's mapping
>    works without it, but the resolution route ("repair the anchor") is
>    currently homeless in the closed vocabulary. *[Update, post-draft: RFC
>    0002 added `reference-unresolvable` as reason #11 and flags it for owner
>    confirmation at its own §8 q1(a). This question survives only as the
>    owner's option to strike it.]*

Answer, verbatim:

> **ANSWERED at acceptance — A5.** `reference-unresolvable` is **retained** as
> RFC2-24 #11; the dangling-reference case keeps its own reason and its own
> resolution route.

Backlink: the active §5 (Relies on RFC 0002) states the mapping and cites
owner decision A5; the active §8 keeps q3's slot marked answered so question
numbering never shifts.

Questions **q1** (unpinned-URL default), **q2** (`not-applicable` scope), and
**q4** (successor convenience) remain open and stay in the active §8.
