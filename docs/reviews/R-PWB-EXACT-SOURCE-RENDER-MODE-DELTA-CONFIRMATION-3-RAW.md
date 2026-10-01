# Review — PWB exact-source render mode (round 4, fresh confirmation of regenerated package)
Reviewed commit: 99cecd84639798feb34275dd652aeb747fb55fcf
Manifest SHA-256: 527be5ac3732619608355ae9658c92cee45341e831521bc526398481dd915785
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh context (CC-REV-1), no authoring share. Per instruction I did
not open the earlier confirmation raw or any ROUND-3-DISPOSITIONS.md. The
manifest digest above is the sha256 of the file
`.syzygy/governance/contracts/candidates/pwb-exact-source-render-mode-scenario/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`,
computed this session with sha256sum.

## What I ran (this session, detached worktree at 99cecd8)

1. `git diff 0b6c583..99cecd8 -- <package> scripts/`. [Observed] `scripts/`
   is unchanged. Package changes: `proposed/GOVERNING-DEPENDENCIES.md.patch`
   (one line, source-digest 9a44bdb6... to 14e01af3...), the manifest (the
   `GOVERNING-DEPENDENCIES.md` row 787d983e... to de3f7b8f... and the `spec.md`
   row 30ce75f9... to 14e01af3...), `OWNER-DECISION-PACKET.md` (exactly two
   digest copies, 5796c154... to 527be5ac...), plus `ROUND-3-DISPOSITIONS.md`
   (+28 lines; per the independence instruction I read only the diff stat,
   not its content). No other package file, and none of the other three
   patches, changed.
2. `build_pwb_exact_source_render_mode_amendment.py --check`: "manifest
   matches 11 proposed behavior subjects (4 patched, 7 unchanged); ... the
   generated dependency file carries the proposed spec.md digest; on the
   scoped-attributes tree the 3 semantic patches apply and the generated one
   collides as declared; ... partial scoped-attributes tree ... detectably
   inconsistent". `--selftest`: the full fail-closed list printed, no
   failures. I read the text, not the exit code.
3. In a `git archive` copy: all four patches applied with `git apply`
   (spec.md patch with a 16-line offset, no rejects). The 11 composed files
   were checked against the 11 manifest rows with `sha256sum -c`: 11 rows,
   0 mismatches. The composed spec.md hashes to 14e01af3..., equal to the
   GOVERNING-DEPENDENCIES.md line 11 source digest. Mutation: in a second
   archive copy, editing a sentence in `proposed/spec.md.patch` made `--check`
   fail with "names a spec.md digest that is not the proposed spec.md digest"
   and "manifest differs from exact regeneration"; an earlier sed whose
   pattern did not match changed nothing and `--check` still passed, which
   confirms the check keys on the bytes.
4. `python3 scripts/check_governance.py`: "31 OK, 21 WARN, 0 FAIL (52 checks)".

## Criteria

1. Withholding. [Observed] Proposed spec text (composed spec.md 658-662, 734-741):
   an excluded record outcome "SHALL NOT be served in any mode", with a
   dedicated scenario, falsifier and mutation-proof entry. I tried: a
   whole-body request for an excluded source; a requirement-sections request
   via a baseline path whose record is excluded; an anchor naming a unit of an
   excluded source (anchor is presentation only and requires a served
   source); a mode parameter outside the closed set. None serves a body. The
   nine-source count (seven manifests, one page, one roster artifact) is
   asserted in SEMANTIC-DELTA, not testable from the text alone, and I did not
   re-derive it [Unknown for the count; the normative text does not depend on
   it]. See Finding 3 for one wording gap.
2. Gates. [Observed] spec.md (composed) 663-666: the four gates apply "to the
   complete transient body before encoding any part of it"; a failed gate
   "SHALL leave that body Unknown with its reason". "Any part" cannot be read
   per-section; the baseline scenario's "only that requirement" governs what is
   encoded after the gates, not what is scanned. Pass.
3. Content class. [Observed] Both new scenarios keep the "existing
   declared-project-shape-text" gates and "grants no wider content-class
   access"; design.md section 8 addition says "reads no wider class". See
   Finding 2 for a retained sentence in tension with the new paragraph.
4. Change class. Normative is right: the adopted text admits one body-reading
   population (baseline requirement) and nothing says what happens elsewhere,
   so no reading already obliges the new text. [Inferred]
5. Anchors. [Observed] Composed spec 667-670 and the citation scenario: the
   anchor is presentation only, removes/narrows/reorders nothing, and does not
   "enter, replace or qualify any source, claim or narrative anchor identity".
   PWB-REQ-014 is unchanged and consistent.
