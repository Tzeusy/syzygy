# Review — Polaris retained-evaluations retention posture decision packet
Reviewed commit: 4ddb1939bcd178e5212c5b6f4b217387302b3a65
Artifact SHA-256: 2d8a89ff81ca682e1f662b24a2df36982d9725ece61698bf0b9a7841875777a5
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the packet was not
read before setup, and no commit message body was read for this artifact.
Read-only throughout the repository; every mutation-shaped check below was a
text comparison, never a live mutation, so no scratch copy was needed. Class:
fresh-reader semantic review of an inert candidate owner decision packet
(CC-REV-1, CC-REV-6).

---

## What I ran

1. `git fetch origin && git checkout -B review/retention-posture-packet
   4ddb193` → switched to a new branch at `4ddb1939bcd178e5212c5b6f4b217387302b3a65`.
2. `git status --porcelain` → empty, before any edit.
3. Read the artifact in full:
   `.syzygy/governance/decisions/POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md`
   (564 lines).
4. Read the governing references named in the brief in full or at the cited
   line ranges: `AGENTS.md` (pinned commit); `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
   in full; `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` in full;
   `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (write-surface lines);
   `THREE-SURFACE-POC-MODE-DIRECTION.md` and
   `POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md` (heads, for the plain-
   direction shape); `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`
   lines 75–110, 960–1340, 1330–1600; `vision.md`, `security.md`,
   `architecture.md` (cited line ranges plus `grep -n "^\*\*VIS-"` /
   `"^\*\*SEC-"` to confirm line anchors); `trust-and-evidence.md` lines 1–20
   and 95–110; `review-and-documentation.md` CC-REV-6.
5. Wrote a Python script (`/tmp/.../scratchpad/extract_blockquotes.py`) that
   parses every contiguous `>`-prefixed block in the artifact by line range.
   Output: **11 blocks**. Block 1 (lines 4–11) is the packet's own candidate
   banner, authored by the packet, not attributed to an external source. The
   remaining **10** are attributed quotes.
6. Wrote a second script
   (`/tmp/.../scratchpad/compare_quotes.py`) that, for each of the 10
   attributed blocks, reads the exact source line range the packet's prose
   names, strips the `> ` prefix, collapses whitespace in both packet and
   source text (to neutralize re-wrapping at a different column width, not a
   content difference), and compares. Read the printed output, not an exit
   code. Result: **9 exact matches, 1 initially reported MISMATCH**
   (VIS-5) that was my own script's off-by-one line range (I sliced one
   source line short); re-run against the correct range
   (`vision.md` 141–146, truncated at the sentence-ending "universe.") gives
   an exact match. **Corrected result: 10 of 10 attributed blockquotes match
   their cited source bytes exactly** (one, the trust-and-evidence.md 10–16
   quote, is a disclosed intentional mid-sentence truncation — the packet
   says so in prose — and matches as an exact prefix through the sentence
   boundary it names).
7. Grepped the artifact for double-quoted inline fragments (not
   blockquotes) attributed to a source (`grep -n '"'`) and checked each
   against its source: P-79's "Q1 yes, a retention-posture change needing an
   owner act before slice 1" and "Nothing in M12 is ready: slices 1–2 wait
   for the retention act" (exact, against the P68–P83 record's own table
   row); "claim identity plus epistemic tuple and challenge state only" and
   "the on-disk total rendered beside the delta" (exact, against the same
   row's ruled text); `"never"` on `rawBodyHandling` (exact, against
   `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`
   lines 178–184, all five members); "in any Syzygy surface, store, or
   endpoint" (exact, SEC-5); "No implementation code inside `openspec/**` or
   `.syzygy/**`" (exact, `AGENTS.md` line 81 at the pinned commit); one
   mismatch found and reported as Finding 1 below.
