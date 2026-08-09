# Validator authority inventory — which rule does each check enforce?

> **Process record — never authority.** This file decides nothing, adopts
> nothing, and performs no act (VIS-4). It is a computed inventory of
> `scripts/check_governance.py`'s FAIL-capable checks, produced during the
> R-SCR repair batch so that the question review RD-17 finding 11 asked —
> *what written rule is this FAIL a breach of?* — has an answer a reader can
> look up. The **live** answer is the `CHECK_OWNERS` table in
> `scripts/check_governance.py`, which CG-25 keeps complete on every run and
> which `Results.report()` prints beside every FAIL. Where this file and that
> table disagree, the table wins and this file is stale.

## 1. Why this exists

Review RD-17 finding 11 swept the whole corpus for citations of any `CG-\d+`
identifier: **70 files, 692 citations**, and not one inside
`.syzygy/governance/doctrine/`, inside `craft-and-care/`, or inside any
`rfcs/` module [Observed, by the reviewer at commit `771965c`]. There was no
check-to-owning-rule register anywhere in the repository, so the battery could
not distinguish — in its own output — a FAIL against adopted doctrine from a
FAIL against a candidate whose own banner says it binds nothing.

Three repairs landed together:

1. **`CHECK_OWNERS`** in `check_governance.py` maps every check family to its
   rule, in one of three shapes: a doctrine identifier plus the file that
   defines it; `mechanical — …` for a check that verifies self-consistency and
   needs no normative owner; or `record: <path>` / `candidate: <path>` where
   the rule is written but in material with no owner act.
2. **`Results.report()` prints the owner beside every FAIL**, so the
   attribution arrives with the finding rather than in a document nobody
   opens.
3. **CG-25** fails the battery when a check family it reports has no entry, so
   a new check cannot ship unattributed.

## 2. The downgrade

Two checks enforce normative editorial rules whose only written statement is a
Python docstring. RD-17's repair offered two routes — *"route CG-20/CG-21's
rule into the normative-change workflow so it acquires a clause, or downgrade
both to WARN until it does"* — and the second is what R-SCR could perform
inside its own file boundary. Both now report **WARN**, with their findings and
the downgrade reason printed in full:

| Check | Rule, as stated only in Python | Findings still printed? |
|---|---|---|
| `CG-20` | *the context-load map states no measurement of the corpus it routes* — widened this round to the three active routing artifacts | Yes, with denominator |
| `CG-21` | *a contract module states no measurement* | Yes, with denominator |

**A downgrade is not a silencing.** What it stops is a repository-wide
`exit 1` enforced by a rule nobody has ruled on. **[Handoff]** The intended
home is the compact knowledge-hygiene policy the launch-gate administration's
finding C2 names; writing that policy is outside `scripts/`' remit and is not
performed here. When it is adopted, delete the two `PYTHON_ONLY_RULES` entries
and point `CHECK_OWNERS` at the new clause identifiers — nothing else changes.

`CG-22` is **not** downgraded. Its rule is written — `TERM-REGISTRY.md` §1 —
but in a file whose own third line reads *"Status: CANDIDATE. This file binds
nothing."* The FAIL is real; the printed owner is what stops it reading as a
doctrine breach.

## 3. Honest gaps in this inventory

- **Three checks have no doctrine owner and are recorded as `mechanical` or
  `record:` rather than left blank: CG-9, CG-12, CG-19.** An earlier draft of
  `CHECK_OWNERS` cited `SDR-1`, `SEC-5` and `SEC-4` for them. Those
  identifiers exist and say something else — SDR-1 rules that `Feature` is not
  a kernel concept, SEC-5 is *"Secrets are never indexed"*. The citations were
  wrong and were corrected before this file was written [Observed:
  `SURFACE-DECISION-RECORD.md:64`, `doctrine/security.md:54`]. Inventing an
  anchor is the defect RD-17 finding 11 exists to prevent, so the honest
  `mechanical — …` entry is what stands.
