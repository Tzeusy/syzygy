# RD-6 — Source-of-truth review

**Commissioned:** 2026-08-06, no authoring context.

# VERDICT
VERDICT: REVISE

---

## Why REVISE and not EXCEPTIONS

The project's central claim — one owning artifact per assertion; presentation,
projections and personal state never become truth — holds in most of the
corpus, and in two places it holds better than I expected (see §0.2). Three
things put it below the line for a package about to be closed:

1. **Seven act digests are examined by no check.** Mutation-proven: I
   falsified all four act arguments in the artifact `AGENTS.md` names as *the
   owner-facing offering*, plus three in the round-2026-08c closure preflight,
   and the full battery reported `0 findings` and exited `0`. Finding **H-1**.
2. **A front-matter key inside act 1's digest set is authorized by no
   clause.** Three of the 32 modules the owner would sign carry
   `constrains: [...]`. The one contract clause that enumerates the selection
   relations (RFC11-4) does not include it, and still names a key
   (`provides_to`) that was deleted from every module. Finding **A-1**. A
   parallel session repaired the *projection* and wrote the *decision record*
   while I was drafting (both recorded, with corrections, at A-1 and E-1);
   neither touches the clause text, so this one stands.
3. **Five thresholds the checker polices, and prints as charter figures on
   every run, are attributed to charter sections that do not exist.** Finding
   **F-1**.

None of this is dishonesty and none is fabrication; every artifact I checked
said true things about itself. The failures are all of one shape: a rule
migrated into the thing that enforces it, and then the enforcement became the
only copy.

## 0.1 Method and denominators

| | |
|---|---|
| Baseline commit | `aee13d563cd9199522fde4297b03c6a8e17fdb79` |
| Tracked files | 237 |
| Working tree | **dirty and changing during the review** — 13 tracked files modified, 2 untracked. A parallel session is editing `TERM-REGISTRY.md`, the nine fixtures, and `scripts/check_governance.py`. Line numbers below are from the **working tree** unless marked *(at HEAD)*; every mutation test was run in a pristine `git archive HEAD` extraction at `scratchpad/mut`, never in the repository. |
| `grep` | ugrep. Every load-bearing enumeration in this report was produced by **Python `re` over `git ls-files`**, never by a bracket character class. Where I used `grep`, it was `grep -F` or `-E` and I say so. |
| Checks | Read for output, not exit code. `check_governance.py` exits `1` today on one working-tree-only finding (§0.3). |

## 0.2 What I tested and could not break

Stated so the findings below are read against a denominator, not against
silence.

