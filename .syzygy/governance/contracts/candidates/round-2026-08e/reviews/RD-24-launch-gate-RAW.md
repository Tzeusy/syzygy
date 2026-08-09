# RD-24 — Launch-gate instrument review (round-2026-08e) — RAW
- Review id: RD-24
- Date: 2026-08-10
- Subject: launch-gate-pre-specifications.md (v1.4)
- Subject sha256: `1e28271ddde68729aa63e59d65dedf2f288899aa4ebcf5e44bd0353a545dd899`
- Frozen commit: e8a4f36
- Reviewer: isolated fresh-context session, Claude family (Fable 5). Same-family review — not the gate's family-diverse formal administration.
- Authoring context: none

---

## Method and what I ran

`[Observed]` I computed the subject digest myself (`sha256sum`, twice, unchanged: `1e28271d…`) and confirmed the clone is byte-clean (`git status --porcelain` empty) after all work; I made no edits inside the clone. Scratch fixtures were written outside it.

`[Observed]` I read the whole instrument (687 lines), `LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34), `scripts/launch_gate_results.py` (369 lines), and the VIS-2 / VIS-4 clauses in `.syzygy/governance/doctrine/vision.md`.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` → 13 fixtures, 0 failing, exit 0. Its printed cases cover vocabulary closure, softened verdicts, missing G1, both digests, the gate-verdict line, three READY-refusal paths, duplicate rows, empty rows, and a nonexistent commit. The mutation fixtures are genuine (each names the error substring it expects), so the self-test is a real check, not a tautology.

`[Observed]` Beyond the self-test I drove `validate()` directly (read-only import, `_git=False`) over six hand-built records to test the §4 formula's terms against the instrument's text. Those runs are cited inline as T1–T5 and "template-verbatim".

`[Observed]` Term sweeps over the instrument's own bytes (Python `re`, not shell grep, per the ugrep hazard) for: `chunk` (9 lines), `Capability` (1 line), `LAUNCH_TARGET` (6), `diverg` (3), `default reading` (3), `front door` (1), `owner act` (5), `not authority` (1), `Reopened` (5), `G1` (10), `F5`/`F6` (3 each), `FIRST_SPEC` (1), `sub-verdict` (2). Counts below rest on these sweeps.

`[Observed]` Existence checks only (no reads) on the instrument's pointer targets: `.syzygy/governance/decisions/launch-gate/` **MISSING**; `round-2026-08d/reviews` EXISTS; `contracts/candidates/DEFERRED-WAVE-POSTURE.md` EXISTS; `.syzygy/intent/OVERVIEW.md`, `PROJECT-STATUS.md`, `doctrine/vision.md` EXIST. A filename-only `find` for the first-spec document returned three files named `FIRST-OPENSPEC-SEQUENCE.md` (in `candidates/`, `round-2026-08c/`, `round-2026-08d/`). I did not open any of them, nor anything under `round-2026-08*`, nor any semantic delta, register, or the git log.

**What is strong, briefly.** `[Inferred]` The closed verdict vocabulary with the "a caveat that matters makes it Not met" rule, the "attempt to fail every question first" instruction, the pre-written `NEAR_MISSES` / `D2_*` tasks / `E4_CASES` / `MAJOR_SHAPE_COMMITMENTS`, E3's trace-table credibility protocol, the three-artifact-class block, and the §6 pilot note's four numbered reasons for refusing the pilot as a trend baseline are all real anti-gaming engineering. The findings below are about the seams between that engineering and the mechanism that will carry it.

---

## Dimension 1 — Authority

### RD24-01 — BLOCKING — the prepared owner act binds a digest the in-force instrument will not have

P-34's mechanism is digest-bound: step 2 records `instrument sha256: <the digest verified in step 1>`, and step 3 then says the status header "is then updated from candidate to in-force in the same change (that edit is part of the act, not a later drift)."

