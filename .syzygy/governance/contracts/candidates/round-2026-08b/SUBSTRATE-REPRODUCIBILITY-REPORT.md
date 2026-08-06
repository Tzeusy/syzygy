# Substrate reproducibility — what Syzygy adopts by reference, and whether a clone can get it

> **Non-authoritative round record.** `../../../policies/GOVERNANCE-SUBSTRATE-LOCK.yaml`
> is the artifact that holds the pins; this file records how they were
> established and what checking them found. Where they disagree, the lock wins.

## The problem

Syzygy's owner-approved engineering policy adopts external material **by
reference**, most consequentially at
`policies/craft-and-care/README.md`: the `th-engineering` skill package —
its `engineering-bar` subskill (biases 1–9 and its Definition of Done), its
`test-rigor` bar (rules 1–8), and its `dependency-hygiene` bar (rules 1–7) —
is named as Syzygy's baseline engineering standard.

Until this round, that reference resolved to
`~/.claude/skills/th-engineering/subskills/` — a path on one machine. Every
reviewer who tried to read the adopted bar from a clone reported the same
thing: the standard Syzygy claims to hold itself to was **unreadable**.

Worse than unreadable, as it turned out: unreadable *and* moving.

## What was established

The substrate is public. `th-engineering` lives in
`https://github.com/Tzeusy/ai-bootstrap` (MIT), and the material craft-and-care
adopted can be pinned exactly. The lock now records, for each substrate: the
public repository, the commit, the commit date, the root path, the git tree
object id, and a sha256 per relevant file — each with the command that
recomputes it.

Five substrates are locked: `th_engineering`, `th_projects`,
`beads_orchestration`, `openspec`, and `beads`. A sixth block, `not_locked`,
names what is deliberately *not* pinned and why — including the founder
machine's `~/.claude/skills/**` symlinks, which are installation detail rather
than adopted content.

**Resolution rule for the pin date.** craft-and-care pins the bar "as read on
2026-07-30", which is a date, not a commit. No `ai-bootstrap` commit lands
between 2026-07-27 and 2026-07-31, so the text read on 2026-07-30 is exactly
the text at commit `61bd8fa` (2026-07-27). That is `[Inferred]` from commit
dates and is labelled so in the lock: the reading was never itself recorded
with a commit id, and no amount of care now can make it `[Observed]`.

## What checking the pin found

**The installed tree had moved two commits past what the owner approved, and
the difference is material.**

| Subskill | Pinned `61bd8fa` → installed `f4cf1c7` | Material? |
|---|---|---|
| `test-rigor` | **Numbered rules went from 1–8 to 1–10.** Two new: (9) suite tiering and targetability — every test maps to one tier, network only above unit, enforced mechanically; (10) governed growth — a test is worth adding only if it catches a bug no existing test catches. Rules 1 and 5 also gained text | **Yes** |
| `engineering-bar` | **Definition of Done gained an item** — "Test delta accounted". Biases 1–9 verified unchanged by diff | **Yes** |
| `dependency-hygiene` | byte-identical; rules 1–7 unchanged | No |

Both material changes land **inside** what D2 approved, not outside it:
craft-and-care adopted "rules 1–8" *by number*, so two rules now exist that
the owner never approved and that CC-TEST-* overrides were written against an
8-rule baseline; and the Definition of Done is explicitly named in the pin, so
a new DoD item is inside the adopted surface.

**The cluster's own rule was due to fire and did not.** `craft-and-care/README.md`
states: *"If the installed bar changes materially against that pin, this
cluster's overrides (registered in CC-BAR-1) are re-checked against the new
text and the conflict is surfaced to the owner, not silently absorbed."* The
change was material. It was not surfaced — because nothing mechanical could
see a founder-machine path, and so no check existed to fire.

That is the shape of the failure worth remembering: **the rule was correct and
unenforceable.** A reference that cannot be resolved from a clone cannot be
compared against anything, so a drift rule written over it is decorative.

## Disposition

The drift is recorded in the lock under `th_engineering.drift` with
`status: OPEN — surfaced to owner, not absorbed`, and as owner item **P-26**.
It is **not** absorbed, and this round did not re-pin. Absorbing it would mean
an agent deciding that two unapproved engineering rules now bind Syzygy, which
is the owner's call.

It bears on **act 2**, whose subject is craft policy text. It does not block
acts 1, 3, 4 or 5.

## What is now mechanical

`scripts/check_governance.py` **CG-19** parses the lock and evaluates eight
predicate families against every pin: population integrity, pin kind and its
required field set, object-id well-formedness, per-file digests and path
sanity, locator hygiene, forge-URL grammar, declared visibility, and drift
derived from the two revision groups and then compared against what the lock
asserts. Current result: **57 predicate evaluations, 0 findings** (recompute — the figure moves when either the pin set or the predicate set moves), with the
classified population printed separately as CG-19b so a pin cannot leave the
denominator quietly. Twenty-eight self-test fixtures cover it, four of them
negative.

**Its first version was very much weaker than this paragraph used to claim.**
It ran two predicates — "some URL-shaped token appears somewhere in the block"
and "if a `drift:` line exists, a status token appears somewhere in the pin" —
and a mutation sweep run against it returned `OK, 5 pins, 0 findings` with
every commit deleted, every digest deleted, a garbage commit id, a private
`visibility`, and a host rewritten to `.invalid`. It caught 2 of 13 defect
classes and both catches were defeatable. That is recorded here rather than
quietly fixed, because the check was cited as evidence in three artifacts
while it was near-inert (RC10-P).

`craft-and-care/README.md` now carries the machine path as *provenance for
where the text was read*, followed by a pointer to the lock — and states that
the lock records an open drift bearing on act 2.

## What this does not establish

- **The lock does not adopt anything.** It is a record. It cannot widen what
  the owner approved, and where it disagrees with an owner-approved policy the
  policy wins.
- **CG-19 does not fetch, and its name no longer says it does.** It was
  called *"substrate pins publicly resolvable"* — a claim about the world that
  an offline check cannot make. It is now *"substrate pins complete and
  well-formed; drift consistent"*, which is a claim about the file. The
  identifier is unchanged: identifiers are amended in place, never renumbered.
  **A pin to a deleted repository at a fabricated commit passes by design**,
  and fixture `F6e` is kept in `--selftest` for the sole purpose of keeping
  that boundary executable rather than only written down. Verifying a pin
  against upstream remains a human step:
  `git cat-file blob <commit>:<path> | sha256sum`.
- **Seven of thirteen defect classes are now fully closed, four partly, one
  conditionally, and one is permanently out of reach offline** (whether the
  recorded digests match the bytes upstream). The partials are all the same
  shape: well-formedness and grammar are decidable offline, existence is not.
- **Drift detection is not continuous.** This drift was found by looking. The
  check will report a drift that has been *declared*; nothing yet notices one
  that has not.
