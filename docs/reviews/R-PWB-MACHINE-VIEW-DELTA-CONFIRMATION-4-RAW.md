# Review — PWB machine-view amendment (round 5, fourth confirmation)
Reviewed commit: cd1fbd392bb6d3df1f8ad22e625b8e5203223c3d
Manifest SHA-256: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
Verdict: CONFIRM WITH EXCEPTIONS

## Commission

Fresh-context session, no authoring context, run per CC-REV-1 (full review),
CC-REV-4 (fresh context) and CC-REV-6 (raw retained verbatim). Working tree:
`/home/tze/GitHub/syzygy/.worktrees/mv-round5` at the commit above. No
tracked file edited, nothing committed, pushed or merged; no other agent
consulted; commit message bodies not read for intent (subject lines only);
`.syzygy/local/` not opened. Required reading completed: `AGENTS.md`
(verification rules 1–10), the package's `REVIEW-BRIEF.md`,
`SEMANTIC-DELTA.md` (all rounds' §Review dispositions), the manifest,
`OWNER-DECISION-PACKET.md`, `IMPACT-LEDGER.md`, `proposed/*.patch`, the
owner's recorded values in
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
§2 and §6, and the four prior raws (`R-PWB-MACHINE-VIEW-DELTA-RAW.md`,
`-CONFIRMATION-RAW.md`, `-CONFIRMATION-2-RAW.md`, `-CONFIRMATION-3-RAW.md`).

## Task 1 — round 4's two findings, repair confirmed

Round 4 (raw `docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-3-RAW.md`,
reviewed commit `194f8cd1e90877842786d7adae9df10893ed2495`, confirmed a real
ancestor of `cd1fbd3` via `git merge-base --is-ancestor 194f8cd1 HEAD`
although absent from a plain `git log --oneline`) found two non-blocking
findings, numbered 1 and 2 in its own "Findings summary" and dispositioned as
R4-1 and R4-2 in the current `SEMANTIC-DELTA.md` §Review "Round 4" section
(lines 717–760).

**R4-1 (F8 disposition named a nonexistent heading).** Raw finding 1 quoted
the superseded text as: `which is what "How this would be adopted" step 6
already said` and required the citation be renamed to `"Migration /
supersession plan" step 6`. `git diff 194f8cd1 cd1fbd39 --
.syzygy/governance/contracts/candidates/pwb-machine-view-amendment/` shows
the removed line is byte-identical (after Unicode NFC + whitespace
normalization) to the raw's quoted superseded text, and the added text at
`SEMANTIC-DELTA.md:748-749` reads "which is what \"How this would be
adopted\" step 6 already said"; the step sits under "Migration /
supersession plan"" (present tense — the R4-1 disposition itself, not the
repaired sentence, retains the historical quote as its own evidence, which
is correct: it is quoting the superseded wording on purpose). The heading
`## Migration / supersession plan` exists at `SEMANTIC-DELTA.md:510`;
confirmed by `grep -n '^## Migration'`. No heading named "How this would be
adopted" exists anywhere in the package (`grep -rn '"How this would be
adopted"' .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/`
returns only the two dispositioned quotes, never a live citation). **Repair
confirmed genuine; no new false claim introduced.**

**R4-2 (packet's arm (a) restated a stale round count).** Raw finding 2
required the "Two rounds have run…" sentence be replaced so it cannot go
stale at the next round. `OWNER-DECISION-PACKET.md:151-153` (arm (a)) now
reads "(For the rounds run so far see the status line at the head of this
packet; the patches and…" — it points at the status line instead of
restating a count. The status line itself
(`OWNER-DECISION-PACKET.md:8-16`) reads "**Status as of 2026-09-23:**
reviewed four times" and enumerates all four raws by filename. This
structurally cannot re-drift the way the round-3 and round-4 defects did
(rule 10's failure mode: a count transcribed in two places, only one
updated). **Repair confirmed genuine; no new false claim introduced.**

Both repairs are truthful at this commit. Consistent with rounds 3 and 4's
own pattern, the repair pass left adjacent, unrelated prose stale — see
Findings 2 and 3 below, neither raised by any of the four prior rounds
(confirmed: `grep -n "three so far\|four so far" docs/reviews/R-PWB-MACHINE-VIEW-DELTA*RAW.md`
returns nothing, and `grep -n "occurs in \*\*7\*\*\|12 tracked files\|4 tracked files"` against
the four raws returns nothing for the IMPACT-LEDGER.md figures either).

## Task 2 — cross-reference sweep (exhaustive, with denominator)

Method: every backtick-quoted path, `§`/heading reference, "step N", "round
N", and bare numeric-count claim ("N tracked files", "N files", "N so far")
in the package's four prose files (`SEMANTIC-DELTA.md` 760 lines,
`OWNER-DECISION-PACKET.md` 244 lines, `IMPACT-LEDGER.md` 290 lines,
`REVIEW-BRIEF.md`) was extracted and checked against the current tree by
script (`grep -n`, `git grep -lF`, heading `grep -n '^#'`), continuing and
extending the same sweep rounds 1–4 already ran (their prior findings are
not re-litigated except where repair is confirmed above). Denominator: all
four prose files in the package, all headings, all cross-file quotes, all
bare numeric-population claims not already covered by the blast-radius and
sibling-count re-derivations in Task 5 below (those are re-verified
separately, not skipped).

