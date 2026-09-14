# Feature request M2 — Evidence currency: compute the horizon, wire `assessCurrency`, make the legend true

> **Candidate — binds nothing.** This is the feature-request funnel for the
> second move released from the 2026-09-13 vision pursuit. It proposes; the
> owner disposes (VIS-4). Nothing here authorizes implementation, and no bead
> becomes runnable by this file. Bead: `syzygy-dov.2`. Dossier:
> `docs/pursuits/2026-09-13-vision-pursuit.md`, section M2. It is written in
> the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and of the ruling
> that packet produced,
> `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`
> (the M1 ruling).

Date: 2026-09-14. Author: a funnel session (Claude), for the owner.

Size: **medium** for slices 1–4 and 6 (app and core renderer plus one
machine-payload field; observable behavior changes; no governed artifact
touched); **large** for slice 5 (it declares a currency bound, which RFC2-9
makes an authorization-bearing governance artifact, so it needs an owner act
and an independent review before that act).

Baseline: Syzygy `a9f671e` (main; the only working-tree change is a co-lead's
in-flight `AGENTS.md`, unrelated) [Observed]. The retained capture this packet
measures is the lane A *after* capture, tailnet host form, at Butlers
evaluation revision 2e3bac97790b, committed 2026-09-13T10:31:11Z and captured
2026-09-13T13:33:24.295Z: 1,484,487 bytes, sha256
`e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`
[Observed: computed this session; recorded in `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json`
beside this file].

## The seven questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1, Q2, Q6 and Q7 are owner gates in the strict sense:
Q1 decides whether today's rendering is conformant or in breach, Q2 decides
which act is needed, Q6 orders this move against a queued owner decision,
and Q7 is a vocabulary choice RFC2-10 says no implementer may make. Q3 and
Q4 are contract-determined on this packet's own reasoning — each has one
lawful arm and one arm that is unlawful or unauthorized — and are put to
the owner for confirmation and disclosure, not as free choices (review 1,
per-question table). Q5 is a real choice between two lawful arms; the
packet recommends one and says why (review 2 finding G9).

