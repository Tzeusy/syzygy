RD-18 — fresh-context exact-package review, **Wave A** (RFC 0001–0006, 19 modules). Baseline commit 771965c, frozen clone. Date 2026-08-09. **(part 1/3)**

I read only the frozen clone. I did not read `round-2026-08d/`, `history/`, any `reviews/`, or `_bootstrap/`. Everything below rests on the 19 wave modules, `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, `wave-manifests/`, `ACTIVE-CONTRACT-MANIFEST.txt`, doctrine, and the repo's own scripts. All greps were Python `re`, never system grep.

---

## 1. Manifest verification

**Digests — all 19 verified, two independent methods.** [Observed]

- `sha256sum -c wave-manifests/WAVE-A-MANIFEST.txt` run from the candidates root: **19 lines, all `OK`, 0 failures.** (Output read, not exit code.)
- Independent Python `hashlib.sha256` recomputation of every row: **ok=19, mismatch=0, missing=0.**

**The manifest's own sha256:**

```
8d4f3e723f0ec6a7645cd70abc0d5fe5ebdc6fe1b27e9faa5ad29761613e7816
```

Byte-identical to the argument in acceptance record §1's Wave A row (`ACCEPT FOUNDATIONAL WAVE A: 8d4f3e72…7816`). [Observed]

**File-set sweep, with denominator.** [Observed]
- Files under `C/rfcs/`: **39**. Files matching `rfcs/RFC-000[1-6]`: **19**.
- In-prefix but absent from the manifest: **∅**. In manifest but outside the prefix: **∅**.
- The set is exactly RFC-0001 (1) + RFC-0002 (README+4) + RFC-0003 (README+2) + RFC-0004 (README+4) + RFC-0005 (README+3) + RFC-0006 (1) = 19. **No RFC 0001–0006 package is split across waves** — every module of every package in the wave is in the wave. That is a real structural strength of this wave and belongs on the record.
- Union of all six wave manifests = **39 rows, zero duplicates, exact partition of `ACTIVE-CONTRACT-MANIFEST.txt`** (39 rows). Every Wave A row's digest also matches its row in the active manifest.

**Independent corroboration from the repo's own tooling** (outputs read, not exit codes):
- `scripts/build_active_manifest.py --check` → `all 7 manifests match regeneration`
- `check_governance.py` → `CG-7a manifest digests valid; waves partition the set — 78 entries examined, 0 findings`; `CG-7b wave-act arguments match the wave manifests — 6 arguments examined, 0 findings`; `CG-14 acceptance install routes valid — 12 paths examined, 0 findings`. Overall `25 OK, 15 WARN, 0 FAIL (40 checks)`.
- `verify_final_prespec.py` → `PASS — all checks clean`, `numbered clauses defined: 341` (matches record §3's "as of 2026-08-09 it reports 341").

**Clause partition, recomputed from the bytes.** I extracted every bolded clause definition per module, filtered to each file's own RFC id:

| Package | Definitions found | Matches its clause map? |
|---|---|---|
| RFC-0001 | RFC1-1..33 + 18(a),(b) + 25(a)–(d) | yes |
| RFC-0002 | 1..11 / 12..14 / 15..22 / 23..26; no lettered | yes |
| RFC-0003 | 15..17 + 5 lettered / 1..14, 18..33 | yes |
| RFC-0004 | 1..9 / 10..17 + 13(a),(b) / 18..21 / 22..30 | yes |
| RFC-0005 | 1..11, 24..27 / 12..17 / 18..23; no lettered | yes |
| RFC-0006 | 1..28 | yes |

**No clause identity appears in more than one module.** [Observed] The clause-map *tables* are accurate; the defects reported in part 3 are in the narrative range statements around them.

**Post-install backlink simulation.** I simulated record §2 step 3 exactly as documented (19 modules → `contracts/rfcs/`, plus `history/`, `matrix-rows/`, `ACTIVE-CONTRACT-MANIFEST.txt`, `wave-manifests/WAVE-A-MANIFEST.txt`, `CONTEXT-BUDGET-REPORT.md`, `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`) and resolved every relative link in the 19 modules against the result: **44 relative links examined, 0 unresolved.** [Observed] The RD-7 repair works for this wave.

**Record claim tested:** the Wave A row asserts "Every `depends_on` edge of these contracts stays inside the wave." I parsed the `depends_on` front matter of all 19 files; every edge names one of RFC-0001…RFC-0006. **Claim holds.** [Observed] (`admission-and-boundary.md` also carries `constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]` — a *constrains* edge, not a dependency; it does not falsify the claim.)

I read all 19 modules in full. Findings follow in parts 2 and 3, ordered blocking → major → minor.

RD-18 Wave A **(part 2/3)** — blocking and major findings.

---

# BLOCKING

## B1. The first act binds a clause that names the retired ceremony phrase as the live install gate for its own category

**Anchor — RFC3-15**, `governance-homes-and-owner-acts.md:86`, the `contracts/` row of the five-category table (the clause text, not prose near it):

> | `contracts/` | Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts | Owner acceptance (for the foundational set, the digest-bound act defined by the active acceptance record — **`ACCEPT COMPACTED FOUNDATIONAL RFCS: <manifest digest>`**; owner sign-off per VIS-4 thereafter) |

The acceptance record retires that phrase, explicitly and unconditionally (§1, "Two phrases are retired and satisfy nothing"):

> The rev10 phrase `ACCEPT COMPACTED FOUNDATIONAL RFCS` (last argument `2862b2f5…`, with the six earlier retired arguments its row recorded) is **retired at round-2026-08d delivery on the same rule**: the wave acts supersede it, and an offer superseded must not remain performable beside its successor.

**Sweep with denominator.** I swept all 19 Wave A modules for any `ACCEPT …FOUNDATIONAL…` string using Python `re`. **Exactly one hit, this one.** [Observed] No other module names a ceremony phrase.

Two things are wrong at once, and both are inside the digest Wave A binds:

1. The named phrase is retired and satisfies nothing.
2. The row describes **one** digest-bound act over "the foundational set". The structure is **six** wave acts, and the reader performing this very act is performing the first of them. The clause misdescribes the ceremony at the instant it is performed.

**Why blocking, not major.** This is not a stale pointer in a report — it is normative text entering the governed tree at `contracts/`, and RFC3-16(b) item 3 plus record §2 make it unfixable afterwards: "an artifact edited after its act is, for the record, an artifact with no act." It cannot be repaired post-act without destroying the act. It is also a **recurrence**: record §1a shows act 1's argument `08793ddf…` was retired precisely because a "retired acceptance phrase [was] removed from `rfcs/RFC-0003/governance-homes-and-owner-acts.md`". The rev9 phrase was cleaned out of this exact cell and replaced with the rev10 phrase; the rev10 phrase has now been retired and the cell was not swept again. And it is the RD-8 shape the AGENTS.md guidance names — routing an owner to a retired offer — except here the retired offer is inside the accepted bytes rather than beside them.

**Repair (concrete).** In `governance-homes-and-owner-acts.md:86`, replace the parenthetical with a phrase-free reference:

> Owner acceptance (for the foundational set, the digest-bound wave acts defined by the active acceptance record — that record owns the exact phrases and their arguments; this clause quotes none; owner sign-off per VIS-4 thereafter)

That removes the transcription entirely, which is also the repo's own rule ("a figure quoted outside its owning artifact goes stale silently" — the record's §3 correction says exactly this about itself). Then regenerate `WAVE-A-MANIFEST.txt` by script, re-quote the §1 Wave A argument, and re-run this wave's review against the new bytes.

**Suggested check to add:** CG-7 currently validates digests. Add a predicate that fails when any file under `rfcs/` contains a ceremony phrase string not currently live in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 — mutate-and-confirm it fails by planting the retired phrase in a fixture.

---

## B2. Performing Wave A puts non-contract material inside `contracts/`, violating the "exclusively" rule of the clause the same act binds

**Anchor — RFC3-15**, `governance-homes-and-owner-acts.md:73–81`:

> **RFC3-15.** The **five** constitutional categories of `.syzygy/governance/` hold, **exclusively** — "exclusively" bounding what each category may contain …

and the `contracts/` row's *May contain* cell: "Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts."

**Anchor — acceptance record §2 step 3**, which the Wave A ceremony executes:

> **Companion material, installed but not accepted:** the first wave act's install also copies `history/` and `matrix-rows/` to `.syzygy/governance/contracts/history/` and `…/matrix-rows/` …

> **Repaired at round-2026-08d in the ceremony, not the modules**: the first wave act's install additionally copies `CONTEXT-BUDGET-REPORT.md` and `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` to `.syzygy/governance/contracts/`

**Failure scenario, concrete.** The owner writes the Wave A phrase. Step 3 completes. `.syzygy/governance/contracts/` now contains: `rfcs/` (19 accepted modules — conforming), plus `history/` (**12 files**, whose own README opens "Nothing in this directory binds"), `matrix-rows/` (**9 files**), `CONTEXT-BUDGET-REPORT.md`, `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`, `ACTIVE-CONTRACT-MANIFEST.txt`, and `wave-manifests/`. None of those is an accepted load-bearing contract. [Observed — file counts recomputed in the clone.] A conforming plane validator built from RFC3-15's own "exclusively" flags the category the instant act 1 finishes.

The record anticipates the objection and answers the wrong question: it says the companion material is "**non-normative** … and carry no authority". RFC3-15's "exclusively" bounds **containment**, not authority. And RFC3-15(a) states the drafters' own precedent against exactly this move:

> The fifth category is an explicit widening of a structure this RFC calls constitutional, made by owner amendment rather than **by stretching a category's "exclusively"** — the precedent any future widening follows.

So the ceremony does to `contracts/` precisely what B19 refused to do to the other four.

**Why blocking.** The owner's first act produces a tree that is non-conforming to the first clause it bound. That is the definition of a surprised act rather than a knowing one. `CG-14` does not catch it — it "checks install *routes* only", per the record's own note.

**Repair — three lawful options, pick one and state it at the gate:**
1. **Move the companions out of the category.** Install `history/`, `matrix-rows/`, and the two generated reports to a sibling outside the five (e.g. `.syzygy/governance/contracts-companion/`) — but note that adds a seventh name under `governance/` and RFC3-15's validator "accepts exactly these six names and rejects a seventh", so this needs the companions to sit outside `governance/` entirely, or
2. **Amend RFC3-15's `contracts/` *May contain* cell** to admit, by name, the non-normative package apparatus an accepted package carries with it (manifests, per-RFC history, migration rows, generated budget/compaction reports), stated as a bounded list — the explicit-widening route RFC3-15(a) mandates, or
3. **Drop the companion copies from the ceremony** and repair the six package READMEs' backlinks in the modules instead — the option round-2026-08d explicitly declined ("repaired … in the ceremony, not the modules"), noted for completeness.

Option 2 is the one RFC3-15(a)'s own precedent points at, and it is a normative edit to a Wave A module, so it forces the same regenerate-and-re-review cycle as B1. Batch it with B1 (verification rule 10).

---

# MAJOR

## M1. RFC1-25's `succeeds` row cannot be resolved by RFC1-25(d), and its semantic class is not a value in RFC1-25's closed class vocabulary

**Anchor — RFC1-25 table, line 502:**

> | `succeeds` | Successor identity → predecessor identity | **Desired (declared) for declared classes; derived for Contradiction successors (RFC1-18(b)), recorded inside the minting evaluation's observation record** | The split/merge continuity edge (RFC1-11); the same relation carries contradiction membership drift, where no declaration act exists to carry it |

**Anchor — RFC1-25(d), lines 566–589:**

> A **typed relation** is one (relation name, ordered endpoint-domain pair) combination from the RFC1-25 table: each row contributes one typed relation **per endpoint pair it lists**. … **a single-pair row names exactly one.**

> every typed relation carries as explicit metadata its **ordered endpoint domains** (domain → range entity kinds) and its **semantic relation class** (RFC1-25's closed class vocabulary). The class is the RFC1-25 table's value **resolved per endpoint pair** — per-pair resolution is what discharges the table's "Varies by endpoint," "Matches endpoint," and "Follows the containing authority" entries into a single class per typed relation.

Three failures compose:

1. `succeeds` lists **one** endpoint pair, so by RFC1-25(d) it "names exactly one" typed relation, which must carry **one** class. Its cell carries **two**.
2. The split is by **subject class** (declared classes vs Contradiction), not by endpoint pair — so per-pair resolution, the only discharge mechanism RFC1-25(d) provides, cannot separate them. RFC1-25(d) names three dischargeable entries; `succeeds`'s cell is none of them.
3. The closed class vocabulary at RFC1-25 lines 453–473 enumerates: Desired/Desired (declared), Proposed, Observed, Inferred, Execution, Derived, Governance act, "Declared … or inferred" (composite), "Desired → execution", plus the three resolution rules. **"Desired (declared) for declared classes; derived for Contradiction successors" is not among them** — and it is not the sanctioned composite either, since that composite is specifically "two queryably distinct *derivation sources*, disclosed per edge", which is `implements`/`realizes`, not a subject-class conditional.

Separately, RFC1-25(d) requires ordered endpoint **entity kinds** as metadata; `succeeds`'s domain→range reads "Successor identity → predecessor identity", which names no entity kind at all.

**Failure scenario.** An implementer builds the typed-relation registry RFC1-25(d) mandates. Every other row resolves. `succeeds` does not: they must either mint two typed relations under one endpoint pair (breaking RFC1-25(d)'s "a single-pair row names exactly one"), or pick one class and lose the Contradiction-successor semantics RFC1-18(b) depends on, or invent a subject-class dispatch RFC1-25(d) does not authorize. Two conforming implementations will choose differently, which is the exact divergence RFC1-25(d) exists to prevent. The consequence is not cosmetic: RFC1-18(b) makes contradiction membership drift travel on `succeeds` as a **derived** edge that is "a fact only when recorded inside an identified observation record", while the declared-class `succeeds` is a Desired-plane declaration — different truth conditions, per RFC1-22's closure.

**The drafters solved this problem one row earlier and did not carry it across.** `supersedes` (line 501) handles the identical shape correctly: it enumerates "for each identity-bearing class … exactly the pair (that class → prior version of the same class)" and takes the named resolution rule "Matches endpoint", so per-pair resolution discharges it. `succeeds` was left generic.

**Repair.** Mirror the `supersedes` construction. Restate `succeeds`'s Domain → Range as same-class pairs — "for each identity-bearing class whose RFC1-11 or RFC1-18(b) lifecycle mints successors, exactly the pair (that class → predecessor of the same class)" — and set the class cell to the resolution rule **"Matches endpoint"**, with the Rule cell carrying: declared classes resolve to Desired (declared); the Contradiction → Contradiction pair resolves to Derived per RFC1-18(b), recorded inside the minting evaluation's observation record. That adds no relation and re-types none (RFC1-26 untouched); it makes explicit the endpoint pairs the row already implies, exactly as RFC1-25(d)'s own reading of the table does elsewhere. Note this **is** a normative edit and should be batched with B1/B2.

## M2. RFC 0005's "deterministic" lookup rule does not resolve RFC5-27 and its exhaustiveness claim is false

**Anchor — `RFC-0005/README.md:57–60`:**

> **Lookup rule (deterministic).** For any citation `RFC5-n`, read `n` as an integer: `1–11` → module 1; `12–17` → module 2; `18–23` → module 3; **`24–26`** → module 1. **The four ranges are contiguous and exhaustive over RFC5-1…RFC5-27 with no gaps**, so the rule never needs a search.

The four stated ranges cover 1–26. **RFC5-27 falls through the rule.** The exhaustiveness sentence is false as written. [Observed]

This is not a stray number. RFC5-27 is the package's **phase-boundary clause** — the same README's own front matter names it: `implementation_boundary: {kind: requires-openspec, clause: RFC5-27}`; module 1's front matter and closing line both correctly say `RFC5-1..RFC5-11, RFC5-24..RFC5-27`; and the acceptance record §"Acceptance schedules no implementation" lists RFC5-27 among the eleven binding phase-rule clauses. So the one clause the record leans on to say "acceptance schedules no implementation" is the one clause the package's stated lookup rule cannot locate.

**Failure scenario.** A reader or a tool implements the rule as written to resolve `RFC5-27` — the citation the acceptance record itself makes — and gets no module. The rule promises "never needs a search"; here it needs one, and the reader has been told not to.

**Repair.** `RFC-0005/README.md:58` — change `` `24–26` → module 1 `` to `` `24–27` → module 1 ``. Normative-adjacent index text inside the digest set, so it rides the same regeneration.

## M3. RFC6-19 class 8 carries an undisclosed normative forward reference into RFC 0008, and routes chain state away from the in-wave clause that defines it

**Anchor — RFC6-19, drawer content class 8** (`RFC-0006-…md:307–311`), a normative enumeration of what the single fact set **contains**:

> 8. **Work and reconciliation state** — where work bears on the selection, the relevant items' normalized work state (**RFC8-12**) and chain state (**RFC8-28**), carried as two fields, never folded, and never rendered as proof of satisfaction …

At position 1, RFC 0008 is not bound. Two distinct problems:

**(i) No staging.** RFC 0001 and the RFC 0002 package each carry an explicit "**Forward references are informative** … informative until that RFC is accepted" paragraph. **RFC 0006 carries none.** I swept all 19 modules for any staging language (`informative until` / `Forward references are informative` / `forward citation`): **3 of 19 files carry one** — RFC-0001, RFC-0002/README (package-level, covering its four modules), and RFC-0002/snapshot-and-evaluation-core. [Observed] RFC 0006 is not among them, and RFC 0006's own §5 Integration lists reliances on RFC 0001 and RFC 0002 only, while its front matter reads `depends_on: [RFC-0001, RFC-0002]`. So the package's own dependency self-description denies a normative reference its clause text makes.

**(ii) The chain-state citation points at the wrong wave.** Chain state is defined **in Wave A**, at RFC2-18 ("Every materialized work item that reaches merge enters a first-class chain … `merged → reconciliation-pending → …`"). RFC6-19 class 8 cites **RFC8-28** for it. So a clause the owner binds at act 1 routes the reader to a not-yet-bound contract for a concept act 1 itself supplies — and RFC6-19's own class-8 tail then cites RFC2-18/RFC2-19 correctly for "the selection's reconciliation state", two lines later. The row is internally split on where chain state comes from.

**Failure scenario.** An implementer building the drawer at position 1 reads class 8, finds RFC8-28 unavailable, and has no clause telling them whether the obligation is inert (informative-until-accepted) or binding-but-unsatisfiable. RFC 0001's rule would have told them; RFC 0006 says nothing.

**Repair.** Two edits to `RFC-0006-…md`:
- In class 8, cite **RFC2-18** for chain state (RFC8-28 may follow parenthetically as the Trajectory rendering of it), and mark the normalized-work-state limb as conditioned on RFC 0008 — e.g. "the relevant items' normalized work state (RFC8-12 — informative until RFC 0008 is accepted) and chain state (RFC2-18; rendered per RFC8-28)".
- Add a **Forward references are informative** paragraph to §5, in the RFC 0001 / RFC 0002 form, naming RFC8-n and RFC9-n, and correct `depends_on` to include `RFC-0004` (RFC6-19 class 7 normatively cites RFC4-2 for the coverage boundary).

## M4. The RFC 0003 package carries no forward-reference staging note at all, and one downstream citation sits inside a normative "exclusively" enumeration

RFC 0003 has **14 non-shape-parallel citations into RFC 0007–0011** and **zero staging language**. [Observed — Python `re` sweep, denominator 3 files / 19 modules.] Breakdown: `governance-homes-and-owner-acts.md` — RFC7-21, RFC7-25, RFC7-30, RFC7-31, RFC8-12, RFC8-16, RFC9-18 ×2, RFC9-26 ×2, RFC9-45 ×2, RFC10-9; `manifests-and-namespace.md` — RFC7-37.

Most are honestly self-staged **by their own clause text**, and I want that credited rather than swept in: RFC3-16(a)'s example list says "**That predicate is the scope; the list below is not**" and "non-exhaustive examples, load-bearing as illustration and never as the boundary"; the gate inventory ends "**This list tracks the gates; it does not bound them.**" Those are the right shape and they hold at position 1.

**The one that is not staged is normative containment.** Anchor — RFC3-15, `records/` row (`governance-homes-and-owner-acts.md:89`), inside the table introduced by "hold, **exclusively**":

> | `records/` | Kernel-authored durable facts minted on a non-owner actor's submission … : **challenge submissions** …, their admission and rejection records and submitted withdrawals (RFC2-13), and **walkthrough execution records** (the fact a comprehension walkthrough ran and what it walked — **RFC7-30, RFC9-45**) | …

At position 1 the `records/` category's exclusive contents include an artifact class whose defining clauses are in Wave B. The practical effect is benign (nothing of that class can exist yet), but the clause is stated in the present indicative with no marker, and RFC3-15 is the clause a conforming plane validator is built from. A validator author at position 1 must decide whether to admit a walkthrough execution record on the strength of a citation to nothing.

**Repair.** Add a short package-level *Forward references are informative* paragraph to `RFC-0003/README.md` in the RFC 0002 form, and in RFC3-15's `records/` cell mark the third item: "walkthrough execution records (RFC7-30, RFC9-45 — the class exists only where those contracts are accepted)". The RFC1-7 mission-profile clause is the model to copy; see part 3.

## M5. Wave A installs a package-identity record naming 20 modules that are not in the tree

**Anchor — acceptance record §2 step 3:**

> the first wave act also installs `ACTIVE-CONTRACT-MANIFEST.txt` beside it as the package identity record

**Measured:** `ACTIVE-CONTRACT-MANIFEST.txt` has **39 rows**; **20 of them name files Wave A does not install**. Its own header line 2 reads "sha256 per active module, **39 modules**" with no statement that installation is partial. [Observed]

**Failure scenario.** Act 1 completes. `.syzygy/governance/contracts/` — the category RFC3-15 defines as holding "**Accepted** load-bearing contracts" — contains a manifest asserting 39 active modules, 20 of which are neither present nor accepted. Anyone running `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` from the installed directory (the natural generalization of the step-3 verification the record teaches) gets 20 "No such file or directory" lines. The ceremony's own check is `sha256sum -c wave-manifests/WAVE-A-MANIFEST.txt`, which passes, so nothing in the ceremony surfaces this. Under RFC3-16, "is this accepted?" is supposed to be answerable from the owner-act record; here the governed tree's *package identity record* answers a different question in a way that reads as an inventory of the accepted set.

**Repair.** Either (a) defer the `ACTIVE-CONTRACT-MANIFEST.txt` install to the final wave act and have each wave act append to a generated `INSTALLED-WAVES.txt`, or (b) install it at act 1 with a generated banner line — written by `build_active_manifest.py`, never hand-edited — stating that it is the six-wave package identity, that installation proceeds wave by wave, and that only the wave manifests present alongside it describe installed content. (b) is cheaper and keeps the identity record's single home; either way the fix is in the generator and the record, not in a Wave A module, so it does **not** move the Wave A digest.

RD-18 Wave A **(part 3/3)** — minor findings, exact-package judgment, verdict.

---

# MINOR

## m1. Three self-descriptions in RFC 0003 state the clause range as RFC3-32; the range is RFC3-33

Verbatim [Observed]:
- `manifests-and-namespace.md:14` — `## Module: manifests and namespace (RFC3-1…RFC3-14, RFC3-18…RFC3-32)`
- `manifests-and-namespace.md:61–62` — "this module holds RFC3-1…RFC3-14 and RFC3-18…**RFC3-32**."
- `governance-homes-and-owner-acts.md:505` — "Every other number in RFC3-1 … **RFC3-32** is in `manifests-and-namespace.md`."

