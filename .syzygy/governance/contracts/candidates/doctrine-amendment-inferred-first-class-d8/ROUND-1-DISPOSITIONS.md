# Round 1 dispositions — D8 doctrine amendment packet

> **Candidate — binds nothing.** The drafter's record of how each round-1
> finding was handled. A disposition is not a confirmation: no reviewer has
> read the repaired bytes.

**Round:** 1, fresh context. **Raw:**
`docs/reviews/R-DOCTRINE-AMENDMENT-D8-1-RAW.md`, retained as the reviewer
handed it back. The reviewer reported that, before handing back, it
corrected two of its own line citations in the raw (REQ-031 vs line 508;
the Definitions span); the drafter did not edit the raw.
**Reviewed commit:** `59fbf78700d72b14d1551926c2b55b464c61aa5e`.
**Package digest reviewed:**
`330e61136be78086f7ecf17418f417d54bbacbb11f7bac7d37782d57108a8746`
(re-derived by the drafter at that commit with the brief's method).
**Verdict, copied from the raw (line 4):** `Verdict: REVISE`.
**Findings:** 15 — five revise-level (1–5) and ten notes (6–15), per the
raw's own summary.

**Stopping rule** (set in `REVIEW-BRIEF.md` before the round): one round;
each finding repaired once and recorded here; no round 2. The repaired
bytes go to the owner as **repaired once, unconfirmed**. `REVIEW-BRIEF.md`
is the round-1 brief and is left as it was reviewed, including its
"running governance root" wording, which clause (d)'s repair replaced.

Every repair below was re-derived from the source file, not copied from the
raw: line numbers, quotations and counts were re-read or re-run at
`59fbf787`. Doctrine, accepted-contract and specification bytes are
identical at `6bb6ef26` and `59fbf787`.

| # | Level | Finding (short) | Repair |
|---|---|---|---|
| 1 | revise | (f) maps to `unadopted-draft`, but a draft that stays non-citable after the human act is RFC2-25's `editorial-draft` | Clause (f) now reads "an editorial draft: it is not a claim source before a human authors it into a presentation artifact, and stays non-citable after"; packet §0 row, §1 (f) class (quoting RFC2-25 lines 191–196), §2 row and the delta's class row now name `editorial-draft` |
| 2 | revise | (d)'s premise ("Yes, by omission", "writable governance root") misplaces the blocker; the no-change arm is overstated; Definitions not reconciled | §0 (d) row rewritten: doctrine does not forbid a write in the abstract; today's blocker is the empty `writeSurface` and the 2026-09-02 act; P-71-Q5's two-act route quoted. (d) is now presented as an *alternative* destination, the grouping in §0 is three groups, and Q4 gains a "use P-71-Q5's act route instead" arm with the trade-off stated in §1 (d). (d1) redefined as "a project whose designated governance root Syzygy may read … but may not write", consistent with the Definitions entry for **Project** (lines 210–216), which §1 (d) now cites. No-change arm rewritten to name the act route |
| 3 | revise | (e) not fully representable: "self-observed" unmapped; "restricted below `gate-backed`" misuses RFC2-25's restriction sentence | Clause (e) now says the records "render with that subject disclosed"; §2 maps that to the observation record's repository identity (a provenance fact, not a tier or state), and restates the effect as a rule on which records a claim may cite, grounded in RFC2-25's "The **only** tier that may support a positive status claim", with no ordering of tiers implied |
| 4 | revise | (e)'s "never satisfy this floor" is broader than intended; trigger phrase undefined; scope lives only in the packet | Clause (e) rewritten: trigger is "Syzygy's observation pipeline evaluates Syzygy's own governance root as its subject"; the denial is confined to "the evidence for a claim about Syzygy's own alignment, convergence, genome-completeness or release verdict"; a last sentence keeps pipeline-property evidence over this repository available. "Raise challenges" became "surface gaps and contradictions", since an observation record holds deterministic facts only (lines 114–115). §1 (e)'s scope note now rests on the defined term "observation record" (line 144) |
| 5 | revise | The reader sweep misses `$CS/` readers; application breaks a battery check the ledger does not name | Ledger §4 rebuilt around an application probe: all seven blocks applied in a clone at `59fbf787` and the canonical battery run against an unapplied baseline — 80 commands, 0 nonzero baseline, 6 nonzero applied. Each is tabled: CG-18, the budget report, the contract index, the directive register, and **the Polaris understanding adoption recorder's `--check` and `--selftest`, which bind `vision.md` as a frozen review input** — a gate the round did not name, now packet §7 Q-A1. The static sweep widened to every tracked code or data file outside doctrine (686 files, 39 readers). Packet §9 step 3 names the context-budget report and its fixture anchors |
| 6 | note | (b) departs from L3-M7's rendering without saying so; L3-M7's Unknown-filler | Packet §0 adds "Two departures from L3-M7 itself", quoting both L3-M7 sentences; clause (b) gains "It sits beside an Unknown, never in its place." |
| 7 | note | (b)'s no-change arm overstates; use is consent-gated too | Arm rewritten, quoting the persistence-and-use sentence. Re-derived: that sentence is in REQ-polaris-generation-019 ("Versioned interchange and reference integrity", requirement heading at line 506, sentence at line 508), not REQ-031, and is cited so |
| 8 | note | (b)'s "which of two sources governs" blurs adjudication; heading no longer covers the section | Example replaced by "a priority between two goals"; §1 (b) states that a contradiction ruling resolves RFC2-24 reason 8 (`contradicted-pending-adjudication`, "Owner adjudication") and is a recorded human decision, not this class; the placement wrinkle is disclosed and left as an editorial question, not drafted |
| 9 | note | (c) is not Clarifying | Reclassified "Normative, narrowing over a wider domain" in packet and delta. Re-reading the doctrine found its authority limit is already doctrine for every subject, `trust-and-evidence.md` lines 118–119 ("Inference has no authority to establish a status — only to challenge one."), now cited in §0 and §1 (c); the decline recommendation stands on that |
| 10 | note | The PWB coverage row is RFC7-2(b) only; `project-fact` inference unlabelled | §0 (a) row and ledger §3.3 now quote the row and its reason, say "RFC7-2(b) only", and label the `project-fact` question [Inferred] |
| 11 | note | §4 table counts 12 readers against 11 | Superseded by the rebuilt §4; the new static count is re-derived and partitioned (20 evidence and pursuit, 1 launch-gate record, 2 historical, 1 index, 15 code), summing to 39 |
| 12 | note | Ledger figures predate the reviewed commit; P-98 hit undispositioned | Ledger re-pinned to `59fbf787`: 1,554 files, 147 hit files, 407 occurrences, two methods 147 each (the drafter's own re-run; matches the raw). `PENDING-OWNER-DECISIONS.md`:1042 (P-98, "the copy roles of the new strings") now has a §3.2 row tying it to Q-S1 |
| 13 | note | Register row P-102 absent; P-75 Q4 cited but unused | §9 now says P-102 is added on this branch, and it is (register row P-102). P-75 Q4 is now quoted in §0 as the reason the state is representable in the shared model today with no constructor |
| 14 | note | (a): "anchors nothing" vs RFC7-9/7-10; "withdrawn" not a freshness value | Clause (a) now says "is never itself an anchored claim" (glossed in §1 (a) as not an RFC7-2(a) claim) and "no fresher than its stalest input, and is withdrawn until regenerated when any input is broken or superseded"; §2 maps each of RFC2-10's four values and says "withdrawn" is a render action |
| 15 | note | (d)'s destination phrase not a doctrine term; cross-project deferral unconsidered | (d2) now says "the observing project, the governed project that records the consent to observe it", the phrase P-76 Q2's ruling uses; §1 (d) quotes RFC1's portfolio-profile deferral and SDR-30, and §7 adds Q-C2 |

## Found while repairing, not in the raw

- **The recorder gate (finding 5's table)** applies to D7 as well, whose
  ledger calls the recorder "unaffected". Routed to the coordinator; D7 is
  not edited here.
- **The application probe moved VIS-7 by seven lines, not six**, because
  repaired (d2) is one line longer. Ledger §4 states 250 → 257.
