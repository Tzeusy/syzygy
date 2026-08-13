# Semantic delta — specification acceptance and shape-to-spec impact, repaired as one model

**Artifacts:**
```text
policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md      CC-SPEC-1…10
policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md          CC-IMPACT-1…7
policy-candidates/CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md new — an offer against CC-REV-2
round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md               new — the blind fixture
round-2026-08g/SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md    new — its golden result
round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md                 superseded
```

**Stable IDs affected:** `CC-SPEC-1`, `CC-SPEC-2`, `CC-SPEC-3`, `CC-SPEC-4`,
`CC-SPEC-6`, `CC-SPEC-8`, `CC-SPEC-9`, `CC-SPEC-10`; `CC-IMPACT-1`,
`CC-IMPACT-2`, `CC-IMPACT-3`, `CC-IMPACT-5`, `CC-IMPACT-6`, `CC-IMPACT-7`.
**No identifier is minted, retired, or renumbered.** `CC-SPEC-5`,
`CC-SPEC-7` and `CC-IMPACT-4` are unchanged.

**Change class:** **Normative** throughout. Someone who complied with the
old CC-SPEC-2 by naming one warrant does not comply now; someone whose
requirement was rejected by the old CC-SPEC-4 for being a prohibition may
now comply. Nothing here is claimed as editorial.

**Author:** authoring session, 2026-08-13. **Adoption belongs to the owner**
(VIS-4) — this delta is the proposal, never the act. Both files remain
candidates; the acts are P-41 and P-42.

**Date:** 2026-08-13

---

## Why this is one delta and not two

The two policies were reviewed together (RD-51) because they define the same
relationship twice. Two of RD-51's four blocking findings are *between* the
files, not inside either:

- **f10** — nothing required a specification's CC-IMPACT-1 declaration to be
  the union of its requirements' CC-SPEC-2 warrants, so a specification
  could satisfy both policies and be invisible to the sweep;
- **f9** — CC-SPEC-2 admitted warrant classes that CC-IMPACT-2 did not
  trigger on, so a requirement could be lawfully warranted by an authority
  whose amendment reached nothing.

Repairing either file alone cannot close either finding. The owner charter
§9 states the requirement plainly — *"one dependency home"* — and its §9.8
sequences one combined review for the same reason. **They are offered
together**: accepting P-41 without P-42, or the reverse, reintroduces both
blocking defects.

---

## Current meaning → proposed meaning, clause by clause

Each row quotes the **exact** current text (from the bytes at commit
`0baf089`) and the exact replacement. A summary here is the first place a
semantic change can hide, so nothing below is summarized.

### CC-SPEC-2 — the warrant rule (charter §9.1; RD-51 f2, f4, f5, f6)

**Current:**

> **CC-SPEC-2 — Every requirement names its lawful higher-level warrant.**
> A requirement traces upward to exactly one of these, **and names which**:
> ```text
> adopted doctrine                 by rule ID
> accepted contract                by clause ID
> recorded owner product decision  by decision identifier or path
> accepted parent specification    by specification and requirement ID
> lawfully admitted user need      by the record that admitted it
> ```

**Proposed:**

> Every requirement names all material governing warrants. One may be
> marked primary for navigation; none may be hidden merely because another
> is more specific.

over a **closed set of six** machine-readable fields — `doctrine[]`,
`contracts[]`, `policies[]`, `decisions[]`, `topology[]`,
`parent_requirements[]` — with four governing rules: all material warrants
rather than one; only accepted/adopted/approved/recorded authorities, so a
**pending** decision is not a warrant; a requirement serving nothing on the
list is a finding; and **this declaration is the only home**, the
specification-level declaration being generated from it.

**Four changes, each separable:**

