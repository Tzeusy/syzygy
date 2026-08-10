# RD-33 — Launch-gate instrument re-review, v1.5 exact bytes (round-2026-08e, frozen commit 997d9bd)

- Review id: RD-33
- Date: 2026-08-10
- Subject: `launch-gate-pre-specifications.md` (v1.5), repo root
- Subject sha256, recomputed by me this session: `0522ef47757c4199a044ef10f98c78b1ff1d66adb2375d96dd08459593bdf898` — **matches** the charter's stated digest
- Frozen clone: `…/scratchpad/clone-08e-r7`, `git rev-parse HEAD` = `997d9bdf257e5a47689373984105cb4d0e413a42`, `git status --porcelain` empty before and after all work
- Reviewer: isolated fresh-context session, Claude family (Opus 5). Same-family re-review — not the gate's family-diverse formal administration (F5's own example applies here too)
- Authoring context: none. I read nothing outside the clone.

---

## Method and what I ran

`[Observed]` I recomputed the subject digest with `sha256sum` and independently through the validator's own `git_show`/`sha256_bytes` path against `997d9bd:launch-gate-pre-specifications.md` — both `0522ef47…`. The §8 parameter block, extracted by the validator's own `param_block_bytes`, hashes to `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6` (104 lines, `## 8.` heading through the separator before `## 9.`).

