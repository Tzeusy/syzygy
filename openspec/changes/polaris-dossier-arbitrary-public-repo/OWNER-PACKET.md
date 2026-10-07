# Owner packet — dossiers for any public repository

> **Candidate — binds nothing.** Questions for you, each with a
> recommendation. Nothing here is decided, and no act is offered until a
> fresh-context review confirms these bytes.

## What you asked for, and what it takes

You asked to run Polaris on any public Git repository you can fork locally,
including ones whose authors never wrote down why they built it the way they
did. The draft does this with three additions to the Polaris spec:

- **037:** one standing permission, signed once, to read any public
  repository you clone, at the commit the run pins. No per-repository
  signature. Each run records the URL, your fork and the commit, and the page
  shows them.
- **038:** the "why" of a project (motivations, trade-offs, position) may be
  reconstructed from code, tests, comments and history. Each reconstruction
  is labelled Inferred, shows its evidence, and says plainly that it is not
  what the authors said.
- **039:** comparisons with other projects from outside sources, shown as
  your agent's unverified report. **Only if you reverse ruling 10b**
  (question 4); otherwise it is deleted.

Redis is not affected. It keeps its own signed consent and statements.

**One thing is bigger than expected.** "Every observed repository needs its
own consent" is not only in the specs. It is in three accepted contract
clauses (RFC1-3, RFC5-12 and RFC3-30) and in doctrine prose:
`architecture.md` says "Every observed repository consents, governance root
or not." A spec sign-off cannot override those, so question 0 comes first.

## Q0. How do we square this with the contracts and doctrine?

- **A. Record a reading (recommended).** You rule that a standing
  permission, applied to one repository per run through a record that names
  that repository, counts as that repository's recorded consent. One act; no
  doctrine or contract text changes. This is how the RFC7-20 reading and the
  bounded-mission interpretation were done.
- **B. Amend them.** A doctrine amendment to `architecture.md` and contract
  amendments to RFC-0005 and RFC-0001. Unambiguous, but three amendment
  packages, each with its own review.

*Why A:* each repository still ends up with its own record carrying every
field RFC5-12 asks for. The only open point is whether a grant made in
advance counts as consent for a repository you never named, and that is
exactly the kind of question your reading settles.

## Q1. What exactly does the standing permission cover?

| Part | Recommendation | Why |
|---|---|---|
| a. Public only? | **Yes.** Public repositories only; you declare that it is public, and the page shows that as your declaration. | Syzygy contacts no server, so it cannot check. A private repository is outside the permission by its own words. |
| b. Which hosts? | **Any host**, over `https`. | Syzygy never talks to the host; the host is only a label. An allow-list (GitHub, GitLab, Codeberg) is the stricter option. |
| c. Forks of private repositories, or your own local commits? | **Excluded.** Only commits published in the public repository. | Your own commits on the fork are not public content, and may carry your own notes or credentials. |
| d. Commit history? | **Include it**: the pinned commit plus its ancestors' commit records, read-only. | You named history as a source for the "why". Without it, history-based reasoning cannot be checked and is refused. Costs: the one-commit clone rule (open PR #392) relaxes for these runs, and the read scope is wider than Redis's. |
| e. Exclusions | **Start empty.** Excluding a repository later is a new version of the permission. | Lets you block one repository without revoking the rest. |
| f. Your own projects | **Always excluded** (Syzygy, Butlers, anything declared in a Syzygy project), as is any repository that already has its own consent, signed or withdrawn. | A withdrawn consent must never be quietly replaced by the standing one. |

It permits reading only: no sending (the provider mode stays parked), no
writing, no issues, pull requests or CI logs, and running code only as D9
already allows.

## Q2. What happens if the repository's tree contains `openspec/` or `.syzygy/`?

- **A. Refuse unless you sign a provider statement for that one repository
  (recommended).** Same as Redis's Anthropic statement today; the page is
  then written under the governed rules. Should be rare.
- **B. Treat any public third-party tree as ungoverned.** No signature ever;
  needs a reading that your data-sending rule (SEC-2) protects only projects
  *you* govern.

*Also:* the check today counts these folders at any depth (a vendored
dependency counts) and in any letter case. **Recommended: keep that** (it was
reviewed as the safe reading). The alternative is the top-level folder only.

## Q3. Reconstructed motivations: adopt 038 as drafted?

**Recommended: yes.** Where the authors explain themselves, their own words
are quoted exactly and anchor the claim. Where they don't, the agent may
reconstruct the reason from code, tests, comments and history, but must list
its evidence and its reasoning, the page marks it "reconstructed — not the
authors' stated intent", and an independent reviewer must agree the evidence
supports it before the dossier is ready. Guesses about the *people* (their
employer, business motives) stay Unknown unless the authors said so.

## Q4. Reverse ruling 10b (advantages: maintainer-stated only)?

- **No, keep 10b for now (recommended).** Advantages stay what the authors
  claimed. Comparisons with named projects are still allowed when the
  authors' own text names them, quoted exactly. Revisit after the first run
  on a repository you don't know.
- **Yes.** Adds 039: a separate section of comparisons from outside sources
  your agent read, labelled as its unverified report, never in the opening,
  never anchored, and never counted as supported by the reviewer.

*Why keep it:* that section would be the one part of the page nobody can
check, and authors usually name their alternatives somewhere.

## Q5. Does each run need anything from you?

**Recommended: no.** Starting the run is the request; the run records the
URL, your fork and the commit as your declarations, and the page shows them.
The alternative, a confirmation command you type yourself for every run (like
the execution choice), adds a step per repository, which is the cost this
change removes.

## Q6. How do you sign?

**Recommended:** one sitting, after review, with three structured questions:
the reading (Q0), the standing permission at its manifest row (a digest-bound
consent act, like Redis's), and the spec by version tag
(`polaris-dossier-arbitrary-public-repo-v1.0`), like the local-agent mode. The
source-acquisition entry then needs a new version naming the standing route,
signed the same way. Nothing is read until all of them are recorded.
