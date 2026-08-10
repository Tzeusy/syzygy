# RD-31 — Wave A exact-package review (round-2026-08e, frozen commit cd484b7)

## 1. Subject identification — recomputed, not transcribed

Clone: `/tmp/claude-1000/-home-tze-GitHub-syzygy/3fa62952-e192-440e-8b1f-5b48212d8da1/scratchpad/clone-08e-r8`, `git rev-parse HEAD` = `cd484b7d782a253c5f94152f0183a78b7678064f`, working tree clean (`git status --porcelain` empty). Nothing outside this clone was read; the live repository at `/home/tze/GitHub/syzygy` was not consulted.

| Quantity | Value | How obtained |
|---|---|---|
| `wave-manifests/WAVE-A-MANIFEST.txt` sha256 | `c649143bdac1a883874e4d9d57d76a031a6e9b2f9357d12ea1f5b9484a48b8dd` | `sha256sum`, then recomputed independently in Python `hashlib` |
| Expected by the commission | identical | **[Observed]** match |
| §1 row A quoted argument | identical, extracted by Python `re` from the record, not read by eye | **[Observed]** match |
| Manifest rows | 19 | computed |

**[Observed]** The subject is the exact package the phrase `ACCEPT FOUNDATIONAL WAVE A: c649143b…` would bind. I proceeded.

## 2. Method

All 19 modules read in full. Every "zero / all / none" claim below states the sweep and its denominator and was run this session. All load-bearing pattern work used Python `re` or `grep -F`, never a bracket class (rule 1). Every finding is anchored to a quoted clause, not to prose near one (rule 8). Checks were read by output, not exit code (rule 4). Context read after the subject: `AGENTS.md`, `doctrine/vision.md`, the acceptance record §§1, 2, 7 (and §§3, 5, 6 in passing), `DEFERRED-WAVE-POSTURE.md`, `round-2026-08e/WAVE-A-SEMANTIC-DELTA.md` §§9, 10, 11, 12, 13, 14, and `decisions/PENDING-OWNER-DECISIONS.md` including its launch-scope index. No file was edited or created anywhere.

---

## 3. Findings

### RD31-01 — BLOCKING. The RD26-04 `records/` widening contradicts the very clause it cites as its authority

The repair gave the expiry-*resolution* act a lawful home by widening RFC3-15's `records/` cell. The widened cell (`rfcs/RFC-0003/governance-homes-and-owner-acts.md:89`) reads:

> **Kernel-authored durable facts minted on a non-owner actor's submission, or by the pre-declared deterministic challenge-sweep policy resolving an expiry-eligible challenge as `expired` (RFC2-13; owner decision B1 — the sweep's policy lives in `policies/`, its resolution record here, and that record is the new snapshot's authoritative input)** (the only minting triggers — **see RFC3-2's transition rule**; expiry *eligibility* derives at evaluation and mints nothing)

It names RFC3-2 as the owner of the trigger set. RFC3-2's transition rule (`rfcs/RFC-0003/manifests-and-namespace.md:129-131`) states a **narrower closure**:

> **Which lifecycle transitions mint a record.** A `records/` fact is minted **only on an actor's submission** — a challenge submitted (and its admission or rejection), a withdrawal submitted, a walkthrough run submitted.

A deterministic policy sweep is not a submission and has no submitting actor. Four sentences later the same clause names it anyway (`:140-145`): "a human resolution in `decisions/`, or the pre-declared deterministic policy sweep's resolution record in `records/` (RFC3-15's `records/` cell names it)". The two clauses point at each other and state different sets: RFC3-15 says the triggers are two and cites RFC3-2; RFC3-2's closure sentence enumerates three submissions and excludes the second trigger. The package's own README makes the deference explicit (`rfcs/RFC-0003/README.md:84`): "the minting-trigger rule is at RFC3-2 and cited by RFC3-15's `records/` row."

