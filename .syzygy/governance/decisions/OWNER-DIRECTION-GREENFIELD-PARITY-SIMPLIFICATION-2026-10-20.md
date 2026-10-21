# Owner direction — greenfield-parity simplification of the implementation plane

Date: 2026-10-20

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-GREENFIELD-PARITY-SIMPLIFICATION-2026-10-20`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in the
family of `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`. It binds
no artifact digest, adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers
nothing in `scripts/check_governance.py`. It signs nothing, adopts nothing
and edits no signed byte.

## The owner's words

[Observed: the owner's message to a Claude Code session on 2026-10-20 at
15:48 UTC. The message is in that session, not in this repository.] The
message, verbatim:

> Please take the position of an auditor for this codebase. Evaluate the goal/vision and the ensuing estimated complexity of a *greenfield* project for these specifications, then reconcile the existing complexity against that. We've had several /th-projects relentless-vision-pursuit runs trying to improve simplicity; I want to ensure the health of the codebase is on the right track regarding keeping this as simple, maintainable, and modular/extensible as possible. *this is not in production* - everything is up for refactoring if it means making this project one that you can be proud of; and one that reviewers will be able to admire the code of, rather than critiquing it as an overly verbose vibe-coded mess.
>
> After having gathered a full list of improvements, concretize them as /beads-orchestration beads-writing beads; be sure not to duplicate your work against any already-existing beads, and also be sure to write these in a way that is modular and progressively implementable. If any large-scale changes are advised (totally acceptable if so), note the ensuing complexity in beads details so a model of appropriate complexity is used to handle it.

## How the session read it

[Inferred: the reading below is the session's, not the owner's words. The
owner is asked to confirm it, as question Q0 of the packet in item 4.]

[Added 2026-10-21: the owner confirmed this reading (GP-Q0, option "Confirm
all three"), added a CC-REV-1 review rule, kept six of item 4's seven topics
at the status quo and approved seven output-changing beads. Item 4 is narrowed
accordingly. The answers are recorded in
`OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`; the text below is
unchanged.]

1. **The audit is a recorded review.** Its report is
   `docs/plans/2026-10-21-greenfield-parity-audit.md`. Each finding there
   carries an identifier and evidence, and the beads under epic
   `syzygy-bpyt` trace to those identifiers.
2. **Behavior-preserving refactors may proceed.** They cover the
   implementation plane: `apps/**`, `packages/**`, `scripts/**`, tests, CI
   and root manifests. They run under the implementation acts and
   directions already in force, which `PROJECT-STATUS.md` names.
   "Behavior-preserving" means that none of the following changes:
   - a rendered byte, a wire format, a refusal string or an exit code;
   - a signed or digest-bound artifact;
   - a consent, security or retention decision.
3. **POC refactors count as improvement-cycle work.** Read with
   `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`, the audit is the
   cycle's recorded review. Its POC beads are admitted although a pure
   refactor does not "alter the runnable demonstration", because the owner
   put "everything" up for refactoring. That direction's other rules stand:
   - WIP one for POC shared-model changes;
   - each cycle is reported to the owner before the next one starts. The
     audit's convergence bead, `syzygy-bpyt.10`, is that report.
4. **Everything else goes to the owner in one sitting.** That covers:
   - retiring spent governed material;
   - the installed/candidate RFC mirror;
   - an evidence retention rule;
   - moving code out of `.syzygy/**`;
   - the record format the consent gate parses;
   - the dossier's execution-permitting arm;
   - the parked provider code.

   Each is put to the owner as one question in a single plain-language
   packet (bead `syzygy-bpyt.1.1`) and done only as answered.

## What this does not do

- It signs, adopts or accepts nothing (VIS-4).
- It amends no doctrine, contract, policy or specification, and edits no
  digest-bound file.
- It deletes no parked code. The provider routes and egress packages stay
  parked as `OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`
  says.
- It lifts no standing prohibition in `AGENTS.md`. Butlers bodies are still
  read only under the consent acts. Nothing is released or deployed, and
  agent coordination is still never unattended.
- It authorizes no new behavior. A change that would alter behavior is out
  of scope, even when it is simpler, and goes to the owner.

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
A "no" to Q0 withdraws the reading in items 2 and 3 for any bead not yet
merged.
