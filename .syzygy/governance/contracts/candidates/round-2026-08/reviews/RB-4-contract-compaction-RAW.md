# RB-4 — foundational contract and compaction (review vertical 4) — RAW report

**Reviewer:** fresh-context session, no authoring context. **Date:** 2026-08-05.
**Charge:** semantic preservation of this round's digest-set edits; clause
accounting; module structure; the RFC/OpenSpec boundary and the P-10 gap;
dependency-graph disclosure.

**Constraint honored:** nothing under `_bootstrap/` was read or opened. Every
claim below rests on clone-visible files plus the commands listed. Where a
baseline exists only in `_bootstrap/`, the limit is stated as `[Unknown]`
rather than papered over.

**Epistemic labels:** `[Observed]` = I ran the command / read the bytes.
`[Inferred]` = my judgment over observed material.

---

## 0. Provenance — commands run

All read-only. Run from
`/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/` unless noted.

```sh
# Scripted checks (all three, this session)
python3 scripts/verify_final_prespec.py
python3 scripts/build_contract_index.py --check
python3 scripts/build_dependency_index.py --check

# Manifest integrity + its own digest (the act-1 argument)
find rfcs -name '*.md' | sort | xargs sha256sum > /tmp/live.txt
diff <(grep -v '^#' ACTIVE-CONTRACT-MANIFEST.txt) /tmp/live.txt
sha256sum ACTIVE-CONTRACT-MANIFEST.txt

# Sibling-gate digests
sha256sum ../../../map/topology-candidates/BUNDLE-MANIFEST.md
sha256sum ../../../intent/OVERVIEW.md
grep -n "3858820f\|aa2d6353" ../../policies/craft-and-care/INSTALL-RECORD.md

# Clause census — Python `re`, definition-based, both corpora
#   CLAUSE_DEF  = ^\*\*(RFC\d+-\d+)(\([a-z]\))?\s*(?:\.|—|—)
#   LETTERED_LIMB = ^\*\*(RFC(\d+)-\d+)(\([a-z]\))\s   (same admission rule as
#   build_contract_index.py: limb counts as a definition only when its RFC
#   number matches the file's own contract and its parent is CLAUSE_DEF-defined)
# run over history/rev9-rfcs/ and rfcs/

# Mention-vs-definition census (to test whether the definition rule hides ids)
# Per-clause rev9→rev10 comparison for RFC-0006 (whitespace-normalized equality
#   over blocks delimited by ^\*\*RFC6-n)
# Sentence-level difflib over the 8 differing RFC-0006 clauses
# Cross-seam citation census for RFC-0007 (clause bodies only, terminated at
#   the next clause definition or the next ^## heading)
# depends_on/provides_to asymmetry recount from module front matter
# cited-contract vs declared-depends_on comparison, all 11 contracts
# per-module `wc -w` vs every figure in 06-CONTEXT-LOAD-MAP.md
# RFC2-24 / RFC2-25 table cell-by-cell diff, rev9 vs rev10
```

**Scripted-check output (read, not exit-code):**

- `verify_final_prespec.py` → `active corpus (RFC files): 99080 words across 32
  modules`; `numbered clauses defined: 322`; two justified notes (RFC-0001
  oversize; corpus over target band); `PASS — all checks clean`. `[Observed]`
- `build_contract_index.py --check` → `index matches regeneration — no drift`. `[Observed]`
- `build_dependency_index.py --check` → `dependency index matches regeneration —
  no drift`. `[Observed]`
- `ACTIVE-CONTRACT-MANIFEST.txt` reproduces byte-exactly against the live 32
  files — all 32 lines OK, zero mismatches. `[Observed]`
- `sha256(ACTIVE-CONTRACT-MANIFEST.txt)` =
  `5c4d6798354135bd860b3a2637c282f535c519bdd1a3cbab67d7555367af6caa`. `[Observed]`

---

## 1. Census numbers (charge item 2)

Independent Python `re` census, both corpora, definition-based:

| Measure | rev9 (`history/rev9-rfcs/`) | rev10 (`rfcs/`) |
|---|---|---|
| Numbered clause identities **defined** | **294** | **322** |
| Lettered sub-clause identities **defined** | **21** | **22** |
| Lost (present rev9, absent rev10) | — | **0** |
| Renumbered | — | **0** |

**Gained set, exhaustively:** `RFC10-1 … RFC10-16` (16), `RFC11-1 … RFC11-12`
(12), and `RFC3-16(c)` — **28 numbered + 1 lettered, nothing else**. `[Observed]`

This reproduces `COMPACTION-EQUIVALENCE-REPORT.md` §2 and
`04-CLAUSE-MIGRATION-MATRIX.md` change-log row 2 **exactly**, including the
corrected "1 new sub-clause, not 2" tally. The 04 head's global-tally sentence
("all 294 rev9 numbered clauses survive with identities unchanged — zero
merged, zero retired, zero renumbered, zero routed out; **1** new sub-clause")
matches my census with no discrepancy. **Agree.**

**Methodology cross-check.** A looser *mention*-based census (any `RFCn-m(x)`
token anywhere) yields rev9 = 294 numbered + 29 lettered, rev10 = 322 + 34. The
extra lettered tokens in both corpora are **in-body list items**, not clause
identities — the corpus says so itself at `rfcs/RFC-0008/README.md:58` ("RFC8-8(a)–(c)
— are *parts of that clause*, list items within one clause body") and
`rfcs/RFC-0008/identity-authority-materialization.md:342`. Rev9 carries 8 such
tokens (`RFC5-18(a)/(c)/(e)`, `RFC8-2(a)`, `RFC9-10(c)`, `RFC9-16(a)`,
`RFC9-19(b)/(c)`); rev10 carries those 8 plus 4 new descriptive ones
(`RFC4-8(c)`, `RFC7-2(a)`, `RFC7-9(a)`, `RFC8-8(a)`), all introduced in rev10
package READMEs and front-matter `clauses:` lines. **The definition-based rule
is the correct one and the report's numbers are right.** `[Observed]` I record
the mention-census here because a future reviewer running the naive sweep will
get 34, not 22, and should not read that as drift.

**Verdict on item 2: ACCEPT.** Census reproduced, zero lost, zero renumbered,
gained set exact, 04's tally rows and change log agree, all three scripts pass.

---

## 2. This round's digest-set edits (charge item 1)

### 2.1 What I could verify, and the one thing I could not

`.syzygy/governance/contracts/` is **untracked** (`git status` → `?? .syzygy/governance/contracts/`),
so git carries no pre-round baseline, and SD-7 places the only byte-baseline
inside `_bootstrap/`, which I am barred from. **There is therefore no
clone-visible way to diff rfcs/ against its own pre-round state.** `[Observed]`

I used two independent methods instead:

**Method A — word-count arithmetic (catches every length-changing edit).**
`COMPACTION-EQUIVALENCE-REPORT.md` §5 claims the corpus moved 99,067 → **99,080
w**, +13, all in `rfcs/RFC-0003/governance-homes-and-owner-acts.md` (4,401 →
4,414). The verifier prints 99,080 across 32 modules and 4,414 for that file.
`[Observed]` I then hand-counted the SD-1 edit itself:

- rev9 gate cell (`history/rev9-rfcs/RFC-0003-project-workspace-manifests.md:363`):
  "Owner acceptance (`ACCEPT FOUNDATIONAL RFCS` for the foundational set; owner
  sign-off per VIS-4 thereafter)" = **14 words**.
- rev10 gate cell (`rfcs/RFC-0003/governance-homes-and-owner-acts.md:87`):
  "Owner acceptance (for the foundational set, the digest-bound act defined by
  the active acceptance record — `ACCEPT COMPACTED FOUNDATIONAL RFCS: <manifest
  digest>`; owner sign-off per VIS-4 thereafter)" = **27 words**.