`[Observed]` I read, in charter order: `AGENTS.md` (byte-identical to the live copy — `diff` empty); `RD-24-launch-gate-RAW.md` (262 lines, 21 findings, `VERDICT: REVISE`); the RD-24 section of `DISPOSITION-REGISTER.md`; the instrument in full twice (802 lines); `LAUNCH-GATE-v1.5-SEMANTIC-DELTA.md` (125 lines); `scripts/launch_gate_results.py` (479 lines); `LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34, 113 lines); `decisions/launch-gate/README.md` and `TREND-LOG.md`.

`[Observed]` `python3 scripts/launch_gate_results.py --selftest` → **22 fixtures, 0 failing, exit 0**. The nine v1.5 fixtures named in the dispositions are all present and each names the error substring it expects: scoped-row pair (RD24-05 T1/T2, plus scoped-outside-A–D), F1 `Not met` blocking (RD24-09 T3), G1 verdict row, missing `Deferred count:`, missing `Reopened count:`, E1 missing sub-rows, E1 rollup over a non-Met sub-row. The delta's "22 fixtures" figure matches the bytes.

`[Observed]` Beyond the self-test I built **ten synthetic administration records outside the clone** (`…/b78f52c3…/scratchpad/rd33/`) and ran the real validator against them, most with git checks **on** (real commit `997d9bd`, real instrument and parameter-block digests, so LG-1/LG-2 actually executed). These are cited below as r1–r5 and p1–p5. No file was written into the clone; the clone stayed byte-clean.

`[Observed]` Term sweeps over the instrument's 802 lines using Python `re` (not shell grep — ugrep hazard, rule 1), each with the full-file denominator stated inline below: `DEFAULT_ROUTE_SET` (4 lines), `default reading|task route|front door` (5), `diverg` (1), `GATE VERDICT|Gate verdict` (4), `chunk|CHUNK` (13), `out of launch scope` (4), version strings (12), `Deferred count|Reopened count|Reopened` (9). Repo-wide sweeps: filename sweep for `FIRST-OPENSPEC-SEQUENCE.md` (3 files), `WAVE-*MANIFEST*` (6 files), and a cross-repo regex for launch-gate version references (29 hits across 15 files).

`[Observed]` Quote verification (rule 8): the `LAUNCH_TARGET` sentence and the `FIRST_SPEC_CANDIDATE` self-declaration were checked against their cited sources with whitespace normalization and markdown emphasis/blockquote markers stripped. `CG-2a` was checked to exist in `scripts/check_governance.py` (11 lines).

`[Observed]` I ran `git diff e8a4f36 HEAD` over the three changed artifacts (instrument +173/−, validator +166/−, P-34 +53/−) to separate *new* defects from ones RD-24 did not reach.

`[Unknown]` I did not run the full `check_governance.py` battery, did not read the round-08d pilot record, and did not administer the gate. All answer sets below are synthetic.

---

## Per-finding repair verification — all 21 RD-24 findings

| RD-24 | Class | Disp. | Status | Anchor in the v1.5 bytes |
|---|---|---|---|---|
| RD24-01 | BLOCKING | R | **verified-closed** | P-34:83–103. "Edit the instrument's `status:` header … in the working tree. That edit is part of the act, not a later drift." → step 2 digests the *result* → step 3 writes the approval block into the decision file (which does not move instrument bytes) → step 4 one commit. The approval attests the in-force bytes. See RD33-11 for one uncovered branch. |
| RD24-05 | BLOCKING | R | **verified-closed** (repair effective; two new defects it introduced — RD33-01, RD33-02) | §2:125–132 adds `Not met (out of launch scope)` to the closed vocabulary; §4:459–460 and §4:482–489: "rendering such a defect as a bare `Met` is a false row; rendering it as a bare `Not met` blocks a verdict §4 says it must not block — the scoped form is the only honest rendering." Validator LG-3:185–188 + LG-6:225–230; fixtures 14–16. The T1/T2 ambiguity is genuinely gone: the rendering is now specified, not chosen. |
| RD24-09 | BLOCKING | R | **verified-closed** | §4:461–462 "AND F1 is `Met` or `Unknown` — a `Not met` F1 blocks, whichever of its two limbs failed"; §4:498–502; §4:468–469 "Every term of this formula is a predicate over the closed verdict vocabulary". Sweep for `diverg`: **1 line of 802** (L501), inside F1's own explanation — the word is out of the formula. Validator:242–244 replaces the dead evidence-cell regex; fixture 17. |
| RD24-02 | MAJOR | R | **verified-closed** | §5:529–530, the template's first body lines: "> This administration record is evidence, never an owner act; its verdict authorizes nothing (instrument preamble; VIS-4)." Reinforced by `decisions/launch-gate/README.md` ("A record here is **evidence, never an owner act**"). Not machine-enforced; the register did not claim it would be. |
| RD24-03 | MAJOR | R + O | **R verified-closed; O partial** | `governs:` §header:8–10 now reads "…the launch-scope parameters (§8), results record format, and trend log" — identical to P-34:17–20. The **O** half is weaker than claimed: P-34:20–21 states the lists are "aligned at v1.5; RD24-03" as settled and offers the owner no choice on it (only F5 promotion is offered, under option (b)). See RD33-08(b). |
| RD24-06 | MAJOR | R | **verified-closed** | §8:664–670. Quote verified against `DEFERRED-WAVE-POSTURE.md:4–5` — present verbatim once markdown `**` emphasis and `> ` markers are stripped. `[Observed]` My first pass reported it absent; that was my normalization, not the bytes. |
| RD24-07 | MAJOR | R | **verified-closed** (delta overstates — RD33-07a) | §8:649 enumerates six paths and binds them explicitly: "the default reading and task routes for D2/D3/F4 and §4's blocking condition 1". D2:315 and D3:327 name the parameter in their own text; F4:415 and §4:476 do not. |
| RD24-10 | MAJOR | R | **verified-closed** (claimed fixture absent — RD33-08a) | §5:561 `GATE VERDICT:` literal; §5:565–566 "The terminal line's `GATE VERDICT:` token is literal"; §5:551–553 the `## G1 — completeness critic` section slot; validator:175–178 makes a `\| G1 \|` row an error and LG-4:196 now requires the heading form. **Proved by construction:** r1, a full §5-template-shaped record with all 39 rows and every template field, validates clean with git checks **on** (LG-1 and LG-2 both executed against `997d9bd`). |
| RD24-13 | MAJOR | R | **verified-closed** | §8:644 names one path and the absent-case rule ("E2 is `Not met` (nothing identified), never `Unknown`"). The path exists; `FIRST-OPENSPEC-SEQUENCE.md:1` is "revision 3" and its banner declares "**This is the single current first-spec document**". Three files still share the basename (sweep: 3), but the parameter now names one. |
| RD24-14 | MAJOR | R | **verified-closed on the primary limb; secondary limb open** (RD33-07b) | §8:655 `PILOT_RECURRENCE_CHECK` describes the defect in place ("a retired ceremony phrase still standing as the live acceptance gate in two digest-carrying owner documents") and names the sweep population via CG-2a, which exists in `check_governance.py` (11 lines, incl. "CG-2a retired acceptance phrase confined"). Executable from the instrument alone. But §6:598–609 still carries the project-specific pilot paragraph (date, v1.3, commit `067d8a0`), so §6 is not project-invariant as the delta claims. |
| RD24-15 | MAJOR | R | **verified-closed** | §2:99–104: "trees holding prior reviews and administrations are in scope as **objects** of the F2/F4/C3 sweeps … but are never **read for content** … A reviewer who has read them for content records that fact as a materials deviation." |
| RD24-16 | MAJOR | R | **verified-closed** (residual — RD33-12) | §8:648 names `SURFACE-CLAUSE-ROUTING-MATRIX.md` and supplies the two-valued mapping ("its OS routes are the spec side, all others the shape side"); E4:374 cites the parameter and states the classification is two-valued. The matrix's four routes (OS / N/A / CR / IR) map cleanly onto that binary. |
| RD24-18 | MAJOR | R | **verified-closed** | §3 B-preamble:218–220 "The unit of decomposition — 'chunk' throughout this section and in D2's seam task — is bound by `CHUNK_UNIT` … never chosen by the reviewer"; §8:647 binds it to the six wave acts, "the wave manifests are the chunk boundaries". Six manifests exist (`candidates/wave-manifests/WAVE-{A,B,C1,C2,D1,D2}-MANIFEST.txt`). |
| RD24-19 | MAJOR | R | **verified-closed** (small residual — RD33-09) | §5:557–558 adds both fields; §5:566–568 "their absence is a validation error, never an implicit zero (VIS-2 applies to the gate's own record)"; validator:258–268 replaces `deferred = len(re.findall("owner-deferred"))` and `reopened = "0"` with parsed required fields; fixtures 18–19. Mutation-confirmed. |
| RD24-04 | MINOR | R | **verified-closed** | P-34:83–85 now reads cleanly: "Edit the instrument's `status:` header — a governance-lifecycle state — from candidate to in-force, in the working tree." The duplicated "header" is gone. |
| RD24-08 | MINOR | **J** | **judgment recorded where claimed** | §8:683–687: "A5 is answered repository-wide and **wave-blind**: whether a commitment's governing semantics sit in a required or a deferred wave does not change its row … and A5's fail condition is unchanged by launch scope." Also in the register (row RD24-08) and delta D-8. The eleven-entry list is unchanged. |
| RD24-11 | MINOR | R | **verified-closed** | §4:505–508: "An `Unknown` F2 is deferrable on exactly the same owner-deferral terms as a `Not met` F2". Validator consistent (`verdicts.get("F2") != "Met"` covers Unknown). |
| RD24-12 | MINOR | R + O | **both halves present** | §4:509–515 states the omission is deliberate and that "a `Not met` F5 or F6 travels as stated owner risk, never silently"; P-34:46–50 offers the promotion as a prepared amendment under option (b), with its cost stated ("no same-family administration can ever read READY"). |
| RD24-17 | MINOR | R | **verified-closed** | §6:580–581 names `.syzygy/governance/decisions/launch-gate/TREND-LOG.md`. The home exists with a README that states what may live there and disclaims authority, and an empty TREND-LOG carrying its header row and the correct "zero rows is the correct current state, not a gap". |
| RD24-20 | MINOR | R | **verified-closed** | Five denominators bound and cited from their questions: `C2_POPULATION` (§8:650, cited at C2:266–268), `C5_POPULATION` (651 / C5:287–288), `C7_POPULATION` (652 / C7:301–302), `D3_POPULATION` (653 / D3:329–330), `D4_POPULATION` (654 / D4:336–337). |
| RD24-21 | MINOR | R | **verified-closed** (residual — RD33-10) | §5:543–548 adds the five sub-rows plus the rollup row; `ROW_RE` now accepts `E1-acceptance-authority`-shaped IDs; LG-8:201–211 cross-checks; fixtures 21–22. |