| # | Question | Recommended |
|---|---|---|
| Q1 | **Does the PWB model's standing argument — "the evaluation itself is the currency", so every project-shape claim is `fresh` with no declared bound — satisfy RFC2-9, or must each claim class declare a currency bound before its claims may leave Unknown?** The argument is a code comment at `packages/three-surface-poc-core/src/project-shape-model.ts` lines 162–166; RFC2-9 says the opposite in terms, and PWB-REQ-007 — the requirement that governs these exact tuples — names RFC2-9 among its own warrants (the `warrants` block at line 480 of the digest-bound spec lists `RFC2-9, RFC2-10`) [Observed]. | **A bound is required.** RFC2-9 is unconditional ("Every claim class must declare a currency bound … before any of its claims can leave Unknown"), and verification rule 8 does not admit an implementation's own reading of a clause as the clause. Rule that the current constant is a disclosed non-conformance to be repaired by slice 5, not a lawful reading — and that until the bound is declared and wired, the page keeps rendering `fresh` **only** because no act has yet authorized the bound, which Q5's legend marking must say out loud. |
| Q2 | **Where does the currency-bound declaration live, and under which act?** Arm (a): amend the adapter-registry entry `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` with a `currencyBounds` block beside `resourceLimits`, adopted by a fresh `adopt-registry-entry` act plus an implementation-authorization continuation. Arm (b): a separate bound-declaration artifact with a new act type, phrase and recorder. | **Arm (a).** It reuses an act phrase, a recorder, a `--check` and a precedent that all already exist (`decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, 2026-09-05), and the entry is already a snapshot input whose digest the daemon already binds. Arm (b) costs a new `_act_subjects()` registration, a new recorder and a new review, and buys separation the POC does not need yet. Two owner steps, both templated: the registry act, then the continuation in the shape of `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`. |
| Q3 | **Is the evidence horizon a second identified evaluation, or may it be folded into the pinned evaluation's freshness field (for example by rendering changed sources as `broken`)?** Disclosed for confirmation: on this packet's reasoning the folding arm is unlawful, not merely worse. | **A second identified evaluation, never a freshness value.** The ground is RFC2-10's evaluation scoping, not render-time drift: the probe is computed once at build, so folding would not make two reads disagree, but a changed source is a fact of a *different* evaluation, and RFC2-10 binds a claim's freshness to the evaluation that produced it, so a value sourced from a second evaluation would be a freshness state no run of the first could reproduce. The legend's own `broken` sentence ("its source changed since capture") describes exactly the probe's condition, which is why slice 1's `broken` marker must say the horizon is not its route (review 1 findings F3 and F4). Render the horizon as its own disclosed claim — a currency probe with its own identity, its own instant and its own tuple — and keep the pinned evaluation's 713 tuples byte-identical. |
| Q4 | **How is re-observation triggered?** Arm (a): an explicit operator route in the shape of the existing materialize route. Arm (b): a timer, poll or file watcher inside the daemon. Disclosed for confirmation: arm (b) is unauthorized today and would need its own act. | **Arm (a), no timer.** **No act found that authorizes a background poller**; it is new daemon behaviour and the 2026-09-02 authorization's "any scope beyond the signed change" trigger is the hook, so arm (b) is not available without a further owner act. The operator route needs none: it changes no consent, policy, registry or spec subject and rides the 2026-09-05 implementation-authorization continuation. Design argument: a human-triggered re-evaluation keeps re-observation an operator fact, not a background one, and every new `asOf` then has a new observation behind it (the inverse of L4-F4, where `asOf` moved with no observation). An earlier draft leaned on AGENTS.md's "no unattended agent coordination"; a single daemon's timer is not agent coordination, and that sentence is withdrawn (review 1 finding F5). |
| Q5 | **The legend promises three states the pipeline cannot produce. Delete them, or mark them?** Both arms are lawful: no clause requires a rendered glossary to carry vocabulary members no claim uses, and the walkthrough preflight requires only presented terms to be explained. | **Mark, do not delete.** RFC2-10 closes the freshness vocabulary at four values and requires a condition outside the four to be "disclosed as a fact of the render". Marking keeps the closed vocabulary visible to the reader and lets one copy oracle carry the legend through slice 5 without a second edit; deleting would make the page silent about three states the contract still defines, which is worse, not unlawful (review 2 finding G9). Mark each unreachable entry in place with the reason it is unreachable (no currency bound is declared; supersession is not modelled) and a route, guarded by a copy-oracle test. The walkthrough preflight permits this: it requires the glossary to explain every **rendered** term, not every vocabulary member. |
| Q6 | **Sequencing against the lane B package, and the honest target.** The scoped-attributes semantic delta (`syzygy-dov.17`, owner decision P-68) rewrites the same clause region of PWB-REQ-007 that M2's currency work reads. | **No M2 spec package is opened until P-68 is ruled.** Slices 1–4 and 6 touch no governed artifact and may run now; slice 5's registry act touches the registry entry, not the spec, so it also does not collide — but any *later* PWB spec text M2 wants must wait for P-68 and then rebase onto the amended bytes. Honest target: `data-epistemic-freshness` takes at least two distinct values over the rendered population at one evaluation, every legend sentence is either reachable or marked unreachable with its reason, and the page's first human-visible instant moves from 58.0% depth into the opening band. |
| Q7 | **What freshness value does a claim of a class with no declared currency bound render?** `assessCurrency`'s `no-bound-declared` arm returns `label: 'Unknown'` and reason `no-currency-bound-declared` but no `freshness` field [Observed: `packages/cap1-core/src/staleness.ts` lines 98–104]; PWB-REQ-007 requires freshness on every tuple; RFC2-10 closes the vocabulary at four and says "no implementation may mint, spell, or force-fit a freshness value it does not carry", so the choice may not be made by whoever implements the render first. Every class is in this arm until its bound is acted, so it is the arm reached first. | **`stale`, with primary reason `no-currency-bound-declared` kept distinct.** CAP1-REQ-062 puts an unbounded class under the same invariant as out-of-bound evidence ("SHALL NOT support a current or favourable answer") — both render Unknown, with distinct reasons — and assigns neither a freshness value; `fresh` is the defect M2 removes, a fifth value is forbidden, and omission is forbidden; `stale` is the one closed value whose legend sentence a reader can reconcile with "no bound is declared" once the reason sits beside it [Inferred]. Against this recommendation stands the RFC2-10 sentence this packet relies on for Q3: "A condition genuinely outside the four is disclosed as a fact of the render, never dressed as a freshness state" — and "no bound is declared" is a condition outside the four, so `stale` here is a candidate for exactly that dressing. It is still preferred because PWB-REQ-007 requires a freshness value on every project-shape tuple (its Falsifier: "a tuple field is absent/out of vocabulary"), so the disclosure route cannot discharge the slot on these claims the way it can for the probe, and the reason beside the value is the disclosure; the alternative does not escape the sentence either, it moves the same choice into the engine (review 4 finding J3). Alternative the owner may prefer: amend the engine's `no-bound-declared` return to carry an explicit freshness, which is a Capability 1 conformance change (CAP1-REQ-062) and needs its own CC-REV-2 route. Until Q7 is ruled, slice 5 cannot render any undeclared class. |

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine (heart-and-soul) | Yes, adopted: VIS-1…7, SEC-1…5 | VIS-2 (currency bound, no silent green), VIS-7 (every encoding means what its legend says; the identity test), plus `architecture.md`'s time-as-explicit-input paragraph and `trust-and-evidence.md`'s staleness section |
| Decisions (legends-and-lore) | Yes | P-52 (the eight-item POC cap — M2 runs under `syzygy-dov.2`, so no new POC bead is filed and P-52 stays untouched); the P-67 ruling's sequencing sentence; P-68, queued and unruled |
| Specification (openspec) | Yes, signed and digest-bound: `openspec/changes/polaris-project-wide-butlers-model/` | PWB-REQ-007 (the complete tuple and its currency scenario), PWB-REQ-006 (the registry's declared envelope), PWB-REQ-016, PWB-REQ-020 (parity), PWB-REQ-021 (the `claim-strength` answer identity), PWB-REQ-004 (the closed project-fact population slice 2's probe claim must stay outside). CAP1-REQ-062 governs Capability 1, not PWB, but owns the engine this move wires |
| Topology (lay-and-land) | Candidate bundle only | Nothing beyond the core-versus-app placement already in force |
| Craft (craft-and-care) | Yes, owner-approved | CC-TEST-5/6 oracles, rule-6 mutation evidence, retained evidence, independent raw review |

## Gate 1 — Motif

**Problem.** Polaris renders one freshness value and promises four. On the
retained capture every one of 713 claim-tuple spans carries
`data-epistemic-freshness="fresh"`, and the glossary sitting on the same page
explains `stale`, `broken` and `superseded` as though a reader might meet
them [Observed: three independent sweeps of the capture, agreeing; see
"Measurements" below]. Eleven of those 713 are `Unknown` claims at tier
`unstated` — claims no evidence reached — and they too are described to the
reader as "captured at this evaluation" [Observed]. Meanwhile
`packages/cap1-core/src/staleness.ts` lines 87–155 already contains
`assessCurrency`, a complete fail-closed currency judge, and nothing outside
`packages/cap1-core` and `packages/cap1-conformance` refers to it
[Observed: 0 references, two methods].

**The dossier's strongest M2 finding, re-measured.** L4-F1 in the dossier
said 135 of 402 rendered rows cite bytes that had changed since the
rendered evaluation (71 of 271 sources, measured at the pre-lane-A
capture against Butlers head 7c8743f63). Re-derived 2026-09-14 against the
retained lane A capture (evaluation revision 2e3bac97790b) and the Butlers
repository's head at measurement time,
2ef3858818fac3cb87b67009ba3884f46380359f (committed 2026-09-13T20:18:28Z),
by two methods each — the machine
capture's per-source blob ids against a `git ls-tree` of head, and a
`git diff --name-status` between the two revisions restricted to the
population; a self-check of the blob ids against the pinned revision's
tree returned 0 mismatches over 278 [Observed: the tree reads are Git
object metadata, paths and ids, of the already-consented repository; no
blob body was read]:

| Measure | Value | Denominator |
|---|---|---|
| Sources whose blob changed between the pinned revision and head | 15 | 278 |
| Sources removed | 0 | 278 |
| Machine items citing a since-changed source (anchor method / string method, agreeing) | 9 | 415 |
| Rendered item rows citing a since-changed source (rows matched to items by class and key; 0 unmatched; the 415 − 409 difference is the six `project-account-section` items, rendered once each as the account's own section rather than as item rows, see slice 3) | 9 | 409 |
| Of those, rendering `fresh` | 9 | 9 |

The number is smaller than the dossier's because the lane A capture is
eight hours newer than the one L4 measured and Butlers moved less in
between; the defect is unchanged in kind. Nine rows say "captured at this
evaluation" about bytes that have since moved, and the page has no field,
band or footnote in which that fact could appear. This is the empirical
basis for slice 2. (Added after review 1 finding F9.)

**Who.** The owner, whose PWB-REQ-021 cold open must answer "for one chosen
fact how strongly Polaris claims to know it and what would make that claim
stronger" — a question whose freshness half currently has one possible
answer; every agent that reads a Polaris tuple as evidence of currency; and
the next reader who opens the page days after the daemon started and meets no
instant of the evaluation until 58.0% of the way down.

**Success, falsifiable.**

1. At one evaluation with a declared bound and at least one out-of-bound
   fixture class, `data-epistemic-freshness` takes at least two distinct
   values over the rendered population, and the machine answer carries the
   same values for the same claim ids.
2. Every freshness sentence in the rendered glossary is either reachable at
   that evaluation or carries, in the rendered text, the reason it is not
   and, where one exists, the route that would make it reachable (slice 1's
   `superseded` marker has a reason and no route, by design). The copy
   oracle enforces the marker in both directions and does not test for a
   route (review 4 finding J4).
3. Re-reading one identified evaluation at two different wall-clock times
   yields a byte-identical page, and `asOf` does not advance without a new
   observation. A test mutates the clock and asserts both.
4. The first human-visible instant on the page appears before the first
   catalog section, and the page states how many sources have moved since the
   evaluation it renders — as a separately identified fact, not as a
   freshness value.
5. A reviewed reading selection whose pinned digest no longer matches
   renders the full declaration *and* a sentence saying the selection was
   withdrawn and why; a test asserts both halves, and a fixture with a
   matching digest renders the condensed form and no withdrawal sentence.

**Motif.** *A field whose domain is one value carries no status, and a legend
that names states the pipeline cannot produce is an unfaithful encoding.*
This is VIS-7's own violation clause ("an unfaithful heatmap") applied to a
four-valued vocabulary rendered as a constant.

**What M2 is not.** It is not a claim that the page is wrong about Butlers.
Every tuple's *label* and *tier* are earned; only the currency dimension is
unearned. And it is not a re-opening of the page-size question, though
it must state that question's arithmetic honestly [Observed: the lane A
measurement record `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`,
the M1 ruling's Q3 row and the 2 MiB ceiling, computed 2026-09-14]: the
page at the retained capture is 1,484,487 bytes through the tailnet mount
and 1,478,637 direct, which is 84,487 and 78,637 bytes **over** the M1
ruling's working target — its words are "1.4 MB"; the lane A record's
`q3Target.bytes` fixes it at 1,400,000, and that decimal figure is used
here — and 612,665 / 618,515 bytes under the 2,097,152-byte response
ceiling (2 MiB; the project writes it "2 MB"); of that ceiling headroom the
418–443 KB the M1 ruling reserves for the pending Butlers P-60/P-61 repairs
are read as 418,000 to 443,000 bytes on the same decimal convention. The
horizon band and the marked legend add bytes measured in hundreds
[Inferred: a projection about unbuilt code]. M2
neither closes nor materially widens the target gap, which is lane B's
subject (P-68). An earlier draft of this paragraph quoted "~479 KB of
headroom", a pre-lane-A figure under the ceiling, not the target; review 1
finding F1 corrected it.

## Measurements on the retained capture

All computed this session from the lane A tailnet capture named above
(1,484,487 bytes; 1,481,819 decoded characters) [Observed]. Counts are
computed, never transcribed; each freshness count was taken three ways
(attribute regex, literal split on the attribute name, and a parse of every
`<span class="claim-tuple">` opening tag) and all three agree.

| Measure | Value | Denominator |
|---|---|---|
| Claim-tuple spans on the page | 713 | the page |
| `data-epistemic-freshness` values rendered | `fresh` × 713 | 713 spans |
| Distinct freshness values rendered | **1 of 4** | the closed RFC2-10 vocabulary |
| Tuple shapes | `Observed · report-fact · fresh · unchallenged` × 702; `Unknown · unstated · fresh · unchallenged` × 11 | 713 |
| Distinct evaluation identities | 1 | 713 `data-evaluation-id` attributes |
| Freshness glossary sentences rendered | 4, each exactly once | 4 |
| Of those, unreachable in this pipeline | **3** (`stale`, `broken`, `superseded`) | 4 |
| ISO-8601 instants anywhere in the bytes | 719 | the page |
| …carried inside `data-evaluation-id` attributes | 713 | 719 |
| …visible to a human as text | **6**, two methods agreeing | 719 |
| Depth of the first human-visible instant | 58.0% (character 859,145) | 1,481,819 characters |
| `data-polaris-item="` attribute occurrences (the substring `data-polaris-item` alone counts 417, of which 8 are the distinct `data-polaris-items` attribute) | 409 | the page |
| Reviewed reading plans defined | 2 | `polaris-reading-plan.ts` |
| …rendering a condensed reading in the capture | 1 | 2 |

The six human-visible instants sit at 58.0–58.1% (two on the
revision/committed/captured `<small>` line at characters 859,145 and
859,189, and one at 860,858 in the authority-disclosure paragraph just
below it, a separate `<p><small>`), 99.7% (the walkthrough-judgment block,
two) and 100.0% (the footer) [Observed: re-derived 2026-09-14 after review
1 finding F14; an earlier draft put all three on one line]. No instant of this
evaluation appears in rendered text above 58% of the page [Observed: ISO
instants in text nodes, two methods; two `YYYY-MM-DD` strings occur earlier,
at 56.7% and 56.8%, both inside one cited source filename, and an earlier
draft's "no date at all" overstated this — review 2 finding G4]. This is
L4-F3 re-measured on the *post-lane-A* page: the trim
removed 625 KB of narrative JSON from the front of the document and the first
instant still does not appear until well past the halfway mark, so the
finding is a layout fact, not a byte-count artifact.

The reading-plan row is L4-F5's silence, caught in the act. Two reviewed
selections exist; one rendered condensed on this capture and one did not, and
**the page says nothing about the second either way** — a reader cannot tell
from the served bytes whether the selection lapsed against changed source
bytes, whether the underlying statement is one of the known whole-source
Unknowns, or whether no selection was ever offered for it. That ambiguity is
the finding; resolving which of the three it is here would not change the
design, because the design's whole point is that the page must say.

### Code sweeps (this session, two methods each)

- `assessCurrency` and `CurrencyBoundDeclaration` are referenced in exactly
  three source files: `packages/cap1-core/src/staleness.ts` and two
  conformance tests (a built declaration file under `packages/cap1-core`
  mirrors the first when a `dist/` tree is present; none is in this
  worktree). References from `packages/three-surface-poc-core` or
  `apps/three-surface-poc`: **0** [Observed: `grep -rF` over both trees, and
  a file-list sweep naming every file that contains the identifier].
- The only freshness value any non-test source under
  `packages/three-surface-poc-core/src` or `apps/three-surface-poc/src`
  assigns is `FRESH`, at `project-shape-model.ts` lines 185 and 193
  [Observed: a Python `re` sweep for `freshness:` assignments across both
  trees, and a sweep of every `FRESHNESS_STATES` index read, which finds one
  — index `0`, at line 167]. The literals `stale` and `superseded` do occur
  in `body-read-authority.ts` and `walkthrough-judgment.ts`, but as act- and
  judgment-lifecycle states in a different vocabulary, never as a
  `FreshnessState`.
- `packages/three-surface-poc-core/src/model.ts` lines 100–110 define the
  evaluation as `snapshot`, `snapshotLabel`, `inputsDigest` and `asOf`. There
  is no evidence or horizon field: a sweep for the term `horizon` across
  every non-test source in `packages/*/src` and `apps/*/src` returns one hit,
  and it is a comment about horizontally scrollable tables [Observed].
- `apps/three-surface-poc/src/main.ts` observes the repository once, at lines
  80–81, outside `buildModel` (line 113), and mints `asOf` from the wall
  clock inside it at line 134. `buildModel` is called at startup (line 187)
  and again only on materialize (line 201) [Observed]. So a materialize
  produces a page reading "captured &lt;now&gt;" over evidence pinned at
  process start — L4-F4, confirmed against current bytes.

## Gate 2 — Doctrine

Cited by identifier and quoted from the defined location, per verification
rule 8. VIS and RFC locations were resolved through `DIRECTIVE-REGISTER.md`
and then read; the register carries no spec-requirement family, so
CAP1-REQ-062 and PWB-REQ-007 were located by heading sweep in their own
spec files [Observed: `grep -c` of `CAP1-REQ` and `PWB-REQ` over the
register returns 0 and 0].

**VIS-2 — No evidence means Unknown, not success**
(`.syzygy/governance/doctrine/vision.md`:96). The clause says, in its own
words:

> No surface may declare a project aligned, converged, or genome-complete —
> nor turn anything green — without current evidence. … Currency is judged at
> a status evaluation's identified as-of instant (architecture.md) — the wall
> clock never silently changes a displayed status. Until a claim class
> declares its currency bound, its evidence is not current and the claim
> renders Unknown. *Violation:* "spec-aligned ✓" computed from a stale index;
> a stale view silently green; a status flipping with no new identified
> evaluation.

Two limbs bite. The third sentence is the one L4-F2 reports as bypassed: no
claim class in the PWB model declares a bound, and its claims nonetheless
render `Observed · report-fact · fresh`. The second sentence is L4-F4: `asOf`
advances from the wall clock on every `buildModel`, without a new
observation.

**VIS-7 — The observatory itself must be trustworthy**
(`.syzygy/governance/doctrine/vision.md`:183):

> The normative trust floor lives in trust-and-evidence.md: the deterministic
> layer of an observation record is identical across runs of one identified
> evaluation (source snapshot + as-of instant, architecture.md); every
> rendered internal project-entity link resolves to its identified target …;
> every encoding means what its legend says; no secret material appears in
> any surface or store. … *Violation:* a dangling internal link; an
> unfaithful heatmap; two runs of one identified evaluation disagreeing in
> the deterministic layer.

"Every encoding means what its legend says" is the legend slice in one
sentence: the page's legend says `stale` means "older than the declared
currency bound" when no bound is declared anywhere, and `broken` means "its
source changed since capture" when nothing in the pipeline can observe that.
The identity limb is why Q3 matters: a horizon read from the live repository
at render time would make two runs of one evaluation disagree.

**CAP1-REQ-062 — Stale evidence cannot silently remain current or
favourable**, defined at line 1837 of
`openspec/changes/project-registration-and-honest-shape-visibility/specs/project-registration-and-honest-shape-visibility/spec.md`:

> Evidence past its declared currency bound at the evaluation's as-of instant
> SHALL NOT support a current or favourable answer: the dependent claim
> renders `Unknown` with reason `stale-beyond-currency-bound`, and a claim
> class with no declared currency bound renders `Unknown` with reason
> `no-currency-bound-declared`. Staleness of superseded observations is
> visible on the primary surface. A displayed answer changes only through a
> new identified evaluation — never by the wall clock silently.

CAP1-REQ-062 governs Capability 1, not the POC, so it does not bind Polaris
directly. It matters three ways: it is the requirement `assessCurrency` was
built and conformance-tested against, so the engine M2 wires already has a
signed oracle; its second sentence is the design M2 proposes for the PWB
side; and its existence is L4-F2's "two halves of Syzygy disagree about the
same rule" — one half implements VIS-2's currency sentence exactly, the other
returns a constant.

**Supporting clauses, quoted at their defined locations.**

- RFC2-9, *The declaration mechanism*, at line 187 of
  `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:
  "Every claim class must declare a currency bound — how old its evidence may
  be and still count as current — before any of its claims can leave Unknown."
  And: "The bound declaration is itself an **authorization-bearing governance
  artifact** — it is the act that lets a claim class leave Unknown — and is
  therefore honored only under the owner-act provenance predicate (RFC3-16(a))
  … A currency bound present in the tree without an effective owner act does
  not unblock its class." This is the clause that makes slice 5 an owner act
  rather than an implementation detail, and it is the clause Q1 puts to the
  owner.
- RFC2-10, *Identity-bearing freshness* (same file, line 209): "Logical
  freshness state — `fresh`, `stale`, `broken`, `superseded` — changes status
  and therefore participates in the VIS-7 identity test: two runs of one
  evaluation must agree on every freshness state. … **Four values, closed.**
  … A condition genuinely outside the four is disclosed as a fact of the
  render, never dressed as a freshness state." This decides Q3 and Q5: the
  horizon is disclosed as its own fact, and the legend keeps all four values.
- `.syzygy/governance/doctrine/architecture.md`:221–229: "A wall clock never
  silently alters a displayed status: the passage of time changes a status
  only through a new identified evaluation, and it may only degrade a claim
  (toward stale or Unknown), never establish or improve one". And at 236:
  "Excluded from the identity test is only display formatting — localized
  timestamps and relative-age strings; extending that exclusion is a doctrine
  amendment." A relative-age string ("evaluated 3 days ago") is therefore
  lawful in the opening band with no amendment; a *count of changed sources*
  is not display formatting and needs its own evaluation identity.
- `.syzygy/governance/doctrine/trust-and-evidence.md`:97–104: an observation
  record "may still be displayed after its evaluation is superseded, but its
  staleness must be visible on the primary surface, not buried in
  drill-down". The clause's subject is a superseded record; the capture
  renders a current one, so the first instant at 58.0% depth is a
  legibility defect (success criterion 4 answers it), not the condition
  this clause forbids. The clause reaches M2 by extension [Inferred]: once
  the horizon exists, a changed-source count *is* staleness, and this
  clause puts it on the primary surface, which is slice 2's opening band.

**Conflict check.** None found. Every slice removes a false encoding or adds
a disclosed one; none turns anything green, none folds an Unknown into a
total, and slice 5 can only move claims toward Unknown, which is the
direction `architecture.md` permits. Slice 5 will make some claims render
Unknown that render Observed today — that is the point, and VIS-2 is the
warrant, but it is also why the owner is asked before, not after.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Legend truth | `apps/three-surface-poc/src/polaris-copy.ts` (lines 45–49), `polaris.ts` line 357, plus the copy-oracle test | none |
| 2 Evidence horizon | `apps/three-surface-poc/src/git-observation.ts` (a second head resolution), `main.ts` (a new operator route beside `materializeRoutes`), `packages/three-surface-poc-core/src/model.ts` (a `currencyProbe` block on the model), `polaris.ts` (the opening band) | none |
| 3 `evidence` block on the machine payload | `packages/three-surface-poc-core/src/model.ts`, `apps/three-surface-poc/src/routes.ts` (`/api/poc`, `/api/poc/polaris`) | none |
| 4 `asOf` immutability | `apps/three-surface-poc/src/main.ts` lines 113–134 plus one test | none |
| 6 Lapsed-selection announcement | `apps/three-surface-poc/src/polaris-reading.ts` (line 44, the digest mismatch return), `polaris.ts` lines 506–510 (the reading block), plus one test | none |
| 5 Currency bound + `assessCurrency` | `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`; `packages/three-surface-poc-core/src/project-shape-model.ts` lines 162–193, importing `assessCurrency` from `packages/cap1-core` | **the adapter-registry entry** — digest-bound by `decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` |

Boundaries crossed: none new. The `three-surface-poc-core → cap1-core` edge
already carries the freshness vocabulary (`project-shape-model.ts` lines
19–27 import `FRESHNESS_STATES` and `FreshnessState` from `@syzygy/cap1-core`);
slice 5 adds the judge that owns it to the same import. That is a
narrowing, not a widening — it replaces a private constant with the package
that already owns the vocabulary [Observed: the import line; corrected
after review 1 finding F8, which noted an earlier draft called this a new
boundary].

Not touched by any slice: the body-read authority gate, the observation
pipeline's classification and extraction stages, the registry's
`resourceLimits` values, the response ceilings, the consent act's pair and
content class, and the signed PWB specification text.

### The authorizing act, per slice

| Slice | Owner act needed | Named act |
|---|---|---|
| 1 Legend | **No** | rides `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05); no escalation trigger is crossed — no spec amendment, no security/privacy/retention change, no registry-envelope change |
| 2 Horizon | **No**, on the recommended design | same continuation. The live head resolution is a `git-revision` input, an input class the registry entry already declares. The implementation-authorization act's escalation trigger (`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, "Escalation triggers") is scoped to the content class and the repository ("any observation outside the consented content class or repository"); the consent act contributes the scope sentence naming "the Butlers revision the POC observes" and has no trigger section of its own (review 2 finding G6); the probe reads a ref of the already-consented repository, not a Git object of the source population at any revision, so no body read is added and the observation trigger is not crossed; the same section's envelope trigger ("a change to the constraints or envelope the registry entry declares") is not crossed either, because the head resolution is a `git-revision` read charged to no source-body limit and changes no declared `resourceLimits` value; the spec-amendment trigger ("an amendment to the signed PWB specification") is not crossed because the probe's count is an epistemically labeled claim under PWB-REQ-014, not a project fact, and PWB-REQ-004's closed population ("The POC SHALL admit project facts only from this closed population … an injected or unrecognized fact, class, key, catalog or account key SHALL mint nothing", lines 491–498) is neither entered nor amended — the probe mints nothing inside it (review 4 finding J1; if that reading is rejected the row flips to yes and slice 2 joins Q6) [Inferred: the design reads `rev-parse HEAD` only, exactly as `git-observation.ts` already does at line 61 and `main.ts` at lines 80–81; restated after review 1 finding F6 and review 3 findings H6 and H8] |
| 3 `evidence` block | **No** | same continuation; the machine payload's field set is not an act-bound artifact |
| 4 `asOf` immutability test | **No** | same continuation; it adds a test and removes a clock read |
| 6 Lapsed-selection announcement | **No** | same continuation; it adds one rendered sentence and one field on a render-time type, reads nothing new |
| 4b A timer or watcher, had one been proposed | **None found** | and none is recommended — see Q4 |
| 5 Currency bound | **Yes — two owner steps** | (i) a fresh `adopt-registry-entry` act over the amended entry's new digest, superseding `decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` for that role only; (ii) a plain owner direction continuing implementation authorization across the registry escalation trigger, in the shape of the 2026-09-05 continuation. RFC2-9 is the warrant for (i); the 2026-09-02 authorization's own trigger list ("a change to the constraints or envelope the registry entry declares") is the warrant for (ii) |

P-52 is not touched by any slice: all five run under `syzygy-dov.2`, the
pursuit bead, so no ninth POC item is filed. This is the same route the M1
ruling took for `syzygy-dov.1`.

## Gate 4 — Design sketch, per slice

### Slice 1 — Legend truth (medium; no act)

`polaris-copy.ts` keeps four freshness entries. Each unreachable one gains,
in its own rendered sentence, the reason and the route:

- `stale` — older than the declared currency bound. *Not reachable at this
  evaluation: no claim's freshness is judged against a currency bound — the
  model assigns a constant. Route: declare the bound in the registry, act on
  it, and route freshness through `assessCurrency` (slice 5).* (Worded so
  the reason stays true until slice 5 lands and false exactly when it does;
  review 2 finding G8.)
- `broken` — its source changed since capture. *Not reachable by design
  under the current evaluation model: this evaluation observes one pinned
  revision and carries no claim from an earlier one, so no claim of this
  evaluation can have a changed source. A changed source is a fact of a
  later evaluation and is reported by the evidence horizon as its own
  claim, never as this value; only a model that carries evidence across
  revisions, which M2 does not build, could reach it.* (This wording
  follows Q3: the horizon never sets a freshness value, so the marker must
  not promise the horizon as its route; review 1 finding F3.)
- `superseded` — a later evaluation replaced it. *Not reachable at this
  evaluation: the model carries no claim from an earlier evaluation.*

Marking, not deleting, keeps RFC2-10's closed vocabulary visible and keeps
the page honest in both directions: it stops promising a state, and it does
not pretend the state does not exist. The marker text is its own copy entry
with a distinctive string, per the copy-oracle guardrail that a short label
is "reached" by coincidence and proves nothing.

The walkthrough preflight permits this without change:
`apps/three-surface-poc/src/walkthrough-preflight.ts` lines 212–220 collect
the terms of the *presented* claims and require `"<term> —"` in the glossary
block, so extra entries are allowed and no rendered term loses its
explanation [Observed].

**Copy-oracle test.** For each of the four freshness values: if the value
occurs in `data-epistemic-freshness` anywhere on the page, its glossary
sentence must carry no unreachable marker; if it does not occur, its sentence
must carry one. That is a single invariant over the rendered bytes, and it
keeps the legend true as slice 5 lands, without a second edit.

### Slice 2 — The evidence horizon (medium; no act)

A **currency probe** is a second identified evaluation with one job: resolve
the repository's current head and compare it to the pinned revision the model
renders. It carries its own identity, of the form
`evaluation:pwb-currency-probe:<instant>`, its own instant and its own tuple,
and under PWB-REQ-014's three claim roles ("anchored project fact,
explicitly non-normative framing, or epistemically labeled claim") it is an
**epistemically labeled claim** and a disclosed fact of the render (RFC2-10:
"A condition genuinely outside the four is disclosed as a fact of the
render"). It is *not* a project fact: PWB-REQ-004 closes that population
("The POC SHALL admit project facts only from this closed population:
`item:<class>:<declared-key>` and `count:<class>` … `catalog-count:<catalog-key>`
… and `project-account:<key>` … Every declaration SHALL be emitted by the
extractor assigned to an admitted source; an injected or unrecognized fact,
class, key, catalog or account key SHALL mint nothing", the digest-bound
spec at lines 491–498), the probe's count is in none of those four forms
and is emitted by no extractor, and the probe mints nothing inside that
population — it is a claim *about* the pinned evaluation, carrying its own
claim id, tier, challenge state and evaluation identity, and it enters
PWB-REQ-020's parity population as a "disclosure Polaris presents", so
parity applies to it like any other (review 4 finding J1; an earlier draft
called the count "a project fact", which would have put slice 2 on the
wrong side of PWB-REQ-004). If the owner or a reviewer reads the count as a
project fact after all, slice 2 acquires a PWB-REQ-004 spec delta, its act
row flips to yes, and it joins Q6's collision — the same contingency slice 3
states for PWB-REQ-020.

**The probe's own freshness.** The probe claim carries no freshness value,
before slice 5 and after it. It is not a project-shape claim, so
PWB-REQ-007's complete-tuple requirement does not reach it, and RFC2-10's
disclosure route is exactly what it is: a fact of the render. Its bracket
therefore has no freshness slot, `data-epistemic-freshness` is never set on
it (S3 already requires that no freshness value on the page derive from
it), and slice 5's `currencyBounds` array carries no row for it, stated
there so no implementer adds one. Rendering the probe `fresh` would
reintroduce, on the page's most prominent new claim, the unearned value M2
exists to remove (review 4 finding J2; an earlier draft's rendering did
exactly that).

Rendered in the opening band, before the first catalog section:

> Evaluated at revision 2e3bac97790b, committed 2026-09-13T10:31:11Z,
> captured 2026-09-13T13:33:24.295Z — 3 hours before this probe. Since that
> revision, **N sources on this page have changed** and M have been added.
> [Observed · report-fact · unchallenged · probe
> `evaluation:pwb-currency-probe:…` — a disclosure of the render, no
> freshness value] · What this means

The relative-age string ("3 hours before this probe") is display formatting
and `architecture.md`:236 excludes it from the identity test by name. The
counts are not: they belong to the probe's own evaluation, and two reads of
the *pinned* evaluation still return byte-identical tuples because the probe's
result is computed once, at build, and carried on the model — never read at
render.

**Why the probe cannot be folded into freshness.** A changed source is a
fact of a *different* evaluation — the probe's — and RFC2-10 binds a claim's
freshness to the evaluation that produced the claim, so a `broken` sourced
from the probe would be a freshness state no run of the pinned evaluation
could reproduce. That is Q3's ground. The render-time argument (two reads
at 10:00 and 14:00 disagreeing) does *not* decide it, because the probe is
computed once at build, as the paragraph above says; it is kept here only
to say so (review 1 finding F4, review 2 finding G7).

**Degradation, not improvement.** The probe may only make the reader trust
the page *less*. It never clears an Unknown, never raises a tier, and never
re-labels a claim — `architecture.md`:227 permits exactly that direction.

### Slice 3 — An `evidence` block on the machine payload (medium; no act)

`PocModel.evaluation` gains a sibling `evidence` block carrying: the pinned
revision and its committer instant, the observation instant, the probe's
identity, instant, changed-source count and added-source count, and the
declared currency bounds once slice 5 lands (empty until then, which is
itself the honest answer). It is served on `/api/poc`, the parity channel,
and mirrored on `/api/poc/polaris`, which is the authenticated envelope of
the presentation artifact, "not `/api/poc`" and "never … part of it"
(`apps/three-surface-poc/src/polaris-narrative.ts` lines 193–198), so the
mirror is a convenience for readers of that envelope and not a second
parity channel. Every human-rendered horizon fact appears on `/api/poc`
with the same claim id, which is what PWB-REQ-020 requires. PWB-REQ-020
does not permit the machine channel to carry more *facts* than the page: its
Observable reads "both populations contain equivalent multisets", its
Scenario "the complete human fact multiset equals the machine fact
multiset", and its Falsifier ends "or associated with a different
evaluation in either channel" [Observed: the digest-bound spec, quoted
verbatim]. So the argument for slice 3 is narrower. The parity population
PWB-REQ-020 enumerates is "every project-shape identity, statement, source
anchor, coverage state, denominator, contradiction, body-read authority
state and walkthrough-judgment state or disclosure Polaris presents". Every
horizon *fact* the page renders (the probe claim, its instant, its
counts) is a project-shape statement and disclosure and therefore enters
that population in both channels with the same claim id and the same
evaluation. The `evidence` block's remaining fields (the declared bounds,
the pinned and current digests) are inputs and identities of the
evaluation, not facts Polaris presents about the project shape; they sit
outside the enumerated population, so the multisets stay equal [Inferred:
this is the reading of the enumeration this packet relies on; if the owner
or a reviewer reads declared bounds as a "disclosure" in PWB-REQ-020's
sense, slice 3 acquires a PWB-REQ-020 spec delta and joins Q6's collision,
and the page must then render the bounds too]. One precedent the capture
does *not* offer, stated so no reader reaches for it: the 415 machine items
against 409 rendered item rows are not six statements absent from the page.
The six `project-account-section` items' statements are each rendered once
as the account's own section (`data-polaris-section="claim:project-account:<key>"`
occurs 6 times, one per key; the string
`claim:item:project-account-section:<key>` occurs 0 times for each of the
six), their statements and anchors byte-identical to the six
`projectAccount` entries the page renders, and the parity sweep omits them
from the item-row family for exactly that stated reason
(`apps/three-surface-poc/src/polaris-parity-sweep.test.ts` lines 202–209:
"presented once, as the account's own section claims, never as an item
table") [Observed: both channels of the retained lane A capture and the
test source, re-derived 2026-09-14 after review 3 finding H1; an earlier
draft read the gap as machine-only facts and was wrong]. Every one of the
six statements and anchor sets is in both channels under the account's own
claim id; what the machine carries and the page does not is six *claim
identities* — the machine `facts` population holds both
`item:project-account-section:<key>` and `project-account:<key>` for each
of the six keys, twelve keys among 439, and PWB-REQ-004 names the two forms
as separate members of its closed population — which PWB-REQ-020's
one-directional human-to-machine invariant permits and the parity sweep
omits by name (review 4 finding J6; "every fact is in both channels" was
false at the spec's own fact granularity). The existing parity sweep
already checks per tuple against the machine claim by id and both id sets,
so any horizon fact rendered on one side only fails it.

### Slice 4 — `asOf` immutability (medium; no act)

`buildModel` stops minting `asOf` from the clock. The observation that
already happens once at `main.ts` lines 80–81 gains an instant, and that
instant *is* `asOf`; a rebuild with no new observation reuses it. A
re-observation (slice 2's operator route) mints a new observation and
therefore a new `asOf`, which is exactly VIS-2's "a status flipping with no
new identified evaluation" turned into a mechanism.

**Test.** Inject a clock, build twice with no re-observation at two different
injected instants, assert the two rendered pages are byte-identical and
`asOf` is unchanged; then re-observe and assert `asOf` moved and the
evaluation identity changed with it.

### Slice 6 — A lapsed reviewed selection announces itself (medium; no act)

The dossier's L4-M5, which an earlier draft carried only as scenario S9 and
a Gate 6 mutation target without a slice (review 2 finding G3).
`applyReadingPlan` (`apps/three-surface-poc/src/polaris-reading.ts` line 44)
returns the full declaration with `condensed: false` at thirteen guard
returns — the pinned-digest mismatch and the empty-passage list at line 44,
and eleven structural guards on passages, figures and chapters at lines 48,
49, 50, 51, 53, 61, 64, 72, 79, 88, 99 and 103 — and none of them carries a
reason (review 4 finding J5; "whenever … digest … or … no passages" was two
of thirteen); the renderer at `polaris.ts`
lines 506–510 then shows neither the "selected passages" label nor the
"full account" disclosure, so the page is byte-for-byte what it would be
had no selection ever been offered [Observed, both files at `a9f671e`].
The slice adds one field to the `ProjectReading` type — the reason the
selection was not applied (`digest-mismatch`, `no-passages` or
`plan-malformed`, the last covering the eleven structural guards so that no
full-declaration return stays silent) — and one rendered sentence beside
the full declaration: that a reviewed selection existed, was withdrawn (for
`digest-mismatch`: because the declaration's bytes changed, returning when
a re-review against the new bytes is recorded; for the other two: because
the recorded plan could not be applied, naming the reason). It is a
disclosure of a render fact (RFC2-10's phrase), not a freshness value, and
it reads nothing new: the digest comparison already runs. No act: no governed
artifact, no consent surface, no spec text.

**Test.** Build with a plan whose `statementSha256` is deliberately wrong
for the fixture text; assert the full declaration renders *and* the
withdrawal sentence renders with its reason; then correct the digest and
assert the sentence is absent and the condensed form returns. Rule-6
mutant: drop the reason from the return and confirm the first assertion
fails.

### Slice 5 — The currency bound and `assessCurrency` (large; owner act)

The registry entry gains, beside `resourceLimits` and
`resourceLimitSemantics`, a `currencyBounds` array — one row per claim class,
each with `claimClass` and `maxAgeMs`, one per project-shape claim class
and none for slice 2's currency probe, which carries no freshness value —
plus a `currencyBoundSemantics`
object in the same style as the existing `resourceLimitSemantics`, saying
what the bound is measured from (the source's committer instant) and to (the
evaluation's as-of instant). The entry's bytes are digest-bound by
`decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, and AGENTS.md's
hard prohibition "Never edit an artifact after an act has bound its digest"
applies: the amended entry is prepared as new bytes and adopted by a fresh
superseding act in the 2026-09-05 shape, which supersedes the earlier record
for the `adopt-registry-entry` role only; the superseded record, its digest,
its tag and the bytes it bound are never edited. That is the act in Q2.

`project-shape-model.ts` deletes its `FRESH` constant and its comment, imports
`assessCurrency` from `packages/cap1-core`, and calls it per claim with the
class, the evidence record, the declared bounds and the evaluation's `asOf`.
`assessCurrency` has five return paths over three `state` values
(`no-bound-declared`; `stale` with basis `unreadable-instant`,
`future-dated-instant` or `age-exceeds-bound`; `current`) [Observed:
`packages/cap1-core/src/staleness.ts` lines 87–155]. Four map straight onto
the tuple: `current` → `fresh`; the three `stale` returns → Unknown with
`stale-beyond-currency-bound` and freshness `stale`, the future-dated and
unreadable bases failing closed, which is the polarity AGENTS.md records as
the project's rule.

**The fifth arm is a gap, and it is the arm every class reaches first.**
The `no-bound-declared` return carries `label: 'Unknown'` and reason
`no-currency-bound-declared` but **no `freshness` field at all** [Observed:
lines 98–104], while PWB-REQ-007 requires the complete tuple including
freshness on every claim and RFC2-10 says "no implementation may mint,
spell, or force-fit a freshness value it does not carry". A claim of an
undeclared class therefore cannot render `fresh` (the defect M2 removes),
cannot omit freshness (PWB-REQ-007), cannot take a fifth value (RFC2-10),
and the engine deliberately declines to say `stale`. RFC2-10's own words
make this an owner choice, not a render-time one; it is Q7 in the batch.
Recommended: `stale`, with the primary reason `no-currency-bound-declared`
kept distinct — CAP1-REQ-062 puts an unbounded class under the same
invariant as out-of-bound evidence ("SHALL NOT support a current or
favourable answer"), both rendering Unknown with distinct reasons and
neither assigned a freshness value, and `stale` is the one closed-vocabulary value whose
legend sentence ("older than the declared currency bound") a reader can
reconcile with "no bound is declared" once the reason is beside it
[Inferred]. The strongest counter-argument is RFC2-10's own sentence,
quoted under Gate 2 and relied on for Q3: "A condition genuinely outside the
four is disclosed as a fact of the render, never dressed as a freshness
state." No declared bound is such a condition, so rendering `stale` for it
is a candidate for that dressing; the packet still prefers it because
PWB-REQ-007 requires the freshness field on every project-shape tuple (its
Falsifier names "a tuple field is absent/out of vocabulary"), which the
disclosure route cannot satisfy on these claims, and because the alternative
— amending the engine so `no-bound-declared` carries a value — places the
same choice inside Capability 1 rather than escaping the sentence (review 4
finding J3). The owner rules with both in view. Until Q7 is ruled, slice 5
is not implementable for any class without a declared bound, which is every
class today.

**Trade-offs rejected.** (a) Declaring one bound for all classes: cheaper, but
RFC2-9 declares bounds per claim class and the classes genuinely differ (a
design contract ages differently from a roster identity). (b) Re-implementing
the judge inside `three-surface-poc-core`: it would duplicate a
conformance-tested module and re-open L4-F2's disagreement in a new place.
(c) Implementing the bound as a code constant: RFC2-9 forbids it in terms —
a bound without an effective owner act does not unblock its class.

### Design bar for the human surface

No new interaction beyond one disclosure in the opening band and one operator
route that is not linked from the page. The existing contract inputs carry
forward unchanged: PWB-REQ-016 comprehension without vision or a pointing
device (the horizon band is text in reading order, and every legend marker is
text, not colour); no fragment target inside a `<details>`; keyboard paths
complete; direct and tailnet parity; the no-JS path complete; the glossary
still explaining every rendered tuple term.

## Gate 5 — Specification

**Slices 1–4 and 6: no spec delta.** Each is conformance with text that
already
binds. Slice 1 makes the rendered legend match what the evaluation produces,
which VIS-7 already requires. Slice 2 adds a disclosed fact of the render,
which RFC2-10 already names as the lawful home for a condition outside the
four values, and an epistemically labeled claim, which PWB-REQ-014 already
names as one of its three claim roles; it adds no project fact, so
PWB-REQ-004's closed population ("The POC SHALL admit project facts only
from this closed population … an injected or unrecognized fact, class, key,
catalog or account key SHALL mint nothing", lines 491–498) is untouched —
the probe's count is in none of the four admitted forms and is emitted by
no extractor, and the slice neither enters nor amends that population
(review 4 finding J1). Were the owner to read the count as a project fact,
slice 2 would need a PWB-REQ-004 delta and would join Q6's collision.
Slice 3 adds machine fields outside PWB-REQ-020's enumerated parity
population and renders every horizon fact in both channels, so the
equal-multiset Observable holds [Inferred, see slice 3 for the reading and
its condition]. Slice 4 removes a clock read that VIS-2's last sentence
already forbids.

**Slice 5: no spec delta either — and this is the packet's most useful
finding.** PWB-REQ-007 already carries the scenario slice 5 implements, at
lines 470–474 (heading at 470, WHEN bullet at 472) of
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`:

> #### Scenario: Missing current evidence remains explicit Unknown
>
> - **WHEN** a declared project fact lacks evidence under its current
>   currency bound
> - **THEN** its claim renders Unknown with the exact primary reason and route
> - **AND** its tier, freshness and evaluation identity remain visible

and its Observable already reads "invalid/missing currency stays Unknown and
aggregates expand to members". The signed specification is therefore not
wrong about currency; the implementation does not yet meet it. That means M2
needs **no amendment to the digest-bound PWB spec**, which is what keeps it
clear of the lane B package. If the owner rules Q1 the other way — that "the
evaluation itself is the currency" is a lawful reading — then the spec text
*would* need an amendment to say so, and that amendment would collide with
lane B head-on; Q1 is therefore also the collision gate.

### New WHEN/THEN scenarios (for the beads' acceptance contract, not the spec)

**S1 — An unreachable freshness state is marked, not promised.**
WHEN a freshness value in the closed four-value vocabulary is rendered by no
claim tuple at this evaluation, THEN its glossary sentence carries the reason
it is unreachable and, where one exists, the route that would make it
reachable, AND a copy oracle fails if any unreachable value's sentence lacks
a marker or any rendered value's sentence carries one (the oracle enforces
the marker, not the route).

**S2 — A reachable state loses its marker automatically.**
WHEN the currency bound lands and at least one claim renders `stale`, THEN
the `stale` sentence carries no unreachable marker, with no separate copy
edit, AND the same oracle enforces it.

**S3 — The horizon is a separate identified evaluation.**
WHEN the page renders an evidence horizon, THEN the count of changed sources
carries its own evaluation identity and instant, distinct from the pinned
evaluation's, AND no `data-epistemic-freshness` value anywhere on the page is
derived from it.

**S4 — One evaluation, two reads, identical bytes.**
WHEN one identified evaluation is served twice at two different wall-clock
instants with no re-observation between them, THEN the two responses are
byte-identical, AND `asOf` is unchanged.

**S5 — `asOf` moves only behind an observation.**
WHEN the model is rebuilt with no new observation, THEN `asOf` and the
evaluation identity are unchanged; WHEN the operator re-observation route is
called, THEN a new observation is taken, `asOf` advances, and the evaluation
identity changes with it.

**S6 — An out-of-bound class renders Unknown, not green.**
WHEN a claim class's evidence is older than its declared currency bound at the
evaluation's as-of instant, THEN every claim of that class renders Unknown
with primary reason `stale-beyond-currency-bound`, freshness `stale`, its
resolution route beside it, and its tier and evaluation identity still
visible.

**S7 — An undeclared class renders Unknown, not green.**
WHEN a claim class has no declared currency bound, THEN its claims render
Unknown with primary reason `no-currency-bound-declared` and the declaration
route, AND no aggregate folds them into a favourable total.

**S8 — A bound without an act does not unblock its class.**
WHEN a currency-bound declaration is present in the tree but no effective
owner act binds its bytes, THEN the class's claims continue to render Unknown
and the invalid declaration is disclosed as a contradiction (RFC2-9's own
arm), AND no claim leaves Unknown on the strength of the unacted file.

**S9 — A lapsed reviewed selection announces itself.**
WHEN a reviewed reading selection is not applied — its pinned statement
digest does not match the observed statement bytes, its plan has no
passages, or a structural guard rejects the plan — THEN the page renders
the complete declaration *and* says that a reviewed selection was withdrawn
and why, naming the reason (`digest-mismatch`, `no-passages` or
`plan-malformed`) and, for a digest mismatch, what would restore it (a
re-review against the new bytes), AND a test asserts both halves.

**Out of scope, explicitly.** Amending the PWB specification; amending
doctrine (none is needed — `architecture.md`:236's relative-age exclusion
already covers the opening band); moving catalogs to their own routes;
raising or narrowing any `resourceLimits` value; any second repository; any
background timer, poll or watcher; scoring or judging the owner's walkthrough
answers; and the generator-side horizon (L4-F6), which belongs to M7.

## Collision and sequencing

**What M2 shares with the lane B package.** The lane B semantic delta
(`syzygy-dov.17`, drafted on branch `agent/syzygy-dov.17`; owner decision
P-68 is queued and unruled **on that branch's copy of the pending register
only** — main at `a9f671e` has no P-68 row and its last register note is
P-67 [Observed]; nine files under
`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`
that are **not present on main at `a9f671e`** [Observed: `git ls-files` over
the tracked tree and a `find` over the worktree both return zero paths])
edits the PWB specification at exactly the clause region M2 reads:

1. **The same requirement.** Lane B's `proposed/spec.md.patch` has three
   hunks; the first covers old lines 450–471 of the spec and the second
   473–483, both inside PWB-REQ-007, inserting a new paragraph and
   rewriting its Case, Observable, Oracle, Oracle-independence and
   Falsifier bullets [Observed: hunk headers `-450,22` and `-473,11`,
   re-read 2026-09-14 after review 1 finding F13; an earlier draft said
   "lines 450–472"]. Line 472, the WHEN bullet of the currency scenario
   quoted under Gate 5, falls between the two hunks and the scenario at
   470–474 is context in both, so the currency scenario M2 relies on is
   byte-unchanged by lane B. PWB-REQ-007 is the requirement that owns the
   tuple, and `freshness` is one of its named fields — it appears in the
   Case bullet lane B rewrites.
2. **The same field.** Lane B lets a tuple field "whose value is the same for
   every claim under one enclosing scope" be carried once on the scope. Today
   `freshness` is the most scope-hoistable field on the page: it has exactly
   one value over all 713 tuples. **After slice 5 it will not be**, because
   an out-of-bound or undeclared class renders `stale`. Lane B's estimated
   saving is computed against a population in which freshness is uniform; M2
   is the move that ends that uniformity.
3. **The same parity comparator.** Both reach PWB-REQ-020. Lane B makes the
   comparator expand scopes before comparing; M2 adds the horizon's claim
   and, after slice 5, tuples whose freshness differs per class. A scope that
   hoists `freshness` and a class that renders `stale` beneath it is exactly
   lane B's "over-asserting scope" falsifier — so the two changes are
   complementary in design and dangerous in sequence.

**The sequencing that avoids two packages editing one clause.**

1. **Rule P-68 first.** The lane B package is drafted, reviewed
   (CONFIRM WITH EXCEPTIONS, raw retained) and queued; its manifest binds
   post-amendment bytes computed against today's spec. A second package
   drafted concurrently against the same pre-amendment bytes could not be
   performed after the first: its manifest would name a digest the spec no
   longer hashes to. So in practice only one PWB behavior-amendment package
   can be open at a time, and that one is open [Inferred: a consequence of
   the manifest binding post-apply bytes, not a stated rule; no clause says
   it, and AGENTS.md's "one coherent category overlapping no other change"
   is about OpenSpec changes, not packages in flight].
2. **Run M2 slices 1–4 and 6 now, in parallel with P-68.** They touch no
   governed
   artifact, no spec text and no manifest, so they cannot collide. They can
   land while P-68 waits.
3. **Slice 5's act is a registry act, not a spec act.** It amends the adapter
   registry entry and leaves the spec byte-unchanged, so it may be prepared
   and performed independently of P-68. Keep it that way: if slice 5 starts
   to want spec text, stop and re-enter this funnel.
4. **Re-measure lane B after slice 5, before its act.** Lane B's headline
   saving (currently recorded as 188,902 bytes tailnet, in the lane B
   package on `agent/syzygy-dov.17` only [Observed there, not on this
   branch]) assumes a uniform
   freshness field. If slice 5 lands first, that number must be recomputed,
   and if the act is performed first, the implementation must not hoist
   `freshness` onto a scope until slice 5's per-class values are known. The
   safe order is: rule P-68 → implement lane B's hoist for evaluation
   identity and the presentation flags only → land slice 5 → then decide
   whether `freshness` is still hoistable at all.
5. **If Q1 is ruled the other way**, M2 acquires a spec delta and must queue
   behind P-68 as a second, separate package — never a second hunk in the
   first.

## Gate 6 — Engineering bar

Acceptance, reusing the M1 and P-63 shape:

1. **Retained measurement, before and after**, direct and tailnet host forms,
   at a named Syzygy commit and Butlers revision, in `docs/evidence/`, from a
   private daemon on port 0 with its own state directory, never the loopback
   daemon, on a committed clean tree. The M2 numbers to record: the
   freshness-value histogram with its denominator, the count and depth of
   human-visible instants, and the page's byte size on both forms (the M1
   ruling's 1,400,000-byte working target is already exceeded by 84,487
   bytes on the tailnet form; M2 must not widen that gap materially, and
   the 2 MiB response ceiling is the hard limit).
2. **Every M1 invariant equal before and after** except the ones M2
   deliberately changes: claim id set, item and source populations, fragment
   targets with zero dangling, and the mount-prefixed link count stay equal;
   the freshness histogram and the instant count are expected to move, and
   the evidence file records both sides. Computed by script, never
   transcribed.
3. **Determinism, proven twice.** The S4 byte-identity test, and a rule-6
   mutant that makes `asOf` read the clock again and confirms S4 fails.
4. **Rule-6 mutation evidence for every new guard branch**: each of
   `assessCurrency`'s five arms as reached through the PWB model; the
   copy-oracle's two directions (an unreachable value without a marker, a
   rendered value with one); the probe's evaluation-identity separation (make
   the probe write the pinned evaluation's id and confirm S3 fails); and the
   reading-plan announcement. Each mutant's `old`/`new` fragment and the
   commit it ran at are recorded, per the evidence rule.
5. **Preflight populations, PWB-REQ-020 parity with both denominators**,
   keyboard, no-JS and browser tests, the app suite twice and the full suite
   pass; `tsc -b packages/three-surface-poc-core` before the app typecheck.
6. **A fixture whose as-of exceeds its bound renders `stale` at least once**,
   and the copy oracle then requires the `stale` sentence to have lost its
   marker — the two halves of the legend contract closing on each other.
7. **Independent review in fresh context** before close, raw retained as a
   `-RAW.md` file; and for slice 5, an independent review of the registry
   delta *before* the owner act, in the 2026-09-05 packet shape.
8. **Conformance expected values hard-coded**, never imported from the module
   under test; the copy oracle's labels distinctive enough that a substring
   match cannot succeed by coincidence.

## Review 1 and repairs (2026-09-14)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the questionnaire invariant) is
retained verbatim at `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-RAW.md`
(39904 bytes, sha256 `ff8c8f836e4488de939ae26d5e0a61c12d110c35a5438dd8aab3d5ff4be882bc`). It reviewed the
packet at 47846 bytes, sha256
`8f57109243f4c26c7b7da268a0050cd61f8ed9a7f71b4416b80ef83d1e721f7b`, and
the evidence record at 3896 bytes, sha256
`98acc654eba4ae11b5e63afe09143e57397580ee1c9e9259064f9944af66f502`, on
commit `a9f671e9d69e1a20c89c7f6ed0c6d9e58a644c1d` with both files
untracked. Its verdict word, copied exactly: **REVISE**. Every edit below
was made after that review, so by verification rule 10 the review binds
the bytes it names and not these; a second fresh-context review follows,
and its raw will be a second `-RAW.md` file, never an overwrite.

| Finding | Severity | Disposition |
|---|---|---|
| F1 headroom claim false | blocking | Accepted and repaired: the paragraph now states the page is over the 1,400,000-byte target and under the ceiling, with the arithmetic and the P-60/P-61 reservation, labeled Observed |
| F2 PWB-REQ-020 paraphrased into its opposite | blocking | Accepted and repaired: Observable, Scenario and Falsifier quoted verbatim; the narrower parity-population argument made, labeled Inferred, with the condition under which slice 3 would join Q6's collision stated. Q6's answer is unchanged |
| F3 `broken` marker's route contradicts Q3 | non-blocking | Accepted and repaired: the marker now says the value is unreachable by design and names what would change that; no route to the horizon |
| F4 Q3's ground | non-blocking | Accepted and repaired: Q3 restated on RFC2-10's evaluation scoping; the render-time-drift argument kept only as a non-ground |
| F5 Q4's first warrant | non-blocking | Accepted and repaired: the unattended-coordination sentence withdrawn; the no-act warrant leads |
| F6 consent scope misquoted | non-blocking | Accepted and repaired: restated on the escalation trigger's actual words and the act's scope sentence |
| F7 undeclared-bound freshness gap | non-blocking | Accepted and repaired: named in slice 5 and added to the batch as Q7 with a recommendation |
| F8 "exactly one new boundary" | non-blocking | Accepted and repaired: none new; the existing edge gains the judge |
| F9 L4-F1 absent | non-blocking | Accepted and repaired: re-measured against the lane A capture and Butlers head by two methods (15 of 278 sources; 9 of 409 rows), carried into Gate 1 |
| F10 digest-bound bytes | non-blocking | Accepted and repaired: the prohibition named and the superseding-act mechanism stated in slice 5 |
| F11 one-package rule | non-blocking | Accepted and repaired: labeled Inferred, argued from manifest mechanics only |
| F12 staleness clause past its subject | non-blocking | Accepted and repaired: the clause's subject stated; the reach to M2 argued as an extension, labeled Inferred |
| F13 hunk header | editorial | Accepted and repaired: both hunk ranges stated; line 472 shown untouched |
| F14 instant grouping | editorial | Accepted and repaired: two on the line, one in the authority disclosure, with offsets |
| F15 four or five arms | editorial | Accepted and repaired: five return paths over three states, stated once and used in Gate 6 |
| F16 register route | editorial | Accepted and repaired: the register's families stated; spec requirements located by heading sweep |
| F17 file count | editorial | Accepted and repaired: three source files; the dist row removed from the evidence record |
| F18 predicate | editorial | Accepted and repaired: the attribute predicate named with the substring count beside it |
| F19 P-68 not on baseline | editorial | Accepted and repaired: said where P-68 lives |
| F20 Q1 omits PWB-REQ-007's warrants | editorial | Accepted and repaired: the warrants line cited in Q1 |

None of the seven recommended answers changed; Q7 is new.

### Review 2 and repairs (2026-09-14)

A second independent fresh-context review of the repaired packet at commit
`ec30494` is retained verbatim at
`docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-2-RAW.md` (35095 bytes,
sha256 `545c39259e370a5019ec40c6de210fcd00ce4bb5dedd09cb60f2350bc6367a22`). Its verdict word,
copied exactly: **REVISE** — three blocking, six non-blocking, five
editorial. It verified review 1's twenty repairs: sixteen repaired, three
partial (F4, F5, F6 — each completed below), one repaired as stated but not
re-derivable on this branch (F13; the lane B package lives on
`agent/syzygy-dov.17`). Every edit below post-dates review 2, so the
current bytes are again uncovered until a third review, retained as a
third `-RAW.md` file, confirms them.

| Finding | Severity | Disposition |
|---|---|---|
| G1 P-69 row kept the withdrawn Q4 warrant | blocking | Accepted and repaired: the clause deleted from the register row |
| G2 P-69 row misnamed the no-act slices | blocking | Accepted and repaired: the row now names slices 1–4 and 6 as the packet has them, including slice 3 |
| G3 S9 had no slice | blocking | Accepted and repaired: slice 6 added with a topology row, an act row, a design sketch, a success criterion and summary lines; Gate 6 item 4 now has a slice to bind to |
| G4 "no date above 58%" false under its own words | non-blocking | Accepted and repaired: restated as no instant of the evaluation, predicate named, the two earlier `YYYY-MM-DD` strings disclosed |
| G5 PWB-REQ-020 reading contradicted by the capture | non-blocking | Accepted and repaired: the six unrendered `project-account-section` items stated as the precedent for the Polaris-scoped population; the contingency dropped and the alternative reading disclosed as a possible finding against the existing implementation |
| G6 trigger attributed to the consent act | non-blocking | Accepted and repaired: attributed to the implementation-authorization act by path and section |
| G7 slice 2 still argued render-time drift | non-blocking | Accepted and repaired: the paragraph now carries Q3's ground and keeps the drift argument only as the non-ground |
| G8 `stale` marker's reason self-falsifying under Q7 | non-blocking | Accepted and repaired: reworded to the constant-assignment reason with slice 5 as the route |
| G9 Q5's losing arm called unlawful | non-blocking | Accepted and repaired: Q5 moved out of the one-lawful-arm sentence; both arms stated lawful; recommendation kept with its reasons |
| G10 CAP1-REQ-062 "exactly" | editorial | Accepted and repaired in both places |
| G11 unit convention | editorial | Accepted and repaired: the byte figure's source named, decimal convention stated |
| G12 two unlabeled estimates | editorial | Accepted and repaired: labeled Inferred; the lane B figure's location stated |
| G13 three offsets | editorial | Accepted and repaired: 470–474, 19–27, 98–104 |
| G14 "two constants" | editorial | Accepted and repaired in the register row |

None of the seven recommended answers changed; the dossier's L4-M5 is now
slice 6.

### Review 3 and repairs (2026-09-14)

A third independent fresh-context review, of the packet at commit
`e0ecdc8`, is retained verbatim at
`docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-3-RAW.md` (30943 bytes,
sha256 `930c4e361a05c677b428afaf4d743af22197984b34623fb49e17fc966d4024ed`). Its verdict word, copied exactly: **REVISE** — one
blocking, five non-blocking, four editorial. It verified G1–G4 and G6–G14
repaired and F4, F5, F6 complete, and found G5 **not repaired**: the
review 2 repair had read the six `project-account-section` machine items
as facts the page never renders, and they are rendered, once each, as the
account's own sections. Every edit below post-dates review 3; the current
bytes are uncovered until a fourth review confirms them.

| Finding | Severity | Disposition |
|---|---|---|
| H1 the PWB-REQ-020 "precedent" was false | blocking | Accepted and repaired: the paragraph now states what the capture and the sweep's own comment show — every fact in both channels, the gap one of rendering form — and slice 3 rests on the enumerated-population reading alone, labeled Inferred, with review 1's contingency restored; the table note, Gate 5 and the evidence record corrected; `/api/poc/polaris` described as the presentation envelope before a field is proposed for it |
| H2 predicate-less "0 times" | non-blocking | Accepted and repaired: the counted string named, in the packet and the evidence record |
| H3 P-69 row's Q3 clause cited VIS-7 | non-blocking | Accepted and repaired: the register clause now names RFC2-10's evaluation scoping and says the identity test is not the ground |
| H4 P-69 row silent on Q5's two lawful arms | non-blocking | Accepted and repaired: the register clause now says both arms are lawful and why marking is recommended |
| H5 success criterion 5 contradicted slice 6's test | non-blocking | Accepted and repaired: "renders the condensed form and no withdrawal sentence" |
| H6 envelope trigger unaddressed | non-blocking | Accepted and repaired: one clause in the slice 2 act row |
| H7 slice 6 size | editorial | Accepted and repaired: medium, in all three places |
| H8 citation crossed two files | editorial | Accepted and repaired |
| H9 `assessCurrency` span | editorial | Accepted and applied, then found not to be a defect: the function opens at line 87 and its closing brace is line 155, so the original "87–155" was correct and the repair moved it two lines past the function; restored after review 4 finding J7 |
| H10 evidence key inverted | editorial | Accepted and repaired: renamed `before_first_evaluation_instant` |

None of the seven recommended answers changed.

### Review 4 and repairs (2026-09-14)

A fourth independent fresh-context review, of the packet at commit
`68123fc`, is retained verbatim at
`docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-4-RAW.md` (33108 bytes,
sha256 `804b11f8284942bca33d2eaa91822ba72f0f91c634be482f62a17c4b3eabef8f`). Its verdict word, copied exactly: **REVISE** — one
blocking, five non-blocking, two editorial. It verified H1–H8 and H10
repaired and found H9 repaired to a false span (J7). Every finding below
was re-derived against the source and the retained captures before it was
applied (the thirteen guard returns, the twelve project-account fact keys
among 439, the function's closing brace at line 155). Every edit below
post-dates review 4; the current bytes are uncovered until a fifth review
confirms them.

| Finding | Severity | Disposition |
|---|---|---|
| J1 slice 2 called the horizon count "a project fact", a closed population under PWB-REQ-004 the packet never cited | blocking | Accepted and repaired: the count restated as an epistemically labeled claim (PWB-REQ-014) and a disclosed fact of the render (RFC2-10), not a project fact; PWB-REQ-004 lines 491–498 quoted in slice 2, the slice-2 act row and Gate 5, with the contingency stated as slice 3 states its own; PWB-REQ-004 added to the Gate 0 specification row |
| J2 the probe's own claim rendered `fresh` with no declared bound | non-blocking | Accepted and repaired: the probe carries no freshness value before or after slice 5, its bracket has no freshness slot, and slice 5's `currencyBounds` sketch says it has no row |
| J3 Q7 never weighed against RFC2-10's "never dressed as a freshness state" | non-blocking | Accepted and repaired: the sentence quoted against the recommendation in Q7 and in slice 5, with why `stale` plus a distinct reason is still preferred and why the engine amendment does not escape it; the recommendation unchanged, the owner rules with both in view |
| J4 criterion 2 and S1 required a route the `superseded` marker lacks | non-blocking | Accepted and repaired: both weakened to "and, where one exists, the route"; the oracle stated to enforce the marker, not the route |
| J5 "whenever" overstated `applyReadingPlan`'s reasons | non-blocking | Accepted and repaired: thirteen guard returns named by line; a third reason value `plan-malformed` covers the eleven structural guards so no full-declaration return stays silent; S9 restated |
| J6 "every fact is in both channels" false at fact granularity | non-blocking | Accepted and repaired: statements and anchor sets shared, six claim identities machine-only, the twelve keys named, PWB-REQ-020's direction and the sweep's omission stated |
| J7 the H9 repair made a true span false | editorial | Accepted and repaired: "87–155" restored in both places; the review-3 disposition row now says H9 was not a defect |
| J8 the P-69 row mischaracterized review 2's blocking findings | editorial | Accepted and repaired: "two register/packet mismatches and a scenario with no slice" |

None of the seven recommended answers changed.

## Funnel summary

```
## Feature Request: M2 — Evidence currency: the horizon, assessCurrency, a true legend
Size: medium (slices 1-4, 6) / large (slice 5)
Baseline: Syzygy a9f671e; capture = lane A after/tailnet, 1,484,487 bytes, Butlers 2e3bac97790b
- G1 Motif: one freshness value rendered 713/713 while the legend promises four; a complete currency engine sits unwired [Observed: three sweeps of the capture; two code sweeps]
- G2 Doctrine: aligned - VIS-2 (currency bound; no clock-driven status), VIS-7 (every encoding means what its legend says; the identity test), CAP1-REQ-062 (the engine's own requirement), RFC2-9, RFC2-10, architecture.md 221-236
- G3 Topology: apps/three-surface-poc + packages/three-surface-poc-core; no new boundary (the existing cap1-core import edge gains assessCurrency); the adapter-registry entry only in slice 5, by a superseding act; no spec text
- G4 Design: legend markers; a currency probe as a second identified evaluation; an evidence block on the machine payload; asOf bound to an observation; the bound declared in the registry and judged by assessCurrency; a withdrawn reading selection announced with its reason
- G5 Spec: no delta - PWB-REQ-007's own currency scenario already requires slice 5's behavior; nine WHEN/THEN scenarios for the beads' acceptance contract; out of scope: spec amendment, doctrine, catalog routes, timers, resourceLimits values
- G6 Bar: retained before/after measurement, determinism proven twice, rule-6 mutants per guard branch, independent review, a registry-delta review before the act
Acts: slices 1-4 and 6 none (the 2026-09-05 implementation-authorization continuation); slice 5 two - adopt-registry-entry over the amended entry, then a continuation across the registry escalation trigger; a timer: none found and none sought
Open questions: Q1-Q7 above; queued as P-69 (P-68 is the lane B decision, on its own branch)
Sign-off: pending - the owner's
Recommended handoff: Q1 "a bound is required" and Q5 "mark, do not delete" -> run slices 1, 3, 4 and 6 now under syzygy-dov.2, plus slice 2 on Q3's second-evaluation design and Q4's operator route; hold slice 5 until Q1 and Q2 are ruled, then draft the registry delta with its own review and put the two-step act to the owner; open no PWB spec package until P-68 is ruled
```

## Recommended handoff

**If Q1, Q3, Q4 and Q5 are answered as recommended:** file no new bead. Run
slices 1, 3, 4 and 6 under `syzygy-dov.2` immediately — they are self-contained,
they touch no governed artifact, and slice 1 alone closes the VIS-7 legend
breach that S5-F1 and L4-F2 named. Run slice 2 next, on the currency-probe
design, with the operator route and no timer.

**If Q7 is answered as recommended:** slice 5 renders every undeclared
class `stale` with reason `no-currency-bound-declared`, and the copy oracle
then requires the `stale` legend sentence to have lost its marker as soon
as any class is undeclared at an evaluation — which, on the day slice 5
lands, is every class. If the owner prefers the engine to carry the value
instead, slice 5 waits for that Capability 1 amendment.

**If Q2 is answered as recommended:** draft the registry delta as a small
package in the 2026-09-05 shape (a semantic delta, an impact ledger, a review
brief, an owner decision packet, a manifest), get its independent
fresh-context review with the raw retained, and put the two-step act — the
`adopt-registry-entry` act, then the implementation-authorization
continuation — to the owner as one batched decision. Only then wire
`assessCurrency`.

**If Q6 is answered as recommended:** nothing in M2 opens a PWB specification
package, and the lane B package keeps the floor until P-68 rules. Record in
`syzygy-dov.17`'s notes that its freshness-hoist estimate is conditional on
M2 slice 5, so whoever implements lane B does not hoist a field that is about
to stop being uniform.

**If Q1 is answered the other way** — that "the evaluation itself is the
currency" is a lawful reading of RFC2-9 — then slice 5 is withdrawn, slice 1's
`stale` marker becomes permanent rather than transitional, and the
disagreement between `packages/cap1-core` and
`packages/three-surface-poc-core` becomes a recorded, accepted gap rather than
a defect. That is a coherent outcome and should be written down as one, not
left as silence; it would also mean the PWB specification's own currency
scenario is unreachable by design, which is worth the owner seeing before
answering.
