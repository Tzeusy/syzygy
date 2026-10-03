# Impact ledger — D8, Inferred as a first-class rendered state

> **Candidate — binds nothing.** The blast-radius record for
> `OWNER-DECISION-PACKET.md` (this directory), drafted 2026-10-03 for
> `syzygy-u05.15`. Round 1 returned `REVISE`; this is the once-repaired,
> unconfirmed text (`ROUND-1-DISPOSITIONS.md`). Every figure here was
> computed at commit `59fbf78700d72b14d1551926c2b55b464c61aa5e` (the
> round-1 reviewed commit, on `origin/main` `d8f0aeec`) with this package's
> own directory excluded; it is valid for that commit only (rule 7) and is
> re-derived, never read, after any later edit to the population. The
> drafting figures at `6bb6ef26` (1,540 files, 145 hit files, 405
> occurrences) are superseded.

## 1. The term sweep

**Predicate** (Python `re`, `re.IGNORECASE`, applied to whole-file text):

```text
synthes[ie]s|\bcorrespondence\b|attributed\s+answer|AttributedAnswer|observed-only|self-observ|reflexive|copy\s+role|recorded\s+human\s+decision
```

The literals cover the five terms the clauses introduce, the copy-role
mechanism clause (a) would need, and the doctrine phrase clause (b) sits
beside. `\s+` spans a hard wrap, so "attributed" and "answer" on adjacent
lines match.

**Population:** every tracked file under `.syzygy/`, `openspec/` and
`docs/`, plus `AGENTS.md`, `README.md` and `PROJECT-STATUS.md`, ending
`.md`, `.json`, `.yaml` or `.txt` — **1,554 files**.

**Result:** **147 files, 407 occurrences.**

**Second method:** `git grep -l -i -E` with the same alternation (POSIX
`[[:space:]]` for `\s`) over the same paths, filtered to the same four
extensions and the same exclusion: **147 files** [Observed: both run this
session; set-equality was confirmed at `6bb6ef26` and the round-1 reviewer
re-confirmed it independently at both commits].

| Lane | Files | Occurrences | Disposition |
|---|---|---|---|
| Doctrine | 1 | 4 | §3.1 |
| Accepted contract (`contracts/rfcs/`) | 0 | 0 | — |
| Decision | 7 | 10 | §3.2 (plus one raw in `decisions/`) |
| Specification (`openspec/`) | 14 | 24 | §3.3 |
| Candidate | 26 | 37 | not authority; untouched |
| Other | 9 | 18 | not authority; untouched |
| Evidence (`docs/evidence`, `docs/pursuits`) | 57 | 247 | records; never edited |
| Raw review | 31 | 64 | CC-REV-6; never edited |
| Historical (`round-*`, `_bootstrap`, `history/`) | 2 | 3 | never edited |

The lane is assigned by path prefix, first match wins, in this order:
doctrine; accepted contract; raw (`docs/reviews/`, a `-RAW.md` suffix or a
`/reviews/` segment); historical; decision; specification; candidate
(`contracts/candidates/`, `policies/`, `map/`); evidence; other. So
`decisions/DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-2-RAW.md` counts as raw,
not decision; §3.2 lists it anyway because it sits in `decisions/`.

**No accepted contract uses any of the five terms** [Observed: 0 files in
the accepted-contract lane, both methods]. The contracts the clauses rest
on (RFC1-14, RFC1-16, RFC4-26, RFC7-2, RFC2-25) use "inferred mapping",
"Inferred with its inference provenance" and the tier names instead;
§3.4 reads them directly.

## 2. Wrapped citations

The predicate's multi-word literals use `\s+`, so a hard wrap inside one is
matched. Single-word literals cannot wrap. A code span broken across lines
does not affect this predicate, which matches terms rather than paths.

## 3. Authority-lane hits and their disposition

### 3.1 Doctrine

