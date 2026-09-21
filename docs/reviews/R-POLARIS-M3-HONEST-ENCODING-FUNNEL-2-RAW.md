# R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW

Independent fresh-context review **2** of the M3 feature-request funnel packet
(bead `syzygy-dov.3`), its evidence record, and the P-70 note and row in the
pending-owner-decisions register. Read-only session: no file in any repository
or worktree was modified, no state-changing git command was run, no `bd` write,
no daemon, no network, no Butlers checkout read. The one file written is this
raw.

Review 1 is retained at `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md`
(F1–F14, verdict word copied exactly: **REVISE**, four blocking). This review
binds the bytes named below and no others (verification rule 10).

## Header — commit and reviewed bytes

Worktree: `…/scratchpad/m3wt`, branch `agent/syzygy-dov.3`, HEAD
**`573abb0`** (`573abb0 docs: Polaris M3 honest-encoding funnel packet, review 1
and P-70 owner questions [syzygy-dov.3]`). All four reviewed files are tracked
at that commit; `git diff a9f671e 573abb0 --stat` shows exactly those four,
2,531 insertions, no deletions.

Digests computed this session with `wc -c` and `sha256sum`, never transcribed
(verification rule 3):

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 102,085 | `bf526da8be926fdae5c58a525d1769b7fcf2d527920df45a6777f7caf6f560cf` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 30,747 | `5370f6cd2af1ff6c00f0625616e5b9c356bebf3a113175a74c8cd8e83d2ea6f5` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 29,780 | `cac255f552e198d318146c402d67e7118cdb1c5a2188cabdfd85dcff987d37e7` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md` (review 1, for reference) | 31,503 | `1eca5fbac6fe95266ac4968f5b55ebf89e6e63544441383c545fb89b9140bc1f` |

The packet's own record of review 1's size and digest (31,503 /
`1eca5fbac6…`) matches the retained bytes exactly [Observed].

Measurement inputs, digests recomputed this session before any sweep ran:

| Input | Bytes | sha256 | Matches the evidence record? |
|---|---|---|---|
| lane A after/tailnet Polaris capture | 1,484,487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` | yes |
| home capture | 38,706 | `c2fd6d1af7103e871c26dc65b76cc391fe2765a1c7391ac19ddf1656e57b5fca` | yes |
| trajectory capture | 244,524 | `fd802531b199084e7145932715150f4977335e49ca6aa168d68d5227c9d6ddde` | yes |
| orrery capture | 37,048 | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` | yes |

Sibling branches read read-only: M2 worktree `…/scratchpad/m2wt` at
**`1befd6f`** (the packet says `68123fc` — see G4); lane B
`origin/agent/syzygy-dov.17` at **`4090f98`**, as the packet states.

Every sweep below was re-run this session with Python `re` / `str.count` over
the named capture, never shell grep (verification rule 1). Denominators are
stated on every count.

## What re-derived clean

| Claim | Packet | Re-derived this session | Denominator / predicate |
|---|---|---|---|
| Claim-tuple spans, three methods | 713 / 713 / 713 | 713 / 713 / 713 | span-open regex, literal `str.count`, split-minus-one over the capture |
| Distinct claim ids | 703, 10 render twice | 703, 10 ids with count > 1 | 713 tuples |
| Label values | Observed 702, Unknown 11 | identical | 713 |
| Tier values | `report-fact` 702, `unstated` 11 | identical | 713 |
| Freshness / challenge | `fresh` 713 / `unchallenged` 713 | identical | 713 |
| `unknown-disclosure` blocks | 22 | 22 | the page |
| `class="unavailable-notice"` / `class="proposal"` | 0 / 0 | **0 / 0** | the page, literal `str.count` |
| `class="proposal-label"` | 1, at 56.29% | 1, at 56.29% | the page |
| Declared badge spans / in legend / in body | 2 / 2 / **0** | 2 (at 99.96% and 99.97%) / 2 / 0 | the page; legend bounded by `<ul class="legend">…</ul>` |
| Legend depth | 99.95%, char 1,481,009 | tag opens at char 1,481,009 | 1,481,819 chars |
| Body encodings: 735 = 713 + 22, of which **0** carry a declared class | 735 / 0 | 735 / 0 | the packet's stated three-family predicate |
| Cross-surface population | home 35, trajectory 299, orrery 18, Polaris 735; total **1,087**; declared **352** | identical | four pages, same predicate |
| Share carrying no declared encoding | 67.6%, all on Polaris | 735 / 1,087 = 67.6% | 1,087 |
| CSS rules naming `.claim-tuple` | 2 (base + mobile, letter-spacing and font-size only) | 2, declarations identical to the packet's description | the one served `<style>` block (1 block, 206 rules parsed) |
| Distinct colour treatments over the tuples | 1 (`var(--muted)`, `polaris.ts`:1307) | 1 | 713 |
| Selectors on `claim-tuple[`, `[data-epistemic-label`, `[data-epistemic-tier`, `[data-epistemic-freshness`, `[data-challenge-state` | 0,0,0,0,0 | **0,0,0,0,0** | served stylesheet, literal substring probes |
| Rules using `var(--unknown)` / `var(--cyan)` | 5 / 17, one cyan rule the declared Observed encoding | 5 / 17, 1 | served stylesheet, parsed |
| First-reading boundary | char 281,986, 19.03% | identical | first `data-polaris-group="catalog"` |
| First reading: tuples / Unknown tuples / disclosure blocks | **126 / 0 / 0** | 126 (all Observed) / 0 / 0 | 126; 22 blocks page-wide |
| Word "Unknown" in the region's visible text | 14, none a rendered state | 14 | the region, tags and script/style stripped |
| First rendered Unknown / first Unknown tuple / whole-shape Unknown | 25.55% / 25.70% / 57.72% | identical | — |
| The 11 Unknown tuples' composition | 9 withheld source claims, 1 class aggregate, the whole-shape claim | identical, enumerated by claim id | 11 |
| "No member claim carries an Unknown reason." | 8 | 8 | the page |
| Item attributes | 409 `data-polaris-item="`, 417 bare, 8 `data-polaris-items` | 409 / 417 / 8 | the page |
| Item rows matched to a tuple by claim id, and their labels | 409 / 409, **0** Unknown | 409 / 409 matched, 0 unmatched, 0 Unknown | 409 |
| Source rows | 278, 9 Unknown | 278 (`claim:source:` tuples: 269 Observed + 9 Unknown = 278) | 278 |
| Glossary state sentences / describing an unrendered value | 15 / 9 | 15 at `polaris-copy.ts` 34–51 (3 label, 7 tier, 4 freshness, 1 challenge, 3 group labels interleaved); 6 values render, so 9 | 15 |
| Sibling surface states + `challenge-pending` on the capture | 0 / 0 / 0 / 0 | **0 / 0 / 0 / 0** | the whole 1,481,819-character page, literal `str.count` |
| ΔE76 full matrix over the 9 distinct declared colours | 36 pairs, 7.85 third-smallest, smallest 3.98 | **identical, all 36 recomputed** | CIE76 over CIE Lab, D65, sRGB, from the hex at `design-tokens.ts` 46–55 |
| ΔE76 over the 5 foreground tokens | 7.85 smallest, 26.74 next | identical, all 10 recomputed | `{--cyan, --amber, --unknown, --muted, --ink}` |
| Contrasts | amber:unknown 1.109; unknown on void/panel 11.93/11.21; muted on void/panel 7.23/6.79; cyan:unknown 1.035; ΔE cyan↔unknown 64.85 | all identical | WCAG 2.x relative luminance |
| `--amber` and `--focus` the same value | yes | both `#f1b85b` | — |
| Byte arithmetic | over target 84,487; under ceiling 612,665; per-tuple alternative 16,366 | 1,484,487 − 1,400,000 = 84,487; 2,097,152 − 1,484,487 = 612,665; 702×19 + 11×18 + 702×4 + 11×2 = 16,366 | — |
| Lane B hoist | `data-epistemic-label` **409 of 713**; `data-challenge-state`/`data-evaluation-id` 713; net saving 188,902; `textBytesRemoved` 25,397; 409 × 32 = 13,088 | identical, read from `hoistedPerField`/`estimates` in `docs/evidence/pwb-laneb-strict-scope-estimate-2026-09-14.json` (container mode) at `origin/agent/syzygy-dov.17` `4090f98` | 713 tuples; ` data-epistemic-label="Observed"` is 32 bytes; 713 − 409 = 304; 409/713 = 57.4% |
| Lane B quotes | the inheritance rule and "same for every claim under one enclosing scope" | both verbatim in `proposed/spec.md.patch` (diff-marker interleaved; a full-phrase grep misses them) | — |
| Register rows | main's last note at `a9f671e` is P-67; P-68 only on lane B, P-69 only on M2 | `git show a9f671e:…/PENDING-OWNER-DECISIONS.md` returns **0** hits for P-68/P-69/P-70 | — |
| Register open count | 22 open + 5 acceptance = 27 | **22 + 5 = 27**, by the file's own stated predicate (split on `## `, match at line start a row whose first cell is `P-` followed by anything but a cell break) — `P-25(c)` included | 27 |
| `git diff f4589e2..a9f671e` over `apps`/`packages` | no home, Trajectory, Orrery, `page-shell.ts` or `design-tokens.ts` source | confirmed: 31 files, every changed app file Polaris-named plus `package.json`/`tsconfig.json`, plus the new `packages/polaris-generation-core` | 31 files |
| Governance battery | `0 FAIL` | ran `python3 scripts/check_governance.py` in the worktree: **`32 OK, 20 WARN, 0 FAIL (52 checks)`** | 52 checks |

**Code-level citations, each read at `573abb0`.** `polaris.ts` 306–307 (both
mints, consecutive) ✓; 1307 (`.claim-tuple … color: var(--muted)`) ✓;
1328–1329 (`.proposal`, `.proposal-label`) ✓; 536 and 555
(`unknownRoutes(item.claim, '')`) ✓; `claimStatesBlock` spans **346–361** with
the tier group at 356 and the freshness group at **357** ✓.
`surface-routes.test.ts` 64–101: `const denominator = pages.length` at 82, two
`String.includes` probes at 85–86, `continue` at 91,
`consistent > 0 && <= denominator` at 95–96 ✓. `cross-cutting.test.ts` 47–64:
`const denominator = pages(model)` at 50, iterates `EPISTEMIC_ENCODING`, and
the only rendered markup it reads is
`/<span class="epistemic (epistemic-\w+)">/g` at 58 ✓ — F11's restatement is
exact. `walkthrough-preflight.ts` `claimStrength` **203–226** ✓ (but see G2).
`polaris-first-reading.test.ts` 96–99 ✓. `polaris-copy.ts` 34–51 ✓, freshness
sentences **46–49** ✓. `design-tokens.ts` `EPISTEMIC_ENCODING` 16–29 ✓,
`DESIGN_TOKENS_CSS` colour tokens 46–55 ✓.
`project-shape-model.ts` `itemClaim` 374–379 with the three arms at 376/377/378
✓, and `SUSPENDED = RENDERING_TIERS[5]` at line 169, i.e. `'suspended'`, one of
RFC2-25's closed six — **F3's "contradiction is returned to the tier table" is
correct against the bytes**. `staleness.ts` 18 (`FRESHNESS_STATES`) ✓ and the
`no-bound-declared` arm at 98–103 returning no `freshness` field ✓.

**Clause anchoring re-checked at the named file and line, quoted against the
bytes (rule 8).** VIS-2 `vision.md`:96 ✓; VIS-7 :183 ✓ (F12 repaired — no added
bold); CC-VIZ-1 `performance-and-visual-discipline.md`:48 ✓ (repaired);
CC-VIZ-3 :74 ✓; POC-REQ-060 spec line 927, Case/Observable/Oracle/Oracle-
independence/Falsifier and the line-948 scenario ✓ verbatim; POC-REQ-061 line
966 ✓ (repaired); PWB-REQ-007 line 439, Case and Falsifier ✓ (repaired);
PWB-REQ-016 line 864 and its falsifier at 882–883 ✓ (repaired); PWB-REQ-020 line
902, Observable 915 and Falsifier 924–926 ✓; PWB-REQ-010 line 600 ✓; RFC2-25
`rendering-vocabularies.md`:153 ✓ verbatim with the source's own emphasis, and
its three-member sibling list at :169–170 ✓ verbatim; RFC2-10
`snapshot-and-evaluation-core.md`:209 ✓ verbatim **as far as it goes** — see G1;
RFC7-34 `rendering-and-surface.md`:241 with `applies_to: [polaris]` ✓ **but with
added emphasis** — see G3; the 2026-09-02 authorization's six escalation
triggers quoted verbatim from its "Escalation triggers" section (lines 86–94) ✓.
The warrants blocks: POC-REQ-060's at **955–964**, `contracts: [RFC6-18,
RFC6-22, RFC8-31]` — no RFC 0009 clause; POC-REQ-061's at **999–1008**,
`contracts: [RFC7-34, RFC8-31, RFC9-48]`; the `[RFC1-26, RFC6-20, RFC9-3,
RFC9-46, RFC9-48]` block at **920** closing the preceding Orrery requirement,
whose scenario ends at 914 ✓. **F1 is repaired exactly.**

All **28** code-span paths in the packet resolve in the worktree (sweep over
every backticked span containing `/` and ending in a tracked extension;
denominator 28, missing 0). No Butlers path appears in a backtick (probe over
`roster/`, `about/`, `butler.toml`, `v1.md`, `components.md`, `frontend.md`,
`MANIFESTO`: 0 hits). The four 64-character hexes in the packet are the
capture's, review 1's, and the reviewed packet's and evidence record's own
sha256s — no manifest digest, act argument or truncated signed digest is quoted.

## Findings

### G1 — blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:52, 277, 549, 1310 and `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:201 — RFC2-10 *does* supply the absence route the packet says it lacks, and Q2 forecloses a lawful arm on that false premise

**Defect.** The packet states four times, and the P-70 register row states once,
that RFC2-10 supplies no remedy for a condition outside its closed four:

- :52 (Q2 scope) — "RFC2-10 closes freshness at four and forbids the minting in
  terms … **supplying no absence marker at all**".
- :277 (Measurements) — "which is stricter than RFC2-25 and **supplies no
  absence remedy** (Gate 2)".
- :549 (Gate 2) — "RFC2-10 forbids the *minting* in terms … **and supplies no
  absence marker at all**".
- :1310 (the F4 disposition row) — "RFC2-25 supplies an absence remedy, RFC2-10
  forbids the minting in terms **and supplies none**, so arm (b) governs tier
  and is **not lawfully available for freshness**".
- Register row :201 — "(RFC2-10 forbids minting, spelling or force-fitting any
  value outside its closed four **and supplies no absence marker**…".

Read at `573abb0`, RFC2-10 runs from line 209 to line 223 of
`.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`.
Its lines 218–222 say:

> … a value existing in no vocabulary can be neither carried verbatim nor
> checked for parity, and leaving it unstated is how the value gets chosen by
> whoever implements the render first. A condition genuinely outside the four is
> disclosed as a fact of the render, never dressed as a freshness state.

That sentence *is* the absence remedy, stated in the clause the packet itself
cites — and it is the mirror of RFC2-25's "an untier'd claim renders at its bare
label", so the asymmetry the whole of Q2's freshness half rests on does not
exist in the form claimed. The packet's Gate 2 block quote (:531–536) stops at
"…a freshness value it does not carry" — one sentence and four lines short of
the remedy — and then draws a universal from the truncation. This is rule 8's
named failure mode (the clause is what the clause says, not where a quote was
cut) and rule 9's (an absence claim with no denominator over the clause's own
text).

Three consequences, in rising order of seriousness:

1. **A lawful arm is never put to the owner.** Q2's freshness limb offers only
   (b-i) "supply one of the closed four" and (b-ii) "hold the claim Unknown and
   do not render the tuple as though it had a freshness state". The clause's own
   route — disclose the condition as a fact of the render, in a carrier that is
   not `data-epistemic-freshness` and is not dressed as a freshness state — is a
   third arm, and it is the one an implementer reading RFC2-10 would reach for.
   The questionnaire invariant this packet is written against forbids calling a
   lawful arm unlawful.
2. **(b-ii) is self-defeating as written and cannot be chosen.** It says "not
   rendered as though it had a freshness state" and then, in the same sentence,
   "PWB-REQ-007's Falsifier … forbids simply omitting the field". It never says
   what (b-ii) *does*. Under RFC2-10's actual remedy the two halves reconcile —
   the field is not omitted and not dressed as a freshness state, because the
   render fact is a disclosure rather than a value; without the remedy the arm
   is an empty box. To be clear on the sub-question this review was asked:
   arm (b-ii) does **not** itself breach PWB-REQ-007's "a tuple field is
   absent/out of vocabulary" Falsifier — only the *omission reading* of it does,
   and the packet supplies no other reading. Whether PWB-REQ-007 requires a
   freshness field on a claim that no freshness state governs ("carry the closed
   label, tier … **that govern it**", spec :443–446) is itself the owner's
   question, and it is a good one; the packet asks it in the right place and
   then answers it for the owner on a false premise.
3. **Q2's freshness half stops being a gate.** The packet's own preamble (:41–44)
   says "Q2 settles a contract reading no agent may settle". The recommendation
   then settles half of it — "arm (b) is not lawfully available for the freshness
   field" — as a legal conclusion rather than a recommended answer among lawful
   arms. That is the difference between a genuine owner gate and an agent's
   ruling on contract meaning.

The clause is not obscure and the corroboration is one worktree away: **M2 at
`1befd6f` quotes this very sentence twice**, in its Q5 recommendation ("RFC2-10
closes the freshness vocabulary at four values and requires a condition outside
the four to be 'disclosed as a fact of the render'") and against its own Q7
("A condition genuinely outside the four is disclosed as a fact of the render,
never dressed as a freshness state" — and "no bound is declared" is a condition
outside the four, so `stale` here is a candidate for exactly that dressing).
P-69 and P-70 would therefore reach the owner giving contradictory readings of
one accepted clause, on the same day, from the same lane.

**Repair.** Quote RFC2-10 through line 222 in Gate 2. Withdraw "supplies no
absence marker at all" in all four packet locations and in the register row.
Restate the asymmetry as it is: RFC2-25 supplies a *rendering* remedy (the bare
label) inside the tuple; RFC2-10 supplies a *disclosure* remedy outside the
freshness slot, and forbids any value in the slot that the closed four do not
carry. Put the render-fact disclosure to the owner as a named arm alongside
(b-i), and state the live tension with PWB-REQ-007's Falsifier as the question
it is rather than resolving it. Say in Q7 or the collision section that M2's Q3,
Q5 and Q7 rest on the same sentence, so the two packets are read together.

### G2 — non-blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:905–919 (slice 5, "The readiness gate this slice regenerates under") — the preflight does not require the `unstated —` sentence, and an existing test does

**Defect.** The slice states: "A generated glossary that drops the lede id, the
strengthen sentence, or the `unstated —` sentence — which Q2 arm (b) makes
tempting to delete — breaks readiness without breaking any test slice 5 writes."
Both halves of the `unstated` limb are false against the bytes.

`apps/three-surface-poc/src/walkthrough-preflight.ts` lines 212–217 build the
required-term set from the model, not the render:

```
214:    if (claim.epistemic.tier !== undefined) terms.add(claim.epistemic.tier);
215:    if (claim.epistemic.freshness !== undefined) terms.add(claim.epistemic.freshness);
```

`unstated` is never a model value — it is not in `RENDERING_TIERS`, and
`polaris.ts` line 306 mints it at render time precisely *because*
`claim.epistemic.tier` is `undefined`. So the term never enters `terms`, line
219's `${term} —` loop never asks for it, and deleting the `unstated —` sentence
leaves `claimStrength` green. Meanwhile
`apps/three-surface-poc/src/polaris-first-reading.test.ts` **line 88**
hard-codes `'unstated —'` in a literal list of fifteen required terms, and lines
96–99 sweep the rendered values — so deleting it fails an existing test that
slice 5 is already extending.

The other four preflight requirements the slice states (exactly one
`<details id="polaris-claim-states"`, the lede id exactly once, the
`states.strengthen` text, `aria-describedby` on every tuple) are all accurate at
205–224, and the file *is* a binding unchanged input to slice 5 — F6's repair is
right in substance. Only the `unstated` example points the implementer at the
wrong guard, and it is the example the packet chose to make the point vivid.

**Repair.** Move the `unstated —` case to `polaris-first-reading.test.ts` line
88 as the guard that actually holds it, and keep the preflight's own three
examples (lede id, strengthen sentence, `aria-describedby`) for the readiness
claim. Mutant (f) is unaffected and correct as written.

### G3 — non-blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:574–576 and :1318 — F12 is not fully repaired, and the disposition row asserts the opposite as fact

**Defect.** The RFC7-34 block quote reads:

```
574: > Every such distinction is recoverable **without colour, position, or
575: > layout** — by label, text, or structure; **visual encodings are legended
576: > and mean exactly what the legend says (VIS-7)**; every curated diagram has
```

Read at `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`
lines 241–243, the source bolds `without colour, position, or layout` and
nothing else in that span:

```
242: **without colour, position, or layout** — by label, text, or structure; visual
243: encodings are legended and mean exactly what the legend says (VIS-7); every
```

So the second bold is added emphasis inside a verbatim quote of an accepted
contract clause — the exact defect F12 names, surviving in the clause Q6 rests
on. Worse, the F12 disposition row (:1318) states as fact: "RFC2-25's and
RFC7-34's bolding matched the source and is untouched". RFC2-25's does (:153–157
verbatim, checked). RFC7-34's does not. Review 1 asserted the same thing and was
wrong; the repair table copied it forward rather than checking, which is how a
review's own error becomes a packet's claim about bound bytes.

Every other F12 target is genuinely repaired: PWB-REQ-007 ×2, PWB-REQ-016 ×2,
VIS-7, CC-VIZ-1 and POC-REQ-061 now carry only the source's own bold (a sweep
over every `^> ` line containing `**` in the packet returns 20 spans; all but
these two match their source).

**Repair.** Drop the added bold at :575–576, or mark it "(emphasis added)".
Correct :1318 to say RFC2-25's bolding matched and RFC7-34's did not.

### G4 — non-blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:1134, 1138, 1147 and the F7 row — the M2 head is stale a third time, and one thing M3 relies on did change

**Defect.** The packet records M2 at **`68123fc`** ("re-read this session … M2 is
at `68123fc` … and has **six** slices"), and the F7 row says the head was
"re-derived past the review". M2's branch and the sibling worktree are both at
**`1befd6f`** ("docs: Polaris M2 funnel packet — review 4 retained and J1–J8
repaired [syzygy-dov.2]"). `git -C <m2wt> diff 68123fc 1befd6f --stat`:

```
 .../decisions/PENDING-OWNER-DECISIONS.md           |   7 +-
 docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md | 180 ++++++--
 ...ris-m2-evidence-currency-funnel-2026-09-14.json |  29 ++
 .../R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-4-RAW.md | 489 +++++++++++++++++++++
 4 files changed, 662 insertions(+), 43 deletions(-)
```

Checked against M2's current bytes, **the structural collision survives**: M2
still has six slices; slice 6 still touches only
`apps/three-surface-poc/src/polaris-reading.ts` line 44 and `polaris.ts` lines
506–510 (its Gate 3 row :365), neither of which any M3 slice touches; Q5 is
still "**Mark, do not delete**"; the two-file overlap (`polaris-copy.ts` 46–49
and `claimStatesBlock` line 357) is unchanged; P-69's register row keeps its Q5
and Q7 wording. So M3's collision conclusion and recommended sequence hold at
`1befd6f`, exactly as the packet says they held at `68123fc`.

Two things did move, and one of them matters:

1. **M2's review 4 (J3) put RFC2-10's "disclosed as a fact of the render, never
   dressed as a freshness state" sentence into M2's Q7 and Q5.** That is G1's
   clause, arriving in the sibling packet after M3's head was recorded. M3's
   flat contradiction of it is now visible in one `git diff`.
2. **M2's J4 weakened its slice-1 marker** to "the reason it is unreachable
   **and, where one exists,** the route that would make it reachable (slice 1's
   `superseded` marker has a reason and no route, by design)", and states that
   its copy oracle "enforces the marker, not the route". M3 slice 5 (:921–926)
   and collision item 1 (:1156–1159) still say M2 "edits each unreachable one to
   carry the reason it is unreachable **and the route**", and require slice 5 to
   carry "those markers … as a per-row *reachability* field". A per-row field
   designed for reason-plus-route will be one field short for `superseded`.

**Repair.** Restate the head as `1befd6f`, note review 4 and J1–J8, and state
that the shared surface and the sequence are unchanged. Weaken slice 5's and
collision item 1's description of the marker to "the reason and, where one
exists, the route", so the per-row field matches what M2 will actually produce.
Fold G1's cross-packet contradiction into Q7 or the collision section.

*Note on this class.* The head has now been stale in three consecutive readings
(`ec30494` → `e0ecdc8` → `68123fc` → `1befd6f`), each time correct when written.
A branch head is the one figure in this packet that cannot be made durable by
re-deriving it; citing M2 by row (P-69) and by the two overlapping files, and
naming the head only once with its date, would stop paying this cost.

### G5 — non-blocking — `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:201 (P-70, Q4) — the row states a depth the packet does not, and attaches it to the wrong object

**Defect.** The row's Q4 reads: "surface the whole-shape Unknown and the one
class-level Unknown in the opening band with their routes (both already exist on
the page, at **57.72% and 25.55%** depth)". The packet's own Measurements table
(:227–229) and slice 3 (:802–804) put the class-level roster-identity Unknown
**tuple** at **25.70%**; **25.55%** is the first Unknown-*disclosure block*, a
different object in a different family, which slice 3 does not name as one of
the two claims the band would carry.

Re-derived this session over the capture: first `class="unknown-disclosure"`
occurrence at 25.55%; first `data-epistemic-label="Unknown"` tuple —
`claim:class:roster-identity` — at 25.70%; `claim:project-shape` at 57.72%. The
packet is internally consistent; the register row is not.

**Repair.** "at 57.72% and 25.70% depth" in the row.

### G6 — non-blocking — Gate 2 and Gate 5 — RFC2-26 is never named, and it is the clause that decides Gate 5's hardest question

**Defect.** Gate 2 opens "Cited by identifier and quoted from the defined
location, per verification rule 8", and cites RFC2-25 and RFC2-10 from
`RFC-0002`. It does not cite **RFC2-26**, four clauses later in the same module
(`rendering-vocabularies.md`:196–205):

> **RFC2-26.** This contract schedules nothing: **it is not a specification of
> record from which implementation work may be scheduled**. No implementation
> work for user-observable consequences of this contract — evaluation and
> snapshot displays, claim and challenge rendering, Unknown-reason and
> rendering-tier presentation, reconciliation-chain and gap surfaces, API
> answers over epistemic state — may be scheduled solely from this RFC. Before
> implementation, every observable consequence either maps to an approved
> OpenSpec requirement and scenario in the governance root's `openspec/**`
> plane, or carries a reviewed N/A judgment proving it purely structural with
> no independently testable behavior.

Slices 5 and 6 are "rendering-tier presentation" and "Unknown-reason …
presentation" in that list, and Gate 5 :1044–1054 is precisely the paragraph
asking whether they map to an approved OpenSpec requirement — it concludes they
are "governed instead by CC-VIZ-1 … POC-REQ-061's legend-to-encoding falsifier
and VIS-7", labelled `[Inferred]`, and discloses the reading under which they
acquire a POC delta. That answer survives RFC2-26 (POC-REQ-061 is an approved
OpenSpec requirement and its falsifier is the map), so this is a gap in the
citation, not in the conclusion. But a packet that quotes the six escalation
triggers verbatim and anchors ten other clauses by line should not leave the one
clause that states the obligation Gate 5 is discharging unnamed, and a reader
checking Gate 5 against RFC-0002 will find it.

**Repair.** Cite RFC2-26 at `rendering-vocabularies.md`:196 in Gate 2 and name
POC-REQ-061 as slices 5–6's mapping requirement in Gate 5, so the discharge is
explicit rather than implied.

### G7 — editorial — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:315, 331, 986 and the evidence record's `pairs_below_26_74` — "below 26.74" is 0.003 off its own floor

**Defect.** The packet says "seven sit below 26.74" and "seven of the 36 pairs
over the nine distinct declared colours sit below 26.74", and its rank table
lists `--ink ↔ --muted` at 26.74 as rank 8. Recomputed to six decimals this
session, that pair is **26.737101**, which is strictly below the literal number
26.74; on the stated predicate the count is eight, not seven.

The packet's *intent* — the seven pairs below the `--ink`↔`--muted` floor — is
exactly the enumeration it gives (3.98, 4.82, 7.85, 8.78, 14.96, 19.56, 23.27),
and the slice-6 bar (ΔE76 ≥ 26.7) is unaffected, since 26.7371 ≥ 26.7. This is a
rounded figure used as a predicate, in a packet whose own F2 repair is about
predicates.

**Repair.** State the floor as the pair, not the rounded number: "seven pairs
sit below the `--ink` ↔ `--muted` floor (26.74 to two decimals, 26.7371
computed)". Same in `pairs_below_26_74` / `pairs_below_26_74_enumerated`.

### G8 — editorial — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:54 (Q4) — a doctrine quote with no anchor, applied to a different subject

**Defect.** Q4's recommendation cites "`trust-and-evidence.md` puts staleness
'on the primary surface, not buried in drill-down'". The phrase is verbatim
(`.syzygy/governance/doctrine/trust-and-evidence.md`:101–102), but it is cited
with no line or clause identifier — the only such citation in a packet whose
Gate 2 says it cites by identifier per rule 8 — and its subject is *an
observation record whose evaluation has been superseded*, not an Unknown. Q4's
on-point warrant (CC-VIZ-3, anchored at :74) does the work; this one is an
analogy carrying a doctrine file's name.

**Repair.** Anchor it (`trust-and-evidence.md`:101) and say it is cited by
analogy, or drop it and rest Q4 on CC-VIZ-3 and VIS-2, which is where its force
actually comes from.

### G9 — editorial — `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:201 (P-70, Q3) — the row softens a cost the packet states as a lower bound

**Defect.** The row states arm (b) of Q3 as "a non-hoistable per-claim carrier
costing lane B **about** 13,088 bytes". The packet (:53 and :1196–1202) says
"**at least** 409 × 32 = **13,088** attribute bytes of its 188,902-byte
estimate" and, in collision item 2, "plus a text component this packet has not
separated out [Inferred: the estimate's `textBytesRemoved` is 25,397 across all
seven fields and is not broken down per field in the record]". "About" drops
both the lower-bound qualifier and the disclosed unquantified component, so the
arm reads cheaper in the register than in the packet — the one place a
sequencing trade-off between two queued rows should not drift.

**Repair.** "costing lane B at least 13,088 attribute bytes plus an unseparated
text component" in the row.

## F1–F14 verification against the current bytes

| # | Severity (review 1) | Claimed disposition | Verified this session | Verdict |
|---|---|---|---|---|
| F1 | blocking | warrants claim withdrawn; both blocks quoted at 955–964 and 999–1008 | Both blocks read and quoted verbatim at those lines; POC-REQ-060 `contracts: [RFC6-18, RFC6-22, RFC8-31]`, POC-REQ-061 `[RFC7-34, RFC8-31, RFC9-48]`; the line-920 block belongs to the Orrery requirement (scenario ends 914, POC-REQ-060 heading 927). RFC9-46 bridge dropped; conclusion restated as "RFC9-48 only, through POC-REQ-061" | **REPAIRED** |
| F2 | blocking | population named, full 36-pair matrix recomputed, seven below 26.74, bar restated over five foreground tokens | All 36 pairs recomputed independently and identical; 7.85 is rank 3; the foreground ten enumerated with 7.85 smallest and 26.74 next; both JSON fields now carry predicates; the `--focus` 0.00 disclosure added; review 1's own five-pair miscount corrected in place with `--line`↔`--void` at 23.27 named | **REPAIRED** (see G7 for a 0.003 precision nit on the stated threshold) |
| F3 | blocking | sibling framing dropped, RFC2-25:169 quoted, family renamed "render disclosures", contradiction returned to the tier table | RFC2-25:169–170 quoted verbatim with the source's emphasis; all three sibling states and `challenge-pending` re-swept at **0 occurrences** over the whole page; `project-shape-model.ts`:377 confirmed to return `SUSPENDED = RENDERING_TIERS[5] = 'suspended'`, inside the closed six. **The family mints nothing**: not a fourth epistemic label, not a seventh tier, not a fourth sibling state — and RFC2-25's own distinguishing criterion supports it, since sibling surface states "*replace* a status rendering" (:188) while the proposal label accompanies narrative material. The invented quotation is gone | **REPAIRED** |
| F4 | blocking | RFC2-10 quoted at :209, Q2 scope extended to freshness, arm (b) ruled unavailable there, closure moved to served output, mutant (e), S9 limb, collision item 3 | The mechanical half is repaired and correct: lines 306–307 shown together, the closure assertion moved to served output with the tuple count as denominator, mutant (e), S9's second limb and collision item 3 all present and sound. **The reasoning half is not**: the RFC2-10 quote stops four lines short of the clause's own absence remedy, and the "supplies no absence marker" universal built on that truncation is false — see **G1** | **PARTIAL** |
| F5 | non-blocking | 713/22 split stated in five places | Split present in Q1, the Motif, the cross-surface table, the funnel summary and the Q1-other-way paragraph, with the served `.unknown-disclosure` rule quoted; both counts re-derived (713, 22) | **REPAIRED** |
| F6 | non-blocking | preflight added to Gate 3 row, `claimStrength` requirements stated, Gate 6 item 6, mutant (f) | All four present; `claimStrength` 203–226 confirmed and four of the five stated requirements exact. The `unstated —` example is wrong — see **G2** | **PARTIAL** |
| F7 | non-blocking | M2 restated at `68123fc`, six slices, slice 6's files named, shared surface unchanged | Accurate as to `68123fc`; M2 is now `1befd6f` — see **G4**. The substance (six slices, slice 6's two files untouched by M3, Q5 unchanged) still holds at the new head | **PARTIAL** |
| F8 | non-blocking | 346–361 with line 357, in all three places | `claimStatesBlock` confirmed at 346–361, freshness group at 357; all three citations (Q7 :57, Gate 3 row :673, collision item 2 :1160) updated | **REPAIRED** |
| F9 | non-blocking | RFC2-10 is the authority; `staleness.ts`:18 the implementation's echo | RFC2-10 quoted in Gate 2 and named as authority in the vocabulary table and slice 5; `staleness.ts`:18 (`FRESHNESS_STATES`) retained and labelled | **REPAIRED** (the quote is short — G1) |
| F10 | non-blocking | `unavailable-notice` 0 and `proposal` 0 disclosed; live reuse 22 + 1 | Both re-derived as **0**; `unknown-disclosure` 22, `proposal-label` 1, legend badges 2; disclosed in both Measurements and Q6 | **REPAIRED** |
| F11 | editorial | restated in the review's terms | `cross-cutting.test.ts` 47–64 read: it iterates `pages(model)` **and** `EPISTEMIC_ENCODING`, asserts every rendered `epistemic-*` class is in the table, and the only markup it reads is the legend's own span pattern at line 58. The packet's restatement is exact | **REPAIRED** |
| F12 | editorial | added bold removed from all five quotes of bound text | Removed from PWB-REQ-007 ×2, PWB-REQ-016 ×2, VIS-7, CC-VIZ-1, POC-REQ-061 — verified against each source. **Not removed from RFC7-34**, and the disposition row asserts it matched the source — see **G3** | **PARTIAL** |
| F13 | editorial | 46–55 in the evidence record | `colour_method` and `declared_colour_token_set.source` both read "lines 46-55"; `design-tokens.ts` 46–55 is exactly the ten colour tokens | **REPAIRED** |
| F14 | editorial | 34–51 in the slice and the Gate 3 row | Both cite 34–51 with the composition stated; `polaris-copy.ts` 34–51 confirmed as the 15 state sentences plus three interleaved group labels | **REPAIRED** |

Totals: **9 REPAIRED, 5 PARTIAL, 0 NOT REPAIRED.** Of the four blocking
findings, three are fully repaired and F4's reasoning half is not.

## Per-question assessment (Q1–Q7)

| Q | Scope truthful? | Genuine owner gate, or engineering judgment dressed as one? | Recommendation follows? | Register row matches the packet? |
|---|---|---|---|---|
| **Q1** — conformance with POC-REQ-060, or a narrow reading | **Yes.** 735 / 0 / 713 / 22 / denominator 4 / 1,087 / 352 / 67.6% all re-derived exactly, each with its denominator. The F5 split is carried through and does sharpen the question rather than soften it | **Genuine gate.** A conformance ruling on signed spec text is VIS-4's; the packet declines to decide it and writes the other arm down with its most uncomfortable consequence intact ("'Unknown looks the same everywhere' satisfied by a page on which Observed and Unknown look the same as each other"). No smoothing | **Yes.** Follows from POC-REQ-060's Case ("the denominator is that population", quoted verbatim at :936–938) and verification rule 4. Gate 5 is right that neither arm creates a spec delta | **Yes** |
| **Q2** — `unstated` in two closed-vocabulary fields | **Tier half yes; freshness half no.** The mint is re-derived exactly (11 / 0), lines 306–307 are quoted from the bytes, and the hazard one branch away is real (`staleness.ts` 98–103 returns no `freshness`). But the clause reading the freshness half rests on is false — **G1** | **Tier half: genuine gate**, correctly put, with RFC2-25's own bare-label remedy argued *against* the recommendation rather than hidden. **Freshness half: not a gate as written** — it hands the owner a legal conclusion ("not lawfully available") derived from a truncated quote, in the question the packet itself says no agent may settle | **Tier: yes**, and six-rows-plus-absence is the right consequence. **Freshness: no** — a lawful arm (RFC2-10's own render-fact disclosure) is absent, and (b-ii) is an empty box without it | **Row repeats the false premise** ("and supplies no absence marker") — G1 |
| **Q3** — inheritance vs a non-hoistable per-claim carrier | **Yes.** 409 of 713, 188,902, 32-byte attribute, 13,088, 304, 57.4% all re-derived against `hoistedPerField` at `4090f98`; both lane B quotes verbatim in `proposed/spec.md.patch` | **Borderline, correctly put.** The CSS mechanism is engineering; what makes it the owner's is that arm (b) spends a saving already before the owner as P-68, which the packet says in those words. Both arms called lawful; arm (b) is "available and honest" | **Yes.** The dual-selector design, the "expand scopes before counting" discipline and the denominator-equality assertion are the direct consequences, and they close the silent drop to 304 | **Substance yes; the cost is softened** — G9 |
| **Q4** — a real Unknown in the opening band | **Yes.** 126 tuples all Observed, 0 disclosure blocks, 14 word-occurrences none a rendered state, first Unknown at 25.55% / 25.70%, whole-shape at 57.72% — all re-derived | **Genuine gate, thinly.** VIS-2 and CC-VIZ-3 press one way but do not compel the band; what the owner's first stop opens with is a product decision. The alternative is called "coherent", never unlawful. The framing leans hard ("the least honest part of it") but leaves the arm standing | **Yes.** Nothing is fabricated — both claims exist on the page and the change is reading order; the position oracle is the right test and the four "No member claim…" sentences are explicitly left true | **No — the row's depth figure is wrong and mislabelled** (G5) |
| **Q5** — extend the table to tier, freshness and challenge | **Yes.** 12 states in prose with no treatment, 15 glossary sentences, 9 describing unrendered values, 0 with a visual treatment — all re-derived; the composition (3/7/4/1) confirmed at `polaris-copy.ts` 34–51 | **Genuine, and honestly bounded.** CC-VIZ-1 compels a legend *for encodings you add*, not the adding, and the packet does not claim otherwise; Gate 5's disclosure of the reading under which slices 5–6 acquire a spec delta and queue behind P-68 remains the packet's best paragraph | **Yes** for generation-from-one-table (it closes POC-REQ-061's falsifier in both directions by construction) and for M2's markers as a per-row field. Six-row tier constraint right. The four-row freshness constraint now asserts over served output, which is correct — but its justification inherits G1, and the per-row field is one slot short of M2's current marker (G4) | **Yes** |
| **Q6** — a `--proposed` token in a render-disclosure family | **Yes, now.** The one-sentence defect re-derived (one `proposal-label` at 56.29% in `var(--unknown)`); five rules / four meanings / two rendering zero times all re-derived; the ΔE76 bar carries its population and the ground-token exclusion is argued. The vocabulary framing is repaired and correct | **Genuine gate.** One token, four declared meanings, VIS-7's legend limb and RFC7-34's Polaris-binding form. The alternative — keep one token and legend the reuse — is explicitly called lawful under CC-VIZ-1, which is the right posture | **Yes.** The family mints nothing into any closed vocabulary (verified against RFC2-25:169–170 and :188, and `project-shape-model.ts`:377), the bar is measurable and computed from the token values, and RFC7-28 is cited as analogue rather than warrant. The RFC7-34 quote carries added emphasis (G3) | **Yes** |
| **Q7** — sequencing against P-69 and P-68 | **Yes on the mechanism, stale on the head.** The two-file overlap, line 357, M2's marker-then-generate ordering and "P-68 first" all check out at M2's current head; the head hash is one commit stale for the third consecutive reading (G4) | **Genuine, and modest.** Both orders are lawful; the packet says so and rests the recommendation on cost (the copy oracle written twice), not legality. "No M3 slice opens a PWB specification package until P-68 is ruled" is the correct conservative floor | **Yes.** Consistent with M2's own Q6 and with P-68's register row. Collision item 3 (M2 decides the value, M3 guards the vocabulary) is a genuinely useful pairing — and would be stronger once G1 is repaired, since M2 and M3 currently read the same clause opposite ways | **Yes** (the row wisely states no head hash) |

## Cross-checks the brief asked for

**(b) The seven questions in the packet against the P-70 row, clause by clause.**
Q1, Q5, Q6 and Q7 match in scope, arms, recommendation and every figure. Q2
matches — including the false premise, which the row carries verbatim (G1). Q3
matches except for the softened cost (G9). Q4's substance matches; one of its
two depth figures does not (G5). The row's default-if-unanswered clause is
complete and states all six standing conditions. The register's arithmetic is
correct by its own stated predicate: 22 open + 5 acceptance-act = 27, with
`P-25(c)` counted.

**(c) The collision section against the M2 packet at `1befd6f` and lane B at
`4090f98`.** Lane B is exactly where the packet says. M2 is one commit ahead
(G4). Nothing M3 *structurally* relies on changed between `68123fc` and
`1befd6f` — six slices, slice 6's two files, Q5's "mark, do not delete", the
two-file overlap and P-69's Q5/Q7 wording all hold — but M2's review-4 repairs
introduced two things M3 should carry: the RFC2-10 sentence at the centre of G1,
and the weakened slice-1 marker ("and, where one exists, the route") that M3's
per-row reachability field must accommodate.

**(d) What a fresh reader would find wrong.** G1 is the one that matters: a
reader who opens `snapshot-and-evaluation-core.md` at the line the packet cites
and reads eleven lines further finds the sentence the packet says is not there,
and finds M2 quoting it in the next worktree. G2, G3 and G5 are the kind a
reader checking the packet's own citations finds in minutes. G6 is what a reader
checking Gate 5 against RFC-0002 finds. Everything else in the packet stands up
to re-derivation: **every load-bearing measurement in this packet re-derived
exactly**, including all 36 ΔE76 pairs, the three-method tuple count, the
1,087-member cross-surface population under a declared predicate, the 409/409
by-id item sweep, the 409-of-713 lane B hoist, the byte arithmetic and the
governance battery. The measurement work and the act analysis are not the
problem; one truncated quote is.

## Questionnaire invariant

| Invariant | Held? |
|---|---|
| Problem scope holds against the project's shape and engineering bar | Yes for Q1, Q3, Q4, Q5, Q6, Q7; **no** for Q2's freshness half (G1) |
| Recommendation holds | Yes for Q1, Q3, Q4, Q6, Q7; Q5 yes with G1 and G4 inherited; **no** for Q2's freshness half |
| No owner trade-off smoothed into consensus | Held everywhere except Q2's freshness half, where a lawful arm is folded into an unlawful one (G1) |
| No lawful arm called unlawful | **Breached once** — G1 |
| Every substantive claim labelled | Yes: `[Observed]`, `[Inferred]` and `[Unknown]` used throughout; the two readings the packet relies on (PWB-REQ-020 presentation-not-fact, POC-REQ-060 scope) are both labelled `[Inferred]` with the consequence of the other reading stated |
| Contract claims quoted at a defined clause | Yes, with one clause truncated before its operative sentence (G1), one clause carrying added emphasis (G3), one anchor missing (G8) and one clause missing (G6) |
| Zero/all claims carry a predicate and a denominator run this session | Yes — every one re-derived here with its denominator, including the four zero-probes on the stylesheet and the four zero-counts on the sibling states |
| Digests computed, never transcribed | Yes — `wc -c` and `sha256sum` on every file above; the capture digest verified before any sweep |
| No manifest or truncated signed digest outside the raws | Held — the four full hexes are the packet's own artifacts |
| No Butlers path in backticks | Held — 0 hits |
| Every code-span path resolves | Held — 28 of 28 |
| `python3 scripts/check_governance.py` ends `0 FAIL` | Held — `32 OK, 20 WARN, 0 FAIL (52 checks)` at `573abb0` |

## Summary

The measurement work in this packet is exceptional and survives a second
independent re-derivation without a single discrepancy — all 36 ΔE76 pairs, the
three-method tuple count, the 1,087-member cross-surface population, the 409/409
by-id item sweep, the lane B hoist figures, the byte arithmetic and the
governance battery. Eleven of review 1's fourteen findings are repaired cleanly,
and three of its four blocking findings are fully discharged, F3's repair
notably so: the render-disclosure family mints nothing into any closed
vocabulary, and RFC2-25's own "replace a status rendering" criterion supports
the reframing better than the packet claims.

The one blocking defect is inherited from F4's repair rather than created by it.
RFC2-10 supplies exactly the absence route the packet says four times it lacks —
"A condition genuinely outside the four is disclosed as a fact of the render,
never dressed as a freshness state" — eleven lines below the line the packet
cites and four lines below where its quote stops. On that truncation the packet
forecloses a lawful arm, leaves arm (b-ii) an empty box, converts half of a
declared owner gate into an agent's ruling on contract meaning, and sends the
owner a reading of one accepted clause that contradicts the reading in the
sibling packet queued beside it. It is a one-paragraph repair and the
recommendation for the *tier* field survives it untouched.

Findings by severity: **1 blocking** (G1), **5 non-blocking** (G2–G6),
**3 editorial** (G7–G9).

Verdict: REVISE
