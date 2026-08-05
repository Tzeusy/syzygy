# Exit report — rev10 final pre-specification run (directive §14)

> **Historical exit report (2026-08-03), tracked as packet history.** Its
> digest values are those current at writing; all four act arguments were
> re-quoted 2026-08-05 — see the acceptance record §1a.


**Date:** 2026-08-03. **Run:** the owner directive preserved at
`_bootstrap/rfc-phase/REV9-FINAL-PRESPEC-DIRECTIVE.md`, executed in full.
**No gate was executed** — every owner act below is an open offer.

## §14's nine exit questions, answered with evidence

1. **Is the active contract corpus materially smaller and more selectively
   loadable than rev9?** Yes on loadability, honestly qualified on size.
   [Observed] Rev9: 90,410 words in nine files, one mandatory whole-corpus
   reading path (~121k words with doctrine/craft/topology/overview). Rev10:
   99,067 words on disk across **32 modules** (compacted rev9-derived
   normative text 73,685, −18.5%; the growth is package scaffolding,
   navigational READMEs, and the two new contracts), with 27,521 words of
   history extracted to Tier 2 outside every default load. The owner's
   35–50k band was **not reached** — nine independent compaction passes
   each hit an incompressibility floor at −12…−22% (arithmetic in
   `WORKER-REPORT-DIGEST.md`); the 03 report presents the trade as record
   §7 item 5. What the corpus optimizes instead is the per-task load.

2. **Can one typical agent task receive complete governed context without
   loading all RFCs?** Yes. [Observed] Five measured context-selection
   fixtures: 10,854–18,302 words mandatory load (median 13,864 ≈ 18.7k
   estimated tokens ≈ 9–15% of the rev9 path), each with deterministic
   selection traces (RFC11-4 over `05-CONTRACT-INDEX.yaml`), omitted-
   candidate reasons, and re-runnable packet digests. The confirming
   review reproduced all five byte-exact on the final corpus.

3. **Does Mission Control let a human approve one bounded Mission rather
   than micromanage every work item?** Yes, as contract. [Observed]
   RFC10-4/5: one owner act approves one mission bound to an envelope
   (scope, budget, gates, prohibited surfaces); work items inside the
   envelope proceed without per-item acts; RFC10-12's attention queue
   routes only genuine escalations, one act per item (or explicit
   enumeration). The approval act itself is always an owner-attended
   A1-mechanism runtime act (RFC10-9) — V0 must ship that ceremony
   (record §7 item 6).

4. **Can no agent widen its own envelope, budget, write scope, or required
   gates?** Yes, multi-layered. [Observed] RFC10-8 (envelope immutable to
   its holder; child grants are explicit, reservation-debited subsets);
   RFC10-15 (prohibition wins ties; store minting needs a recorded owner
   widening); RFC11-1 (packets report, never grant); RFC11-10
   (self-asserted gate-satisfying profile fields fail closed); RFC11-8
   (envelope-interpreting memory is authorization-bearing);
   RFC3-16(a)/(b)/(c) (authorizations-for-effect fail the predicate
   without owner-act provenance). Disclosed residual: the rule is
   single-sourced in RFC-0010/0011 — RFC 0001–0009 do not restate it
   (record §7 item 9).

5. **Are portfolio policy and project truth kept in distinct authority
   planes?** Yes, unchanged from the accepted design. [Observed]
   SDR-28…30 + RFC3-10…13 + RFC7-36 (portfolio truth derived-only; the
   workspace manifest never authoritative for project-internal truth);
   RFC-0010 adds nothing cross-project without its own act — fixture 5
   walks the cross-project mission case and loads both planes' rules.

6. **Is owner-act status honest before and after independent audit
   correlation?** Yes. [Observed] RFC3-16(c)'s two-state model:
   "owner-adopted (bootstrap, uncorrelated)" vs "Syzygy-verified", never
   conflated, commits/tags alone never sufficient (owner decision
   preserved verbatim); the constraint/authorization split in RFC3-16(b)
   fixes what each state suffices for; record §2 states the machine-side
   complement so acceptance is knowing.

