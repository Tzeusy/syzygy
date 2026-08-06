# RD-8 — Final exact-manifest semantic confirmation

**Subject commit:** a7b3375
**Commissioned:** 2026-08-07, independent, no authoring context.

# VERDICT
VERDICT: REVISE

---

## Scope note on commit drift, stated before anything else

[Observed] The repository moved under this review. Commissioned at `a7b3375`;
`git log --oneline -1` during the review returned `c70540e`. `git diff
--name-only a7b3375 HEAD` over every subject path — `rfcs/`,
`ACTIVE-CONTRACT-MANIFEST.txt`, `topology-candidates/`, `OVERVIEW.md`,
`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`, `craft-and-care/`,
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`,
`round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md` — returns **empty**. The
three files that moved are `round-2026-08c/SOURCE-OF-TRUTH-CLOSURE-REPORT.md`
(new), `decisions/PROCESS-LESSONS.md`, and `PROJECT-STATUS.md`.

**Every finding below therefore holds at both commits**, with one exception
flagged inline: finding S1's corroborating quotation
(`PROJECT-STATUS.md:79`) exists only at `c70540e`. The defect it corroborates
— the offering's silence — exists at `a7b3375` too.

---

# Would the owner be surprised?

**Yes. Twelve surprises, and one of them means the act would not be a knowing
act at all.**

The digest arithmetic is sound. All 32 module digests recompute exactly, the
manifest's population is exactly the module set in both directions, all five
act arguments match their named subjects, every mechanical check passes, and
the four contract sections I was asked to read in full are unusually
well-written — a cold reader can restate what nearly all of them bind.

What is not sound is **the owner-facing offering**. The document whose entire
job is to make these acts knowing does not name the two open blocking
contract defects that this repository's own status page says it names. The
governing acceptance record's package-identity section understates act 1 by
six clauses. And one binding clause inside act 1's digest set selects on a
metadata key that was deliberately deleted from all 32 modules in the same
round.

An owner who read only the offering and the subjects would perform act 1
believing the corpus contains 322 clauses, that its known defects are the ten
listed, and that RFC-0011's selection rule is implementable. All three are
false.

---

# The surprises

## S1 — The offering does not state the two open blocking contract defects, and the status page asserts that it does. **[Sharpest]**

[Observed] `PROJECT-STATUS.md` names two open contract-level defects, "both
found by independent review at the 2026-08-07 close, and neither repaired":

1. Mission safety is not closed — "RFC10-17's `reserved + spent never exceeds
   authorized` is stated over the ledger and nothing states it over
   consumption, while RFC10-10 says Mission Control MUST prevent every
   mediated act from exceeding the envelope. **Both cannot be true as
   written.**"
2. "Deterministic context selection is not yet true, and not yet true even
   for a human. RFC11-4 requires the phase-rule clause of every selected
   contract; 6 of 353 clause rows carry that kind and RFC-0001…0005 have
   none, so a conformant selector fail-closes on all nine golden fixtures."

It then claims, at `PROJECT-STATUS.md:79`:

> knowingly, and the acceptance packet states them before the act phrases.

[Observed] **The acceptance packet states neither.** Mechanical sweep of
`round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md` with `grep -c -F`:

| Token | Hits in the offering |
|---|---|
| `RFC10-10` | **0** |
| `RFC11-4` | **0** |
| `consumption` | **0** |
| `round-2026-08c` / `08c` | **0** |
| `2026-08-07` | **0** |
| `RD-1`, `RD-4` | **0** |
| `RFC10-17` | 1 — only inside the range "RFC10-17…RFC10-22" at §2 |

The full set of clause identifiers the offering mentions anywhere, extracted
with Python `re` over the file: `RFC2-24, RFC3-10, RFC6-14, RFC7-24, RFC8-9,
RFC9-8, RFC9-32, RFC10-15, RFC10-17, RFC10-18, RFC10-19, RFC10-20, RFC10-22`.
Neither `RFC10-10` nor `RFC11-4` is among them. The only round directory it
cites is `round-2026-08`.

The offering's §3 "What is knowingly imperfect inside the acts" has ten rows.
Row 9 covers RFC10-20/RFC10-19 — **different** findings, from RC-10. Nothing
covers the RFC10-17/RFC10-10 contradiction or the RFC11-4 unsatisfiability.

[Inferred] The offering was partially refreshed on 2026-08-06 — its act-2 row
cites "review RD-6 (finding H-1)" — so the mechanism to update it exists and
was exercised for the act-2 digest. Its §3 defect table simply was not
carried forward through the 08c round.

**Consequence.** The owner is routed to this offering by two independent
paths — `AGENTS.md` ("The owner-facing offering is
`contracts/candidates/round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`") and
`PROJECT-STATUS.md` — and told by the second that it carries the blocking
defects before the act phrases. It does not carry them at all. A checker who
verified the claim at `PROJECT-STATUS.md:79` by reading the offering would
find ten imperfections and conclude the two blocking ones must be among them.

This is the finding that converts act 1 from a knowing act into a surprised
one, and it is the reason for the verdict.

## S2 — The governing acceptance record understates act 1 by six clauses

[Observed] `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:185-189`, under
"## 3. Package identity":

> **Clause inventory (script-verified, `scripts/verify_final_prespec.py`):**
> **322 numbered clauses** — … **RFC10-1..16, RFC11-1..12** (new contracts).

[Observed] The actual inventory, by two independent methods:

- My own parse (Python `re`, `^\*\*(RFC(\d+)-(\d+))(\([a-z]\))?\s*(?:\.|—|-)`
  anchored at line start, over all 32 modules): **328 numbered clauses**, 24
  lettered sub-clauses, RFC10 running **1..22**.
- `verify_final_prespec.py` output, read directly rather than by exit code:
  `numbered clauses defined: 328`.

The gap is exactly the six correction-plane clauses **RFC10-17..RFC10-22**.
§1's act-1 row narrates that they were added ("RFC-0010 gained six clauses
(RFC10-17..22, the correction plane)"), but §3 — the section titled *Package
identity*, the one a reader consults to learn what the package **is** — was
never updated. It still claims the label "script-verified" for a figure the
script now contradicts.

[Observed] Two derived figures in the same section are stale in the same way:
`:193` states RFC-0001 at "8,353 words" against an actual `wc -w` of
**8,342**; `:199-201` states the corpus at "99,067 on disk" against
`verify_final_prespec.py`'s **102,623**.

[Observed] `:276` states "The manifest has been regenerated twice since" the
2026-08-03 CONFIRM. §1's own act-1 row records **six** re-quotes.
`PROJECT-STATUS.md` says "superseded three times". Three incompatible counts
across two files, one of which is the acceptance authority.

## S3 — A binding clause inside act 1 selects on a front-matter key that was deleted from all 32 modules

[Observed] `rfcs/RFC-0011-context-compiler.md:108-109`, inside **RFC11-4**, a
normative clause:

> contract dependencies (`depends_on` /
> `provides_to`); explicit `applies_to` and clause-level metadata …

[Observed] `grep -rn -F "provides_to"` over `rfcs/` returns **exactly one
line: this one.** No module carries a `provides_to:` key. The offering itself,
§2, states why:

> `provides_to` was removed from all 32 modules and is now derived by
> reversing `depends_on`, so the asymmetry class that had sat at 20 edges
> under a green drift check is unrepresentable rather than merely absent.

So RFC11-4 instructs the compiler to select on a key the corpus does not
have. The removal was a deliberate normative change made in this round; the
clause that names the key was not swept. Nothing checks it: `CG-13` validates
dependency *edges*, and `build_contract_index.py` reads `depends_on`, so a
prose mention inside clause text is invisible to both.

This is not fatal — a reader can infer the derived reverse-edge is meant —
but it is a **live dangling reference inside act 1's digest set**, of the same
class the round spent six re-quotes eliminating. It is disclosed nowhere.

## S4 — §7 item 10 asks the owner to rule on a defect that no longer exists

[Observed] `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:334-344`, the
last of the "Items requiring explicit owner attention at the gate":

> 10. **R1 — one stale navigation count inside the accepted digest set**
>     (confirming review): `rfcs/RFC-0007/README.md` line 46 states its own
>     size as 2,268 words … The owner chooses knowingly: **accept as-is** …
>     or direct a fix + digest regeneration + one more digest-binding review.

[Observed] `rfcs/RFC-0007/README.md` line 46 now reads (lines 45-53):

> Module sizes are deliberately **not stated here**. A measurement copied into
> contract prose goes stale the moment any module moves … the current
> measurement lives in the generated budget report
> `../../CONTEXT-BUDGET-REPORT.md`, which is regenerated, never transcribed.

`grep -rn -F "2,268"` and `-F "10,578"` over `rfcs/` return **zero hits**. The
figure was removed by the fourth re-quote ("six package READMEs and
RFC-0009's word-accounting section lost every volatile measurement they
carried", §1 act-1 row). The owner-attention item survived the fix.

**The surprise is the shape of it, not the size.** The record presents the
owner with a live, consequential-sounding choice — one branch of which is
"direct a fix + digest regeneration + one more digest-binding review" — over
nothing. An owner who chose that branch would commission a review cycle for a
string that is not in the corpus.

## S5 — Two of the offering's ten disclosed imperfections are themselves stale

[Observed] Offering §3 row 6:

> | 6 | act 1 | RFC9-32 cites `RFC 0008 §5` — a navigational section — as
> authority |

`grep -rn -F "RFC 0008 §5"` over `rfcs/` returns **zero hits**. I read RFC9-32
in full at `rfcs/RFC-0009/visual-grammar-and-lenses.md:194-206`: it cites
RFC1-22 and RFC9-31, both clause identities. The acceptance record's §1
act-1 row confirms the fix landed in the fourth re-quote.

[Observed] Offering §3 row 10:

> | 10 | act 1 | The RFC10-18 repair RC-10 prompted is inside act 1's digest
> set and **has been read by no reviewer** |

Superseded. The acceptance record §1 act-1 row records a sixth re-quote:
"confirming review RD-1 returned `REVISE` over the fifth argument's bytes with
three blocking findings, all repaired". The "Read this first" section's whole
framing — "**Those fixes have in turn been read by no reviewer**" — is
likewise pinned to the RC-10 round, two rounds back.

Both errors run in the *conservative* direction (warning about defects since
fixed), which is the safe way to be wrong. But combined with S1 they establish
that **§3 is not a current inventory of what is wrong**, and the owner has no
way to know which rows are live.

## S6 — The offering declares its own act-1 row superseded by a document that does not exist

[Observed] `round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md:39`:

> | 1 — foundational contracts | `2862b2f5…` | **Yes, five times** — most
> recently 2026-08-06 for the rev11b correction-plane repairs; **superseded by
> the 2026-08-06 closure round's owner acceptance packet** |

[Observed] `find .syzygy -iname '*ACCEPTANCE*' -o -iname '*OWNER-ACCEPT*'`
returns exactly three files: the governing
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, this offering, and the
banner-marked `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md`.
`round-2026-08c/` contains **no** acceptance record. `grep -rn -F "closure
round's owner acceptance packet"` over `.syzygy/` returns this one line and
nothing else.

