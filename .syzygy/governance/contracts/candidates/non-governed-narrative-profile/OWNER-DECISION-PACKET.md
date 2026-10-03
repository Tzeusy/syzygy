# Owner decision packet — non-governed narrative profile

> **Candidate — binds nothing.** Drafted 2026-10-03. It performs no act and
> carries no digest. Effect comes only from an owner act over the exact
> reviewed bytes, after a confirming review. A commit, a review or a merged
> pull request performs no act.

## What this is, in one paragraph

To write a Polaris dossier for `redis/redis`, the adopted narrative rules need
a defined reading for a repository that has no Syzygy declarations. This
package adds requirement 032 to the Polaris generator specification. It
says what a declared capability is for such a repository, how a deep dive
reports a band it cannot render, and, with no specification to quote, what the
leaf altitude and the exact-source anchor are. It edits no adopted file, grants
no read or egress, and does not decide the dossier's altitude order. It
changes how requirement 004 reads for such a repository without editing 004:
today a thin, predominantly Unknown narrative is correct output there, and
this replaces that defined outcome with a fuller one.

## What the package changes, in plain terms

- **Catalog.** A capability is listed as declared only if the maintainers
  wrote it down in a form fixed before the run began (documentation naming
  it, a reference entry, a manifest). Code alone only yields a labelled draft
  or Unknown.
- **Deep dives.** Argument and reference material appear. No reality band
  appears, because Syzygy has no evidence drawer for that project. A line for
  each band not rendered (at most two) says what is absent and why, never
  that nothing exists.
- **Exact source.** The reader reaches the maintainers' own words, quoted
  byte for byte, as an anchor one step from the claim (an object identifier,
  a byte range and a revision, with repository and path shown beside it as
  labels). The leaf altitude is one honest line saying no
  specification exists; the maintainers' text is never presented as one.

## Questions for the owner

Each has a recommendation. None is decided by this packet.

**O1. Is the maintainer span the leaf, or the anchor beside an honest leaf line?**
RFC7-13 has every narrative descend to a "verbatim specification leaf"
(RFC7-14), and RFC7-14 makes the leaf "the one place Polaris tells a reader
the text before them *is* operative". A maintainer's README is not a
specification. *Recommended (as drafted):* no contract act. The leaf altitude
is one honest `missing-declaration` line (RFC7-19), and the byte-exact span is
the one-step anchor (RFC7-2 (a)), never called a leaf or a specification
[Inferred]. *Alternative:* amend RFC7-13/14 first, as a separate
accepted-contract act, so that a non-governed subject's leaf is its
maintainer span, and redraft (c) after it lands. Round 1 of the review found
that making the span a substitute for the leaf without an amendment was not
lawful; the reviewer's reading is the one adopted here.

**O2. Does the reality-band omission stand?** The profile renders no reality
band for a non-governed subject. *Recommended:* yes. *Alternative:* let the profile
populate a reality-class band from non-kernel sources, labelled Inferred. That
contradicts RFC7-18 (every reality-band fact comes from the kernel's single
evidence drawer), so it needs an RFC7-18 amendment first and an evidence
source Syzygy does not have.

**O3. Sign-off form.** The version-tagged sign-off of
`decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md` names the
PWB specification deltas, the observer registry entry and the contract
successors queued behind them. This is a Polaris generation specification
delta, which Scope A does not name [Inferred]. The tree-form amendment to the
same specification was adopted on 2026-09-28 by the owner's option selection
recorded in `decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`. *Recommended:*
a structured option selection naming the package, with the owner stating in
that selection whether Scope A is read to cover it; the recorder, if the
owner prefers a tag, is `scripts/record_versioned_signoff.py`, whose
package-builder contract this package does not yet meet. *Alternative:* the
phrase-and-digest act used for the understanding amendment.

**O4. Adoption mechanics.** On adoption the spec file moves from `proposed/`
to `specs/` and the recount tooling is generalized in the same change
(`tasks.md`). *Recommended:* accept that as part of the act. *Alternative:*
edit requirement 004 in place, as the tree-form adoption did; that touches a
bound file and needs its own regeneration and review.

