Title: Polaris tree-form amendment — review 1
Verdict: REVISE
Reviewed: SPEC-DIFF.patch and PACKET.md in review-pg1/
Reviewer: independent fresh-context agent

## Material

**M1. A "no-diagram disposition" can clear an obligation that REQ-004 already treats as unmet.**
- Quotes:
  - Clause: "SHALL have a supported diagram or an explicit disposition naming why it has none"
  - Scenario 2, which covers a diagram whose premises support every edge: "or the relationship takes an explicit no-diagram disposition"
- Problem:
  - REQ-004 allows three dispositions: "produced, reasoned-omission or unresolved".
  - *Required visual unavailable* says a missing renderer, authorization or support leaves the readiness criterion unmet.
  - The new clause does not say which of the three dispositions a "no-diagram disposition" is, or which reasons are allowed. A generator could write "reasoned omission: renderer unavailable" and satisfy the new clause while dodging that scenario.
  - The clause also never says whether each per-relationship diagram is a requested asset with its own identity and requiredness, which REQ-007 and *Two requested diagrams have different obligations* require.
  - Scenario 2's WHEN is the fully supported case. Its AND then allows a no-diagram disposition with no condition, so the scenario cannot fail when the diagram is simply left out. It is not falsifiable.
- Fix:
  - State that each explained relationship's diagram is a requested asset under REQ-007, with its own identity and requiredness, resolved to one of the existing three dispositions.
  - Allow a reasoned omission only when prose explains the relationship at least as clearly, or when premises do not support it. That judgment is recorded for the independent design review.
  - Missing support from the renderer or from permission is always unresolved, never a reasoned omission.
  - Rewrite Scenario 2 so the supported case requires the diagram, and move the no-diagram case into its own WHEN.

**M2. The clause asks for more than CC-REV-8 and drops "useful", which works like a quota.**
- Quotes:
  - New clause: "Every structural relationship the presentation explains — composition, dependency, flow, lifecycle or decision — SHALL have a supported diagram or an explicit disposition"
  - CC-REV-8: "**Diagrams wherever structure beats prose.** Flows, lifecycles, state machines, boundaries, dependencies, and placements get a diagram"
  - Existing REQ-004: "relationship assets where supported and useful"
- Problem:
  - CC-REV-8 is conditional on structure beating prose. The amendment is unconditional: every explained relationship, even one a single sentence covers, needs a diagram or a disposition record.
  - That is a per-relationship quota of figures or paperwork. It pulls against "where supported and useful" and against *Meaningful visual instead of decorative quota*.
  - The list of relationship kinds also differs from CC-REV-8. It adds "composition" and "decision", and drops state machines, boundaries and placements. "Decision" is not a structural relationship in CC-REV-8's sense.
- Fix: "Where a diagram would explain a structural relationship the presentation explains (flow, lifecycle, state machine, boundary, dependency or placement) better than prose (CC-REV-8), it SHALL have a supported diagram or a disposition under [M1]; coverage is judged per such relationship, never by figure count."

**M3. It is not said who decides which relationships are "explained", so the generator sets its own coverage count.**
- Quote: "coverage is judged per explained relationship"
- Problem:
  - Nothing says who lists the explained relationships. If the author does, it narrows its own count by describing fewer relationships, which breaks REQ-006: "The candidate-authoring stage SHALL NOT define or narrow its own review denominator."
  - As written, coverage cannot be observed independently.
- Fix:
  - Say that the independent design or fidelity review lists the structural relationships the rendered account explains, and judges coverage against that list.
  - Alternatively, list them in the editorial plan, which already records "reasons for diagram … selection", with that list independently reviewed.
  - Add a scenario in which a relationship explained in prose but missing from the author's list is a finding.

**M4. PACKET.md's claim about PWB-REQ-006 is not established, and may be false for SVG.**
- Quotes:
  - PACKET: "PWB-REQ-006 still forbids active content on the page, and the inert-rendering clause keeps diagrams within it"
  - PACKET, renderer section: "Mermaid renders to SVG on the server"
  - PWB-REQ-006: "SHALL NOT … emit active HTML, SVG, scripts, event handlers or unsafe URL schemes"
- Problem:
  - "SVG" sits in a list of active-content classes. It can fairly be read as a ban on emitting any SVG, not only active SVG. PWB-REQ-006 also treats SVG outside a code context as grounds to exclude a source.
  - If generated diagrams ever reach `/polaris`, emitting sanitized SVG may need a ruling on how PWB-REQ-006 reads, or an amendment. A spec amendment is an escalation trigger, not something this packet can assert away.
  - The spec clause itself names no format, so the conflict lives in the packet's implementation plan and its "stays fixed" claim.
- Fix:
  - Either state that this packet emits nothing on `/polaris`, since the Butlers page package is out of scope, and that PWB-REQ-006's position on sanitized SVG is left to that later package's owner act.
  - Or choose an inert output that PWB-REQ-006 plainly allows, such as HTML/CSS boxes with no SVG.
  - Remove "keeps diagrams within it" unless one of these is done.