**Finding 1 (non-blocking) — `SEMANTIC-DELTA.md:512` self-contradicts its
own step 4 and `OWNER-DECISION-PACKET.md`'s "Two acts" framing.** The
"Migration / supersession plan" intro sentence reads: "In order. Steps 1–3
are drafting and review; only step 5 is an owner act." But step 4
(`SEMANTIC-DELTA.md:526-531`) reads: "**The registry act** (P-72 question 2,
gate bead `syzygy-dov.18`)… It is a separate owner act over a separate
subject and may be performed before or after this one." `git grep -n
"owner act" .../SEMANTIC-DELTA.md` confirms both sentences exist verbatim.
`OWNER-DECISION-PACKET.md:190-205` ("## Two acts, and why their order is
free") independently and consistently calls both the registry act and the
behavior amendment act acts, numbered 1 and 2, and states "Either may be
performed first" — directly incompatible with "only step 5 is an owner
act". Required repair: strike "only" and name both acts, e.g. "steps 4 and
5 are owner acts, over different subjects, in either order" — matching
`OWNER-DECISION-PACKET.md`'s own framing and step 4's own sentence.

**Finding 2 (non-blocking) — `IMPACT-LEDGER.md:88,89,93` citer counts are
stale.** Re-derived this session by `git grep -lF <literal> HEAD | wc -l`
against the whole tracked tree (not the historically-scoped IMPACT-LEDGER.md
sweep commit):
- `/api/poc/briefing`: claimed "occurs in 12 tracked files" at
  `IMPACT-LEDGER.md:88`; actual current count is **25**.
- `/polaris/draft`: claimed "occurs in 4 tracked files" at
  `IMPACT-LEDGER.md:89`; actual current count is **15**.
- `maxBriefingResponseBytes`: claimed "occurs in **7** tracked files" at
  `IMPACT-LEDGER.md:93`; actual current count is **24** total, of which 3
  are this package's own self-citations (`IMPACT-LEDGER.md`,
  `OWNER-DECISION-PACKET.md`, `SEMANTIC-DELTA.md`), leaving **21** external
  citers.

Unlike the structurally identical table in `SEMANTIC-DELTA.md:63-71`, which
is explicitly headed "What is true today, **2026-09-21**" (a dated,
historical snapshot, correctly scoped — not a defect), the
`IMPACT-LEDGER.md` occurrences at lines 88, 89 and 93 carry no such dating
and are written in the present tense as live facts supporting a live
conclusion ("No registry file names it. The inserted specification text
therefore does not name it either."). The growth is real and identifiable:
`git grep -lF maxBriefingResponseBytes HEAD` now includes the sibling
package `pwb-registry-currency-briefing-amendment/` (created after this
package's 2026-09-21 draft — its own three prose files plus a patch),
`docs/pursuits/2026-09-22-vision-pursuit-data.json`,
`docs/pursuits/2026-09-22-vision-pursuit-harvest.json`, three retained raws
for that sibling
(`docs/reviews/R-PWB-REGISTRY-CURRENCY-BRIEFING-DELTA{,-CONFIRMATION,-CONFIRMATION-3}-RAW.md`),
`scripts/build_pwb_registry_currency_briefing_amendment.py`, and
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
— none of which existed when this package's IMPACT-LEDGER.md was drafted.
**The substantive conclusion remains true** (re-verified this session: no
file under `.syzygy/governance/declarations/**/*.json` names
`maxBriefingResponseBytes` — confirmed by
`git grep -lF maxBriefingResponseBytes -- '.syzygy/governance/declarations/'`
returning nothing), and none of the three stale counts are manifest rows
(`PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` lists only the 11
`openspec/changes/polaris-project-wide-butlers-model/` subjects —
`IMPACT-LEDGER.md` is not one of them), so no digest is affected. Required
repair: either re-run the sweep and update all three counts, or reword as
dated snapshots the way `SEMANTIC-DELTA.md`'s table already is (the cheaper,
more durable fix, since these counts will keep drifting as sibling packages
and pursuit docs are added).

**Finding 3 (non-blocking) — `SEMANTIC-DELTA.md:576-577` round-count/date
sentence is stale and contradicts the package's own status line.** "##
Review" reads: "**Reviewer:** a fresh-context session with no authoring
context, per round (three so far: 2026-09-21, and two on 2026-09-23)." Two
defects, both re-derived this session:
1. **Count.** Four rounds have run, not three: the package's own §Review
   log documents "Round 2", "Round 3" and "Round 4" as headed subsections
   (`grep -n '^### Round' SEMANTIC-DELTA.md` → lines 617, 658, 717) on top
   of round 1, and `OWNER-DECISION-PACKET.md:8` independently states
   "reviewed four times", naming all four raws. "Three so far" undercounts
   by one and was never updated after round 4 landed (confirmed absent from
   all four raws' own text, per Task 1's grep above).
2. **Date split.** `git log --format='%ad' --date=short -- <path>` on each
   of the four raws (taking the first/introducing commit per file) gives:
   round 1 raw `R-PWB-MACHINE-VIEW-DELTA-RAW.md` → **2026-09-22**, not
   2026-09-21 as the sentence claims (2026-09-21 is the draft's own "Date"
   line, not a review date); rounds 2, 3 and 4 → **2026-09-23** each (three
   on that date, not two). So even reading "three so far" charitably as
   "three total", the 2026-09-21/2026-09-23 split is also wrong on both
   sides.

Required repair: update to something that cannot re-drift, e.g. point at the
status line the same way R4-2's repair did for
`OWNER-DECISION-PACKET.md`'s arm (a) — "see the status line at the head of
`OWNER-DECISION-PACKET.md` for the rounds run so far" — rather than carrying
a second, independently-maintained count and date pair.

No other cross-reference defects found. Headings cited elsewhere in the
package (`## Migration / supersession plan`, `## Two acts, and why their
order is free`, `## The ceiling this delta depends on but does not mint`,
`## Ordering against the sibling candidates`) all exist and are cited
correctly; step numbers within the Migration plan (1–7) are cited
consistently at every callsite checked; file paths quoted in all four prose
files (`proposed/*.patch` names, the eleven manifest rows, the four sibling
package directories, `GOVERNING-DEPENDENCIES.md`,
`polaris-presentation-route.test.ts`, `routes.ts`,
`project-shape-observation.ts`) all resolve via `git cat-file -e HEAD:<path>`.