**[Inferred]** Failure scenario: a conforming plane validator implementing RFC3-2's "only on an actor's submission" rejects a sweep resolution record; one implementing RFC3-15's cell accepts it. Where it is rejected, RFC2-13's B1 resolution act has no home and the expiry-eligible challenge suspends forever — which is exactly the defect RD26-04 set out to repair. Two conforming implementations disagree on the admissibility of the record the repair exists to create.

Compounding it, **[Observed]** RFC3-2's own justification for why eligibility mints nothing applies verbatim to a *deterministic* sweep resolution: eligibility "involves no act and is reproducible from snapshot inputs the tree already holds, so minting it would add a snapshot input (RFC2-1 item 9) that pure recomputation created." A pre-declared deterministic sweep over a declared bound and an admission instant is reproducible on the same terms. Either the sweep resolution is reproducible — and RFC3-2's stated reason bars minting a record for it — or it is not, and it is a judgment act that does not belong in `kernel-recorded`. Neither branch supports the cell as written.

`verify_final_prespec.py` and `check_governance.py` do not reach this: no check compares a widened enumeration against the clause it names as its authority.

### RD31-02 — BLOCKING. §7 item 11 forbids this offer, and P-33 is unruled

The acceptance record's own §7 item 11 (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:498-500`):

> **Until P-33 is ruled, this record offers no Wave A act** — performing act 1 over the current step 3 would freeze an install that breaches a clause the act binds.

**[Observed]** P-33 sits in `decisions/PENDING-OWNER-DECISIONS.md`'s table headed "**Open, and only the owner can dispose**" (row `P-33`, line 179), with its own "Earliest gate: before Wave A is re-offered". The launch-scope index (line 124) lists it under "**Gate the Wave A offer**" alongside P-31, P-37 and P-28. Neither of P-33's two sub-choices has been ruled or drafted; the semantic delta's own handoff 6 says so plainly: "**P-33 arms are undrafted** (RD-18 B2, M5)".

This is a gate, not a byte defect — and the record's honesty here is a strength, not a fault. But it is dispositive of the question I was asked. The bytes may be perfect and the act still may not be offered, because the record that owns the offer says it is not offered. §1 row A and §7 item 11 currently read against each other; §2 step 0 makes §7 the controlling reading, so the record is internally lawful, but the phrase in §1 is not currently on offer.

### RD31-03 — MAJOR. The RFC 0002 package index denies the sub-clause the RD-30 batch minted, at three sites, one of them a deterministic lookup rule

The RD-30 batch (delta §14) minted `RFC2-19(a)` "so it is anchorable under verification rule 8", and edited **one** module: `RFC-0002/reconciliation-chain.md`, whose front matter now declares `clauses: RFC2-15..RFC2-22 (sub-clause RFC2-19(a); …)`. The package index was not updated and now contradicts its own module at three sites, all inside the bound bytes:

1. `rfcs/RFC-0002/README.md:7` — `clauses: RFC2-1..RFC2-26 (contiguous; **no sub-clauses**, no gaps, no retired numbers, no merges)`
2. `rfcs/RFC-0002/README.md:59-61` — under the heading **Lookup rule (deterministic)**: "**RFC 0002 has no lettered sub-clauses** — every `(a)`/`(b)` appearing in its text cites another contract — so the integer alone always resolves."
3. `rfcs/RFC-0002/README.md:266` — "No lettered sub-clauses, no retired numbers, no merged numbers, no gaps in the range".

Site 2 is the harmful one. **[Inferred]** Failure scenario: a reader — the owner following §7 item 12 to the drafted arm, or any later citer — resolves `RFC2-19(a)` through the package's own deterministic lookup rule and is told the token cites *another contract*. The one repair whose stated purpose was anchorability is undercut by the index a citer consults to anchor it.

