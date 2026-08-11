# RD-48 — Launch-policy v2.0 semantic preservation (round-2026-08f, frozen commit `e2efda6`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 review 2 — did v1.18 → v2.0 preserve the instrument's meaning? |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `e2efda6` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Subject files** | `launch-gate-pre-specifications.md`; `round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` (given as a claim to test, not as evidence) |
> | **Context** | fresh — subject, governing references and acceptance criteria only |
> | **Model family** | same family as the corpus authors. Supports repair; **is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `REVISE` |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.

---

I have everything I need.

---

VERDICT: REVISE

---

## A. Byte-identity claim, recomputed

**Method.** `git show 4aa221b:launch-gate-pre-specifications.md` (last v1.18 revision) and `git show e2efda6:launch-gate-pre-specifications.md` (HEAD; byte-equal to the worktree file, confirmed by `diff`). Split both with Python `re` on `^## \d+\.` — the delta's own stated method — and sha256 each span. I did not read the delta's table before running this.

| Section | v1.18 bytes | v2.0 bytes | identical? | v1.18 sha256[:12] | v2.0 sha256[:12] | delta says |
|---|---|---|---|---|---|---|
| Preamble | 2914 | 3702 | no | `541862fac53a` | `10be446f5aac` | changed ✓ |
| §1 Derivation tiers | 793 | 793 | **yes** | `af8755392208` | `af8755392208` | byte-identical ✓ |
| §2 Administration protocol | 4387 | 4790 | no | `28c745f6beab` | `76a2a640863d` | changed ✓ |
| §3 The question series | 15376 | 15376 | **yes** | `4143073e44c8` | `4143073e44c8` | byte-identical ✓ |
| §4 Verdict computation | 5687 | 5687 | **yes** | `7952a130c8ba` | `7952a130c8ba` | byte-identical ✓ |
| §5 Record format | 3600 | 5999 | no | `aa7a227c1f8d` | `8eb1778432e8` | replaced ✓ |
| §6 Trend log | 2191 | 3215 | no | `5884c5aec674` | `4591d785c566` | changed ✓ |
| §7 Generalization | 1037 | 1228 | no | `bdc18cf9061a` | `cb9c508d2566` | changed ✓ |
| §8 Parameter block | 6609 | 6609 | **yes** | `4ff1b98668d0` | `4ff1b98668d0` | byte-identical ✓ |
| §9 Changelog | 76167 | 80206 | no (appended) | `3d37b13fb395` | `e49dde205d06` | appended ✓ |

**Observation.** The identity verdicts are correct in all ten rows. No section the delta calls unchanged is changed; no section it calls changed is unchanged. Denominator: all 10 spans, which exhaust both files (spans are contiguous and cover byte 0 to EOF).

The delta's *byte counts* are not reproducible. Every figure it prints is lower than mine by a non-constant offset (§1 −5, §3 −126, §9 −595). I tried four readings of its stated method (raw span, `strip()`, strip + drop `---` rules, drop blank lines); the best matched **1 of 10** rows. The delta says "sha256 each span" but publishes no digests, only the unreproducible counts.

**Judgement.** Claim A holds on substance. The delta's supporting table is decorative rather than checkable — a "measured, not asserted" heading over figures that cannot be re-derived from the stated method.

**Also observed and not in the delta's table:** v1.18 carried a `## G1 — completeness critic` heading *inside* §5 (v1.18 line 590). It is gone in v2.0. G1 itself survives — `**G1 [U]**` is in the byte-identical §3 (v2.0 line 469), and the record now carries `g1: {critic_answer, proposed_missing_questions[]}` with `LA-14` refusing a placeholder answer, which is stronger than v1.18's `LG-4` presence-of-a-section test. Not a drop; but it is a change of shape the delta's section table renders invisible.

---

## B. Every changed section: before vs after

**Method.** Per-section unified diff of the two revisions.