8. `grep -n "interface ProjectShapeClaim" -A 20
   packages/three-surface-poc-core/src/project-shape-model.ts` → confirmed
   the type carries exactly six fields (`claimId`, `evaluationId`,
   `epistemic`, `resolutionRoutes`, `challenge`, `support`), matching the
   packet's table of what is retained (3), carried once in the envelope (1)
   and dropped (2).
9. `grep -n "writeSurface"
   .syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
   → line 125, `"writeSurface": []`, matching the packet's citation.
10. `grep -n "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE"
    PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` → confirms the registry
    file is the digest-bound artifact identity of that act, matching the
    packet's "digest-bound" claim.
11. `grep -n "empty write surface\|No write, egress"
    PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` → lines 70/72, matching the
    packet's quote in "What the direction would not authorize" §3.
12. `bd show syzygy-dov.28` → confirms the gate bead exists, is open, and its
    description matches the packet's account of what it gates.
13. `grep -n "STATE_DIR_MODE\|RECORD_FILE_MODE"
    materialization.ts test-artifact-verification.ts` → both existing
    writers use `0o700`/`0o600`, matching the packet's "same posture, byte
    for byte" claim and invariant I8.
14. `awk` line-length sweep over the artifact for lines >79 chars, and a
    Python odd-backtick-count sweep over every non-fence, non-table-row line
    (the AGENTS.md wrapped-citation method) → the only long lines are table
    rows (94–98, 253–264) and one fenced verbatim reply line (514), both
    legitimate exceptions to prose wrap; **zero** lines with an odd inline
    backtick count, so no broken code span.
15. `grep -oE '`[^`]+`' <artifact> | sort -u` → 43 distinct backticked
    spans, all Syzygy-tree paths, doctrine files, decision files, or bare
    identifiers/labels (`[Observed]`, `claimId`, mode octals, the short
    commit `a9f671e`, the gate bead id). **Zero** Butlers paths, **zero**
    performed-act digests (no 64-hex string anywhere in the file).
16. `python3 scripts/check_governance.py` (full run, read the printed
    summary, not the exit code): **32 OK, 20 WARN, 0 FAIL (52 checks)**.
    `grep -i "RETENTION-POSTURE"` over the full output → zero hits: the
    artifact appears in no OK, WARN or FAIL line. All 20 WARNs are
    pre-existing findings against other files (CG-19b, CG-22b, CG-23, CG-24,
    CG-25, CG-27), none naming this packet.

## Findings

**F1 [revise] — one inline quote drops three words from its source without
an ellipsis.** `.syzygy/governance/decisions/POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md:58-60`
reads: `it "binds no artifact bytes, adds no row to the acceptance-act
record and registers nothing"`. The source,
`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`'s HTML head comment,
reads in full: "it binds no artifact bytes, adds no row to the
acceptance-act record and registers nothing **in CG-7e**." The packet's
quotation marks close before "in CG-7e" with no ellipsis marking the cut.
Violated expectation: acceptance criterion 1 is scoped to blockquotes and
this is an inline quote, so it is not a blocking violation of that
criterion by its letter — but the file's own discipline elsewhere is to
either quote a clause to its natural boundary or mark a cut, and every
other inline quote I checked (F7 above) does. Repair: quote through "in
CG-7e", or close the quotation mark one clause earlier at "registers
nothing" with an explicit "…" if the drafter wants the CG-7e detail
omitted as not load-bearing here.

**F2 [note] — the SEC-4 reading is defensible but rests on an undefined
term without its strongest supporting cross-reference.** `security.md:47-52`
never defines "governed repository," and neither does `vision.md`. The
packet's reading (lines 186-193: "SEC-4 governs writes *into a governed
repository*... The retained record is written into neither the observed
repository nor Syzygy's governed plane, so SEC-4 is not the clause that
permits it and is not the clause that forbids it") is well supported by
context — SEC-4's own "per-repository consent (onboarding)" phrase and
VIS-5's *Violation* line ("Syzygy committing a source-file edit to a
governed repository") both point at an external observed project, never
Syzygy's own `openspec/**`/`.syzygy/**` plane — and I agree with the
reading. But the packet cites neither VIS-5's *Violation* line nor any
other clause to anchor "governed repository" to that reading; it is
asserted, not shown. Repair: one clause citation (VIS-5's *Violation* line
is the cleanest) would move this from asserted to anchored, per
verification rule 8.

