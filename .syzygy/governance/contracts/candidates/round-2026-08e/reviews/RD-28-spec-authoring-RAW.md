# RD-28 — Specification-authoring review (round-2026-08e, frozen commit 246af62)

## 1. Subject identification

**Clone:** `/tmp/claude-1000/-home-tze-GitHub-syzygy/3fa62952-e192-440e-8b1f-5b48212d8da1/scratchpad/clone-08e-r4`
**Commit verified this session:** `git log -1` → `246af620e993984dedbff8c44207dcea75d07e91  round-2026-08e: the RD-27 Wave B repair batch — argument regenerated, apparatus brought current` [Observed]
**Tracked file population:** 346 tracked files, of which 335 are `.md`/`.py`/`.yaml`/`.yml`/`.txt` (computed via `git ls-files` this session) — this is the denominator for every repo-wide sweep below. [Observed]

**Charter role:** specification-authoring reviewer. The question asked is not "is the gate READY" but: *if the owner ruled "go" tomorrow, could a competent spec author author Capability 1 correctly from these bytes, or would they improvise?* I am reviewing whether the artifacts that would answer launch-gate criteria E1–E6 are sound, internally consistent, mutually consistent, and honest. I administered no gate question and recorded no gate verdict.

**Artifacts read in full:** `AGENTS.md`; `.syzygy/governance/doctrine/vision.md`; `launch-gate-pre-specifications.md` §§1–2, E-region, §8, §9 changelog; `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`; `FIRST-OPENSPEC-SEQUENCE.md` (rev3); `OPENSPEC-FORM-AND-VERSION-DECISION.md`; `SPECIFICATION-GRANULARITY-DECISION.md`; `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`; `round-2026-08e/FIRST-SPEC-TRACE-TABLE.md`; `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`; `DEFERRED-WAVE-POSTURE.md`; `decisions/PENDING-OWNER-DECISIONS.md`; `decisions/launch-gate/README.md` + `TREND-LOG.md`; `06-CONTEXT-LOAD-MAP.md`; `fixtures/context-selection-8-openspec-authoring.md`. **Sampled:** `SURFACE-CLAUSE-ROUTING-MATRIX.md` (header, four-route rule, future-domains section, standing caveats, RFC-0006/0007 notes, the round-08d addition block, and eight individual rows); `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md` (E1–E6 rows, E3 trace, G1, reconciliation notes); RFC1-33 / RFC2-26 / RFC3-33 / RFC4-30 / RFC5-27 / RFC6-28 clause text; RFC4-10; RFC3-5 declaration row and RFC3-26; `craft-and-care/review-and-documentation.md` (CC-REV-2 in full, whole-file sweeps); `policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` (§"What this workflow does not do"); `TASK-ROUTER.md`; `PROJECT-STATUS.md`; `09-OPEN-SPEC-READINESS-REPORT.md` banner + sequence; `TASK-TO-CONTRACT-INDEX.md` banner; `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 act table; the six wave manifests.

## 2. Method

- Every substantive claim is labelled `[Observed]` / `[Inferred]` / `[Unknown]`. LLM assertion is never Observed.
- **Verification rule 1.** No load-bearing measurement used shell `grep` pattern classes. Clause enumeration, row parsing, domain-token extraction and the repo-wide sweeps were done with Python `re` over file bytes; `grep -F` was used only for literal-substring existence checks. One consequence is recorded honestly in §4 (a literal-space `grep` returned 0 on a phrase that is line-wrapped in the source; the Python read caught it).
- **Verification rules 2 and 9.** Every "zero / none / all" claim below states its denominator and names the sweep. Where I did not run a sweep, I record `[Unknown]` rather than a clean result — see §5.
- **Verification rule 5.** I distinguish citation from reliance. A clause named for orientation is not a dependency; a derivation step that cannot execute without the named clause is.
- **Verification rule 8.** Each finding quotes the sentence it anchors to, with its file. Where I claim a clause does not say something, I quote the clause and state the sweep.
- **Verification rule 10.** I edited nothing, anywhere. Read-only throughout.
- **Isolation.** I read only inside the frozen clone and did not consult the live repository.

Findings are numbered `RD28-nn` and classed **BLOCKING** (the launch decision must not be offered on this path) / **MAJOR** (must be repaired before the formal gate administration) / **MINOR** (repair or record).

---

## 3. Findings

### RD28-01 — MAJOR — The E4 routing authority is silent on 11 of the 20 clauses the first spec is built on, and the rationale it gives for that silence is contradicted by its own corpus and by itself

`launch-gate-pre-specifications.md` §8 binds `E4_ROUTING_AUTHORITY` to `SURFACE-CLAUSE-ROUTING-MATRIX.md`. That file's scope is stated in its own header:

> "This file records, for every clause of RFC 0006–0011, where that clause's content belongs *after* foundational acceptance." — `SURFACE-CLAUSE-ROUTING-MATRIX.md:2-4`

**Sweep, run this session** (Python `re` over the whole file, row pattern `^\|\s*\*{0,2}(RFC\d+-\d+(\([a-z]\))?)\*{0,2}\s*\|`): **210 clause rows**, distributed RFC-0006 ×28, RFC-0007 ×47, RFC-0008 ×32, RFC-0009 ×60, RFC-0010 ×27, RFC-0011 ×16. **Zero rows for RFC-0001, 0002, 0003, 0004, 0005.** Denominator: all 210 rows. [Observed]

Cross-swept against the twenty clause identities `round-2026-08e/FIRST-SPEC-TRACE-TABLE.md` names as governing Capability 1 (rows 1–10 of that table): **9 of 20 have a matrix row; 11 do not** — RFC3-1, RFC3-4, RFC3-5, RFC3-9, RFC1-1, RFC1-3, RFC3-6, RFC3-7, RFC5-3, RFC2-24, RFC1-7. [Observed] Every clause governing trace rows 1 and 2 — *"Parse/validate the project declaration…"* and *"Record consent and repository coverage…"*, i.e. the registration half of "Project registration and honest shape visibility" — is unrouted. The one deferred-wave clause in the trace table (RFC10-4, Wave D1) **does** have a row.

The exclusion carries two different and independently defective justifications inside the one file.

**(a) The header's reason does not distinguish the excluded set.**

> "this file's rows cover RFC 0006–0011; RFC 0001–0005's enumerations are produced at surface specification, per each phase clause's own staging" — `SURFACE-CLAUSE-ROUTING-MATRIX.md:11-13`

But the staging sentence is identical in the included contracts. RFC3-33: *"At surface specification a clause-to-requirement coverage matrix over RFC3-1..RFC3-33 is produced — **that matrix is review material, never authority**"* (`rfcs/RFC-0003/manifests-and-namespace.md:516-519`). RFC6-28: *"The surface-specification phase must produce, as a deliverable, a **clause-to-requirement coverage matrix** for this RFC … and that matrix is review material, never authority"* (`rfcs/RFC-0006-cross-surface-selection-query-drawer.md:494-498`). RFC-0006 nonetheless received 28 routing rows. The staging sentence is therefore not a discriminator, and the stated reason does not support the line drawn. [Observed]

**(b) The standing caveat states a fact the corpus contradicts, and the same file contradicts it 900 lines later.**

> "**RFC 0001–0005 are deliberately not enumerated here.** Their observable consequences reach users exclusively *through* the six rule-carrying contracts above. That is a recorded judgment, not an omission … One residue is named rather than hidden: RFC 0005's ceremony, login, and consent *experiences* are user-observable and **carry no phase rule of their own**." — `SURFACE-CLAUSE-ROUTING-MATRIX.md:118-123`

RFC5-27 *is* that phase rule, and it names those exact experiences:

> "**RFC5-27.** This contract schedules nothing… No implementation work for user-observable consequences of this contract — **authentication and session flows, machine-client admission, consent and egress gate behavior**, secret-handling behavior, execution-profile effects, audit and revocation surfaces — may be scheduled solely from this RFC." — `rfcs/RFC-0005/admission-and-boundary.md:337-342`

The same matrix file says so itself:

> "**every** active contract now carries a binding phase rule (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27 joined the six the header names…)" — `SURFACE-CLAUSE-ROUTING-MATRIX.md:1032-1035`

The broader premise — *"Their observable consequences reach users exclusively through the six rule-carrying contracts above"* — is contradicted by RFC1-33 and RFC3-33 enumerating their own user-observable consequences: *"project registration and declaration validation flows, entity and relation rendering, lifecycle and succession displays…"* (`RFC-0001-…:750-753`) and *"governance-home layout behavior, project declaration and manifest validation flows, owner-act ceremony surfaces, provenance and effective-status rendering"* (`RFC-0003/manifests-and-namespace.md:499-502`). "Project registration and declaration validation flows" is Capability 1. [Observed]

**Effect on an author.** An author of Capability 1 asking the E4 routing authority "which clauses govern registration, and which side of the boundary does each fall on" gets no answer for the registration half of their own spec, and gets a recorded judgment explaining the absence that its own corpus refutes. The launch-gate pilot recorded the coverage gap but explicitly declined to let it carry E4's verdict (*"That is a coverage gap, not a disagreement, so it does not carry the verdict"* — pilot E4 row). That triage was correct for E4-as-administered; it is not correct for the authoring question, and the 08e pass did not close it.

### RD28-02 — MAJOR — The routing matrix routes the first spec's two Wave B clauses into a spec domain it never minted, contradicting its own domain declaration and its own RFC-0007 note

> "## Future specification domains — Provisional names, minted for routing only… `spec/selection-api` · `spec/intent-surface` · `spec/work-surface` · `spec/map-surface` · `spec/map-scenes` · `spec/map-lenses` · `spec/mission-control` · `spec/context-packets`. One further domain is **proposed, not minted**: `spec/platform-service`" — `SURFACE-CLAUSE-ROUTING-MATRIX.md:102-114`

**Sweep, run this session** (Python `re`, all `` `spec/…` `` tokens extracted from all 210 clause rows, compared against the minted eight plus the proposed one): exactly one domain token appears in rows and in neither list — **`spec/polaris`** — and it appears on exactly two rows: [Observed]

> `| RFC7-39 | OS | `spec/polaris` | …` — `SURFACE-CLAUSE-ROUTING-MATRIX.md:1039`
> `| RFC7-40 | OS | `spec/polaris` | …` — `SURFACE-CLAUSE-ROUTING-MATRIX.md:1040`

RFC7-39 and RFC7-40 are rows 3 and 4 of `FIRST-SPEC-TRACE-TABLE.md` — the human-entry and discoverability obligations of Capability 1. The matrix's own RFC-0007 note says the opposite:

> "10. **No new spec domain is needed for RFC-0007.** Everything lands in `spec/intent-surface`…" — `SURFACE-CLAUSE-ROUTING-MATRIX.md:467-468`

So the two clauses the first spec most directly needs are routed to a domain the file declares does not exist, in contradiction of the file's own note about the very contract those clauses belong to. This is a per-row defect of the class other reviewers have found, on rows relevant to Capability 1 and not previously repaired (the round-08d addition block that carries them post-dates the RFC-0007 pass and was not reconciled against it). [Observed]

### RD28-03 — MAJOR — The matrix claims to be the enumeration the binding phase rules stand on, but its unit is the clause and the phase rules' unit is the observable consequence

The matrix states its own purpose and unit:

> "That rule is only as good as the enumeration behind it. **This matrix is that enumeration: every declared clause identity of RFC 0006–0011, each routed exactly once**" — `SURFACE-CLAUSE-ROUTING-MATRIX.md:20-23`

Every one of the eleven phase-rule clauses carries, as defined clause text, the opposite unit:

> "**Rows are per observable consequence, not per clause.** A clause with five observable consequences and one mapped requirement is not covered; the matrix discloses the consequences it enumerates for each clause, so **a complete-looking matrix over under-enumerated consequences is a defect of the matrix**." — `rfcs/RFC-0006-…:490-494`; verbatim-parallel at `RFC-0001-…:764-768`, `RFC-0003/manifests-and-namespace.md:512-516`, `RFC-0005/admission-and-boundary.md:353-357`

A one-route-per-clause table cannot disclose per-consequence enumeration, and the matrix's rows do not attempt it — the sampled rows carry a single "a spec must assert…" obligation per clause (e.g. RFC6-19 at `:198`, whose retained-invariant cell alone names eight content classes with distinct observable members). [Observed] The author's actual question at authoring time — *how many requirements does RFC6-19 need before it is covered?* — is the per-consequence question, and the artifact that presents itself as "that enumeration" answers the per-clause one. The clause text calls that shape a defect of the matrix by name. `[Inferred]` that this is the highest-cost gap for a real first spec, because coverage is exactly what CC-SPEC-8 will be judged against.

### RD28-04 — MAJOR — The E6 propagation path attributes to CC-REV-2 an exception limb that CC-REV-2 does not contain, and its detection step has no clause owner at all

`HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` routes E6 as follows:

> "## What happens when shape changes after specs exist (E6) — Owned by craft CC-REV-2 (the merge invariant) with the propagation path recorded in `round-2026-08e/SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md`'s governing description" — `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:45-49`

That governing description opens by claiming its owners are cited and nothing is invented:

> "## Governing description (what the path is; **owners cited, nothing invented**)" — `SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md:14`

Two of its five steps are not owned as claimed.

**Step 4's second limb is invented.** The fixture says:

> "4. **Responsible amendment** — the shape change's author owns the spec amendments (CC-REV-2's same-logical-change merge invariant), **or records an explicit exception with its reason and expiry condition**." — `SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md:26-28`

CC-REV-2 contains no exception limb. Its only carve-out is doctrine: *"The one structural carve-out: **doctrine** is amended only through the owner gate (VIS-4)"* (`craft-and-care/review-and-documentation.md:67-68`). **Sweep, run this session** over the whole of `review-and-documentation.md` (the named owning file, Python `re`, case-insensitive): `exception` **0 hits**, `expiry` **0 hits**. Denominator: the complete file. [Observed]

**Step 2 has no owner in any authority.** The fixture says:

> "2. **Affected-spec enumeration** — a blast-radius sweep over the spec corpus for every requirement citing the amended clause or consuming its vocabulary; the sweep's denominator is recorded (**verification rule 9**)." — `SHAPE-TO-SPEC-PROPAGATION-FIXTURE.md:18-21`

Verification rule 9 lives in `AGENTS.md`, which declares of itself: *"This file is **repository operating procedure** — never citable as authority"* (`AGENTS.md:5-6`). **Sweep, run this session** over `review-and-documentation.md`: `sweep` 0, `enumerat*` 0, `affected` 0, `detect*` 0, `denominator` 0; `blast` 1 hit, at `:6`, in a preamble about severity grading (*"severity follows blast radius"*), unrelated to spec enumeration. Denominator: the complete file. [Observed] Extending to the craft cluster: `blast` appears in **1 of 10** craft files, the same line. [Observed]

The only artifact that describes the detection step still disclaims itself, unchanged at this commit:

> "**It has no enforcement.** Every step is a discipline, not a gate. The script-checkable parts — **blast-radius sweeps**, count re-verification, citation resolution — **do not exist as checks yet** … **It has not been executed end to end.**" — `policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`, §"What this workflow does not do"

The pilot failed E6 precisely on detection (*"the path demonstrably does not detect affected artifacts"*). The 08e repair adds a paper dry-run with a golden answer — genuinely valuable, and honest about being a fixture — but it does not add a detection mechanism, and the E6 router does not disclose that step 2 and step 4's exception limb rest on nothing citable. An administration handed this chain could reasonably read it as a discharge. `[Inferred]`

### RD28-05 — MAJOR — E5's sole named owner is a prerequisite craft act with no gate: no act row, no ceremony phrase, no digest, no queue entry, and no presence in the cluster it claims to join

`HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:39-43` routes E5 entirely to `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`, and `FIRST-OPENSPEC-SEQUENCE.md` lists satisfying it as a Capability 1 prerequisite:

> "| Specification acceptance standard in force | Craft act | **blocking** — candidate exists (`policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`); wants review + its craft act, or the owner knowingly authors against the candidate |" — `FIRST-OPENSPEC-SEQUENCE.md:50`

The candidate names its own gate: *"**Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT` act.**"* (`SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:3`).

