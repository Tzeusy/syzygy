# Owner decision packet — the shape-to-spec impact craft act (P-42)

> **This file decides nothing.** Bounded packet, in the fixed seven-part
> shape: question, current authority, options, recommendation, costs, which
> digest would change, exact next transaction. **No history chain** — the
> reviews are named once as provenance, not narrated.
>
> **The subject was reviewed `REVISE` and then repaired; the repair is
> unreviewed.** RD-51 returned **`VERDICT: REVISE`** over the joint
> `CC-SPEC`/`CC-IMPACT` subject; the disposition register grades its twenty
> findings 15 repaired, 4 repaired in part, 1 deliberately open — repaired
> **by the session that read the verdict**, and a repair session cannot
> confirm its own repairs. This packet does not ask the owner to approve
> unrepaired or unreviewed bytes. Read the options with that in front.
>
> Repaired 2026-08-16 against review **RD-64** (`REVISE`,
> `../contracts/candidates/round-2026-08h/reviews/RD-64-p42-impact-packet-RAW.md`);
> the repaired packet has had no fresh read.

## Question

When a **shape** changes — a contract clause, an owner decision, a craft
policy — what finds the specifications that change with it?

Launch-gate **E6** asks exactly this. Today the propagation path's *detection*
step has no owner: steps 3 and 4 (judge honestly; update in the same logical
change) are carried by `VIS-2` and `CC-REV-2`, and **step 2, the reverse-
reference sweep, is carried by nothing citable.** It is proposed in a candidate
workflow whose own disclaimer says its sweeps *"do not exist as checks yet"*,
and its denominator discipline is repository operating procedure, which
`AGENTS.md` says of itself is never citable as authority.

So `E6` cannot be answered `Met` by citation. That is the gap.

## Current authority

| | |
|---|---|
| Candidate that would close it | `../contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md` — `CC-IMPACT-1…7` |
| The trigger set it uses | `CC-IMPACT-2`, stated as a **set identity** with `CC-SPEC-2`'s six warrant classes rather than a second enumeration that could drift |
| The blind exercise it requires | `CC-IMPACT-7`, naming its fixture by path and sha256 |
| What already has an owner | `VIS-2` (absence renders Unknown), `CC-REV-2` (every invalidated artifact updated in the same logical change) |
| Offered jointly with | **`P-41`**, the specification-acceptance policy — the two are one model and were repaired together |
| Provenance | launch-gate `E6`; `round-2026-08f/reviews/RD-51-spec-acceptance-and-impact-RAW.md` (verdict `REVISE`); the graded blind run `RD-59` (`round-2026-08g/reviews/`) |

`CC-IMPACT-*` is **candidate craft policy**. It binds nothing today.

## Options

- **(a) Review, then act.** Commission the fresh-context review of the
  repaired `CC-SPEC` + `CC-IMPACT` bytes as one combined subject, disposition
  its findings, then perform `CONFIRM CRAFT AMENDMENT` over the reviewed
  digest. `E6` becomes answerable by citation.
- **(b) Act without the review.** Perform the craft act over the current
  bytes. Fastest, and it accepts a policy whose most recent repair no session
  independent of the repair has read.
- **(c) Decline the rule, and record it.** Record a ruling that the first
  specification may be authored with no owned propagation rule, and that `E6`
  is `Not met` by decision rather than by omission. **This does not license
  a launch through the gate as written:** the instrument's §4 formula
  requires every E question `Met` for `READY FOR <target>` and for
  `READY-WITH-DEFERRALS` alike, and the E conjuncts are never deferrable
  (only F2 is) — so (c) also means either amending the instrument (P-34's
  subject) or not seeking a `READY` verdict.
- **(d) Defer.** No ruling; `E6` stays unanswerable and the reason is not
  recorded anywhere an administrator can cite.

## Recommended option

`[Inferred]` **(a)**.

The clause set exists and has been exercised, which is the part that usually
does not happen: `CC-IMPACT-7`'s blind propagation run was **administered**,
not merely specified, and it **passed** — while measuring that a
contract-only sweep would have missed **4 of 6** affected requirements, and
finding two defects in the fixture itself. That is real evidence the rule is
worth adopting.

It is also evidence the bytes have moved recently, which is why (b) is not
recommended: this repository's own rule is that a repair session cannot
confirm its own repairs, and the last hands on these clauses were the repair's.