| # | Change | Warrant |
|---|---|---|
| 1 | "exactly one" → "all material governing warrants", with an optional `primary` marker | charter §9.1. RD-51 f6: "exactly one" was ambiguous between "one warrant exists" (making a genuinely three-warranted requirement *unlawful*) and "name one" (with no tie-break supplied either way) |
| 2 | `policies[]` and `topology[]` added as warrant classes | charter §9.1's closed list. RD-51 f5: the craft cluster is its own authority tier and several approved clauses mandate directly user-observable behaviour; topology was declarable and sweepable under the sibling policy but not warrantable, so the two policies named different authority sets |
| 3 | `lawfully admitted user need` **removed** | charter §9.1: *"Do not include `lawfully admitted user need` until a real admission record class and authority exist."* RD-51 f4, and the sweep re-run this session |
| 4 | Declarations become machine-readable named fields; a pending decision is excluded | charter §9.4 |

**On the removed class, and a disclosed conflict inside the charter.**
Charter §9.1 forbids admitting the class until the mechanism exists; charter
§9.4's field list nonetheless names `admitted_needs[]`. These cannot both be
followed. **Resolved by removing both the class and the field**, on the
ground that removal is the reversible choice: adding a field later is an
amendment, whereas shipping a field with no defined admitting authority
invites its use and re-opens the escape hatch §9.1 closes. `[Inferred]` —
this is the authoring session's reading of two charter sentences, not the
owner's ruling, and it is flagged for the owner rather than settled here.
Defining the admitting authority and record is shape-layer work.

**A false claim withdrawn.** The old rationale read: *"a requirement
implementing a recorded owner decision had no lawful warrant to cite, and
the first specification is full of them: P-31, P-36, P-37, P-38 and P-40 are
all owner rulings that Capability 1 must implement."* `[Observed]` — every
one of the five is **pending**; `PENDING-OWNER-DECISIONS.md` states "every
item below is PENDING. This file decides nothing", and each named packet
opens "This file decides nothing." And "the first specification is full of
them" describes a specification that does not exist. RD-51 f2, blocking. The
sentence is withdrawn and replaced with the true one: these are **queued**
decisions whose rulings, once made, would be citable under `decisions[]`.

### CC-SPEC-4 — requirement forms (charter §9.2; RD-51 f7)

**Current:** four parts required of "a testable observable requirement" —
`initiating condition`, `observable result`, `positive success oracle`,
`falsifying evidence` — closing with *"A requirement whose satisfaction no
evidence could ever contradict is not a requirement."*

**Proposed:** five named forms (`event-response`, `state projection/query`,
`invariant`, `prohibition`, `lifecycle transition`); five obligations on
**every** form (`reachable/producible case`, `observable consequence or
violation`, `effective success/failure oracle`, `oracle independence`,
`concrete falsifying evidence`); and four oracle forms rejected outright
(`tautological`, `unbounded semantic-equivalence`, `unreachable initiating
condition`, `oracle equal to "whatever the implementation computes"`). For
an invariant or a prohibition, the reachable case is the **scope of
quantification, a counterexample schema, and the sweep whose denominator
bounds it**.

**What was wrong at each end**, and both ends were demonstrated by
counterexample rather than asserted:

- **Under-inclusive.** *"No surface renders a green status from evidence
  whose currency bound is undeclared"* — VIS-2's own shape — has no
  initiating condition and no positive success oracle, so the four parts
  rejected it while the clause's own closing sentence admitted it. The
  clause contradicted itself. The hedge "**observable** requirements" does
  not rescue it: either prohibitions are observable requirements and the
  clause wrongly rejected them, or they are not and **no clause stated any
  testability bar for the largest requirement class in the corpus**.
