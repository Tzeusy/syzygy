# Owner direction — the Butlers machine-answer ceiling: raise it first, then serve governedBy once

Date: 2026-10-15

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-MACHINE-CEILING-2026-10-15`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in the
family of `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`. It binds
no artifact digest, adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers
nothing in `scripts/check_governance.py`. It signs nothing, authorizes no
implementation and edits no signed byte. It directs what is drafted, and in
what order.

## The owner's words

[Observed: the question and the selection as the lead Claude Code session
relayed them to the drafting lane. The owner's answer itself is in that
session, not in this repository.] On 2026-10-15, in the lead Claude Code
session, the owner answered a structured question.

The question, verbatim:

> P-100 merged, and the live Butlers machine answer (/api/poc) is now 7.93 MB of its 8 MB ceiling (94.5%). Past the ceiling the daemon serves a bare 503 and logs nothing. Each new Butlers bead adds ~450 bytes, so roughly 1,000 more beads breaches it, and P-86 adds project-shape bytes too. The ceiling sits in the adopted Butlers registry entry, so changing it, or changing how governedBy is served, needs your sign-off. What should I do?

The owner selected "Both, ceiling first (Rec.)", whose option text was:

> Now: a registry-entry amendment raising maxMachineResponseBytes to 16 MiB, signed by version tag after one review. Then a POC-REQ-014 amendment serving the identical governedBy Unknown once per observation, by reference (~2 MB saved). P-86 waits for the raise.

Two statements in the question are no longer true, and the quotation
preserves them as asked. These notes were added 2026-10-20 and are not
the owner's words:

- "logs nothing": [Observed] since `86bbddc4` (2026-09-23) the daemon writes
  one `daemon-http-outcome` stderr line per ceiling breach, giving the limit
  and the declared and observed sizes (`packages/cap1-daemon/src/server.ts`,
  `emitNonSuccess`). Bead `syzygy-vqcc` corrects the AGENTS.md guardrail.
- "roughly 1,000 more beads": [Observed] five days later, on 2026-10-20, the
  machine answer was already 8,497,943 bytes and refused
  (`docs/evidence/syzygy-59s5-live-size-2026-10-20.json`).

## The direction

1. **The ceiling first.** Draft a registry-entry amendment that raises
   `maxMachineResponseBytes` in the Butlers observer registry entry to
   16 MiB, review it once, and offer it for a version-tagged sign-off.
   Package `contracts/candidates/pwb-registry-machine-ceiling-amendment/`,
   register row P-114.
2. **Then governedBy once.** Draft a POC-REQ-014 amendment that serves the
   identical governedBy Unknown once per observation, with items
   referencing it. As of 2026-10-20 its drafting has not started. P-115 is
   reserved for it and is not yet in the register.
3. **P-86 waits** for the raise.

## What this does not do

It signs neither package; each is offered to the owner after its review.
It authorizes no code change. The daemon hard-codes the ceiling, so the
raise takes effect only under a separate implementation authorization,
asked in the P-114 packet. It changes no check, no recorder and no other
registry field.

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