`[Observed]` Those two steps cannot both hold. I copied the instrument to a scratch path and applied one representative status-line edit (`status: candidate process policy — owner approval pending, see` → `status: in force as process policy (owner-approved) — see`); the digest moved from `1e28271d…` to `2abdc4e8…`. Any wording the owner chooses moves it.

`[Inferred]` The consequence is not cosmetic. The instrument's §2 requires that "the record quotes the instrument's sha256" at the administered commit, and `[Observed]` LG-2 verifies that quoted digest against `git show <commit>:launch-gate-pre-specifications.md`. So every administration after the act will quote and verify the *post-edit* bytes, while the approval block in the decisions tree attests to the *pre-edit* bytes. A later reader asking "which bytes did the owner approve as process policy?" gets a digest that matches nothing in force, and no check in the repository detects the gap.

*Direction:* perform the status edit first and bind the approval to the resulting digest (or exclude the `status:` line from the approved extent and say so).

### RD24-02 — MAJOR — the mandated record carries no non-authority statement, and its mandated home is the decisions tree

The boundary is stated well where a reader of *the instrument* meets it: line 49, "An administration verdict is never itself an owner act, and a READY verdict authorizes nothing," plus the header's `owner:` line and §8's closing note.

`[Observed]` It is absent from §5. Sweeping the instrument for `owner act` returns 5 lines (6, 49, 260, 570, 642) and for `not authority` returns 1 line (29) — none inside §5's record template (lines 474–496). The template's terminal field is `Gate verdict per §4: READY FOR <LAUNCH_TARGET> / NOT READY / READY-WITH-DEFERRALS(owner only)`. `[Observed]` The mandated home is `canonical_result_home: .syzygy/governance/decisions/launch-gate/` — inside the tree where owner decisions live.

`[Inferred]` A file in `decisions/` headed "Launch-gate administration" and ending "READY FOR Capability 1", with no banner disclaiming authority, is the instrument's own C4 fails-when: "an agent-authored artifact could pass as an owner act, or a pending decision is indistinguishable from a made one." The disclaimer travels with the definition; the artifact that will actually be read years later travels without it.

*Direction:* make a one-line non-authority banner a required first field of the §5 template.

### RD24-03 — MAJOR — P-34 binds more than the instrument says it governs

The instrument's header `governs:` reads: "how pre-specification readiness is evaluated — the question set, administration protocol, verdict vocabulary, verdict formula, results record format, and trend log." P-34 says approval makes it governing for "the question set, administration protocol, closed verdict vocabulary, **launch-scope parameters**, verdict formula, results-record format, and trend log."

`[Observed]` The two lists differ by exactly one term: launch-scope parameters (§8). `[Inferred]` This is a live difference, not a wording nit, because the header's `amendment_process` says "owner approval required once this instrument is in force." Under P-34's reading, changing `LAUNCH_TARGET` from Capability 1 to something else, or editing `E4_CASES` or `MAJOR_SHAPE_COMMITMENTS`, becomes an owner-approved amendment; under the instrument's own reading, §8 is outside what approval binds and could be re-parameterized freely. The owner would be signing a packet whose scope statement the subject does not confirm.

*Direction:* make the two lists identical, in whichever direction the owner intends.

### RD24-04 — MINOR — P-34's mechanism step 3 is garbled

`[Observed]` P-34 step 3 reads: "Commit with the approval in the message. The instrument's `status:` header — a governance-lifecycle state — header is then updated from candidate to in-force in the same change". The duplicated "header" leaves the sentence without a clean subject, in the one paragraph the owner executes literally.

*Direction:* repair the sentence when RD24-01 is addressed.

---

## Dimension 2 — Scope

### RD24-05 — BLOCKING — the launch-scope rule governs *defects*, but the formula ranges over *question verdicts*, and nothing bridges them

§4 says A–D "are answered over the whole repository … but a defect that lives *only* in a deferred wave's candidate semantics blocks the verdict **only if** it" meets one of five conditions, and "A deferred wave's internal defect meeting none of these is recorded in the results (it stays a finding) without converting the launch-scope verdict."

