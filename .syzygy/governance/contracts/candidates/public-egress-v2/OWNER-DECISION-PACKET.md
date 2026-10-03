# Owner decision packet — second Anthropic egress version (sitting row 8)

> **Candidate — binds nothing.** This packet describes one record the owner
> could act on. It performs no act, infers none and carries no digest by
> design: the argument of an act is derived from the manifest by script
> (`python3 scripts/build_public_egress_v2.py --digests`), never transcribed.
> The record is **not ready** while the generator code that adds the
> discovery stages (PR #281) is not on main: the script refuses to print a
> digest until the table it derives from main's code carries them.

## What the record is

[Observed] `instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md` here is the
first version's egress record
(`../public-repo-admission/instances/egress-anthropic/EGRESS-CONSENT-ANTHROPIC.md`)
with these differences, all produced by the builder from this package's own
template and parameters (compare the two files):

1. the record version (`v2.json`);
2. the permitted content classes gain `project-documentation`;
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
   entry lists, whether the runtime fixes them or the entry pins them (model,
   effort, tool list, thinking, output ceiling), and that approving a route entry
   is a separate act. Retention, route-context and telemetry wording are made
   route-neutral the same way; the admitted repositories and content-class
   list are the first version's.

5. the record states, per route, the fixed bytes that route adds, by citing
   each entry's `requestBytes` (the Agent SDK runtime's additions for route A;
   the SDK library's headers, including the three machine-identifying ones, for
   route B) and permits a route's bytes only while that route's entry is in
   force. Stripping the three headers is marked as the owner's option in each
   route's packet; the record neither requires nor forbids it.

**Route choice and this record are independent.** Signing this version does not
choose a route, and choosing a route does not require signing it. The route is
the registry entry the owner puts in force (row 2a); this record only says the
requests may carry that entry's listed bytes. Both route packets said the first version's wording might need a version
like this one; this version settles that reading by stating each route's bytes,
and it is also needed for the class and the discovery stages.

## Why it exists

- [Observed] The first version's packet records that adding
  `project-documentation` "is a further version after that amendment is in
  force", and the sitting packet's row 8 is that version.
- [Observed] Discovery (map and reduce calls over subsystems) adds stages and
  probably request fields. The record enumerates fields and stages in its
  table and refuses a field outside it ("a request with a field outside the
  generated table, or generator-authored text the rule does not name, is
  refused"), so a table that changes is a record that changes.
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
  version's whole scope. With an act over version 0.1.0-candidate.7 in force
  this version supersedes it prospectively (RFC5-13); with none in force it
  supersedes nothing. Signing this version alone is therefore lawful, and so
  is signing both in order; the owner chooses, and this packet does not.
- **No new observation consent.** [Observed] The observation records name no
  content classes, so the class does not touch them.

## What is open

- PR #281 on main. [Observed] Its author delivered the stages
  (`discovery-map`, `discovery-reduce`), now `requiredStages` in `v2.json`, and
  the table with 21 discovery rows; `--table --discovery` was run at its local
  head and the committed record was generated from that output. The record
  is **not ready** until #281 is on main and `--check` and `--ready` pass
  there; any change to #281 means regenerating (`--write`), which changes the
  digest.
- The recorder for the row-8 act and its registration in
  `scripts/check_governance.py` (act subject and digest-copy rows) are not
  drafted: their frozen digest depends on the delivered table, and a recorder
  that hard-codes a digest of an unready record would be wrong on arrival.
  Both follow the stage list.
- The confirming review (`REVIEW-BRIEF.md`) is not dispatched.

## What this does not do

It reads no repository, calls no model, performs no act and lists no
provider-route change: the route entries are separate acts (rows 2 and 3).
Nothing here is authority until the owner acts on a confirmed record.
