> # Historical — round record, not a current offering
>
> **Do not read a digest here as an act argument.** Its term inventory and contradiction list C-1…C-6 are round 2026-08's; the digests it quotes are that round's. Current arguments
> come from `ACTIVE-CONTRACT-MANIFEST.txt` and
> `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, never from a round record.

# Term migration report — human-clarity refactor round, 2026-08-05

Companion to `../policy-candidates/TERM-REGISTRY.md` (candidate, binds
nothing). This report records **what deprecated or drifting vocabulary exists,
where, in what quantity, what replacement is recommended, and what was
deliberately not touched.**

> **No term was replaced, renamed, edited, or migrated anywhere in this
> repository during this pass.** The round charter is explicit that broad
> replacement waits on review of this report. Every "recommended replacement"
> below is a proposal for a later, separately reviewed pass.

Findings are numbered `TM-n`. The series continues the numbering of the prior
founder-local draft (`_bootstrap/knowledge-refactor/TERM-MIGRATION-REPORT-DRAFT.md`,
TM-1…TM-7), so **TM-1…TM-7 are that draft's findings and are not restated
here**; this report opens at **TM-8** and re-states only where it *corrects*
an earlier finding. Where it does, it says so and names the defect.

---

## 1. Method, and the two hazards it hit

### 1.1 Corpus, pinned

Every sweep below runs over one explicitly enumerated corpus of **71 tracked
or clone-visible active/candidate artifacts**:

| Group | Files |
|---|---:|
| Adopted doctrine — `.syzygy/governance/doctrine/*.md` | 6 |
| Craft-and-care — `.syzygy/governance/policies/craft-and-care/*.md` | 10 |
| Candidate contract modules — `.syzygy/governance/contracts/candidates/rfcs/**` | 32 |
| Owner decisions — `.syzygy/governance/decisions/*.md` | 5 |
| Front door — `README.md`, `AGENTS.md`, `CLAUDE.md`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.syzygy/intent/OVERVIEW.md` | 7 |
| Topology candidates — `.syzygy/map/topology-candidates/**` | 11 |
| **Total** | **71** |

**The counts are pinned, because the tree moved under them.** Other
workstreams of this round were editing the front door, the craft cluster, and
the topology bundle *while these sweeps ran*. Two observed effects: the corpus
grew from 70 files to 71 mid-pass, and one identical pattern
(`\bstate planes?\b`) scored **13** in an early run and **12** in the pinned
run. Every number in this report is therefore valid **only** against:

```text
HEAD          9e6f2f7db55c4ce672daf9636f1cf2ab664879c8
working tree  dirty (concurrent round edits)
corpus files  71
corpus sha256 21ff53b0ed543219a6ac26a21a694656e658421d8000afad676ad447ec6ed04c
as-of         2026-08-05T04:32:25+08:00
```

The digest is over the sorted `(path, bytes)` of all 71 files:

```sh
python3 -c "
import glob, hashlib
C = sorted(set(glob.glob('.syzygy/governance/doctrine/*.md')
 +glob.glob('.syzygy/governance/policies/craft-and-care/*.md')
 +glob.glob('.syzygy/governance/contracts/candidates/rfcs/*.md')
 +glob.glob('.syzygy/governance/contracts/candidates/rfcs/*/*.md')
 +glob.glob('.syzygy/governance/decisions/*.md')
 +glob.glob('.syzygy/map/topology-candidates/**/*.md', recursive=True)
 +[f for f in ['README.md','AGENTS.md','CLAUDE.md','PROJECT-STATUS.md',
               'CONTRIBUTING.md','SECURITY.md','.syzygy/intent/OVERVIEW.md']
   if glob.glob(f)]))
