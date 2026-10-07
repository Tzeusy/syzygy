# Owner packet — dossiers for any public repository

> **Candidate — binds nothing.** Questions for you, each with a
> recommendation. Nothing here is decided, and no act is offered until a
> fresh-context review confirms these bytes. Revised after the first review
> asked for changes.

## What you asked for, and what it takes

You asked to run Polaris on any public Git repository you can fork locally,
including ones whose authors never wrote down why they built it the way they
did (your direction of 2026-10-07, recorded as
`ARBITRARY-PUBLIC-REPO-DOSSIER-2026-10-07` in
`decisions/ARBITRARY-PUBLIC-REPO-DOSSIER-DIRECTION.md`). The draft does this
with three additions to the Polaris spec:

- **037:** one standing permission, signed once, to read any public
  repository you clone, at the one commit the run pins. No per-repository
  signature. Each run records the URL, your fork and the commit, and the page
  shows them.
- **038:** the "why" of a project (motivations, trade-offs, position) may be
  reconstructed from code, tests and comments. Each reconstruction is
  labelled Inferred, shows its evidence, and says plainly that it is not
  what the authors said.
- **039:** comparisons with other projects from outside sources, shown as
  your agent's unverified report. **Only if you reverse ruling 10b**
  (question 6); otherwise it is deleted.

