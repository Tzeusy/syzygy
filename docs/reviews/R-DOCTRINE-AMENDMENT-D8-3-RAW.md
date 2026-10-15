# Review - D8 doctrine amendment packet (Inferred first-class, P-102) — round 3
Reviewed commit: b913d1ef37b8e6fc5dffe65b113285f00eb8ab8c
Package digest: 801ad3c05edb70f87784e8129ea2da6414518fe48a6f4c2cb5a096dfde35eaad
Verdict: REVISE

Reviewer: a fresh-context agent that drafted none of this package (CC-REV-1).
Round 3 under `REVIEW-BRIEF.md` §"Round 3". Date 2026-10-14.

## Method

- `git fetch origin main`, then `git checkout --detach b913d1ef…`.
  `git rev-parse HEAD` returned the reviewed commit, and the worktree was
  clean.
- **Package digest.** Computed by the brief's method in a Python script:
  `git ls-files` of the package directory, sorted by bytes, one
  `<sha256>  <path>` line per file, then sha256 of the concatenation. The
  population is 6 files: IMPACT-LEDGER.md, OWNER-DECISION-PACKET.md,
  REVIEW-BRIEF.md, ROUND-1-DISPOSITIONS.md, ROUND-2-DISPOSITIONS.md and
  SEMANTIC-DELTA.md. A plain `sha256sum` of IMPACT-LEDGER.md gave the same
  per-file hash the script gave (`6e3e6b6a…`).
- **What I read.** All six package files. The governing references the
  brief names, including:
  - `trust-and-evidence.md` (whole file);
  - `vision.md` VIS-5 to VIS-7 (lines 220–262);
  - `architecture.md` lines 1–40, 105–120 and 205–220;
  - RFC7-20 and RFC7-21 (`narrative-contract.md` lines 414–440);
  - generator `spec.md` lines 98 and 528;
  - the PWB coverage part, lines 35 and 74;
  - the RFC7-20 reading act;
  - the P-71, P-71-Q5, P-74, P-75 and P-76 rows of the rulings file
    (lines 58–64);
  - M4 funnel Q3 (line 115);
  - A6 line 25;
  - amendment `spec.md` line 508;
  - `DOCTRINE-AMENDMENT-LOG.md`;
  - REQ-polaris-generation-032 and its adoption record;
  - both earlier raws and both dispositions records;
  - register row P-102 (line 1179);
  - D7's packet anchors and its ledger line 201.
- **Sweeps.** Each was re-run by my own scripts at `09c7a61d`:
  - the term sweep: Python `re` over the ledger's predicate, population and
    lane order, then `git grep -l -z -i -E` as the second method, with the
    sets compared;
  - the static reader sweep at both `59fbf787` and `09c7a61d`, with the two
    reader lists diffed.
- **Partial application probe.** I made a scratch clone at the reviewed
  commit. A script extracted exactly seven `markdown` fences from the packet
  and checked all three doctrine digests. It then inserted each block at its
  stated anchor, with an assertion on each anchor line. I ran 8 of the
  battery's commands before and after the insertion. I did not run the full
  96-command battery. No repository file was edited.
- **Process note.** The brief names `docs/reviews/R-DOCTRINE-AMENDMENT-D8-3-RAW.md`
  as the output path. The dispatcher told me to write this raw to a session
  scratchpad file instead and to edit no repository file, so I followed the
  dispatcher. The head is the brief's four-line contract, unchanged.

## What holds [Observed unless marked]

- **Digests.** The three doctrine sha256 values in packet §1 and in the
  delta match the bytes at the reviewed commit. `git diff --stat 09c7a61d
  b913d1ef` touches no doctrine file. It touches only the D7 and D8
  packages and `PENDING-OWNER-DECISIONS.md`.