**Tally, stated with its denominator:** of 21 RD-24 findings, **19 verified-closed**, **1 closed with its O-half only partly delivered** (RD24-03), **1 closed on its primary limb with its secondary limb open** (RD24-14). **Zero repairs are absent.** Every claimed repair I looked for was present in the bytes. Two BLOCKING repairs (RD24-05, RD24-09) and one MAJOR (RD24-10) I confirmed by execution, not by reading.

---

## New findings

### RD33-01 — MAJOR — the scoped row's one corroboration requirement is unenforced, and a self-contradicting record validates clean

§4:482–485 makes the scoped form conditional: "its question's row takes the verdict `Not met (out of launch scope)`, and the defect is listed on the record's deferred-wave findings line."

`[Observed]` **r2**: a record with `| C2 | Not met (out of launch scope) | … |`, `Deferred-wave findings recorded outside launch scope: none`, and `GATE VERDICT: READY FOR Capability 1 …` validates with **0 errors** (git checks on, LG-1/LG-2 executed). The record asserts a scoped defect exists and simultaneously that none exists, and the gate reads READY.

`[Inferred]` The BLOCKING repair for RD24-05 rests on the scoped form being *the honest rendering*. Its only honesty guarantee — that the defect is named on the findings line, where a reader can check it against §4's five conditions — is prose with no check and no fixture. LG-3 validates the *word*; nothing validates the *disclosure*.

