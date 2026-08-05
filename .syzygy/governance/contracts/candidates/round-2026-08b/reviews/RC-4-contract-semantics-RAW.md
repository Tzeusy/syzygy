# RC-4 — Contract semantics review (fresh context, adversarial)

**Reviewer:** independent fresh-context session. No authoring history read; no
`_bootstrap/` tree read. Given only the artifacts in scope, the adopted
doctrine, the owner-approved craft policy, and the acceptance criteria.

**Date of run:** 2026-08-05.

**Scope reviewed:** `.syzygy/governance/contracts/candidates/` —
`rfcs/**` (32 modules, RFC-0001…RFC-0011), `05-CONTRACT-INDEX.yaml`,
`CONTRACT-DEPENDENCY-INDEX.md`, `TASK-TO-CONTRACT-INDEX.md`,
`06-CONTEXT-LOAD-MAP.md`, `ACTIVE-CONTRACT-MANIFEST.txt`.

**Treated as settled upstream authority:** `.syzygy/governance/doctrine/**`
(adopted), `.syzygy/governance/policies/craft-and-care/**` (owner-approved).

**Question answered:** are these candidates semantically coherent enough to
deserve an owner's acceptance act?

---

## 0. Mechanical baseline — and a corpus that changed mid-review

### 0.1 The review straddles an edit. Read this before any number below.

**`rfcs/RFC-0010-mission-control-autonomy.md` was modified at
`2026-08-05 18:04:52`, during this review**, by a concurrent session
(`git status` shows it modified against `HEAD`, +200/−9 lines). The edit adds a
new §3.7 "The correction plane" carrying **six new clauses, RFC10-17 …
RFC10-22**, and grows the file from 3,103 to **4,843 words**.

I did not detect this by inspection — I detected it because my own clause census
returned **16** clauses for RFC-0010 on the first pass and **22** on a later
pass. I re-ran both regexes against the file to find my own bug, found none, and
then found the mtime. **Every count in this report is therefore stamped with
which snapshot it came from.** I have re-run all load-bearing measurements
against the post-edit state and report those as current.

The edit is **coherent as far as it goes** — front matter now reads
`clauses: "RFC10-1..RFC10-22"`, `verify_final_prespec.py` has been updated to
`REV10_ENDS = {10: 22, 11: 12}`, `05-CONTRACT-INDEX.yaml` has been regenerated
(+6 entries), and RFC10-16's own coverage matrix now spans `RFC10-1..RFC10-22`.
This is work in progress, not corruption. But one step has not been taken, and
it is the decisive one.

### 0.2 The manifest no longer describes the corpus — act 1 is not performable today

| Check | Pre-edit (≈17:45) | **Current (post-edit)** |
|---|---|---|
| `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` | **32/32 OK** | **31 OK, 1 FAILED** — `rfcs/RFC-0010-mission-control-autonomy.md` |
| `CG-7a` manifest digests valid | OK | **FAIL** — 32 entries examined, 1 finding |
| `CG-7c` acts 2/3/4 arguments | OK | **FAIL** — 1 finding |
| `CG-7d` act digests quoted anywhere | OK | **FAIL** — 2 findings |
| `check_governance.py` totals | 12 OK / 7 WARN / 3 FAIL | **9 OK / 7 WARN / 6 FAIL** over 22 checks |
| Corpus size | 99,094 w | **100,834 w** |
| `verify_final_prespec.py` | PASS | **PASS** (updated in the same edit) |
| `build_contract_index.py --check` | no drift | **no drift** |
| `build_dependency_index.py --check` | no drift | **no drift** |

`CG-7b` still reports OK — the act-1 argument
`f2914fc56cd2aa069b952747b9c78b00dc41d908830887ecd2f1addd37e61fc4` still matches
the *manifest file*. But the manifest no longer matches the *corpus*. **Uttering
the act-1 phrase today would bind a digest set that does not describe
RFC-0010**, which is precisely the failure mode the acceptance ceremony exists
to prevent. This is blocking and it is mechanical, not a matter of judgment.

**Second-order consequence:** RFC10-17 … RFC10-22 (~1,740 words) have been read
by **no reviewer in this round**, mine included — they did not exist when the
round's review battery ran, and they arrived after I had loaded RFC-0010. The
acceptance record already names as the round's **principal residual** that "no
fresh-context confirming review has been run over the current digests"
(`round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:188`). That residual has just
grown by a new §3.7.

### 0.3 What is mechanically sound

Setting the live edit aside, the package's machinery is in good order and I
could not break it: both index builders regenerate byte-identically, the package
verifier passes, clause numbering is contiguous everywhere (§2), there are no
dangling contract edges (§1.2), and **no contract cites a VIS-, SEC- or CC-
identifier that does not exist upstream** (0 findings over all 32 modules against
the 12 doctrine rules and 53 craft clauses; Python `re`).

All five in-scope index files carry correct derived/never-authority banners
(`05-CONTRACT-INDEX.yaml:1-2`, `CONTRACT-DEPENDENCY-INDEX.md:1`,
`TASK-TO-CONTRACT-INDEX.md:1`, `06-CONTEXT-LOAD-MAP.md:3`,
`ACTIVE-CONTRACT-MANIFEST.txt:1-2`).

**The 20-edge analysis in §1 is unaffected by the edit.** RFC-0010's
`depends_on` / `provides_to` were not changed; the dependency index still
reports exactly 20 asymmetries over the same 20 pairs, verified post-edit.

---

## 1. Dependency closure — all 20 asymmetric edges, exhaustively

### 1.0 Method and independent reproduction

`build_dependency_index.py --check` reports no drift. I did **not** take the
index's 20-edge list on trust: I re-parsed all 32 modules' front matter with an
independent Python reader and recomputed the graph. Results agree exactly:

- **11 contracts, 32 modules.**
- **61 distinct contract-level edges**: 41 symmetric (both halves declared) +
  **20 asymmetric**.
- **0 dangling IDs.** Every `depends_on` / `provides_to` value resolves to a
  contract that has at least one module in the package. Verified by set
  difference against the 11 declared `id` values — no `RFC-0012`, no typo, no
  reference to a retired or future contract.

One structural fact drives much of what follows: the generator **unions
module-level edges into a contract-level row** (`build_dependency_index.py`,
`collect()`), so a package README and its sibling modules may declare different
edges and the contract row shows their union. Several asymmetries are therefore
package-internal disagreements surfacing at contract level.

For each of the 20 I read **both** contracts involved — their clause bodies and
their prose `§Integration` "Relies on / Provides to" sections, which are the
authored statement of what each module actually consumes. I then cross-checked
against a mechanical citation census: for every ordered contract pair, how many
times the source's body text cites a clause of the target (Python `re`,
excluding front matter).

**Disposition rule applied consistently.** `depends_on: X` means *this
contract's clauses cannot be correctly implemented without loading X*.
`provides_to: Y` means *Y consumes something this contract defines*. These are
converse relations, so a correct graph is symmetric. An edge is genuinely
**one-way** only where the "provision" imposes no load obligation on the named
consumer — the consumer's own text discharges it without needing this
contract. I required demonstrable evidence for that, not assertion.

### 1.1 The 20-row disposition table

