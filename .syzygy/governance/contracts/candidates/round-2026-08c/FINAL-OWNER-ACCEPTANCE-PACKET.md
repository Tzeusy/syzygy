# Owner acceptance packet — 2026-08-07

> **This packet performs nothing.** No act has been performed and no agent may
> perform one (VIS-4). It states what each act would bind, **what is knowingly
> imperfect inside it**, and then the exact phrase.
>
> **Where this packet and `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
> disagree, that record wins** — it owns the ceremony, the five steps, and the
> canonical phrases. This packet is the round's offering, not a second
> ceremony.
>
> **Verify before acting:** `python3 scripts/check_governance.py`, and read
> CG-7a…CG-7e. **A CG-7 failure means "do not perform that act"**, never a
> formatting nit. This packet restates no measurement — every figure lives in
> its generated home.

## Read this first

**Eight independent reviews ran this round. Every verdict was `REVISE`.** None
is softened here; raw output is at `reviews/`, never edited.

**No CONFIRM verdict is bound to the bytes below.** The last CONFIRM
(2026-08-03) named a manifest digest superseded three times since.

**Three of twelve pre-specification criteria are unmet** — deterministic
context selection, the golden fixture set, and Mission safety. They are named
in `FINAL-PRE-SPECIFICATION-READINESS-REPORT.md` with the finding that blocks
each.

**None of that blocks an act.** Every one of these is a **candidate-corpus
defect an act would bind knowingly**, and the whole purpose of the section
below is that "knowingly" is true.

---

# What is knowingly imperfect, stated before any phrase

## Inside act 1 — the 32 foundational contract modules

### 1. Mission safety is open, and the answer to its question is yes

Asked whether a bounded, autonomous Mission can cause an unrecoverable or
unauthorized outcome without an owner act, an independent reviewer answered
**yes, by at least three independent routes**. Two reviews read the identical
RFC-0010 bytes without reading each other and converged on the same structural
defect.

- **The budget reservation is accounting, not enforcement.** RFC10-17's
  `reserved + spent never exceeds authorized` is stated over the ledger;
  nothing states it over consumption. RFC10-10 says Mission Control MUST
  prevent. **Both cannot be true as written.**
- **`reversible` is an effect class with no definition, no named action, no
  funding and no duty** — and it is the class an implementer will choose.
- **Provider egress breaks the contract whichever way the effects-applied
  predicate answers.**

Three RD-1 blocking findings were repaired; the repair re-instantiated one
escape **one state earlier**. **Nothing further was repaired**, and RFC-0010 is
frozen at its current digest — including a one-token `depends_on` fix both
reviewers found, because applying it would invalidate two reviews bound to
these bytes.

Full disposition, nothing waived: `MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md`.

### 2. RFC11-4's phase-rule universal has no population for five contracts

RFC11-4 requires the governing phase-rule clause of every selected contract.
**Six of 353 clause rows carry that kind; RFC-0001 through RFC-0005 have
none.** All nine golden fixtures load at least one of those five, so a
conformant selector marks every packet incomplete and does not launch.

> the nine artifacts offered as proof that deterministic selection works are
> the nine a conformant implementation cannot produce.

### 3. RFC11-4 does not name `constrains`, and still names `provides_to`

Two modules declare `constrains` with a clause anchor. The clause enumerating
the selector's inputs names neither it nor the reality that `provides_to` was
deleted from every module. **P-21(c).**

### 4. Eleven `depends_on` edges carry no clause evidence

Three of them are RFC-0011's. The earlier citation test was **scoped to 20
edges and the scoping was undisclosed**. **P-21(b).**

### 5. `Mission` is a first-class entity RFC-0001 does not admit

**Zero occurrences of `Mission` in RFC-0001**, while RFC10-4 declares a Mission
*"a first-class identified entity (minted under RFC 0001's identity rules)"*
and RFC10-12 says the same of the Attention Item. RFC1-5's vocabulary is
closed; RFC1-7's five profiles contain none that fits; its *"RFCs 0002–0009"*
range excludes RFC-0010. **Consequence: none of the eleven universal-visibility
facts is contractually available for a Mission. P-28.**

### 6. Three drawer facts are missing

The evidence drawer (RFC6-19) carries no **work and reconciliation state**
(`reconcil` has zero occurrences in RFC-0006), no **state plane**, and only a
partial **governing revision**.

### 7. RFC9-8(a) contradicts RFC3-10/11/21

An owner-gated snapshot-input registry placed inside a manifest those clauses
close as personal presentation state. **The corpus contains both the error and
its remedy** — RFC10-15 rejects the placement. **P-22**, to be ruled rather
than silently edited.

### 8. The manifest that is act 1's own argument has no generator

`ACTIVE-CONTRACT-MANIFEST.txt` is maintained by hand, in a repository whose
third verification rule reads *digests are scripted, never transcribed*.
Nothing suggests it is wrong today — CG-7a recomputes all 32 entries and
reports zero findings. **Repairing it would move the digest being offered.**

### 9. RFC-0001 is over the 7,000-word ceiling

Justified oversize, recorded in `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` —
*not* in RFC-0001 itself, which records no waiver. The corpus total exceeds the
35–50k target band. Current figures: `CONTEXT-BUDGET-REPORT.md`.

### 10. Eleven candidate-lane artifacts carry no candidate marker

Enumerated by review RD-6. A generated projection with no candidate banner is
one careless citation away from being read as accepted.

### 11. The §7 owner-attention items of the acceptance record still stand

They remain part of act 1's knowing acceptance.

## Inside act 2 — craft amendment CC-TEST-2

**This act's argument was wrong in the owner-facing offering until 2026-08-07.**
The offering carried a **retired** digest, and **no check examined it** — CG-7c
read the acceptance record's form, and a bare digest in a table row matched
neither CG-7c, CG-7d nor CG-15. Found by review RD-6 by mutating all four
arguments and observing the battery report zero findings. Corrected in three
files, and closed by **CG-7e**, which now enumerates every file carrying an act
argument and the acts each carries.

**Also open:** the knowledge-hygiene policy is a **separate** craft act and is
undecided between a 22-rule and a compact 10-rule version (**packet 7**). Until
it fires, **`CC-BUDGET-1` — the context-budget threshold — is installed
nowhere**, and four golden fixtures exceed a threshold no rule owns.

## Inside act 3 — the topology bundle

Nine files at the per-member digests in `BUNDLE-MANIFEST.md`. **No review this
round read the topology bundle.** That is a gap in coverage, not a finding
against it, and it is stated so the silence is not read as a clean bill.

## Inside act 4 — the project overview

- **Two advanced terms leak onto the default path** — `Evaluation` (T-22) and
  `Claim` (T-13) ×2. Reported by CG-23 every run.
- **`Reconciliation` is used in the sense T-26's entry explicitly reserves
  against**, and the corpus has **no term at all** for *"the difference between
  desired and observed"* — the concept the narrative is reaching for.
- **`README.md` and `OVERVIEW.md` contradict each other** on whether Mission
  Control is a surface.
- **Nine default-path terms have no registry entry**, including `workspace`,
  which has **zero occurrences in the entire adopted doctrine tree**.

**None was edited**, because they sit inside this act's own digest subject. The
reviewer's counter-argument is on the record and is a real one:

> Findings A.5, A-6 and G-1 are repairs to a *pending* offering, not
> corrections to a bound artifact — which, if the act has not fired, is the
> cheapest moment they will ever be available.

**That is owner packet 5(c): authorize the edits and re-digest before act 4, or
accept these bytes as they are.**

## Inside act 5 — doctrine amendment D3 (optional)

**Adopting D3 as written also settles open question D4 by stipulation** —
inside the one sentence of VIS-4 whose second half exists to foreclose that
move. The packet discloses this at its §6 and carries the reviewer's
alternative text, which states the reason rather than assuming it. **Neither is
adopted.**

**If D4 is ruled the other way**, no `vision.md` insertion is lawful without an
accepted adjudication RFC, and **act 1 becomes a *requirement* before act 5**
rather than the recommendation it currently is.

Separately: the `architecture.md` floor as drafted **omits any maximum autonomy
level**, moving *"how autonomous may a Mission be"* permanently out of
doctrine. Easy to miss, and it is a separate ruling. **P-24.**

---

# The acts

**Perform act 1 before act 5** (recommendation, not a rule): adopting D3 first
would leave *bounded mission* and *autonomy envelope* as adopted doctrine terms
whose binding definitions live only in an unaccepted contract.

**Verify each digest with CG-7 immediately before acting.** The five-step
ceremony is `../FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §2.

