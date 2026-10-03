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
read gate refuse the policy on its digest first and its version second. The
change that records the act would re-point exactly the list the simulation
script produces (impact ledger, "What the act breaks"), in the same commit,
with the tests: the gate's expected version, scope anchors, act identity,
recording tag and the act-record and superseded-record pointers in
`governance-inputs.ts`; the version copy in `git-object-reader.ts` and the value
`content-classification.ts` takes from it; the tests that assert them; the
`PROJECT-STATUS.md` battery lines and the two CI steps that carry the policy
digest; and the act-subject chain and digest-copy rows in `check_governance.py`.
*Recommended:* widen the owner's continuation from the gate alone to all of
those, as the 2026-10-02 re-pin did for its set. Not bumping the version would
not avoid the refusal.

**Q3. Source extensions.** The `code-content` list is a proposal [Inferred],
matched case-sensitively on the final path segment. *Recommended:* accept it; a
file outside it is excluded from reading and egress, never guessed. Note that
configuration written in a listed extension (`.config.js`, `setup.py`, `.sh`) is
`code-content`.

**Q4. Order against PR #120.** The ordering is asymmetric. If PR #120's act
lands first, this package needs only `--write` and a fresh review. If this one
lands first, PR #120 needs builder edits and a changed digest-bound consent.
Both used the label `1.2.0-candidate.1` for different bytes; this package now
uses `public-source-candidate.1`. *Recommended:* PR #120 first when both are
signed in one sitting; otherwise this one alone.

**Q5. Narrowing of Q2/Q7.** Your answers were "all but work-history" and "code
and specs only" for T1. This scope has no closed rule for specification and
design documents or committed reports, so they, README files and LICENSE files
are excluded from reading and from egress until `project-documentation` exists.
For T1 that leaves the source extensions. *Recommended:* accept the narrowing
rather than have a class guessed. The alternative is a later closed rule for
specification paths, offered with its own review.

**Q6. Active content stays as the base has it.** No loosening is proposed
[Inferred]: a body with markup-like bytes outside a valid inert code context is
withheld, so some target files will be. Two cases are worth naming: `.jsx` and
`.tsx` files contain element forms by construction and will nearly always be
withheld, though the list proposes a class for them; and an unmatched backtick
run (an unclosed inline span) excludes the whole artifact, so shell scripts with
command substitution, Go raw strings and JavaScript template literals of odd
backtick count are excluded independent of markup. *Recommended:* accept, run the
first target, and decide any loosening or any trimming of the list from the
measured counts as a later version.

**Q7. Which exclusion reasons may leave.** The rule carries a source's reason
only as one of the policy's two emitted classes (`excluded-artifact`,
`unclassifiable-excluded`). The generator also emits `oversize-source-excluded`
for a source that is too large, which no class lists, so that reason would be
refused. *Recommended:* add it to the closed list in this scope rather than
widen to free text.

**Q8. The run-profile carrier.** The rule classifies reader questions and
requested assets only as the values of the code-declared symbols in the
dossier profile, selected by a profile id a request carries. The base has no
request field for one, and the engine branch selects a profile by configuration
(`profile: "dossier"`), not by an id. Until you decide the id and its carrier,
nothing is classified under the rule and a request that carries reader
questions is refused. *Recommended:* decide the carrier when the dossier
engine lands, not here.

## What it does not do

It admits no repository, grants no read or egress, defines no content class,
and changes nothing for Butlers.
