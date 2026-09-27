Title: Doctrine D5 readability rewrite — fresh-reader and drift review 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: NEW-*.md vs OLD-*.md in review-in/
Reviewer: independent fresh-context agent

## Task A

I read only the NEW-*.md files for this task. I opened no OLD file until Task A was complete.

### Restatements

- **VIS-1 (comprehensible truth first).** Five priorities are ranked: truth and determinism, then comprehension, then momentum, then breadth and fidelity, then reproducibility of derived conveniences. Lower ranks are given up before higher ones, and truth is never given up. Views may simplify how Unknowns are presented (aggregate them, defer them, disclose them progressively). They may never show a confident state where the real state is Unknown.
- **VIS-2 (no evidence means Unknown).** Nothing may be shown as aligned, converged, genome-complete or green without current evidence. Evidence must be a durable, identified, integrity-verifiable artifact. Currency is judged at an evaluation's identified as-of instant, never by the wall clock. A claim class that declares no currency bound always renders Unknown.
- **VIS-3 (human interpretability).** Every normative artifact must stay understandable to a newcomer. This is tested by a fresh-reader review at adoption and on every material amendment, and a failure is recorded on the artifact. In the Syzygy repo a failure means only the owner may adopt amendments, though agents may still draft them, until the artifact passes. In governed projects the failure is shown as status, and each project decides whether to freeze.
- **VIS-4 (humans steer, agents shape).** Doctrine, craft-and-care standards, topology and RFC acceptance always need owner sign-off; agents may draft them but never adopt them. Autonomous adoption of behavioral specs is possible only after two things: an accepted adjudication RFC and an explicit owner doctrine amendment opening the gate. Even then, spec changes touching security, privacy or retention, or normative data contracts stay human-gated. The agent making a change never classifies it as spec-level or shape-level.
- **VIS-5 (never writes code; two write namespaces).** Syzygy writes project content directly only in `openspec/**` (in OpenSpec-compatible form) and `.syzygy/**`, and nothing may widen that set. It reaches VCS, the scheduler, CI and runtime only through typed, explicitly authorized adapters. It may commit code-shaped proposals as artifacts into `.syzygy/**`, but never apply them to implementation code or branches. Only workers doing scheduled work materialize code.
- **VIS-6 (derived, two closed exceptions).** Every fact must be rebuildable from the artifact that owns it, and authored content is committed out to the governed plane. There are only two exceptions. The first is owner presentation state, which may never affect truth, work, status or certificates; a promoted note or dismissal is committed with attribution, a reason and an expiry. The second is immutable observation records.
- **VIS-7 (trustworthy observatory).** Four floor properties block Syzygy's own releases:
  - the deterministic layer is identical across runs of one evaluation;
  - internal links resolve;
  - encodings match their legends;
  - no secrets appear anywhere.
  The floor never gates a governed project's releases.
- **SEC-1 (authenticated by default).** Only loopback may serve without authentication. Even on loopback, browsers need origin/CSRF protection and machine clients need explicit authentication; loopback location never proves identity. Anything beyond localhost needs authenticated TLS limited to the owner's devices.
- **SEC-2 (consented egress).** Project content, including derivatives and prompts, goes to any non-owner-controlled service only with explicit, recorded, per-project consent. That consent names the permitted providers and content classes. Model providers count as such services. Without consent, the inferred layer renders Unknown.
- **SEC-3 (observed code untrusted).** Observed code runs only in an opt-in, default-deny, isolated execution profile, whoever owns the project. None runs until the profile RFC is accepted.
- **SEC-4 (consented, attributed, revertable writes).** Writes need per-repository consent. Each write must be attributed, atomic and individually revertable. Syzygy never overwrites a governance artifact it did not author without surfacing the conflict.
- **SEC-5 (secrets never indexed).** A declared secret-detection policy excludes matching content and renders the exclusion. Content that cannot be classified is also excluded (fails closed). A leaked secret breaks the trust floor.

### Unclear or hard to follow as a first-time reader

