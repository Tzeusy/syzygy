Title: Doctrine D6 tree-style restyle — fresh-reader and drift review 1
Verdict: REVISE
Reviewed: NEW-*.md vs OLD-*.md in review-d6/
Reviewer: independent fresh-context agent

Scope: six file pairs. NEW-README.md is byte-identical to OLD-README.md (checked with `cmp`), so five pairs actually changed. The NEW files contain 8 Mermaid diagrams: vision 1, security 1, trust-and-evidence 1, architecture 4, v1 1. I found 4 material and about 20 minor findings.

## Task A

### Restatements from NEW-*.md alone

- **VIS-1.** Truth comes first. The priority order is truth, then comprehension, then momentum, then breadth, then derived-convenience reproducibility. Lower ranks are given up first and truth is never given up. A view may simplify how it presents Unknowns but may never show a confident state in place of one.
- **VIS-2.** Nothing turns green, and nothing is declared aligned, converged or genome-complete, without current evidence. Currency is judged at the evaluation's as-of instant. A claim class with no declared currency bound renders Unknown.
- **VIS-3.** Every normative artifact must pass a fresh-reader review at adoption and on every material amendment. If it fails in the Syzygy repo, every amendment to it needs owner adoption until it passes. Agents may still draft repairs.
- **VIS-4.** Shape-defining changes (doctrine, craft standards, topology, RFC acceptance) always need owner sign-off. Specs could be adopted by an LLM only after both an adjudication RFC and an owner doctrine amendment. Security, privacy, retention and data-contract changes stay human-gated regardless. An author never decides the level of its own change.
- **VIS-5.** Syzygy writes project content directly only in `openspec/**` and `.syzygy/**`. It may read anywhere and uses typed, authorized adapters for other authorities. It may commit proposals but never materialize implementation code.
- **VIS-6.** Every fact must be rebuildable from its owning artifact. There are two exceptions: personal presentation state, and immutable observation records. Promoted notes and dismissals must be committed out to the governed plane.
- **VIS-7.** Syzygy's own releases are blocked by the trust floor: deterministic identity, links that resolve, faithful encodings, and no secrets. It never gates governed projects.
- **SEC-1.** Only loopback may serve without authentication. Even there, browsers need origin/CSRF checks and machine clients need explicit authentication. Anything beyond localhost needs authentication, TLS, and access limited to the owner's own devices.
- **SEC-2.** Project-derived data, including prompts, goes to a service the owner doesn't control only with recorded per-project consent that names the providers and content classes. Without consent the inferred layer renders Unknown.
- **SEC-3.** Observed code runs only in an opt-in, default-deny execution profile. Nothing runs until the profile RFC is accepted.
- **SEC-4.** Writes need per-repository consent and are attributed, atomic and individually revertable. A governance artifact Syzygy did not author is never overwritten without surfacing the conflict.
- **SEC-5.** Content that matches the secret-detection policy, or that cannot be classified, is excluded, and the exclusion is rendered. A reproduced secret breaks the trust floor.

### Form judgment

Most openings summarize their sections correctly. For most rules, cutting down to the lead-in plus the first sentence still gives a correct, coarser rule. **VIS-5 does not.** Its first sentence says Syzygy "reaches everything else through authorized adapters". That drops "typed" and "only", and it contradicts the next bullet ("Reading is unrestricted").

Openings that overstate, understate or misstate their section:

