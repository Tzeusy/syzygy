# Process glossary

> **Navigation, never authority.** This page defines the vocabulary this
> repository uses to talk about *its own process* — how a document becomes
> binding, who may make it so, and what the shorthand identifiers mean. It
> defines no product term, adopts nothing, and binds nothing. Where this page
> and an owning record disagree, **the owning record wins and this page is
> stale.** For every claim below about current wave, gate or launch state, that
> owning record is [`PROJECT-STATUS.md`](PROJECT-STATUS.md) — named here rather
> than left implicit, so a reader who suspects a sentence has gone stale knows
> where to check without first working out who owns the answer.
>
> Two other glossaries exist and this one replaces neither:
>
> | For | Go to |
> |---|---|
> | Adopted product/doctrine terms | [`doctrine/README.md`](.syzygy/governance/doctrine/README.md#glossary-read-first) — **adopted**, seven entries |
> | The wider working product vocabulary | [`TERM-REGISTRY.md`](.syzygy/governance/contracts/candidates/policy-candidates/TERM-REGISTRY.md) — **candidate** |
> | How this repository's process works | this page |
>
> Written 2026-08-13 to close review finding RD-50 f8: seven process terms
> were used on the default reading path before anything defined them.

## The lifecycle of a document

These four words are not synonyms, and the difference between them is the
single thing most worth understanding here. They describe **increasing force**,
and a document at one level must never be described using a word from a
higher one.

| Word | Means | Who makes it so |
|---|---|---|
| **candidate** | Drafted and reviewable. **Binds nothing.** May be discussed, may not be cited as authority. Most of this repository is here | anyone |
| **confirmed** | An independent fresh-context reviewer examined the exact bytes and returned `CONFIRM`. Says the bytes are *ready to be offered* — **still binds nothing** | a reviewer |
| **accepted** | An owner **act** was performed on it. It is now binding authority | the owner, and only the owner |
| **recorded** | An owner **decision** was written down. Binding, but not digest-bound — no ceremony phrase, no argument | the owner |

**Confirmed is not accepted.** This is the distinction a newcomer most often
collapses: a `CONFIRM` verdict says the bytes are ready to be offered, and an
act is a separate thing that only the owner does. Confirmation of Waves A and
B did not make them binding — the two acts performed on 2026-08-17 did, and
each was a separate transaction after the review. Which artifacts are accepted
today is owned by `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` and
summarised in `PROJECT-STATUS.md`; read those, not this page, for status.

*Superseded, dated:* until 2026-09-05 this paragraph ended "Waves A and B are
both *confirmed* today and **neither is accepted**; no owner act has been
performed in this repository at all." That was true when written and stopped
being true on 2026-08-17.

## Acts, arguments, offers

- **act** — a formal owner transaction that changes what is binding. An act
  has an exact **ceremony phrase** the owner types, and an **argument**. Only
  the owner performs acts (doctrine VIS-4). Acts have been performed here, and
  `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` — created by the
  first of them — is the append-only record of every one. This page defines
  the word; it never says which acts exist. *(Until 2026-09-05 this entry read
  "No act has been performed yet; `decisions/ACCEPTANCE-ACT-RECORD.md`
  therefore does not exist, and that absence is correct rather than a gap" —
  correct when written, false from 2026-08-17 onward.)*

- **argument** — the exact bytes an act binds, identified by a `sha256`
  digest. For a wave act the argument is the digest of that wave's **whole
  manifest file** — four generated header lines plus one digest row per
  module. A change to a file that is not in the manifest moves no accepted
  byte. **But the header names the acceptance phrase**, so renaming the phrase
  regenerates the argument and retires the confirmation without touching any
  module. *(Corrected 2026-08-13, RD-54: the shorter form of this rule — "the
  ceremony is in no manifest, so a ceremony change costs nothing" — was false
  in exactly that case.)*

- **offer** — presenting a prepared act to the owner for a yes/no. Preparing
  an offer is not performing it. An act can be *confirmed and unoffered* —
  Wave A spent a week in exactly that state while the P-33 install-shape
  decision withheld its offer (`PROJECT-STATUS.md` owns the current state).

- **wave** — one batch of contract modules accepted by one act. There are six
  (A, B, C1, C2, D1, D2). Waves A and B are the launch path; C1/C2/D1/D2 are
  **deferred** — candidate, not accepted, not used by the launch target, and
  excluded from default task routing.

- **retire / survive** — what happens to a *confirmation* when bytes move. If
  an act's argument regenerates, the review that confirmed the old argument
  no longer covers anything and is **retired**; otherwise it **survives**.

## Identifiers

Identifiers are amended in place or retired — **never renumbered**.

| Form | Is | Example |
|---|---|---|
| `P-nn` | An open **owner decision**, queued in `PENDING-OWNER-DECISIONS.md`. A question only the owner may answer | `P-41` — the specification-acceptance craft act |
| `RD-nn` | A **review**. Raw reviewer output, stored verbatim and never edited | `RD-49` — the P-33 review |
| `VIS-n`, `SEC-n` | An adopted **doctrine** rule. Binding since 2026-07-30 | `VIS-2` — no evidence means Unknown |
| `SDR-n` | A prior recorded owner **decision** | `SDR-9` |
| `CC-*` | An owner-approved **craft policy** clause | `CC-REV-3` |
| `RFCn-m` | Clause *m* of candidate contract RFC-000*n* | `RFC3-15` — the governance category rules |
| `D1`, `D2`, `D3` | A **doctrine amendment**. D1 and D2 are in force; D3 is a candidate | |
| `CG-nn` | A check inside `check_governance.py` | `CG-15` |
| `round-YYYY-MMx` | One work pass, with its own reviews and reports. Historical once superseded | `round-2026-08g` |

`D1`/`D2` as doctrine amendments and `D1`/`D2` as deferred waves are
different things that share a spelling. Context distinguishes them; nothing
else does.

## The launch gate

- **launch gate** — a fixed question set (`A1…G1`) asking whether this
  repository is ready for anyone to author its first specification. It is an
  **instrument**: it judges, and it authorizes nothing.

- **administration** — one run of the gate against the corpus, producing a
  record. The record is **structured JSON**; the human-readable Markdown
  report is *generated from it and never read back as authority*.

- **formal administration** — an administration that may be cited as launch
  evidence. It must be run in **fresh context**, by someone who is not an
  authoring session of this repository, preferably outside the corpus
  authors' model family. Which administrations have been run, and what each
  returned, is a status question this page does not own: the launch-path
  table in `PROJECT-STATUS.md` owns it, and the records live under
  `.syzygy/governance/decisions/launch-gate/`. The 2026-08-09 run was a
  **pilot**, not a formal administration, and is steering evidence only.

  *Superseded, dated:* until 2026-09-05 this entry read "**None has ever been
  run.** The only administration on record is the 2026-08-09 pilot, which
  returned `NOT READY`." That was true when written and stopped being true on
  2026-08-18, when Administration 1 was performed out-of-family in fresh
  context — an administration whose own strongest findings were stale
  current-state claims on the default path, of which this sentence was one.

- **E1…E6** — the six readiness questions in the gate's section E, the
  section that asks the gate's actual question. Abbreviated constantly:

  | | Asks |
  |---|---|
  | **E1** | Is it defined what a specification *is* here — form, home, granularity, acceptance authority, change process — before the first one is written? |
  | **E2** | Is the first specification identified, with every prerequisite satisfied or explicitly waived? |
  | **E3** | Would authoring the first spec force reopening any vision- or shape-level question? *The sharpest single gate — an empty list is the readiness signal* |
  | **E4** | Is the shape/spec boundary crisp enough that an author knows which side a sentence falls on, without asking? |
  | **E5** | Do acceptance criteria exist for a specification itself? |
  | **E6** | Is there a defined propagation path for a shape change *after* specs exist? |

  `A`–`D`, `F`, `G` cover problem and vision, decomposability, spec-driven
  discipline, comprehensibility, process health, and the gate's scrutiny of
  itself.

- **`READY` authorizes nothing.** It is evidence the owner may weigh when
  making a separate launch decision.

## Review vocabulary

- **verdict words** are a closed set and are **copied exactly**, never
  paraphrased: `CONFIRM`, `CONFIRM WITH EXCEPTIONS`, `REVISE`. "Pass with
  findings" is not a verdict and never substitutes for `EXCEPTIONS`.

- **fresh context** — the reviewer is given only the artifact, its governing
  references, and the acceptance criteria. No summaries, no prior verdicts,
  no "how it's going".

- **raw review lane** — the directories holding reviewer bytes verbatim
  behind a provenance banner. **Never edited**, including to fix an error the
  reviewer made; the register records the disposition instead.

- **disposition register** — where each finding's outcome is recorded, in the
  vocabulary `repaired` · `open` · `declined`. Never "acknowledged".

- **same-model-family** — the reviewer is the same model family as the corpus
  authors. Such a review **supports repair** and is never the formal launch
  administration. Every review obtained so far is same-family, and each one
  says so.

- **exact-package review** — a review bound to a specific digest. Editing the
  subject afterwards makes the review worth nothing, however small the edit.

- **semantic delta** — the document normative changes travel in. "Editorial"
  and "no semantic change" are reviewable claims, not exemptions.

## Epistemic labels

Used on substantive claims throughout, and load-bearing:

```text
[Observed]   measured, with the method and denominator available
[Inferred]   reasoned. An LLM assertion is always Inferred, never Observed
[Unknown]    no evidence — never rendered as green, never as zero
```

`Unknown` is a **result**, not a failure to produce one.

## Where to ask what

| Question | Owning record |
|---|---|
| What is this project? | [`README.md`](README.md), [`OVERVIEW.md`](.syzygy/intent/OVERVIEW.md) |
| What is the current gate state? | [`PROJECT-STATUS.md`](PROJECT-STATUS.md) |
| Has the owner decided X? | [`decisions/README.md`](.syzygy/governance/decisions/README.md) |
| What does this *product* word mean? | the two glossaries at the top of this page |
| How do I work in this repository? | [`AGENTS.md`](AGENTS.md), [`CONTRIBUTING.md`](CONTRIBUTING.md) |
