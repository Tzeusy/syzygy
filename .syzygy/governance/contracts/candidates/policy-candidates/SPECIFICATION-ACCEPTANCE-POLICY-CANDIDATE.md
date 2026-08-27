# Specification acceptance policy — candidate craft rule set

> **Proposed post-act amendment — non-binding.** Acts 6 and 7 confirmed the
> predecessor CC-SPEC bytes at sha256
> `9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871`.
> Those predecessor bytes remain the binding mainline policy. The edited
> bytes below are a draft successor: they do not bind, replace, or amend the
> confirmed policy unless an independent review is completed and the owner
> confirms the exact proposed digest in a new act.
>
> Identifiers `CC-SPEC-1…11` remain stable and are never renumbered. This
> file and `SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` remain one model:
> CC-SPEC-2 owns requirement provenance, and CC-IMPACT-1 generates the
> specification-level declaration from it. The plain-language change summary,
> exact before/after text, evidence, non-goals, and review requirements are in
> `../round-2026-08l/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA-3.md`.

## The rule

**CC-SPEC-1 — Capability, scope, and acceptance unit are clear.** The
specification names one coherent capability, what is in it, and what is out.
A reader can say what the capability is in one sentence without reading the
requirements. Each proposed specification change also says whether its
acceptance unit is the whole capability or one focused change to that
capability.

*"One coherent capability" is the granularity rule the owner ruled on
2026-08-16 as **SDR-37** (`../../../decisions/SURFACE-DECISION-RECORD.md`),
quoted exactly:*

> the specification-granularity rule — **one OpenSpec change governs one
> coherent capability, or one coherent change to one**: one owner-readable
> product argument, one acceptance decision per change.

The rule is cited from its recorded home, never restated normatively here.

The two acceptance units are distinct:

1. **Whole-capability acceptance.** The owner-readable argument covers the
   complete capability declared by the specification. CC-SPEC-11 independently
   enumerates the coverage population from the scope, complete requirement
   inventory (including retired entries), and non-goals. The acceptance
   decision applies to that classified population at the exact digest recorded
   under CC-SPEC-10.
2. **Focused-change acceptance.** The owner-readable argument names the
   accepted capability baseline being changed and the exact obligations the
   change adds, modifies, retires, or makes newly relevant. CC-SPEC-11
   independently enumerates the coverage population from the exact
   baseline-to-proposal difference, the change scope and non-goals, and a stated
   affected-baseline sweep. The acceptance decision applies only to this
   classified coherent change at the exact digest recorded under CC-SPEC-10;
   it does not silently re-accept the whole capability or widen the change's
   declared scope.

Both units must satisfy CC-SPEC-2 through CC-SPEC-11. If a reviewer finds an
obligation omitted from the declared coverage population, the acceptance-unit
statement is incomplete; narrowing the population does not make the change
acceptable.

**CC-SPEC-2 — Requirement provenance names every material governing
authority.** In this rule, a *governing warrant* means the accepted authority
that explains why a requirement belongs in the specification. It does not
authorize drafting, implementation, scheduling, or any other work. The rule:

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

**A work warrant is separate.** RFC1-25 defines the `motivates` edge from a
permitted authority to a work item or proposal as the work-warrant carrier. A
confirmed review finding may warrant corrective work through that edge, but it
is not a seventh requirement-provenance class and is not inserted into the six
fields above. RFC1-25 requires a recorded confirmation act before a
finding-class warrant can motivate work. If an adopted, accepted, approved, or
recorded authority later incorporates the finding's substance, a requirement
cites that authority in the matching provenance field. A work warrant never
makes proposed requirement text accepted.

**`lawfully admitted user need` is deliberately not a class.** This policy
defines no authority or record that could admit such an entry. Adding it first
requires a shape-layer definition of the admitting authority and record, then
an amendment to this closed set. Exact sweep evidence belongs in the amendment
record, not in this binding rule.

**CC-SPEC-3 — Every requirement has a stable identity.** Identifiers are
minted once, amended in place, never renumbered or reused, and a withdrawn
requirement's identifier is **retired in place with its entry marked
retired**, never deleted and never reissued — CC-REV-7's discipline
extended to requirement identifiers, including its retirement limb.

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
may reclassify at any time.

**CC-SPEC-7 — Implementation detail appears only when it is required
behavior.** A stack, schema, or mechanism appears in a spec only if the
behavior being specified is genuinely about it; otherwise it belongs to
implementation, later.

**CC-SPEC-8 — Applicable contract observable consequences are covered or
lawfully N/A.** The observable-consequence-to-requirement coverage matrix is
produced with the specification; every applicable observable consequence is
covered by requirements or carries a reviewed N/A judgment. **Rows are per
observable consequence, not per clause** (RFC1-33, RFC6-28) — a clause with
five observable consequences and one mapped requirement is not covered.

**"Applicable", defined.** A contract clause's observable consequence is
applicable to a specification when **the capability uses the entity, behavior,
authority boundary, state vocabulary, or interface that consequence
governs**. A reviewer applies this test consequence by consequence against the
specification's CC-SPEC-1 scope statement. A consequence governing something
the capability neither renders, stores, transitions, queries, nor crosses is
not applicable, and saying so is an N/A judgment, not an omission.

