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
with exactly three differences, all produced by the builder and none
hand-written (compare the two files):

1. the record version (`v2.json`);
2. the permitted content classes gain `project-documentation`;
3. the carried-content table is the one
   `scripts/derive_generator_sent_text.mjs --table` prints from the code at
   regeneration time. Today it equals the first version's table. Once the
   discovery stages and fields are on main it carries them, each with its one
   class; the derivation fails on a field with no class.

Provider, route, retention, route context and the admitted repositories
(`psf-requests`, `redis-redis`) are read from the first version's parameters,
so the two versions cannot drift apart.

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