1. **security.md intro:** "Syzygy treats every client, every outside service, and all observed code as untrusted until proven otherwise". SEC-3 says observed code is untrusted "everywhere" and "whoever owns the project", with no way to prove it trustworthy. "Until proven otherwise" invents one. This misstates the section and is **material** (see B5).
2. **VIS-5 opening:** as above (see B2).
3. **trust-and-evidence.md intro:** "inference may question a claim but never establish one". This overstates. The text limits it to *status*: "Inference has no authority to establish a status". Inferred narrative claims are legitimate.
4. **Trust floor opening:** "so four properties block every Syzygy release". Read literally, releases are always blocked. The intended sense is that breaking any of the four blocks a release.
5. **Staleness opening:** "always visibly stale and never green". The body says "cannot *silently* stay green". This strengthens the rule slightly.
6. **Typed authority opening:** "a conflict between homes is surfaced to the owner". This understates. The body says contradictions arise "from different typed authorities or from one", and that they render Unknown.
7. **Snapshots opening:** "the same inputs always give the same answer". Determinism is asserted over the deterministic layer only, and the inferred layer is excluded. This overstates slightly.
8. **What Syzygy is:** "always a plane beside the code rather than inside it". This conflicts with the **in-tree** plane in architecture.md. OLD said "live alongside each governed project".
9. **v1.md opening:** "proves the loop works end to end". The body says one minimal slice per axis, which is narrower.
10. **Platform opening:** "A local-first, single-owner tool". This presents local-first as settled, but the body says "(the current shape; open to RFC)".
11. **v1 "Three conditions frame every V0 claim".** "Trust floor" and "Proving ground" are not conditions on V0 claims. This is new framing.
12. **Status vs narrative opening:** "everything else carries exactly one of three labels". Policy dismissal is a third category, handled by a human-decision warrant. This is a minor understatement.

## Task B

### Material findings

**B1. vision.md, VIS-4: the subject of the adoption ban is narrowed.**
- OLD: "Syzygy and its agents may draft them, never adopt them."
- NEW: "agents may draft them, never adopt them."
- Why it matters: Syzygy itself is no longer named in the prohibition, so the scope is narrowed.
- Fix: restore "Syzygy and its agents".

**B2. vision.md, VIS-5: exclusivity is lost and the verb changes.**
- OLD: "Everything else … Syzygy affects only through **typed, explicitly authorized adapters**"
- NEW opening: "reaches everything else through authorized adapters"
- NEW bullet: "Every other authority is reached through typed, explicitly authorized adapters"
- Why it matters: "only" is dropped, which weakens exclusivity. "Affects" becomes "reached", which also covers reads and so contradicts "Reading is unrestricted". NEW-architecture.md still says "affects only through", so the two files now disagree.
- Fix: "affects everything else only through typed, explicitly authorized adapters" in both places.

**B3. architecture.md, plane diagram: the consent label implies the governance root needs none.**
- Diagram: `K -.->|"reads"| CODE` alongside `K -.->|"reads, with consent"| SRC`.
- Text: "**Every observed repository consents, governance root or not.**"
- Why it matters: putting "with consent" on the observed-source edge only implies that reading the root's code needs no consent. The text says the opposite. The direct-write edges are also consent-gated (SEC-4).
- Fix: drop "with consent" from the SRC edge. Alternatively, add a note that every edge is consent-gated.

**B4. security.md intro: "until proven otherwise".**
- OLD SEC-3: "It is untrusted whoever owns the project."
- NEW intro: "untrusted until proven otherwise"
- Why it matters: it adds a trust-earning path that doctrine does not have. It also asserts a trust posture toward "every outside service" that no rule states; SEC-2 is about consent, not trust.
- Fix: "treats observed code as untrusted everywhere, admits clients only as SEC-1 allows, sends data out only with scoped consent, and makes only consented, revertable writes".

### Minor findings

**B5. vision.md, Success: a qualifier is lost.**
- OLD: "no single quantitative metric is constitutional"
- NEW: "No single metric is constitutional"
- This broadens the ruling. Fix: restore "quantitative".

**B6. vision.md, live fleet: exclusivity is lost.**
- OLD: "It is deferred only because live monitoring means nothing…"
- NEW: "**Why it waits:** live monitoring means nothing…"
- Fix: "It waits only because…"

**B7. vision.md, Thesis: the portfolio framing is lost.**
- OLD: "control plane for a portfolio of software projects. It makes each project's vision → spec → code hierarchy…"
- NEW: "makes a portfolio's vision → spec → code hierarchy"
- The per-project hierarchy is lost. Fix: "for a portfolio of software projects, making each project's…"

**B8. vision.md, VIS-4: mis-nesting.**
- NEW nests "RFC acceptance alone never opens it." as a third sibling under "needing both:". It reads as a third condition.
- Fix: dedent it to sit beside the "needing both" bullet.

