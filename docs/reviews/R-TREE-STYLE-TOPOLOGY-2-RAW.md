Title: Topology bundle tree-style restyle — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: the NEW-* files against the OLD-* files in `review-topo2/`. That covers the nine topology members, `BUNDLE-MANIFEST.md`, the acceptance-record row 3, `05-CONTRACT-INDEX.yaml` and `TOPOLOGY-TREE-RESTYLE.md`. I checked them against review 1's M2 and its "Topology views" table.
Reviewer: independent fresh-context agent

**How I checked** [Observed]
- I read every OLD/NEW diff in full, and the full NEW text of each changed section.
- I compared the files with Python scripts. Across all nine member pairs:
  - **Mermaid blocks:** all 8 OLD blocks appear byte-identical in NEW. NEW adds 2 blocks, both in 04.
  - **Table rows:** all 37 OLD rows appear in NEW, in the same order, with no extra rows.
  - **Head banners:** 9/9 are byte-identical. The first two paragraphs of each file are also byte-identical.
  - **Headings:** 9/9 are identical.
  - **Identifiers and code spans:** none lost and none added.
  - **Links:** none lost. Each file gains exactly one link, `../../governance/decisions/TOPOLOGY-TREE-RESTYLE.md`.
  - **Backticks:** outside fences, no line has an odd backtick count.
  - **Characters:** NEW adds no non-ASCII characters.
  - **Epistemic labels:** the counts match in 8/9. README gains one bracket, and it is a mention of the label ("all runtime behavior is **[target]**"), not a new label.
- **Manifest digests:** I ran sha256 over every NEW member. 9/9 match the NEW manifest rows.
  - Manifest file sha256: OLD `568a6f17659af770a5f052922b10299fceb564cc4601b65d5c5a3c13d9dba096`, NEW `f1cf040728c94106df46cb01462070ddcb05d6730ddb8c5c190131f92bed5083`.
  - The NEW value equals the argument in NEW acceptance-record row 3.
- **The restyle-line link:** it resolves from `.syzygy/map/topology-candidates/`. It also resolves from the post-act home `.syzygy/map/topology/`, which acceptance record line 194 names and which sits at the same depth.

## Review-1 findings in scope

| Finding | Status | NEW text |
|---|---|---|
| M2: manifest history line, banners over changed bytes | RESOLVED | Manifest Date line: "…semantic delta on record), and again 2026-09-28 after the tree-style readability restyle (no change of meaning)." Each of the nine members, under an unchanged banner: "Restyled 2026-09-28 for readability (no change of meaning); reviews 5–7 reviewed the prior bytes, and this restyle's review is recorded in [the topology restyle packet](…)". Row 3 re-quoted, with a dated note. |
| README: dropped "drawn while…in flight" | RESOLVED | "These diagrams were drawn while the whole RFC set was still in flight, and they lag it in both directions, so the RFC governs wherever the two disagree." |
| 01: "Three SEC boundaries enclose Syzygy" | RESOLVED | "Three SEC boundaries apply (SEC-1 around Syzygy, SEC-2 around owner-controlled infrastructure, SEC-4 per repository)". This matches the unchanged diagram's subgraphs. |
| 01: "consumes it: the single owner" | RESOLVED | "**Who surrounds it:** the single owner, and the machine clients that consume the same truth." |
| 02: "All of this is target" | RESOLVED | "The machinery drawn here is target. Today only this repository's governance-root shape exists; the generalization to the owner's portfolio is inferred." |
| 03: drops "at one evaluation" | RESOLVED | "…shows the same facts for the same selection at one evaluation." and "one per selection, evaluation and scenario context." |
| 04: "each written under one of four classes" | RESOLVED | "…four write-authority classes; the table gives each path's typical write authority." |
| 04: `declarations/` without OPEN | RESOLVED | "a reserved `declarations/` category whose standing is OPEN" |
| 04: drops "mutable" | RESOLVED | "For every mutable field of an externally owned record exactly one store is writable…" |
| 05: "each failure has a defined rendering" | RESOLVED | "the named failures render as Unknown with a reason". The body still enumerates the six. |
| 06: "Five human gates" | RESOLVED | "Human gates sit on the loop, …". No count. |
| 06: "split between V0 and V1" | RESOLVED | "The entire flow is target; the reconciliation evaluation exists in no substrate today." This matches the [Observed] bullet. |
| 06: "separates planned from scheduled work" | RESOLVED | "**The one-way materialization door** is drawn." |
| 07: "unsafe configurations fail closed" | RESOLVED | "an unauthenticated network-exposed configuration is refused" |
| 08: "mediates one external authority" | RESOLVED | "…mediates an external system under a stated authority boundary…" |

## Material findings

**M1. The packet's "Found while restyling, not changed" list is incomplete for the stale draft-RFC claims.** This does not change the bundle's meaning, but it changes what the owner is told.
- The packet says: "RFC 0001–0009 are now accepted. 07 likewise blocks execution 'until RFC 0005 is accepted'."
- The same stale claim stands, unchanged and unlisted, in five other members:
  - 02:83 "RFC 0003 is a draft contract; nothing enforces it yet."
  - 03:73 "These are drafted contracts (RFC 0001/0002/0006), not running systems."
  - 04:153 "…adapter authorization, audit trail, and migration machinery are draft contracts."
  - 05:92 "The twelve Unknown reasons and six tiers are RFC-draft vocabulary, not yet accepted."
  - 06:119 "The chain is created by these drafts."
