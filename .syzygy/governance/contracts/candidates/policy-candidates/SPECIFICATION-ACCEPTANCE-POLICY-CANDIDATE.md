# Specification acceptance policy — candidate craft rule set

> **Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT`
> act.** Proposed at the 2026-08-10 launch-closure pass to close
> launch-gate question E5 (no acceptance criteria existed for a
> specification itself — "spec acceptance would be a vibe check").
> Identifiers `CC-SPEC-1…10`; amended in place, never renumbered. The
> testability sub-criterion (CC-SPEC-4) is the one E5 limb that had no
> criterion even in candidate form before this file.
>
> **Amended 2026-08-13** — the warrant rule, the requirement forms, the
> adoption clause and the dependency declaration. The delta is
> `../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`, which
> quotes every before/after text; the findings it answers are RD-51's,
> raw at `../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`.
> **This file and `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` are one
> model** and are reviewed and offered together: CC-SPEC-2 is the single
> home of a requirement's governing identities, and CC-IMPACT-1 generates
> the specification-level declaration from it.
>
> **Not frozen.** CC-SPEC-1's operative text is conditional on owner
> decision **P-40**, which is unruled. These bytes may still move.

## The rule

**CC-SPEC-1 — Capability and scope are clear.** The specification names
one coherent capability, what is in it, and what is out. A reader can say
what the capability is in one sentence without reading the requirements.

*"One coherent capability" is the granularity rule queued as **P-40**:*

> One OpenSpec change governs one coherent capability, or one coherent
> change to a capability. Its requirements may span several views, but the
> change has one owner-readable product argument and one acceptance
> decision.

**P-40 is not ruled** (`../../../decisions/PENDING-OWNER-DECISIONS.md`;
packet `../../../decisions/SPECIFICATION-GRANULARITY-DECISION.md`, whose
own first line is "This file decides nothing"). This clause therefore
states the rule it *proposes*, and its force is conditional: if the owner
rules P-40 arm (a), this clause is confirmed as written; if the owner rules
otherwise or declines, the clause is amended before the craft act, not
silently re-pointed. **This clause may not be frozen before P-40 is
ruled.** *(Restated 2026-08-13, RD-51 f3 — the clause previously said
"per the granularity rule, P-40", so its meaning would have changed with
no amendment the moment P-40 was ruled differently. A bound clause that
silently re-points is what CC-REV-7's discipline exists to prevent, and it
put CC-SPEC-1 in the very posture CC-SPEC-6 forbids.)*

**CC-SPEC-2 — Every requirement names all its material governing
warrants.** The rule:

> Every requirement names all material governing warrants. One may be
> marked primary for navigation; none may be hidden merely because another
> is more specific.

The warrant classes are a **closed set of six**, and a requirement's
declaration is machine-readable, one field per class:

```text
doctrine[]              adopted doctrine rule, by rule ID
contracts[]             accepted contract clause, by clause ID
policies[]              approved craft/policy clause, by clause ID
decisions[]             recorded owner product decision, by decision identifier
topology[]              accepted topology identity, by identity
parent_requirements[]   accepted parent requirement or specification,
                        by specification and requirement ID