**The reviewed-N/A judgment's home, gate, unit, and effect rule are the
contract's, not this clause's.** Here, *reviewed N/A* means a recorded
**owner** judgment, not an author's or reviewer's sign-off. Examples of
confirmed contract modules that state the rule include **RFC1-33, RFC6-28,
RFC7-38, RFC8-32, and RFC9-52**; this is an examples list, not a completeness
claim. The judgment is homed in `decisions/`
(RFC3-15), honored only where its owner-act provenance is verifiable under
**RFC3-16(a)**; where that provenance does not verify, the judgment maps
nothing — the consequence remains unmapped and **renders Unknown, never
covered** (VIS-2). This clause adds only the specification-side
**production obligation**: the specification ships with its coverage
matrix, and every N/A row in that matrix cites the owner judgment's record
in `decisions/`, so the RFC3-16(a) check has something to verify. A matrix
whose N/A rows rest on anything less — the author's or a reviewer's
say-so, a judgment recorded only inside the spec — does not discharge this
clause. An earlier amendment incorrectly made this clause a second, weaker
home for the contract rule. The repair removed that duplicate and retained
only this specification-side production obligation and the definition of
"applicable"; the evidence and review history remain in the amendment
records.

**CC-SPEC-9 — A fresh technical reader can restate it.** A specification is
a normative artifact, so **CC-REV-4** and **VIS-3** apply unmodified: a
reader with no authoring context restates intent and constraints correctly,
and failure is recorded on the artifact's surface. This clause adds nothing
and exists only so that E5's comprehensibility limb has a routed answer;
the obligation is CC-REV-4's.

**CC-SPEC-10 — Lawful adoption is recorded at the exact digest.**

> Lawful adoption under VIS-4 is recorded at the exact digest, and the
> record quotes what was adopted at which digest.
>
> Apply VIS-4's gate at the adoption act. Owner adoption is required unless
> the act can verify **both** delegated-gate conditions —
> *"an accepted adjudication RFC (defining what makes adversarial judgment
> independent, how the ambiguity determination is recorded, and how each
> adopted change stays individually revertable)* ***and*** *the owner's
> explicit doctrine amendment recording that the gate opens; RFC acceptance
> alone never opens it"*. This policy makes no time-sensitive claim that the
> conditions are present or absent; the exact-digest adoption record must show
> the authority it applies.
>
> **One class is always human-gated, gate open or not:** VIS-4 —
> *"spec changes touching security posture, privacy or retention
> obligations, or normative data contracts."* No delegated mechanism ever
> reaches this class.

Until the adoption record exists, the proposed acceptance unit is a candidate.
For a focused change, the accepted capability baseline keeps its prior state;
only the proposed change remains a candidate.

**CC-SPEC-11 — The requirement set covers the declared acceptance unit, and
the coverage is demonstrated.** This clause covers the acceptance unit's own
obligations; CC-SPEC-8 separately covers contract observable consequences.

A specification demonstrates that its requirements cover the acceptance unit
declared under CC-SPEC-1, with a **coverage table** produced with the
specification. The **coverage population** is independently enumerated before
classification; the table author may not define it merely by listing the rows
they chose to include. Membership in the population does not itself place an
obligation in scope.

For **whole-capability acceptance**, enumerate:

1. each obligation in the CC-SPEC-1 capability-scope statement;
2. every stable requirement ID in the proposed specification, including every
   entry marked retired under CC-SPEC-3; and
3. each explicit non-goal.

For **focused-change acceptance**, enumerate:

1. every requirement ID added, modified, or retired by the exact
   baseline-to-proposal difference;
2. each obligation in the change scope and each explicit non-goal; and
3. every unchanged baseline requirement found affected by a stated sweep over
   references, governing-provenance declarations, coverage mappings, and
   defined vocabulary. The sweep records its method and denominator; a
   relationship the method cannot settle enters `Unknown / unresolved`.

Deduplicate the sources into one row per obligation. Each row carries the
stable requirement ID when one exists; otherwise it carries a table-local ID,
its source locator, and the discovery method that put it in the population.

Each obligation in the declared coverage population is placed in
**exactly one** of three sets, which sum to that population:

```text
covered                 included in the acceptance unit; named requirement IDs
                        satisfy it
lawfully out of scope
  / retired             excluded by a named non-goal (CC-SPEC-5), or retired
                        in place under CC-SPEC-3 with the requirement ID and
                        retired entry named
Unknown / unresolved    inclusion or coverage is unresolved; rendered with
                        what would settle it, never
                        silently omitted (VIS-2)
```

The completeness test is **bounded to the independently enumerated coverage
population**. A reviewer who finds a source item absent from that population
raises the omission against CC-SPEC-1's acceptance-unit statement. The table is
**confirmed by a party other than the specification's author**; that explicit
separation is the rule, with no external pattern needed to interpret it. A
fresh engineer reproduces the population from the named baseline and proposed
digests, scope, complete requirement inventory, non-goals, and affected-baseline
sweep, then checks that every member appears in exactly one set — no authoring
context is required.

## What this policy is not

Not a workflow (the th-projects feature-request workflow is referenced
process, never authority); not a format (the specification's adopted format
authority owns the medium); not a review procedure (CC-REV-1/2/4 own review).
One fact, one home.

## Amendment status

The review findings that warrant this proposed amendment, their evidence, and
their excluded routes are recorded in the amendment record linked in the top
banner. This policy surface states the durable rules rather than repeating a
review disposition ledger. The sibling policy's CC-IMPACT-6 remains the rule
for shape changes whose specification amendments cannot move with them.
