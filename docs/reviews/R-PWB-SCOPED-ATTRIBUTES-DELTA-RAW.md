# Raw review — PWB scoped epistemic attributes amendment (lane B candidate)

Reviewed commit: `9098b0b11ab548b4ea00081b26ec4ad2b84e693e`

Manifest SHA-256 (computed with `sha256sum` over `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`): `6d9c81b7b399d069d124b6e620776283681bd926875db9d5d0ad4037de33a5a6` — this equals the argument quoted in `OWNER-DECISION-PACKET.md:18` and `:90`.

Verdict: REVISE

Reviewer: fresh-context session, no authoring context, `syzygy-dov.17` package not read before this review. Class: fresh-reader semantic review of a normative delta (CC-REV-4, CC-REV-6).

---

## What I ran

- `python3 scripts/build_pwb_scoped_attributes_amendment.py --check` → exit 0, "manifest matches 11 proposed behavior subjects (3 patched, 8 unchanged)".
- `--selftest` → exit 0, "closed population, byte drift, path order, subject drift and patch corruption fail closed". I read the fixtures at lines 171–222: each of the five predicates mutates a real input and asserts failure, per verification rule 6.
- `python3 scripts/check_governance.py` at the reviewed commit → `32 OK, 20 WARN, 0 FAIL (52 checks)`. The third successor-chain link is registered but skipped (`check_governance.py:2848` `if not (link_recorded or link_dedicated): continue`), so merging changes no authority. Criterion 6's "cannot bind anything by merge" **verified**.
- Rule-6 mutation on the registration (in a scratch `git archive` extraction, not the repo): replacing the packet's argument with sixty-four zeros produces `FAIL CG-7d` and `FAIL CG-7e`, both naming the packet by path and line 90. The registration works.
- Rule-6 mutation on drift: `--apply` without `--at-adoption` refuses (exit 2); with it, `check_governance.py` goes to `FAIL CG-7h` naming all three drifted subjects. CG-7h keeps binding the 2026-09-05 package.
- Post-apply manifest parity: I re-hashed all eleven subjects after `--apply --at-adoption`; **11/11 rows match**. Criterion 6's "hashes exactly the post-apply bytes" **verified**.
- `GOVERNING-DEPENDENCIES.md` self-consistency: after apply, `build_polaris_project_wide_spec_dependencies.py --check` passes and regeneration is byte-identical (`b0622db43285d20e2c477ca7a9e9be93aee5c42408ef89d78bb5939e20245dad` before and after). The patched digest line equals `sha256(proposed spec.md)` = `a47bf89f610eb4b72761a2f0185b0e5b9098356dc87be50ac1fcb95422b6dd93`, the manifest's spec row. Scripted, not transcribed (rule 3).
- Independent re-derivation of the ledger's 80/1,216: at the stated baseline `a9f671e`, `git ls-tree -r --name-only` = **1,216** and the union of `git grep -l -F` over the three identifiers = **80**. A Python `re` sweep over `git ls-files -z` agrees file-for-file with the grep union and with the ledger's 80 rows (zero symmetric difference). Two methods, denominator enumerated (rules 2 and 9). Criterion checkability **verified**; see F13 for the caveat.

---

## Findings

### Blocking

**F1 — PWB-REQ-014's scoped non-authority attributes contradict accepted RFC7-33, and no contract amendment travels with them.**
*Severity: blocking. Anchor:* `proposed/spec.md.patch:77-80`; conflicting clause `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md:205-231`.

The patch adds:

```
In the human
view the two attributes MAY be carried once by an enclosing scope under the
PWB-REQ-007 inheritance rule
```

RFC7-33 (accepted; `status_source: owner-act-record`) says, quoted exactly:

> **RFC7-33 — Every distinction, machine-readable.** Every distinction this package draws — **`non-citable` / `presentation-artifact`** (below), … — is carried as a **machine-readable attribute on the rendered unit**

