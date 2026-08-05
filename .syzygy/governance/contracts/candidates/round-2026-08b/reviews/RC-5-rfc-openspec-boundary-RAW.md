# RC-5 — RFC/OpenSpec boundary review (raw reviewer output)

**Reviewer:** independent fresh-context session. No authoring history read; no
`_bootstrap/` directory read.
**Date of review:** 2026-08-05
**Primary artifact:** `.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md`
**Secondary:** `09-OPEN-SPEC-READINESS-REPORT.md`; RFCs 0006–0011 (all modules).

---

## 0. Method (stated so every count below is reproducible)

`grep` on this machine is ugrep and silently mismatches `[^]]`-style classes, so
**every count in this report was produced with Python `re`**, never with grep.
Two independent enumerations were run and cross-checked:

1. **Clause definitions in the RFC bytes.** Regex
   `^\*\*(RFC\d+-\d+)(\([a-z]\))?\s*(?:\.|—|-)` over all files under
   `candidates/rfcs/`, plus the lettered-limb admission rule
   (`^\*\*(RFC(\d+)-\d+)(\([a-z]\))\s` admitted only when the file's front-matter
   `id` matches the clause's RFC number **and** the parent integer clause is
   defined in the same file). This is the same rule
   `scripts/build_contract_index.py` uses; I re-implemented it rather than
   importing it, so the two are independent runs of one rule.
2. **Matrix rows.** Regex `^\|\s*(RFC(\d+)-\d+(?:\([a-z]\))?)\s*\|\s*([^|]*?)\s*\|`
   over `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md`, capturing the clause ID and the
   Class column.

Cross-check against the committed projection `05-CONTRACT-INDEX.yaml`: 344 clause
entries, 344 unique, per-RFC counts identical to enumeration (1). **The three
methods agree exactly.** `scripts/verify_final_prespec.py` reports "numbered
clauses defined: 322" — that figure counts *integer* clauses only, excluding the
9 lettered sub-clauses; 344 is the same corpus counted inclusively. Both are
correct under their own convention. This report uses the **inclusive**
convention throughout, because that is the convention the routing matrix's own
row set uses (it carries rows for `RFC7-11(a)`, `RFC9-8(a)`, `RFC9-9(a)`,
`RFC9-9(b)`, `RFC9-13(a)`, `RFC9-14(a)`, `RFC9-15(b)`, `RFC9-16(d)`,
`RFC9-47(a)`).

**Convention for "routed."** The task defines four routing categories:
(a) future OpenSpec requirement/scenario, (b) pure structural invariant —
reviewed N/A, (c) craft/release policy, (d) informative rationale. The matrix
uses five *classes*: DI, OS, CR, IR, DI+OS. The mapping is **not** one-to-one,
and the matrix itself says so:

> `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:229–231` — "the DI/OS classification
> here is a **routing aid only** — a DI or CR class never exempts a clause's
> observable consequences from OpenSpec coverage."

So **DI ≠ category (b)**. A DI row is not a reviewed N/A judgment; it is an
explicit deferral of the routing decision to a future coverage matrix. I score
a clause as *routed* only where its row places it in (a), (c) or (d):
OS and DI+OS → (a); CR → (c); IR → (d). DI rows are scored **unrouted**, and
this is the matrix's own reading, not mine.

---

## 1. COMPLETENESS OF ROUTING — and the RFC-0006 question

### 1.1 The corpus-level numbers

| | count |
|---|---|
| Clauses defined in RFCs 0006–0011 | **187** |
| Clauses with a row in the matrix | **159** (RFC 0007–0011 only) |
| Clauses in category (a) — OS or DI+OS | **22** (5 OS + 17 DI+OS) |
| Clauses in category (c) — CR | **8** |
| Clauses in category (d) — IR | **0** (matrix line 334: "no clause was found to be pure INFORMATIVE-RATIONALE") |
| Clauses in category (b) — reviewed N/A | **0** |
| **Routed into one of the four categories** | **30 / 187 = 16.0%** |
| **Unrouted** | **157 / 187 = 84.0%** |

Of the 157 unrouted, **129** are DI rows in the matrix and **28** are RFC-0006
clauses with no row at all.

Class tallies, machine-recounted: RFC 0007 — DI 28, DI+OS 6, OS 1, CR 4, 39
rows. RFC 0008 — DI 30, DI+OS 1, OS 1, CR 0, 32 rows. RFC 0009 — DI 50,
DI+OS 3, OS 3, CR 4, 60 rows. RFC 0010 — DI 11, DI+OS 5, 16 rows. RFC 0011 —
DI 10, DI+OS 2, 12 rows. **These reproduce the matrix's own Tallies block
(`:321–327`) exactly.** The matrix's arithmetic is correct; its scope is the
problem, not its counting.

### 1.2 RFC-0006 — the suspicion is confirmed against the bytes

**[Observed] RFC-0006 defines 28 clauses (RFC6-1 … RFC6-28, no gaps) and the
routing matrix contains ZERO rows for any of them.** The regex sweep over the
matrix returns rows for RFC numbers 7, 8, 9, 10, 11 only. There is no RFC-0006
section, no RFC6-n row, and no per-clause classification anywhere in the file.

This is **disclosed, not concealed**. The matrix says so itself:

> `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:233–236` — "**This matrix routes
> RFC 0007–0009 and RFC-0010/0011; RFC 0006's clause-level routing (including its
> `spec/selection-api` material) is a surface-specification deliverable under
> RFC6-28's coverage matrix, not re-enumerated here.**"

and the coverage skeleton carries an empty row:

> `:305` — "| spec/selection-api | RFC 0006 clause routing — deliverable of
> RFC6-28's coverage matrix |"

and the gap is already tracked as an open owner decision:

> `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:57` (P-10) —
> "**What remains genuinely uncovered:** RFC-0006 has *no* clause-level routing
> classification at all… Accept the deferral to RFC6-28's coverage matrix at
> surface specification, or commission the classification now".

