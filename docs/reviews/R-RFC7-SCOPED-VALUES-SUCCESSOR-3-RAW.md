# Review — RFC-0007 scoped-values amendment, round 3
Reviewed commit: cf0bf6f50c903db2094dee93e9623e87f2040ee7
Manifest SHA-256: 01e76e0b357d847684c7f460a9ff0e708c5cfba3d9d246d5aa2ed318eb1cd8ad
Verdict: REVISE

Fresh context. Subject: `.syzygy/governance/contracts/candidates/rfc7-scoped-values-successor/`
at the commit above, in a detached worktree (removed afterwards). Mutations ran
only in `git archive` copies under the session scratchpad. The two earlier
raws for this package were not read. The sign-off will be version-tagged
(OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md), so the head digest
is informational.

## Verification run this session

- `build_rfc7_scoped_values_successor.py --check`: passes. `--selftest`:
  21 fixtures, 0 failing. `record_rfc7_scoped_values_successor.py --selftest`:
  33 fixtures, 0 failing. `check_governance.py`: 31 OK, 21 WARN, 0 FAIL.
- `sha256sum` of the manifest file: 01e76e0b...cd8ad (as in the head).
  Patching the installed module with the package patch by script gives
  dcdab7d43505...2b2a, the manifest row. The two mirrors are `cmp`-identical.
- Diff content: exactly one parenthetical and one paragraph (criterion 4
  holds). The non-citability sub-clause is untouched (criterion 2 holds by
  reading). Packet offers nothing, recorder refuses (unpinned), no chain link
  is registered in `CONTRACT_SUCCESSOR_CHAIN` (criterion 6 holds).
- Mutations in the archive copy: (1) the exclusion of non-citable removed from
  the package patch only: `--check` rejects, "lane B contract patch and this
  package's patch give different module bytes". (2) Manifest first hex digit
  flipped: rejected, "manifest differs from exact regeneration". (3) One
  mirror edited: rejected, mirrors differ. (4) The exclusion removed from
  BOTH patches, then `--write`: `--check` passes. The builder guards bytes,
  mirrors, leads, headings and lane B agreement; it has no predicate on the
  paragraph's content (see Finding 6).

## Findings

