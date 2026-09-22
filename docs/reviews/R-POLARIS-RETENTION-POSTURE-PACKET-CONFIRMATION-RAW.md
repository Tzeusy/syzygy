# Review — Polaris retained-evaluations retention posture decision packet (confirmation pass)
Reviewed commit: fab7fb3c5550f62dabc2df723e490d0bae3a834d
Artifact SHA-256: 572e6c4ba7881483d4807c1729298c0ed790feeff9000fff94e136b2a037ce91
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context session. No authoring context; the repair diff was
not read, only the finished artifact and the governing references it
quotes. Read-only throughout; no mutation was made to any input, so no
scratch copy was needed. Class: fresh-reader confirmation review of a
repaired candidate owner decision packet, second pass (CC-REV-1, CC-REV-6).

---

## What I ran

1. `git fetch origin && git checkout -B review/retention-posture-confirmation
   fab7fb3` → switched to a new branch at
   `fab7fb3c5550f62dabc2df723e490d0bae3a834d`. `git status --porcelain` →
   empty, before any edit and again at the end (only this file added).
2. Read `AGENTS.md` in full, the prior raw review
   (`docs/reviews/R-POLARIS-RETENTION-POSTURE-PACKET-RAW.md`, verdict CONFIRM
   WITH EXCEPTIONS, F1 revise / F2–F4 note), and the artifact in full (657
   lines — see Finding N1 on the packet's own count).
3. Read every governing reference the packet cites, at the packet's own
   line numbers, and confirmed each against source with `sed -n` plus
   `grep -n`: `vision.md` VIS-2 (96–106), VIS-4 (122–140, and the 131–133
   sub-quote), VIS-5 (141–166, its 162–165 *Violation* clause), VIS-6
   (167–181); `security.md` SEC-4 (47–52), SEC-5 (54–60); `trust-and-
   evidence.md` 10–16 and 99–107; `architecture.md` 221–229 and 231–235;
   `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`'s escalation
   triggers (§ body) and its own HTML-comment self-description ("it binds
   no artifact bytes, adds no row to the acceptance-act record and
   registers nothing in CG-7e"); row P-79 of
   `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`; the registry entry
   `POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` (`writeSurface`
   at line 125); the secret-classification policy's `rawBodyHandling` block
   (lines 178–184, all five members `"never"`).
4. Wrote and ran a Python script
   (`extract_blockquotes.py`) that parses every contiguous `>`-prefixed
   block by line range: **13 blocks total**. Block 1 (lines 4–11) is the
   packet's own candidate banner; the remaining **12** are attributed
   quotes — matching the packet's own claim of 13/12 exactly.
5. Wrote a second script (`compare_blockquotes.py`) that, for each of the
   12 attributed blocks, reads the exact cited source range, whitespace-
   normalizes both sides, and compares. Read the printed output, not an
   exit code. Result: **12 of 12 exact matches** — 8 as full-range matches,
   4 (blocks at packet lines 170–175, 204–207, 344–351, 417–419) as exact
   prefix/suffix substrings of their cited range, each confirmed against
   the packet's own disclosure that the quote starts or stops mid-line at
   a sentence boundary. See Finding N1: the packet's Review section counts
   only **three** such disclosed truncations; I count **four** (see below).
6. Manually enumerated every double-quoted inline fragment outside a
   blockquote (`grep -n '"'` minus blockquote-range lines) and classified
   each as attributed-to-a-named-source or not (self-referential section
   titles, scare-quoted generic words such as "unbounded"/"no change", and
   the Review-table prose are not attributed source quotes). Checked every
   attributed candidate against its named source with `grep -o` (exact
   substring, not normalized): P-79's "Q1 yes, a retention-posture change
   needing an owner act before slice 1"; "Nothing in M12 is ready: slices
   1–2 wait for the retention act"; "claim identity plus epistemic tuple
   and challenge state only" (occurs twice, lines 83–84 and 118–119); "on-
   disk total rendered beside the delta" (and its line-477 fragment
   "beside the delta"); the continuation act's "binds no artifact bytes,
   adds no row to the acceptance-act record and registers nothing in
   CG-7e" (now includes "in CG-7e" — F1 confirmed repaired); `"never"` on
   `rawBodyHandling`, all five members; SEC-5's "in any Syzygy surface,
   store, or endpoint"; AGENTS.md's "No implementation code inside
   `openspec/**` or `.syzygy/**`" (still at line 81 in this commit); the
   VIS-5 *Violation* clause's "committing a source-file edit to a governed
   repository" and "a direct write landing outside `openspec/**` and
   `.syzygy/**`"; SEC-4's "recorded per-repository consent (onboarding)";
   the registry's `"writeSurface": []` at line 125. **Every candidate I
   checked matched its source exactly, zero mismatches.** My own
   enumeration yields 12–14 attributed instances depending on whether a
   repeated identical quote and a two-fragment same-clause citation are
   counted once or per occurrence; I could not independently re-derive the
   packet's declared "11" from a stated rule. See Finding N2 — not a
   content defect (nothing I found is wrong), a denominator-transparency
   gap.
7. `wc -l`, `grep -c ''`, and `awk 'END{print NR}'` on the artifact — three
   independent methods, all agreeing: **657 lines**. The packet's own
   Review section (line 648) states "over all 658 lines." See Finding N1.
8. `python3` odd-backtick-count sweep over every non-fence line, and a
   long-line sweep excluding fenced and table-row (`|`-leading) lines:
   **0** broken code spans, **0** prose lines over 78 columns — confirms
   the packet's claim on both predicates (the denominator is off by one
   per Finding N1, the zero-counts themselves are correct).