So the finding is not "hidden defect." The finding is **structural**: the
`09-OPEN-SPEC-READINESS-REPORT.md:37–39` sequence makes `spec/selection-api` the
**first** OpenSpec changeset — "Every surface and every machine client consumes
it; smallest surface area; unblocks parity testing for everything after" — and
that is precisely the one domain for which the routing input does not exist.
The routing preparation is inverted with respect to its own recommended order.

### 1.3 Every unrouted RFC-0006 clause, enumerated

All 28 are unrouted. One line each: what it says, and which of the four
categories it belongs in on my reading. Paths are
`.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`.

| Clause | line | What it says | Category |
|---|---|---|---|
| RFC6-1 | 92 | Selection reference is (entity kind, durable identity), optionally evaluation- and scenario-qualified; no surface-local handle (file path, node index, row, coordinate) is ever a selection identity, and every private handle resolves before crossing a surface, URL or endpoint | **(a)** `spec/selection-api` — the handle-rejection rule is a testable endpoint/URL behavior; the "kernel mints nothing new" limb is (b) |
| RFC6-2 | 102 | Every V0-core entity is selectable; selection targets the durable identity level, the evaluation qualifier picks the instance | **(a)** — a coverage scenario per entity kind |
| RFC6-3 | 108 | One reference resolves identically in all three surfaces; a surface that can only answer at a different evaluation must render the skew naming **both** evaluation identities | **(a)** — a directly testable cross-surface scenario |
| RFC6-4 | 114 | Unqualified selection resolves at the latest identified evaluation and the answer names it; there is no unstamped answer | **(a)** |
| RFC6-5 | 124 | Total resolution: nine typed outcomes in a closed table with per-outcome obligations; silence, empty panel, dropped selection, bare 404 or unexplained error are violations | **(a)** — nine scenarios minimum; the highest-value single row in the corpus |
| RFC6-6 | 143 | Navigation outcomes are not RFC2-24 Unknown reasons and are never counted among them | **(a)** — a countable, testable separation |
| RFC6-7 | 150 | Resolution is deterministic per (reference, evaluation, scenario); only display formatting is excluded | **(a)** — a two-run determinism check |
| RFC6-8 | 157 | What a URL pins: (project, selection reference, optional evaluation, optional scenario) + presentation hints that never affect resolution; stripping hints yields the same answer | **(a)** — testable; URL *spelling* is deliberately unbound, which is the (b) limb |
| RFC6-9 | 167 | Rename-stability: URLs embed durable identifiers; rename, file move, or re-layout changes no URL | **(a)** |
| RFC6-10 | 173 | Two URL temporalities: evaluation-pinned URLs are permanently stable with staleness visible; unpinned resolve latest; which-one-this-is must be visible | **(a)** |
| RFC6-11 | 181 | A URL to a retired identity resolves `retired` with retirement record and successors — never a 404, never a silent redirect | **(a)** — has its own §4 violation case (line 419) already written as a test |
| RFC6-12 | 190 | URLs are surface-independent; same body + different surface hint is the same selection; bookmarks honored across surfaces | **(a)** |
| RFC6-13 | 198 | Machine endpoints answer from the same kernel fact set the surfaces render; no endpoint-only and no UI-only facts, bidirectionally | **(a)** — the parity property everything else in the readiness sequence rests on |
| RFC6-14 | 206 | Label parity: every entity/claim/aggregate in a machine answer carries label + tier + Unknown reason + freshness verbatim, plus sibling surface states and `challenge-pending` | **(a)** |
| RFC6-15 | 221 | Every answer is evaluation-stamped; same evaluation + same filters ⇒ same answer; an answer that cannot name its evaluation is not an answer | **(a)** |
| RFC6-16 | 227 | Filters are declared scope, carried in the answer envelope; a partial result is never presented as full scope | **(a)** |
| RFC6-17 | 233 | Aggregation discloses membership count and the full RFC6-22 equivalence tuple (per-label, per-tier over all six tiers, per-reason, per-freshness, plus sibling states) and supports expansion | **(a)** — the tier enumeration makes this a literal assertion set |
| RFC6-18 | 252 | One fact set per (reference, evaluation, scenario); surfaces may differ in presentation, never in which facts exist; divergence is a kernel defect | **(a)** |
| RFC6-19 | 262 | Drawer content classes 1–7 (identity, epistemic state, evidence, provenance, warrant, challenge/contradiction state, policy visibility), each with sub-obligations | **(a)** — seven scenario families; this is a response-shape enumeration |
| RFC6-20 | 293 | Every internal link in the fact set resolves; doctrine/contract citations render by stable identifier and resolve if rendered as links; external URLs classified external | **(a)** |
| RFC6-21 | 302 | Minimal display is a presentation depth, not a fact-set subset; endpoints always serve the full set | **(a)** |
| RFC6-22 | 310 | The equivalence definition — the exact tuple two renderings must share to be equivalent | **(a)** (the tuple is arguably a shared vocabulary, i.e. partly (b), but it is the assertion set every parity test is written against) |
| RFC6-23 | 319 | Finer detail is allowed and must be disclosed as an aggregation difference; disagreement on existence, edge, label, tier, reason, freshness, sibling state, context, or count is release-blocking | **(a)** + **(c)** — the release-blocking limb is craft/release policy |
| RFC6-24 | 330 | Scenario context is explicit and singular: Base / Proposed / Historical, with the non-default-revision marker, the exclusivity refusal, and the historical-access rule | **(a)** |
| RFC6-25 | 362 | Context travels with the selection through sync, URLs and answers; silent context swap is a violation | **(a)** |
| RFC6-26 | 370 | Unconsented resolution renders Unknown (`unconsented-source-or-provider`) as a policy state with its resolution route, never as failure or empty region | **(a)** |
| RFC6-27 | 379 | Excluded content renders as *excluded* with a count, never absent; nothing derived from excluded content reaches any surface, drawer or endpoint | **(a)** |
| RFC6-28 | 387 | The phase rule itself — this contract schedules nothing; every observable consequence of RFC6-1…27 maps to an approved requirement or a reviewed N/A; a coverage matrix is a surface-specification deliverable | **(b)** — genuinely self-N/A: the clause's only effect is on scheduling |

