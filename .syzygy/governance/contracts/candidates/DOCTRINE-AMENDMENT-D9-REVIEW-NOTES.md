# Doctrine amendment D9 — round-3 review notes

> **Candidate — binds nothing.** This is the sibling record for the notes of
> D9's third fresh-context review. Under the owner's notes-only rule
> (`../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a round
> with no revise-level finding clears the exact bytes it read, and its notes
> go in a sibling record, never into the reviewed bytes. So this file sits
> outside the package directory and edits nothing in it. It adopts nothing:
> only the owner's own words adopt doctrine (VIS-4). D9 binds no act digest,
> so nothing here is registered in `check_governance.py`.

## How to adopt

To adopt, say it plainly in your own session, naming the arm and the Q3
choice. For example: **"Adopt D9, arm A, with the v1 sentence, Q3 (b)"**.
Doctrine amendments carry no phrase and no digest (D1, D5 and D6 set that
precedent). If you say only **"Adopt D9"**, this record recommends reading
it as the packet's recommendations:

- Q1: arm A, with the `v1.md` sentence;
- Q3: (b) for RFC5-24 (the credential condition is kept) and (a) for RFC5-12
  (its effect change is recorded), with (c), an RFC 0005 amendment, queued
  and not blocking;
- Q4: A, a conforming CC-SEC-3 amendment after D9;
- Q5: A, the definitions stay in place.

The adoption commit writes that reading out in the log row, so a different
intention can be corrected before anything else relies on it. That one
commit will:

1. re-check `security.md` (sha256
   `c2be53d1e25c18f9329e9e18caea2256773f584e7fd45077b9caa6323aaf4892`) and
   `v1.md` (sha256
   `99d3164f2150a0faeebe0221fe0a977cb6c9c07e8d456f328f42717b247e1505`); if
   either has moved, stop and send the change back for review;
2. replace `security.md` lines 61–70 and `v1.md` lines 119–120 with the
   confirmed bytes of the chosen arm, deleting the credential lines only if
   you declined Q3 (b);
3. regenerate the seven derived files (four context fixtures, the budget
   report, the contract index and the directive register) and run the
   canonical battery;
4. add a `D9` row to `../../decisions/DOCTRINE-AMENDMENT-LOG.md` quoting
   your words and the Q1, Q3, Q4 and Q5 answers, and close register row
   P-103 with the outcome.

It does not sign the dossier specification (PR #353), which is your separate
sign-off. N1, N2 and N6 below are yours to rule on, at adoption or later.

## What was confirmed

- **Package:** the six files of
  .syzygy/governance/contracts/candidates/doctrine-amendment-sec3-attended-agent-session-d9/
  on draft PR #357. That directory is not on `main` yet, which is why it is
  not written as a code span here.
- **Reviewed commit:** `62c29093935c9370efe030d1a3a54672f50dbd72`.
- **Package digest:**
  `7168a3e2f062b6c9d96ac0d9cb6bcee69900d49785261e44b02a0f950fbfe413`,
  computed as `sha256sum` over the package's tracked files in C-locale
  order, then `sha256sum` of that listing.
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, at
  docs/reviews/R-DOCTRINE-AMENDMENT-D9-3-RAW.md:4. The lead retains that raw.
  The verdict carries no revise-level finding ("## Revise-level findings"
  reads "None.") and seven notes.
- Rounds 1 and 2 returned `REVISE`. Their dispositions are in the package's
  ROUND-1-DISPOSITIONS.md and ROUND-2-DISPOSITIONS.md.

Every claim below re-checked against the package at `62c29093` is marked
[Observed]. Each recommendation is the drafter's [Inferred].

## The notes

| # | Who decides | What the note says, in plain terms | Recommendation |
|---|---|---|---|
| N1 | **Owner** | A choice is recorded "for that one run", but D9 does not say what a run is. A feature that called a long-lived job one run could get close to the standing approval you ruled out. "Naming what the instruction covers" limits this only partly. The dossier specification (PR #353) closes it for the dossier: there a run is one authoring session at one pinned revision. The packet leaves to the specification who records the choice, but does not say that what counts as a run is left there too | Leave the definition of a run to each feature's specification, as the dossier does, and say so in your adoption words. Each feature must then define a run as bounded: one session, a named scope, and an end. A doctrine definition would be a new text and a new review |
| N2 | **Owner** | Condition 4 holds "for as long as any of them runs". Syzygy cannot see which processes a session started or when the last one ends, and observed code can set itself up to restart (a cron entry, a user service). So once any permitted run has happened, the only way to be sure the condition holds is to keep adapter credentials unreadable by your user account from then on. The packet's cost, "a separate OS user or a protected store", already implies that, but it does not say "from the first such run on" | Accept it as a standing cost. It costs nothing today, because Syzygy holds no adapter credential [Inferred, from the package's code search]. Once Syzygy holds one, it is kept from your user account permanently. Code your own command later runs, from a file the session changed, is outside condition 4 and outside SEC-3's scope under arm A; it would reach a credential your user can read with or without D9 |
| N3 | Drafter | The violation sentences name "a standing record" but not "a per-project record". The permitted case already excludes both ("A standing or per-project record does not qualify"), so an instruction on a per-project record is still forbidden. The two lists simply differ | No action. The prohibition is already complete. Changing it now would edit confirmed bytes and need another review |
| N4 | Drafter | ROUND-2-DISPOSITIONS.md said "nothing more" and "matches the ruling" had "0 occurrences in the package". Read literally, that is false. [Observed at `62c29093`, case-insensitive over whitespace-normalized text: "nothing more" occurs 5 times in 3 files (packet 1, brief 2, dispositions 2), and "matches the ruling" occurs 2 times, both in the dispositions.] None of them claims arm A is minimal: they quote the retired claim or state the criterion | Corrected here, not in the reviewed bytes. The sentence should have read: "0 occurrences that assert arm A is minimal". The lesson is rule 9's: an absence claim needs its predicate stated |
| N5 | **lane-spec** | Arm A counts a shipped skill as an instruction, and condition 1 requires the choice for a run to be recorded before the instruction is given. A skill ships before any run exists, so it can never carry the permission itself. It can only defer to a per-run instruction, such as the brief. PR #353's design already does this ("Follow the execution rule in `brief.md`") | Routed to lane-spec. The dossier specification should state that the skill defers to the per-run brief and never grants execution itself. Any future feature that ships a skill should follow the same pattern |
| N6 | **Owner** | "Naming what the instruction covers" limits Syzygy's instruction, not the session. Under arm A, a session that runs more than the named scope does not violate SEC-3, because SEC-3 governs what Syzygy does about the session, not what the session does. Syzygy's own duties still apply: every claim resting on the run is Inferred, and every reported command is disclosed. A reader could take the named scope as a limit on the session | Accept it, in keeping with your choice of disclosure over containment. Ask the dossier specification to have the run record compare the commands the session reports against the named scope and flag any outside it, so overreach is visible rather than forbidden |
| N7 | Drafter | Editorial. [Observed at `62c29093`:] (1) SEMANTIC-DELTA.md line 43 is 128 columns, an unwrapped prose line in the arm A heading bullet, outside the fenced blocks. (2) In the source of IMPACT-LEDGER.md §5 the list is numbered 1, 2, 3, 6, 7, 4, 5. CommonMark numbers it from its first item, so the rendered page shows "Who records the owner's choice" and "Attendance is not observable" as items 4 and 5, while ROUND-2-DISPOSITIONS.md cites them as items 6 and 7. (3) The P-103 register note gives its count's base as `5863d470`, while the branch sits on `5126610b`; the count (31 open, 5 acceptance-act, 36 in all) is the same at both | No repair in the reviewed bytes. When citing §5, name the item by title rather than number. None of these touches the bytes the adoption applies, which are the fenced blocks |

## Routing

- N1, N2, N6: put to the owner with this record. Each has a recommended
  answer above, and none blocks adoption.
- N5: to lane-spec, for the dossier specification (PR #353).
- N3, N4, N7: no action beyond this record.
