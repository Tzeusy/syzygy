# R-POLARIS-M3-HONEST-ENCODING-FUNNEL-1-RAW

Independent fresh-context review of the M3 feature-request funnel packet
(bead `syzygy-dov.3`). Read-only session; no file in any repository or
worktree was modified.

## Header — commit and reviewed bytes

Worktree: `…/scratchpad/m3wt`, branch `agent/syzygy-dov.3`, HEAD
`a9f671e` (`a9f671e docs: Polaris lane A measurement evidence and
independent review [syzygy-dov.1]`). Working tree carries exactly the two
untracked files under review; nothing else is modified.

| File | Bytes (`wc -c`) | sha256 (`sha256sum`) |
|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 71,765 | `a5e4cc4f6aaf40031131dda2c8366e931f5bea7a8a2b9a45e2ec5da41d2a6383` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 16,677 | `886cf48ef0e11c7ed72033b8334b1f61fd8db71cd3af5c5a3e97e2aeff9fb7ea` |

Capture and comparison inputs, digests recomputed this session (rule 3):

| Input | Bytes | sha256 | Matches packet? |
|---|---|---|---|
| lane A after/tailnet Polaris capture | 1,484,487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` | yes |
| home capture | 38,706 | `c2fd6d1af7103e871c26dc65b76cc391fe2765a1c7391ac19ddf1656e57b5fca` | yes |
| trajectory capture | 244,524 | `fd802531b199084e7145932715150f4977335e49ca6aa168d68d5227c9d6ddde` | yes |
| orrery capture | 37,048 | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` | yes |

