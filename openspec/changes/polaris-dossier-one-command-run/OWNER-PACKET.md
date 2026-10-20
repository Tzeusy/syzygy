# Owner packet — one-command Polaris dossier run

> **Candidate — binds nothing.** Questions for you, each with a
> recommendation. Nothing here is decided, and no act is offered until a
> fresh-context review confirms these bytes.

## What you asked for, and what it takes

You asked that a Syzygy user run one command and get a Polaris dossier, with
the independence rules settled inside Syzygy's workflow rather than by you
starting each session (operator session, 2026-10-14; quoted in
`proposal.md`). The draft does this with six additions to the Polaris spec:
one command for the whole run (040); Syzygy, not you and not the authoring
agent, starts every session (041); each session sees only what its role needs,
enforced by the operating system (042); one terminal view for everything
(043); launched runs never execute the observed project (044); and each
session is your own local `claude` or `codex` binary, started with explicit
inputs only and no SDK or API tooling (045).

**Your doctrine already allows this; three of your own directions do not.**
Vision says Syzygy "harnesses the existing actuator toolchain" and
"integrates" orchestration tools, and the loop stays human-triggered by your
one command. What forbids it is narrower and is yours to change by direction:

- 2026-10-08, waiting sessions: "**No Syzygy-launched sessions.**" You chose
  option B over option D, which was this.
- 2026-10-03, item 2: "the product still coordinates no agents."
- 2026-10-05, item 2: the fidelity review "runs in a separate top-level
  session that the operator starts" (and REQ-035, which extends that to all
  three helper sessions).

**What changes in what you can trust.** Today who started each session is
your declaration (Inferred), and any session could write another's directory
or the gate records. In a launched run Syzygy records each launch itself
(Observed), and the operating system keeps each session out of the others'
directories and the records read-only. That is stronger independence than
today, not weaker. What stays Inferred: the model actually served, that each
context was fresh, and that the view held for the session's whole life.

## Questions

**Q0. Record the request as an owner direction.** *Answered yes 2026-10-14
(`decisions/POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`).*
Recommendation: yes, as `POLARIS-DOSSIER-ONE-COMMAND-RUN-2026-10-14`, a plain
direction that directs this draft and performs no act. Without it this
draft has no warrant and no review of it counts.

**Q1. Supersede the three directions for launched runs only.** *Answered
yes 2026-10-14, same direction.*
Recommendation: yes, and only for runs started with `syzygy polaris`. The
operator-started flow, its launch forms and REQ-035 stay exactly as signed.
Alternative: supersede them outright and retire the operator-started flow;
not recommended while execution runs (D9) still need it.

**Q2. Whose act are the agents' provider transmissions in a launched run?** *Answered with the recommendation 2026-10-14 (direction follow-up).*
REQ-033 says Syzygy makes "no model-provider call" and that the sessions'
transmissions are "the operator's own act". The 2026-10-08 packet warned that
if Syzygy launches, the "no provider call" disclosure "turns false". This
packet's drafter added that RFC7-20 and the public egress record would then
apply; that addition is not in the 2026-10-08 packet.
Recommendation: rule that a launch Syzygy makes on your one command, of your
own agent tool, under your own account, with the agent tool and provider you
declared, keeps the transmissions your own act; Syzygy still makes no
provider call, resolves no route and sends no content itself. The pages say
so. Alternative: treat launched runs as Syzygy egress under RFC7-20, which
needs an egress record per provider before any launched run.

**Q3. New change, or v1.3 of the local-agent mode?** *Answered with the recommendation 2026-10-14 (direction follow-up).*
Recommendation: a new change, as drafted, following the arbitrary-repo
precedent: added requirements that name the exact predecessor text they
displace, no byte of REQ-033 to 036 edited. Alternative: a v1.3 amendment
package of `polaris-dossier-local-agent-mode` through CC-REV-2.

**Q4. Refuse launched runs where isolation cannot be built?** *Answered with the recommendation 2026-10-14 (direction follow-up).*
Recommendation: yes, fail closed and point to `syzygy dossier init`. A
launched run without isolation would be weaker than today, because nobody
would be attending each launch. [Observed 2026-10-14 on this host:
bubblewrap 0.11.1 builds an unprivileged view.]

**Q5. May a launched run continue while you are detached?** *Answered with the recommendation 2026-10-14 (direction follow-up).*
Recommendation: yes, but only through reading, checking, freezing,
delivering and rendering, with each detached interval recorded; no session
gains any permission while detached. This is the "walk away" you asked for,
and it is within what the waiting-sessions direction already allowed ("an
unattended stretch of a run is a reading-only stretch").
Alternative: pause the run whenever no operator is attached.

**Q6. The command's name.** *Answered with the recommendation 2026-10-14 (direction follow-up).*
Recommendation: `syzygy polaris <url>`, your words, with `--resume <run>`.
Alternative: `syzygy dossier run <url>`, beside the existing subcommands.

**Q7. Which agent tools first?** *Answered with the recommendation 2026-10-14 (direction follow-up).*
Recommendation: Claude Code first, since its provider statement and the
waiting-session tool rules exist; Codex once its statement is in force.

**Q8. How does Syzygy start each session?** *Answered 2026-10-15
(`decisions/OWNER-DIRECTION-DOSSIER-LOCAL-CLI-SUBPROCESS-2026-10-15.md`).*
In your words: "Syzygy should run *our local codex or claude cli binary* like
a subprocess with explicit workspace/instructions/artifacts path and
skill/mcp guidance, no custom SDK or API tooling". REQ-045 writes that down.
It was reviewed separately in five rounds and was cleared at round 5 with
notes only; those notes are carried into this text.

**Q9. Content classes the provider statement does not list.** *Answered
2026-10-15, "Repair + disclose"
(`decisions/OWNER-DIRECTION-DOSSIER-CLI-RUNNER-REPAIR-AND-DISCLOSE-2026-10-15.md`).*
A launched run is not refused for them. The run page lists the classes
present, marks the unlisted ones, and says the tool may have sent them.
Syzygy's own packets carry only the classes the statement lists.

What is still missing for Codex: no agent-provider statement for Codex is in
force for any target, so REQ-045 refuses a Codex run until one is.

## Acts, in order

1. Q0 and Q1 as one plain owner direction (binds no digest).
2. Q2 to Q7 answered in that direction or a follow-up.
3. Fresh-context review rounds over these bytes.
4. This spec, REQ-045 included, signed once by version tag
   (`scripts/record_versioned_signoff.py`); register row P-111 Q1.
