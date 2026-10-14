# Owner decision packet — PWB release-label amendment

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts five questions to the owner (the fifth added
> 2026-10-14), and only the owner's answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 under your direction of 2026-10-02 on bead
`syzygy-l362`. Rounds 1 and 2 both returned `REVISE`; their dispositions are
in `ROUND-1-DISPOSITIONS.md` and `ROUND-2-DISPOSITIONS.md` beside this file.

**Round-2 findings repaired once on 2026-10-14, unconfirmed pending round
3.** On 2026-10-14 you instructed one new version repairing all six round-2
findings, then one fresh confirmation round. This is that version. No round
has read these bytes, so it is **not offered for sign-off** until round 3
returns `CONFIRM`, or `CONFIRM WITH EXCEPTIONS` with notes only. The
questions below are unchanged; your instruction answers Question 1 with
*Revise* for round 2's bytes, and Question 1 is asked again of this version
once round 3 clears it.
*(Marked 2026-10-14: "unconfirmed pending round 3" and "No round has read
these bytes" are no longer true. Round 3 read them and returned `REVISE`,
two revise findings and five notes
(`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md` line 4), so round 3
did not clear this version. Under the stopping rule recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` it is
not repaired again and comes to you with those findings open;
`ROUND-3-DISPOSITIONS.md` beside this file classifies them.)*

**Round-3 findings repaired once on 2026-10-14, unconfirmed pending round
4.** Later on 2026-10-14 you directed one more cycle: repair every round-3
finding, notes included, then one fresh review under the same stopping
rule. This is that version; the repairs are mapped in
`ROUND-3-DISPOSITIONS.md` §"Repairs, 2026-10-14 (cycle 2)". No round has
read these bytes, so it is **not offered for sign-off** until round 4
returns `CONFIRM`, or `CONFIRM WITH EXCEPTIONS` with notes only. Questions
1–4 are unchanged, and one repair needed a content choice that is yours,
so it is added as Question 5.
*(Marked 2026-10-14, round 4: "unconfirmed pending round 4" and "No round
has read these bytes" are no longer true. Round 4 ran and returned
`REVISE` (`docs/reviews/R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md` line 4):
one revise finding (the provenance-stamp exception is decided by the
implementation's own mark) and seven notes, all open in
`ROUND-4-DISPOSITIONS.md`. Under the stopping rule the package is not
repaired again and this version is not offered for sign-off; it comes to
you with those findings open.)*

## What you would be signing

One amendment to PWB-REQ-001 in the signed PWB specification. Read
`SEMANTIC-DELTA.md` for the full account. In short:

- **Polaris leads with the release label.** "Butlers v1.0.23" is shown, with
  the full Git object id beneath it. Every claim still binds to the object id,
  never to a tag.
- **Four forms, in order:**
  - **not read:** a short id and a statement saying which read is missing:
    "release tags were not read" when the tags were not read, or "the
    history needed to judge release tags was not read" when the tags were
    read but the history was not;
  - **tagged:** "Butlers v1.0.23";
  - **described:** the nearest tag plus a count of later commits;
  - **untagged:** a short id, and the statement "no release tag reaches this
    revision".

  A tag set nobody read is never shown as "untagged". "Release tags" means
  the tags the label counts, which is whatever Question 4 decides.
- **Polaris names the revision only in a label unit.** Each unit is one
  marked element holding the label, its statement, the full id beneath, the
  tied names and any moved-tag disclosure, and every Polaris page has at
  least one. Elsewhere the visible text may not show the revision's id or
  "Butlers" followed by a tag name, with three exceptions:
  - the short id stamped beside each claim's source, which is the identity
    the claim binds to and carries no label;
  - Butlers' own text shown verbatim, which stays byte-identical;
  - the shared status line above every surface's content (Question 5).
- **Moved tags** are disclosed when an earlier evaluation, named as compared,
  saw the tag on another commit, wherever the tag's name appears, tied names
  included. Nothing ever says a tag is unmoved, unchanged or stable, and the
  checker searches for those words.
- **Determinism is kept.** The tags are an input of the evaluation. Your
  "some cost in determinism" is paid only here: the same commit can show a
  different label once its tags change.

**What it touches besides PWB-REQ-001.**

- **One contract-coverage row.** RFC4-11's "not applicable" basis, "no commit
  history is rendered", stops being true, so that row is split into two
  repair rows (see `SEMANTIC-DELTA.md` §"Coverage matrix").
- **Not PWB-REQ-007 or PWB-REQ-020.** Your direction named the
  "PWB-REQ-007/020 tuple". The label is treated as a presentation of the
  revision, not a project claim, so neither requirement changes. Answer
  "Revise" if you want it to be a challengeable claim instead.

**Three choices the round-2 repair made** (`SEMANTIC-DELTA.md` §"Choices
the round-2 repair made"): one tag that cannot be peeled makes the whole tag
set read as failed; the three statements are fixed wording; and each label
unit is one element of the page, so a checker can count them. Answer
*Revise* if you want any of them otherwise.

**Four more choices the cycle-2 repair made** (`SEMANTIC-DELTA.md`
§"Choices the cycle-2 repair made"): every Polaris page shows at least one
label unit; per-claim source stamps keep a bare short id with no label;
Butlers' verbatim text is never rewritten to carry a label; and "unmoved"
is caught by a closed list of five terms. Answer *Revise* if you want any
of them otherwise.

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
| Admit tag refs only | Only the tagged form works. Every other revision reads "not read", because neither "N later commits" nor "untagged" can be decided without the history. |
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

## Question 5 — the shared status line on Polaris (added 2026-10-14, cycle 2)

Every surface, Polaris included, shows one shared status line above its
content, and it shows the revision's short id ("project" followed by twelve
hexadecimal digits).
That line is built by one component that the Three-Surface POC
specification governs, not the PWB one. This version leaves it alone and
excepts it from the label rule, so on Polaris the short id there stays.

| Option | Meaning |
|---|---|
| **Leave it to the POC specification** (this version) | The status line keeps its short id on every surface. If you want the label there too, it travels with Trajectory and Orrery under Question 3. |
| Label it on Polaris now | The status line on Polaris carries a label unit. The shared component then behaves differently on Polaris, which changes a POC-governed file, so this needs a POC amendment beside this one (Question 3) and a new version of this package. |

**If unanswered,** nothing is signed and the package stays a candidate.