Sibling worktrees read read-only: M2 at `…/scratchpad/m2wt` (HEAD
**`e0ecdc8`**, not the packet's `ec30494` — see F7); lane B at
`…/scratchpad/laneb` (HEAD `4090f98`, as the packet states).

## What re-derived clean

Every sweep below was re-run this session with Python `re`/`str.count`
over the named capture, never shell grep (rule 1). Denominators stated.

| Claim | Packet | Re-derived | Denominator/predicate |
|---|---|---|---|
| Claim-tuple spans, three methods | 713 / 713 / 713 | 713 / 713 / 713 | span-open regex, literal split, `class="claim-tuple"` count over the capture |
| Distinct claim ids | 703 (10 render twice) | 703, 10 ids with count > 1 | 713 tuples |
| Label values | Observed 702, Unknown 11 | identical | 713 |
| Tier values | `report-fact` 702, `unstated` 11 | identical | 713 |
| Freshness / challenge | `fresh` 713 / `unchallenged` 713 | identical | 713 |
| Distinct tuple shapes | 2 | 2 | 713 |
| CSS rules naming `.claim-tuple` | 2 (base + mobile, no colour change) | 2, identical declarations | the one served `<style>` block |
| Distinct colour treatments over the tuples | 1 (`var(--muted)`) | 1 | 713 |
| Selectors keyed on `claim-tuple[`, `[data-epistemic-label`, `[data-epistemic-tier`, `[data-epistemic-freshness`, `[data-challenge-state` | 0,0,0,0,0 | 0,0,0,0,0 | served stylesheet, literal substring probes |
| Declared badge spans on Polaris / in legend / in body | 2 / 2 / 0 | 2 (at 99.96% and 99.97%) / 2 / 0 | the page; legend bounded by `<ul class="legend">…</ul>` |
| Legend depth | 99.95%, char 1,481,009 | tag opens at char 1,481,009 | 1,481,819 chars |
| Cross-surface body encodings | home 35, trajectory 299, orrery 18, Polaris 735; total 1,087; declared 352 | identical | four pages, the packet's stated three-family predicate |
| Share carrying no declared encoding | 67.6%, all on Polaris | 735/1,087 = 67.6% | 1,087 |
| Checker denominator | `pages.length` = 4, `String.includes`, `continue`, `consistent > 0 && <= denominator` | confirmed at `apps/three-surface-poc/src/surface-routes.test.ts` lines 64–100 | — |
| First-reading boundary | char 281,986, 19.03% | identical | first `data-polaris-group="catalog"` |
| First reading: tuples / Unknown tuples / Unknown-disclosure blocks | 126 / 0 / 0 | 126 (all Observed) / 0 / 0 | 126; 22 blocks page-wide |
| Word "Unknown" in the region's visible text | 14, none a rendered state | 14 | — |
| First rendered Unknown / first Unknown tuple / whole-shape Unknown | 25.55% / 25.70% / 57.72% | identical | — |
| "No member claim carries an Unknown reason." | 8 | 8 | the page |
| Item attribute occurrences | 409 (`data-polaris-item="`), 417 bare substring, 8 `data-polaris-items` | 409 / 417 / 8 | the page |
| Item rows matched to a tuple by claim id, and their labels | 409/409, all Observed | 409/409 matched, 409 Observed, 0 unmatched | 409 |
| Source rows | 278, 9 Unknown | 278, Observed 269 / Unknown 9 | 278 |
| Glossary state sentences / describing an unrendered value | 15 / 9 | 15 (3 label + 7 tier + 4 freshness + 1 challenge, `polaris-copy.ts` 34–51); 6 values render, so 9 | 15 |
| ΔE76 `--amber`↔`--unknown` | 7.85 | 7.85 | CIE76, CIE Lab D65, recomputed from the hex values |
| ΔE76 `--muted`↔`--ink` | 26.74 | 26.74 | same |
| ΔE76 `--cyan`↔`--unknown` | 64.85 | 64.85 | same |
| Contrast `--amber`:`--unknown` | 1.109 : 1 | 1.109 | WCAG 2.x relative luminance |
| `--unknown` on `--void`/`--panel` | 11.93 / 11.21 | 11.93 / 11.21 | same |
| `--muted` on `--void`/`--panel` | 7.23 / 6.79 | 7.23 / 6.79 | same |
| `--amber` and `--focus` the same value | yes | both `#f1b85b` | — |
| Rules using `var(--unknown)` / `var(--cyan)` | 5 / 17, one cyan rule declared-Observed | 5 / 17, 1 | served stylesheet |
| Byte arithmetic | over target 84,487; under ceiling 612,665 | 1,484,487 − 1,400,000 = 84,487; 2,097,152 − 1,484,487 = 612,665 | — |
| Per-tuple alternative cost | 16,366 | 702×19 + 11×18 + 702×4 + 11×2 = 16,366 | — |
| Lane B hoist | `data-epistemic-label` 409 of 713; net saving 188,902; 409 × 32 = 13,088 | identical in `docs/evidence/pwb-laneb-strict-scope-estimate-2026-09-14.json` at `4090f98`; ` data-epistemic-label="Observed"` is 32 bytes | — |
| Lane B quotes | inheritance rule and "same for every claim under one enclosing scope" | both verbatim in `proposed/spec.md.patch` (line-wrapped; a full-phrase grep misses them — the corpus's own wrapped-citation class) | — |
| Register rows | main's last note P-67; P-68 only on lane B; P-69 only on M2 | confirmed on all three branches | — |
| `git diff f4589e2..a9f671e` over `apps`/`packages` | no home, Trajectory, Orrery, `page-shell.ts` or `design-tokens.ts` source | confirmed: every changed app file is Polaris-named plus `package.json`/`tsconfig.json`; new `packages/polaris-generation-core` only | 31 files |
| Governance battery | "32 OK, 20 WARN, 0 FAIL (52 checks)" | ran `python3 scripts/check_governance.py` in the worktree: **`32 OK, 20 WARN, 0 FAIL (52 checks)`** | 52 checks |

Clause anchoring re-checked at the named file and line, quoted against the
bytes (rule 8): **VIS-2** `vision.md`:96 ✓; **VIS-7** :183 ✓; **CC-VIZ-1**
`performance-and-visual-discipline.md`:48 ✓; **CC-VIZ-3** :74 ✓;
**POC-REQ-060** spec line 927, its Case/Observable/Oracle/Falsifier and the
line-948 scenario ✓ verbatim; **POC-REQ-061** line 966 ✓; **PWB-REQ-007**
line 439, Case and Falsifier ✓; **PWB-REQ-016** line 864 and its falsifier
✓; **PWB-REQ-020** line 902, Observable and Falsifier ✓; **PWB-REQ-010**
line 600 ✓; **RFC2-25** `RFC-0002/rendering-vocabularies.md`:153 ✓
verbatim including "an untier'd claim renders at its bare label";
**RFC7-34** `RFC-0007/rendering-and-surface.md`:241 with
`applies_to: [polaris]` ✓; **RFC 0009** `applies_to: [orrery,
machine-clients]` in all four modules ✓; **RFC9-46** and **RFC9-27**
quoted verbatim ✓. The 2026-09-02 authorization's six escalation triggers
are quoted verbatim from its "Escalation triggers" section (lines 86–94) ✓,
and the 2026-09-05 continuation's family and date check out ✓.

All 27 code-span paths in the packet resolve in the worktree. No Butlers
path appears in a backtick. No manifest digest, act argument or truncated
signed digest is quoted; the one long hex in the packet is the capture's
own full sha256, recomputed here.

## Findings

### F1 — blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:~487 (Gate 2, "A scope note, stated rather than assumed")

**Defect.** The packet states, labelled `[Observed]`: "POC-REQ-060 and
POC-REQ-061 name RFC9-3, RFC9-46 and RFC9-48 among their own warrants". It
does not hold. Read at `a9f671e`:

- POC-REQ-060's own `warrants` block (immediately after its line-948
  scenario) is `contracts: [RFC6-18, RFC6-22, RFC8-31]` — **no RFC 0009
  clause of any kind**.
- POC-REQ-061's own block is `contracts: [RFC7-34, RFC8-31, RFC9-48]` —
  RFC9-48 only; **no RFC9-3, no RFC9-46**.
- The block carrying `[RFC1-26, RFC6-20, RFC9-3, RFC9-46, RFC9-48]` sits at
  spec line 920, i.e. it closes the **preceding** (Orrery) requirement, not
  POC-REQ-060, whose heading is line 927.

This is the classic "the yaml block above the heading belongs to the
heading" misread, and it is the sentence that establishes one of the two
routes by which RFC 0009 is said to reach this work. A false `[Observed]`
claim about digest-bound specification bytes is exactly the class this
corpus punishes.

**Repair.** Restate as: POC-REQ-061 names RFC9-48 among its own warrants;
POC-REQ-060 names none. Quote both `warrants` blocks. The conclusion the
paragraph reaches (RFC9-24/26/27 do not bind Polaris; RFC9-27's two-carrier
rule is a voluntarily adopted standard) is unaffected and in fact better
supported by the corrected reading — but the bridge must be stated as it is.

### F2 — blocking — packet ~line 264 (Measurements, "Token reuse") and slice 6; evidence JSON `token_reuse.smallest_deltaE76_between_any_two_named_tokens` / `next_smallest_deltaE76`

**Defect.** The packet's measurable bar for Q6 rests on "every other pair of
named tokens is ≥ 26.7" and "the next-smallest distance between any two
named tokens today", and the evidence record asserts
`smallest_deltaE76_between_any_two_named_tokens: 7.85`. Both are universals
over "named tokens" with no stated predicate, and both are false over the
declared token set. Recomputed this session over every named token in
`DESIGN_TOKENS_CSS` (excluding `--focus`, which duplicates `--amber`):

| Pair | ΔE76 |
|---|---|
| `--void` ↔ `--panel` | 3.98 |
| `--panel` ↔ `--panel-raised` | 4.82 |
| `--amber` ↔ `--unknown` | 7.85 |
| `--void` ↔ `--panel-raised` | 8.78 |
| `--panel-raised` ↔ `--line` | 14.96 |
| `--panel` ↔ `--line` | 19.56 |

So 7.85 is the third-smallest, not the smallest, and five pairs sit below
26.74. The figure only comes back as stated over the five foreground tokens
`{--cyan, --amber, --unknown, --muted, --ink}` — a population the packet
never names. This is rule 2 and rule 9 exactly: an "every other" claim whose
denominator is unstated and, as written, wrong.

**Repair.** State the predicate ("over the five tokens that carry
foreground meaning; ground tokens are excluded because adjacency is their
purpose"), enumerate the population, and re-derive: over that population the
floor is `--muted`↔`--ink` at 26.74 and 7.85 is the smallest. Correct the
two JSON fields to carry the same predicate. The ≥ 26.7 bar itself survives
and Q6's recommendation does not change.

### F3 — blocking — packet Q6 (question table) and "Slice 6 — A sibling-state family and a `--proposed` token"

**Defect.** Three linked errors put a **closed** vocabulary at risk:

1. *Invented quotation.* Q6 writes: RFC2-25 "makes sibling surface states
   'never fourth labels'". The quoted fragment appears nowhere. RFC2-25 says
   "**a tier** never becomes a fourth epistemic label", and its case 14 says
   "any **tier** rendered as a fourth label". The clause says this of tiers,
   not of sibling surface states. Rule 8 does not admit a paraphrase inside
   quotation marks attributed to a defined clause.
2. *Misassigned membership.* Slice 6 opens "A fourth declared family:
   sibling surface states … The one this page renders today is the proposal
   treatment". RFC2-25's surrounding text closes that family at **three**
   members — `dismissed-by-decision`, `unadopted-draft`, `editorial-draft`
   ("*Deliberately outside the registry — **three** sibling surface states,
   closed*", `rendering-vocabularies.md`:169) — and states they are "equally
   closed". Swept this session: the capture contains **0** occurrences of
   each of the three, and 0 of `challenge-pending`. The page renders **no**
   sibling surface state. The proposal rendering is RFC 0007's
   proposed-scenario material (the packet itself reaches for RFC7-28 four
   paragraphs later), not a member of RFC2-25's closed three. As written the
   slice instructs an implementer to add a fourth member to a closed
   three-member vocabulary — the same minting failure Q2 is drafted to
   prevent one family over.
3. *Internal contradiction.* The same sentence says "contradiction is
   reachable through slice 4's fixture", placing contradiction in the
   sibling family; slice 4 says contradiction renders tier **`suspended`**,
   which is inside the tier registry. Both cannot be true.

**Repair.** Drop the term "sibling surface states" from Q6 and slice 6, or
quote RFC2-25's three-member list and state explicitly that the proposal
treatment is *not* one of them and is not being added to that family. Name
the proposal treatment for what it is (a render disclosure governed by
RFC7-28/RFC7-34 and CC-VIZ-1), give it its own family name, and move
contradiction back to the tier table where slice 4 already puts it. Quote
"a tier never becomes a fourth epistemic label" verbatim if the clause is
cited at all.

### F4 — blocking — packet Q2 and Q5 / "Slice 5" (the closed-vocabulary guard is one line short)

**Defect.** Q2's problem scope is stated as "`unstated` sits in the **tier**
field of 11 rendered tuples". The renderer mints it in **two** fields, on
consecutive lines (`apps/three-surface-poc/src/polaris.ts`):

```
306:  const tier = claim.epistemic.tier ?? 'unstated';
307:  const freshness = claim.epistemic.freshness ?? 'unstated';
```

The freshness twin never fires on this capture (all 713 render `fresh`), so
the packet's measurements are right — but the governing clause there is
**stricter**, not weaker. RFC2-10 (`RFC-0002/snapshot-and-evaluation-core.md`:209):

> Logical freshness state — `fresh`, `stale`, `broken`, `superseded` —
> changes status and therefore participates in the VIS-7 identity test … .
> **Four values, closed.** The list changes only by amendment to this RFC;
> **no implementation may mint, spell, or force-fit a freshness value it
> does not carry.**

RFC2-25 forbids a new *tier*; RFC2-10 forbids the *minting* itself in
terms. And the hazard is live, not theoretical: M2's own Q7 records that
`assessCurrency`'s `no-bound-declared` arm returns **no** `freshness` field,
and M2 slice 5 routes freshness through it — the day that lands, line 307
mints a fifth freshness value on every unbounded class. Q5's recommendation
("four freshness rows (the closed four)") and slice 5's closure assertion
would not see it, because they assert over the declared table, not over the
renderer.

**Repair.** Extend Q2's scope sentence and its arms to the freshness field,
citing RFC2-10 at :209 verbatim, and say which arm governs there (arm (b)'s
absence treatment must cover both fields, or the owner must be shown that
freshness has no lawful absence marker under RFC2-10 and the field must
therefore be rendered or the claim held Unknown). Add a rule-6 mutant that
forces `claim.epistemic.freshness` undefined and asserts the page does not
emit a fifth `data-epistemic-freshness` value. Name the M2 slice-5
interaction in the collision section.

### F5 — non-blocking — packet Q1 and the "735 … 0" headline

**Defect.** "Polaris renders 735 body epistemic encodings and **0** of them
carry a declared encoding class" is true on the stated predicate (class name
drawn from `EPISTEMIC_ENCODING`), but 22 of the 735 are
`unknown-disclosure` blocks and the served rule for them is
`.unknown-disclosure { color: var(--unknown); border-left: 3px solid
var(--unknown); … }` — the declared Unknown **token**, under an undeclared
class. Those 22 are already visually distinct; the population that renders
indistinguishably is the 713 tuples. The packet's own measurement table
carries the rule, so the two halves are inconsistent rather than wrong.

**Repair.** In Q1 and the funnel summary, split the figure: 713 of 735 carry
no declared class **and no distinguishing treatment**; 22 carry the declared
Unknown token under an undeclared class (an ad-hoc styling of epistemic
state in POC-REQ-060's falsifier sense, and a legend-to-encoding gap, but
not an invisible one). It strengthens Q1 rather than weakening it.

### F6 — non-blocking — Gate 3, Gate 6 and slice 5: `walkthrough-preflight.ts` is never named

**Defect.** Slice 5 regenerates `claimStatesBlock`, which is the exact
artifact `apps/three-surface-poc/src/walkthrough-preflight.ts` binds. Read
at `a9f671e`, the preflight requires: exactly one
`<details id="polaris-claim-states"`; `id="polaris-claim-states-lede"`
present exactly once; a `"<term> —"` sentence in that block for every label,
tier, freshness and challenge value of every presented claim; the
`states.strengthen` text present; and `aria-describedby=
"polaris-claim-states-lede"` on every claim tuple. A generated glossary that
drops the lede id, the strengthen sentence, or the `unstated —` sentence
(which Q2 arm (b) makes tempting to delete) breaks PWB-REQ-021 readiness —
and the packet's Gate 3 file table, Gate 6 bar and out-of-scope list never
mention the file.

**Repair.** Add `apps/three-surface-poc/src/walkthrough-preflight.ts` to
slice 5's Gate 3 row as an unchanged-but-binding input, add the preflight to
Gate 6's re-run list, and add a rule-6 mutant that removes the strengthen
sentence from the generated block and confirms the preflight fails.

### F7 — non-blocking — "Collision and sequencing", M2 head

**Defect.** The packet records M2's branch head as `ec30494` and describes
M2 as five slices. M2 is now at `e0ecdc8` ("review 2 (REVISE) retained and
repaired; slice 6 added"), committed 2026-09-14 08:17:00 +0800 — 73 seconds
after this packet's own mtime (08:15:47), so the packet was correct when
written and is stale now. Checked against the current M2 bytes: the new
slice 6 ("A lapsed reviewed selection announces itself") touches
`apps/three-surface-poc/src/polaris-reading.ts` line 44 and
`apps/three-surface-poc/src/polaris.ts` lines 506–510, **neither of which
any M3 slice touches**, and M2's slice 1 wording and Q5 "mark, do not
delete" ruling are unchanged. So M3's collision conclusion and its
recommended sequence survive at `e0ecdc8`; only the head hash and the slice
count are stale.

**Repair.** Restate the head as `e0ecdc8`, note slice 6 and its two files,
and state that the shared surface is unchanged.

### F8 — non-blocking — Q7, Gate 3 slice-5 row and Collision item 2: the cited line range excludes the whole overlap

**Defect.** Three places cite the shared region as
`apps/three-surface-poc/src/polaris.ts` **lines 346–353**. Read at
`a9f671e`, `claimStatesBlock` spans lines **346–361**, and the lines the
slice actually regenerates — and the whole of the stated overlap with M2 —
are outside the cited range:

```
353:    ${sentence('states.observed')}
356:    ${group('states.tier', [...])}
357:    ${group('states.freshness', ['states.freshness.fresh', 'states.freshness.stale', …])}
358:    ${group('states.challenge', [...])}
359:    ${sentence('states.strengthen')}
```

The freshness group — the precise collision with M2 slice 1 — is line 357.
A reader following the citation lands on the lede and the Observed sentence
and sees no overlap at all.

**Repair.** Cite lines 346–361, or cite line 357 for the freshness overlap
specifically.

### F9 — non-blocking — slice 5's freshness closure is anchored to a source constant, not a clause

**Defect.** The vocabulary table cites "four freshness rows (the closed
four)" and the measurement table cites
`packages/cap1-core/src/staleness.ts` line 18 as the closure's source. A
source constant is an implementation, not an authority (rule 8, and rule 5's
"a citation is not a reliance"). The clause is RFC2-10 at
`RFC-0002/snapshot-and-evaluation-core.md`:209, which the packet never
cites. The tier family is anchored correctly (RFC2-25); freshness is not.

**Repair.** Anchor the freshness closure to RFC2-10 and quote it; keep the
source-constant citation as the implementation's echo, labelled as such.

### F10 — non-blocking — Q6's "five rules, four meanings" omits that two never render

**Defect.** Q6 says "Five CSS rules use that one token for four different
meanings". Confirmed: `.epistemic-unknown`, `.unavailable-notice`,
`.unknown-disclosure`, `.proposal`, `.proposal-label`. But on this capture
`.unavailable-notice` renders 0 times **and `.proposal` renders 0 times**
(the evidence JSON records both as 0; the packet's prose discloses only the
notice and lists "the proposal treatment and its label" as though both
render). The live collision is three renderings of two meanings — the
legend's 2 badge spans, 22 disclosure blocks, and 1 proposal label.

**Repair.** One clause in Q6: "five rules, of which two (`.unavailable-notice`,
`.proposal`) render zero times on this capture; the live reuse is the
disclosure block and the proposal label".

### F11 — editorial — `cross-cutting.test.ts` characterised as iterating pages "rather than encodings"

**Defect.** It iterates pages **and** the two entries of the declared table,
and additionally asserts every rendered `epistemic-*` class name is in the
table. Its defect is narrower and more precise than the packet's phrasing:
its denominator is `pages(model)`, and it enumerates the **declared table**,
never the rendered encoding population, so a page carrying 735 body
encodings in no declared class passes.

**Repair.** Restate in those terms.

### F12 — editorial — emphasis added inside verbatim quotes of bound text

**Defect.** Several block quotes add bold that is not in the source:
PWB-REQ-007 ("including fixtures for every admitted label…", "a tuple field
is absent/out of vocabulary"), PWB-REQ-016 ("without relying on color,
position or layout", "color/layout-only distinction"), VIS-7 ("every
encoding means what its legend says"), CC-VIZ-1 ("a legend stating exactly
what it means"), POC-REQ-061 ("a legend entry matching no rendered
encoding"). RFC2-25's and RFC7-34's bolding does match the source. Quoting
bound bytes with undisclosed emphasis is a small drift in exactly the
direction rule 8 guards.

**Repair.** Add "(emphasis added)" to each such quote, or drop the bold.

### F13 — editorial — evidence JSON `colour_method` names the wrong line range

**Defect.** `"…computed this session from the token hex values at
apps/three-surface-poc/src/design-tokens.ts lines 51-55"`. `--cyan`,
`--amber`, `--unknown` and `--focus` are lines 52–55, but `--ink` (46) and
`--muted` (47) are also in the measured pair table and lie outside the
range; line 51 is `--line`, which is not measured.

**Repair.** Cite lines 46–55.

### F14 — editorial — Gate 4 slice 5 cites `polaris-copy.ts` "lines 38–51"; the JSON cites 34–51

**Defect.** The 15 state sentences run 34–51 (the JSON is right: 3 label,
7 tier, 4 freshness, 1 challenge, with the three group labels interleaved).
Slice 5 as designed regenerates the label sentences too, so 38–51 understates
what is replaced by three lines.

**Repair.** Cite 34–51 in both places.

## Per-question assessment (Q1–Q7)

| Q | Scope truthful? | Genuine owner gate, or engineering judgment dressed as one? | Recommendation follows? |
|---|---|---|---|
| **Q1** — conformance or narrow reading of POC-REQ-060 | **Yes, with F5.** 735 / 0 / 713 / denominator 4 / 1,087 all re-derived. The 22 disclosure blocks already carry the declared Unknown *token*, which the headline flattens. | **Genuine gate.** A conformance ruling on signed spec text is VIS-4's, not an agent's, and the packet declines to decide it. The other arm is written down with its most uncomfortable consequence stated ("'Unknown looks the same everywhere' satisfied by a page on which Observed and Unknown look the same as each other") — no smoothing. | **Yes.** Follows from POC-REQ-060's Case (denominator = the population, quoted verbatim) and rule 4. Gate 5 correctly notes neither arm creates a spec delta. |
| **Q2** — `unstated` as out-of-vocabulary, absence marker, or amendment | **Incomplete — F4.** True of the tier field; silent on the identical mint one line below for freshness, where RFC2-10 is stricter. | **Genuine gate.** A reading of digest-bound PWB-REQ-007 against RFC2-25; arm (c) is correctly named as a CC-REV-2 amendment and never as a plan step. Arm (a) is presented as "RFC2-25's own remedy" — the packet argues against its own citation rather than hiding it. | **Yes for tiers**, and the six-rows-plus-absence constraint on slice 5 is the right consequence. Does not follow for freshness until F4 is repaired. |
| **Q3** — inheritance vs a non-hoistable per-claim carrier | **Yes.** 409/713, 188,902, 32-byte attribute, 13,088 all re-derived against lane B's record at `4090f98`. | **Borderline but correctly put.** The CSS mechanism is an engineering judgment; what makes it the owner's is that arm (b) spends 13,088 bytes of a saving already before the owner as P-68 — which the packet says in those words. Both arms are called lawful; arm (b) is "available and honest". | **Yes.** The dual-selector design and the "expand scopes before counting" discipline are the direct consequence, and the denominator-equality assertion is the guard against the silent drop to 304. |
| **Q4** — a real Unknown in the opening band | **Yes.** 126 tuples / 0 Unknown / 0 disclosure blocks / 14 word-occurrences / first Unknown at 25.55% all re-derived. | **Genuine gate**, thinly. Doctrine (VIS-2, CC-VIZ-3) presses one way but does not compel the band; what the owner's first stop opens with is a product decision. The alternative is called "coherent", not unlawful — the line is held. The framing ("makes the page's own first impression the least honest part of it") leans hard but does not remove the arm. | **Yes.** Nothing is fabricated — both claims exist on the page; the change is reading order, and the position oracle is the right test. |
| **Q5** — extend the declared table to tier/freshness/challenge | **Yes, with F4 and F9.** 12 states in prose with no treatment, 15 glossary sentences, 9 unreachable, 0 with a visual treatment — all re-derived. | **Genuine, and honestly bounded.** CC-VIZ-1 compels a legend *for encodings you add*, not the adding; the packet does not claim otherwise, and it discloses the reading (POC-REQ-060's scope) under which slices 5–6 would acquire a spec delta and queue behind P-68. That disclosure is the packet's best single paragraph. | **Yes** for generation-from-one-table (it closes POC-REQ-061's falsifier in both directions by construction) and for M2's markers as a per-row field. The six-row tier constraint is right; the four-row freshness constraint is a line short (F4). |
| **Q6** — a sibling-state family and a `--proposed` token | **Partly — F2 and F3.** The one-sentence defect is real and re-derived (the proposal label renders at 56.29% in `var(--unknown)`, the token the legend assigns to Unknown). The vocabulary framing and the ΔE76 universal are not. | **Genuine gate** on the substance (one token, four meanings, VIS-7's legend limb). The alternative arm — keep one token and legend the reuse — is explicitly called lawful under CC-VIZ-1, which is the right posture. | **Not as written.** The ≥ 26.7 bar survives with a stated predicate (F2), but "they enter the table as their own family" points an implementer at a closed three-member vocabulary (F3). Repair both before the owner sees it. |
| **Q7** — sequencing against P-69 and P-68 | **Yes, with F7 and F8.** The two-file overlap, M2's marker-then-generate ordering, and "P-68 first" all check out; the head hash is one commit stale and the line range misses the overlap. | **Genuine, and modest.** Both orders are lawful; the packet says so and rests the recommendation on cost (the copy oracle written twice) rather than on legality. "No M3 slice opens a PWB specification package until P-68 is ruled" is the correct conservative floor. | **Yes.** Consistent with M2's own Q6 and with P-68's register row. |

## Dossier coverage — section M3's five moves

Read `docs/pursuits/2026-09-13-vision-pursuit.md` lines 172–196.

| Dossier move | Packet disposition | Verdict |
|---|---|---|
| **L6-M1** — declared Observed/Unknown encoding on Polaris; replace the four-page checker with the sweep the requirement specifies | Slice 1 (declared encoding reaches the tuple, both selector forms) and slice 2 (population sweep with a reported denominator and an independent count) | **Covered.** Q1 and Q3 are the gates on it. |
| **S1-M2** — one real Unknown before the reader leaves the first reading | Slice 3 (opening band renders the whole-shape and class-level Unknowns in place with routes; position oracle) | **Covered.** Q4 is the gate. |
| **S4-M5** — exercise the per-item Unknown route with a fixture independent of live Butlers content | Slice 4 (two text-map variants in the app's own fixture module; reads no repository) | **Covered.** The scope note honestly records the residual gap (three of six tiers still unfixtured) rather than claiming PWB-REQ-007's Case met. |
| **S11-M1** — extend the encoding-table pattern to the seven tier, four freshness and one challenge values | Slice 5 (three declared tables, generated glossary) | **Covered, and corrected.** The dossier's "seven tier" is the `unstated` mint; the packet refuses it and routes it to Q2 as six rows plus an absence treatment — the right move, and better than the dossier. Incomplete only on the freshness twin (F4). |
| **S11-M2** — give proposed-not-authority its own token out of the no-evidence colour's way | Slice 6 (`--proposed` token at a measured distance) | **Covered in substance, defective in framing** — F2 and F3. |

No dossier move for M3 is dropped and none is left without a slice or an
explicit out-of-scope entry. The packet's "Out of scope, explicitly" list is
specific and does not quietly widen the move.

## Summary

The measurement work is the strongest part of this packet: every load-bearing
figure re-derived exactly, including the three-method tuple count, the
1,087-member cross-surface population under a declared predicate, the
409/409 item-row sweep with the by-id matching method the packet itself says
it had to correct, the ΔE76 arithmetic from the hex values, and the
byte arithmetic. The clause anchoring is careful and mostly verbatim, the
authorizing-act analysis is sound (six escalation triggers quoted and each
addressed), and Gate 5's "no slice needs a specification delta" is correct
and well argued. Four defects must be repaired before the owner reads it: a
false `[Observed]` claim about two requirements' warrants (F1), a false
universal about token distances that the evidence record repeats (F2), a
vocabulary misassignment that would have an implementer add a fourth member
to a closed three-member family (F3), and a closed-vocabulary guard that
stops one line short of a live RFC2-10 hazard (F4).

Findings by severity: **4 blocking** (F1–F4), **6 non-blocking** (F5–F10),
**4 editorial** (F11–F14).

Verdict: REVISE