| From | To | Declared on | Disposition | Justification |
|---|---|---|---|---|
| `RFC-0002` | `RFC-0003` | `depends_on` | **ADD-MISSING-HALF** | Real. `rfcs/RFC-0002/snapshot-and-evaluation-core.md:237-239` — RFC3-16(a) gates RFC2-9's currency-bound declaration, and RFC3-16(b) item 9 supplies the audit-correlation identity snapshot input 11 binds. Root cause is a range error, not a missing dependency: `rfcs/RFC-0003/governance-homes-and-owner-acts.md:462` reads "**Provides to every downstream RFC, 0004–0011**", silently excluding RFC-0002, which does consume the predicate. Add `RFC-0002` to `RFC-0003.provides_to` (all 3 modules) and correct the prose range to `0002, 0004–0011`. |
| `RFC-0002` | `RFC-0004` | `depends_on` | **ADD-MISSING-HALF** | Real and load-bearing. `rfcs/RFC-0002/reconciliation-chain.md:181-182` and `:277` — RFC4-13 route 4 plus its governed-checker requirement RFC4-13(b) is *the* `gate-backed` route by which doc-only and governance-only work reaches `reconciled@E`. Without RFC-0004 that chain state is unreachable. Add `RFC-0002` to `RFC-0004.provides_to`; the owning module is `named-adapters.md`, which defines RFC4-13. |
| `RFC-0003` | `RFC-0006` | `provides_to` | **REMOVE** | Not real. The claim originates in a range shorthand at `rfcs/RFC-0003/manifests-and-namespace.md:549-551` — "**To RFCs 0006–0009:** the namespace authority classes for `intent/`, `work/`, `map/`" — which sweeps RFC-0006 in with the three surface RFCs. RFC-0006 governs none of them: the strings `.syzygy` and `namespace` occur **0 times** in `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` (Python sweep, whole file). Its only RFC-0003 citation is the universal status banner at `:19` (`RFC3-16`), boilerplate identical in `rfcs/RFC-0001-...:19`, whose `depends_on` is `[]`. RFC-0006's own §5 at `:439-451` names only RFC 0001 and RFC 0002, and `:463-464` disclaims URL spelling and wire formats. |
| `RFC-0004` | `RFC-0003` | `provides_to` | **ADD-MISSING-HALF** | Real. RFC-0003 substantively consumes RFC-0004 clauses: `rfcs/RFC-0003/governance-homes-and-owner-acts.md:304-306` enumerates RFC4-12, RFC4-13, RFC4-13(b), RFC4-16, RFC4-26, RFC4-7 and RFC4-23(2) as the artifacts honored under its own RFC3-16(a) predicate (12 body citations of RFC-0004 total). Add `RFC-0004` to `RFC-0003.depends_on`. |
| `RFC-0005` | `RFC-0002` | `depends_on` | **ADD-MISSING-HALF** | Real, and the converse half is already declared and symmetric. `rfcs/RFC-0005/admission-and-boundary.md:357-359` — RFC2-4's degradation-only rule, which RFC5-11 "reconciles against rather than excepts"; `rfcs/RFC-0005/execution-profiles.md:210-213` — RFC2-1 item 7, RFC2-24 #12, RFC2-23, RFC2-25. RFC-0002's `provides_to` lists 0003, 0004, 0006–0011 and omits only 0005. Add `RFC-0005` to `RFC-0002.provides_to`. |
| `RFC-0005` | `RFC-0003` | `provides_to` | **ADD-MISSING-HALF** | Real, and structurally load-bearing in the *reverse* direction of intuition: RFC-0003's own owner-act predicate depends on an RFC-0005 clause. `rfcs/RFC-0003/governance-homes-and-owner-acts.md:263` — RFC3-16(b) binding-set **item 9 is "the identity of the audit record (RFC5-25 or successor)"**, and `:267` binds RFC5-25's location constraint as what keeps item 9 unforgeable. Add `RFC-0005` to `RFC-0003.depends_on`. |
| `RFC-0005` | `RFC-0006` | `provides_to` | **REMOVE** | Not real. The claimed provision is "session semantics for URL/selection state" (`rfcs/RFC-0005/README.md:187-188`; `admission-and-boundary.md:369-370`). The string **`session` occurs 0 times** in `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` (Python sweep, whole file), and RFC-0006 cites **0** RFC5-n clauses. Nothing in RFC-0006 consumes this. |
| `RFC-0006` | `RFC-0005` | `provides_to` | **ACCEPT-AS-IS** | Genuinely one-way, and deliberately so. `rfcs/RFC-0006-...:453-455` states the provision as a *constraint*: "client class never changes an answer's fact set or labels, only whether the client is admitted (SEC-1)." RFC-0005 discharges that constraint directly from doctrine, not from RFC-0006: `rfcs/RFC-0005/admission-and-boundary.md:100-106` grounds RFC5-3 in SEC-1 explicitly and cites no RFC6-n clause anywhere. RFC-0006 in turn disclaims auth at `:463-464`. So RFC-0005's clauses are complete without loading RFC-0006 — no load obligation, hence no missing `depends_on`. **Caveat (finding 6):** RFC-0005 carries no clause acknowledging the constraint, so it is stated in only one contract and enforced in neither. |
| `RFC-0006` | `RFC-0011` | `provides_to` | **ADD-MISSING-HALF** | Real, and stated by the consumer itself. `rfcs/RFC-0011-context-compiler.md:261-262` lists in its own relies-on section: "**RFC 0006:** packet contents are queryable through the same semantic API with human/machine parity (RFC6-13/RFC6-14)." Add `RFC-0006` to `RFC-0011.depends_on`. |
| `RFC-0007` | `RFC-0004` | `depends_on` | **ADD-MISSING-HALF** | Real. `rfcs/RFC-0007/narrative-contract.md:550-552` — RFC4-10's verbatim-read and anchor obligations behind RFC7-14; RFC4-5's anti-duplication invariant behind RFC7-18 (6 body citations of RFC-0004). Add `RFC-0007` to `RFC-0004.provides_to`. |
| `RFC-0007` | `RFC-0005` | `depends_on` | **ADD-MISSING-HALF** | Real. `rfcs/RFC-0007/narrative-contract.md:552-554` — the RFC5-14/15 egress choke point behind RFC7-20's consent gate, and RFC5-25 act attribution behind RFC7-7. RFC-0005's prose says "RFC 0006 and **the surfaces**" (`README.md:187`) but its front matter enumerates only 0006 and 0008, dropping Polaris. Add `RFC-0007` to `RFC-0005.provides_to`. |
| `RFC-0007` | `RFC-0008` | `provides_to` | **ADD-MISSING-HALF** | Real, and the consumer cites it inside a normative clause. `rfcs/RFC-0008/identity-authority-materialization.md:204` — RFC8-9's own text reads "**Polaris renders that state read-only** (RFC7-24)"; `:290-292` lists "**RFC 0007:** Polaris rendering queue state read-only (RFC7-24)" in its relies-on block. Add `RFC-0007` to `RFC-0008.depends_on`. |
| `RFC-0007` | `RFC-0009` | `provides_to` | **ADD-MISSING-HALF** | Real, though for a different reason than the prose gives. The stated provision, RFC7-28's curated-versus-computed attribute (`rfcs/RFC-0007/README.md:212-215`), has **no consumer** — `curated` occurs 0 times in RFC-0009 and RFC7-28 is never cited there. The genuine link is the shared verdict protocol: `rfcs/RFC-0009/visual-grammar-and-lenses.md:528-529` — "*(This paragraph and RFC7-31 state one protocol, with the same outcome on both surfaces.)*". Add `RFC-0007` to `RFC-0009.depends_on`, and correct the provision named in RFC-0007's prose from RFC7-28 to RFC7-31. |
| `RFC-0008` | `RFC-0007` | `provides_to` | **ACCEPT-AS-IS** | Genuinely one-way. RFC-0007 cites **0** RFC8-n clauses across all three of its modules (Python `re` sweep) and its §5 lists no RFC 0008 reliance. The SDR-18 seam is stated independently and completely from Polaris's own side at `rfcs/RFC-0007/narrative-contract.md:433` (**RFC7-24 — The SDR-18 seam.**), so RFC-0007's text is self-standing; RFC8-9 asserts ownership *against* Polaris rather than handing Polaris something to load. **Caveat (finding 5):** one seam, two independent statements, no citation link in either direction — this is the package's own "stated once and cited" discipline not being applied, and it is a live drift risk. |
| `RFC-0008` | `RFC-0011` | `provides_to` | **ADD-MISSING-HALF** | Real, via a different clause than claimed. The prose claims RFC8-26/8-27 compaction preservation (`rfcs/RFC-0008/README.md:184-186`), which RFC-0011 never cites. But `rfcs/RFC-0011-context-compiler.md:90-91` binds RFC11-2 normatively into RFC-0008's records: "The packet digest is part of every resulting **Execution Record** (RFC8-18..RFC8-20)". Add `RFC-0008` to `RFC-0011.depends_on`. Note the module-level mismatch: RFC8-18..20 live in `state-vocabulary-and-cost.md`, whose `provides_to` omits RFC-0011. |
| `RFC-0009` | `RFC-0005` | `depends_on` | **ADD-MISSING-HALF** | Real. `rfcs/RFC-0009/visual-grammar-and-lenses.md:574-575` — "**RFC 0005:** execution profiles gating every runtime-lens input (RFC5-20…23; SEC-3)." A runtime lens cannot render without the SEC-3 gate. Add `RFC-0009` to `RFC-0005.provides_to`. |
| `RFC-0009` | `RFC-0007` | `provides_to` | **ADD-MISSING-HALF** | Real and explicit. `rfcs/RFC-0007/rendering-and-surface.md:368` — "with the shared release-policy leg **stated at RFC9-45, never duplicated here**"; also `:176-179`. RFC-0007 cannot be implemented without RFC9-45. Add `RFC-0009` to `RFC-0007.depends_on`. (Paired with row 13, this makes RFC-0007↔RFC-0009 a legitimate mutual edge.) |
| `RFC-0009` | `RFC-0008` | `provides_to` | **REMOVE** | Not real; the direction is inverted. All five RFC-0009 mentions in RFC-0008 name RFC9-32 as the **consumer** of RFC-0008's two-field handoff, never as a source: `rfcs/RFC-0008/README.md:149`, `state-vocabulary-and-cost.md:320`, `accounting-reconciliation-and-release.md:332`. The claimed provision, "map-side rendering obligations behind cross-surface highlights" (`rfcs/RFC-0009/visual-grammar-and-lenses.md:579-580`), has no consumer — "cross-surface highlight" occurs 0 times in RFC-0008. The true `RFC-0008 → RFC-0009` direction is already declared and symmetric, so nothing is lost. |
| `RFC-0009` | `RFC-0010` | `provides_to` | **REMOVE** | Not real. RFC-0010's only RFC9-n citation is `rfcs/RFC-0010-mission-control-autonomy.md:481` (`:328` pre-edit) — "(Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52.)" — a peer-shape note inside RFC10-16, which states its **own** phase rule (over RFC10-1..RFC10-22 as amended) and consumes nothing from RFC9-52. RFC-0010's §5 (`:519 ff.`) lists RFC 0001/0002/0003/0005/0006/0008/0011 and omits RFC 0009 entirely. Decisive internal proof: RFC7-38 is cited in the *same parenthetical on the same line*, yet RFC-0007 correctly does **not** declare `provides_to: RFC-0010`. The edge is an artifact of reading a shape-parallel citation as consumption. |
| `RFC-0009` | `RFC-0011` | `provides_to` | **REMOVE** | Not real, identical reasoning. `rfcs/RFC-0011-context-compiler.md:223-225` — "(Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16.)" inside RFC11-12, which states its own phase rule over RFC11-1..RFC11-12. RFC-0011's §5 at `:249-264` lists RFC 0001/0002, 0003, 0004, 0005, 0006, 0010 and omits RFC 0009. Same asymmetric treatment as row 19: RFC-0007 does not claim the edge on identical evidence. |

**Disposition tally:** ADD-MISSING-HALF **13** · REMOVE **5** · ACCEPT-AS-IS
**2** · REVERSE **0**. Total 20.

### 1.2 Dangling IDs

