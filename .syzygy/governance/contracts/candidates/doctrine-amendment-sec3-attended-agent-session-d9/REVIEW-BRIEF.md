# Review brief — D9 doctrine amendment packet (SEC-3), rounds 1 and 2

> **Candidate — binds nothing.** The brief for one fresh-context review of
> this package (CC-REV-1). A review is evidence for the owner. It adopts
> nothing, and its verdict is not an owner act (VIS-4).
>
> **Round 2 (2026-10-06).** Round 1 returned `REVISE` (raw:
> docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md, which the lead retains). Each
> finding was repaired once (`ROUND-1-DISPOSITIONS.md`). Round 2 is the
> confirming round, and the stopping rule below applies to it unchanged.

## Stopping rule, set before the round

Agreed before round 1 so it is not invented after a REVISE:

- `CONFIRM` clears the bytes.
- `CONFIRM WITH EXCEPTIONS` with notes only also clears them. The notes go
  in a sibling record, and the reviewed bytes are not repaired (the owner's
  2026-09-26 notes-only rule).
- `REVISE`: the drafter repairs each finding once and records the finding
  and its repair in `ROUND-1-DISPOSITIONS.md`. Round 2 then confirms. A
  second `REVISE` goes to the owner with both raws; no round 3 is
  dispatched without the owner.

A verdict is never re-labelled.

## Subject

The tracked files of
`.syzygy/governance/contracts/candidates/doctrine-amendment-sec3-attended-agent-session-d9/`
at the reviewed commit: `OWNER-DECISION-PACKET.md`, `SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`, `ROUND-1-DISPOSITIONS.md`. The
proposed doctrine text is in the fenced blocks under the delta's "Proposed
meaning": arm A, arm W, their optional `v1.md` clauses, and the removable
credential lines.

## Governing references

Read these, and nothing else is needed:

- Doctrine: `.syzygy/governance/doctrine/security.md` (whole file),
  `v1.md` ("Platform and audience"), `README.md` (glossary, and "Doctrine
  is slow to change"), `vision.md` VIS-3 and VIS-4.
- Owner directions, all in `.syzygy/governance/decisions/`:
  - `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`;
  - `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md` (item 2);
  - `POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`;
  - `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md` (item 1,
    the owner's choice and the two options declined).
- Amendment ceremony: `decisions/DOCTRINE-AMENDMENT-LOG.md`,
  `decisions/DOCTRINE-AMENDMENT-D5-READABILITY.md`,
  `decisions/DOCTRINE-AMENDMENT-D6-TREE-STYLE.md`.
- Accepted contracts: RFC5-18 to RFC5-24 and the package reader map
  (`contracts/rfcs/RFC-0005/`), RFC3-16(a)
  (`contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`), RFC4-12
  and RFC4-13 (`contracts/rfcs/RFC-0004/named-adapters.md`), RFC9-33.
- Craft: `policies/craft-and-care/security-and-secrets.md` (CC-SEC-3 and its
  preamble).
- Added for round 2:
  - RFC5-12 (`contracts/rfcs/RFC-0005/consent-egress-secrets.md`);
  - `decisions/POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`;
  - `apps/three-surface-poc/src/capture-test-artifact-main.ts` and
    `docs/THREE-SURFACE-POC.md` ("Capturing test-run evidence");
  - `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md` (finding 8).
- `contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` and
  `SEMANTIC-DELTA-TEMPLATE.md`.

## Acceptance criteria (from the owner's direction and the lead's task)

1. The amendment permits the owner's ruling and nothing more. Observed code
   still never runs inside Syzygy, or under anything Syzygy launches or
   schedules, outside a profile. The owner's own attended agent session may
   run it on the owner's host when the owner chose that, provided that:
   - Syzygy never issues the instruction without the owner's recorded
     choice;
   - every claim resting on that execution is Inferred;
   - the commands are disclosed.
2. "It is untrusted whoever owns the project" is kept intact.
3. The violation example is kept. The text says why the attended session is
   not the forbidden profile, or narrows the example honestly.
4. The owner's trade-off is preserved in the text: the owner declined a
   sandbox-only option and a forbid option.
5. Every clause, specification and contract that cites SEC-3 is identified,
   with a stated effect on its meaning.
6. Nothing is adopted, no doctrine byte is edited, and there is no code.

## What to test, at least

- **Minimality.** Does the proposed text permit anything beyond criterion 1?
  Press on "attends", "the owner's own host", "launches or schedules", and
  the generality the ledger discloses (§5 item 5). Is clause (b) needed, or
  is `v1.md` already true as written?
- **Honesty of the violation sentence.** Is "The attended session is not such
  a profile: it claims no containment …" a real distinction, or does it hide
  that observed code reaches ambient credentials either way? Does the cost
  bullet state that plainly enough?
- **Contract fit.** Is RFC5-18 really scoped by RFC5-19's "profiles govern
  only code Syzygy itself launches"? Is a brief that Syzygy issues, telling
  the session it may run code, "Syzygy launching"? Does the RFC-0005 reader
  map's "no observed-project code executes until …" create a conflict that
  only a contract amendment can resolve (packet Q3)?
- **CC-SEC-3.** Is the packet right that the clause's own "Doctrine's text
  prevails" line governs the gap until a policy amendment (packet Q2)?
- Does any quotation differ from its source? Re-derive the anchors' sha256
  and line numbers at the reviewed commit.
- Re-run the ledger's sweeps (§1, §2) and the application probe (§4). Do
  the figures and lane sums hold?
- Is the change class (Normative, widened) right?
- Is the packet written so that the owner can decide without reading the
  delta?

## Round 2: what to test, at least

- Is each round-1 finding resolved, partly resolved, or not, by the repair
  recorded for it? Re-derive rather than trust the dispositions.
- **Arm A against criterion 1.** Does it permit the ruling and nothing
  more? Test it against `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  line 56, "In the local-agent mode the operator's agent session may
  build and run the observed project". Does naming Syzygy as the actor
  claim jurisdiction the current text lacks, or give some up silently?
  Is Q2 put fairly?
- **The violation sentence under each arm.** Is it exact (R1)?
- **RFC5-12 and RFC5-24.** Are the quotations exact? Is each arm's effect
  stated correctly? Does condition 4 keep RFC5-24 true, and is Q3's cost
  honest? An effect change on an accepted contract is reported for the
  owner, not resolved.
- **The capture tool.** Is the reading "non-conforming today, independent
  of D9" right? Is its effect under each arm stated correctly?
- **The removable credential lines.** Does deleting them leave each arm
  grammatical and exact?
- Re-run the ledger's sweeps (§1, §2) and the arm A application probe (§4)
  at the reviewed commit.

## Output

Round 1 wrote docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md. Round 2 writes
docs/reviews/R-DOCTRINE-AMENDMENT-D9-2-RAW.md, a file that round creates. Its
first four non-blank lines must be exactly:

```text
# Review - D9 doctrine amendment packet, round 2 (SEC-3 attended agent session)
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

Package digest method: at the repository root of a clone at the reviewed
commit, run
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-sec3-attended-agent-session-d9 | LC_ALL=C sort) | sha256sum`.

Number every finding, label each `[Observed]`, `[Inferred]` or `[Unknown]`,
and mark each as revise-level or a note. Any finding that the amendment
changes an accepted contract's effect is reported for the owner, not
resolved.
