# Review — RFC-0007 scoped-values contract successor (candidate package)
Reviewed commit: c67ab2060fdcd18df3203d8c001a66bf1c5b3594
Manifest SHA-256: e9979e0592a77f60eb9914ff84eb9f9eaade8b38f38e1d321bcda2dd4c1c3e50
Verdict: REVISE

Fresh-context review per REVIEW-BRIEF.md, in a detached worktree at the commit above; mutations ran only in a git-archive copy.

## Verification run this session

- [Observed] `build_rfc7_scoped_values_successor.py --check`: exit 0, "manifest matches the patched module on both identical mirrors ... lane B contract patch gives the same bytes".
- [Observed] `--selftest` (builder): 21 fixtures, 0 failing. Recorder `--selftest`: 33 fixtures, 0 failing.
- [Observed] `check_governance.py`: 31 OK, 21 WARN, 0 FAIL (52 checks printed; CG-26 reports 55 published, 55 hosted). CG-7a/7c/7e/7h OK.
- [Observed] `sha256sum` of the manifest file is the digest in the head and equals the digest in OWNER-DECISION-PACKET.md. The installed and candidate mirrors are byte-identical (`cmp`).
- [Observed] Diff scope (criterion 4): the patch has exactly two hunks, one parenthetical in RFC7-33's opener and one inserted paragraph. No heading, front-matter or clause-lead line is touched.
- [Observed] Criterion 5, composition: the lane B patch (path-prefixed) and this patch give identical module bytes (builder check, plus the lane B SEMANTIC-DELTA quotes the same two texts).
- [Observed] Criterion 6: `FROZEN_MANIFEST_SHA`, `REVIEW` and `REVIEW_SHA` are all `None`. The packet says "not yet offered". `CONTRACT_SUCCESSOR_CHAIN` has no link for this package, and the scripts' `--apply` refuses without an act record.

## Mutation checks (rule 6, archive copy)

Builder `--check` fails as it should for each of these:
- patch text altered (exclusion word replaced), manifest unregenerated: fails, "different module bytes" against lane B.
- the same alteration with the manifest regenerated: still fails, because of the lane B agreement check (digest back to the original after restoring).
- manifest row digit changed: "differs from exact regeneration".
- candidate mirror appended: mirrors differ.
- heading line introduced by the patch, manifest regenerated: "heading lines changed".

Recorder `validate_pins` / `validate_phrase` refuse each of these: REVISE verdict, wrong manifest digest in head, verdict outside the first four non-blank lines, raw bytes drifted from the pinned sha, unpinned, wrong pinned manifest, wrong label, uppercase digest, trailing newline in the phrase. They accept a well-formed CONFIRM and CONFIRM WITH EXCEPTIONS head. `check()` on the live tree returns False (not performed).
- [Observed] Predicate gap: the recorder accepts a blank line after the title and does not require the title, `Reviewed commit` line, or line order. See Finding 4.

## Findings

**Finding 1 — The paragraph concedes the copy-out loss that criterion 1 forbids, for every distinction but non-citability** (revise)
Evidence: `rendering-and-surface.md.patch` lines 28-32 (the paragraph's last sentence): "A unit copied out of the interactive surface without its scope has lost what the scope carried, which is why non-citability is excluded". Criterion 1 requires that no reading lets a scope replace a unit's attribute "on a copy taken out of the surface". The unmodified RFC7-33 closing sentence (module line 213-215) still says a distinction available only to pixels "does not survive ... a copy-paste into an agent prompt". The permission reaches label, tier, freshness, reason, editorial-draft state, adopted versus unadopted, review state and target-changed state. A copied claim loses its Unknown or draft marker, which is the VIS-1/VIS-2 hazard the sentence names. The rationale justifies excluding only one attribute, and the contract states no principle for why losing the others is acceptable. Either narrow the permission to a named set of distinctions the owner accepts losing on copy, or state the acceptance explicitly with the reasoning (and amend the unqualified closing sentence's reach). As drafted, the exception that swallows the rule is not owner-visible as a trade-off.

**Finding 2 — Lane B relies on scoping evaluation identity, which the paragraph does not clearly give** (revise)
Evidence: the paragraph permits scoping "a distinction" and sits in RFC7-33, whose enumerated list is "label + tier + reason + freshness" plus the named states. Evaluation identity is an RFC7-16 obligation (`narrative-contract.md:348-355`), not in the RFC7-33 list. The lane B SEMANTIC-DELTA states (in its proposed PWB-REQ-007 paragraph) "this holds for evaluation identity as for every other field" and its estimate hoists evaluation identity "for all 713" tuples. It also hoists secondary reasons and challenge state. Criterion 5 asks that lane B rely on no permission the paragraph does not give. Either name evaluation identity (and RFC7-16's stamp) in the paragraph, or lane B must drop it. Note also that RFC7-16 requires staleness to be "visible on the narrative page itself". Add the sentence confirming a scope-carried freshness stays visible on the page.

**Finding 3 — "Interactive human surface" is undefined, and Polaris pages are fetchable by agents** (note)
Evidence: the phrase appears nowhere else in `RFC-0007/*.md` except line 222's "interactive surface" in the unchanged sub-clause (where it is contrasted with exports). Criterion 1 turns on the boundary between this surface and "plain-text or exported" renderings. The same served HTML can be fetched by an agent without the endpoint. The contract does not say whether a fetched page is interactive. Define the term or tie it to "the HTML page as rendered for a human reader, not served from RFC6-13/14 endpoints".

**Finding 4 — Recorder head predicate is weaker than the brief's head contract** (note)
Evidence: `record_rfc7_scoped_values_successor.py` `validate_pins` accepts any head whose first four non-blank lines contain the exact verdict and manifest lines, in any order, with a blank line after the title, and does not require the title or commit line (my harness case "blank line after title" and "verdict" order). This matches the sibling recorders' stated contract (non-blank lines) but is broader than the brief; harmless for this raw, which meets the stricter form.

## Not found (criteria 2, 3, 4, 6)

- Criterion 2: the exclusion is in the paragraph text and the sub-clause below it is byte-intact. Mutating it away fails the lane B agreement check.
- Criterion 3: the paragraph's three bounds (every unit's value, no identity, text on its own element) plus "expanded before parity" read as sufficient. I could not construct a hiding reading from the text alone. Nested scopes can only repeat values, because an outer scope cannot carry a value that differs from any unit under it.
- Criterion 4 and 6 are as verified above.
