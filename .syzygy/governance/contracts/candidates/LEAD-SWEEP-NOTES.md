> # Historical — round record, not a current offering
>
> **Do not read a digest here as an act argument.** Working notes from the rev10/round-2026-08 leads. Every digest in this file is that round's and none is a current act argument. Current arguments
> come from `ACTIVE-CONTRACT-MANIFEST.txt` and
> `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, never from a round record.

# Lead's final-sweep obligations (working notes, non-normative)

Accumulated from compaction-worker reports; each must be discharged before
the fresh-context reviews.

1. **Citation normalization across packages.** RFC-0004, RFC-0005, RFC-0009
   are packages; internal section numbering diverged (RFC-0001 has no §2;
   RFC-0005 renumbered before splitting). Sweep all active files: cross-RFC
   citations must use clause IDs (`RFCn-m`) or RFC-level question IDs
   (`RFC 000n qN`) — never another RFC's `§n.m`. Question numbers are
   RFC-level and immutable.
2. **RFC-0002 invariants to verify at integration:** RFC2-24 primary-reason
   list keeps **#12 `execution-blocked`** and #11 `reference-unresolvable`
   (RFC5-18 and RFC6 cite them); RFC2-4's degradation-only rule intact
   (B4/RFC5-11 relies on it); RFC2-1 items 1–11 verbatim, unrenumbered.
3. **RFC4-23(2) cites RFC8-16** (forward) — confirm resolves after RFC-0008
   compaction.
4. **RFC9-9 follow-on** (from RFC-0001 §8 q6 / A6): legend/edge-channel pass
   for the kernel-level declared dependency — must surface as an open item in
   RFC-0009's package or be added to the open-question triage.
5. **provides_to/depends_on graph consistency:** RFC-0001 and RFC-0006 now
   declare RFC-0010/0011 edges; RFC-0004 adds RFC-0011; RFC-0005 declares
   RFC-0008/0010/0011. Rebuild the graph at index time and check symmetry
   claims in 05-CONTRACT-INDEX.yaml (a `provides_to` edge should appear as
   the counterpart's `depends_on` where the dependency is real, but
   asymmetry is allowed where consumption is one-way — record, don't force).
6. **Corpus-size justification** for 03-ACTIVE-CONTRACT-COMPACTION-REPORT:
   RFC-0001 8,350 (dictionary-shaped, 23% verbatim vocabularies);
   RFC-0006 4,172 (floor 2,898 clause words); RFC-0004 7,694 → package;
   RFC-0005 6,543 → package. Collect per-RFC incompressibility accountings
   verbatim from worker reports (stored in ARTIFACT_REGISTER addendum or
   report itself).
7. **Verifier updates needed at integration:** package README front matter
   (id present; status_source may be absent on READMEs — decide and align
   script); matrix outcome vocabulary now includes package module targets.
8. **RFC-0005 limb rows**: rev9 end marker says no lettered sub-clauses;
   worker added limb rows marked as such — keep the matrix's limb-row
   convention documented in 04's preamble.
9. **RFC-0002 rulings for the semantic-equivalence reviewer:** the
   "#10 not split" wording in RFC2-24 is a deductive entailment of A5's
   closed-at-twelve (flagged in history q1); RFC2-24's per-cell
   `*Added:*/*Renamed:*` narratives moved to history with Condition/
   Resolution columns verbatim. Both deliberate, lead-accepted.
10. **Packages now: RFC-0002 (4 modules), RFC-0004 (4), RFC-0005 (3),
    RFC-0009 (3).** RFC-0004 package built and single file deleted;
    0002/0005 authorized, executing. Verify single-file deletions and
    matrix-row target updates for each.
11. **RFC-0001 (8,350) and RFC-0002/0005 pre-split sizes** — RFC-0001
    remains the only above-band single file (dictionary-shaped; no split:
    reader groups not distinct — it is one dictionary). Owner-facing
    justification + context-load test required per OD-R10-3. RFC-0006
    (4,172) fine.
12. **RFC-0003 package authorized** (2 modules, non-contiguous set:
    governance-homes owns RFC3-15..17+letters incl. new 16(c); manifests
    owns the rest). RFC3-16(c) final text verified against design — the
    acceptance-record §2 rewording remains the lead's job in the FINAL
    record. RFC-0003 sweep numbers (23 tokens, 90 citations, 12/4/1
    labels) live in its matrix-rows preamble for the reviewer.
13. **RFC-0008 rulings:** B13-supersession of RFC8-25's "operative limit"
    fallback upheld (strictly stricter; retired text verbatim in history) —
    the ONE clause-text semantic resolution of the corpus; point the
    semantic-equivalence reviewer at it explicitly. Split authorized
    (3 modules: 8-1..11 / 8-12..20 / 8-21..32). RFC8-27's "RFC 0004 §6"
    cite repointing assigned to the rfc8 worker. RFC-0010 §5 updated with
    the two-field rule (RFC8-12 + RFC8-28, RFC8-30 gate).
14. **Worker calibration consensus:** compaction band is −12% to −22%
    across all seven reporting passes; the 35–50k corpus target is
    unreachable by prose compaction alone. The honest rev10 posture:
    materially-below-90k corpus (~65–70k projected) + selective loading
    via packages/index/context-packets as the real context reduction —
    the 03 report must present this as the owner-facing justification
    OD-R10-3 provides for, with the per-RFC incompressibility arithmetic.
15. **RFC-0007 rulings:** split authorized (narrative-contract RFC7-1..25 /
    rendering-and-surface RFC7-26..38; spanning violation cases 10/13/15 →
    README, rest distributed). Accepted: source-grounded front matter (no
    0010/0011 edges); authored-position markers → decision cites (B5/B6 —
    strengthening, show the reviewer); B10 folded into RFC7-20;
    `dismissed-by-decision` enumeration restored in RFC7-20 (closed-vocab
    partial-quote catch). Sub-clause rows supplementary; numbered corpus
    count for 0007 = 38. RFC3-31 cite left with §6 alternative in history
    (deliberate).
16. **RFC-0003 package complete & verified** (M1 4,824 / M2 4,275 / README
    920; union sweeps clean vs both baselines; case 9 limb-split across
    modules with cross-pointers — documented design). Lookup: 15–17+letters
    → governance-homes; else manifests. +903 w scaffolding overhead noted
    for the 03 report's package-overhead accounting.
17. **RFC-0002 package complete & verified** (modules sliced at §3 seams,
    byte-identical clause text; obligation sweep: package matches rev9
    better than the single file did, zero split-introduced losses). Two
    restorations during split: q4's "never as two independent aggregates"
    wording; end-marker's add-lettered-sub-clauses permission. Cases
    3/5/11 package-level. Bidirectional 0003/0004 edges accepted (real).
    Cross-pass lesson recorded: package indexes thin §8 answer tables —
    obligation sweep over the union is the catch. RFC-0010/0011 cite
    RFC-0002 by name not clause ID — lawful (charter forbids only
    section-number cites); optional sharpening at final sweep.
18. **RFC-0005 package complete & verified** (34 closed-vocab strings, 56
    cross-refs, transposition diff pointer-only; case 11 → README; §3.n
    numbering restored so external section cites resolve — no
    normalization needed for RFC-0005). Its two sweep asks: RFC-0002 #12 +
    RFC2-4 — already confirmed by the RFC-0002 pass; RFC-0004 README's
    RFC5-17/18(e)/21 cites — confirm at final citation sweep.
19. **RFC-0008 package complete & verified** (byte-identical except ordered
    RFC8-27 repoint to RFC-0004 history record; cases 4/12 → README;
    two-field handoff rule stated once in README §5; RFC8-32's coverage
    matrix explicitly package-wide — pattern for other packages' phase
    rules: check RFC7-38/RFC9-52/RFC2's and RFC3/4/5's absence of one).
    Distributed provides_to per-module (union in README) — richer than
    other packages; index generator must read module-level front matter.
20. **RFC-0007 package complete & verified** (case-anchor deviation
    accepted: only case 13 spans, 10/15 → module 2 — anchor test is the
    standing rule; RFC7-38 package-scope note added matching RFC8-32's;
    module-level narrower front matter, README union; module 2 explicitly
    §8-empty). Zero stale §3.x refs — all clause-ID'd at split.
20a. **Correction to note 20 (final RFC-0007 state):** crossed messages led
    the worker to apply "10/13/15 → README" with anchor annotations naming
    the module-1 invariant each defeats (10: RFC7-2/3; 15: RFC7-13). With
    those annotations all three dual-anchor across the seam, so README
    placement satisfies the anchor test — ACCEPTED as final. Final counts:
    README 2,268 / narrative 5,167 / rendering 3,143; sweeps re-run clean;
    single file deleted. Note 20's "10/15 → module 2" is superseded.
21. **RFC-0009 package complete & verified** (report received in full).
    RFC9-9 legend/edge-channel follow-on: visible open item at
    semantic-geography §10, owner-scoped, home RFC1-7/RFC1-26,
    fails-closed mitigation under RFC9-26 — ADDED to triage. Accepted:
    module-scoped deferral lists stay active (charter-conforming); q3
    residual stays as RFC9-41 clause text; 15,568 package floor; 6,999
    one-word margin (range-split remedy noted, not needed). provides_to
    0010/0011 on module 3 only (RFC9-52) — correct precision.
22. **Transaction review dispositioned** (EXCEPTIONS ×5 → 4 fixed now, 1
    queued). E4 retirement notice added to the rev9 record header — lead
    action, adopts nothing, surfaced to owner. E1-RFC sentence queued in
    reviews/DISPOSITIONS.md; it is currently the ONLY manifest-invalidating
    fix. Topology bundle now ships in the packet (E2). Reviewer confirmed:
    manifest digest byte-exact, 32/32 modules verify, all four act digests
    match their real homes, all 32 Status headers clean, rev9 defect absent.
23. **Four of six reviews dispositioned** (transaction, digestibility,
    boundary, portability — all EXCEPTIONS, none reopening an owner
    decision; all four independently confirmed the manifest digest,
    fixture measurements, and verifier). Free-side fixes applied; the
    consolidated rfcs/ batch (DISPOSITIONS §"Consolidated") is the ONLY
    thing that will churn the act-1 digest, applied once after the
    remaining two reviews (equivalence, safety) land. Triage-count
    transposition (boundary E9) was my own unverified-summary error —
    the enumeration now lives beside the summary. Index generator gained
    kind: phase-rule + governance_sources; had a cross-process
    set-order-tie nondeterminism, fixed with a total-order sort key.

24. **All six reviews dispositioned; consolidated rfcs/ batch APPLIED
    (2026-08-03)** — RFC-0010 (13 edits, 2,453→3,096 w), RFC-0011 (11
    edits, 1,880→2,257 w; first run aborted on a line-wrap mismatch in
    the RFC11-6 anchor — nothing was written, whole batch re-run),
    RFC-0003 RFC3-16(b)/(c) constraint-vs-authorization split, RFC-0001
    history cite, RFC-0007 README phase-boundary section, RFC-0008
    README substrate tag, three README count tables. Scripted refresh:
    fixtures 1–5 re-measured (10,854–18,302 w; digests updated —
    fixture 3's byte digest changed with an unchanged word total, which
    is exactly why digests are scripted), 06 map regenerated (incl. the
    two stale README cells 2,266→2,029 and 2,268→2,326), index
    regenerated `--check`-clean, manifest regenerated. **New act-1
    digest `08793ddf70f3c2a3…`; verifier PASS (99,067 w, 322 clauses).**
    Record §1/§3/§6/§7 updated (§7 now 9 items). Final confirming
    review dispatched over the exact final manifest.
