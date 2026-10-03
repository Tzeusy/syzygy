# Owner decision packet — second Anthropic egress version (sitting row 8)

> **Candidate — binds nothing.** This packet describes one record the owner
> could act on. It performs no act, infers none and carries no digest by
> design: the argument of an act is derived from the manifest by script
> (`python3 scripts/build_public_egress_v2.py --digests`), never transcribed.
> The record's table is generated from the generator's code on main, which
> already carries the discovery stages; the script refuses to print a digest
> if the record is stale or the stage list is not met.

## What signing this record lets leave your machine

In plain words, if you give this act and a run follows:

- **Excerpts of files** from the two named public repositories (psf/requests at
  its pinned commit and redis/redis at its four pinned commits) are sent to
  Anthropic, before the pipeline chooses what to read, so the model can rank
  which files matter. A second call sends the model's own claims about those
  files back to it for the final ranking. The subsystem names, file paths,
  blob counts and blob ids that go with them are sent too.
- **This record caps no volume.** The numbers in today's code (excerpts of 1,500
  characters, up to 40 files per map call, up to 40 map calls, and up to 400
  claims of up to 400 characters each in the second call) are defaults of the
  discovery code, not terms of this consent: a run given a larger discovery
  budget stays inside it. How much leaves is bounded by the run budget the
  trigger supplies, which the owner sets and which this act does not (the
  `dossier-units-v1` proposal under "Proposed run budget" in the sitting packet).
- **README files, guides, tutorials and design documents** of those
  repositories become sendable under the new `project-documentation` class.
  Today the screening scope treats such prose as indeterminate and withholds
  it. This is the one widening of what kinds of content may leave, and it takes
  effect only after sitting row 7 is performed.
- **Nothing about the route changes.** Which route carries the requests (Agent
  SDK or Messages API) is the separate choice in row 2a; this record only says
  the requests may carry that route's listed bytes, and only while that route's
  entry is in force.
- **What does not leave:** anything excluded or unclassifiable under the
  screening scope, the Butlers repository, the rest of Syzygy's repository,
  and any work history. Nothing is published; the dossier is a local draft.

## What the record is

[Observed] `instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md` here is the
first version's egress record
(`../public-repo-admission/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`)
with these differences, all produced by the builder from this package's own
template and parameters (compare the two files):

1. the record version (`v2.json`);
2. the permitted content classes gain `project-documentation`, a declared and
   intended widening (the class list is otherwise the first version's);
3. the carried-content table is the one
   `scripts/derive_generator_sent_text.mjs --table --discovery` prints from the
   code at regeneration time: the first version's rows plus the discovery
   stages and fields, each with its one class;
4. the record is **route-neutral**. It names the provider and the request, and
   refers to the route only through the registered route entry, so it follows
   whichever entry is in force: the Agent SDK entry (PR #255) or the Messages
   API entry (PR #273). The first version names the Agent SDK route, says the
   route "adds no context of its own" and admits only bytes "fixed by the
   runtime"; this version says the route adds only the bytes the registered
   entry lists, whether the runtime fixes them or the entry pins them, and that
   approving a route entry is a separate act. Retention and telemetry wording
   are made route-neutral the same way. The first version's absolute ban on
   memory files, settings, MCP servers, hooks and an environment summary is
   kept: a route entry may narrow it and never override it;
5. the record states, per route, the fixed bytes that route adds, citing each
   entry's `requestBytes` and spelling out where the two routes differ (tool
   list, thinking setting, endpoint, `cache_control`, the runtime's
   additions). Stripping the three machine-identifying headers is marked as the
   owner's option in each route's packet; the record neither requires nor
   forbids it;
6. the scope bullet for target metadata names the discovery stages' subsystem
   names, blob counts, blob ids and paths, and the Stages column's `all` is
   defined.

The template differs from the first version's in the lines that make 4 to 6
true. `v2.json` pins the size of that difference (hunks and lines), and `--check`
fails when the template moves without that pin being updated.

**Route choice and this record are independent.** Signing this version does not
choose a route, and choosing a route does not require signing it. The route is
the registry entry the owner puts in force (row 2a); this record only says the
requests may carry that entry's listed bytes. Both route packets said the
first version's wording might need a version like this one; this version
settles that reading by stating each route's bytes, and it is also needed for
the class and the discovery stages.

## Why it exists

- [Observed] The first version's packet records that adding
  `project-documentation` "is a further version after that amendment is in
  force", and the sitting packet's row 8 is that version.
- [Observed] Discovery (map and reduce calls over subsystems) adds stages and
  request fields. The record enumerates fields and stages in its table and
  refuses a field outside it ("a request with a field outside the generated
  table, or generator-authored text the rule does not name, is refused"), so a
  table that changes is a record that changes.
- [Observed] Folding both into one version means one signature covers both.
  The screening rule is unchanged only if discovery's instruction text comes
  out of `promptForStage` and `stageSchema`, the two symbols the screening
  scope names; a new symbol needs a new screening-policy version, which this
  record cannot supply [Inferred from the scope's instruction-text rule].

## Dependencies and order

- **Row 7 first.** [Observed] RFC5-14's vocabulary is closed. Until the
  `rfc5-project-documentation-class` act is performed, this record would
  permit a class no accepted contract defines, and the single egress check
  would find it undeterminable. The order in one sitting is row 7, then
  row 8. A reviewer confirms row 8 beforehand against that package's
  proposed RFC5-14 text, read as if in force; nothing here is performed by the
  review.
- **Row 6 is optional once this is signed.** The record carries the first
  version's whole scope plus the additions above. With an act over version
  0.1.0-candidate.7 in force this version supersedes it prospectively
  (RFC5-13); with none in force it supersedes nothing. Signing this version
  alone is lawful (the first version is then never performed), and so is
  signing the first version and then this one; the owner chooses, and this
  packet does not.
- **Signing the first version after this one is not an offered order.** It
  would leave two records in force for one (project, provider) pair, against
  RFC5-12's one record per pair. The first version's recorder refuses it once
  this version's act record exists, and the sitting installer follows the same
  order.
- **No new observation consent.** [Observed] The observation records name no
  content classes, so the class does not touch them.

## A known limitation: successor route entries

The record refers to the route through the registered entry, by kind (the Agent
SDK entry or the Messages API entry), not by a pinned version or digest. A later
owner-approved successor entry in the same role therefore flows into this
consent without a new egress version, bounded only by the record's absolute ban
(memory files, settings, MCP servers, hooks, environment summary) and its
refusal of any field outside the table. That successor entry needs its own owner
act; this consent does not approve it.

## What is open

- The recorder for the row-8 act and its registration in
  `scripts/check_governance.py` are drafted but unfrozen: they refuse every
  act until a confirming review returns and its digests are filled in.
- The confirming review (`REVIEW-BRIEF.md`) is round 2 over this packet after a
  round-1 REVISE (`reviews/`, `ROUND-1-DISPOSITIONS.md`).

## What this does not do

It reads no repository, calls no model, performs no act and lists no
provider-route change: the route entries are separate acts (rows 2a to 3b).
Nothing here is authority until the owner acts on a confirmed record.
