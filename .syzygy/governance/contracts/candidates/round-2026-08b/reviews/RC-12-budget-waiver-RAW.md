# RC-12 — Context-packet budget waivers: independent review (RAW)

**Reviewer:** RC-12, independent. Fresh context; no authoring conversation, no
`_bootstrap/` material, no other reviewer's output read. Commissioned to rule on
the budget breaches in the context-selection fixture set.

**Date of run:** 2026-08-06.

**Commit this report is pinned to: `fc4632d`.** Every figure below was
recomputed against a clean `git archive HEAD` export at `fc4632d`, in
`$SCRATCH/head/`, *not* against the working tree. All nine fixtures are tracked
(fixture 9 committed at `7f0efa4`); doctrine and every RFC module are unmodified
at the working tree.

**The corpus moved under this review, and the report is pinned rather than
patched.** Partway through, a concurrent session modified four files under
`.syzygy/governance/policies/craft-and-care/` — including
`engineering-bar.md` (+46 words) and `testing-and-verification.md` (+163 words),
which are **mandatory members of fixtures 7, 8 and 9**. My measurement pass and
the confirming CG-18 run happened before those edits landed and reproduce
exactly at `fc4632d`; a later verification pass against the mutated tree did
not, which is how the drift was caught. Per the house rule that a report is
valid only for the commit it was run at, I re-ran everything at `fc4632d`
instead of adjusting figures in place. §1.3 records the working-tree state
separately and measures its effect. **The breach set is the same at both
states**, so no ruling depends on which is read.

**Standing of this document.** It is reviewer output, stored verbatim. It binds
nothing. It supplies field *values* for someone else to place; per the
commission I edited no fixture.

---

## 0. Summary of rulings

| Fixture | Est. tokens | Over 20,000 by | Ruling |
|---|---:|---:|---|
| 2 — Trajectory work-provider adapter | 24,680 | +23.4% | **WAIVER SOUND** |
| 7 — Kernel identity change | 21,246 | +6.2% | **WAIVER SOUND** |
| 8 — OpenSpec requirement authoring | 30,026 | +50.1% | **WAIVER SOUND** |
| 9 — Evidence-adapter change | 32,433 | +62.2% | **WAIVER SOUND** |

