rev-pr489-q8m3vt

This is the verification round on PR #489 at head `e990c27e49381d659226abf7c28d9e98915ed4bd` (one repair commit after `9e63b856`). I made no edits and no git, gh or bd writes. Line numbers refer to `.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md` (called "record" below) unless another path is given. The repair commit touches only the record, `PROJECT-STATUS.md` and `decisions/README.md`.

**Resolved repairs**

- **Finding 6.** [Observed] The tree-framing row now has a dated 2026-10-21 mark after the 2026-10-15 one.
- **Finding 7.** [Observed] The container-shape row is now a dated mark. The README and gate rows list the carve-outs.
- **Finding 8.** [Observed] Record:226–231 now separates the bead graph from the packet's third gate.
- **Finding 9.** [Observed] A dated mark at the P-114 sentence explains what "this revision" refers to, and the evidence file is left unedited.
- **Finding 10.** [Observed] Record:187–195 adds link 4, `syzygy-dov.12.1`, marked "position only". It is placed and not authorized, and its authority is stated.
- **Finding 4.** [Observed] Record:143–155 now states openly that machine-view applies a narrower reading of the 2026-10-15 rule, gives a fallback order if the owner overrules it, and labels it [Inferred].
- **Finding 5.** [Observed] The draft-view fence quotes `PWB-MACHINE-VIEW-AMENDMENT-ACT.md:90-92` exactly. `syzygy-dov.11.2` is removed from the authorized beads.
- **Checks.** [Observed] `check_governance.py` gives 32 OK, 21 WARN, 0 FAIL. The only change from the previous head is one extra CG-1b reference examined. No added line has an unbalanced backtick, and no digest appears.

**Findings**

1. **Important. [Observed] The overlap reading builds behaviour across the five contract-coverage gaps that the record admits are unresolved.**
   - The packet's gate is not only about M2 slice 5. `pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md:72-74` says the act does "not weaken those contracts or authorize implementation across the gaps".
   - The gaps sit on the disclosure itself. `SEMANTIC-DELTA.md:120-124` names them as RFC6-14.r1, RFC6-14.r3, RFC6-17.r1, RFC7-16.r1 and RFC7-33.r1, and they arise from the outside-slot disclosure, not from slice 5's declared bound.
   - Record:229 says the owner's selection "resolves none of the five gaps". Yet record:253–263 authorizes rows to build that disclosure (item depth's relation-claim disclosure, the opening-band count).
   - The justification at record:266–268 ("places its open gates on 'M2 slice 5' specifically") leaves out packet lines 72–74.
   - [Observed] None of the five gap identifiers appears anywhere in the item-depth package's `.md` files.
   - On scope: granting a narrower piece of what the owner selected does stay inside the owner's 2026-10-20 answer. The problem is not scope. It is that the packet requires the gap-crossing authorization to resolve the gaps and name the built behaviour, and this one does neither.

2. **Important. [Observed / Inferred] The opening-band count would assert a condition that the registry falsifies.**
   - The scenario at `spec.md:1037-1062` applies only when a class has "no currency-bound declaration with effective owner-act provenance".
   - The 2026-09-30 registry act (`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md:70`, "13 explicit per-class currency bounds") is in force. The adopted entry, `adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` at `/entries/0/currencyBounds`, has a row for each of the thirteen existing project-shape classes.
   - The implementation consumes none of them: `packages/three-surface-poc-core/src/model.ts:152-159` keeps `currencyBounds: []`. So today's per-claim "Currency bound not declared" text is already a pre-existing mismatch.
   - [Inferred] Record:256–262 has the opening band count "members under the condition" while "no existing claim class changes how its freshness is decided". That carries the mismatch into a new aggregate count, a VIS-2 problem.
   - Only item depth's new `governing-intent-relation` class truly has no row, so item depth's half of the reading is sound against `spec.md:1993-1999`.
   - Fix: limit the opening-band half to members whose class has no registry row, or disclose the pre-existing mismatch and route it to `syzygy-dov.19`.

3. **Important. [Observed] Record:243–244 misquotes the specification (rule 8).** "the PWB-REQ-007 label, tier and freshness" does not occur in `spec.md`; I checked with a whitespace-normalized search. The clause, at `spec.md:1383-1385`, reads "it discloses its own label, tier, freshness and separate primary and secondary reason counts as PWB-REQ-007 requires of an aggregate". The substance holds, because the clause incorporates PWB-REQ-007's aggregate rules by reference, but the quotation must be exact.

4. **Important. [Observed / Inferred] The confirmation line does not bind the bytes it confirms.** The repair answers the first-round problem: the channel is now the owner questionnaire, the same channel as the original answer, and the GitHub-approval claim is gone (record:20–34). Three gaps remain:
   - The template at record:32–34 names no commit or file digest. [Inferred] Any edit after confirmation, such as a further repair round, would carry the confirmation over bytes the owner never saw (rule 10/11).
   - "corrections: <none or list>" lets corrections be recorded beside body text that contradicts them, rather than applied to the body and confirmed again.
   - Only process stops a merge before the line exists. Meanwhile the PROJECT-STATUS gate row already shows "✅ Granted" under "Every gate below is closed" (`PROJECT-STATUS.md:304`).
   - Fix: have the line name the commit it confirms, and require corrections to be applied before confirming.

5. **Note. [Observed] The dismissal stop list resolves finding 3, with one ambiguity.**
   - The no-home quote at record:317–321 matches PWB-REQ-007 "Dismissal records" verbatim.
   - Question 2's "where" half is now fenced (record:325–326), and question 7 is fenced (record:327–328).
   - The open point: record:321–322 says "Every other dismissal behaviour is exercised only on synthetic fixtures", while record:327–328 forbids re-reading "a dismissal through a retained evaluation". It is unclear whether a fixture-only test of the signed retained re-read scenario is allowed. Say which, or say that scenario stays unbuilt and goes to escalation.

6. **Note. [Observed] Two unlabelled or inconsistent statements around `syzygy-dov.11.2`.**
   - Record:297–300 says the status route's authority is P-78 under the continuation act. That is the recorder's inference and carries no [Inferred] label.
   - The fallback order at record:154–155 places `syzygy-dov.11.2` in the chain even though the record does not authorize it. Mark it "position only", as link 4 is.

7. **Note. [Inferred] The draft-view fence is correct but probably makes `syzygy-dov.7.2` unbuildable** until the later route amendment exists, because no record-level fields may be designed (record:305–306). The escalation route is stated, so a lane will stop honestly. Telling the owner this up front would help.

Verdict: REVISE