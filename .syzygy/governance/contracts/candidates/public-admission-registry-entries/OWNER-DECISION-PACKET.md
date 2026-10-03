# Owner decision packet — public-admission registry entries

> **Candidate — binds nothing.** Drafted 2026-10-03. Effect comes only from an
> owner act over an entry's exact bytes. A commit, a review or a passing check
> performs none. No target repository body has been read and no provider has
> been called.

## What this is

The public-repository admission package needs two registry entries before a
read or a model call can be lawful (REQ-polaris-generation-017; RFC4-1):

1. the **provider execution route** for Anthropic through the Claude Agent SDK
   runtime (`proposed/POLARIS-PROVIDER-ROUTE-ANTHROPIC-AGENT-SDK-CANDIDATE.json`);
2. one **shared public Git-hosting source-acquisition adapter**
   (`proposed/POLARIS-PUBLIC-GIT-SOURCE-ACQUISITION-CANDIDATE.json`).

Each is its own record with its own act. Signing either enables nothing by
itself: the implementation does not exist, and the egress consent, the
observation consents and the public-source screening scope are separate acts.

## How the acts would be given

The form proposed is the admission package's Q5 form: one structured question
whose option names the entries "at the manifest rows" of
`PUBLIC-ADMISSION-REGISTRY-MANIFEST.txt`, stated as provenance state (1),
`owner-adopted (bootstrap, uncorrelated)`, A1 audit-record identity absent. A
recorder binds each act to its row and refuses any other argument. This
follows the 2026-10-02 behaviour-contract re-pin, which re-pinned the Butlers
registry entry that way.

The version-tagged Scope A sign-off is not used [Inferred]. The direction
names "the PWB specification deltas, the observer registry entry and the
contract successors queued behind them", which reads as the Butlers project-
shape observer entry and its queue, and its recorder applies package patches
to an existing subject. These are two new files for different authorities,
and the admission package already signs its consents at manifest rows, so one
form across one sitting is simpler. If the owner reads Scope A as covering
any implementation-phase registry entry, the entries could instead be signed
by version tag; the bytes would not change.

## Questions for the owner

None is decided by this packet.

**O1. One shared source-acquisition adapter, or one per target?** *Recommended:*
one shared adapter. RFC4-1 requires exactly one registered adapter per
external authority per project, the hosting service is one such authority, and
a per-target entry would repeat the per-target cost the admission package
exists to remove. The cost: a change to the adapter is a new entry version
that affects every target.

**O2. Resource limits for the acquisition adapter.** The entry proposes 4,096
sources, 1 MiB per source, 128 MiB total, 256 MiB per shallow fetch, 65,536
tree entries and index depth 16. [Inferred] None is measured; the sources for
Redis are unread. *Recommended:* accept as the ceiling for the first target,
and treat the first run's measurement as the input to a later entry version.
A breach leaves dependent claims Unknown and never fails silently.

**O3. Route unknowns.** The provider entry lists what is [Unknown] today,
chiefly whether the Agent SDK on the owner's login can disable tools,
ambient context and telemetry and keep its transcript in the run directory.
*Recommended:* sign the entry only after that check, since the egress record
makes a runtime that cannot be so configured a run that does not start.

## What it does not do

It grants no read, egress, write, execution or release; installs nothing in
the registry directory; and changes no adopted specification, policy or
consent. It does not touch the Butlers entry.

## Review

A fresh-context review precedes any offering; `REVIEW-BRIEF.md` names the
artifacts, references and criteria. None has run.
