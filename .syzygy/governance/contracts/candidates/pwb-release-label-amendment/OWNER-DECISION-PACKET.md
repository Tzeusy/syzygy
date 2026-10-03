# Owner decision packet — PWB release-label amendment

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts four questions to the owner, and only the owner's
> answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 under your direction of 2026-10-02 on bead
`syzygy-l362`. The review round's verdict and its dispositions are in
`ROUND-1-DISPOSITIONS.md` beside this file, which also says whether this
version is ready to offer.

## What you would be signing

One amendment to PWB-REQ-001 in the signed PWB specification. Read
`SEMANTIC-DELTA.md` for the full account. In short:

- **Polaris leads with the release label.** "Butlers v1.0.23" is shown, with
  the full Git object id beneath it. Every claim still binds to the object id,
  never to a tag.
- **Four forms, in order:**
  - **not read:** a short id, and the statement that tags were not read;
  - **tagged:** "Butlers v1.0.23";
  - **described:** the nearest tag plus a count of later commits;
  - **untagged:** a short id, and the statement that no release tag reaches
    it.

  A tag set nobody read is never shown as "untagged".
- **Moved tags** are disclosed when an earlier evaluation saw the tag on
  another commit. Nothing ever says a tag is unmoved.
- **Determinism is kept.** The tags are an input of the evaluation. Your
  "some cost in determinism" is paid only here: the same commit can show a
  different label once its tags change.

**What signing does not do.**

- **It does not let the observer read tags.** The observer's registry entry
  admits neither tag refs nor commit history. Until it does, every label shows
  the *not-read* form. See Question 2.
- **It does not change Trajectory or Orrery.** Their specification is the
  Three-Surface POC one. See Question 3.
- **It starts no implementation.** That needs its own authorization.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | The patches are applied in the sign-off change by version tag (Scope A covers PWB specification deltas). PWB-REQ-001 gains the release label and four scenarios. |
| Decline | PWB-REQ-001 stays as signed, and Polaris keeps showing a short object id. |
| Revise | Name what to change, and a new version gets a new review round. |

## Question 2 — the read your direction said would not change

Your direction said "no read or egress change". There is no egress change,
but the label needs two reads the observer is not admitted to make today:

- tag refs, as names and the commits they peel to;
- commit ancestry, as parent ids, for the "N later commits" count.

| Option | Meaning |
|---|---|
| **Draft a registry amendment admitting both, metadata only** (recommended) | A separate Scope A package amends the observer registry entry. It admits ref names, peeled object ids and parent ids only: no tag message, signature or commit message. You would sign it separately. |
| Admit tag refs only | The tagged and untagged forms work. The described form becomes "not read" for a revision that sits after a tag. |
| Admit nothing | The specification is signed, and every label stays "not read" until you decide otherwise. |

## Question 3 — Trajectory and Orrery

Their revision display is governed by the Three-Surface POC specification,
which already has one open amendment (P-84). You were advised to answer that
one with Revise.

| Option | Meaning |
|---|---|
| **Fold it into P-84's revision** (recommended) | The release label for Trajectory and Orrery joins the POC identity amendment when it is revised. Both packages then point at the same rule. |
| A separate POC successor after P-84 is disposed of | Drafted later, so the two never overlap. |
| Polaris only | Trajectory and Orrery keep the short object id. |

## Question 4 — which tags count

| Option | Meaning |
|---|---|
| **Every tag under `refs/tags/`** (recommended; this version) | There is no new declaration. A project's non-release tags would show as labels if they sit nearest the revision. |
| A declared release-tag pattern | A project's profile names a pattern (for example `v*`). That is a new profile field and a new version of this package. |

**If unanswered,** nothing is signed and the package stays a candidate.
