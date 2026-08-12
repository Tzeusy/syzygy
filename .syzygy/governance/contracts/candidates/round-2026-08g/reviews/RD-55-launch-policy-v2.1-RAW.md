# RD-55 — raw reviewer output, launch-policy semantics at v2.1

> **Provenance banner. Everything below the rule is the reviewer's raw
> output, copied verbatim and unedited** — including any error it contains.
> Corrections live in the disposition register, never here.
>
> | | |
> |---|---|
> | Role | Launch-policy semantics reviewer (charter §7.7, review 1 of 2) |
> | Dispatched | 2026-08-13 |
> | Subject commit | `939363f` |
> | Subject digest | `launch-gate-pre-specifications.md` sha256 `3afdffdab0d71d32a4e901f43db1c11ba096f699e240050e8cc6cbb95ada12c8` |
> | Context | Fresh — no prior contact with this repository's review history |
> | Model family | **Same as the corpus's authors.** This review therefore supports repair and is **never** the formal launch administration (instrument §2, F5) |
> | Verdict | `REVISE` — copied exactly |
>
> The reviewer verified `git status --porcelain` unchanged and the subject
> digest identical at the start and end of its session; this session verified
> the same independently afterwards.

---

# RD-55 — Launch-policy v2.1 semantic review (round-2026-08g, subject `939363f`)

Subject bytes verified unchanged at start and end of this review: `launch-gate-pre-specifications.md` sha256 `3afdffdab0d71d32a4e901f43db1c11ba096f699e240050e8cc6cbb95ada12c8`. Nothing in the repository was edited; all probe records were written to a scratchpad and the differential worktree was removed. `git status --porcelain` reports only the pre-existing untracked prompt file.

---

## A. Byte-identity — the delta's table reproduces exactly

**Method.** I ran the delta's published script verbatim (its §"What did not change" code block, lines 46–56), against `git show efa6d63:launch-gate-pre-specifications.md` and the working-tree file. I did this before reading the delta's table values. Denominator: all 9 spans, which exhaust both files — `re.split` on `^## \d+\.` yields 9 headings in each text, and the spans are contiguous from the first heading to EOF.

| Span | delta publishes | I computed | agree |
|---|---|---|---|
| §1 | `1f2d1d60a28ada2a` identical | `1f2d1d60a28ada2a` identical | yes |
| §2 | `0d7340f2ee9a8b8c` identical | `0d7340f2ee9a8b8c` identical | yes |
| §3 | `fe0b051e136d2fee` identical | `fe0b051e136d2fee` identical | yes |
| §4 | `f4a2a6423a89703f -> 84d5d3d456e7c05a` | same | yes |
| §5 | `c6847ffa7812853b -> 0b63585544520df4` | same | yes |
| §6 | `9906fcac454062cd` identical | `9906fcac454062cd` identical | yes |
| §7 | `d24deb9c8eb39995 -> 9e17cb8de0458976` | same | yes |
| §8 | `01209c0f052971f7` identical | `01209c0f052971f7` identical | yes |
| §9 | `e49dde205d069a96 -> 9301d992b12b889a` | same | yes |

9 of 9 rows reproduce. The two whole-file digests reproduce too (`05ecaa95…` / `3afdffda…`). The delta's stated §9 caveat did not fire — §9 matched.

**Second method.** `git diff -U0 efa6d63` produces **14 hunks**; mapping each hunk's old-file line number against v2.0's section boundaries (§1@80, §2@98, §3@188, §4@478, §5@582, §6@703, §7@761, §8@785, §9@889) gives: preamble 1, §4 9, §5 1, §7 1, §9 2 — **zero hunks in §1, §2, §3, §6, §8**. Denominator: all 14 hunks of the complete diff.

`[Observed]` **RD-48 f7 is repaired.** The v2.0 delta's defect was a table of unreproducible byte counts with no digests; v2.1 publishes digests plus the script, and the script reproduces the table.

`[Observed]` **The §8 span digest `01209c0f052971f7…` equals the parameter-block digest the sealed packet binds** (`FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md`, `01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6`), so that cross-claim holds. All five packet digests match the working tree; `launch-gate-administration.schema.json` is byte-identical to `efa6d63` (`e0167fb8…` both).

