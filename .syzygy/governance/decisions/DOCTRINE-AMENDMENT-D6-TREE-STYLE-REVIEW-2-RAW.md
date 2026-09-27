Title: Doctrine D6 tree-style restyle — confirmation review 2
Verdict: REVISE
Reviewed: NEW-*.md vs OLD-*.md in review-d6b/, against REVIEW-1-RAW.md
Reviewer: independent fresh-context agent

Scope: I read all six OLD/NEW pairs in full, including all 9 Mermaid diagrams in NEW (vision 1, security 1, trust-and-evidence 1, architecture 4, v1 1). `NEW-README.md` is byte-identical to `OLD-README.md`, checked with `cmp` this session. I edited nothing.

## Part 1 — Status of the REVIEW-1 findings

### Task A items

| # | Status | Current NEW text |
|---|---|---|
| 1 | RESOLVED | security intro: "Syzygy treats observed code as untrusted everywhere, admits clients only as SEC-1 allows, sends data out only with scoped consent, keeps secrets out, and makes only consented, revertable writes." |
| 2 | RESOLVED | VIS-5: "affects everything else only through typed, explicitly authorized adapters, and never materializes implementation code." |
| 3 | RESOLVED | "inference may challenge a status but never establish one" |
| 4 | RESOLVED | "so a Syzygy release that breaks any of four properties is blocked." |
| 5 | RESOLVED | "always visibly stale and never silently green." |
| 6 | RESOLVED | "a contradiction — across authorities or within one — renders Unknown and goes to the owner, never settled silently." |
| 7 | RESOLVED | "so the deterministic layer always gives the same answer for the same inputs" |
| 8 | RESOLVED | "A witness, a harness, and a governance plane that lives alongside each governed project and reaches its code only through scheduled work." |
| 9 | RESOLVED | "V0 is an honest observatory with one working slice of the loop on each axis" |
| 10 | RESOLVED | "Currently a local-first tool (open to RFC)" |
| 11 | PARTIAL | "Three further points bound what V0 may claim:". The Trust floor point is a release block, not a limit on what V0 may claim, so the framing is still new (see N7). |
| 12 | RESOLVED | "Anything that does a status claim's work needs evidence, whatever it looks like; a gap may also be dismissed by recorded human decision; narrative claims carry exactly one of three labels." |

### B findings

- **B1 — RESOLVED.** "Syzygy and its agents may draft them, never adopt them."
- **B2 — RESOLVED.** Both files now read "affects … only through typed, explicitly authorized adapters":
  - vision lines 194 and 206–207;
  - architecture lines 38–40.
- **B3 — RESOLVED as asked.** The edges now read `K -.->|"reads"| CODE` and `K -.->|"reads"| SRC`, and a caption says "Every edge from Syzygy is gated: each observed repository, governance root included, has consented (SEC-4)". The caption now contradicts the same file's "Reading is unrestricted" (see N1).
- **B4 — RESOLVED.** Same text as item 1.
- **B5 — RESOLVED.** "**No single quantitative metric is constitutional**, by explicit owner ruling".
- **B6 — RESOLVED.** "It waits only because live monitoring means nothing…". The line reads "**Why it waits:** it waits only because…", which duplicates the phrase. That is editorial only.
- **B7 — RESOLVED.** "control plane for a portfolio of software projects, making each project's vision → spec → code hierarchy…"
- **B8 — RESOLVED.** "**RFC acceptance alone never opens it.**" is now a top-level sibling bullet.
- **B9 — RESOLVED.** "no project is declared aligned, converged, or genome-complete (defined in architecture.md), without current evidence."
- **B10 — RESOLVED.** Same text as item 8. The "witness first" ranking is gone.
- **B11 — RESOLVED.** "sent to a store or service the owner does not control — model providers included — without explicit, recorded, per-project consent."
- **B12 — RESOLVED.** Both parts are fixed:
  - The bullets sit under "**Client classes, told apart even on loopback:**".
  - The opening now reads "loopback location alone never proves a client's identity."
- **B13 — RESOLVED.** "Anything that matches the declared secret-detection policy, or cannot be classified, is excluded; a matching exclusion is rendered."
- **B14 — RESOLVED.** See items 3, 4, 5 and 12.
- **B15 — RESOLVED.** See items 6 and 7. The "exactly one authoritative home" wording is gone.
- **B16 — PARTIAL.** Items 9 and 10 are resolved; item 11 is only partly resolved.

### D findings (diagrams)

- **D1 — RESOLVED.** The "never proof" edge is removed, and the caption reads "execution state feeds nothing back into the difference". The node reads `"Difference, shown<br/>(absences at V0, gaps at V1)"`, which v1.md's V0/V1 boundary supports.
- **D2 — no finding before, none now.**
- **D3 — RESOLVED.** `C["A narrative or exploratory claim"]`
- **D4 — RESOLVED.** Same as B3.
- **D5 — RESOLVED.** `IL -. "may challenge, never establish" .-> SC`, where `SC["Displayed status claim"]`.
- **D6 — RESOLVED.** `V -. "verification or runtime evidence:<br/>spec-indictment gap, to the owner" .-> I`
- **D7 — no finding before, none now.** The new kernel diagram is also consistent with the text.
- **D8 — RESOLVED.** The `L["Deferred…"]` node now has no edges.

## Part 2 — Fresh drift audit, NEW vs OLD

