# Owner decision packet — the shape-to-spec impact craft act (P-42)

> **This file decides nothing.** Bounded packet, in the fixed seven-part
> shape: question, current authority, options, recommendation, costs, which
> digest would change, exact next transaction. **No history chain** — the
> reviews are named once as provenance, not narrated.
>
> **The subject has been through two review rounds; the final blocker
> repair awaits its confirming review.** RD-51 returned
> **`VERDICT: REVISE`** over the joint `CC-SPEC`/`CC-IMPACT` subject and
> was repaired; the combined fresh-context review **RD-69** (2026-08-17)
> then returned **`VERDICT: REVISE`** with one launch blocker (against
> CC-SPEC-8, repaired same day — no CC-IMPACT clause was found blocking)
> and five non-blocking findings. The one confirming review **RD-70**
> (2026-08-17) returned **`VERDICT: CONFIRM WITH EXCEPTIONS`**: the
> blocker is cleared, no new blocker, four further non-blocking findings
> batched. The review cycle is closed; the open findings travel with the
> offer, disclosed. Read the options with that in front.
>
> Repaired 2026-08-16 against review **RD-64** (`REVISE`,
> `../contracts/candidates/round-2026-08h/reviews/RD-64-p42-impact-packet-RAW.md`);
> the repaired packet has had no fresh read. **Updated 2026-08-17 to
> offering-ready state**: the subject's review cycle closed and act 7 was
> minted at the offering.

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

- **(a) Act — the review half is done.** The combined fresh-context
  review ran (RD-69), its one blocker (against the sibling CC-SPEC file)
  was repaired, and RD-70 confirmed the repair; no CC-IMPACT clause drew
  a finding in either round. Perform **act 7** jointly with **act 6**
  (acceptance record §1; the exact phrase lives there —
  `CONFIRM CRAFT AMENDMENT: CC-IMPACT@…` over this file's own digest,
  which RD-70 verified byte-unchanged through the cycle). `E6` becomes
  answerable by citation.
- **(b) — discharged by events.** This arm was "act without the review";
  the review has now happened, so (b) no longer describes a real
  alternative and is retained only so the option lettering stays stable.
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

The bytes have now had two independent fresh-context reads (RD-69 and
RD-70) — the CC-IMPACT file is byte-unchanged through both, and the one
blocker found in the cycle lived in the sibling CC-SPEC file and was
repaired and confirmed. What remains for the owner is the act itself.

(c) is a lawful and honest posture — `E6` `Not met` **by recorded decision** is
strictly better than `Not met` by silence — but under the instrument as
written it forecloses any `READY` verdict, so it pairs with amending the
gate (P-34), not with launching past it. (d) is the only option that leaves
an administrator with nothing to cite.

## Costs

| | |
|---|---|
| **(a)** | minutes — the review and its disposition pass are done; what remains is verifying the digests and performing acts 6 + 7 in one sitting |
| **(b)** | discharged by events — the review this arm proposed skipping has happened |
| **(c)** | one recorded decision — and no administration can return `READY` while `E6` is `Not met` (§4: every E question `Met`; E conjuncts never deferrable) |
| **(d)** | zero now; `E6` unanswerable at the formal administration, with no reason on record |

**Known open findings that travel with the act**, stated so it is not
performed blind:

- `RD-51 f14` — **repaired 2026-08-17** (CC-SPEC-11, the bounded coverage
  model); RD-69 raised no finding against it, and the confirming review of
  the same-day blocker repair has the last word.
- `RD-51 f15` — **repaired 2026-08-17, twice**: the first repair defined
  *"applicable"* but wrongly declared CC-SPEC-8 the reviewed-N/A rule's one
  home (RD-69's launch blocker); the blocker repair reduced CC-SPEC-8 to a
  citation of the nine contract modules that own the rule. Awaits the
  confirming review.
- `RD-69`'s five non-blocking findings (N1–N5, dispositioned open in
  `../contracts/candidates/round-2026-08i/reviews/RD-69-DISPOSITION-REGISTER.md`).
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
other leaves a dangling generation. P-41's own prerequisite is
**satisfied**: P-40 was ruled 2026-08-16 (SDR-37), and `CC-SPEC-1` was
re-grounded on the recorded ruling in the 2026-08-17 amendment — the
freeze conditional it used to carry is discharged. One further coupling
is disclosed, not
blocking: `CC-IMPACT-6` hard-points at the separately offered **P-44**
(the CC-REV-2 lagging-specification amendment); its review is part of this
combined review, and adopting `CC-IMPACT-6` creates no lag alternative on
its own.

Under **(a)**, in order:

1. ~~rule `P-40`~~ — **done, 2026-08-16 (SDR-37)**;
2. ~~commission one fresh-context review of both files as a single
   subject~~ — **done, 2026-08-17**: RD-69 (three subjects, the P-44
   offer included), one blocker, repaired; RD-70 confirming;
3. ~~store the raw output verbatim and disposition every finding~~ —
   **done**: `../contracts/candidates/round-2026-08i/reviews/`;
4. ~~freeze the bytes and compute the digest~~ — **done**: both act
   arguments stand in the acceptance record §1 (**acts 6 and 7**, minted
   2026-08-17 at this offering per the act-2 precedent), checked live by
   `check_governance.py` CG-7d;
5. **remaining:** run the verify block above — a `sha256sum` mismatch
   against the act arguments means the bytes moved, the reviews are
   retired, and the act stops — then perform **act 6** and **act 7** in
   one sitting, recorded in the craft `INSTALL-RECORD.md`.

Under **(b)**: discharged by events — the review this arm would have
skipped has happened; its remaining content is identical to (a) step 5.

Under **(c)**, the transaction is one row in `SURFACE-DECISION-RECORD.md`
stating that the first specification may be authored with no owned propagation
rule, and that `E6` is `Not met` by decision — naming the no-`READY`
consequence stated under Options.

## Earliest required gate

**Before the first specification is authored.** A propagation rule adopted
after specifications exist is adopted after the first amendment it was meant
to govern.