## Task 3 — machine checks (output read, not exit code)

```
$ python3 scripts/build_pwb_machine_view_amendment.py --check
PWB machine-view amendment manifest matches 11 proposed behavior subjects (2
patched, 9 unchanged); the dependency declaration is regenerated from the
proposed spec and the spec patch composes with the sibling candidate in
either order
exit=0

$ python3 scripts/build_pwb_machine_view_amendment.py --selftest
selftest: closed population, byte drift, path order, subject drift,
context-line and added-line patch corruption, transcribed and unwarranted
dependency declarations, sibling drift and a missing sibling patch fail
closed
exit=0

$ python3 scripts/check_governance.py
...
32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted
```

0 FAIL confirmed by reading the summary line, not the process exit code.
`CG-7d` (60 quotations examined, 0 findings) shows this package's subject
"SIGN OFF PWB MACHINE-VIEW AMENDMENT" with 1 quotation, 0 findings, 0
performed digests. `CG-7e` (37 files examined, 0 findings) shows
`OWNER-DECISION-PACKET.md` registered with "1 current and 0 performed-history
act(s); 1 current, 0 historical valid". All WARNs are pre-existing,
unrelated advisory/report-only checks (CG-22b, CG-23, CG-24, CG-27) over
files outside this package.

## Task 4 — digests, scripted

```
$ sha256sum .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt
2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c  ...MANIFEST.txt
```

