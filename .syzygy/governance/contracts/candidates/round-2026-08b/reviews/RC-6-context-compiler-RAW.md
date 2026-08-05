# RC-6 — Context Compiler (RFC-0011) and the eight context-selection fixtures — RAW reviewer output

**Reviewer:** independent fresh-context session, 2026-08-05. No authoring
history consulted; `_bootstrap/**` not read (I did read
`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`, which is in scope and
tracked).

**Scope reviewed:** `rfcs/RFC-0011-context-compiler.md`; `fixtures/**` (eight
context-selection fixtures + `semantic-equivalence-fixtures.md`);
`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`;
`06-CONTEXT-LOAD-MAP.md`; `TASK-TO-CONTRACT-INDEX.md`;
`05-CONTRACT-INDEX.yaml`; `scripts/context_load.py`.

All paths below are relative to
`/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/` unless
prefixed. Everything labelled [Observed] was executed in this session; the
commands and their real output are shown.

---

## 0. The finding that reframes items 1 and 3

[Observed] `scripts/context_load.py` is **not a context compiler and not a
route**. Its own docstring says so — `scripts/context_load.py:2-5`: *"Measure
a context-packet selection: word and token-estimate totals for a set of
governed artifacts."* Its entire interface is:

```
$ python3 .syzygy/governance/contracts/candidates/scripts/context_load.py --help
usage: context_load.py [-h] [--root ROOT] paths [paths ...]

positional arguments:
  paths

options:
  -h, --help   show this help message and exit
  --root ROOT
```

It takes **paths you have already chosen** (`scripts/context_load.py:60-73`),
`len(text.split())`s them, multiplies by 1.35, and prints a total. It has no
notion of a task, a warrant, a risk class, an `applies_to` value, a clause ID,
or a dependency edge. There is no code anywhere in `scripts/` that maps a task
to a selection.

Consequence for this review: **"reproduce the mechanical route" is not
possible as posed, because there is no mechanical route.** What I can (and
did) reproduce is the *measurement* of each fixture's hand-authored selection.
The selection itself is human judgment, narrated afterwards in each fixture's
"Selection rule trace (RFC11-4)" prose. Every fixture nonetheless records
`Compiler: context_load.py, selection rules rev10-fixtures` — language that
reads as though a compiler produced the set.

This is not hidden by the package — `round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md:230-234`
states plainly: *"these are selection fixtures, not packets."* But the report
does not say the further thing: they are also **not compiled selections**.
They are worked examples of what a compiler, if one existed, ought to produce.
See finding 3.

---

## 1. REPRODUCTION OF THE EIGHT FIXTURES

### Method

For each fixture I copied its own `Required context` command block verbatim
and ran it from the package root. Digests were recomputed with the fixture's
own stated recipe — `cat <mandatory files> | sha256sum`, files concatenated in
listed order, with `doctrine:`/`craft:` resolved to the canonical homes the
fixtures pin (`fixtures/context-selection-8-openspec-authoring.md:165-170`).

### Commands and real output

```
$ cd /home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates

$ python3 scripts/context_load.py rfcs/RFC-0007/README.md \
    rfcs/RFC-0007/narrative-contract.md rfcs/RFC-0002/README.md \
    rfcs/RFC-0002/rendering-vocabularies.md doctrine:vision.md
[source] doctrine:vision.md -> /home/tze/GitHub/syzygy/.syzygy/governance/doctrine/vision.md (canonical home)
   2326  rfcs/RFC-0007/README.md
   5167  rfcs/RFC-0007/narrative-contract.md
   1818  rfcs/RFC-0002/README.md
   2397  rfcs/RFC-0002/rendering-vocabularies.md
   2156  doctrine:vision.md
-------
  13864  TOTAL words
  18716  estimated tokens (words × 1.35)

$ python3 scripts/context_load.py rfcs/RFC-0004/README.md \
    rfcs/RFC-0004/general-contract.md rfcs/RFC-0004/named-adapters.md \
    rfcs/RFC-0008/README.md rfcs/RFC-0008/state-vocabulary-and-cost.md \
    rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md \
    doctrine:security.md
  … 18315  TOTAL words / 24725  estimated tokens

$ python3 scripts/context_load.py rfcs/RFC-0009/README.md \
    rfcs/RFC-0009/visual-grammar-and-lenses.md rfcs/RFC-0002/README.md \
    rfcs/RFC-0002/rendering-vocabularies.md doctrine:architecture.md
  … 14134  TOTAL words / 19080  estimated tokens

$ python3 scripts/context_load.py rfcs/RFC-0005/README.md \
    rfcs/RFC-0005/execution-profiles.md rfcs/RFC-0003/README.md \
    rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:security.md \
    craft:security-and-secrets.md
  … 10893  TOTAL words / 14705  estimated tokens

$ python3 scripts/context_load.py rfcs/RFC-0010-mission-control-autonomy.md \
    rfcs/RFC-0011-context-compiler.md rfcs/RFC-0003/README.md \
    rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:vision.md
   3103  rfcs/RFC-0010-mission-control-autonomy.md
   2264  rfcs/RFC-0011-context-compiler.md
    920  rfcs/RFC-0003/README.md
   4414  rfcs/RFC-0003/governance-homes-and-owner-acts.md
   2156  doctrine:vision.md
-------
  12857  TOTAL words
  17356  estimated tokens (words × 1.35)          <-- fixture states 12,843 / 17,338

$ python3 scripts/context_load.py doctrine:vision.md doctrine:v1.md \
    doctrine:architecture.md doctrine:README.md rfcs/RFC-0003/README.md \
    rfcs/RFC-0003/governance-homes-and-owner-acts.md
  … 11537  TOTAL words / 15574  estimated tokens

$ python3 scripts/context_load.py rfcs/RFC-0001-project-graph-identity-state-planes.md \
    rfcs/RFC-0002/README.md rfcs/RFC-0002/snapshot-and-evaluation-core.md \
    doctrine:architecture.md craft:engineering-bar.md
  … 15767  TOTAL words / 21285  estimated tokens

$ python3 scripts/context_load.py rfcs/RFC-0001-project-graph-identity-state-planes.md \
    rfcs/RFC-0007/README.md rfcs/RFC-0007/narrative-contract.md \
    rfcs/RFC-0007/rendering-and-surface.md doctrine:vision.md \
    craft:testing-and-verification.md
   8353  rfcs/RFC-0001-project-graph-identity-state-planes.md
   2326  rfcs/RFC-0007/README.md
   5167  rfcs/RFC-0007/narrative-contract.md
   3143  rfcs/RFC-0007/rendering-and-surface.md
   2156  doctrine:vision.md
   1113  craft:testing-and-verification.md
-------
  22258  TOTAL words
  30048  estimated tokens (words × 1.35)
```

