# Owner decision packet — public-source screening scope, version 2

> **Candidate — binds nothing.** It carries no digest. Nothing here is a
> decision, and no act is performed by reading it. It is offered only after a
> confirming review.

## What this is, in plain words

The version-1 scope lets the generator read a public repository's source code
and nothing else. A dossier needs the project's own explanation of itself, so
this version lets it read the README, changelog, contribution and licence
files, and the guides under a top-level docs folder.

## What becomes sendable, and what stays withheld

**Becomes readable and, under a consent that lists the class and a separate
egress consent, sendable:**

- root-level README, CHANGELOG or CHANGES, release notes (including a numbered
  name such as 00-RELEASENOTES), NEWS, HISTORY, CONTRIBUTING, LICENSE or
  LICENCE, COPYING, NOTICE, AUTHORS, SECURITY, MANIFESTO, ARCHITECTURE, DESIGN,
  FAQ, GOVERNANCE and CODE_OF_CONDUCT (or with hyphens), with no extension or
  .md, .rst or .txt, in any letter case. The list is wide because a project's
  top level often holds its stated ideas and trade-offs in files like these
  [Inferred, from general knowledge; no body was read];
- any .md, .rst or .txt file under a top-level docs or doc folder, at any depth;
- .txt or .md files directly inside a top-level licenses folder.

**Stays withheld (excluded from reading and from egress, hash-not-body):**

- READMEs below the root outside docs (including vendored libraries'), the
  root names above when they sit in a subfolder outside docs, specification, design and decision documents, reports,
  and any other prose;
- any file that fails a secret detector or the active-content rule: those
  screens are unchanged and apply to this prose in full;
- anything while the RFC-0005 amendment of PR #257 is not in force.

It does not give consent: a repository consent that does not list
`project-documentation` still sends none of it.

## The act

An `approve-policy` act over the proposed policy bytes, at the package
manifest's row, in the form of the version-1 act. It supersedes the version-1
bytes. A recorder is written after the review.

## Questions

**Q1. Sign this scope?** *Recommended:* yes, after a confirming review, and only
once the RFC-0005 amendment (PR #257) is signed; the package refuses to be
ready before.

**Q2. Order with version 1.** This act's subject is the policy as version 1
leaves it. *Recommended:* sign version 1 first in the same sitting, then this
one. Each policy act breaks the Butlers read gate until its code re-pin lands
(the version-1 ledger lists the set), so the second act repeats that re-pin;
the recorded continuation should cover both, and the code change should be made
once against the final bytes. [Inferred] The alternative, signing only this one,
is impossible: its base requires version 1.

**Q3. design/ and specification text.** The request asked whether a design
folder belongs here. RFC5-14 puts design, specification and decision text in
`governance-text`, which this policy leaves unmapped. The design directory is
withheld. Note the tension: root files named DESIGN, GOVERNANCE, SECURITY or
ARCHITECTURE are mapped at the lead's direction, and a reviewer may find one of
them is governance-text by RFC5-14; the file name, not its content, decides.
*Recommended:* keep the directory withheld, and confirm or strike those four
root names. The alternative is a separate closed rule for that class, offered with
its own review, not folded into prose.

**Q4. Nested READMEs.** Only the root README is mapped, because a README below
the root outside docs is often a vendored library's. *Recommended:* accept. For
Redis the cost is that bundled-library READMEs stay withheld, which is the
safer side.

**Q5. The paths themselves.** The names and folders in the rule are a proposal
[Inferred] from the class text; a file outside them is withheld, never guessed.
Adding a name later is a further version.

## What it does not do

It loosens no secret or active-content screen, grants no consent or egress,
admits no repository, and defines no class (PR #257 does).