1. **VIS-4 classification.** The sentence is "It is settled without a human only while an opened gate is in force." It does not say who or what settles it: the adjudication RFC's mechanism? a non-authoring agent? It also gives no criteria for what makes a change "spec-level" versus "shape-level".
2. **VIS-1's "spent" and "rank 1 is never spent".** The spending metaphor is never explained. It is also unclear whether rank 2 may ever be spent, since Performance says "never below the comprehension constraint".
3. **VIS-3.** "A failure is recorded on the artifact's surface": which surface (Polaris? the file itself?) is unstated.
4. **VIS-5.** "VIS-6's commit-out, through the version-control adapter" is jargon at the point of use. "Commit-out" is only implicitly defined in VIS-6.
5. **VIS-6(b).** "marked stale" reads as though observation records are always stale. The intended meaning is presumably "marked stale once superseded", as trust-and-evidence.md says.
6. **VIS-2.** "Currency bound" appears here but is defined only in trust-and-evidence.md.
7. **Actuator glossary vs. VIS-5.**
   - An actuator includes "a human working by hand", but VIS-5 says "materialization is only ever a worker acting on scheduled work". It is unclear whether a human counts as a "worker".
   - The citation "(VIS-5, VIS-6)" for "writes no implementation code" is odd, because VIS-6 is about derivation, not code writes.
8. **"Public" toolchain.**
   - vision.md says Syzygy "assumes the public actuator toolchain". The glossary defines that toolchain as including the claude/codex CLIs, so in what sense is all of it public?
   - v1.md says "the designated initial substrate is the public ai-bootstrap toolchain" (singular), while the README defines ai-bootstrap as only the `/th-*` skills and lists OpenSpec and Beads as further substrates.
9. **SEC-1.** A missing `Origin` header is "neither trusted automatically nor treated as a browser-origin violation", but what happens instead is not stated, not even as "RFC matter".
10. **SEC-4.** What "atomic" means for a multi-file first-pass draft is unclear.

## Task B

No rule's core requirement, permission or prohibition changed materially. All findings are minor: modal verbs softened, qualifiers dropped, or scope narrowed. The deliberate additions (actuator glossary bullet, ai-bootstrap sentence) and the removal of the amendment log were excluded as drift. Interaction notes on them are at the end.

### B1. NEW-README.md, Glossary: rule identifiers (minor, added constraint)
- OLD: "Identifiers are stable after adoption: amend text in place; retire rather than renumber."
- NEW: "Identifiers are stable: text is amended in place, and a retired number is never reused."
- Why it differs: NEW adds a rule OLD did not state (a retired number is never reused). It also drops the explicit "retire rather than renumber" instruction, leaving it implied by "stable". "After adoption" is lost too.
- Fix: "Identifiers are stable after adoption: text is amended in place, and a rule is retired rather than renumbered." Keep the no-reuse clause only if the owner intends it.

### B2. NEW-README.md, Scope boundary (minor, obligation weakened)
- OLD: "downstream artifacts must be re-checked for alignment when it changes."
- NEW: "downstream artifacts are re-checked for alignment when it changes."
- Why it differs: an obligation became a description.
- Fix: "and downstream artifacts must be re-checked for alignment when it changes."

### B3. NEW-vision.md, VIS-3 (minor, qualifier lost)
- OLD: "every amendment to the failing artifact requires owner adoption until it passes a fresh-reader review."
- NEW: "every amendment requires owner adoption until the artifact passes a fresh-reader review."
- Why it differs: "every amendment" no longer names its scope, so it can be read as all amendments anywhere in the repo.
- Fix: "every amendment to that artifact requires owner adoption until it passes a fresh-reader review."

### B4. NEW-vision.md VIS-5 and NEW-architecture.md, two-namespace plane (minor, qualifier "directly" dropped)
- OLD (vision): "it may never directly create, modify, move, or delete project content outside its two roots."
- OLD (architecture): "it may never directly create, modify, move, or delete project content outside its two roots."
- NEW (vision): "may never create, modify, move, or delete project content outside those two roots."
- NEW (architecture): "may never create, modify, move, or delete project content outside its two roots."
- Why it differs: without "directly" the ban reads as absolute. That sits awkwardly beside the adapter path and dispatched worker materialization, both of which cause out-of-root changes Syzygy set in motion. OLD scoped the ban to direct writes, which matches the heading "direct writes are confined".
- Fix: restore "directly" in both places.