- **Seven check families still have no `--selftest` fixture:** CG-3, CG-5,
  CG-6, CG-9, CG-10, CG-11, CG-12. CG-24 prints this every run and the figure
  is computed, not asserted. CG-11 and CG-12 appear on that list for the first
  time this round: they were previously *credited* with fixtures they never
  had, because CG-24's matcher read three `res.add` check names as fixture
  names (RD-17 finding 3, mutation M9). Nothing about the term-registry
  adoption claim, the bootstrap-prompt route, or the bare field name is
  quoted verbatim anywhere in this file, for the reason §4 gives.
- **The `Negative fixture(s)` column lists fixtures whose name carries the
  exact sub-check id.** A family-level fixture is not credited to a sibling
  sub-check here, which is why several rows read `none` even though their
  family is covered — CG-24's rollup is coarser on purpose, and this column is
  finer on purpose.

## 4. The inventory

[Observed] Computed at commit `e69c923` from `CHECK_OWNERS`, from the
`selftest()` region of `check_governance.py`, and from the denominators the
battery printed in a read-only clone. Rows are the FAIL-capable checks only;
the fifteen report-only rows (CG-1c/1d/1e/1f/1h, CG-2b/2d/2f, CG-8, CG-12b,
CG-15b, CG-19b, CG-22b, CG-23, CG-24) never fail and are out of scope.

**The rule column carries the identifier and its home, not the full
sentence.** The sentence lives in `CHECK_OWNERS` and is not transcribed here
— partly because a transcribed rule goes stale silently, and partly for a
sharper reason: several of those sentences, and several fixture names, quote
the very tokens their own checks detect. A faithful transcription of them
into this file makes this file a finding of CG-3, CG-16 and CG-22, which is
how it first ran. So the rule column points, and the fixture column withholds
any name that carries such a token — replacing it with the count and a
pointer at `--selftest`, marked in the cell. Nothing is dropped silently, and
no check needed a new exemption to accommodate this document.