**None.** All `depends_on` / `provides_to` values across all 32 modules resolve
to one of the 11 declared contract ids. Verified by set difference in this
session. The generator has a `dangling` branch (`build_dependency_index.py`,
`asymmetries()`); it fired zero times, and the index's 20 rows are all
`depends_on` / `provides_to` disagreements, none of kind `dangling`.

### 1.3 Cycles

Computed over the **`depends_on`** graph (the load-obligation direction; the
`provides_to` view is not a build order and the index says so at
`CONTRACT-DEPENDENCY-INDEX.md:107-110`).

**As declared today — 4 mutual pairs, 8 distinct cycles, all inside the kernel
cluster {RFC-0002, RFC-0003, RFC-0004, RFC-0005}:**

| Cycle | Legitimate? |
|---|---|
| RFC-0002 ↔ RFC-0003 | **Yes.** RFC-0002 needs RFC3-16(a) to gate its currency-bound declaration (`snapshot-and-evaluation-core.md:237-239`); RFC-0003 needs RFC2-1 snapshot inputs and RFC2-6 kernel-fact immutability (`governance-homes-and-owner-acts.md:450-453`). A governance predicate and a temporal model defining each other's preconditions is a real mutual definition, not sloppiness. |
| RFC-0002 ↔ RFC-0004 | **Yes.** RFC-0002's `reconciled@E` needs RFC4-13 route 4 (`reconciliation-chain.md:181-182`); RFC-0004's evidence semantics need the RFC2-25 tier registry (`RFC-0004/README.md:139-141`). |
| RFC-0002 ↔ RFC-0005 | **Yes.** RFC-0002's Unknown reasons #6 and #12 need consent records and execution profiles (`rendering-vocabularies.md:208-210`); RFC-0005 needs RFC2-4's degradation-only rule (`admission-and-boundary.md:357-359`). |
| RFC-0004 ↔ RFC-0005 | **Yes, and explicitly bounded.** RFC-0004's gate provenance needs RFC5-21 profiled runs (`named-adapters.md:411-413`); RFC-0005's execution gate needs RFC4-13's `gate-backed` provenance predicate (`execution-profiles.md:217-220`). The modules draw the line themselves: "RFC5-19 governs **only** whether a profile is required" (`execution-profiles.md:218-219`), which stops the mutual reference becoming circular reasoning. |
| 4 longer cycles (3-node ×3, 4-node ×1) | Consequences of the four pairs above; no independent cycle exists. |

**After the 13 recommended repairs**, two further mutual pairs appear —
RFC-0007 ↔ RFC-0008 (the SDR-18 seam) and RFC-0007 ↔ RFC-0009 (the
RFC7-31/RFC9-45 verdict protocol). Both are legitimate surface seams where each
side owns one leg and cites the other's.

**No illegitimate cycle found.** The package's own statement — "the contract
graph is **not acyclic** — mutual edges between kernel contracts are declared
deliberately… Read it as a reference graph for context selection, not as a
build order" (`CONTRACT-DEPENDENCY-INDEX.md:107-110`) — is accurate. The cost
of the cycles is real but belongs to item 6, not here: they make the kernel
cluster's transitive closure 50.6% of the corpus.

### 1.4 Advisory — should `depends_on` be the single authored direction, with `provides_to` generated?

**Yes, with two named prerequisites.** I simulated the rule mechanically
(generate `provides_to` as the exact inverse of the declared `depends_on`) and
diffed against the declared `provides_to`:

- **6 edges newly created — all 6 correct.** RFC-0002→RFC-0005,
  RFC-0003→RFC-0002, RFC-0004→RFC-0002, RFC-0004→RFC-0007,
  RFC-0005→RFC-0007, RFC-0005→RFC-0009. These are exactly six of my
  ADD-MISSING-HALF rows, repaired for free. **Zero spurious edges created.**
- **14 edges lost.** Broken down:
  - **5 lost and good riddance** — precisely my REMOVE set
    (RFC-0003→RFC-0006, RFC-0005→RFC-0006, RFC-0009→RFC-0008,
    RFC-0009→RFC-0010, RFC-0009→RFC-0011). The rule deletes all five
    spurious edges automatically.
  - **7 lost that must not be** — RFC-0004→RFC-0003, RFC-0005→RFC-0003,
    RFC-0006→RFC-0011, RFC-0007→RFC-0008, RFC-0007→RFC-0009,
    RFC-0008→RFC-0011, RFC-0009→RFC-0007. These are real edges whose
    `depends_on` half is currently *unauthored*. **Prerequisite 1: author
    those 7 `depends_on` halves before switching, or the switch silently
    deletes seven true dependencies.**
  - **2 lost with no repair available** — **RFC-0006→RFC-0005** and
    **RFC-0008→RFC-0007**, my two ACCEPT-AS-IS rows. These are genuine
    one-way *constraints*: the named contract is bound by them but loads
    nothing. An inverse-of-`depends_on` rule **cannot express them** and
    will erase both. **Prerequisite 2: keep a separate authored field for
    them** — `constrains:` is the honest name, since `provides_to` would
    then mean two different things.

**Net recommendation.** Make `depends_on` the single authored load-obligation
direction and generate `provides_to` from it — the graph then becomes correct
and self-checking, and 18 of the 20 asymmetries stop being possible by
construction. But do it *after* authoring the 7 missing halves, and add a small
`constrains:` field for the 2 one-way constraint edges. Doing it without those
two steps trades 20 visible asymmetries for 9 invisible deletions, which is
strictly worse.

**One further caution.** `depends_on` values are **contract-granular**
(`RFC-0003`), while loading is **module-granular** (`rfcs/RFC-0003/
governance-homes-and-owner-acts.md`). Generating `provides_to` at contract
granularity preserves that mismatch; see finding 8.

---

## 2. Stable identity

### 2.1 Method

`grep` on this machine is ugrep and silently mismatches `[^]]`-style classes,
so **every sweep in this section was done in Python with the `re` module**, and
each universal claim was run as its own exact sweep in this session. My first
attempt used the regex `(RFC\d+-\d+(\([a-z]\))?)\b`, which **backtracks off the
sub-clause letter** (`\b` fails between `)` and a following space, so
`RFC1-18(a)` matched as `RFC1-18`) and produced 20 phantom duplicates. The
corrected anchor drops the trailing `\b`. I report this because the first
result was wrong and the second method is what the numbers below rest on.

