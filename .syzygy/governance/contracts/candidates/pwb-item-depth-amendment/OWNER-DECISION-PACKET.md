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
PWB behavior subject. Five rows hash proposed bytes and six hash current
bytes.

Manifest SHA-256:
`d46444901790955fa483f156e017d8014983a2bb2f1d51b4ed9b5f957b323771`

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
- one or more captured declared relations that do not exclude one another make
  that claim Observed over the whole set, and each related current intent
  renders verbatim; no declared relation makes it Unknown with
  `missing-declaration`; mutually exclusive relations make it Unknown with
  `contradicted-pending-adjudication`; each keeps its resolution route. A label,
  basename, similarity or generated prose never makes a relation;
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
| Compatible plural relations | one Observed relation over the whole set, every related intent verbatim | classify every plural population as a contradiction, which needs a governing invariant making the relation functional |
| Proposal scope | matching declared capabilities only, as PWB-REQ-013 requires | amend PWB-REQ-013 in a separately owner-scoped change before widening |
| Location | specify semantic item selection and leave the incidental URL to implementation | require a particular observable route shape |
| Existing capability | reuse the matching item detail and identity | retain a second capability-only detail, which needs a duplication rationale |

Three points the drafted text leaves open, stated so a reviewer does not have
to find them (`SEMANTIC-DELTA.md`, "Open points for the owner"): whether an
Observed relation stays Observed when PWB-REQ-011's gates leave the exact text
Unknown; which currency class the relation claim belongs to, since a class with
no effective bound renders Unknown under PWB-REQ-007; and the compatible-set
arm above. None changes the drafted bytes unless you rule on it, and a ruling
that changes them goes back to review.

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
   RFC7-17 and RFC7-26 are reworded to the item scope. No row changes status.

## How it is signed

Sign-off is by version, under
`.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
once a fresh independent review of these exact bytes returns CONFIRM, or
CONFIRM WITH EXCEPTIONS with every finding a note, you are asked once whether
to sign off version 1.0. Nothing is performed until you say so, and replying
before then performs nothing. The recorder
`scripts/record_versioned_signoff.py` then proves every manifest row against
the tree after the patches are applied, applies the five patches in one
change, writes the record and tags the merged commit. The retained phrase, for
governance checks only:

`SIGN OFF PWB ITEM-DEPTH AMENDMENT: d46444901790955fa483f156e017d8014983a2bb2f1d51b4ed9b5f957b323771`

## Read-only checks

```text
python3 scripts/build_pwb_item_depth_amendment.py --check
python3 scripts/build_pwb_item_depth_amendment.py --selftest
python3 scripts/build_pwb_item_depth_amendment.py --diff
```
