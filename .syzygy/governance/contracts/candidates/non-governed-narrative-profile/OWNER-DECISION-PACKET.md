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
  appears, because Syzygy has no evidence drawer for that project. One line
  says what is absent and why, never that nothing exists.
- **Exact source.** The reader reaches the maintainers' own words, quoted
  byte for byte with repository, revision, path and span, as an anchor one
  step from the claim. The leaf altitude is one honest line saying no
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
band for a non-governed subject. *Recommended:* yes. *Alternative:* require
the reality band to appear as a single Unknown line only, which is what the
package already does for the absent bands; no further option is needed
unless you want a populated reality band, which would need an evidence source
Syzygy does not have.

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

Fresh-context review before any offering, per `REVIEW-BRIEF.md`. None has
been run.