The digest on that row is nonetheless **correct** — `2862b2f5…` is the current
`sha256sum` of `ACTIVE-CONTRACT-MANIFEST.txt`. So the row's *argument* is
good and its *provenance sentence* points nowhere. The most charitable reading
is that it means the governing acceptance record's sixth re-quote; the text
does not say that.

The owner is thus routed by `AGENTS.md` and `PROJECT-STATUS.md` to a document
that tells them, in its own act-1 row, that it has been superseded — without
naming what by.

## S7 — Act 2's phrase names one amendment; its digest binds a file that adopts two external bars

[Observed] The act phrase, `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:16`:

> `CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0`

and its "Accepts exactly" cell: "only this amendment needs confirming."

[Observed] `sha256sum
.syzygy/governance/policies/craft-and-care/testing-and-verification.md` =
`7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0`. The
argument is the **whole file's** digest, matching `INSTALL-RECORD.md:105`.
The file carries CC-TEST-1 through CC-TEST-7 (verified by `grep -on`, seven
rule headings at lines 13, 28, 65, 81, 106, 121, 136).

[Observed] `testing-and-verification.md:146-147`, inside CC-TEST-7:

> This cluster adopts bars 9 and 10 unmodified, by
> reference, the same as bars 1–8.

That is an **adoption by reference of two external canonical bars**, riding
inside the digest bound by an act phrase that names CC-TEST-2. `INSTALL-RECORD.md:93-95`
discloses CC-TEST-7's existence but describes it as "recording the re-check of
CC-TEST-1…6 against test-rigor's two new bars (no conflicts found)" — framing
it as a *record*, not as an adoption.