h = hashlib.sha256()
for f in C: h.update(f.encode()); h.update(open(f,'rb').read())
print(len(C), h.hexdigest())"
```

**Expect the digest not to match on re-run.** Re-computing it four minutes
after the pin already returned `ac817d5b4838df52…` over the same 71 files,
because a sibling workstream had written in the interval. **Re-running any
sweep against a different digest may legitimately yield different numbers, and
that is not a defect in either run.** A count in this report that disagrees
with a later count is evidence the corpus changed, not evidence one of them is
wrong — the same discipline RFC2-1 imposes on evaluations, applied to this
report.

**Line numbers cited below are as-of the pin and drift with every concurrent
edit.** Where a citation must survive, it quotes the text as well.

**Not swept**, and therefore invisible to every count here: `_bootstrap/**`
(git-excluded historical process material), `contracts/candidates/history/**`,
this round's own working files under `round-2026-08/`, `.github/`, `scripts/`,
and `.beads/issues.jsonl`. A term used only there scores zero below; that zero
means *absent from the active corpus*, never *absent from the repository*.

### 1.2 The commands, verbatim

**ugrep is this machine's `grep`**, and it silently matches nothing on some
pattern classes. Every count below was produced by **Python `re`**. Every
zero supporting a claim was re-checked by a **second method** (`grep -F`,
literal, which the repository's own hazard notes mark safe).

**Sweep A — whitespace- and emphasis-normalized phrase counts (primary).**
Run from the repository root:

```sh
python3 - <<'PY'
import re, glob
GROUPS = {
 "doctrine": sorted(glob.glob(".syzygy/governance/doctrine/*.md")),
 "craft": sorted(glob.glob(".syzygy/governance/policies/craft-and-care/*.md")),
 "rfc-candidates": sorted(glob.glob(".syzygy/governance/contracts/candidates/rfcs/*.md")
                        + glob.glob(".syzygy/governance/contracts/candidates/rfcs/*/*.md")),
 "decisions": sorted(glob.glob(".syzygy/governance/decisions/*.md")),
 "front-door": [f for f in ["README.md","AGENTS.md","CLAUDE.md","PROJECT-STATUS.md",
                            "CONTRIBUTING.md","SECURITY.md",".syzygy/intent/OVERVIEW.md"]
                if glob.glob(f)],
 "topology-candidates": sorted(glob.glob(".syzygy/map/topology-candidates/**/*.md",
                                         recursive=True)),
}
T = {}
for g, fs in GROUPS.items():
    for f in fs:
        T[(g, f)] = open(f, encoding="utf-8", errors="replace").read()

def ws(phrase):
    """Exact phrase, tolerating any whitespace (incl. newline) and markdown
    emphasis markers between words; optional trailing plural 's'."""
    return r"\b" + r"(?:\s|\*|_|`)+".join(re.escape(w) for w in phrase.split()) + r"s?\b"

PHRASES = ["source snapshot", "snapshot", "state plane", "desired state",
           "proposed state", "observed state", "inferred state", "execution state",
           "historical state", "observed implementation state",
           "desired plane", "proposed plane", "observed plane", "inferred plane",
           "execution plane", "historical plane", "observation record",
           "attention item", "autonomy envelope", "context packet",
           "evidence tier", "rendering tier", "epistemic label",
           "normalized state", "chain state", "work lifecycle",
           "governance lifecycle", "governance root", "project genome",
           "feature", "feature request", "status", "state", "done", "complete",
           "finished", "proof", "conflict", "source of truth", "passing",
           "compliant", "notification", "alert", "context window",
           "system prompt", "main repo", "primary repo", "tech debt",
           "audit log", "not applicable"]

print(f"{'phrase':30s} {'tot':>5s} {'files':>5s}  by-group")
for p in PHRASES:
    tot = fh = 0; per = {}
    for (g, f), t in T.items():
        n = len(re.findall(ws(p), t, re.IGNORECASE))
        if n:
            tot += n; fh += 1; per[g] = per.get(g, 0) + n
    print(f"{p:30s} {tot:5d} {fh:5d}  " + ", ".join(f"{k}={v}" for k, v in sorted(per.items())))