**But the table's denominator is not the file.** The split discards `p[0]` — the preamble — which the published script never digests. See f3.

---

## B. Weakening — populations swept, with counts

Method: Python `re` over the v2.0 and v2.1 texts restricted to §1–§8 (the normative body; §9 is history), plus cross-checks against `ROSTER` in the validator and the schema's enums.

| Population | v2.0 | v2.1 | Δ | direction |
|---|---|---|---|---|
| §3 question bullets `^- \*\*(ID) \[tier\]\*\*` | 35 (A1–A6,B1–B5,C1–C7,D1–D4,E1–E6,F1–F6,G1) | 35, same IDs, same order | 0 | — |
| Tier split | [U] 33 / [G] 2 | [U] 33 / [G] 2 | 0 | — |
| Roster rows (`len(ROSTER)`) | 39 | 39 | 0 | — |
| Row verdict enum (schema `$defs/question_result/properties/verdict`) | `Met`, `Not met`, `Not met (out of launch scope)`, `Unknown` = 4 | identical 4 | 0 | — |
| Forbidden forms named | `Partially met`, `Met with caveats` = 2 | identical 2 | 0 | — |
| Trend columns (`\| Date \| Commit \| …` header) | 9 | 9, byte-identical | 0 | — |
| §4 `READY FOR` formula terms | 6 (1 lead + 5 `AND`) | **7** (1 lead + 6 `AND`) | **+1** | **strengthening** |
| Gate verdict words defined in §1–§8 | 2 (`NOT READY` = 0 occurrences) | **3** (`NOT READY` = 2) | **+1** | **strengthening** |

Confirming second method for the top rows: §3, §6 and the schema are byte-identical by digest (criterion A), so no question, no trend column and no row-verdict word can have moved.

`[Observed]` **Nothing was dropped, renamed, weakened, or made unreachable.** Two populations grew, both in the blocking direction. The one added conjunct — *E3's reopen list is empty* — makes strictly fewer records pass, and it was already computed at v2.0.

---

## C. New pass routes — none found, by two methods

**Method 1 — differential execution.** I created a git worktree at `efa6d63` and ran both validators over a 25-record battery built from the v2.1 `_base_record(git_bound=True)` with `formal/full/fresh` set, covering every surface the delta says moved: eleven deferral-citation shapes (`SDR-9`, `SDR-999`, the pending queue, `.beads/issues.jsonl`, root `README.md`, the decisions-home `README.md`, a bare filename, a directory, prose, `P-34`, a `./`-prefixed path), plus `e4.routing_authority`, evidence paths, wave declaration, `administration_kind`, `formal`, `fresh_context`, E3 reopen items, G1 placeholder, forged instrument/parameter-block digests, a nonsense launch target, gate-word forgery in free text, and an undisclosed scoped row. Repeated the six most leak-prone under a fake `git` returning 127.

Result over 25 cases: **0 cases fail v2.0 and pass v2.1.** Five are stricter under v2.1 (`cite_pendqueue`, `cite_beads`, `cite_dec_README`, `cite_dotslash`, `e4_routing_bogus`); the rest are unchanged. One case (`evidence_fake_path`) was malformed — it failed `LA-1` for a missing `locator` in both trees, so it is **inconclusive for its intended predicate** and I do not count it as evidence about the evidence-existence check; it does not affect the conclusion, since it failed both.

**Method 2 — code identity of the deciding logic.** The formula is not merely equivalent, it is the same bytes:

```
v2.0 conjunct block == v2.1: True
v2.0 branch logic   == v2.1: True
```

(extracted by `re` from `conjuncts = [ … ]` and from `if core and … branch = "blocked"` in both revisions of `scripts/validate_launch_administration.py`).

`[Observed]` **I could not construct a record that fails under v2.0 and passes under v2.1**, and the deciding code is byte-identical. `[Inferred]` No new pass route exists; the battery is 25 targeted cases, not a proof.

---

## D. RD-48's eleven findings, one row each

Finding text is RD-48's own, abridged only where marked with `…`.