**M5. The precedence list for tree form leaves out verbatim exact-source text.**
- Quote: "where required headings, the altitude order or authority bands fix structure, they take precedence"
- Problem:
  - The verbatim specification leaf altitude, and contract-band text linked to its owner, must stay verbatim under REQ-012: "Exact normative leaves SHALL retain their owning identity and verbatim text". Such text cannot be restructured into an abstraction tree, and truncating it at a nesting depth is not a "true coarser account".
  - CC-REV-8 itself has "Format requirements win" and "Normative text keeps its qualifiers attached".
- Fix: add "verbatim exact-source text and quoted owning artifacts" to the precedence list, and state that tree form governs the generated prose around them.

## Minor

**m1. Scenario 1 is stricter than its clause and than CC-REV-8.**
- Scenario: "opens with a one-sentence answer"
- Clause: "opens with its answer"
- CC-REV-8: "one sentence or one bullet"
- Fix: use "opens with its answer in one sentence or one bullet" in both places.

**m2. Scenario 2 mixes two cases.**
- Its WHEN says "admitted premises support each dependency", but its AND handles "an unsupported edge".
- Fix: split it into a supported case and a partly supported case.

**m3. No new scenario tests that an element's epistemic class stays recoverable.**
- Clause: "SHALL keep each element's epistemic classification recoverable".
- REQ-007's scenario on line 530 of NEW-amendment-spec.md covers this only indirectly.
- CC-REV-8 is also stronger ("carry the same Observed / Inferred / Unknown labels").
- Fix: add an AND to Scenario 2: an Inferred edge renders with its Inferred marking, and the diagram's text equivalent (REQ-012) carries it.

**m4. Scenario 3's list of forbidden content is vaguer than PWB-REQ-006 and than the packet.**
- Quote: "no script, external reference or interactive content".
- Fix: "no script, event-handler attribute, `foreignObject`, external or unsafe-scheme reference". This matches PWB-REQ-006's vocabulary and the packet's sanitizer, and makes the check mechanical.

**m5. Scenario 3 does not cover a renderer that exists but fails.**
- It covers "no inert renderer is available". The packet covers "If rendering fails".
- Fix: "when no inert renderer is available or rendering fails".

**m6. "declarative source" is required but never required to be kept.**
- CC-REV-8 wants the source "diffed and reviewed like prose".
- Fix: add "retained with the asset for review".

**m7. PACKET.md's "They restate nothing" is inaccurate.**
- The honesty clause partly repeats the existing sentence "A diagram SHALL identify the relationship it clarifies, with support for factual edges as well as nodes".
- The truncation wording repeats "Each depth SHALL retain a true coarser account".
- Fix: merge the new honesty clause into the existing diagram sentence, and change the packet to "They add to REQ-004; where they overlap existing text they narrow it".

**m8. PACKET.md's counts can only be partly checked here.**
- Verified:
  - REQ-004's `#### Scenario:` headings go from 11 to 14.
  - The P-73 offset of 26 lines matches the second hunk (`-156,6 +156,32`).
- Not verifiable:
  - "31 requirements and 177 scenarios" cannot be checked from these files. NEW-amendment-spec.md holds 9 requirements and 59 scenarios, and the predecessor spec was not supplied.
- Fix: cite the path and command that produce 31/177, or state that the figure covers the predecessor plus the amendment.

**m9. The packet's validation step checks labels, not edges.**
- Quote: "A diagram whose node or edge labels are absent from its section's text fails the stage"
- Unlabeled edges between nodes named in the text pass this check. That is exactly the failure *Meaningful visual instead of decorative quota* describes.
- Fix: say that validation also checks each edge's support reference, and that the label check is necessary, not sufficient.

**m10. Tree form may pull against REQ-002's "connected account".**
- The packet replaces "Connected prose" with "an abstraction tree". REQ-002 still requires a "coherent project-specific argument" and a "connected account".
- Fix: say in the packet (or the prompt note) that tree form keeps the argument's connections between motives, promises and capabilities.

**m11. The inertness scenario may belong under REQ-012.**
- It is a prohibition, placed under REQ-004 whose Form is "state projection/query".
- REQ-012 (Form: invariant) already covers inert rendering and diagram text equivalents.
- The existing Falsifier ("A prohibited effect occurs") does cover it, so this is acceptable. But the packet should name REQ-012 as an interaction, including that "Diagram text equivalents SHALL preserve elements, relationships, anchors, legends and markings" applies to the new SVG output.

**m12. Concision.**
- The new text adds about 150 words to a single paragraph that is already over 600.
- Fix: consider "Each section SHALL be an abstraction tree (CC-REV-8): …", so the clause cites the policy instead of paraphrasing it, keeping only the Polaris-specific deltas (precedence, disposition, inertness, epistemic class).
