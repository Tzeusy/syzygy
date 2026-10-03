> # Record beside the package — not authority, binds nothing
>
> Dispositions of the first fresh-context review of the PWB opening-index
> amendment package. This record is not a package artifact: the manifest
> does not hash it and no builder reads it. It offers nothing and performs
> no act (VIS-4).

# Round 1 dispositions — PWB opening-index amendment

- **Reviewed commit:** `0241fb835471af3a2ea23119959bdfa34ef14464`.
- **Verdict (raw line 4):** `REVISE`. The review has two revise findings
  (1, 2) and six notes (3–8), with no blocking finding.
- **Stopping rule, set in `REVIEW-BRIEF.md` §"Output contract" before the
  round ran.** A notes-only verdict clears the bytes it read. Any other
  verdict leaves the package unedited: no second round is dispatched, and
  its findings go to the owner.
- **Applied here:**
  - Nothing in the package was edited after the review. Every finding below
    is **open**, with a proposed repair for a later version.
  - No round 2 is dispatched.
- **Status: not cleared.** Scope A offers a package only after a round that
  returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only. This version
  is not offered for sign-off. It goes to the owner as P-98. The drafter
  recommends packet question 1 *Revise*: one new version repairing all eight
  findings, then one fresh round.
- **Figures** [Observed]. Re-derived at the reviewed commit by
  `scripts/build_pwb_opening_index_amendment.py --check`: 11 proposed
  subjects, 2 patched; 17 requirements and 53 scenarios. The manifest
  file's sha256 is the one on raw line 3, recomputed by
  `git show 0241fb83:<manifest> | sha256sum`.

Reviewed record: docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-1-RAW.md

## Dispositions

### 1 — the word-counting method is not judgment-free (revise)

**Accepted, open.** The method names neither the representation it counts
(served bytes or the post-load DOM) nor an exhaustive exclusion list, and it
drops a closed disclosure's visible `summary` text, against the delta's own
rationale. The offset base is also unstated.

Proposed repair: count over the post-load DOM in a named browser driver;
list every excluded element and attribute (`script`, `style`, `template`,
`noscript`, `hidden`, `aria-hidden="true"`, computed `display: none`, and
the content of a closed `details` other than its `summary`); define an
offset as the number of words before the target's first word.

### 2 — the stopping line has no presence, uniqueness or placement falsifier (revise)

**Accepted, open.** Proposed repair: place the line immediately after the
last-beginning target's first element, and add Falsifier and Oracle limbs
for a missing line, a second line, a misplaced line and a "largest offset"
that is not the largest.

### 3 — index targets are prose and have no stated recognizer (note)

**Open.** Proposed repair: bind each target to a machine identity the
renderer already emits (a group anchor or a claim category), and say which
element is "first". The two narrower targets the review names
(`unknown-or-contradiction` routes only to the Unknown aggregate;
`refusals-and-rule` routes to non-goals, not their rule text) go to the
owner with packet question 2.

### 4 — copy role and narrative-unit fit not reconciled with PWB-REQ-012 and PWB-REQ-014 (note)

**Open.** Proposed repair: state that PWB-REQ-012's one-instruction limit
applies only to the POC-bound statement, assign the unrendered row's text a
role, and say whether the index is a PWB-REQ-014 narrative unit or sits
outside the tree. Packet question 5 gains the PWB-REQ-014 half.

### 5 — register rows P-98 and P-99 absent at the reviewed commit (note)

**Open in the package; the rows land in this change.** [Observed] The rows
were added after the review, in a later commit on the same branch, so the
package sentence "P-98 is added by this change" is true of the change and
was false of the reviewed commit. The package is not edited.

### 6 — pair-checking and "do not overlap" overstate what was checked (note)

**Accepted, open.** The builder checks this package against each other
pending package, three of the six pairs, and P-85 and P-86 do overlap
outside the spec (design decision 12 and capability row 34). The reviewer
applied all 24 orders of the four spec patches to one identical result, so
the composition conclusion stands. Proposed repair: say "against each other
pending package", and drop "do not overlap" from the packet.

### 7 — replaced lines may lose signed text, and table targets are unpinned (note)

**Accepted, open.** The reviewer confirmed by hand that every replaced line
survives as a prefix in this version. Proposed repair, in the shared
engine: require each `replaced` signed line to survive as the prefix of a
proposed line, pin all nine table rows as required phrases, and add a
mutant for each.

### 8 — index rows may trip the distinct-name check if both packages are signed (note)

**Open.** Proposed repair: say in both packages that an index row's
accessible name names its question, so it cannot share a name with a group
heading's link.