**This needs amendments, not just a sign-off.** The rule that every
repository Syzygy reads has its own signed consent is written into doctrine
(`architecture.md`: "Every observed repository consents, governance root or
not") and into four accepted contracts. A standing permission for
repositories you have never named does not meet those words, so they have to
change first. The first draft suggested you could simply rule that it did;
the review showed that it does not, and that suggestion is withdrawn.

**Redis keeps its own signed consent, but 038 would reach it.** If you adopt
038 for every run (question 5), Redis's dossier could also carry
reconstructed motivations and trade-offs, which loosens ruling 10b's
"maintainer-stated" rule for those two topics. Redis's advantages stay
maintainer-stated either way.

## Q0. Amend doctrine and the contracts to allow a standing permission?

**Recommended: yes, with the smallest amendment.** It adds one new form of
the existing "observation consent": a signed record that covers every
repository meeting stated conditions (public, the host rule, not excluded),
instead of one named repository. Each run then writes a short entry naming
the one repository and commit it reads; the entry grants nothing by itself,
and revoking the standing permission revokes every entry. Reading only:
writing, running code and sending data keep their per-repository or
per-provider consents.

What you would sign, each after its own review (drafts in `AMENDMENTS.md`):

| Act | What it changes |
|---|---|
| Doctrine amendment (log row D10, if D7 and D8 keep their numbers) | Two sentences of `architecture.md` |
| Contract amendment, RFC 0001 | Where a repository's identity, consent and membership come from (RFC1-2, RFC1-3, RFC1-4) |
| Contract amendment, RFC 0003 | Repository entries, consent records, per-pair consent (RFC3-6, RFC3-7, RFC3-30) |
| Contract amendment, RFC 0005 | Defines the standing form (RFC5-12) |
| The standing permission itself | Signed like Redis's consent, once the amendments are in force |

The three contract amendments can be one act over a multi-row manifest, as
the contract readability restyle was.

*Costs:* the D7 and D8 doctrine drafts were reviewed over today's
`architecture.md`, so whichever lands second must be re-confirmed. An RFC5-12
amendment queued after D9 touches the same clause.

*Alternative:* keep per-repository consent and make signing one faster (a
template and one question per repository). Simpler doctrine, but every new
repository needs you.

## Q1. What exactly does the standing permission cover?

| Part | Recommendation | Why |
|---|---|---|
| a. Public only? | **Yes.** You declare that the repository is public and that the commit is published there; the page shows both as your declaration. | Syzygy contacts no server, so it cannot check. |
| b. Which hosts? | **Any host**, over `https`. | Syzygy never talks to the host. An allow-list (GitHub, GitLab, Codeberg) is the stricter option. |
| c. Your own local commits? | **Excluded.** The clone must hold the published commit alone; a commit you made on top of it is refused automatically. | A single commit you wrote from scratch looks identical to a published one, so for that case Syzygy relies on your declaration in (a). |
| d. Exclusions | **Start empty.** Adding one later is a new version of the permission. It can name repositories, URLs or commits. | Lets you block one repository without revoking the rest. |
| e. Repositories already handled | **Always excluded:** anything declared in a Syzygy project, and any repository with its own consent, signed or withdrawn. Matched by name, by commit and by URL, so a withdrawn repository cannot come back under a new name. | Some cases slip through: a later commit of a withdrawn repository, reached through a different mirror. Only your declaration separates those, and every page says so. |
| f. May a run execute the repository's code? | **No by default.** Recording the per-run execution choice D9 allows is refused under the standing permission unless it says otherwise. | Under D9 that code runs with your own credentials and network, "and can change any file the owner can"; nothing contains it. For code from unknown authors that is a real risk. |

## Q2. Read commit history?

**Recommended: no, not now.** Reads stay at the one pinned commit, as for
Redis and as the one-commit clone check (open PR #392) enforces.
Reconstructions rest on the code, tests and comments at that commit. Your
direction mentioned reconstructing from "the code and its history"; this
recommendation departs from that for now, and saying yes here restores it.

*The option:* allow the pinned commit's ancestors' commit records (messages
only; never older files). This changes REQ-033's rule that "every read … at
the pinned revision", which 037 would then name and reread. Author and
committer names and email addresses would be withheld and never shown, since
showing them is a privacy question of its own.

## Q3. What if the repository contains `openspec/` or `.syzygy/`?

- **A. Refuse unless you sign a provider statement for that one repository
  (recommended).** Same as Redis's Anthropic statement today; the page is
  then written under the governed rules. Should be rare.
- **B. Treat any public third-party tree as ungoverned.** No signature ever;
  needs a reading or amendment of your data-sending rule (SEC-2).

*Also:* the check counts these folders at any depth (a vendored dependency
counts) and in any letter case. **Recommended: keep that.** A tree built to
dodge the check with invisible characters can still pass; the earlier review
judged that acceptable because a project has no reason to hide its own
governance folder, but a stranger's repository might. The page discloses it,
and nothing is sent anywhere by Syzygy in this mode. The alternative is the
top-level folder only.

## Q4. Reconstructed motivations: adopt 038 as drafted?

**Recommended: yes.** Where the authors explain themselves, their own words
are quoted exactly. Text the repository merely bundles from someone else
does not count as the authors' words. Where they don't explain, the agent
may reconstruct the reason, but must list its evidence and reasoning, the
page marks it "reconstructed — not the authors' stated intent", and an
independent reviewer reads every inferred claim, marked or not, and blocks
the dossier if a motive is asserted without that marking or without
support. Guesses about the *people* (their employer, business motives) stay
Unknown unless the authors said so.

## Q5. Should 038 apply to Redis too?

**Recommended: yes.** Redis's dossier could then reconstruct motivations and
trade-offs the Redis authors never wrote down, with the same labels and
review. This loosens ruling 10b and the "maintainer-stated advantages and
trade-offs" topic for Redis's motivations and trade-offs. Advantages stay
maintainer-stated (question 6). If you say no, 038 is limited to repositories
read under the standing permission.

## Q6. Reverse ruling 10b (advantages: maintainer-stated only)?

- **No, keep 10b for now (recommended).** Advantages stay what the authors
  claimed. Comparisons with named projects are still allowed when the
  authors' own text names them, quoted exactly. Revisit after the first run
  on a repository you don't know.
- **Yes.** Adds 039: a separate section of comparisons from outside sources
  your agent read, labelled as its unverified report, never in the opening,
  never anchored, and never counted as supported by the reviewer. Syzygy can
  only spot such claims if your agent marks them; the reviewer is the
  backstop.

## Q7. Does each run need anything from you?

**Recommended: no.** Starting the run is the request; the run records the
URL, your fork, the commit and your publication declaration, and the page
shows them. The alternative, a confirmation you type for every run, adds a
step per repository, which is the cost this change removes.

## Q8. In what order do you sign?

**Recommended:** after review, in this order, because each needs the one
before: the doctrine amendment, the contract amendments, the standing
permission, this spec by version tag
(`polaris-dossier-arbitrary-public-repo-v1.0`), and a new version of the
source-acquisition entry naming the standing route. Nothing is read until
all of them are recorded. They can share one sitting.