The correct bound appears three other places: both front matters, the README lookup rule ("Every other number in RFC3-1 … RFC3-33"), and `manifests-and-namespace.md:622`'s closing line ("RFC3-1 … RFC3-14 and RFC3-18 … RFC3-33"). RFC3-33 is the package phase-boundary clause, defined at `manifests-and-namespace.md:487`. **Failure scenario:** a reader resolving `RFC3-33` from the module heading or the governance-homes closer concludes it lives in neither module. **Repair:** `RFC3-32` → `RFC3-33` at those three sites.

## m2. RFC 0004's package index closes on the wrong clause bound

`RFC-0004/README.md:222` — "*End of RFC 0004 package index. Clauses **RFC4-1 … RFC4-29**, with sub-clauses RFC4-13(a) and RFC4-13(b)…*" — while the same file's front matter says `RFC4-1..RFC4-30`, its clause map assigns `RFC4-22..RFC4-30` to module 4, and its `implementation_boundary.clause` is `RFC4-30`. RFC4-30 is defined at `fidelity-joins-and-mappings.md:185`. **Repair:** `RFC4-29` → `RFC4-30`.

## m3. Acceptance record §7 item 9 makes a false absence claim

> 9. **Single-source structure, disclosed** (safety review): **RFC 0001–0009 never cite RFC-0010/0011**, so the no-self-widening rule has no redundant restatement inside the nine earlier contracts.