### Material

**N1. vision.md line 202 and architecture.md line 34: "Reading is unrestricted".**
- OLD, in both files: "Syzygy may *read* declared implementation and evidence sources anywhere (in the project)"; architecture adds "Every observed repository consents, governance root or not."
- NEW heading, in both files: "**Reading is unrestricted; direct writing is not.**"
- Why it matters:
  - OLD limits reading to *declared* sources in consented repositories. "Anywhere" is about location, not permission.
  - The bold heading drops both limits, so reading only the headings gives a wrong rule rather than a coarser one.
  - It now contradicts architecture.md's own caption, which says every read is gated: "Every edge from Syzygy is gated: each observed repository … has consented".
  - This wording was already in the version REVIEW-1 saw, and REVIEW-1 did not flag it. Fixing B3 made the contradiction explicit.
- Fix, in both files: "**Reading reaches declared sources anywhere in the project; direct writing is confined to two roots.**"

### Minor

**N2. vision.md, "The human problem" opening.**
- OLD: "an owner running a portfolio of projects built largely by agent fleets."
- NEW: "…built largely by agent fleets, who cannot tell what those fleets have done."
- Why: it defines the primary user by one of the four listed failures.
- Fix: drop the relative clause, or say "…and who suffers the failures below."

**N3. vision.md, "What Syzygy is not" opening.**
- OLD: "Not an issue tracker with a code browser"; "Not a replacement for its substrate".
- NEW: "Syzygy is not a tracker, a portal, a replacement, an outward enforcer, or an autonomous agent."
- Why: "not a tracker" and "not a replacement" drop their qualifiers. Syzygy does show work state, and it replaces the README ritual.
- Fix: "not merely an issue tracker with a code browser, not a documentation portal, not a replacement for its substrate, not an outward enforcer, and not autonomous."

**N4. security.md, SEC-2 opening.**
- OLD: "Governed-project content — source structure, specs, work history, and anything derived from them, including prompts — is never sent…"
- NEW: "Nothing derived from a governed project is sent…"
- Why: the opening moves the scope off the enumerated content. A "What is covered" bullet restores it, which is why this is minor.
- Fix: "No governed-project content, or anything derived from it, is sent…"

**N5. security.md, SEC-3: a qualifier has moved.**
- OLD: "It is untrusted whoever owns the project."
- NEW: "Observed-project code runs only inside an explicit, opt-in execution profile, whoever owns the project."
- Why: "whoever owns the project" now qualifies the run rule instead of the trust status. The explicit untrusted-whoever-owns sentence is gone; only the heading keeps "untrusted, everywhere".
- Fix: add the bullet "**It is untrusted whoever owns the project.**"

**N6. architecture.md, "One kernel, three surfaces" opening.**
- OLD: "The kernel's shared semantics … must never fork across surfaces, and no surface is independently authoritative"; "There is no single universal source of truth."
- NEW: "One shared kernel computes every truth, and the three surfaces are only views of it."
- Why: "computes every truth" goes beyond OLD and conflicts with typed authority. Code, the scheduler and git are authorities that the kernel does not compute.
- Fix: "One shared kernel holds the semantics every surface uses, and the three surfaces are only projections of it."

**N7. v1.md, the lead-in line.**
- OLD: three standalone paragraphs: Increments, Trust floor, Proving ground.
- NEW: "Three further points bound what V0 may claim:"
- Why: the Trust floor point blocks releases; it does not limit claims. This is REVIEW-1 item 11, carried over.
- Fix: "Three further points apply to V0:"

**N8. v1.md, V0 opening.**
- OLD: "V0 observes **whatever Project Genome artifacts and evidence exist** … and code structure".
- NEW: "V0 shows whatever each governed project has declared and evidenced".
- Why: code structure and work state are observed, not "declared and evidenced". The bullet below restores the OLD list.
- Fix: "V0 shows whatever Genome artifacts and evidence each governed project has".

### No drift found

- **Diagrams:** vision thesis, SEC-1, the claim-label tree, the plane diagram apart from N1, snapshot, loop, kernel, and the v1 stage diagram.
- **vision.md:** the VIS-1 to VIS-7 bodies, Performance, North star, Live fleet and Success. The VIS-4 "Always human-gated, gate open or not" matches OLD "Even with the gate open … stay human-gated".
- **security.md:** the SEC-1, SEC-4 and SEC-5 bodies.
- **trust-and-evidence.md:** all bodies.
- **architecture.md:** the Typed authority, Genome, Definitions, Snapshot and Vocabulary bodies.
- **v1.md:** the V1, Deferred, Platform and Success bodies. The Success opening's "owner judgment" matches vision.md: "the owner re-judges them at each stage gate".

## Summary

All REVIEW-1 findings are resolved except item 11 and B16, which are partial. The verdict is REVISE because of one material item, N1: "Reading is unrestricted" states a rule OLD does not have, and after the B3 repair it contradicts its own file. The seven minor items N2–N8 are wording in section openings and one moved qualifier (N5). Fixing N1 and N7 would bring this to CONFIRM WITH EXCEPTIONS at worst.

Files reviewed are in `/tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/review-d6b/`: `NEW-vision.md`, `NEW-architecture.md`, `NEW-security.md`, `NEW-v1.md`, `NEW-trust-and-evidence.md`, and `REVIEW-1-RAW.md`.