```

Four rules govern the declaration:

1. **All material warrants, not one.** A requirement genuinely serving
   VIS-2, a reason-vocabulary clause and an owner decision names all
   three. Marking one `primary` is a navigation aid and removes nothing.
2. **Only accepted, adopted, approved or recorded authorities.** A
   candidate contract, an unapproved policy clause, an unaccepted topology
   identity and a **pending owner decision** are not warrants. A pending
   decision cited as a warrant is the CC-SPEC-6 violation with a citation
   attached.
3. **A requirement serving nothing on this list is a finding against the
   spec, not a bonus.**
4. **This declaration is the only home.** The specification-level
   dependency declaration is *generated* as the union of its requirements'
   declarations (CC-IMPACT-1). A hand-authored second list at
   specification level is a defect, not a convenience.

**`lawfully admitted user need` is deliberately not a class.** It appeared
in this clause until 2026-08-13 and is removed: no admission act, register,
or record class for a user need is defined by any authority in this
repository. `[Observed]` — the sweep, re-run 2026-08-13 in the session that
made this amendment rather than quoted from the review that prompted it.
Python `re` `user\s+need`,
case-insensitive, over `.syzygy/**` `*.md|*.yaml|*.json` — **371 files
scanned, 2 files with hits**: this clause's own discussion of the class, and
the review that found it. Second method, repo-wide over
`.md|.py|.json|.yaml|.yml|.txt` — **784 files scanned, 3 files with hits**:
those two, plus an untracked file absent from every commit. **No admission
act, register, or record class is defined by any authority.** A class whose
satisfying record
an author may name at will is an unbounded escape hatch in the clause whose
purpose is to close one. **Admitting the class requires first defining the
admitting authority and record in the shape layer** — queued as a question,
not assumed here.

*(Widened and restated 2026-08-13, RD-51 f2/f4/f5/f6. The clause previously
required a requirement to trace "to exactly one" of five sources. Three
defects: (i) "exactly one" was ambiguous between "one warrant exists" and
"name one", and supplied no tie-break either way; (ii) approved craft
clauses and accepted topology identities were unwarrantable although the
sibling policy made topology both declarable and sweepable — the two
policies named different authority sets; (iii) the rationale asserted that
P-31, P-36, P-37, P-38 and P-40 "are all owner rulings", which was false —
every one is pending — and that "the first specification is full of them",
describing a specification that does not exist. Those claims are withdrawn.
The true statement: these are **queued** decisions whose rulings, once made,
would become citable under `decisions[]`.)*

**CC-SPEC-3 — Every requirement has a stable identity.** Identifiers are
minted once, amended in place, never renumbered or reused, and a withdrawn
requirement's identifier is **retired in place with its entry marked
retired**, never deleted and never reissued — CC-REV-7's discipline
extended to requirement identifiers, including its retirement limb.
*(Retirement limb added 2026-08-13, RD-51's finding that the clause
extended CC-REV-7 to a new population while dropping half of it, leaving a
withdrawn requirement with no lawful disposition.)*

**CC-SPEC-4 — Every requirement is falsifiable in a named form.** A
specification's requirements take one of **five forms**, and the
requirement states which:

```text
event-response          a trigger occurs; a response is then observable
state projection/query  a query is made; the projected state is observable
invariant               a stated property holds across a stated scope
prohibition             a stated act or state never occurs within a scope
lifecycle transition    an entity moves between named states under stated
                        conditions
```

**Every form, without exception, names five things:**

```text
reachable/producible case      the case can be produced by a party performing
                               the check, using means the requirement names
observable consequence         what is then visible, and where — human view,
  or violation                 machine endpoint, or both
effective success/failure      how one decides the observation IS (or is not)
  oracle                       the expected one, by a stated procedure that
                               terminates in bounded effort, without judgment
oracle independence            the oracle is not defined by, and does not
                               consult, the implementation under test
concrete falsifying evidence   the specific observation that would show the
                               requirement unmet
```

For an **invariant** or a **prohibition** the "reachable case" is the
**scope of quantification, a counterexample schema, and the sweep whose
denominator bounds it** — a prohibition is satisfied by an exhausted
population, never by an absence of complaints.

**Four oracle forms are rejected outright:**

```text
tautological oracle                    "the value equals the value"
unbounded semantic-equivalence oracle  "the corpus and the code mean the same"
unreachable initiating condition       a case no party performing the check
                                       can produce
oracle equal to "whatever the          the implementation is its own judge
  implementation computes"
```

A requirement whose satisfaction no evidence could ever contradict is not a
requirement.

*(Rewritten 2026-08-13, RD-51 f7. The clause previously demanded four parts
— initiating condition, observable result, positive success oracle,
falsifying evidence — of "a testable observable requirement", and was wrong
at both ends. **Under-inclusive:** a prohibition such as "no surface renders
a green status from evidence whose currency bound is undeclared" — VIS-2's
own shape, and the dominant requirement shape this doctrine generates — has
no initiating condition and no positive success oracle, so the four-part
test rejected it while the clause's own closing sentence admitted it. Either
prohibitions were observable requirements and the clause wrongly rejected
them, or they were not and **no clause stated any testability bar for the
largest requirement class in the corpus**. **Over-inclusive:** the four
parts admitted an unreachable initiating condition ("a repository whose
evidence set has been continuously current for one year") and a tautological
oracle ("the flag equals what the reconciliation engine computes") — the
canonical bar's no-tautologies rule governs *tests*, and a spec's oracle is
not a test, so nothing forbade it. The five forms and the five universal
obligations replace the four parts; the oracle's **effectiveness** and
**independence** are the two additions that close the over-inclusive end.)*

**CC-SPEC-5 — Non-goals and Unknowns are explicit.** What the capability
deliberately does not do is listed; what is not yet known renders
Unknown with its reason, never silently omitted (VIS-2 and CC-REV-5
applied to the spec itself — cited, not restated).

**CC-SPEC-6 — No unresolved shape decision is silently selected.** If a
requirement's content would settle an open owner question, the spec is
blocked on that question — authoring around it by implication is the
violation this rule exists to name. Following VIS-4's own rule for the
analogous judgment, **this classification is contested by default and is
never finally made by the party authoring the requirement**: the spec
records which open questions it believes it does not settle, so a
misclassification is findable after the fact, and a reviewer or the owner
may reclassify at any time. *(Confirmer limb added 2026-08-13, RD-51's
finding that the clause's trigger was a counterfactual with nobody assigned
to evaluate it — the spec's own author was both the only party positioned
to notice and the party least able to.)*

**CC-SPEC-7 — Implementation detail appears only when it is required
behavior.** A stack, schema, or mechanism appears in a spec only if the
behavior being specified is genuinely about it; otherwise it belongs to
implementation, later.

**CC-SPEC-8 — Applicable contract clauses are covered or lawfully N/A.**
The clause-to-requirement coverage matrix (the phase-rule clauses'
obligation) is produced with the spec; every applicable clause is covered
by a requirement or carries a reviewed N/A judgment whose home and
provenance follow the corpus's reviewed-N/A rule. **The N/A judgment is
confirmed by a party other than the specification's author** — the
CC-TEST-4 pattern ("never made by the implementing agent alone …
confirmed by the change's reviewer, or the owner where no reviewer
exists"). *(Confirmer added 2026-08-13, RD-51 f15. Two further defects that
finding names are **not** repaired here and remain open: "applicable" is
undefined, and "the corpus's reviewed-N/A rule" carries no identifier while
the routing matrix names *this clause* as the rule's home — a circular
citation. Both are recorded in the delta; naming the clause requires reading
RFC modules that are candidates, and defining "applicable" is a rule this
session may not invent.)*

**CC-SPEC-9 — A fresh technical reader can restate it.** A specification is
a normative artifact, so **CC-REV-4** and **VIS-3** apply unmodified: a
reader with no authoring context restates intent and constraints correctly,
and failure is recorded on the artifact's surface. This clause adds nothing
and exists only so that E5's comprehensibility limb has a routed answer;
the obligation is CC-REV-4's. *(Reduced to a citation 2026-08-13, RD-51
f17 — the clause previously restated CC-REV-4 normatively, which CC-REV-3
forbids: "documentation cites authoritative artifacts, it does not restate
them normatively — a restated rule drifts and becomes a shadow authority.")*

**CC-SPEC-10 — Lawful adoption is recorded at the exact digest.**

> Lawful adoption under VIS-4 is recorded at the exact digest, and the
> record quotes what was adopted at which digest.
>
> **Under the current doctrine state this means owner adoption**, because
> VIS-4 opens the delegated gate only on **both** of two conditions —
> *"an accepted adjudication RFC (defining what makes adversarial judgment
> independent, how the ambiguity determination is recorded, and how each
> adopted change stays individually revertable)* ***and*** *the owner's
> explicit doctrine amendment recording that the gate opens; RFC acceptance
> alone never opens it"* — and neither exists.
>
> **One class is always human-gated, gate open or not:** VIS-4 —
> *"spec changes touching security posture, privacy or retention
> obligations, or normative data contracts."* No delegated mechanism ever
> reaches this class.

Until the adoption record exists the spec is a candidate like everything
else. *(Restated 2026-08-13, RD-51 f12. The clause previously read "Lawful
adoption under VIS-4 is recorded at the exact digest. Under the current
doctrine state, this means owner adoption." Word-by-word against VIS-4 it
**added** the digest binding — its genuine contribution — **paraphrased
correctly** for today, and **subtracted** two limbs: the two conjoined
preconditions, and the always-human-gated class. The subtracted sentence is
precisely the rule that binds in the future the restatement was written to
anticipate: a reader in a gate-open future, reading CC-SPEC-10 alone, would
conclude the entire spec corpus is LLM-adoptable at a digest. The clause now
quotes both limbs rather than glossing them.)*

## What this policy is not

Not a workflow (the th-projects feature-request workflow is referenced
process, never authority); not a format (P-39 owns the medium); not a
review procedure (CC-REV-1/2/4 own review). One fact, one home.

## Known open findings against this file

`[Observed]` — from RD-51, raw at
`../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`;
dispositioned in `../round-2026-08g/reviews/DISPOSITION-REGISTER.md`.
Listed here because a candidate that hides its own open findings is the
failure VIS-2 names.

| Finding | Open defect |
|---|---|
| f14 | **No clause tests a specification for completeness against its capability.** E5 asks that a spec be judged "complete, testable, and faithful"; CC-SPEC-8 is completeness with respect to contract clauses, CC-SPEC-5 requires non-goals but not in-scope coverage, and CC-SPEC-1 requires scope *stated*, not *covered*. 0 of 10 clauses ask whether the requirement set covers the capability it claims. E5's "complete" limb is unclosed |
| f15 (part) | "applicable" (CC-SPEC-8) is undefined, and "the corpus's reviewed-N/A rule" has no identifier while the routing matrix routes the deliverable back to CC-SPEC-8 — each names the other as owner |
| f1 (sibling) | the lagging-specification exception is not lawful until CC-REV-2 is itself amended — see `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` CC-IMPACT-6 and the offer it names |
