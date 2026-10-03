# Impact ledger — D8, Inferred as a first-class rendered state

> **Candidate — binds nothing.** The blast-radius record for
> `OWNER-DECISION-PACKET.md` (this directory), drafted 2026-10-03 for
> `syzygy-u05.15`. Every figure here was computed at `origin/main`
> `6bb6ef26` with this package's own directory excluded; it is valid for
> that commit only (rule 7) and is re-derived, never read, after any later
> edit to the population.

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
`.md`, `.json`, `.yaml` or `.txt` — **1,540 files**.

**Result:** **145 files, 405 occurrences.**

**Second method:** `git grep -l -i -E` with the same alternation (POSIX
`[[:space:]]` for `\s`) over the same paths, filtered to the same four
extensions and the same exclusion: **145 files, set-equal** to the Python
result (symmetric difference empty) [Observed: both run this session].

| Lane | Files | Occurrences | Disposition |
|---|---|---|---|
| Doctrine | 1 | 4 | §3.1 |
| Accepted contract (`contracts/rfcs/`) | 0 | 0 | — |
| Decision | 6 | 9 | §3.2 (plus one raw in `decisions/`) |
| Specification (`openspec/`) | 14 | 24 | §3.3 |
| Candidate | 25 | 36 | not authority; untouched |
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
| `DOCTRINE-AMENDMENT-D6-TREE-STYLE-REVIEW-2-RAW.md`:25 (raw lane) | quotes line 54's "recorded human decision" | a retained raw; never edited |

### 3.3 Specifications

| File:line | Hit | Disposition |
|---|---|---|
| `polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`:337, 508, 640; `design.md`:58 | REQ-polaris-generation-031 and its record shapes: "Attributed answers, presentation preferences and adopted intent SHALL remain distinct existing classes", withdrawal invalidation | **consistent with (b).** (b) states at doctrine level what REQ-031 already requires; it adds the rendering (Observed as a fact about the record) and the VIS-6 commit-out. REQ-031's "Missing input/persistence consent SHALL preserve the limitation without silently retaining or using the answer" stays the rule wherever (d) gives no destination |
| `polaris-manifesto-generation/specs/polaris-generation/spec.md`:755; amendment `spec.md`:422; `design.md`:24, 31, 149; `INTERFACES.md`:318; `CAPABILITY-COVERAGE.md`:56 | "synthesis" as the generator's task of explaining a project's argument | **a different sense.** The generator's output is a generated asset governed by its own specification and adoption path; clause (a) is scoped to prose "a surface composes over several claims". Whether a generated manifesto shown on a surface before adoption is also a clause-(a) synthesis is **[Unknown]** here: (f) would render it an unadopted draft, (a) would render it Inferred, and the two may both apply. The reviewer is asked to test this |
| amendment `COVERAGE.md`:1, 4; `SYNTHESIS-MAP.json`:2; `proposal.md`:8, 58; `tasks.md`:8, 10; amendment `spec.md`:3 | specification-synthesis sense | unaffected |
| `polaris-project-wide-butlers-model/specs/…/spec.md`:1374; `design.md`:499 | "one copy role is `project-fact`" (openings) | PWB-REQ-012's closed roles; untouched. Clause (a) does not open a role (packet §6, Q-S1) |
| `polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md`:35 | RFC7-2's three-way classification recorded "**Unknown uncovered**" against PWB-REQ-012 | the coverage gap behind Q-S1; untouched |
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

Found by a digest sweep (`git grep -l -F` for each of the three doctrine
digests, every tracked file) and a reader sweep: Python `re`
`governance/doctrine|doctrine/(vision|architecture|trust-and-evidence)\.md`
over every tracked file under `apps/`, `packages/` and `scripts/` ending
`.ts`, `.py`, `.js`, `.mjs`, `.json`, `.yaml` or `.yml` — **421 files, 11
readers**, the same eleven D7's ledger names (its IMPACT-LEDGER.md §4,
in the sibling directory doctrine-amendment-held-derived-computation-d7,
pull request #296).

| Artifact | Reads | On application |
|---|---|---|
| `DIRECTIVE-REGISTER.md` (generated by `scripts/build_directive_register.py`) | file and line of every VIS identifier | insertion (d2) after `vision.md` line 234 moves VIS-7 (line 250) and every later VIS line down six lines; regenerate. It indexes no `trust-and-evidence.md` or `architecture.md` line [Observed: 0 rows name either file] |
| `contracts/candidates/05-CONTRACT-INDEX.yaml` (rebuilt by the battery's `build_contract_index.py`) | a `words` count and `rule_ids` for each doctrine file (lines 570, 572, 574) | all three word counts change; `trust-and-evidence.md`'s `rule_ids` would gain VIS-4 (clause (b) cites it). Regenerate. Whether any PWB builder's manifest reaches these values is **[Unknown]** here, as it was for D7; the battery run after application decides it |
| `scripts/check_polaris_response_ceiling_reading.py` | a quoted `vision.md` sentence outside VIS-6 | unaffected |
| `scripts/record_polaris_understanding_adoption.py` | `vision.md` at a historical commit | unaffected |
| `docs/evidence/polaris-understanding-reconciliation-2026-09-28/` (3 files) | the `vision.md` digest reviewed then | unaffected: a record |
| `apps/three-surface-poc/src/polaris-generation/self-corpus.ts` (and test) | doctrine Markdown at a pinned commit | a later pin gets a new corpus digest; not a break |
| five tests and `scripts/polaris_generator_approval.py` | a doctrine path as a fixture path | unaffected |
| `scripts/check_governance.py` | doctrine paths in messages | unaffected |

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