- **Anchors.** Every anchor is exact at the reviewed commit:
  - `trust-and-evidence.md` 44–49, 57–67 ((e)'s new anchor), 95–96,
    118–119, 134–137 and 144;
  - `vision.md` 232–234;
  - `architecture.md` 14, 18–27 ((d1)'s new anchor), 115–117 and 210–216
    (the Project bullet is at 212).

  Every insertion position the packet states, such as "after line 67, blank
  line before", lands where the prose says. My insertion script asserted
  each anchor line before inserting.
- **Quotations.** Each of these is exact:
  - RFC7-20 (line 416) and RFC7-21 (line 432);
  - generator `spec.md` lines 98 ("Generated diagrams SHALL remain
    editorial-draft until their applicable authorship act") and 528;
  - the PWB coverage part's RFC7-20 row (line 74) and RFC7-2 row (line 35);
  - the reading act's "The agent draft renders as an editorial draft"
    (line 46);
  - the funnel Q3 phrases: arm (a)'s "into Syzygy's own
    `.syzygy/governance/decisions/`", its cost sentence, and "a new effect
    no act in force names";
  - P-71 Q3 arm (b) at rulings line 58, which records no reason, as the
    packet now says;
  - P-76 Q2 ("an observing project reading its own tree");
  - A6 line 25;
  - REQ-019's consent sentence (line 508);
  - D9 at log line 12.

  The packet says doctrine cites no RFC number. The pattern `RFC ?[0-9]`
  matches 0 lines in each of the 6 doctrine files.
- **Term sweep at `09c7a61d`.** It reproduces exactly:
  - population 1,883 (1,889 with the package);
  - 151 hit files and 438 occurrences;
  - every lane row: doctrine 1/4, contract 0/0, decision 7/19, spec 14/24,
    candidate 26/39, other 9/18, evidence 58/248, raw 34/83, historical
    2/3.

  The `git grep` second method returns 151 files, set-equal to the first
  (0 files in either difference). P-98 sits at line 1175 and P-102 at line
  1179. Under the predicate, P-102's line carries 9 occurrences: one
  "correspondences" fails the trailing `\b`, so a plain `-o` count shows 10.
- **Static reader sweep.** It reproduces at both commits: 686 files and 39
  readers at `59fbf787`, and 962 files and 52 readers at `09c7a61d`. The
  diff of the two lists is exactly the 13 files the ledger names.
- **Partial application probe at `b913d1ef`.** All seven blocks were
  applied. The baseline is 8 of 8 commands exiting 0. Applied, 6 commands
  fail, with the messages the ledger tables:
  - CG-18: 16 findings over 10 fixtures × 2 predicates;
  - the budget report: DRIFT in fixtures 1, 3, 5, 6, 7, 8, 9 and 10 and in
    `CONTEXT-BUDGET-REPORT.md`;
  - `05-CONTRACT-INDEX.yaml` differs;
  - "DIRECTIVE-REGISTER.md is stale";
  - the recorder's `--check`: "review retired by changed input:
    .syzygy/governance/doctrine/vision.md";
  - the recorder's `--selftest`: "candidate input drift" on the same path.

  `build_task_router.py --check` and `check_quotations.py` stay green, and
  VIS-7 moves from line 250 to 257. This confirms those rows, not the whole
  96-command battery.
- **Composition (§8).** D7's packet at the reviewed commit anchors
  `vision.md` 105–107 (line 126) and `architecture.md` 329–334 (line 160).
  `git diff 7071a744 b913d1ef` touches no D7 or doctrine file, so D8's
  anchors do not overlap D7's. D7's ledger line 201 still says
  "unaffected: it reads history, not today's bytes", which my probe
  contradicts for D8's `vision.md` insertion, as ledger §5 item 4 says.
- **REQ-032.** It was adopted 2026-10-07 (`POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md`;
  the spec file's own "not yet adopted" banner is the known pre-act banner).
  Its "governed" test admits any subject whose inventory holds `openspec/**`.
  So an observed-only project such as Butlers is governed under REQ-032
  too, which agrees with §8 [Inferred].
- **Acceptance criterion 4.** No doctrine, contract, specification or code
  byte is edited by the package.

## Round-2 findings, checked in the bytes

Each was checked in the packet, delta, ledger and §7 table, not only in the
cycle-2 mapping.

1. **Repaired** (revise). Packet lines 407–414:
   - "release verdict" is gone;
   - the denial covers the line-60 triggers;
   - the permissive sentence names "any of the trust floor's four
     properties";
   - the clause now sits after line 67, outside the floor's section.

   The delta's (e) row and proposed meaning agree. See note 2 for a residue.
2. **Repaired** (revise):
   - RFC7-20 is named and quoted in §0's (a) row, in §1 (a), in §2's (a)
     row, in ledger §3.4 (new RFC7-20 and RFC7-21 rows) and in the delta;
   - the (a) bytes carry "unless the surface admits generated prose only as
     a draft";
   - Q1's reason names RFC7-20;
   - Q-C3 is added, and Q-S1 notes the `editorial-draft` consequence and
     PWB's line-74 exclusion.

   See note 3 for a residue.
3. **Repaired** (revise). Ledger §5 item 2 now quotes the current trigger.
   The superseded quotation sits inside a dated parenthesis, and "main risk"
   is withdrawn.
4. **Repaired**. Dated marks sit at each stale review-state sentence: the
   packet (lines 16–29), the delta (lines 8–12 and 194–204), the ledger
   head, both dispositions records and register row P-102.
5. **Repaired**. §2's (f) row says "before … after … presentation,
   non-citable (RFC7-4)". §1 (f) discloses the extension past "Narrative
   prose" and cites spec line 98.
6. **Repaired**. Packet lines 334–342 cite funnel Q3 for (d2)'s sense and
   say that P-76 Q2 uses the phrase for self-observation.
7. **Repaired**. Packet lines 368–381 state the declined arm (a), quote its
   cost, record that the owner gave no reason, and leave the trade-off with
   the owner.
8. **Repaired** in bytes:
   - (d1) is a paragraph after line 27;
   - it says "It is still governed";
   - `writeSurface` is replaced by "no act in force names a write into it".

   But the packet's new explanation of "the governed plane" exposes finding
   1 below.
9. **Repaired**. Q-C2's arms are rewritten, and Q-D1 is added with three
   arms and nothing drafted.
10. **Repaired**. "The rule adds no property to the trust floor." §1 (e)
    answers "Release-blocking? No, as drafted", and Q5 gains the
    fifth-bullet arm, disclosing its VIS-7 and Q-A1 cost.
11. **Repaired**. The Q3 cell rests on lines 118–119, and the delta's (a)
    row states the stale and withdrawn rule.
12. **Repaired**. The figures are re-pinned to `09c7a61d` and reproduce
    (above). D9 and the D7 anchors are added to §8, and the digest census
    is marked at the sentence. See note 4 for one inaccuracy in the new
    reader prose.

## Findings

### 1. Revise-level [Inferred]: under the packet's own reading of "the governed plane", a (d2) dismissal either cannot take effect or violates VIS-6, and the packet does not say which

Doctrine ties a dismissal's effect to where it lives:

- `trust-and-evidence.md` lines 42–43 say a recorded human decision "takes
  effect only once committed out to the governed plane".
- VIS-6(a) says promoting a note "(as an annotation or a dismissal)
  commits it to the governed plane".
- VIS-6's violation sentence names "a dismissal taking effect without
  living in the governed plane".

The repaired packet now fixes what that phrase means for an observed-only
project. Lines 300–304 say an observed-only project is governed, "so 'the
governed plane' in VIS-6 and in (b) still means the project's own plane,
which Syzygy may not write, and (d2) adds a second destination beside it".

Clause (d2) names "a dismissal" as content committed out to the *observing*
project's `.syzygy/**`. Read with lines 300–304, that dismissal does not
live in the governed plane of the project whose gap it dismisses. So one of
two things holds:

- it never takes effect, and the gap keeps rendering, in which case listing
  dismissals among (d2)'s examples promises a destination for something
  inert;
- or it takes effect, and that is the VIS-6 violation the sentence names,
  unless (d2) is read as redefining "the governed plane", which lines
  300–304 deny.

(d2)'s own limits say the record "never anchors the project's capability
map", is not the project's declaration and is not cited as its text. None of
them says whether it suppresses a gap.

This decides something concrete for the owner. P-71 Q3 is about drafted acts
over the observed project's *gaps*, and (d) is recommended for adoption on a
trade-off framed around that case. The same question touches (b): its bytes
say an answer is "committed out to the governed plane", which the packet
reads as the observed project's own plane. Adoption therefore relies on
(d2), a sub-bullet, to supply the other destination. That works for an
answer, which has no "takes effect" condition, but not cleanly for a
dismissal.

No earlier round raised this. A sweep of the round-1 raw, the round-1
dispositions and the packet for "violation" and "take(s|ing) effect"
returns 0 lines. It is sharpened, not created, by the note-8 repair.

Repair, one of:

- say in (d2), or in §1 (d) with an owner arm, whether such a dismissal
  takes effect, and if it does, reconcile it with VIS-6's violation
  sentence and lines 42–43;
- drop "a dismissal" from (d2)'s examples, and say that dismissals of an
  observed-only project's gaps keep only P-71-Q5's route;
- ask the owner (a Q-D2 beside Q-D1).

### 2. Note [Inferred]: repaired (e) keeps residues of its trust-floor placement

- The denial's citation, "(vision.md VIS-7)", attaches the
  alignment/convergence/genome-completeness denial to the rule whose body is
  the release-blocking trust floor. The same paragraph now says it "adds no
  property to the trust floor". VIS-7's title ("The observatory itself must
  be trustworthy") supports the citation in spirit. A reader could still
  take it as floor matter, which is the reading the repair set out to
  remove. Citing the line-60 trigger's own section, or no rule, would be
  cleaner.
- The final sentence, "a claim resting only on such records has no
  evidence, and renders Unknown", does not say which claim it means. Read
  alone, it denies all claims, including the floor-property claims that the
  sentence before it allows. Context resolves this toward the denied kind.
  In doctrine bytes, "such a claim" or "a claim of that kind" would remove
  the ambiguity.
- The heading "never self-certifies" is wider than the rule. The denial
  covers only the line-60 trigger. The other triggers, a green badge or a
  gap "factually resolved or absent" about Syzygy itself, may still rest on
  self-observation records. That may be intended. If so, §1 (e) should say
  so, since a green badge about Syzygy resting on its own records is what a
  reader would call self-certification.

### 3. Note [Inferred]: (a)'s "never a claim" is unscoped in time, while Q-C3's rationale relies on RFC7-21's adoption path

The bytes say that on a draft-only surface a synthesis "is that draft and
never a claim". RFC7-21 lets a human adoption act make a draft "curated
narrative". RFC7-2 is then enforced claim by claim, and RFC7-2(c) admits
Inferred claims there. Q-C3's recommended "no" rests on "no gap RFC7-21's
human adoption path leaves". That reasoning needs the adopted text to be
able to carry Inferred claims, but "never a claim" read literally forbids
it. Context suggests "while it is that draft" is meant, and one would read
that way. Separately, the clause's freshness obligations ("no fresher than
its stalest input") are stated for an object that, on Polaris, is not a
claim. That is harmless but could be said.

### 4. Note [Observed]: ledger §4's account of the 13 new readers is inaccurate in one place

The ledger says every doctrine file the 13 name is `security.md` or
`v1.md`, apart from one made-up fixture name and one directory. But
`packages/polaris-dossier/src/gate-acts.test.ts` line 298 names
`.syzygy/governance/doctrine/README.md` and reads its real bytes into a
fixture (`write(root, readme, real(readme))`), hashing them live. Packet §9
step 3 edits that README's glossary. So this test is a reader of a file D8's
recipe changes, and the ledger's sentence "none of them is a D8 reader" is
not right as stated. Because the test hashes live, it should stay green
[Inferred: not run]. The application probe inserts only the seven blocks,
not the step-3 glossary edit, so the glossary edit's battery effect is
unprobed. Say so beside the probe.

### 5. Note [Observed]: register row P-102 (outside the subject) still states Q1's pre-repair rationale

Line 1179 says Q1 (a) "synthesis renders Inferred … recommended
**decline**, since `trust-and-evidence.md` and accepted
RFC7-2/RFC1-16/RFC4-26 already permit both". After the finding-2 repair,
the packet's Q1 reason is that RFC7-20 already decides the rendering on
Polaris, as an `editorial-draft`, not an Inferred claim. The row's later
mark adds Q-C3 but does not mark the Q1 sentence. Under the CG-27 lesson,
mark it at the sentence. The register is not a package file, so this does
not count against the package digest.

## Summary

- Revise-level findings: 1 (finding 1).
- Notes: 4 (findings 2–5).
- All twelve round-2 findings are repaired in the bytes. Their figures
  reproduce: the term sweep is 1,883 / 151 / 438 and set-equal; the static
  sweep is 962 / 52 at `09c7a61d` and 686 / 39 at `59fbf787`; the partial
  probe reproduces the 6 failing rows. Every anchor, digest and quotation I
  checked is exact.
- Finding 1 is a doctrinal coherence gap in (d2) that the note-8 repair's
  explanation makes explicit. A dismissal placed in the observing project's
  tree either never takes effect or violates VIS-6's violation sentence, and
  the packet, which recommends adopting (d), does not say which.
- Under the brief's Round 3 stopping rule this verdict goes to the owner
  with its findings, and the package is not repaired again.
