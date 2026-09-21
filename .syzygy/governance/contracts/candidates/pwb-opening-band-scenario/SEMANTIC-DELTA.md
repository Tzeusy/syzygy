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

`PWB-REQ-007`'s aggregate sentence and its Observable (lines 444–458):

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
   "or disclosure Polaris presents".
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
  820–914); Gate 5's subsection "The RFC2-26 test for slices 4 and 5" (line
  1210 onwards) with its eight-row table.
- `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` lines 441–480 — slice
  2, the currency probe.
- `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` lines 903–935 — slice 3,
  "One real Unknown in the first reading".
- `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
  lines 196–221 — RFC2-26, quoted in the reconciliation below at the defined
  clause (`DIRECTIVE-REGISTER.md` line 260 gives that definition site).
- Both signed specifications, read for the requirement and scenario
  populations.
- `apps/three-surface-poc/src/polaris.ts` lines 922–931 — the
  `gapReasonCounts` projection, for finding R-3 below.

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

and, at line 473:

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

and, at line 838:

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
(`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md` line
196):

> Before implementation, every observable consequence either maps to an
> approved OpenSpec requirement and scenario in the governance root's
> `openspec/**` plane, or carries a reviewed N/A judgment proving it purely
> structural with no independently testable behavior.

The M4 funnel's own table gives slice 4's mapping as "**None** — the three
sweeps above find no requirement naming the field" and slice 5's as "**None**
— the three sweeps above find no requirement reaching the home route", both
"**Unavailable**, both limbs". Slice 4's consequence is a declared surface
population; slice 5's is the home route. Neither lies within this
specification's subject, which its own proposal states as the declared shape
of the configured project; and the sweeps behind those two cells returned zero
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
which collides on the same lines as two other live changes — lane B's
`proposed/spec.md.patch` hunks cover lines 450–471 and 473–483, which contain
PWB-REQ-007's only scenario at line 470, and P-69 Q7a's clarification scenario
(gate `syzygy-dov.20`) is destined for the same requirement; (c) minting a new
requirement, which would give the consequence its own clause and its own
scenario but is not "one CC-REV-2 scenario" and would move the requirement
count, the proposal's stated totals and the coverage matrices. The reading not
taken: asserting that (a) is sufficient. It is stated as a question.

**OQ-3 — the designed band does not satisfy the clause it inherits.**
PWB-REQ-007 requires an aggregate to disclose "separate primary/secondary
reason counts". The projection party 3 reuses counts primary reasons only —
`gapReasonCounts` in `apps/three-surface-poc/src/polaris.ts` lines 922–931
reads `claim.epistemic.reasons.primary` and increments one map [Observed at
source this session]. So the band as M4 designs it, rendering that map, would
falsify the scenario's third bullet. This delta keeps the clause's words
rather than the design's, which means the implementation must supply the
secondary counts. The reading not taken: softening the third bullet to
"reason counts" so that today's projection would pass — that would quietly
narrow PWB-REQ-007 through a scenario under a different requirement.

**OQ-4 — an opening aggregate against POC-REQ-032's "in place".** The
three-surface specification's POC-REQ-032 says, quoted at
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
line 578: "where the model is Unknown, the narrative SHALL disclose the
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
criteria", and M2 slice 2's stated target that "the page's first human-visible
instant moves from 58.0% depth into the opening band". The scenario says only
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
| continuation forms of it | 0 | 0 |
| the patched `spec.md` path | 51 | 113 |
| the patched `GOVERNING-DEPENDENCIES.md` path | 9 | 13 |
| the current `spec.md` digest | 13 | 13 |

The continuation sweep adds no file over the full-identifier sweep; every
file it would have matched also matches pattern 1 [Observed, both sweeps run
this session].

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
  ruled in P-74 Q4 and P-78 Q4 that the registry entry "is edited on no arm"
  of those moves, and P-69 Q2(a) and P-72 Q2 travel together as one
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
   (rule 10).
2. The owner answers the five open questions in `OWNER-DECISION-PACKET.md`.
   Answers to OQ-2 or OQ-3 may change the proposed bytes, which retires the
   review and needs a fresh one.
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

**Reviewer:** not yet assigned. Must not have authored these bytes or shared
the drafting session.

**Verdict:** none. No review has been run against this package. Per the
normative-change workflow this delta stops at step 2; the drafting agent did
not review its own work, and the absence of a verdict here is the honest
state, not an omission [Observed].