### B5. NEW-security.md, SEC-2 (minor, obligation weakened)
- OLD: "Onboarding consent must name the providers permitted for a governed project and the content classes that may be sent"
- NEW: "Onboarding consent names the providers permitted for the project and the content classes they may receive"
- Why it differs: a requirement on what consent must contain became a description of what it contains.
- Fix: "Onboarding consent must name the providers permitted for the project and the content classes they may receive; Syzygy renders that consent on the project's surface."

### B6. NEW-trust-and-evidence.md, deterministic/inferred seam (minor, scope narrowed)
- OLD: "An inference never silently overrides or replaces deterministic evidence: the suspended claim's deterministic basis stays visible, and resolving the challenge is what restores or revises the status."
- NEW: "The suspended claim's deterministic basis stays visible; inference never silently overrides or replaces it."
- Why it differs: OLD states a general prohibition covering all deterministic evidence. In NEW, "it" binds to "the suspended claim's deterministic basis", so the prohibition covers only the challenge/suspension case.
- Fix: "Inference never silently overrides or replaces deterministic evidence: the suspended claim's deterministic basis stays visible. Resolving the challenge is what restores or revises the status."

### B7. NEW-vision.md, "Not a documentation portal" (minor, framing strengthened)
- OLD: "Rendering and drafting governance artifacts is a means; the escape property is that intent changes produce dispatched work."
- NEW: "Rendering and drafting governance artifacts is a means. Intent changes must produce dispatched work;"
- Why it differs: OLD names a product-level escape property. NEW reads as a mandate that every intent change must yield dispatched work. That is stronger, and it sits uneasily with the human-triggered loop, where a tuned intent may legitimately wait for a deliberate propagate pass.
- Fix: "Rendering and drafting governance artifacts is a means; what sets Syzygy apart is that intent changes produce dispatched work."

### B8. NEW-vision.md, Thesis (minor, agency shifted)
- OLD: "Syzygy computes and shows the difference, and harnesses the existing actuator toolchain to close it."
- NEW: "Syzygy computes the difference between desired and observed state, shows it, and drives the existing actuator toolchain to close it."
- Why it differs: "drives" suggests Syzygy initiates the closing work, which is in tension with "Not autonomous" and the human-triggered loop. "Harnesses" is also the verb the NEW glossary itself uses ("harnesses rather than replaces").
- Fix: "…shows it, and harnesses the existing actuator toolchain to close it."

### Interaction notes on the deliberate additions

These are not drift, but they affect consistency.

- **N1.** NEW-README defines ai-bootstrap as the `/th-*` skills only ("The skills are published as the public ai-bootstrap toolchain that v1.md names as the initial substrate"). NEW-v1 says "the designated initial substrate is the public ai-bootstrap toolchain", singular, while the glossary lists OpenSpec, Beads, and skills plus CLIs as substrates. A reader can no longer tell whether v1's "substrate" means the actuator substrate only.
  - Suggested fix in v1: "the designated initial actuator substrate is the public ai-bootstrap toolchain".
- **N2.** The actuator bullet counts "a human working by hand" as an actuator. VIS-5 says materialization is "only ever a worker acting on scheduled work". It needs to be clear that a human actuator is a "worker" in VIS-5's sense, or the two read as conflicting.
- **N3.** The actuator bullet cites "(VIS-5, VIS-6)" for "writes no implementation code". VIS-6 does not govern code writes. Consider citing VIS-5 alone.

I checked every other section in all six files: SEC-1, SEC-3, SEC-4, SEC-5, VIS-1, VIS-2, VIS-4, VIS-6 and VIS-7, Performance, North star, Fleet mandate, Success, v1 scope/deferrals/success table, and the architecture Genome, definitions, snapshots, loop, idempotence, surfaces and vocabulary. They preserve meaning; the differences are wording and structure only.
