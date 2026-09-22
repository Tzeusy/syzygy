# Polaris gate packages — the owner's answers to the open questions left by the first 2026-09-23 sitting (`syzygy-dov.21`, `.18`)

> **Plain owner direction. Performs no act.** This record answers the open
> questions that `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
> (this directory) left unput: `.21` OQ-3, OQ-4 and OQ-5, and `.18` open
> questions 1, 2, 4, 5 and 6. That earlier record is not edited; its
> sentences saying these questions "stay open" were true when written and
> are answered here. This record binds no digest, amends no specification,
> policy or registry byte, adds no row to `ACCEPTANCE-ACT-RECORD.md` and
> registers nothing. Each package still takes effect only through its own
> owner act, after its own review.

## How the answers were given

Date: 2026-09-23. Owner: Tzeusy. Channel: the Claude Code CLI, the same
sitting as the earlier record. The owner asked for recommendations ("Let's
solve those too, what do you recommend?"), and then answered structured
questions in two batches. Each answer below is the option label the owner
selected, quoted byte-for-byte. The owner made no edits and added no notes.
Every selection was the option presented as recommended.

Evidence snapshot: Syzygy `origin/main` at `39bc2dc`. The questions were
presented from the two packets' own open-question sections. They were not
re-reviewed adversarially before presentation. Each package still owes the
review its packet names.

## 1. Opening-band aggregate scenario — `syzygy-dov.21`

Packet: `contracts/candidates/pwb-opening-band-scenario/OWNER-DECISION-PACKET.md`.

| Question | Owner's answer (verbatim) |
|---|---|
| OQ-3: the band counts only primary Unknown reasons; PWB-REQ-007 requires separate primary and secondary counts. Which gives way? | "Keep clause; code adds secondary (Recommended)" |
| OQ-4: may an opening aggregate exist at all under POC-REQ-032's "in place"? | "Clarify inside .26 (Recommended)" |
| OQ-5: block order at the top of the Polaris page (reserved to the owner by P-71 Q7) | "Account first, then band (Recommended)" |

Reading:

- **OQ-3.** The scenario keeps PWB-REQ-007's "separate primary/secondary
  reason counts" unchanged, and slice 3's implementation supplies the
  secondary counts. No PWB-REQ-007 amendment is sought. [Observed] The
  core model already computes a secondary reason count per aggregate:
  `project-shape-model.test.ts` asserts `reasonCounts` with both `primary`
  and `secondary` keys. Only the Polaris gap-reason projection drops the
  secondary count.
- **OQ-4.** Whether a conforming rendering may carry an opening aggregate
  under POC-REQ-032 will be settled by a clarification of that requirement
  inside the P-75 Q1 three-surface package at gate `syzygy-dov.26`. This
  is the same package that OQ-1 already routes slices 4 and 5 to. Slice 3
  waits for that clarification. The `.21` package does not read
  POC-REQ-032 itself.
- **OQ-5.** As presented, the option read: "Purpose, promises, non-goals,
  architecture, V1 scope and success criteria come first, as PWB-REQ-010
  requires. The band comes next, before the first catalog: the currency
  probe, then the Unknown aggregate." So the order is:
  1. PWB-REQ-010's project-level categories, first.
  2. The opening band, before the first catalog. Inside the band, the M2
     currency probe comes first and the project-shape Unknown aggregate
     second.

  This settles the order that P-71 Q7 reserved to the owner. It is a
  design value for slices 2 and 3, not a specification sentence. The
  scenario's own wording ("displaces and defers no project-level category
  of this requirement") is compatible with it and stays unchanged.

## 2. Registry currency bounds and briefing ceiling — `syzygy-dov.18`

Packet: `contracts/candidates/pwb-registry-currency-briefing-amendment/OWNER-DECISION-PACKET.md`,
section "Open questions this package did not resolve".

| Question | Owner's answer (verbatim) |
|---|---|
| 1: does M11's breach recording cover the new third ceiling (briefing response) as well as the two existing ones? | "Yes, all three (Recommended)" |
| 2: do the new registry fields stay outside P-77 Q6's parity sweep? | "Confirm: outside sweep (Recommended)" |
| 4: the truth-policy builder's check goes red at adoption because its subject bytes move — handling? | "Retire it in the adoption change (Recommended)" |
| 5: is the thirteen-class set permanently complete? | "No; new class needs amendment (Recommended)" |
| 6: what is the "one named subject" the briefing ceiling bounds? | "Hold for .22 review (Recommended)" |

Reading:

- **1.** M11's breach recording extends to every ceiling the registry
  declares, including the briefing response ceiling once the `.18` act adds
  it. P-78 Q4's "the two ceilings" is read as describing the registry at the
  time of that ruling, not as limiting recording to two.
- **2.** The drafter's reading is confirmed. The currency bounds and the
  briefing ceiling are registry configuration, not machine-response fields.
  They are therefore outside P-77 Q6's parity sweep and need no family
  there. A future machine field that *serves* one of these values would be
  inside the sweep.
- **4.** The change that applies the `.18` act also retires or rebases
  `scripts/build_pwb_truth_policy_amendment.py`'s check, so that the battery
  never shows a red without a defect behind it. This extends the
  superseded-recorder convention to that builder by the owner's ruling. It
  does not authorize editing any performed record.
- **5.** The thirteen classes are complete against today's two source files,
  and they are not a closed set. A new claim class needs a registry
  amendment. Until it has a row, `undeclaredClass` makes it Unknown. An
  agent may add a mechanical check that every minted class has a registry
  row. That check is ordinary engineering and needs no further act.
- **6.** Held. The drafter's leaning, one claim id, goes to the `.22`
  reviewer as input only. The owner decides when that review returns.

## What this does not do

It performs no act, offers no phrase, and authorizes no implementation
beyond what existing acts already cover. It waives no review. It does not
amend POC-REQ-032, PWB-REQ-007 or PWB-REQ-010. It leaves `.18` open
question 6 open.