Digest recomputation (all eight, one command each, `cat … | sha256sum`):

```
F1 recorded 4544d4b27646e905 actual 4544d4b27646e90595ff624137329ba8…  MATCH
F2 recorded a398a06362074451 actual a398a063620744514bc8fc60286c13d1…  MATCH
F3 recorded 2e408eaf40278ca7 actual 2e408eaf40278ca737b057dbbfb769ce…  MATCH
F4 recorded a56fb116fa588b9b actual a56fb116fa588b9bab7126f0d0f42986…  MATCH
F5 recorded c92c6f8a936b12b0 actual ca4e8511348c14c8539e0be53654fa9a…  ***MISMATCH***
F6 recorded 958090be70dd525b actual 958090be70dd525b5a07f4378ac95fb4…  MATCH
F7 recorded 4de5ebff52463686 actual 4de5ebff52463686ae62655efda62290…  MATCH
F8 recorded 36be8f90fa12a01d actual 14488b9b31892bfedc2b00261b6214ab…  ***MISMATCH***
```

### Per-fixture verdict

| # | Command reproduces? | Words match record? | Digest valid? | Output size |
|---|---|---|---|---|
| 1 | yes | yes (13,864) | **yes** | 5 files, 13,864 w / 97,537 chars |
| 2 | yes | yes (18,315) | **yes** | 8 files, 18,315 w / 132,711 chars |
| 3 | yes | yes (14,134) | **yes** | 5 files, 14,134 w / 100,409 chars |
| 4 | yes | yes (10,893) | **yes** | 6 files, 10,893 w / 78,354 chars |
| 5 | yes | **NO — 12,857 measured vs 12,843 recorded (+14 w)** | **NO** | 5 files, 12,857 w / 92,461 chars |
| 6 | yes | yes (11,537) | **yes** | 6 files, 11,537 w / 83,269 chars |
| 7 | yes | yes (15,767) | **yes** | 5 files, 15,767 w / 112,994 chars |
| 8 | yes | yes (22,258) | **NO** | 6 files, 22,258 w / 157,195 chars |

### Isolating the fixture-5 drift

[Observed] The three files fixture 5 shares with reproducing fixtures
(`RFC-0003/README.md` 920, `governance-homes-and-owner-acts.md` 4,414,
`doctrine:vision.md` 2,156 = 7,490) are unchanged, since fixtures 2, 4 and 6
load them and reproduce exactly. The +14 is therefore entirely in fixture 5's
two unique files. Confirmed by sweeping all 32 module rows of
`06-CONTEXT-LOAD-MAP.md` against `wc -w`:

```
modules checked: 32   total words now: 99094
MISMATCHES (module, actual, 06-claimed):
   ('RFC-0010-mission-control-autonomy.md', 3103, 3096)
   ('RFC-0011-context-compiler.md', 2264, 2257)
```