`[Observed]` The formula's second conjunct is "AND no `Not met` in launch-scope A–D", and §5's row format is `| Q | Verdict | Evidence |` — there is no per-row scope marker, and the instrument never says how to render a question whose only counterexample is an out-of-scope deferred-wave defect. The §2 rules push toward `Not met` ("Not met requires a concrete counterexample — the artifact and passage that fails"), since a counterexample exists; §4 pushes toward not blocking.

`[Observed]` I ran the two renderings through the named validator with everything else identical (all E Met, F1 Met, F2/F3/F4 Met, one out-of-scope C2 defect, the deferred-wave findings line filled in):

- **T1**, defect recorded honestly as `| C2 | Not met | defect confined to a deferred wave; §4 five conditions all absent |` → `ERROR LG-6: verdict claims READY but the rows refuse it — Not met in A–D: C2`.
- **T2**, same substance recorded as `| C2 | Met | (defect confined to a deferred wave, recorded outside launch scope) |` → no errors; READY FOR Capability 1 accepted.

Same answers, opposite gate outcomes, decided by a rendering choice the instrument does not specify. This is dimension 3's failure question answered in the affirmative, arriving through §4's scope prose.

*Direction:* add a scope column (or a `Not met (out of launch scope)` row form) that the formula and LG-6 both read.

### RD24-06 — MAJOR — `LAUNCH_TARGET` names a capability the instrument never locates

`[Observed]` Sweeping the instrument for `Capability` returns exactly one line: 581, `Capability 1 — Project registration and honest shape visibility`. No citation, no defining artifact, no scope statement accompanies it.

`[Inferred]` Three load-bearing operations depend on knowing what Capability 1 *is*: the formula's "every E question `Met` **for the named launch target**"; blocking condition 3, "is a dependency of the launch target"; and `DEFERRED_WAVE_POSTURE`'s claim that deferred waves are "not used by the launch target". An administrator with only the instrument, the doctrine, the overview, and repository read access must reconstruct the capability's extent from the corpus — which is precisely the derivation dependency §1 forbids for questions and §7 says should live in the parameter block.

*Direction:* give `LAUNCH_TARGET` a path-and-quote citation to the artifact that defines Capability 1.

### RD24-07 — MAJOR — blocking condition 1 rests on an undefined term

`[Observed]` "is on the default reading or task route" (line 441) is the first of the five conditions. Sweeping for `default reading` returns 3 lines (303, 385, 441) and for `task route` returns 1 (441); none defines the term. D2 introduces a third, unreconciled name for the neighbourhood: "from the front door" (line 292). D3 and F4 use "default reading path" as if defined.

`[Inferred]` This is the condition most likely to decide whether a deferred-wave defect blocks, and two administrators will draw the route set differently — one from `README.md` + `AGENTS.md` + the overview, another including anything reachable in two hops from the task router. Contrast A3/D2/E4/A5, where v1.4 deliberately closed the populations; this one was left open.

*Direction:* define the default route set in the parameter block, by path enumeration.

### RD24-08 — MINOR — A5's closed population may straddle the deferred waves, with no stated interaction

`[Observed]` `MAJOR_SHAPE_COMMITMENTS` is closed and fixed (11 entries), which is the right shape. It includes `context packets` and `Mission Control`. `[Unknown]` Whether those commitments are governed by the deferred waves C1/C2/D1/D2 cannot be determined from the instrument's own text — it never states what any wave contains. `[Inferred]` If they are, A5's two-way table spans deferred material and inherits RD24-05's rendering ambiguity for a question that is otherwise well-specified.

*Direction:* mark each `MAJOR_SHAPE_COMMITMENTS` entry with its governing wave, or state that A5 is answered wave-blind.

---

## Dimension 3 — Formula

### RD24-09 — BLOCKING — "F1 is not diverging" is not an outcome of any question, and the named check for it cannot fire

§2 fixes the vocabulary: "**Verdict vocabulary is closed:** `Met`, `Not met`, `Unknown(reason)`. Nothing else." §4's third conjunct is "AND F1 is not diverging", qualified by "An `Unknown` F1 (no trend yet) does not veto; a diverging F1 does."