- Delta **+13**, exactly the corpus delta. `[Observed]`

**This bounds length-changing edits inside `rfcs/` this round to exactly one
file and exactly one cell.** `[Inferred]` It is the strongest independent
confirmation available without the baseline.

**Method B — length-neutral edits.** `Seven → Twelve` and the four RFC-0007
numerals are word-count-neutral, so Method A is blind to them and to any other
length-neutral edit. **Whether further length-neutral edits landed in `rfcs/`
this round is `[Unknown]` from a clone**, and no register asserts a method that
would have caught them. This is a real gap in the round's own evidence, recorded
as **F6**, not as a defect I can prove.

### 2.2 SD-1 — the RFC-0003 install-gate edit

**Landed, and complete.** `rfcs/RFC-0003/governance-homes-and-owner-acts.md:87`
now cites the digest-bound act. A `grep -F` sweep for the retired phrase over
tracked files finds **zero live uses inside `rfcs/`** — the surviving hits are
all statements *about* the retirement (`00-README.md:23`, `AGENTS.md`,
`10-EXIT-REPORT.md:114`, `TERM-MIGRATION-REPORT.md`), the frozen rev9 corpus,
`history/`, and stored reviews (correctly never edited). `[Observed]`

**Class label "Clarifying/corrective" — I agree.** The rev9 → rev10 cell diff
is confined to the gate column's mechanism reference. The `contracts/` row's
description column is byte-identical; no other row in the six-category table
changed; the "six-name category validator" sentence is intact; VIS-4 sign-off
"thereafter" is unchanged. **No obligation changes beyond the acceptance-mechanism
reference.** `[Observed]` If anything the edit is a mild strengthening (the act
now requires a digest argument), which is the fail-closed direction and does not
make the class label dishonest.

**One residual defect in the new text (F5, minor).** The cell now says "the
digest-bound act defined by **the active acceptance record**" and gives no path.
A reader inside RFC-0003 cannot resolve which record that is; and after act 1 the
contract's accepted home is `contracts/rfcs/` while the record it points at is
today a candidate at `contracts/candidates/`. The charter's own citation rule
("every cross-RFC citation must resolve after compaction") is met in letter — it
is not a clause citation — but not in spirit.

### 2.3 The RFC-0007 README edits

**Four numerals — verified internally consistent.** `rfcs/RFC-0007/README.md:45-48`
states index = 2,326; package union = 10,636; default path 7,493 / 5,469.
Live `wc -w`: narrative 5,167 · rendering 3,143 · README 2,326 →
5,167+3,143+2,326 = **10,636** ✓; 2,326+5,167 = **7,493** ✓; 2,326+3,143 =
**5,469** ✓. `[Observed]` `matrix-rows/RFC-0007-rows.md:22-23` now carries the
same figures with a dated correction note at line 132, and `06-CONTEXT-LOAD-MAP.md:20`
agrees. All four numerals are correct and the three files agree.

**Recording gap (F4).** These edits are **not** in
`round-2026-08/SEMANTIC-DELTAS-THIS-ROUND.md`, whose opening sentence is "Every
normative or authority-adjacent edit this round travels as a recorded delta."
They are recorded only in `04-CLAUSE-MIGRATION-MATRIX.md` change-log row 4. An
edit inside the act-1 digest set is authority-adjacent by construction — it
invalidated the manifest. See F4.

**Direct contradiction inside 04 (F3).** The change-log preamble
(`04-CLAUSE-MIGRATION-MATRIX.md:1050-1057`) states: *"Corrections to this file's
**accounting**, not to any clause text. **No contract module changed in this
batch**."* Row 4 of that same table states: *"The same stale figures were
corrected in `rfcs/RFC-0007/README.md` in the same batch."* `rfcs/RFC-0007/README.md`
**is** a contract module and **is** in the act-1 digest set. The preamble is
false about its own table. `[Observed]`

### 2.4 The `Seven → Twelve` cross-module edge count

**The claim, verified.** `rfcs/RFC-0007/README.md:65-71`: *"Twelve citation
edges cross it, all resolvable by the lookup rule above:"* followed by an
enumeration. Counting the enumerated items: module 1 → module 2 has **5**
(RFC7-6→30; RFC7-11/11(a)→33; RFC7-14→26; RFC7-17→26/33; RFC7-20/25→33);
module 2 → module 1 has **7** (RFC7-26→17; 27→2; 29→14/18/23; 30→6; 31/32→25;
33/34→5/11/11(a)/13; 36→2/3/7/11/11(a)). **5 + 7 = 12.** The stated figure
matches the enumeration exactly. `[Observed]` The prior "Seven" was wrong under
any counting; the correction direction is right.

**But the enumeration is not a census, and "edges" is the wrong noun (F7,
minor).** Machine census of clause bodies only (definition-delimited, cut at the
next `##` heading):

