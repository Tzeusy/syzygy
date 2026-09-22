# Semantic delta — the Polaris opening-band aggregate (PWB-REQ-010)

> **Candidate — binds nothing.** An agent drafted these bytes under the
> owner's 2026-09-21 direction recorded in
> `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
> (row P-71, arm A, question 7: "slices 3–5 routed through one CC-REV-2
> scenario for the opening-band aggregate"). That direction authorizes
> drafting and nothing else. Only the human owner may amend the signed PWB
> behavioral change, by a dedicated owner act of its own that names this
> package's manifest digest. Silence, a commit, a review, a merged pull
> request or a manifest performs no act. Nothing here authorizes an
> implementation, and nothing here is an act record.

**Artifact(s):**

- `openspec/changes/polaris-project-wide-butlers-model/` — the
  eleven-artifact signed PWB behavioral package. **Two** of the eleven
  change: `specs/polaris-project-wide-butlers-model/spec.md` (one scenario
  added under PWB-REQ-010) and the generated `GOVERNING-DEPENDENCIES.md`
  (its source-digest line only). The other nine rows of
  `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` equal current bytes.
- Proposed bytes live only as unified diffs under `proposed/`. Nothing in
  the signed change directory is edited in place: CG-7h binds the current
  openspec bytes to the latest performed act, so a drafted edit in the tree
  would read as drift.

**Stable IDs affected:** `PWB-REQ-010`. One scenario is added under it. No
requirement is minted, retired or renumbered, and no `warrants` block
changes, so the dependency declaration's authority union is unchanged at 17
requirements and 96 distinct authorities and only its `spec.md` digest line
moves. `PWB-REQ-007` and `PWB-REQ-020` are **cited** by the new scenario and
are **not** amended (see "What explicitly does NOT change").

**Change class:** **Normative.** Argued below rather than asserted.

**Author:** drafting agent (Claude Opus 5, 1M context), on branch
`agent/gate-opening-band-scenario`, serving bead `syzygy-dov.21`.

**Date:** 2026-09-21

---

## Current meaning

`PWB-REQ-010` today, quoted in full from
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 596–630 (read at source this session):

> ### Requirement: PWB-REQ-010 — Polaris opens with the whole project
>
> Group: Presentation. Form: **state projection/query**.
>
> WHEN Polaris is opened, it SHALL first present Butlers' purpose, promises,
> non-goals, architecture, V1 scope and success criteria before presenting any
> single capability's detail.
>
> - **Case**: load Polaris with a model containing project statements and one or
>   more capability deep dives.
> - **Observable**: the first reading level answers the project questions and
>   routes to the catalogs; capability detail is subordinate.
> - **Oracle**: inspect the heading order and entity references against an
>   independently enumerated project-level fact set.
> - **Oracle independence**: expected facts and order come from RFC7-13 and the
>   machine model, not the rendered page.
> - **Falsifier**: the entry opens on one capability, omits a project-level
>   category, or requires reading a capability deep dive to learn what Butlers is.
>
> #### Scenario: WhatsApp is a drill-down, not the project account
>
> - **WHEN** the existing WhatsApp capability slice is present
> - **THEN** the Polaris entry explains Butlers before linking to that slice
> - **AND** the slice is labeled as one capability within the complete catalog
>
> ```yaml
> warrants:
>   primary: RFC7-1
>   doctrine: [VIS-1, VIS-3]
>   contracts: [RFC7-1, RFC7-6, RFC7-13, RFC7-15]
>   policies: [CC-BAR-3]
>   decisions: [POLARIS-DIR-2026-08-31]
>   topology: []
>   parent_requirements: [three-surface-poc-experience/POC-REQ-030]
> ```

Two neighbouring clauses the new scenario cites without amending, quoted
exactly from the same file.

`PWB-REQ-007`'s aggregate sentence and its Observable (lines 448–450 and
457–458):

> Aggregates SHALL disclose label, tier, freshness and separate primary/
> secondary reason counts without a headline status, composite maturity or
> inferred success.

> - **Observable**: human and machine views expose identical complete tuples;
>   invalid/missing currency stays Unknown and aggregates expand to members.

`PWB-REQ-020`'s requirement text (lines 906–910):

> Every project-shape identity, statement, source anchor, coverage state,
> denominator, contradiction, body-read authority state and walkthrough-judgment
> state or disclosure Polaris presents SHALL be recoverable from the same
> evaluation in the machine answer, preserving multiplicity and exact provenance
> state.

**What the current text does and does not settle.** PWB-REQ-010 settles the
*order* of the first reading level and the *categories* it must carry.
PWB-REQ-007 settles what any aggregate must disclose. Neither settles whether
an aggregate over the Unknown project-shape claims may be rendered at the
opening, how many such aggregates there may be, or what relation such an
aggregate bears to the claims it counts. That silence is the gap the M4
funnel's Gate 5 records: for slice 3 it finds "**None found.**" under "Approved
requirement **and** scenario" and "**Unavailable**" under limb 1, over a
stated denominator of 41 approved requirements and 55 scenarios across both
signed specifications.

---

## Proposed meaning

One scenario is inserted under PWB-REQ-010, after the existing scenario's
last bullet and before the requirement's `warrants` block. Quoted exactly as
`proposed/spec.md.patch` adds it:

> #### Scenario: One opening Unknown aggregate, reconciled with members
>
> - **WHEN** Polaris's first reading level renders an aggregate over the Unknown
>   project-shape claims one evaluation holds, before the first capability
>   catalog
> - **THEN** exactly one such aggregate is rendered there, it displaces and
>   defers no project-level category of this requirement, and it reads only that
>   same evaluation's machine claims
> - **AND** it discloses its own label, tier, freshness and separate primary and
>   secondary reason counts as PWB-REQ-007 requires of an aggregate, claims no
>   headline status, and exposes every counted Unknown reason's resolution route
> - **AND** its member population and its primary and secondary reason counts
>   equal those of the claims it names at that evaluation, every counted member
>   stays separately disclosed at its own claim and reachable from the aggregate,
>   and the machine answer carries the same aggregate under PWB-REQ-020

**The obligation this adds.** The scenario is *conditional*: it does not
require an opening aggregate to exist. It says that **if** one is rendered,
then five things hold — uniqueness in that region, non-displacement of the
project-account categories, the PWB-REQ-007 tuple on the aggregate itself,
identity of the aggregate's population and counts with the claims it names,
and continued separate in-place disclosure of, and reachability to, every
counted member, in both channels.

**Why conditional and not mandatory.** Mandating the band would schedule the
implementation work by amendment. Under VIS-4 that is the owner's to
schedule, and P-71's own sequencing keeps slice 3 behind this scenario's
sign-off rather than the reverse. A scenario that *admitted* the band while
*requiring* it would also foreclose the owner's express reservation recorded
in the M4 funnel's Q7 cell — "The block order *within* the band is the
owner's to set, not this packet's".

**Why it is Normative, not Clarifying.** Someone who complied with
PWB-REQ-010 before may not comply now. Today a renderer may place two
independent aggregates in the opening region, may give an opening aggregate
no tuple, and may hoist a member's Unknown out of its own claim into a
summary. After this scenario each of those is a falsifier. An obligation is
added; by the change-class rule "Class is determined by what changes in the
obligation, never by diff size", that is Normative and nothing narrower.

---

## What explicitly does NOT change

Enumerated, because "I only touched X" is the field's stated failure mode.

1. **PWB-REQ-010's requirement sentence, Case, Observable, Oracle, Oracle
   independence, Falsifier and `warrants` block** are byte-identical. The
   existing scenario "WhatsApp is a drill-down, not the project account" is
   byte-identical and is not superseded.
2. **PWB-REQ-007 is not amended.** Its aggregate sentence is cited by the new
   scenario and its text does not move. The separate CC-REV-2 clarification
   scenario to PWB-REQ-007 the owner ruled in P-69 Q7a (gate bead
   `syzygy-dov.20`) is a different change and this package does not touch its
   region of the file.
3. **PWB-REQ-020 is not amended.** Parity's population, oracle and mutation
   proof are unchanged; the new scenario states that the aggregate is inside
   that population, which PWB-REQ-020's own text already reaches through
   "or disclosure Polaris presents". Two readings of that clause exist and
   this package takes the wider one without amending the requirement: the
   Case at spec lines 912–914 enumerates "every PWB-REQ-005 authority state
   and PWB-REQ-022 judgment state and disclosure", and the M2 funnel itself
   flags (lines 462–464) that on the narrower reading, where "disclosure"
   attaches to the PWB-REQ-022 judgment state, a currency probe's facts
   "fall outside the enumerated population entirely". On that narrower
   reading the scenario's fourth bullet is a scope claim on a requirement
   this package does not amend, and the package would need a PWB-REQ-020
   amendment outside this category. The wider reading is the one under
   which this change lands without touching PWB-REQ-020; it is named here,
   not settled: an owner who holds the narrower reading should say so
   before any act (round 5 finding 27).
4. **PWB-REQ-011 and PWB-REQ-012 are not amended.** Progressive depth and the
   copy rules (six-word headings; the prohibited words `page`, `document`,
   `reading`, `section`, `movement`, `presentation`) continue to bind any
   rendered band exactly as they do today; the new scenario grants no
   exemption from either.
5. **No warrant list changes**, so no authority is added to or removed from
   the CC-IMPACT-1 union. The generated declaration's only changed byte is
   its `spec.md` digest.
6. **Nothing is written into an observed repository.** The scenario describes
   a rendering and a machine answer only. Per P-71-Q5 the return path's write
   into the observed repository is foreclosed and slice 6 does not run; this
   package neither revisits nor relies on that.
7. **The three-surface POC specification is not amended** and no POC-REQ is
   minted. The owner's P-75 Q1 routes POC-spec amendment into its own
   CC-REV-2 package behind gate `syzygy-dov.26`; this package must not
   overlap it.
8. **No implementation file changes.** `proposed/` carries diffs against two
   governed artifacts and nothing else.

---

## Warrant

The owner's dated direction of 2026-09-21, row **P-71**, arm **A**, question
7, quoted from
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`:

> **A** — … Q7 slices 3–5 routed through one CC-REV-2 scenario for the
> opening-band aggregate.

and, from the same row's "What it means" cell:

> Slices 1–2 after M3 slice 5 under the continuation act; slice 3 only after
> the three-way opening-band reconciliation and the scenario's sign-off;
> slices 4–5 behind the same scenario …

The record's own head states its force: "Nothing here is an act: no digest is
bound, no specification, policy or registry byte changes, and no
acceptance-record row is added. It is a plain owner direction". Drafting is
therefore warranted; adoption is not.

---

## Evidence or decision basis

All reachable by anyone who can reach this file; every one read at source
this session.

- `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
  — rows P-68, P-69, P-70, P-71, P-71-Q5, P-74, P-75, P-78 and the
  cross-cutting readings section.
- `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` — the question table's Q4,
  Q6 and Q7 cells (line 119 carries Q7); the slice 3, 4 and 5 designs (lines
  820–913); Gate 5's subsection "The RFC2-26 test for slices 4 and 5" (line
  1210 onwards) with its eight-row table.
- `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` lines 441–513 —
  slice 2, the currency probe; the two passages quoted below sit at 443–446
  and 472–475.
- `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` lines 903–935 — slice 3,
  "One real Unknown in the first reading".
- `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
  lines 196–221 — RFC2-26, quoted in the reconciliation below at the defined
  clause (`DIRECTIVE-REGISTER.md` line 260 gives that definition site).
- Both signed specifications, read for the requirement and scenario
  populations.
- `apps/three-surface-poc/src/polaris.ts`, the `gapReasonCounts` function
  (lines 951–960 at `194f8cd`; 922–931 at the baseline `a4a3451`) — the
  projection for OQ-3 below (an earlier bullet said "finding R-3"; round 6
  finding 32).

---

## The three-way reconciliation, performed

P-71 conditions slice 3 on "the three-way opening-band reconciliation". The
three parties are named by the M4 funnel's Q7 cell:

> M2's slice 2, M3's slice 3 and M4's slice 3 all render into the **same
> region** — the opening band of `polaris.ts`, before the first catalog
> section — with three distinct payloads.

Each party's own design text, quoted from its own packet rather than from
the M4 summary of it.

**Party 1 — M2 slice 2, the evidence horizon.** From
`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` line 443 onwards:

> A **currency probe** is a second identified evaluation with one job: resolve
> the repository's current head and compare it to the pinned revision the model
> renders. It carries its own identity, of the form
> `evaluation:pwb-currency-probe:<instant>`, its own instant and its own tuple

and, at line 472:

> **The probe's own freshness.** The probe claim carries no freshness value,
> before slice 5 and after it. It is not a project-shape claim, so
> PWB-REQ-007's complete-tuple requirement does not reach it.

**Party 2 — M3 slice 3, one real Unknown in the first reading.** From
`docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` line 905 onwards:

> **Design.** The opening band renders, in place and before the first catalog
> group, the two Unknown claims the page already carries at 25.70% and 57.72%
> depth: the whole-shape claim and the class-level roster-identity claim. Each
> renders as the existing `unknown-disclosure` block — its reason verbatim, its
> route as an affordance — with its tuple beside it

and, at line 914:

> The band states the count of Unknowns on the page and links to them, so the
> reader who stops at the catalogs has met the page's honesty rather than only
> its coverage counts.

**Party 3 — M4 slice 3, the opening band.** From
`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` line 827 onwards:

> A band placed after the project account and before the first catalog
> section, rendering the same `gapReasonCounts` projection the gaps section
> already renders, every row linking to the existing `#polaris-gap-<reason>`
> anchor and carrying the reason's route.

and, at line 836:

> **One count, two renderings, one denominator.** The band must not be a
> second projection that can drift: it takes the same map and the same
> ordering function, and a test asserts the band's total equals the gaps
> section's total on every fixture.

### What the three agree on, and what the scenario therefore says

**R-1. One region, one uniqueness rule.** All three place their payload
before the first capability catalog. The M4 funnel's revised answer is that
three independent "renders before the first catalog section" assertions are
three oracles over one piece of page order, and that "whichever … lands first
**builds the band container and owns its single ordering oracle**". The
scenario carries that reconciliation into the specification as the words
"**exactly one** such aggregate is rendered there" — the falsifiable form of
"one band, one owner, one oracle". This is the part of the reconciliation
that only a specification can hold: an ordering convention agreed between
three unadopted design packets binds nothing, and the packet that lands last
cannot make the first two conform.