`[Observed]` "Diverging" is not in the closed vocabulary and the instrument gives no mapping from F1's `Met`/`Not met`/`Unknown` to diverging/not-diverging. It is not simply `Not met`: F1's own fails-when has two limbs — "each round's fixes mint the next round's findings" (divergence) **or** "no one can state what would end the cycle" (a missing stop condition, which is not divergence). So `F1 = Not met` is genuinely ambiguous with respect to the conjunct.

`[Observed]` The named validator does not resolve it. `f1_row = re.search(r"^\|\s*\**F1\**\s*\|([^|]*)\|", txt, re.M)` captures the **verdict** cell, not the evidence cell — and the verdict cell can never legally contain "diverging" (LG-3 would reject it). I confirmed the conjunct is dead:

- **T3** `| F1 | Not met | x |` with READY → accepted, no error.
- **T4** `| F1 | Not met | rounds are diverging |` with READY → accepted, no error.

A record stating in its own evidence that the process loop is diverging passes as READY. §4's stated protection — "a project must not launch while … the process loop is visibly diverging (F1)" — is unenforced by the mechanism the instrument names, and undecidable from the instrument's text.

*Direction:* express the conjunct as an F1 verdict predicate (e.g. F1 ∈ {Met, Unknown}) so it lives inside the closed vocabulary.

### RD24-10 — MAJOR — a record written to §5's own template is rejected by the validator §5 names

§5 mandates the format and then says "`scripts/launch_gate_results.py` validates a record — verdict vocabulary, counts, G1 presence, named commit, digests".

`[Observed]` I built a record using §5's literal field names and ran it: two errors.
- `LG-6: no GATE VERDICT line found` — the template's terminal field is `Gate verdict per §4:`, while `GATE_VERDICT_RE` matches `GATE VERDICT[:\s]+…` case-sensitively and with no room for "per §4" between the phrase and the verdict.
- `LG-3: question G1 carries verdict 'n/a — no verdict' — outside the closed vocabulary` — but §3 forbids G1 a Met/Not-met verdict ("G1 yields no Met/Not-met verdict"), so *every* legal G1 row is a vocabulary error. LG-4 accepts either a `## …G1` heading or a `| G1 |` row, so the row form reads as sanctioned and is a trap.

`[Inferred]` The gate's output line — the single sentence the owner reads — is not reliably parseable from the format the instrument prescribes, and the failure is silent in the direction that matters: the trend row printed `| … | — |` for the gate verdict.

*Direction:* make §5's template emit the literal token the validator matches, and give G1 a non-table slot in the template.

### RD24-11 — MINOR — an `Unknown` F2 has no stated handling, unlike `Unknown` F1

`[Observed]` The qualifications state that "`Unknown` in launch-scope A–D does not block by itself" and that an Unknown F1 does not veto, but say nothing about F2. F2's conjunct is "F2 is `Met` OR explicitly owner-deferred with a bounded reduction plan", and deferral presumes a Not-met with "maximum new meta-artifacts, artifacts to retire, stop condition". `[Inferred]` F2's operational proxies are trend-shaped ("the artifact-count trend across cycles"), so Unknown is a live outcome at Administration 1, and it blocks READY with no defined route out.

*Direction:* say whether an Unknown F2 is deferrable or blocking.

### RD24-12 — MINOR — F5 and F6 carry no formula weight, and the asymmetry is unexplained

`[Observed]` The qualifications explain why F1/F3/F4 are conjuncts. F5 (assurance independence) and F6 (governance effort) — both added in v1.4 — appear nowhere in §4. `[Inferred]` F5 can be `Not met` (the instrument itself anticipates the same-family case: "A gate administered only by the corpus's own authors' model family is this question's own example") and the gate can still read READY, with the disclosure living only in the record's prose.

*Direction:* add one sentence saying the omission is deliberate, or make F5 a conjunct.