| # | RD-48's words | v2.1 |
|---|---|---|
| f1 | *"§4's normative clauses name record fields and validator checks that do not exist for a v2.0 record"* | **partly repaired.** 4 of 5 named items fixed: `Owner deferral decision:` → `owner_deferrals[].decision_citation`; `Deferred count:` → `len(owner_deferrals)`; *"§5's family line"* → `reviewer.model_family`; `LG-9` → `LA-9`. **`LG-6/LG-7` is not fixed** — see f1 below |
| f2 | *"the computed formula has a sixth core conjunct that §4 does not contain"* | **repaired.** §4 line 531 now carries `AND E3's reopen list is empty`, with a labelled note. Formula terms 6 → 7 |
| f3 | *"the gate verdict word `NOT READY` no longer exists in §1–§8"* | **repaired.** §4 lines 489–493 define all three in a table; `NOT READY` occurs 2× in §1–§8 (was 0) |
| f4 | *"§7's new clause 'it names no Syzygy artifact' is false"* | **repaired.** §7 lines 833–847 withdraw the claim, name the `$id`, the two file names, VIS-2/VIS-4 and the `SDR-n`/`P-n` conventions, and add the two tools to the portable core |
| f5 | *"§5 delegates the normative check enumeration to a script docstring and disclaims responsibility for its currency, and that docstring is already wrong"* | **repaired in both halves.** §5 lines 735–751 take back the enumeration; the `LA-13` docstring is corrected. **But the retaken enumeration is already incomplete** — see f2 below |
| f6 | *"the §9 changelog quotes a stale fixture count"* | **repaired.** Line 2141 now reads *"each with at least one mutation fixture; the count is printed by `--selftest` and stated nowhere else"* |
| f7 | *"the 'measured, not asserted' table is not reproducible by its stated method"* | **repaired.** Reproduced exactly — criterion A |
| f8 | *"two obligations deleted from §2 are unrecorded"* | **recorded, not restored.** Delta D-8 states both, names their successors, and marks the not-restoring judgement `[Inferred]` and this session's. The successor argument is only partly established — see f5 below |
| f9 | *"the new-check table is incomplete and misstates its baseline"* | **recorded.** Delta D-9 adds `LA-14`, scopes `LA-16`, and **withdraws** the `LA-13` "previously trusted" claim as false |
| f10 | *"three limits are undisclosed and one names the wrong field"* | **partly repaired, partly recorded.** (a) git-unavailable → limit 3; (c) placeholder lexicon → limit 8; the retarget to `deferred_wave_findings[].blocking_conditions_met` → limit 7. **(b) the unconditional trend row is claimed repaired and is not** — see f1 below |
| f11 | *"'stored verbatim' is dropped from the record artifact class without record"* | **recorded, not restored.** Delta D-8 row 3 |

**Claimed-but-not-delivered:** the delta's D-4 table row and the packet both assert repairs that the bytes do not carry (f1, f4 below). No finding is silently omitted.

---

## E. Does §4's rule reach "every place a gate result appears"?

§4 line 511: *"This reaches every place a gate result is stated, and §6's trend log is one of them."* I enumerated the places a gate result can appear and tested each.

| Place | Reached? | Evidence |
|---|---|---|
| Instrument §4 (definition) | yes | lines 489–517 |
| Instrument §6 trend-log rules | yes, by reference — §6 bytes unmoved | §4 line 515 states why |
| Validator CLI `Formal gate result:` line | **yes, all four conditions** | line 1831 `if computed["eligible"] and not errors:` |
| Validator `--trend-row` output | **NO** | `trend_row()` line 1146 branches on `computed["eligible"]` alone; `--trend-row` at line 1844 runs regardless of `errors` |
| Generated report `GATE VERDICT:` line | **NO** | renderer line 360 branches on `computed.get("eligible")` alone; `--allow-invalid` reaches it |
| Report's embedded §6 trend row | **NO** | same `trend_row()` |
| `.syzygy/governance/decisions/launch-gate/TREND-LOG.md` | n/a — zero rows today | header verified |
| `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` §10 | **NO** | *"one trend row printed by `--trend-row`, appended to TREND-LOG.md"* — the packet never states the three-outcome separation, never uses the words eligibility / row outcome / formal gate result, and gives no instruction about an invalid record |
| `PROJECT-STATUS.md` line 33 | **NO** | *"the 2026-08-09 **pilot** (v1.3), which returned `GATE VERDICT: NOT READY`"* — single-verdict form. Defensible (a v1.3 Markdown record), but the §4 claim is unqualified |
| `AGENTS.md` line 73 | **NO** | same pilot, same form |