Two corroborations that this is not cosmetic. **[Observed]** The generated `05-CONTRACT-INDEX.yaml` carries `{id: RFC2-19(a), module: RFC-0002/reconciliation-chain.md, kind: normative}` — the generated view and the bound contract byte now disagree about whether the clause exists. And **[Observed]** `check_governance.py`'s CG-17 sub-clause extractor treats exactly this sentence shape as authoritative: its denial regex is `\bno lettered sub-clause|\bnot\s+(?:separate\s+)?sub-clauses?\b`, so the checker's own machinery is designed to *believe* a statement of this form. CG-17's population is the 210 surface clauses of RFC 0006–0011, so RFC-0002 escapes it — the sentence is false and unchecked, not false and caught.

RFC-0004 shows the correct handling: its README front matter carries `sub-clauses RFC4-13(a), RFC4-13(b)` and its module agrees. RFC 0002's index was simply not swept after the mint. Denominator: 19 modules; 1 module carries a declared sub-clause; 1 package index contradicts it; 3 sites.

### RD31-04 — MAJOR. The widened cell routes an un-suspending record into the one category with no install gate, while its co-equal human counterpart is gated

RFC2-13 (`challenge-lifecycle.md`) makes the two resolution authorities co-equal and gates the sweep policy:

> **Resolution authority:** a human, or a deterministic policy declared in `.syzygy/governance/policies/` before the challenge was admitted. Such a policy is a resolution authority **co-equal with a human**, so it is honored **only under RFC3-16(a)**

The same clause names the exposure it is guarding: "a worker-minted resolution or sweep policy would un-suspend wholesale, without any human act, every claim an admitted challenge conservatively suspended to Unknown."

The repair then splits the two co-equal authorities across two homes with different gates. RFC3-2 sends the human's act to `decisions/` — "never minted into `records/`" — where RFC3-15's install-gate column requires "Recording by the owner". The sweep's act goes to `records/`, whose install-gate column (`governance-homes-and-owner-acts.md:89`) reads:

> **No install gate — these are recorded facts, not authorizations.** Minted by the kernel under its own rules; the *submission* they record is attributed, and the record itself is neither adopted nor adoptable

**[Observed]** That justification does not describe the new member: a sweep resolution record records no submission and is attributable to no actor. And RFC3-2 states a rule the new member appears to violate outright (`:125-127`): "Anything in this class that *would* authorize — a resolution policy, a sweep policy, an approval — is by that fact not in this class and falls under RFC3-16(a) instead." A record whose presence, as an authoritative snapshot input, lifts a suspension is squarely inside RFC3-16(a)'s predicate — "unblocks or widens a claim class".

**[Inferred]** The chain that partly saves this — the sweep *policy* lives in `policies/` and is gated, so a conforming kernel could refuse a resolution record not backed by a provenance-verified policy — is nowhere stated. Neither RFC3-15's cell nor RFC3-16's lifecycle row conditions the record on the policy's provenance. Compare RFC3-17(a), which does state the analogous safeguard for admission records: "an admission record's authority is the kernel's recomputation of the RFC2-13 check over the snapshot, never the file's own say-so." The sweep resolution record has no such sentence. §7 item 14(a) discloses the widening to the owner as a widening; it does not disclose that the widened member lands in the corpus's only ungated category.

### RD31-05 — MAJOR. Wave A ratifies the `constrains:` relation while P-21(a) is open, and §7 does not disclose it

**[Observed]** Sweep of all 39 `rfcs/` modules for the token `constrains` (Python `re`): the front-matter relation is declared on exactly two modules — `rfcs/RFC-0005/admission-and-boundary.md:10-11` (`constrains: [RFC-0006, RFC-0009, RFC-0010, RFC-0011]`, `constrains_source: RFC5-3`) and `rfcs/RFC-0007/narrative-contract.md:10-11`. **One of the two is a Wave A module.**

P-21's register row records that this relation "**was installed into candidate front matter while this question was still open** (RD-4 finding **F-17**), on two modules", and states "The (a) ruling — whether `constrains:` is the right relation at all — is still the owner's; **accepting Wave C2 ratifies the drafted arm**."

