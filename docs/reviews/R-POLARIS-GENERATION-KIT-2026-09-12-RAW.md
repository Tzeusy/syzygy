# Polaris generation kit independent review

Verdict: PASS for the bounded documentation handoff. This is not a runtime-generator, source-access, provider, adoption or release verdict.

## Frozen subjects

- `docs/polaris-generation/README.md`: `46134c4b7584903320f42a91db9cc86d55303cb89223e24b48cb781b44b98842`
- `docs/polaris-generation/AUTHORING.md`: `f174270cb4ad8b6a86905754572fc7f52d41cf2632dcb8ef9203ee7d30f31e55`
- `docs/polaris-generation/ARTIFACTS-AND-TOOLS.md`: `f5c0fa6c58dbdf6adfe84c37754cda8e37d3f4f40a210fb81e835c5409c9c22b`
- `docs/polaris-generation/example.json`: `c4550213ac534f5e1f270c7bc2dae8d2d04fca5e3aac3e9eb7023f0a90126460`
- `AGENTS.md`: `fb6cbca9093621ca1de46b1f8427530d05e71b9714e189ff2e7cd3fdb9e41815`
- `docs/POLARIS-READING-LAYOUT.md`: `bb7ee02d2e18a8349362f0f5809c444384b639bfa6faa8383aa37283094e0da6`

## Scope and methods

[Observed] Read the four kit artifacts and the added AGENTS/reading-layout references. Compared their practical handoff against the previously supplied generator candidate, asset contract and design acceptance. Verified the named existing functions directly in application source. Ran an independent Python standard-library check over the example's UTF-8 digest, all three claim support slices, qualification references, coverage references and later-draft references. No observed-project body was read and no external provider or project tool was called for this review.

[Observed] The source is 154 code points. Its SHA-256 matches the recorded value. The three spans [0,66), [67,109), [110,154) exactly equal their claim statements. All examined references resolve. The synthetic example explicitly records that no provider call occurred; it makes no completed-run claim.

[Observed] Tool descriptions correctly name existing exports and distinguish current renderer helpers from proposed operations. The documented commands parse an example or run existing tests; the text explicitly says they do not generate a manifesto. Guidance covers argument, material qualifications, prompt injection boundaries, meaningful visual placement, node and edge support, optional deep-dive linking, output invalidation, bounded repair and independent rendered review. The portability recipe requires two admitted real domains plus semantic source-change regeneration with unchanged tools and prompts. No kit file adopts a specification or grants effects.

## Manual application of Plan to a different synthetic domain

This is a small reviewer-authored application of the supplied prompt to invented inputs. It tests whether the instructions permit a different argument and asset selection. It is not an executed generator run, an independent real-project evaluation or provider-cost evidence.

Synthetic source, three sentences:
1. PlateAtlas makes a university's historical astronomical photographs searchable by visiting researchers.
2. An archivist scans a plate, a curator records its date and sky region, and the catalog indexes that record for search.
3. Original plates remain the authoritative measurement source because scan defects can obscure faint objects.

Audience: visiting researcher. Ledger: c1 = source sentence 1 (declared purpose and beneficiary); c2 = sentence 2 (declared workflow); c3 = sentence 3 (declared qualification). No observed-runtime evidence is supplied.

Frozen questions: What does the project make easier? How does a plate become searchable? When should a researcher consult the original? What remains unknown?

Plan output:
- Section `find-a-plate`: question “Why does this exist?”; c1; lead with research discovery rather than an inventory of components.
- Section `from-plate-to-search`: question “How does a plate become searchable?”; c2; place the workflow figure here, immediately after the introduction, because the documented handoffs explain the mechanism.
- Section `when-the-original-matters`: question “What can a scan fail to preserve?”; c3; keep this qualification beside discussion of using search results and link the optional fidelity note.
- Section `open-questions`: question “What cannot these sources tell us?”; Unknown for coverage, search completeness and operational performance; do not imply these are measured failures or guarantees.

Requested-asset dispositions:
- Workflow figure: planned; Archivist scans plate → Curator records date and sky region → Catalog indexes record for search; all stages and sequence supported by c2. Legend: declared workflow, not runtime telemetry. Text equivalent repeats the supported sequence. c3 qualifies use of the scanned material without inventing an additional processing edge.
- Deep dive `scan-fidelity`: planned; focused question “When should I return to the original plate?”; c3 supports a short explanation only, with return link to `when-the-original-matters` and evidence reference. Do not invent scanning parameters or restoration algorithms.
- Glossary: unnecessary-with-reason for this stated audience and short account; terms are introduced in context. Revisit if reader review finds terminology confusing.
- Architecture component map: unresolved; component boundaries and dependencies are not supplied. Do not transform the three human/workflow roles into invented software services.
- Comparison table: unnecessary-with-reason; the sources do not provide comparable alternatives or measurements.

[Inferred] The Plan prompt supports a different project's vocabulary, order and selection without injecting Butlers roles. The meaningful workflow is permitted while unsupported architecture is explicitly unresolved. This is a narrow instruction check, not proof of generality.

## Findings and limits

No blocking finding for publication as candidate documentation.

Non-blocking wording clarification: the README Author-stage input says “Approved-for-drafting plan.” The term has no attributed approval actor or defined gate in this kit and could imply an extra owner permission at every pass. Prefer “Validated argument plan” within an already authorized run. This recommendation changes workflow clarity, not authority.

Non-blocking clarification opportunity: the illustrative later draft references c1/c2 while the c3 limit remains only in the accompanying ledger. Because this artifact explicitly illustrates one small handoff rather than a complete manifesto, it is not a coverage failure. A future complete output example should show where c3 reaches the rendered account, reinforcing the guide's qualification-preservation rule.

[Unknown] No runnable stage runner, registered bundle schema, arbitrary draft-bundle ingestion, provider execution, retry/cancellation implementation, rendered result from this example, or two-real-project result was verified. Those remain implementation and product evidence work. Syntax and reference integrity do not establish semantic fidelity or rendered beauty.
