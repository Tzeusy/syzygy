# RFC-0001 — clause migration rows (rev9 → rev10 compaction)

Source: `_bootstrap/rfc-phase/rfcs/RFC-0001-project-graph-identity-state-planes.md`
(frozen rev9, 9,534 words). Target:
`final-prespec/rfcs/RFC-0001-project-graph-identity-state-planes.md`
(8,350 words, of which 1,919 are verbatim-copied tables and closed
enumerations). History: `final-prespec/history/RFC-0001-history.md`.

No clause was retired, merged, renumbered, or routed out. Every rev9 clause and
lettered sub-clause survives in the active contract at its original identifier.

| Clause | Outcome | Target | Reason |
|---|---|---|---|
| RFC1-1 | retained with wording sharpened | active §3.1 | Rule and both surfacing contexts unchanged; the zero-roots justification compressed to one clause. |
| RFC1-2 | retained with wording sharpened | active §3.1 | `*(History: …)*` parenthetical moved to history; the SDR §4 divergence now cites owner decision B22 explicitly. |
| RFC1-3 | retained with wording sharpened | active §3.1 | SEC-4/SEC-2 premises verbatim; only the forward-reference parenthetical shortened. |
| RFC1-4 | retained unchanged | active §3.1 | Two-authority rule already minimal. |
| RFC1-5 | retained unchanged | active §3.2 | Closed entity table copied verbatim, all 25 rows. |
| RFC1-6 | retained unchanged | active §3.2 | Both deliberate narrowings and their `[Inferred]`/`[Observed]` labels intact. |
| RFC1-7 | retained unchanged | active §3.2 | Extension-profile enumeration is a closed vocabulary. |
| RFC1-8 | retained unchanged | active §3.2 | Frozen-noun mapping is definitional. |
| RFC1-9 | retained with wording sharpened | active §3.3 | Obligation and RFC 0003 delegation verbatim in force; the collision worked-example compressed. |
| RFC1-10 | retained unchanged | active §3.3 | Opaque-identifier rule already minimal. |
| RFC1-11 | retained unchanged | active §3.3 | Split/merge successor rule and rendered-event obligation intact. |
| RFC1-12 | retained unchanged | active §3.3 | No-silent-transfer rule plus its `[Inferred]` label retained. |
| RFC1-13 | retained unchanged | active §3.3 | Map-anchor reliance list is what RFC 0009 cites. |
| RFC1-14 | retained unchanged | active §3.4 | Contains the verbatim architecture.md capability definition. |
| RFC1-15 | retained unchanged | active §3.4 | Reference-not-content rule and its `[Unknown]` label retained. |
| RFC1-16 | retained unchanged | active §3.4 | SDR-3's four classes are a closed enumeration. |
| RFC1-17 | retained unchanged | active §3.4 | Identity-based counting rule (SDR-22) already minimal. |
| RFC1-18 | retained unchanged | active §3.5 | Two-level identity (SDR-2) and the accepted-instability paragraph intact. |
| RFC1-18(a) | retained with wording sharpened | active §3.5 | Rule verbatim; only the sub-clause provenance parenthetical shortened to its consumer list. |
| RFC1-18(b) | retained with wording sharpened | active §3.5 | `*(History: …)*` moved to history; the clause now cites owner decision B3 with a backlink. |
| RFC1-19 | retained unchanged | active §3.5 | Status-claim/evidence rule (VIS-2) already minimal. |
| RFC1-20 | retained unchanged | active §3.5 | Two-exit gap rule with expiry semantics intact. |
| RFC1-21 | retained unchanged | active §3.5 | Contradiction routing and the derived-gap-is-not-a-warrant rule intact. |
| RFC1-22 | retained with wording sharpened | active §3.6 | Plane table and the closure paragraph copied verbatim; the rev8 rewording note moved to history. |
| RFC1-23 | retained unchanged | active §3.6 | Act-assignment rule and both corollaries (SDR-9) intact. |
| RFC1-24 | retained unchanged | active §3.7 | All-status-through-claims already minimal. |
| RFC1-25 | retained with wording sharpened | active §3.7 | Closed class vocabulary and all 26 relation rows copied verbatim; only the rev8 restatement note moved to history. |
| RFC1-25(a) | retained unchanged | active §3.7 | Records owner decisions A6 and A7 and the closure-vs-re-typing distinction. |
| RFC1-25(b) | retained with wording sharpened | active §3.7 | Four-sense table and the twelve-pair checkable rule verbatim; owner decision B20 now cited at the spelling decision as well as in the `[Inferred]` note. |
| RFC1-25(c) | retained with wording sharpened | active §3.7 | Non-functionality, no-primacy, contradiction, and zero-edge rules verbatim; `*(History: review 8, ML-R8)*` moved to history. |
| RFC1-25(d) | retained with wording sharpened | active §3.7 | All four binding-consequence bullets and the class-is-not-a-plane rule verbatim; the rev7-directive provenance note (directive item B5, **not** owner decision B5) moved to history. |
| RFC1-26 | retained unchanged | active §3.7 | Closure and the owner-decision amendment gate intact. |
| RFC1-27 | retained unchanged | active §3.8 | Proposal kinds and exclusivity-group refusals (VIS-1) intact. |
| RFC1-28 | retained unchanged | active §3.8 | Plan-item resolution (SDR §5 q1) intact. |
| RFC1-29 | retained with wording sharpened | active §3.8 | One-way door, constitutive-record, orphaned-work contradiction, and re-materialization rules all intact; the distributed-act framing compressed. |
| RFC1-30 | retained unchanged | active §3.8 | Decomposition/inheritance default already minimal. |
| RFC1-31 | retained unchanged | active §3.9 | Lifecycle state machine copied verbatim (cited by RFC-0003's lifecycle table and by RFC1-25's `supersedes` pair closure). |
| RFC1-32 | retained unchanged | active §3.10 | No-Feature rule (SDR-1) intact. |