- **31 (source, target) pairs** across **18 source clauses** — not 12 by any
  edge-counting reading. Twelve is the count of *enumerated groupings*.
- Two source clauses are **absent from the enumeration entirely**:
  **`RFC7-5 → RFC7-28`** (the entity table's *Curated diagram* row at
  `rfcs/RFC-0007/narrative-contract.md:124` cites RFC7-28) and `RFC7-38 → RFC7-1`
  (a range endpoint, `RFC7-1…RFC7-37`, which I discount as not a navigational
  edge). `[Observed]`
- Four enumerated groups understate their targets: `RFC7-6` also cites RFC7-31
  (`narrative-contract.md:154`); `RFC7-29` also cites RFC7-2; `RFC7-31` also
  cites RFC7-3; `RFC7-33` also cites RFC7-3; `RFC7-36` also cites RFC7-5.

**Reader impact: low.** The README's own sentence — "all resolvable by the
lookup rule above" — is true regardless, and the lookup rule (`n ≤ 25` →
module 1) is total over RFC7-1…38, so nothing mis-navigates. The defect is that
a figure presented as exhaustive is not, in a corpus whose discipline is
"enumerate remainders instead of rounding."

### 2.5 Any other divergences the matrix + equivalence report do not account for?

Within the limits of §2.1: **none found by Method A.** Two accounting
divergences *are* present and are recorded below as F8 and F9 — a 6-vs-5 count
error in a disclosed imprecision, and an undisclosed seventh changed table cell.
Both are accounting, not obligation.

**Verdict on item 1: EXCEPTIONS** (F3, F4, F5, F6, F7 — none touching an
obligation).

---

## 3. Module structure (charge item 3)

**Pointer note.** The charge cites "charter §11.3". `grep -rn "11\.3"` over the
whole tree returns nothing; `COMPACTION-CHARTER.md` has named, unnumbered
sections. I reviewed against the charter's **"Tier rules → Tier 1"** list, which
is the requirement the charge describes: *scope + a short reader map;
definitions; every normative clause; closed vocabularies; state machines;
authority and lifecycle boundaries; integration obligations; failure, Unknown,
and degradation semantics; violation cases; explicit deferrals and open
defaults*, plus the **Metadata front matter** and **Status header** sections.

Six modules sampled (as charged), plus `rfcs/RFC-0003/README.md` as the package
equivalent:

| Module | Front matter | Status header | Scope / reader map | Definitions | Normative clauses | Authority boundary | Failure / Unknown | Integration | Violation cases | Deferrals | History link |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `RFC-0001-…-state-planes.md` | ✔ | ✔ | §1 (merged) | §3.2 tables | §3 | §3.4 | ✔ | §5 | §4 | §7 | ✔ |
| `RFC-0003/governance-homes-and-owner-acts.md` | ✔ (+`module:`) | ✔ | §0 | §1 tables | §1 | §1 (RFC3-16/16(a)) | ✔ | §3 | §2 | §4 | ✔ |
| `RFC-0006-…-query-drawer.md` | ✔ | ✔ | §0 + §1 | §3.1/§3.5 | §3 | §3.9 | §3.2 outcome set | §5 | §4 | §7 | ✔ |
| `RFC-0009/semantic-geography.md` | ✔ (+`module:`) | ✔ | §0 | §2 | §2–§6 | §1 | ✔ | §8 | §7 | §9 | ✔ |
| `RFC-0010-mission-control-autonomy.md` | ✔ | ✔ | §0 + §1 | §3 | §3 | §3.7 (RFC10-16) | ✔ | §5 | §4 | §7 | **✘ — see F10** |
| `RFC-0011-context-compiler.md` | ✔ | ✔ | §0 + §1 | §3 | §3 | §3.6 (RFC11-12) | ✔ | §5 | §4 | §7 | **✘ — see F10** |
| `RFC-0003/README.md` (pkg equiv.) | ✔ | n/a | ✔ | n/a | lookup rule | n/a | n/a | §"Package-spanning" | n/a | n/a | ✔ (`:119`) |

`[Observed]` Every sampled module carries the Tier-1 set. Two structural
observations:

**F10 (material).** `rfcs/RFC-0010-…:374` and `rfcs/RFC-0011-…:266` both head §6
**"Alternatives considered (summary — details in history)"**. `history/` contains
`RFC-0001-history.md … RFC-0009-history.md` and **no RFC-0010 or RFC-0011 history
file**. The pointer resolves to nothing. `verify_final_prespec.py`'s citation
check does not catch it because it is prose, not a link. `[Observed]`

**F11 (material).** Revision-process bookkeeping sits inside the act-1 digest
set. `rfcs/RFC-0009/README.md:200-215` carries a **"Word accounting (rev10
compaction)"** table (rev9 monolith 19,269 / modules 6,999 / 5,540 / 3,027 /
index 2,029 / "Net −19.2%"); `rfcs/RFC-0007/README.md:45-48`, `RFC-0002/README.md:49`,
`RFC-0004/README.md:50`, `RFC-0005/README.md:48` carry the same shape. I verified
the RFC-0009 figures are currently correct (`wc -w history/rev9-rfcs/RFC-0009-orrery-map-surface.md`
= 19,269 ✓; the three modules ✓). `[Observed]` The problem is not accuracy, it is
**location**: recomputable measurement figures inside digest-bound normative
modules mean any recount forces a digest-invalidating edit. That is exactly what
happened this round — 04 change-log row 4 is the RFC-0007 instance, and it is
one of the two edits that killed the act-1 digest. The generated home for these
figures already exists (`06-CONTEXT-LOAD-MAP.md`, which I verified is
byte-current for all 32 modules).

**Leakage check — revision narrative / reviewer transcript in active modules.**
Swept `rfcs/` for `rev7|rev8|rev9|rev10|reviewer|_bootstrap|fresh-context|§20|adversarial`.
`[Observed]`

- **No reviewer-transcript material, no `_bootstrap/` path citations, no `§20`
  references** anywhere in `rfcs/`. The charter's "do not cite `_bootstrap/`
  paths in active normative text" rule is clean.