**F3 [note] — the doctrine test omits the one doctrine clause that names
"retention" verbatim as a gating trigger.** `vision.md:122-140` (VIS-4)
reads in part: "One class is always human-gated, gate open or not: spec
changes touching security posture, privacy or retention obligations, or
normative data contracts." The packet's "doctrine test" section (VIS-6,
VIS-2, SEC-5, SEC-4, the temporal rule) never mentions VIS-4. The omission
is defensible — VIS-4 gates *OpenSpec specification* amendments, and this
packet's actual gate is the continuation act's implementation-posture
escalation trigger, a different and correctly-cited mechanism, since
nothing here amends `openspec/**` text — but a reader who greps doctrine
for "retention" before reading this packet will find VIS-4 first and may
wonder why it goes unaddressed. Repair: one sentence distinguishing VIS-4's
spec-amendment gate from the continuation act's implementation-posture
gate would close the gap and costs little.

**F4 [note] — the envelope's "six keys" count is not fully spelled out
against the shown record shape.** "What is the drafter's and not yours" §1
(`decision-packet.md:411-415`) says the drafter "closed it at six keys."
The record shape shown at lines 88-99 groups the evaluation identity under
one `evaluation` object and both counts under one `counts` object, i.e. five
top-level envelope keys (`schema`, `evaluation`, `observerRevision`,
`projectRevision`, `counts`) unless the two counts are meant to be flattened
to their own keys, which would make six. The direction text (clause 1) lists
the same content without settling which shape it is. This is not a
disclosure-accuracy problem — every field named is fully enumerated either
way, and the owner is told exactly what is retained — but it is arithmetic
the implementing bead will have to resolve rather than read off the
direction, and invariant I3 ("the envelope is closed at the declared keys")
needs that shape settled before its key-set assertion can be written.

## Summary of what held up

- Every blockquote and every checked inline attributed quote, except F1,
  matches its cited source exactly (10 of 10 blockquotes; 6 of 7 checked
  inline quotes).
- The retained-field table matches `ProjectShapeClaim`'s actual six fields
  exactly, and correctly separates "retained per claim" (3), "carried once
  in the envelope" (`evaluationId`) and "excluded" (2).
- Unbounded retention, its exclusive home in the daemon's state directory,
  and the explicit non-authorization of any write into an observed
  repository are all stated in terms that leave no sentence reachable as
  authorizing a Butlers write, and the P-71-Q5 foreclosure and the
  registry's empty `writeSurface` are both accurately cited.
- The "not authorized" list is comprehensive over dismissal, note
  promotion, observed-repository writes, and any new route or ceiling, and
  the packet's own banner and §(c) both state that silence, a partial
  answer, or a merge performs nothing.
- All twelve invariants name a concrete falsifying mutation.
- `scripts/check_governance.py` reports 0 FAIL and never names this file in
  any OK/WARN line; no backticked Butlers path, no performed-act digest, no
  broken code span, no line over 78 columns outside a table row or the
  fenced verbatim reply text.
- The packet correctly declines to restate `bd ready`-owned readiness state
  and correctly does not draft the record file it describes.

## Rubber-stamp risk, named per CC-REV-6

Even confirming, the concrete risk in shipping this as-is: F1's dropped
clause is the kind of small, unflagged cut that this corpus's own notes
(`AGENTS.md`'s "citation wrapped" and "quote a clause to its ending, never
past it" discipline) treat as exactly the failure mode that compounds —
one silent three-word cut in a governance artifact that will itself become
a cited precedent for the next "plain owner direction" packet. It costs one
edit to fix and should be fixed before the owner is asked to rule on this
packet, even though nothing here changes the substance of the decision put
to them.