RFC-0010 and RFC-0011 each grew 7 words after `06-CONTEXT-LOAD-MAP.md:33-34`
and fixture 5 were measured. **`RFC-0011-context-compiler.md` — the contract
under review — is one of the two drifted files**, which directly contradicts
`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md:5-6` ("the contract they
exercise is RFC-0011, which this pass did not edit") and
`TASK-TO-CONTRACT-INDEX.md:110-114` finding T-4 ("The rest of 06's per-module
table reproduces exactly (`wc -w`, all 32 modules, same date)"). T-4 is itself
false, and its own reported defect (governance-homes 4,401) is already fixed
in `06-CONTEXT-LOAD-MAP.md:26`, which now reads 4,414.

### Isolating the fixture-8 digest failure

Fixture 8's word total reproduces exactly (22,258) but its digest does not —
so the change is **word-neutral bytes** in one of its six members. I tested
the one word-neutral edit the package documents (the RFC-0007 README
cross-module edge count, `round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md:262-269`)
by reverting it in memory and recomputing; neither `12→7` nor `Twelve→Seven`
reproduces `36be8f90…`. I could not reconstruct the byte state
`36be8f90fa12a01d…` was computed over. Since every member file entered git in
a single commit (`f2d202c`), git bisection is unavailable.

[Inferred] Fixture 8's recorded digest was stale **at the moment it was
committed** — it was never recomputable from the delivered tree. The same is
true of fixture 5, whose totals no artifact in the tree agrees with.

### The reproduction gap this exposes

[Observed] Nothing in the repository checks any of this.
`scripts/verify_final_prespec.py:237-246` is the only fixture check, and it is
a case-insensitive substring test:

```python
    ctx = sorted(fx.glob("context-selection-*.md")) if fx.is_dir() else []
    if len(ctx) < 5:
        fail(f"context-selection fixtures: found {len(ctx)}, need ≥5")
    for p in ctx:
        t = p.read_text(encoding="utf-8")
        for req in ("Required context", "Omitted", "estimate", "constraint", "Suggested", "digest"):
            if req.lower() not in t.lower():
                fail(f"{p.relative_to(root)}: missing '{req}' section")
```

It never executes a fixture's own command block, never recomputes a digest,
never compares a stated total to a measured one. `scripts/check_governance.py`
CG-8 grades *artifact* word counts, not packet totals. Both pass today:

```
$ python3 scripts/verify_final_prespec.py    →  PASS — all checks clean
$ python3 scripts/build_contract_index.py --check  →  index matches regeneration — no drift
$ python3 scripts/build_dependency_index.py --check →  dependency index matches regeneration — no drift
$ python3 scripts/check_governance.py  → 13 OK, 7 WARN, 2 FAIL (22 checks)
     (both FAILs are CG-1b/CG-12 in round-2026-08b/, outside this scope)
```

So a 25%-invalid digest set passes every gate. The package's own doctrine —
`fixtures/context-selection-8-openspec-authoring.md:171-174`, *"A stale digest
is the correct, visible outcome"* — is only true if something looks. Nothing
looks.

---

## 2. AUTOMATIC vs MANUAL COMPLETENESS (the core of this review)

Method for each of the three: I read the fixture's **Objective** paragraph
only, closed the fixture, derived a needed-context set from doctrine + craft +
the contract corpus, then reopened the fixture and diffed.

### 2a. Fixture 8 — OpenSpec requirement authoring (required)

**Task as stated** (`fixtures/context-selection-8-openspec-authoring.md:8-11`):
*"author the first OpenSpec requirements for an adopted Polaris capability —
the behaviour a surface clause makes user-observable. Risk class: normative
behavioural specification; the output is an owner-approved spec delta, not
code."*

**My independent derivation.** An author of the *first* behavioural
requirements for a Polaris capability must hold:

| # | Need | Where it lives | In the fixture's set? |
|---|---|---|---|
| M1 | What a Capability identity is; that Requirement/Scenario are *references*, not owned content | RFC1-14, RFC1-15 (`rfcs/RFC-0001-…:266-281`) | ✅ mandatory |
| M2 | The obligations the surface must satisfy, i.e. what is user-observable | `RFC-0007/rendering-and-surface.md` | ✅ mandatory |
| M3 | The boundary rule saying this RFC schedules nothing and demanding a clause-to-requirement matrix | RFC7-38 (`RFC-0007/rendering-and-surface.md:306-320`) | ✅ mandatory |
| M4 | The adoption gate the delta must pass | VIS-3, VIS-4 (`doctrine/vision.md`) | ✅ mandatory |
| M5 | That direct writes are confined to `openspec/**` "in OpenSpec-compatible form" | VIS-5 (`doctrine/vision.md`) | ✅ (rides along in M4's file) |
| M6 | How a requirement must be stated to be verifiable; Unknown/absence branches are first-class | CC-TEST-5, CC-TEST-6 (`craft:testing-and-verification.md:105-133`) | ✅ mandatory |
| **M7** | **The closed vocabulary the requirement's observable outcomes must be stated in — Unknown reasons and sibling surface states** | **RFC2-24, RFC2-25 (`RFC-0002/rendering-vocabularies.md`)** | ❌ **demoted to *suggested*** (`…-8-…:145-151`) |
| **M8** | **The act machinery that makes "owner-approved" mean something for a first-ever artifact in a governance home** | **RFC3-16(a)/(b)/(c) (`RFC-0003/governance-homes-and-owner-acts.md`)** | ❌ **not loaded, and not individually named — swept into a blanket line at `…-8-…:91-92`** |

**M7 is the substantive omission, and it is self-contradicting.** [Observed] I
extracted every `RFCn-m` citation from fixture 8's four loaded RFC modules and
resolved each through `05-CONTRACT-INDEX.yaml`:

```
F8: clause citations pointing at modules NOT in the packet (module -> citation count):
    20  RFC-0006-cross-surface-selection-query-drawer.md
    11  RFC-0002/rendering-vocabularies.md
     9  RFC-0003/manifests-and-namespace.md
     9  RFC-0003/governance-homes-and-owner-acts.md
     7  RFC-0002/reconciliation-chain.md
     6  RFC-0002/snapshot-and-evaluation-core.md
     5  RFC-0009/visual-grammar-and-lenses.md
     3  RFC-0005/consent-egress-secrets.md
     3  RFC-0004/execution-record.md
     2  RFC-0002/challenge-lifecycle.md
Total distinct out-of-packet clauses cited: 34
RFC-0002/rendering-vocabularies clauses cited by F8's loaded modules: ['RFC2-24', 'RFC2-25']
```

The packet loads `narrative-contract.md`, which invokes RFC2-24's closed
Unknown-reason vocabulary and RFC2-25's sibling-surface-state vocabulary
**eleven times at binding strength** — e.g. `RFC-0007/narrative-contract.md:252`
*"nothing here mints, implies, or requires an RFC2-24 Unknown reason — that
vocabulary…"* and `:315` *"one epistemic state — its label with its RFC2-25…"*.
An author writing the first scenarios for a Polaris capability will state
observable outcomes; without RFC2-24/25 they will invent state names. That is
precisely the closed-vocabulary failure the corpus is built to prevent.

The comparison that makes this decisive: **accepted fixture 1 — a *lower-risk*
content edit on the same surface — loads `RFC-0002/rendering-vocabularies.md`
as mandatory** (`fixtures/context-selection-1-polaris-narrative.md:19-21`).
Fixture 8, authoring normative behaviour on the same surface, demotes the same
file to suggested. The stated reason (`…-8-…:84-87`) is *"requirements
reference capabilities, not evaluations"* — but RFC2-24/25 are not evaluation
machinery, they are the rendering vocabulary, which is exactly what fixture 1
loads it for. [Inferred] the demotion is budget pressure acting on a packet
already 50% over the trigger — the pressure RFC11-5 exists to make visible,
here operating silently under a "suggested" label.

**Avoidable bulk in fixture 8's set.** `RFC-0007/narrative-contract.md` is
5,167 words — 23% of the packet — and it governs *curated narrative authoring*
("may this sentence exist in curated narrative, and what act does it take to
put it there?", `RFC-0007/README.md:62-63`), which is fixture 1's task, not
fixture 8's. It is pulled in because routing granularity is the **contract**
(`applies_to: polaris` → all of RFC-0007), not the clause. The fixture's own
decomposition table dismisses dropping it as buying "nothing" (`…-8-…:73`) —
that is measured against the wrong baseline: the honest question is whether an
author of *requirements* needs the clauses governing *narrative sentence
adoption*, and I could not construct a case that they do.

**Net honest packet.** Remove `narrative-contract.md` (−5,167 w) and add
`RFC-0002/README.md` + `rendering-vocabularies.md` (+4,215 w) and the packet
lands at **21,306 w ≈ 28,763 est. tokens — still 92% over the band top and
44% over the trigger.** So the fixture's headline conclusion (no lawful split
lands inside the band) survives my re-derivation; its *composition* does not.

### 2b. Fixture 6 — doctrine amendment (D3)

**Task as stated** (`fixtures/context-selection-6-doctrine-amendment.md:8-10`):
*"draft a minimal doctrine amendment packet (the D3 bounded-mission shape) and
prepare its owner-adoption ceremony."*

**Omission the automatic route makes, which I call mandatory: the amendment
packet itself.** The objective's primary entity is D3. The tree holds
`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1, 13,525 bytes) and the
superseded `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`. Neither is in the
mandatory set, and **neither appears in the omission register** — the register
(`…-6-…:44-72`) accounts for every RFC, every doctrine file, the craft
policies, topology and the historical lane, but not the artifact being
drafted. This is the *identical defect class* the pass repaired in this
fixture: `round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md:139-144` records
that the pre-repair fixture *"stated 'the amended text itself is mandatory'
and then omitted half of it, from both its mandatory set and its exclusion
register."*

**Worse, the one place it is named is stale.** `…-6-…:18` cites
`DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md` as the source of the amendment
sites. `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md:3-7` declares itself *"a
minimally revised replacement for `DOCTRINE-AMENDMENT-BOUNDED-MISSION-DRAFT.md`
(sha256 30efb7c5…)"*, and `AGENTS.md`'s act-5 row says rev1 supersedes the
DRAFT. The fixture's selection trace therefore routes through a superseded
artifact. Line `…-6-…:100-101` then refers to "the D3 packet" without
disambiguating which — the two disagree on §1's structure.

**Everything else in fixture 6 I independently derived was present:** both
amendment sites (`architecture.md`, `vision.md`), the V0/V1 boundary
(`v1.md`), the amendment-log home and identifier-stability rule
(`doctrine/README.md`), and the act machinery (RFC-0003 README +
governance-homes). I could name no *further* mandatory miss.

**Avoidable bulk:** none material. `RFC-0003/README.md` (920 w) is an index,
but it carries the deterministic clause-lookup rule and is cheap.

### 2c. Fixture 2 — Trajectory work-provider adapter (accepted set)

**Task as stated** (`fixtures/context-selection-2-trajectory-adapter.md:3-7`):
amend the substrate→normalized work-state derivation mapping; *"the mapping
widens what the surface reports as live/dispatchable, so it is an RFC3-16(a)
artifact."*

**Omission I call mandatory: `doctrine/vision.md`.** The change alters what
Syzygy asserts about work state. The governing doctrine is the three-state
thesis — *"scheduled or completed work is never proof that the implementation
satisfies intent"* (`doctrine/vision.md`, Thesis) — plus VIS-2 (*no evidence
means Unknown, not success*) and VIS-1's ordering. The packet loads
`RFC-0008/README.md`, which at `:29-30` says only *"**Serves:** vision.md
Thesis (three states; work is never proof), VIS-1, VIS-2, VIS-5…"* — a
**citation of the rule, not the rule text**. That is exactly the substitution
the pass repaired in fixture 8
(`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md:148-152`: a README
"restates … and points at this module"). The accepted set was not held to the
standard the repaired set was.

Compounding it, fixture 2's register **does not name vision.md at all**; the
fixture report's own §2 table (`…FIXTURE-REPORT.md:89`) records fixture 2 as
leaving *"vision, architecture, v1, trust-and-evidence"* neither loaded nor
named — recorded as finding §6e and deliberately not fixed.

**Second omission: any craft policy.** Fixture 2 loads none, and dismisses all
of them in one line (`…-2-…:46`, *"craft — not cited by the warrant's clause
set"*). But the artifact being amended is a derivation mapping whose output
becomes rendered status; CC-TEST-6 (*"Unknown and absence paths are
first-class test targets"*, `craft:testing-and-verification.md:120-133`) binds
exactly this change. Fixtures 4 and 7 both pull a craft policy when a duty is
implicated; fixture 2 does not, on a change it labels authorization-bearing.
The selection rule is not being applied consistently across the set.

**Avoidable bulk in fixture 2:** `RFC-0004/named-adapters.md` (3,685 w) is the
largest single item and covers *all* named adapters, of which one is in scope
— again a whole-module pull where clause-level routing would narrow. This is a
corpus-granularity limit, not a selector error.

### 2d. What items 2a–2c establish

The automatic route's misses are not random. They cluster in two shapes:

1. **README-citation-for-clause-text substitution** — a packet loads a module
   that *names* a rule (VIS-2, RFC2-24) and treats the naming as carriage.
   Found in fixtures 2 and 8. The package identified this failure mode
   (`…FIXTURE-REPORT.md:100-108`, "no generated summary replaces exact
   authority", left ⬜ unchecked in all eight) and then committed it twice more
   in files it had just repaired.
2. **Whole-contract granularity** — `applies_to: polaris` pulls 10,636 words
   of RFC-0007 when two of its three modules carry the load-bearing clauses.
   No mechanism exists to pull `RFC7-38 + RFC7-26..37` without
   `RFC7-1..RFC7-25`.

---

## 3. DOCTRINE AND CRAFT AS FIRST-CLASS INPUTS

**Answer: partially, and at strictly coarser granularity than RFC contracts —
with a routing key that cannot distinguish a rule's owner from a rule's
mention.**

### 3a. In the script: no routing at all, only path resolution

`scripts/context_load.py:23-26` gives doctrine and craft *prefixes*:

```python
PREFIX_HOMES = {
    "doctrine:": [".syzygy/governance/doctrine", "doctrine"],
    "craft:": [".syzygy/governance/policies/craft-and-care", "craft-and-care"],
}
```

That is a filename resolver (`:29-48`), nothing more. It resolves to the
canonical home and prints the source to stderr — a genuinely good
anti-source-swap guard, and it fired correctly in every run above. But the
script selects nothing.

### 3b. In the projection: whole-file, and the key is a mention scan

`05-CONTRACT-INDEX.yaml` does carry doctrine and craft now, as
`governance_sources` (27 rows). [Observed] the generator:

```python
RULE_ID = re.compile(r"\b(VIS-\d+|SEC-\d+|CC-[A-Z]+-\d+)\b")   # build_contract_index.py:36
GOV_SOURCES = [("../../doctrine", "doctrine", "doctrine"),
               ("../../policies/craft-and-care", "craft-and-care", "craft-policy"),
               ("../../../map/topology-candidates", "topology", "topology")]   # :42-44
…
            ids = sorted(set(RULE_ID.findall(text)), …)                        # :143
            words = len(text.split())
            lines.append(f"  - {{file: {dirname}/{f.name}, role: {role}, words: {words}"
                         + (f", rule_ids: [{', '.join(ids)}]" if ids else "") + "}")  # :146-147
```

Three consequences, all [Observed]:

1. **`rule_ids` is "rules mentioned anywhere in this file", not "rules this
   file owns."** Routing on it over-selects badly:

   ```
   VIS-4:  7 files -> doctrine/v1.md, doctrine/vision.md, craft/engineering-bar.md,
                      craft/review-and-documentation.md, craft/security-and-secrets.md,
                      topology/01-system-context.md, topology/06-intent-to-reconciliation-flow.md
   VIS-7: 13 files
   SEC-3:  7 files
   VIS-3:  3 files
   ```

   A deterministic selector asked "which artifact carries VIS-4?" gets seven
   answers, one of which is authoritative and two of which are candidate
   topology files that bind nothing.

2. **No clause-level rows exist for doctrine or craft.** RFC clauses get
   `{id: RFC7-38, module: …, kind: phase-rule}` — 322 such rows. Doctrine and
   craft rows carry `{file, role, words, rule_ids}` and nothing else:

   ```
   total governance_sources rows: 27
   rows with 'clauses' key:        0
   ```

   So RFC11-4's *"clause-level metadata (the contract-index projection)"* is
   satisfiable for contracts and **not satisfiable for doctrine or craft**.
   Fixtures 6, 7 and 8 concede this in a shared paragraph ("the doctrine and
   craft selections above were additionally verified against the files
   directly", e.g. `…-8-…:141-143`) — i.e. by hand.

3. **No `governs` / `applies_to` / `depends_on` for doctrine or craft.** There
   is no machine path from a task class to VIS-5, only from a task class to
   "the file that mentions VIS-5 most plausibly."

### 3c. Do the fixtures route at clause level where clause metadata exists?

Sometimes, and that is the honest answer. Fixture 8's RFC7-38 catch is a real
clause-level routing success and the fixture says so
(`…-8-…:132-137`): the index row `{id: RFC7-38, module:
RFC-0007/rendering-and-surface.md, kind: phase-rule}` forced a second module
into the set. That is the mechanism working.

But it is used as a *check after the fact*, not as the selector. And it
routes **up** to a whole module, never down to a clause: catching RFC7-38 cost
3,143 words to obtain one clause of ~200. There is no shard-a-module facility,
so clause-level metadata always cashes out as module-level loading.

### 3d. The deterministic rule has no stated closure cutoff

RFC11-4 (`rfcs/RFC-0011-context-compiler.md:106-121`) lists *"contract
dependencies (`depends_on` / `provides_to`)"* among the deterministic inputs.
`RFC-0007/README.md:10` declares `depends_on: [RFC-0001, RFC-0002, RFC-0003,
RFC-0004, RFC-0005, RFC-0006]`. Fixture 8 follows exactly one of those six
edges and states no rule for stopping. Measured across the set, every fixture
leaves a large tail of cited-but-unloaded clauses:

```
 fx   distinct out-of-packet clauses cited by the loaded modules
  1    53      top: RFC-0007/rendering-and-surface (11), RFC-0006 (8), RFC-0001 (7)
  2    67      top: RFC-0003/manifests (12), RFC-0001 (8), RFC-0002/core (8)
  3    70      top: RFC-0009/semantic-geography (16), RFC-0006 (11), RFC-0002/core (7)
  4    54      top: RFC-0003/manifests (13), RFC-0005/admission (11), RFC-0005/consent (6)
  5    49      top: RFC-0003/manifests (11), RFC-0004/named-adapters (4), RFC-0005/admission (4)
  6    36      top: RFC-0003/manifests (11), RFC-0004/named-adapters (4), RFC-0005/consent (3)
  7    22      top: RFC-0002/reconciliation (6), RFC-0002/challenge (3), RFC-0003/gov-homes (3)
  8    34      top: RFC-0006 (10), RFC-0003/manifests (6), RFC-0002/reconciliation (5)
```

A citation is not a mandatory inclusion — I am not claiming these 22–70 items
each belong in each packet. The claim is narrower and firmer: **RFC11-4 names
`depends_on` as a deterministic input and gives no termination rule, so two
compliant compilers can produce different "deterministic" sets from the same
warrant.** Nothing in the corpus closes that.

### 3e. The compiler/selection-rule version does not resolve

RFC11-4 requires *"The selection rule set is versioned with the compiler
(RFC11-1's version identity)."* All eight fixtures record `Compiler:
context_load.py, selection rules rev10-fixtures`. [Observed] `rev10-fixtures`
appears **only inside the eight fixtures** and in no other file in `.syzygy/`
or `scripts/`; `context_load.py` contains no version constant (`grep -n
"version\|VERSION" scripts/context_load.py` → no output). The version field is
a self-referential label naming nothing.

---

## 4. BUDGET

### Token-estimation method (both figures are estimates; neither is a tokenizer)

- **Estimate A** — the repository's own heuristic, `words × 1.35`, stated at
  `scripts/context_load.py:13-15`. Used for all in-tree verdicts.
- **Estimate B** — `characters ÷ 4`, the conventional English-BPE
  approximation, computed here as a second method because these files are
  markdown with tables and hyphenated identifiers (`RFC3-16(a)`,
  `state-undetermined`), which tokenize far worse than prose. Measured mean
  density across the eight packets is **7.15 characters per whitespace word**
  (854,930 chars / 119,625 words)
  versus ~6.0 for ordinary English prose, so Estimate A is optimistic by
  construction.

No tokenizer is installed on this machine (`import tiktoken` and `import
transformers` both fail), so I cannot give a true count. The true value very
likely sits between A and B, nearer B for the table-heavy modules.

Band: default **5,000–15,000 tokens**; **above 20,000** → justification or
decomposition (`round-2026-08/OWNER-ROUND-CHARTER.md:804-818`, and identically
`policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:288-296` as CC-BUDGET-1).

### The table

| Fixture | Words | Est. A (w×1.35) | Est. B (chars/4) | Within 5–15k band? | Above 20k trigger? |
|---|---:|---:|---:|---|---|
| 1 — Polaris narrative re-anchor | 13,864 | 18,716 | 24,384 | **NO** (A and B) | A: no · **B: YES** |
| 2 — Trajectory adapter mapping | 18,315 | 24,725 | 33,177 | **NO** (A and B) | **YES** (A and B) |
| 3 — Orrery lens change | 14,134 | 19,080 | 25,102 | **NO** (A and B) | A: no · **B: YES** |
| 4 — Execution-profile amendment | 10,893 | 14,705 | 19,588 | A: **yes** · B: **NO** | no (A and B) |
| 5 — Cross-project Mission | 12,857 | 17,356 | 23,115 | **NO** (A and B) | A: no · **B: YES** |
| 6 — Doctrine amendment (D3) | 11,537 | 15,574 | 20,817 | **NO** (A and B) | A: no · **B: YES** |
| 7 — Kernel identity change | 15,767 | 21,285 | 28,248 | **NO** (A and B) | **YES** (A and B) |
| 8 — OpenSpec authoring | 22,258 | 30,048 | 39,298 | **NO** (A and B) | **YES** (A and B) |

Corpus baseline for scale: 99,094 words of RFC modules alone (measured this
session); the package's whole-corpus figure is ~123,180 w ≈ 166,293 est. tokens.

### Design findings from the table

- **Under the repository's own heuristic, exactly one of eight fixtures (4)
  lands inside the default band, and three breach the trigger.** The package
  states this honestly at `…FIXTURE-REPORT.md:123-125`.
- **Under the second estimate, zero of eight land inside the band and six of
  eight breach the trigger.** Every "inside the band / below the trigger"
  verdict in fixtures 1, 3, 5 and 6 is an artifact of choosing 1.35. Fixture 6
  is the sharpest case: it self-reports as *"above the default band by 574
  tokens, disclosed; below the 20k justification trigger, so no waiver"*
  (`…-6-…:144-146`) — under Estimate B it is 20,817 and needs a waiver it does
  not have.
- **The budget posture is therefore untestable as written.** RFC11-11
  (`rfcs/RFC-0011-context-compiler.md:193-209`) requires that *"exceeding the
  posture is a disclosed, reasoned event, never silent"* — but whether the
  posture is exceeded depends on an unfixed heuristic, and the fixtures pick
  the most favorable one without saying it is favorable.
- **Two baselines still coexist**, as the package records (§6d,
  `…FIXTURE-REPORT.md:298-305`): `06-CONTEXT-LOAD-MAP.md:55` grades against a
  *"15–20k working target"* while the fixtures grade against §11.4's 5–15k.
  Under 06's target, fixtures 1/3/4/5 read "✓". Under §11.4 they do not. `06`'s
  table at `:57-61` still shows all four with a bare ✓ and still carries
  fixture 5's stale 12,843 / 17,338.
- **A live contradiction the package does not yet know about.** Fixtures 6, 7
  and 8 each assert that the knowledge-hygiene craft policy *"is not
  installed, and no `CC-BUDGET-*` identifier resolves to a governed artifact
  today"* (`…-6-…:38-41`, `…-7-…:45-48`, `…-8-…:51-55`). [Observed] the file
  exists — `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`, 22,700
  bytes, carrying CC-BUDGET-1…4 at `:288-330` — and
  `06-CONTEXT-LOAD-MAP.md:8-9` *already cites* `CC-BUDGET-1` by identifier and
  path. The fixture report's own §6g (`…FIXTURE-REPORT.md:322-328`) set the
  trigger — *"When the policy lands … three citations in fixtures 6–8 should
  be re-pointed"* — and the trigger has fired unnoticed. (The narrower reading,
  "no CC-BUDGET-* resolves to a *governed* artifact", survives, since a
  candidate binds nothing; "is not installed" does not.)

---

## 5. FIXTURE COVERAGE AGAINST THE REQUIRED CLASSES

| Required class | Fixture | Assessment |
|---|---|---|
| Doctrine amendment | **6** | Clean fit. |
| Kernel identity change | **7** | Clean fit. |
| OpenSpec capability authoring | **8** | Clean fit. |
| Evidence adapter change | **2 (contested)** | See below — **effectively uncovered.** |
| Polaris governed-presentation edit | **1** | Clean fit. |
| Trajectory work-lifecycle change | **2** | Best fit for fixture 2. |
| Orrery visual/lens change | **3** | Clean fit. |
| Bounded Mission spanning capabilities | **5** | Clean fit. |
| — | **4** | **Serves no required class.** |

**The evidence-adapter class has no fixture.** Fixture 2 is a *work-provider*
adapter change. It loads `RFC-0004/general-contract.md` +
`named-adapters.md` and explicitly **excludes** the two modules that carry the
evidence plane — `execution-record.md` and `fidelity-joins-and-mappings.md`
(`…-2-…:36-39`, *"the mapping change touches ingestion classification, not
execution-record capture or join semantics"*). RFC-0004 is titled *"Observation
Sources, Evidence, Execution Records and Adapters"*; fixture 2 deliberately
takes the non-evidence half. So the class *"evidence adapter change"* —
capture cadence, fidelity labels, provenance joins, gate-artifact tiering
(RFC4-13's four routes, which CC-TEST-2 leans on) — is exercised by **no
fixture in the set**. Counting fixture 2 twice makes the eight-for-eight map
look complete when it is seven-for-eight with one double-count.

**Fixture 4 (security / execution-profile amendment) matches no required
class.** It is a good fixture — it is the *only* one inside the default band
under Estimate A, and the only accepted-set fixture that pulls a craft policy
— but it is not one of the eight classes asked for.

Neither gap is named in `…FIXTURE-REPORT.md`, whose §1 table presents the
eight as a set without mapping them to required classes at all.

`semantic-equivalence-fixtures.md` is a separate instrument (rev9→rev10
equivalence, F-EQ-1…8) and correctly not counted here. Note its commands are
written for GNU grep (`:9-11`); on this machine `grep` is ugrep, so F-EQ-4/F-EQ-8
would need re-running under a real GNU grep before their results are quotable.

---

## 6. RECORD-COMPLETENESS MATRIX

Legend: **P** present · **∼** partial · **✗** absent · **P!** present but
**invalid as recorded** (verified this session).

| # | Task | Mandatory inclusions | Forbidden / irrelevant exclusions | Risk class | Authority layers | Budget | Omissions | Packet digest | Compiler / metadata version |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P | P | ∼ | P | ∼ | P | ∼ | P | ∼ |
| 2 | P | P | ∼ | P | ∼ | P | ∼ | P | ∼ |
| 3 | P | P | ∼ | P | ∼ | P | ∼ | P | ∼ |
| 4 | P | P | ∼ | P | ∼ | P | ∼ | P | ∼ |
| 5 | P | P | ∼ | P | ∼ | P | ∼ | **P!** | ∼ |
| 6 | P | P | P | P | ∼ | P | P | P | ∼ |
| 7 | P | P | P | P | ∼ | P | P | P | ∼ |
| 8 | P | P | P | P | ∼ | P | P | **P!** | ∼ |

**Column notes.**

- *Forbidden / irrelevant exclusions* — fixtures 1–5 account for the RFC
  universe only. Per `…FIXTURE-REPORT.md:86-95` (which I spot-verified against
  fixtures 1, 2 and 4): F1 leaves architecture/v1/trust-and-evidence unnamed;
  F2 leaves vision/architecture/v1/trust-and-evidence unnamed; F4 names no
  craft policy **despite loading one**; none of 1–5 names the topology bundle
  or the historical lane. Fixtures 6–8 enumerate everything. Recorded as
  finding §6e and deliberately not repaired.
- *Authority layers* — **∼ for all eight**, and this is the weakest column. No
  fixture records the authority tier of what it loads as a field; the
  `doctrine:`/`craft:`/`rfcs/` prefixes imply it. More seriously: every
  fixture labels the topology bundle *"candidate material that binds
  nothing"* (e.g. `…-7-…:95-97`) and **no fixture says the same of the RFC
  modules that form its mandatory core** — which are equally candidates
  pending act 1 per `AGENTS.md`. A packet whose entire normative core binds
  nothing should disclose that under RFC11-6.
- *Budget* — P for all eight, and this is the strongest column: every fixture
  states a measured figure, a baseline and a verdict, and fixtures 7 and 8
  measure their decomposition alternatives rather than asserting none exists.
- *Packet digest* — P! for 5 and 8 (§1 above). The other six recompute exactly.
- *Compiler / metadata version* — ∼ for all eight: the string
  `selection rules rev10-fixtures` resolves nowhere (§3e).

**RFC11-1 fields absent from all eight**, and this is the honest headline the
package itself states at `…FIXTURE-REPORT.md:230-234`: project/workspace
identity; selected evaluation and as-of instant; the work warrant and autonomy
envelope; allowed tools and permissions; active decisions/contradictions/
Unknowns in scope; the projection-verification record RFC11-4 requires ("the
packet records the projection verification it performed"). Eight fixtures
demonstrate the **document-selection dimension only**. The report says this in
one paragraph; I would put it in every fixture's banner, because the phrase
"eight measured fixtures" will otherwise be read downstream as packet-format
validation.

---

## 7. OPENSPEC READINESS PROOF — attempting fixture 8's task from its packet alone

I attempted the task using only `RFC-0001`, `RFC-0007/{README,
narrative-contract, rendering-and-surface}`, `doctrine/vision.md`,
`craft:testing-and-verification.md`.

**(a) Restate the relevant north-star constraint — SUCCEEDED.** `vision.md`
§"The north star (honestly labeled)" is in the packet: the regeneration ideal
(Project Genome) is *direction, not present doctrine*; no artifact may claim it
as current capability; **a decision that materially forecloses it must record
that foreclosure — the unrecorded foreclosure is the violation.** A requirement
author can act on that: if a requirement freezes a schema or hard-codes a
realization detail that forecloses regeneration, the delta must say so. VIS-1's
five-rank ordering and VIS-5's `openspec/**`-and-`.syzygy/**` write confinement
are likewise present and directly usable.

**(b) Identify the correct capability — FAILED, and the packet is not at
fault.** The objective says *"an adopted Polaris capability"* and **names
none**. RFC11-4's first deterministic input is *"stable entity and relation
identities in the objective's scope"*; fixture 8's warrant supplies no entity
identity. The packet gives me RFC1-14 (what a Capability *is*: "a named unit
of declared behavior that the project's own spec or shape documents assert
exists") and RFC1-14's rule that capability identities come only from the
project's own declared artifacts — and there are no such artifacts, because
there is no application and no `openspec/`. So the correct output here is
**Unknown, and under RFC11-6 the run does not launch.** The fixture does not
render that verdict; it renders a complete packet with a budget waiver. That
is a real gap between the fixture and the clause it exercises.

**(c) Cite applicable contracts — SUCCEEDED, partially.** From the packet I can
cite RFC1-14/RFC1-15 for identity and reference-not-content, RFC7-38 verbatim
for the phase boundary, and the RFC7-26..37 obligations by ID. What I cannot do
from the packet is resolve any of the 34 out-of-packet clause citations those
modules make — most consequentially RFC2-24/RFC2-25, which `narrative-contract.md`
invokes eleven times. Writing a scenario asserting an observable Unknown state
requires that vocabulary and I do not have it. See finding 2.

**(d) Distinguish required behaviour from structural design — SUCCEEDED.**
RFC7-38 is unambiguous and in the packet as clause text, not restatement:
*"every observable consequence of RFC7-1…RFC7-37 must either map to an approved
OpenSpec requirement or scenario … or carry an explicit, reviewed N/A judgment
recording why that consequence needs no requirement,"* plus the
clause-to-requirement coverage matrix as a **package-level** deliverable
(`RFC-0007/rendering-and-surface.md:306-323`). That is exactly the required
distinction, with the N/A route named. Loading `rendering-and-surface.md`
rather than the README's pointer is what makes this work — the repair earned
its cost.

**(e) Name unresolved product questions — SUCCEEDED.** `RFC-0007/README.md:250-270`
gives the stable §8 index: **q2** (primary-narrative cardinality, RFC7-6) and
**q4** (rejected-draft retention, RFC7-22) are open, plus **OQ-010** (where a
cross-project fact or Project-relationship entity lives) flagged as open and
not a §8 question. RFC-0001 §8 is also in the packet. I could name these
without leaving the packet.

**(f) Avoid creating implementation work — SUCCEEDED, with a caveat.** RFC7-38
and VIS-4 make it plain that the output is a spec delta requiring owner
adoption, and VIS-5 confines writes. But the packet contains **no OpenSpec
house conventions** — the fixture names this correctly as *"a real gap, not an
exclusion"* (`…-8-…:112-115`) and says the packet "would render that gap as
Unknown (RFC11-6)". It says *would*. The fixture's §15 checklist then ticks
*"All mandatory context included"* (`…-8-…:180-183`). Both cannot hold: a
packet with a named, unfilled Unknown in its required set is incomplete under
RFC11-6, and under RFC11-6's default the run blocks. The fixture is one
sentence away from being right and instead grades itself complete.

**(g) One further shortfall.** `craft:testing-and-verification.md` was selected
because *"a requirement must be stated so it can be verified"*
(`…-8-…:33-34`). Reading it, CC-TEST-5 (declared verification scope, oracle
adequacy) and CC-TEST-6 (Unknown/absence branches are first-class) genuinely
help a scenario author. The other four clauses govern *test execution and gate
evidence*, not requirement statement. And CC-TEST-2 is itself mid-amendment
(act 2 pends on its digest per `AGENTS.md`) — the fixture discloses this in its
digest-pinning note (`…-8-…:170-173`) but does not mark the clause as pending
inside the selection, which is what RFC11-6's "staleness disclosed *inside* the
packet" asks for.

**Net:** four of six sub-tasks succeed cleanly from the packet alone; (b) fails
because the warrant is underspecified and the fixture should have rendered
Unknown; (c) is degraded by the RFC2-24/25 demotion. The packet is good enough
to write *about* requirements and not good enough to write *a* requirement.

---

# VERDICT: REVISE

*(The word above is my verdict for the fixture/report package as delivered.
RFC-0011's own clause text I found sound; I raise no defect against
RFC11-1…RFC11-12 as written. The revisions below are in the evidence that the
contract's testable claims rest on, plus two contract-level gaps.)*

---

### Findings

**1. [Blocking] Two of eight recorded packet digests do not reproduce, and one
fixture's word total is wrong.** Fixture 5 measures 12,857 w / 17,356 est.
tokens against a recorded 12,843 / 17,338, and its digest is `ca4e8511348c14c8`
not `c92c6f8a936b12b0`. Fixture 8's words reproduce exactly but its digest is
`14488b9b31892bfe` not `36be8f90fa12a01d` — a word-neutral byte change I could
not reconstruct, meaning it was already stale when committed. The drifted files
are `RFC-0010` (3,096→3,103) and `RFC-0011` (2,257→2,264); RFC-0011 is the
contract under review, contradicting `…FIXTURE-REPORT.md:5-6` ("which this pass
did not edit").
*Fix:* re-run each fixture's own command block and its `cat … | sha256sum`,
restate the five affected numbers (fixture 5's total and digest, fixture 8's
digest), and correct `06-CONTEXT-LOAD-MAP.md:33-34`, `:61` and the
`…FIXTURE-REPORT.md:44` row.

**2. [Blocking] Fixture 8 demotes RFC2-24/RFC2-25 to *suggested* while loading
a module that invokes them eleven times at binding strength.** The lower-risk
accepted fixture 1 loads `RFC-0002/rendering-vocabularies.md` as mandatory for
the same surface. A requirement author without the closed Unknown-reason and
sibling-surface-state vocabularies will invent state names.
*Fix:* promote `RFC-0002/README.md` + `rendering-vocabularies.md` to fixture
8's mandatory set (+4,215 w) and restate the waiver at the honest number; if
budget is the reason not to, say that in the waiver rather than in the word
"suggested".

**3. [Blocking] Fixture 6 omits the artifact it is drafting, from both its
mandatory set and its omission register, and cites a superseded version of
it.** `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1) appears in neither
set; `…-6-…:18` names the superseded `…-DRAFT.md`. This is the same defect
class the pass repaired in this fixture
(`…FIXTURE-REPORT.md:139-144`).
*Fix:* add the D3 rev1 packet to fixture 6's mandatory set (or name it in the
register with a reason), re-measure, and re-point `…-6-…:18` to the rev1 file.

**4. [Blocking] Nothing in the repository verifies a fixture against its own
bytes.** `verify_final_prespec.py:237-246` is a six-substring presence test; it
never runs a fixture's command block, never recomputes a digest, never compares
a stated total to a measured one. All gates pass over a 25%-invalid digest set.
*Fix:* extend the verifier to parse each fixture's fenced `Required context`
command, execute `context_load.py` on it, compare the total against the stated
`Measured:` figure, and recompute the sha256 against the stated prefix — three
`fail()`s.

**5. [Blocking] Fixture 2 loads a README's *citation* of VIS-1/VIS-2 in place
of the doctrine rule text, on a change it labels authorization-bearing.**
`RFC-0008/README.md:29-30` says "Serves: vision.md Thesis (three states; work
is never proof), VIS-1, VIS-2…"; `vision.md` is neither loaded nor named. This
is exactly the substitution repaired in fixture 8. Fixture 2 also loads no craft
policy despite CC-TEST-6 binding a status-deriving mapping change.
*Fix:* either add `doctrine:vision.md` to fixture 2's mandatory set, or record
in its register why a rule cited by a loaded module need not travel — and apply
whichever answer uniformly across all eight.

**6. [Non-blocking] The required class "evidence adapter change" has no
fixture, and fixture 4 serves no required class.** Fixture 2 covers the work-
provider half of RFC-0004 and explicitly excludes `execution-record.md` and
`fidelity-joins-and-mappings.md`, so evidence capture, fidelity labels,
provenance joins and RFC4-13 gate tiering are exercised nowhere.
*Fix:* add a ninth fixture for an evidence-adapter change, or state in
`…FIXTURE-REPORT.md` §1 which required class each fixture serves and record
the gap.

**7. [Non-blocking] Every budget verdict is an artifact of the chosen 1.35
tokens/word heuristic.** Under `chars ÷ 4`, zero of eight land inside the
default band and six of eight breach the 20,000 trigger; fixtures 1, 3, 5 and 6
flip from "no waiver needed" to "waiver needed". The packets average 7.15
chars/word, well above prose density.
*Fix:* state both estimates in each fixture's `Measured:` line (the script can
print both in three lines), or pin one tokenizer as the measuring instrument
and say so. Until then no "within budget" claim is falsifiable.

**8. [Non-blocking] Fixtures 6, 7 and 8 assert that the knowledge-hygiene craft
policy "is not installed" and that no `CC-BUDGET-*` identifier resolves.** The
policy exists at `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` carrying
CC-BUDGET-1…4 at `:288-330`, and `06-CONTEXT-LOAD-MAP.md:8-9` already cites
`CC-BUDGET-1` by identifier and path. The re-point trigger recorded at
`…FIXTURE-REPORT.md:322-328` has fired unnoticed.
*Fix:* re-point the three citations to `CC-BUDGET-1`, keeping the "candidate,
binds nothing" qualifier — a one-line change per fixture, already scoped by §6g.

**9. [Non-blocking] `TASK-TO-CONTRACT-INDEX.md` finding T-4 is false in both
directions.** It reports `06-CONTEXT-LOAD-MAP.md` as carrying governance-homes
at 4,401 (06 line 26 reads 4,414 — already fixed) and claims *"the rest of 06's
per-module table reproduces exactly (`wc -w`, all 32 modules, same date)"*,
which my 32-module sweep disproves (RFC-0010 and RFC-0011).
*Fix:* rewrite T-4 against a re-run sweep, or delete it and let the drift check
in finding 4 own the claim.

**10. [Non-blocking] The compiler/selection-rule version identifier resolves to
nothing.** `selection rules rev10-fixtures` occurs only inside the eight
fixtures; `context_load.py` carries no version constant. RFC11-4 requires the
selection rule set to be versioned with the compiler.
*Fix:* add a `SELECTION_RULES = "…"` / `COMPILER_VERSION = "…"` constant to
`context_load.py`, print it in the output, and have the fixtures quote what the
script prints.

**11. [Non-blocking] Doctrine and craft route at whole-file granularity on a
mention scan.** `build_contract_index.py:36,143` keys `rule_ids` on
`RULE_ID.findall(text)`, so VIS-4 resolves to seven files (two of them
candidate topology) and VIS-7 to thirteen; `governance_sources` rows carry no
clause rows, no `governs`, no `applies_to`. RFC contracts get 322 clause rows;
doctrine and craft get zero.
*Fix:* either emit an `owns:` field (rules whose definition heading appears in
the file) distinct from `mentions:`, or state in RFC-0011 §7 that clause-level
routing for doctrine and craft is deliberately deferred — right now the corpus
implies a capability it does not have.

**12. [Non-blocking] RFC11-4 names `depends_on`/`provides_to` as deterministic
selection inputs and states no closure-termination rule.** RFC-0007 declares
six dependencies; fixture 8 follows one and explains the cutoff in prose.
Measured, each fixture leaves 22–70 distinct cited-but-unloaded clauses. Two
conforming compilers can produce different "deterministic" sets from one
warrant.
*Fix:* one sentence in RFC11-4 fixing the closure (e.g. "first-order
`depends_on` edges of contracts selected by `applies_to`, plus every
phase-rule clause of every selected contract; deeper edges are suggested"), or
an explicit deferral in §7.

**13. [Non-blocking] No fixture discloses that its own mandatory core is
candidate material binding nothing.** All eight label the topology bundle
"candidate … binds nothing"; none says it of the RFC modules that constitute
their packets, which are equally pending act 1.
*Fix:* one line in each fixture's banner, or one line in
`…FIXTURE-REPORT.md` §5 beside the existing "these are selection fixtures, not
packets" disclosure.

**14. [Non-blocking] Fixture 8 ticks "All mandatory context included" while
naming an unfilled required gap.** It says the missing `openspec/**` house
conventions are *"a real gap, not an exclusion"* and that the packet "would
render that gap as Unknown (RFC11-6)" — then grades the checklist complete. Its
warrant also names no capability identity, so RFC11-4's first deterministic
input is absent and RFC11-6's default (do not launch) is the correct verdict.
*Fix:* change fixture 8's first checklist item to the honest state —
incomplete/Unknown, gap named, run blocked absent an owner-visible relaxation —
which is a *better* demonstration of RFC11-6 than a green tick.

---

*End of RC-6 raw output. Verdict word: REVISE.*