---

## Dimension 4 — Reproducibility

### RD24-13 — MAJOR — `FIRST_SPEC_CANDIDATE` is not fixed, and E3 depends on it

`[Observed]` The parameter reads: `per the current first-OpenSpec-sequence document, if one exists at the administered commit`. A filename-only sweep at e8a4f36 found **three** files named `FIRST-OPENSPEC-SEQUENCE.md` (under `contracts/candidates/`, `round-2026-08c/`, `round-2026-08d/`) plus a `round-2026-08e/FIRST-SPEC-TRACE-TABLE.md`. The instrument states no rule for choosing among them — "the current" is exactly the judgment a fresh reviewer cannot make without the round history §2 withholds.

`[Inferred]` E3, which the instrument calls "the sharpest single gate" and which requires handing the reviewer "the first spec's charter", and E2 ("Is the first specification identified") both take this parameter as input. The "if one exists" clause also leaves the verdict undefined when none does: E2 `Not met` (nothing identified) and E2 `Unknown` (input absent) are both defensible readings, and they differ — an `Unknown` E blocks READY just as a `Not met` does, but they trend differently in §6's columns.

*Direction:* name the one path and its digest in the parameter block, and state the verdict rule when it is absent.

### RD24-14 — MAJOR — §6 preloads a corpus finding the reviewer is forbidden to read

§6's pilot note ends: "At that administration, the pilot's corpus-level recurrence note applies: if the retired-phrase defect the pilot documented under E6/F1/F3 is still present, it belongs in the Reopened column, not the Not-met column alone."

`[Observed]` This is a normative instruction addressed to the next administrator. Its referent — "the retired-phrase defect the pilot documented" — is described nowhere in the instrument; §2 withholds "prior administrations of this gate (except when answering F1, which needs the trend log)", and the pilot record is not the trend log. `[Observed]` I could not identify the defect from the instrument's text; the sentence is unexecutable from the instrument alone, which is dimension 4's failure condition exactly.

`[Inferred]` Secondarily this is a §7 violation by the instrument against its own rule — "everything project-specific lives in the parameter block" — with a corpus-specific finding lodged in §6, a section §7 declares invariant.

*Direction:* move the recurrence instruction into §8 and state the defect in enough detail to be recognized without the withheld record.

### RD24-15 — MAJOR — the withhold rule is unenforceable against the read access the same section grants

§2 gives the reviewer "Read access to the repository at a **named commit**" and, four lines later, withholds "Authoring history, prior review results, and prior administrations of this gate."

`[Observed]` The withheld class lives inside the granted scope: `round-2026-08d/reviews` exists in the repository (existence check), and the canonical result home is a repository path. Meanwhile F4 asks whether "any stale claim, superseded offering, or dead route is reachable from a default reading path", F2's proxies call for "a sweep for artifacts no reading route reaches", and C3 requires checking status claims against current bytes — all repo-wide sweeps.

`[Inferred]` One administrator will exclude the reviews trees and under-count F2/F4; another will sweep them and be contaminated for F1/E-section purposes. The instrument gives no rule for the collision, so the freshness guarantee it advertises is procedural only.

*Direction:* state the reconciliation — e.g. reviews trees are in scope as *objects* of the F2/F4 sweeps but never read for content.

### RD24-16 — MAJOR — E4's comparison target is never named

E4: "the reviewer classifies each from its text alone, then compares against **the project's own routing**. Disagreement with the project's routing is a fail; the project's routing disagreeing with itself over parallel cases is a fail."

`[Observed]` Sweeping for `routing rule` returns one line (613), inside E4's own preamble; the parameter block contains no pointer to the artifact holding the project's shape/spec routing rule. `[Inferred]` The reviewer must locate the routing authority themselves — and if they locate a different one than the last administrator did, E4 verdicts stop being comparable across the trend log, which is the stated reason the cases were fixed in the first place ("so E4 verdicts are comparable across the trend log"). The same gap makes E4's classification target implicit: the instrument never says the classification is two-valued (shape side / spec side), though it is inferable from the question stem.