*Direction:* make a nonzero scoped-row count require a non-empty deferred-wave findings line (LG-9), with a mutation fixture.

### RD33-02 — MAJOR — the scoped form launders the trend log, and §6's own anti-laundering rule now fails against the instrument's own vocabulary

§6:593–594: "A deferral is a finding until resolved: moving a finding from Not-met to Deferred must never improve the read of any other column." The delta's "What did not change" states §6's columns are unchanged — and they are.

`[Observed]` **p1**: prior record `| C2 | Met |`, current record `| C2 | Not met (out of launch scope) |`, all else identical → trend row `| 2026-08-10 | 997d9bd | 0 | 1 | 0 | 0 | 0 | NOT READY |`. A brand-new deferred-wave finding registers in **no** column: not Not-met (excluded by design), not Deferred (that field counts owner-deferrals), not New-findings. Only an ephemeral stdout `NOTE` mentions it, and the NOTE is not the appended line.

`[Observed]` **r5**: the prior/current comparison is additionally asymmetric in code. `prior_not` is built with `.strip().startswith("Not met")` (validator:274) — which matches the scoped form — while `cur_not` uses `v == "Not met"` (validator:275), which does not. With prior `C2` scoped and current `C2` a plain `Not met`, "New findings vs prior" prints **0**. This asymmetry did not exist in v1.4; the code is unchanged, but the new verdict string made `startswith` overreach.

`[Inferred]` F1 — a §4 conjunct — is answered from the trend log and only from it ("*Requires the trend log (§6)*", §3:393). A finding class that is structurally invisible to every trend column cannot be part of the convergence measure, so the more defects a round renders scoped, the better convergence reads. This is VIS-2 turned on the gate's own instrument in exactly the way RD24-19 was, one level up: the previous defect was a zero printed from a missing field; this is a zero printed from a finding that exists.

*Direction:* add a Scoped column to §6 (an instrument amendment, so it must go into the P-34 offer, not after it), and fix the `startswith`/`==` asymmetry.

### RD33-03 — MAJOR — READY-WITH-DEFERRALS self-authorizes: LG-7 is satisfied by the template's own "(owner only)" label

§4:516–517: "The gate can be *passed with enumerated deferrals* only by explicit owner decision, never by the reviewer or the administering session." §5's terminal template line (561–562) ends `READY-WITH-DEFERRALS (owner only)`. LG-7 fires only when `"owner" not in gv.lower()` **and** no `owner decision` string appears anywhere (validator:248–252).

`[Observed]` **r3**: `GATE VERDICT: READY-WITH-DEFERRALS (owner only)`, with no owner-decision citation anywhere in the record → **0 errors**; trend row carries the deferral verdict. The check is defeated by copying §5's own parenthetical.

