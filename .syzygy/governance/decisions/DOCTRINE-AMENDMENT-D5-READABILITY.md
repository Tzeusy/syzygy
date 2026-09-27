# Doctrine amendment D5 — readability rewrite

> **Status:** Proposal. It binds nothing until the owner adopts it (VIS-4).
> The owner adopts by saying so plainly; no phrase or digest is required
> (D1 precedent).

## What it does

It rewrites all six files in `../doctrine/` for readability, following the
owner's direction of 2026-09-27: prioritize concision, human readability, and
maintainability, with no proof of strict semantic equivalence. Dense
paragraphs become short lists; the V0/V1 success tests become a table;
sentences are shorter and use plainer words.

It also absorbs two pending editorial amendments:

- **P-25(a).** The three "README glossary" citations now name the file
  (`governance/doctrine/README.md`).
- **P-25(c).** The glossary gains the *actuator / actuator toolchain* bullet
  drafted in `../contracts/candidates/policy-candidates/DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md`,
  lightly condensed. That packet flags one inferred sentence for the owner to
  confirm or strike: *"Agent toolchain" and "actuator toolchain" name the
  same role.*

The amendment log moves from the doctrine README to
[`DOCTRINE-AMENDMENT-LOG.md`](DOCTRINE-AMENDMENT-LOG.md), so doctrine carries
only current text.

## What stays fixed

Other artifacts cite these by name or position, so each is unchanged:

- every rule identifier and rule title (`VIS-1`–`VIS-7`, `SEC-1`–`SEC-5`), in
  the bold lead-in form the directive register parses;
- VIS-1's five ranks and their order; VIS-6's exceptions (a) and (b); the
  trust floor's four bullets and their order;
- every section heading cited elsewhere ("Glossary (read first)", "One
  kernel, three surfaces", "Status claims vs narrative claims", "Not an
  enforcement engine", and the rest);
- the two sentences pending amendment D3 anchors on (the loop paragraph in
  architecture.md and the "Not autonomous." bullet in vision.md).

## Judgment calls for the owner

1. **One new inferred sentence.** The glossary's substrate bullet now says the
   `/th-*` skills "are published as the public ai-bootstrap toolchain that
   v1.md names". [Inferred] P-25(a) had left *ai-bootstrap toolchain*
   undefined. Strike the sentence if it names the wrong thing.
2. **The actuator identity sentence** described above (from P-25(c)).
3. **Wording that could be read as a shift.** None is intended. The places a
   reviewer should check are VIS-4 (the adjudication-gate conditions, now a
   two-item list), VIS-5 (split into four short paragraphs), and VIS-6(a)
   (the dismissal-expiry clause, reworded).

## Blast radius

- **Generated views**, regenerated in the same change:
  `DIRECTIVE-REGISTER.md`, `05-CONTRACT-INDEX.yaml`,
  `CONTEXT-BUDGET-REPORT.md`, and the digest and word-count anchors of the ten
  context-selection fixtures (CG-18). No performed act's manifest binds any of
  them.
- **Pending doctrine packets.** P-25(a) and P-25(c) close on adoption. D3
  (P-5) pins pre-D5 doctrine digests and line numbers, so it must be
  re-anchored before it is offered. Its two anchor sentences are unchanged.
- **Line-number citations** of doctrine in historical records (round
  reviews, pursuit JSON) stay as they are: they describe the bytes of their
  own date.
- **Runtime code.** Nothing reads doctrine from the working tree;
  `self-corpus.ts` reads a pinned commit.

## Review

VIS-3 requires a fresh-reader review on material amendment. One independent
reader, given only the old and new files, restated every rule from the new
text alone and then audited the new text against the old for drift. The raw
output is [`DOCTRINE-AMENDMENT-D5-READABILITY-REVIEW-1-RAW.md`](DOCTRINE-AMENDMENT-D5-READABILITY-REVIEW-1-RAW.md),
with verdict **CONFIRM WITH EXCEPTIONS** and no material findings.

How its findings were handled:

- **B1–B8** (minor drift: dropped qualifiers, "must" softened to a
  description, one narrowed prohibition, "drives" for "harnesses") — each
  applied with the reviewer's suggested wording.
- **N1** (which substrate v1.md's ai-bootstrap sentence names) — applied as
  "initial *actuator* substrate". This joins judgment call 1 above.
- **N3** (the actuator bullet cited VIS-6 for code writes) — citation reduced
  to VIS-5.
- **N2** (the actuator bullet counts "a human working by hand", while VIS-5
  says materialization is only ever "a worker acting on scheduled work") —
  left for the owner, as part of judgment call 2.
- **Task A clarity notes 1–10** describe the adopted text as much as the
  rewrite; none was introduced by D5. They are left for a later amendment.

By the owner's direction, the fixes were not sent for a second review round.

## On adoption

1. Fill D5's date and the owner's words in `DOCTRINE-AMENDMENT-LOG.md`, and
   change this packet's status to adopted.
2. Merge the branch.
3. Close P-25 and P-25(c) in `PENDING-OWNER-DECISIONS.md`.
