# Owner decision packet — public-source screening scope

> **Candidate — binds nothing.** It carries no digest. Nothing here is a
> decision, and no act is performed by reading it. It is offered only after a
> confirming review.

## What this is

Before the generator may read any public repository, `project:syzygy` needs a
screening policy that covers one. The existing policy covers only Butlers and
refuses most source code. This package adds one scope to the same policy (see
`SEMANTIC-DELTA.md`), which is the "once" item of the public admission
package.

## The act

An `approve-policy` act over the proposed policy bytes, at the package
manifest's row. Form: an option in a structured question, state (1)
`owner-adopted (bootstrap, uncorrelated)`, as for the 2026-10-02 policy
re-pin [Inferred: the same form fits]. A recorder is written after the review.

## Questions

**Q1. Sign this scope?** *Recommended:* yes, after a confirming review.

**Q2. Read-gate continuation.** An act over these bytes makes the Butlers
read gate refuse the policy until its pinned version and act record are
re-pointed. *Recommended:* the same direction as the 2026-10-02 re-pin: the
change that records the act re-points the gate in the same commit, with its
tests. The alternative, no version bump, leaves a changed file under an
unchanged label, which this package does not offer.

**Q3. Source extensions.** The `code-content` list is a proposal [Inferred].
*Recommended:* accept it; a file outside it is refused egress, never guessed.

**Q4. Order against PR #120.** Either act may land first; the second is
regenerated and re-reviewed. *Recommended:* whichever is ready first.

## What it does not do

It admits no repository, grants no read or egress, defines no content class,
and changes nothing for Butlers.