**O5. Is a model-authored glossary, anchored to admitted spans, part of this
profile?** *Recommended: deferred, recorded here, not added.* The adopted
requirements already forbid an unestablished glossary definition (the
scenario "the sources do not establish a glossary definition" in both the
base spec and the understanding amendment), and the provider draft schema has
no glossary field today (reported by lane-e, PR 265; relayed, not re-read here), so
a glossary requirement would need a schema change in the artifact contract, an
implementation path this package does not authorize. It is also a different
category from the three readings here: it would apply to governed and
non-governed subjects alike, and an OpenSpec change is one coherent category
(AGENTS.md hard prohibitions), so it belongs in its own change. If you want
it, it would be an additive requirement of its own: each glossary term SHALL
cite at least one admitted span that establishes its definition, a definition
no span establishes SHALL render Unknown, and a term with no span SHALL NOT
appear; its scenarios would cover an anchored term, an unestablished term and
a term whose span is later withdrawn. *Alternative:* add it to this profile
now; the review of that addition then restarts.

**O6. Is reading maintainer documentation as "the project's own spec or shape
documents" (RFC1-14) acceptable?** The profile's declared capabilities rest on
it. *Recommended:* yes, bounded as drafted (maintainer-written, not generated,
form fixed outside the producer), because for a project with no Syzygy
declarations those are the only artifacts in which its maintainers assert what
exists [Inferred]. *Alternative:* rule that RFC1-14 needs a specification, and
amend RFC1-14 to widen it first; then (a) waits on that act.

**O7. Is a source object of an observed repository an "evidence artifact" for
RFC7-10?** RFC7-10 allows five anchor target classes and says anchors embed
"durable identifiers, never labels, paths, or coordinates"; adopted
REQ-polaris-generation-019 refuses "a label/path in place of a durable target
and fragment". (c) uses the last class, an evidence artifact identifier with
integrity digest: the source's content-addressed object identifier, a byte-range
fragment and the admission revision as target state, with repository and path
beside it as labels. The generator's own anchor string embeds the path and so
is not that anchor [Observed]. *Recommended:* yes, bounded as drafted, because a
content-addressed object identifier is an integrity digest and no other class
fits a non-governed source [Inferred]. *Alternative:* rule the class narrow, so
that observed-repository sources need a new target class; RFC7-10 is amended
first and (c) waits on that act.

**Related to O6, not a separate question.** The scenario "Partly governed
subject" makes an outside repository's `openspec/**` text the verbatim leaf,
which RFC7-14 calls "the one place Polaris tells a reader the text before them
*is* operative". That rests on the same reading of RFC1-14 as O6 (a project's
own spec counts): rule O6 the other way and the scenario changes with it.

**Implementation note, not a question.** The selection predicate needs the
admitted project input to state whether an evidence drawer exists, and the
frozen profile is a new run-control record. Whether the interchange records of
REQ-polaris-generation-019 can carry them is Unknown; if not, a schema change
is needed that no act authorizes here (as for O5). `tasks.md` lists it.

### Rulings this package deliberately leaves open

These are the owner's alone and need no amendment to be put (gap analysis
`docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md`):

- **Altitude order for a dossier** (item 17d). RFC7-13: the primary narrative
  uses the V0 default order "unless the owner rules otherwise".
- **Advantages** (item 18): maintainer-stated only, or also external
  comparison sources.
- **Reader-facing page budget** (item 19): after the first measurement.

## What it does not do

It grants no read, egress, write, execution or release. It admits no
repository. It amends no accepted contract, doctrine or adopted
specification. It binds nothing until reviewed and acted on.

## Review

Fresh-context review before any offering, per `REVIEW-BRIEF.md`. Three
rounds have run: round 1 REVISE, round 2 REVISE, round 3 CONFIRM WITH
EXCEPTIONS with seven notes (each raw's own `Verdict:` line is the verdict of
record). Under the 2026-09-26 ruling the round-3 notes clear the specification
bytes; they are dispositioned in `reviews/ROUND-3-DISPOSITIONS.md`.

### Known limitations in the specification bytes

Two round-3 notes live in the specification itself, which is the reviewed
subject and is not edited after its clearance. You can sign as it stands, or
ask for one more round that makes these two changes. Proposed wording is given
for each.

1. **Silent project input.** The scenario "Partly governed subject" says "the
   project input records no evidence drawer", which a silent input also
   satisfies, while the requirement's own text refuses or limits the run for a
   silent input. Proposed wording: "the project input states that no evidence
   drawer exists". Until then, an oracle writer reads the scenario as the case
   where the input states the absence.
2. **Hash algorithm in the anchor.** The requirement asks for the object
   identifier "with its hash algorithm named", but the generator's source
   record carries no algorithm field; the algorithm is recoverable only from
   the identifier's length (40 or 64 hex characters). Proposed wording: "with
   its hash algorithm named, derived from the identifier's length or carried
   in the source record", with the record-home Unknown in `design.md` deciding
   which.