**Preamble.** `effective_version` v1.18→v2.0; `governs:` now names "the structured administration source record and its generated report (§5)"; a new `record_schema:` key with a normative clause ("an administration source record conforms to it or it is not a record"); `canonical_result_home` now describes JSON + reports; three artifact classes become four; "Launch-gate definition" renamed "Launch-gate policy".
- Could conclude before, not now: that the record class requires being **"stored verbatim"** — that phrase is deleted (v1.18 line 42 → v2.0 line 51, `never adopts anything; superseded, never edited`). The successor obligation ("Never edit a past administration; supersede it.") survives in §5, so the substance is retained, but the verbatim-storage requirement is gone and the delta does not say so.
- Could conclude now, not before: that the report is never authority. Strengthening.

**§2.** Three hunks. (i) "the record **quotes** the instrument's sha256" → "**carries**". (ii) A new integrity bullet (line 130): "**The record is the JSON source, not the report.** A reviewer who submits only prose has submitted no record…" — pure addition, strengthening. (iii) The verdict-word paragraph is rewritten (line 179).

Old clause: *"Copy these verdict words exactly into the results record. Never translate a verdict into softer language. Questions are quoted verbatim at the version administered — a verdict rendered against a paraphrased question is void…"*
New clause: *"Record these verdict words exactly. In the structured record the vocabulary is a closed enumeration, so a softened verdict is a schema error rather than a reading the next reader has to catch. Questions are bound at the version administered — a verdict rendered against a paraphrased question is void — and every operationalization judgment call is recorded in the record's own field, never left in prose."*

- Two sentences are **deleted**: "Never translate a verdict into softer language," and the *verbatim quotation* obligation on questions ("quoted verbatim" → "bound"). Delta D-6 records only the addition.
- Is it a loosening? On the row `verdict` field, no — the schema enum is strictly tighter than a prose instruction. On question binding, the record now carries `question_digest`, whose schema pattern permits the literal `"instrument-bound"` as an alternative to a real digest, so no question text ever needs to appear in a record. Because `LA-2` verifies the instrument's own sha256 against the committed bytes, and §3 is inside those bytes, the binding is substantively equivalent. **Net: not a loosening, but two explicit obligations were dropped without record.**

**§5.** Replaced. Reader could conclude before: the record is one Markdown file in a stated template with a terminal `GATE VERDICT:` line, six declared fields, and a G1 section. Cannot now. Can conclude now: the record is JSON validated against a committed schema; it carries **no** verdict; absence is an error; counts are array lengths; scope needs two agreeing typed fields. All strengthening. One thing a reader could rely on before and cannot now: **§5 itself enumerated what the validator checks.** v2.0 line 676 delegates that: *"the tool's own docstring is the enumeration, and it is the tool's, not this instrument's, to keep current."* See Finding 5.

**§6.** The row is now generated, and the cross-boundary comparability limit is stated. Both additions. Column semantics and the nine-column header are byte-unchanged.

**§7.** The generalization rule gains "**and the record schema**" plus a new factual clause. See Finding 4 — the clause is false.

**§9.** Appended one v2.0 entry. Contains one stale figure (Finding 6).

**Judgement.** Directionally every changed section is a strengthening or a neutral restatement. **No loosening of any readiness question in any changed section.**

---

## C. Dropped, renamed, or unreachable — full populations with counts