[Inferred] The substance is almost certainly benign; the pin move was an
explicit owner override closing P-26. The surprise is structural: the act's
name and its argument have different scopes, and the wider scope contains an
adoption the act's name does not mention.

## S8 — `constrains:` is a normative-looking relation key that no clause defines, and both instances are under-inclusive against their own source

[Observed] `grep -rn "^constrains"` over `rfcs/` returns four lines in two of
32 modules:

- `rfcs/RFC-0005/admission-and-boundary.md:10-11` —
  `constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]`, `constrains_source: RFC5-3`
- `rfcs/RFC-0007/narrative-contract.md:10-11` —
  `constrains: [RFC-0001, RFC-0002, RFC-0004, RFC-0008]`, `constrains_source: RFC7-3`

[Observed] RFC7-3, the declared source, at `narrative-contract.md:98-102`:

> No claim, gap, mapping, evidence link, work warrant, source anchor, or
> citation **anywhere in Syzygy** may resolve to a Polaris narrative …

RFC7-3 constrains *every* contract. The declared list names four. Likewise
RFC5-3 at `admission-and-boundary.md:109-117` binds "**for all present and
future clients** … **no later contract may introduce one**"; the list names
four of the six later contracts.

[Observed] `build_contract_index.py` reads and projects `constrains` (lines
89-142) but **validates nothing about its completeness**; `CG-13` examines
`depends_on` edges only. No module, README, or manifest defines what
`constrains` means. This key was added, removed, and re-added across the
fourth and fifth re-quotes (per §1's act-1 row) — three digest churns for a
relation with no definition and no check.

[Unknown] Whether the four-element lists are intended as exhaustive or as
exemplary. The text does not say, and there is no owning definition to consult.

## S9 — Act 1 binds contract text that names unresolvable identifiers as "binding provenance"

[Observed] `rfcs/RFC-0005/admission-and-boundary.md:72-74`:

> Decision
> identifiers named inline (A1, B4, B9, FD-009, FD-018/FD-029) remain binding
> provenance here.

[Observed] `A1`, `B4`, `B9` resolve — `decisions/OWNER-ANSWERS-2026-08-01.md`
carries them (e.g. `:56` for B9). **`FD-009` and `OQ-007` resolve nowhere
authoritative in the clone:** `grep -rn -F "FD-009"` over
`.syzygy/governance/decisions/` and `.syzygy/governance/doctrine/` returns
**zero hits**. The identifier appears only inside RFC-0005's own modules, the
frozen rev9 history, and one review transcript. There is no FD-register in
`decisions/`.

[Inferred] `FD-*` and `OQ-*` are founder-decision identifiers from the
git-excluded `_bootstrap/` tree. `CG-12` guards `_bootstrap/` **paths**; bare
identifiers pass it invisibly.

So act 1 binds a clause stating that an identifier is binding provenance,
where no clone reader can discover what that provenance says. This is the
"grounded in FD-009 (LAN posture) and OQ-007" attribution at
`admission-and-boundary.md:30-31` behind RFC5-8's exposure-mode set.

## S10 — README and OVERVIEW type Mission Control differently

The commission asks whether the overview contradicts `README.md`. One place.

[Observed] `.syzygy/intent/OVERVIEW.md:85-88`:

> And one thing that is *not* a surface: **Mission Control**, a
> **workspace-level operator capability** spanning projects …

[Observed] `README.md:40` heads a table "## The four experiences", and
`README.md:47` gives Mission Control the literal-subtitle cell:

> | **Mission Control** | workspace operator surface | …

The subtitle column is the same column carrying "the intent surface", "the
work surface", "the map surface". README cures it two paragraphs later
(`:50-52`: "Mission Control is a workspace-level operator capability, not a
fourth project truth surface"), so a reader who continues is not misled. A
reader who reads the table is.

[Inferred] The governing clause is RFC10-1, which OVERVIEW's drawer-2 row 231
cites as "Mission Control is not a fourth surface". README's table cell is the
odd one out.

## S11 — `PROJECT-STATUS.md` routes act 2 to the superseded correction block

[Observed] `PROJECT-STATUS.md:24`:

> | 5 | Craft amendment CC-TEST-2 (act 2) | ⏳ **Awaiting confirmation** at the
> current digest | `INSTALL-RECORD.md` correction block, **2026-08-05** |

[Observed] The 2026-08-05 block (`INSTALL-RECORD.md:58-78`) carries
`3858820f…`, which `:111-112` states "satisfies nothing". Act 2's current
argument comes from the **2026-08-06** block at `:102-112`.

The cell hedges with "at the current digest", so it does not state a wrong
value — it points at the block that holds the retired one. This is the exact
class the offering's own act-2 row was corrected for (finding RD-6 H-1,
closed by CG-7e); CG-7e enumerates files carrying act-argument *copies*, and
`PROJECT-STATUS.md` carries a *pointer*, not a copy, so it passes.

## S12 — The offering carries no act phrases and no §7, and its imperfections sit after its arguments

The commission asks four questions about the offering. Answering them exactly:

**"Does every act phrase in it match the phrase its owning record defines,
character for character?"** [Observed] **The offering contains no act
phrases.** Its §1 table column is headed "Argument (verify, never
transcribe)" and holds five bare digests. The phrases live only in
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:15-19`. This is deliberate
and disclosed at `:3-8` ("that record wins — it owns the exact phrases and the
ceremony"), and it is the safer design. All five **arguments** verify against
their subjects, computed fresh:

| Act | Subject | Computed sha256 | Matches offering |
|---|---|---|---|
| 1 | `ACTIVE-CONTRACT-MANIFEST.txt` | `2862b2f5…f057d7` | yes |
| 2 | `craft-and-care/testing-and-verification.md` | `7a716090…9690a0` | yes |
| 3 | `topology-candidates/BUNDLE-MANIFEST.md` | `7a3b2249…1fbaeb` | yes |
| 4 | `intent/OVERVIEW.md` | `01d62951…29c7cd1` | yes |
| 5 | `DOCTRINE-AMENDMENT-…-D3.md` | `e973e8e0…f8d9c9` | yes |

**"Does it put remaining substantive imperfections before the act phrases, or
after?"** [Observed] **After.** §1 is the arguments table; §3 "What is
knowingly imperfect inside the acts" follows it. The single sharpest residual
is hoisted above §1 into "## Read this first", which is the right instinct —
but the ten-row table sits below the arguments, and the two blocking defects
(S1) sit nowhere.

**"Does it state anything as settled that is actually open?"** [Observed] Yes
— by omission, per S1: silence on the RFC10-17/RFC10-10 contradiction and
RFC11-4's unsatisfiability presents act 1's defect set as complete at ten
items. Also S5: rows 6 and 10 state as open what is closed, the harmless
direction.

Against that, §2's withdrawn-count paragraph (`:82-94`) is exemplary —
"**No definition of 'an ordinal citation' yet proposed yields a stable
number** … The count is [Unknown] and is stated as Unknown rather than picked."
That is the discipline the rest of §3 lacks.

**"Are the §7 owner-attention items still accurate?"** [Observed] **The
offering has no §7** — its sections are "Read this first", 1, 2, 3, 4, 5, 6.
The §7 items are in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:293-344`.
Reading those ten:

- Items 1–9: [Observed] still accurate. Item 1 (RFC 0003 §8 q4 `declarations/`),
  2 (SEC-3 extension), 3 (RFC 0005 §8 q1 — confirmed still OPEN at
  `rfcs/RFC-0005/admission-and-boundary.md:394`), 4 (D3), 5 (corpus size), 6–9
  (safety consequences) all check out against their subjects.
- **Item 10: dead.** See S4.

---

# Subject-by-subject findings

## Subject 1 — act 1, the 32 compacted foundational contract modules

### 1. Population, both denominators

[Observed] **Exact match, no remainder in either direction.**

- Manifest entries parsed with Python `re` (`^([0-9a-f]{64})\s+(.+)$`, skipping
  `#` lines): **32**.
- Files under `rfcs/` of **any** extension (`Path.rglob('*')`, `is_file()`):
  **32**. All 32 are `.md`. There is no non-markdown file, no dotfile, no
  subdirectory artifact.
- Manifest entries with no corresponding file: **0** (enumerated: empty list).
- Files present but not listed in the manifest: **0** (enumerated: empty list).

The manifest's own regeneration recipe (`ACTIVE-CONTRACT-MANIFEST.txt:2`) is
`find rfcs -name '*.md' | sort | xargs sha256sum`, whose output I reproduced
independently — 32 lines, byte-identical set.