No fixture is oversized because it carries context its task does not need. I
found exactly one includable-but-unneeded item across the four packets (fixture
2's `RFC-0003/README.md`, 1,233 est. tokens), and removing it leaves that packet
17% over the line — so it is a hygiene finding, not the cause of a breach.

**The threshold these four are measured against binds nothing today.** §5 below.

Six exceptions are recorded in §7 and carried into the verdict.

---

## 1. The breach set, measured independently

I did not trust any stated figure. Four methods, all run in this session.

**Method A — `context_load.py` on each fixture's own declared command.** The
mandatory-set command was extracted programmatically from each fixture's fenced
block (not retyped) and executed.

**Method B — independent reimplementation.** My own Python: resolves the
`doctrine:` / `craft:` prefixes against the canonical homes, reads each file as
bytes, decodes UTF-8, `str.split()`, sums; sha256 over the concatenation in
listed order.

**Method C — `python3 scripts/check_governance.py`, CG-18.** Output read, not
exit code:

```
OK    CG-18  context fixtures recompute — 18 measurements examined, 0 findings
        (run at fc4632d; see §1.3 — this check FAILs at the working tree)
```

18 measurements over 9 fixtures = digest + word count each. Examined > 0, so the
OK is over a real population. CG-18 recomputes both the packet digest and the
word count from the declared mandatory set, so a zero-finding result is
independent confirmation that every fixture's stated word count and digest are
current.

**Method D — `wc -w`**, external to every Python path above, on the four
breaching packets.

### Results — all nine fixtures

| # | Fixture | Files | Words (A=B=C=D) | est. tokens (×1.35) | chars ÷ 4 | Digest (first 16) | vs. band | vs. 20k |
|---|---|---:|---:|---:|---:|---|---|---|
| 1 | polaris-narrative | 5 | 13,842 | 18,686 | 24,325 | `397ff4a12fccd9a8` | over | under |
| 2 | trajectory-adapter | 8 | 18,282 | **24,680** | 33,088 | `8e6399be638c2dc2` | over | **BREACH** |
| 3 | orrery-lens | 5 | 14,110 | 19,048 | 25,038 | `d513d1a1d3a51db2` | over | under |
| 4 | execution-profile | 6 | 10,866 | 14,669 | 19,517 | `ecda3b07013a7fb8` | **inside** | under |
| 5 | cross-project-mission | 5 | 14,770 | 19,939 | 26,435 | `fe06aa9df387474c` | over | under (by 61) |
| 6 | doctrine-amendment | 6 | 11,523 | 15,556 | 20,780 | `e4e186b76b6ec14e` | over | under |
| 7 | kernel-identity | 5 | 15,738 | **21,246** | 28,173 | `27955fccd11d8b63` | over | **BREACH** |
| 8 | openspec-authoring | 6 | 22,242 | **30,026** | 39,254 | `22f8187a89cc5013` | over | **BREACH** |
| 9 | evidence-adapter | 12 | 24,025 | **32,433** | 42,947 | `7f3b976d52b7e7f0` | over | **BREACH** |

**The four methods do not disagree.** Word totals are identical to the unit
across A, B, C and D; every computed digest matches the one the fixture
declares. [Inferred — from four runs in this session; the figures are
reproducible from the commands above.]

**Breach set = {2, 7, 8, 9}.** This matches the set the commission expected.
Fixture 2 is the one worth naming explicitly: it is a member of the **accepted**
rev10 set (fixtures 1–5), not a draft, and it breaches by 4,680 tokens.

### Two things the breach set does not show, and should

**(a) The default band, not the trigger, is the instrument that has failed.**
Sweep run this session over all nine: exactly **one of nine** packets — fixture
4, at 14,669 — lands inside CC-BUDGET-1's 5,000–15,000 default band. The
remaining eight are the enumerated remainder: 15,556 / 18,686 / 19,048 / 19,939
/ 21,246 / 24,680 / 30,026 / 32,433. Median packet = 19,939. See §6.

**(b) Breach-set membership is not stable.** Fixture 5 sits **61 estimated
tokens** (45 words) below the trigger. Its own re-measurement footnote records a
prior figure of 12,843 words against a current 14,770 — a 1,927-word movement.
A packet 0.3% from the line, in a corpus that moves by more than that between
measurements, is a coin-flip member of the breach set. I did not rule on fixture
5 (it does not breach as measured), but a reviewer relying on this set should
know the boundary is that thin.

### 1.3 The working-tree state, measured separately

The four methods above ran at `fc4632d`. Re-running the same extraction against
the **working tree** at the close of this session gives:

| Fixture | at `fc4632d` | at working tree | Δ | craft file loaded |
|---|---:|---:|---:|---|
| 1, 2, 3, 5, 6 | unchanged | unchanged | 0 | none |
| 4 | 14,669 | 14,669 | 0 | `security-and-secrets.md` (unedited) |
| 7 | 21,246 | **21,308** | +62 | `engineering-bar.md` (+46 w) |
| 8 | 30,026 | **30,246** | +220 | `testing-and-verification.md` (+163 w) |
| 9 | 32,433 | **32,653** | +220 | `testing-and-verification.md` (+163 w) |

**The breach set is {2, 7, 8, 9} at both states**, and no non-breaching fixture
crosses the line at either — fixture 5, the near-miss at 19,939, loads no craft
file and does not move. Every ruling in §3 therefore holds at both states.

**But the battery no longer passes at the working tree, and a reviewer must not
read this report's CG-18 confirmation as current.** Re-running
`check_governance.py` at the working tree:

```
FAIL  CG-18  context fixtures recompute — 18 measurements examined, 7 findings
        …context-selection-3-orrery-lens.md — packet digest `d513d1a1d3a51db2…`
                but the declared mandatory set hashes to `44dbffa47adfe17e…`
        …context-selection-7-kernel-identity.md — claims 15,738 words;
                the declared mandatory set is 15,784
        …context-selection-8-openspec-authoring.md — claims 22,242 words;
                the declared mandatory set is 22,405
        …context-selection-9-evidence-adapter.md — claims 24,025 words;
                the declared mandatory set is 24,188
        (+ the three corresponding digest mismatches)

19 OK, 11 WARN, 6 FAIL (36 checks)
```

Three of the four breaching fixtures no longer reproduce their declared word
counts or digests at the working tree, and fixture 3 has a digest mismatch with
**no** word-count change — a whitespace-neutral edit in one of its mandatory
files. Fixture 3 is outside my commission (it does not breach) and I did not
chase it; it is recorded here because a digest that moves while the word count
does not is precisely the silent-drift case CG-18 exists to catch, and someone
owns it.

I take no position on the concurrent session's edits — they are mid-flight
repair work and their correctness is not my commission. What I record is that
**this review's figures are `fc4632d` figures**, that the fixtures' declared
figures are stale against the working tree as of this writing, and that whoever
places the fields in §3 must re-run CG-18 and re-measure before doing so. That
is not a criticism of the edits; it is the invalidation the digests are designed
to produce, working correctly.

### One transcription note

Fixture 9 states *"43,228 estimated tokens at chars ÷ 4 over 172,915
characters."* 172,915 is the **byte** count; the character count is 171,791
(chars ÷ 4 = 42,947). The figure reproduces exactly as bytes, so the arithmetic
is right and the label is wrong. Immaterial to any ruling — recorded because a
derived figure that reproduces under the wrong name will mislead the next person
who recomputes it.

---

## 2. What the governing clause actually requires

Read at source, not from the commission's paraphrase.

**Long form** — `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md:288-298`
holds **CC-BUDGET-1**, which is *only* the trigger table. The five waiver fields
are **CC-BUDGET-3** (`… — Waivers are recorded, with an expiry`):

> A waiver records artifact, reason, scope, reviewer, and an expiry or revisit
> trigger; the verifier prints the recorded justification alongside the breach
> rather than passing silently. A waiver with no expiry is a permanent exception
> pretending to be temporary.

**Compact form** — `CRAFT-KNOWLEDGE-HYGIENE-POLICY-COMPACT.md:213-243` folds
CC-BUDGET-2/3/4 into CC-BUDGET-1 (`*Absorbs:* CC-BUDGET-2, CC-BUDGET-3,
CC-BUDGET-4`), so under the compact form the five fields **are** CC-BUDGET-1's.

So the commission's attribution is correct for the compact form and wrong for
the long form. It matters only because the two versions are both candidate and
neither is installed — a citation of "CC-BUDGET-1" resolves to a different
obligation depending on which unadopted file the reader opens. [Inferred]

**The charter text differs from the commission's quote.** The commission quotes
"§12.4" as requiring *"task decomposition or an explicit reviewed waiver."*
There is no §12.4. The table is at
`round-2026-08/OWNER-ROUND-CHARTER.md:804-817`, **§11.4**, and its trigger row
reads:

> | Context packet above 20,000 tokens | justification or task decomposition |

followed by: *"The limits are decomposition triggers, not validity laws."* A
regex sweep this session for `reviewed waiver|explicit reviewed` across
`.syzygy/**` returns three hits, none in a budget context (two are RFC9-52
routing rows, one is the surface-clause matrix preamble). **The phrase "explicit
reviewed waiver" is not in the governing text.** What the text asks for is a
*justification*; the waiver-with-a-reviewer shape comes from CC-BUDGET-3, which
is candidate. This distinction is load-bearing for §5.

**RFC11-5 and RFC11-11**, read at `rfcs/RFC-0011-context-compiler.md`, are as
the fixtures represent them. RFC11-5: inference "may never suppress, demote, or
replace mandatory deterministic context." RFC11-11: "budget pressure never
justifies dropping mandatory context (RFC11-5) — the lawful responses are
sharding, narrowing the objective, or escalating," with a **non-shardable core**
that every shard must carry (envelope, prohibited/human-only surfaces,
applicable doctrine rules, governing phase rules). Both are candidate; RFC-0011
carries the *"Absent such a record, this contract binds nothing"* banner and is
inside pending act 1.

---

## 3. Per-fixture rulings

Every alternative configuration below was **measured with `scripts/context_load.py`
against the clean `fc4632d` export**, not computed by arithmetic on this page and
not taken from the working tree. Figures the fixtures also state are marked where
they disagree.

---

### Fixture 2 — Trajectory work-provider adapter mapping

`context-selection-2-trajectory-adapter.md` · 18,282 w · **24,680 est. tokens**

Per-file: `RFC-0004/README` 1,670 · `general-contract` 1,677 · `named-adapters`
3,682 · `RFC-0008/README` 1,918 · `state-vocabulary-and-cost` 3,504 ·
`RFC-0003/README` 913 · `governance-homes-and-owner-acts` 4,407 ·
`doctrine:security` 511.

## RULING: **WAIVER SOUND**

**Necessity test, item by item.** The task is an authorization-bearing edit to
the substrate→normalized work-state derivation mapping (RFC8-12/13).

- `RFC-0003/governance-homes-and-owner-acts.md` (4,407 w, 24% of the packet) —
  **necessary and irreducible.** It is the smallest load unit carrying
  RFC3-16(a)/(b)/(c); RFC-0003 is a two-module package and the other module is
  manifests/namespace, correctly excluded. The editor of an RFC3-16(a) artifact
  needs (b) in particular: what a conforming act must *bind* determines whether
  the edit is even act-ready. Deferring this to "the ceremony packet" would ship
  an edit whose author did not know it was inert.
- `RFC-0008/README.md` (1,918 w) — **necessary under RFC11-4.** RFC-0008's
  governing phase rule is RFC8-32, whose clause text lives in
  `accounting-reconciliation-and-release.md` (not loaded); the README's "Phase
  boundary" section is the restatement. RFC11-4 requires "the governing
  phase-rule clause of every selected contract (**the module or README text
  carrying it**)" — the parenthetical makes the README a lawful carrier. Without
  it this packet violates RFC11-4.
- `RFC-0004/README.md` (1,670 w) — **necessary.** It carries the RFC4-n lookup
  rule and the package's open owner questions (q2 envelope minimality, q3 marker
  adoption, q4 capture cadence — all open), which live in no loaded module.