**Finding 1 — "Only a reader's own manual selection ... can separate a unit from its scope's text" is false, and the lane B delta says so** (revise)
`proposed/RFC-0007/rendering-and-surface.md.patch` (the sentence beginning "Only a reader's own manual selection") makes an absolute claim in normative text. The lane B SEMANTIC-DELTA concedes the opposite at `pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md:416-421`: a reader arriving by anchor or exact-source route "lands inside the scope, after its text" and finds on the unit only the fields the scope does not carry. Fragment links, find-in-page, tab or screen-reader element navigation and the RFC6-18 drawer handoff all separate a unit from its scope's text without any selection. The sentence is the paragraph's only answer to the loss of a distinction when a unit is reached or copied alone, and it is wrong. A reader (or an agent given one row) loses Unknown, stale freshness, draft or review state, and the contract text tells the next implementer the case cannot arise. Replace with an honest statement of the residual (arrival or selection away from the scope's text recovers the scope by the enclosing element), or remove the sentence.

**Finding 2 — the paragraph licenses the loss that RFC7-33's own closing sentence forbids, for every distinction but non-citability** (revise)
RFC7-33's final sentence (`rendering-and-surface.md:218-219`) is left unchanged: "A distinction available only to pixels does not survive ... a copy-paste into an agent prompt". The new paragraph's last two sentences accept that a manually selected unit loses its scope's text, and justify excluding only non-citability "because it must travel with a unit wherever it goes". The converse reads as a rule: Unknown, stale freshness, editorial-draft, unadopted and review state need not travel with a unit. Those are the VIS-1/VIS-2 distinctions (Unknown never folds; draft is not curated). A pasted row under an all-Unknown or all-stale scope carries no label at all, and an agent reads an unlabeled fact. The exclusion list should be argued from what a unit loses, not from non-citability alone, or the scope must be restricted so that no VIS-2 distinction (Unknown, freshness, draft/adopted, review state) is scope-carried, or the unit must keep a minimal marker.

**Finding 3 — the interactive surface is defined by delivery, which puts HTML-fetching agents under the permission** (revise)
The paragraph defines the surface as "the HTML document served for a browser to render" and everything else as "every output that is not that document". The test is the document, not the consumer. RFC7-33 names agents as first-class consumers. An agent that fetches the page URL, or any text conversion of it (reader mode, web-fetch tools, "save as text"), is served that document, so it receives the scoped form; conversion drops the scope marker and attributes, leaving the association to document position, which RFC7-34 says recovery must not depend on ("without colour, position, or layout"). The sentence "so does any copy, share or export function the surface offers" covers only functions the surface itself provides, not browser-native save, print or reader mode. Either say that a consumer other than a browser rendering the page receives the unit-carried form (content negotiation or a distinct representation), or state in the paragraph that the scope marker and scope text are its only recovery path and say what a text conversion must preserve.

**Finding 4 — scope-carried tier and label lose RFC7-16's "beside it" at-rest requirement; only freshness is protected** (revise)
The paragraph says "a scope-carried freshness stays visible on the page itself (RFC7-16)". RFC7-16 (`narrative-contract.md:348-364`) puts label, tier and freshness in the at-rest set and says tier must "render beside" a composed-prose sentence or it "reads as settled"; it also requires one epistemic state per capability or major claim. The paragraph permits tier, label and evaluation identity to be carried on an enclosing element, yet protects only freshness by name, and "visible on the page" is weaker than "beside the sentence". A narrative sentence under a section scope can then sit away from its tier and label. Also, "this includes the evaluation identity RFC7-16 requires" reads RFC7-16 as satisfied by expansion, which the walkthrough prompt ("every capability carries four technical carriers", `rendering-and-surface.md:147-150`) does not say. State whether RFC7-16's per-capability at-rest display is met by scope text, and apply the same visibility rule to label and tier.

**Finding 5 — the lane B SEMANTIC-DELTA "Proposed meaning (quoted, the bytes the patches produce)" quotes a different paragraph and parenthetical from the bytes this package produces** (revise)
`SEMANTIC-DELTA.md:285-313` quotes the parenthetical "(except as the interactive-surface paragraph below permits)" and an older paragraph ("On the interactive human surface only ... A unit copied out of the interactive surface without its scope has lost what the scope carried ..."). The package patch and the lane B contract patch (which compose to the same module bytes; only the patch file headers differ, so `cmp` of the two files differs at byte 14 as expected) say "(except, on the interactive surface alone, as the scope paragraph below permits)" and a paragraph with the HTML-document definition, the RFC7-16 clause, the validity rule and the manual-selection sentences. A reader relying on the delta (rule 8; the delta is what the owner reads for step 2) would sign over text the module does not contain; `SEMANTIC-DELTA.md:355` ("keeps every word and gains one parenthetical") and `:24` rely on the older shape. The same delta also rests on "Nothing here relies on position" (`:412`) while the contract paragraph now concedes selection loss. Criterion 5: bytes agree, the quoted meaning does not. It cannot be repaired here without a lane B revision; flag for the lane B package before step 2.

**Finding 6 — the owner packet describes the amendment more narrowly than the paragraph reads** (revise)
`OWNER-DECISION-PACKET.md` "What the package changes" summarizes the paragraph as the permission plus "never carries a value that is not every unit's value ... expanded before any parity comparison". It omits the four additions that carry the policy weight: the delivery definition of the interactive surface (Finding 3), the explicit inclusion of evaluation identity and freshness (Finding 4), the validity rule that a differing unit invalidates and suppresses the scope, and the concession that manual selection can separate a unit from its scope's text (Findings 1 and 2). The owner decides (a), (b) or (c) from the packet. Add those four items to the packet so the choice is informed. Related, and a note-level point folded in here: nothing mechanical protects the exclusion of `non-citable` / `presentation-artifact` (mutation 4 above: exclusion deleted from both patches and the manifest regenerated, `--check` passes). That is a review obligation at each regeneration, which a one-line predicate in the builder would turn into a check.

**Finding 7 — wording that can be read against the paragraph's own rule** (note)
(a) "it never overrides, replaces or fills in for a unit's own attribute" sits beside "A unit under a scope then carries the value by expansion": expansion is filling in an absent per-unit attribute. The intended meaning is probably "never supplies a value the unit's model value does not have"; as written it can be read as forbidding the inheritance rule lane B states ("a claim's value for a field it does not carry itself is the value of the nearest enclosing scope"). (b) "identity" is used for two things: "the evaluation identity RFC7-16 requires" may be scope-carried, while "a scope never carries a unit's identity" is not. "Unit's identity" is undefined in the module; name it (the claim id, anchor) to avoid a reading in which an evaluation-identity scope is itself forbidden. (c) The parenthetical in the opener sits before "served identically through the machine-queryable endpoints" and applies to every distinction in the enumeration including non-citability until the paragraph below is read; a rule-8 quote of the opener alone shows an exception that the sub-clause then removes. The delta accepts this (`SEMANTIC-DELTA.md:355`); noted only.