### 2. Digest recomputation

[Observed] **All 32 match.** Two methods:

- `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` from
  `contracts/candidates/` — every line `OK`, zero non-`OK` lines after
  filtering.
- Independent Python `hashlib.sha256(p.read_bytes()).hexdigest()` compared
  against the parsed manifest map: `DIGEST MISMATCHES: 0`.

No digest was read out of prose. Re-verified after the commit drift; still 32/32.

The manifest's own digest, computed: `2862b2f54e39e6d477129147eb2e1d0cb4ca714c26edabd75505e2e38ff057d7`
— identical to act 1's argument in both the acceptance record and the offering.

### 3. Volatile artifacts inside the digest set

[Observed] **None found, and the corpus is actively defended against the
class.** I swept all 32 modules with Python `re` for six volatility patterns:
transcribed word counts (`\d[\d,]{2,}\s*words`), generated-file markers,
as-of dates, literal sha256 strings, measurement/budget references, and
status-file references.

The only hits are the **inverse** of the defect: seven package READMEs each
carry a paragraph refusing to state a measurement, e.g.
`rfcs/RFC-0002/README.md:51-53`:

> This artifact is governed by the applicable context-budget
> policy; the current measurement lives in the generated budget report
> `../../CONTEXT-BUDGET-REPORT.md`, which is regenerated, never transcribed.

Zero transcribed word counts, zero literal digests, zero dates-of-measurement
inside the 32.

[Observed] No generated file is in the digest set. `build_contract_index.py`
writes only `05-CONTRACT-INDEX.yaml`; `build_dependency_index.py` writes only
`CONTRACT-DEPENDENCY-INDEX.md`; `build_budget_report.py` writes only
`CONTEXT-BUDGET-REPORT.md` and the **fixture** files under
`fixtures/` (`build_budget_report.py:390`, target resolved from
`fixture_paths()`, not from `rfcs/`). None of these paths is a manifest entry.
`CG-21` independently reports "contract prose states no measurement — 32
modules examined, 0 findings", denominator correct.

**This subject is clean.** It is the one place the round's discipline fully
took.

### 4. Front-matter internal consistency

[Observed] **Consistent across all 32, with the `constrains` caveat at S8.**
I parsed each module's front matter and independently extracted every clause
definition, then compared.

- **Declared range vs. defined clauses:** every module's `clauses:` range
  matches exactly what it defines. Verified per module — e.g.
  `RFC-0005/admission-and-boundary.md` declares `RFC5-1..RFC5-11,
  RFC5-24..RFC5-26` and defines exactly `{1..11, 24, 25, 26}`;
  `RFC-0003/manifests-and-namespace.md` declares `RFC3-1..14 and RFC3-18..32`
  and defines exactly that, with 15/16/17 living in the sibling module as its
  front matter says.