7. **Does every user-observable future behavior still route through
   OpenSpec?** Yes. [Observed] Six shape-parallel phase-rule clauses
   (RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12), each with
   the four limbs; the routing matrix classifies all 322 clauses
   (DI/OS/CR/IR/DI+OS) with a coverage skeleton; RFC11-4 forces the
   governing phase rule into every packet; the index marks the six
   clauses `kind: phase-rule`. No OpenSpec changeset was created.

8. **Can a fresh reviewer reproduce every mechanical claim on another
   machine?** Yes, demonstrated twice. [Observed] The portability review
   ran the full battery from a copy outside the repository on stdlib
   Python (verifier, index check, manifest check, all five fixtures
   exact); the confirming review re-reproduced everything on the final
   bytes. Scripts derive their root from their own location; source
   resolution is logged to stderr; shell assumptions are stated.

9. **Is the project genuinely ready to begin its first OpenSpec feature
   changesets?** Yes, conditional only on the owner gate. [Observed]
   `09-OPEN-SPEC-READINESS-REPORT.md`: criterion table + the re-derived
   per-question triage (6 questions may stay open; 13 close before V0;
   7 before Mission Control V1; none blocks specification authoring, with
   the argument shown per question in `08-OPEN-QUESTION-TRIAGE.md`).

## The five §14 return items

1. **Compaction result:** `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` +
   `04-CLAUSE-MIGRATION-MATRIX.md` (all 294 rev9 clauses accounted for;
   zero merged, retired, renumbered, or routed out) + `history/` Tier 2.
2. **The two new foundational RFCs:**
   `rfcs/RFC-0010-mission-control-autonomy.md` (RFC10-1..16) and
   `rfcs/RFC-0011-context-compiler.md` (RFC11-1..12), both reviewed
   through the six-round battery + confirming review.
3. **Owner decisions still requiring explicit judgment:** the **ten** §7
   items in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` —
   headline items: q4 `declarations/` six-name validator; SEC-3
   extension ratification; D3 bounded-mission amendment (adopt/amend/
   decline, consequence stated); the A1-ceremony-as-V0-precondition
   consequence; the decomposition-grant ruling; D4 (VIS-4
   self-licensing); the corpus-size trade; and R1 (the one stale
   navigation count inside the digest set — knowing acceptance or one
   more digest cycle).
4. **Final exact-digest acceptance record:**
   `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`. Act 1 gate (open,
   not executed): `ACCEPT COMPACTED FOUNDATIONAL RFCS:
   08793ddf70f3c2a30b5dcec51cac9266a81d03e9db48aa8b7071953f7687c936`.
   Acts 2–4 unchanged from rev9 (craft `aa2d6353…`, topology
   `0d34d1b5…`, overview `42de2eb1…`); optional phraseless act 5 = D3.
   The rev9 phrase `ACCEPT FOUNDATIONAL RFCS` is retired unconditionally
   (notice in the rev9 record). Confirming review: **CONFIRM** at the
   exact digest above (`reviews/rev10-confirming-review.md`).
5. **Recommended first OpenSpec changeset sequence** (advisory, commits
   nothing): selection-api → intent-surface (Polaris) → work-surface
   (Trajectory) → mission-control → context-packets → map-surface
   (Orrery) — rationale and coverage obligations in
   `09-OPEN-SPEC-READINESS-REPORT.md`.

## Boundary attestation

No OpenSpec changesets, Beads issues, implementation plans, stack
choices, application code, or `about/**` were created in this run
(directive §14 closing constraint; AGENTS.md hard boundaries). The
`verify_pre_beads_boundary.sh` known `.beads/` false positive stands as
the only expected flag.