*Direction:* add an `E4_ROUTING_AUTHORITY` parameter with a path and clause citation.

### RD24-17 — MINOR — the canonical result home does not exist, and TREND-LOG.md is named only in the header

`[Observed]` `.syzygy/governance/decisions/launch-gate/` is MISSING at e8a4f36. `TREND-LOG.md` appears on exactly one line of the instrument (18), inside the header comment; §6 says "Append one line per administration" without naming the file. `[Inferred]` Benign for Administration 1 (F1 is legitimately Unknown with no trend), but F1's evidence source is a path that does not exist and a filename mentioned once in a parenthetical.

*Direction:* name the trend-log path in §6 itself.

---

## Dimension 5 — Administrability

### RD24-18 — MAJOR — "chunk" is undefined, and five questions quantify over it

`[Observed]` Sweeping for `chunk` returns 9 lines: B1 (206, 208), B2 (212, 214), B4 (222, 224), B5 (229, 230), and D2's seam requirement (297, "between two chunks"). The term is defined nowhere in the instrument, and the parameter block binds no `CHUNKS` value — though it does fix `REQUIRED_WAVES: [A, B]` and `DEFERRED_WAVES: [C1, C2, D1, D2]`, which are never connected to the word.

`[Inferred]` B4 ("Can any single chunk be rejected without collapsing the whole") gives materially different answers under chunk = wave, chunk = RFC, or chunk = capability, and B2's acyclicity claim likewise. D2's seam task is fixed by text so it survives, but B1–B5 — one seventh of the question set — are not answerable identically by two administrators. Note the self-referential edge: D3 asks whether the project's coined vocabulary is "defined-before-use", and the instrument's own coined term is not.