PY
```

**Sweep B — literal second method for every zero.** Run from the repository
root:

```sh
FILES=$(python3 -c "
import glob
c=sorted(set(glob.glob('.syzygy/governance/doctrine/*.md')
 +glob.glob('.syzygy/governance/policies/craft-and-care/*.md')
 +glob.glob('.syzygy/governance/contracts/candidates/rfcs/*.md')
 +glob.glob('.syzygy/governance/contracts/candidates/rfcs/*/*.md')
 +glob.glob('.syzygy/governance/decisions/*.md')
 +glob.glob('.syzygy/map/topology-candidates/**/*.md',recursive=True)
 +[f for f in ['README.md','AGENTS.md','CLAUDE.md','PROJECT-STATUS.md',
               'CONTRIBUTING.md','SECURITY.md','.syzygy/intent/OVERVIEW.md']
   if glob.glob(f)]))
print(' '.join(c))")
for p in "inferred state" "proposed state" "inferred plane" "four states" \
         "notification" "alert" "inbox" "context window" "system prompt" \
         "main repo" "primary repo" "tech debt" "audit log" "not applicable"; do
  echo "grep -ioF '$p' -> $(grep -ioF "$p" $FILES 2>/dev/null | wc -l)"
done
```

### 1.3 Hazard 1 — the prior draft's counts were scoped to the wrong phrase

**This is the defect this report exists to correct.** The prior draft's entry
for *Source snapshot* (its T-16) carried an occurrence count of **206**. That
number is a count of the bare word **"snapshot"**, not of the phrase **"source
snapshot"** the entry was about.

Corrected, over the pinned 71-file corpus, Sweep A:

| Phrase | Occurrences | Files |
|---|---:|---:|
| `source snapshot` (the term the entry names) | **27** | 16 |
| `snapshot` (bare — includes every occurrence of the above) | **235** | 40 |

The prior draft's 206 was a bare-`snapshot` count over a different 48-file
corpus, so it is not expected to equal 235; what matters is the ratio it stood
in to the phrase it was attached to. Against the 27 that phrase actually
scores, the figure overstated the term's presence by roughly **8×**.

The generalisable rule, and the reason every count in this report names its
exact pattern: **an occurrence count is a measurement of a pattern, not of a
concept, and it is only as scoped as the pattern that produced it.** Two
patterns that look interchangeable are not: this report's Sweep A counts an
optional trailing plural, so its bare-`snapshot` figure (235) legitimately
differs from a singular-only sweep of the same corpus (224). Neither is wrong;
quoting one under the other's name would be.

### 1.4 Hazard 2 — line wrapping makes phrases invisible (new, found here)

The corpus is hard-wrapped at ~76 columns and uses markdown emphasis inside
phrases. A naive phrase count therefore **misses every occurrence that
straddles a line break or carries a `**` in the middle**.

Concretely: `RFC-0001-project-graph-identity-state-planes.md` contains the
phrase *execution plane* at RFC1-28, written as `the **execution\nplane**`.
A literal-space pattern — and `grep -ioF 'execution plane'` — both score it
**zero**. Sweep A's whitespace-and-emphasis-tolerant pattern scores it **1**,
correctly.

Effect on the numbers, measured at the pinned corpus, isolating each cause:

| Pattern for *state plane* | Count |
|---|---:|
| `\bstate plane\b` — literal space, no plural | 1 |
| `\bstate planes?\b` — literal space, plural | 12 |
| Sweep A — normalized whitespace/emphasis, plural | **16** |

Two separate defects, and they must not be conflated: **plural handling**
accounts for 1 → 12, and **wrapping/emphasis** accounts for 12 → 16. Only the
second is the hazard this section names; the first is ordinary carelessness.
For `execution plane` the wrapping effect is total: literal-space plural
scores **0**, Sweep A scores **1**.

> **Method rule proposed for the checks battery:** any phrase sweep over this
> corpus must normalize whitespace and markdown emphasis. A literal-space
> sweep over hard-wrapped prose is a broken instrument, and its zeros are
> worthless.

All counts in §2–§4 below are Sweep A (normalized). Where a zero is
load-bearing it also carries its Sweep B result.

---

## 2. TM-8 — the six-plane vocabulary: what actually exists (P-16)

Sweep A, whole corpus:

| Charter's phrasing | Count | Corpus's own phrasing | Count |
|---|---:|---|---:|
| `desired state` | 13 | `desired plane` | 1 |
| `proposed state` | **1** | `proposed plane` | 1 |
| `observed state` | 11 | `observed plane` | 4 |
| `inferred state` | **0** | `inferred plane` | **0** |
| `execution state` | 12 | `execution plane` | 1 |
| `historical state` | 9 | `historical plane` | 1 |
| `observed implementation state` (doctrine's own) | 2 | `state plane` | 16 |

Zeros confirmed by Sweep B: `inferred state` → 0; `proposed state` → 0
(Sweep B's literal form finds 0; Sweep A's normalized form finds the single
occurrence, which is line-wrapped); `inferred plane` → 0.

**Observed.** Neither vocabulary is dominant. The corpus names the *dimension*
`state plane` (16) and then writes the individual plane names **bare**, inside
RFC1-22's table — which is why `inferred plane` and `desired plane` score near
zero while the Inferred and Desired planes are fully specified. The charter's
`<name> state` phrasing is what appears in doctrine and presentation prose.

**Observed.** The three/four-state phrasings are few and every one is
locatable:

| Site | Phrasing | Assessment |
|---|---|---|
| `doctrine/vision.md:19` | *"Three states are kept semantically distinct"* | **Adopted doctrine.** The thesis. Not drift. |
| `decisions/SURFACE-DECISION-RECORD.md:15` | *"desired state … observed implementation state … execution state"* | Owner-ratified restatement of the thesis. Not drift. |
| `.syzygy/intent/OVERVIEW.md:45` | *"(three-state thesis)"* as a source anchor, beside a six-plane diagram | Correct citation of doctrine. Not drift. |
| `rfcs/RFC-0008/README.md:29`, `identity-authority-materialization.md:28` | *"Serves: vision.md Thesis (three states…)"* | Citation of doctrine. Not drift. |
| `rfcs/RFC-0008/identity-authority-materialization.md:71` | RFC8-1: *"all three state planes relevant to work — desired, execution, [observed]"* | **Scoped**, and correctly so: three of the six are the ones work touches. Not a competing model. |
| `decisions/PENDING-OWNER-DECISIONS.md:50` | P-16: *"Canonicalize the six-plane state vocabulary over the older four-state phrasing"* | The open item itself. |
| `decisions/DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md:48` | *"vision.md three-state thesis"* | Citation. Not drift. |

`four states` → 0 (Sweep A **and** Sweep B). The register's phrase *"the older
four-state phrasing"* does not correspond to any four-state text in the active
corpus; the older phrasing that actually exists is **three**-state, in adopted
doctrine.

**Assessment.** There is **no term drift to repair here.** There is a
**compression relationship** between an adopted three-state thesis and a
candidate six-plane model, and every site above uses it correctly. What is
missing is not consistency but a **single place that states the relationship**
— which is what `TERM-REGISTRY.md` §2 now does.

**Recommended disposition.**

1. Adopt **six planes** as the registry's canonical vocabulary — done, §2.
2. Record the three-state thesis as a **compression, permitted in presentation
   prose**, not as a deprecated synonym. **Do not rewrite `vision.md`.**
3. **Correct the P-16 register wording** from *"the older four-state phrasing"*
   to *"the adopted three-state thesis"*, since no four-state phrasing exists.
   **Not done this round** — `PENDING-OWNER-DECISIONS.md` is another
   workstream's file (§5).
4. Prefer `<name> plane` in contracts and schemas; `<name> state` remains
   permitted in narrative. **No file was changed to conform.**

**This finding supersedes the prior draft's TM-1** in one respect: TM-1
proposed canonicalizing "plane" over "state" and flagged the mismatch as term
drift *requiring owner confirmation*. Located at their sites, the phrasings
are not drift; they are correct citations of two authorities at two altitudes.
The owner question that remains is narrower and is P-16 as re-worded above.

---

## 3. TM-9 — deprecated-synonym inventory

Sweep A over the pinned 71-file corpus. **"Occurrences" is not "violations"** — every
row's assessment was made by reading the sites, not by trusting the count.

| Deprecated / risky term | Occ. | Files | Recommended replacement | Assessment of actual sites |
|---|---:|---:|---|---|
| `feature` | 28 | 12 | **Capability** where an identity is meant | **No drift found.** 11 of 28 are RFC1-32's own no-Feature clause; 3 are RFC8's restatement; the remaining 14 use "feature" as ordinary English for a piece of functionality (*"a semantic-search feature"*, *"feature-plannable"*), never as an identity. `feature id` → **0** (Sweep A and B). SDR-1/RFC1-32 are being honoured. |
| `status` (bare) | 316 | 62 | Name the dimension (registry §1) | The **largest live risk**, and unresolvable by sweep: most occurrences are the lawful compound *status claim* (33) or *status evaluation*. A per-site audit is required before any replacement. Recommendation: no mass replacement; add a checks-battery rule forbidding a bare `status` **field/column/API key**, not a bare `status` **word**. |
| `state` (bare) | 693 | 63 | Name the dimension | Same shape, larger. Not actionable by sweep. |
| `done` / `complete` / `finished` | 34 / 48 / 5 | 12 / 23 / 3 | `reconciled@E`, or `closed-unmerged`, or *Converged* — per the dimension meant | RFC8-12 names `closed-unmerged` *"never `done`, `complete`, `finished`, or `resolved`"*. Craft carries 11 of the `done` occurrences as ordinary definition-of-done prose, which is lawful. Needs per-site review at surface specification, not now. |
| `proof` | 36 | 20 | *evidence*, or *gate-backed evidence* | Nearly all are doctrine's own *"work is never proof"* formula — lawful and load-bearing. No replacement recommended. |
| `conflict` | 22 | 16 | **Contradiction**, or the substrate's own word with the adapter naming which | RFC2-17 forbids translating a substrate's "conflict" into either Contradiction or gap without the adapter naming which one. Sites are mostly meta-prose ("no conflict found"), not substrate translation. Watch at adapter specification. |
| `source of truth` | 8 | 6 | *typed authority*, or name the authority | Doctrine states *"There is no single universal source of truth; authority is typed."* The phrase's continued use in prose invites exactly the collapse doctrine forbids. Recommend replacement at next edit of each site. |
| `passing` / `compliant` | 12 / 2 | 10 / 2 | **Aligned** (one subject, one claim, one evaluation) | **No misuse found.** `passing` is ordinary prose about tests passing. Both `compliant` sites were read: `architecture.md:175` is the Converged definition's own policy-compliance limb, and `performance-and-visual-discipline.md:85` means *conforming to the cited clause*. Neither is drift. |
| `notification`, `alert`, `inbox` | **0** | 0 | **Attention item** | Sweep A **and** Sweep B agree: zero. The Attention Item vocabulary is clean — nothing to migrate. |
| `context window`, `system prompt` | **0** | 0 | **Context packet** | Zero by both methods. Clean. |
| `main repo`, `primary repo` | **0** | 0 | **Governance root** | Zero by both methods. A pattern for `root repo` fires once, on `topology-candidates/01-system-context.md:24` — but the text there is the diagram label *"Governance-root repos"*, i.e. the **correct** term split by the hyphen. A false positive, not a usage. |
| `tech debt`, `backlog item`, `TODO` | 0 / 1 / 1 | — | **Gap**, or a work item | Effectively clean. The single `TODO` is `AGENTS.md:164`, in an instruction *against* markdown TODO lists — the opposite of drift. |
| `audit log`, `not applicable` | **0** | 0 | *Historical plane* / *Unknown* | Zero by both methods. Note `N/A` occurs 10× in candidate contracts — all in the lawful RFC6/RFC10 *"reviewed N/A judgment"* sense, which is a defined term of art, not an Unknown-avoidance. |

**Net.** Of the thirteen families checked:

- **Five score a verified zero by both methods** — `notification`/`alert`/
  `inbox`, `context window`/`system prompt`, `main repo`/`primary repo`,
  `audit log`/`not applicable`, `tech debt`. Nothing to migrate.
- **Four score non-zero but hold no drift once the sites are read** —
  `feature`, `proof`, `passing`/`compliant`, `N/A`. Every occurrence is either
  the clause deprecating the term or ordinary English. Nothing to migrate.
- **Two are real but small** — `source of truth` (8) and `conflict` (22).
  `source of truth` is the only family where per-site replacement is
  recommended at next edit.
- **Two are large and not migratable by pattern** — `status` (316) and `state`
  (693). These need a rule about **fields, columns, and API keys**, not a
  find-and-replace over prose.

**No mass replacement is recommended for this round in any family.**

---

## 4. TM-10 — the five-dimension vocabulary is used but never named

Sweep A:

| Dimension name as a phrase | Occ. | Files |
|---|---:|---:|
| `state plane` | 16 | 6 |
| `epistemic label` | 17 | 14 |
| `evidence tier` | **2** | 2 |
| `rendering tier` | 7 | 7 |
| `work lifecycle` | 15 | 11 |
| `governance lifecycle` | **1** | 1 |

**Observed.** Two of the five dimensions have essentially no name in the
corpus. The **evidence-tier** dimension is the corpus's most-cited closed
vocabulary (RFC2-25 is cited across the RFC set), and it is called
`rendering tier` in its own contract (7) and `evidence tier` almost nowhere
(2). The **governance-lifecycle** dimension — which decides whether an
artifact binds at all — is named **once** in 71 files.

**Assessment.** This is why "status" absorbs five meanings: three of the five
dimensions have no convenient name, so writers reach for the generic word. The
registry's §1 table is the proposed fix; it needs the names to be *used*.

**Recommended disposition.** Treat `rendering tier` and `evidence tier` as
**permitted aliases of one another** (recorded at registry T-16) rather than
renaming RFC2-25, which is digest-bound candidate material — renaming it would
invalidate its manifest entry for no semantic gain. Adopt `evidence tier` in
new public prose because it says what the dimension *is* rather than where it
shows up. **No file was changed.**

---

## 5. TM-11 — corrections to material this report was given

Three claims reached this workstream as background and did **not** survive
verification at source. Recording them because each would have propagated into
a candidate policy artifact.

**(a) The "class 5" artifact-classification scheme does not exist in any
tracked artifact.** The prior draft's header places the registry in *"derived
machine navigation (class 5)"*, citing `KA-9…KA-11` of
`_bootstrap/knowledge-refactor/KNOWLEDGE-ARCHITECTURE-CONTRACT-DRAFT.md`.
Verified:

```sh
# KA-n identifiers across all tracked files
git ls-files | while read f; do
  case "$f" in *.md|*.txt|*.yaml|*.py) n=$(grep -coE '\bKA-[0-9]+\b' "$f");
    [ "$n" != 0 ] && echo "$f: $n";; esac; done
