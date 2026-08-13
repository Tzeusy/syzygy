# Owner decision packet — the shape-to-spec impact craft act (P-42)

> **This file decides nothing.** Bounded packet, in the fixed seven-part
> shape: question, current authority, options, recommendation, costs, which
> digest would change, exact next transaction. **No history chain** — the
> reviews are named once as provenance, not narrated.
>
> **The subject is unreviewed.** Its most recent repair has had no
> fresh-context review, and this packet does not ask the owner to approve
> unrepaired or unreviewed bytes. Read the options with that in front.

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
| Provenance | launch-gate `E6`; `round-2026-08g/reviews/RD-51-*`; the graded blind run `RD-59` |

`CC-IMPACT-*` is **candidate craft policy**. It binds nothing today.

## Options

- **(a) Review, then act.** Commission the fresh-context review of the
  repaired `CC-SPEC` + `CC-IMPACT` bytes as one combined subject, disposition
  its findings, then perform `CONFIRM CRAFT AMENDMENT` over the reviewed
  digest. `E6` becomes answerable by citation.
- **(b) Act without the review.** Perform the craft act over the current
  bytes. Fastest, and it accepts a policy whose most recent repair no session
  independent of the repair has read.
- **(c) Launch knowingly without it.** Record a ruling that the first
  specification may be authored with no owned propagation rule, and that `E6`
  is `Not met` by decision rather than by omission.
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
strictly better than `Not met` by silence, and it is the right choice if the
owner judges the review cost not worth paying before launch. (d) is the only
option that leaves an administrator with nothing to cite.

## Costs

| | |
|---|---|
| **(a)** | one fresh-context review over the combined `CC-SPEC` + `CC-IMPACT` subject, its disposition pass, then the act. The review is the cost; the act is minutes |
| **(b)** | minutes, and a policy in force that no independent reader has checked. The known-open findings below travel into force with it |
| **(c)** | one recorded decision. `E6` is permanently `Not met` until someone reopens it, and every future administration records it |
| **(d)** | zero now; `E6` unanswerable at the formal administration, with no reason on record |

**Known open findings that travel with (b)**, stated so the option is not
chosen blind:

- `RD-51 f14` — no clause tests a specification for **completeness** against
  its capability.
- `RD-51 f15` — *"applicable"* is undefined, and the reviewed-N/A rule has a
  circular home.
- `CC-IMPACT-7`'s fixture carries two known defects (one warrant class
  entirely unexercised; the clauses it exercises are not stated in it). It is
  **superseded by a fixture 3, never edited** — its digest binds a completed
  run.

## Which digest would change

**No contract module and no wave manifest.** `CC-IMPACT-*` is craft policy,
not a contract wave: neither Wave A's nor Wave B's manifest digest moves under
any option, and neither confirmation is retired.

What the act binds is the **policy file's own digest, computed at the act**
(the `CC-TEST-2` precedent). Under (a) that digest is the reviewed one; under
(b) it is today's.

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
other leaves a dangling generation.

Under **(a)**, in order:

1. commission one fresh-context review of both files as a single subject,
   given the artifacts, their governing references and the acceptance
   criteria, and nothing else;
2. store the raw output verbatim and disposition every finding
   `repaired` · `open` · `declined`;
3. **freeze the bytes** and compute the digest;
4. perform `CONFIRM CRAFT AMENDMENT` over that digest, for both files.

Under **(c)**, the transaction is one row in `SURFACE-DECISION-RECORD.md`
stating that the first specification may be authored with no owned propagation
rule, and that `E6` is `Not met` by decision.

## Earliest required gate

**Before the first specification is authored.** A propagation rule adopted
after specifications exist is adopted after the first amendment it was meant
to govern.