`[Observed]` LG-7 has **no `--selftest` fixture**: sweeping all 22 fixture names and the whole selftest body for `LG-7` returns 0 hits, and `DEFERRALS` does not appear in the selftest at all. The module docstring's header — "Checks (each with a `--selftest` mutation fixture)" (validator:13) — is false for LG-7, and for LG-2's digest-mismatch path (no fixture name contains "mismatch"; the git-on fixture exercises LG-1's commit-existence path).

`[Observed]` LG-7's logic is unchanged since `e8a4f36` — the hole is pre-existing. But at v1.4 no template-shaped record ever reached it, because the gate-verdict line did not parse (RD-24's own finding). RD24-10's repair made a dead check live and defective in the same change, and no fixture would have caught it.

*Direction:* require an explicit `Owner deferral decision: <path/id>` field for any `READY-WITH-DEFERRALS`, matched against a path that exists; add the fixture.

### RD33-04 — MAJOR — a reviewer can self-authorize an F2 deferral under a plain `READY FOR` verdict, bypassing LG-7 entirely

§4:503–505: "Only the owner may defer F2, and only against a bounded reduction plan (maximum new meta-artifacts, artifacts to retire, stop condition)."

`[Observed]` **r4**: `| F2 | Not met | corpus still growing; treated as owner-deferred pending a reduction plan |` with `GATE VERDICT: READY FOR Capability 1` → **0 errors**. The `f2_deferral` regex (validator:237–239) accepts any line containing both `F2` and `owner-deferred` — including the reviewer's own evidence cell. No bounded plan is required, no owner citation is required, and LG-7 never runs because the verdict word is `READY FOR`, not `READY-WITH-DEFERRALS`.

`[Inferred]` The instrument shares the defect: §4's formula lists "F2 is `Met` OR explicitly owner-deferred…" as a conjunct of **READY FOR `<LAUNCH_TARGET>`**, while §4:516 treats "passed with enumerated deferrals" as a separate owner-only outcome. Nothing says a record with a deferred F2 must carry the `READY-WITH-DEFERRALS` word. The v1.5 tightening of the regex (its new comment correctly excludes §5's own `Deferred count (owner-deferred …)` label) fixed the false-positive from the template but left the false-positive from the reviewer.

*Direction:* state in §4 that any deferral-carrying pass is `READY-WITH-DEFERRALS`, and make the F2 deferral marker a citation to an owner decision rather than a word match.

### RD33-05 — MAJOR — "every E question `Met`" is satisfiable by omission; nothing checks the question set is complete

§4:458: "every E question `Met` for the named launch target". LG-6 computes `e_rows` from the rows that are present (validator:222–228).

`[Observed]` **p2**: a READY record with the `| E5 | … |` row deleted outright validates clean — "rows parsed: 38", `GATE VERDICT: READY FOR Capability 1 …`, 0 errors. E5 ("Do acceptance criteria exist for a spec itself") simply is not asked, and the gate reads READY.

`[Inferred]` This is RD24-19's principle — absence must not read as success — applied to the 35-question denominator instead of two count fields. The instrument's §2 full-vs-delta rule ("The gate decision itself requires a full administration at the named commit — regressions do not announce themselves", §2:158–160) is prose-only, and the validator that §5 names has no roster to check against. Given that §8 now fixes populations for five questions specifically so `Met` cannot rest on a partial read, the question set itself being open is the same defect at the top level.

*Direction:* bind the roster (A1–A6, B1–B5, C1–C7, D1–D4, E1–E6 + five sub-rows, F1–F6) in the validator and error on any missing row; fixture it.

### RD33-06 — MINOR — nothing checks that the record's launch target or instrument version agree with what the digest binds

§5:531–533 requires `Instrument version:` and `Launch target: <LAUNCH_TARGET, verbatim from the parameter block>`. LG-1 captures the version (validator:117) and never compares it; the launch target is never parsed at all.

`[Observed]` **p5**: a record reading `Instrument version: v1.2` and `GATE VERDICT: READY FOR Capability 7 — anything the reviewer names`, while quoting the correct v1.5 instrument and §8 digests at `997d9bd`, validates clean. The entire launch-scope apparatus is target-relative; the target the record declares READY is unconstrained by §8.

### RD33-07 — MINOR — the semantic delta's account diverges from the bytes in two places

