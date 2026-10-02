# Owner decision packet — a readable PWB specification

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. No phrase is offered. Sign-off is by version once a fresh review has
> confirmed the exact bytes (see "How it is signed").

Date: 2026-10-02. Gate bead: `syzygy-73e.5.5`.

Warrant: the owner's 2026-09-27 readability direction under `syzygy-73e`,
which authorizes drafting this successor only.

Manifest: `PWB-READABILITY-SUCCESSOR-MANIFEST.txt`, eleven rows over the
signed PWB behavior subject. Four rows hash proposed bytes and seven hash
current bytes. The builder writes the manifest, and any change to a patch,
the manifest or the subject retires a review of it.

## What you would be deciding

Whether the signed PWB specification, proposal and design should be replaced
by versions a newcomer can read, with the same requirements.

Under the drafted text:

- `spec.md` opens with a reading guide, marked non-normative, saying what the
  specification covers, how a requirement reads and that the file order is
  not numeric, with one flow diagram and a table of all 17 requirements;
- each requirement keeps its exact normative words, split into one paragraph,
  one bullet per sentence, or bullets under short bold labels; a
  `Verification` line then separates them from the unchanged case, oracle and
  falsifier bullets;
- every requirement identity, title, modal, scenario and warrant is
  unchanged, in the same order;
- the proposal and design are rewritten answer-first in the present tense.
  They now summarize the signed amendments each omitted (both: opening
  aggregate, project profiles, machine views; the proposal also item depth and
  render modes; the design also missing currency and dismissal), and they drop
  sentences that later acts made false (the proposal's "is a candidate and binds nothing" and the
  design's "remains inert until a later owner act").

`SEMANTIC-MAP.json` classifies all 120 units: every requirement and scenario
is `preserved`; 7 proposal, design and guide units are `clarified`; and 15
proposal and design units are `changed`. The changed units are the new
summaries and the two removals. All 15 are non-normative, and the package
claims no blanket equivalence.

## Choices for you

| Question | Drafted arm | Other lawful arm |
|---|---|---|
| Normative words | kept exactly; only layout and reading labels change, so long requirements stay long | reword requirements into plainer sentences, each then classified `clarified` or `changed` and reviewed requirement by requirement |
| Reading guide | inside `spec.md`, marked non-normative, before the reader definitions | keep `spec.md` free of a guide and put it in a separate unsigned page |
| Requirement order | file order kept (PWB-REQ-004 after PWB-REQ-007); the guide says so | renumber or reorder, which changes parser-stable form and every citer |
| Proposal and design history | summarize what is in force; route amendment history to the act record | keep each amendment's own history in the proposal |

The drafted arms keep this a structural change to the specification. The
"reword" arm reads better but needs a new package and review, because each
reworded requirement would need its own semantic classification.

## What remains outside the decision

- No requirement, scenario, warrant, modal or qualification change.
- No consent, policy, registry, retention or content-class change.
- No Butlers write, egress, observed-code execution, deployment or release.
- No implementation authorization. A signed version authorizes no code or
  body read; that needs a fresh explicit authorization.

## Owner-visible consequences

1. The observer registry entry and the secret policy pin a `spec.md` digest
   that is already stale before this package. A signed version moves
   `spec.md` again; this package does not repair the pins.
2. The sign-off change must also add one `VERSIONED_PWB_PACKAGES` row, one
   `VERSIONED_LATER` entry and one battery line, as the item-depth sign-off
   did. In a scratch clone with the patches applied and that entry added, the
   canonical battery passes except CG-7h, which waits for the row.
3. This restyle rewrites every requirement block. Any later PWB amendment is
   drafted over the restyled text; earlier packages' patches stay as history.

## How it is signed

Sign-off is by version, under
`.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
once a fresh independent review of these exact bytes returns CONFIRM, or
CONFIRM WITH EXCEPTIONS with every finding a note, you are asked once whether
to sign off version 1.0. Nothing is performed until you say so, and replying
before then performs nothing. The recorder
`scripts/record_versioned_signoff.py` then proves every manifest row against
the tree after the patches are applied, applies the four patches in one
change, writes the record and tags the merged commit
`pwb-readability-successor-v1.0`.

## Read-only checks

```text
python3 scripts/build_pwb_readability_successor.py --check
python3 scripts/build_pwb_readability_successor.py --selftest
python3 scripts/build_pwb_readability_successor.py --diff
```