9. `grep -oE '\b[0-9a-f]{40,64}\b'` over the artifact → **0** matches (no
   40- or 64-character hex string; `4ddb193` and `a9f671e` are 7-character
   short commit references, not digests). `grep -ni butlers` → **0**
   matches (the observed repository's name never appears).
10. `grep -oE '`[^`]+`'` over the artifact, sorted unique → 55 distinct
    backticked spans, all Syzygy-tree paths, doctrine/decision filenames,
    schema field names, mode octals, short commit hashes, or epistemic
    labels. **Zero** Butlers paths.
11. `python3 scripts/check_governance.py` (full run, read the printed
    summary): **32 OK, 20 WARN, 0 FAIL (52 checks)** — exact match to the
    packet's own claim. `grep -n` for the packet's exact filename in the
    output → **0 hits** (it appears in no OK/WARN/FAIL line). Two lines
    under the CG-1f "frozen-lane path references" WARN bucket (report-
    only, 0 findings) name the *prior raw review's* scratchpad-script
    citations, not the packet itself, and are pre-existing, unrelated to
    this repair.
12. `python3 scripts/check_governance.py --selftest` → **255 fixtures, 0
    failing**.
13. Reread the repaired sections slowly for the F1–F4 repairs themselves
    (acceptance criterion 1), quoted below.
14. Read the `## Review` section's own rule-10 sentence and confirmed it
    correctly states that the retained raw review confirms `4ddb193`, not
    these bytes, and that a confirmation of the repaired bytes is a
    separate review (which this file is).

## F1–F4 repair verification

**F1 (revise → repaired).** `POLARIS-RETAINED-EVALUATIONS-RETENTION-
POSTURE-DECISION-PACKET.md:58–60` now reads: `and of the continuation act
quoted above, which says of itself that it "binds no artifact bytes, adds
no row to the acceptance-act record and registers nothing in CG-7e".` This
runs to the clause's actual end; the source
(`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`'s HTML head
comment) reads "…and registers nothing in CG-7e." — exact match, no more
silent drop. **Repaired as disposed.**

**F2 (note → repaired).** Lines 187–226 ("Where it lives") now quote VIS-
5's *Violation* clause in full (`vision.md` lines 162–165, blockquote
confirmed exact) and cite the registry entry's empty write surface "at
line 125" (confirmed: `writeSurface": []` is on line 125 of
`POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`). The SEC-4
non-applicability reading is now anchored to quoted clause text rather
than asserted. **Repaired as disposed.**

**F3 (note → repaired).** Lines 412–433 ("The doctrine test") now quote
VIS-4's human-gated-class sentence in full at `vision.md` lines 131–133
(blockquote confirmed exact) and state the distinction between VIS-4's
specification-amendment gate and the continuation act's implementation-
posture gate. **Repaired as disposed.**

**F4 (note → repaired).** Lines 100–120 now tabulate the envelope's six
top-level keys by name (`schema`, `evaluation`, `observerRevision`,
`projectRevision`, `claimCount`, `identityCount`), invariant I3 (line 288)
asserts key-set equality over exactly those six with an explicit
falsifying mutation ("nest `claimCount` and `identityCount` under a
`counts` object"), and "What is the drafter's and not yours" §1 (lines
467–475) labels the six-key shape as the drafter's, not the owner's ruling.
**Repaired as disposed.**

## Findings

**N1 [note] — the packet's own `[Observed]` sweep sentence miscounts its
own denominators on two independent measures.**
`.syzygy/governance/decisions/POLARIS-RETAINED-EVALUATIONS-RETENTION-
POSTURE-DECISION-PACKET.md:640–648` is labeled `[Observed]` and states
"three of them as disclosed truncations that begin or end mid-line at a
sentence boundary" and "over all 658 lines." Both figures are off by one,
confirmed by a second method each:

- *Truncation count.* Four blockquotes are explicitly narrated in the
  surrounding prose as starting or stopping mid-line at a sentence
  boundary, not three: the VIS-5 opening at line 168 ("through the word
  ending that third sentence early on line 146"), the VIS-5 *Violation*
  clause at line 202–203 ("quoted from the clause marker where it begins
  mid-line"), the `trust-and-evidence.md` evidence definition at lines
  341 ("stopping mid-line where the sentence ends"), and the VIS-4
  sentence at line 414 ("from \"One class\" where the sentence begins
  mid-line"). The fourth (`trust-and-evidence.md` 10–16, packet lines
  344–351) is a genuine disclosed truncation the summary sentence omits
  from its count — I confirmed it independently against source: the
  packet's quote ends at "…durably captured and identified, is evidence."
  while source line 16 continues "An LLM assertion is **Inferred, never
  Observed**,".
- *Line count.* `wc -l`, `grep -c ''`, and `awk 'END{print NR}'` all agree
  the file is 657 lines, not 658.

Neither error affects the substance of any quote, disclosure, or
invariant — every blockquote I compared matched its source exactly, and
the zero-counts in the same sentence (0 long lines, 0 broken code spans,
0 hex digests, 0 Butlers mentions) are all independently confirmed
correct. This is a self-audit arithmetic error inside a claim explicitly
labeled `[Observed]`, which is exactly the class of claim verification
rules 2 and 9 hold to a "confirmed by a second method" / "sweep with a
denominator" standard. Repair: correct "three" to "four" and "658" to
"657," or state the counting rule that yields three and 658 if one exists
that I did not find.

**N2 [note] — the "11 attributed inline quotations" figure is not
independently re-derivable from a stated rule.** I enumerated every
double-quoted inline fragment outside a blockquote and checked every one
plausibly attributed to a named source (P-79, the continuation act, the
secret-classification policy, SEC-4, SEC-5, AGENTS.md, VIS-5's *Violation*
clause, the registry entry) — every single one I checked matched its
source byte-for-byte, so this is **not** a content-accuracy finding.
Depending on whether a quote repeated verbatim at two locations (the
P-79 Q2 phrase at lines 83–84 and 118–119) counts once or twice, and
whether a single sentence quoting two fragments of one clause (the VIS-5
*Violation* clause's "committing a source-file edit…" and "a direct write
landing outside…" at lines 209–211) counts as one citation event or two,
my own count lands between 12 and 14, not 11. I could not find a stated
counting rule in the packet that resolves this. Given AGENTS.md's own
recorded lesson that "a word set published as 'X, Y or similar' is not a
predicate" and figures resting on an unstated rule cannot be re-derived,
I record this as a denominator-transparency gap rather than asserting the
"11" is wrong — it may be exactly right under a rule the drafter had in
mind and did not write down.

**N3 [note, informational] — no new defect from the repairs.** The
candidate banner (lines 4–11) is unchanged in substance from the version
the prior review read; no sentence performs, records, or adopts an act
outside the disclosed candidate direction-text fence (lines 498–567,
itself labeled "candidate text and binds nothing"); no backticked Butlers
path exists anywhere in the file (0 hits on `grep -ni butlers`); no
40- or 64-character hex digest appears; every `[Observed]`/`[Inferred]`/
`[Unknown]` label I checked is present where the packet's own epistemic
discipline requires one; the 78-column wrap holds with no broken code
span (both confirmed by independent script, not by trusting the packet's
count); and the `## Review` section's rule-10 sentence (lines 654–657)
correctly states that the retained raw review confirms `4ddb193` and not
these repaired bytes, and that a confirmation of the repaired bytes is a
separate review — which is this file.

## Summary of what held up

- All four prior findings (F1 revise, F2–F4 note) are repaired exactly as
  their disposition table says, at the location it names, quoted above.
- 12 of 12 attributed blockquotes match their cited source exactly
  (whitespace-normalized full-range matches or exact prefix/suffix
  substrings at a disclosed sentence-boundary truncation).
- Every attributed inline quote I checked (12–14 candidates by my own
  count) matched its source byte-for-byte with zero mismatches.
- `check_governance.py`: 32 OK, 20 WARN, 0 FAIL (52 checks), matching the
  packet's own claim exactly; the packet's own filename appears in no
  OK/WARN/FAIL line. `--selftest`: 255 fixtures, 0 failing.
- No Butlers path, no performed-act digest, no broken code span, no line
  over 78 columns outside a table row or fenced block, candidate banner
  intact, rule 10 correctly recorded.

## Rubber-stamp risk, named per CC-REV-6

The prior review's own rubber-stamp warning was about a small, unflagged
cut compounding into a cited precedent. This pass's finding is the same
failure mode one level up: the repair pass added a scripted-looking
`[Observed]` sweep sentence with six numeric claims, and two of the six
are off by one — caught only by independently re-running the same sweeps
rather than trusting the printed numbers. Nothing here changes the
decision put to the owner (the retention posture, the three retained
fields, the exclusions, the invariants are all intact and accurate), so I
am not withholding confirmation over it, but the next drafter who copies
this packet's "sweep behind the table" pattern into a future packet should
regenerate the denominators from a script rather than hand-count them —
exactly the discipline AGENTS.md's verification rules already require and
this sentence did not follow.