(a) D-6 (delta:86–88): "`DEFAULT_ROUTE_SET` (the enumerated default reading/task routes — §4's blocking condition 1, D2's 'front door', and D3/F4's 'default reading path' all now name it)". `[Observed]` Sweep of all **802** lines: `DEFAULT_ROUTE_SET` appears at L315 (D2), L327 (D3), L649 (§8), L793 (changelog). F4:415 reads "reachable from a default reading path without a banner" and §4:476 reads "is on the default reading or task route" — neither names it. The binding is still unambiguous from §8:649, so RD24-07 is closed; the delta's claim is not true of the bytes.

(b) D-7 (delta:103–104): "*Semantic change:* §6 returns to being project-invariant (§7's own rule)". `[Observed]` §6:598–609 still carries a project-specific pilot paragraph naming the 2026-08-09 administration, v1.3, and commit `067d8a0`. Only the *instruction* moved to §8. RD24-14's secondary limb — §7's "everything project-specific lives in the parameter block" against §6 — is not closed, and the delta asserts it is.

### RD33-08 — MINOR — three disposition/delta coverage claims are not matched by the bytes

(a) RD24-10's row claims a "validator fixture for the template-verbatim case". `[Observed]` None of the 22 fixtures is that case; the `GOOD` fixture is an 11-row reduced record without `Materials given`, `Operationalization notes`, `E3 reopen-list`, the deferred-wave findings line, `Unknowns…`, or the falsification notes. The repair works (r1 proves it), but the template↔parser coupling that broke in v1.4 is guarded by nothing: a future edit to §5's field names would break records again silently.

(b) RD24-03's row claims "the delta flags the choice for the owner at P-34". `[Observed]` P-34:20–21 presents the alignment as done; the only owner choice offered is F5 promotion (option (b)).

(c) Delta:17–18: "Validator changes each carry a mutation fixture". `[Observed]` True of the nine v1.5 changes; the docstring's stronger claim that *every* check has one is false (RD33-03).

### RD33-09 — MINOR — §5's "counts computed from the rows, never transcribed" now sits beside two required transcribed counts

§5:571–573 keeps the sentence; the tool prints it on every run ("— counts computed from the rows, never transcribed", validator:300) on a line whose Deferred and Reopened figures are parsed from prose (validator:258–268). The docstring's LG-5 text carries the reconciliation; §5 does not. `[Inferred]` Benign today, but it is the exact "a generator that quotes prose" seam the repo's own rules warn about, and a reader of §5 alone will believe both figures are computed.

### RD33-10 — MINOR — omitting the E1 rollup row silently disables LG-8

LG-8 is gated on `if "E1" in verdicts` (validator:201). `[Observed]` **p4**: deleting `| E1 | … |` while keeping all five sub-rows validates clean. §3:347–348 ("five answers, not one. E1 is Met only when all five are") is then unenforced, and LG-6 evaluates the sub-rows alone.

### RD33-11 — MINOR — P-34's ordering covers the status edit but not option (b)'s amendments

P-34:76–88 fixes the order for the `status:` edit only. Option (b) (P-34:45–50) has the owner approving with amendments and "the changelog takes a v1.6 entry" — edits that would move the bytes *after* step 2's digest unless applied before it. The mechanism does not say so, and (b) is the branch the F5-promotion option lives on.

### RD33-12 — MINOR — E4's routing authority answers per clause, not per statement, and is silent for cases with no row

§8:648 names the routing matrix; E4:369–376 has the reviewer classify six ordinary-language statements and compare "against the project's own routing as recorded in" it. `[Observed]` The matrix's per-clause tables cover RFC 0006–0011 only; RFC 0001–0005 are represented by an 11-row "Capability 1 authoring supplement" (matrix:131–163), and the matrix states plainly that "the RFC 0001–0005 full enumerations are staged at surface specification". `[Inferred]` Cases 1–3 and 5 map onto supplement or RFC-0006 rows; cases 4 (independent fresh-context review before adoption) and 6 (shape-change propagation) are craft/governance obligations whose routing may have no row at all. The instrument gives no rule for "the routing authority is silent" — and silence is not the same as either side of a two-valued classification.

