# Owner decision packet — knowledge-hygiene craft policy (P-12, current packet)

> **This file decides nothing.** It is the current packet for **P-12**
> (previously round-2026-08d packet 10); the register row still owns the
> queue entry.

## Question

Confirm the **compact 10-rule knowledge-hygiene policy** as a craft
amendment (its own `CONFIRM CRAFT AMENDMENT` act), after independent
review?

## What the active rules cover (the compact set's territory)

```text
one fact, one home
active / history / derived lanes
terms are scarce
semantic-delta edits
fresh-context review
current-state generation
compiled context
clone reproducibility
measured claims
context/decomposition budgets
```

Examples and operational guidance stay **outside** the active rule set
(the compact policy's design: rules bind, appendices teach).

## Why it is launch-critical now

1. **`CC-BUDGET-1` is installed nowhere** until this act — the context
   budget threshold that specs will cite has no owning rule.
2. The launch-gate pilot's C2 finding: two repo-wide rules live only
   inside `check_governance.py` (CG-20/CG-21's "states no measurement").
   The 2026-08-10 repair downgraded those checks to advisory **until this
   policy is adopted** — the compact policy is their intended owning
   home, so adoption re-arms them lawfully.
3. F2 (governance proportionality) needs the lanes rule in force to make
   the reduction plan binding rather than aspirational.

## Current authority

None — both candidate versions sit in `policy-candidates/`
(`CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`, 22 rules; `…-COMPACT.md`, 10 rules
carrying the migration map, retiring twelve into named survivors,
renumbering nothing, adding exactly one listed obligation). The
launch-gate pilot noted (without failing on it) that offering two
labelled alternatives is legitimate pre-decision governance — but the
choice must land before specs cite the rules.

## Options

- **(a)** Confirm the **compact 10-rule** version, after a fresh
  confirming review of the compaction. *(Recommended.)*
- **(b)** Confirm the original 22-rule version — more maintenance
  surface; the migration map becomes unnecessary.
- **(c)** Neither — CC-BUDGET-1 stays orphaned; CG-20/21 stay advisory;
  the shadow-authority finding stands at every future administration.

## Recommendation

`[Inferred]` **(a)**, unchanged from round-08d packet 10, now with the
CG-20/21 re-arming consequence attached.

## Digest consequences and the exact next transaction

*(Added 2026-08-13, owner charter §16.)*

| Arm | Wave A / Wave B manifests | Confirmations | Side effect |
|---|---|---|---|
| **(a)** the compact 10-rule version | **unchanged** | **both survive** | `CG-20`, `CG-21` and `CG-27` stop being advisory and can fail the battery |
| **(b)** the original 22-rule version | unchanged | both survive | same re-arming; the migration map becomes unnecessary |
| **(c)** neither | unchanged | both survive | `CC-BUDGET-1` stays orphaned; the three checks stay advisory; the shadow-authority finding stands at every future administration |

**No arm touches a contract wave.** The consequence to weigh is not a digest —
it is that **three repository checks currently downgraded to WARN would begin
to fail**, because their rules would have a binding home. `CG-27` is new as of
2026-08-13 and enforces `CC-KNOW-11`'s currency limb over the default reading
path; it is clean today, and arm (a) or (b) makes that cleanliness load-bearing
rather than advisory.

**Pre-work required:** none. **Review required:** one fresh-context confirming
review of the compaction under (a) — specifically that the twelve retired
identifiers' obligations survive in their named absorbers, which is the claim
the migration map makes and the one a reviewer can check.

**Exact next transaction.** Under (a): commission that review; disposition it;
freeze the bytes; then `CONFIRM CRAFT AMENDMENT` over the frozen digest,
recorded in the craft `INSTALL-RECORD.md`. Under (c): a recorded decision
saying so, which is strictly better than leaving the question open — an
advisory check with a recorded reason is honest, one with none is drift.

## Earliest required gate

Its own craft act; **before OpenSpec** (specs will cite CC-BUDGET-1).

## Independent work

Yes.