Three of the ten are mechanism failures rather than scope questions, and one of them is exactly the failure class D-3 claims to have caught. See f1.

---

## Findings

### f1 — BLOCKING — §4's fourth eligibility condition is not implemented, and the §6 trend row leaks `READY FOR` for an invalid record

`launch-gate-pre-specifications.md` §4, line 505 (a defined clause in the eligibility table):

> **Administration eligibility** | Separately determined: a record is eligible to be cited as launch evidence only when it is `formal`, of kind `full`, declares fresh context, **and validates without error**

and line 509: *"**It may never produce a `READY FOR` gate result.**"*

`scripts/validate_launch_administration.py` lines 1069–1077 compute eligibility from **three** conditions:

```python
ineligible = []
if not rec["formal"]:                         ineligible.append("`formal: false`")
if rec["administration_kind"] != "full":      ineligible.append(...)
if not rec["reviewer"]["fresh_context"]:      ineligible.append(...)
eligible = not ineligible
```

`trend_row()` (line 1146) and the renderer (line 360) both branch on this three-condition `eligible`. Only the CLI's own printed line (line 1831) adds `and not errors`.

`[Observed]` **Constructed and executed.** Two records identical but for one field — `instrument.sha256` forged to `0000…`:

```
CLEAN, formal/full/fresh
  | 2026-08-11 | 939363f | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — Project registration and honest shape visibility |
  record valid

SAME RECORD, one forged instrument digest
  | 2026-08-11 | 939363f | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — Project registration and honest shape visibility |
  1 validation error(s):
    LA-2: instrument digest mismatch — the record quotes 000000000000…, the committed instrument is 3afdffdab0d7…
```

The two trend rows are byte-identical. A record bound to bytes that are not the instrument deposits `READY FOR Capability 1 …` into the log §6 line 791 calls the evidence F1 is *"answered from … and only from it."* The same gap reaches the report: `render_launch_administration.py --allow-invalid` on that record emits line 217 `GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility`, mitigated only by a banner ten lines from the top of a 217-line document. §5 line 732's clause *"A record that does not validate is not rendered at all"* is false of the tool as shipped.

This is the same failure shape D-3 says the rule caught. The delta's own D-3 states the repair as covering four conditions — *"Eligibility is computed from `formal`, `administration_kind`, `fresh_context` and the presence of validation errors"* — which is false of the code in the same sentence that describes it. RD-48 f10(b), which the delta lists as *"repaired instead"*, is therefore repaired only for the three-boolean case.

*Fix:* fold the error count into `_compute`'s eligibility (it already receives `errs`), or have `trend_row()` and the renderer take validity as an argument; and either drop `--allow-invalid`'s gate-verdict line or make it print the `NONE` form. Add a fixture in the failing direction: formal + full + fresh + one validation error must not produce a `READY FOR` trend row.

### f2 — MATERIAL — §5 takes back the check enumeration in the same pass that adds a check the enumeration does not name

§5 line 740, added at v2.1:

> **The enumeration below is this instrument's**; the tool implements it, and a check the tool runs that this list does not name is a finding against the tool.

The header is `(`LA-1` … `LA-16`, each with at least one mutation fixture)` and the list covers sixteen predicates. The same repair pass added **`LA-3b`** — the delta's own tool-changes table, RD-47 f7 row: *"`LA-3b` binds it to §8, as `LA-3` does for the launch target"* — which errors at `validate_launch_administration.py` lines 667 and 671 and carries fixture `"LA-3b the E4 routing authority is bound to §8"` at line 1325.

