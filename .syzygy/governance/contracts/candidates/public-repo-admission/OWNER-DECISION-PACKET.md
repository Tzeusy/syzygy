# Owner decision packet — reusable public-repository admission

> **Candidate — binds nothing.** Drafted 2026-10-03 at the owner's request
> ("Yeah ok let's do it", answering the proposal to "draft the reusable
> public-repo admission template for your sign-off"). Effect comes only from
> owner acts over the exact records in this directory. A commit, a review, a
> merged pull request or a passing check performs no act. No act record is
> written here, and no target repository body has been read.

## What this is, in one paragraph

The generalized Polaris generator is to be proven on open-source repositories
(`docs/polaris-generation/TARGETS.md`: requests, Redis, Sentry). Before the
generator may read any of them or send any of their content to a model
provider, doctrine and the adopted generator specification require separate,
separately revocable records (SEC-2; RFC5-12, RFC5-14, RFC5-15, RFC5-16;
REQ-polaris-generation-001 and 025). Drafting those as a bespoke package per
repository, the way the Butlers and self-observation acts were drafted, costs
several review rounds each. This package instead fixes **one shape** for
public repositories: a one-time screening-policy extension, one egress
consent revised as targets are added, and per target an observation consent
and a registry entry.

## Who observes

**Syzygy observes; each target is an observed repository.** The observing
project is `project:syzygy`, exactly as for Butlers (subject
`(project:syzygy, repository:butlers-configured-poc)`). Under RFC3-30 the
governing policy is the observing project's: "Project A screens, bounds, and
classifies everything it ingests under **A's** policies in A's own plane".
So every target is screened under `project:syzygy`'s policy, extended once,
and nothing a target's repository contains can act as policy. Q4 asks whether
to keep this model.

## The shape

**Once:**

1. **Public-source screening scope** (`templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md`).
   A versioned extension of `project:syzygy`'s secret-classification policy
   (`.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`,
   which carries performed acts) adding a public-repository scope with its
   own classification-success rule and the content-classification rules
   RFC5-14 needs. That policy's `rawBodyHandling` is `never` for storage,
   logging, rendering, machine response and external egress, and its
   active-content rule would withhold any source file containing a
   `<tag`-shaped string. The public scope changes both for public content
   only (outline items 3 and 4), so this is a real policy change, not a
   formality.
2. **Provider execution route registry entry** (REQ-polaris-generation-017).
   RFC4-1: "Every external authority is reached through exactly one
   registered adapter per project". The provider is one external authority
   of `project:syzygy`, so its route is registered once and shared by every
   target. Drafted with the first implementation that reads it, because a
   registry entry naming no implementation registers nothing.

**Once, then revised per target:**

3. **Egress consent** (`templates/EGRESS-CONSENT-TEMPLATE.md`). RFC5-12 fixes
   "one record per *(Project, provider)* pair", so there is one record for
   `(project:syzygy, provider)`. Its scope lists the admitted public
   repositories and excludes every other source of `project:syzygy`
   content, Butlers included. Admitting a target is a new version of this
   record that adds it; withdrawing one target is a new version that removes
   it (RFC5-13: prospective).

**Per target:**

4. **Observation consent** (`templates/OBSERVATION-CONSENT-TEMPLATE.md`) — per
   `(project:syzygy, repository)` pair (RFC5-12, RFC3-30): read-only reads of
   the Git snapshot objects of the listed revisions. No execution of the
   target's code (SEC-3), no writes anywhere in the target.
5. **Source-acquisition registry entry** (REQ-polaris-generation-017; fields
   per `openspec/changes/polaris-manifesto-generation/ADAPTER-DECLARATIONS.md`
   "Required registration fields"). Whether this is one entry per target or
   one shared Git-hosting adapter is decided when it is drafted: reading a
   fetched tree is an observer's work, but the fetch itself reaches the
   hosting service, which RFC4-1 lists as an external authority [Inferred].
   Drafted with the first implementation that reads it.

Each numbered item is its own record with its own act. For the two
consents REQ-025 requires it ("These permissions SHALL remain separately
revocable/renderable and SHALL NOT imply one another"); the policy and the
registry entries are each honored only under their own RFC3-16(a) act (Q5).
Several acts may be given in one sitting.

`instances/requests/` and `instances/redis/` fill item 4 for T1 (psf/requests
at `v2.34.2`) and T2 (redis/redis at `8.10.2` plus the licence-history trio
`7.2.4`, `7.4.0`, `8.0.0`; the pins are in
`docs/polaris-generation/TARGETS.md`), and `instances/egress-anthropic/`
fills item 3 once, listing both repositories as the next version of the single
`(project:syzygy, provider:anthropic)` record. All three use the owner's
2026-10-03 answers. The egress version lists the five content classes in
force, so it does not yet carry Q7's `project-documentation` class; adding it
is a further version after that amendment is in force. Only bytes that pass a confirming review are
offered for an act. Fields that depend on an
answer: the provider and subject (Q1), the content classes (Q2 and Q7), the
retention line (Q3), the subject and scope (Q4).

## Questions for the owner

Each has a recommendation. None is decided by this packet.

**Answered 2026-10-03** by plain owner direction
(`decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md`): every
recommendation was taken except Q1, where the owner chose Anthropic through
the Claude Code / Agent SDK runtime instead of direct API calls. The
questions below are kept as put; the instances now follow the answers.

**Q1. Which provider?** Egress consent must name the provider (SEC-2).
*Recommended:* Anthropic, via the Claude API, with the model recorded per run
rather than fixed in the consent; RFC5-14 asks for the provider, not a model.
A second provider later is a fresh egress consent.

**Q2. Which content classes may be sent?** RFC5-14's closed vocabulary:
`governance-text`, `code-structure`, `code-content`, `work-history`,
`evidence-content`, `derived-composites`. *Recommended for public targets:*
all but `work-history` — understanding a codebase needs its bodies, and the
repositories are public; issue trackers and CI history stay out.
`derived-composites` is included because every prompt is one; RFC5-14:
"`derived-composites` consent alone never launders an unconsented class into
an egress."

**Q3. Retention of sent content and provider replies.** SEC-2 does not state
these fields; the generation kit proposes them (`docs/polaris-generation/README.md`,
"Start here" step 4). *Recommended:* provider requests, provider replies and run records are
retained in a run
directory under `project:syzygy`'s state directory, outside git. Requests and
replies contain the source spans sent, so the run directory holds those spans
for as long as the run is retained (screening outline item 4); nothing is
retained in git, logs or machine responses. The provider's own retention is
whatever the terms of the account used say, recorded as a disclosed fact
rather than a Syzygy promise.

**Q4. Observation model.** *Recommended:* keep `project:syzygy` as the observing
project (above). The alternative — each target its own project — would need
a governance root and a separately approved policy per target (RFC3-30,
RFC5-16), which is the per-target cost this package exists to remove.
REQ-polaris-generation-001's "Two project identities" scenario shows the
generator must *support* distinct identities; it does not require each
proving target to be one. The cost of this model: RFC5-12 fixes one egress
record per (project, provider) pair, so this record becomes the only
`(project:syzygy, anthropic)` egress record. Any later egress of Butlers or
Syzygy content to the same provider would be a new version of it widening its
scope, not a separate record.

**Q5. Sign-off form.** Every record here needs an effective owner act under
RFC3-16(a) bound to its exact bytes: the policy (RFC5-16, RFC3-30), the
egress consent (RFC5-15), the observation consent (the Butlers observation
consent act, `decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`, was bound to
its record's exact digest), and each registry entry (RFC-0004's general
contract: "a registry entry is honored **only under RFC3-16(a)**"). That act
need not be typed: the 2026-10-02 policy re-pin act
(`decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`)
was given by an option selection naming the acts "at the manifest rows"; the
packet shown carried no digest, and the recorder bound each act to its
subject's row of the package manifest, refusing any other argument. Its
provenance state was recorded as state (1).

*Recommended:* the same form — one structured question per target sitting,
its option naming each record at its manifest row — and one step further:
the option states the provenance state it selects, state (1),
`owner-adopted (bootstrap, uncorrelated)`, A1 audit-record identity
explicitly absent. `scripts/build_public_repo_admission.py` regenerates the
instances (`--write`, `--check`) and prints each record's digest (`--digests`,
which refuses while any instance is stale). `--write` also writes the
package manifest, `PUBLIC-REPO-ADMISSION-MANIFEST.txt`, whose rows are those
digests, one per record. The version-tagged sign-off of
`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` is not
used: it names the PWB specification deltas, the observer registry entry and
the contract successors queued behind them, and these are consents, which
that direction does not mention [Inferred]. Before the first offering: a
recorder that binds each act to its manifest row and the act labels and
packet copies registered in `scripts/check_governance.py`, following the
repository's recorder convention; both are prepared after the confirming
review, against the confirmed commit. Registry entries are signed the same way
when they are drafted.

**Q6. Where generated pages may be served.** *Recommended:* only on the local
daemon's generated editorial draft view, `GET /polaris/draft/<runId>` — named
by the PWB machine-view amendment but not yet implemented — or, until it
exists, as a static file in the run directory opened locally; labelled
editorial draft and non-release; never
published, and never presented as the target project's own site or as
endorsed by its maintainers.

**Q7. General prose documentation has no content class.** RFC5-14 defines
`governance-text` as "Doctrine, spec, decision, policy text" and
`code-content` as "Source and test bodies". A README, user guide or tutorial
is neither, so under the closed vocabulary it is indeterminate and RFC5-14
refuses its egress — and those files are the best evidence of what a project
is for. *Options:* (a) amend RFC5-14 to add a class such as
`project-documentation` (an accepted-contract amendment, its own act);
(b) classify only design and specification documents as `governance-text`
and leave other prose unsent, accepting weaker pages. Under (b), LICENSE
files are unsent too, so T2's licence-history regeneration proof cannot run
until (a) is in force. *Recommended:* (a); until it is in force, T1 uses (b)
and records what it could not send.

## What it does not do

It grants no read, egress, write, execution or release. It changes no adopted
specification or policy. It admits no target. It does not touch the Butlers
consent or registry records, or the self-observation package on PR #120.
PR #120 patches the same policy file; whichever policy act lands second is
re-drafted against the other's performed bytes and re-reviewed before it is
offered.

## Review

Fresh-context review before any offering, per the repository's review
discipline. Rounds 1, 2 and 3 (`reviews/R-PUBLIC-ADMISSION-1-RAW.md`,
`reviews/R-PUBLIC-ADMISSION-2-RAW.md`, `reviews/R-PUBLIC-ADMISSION-3-RAW.md`)
each returned REVISE; the dispositions follow. Stopping rule, set before
round 3: after a third REVISE the drafter repairs, dispatches no further
round, and asks the owner. The round-3 repair below is therefore unreviewed;
a confirming round precedes any offering.

| R1 finding | Disposition |
|---|---|
| 1 Observation scope contradicts itself | Grant restated as the snapshot objects of the listed revisions only; ancestor history excluded; the local clone is the means, not the grant |
| 2 Policy is the wrong project's under Q4 | Observing project fixed as `project:syzygy` ("Who observes"); Q4 restated with the RFC3-30 consequence |
| 3 Q4 answer filled unmarked | Instances declared drafts regenerated after the answers; dependent fields listed above |
| 4 Q5 false premise | Q5 rewritten on the 2026-10-02 option-selection-over-digest precedent; builder and digest named as offering prerequisites |
| 5 RFC4-1 "permits" | "requires exactly one" |
| 6 REQ-001 overread | Q4 says the scenario requires support, not one project per target |
| 7 Review credited to Scope A | Credited to the repository's review discipline |
| 8 Summary omits registry entry | Added |
| 9 Active content and egress conflict with existing policy | Outline: egress named as the change; active content superseded by R2 row 1 |
| 10 General docs mapped to `governance-text` | Q7 added; outline maps only spec and design text |
| 11 No egress Scope field; no provenance state | Both added to the templates |
| 12 REQ-010 overcited | Citation removed; stated as the record's own condition |
| 13 "pending" markers in signed bytes | Removed; instances regenerated before offering |
| 14 Revocation omits Unknown | Added to the observation template |

| R2 finding | Disposition |
|---|---|
| 1 Active content misdescribed | Outline item 3 quotes the policy's closed markup list and proposes a source-code rule as a change the act approves |
| 2 Provider route per target breaks RFC4-1 | Provider route registered once (item 2); source entry's shape left to drafting, labelled Inferred (item 5) |
| 3 Q5 incomplete | Q5 covers all four record kinds, the state-(1) selection and the recorder |
| 4 Single egress record per pair | Q4 states the cost |
| 5 Builder selftest and modes | Selftest exercises the placeholder guard, banner replacement and staleness check; unknown modes exit 2; joins the battery at integration, not in a draft |
| 6 `rawBodyHandling` | Outline item 4 proposes per-field handling for the public scope |
| 7 Observation template gaps | Supersession is a field; fetch is shallow by commit; "effective" added |
| 8 LICENSE under Q7(b) | Q7 states it blocks T2's proof |
| 9 Collision with PR #120 | Stated in "What it does not do" and the outline |

| R3 finding | Disposition |
|---|---|
| 1 Retention contradiction (blocking) | Egress retention and Q3 now say the run directory holds the source spans sent, matching outline item 4 |
| 2 `accessBoundary` and path rules | Outline item 4 covers every `accessBoundary` field; item 2 keeps path admission and the denied-path rules |
| 3 Active-content list incomplete | All eight entries listed |
| 4 Q5 misdescribes precedent | Rewritten from the act's Ceremony section; manifest, recorder and check registration listed |
| 5 Syzygy's own prompts blocked | Egress scope permits the generator's own instruction text |
| 6 Stale R1 row 9 | Marked superseded by R2 row 1 |
| 7 Observer "for this pair" | Observation template defers to packet item 5 |
| 8 Draft route does not exist | Q6 names the prospective route and a local-file fallback |
| 9 `--digests` and orphans | `--digests` refuses while stale; `--check` reports orphan records |
| 10 "allows"; REQ-025 overcredited | "fixes"; separate policy and registry acts credited to RFC3-16(a) |

Round 4 (`reviews/R-PUBLIC-ADMISSION-4-RAW.md`), run over the owner's
answers at the owner's choice, returned REVISE with one blocking finding.
Repaired below; per the owner's choice the drafter reports rather than
dispatching a fifth round unasked.

| R4 finding | Disposition |
|---|---|
| 1 Transcript written elsewhere then moved (blocking) | The runtime's state and transcript are written inside the run directory from the start; a run whose runtime cannot be so configured does not start |
| 2 Garbled Q3 sentence | Repaired |
| 3 Prompt text has no class | Named as `code-content` of `project:syzygy`, with its source path |
| 4 Runtime may add its own context or telemetry | The record requires the runtime's own instruction, memory, settings, MCP and environment context off, an empty working directory, telemetry and error reporting off, and an adapter acceptance check on the captured request |
| 5 Which provider terms | The record names the owner's signed-in Claude account and its terms |
| 6 Direction says the packet "remains the question" | No change; the packet edits only point to the answers |

Round 5 is to run over the whole package after the Redis instances and the
egress version above are added (`REVIEW-BRIEF.md` in this directory names the
artifacts, the references and the acceptance criteria). The round-4 repair and
these additions are unreviewed until it returns.