**Summary for RFC-0006: 27 of 28 clauses belong in category (a); 1 (RFC6-28) is
a true (b). Zero are currently routed.** There is not a single clause in this
contract that a first-pass classification would have to think hard about, which
makes the omission a scope decision rather than a difficulty.

---

## 2. UNROUTED ELSEWHERE — the per-RFC table

Inclusive clause convention (lettered sub-clauses counted as clauses, matching
the matrix's own row set and `05-CONTRACT-INDEX.yaml`).

| RFC | clauses defined | routed | unrouted | unrouted IDs |
|---|---|---|---|---|
| RFC-0006 | 28 | 0 | 28 | RFC6-1 … RFC6-28 (all; see §1.3) |
| RFC-0007 | 39 | 11 | 28 | RFC7-1, RFC7-2, RFC7-3, RFC7-4, RFC7-6, RFC7-7, RFC7-8, RFC7-9, RFC7-11, RFC7-11(a), RFC7-12, RFC7-14, RFC7-15, RFC7-18, RFC7-19, RFC7-20, RFC7-21, RFC7-23, RFC7-24, RFC7-26, RFC7-27, RFC7-28, RFC7-29, RFC7-33, RFC7-35, RFC7-36, RFC7-37, RFC7-38 |
| RFC-0008 | 32 | 2 | 30 | RFC8-1, RFC8-2, RFC8-3, RFC8-4, RFC8-5, RFC8-6, RFC8-7, RFC8-8, RFC8-9, RFC8-10, RFC8-11, RFC8-12, RFC8-13, RFC8-15, RFC8-16, RFC8-17, RFC8-18, RFC8-19, RFC8-21, RFC8-22, RFC8-23, RFC8-24, RFC8-25, RFC8-26, RFC8-27, RFC8-28, RFC8-29, RFC8-30, RFC8-31, RFC8-32 |
| RFC-0009 | 60 | 10 | 50 | RFC9-1, RFC9-2, RFC9-3, RFC9-4, RFC9-5, RFC9-6, RFC9-7, RFC9-8, RFC9-8(a), RFC9-9, RFC9-9(a), RFC9-9(b), RFC9-10, RFC9-11, RFC9-12, RFC9-13(a), RFC9-14, RFC9-14(a), RFC9-15, RFC9-15(b), RFC9-16, RFC9-16(d), RFC9-17, RFC9-18, RFC9-19, RFC9-20, RFC9-21, RFC9-22, RFC9-23, RFC9-25, RFC9-26, RFC9-27, RFC9-28, RFC9-29, RFC9-30, RFC9-31, RFC9-34, RFC9-35, RFC9-37, RFC9-38, RFC9-39, RFC9-40, RFC9-42, RFC9-43, RFC9-44, RFC9-46, RFC9-48, RFC9-50, RFC9-51, RFC9-52 |
| RFC-0010 | 16 | 5 | 11 | RFC10-1, RFC10-2, RFC10-3, RFC10-6, RFC10-8, RFC10-9, RFC10-10, RFC10-11, RFC10-14, RFC10-15, RFC10-16 |
| RFC-0011 | 12 | 2 | 10 | RFC11-2, RFC11-3, RFC11-4, RFC11-5, RFC11-6, RFC11-7, RFC11-8, RFC11-9, RFC11-11, RFC11-12 |
| **TOTAL** | **187** | **30** | **157** | — |

Five of the 157 (RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12) are the
phase-rule clauses themselves and are defensibly self-N/A. **The remaining 152
carry no routing decision.**

For contrast, expressed as "has a row in the matrix at all": RFC-0006 0/28
(0%); RFC-0007 39/39; RFC-0008 32/32; RFC-0009 60/60; RFC-0010 16/16;
RFC-0011 12/12. Row coverage for 0007–0011 is genuinely complete and no clause
is duplicated across rows (checked: zero duplicate IDs in any section).

---

## 3. QUALITY OF N/A CLASSIFICATIONS

**There are zero explicit N/A classifications in the corpus to sample.** The
matrix's five classes contain no N/A class; the closest analogue is `DI` with
"Routes to: RFC," which reads *to a fast reader* as "stays here, needs no spec"
— and matrix lines 229–231 explicitly deny that reading. So the honest finding
for this item is: **the artifact does not perform category (b) at all**, and the
question "was N/A used because writing a spec is inconvenient?" cannot be asked
of judgments that were never made.

What I can do instead is test whether the DI class *behaves* like an unexamined
N/A — i.e. whether DI rows are in fact free of independently testable behavior.
I took a **deterministic sample**: the DI row list in file order, every 6th row,
n = 22. No cherry-picking; the sample is reproducible from the matrix bytes.

| # | Clause | Definition site | Independently testable observable behavior? |
|---|---|---|---|
| 1 | RFC7-1 | `rfcs/RFC-0007/narrative-contract.md:70` | **No** — surface charter/identity. Genuinely (b). |
| 2 | RFC7-8 | `narrative-contract.md:167` | **Partly** — "must not live in `.syzygy/cache/`" and "stays with the repository at offboarding" are checkable residence facts, not behavior. Borderline (b). |
| 3 | RFC7-15 | `narrative-contract.md:302` | **Yes** — "drafted capabilities render unadopted; unmapped code renders Unknown, never silently inferred"; "a predominantly-Unknown catalog … rendered as normal — not broken — with RFC2-24 reasons and resolution routes." Three scenarios. **Misclassified.** |
| 4 | RFC7-24 | `narrative-contract.md:433` | **Yes** — "Polaris renders that state read-only"; "No queue store exists under `.syzygy/intent/**`; no narrative store under `.syzygy/work/**`"; "each act is recorded once." **Misclassified.** |
| 5 | RFC7-35 | `rfcs/RFC-0007/rendering-and-surface.md:245` | **Yes** — "Unresolvable entries render Unknown with their reason, never dropped." A one-line scenario. **Misclassified.** |
| 6 | RFC8-3 | `rfcs/RFC-0008/identity-authority-materialization.md:85` | **Yes** — "every mutation it offers is a synchronous, attributed adapter or governance-plane act followed by a re-read — never write-locally-and-sync-later." Directly observable. **Misclassified.** |
| 7 | RFC8-9 | `identity-authority-materialization.md:201` | **Partly** — ownership boundary is structural; "Polaris renders that state read-only" is behavior (duplicated with RFC7-24). Borderline. |
| 8 | RFC8-16 | `rfcs/RFC-0008/state-vocabulary-and-cost.md:191` | **Yes, emphatically** — "Until the bound is declared, `active` is unrenderable"; claimed items render `activity-undetermined`; past the bound `stale-or-dead` with last-signal instant; heartbeat/lock label/worktree never admissible. Four scenarios. **Misclassified.** |
| 9 | RFC8-23 | `rfcs/RFC-0008/accounting-reconciliation-and-release.md:102` | **Yes** — Unknown-provenance is "a first-class, filterable, counted rendered state — never green"; and the Unknown-provenance-vs-orphaned-work routing is a decision table. **Misclassified.** |
| 10 | RFC8-29 | `accounting-reconciliation-and-release.md:237` | **Yes** — "every merged-but-unreconciled item renders 'reconciliation evidence absent / Unknown'"; nothing at V0 simulates a verdict. **Misclassified.** |
| 11 | RFC9-3 | `rfcs/RFC-0009/semantic-geography.md:68` | **Yes** — "for any selected element, the exact channel readings currently applied and the metric behind each must be reachable at the point of selection"; and the encoding-provenance affordance is explicitly *not* a drawer fact-set member — a parity assertion. **Misclassified.** |
| 12 | RFC9-8(a) | `semantic-geography.md:136` | **Yes** — portfolio layout version + registry + reorganisation events + owner gate at workspace scope; RFC9-13(a) stamp-and-refuse covers portfolio cameras. **Misclassified.** |
| 13 | RFC9-12 | `semantic-geography.md:375` | **Yes** — "same camera, same selection, same geography, visible legend swap"; any view change that moves entities is labelled. A two-line fixture. **Misclassified.** |
| 14 | RFC9-16 | `semantic-geography.md:459` | **Yes** — closed trigger set (a)–(d), each a rendered event, none a silent teleport; "a version change with no recorded rationale is not a lawful trigger." **Misclassified.** |
| 15 | RFC9-21 | `semantic-geography.md:638` | **Yes** — the exact disclosure string "N shared, counted once at project scope" on **every** rendered aggregate that includes a shared contribution. **Misclassified.** |
| 16 | RFC9-28 | `rfcs/RFC-0009/visual-grammar-and-lenses.md:143` | **Yes** — exactly one declared height meaning per active lens, always in the legend; Unknown height treatment lens-invariant. **Misclassified.** |
| 17 | RFC9-37 | `visual-grammar-and-lenses.md:286` | **Yes** — capture window renders at all times; motion stops and marks when its source stales; unmeasured factory renders visibly unmeasured; no synthesized flow. Four scenarios, deliberately bound now for a later profile. **Misclassified.** |
| 18 | RFC9-44 | `visual-grammar-and-lenses.md:434` | **Yes** — "no filter default, LOD step, lens, or profile may drop it"; the path-derived-*placement* marker; identity survives refactor. **Misclassified.** |
| 19 | RFC10-1 | `rfcs/RFC-0010-mission-control-autonomy.md:73` | **Partly** — "not a fourth truth surface" is structural; "a Mission Control view of project state is a projection of kernel answers, rebuildable and non-authoritative" is testable via §4 case 3. Borderline. |
| 20 | RFC10-10 | `RFC-0010-mission-control-autonomy.md:222` | **Yes** — "an out-of-envelope act is refused at the choke point … not performed-then-flagged"; "every guardrail decision — allow, refuse, halt — is recorded as identified evidence attributable to its mission, work item, and principal." **Misclassified.** |
| 21 | RFC11-3 | `rfcs/RFC-0011-context-compiler.md:97` | **Yes** — for governed runs a packet is required; dispatching without one, or instructing "read all project documentation," is a violation. Directly testable at dispatch. **Misclassified.** |
| 22 | RFC11-9 | `RFC-0011-context-compiler.md:164` | **Yes** — secret material never enters packets or memory; packet content crossing egress is subject to the consent gate; canonical memory never silently deleted. **Misclassified.** |

**Sample result: 17 of 22 (77%) carry at least one independently testable
observable consequence and would not survive a reviewed-N/A judgment as
written. 4 are borderline. 1 (RFC7-1) is a clean structural invariant.**

Extrapolated over 129 DI rows this implies roughly 100 clauses whose observable
consequences currently have no routing decision. Additional DI rows I checked
outside the sample and consider unambiguously behavior-bearing, with sites:
RFC7-11 (`narrative-contract.md:224`, broken anchor ⇒ Unknown, break named,
same state to machine consumers), RFC7-19 (`:369`, empty block collapses to one
honest line, never an empty heading), RFC7-33 (`rendering-and-surface.md:189`,
the `non-citable`/`presentation-artifact` attribute on **every** exported,
embedded or plain-text rendering — its own package violation case 13 is written
as a test), RFC8-13 (`state-vocabulary-and-cost.md:139`, thirteen derivations
and thirteen honest-absence behaviors), RFC8-17 (`:210`, closed blocked-cause
taxonomy with "blocked with cause Unknown" fallback), RFC8-19 (`:246`, "cost
known for n of m runs"), RFC8-30 (`accounting-…:243`, "progress aggregates …
disclose their reconciliation composition (n reconciled, m pending, k
unsatisfied, c contradiction-raised, j Unknown)"), RFC9-26
(`visual-grammar-…:88`, "a channel with no registry entry must not render"),
RFC9-27 (`:116`, Unknown never invisible at element **and** aggregate scale;
earned emptiness backed by a coverage record else `mapping-coverage-absent`),
RFC9-48 (`interaction-parity-…:231`, full keyboard navigation of an enumerated
action set), RFC10-8 (`RFC-0010:180`, attempted self-widening ⇒ `blocked` +
recorded attempt + Attention Item), RFC11-6 (`RFC-0011:128`, incomplete context
⇒ run does not launch, escalates).

**Judgment.** The DI class is not being abused as a convenience N/A — the matrix
is explicit that it grants no exemption. But the effect on a reader is the same
as an unexamined N/A, because the "Routes to" column says `RFC` and nothing
else. A reader planning work sees 129 rows that name no future artifact and no
judgment. That is the risk this review exists to find.

---

## 4. LEAKAGE — prose concrete enough to build from

The corpus is disciplined about the classic leaks: **no latency numbers, no
frame-rate targets, no HTTP verbs, no status-code specifications, no wire
formats, no query grammar, no URL spelling** anywhere in RFCs 0006–0011
(verified by regex sweep for `\d+\s?(ms|seconds|fps)`, `HTTP|JSON|REST|GraphQL|SQL|YAML`,
`\b404|200|403\b`). The three `404` hits are all *prohibitions* ("never a
404"), which is a semantic constraint, not an endpoint spec. `10%`, `90%` and
`ninety days` are illustrative inside violation cases and rationale.

What **is** concrete enough that a competent implementer could and would build
straight from it, skipping specification:

**L1 — RFC8-12's thirteen literal state values, spelled.**
`rfcs/RFC-0008/state-vocabulary-and-cost.md:81–89`: "`future`, `planned`,
`ready`, `active`, `blocked`, `review`, `merged`, `reconciled`; … one terminal
state — `closed-unmerged` … four absence values — `state-undetermined`,
`eligibility-undetermined`, `activity-undetermined`, `stale-or-dead`." Followed
at `:139–166` by a three-table derivation matrix giving, per value, Meaning /
Derivation / Honest absence. This is an enum plus a state-derivation function.
The RFC even says why: `README.md:197–202` records that leaving the value
unnamed was *rejected* so implementations would not spell it differently. The
reasoning is sound and the consequence is that RFC8-12/13 is a specification in
everything but name. **Highest-risk leak in the corpus.**

**L2 — RFC6-5's nine-outcome table with per-outcome obligations.**
`RFC-0006-…:131–141`. Outcome name, meaning, and obligation columns —
`resolved`, `resolved-absent`, `retired`, `unknown`, `not-applicable`,
`excluded`, `unconsented`, `unresolvable`, `incompatible-scenario` — with rules
like "never auto-redirect", "never render as error", "must still offer the
drawer and name the surfaces where the entity does project". Directly
implementable resolver. **And it is the contract with zero routing rows.**

**L3 — RFC6-19's drawer content classes 1–7.** `RFC-0006-…:262–291`. A
seven-part response shape with sub-fields (identity/lifecycle/succession;
label+tier+reason+freshness; evidence links with source, capture time, scope,
integrity identity; producing evaluation + typed authority + observer/adapter
identities and versions; warrants with reason and expiry; per-challenge
lifecycle state; exclusion counts and consent state). An implementer would
serialize this verbatim.

**L4 — RFC10-14's literal filesystem path.**
`RFC-0010-mission-control-autonomy.md:287`: "a governed project home —
`.syzygy/work/missions/<mission-id>/`". A concrete on-disk layout with an ID
template, in a contract whose §7 defers "workspace governance store home and
schema." The asymmetry is itself a signal that this path was not meant to be
fixed here.

**L5 — RFC10-5's mission lifecycle as a code-block state machine.**
`RFC-0010-…:121–128`, a fenced `text` block with transition arrows
(`draft → awaiting-approval → approved → running`, `running ⇄ paused`, etc.).
The clause immediately says it is provisional and freezes by OpenSpec review —
but a fenced state machine is the single most copy-pasteable artifact shape
there is.

**L6 — RFC10-7's envelope minimum-content field list.** `RFC-0010-…:156–178`.
Fourteen named fields (change classes, prohibited surfaces, maximum autonomy
level, projects/repos/paths, tools/model classes/execution profiles, budgets —
"token, monetary, wall-clock, retry, and concurrency", gates, evidence
requirements, stop/pause/cancel/expiry, checkpoint/recovery, escalation
triggers, completion predicate). A schema.

**L7 — RFC11-1's packet field list.** `rfcs/RFC-0011-context-compiler.md:69–88`.
Sixteen enumerated fields ending in "the packet's **final digest**". A schema,
and one an implementer would treat as normative because RFC11-2 makes the digest
a required Execution Record component.

**L8 — RFC10-12's Attention Item field list.** `RFC-0010-…:258–270`. Ten named
fields including "the **default and expiry if ignored**" and "on resolution, the
**resolution act and its provenance**". A schema plus a resolution protocol
("one authorizing resolution act resolves **one** item — or explicitly
enumerates each resolved item's identity and the option chosen for it").

**L9 — RFC9-9(b)'s channel registry entry, written out as a registry entry.**
`rfcs/RFC-0009/semantic-geography.md:244–277`. Source metric/domain (closed
three-value: `honored` / `not-honored` / `unknown`), update cadence, freshness,
epistemic class, evidence path, Unknown value, fail-closed behavior. This is a
filled-in instance of the registry schema RFC9-26 defines — i.e. contract prose
in the shape of data.

**L10 — RFC9-15(b) part 4's backlog partition and its rendering rule.**
`semantic-geography.md:518–535`. Two named partitions (`refresh-clearable`,
`structurally unhonorable`), plus "**The partition is mandatory, and an
unpartitioned backlog count must not render.**" That is a UI acceptance
criterion.

**L11 — RFC9-47's release-check list.**
`rfcs/RFC-0009/interaction-parity-and-release.md:106–195`. ~25 named checks,
several with fixture specifications ("run against a fixture carrying **every
chain outcome the release can produce**, co-located on one district"; "run
against a fixture that bumps the version between save and restore"; "exercised
over a portfolio fixture carrying both an observed intra-project dependency and
a declared `depends-on` edge"). This is a test plan. It is classed CR, which is
the right *category*, but its concreteness means it would be built from
directly, and the craft/release policy it routes to **does not exist** (see F6).

**L12 — RFC7-13 and RFC7-17's information architecture.**
`rfcs/RFC-0007/narrative-contract.md:278–279` ("thesis/manifesto → architecture
story → capability catalog → capability deep dive → verbatim specification
leaf") and `:338–356` (three bands — argument, contract, reality — "**Exactly
these three bands, in this order**"). Both are labelled V0 defaults under owner
decision B7, and both are the routed limbs of DI+OS rows, which is the correct
handling. Noted because they are page-layout instructions and read as such.

**L13 — RFC7-30's walkthrough script.** `rendering-and-surface.md:129–140`. Six
enumerated prompts a fresh reader must answer, plus "at least one run per
release milestone … non-visually or keyboard-only". A test procedure.

**L14 — RFC9-45's three artifacts with field lists and homes.**
`visual-grammar-and-lenses.md:459–504`. Execution record fields, judgment fields
(including the outcome vocabulary **pass / fail / insufficient-to-judge**), the
policy's required contents, and three literal governance homes. Implementable
as-is.

**L15 — named client technology.** `RFC-0010-…:84–85`: "the official `syzygy`
CLI, scripts, and agent-protocol adapters (e.g. MCP) are **clients**", repeated
at `:97` ("an MCP or equivalent adapter") and `:321` ("MCP-or-equivalent
tools"). The clause hedges ("Exact implementation language, daemon packaging,
transport … remain implementation choices; this clause binds the topology … not
the technology") and `e.g.`/`or equivalent` are doing real work. But a binary
name and a named wire protocol in contract text are the two things an
implementer treats as decided.

**L16 — RFC9-48's enumerated keyboard action set.**
`interaction-parity-and-release.md:231–238`: "full keyboard navigation of every
action — traverse, select, zoom, lens, analytical plane, scenario, drawer,
filter — without pointer or camera." No keystrokes are given, which is the right
line; the action enumeration is a keybinding backlog.

**Assessment of the leak set.** None of these are wire formats or UI
pixel-specs, and the corpus is unusually careful about the boundary it draws.
The leaks cluster in one shape: **closed vocabularies and required-field
lists**. That shape is legitimately contract material (a closed vocabulary *is*
a structural invariant), but it is also exactly what an implementer will treat
as a spec. The mitigation is not to remove them — RFC 0008's README argues
persuasively that removing them causes worse harm — but to make sure each one
appears in a coverage matrix so the requirement that *tests* the vocabulary
exists. **Of L1–L16, the ones currently carrying a routing decision are L5, L6,
L7, L8 and L12 (DI+OS rows) and L11/L14 (CR rows). L1, L2, L3, L4, L9, L10, L13,
L15 and L16 carry none.**

---

## 5. DOMAIN NAMING

**For clauses routed to a future OpenSpec domain, naming is complete: 22 of 22
(100%) name a domain.**

- 5 OS rows name their domain in the **Routes to** column: RFC7-22 →
  `spec/intent-surface`; RFC8-20 → `spec/work-surface`; RFC9-32 →
  `spec/map-lenses`; RFC9-33 → `spec/map-lenses`; RFC9-36 → `spec/map-scenes`.
- 17 DI+OS rows all name a domain, but **only 7 of 17 name it in the Routes-to
  column** (RFC10-4, RFC10-5, RFC10-7, RFC10-12, RFC10-13, RFC11-1, RFC11-10).
  The other 10 (RFC7-5, RFC7-10, RFC7-13, RFC7-16, RFC7-17, RFC7-34, RFC8-14,
  RFC9-13, RFC9-24, RFC9-41) carry the literal string "RFC; routed limb per
  rationale" and name the domain only inside the Rationale prose.

That is a self-inconsistency against the matrix's own class definition:

> `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:41` — DI + OS: "**Both columns of its
> row name their target**."

Ten of seventeen DI+OS rows do not satisfy the sentence that defines their
class. A mechanical consumer reading the Routes-to column gets `spec/…` for 12
rows out of 22 and a prose pointer for 10.

**The coverage skeleton (`:300–307`) is complete over the routed set** —
I verified it accounts for all 5 OS and all 17 DI+OS clauses, with no clause
listed twice and none omitted. Eight domains are named corpus-wide
(`intent-surface`, `work-surface`, `map-surface`, `map-scenes`, `map-lenses`,
`selection-api`, `mission-control`, `context-packets`), matching
`09-OPEN-SPEC-READINESS-REPORT.md:13`'s claim of 8.

**Category (c) naming is the weak leg: 0 of 8 CR rows name a resolvable target
artifact.** The Routes-to values are "Review/release policy" (RFC7-25),
"Release policy" (RFC7-30, RFC7-31, RFC7-32, RFC9-45), "Release policy / craft"
(RFC9-47, RFC9-47(a)) and "Craft (performance policy)" (RFC9-49). No CC-*
clause identity is cited, and **no release policy artifact exists**:
`.syzygy/governance/policies/` contains only `craft-and-care/`, whose eight
files are `agent-provenance-and-execution-evidence.md`, `engineering-bar.md`,
`interfaces-and-dependencies.md`, `observability-and-operations.md`,
`performance-and-visual-discipline.md`, `review-and-documentation.md`,
`security-and-secrets.md`, `testing-and-verification.md`. So a CR row routes to
a named-but-nonexistent home. RFC9-45 handles this well in its own text (owner
decision B12(b) binds directly in the absence of a policy) — the matrix does
not carry that nuance.

---

## 6. IS THE MATRIX FIT TO GATE THE NEXT PHASE?

**No — not as a gate. Yes — as an input, which is what it says it is.**

The matrix is explicit about its own standing: "This file is not a contract and
creates no OpenSpec changeset" (`:30`); "the coverage matrices required by those
clauses are a later, surface-specification deliverable; **this file is their
input, not their substitute**" (`:231–232`). Judged against that self-statement
the artifact is honest. Judged against the question "can I answer *may I
implement X yet?* for an arbitrary X," it answers 30 of 187 clauses and returns
nothing usable for the other 157.

### A question it answers well

> *"May I implement the V0 lens set — the Architecture and Verification lenses
> and the work/construction and freshness overlays?"*

Look up RFC9-32. Row: `| RFC9-32 | OS | spec/map-lenses | V0 lens set and
staging — product scoping; the two-field work-state consumption invariant inside
it stays DI |` (`:178`). The answer is complete and actionable in one line:
**no, not until `spec/map-lenses` carries an owner-approved requirement**; the
domain is named; the retained invariant that survives into the RFC is named; and
`09-OPEN-SPEC-READINESS-REPORT.md:51–54` even sequences the domain ("largest;
deliberately last in V0 or early V1"). A planner gets a decision, a target, and
an ordering. This is what the whole file should look like.

### A question it answers badly

> *"May I implement URL handling — pinning a selection, resolving a retired
> identity, and the never-auto-redirect rule?"*

RFC6-8, RFC6-9, RFC6-10, RFC6-11 and RFC6-12 are the governing clauses. The
matrix has **no row for any of them**. It forwards the reader
(`:233–236`) to "RFC6-28's coverage matrix," which does not exist and cannot
exist until the surface-specification phase. Meanwhile RFC6-11's text at
`RFC-0006-…:181–188` is fully implementable prose — retirement record, `succeeds`
edges, successors offered, never a 404, never a silent redirect, evaluation-
pinned URLs resolve forever — and `09-OPEN-SPEC-READINESS-REPORT.md:37–39`
tells the reader `spec/selection-api` is changeset **#1**. So the planner is
told: this is the first thing to spec, the RFC prose is complete enough to code
from, and the artifact whose job is to say "route it first" declines to
classify it. An implementer under schedule pressure resolves that in one
direction.

A second bad case, inside the routed contracts: *"May I implement `active`
liveness — the staleness bound and the `activity-undetermined` / `stale-or-dead`
rendering?"* RFC8-16's row reads `| RFC8-16 | DI | RFC | `active` needs a signal
within a declared bound; fail-closed |`. "Routes to: RFC" tells the reader the
clause stays in the RFC — which is true and unhelpful. It does not say whether
this needs a requirement (it does; it has at least four testable scenarios), it
names no domain, and it carries no N/A judgment. The reader cannot distinguish
"reviewed and found non-behavioral" from "not yet examined," and 129 rows are in
that state.

---

## VERDICT: REVISE

### Findings

**F1 [Blocking] — RFC-0006's 28 clauses carry no routing classification, and it
is the contract the readiness report sequences first.**
Verified against the bytes: 28 clauses defined
(`rfcs/RFC-0006-cross-surface-selection-query-drawer.md:92` … `:387`), 0 matrix
rows. The exclusion is stated at `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:233–236`
and tracked at `PENDING-OWNER-DECISIONS.md:57` (P-10), so it is disclosed — but
`09-OPEN-SPEC-READINESS-REPORT.md:37–39` makes `spec/selection-api` changeset #1
on the grounds that "every surface and every machine client consumes it," and
`:13` asserts "Routing prepared." Routing is *not* prepared for the first
changeset. My §1.3 classification finds 27 of the 28 clauses belong in category
(a) and one (RFC6-28) in category (b) — none is a hard call.
**Minimal fix:** add an `## RFC 0006` section to the matrix with 28 rows using
§1.3 of this report as the first pass, or — if the owner accepts the deferral —
strike "Routing prepared" from `09-OPEN-SPEC-READINESS-REPORT.md:13` and replace
it with "Routing prepared for RFC 0007–0011; RFC 0006 deferred to RFC6-28's
coverage matrix," and re-order the recommended sequence so an unrouted domain is
not #1.

**F2 [Blocking] — the DI class is not category (b), and nothing in the matrix's
own tabular surface says so.**
129 of 159 rows are DI with "Routes to: `RFC`". Matrix `:229–231` correctly
denies that DI exempts anything, but that denial lives in a prose section 200
lines below the tables, and the Routes-to column reads as a terminal
disposition. My deterministic 22-row sample (§3) finds 17 (77%) carry
independently testable observable behavior and would not survive a reviewed-N/A
judgment as written; 4 borderline; 1 genuinely structural. Extrapolated: ~100
clauses whose observable consequences have no routing decision, presented in a
column that looks like one.
**Minimal fix:** change the DI rows' Routes-to value from `RFC` to
`RFC + coverage matrix pending` (or add a sixth column `N/A judgment: not yet
made`), and add one sentence to the class table at `:37` stating that DI is a
retention decision, never an N/A judgment.

**F3 [Blocking] — `10-EXIT-REPORT.md:75` states a universal claim the matrix's
own text contradicts.**
"the routing matrix classifies all 322 clauses (DI/OS/CR/IR/DI+OS) with a
coverage skeleton". Machine-counted: the matrix carries 159 rows, covering
RFC 0007–0011 only — **150 of the 322 numbered clauses (46.6%)**, or 159 of 344
inclusive. RFC 0001–0006's 172 numbered clauses are not classified at all, and
the matrix says so at `:233–236` and `:238–253`. This is exactly the class of
claim `AGENTS.md` names ("never write a 'zero / all / 100%' claim without
running that exact sweep"). It is also the claim most likely to convince a
reader that the boundary is closed.
**Minimal fix:** replace with "the routing matrix classifies the 150 numbered
clauses of RFC 0007–0011; RFC 0001–0005 route through those contracts by
recorded judgment (`:238–253`) and RFC 0006's routing is deferred to RFC6-28's
coverage matrix."

**F4 [Non-blocking] — 10 of 17 DI+OS rows violate the class definition the
matrix states for them.**
`:41` says "Both columns of its row name their target." RFC7-5, RFC7-10,
RFC7-13, RFC7-16, RFC7-17, RFC7-34, RFC8-14, RFC9-13, RFC9-24 and RFC9-41 carry
"RFC; routed limb per rationale" and name the domain only in prose; RFC10-4/5/7/12/13
and RFC11-1/10 do it correctly (`RFC; queue rendering → spec/mission-control`).
**Minimal fix:** rewrite the 10 Routes-to cells in the RFC10/11 style —
e.g. RFC7-16 → `RFC; SDR-17 minimal-density default → spec/intent-surface`.

**F5 [Non-blocking] — nine of the sixteen most implementable passages carry no
routing row at all.**
§4 lists L1–L16. L1 (RFC8-12/13's thirteen spelled state values plus a
per-value derivation matrix, `state-vocabulary-and-cost.md:81–166`), L2 (RFC6-5's
nine-outcome obligation table, `RFC-0006-…:131–141`), L3 (RFC6-19's seven drawer
content classes, `:262–291`), L4 (RFC10-14's literal
`.syzygy/work/missions/<mission-id>/`, `RFC-0010-…:287`), L9 (RFC9-9(b)'s
filled-in registry entry, `semantic-geography.md:244–277`), L10 (RFC9-15(b)
part 4's mandatory backlog partition, `:518–535`), L13 (RFC7-30's six-prompt
walkthrough script, `rendering-and-surface.md:129–140`), L15 (`syzygy` CLI and
MCP named, `RFC-0010-…:84–97`) and L16 (RFC9-48's keyboard action enumeration,
`interaction-parity-…:231–238`) are all DI or unrouted. Each is a passage an
implementer would build from without noticing they had skipped a phase.
Positively: no latency numbers, frame rates, wire formats, query grammar, URL
spellings or HTTP semantics appear anywhere in RFCs 0006–0011 — verified by
sweep. The leakage is exclusively closed vocabularies and required-field lists.
**Minimal fix:** flag these nine in the matrix (a `leak-risk` column, or promote
them to DI+OS with a routed limb) so the coverage matrix cannot silently skip
the passages most likely to be implemented from prose.

**F6 [Non-blocking] — all 8 CR rows route to a policy artifact that does not
exist, and none names a CC-* identity.**
Routes-to values are "Review/release policy", "Release policy", "Release policy
/ craft", "Craft (performance policy)". `.syzygy/governance/policies/` contains
only `craft-and-care/` (8 files, no release policy). RFC9-45 itself handles the
absence correctly — owner decision B12(b) binds directly with no adopted policy
(`visual-grammar-and-lenses.md:497–504`) — but the matrix's CR column carries
none of that, so "may I implement X?" for a CR clause resolves to a dangling
pointer.
**Minimal fix:** name the target per row — either a CC-* clause identity that
exists today, or `governance/policies/release-policy (does not yet exist; RFC9-45
B12(b) default binds meanwhile)`.

**F7 [Non-blocking] — the matrix's "two §7 non-deferring obligations" is a
universal claim; a mechanical sweep surfaces more candidate sentences.**
`:203–206` asserts "Two such obligations exist" and enumerates RFC 0008 §7's
board-layout ladder (`rfcs/RFC-0008/README.md:213–218`) and RFC 0007 §7's
link-integrity cadence (`rfcs/RFC-0007/README.md:241–248`). A regex sweep for
non-deferral phrasing in §7 sections also returns
`rfcs/RFC-0007/README.md:233` ("Reader-controlled status density … **the minimal
default binds now**"), `rfcs/RFC-0009/interaction-parity-and-release.md:339`
("the obligation to declare budgets, **and to declare them before V0 ships**,
binds here regardless"), `rfcs/RFC-0008/accounting-reconciliation-and-release.md:352`
and `rfcs/RFC-0008/state-vocabulary-and-cost.md:331`. Each of these four
restates an obligation a numbered clause already carries (RFC7-16, RFC9-49,
RFC8-24, RFC8-16 respectively), so the count of *novel* non-deferring
obligations is defensibly two — but the matrix does not say "novel," and the
claim as written does not survive a mechanical check.
**Minimal fix:** amend `:204` to "Two such obligations are carried **only** by
§7 prose; four further §7 sentences restate obligations already numbered
(RFC7-16, RFC8-16, RFC8-24, RFC9-49)."

**F8 [Non-blocking] — the matrix's row set has no drift guard.**
`scripts/verify_final_prespec.py` (269 lines) contains no reference to
`SURFACE-CLAUSE-ROUTING-MATRIX` (checked by literal substring on the source).
Neither `build_contract_index.py --check` nor `build_dependency_index.py --check`
covers it. So adding a clause to any of RFC 0007–0011 produces a matrix with a
missing row and every check still PASSes, and the Tallies block at `:321–327`
goes stale silently. Today the tallies are correct — I reproduced all five rows
exactly — which is the good moment to install the guard.
**Minimal fix:** add a check to `verify_final_prespec.py` asserting that the
matrix's row-ID set equals the clause set of the contracts the matrix declares
in scope, and that the Tallies block reproduces from the rows.

---

*End of RC-5 raw output. Counts in this file were produced with Python `re` in
this session and cross-checked against `05-CONTRACT-INDEX.yaml` and
`scripts/verify_final_prespec.py`; the sampling in §3 is deterministic (every
6th DI row in file order) and reproducible from the matrix bytes.*