**Method.** Regex enumeration over §3 for `^- \*\*(ID) \[tier\]\*\*`; literal counts over §1–§8 (excluding §9's history) for verdict vocabulary; column split of the trend header line; and cross-check against `ROSTER` in `scripts/validate_launch_administration.py` and the schema's `question_id` pattern.

| Population | v1.18 | v2.0 | Δ |
|---|---|---|---|
| Question bullets in §3 | 35 (A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1) | 35, same IDs in same order | 0 |
| Tier split | [U] 33 / [G] 2 | [U] 33 / [G] 2 | 0 |
| Roster rows (with E1's five sub-rows, G1 excluded as a row) | 39 | 39 (`len(ROSTER)`, schema pattern, `LA-4`) | 0 |
| Row verdict vocabulary | Met / Not met / Not met (out of launch scope) / Unknown(reason) = **4** | same 4, now a schema `enum` | 0 |
| Forbidden forms named | "Partially met", "Met with caveats" | same 2 (schema description) | 0 |
| §4 formula core conjuncts, as written | 5 + F2 limb | 5 + F2 limb (byte-identical) | 0 |
| §4 formula core conjuncts, **as computed** | 5 + F2 limb (`LG-6`) | **6** + F2 limb (`_compute` adds "E3's reopen list is empty") | **+1** |
| Trend columns | 9: Date, Commit, Not-met, Scoped, Unknown, Deferred, Reopened, New findings vs prior, Gate verdict | identical 9 | 0 |
| Gate verdict words defined in §1–§8 | 3 (`READY FOR <target>`, `NOT READY`, `READY-WITH-DEFERRALS`) | **2** — `NOT READY` occurs 0 times in §1–§8 | **−1** |

**Observation on `NOT READY`.** Sweep denominator: all 2059 lines of the v2.0 file. `grep -n -F "NOT READY"` returns 9 hits, at lines 1186, 1196, 1229, 1308, 1470, 1567, 1666, 1796, 1924 — every one ≥ 889, the first line of §9. §9 is history. In v1.18 the word was defined in §5's record template. It is still *reachable* (`_compute` emits the Python literal `"NOT READY"`, and the generated report ends `GATE VERDICT: NOT READY`), but the instrument that "owns readiness semantics" (its own words, v2.0 line 687) no longer names the verdict word its failing branch produces.

**Judgement.** No readiness question, verdict word for a *row*, or trend column was dropped, renamed, or made unreachable. Two structural discrepancies exist: the operative formula gained a conjunct §4 does not contain, and the gate-level verdict word `NOT READY` lost its home in the instrument body.

---

## D. Does the delta record every change of meaning?

**Method.** Walked every diff hunk in every changed section and matched it against D-1…D-10 and the "What did not change" section.

Recorded correctly: D-1 (§5 replaced), D-2 (three classes → four, with the renames quoted), D-3 (no `final_verdict`; verified — schema `additionalProperties: false` and no such property), D-4 (counts as array lengths; verified in `_compute` lines 853–854), D-5 (`verdict`/`launch_scope` cross-check; verified `LA-5` lines 562–570), D-6 (§2's new bullet), D-7 (generated trend row + comparability limit), D-8 (schema in the portable core), D-10 (`launch_gate_results.py` retained at 329 fixtures — verified by running `--selftest`: "329 fixtures, 0 failing").

**Unrecorded changes of meaning:**

1. §4's byte-identity leaves five references to a record format that no longer exists (Finding 1). The delta presents §4 byte-identity purely as reassurance.
2. The computed formula has a sixth core conjunct (Finding 2). The delta says "no formula term" changed.
3. §5 delegates the normative check enumeration to a script docstring and disclaims currency (Finding 5). Not mentioned anywhere in the delta.
4. §2's two deleted obligations (Criterion B).
5. Preamble's deleted "stored verbatim".
6. D-9's new-check table omits `LA-14`'s placeholder refusal, which is a genuinely new obligation over `LG-4`.
7. D-9 says `LA-13` enforces a rule "previously trusted." v1.18's own §5 (line 630) says the opposite of its baseline: *"a delta administration's record cannot support a gate decision (§2's full-vs-delta rule, **now checked rather than trusted**)."* The delta mischaracterizes the baseline it names.
8. D-9's `LA-16` row does not disclose that the check runs only when `formal` **and** `prior_record is null` (code line 826) — i.e. on the first formal administration only.

**Judgement.** **Fails.** Eight changes of meaning or of characterization are unrecorded, of which items 1, 2 and 3 are substantive.

---

## E. New ways to reach a pass verdict?

**Method.** Executed the validator against constructed records in `/tmp` (repo untouched), starting from the committed `round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json`. Read the schema's optionality/defaults/enums directly. Compared against `LG-6`/`LG-7`/`LG-10`/`LG-11`/`LG-13` in `git show 4aa221b:scripts/launch_gate_results.py`.

Probes run:
- **All rows `Met`** → `READY FOR Capability 1 — Project registration and honest shape visibility`, exit 0. Correct per §4.
- **F2 `Not met` + one `SDR-9` deferral with a bounded plan** → `READY-WITH-DEFERRALS`, exit 0. Correct per §4; `LA-11` correctly rejects a `P-n`/`D-n`/`B-n` citation, a non-existent path, and a directory.
- **All `question_digest` set to `"instrument-bound"`** → passes. Permitted by the schema pattern. Not a loosening: `LA-2` pins the instrument bytes, which contain §3.
- **`formal: false`, `administration_kind: "delta"`, `fresh_context: false`, all rows Met** → **`READY FOR …`, "record valid", exit 0, and `--trend-row` prints a §6 row carrying that verdict.** `LA-13` and `LA-16` are gated on the self-declared `formal` boolean (code lines 769, 826). The validator's own docstring asserts "`LA-13` … a `delta` record can never support a gate decision (§2)"; the code does not implement that. Mitigation: the generated report prints "Administration: delta, not formal (steering only)". No *rejection*, no note in the validator output.
- **git made unavailable** (fake `git` returning 127) with a fabricated instrument sha256 (`000…`), fabricated parameter-block sha256 (`111…`) and launch target `"Total nonsense target"` → **"record valid", `READY FOR …`, trend row printed, exit 0**, preceded only by one `note:` line. The same record with git present produces three `LA-2`/`LA-3` errors. Under v1.18, `LG-2` skipped the digest checks the same way; in v2.0 the skipped set is **wider** (identity, wave binding, E4 case-text fidelity via `pb_text is None` at code line 674, deferral-citation existence, prior-record ancestry).

**Typed-field surfaces that replaced reviewer prose, examined for softness:** `formal` (boolean, reviewer-set, gates two checks); `needed_by_launch_target` (boolean, reviewer-set, gates `LA-10`'s silence rule); `blocking_conditions_met` (enum array, reviewer-set, empty ⇒ scoped verdict lawful — this, not `launch_scope`, is the real scope oracle and the delta's limit note names the wrong field); `counterexample`, `falsification_summary`, `evidence.quote` are **not** run through `_is_placeholder`, while `falsification_attempt`, `bounded_reduction_plan`, `g1.critic_answer` and `pilot_recurrence_check.method` are.

**Judgement.** **No new pass path relative to v1.18.** Everything that passes v2.0 would have passed v1.18's checks, and v2.0 blocks several things v1.18 did not (`LA-6` per-row evidence/counterexample/falsification, `LA-9` trace coverage, `LA-10` case-text equality, `LA-11` vacuous-deferral guard, `LA-14` placeholder G1). The two surfaces above are undisclosed limits, not regressions — but they are limits, and the delta's six-item list omits both.

---

## F. Self-containment and portability

**Method.** Read §7's clause verbatim; swept the schema and both tools for repository-specific strings.

The clause (line 777): *"The schema generalizes without change — **it names no Syzygy artifact**, and the launch target, waves, and fixed cases it carries are values a parameter block supplies."*

Sweep of `launch-gate-administration.schema.json` (denominator: all 449 lines):
- `"$id": "https://github.com/Tzeusy/syzygy/launch-gate-administration.schema.json"`
- top-level `description` names `launch-gate-pre-specifications.md`, `scripts/validate_launch_administration.py`, and `(VIS-4)`
- `reopened_findings.description` names `(VIS-2)`
- `owner_deferrals.decision_citation.description`: *"A repository path existing at repository_commit, or an **SDR-n** identifier. **P-n** names the pending queue and grants nothing."*

And `scripts/validate_launch_administration.py` line 116: `DECISIONS_HOME = ".syzygy/governance/decisions"`, used by `LA-11`.

**What the portable core omits.** §7 names the [U] questions, the §2/§4 protocol, and the schema. It does **not** name `validate_launch_administration.py` — which computes the verdict and, per §5 line 676, owns the check enumeration — or `render_launch_administration.py`, which produces the only human-readable form of a record. Under v1.18 a reviewer with the instrument alone could write a conforming record by hand and a human could check it against §5's template. Under v2.0 a record cannot be validated, its verdict cannot be computed, and its report cannot be produced without two uncommitted-to-the-core Python tools, one of which hardcodes a Syzygy path.

**Judgement.** **Fails.** The self-containment claim in §7 is false as written, and the portable core is under-specified in the direction the amendment moved.

---

## G. The delta's self-reported defects and disclosed limits

**Method.** Verified both defects in the committed bytes; audited the six disclosed limits against the code.

Defect 1 — `lstrip("./")` eating the leading dot of `.syzygy/…`. **Honestly characterized and fixed.** Code lines 738–743 carry a prefix strip and the reason in a comment; fixtures at lines 1258/1261 exercise the non-existent-path and directory cases; I confirmed both reject.

Defect 2 — `DO_NOT_EDIT in out1` tautology. **Honestly characterized and fixed.** `scripts/render_launch_administration.py` line 343 comments "The LITERAL string, never the constant". `--selftest` reports "12 fixtures, 0 failing", including "`--check` detects a hand-edited report".

Limits audit — the six disclosed limits are all real and all accurately stated. Two of them understate:
- "`launch_scope` agreement is a consistency check, not a scope oracle" names the wrong field. The reviewer-authored field that actually decides whether a defect is scoped-lawful is `deferred_wave_findings[].blocking_conditions_met`; an empty array is what makes the scoped verdict survive `LA-8` (code lines 630–637).
- "`--check` detects an edited report; it does not detect a deleted one" is accurate but sits beside no mention that nothing detects a *missing* validation either.

**Limits I found that the delta does not disclose:**
- The git-unavailable degradation (Criterion E): a record with a fabricated instrument digest, fabricated parameter-block digest and a nonsense launch target reports "record valid" with a READY verdict.
- The `formal: false` gate on `LA-13`/`LA-16`, and the unconditional trend-row generation for a non-formal delta record.
- The placeholder-lexicon asymmetry: `counterexample`, `falsification_summary` and `evidence.quote` are presence-only.

Baseline claims I independently verified and found **true**: the four subject digests at `a8c2031` all match, and are unchanged at HEAD `e2efda6`; the v1.18 instrument digest `616364a5…` and `launch_gate_results.py` digest `278ee1ea…` at `4aa221b` match; `RD-33 … RD-45` is thirteen reviews and every one carries `VERDICT: REVISE` (checked by grepping each file); RD-45 is on v1.17 and no RD-46 exists (denominator: all 27 files in `round-2026-08e/reviews/`).

**Judgement.** The two self-reported defects are honestly characterized — genuinely so; both are the kind a delta could have quietly omitted. The disclosed limits are honest but incomplete on three counts.

---

# Findings

**1. [material] `/home/tze/GitHub/syzygy/launch-gate-pre-specifications.md` lines 511, 518, 539, 545, 557, 559, 564, 568 — §4's normative clauses name record fields and validator checks that do not exist for a v2.0 record.**
§4 is byte-identical, which is exactly what left it pointing at the deleted format. Line 539: *"the record's `Owner deferral decision:` field names the owner decision"* — no such field; the record has `owner_deferrals[]`. Line 559, inside the stated `READY-WITH-DEFERRALS` predicate: *"AND `Deferred count:` is nonzero AND the citation is present"* — no such field; it is `len(owner_deferrals)`. Line 568: *"(§5's family line; the trend row)"* — §5 has no family line. Lines 518 and 564 cite `LG-9` and `LG-6/LG-7`, checks in `launch_gate_results.py`, which by §5 line 696 validates historical Markdown records **only** and never runs on a v2.0 record. Sweep denominator: all 888 lines of §1–§8; the literals `Owner deferral decision:` and `Deferred count:` occur 4 times, all in §4, and no clause anywhere in §1–§8 states the mapping to the JSON field names.
*Fix:* amend §4's clauses to name the schema fields (`owner_deferrals[].decision_citation`, `len(owner_deferrals)`, `reviewer.model_family`) and the `LA-*` checks, as a recorded semantic delta. It cannot be done silently — §4's byte-identity is a load-bearing claim of this amendment.

**2. [material] `scripts/validate_launch_administration.py` line 876 — the computed formula has a sixth core conjunct that §4 does not contain, and the generated report attributes it to §4.**
`_c("E3's reopen list is empty", not rec["e3"]["reopen_items"], …)` is added to the five conjuncts §4 states, and `render_launch_administration.py` prints all six under the heading "Conjuncts of the §4 formula" (see `fixtures/DRY-RUN-ADMINISTRATION.md`). §4 (byte-identical) lists five. §5 line 687 says *"The instrument, not the tool, owns readiness semantics."* The delta's "What this does not touch" says *"no formula term"* changed. The conjunct is a strengthening and is grounded in §3's E3 rule — but it is a formula term the instrument does not carry.
*Fix:* either add the conjunct to §4 by amendment, or relabel it in the tool and report as an §3-derived gate rather than a §4 conjunct.

**3. [material] `launch-gate-pre-specifications.md` — the gate verdict word `NOT READY` no longer exists in §1–§8.**
Sweep denominator: all 2059 lines; 9 occurrences, all at line ≥ 1186, i.e. all inside §9's history. v1.18 defined it in §5's template. The word is emitted by `_compute` (a Python literal), printed by the renderer as the report's last line, and carried in the trend log's "Gate verdict" column — but the instrument that owns readiness semantics no longer defines it. The 2026-08-09 pilot's recorded outcome and `PROJECT-STATUS.md`'s standing claim both rest on this word.
*Fix:* state the three gate verdict words in §4 or §5, so the failing branch's word has a home in the instrument.

**4. [material] `launch-gate-pre-specifications.md` lines 777–779 — §7's new clause "it names no Syzygy artifact" is false.**
`launch-gate-administration.schema.json` line 3 is `"$id": "https://github.com/Tzeusy/syzygy/…"`; line 5 names `launch-gate-pre-specifications.md`, `scripts/validate_launch_administration.py` and `(VIS-4)`; line 298 names `(VIS-2)`; line 257 names the `SDR-n` and `P-n` decision-identifier conventions. Separately, `scripts/validate_launch_administration.py` line 116 hardcodes `DECISIONS_HOME = ".syzygy/governance/decisions"`, on which `LA-11` depends. §7's portable core also omits both tools, without which a v2.0 record cannot be validated, verdicted, or read.
*Fix:* replace the false clause with what is true — the schema's *field shapes* generalize; its `$id`, its doctrine citations and its `SDR-n`/`P-n` conventions are project bindings — and add the two tools (or a stated tool-independent procedure) to the portable core.

**5. [material] `launch-gate-pre-specifications.md` line 676 — §5 delegates the normative check enumeration to a script docstring and disclaims responsibility for its currency, and that docstring is already wrong.**
The clause: *"the tool's own docstring is the enumeration, and it is the tool's, not this instrument's, to keep current."* The docstring's `LA-13` entry reads *"a `delta` record can never support a gate decision (§2)"*. The code (line 769) gates `LA-13` entirely on `rec["formal"]`. I built a record with `formal: false`, `administration_kind: "delta"`, `fresh_context: false` and all rows `Met`; the tool printed `Computed gate verdict: READY FOR Capability 1 …`, then a §6 trend row carrying that verdict, then `record valid — the verdict above is computed from the rows`, exit 0, with no error and no note. This is not a regression against v1.18 — but it is a false statement in the artifact §5 makes normative, and the delta never records the delegation.
*Fix:* either restore the enumeration to §5, or make §5's delegation conditional on the docstring being fixture-bound; and either suppress the verdict/trend-row for a non-formal or delta record, or emit a diagnostic. The docstring's `LA-13` sentence must be corrected regardless.

**6. [minor] `launch-gate-pre-specifications.md` line 2021 — the §9 changelog quotes a stale fixture count.**
It says "74 mutation fixtures". `python3 scripts/validate_launch_administration.py --selftest` prints "75 fixtures, 0 failing"; the delta says 75 and explains the two fixture repairs (m17, m30) that moved it. A derived value quoted outside its owning artifact went stale between the delta and the changelog in the same commit.
*Fix:* state the count once, in the tool, and have §9 point at it — or correct it to 75.

**7. [minor] `round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` lines 219–242 — the "measured, not asserted" table is not reproducible by its stated method.**
Method stated: *"split both texts on `^## <n>\.` headings and sha256 each span."* Executing exactly that gives byte figures differing from every published row by a non-constant offset; three further readings (strip, strip-plus-drop-`---`, drop-blank-lines) matched at most 1 of 10 rows. No sha256 values are published, so the claim that spans were digested is unverifiable from the delta.
*Fix:* publish the span digests, or the script, and regenerate the counts.

**8. [minor] `LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` D-6 (lines 147–154) — two obligations deleted from §2 are unrecorded.**
"Never translate a verdict into softer language." and "Questions are **quoted verbatim** at the version administered" (→ "bound at"). D-6 records only what §2 gained. Neither deletion is a substantive loosening — the schema enum and the `LA-2` instrument-digest binding are equivalent-or-stronger — but a deletion of a normative sentence is a change of meaning, and this delta's stated purpose is that "no question was weakened" stay a reviewable claim.
*Fix:* record both deletions with the reasoning above.

**9. [minor] `LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` D-9 (lines 183–204) — the new-check table is incomplete and misstates its baseline.**
`LA-14`'s refusal of a placeholder G1 answer is new over `LG-4` (presence of a section) and is absent from the table. `LA-16`'s row does not disclose that the check runs only when `formal` **and** `prior_record is null`. And the `LA-13` row says the rule was "previously trusted", where v1.18's own §5 (line 630) said *"now checked rather than trusted"*.
*Fix:* add `LA-14`; scope the `LA-16` row; and either substantiate or withdraw "previously trusted".

**10. [minor] `LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` lines 278–308 — three limits are undisclosed and one names the wrong field.**
(a) With git unavailable, `LA-2`/`LA-3`/`LA-10`'s case-text comparison/`LA-11`'s existence check/`LA-15`'s ancestry check all degrade to a single `note:` and the tool prints "record valid" with a READY verdict — I passed a record carrying `sha256: "000…"`, `parameter_block_sha256: "111…"` and `launch_target: "Total nonsense target"`. (b) The `formal`-gated checks and the unconditional trend row. (c) The placeholder lexicon is applied to `falsification_attempt`, `bounded_reduction_plan`, `g1.critic_answer` and `pilot_recurrence_check.method` but not to `counterexample`, `falsification_summary` or `evidence.quote`. And the `launch_scope` limit note names `launch_scope`, where the reviewer-authored field that actually decides scope lawfulness is `deferred_wave_findings[].blocking_conditions_met`.
*Fix:* add the three; retarget the fourth.

**11. [minor] `launch-gate-pre-specifications.md` line 51 — "stored verbatim" is dropped from the record artifact class without record.**
The successor obligation survives in §5 line 701 ("Never edit a past administration; supersede it"), so nothing substantive is lost, but the deletion is unmentioned in D-2.
*Fix:* note it in D-2, or restore the word.

---

# What I could not test and why

- **The delta's "31 mutation-reverts, one per decision branch, 0 unwitnessed" and its kill counts (m1 2; m12 3; m23 2; m24 crashes; all others 1).** No mutation harness or mutant list is committed anywhere I could find, so the claim is not reproducible from the repository. I verified only the two mutants the delta names as having caught real defects (m13's prefix strip and m30's literal assertion) by reading the fixed code and its comments. The claim "0 unwitnessed" is unverifiable by an outside reviewer.
- **Whether the delta's baseline claim that no review is bound to v1.18 is complete.** I confirmed the absence of an RD-46 file in `round-2026-08e/reviews/` (27 files enumerated) and that RD-45 is titled `v117`. I did not sweep every reviews directory in the repository, so my denominator is one directory, not all.
- **The instrument's behavior under a real administration.** As the delta itself discloses, none has been run under v2.0. Everything I tested is a synthetic record I constructed, so my Criterion E conclusions are about the mechanism, not about whether a reviewer using it produces truthful fields.
- **Truthfulness of any evidence quote.** Content-blindness is by design and correctly disclosed; nothing in this review tests it.
- **Whether §3's questions are the *right* questions.** Out of scope for this comparison, and §3 is byte-identical, so the question does not arise for this amendment.
- **`jsonschema` cross-check parity.** The selftest reported "the base record validates identically under the reference jsonschema implementation" on this machine, so the subset interpreter agreed with the reference on the base record. I did not test agreement on my mutated records, and the delta correctly states that this cross-check gates nothing.