6. Parity. [Observed] "recoverable, per rendered tuple, from the same
   evaluation in the machine answer"; the oracle partitions the complete source
   population with both denominators and states per-tuple. Falsifiable via the
   mutation-proof list. PWB-REQ-020 untouched.
7. Closed vocabulary. [Observed] "exactly one render mode drawn from the closed
   set `requirement-sections`, `whole-body`", mode chosen by source class, a
   mode outside the set and a mode on the wrong class are falsifiers. Mode and
   refusal reason are recoverable per tuple.
8. Package mechanics. Verified above (items 2 and 3 of the run list).
9. Coverage. [Observed] The coverage patch changes only row 10 (one line);
   row 10 still names PWB-REQ-011; no other row touched; the patch does not
   alter the totals lines.
10. Scope. [Observed] The spec patch hunks lie wholly inside PWB-REQ-011
    (composed lines 640-760); no PWB-REQ-015 or PWB-REQ-002 text is touched.
11. Comprehension. A cold reader can restate change, refusals, the owner
    choice and path from SEMANTIC-DELTA; the stale items are in Findings 1-2.
12. Owner packet. [Observed] OWNER-DECISION-PACKET.md:3-6 and 164-177: inert
    offering, silence/partial answers perform nothing, the phrase is stated as
    "not offered". Only the two digest copies changed and both equal the
    manifest digest.

## Opening-band collision (item 4 of the brief)

[Observed] The opening-band scenario is
`#### Scenario: One opening Unknown aggregate, reconciled with members`
(composed spec.md line 621), in PWB-REQ-010. The render-mode patch edits
only PWB-REQ-011 (hunks at original lines 637 and 699, 16-line offset from the
earlier base). Applying the patch left the opening-band scenario text
byte-present at 621-633 and the diff against the unpatched tree shows only
PWB-REQ-011 additions plus the generated dependency line. No opening-band
text is dropped or collided.

## Findings

**Finding 1 — stale line citation in the current-meaning section** (note)
`SEMANTIC-DELTA.md:24` says PWB-REQ-011 is "spec.md lines 632-677". After the
opening-band base, the requirement occupies lines 648-694 of the unpatched
spec.md (heading at 648, PWB-REQ-012 heading at 695). The quoted text is still
byte-identical to the tree; only the coordinate is stale. This is an artifact
of regeneration over a moved base. The same page's REVIEW-BRIEF.md:16 carries
the stale "first round / no prior raw review" sentence (the brief's own
staleness was flagged by the requester; I noted it and did not act on it).

**Finding 2 — retained "raw artifact" sentence sits beside the new whole-body paragraph** (note)
`design.md` section 8 (unpatched lines 256-270, the unchanged paragraph at its
end: "Any proposal to read a body outside that population or return a raw
artifact requires a separate consent amendment and act") is followed directly
by the new patch paragraph (proposed/design.md.patch, "The same reasoning
carries to every other source ...") which serves the complete body of a
non-baseline admitted source. The patch never says that a `whole-body` serve
of an in-population admitted blob is not "returning a raw artifact"; the
SEMANTIC-DELTA quotes the sentence (SEMANTIC-DELTA.md:99) but does not
reconcile it. A reader could reasonably read the old sentence as forbidding
the new mode. The intended reading (raw artifact means outside the signed
population) is [Inferred], not stated.

**Finding 3 — "SHALL serve every admitted source" versus gate failure and non-excluded non-admitted sources** (note)
Composed spec.md 655-657 says the route "SHALL serve every project-shape
source the evaluation admitted as a classified blob", while 663-666 and the
whole-body scenario say a failed gate leaves the body Unknown, and the
scenario uses "may". The unconditional SHALL is reconciled only by implication.
Separately, the explicit never-served guarantee (658-662, 734-741) names the
"excluded" record outcome only; sources that are missing, unreadable or
unclassifiable (PWB-REQ-003) are not "admitted as a classified blob" so they
are not served, but no sentence says so, and the sweep wording ("admitted and
excluded alike") does not name them. Not a way to serve a withheld body, so
not blocking.

**Finding 4 — an additional changed package file outside the declared change set** (note)
The diff 0b6c583..99cecd8 for the package also changes
`ROUND-3-DISPOSITIONS.md` (+28 lines), which the regeneration description did
not list among the intended changes. It is not a manifest subject and not a
digest-bound act copy, so it does not affect any digest verified above; I did
not read it, per the independence instruction, and report only that it
changed.

## Verdict basis

Zero blocking and zero revise findings. [Observed] Manifest, patches, composed
digests, `--check`, `--selftest`, and check_governance all pass as run this
session; the four findings are notes on wording and coordinates. Verdict:
CONFIRM WITH EXCEPTIONS (notes only). This confirmation is bound to manifest
SHA-256 527be5ac... at commit 99cecd8; any repair of the notes retires it
(rule 10).