- `doctrine:security.md` (511 w) — the SEC-3 untrusted-actor premise; the whole
  reason the artifact is RFC3-16(a). Non-shardable core under RFC11-11.
- `RFC-0003/README.md` (913 w ≈ 1,233 est. tokens) — **fails the necessity
  test.** See the finding below.

**Decomposition, measured.** Fixture 2 names one lawful alternative in passing —
*"sharding the task (mapping edit vs approval ceremony as two packets)"* — and
does not measure it. I measured it:

| Configuration | Words | est. tokens |
|---|---:|---:|
| As declared | 18,282 | 24,680 |
| Shard A — mapping edit, sheds RFC-0003 entirely | 12,962 | **17,498** |
| Minus `RFC-0003/README.md` only | 17,369 | 23,448 |
| Under the strict RFC11-4 reading (+ RFC-0008 phase module, keeps RFC-0003 README) | 21,333 | 28,799 |

Shard A lands under the trigger — and is **not lawful**. It is the same trim the
fixture's own necessity argument forbids, and the same one fixture 9 refuses in
identical words (*"sheds the contract that makes the edited registry entry
honored — the shape fixture 2 refuses for the same reason"*). The "shard" fixture
2 gestures at is a trim wearing a shard's name. Recorded so the next reader does
not take it as an available option.

No other split exists: the task is one mapping edit. Splitting it by RFC-0008
clause (RFC8-12 vs RFC8-13) would put both halves in the same module.

### Waiver fields — fixture 2

Fixture 2 records **no waiver block at all** — no artifact, reason, scope,
reviewer, or expiry field. It states its position as prose against the wrong
line (see finding F-1). So unlike fixtures 7/8/9 I am not filling two empty
fields; I am supplying all five.

| Field | Value |
|---|---|
| **Artifact** | Fixture 2's mandatory selection — 8 files, 18,282 words, packet digest `8e6399be638c2dc2…`, measured at the canonical-home bytes of 2026-08-06 |
| **Reason** | An authorization-bearing derivation-mapping edit cannot shed (i) the act contract that makes the edited artifact honored — RFC3-16(a)/(b)/(c), whose smallest load unit is a 4,407-word module; (ii) the consuming state vocabulary the mapping projects into (RFC8-12/13, tables read verbatim); (iii) the adapter contract bounding what the adapter may write; or (iv) the SEC-3 premise that makes (i) necessary. The only measured configuration under the trigger (17,498) is reached by dropping (i), which RFC11-5 forbids and which this fixture's own reasoning refuses |
| **Scope** | Work-provider adapter changes that edit an **RFC3-16(a) authorization-bearing** derivation mapping. Does **not** cover: the approval ceremony for such a mapping (that is a separate, smaller packet); mapping edits that are not authorization-bearing; adapter changes touching execution-record capture or fidelity joins (that is fixture 9's class) |
| **Reviewer** | RC-12, independent reviewer, 2026-08-06 — reviewed the *selection*, not the contracts it selects. See §5 on what this signature can and cannot mean while no rule is installed |
| **Expiry / revisit trigger** | Expires at the **earlier** of (a) the first real work-provider adapter mapping change, or (b) **owner act 1**, which binds the digests of every RFC module in this set. Re-review is mandatory at expiry; this waiver does not auto-renew |
| **Early-revisit conditions** | (i) If the strict RFC11-4 reading is adopted (finding F-3), the packet becomes 28,799 and this waiver's reason no longer covers it — re-measure before relying on it. (ii) If `RFC-0003/governance-homes-and-owner-acts.md` is ever split, a smaller load unit exists and the "smallest load unit" reason is void. (iii) If a budget rule is installed whose number is not 20,000 |

### Finding F-1 (fixture 2) — the breach is not stated as a breach

Fixture 2's prose reads: *"above the **15–20k working target**, disclosed as a
risk-class exception (RFC11-11)."* That is the `06-CONTEXT-LOAD-MAP.md` target,
not the trigger. The fixture nowhere states that 24,680 is **23.4% above the
20,000-token decomposition trigger** — the line that actually calls for
justification. A reader checking fixture 2 against §11.4 finds no acknowledgment
that §11.4 was crossed.

This is the only fixture in the breach set that does not name the line it
crossed, and it is the only one in the **accepted** set. The accepted fixture has
the weakest budget record in the file; the three drafts have full waiver tables.

### Finding F-2 (fixture 2) — `RFC-0003/README.md` is includable-but-unneeded

Fixture 9 declines this exact file and states its reasoning as *a departure from
fixtures 2, 4, 5 and 6*: the loaded module's own front matter reads

```
clauses: "RFC3-15, RFC3-15(a), RFC3-16, RFC3-16(a), RFC3-16(b), RFC3-16(c),
          RFC3-17, RFC3-17(a) (every other RFC3-n lives in manifests-and-namespace.md)"
```

I verified that line at `rfcs/RFC-0003/governance-homes-and-owner-acts.md:6`. It
resolves every `RFC3-n` deterministically without the package index. The
README's remaining unique content is open questions q1 (monorepo subprojects,
RFC3-29) and q2 (workspace manifest classification, RFC3-10) — **both live in
`manifests-and-namespace.md`**, which this packet correctly excludes as out of
scope; q4 (the `declarations/` category) is carried in the loaded module's §5;
q5 is answered in RFC3-16(a)/(c), loaded. RFC-0003 has no phase rule, so RFC11-4
does not require its README.

**Fixture 9 is right and fixture 2 is wrong on this file.** Removing it is a
correction, not a budget trim — it was never mandatory, so RFC11-5 is not
engaged. Effect: 23,448 est. tokens, still 17.2% over the trigger. The ruling
stands unchanged.

---

### Fixture 7 — Kernel identity change

`context-selection-7-kernel-identity.md` · 15,738 w · **21,246 est. tokens**

Per-file: `RFC-0001` 8,342 · `RFC-0002/README` 1,809 ·
`snapshot-and-evaluation-core` 1,955 · `doctrine:architecture` 2,350 ·
`craft:engineering-bar` 1,282.

## RULING: **WAIVER SOUND**

This is the mildest breach in the set — 1,246 tokens, 6.2% — and the most
structurally determined. **RFC-0001 alone is 11,261 est. tokens: 53% of the
packet, in one indivisible file.** `check_governance.py` CG-8 reports it this
session: *"RFC-0001 … 8342 words, above 5000: §11.4 focused decomposition
review"*, and the acceptance record carries it as known exception #2 (*"RFC-0001
is 8,342 words against a 7,000 ceiling — justified as a dictionary-shaped kernel
contract, not fixed"*).

**Both of the fixture's own decomposition options are correctly declined, and I
re-measured both** — the fixture's figures are stale (finding F-4):

| Configuration | Words | est. tokens | fixture's figure |
|---|---:|---:|---:|
| As declared | 15,738 | 21,246 | 21,285 (stale) |
| (a) Drop `craft:engineering-bar.md` | 14,456 | **19,515** | 19,554 (stale) |
| (b) Drop `RFC-0002/README.md` | 13,929 | 18,804 | 18,831 (stale) |
| Drop RFC-0002 entirely | 11,974 | 16,164 | not measured |

- **(a) declined, correctly.** CC-BAR-5 floor 7 is this change's *declared risk
  class* — "kernel identities and `.syzygy/**` schema migrations are
  identity-preserving; migrations never orphan or silently re-mint durable IDs."
  Its text is restated in no loaded RFC. A change classified by a floor whose
  text the implementer does not hold is classified by a label. Consistent with
  fixture 4's precedent and with fixture 9's treatment of CC-TEST-2.
- **(b) declined, correctly — and I checked the reason mechanically.** The
  loaded `snapshot-and-evaluation-core.md` cites **RFC2-12, 13, 15, 17, 18 and
  24** — six clause identities outside its own RFC2-1..11 range — and the loaded
  `RFC-0001` cites nine (RFC2-3, 11, 12, 13, 15, 16, 18, 21, 24). The README's
  lookup rule is what resolves fifteen citations without a search, and its
  *"Forward references are informative"* rule is what stops the reader chasing
  RFC3-n/RFC4-n citations into the packet. Both live nowhere else here.

**Dropping RFC-0002 entirely (16,164) is the one configuration that lands well
inside the band, and it is not lawful.** The fixture does not measure it, so I
did. It is unlawful for a specific reason: identity orphaning — the exact harm
CC-BAR-5 floor 7 names — becomes visible only at the claim-resolution seam that
RFC-0002 owns. A shard that changes minting without the evaluation semantics
cannot see what it breaks.

**No split reduces the kernel term.** Splitting "the minting/successor scheme"
from "the continuity links recorded for it" gives two shards that each carry
RFC-0001 in full: 22,522 est. tokens of kernel across the pair, against 11,261
undivided. Decomposition here is arithmetically negative before it is
epistemically bad.

### Waiver fields — fixture 7

Fixture 7 records Artifact, Reason and a partial Expiry; Scope is thin and
Reviewer is empty. Supplied and completed:

| Field | Value |
|---|---|
| **Artifact** | Fixture 7's mandatory selection — 5 files, 15,738 words, packet digest `27955fccd11d8b63…` |
| **Reason** | Retained as written, with the figures corrected to 21,246 / 19,515 / 18,804. The substance survives scrutiny: 53% of the packet is one indivisible contract, and the two measured trims each remove either the obligation the change may violate (a) or the lookup rule for fifteen out-of-range citations (b) |
| **Scope** | Kernel identity and continuity changes — minting, successor edges, split/merge, and the continuity links recorded across them — **where CC-BAR-5 floor 7 is the declared classifier**. Does **not** cover: the adoption ceremony for such a change (RFC-0003 stays deferred to that packet, as the fixture already rules); `.syzygy/**` schema migrations that do not alter minting; changes to challenge, reconciliation or rendering semantics (those pull further RFC-0002 modules and must be re-measured) |
| **Reviewer** | RC-12, independent reviewer, 2026-08-06 |
| **Expiry / revisit trigger** | Expires at the **earlier** of (a) the first real kernel identity work item, or (b) **any change that makes RFC-0001 divisible** — a package split, or the focused decomposition review §11.4 already calls for and CG-8 already reports. Condition (b) is the operative one: 53% of this packet is that file, and if it becomes divisible the entire justification is void, not merely weakened |
| **Early-revisit conditions** | (i) If the owner rules that a craft floor cited to *classify* a change need not be held in text by the implementer, the packet measures 19,515 and needs **no waiver at all** — this waiver must then be **retired**, not renewed. (ii) **Owner act 5** (doctrine amendment D3) amends `architecture.md`, which is mandatory here; act 5 invalidates the packet digest and requires re-measurement. (iii) Owner act 1 |

---

### Fixture 8 — OpenSpec requirement authoring

`context-selection-8-openspec-authoring.md` · 22,242 w · **30,026 est. tokens**

Per-file: `RFC-0001` 8,342 · `RFC-0007/README` 2,324 · `narrative-contract`
5,165 · `rendering-and-surface` 3,142 · `doctrine:vision` 2,156 ·
`craft:testing-and-verification` 1,113.

## RULING: **WAIVER SOUND**

The fixture measured three splits and declined all three. I checked each and
added a fourth the fixture did not consider — the *floor* configuration, which
is the one that decides the ruling.

| Configuration | Words | est. tokens |
|---|---:|---:|
| As declared | 22,242 | 30,026 |
| **Floor A** — kernel + RFC-0007 README + narrative module only + vision + testing | 19,100 | **25,785** |
| **Floor B** — kernel + RFC-0007 README + rendering module only + vision + testing | 17,077 | **23,053** |

**Neither floor lands under the trigger.** Floor B — the smallest configuration
that is lawful at all under RFC11-4 and RFC11-11 — is still 15.3% over. This is
the fixture's central claim (*"no lawful split lands inside the default band"*)
and it is correct; I am strengthening it, because the fixture stopped at "not
inside the band" and the sharper true statement is **not inside the trigger
either, under any lawful configuration.**

**Necessity test.**

- `RFC-0001` (11,261 est. tokens, 38%) — RFC1-14 capability identity and RFC1-15
  ("Requirement and Scenario are references, not owned content") are exactly what
  a requirement author must not invent. Indivisible.
- `doctrine:vision.md` — VIS-3 fresh-reader review and VIS-4's always-human
  spec-adoption class. **Doctrine is the only adopted authority in this
  repository**, and RFC11-11's non-shardable core names applicable doctrine
  rules explicitly. Not droppable in any shard.
- `craft:testing-and-verification.md` — a requirement that cannot be stated
  testably is not a requirement. Owner-approved policy (D2).
- `RFC-0007/README.md` — **necessary, for a better reason than the fixture
  gives.** The fixture justifies it weakly (as the phase-rule carrier, then
  notes its phase section "is a restatement pointing there"). I read it: the
  README uniquely carries (i) package-spanning violation cases 10, 13 and 15,
  explicitly "held here" rather than in either module; (ii) the owner-question
  index, of which **q2 (primary-narrative cardinality, RFC7-6) and q4
  (rejected-draft retention, RFC7-22) are open** — an author writing requirements
  against RFC7-6 must know its cardinality is unruled; and (iii) the instruction
  that RFC7-38's coverage matrix "must cover **RFC7-1…RFC7-37 across both
  modules**, not the rendering module alone" — which is a scope constraint on
  this task's actual deliverable, stated nowhere else. The README earns its
  place three times over.
- Both RFC-0007 modules — the fixture's declined-split table is right that
  authoring from the README alone is the summary-as-authority substitution the
  round exists to prevent.

**Task decomposition, considered independently of the packet.** Authoring splits
by requirement, by capability, or by phase (derive the coverage matrix, then
author text). None reduces the packet: every sub-task needs RFC-0001 for
identity and at least one RFC-0007 module for the behaviour, which is Floor A or
Floor B. The narrowing the fixture names — "a capability whose surface contract
is smaller than RFC-0007's" — is not a decomposition of *this* task; it is a
different task. Correctly characterised as an owner trade, and correctly
declined as a default.

### Waiver fields — fixture 8

Fixture 8 records Artifact, Reason, Scope and Expiry, with Reviewer empty.
Reviewer supplied; Scope and Expiry tightened.

| Field | Value |
|---|---|
| **Artifact** | Fixture 8's mandatory selection — 6 files, 22,242 words, packet digest `22f8187a89cc5013…` |
| **Reason** | Retained as written, with the token figures corrected to 30,026 (finding F-4). Strengthened: the *lawful floor* of this task — one indivisible kernel plus one surface module plus its package index plus doctrine plus the verification bar — measures 23,053, above the trigger with nothing left to remove |
| **Scope** | OpenSpec requirement authoring against an adopted capability **whose surface contract is RFC-0007 (Polaris)**. Does **not** stretch to another surface contract: the fixture itself names "a capability whose surface contract is smaller" as the narrowing that retires this waiver, so applying it there would be applying it to the case that voids it. Does not cover review of the authored delta (that packet pulls `craft:review-and-documentation.md` instead) |
| **Reviewer** | RC-12, independent reviewer, 2026-08-06 |
| **Expiry / revisit trigger** | Expires at the **earlier** of (a) the first real OpenSpec authoring task, or (b) **unconditionally at the creation of `openspec/**`**. (b) is not in the fixture and should be: the packet currently renders the absent house conventions as an RFC11-6 Unknown and proceeds; the moment conventions exist they become mandatory context, the measured floor changes, and this waiver was computed against a corpus that no longer describes the task |
| **Early-revisit conditions** | (i) RFC-0001 becoming divisible — 38% of this packet. (ii) **Owner act 2** (CC-TEST-2 amendment) lands in `testing-and-verification.md`, and **owner act 5** (D3) amends `vision.md`; both files are mandatory here, so either act invalidates the digest and requires re-measurement. (iii) Owner act 1 |

---

### Fixture 9 — Evidence-adapter change (gate provenance and fidelity)

`context-selection-9-evidence-adapter.md` · 24,025 w · **32,433 est. tokens**

Per-file: `RFC-0004/README` 1,670 · `general-contract` 1,677 · `named-adapters`
3,682 · `execution-record` 1,770 · `fidelity-joins-and-mappings` 1,737 ·
`RFC-0002/README` 1,809 · `rendering-vocabularies` 2,388 ·
`RFC-0005/execution-profiles` 2,192 · `RFC-0003/governance-homes` 4,407 ·
`doctrine:trust-and-evidence` 1,069 · `doctrine:security` 511 ·
`craft:testing-and-verification` 1,113.

## RULING: **WAIVER SOUND**

This is the largest packet and the closest call, because **the fixture itself
argues against its own waiver**: *"a lawful split exists, and only half of it
fits… Whether the undivided form or the two-shard form is the default is an
owner trade."* The commission asks me to rule rather than defer, so I checked
the split against clause text.

### Finding F-5 — fixture 9's declared Shard 1 is incomplete for its own warrant

The warrant declares three things: (i) the route-2 external-confirmation capture
artifact (RFC4-13(a)); (ii) the observer's degradation mapping (RFC4-25); (iii)
the `reduced-fidelity` cause emitted when the provider's run records fall past
the retention horizon (**RFC4-24, RFC4-16**).

Declaration (iii) spans two modules, and I confirmed this at clause text:

- **RFC4-16** — "Capture-before-horizon", in `named-adapters.md` (module 2,
  RFC4-10..17): the retention bound, "a declared policy in the governance plane
  and a snapshot input… honored **only under RFC3-16(a)**."
- **RFC4-24** — the labeling schema, in `fidelity-joins-and-mappings.md` (module
  4, RFC4-22..29): the closed cause list, which contains
  `retention-horizon-passed`.

Fixture 9's **Shard 1 is "modules 1 + 4"** — it holds RFC4-24's cause list but
**not** RFC4-16, so it cannot evaluate when the horizon is crossed. Its **Shard
2 is "modules 1–3"** — it holds RFC4-16 but **not** RFC4-24, so it cannot know
which cause to emit. **The declared split cuts declaration (iii) in half and
neither shard is complete for it.** The fixture's shard table does not notice
this, and it is the fixture's own load-bearing finding.

### The corrected split, measured

| Configuration | Words | est. tokens |
|---|---:|---:|
| As declared (undivided) | 24,025 | 32,433 |
| Fixture's Shard 1 (modules 1+4, tiers, trust) — **incomplete** | 10,350 | 13,972 |
| **Corrected Shard 1′** — Shard 1 **+ `named-adapters.md`**, closing RFC4-16 × RFC4-24 | 14,032 | **18,943** |
| Corrected Shard 1′ + `craft:testing-and-verification.md` | 15,145 | 20,445 |
| Shard 2′ (= fixture's Shard 2: modules 1–3, tiers, profiles, acts, doctrine, craft) | 22,288 | **30,088** |
| Three-way sub-shard 2a (registry + act machinery) | 13,016 | 17,571 |
| Three-way sub-shard 2b (routes + records + tiers) | 17,370 | 23,449 |

Two results follow, and together they settle the ruling.

**First: a *complete* Shard 1 exists at 18,943 — under the trigger.** That is a
better result than the fixture claims and I record it in its favour. (Adding
CC-TEST-2 pushes it to 20,445; I hold CC-TEST-2 *suggested* for a labeling-only
warrant, because RFC4-24's closed cause list, not CC-TEST-2, is that sub-task's
classifier. If a reviewer disagrees, Shard 1′ breaches by 445 tokens and the
split loses its only in-band half.)

**Second: no configuration of the remainder fits.** Shard 2′ is 30,088. A
three-way split leaves 2b at 23,449 — still over — and its cost is severe: the
three shards total 40,736 words against 24,025 undivided (**+70%**), with
`RFC-0004/README`, `general-contract`, `named-adapters`, `RFC-0002/README`,
`rendering-vocabularies` and `trust-and-evidence` — 11,014 words, 46% of the
packet — duplicated into every shard by RFC11-11's non-shardable core.

**Why WAIVER SOUND rather than DECOMPOSE.** CC-BUDGET-1's second paragraph asks
whether an **honest** split exists, and its named violation is *"a module split
into two files just under the trigger, sharing a preamble and always read
together — the number is satisfied and the reader's load is unchanged."* A split
that duplicates 46% of its own content, increases total reading by 70%, still
requires a waiver for the larger half, and puts a warrant seam exactly between
"what fidelity label is emitted" and "what tier the outcome enters" — the two
halves of the *"confident adapter — an integration that silently normalizes,
silently interpolates, or silently forgets"* failure that RFC-0004's own reader
map names at `RFC-0004/README.md:117-120` — is that violation, not its remedy.
**For the warrant as stated, the undivided packet is the honest form.**

**Necessity test on the remaining items.** `RFC-0003/governance-homes` (4,407 w,
18%) — the change edits an RFC4-7 registry entry and relies on RFC4-16's
retention bound, both honored only under RFC3-16(a); irreducible, same argument
as fixture 2. `RFC-0002/README` — nine cited RFC2-n resolve through its lookup
rule; the fixture's measured drop (29,991) is still over and loses the lookup.
`RFC-0005/execution-profiles` — RFC5-21 is route 1's predicate; without it the
four-route test is unevaluable. `doctrine:trust-and-evidence` + `security` —
adopted authority, non-shardable core. `craft:testing-and-verification` —
CC-TEST-2 is quoted at binding strength inside RFC4-13. **Nothing here is
includable-but-unneeded.** I found no unneeded item in this packet at all; its
omission register is the most rigorous in the set, and its declared
dependency-closure rule with the RFC-0001 edge left open and its three promotion
triggers named is the correct handling of an unclosed edge.

### Waiver fields — fixture 9

| Field | Value |
|---|---|
| **Artifact** | Fixture 9's mandatory selection — 12 files, 24,025 words, packet digest `7f3b976d52b7e7f0…` |
| **Reason** | Retained as written. Strengthened by finding F-5: the four-module RFC-0004 package is irreducible **for this warrant specifically**, because declaration (iii) binds RFC4-16 (module 2) to RFC4-24 (module 4), and the union of any split that keeps them together is the whole package |
| **Scope** | Evidence-adapter changes touching gate provenance (RFC4-13 routes), capture cadence or retention (RFC4-16), or fidelity labels (RFC4-24/25), **where the warrant spans the retention × cause coupling** — i.e. where a `reduced-fidelity` cause depends on a retention-horizon fact. A warrant touching **labels only**, with no RFC4-16 dependency, is **out of scope** and must use the 18,943-token Shard 1′ instead of this waiver. Does not cover changes that also touch work-state rendering (fixture 2's class) or that add prose fields to a record (which pulls `RFC-0005/consent-egress-secrets`) |
| **Reviewer** | RC-12, independent reviewer, 2026-08-06 |
| **Expiry / revisit trigger** | Expires at the **earlier** of (a) the first real evidence-adapter work item, or (b) **owner act 2**. (b) is mandatory, not optional: CC-TEST-2 is in this packet and is the subject of act 2, so every conclusion the packet supports from CC-TEST-2 is provisional until the act lands — the fixture discloses this correctly, and the waiver must not outlive the disclosure |
| **Early-revisit conditions** | (i) Any of the three RFC-0001 promotion triggers the fixture names entering the warrant (code-element identity minting, the materialization/warrant join, or Execution Record run identity) — the packet is then incomplete under RFC11-6 and this waiver does **not** cover the resulting 43,695-token packet; the run blocks instead. (ii) The warrant narrowing to labeling-only — Shard 1′ applies and **no waiver is needed**. (iii) Owner act 1 |

---

## 4. Overlap between breaching fixtures

The commission asks whether the same decomposition argument applies to more than
one. It applies to two disjoint pairs, and both are facts about the **corpus**,
not about the selections.

**Pair {7, 8} — the indivisible kernel.** Shared mandatory content: `RFC-0001`,
8,342 w = **11,261 est. tokens**. That is 53% of fixture 7 and 38% of fixture 8.
Any task touching entity identity or capability identity starts there before a
second file loads. The decomposition argument is identical in both — *every*
shard carries the whole kernel, so sharding multiplies the dominant term rather
than dividing it — and it produces the same answer in both. One finding, not
two.

**Pair {2, 9} — the authorization-bearing evidence-plane floor.** Shared
mandatory content, measured: `RFC-0004/README` + `general-contract` +
`named-adapters` + `RFC-0003/governance-homes` + `doctrine:security` = 11,947 w
= **16,128 est. tokens** — 65% of fixture 2 and 50% of fixture 9. An
authorization-bearing change on the evidence plane costs 16,128 tokens before
its own subject matter loads, driven by one 4,407-word governance module and one
3,682-word adapter module, neither divisible. Again one argument, applied twice,
with the same answer. Fixture 9 already recognises the shared shape (*"the shape
fixture 2 refuses for the same reason"*), which is the strongest internal
evidence in the set that the two fixtures were reasoned consistently.

**Consequence.** Four breaches, two structural causes. Any owner remedy that
addresses the two causes — RFC-0001's indivisibility and the RFC-0003/RFC-0004
module sizes — resolves all four; no remedy aimed at the fixtures resolves any
of them.

---

## 5. Is the threshold established anywhere binding?

**No. [Inferred, from five source checks run this session.]** Enumerated in
descending order of authority:

1. **Adopted doctrine** (`.syzygy/governance/doctrine/`, VIS-1..7 / SEC-1..5) —
   the only adopted authority in this repository. A regex sweep this session for
   `token|budget|word count|packet size` across all doctrine files returns **two
   hits, both the phrase "zero-token synchronization"** (`architecture.md:252`,
   `vision.md:86`) — a substrate property, not a budget. **Doctrine contains no
   context budget.**
2. **Owner-approved craft-and-care** (`.syzygy/governance/policies/craft-and-care/`,
   D2). A sweep of every `CC-*-n` identifier installed there returns 47
   identifiers across BAR/DEP/OBS/PERF/PROV/REV/SEC/TEST/VIZ. **`CC-BUDGET-*`
   is not among them, and neither is `CC-KNOW-*`.** The fixtures' claim that no
   `CC-BUDGET-*` identifier resolves to an installed governed artifact is
   **correct**.
3. **`policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY[-COMPACT].md`** — where
   CC-BUDGET-1 actually lives. Its own banner: *"**Candidate — binds nothing.**
   … it is not installed at that cluster's canonical home … it acquires force
   only through its **own** owner craft-amendment act … Until that act the
   identifiers below are **provisional**."* And it is **not among the five
   pending owner acts** — acts 1–5 are the 32 contract modules, CC-TEST-2, the
   topology bundle, the overview, and D3. **There is no scheduled path by which
   CC-BUDGET-1 becomes binding.**
4. **`round-2026-08/OWNER-ROUND-CHARTER.md` §11.4** — the table the fixtures
   cite directly. The charter's own opening line is *"Run this prompt in a fresh
   Claude Fable session"*: it is a **session prompt**, filed under
   `contracts/candidates/`, and per AGENTS.md everything under that root is
   candidate and never citable as binding. Its own text says *"The limits are
   decomposition triggers, not validity laws."*
5. **RFC-0011 / RFC11-11** — candidate, inside pending act 1, carrying *"Absent
   such a record, this contract binds nothing."* And it **explicitly declines to
   fix a number**: *"[Inferred] The concrete numeric target is a policy default,
   not doctrine — it must not be frozen into contract text without an owner act;
   … its permanent custody is §8 q1."* §8 q1 is open: *"does the owner want it
   recorded as a named policy artifact at V0, or left to the OpenSpec phase?"*

**What this means for these four objects.** The commission's framing is right
that "a waiver against a non-existent rule is a different object than a waiver
against a rule," and the difference is worth stating precisely:

- **A waiver presupposes a rule to waive and a reviewer empowered to waive it.**
  Neither exists. My signature in the Reviewer field above does not confer
  permission, because there is no permission to confer. What it records is that
  an independent reader recomputed the figures, examined every alternative, and
  found no packet padded.
- **What RFC11-11 *would* bind at act 1 is not the number but the posture:**
  *"exceeding the posture is a disclosed, reasoned event, never silent; and
  budget pressure never justifies dropping mandatory context."* **All four
  fixtures satisfy that posture** — each discloses, each reasons, none trims.
  Measured against the only rule that has any prospect of binding, the breach
  set is compliant.
- **The honest name for these objects is *disclosures*, not waivers.** Three of
  the four already use the weaker word in their headings ("Above the
  justification trigger — disclosed", "Above the decomposition trigger —
  disclosed"); only fixture 8 says "waiver". [Inferred] Fixture 8's heading
  should say what the other two say.

**Recommendation (marked as recommendation, not finding):** the fields I supply
should be placed as *disclosure* fields, and the word "waiver" should not appear
in any fixture until a rule exists to be waived. If the owner later installs
CC-BUDGET-1, these four disclosures convert to waivers at that moment and
**every expiry trigger above must be re-evaluated then**, because each was
written against a posture rather than a rule.

---

## 6. Is 20,000 the right instrument? (Recommendation, not finding)

**Marked as a recommendation throughout.** RFC11-11 §8 q1 already reserves this
figure's custody to the owner; what follows is input to that open question.

**The trigger is not the broken instrument. The default band is.** Measured this
session over all nine fixtures:

| Instrument | Fires on | Rate |
|---|---|---:|
| Default band, 5,000–15,000 tokens | fixtures 1,2,3,5,6,7,8,9 miss it; only 4 is inside | **8 of 9 miss** |
| Trigger, 20,000 tokens | fixtures 2,7,8,9 | 4 of 9 |

A band that eight of nine hand-authored, best-effort, independently-reviewed
packets miss is not discriminating good selection from bad — it is reporting
that the corpus is bigger than the band was written for. And the cause is
mechanical, not editorial:

- RFC-0001 is 8,342 words = **11,261 est. tokens**, indivisible.
- The corpus's own declared module ceiling is ~7,000 words ≈ **9,450 est.
  tokens**; CG-8 reports **eight** artifacts over a §11.4 trigger this session,
  including `RFC-0003/governance-homes` at 4,407 w and
  `RFC-0007/narrative-contract` at 5,165 w.
- Therefore a packet of *one indivisible kernel + one package index + one
  module* — the smallest realistic governed selection — is already ~18,000–25,000
  tokens. **The 5,000–15,000 band is unreachable by construction for any
  kernel-touching task.**

**By contrast the 20,000 trigger performed well in this review.** It fired on
exactly the four packets where I had something substantive to say, and stayed
silent on the five where I did not. That is what a trigger is for.

**Recommendation, in two parts:**

1. **Keep the 20,000 trigger; replace the 5,000–15,000 default band.** The band
   should be derived from the corpus's module granularity, not inherited. On
   this evidence a defensible default band is **12,000–22,000**, with the median
   observed packet (19,939) sitting inside it rather than 33% above it.
2. **Better, add a headroom instrument that measures what a selector can
   control.** Trigger a decomposition review when a packet exceeds its own
   **irreducible floor** — the sum of the indivisible mandatory units its
   warrant's clause set forces — by more than a stated margin. An absolute
   threshold measures corpus size, which the selector cannot change; headroom
   measures selection quality, which is the only thing a reviewer can act on.
   The evidence for this is the present review's own outcome: **all four
   breaching packets have near-zero headroom, which is exactly why all four
   rulings came out WAIVER SOUND.** An absolute-threshold instrument that fires
   four times and yields four "nothing to do" rulings is producing review load
   without producing decisions.

If part 2 is adopted, `context_load.py` would need to know which units are
indivisible — it currently has no such notion (fixture 9 is correct that the
script "has no notion of a task, a warrant, a risk class"). That is a real cost
and I name it rather than assume it away.

---

## 7. Exceptions carried into the verdict

**F-1 — Fixture 2 does not state the breach it committed.** It measures itself
against the load map's "15–20k working target" and never states that 24,680 is
23.4% above the §11.4 20,000-token trigger. It records **no waiver block**: none
of artifact, reason, scope, reviewer, or expiry appears in structured form. The
commission's premise that "every one of them records its reviewer as unassigned
or empty" is **not true of fixture 2** — it records no reviewer field at all,
because it records no waiver at all. This is the only breaching fixture in the
**accepted** set, and it has the weakest budget record of the four. §3.

**F-2 — Fixture 2 loads `RFC-0003/README.md` unnecessarily** (913 w ≈ 1,233 est.
tokens). Fixture 9 declines the identical file with reasoning I verified at
source (`governance-homes-and-owner-acts.md:6` resolves every RFC3-n; the
README's unique open questions belong to the excluded module; RFC-0003 has no
phase rule so RFC11-4 does not compel it). Removing it is a correction, not a
budget trim, and does not cure the breach (23,448). §3.

**F-3 — The set applies two incompatible readings of RFC11-4's phase-rule
rule.** RFC11-4 requires the governing phase-rule clause of every loaded
contract, "(the module or README text carrying it)". Fixture 2 relies on the
**permissive** reading — it loads `RFC-0008/README.md` and *not*
`accounting-reconciliation-and-release.md`, where RFC8-32's clause text actually
lives. Fixture 8 adopts the **strict** reading and pulls
`rendering-and-surface.md` precisely because "the README's phase-rule text is a
restatement pointing elsewhere." Both cannot be the rule. Under the strict
reading fixture 2's mandatory set grows by 3,051 words to **28,799 est. tokens**
and its waiver's reason no longer covers it. Which reading holds is not mine to
decide — see §8. The permissive reading is the textually supported one; the
inconsistency is the finding.

**F-4 — CG-18 re-measures one line per fixture, and the waiver blocks went
stale.** CG-18's regex anchors on `Measured:\s*\*\*([\d,]+)\s*words`, so it
verifies the headline word count and the digest and **nothing else**. A sweep
this session over every `NN,NNN tokens` figure in each fixture, compared against
the computed total, finds stale figures the check cannot see:

| Fixture | Location | States | Computes to |
|---|---|---:|---:|
| 6 | §15 checklist | 15,574 | 15,556 |
| 7 | breach heading | 21,285 | 21,246 |
| 7 | §15 checklist | 21,285 | 21,246 |
| 7 | decomposition option (a) | 19,554 | 19,515 |
| 7 | decomposition option (b) | 18,831 | 18,804 |
| 8 | breach heading | 30,048 | 30,026 |
| 8 | §15 checklist | 30,048 | 30,026 |
| 8 | split table, README-alone | 18,829 | 18,812 |
| 8 | split table, drop RFC-0001 | 18,771 | 18,765 |
| 8 | split table, drop narrative | 23,072 | 23,053 |

Every stale value is the pre-re-measurement figure. Fixtures 2 and 9 are clean
(fixture 2 carries no derived figures; fixture 9 was authored after the
re-measure and every one of its figures — 13,972, 30,088, 26,484, 29,991, 43,695,
43,228 — reproduces). **A waiver whose decomposition table reasons from numbers
that no longer hold is reasoning from stale evidence**, and this is the exact
defect class AGENTS.md names ("a derived value quoted outside its owning
artifact goes stale silently") appearing *inside* the owning artifact because the
check parses one line of it. The magnitudes are small (≤39 tokens); the
mechanism is not.

**F-5 — Fixture 9's declared Shard 1 is incomplete for its own warrant**, and it
is the fixture's load-bearing finding. The split cuts the RFC4-16 × RFC4-24
coupling that the warrant's third declaration depends on; neither declared shard
can emit `retention-horizon-passed`. The corrected complete shard measures
**18,943**, not 13,972. Verified against clause text in both modules. §3.
**F-6 — Three of the four breaching fixtures are stale at the working tree as of
this writing**, and the fourth check that would have caught it now FAILs.
Concurrent craft-policy edits (+46 w to `engineering-bar.md`, +163 w to
`testing-and-verification.md`) landed during this review, moving fixtures 7, 8
and 9 to 21,308 / 30,246 / 32,653 and invalidating their declared word counts and
digests; fixture 3's digest moved with **no** word-count change, which is the
silent-drift case and belongs to whoever owns the concurrent repair. This is not
a defect in the fixtures — it is the digest machinery working as designed, and
fixture 9 predicts it in terms (*"a stale digest is the correct, visible
outcome"*). It is carried as an exception because **the waiver fields in §3 must
not be placed until CG-18 is green again and the packets are re-measured**: a
disclosure whose Artifact field names a digest that no longer reproduces
documents a packet that no longer exists. §1.3.

---

## 8. Unresolved

**[Unknown] — Whether the owner intends `CC-BUDGET-*` ever to be installed.**
The knowledge-hygiene policy is candidate and is not among the five pending
acts. Nothing in the acceptance record or `PENDING-OWNER-DECISIONS.md` that I
read schedules it. If it is never installed, these four disclosures never become
waivers and the Reviewer field never acquires meaning.

**[Unknown] — What "reviewer" means in CC-BUDGET-3.** If it means an owner act,
no agent review can fill the field and my signature is a placeholder that a
future reader may misread as satisfaction of a gate. If it means an independent
review of the kind this document is, the field is filled. The clause does not
say, and I will not decide it — VIS-4 reserves that class of question. Whoever
places these fields should place my name with that ambiguity visible, not
resolved.

**[Unknown] — Which reading of RFC11-4's phase-rule inclusion is intended**
(F-3). It changes fixture 2's mandatory set by 3,051 words and it is a contract
question, not a budget question; RFC-0011 is candidate and cannot be cited to
settle it.

**[Unknown] — Whether `craft:testing-and-verification.md` is mandatory for a
labeling-only evidence-adapter warrant.** My judgment is no (RFC4-24's closed
cause list is that sub-task's classifier), which is what keeps fixture 9's
corrected Shard 1′ at 18,943 rather than 20,445. A reviewer who holds CC-TEST-2
mandatory there loses the split's only in-band half. I flag it because the whole
"a lawful shard exists" claim turns on a 445-token judgment call.

**Not assessed.** I ruled on selection size and necessity only. I did not verify
that each fixture's *task* is a realistic one, that its risk classification is
right, or that its omission register is complete against every candidate — those
are other commissions. I read no other RC-* review.

---

## 9. Verdict reasoning

For the set's budget discipline as a whole:

**What is sound.** Four of four breaches are honest. No packet is padded; the
one includable-but-unneeded item I found (F-2) accounts for 1,233 of 24,680
tokens in a single fixture and does not cure its breach. Nothing was trimmed to
fit a number anywhere in the set — I looked for it specifically and found the
opposite: three fixtures measured trims that would have brought them under and
declined each with a stated reason. The measurement machinery is trustworthy:
nine fixtures, four independent methods, zero disagreement, every declared digest
current **at `fc4632d`**. Fixtures 7, 8 and 9 conduct genuine decomposition reviews rather than
asserting that none exists, and fixture 9 goes further and measures an
alternative that argues against its own form — which is the behaviour the
epistemic discipline asks for.

**What is not.** Fixture 2 — the only accepted-set member in the breach set —
does not state the line it crossed, records no waiver fields at all, carries an
unneeded file, and rests on a phase-rule reading its sibling contradicts (F-1,
F-2, F-3). Three fixtures reason inside their waiver blocks from stale numbers
that the freshness check structurally cannot see (F-4). Fixture 9's central
decomposition finding is wrong as stated (F-5). Three of the four no longer
reproduce at the working tree, so the fields I supply cannot be placed until the
concurrent repair settles and CG-18 is green again (F-6). And all four are
measured against a threshold established in nothing binding, with a "reviewer"
role that no installed rule creates (§5).

None of that is fabrication, concealment, or trimming — the failures that would
force REJECT or REVISE. All of it is correctable by editing the fixtures,
extending one check, and re-measuring after the concurrent repair lands, with no
ruling disturbed: all four rulings stand as WAIVER SOUND regardless of how F-1
through F-6 are resolved, and they hold at both measured corpus states.

That is a set whose discipline is real and whose record has named, enumerated,
correctable defects.

VERDICT: EXCEPTIONS