Matches the phrase quoted at `OWNER-DECISION-PACKET.md:178` ("SIGN OFF PWB
MACHINE-VIEW AMENDMENT: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c")
and `scripts/check_governance.py:1544-1545`'s `PWB_MACHINE_VIEW_SUBJECT`,
which resolves to this same file's path (the act's subject and the manifest
file's own digest are, for this package, the same value — confirmed
unusual but correct per the package's own design, matching what rounds 2–4
already established). This is the value on the four-line head above.

## Task 5 — judgment against `REVIEW-BRIEF.md`'s 12 criteria and the
CC-SPEC bar

1. **Change class.** Normative, three grounds stated, ground 3 marked
   weakest by the drafter's own hand — disclosed, not concealed. Holds.
2. **Closure.** Both categories closed by enumeration; `spec.md.patch`
   re-checked this session (`grep -c '^-'` = 1, the diff header only — zero
   real deletions). Holds.
3. **Two genuinely-two categories.** Draft view's exclusion list and the
   two named members remain disjoint on inspection; unchanged since round 4.
4. **Parity not weakened.** Zero-deletion patch confirms Case/Observable/
   Oracle text is untouched; the amendment is pure insertion. Holds.
5. **`RFC6-21`.** Both quoted sources verified byte-exact against
   `contracts/rfcs/RFC-0006-...md:382-386` and
   `contract-coverage-matrix/RFC-0004-0006.md:234` this session. The tension
   is disclosed, not silently resolved; the owner's narrow reading is
   recorded as her ruling, not manufactured consensus. Holds.
6. **Ceiling precondition.** The inserted text leaves the field identity to
   the registry act and states the precondition correctly; Finding 2 above
   is a citation-count staleness in the *supporting* ledger prose, not in
   the inserted specification text itself, which names no count. Holds,
   with Finding 2 noted.
7. **Unchanged boundaries.** Eleven enumerated items; spot-checked, none
   contradicted by the proposed patches.
8. **Blast radius.** 121-over-1,334 re-derived this session (prior segment
   of this same review): section counts in `IMPACT-LEDGER.md`'s "Every
   citing file" enumeration sum to 121 (9+1+4+8+12+48+26+12+1), and all 121
   listed paths exist at HEAD. This is a distinct, correctly-scoped count
   from the stale ones in Finding 2 (those measure two unbuilt route
   literals and an undeclared field name across the whole tree; this one
   measures PWB-REQ-020 citers specifically) — not affected by Finding 2.
9. **Package mechanics.** `--check`/`--selftest` green this session; manifest
   hashes proposed bytes only, confirmed by scratch `git apply` in a prior
   segment of this session.
10. **Sibling ordering.** "Five candidates carry a `proposed/spec.md.patch`"
    re-checked at current HEAD (not only at the historically-cited
    `76b4beb`) via `find … -name spec.md.patch` filtered to siblings against
    `spec.md`: still exactly 5. Holds, unaffected by the new sibling
    (`pwb-registry-currency-briefing-amendment` patches a different subject,
    the registry JSON, not `spec.md`).
11. **Comprehension.** A fresh reader can restate the two categories and the
    ceiling precondition from the delta text alone; Findings 1 and 3 are
    self-contradictions a careful reader would trip on, which argues for
    repair but does not by itself defeat comprehension of the substantive
    change.
12. **Owner packet.** One decision, three arms, sign-off phrase withheld
    pending a confirming round and matching the manifest digest exactly
    (Task 4). The owner's recorded §2 and §6 values (category name, route
    shape, RFC6-21 = Narrow, landing order ".21 → .30 → .22 → lane B") are
    all correctly reflected in the packet, cross-checked this session.

No criterion is defeated. All three findings this round are non-blocking:
none touches a manifest byte (Finding 1 and 3 are in `SEMANTIC-DELTA.md`
prose outside the 11 manifest rows; Finding 2 is in `IMPACT-LEDGER.md`,
also not a manifest row), none reverses a substantive conclusion (Finding
2's underlying "no registry file names it" claim re-verified true this
session), and none is a repeat of any prior round's finding (checked against
all four raws by grep, per Task 1).

## Findings summary

1. **(non-blocking)** `SEMANTIC-DELTA.md:512` — "only step 5 is an owner
   act" contradicts step 4 (`SEMANTIC-DELTA.md:526-531`, "a separate owner
   act") and `OWNER-DECISION-PACKET.md:190-205` ("Two acts"). Repair: strike
   "only"; name both acts.
