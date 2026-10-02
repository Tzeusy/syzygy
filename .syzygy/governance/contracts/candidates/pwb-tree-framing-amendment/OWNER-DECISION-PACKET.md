# Owner decision packet — Polaris's own framing as an abstraction tree, with supported diagrams

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. No phrase is offered. Sign-off is by version once a fresh review has
> confirmed the exact bytes (see "How it is signed").

Date: 2026-10-03. Gate bead: `syzygy-73e.9`, the last open child of the
prose-readability epic `syzygy-73e`.

Warrant: CC-REV-8 and the owner's 2026-09-28 tree-style rollout direction,
which cover documents but no code behavior; and the Polaris tree-form
amendment's "Interactions", which leaves diagrams on Butlers' page to this
package. Together they authorize drafting this delta only.

Manifest: `PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt`, eleven rows over the
signed PWB behavior subject. Five rows hash proposed bytes and six hash
current bytes. The builder writes the manifest, and any change to a patch,
the manifest or the subject retires a review of it.

## What you would be deciding

Whether PWB-REQ-014 should require Polaris's own words to open every group
with its answer, and to draw the relationships a diagram explains better, with
Butlers' words left verbatim.

Under the drafted text:

- every project-level category, project catalog, item detail and evidence
  group opens with one Syzygy-authored sentence, derived from the model,
  stating only what its children state under their weakest label, so
  stopping there still leaves a true account that is never more favourable;
- above Butlers text that sentence names which declared text follows, and
  never paraphrases or replaces the text; its state and route sit beside it;
- no opening counts anything, so the opening aggregate stays the only one
  before the first capability catalog;
- the independent rendered-design review lists the relationships a diagram
  explains better than prose, with their expected nodes and edges; one with
  at least one edge an Observed or Inferred claim supports is drawn, and one
  with none is disclosed in place and never drawn;
- every drawn node, edge and label is one model claim with its epistemic
  label, beside a text equivalent that also names each listed element left
  undrawn and its reason, with the same tuples in the machine view;
- diagrams are inline static SVG checked against an allow-list before
  emission, following your 2026-09-28 ruling that such SVG is inert under
  PWB-REQ-006; a failure emits no SVG and keeps the text.

Nothing reads a new source, and no generated draft reaches `/polaris`.

## Choices for you

| Question | Drafted arm | Other lawful arm |
|---|---|---|
| Where the rule lives | amend PWB-REQ-014; identity, title and requirement count unchanged | mint a new requirement, which moves the reading guide's table, the count and every coverage table |
| Who decides which diagrams are owed | the independent rendered-design review, as for the generator | a closed list in the spec (today: the capability's claim relationships and the precedence order), easier to test, stale as the model grows |
| Which groups open | every project-level category, project catalog, item detail and evidence group (about 32 today, Inferred) | only the top-level groups (eight today): fewer bytes, deeper groups still start on their first child |
| A failed diagram | no SVG, text equivalent kept, failure disclosed in place | fail the whole page as a final-output failure: stricter, and one figure blanks the page |
| Openings' source | derived from the shared model at render time | generator-authored prose, which needs a generator emission on `/polaris` that no act permits |
| How an opening shows a weaker child | the children's weakest label and the opening's scope; no opening counts | name Unknown and withheld counts: more specific, but each such opening becomes an aggregate owing PWB-REQ-007's full disclosure |
| A relationship whose only claimed edges are Unknown | not drawable; each edge disclosed with its reason | draw an all-Unknown figure: shows the expected shape, with no supported edge in it |

## Page size

Measured on 2026-10-03 at `main` (`a0d218a52eca8e10214401306fc88d7e06ddc7dc`),
`/polaris` is 1,467,147 bytes direct and 1,473,252 bytes on the tailnet form,
about 180 KB under your 1,650,000-byte working target [Observed]. The drafted
obligations should add about 30 KB per form [Inferred]; the machine JSON
sink is not measured [Unknown]. The implementation must measure both human
forms and the machine JSON before it merges.

## What remains outside the decision

- No wider content class, repository, consent, policy, registry or retention
  posture, and no change to PWB-REQ-006's text.
- No new claim, reason, tier, band or authority.
- No implementation authorization. A signed version authorizes no code; the
  implementation needs a fresh explicit authorization.

## Owner-visible consequences

1. The registry entry and the secret policy pin `spec.md`'s digest. A signed
   version stales both pins, as each earlier signed version did; this package
   does not repair them.
2. The dependency patch is generated over the current spec. A later amendment
   to the same files regenerates it and the manifest.
3. Coverage gains row 33; no contract coverage row changes.

## How it is signed

Sign-off is by version, under
`.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
once a fresh independent review of these exact bytes returns CONFIRM, or
CONFIRM WITH EXCEPTIONS with every finding a note, you are asked once whether
to sign off version 1.0. Nothing is performed until you say so, and replying
before then performs nothing. The recorder
`scripts/record_versioned_signoff.py` then proves every manifest row against
the tree after the patches are applied, applies the five patches in one
change, writes the record and tags the merged commit.

## Read-only checks

```text
python3 scripts/build_pwb_tree_framing_amendment.py --check
python3 scripts/build_pwb_tree_framing_amendment.py --selftest
python3 scripts/build_pwb_tree_framing_amendment.py --diff
```
