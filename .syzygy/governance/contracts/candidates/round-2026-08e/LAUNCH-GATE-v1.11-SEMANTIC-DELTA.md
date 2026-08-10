# Launch-gate v1.10 → v1.11 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.11 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-39**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.10 as re-reviewed by RD-38 (subject sha256
`3cb0814eebe734cc6f9279df35fddc967a5b05b131ea8d3b653a8b0d4f19f48f` at
commit `34cbe5e`; raw review `reviews/RD-38-instrument-v110-RAW.md`,
`VERDICT: REVISE`, 1 BLOCKING / 2 MAJOR / 4 MINOR — and all six RD-37
repairs verified against the bytes, RD37-01 "genuinely and completely
closed" with the regression measurably reversed, §1–§8 byte-identical
per-section for the fourth amendment running). Every delta below closes an
RD-38 finding; dispositions in `reviews/DISPOSITION-REGISTER.md`. **This
is a validator-and-records batch a fourth time: no question block, no
verdict word, and no section §1–§8 of the instrument changed** (verified
per-section against `git show 34cbe5e:launch-gate-pre-specifications.md`;
§8 parameter block `6610` bytes, digest unchanged across all seven
instrument versions — recompute with the validator's own
`param_block_bytes`). The instrument bytes that move: the
`effective_version:` header, the appended §9 v1.11 entry, and one dated
correction marker in the §9 v1.10 entry (D-3 below). Validator changes
carry fixtures (`scripts/launch_gate_results.py --selftest`, **116
fixtures**); **eight** repairs re-proven by mutation, each failing exactly
the fixtures it added.

RD-38's refinement of RD-37's diagnosis, adopted as this batch's
discipline: *"the discipline is uniformity of application **to every rule
the code carries, not to every rule the batch touched**."* RD-38
enumerated 16 predicates/parsing rules, 10 satisfying uniformity, 6 not —
the six are exactly what this batch repairs: the record-versus-quotation
distinction reaches every presence and duplicate check (D-2), RD36-02's
line anchoring reaches the three fields RD37-06 brought under `_decl`
without it (D-4), and the closed verdict vocabulary and duplicate-row
rules reach the `--prior` side (D-6). Like its four predecessors, this
record predicts nothing about whether the batch is the last.

## D-1 — corrections of the frozen v1.10 delta (the frozen record is not edited)

Three sentences of the v1.10 delta are false; per the D-10 convention the
frozen record is not edited, and this entry is the correction of record.