`[Observed]` Sweep of the whole instrument, denominator all 2182 lines: `LA-3b` occurs **0 times**. §5's enumeration names *"instrument, parameter-block and commit identity; the launch-target and wave binding"* and separately *"E4's fixed-case completeness and case-text fidelity"* — neither is the binding of `e4.routing_authority` to §8. §5's only mention of the field is line 689, `e4: routing_authority, fixed_case_results[]`, in the record-shape block, not the check list.

By §5's own new clause, `LA-3b` is a finding against the tool. It is more usefully read as a finding against the amendment: the pass that made §5 the owner of the enumeration shipped an enumeration already one short.

*Fix:* name `LA-3b` in §5's list (and decide whether the `LA-1 … LA-16` range notation should read `LA-1 … LA-16, with LA-3b`).

### f3 — MATERIAL — the delta asserts preamble byte-identity, which is false, and the published method cannot detect it

Delta D-8, line 215:

> **§2 and the preamble are byte-identical at v2.1, so nothing here is restored**

`[Observed]` The preamble is **not** byte-identical. Two independent methods:

1. sha256 of `re.split(r"(?m)^(## \d+\..*)$", text)[0]`: v2.0 `9d47c028832d2bf4…`, v2.1 `08b200cd4581d4b9…`, both 3678 bytes.
2. `git diff -U0` hunk mapping: 1 of 14 hunks falls in the preamble.

```diff
-effective_version: v2.0 (candidate; v1.3 was the pilot-administered version)
+effective_version: v2.1 (candidate; v1.3 was the pilot-administered version)
```

The change is a required version bump and nothing turns on it substantively. What turns on it is that this is the one document in the round whose stated purpose is that measurements be checkable, and its published script **structurally cannot check this claim**: the split discards `p[0]`, so the delta's own byte-identity table has a denominator of §1–§9 while its prose makes a claim about the preamble. The equal byte lengths mean a length-based check would also have missed it.

The instrument's own §9 entry is careful here — it claims byte-identity for *"§1, §2, §3, §6 and §8"* only, and is correct. The delta is the document that overreaches.

*Fix:* correct D-8 to *"§2 is byte-identical; the preamble changed in exactly one line, the version bump"*, and extend the published script to digest `p[0]` so the table's denominator is the file.

### f4 — MATERIAL — the `LG-6/LG-7` half of RD-48 f1 is not repaired, and three documents say it is

§4 line 620 — still the operative sentence, unchanged from v2.0 line 564:

> the validator runs the full conjunct battery on both branches (LG-6/LG-7): plain `READY FOR` requires F2 `Met` and zero declared deferrals

followed at line 623 by a note in the past tense:

> *(Check identifiers corrected at v2.1, RD-48 f1: this sentence cited `LG-6/LG-7` … The structured path's checks are `LA-*`.)*

`[Observed]` Sweep of §1–§8, denominator 890 lines: `LG-6` occurs 2×, `LG-7` 2× — line 620 (live clause) and line 624 (the note quoting it). Compare `LG-9`, where the literal *was* replaced (`LA-9` at line 567) and the note explains the replacement. The two halves of the same finding got opposite treatments, and the note's tense is wrong about its own subject.

The consequence is a live clause pointing a reader at `launch_gate_results.py` — which §5 line 763 says *"is not the correctness path for any v2.0 administration"* — as the checks enforcing §4's two pass branches. The correct identifier exists: `LA-12`, docstring *"the §4 formula, computed — both pass branches run the full conjunct battery."* The note declines to name it.

Three documents claim otherwise:
- delta D-4's table: `| `LG-6/LG-7` | the `LA-*` checks, with a note … |` under the column heading **"§4 now says"**. §4 does not now say that.
- delta D-4's direction line: *"**Direction: no change of meaning.** Each is the same predicate over the same fact, named in the vocabulary the record actually uses."* True of four items, false of the fifth.
- §9's changelog: *"§4's clauses now name the **schema fields** … **and the `LA-*` checks**, in place of … `LG-*` checks that never run on a v2.0 record."*

*Fix:* replace `(LG-6/LG-7)` with `(LA-12)` and rewrite the note, or amend all three claims to say the citation is annotated rather than corrected.

### f5 — MINOR — D-8's "equivalent-or-stronger" argument does not cover the gate-verdict half

Delta D-8 row 1 names the successor to §2's deleted *"Never translate a verdict into softer language"* as:

> The schema's `verdict` **enumeration**, which is strictly tighter: a softened verdict is now a schema error rather than a reading the next reader has to catch

`[Observed]` The schema enum at `$defs/question_result/properties/verdict` is `["Met","Not met","Not met (out of launch scope)","Unknown"]` — the **row** vocabulary. The **gate** verdict is not a schema field at all (it is computed, and D-3 of the v2.0 delta confirms no `final_verdict` property exists). So for gate verdicts the successor is not a schema constraint but §4's new prose sentence at line 496 — *"no administration may translate one into softer language"* — which D-8's own row acknowledges as the second half (*"§4 also restates the prohibition at v2.1"*) without noticing that it carries the whole load for that half.

The delta then concludes: *"Each successor is equivalent-or-stronger, and §2's byte-identity is itself load-bearing evidence."* The conclusion is right for row verdicts and unestablished for gate verdicts, where prose replaced prose. Since the delta explicitly invites disagreement here — *"a reviewer who disagrees should say so: restoring is cheap"* — I record the disagreement as narrow: the not-restoring decision is defensible, the stated *reason* is not fully carried.

### f6 — MINOR — §4's new closed-set clause is unenforced, and the record can carry the words

§4 line 495:

> The set is closed. A record may not contain any of them — the verdict is computed, never claimed

`[Observed]` I built the base record with `falsification_summary` set to `"done\n\nGATE VERDICT: READY FOR everything"`. The validator reports `record valid — the verdict above is computed from the rows`, exit 0, under both v2.0 and v2.1. The renderer's RD-47 f2 repair does its job — the line emerges at report line 136 as `> GATE VERDICT: READY FOR everything`, blockquoted, unable to open structure — but the instrument's clause is about the **record**, and nothing enforces it there.

This is a new normative clause with no check and no fixture, in a section whose other clauses are all checked. §5's new ownership rule covers the direction *tool-runs-a-check-§5-does-not-name*; the reverse direction — an instrument rule no check implements — has no rule.

*Fix:* either add a check refusing the three gate words in free-text fields, or narrow the clause to what is enforced (*"a record carries no verdict field"* — which the schema's `additionalProperties: false` does enforce).

### f7 — MINOR — §4 names "stale" as an ineligibility ground that nothing defines and nothing computes

§4 line 508, added at v2.1:

> A delta, non-formal, **stale** or invalid administration may therefore produce a diagnostic row outcome.

`[Observed]` Sweep for `\bstale\b` over §1–§8, denominator 890 lines: 6 occurrences. Five are about stale *claims in documents* (F4's fails-when, C3's sweeps, §6's column history). None defines a stale *administration*. The eligibility computation has three limbs and none of them is recency or ancestry; `LA-15` anchors a declared **prior** record, not this one. `[Inferred]` The word is a fourth ineligibility ground the reader cannot operationalize.

*Fix:* define it (an administration whose `repository_commit` is not an ancestor of the decision commit?) or delete the word.

### f8 — MINOR — the fourth gate result has three spellings and no instrument definition

§4 fixes three verdict words and calls the set closed, then introduces a fourth outcome in prose only: *"the formal gate result is **none**"* (line 506). Three tool surfaces spell it three ways:

| Surface | Literal |
|---|---|
| `_compute`'s `gate_result` value | `NO FORMAL GATE RESULT` |
| generated report, line 217 | `GATE VERDICT: NONE — this administration is not eligible to be cited as launch evidence (…)` |
| §6 trend column | `NONE — not eligible; row outcome was NOT READY` |

The common prefix `NONE` is at least stable across the two that surface in artifacts, and the committed dry-run report and its trend row both carry it — the delta's "visible immediately" claim is `[Observed]` true and `--check` confirms the report regenerates. But §6's Gate-verdict column is F1's only evidence and its vocabulary is now four-valued with the fourth value defined nowhere in §1–§8.

### f9 — MINOR — the packet routes an administrator to a disposition register that contains no RD-47/RD-48 rows

`FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` §9:

> The raw files are `…/round-2026-08f/reviews/RD-47-…` and `…/RD-48-…`, with the repair account in `round-2026-08g/reviews/DISPOSITION-REGISTER.md`.

`[Observed]` `round-2026-08g/reviews/DISPOSITION-REGISTER.md`, denominator all 71 lines: `RD-47` 0 hits, `RD-48` 0 hits, `RD-54` 2 hits. The file dispositions RD-54 only, under a banner stating *"**nothing is dismissed by omission**: if a review raised twelve findings, twelve rows appear below."* The v2.1 repair account is in `round-2026-08g/LAUNCH-GATE-v2.1-SEMANTIC-DELTA.md`; the round-08f register still carries the RD-47/RD-48 rows as **open**, which was true at that commit and is now stale for the repaired ones.

*Fix:* point §9 at the v2.1 delta, or add the RD-47/RD-48 disposition rows to the 08g register.

### f10 — MINOR — D-7's "stated nowhere else" is a claim of absence the same file contradicts

Delta D-7: *"**Is:** the sentence names no count. The count is printed by `--selftest` and stated nowhere else."*

`[Observed]` The §9 repair is real — line 2141 names no count, and `--selftest` prints `88 fixtures, 0 failing` / `16 fixtures, 0 failing`, matching the delta's Fixtures block. But the delta's own Fixtures section, 100 lines later, states `88`, `16`, `75` and `12`. Sweep over 393 tracked `.md`/`.py`/`.yml` files for `\b(7\d|8\d|9\d)\s+(mutation\s+)?fixtures?\b` also surfaces `round-2026-08g/FINAL-OWNER-AND-SPEC-CLOSURE-PREFLIGHT.md:67` at the now-stale `75`. That file is explicitly a commit-anchored snapshot (*"the verified starting state of round-2026-08g at the commit named below"*, HEAD `f7ba735`), so I do **not** call it a defect — but "stated nowhere else" is unqualified and false as written. The delta's Fixtures block itself half-retracts it (*"it is not this file's to keep current"*).

*Fix:* scope the claim — *"stated in no artifact that must stay current."*

---

## What I could not test, and why

- **Whether the questions are the right questions.** Out of scope; §3 is byte-identical.
- **Truth of any evidence quote.** Content-blindness is by design and is disclosed as limit 1.
- **The instrument under a real administration.** None has been performed under v2.0 or v2.1 (delta limit 5, confirmed by a zero-row TREND-LOG.md). Everything in criterion C is synthetic.
- **Completeness of the "no new pass route" claim.** 25 constructed cases plus code identity of the deciding logic is not an exhaustive proof over the record space.
- **RD-47's twelve findings.** Out of my role; I read the delta's tool-changes table only to test claims it makes about §4's meaning.
- **The `--selftest` counts as clean-clone evidence.** Run in the working tree, not a fresh clone; `check_governance.py` reports `31 OK, 18 WARN, 0 FAIL (49 checks)` locally.

---

## Judgement

The amendment does what it was commissioned to do on the question the charter asked: `[Observed]` **nothing was weakened.** The formula gained a conjunct, the verdict vocabulary gained its missing word, five populations are unchanged by digest, and no record I could build fails v2.0 and passes v2.1. RD-48 f7 — the exact reproducibility defect that made the v2.0 delta's table decorative — is fully repaired, and I reproduced all nine rows before reading them.

It does not clear on internal consistency. **f1 is blocking**: §4's new eligibility clause states four conditions, the tool implements three, and the gap is demonstrable — a record whose sole defect is a forged instrument digest writes `READY FOR Capability 1 …` into the log that §6 calls F1's only evidence. That is the precise failure D-3 claims the "every place" rule caught, surviving one condition to the left of where the repair stopped. **f2 and f4** are the same species: §5 claims an enumeration it does not complete, §4 claims a correction it did not make, and three documents restate the second claim. **f3** falsifies a byte-identity assertion in the one file whose purpose is that assertions be checkable, using a script that structurally cannot see the span it asserts about.

None of these reopens a pass route. All of them are claims the amendment makes about itself that its own bytes do not carry — which is the defect class this round exists to close.

f1: BLOCKING. f2, f3, f4: MATERIAL. f5–f10: MINOR.

VERDICT: REVISE
