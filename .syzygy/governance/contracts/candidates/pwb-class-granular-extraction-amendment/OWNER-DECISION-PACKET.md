# Owner decision packet — PWB class-granular extraction amendment (M15)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts seven questions to the owner, and only the
> owner's answer binds anything (VIS-4). *(Marked 2026-10-14: the cycle-2
> repairs added question 8, so the packet now puts eight questions.)*

**Status:** drafted 2026-10-03 under your ruling P-82 (A) of 2026-09-21, on
bead `syzygy-dov.15.1`. Round 1 returned `REVISE`: findings 1–9 were
repaired and finding 10, which named residual risks, changed nothing
(`ROUND-1-DISPOSITIONS.md`). Round 2, over the repaired bytes on bead
`syzygy-418x`, also returned `REVISE`: one revise finding and seven notes
(`ROUND-2-DISPOSITIONS.md`). On 2026-10-14 you directed one new version
repairing all eight, then one fresh round. **All eight round-2 findings
were repaired once on 2026-10-14. These bytes are unconfirmed, pending
round 3** *(marked 2026-10-14: round 3 ran at `00e24fd2` and returned
`REVISE`, one revise finding and four notes, `ROUND-3-DISPOSITIONS.md`)*,
and are not cleared to sign until a round over them returns
`CONFIRM`, or `CONFIRM WITH EXCEPTIONS` with notes only. The repairs added
question 7 below; questions 1–6 are unchanged except where round 2 asked
for it (question 4's recommended arm, finding 5).

On 2026-10-14 you directed one more cycle. **Round-3 findings repaired
once on 2026-10-14, unconfirmed pending round 4.** The repairs state which
rule names a source that two rules admit (round-3 finding 1), which adds
question 8 below and a fourth new scenario; the four notes changed only
the builder's selftest, one scenario line and the package's own prose.
Questions 1–7 are unchanged except question 1's count of scenarios.

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
  which do not need it, carry a note that they were made without it. Each
  source also names the rule that admitted it, from five names bound to the
  four signed rules; the root index itself is filed under the first rule,
  as today's code files it.

**What it touches besides PWB-REQ-002 and the reader definitions.** A
proposal bullet, design decision 12, capability row 34, and the regenerated
dependency file. No other requirement, no contract-coverage row, no warrant.

**What signing does not do.**

- **It starts no implementation.** You ruled "build only after sign-off and
  a fresh authorization". That authorization is separate.
- **It reads nothing new.** No Butlers body is read beyond the consented
  class.
- **It changes nothing visible on Butlers today, as far as is known.**
  [Observed] The latest recorded run, at Butlers `32f38feb`
  (`docs/evidence/smooth-example-live-run-2026-10-03.json`), has 9 sources
  with an Unknown item denominator, and they are the 9 withheld ones, equal
  per source (that record's `unknownDenominatorWithheldComparison`, added in
  `b044a756`); none is Unknown for a grammar failure. One exception is [Unknown]: whether the
  V1 index has another level-3 heading beside the catalog's nine. If it
  does, the catalog count, and the V1 index's own count, would read Unknown
  once this is built. No Butlers body was read to find out.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended only once a round-4 dispositions record beside this file records the repaired bytes cleared; until 2026-10-14 this said round 3) | The patches are applied in the sign-off change by version tag (Scope A covers PWB specification deltas). PWB-REQ-002 gains four scenarios (three until the 2026-10-14 cycle-2 repairs). |
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
| **List and table rows naming two or more headings at one level** (recommended; this version) | Covers the V1 catalog and any profile row shaped like it. Rows that read a heading's section (`heading-section`) are left out, so Butlers' V1-scope row does not flag the V1 index's other level-2 headings. The rule does reach further for other row shapes: a loaded profile's list or table row naming two or more level-2 headings would flag every level-2 heading in its level-1 section (or file) that no row declares. Butlers' written grammar has no such row (its one multi-heading list row is the level-3 catalog), so nothing changes for Butlers. |
| The V1 catalog only | Narrower. A profile row of the same shape would still skip an extra heading silently. |

## Question 5 — order against the release-label amendment (P-85)

Both packages add a design decision 12 and a capability row 34. Their
specification changes do not overlap.

| Option | Meaning |
|---|---|
| **Whichever is ready first lands first** (recommended) | The second is regenerated over the first's applied bytes, renumbered and reviewed again before it is offered. |
| This one waits for P-85 | It is regenerated after P-85 is signed or declined. |

## Question 6 — the root-summary and precedence half of Q3

The funnel's Q3, which you ruled on, named "a level-3 catalog heading
outside the closed vocabulary, or an unenumerated root-summary or precedence
heading". This package designs only the first. Those root grammars belong
to PWB-REQ-004, and the drafter read the record's gloss ("One CC-REV-2
semantic delta to PWB-REQ-002") as narrowing the package. That gloss is not
your words.

| Option | Meaning |
|---|---|
| **Defer to a separate PWB-REQ-004 delta** (recommended) | This package stays on PWB-REQ-002. A second package, drafted after this one is signed, carries the root grammars. Until then an extra root-summary or precedence heading is still skipped silently. |
| Widen this package | It also amends PWB-REQ-004, and needs a new review round over the wider bytes. |

## Question 7 — when does the root index count as read? (added 2026-10-14)

Round 2 found that "the root index was not read" was undefined for a root
index whose body reads but whose grammar fails. The repair chose a reading,
and it is yours to confirm.

| Option | Meaning |
|---|---|
| **Read means its body was read** (recommended; this version) | If the body reads, the root index is read even when part of it fails its grammar. A pillar root it does not name clearly leaves that pillar's files out, and a root-summary or precedence table that fails is reported as that table's failure. Baseline-spec and roster counts carry no "made without the root index" note, because they never use the root index's grammar. This matches how today's code records the root index. |
| Read means its body read and its grammar held | Any root-grammar failure also counts as an unread root index. The pillar rules would then mint nothing from any pillar, and baseline-spec and roster counts would carry the note whenever any root table fails, though nothing in those counts came from that table. |

## Question 8 — which rule names a source that two rules admit? (added 2026-10-14, cycle 2)

Round 3 found the rule names undecidable for a file two rules admit. That
can happen on Butlers: the code's own comment says Butlers declares its
Spec and Spine pillar at `openspec/`, so that pillar's index can name a
baseline spec that rule 3 also admits. Today's
code settles it by an order the text never stated. The repair writes an
order into the text; it is yours to confirm.

The order as drafted: the root index is always `root-index`; a pillar's
index file is always `pillar-index`; a baseline spec or roster
`butler.toml` keeps its tree rule's name and class whoever else names it;
any other file a pillar's index names, a roster `MANIFESTO.md` included, is
`pillar-named-file`. For a loaded profile, a file one of its tree
populations admits keeps that population's name, and a file two of them
admit takes the first the profile declares.

| Option | Meaning |
|---|---|
| **The order as drafted, code changed at build where it differs** (recommended; this version) | For Butlers it is today's code in every case but one. The exception needs one declared pillar root inside another: the code files that inner pillar's index as a named file of the outer pillar, and the text files it as a pillar index. Whether Butlers has nested roots is unknown (no Butlers body was read). The build would change the code for that case. The loaded-profile clauses follow the code's reason for rules 3 and 4: the tree rule carries the class. No loader exists yet, so no code changes for them. |
| The code's order, written into the text | The text says sources are registered pillar by pillar in a fixed pillar order, and the first registration wins, with the same tree-rule exception. No code changes. A nested pillar's index would lose its pillar-index classes. |

**If unanswered,** nothing is signed and the package stays a candidate.