- **[Observed] Criterion B is substantially clean.** I enumerated every line
  in the 65 files of the authoritative/normative lanes (`doctrine/`,
  `policies/craft-and-care/`, `contracts/candidates/rfcs/`, `decisions/`,
  `map/topology-candidates/`) that names a non-authoritative artifact —
  `intent/OVERVIEW.md`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`, the root
  `README.md`, any `round-*/`, any `/reviews/`. **90 lines in 27 files.**
  Adopted doctrine: **zero**. Craft policy: only `INSTALL-RECORD.md`, and only
  as digest provenance. Of the 90, **every `README.md` hit in a contract module
  is a *package* README** (`rfcs/RFC-000N/README.md`) — itself a contract module,
  a member of the act-1 manifest, and checked by CG-13. I found **no case** of
  `OVERVIEW.md`, `PROJECT-STATUS.md` or a round report cited as settling
  anything. This is a real pass and it is the hardest of the eight criteria to
  pass.
- **[Observed] Supersession precedence is stated everywhere it is needed.**
  The three paired artifacts that could disagree each name their winner in
  their own first ten lines: `SURFACE-CLAUSE-ROUTING-MATRIX.md:3` ("Where it
  and a clause disagree, **the clause wins**"),
  `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:5` ("Where this file and
  `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` disagree, **that record
  wins**"), and the two superseded files carry `SUPERSEDED` banners at line 1.
- **[Observed] Two registries I expected to be misplaced are not.**
  `07-AUTONOMY-EXTENSION-REGISTER.md:39` closes itself: "the register itself
  authorizes nothing." The RFC9-18 layout-version registry — which RFC3-16(a)
  *does* gate — is placed under `.syzygy/map/**` (RFC9-16(d)), inside the
  governed plane. Correct.
- **[Observed] All four regeneration checks are clean at the working tree.**
  `build_contract_index.py --check`, `build_dependency_index.py --check`,
  `build_budget_report.py --check`, `verify_final_prespec.py` — no drift, PASS.
- **[Observed] Manifest population is complete.** 32 manifest rows, 32 `.md`
  modules on disk under `rfcs/`, set difference empty in both directions
  (Python `os.walk` vs. parsed manifest). No module is silently outside act 1.
- **[Observed] All 26 act-digest copies in the repository currently agree**
  with their subjects. The problem in **H-1** is not a stale digest; it is that
  11 of them are unpoliced, so the next one to go stale will not be seen.

## 0.3 One live, working-tree-only finding, disclosed and excluded

`check_governance.py` **FAILs CG-1b today**: `TERM-REGISTRY.md` cites
`../round-2026-08c/PUBLIC-VOCABULARY-COMPREHENSION-REPORT.md`, which does not
exist. It is **absent at HEAD** — a parallel session introduced it minutes ago
and is presumably about to create the target. I record it and score nothing on
it. At HEAD the battery is `0 FAIL`.

---

# Findings

## H — Act digests

### H-1 · Seven act digests are examined by no check. Mutation-proven. **[Observed]**

**The claim under test.** The battery reports `CG-7d act digests quoted
anywhere match their subjects — 7 quotations examined, 0 findings`, whose own
docstring says "This check makes every copy load-bearing"
(`scripts/check_governance.py:714`). It does not.

**Enumeration (Python `re` over all 237 tracked files, byte-scanning every
`\b[0-9a-f]{8,64}\b` token against the five live subject digests).** 26 copies
in 15 files. Computed subjects:

| Act | Subject | sha256 |
|---|---|---|
| 1 | `ACTIVE-CONTRACT-MANIFEST.txt` | `9fac6b78…3f2e68` — **re-quoted to `2862b2f5…f057d7` during this review**, see the note at the end of H-1 |
| 2 | `craft-and-care/testing-and-verification.md` | `7a716090…9690a0` |
| 3 | `topology-candidates/BUNDLE-MANIFEST.md` | `7a3b2249…baeb45` |
| 4 | `.syzygy/intent/OVERVIEW.md` | `01d62951…9c7cd1` |
| 5 | `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | `e973e8e0…d8f9c9` |

**Which of the 26 each check reaches.** CG-7d requires *the act phrase and the
64-hex on the same line* (`ACT_SUBJECTS`, `:672-689`; matcher `:740-746`). CG-15
requires *a truncation marker* — `TRUNC_DIGEST = r"`?\b(?P<d>[0-9a-f]{8,63})(?:…|\.\.\.)"`,
`:1298` — and caps at **63** hex. **A full 64-hex digest quoted without its act
phrase therefore matches neither pattern.** There are 11 such copies; 4 more sit
in `ACT_QUOTE_EXEMPT` review directories (correctly — verbatim evidence).

Unpoliced copies, with the file and line:

| File:line | Act | Why unseen |
|---|---|---|
| `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:39` | 1 | bare 64-hex, no phrase |
| `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:41` | 3 | bare 64-hex, no phrase |
| `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:42` | 4 | bare 64-hex, no phrase |
| `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:43` | 5 | bare 64-hex, no phrase |
| `round-2026-08b/PUBLIC-CLONE-VERIFICATION-REPORT.md:60,61,62` | 3,4,5 | bare 64-hex, no phrase |
| `round-2026-08c/FINAL-CLOSURE-PREFLIGHT.md:131,132,133` | 3,4,5 | bare 64-hex, no phrase |
| `craft-and-care/INSTALL-RECORD.md:105` | 2 | digest-list row, no phrase |

The first four are the decisive ones. `AGENTS.md:49` states: "The owner-facing
offering is `contracts/candidates/round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`."
**Every act argument in the document the owner actually reads is unchecked.**
The three in `FINAL-CLOSURE-PREFLIGHT.md` are the closure gate's own copies.

**Mutation test (verification rule 6), run in a pristine `git archive HEAD`
extraction, not in the repository.** I replaced all four digests in the
owner-facing offering with `dead000…` and all three in the closure preflight
with `beef111…` — seven falsified act arguments — and re-ran the battery:

```
OK    CG-7a  manifest digests valid — 32 entries examined, 0 findings
OK    CG-7b  act-1 argument matches the manifest — 1 argument examined, 0 findings
OK    CG-7c  acts 2/3/4 arguments match their subjects — 3 arguments examined, 0 findings
OK    CG-7d  act digests quoted anywhere match their subjects — 7 quotations examined, 0 findings
OK    CG-15  truncated digest quotes still current — 1 quotation examined, 0 findings
exit=0
```

Denominator unchanged, findings zero, exit clean. This is precisely the defect
CG-7d's own docstring says it was written to close after "six independent
reviewers, RB-1 F1 … RB-8 F1" — closed for the *phrase-bearing* half of the
population and left open for the other.

**Smallest correction.** CG-7d's population is "a line carrying an act phrase";
it should be "a line carrying any 64-hex token", checked against the set of
current subject digests exactly as CG-15 already does for truncations
(`:1311-1325` already computes that set). Equivalently: extend `TRUNC_DIGEST`'s
`{8,63}` to `{8,64}` and make the ellipsis optional. Either makes all 26 copies
load-bearing. **[Inferred]** — I did not implement or test the fix.

**The act-1 argument moved during this review, and the evidence got stronger.**
The parallel session's contract edits regenerated the manifest: act 1's
argument is now `2862b2f54e39e6d477129147eb2e1d0cb4ca714c26edabd75505e2e38ff057d7`
(computed; `CG-7a` prints the same). I re-checked all four unpoliced copies in
the owner-facing offering. **They were updated by hand and are correct** —
`FINAL-OWNER-ACCEPTANCE-RECORD.md:39` now carries the new digest.

That is the finding, not a refutation of it. This is the **fifth** re-quotation
of the act-1 argument (the acceptance record's own §1 note enumerates four
prior ones: `f2914fc5…`, `41195c81…`, `ac07a064…`, `2922de1c…`). Four of those
copies stay correct **only because a person remembered them**, on a package
whose stated design principle is that a digest quoted anywhere is a promise the
artifact keeps. The phrase-bearing copy at
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15` is held true by CG-7b/d;
the four beside it in the document the owner reads are held true by
recollection. On the next re-quote — and there has been one per repair pass —
the battery will report `7 quotations examined, 0 findings` whether or not they
were updated. **[Observed]**

**Also observed, minor.** `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md`
carries a `SUPERSEDED — Do not act from this file` banner, is listed by CG-15b
among "superseded records holding old digests", **and** contributes 2 of CG-7d's
7 live-offer quotations (`:81` act 2, `:107` act 3). A file cannot
simultaneously be history for one check and a live offer for another. Both
digests are currently correct, so nothing is wrong today.

---

## F — The generated-vs-authored boundary in the checks

### F-1 · Five thresholds the checker enforces cite charter sections that do not exist. **[Observed]**

`check_governance.py` cites charter sections 19 times (`grep -oE`, deduped).
Tested against the two charters in the repository —
`candidates/COMPACTION-CHARTER.md` and `round-2026-08/OWNER-ROUND-CHARTER.md` —
by parsing every numbered heading with Python `re` **and** by `grep -F "§N.N"`:

| Cited by the checker | Sites | In COMPACTION-CHARTER | In OWNER-ROUND-CHARTER |
|---|---|---|---|
| `§11.4` | `:36, 769, 836, 853, 857, 861` | absent | **present** |
| `§18` | `:59` | absent | **present** |
| `§17` | (docstring `:10`) | absent | **present** |
| **`§7.1`** | `:796, 838, 845` | **absent** | **absent** |
| **`§7.3`** | `:36, 781, 815, 818, 860, 2037` | **absent** | **absent** |
| **`§9.3`** | `:53` | **absent** | **absent** |
| **`§9.4`** | `:52, 2717` | **absent** | **absent** |

`COMPACTION-CHARTER.md` has **no numbered headings at all** (Python `re` over
`^#{1,6}\s*\d+`, result `[]`).

What that leaves living only inside the checker:

- **`DEFAULT_LOAD`** (`:785-790`) — the four-file set said to be "what a fresh
  agent session loads", attributed to "Charter §7.3 requires the *default agent
  load* to be reported" (`:781`). Printed as `§7.3 default-load figures` in the
  CG-8 summary note **on every run** (`:860`). No charter says this.
- **The 900–1,200 authored-word band for `AGENTS.md`** (`:843`), attributed to
  "§7.1's tighter target" (`:838`) and reported as "outside the §7.1
  900–1,200 target band" (`:844-845`). No charter says this. `CC-BUDGET-1`
  (`policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:290-297`) gives AGENTS
  a **1,500-word** trigger and no band; the 900 floor appears nowhere else.
- **`TOKENS_PER_WORD = 1.35`** (`:791`), duplicated at
  `scripts/build_budget_report.py:51`.

The rest of `BUDGETS`/`MODULE_TRIGGER`/`MODULE_DECOMPOSE` (1,200 / 1,500 /
4,000 / 5,000, `:774-779`) *are* transcriptions of `CC-BUDGET-1`'s table — a
**candidate** policy that binds nothing. So the checker's numbers have two
provenances and neither is a binding artifact: four copied from an unaccepted
policy, three invented.

This is the exact class the battery's own comment names as the one it exists to
catch — `check_governance.py:2774-2778`: *"A hard-coded copy is the
transcription class this battery exists to catch: the list sat here for one
round, and the moment the registry moved a term between tiers the check went on
policing the old split while reporting green."*

**Smallest correction.** Either (a) correct the four citations to the sections
that do exist and move the two invented figures into `CC-BUDGET-1` as a
proposed addition, or (b) say plainly in CG-8's note that the default-load set
and the 900–1,200 band are the checker's own operating figures with no
governing artifact. (b) is honest and costs one sentence. **[Inferred]**

### F-2 · A justification hard-coded in the verifier, attributed to a report that does not contain it. **[Observed]**

`candidates/scripts/verify_final_prespec.py:26-32`:

```python
JUSTIFIED_OVERSIZE = {
    "rfcs/RFC-0001-project-graph-identity-state-planes.md":
        "dictionary-shaped kernel contract: 23% verbatim closed vocabularies "
        "(entity/plane/relation/four-sense tables); reader groups not "
        "distinct, so no honest split exists; floor established by two "
        "compaction passes (see 03 report)",
```

The comment above it (`:24-25`) says the justification is "also carried in
`03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`". It is not. `grep -F "23%"` over all
tracked `.md`/`.py` returns 7 hits; **none is in the 03 report.** The 03
report's "Risks accepted" item 3 (`:114-115`) reads in full: *"RFC-0001's 8,353
words remain a single mandatory load for kernel tasks; accepted as the honest
floor of a dictionary contract."* — no percentage, no "reader groups not
distinct", no "two compaction passes". The 23% figure lives in
`LEAD-SWEEP-NOTES.md:34` and `WORKER-REPORT-DIGEST.md:12` (both **unmarked**
candidate artifacts — see C-2).

So the sole full statement of the only waiver against the module ceiling is a
Python dict literal, printed to the reviewer as a `note:` on every run, citing
a source that does not carry it. Two prior reviews accepted it as recorded
(`rev10-digestibility-review.md:114` explicitly attributes it to "03 report
§'Risks accepted' item 3").

### F-3 · Rules with a second copy inside the enforcement, enumerated. **[Observed]**

All read directly; population is the five scripts (2,992 + 412 + 171 + 321 +
82 + 272 = 4,250 lines).

| # | Constant | Line | The rule it copies | Consequence |
|---|---|---|---|---|
| 1 | `STATUS_QUALIFIERS` (8 entries) | `check_governance.py:2671-2674` | the term registry §1's closed dimension set | The registry is **candidate and being rewritten right now**; the checker's copy cannot notice. Contrast CG-23 six lines of comment later, which *derives* the core set from the registry precisely so it "cannot disagree with the artifact it checks" (`:2778`). CG-22 does what CG-23's comment forbids. |
| 2 | `PHASE_RULES` / `PHASE_RULE_CLAUSES` | `build_contract_index.py:35` **and** `verify_final_prespec.py:47` | the six phase-boundary clauses | Two independent copies of one closed set in two scripts. Both list `RFC10-16`; `REV10_ENDS` in the same file says RFC-0010 now ends at 22. |
| 3 | `REV9_ENDS` / `REV10_ENDS` | `verify_final_prespec.py:36, 41` | per-RFC clause-count ends | Sourced to "`FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` §3 of the rev9 package" — a **git-excluded `_bootstrap/`** artifact. Unverifiable in a clone. |
| 4 | `OUTCOMES` (10 entries) | `verify_final_prespec.py:48-59` | the migration matrix's closed outcome vocabulary | The matrix does not state its own vocabulary; the script is the only copy. |
| 5 | `7000` ceiling / `57000` corpus band | `verify_final_prespec.py:119, 256`; `build_budget_report.py:276-284` | "~7,000" (approximate) in `COMPACTION-CHARTER.md:154`, `02:47`, `03:149` | The authoring sources say **~7,000**; the enforcement says `> 7000` and the generated report prints "**The 7,000-word per-module ceiling**" as definite. Approximation lost in derivation. |
| 6 | `PROPOSED_TRIGGER_TOKENS=20000`, `PROPOSED_BAND=(5000,15000)` | `build_budget_report.py:57-58` | `CC-BUDGET-1` rows 5–6 | Correct transcription today; a second copy of a candidate policy's table. The report is honest that the rule is not installed. |
| 7 | `LOCK_DISPOSITIONS`, `LOCK_FORGE_ALLOW`, `LOCK_META_KEYS`, `LOCK_NONPIN_SECTIONS` | `check_governance.py:1592-1594` | the substrate lock's own vocabularies | The lock does not declare them; the script is the only copy. Defensible (the allowlist is deliberately a deliberate edit) but undeclared in the artifact. |
| 8 | `ACT_SUBJECTS` — five act phrases + subjects | `check_governance.py:672-689` | `AGENTS.md:41` says "The acceptance record owns the phrases and the ceremony" | Partly mitigated: CG-7c reports a finding if a phrase disappears from the record. But the checker, not the record, decides what counts as an act phrase — which is how H-1 is possible. |
| 9 | `status_source: owner-act-record` **emitted unconditionally** | `build_contract_index.py:117` | each module's front matter | The generator asserts the field rather than projecting it. A module whose front matter said something else would be silently overwritten in the index. |
| 10 | `clause_kind` §8→open-question, §0/§6/§7→informative | `build_contract_index.py:61-70` | the contracts' section conventions | Section-number semantics stated nowhere but the generator. |
| 11 | `RFC(?:6\|7\|8\|9\|10\|11)` | `check_governance.py:1450` | which contracts CG-17 routes | A twelfth contract would silently leave CG-17's denominator. |

### F-4 · CG-9's name overclaims what it can test. **[Observed]**

`cg9_duplicate_homes` (`:877-892`) counts files whose path contains
`/doctrine/` or `/craft-and-care/` and then asserts they start with the doctrine
or craft home. Those two conditions are near-tautological, which is why it
reports `16 files examined, 0 findings` and structurally cannot do otherwise —
16 is exactly the count of `.md` files under those two directories
(`git ls-files | grep -E "(/doctrine/|/craft-and-care/)"`, 16). **The check
named "duplicate authority homes absent" tests path strings, not duplicated
content, and every finding in section A of this report is invisible to it.**
The check is not wrong; its name is a coverage claim it does not make good on.

---

## A — Duplicate authority

### A-1 · The contract-relation vocabulary is stated in two places that disagree today. **[Observed]**

**Copy 1 — a contract clause, inside act 1's digest set.**
`rfcs/RFC-0011-context-compiler.md:105-112`, RFC11-4:

> Mandatory context is selected deterministically … from, at minimum: … **contract
> dependencies (`depends_on` / `provides_to`)**; explicit `applies_to` and
> clause-level metadata (the contract-index projection …)

**Copy 2 — a generator docstring and the file it emits.**
`candidates/scripts/build_dependency_index.py:7-39` defines **three** relations
with their authoring rules, and `CONTRACT-DEPENDENCY-INDEX.md:14` (generated,
`:181-190` of the generator) states them as a normative table telling a
selector what to load: `depends_on` = "**mandatory load**, transitively";
`constrains` = "loaded **when the task class crosses the constrained seam**";
`cites` = "**never automatic**".

They disagree in both directions:

- RFC11-4 tells a compiler to select on **`provides_to`**. The generator
  (`:31-37`, `:187-190`) states that `provides_to` is derived by reversal and
  "appears in no module's front matter". `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`
  records that "every module's `provides_to` front matter was removed as
  derived". **RFC11-4 names an input that no longer exists as authored data.**
- The generator adds **`constrains`** and **`cites`**, which RFC11-4's
  enumeration does not contain and no clause anywhere defines.

**Which wins today, and what enforces it.** RFC11-4 is a contract clause and
`CONTRACT-DEPENDENCY-INDEX.md:5` says "**The modules win over this file,
always**" — so the contract wins. **Nothing enforces it.** The `--check` drift
test compares the generated file against a regeneration, so both copies of the
disagreement regenerate identically; this is the same failure the generator's
own docstring describes at `:32-34` ("regenerating a knowingly-broken graph
reproduces the same knowingly-broken file"). `verify_final_prespec.py` checks
clause citations, not front-matter key vocabulary. No check reads RFC11-4's
enumeration.

**The sharper half.** Three modules **inside act 1's digest set** now carry a
front-matter key no clause authorizes (`sed` over front matter, verified):

- `rfcs/RFC-0006-cross-surface-selection-query-drawer.md:9` — `constrains: [RFC-0005]`
- `rfcs/RFC-0008/identity-authority-materialization.md:10` — `constrains: [RFC-0007]`
- `rfcs/RFC-0008/README.md:11` — `constrains: [RFC-0007]`

**Re-checked at submission:** the parallel session has since *moved* these keys
— they now sit on `rfcs/RFC-0007/narrative-contract.md:10`
(`constrains: [RFC-0001, RFC-0002, RFC-0004, RFC-0008]`) and
`rfcs/RFC-0005/admission-and-boundary.md:10`
(`constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]`). The edge set changed;
the finding did not. **RFC11-4 is byte-unchanged** (re-read at submission,
`:105-113`): it still enumerates "contract dependencies (`depends_on` /
`provides_to`)", still names a key no module carries, and still defines no
relation called `constrains`. Two modules inside act 1's digest set now carry
eight `constrains` edges authorized by no clause — more than when I started.

The owner would be binding, at digest, a metadata key whose meaning is defined
only in a script. **Smallest correction:** amend RFC11-4 to enumerate the
relation set actually in use, and drop `provides_to` from it as derived. That
is a semantic delta on a clause in act 1's digest set, so it re-quotes the
act-1 argument — which is the honest cost, not a reason to defer. **[Inferred]**

**Disclosure — a partial repair landed mid-review.** `build_contract_index.py`
was edited by the parallel session while I was reading it (+25/−2; my earlier
line numbers for that file shifted, and are corrected above). The new comment
at `:129-135` reads: *"`constrains` and its clause anchor are projected because
RFC11-4 names this index as a selection input, and a relation absent from the
selector's declared inputs is a relation no selector reads — review RD-4,
finding F-14."* That makes the **index** carry `constrains`. It does **not**
close this finding: RFC11-4's clause text still enumerates only
`depends_on` / `provides_to`, still names a key that no module carries, and
still defines no relation called `constrains`. The repair moves the vocabulary
one register further out — into the projection RFC11-4 points at — rather than
into the clause that owns the enumeration. **[Observed]** for the edit and its
comment; **[Inferred]** that it does not close the disagreement.

### A-2 · The budget figures exist in four places. **[Observed]**

`CC-BUDGET-1` (candidate policy, binds nothing) →
`check_governance.py:774-779` → `build_budget_report.py:57-58` →
`verify_final_prespec.py:119,256`. Four copies of one table; all four agree
today (checked value by value); none is a binding artifact; nothing compares
them. Detail in **F-1** and **F-3 #5/#6**.

### A-3 · Approximate in the source, exact in the derivation. **[Observed]**

Every authoring statement of the module ceiling says **"~7,000"**
(`COMPACTION-CHARTER.md:154`, `02-OWNER-DIRECTION-RECORD.md:47`,
`03-ACTIVE-CONTRACT-COMPACTION-REPORT.md:149`, `04-CLAUSE-MIGRATION-MATRIX.md`
×5). The generated `CONTEXT-BUDGET-REPORT.md:100,105` prints "**The 7,000-word
per-module ceiling**" and a per-module "Over the 7,000 ceiling | **yes**"
column. `rev10-digestibility-review.md:115` records the consequence a reader
already had: *"RFC-0009 `semantic-geography`, 6,999 w against a stated
7,000-word ceiling — one word under."* The tilde is the whole difference
between a trigger and a law, and the projection dropped it.

---

## E — Derived views that have become truth stores

### E-1 · `CONTRACT-DEPENDENCY-INDEX.md` is the only home of the relation model, and its cited decision record does not exist. **[Observed]**

`build_dependency_index.py:38-39` cites two records for the three-relation
decision:

```
`round-2026-08b/DEPENDENCY-CLOSURE-REPORT.md` and
`round-2026-08c/RELATION-MODEL-DECISION.md`.
```

When I ran `ls .syzygy/governance/contracts/candidates/round-2026-08c/`, the
directory held `FINAL-CLOSURE-PREFLIGHT.md`,
`MISSION-CONTRACT-SEMANTIC-DELTA.md`, `PROJECT-SHAPE-FACETS-BRIEF.md`,
`PROJECT-SHAPE-FACETS-ROUTING.md`, `TERM-REGISTRY-SEMANTIC-DELTA.md`,
`reviews/`. **`RELATION-MODEL-DECISION.md` was absent.**

> **CORRECTION, made before submitting.** The file now exists — mtime
> `02:37:18`, created by the parallel session **after** my check and while I
> was drafting. It is absent at HEAD and present, untracked, in the working
> tree. I read it: 9,181 bytes, correctly banner-marked *"Candidate. Binds
> nothing"*, and it states the three-relation model and its rationale. **This
> half of E-1 is repaired in the working tree** and I withdraw the "does not
> exist" claim as of now. What survives:
>
> - The generator cited it for the whole of the interval it did not exist,
>   which is how the gap was findable at all; and **CG-1b still cannot see a
>   dangling reference in a `.py` docstring**, so if the file is moved or
>   renamed the citation will dangle silently again. That sub-finding stands
>   unchanged.
> - The new record says *"Where this file and the generated
>   `../CONTRACT-DEPENDENCY-INDEX.md` disagree, the index is derived from the
>   modules and the modules win over both."* It is a **candidate decision
>   record, not a clause**, and it does not touch RFC11-4's enumeration. **A-1
>   is unaffected**: the contract text still names `depends_on` / `provides_to`
>   and no relation called `constrains`.

No check sees this: **CG-1b scans `.md` files only** (`md_files(paths)`,
`:285`), so a dangling path reference inside a `.py` docstring is outside the
1,130-reference denominator entirely.

The standing point, restated against the corrected facts: for the whole of the
reviewed commit, a rule that (a) governs a front-matter key inside act 1's
digest set and (b) tells a context selector what to load existed **only** in a
generator's docstring and the file that generator emits, with its decision
record named and absent. That is the definition of a derived view that has
become a source. It has now been given an authored home — a candidate one, and
not the clause that A-1 says needs the edit.

### E-2 · Facts that exist only in `CONTEXT-BUDGET-REPORT.md`. **[Observed]**

The report is honest about being generated and is checked two ways. Two
residuals:

- **`**As-of commit:** <sha>`** (`build_budget_report.py:224`, from
  `head_commit()` at `:190-198`) writes the founder's `git rev-parse HEAD` and
  a `git status --porcelain` dirty flag into a **tracked** artifact. In a clone
  without git it renders `unknown` *and* asserts "(plus uncommitted
  working-tree edits at generation time)" — a claim about a working tree that
  does not exist. `_without_asof` (`:309-320`) excludes the line from `--check`,
  so nothing ever verifies it. Machine-local state in a tracked file, by
  construction. Low severity — the line is disclosed as generated — but it is a
  criterion-D instance.
- The §2 candidate-budget-exception rows are correctly *parsed* from each
  fixture (`waiver_fields`, `:121-135`, with the right comment about why). No
  finding.

### E-3 · `05-CONTRACT-INDEX.yaml` carries no candidate marker and asserts a status field it does not project. **[Observed]**

See **C-1**. Both halves — the missing marker and the hard-coded
`status_source` — sit in the same file.

### E-4 · `ACTIVE-CONTRACT-MANIFEST.txt` has no generator. **[Observed]**

`grep -F "ACTIVE-CONTRACT-MANIFEST"` over `scripts/`,
`candidates/scripts/` and `.github/` returns only `check_governance.py` (4
hits, all consumers). The file's header carries a shell one-liner
(`find rfcs -name '*.md' | sort | xargs sha256sum`) and nothing runs it. It is
therefore hand-maintained — and it is **act 1's subject**. I could not break it
(population verified complete, §0.2), and CG-7a validates all 32 rows, so this
is an observation about how the guarantee is obtained, not a defect: the
protection is CG-7a, not the regeneration discipline the other three views
have.

---

## C — Hidden candidate definitions

### C-1 · The contract index states `status_source: owner-act-record` for eleven candidate contracts, with no candidate marker anywhere in the file. **[Observed]**

`05-CONTRACT-INDEX.yaml:1-6`:

```yaml
# CONTRACT-INDEX — generated projection; rebuild with scripts/build_contract_index.py
# Authoritative metadata lives in the active contract files' front matter.
contracts:
  - id: RFC-0001
    title: Project Graph, Identity and State Planes
    status_source: owner-act-record
```

Two problems in six lines. **First**, the header discloses that the file is
*generated* and says nothing about the contracts being *candidate*. Every
module it projects carries, in its own body, "Absent such a record, this
contract binds nothing" — the projection carries none of that. A reader who
opens the index (which `06-CONTEXT-LOAD-MAP.md` and the routing matrix send
them to) sees eleven contracts with a status field and no indication that no
act has been performed.

**Second**, `status_source` is **not projected** — `build_contract_index.py:128`
emits the literal string unconditionally for every contract, outside the
front-matter key loop immediately below it. The one field in the file that
speaks to authority is the one field that is not read from the artifact it
claims to project. All 32 modules do declare `status_source: owner-act-record`
today (`grep -h "^status_source:"`, 32/32 identical), so nothing disagrees
right now; the defect is that a module changing it would be silently
overwritten rather than reported.

**Smallest correction.** Emit the candidate banner as a comment block from the
generator, and read `status_source` from `fm` like every sibling key.
**[Inferred]**

### C-2 · Eleven candidate-lane artifacts carry no candidate or non-authority marker. **[Observed]**

Method: Python `os.walk` over `candidates/*.{md,yaml,txt}` plus `rfcs/**` and
`policy-candidates/**` — **62 artifacts** — testing the first 30 lines for any
of `candidate` / `binds nothing` / `not authority` / `never authority` /
`superseded` / `proposed foundational`. (I ran a 12-line window first and it
over-reported 47; the 32 RFC modules carry their disclaimer at lines ~15-22.
Corrected figure below.)

**11 of 62** have no marker:

```
01-REV9-ADVERSARIAL-FINDINGS.md      07-AUTONOMY-EXTENSION-REGISTER.md
02-OWNER-DIRECTION-RECORD.md         08-OPEN-QUESTION-TRIAGE.md
03-ACTIVE-CONTRACT-COMPACTION-REPORT.md   09-OPEN-SPEC-READINESS-REPORT.md
05-CONTRACT-INDEX.yaml               10-EXIT-REPORT.md
COMPACTION-CHARTER.md                LEAD-SWEEP-NOTES.md
WORKER-REPORT-DIGEST.md
```

Three of these matter beyond hygiene, because other artifacts and scripts lean
on them as sources: `03-…COMPACTION-REPORT.md` is cited by
`verify_final_prespec.py:24` and `build_budget_report.py:278` as the home of the
ceiling and the corpus band; `COMPACTION-CHARTER.md` is the charter CG-8 cites
(**F-1**); `WORKER-REPORT-DIGEST.md:12` and `LEAD-SWEEP-NOTES.md:34` are the
only artifacts carrying the 23% figure the verifier attributes elsewhere
(**F-2**). `07-AUTONOMY-EXTENSION-REGISTER.md` closes itself in its own body
(`:39`) and is fine.

**CG-4's denominator is the reason none of this shows.** CG-4 examines **8
files** — `00-README.md`, `policy-candidates/*`, and the topology members
(`:465-487`). The other 54 artifacts in the candidate lane are outside the
check entirely, while the summary line reads `OK CG-4 candidate homes carry
candidate banners — 8 files examined, 0 findings`. Denominator against
population: 8 of 62.

### C-3 · The term registry claims mechanical enforcement from a check that does not do it. **[Observed, at HEAD; being repaired in the working tree]**

`policy-candidates/TERM-REGISTRY.md:60-61` **(at HEAD)**:

> Tracked in `PENDING-OWNER-DECISIONS.md`; **enforced mechanically by
> `check_governance.py` CG-17** once the core set is owner-accepted, and
> reported until then.

CG-17 routes surface clauses of RFC 0006–0011 and has nothing to do with
vocabulary. The checker **already records this correction as done** —
`check_governance.py:2771-2773`: *"The registry previously promised this
enforcement from 'CG-17', which routes surface clauses and has nothing to do
with vocabulary. **Corrected 2026-08-06.**"* The correction was made in the
script's comment; the artifact still said `CG-17`. A repair recorded in the
enforcement rather than in the thing repaired is the same shape as **F-1** and
**F-2**.

**Disclosure:** the uncommitted working tree now reads `check_governance.py
**CG-23** performs that sweep` at `:85`. A parallel session is fixing it as I
write. I score it because it was true at the reviewed commit and because the
*shape* — correction lands in the checker's comment, artifact left stale —
recurs three times in this report.

---

## D — Personal or machine-local state affecting truth

### D-1 · CG-14's git-excluded-location guard misses two of the three git-excluded paths. **[Observed]** — this is the prior round's defect class, recurring.

`_git_excluded_roots()` (`check_governance.py:1151-1169`) parses `.gitignore`
rather than hardcoding — the right instinct, and its docstring says so. But
`:1167`:

```python
if seg and not seg.startswith("."):
    roots.add(seg)
```

Any git-excluded path whose first segment begins with `.` is dropped.
Executed:

```
excluded roots parsed from .gitignore: ['__pycache__', '_bootstrap']
```

`.gitignore` declares **five** exclusions: `.dolt/`, `.syzygy/cache/`,
`.syzygy/local/`, `_bootstrap/`, `__pycache__/`. **`.syzygy/cache/` and
`.syzygy/local/` — the two paths `AGENTS.md` and this commission both name as
"git-excluded by design" — are outside the guard.**

Demonstrated against the real function:

```
.syzygy/local/         -> OK     []
.syzygy/cache/         -> OK     []
_bootstrap/state/      -> FAIL   ['`_bootstrap/state/` — named by the ceremony as a
                                   location, but it is git-excluded and therefore
                                   absent from every clone; …']
```

A ceremony step naming `_bootstrap/state/` fails, as designed. The identical
step naming `.syzygy/local/state/` passes. For those two paths CG-14 falls back
to `_dir_exists` (`:1135-1148`), which asks `os.path.isdir` **first** — the
founder-machine answer. So: a ceremony step naming `.syzygy/local/**` passes on
a machine where the directory happens to exist and fails inside a clone. That
is verbatim the divergence CG-14's docstring says it was written to end
(`:1185-1189`: *"the founder's copy of `_bootstrap/` made a step read as
executable here that failed the moment the same check ran inside a clone"*).

**No ceremony step names those paths today**, so nothing is currently wrong —
the guard is simply not load-bearing where it is claimed to be. The `--selftest`
fixture at `:2022-2028` tests `_bootstrap/state/` only, so the gap has never
been exercised.

**Smallest correction.** Delete `and not seg.startswith(".")` at `:1167` and
compare full path prefixes rather than first segments; add a `--selftest`
fixture for `.syzygy/local/`. **[Inferred]** — I did not implement it.

### D-2 · The default check scope depends on the founder's working tree. **[Observed]**

`corpus_paths(scope="clone")` (`:139-171`) unions `git ls-files` with
`git ls-files --others --exclude-standard`. Today that adds two untracked
files, one of which is `syzygy_claude_surgical_final_prespec_closure_prompt.md`
— a session prompt at the repository root, not part of the repository. The
battery's header prints:

```
scope:  clone — 238 file(s) examined (237 tracked, 1 untracked-not-ignored)
```

so **every denominator in the run is a function of what happens to be lying in
the founder's working directory**, and a clone reports 237. The design note at
`:141-147` justifies including untracked files (the candidate package was
untracked once) and both counts are printed, which is the mitigation. But the
justification has expired — the candidate package is tracked now — and the
residual cost is that CG-2a/CG-3/CG-12/CG-22 will scan, and could report
findings against, whatever scratch file is present. Low severity; disclosure is
adequate; the default should now arguably be `tracked`.

### D-3 · Machine-local state in a tracked generated artifact. **[Observed]**

See **E-2** — `CONTEXT-BUDGET-REPORT.md`'s as-of commit line, written from the
founder's `git rev-parse HEAD` and never verified.

### D-4 · A verifier's clause-count baseline is sourced to a git-excluded artifact. **[Observed]**

`verify_final_prespec.py:35-36`:

```python
# Rev9 baseline: authoritative numbered-clause ends per RFC (frozen facts;
# see FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md §3 of the rev9 package).
REV9_ENDS = {1: 32, 2: 25, 3: 32, 4: 29, 5: 26, 6: 28, 7: 38, 8: 32, 9: 52}
```

The rev9 package lived under `_bootstrap/` (`CG-1d`'s whole premise; the
acceptance record at `:4-5` names
`_bootstrap/rfc-phase/FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md`). The nine
clause-count ends that gate the entire corpus completeness check are therefore
**unverifiable from a clone** — the script's copy is the only accessible
statement of them. Correctly labelled "frozen facts" and honest about it; noted
because it is a tracked check depending on a git-excluded source, which is the
class the criterion asks about.

---

## G — Owner-gated registries in the wrong plane

### G-1 · P-22 is real, is correctly recorded, and one leg of it is a plain citation error nobody has named. **[Observed]**

The four clauses, quoted:

**RFC3-10** (`rfcs/RFC-0003/manifests-and-namespace.md:235-242`) — the
workspace manifest "living **outside every governed plane**… classified under
**VIS-6, exception (a)** — personal presentation state: it may never affect
truth, work, status, or certificates, and it is never a snapshot input
(RFC2-1)."

**RFC3-11** (`:244-249`) — "Its field set is **closed at SDR-29's list**: local
project membership…, grouping and ordering, saved cross-project views, and
owner-specific portfolio narrative/dashboard preferences. **Additions require
an amendment to this RFC.**"

**RFC3-21** (`:340-347`) — "**`.syzygy/local/` is personal presentation
state** — VIS-6, exception (a): layouts, filters, bookmarks, unpromoted
notes… The **only** path by which its content gains authority is promotion."

**RFC9-8(a)** (`rfcs/RFC-0009/semantic-geography.md:135-145`) — "SDR-29 and
RFC3-21 put its arrangement in the **workspace manifest**… so it carries the
**same machinery at workspace scope**: a **portfolio layout version** and its
registry, reorganisation events with recorded rationale, and the RFC9-16(d)
owner gate, all held in the workspace manifest's **governed space (RFC3-21)**".

**RFC10-15** (`rfcs/RFC-0010-mission-control-autonomy.md:357-374`) —
portfolio-level governance "lives in a typed, platform-level **workspace
governance store**, distinct from the presentation-only workspace manifest
(which remains personal presentation state, RFC 0003). The store's entries that
authorize anything are RFC3-16(a) artifacts… minting the store is an
authority-plane widening that requires an RFC3-15-style recorded owner
widening".

**Do they actually conflict? Yes, on three independent grounds.**

1. **Category error in terms.** RFC9-8(a) writes "the workspace manifest's
   **governed space**". RFC3-10 places the manifest "outside every governed
   plane". There is no such space; the phrase is self-contradictory against the
   clause that defines the object.
2. **Closed-field-set breach, mechanically checkable.** RFC3-11 closes the
   manifest at SDR-29's four items — membership, grouping/ordering, saved
   views, narrative/dashboard preferences (confirmed verbatim at
   `SURFACE-DECISION-RECORD.md:157-160`). RFC9-8(a) adds **three** more: a
   layout-version registry, reorganisation events with recorded rationale, and
   an owner gate. None is an SDR-29 item. RFC3-11 says additions "require an
   amendment to this RFC"; **no such amendment exists** in the corpus.
3. **An owner gate is authority-bearing by construction.** RFC9-16(d) is "an
   **owner governance act**" (`semantic-geography.md:472-474`), squarely inside
   RFC3-16(a)'s predicate ("authorizes a dangerous act… or otherwise binds
   project truth"). RFC3-10 says the manifest "may never affect truth, work,
   status, or certificates", and RFC3-16's own lifecycle table
   (`governance-homes-and-owner-acts.md:116`) gives `cache/`, `local/` the
   lifecycle "**none** — No governance lifecycle". RFC3-15(a) sets the exact
   precedent: `cache/` and `local/` were **barred** to identity-bearing
   snapshot inputs, and admitting a new home required an owner amendment.

**The leg nobody has named.** RFC9-8(a) cites **RFC3-21** twice for the
proposition that the arrangement lives in the workspace manifest's governed
space. **RFC3-21 is not about the workspace manifest.** It governs
`.syzygy/local/` — a per-project directory, a different object. RFC3-10/11 are
the clauses that govern the workspace manifest. So the citation is wrong on two
counts at once: wrong artifact, and the clause cited says the opposite of what
it is cited for (RFC3-21 is the strongest *anti*-authority clause in the
package). P-22's register entry says "RFC3-10/11/21 close as personal
presentation state" and does not distinguish them, so the miscitation is
currently invisible in the register too. It is also, separately, the cheapest
half of the fix.

**Smallest correction.** Two edits, no new clause:

1. In RFC9-8(a), move the portfolio layout version, its registry, the
   reorganisation events, and the RFC9-16(d) owner gate from "the workspace
   manifest's governed space" to **RFC10-15's workspace governance store**, and
   cite **RFC10-15 / RFC3-16(a)** instead of RFC3-21. RFC10-15 already exists,
   already carries the right authority semantics, and already names its own
   minting gate — the remedy is in the corpus, which is why P-22 says the
   corpus "contains both the error and its remedy".
2. Leave in the manifest only *grouping and ordering*, which SDR-29 and RFC3-11
   already allow as presentation.

That needs **no RFC3-11 amendment** — which the alternative repair (widening
the closed field set) would, and which would also have to overcome RFC3-10's
"may never affect truth". **[Inferred]** — this is my reading of the smallest
edit, not a ruling; P-22 correctly reserves the plane choice for the owner, and
I agree it should not be settled by editing whichever clause is younger.

### G-2 · Sweep for other authority-bearing registries in presentation or personal state. **[Observed]** — one instance, no others.

Method: Python `re` over all 237 tracked files for `registry`, `register`,
`owner gate`, `owner-gated`, `RFC3-16(a)`, cross-read against each named
home. Registries found and their planes:

| Registry | Home | Authority-bearing? | Verdict |
|---|---|---|---|
| **Portfolio layout version + registry, RFC9-8(a)** | **workspace manifest** (presentation) | **yes — RFC9-16(d) owner gate** | **the P-22 defect, G-1** |
| Layout version registry, RFC9-18 | `.syzygy/map/**` | yes — RFC3-16(a)-gated | correct plane |
| Channel registry, RFC9-26 | governed plane, module 2 | yes — RFC3-16(a)-gated | correct plane |
| Agent/Fleet profile registry | RFC11-10 profiles + RFC 0010 §8 q3 store; **deferred** | would be | not yet placed — no defect |
| `07-AUTONOMY-EXTENSION-REGISTER.md` | candidate package | **no** — `:39` "the register itself authorizes nothing" | correct |
| `TERM-REGISTRY.md` | `policy-candidates/` | no — CG-16 polices the claim over 41 mentions | correct |
| Substrate lock | `policies/` | record, never authority; CG-19 checks it | correct |
| `PENDING-OWNER-DECISIONS.md` | `decisions/` | register of open questions; `:92` "Nothing in this register is self-executing" | correct |

RFC-0009's README (`:118-128`) explicitly reasons about which registries
RFC3-16(a) gates and where they sit, and gets both right. **G-1 is the only
misplacement I found**, and it is already an open owner item.

---

# Summary of findings

| ID | Criterion | Severity | One line |
|---|---|---|---|
| **H-1** | H | **high** | 7 act digests — incl. all 4 in the owner-facing offering — falsifiable with a green battery and exit 0. Mutation-proven. |
| **A-1** | A | **high** | The contract-relation vocabulary disagrees with RFC11-4 in both directions, and puts a `constrains:` key no clause defines into 3 modules inside act 1's digest set. **Not repaired** by the in-flight work. |
| **E-1** | E | medium *(partly repaired mid-review)* | The relation model lived only in a generator + its output; its cited decision record was absent and **now exists, untracked** (correction recorded in full at E-1). Residual: CG-1b cannot see a dangling path reference inside a `.py` docstring. |
| **F-1** | F | **medium-high** | `§7.1`, `§7.3`, `§9.3`, `§9.4` exist in no charter; the default-load set and the 900–1,200 band live only in the checker and are printed as charter figures every run. |
| **F-2** | F | medium | The only ceiling waiver is a Python dict literal citing a report that does not contain it. |
| **C-1** | C, E | medium | `05-CONTRACT-INDEX.yaml`: no candidate marker, and `status_source` hard-coded rather than projected. |
| **D-1** | D | medium | CG-14's excluded-root guard drops `.syzygy/local/` and `.syzygy/cache/` — the prior round's defect class, recurring. Demonstrated. |
| **C-2** | C | medium | 11 of 62 candidate-lane artifacts unmarked; CG-4's denominator is 8. |
| **F-3** | F | medium | 11 rules with a second copy inside the enforcement, enumerated with lines. |
| **C-3** | C | low-medium | Registry claimed CG-17 enforcement; correction landed in the checker's comment, not the artifact. Being repaired in the working tree. |
| **F-4** | F | low-medium | CG-9 "duplicate authority homes absent" is a path-string tautology over 16 files. |
| **A-2 / A-3** | A | low | Budget figures in 4 places; the ceiling's "~" lost in derivation. |
| **E-2 / D-3** | E, D | low | Founder's HEAD sha and dirty flag written into a tracked generated artifact, never verified. |
| **D-2** | D | low | Default scope unions untracked working-tree files into every denominator. |
| **D-4** | D | low | `REV9_ENDS` sourced to a git-excluded rev9 artifact. |
| **G-1** | G | **already owner-tracked (P-22)** | Confirmed on three grounds; plus one unnamed leg — RFC9-8(a) cites RFC3-21, which governs a different object and says the opposite. |
| **G-2** | G | — | No second misplaced registry found, over 8 registries examined. |

**Counts.** 17 findings. 2 high, 1 medium-high, 6 medium (one partly repaired
mid-review), 5 low-to-low-medium, 1 confirmation of an existing owner item with
a new leg, 1 clean sweep. Criterion **B** produced **no findings** over 65 files
and 90 candidate lines — recorded as a pass, not as an absence of looking.

**On the moving target.** Three of the artifacts I reviewed were edited by a
parallel session during the review: `scripts/check_governance.py`,
`build_contract_index.py`, and `TERM-REGISTRY.md`; and
`RELATION-MODEL-DECISION.md` was created. I have marked every place this
changed a finding, corrected two claims that went stale under me (**E-1**, and
the `build_contract_index.py` line numbers), and re-verified every load-bearing
line citation against the working tree before submitting. The two **high**
findings and **F-1** were re-checked last and are unaffected. A verdict against
a tree that is being edited is a verdict about the reviewed commit
(`aee13d5`) plus the disclosed deltas, and not about whatever is committed
next.

---

*Reviewer note on scope discipline: I did not read any `round-2026-08c/`
artifact except `FINAL-CLOSURE-PREFLIGHT.md` (criterion H, digest copies) and
the directory listing (criterion E, to establish that
`RELATION-MODEL-DECISION.md` is absent). A `grep` for `constrains` incidentally
surfaced excerpt lines from a sibling reviewer's `RD-4` raw output; I did not
open that file and no conclusion here rests on it. I read no commit messages.*
