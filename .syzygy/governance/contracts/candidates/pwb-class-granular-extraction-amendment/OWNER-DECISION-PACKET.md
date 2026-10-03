# Owner decision packet — PWB class-granular extraction amendment (M15)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts five questions to the owner, and only the
> owner's answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 under your ruling P-82 (A) of 2026-09-21, on
bead `syzygy-dov.15.1`. The review round's verdict and its dispositions are
in `ROUND-1-DISPOSITIONS.md` beside this file, which also says whether this
version is ready to offer.

## What you would be signing

One amendment to PWB-REQ-002 and the reader definitions it reads by, in the
signed PWB specification. Read `SEMANTIC-DELTA.md` for the full account. In
short:

- **One bad class no longer wipes its neighbours.** Today one grammar defect
  in a source makes the whole source Unknown, throwing away classes that
  read fine. At one earlier Butlers revision the whole V1 index went Unknown
  this way; on a later capture its three classes held 75 items. After this,
  only the failing class goes Unknown; the others keep their items. The
  source is shown as *partially extracted*, class by class.
- **A heading nobody declared is shown, not skipped.** If the V1 catalog
  gains a tenth category, today nothing counts it and nothing says Unknown.
  After this, the extra heading is listed with a link to its source, and
  the catalog's count reads Unknown until it is declared.
- **Counts made without the root index say so.** Every source rule now says
  whether it needs Butlers' root index. If the root index cannot be read,
  rules that need it mint nothing, and baseline-spec and roster counts,
  which do not need it, carry a note that they were made without it.

**What it touches besides PWB-REQ-002 and the reader definitions.** A
proposal bullet, design decision 12, capability row 34, and the regenerated
dependency file. No other requirement, no contract-coverage row, no warrant.

**What signing does not do.**

- **It starts no implementation.** You ruled "build only after sign-off and
  a fresh authorization". That authorization is separate.
- **It reads nothing new.** No Butlers body is read beyond the consented
  class.
- **It changes nothing visible on Butlers today, as far as is known.**
  Butlers' root index reads, and the latest recorded run had no grammar
  failure. One exception is [Unknown]: whether the V1 index has another level-3
  heading beside the catalog's nine. If it does, the catalog count would read
  Unknown once this is built. No Butlers body was read to find out.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | The patches are applied in the sign-off change by version tag (Scope A covers PWB specification deltas). PWB-REQ-002 gains three scenarios. |
| Decline | PWB-REQ-002 stays as signed: one failing class keeps making its whole source Unknown. |
| Revise | Name what to change, and a new version gets a new review round. |

## Question 2 — how an unenumerated heading is counted

You ruled it a "surface-flag (a counted, routed Unknown)". The draft reads
"counted" as: the number of extra headings is shown, and the class's count
for that source is Unknown.

| Option | Meaning |
|---|---|
| **Count Unknown, list the headings** (recommended; this version) | The nine headings' items stay modeled; the catalog count reads Unknown with the reason `unenumerated-heading` and the number of extra headings. Nothing under an extra heading is guessed. |
| Count each extra heading as one Unknown item | The count stays a number. But the items under the heading are not read, so that number would be wrong. |

## Question 3 — are baseline specs and roster directories root-independent?

Their paths are fixed in the specification, not named by the root index.

| Option | Meaning |
|---|---|
| **Independent, with a note** (recommended; this version) | With the root index unread, they are still counted, and every count that includes them says it was made without the root index. Butlers' manifest is unchanged. |
| Dependent | With the root index unread, they mint nothing and read Unknown. Safer, but it hides counts the Git tree already proves. |

## Question 4 — which rows can have unenumerated headings?

| Option | Meaning |
|---|---|
| **List and table rows naming two or more headings at one level** (recommended; this version) | Covers the V1 catalog and any profile row shaped like it. Rows that read a heading's section are left out, so the V1 index's other level-2 headings are never flagged. |
| The V1 catalog only | Narrower. A profile row of the same shape would still skip an extra heading silently. |

## Question 5 — order against the release-label amendment (P-85)

Both packages add a design decision 12 and a capability row 34. Their
specification changes do not overlap.

| Option | Meaning |
|---|---|
| **Whichever is ready first lands first** (recommended) | The second is regenerated over the first's applied bytes, renumbered and reviewed again before it is offered. |
| This one waits for P-85 | It is regenerated after P-85 is signed or declined. |

**If unanswered,** nothing is signed and the package stays a candidate.