- **Over-inclusive.** A requirement can name all four parts, state its
  oracle as an equality so it survives "without judgment", and still be
  untestable twice over — an initiating condition nobody can produce ("a
  repository whose evidence set has been continuously current for one
  year") and an oracle no procedure decides ("the corpus and the
  implementation are semantically equivalent"). And *"the oracle is: the
  flag equals what the reconciliation engine computes"* is tautological;
  the canonical bar's no-tautologies rule governs **tests**, and a spec's
  oracle is not a test, so nothing forbade it.

The two additions that close the over-inclusive end are the oracle's
**effectiveness** (terminates in bounded effort by a stated procedure) and
its **independence** (not defined by, and not consulting, the implementation
under test).

### CC-SPEC-10 — adoption posture (charter §9.3; RD-51 f12)

**Current:**

> Lawful adoption under VIS-4 is recorded at the exact digest. Under the
> current doctrine state, this means owner adoption.

**Proposed:** the same digest binding, plus **both** limbs the restatement
had dropped, quoted from VIS-4 rather than glossed — the two conjoined
preconditions for opening the delegated gate (*"an accepted adjudication
RFC … **and** the owner's explicit doctrine amendment recording that the
gate opens; RFC acceptance alone never opens it"*), and the always-human-gated
class (*"spec changes touching security posture, privacy or retention
obligations, or normative data contracts"*).

Charter §9.3: *"Do not restate only the convenient half of VIS-4."* RD-51's
word-by-word table found the clause **added** the digest binding (its genuine
contribution, absent from VIS-4), **paraphrased correctly** for today's
state, and **subtracted** exactly the limbs that bind in the future the
restatement was written to anticipate: a reader in a gate-open future,
reading CC-SPEC-10 alone, would conclude the entire specification corpus is
LLM-adoptable at a digest.

### CC-SPEC-1 — the P-40 dependency (RD-51 f3)

**Current:** *"The specification names one coherent capability (per the
granularity rule, P-40)"*.

**Proposed:** the clause states the granularity rule it **proposes**, quoted
in full from P-40's packet, and states that its force is conditional: arm
(a) confirms the clause as written; any other ruling amends it before the
craft act. It adds: **this clause may not be frozen before P-40 is ruled.**

A clause bound to a pending decision changes meaning with no amendment the
moment that decision is ruled differently — the silent re-pointing CC-REV-7
exists to prevent — and it put CC-SPEC-1 in the exact posture CC-SPEC-6
forbids. This is also why charter §9.8 sequences the freeze after P-40.

### CC-SPEC-3, CC-SPEC-6, CC-SPEC-8, CC-SPEC-9 — four smaller repairs

| Clause | Change | Warrant |
|---|---|---|
| CC-SPEC-3 | the **retirement limb** added: a withdrawn requirement's identifier is retired in place with its entry marked retired | the clause extended CC-REV-7 to a new population while dropping half of it, leaving a withdrawn requirement with no lawful disposition |
| CC-SPEC-6 | classification is **contested by default and never finally made by the party authoring the requirement**, following VIS-4's rule for the analogous judgment | RD-51's finding that the trigger was a counterfactual ("*would* settle an open question") with nobody assigned to evaluate it |
| CC-SPEC-8 | the N/A judgment is **confirmed by a party other than the author** (CC-TEST-4 pattern) | RD-51 f15, part |
| CC-SPEC-9 | reduced to a **citation** of CC-REV-4 and VIS-3 | RD-51 f17; CC-REV-3 forbids restating an authoritative rule normatively |

### CC-IMPACT-1 — one dependency home (charter §9.4; RD-51 f10 **blocking**, f16)

**Current:** four spec-level declaration classes of the clause's own —
`capability identities` (*"which capability (or capabilities) it
specifies"*), `doctrine rule IDs`, `contract clause IDs`, `topology
identities` — hand-authored, with nothing tying them to the requirements'
warrants.

**Proposed:** the same six classes CC-SPEC-2 defines, and

> The specification-level declaration is the union of its requirements'
> CC-SPEC-2 declarations, generated — never hand-authored. A declaration
> narrower than that union is a defect, and a second hand-maintained list
> beside it is the duplicate-authority CC-REV-3 forbids.

plus: a specification specifies **one** capability (CC-SPEC-1), reconciling
the singular/plural conflict.

The defect this closes, stated concretely: a specification whose REQ-3 named
`RFC6-19` as its contract warrant while its declaration listed only
`RFC6-18` satisfied both policies and was **invisible to CC-IMPACT-2's
sweep** — the propagation fixture's own headline failure case, reproduced
inside the policy written to catch it. Charter §9.4: *"Do not maintain an
independent hand-authored second list."*

### CC-IMPACT-2 — trigger set (charter §9.5; RD-51 f9 **blocking**)

**Current:** *"When an accepted doctrine rule, contract clause, or topology
identity changes…"* — three classes.

**Proposed:**

> The identities that can trigger a sweep are exactly the identities that
> can warrant a requirement — CC-SPEC-2's six classes, and no others.

Stated as an **identity between two sets**, not as a second enumeration.
This is the point of the repair and not a stylistic choice: two lists drift,
and the drift is silent. Any class that becomes warrantable becomes
sweepable in the same act.

Charter §9.5 lists seven trigger classes including `admitted need`; that
class is absent here for the same reason it is absent from CC-SPEC-2, and by
the same identity it will appear in both or neither.

The defect: a requirement lawfully warranted by a recorded owner decision
was invisible when that decision was amended — **warrantable but
unsweepable**, which is silent staleness by construction.

### CC-IMPACT-3 — method, and a mis-citation (charter §9.5; RD-51 f11, f20)

**Current:** four sets with a denominator, `explicitly unaffected` requiring
only "the reason"; justified by the claim that the denominator discipline
*"lives only in operating procedure"* and mis-attributing the defect to
CC-IMPACT-2.

**Proposed:** `explicitly unaffected` requires **the reason and the method**,
and `undecidable` requires **what would settle it**. Added:

> "Does not declare the changed identity" is an *observation*; if
> declaration-matching is the whole method, the sweep says so, and
> everything that method cannot decide routes to `undecidable` under
> CC-IMPACT-4 rather than to `explicitly unaffected`.

And the denominator discipline is **cited to CC-KNOW-16** rather than
claimed as a new home.

Two defects, both self-inflicted: the clause named **CC-IMPACT-2** as the
defect it fixes, contradicting its own file's table; and it justified itself
by a **claim of absence made with no sweep** — CC-KNOW-16, in the same
directory, already carried the rule. RD-51 f20's failure mode is what the
method limb closes: a **true reason producing a wrong answer**, carrying a
denominator and full compliance. VIS-2's violation example is "a stale view
silently green"; the unrepaired clause could produce a stale view
**confidently** green.

### CC-IMPACT-5 — the sweep's own actor (RD-51's G section)

**Added:** *"The sweep itself has an actor: the shape change's author
performs it, and a party other than that author confirms it is adequate."*

The fixture's words were *"this step has no owner in any authority today."*
After the unrepaired CC-IMPACT-1…7, detection had acquired a *requirement*
and still had **no owner** — CC-IMPACT-2's "the change carries a sweep" is
passive voice, and CC-IMPACT-5 assigned an actor to *amendments*, not to
detection. E6's detection limb is what this closes.

### CC-IMPACT-6 — the exception (charter §9.6; RD-51 f1 **blocking**)

**Current:** *"This rule therefore adds exactly one lawful alternative … an
affected specification may lag its shape change only under a recorded
exception that names the specification, the reason, the owning actor, and
the condition that ends it."*

**Proposed:** the clause creates **no** alternative. CC-REV-2's merge
invariant governs unmodified; a lagging specification is lawful only if
**CC-REV-2 is itself amended**, and that amendment is offered separately as
`CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md` (queue row **P-44**),
carrying charter §9.6's five elements — affected specification, reason,
owner, end condition, **visible contradiction/Unknown interim state** — plus
a **confirmer distinct from the change's author**. Until that act, no lawful
lag exists.

Charter §9.6 gives two directions — *"do not create a casual exception that
conflicts with CC-REV-2"* and *"any lagging specification requires a lawful
owner-visible exception mechanism owned by craft policy"* — and they have
exactly one consistent implementation: amend CC-REV-2.

Three independent problems with the old form, all RD-51 f1's:

1. **It weakened an owner-approved clause by writing a new clause beside it
   rather than amending it.** Behavioral specs are the **first** population
   CC-REV-2 names. Both clauses would sit in craft-cluster tier 2, where the
   cluster's precedence rule resolves *cross-tier* weakening only — so two
   clauses of one approved cluster would give opposite answers to "may this
   merge land?" with nothing to arbitrate.
2. **It created a second home for the merge invariant**, which CC-REV-3
   forbids.
3. **The exception had no confirmer.** Four fields and no second party: the
   author of the shape change writes their own exception to CC-REV-2 and
   merges. Compare the cluster's two approved exception mechanisms —
   CC-TEST-1 and CC-TEST-4 — both of which name one.

A fourth fact worth keeping: the predecessor fixture records this same limb
as previously **invented and withdrawn** for want of any craft clause
containing it, and the candidate reinstated it. Creating a rule by act is
lawful; creating one that overrides a different approved clause without
amending it is not.

**The fifth element is genuinely new.** The old four fields did not include
the interim contradiction/Unknown state. Without it, a lagging specification
is exactly the silent staleness CC-REV-2 forbids; with it, the lag is
visible on the specification's own surface, which is what makes arm (a)
arguable at all.

### CC-IMPACT-7 — the blind exercise (charter §9.7; RD-51 f13, f8)

**Current:** *"the reviewer derives the affected, unaffected and undecidable
sets without reading the answer, and the comparison is recorded."*

**Proposed:** the fixture is named **by path and sha256**; the administrator
is **fresh-context per CC-REV-1**; the **pass criterion is the answer key's**
and is quoted there; every divergence carries a recorded disposition
(CC-REV-6); and the consequence of failure is stated — **the path is not
relied on until a passing run exists**, so a recorded failing run satisfies
the record obligation and not the clause.

The old clause required only that the comparison be recorded, so **a blind
run that missed every impacted specification, recorded honestly, satisfied
it in full**. It named no fixture, no administrator standard, and no
consequence. And the only fixture then in the corpus was itself defective
(RD-51 f8): its golden ANSWER graded *"or a recorded exception"* as correct
while its own governing step 4 said CC-REV-2 admits no such limb — so a
reviewer answering correctly from the governing description was marked
divergent.

---

## The new fixture

`SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` supersedes
`../round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`. Charter §9.7's
five required properties, and where each lives in it:

| Required property | In fixture 2 |
|---|---|
| one shape change affects several requirements | `CC-PROV-5`'s amendment affects three requirements across **two** specifications |
| one spec is unaffected | SPEC-ENTRY, wholly |
| one relationship is undecidable | FAC-3 — impacted at one remove through `RFC6-18`'s composition rule, which the sweep cannot settle without a contract reading it does not own |
| one owner decision changes | `OD-2`, a **mock** decision — no real owner decision has been ruled, and writing a pending identifier into a "was amended" scenario would state a falsehood inside a governance artifact |
| one policy changes | `CC-PROV-5` |
| the reviewer derives the result without reading the answer | the answer lives in a **separate file**, so blindness is structural rather than an honour system |
| denominator and all four sets required | the task states it, and the pass criterion fails a run without it |

**Population 16 requirements across 5 specifications; golden affected 6,
undecidable 1, explicitly unaffected 9.** The fixture is built so that a
sweep matching contract clause IDs only misses **4 of the 6** affected
requirements — the warranted-but-unsweepable class of f9, made measurable.

---

## What explicitly does NOT change

Named because "I only touched X" is the most common false claim in normative
editing:

- **CC-SPEC-5, CC-SPEC-7, CC-IMPACT-4** — byte-identical in substance; only
  CC-SPEC-5 gains the word "cited, not restated" about VIS-2/CC-REV-5.
- **No identifier is minted, retired, or renumbered.** CC-SPEC-1…10 and
  CC-IMPACT-1…7 are the same identifiers over the same subjects, so every
  existing citation still resolves. No new clause is added to either file —
  in particular, **no clause is added for RD-51 f14** (see the open list
  below).
- **Neither file's candidate status.** Both bind nothing. The acts are P-41
  and P-42, unperformed.
- **CC-REV-2 itself.** It is quoted, and an amendment to it is *offered*.
  Nothing in this delta changes an approved clause.
- **`openspec/` is not created, implied, or authorized.** Every
  specification either policy speaks of is future.
- **The launch gate**, its schema, its validator, and its renderer. E5 and
  E6 remain open questions the gate asks; nothing here answers them by act.

---

## Warrant

Owner charter §9 (§9.1–§9.8), and RD-51, raw at
`../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`, verdict
`REVISE`.

**On citing the charter.** RD-51 f18 recorded that the three previous
amendment notes cited "owner charter §9", a document absent from every
commit and therefore unreadable from a clone. Those three citations are
replaced: every amendment note in both files now cites **this delta** and
the **RD-51 finding number**, both of which are tracked. The charter remains
the owner's instruction and remains untracked; this file is the tracked
record of what it directed.

## Evidence or decision basis

`[Observed]` — RD-51's bytes at
`../round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md`; the two
candidates' bytes at commit `0baf089`; CC-REV-2, CC-REV-3, CC-REV-4,
CC-REV-7, CC-TEST-4 and the cluster precedence rule, read in
`policies/craft-and-care/`; VIS-2, VIS-3, VIS-4 read in
`doctrine/vision.md`; P-40's packet at
`decisions/SPECIFICATION-GRANULARITY-DECISION.md`.

`[Observed]` — the `user need` sweep, re-run in this session, both methods:
371 files (`.syzygy/**`, `*.md|*.yaml|*.json`) and 784 files (repo-wide,
six extensions), hits confined to the clause's own discussion, the review
that found it, and one untracked file. **No admission record class exists.**

`[Inferred]` — every claim about how these clauses behave in use. **No
specification exists**, so the counterexamples are constructed and the mock
corpus is a fixture. This is the same limit RD-51 disclosed, and it does not
weaken: a clause that fails on a constructed counterexample fails.

## Terms introduced / retired

`admitted user need` is **retired from the warrant vocabulary** without ever
having had a defining record. No durable term is introduced: the six field
names are the existing authority classes in machine-readable form.

## Downstream impact

**Method** — Python `re` (ugrep's `[^]]` classes silently match nothing;
verification rule 1), over `.md|.py|.json|.yaml|.yml|.txt`, run twice: once
before the edits, to find what could break, and once **after** them, so the
figures published here are the ones a reader can reproduce at this commit.

| Sweep | Scope | At this commit |
|---|---|---|
| `CC-(SPEC\|IMPACT)-\d+` | working tree, `_bootstrap/` and `.git/` excluded | 422 files scanned, **30** with citations |
| `CC-REV-2\b` | working tree, `_bootstrap/` **included** | 786 files scanned, **40** with hits, **130** occurrences |

The counts alone would be uninterpretable — the sweeps grew because this
change adds files that cite the clauses it amends. So the load-bearing
measurement is the **set difference against `HEAD` (`0baf089`)**, computed
file-by-file rather than by subtracting totals:

`[Observed]` **22 files cited `CC-SPEC-*`/`CC-IMPACT-*` at `0baf089`; 30 do
now; 8 gained, 0 lost.** Enumerated:

```text
new in this change   SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md
                     CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md
                     SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md
                     SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2-ANSWER-KEY.md
                     reviews/RD-59-blind-propagation-RAW.md
edited in this change round-2026-08g/reviews/DISPOSITION-REGISTER.md  (RD-51 section)
                     round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md
                                                        (the supersession banner)
not part of the repo the untracked owner charter at the root
```

**No pre-existing citation was invalidated, and none was lost.** The two
pre-existing files that gained citations gained them from this change's own
prose, not from a moved obligation. Both enumerations were read, not counted
only.

`[Observed]` **No citation is invalidated.** Every citation outside the two
policies is either a **range** (`CC-SPEC-1…10`, `CC-IMPACT-1…7`) or points
at `CC-SPEC-8`, whose subject — the clause-to-requirement coverage matrix —
is unchanged. The load-bearing dependants, each checked individually:

| Artifact | Citation | Still true? |
|---|---|---|
| `PROJECT-STATUS.md` | both ranges, "Candidate — own craft act" | yes |
| `TASK-ROUTER.md` | both ranges, "CANDIDATE craft policy, in force from neither" | yes — regenerate and `--check` |
| `05-CONTRACT-INDEX.yaml` | `CC-SPEC-1`, `CC-SPEC-10` via `INSTALL-RECORD.md`'s rule_ids | yes — regenerate and `--check` |
| `SURFACE-CLAUSE-ROUTING-MATRIX.md` | `CC-SPEC-8` owns RFC6-28's coverage-matrix deliverable | yes — CC-SPEC-8's subject is unchanged; its **circular citation** with this matrix remains an open finding (f15) |
| `candidates/README.md`, `INSTALL-RECORD.md` | the `CC-SPEC-1…10` range | yes |
| `decisions/SPECIFICATION-ACCEPTANCE-DECISION.md` (P-41 packet) | the range, and "rule P-40 before this act" | yes — and the packet's sequencing claim is now *stated by the clause itself* |
| `decisions/PENDING-OWNER-DECISIONS.md` | P-41, P-42 rows | updated in this change: both rows record the amendment, and **P-44 is added** |

## Migration / supersession plan

Same logical change (CC-REV-2 applied to this change itself):

1. both candidates amended, and the delta written — this file;
2. the CC-REV-2 amendment **offered**, not applied, with its queue row;
3. fixture 2 and its answer key created; **fixture 1 banner-marked
   superseded** in the same change, so no reading path reaches it as current;
4. `PENDING-OWNER-DECISIONS.md`: P-44 added; P-41 and P-42 rows record that
   the candidates were amended and are offered jointly;
5. `PROJECT-STATUS.md` and the round's disposition register updated;
6. generated views regenerated and `--check`ed after the source edits, never
   in anticipation of them.

**Nothing here is digest-bound by an act**, so no re-sealing is required.
Fixture 2 **is** digest-bound by CC-IMPACT-7: editing it voids every run
bound to the old digest, so it is superseded rather than edited.

## Review

**Required class:** CC-REV-1 and CC-REV-4 — normative amendment to two
candidate craft rule sets, one of which now proposes an amendment to an
approved clause.

**Reviewer:** must not have authored this delta or shared its session.

**Verdict:** `[Unknown]` — **no review has been run against these bytes.**
Charter §9.8 sequences one combined fresh-context review, **after P-40 is
ruled**, and P-40 is not ruled. What exists today is a repair pass by the
session that read RD-51's verdict, which is the weakest possible evidence
about its own correctness. The freeze §9.8 asks for has therefore **not**
happened and cannot happen in this session; these bytes may still move.

---

## Open findings NOT repaired here

RD-51 raised 20 findings. Recorded because a delta that lists only what it
fixed is the same defect as a sweep that reports only its numerator.

| Finding | Severity | Why it is open |
|---|---|---|
| **f14** | material | **No clause tests a specification for completeness against its capability**, so launch-gate E5's "complete" limb is unclosed. The fix is a new clause — and charter §9 does not direct one. Adding an unrequested clause to a candidate enlarges what the owner must approve at P-41, which is the owner's call. Recorded on the policy's own surface and here |
| **f15** (part) | material | "applicable" (CC-SPEC-8) is undefined, and "the corpus's reviewed-N/A rule" carries no identifier while the routing matrix routes the deliverable back to CC-SPEC-8 — each names the other as owner. The confirmer half is repaired. Naming the rule requires reading candidate RFC modules and quoting a defined clause (verification rule 8); defining "applicable" is a rule this session may not invent |
| **f13** (part) | material | CC-IMPACT-7 now names a fixture, a standard, a pass criterion and a consequence. It still does not say **who selects** the administrator |
| **G** | — | **"consumes its vocabulary" remains undefined.** CC-IMPACT-4 keeps it honest — an undecidable case is `Unknown`, never `unaffected` — but the term's undefinedness still decides real cases, and fixture 2's FAC-3 is one. Recorded as `[Unknown]` on the policy's own surface |
| **f19** | minor | epistemic labels: partially repaired. The substantive claims in the amendment notes and the rationale carry labels; the "why each rule is here" table does not |