(c) is a lawful and honest posture — `E6` `Not met` **by recorded decision** is
strictly better than `Not met` by silence — but under the instrument as
written it forecloses any `READY` verdict, so it pairs with amending the
gate (P-34), not with launching past it. (d) is the only option that leaves
an administrator with nothing to cite.

## Costs

| | |
|---|---|
| **(a)** | one fresh-context review over the combined `CC-SPEC` + `CC-IMPACT` subject, its disposition pass, then the act. The review is the cost; the act is minutes |
| **(b)** | minutes, and a policy in force that no independent reader has checked. The known-open findings below travel into force with it |
| **(c)** | one recorded decision — and no administration can return `READY` while `E6` is `Not met` (§4: every E question `Met`; E conjuncts never deferrable) |
| **(d)** | zero now; `E6` unanswerable at the formal administration, with no reason on record |

**Known open findings that travel with (b)**, stated so the option is not
chosen blind:

- `RD-51 f14` — **the one deliberately open finding**: no clause tests a
  specification for **completeness** against its capability.
- `RD-51 f15` — **repaired in part**: *"applicable"* is undefined, and the
  reviewed-N/A rule's identifier is unresolved.
- the undefined term *"consumes its vocabulary"* inside `CC-IMPACT-2`'s
  second trigger limb — the policy flags it against itself (`[Unknown]`,
  RD-51's G section), and it governs one of the sweep's two limbs.
- `CC-IMPACT-7`'s fixture carries two known defects (one warrant class
  entirely unexercised; the clauses it exercises are not stated in it).
  Their supersession by a fixture 3 is **filed as work, not done** — today
  only fixture 2 and its round-08e predecessor exist; the fixture is never
  edited, because its digest binds a completed run.

## Which digest would change

**No contract module and no wave manifest.** `CC-IMPACT-*` is craft policy,
not a contract wave: neither Wave A's nor Wave B's manifest digest moves under
any option, and neither confirmation is retired.

What the act binds is the **policy file's own digest, computed at the act**
(the `CC-TEST-2` precedent). Under (a) that digest is the reviewed one; under
(b) it is today's. Under (c) and (d) no act is performed, so no digest
binds — that absence is the recorded state, not an oversight.

Verify before acting, from the repository root:

```sh
python3 scripts/check_governance.py
sha256sum .syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md \
          .syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md
```

## Exact next transaction

**Do not rule `P-42` alone.** It is offered jointly with **`P-41`**: the two
policies are one model — `CC-IMPACT-1`'s spec-level declaration is *generated*
as the union of `CC-SPEC-2`'s six fields — and adopting either without the
other leaves a dangling generation. The coupling drags in P-41's own
prerequisite: **P-40 must be ruled first**, because the joint subject
includes `CC-SPEC-1`, which states of itself *"This clause may not be
frozen before P-40 is ruled."* One further coupling is disclosed, not
blocking: `CC-IMPACT-6` hard-points at the separately offered **P-44**
(the CC-REV-2 lagging-specification amendment); its review is part of this
combined review, and adopting `CC-IMPACT-6` creates no lag alternative on
its own.

Under **(a)**, in order:

1. **rule `P-40`** (the prerequisite above);
2. commission one fresh-context review of both files as a single subject,
   given the artifacts, their governing references and the acceptance
   criteria, and nothing else;
3. store the raw output verbatim and disposition every finding
   `repaired` · `open` · `declined`;
4. **freeze the bytes** and compute the digest;
5. perform `CONFIRM CRAFT AMENDMENT` over that digest, for both files. No
   `CC-SPEC`/`CC-IMPACT` act row exists in the acceptance record yet — the
   act and its ceremony phrase are minted at the offering (the precedent
   is act 2, `CONFIRM CRAFT AMENDMENT: CC-TEST-2@…`).

Under **(b)**: freeze today's bytes, compute the digest, perform the act
over them for both files, and record it in the craft `INSTALL-RECORD.md` —
with the register's open findings above traveling into force.

Under **(c)**, the transaction is one row in `SURFACE-DECISION-RECORD.md`
stating that the first specification may be authored with no owned propagation
rule, and that `E6` is `Not met` by decision — naming the no-`READY`
consequence stated under Options.

## Earliest required gate

**Before the first specification is authored.** A propagation rule adopted
after specifications exist is adopted after the first amendment it was meant
to govern.