## §8 questions

| Question | Outcome | Target | Reason |
|---|---|---|---|
| q1 | open — retained | active §8.1 | RFC1-12 judgment lapse on split/merge — still the owner's choice. |
| q2 | open — retained | active §8.2 | RFC1-6 no doctrine-claim/contract kernel entities at V0 — still the owner's choice. |
| q3 | open — retained | active §8.3 | RFC1-30 decomposition approval inheritance — still the owner's choice. |
| q4 | answered — moved to history | history "RFC1-18(b)" | Answered at acceptance by owner decision B3; outcome carried by RFC1-18(b) and the `succeeds` derived form. |
| q5 | answered — moved to history | history "RFC1-2" | Answered at acceptance by owner decision B22; outcome carried by RFC1-2. |
| q6 | answered — moved to history | history "RFC1-25(a)/(b)" | Answered at acceptance by owner decisions A6/A7 (with B20); outcome carried by RFC1-25, RFC1-25(a) and RFC1-25(b). The RFC9-9 legend follow-on the question raised is recorded in history as still open for RFC 0009. |

## Non-clause sections

| Section | Outcome | Target | Reason |
|---|---|---|---|
| rev9 §0 Reader's summary | retained with wording sharpened | active §1 | Merged with §1 Summary into one scope + reader map; no normative content in either. |
| rev9 §1 Summary | retained with wording sharpened | active §1 | Merged as above. |
| rev9 §2 Motivation and doctrine grounding | retained with wording sharpened | active §1 / history "§2 (rev9)" | Doctrine-grounding citations and both epistemic labels kept in active §1; the failure-mode essay moved to history. |
| rev9 §4 Violation cases | retained with wording sharpened | active §4 | All eleven cases verbatim; only the section's one-line lead-in shortened. |
| rev9 §5 Integration | retained with wording sharpened | active §5 | Both reliance and left-to-them lists retained (the Proposal identity scheme now named explicitly under 0003); forward-references-are-informative rule verbatim. |
| rev9 §6 Alternatives considered | moved to rationale/history | history "§6 (rev9)" | Moved wholesale; alternative 6.1(i) stays in active §6 as one sentence with a pointer, because RFC1-29's sequencing rule is read against it. |
| rev9 §7 Deliberately deferred | retained unchanged | active §7 | Explicit deferrals are Tier 1. |
| rev9 end-of-contract marker | retained with wording sharpened | active end marker | Now states the clause range **and** that there are no gaps, retirements, or merges. |