- **Package unions:** complete and disjoint. RFC2 = 1..25 across four files;
  RFC3 = 1..32 across two; RFC4 = 1..29 across four; RFC5 = 1..26 across
  three; RFC7 = 1..38 across two; RFC8 = 1..32 across three; RFC9 = 1..52
  across three. No clause defined twice, no gap.
- **Package READMEs define zero clauses** and declare the package-wide range —
  correct index behavior, not a clause-ownership conflict.
- **`id` matches package:** all 32. `ids present:` exactly `RFC-0001` …
  `RFC-0011`.
- **Sub-clauses:** every lettered sub-clause declared in front matter is
  defined in the file that declares it — RFC1-18(a)/(b), RFC1-25(a)–(d),
  RFC3-15(a)/16(a)(b)(c)/17(a), RFC4-13(a)/(b), RFC7-11(a) (with RFC7-2(a)–(c)
  and RFC7-9(a)–(c) as in-clause lettered parts), RFC9-8(a)/9(a)/9(b)/13(a)/
  14(a)/15(b), RFC9-47(a), RFC10-17(a)/18(a)/19(a). 24 total.
- **`depends_on`:** every target is one of RFC-0001…RFC-0011. **No dangling
  contract reference.** Corroborated by `CG-13` ("dependency edges resolve;
  README = module union — 146 edges examined, 0 findings") and
  `build_dependency_index.py --check` ("dependency index matches
  regeneration — no drift").

### 5. Could a cold reader restate what these bind?

I read all four in full.

**RFC-0001 §3.4 (capability), `RFC-0001-…-state-planes.md:263-295`.** [Observed]
Mostly yes. RFC1-14 (capability is stable product-behavior identity, drafted
capabilities may not anchor the map, unmapped code renders Unknown), RFC1-15
(Requirement/Scenario are references, degrade to Unknown, never guess),
RFC1-16 (four never-conflated capability↔code classes; a passing test does not
prove semantic ownership), RFC1-17 (identity-based aggregation, one code
element counted once per query subject) are each restatable from the text
alone.

**One clause whose meaning I could not establish from the text alone:**
**RFC1-16.** It says class (i) "lives in the **Declared implementation
mapping** governance artifact — the primary declaration site (SDR-4)". The
text capitalizes a specific artifact it never defines, never locates, and
never cites a clause for. A cold reader cannot determine what artifact this
is or where it lives. (RFC-0003 owns homes, but RFC1-16 does not say so.)

Also: RFC1-14 and RFC1-15 rest on `[Observed: architecture.md, Definitions]`
and `[Observed: v1.md]`. Both files exist under `doctrine/`, so these resolve
— unlike S9's FD identifiers.

**RFC-0005 admission (`admission-and-boundary.md`, full module).** [Observed]
**Yes, and this is the best-written module I read.** The §0 reader map names
the four load-bearing rules before any clause. RFC5-3's two exhaustive client
classes, RFC5-4's session discipline (with the explicit `[Inferred]`
justification for why lifetime and revocation are the *entire* remaining
mitigation), RFC5-6's six-property credential shape, RFC5-8's closed exposure
set, RFC5-11's acts-versus-claims rule, RFC5-24's injection prohibition, and
RFC5-25's out-of-tree audit-trail constraint are all restatable cold. RFC5-25
even explains *why* the location is normative rather than organizational —
that a trail inside the governed tree "would let any fleet worker forge the
very correlation every RFC3-16(a) gate rests on".

**Clauses I could not fully establish:** none on their operative content.
But RFC5-8's grounding in `FD-009` and `OQ-007` (S9) is unresolvable, and
`:72-74` calls those identifiers "binding provenance".

**RFC-0007 narrative-contract (full module).** [Observed] **Yes.** RFC7-2's
three-and-only-three kinds of load-bearing claim, RFC7-3's total
non-citability ("Deleting everything under `.syzygy/intent/**` changes **no
truth, status, work, consent, or normative fact**"), RFC7-9's
covers/minimality/bounding triad with its concrete twenty-anchor
counter-example, RFC7-10's target-state component, RFC7-11(a)'s drift
rendering with its explicit non-minting of an RFC2-24 reason, RFC7-21's
per-claim adoption attestation, and RFC7-25's asymmetric materiality
declaration are all restatable cold. The clauses that gate on RFC3-16(a)
each state the loop they close, in one sentence, in place.

**Clauses I could not fully establish:** none. The one place a cold reader
must leave the file — RFC7-16's "architecture.md reserves composite maturity
rendering to 'the graph/status RFC'" — names the reservation, names that no
contract in the set discharges it, and names where the deferral is carried.
That is the honest form.

**RFC-0011 (full contract).** [Observed] Yes on 11 of 12. RFC11-1's packet
field list, RFC11-2's digest-in-execution-record rule, RFC11-3's
"read all project documentation is a violation, not a fallback", RFC11-5's
one-way inference rule, RFC11-6's fail-closed default, RFC11-7's no-second-
truth-store, RFC11-8/9's memory boundaries, RFC11-10's profile rules, and
RFC11-11's non-shardable core are restatable cold.

**The clause whose meaning I could not establish from the text alone:
RFC11-4.** Two reasons. (a) It selects on `provides_to`, which does not exist
— S3. (b) `PROJECT-STATUS.md` records an independent derivation showing its
phase-rule requirement makes a conformant selector fail closed on all nine
golden fixtures, because RFC-0001…0005 carry no phase-rule clause. Reading
the clause alone, I could restate the *words*; I could not establish that
they describe a satisfiable procedure, and the offering does not tell the
owner they do not.

## Subject 2 — acts 2, 3, 4

**Act 2 — CC-TEST-2.** [Observed] Digest verifies (see S12 table). Subject
per `INSTALL-RECORD.md:105`. I read CC-TEST-2 (`testing-and-verification.md:28`)
and CC-TEST-7 (`:136-150`). **Is what the act confirms the same thing the
acceptance record describes?** [Observed] **Not exactly** — see S7. The
record describes confirming one amendment; the digest binds a seven-rule file
whose seventh rule adopts two external bars by reference.

**Act 3 — topology bundle.** [Observed] **Clean.** `BUNDLE-MANIFEST.md`
digest = `7a3b2249…`, matching both records. `sha256sum -c` against the
manifest's own block from `topology-candidates/`: **9 of 9 OK**. Population:
the directory holds 11 `.md` files — the 9 members, plus `BUNDLE-MANIFEST.md`
itself (correctly excluded; it is the act's argument, not a member) and
`TRACKING-NOTE.md`. [Inferred] `TRACKING-NOTE.md`'s exclusion is right — a
tracking note is exactly the volatile class that must not be digest-bound —
but the manifest does not say it is deliberately excluded, so a reader
counting files in the directory sees 11 and a manifest listing 9 with no
statement of why. Minor; not counted among the twelve.

**Act 4 — project overview.** [Observed] Digest verifies. I read
`OVERVIEW.md` in full against `README.md` and the contracts.

*Does it claim anything the contracts do not support?* [Observed] No claim
outruns its authority, and drawer 2 (`:220-242`) is an explicit
claim→authority→kind table marking each row Adopted / Candidate / Recorded.
The strongest candidate for over-claim is §"What the owner actually approves"
(`:90-96`), which states the Mission envelope in the present indicative
without repeating the candidate caveat — but `:88` has already said Mission
Control "rests on a candidate contract and a proposed doctrine amendment,
neither accepted", and drawer-2 row 232 marks RFC10-7/RFC10-8 Candidate. The
disclosure is present, eight lines earlier.

The overview's refusal to restate gate state (`:119-125`: "a gate table frozen
inside it would go quietly false the first time a gate fired") is the correct
handling of a digest-frozen file and should be preserved.

*Does it contradict README.md anywhere?* [Observed] One place — S10, the
Mission-Control-as-surface typing.

[Observed] `CG-23` reports the overview uses two advanced registry terms on
the default path (`Claim` ×2, `Evaluation` ×1). Report-only, the registry
being candidate; noted, not counted.

## Subject 3 — act 5, D3 rev1

[Observed] Digest verifies. I read the packet in full against adopted
`doctrine/vision.md` VIS-4 (`vision.md:124-140`).

**Does adopting D3 as written also settle D4 by stipulation?** [Observed]
**Yes, and the packet says so.** `D3.md:222-229`:

> The insertion places a bounded mission inside VIS-4's bounds
> by declaring it a species of human trigger. It does that inside the one
> sentence whose second half exists to foreclose exactly that move …
> An owner who adopts §1.2 to settle the mission question
> would also, silently, have settled D4.

**Is the §6 disclosure adequate for a reader who has not been told to look for
it?** [Observed] **Partly — with one structural defect.**

In its favor: §6 opens "**Read this before adopting §1.2.**"; it quotes the
objection, states the procedural consequence ("rule D4 first, then adopt
whichever text the ruling implies"), offers the reviewer's alternative text
verbatim marked unadopted, adds the separable §1.1 maximum-autonomy point,
and closes "**Nothing here is adopted, and this section changes no proposed
text.** It exists so that adopting §1 is a knowing act." That is a model
disclosure. And D4 is raised on the first screen, at `:31-44`, under a heading
naming it ("the D4 question; the owner may overrule this position").

The defect: **§6 sits after §5 "Adoption mechanics".** §5 is a numbered
five-step procedure ending with "**Digest of this packet:** compute at act
time", which reads as the document's close. A reader who reaches the adoption
instructions and executes them never reaches the disclosure. Nothing in §5
cross-references §6, and nothing in §1.2 — the very text the disclosure is
about — points forward to it.

[Inferred] The fix is one line: a forward pointer at §1.2 and at §5 step 1.
The disclosure's content is adequate; its position is not.

**Two smaller observations.** (a) The anchor digests at `:56` and `:93` are
whole-file `sha256`s of `architecture.md` and `vision.md` — both verified
current — but are written as "`architecture.md` lines 246–248 at sha256
`e19d…`", which reads as a digest of the quoted lines. It is not:
`sed -n '246,248p' architecture.md | sha256sum` gives `ab6cf641…`. Harmless
because both file digests are current, ambiguous as written. (b) `:234-236`
cites `doctrine/vision.md:127-131` for the adjudication-RFC requirement; that
range does fall inside VIS-4, which I read at `:124-140`.

## Subject 4 — the offering

Answered in full at **S12**, with the substantive failures at **S1**, **S5**
and **S6**.

---

# What I verified mechanically, with denominators

Every claim above rests on a sweep run in this session. Per the repository's
own rule 2, I make no "zero / all / 100%" claim without naming the sweep and
its denominator, and each was confirmed by a second method where one exists.

| Claim | Method 1 | Method 2 | Denominator |
|---|---|---|---|
| 32 digests match | `sha256sum -c` | Python `hashlib` | 32 / 32 |
| Population exact both ways | `rglob('*')` + `is_file()` | manifest parse via `re` | 32 files, 32 entries, 0 remainder each way |
| 328 numbered clauses | my own `re` parse | `verify_final_prespec.py` output | 32 modules |
| No transcribed measurement in the 32 | 6-pattern `re` sweep | `CG-21` (32 modules, 0 findings) | 32 modules |
| `provides_to` orphaned | `grep -rn -F` over `rfcs/` | `grep -rln -F` over `.syzygy/` | 1 hit in 32 modules |
| `RFC 0008 §5` gone | `grep -rn -F` over `rfcs/` | read RFC9-32 in full | 0 hits |
| `2,268` gone | `grep -rn -F` over `rfcs/` | read `RFC-0007/README.md:40-60` | 0 hits |
| Offering omits the two defects | `grep -c -F` per token | Python `re` extraction of every `RFC\d+-\d+` | 13 identifiers, neither present |
| No 08c acceptance packet | `find -iname '*ACCEPTANCE*'` | `grep -rn -F` on the phrase | 3 files found, 1 line found |
| 9 topology members | `sha256sum -c` | directory listing | 9 / 9 OK, 11 `.md` present |
| 5 act arguments | `sha256sum` per subject | `CG-7a`–`CG-7e` output | 5 / 5 |

[Observed] Full check battery, output read rather than exit codes:
`check_governance.py` — **26 OK, 14 WARN, 0 FAIL (40 checks)**.
`verify_final_prespec.py` — **PASS**, with two printed notes (RFC-0001 over
ceiling, justified; corpus 102,623 over band).
`build_contract_index.py --check` — no drift.
`build_dependency_index.py --check` — no drift.

[Observed] Per rule 4, one denominator worth naming: `CG-24` reports "16 of 24
check families have at least one fixture", enumerating the eight without one
(`CG-1, CG-2, CG-3, CG-4, CG-5, CG-6, CG-9, CG-10`). None of my findings rests
on those eight.

[Unknown] I did not perform rule 6 (mutate the input, confirm the check fails)
per predicate, and I did not run rule 7 (battery in a clone). Both were out of
scope for this commission and neither is claimed.

---

# What would make this CONFIRM

The subjects are in far better shape than the offering. In rough order of
what actually changes the owner's knowledge:

1. **S1** — put the two blocking defects in the offering, before the act
   phrases, or correct `PROJECT-STATUS.md:79`. Until one of these happens, act
   1 is not a knowing act.
2. **S2** — regenerate the acceptance record §3 inventory. It is
   digest-stable: §3 is not inside act 1's digest set, so the fix costs no
   re-quote.
3. **S3** — the only finding requiring a manifest churn. Strike `/
   `provides_to`` from RFC11-4 or replace it with the derived-reverse-edge
   wording. Worth batching with any other in-corpus fix rather than done alone.
4. **S4** — delete §7 item 10. Also digest-stable.
5. **S5, S6** — refresh the offering's §3 rows 6 and 10, and either name the
   superseding packet at `:39` or drop the clause.
6. **S7, S8, S9, S10, S11** — disclosure and definition work, none requiring a
   digest change to a contract module except S8 if `constrains` is to be
   defined in-corpus rather than in the manifest.

The digest arithmetic, the population accounting, the front-matter discipline,
the volatility defense inside the 32, and the four contract sections I read in
full are all sound. The failure is that the document standing between the
owner and these subjects no longer describes them.
