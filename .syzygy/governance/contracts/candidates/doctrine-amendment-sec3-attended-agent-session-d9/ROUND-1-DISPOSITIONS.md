# Round 1 dispositions — D9 doctrine amendment packet

> **Candidate — binds nothing.** This record lists each finding of round 1
> and its one repair, under the stopping rule in `REVIEW-BRIEF.md`. The raw
> review is docs/reviews/R-DOCTRINE-AMENDMENT-D9-1-RAW.md, which the lead
> retains. It reviewed commit `c691c6a037098b86046958e0ed023e804edb626c`
> (package digest
> `efb43ad981c30a385ce06732c1e5d470e7bf6e9872d9980d3bb6de91b7886fd5`) and
> returned the verdict `REVISE`, with 4 revise-level findings and 12 notes.
> The lead's dispositions, given 2026-10-06, directed each repair below. None
> of these repairs is confirmed until round 2.

## Revise-level findings

| # | Finding (short) | Repair |
|---|---|---|
| R1 | The violation sentence said the session runs "only on the owner's recorded choice", but the grant required recording only when Syzygy instructs | **Arm A:** the permitted case *is* a Syzygy instruction, and condition 1 requires the choice to be recorded before it is issued, so "Syzygy instructs it only on the owner's recorded choice" is exact. **Arm W:** the sentence now reads "it runs observed code only because the owner chose that (on a recorded choice wherever Syzygy instructs it)". The packet and the P-103 row no longer say "recorded choice" universally |
| R2 | The general exception was wider than the ruling, yet the packet called it the smallest text | The recommended **arm A** is redrafted to the ruling's scope. SEC-3's execution rule binds Syzygy itself, what it launches or schedules, and every instruction Syzygy's software issues, with one permitted case: Syzygy's instruction, on the owner's recorded choice, to an attended session the owner started on the owner's host. The old general text is kept as **arm W** and declared a widening beyond the ruling. The "smallest text" argument is gone (packet §3, Q1) |
| R3 | "One exception" with an agent-session subject would make CI and hand-typed commands violations; the ledger missed the capture tool; the `AGENTS.md` 89 row claimed a "doctrine footing"; it was unaddressed whether an instruction file counts as Syzygy instructing | Arm A names Syzygy as the actor, so CI and hand-typed commands are outside SEC-3's execution rule. They are not permitted by it. The actor question is put to the owner as **Q2**, with a recommendation. Ledger §3.6 adds `capture-test-artifact-main.ts` (`poc:capture-test-artifact`) and states its effect under each arm. It is disclosed as **non-conforming today, independent of D9** [Inferred], and stays forbidden under both arms; no code was changed. The `AGENTS.md` 89 row is corrected. Ledger §3.6 and the delta's terms section address `AGENTS.md`: it is not "an instruction Syzygy's software issues" [Inferred]. Arm W's "Syzygy never instructs" leaves that open, and the ledger says so |
| R4 | RFC5-24 "never visible to observed-project code" and RFC5-12 "Absent: no observed code runs" were misstated as unchanged | Both are quoted exactly in ledger §3.2, with their effect under each arm: RFC5-12's effect changes under both arms; RFC5-24's changes unless the new condition is adopted. The rows are corrected. **Q3** offers (a) accept and record, (b) the D9 condition that no credential Syzygy holds for its typed adapters is readable by the session, and (c) a later RFC 0005 amendment. The recommendation is (b), (a) for RFC5-12, and (c) queued, priced against the owner's 2026-10-05 records ruling. The condition is in both arms as removable bytes (delta, "The credential condition") |

## Notes

| # | Note (short) | Repair |
|---|---|---|
| N1 | RFC5-18 fit holds. The §0 placement was wrong, a third reader-map sentence was missing, and README 199–205's SSH-agent line was unaddressed | Ledger §3.2 fixes the placement: `execution-profiles.md` 30–31 sits above §0, so neither rule strictly covers it. README 130–131 is added, quoted. A row for README 199–205 says D9 permits exactly that case, disclosed |
| N2 | §4 case 7 was missing | Ledger §3.2 adds a row: the case is distinguishable because the code stays untrusted and no trust is assumed |
| N3 | Tell the owner that the dossier brief is CC-SEC-3's named case | Packet §3 and Q4 say so plainly, quoting the clause; ledger §3.3 adds the "Syzygy addition" marker reasoning |
| N4 | "Attends" and "host" left cases open | Both arms add: subagents are part of the session; a process left running after it ends is not, and (arm A) Syzygy's instruction never asks for one. Cloud sessions and rented VMs are in ledger §5 item 5 and packet **Q5** |
| N5 | Condition 3 was narrower than "the run record lists the commands" | Arm A reads "Every command the session reports having run is disclosed". Arm W adds "wherever Syzygy renders anything drawn from the session" |
| N6 | Ledger figures lacked commits; 57 vs 62 | Every figure now names its commit. The sweep was re-run at `eb7be564`: 241 files; the term sweep, 250 files, now over the same population; line citations, 66 matches in 29 files, 5 of them register rows. The round-1 "57" is explained in §2. The packet's figure names its commit |
| N7 | "ambient credentials for convenience" was presented as a quotation and is not one | The packet now quotes the real sentence, "an execution profile that inherits the host user's ambient credentials 'for convenience.'" |
| N8 | Put the "exposure is the same" point into the violation bullet | Both arms' violation bullets read: "Its exposure to the owner's credentials is the same; what differs is that nothing claims otherwise." |
| N9 | Clause (b) is optional either way | (b) is labelled optional in the delta, the packet and Q1, and ledger §3.1 states its cost |
| N10 | The change class: "widened" describes the permission | The delta's class now reads: Normative; the prohibition is narrowed for one case, obligations are added, and arm A states the rule's actor |
| N11 | The blocking-RFC bullet is unscoped beside the exception, which is moot | Kept verbatim; it is moot because RFC 0005 is accepted. No change |
| N12 | The packet hid R2, R3 and R4 from the owner | Packet §3 states all three in plain terms, with the capture tool, CI and hand-typed commands, RFC5-12 and RFC5-24 |

## Other changes made in this repair

- The branch was rebased onto `origin/main` `eb7be564`, which retains the
  dossier review-1 raw. The delta now quotes finding 8 from it instead of
  routing through the rulings direction.
- The application probe was re-run at `eb7be564` with arm A applied: 78
  commands, 4 nonzero, the same four regenerations. Arm W was not re-run
  (ledger §4).
- The owner's records ruling (`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`),
  which landed after round 1, is cited where it bears on the evidence and on
  Q3's cost.
