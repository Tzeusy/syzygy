# M14 provenance-depth funnel — independent review 1 (RAW)

Reviewer: fresh-context reviewer (Claude), read-only.
Date: 2026-09-17. Subject commit: 7d764fc3b68dd5bc128e25f0e309b036906ed87f
on branch agent/syzygy-dov.14. No daemon started; port 7478 never
contacted; no tracked file edited; no Butlers checkout read. The
retained captures were read read-only, never re-served.

## Frozen bytes I measured (computed myself)

Packet   docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md
  bytes  31659
  sha256 0ed3940533bfb368170ba5a4226e40273e646dcb442da0f7349d
         633e025cb3e3
Evidence docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json
  bytes  13943
  sha256 1a16d30552f04f6e08f149790f487e22d9ccb5e344fd134278e87
         e5903adcafe
Register .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md
  bytes  29287
  sha256 ba741cc157371f9e966e1e7b93c5278b19ff7c8ad55cb74655828
         5ef20598b
(The two sha256 tails are wrapped across two lines for width; join
them. Each is the value sha256sum printed over the frozen bytes.)

Captures (read-only, byte-verified against the evidence record):
  post-trim polaris-direct.html  1478637 bytes,
    sha256 2fecdd01e1a2ff577567495796ea7e59ab89f1420be6033e233
    14d26442ea094 — matches the evidence record exactly.
  post-trim polaris-tailnet.html 1484487 bytes — matches.
  post-trim api-poc.json         5520314 bytes — matches.
  pre-trim  polaris-7478.html    2090025 bytes — matches.

## What I re-derived, and by what method

Method: Python re over the frozen capture bytes; a second, independent
method for every load-bearing figure (verification rule 2).

1. Headline source-row distribution.
   - post-trim direct: 278 `<tr id="polaris-source-` rows, 278
     `<b>Rule:</b>` tokens. Per-rule (Counter): root-index 1,
     pillar-index 5, pillar-named-file 54, baseline-spec-tree 192,
     roster-tree 26. Non-baseline = 1+5+54+26 = 86; 86/278 = 30.9%.
   - pre-trim 7478: 271 rows; root-index 1, pillar-index 5,
     pillar-named-file 54, baseline-spec-tree 185, roster-tree 26;
     non-baseline = 86; 86/271 = 31.7%.
   - Figure that moved: denominator 271->278 (+7), baseline
     185->192 (+7); the 86 unchanged in count and composition on
     both. Matches the packet and evidence EXACTLY.
   - Second method: machine projectShape.sources rule tally equals
     the HTML per-rule tally on the post-trim capture (both 192
     baseline, 86 non-baseline). Third corroboration: distinct route
     identities = 192.

2. Route links. post-trim: 386 `/polaris/source?identity=` hrefs over
   192 distinct identities; decoding each identity and mapping it to
   its source rule, ALL 386 are baseline-spec-tree and 0 are
   non-baseline. Confirms "386 hrefs over 192 distinct, 0
   non-baseline." pre-trim: 372 over 185 (the packet cites only the
   post-trim 386/192; the pre-trim link figure is not stated and did
   not need to be).

3. The 77/9 split (projectShape.sources, 278 entries, tallied by
   (anchor.kind, record.outcome)):
   - baseline-spec-tree: 192 blob+classified (all routed).
   - non-baseline: 86 = 77 blob+classified + 9 blob+excluded.
     77 = pillar-index 5 + pillar-named-file 53 + root-index 1 +
     roster-tree 18. 9 = pillar-named-file 1 + roster-tree 8.
   - All 278 anchors are kind 'blob'; 0 tree, 0 missing-at-revision.
     Confirms "no tree or missing anchors in this capture."
   Matches the packet (Sec 2) and evidence EXACTLY. The withheld
   count 9 is correct, and all 9 carry record.outcome == 'excluded',
   which verbatim-route.ts line 87 refuses (fail-closed) once the
   class gate is dropped — so they stay digest-only by construction.

4. Item reconciliation (Q4). projectShape.items length 415 across 9
   classes: baseline-spec 192, topology-component 87, catalog-entry
   65, design-contract 32, success-criterion 13, principle 7,
   craft-policy 7, roster-identity 6, project-account-section 6.
   Catalog 8-class sum = 415 - 6 (project-account-section) = 409.
   Page renders 417 bare `data-polaris-item` occurrences. Delta
   417-415 = 2. All EXACT. The delta is labelled [Unknown] from the
   HTML alone in both the packet (Sec 3, Q4) and evidence — honest,
   not silently reconciled. Denominator/predicate stated at each.

5. Depth page (Q5). projectShape.entities = 9, one of each kind,
   exactly 1 of kind 'capability'; deriveCapabilityDeepDives filters
   kind === 'capability', so exactly 1 hard-coded capability depth
   page. Matches Sec 4.

## Source citations (checked at a9f671e, the packet's baseline)