Two problems. First, the routing is wrong for the current posture: **[Observed]** Wave C2 is deferred and will not be offered (`DEFERRED-WAVE-POSTURE.md`), so the Wave A act is in fact the first and only act that would freeze this declaration into bytes an owner has bound. Second, §7 does not disclose it. The record's only mention (`:470-471`) is inside item 9 and says something else entirely — "(RFC-0005's front matter lists RFC-0010/0011 under `constrains:` — an outbound constraint edge, not a reliance.)" That is a statement about edge *direction*, offered to support a no-reliance claim. It does not tell the owner that the relation's existence is an unruled question, nor that the only clause defining what a consumer does with it (RFC11-16) sits in a deferred wave.

By §7's own charter — "lists what each act ratifies beyond its digest — drafted arms, disclosed rulings, **open questions riding in**" — this is an open question riding in undisclosed. It is not a reliance escape (nothing in Wave A evaluates the field), so it is MAJOR rather than BLOCKING; but it is the surprised-act shape §7 exists to prevent.

### RD31-06 — MINOR. RFC1-7's mission extension profile carries no in-place drafted marker

**[Observed]** RFC1-7 (`RFC-0001…:196-221`) states the mission profile in settled contract voice — "**mission** (Mission and Attention Item identities and their relations …)" — with no bracketed drafted note, no P-28 reference, and no "ratified or reverted at the act" sentence. Compare RFC2-19(a), which carries a blockquoted `[P-31 — drafted arm, awaiting an owner ruling.]`, and RFC4-19 §8 q2, which carries `**[Drafted 2026-08-10 (RD26-05):** … the owner ratifies or reverts it at the act]`. §7 item 16 discloses it at the record level, so the act can be knowing if §2 step 0 is honored; a reader of the module alone cannot tell. The three drafted answers in this package are marked in three different ways, one of them not at all.

### RD31-07 — MINOR. `manifests-and-namespace.md` declares an RFC-0004 dependency its own integration section does not claim, inconsistently with its repaired sibling

The delta's handoff 4 flagged this for me explicitly ("left as found (§6.2) — flagged for the fresh review, not repaired by inference"). **[Observed]** `rfcs/RFC-0003/manifests-and-namespace.md` declares `depends_on: [RFC-0001, RFC-0002, RFC-0004, RFC-0005]`; its §4 Integration names as reliances only RFC 0001, RFC 0002 and the package's other module. Its total RFC4-n citation count is **two** (`RFC4-12` ×1, `RFC4-16` ×1), both inside RFC3-30's illustrative policy list.

Its sibling `governance-homes-and-owner-acts.md` had precisely this shape repaired in this round (delta §10: "RFC-0003/governance-homes `−RFC-0004`") and now says so in text: "**Not a reliance:** RFC 0004. Every RFC4-n citation in this module sits inside RFC3-16(a)'s **non-exhaustive examples** or its gate inventory … and this module's front matter says so." Two modules of one package, one citation shape, two treatments. No wave escape results (RFC-0004 is in Wave A), and CG-13 passes because the README is the correct union of the two module sets — which is exactly why nothing catches it.

### RD31-08 — MINOR. Two disclosure artifacts name RFC2-19 rather than RFC2-19(a)

**[Observed]** §7 item 12 reads "RFC2-19 carries a drafted-awaiting-ruling arm" — the pre-mint wording; only §1 row A names the sub-clause. **[Observed]** §3's clause-range enumeration annotates lettered sub-clauses for RFC3 (+5), RFC4 (+2), RFC7 (+7), RFC9 (+8) and RFC10 (+3) but carries none for RFC 0002. §3 disclaims itself ("read it from the verifier, never from here") and the verifier's 341 figure is a count of *numbered* identities, so the count is not wrong — but the enumeration alongside it is now incomplete. Neither is a Wave A byte; both are the offer's own narrative.