Swept with Python `re` over every RFC 0001–0009 module file: **denominator 30 files; 22 contain an RFC-0010/0011 citation.** [Observed] Most are the shape-parallel tails (`RFC10-16, RFC11-12`), which verification rule 5 correctly says are not dependency edges — but not all are: `RFC-0003/governance-homes-and-owner-acts.md:282` cites **RFC10-9** substantively ("RFC10-9 is the worked example"), `RFC-0004/fidelity-joins-and-mappings.md` cites RFC 0011 in §5, `RFC-0009/semantic-geography.md:147` cites **RFC10-15**, and `RFC-0005/admission-and-boundary.md` names RFC-0010/RFC-0011 in its front matter `constrains` list.

The *conclusion* the item draws still holds — I found no restatement of a no-self-widening rule in any Wave A module — but the premise as written is false, and this is exactly what verification rule 9 exists for. It sits in the section the owner reads at the gate. **Repair:** restate as measured — "no contract in RFC 0001–0009 *relies on* RFC-0010/0011; the citations that exist are the shape-parallel phase-rule tails plus N named informative references (enumerated), so the no-self-widening rule has no redundant restatement…" — with the sweep and its denominator recorded. This is outside every wave digest, so it costs no regeneration.

## m4. RFC4-13 quotes CC-TEST-2 as already amended; that amendment is act 2, unperformed at Wave A