# -> .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md: 1
```

The single tracked occurrence is inside P-10, which lists `KA-1…24` among the
pass's **unreviewed drafts**. The scheme lives only in git-excluded
`_bootstrap/**`. **The new registry therefore rests no argument on it** and
names lifecycle labels directly ("candidate", "adopted") instead. A separate
`grep -icE 'class[[:space:]]+5'` over tracked files returns exactly one hit,
in `craft-and-care/interfaces-and-dependencies.md`, where "class 5" is a
**review class** under CC-REV-1 — an unrelated scheme.

**(b) The craft clause families are CC-BAR, CC-DEP, CC-OBS, CC-PERF, CC-PROV,
CC-REV, CC-SEC, CC-TEST, CC-VIZ.** The list this workstream was given named
**`CC-INT`**; there is no such family. The interfaces-and-dependencies policy
numbers its clauses **`CC-DEP-1…6`**. Verified:

```sh
python3 -c "
import re,glob
f=set()
for p in glob.glob('.syzygy/governance/policies/craft-and-care/*.md'):
    f|=set(re.findall(r'\bCC-([A-Z]+)-\d+', open(p).read()))
print(sorted(f))"
# -> ['BAR', 'DEP', 'OBS', 'PERF', 'PROV', 'REV', 'SEC', 'TEST', 'VIZ']
```

The registry cites no CC clause, so nothing downstream was affected — but any
artifact citing `CC-INT-n` is citing a family that does not exist.

**(c) The prior draft's "zero unverified citations" claim.** The prior draft's
TM-4 claimed zero unverified citations while having examined only the three
rows it had already flagged; TM-7 then found six more. **The new registry does
not make a completeness claim about its citations.** Every clause quoted in it
was read in its source file during this pass; that is a statement about what
was done, not a proof that nothing was missed.

---

## 6. TM-12 — retired acceptance phrase still names the gate in one decision file

Sweep for the retired rev9 phrase across the corpus: **4 occurrences, 3
files.** Located:

| Site | Use | Assessment |
|---|---|---|
| `AGENTS.md:54` | *"The rev9 phrase `ACCEPT FOUNDATIONAL RFCS` is retired and satisfies nothing."* | Correct — a statement *about* the retirement. |
| `craft-and-care/INSTALL-RECORD.md:23` | Same, in the same form | Correct. |
| `decisions/OWNER-ANSWERS-2026-08-01.md:16` | *"They do not constitute `ACCEPT FOUNDATIONAL RFCS` — the gate remains open."* | **Uses the retired phrase to name the live gate.** |
| `decisions/OWNER-ANSWERS-2026-08-01.md:255` | *"The gate itself. `ACCEPT FOUNDATIONAL RFCS` has not been written…"* | Same. |

**Assessment.** Both `OWNER-ANSWERS-2026-08-01.md` sites are *historically
accurate* — the phrase was current when the answers were recorded on
2026-08-01 — and both make the correct substantive point (the gate is open).
They are nonetheless a reader trap: a newcomer reading the decisions directory
learns the wrong phrase for the live act.

**Recommended disposition.** Add a dated editorial note to that file pointing
to the current phrase, rather than editing the recorded answers. **Not done —
that file belongs to the decisions workstream, and editing an owner-answer
record is not this workstream's call.**

---

## 7. Files NOT modified — and why

This pass wrote **exactly two files**:

- `.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md` (new)
- `.syzygy/governance/contracts/candidates/round-2026-08/TERM-MIGRATION-REPORT.md` (this file)

**Nothing else in the repository was touched.** Specifically not:

| Not modified | Why not |
|---|---|
| All 6 adopted doctrine files | Adopted. Amendment is an owner act (VIS-4). The three-state thesis is correct as written (TM-8). |
| All 32 candidate contract modules | Digest-bound candidate material awaiting act 1. **An artifact edited after an act has bound its digest is an artifact with no act** — and re-offering act 1 requires a regenerated manifest. A vocabulary edit is not worth invalidating the acceptance package. |
| All 10 craft-and-care policies | Awaiting their own craft amendment act (P-2). |
| `decisions/PENDING-OWNER-DECISIONS.md` | The P-16 wording correction recommended at TM-8(3) belongs to the decisions workstream. |
| `decisions/OWNER-ANSWERS-2026-08-01.md` | An owner-answer record. See TM-12. |
| `README.md`, `AGENTS.md`, `PROJECT-STATUS.md`, `CONTRIBUTING.md`, `SECURITY.md` | Front-door workstream. |
| `.syzygy/intent/OVERVIEW.md` | Governed presentation artifact under its own refactor (P-13/P-4) and digest-bound at act 4. |
| `.syzygy/map/topology-candidates/**` | Digest-bound bundle awaiting act 3. |
| The prior founder-local drafts under `_bootstrap/**` | Read-only by charter. They remain as the historical record of what this pass corrected. |

**The registry is additive.** It introduces no obligation on any existing file
and requires no existing file to change in order to be correct.

---

## 8. Contradictions and tensions found between authorities

**Listed, not resolved.** None of these is this workstream's to settle.

**C-1 — Doctrine names three states; the candidate kernel names six planes.**
`vision.md` (adopted) keeps *three* states semantically distinct. RFC1-22
(candidate) assigns every source-state assertion to one of *six* planes.
Reconcilable as a compression (registry §2), and every site uses it correctly
(TM-8) — but the reconciliation itself is stated **only in a candidate
artifact**, so the compression reading is not itself adopted.

**C-2 — Eight of thirty foundational public terms have no adopted
definition.** State plane, Proposed state, Historical state, Evidence tier,
Mission, Autonomy envelope, Attention item, Context packet exist only in
candidate contracts. They are usable vocabulary and unusable authority. The
front door and the overview already use several of them.

**C-3 — "Claim" is not a doctrine-frozen noun.** `architecture.md`,
"Vocabulary" freezes thirteen technical nouns for stable citation; *claim* is
not among them, although RFC1-24 (candidate) makes the Claim the **sole
carrier of all positive status**. The most load-bearing noun in the candidate
kernel has no frozen doctrinal identity.

**C-4 — Bounded missions are specified but cannot lawfully operate.**
`vision.md` states Syzygy is *"not autonomous — the loop is human-triggered."*
RFC-0010 §2 (candidate) records this against itself: missions can be
*specified* under that contract but **cannot lawfully operate** under unamended
doctrine. The registry marks T-27/T-28/T-29 candidate and carries the note.
Resolution is owner act 5 (D3) or nothing.

**C-5 — `evidence tier` versus `rendering tier`.** RFC2-25 (candidate) titles
its own registry *rendering-tier*; the charter and downstream prose say
*evidence tier*. One dimension, two names, neither wrong (TM-10). Recorded as
aliases rather than resolved, because RFC2-25 is digest-bound.

**C-6 — Governance-category count.** `architecture.md` (adopted) names **four**
constitutional `governance/` categories and calls them *"constitutional
minimums"*. RFC3-15 (candidate) names **five** constitutional categories plus a
sixth reserved one, and calls the five *"closed except by recorded owner
widening"*. Compatible on a plain reading of "minimums", but the two describe
the same set with opposite closure language. Flagged for the contracts
workstream, not resolved here.

---

## 9. Open items

| # | Item | Owner |
|---|---|---|
| O-1 | **Fresh-reader review of the registry** (VIS-3). Thirty entries, none newcomer-tested. Charter §10 requires review before broad replacement, and §4 requires a fresh-context reviewer. | Review battery |
| O-2 | **The corpus was not swept for terms used normatively that are absent from this registry entirely.** This is the larger, unrun half of a lexical audit, and it is the reason the registry may not be called a validated vocabulary. Carried forward from the prior draft's TM-6, still unrun. | Next pass |
| O-3 | **Near-identical definitions across terms** — checking whether any two registry entries define the same thing twice — was not run systematically. | Next pass |
| O-4 | **Acronym first-use expansion** — not attempted; no acronym policy exists. | Next pass |
| O-5 | **`status` / `state` per-site audit** (TM-9). Not migratable by sweep; needs a rule about fields and API keys rather than prose. | Checks battery + surface specification |
| O-6 | **P-16 register wording** — *"older four-state phrasing"* names text that does not exist (TM-8). | Decisions workstream |
| O-7 | **`OWNER-ANSWERS-2026-08-01.md` retired-phrase note** (TM-12). | Decisions workstream |
| O-8 | **Whitespace-normalized phrase matching** must become the checks battery's standard (§1.4). Any existing check using literal-space phrase matching over this corpus is reporting false zeros. | Validation workstream |
| O-9 | **Registry-citation resolution check** — every registry entry cites an authority that resolves, and no entry lacks a citation. Proposed by the prior draft's TM-5; still not implemented as a check. | Validation workstream |
| O-10 | **Owner acts 1–5 gate eight of thirty terms** (C-2). Until then the registry's §5 coverage table is the honest statement of what may be cited as binding. | Owner |