- Provenance-shaped rev-references remain and are **charter-permitted** (owner
  decisions must not disappear): e.g. `RFC-0003/governance-homes:224` ("decision
  **A1**, reaffirmed at the rev8 rework"), `RFC-0006:341` ("Renamed from
  `Current` at the rev7 rework, semantics unchanged — see history"),
  `RFC-0008/accounting…:376`.
- **One borderline case (F12, minor):** `rfcs/RFC-0002/reconciliation-chain.md:295`
  — "the `gate-backed` route (RFC4-13 route 4), which **at the rev7 rework**
  additionally…" — carries amendment narrative inside clause text with no
  decision identifier attached, which Tier 2 sends to history. Single instance;
  no obligation affected.

**Verdict on item 3: EXCEPTIONS** (F10, F11, F12).

---

## 4. RFC-versus-OpenSpec boundary — the P-10 gap (charge item 4)

### 4.1 The charge's premise is wrong, and the way it is wrong *is* the finding

**F2 (material, and the substance of P-10).** The charge — and
`decisions/PENDING-OWNER-DECISIONS.md:39` (P-10), and
`round-2026-08/PUBLIC-CLONE-AUTHORITY-MATRIX.md:28` ("RFC/OpenSpec routing
matrix (matrix-rows, 28 RFC-0006 rows)") — describe
`matrix-rows/RFC-0006-rows.md` as holding 28 **routing** rows carrying markings
of the class *future OpenSpec requirement / structural invariant with reviewed
N/A / craft policy / informative*.

**It does not.** `[Observed]` `matrix-rows/RFC-0006-rows.md` is a **rev9→rev10
clause-migration** matrix. Its 28 clause rows carry outcomes from the migration
vocabulary (`retained unchanged` · `retained with wording sharpened`), plus 4
`q<n>` rows. It contains no routing class, no `spec/` domain, and no N/A
judgment. Neither does anything else in the package.

The routing matrix is `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md`, and it
**explicitly excludes RFC-0006** (`:234-237`):

> *"This matrix routes RFC 0007–0009 and RFC-0010/0011; **RFC 0006's
> clause-level routing (including its `spec/selection-api` material) is a
> surface-specification deliverable under RFC6-28's coverage matrix, not
> re-enumerated here.**"*

and its coverage skeleton at `:305` carries one placeholder row: `| spec/selection-api
| RFC 0006 clause routing — deliverable of RFC6-28's coverage matrix |`.

**So the P-10 gap is larger and different than P-10 says.** It is not "28
routing rows exist but were never reviewed." It is: **RFC-0006 — by the routing
matrix's own account the most directly user-observable cross-surface contract —
has no clause-level routing classification anywhere in the package, and the
register that tracks the gap misidentifies a migration matrix as the missing
artifact.** An owner reading P-10 would believe the classification exists and
needs review; it does not exist. The deferral itself is defensible (RFC6-28 does
require that matrix at surface specification, and the routing matrix says so in
terms) — **the misdescription is not**.

### 4.2 What I did instead: full 28-row verdict table

Because the routing markings do not exist, each row below carries **two**
verdicts, so the table is usable either way:

- **Migration verdict** — agree/disagree with the migration outcome actually on
  the row in `matrix-rows/RFC-0006-rows.md`, tested mechanically.
- **Routing class (mine)** — the class I would assign under
  `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md`'s five-class scheme (DI · OS · DI+OS ·
  CR · IR), so the P-10 gap is closable from this report rather than reopened.

**Mechanical basis for the migration verdicts** `[Observed]`: whitespace-normalized
per-clause comparison of `history/rev9-rfcs/RFC-0006-…md` against
`rfcs/RFC-0006-…md`, blocks delimited by `^\*\*RFC6-n`. Result: **20 clauses
byte-identical, 8 differing** — differing set = {RFC6-2, 4, 8, 14, 17, 19, 24,
28}. The matrix marks **exactly those 8** `retained with wording sharpened` and
**exactly the other 20** `retained unchanged`. **Perfect correspondence, zero
mismatches.** I then read the sentence-level diff of all 8.

| # | Clause | Migration outcome on row | Migration verdict | Routing class (mine) | Note |
|---|---|---|---|---|---|
| 1 | RFC6-1 | retained unchanged | **agree** | **DI** | Byte-identical. "No surface-local handle is ever a selection identity" is a conforming-implementation invariant; wire shape is §7-deferred |
| 2 | RFC6-2 | retained w/ sharpened | **agree** | **DI + OS** → `spec/selection-api` | Only loss: the SC-1 refinement parenthetical, verbatim at `history/RFC-0006-history.md` §RFC6-2. Retained DI: selection targets the durable identity level (SDR-2). OS limb: "every V0-core entity is selectable" is enumerable per entity |
| 3 | RFC6-3 | retained unchanged | **agree** | **DI + OS** | Byte-identical. Skew *rendering* is user-observable → OS limb; identical-resolution-in-all-surfaces is DI |
| 4 | RFC6-4 | retained w/ sharpened | **agree** | **DI + OS** | Sole change: "but each answer says which evaluation answered" → "always naming which evaluation answered". Identical obligation. Stamped-answer content is requirement material |
| 5 | RFC6-5 | retained unchanged | **agree** | **DI + OS** | Byte-identical incl. all 9 outcome rows and their obligations. **The single most OpenSpec-shaped clause in the RFC** — 9 outcomes × per-outcome obligations = the core of `spec/selection-api`. Retained DI: totality + "absence of a projection is never rendered as absence of the thing" |
| 6 | RFC6-6 | retained unchanged | **agree** | **DI** | Byte-identical, `[Inferred]` label intact. Pure vocabulary-hygiene invariant; nothing independently testable as behavior |
| 7 | RFC6-7 | retained unchanged | **agree** | **DI (+ CR limb)** | Byte-identical. Determinism is DI; *demonstrating* determinism is a release-gate/test obligation → craft |
| 8 | RFC6-8 | retained w/ sharpened | **agree** | **DI + OS** | Sole change: "unbound **here**" → "unbound" (one word). Row says "one word cut" — exact. DI: the four identity-bearing components + hint-neutrality. OS: actual URL grammar at spec time |
| 9 | RFC6-9 | retained unchanged | **agree** | **DI (+ CR limb)** | Byte-identical. Rename-stability is a mechanically testable invariant |
| 10 | RFC6-10 | retained unchanged | **agree** | **DI + OS** | Byte-identical. "The rendering must make which-one-this-is visible" is observable → OS limb |
| 11 | RFC6-11 | retained unchanged | **agree** | **DI + OS** | Byte-identical incl. never-404 / never-silent-redirect and the governance-event reasoning. Retirement rendering + successor offering is squarely OpenSpec material; the prohibitions stay DI |
| 12 | RFC6-12 | retained unchanged | **agree** | **DI** | Byte-identical |
| 13 | RFC6-13 | retained unchanged | **agree** | **DI** | Byte-identical. Bidirectional SDR-27 parity is the invariant the whole machine plane rests on; cited by RFC-0010/0011 as the row says |
| 14 | RFC6-14 | retained w/ sharpened | **agree** | **DI + OS** | Loses one closing justification ("…exactly the divergence RFC6-13 forbids"), present verbatim at `history/RFC-0006-history.md:60`. Every vocabulary element retained: label, tier (RFC2-25), Unknown reason (RFC2-24), freshness (RFC2-10), the three sibling surface states, `challenge-pending` and its travels-beside rule. Row's "one justifying clause moved" is exact. Field-level answer content → OS |
| 15 | RFC6-15 | retained unchanged | **agree** | **DI + OS** | Byte-identical. Envelope field |
| 16 | RFC6-16 | retained unchanged | **agree** | **DI + OS** | Byte-identical. Envelope field |
| 17 | RFC6-17 | retained w/ sharpened | **agree, with one note** | **DI + OS** | All six RFC2-25 tiers enumerated verbatim, sibling states retained, expandability retained, "all six … not a subset" made *more* explicit. Dropped: the "previously omitted" narrative (at history §RFC6-17) and the "Unknown ×40" example. **Note:** rev9's trailing clause "…which is exactly where doctrine requires staleness to stay visible on the primary surface rather than in drill-down" is dropped; the obligation survives at RFC6-24's Historical bullet, so nothing is lost — but the row does not mention it |
| 18 | RFC6-18 | retained unchanged | **agree** | **DI** | Byte-identical incl. "kernel defect, not a UI inconsistency" |
| 19 | RFC6-19 | retained w/ sharpened | **agree** | **DI + OS** | All 7 content classes intact; class 6's `submitted`/`admitted` distinction and the `challenge-pending`-suspends-nothing rule retained at identical strength; the two dropped rationale tails are at history §RFC6-19 (`:97`). Drawer content is the canonical OpenSpec surface |
| 20 | RFC6-20 | retained unchanged | **agree** | **DI (+ CR limb)** | Byte-identical. Trust-floor invariant; link-integrity *cadence* is craft (the routing matrix already routes RFC-0007's analogue that way) |
| 21 | RFC6-21 | retained unchanged | **agree** | **DI + OS** | Byte-identical, `[Inferred]` label intact |
| 22 | RFC6-22 | retained unchanged | **agree** | **DI** | Byte-identical. Closed tuple = definitional |
| 23 | RFC6-23 | retained unchanged | **agree** | **DI + CR** | Byte-identical. "**release-blocking** under the trust floor" is a release-gate obligation → the CR limb is real and unrouted anywhere today |
| 24 | RFC6-24 | retained w/ sharpened | **agree** | **DI + OS** | Three scenario contexts intact; non-default-revision marker intact; the kernel's **refusal** to union incompatible proposals and `incompatible-scenario` intact; D1's map scope intact. Dropped: the rev7 rename narrative (history §RFC6-24) and "(ghost steps, milestone scenes, timeline scrubbing)". Row's account is exact |
| 25 | RFC6-25 | retained unchanged | **agree** | **DI** | Byte-identical |
| 26 | RFC6-26 | retained unchanged | **agree** | **DI + OS** | Byte-identical. Policy-not-error rendering + resolution route is observable |
| 27 | RFC6-27 | retained unchanged | **agree** | **DI + OS** | Byte-identical incl. "unclassifiable fails closed" and the SEC-5 gravity sentence. Security invariant DI; excluded-with-count rendering OS |
| 28 | RFC6-28 | retained w/ sharpened | **agree** | **DI (phase rule)** | Clause text **byte-identical** to rev9 apart from the removed `*(History: added at the rev8 rework…)*` parenthetical, which is at history §RFC6-28. Row's "only its origin note moved" is exactly right |

**Disagreements: 0 of 28.** Every migration marking is defensible against the
clause text I read. `[Observed]`

**§4 violation-case edits are unaccounted (F13, minor).** Comparing rev9 §4 to
rev10 §4: case 8 drops "membership" ("a freshness state or a **membership**
count" → "a … count"); case 9 drops "in answer to one selection"; case 10 drops
"(deriving from excluded content)". The row file's "Non-clause material moved"
paragraph lists §0, §1, the §5 defect narrative and §6 — **not §4**. No
obligation is lost (case 8 widens if anything; case 10's parenthetical survives
as RFC6-27's own sentence), but three edited cases carry no accounting row.

### 4.3 Spot-checks across the other matrix-rows files (6 charged)

| # | Row checked | Claim tested | Result |
|---|---|---|---|
| 1 | RFC2-13 (`04:138`) | VIS-7 exemption survived a near-loss | **CONFIRMED** — present in `rfcs/` |
| 2 | RFC2-18 (`04:143`) | "never as two independent aggregates" restored | **CONFIRMED** — verbatim in `rfcs/` |
| 3 | RFC7-20 (03 report) | `dismissed-by-decision` enumeration restored | **CONFIRMED** — both spellings present |
| 4 | RFC8-25 (`04`, equiv. §3) | rev9 fallback retired, B13 rule in its place, dropped text verbatim in history | **CONFIRMED** — "Where no threshold is declared, no mutation inherits" present in `rfcs/`, absent from `history/`; "the coverage test above is the operative limit" absent from `rfcs/`, present in `history/`. Exactly as disclosed |
| 5 | RFC2-24 (`04:149`) | "Twelve-row table **copied verbatim** in Condition and Resolution-route columns" | **DISAGREE — see F8.** Cell-by-cell diff of the 12-reason table: **6** Resolution-route cells differ (reasons #3, #6, #9, #10, #11, #12), all shedding `*Added:*`/`*Renamed:*` narrative. The Condition column is verbatim. `COMPACTION-EQUIVALENCE-REPORT.md` §6 discloses this as "**five** Resolution-route cells" — the true count is **six** |
| 6 | RFC2-25 tier table (adjacent to RFC2-24) | — | **F9.** The `asserted-by-worker` row sheds "**(per T-F9/R-11 disposition)**" — a review-disposition provenance pointer, a different class from the amendment narratives, disclosed on no row I could find |

### 4.4 The six phase-rule clauses

All six read and confirmed to state that user-observable behavior routes through
OpenSpec before implementation `[Observed]`:

| Clause | Location | States the rule? | N/A limb | "matrix is review material, never authority" |
|---|---|---|---|---|
| RFC6-28 | `RFC-0006-…:387` | ✔ | "explicit, reviewed N/A judgment" | ✔ |
| RFC7-38 | `RFC-0007/rendering-and-surface.md:306` | ✔ | same | ✔ |
| RFC8-32 | `RFC-0008/accounting-…:269` | ✔ | same | ✔ |
| RFC9-52 | `RFC-0009/interaction-parity-…:284` | ✔ | same | ✔ |
| RFC10-16 | `RFC-0010-…:316` | ✔ (incl. CLI, API endpoints, MCP-or-equivalent tools) | **stricter**: "proving it purely structural with no independently testable behavior" | ✔ |
| RFC11-12 | `RFC-0011-…:213` | ✔ | **stricter**, same wording | ✔ |

Boundary-review **E4**'s queued fix landed: the "review material, never
authority" limb is present in RFC10-16 and RFC11-12. `[Observed]`

**F14 (minor).** All six carry a "(Shape-parallel with …)" parenthetical, but
RFC10-16/RFC11-12 differ from the four surface clauses on the N/A limb (stricter
— deliberately, per E4's disposition "keep the stricter N/A limb") and on
headline form: the four surface clauses open `**RFC6-28 — This contract
schedules nothing.**`, the two new ones open `**RFC10-16.**` with no title.
E4 already flagged "'shape-parallel' overstated"; the limb was restored but the
overstated claim was left standing.

**Verdict on item 4: EXCEPTIONS** (F2 blocking-adjacent-material, F8, F9, F13,
F14). The 28 migration rows themselves: **ACCEPT, 0 disagreements.**

---

## 5. Dependency graph (charge item 5)

**The 20-edge disclosure is accurate.** I recomputed asymmetries directly from
module front matter with my own script: **20**, matching
`CONTRACT-DEPENDENCY-INDEX.md:82` exactly. `[Observed]` Five verified by hand
against the front-matter rows:

| # | Edge | Verified |
|---|---|---|
| 1 | `RFC-0002 → RFC-0003` (depends_on) | ✔ RFC-0003's `provides_to` = 0004,0005,0006,0007,0008,0009,0010,0011 — no 0002 |
| 2 | `RFC-0002 → RFC-0004` (depends_on) | ✔ RFC-0004's `provides_to` = 0003,0005,0008,0009,0011 — no 0002 |
| 3 | `RFC-0003 → RFC-0006` (provides_to) | ✔ RFC-0006's `depends_on` = 0001,0002 only |
| 4 | `RFC-0006 → RFC-0011` (provides_to) | ✔ RFC-0011's `depends_on` = 0001,0002,0003,0004,0005,0010 — no 0006 |
| 5 | `RFC-0009 → RFC-0010` (provides_to) | ✔ RFC-0010's `depends_on` = 0001,0002,0003,0005,0006,0008 — no 0009 |

The file's stance — *reported, not repaired*, because "adding the missing half
would be inventing an edge no module declares" — is **correct and I endorse
it**. The generator reads, never infers (`:9-10`), consistent with RFC11-7.

**Would a reader mis-navigate on any of the 20? No.** `[Inferred]` Both halves
are printed side by side in the same table, the file says the modules win, and
the graph is documented as a reference graph, not a build order. A reader
following either half lands on a real contract.

**But there is a second, undisclosed asymmetry class that *does* mis-navigate
— F15 (material).** `depends_on` is not just asymmetric against `provides_to`;
it is **incomplete against the modules' own clause text**. Comparing every
contract's cross-contract clause citations to its declared `depends_on`
`[Observed]`:

| Contract | Cites clauses of | but `depends_on` omits |
|---|---|---|
| RFC-0001 | 0002, 0003, 0004, 0005, 0006, 0009 | **all six** (declares none) |
| RFC-0002 | … 0006, 0007 | 0006, 0007 |
| RFC-0003 | … 0004…0010 | 0004, 0005, 0006, 0007, 0008, 0009, 0010 |
| RFC-0004 | … 0008 | 0008 |
| **RFC-0006** | 0003, **0009** | 0003, **0009** |
| RFC-0007 | … 0009 | 0009 |
| RFC-0008 | … 0007, 0009 | 0007, 0009 |
| RFC-0009 | … 0007 | 0007 |
| RFC-0010 | … 0007, 0009 | 0007, 0009 |
| **RFC-0011** | 0006, 0007, 0008, 0009 | **all four** |

The concrete case: `rfcs/RFC-0006-…:340` and `:359` cite **RFC9-14** and
**RFC9-41** inside RFC6-24's clause body, and `:496` again in §7 — yet
RFC-0006 declares `depends_on: [RFC-0001, RFC-0002]`. A selector building a
mandatory packet from `depends_on` (which is what `06-CONTEXT-LOAD-MAP.md`
§"Rules the map rides on" says RFC11-4 does — "mandatory selection is
deterministic from the index metadata + warrant") produces a packet in which
RFC9-41 does not resolve. Under **RFC11-6** that is "incomplete → Unknown →
blocks", so the system fails closed rather than silently — but the packet is
wrong, and nothing discloses that `depends_on` under-declares.

The mirror also exists, less seriously: `RFC-0008` declares `RFC-0005`,
`RFC-0010` declares `RFC-0001`, and `RFC-0011` declares `RFC-0001`, `RFC-0002`,
`RFC-0004` without citing a single clause of them — over-selection, which
RFC11-5's "suggestion never suppresses" tolerates.

**Verdict on item 5: EXCEPTIONS.** The 20-edge disclosure is accurate and its
findings-not-repairs stance is right (**ACCEPT** on what it claims); F15 is a
distinct, undisclosed defect class the file does not cover and does not claim to.

---

## 6. Findings

### F1 — BLOCKING. The acceptance record offers a retired digest for act 1 (and acts 2, 3, 4)

`AGENTS.md` names the acceptance record as "the single owning record for exact
phrases, digests, and ceremony." `SEMANTIC-DELTAS-THIS-ROUND.md` SD-1 states the
consequence of its own edit: *"**Impact:** invalidates the prior act-1 manifest
digest `08793ddf…` → manifest regenerated."* The manifest **was** regenerated —
it reproduces byte-exactly against the 32 live files, and its own sha256 is now
`5c4d6798354135bd860b3a2637c282f535c519bdd1a3cbab67d7555367af6caa`. `[Observed]`

**The record was not updated.**
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15` still reads:

> `| 1 | ACCEPT COMPACTED FOUNDATIONAL RFCS: 08793ddf70f3c2a30b5dcec51cac9266a81d03e9db48aa8b7071953f7687c936 |`

repeated at `:118` (§3), `:213` and `:215`. §3 even states the invariant it
violates: *"The phrase in §1 always carries the current manifest digest."*
It does not.

**All four digest-bearing gates are stale in that record** `[Observed]`:

| Act | Record states | Live value | Source of the live value |
|---|---|---|---|
| 1 | `08793ddf…7c936` | **`5c4d6798…6caa`** | `sha256sum ACTIVE-CONTRACT-MANIFEST.txt` |
| 2 | `CC-TEST-2@aa2d6353…b52821` | **`CC-TEST-2@3858820f…cb26d`** | `craft-and-care/INSTALL-RECORD.md:68,72` — which at `:74` states in terms that "the `CC-TEST-2@aa2d6353…` argument is **stale and satisfies nothing**" |
| 3 | `0d34d1b5…d61560` | **`89279260…1ef9`** | `sha256sum .syzygy/map/topology-candidates/BUNDLE-MANIFEST.md`; SD-2 says the prior digest is invalidated |
| 4 | `42de2eb1…24f240` | **`49a1a09c…61fa`** | `sha256sum .syzygy/intent/OVERVIEW.md` (working tree; the file is modified, 162+/172−) |

Also stale in the same record: §1 act-3 says the bundle "is shipped in this
packet at `topology/`" — `candidates/topology/` **does not exist** (the bundle
moved to `.syzygy/map/topology-candidates/` under SD-7). §3's retention
paragraph still says the package "lives in the deliberately git-excluded
`_bootstrap/` working tree", also superseded by SD-7. `[Observed]`

**Why blocking:** an owner performing act 1 today by copying the phrase from the
owning record binds a digest that matches nothing in the tree. The record's own
rule (§3: "only edits to the 32 modules invalidate the digest") was correctly
stated and then not applied to the two edits that landed in `rfcs/` this round.

**Corroboration:** the act-1 half was independently found by
`round-2026-08/reviews/RB-1-fresh-engineer-RAW.md:65,77` this round. Acts 2, 3
and 4 and the two dangling location statements I do not see reported there.

**Fix:** regenerate all four phrases in the record from live sources by script;
re-state §1 act-3's bundle location; re-state §3's retention paragraph.
Digest-stable for `rfcs/` — no contract module needs to change.

### F2 — MATERIAL. The P-10 gap is misdescribed, and RFC-0006 has no routing classification at all

Detail at §4.1. `matrix-rows/RFC-0006-rows.md` is a migration matrix; the routing
matrix (`SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:234-237`) explicitly excludes
RFC-0006. P-10 (`decisions/PENDING-OWNER-DECISIONS.md:39`) and
`PUBLIC-CLONE-AUTHORITY-MATRIX.md:28` both present a nonexistent artifact as
existing-but-unreviewed. An owner asked to "commission further review, or accept
them explicitly as unreviewed drafts" cannot do either, because the thing has not
been drafted. **Fix:** restate P-10 as *"RFC-0006's clause-level routing does not
exist and is deferred to RFC6-28's coverage matrix at surface specification —
accept the deferral, or commission the classification now"*; correct the
authority-matrix row. §4.2 of this report supplies a first-pass classification
for all 28 clauses if the owner chooses the latter.

### F3 — MATERIAL. `04`'s change-log preamble contradicts its own row 4

`04-CLAUSE-MIGRATION-MATRIX.md:1050-1057` asserts "**No contract module changed
in this batch**"; row 4 of the same table records the correction of
`rfcs/RFC-0007/README.md`, which is a contract module in the act-1 digest set.
The false sentence is exactly the one a reader would use to decide whether the
manifest needed regenerating.

### F4 — MATERIAL. Two rfcs/ edits bypass the semantic-delta register

`SEMANTIC-DELTAS-THIS-ROUND.md` opens "Every normative or authority-adjacent
edit this round travels as a recorded delta" and contains **no** entry for the
RFC-0007 README edits, which are recorded only in 04's change log. An edit that
invalidates the act-1 digest is authority-adjacent by construction. Either add
SD entries, or narrow the register's opening claim to what it actually covers.

### F5 — MINOR. SD-1's replacement text points at an unlocated record

`rfcs/RFC-0003/governance-homes-and-owner-acts.md:87` — "the digest-bound act
defined by **the active acceptance record**", no path, and the record it means
lives outside the accepted home the row will occupy after act 1. Detail at §2.2.

### F6 — MINOR (evidence gap, not a defect). No clone-visible baseline for length-neutral edits

Detail at §2.1. `rfcs/` is untracked and the byte-baseline is `_bootstrap/`-only,
so "exactly three content edits this round" cannot be verified from a clone for
edits that do not change word count. Method A bounds *length-changing* edits to
one file, one cell. A per-file digest snapshot committed before each round's
edits would close this permanently.

### F7 — MINOR. "Twelve citation edges" is a count of enumerated groups, and the enumeration is not exhaustive

Detail at §2.4. Twelve is correct as a count of listed items; the true clause-body
census is 31 (source, target) pairs across 18 source clauses, and `RFC7-5 →
RFC7-28` is missing from the list entirely. No mis-navigation (the lookup rule is
total), but a figure presented as a census is not one.

### F8 — MINOR. Disclosed-imprecision count is off by one: six RFC2-24 cells changed, not five

Detail at §4.3 row 5. `COMPACTION-EQUIVALENCE-REPORT.md` §6 says "five
Resolution-route cells"; cell-by-cell diff gives **six** (reasons #3, #6, #9,
#10, #11, #12). Also: `04:149`'s "copied verbatim in Condition **and
Resolution-route** columns" is true of the Condition column and false of six
Resolution-route cells.

### F9 — MINOR. A seventh changed table cell is disclosed nowhere

The RFC2-25 tier table's `asserted-by-worker` row sheds "(per T-F9/R-11
disposition)" — a review-disposition pointer, not an amendment narrative, so it
falls outside 04's stated "per-cell `*Added:*` / `*Renamed:*` narratives moved
to history" account.

### F10 — MATERIAL. RFC-0010 and RFC-0011 point at history files that do not exist

`rfcs/RFC-0010-…:374` and `rfcs/RFC-0011-…:266` head §6 "Alternatives considered
(**summary — details in history**)". `history/` holds RFC-0001…0009 only. Either
create the two history files or reword the headings — but note that rewording is
an `rfcs/` edit, so it must be batched with any other digest-set fix (see F1)
and cannot be done after the manifest is re-bound.

### F11 — MATERIAL. Recomputable measurement figures live inside the digest-bound modules

Detail at §3, F11. Package READMEs carry word-accounting tables (`RFC-0009/README.md:200-215`
is the largest). Their presence is why a routine recount forced an `rfcs/` edit
this round and killed the act-1 digest. The correct home already exists and is
byte-current: I verified **all 32** module figures in `06-CONTEXT-LOAD-MAP.md`
against live `wc -w` — every one matches. **Recommendation:** move the accounting
out of the digest set in the same batch as F10, so the digest set contains only
material that changes when an *obligation* changes.

### F12 — MINOR. One amendment narrative left in clause text

`rfcs/RFC-0002/reconciliation-chain.md:295` — "which **at the rev7 rework**
additionally…" with no decision identifier attached. Tier 2 material by the
charter's rule; single instance; no obligation affected.

### F13 — MINOR. RFC-0006 §4 violation-case edits carry no accounting row

Detail at §4.2. Cases 8, 9 and 10 were word-edited; the row file's "Non-clause
material moved" paragraph lists §0, §1, §5 and §6 only. No obligation lost.

### F14 — MINOR. "Shape-parallel" still overstated on RFC10-16 / RFC11-12

Detail at §4.4. Boundary-review E4 flagged this; the limbs were restored but the
claim was not qualified, and the two clauses also differ in headline form.

### F15 — MATERIAL. `depends_on` under-declares against the modules' own citations, and nothing discloses it

Detail at §5. Ten of eleven contracts cite clauses of contracts they do not
declare; RFC-0006 cites RFC9-14/RFC9-41 in clause text while declaring only
RFC-0001/0002, and RFC-0011 declares none of the four contracts it cites. The
dependency index's disclosure covers declaration-vs-declaration asymmetry only —
correctly, per its stated scope — so this class is invisible. Under RFC11-6 the
consequence fails closed rather than silently, which is why this is material
rather than blocking. **Fix (front-matter only, no clause text):** complete
`depends_on` from the citation census, or add a disclosure section to the
dependency index naming this class as a known, unrepaired divergence.

### Stale-disclosure cleanups (sub-minor, grouped)

Three statements are now false because the thing they say was not done, **was**
done `[Observed]`:

- `04`'s change-log "Not corrected here" list names "the identical stale
  RFC-0007 word-count table in `matrix-rows/RFC-0007-rows.md`" — it **was**
  corrected (`matrix-rows/RFC-0007-rows.md:22-23`, with a dated note at `:132`).
- The same list names "`06-CONTEXT-LOAD-MAP.md`'s RFC-0003 governance-homes
  figure" — it is **current** (4,414, matching live).
- `COMPACTION-EQUIVALENCE-REPORT.md` §5 says "one `06-CONTEXT-LOAD-MAP.md`
  module figure [is] stale" — **no** figure in that file is stale; I checked all 32.
- `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:264-281` (§7 item 10, "R1")
  presents the RFC-0007 stale-count as a live owner choice — "accept as-is …, or
  direct a fix + digest regeneration" — when the fix **was** applied and the
  digest **was** regenerated. The owner is being offered a decision already taken.

---

## 7. What I checked and found clean

Recorded so a later reader knows the negative results are real, not unexamined:

- All three scripts pass on output, not exit code. `[Observed]`
- Manifest ↔ live files: 32/32 byte-exact. `[Observed]`
- Clause census: 294→322 / 21→22, zero lost, zero renumbered, gained set exact. `[Observed]`
- RFC-0006: 28/28 migration rows correct; 20 byte-identical / 8 sharpened,
  matching the row outcomes exactly; every "moved to history" claim resolves to
  real text in `history/RFC-0006-history.md`. `[Observed]`
- All six phase-rule clauses present, all six state the OpenSpec-before-implementation
  rule, all six carry "review material, never authority". `[Observed]`
- Three named near-losses (RFC2-13 VIS-7 exemption, RFC2-18's "never as two
  independent aggregates", RFC7-20's `dismissed-by-decision`) all present. `[Observed]`
- RFC8-25's disclosed semantic resolution is exactly as described: rev9 fallback
  gone from `rfcs/`, present in `history/`; B13's stricter rule in place. `[Observed]`
- No reviewer-transcript material, no `_bootstrap/` path citations, no `§20`
  references anywhere in `rfcs/`. `[Observed]`
- 20 dependency asymmetries: recomputed independently, count exact, 5 hand-verified. `[Observed]`
- All 32 module word figures in `06-CONTEXT-LOAD-MAP.md` match live `wc -w`. `[Observed]`

**What this report does not establish.** Obligation-level preservation
corpus-wide — same limit `COMPACTION-EQUIVALENCE-REPORT.md` §6 states about
itself. My obligation-level reading is exhaustive for **RFC-0006** (all 28
clauses, sentence-level) and sampled elsewhere (6 spot-checks + the 5 structure
modules). Anything stronger is `[Unknown]`.

---

## Final verdict

The contract corpus itself is in good order: the census is exact, the RFC-0006
migration rows survive an exhaustive mechanical audit with **zero**
disagreements, the phase-rule spine is complete, and all three scripts pass on
their output. Every finding below blocking is in the **accounting and ceremony
records that wrap the corpus**, not in the clauses — with one exception (F1),
which makes the act-1 phrase unexecutable as written and is fixable without
touching a single contract module.

**EXCEPTIONS**