`named-adapters.md:196–200`: "Craft-and-care states the routes-1-and-2 capture side of this rule — '…' (**CC-TEST-2, amended at the rev7 rework to name routes 3 and 4** as the owner-created exceptions with their own guards)". Record §1 act 2 is `CONFIRM CRAFT AMENDMENT: CC-TEST-2@7a716090…` — i.e. the amendment is a separate, later gate. At position 1 the clause asserts in the present tense that an unconfirmed amendment exists in its amended form.

I rate this **minor, not major**, for one reason and I want the reason on the record: the same sentence ends "**and this clause carries the full four-route model**", so RFC4-13 is self-standing and the CC-TEST-2 reference is corroborative, not load-bearing. **Repair (optional, batch only):** "(CC-TEST-2, whose rev7 amendment naming routes 3 and 4 is confirmed by its own owner act)". Two Wave A modules cite craft: this one and `manifests-and-namespace.md:373` (CC-REV-1, whose force begins at act 1 — no issue).

## m5. RFC 0006's `depends_on` omits RFC-0004

Front matter reads `depends_on: [RFC-0001, RFC-0002]`, but RFC6-19 class 7 normatively cites **RFC4-2** for the coverage boundary the drawer must carry. Same file, same fix pass as M3. (Both RFC-0004 and RFC-0006 are in this wave, so this does not disturb the record's "every `depends_on` edge stays inside the wave" claim — which remains true, and would remain true after the correction.)

## m6. Noted and cleared, not a finding

RFC2-25's `editorial-draft` paragraph attributes its wording to RFC 0007 and cites RFC7-20. I checked whether this is unstaged: it is not — the RFC 0002 **package** README's staging paragraph reads "Where **this package** cites a sibling *draft* by clause number (RFC3-n, RFC4-n, RFC5-n, **and the surface RFCs**) … informative until that RFC is accepted", which reaches module 4. Correctly handled. Recording it so a later reviewer does not re-raise it.

---

# 3. Exact-package judgment

## (a) Is Wave A independently acceptable standing alone at position 1?

**Structurally, yes — and by a clearer margin than I expected.** [Observed]
- Every `depends_on` edge of all 19 modules stays inside the wave (verified, part 1).
- No package is split: all four multi-module packages (0002, 0003, 0004, 0005) are wholly inside the wave.
- All 44 relative backlinks resolve after the documented install.
- The clause namespace partitions cleanly with no duplicate identity.
- RFC5-18(a)'s gate limb — "(a) this RFC is accepted" — is satisfied by this act itself, so the SEC-3 execution unblock is coherent at position 1.

**Complete enumeration of normative reliance on not-yet-bound artifacts, and how each is staged:**

| Reliance | Where | Staged honestly? |
|---|---|---|
| RFC 0009 — unmapped district, governance-answer rule (RFC9-4, RFC9-19, RFC9-20 ×2, RFC9-44 ×2) | RFC1-25 `placed_in` row; RFC1-25(c) | **Yes** — RFC 0001 §5's "Forward references are informative … informative until that RFC is accepted" names RFC9-n explicitly |
| RFC 0007 — composite maturity addressee (RFC7-16 ×2); `editorial-draft` wording (RFC7-20) | RFC 0002 README §7; RFC2-25 | **Yes** — RFC 0002 README's package-level staging paragraph covers "the surface RFCs" |
| RFC 0008 — `active` unrenderable until the staleness bound is declared (RFC8-16) | RFC4-23(2); disclosed at `fidelity-joins-and-mappings.md` §5 | **Partly** — §5 names it "a forward citation into RFC 0008" by name, which is honest disclosure, but stops short of stating its force at position 1 |
| RFC 0007/0008/0009/0010 — RFC3-16(a) example list and gate inventory (RFC8-12, RFC8-16, RFC9-18, RFC9-26, RFC9-45, RFC7-21/25/31, RFC10-9) | RFC3-16(a), RFC3-16(b) | **Yes, by clause self-statement** — "the list below is not [the scope]"; "This list tracks the gates; it does not bound them" |
| RFC 0007 — narrative-side twin obligation (RFC7-37) | RFC3-32 | **Yes** — stated as a parallel, not a dependency |
| RFC 0007/0009 — walkthrough execution records (RFC7-30, RFC9-45) | RFC3-15 `records/` row, inside an "exclusively" enumeration | **No** — **M4** |
| RFC 0008 — normalized work state and chain state as required drawer fields (RFC8-12, RFC8-28) | RFC6-19 class 8 | **No** — **M3**, the worst of the set |
| RFC 0009 — layout baseline (RFC9-14), historical-map design (RFC9-41 ×2) | RFC6-24, §7 | **Partly** — RFC9-41 self-stages ("nothing in this clause depends on it"); RFC9-14 does not, but is a distinguish-from, not a rely-on |
| Craft — CC-TEST-2 amendment (act 2) | RFC4-13 | **Partly** — **m4**; the clause states it carries the full model itself |
| Topology bundle (act 3) | — | **No reference anywhere.** Sweep for `topology-candidates` / `map/topology` / `BUNDLE-MANIFEST` across all 19 modules: **zero hits** [Observed] |

Twenty-five of the 55 downstream citations are the shape-parallel phase-rule tails `(Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12.)` — per verification rule 5 these are not dependency edges, and I have not counted them as reliances.

**The model the corpus should copy is already in it.** RFC1-7 gets this exactly right:

> **mission** (Mission and Attention Item identities and their relations …; **loadable only where the Mission contracts (RFC 0010 and successors) are accepted and active** for the project or workspace, and never part of any project's unconditional V0 core)

That is a reliance made conditional on the act that will bind it. RFC6-19 class 8 and RFC3-15's `records/` row need the same sentence shape.

**So: structurally acceptable, but not acceptable as it stands** — because of B1 and B2, which are not about cross-wave staging at all. They are about the act misdescribing its own ceremony and producing a tree its own newly-bound clause forbids.

## (b) Does the acceptance record describe Wave A accurately?

Mostly yes, and its honesty about its own state is genuine. Specifically verified: the phrase and argument match the manifest byte-for-byte; "19 modules of RFC 0001–0006" is exact; the `depends_on` containment claim holds; §2 step 2's verification procedure is executable as written and I executed it; step 3's install routes pass CG-14 and produce zero broken backlinks; §"Acceptance schedules no implementation" correctly lists RFC6-28 and RFC5-27 among the eleven phase-rule clauses, and all five Wave A phase-rule clauses (RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28) exist and bind their packages.

Above all, the wave-history note is **not** the stale-offering failure RD-8 named — it states plainly that "**no confirming review is yet bound to any wave argument above**" and that the round's fresh-context pass is owed. No retired phrase is presented as live *in the record*. The retired phrase is presented as live **inside the package** (B1), which the record cannot see.

Two record-level defects: the false absence claim at §7 item 9 (**m3**), and the `ACTIVE-CONTRACT-MANIFEST.txt` install (**M5**).

## (c) Are the package self-descriptions accurate?

Clause maps, module lists, lookup tables, front-matter clause sets, "no lettered sub-clauses" claims for RFC 0002 and RFC 0005, and the twelve/six/nine closed-vocabulary counts (RFC2-24 twelve reasons, RFC2-25 six tiers + three sibling states, RFC6-5 nine outcomes) all check out against the bytes. The six package READMEs correctly state no volatile measurements — CG-21 confirms "39 modules examined, 0 findings", and the R1 defect the record describes as closed is genuinely closed.

The failures are **M2** (RFC 0005's lookup rule missing RFC5-27 plus a false exhaustiveness claim), **m1** (three RFC3-32 sites), **m2** (RFC4-29), and **m5**.

## (d) Internal contradictions that would make the act surprised rather than knowing

**B1**, **B2**, **M1**, and **M2** each qualify. B1 and B2 are the ones that turn the act itself into a surprise: the owner writes a phrase and binds a clause naming a different, retired phrase, then watches the install produce a `contracts/` directory that violates the containment rule that clause states. M1 is a contradiction between two clauses of the same section, both load-bearing on the closed relation vocabulary. M2 breaks a rule the package advertises as deterministic.

Everything else is repairable text that would not have surprised the owner in a way that changes what they meant to do.

---

# Summary

| # | Severity | Finding | Moves the Wave A digest? |
|---|---|---|---|
| B1 | blocking | RFC3-15 names the retired `ACCEPT COMPACTED FOUNDATIONAL RFCS` phrase as the live install gate, and describes one act where there are six | **yes** |
| B2 | blocking | The Wave A install puts `history/`, `matrix-rows/` and two reports inside `contracts/`, against RFC3-15's "exclusively" | yes, if repaired by amending RFC3-15 |
| M1 | major | RFC1-25 `succeeds` is unresolvable under RFC1-25(d) and its class is outside the closed vocabulary | **yes** |
| M2 | major | RFC 0005 lookup rule omits RFC5-27; exhaustiveness claim false | **yes** |
| M3 | major | RFC6-19 class 8 forward-references RFC8-12/RFC8-28 unstaged; chain state routed away from RFC2-18 | **yes** |
| M4 | major | RFC 0003 has no staging note; RFC3-15 `records/` cites RFC7-30/RFC9-45 inside an "exclusively" list | **yes** |
| M5 | major | `ACTIVE-CONTRACT-MANIFEST.txt` installed at act 1 names 20 absent modules | no |
| m1 | minor | Three `RFC3-32` self-descriptions; range is RFC3-33 | yes |
| m2 | minor | RFC 0004 README closes on `RFC4-29`; range is RFC4-30 | yes |
| m3 | minor | Record §7 item 9 absence claim false (22 of 30 files) | no |
| m4 | minor | RFC4-13 states CC-TEST-2's amendment as done; it is act 2 | yes |
| m5 | minor | RFC 0006 `depends_on` omits RFC-0004 | yes |

Nine of the twelve require edits inside the digest set. Per verification rule 10, batch every one of them into a single pass, regenerate the wave manifests **by script**, re-quote §1's Wave A argument, and bind a fresh review to the new bytes — do not fix B1 alone and let the rest ride.

I want to be clear about what I am not saying. The wave decomposition itself is sound, the digests are correct, the ceremony's mechanics are executable and I executed them, and the package is internally far more coherent than the finding count suggests. The blocking items are two places where the act's own paperwork and its own first clause disagree about what the act is — and both are unfixable after the act, which is the only reason they outrank M1.

VERDICT: REVISE
