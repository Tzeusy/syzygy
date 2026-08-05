# RC-10 — Final confirming review of the foundational contract package

**Reviewer role:** independent confirming reviewer, no prior involvement in this
work. Fresh context. Did not read any authoring conversation and did not read
`_bootstrap/**`.

**Subject:** the 32 active contract modules under
`.syzygy/governance/contracts/candidates/rfcs/`, at the manifest digest offered
as act 1's argument.

**Repository state as reviewed:** commit `864718c04b905e4bc0a11a32dd46498baffa9b65`.

**Question answered:** is this package, at its exact current manifest digest,
fit to be offered to the owner for acceptance act 1?

---

# VERDICT

VERDICT: REVISE

---

## 0. A condition of the review that the owner must know about first

**[Observed] The repository was being written by another session while this
review ran.** The working tree was clean at review start
(`git status --porcelain` → empty). Within the next eleven minutes the
following files changed underneath me, none of them by my hand:

```
18:36:41  SURFACE-CLAUSE-ROUTING-MATRIX.md
18:36:41  round-2026-08b/matrix-parts/RFC-0007-0011.md
18:36:41  round-2026-08b/matrix-parts/RFC-0008-0010.md
18:36:48  .syzygy/governance/policies/craft-and-care/README.md
18:37:34  round-2026-08b/PUBLIC-CLONE-VERIFICATION-REPORT.md   (new, untracked)
later     round-2026-08/FINAL-HUMAN-CLARITY-REVIEW.md
later     round-2026-08/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md
later     round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md
later     round-2026-08/ROUND-DISPOSITIONS.md
later     06-CONTEXT-LOAD-MAP.md
later     FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md
later     scripts/check_governance.py
```

Two consequences the owner should weigh:

1. **A concurrent session is currently editing the acceptance record that owns
   act 1's phrase and argument, and the checker that verifies it.** An act
   performed against a document in that state is an act against a moving
   target. [Observed]
2. **All substantive verification below was therefore performed against a
   pristine export of commit `864718c`**
   (`git archive 864718c` into a scratch directory), not against the live
   working tree. Where I report a figure, it is the committed figure.
   [Observed]

**[Observed] The act-1 digest set itself was not touched by that session.** At
18:47:41 I re-ran the manifest over the live working tree: all 32 modules still
match their manifest digests and the manifest still hashes to `718fe095…`. So
the bytes under act 1 are, as of this writing, intact — but the surrounding
offering is not stable.

### Disclosure of my own one write to the repository

**[Observed] I made exactly one unintended modification and reverted it.** I
invoked `scripts/build_contract_index.py` without `--check`; that script's
default mode **writes** `05-CONTRACT-INDEX.yaml`. I restored the file with
`git checkout --` and confirmed it is byte-identical to the committed version
(`git diff --stat` on that path is empty). I made no other change. The
`RC-10-final-confirming-RAW.md` file you are reading is the only file I created.

I flag the script's ergonomics as a minor hazard: a read-only-looking
verification tool whose default argument-less invocation mutates a
digest-adjacent artifact is a foot-gun in a repository whose whole discipline is
"do not let an artifact move after a record binds it." [Inferred]

---

## 1. Establishing the bytes

**[Observed] The digest I actually reviewed:**

```
718fe095192a415fe7300b039e887b4d286bbb3d06b45e0f823cfb1ce6d4724f
```

Recomputed by the manifest's own stated recipe
(`ACTIVE-CONTRACT-MANIFEST.txt:2`):

| Check | Result | Denominator |
|---|---|---|
| Files under `rfcs/` | 32 `.md` files | 32 of 32 enumerated |
| Per-module sha256 recomputed vs manifest body | **exact match, zero differences** | **32 of 32** |
| `sha256sum ACTIVE-CONTRACT-MANIFEST.txt` | `718fe095…4724f` | 1 of 1 |
| Matches `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:17` §1 row 1 | **yes** | 1 of 1 |
| Same, recomputed on the pristine `864718c` export | **identical** | 32 of 32 |
| Same, re-checked on the live tree at 18:47 | **identical** | 32 of 32 |

**[Observed]** `check_governance.py` CG-7a independently confirms: "manifest
digests valid — 32 entries examined, 0 findings — manifest sha256 718fe095…";
CG-7b "act-1 argument matches the manifest — 1 argument examined, 0 findings".

**Finding: none. The bytes are established. Act 1's argument is correct for the
corpus it names.** This is the strongest part of the package and I could not
break it.

---

## 2. The six clauses no reviewer has read

Scope: RFC10-17 … RFC10-22 in
`rfcs/RFC-0010-mission-control-autonomy.md:367-464`, plus the in-place
amendments to RFC10-6 (`:158-166`), RFC10-7 (`:194-219`) and RFC10-11
(`:295-298`).

### 2.1 Provenance — a material fact the closure report understates

**[Observed] The six clauses are, very nearly verbatim, RC-7's own proposed
clause text.** I diffed each adopted clause against the proposal in
`reviews/RC-7-mission-safety-RAW.md`:

| Clause | Source | Deviation from RC-7's proposal |
|---|---|---|
| RFC10-7 `propose-only` | RC-7:1039-1052 | identical + `(RFC10-17)` inserted + one closing sentence ("a cap binding to an undefined term is not a cap") |
| RFC10-7 grants/obligations | RC-7:1168-1177 | identical in substance + an explanatory parenthetical |
| RFC10-19 | RC-7:1133-1152 | identical but for word order in one clause reference |
| RFC10-20 | RC-7:1189-1205 | identical **except** RC-7's citation `(RFC5-11's acts-versus-claims rule)` was **dropped** |
| RFC10-21 | RC-7:1218-1236 | identical |

**[Inferred] This materially lowers the risk of the round's headline residual.**
`MISSION-SAFETY-CLOSURE-REPORT.md:73-76` says "The six new clauses have been
read by no reviewer. They were written in response to RC-7 and RC-7 has not
seen them." That is true as stated but understates the position in the owner's
favour: RC-7 did not merely prompt them, it *drafted* them. Text authored by an
adversarial reviewer and adopted unaltered is not the same risk as text authored
by the party the reviewer was attacking.

**[Observed] But the round did the opposite of what RC-7 instructed.**
`RC-7:1022-1026`: "Proposed text is drafted in the corpus's voice for insertion
**by owner act after act 1**, since RFC-0010 is inside the act-1 frozen digest
set and editing it now churns the manifest." The lead inserted the text
*before* act 1, churning the manifest twice. I judge the outcome better than the
instruction (the owner now binds corrected text rather than knowingly defective
text), but **the deviation from explicit reviewer guidance is nowhere recorded.**
[Inferred] Minor.

**[Observed] RFC10-20 silently dropped RC-7's `RFC5-11` citation.** RC-7 grounded
"all immediate at the act" in RFC5-11's acts-versus-claims rule; the adopted
`:421` reads "all immediate at the act:" with no citation. The clause is
weaker-grounded than proposed and no delta records the removal.

### 2.2 Are they well-formed obligations?

**[Observed] Yes, structurally.** Each of RFC10-17…22 states a subject, a
modal obligation, a defined failure disposition, and a named consequence. Each
carries at least one violation case in §4 (`:502-517`, cases 8–13, one per new
clause — 6 of 6 covered). Front matter `clauses: "RFC10-1..RFC10-22"` (`:5`)
matches the closing self-statement (`:588`) and matches my independent count of
22 defined RFC10 clauses with no gaps.

**[Observed] Numbering discipline held.** No clause was renumbered or retired;
RFC10-1…16 retain their identifiers; the amendment log (`:545-557`) records the
three in-place amendments. `RFC10-16` (`:473`) was correctly extended to cover
the new clauses — "including everything RFC10-17..22 requires of a runtime" —
so the phase rule reaches them and none of them can be used to schedule
implementation.

**[Observed] Citations resolve.** I swept every `RFCn-m` citation in all 32
modules against every bold-defined clause id: **0 cited-but-never-defined, over
the full corpus.** The new clauses' outbound citations (RFC2-19, RFC2-23,
RFC2-25, RFC3-16(a), RFC5-14, RFC5-15, RFC5-21, RFC5-22, RFC8-19, RFC10-4/5/7/
8/9/10/11/13/15/17/19) all resolve.

### 2.3 Consistency with RFC10-1..16 — one real contradiction

**FINDING RC10-A [Observed] — `RFC10-18` calls `blocked` a termination;
`RFC10-5` defines `blocked` as non-terminal.**

- `RFC-0010:131` — RFC10-5's lifecycle: `running → completed | failed | cancelled | expired` are the terminals.
- `RFC-0010:130` — `running → blocked (→ running on unblock)`: `blocked` is explicitly a *resumable, non-terminal* state.
- `RFC-0010:394-395` — RFC10-18: "the mission **terminates as `blocked`** with an Attention Item, never as `completed`."

A state the lifecycle defines as resumable is used by a new clause as a terminal
outcome. RFC10-5 also requires "every terminal state is recorded with its
reason" (`:139`) — which reason vocabulary applies to a `blocked` "termination"
is undefined.

**This is not cosmetic, because of RC10-B.**

**FINDING RC10-B [Observed] — the correction plane's recovery duties do not fire
on the state RFC10-18 routes failures into.**

`RFC10-19:407-411` attaches every compensation and enumeration duty to a closed
trigger set: "Where a mission enters `failed`, `cancelled`, or `expired` with
effects already applied…". `blocked` is not in that set. `RFC10-19:413-414`
says only that pausing/blocking "discharges no obligation" — it does not
*create* one.

**Constructed scenario I could not find a clause to stop:** a mission with
applied effects reaches its completion predicate; no independent establisher
exists for its objective class (RFC10-18's own named case, e.g. wherever RFC2-19
leaves reconciliation uncomputed); RFC10-18 routes it to `blocked`. Result:
applied effects are never enumerated, no compensating action is owed, no
irreversibility Attention Item is minted, and the mission has no terminal reason
because it never reached a terminal state. The correction plane is bypassed —
not by widening anything, but by taking the exit the correction plane's own new
clause prescribes.

**[Observed] This is aggravated by a residual RC-7 itself recorded and the
closure report deliberately did not restate.** `RC-7:1371` — non-blocking
finding **F13, "Escalation-sourced `blocked` states have no human-exit rule."**
RFC10-5's human-resolution requirement (`:140-142`) is scoped to blocks "where
the block arose under RFC10-8 or RFC10-11" — an RFC10-18-sourced block arises
under neither, so even that exit rule does not reach it.

F13 was correctly judged non-blocking when `blocked` carried little weight. The
six new clauses substantially increased the load on `blocked`, and nothing
re-examined F13 against them. `MISSION-SAFETY-CLOSURE-REPORT.md:84-85` disposes
of the whole non-blocking class in one line — "The residual seams RC-7 recorded
as non-blocking are not restated here" — which is honest but is exactly how this
interaction escaped.

### 2.4 Adversarial scenarios against each new clause

I attempted to construct, for each clause, a scenario it fails to constrain.

**RFC10-17 (budget reservation) — FINDING RC10-C [Inferred], asymmetric
independence.** The clause defines `spent` as "measured consumption" (`:370`)
but never says *by whom*, and imposes no independence requirement on the
measurer. RFC10-18, written in the same pass, felt the need to state exactly
that requirement for completion ("never by the principal that performed the
work"). A fleet that self-reports `spent` low is not reached by RFC10-17's text.
Partial mitigation, and it is good: `:377-379` treats Unknown spend as the bound
being reached, so *absent* telemetry fails closed. The gap is *false* telemetry,
not missing telemetry. Also unconstrained: who declares the "declared maximum
cost" (`:372`) that sizes the reservation — chronic under-declaration is
recorded as overrun after the fact but never prevented. I rate this the weakest
of the six clauses. Note the flooding follow-on is contained: overrun Attention
Items are bounded by RFC10-22, which pauses the mission.

**RFC10-18 (completion adjudication) — holds against my attacks except RC10-A/B.**
"never by a principal that principal routed" (`:390-391`) closes the delegation-
laundering route I tried first. Requiring `gate-backed` evidence and defaulting
an unstated tier to `gate-backed` (`:396`) closes the tier-shopping route.

**RFC10-19 (reversibility) — FINDING RC10-D [Observed], compensation failure has
no escalation.** `:409-410`: "every compensatable effect's compensating action
is attempted and its outcome recorded as evidence." A *failed* compensation is
therefore recorded and nothing more. It is not reclassified as irreversible, and
the "single Attention Item naming what cannot be undone" (`:410-411`) is scoped
only to effects *declared* irreversible up front. Scenario: an effect declared
`compensatable`; the compensating action fails; the mission terminates; the
owner is never told that a supposedly-undoable effect stands. Under the
propose-only cap this is inert today; it becomes live the moment the cap lifts.

**RFC10-20 (stop) — FINDING RC10-E [Observed], stop does not reach child
missions.** `:423-424` scopes (b) to "every run Syzygy launched **under the
mission**". RFC10-8 (`:230-239`) establishes child missions as first-class
reservations against the parent. A child's runs are launched under the *child*.
No clause propagates a parent stop to its children. Scenario: parent mission
grants decomposition, mints three children, owner stops the parent — dispatch
under the parent ceases, and the children's runs continue. This is precisely
RC-7's F6 escape, reproduced one level up in the very structure RFC10-8 created.
RFC10-8 debits child grants from the parent's budget but says nothing about stop.

**FINDING RC10-F [Observed], synchronous stop has no failure path.** `:428-430`:
"an undeclared latency means stop is synchronous — the act does not return until
(a) and (b) hold." If (b) cannot be achieved — a run that will not die — the
clause specifies no timeout, no failure disposition, and no Attention Item. The
default (undeclared latency) is the deadlocking one. RC-7's F6 asked for a
latency *bound*; the adopted text supplies a bound only when declared, and an
unbounded wait when not.

**RFC10-21 (cross-project consent) — FINDING RC10-G [Inferred], the rule keys on
mission scope, the harm keys on content provenance.** `:435-437` applies to a
composite "assembled under a mission **spanning more than one project**". The
predicate is a property of the mission's declared target, not of the content
embedded. Scenario: declare the mission targeting project A only; the envelope
grants paths that include a checkout of B; the composite embeds B's content. By
its own predicate RFC10-21 does not engage. RFC5-15's per-project check may
still catch it — I could not establish that it does for a composite that names
A as its project, which is the exact hole RC-7's F7 described (`RC-7:1210-1216`).
The clause closes the multi-project-mission case and leaves the
single-project-mission-with-foreign-content case open.

**RFC10-22 (attention bounds) — FINDING RC10-H [Observed], the bound can suppress
notice of itself.** `:453-457`: "an undeclared maximum means one outstanding
item"; "On reaching either bound the mission pauses rather than enqueueing
further items." Scenario at the default: the mission mints item #1; it then hits
a condition requiring escalation; it reaches the bound and pauses; it may not
enqueue the item that would tell the owner it paused. The safe behaviour (pause)
is correct; the notification of that behaviour is blocked by the same sentence.
No carve-out exists for a bound-reached or state-change item.

**[Inferred] Aggregate attention across envelopes is unbounded.** `:453-455`
bounds outstanding items per envelope. Nothing bounds the sum across many
envelopes. Mitigated in practice because each envelope needs an owner act
(RFC10-9), so this is a low-severity residual, not an exploit.

### 2.5 Contradiction with RFC-0003 / 0005 / 0008 / 0011

**[Observed] I found no contradiction with these four contracts.** Specifically
checked and consistent:

| New clause's claim | Target | Result |
|---|---|---|
| RFC10-18 requires `gate-backed` tier | RFC2-25 tier registry, `RFC-0002/rendering-vocabularies.md` | tier exists; "only `gate-backed` Observed evidence may support a positive status claim" — RFC10-18 is consistent and stricter |
| RFC10-17 Unknown ≠ zero | RFC2-23 / RFC8-19, and RFC2-24's "absence is never zero" | consistent; RFC10-17 applies the corpus rule rather than restating a new one |
| RFC10-19 destructive class not inherited | RFC5-22 standing approval | RFC10-19 narrows RFC5-22 for missions; narrowing, not contradiction |
| RFC10-20 kill switch | RFC5-21 isolation-class kill switch | RFC10-20 routes a mission stop to an existing RFC5-21 obligation; this is the routing RC-7 said was missing |
| RFC10-21 choke point | RFC5-15 single choke point | consistent; RFC10-21 adds a conjunctive project condition at the same point |
| RFC10-14 act record home | RFC3-16(b) item 3 | consistent |

**[Observed] One dependency-graph observation, not a defect.** RFC-0010's
front matter (`:8`) does not list RFC-0011, while `:540-541` integrates with it.
RFC-0011 declares `depends_on: [… RFC-0010]`. The one-directional declaration
keeps the graph acyclic and is consistent with the round's stated rule that
`depends_on` is a load obligation, not a relation register. The
`DEPENDENCY-CLOSURE-REPORT.md:110-137` bounded-imprecision table records this
class explicitly. Correct handling.

### 2.6 Does the closure report's claim match the clause text?

**This is where I found the most material problem in the round.**

`MISSION-SAFETY-CLOSURE-REPORT.md:44-45` claims "**Nine of eleven closed by
clause text.**" I checked each of the nine disposition rows against the adopted
text. **Four of the nine rows describe something the clause does not say.**

**FINDING RC10-I [Observed] — F1's row states a carve-out that exists in no
clause.**

`MISSION-SAFETY-CLOSURE-REPORT.md:32` — "RFC10-7 now defines `propose-only` as
*no effect outside `.syzygy/**` and `openspec/**` **that is not itself an
owner-signed dispatch of one work item***".

Sweep result: **`owner-signed` occurs 0 times in `RFC-0010-mission-control-autonomy.md`.**
It occurs at `RC-7:863` and `RC-7:873` — inside RC-7 §10.5, "The V0 autonomy
ceiling, stated concretely", a **separate and unadopted** recommendation. The
adopted RFC10-7 definition (`:205-219`) has **no carve-out at all**: "It may
**not** cause any effect outside those two namespaces."

The report describes a *more permissive* clause than was written. The text is
safe; the owner-facing description of it is wrong, and it was assembled by
quoting the wrong RC-7 section.

**FINDING RC10-J [Observed] — F4's row claims a rule RFC10-19 does not contain.**
`:35` — "RFC10-19 … **defines the relationship between completed and failed
sibling work**." Sweep: `sibling work` occurs **0 times** in RFC-0010.
RFC10-19 contains no sibling-work rule. (RFC10-8 and RFC10-17 have a sibling
*budget* invariant; that is a different subject.)

**FINDING RC10-K [Observed] — F6's row claims a consistency guarantee that does
not exist.** `:37` — "RFC10-20 … **states the consistency claim**." Sweep:
`consistency` occurs **0 times** in RFC-0010; `atomic` occurs once, at `:548`,
inside the amendment log listing it as a term that *used to be* zero-occurrence.
RC-7's F6 had three limbs — no termination of running work, no latency bound,
no consistency guarantee. RC-7's own proposed text closes the first two and
supplies checkpointing for the third, not a consistency claim. **The third limb
is not closed, and the report says it is.** F6 is one of the three seams the
same report flags as live "under the cap, on day one" (`:80-83`).

**FINDING RC10-L [Observed] — F7's row labels the budget rule as the consent
rule.** `:38` — "RFC10-21 supplies the selection rule for cross-project consent:
**the lesser binds**." In RFC10-21, "the lesser binds" (`:446`) governs
*budgets*. The consent rule (`:435-443`) is conjunctive and stricter — *every*
embedded project's consent, failing closed. Calling a conjunctive
all-must-consent rule "the lesser binds" describes a selection among consents,
which is what RC-7 said must **not** happen. The clause is right; the one-line
summary of the round's self-described "highest-consequence leak" is wrong.

**[Observed] Mitigating.** The report is banner-marked non-authoritative and
states "Where either disagrees with this file, this file is wrong" (`:3-6`). So
the errors are formally harmless. **[Inferred] But they are not practically
harmless**: this table is the artifact through which the owner is invited to
understand what act 1 newly binds, and `FINAL-OWNER-ACCEPTANCE-RECORD.md:51-52`
routes the owner to it for exactly that purpose. A disclaimer does not make a
misdescription informative.

**Score for §2.6: of nine rows claimed "closed by clause text", 5 are accurate
(F2, F3, F5, F8, F9), 3 misdescribe the closure (F1, F4, F7), and 1 overclaims
a seam that is not closed (F6).** F10 (owner ruling, open by design) and F11
(record correction) are both accurately dispositioned — I independently confirm
F10 is tracked as P-24 at `PENDING-OWNER-DECISIONS.md:72`.

---

## 3. Re-testing the dependency graph

All extraction below used Python `re`, never `grep`.

### 3.1 The four refuted Group B edges — verified reverted, 4 of 4

`DEPENDENCY-CLOSURE-REPORT.md:158-163` names four edges reverted after RC-4.

| Reverted edge | Current front matter | Verdict |
|---|---|---|
| `RFC-0006` → `RFC-0003` | `RFC-0006-…drawer.md:8` → `depends_on: [RFC-0001, RFC-0002]` | **absent — reverted** |
| `RFC-0008` → `RFC-0009` | all 4 RFC-0008 modules; none lists RFC-0009 | **absent — reverted (4/4 modules)** |
| `RFC-0010` → `RFC-0009` | `RFC-0010-…autonomy.md:8` → `[RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008]` | **absent — reverted** |
| `RFC-0011` → `RFC-0009` | `RFC-0011-context-compiler.md` → `[…, RFC-0008, RFC-0010]` | **absent — reverted** |

**4 of 4 confirmed reverted. [Observed]**

**[Observed] The surviving 7 Group B edges are all present.** I checked each
module row the report says received an edge: **12 of 12 module-level rows carry
their edge.** So "Group B is therefore 7 edges, not 11"
(`DEPENDENCY-CLOSURE-REPORT.md:170`) is exactly reproduced.

**[Observed] `provides_to` removal verified: 0 of 32 modules retain the key.**
The asymmetry class is genuinely unrepresentable, as claimed.

### 3.2 README `depends_on` = union of members

**[Observed] The claim is true and its stated denominator is smaller than the
population.** The report says "the union rule holds in 6 of 6"
(`DEPENDENCY-CLOSURE-REPORT.md:205`); its "six" is the six READMEs that
declare dependencies with no clause-level citation (`:198-199`).

There are **7** multi-file packages. My independent computation over all of them:

| Package | Members | README == union |
|---|---|---|
| RFC-0002 | 4 | **yes** |
| RFC-0003 | 2 | **yes** |
| RFC-0004 | 4 | **yes** |
| RFC-0005 | 3 | **yes** |
| RFC-0007 | 2 | **yes** |
| RFC-0008 | 3 | **yes** |
| RFC-0009 | 3 | **yes** |

**7 of 7 — set-equal, no readme-only or union-only elements in any package.**
The invariant is stronger than claimed. **[Observed]** Not a defect; noted
because "6 of 6" reads as a full-population claim and is not one.

### 3.3 Dangling edges, independently

**[Observed] 139 module-level `depends_on` entries examined; 0 dangling** —
every target resolves to a contract with at least one module in the tree.

**[Unknown] I could not reconcile CG-13's denominator with mine.** CG-13 reports
"146 edges examined"; my module-level sweep finds 139. The 7-edge difference is
plausibly the 7 package-level aggregate rows, but I did not confirm this and do
not assert it. Both populations report zero dangling, so no finding turns on it.

### 3.4 The vocabulary-ordinal correction

`DEPENDENCY-CLOSURE-REPORT.md:214-215` / `FINAL-OWNER-ACCEPTANCE-RECORD.md:69`:
"A sweep of all **13** `RFC2-24 #N` citations in the corpus finds **0**
remaining mismatches."

**[Observed] The substance is correct; the denominator is not reproducible.**
I extracted RFC2-24's twelve-reason table (`RFC-0002/rendering-vocabularies.md:85`
ff.) and checked every ordinal citation inside the 32 modules:

- `RFC-0009/semantic-geography.md:270` now reads `missing-declaration` (RFC2-24 #1) — **the correction landed.**
- **15 in-corpus ordinal citations found (16 counting a second ordinal sharing one line at `RFC-0004/general-contract.md:205`), and all 15/15 are correct against the table.**

So "0 mismatches" is true and I confirm it by my own sweep. But the population is
15–16, not 13. **[Observed] This is a "zero / all" claim published with a
denominator that does not reproduce** — the precise discipline
`AGENTS.md` verification rule 2 exists to enforce. Low severity, indicative.

---

## 4. The validators — output, not exit codes

Run against the pristine `864718c` export.

### 4.1 Results

| Command | Result | What its output actually shows |
|---|---|---|
| `check_governance.py` | **FAIL — 19 OK, 10 WARN, 1 FAIL (30 checks)** | CG-1b fails with 2 findings |
| `check_governance.py --selftest` | **PASS — 10 fixtures, 0 failing** | covers CG-13…CG-19 only |
| `verify_final_prespec.py` | **PASS — all checks clean** | 32 modules, 100673 words, 328 clauses, 2 notes |
| `build_contract_index.py --check` | **no drift** | — |
| `build_dependency_index.py --check` | **no drift** | — |

**FINDING RC10-M [Observed] — the repo-wide governance check FAILS at the
offered commit, and the offering record does not say so.**

```
FAIL  CG-1b  code-span path references resolve — 931 references examined, 2 findings
  round-2026-08/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md:3
      -> ../round-2026-08b/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md
  round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md:3
      -> ../round-2026-08b/PUBLIC-CLONE-VERIFICATION-REPORT.md
```

Both are superseded round records pointing at successor files in
`round-2026-08b/` that do not exist there. `FINAL-OWNER-ACCEPTANCE-RECORD.md:99-107`
§5 "Evidence you can reproduce" lists this command first and describes it as "30
checks, denominators printed", with no mention that it currently exits nonzero.
The "knowingly imperfect" table (`:71-83`) does not carry it.

The two failing files are **not** inside act 1's digest set, and CG-7a–7d all
pass, so the acceptance record's own gating rule ("A CG-7 failure means do not
perform that act") is not tripped. The defect is that an owner told to run the
battery as evidence gets a red result no document prepared them for, in a
repository whose stated rule is to read a check's output before claiming
anything is clean. **[Observed] The concurrent session appears to be fixing
exactly this** — it created an untracked
`round-2026-08b/PUBLIC-CLONE-VERIFICATION-REPORT.md` during my review — which
confirms the defect is real but also that the offered commit is not the intended
final state.

**[Observed] Correction to my own first result.** My initial run against the
*live* working tree reported `build_contract_index.py --check` → "DRIFT:
05-CONTRACT-INDEX.yaml differs from regeneration". That was an artifact of the
concurrent session's edit to `craft-and-care/README.md` (which the index
projects a word count from: 649 → 725), **not** a defect at `864718c`. Against
the pristine export both index checks are clean. I record the false start
because a reviewer who had not isolated the commit would have reported a drift
that is not in the package.

### 4.2 Attacking the checks — CG-13, CG-17, CG-18, CG-19

I copied the pristine tree to a scratch directory and introduced, one at a time,
the exact defect each check claims to detect. The real repository was never
mutated.

| Check | Claims to detect | Mutation applied | Result |
|---|---|---|---|
| **CG-13** | dangling edges; README ≠ module union | added `RFC-0009` to `RFC-0008/state-vocabulary-and-cost.md`'s `depends_on`, left the README alone | **CAUGHT** — `FAIL … 147 edges examined, 1 finding` |
| **CG-17** | a surface clause not routed | deleted the `RFC10-22` row from the routing matrix | **CAUGHT** — `FAIL … 1 finding: RFC10-22 declared in a contract, absent from the matrix` |
| **CG-17** | (converse) | appended a routing row for `RFC11-999`, a clause no contract declares | **MISSED** — `OK … 200 clauses examined, 0 findings` |
| **CG-18** | a fixture whose word count no longer recomputes | falsified fixture 5's count to 99,999 **and** de-anchored its load command | **MISSED** — `OK … 14 measurements examined, 0 findings` |
| **CG-19** | a substrate pin that is not publicly resolvable | replaced all pin URLs with well-formed but nonexistent GitHub URLs | **MISSED** — `OK … 5 pins examined, 0 findings` |

**FINDING RC10-N [Observed] — CG-17 does not detect routed-but-undeclared
clauses, and a fabricated row inflates its own denominator.** `check_governance.py:1270-1275`
flags `declared - routed` and duplicates, never `routed - declared`. Adding a
fictional clause row raised the printed count from 199 to **200** — a
denominator that grows when you add fiction is the failure mode this repository
says it exists to prevent.

**This is live, not hypothetical.** See §5.1: **6 of the 199 currently routed
ids are not bold-declared clauses.**

**FINDING RC10-O [Observed] — CG-18 silently skips a fixture whose anchors are
broken, and reports OK.** `check_governance.py:1318-1320` `continue`s *before*
incrementing `examined` when the load-command block or digest heading is not
matched. With fixture 5 de-anchored and its stated word count falsified to
99,999, CG-18 printed `OK … 14 measurements`. The only signal is the
denominator dropping 16 → 14. `FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md:76-79`
discloses that the check's *first* version examined 4 of 8 while printing a
count — the residual form of that same bug is still present, undisclosed.

**FINDING RC10-P [Observed] — CG-19 does not check resolvability; it checks for a
URL-shaped string.** `check_governance.py:1315-1319` searches for
`https?://|npm:|pypi:`. No network call is made and no revision is verified. A
pin to a deleted repository at a nonexistent commit passes as "publicly
resolvable". The check detects the one defect it was written for (a
founder-local path with no URL); its **name overclaims what it establishes.**

**FINDING RC10-Q [Observed] — CG-14 verified nothing.** `WARN CG-14 acceptance
install routes valid — **0 routes examined**, 0 findings — no `source/ →
destination/` pairs found in the acceptance record`. Its selftest passes against
synthetic input, so it *can* fail — but over the real corpus it examined zero
items. `FINAL-OWNER-ACCEPTANCE-RECORD.md:102-103` presents the battery as "30
checks, denominators printed" without noting that one of them has an empty
population. To the checker's credit it reports WARN rather than OK, and states
why — this is the honest form of the failure and I credit it.

**[Observed] Selftest scope.** `--selftest` runs 10 fixtures covering CG-13…CG-19
only. **CG-1 through CG-12 have no self-test at all** — including CG-7, the
check every act-verification instruction depends on. The offering record's
"each check shown able to fail" (`FINAL-OWNER-ACCEPTANCE-RECORD.md:103`) is
therefore true of 7 of 30 checks, not 30 of 30. **[Observed] This is an
inaccurate claim about the evidence.**

---

## 5. Recomputing the numeric claims

Every figure below was recomputed by me, independently, and where a "second
method" is stated the two agreed.

| Claim | Source | My recomputation | Verdict |
|---|---|---|---|
| **328 clauses** | `verify_final_prespec.py`; §3 row 3 context | **328** distinct unlettered clause ids across 32 modules; per contract 32/25/32/29/26/28/38/32/52/22/12; **no gaps, no duplicates**; +21 lettered limbs = 349 total | **VERIFIED** |
| **100,673 words** | `FINAL-OWNER-ACCEPTANCE-RECORD.md:77` | `wc -w` over the 32 modules → **100673**, matching the script's independent sum (second method agrees) | **VERIFIED** |
| **RFC-0001 = 8,342 words vs 7,000 ceiling** | `:76` | 8342 | **VERIFIED** |
| **199 routed clauses** | `FINAL-OWNER-ACCEPTANCE-RECORD.md`/commit msg; CG-17 | union of declared∪routed = **199**; but **declared = 193**, routed-unique = 199 | **MISLEADING — see RC10-R** |
| **8 fixture drift figures** | `FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md:53-62` | all 8 recomputed | **VERIFIED 8 of 8** |
| **fixture 5 drift = +1,738** | `:59` | 12,843 → 14,581 = **+1,738** | **VERIFIED** |
| **"between roughly 10.8k and 22.2k"** | `:42-43` | min 10,866 / max 22,242 | **VERIFIED** |
| **seven-of-eight class coverage** | `:81-108` | see below | **VERIFIED** |
| **all 13 RFC2-24 ordinals agree** | `:69` | 0 mismatches over **15–16** citations | **substance verified, denominator not reproducible (§3.4)** |
| **20 asymmetric edges (historical)** | `DEPENDENCY-CLOSURE-REPORT.md:9` | pre-fix state, not reconstructible at this commit | **[Unknown]** |
| **"nine compaction passes, floor −12…−22%"** | `:77` | process history outside this commit | **[Unknown]** |

### 5.1 The 199

**FINDING RC10-R [Observed] — "199 routed clauses" is the size of a union of two
differently-derived sets, not a count of clauses.**

- Clauses bold-declared in RFC-0006…0011: **193**
- Unique clause ids appearing as routing-matrix rows: **199**
- `declared − routed` = **∅** (every declared clause is routed — the real, good result)
- `routed − declared` = **6**: `RFC7-2(a)`, `RFC7-2(b)`, `RFC7-2(c)`, `RFC7-9(a)`, `RFC7-9(b)`, `RFC7-9(c)`

Those six are declared in prose and front matter — `RFC-0007/README.md:7`,
`RFC-0007/narrative-contract.md:6` and `:589` all enumerate "sub-clauses
RFC7-2(a)-(c), RFC7-9(a)-(c), RFC7-11(a)" — but unlike `RFC7-11(a)`
(`narrative-contract.md:234`, a bold headline) they have **no bold clause
definition** in the body. So either the corpus asserts six sub-clauses it never
defines in definitional form, or CG-17's `declared` regex is incomplete. Either
way the published figure 199 mixes the two populations, and §4.2 shows CG-17
cannot tell the difference. **[Unknown] which of the two readings is correct** —
resolving it requires an owner/author judgment about whether `RFC7-2(a)-(c)` are
intended as citable clauses.

### 5.2 The seven-of-eight coverage claim — verified

**[Observed] Confirmed by direct inspection.** The claim is that the
evidence-adapter class is uncovered because fixture 2 takes RFC-0004's
non-evidence half. Fixture 2's mandatory load is:

```
rfcs/RFC-0004/README.md rfcs/RFC-0004/general-contract.md rfcs/RFC-0004/named-adapters.md
rfcs/RFC-0008/README.md rfcs/RFC-0008/state-vocabulary-and-cost.md
rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:security.md
```

`execution-record.md` and `fidelity-joins-and-mappings.md` — the two
evidence-plane modules — are **absent from the mandatory set** and are named
only as deliberate exclusions. **The seven-of-eight-with-one-double-count claim
is accurate, and the self-criticism is correct.** This is exemplary disclosure:
the round found its own coverage table had been inflated by a double-count and
said so with the mechanism.

### 5.3 The eight fixture figures — verified individually

| Fixture | Recorded | Report "Actual" | My recomputation | Digest |
|---|---|---|---|---|
| 1 Polaris narrative | 13,864 | 13,842 | **13,842** | match |
| 2 Trajectory adapter | 18,315 | 18,282 | **18,282** | match |
| 3 Orrery lens | 14,134 | 14,110 | **14,110** | match |
| 4 execution profile | 10,893 | 10,866 | **10,866** | match |
| 5 cross-project mission | 12,843 | 14,581 | **14,581** | match |
| 6 doctrine amendment | 11,537 | 11,523 | **11,523** | match |
| 7 kernel identity | 15,767 | 15,738 | **15,738** | match |
| 8 OpenSpec authoring | 22,258 | 22,242 | **22,242** | match |

**8 of 8 word counts recompute exactly; 8 of 8 packet digests recompute exactly;
all 8 drift figures reproduce.** [Observed]

---

## 6. A stale-derived-value class inside the digest set

**FINDING RC10-S [Observed] — 21 derived word-count values inside act 1's digest
set are stale, undisclosed, caused by the offered commit itself, and contradict
that commit's own message.**

Commit `864718c`'s subject line is: *"governance: close contract dependencies on
evidence, extend the check battery, **correct every stale derived value**."*

That commit removed the `provides_to` front-matter key from all 32 modules. Each
package README carries a module table quoting each member's word count. **Those
tables were not updated.** Every value is high by 1–9 words, exactly consistent
with the removed key:

| File:line | Module | Claims | Actual |
|---|---|---|---|
| `RFC-0002/README.md:43` | snapshot-and-evaluation-core.md | 1,964 | 1,955 |
| `RFC-0002/README.md:44` | challenge-lifecycle.md | 2,231 | 2,225 |
| `RFC-0002/README.md:45` | reconciliation-chain.md | 2,477 | 2,470 |
| `RFC-0002/README.md:46` | rendering-vocabularies.md | 2,397 | 2,388 |
| `RFC-0004/README.md:44` | general-contract.md | 1,680 | 1,677 |
| `RFC-0004/README.md:45` | named-adapters.md | 3,685 | 3,682 |
| `RFC-0004/README.md:46` | execution-record.md | 1,775 | 1,770 |
| `RFC-0004/README.md:47` | fidelity-joins-and-mappings.md | 1,742 | 1,737 |
| `RFC-0005/README.md:43` | admission-and-boundary.md | 3,643 | 3,635 |
| `RFC-0005/README.md:44` | consent-egress-secrets.md | 2,351 | 2,343 |
| `RFC-0005/README.md:45` | execution-profiles.md | 2,197 | 2,192 |
| `RFC-0007/README.md:41` | narrative-contract.md | 5,167 | 5,165 |
| `RFC-0007/README.md:42` | rendering-and-surface.md | 3,143 | 3,142 |
| `RFC-0008/README.md:43` | identity-authority-materialization.md | 2,686 | 2,684 |
| `RFC-0008/README.md:44` | state-vocabulary-and-cost.md | 3,507 | 3,504 |
| `RFC-0008/README.md:45` | accounting-reconciliation-and-release.md | 3,055 | 3,051 |
| `RFC-0009/README.md:49` | semantic-geography.md | 6,999 | 6,996 |
| `RFC-0009/README.md:50` | visual-grammar-and-lenses.md | 5,540 | 5,538 |
| `RFC-0009/README.md:51` | interaction-parity-and-release.md | 3,027 | 3,023 |

Plus two package-level totals on one line, `RFC-0007/README.md:45`:

- "this index is **2,326**" — the README is **2,324** words
- "Package union: **10,636** words" — the package is **10,631** words

**19 module rows + 2 package totals = 21 stale derived values, across 6 of the 7
package READMEs** (RFC-0003's README carries a clause-range table with no word
counts and is unaffected).

Why this matters more than 1–9 words each:

1. **It is inside the bytes act 1 binds.** Correcting it necessarily changes
   those modules' digests and therefore the act-1 argument. This cannot be
   dispositioned as an accepted exception; it is a re-offer.
2. **It is precisely the failure mode `AGENTS.md` verification rule 3 names**:
   "a derived value quoted outside its owning artifact goes stale silently."
   Twenty-one instances, in the commit that claims to have corrected every one.
3. **It is a regression of a defect class this project already fixed once.**
   `AGENTS.md` records that a prior round changed act 1's argument partly
   because "RFC-0007 README self-counts and edge count corrected". The RFC-0007
   self-counts are stale again.
4. **No check covers it.** CG-18 recomputes fixture word counts and CG-8 reports
   module budgets, but nothing compares a README's quoted member counts to the
   members. This is the same shape as the fixture drift CG-18 was written to
   catch — caught in one artifact class, uncaught in another.
5. **It is undisclosed.** It appears in no row of
   `FINAL-OWNER-ACCEPTANCE-RECORD.md:71-83`.

---

## 7. Judging the disclosures

### 7.1 What the offering gets right — and it is a great deal

**[Observed] This is the most honest offering document I have reviewed in this
repository.** Specifically:

- It **leads with its own worst residual** (`FINAL-OWNER-ACCEPTANCE-RECORD.md:15-22`):
  "no confirming review is bound to the bytes you would be accepting." Putting
  the strongest argument against acting at the top, above the acts, is the
  correct structure and the opposite of advocacy.
- It **records its own reverted mistake** rather than quietly fixing it
  (`:60-64`), and `DEPENDENCY-CLOSURE-REPORT.md:64-67` leaves the wrong table
  standing "because the error it records is instructive."
- It **retracts a completeness claim against its own interest**: the
  eight-for-eight fixture coverage is restated as seven-for-eight with a
  double-count (`FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md:105-108`).
- It **refuses to overclaim the compiler**: "Any claim that Syzygy has automatic
  context compilation today is false" (`:36-37`).
- It **discloses an instrument it cannot quote**: F-EQ-4 and F-EQ-8 need a real
  GNU grep and "They have not been" re-run (`:132-138`).
- It **states the check-battery reading rule** — output, not exit code
  (`FINAL-OWNER-ACCEPTANCE-RECORD.md:109-113`).
- Every owner item it defers is really tracked: **P-21, P-22, P-23, P-24 all
  present** in `PENDING-OWNER-DECISIONS.md:64-72`. [Observed]
- I spot-checked disclosure row 6 ("RFC9-32 cites `RFC 0008 §5`, a navigational
  section, as authority") and confirm it at
  `RFC-0009/visual-grammar-and-lenses.md:209` and `:238`. [Observed]

### 7.2 What is materially missing from the list

An owner reading `FINAL-OWNER-ACCEPTANCE-RECORD.md` §3 would not learn any of
the following, each of which I judge material:

| # | Missing disclosure | Where established |
|---|---|---|
| i | **21 stale derived word counts inside act 1's own digest set**, caused by this commit, in the commit that claims to have corrected every stale derived value | §6, RC10-S |
| ii | **`check_governance.py` currently FAILS** (CG-1b, 2 findings) while §5 offers it as reproducible evidence | §4.1, RC10-M |
| iii | **The closure report misdescribes 4 of the 9 seams it reports closed**, including F6 which it separately flags as live on day one, and F7 which it calls the highest-consequence leak | §2.6, RC10-I…L |
| iv | **"199 routed clauses" counts 6 ids no contract defines**; CG-17 structurally cannot detect this and the fake rows inflate its denominator | §5.1, RC10-R |
| v | **CG-17, CG-18 and CG-19 each pass over the defect they name** — demonstrated by mutation | §4.2, RC10-N/O/P |
| vi | **"each check shown able to fail" is true of 7 of 30 checks**; CG-1…CG-12, including CG-7, have no selftest | §4.2 |
| vii | **CG-14 examined 0 items** — disclosed by the checker, not by the offering record | §4.2, RC10-Q |
| viii | **RFC10-18 routes failures into `blocked`, which RFC10-5 defines as non-terminal and which RFC10-19's recovery duties do not reach**; RC-7's non-blocking F13 was not re-examined against the new clauses | §2.3, RC10-A/B |
| ix | **Stop does not propagate to child missions**, and synchronous stop has no failure path | §2.4, RC10-E/F |
| x | RC-7 explicitly asked that the six clauses be inserted **after** act 1; they were inserted before, churning the manifest twice. The deviation is unrecorded | §2.1 |

Items i–iv are the ones I consider disqualifying at this digest. Items v–x are
disclosable exceptions.

### 7.3 The honest counterweight

**[Inferred] None of what I found is concealment.** The pattern is uniform: this
round built new checks, found real defects with them, fixed those, and reported
them well — and the residue is in the places the new checks do not look
(package-README self-counts, routed-but-undeclared ids, cross-artifact
paraphrase). That is the signature of a maturing verification battery, not of
advocacy. The disposition table errors in §2.6 read as paraphrase drift under
time pressure, not as spin; three of the four describe a *stricter* clause than
was written or mislabel a rule that is present.

---

## 8. Why REVISE and not EXCEPTIONS

The distinguishing test I applied: **can the owner accept this, at this digest,
knowing everything material?**

Two findings say no, because neither can be cured by disclosure:

1. **RC10-S — 21 stale derived values inside the digest set.** Any correction
   changes the modules' digests and therefore act 1's argument. The owner cannot
   "accept it knowingly" and leave it; the artifact must be regenerated and the
   act re-offered. And leaving it uncorrected means act 1 binds, permanently and
   by digest, twenty-one numbers the corpus itself contradicts — in a project
   whose central discipline is that derived values go stale silently.

2. **RC10-I…L — the owner-facing description of the round's most
   safety-critical change is wrong in four of nine rows.** `FINAL-OWNER-ACCEPTANCE-RECORD.md:51-52`
   routes the owner to that table to understand what act 1 newly binds. An owner
   who reads it believes `propose-only` carries a carve-out it does not carry,
   that RFC10-19 contains a sibling-work rule it does not contain, that stop
   guarantees consistency it does not guarantee, and that cross-project consent
   is selected by "the lesser binds" when it is conjunctive. Informed consent
   over misdescribed text is not informed consent. This is fixable **without**
   touching the digest set — the closure report is outside it — which is exactly
   why it should be fixed before the offer rather than accepted as an exception.

RC10-R (the 199) is a third, lesser reason: a published coverage figure that
counts six undefined ids should be resolved before it is quoted in an
acceptance context, and resolving it may or may not touch RFC-0007.

**What REVISE does not mean here.** It is not a judgment that the contracts are
unsound. The 32 modules verify byte-exact; the dependency work is correct and I
could not refute any part of it; 328 clauses, 100,673 words, all eight fixture
figures and the seven-of-eight coverage claim all recompute exactly; the six new
clauses are well-formed, are the adversarial reviewer's own text, and close nine
real seams. The correction plane is a genuine improvement and RFC10-16 correctly
prevents any of it scheduling work. **The package is close.** What it is not,
at this exact digest, is ready to be bound.

### Minimum to reach CONFIRM

1. Correct the 21 derived word counts in the six package READMEs; regenerate the
   manifest **by script**; re-quote act 1's argument. (RC10-S)
2. Correct the four disposition rows in `MISSION-SAFETY-CLOSURE-REPORT.md` to
   describe the clauses as adopted; state explicitly that F6's consistency limb
   is **not** closed. (RC10-I…L)
3. Resolve whether `RFC7-2(a)-(c)` and `RFC7-9(a)-(c)` are citable clauses; make
   the 199 figure reproducible either way. (RC10-R)
4. Fix or disclose CG-1b. (RC10-M)
5. Add the §7.2 items v–x to the "knowingly imperfect" table, and correct "each
   check shown able to fail" to its true denominator.
6. Record RC10-A/B (the `blocked` contradiction) as an owner item — it is a
   genuine internal inconsistency in the digest set and should be ruled on, not
   silently carried.
7. Let the concurrent session's edits settle, then re-verify. The offering must
   be stationary when it is offered.

Items 2–7 do not touch the digest set. Only item 1 — and possibly item 3 —
changes act 1's argument.

---

## 9. Scope statement

**What I verified mechanically:** manifest and all 32 per-module digests; clause
counts and numbering; word totals by two methods; all clause cross-citations;
the full dependency graph; all package README unions; all eight fixtures'
digests and word counts; every RFC2-24 ordinal; all five validators; four
mutation tests against three checks.

**What I read and judged as text:** RFC-0010 in full, RFC10-17…22 and the three
amendments in detail against RC-7's proposals; the closure report; the
dependency closure report; both offering records; the fixture report; RC-7's
findings F1–F17 and verdict.

**What I did NOT do and where I am [Unknown]:** I did not read `_bootstrap/**`
or any authoring conversation. I did not re-derive the historical figures (the
20 asymmetric edges, the nine compaction passes, the ~121k rev9 corpus path). I
did not independently review RFC-0001…0009 as contract text — my clause-level
adversarial reading was scoped to RFC-0010 as instructed, so **the substantive
correctness of the other 30 modules is [Unknown] to me and rests on prior
reviews**. I did not re-run F-EQ-4/F-EQ-8 under GNU grep. I did not verify
CG-13's 146-edge denominator against my 139. I could not determine whether
`RFC7-2(a)-(c)` are intended as clauses.

**Verdict word, stated once more exactly:**

VERDICT: REVISE