`trust-and-evidence.md` lines 14, 38, 54 and 75, all "recorded human
decision". These are the anchors clause (b) sits beside: it adds a third
class named *apart* from the recorded human decision and the work warrant.
No line is made false: line 14 ("Status rests on evidence; a recorded human
decision and a work warrant…") enumerates the two warrants and stays true,
because clause (b) says the answer is "neither evidence nor a warrant"
[Inferred]. If the owner reads line 14 as an exhaustive list of
non-evidence *records*, (b) is in tension with it; the reviewer is asked to
test this.

### 3.2 Decisions

| File:line | Hit | Disposition |
|---|---|---|
| `ACCEPTANCE-ACT-RECORD.md`:833, 839, 1144 | `SYNTHESIS-MAP.json` row; "synthesis" in two act scopes | the specification-synthesis sense (an amendment synthesized from agreed sources), not clause (a)'s; unaffected |
| `POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md`:35, 41; `POLARIS-UNDERSTANDING-DEPENDENCY-UNION-SUCCESSOR-ACT.md`:34 | the same rows and scopes | the same; unaffected |
| `PROCESS-LESSONS.md`:49 | "A synthesis wrote 'PASS with…'" (verdict smoothing) | a review synthesis; consistent with (a)'s rule that a synthesis states no fact not derivable from its inputs; unaffected |
| `DECISION-HISTORY.md`:48; `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`:64 | P-74 Q3, "three acts scoped to a test-only self-observation (consent record, second registry entry, secret-policy extension)" | **interaction.** Clause (e) is consistent with these acts and adds no fourth; the packet recommends adopting (e) before any of the three is performed (packet §1 (e)). A test-only self-observation that never renders a certifying claim is untouched by (e) |
| `PENDING-OWNER-DECISIONS.md`:1042 | P-98 (PWB opening-index amendment), "Q5: the copy roles of the new strings" | **interaction with Q-S1.** P-98 assigns copy roles inside PWB-REQ-012's closed set; it opens no synthesis role. If the owner commissions Q-S1, it lands after or beside P-98's ruling on the same closed set |
| `DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-2-RAW.md`:25 (raw lane) | quotes line 54's "recorded human decision" | a retained raw; never edited |

### 3.3 Specifications

| File:line | Hit | Disposition |
|---|---|---|
| `polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`:337, 508, 640; `design.md`:58 | REQ-polaris-generation-031 and its record shapes: "Attributed answers, presentation preferences and adopted intent SHALL remain distinct existing classes", withdrawal invalidation | **consistent with (b).** (b) states at doctrine level what REQ-031 already requires; it adds the rendering (Observed as a fact about the record) and the VIS-6 commit-out. REQ-031's "Missing input/persistence consent SHALL preserve the limitation without silently retaining or using the answer" stays the rule wherever (d) gives no destination |
| `polaris-manifesto-generation/specs/polaris-generation/spec.md`:755; amendment `spec.md`:422; `design.md`:24, 31, 149; `INTERFACES.md`:318; `CAPABILITY-COVERAGE.md`:56 | "synthesis" as the generator's task of explaining a project's argument | **a different sense.** The generator's output is a generated asset governed by its own specification and adoption path; clause (a) is scoped to prose "a surface composes over several claims". Whether a generated manifesto shown on a surface before adoption is also a clause-(a) synthesis is **[Unknown]** here: (f) would render it an `editorial-draft`, (a) would render it Inferred, and the two may both apply. The reviewer is asked to test this |
| amendment `COVERAGE.md`:1, 4; `SYNTHESIS-MAP.json`:2; `proposal.md`:8, 58; `tasks.md`:8, 10; amendment `spec.md`:3 | specification-synthesis sense | unaffected |
| `polaris-project-wide-butlers-model/specs/…/spec.md`:1374; `design.md`:499 | "one copy role is `project-fact`" (openings) | PWB-REQ-012's closed roles; untouched. Clause (a) does not open a role (packet §6, Q-S1) |
| `polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md`:35 | the RFC7-2 row "Non-factual framing is machine-marked non-normative", recorded "**Unknown uncovered** — its closed roles contain no `non-normative` standing" | RFC7-2(b) only, not the whole three-way classification; whether `project-fact` may carry an Inferred sentence is this drafter's open question [Inferred]; the gap behind Q-S1; untouched |
| `…/contract-coverage-parts/RFC-0007-0009.md`:253; `…/contract-coverage-matrix/RFC-0007-0009.md`:192 | "Copy role" in an overclaim note and an RFC9-26 row | unaffected |

The POC specification (`openspec/changes/three-surface-poc-experience/`)
returns no hit for the predicate; its class (ii) exclusion is read
directly in §3.4.

### 3.4 Accepted contracts read directly (no term hit)

| Clause | Quoted text | Effect of D8 |
|---|---|---|
| RFC7-2(c), `RFC-0007/narrative-contract.md` lines 96–97 | "**(c) epistemically labeled** — Observed with its evidence link, Inferred with its inference provenance, or Unknown" | (a) and (c) are instances; nothing made false |
| RFC1-14, `RFC-0001-project-graph-identity-state-planes.md` lines 361–368 | "Code mapping to no declared capability renders Unknown — never silently inferred into a capability." | (c) keeps the claim Unknown ("never moves a claim off Unknown"); consistent |
| RFC1-16, same file lines 378–390 | "Class (ii) enters only via the inference profile, challenge authority only." | (c) restates "challenge authority only"; the profile stays undefined (Q-C1) |
| RFC1 deferrals, same file lines 1003–1004 | "Challenge machinery beyond the admissibility floor, and inference records → inference profile / RFC 0002." | untouched; the reason (a) and (c) cannot be built yet |
| RFC4-26, `RFC-0004/fidelity-joins-and-mappings.md` lines 154–162 | "class (ii) inferred mappings enter only through the inference profile with challenge authority only." | the same |
| RFC2-25, `RFC-0002/rendering-vocabularies.md` lines 168–189 | six closed tiers; "an untier'd claim renders at its bare label"; three sibling surface states | every clause maps into it (packet §2); nothing added |

The POC specification's coverage row for RFC4-26
(`three-surface-poc-experience/CONTRACT-COVERAGE.md` line 119, routed to
POC-REQ-050 and POC-REQ-052) reads "covered — Orrery's declared-mappings-only design is exactly class (i) with class (ii) excluded", so the POC builds no correspondence; untouched
(Q-S2).

## 4. Derived artifacts that read doctrine bytes

**Method 1, an application probe (decisive).** In a scratch clone at the
round-1 reviewed commit `59fbf787`, all seven insertion blocks were applied
exactly as packet §1 shows them, and the canonical battery (`PROJECT-STATUS.md`
"How to verify this page", plus the `--check` and `--selftest` of the five
PWB amendment builders present) was run. An unapplied clone at the same
commit was run the same way as a baseline [Observed, both this session]:

- baseline: **80 commands, 0 nonzero**;
- applied: **80 commands, 6 nonzero**, every one attributable to the
  insertion:

| Command | Failure | What application must do |
|---|---|---|
| `scripts/check_governance.py` | CG-18 FAIL, "context fixtures recompute": 16 findings over 10 fixtures × 2 predicates (packet digest and word count of each fixture's declared mandatory set) | re-anchor the context-selection fixtures |
| `$CS/build_budget_report.py --check` | DRIFT in 8 fixtures (`context-selection-1`, `3`, `5`, `6`, `7`, `8`, `9`, `10`) and in `CONTEXT-BUDGET-REPORT.md` | regenerate the report and re-anchor the fixtures |
| `$CS/build_contract_index.py --check` | `05-CONTRACT-INDEX.yaml` differs (doctrine `words` and `rule_ids`, lines 570, 572, 574) | regenerate |
| `scripts/build_directive_register.py --check` | "DIRECTIVE-REGISTER.md is stale": insertion (d2) moves VIS-7 from line 250 to 257 | regenerate |
| `scripts/record_polaris_understanding_adoption.py --check` | "review retired by changed input: .syzygy/governance/doctrine/vision.md" | **not a regeneration.** See below |
| `scripts/record_polaris_understanding_adoption.py --selftest` | "candidate input drift: .syzygy/governance/doctrine/vision.md" | the same |

**The recorder failure is a gate, not a rebuild.** The Polaris understanding
adoption recorder binds `vision.md` (`VISION`, line 240) as a frozen input
of its C1 reconciliation review, and requires every frozen input outside its
history set to hash today to the digest that review confirmed (line 592:
`'review retired by changed input: ' + path`). Any byte change to
`vision.md` therefore retires that review for the recorder's purposes.
Clause (d2) is D8's only `vision.md` insertion; (a), (b), (c), (e), (f) and
(d1) alone leave the recorder green [Inferred: from the recorder's frozen
set, which names no other doctrine file; not separately probed]. Applying
(d2) needs one of: a new reconciliation review over the amended
`vision.md`, or a recorder change moving `vision.md` into its history set,
each reviewed. Which is the owner's question (packet §7 Q-A1). **The same
holds for D7**, which also inserts into `vision.md` [Inferred: D7 was not
probed here; routed to the coordinator].

**Method 2, a static reader sweep (lower bound).** Python `re`
`governance/doctrine|doctrine/(vision|architecture|trust-and-evidence|README|v1|security)\.md|doctrine:(vision|architecture|trust-and-evidence)`
over every tracked file ending `.ts`, `.tsx`, `.py`, `.js`, `.mjs`, `.cjs`,
`.json`, `.yaml`, `.yml` or `.sh`, outside the doctrine directory — **686
files, 39 readers** at `59fbf787`. Of the 39: 20 are evidence or pursuit
records (`docs/evidence/`, `docs/pursuits/`) and 1 is the launch-gate
administration record, all describing past bytes and never edited; 2 are
`round-2026-08j` sweep scripts (historical); 1 is `05-CONTRACT-INDEX.yaml`;
the other 15 are the generators, checkers and tests in the tables above and
below. The static sweep misses `build_contract_index.py`, which reaches
doctrine through a relative directory (`GOV_SOURCES`, `"../../doctrine"`),
so method 1 is the one relied on. `build_capability_1_views.py` carries
doctrine identifiers from its charter, not doctrine bytes, and stayed
green.

| Reader | On application |
|---|---|
| `$CS/context_load.py`, `$CS/build_task_router.py` | read doctrine through the fixtures and router; covered by the CG-18 and budget-report rows; `build_task_router.py --check` stayed green |
| `scripts/check_quotations.py` | stayed green: no quoted doctrine bytes move (every insertion is between existing lines) |
| `scripts/check_polaris_response_ceiling_reading.py` | stayed green |
| `apps/three-surface-poc/src/polaris-generation/self-corpus.ts` (and its test) | doctrine Markdown at a pinned commit; a later pin gets a new corpus digest, not a break |
| four other tests (`git-blob-batch.test.ts`, the `req-023`, `req-061` and `req-integration` conformance tests) and `scripts/polaris_generator_approval.py` | a doctrine path as a fixture path; unaffected |
| `scripts/check_governance.py` | the CG-18 row above; otherwise messages only |
| `docs/evidence/polaris-understanding-reconciliation-2026-09-28/` (3 files) | the `vision.md` digest the recorder above binds; records, never edited |

Neither `trust-and-evidence.md`'s nor `architecture.md`'s digest occurs in
any tracked file; `vision.md`'s occurs only in the three evidence files
above [Observed]. No doctrine digest is in a performed act's manifest.

## 5. Observations routed, not repaired

1. **N15's wording of (b).** The pursuit says "agent-produced answers"; the
   merged move L3-M7 and REQ-031 say owner answers. Packet §0 discloses the
   departure.
2. **Clause (e) and the launch-gate battery.** The launch-gate
   administration (`decisions/launch-gate/`) and the canonical battery are
   tooling runs over Syzygy's own tree. Clause (e) is drafted to bind only
   observation-pipeline records ("observes its own repository as an
   observed project"); if the owner reads a battery run as
   self-observation, (e) would deny it the floor, which no one intends.
   The scope sentence is the clause's main risk and is flagged to the
   reviewer.
3. **The (a)/(f) overlap for a generated manifesto** (§3.3) is unresolved
   and left to the owner or a later specification.
4. **D7 shares the recorder gate** (§4): its `vision.md` insertion would
   fail `record_polaris_understanding_adoption.py --check` the same way.
   D7's ledger lists that script as "unaffected". Routed to the
   coordinator; D7's bytes are not edited here.