```text
ACCEPT COMPACTED FOUNDATIONAL RFCS: 2862b2f54e39e6d477129147eb2e1d0cb4ca714c26edabd75505e2e38ff057d7
```

```text
CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090bc827121b3f70c4f7e252fc5680cd8a56d7b4121b70f3673489690a0
```

```text
ACCEPT TOPOLOGY: 7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45
```

```text
ADOPT PROJECT OVERVIEW: 01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1
```

```text
ADOPT DOCTRINE AMENDMENT: D3 — e973e8e025c93b5d1e59d16d8661b0ae1f9804304c8f8de8957950acf3d8f9c9
```

**Act 5 is `ADOPT`, `AMEND`, or `DECLINE`.** Declining is a complete answer and
leaves bounded Missions outside doctrine.

**The first act creates `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`.**
Its absence today is correct.

---

## What happens after

Not a plan the owner is bound to — the order that follows from the evidence:

1. **The three unmet criteria's repair lists**, each written by someone who did
   not author the defect: split the RFC-0010 package then B1–B6; give
   RFC-0001…0005 a phase-rule clause or narrow RFC11-4; split each fixture's
   question from its answer.
2. **A fresh review over the new bytes**, by a reviewer who wrote none of it.
   *A repair pass may not be its own confirming reviewer* — the rule that
   produced every finding in this packet.
3. **The owner decisions that gate specification** — packets 6 (facets), 8
   (OpenSpec version) and 9 (license) block the first changeset;
   `OWNER-DECISION-PACKETS.md` states each with its earliest gate.
4. **Then OpenSpec Capability 1**, per `FIRST-OPENSPEC-SEQUENCE.md`.

**Nothing in this packet is self-executing.**
