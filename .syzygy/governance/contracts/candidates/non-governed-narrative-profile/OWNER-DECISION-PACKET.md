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
reports a band it cannot render, and what the exact-source terminus is. It
edits no adopted file, grants no read or egress, and does not decide the
dossier's altitude order.

## What the package changes, in plain terms

- **Catalog.** A capability is listed as declared only if the maintainers
  wrote it down in a form fixed before the run began (documentation naming
  it, a reference entry, a manifest). Code alone only yields a labelled draft
  or Unknown.
- **Deep dives.** Argument and reference material appear. No reality band
  appears, because Syzygy has no evidence drawer for that project. One line
  says what is absent and why, never that nothing exists.
- **Exact source.** The reader reaches the maintainers' own words, quoted
  byte for byte with repository, revision, path and span.

## Questions for the owner

Each has a recommendation. None is decided by this packet.

**O1. Is a spec overlay enough, or does RFC7-14 need its own amendment?**
RFC7-14 says the leaf renders "verbatim from `openspec/**`". *Recommended:*
overlay only, because RFC7-13 binds another narrative to the verbatim
terminus, not to that directory [Inferred]. *Alternative:* amend RFC7-14
first, as a separate accepted-contract act, and hold this requirement until
it lands. The review will give its reading; it does not decide.

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