---

## 4. What passes — stated in full

**Mechanical soundness (item 1) — clean, every result read as output.**

- `sha256sum` over `wave-manifests/WAVE-A-MANIFEST.txt` → `c649143bdac1a883874e4d9d57d76a031a6e9b2f9357d12ea1f5b9484a48b8dd`; recomputed independently in Python `hashlib`; identical. §1 row A's quoted argument extracted by `re` matches character-for-character.
- `sha256sum -c` over the manifest's 19 non-comment rows, run from the candidates root exactly as §2 step 2 documents: **19 of 19 `OK`, 0 failures.** Every one of the 19 lines is listed above in my working record.
- `python3 scripts/build_active_manifest.py --check` → `all 7 manifests match regeneration — 7 manifest(s) over 39 module(s) in 6 wave(s)`. The manifest is the generator's current output.
- Independent cross-check: all 19 Wave A rows are a subset of the 39-row `ACTIVE-CONTRACT-MANIFEST.txt` with byte-identical per-module digests (Python dict comparison, denominator 19/19).
- `python3 scripts/check_governance.py` (repo root) → **30 OK, 18 WARN, 0 FAIL (48 checks)**. Every WARN is a declared report-only or allowlist family. The four that bear on this act are green: **CG-7a** (78 entries, 0 findings — waves partition the set), **CG-7b** (6 wave arguments match their manifests, 0 findings), **CG-7d** (9 act-digest quotations current, 0 findings), **CG-2a** (339 files, 2 retired phrases declared, **0 presented as current**).
- `python3 scripts/verify_final_prespec.py` → **PASS — all checks clean**; 341 numbered clause identities over 39 modules; clause continuity, package disjointness and completeness, citation resolution, closed matrix vocabulary, phase-rule presence, fixture completeness and module ceilings all clean; the two oversize justifications (RFC-0001, RFC-0009/semantic-geography) print with their stated reasons.

**Package integrity (item 2).** All 19 modules read in full. Clause numbering is continuous per each module's front-matter declaration and mechanically confirmed by the verifier — with the single declaration defect at RD31-03, which the verifier does not cover because sub-clause *denials* in a package index are outside every check's population. **[Observed]** Sweep of the 19 for the six act phrases (`grep -F`-equivalent literal match, denominator 19 modules): **zero hits** — no retired ceremony phrase and no current one appears anywhere inside the package, corroborating the delta's handoff-3 claim. **[Observed]** Sweep for self-presentation as accepted (Python `re`, denominator 19): 2 hits, both conditional forward statements ("migrating to a schema no accepted contract defines", "when this RFC is accepted"); no module presents itself as accepted. Every module carries the identical "Absent such a record, this contract binds nothing" banner, and CG-4a covers the directory-level candidate marker for all 39.

**Wave containment (item 5).** **[Observed]** Front-matter `depends_on` extracted from all **19 of 19** modules: the union of every declared edge is `{RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005}`. **No edge names RFC 0006–0011.** No escape. The one outbound `constrains:` edge is discussed at RD31-05.

**[Observed]** Cross-wave token sweep over the 19 (Python `re`, `RFC(7|8|9|10|11)-\d+` plus package names `RFC[- ]00(07|08|09|10|11)`): **63 clause-token hits and 50 package-name hits**, every one classified by reading its site. They fall into five classes, all non-reliances under rule 5: (a) the six phase clauses' `(Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12.)` sibling lists; (b) "**Provides to RFC 000n:**" outbound provision statements in §5 integration sections; (c) citations the clause itself marks informative in-line — RFC6-19 class 8's "RFC8-12 — a forward reference, informative until RFC 0008 is accepted: until then the field is not required, its absence renders as absence, and nothing may be substituted for it"; (d) RFC 0003's RFC10-9 "the worked example", disclosed at §7 item 9; (e) RFC2-19(a)'s RFC8-12 citation, which states its own rule in full before naming the precedent, exactly as delta §9 claims. **Zero hits are a rule a Wave A reader could not evaluate without a deferred wave's text.** Each module additionally carries an explicit "Forward references are informative" paragraph naming which citations are load-bearing; RFC-0003's names the one normative-enumeration exception and requires the cell to state its condition in its own text.

