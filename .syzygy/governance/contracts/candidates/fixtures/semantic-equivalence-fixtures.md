# Semantic-equivalence fixtures — rev9 → rev10 (re-runnable)

The frozen rev9 corpus is included at `history/rev9-rfcs/` (nine files,
digests matching the rev9 acceptance record §3: `34f930c5…`, `3f57935c…`,
`90c1279d…`, `bb0fce86…`, `ebfe7401…`, `20bd414e…`, `2b94c3b7…`,
`74f59fde…`, `ceabc3e3…`), so every check below runs from the delivered
packet on any machine. Full per-clause accounting:
`04-CLAUSE-MIGRATION-MATRIX.md`. Run all commands from the packet root
**under bash or zsh with GNU grep** (F-EQ-2 uses process substitution;
F-EQ-8 uses GNU word boundaries).

## F-EQ-1 — RFC2-1's eleven snapshot inputs, verbatim and unrenumbered

```
grep -A40 'RFC2-1' history/rev9-rfcs/RFC-0002-*.md | grep -E '^[0-9]+\.' > /tmp/a
grep -A40 'RFC2-1' rfcs/RFC-0002/snapshot-and-evaluation-core.md | grep -E '^[0-9]+\.' > /tmp/b
diff /tmp/a /tmp/b   # expect: items 1-11 identical; trailing lines differ (the -A40 window also catches unrelated numbered lines past RFC2-1)
```
Pass condition: items 1–11 present in order, byte-identical, no
renumbering. (The removed `*(History:…)*` note sat inside item 11's body
and is not visible in this first-line capture; it is verbatim in
`history/RFC-0002-history.md`.)

## F-EQ-2 — RFC3-16(b)'s nine binding items

```
grep -c '' <(sed -n '/^\*\*RFC3-16(b)\. What an owner act binds/,/Bootstrap correlation/p' rfcs/RFC-0003/governance-homes-and-owner-acts.md | grep -E '^[0-9]+\.')
```
Pass condition: nine numbered items; spot-diff any item against
`history/rev9-rfcs/RFC-0003-*.md` — wording identical (item 9 retains
"always, under the A1 mechanism class").

## F-EQ-3 — the `supersedes` closed-pair rule (review-10-hardened)

```
grep -n 'Same-class pairs only' rfcs/RFC-0001-*.md history/rev9-rfcs/RFC-0001-*.md
```
Pass condition: present in both, byte-identical row text (the RFC-0001
pass verified its four tables byte-identical; this is the highest-risk
row).

## F-EQ-4 — RFC8-12/13: thirteen states, three partitions, derivation tables

```
for t in future planned ready active blocked review merged reconciled \
  closed-unmerged state-undetermined eligibility-undetermined \
  activity-undetermined stale-or-dead; do \
  grep -q "\`$t\`" rfcs/RFC-0008/state-vocabulary-and-cost.md || echo "MISSING $t"; done
```
Pass condition: no MISSING lines; RFC8-13's three tables cell-for-cell
identical to `history/rev9-rfcs/RFC-0008-*.md`.

## F-EQ-5 — RFC6-5's nine typed resolution outcomes

```
sed -n '/RFC6-5/,/RFC6-6/p' rfcs/RFC-0006-*.md | grep -c '^|'
sed -n '/RFC6-5/,/RFC6-6/p' history/rev9-rfcs/RFC-0006-*.md | grep -c '^|'
```
Pass condition: same table row count; row text identical.

## F-EQ-6 — RFC5-25's audit-trail location constraint

```
grep -n 'outside `.syzygy/\*\*` and outside the untrusted actor' \
  rfcs/RFC-0005/admission-and-boundary.md rfcs/RFC-0003/governance-homes-and-owner-acts.md
```
Pass condition: the constraint appears at binding strength in both homes,
wording preserved from rev9.

## F-EQ-7 — the one deliberate semantic resolution (must NOT be equivalent)

```
grep -n 'operative limit' rfcs/RFC-0008/accounting-reconciliation-and-release.md; \
grep -n 'operative limit' history/rev9-rfcs/RFC-0008-*.md history/RFC-0008-history.md
```
Pass condition: absent from the active module, present in rev9 AND in the
history record with the B13-supersession reasoning. This fixture exists so
the equivalence review confirms the change was deliberate, recorded, and
strictly-stricter — not a silent loss.

## F-EQ-8 — no live History parentheticals; no lost decision IDs

```
python3 scripts/verify_final_prespec.py    # includes the History-paren check
grep -o 'B13\|A8\|B19\|A1\b\|A5\b\|A9\b\|B9\b\|D1\b\|D2\b\|CC-TEST-2' -r rfcs/ | cut -d: -f2 | sort -u
```
Pass condition: verifier PASS; every listed decision ID appears somewhere
in the active corpus (each pass's full decision-census results are in its
`matrix-rows/` preamble).
