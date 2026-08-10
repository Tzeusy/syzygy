# Launch-gate v1.8 → v1.9 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.9 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-37**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.8 as re-reviewed by RD-36 (subject sha256
`49b0b5e5ad70d1eb6c1c0b78976ff4bf1d786e95d4c900bfd5a518636f868a51` at
commit `b00c3dd`; raw review `reviews/RD-36-instrument-v18-RAW.md`,
`VERDICT: REVISE`, 0 BLOCKING / 2 MAJOR / 5 MINOR — and all seven RD-35
repairs verified present, four re-proven by mutation). Every delta below
closes an RD-36 finding; dispositions in `reviews/DISPOSITION-REGISTER.md`.
**This is again a validator-and-records batch: no question block, no
verdict word, and no section §1–§8 of the instrument changed.** The
instrument bytes that move are the `effective_version:` header, the §9
v1.9 entry, and one dated correction marker inside the §9 v1.8 entry,
whose family claim RD-36 proved false — the narrowest lawful correction to
a false sentence an approval digest would otherwise bind. Validator
changes each carry fixtures **in both directions** where a direction
exists (`scripts/launch_gate_results.py --selftest`, **74 fixtures**).

RD-36's diagnosis, adopted as this batch's discipline: *"five of my seven
findings are cases where a fixture exists, passes, and cannot see the
defect, because the fixture set tests one direction of each predicate."*
This batch fixtures the empty and shadowed field cases, not only the
absent case, and replaces the one accepting fixture that certified a false
taxonomy. RD-37 tests whether that discipline change ends the chain's
pattern; like RD-35 and RD-36, this record predicts nothing.

## D-1 — `B-n` leaves the identifier family, and the false taxonomy is corrected everywhere it was asserted (RD36-01, MAJOR)

RD-36 swept 348 files: every `B-n` token outside the validator is
round-2026-08c review-finding numbering; **zero** appear in the decisions
home; no warrant identifier family exists. Yet a `READY-WITH-DEFERRALS`
pass citing `B-1` validated clean, and four artifacts asserted the family
"names made decisions" — including the §9 changelog, instrument bytes an
approval digest would bind. At v1.9:

- `DECISION_ID_RE` accepts **`SDR-n` alone**; `B-n` is rejected with a
  reason naming what it is ("review-finding numbering … names no decision
  in this repository and grants nothing").
- The accepting `B-1` fixture is **replaced** by a rejecting one —
  RD-36's words, accepted: an accepting fixture asserting a false
  taxonomy is worse than none.
- The §9 v1.8 entry gains a dated correction marker pointing at the v1.9
  entry; the entry is otherwise left as written.
- **Correction of the v1.8 delta's D-6, in the D-10 convention (the
  frozen record is not edited):** D-6 stated the identifier form
  "accepts `SDR-n`/`B-n` (made decisions)" — the parenthetical was false
  of `B-n`. The docstring is corrected in place; the disposition
  register's RD35-06 row (which named "warrant identifiers" the bytes
  never implemented) and the RD34-02 row's third stale claim carry dated
  corrections (RD36-07).

*Semantic change:* a citation family that granted nothing is closed.
Nothing weakened.

## D-2 — An empty field is absent, never the next line's text (RD36-02, MAJOR)

Every §5 field regex anchored its value with `\s*`, which crosses the
newline: a field written with an empty value silently captured the
following line as its answer, so a scoped row with no named defect and a
record with six Unknown rows and no settling evidence each validated
clean under `READY FOR` — while deleting the same lines errored. At v1.9
every field value is anchored `[^\S\n]*`: a valueless findings line takes
LG-9's absence path (its message now says so), and a valueless Unknowns
line beside Unknown rows is its own LG-12 error. Fixtures in both
directions per limb: empty-findings-beside-scoped rejected,
empty-Unknowns-beside-Unknown-rows rejected, the non-empty controls pass,
and the newline-crossing mutation was re-applied to a copy — the selftest
fails on exactly the new fixture.

## D-3 — A narrative line cannot shadow a declared field (RD36-03, MINOR)

The count fields, the deferral citation, and the launch-target line are
now parsed by collecting **all** occurrences: values that disagree are an
error naming the disagreement; agreeing occurrences resolve to the last
(declared) value. RD-36's demonstration — `Deferred count summary for the
reader: 0` zeroing a declared `Deferred count: 3` in the trend row while
three checks looked away — is a fixture.

## D-4 — A leading negation asserts emptiness (RD36-04, MINOR)

`_names_nothing()` gains the negation-prefix rule: a value whose first
token is `no`/`none`/`nothing`/`zero` names nothing, whatever nouns
follow. `no defects found`, `none identified`, `nothing of note`, and
`no findings in the deferred waves` — RD-36's four residuals — now reject
on LG-9, and the mirror false-rejection RD-36 found on LG-13
(`E3 reopen-list: none identified` erroring beside `E3 | Met`) disappears:
that value is again a lawful empty marker, fixtured. This is a semantic
rule, not a fifth enumeration extension. One disclosed edge: a genuine
finding line *led* by a negation clause would be wrongly classed as
empty — loudly, as a rejection the administrator sees, never as a silent
pass. **Correction of the v1.8 delta's D-5 reading, in the D-10
convention:** D-5's "the residual class is removed rather than chased"
was true of the eight strings RD-35 named and not of the class; RD-36
called the sentence "an invitation to the wrong reading," and this delta
adopts that correction rather than defending the sentence.

## D-5 — The eighth field (RD36-05, MINOR)

§5's `Reviewer:` fresh-context disclosure joins LG-12's presence set —
the one declared field the v1.8 batch left unenforced. Deletion is a
fixture. Presence tests remain content-blind by design; the docstring's
scope note now says so explicitly.

## D-6 — Both citation forms carry an existence guard (RD36-06, MINOR)

An `SDR-n` identifier is existence-checked against the decisions home at
the record's named commit (`git grep`, fixed string) when git checks run
— `SDR-9999` rejects, `SDR-33` accepts, both fixtured with real digests.
A path resolving to a git **tree** is rejected: a directory is not a
decision record. The identifier form is no longer the only citation form
without an existence guard.

## What did not change

Question IDs and texts A1–A6, B1–B5, C1–C7, D1–D4, E1–E6, F1–F6, G1 —
**zero question blocks changed**; §1 through §8 of the instrument are
**byte-unchanged from v1.8** (and therefore from v1.7 — the normative
text has now gone three amendments untouched). The closed verdict
vocabulary, the `READY FOR` conjuncts, and the `READY-WITH-DEFERRALS`
predicate are unchanged. All 74 fixtures pass; the prior 74-minus-new
still pass unmodified except that the shared GOOD template's version
line tracks the header (now substituted by shape, not by literal — the
RD34-05 lesson applied to the selftest builder itself) and the one
`B-1` fixture inverted its expectation deliberately (D-1). A record
lawful under a **correct** v1.8 reading remains lawful under v1.9 — the
newly rejected records are those §4 and §5 already condemned in prose:
citations that granted nothing, and fields that answered nothing.