**B9. vision.md, VIS-2: a qualifier is detached.**
- "Aligned, converged, and genome-complete are defined in architecture.md." is nested under the **Evidence** bullet. In OLD it qualified the declaration clause.
- Fix: move it under the opening sentence.

**B10. vision.md, "What Syzygy is".** The opening is covered in Task A item 8. "A witness first, a harness second" also adds a ranking OLD did not state. Fix: "alongside each governed project, reaching its code only through scheduled work".

**B11. security.md, SEC-2 first sentence: "store" is dropped.**
- OLD: "never sent to a store or service the owner does not control without explicit, recorded…"
- NEW: "reaches a service … without recorded, per-project consent"
- "store" and "explicit" are dropped. The lead-in still covers them, which is why this is minor. Fix: restore "store or service" and "explicit".

**B12. security.md, SEC-1: a scope change.**
- NEW nests the CSRF and machine-auth bullets under "**On loopback:**". In OLD they sit under "even there client classes are told apart". The CSRF bullet's own "including on loopback" shows it is not loopback-only.
- The opening also generalizes: "where a client connects from never proves who it is" versus OLD "Loopback location alone never proves a client's identity".
- Fix: heading "Client classes, told apart even on loopback:".

**B13. security.md, SEC-5 opening: a slight strengthening.**
- NEW: "Anything that matches … or cannot be classified, is excluded, and the exclusion is shown"
- OLD rendered the exclusion only for matching content.
- Fix: "…is excluded; a matching exclusion is rendered", or accept the change explicitly.

**B14. trust-and-evidence.md, openings.** Task A items 3, 4, 5 and 12 (inference "never establish one"; "four properties block every Syzygy release"; "never green"; "everything else"). Suggested wording:
- "never establish a status"
- "Any release that breaks one of four properties is blocked"
- "never silently green"

**B15. architecture.md, openings.** Task A items 6 and 7. The typed-authority opening also asserts "exactly one authoritative home", which OLD does not say in those words.
- Fix: "Authority is typed by question; a contradiction — across homes or within one — renders Unknown and goes to the owner."

**B16. v1.md, openings.** Task A items 9, 10 and 11.

### Diagram audit

**D1. vision.md thesis diagram.**
- `E -. "never proof of intent" .-> G` draws an arrow from execution state into the difference computation. An arrow reads as an input, and the label contradicts it. Minor. Fix: remove the edge and state it in a note.
- `G -->|"human-triggered work"| A` is acceptable.
- "Difference computed and shown" is unlabelled as V1. At V0 there are only absences (v1.md). Minor.

**D2. security.md SEC-1 diagram.** Consistent with the text. No finding.

**D3. trust-and-evidence.md label tree.**
- The root `C["A claim"]` applies the Observed / Inferred / Unknown tree to every claim. Under it, a *status* claim could land on "Inferred", which contradicts "Inferred evidence never establishes, raises, or independently satisfies a positive status claim". Minor.
- Fix: root node "A narrative or exploratory claim".

**D4. architecture.md plane diagram.** See B3 (material). The other edges are consistent.

**D5. architecture.md snapshot diagram.**
- `IL -. "may challenge, never establish" .-> OR` aims the inferred layer at the observation record.
- The text has inference suspending a displayed *claim*. The record is immutable and holds deterministic facts only.
- Minor. Fix: target a "Displayed status claim" node.

**D6. architecture.md loop diagram.**
- The upward edge originates only from `V`. The text says "verification and runtime evidence may open spec-indictment gaps". Minor.
- Fix: label it "verification or runtime evidence: spec-indictment gap, to the owner".

**D7. architecture.md kernel diagram.** Consistent with the text. No finding.

**D8. v1.md stage diagram.**
- `V1 -.-> L["Deferred …"]` sequences every deferred item after V1.
- The text dates only certificates as "post-V1". Autonomous spec adoption opens by act at any time, and regeneration is "not scope".
- Minor. Fix: detach the Deferred node, or drop the edge.

### No drift found

VIS-1, VIS-3, VIS-6 and VIS-7 bodies; Performance; North star; SEC-3 and SEC-4 bodies; the Evidence, Seam and Staleness bodies; the Genome, Definitions, Snapshot and Vocabulary bodies; the V0 and V1 lists; the deferred and success tables. README is unchanged.