and, in the sub-clause that exists *specifically* to close this gap:

> **Non-citability travels, on every rendering.** Every narrative-model unit (RFC7-5) carries the **`non-citable` / `presentation-artifact`** attribute, required on **every** exported, embedded, or plain-text rendering — not only on the interactive surface. … The catch-all opener above is not sufficient cover: [Inferred] enumerations of this shape are implemented as literal field lists, so the one field whose omission is unrecoverable at the consumer must be named.

The clause's stated harm model is the consumer that receives a unit detached from its context — "a copy-paste into an agent prompt" (line 216). A claim block hoisted out of a scope is exactly that case: the unit no longer carries the attribute, and expansion is available only to a reader who has the whole page. "Carried on the rendered unit" and "carried once by an enclosing scope" cannot both be true of the same rendering.

`SEMANTIC-DELTA.md:269-270` asserts the opposite as warrant — "RFC7-16 and RFC7-33 (evaluation identity and machine-readable distinctions on every rendering, preserved by expansion)". RFC7-33 does not say "recoverable by expansion"; it says carried on the unit, on every rendering. PWB-REQ-014's warrant list still names `RFC7-33` (`spec.md:809`) and the delta says "No warrant list changes" (`SEMANTIC-DELTA.md:18`).

CC-REV-2 (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:54-57`), quoted:

> A change that invalidates any authoritative artifact updates **every** invalidated authoritative artifact in the same logical change: behavioral specs (`openspec/`), declared topology, **accepted contracts**, and the policies in this cluster. "We'll sync the spec later" is a violation, not a plan

This is also an act escalation trigger (contract change) in its own right.

*Resolution:* either (a) carry an RFC-0007 semantic delta for RFC7-33 in the same package and route it to its own owner act, or (b) drop the PWB-REQ-014 half of the amendment and scope only PWB-REQ-007 tuple fields that RFC7-33's enumeration does not name — noting that RFC7-33's enumeration also names "label + tier + reason + freshness", so (b) needs the same analysis and probably reaches the same place. The 100 KB attribute saving in `OWNER-DECISION-PACKET.md:63-64` is the part at stake.

**F2 — PWB-REQ-007's new scope-hidden falsifier is vacuous in the flat case and over-fires in the nested case.**
*Severity: blocking. Criterion 3 ("a finite falsifier for a scope hiding a differing member"), criterion 1. Anchor:* `proposed/spec.md.patch:48-51`.

```
- **Falsifier**: a positive claim lacks current support, a tuple field is
  absent/out of vocabulary after expansion, a scope carries a value that
  differs from a claim under it that does not carry the field itself, …
```

Parse the middle predicate. Let scope `S` carry field `F=B`, and let claim `C` be under `S` and not carry `F` itself. What is "a claim … that does not carry the field itself" *compared against*? By the inheritance rule stated three sentences earlier — "a claim's value for a field it does not carry is the value of the nearest enclosing scope that carries the field" — `C`'s value **is** `B`. The comparison is analytically never unequal. In the flat case the falsifier can never fire.

The only reading under which it has a referent is the nested one: `S_outer` carries `F=B`, `S_inner` carries `F=A`, `C` under `S_inner` carries nothing. Then `C`'s value is `A` (nearest), `S_outer` "carries a value that differs from a claim under it that does not carry the field itself", and the falsifier **fires on a legal render** — nested override is exactly what "nearest enclosing scope" exists to permit. So the predicate is either empty or wrong, with nothing in between.

The scenario at `proposed/spec.md.patch:105-111` does not rescue it: "a scope whose value would hide that difference fails the oracle" names the intent, but a scenario is not the falsifier, and the amended falsifier is the text an oracle author implements.

What actually catches scope-hiding is PWB-REQ-020's independent predicate, which *is* well defined because it compares against the machine channel: "a scope value SHALL never stand in for a claim whose own value differs" (`proposed/spec.md.patch:132-133`). PWB-REQ-007 is therefore left without the falsifier criterion 3 requires of it, and its "Oracle independence" bullet's "reads captured authority/evidence" is the only thing that could supply an independent value — which the falsifier does not reference.

*Resolution:* restate the predicate against a source outside the human rendering, e.g. "a claim's expanded value for a field differs from the value its machine tuple carries", and restrict the scope quantifier to *the nearest enclosing scope that carries the field* so nested override does not trip it.

**F3 — The hoisting precondition and the override sentence are mutually inconsistent, and different parts of the package depend on different readings.**
*Severity: blocking. Criteria 1, 2, 5. Anchor:* `proposed/spec.md.patch:9-12`.

```
In the human view, a tuple field whose value is identical for every claim
under one enclosing scope MAY be carried once on that scope instead of on
each claim; the claim still carries the field by the inheritance rule, and a
claim whose value differs from its scope's SHALL carry the field itself.
```

If the value is identical for *every* claim under the scope, no claim can differ, and the second half of the sentence has no subject. If a claim can differ, the first half's precondition is not the governing rule. Exactly one of the two is normative and the text does not say which.

The package then leans both ways:

- `SEMANTIC-DELTA.md:249-250` relies on the **strict** reading: "A scope may carry a value only when every claim under it has that value; an Unknown claim under a scope carrying a positive label carries its own label". That sentence is the package's whole Unknown assurance, and it is *not* what the spec bytes say.
- The falsifier (`proposed/spec.md.patch:49-51`) and the scenario's third bullet only make sense under the **permissive** reading, where a scope value coexists with an overriding member.

Under the permissive reading the scope element asserts a value over a population one of whose members is Unknown. Per-claim truth survives (the Unknown claim carries its own label), so I do not find a hard Unknown-folding hole — but a scope marker is then a population-level assertion that is false for a member, and the spec grants the scope marker no epistemic status, no label, no tier and no falsifier of its own. That is a VIS-2 surface the amendment creates and does not govern.

*Resolution:* pick one. If strict, delete "and a claim whose value differs from its scope's SHALL carry the field itself" from the permission and keep it only as the falsifier's condition-of-violation; if permissive, delete "identical for every claim" and say what an outlier-bearing scope marker means and how a reader is told it has outliers.

**F4 — "SHALL fail to render" on two evaluation identities forbids a rendering the current clauses admit, with no observable, oracle, falsifier or scenario, and the delta does not disclose it.**
*Severity: blocking. Criteria 5, 3 (CC-TEST-5/CC-TEST-6), VIS-2. Anchor:* `proposed/spec.md.patch:16-18`.

```
A page whose claims would carry two distinct evaluation
identities SHALL fail to render rather than carry either on a scope.
```

Three defects in one sentence.

1. **It is unconditional.** It is not written as "a page that hoists the evaluation identity"; it is a property of the page. Today PWB-REQ-007 forbids no such page — every claim carries its own identity and the page renders. The amendment removes a legal rendering. `SEMANTIC-DELTA.md:20-21` describes the change class as "The amended clauses admit a human rendering the current clauses forbid, and add one falsifier class". It also forbids a rendering the current clauses admit, which is not stated anywhere in the delta, the ledger or the packet.
2. **The conservative fallback is not offered.** "rather than carry either on a scope" presents exactly two options. The obvious third — *do not hoist; carry the identity per claim, as today* — is strictly safer and the clause forecloses it.
3. **It has no verification apparatus.** No Observable, Oracle, Falsifier bullet or scenario covers it, and there is no Unknown, disclosure or readiness path — the response is to serve nothing. CC-TEST-6 (`testing-and-verification.md:121-130`): "Every status-rendering or evidence-consuming feature ships tests for its no-data branches … Expected behavior in each is the doctrine-prescribed one — Unknown, excluded, aggregated-with-count — never a silent default (VIS-2 …). Happy-path-only coverage of an epistemic surface is a finding … at elevated severity: for this product the failure mode of the empty branch is *lying*." A silent non-render is the empty branch with no disclosure at all — the same shape as the response-ceiling 503 the project already treats as a known sore point.

Note that `polaris-epistemic-tuples.test.ts:227-228` already asserts `evaluationIds(...).size === 1` over the fixture model. A test assertion is not a render-time SHALL, and the existing page-wide check at line 233 (`expect(firstHtml).toContain('data-evaluation-id="…"')`) is a substring check that a hoisted identity satisfies unchanged — so the existing oracle would not detect a wrongly hoisted identity either.

*Resolution:* condition the sentence on hoisting, name the fallback ("SHALL carry the evaluation identity on each claim rather than on a scope"), and either give the failure mode an Observable/Falsifier pair and a disclosure, or delete it.

**F5 — `design.md` decision 9 attributes scope-hiding to PWB-REQ-020's `collapsed` falsifier; the patch creates a separate one.**
*Severity: blocking. Criteria 4, 5. Anchor:* `proposed/design.md.patch:23-25`; conflicting `proposed/spec.md.patch:140-148`.

Decision 9 says:

```
statement of the rule, so the comparator still imports no rendering code and
PWB-REQ-020's collapsed falsifier still fires when a scope value would hide a
differing member.
```

The spec patch does the opposite: it adds `scope-hidden` as a distinct mutant class ("independently inject a missing, duplicated, changed, collapsed, wrong-evaluation and scope-hidden marker") and a distinct falsifier clause ("missing, duplicated, changed, collapsed, hidden behind a scope value or associated with a different evaluation"). `collapsed` and scope-hiding are deliberately separated in the requirement and merged in the design note.

This also falsifies two of the delta's own assertions: `SEMANTIC-DELTA.md:244-247` — "PWB-REQ-020's `collapsed` and `duplicated` falsifiers keep their meaning" — and `:232-233` — decision 9 "restates the rule and the rejected alternatives and binds nothing the spec does not." It binds a different falsifier assignment than the spec does, in an artifact the act would digest-bind and that could then never be corrected. Criterion 5's "does NOT change list accurate against the patch" fails here, and criterion 4's "`collapsed`/`duplicated` falsifiers keep their meaning" fails in `design.md`.

*Resolution:* change decision 9 to name the new `scope-hidden` falsifier and mutant class.

### Non-blocking

**F6 — The owner packet routes to a register row that does not exist.**
*Anchor:* `OWNER-DECISION-PACKET.md:10` — "Register row: P-68 in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`."

`git grep -n -F "P-68" 9098b0b` returns exactly two hits, both inside this commit's own new/edited files (the packet itself and `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md:238`). `PENDING-OWNER-DECISIONS.md` ends at P-67 (its last two update banners, lines 90 and 100, add and rule P-67). The owner who follows the packet's routing line finds nothing. Against criterion 8 and VIS-2 (a stated [Observed]-shaped fact with no referent). *Resolution:* add the P-68 row in the adoption-preparation change, or drop the line. Note this fix alone changes the packet bytes but not the manifest digest, so the act phrase is unaffected.

**F7 — No existence-gated activation registers the act record and the aggregate copy.**
*Anchor:* `scripts/check_governance.py:2216-2217` (packet registered) versus `:2279-2294` (`_activate_pwb_truth_amendment_act_copy_registry`).

The precedent registers three things: the packet statically, and — once `PWB-TRUTH-READINESS-AMENDMENT-ACT.md` exists — both the dedicated record and `ACCEPTANCE-ACT-RECORD.md`, from an existence-gated function. This commit registers only the packet. `PWB_SCOPED_AMENDMENT_ACT` is defined (`:1535-1536`) and used by the chain, but never added to `ACT_DIGEST_COPY_FILES`. After the act, a stale argument copy in the dedicated record or the aggregate section would not be a CG-7e finding. `SEMANTIC-DELTA.md:305-310` (migration step 3) names the recorder's duties and does not name this one.

*Resolution:* add `_activate_pwb_scoped_amendment_act_copy_registry()` in the same shape now (it is a no-op until the act file exists), and name it in migration step 3.

**F8 — The builder is not in CI.**
*Anchor:* `.github/workflows/governance-docs.yml:109-110` runs `build_pwb_truth_policy_amendment.py --check`; no line runs `build_pwb_scoped_attributes_amendment.py --check` or `--selftest`.

The candidate's whole integrity claim is that `--check` still verifies the patches apply and that the manifest hashes their result. Nothing runs it. *Resolution:* add both steps beside line 109.

**F9 — PWB-REQ-014's "Oracle independence" bullet is left unamended.**
*Anchor:* `spec.md:793-794`, untouched by the patch.

007's and 020's independence bullets both gain language about the checker's own statement of the rule and about importing no rendering code (`proposed/spec.md.patch:43-45`, `:135-138`). 014's still reads only "expected source spans and reference targets come from captured artifacts, not the rendered claim blocks" — it never said "imports no rendering code" and still does not. Criterion 3 asks this of all three. *Resolution:* amend 014's independence bullet to match, or say in the delta why 014 does not need it.

**F10 — The inheritance rule is written for claims and applied to narrative units.**
*Anchor:* `proposed/spec.md.patch:11-15` versus `:77-80`.

PWB-REQ-007's rule quantifies over "a claim" throughout ("a claim's value for a field it does not carry…", "every claim under it SHALL carry its Claim identity itself"). PWB-REQ-014 invokes it for "every owner-visible narrative unit under that scope", a superset that includes explicitly non-normative framing. Applying the rule requires silently reading "claim" as "unit". Criterion 1 asks the rule be stated once *and complete*; it is stated once but is not complete over 014's population. *Resolution:* generalize 007's rule text to "a claim or owner-visible narrative unit", or state the extension explicitly in 014.

**F11 — The scope element's own contribution to the parity multiset is unspecified.**
*Anchor:* `proposed/spec.md.patch:127-130` (Case: "enumerate every project-shape parity marker on Polaris, expanding scopes").

A scope is "one element carrying a machine-readable scope marker" that also carries field values. Nothing says whether its field values are themselves parity markers. A comparator that counts them produces surplus human members and fires `duplicated`; one that does not must know to skip them, and the spec gives it no rule to do so. Criterion 4 ("one tuple per rendered claim survives expansion, multiplicity is preserved") is stated in the delta but not secured by the bytes. *Resolution:* one sentence — after expansion the scope element contributes no marker of its own.

**F12 — Two implementation-column inconsistencies in the ledger.**
*Anchor:* `IMPACT-LEDGER.md:41-42, 61, 65`.

Line 41 states the legend: "Files the implementation must change after adoption are marked **must** in the last column; every other row is untouched by this package."

- `polaris-copy.ts` (line 61) is marked `—`. But `OWNER-DECISION-PACKET.md:72-73` says "The rule is stated once in the spec and the page's claim-states lede would restate it", and that lede is `polaris-copy.ts:29` (`{ id: 'label.claim-states', … text: 'What the claim states mean' }`). The packet's risk mitigation lands in a file the ledger says is not an implementation site.
- `project-shape-model.ts` (line 65) carries `model`, a third value the legend does not define; the prose at `:156-158` explains it, but the column legend at line 41 admits only `must` and "untouched".

Also, "every other row is untouched by this package" is trivially true of every row — the package touches no file at all — so the sentence carries no information where it is meant to bound the implementation.

**F13 — The 80/1,216 figure does not hold at the commit that publishes it.**
*Anchor:* `IMPACT-LEDGER.md:19-20`, baseline declared at `:5`.

At `a9f671e` I reproduce 80/1,216 exactly, by both methods. At the reviewed commit `9098b0b` the same sweeps return **86 files over 1,225** — the six extra are this package's own `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`, `OWNER-DECISION-PACKET.md`, `proposed/spec.md.patch` and `proposed/design.md.patch`. The ledger declares its baseline, so the figure is checkable and I checked it — but a reader sweeping the commit in front of them gets a different number with no note explaining why. This is the "measuring last is not enough" class: a count over a population the same pass is still editing. *Resolution:* one line — "at the reviewed commit the figure is 86/1,225; the six additions are this package's own files."

**F14 — Decision 9 embeds a perishable measured claim in an artifact the act would bind forever.**
*Anchor:* `proposed/design.md.patch:13-16` — "after the 2026-09-13 lane A trim the page still sits above the ruled 1.4 MB working target under the 2 MiB response ceiling".

`design.md` is manifest row 15 of the eleven; once the act binds its digest the sentence cannot be corrected. It will go false the moment the implementation bead lands its measurement — which is the amendment's own success condition. *Resolution:* write it as of a date and cite `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json` rather than restating the state.

**F15 — The manifest's own header goes false at the act and is uncorrectable.**
*Anchor:* `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt:2, 5-6` — "Candidate; this file and its rows bind nothing by themselves." and "They match the tree only after --apply, the adoption step."

This file *is* the act subject: its digest is the owner's argument. After the act, line 2 is false about the very bytes the owner signed, and any edit changes the digest, so it can never be repaired. I note the precedent `pwb-truth-policy-amendment/PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt:2` carries the identical line and was bound by the performed 2026-09-05 act — so this is an inherited house shape, not a novel error, which is why I rate it non-blocking. It is nonetheless free to fix *now* and impossible to fix later. *Resolution:* word the header so it stays true across the transition ("These rows bind only by the act named in `ACCEPTANCE-ACT-RECORD.md`; until that act they bind nothing"). Fixing it changes the manifest digest, so the packet's two digest copies and the ledger must be regenerated in the same change.

### Editorial

**F16 —** `proposed/spec.md.patch:14-15`, "a claim under no such scope leaves the field absent", reads as a grant of permission, against PWB-REQ-007's own opening SHALL ("carry the closed label, tier, exactly one primary reason … freshness, challenge state and evaluation identity") and against `SEMANTIC-DELTA.md:241-243` ("No field is dropped for any claim in any channel"). The amended falsifier does forbid it ("absent/out of vocabulary **after expansion**"), so this is a clarity defect, not a hole. *Resolution:* "…leaves the field absent, which the falsifier below forbids."

**F17 —** The change class at `SEMANTIC-DELTA.md:20-21` also omits that the patch *broadens* PWB-REQ-014's falsifier: `spec.md:796` "missing non-citable attribute" becomes "a non-citable or presentation-artifact attribute missing after scope expansion". That is a strengthening and a good one, but an unstated normative change in a delta whose purpose is to state them all.

**F18 —** `IMPACT-LEDGER.md:28` puts two populations in one cell: "signed package | 6 | … three rows change, eight are byte-identical". The 6 is citing files; the 3+8 is the 11-row manifest. A reader checking 3+8=11 against 6 has to work out that these are different sets.

**F19 —** `OWNER-DECISION-PACKET.md:83-85` presents the alternatives as "cut items from the page, which the item-per-page contract (P-67 question 3) rules out, or … leave the page 78–84 KB over the target you set." A third option is the owner's to take and is not named: revise the 1,400,000-byte working target, which is itself an owner number from P-67 Q3 and not a ceiling — the page currently sits ~612 KB *under* the hard 2 MiB ceiling, which the packet states at line 31. Under the discipline "preserve the owner's trade-offs; never smooth them", the cheapest option should be on the page. The "Recommended: **accept**" framing itself matches house style (the precedent packet recommends at three decision points), so I raise no finding on that.

**F20 —** `scripts/build_pwb_scoped_attributes_amendment.py:271-275`: invoking the builder with no flags silently regenerates and overwrites the manifest. Once the packet is in front of the owner, a bare run rewrites the act's subject. CG-7d/CG-7e would then fail on the packet copy (I verified this fires), so it is detected, not silent — but a `--write`-style flag, matching `--apply`'s own refusal pattern, would make it fail earlier.

### Criteria with zero findings

**Criterion 7 (comprehension)** — zero findings. I restate the package below without author context; nothing in the substance was unrecoverable from the delta and the patch. The two things I could not restate from the bytes alone (which reading of the hoisting precondition governs; which falsifier catches scope-hiding) are recorded as F3 and F5 against criteria 1/2/5 rather than here.

Every other criterion has at least one finding above: criterion 1 → F2, F3, F10, F16; criterion 2 → F3, F16; criterion 3 → F2, F9; criterion 4 → F5, F11; criterion 5 → F1, F4, F5, F17; criterion 6 → F7, F8, F15, F20 (its core mechanics verified clean — see "What I ran"); criterion 8 → F6, F19.

---

## What I could not verify

- **The 450 KB estimate and its transfer to the post-lane-A page.** `OWNER-DECISION-PACKET.md:63-67` labels it `[Inferred]` and states plainly that the lane A page has not been measured with scopes, which is honest under VIS-2. I did not build the renderer, so I cannot say whether the 50/300/100 KB split survives lane A's own trim, nor whether the three components overlap bytes lane A already removed. The packet's caveat is adequate; the number is not checkable from anything in the package.
- **Whether any real Polaris render today carries two distinct evaluation identities.** `polaris-epistemic-tuples.test.ts:227-228` asserts a single identity over the fixture model, but I did not serve a daemon or measure a page (the observer refuses uncommitted inputs and the daemon serves only the registered locator). So I cannot say whether F4's new SHALL would fail any page that renders today — only that it forbids a class the current clauses admit.
- **The implementability of the expansions in each of the nine oracle/test files.** I read the four comparator sites the brief named and confirm they are correctly identified: `leafMarkers` (`polaris-parity-sweep.test.ts:110`) throws on any non-leaf marker element, so a scope carrying a marker attribute would hard-fail it, and the claim-tuple join (`:415-423`) reads six fields off the claim's own span; `TUPLE_FIELDS` (`polaris-epistemic-tuples.test.ts:83`) enumerates all eight and line 99 asserts each is `toBeDefined()` on the span. All would need the ledger's stated expansion. I did not run the suites or attempt the expansion, so I cannot confirm the expansions are *achievable* without importing rendering code — only that the sites named are the right ones.
- **Whether `POLARIS-M1-PAGE-SIZE-FUNNEL.md`'s draft delta is superseded cleanly.** The ledger asserts it "is superseded by this package and says so by date" (`IMPACT-LEDGER.md:34`); I read the funnel's P-68 reference at line 238 but did not audit the funnel's lane B section against the final text clause by clause.
- **Any Butlers-side effect.** Out of scope for this package and not examined.

---

## Comprehension restatement

*In my own words, from the bytes, with no authoring context.*

**The inheritance rule.** Today every claim on the Polaris human page wears its whole epistemic tuple — label, tier, one primary reason, any secondary reasons, freshness, challenge state, evaluation identity — plus, for narrative units, two attributes saying "this is presentation, don't cite it". Each of those is repeated on every claim, even when a whole table of claims says the same thing. The amendment would let a shared value be written once on an enclosing element (a "scope", marked machine-readably) instead of on each member. A claim that doesn't carry a field takes the value of the *nearest* enclosing scope that does — nearest, so nested scopes work — and if no enclosing scope carries it, the field is simply absent, which the falsifier then forbids. Two things never inherit: the claim's own identity, and anything in the machine answer, which keeps carrying every field on every claim exactly as today. The parity check no longer compares raw HTML against the machine model; it first *expands* the human page under the rule, using its own independent statement of the rule rather than any renderer code, and then compares as before — one tuple per rendered claim, multiplicity preserved.

**What it buys.** Bytes, and only bytes. The 2026-09-13 lane A trim got the page from about 2.13 MB to about 1.48 MB, which is inside the hard 2 MiB response ceiling with roughly 612 KB of headroom but still 78–84 KB over the 1.4 MB working target the owner set in P-67. What's left per item is the tuple and its citations, and the estimate is that stating shared values once removes about 450 KB — enough to clear the target comfortably. The estimate is explicitly an inference on a pre-lane-A capture; only the implementation bead's measurement would settle it.

**The risks.** Three, as I read them. *Detachment*: a claim copied or exported out of the page loses whatever its scope was carrying — and that is exactly the harm RFC7-33 was written to prevent, which is F1 and the reason I cannot confirm this. *Ambiguity*: the amended text does not settle whether a scope may only carry a value every member shares, or may carry a majority value with members overriding it; the package's Unknown assurance assumes the first and its falsifier assumes the second (F3), and its PWB-REQ-007 falsifier as literally written can't fire in the flat case and fires wrongly in the nested one (F2). *A new hard failure*: a page carrying two evaluation identities would fail to render outright rather than fall back to carrying them per claim, with no disclosure and no test (F4). Against those, the machine channel is genuinely untouched, so an agent consumer loses nothing, and PWB-REQ-020 gains a real new named mutant class — `scope-hidden` — that a scope hiding a differing member has to survive.

**The one owner choice.** Whether the eleven-artifact package described by manifest `6d9c81b7b399d069d124b6e620776283681bd926875db9d5d0ad4037de33a5a6` becomes the PWB behavioral authority for this bounded one-repository POC, superseding the 2026-09-05 package as the third link of the successor chain. One phrase, one digest; silence, a merge, a review or a general "approved" performs nothing; and an implementation bead exists only after the act.

**Criterion 8, on the authorization question specifically:** I looked for any reading under which the packet authorizes implementation and found none. `OWNER-DECISION-PACKET.md:3-6` disclaims it, `:103-105` says "Only then is an implementation bead opened … Nothing is implemented before the act", and `SEMANTIC-DELTA.md:313-315` puts the implementation bead strictly after the act. `IMPACT-LEDGER.md:131-158` is prescriptive about *what* the bead would touch, but it is titled "for the bead that follows adoption" and reads as impact analysis, not a work order. One decision, one phrase, one set of bytes — that part is clean.

---

## Why REVISE rather than CONFIRM

The package's mechanics are the strongest part of it and I verified them independently: the manifest hashes the post-apply bytes of all eleven subjects, the builder fails closed on five distinct mutations, the generated dependency file regenerates byte-identically from the patched spec, the registration fires CG-7d and CG-7e on a stale argument, and a merge binds nothing because CG-7h skips an unperformed chain link. The delta follows the template and the 80-file impact claim reproduces exactly at its stated baseline by two agreeing methods.

What it cannot carry as it stands is the normative text. F1 puts PWB-REQ-014 in conflict with an accepted contract clause whose sub-clause exists specifically to forbid what the amendment permits, and CC-REV-2 requires that contract to be amended in the same logical change — that is an owner act this package does not contain. F2 leaves PWB-REQ-007 without a working falsifier for the very class the amendment introduces. F3 leaves the central permission ambiguous in a way the delta's own Unknown assurance depends on resolving. F4 adds an untested prohibition the delta does not disclose. F5 puts a contradiction between two artifacts the same act would bind, one of which could then never be corrected.

Each is repairable in prose. None can be repaired by me: a reviewer who authors a semantic fix retires their own review (`REVIEW-BRIEF.md:52-53`). The repaired bytes need a fresh reviewer, and the manifest digest — and therefore the owner's phrase — changes with them, so the packet must not go to the owner at `6d9c81b7b399d069d124b6e620776283681bd926875db9d5d0ad4037de33a5a6`.