**Disclosure sweep (item 4).** **[Observed]** Sweep of the 19 for `[Drafted` / `drafted` / `awaiting` / `P-\d{1,2}` / `owner-decision(` / `until the owner rules` / `ratifies or reverts` (Python `re`, denominator 19 modules, 31 line-hits triaged individually). The drafted-answer-in-clause-text population is **five**, and **all five are disclosed at §7**: RFC2-19(a) (item 12), RFC4-19's `unknown-terminal` (item 14(b)), RFC3-15's `records/` widening (item 14(a)), RFC3-17's `declarations/` drafted default (item 1), RFC1-7's mission profile (item 16). Every other hit is contract vocabulary (`drafted` as a lifecycle state), settled-decision narrative (B1, B2, B19, A5), or a §8 open question stating a "Proposed:" answer *outside* clause text (RFC4-26 q3, RFC5-6 q5, RFC5-22 q4), collectively disclosed at §5 with its triage file. **I found no undisclosed drafted arm.** RD31-05 is a different class — an unruled *relation declaration* in front matter, not a drafted clause arm — which is why the marker sweep did not surface it and why I ran the `constrains` sweep separately.

**§7 item 13 independently confirmed.** **[Observed]** Sweep of the 19 for the shape-facet vocabulary (`facet|mission-ready|rollup|roll-up|composite (score|number|maturity)`, denominator 19): 5 hits, none a facet name — two are RFC-0006's equivalence-tuple sense of "facet", two are RFC-0002's composite-maturity *prohibition*, one is RFC3-32's roll-up disclosure obligation. §7 item 13's corrected form ("the seven-facet vocabulary itself is in no Wave A byte") is accurate, and the anti-rollup ground it says the act *does* ratify is present and coherent at RFC6-18/RFC6-19.

**The repairs, checked adversarially (item 3) — three of five verified sound.**

- **The RFC1-1/RFC3-4 zero-roots split states one rule at both sites.** RFC1-1: zero roots "surfaces at the **workspace/manifest level** — unevaluable as a Project, rendered Unknown (`missing-declaration`) … with **no kernel contradiction minted**", with the reason given (evaluation identity is (snapshot, as-of) per RFC2-3, and the workspace manifest is barred from being a snapshot input). RFC3-4: "A Project resolving to **zero** roots mints no contradiction: RFC1-1's zero-roots rule (**cited, not restated**) surfaces that case at the workspace/manifest level, unevaluable as a Project and rendered Unknown (`missing-declaration`), with no kernel contradiction to route." Same rule, same reason, cited rather than paraphrased — the correct shape. The two-roots limb is unchanged at both sites. Clean.
- **RFC2-19(a) is well-formed, correctly declared, and — checked against the clauses that could have contradicted it — coherent.** Its identifier is declared in the module's front matter; its bracketed `[P-31 — drafted arm, awaiting an owner ruling.]` note is intact and still governs the arm, naming both routes, why the thirteenth reason is an owner act (A5), and that the paragraph is deleted if the owner directs otherwise. Against RFC2-24 as it now reads, it does not contradict: RFC2-24's own closure paragraph provides exactly the route the arm takes — "A condition genuinely not among the twelve is disclosed as a **fact of the render** — named, expandable, routed to its resolving action — never dressed as a reason." Against RFC-0006 it composes rather than collides: RFC6-14 requires "the Unknown reason **where applicable**", and RFC6-17 and RFC6-22 both make **chain state** a *separate* per-value disclosure and parity dimension from Unknown reason. The arm therefore closes a real RFC6-22 parity hole (whether the reconciliation-pending Unknown carries a reason field) rather than opening one. It also honors rule 8's spirit: it quotes RFC2-24's terms as RFC2-24 now reads them.
- **RFC4-19's `unknown-terminal` and the four citation/wording repairs are present and coherent.** The `terminal outcome + blocker set` row carries the drafted value with its `[Drafted 2026-08-10 (RD26-05)]` marker and its ratify-or-revert sentence; RFC4-19's join-basis citation now reads `(RFC4-22)`; route 4 is attributed at both sites to "owner decision **A2** … route 4 was added by the Tier C **RFC 0002 §8 q3** ruling in the same record"; RFC4-13's authority line now says the observer "reads reports and never executes anything; execution happens only through RFC5-18's profiled launch gate"; RFC4-23(2) states its liveness-bound rule in its own words with RFC8-16 explicitly demoted to "a parallel-obligation pointer, not this rule's source". RFC-0002's README load-bearing exception is correctly extended to the RFC4-13 route-4 citations.
- **The expiry-eligibility half of the split is consistent across all three sites.** RFC2-13 ("Expiry is eligibility, never an outcome … it does **not** end the suspension"), RFC3-2 ("the *eligibility* mints **no record**"), and RFC3-16's `records/` lifecycle row ("expiry *eligibility* derives; the resolution is a recorded act") agree exactly. It is the **resolution** half that fails — RD31-01 and RD31-04.