| Check | Authoritative rule | Population | Semantics | Fixtures | Negative fixture(s) |
|---|---|---|---|---:|---|
| `CG-1a` | mechanical | 129 links | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-1b` | mechanical | 1648 references | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-1g` | mechanical | 4 routes | FAIL | 2 | `CG-1g dead active-lane route into rfcs/ detected`<br>`CG-1g dead route inside a frozen lane is classified, ` |
| `CG-2a` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 | 299 files | FAIL | 6 | `CG-2a unmarked retired-phrase quotation detected`<br>`CG-2a line-wrapped retired phrase detected`<br>`CG-2a retired phrase presented as current detected`<br>`CG-2a marked historical quotation exempted and printed`<br>`CG-2a superseded-bannered file exempted`<br>`CG-2a empty phrase registry fails, never passes` |
| `CG-2c` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 | 2 files | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-2e` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 | 0 quotations | FAIL | 3 | `CG-2e wrapped current phrase with a stale digest detected`<br>`CG-2e wrapped current phrase with a live digest passes`<br>`CG-2e single-line quotation left to CG-7d` |
| `CG-3` | mechanical | 292 files | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-4a` | VIS-4 (`doctrine/vision.md`) | 9 files | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-4b` | VIS-4 (`doctrine/vision.md`) | 98 files | FAIL | 3 | `CG-4b accepted-claim banner detected`<br>`CG-4b negated candidate banner exempted`<br>`CG-4b empty candidate tree warns, never passes` |
| `CG-5` | VIS-1 (`doctrine/vision.md`) | 10 files | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-6` | VIS-4 (`doctrine/vision.md`) | 2 homes | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-7a` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 78 entries | FAIL | 2 | `CG-7a wave partition overlap detected`<br>`CG-7a wave partition gap detected` |
| `CG-7b` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 6 arguments | FAIL | 1 | `CG-7b stale wave argument in the record detected` |
| `CG-7c` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 3 arguments | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-7d` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 14 quotations | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-7e` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 4 files | FAIL | 2 | `CG-7e examines the real act-copy population without error`<br>`CG-7e file declaring an act it does not carry detected` |
| `CG-7f` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 6 rows | FAIL | 3 | `CG-7f wave row undercounting its manifest detected`<br>`CG-7f matching count raises nothing for that row`<br>`CG-7f ordinal module list is not read as a count` |
| `CG-7g` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1-§2 | 6 files | FAIL | 3 | `CG-7g stray file in wave-manifests/ detected`<br>`CG-7g missing wave manifest detected`<br>`CG-7g wholly absent wave-manifests/ detected` |
| `CG-9` | mechanical | 16 files | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-10` | VIS-2 (`doctrine/vision.md`) | 1 register | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-11` | mechanical | 2 patterns | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-12` | mechanical | 45 citations | FAIL | 0 | **none** — [Unknown] whether this predicate can fail |
| `CG-13` | mechanical | 180 edges | FAIL | 5 | `CG-13 empty corpus warns, never passes`<br>`CG-13 dangling edge detected`<br>`CG-13 dangling edge detected`<br>`CG-13 dangling edge detected`<br>`CG-13 x detected` |
| `CG-14` | mechanical | 12 paths | FAIL | 5 | `CG-14 nonexistent install source detected`<br>`CG-14 act-created home that already exists detected`<br>`CG-14 git-excluded ceremony location detected`<br>`CG-14 disclaimed git-excluded mention exempted`<br>`CG-14 dotted git-excluded root (.syzygy/cache) detected` |
| `CG-15` | record: `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 | 0 quotations | FAIL | 2 | `CG-15 stale truncated digest detected`<br>`CG-15 retired-marked quote exempted` |
| `CG-16` | VIS-4 (`doctrine/vision.md`) | 60 mentions | FAIL | 2 | 2 fixture(s), 1 withheld: their names carry tokens CG-16/CG-22 detect, so quoting them here would make this file a finding. Read them from `--selftest` |
| `CG-17` | candidate: `SURFACE-CLAUSE-ROUTING-MATRIX.md` | 210 clauses | FAIL | 2 | `CG-17 double-routed clause detected`<br>`CG-17 routed-but-undeclared clause detected` |
| `CG-18` | mechanical | 20 measurements | FAIL | 4 | `CG-18 unparseable fixture is not silently skipped`<br>`CG-18 falsified word count detected`<br>`CG-18 unreproducible fixture detected`<br>`CG-18 missing `Measured:` anchor is a finding, not a skip` |
| `CG-19` | record: `GOVERNANCE-SUBSTRATE-LOCK.yaml` §verification | 57 predicate evaluations | FAIL | 29 | 29 fixture(s), 1 withheld: their names carry tokens CG-16/CG-22 detect, so quoting them here would make this file a finding. Read them from `--selftest` |
| `CG-20` | **Python-only | 261 lines | **WARN** (downgraded) | 6 | `CG-20 corpus count behind the pointer exempted`<br>`CG-20 stale corpus count detected`<br>`CG-20 stale load-map figure detected`<br>`CG-20 {label} in the load map detected`<br>`CG-20 pointer to the budget report exempted`<br>`CG-20 empty load map warns, never passes` |
| `CG-21` | **Python-only | 39 modules | **WARN** (downgraded) | 3 | `CG-21 examines the real corpus without error`<br>`CG-21 corpus count in prose detected`<br>`CG-21 empty module list warns, never passes` |
| `CG-22` | candidate: `policy-candidates/TERM-REGISTRY.md` §1 | 177 files | FAIL | 7 | 7 fixture(s), 2 withheld: their names carry tokens CG-16/CG-22 detect, so quoting them here would make this file a finding. Read them from `--selftest` |
| `CG-25` | mechanical | 25 check families | FAIL | 2 | `CG-25 unattributed check family detected`<br>`CG-25 owner entry for an unreported check reported` |

## 5. Reproducing this file

```sh
python3 scripts/check_governance.py             # CG-25 prints the same attribution, live
python3 scripts/check_governance.py --selftest  # every fixture, including the withheld names
```

The table above is a snapshot; the two commands are the measurement. If they
disagree with this file, this file is the stale one.