---

## What passes

`[Observed]` These are not inferences — I executed them:

- **The three BLOCKING repairs are real.** RD24-01's reorder is coherent end to end; RD24-09's conjunct is a vocabulary predicate the validator actually enforces, with "diverging" reduced to a single explanatory line; RD24-05's rendering choice is now specified rather than left to the reviewer.
- **A §5-template-shaped record validates.** r1 — 39 rows, every template field, real digests, real commit — passes with LG-1 and LG-2 executing against `997d9bd`. RD24-10's core complaint ("a record written to §5's own template is rejected by the validator §5 names") is closed by demonstration.
- **The self-test is a real check, not a tautology.** 22 fixtures, each naming the substring it expects; the nine new ones map one-to-one onto the repaired defect classes; `--selftest` exits 0 and the count matches the delta.
- **VIS-2 was applied to the gate's own record where RD-24 asked.** Missing `Deferred count:`/`Reopened count:` are errors, mutation-confirmed. Bare `Unknown` without a reason is rejected (p3).
- **Every path and quote in §8 that I checked resolves.** All 13 parameter-block paths exist at the frozen commit; the `LAUNCH_TARGET` and `FIRST_SPEC_CANDIDATE` quotes are faithful to their sources; `CG-2a` exists and names the retired-phrase population; six wave manifests back `CHUNK_UNIT`.
- **The result home exists and disclaims correctly.** README states records are "evidence, never an owner act", the trend log is empty with "zero rows is the correct current state, not a gap" — the right rendering of absence.
- **No version drift on the default path.** Cross-repo sweep (29 hits, 15 files): every current-facing reference reads v1.5; the two v1.3 references are historically correct (the pilot) and `LAUNCH-CLOSURE-PREFLIGHT.md:35` carries an explicit "Historical snapshot — non-authoritative" banner.
- **No question was weakened.** IDs A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1 are all present, none renumbered, and every change I traced adds a population, a pointer, or a requirement. The delta's "What did not change" section is accurate on this point.

---

## Overall assessment — may v1.5 be offered to the owner at P-34?

The repair session did the work it claimed. Of RD-24's 21 findings, none is absent from the bytes, 19 are closed outright, and the three BLOCKING ones are closed in a way I confirmed by running the mechanism rather than by reading its description — the F1 conjunct now blocks, the scoped row now has one specified rendering, and P-34 now binds the digest of the bytes that will be in force. That is a materially better instrument than v1.4, and the disposition register's account is honest about what it did.

But the repairs introduced a defect class of their own, and the pattern is consistent: **v1.5 makes several checks live for the first time, and three of them are defeated by the instrument's own text or by absence.** The scoped verdict form — the fix for a BLOCKING finding — has no check binding it to the disclosure §4 requires (RD33-01) and is invisible in every column of the trend log that F1, a §4 conjunct, is answered from (RD33-02). The literal `GATE VERDICT:` token — the fix for a MAJOR finding — woke LG-7, which §5's own "(owner only)" label then satisfies without an owner (RD33-03), while a deferral routed through the `READY FOR` word bypasses LG-7 altogether (RD33-04). And the conjunct the whole gate turns on, "every E question `Met`", is still satisfiable by deleting a row (RD33-05). Each is the same failure RD24-19 named — absence reading as success — one level up from where it was repaired. Two of them (RD33-01, RD33-02) are properties of the instrument's text, not just the tool, so they cannot be fixed after approval without another owner act.

So: **v1.5 is not yet what should be put in force.** I would not call it BLOCKING in the sense of "the packet is unsafe to show the owner" — P-34 is coherent, its digest mechanism is right, its options are priced honestly, and nothing in v1.5 misleads the owner about what they would be binding. But five MAJOR findings stand, two of them requiring instrument amendments rather than validator patches, and offering these exact bytes would ask the owner to make owner-approved a vocabulary whose findings the trend log cannot represent. The cheap path is one more repair batch — a Scoped trend column, a scoped-row disclosure check, an owner-citation requirement on any deferral, a question roster in the validator, each with a fixture — then a short re-review of the delta, then the offer. The formal administration must not run on this validator as it stands.

VERDICT: REVISE
