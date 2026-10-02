# Owner decision packet — every declared catalog item opens in depth

> **Inert draft.** This packet performs nothing. It records no act,
> authorizes no implementation and changes no signed byte. A commit, review,
> merged pull request, passing check, silence or general approval performs no
> act. The phrase and digest below are retained only so governance checks can
> detect drift; they are not offered. Sign-off is by version once a fresh
> review has confirmed the exact bytes (see "How it is signed").

Date: 2026-10-02. Gate bead: `syzygy-dov.14.2` (P-81 question 5).

Warrant: the P-81 question 5 ruling in
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
which authorizes drafting this amendment only.

Manifest: `PWB-ITEM-DEPTH-AMENDMENT-MANIFEST.txt`, eleven rows over the signed
PWB behavior subject. Six rows hash proposed bytes and five hash current
bytes.

Manifest SHA-256:
`4aff2dfa1fc4c8964dafebf9acec8adbd5baa01b4b58c1c7509e4cff995462f6`

The builder writes the manifest; this digest was computed from it by script.
Any change to a patch, the manifest or the subject retires it.

## What you would be deciding

Whether PWB-REQ-015 should cover every declared catalog item, where it covers
only the capability deep dive today.

Under the drafted text:

- every item in the declared `catalog-entry` population has one item detail,
  keyed by the item's existing stable claim identity; the population is not
  frozen at today's count. The capability deep dive is the detail for its
  matching item, not a second identity;
- every item detail keeps the existing three bands in the existing order:
  `argument` (non-normative framing that cannot create intent, authority or a
  capability), `contract` (captured governing identities and verbatim-reachable
  current text), and `reality` (only the one shared model);
- the contract band carries a separate **governing-intent relation claim**,
  identified by the item's identity and a fixed role, with its own complete
  tuple. It never changes or borrows the item's tuple;
- one or more captured declared relations, no two of which an admitted
  declaration names as mutually exclusive, make that claim Observed over the
  whole set, and each related governing identity reaches its verbatim current
  text through the exact-source route; no declared relation makes it Unknown
  with `missing-declaration`; any two exclusive relations make the whole
  population Unknown with `contradicted-pending-adjudication`, however many
  compatible relations it also holds; each keeps its resolution route. A
  label, basename, similarity, generated prose or precedence outcome never
  makes or resolves a relation;
- no extraction class admits a relation declaration today, so until a separate
  owner-scoped change admits a source every relation claim is the absent arm;
- a declared capability matches an item only by exact equality of declared
  keys; one matching no item or several gets no detail and no proposal
  rendering, and is disclosed Unknown;
- both channels carry the same item and relation tuples, and the
  catalog-to-detail-to-exact-source path keeps the item's identity and state;
  a URL, label, path or coordinate is never identity;
- proposal material renders only in a matching declared capability's detail,
  as PWB-REQ-013 requires; a non-capability detail renders none.

Nothing reads a new source: exact intent stays behind the existing exact-source
route and its gates.

## Choices for you

| Question | Drafted arm | Other lawful arm |
|---|---|---|
| Population | every declared `catalog-entry`, without freezing today's count | name a narrower closed population and return the delta to review |
| Unmapped item relation | separate Unknown relation claim with its reason and route; item tuple unchanged | keep such an item at catalog altitude only, with no detail |
| Compatible plural relations | one Observed relation over the whole set unless a declaration names two members exclusive, when the whole population is contradicted | classify every plural population as a contradiction, which needs a governing invariant making the relation functional |
| Relation source | none admitted: inert until a separate owner-scoped change admits a class and key and a currency bound | amend PWB-REQ-002 and PWB-REQ-004 in this delta, widening it beyond PWB-REQ-015 |
| Capability matching | exact declared-key equality; no or several matches get no detail and no proposal rendering | require a separate capability-to-item declaration, returning the delta to review |
| Failed gate behind a related intent | only that text is Unknown; the relation claim, asserting the declaration, is unchanged | make the relation claim Unknown too |
| Proposal scope | matching declared capabilities only, as PWB-REQ-013 requires | amend PWB-REQ-013 in a separately owner-scoped change before widening |
| Location | specify semantic item selection and leave the incidental URL to implementation | require a particular observable route shape |
| Existing capability | reuse the matching item detail and identity | retain a second capability-only detail, which needs a duplication rationale |

Four consequences of the drafted text, stated so a reviewer does not have to
find them (`SEMANTIC-DELTA.md`, "Open points for the owner"): the relation
claim is inert until a source is admitted and a bound is declared for its
class, so every item shows the absent arm meanwhile; the exclusion and
compatible-set arms above; a capability with no or several matching items loses
its deep dive and proposal rendering; and a failed gate leaves the relation
claim unchanged. None changes the drafted bytes unless you rule on it, and a
ruling that changes them goes back to review.

## What remains outside the decision

- No wider content class, repository, consent, policy, registry or retention
  posture.
- No new band class, capability inference, positive status or authority.
- No Butlers write, egress, observed-code execution, deployment or release.
- No implementation authorization. A signed version authorizes no code or body
  read; that needs a fresh explicit authorization.

## Owner-visible consequences

1. The registry entry and the secret policy pin `spec.md`'s digest. A signed
   version stales both pins; this package does not repair them.
2. The dependency patch is rebased on the current spec. A later amendment to
   the same files regenerates it.
3. Coverage row 18 is restated; contract coverage rows RFC7-13, RFC7-14,
   RFC7-17 and RFC7-26 are reworded to the item scope and the generated
   `CONTRACT-COVERAGE.md` summary moves with them (its repair-overlay digest
   only). No row changes status or count.

## How it is signed

Sign-off is by version, under
`.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
once a fresh independent review of these exact bytes returns CONFIRM, or
CONFIRM WITH EXCEPTIONS with every finding a note, you are asked once whether
to sign off version 1.0. Nothing is performed until you say so, and replying
before then performs nothing. The recorder
`scripts/record_versioned_signoff.py` then proves every manifest row against
the tree after the patches are applied, applies the six patches in one
change, writes the record and tags the merged commit. The retained phrase, for
governance checks only:

`SIGN OFF PWB ITEM-DEPTH AMENDMENT: 4aff2dfa1fc4c8964dafebf9acec8adbd5baa01b4b58c1c7509e4cff995462f6`

## Read-only checks

```text
python3 scripts/build_pwb_item_depth_amendment.py --check
python3 scripts/build_pwb_item_depth_amendment.py --selftest
python3 scripts/build_pwb_item_depth_amendment.py --diff
```