**Repo-wide sweep, run this session** (Python `re` over all 335 tracked `.md`/`.py`/`.yaml`/`.yml`/`.txt` files):

| Token | Files | Which |
|---|---|---|
| `SPECIFICATION-ACCEPTANCE-POLICY` | **5** | `FIRST-OPENSPEC-SEQUENCE.md`, `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`, `SURFACE-CLAUSE-ROUTING-MATRIX.md`, `TASK-ROUTER.md`, `scripts/build_task_router.py` |
| `CC-SPEC-\d` | **2** | the candidate itself, `SURFACE-CLAUSE-ROUTING-MATRIX.md` |
| `specification[- ]acceptance` (case-insensitive) | **6** | the five above plus the candidate |

Denominator: 335 files. [Observed] Confirmed by a second method (literal `grep -rlF` over the same trees, same result sets).

It therefore appears in **none** of: `decisions/PENDING-OWNER-DECISIONS.md` (the owner decision queue), `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (the live gates), `ACCEPTANCE-PHRASE-REGISTRY.yaml`, `AGENTS.md`, `PROJECT-STATUS.md`, or any file under `policies/craft-and-care/` (the cluster whose `CC-*` namespace it mints into). I read the acceptance record's §1 act table directly: its rows are A, B, C1, C2, D1, D2, 2 (CC-TEST-2), 3 (topology), 4 (overview), 5 (D3) — **ten acts**, matching `AGENTS.md`'s *"Ten acts are open"*, with no eleventh. [Observed]

So Capability 1 carries a blocking prerequisite whose satisfaction has no route: the owner has no phrase to say, no digest to verify, and no queue row telling them the question is outstanding. The sequence document discloses the situation to a reader who reaches it, which is why this is MAJOR rather than BLOCKING — but the gate apparatus, the decision register, and the craft cluster are all unaware of it.

Recorded in fairness: CC-SPEC-4 is a real repair. The pilot's E5 finding was that *"Testability has none… the third limb has no criterion even in candidate form"*; `CC-SPEC-4` now states one (*"A requirement is testable when it names: the observable surface…, the initiating condition, the expected observable outcome, and the evidence that would show the outcome absent"*). The gap is the gate, not the content.

### RD28-06 — MAJOR — The E1 table labels the status of three of its five rows and leaves the two that failed the pilot unlabeled, and states an unruled decision's recommended option as the answer

`HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:13-19`, the five-row table that is the E1 answer:

| Row | Owner cell as written | Status disclosed? |
|---|---|---|
| Form / version | "Owner decision **P-39** + the adapter contract" | **no** |
| Home / identity | "RFC 0003 / RFC 0004 **(candidate, Wave A)**" | yes |
| Granularity | "Owner decision **P-40**" | **no** |
| Acceptance authority | "Doctrine **VIS-4 (adopted)**" | yes |
| Change process | "Craft **CC-REV-2 (owner-approved)**" | yes |

[Observed] The two unlabeled rows are exactly the two sub-verdicts the pilot failed (*"E1 | **Not met** (2 of 5 sub-verdicts fail)"* — Form and Granularity). P-39 and P-40 are both open: `PENDING-OWNER-DECISIONS.md:148-149` lists them among "Open, and only the owner can dispose", and both packets open *"**This file decides nothing.**"* [Observed]

The granularity row goes further and states the unruled rule's content as the answer:

> "| **Granularity** … | Owner decision **P-40** | `decisions/SPECIFICATION-GRANULARITY-DECISION.md` — **one coherent capability, one product argument, one acceptance decision** |" — `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:17`

That text is option (a) of an unruled packet whose own "Current authority" section reads *"None — this is the gap"* (`SPECIFICATION-GRANULARITY-DECISION.md:29-31`), and whose recommendation is labelled *"`[Inferred]` **(a)**"*. The router restates it without the `[Inferred]` label, without "recommended", and without the "Current authority: none" fact.

Mitigation, recorded: the file's banner does say *"**No specification may be authored yet** — the prerequisites table in `FIRST-OPENSPEC-SEQUENCE.md` … is the current gate state"* (`:6-9`), and that table does mark P-39 and P-40 **blocking**. The defect is that the table which *answers* E1 presents two unruled questions in the same visual form as three settled ones, and quotes one of them as decided — inside a file whose own governing instruction is *"this file cites the owner and invents nothing"* (`:3-4`).

### RD28-07 — MAJOR — The one worked example of compiling context to author an OpenSpec spec derives its entire mandatory set from deferred Wave C2 clauses, and carries no deferred label

`DEFERRED-WAVE-POSTURE.md:36-40` binds the containment and instructs reviewers to report escapes:

> "2. **Default navigation.** No default reading or task route ends in a C/D candidate."
> "Escapes are findings against *this file's* claims — report them, never absorb them." (`:46`)

`fixtures/context-selection-8-openspec-authoring.md` is the fixture set's OpenSpec-authoring worked example. Its selection is not merely *cited* to RFC-0011 — it is *derived* from it, step by step (verification rule 5's reliance test):

> "**Selection rule trace (RFC11-4, traversal per RFC11-14).**" — `:37`
> "**Phase-boundary rule, applied (RFC11-4 with RFC11-13) — the on-seam case.** … The amended rule **therefore forces** the module *defining* RFC7-38 — `rendering-and-surface.md` … **into the mandatory set**" — `:48-54`

RFC11-4, RFC11-13 and RFC11-14 are all defined in `rfcs/RFC-0011/deterministic-selection-and-budget.md` — verified this session by Python `re` over that module (clauses defined there: RFC11-4, 11-11, 11-13, 11-14, 11-15, 11-16). That module is the **entire content of Wave C2**: `wave-manifests/WAVE-C2-MANIFEST.txt` lists exactly one row, `rfcs/RFC-0011/deterministic-selection-and-budget.md`. [Observed] Wave C2 is deferred.

**Sweep, run this session:** the string `defer` (case-insensitive) occurs **0 times** in the whole of `context-selection-8-openspec-authoring.md`. Denominator: the complete file. [Observed] By contrast `06-CONTEXT-LOAD-MAP.md` *does* label its Mission Control reader row (*"— **deferred-wave candidates**, see `DEFERRED-WAVE-POSTURE.md`"*, `:51-52`), so the labelling convention exists and was simply not applied here.

The same escape appears in the load map's own closing section, which states the operative rules of context compilation entirely from deferred clauses with no label:

> "Mandatory selection is deterministic from the index metadata + warrant (**RFC11-4**); suggestion never suppresses (**RFC11-5**); incomplete is Unknown and by default blocks launch … (**RFC11-6**); the index is a rebuildable projection, never a second truth store (**RFC11-7**)." — `06-CONTEXT-LOAD-MAP.md:87-91`

Capability 1's *specification content* does not depend on C/D — that separation holds and I found no counter-example. What depends on C/D is the *procedure by which an author would assemble the context to write it*, and that is the one procedure a "go" ruling would immediately exercise. `[Inferred]`

### RD28-08 — MINOR — The E4 classification rule says "the six phase-rule clauses" where the corpus has eleven, and the five it omits are exactly the unrouted RFC 0001–0005

> "One classification rule, owned by **the six phase-rule clauses** and the routing matrix's route table" — `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:22-25`

Against `SURFACE-CLAUSE-ROUTING-MATRIX.md:9-13` (*"Eleven contracts each carry the same binding phase rule — RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12"*), and against the same file's own §hard-boundary sentence eight lines later (*"Doctrine (VIS-4, VIS-5) and **every contract's** phase rule"*, `:71-72`). All eleven clause definition sites verified present this session by locating each `**RFCn-nn.**` definitional header. [Observed] The stale count is internally inconsistent within one short file, and it drops the same five contracts RD28-01 shows are unrouted — compounding rather than flagging that blind spot.

### RD28-09 — MINOR — The prerequisite table declares "each with exactly one state" and three rows carry two, mixing prerequisites-for-authoring with prerequisites-for-the-launch-decision

> "## Prerequisites for authoring Capability 1 — **each with exactly one state** — States: `satisfied` / `owner-waived` / `blocking` / `not applicable`." — `FIRST-OPENSPEC-SEQUENCE.md:35-37`

Three of the fifteen rows carry two states, or a state scoped to something other than authoring Capability 1: [Observed]

- P-12: *"**blocking** for Capability 2; for Capability 1 the budget rule is not consumed — **not applicable** to Capability 1's own authoring"* (`:51`) — two state words in one cell.
- P-34: *"**blocking** for the launch decision (the owner may lawfully decide without it…)"* (`:52`) — a state about the launch decision, not about authoring.
- P-35: *"**blocking** for the formal administration's A6/F5 verdicts; the spec itself does not consume it"* (`:54`) — likewise.

Each is individually honest and well-reasoned; the table's stated invariant is nonetheless violated, and E2's fail clause turns on prerequisites being *listed* rather than discovered — a list whose states mean different things per row is weaker evidence than the header promises.

### RD28-10 — MINOR — The OpenSpec-authoring fixture asserts an "accepted fixture set" that does not exist

> "**Status:** DRAFT — a candidate fixture, not part of the rev10 accepted fixture set (fixtures 1–5)." — `fixtures/context-selection-8-openspec-authoring.md:3-4` (line-wrapped after "accepted")

No fixture is accepted: no owner acceptance act has been performed at this commit, and a sweep this session over **all six wave manifests** found **zero** rows referencing `fixtures/` (denominator: the six files `WAVE-{A,B,C1,C2,D1,D2}-MANIFEST.txt`). [Observed] `DEFERRED-WAVE-POSTURE.md:18` independently records the same fact for C2 (*"fixtures outside every manifest"*). "rev10" is itself superseded (`SURFACE-CLAUSE-ROUTING-MATRIX.md:47-49`). This is an inherited phrase and the fixture's own status line says "Binds nothing", which is why it is MINOR — but it is a candidate presented as accepted, on the authoring path, in the file `AGENTS.md`'s hard prohibitions name that class for.

---

## 4. What passes

These are not concessions; they are measured results, and several are real discharges of pilot findings.

- **E2's "two documents answer differently" is closed.** `09-OPEN-SPEC-READINESS-REPORT.md` now opens *"# SUPERSEDED — … **SUPERSEDED — do not rely on anything below this banner.** … the first-spec sequencing below is superseded by the current `FIRST-OPENSPEC-SEQUENCE.md` … No active route may point here except as history"* (`:1-14`), and `TASK-TO-CONTRACT-INDEX.md` carries a parallel banner (`:1-11`). `FIRST-OPENSPEC-SEQUENCE.md` rev3 declares itself *"**This is the single current first-spec document**"* (`:5-6`). `TASK-ROUTER.md:109` states *"The superseded 09 readiness report is history and answers nothing."* The pilot's E2 count (i) is discharged in bytes. [Observed]
- **E3's trace table exists and meets the credibility protocol's form.** `FIRST-SPEC-TRACE-TABLE.md` enumerates ten central concepts, traces each to a named shape artifact, marks acceptance state, and names the owner question on the path — and it refuses to claim its own verdict: *"E3 becomes `Met` only when a fresh reviewer's own trace finds every launch-scope row either governed by an accepted artifact or covered by a recorded owner ruling — **never from this file's say-so**"* (`:36-38`).
- **Every owner decision the trace table and the sequence name is genuinely queued.** I checked P-31, P-33, P-36, P-37, P-38, P-39, P-40 row by row against `PENDING-OWNER-DECISIONS.md` (`:139`, `:141`, `:145`–`:149`) and confirmed each named packet file exists at the path given. **7 of 7 present.** [Observed]
- **E1's Home, Acceptance authority and Change process sub-answers verify against defined clauses.** RFC3-5's declaration row does carry *"the spec root (`openspec/`, fixed)"* (`RFC-0003/manifests-and-namespace.md:181`); RFC3-26 exists and reads *"**`openspec/**` is outside Syzygy's migration authority**"* (`:396`); VIS-5 confines direct writes to the two roots (`vision.md:141-146`); VIS-4 places behavioural specs below the owner line with the compound-amendment gate (`vision.md:124-133`); CC-REV-2 is quoted accurately for the merge invariant. [Observed]
- **The P-39 packet's contract citation is exact.** Its claim that identity survival *"is RFC 0004's adapter-contract obligation"* verifies at the clause: *"Whether OpenSpec identities survive edit and rename is [Unknown] (RFC1-15); the adapter therefore declares its anchor **stability class**…"* (`RFC-0004/named-adapters.md:84-88`). The packet acknowledges rather than resolves the Unknown, exactly as it says. [Observed]
- **CC-SPEC-4 closes the one E5 limb that had no criterion in any form.** See RD28-05.
- **The forbidding is uniform where an author would look.** `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md:6-9` and `:69-75`; `FIRST-OPENSPEC-SEQUENCE.md:2-4`; `TASK-ROUTER.md:97` (*"the answer to 'may I author OpenSpec?' is the owner's launch decision"*); `AGENTS.md:78`; `PROJECT-STATUS.md:48` (*"⛔ **Not started**"*). I found no artifact on this path that says authoring is permitted. [Observed]
- **The absences are honestly declared rather than hidden.** `FIRST-OPENSPEC-SEQUENCE.md:57-58`: *"Nothing is `satisfied` and nothing is `owner-waived` today."* `decisions/launch-gate/README.md`: *"Empty today, correctly: no formal administration has been run."* `TREND-LOG.md`: *"zero rows is the correct current state, not a gap."* Fixture 8: *"`openspec/**` house conventions — **do not exist yet.** A real gap, not an exclusion", and an unchecked verification box carrying "*not verifiable by the script*". This is the epistemic discipline VIS-2 asks for, applied to the project's own claims.
- **Fixture 8 is, on its merits, a strong worked example** — the decomposition review declines three splits with measured reasons, the waiver names its reviewer and expiry trigger, and the digest-pinning paragraph explains why staleness is the correct visible outcome. RD28-07 is about its unlabeled deferred-wave reliance, not its quality.
- **The pilot's E4 pass-2 defect is repaired.** RFC6-28 now routes CR with the repair recorded in place: *"**Re-decided CR on 2026-08-10** — launch-gate pilot finding E4 required the six shape-parallel phase clauses to route identically"* (`SURFACE-CLAUSE-ROUTING-MATRIX.md:207`), and the superseded N/A reasoning is preserved rather than deleted. Per charter I did not re-sample that row for its own sake. [Observed]

## 5. What I did not measure

Recorded so no reader takes silence for a clean result (VIS-2 applied to this review).

- **`PILOT_RECURRENCE_CHECK` — [Unknown].** I located the two retired phrases across the corpus (`ACCEPT FOUNDATIONAL RFCS`: 24 of 334 files; `ACCEPT COMPACTED FOUNDATIONAL RFCS`: 27 of 334) but did **not** classify each hit as history/registry versus presented-as-current. That classification is the gate administrator's sweep, and I make no claim either way.
- **The routing matrix's remaining ~200 rows.** I sampled eight rows plus the domain and phase-rule metadata. RD28-02's `spec/polaris` result *is* a full-population sweep over the domain tokens (denominator 210 rows); no other per-row claim here generalises beyond the rows quoted.
- **The validator battery.** I ran no script (`check_governance.py`, `verify_final_prespec.py`, `build_*.py`) — every finding above is derived from the bytes directly, which is the weaker method for anything the battery owns and the stronger one for anything it does not check.
- **Waves C1/C2/D1/D2 content.** Read only through `DEFERRED-WAVE-POSTURE.md` and manifest membership, per the deferred posture.

## 6. Overall assessment

A competent spec author handed a "go" tomorrow would not be improvising about *what a specification is* — form, home, granularity, acceptance authority and change process each now have a named home, three of them binding or owner-approved and two queued as prepared owner decisions, and the first spec is identified once, with its prerequisites listed rather than discovered and the superseded competitors banner-marked. That is a materially better position than the pilot found on 2026-08-09, and the honesty posture of the path is genuinely strong: every artifact I read declares what it is, refuses to claim its own verdict, and names its gaps rather than smoothing them. What the author *would* have to improvise is the part the pilot's E4 and E6 rows pointed at and that this pass did not close: the routing authority is silent on the eleven of twenty clauses that govern the registration half of Capability 1 and justifies that silence with a recorded judgment its own corpus refutes; it routes the first spec's two entry clauses into a domain it declares does not exist; its unit is the clause where the binding phase rules demand the observable consequence, which is precisely the unit coverage will be judged in; the E6 propagation path attributes an exception limb to a craft clause that contains none and rests its detection step on a file that declares itself never citable as authority; the standard the spec would be accepted against is a prerequisite act with no ceremony, no digest and no queue row; and the one worked example of assembling the author's own context executes entirely on deferred Wave C2 clauses with no deferral label. None of these rises to BLOCKING, because nothing on this path currently offers the owner a launch decision — the gate stands at `NOT READY`, every prerequisite reads `blocking`, and every route says authoring is forbidden. All seven are MAJOR: each would corrupt a formal administration's E1, E4, E5 or E6 answer if administered against these bytes as they stand.

VERDICT: REVISE