*Direction:* bind `CHUNK_UNIT` in the parameter block (waves, on the evidence of §8's own vocabulary).

### RD24-19 — MAJOR — the trend row reports Deferred and Reopened as zero without evidence

§6's table has `| Deferred | Reopened |` columns, and §5 says the validator "generates the trend row".

`[Observed]` §5's record template contains no `Deferred:` field and no `Reopened:` field — the sweep for `Reopened` returns 5 lines (511, 520, 521, 534, 659), none in §5. `[Observed]` The validator therefore derives them by other means: `deferred = len(re.findall(r"owner-deferred", txt, re.I))` — a substring frequency count over the whole record — and `reopened = "0"` whenever no `Reopened…: <n>` line is found. In T1, a record that explicitly filled in "Deferred-wave findings recorded outside launch scope: C2 defect …" printed `| … | 0 | 0 | …` for Deferred and Reopened.

`[Inferred]` This is VIS-2 turned on the gate's own instrument: "No evidence means Unknown, not success… nor turn anything green — without current evidence." A zero in the Reopened column is a positive claim that no previously-resolved finding recurred, and it is produced by the absence of a field. §6 leans on that column hard — "a nonzero Reopened column indicts the resolution process" — and §6's pilot note directs the next administrator to use it. As built, it will read zero.

*Direction:* add explicit `Deferred:` and `Reopened:` count fields to §5 and make their absence an LG error, not a zero.

### RD24-20 — MINOR — five questions quantify over populations with no closed extension

`[Observed]` I classified all 35 questions (A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1) by whether they quantify over a population and whether that population has a defined extension. Four have parameter-fixed closed sets: A3 (`NEAR_MISSES`), A5 (`MAJOR_SHAPE_COMMITMENTS`), D2 (three fixed tasks), E4 (`E4_CASES`). Several are closed by construction (C1's four named layers; C4's and F3's populations are the project's own enumerations; F2's artifact set is the file set). Five quantify over populations the instrument neither closes nor points to: **C2** ("every normative 'should'"), **C5** ("each load-bearing assumption"), **C7** ("each irreversible decision"), **D3** ("each coined term"), **D4** ("the entry/summary documents" — `ENTRY_DOCUMENT` fixes only the first).

`[Inferred]` Each of these is a universal whose `Not met` needs a counterexample (easy) but whose `Met` needs an absence sweep with a denominator (undefined). The likely failure is a confident `Met` resting on a partial read — the pattern A5 was explicitly rewritten to prevent.

*Direction:* give each a denominator rule (a path glob or a named enumeration), even a coarse one.

### RD24-21 — MINOR — §5 has no slot for G1 or for E1's five sub-verdicts, and the natural workarounds fail silently

`[Observed]` §3 requires that E1's "form, home, granularity, acceptance authority, change process — five answers, not one" be recorded, and that G1's proposals be "recorded in the results". §5's template shows only `| Q | Verdict | Evidence |` rows and no G1 or sub-verdict field. `[Observed]` Sub-verdict rows are silently dropped by the parser: `| E1a (form) | Met | x |` → NO MATCH, `| E1.form | Not met | x |` → NO MATCH, while `| E1 | Met | x |` and `| **E1** | Met | x |` parse. A dropped `Not met` sub-verdict does not appear in LG-5's computed counts, which §5 advertises as "counts computed from the rows, never transcribed". The G1-row trap is covered under RD24-10.

*Direction:* add an E1 sub-verdict block and a G1 section to the §5 template.

---

## Findings table

| id | class | summary |
|---|---|---|
| RD24-01 | BLOCKING | P-34's approval binds a digest the post-act, in-force instrument will not have |
| RD24-05 | BLOCKING | §4's launch-scope rule governs defects but the formula reads question verdicts; T1/T2 show opposite gate outcomes from identical answers |
| RD24-09 | BLOCKING | "F1 is not diverging" maps to no defined outcome, and the named check reads the verdict cell so it can never fire (T3/T4) |
| RD24-02 | MAJOR | The mandated record carries no non-authority statement and is stored in the decisions tree — the instrument's own C4 fails-when |
| RD24-03 | MAJOR | P-34 says approval binds the launch-scope parameters; the instrument's `governs:` line does not list them |
| RD24-06 | MAJOR | `LAUNCH_TARGET` names Capability 1 once, with no pointer to a defining artifact |
| RD24-07 | MAJOR | Deferred-wave blocking condition 1 rests on the undefined "default reading or task route" |
| RD24-10 | MAJOR | A record written to §5's own template is rejected by the validator §5 names (gate-verdict line, G1 row) |
| RD24-13 | MAJOR | `FIRST_SPEC_CANDIDATE` is unfixed — three candidate files exist at the commit; E2/E3 take it as input |
| RD24-14 | MAJOR | §6 instructs a Reopened classification for a pilot defect §2 withholds from the reviewer |
| RD24-15 | MAJOR | §2's withhold list lives inside §2's grant of repository read access, with no reconciliation |
| RD24-16 | MAJOR | E4's comparison target — "the project's own routing" — is never named |
| RD24-18 | MAJOR | "Chunk" is undefined and unbound; B1–B5 quantify over it |
| RD24-19 | MAJOR | Trend-row Deferred and Reopened print zero from missing fields — VIS-2 violated by the gate's own measurement |
| RD24-04 | MINOR | P-34 mechanism step 3 is a garbled sentence in the paragraph the owner executes |
| RD24-08 | MINOR | A5's closed population may straddle deferred waves with no stated interaction |
| RD24-11 | MINOR | An `Unknown` F2 has no stated handling, unlike `Unknown` F1 |
| RD24-12 | MINOR | F5 and F6 carry no formula weight and the asymmetry is unexplained |
| RD24-17 | MINOR | The canonical result home does not exist; TREND-LOG.md is named once, in a header parenthetical |
| RD24-20 | MINOR | C2, C5, C7, D3, D4 quantify over populations with no closed extension (sweep over all 35 questions) |
| RD24-21 | MINOR | §5 has no slot for G1 or E1's five sub-verdicts; sub-verdict rows are silently dropped |

Three BLOCKING, eleven MAJOR, seven MINOR.

VERDICT: REVISE