All correct:
- verbatim-route.ts line 78-79: the class gate
  `if (source.rule !== 'baseline-spec-tree')`, refusal
  'unconsented-source-or-provider', detail "the exact-requirement
  route applies to baseline specs only." Line 87: the
  `outcome === 'excluded'` refusal 'excluded-content'. Both exact.
- capability-detail.ts lines 96-119: deriveCapabilityDeepDives.
  Lines 256-260: the selectRequirementSections call and the join;
  line 258 is the "carries no requirement heading" notRendered.
- polaris-source.ts lines 41-43: sourceRouteHref. Lines 49-58:
  sourceRouteIdentities (function spans 49-60; the cited 49-58 is
  the body). Comment "the one carrier of the identity; no attribute
  restates it" is at lines 45-47, quoted correctly.
- project-shape-manifest.ts line 71: SOURCE_RULES = the five rules,
  exact.
- spec.md line 816: the heading "Requirement: PWB-REQ-015 —
  Capability detail preserves authority bands and exact intent".
  Exact.

## Owner questions (Q1-Q5)

Exactly five, one per slice (Q1 S5-M2, Q2 S5-M3, Q3 S5-M4, Q4 S4-M4,
Q5 S4-M3). Each carries a recommended answer, its lawful arms, and a
stated default of "nothing ships." Trade-offs are preserved, not
smoothed (the counter-argument to Q1 arm (b) is stated as "the strong
one"; Q2's selector arm is flagged as a route-shape change). Q5 asks
for amendment-DRAFTING authorization only: it states a CC-REV-2
semantic delta binds nothing (VIS-4), that it trips the continuation
act's spec-amendment escalation trigger, and that implementation
waits on the signed amendment plus a fresh authorization. It does NOT
authorize implementation. Confirmed.

## Planning-only and lawful

git diff a9f671e..7d764fc: 3 files, 591 insertions, 0 deletions —
the packet, the evidence record, and a 2-line addition to the
register. No implementation code; no act-bound byte edited; nothing
installed into an accepted home. The register change is a pure
addition of the P-81 row. Confirmed.

## Register row P-81

- branch 7d764fc: `^| P-` rows = 27 (22 open + 5 acceptance, the
  P-25/P-25(c) sub-lettered pair both counted); main a9f671e = 26.
  Confirmed.
- Exactly one `^| P-81 ` row; P-81 appears in no sibling file — only
  the register, the packet, and the evidence record carry the token.
- The P-81 row quotes no signed digest and backticks no Butlers path.
  Its Q1-Q5 renderings are faithful one-line restatements of the
  packet's questions, recommendations, arms and defaults.

## Conventions

- Self-referential figures re-derive: 391 content lines (wc -l = 391,
  sed 391p is the last real line, 392p empty), 365 non-fence lines,
  0 lines over 78 columns under the stated predicate (first non-space
  not `|`, `>`, `#`), 0 odd-backtick non-fence lines. All match the
  packet's Gate 6 and the evidence record.
- No code span is broken across a line break; hard-wrap respected.
- `python3 scripts/check_governance.py` at 7d764fc: 32 OK, 20 WARN,
  0 FAIL. The 20 WARN are the standing downgrades (CG-20/21/27
  advisory, etc.), none touching this packet.

## Findings

F1 — non-blocking. The evidence record
(polaris-m14-provenance-depth-funnel-2026-09-17.json,
`body_classification_for_s5_m2.nonbaseline_blob_excluded.meaning`)
and the packet (Q1 line 54 "roster identity files and one named
file", and Sec 2 "The 9 excluded are withheld active content")
characterize all 9 withheld sources uniformly as active content whose
"TOML has no inert context." The machine answer shows 8 of the 9
carry redactionClass `unclassifiable-excluded` (the TOML case) but
one — roster/qa/MANIFESTO.md, a roster-tree markdown file — carries
`excluded-artifact`, which is neither TOML nor an identity file. The
load-bearing partition is unaffected: all 9 have
record.outcome == 'excluded' and are kept digest-only by the
line-87 refusal regardless of sub-class, so every count and every
recommendation stands. Repair: qualify the gloss, e.g. "withheld by
policy — 8 unclassifiable-excluded (TOML, no inert context) + 1
excluded-artifact (a roster manifesto)," and soften "roster identity
files," since one of the 8 roster-tree exclusions is a manifesto, not
a butler.toml identity file. Editing the evidence record and the
packet's two glosses discharges it; no figure changes.

F2 — editorial. The evidence record's `route_leaf_caveat` cites
`capability-detail.ts:256-259` while the packet body cites 256-260
for the same block. Both point at the selectRequirementSections call
plus its refusal/join; the join is at line 260 and the refusal string
at 258. Harmless inconsistency; align to 256-260 if touched.

No blocking finding: every load-bearing measurement reproduces
exactly by at least two independent methods, all source citations are
correct, the questions are well-formed and planning-only, and the
register row is faithful.

Verdict: CONFIRM WITH EXCEPTIONS