**R-2. Aggregation must not cost in-place disclosure.** Party 2 renders its
claims "in place", each with "its tuple beside it"; party 3 renders counts
whose rows link back to the existing per-reason anchors; PWB-REQ-007's
Observable says "aggregates expand to members". The scenario's fourth bullet
is the conjunction of all three: "every counted member stays separately
disclosed at its own claim and reachable from the aggregate". This is the
reconciliation's load-bearing clause, because it is the one that keeps an
opening aggregate from becoming the summary-without-member pattern M3's own
design rejects ("A count with no member rendered in place is the half of the
pattern the page already has").

**R-3. The aggregate's population is the project-shape plane, and only it.**
Party 1 states in its own words that the probe "is not a project-shape claim,
so PWB-REQ-007's complete-tuple requirement does not reach it". The owner
ruled the same boundary generally on 2026-09-21 in P-75 Q2: "PWB-REQ-007
reaches only the project-shape plane". So the region may hold three blocks
but the *aggregate this scenario governs* quantifies over "the Unknown
project-shape claims one evaluation holds" and over nothing else. The
currency probe and the POC relationship and entity Unknowns are in the
region, not in the aggregate. Without this, a single "all Unknowns in the
opening" aggregate would be required to carry a PWB-REQ-007 tuple for members
whose type cannot supply one — `PocEpistemic`'s Unknown arm in
`packages/three-surface-poc-core/src/model.ts` carries a `reason` and nothing
else, no tier and no freshness [Observed at source this session].

### What the reconciliation exposes and this delta does not resolve

Per the semantic-delta form's rule 6, "Contradictions are surfaced, never
silently reconciled inside a delta." Five are surfaced here and answered in
`OWNER-DECISION-PACKET.md` as open questions, not by this delta. In each the
reading that would make this change land the more easily is stated and **not**
taken.

**OQ-1 — one scenario cannot supply RFC2-26 limb 1 for slices 4 and 5.**
RFC2-26, quoted at the defined clause
(`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 201–205, inside the clause defined at line 196):

> Before implementation, every observable consequence either maps to an
> approved OpenSpec requirement and scenario in the governance root's
> `openspec/**` plane, or carries a reviewed N/A judgment proving it purely
> structural with no independently testable behavior.

The M4 funnel's own table gives slice 4's mapping as "**None** — the three
sweeps above find no requirement naming the field" and slice 5's as "**None**
— the three sweeps above find no requirement reaching the home route", both
"**Unavailable**, both limbs". Slice 4's consequence is a declared surface
population; slice 5's is the home route. Neither lies within this
specification's subject, which its own proposal states (paraphrased here,
from `proposal.md` §Scope) as the declared shape of the configured project;
and the sweeps behind those two cells returned zero
whole-word `home` hits in the POC specification, six in this one (all in the
precedence table's `Home` column or the registry governance-home field) and
zero hits for `surfaces` or `model.surfaces` in either. **A scenario placed
under PWB-REQ-010 therefore clears RFC2-26 for slice 3 only.** P-71's "slices
4–5 behind the same scenario" is honoured as a *sequencing* condition — they
wait for it — but it does not, and on these bytes cannot, supply their limb 1.
The reading not taken: widening this scenario's WHEN until it also names the
home route and the surface descriptors, which would make one package appear to
clear all three slices and would put material outside this specification's
subject inside it.

**OQ-2 — the host requirement, and whether RFC2-26 is satisfied by the pair.**
RFC2-26 wants a requirement **and** a scenario, and adds "Rows are per
observable consequence, not per clause." The opening-band aggregate has two
halves: *position and uniqueness* (PWB-REQ-010's subject) and *the aggregate
tuple* (PWB-REQ-007's subject, whose sole scenario is the per-claim case).
This package hosts the scenario under PWB-REQ-010 and cites PWB-REQ-007 for
the tuple. Three placements were considered and the trade-off is the owner's,
not this package's: (a) under PWB-REQ-010, as drafted; (b) under PWB-REQ-007,
which aligns clause and scenario for the tuple half but not for position, and
which collides on the same lines as two other live changes — two of the
three hunks of lane B's `proposed/spec.md.patch` cover lines 450–471 and
473–483, which contain PWB-REQ-007's only scenario at line 470, and P-69
Q7a's clarification scenario
(gate `syzygy-dov.20`) is destined for the same requirement; (c) minting a new
requirement, which would give the consequence its own clause and its own
scenario but is not "one CC-REV-2 scenario" and would move the requirement
count, the proposal's stated totals and the coverage matrices. The reading not
taken: asserting that (a) is sufficient. It is stated as a question.

**OQ-2 is a precondition, not a placement preference.** Until it is
answered, it is **not settled that this scenario clears RFC2-26 limb 1 even
for slice 3** — the position half and the tuple half sit under two
requirements, and PWB-REQ-007's only scenario remains the unmodified
per-claim case. This delta never asserts that RFC2-26 is satisfied; it says
the scenario is placed so as to clear it for slice 3 only, with OQ-2 open.
Whoever performs the amendment act should treat OQ-2 as a condition of any
later claim that slice 3's limb 1 is supplied, and not round it off as a
drafting nicety. The 2026-09-21 review raised this as finding 2 and it is
carried here unresolved, by design (rule 6).

**OQ-3 — the designed band does not satisfy the clause it inherits.**
PWB-REQ-007 requires an aggregate to disclose "separate primary/secondary
reason counts". The projection party 3 reuses counts primary reasons only —
`gapReasonCounts` in `apps/three-surface-poc/src/polaris.ts` (lines 951–960 at
`194f8cd`; 922–931 at `a4a3451`) reads `claim.epistemic.reasons.primary` and
increments one map [Observed at source, re-read 2026-09-23]. So the band as M4
designs it, rendering that map, would falsify the scenario's third bullet.
This delta keeps the clause's words rather than the design's, which means the
implementation must supply the secondary counts. The reading not taken:
softening the third bullet to "reason counts" so that today's projection would
pass — that would quietly narrow PWB-REQ-007 through a scenario under a
different requirement.

**OQ-4 — an opening aggregate against POC-REQ-032's "in place".** The
three-surface specification's POC-REQ-032 says, quoted at
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
lines 578–580: "where the model is Unknown, the narrative SHALL disclose the
Unknown and its reason in place", with Observable "Unknown regions appear as
disclosed Unknowns inside the narrative flow". The M4 funnel reads that as
excluding an opening aggregate: "requires the Unknown disclosed **in place**
in the narrative flow, which an opening aggregate is not." The scenario's
fourth bullet is drafted so that the aggregate never *replaces* an in-place
disclosure. Whether that is enough — whether a conforming rendering may carry
an aggregate at all, given that POC-REQ-032 is a prohibition in a **different**
signed specification this package may not amend — is not this package's to
decide. The reading not taken: treating "the members are still in place" as
settling POC-REQ-032, which would be this package reading another signed
change's prohibition in the direction that lets this one land.

**OQ-5 — the region's block order.** Q7 reserves it expressly: "The block
order *within* the band is the owner's to set, not this packet's — a currency
disclosure and an Unknown band are arguably separate regions, and if the owner
rules them so, each still needs a stated position relative to the other two
rather than three independent claims on 'first'." Against that sits
PWB-REQ-010's own signed sentence, that Polaris "SHALL **first** present
Butlers' purpose, promises, non-goals, architecture, V1 scope and success
criteria", and M2 slice 2's own stated target, in its Q6 cell
(`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` line 50), that "the
page's first human-visible instant moves from 58.0% depth into the opening
band" — M2's words, which M4's Q7 cell (line 119) quotes as M2's "own honest
target"; beside it sit M2's success criterion 4, "The first human-visible
instant on the page appears before the first catalog section", and its
58.0% depth measurement (§Review findings 6 and 11). The scenario says only
that the aggregate "displaces and defers no project-level category of this
requirement", which is compatible with either order and settles neither. The
reading not taken: fixing an order in the specification, which would decide an
owner value inside a delta.

---

## Terms introduced / retired

**None.** "Aggregate", "Unknown", "project-shape claim", "reason",
"resolution route", "evaluation", "primary" and "secondary reason", "machine
answer" and "first reading level" are all in use in the two clauses quoted
above and in RFC2-24's closed reason vocabulary. No durable term is minted,
so no term-registry admission is required. The phrase "opening band" is
deliberately **absent** from the proposed text: it is a design word from three
unadopted packets, and PWB-REQ-012 forbids `page`, `document`, `reading`,
`section`, `movement` and `presentation` in rendered headings, so the
specification names the region by its relation to the catalogs instead.

---

## Downstream impact

**Method, stated so the figures can be re-derived rather than re-read**
(verification rules 2, 4 and 9). Python `re` over the decoded UTF-8 text of
every path returned by `git ls-files -z` in this worktree, run 2026-09-21.
Denominator: **1,334** tracked files. Four patterns, counted per file:

1. `PWB-REQ-010` (the literal identifier).
2. A continuation-form pattern for the same identifier written as a run
   (`PWB-REQ-009, 010`, `PWB-REQ-009/010`), because a full-identifier sweep
   misses continuations and produces a false absence.
3. The two patched paths, as path literals.
4. The current `spec.md` digest, as a 64-hex literal.

Second method: `git grep -l -F` over the same literals, union compared to the
`re` result (rule 2). Results:

| Pattern | Files | Occurrences |
|---|---|---|
| `PWB-REQ-010` | 36 | 110 |
| continuation forms of it (the regex `IMPACT-LEDGER.md` states) | 6 | 7 |
| the patched `spec.md` path | 51 | 113 |
| the patched `GOVERNING-DEPENDENCIES.md` path | 9 | 13 |
| the current `spec.md` digest | 13 | 13 |

The continuation sweep adds five files over the full-identifier sweep, so
the citer population is 41, not 36; `IMPACT-LEDGER.md` names them and states
the regex [Observed, both sweeps re-run 2026-09-23 at the baseline commit].
An earlier draft said "adds no file" (0 / 0), which was false for the run
form the corpus writes (§Review finding 4).

**What is affected, by class.**

- **Regenerated in the same logical change:** `GOVERNING-DEPENDENCIES.md`,
  by `scripts/build_polaris_project_wide_spec_dependencies.py`. This
  package's builder regenerates it from the proposed specification bytes and
  `--check` fails if the proposed declaration differs from that regeneration,
  so a hand-edited generated file cannot ride along.
- **Digest-pinned and stale on adoption — a finding this package records.**
  Two governed JSON declarations pin the specification's current digest in a
  `governingBehaviorContract.version` field:
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
  and
  `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`.
  Both carry a `signedBy` value naming a pending exact owner act over the
  PWB truth-and-readiness amendment manifest. **Any** amendment to this
  specification stales both pins, this package's included; the owner has
  ruled, in the P-74 and P-78 rows, that the registry entry is edited on no
  arm of those moves — P-78 closing "The registry entry is edited on no
  arm." and P-74 "The consent record, the registry entry and PWB-REQ-005
  are edited on no arm.", each row's own sentence (§Review finding 9),
  each closing its row's whole "What it means" cell, not one scoped to a
  numbered sub-question, so the "Q4" tag an earlier draft carried is
  withdrawn (§Review finding 3) while the ruling stands —
  and P-69 Q2(a) and P-72 Q2 travel together as one
  superseding registry-entry amendment act at gate bead `syzygy-dov.18`. So
  the repair belongs to that act, not to this package, and this package edits
  neither file. [Observed: the two pins found by the digest sweep above;
  [Inferred]: that the registry act is where they are repaired — no record
  read this session says so in those words.]
- **Immutable act-time history, not edited:** the performed PWB amendment act
  records and their manifests quote the digests they bound at act time. They
  are correct about their own moment and are never rewritten. This delta
  cites them by path only and quotes no act argument.
- **Bound sibling packages, not edited:** lane B
  (`pwb-scoped-attributes-amendment`) proposes its own diffs against the same
  eleven subjects. See "Migration" for how the two compose.
- **Implementation and evidence citers:** the remaining PWB-REQ-010 citers are
  tests, the mutation sweep, the implementation plan, funnel packets, retained
  raw reviews and evidence records. None carries an obligation this scenario
  changes; retained raw reviews and dated evidence records are never edited
  (CC-REV-6), and the implementation sites change only when the owner
  authorizes slice 3, which this package does not do.

---

## Migration / supersession plan

**Regeneration cycle for the digest-bound artifacts** (the form's rule 7).
The eleven PWB behavior artifacts are one indivisible subject, as in the two
performed PWB amendments. `scripts/build_pwb_opening_band_scenario.py`
regenerates `PWB-OPENING-BAND-SCENARIO-MANIFEST.txt` over the *proposed*
bytes — current bytes with `proposed/*.patch` applied in a scratch tree —
never over the tree. Its current digest is quoted once, in
`OWNER-DECISION-PACKET.md`; regenerating the manifest retires that copy, and
CG-7d and CG-7e catch a stale copy once the package is registered.

**Order of operations, none of which this package performs.**

1. The package is reviewed in fresh context against `REVIEW-BRIEF.md`; the
   raw output is retained verbatim and the bytes it is bound to are frozen
   (rule 10). **Done six times**: round 1 CONFIRM WITH EXCEPTIONS; round
   2, over the repaired bytes at `9d74185`, REVISE; round 3, over `76b4beb`,
   REVISE; round 4, over `194f8cd`, REVISE; round 5, over `7fd2db3`,
   REVISE; round 6, over `2c5745e`, REVISE — dispositions for all in
   §Review — and the prose repairs that followed each round left its
   verdict bound to the reviewed commit, not to these bytes. A round 7 over
   these bytes is the next step.
2. The owner answers the five open questions in `OWNER-DECISION-PACKET.md`.
   Answers to OQ-2 or OQ-3 may change the proposed bytes, which retires the
   review and needs a fresh one. **Done, 2026-09-23**, in the two plain
   owner directions §Review round 2 cites; no proposed byte moved.
3. The owner performs a dedicated amendment act naming this manifest's
   digest, with a dedicated record and one aggregate section in
   `ACCEPTANCE-ACT-RECORD.md`, written by a recorder script — never
   transcribed.
4. `--apply --at-adoption` writes the proposed bytes into the tree **in the
   same change as the act record**, so the tree and the latest performed link
   agree.
5. Only then may slice 3 be scheduled, and only on the owner's separate
   implementation authorization. Slices 4 and 5 still need their own RFC2-26
   route (OQ-1).

**Composition with lane B.** Lane B is a separate candidate over the same
eleven subjects, at gate bead `syzygy-dov.17`; P-68 ruled its ceremony order
and its manifest's disposition gates four other beads. The two packages are
independent offerings and either may be adopted first. This package's builder
asserts that in code: `--check` applies lane B's `proposed/spec.md.patch` and
this package's, **in both orders**, in a scratch tree, and fails if either
order does not compose. It composes today [Observed, this session]. The two
`GOVERNING-DEPENDENCIES.md` patches do **not** compose, and that is correct
rather than a defect: both rewrite the one generated digest line, and a
generated file is regenerated after the second specification patch lands, not
patched twice. The builder's `--selftest` asserts that collision, so if lane B
changes shape the claim fails loudly instead of going stale.

**Nothing is superseded.** No clause, scenario or file becomes historical, so
no reading path drops anything.

---

## Review

**Required class:** full independent review in fresh context (CC-REV-1), on
the frozen bytes of this package, against `REVIEW-BRIEF.md`. The change class
claim above is itself part of what is reviewed.

**Reviewer:** a fresh-context session with no authoring context, per
CC-REV-1. The drafting agent did not review its own work.

**Round 1 verdict:** **CONFIRM WITH EXCEPTIONS**. The word is copied
exactly from the retained raw output, never restated.

**Raw output:** `docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-RAW.md`,
retained verbatim and never edited (CC-REV-6).

**Bytes the verdict is bound to (rule 10).** The raw names commit
`59733d3` and the manifest digest quoted in `OWNER-DECISION-PACKET.md`. The
three dispositions below edited `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md` and
`OWNER-DECISION-PACKET.md` **after** that commit, and `REVIEW-BRIEF.md`'s
status paragraph moved in the same commit with its criteria byte-identical
(four files changed, not three — §Review round 2 finding 8), so **the
confirmation is bound to the reviewed bytes and not to these**. The repairs touch prose only
— no byte of `proposed/spec.md.patch`, `proposed/GOVERNING-DEPENDENCIES.md.patch`
or the manifest moved, so the manifest digest is unchanged. The reviewer's
machine findings (items 2–10 and 13–16 of the raw: thirteen items) held at
the round-1 disposition commit; at the current bytes three do not hold as
written: item 9's continuation-form figure (0/0) is retracted by round 2
finding 4 below (the ledger now gives 6 files / 7 occurrences); item 13's
`polaris.ts` line range has moved (round 4 finding 21); and item 15's three
`check_governance.py` line pointers (1976, 2173 and 2300) moved to 2022,
2236 and 2371 when the lane B registration landed at `9d74185`, its
constants at 1518–1523 unmoved (round 6 finding 31) — the substance of 13
and 15 holds, their pointers do not. The other ten hold [Observed: builder
`--check`, `--selftest` and `--diff` re-run after the round-6 repairs cover
items 3, 4 and 5, and the manifest re-hashed covers item 2; items 6, 7, 8,
10, 14 and 16 were re-read at source by the round-5 reviewer]. Two earlier
sentences here are superseded and kept marked: the first said all "still
hold at this commit" — true at `9d74185`, false once the round-2 repair
moved the ledger's figure (round 5 finding 23); the second, the round-5
repair, said "two of the fourteen" do not and "the other twelve hold" —
the population is thirteen, not fourteen, and item 15 fails the sentence's
own moved-pointer test (round 6 finding 31). A
reader who needs a confirmation over *these* bytes needs a fresh review; this
section records the disposition, it does not extend the verdict.

**Dispositions.** Three findings, all notes, none blocking.

1. **Finding 1 — the ledger's "none did" was false.** Four tracked files
   fail UTF-8 decode, all binary images under `docs/evidence/`; the reviewer
   enumerated them. **Accepted and repaired.** `IMPACT-LEDGER.md`'s
   Population section now enumerates the four skipped paths from a scripted
   re-derivation, states the branch population it was derived over, and adds
   the remainder rule 2 demands: a NUL-byte second method returns **six**
   files, not four — the two extra decode as UTF-8 and were swept, not
   skipped — so the skip figure now names which predicate it uses. No swept
   figure moves; the reviewer independently reproduced all five.
2. **Finding 2 — OQ-2 should not be rounded off.** **Accepted; wording
   promoted, no decision taken.** OQ-2 stays open. Both `SEMANTIC-DELTA.md`
   and `OWNER-DECISION-PACKET.md` now say plainly that until OQ-2 is
   answered it is not settled that this scenario clears RFC2-26 limb 1 even
   for slice 3, and that whoever performs the act must treat OQ-2 as a
   condition of any later limb-1 claim. Nothing in the package asserts
   RFC2-26 is satisfied, which the reviewer confirmed.
3. **Finding 3 — the "Q4" attribution is tighter than the source.**
   **Accepted and withdrawn.** The sentence "is edited on no arm" closes the
   P-74 and P-78 rows' whole "What it means" cells; it is not scoped to a
   numbered sub-question. All three prose files now cite the rows rather
   than a sub-question, and say the earlier tag was this package's inference
   and is withdrawn. The ruling itself stands and remains [Observed].

**What no disposition changed.** No patch byte, no manifest row, no
requirement, no scenario text, and none of the five open questions. OQ-1 to
OQ-5 remain the owner's, unresolved.

### Round 2 — confirmation review over the repaired bytes

**Reviewed bytes:** commit `9d74185`, the merge of PR #52, with the manifest
digest quoted in `OWNER-DECISION-PACKET.md`. **Reviewer:** a fresh-context
session with no authoring context, commissioned on 2026-09-23 by the session
that had dispositioned round 1, with the raw and dispositions of round 1 as
its input and `REVIEW-BRIEF.md` as its commission. **Verdict:** **REVISE**,
copied exactly from the retained raw output. **Raw output:**
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-RAW.md`,
retained verbatim and never edited (CC-REV-6).

The reviewer found all three round-1 findings discharged and their
dispositions truthful, reproduced every machine figure, and confirmed that
the OQ-2 answer the owner gave on 2026-09-23 (placement (A), recorded in
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`) changes no proposed byte. The verdict is REVISE on
findings 4 and 5, two false sentences in `IMPACT-LEDGER.md`; findings 6–10
are notes. **Bytes the verdict is bound to (rule 10):** the reviewed commit.
The repairs below edited `IMPACT-LEDGER.md`, `SEMANTIC-DELTA.md`,
`OWNER-DECISION-PACKET.md` and `REVIEW-BRIEF.md` after it; no byte of
`proposed/spec.md.patch`, `proposed/GOVERNING-DEPENDENCIES.md.patch` or the
manifest moved, so the manifest digest is unchanged. These bytes carry no
confirmation until a round 3 reads them.

**Dispositions**, finding by finding:

4. **The continuation-form figure "0 / 0" and "adds no file" were false.**
   **Accepted and repaired.** The predicate was stated in words and run over
   one member; the corpus writes runs (`PWB-REQ-001/002/003/004/005/010`).
   `IMPACT-LEDGER.md` now states the regex, gives the six run-form files
   (five carry no literal), recounts the population to **41** and class 5 to
   **37**, and this file's table and sentence move with it. Re-derived this
   session at the baseline commit with a second method; the reviewer's
   figures reproduce exactly [Observed].
5. **"A new artifact appearing in the change directory fails `--check`" was
   false.** **Accepted and repaired.** The builder hashes a hard-coded tuple
   of eleven paths and never lists the directory. The sentence now states
   what the selftest does assert (eleven named paths; any change to an
   unpatched one fails) and that a twelfth file is outside the bound subject.
   No directory scan was added: the manifest is the bound subject, and a
   scan would make the act's argument depend on files it does not hash.
6. **A paraphrase presented as a quotation (OQ-5).** **Accepted in round
   2; that repair withdrawn in round 3.** The round-2 repair attributed the
   sentence to the M4 funnel's Q7 cell as "M4's words, not M2's"; round 3
   re-read the source and found the sentence in M2's own Q6 cell (line 50),
   which M4 quotes, so the original attribution to M2 had been correct and
   the repair made it false (round 3 finding 11). The sentence is now
   attributed to M2 with its line, M4's quotation of it is noted, and M2's
   success criterion 4 (not "step 4") is quoted beside it.
7. **The registration sentences were stale at `9d74185`.** **Accepted and
   marked at the sentence.** `IMPACT-LEDGER.md` and `OWNER-DECISION-PACKET.md`
   now carry a dated note that the three edits landed at the merge of PR #52
   with the chain link deliberately withheld, and name the files that own
   that fact; the drafted text stays beneath, unedited.
8. **§Review named three edited files; four changed.** **Accepted and
   repaired** above: `REVIEW-BRIEF.md` is named, with its criteria
   byte-identical.
9. **Quotation drift on "is edited on no arm" for P-74.** **Accepted and
   repaired** in all three prose files: each row's own closing sentence is
   quoted. The `**is**` / `**are**` emphasis those quotations carried until
   2026-09-23 was the round-2 raw's own rendering, not the record's, and is
   dropped in all six sites (round 3 finding 12).
10. **"changes the proposed bytes" overstated.** **Accepted and repaired.**
    `OWNER-DECISION-PACKET.md` now says "may change", matching this file.

### A parallel independent round 2, retained beside it

Added 2026-09-23 after round 3 was dispatched over `76b4beb`, so round 3's
verdict does not cover this paragraph. A second lead session dispatched its
own fresh-context confirmation over the same package bytes at main commit
`dfb605c` (byte-identical to `9d74185` for this package) before the two
sessions coordinated. Its raw is retained verbatim as
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-B-RAW.md`
(CC-REV-6; a second reviewer run is a second file, never a replacement).
**Verdict:** **CONFIRM WITH EXCEPTIONS**, copied exactly. Its finding A is
the P-74 quotation drift that round 2's finding 9 also found, repaired
above; its finding B is editorial and needs no change. It did not test the
continuation-form sweep or the directory-scan sentence, so the two REVISE
findings of round 2 stand as the verdict of record for that commit's bytes:
two independent readers of the same bytes returned different words, and
this file records both rather than the more favourable one.

**What no round-2 disposition changed.** No patch byte, no manifest row, no
requirement, no scenario text. All five open questions are now answered by
plain owner direction, performing no act: OQ-1 and OQ-2 in
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
and OQ-3 to OQ-5 in
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`
(both 2026-09-23). None of the answers changed a proposed byte: OQ-2 is
placement (A), the drafted host; OQ-3 keeps PWB-REQ-007 and leaves the
secondary counts to slice 3's code; OQ-4 routes the POC-REQ-032 question to
the `syzygy-dov.26` package; OQ-5 is a design value for slices 2 and 3
(project-level categories first, then the band: currency probe, then the
Unknown aggregate), which the scenario's wording is compatible with and
which this package does not write into the specification.

### Round 3 — re-review over the round-2 repairs

**Reviewed bytes:** commit `76b4beb`, with the manifest digest quoted in
`OWNER-DECISION-PACKET.md`. **Reviewer:** a fresh-context session with no
authoring context, commissioned 2026-09-23 with the round-1 and round-2
raws and their dispositions as input and `REVIEW-BRIEF.md` as its
commission. **Verdict:** **REVISE**, copied exactly from the retained raw
output. **Raw output:**
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-2-RAW.md`,
retained verbatim and never edited (CC-REV-6).

The reviewer found round-2 findings 4, 5, 7, 8 and 10 discharged with
truthful dispositions, 9 discharged in substance, and 6 not discharged
because the repair had replaced a correct attribution with a false one;
reproduced every figure of finding 4 by two methods; found no byte of the
patches, the manifest or the builder moved in three rounds; and checked the
five owner answers against their records. The REVISE rests on three new
findings (11, 13, 14); findings 12 and 15–18 are notes. **Rule 10:** the
repairs below edited `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`,
`OWNER-DECISION-PACKET.md` and `REVIEW-BRIEF.md` after that commit; no
patch or manifest byte moved. These bytes carried no confirmation until a
round 4 read them; it did, and returned REVISE (next section).

**Dispositions**, finding by finding:

11. **The round-2 repair for finding 6 turned a correct quotation into a
    false attribution.** **Accepted and repaired**, above at OQ-5 and in
    disposition 6: the sentence is M2's (Q6 cell, line 50), M4 quotes it,
    and the "step 4" label now reads "success criterion 4". Verified at
    source this session before the repair was written.
12. **Emphasis markers inside verbatim quotations.** **Accepted and
    repaired** in all six sites across the three prose files; disposition 9
    no longer says "verbatim".
13. **The class-5 remainder is 39 by the ledger's own arithmetic, stated
    as 37.** **Accepted and repaired** in `IMPACT-LEDGER.md` class 5: the
    41 citers were re-swept at `a4a3451` this session and every hit placed;
    the remainder is stated as 41 less the two class-1 files, the paths
    behind "dated evidence records (12)" are named, and the two unplaced
    citers (`docs/PWB-IMPLEMENTATION-PLAN.md` and
    `docs/reviews/2026-09-09-polaris-editorial-repair.md`) have a kind of
    their own. The impact conclusion is unchanged: neither carries an
    obligation the scenario changes.
14. **The packet head reported one review and one verdict.** **Accepted and
    repaired**: the head now names every round, its verdict word and its
    raw, says this file owns the dispositions, and says a round 4 is what
    the bytes await; step 1 of "What would happen next" is updated to match.
15. **"Slices 4 and 5 still need OQ-1 answered."** **Accepted and
    repaired** in the packet to the delta's form: they need the
    `syzygy-dov.26` amendment the answer routes them to.
16. **"Not drafted at this commit" was true at the baseline and stale as
    the live state.** **Accepted and marked at the sentence**: the ledger
    now says "at the baseline commit", names the sibling
    `pwb-missing-currency-disclosure-scenario/` as drafted since, and states
    the composition result, re-derived this session.
17. **"Plus this package's own untracked files" could not be true of the
    published figures.** **Accepted and repaired**: the sentence now says
    the figures are over the tracked files of the baseline commit, except
    where a paragraph names another population.
18. **The §Review head's verdict was unqualified by round.** **Accepted and
    repaired**: "Round 1 verdict:".

**What no round-3 disposition changed.** No patch byte, no manifest row, no
requirement, no scenario text, and no owner answer.

**Author's standing:** this draft's author dispositioned these findings and
authored the repairs, and therefore may run no review of them.

### Round 4 — re-review over the round-3 repairs

**Reviewed bytes:** commit `194f8cd`, with the manifest digest quoted in
`OWNER-DECISION-PACKET.md`. **Reviewer:** a fresh-context session with no
authoring context, commissioned 2026-09-23 with the four earlier raws and
their dispositions as input and `REVIEW-BRIEF.md` as its commission.
**Verdict:** **REVISE**, copied exactly from the retained raw output. **Raw
output:**
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-3-RAW.md`,
retained verbatim and never edited (CC-REV-6).

The reviewer found every round-3 item — finding 6 and findings 11 to 18 —
discharged with truthful dispositions; reproduced every ledger figure by
two methods; found the manifest, both patches and the builder
byte-identical from `76b4beb` to `194f8cd`; composed the spec patch with
all four sibling spec patches in both orders; regenerated the coverage
views over the proposed spec and found them equal to the tree; and caught
six scratch mutations. The REVISE rests on one new finding (20); findings
19, 21 and 22 are notes. **Rule 10:** the repairs below edited
`SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md` and
`REVIEW-BRIEF.md` after that commit; no patch or manifest byte moved.
These bytes carry no confirmation until a round 5 reads them.

**Dispositions**, finding by finding:

19. **Migration step 1 of this file still said "Done twice" and named a
    round 3 as the next step.** **Accepted and repaired**: the step now
    names all four rounds and their verdict words and says a round 5 is
    the next step. The round-3 repair of finding 14 fixed the packet's
    parallel step and missed this one.
20. **A manifest row carries `PWB-REQ-010`, and the ledger said twice that
    it does not.** **Accepted and repaired.** The round-3 repair had
    written "no class-2, class-3 or class-4 file carries the identifier
    except `CAPABILITY-COVERAGE.md`", widening the round-3 raw's own
    class-3-and-4 sentence to class 2 without re-sweeping the eleven rows;
    `contract-coverage-matrix/RFC-0007-0009.md` is manifest row 8 and
    carries the literal four times at `a4a3451` [Observed — re-swept at
    source]. The pre-existing kind sentence, "the first is a manifest row;
    the other three are outside the bound eleven", was false for the same
    file. Both sentences now name both class-2 citers and mark the earlier
    text; no figure, kind count or placement moved — the file was already
    counted once, in "generated coverage views (4)".
21. **The `polaris.ts` line range for `gapReasonCounts` was stale at the
    reviewed commit.** **Accepted and repaired** at both sites: the
    function is cited by name with its range at `194f8cd` and at the
    baseline, since the file moves under commits outside this package.
22. **Two quoted line positions in the reconciliation section were off by
    one and by two at every commit since drafting.** **Accepted and
    repaired**: 472 and 836, re-read at source; the quoted words were
    exact and are unchanged.

**What no round-4 disposition changed.** No patch byte, no manifest row, no
requirement, no scenario text, and no owner answer.

**Author's standing:** this draft's author dispositioned these findings and
authored the repairs, and therefore may run no review of them.

### Round 5 — re-review over the round-4 repairs

**Reviewed bytes:** commit `7fd2db3`, with the manifest digest quoted in
`OWNER-DECISION-PACKET.md`. **Reviewer:** a fresh-context session with no
authoring context, commissioned 2026-09-23 with the five earlier raws and
their dispositions as input and `REVIEW-BRIEF.md` as its commission, and
asked for an exhaustive internal cross-reference sweep with a stated
denominator. **Verdict:** **REVISE**, copied exactly from the retained raw
output. **Raw output:**
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-4-RAW.md`,
retained verbatim and never edited (CC-REV-6).

The reviewer found all 22 prior findings dispositioned truthfully; swept
496 extracted pointers over the four prose files and found every filename,
commit token, section, finding, step, row and round reference resolving,
with three line ranges imprecise (24–26); re-derived every ledger figure by
two methods over 1,334 tracked blobs at `a4a3451` and found all reproduce;
found the manifest, both patches and the builder byte-identical across all
five reviewed commits; composed the spec patch with all four sibling spec
patches in both orders; and caught eight scratch mutations. The REVISE
rests on one new finding (23); findings 24 to 30 are notes. **Rule 10:**
the repairs below edited `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md`
and `REVIEW-BRIEF.md` after that commit; `IMPACT-LEDGER.md` and every
patch and manifest byte are unchanged. These bytes carry no confirmation
until a round 6 reads them.

**Dispositions**, finding by finding:

23. **The round-1 section said all fourteen machine items of the round-1
    raw "still hold at this commit"; two do not.** **Accepted and
    repaired.** Item 9's continuation-form figure (0/0) was retracted by
    round 2 finding 4 and item 13's `polaris.ts` range moved (round 4
    finding 21); the sentence was true at `9d74185` and went false when
    the round-2 repair moved the ledger's figure. It now anchors the claim
    to the round-1 disposition commit, excepts the two items, and keeps the
    superseded wording marked in place.
24. **RFC2-26's quotation was pointed at the clause's opening line, not
    the quoted sentence.** **Accepted and repaired**: lines 201–205, inside
    the clause defined at line 196. The words were exact.
25. **The M4 slice 3–5 range ended on slice 6's heading.** **Accepted and
    repaired**: 820–913.
26. **The M2 slice 2 range was a fragment of the slice.** **Accepted and
    repaired**: 441–513, with the two quoted passages placed at 443–446
    and 472–475.
27. **The delta took the wider reading of PWB-REQ-020's population without
    naming the narrower one the M2 funnel flags.** **Accepted and
    repaired** at "What does NOT change" item 3: both readings are now
    named with the funnel's own words and the spec Case quoted, the wider
    reading is identified as the one this change lands under, and the
    choice is left to the owner rather than settled here. No OQ-6 is
    minted: OQ-1 to OQ-5 are answered by record and a sixth would reopen
    the packet's answered set; the owner may raise one.
28. **The packet's head banner did not itself name the act.** **Accepted
    and repaired**: one sentence added to the banner naming the dedicated
    amendment act on this manifest's digest; the lower paragraphs already
    named it.
29. **An unmarked paraphrase of the proposal's subject.** **Accepted and
    repaired**: marked as a paraphrase with its source section named.
30. **The current source digest appears in the declaration patch's removed
    line while the ledger says it is reproduced in no prose.** **Accepted,
    no change**: a unified diff carries the line it removes and is not
    prose; CG-7e and CG-15 pass on these bytes.

**What no round-5 disposition changed.** No patch byte, no manifest row, no
requirement, no scenario text, no ledger figure, and no owner answer.

**Author's standing:** this draft's author dispositioned these findings and
authored the repairs, and therefore may run no review of them.

### Round 6 — re-review over the round-5 repairs

**Reviewed bytes:** commit `2c5745e`, with the manifest digest quoted in
`OWNER-DECISION-PACKET.md`. **Reviewer:** a fresh-context session with no
authoring context, commissioned 2026-09-23 with the six earlier raws and
their dispositions as input and `REVIEW-BRIEF.md` as its commission, asked
to check each round-5 repair for truth and to repeat the cross-reference
sweep with a denominator. **Verdict:** **REVISE**, copied exactly from the
retained raw output. **Raw output:**
`docs/reviews/R-PWB-OPENING-BAND-SCENARIO-DELTA-CONFIRMATION-5-RAW.md`,
retained verbatim and never edited (CC-REV-6).

The reviewer found every round-5 range repair exact; swept 592 extracted
pointers over the four prose files with none failing to resolve; found
findings 1 to 30 dispositioned truthfully except the count inside the
round-5 repair of 23; reproduced every ledger figure by two methods at
`a4a3451`; found the manifest, both patches and the builder byte-identical
across all six reviewed commits; composed the spec patch with all four
sibling spec patches in both orders; ran `--diff` and matched it to the
two patch files; and exercised nine scratch mutations. The REVISE rests on
one new finding (31); findings 32 to 35 are notes. **Rule 10:** the
repairs below edited `SEMANTIC-DELTA.md`, `OWNER-DECISION-PACKET.md` and
`REVIEW-BRIEF.md` after that commit; `IMPACT-LEDGER.md` and every patch
and manifest byte are unchanged. These bytes carry no confirmation until a
round 7 reads them.

**Dispositions**, finding by finding:

31. **The round-5 repair of finding 23 excepted two items for moved
    pointers and missed a third, and its bracket claimed a re-read the
    round-5 raw does not record.** **Accepted and repaired.** Item 15's
    three `check_governance.py` pointers moved at `9d74185` by the same
    test that excepted item 13; the sentence now names all three, gives
    the population as thirteen (items 2–10 and 13–16 — both the round-5
    repair and the reviewer wrote fourteen, and neither count was
    derived), and states per item what evidence covers the other ten,
    with `--diff` re-run this session for item 5. The superseded round-5
    wording is marked in place beside its predecessor.
32. **The Evidence bullet for `gapReasonCounts` pointed at finding R-3
    instead of OQ-3.** **Accepted and repaired**, with the earlier wording
    marked.
33. **The PWB-REQ-020 two-readings passage is a surfaced tension with
    exact quotations, left to the owner.** **Noted, no change**: this is
    the form round 5 finding 27 asked for.
34. **The packet's date line said "repaired 2026-09-21" for dispositions
    committed 2026-09-22 01:11 +0800.** **Accepted and repaired**: the
    line now reads 2026-09-22 and 2026-09-23, with the earlier date
    marked as the author's working date.
35. **M4's Gate 5 table is headed "Limb 1" while its slice-3 cell discusses
    limb 2.** **Noted, no change**: the inconsistency is the funnel's, and
    the funnel is read-only to this package; the delta reports the header
    faithfully.

**What no round-6 disposition changed.** No patch byte, no manifest row, no
requirement, no scenario text, no ledger figure, and no owner answer.

**Author's standing:** this draft's author dispositioned these findings and
authored the repairs, and therefore may run no review of them.