2. **(non-blocking)** `IMPACT-LEDGER.md:88,89,93` — three citer counts are
   stale versus this session's re-derivation (`/api/poc/briefing` 12→25,
   `/polaris/draft` 4→15, `maxBriefingResponseBytes` 7→24 total/21
   external), driven by the newer sibling package
   `pwb-registry-currency-briefing-amendment/` and new pursuit docs not
   present when this ledger was drafted. Substantive conclusion ("No
   registry file names it") remains true. Repair: re-run the sweep and
   update the three counts, or date them as a historical snapshot the way
   `SEMANTIC-DELTA.md:63-71`'s table already is.
3. **(non-blocking)** `SEMANTIC-DELTA.md:576-577` — "three so far:
   2026-09-21, and two on 2026-09-23" undercounts (four rounds have run,
   confirmed by the package's own §Review log and by
   `OWNER-DECISION-PACKET.md:8`'s "reviewed four times") and misdates (round
   1's raw was committed 2026-09-22, not 2026-09-21; rounds 2–4 were all
   committed 2026-09-23, three, not two). Repair: point at the status line
   the way R4-2's repair already did for the packet's arm (a), rather than
   carrying a second, independently-drifting count.

None of the three findings are repeats of any of round 1–4's findings
(checked by grep against all four retained raws). R4-1 and R4-2 are
confirmed genuinely repaired with no new false claim from the repair pass
itself. The package remains materially sound: closed categories, zero-
deletion patch, disclosed RFC6-21 tension, correctly-scoped blast radius and
sibling-ordering claims, matching digests throughout. `CONFIRM WITH
EXCEPTIONS`, consistent with all four prior rounds' verdicts.

## Method and commands

```
git rev-parse HEAD
git merge-base --is-ancestor 194f8cd1e90877842786d7adae9df10893ed2495 HEAD
git diff 194f8cd1e90877842786d7adae9df10893ed2495 cd1fbd392bb6d3df1f8ad22e625b8e5203223c3d -- \
  .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/
grep -n '^## Migration' .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/SEMANTIC-DELTA.md
grep -rn '"How this would be adopted"' .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/
grep -n "maxBriefingResponseBytes" .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/*.md
git grep -lF "/api/poc/briefing" HEAD | wc -l
git grep -lF "/polaris/draft" HEAD | wc -l
git grep -lF "maxBriefingResponseBytes" HEAD | wc -l
git grep -lF "maxBriefingResponseBytes" HEAD
git grep -lF "maxBriefingResponseBytes" -- '.syzygy/governance/declarations/'
grep -n "^### Round" .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/SEMANTIC-DELTA.md
grep -n "three so far\|four so far" docs/reviews/R-PWB-MACHINE-VIEW-DELTA*RAW.md \
  .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/SEMANTIC-DELTA.md
git log --format='%ad %s' --date=short -- docs/reviews/R-PWB-MACHINE-VIEW-DELTA-RAW.md | tail -1
git log --format='%ad %s' --date=short -- docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-RAW.md | tail -1
git log --format='%ad %s' --date=short -- docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-2-RAW.md | tail -1
git log --format='%ad %s' --date=short -- docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-3-RAW.md | tail -1
python3 scripts/build_pwb_machine_view_amendment.py --check
python3 scripts/build_pwb_machine_view_amendment.py --selftest
python3 scripts/check_governance.py
sha256sum .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt
grep -n "SIGN OFF PWB MACHINE-VIEW AMENDMENT" .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/OWNER-DECISION-PACKET.md
grep -n "PWB_MACHINE_VIEW_SUBJECT" scripts/check_governance.py
grep -c '^-' .syzygy/governance/contracts/candidates/pwb-machine-view-amendment/proposed/spec.md.patch
```

Plus, carried over from the earlier segment of this same review session
(prior to a context-management interruption, not a new session): the
121-over-1,334 blast-radius re-derivation by two independent methods
(Python regex over `git show` per-file text, and `grep -rlF` over a `git
archive` extraction into scratch), the 5-sibling `proposed/spec.md.patch`
re-count at current HEAD, the `GOVERNING-DEPENDENCIES.md` before/after
patch inspection ("17 requirement(s), 96 distinct authorities" untouched,
only the sha256 hex changes), and the byte-exact confirmation of both
RFC6-21 quotations against `contracts/rfcs/RFC-0006-...md` and
`contract-coverage-matrix/RFC-0004-0006.md`.