**The register and the record are accurate about the argument's history.** §1 row A's account of two script-driven regenerations (retiring `6b98e0c6…` then `8af6805f…`) matches delta §§13 and 14, and CG-15/CG-15b confirm no stale digest is presented as current.

---

## 5. Overall assessment

**No — the Wave A act may not be offered to the owner on argument `c649143b…`.**

The argument is mechanically impeccable. Every digest recomputes, the manifest is the generator's current output, §1 row A is exact, the 19 modules partition cleanly inside RFC 0001–0006 with no reliance escape across 113 classified cross-wave references, no retired phrase survives anywhere in the package, no module claims acceptance, and every drafted arm I could find is disclosed at §7. The RD-26 and RD-30 repairs are, in the main, careful work: the zero-roots split is the model of how to cite rather than restate, and RFC2-19(a) is a genuinely well-reasoned arm that closes a parity hole rather than papering over one. If the package's quality were the only question, this would be a short review.

But two things stop the offer. The RD26-04 repair — the one that gives the expiry-resolution act a home — widened RFC3-15's `records/` cell while citing RFC3-2 as the owner of the trigger set, and RFC3-2's closure sentence still says "only on an actor's submission" and enumerates three submissions that do not include the sweep. A clause the act binds contradicts the clause it names as its own authority, on the precise point the repair exists to settle; and the widened member lands in the one governance category the corpus declares gateless, splitting two authorities RFC2-13 calls co-equal across a gated home and an ungated one. That is a repair batched short, and rule 10 says the fix belongs in the next pass, not on top of these bytes. Separately and independently, §7 item 11 states in the record's own voice that until P-33 is ruled this record offers no Wave A act, and P-33 sits unruled in the open table with its arms undrafted. An offer made now would contradict the record making it.

The remaining findings are smaller but should ride the same pass: the RFC 0002 package index tells a reader, under a heading called "Lookup rule (deterministic)", that the package has no lettered sub-clauses — three days after a repair minted one specifically so it could be anchored; and §7 is silent that Wave A is the act which freezes the `constrains:` relation while P-21(a) is open and the wave that was supposed to ratify it is deferred.

None of this is a verdict against the package. It is a verdict against binding *these* bytes today. Repair RD31-01, RD31-03, RD31-04 and RD31-05 in one batch, regenerate the manifest by script, get P-33 ruled, and re-offer to a fresh exact-package review bound to the new argument. I would not stake the offer on these bytes.

VERDICT: REVISE