1. **D-2's first bullet** grounds the LG-13 marker vocabulary in "the
   closed marker vocabulary §5's own template slot names." **False** —
   §5's slot is `<empty | enumerated items>`; it names no vocabulary
   (RD38-02's measurement: §5 "publishes no vocabulary"). The vocabulary
   is validator policy. The same false grounding appeared in the §9 v1.10
   entry, which carries a dated correction marker in place (D-3 below).
2. **"What did not change"** claims *"A lawful record under a correct
   v1.9 reading remains lawful under v1.10."* **False of three measured
   records** (RD-38 §RD38-03): the empty-digest-field record and the
   narrative-version-mention record both validate clean at v1.9 and are
   rejected at v1.10, and a record quoting §5's three field slots in a
   fenced appendix scores 0 at v1.9 and 4 errors at v1.10. The
   over-rejection direction was the safe one, but the claim was wrong.
3. **D-3's meta-fixture sentence** claims the source scan "fails any
   future field reverting to a first-match read." **False** — RD-38
   defeated it with three trivial refactors, one a literal `re.search`
   on a literal label with a long comment pushing the pattern outside
   the fixed scan window (RD38-04). The scan asserted a syntactic
   pattern, not the behavior. Replaced at v1.11 by D-5's behavioral
   loop.

## D-2 — a quotation is not the record: fenced blocks are stripped before any check reads the text (RD38-01, BLOCKING)

RD-38's composite: a record that deletes its G1 section and six of the
eight declared §5 fields — the non-authority banner, `Reviewer:`,
`Reviewer model family:`, `Materials given:`, `Operationalization
notes:`, `Reviewer's falsification notes:` — validated **clean** under
`READY FOR <the verbatim launch target>` if it quoted §5's own template
in a fenced appendix; the identical record without the appendix produced
7 errors. Seven checks turned into no-ops by one appendix. At v1.11:

- `_active_text()` strips fenced blocks (``` and ~~~) from the text
  **every** check reads — LG-4's G1 anchor, LG-12's presence tokens, the
  row parser, `_decl`, the gate-verdict scan — on the record and the
  `--prior` side alike. One strip at the source, uniformly, rather than
  per-check exemptions (the uniformity lesson applied prospectively).
- Both polarities fixtured: a G1 section present only inside a fence
  rejects (LG-4); a `Reviewer model family:` line present only inside a
  fence rejects (LG-12); a lawful record WITH a fenced template appendix
  still validates — a quotation shadows nothing; a fenced example table
  with a duplicate `A1` row fires no duplicate check.
- RD-38's composite re-executed at v1.11, git on, real digests: **7
  errors with the appendix, 7 without, identical error sets** — the
  appendix is no longer the difference.
- Mutation-proven: making `_active_text` the identity fails exactly the
  four RD38-01 fixtures.

## D-3 — the LG-13 marker vocabulary: attribution corrected, vocabulary widened, and published where the reviewer meets it (RD38-02, MAJOR)

Two defects, one root: the v1.10 batch attributed its marker vocabulary
to §5, which publishes none, and the three-marker list rejected **eleven
honest emptiness wordings** (`n/a`, `nil`, `nothing`, `0`,
`(none known)`, `-- none --`, and decorated `empty` forms) with a
message asserting the record "enumerates" a value that enumerates
nothing. At v1.11:

- The §9 v1.10 entry's false grounding carries a **dated correction
  marker in place** (the RD36-01 precedent — §9 is changelog, not
  §1–§8); the v1.11 entry states the truth: the vocabulary is validator
  policy, published in LG-13's own error message.
- The vocabulary widens to ten honest emptiness markers — `empty`,
  `none`, `none identified`, `none known`, `n/a`, `na`, `nil`,
  `nothing`, `zero`, `0` — matched full-line after stripping
  decoration (bold, backticks, brackets, trailing punctuation), so
  `**None.**` and `(empty)` are the marker and `none identified (see
  G1)` is not.
- Both LG-13 messages now say what the field *carries* and append the
  lawful markers, so a rejected reviewer learns the vocabulary from the
  rejection itself. `unknown` and `TBD` still reject — an unknown
  reopen-list is not an empty one (VIS-2: no evidence is never green).
- Re-executed: the eleven wordings score 0 errors; RD-37's four attack
  enumerations still score 2 LG-13 errors each.
- No instrument sentence outside §9 changes; §5's slot remains
  `<empty | enumerated items>`.

## D-4 — the three §2 anchors carry the line-anchoring rule the other fields already had (RD38-03, MAJOR)

RD37-06 brought `Instrument version:`, its `sha256:`, and
`Parameter block sha256:` under `_decl` without bringing them under
RD36-02's anchoring rule — so an empty `Parameter block sha256:` field
silently borrowed the digest from the next line, and a mid-line
narrative mention (*"I checked whether Instrument version: v1.9 would be
accepted"*, in the falsification-notes field §5 itself invites) became
the value LG-11 reported on, producing an error about a claim the record
does not make. Both records validated clean at v1.9 and were the
measured counterexamples to the v1.10 delta's both-directions claim
(D-1.2). At v1.11 the three patterns are `^`-anchored with `[^\S\n]*`
like every other declared field: the empty digest field is **absent**
(loud LG-1 error, never borrowed), and the narrative mention is inert.
Fixtures both directions; mutation-proven per anchor (un-anchoring the
version pattern fails the narrative fixture; restoring `\s*` on the
param pattern fails the borrowed-digest fixture).

## D-5 — the meta-fixture becomes behavioral: every declared label, a disagreeing decoy, both orders (RD38-04, MINOR)

The v1.10 source-scan meta-fixture asserted a syntactic pattern and was
defeated by refactors (D-1.3). At v1.11 it is replaced by what RD-37
actually prescribed, asserted behaviorally: a generated loop drives a
disagreeing decoy through **every** declared label — the seven §5 fields
and the three §2 anchors — in both orders, decoy above and decoy below,
expecting the disagreement error each time. Twenty fixtures from one
loop; a new declared field means a new row in the loop. Mutation-proven
with RD-38's own evasion shape: a copy reverting the E3 field to a
first-match `re.search` behind a long comment (the exact refactor that
defeated the source scan) fails the loop's two E3 fixtures — caught by
the behavior it changes, not by any pattern in the source.

## D-6 — the prior obeys the vocabulary and duplicate rules a current record obeys (RD38-06, MINOR)

RD37-04's repair validated the `--prior` for roster coverage and alien
rows only, so a fabricated prior carrying out-of-vocabulary verdicts
(`Partially met`) or duplicate rows could still drive the New-findings
column F1 is answered from. At v1.11 the prior's rows are checked
against the same closed `VERDICT_RE` vocabulary and the same
duplicate-row rule; failure refuses the prior loudly and the trend
column reads `n/a — prior record failed validation`. Two bespoke
fixtures (roster-complete + bad vocabulary; roster-complete + duplicate
row), each mutation-proven separately.

**Disclosed residual, stated rather than silent:** a bare
roster-complete row block with lawful verdicts is still a lawful prior.
This is not closable by version cross-checks: a prior administration
*lawfully* names an older instrument version and older digests, so the
prior side cannot demand the current instrument's integrity anchors.
The residual is disclosed here and in the §9 v1.11 entry.

## D-7 — `_decl` returns the normalization the disagreement compares on (RD38-07, MINOR)

Occurrences were compared whitespace-normalized but the raw last value
was returned, so two "agreeing" occurrences could yield a whitespace
variant a downstream exact comparison then rejects. At v1.11 `_decl`
returns `_norm_ws(vals[-1])`. The behavioral witness fixture: the
none-marker test on `Owner deferral decision:` compares the returned
value exactly, so `Owner deferral decision: none ` (trailing space) must
be the none marker, not a citation the validator rejects — proven by
mutation (raw return fails exactly that fixture).

## D-8 — the register correction (RD38-05, MINOR)

The disposition register's RD37-04 row overclaimed that the prior-side
repair enforced "closed verdict vocabulary" — it did not until D-6. The
row carries a dated correction in the register (the register is a living
record; dated corrections in place are its convention, unlike frozen
deltas and reviews). No validator or instrument change.

## What did not change

- **No section §1–§8 of the instrument changed** — verify per-section
  against `git show 34cbe5e:launch-gate-pre-specifications.md`. The §8
  parameter block hashes identically across all seven instrument
  versions (recompute with the validator's own `param_block_bytes`,
  never from this record). The instrument bytes that move: the
  `effective_version:` header, the appended §9 v1.11 entry, and the
  dated RD38-02 correction marker in the §9 v1.10 entry (D-3).
- **No frozen record is edited.** The v1.4–v1.10 deltas and the RD-33 …
  RD-38 raw reviews are byte-identical to their pre-batch state; the
  v1.10 delta's three false sentences are corrected by this delta's
  D-1, in the D-10 convention.
- **No question weakened, no ID renumbered, no verdict word changed.**
- Directionality, stated with its exceptions: D-2, D-4's empty-field
  limb, and D-6 only reject records or refuse inputs v1.10 trusted.
  D-3, D-4's narrative limb, and D-7 newly **accept** records v1.10
  wrongly rejected — the eleven honest emptiness wordings, the
  narrative version mention, the trailing-space none marker — each a
  record the instrument's own text never condemned; every acceptance is
  fixtured, and the borrowed-digest and enumeration directions those
  checks exist for are re-proven rejected in the same run. RD-38's
  carried-forward §0 nit (RD-37's frozen raw review records §8 length
  6577 vs measured 6610 — a transcription slip in a frozen record) is
  noted and, per rule 10, not edited.

## Fixture arithmetic

86 → **116**: −1 (the source-scan meta-fixture removed, D-5), +20 (the
behavioral decoy loop — ten labels × both orders), +4 RD38-01 (two
fence-rejections, two quotation-shadows-nothing accepts), +2 RD38-03
(borrowed digest absent; narrative mention inert), +2 RD38-02/07 marker
vocabulary (`n/a` accepted; decorated `**None.**` accepted), +1 RD38-07
behavioral witness (trailing-space none marker), +2 RD38-06 bespoke
priors (bad vocabulary refused; duplicate row refused). Count read from
the selftest's own printed output (`116 fixtures, 0 failing`). All
LG-1…LG-13 checks still fire; the eight mutation-reverts each fail
exactly the fixtures their repair added.