Definition marker used (the package's own, with the sub-clause group fixed):
`^\*\*(RFC(\d+)-(\d+)(\([a-z]\))?)\s*(?:\.|—|-)`.

### 2.2 Counts

Both snapshots reported, because the live edit moved them.

| Quantity | Pre-edit | **Current** |
|---|---|---|
| Definition sites matched at line start | 343 | **349** |
| Distinct base (numbered) clause IDs defined | 322 | **328** |
| Distinct lettered sub-clause IDs defined | 21 | **21** |
| **Duplicate definition sites** | 0 | **0** |
| Clause entries in `05-CONTRACT-INDEX.yaml` | 344 | **350** (350 distinct, **0 duplicates**) |
| In index but not matched by the strict marker | 1 — `RFC9-16(d)` | **1 — `RFC9-16(d)`** |
| Defined but absent from the index | 0 | **0** |

The +6 in every column is RFC10-17 … RFC10-22. The index was regenerated in the
same edit, so index and corpus remain in agreement.

The single index/corpus difference is **not** a defect. `RFC9-16(d)` opens its
bold headline with running prose rather than a `.`/em-dash separator —
`rfcs/RFC-0009/semantic-geography.md:473`, "**RFC9-16(d) is owner-gated, with
one narrow carve-out**" — and `scripts/build_contract_index.py:14-29` documents
exactly this case and admits it under a deterministic `LETTERED_LIMB` rule.
With that rule applied, **index and corpus agree exactly in both directions**.

### 2.3 Gaps and renumbering

Base-number contiguity, per contract, checked against the frozen rev9/rev10
ends:

| Contract | Defined | Expected | Gaps | Above expected |
|---|---|---|---|---|
| RFC-0001 | 32 | 1..32 | none | none |
| RFC-0002 | 25 | 1..25 | none | none |
| RFC-0003 | 32 | 1..32 | none | none |
| RFC-0004 | 29 | 1..29 | none | none |
| RFC-0005 | 26 | 1..26 | none | none |
| RFC-0006 | 28 | 1..28 | none | none |
| RFC-0007 | 38 | 1..38 | none | none |
| RFC-0008 | 32 | 1..32 | none | none |
| RFC-0009 | 52 | 1..52 | none | none |
| RFC-0010 | **22** | 1..22 | none | none |
| RFC-0011 | 12 | 1..12 | none | none |

**328 = 32+25+32+29+26+28+38+32+52+22+12.** Zero gaps, zero duplicates, zero
IDs above the declared end, across all 11 contracts. The "no retirements, no
merges, no gaps" claims in the front matter are **true as stated** for base
numbering. This is the strongest part of the package.

Module-level ownership is equally clean, checked separately: **0 clauses defined
in more than one module**, **0 clauses defined inside a foreign contract's
module**, and every contract's module union equals its declared `1..N` exactly.

*(Transient note, for the record: mid-edit I observed RFC-0010 defining
RFC10-17…22 while its front matter still read `RFC10-1..RFC10-16` and RFC10-16's
coverage matrix still read `RFC10-1..RFC10-16`. Both have since been updated by
the editing session. I record it only because it shows the window during which
the corpus was internally inconsistent, and because nothing in the tooling would
have caught it — `verify_final_prespec.py` passed on both sides of that window,
against different `REV10_ENDS` constants.)*

### 2.4 Cross-module citations of IDs that do not exist

A full sweep of every `RFCn-m` and `RFCn-m(x)` token in all 32 module bodies
against the definition set returns **13 lettered tokens with no definition
site**. I checked each one against its parent clause body:

`RFC4-8(c)`, `RFC5-18(a)`, `RFC5-18(c)`, `RFC5-18(e)`, `RFC7-2(a)`,
`RFC7-9(a)`, `RFC8-2(a)`, `RFC8-8(a)`, `RFC9-10(c)`, `RFC9-16(a)`,
`RFC9-19(b)`, `RFC9-19(c)` — **all 12 are genuine in-clause enumerated limbs**,
i.e. `(a)`, `(b)`, `(c)` list items inside a numbered clause's own body, not
missing clauses. Verified individually: RFC9-19's three placement mechanisms
at `rfcs/RFC-0009/semantic-geography.md:589-594`; RFC9-10's three plane
obligations at `:352-355`; RFC7-2's three claim kinds at
`rfcs/RFC-0007/narrative-contract.md:80-85`; RFC7-9's three bound properties at
`:182-187`; RFC5-18's gate conjuncts at
`rfcs/RFC-0005/execution-profiles.md:81`; RFC4-8's skew limbs at
`rfcs/RFC-0004/general-contract.md:163`.

The 13th, `RFC9-16(d)`, is a defined clause (§2.2).

The corpus documents the limb convention in three places:
`rfcs/RFC-0009/semantic-geography.md:800` ("Lettered limbs (RFC9-10(c),
RFC9-19(b)) are parts"), `rfcs/RFC-0008/identity-authority-materialization.md:342`
("clauses (e.g. RFC8-2(a)–(c), RFC8-8(a)–(c)) are parts of those clauses — list
…"), and `rfcs/RFC-0005/README.md:7` ("no lettered sub-clauses — RFC5-18(a)–(e)
are list items inside RFC5-18").

**So: zero dangling clause citations.** But the convention is applied
inconsistently — see findings 3 and 4.

---

## 3. Contradictions

### 3.0 Method

All 32 modules, all 6 doctrine files, and all 9 craft policy files read in full.
Every count claim was checked by **manually counting the rows of the source
table**, not by trusting the prose: RFC2-24 = 12 rows; RFC2-25 = 6 tiers;
RFC6-5 = 9 outcomes; RFC1-22 = 6 planes; RFC1-25(b) = 4 senses → 4×3 = **12
ordered pairs** (arithmetic correct); RFC8-12 = 8 live + 1 terminal + 4 absence
= **13 values in 3 partitions** (correct). Vocabulary index citations
(`RFC2-24 #N`, `RFC2-1 item N`, `RFC3-16(b) item N`) were swept with Python `re`
and cross-checked with `grep -F`. Doctrine-conflict patterns were swept twice by
different methods to make the negatives genuine.

**A note on tooling, since it affected citation accuracy:** `grep -n` on this
machine returned *three different* line numbers for one RFC-0010 anchor during
the sweep — an artifact of the file being rewritten underneath it. Line numbers
below were re-derived with Python after the edit settled; the quoted text is the
stable anchor.

### 3.1 Real contradictions between two contract modules

**(1) `missing-declaration` is indexed as RFC2-24 #4 in one place and #1 in
another. #4 is a different reason.** *(Verified independently by me against both
sources.)*

- `rfcs/RFC-0002/rendering-vocabularies.md:113` — `| 1 | missing-declaration |
  No governing declaration (capability, topology, mapping, policy) exists |
  First-pass drafting for owner sign-off |`
- `rfcs/RFC-0002/rendering-vocabularies.md:116` — `| 4 |
  stale-beyond-currency-bound | Evidence exists but exceeds its declared bound
  at the as-of instant | Capture fresh evidence via a new snapshot |`
- `rfcs/RFC-0009/semantic-geography.md:271` (RFC9-9(b)) — "It renders the
  reserved Unknown treatment with reason `missing-declaration` (**RFC2-24 #4**)
  where the placement declaration is absent"
- The same module gets it right 335 lines later —
  `rfcs/RFC-0009/semantic-geography.md:606` (RFC9-20): "(Unknown reason
  `missing-declaration`, **RFC2-24 #1**, routing to the drafting affordance)"

**Why it bites rather than being a typo.** RFC6-14 requires machine answers to
carry the reason **verbatim**, and RFC6-22/23 make two renderings that disagree
**release-blocking**. An implementer keying off the index emits
`stale-beyond-currency-bound` — with resolution route "capture fresh evidence" —
for an entity that has no declaration at all. It is the wrong reason and the
wrong remedy, in a closed vocabulary. This is the **only** wrong index in the
corpus: the other 16 `RFC2-24 #N` citations all resolve correctly.
**One-character fix; blocking because it is a wrong value in a closed
vocabulary.**

**(2) RFC9-8(a) places an owner-gated, truth-bearing, snapshot-input registry
inside the artifact RFC3-10/11/21 close and classify as personal presentation
state.** *(Verified independently by me against all four clauses.)*

- `rfcs/RFC-0009/semantic-geography.md:136-146` (RFC9-8(a)) — the portfolio
  "carries the **same machinery at workspace scope**: a **portfolio layout
  version** and its registry, reorganisation events with recorded rationale, and
  the RFC9-16(d) owner gate, **all held in the workspace manifest's governed
  space (RFC3-21)**"
- `rfcs/RFC-0003/manifests-and-namespace.md:236-241` (RFC3-10) — the workspace
  manifest "is classified under **VIS-6, exception (a)** — personal presentation
  state: **it may never affect truth, work, status, or certificates, and it is
  never a snapshot input (RFC2-1)**."
- `rfcs/RFC-0003/manifests-and-namespace.md:245-250` (RFC3-11) — "Its field set
  is **closed at SDR-29's list**… **Additions require an amendment to this
  RFC.**"
- `rfcs/RFC-0003/manifests-and-namespace.md:341-346` (RFC3-21) —
  "`.syzygy/local/` **is personal presentation state** — VIS-6, exception (a)…
  It is **never truth-bearing, never a snapshot input**"

**Three separate incompatibilities, not one.** (i) RFC9-8(a) adds fields to a set
RFC3-11 declares closed, without the amendment RFC3-11 demands. (ii) A layout
version is a **snapshot input** (RFC2-1 item 7) and RFC9-18 requires registry
entries be honored **only under RFC3-16(a)** owner-act provenance — neither is
possible on a plane that "may never affect truth" and "is never a snapshot
input". (iii) The phrase "**the workspace manifest's governed space
(RFC3-21)**" is self-refuting: RFC3-21 *is* the non-governed personal plane.

**The package contains both the rejected construction and its rejection.**
`rfcs/RFC-0010-mission-control-autonomy.md:340-348` (RFC10-15) creates a typed,
platform-level **workspace governance store** "**distinct from the
presentation-only workspace manifest (which remains personal presentation state,
RFC 0003)**", whose authorizing entries are RFC3-16(a) artifacts — and RFC-0010's
alternatives section explicitly records "**Extending the workspace manifest into
portfolio governance — rejected: presentation state and typed authority must not
share one artifact**". RFC-0010 solves exactly this problem correctly;
RFC-0009 solves it incorrectly.

This is the one finding that **cannot be fixed by editing a sentence.** It spans
three contracts, it has a doctrine consequence (implementing RFC9-8(a) as
written violates VIS-6 exception (a)), and it needs an owner call on where
portfolio layout authority lives. RFC10-15's store is the obvious home.
**Blocking.**

### 3.2 Drift risks — one rule, several hand-maintained homes

These are currently *consistent*; the defect is that nothing keeps them so, and
in two cases they have **already** diverged.

**(3) RFC9-24 calls four things "sibling states" citing RFC2-25, whose set is
closed at three — and omits the one RFC2-25 actually mints.**
`rfcs/RFC-0002/rendering-vocabularies.md:163-164` — "*Deliberately outside the
registry — **three** sibling surface states, closed:* `dismissed-by-decision`,
`unadopted-draft` and `editorial-draft`." vs
`rfcs/RFC-0009/visual-grammar-and-lenses.md:62-71` (RFC9-24) — "the rest are
**sibling states**… (**RFC2-25**): **Contradicted**…; **Dismissed by
decision**…; **Proposed/speculative**…; **Unadopted draft**…". `Contradicted` is
the `suspended` *tier*, not a sibling state; `Proposed/speculative` is a state
plane (RFC1-22); and `editorial-draft` — the one RFC2-25 mints by owner decision
B10 — **gets no reserved map treatment at all**, while RFC9-43 and RFC9-46
require per-sibling-state counts everywhere. **Already drifted.**

**(4) The aggregation-disclosure enumeration is claimed single-sourced and exists
in five places, three of which assert they are not restating it.** Owner:
`rfcs/RFC-0006-...:233-243` (RFC6-17). Copies:
`rfcs/RFC-0002/rendering-vocabularies.md:138-143` ("The obligation is cited here,
not restated, so the two cannot drift" — in the same sentence that restates it);
`rfcs/RFC-0003/manifests-and-namespace.md:473-477` ("cited here, never
restated"); `rfcs/RFC-0007/rendering-and-surface.md:296-298` ("cited, never
restated here"); `rfcs/RFC-0009/visual-grammar-and-lenses.md:394-402` (the
longest copy, spelling out all six tier names). **Five hand-maintained copies of
a vocabulary whose entire purpose is not to drift, three carrying a false
self-description.** This is the failure RFC9-47(a) was written to prevent,
occurring one layer above it.

**(5) RFC9-43 defines its obligation as "the full RFC9-46 equivalence tuple" then
enumerates a strict subset.** `rfcs/RFC-0009/visual-grammar-and-lenses.md:396`
vs `rfcs/RFC-0009/interaction-parity-and-release.md:62-78`, where RFC9-46's tuple
*additionally* carries the RFC9-9(b) positional-expression state, both RFC9-15(b)
part-4 partition counts, and both work-state fields. An implementation
satisfying RFC9-43's enumeration violates RFC9-43's own first sentence. RFC9-46
flags the mechanism itself (`:96-104`: "a **hand-maintained enumeration**… an
omission does not fail loudly anywhere") — and the omission has already
happened, in the clause that consumes it. **Already drifted.**

**(6) The same defect shape at the foundation layer.**
`rfcs/RFC-0006-...:236` — "**The disclosed composition is the full RFC6-22
equivalence tuple**" — where RFC6-22 at `:310-316` is wider (it adds the same
underlying graph and the same scenario context). Defensible as *composition of an
aggregate ≠ whole tuple*, but the identity claim is literally false, and it is
the sentence RFC9-43 copied.

**(7) RFC5-25's location constraint has two binding homes.** *(My own finding.)*
Stated in full at `rfcs/RFC-0005/admission-and-boundary.md:302-306` ("**Where the
trail lives — a normative constraint, not a schema choice.** The audit trail
lives **outside `.syzygy/**` and outside the untrusted actor class's write
reach**"), and restated at binding strength at
`rfcs/RFC-0003/governance-homes-and-owner-acts.md:263-267` as item 9 of
RFC3-16(b). Currently identical in substance. The knot is mutual — RFC5-25 cites
RFC3-16(a) for the extension, and RFC3-16(b) item 9 cites RFC5-25 back — so
neither can be designated the single home without care. Non-blocking, but it is
the same disease as (4).

**(8) RFC9-14(a) sources the layout *baseline* to RFC2-1 item 7, which names
layout *versions* only.** `rfcs/RFC-0009/semantic-geography.md:436` vs
`rfcs/RFC-0002/snapshot-and-evaluation-core.md:86-88`. Satisfiable — RFC2-1's
list is a stated minimum and the baseline is reachable through item 2 — but the
citation does not carry what it is cited for. Minor.

### 3.3 Contradictions against adopted doctrine

**None found, stated plainly rather than padded.** Two-method sweeps for the
specific hazards returned genuine zeroes: no clause permits a default, zero, or
green in the absence of evidence (VIS-2); none lets an agent or renderer decide a
governance question (VIS-4 — and RFC1-25(c) and RFC9-20 go out of their way to
forbid it); no module claims a third exception to VIS-6's two; no clause permits
nondeterministic output (VIS-7). Finding (2) above is a *contract-vs-contract*
conflict whose **consequence** would be a VIS-6(a) violation if RFC9-8(a) were
implemented as written — but no clause contradicts the doctrine text directly.

### 3.4 Contradictions against owner-approved craft policy

**None found.** The one live suspect — RFC9-10(c)'s parenthetical "**CC-VIZ-5 is
amended to match**" — checks out on inspection of the upstream policy:
`policies/craft-and-care/performance-and-visual-discipline.md:112-114` already
carries the superseding wording, and
`policies/craft-and-care/INSTALL-RECORD.md:9-12` records it as owner amendment
**B21**. CC-VIZ-5's three-input layout tuple matches RFC9-14 exactly, including
the post-review-8 baseline correction. Separately, **no contract cites a CC-
identifier that does not exist** (0 findings over 53 CC clauses).

### 3.5 Near-misses examined and cleared

Reported so the negatives are legible as work done, not as absence of looking:

- **RFC3-15's "five constitutional categories" vs `doctrine/architecture.md:60`'s
  "four".** Doctrine says "constitutional **minimums**", which licenses
  widening, and RFC3-15(a) records both widenings (owner decision B19 minting
  `records/`; RFC3-17 reserving `declarations/`). **Not a contradiction.**
- **RFC9-9's "three classes of intra-project dependency edge" vs RFC1-25(b)'s
  four senses.** The fourth is Project→Project, i.e. cross-project; RFC9-9 is
  explicitly intra-project scoped. **Scoping, not disagreement.**
- **RFC8-12's four absence values vs RFC2-24's closed twelve Unknown reasons.**
  Held apart deliberately in three places (RFC8-12, RFC8-24, RFC6-6): absence
  values "take no reason from this list, and are counted separately". **Clean.**
- **RFC9-45's `verdict-unlawful`** — self-declared as "**not** an RFC2-24 Unknown
  reason (that vocabulary is closed at twelve)". Closure preserved by
  construction.
- **RFC5-11/B4 forced evaluation vs RFC2-4 degradation-only; RFC2-13's "two
  senses of deterministic" vs VIS-7; RFC7-8's "VIS-6 is satisfied without an
  exception"; RFC4-13 routes 3/4 vs CC-TEST-2's routes-1–2 scoping.** Each is
  pre-reconciled in the text, with the reconciliation stated.
- **The declared front-matter cycles** (RFC-0002↔0003/0004/0005, RFC-0004↔0005).
  Genuine mutual definitions; see §1.3. **Not contradictions.**
- **The six phase-rule ranges** (RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16,
  RFC11-12): each names `RFCn-1 … RFCn-(last−1)`, correctly excluding itself,
  and RFC-0009's README restatement agrees. **Clean** — including RFC10-16 after
  the live edit, which now correctly spans `RFC10-1..RFC10-22`.

---

## 4. Normative / informative boundary

### 4.0 Method and headline

A full-corpus segmenter classified every line as clause text (from any
`^\*\*RFC\d+-\d+` opener to the next heading or `---`) or prose: **5,615 prose
lines / 6,201 clause lines**, **351** line-start clause openers. An
obligation-language sweep over the prose partition (`MUST`, `shall`, `may
never`, `is required`, `is prohibited`, `never`, `always`) returned ~360 hits,
triaged by hand. All sweeps used Python `re` on whitespace-normalized whole-file
text — this mattered: at least one load-bearing phrase is wrapped across lines
and is invisible to any line-based grep. I independently re-verified every
finding quoted below against the source files.

**The convention is real and mostly honoured.** Nearly all ~360 prose obligation
hits are Integration or reader-map sentences that restate a clause and cite it
by identifier, inside a file carrying an explicit precedence disclaimer. That is
the declared convention working, and flagging it wholesale would be padding. The
exemplar of correct hygiene is `rfcs/RFC-0003/README.md:24-26`: "This index is
**navigational and non-normative**. It duplicates no clause… where this file and
a clause disagree, the clause wins."

**The boundary leaks in one systematic way: package `README.md` §5 "Integration"
and §7 "Deliberately deferred" sections are being used as a clause home.**

### 4.1 Binding rules that exist only in rationale (the serious category)

**(a) The two-field conformance rule is homed in a README, and a numbered clause
cites the README as its authority.** `rfcs/RFC-0008/README.md:163-168`:

> "Stated as **two fields** rather than a value count on purpose… **a consumer
> conforms by consuming both fields and rendering every value each field
> currently carries**, so an addition to either vocabulary crosses the seam
> without amending this paragraph, and a value the consumer cannot render is a
> defect in the consumer, never a licence to fold it into a neighbour."

Two modules explicitly designate the README as the rule's only home —
`rfcs/RFC-0008/state-vocabulary-and-cost.md:322-323` ("the **conformance rule
binding both halves** is stated once, in `README.md` §5") and
`rfcs/RFC-0008/accounting-reconciliation-and-release.md:335-336`. And RFC9-32
cites it as authority twice: `rfcs/RFC-0009/visual-grammar-and-lenses.md:210`
("orthogonal fields, not one** (RFC8-12; RFC8-28; **RFC 0008 §5**)") and `:239`
("never grounds to fold that value into a neighbouring one (**RFC 0008 §5**)").
**A binding clause whose citation chain terminates in a section the package
itself declares navigational is a circular-authority defect.** Partly mitigated:
RFC8-12 and RFC8-28 carry a clause-borne core — but RFC8-12 itself defers to
"(§5)", and the growth-resilience half of the rule has no clause home at all.
*Fix: promote the paragraph to an RFC-0008 clause; repoint RFC9-32, RFC8-12 and
both module cross-references at it.*

**(b) A general prohibition whose own parenthetical concedes no clause carries
it.** `rfcs/RFC-0002/README.md:200-209`, §7: "**no surface renders a composite
maturity number** (RFC7-16 binds Polaris to that; **the prohibition is
general**)." A whole-corpus sweep for `composite maturity` returns 6 lines in 3
files; none states a general all-surfaces prohibition inside a clause.
`rfcs/RFC-0007/narrative-contract.md:331-333` confirms the clause's true reach:
"Until then **Polaris** renders no composite number." *Fix: write the general
clause, or narrow the README sentence to RFC7-16's actual Polaris scope.*

**(c) A layout obligation invented in a "Deliberately deferred" section.**
`rfcs/RFC-0008/README.md:213-218`: queue and board presentation defers to craft
"**with one obligation that does not defer**: … any such layout **must place the
terminal and absence values off the ladder, not at the end of it**." The
section's own framing admits it is normative text in an informative section.
Sweep for `progress ladder|off the ladder` across all 32 files: **2 lines, both
inside this passage**. RFC8-12 supplies the partition but says nothing about
column ordering.

**(d) An operability gate stated only in unlabelled Motivation prose, in a file
with no precedence disclaimer.** `rfcs/RFC-0010-mission-control-autonomy.md:60-67`:
"…until the owner rules on it, this contract's reading of human-triggered
propagation stands only as far as doctrine already permits — which means
missions can be *specified* under this contract but **cannot lawfully
*operate*** under unamended doctrine's **one-pass trigger**." Sweep for
`one-pass trigger`: **1 hit, this line, corpus-wide.** This is arguably the
highest-stakes sentence in the package — it gates whether anything RFC-0010
specifies may run, and couples RFC-0010's operability to act 5, which the
acceptance record marks *optional*. It sits in §2 Motivation, which carries no
`(non-normative)` label, in one of the only two files with no clause-precedence
disclaimer. A reader obeying the stated convention reads it as background.

**(e) The "forward references are informative" meta-rule exists in 2 of 32
files.** `rfcs/RFC-0001-...:778` and `rfcs/RFC-0002/README.md:166` only. This is
a rule *about how to read clause bodies* — it downgrades the binding force of
forward citations — yet 30 of 32 files carry no equivalent. Either it is
package-wide and under-stated, or forward references in the other nine RFCs are
binding and the asymmetry is undocumented. Both readings survive the current
text; the ambiguity is the defect. This directly affects item 1: my
ACCEPT-AS-IS dispositions turn on which reading holds.

**(f) A cross-package non-weakening rule with no clause anchor.**
`rfcs/RFC-0006-...:483-485` — "none may weaken the semantics here" — where
RFC-0009 states the same idea twice and anchors it to a clause both times
(`interaction-parity-and-release.md:340` and `visual-grammar-and-lenses.md:594`,
both "none may weaken a clause here **(RFC9-2)**"). The package knows the right
pattern and applies it inconsistently.

### 4.2 Rationale prose reading as binding

Structural rather than lexical. `rfcs/RFC-0009/README.md:109-138`
("## Package-level integration") carries no `(non-normative)` label and contains
the **only two README lines in the entire package matching the numbered-clause
opener pattern** (`^\*\*RFC\d+-\d+`; 351 openers corpus-wide, exactly 2 of them
in a README): `:122` "**RFC3-16(a) gates four artifacts across two modules:**…"
and `:134` "**RFC9-52 binds the package, not one module.**". Typographically
indistinguishable from clauses.

### 4.3 Clause text that is actually rationale

**(a) A tie-break rule carried only by an `[Inferred]` bracket, yet cited
downstream.** `rfcs/RFC-0009/semantic-geography.md:195-199`, inside RFC9-9:
"[Inferred] The two readings are ordered: where containment and relatedness
compete for the same position, **containment wins**…". Sweep for `containment
wins`: 2 hits — this one and `:522`, which *relies* on it ("because containment
wins (RFC9-9)"). A downstream clause cites RFC9-9 for a rule that exists in
RFC9-9 only inside an epistemic bracket. *Fix: make the tie-break an unbracketed
limb.*

**(b) Cross-module gate scope carried by an `[Inferred]` bracket.**
`rfcs/RFC-0009/interaction-parity-and-release.md:225-229` — RFC9-47(a)'s
cross-module reach arrives inside `[Inferred — …]`; its only restatement is the
clause-shaped README text of §4.2. **Neither carrier is unbracketed clause
text.**

**(c) Rationale issuing an imperative inside the package's most-cited
predicate.** `rfcs/RFC-0003/governance-homes-and-owner-acts.md:165-171`, inside
RFC3-16(a): "[Inferred] The fourth limb is deliberately the vaguest… **treat
that as a finding, not as settled coverage.**" Either a rule (promote it) or
advice (drop the imperative). Also `rfcs/RFC-0002/challenge-lifecycle.md:159-169`
— a ten-line justification paragraph mid-clause, correctly labelled but
separating RFC2-13's limbs.

### 4.4 Mixed parentheticals

**54** strict italic parentheticals inside clause bodies; **14** carry
obligation language.

**(a) A parenthetical that reports an amendment to owner-approved craft policy.**
`rfcs/RFC-0009/semantic-geography.md:352-362`, inside RFC9-10(c): "…the
*interaction cost* of returning is not bound here (**the owner granted this
relaxation at acceptance, decision B21**… — CC-VIZ-5 is amended to match)".
Sweep for `CC-VIZ-5` across the corpus: **1 hit, this line**.

**I checked this against the upstream policy before judging it, and it is
weaker than it looks.** The amendment is a real, owner-authorized act already
performed and recorded: `policies/craft-and-care/INSTALL-RECORD.md:9-12`
("Amendment **B21** (relaxing SDR-21's 'one action back to home' to RFC9-10(c)'s
availability wording) is applied in `performance-and-visual-discipline.md`
(CC-VIZ-5) with its supersession note in place"), and
`policies/craft-and-care/performance-and-visual-discipline.md:112-114` carries
the superseding text. **So this is not a candidate contract unilaterally
amending approved policy** — it is a *report* of decision B21 in a citable
record that does exist. The residual defect is only that the report lives in a
parenthesis inside an unrelated sub-limb, discoverable nowhere else in the
corpus. **Non-blocking.**

**(b) An applicability precondition italicised into commentary.**
`rfcs/RFC-0009/semantic-geography.md:594`, inside RFC9-19: "*(Mechanism (c) is
available only where a **determinate** declared home exists…)*". "Available only
where" is a precondition on the clause's own mechanism.

**(c) Release-gate package scope stated in italic asides, in both multi-module
packages.** `rfcs/RFC-0007/rendering-and-surface.md:321-323` and
`rfcs/RFC-0009/interaction-parity-and-release.md:298-300`. The *scope* of a
release-blocking obligation is the most consequential attribute a gate has.

The remaining ~11 obligation-bearing parentheticals are short owner-decision
attributions and are commentary, not defects.

*Completeness caveat, stated honestly:* the 54/14 counts are a **floor**. The
RFC9-10 parenthetical — the most serious in this category — has nested
parentheses and escaped two regex passes; it was recovered only by slicing the
clause text directly. This category should be re-run with a paren-balancing
parser before anyone calls it exhausted. Categories 4.1–4.3 and 4.5 rest on
whole-file sweeps plus a complete read of all 32 files.

### 4.5 Disclaimer consistency — exact census

**30 of 32 files carry a clause-precedence disclaimer. 2 do not:**
`rfcs/RFC-0010-mission-control-autonomy.md` and
`rfcs/RFC-0011-context-compiler.md` — the package's only two single-file
contracts of the rev10 additions. Both label §0 "Reader's summary
(non-normative)" but leave **§1 Summary and §2 Motivation unlabelled**.

The coincidence is not benign: **finding 4.1(d) — RFC-0010's operability gate —
sits in unlabelled §2 of the file with no precedence rule.** The two gaps
compound. RFC-0011's gap is latent; I found no equivalent buried obligation in
it.

### 4.6 The one structural fix

A single mechanical rule would catch four of the six §4.1 items and the §4.2
item: **no `README.md` §5 or §7 sentence may state an obligation no clause
states, and no clause may cite a README section as authority.** Both patterns
are already regular enough to sweep in one pass — the clause-opener regex found
the 2 misplaced README lines out of 351 openers, and `RFC 0008 §5` is a literal.

---

## 5. Selective loadability — three concrete tasks

I state each task, route it through `06-CONTEXT-LOAD-MAP.md` and
`TASK-TO-CONTRACT-INDEX.md` exactly as a worker would, then check what the task
actually needs against the modules' own declared reliance. All word figures are
`scripts/context_load.py` output re-run in this session; token estimates use the
package's own ×1.35 heuristic.

**First, the routing instruments work.** `05-CONTRACT-INDEX.yaml` maps clause →
module for all 344 clause IDs with no duplicates, so a cited `RFCn-m` resolves
to exactly one module without search. All 7 package READMEs carry the
deterministic clause-lookup rule (verified: `lookup` present in each of the 7);
the 4 single-file RFCs need none. That claim at `06-CONTEXT-LOAD-MAP.md:50-51`
holds.

### Task A — "Add reason #13 to the closed Unknown-reason vocabulary (RFC2-24)."

- **Route.** `05-CONTRACT-INDEX.yaml` → `rfcs/RFC-0002/rendering-vocabularies.md`.
  Neither index has a task class for *amend a closed kernel vocabulary*; the
  nearest is the **Kernel implementer** row.
- **Answer given:** `06-CONTEXT-LOAD-MAP.md:38-39` — RFC-0001 + RFC-0002
  (core, challenge, reconciliation) + RFC-0003 governance-homes =
  **19,439 w ≈ 26,242 tok** (re-measured, matches
  `TASK-TO-CONTRACT-INDEX.md:43` exactly).
- **Determinate?** No. **The row omits `rendering-vocabularies.md` — the very
  module that owns RFC2-24.** The Kernel implementer row names three of
  RFC-0002's four normative modules and drops the fourth, which holds the
  Unknown-reason vocabulary *and* the rendering-tier registry. A worker
  following the reader map would not load the file they must edit.
- **What it also omits.** `rendering-vocabularies.md`'s own `provides_to`
  names 8 downstream contracts, and `:217-220` binds "the label+tier+reason
  triple **every surface renders verbatim**". Adding a reason therefore
  obliges RFC-0003, 0004, 0006, 0007, 0008, 0009, 0010 and 0011. An honest
  packet covering the owning module plus one consuming module per affected
  contract measures **39,780 w ≈ 53,703 tok** — 40% of the corpus, ~2.7× the
  15–20k working target.
- **Verdict:** not determinate, and the answer that is given is wrong.

### Task B — "Decide how Orrery renders a topology entry carrying two adopted `placed_in` edges."

- **Route.** `TASK-TO-CONTRACT-INDEX.md:46`, **Surface implementer — Orrery**.
- **Answer given:** RFC-0009 package (4 files) + RFC-0002 rendering + RFC-0006
  = **24,166 w ≈ 32,624 tok** (re-measured, matches exactly).
- **Determinate?** Yes, but wrong in both directions. It is **63% over** the
  20,000-token decomposition trigger — the index says so itself at
  `TASK-TO-CONTRACT-INDEX.md:103-109` (finding T-3) — *and* it omits the
  clause that decides the question. **RFC1-25(c)** is the governing rule:
  "`placed_in` is **not functional**… Two or more adopted `placed_in` edges
  from one entry are therefore a **declared placement contradiction**… **A
  surface that picks a home among competing `placed_in` edges by any rule
  whatsoever has given a governance answer**" —
  `rfcs/RFC-0001-project-graph-identity-state-planes.md:533-549`. RFC-0001 is
  not in the row.
- **The general form of the defect:** `06-CONTEXT-LOAD-MAP.md:40-41` reads
  "Surface implementer (any): owning surface package + RFC-0002 rendering +
  RFC-0006." **No surface row loads the kernel at all** — yet RFC-0009 cites
  RFC-0001 **60** times, RFC-0008 **58** times and RFC-0007 **37** times
  (Python census, body text only). Adding RFC-0001 takes this task to
  **32,519 w ≈ 43,900 tok**.
- **Verdict:** determinate, small-ish, and materially incomplete.

### Task C — "Amend the execution gate RFC5-18 to add a new isolation class."

- **Route.** `TASK-TO-CONTRACT-INDEX.md:48`, **Security / execution-profile
  work**; and `fixtures/context-selection-4-execution-profile.md`, the
  authoritative worked example for this exact task.
- **Answers given — two, and they disagree.** The reader-map row measures
  **7,968 w ≈ 10,756 tok**; fixture 4 measures **10,893 w ≈ 14,705 tok**
  (both re-measured, both match their sources). The 2,925-word gap is the two
  package READMEs the fixture adds. The index discloses the distinction
  honestly at `TASK-TO-CONTRACT-INDEX.md:52-59` ("A reader-map row is a
  role's orientation, not a task packet"), so this is a documented, not
  hidden, divergence.
- **Determinate?** Via the fixture, yes — and **fixture 4 is genuinely good
  work**: it traces the selection rule to RFC11-4, enumerates omitted
  applicable candidates *with reasons*, states why no applicable constraint
  was lost, separates mandatory from suggested-inferred additions, and carries
  a packet digest.
- **Does it omit anything the task needs?** The reader-map row does. The
  module's own §5 at `rfcs/RFC-0005/execution-profiles.md:208-226` declares
  reliance on RFC5-11/24/25 (module 1), RFC5-12/13/16 (module 2), RFC4-13,
  and RFC2-1/2-23/2-24/2-25 — **none of which the 7,968-word row carries**.
  Fixture 4 catches two of these and lists them as "suggested inferred
  additions" (`fixtures/context-selection-4-execution-profile.md`, §Suggested)
  rather than mandatory. A closure honoring the module's own declared reliance
  is **20,044 w ≈ 27,059 tok**.
- **Verdict:** the fixture answer is determinate and small; the reader-map
  answer is smaller and under-scoped. Neither is derived from the graph.

### Cross-cutting observation

Across all three tasks the pattern is identical: **selection is hand-authored,
never computed.** `context_load.py` only measures a list a human supplies; no
tool takes a task or a clause and returns its closure. The task index says this
itself — finding **T-1**, `TASK-TO-CONTRACT-INDEX.md:90-96`: the charter §11.5
`task_classes` / `risk_classes` metadata "**does not exist on any of the 32
modules**", so the index "cannot be generated and cannot be drift-checked the
way `05-CONTRACT-INDEX.yaml` and `CONTRACT-DEPENDENCY-INDEX.md` can." That is
an accurate self-assessment and it is the root of every routing gap above.

---

## 6. Size — does modularization actually deliver selective loading?

**Corpus: 100,834 words across 32 modules** (current, post-edit; 99,094 before
the RFC-0010 addition). Mean normative module ~3,700 words; largest
`rfcs/RFC-0009/semantic-geography.md` at 6,999; `rfcs/RFC-0001-...` at 8,353
over the 7,000 ceiling with a recorded justification the verifier accepts. The
brief's "~99,000 words" is now low by 1,740.

**The evidence cuts both ways, and the honest answer is "yes in practice, no by
the declared graph."**

**Against — the declared dependency graph mandates near-total loads.** I
computed the transitive `depends_on` closure per contract (post-repair, so this
is the *corrected* graph, not a strawman):

| Contract | Own words | Closure size | Closure words | % of corpus |
|---|---|---|---|---|
| RFC-0001 | 8,353 | 1 | 8,353 | **8.3%** |
| RFC-0002 / 0003 / 0004 / 0005 | 10,158–10,887 | 5 | 50,152 | **49.7%** |
| RFC-0006 | 4,174 | 6 | 54,326 | **53.9%** |
| RFC-0007 / 0008 / 0009 | 10,636–17,595 | 9 | 93,727 | **93.0%** |
| RFC-0010 | 4,843 | 10 | 98,570 | **97.8%** |
| RFC-0011 | 2,264 | 11 | 100,834 | **100.0%** |

Taken literally, `depends_on` says: to work on any surface contract, load 95%
of the corpus; to work on the context compiler, load all of it. The four-node
kernel cycle {0002,0003,0004,0005} means no kernel contract is ever readable
alone. **Only RFC-0001 is genuinely self-contained** — and it is the one
module that declares `depends_on: []` and explicitly makes all its forward
references informative (`rfcs/RFC-0001-...:778-786`).

**For — the fixtures demonstrate real selective loading anyway.** The five
accepted fixtures measure 10,893–18,315 words (11–18% of the corpus), and I
re-measured all five plus all eight reader-map rows: **every figure in
`TASK-TO-CONTRACT-INDEX.md` reproduces exactly** except the two noted in
finding 7. Median fixture load is ~13,900 words. That is a genuine, verified,
order-of-magnitude improvement over rev9's whole-corpus baseline.

**Why both are true.** The closure is near-total because `depends_on` is
declared at **contract** granularity while loading happens at **module**
granularity. RFC-0011 declares `depends_on: RFC-0009`-worth of relationships
that in reality reach one or two clauses of one module. The fixtures achieve
small packets by working at **clause** granularity — pulling RFC5-18(c) and
RFC3-16(b) rather than "RFC-0003" — and relying on the "stated once and cited"
discipline plus the clause-lookup index. That works, and it is the right
technique. But it is invisible to the graph, unverifiable by any tool, and
reproducible only by a human repeating the fixture author's judgment.

**Judgment.** Modularization delivers selective loading **as a hand-crafted
artifact, not as a property of the corpus.** The 32-module split plus the
clause index is a real and substantial improvement; the dependency graph
contributes nothing to it and, read as written, contradicts it. The corpus is
not too large *given* the fixtures; it is too interdependent *given* the graph.
Making `depends_on` module-granular (§1.4, finding 15) is what would close the
gap — and it is the single change that would make a 100k-word corpus defensible
on its own terms rather than on its fixtures'.

---

## Verdict

The substance of these contracts is strong, and I want that on the record before
the findings: **328 clauses across 11 contracts with zero duplicates, zero gaps,
zero renumbering, zero dangling clause citations, zero dangling contract edges,
zero dangling doctrine/craft citations, no contradiction against adopted
doctrine, and no contradiction against owner-approved craft policy.** Both index
builders regenerate byte-identically. The fixtures are honest, reason about
their own omissions, and carry digests. I tried to break the identity scheme and
could not.

But the artifact offered for acceptance is not the artifact on disk. The
manifest no longer describes the corpus, so the act-1 argument binds a digest
set that is wrong about RFC-0010; six new clauses have been read by no reviewer;
one cross-contract contradiction needs an owner ruling rather than an edit; and
18 of the 20 declared graph asymmetries are genuine errors rather than the
"reported, not repaired" one-way edges the index presents them as. None of that
is fatal, and most of it is bounded and mechanical — but "accept with noted
exceptions" is not available when the ceremony's own digest check fails.

VERDICT: REVISE

### Findings

1. **[Blocking] The manifest does not describe the corpus; act 1 is not
   performable.** `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt` → 31 OK, **1
   FAILED** (`rfcs/RFC-0010-mission-control-autonomy.md`, edited
   2026-08-05 18:04:52 during this review). `CG-7a`, `CG-7c` and `CG-7d` now
   FAIL; repo totals moved from 12 OK/7 WARN/3 FAIL to **9 OK/7 WARN/6 FAIL**.
   *Fix:* let the in-flight edit settle, regenerate
   `ACTIVE-CONTRACT-MANIFEST.txt`, recompute the act-1 argument, update every
   quoted copy of it, and re-run `check_governance.py` until CG-7a–d are OK.

2. **[Blocking] RFC10-17 … RFC10-22 (~1,740 words, new §3.7 "The correction
   plane") have been reviewed by nobody.** They postdate the round's review
   battery and postdate my own load of RFC-0010. The acceptance record already
   names "no fresh-context confirming review over the current digests" as the
   round's principal residual (`round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:188`);
   that residual has just grown.
   *Fix:* one fresh-context review scoped to RFC-0010 §3.7 before act 1.

3. **[Blocking] RFC9-8(a) puts an owner-gated, snapshot-input, truth-bearing
   registry inside an artifact three RFC-0003 clauses close and classify as
   personal presentation state.** `rfcs/RFC-0009/semantic-geography.md:136-146`
   vs `rfcs/RFC-0003/manifests-and-namespace.md:236-241`, `:245-250`, `:341-346`.
   Implementing it as written violates VIS-6 exception (a). RFC-0010 rejects
   this exact move and builds the correct alternative at RFC10-15
   (`rfcs/RFC-0010-mission-control-autonomy.md:340-348`).
   *Fix:* owner ruling — move the portfolio layout version, registry and
   RFC9-16(d) gate into RFC10-15's typed workspace governance store; or amend
   RFC3-11's closed field set explicitly. Not an editorial fix.

4. **[Blocking] Wrong index into a closed vocabulary.**
   `rfcs/RFC-0009/semantic-geography.md:271` cites `missing-declaration` as
   "RFC2-24 **#4**"; RFC2-24 #4 is `stale-beyond-currency-bound`
   (`rfcs/RFC-0002/rendering-vocabularies.md:113,116`). RFC6-14 requires the
   reason emitted verbatim; RFC6-22/23 make disagreement release-blocking.
   *Fix:* `#4` → `#1`. One character.

5. **[Blocking] A binding conformance rule is homed in a README, and a numbered
   clause cites the README as authority.** `rfcs/RFC-0008/README.md:163-168`;
   designated as the sole home by `state-vocabulary-and-cost.md:322-323` and
   `accounting-reconciliation-and-release.md:335-336`; cited as authority by
   RFC9-32 at `rfcs/RFC-0009/visual-grammar-and-lenses.md:210` and `:239`
   ("RFC 0008 §5").
   *Fix:* promote the paragraph to an RFC-0008 clause; repoint the four
   citations at the new clause ID.

6. **[Blocking] 18 of the 20 declared graph asymmetries are errors, not one-way
   edges.** 13 need their missing half; 5 are spurious and should be deleted
   (§1.1). The dependency index presents all 20 as "reported, not repaired…
   adding the missing half would be inventing an edge no module declares"
   (`CONTRACT-DEPENDENCY-INDEX.md:96-102`) — but for 13 of them the module's own
   §Integration prose already declares the reliance in words, so the half is not
   invented, merely untranscribed.
   *Fix:* apply the 20 dispositions in §1.1. Then adopt §1.4: author
   `depends_on` only, generate `provides_to`, and add a `constrains:` field for
   the 2 genuine one-way edges — otherwise the switch deletes them silently.

7. **[Blocking] RFC-0010's operability precondition has no clause home, in the
   file with no clause-precedence disclaimer.**
   `rfcs/RFC-0010-mission-control-autonomy.md:71-72` — missions "cannot lawfully
   *operate* under unamended doctrine's one-pass trigger" — sits in §2
   Motivation, which carries no `(non-normative)` label, in one of the only two
   modules lacking "the clause wins". Corpus sweep for `one-pass trigger`: 1
   hit. It also couples RFC-0010's operability to act 5, which the acceptance
   record marks optional.
   *Fix:* promote to a clause (RFC10-23), or at minimum label §1/§2 and add the
   precedence disclaimer to both RFC-0010 and RFC-0011.

8. **[Non-blocking] Three further obligations exist only in non-clause prose.**
   The general composite-maturity prohibition (`rfcs/RFC-0002/README.md:200-209`,
   whose own parenthetical concedes RFC7-16 is narrower); the board-layout rule
   "must place the terminal and absence values off the ladder"
   (`rfcs/RFC-0008/README.md:213-218`, corpus sweep: 2 lines, both in that
   passage); and "none may weaken the semantics here"
   (`rfcs/RFC-0006-...:483-485`, where RFC-0009 anchors the same rule to RFC9-2
   twice).
   *Fix:* the mechanical rule in §4.6 — no README §5/§7 sentence may state an
   obligation no clause states, and no clause may cite a README section as
   authority — plus a checker. It is a one-pass regex sweep.

9. **[Non-blocking] Four "stated once, never restated" claims are false, and two
   of the duplicated enumerations have already diverged.** The
   aggregation-disclosure enumeration exists in 5 places, 3 asserting they do not
   restate it (§3.2 finding 4); RFC9-43 vs RFC9-46 and RFC6-17 vs RFC6-22 both
   claim "the full equivalence tuple" while enumerating a subset (findings 5, 6);
   RFC9-24 names 4 sibling states where RFC2-25 closes the set at 3 and omits
   `editorial-draft` (finding 3); RFC5-25's location constraint has two binding
   homes (finding 7).
   *Fix:* one home each, cited by ID; and for the tuples, replace the
   enumerations with a bare citation so the identity claim cannot go stale.

10. **[Non-blocking] Two normative rules are carried only inside `[Inferred]`
    brackets, one of which a downstream clause cites.**
    `rfcs/RFC-0009/semantic-geography.md:195-199` ("containment wins", relied on
    at `:522`) and `rfcs/RFC-0009/interaction-parity-and-release.md:225-229`
    (RFC9-47(a)'s cross-module reach).
    *Fix:* move both out of the bracket into unbracketed clause limbs.

11. **[Non-blocking] Obligations carried by italic parentheticals inside
    clauses.** 54 such parentheticals, 14 obligation-bearing; the notable ones
    are an applicability precondition (`semantic-geography.md:594`) and the
    package scope of two release gates (`rfcs/RFC-0007/rendering-and-surface.md:321`,
    `rfcs/RFC-0009/interaction-parity-and-release.md:298`). The CC-VIZ-5
    parenthetical looks worse than it is — it reports owner amendment B21, which
    is genuinely installed and recorded (§4.4(a)).
    *Fix:* de-italicise the four obligation-bearing cases. *Caveat:* this count
    is a floor — one parenthetical escaped two regex passes; re-run with a
    paren-balancing parser before calling it exhausted.

12. **[Non-blocking] The reader map omits, for two of my three test tasks, the
    module that decides the question.** The Kernel implementer row
    (`06-CONTEXT-LOAD-MAP.md:38-39`) drops `rfcs/RFC-0002/rendering-vocabularies.md`,
    which owns RFC2-24 and RFC2-25. The Surface implementer row (`:40-41`) loads
    no kernel at all, though RFC-0009/0008/0007 cite RFC-0001 60/58/37 times.
    *Fix:* add `rendering-vocabularies` to the kernel row and RFC-0001 to the
    surface rows; or state on the map that role rows are orientation only and
    route selection through the fixtures, as `TASK-TO-CONTRACT-INDEX.md:52-59`
    already does.

13. **[Non-blocking] Two stale measured figures, and a universal claim about
    them that is false.** `06-CONTEXT-LOAD-MAP.md:33-34` states RFC-0010 3,096
    and RFC-0011 2,257; `context_load.py` — the tool the map names as the source
    of "all figures below" — returned 3,103 and 2,264 pre-edit (4,843 and 2,264
    now). `TASK-TO-CONTRACT-INDEX.md:113` asserts "The rest of 06's per-module
    table reproduces exactly (`wc -w`, **all 32 modules**, same date)"; I ran
    that exact sweep — **30 of 32 reproduce, 2 do not.** T-4 also still reports a
    governance-homes figure (4,401) that 06 has since corrected to 4,414. The
    Mission Control row at `:49` is likewise 14 words stale.
    *Fix:* re-run `context_load.py` across the table and rewrite T-4; replace
    the universal claim with the sweep's actual output.

14. **[Non-blocking] `RFC9-15(b)` is a lettered sub-clause with no `(a)`
    sibling.** Corpus-wide occurrences of `RFC9-15(a)`: **0**. It is a defined
    clause carried in `05-CONTRACT-INDEX.yaml` and cited 6 times, including by
    owner-approved craft policy (`performance-and-visual-discipline.md:126`),
    inside a package whose front matter asserts "no gaps, no retirements". Either
    reading — a removed `(a)`, or a letter chosen to mean "model (b)" — is an
    unexplained identity artifact.
    *Fix:* one sentence in RFC-0009 recording why the letter is `(b)`.

15. **[Non-blocking] `depends_on` is contract-granular while loading is
    module-granular.** This is why the declared graph mandates 50–100% closures
    (§6) while the fixtures achieve 11–18%, and why no tool can compute a packet.
    It is also why `TASK-TO-CONTRACT-INDEX.md` finding T-1 is correct that the
    index "cannot be generated and cannot be drift-checked".
    *Fix:* make `depends_on` values module paths rather than contract ids. Larger
    than the other fixes, and the highest-leverage one in this report.

16. **[Non-blocking] RFC-0007's front matter calls six list limbs
    "sub-clauses".** `rfcs/RFC-0007/README.md:7` and `narrative-contract.md:6`
    declare "sub-clauses RFC7-2(a)-(c), RFC7-9(a)-(c), RFC7-11(a)"; only
    RFC7-11(a) is a defined clause and only it appears in
    `05-CONTRACT-INDEX.yaml`. RFC-0005 and RFC-0008 get this right explicitly
    ("no lettered sub-clauses — RFC5-18(a)–(e) are list items inside RFC5-18").
    *Fix:* adopt RFC-0005's wording in RFC-0007's front matter.

17. **[Non-blocking, out of scope but material] Three copies of a stale
    check-result total sit in the owner-facing pre-act documents.**
    `round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md:201-202`,
    `round-2026-08/PUBLIC-CLONE-VERIFICATION-REPORT.md:51`, and
    `round-2026-08/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md:120` all state
    "15 OK, 7 WARN, 0 FAIL over 22 checks". Current: **9 OK / 7 WARN / 6 FAIL**.
    The pre-edit substance was benign — the FAILs came from this round's own raw
    reviewer files under CG-12/CG-1b, which are exactly what the CG-12b
    allowlist exists for — but finding 1 has since made CG-7a–d fail for real.
    *Fix:* regenerate the three copies from one run, or replace them with a
    pointer to a single generated block.

### What would make this an accept

Findings 1, 2 and 4 are hours of work. Finding 6 is a mechanical transcription of
prose the modules already contain, plus one schema decision. Finding 5 is a
promotion and four citation updates. Finding 3 is the only one needing the
owner's judgment, and RFC-0010 has already written the answer. Everything else
can ride as disclosed exceptions in the acceptance record, as the round already
does for the 20 edges.

I would expect a re-offer after those five to earn ACCEPT.

---

*End of RC-4. All measurements re-runnable from this packet; where pre-edit and
post-edit figures differ, both are stated. No `_bootstrap/` material was read.*
