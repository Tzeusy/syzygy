# Contract-coverage repair delta

The three normalized consequence matrices are frozen audit outputs. This delta
supersedes only the listed consequence dispositions after requirements
PWB-REQ-007 and PWB-REQ-014…016 and the strengthened PWB-REQ-001/005/022 were
added. Unlisted matrix rows remain unchanged.

Each effective consequence has exactly one disposition. Rows that split a
broader audited consequence use distinct repair IDs and jointly supersede it.

Declared totals: **69 rows; 62 superseded base rows; 52 covered; 14 Unknown
uncovered; 3 believed not applicable.**

| Repair consequence ID | Supersedes | Clause | Effective consequence | Disposition |
|---|---|---|---|---|
| RFC4-3.r1 | RFC4-3.c2 | RFC4-3 | Every emitted project-shape fact carries a capture instant distinct from source-claimed time | unknown-uncovered |
| RFC4-3.r2 | RFC4-3.c3 | RFC4-3 | Every emitted project-shape fact carries observer identity and version | covered:PWB-REQ-001 |
| RFC4-3.r3 | RFC4-3.c4 | RFC4-3 | Output from an unregistered or unverifiable observer cannot influence the model | covered:PWB-REQ-005 |
| RFC4-7.r1 | RFC4-7.c1 | RFC4-7 | The project-shape observer has a versioned per-project registry entry | covered:PWB-REQ-005 |
| RFC4-7.r2 | RFC4-7.c2 | RFC4-7 | Observer registry identity/version is an evaluation input | covered:PWB-REQ-005 |
| RFC4-7.r3 | RFC4-7.c3 | RFC4-7 | Missing or unverifiable registry provenance blocks reads and facts to Unknown | covered:PWB-REQ-005 |
| RFC1-18.r1 | RFC1-18.c1 | RFC1-18 | Every project Claim has the accepted durable-identity derivation and an evaluation instance | unknown-uncovered |
| RFC1-18.r2 | RFC1-18.c2 | RFC1-18 | Every project Claim instance has deterministic same-evaluation identity and the complete accepted tuple | unknown-uncovered |
| RFC1-19.r1 | RFC1-19.c1 | RFC1-19 | Positive project status requires current support; absence remains Unknown | covered:PWB-REQ-007 |
| RFC1-19.r2 | RFC1-19.c2 | RFC1-19 | Narrative prose doing badge work is held to the same evidence rule | covered:PWB-REQ-007 |
| RFC1-24.r1 | RFC1-24.c1 | RFC1-24 | Positive status flows through a challengeable Claim with resolvable support | covered:PWB-REQ-007 |
| RFC1-24.r2 | RFC1-24.c2 | RFC1-24 | Edges or source presence alone cannot create positive status | covered:PWB-REQ-007 |
| RFC2-9.r1 | RFC2-9.c1 | RFC2-9 | A claim cannot leave Unknown without a provenance-verified currency input | covered:PWB-REQ-007 |
| RFC2-10.r1 | RFC2-10.c1 | RFC2-10 | Freshness uses the closed vocabulary, is evaluation-deterministic and remains distinct from label/tier | unknown-uncovered |
| RFC2-24.r1 | RFC2-24.c1 | RFC2-24 | Unknown reasons use the closed twelve, one primary, closed secondaries, distinct routes and complete aggregate disclosure | covered:PWB-REQ-007 |
| RFC2-25.r1 | RFC2-25.c1 | RFC2-25 | Claim tiers retain their closed meanings and stay distinct from labels and sibling states | covered:PWB-REQ-007 |
| RFC6-14.r1 | RFC6-14.c2 | RFC6-14 | Every project claim carries label, tier, primary/secondary reasons and freshness | covered:PWB-REQ-007 |
| RFC6-14.r2 | RFC6-14.c3 | RFC6-14 | Project aggregates carry no headline epistemic status of their own | covered:PWB-REQ-007 |
| RFC6-14.r3 | RFC6-14.c4 | RFC6-14 | Machine answers retain the complete epistemic tuple and never fold Unknown into totals | covered:PWB-REQ-007 |
| RFC6-17.r1 | RFC6-17.c2 | RFC6-17 | Aggregate composition retains label, tier, reason and freshness counts | covered:PWB-REQ-007 |
| RFC6-17.r2 | RFC6-17.c2 | RFC6-17 | Aggregate composition retains the used `unadopted-draft` sibling state | unknown-uncovered |
| RFC6-17.r5 | RFC6-17.c2 | RFC6-17 | Aggregate composition retains challenge state carried by project claims | unknown-uncovered |
| RFC6-17.r6 | RFC6-17.c2 | RFC6-17 | Aggregate composition of reconciliation-chain and work states | believed-not-applicable |
| RFC6-17.r3 | RFC6-17.c3 | RFC6-17 | Primary and secondary Unknown-reason counts remain distinct | covered:PWB-REQ-007 |
| RFC7-16.r1 | RFC7-16.c1 | RFC7-16 | Status is evaluation-bound and carries label, tier, reason and freshness with visible staleness | covered:PWB-REQ-007 |
| RFC7-16.r2 | RFC7-16.c2 | RFC7-16 | Polaris renders no composite maturity, inferred-success headline or metric wall | covered:PWB-REQ-007 |
| RFC7-16.r3 | RFC7-16.c2 | RFC7-16 | Minimal density and drawer/Trajectory handoff for every status | unknown-uncovered |
| RFC7-16.r4 | RFC7-16.c2 | RFC7-16 | Default Polaris status presentation renders no trend or count wall | covered:PWB-REQ-007 |
| RFC7-33.r1 | RFC7-33.c3 | RFC7-33 | Label, tier, reason and freshness travel identically in human and machine views | covered:PWB-REQ-007 |
| RFC7-1.r1 | RFC7-1.c3 | RFC7-1 | Polaris remains a non-authoritative projection | covered:PWB-REQ-014 |
| RFC7-2.r1 | RFC7-2.c1 | RFC7-2 | Every load-bearing narrative claim has exactly one anchored, non-normative or epistemically labeled role | covered:PWB-REQ-014 |
| RFC7-2.r2 | RFC7-2.c2 | RFC7-2 | Framing is explicitly non-normative | covered:PWB-REQ-014 |
| RFC7-2.r3 | RFC7-2.c3 | RFC7-2 | Other project claims are exclusively epistemically labeled | covered:PWB-REQ-014 |
| RFC7-2.r4 | RFC7-2.c4 | RFC7-2 | The claim-role check binds every possible narrative-producing authoring act | unknown-uncovered |
| RFC7-3.r1 | RFC7-3.c1 | RFC7-3 | No project artifact, evidence, snapshot, work warrant or internal relation cites Polaris as authority | covered:PWB-REQ-014 |
| RFC7-3.r2 | RFC7-3.c2 | RFC7-3 | Deleting Polaris presentation changes no truth, status, work, consent or normative fact | covered:PWB-REQ-014 |
| RFC7-5.r1 | RFC7-5.c1 | RFC7-5 | Narrative units retain the complete defined entity classes and ownership | unknown-uncovered |
| RFC7-5.r2 | RFC7-5.c2 | RFC7-5 | Narrative identifiers are opaque and personal view state remains outside truth | unknown-uncovered |
| RFC7-9.r1 | RFC7-9.c1 | RFC7-9 | Every claim's anchor set covers the claim and makes support reader-identifiable | covered:PWB-REQ-014 |
| RFC7-9.r2 | RFC7-9.c2 | RFC7-9 | No claim block carries an unused anchor | covered:PWB-REQ-014 |
| RFC7-9.r3 | RFC7-9.c3 | RFC7-9 | Claim blocks are bounded so attribution remains recoverable | covered:PWB-REQ-014 |
| RFC7-10.r1 | RFC7-10.c1 | RFC7-10 | Anchors use every accepted target class and durable identity rather than labels, paths or coordinates | unknown-uncovered |
| RFC7-10.r2 | RFC7-10.c3 | RFC7-10 | Anchors carry evaluation label/tier/reason and are not rewritten on later reads | covered:PWB-REQ-014 |
| RFC7-12.r1 | RFC7-12.c1 | RFC7-12 | Every claim's owning source is one step away through its anchor | covered:PWB-REQ-014 |
| RFC7-12.r2 | RFC7-12.c2 | RFC7-12 | Operative doctrine, non-goal and requirement text is verbatim | covered:PWB-REQ-015 |
| RFC7-13.r1 | RFC7-13.c2 | RFC7-13 | Every capability narrative reaches a verbatim specification leaf | covered:PWB-REQ-015 |
| RFC7-14.r1 | RFC7-14.c1 | RFC7-14 | Requirement, scenario and doctrine text is byte-verbatim, unreordered and unstored as a normative copy | covered:PWB-REQ-015 |
| RFC7-14.r2 | RFC7-14.c3 | RFC7-14 | Proposal deltas never substitute, ambiguously interleave or become anchorable | covered:PWB-REQ-015 |
| RFC7-15.r1 | RFC7-15.c2 | RFC7-15 | Drafted capabilities remain visibly unadopted | covered:PWB-REQ-015 |
| RFC7-17.r1 | RFC7-17.c1 | RFC7-17 | Every deep-dive block declares exactly one authority band | covered:PWB-REQ-015 |
| RFC7-17.r2 | RFC7-17.c2 | RFC7-17 | Every capability deep dive contains argument, contract and reality bands in order | covered:PWB-REQ-015 |
| RFC7-26.r1 | RFC7-26.c1 | RFC7-26 | Current Base intent remains operative beside proposal material | covered:PWB-REQ-015 |
| RFC7-26.r2 | RFC7-26.c3 | RFC7-26 | Proposal content grants no status or anchor authority | covered:PWB-REQ-015 |
| RFC7-26.r3 | RFC7-26.c3 | RFC7-26 | Proposal scenario context travels with URL, query and selection | unknown-uncovered |
| RFC7-27.r1 | RFC7-27.c1 | RFC7-27 | Competing proposals remain separate candidate futures | covered:PWB-REQ-015 |
| RFC7-29.r1 | RFC7-29.c1 | RFC7-29 | Doctrine, contracts, requirements, capabilities and decisions retain every typed-authority-table consequence | unknown-uncovered |
| RFC7-29.r2 | RFC7-29.c3 | RFC7-29 | Narrative owns composition only and personal state remains outside the model | covered:PWB-REQ-014 |
| RFC7-33.r2 | RFC7-33.c2 | RFC7-33 | Claim type, band class, provenance and proposal state are explicit machine attributes | covered:PWB-REQ-014,PWB-REQ-015 |
| RFC7-33.r3 | RFC7-33.c4 | RFC7-33 | Every narrative unit carries non-citable and presentation-artifact attributes | covered:PWB-REQ-014 |
| RFC7-33.r4 | RFC7-33.c5 | RFC7-33 | Narrative claim-block type remains distinct from kernel Claim | covered:PWB-REQ-014 |
| RFC7-30.r1 | RFC7-30.c5 | RFC7-30 | A release-milestone walkthrough runs nonvisually or keyboard-only and exercises paths | believed-not-applicable |
| RFC7-31.r1 | RFC7-31.c4 | RFC7-31 | The walkthrough record states nonvisual/keyboard-only mode | covered:PWB-REQ-016,PWB-REQ-022 |
| RFC7-31.r2 | RFC7-31.c5 | RFC7-31 | Owner judgment records verdict, rationale, judging party and exact run record | covered:PWB-REQ-022 |
| RFC7-31.r3 | RFC7-31.c7 | RFC7-31 | Invalid owner judgment records verdict-unlawful | covered:PWB-REQ-022 |
| RFC7-32.r1 | RFC7-32.c1 | RFC7-32 | This material narrative change triggers a walkthrough | covered:PWB-REQ-016 |
| RFC7-32.r2 | RFC7-32.c1 | RFC7-32 | Every future material narrative change and release milestone triggers a walkthrough | unknown-uncovered |
| RFC7-32.r3 | RFC7-32.c2 | RFC7-32 | At least one release-milestone walkthrough is nonvisual or keyboard-only | believed-not-applicable |
| RFC7-34.r1 | RFC7-34.c1 | RFC7-34 | Every distinction is recoverable without color, position or layout | covered:PWB-REQ-016 |
| RFC7-34.r2 | RFC7-34.c2 | RFC7-34 | Every disclosure and anchor path is operable without a pointing device | covered:PWB-REQ-016 |

## Verification rule

The effective matrix is the three normalized matrix parts with every base row
named in `Supersedes` removed, plus every repair row above. The coverage checker
must reject duplicate repair IDs, missing superseded IDs, an uncovered accepted
clause, an invalid disposition, or a covered row whose requirement does not
cite the row's clause in its current warrants block.