- [Unknown] Whether "OPEN at RFC 0003 §8 q4" in 04 is still open now that RFC 0003 is accepted. It belongs in the same list either way.
- Fix: widen the "likewise" to name 02, 03, 04, 05 and 06, and note the §8 q4 question.
- The items the list does name are correct [Observed]:
  - README:57 "Since Syzygy is unimplemented".
  - 01:88 "No implementation exists; no stack is chosen".
  - 03:77 "only `governance/` is populated". This is stale: `.syzygy/intent/`, `map/` and `local/` exist.
  - 07:88 "no daemon".
  - 08:98 "none is implemented".
  - 05 has "twelve" in prose against "Unknown reason (11, closed)" in the diagram.
  - 06 has five gates against four `{{…}}` hexagons, with the Owner hexagon carrying two acts.
  - README gives "SDR-1..33" and "RFC drafts 0001–0006".
  - The banners differ: "candidate" in README, "proposed" in the eight views.

## Notes

**N1. The packet's claims about citations and links are slightly too broad.**
- Line 8 says "No placement, boundary, identifier or citation changes."
- "What stays fixed" lists "Every … link target".
- In fact each member gains one new link, to the packet. "What changes" does disclose this ("links this packet"), so the claim is inaccurate only as worded. Suggested wording: "no link target lost".

**N2. "Nested bullets… reusing their own words" is not strictly true.** Several parent bullets are newly worded statements. Each is faithful to its children:
- 01: "each external authority answers its own question; none answers intent."
- 04: "the two namespaces have different schema owners."
- 06: "one authority answers 'what is the state of this planned work' at a time."
- 07: "The profile carries default-deny credentials…"

**N3. 07's [target] opening drops a qualifier.**
- The opening says: "SEC-1..5 are adopted doctrine and the platform posture is recorded scope."
- It leaves out "and remains RFC-open", which the body keeps: "is recorded scope (v1.md) and remains RFC-open".
- Suggested wording: "…is recorded scope, still RFC-open."

**N4. 06 no longer says every gate is marked.**
- OLD: "with every human-triggered gate marked (hexagons)".
- NEW: "**Human-triggered gates** are marked as hexagons."
- Given the five-versus-four mismatch in the packet list, the weaker wording is the less false of the two. I record it only as a change of wording.

**N5. README states the RFC-governs rule twice.**
- The opening says: "Where a diagram and an RFC disagree, the RFC governs, including for vocabulary."
- The currency caveat repeats it: "so the RFC governs wherever the two disagree."
- This is redundant, not drift.

**N6. The new openings are unlabelled substantive prose.**
- README's convention says "Every substantive prose claim is labelled…". The new section openings summarise labelled bullets and carry no label themselves.
- Example from 08: "every fidelity loss is labelled, and Syzygy depends on no instrumentation". Its parent bullet is "[Inferred: RFC 0004 §2]".
- None of the openings asserts beyond its body, so this is a convention gap, not drift.

**N7. The two new diagrams in 04 are faithful but partial.**
- The walkthrough diagram omits "never from a stored verdict alone".
- The inward limb omits the captured-evidence exception (RFC4-16).
- The outward limb omits "divergence is re-asserted and annotated, never merged".
- The prose beside each diagram keeps all three, and no edge asserts something the body denies.

**N8. The other copy of the old digest is act-bound.**
- The only other tracked copy of `568a6f17…` is `docs/evidence/polaris-generator-approval-offer-2026-09-12.json:2218`.
- That file is `POLARIS_GENERATOR_APPROVAL_SUBJECT` in `check_governance.py`, the argument of a performed act, so it must stay unchanged. It is not in `ACT_DIGEST_COPY_FILES`.
- The packet's "No other registered act-argument copy quotes it" is therefore accurate.

**N9. Other claims check out.** [Observed]
- **Manifest Date line:** the history clause is true. 2026-09-28 is today, and the digests were regenerated (9/9 match). The earlier clauses are byte-unchanged. "(no change of meaning)" is the claim under review, and this review found no material meaning change in the members.
- **Acceptance-record row 3:** the note is accurate. It says "two new diagrams in view 04", "one dated restyle line under each head banner" and "no placement or identifier changed", all confirmed by script.
  - CC-REV-8 exists, added 2026-09-27 per `PROJECT-STATUS.md`:184.
  - The owner direction file exists only on branch `prose/craft-tree`, as the packet says ("lands on the craft branch").
  - "as act 4's was for OVERVIEW" is true: row 4 was re-quoted 2026-09-27.
- **`05-CONTRACT-INDEX.yaml`:** only the ten topology `words:` values change.
- **Nothing labelled accepted or adopted:** the packet opens with "Proposal. It binds nothing until the owner adopts it (VIS-4)". Row 3 calls the packet "a proposal until the owner adopts it". Act 3 stays unperformed.
  - The packet's one "accepted" ("RFC 0001–0009 are now accepted") describes the current state recorded elsewhere. It labels nothing on the owner's behalf.
