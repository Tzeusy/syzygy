#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Build and verify the inert PWB dismissal-expiry amendment package.

The signed PWB bytes are never edited while this package is a candidate.
Proposed bytes live as patches, and the manifest hashes the eleven-artifact
subject after those patches. Applying them is an adoption-time operation.

The package is drafted against the current tree, which already carries the
performed opening-band, render-mode, machine-view and missing-currency
amendments; lane B is declined. There is no sibling left to compose with.

What is pinned, exactly. The proposed spec.md is pinned whole: it must equal
the current spec.md with SPEC_EDITS applied inside PWB-REQ-007, byte for
byte. The rule tables only name which rule a drift broke, and their digest is
pinned. GOVERNING-DEPENDENCIES.md and CONTRACT-COVERAGE.md are regenerated and
compared byte for byte. proposal.md, CAPABILITY-COVERAGE.md and
CONTRACT-COVERAGE-REPAIR-DELTA.md are pinned only by named tokens (the
proposal bullet, row 32 and its totals, the thirteen repair rows) and
otherwise only by the manifest digest. The patch files' own bytes are not
pinned beyond what they produce.

**After sign-off, ``--check`` fails by design** (syzygy-gv2f, 2026-10-03). The
owner signed this package off as v1.0 on 2026-10-02
(``decisions/PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md``), and the
recorder applied its patches. They are deltas *to* the signed bytes, so the
first one applied (``CAPABILITY-COVERAGE.md.patch``) cannot apply a second
time, and this builder has no mode that recognises the applied state.
``--check`` therefore stops at "patch does not apply" from the sign-off commit
onward. That is not a defect. ``--selftest`` does not stop there: since
syzygy-tmkb it re-runs itself against the pre-adoption tree through
``scripts/pwb_signed_selftest.py`` (``rerun_before_signoff``) and passes. The
container-shape, item-depth, readability-successor and tree-framing sign-offs
then rewrote seven of the eleven subjects. This manifest now matches 4 of 11
and describes superseded bytes, so an applied-state mode would never fire
here. To check the bytes in force, run the builder of the latest sign-off in
the chain (``build_pwb_tree_framing_amendment.py --check`` as of 2026-10-03).
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHANGE = pathlib.Path("openspec/changes/polaris-project-wide-butlers-model")
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
CANDIDATE = CANDIDATES / "pwb-dismissal-expiry-amendment"
PROPOSED = CANDIDATE / "proposed"
MANIFEST_OUT = CANDIDATE / "PWB-DISMISSAL-EXPIRY-MANIFEST.txt"
TITLE = "PWB DISMISSAL-EXPIRY AMENDMENT MANIFEST"

SPEC = CHANGE / "specs/polaris-project-wide-butlers-model/spec.md"
DEPENDENCIES = CHANGE / "GOVERNING-DEPENDENCIES.md"
PROPOSAL = CHANGE / "proposal.md"
CAPABILITY_COVERAGE = CHANGE / "CAPABILITY-COVERAGE.md"
CONTRACT_REPAIR = CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md"
CONTRACT_COVERAGE = CHANGE / "CONTRACT-COVERAGE.md"

BEHAVIOR_SUBJECTS = tuple(
    sorted(
        (
            CHANGE / ".openspec.yaml",
            CHANGE / "CAPABILITY-COVERAGE.md",
            CHANGE / "CONTRACT-COVERAGE-REPAIR-DELTA.md",
            CHANGE / "CONTRACT-COVERAGE.md",
            CHANGE / "GOVERNING-DEPENDENCIES.md",
            CHANGE / "contract-coverage-matrix/RFC-0001-0003.md",
            CHANGE / "contract-coverage-matrix/RFC-0004-0006.md",
            CHANGE / "contract-coverage-matrix/RFC-0007-0009.md",
            CHANGE / "design.md",
            CHANGE / "proposal.md",
            CHANGE / "specs/polaris-project-wide-butlers-model/spec.md",
        ),
        key=lambda path: path.as_posix(),
    )
)
PATCHED = tuple(
    sorted(
        (
            CAPABILITY_COVERAGE,
            CONTRACT_COVERAGE,
            CONTRACT_REPAIR,
            DEPENDENCIES,
            PROPOSAL,
            SPEC,
        ),
        key=lambda path: path.as_posix(),
    )
)
ROW = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.MULTILINE)

REQUIREMENT = "### Requirement: PWB-REQ-007"
NEXT_REQUIREMENT = "### Requirement: PWB-REQ-004"
CASE = "- **Case (sweep)**"
PARAGRAPH_OPENING = (
    "A claim MAY carry the `dismissed-by-decision` sibling surface state, and only"
)
PRECEDING_SCENARIO = "#### Scenario: Missing current evidence remains explicit Unknown"
SCENARIOS = (
    "#### Scenario: A dismissal lapses only through a new evaluation",
    "#### Scenario: A dismissal replaces the rendering, never the facts",
    "#### Scenario: A record that no longer applies is lapsed or retired, never refused",
)
WARRANTS = "```yaml\nwarrants:"
# Each rule the new paragraph must state, compared after whitespace folding.
PARAGRAPH_RULES = {
    "attributed human decision": "an attributed human decision",
    "reason and expiry": "states a reason and an expiry instant",
    "governed-plane record": "is committed to the governed plane",
    "identified evaluation input": (
        "Every dismissal record present in the governed plane at an "
        "evaluation's snapshot is an identified input of that evaluation"
    ),
    "unreadable record set": (
        "When an evaluation cannot read that record set, or no governed-plane "
        "home for dismissal records is designated, it dismisses no claim and "
        "SHALL disclose its dismissed count and the count of each record class "
        "below as Unknown, never as zero"
    ),
    "Unknown-only scope": "Only a claim whose label is Unknown MAY be dismissed",
    "contradiction exclusion": (
        "never one whose primary reason is `contradicted-pending-adjudication`"
    ),
    "challenge exclusion": (
        "or `challenge-suspended`, which leaves only through its challenge's "
        "resolution"
    ),
    "no other dismissal source": (
        "Nothing else dismisses a claim: not a view preference, a query "
        "parameter, browser or daemon state, an owner note or a model assertion"
    ),
    # One rule, so the connectives between the three tests are pinned too.
    "in-effect conjunction": (
        "A dismissal is in effect at an evaluation only while all three hold: "
        "the evaluation carries the claim identity the record names, the "
        "evaluation's as-of instant is earlier than the record's expiry "
        "instant, and the claim's primary reason is the one the record "
        "dismissed"
    ),
    "as-of instant only": (
        "SHALL decide this from its own as-of instant and never from the "
        "instant a page or answer is read"
    ),
    "lapse by new evaluation": (
        "a dismissal lapses only through a new identified evaluation"
    ),
    "facts stay visible": (
        "replaces the claim's status rendering and never its facts"
    ),
    "every fact named": (
        "the claim's label, tier, primary and secondary reasons, resolution "
        "route, freshness, challenge state, claim identity and evaluation "
        "identity stay visible and unchanged"
    ),
    "same surface": (
        "on the same surface as the claim and without further disclosure"
    ),
    "human and machine parity": (
        "disclosure, identically in the human and machine views"
    ),
    "several records in effect": (
        "When more than one record is in effect for the same claim, each is "
        "disclosed that way beside the claim and the claim is counted once as "
        "dismissed"
    ),
    "no tuple change": "SHALL not change any tuple value",
    "never positive": "render as a positive, resolved, aligned or current state",
    "no favourable aggregate": (
        "count as resolved or favourable in any aggregate"
    ),
    "aggregate counts kept": (
        "Dismissed members SHALL remain in every per-label, tier, freshness "
        "and reason count of an aggregate"
    ),
    "aggregate expansion": (
        "SHALL additionally be counted and expandable as a sibling state"
    ),
    "three disclosed classes": (
        "is disclosed in exactly one of three classes, each distinct from the "
        "others and from a dismissal in effect"
    ),
    "class order": (
        "The classes are tested in order, refused first, then bound to a "
        "retired identity, then lapsed, and a record is disclosed in the first "
        "class whose test it meets"
    ),
    "refused records disclosed": (
        "It is a refused record when it lacks an author, reason, expiry "
        "instant, claim identity or dismissed primary reason"
    ),
    "refused by its own reason": (
        "or when it itself names, as the reason it dismisses, a primary reason "
        "that may not be dismissed"
    ),
    # Author authority is a test on the record itself (round-4 R2).
    "refused by its author": (
        "when it does not itself state that its author is a human, as with "
        "every record whose stated author is a model, agent or automated "
        "process, since the evaluation takes the author's kind from the "
        "record alone and never infers it"
    ),
    "refused by a malformed value": (
        "when its expiry instant is not a readable instant or its dismissed "
        "primary reason is not one of the closed Unknown reasons"
    ),
    "never refused by claim state": (
        "A record is never refused because of the state of the claim it names"
    ),
    "refused records placed": (
        "A refused record is disclosed among the evaluation's refused records "
        "with its record identity, the test that refused it and whatever "
        "author, reason, expiry instant and claim identity it states"
    ),
    "in effect only when Unknown": (
        "which only an Unknown claim can meet, since only an Unknown claim "
        "carries a primary reason"
    ),
    "lapse conditions": (
        "Otherwise it is a lapsed record when the evaluation's as-of instant "
        "is not earlier than its expiry instant, the evaluation does not carry "
        "the claim identity it names, or the claim's primary reason is not the "
        "one it dismissed, including because the claim is not Unknown or its "
        "primary reason is one that may not be dismissed"
    ),
    "lapsed records disclosed": (
        "A lapsed record is disclosed with its reason, expiry instant, author, "
        "record identity and the condition that lapsed it, beside the claim "
        "when the evaluation carries it and otherwise among the evaluation's "
        "lapsed records"
    ),
    "never-matched records": (
        "the condition names the test that failed and never states whether the "
        "record once took effect"
    ),
    # The evaluation's own record decides retirement, the same side of the
    # world as the lapse test for an identity the evaluation does not carry.
    "retired identity": (
        "Otherwise it is bound to a retired identity when the evaluation "
        "records the claim identity it names as retired by a split or merge; "
        "it is never transferred to a successor"
    ),
}
# Each rule a scenario's body must state, compared after whitespace folding.
SCENARIO_RULES = {
    SCENARIOS[0]: {
        "boundary evaluations": (
            "one evaluation's as-of instant falls before that instant and a "
            "second evaluation's as-of instant equals it exactly"
        ),
        "re-read unchanged": (
            "reading the first evaluation again after the expiry instant has "
            "passed renders the same claim state"
        ),
        "lapsed at the boundary": "discloses the record as lapsed",
        "no tuple change": "none of them changed by the dismissal",
    },
    SCENARIOS[1]: {
        "parity on the claim's surface": (
            "carry the same sibling state and the same complete tuple on the "
            "claim's own surface"
        ),
        "aggregate counts kept": (
            "keeps the claim in its per-label, tier, freshness and reason "
            "counts"
        ),
        "refused by its own reason": (
            "a record whose own dismissed primary reason is "
            "`contradicted-pending-adjudication`"
        ),
        "refused records": (
            "or `challenge-suspended`, each dismiss nothing and are disclosed "
            "among the evaluation's refused records"
        ),
        "refused by its author": "a record whose stated author is a model",
        "refused by a malformed value": (
            "a record whose expiry instant is not a readable instant"
        ),
    },
    SCENARIOS[2]: {
        "reason drift lapses": "is disclosed beside the claim as lapsed",
        "lapsed onto an undismissable reason": (
            "even when the claim's new primary reason is one that may not be "
            "dismissed"
        ),
        "retired by the evaluation's record": (
            "names a claim identity that the evaluation records as retired by "
            "a split or merge"
        ),
        "no transfer": "is never transferred to a successor",
        "neither carried nor retired": (
            "a third complete record names a claim identity the evaluation "
            "neither carries nor records as retired"
        ),
        "uncarried identity lapses": (
            "the third is disclosed as lapsed with the condition that the "
            "evaluation does not carry its claim identity"
        ),
        "never refused": "no record is disclosed as refused",
    },
}
# Each phrase a scenario's body must carry exactly once, so a second
# rendering claim for the same evaluation cannot be appended beside the first.
SCENARIO_ONCE = {
    SCENARIOS[0]: ("the first evaluation renders", "without the sibling state"),
}
# Wording that would let a dismissal act by reading time, leave the page,
# leave a count, come from another source or be refused by another route.
FORBIDDEN = {
    "clock": r"clock",
    "hide": r"\bhid(?:e|es|den|ing)\b",
    "collapse": r"collaps",
    "expire-on-read": r"expir\w*[- ]on[- ]read",
    "removal": r"\bremov\w*",
    "exclusion": r"\bexclu\w*",
    "second refusal route": r"refused record also|also (?:a )?refused",
    "permissive dismissal source": r"\b(?:MAY|SHALL|can|could)\s+dismiss\b",
    "uncounted member": r"\bnot (?:be )?counted\b",
    "claim-reason refusal": r"naming a claim whose primary reason",
    "refusal by an absent claim": r"refused[^.]*\bcarr(?:y|ies)\b",
    "two classes at once": (
        r"\b(?:lapsed|retired|refused) and (?:as )?(?:lapsed|retired|refused)\b"
    ),
}
# The selftest's total, fixed so that a rule removed from any table above
# fails the selftest instead of lowering its count.
EXPECTED_KILLED = 166
REQUIRED_WARRANTS = (
    "VIS-4", "VIS-6", "RFC1-12", "RFC1-20", "RFC1-25", "RFC2-1", "RFC2-15"
)
# The rule tables above name which rule a drifted paragraph or scenario
# breaks; they are not the guard on the bytes (SPEC_EDITS below is). Their
# digest is pinned so that a rule weakened, dropped or added in one place
# fails the selftest instead of passing with its own derived mutant.
RULE_TABLES_SHA256 = "cc34f7295b0a35aacb964af03dccd9946d538d84bc94f99936dc2be590c283c1"
# The whole proposed spec.md, pinned by construction: it must equal the
# current spec.md with each (anchor, replacement) pair applied once inside
# PWB-REQ-007, and every other byte of the file unchanged. Each anchor must
# occur exactly once in the current PWB-REQ-007 section.
SPEC_EDITS = (
    (
        """\
- **Case (sweep)**: enumerate every project entity, claim and aggregate across
""",
        """\
A claim MAY carry the `dismissed-by-decision` sibling surface state, and only
under a dismissal record: an attributed human decision that names the
dismissed claim's semantic Claim identity and the primary reason it dismisses,
states a reason and an expiry instant, and is committed to the governed plane.
Every dismissal record present in the governed plane at an evaluation's
snapshot is an identified input of that evaluation. When an evaluation cannot
read that record set, or no governed-plane home for dismissal records is
designated, it dismisses no claim and SHALL disclose its dismissed count and
the count of each record class below as Unknown, never as zero. Only a claim
whose label is Unknown MAY be dismissed, and never one whose primary reason is
`contradicted-pending-adjudication`, which leaves only by owner adjudication,
or `challenge-suspended`, which leaves only through its challenge's
resolution. Nothing else dismisses a claim: not a view preference, a query
parameter, browser or daemon state, an owner note or a model assertion. A
dismissal is in effect at an evaluation only while all three hold: the
evaluation carries the claim identity the record names, the evaluation's as-of
instant is earlier than the record's expiry instant, and the claim's primary
reason is the one the record dismissed, which only an Unknown claim can meet,
since only an Unknown claim carries a primary reason. The evaluation SHALL
decide this from its own as-of instant and never from the instant a page or
answer is read, so a dismissal lapses only through a new identified
evaluation. While a dismissal is in effect, the sibling state replaces the
claim's status rendering and never its facts: the claim's label, tier, primary
and secondary reasons, resolution route, freshness, challenge state, claim
identity and evaluation identity stay visible and unchanged beside the
dismissal's reason, expiry instant, author and record identity, on the same
surface as the claim and without further disclosure, identically in the human
and machine views. When more than one record is in effect for the same claim,
each is disclosed that way beside the claim and the claim is counted once as
dismissed. A dismissal SHALL not change any tuple value, render as a positive,
resolved, aligned or current state, or count as resolved or favourable in any
aggregate. Dismissed members SHALL remain in every per-label, tier, freshness
and reason count of an aggregate, and SHALL additionally be counted and
expandable as a sibling state. A record that dismisses nothing is disclosed in
exactly one of three classes, each distinct from the others and from a
dismissal in effect, identically in the human and machine views. The classes
are tested in order, refused first, then bound to a retired identity, then
lapsed, and a record is disclosed in the first class whose test it meets. It
is a refused record when it lacks an author, reason, expiry instant, claim
identity or dismissed primary reason; when it does not itself state that its
author is a human, as with every record whose stated author is a model, agent
or automated process, since the evaluation takes the author's kind from the
record alone and never infers it; when its expiry instant is not a readable
instant or its dismissed primary reason is not one of the closed Unknown
reasons; or when it itself names, as the reason it dismisses, a primary reason
that may not be dismissed. A record is never refused because of the state of
the claim it names. A refused record is disclosed among the evaluation's
refused records with its record identity, the test that refused it and
whatever author, reason, expiry instant and claim identity it states.
Otherwise it is bound to a retired identity when the evaluation records the
claim identity it names as retired by a split or merge; it is never
transferred to a successor, it is disclosed beside the retirement record, and
dismissing a successor needs a new record. Otherwise it is a lapsed record
when the evaluation's as-of instant is not earlier than its expiry instant,
the evaluation does not carry the claim identity it names, or the claim's
primary reason is not the one it dismissed, including because the claim is not
Unknown or its primary reason is one that may not be dismissed. A lapsed
record is disclosed with its reason, expiry instant, author, record identity
and the condition that lapsed it, beside the claim when the evaluation carries
it and otherwise among the evaluation's lapsed records; the condition names
the test that failed and never states whether the record once took effect, so
a record whose claim or reason never matched is lapsed under the same
condition as one whose claim or reason changed.

- **Case (sweep)**: enumerate every project entity, claim and aggregate across
""",
    ),
    (
        """\
  out-of-vocabulary and missing-currency cases.
- **Observable**: human and machine views expose identical complete tuples;
""",
        """\
  out-of-vocabulary and missing-currency cases, and dismissal records that
  are in effect, lapse at or after their expiry instant, outlive a change of
  the dismissed primary reason, name a claim identity the evaluation does not
  carry, share one claim, are bound to a retired identity, or are refused,
  including for an author not stated to be human or an unreadable expiry
  instant, and a record set that cannot be read.
- **Observable**: human and machine views expose identical complete tuples;
""",
    ),
    (
        """\
  zero invalid, missing or folded values decides.
- **Oracle independence**: the checker hard-codes the accepted vocabularies and
""",
        """\
  decide each dismissal record against each evaluation's own as-of instant
  with the checker's own statement of the rule; zero invalid, missing or
  folded values decides.
- **Oracle independence**: the checker hard-codes the accepted vocabularies and
""",
    ),
    (
        """\
  total, or an aggregate claims its own headline status.

""",
        """\
  total, an aggregate claims its own headline status, or a dismissal changes
  a tuple value, takes effect without a governed-plane record, lapses or
  persists by reading time rather than by evaluation, hides the dismissed
  claim's facts, leaves an aggregate's label, tier, freshness or reason
  counts, counts as resolved or favourable in an aggregate, or discloses a
  record that dismisses nothing in any class but the first, in the stated
  order, whose test it meets, or an unreadable record set yields a dismissed
  or record-class count of zero.

""",
    ),
    (
        """\
```yaml
""",
        """\
#### Scenario: A dismissal lapses only through a new evaluation

- **WHEN** a dismissal record for an Unknown claim states an expiry instant,
  one evaluation's as-of instant falls before that instant and a second
  evaluation's as-of instant equals it exactly
- **THEN** the first evaluation renders the claim `dismissed-by-decision`
  beside its unchanged tuple and the dismissal's reason, expiry instant,
  author and record identity, and reading the first evaluation again after
  the expiry instant has passed renders the same claim state
- **AND** the second evaluation renders the claim without the sibling state
  and discloses the record as lapsed, and each evaluation carries the tuple
  values it derives from its own snapshot and as-of instant, none of them
  changed by the dismissal

#### Scenario: A dismissal replaces the rendering, never the facts

- **WHEN** a dismissal is in effect for a claim
- **THEN** the human and machine views carry the same sibling state and the
  same complete tuple on the claim's own surface, and every aggregate keeps
  the claim in its per-label, tier, freshness and reason counts, counts it
  additionally as dismissed and never counts it as resolved or favourable
- **AND** a record without an author, reason or expiry instant, a record
  whose stated author is a model, a record whose expiry instant is not a
  readable instant, and a record whose own dismissed primary reason is
  `contradicted-pending-adjudication` or `challenge-suspended`, each dismiss
  nothing and are disclosed among the evaluation's refused records

#### Scenario: A record that no longer applies is lapsed or retired, never refused

- **WHEN** a complete dismissal record names a primary reason that is no
  longer the claim's primary reason at an evaluation, a second complete
  record names a claim identity that the evaluation records as retired by a
  split or merge, and a third complete record names a claim identity the
  evaluation neither carries nor records as retired
- **THEN** the first record dismisses nothing and is disclosed beside the
  claim as lapsed, with the condition that lapsed it, even when the claim's
  new primary reason is one that may not be dismissed
- **AND** the second record is never transferred to a successor and is
  disclosed as bound to a retired identity beside the retirement record, the
  third is disclosed as lapsed with the condition that the evaluation does
  not carry its claim identity, and no record is disclosed as refused

```yaml
""",
    ),
    (
        """\
  doctrine: [VIS-1, VIS-2, VIS-7]
  contracts: [RFC1-18, RFC1-19, RFC1-24, RFC2-9, RFC2-10, RFC2-23, RFC2-24, RFC2-25, RFC6-14, RFC6-17, RFC7-16, RFC7-33]
  policies: [CC-BAR-3, CC-BAR-4, CC-TEST-5, CC-TEST-6]
""",
        """\
  doctrine: [VIS-1, VIS-2, VIS-4, VIS-6, VIS-7]
  contracts: [RFC1-12, RFC1-18, RFC1-19, RFC1-20, RFC1-24, RFC1-25, RFC2-1, RFC2-9, RFC2-10, RFC2-15, RFC2-23, RFC2-24, RFC2-25, RFC6-14, RFC6-17, RFC7-16, RFC7-33]
  policies: [CC-BAR-3, CC-BAR-4, CC-TEST-5, CC-TEST-6]
""",
    ),
)
PROPOSAL_TOKEN = (
    "A claim that renders Unknown may carry a recorded, attributed human "
    "dismissal with a reason and an expiry, committed to the governed plane."
)
CAPABILITY_ROW = (
    "| 32 | Admit an attributed, reasoned, expiring governed-plane dismissal of "
    "an Unknown claim, decided at each evaluation's as-of instant, replacing "
    "the rendering and never the facts | covered — PWB-REQ-007 |"
)
CAPABILITY_TOTALS = (
    "Totals: 26 covered, 6 lawfully out of scope, 0 Unknown/unresolved; 32 total."
)
# The gap rows stay Unknown until the owner decides which gap a claim-level
# dismissal binds (packet question 4); unadopted-draft is a used state; and
# RFC1-12.r3 stays Unknown until the owner decides who may re-dismiss
# (packet question 3).
REPAIR_DISPOSITIONS = {
    "RFC1-12.r1": ("RFC1-12.c1", "covered:PWB-REQ-007"),
    "RFC1-12.r2": ("RFC1-12.c1", "believed-not-applicable"),
    "RFC1-12.r3": ("RFC1-12.c1", "unknown-uncovered"),
    "RFC1-20.r1": ("RFC1-20.c1", "unknown-uncovered"),
    "RFC1-25.r1": ("RFC1-25.c14", "unknown-uncovered"),
    "RFC1-25.r2": ("RFC1-25.c14", "believed-not-applicable"),
    "RFC2-1.r2": ("RFC2-1.c12", "unknown-uncovered"),
    "RFC2-1.r3": ("RFC2-1.c12", "covered:PWB-REQ-007"),
    "RFC2-15.r1": ("RFC2-15.c2", "unknown-uncovered"),
    "RFC6-14.r4": ("RFC6-14.c5", "covered:PWB-REQ-007"),
    "RFC6-14.r5": ("RFC6-14.c5", "unknown-uncovered"),
    "RFC6-14.r6": ("RFC6-14.c5", "unknown-uncovered"),
    "RFC6-17.r7": ("RFC6-17.c2", "covered:PWB-REQ-007"),
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fold(text: str) -> str:
    return " ".join(text.split())


def current_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
) -> dict[pathlib.Path, bytes]:
    overrides = overrides or {}
    values: dict[pathlib.Path, bytes] = {}
    for rel in BEHAVIOR_SUBJECTS:
        target = ROOT / rel
        if rel in overrides:
            values[rel] = overrides[rel]
        elif target.is_file():
            values[rel] = target.read_bytes()
        else:
            raise ValueError(f"missing amendment subject: {rel}")
    return values


def patch_files() -> list[pathlib.Path]:
    return sorted((ROOT / PROPOSED).glob("*.patch"), key=lambda path: path.name)


def apply_patches(base: pathlib.Path, patches: list[pathlib.Path]) -> None:
    for patch in patches:
        done = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", str(patch)],
            cwd=base,
            capture_output=True,
            text=True,
        )
        if done.returncode != 0:
            raise ValueError(f"{patch.name} does not apply: {done.stderr.strip()}")


def proposed_bytes(
    overrides: dict[pathlib.Path, bytes] | None = None,
    patches: list[pathlib.Path] | None = None,
) -> dict[pathlib.Path, bytes]:
    current = current_bytes(overrides)
    patches = patch_files() if patches is None else patches
    with tempfile.TemporaryDirectory() as scratch:
        base = pathlib.Path(scratch)
        for rel, body in current.items():
            (base / rel).parent.mkdir(parents=True, exist_ok=True)
            (base / rel).write_bytes(body)
        apply_patches(base, patches)
        return {rel: (base / rel).read_bytes() for rel in BEHAVIOR_SUBJECTS}


def scenario_body(text: str, heading: str) -> str:
    """A scenario's text from its heading to the next heading or warrants."""
    start = text.index(heading) + len(heading)
    stops = [at for at in (text.find("\n#### ", start), text.find("\n```yaml", start)) if at >= 0]
    return text[start:min(stops)] if stops else text[start:]


def forbidden_findings(where: str, text: str) -> list[str]:
    return [
        f"{where} uses forbidden {label} wording"
        for label, pattern in FORBIDDEN.items()
        if re.search(pattern, text, re.IGNORECASE)
    ]


def rule_tables_digest() -> str:
    tables = (
        PARAGRAPH_RULES, SCENARIO_RULES, SCENARIO_ONCE, FORBIDDEN,
        REQUIRED_WARRANTS,
    )
    return sha256(repr(tables).encode("utf-8"))


def expected_spec(base: str) -> tuple[str | None, list[str]]:
    """The current spec with SPEC_EDITS applied inside PWB-REQ-007 only."""
    start = base.find(REQUIREMENT)
    end = base.find(NEXT_REQUIREMENT, start)
    if start < 0 or end < 0:
        return None, ["current spec lacks PWB-REQ-007 or its following requirement"]
    section = base[start:end]
    findings: list[str] = []
    for anchor, replacement in SPEC_EDITS:
        if section.count(anchor) != 1:
            findings.append(
                "current PWB-REQ-007 does not carry the pinned anchor exactly "
                f"once: {anchor.splitlines()[0]!r}"
            )
            continue
        section = section.replace(anchor, replacement, 1)
    if findings:
        return None, findings
    return base[:start] + section + base[end:], []


def pin_findings(text: str, base: str) -> list[str]:
    want, findings = expected_spec(base)
    if want is None:
        return findings
    if text == want:
        return []
    got_lines, want_lines = text.splitlines(), want.splitlines()
    for number, (got, wanted) in enumerate(zip(got_lines, want_lines), 1):
        if got != wanted:
            break
    else:
        number = min(len(got_lines), len(want_lines)) + 1
        got = got_lines[number - 1] if number <= len(got_lines) else "<end>"
        wanted = want_lines[number - 1] if number <= len(want_lines) else "<end>"
    return [
        f"proposed spec differs from the pinned text at line {number}: "
        f"got {got!r}, want {wanted!r}"
    ]


def requirement_findings(spec: bytes, base: bytes | None = None) -> list[str]:
    """The proposed spec equals the pinned text; the rules name what drifted."""
    text = spec.decode("utf-8")
    if base is None:
        base = (ROOT / SPEC).read_bytes()
    findings = pin_findings(text, base.decode("utf-8"))
    start = text.find(REQUIREMENT)
    end = text.find(NEXT_REQUIREMENT, start)
    if start < 0 or end < 0:
        return findings + ["PWB-REQ-007 or its following requirement is missing"]
    section = text[start:end]
    if text.count(PARAGRAPH_OPENING) != 1:
        findings.append("missing or duplicate dismissal paragraph")
    else:
        opening = section.find(PARAGRAPH_OPENING)
        case = section.find(CASE)
        if not 0 <= opening < case:
            findings.append(
                "dismissal paragraph is not in the required PWB-REQ-007 position"
            )
        else:
            paragraph = fold(section[opening:case])
            for label, rule in PARAGRAPH_RULES.items():
                if fold(rule) not in paragraph:
                    findings.append(f"dismissal paragraph lacks {label}")
            findings.extend(forbidden_findings("dismissal paragraph", paragraph))
    preceding = section.find(PRECEDING_SCENARIO)
    warrants = section.find(WARRANTS)
    for heading in SCENARIOS:
        if text.count(heading) != 1:
            findings.append(f"missing or duplicate scenario: {heading}")
            continue
        at = section.find(heading)
        if not 0 <= preceding < at < warrants:
            findings.append(
                f"scenario is not in the required PWB-REQ-007 position: {heading}"
            )
            continue
        body = fold(scenario_body(section, heading))
        for label, rule in SCENARIO_RULES[heading].items():
            if fold(rule) not in body:
                findings.append(f"scenario lacks {label}: {heading}")
        for phrase in SCENARIO_ONCE.get(heading, ()):
            if body.count(fold(phrase)) != 1:
                findings.append(f"scenario does not say {phrase!r} exactly once: {heading}")
        findings.extend(forbidden_findings(f"scenario {heading}", body))
    block = section[warrants:] if warrants >= 0 else ""
    for authority in REQUIRED_WARRANTS:
        if not re.search(rf"[\[ ,]{re.escape(authority)}[\],]", block):
            findings.append(f"PWB-REQ-007 warrants lack {authority}")
    return findings


def dependency_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_spec_dependencies as generator

    rendered, errors = generator.generate(proposed[SPEC].decode("utf-8"))
    if errors:
        return [f"proposed warrants do not validate: {'; '.join(errors)}"]
    if rendered.encode("utf-8") != proposed[DEPENDENCIES]:
        return [
            "proposed GOVERNING-DEPENDENCIES.md differs from regeneration "
            "over the proposed spec bytes"
        ]
    return []


def companion_findings(proposed: dict[pathlib.Path, bytes]) -> list[str]:
    findings: list[str] = []
    proposal = proposed[PROPOSAL].decode("utf-8")
    capability = proposed[CAPABILITY_COVERAGE].decode("utf-8")
    repair = proposed[CONTRACT_REPAIR].decode("utf-8")
    if fold(PROPOSAL_TOKEN) not in fold(proposal):
        findings.append("proposal does not carry the dismissal obligation")
    if capability.count(CAPABILITY_ROW) != 1:
        findings.append("capability coverage does not carry row 32 exactly once")
    if CAPABILITY_TOTALS not in capability or "Population: 32 positive" not in capability:
        findings.append("capability coverage population or totals are not 32")
    for repair_id, (supersedes, disposition) in REPAIR_DISPOSITIONS.items():
        rows = [line for line in repair.splitlines() if line.startswith(f"| {repair_id} |")]
        if len(rows) != 1:
            findings.append(f"{repair_id} is missing or duplicated")
            continue
        cells = [cell.strip() for cell in rows[0].strip("|").split("|")]
        if cells[1] != supersedes or cells[-1] != disposition:
            findings.append(
                f"{repair_id} does not supersede {supersedes} as {disposition}"
            )

    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_project_wide_contract_coverage as coverage

    # The coverage generator checks each covered row against the spec's
    # warrants, which it reads from disk; this package changes those warrants,
    # so serve it the proposed spec bytes for that one path.
    spec_path = pathlib.Path(coverage.dependencies.SPEC).resolve()
    proposed_spec = proposed[SPEC].decode("utf-8")
    original_read = coverage.base.read

    def read(path: str) -> str:
        if pathlib.Path(path).resolve() == spec_path:
            return proposed_spec
        return original_read(path)

    coverage.base.read = read
    try:
        rendered = coverage.render(repair_text=repair)
    except ValueError as error:
        findings.append(f"contract-coverage repair does not validate: {error}")
    else:
        if rendered.encode("utf-8") != proposed[CONTRACT_COVERAGE]:
            findings.append(
                "proposed CONTRACT-COVERAGE.md differs from regeneration over "
                "the proposed repair delta"
            )
    finally:
        coverage.base.read = original_read
    return findings


def render(values: dict[pathlib.Path, bytes]) -> str:
    lines = [
        f"# {TITLE}",
        "# These rows bind only by the owner act that names this file's digest in",
        "# ACCEPTANCE-ACT-RECORD.md; until that act is performed they bind nothing.",
        f"# {len(BEHAVIOR_SUBJECTS)} artifacts; rows sorted by codepoint path.",
        "# All rows take effect together or none do.",
        "# Rows hash the PROPOSED bytes: current bytes with proposed/*.patch",
        "# applied. They match the tree only after --apply, the adoption step.",
    ]
    lines.extend(f"{sha256(values[rel])}  {rel.as_posix()}" for rel in BEHAVIOR_SUBJECTS)
    return "\n".join(lines) + "\n"


def verify_manifest(text: str, expected: str) -> list[str]:
    rows = ROW.findall(text)
    expected_paths = [path.as_posix() for path in BEHAVIOR_SUBJECTS]
    if [path for _digest, path in rows] != expected_paths:
        return ["manifest path population or order differs"]
    if text != expected:
        return ["manifest differs from exact regeneration over proposed bytes"]
    return []


def population_findings(patches: list[pathlib.Path]) -> list[str]:
    findings: list[str] = []
    if [patch.name for patch in patches] != [f"{path.name}.patch" for path in PATCHED]:
        findings.append("proposed patch population differs from declared subjects")
    try:
        proposed = proposed_bytes(patches=patches)
    except ValueError as error:
        return findings + [str(error)]
    current = current_bytes()
    for rel in BEHAVIOR_SUBJECTS:
        changed = proposed[rel] != current[rel]
        if changed and rel not in PATCHED:
            findings.append(f"undeclared subject change: {rel}")
        if not changed and rel in PATCHED:
            findings.append(f"declared patched subject is unchanged: {rel}")
    return findings


def check() -> list[str]:
    findings = population_findings(patch_files())
    try:
        proposed = proposed_bytes()
    except ValueError as error:
        return findings + [str(error)]
    findings.extend(requirement_findings(proposed[SPEC]))
    findings.extend(dependency_findings(proposed))
    findings.extend(companion_findings(proposed))
    target = ROOT / MANIFEST_OUT
    if not target.is_file():
        findings.append(f"manifest missing: {MANIFEST_OUT}")
    else:
        findings.extend(verify_manifest(target.read_text(), render(proposed)))
    return findings


def _fail(name: str) -> int:
    print(f"SELFTEST FAILED: {name}")
    return 1


def selftest() -> int:
    global MANIFEST_OUT, patch_files, proposed_bytes
    if len(BEHAVIOR_SUBJECTS) != 11 or len(set(BEHAVIOR_SUBJECTS)) != 11:
        return _fail("behavior subject is not eleven unique paths")
    proposed = proposed_bytes()
    spec = proposed[SPEC]
    if requirement_findings(spec) or companion_findings(proposed) or dependency_findings(proposed):
        return _fail("unmutated proposed bytes do not verify")
    killed = 0

    # Manifest: subject drift and row order.
    baseline = render(proposed)
    current = current_bytes()
    first = next(path for path in BEHAVIOR_SUBJECTS if path not in PATCHED)
    if baseline == render(proposed_bytes({first: current[first] + b"\nsubject drift\n"})):
        return _fail("subject drift did not stale the manifest")
    rows = ROW.findall(baseline)
    reordered = baseline.replace(
        f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
        f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
    )
    if not verify_manifest(reordered, baseline):
        return _fail("manifest path-order mutation passed")
    killed += 2

    # Patch population: dropping one declared patch.
    without_proposal = [p for p in patch_files() if p.name != "proposal.md.patch"]
    population = population_findings(without_proposal)
    if (
        "proposed patch population differs from declared subjects" not in population
        or f"declared patched subject is unchanged: {PROPOSAL}" not in population
    ):
        return _fail("dropped-patch mutation passed the population predicate")
    killed += 1

    # One mutant per paragraph rule, each isolating its own finding.
    text = spec.decode("utf-8")
    opening = text.index(PARAGRAPH_OPENING)
    case = text.index(CASE, opening)
    paragraph = text[opening:case]
    for label, rule in PARAGRAPH_RULES.items():
        folded = fold(paragraph)
        mutated_paragraph = folded.replace(fold(rule), "[removed]", 1)
        if mutated_paragraph == folded:
            return _fail(f"paragraph-rule fixture matched nothing: {label}")
        mutated = (text[:opening] + mutated_paragraph + "\n\n" + text[case:]).encode()
        found = requirement_findings(mutated)
        if f"dismissal paragraph lacks {label}" not in found:
            return _fail(f"paragraph-rule mutation passed: {label}")
        killed += 1

    # Paragraph missing, duplicated and moved out of PWB-REQ-007.
    next_start = text.index(NEXT_REQUIREMENT)
    next_case = text.index(CASE, next_start)
    moved = (
        text[:opening]
        + text[case:next_case]
        + paragraph
        + text[next_case:]
    ).encode()
    paragraph_mutants = {
        "missing paragraph": (
            text.replace(PARAGRAPH_OPENING, "A claim may be annotated", 1).encode(),
            "missing or duplicate dismissal paragraph",
        ),
        "duplicate paragraph": (
            (text[:case] + paragraph + text[case:]).encode(),
            "missing or duplicate dismissal paragraph",
        ),
        "misplaced paragraph": (
            moved,
            "dismissal paragraph is not in the required PWB-REQ-007 position",
        ),
    }
    for name, (mutated, expected) in paragraph_mutants.items():
        if expected not in requirement_findings(mutated):
            return _fail(f"{name} mutation passed")
        killed += 1

    # Each scenario missing, duplicated and moved into the next requirement.
    for heading in SCENARIOS:
        start = text.index(heading)
        stop = text.index("\n\n", text.index("- **AND**", start)) + 2
        block = text[start:stop]
        removed = text[:start] + text[stop:]
        next_heading_end = removed.index("\n", removed.index(NEXT_REQUIREMENT)) + 1
        misplaced = (
            removed[:next_heading_end] + "\n" + block + removed[next_heading_end:]
        )
        scenario_mutants = {
            "missing": (
                text.replace(heading + "\n", "", 1),
                f"missing or duplicate scenario: {heading}",
            ),
            "duplicate": (
                text.replace(heading + "\n", heading + "\n" + heading + "\n", 1),
                f"missing or duplicate scenario: {heading}",
            ),
            "misplaced": (
                misplaced,
                f"scenario is not in the required PWB-REQ-007 position: {heading}",
            ),
        }
        for name, (mutated, expected) in scenario_mutants.items():
            if expected not in requirement_findings(mutated.encode()):
                return _fail(f"{name} scenario mutation passed: {heading}")
            killed += 1

    # One mutant per scenario-body rule, each isolating its own finding.
    for heading, rules in SCENARIO_RULES.items():
        body = scenario_body(text, heading)
        at = text.index(heading) + len(heading)
        for label, rule in rules.items():
            folded = fold(body)
            if folded.count(fold(rule)) != 1:
                return _fail(f"scenario-rule fixture is not unique: {label}")
            mutated = (
                text[:at] + "\n\n" + folded.replace(fold(rule), "[removed]", 1)
                + text[at + len(body):]
            ).encode()
            if f"scenario lacks {label}: {heading}" not in requirement_findings(mutated):
                return _fail(f"scenario-rule mutation passed: {label}")
            killed += 1

    # Each forbidden wording, once in the paragraph and once in a scenario.
    fixtures = {
        "clock": "The reader's clock decides it.",
        "hide": "A page MAY hide the dismissed claim.",
        "collapse": "A view MAY collapse the claim's facts.",
        "expire-on-read": "A dismissal MAY expire on read.",
        "removal": "A dismissed Unknown claim is removed from the aggregate's Unknown total.",
        "exclusion": "A dismissed member is excluded from the freshness count.",
        "second refusal route": "It is a refused record also when its expiry has passed.",
        "permissive dismissal source": "A model assertion MAY dismiss a claim.",
        "claim-reason refusal": (
            "A record naming a claim whose primary reason is `challenge-suspended` is refused."
        ),
        "refusal by an absent claim": (
            "It is refused when the evaluation neither carries nor records its claim."
        ),
        "two classes at once": "The record is disclosed as lapsed and as refused.",
        "uncounted member": "A dismissed claim is not counted in the Unknown headline.",
    }
    if set(fixtures) != set(FORBIDDEN):
        return _fail("forbidden fixtures do not cover every forbidden wording")
    first_heading = SCENARIOS[0]
    first_body_end = text.index(first_heading) + len(first_heading) + len(
        scenario_body(text, first_heading)
    )
    for label, sentence in fixtures.items():
        if [name for name, pattern in FORBIDDEN.items()
                if re.search(pattern, sentence, re.IGNORECASE)] != [label]:
            return _fail(f"forbidden fixture does not isolate: {label}")
        in_paragraph = (text[:case] .rstrip("\n") + " " + sentence + "\n\n" + text[case:]).encode()
        if f"dismissal paragraph uses forbidden {label} wording" not in requirement_findings(in_paragraph):
            return _fail(f"forbidden paragraph wording passed: {label}")
        in_scenario = (
            text[:first_body_end] + "\n  " + sentence + text[first_body_end:]
        ).encode()
        if f"scenario {first_heading} uses forbidden {label} wording" not in requirement_findings(in_scenario):
            return _fail(f"forbidden scenario wording passed: {label}")
        killed += 2

    # Round-2 review mutants: a second rendering claim in Scenario 1, one fact
    # dropped from the disclosure list, and Scenario 2's refusal reverted to
    # naming the claim's current reason.
    for heading, phrases in SCENARIO_ONCE.items():
        end = text.index(heading) + len(heading) + len(scenario_body(text, heading))
        for phrase in phrases:
            repeated = (text[:end] + "\n  " + phrase + text[end:]).encode()
            expected = f"scenario does not say {phrase!r} exactly once: {heading}"
            if expected not in requirement_findings(repeated):
                return _fail(f"repeated scenario phrase passed: {phrase}")
            killed += 1
    fact_list = fold(PARAGRAPH_RULES["every fact named"])
    folded = fold(paragraph)
    dropped_fact = folded.replace(fact_list, fact_list.replace("freshness, ", "", 1), 1)
    if dropped_fact == folded:
        return _fail("fact-list fixture matched nothing")
    mutated = (text[:opening] + dropped_fact + "\n\n" + text[case:]).encode()
    if "dismissal paragraph lacks every fact named" not in requirement_findings(mutated):
        return _fail("dropped-fact mutation passed")
    killed += 1
    reverted = text.replace(
        "whose own dismissed primary reason is", "naming a claim whose primary reason is", 1
    )
    if reverted == text:
        return _fail("scenario-2 reversion fixture matched nothing")
    found = requirement_findings(reverted.encode())
    if (
        f"scenario lacks refused by its own reason: {SCENARIOS[1]}" not in found
        or f"scenario {SCENARIOS[1]} uses forbidden claim-reason refusal wording" not in found
    ):
        return _fail("scenario-2 reversion passed")
    killed += 1

    # Round-3 review mutants: the in-effect conjunction weakened to a
    # disjunction, retirement decided outside the evaluation, and a Scenario 3
    # record put in two classes.
    folded = fold(paragraph)
    round3 = {
        "in-effect disjunction": (
            "earlier than the record's expiry instant, and the claim's",
            "earlier than the record's expiry instant, or the claim's",
            "dismissal paragraph lacks in-effect conjunction",
        ),
        "world-side retirement": (
            "when the evaluation records the claim identity it names as retired "
            "by a split or merge",
            "when a split or merge has retired the claim identity it names",
            "dismissal paragraph lacks retired identity",
        ),
    }
    for name, (old, new, expected) in round3.items():
        mutated_paragraph = folded.replace(old, new, 1)
        if mutated_paragraph == folded:
            return _fail(f"round-3 fixture matched nothing: {name}")
        mutated = (text[:opening] + mutated_paragraph + "\n\n" + text[case:]).encode()
        if expected not in requirement_findings(mutated):
            return _fail(f"round-3 mutation passed: {name}")
        killed += 1
    two_classes = text.replace(
        "is disclosed beside the\n  claim as lapsed,",
        "is disclosed beside the\n  claim as lapsed and as refused,",
        1,
    )
    if two_classes == text:
        return _fail("two-class fixture matched nothing")
    expected = f"scenario {SCENARIOS[2]} uses forbidden two classes at once wording"
    if expected not in requirement_findings(two_classes.encode()):
        return _fail("two-class scenario mutation passed")
    killed += 1

    # Round-4 review mutants. Each adds, reverses or drops required text
    # that no rule above pins whole; the spec pin must fail each one.
    def reworded(old: str, new: str) -> bytes | None:
        pattern = r"\s+".join(re.escape(word) for word in old.split())
        if len(re.findall(pattern, text)) != 1:
            return None
        return re.sub(pattern, new, text, count=1).encode()

    round4 = {
        "Q5 model author in effect": (
            "condition as one whose claim or reason changed.",
            "condition as one whose claim or reason changed. A record whose "
            "author is a model is in effect like any other.",
        ),
        "Q9 re-read flips": (
            "renders the same claim state",
            "renders the same claim state until it is re-read, then without it",
        ),
        "Q12 renders green": (
            "the claim is counted once as dismissed.",
            "the claim is counted once as dismissed (though it renders green).",
        ),
        "Q13 read-time lapse": (
            "condition as one whose claim or reason changed.",
            "condition as one whose claim or reason changed. A page read after "
            "the expiry instant shows the claim undismissed.",
        ),
        "Q14 refused or lapsed": (
            "are disclosed among the evaluation's refused records",
            "are disclosed among the evaluation's refused records or as lapsed "
            "records",
        ),
        "Q15 successor transfer": (
            "and dismissing a successor needs a new record.",
            "and the record then applies to the successor.",
        ),
        "Q16 class parity dropped": (
            "from a dismissal in effect, identically in the human and machine "
            "views. The classes",
            "from a dismissal in effect. The classes",
        ),
        "Q17 oracle clause dropped": (
            "as-of instant with the checker's own statement of the rule; zero",
            "as-of instant; zero",
        ),
        "Q18 case clause dropped": (
            "expiry instant, and a record set that cannot be read.",
            "expiry instant.",
        ),
        "Q19 falsifier clause dropped": (
            "whose test it meets, or an unreadable record set yields a "
            "dismissed or record-class count of zero.",
            "whose test it meets.",
        ),
        "Q20 headline narrowed": (
            "expandable as a sibling state.",
            "expandable as a sibling state, and the Unknown headline shows "
            "only undismissed members.",
        ),
        "byte outside PWB-REQ-007": (
            "### Requirement: PWB-REQ-004",
            "### Requirement: PWB-REQ-004\n\nA dismissal MAY apply here.",
        ),
    }
    for name, (old, new) in round4.items():
        mutated = reworded(old, new)
        if mutated is None:
            return _fail(f"round-4 fixture does not match once: {name}")
        found = requirement_findings(mutated)
        if not any(f.startswith("proposed spec differs from the pinned text") for f in found):
            return _fail(f"round-4 mutation passed the spec pin: {name}")
        killed += 1
    base_text = (ROOT / SPEC).read_text()
    for anchor, _ in SPEC_EDITS:
        base_start = base_text.index(REQUIREMENT)
        at = base_text.index(anchor, base_start)
        drifted = (base_text[:at + 1] + "~" + base_text[at + 1:]).encode()
        expected = (
            "current PWB-REQ-007 does not carry the pinned anchor exactly "
            f"once: {anchor.splitlines()[0]!r}"
        )
        if expected not in requirement_findings(spec, drifted):
            return _fail(f"drifted anchor passed: {anchor.splitlines()[0]}")
        killed += 1

    # Forbidden wording is matched regardless of case.
    for label, sentence in fixtures.items():
        swapped = sentence.swapcase()
        in_paragraph = (text[:case].rstrip("\n") + " " + swapped + "\n\n" + text[case:]).encode()
        if f"dismissal paragraph uses forbidden {label} wording" not in requirement_findings(in_paragraph):
            return _fail(f"case-swapped forbidden wording passed: {label}")
        killed += 1

    # Each required warrant removed from PWB-REQ-007's block only.
    warrants_at = text.index(WARRANTS, text.index(REQUIREMENT))
    block_end = text.index("```\n", warrants_at + len(WARRANTS)) + 4
    block = text[warrants_at:block_end]
    for authority in REQUIRED_WARRANTS:
        stripped = re.sub(
            rf"(?<=\[){re.escape(authority)}, |, {re.escape(authority)}(?=[,\]])",
            "",
            block,
            count=1,
        )
        if stripped == block:
            return _fail(f"warrant fixture matched nothing: {authority}")
        mutated = (text[:warrants_at] + stripped + text[block_end:]).encode()
        if f"PWB-REQ-007 warrants lack {authority}" not in requirement_findings(mutated):
            return _fail(f"warrant mutation passed: {authority}")
        killed += 1

    # Generated companions: dependency and contract-coverage drift.
    tampered = dict(proposed)
    tampered[DEPENDENCIES] = proposed[DEPENDENCIES].replace(
        b"17 requirement(s)", b"18 requirement(s)", 1
    )
    if tampered[DEPENDENCIES] == proposed[DEPENDENCIES] or not dependency_findings(tampered):
        return _fail("generated dependency drift passed")
    coverage_drift = dict(proposed)
    coverage_drift[CONTRACT_COVERAGE] = proposed[CONTRACT_COVERAGE].replace(
        b"136 covered", b"137 covered", 1
    )
    if coverage_drift[CONTRACT_COVERAGE] == proposed[CONTRACT_COVERAGE] or not companion_findings(coverage_drift):
        return _fail("generated contract-coverage drift passed")
    killed += 2

    # Companion rules: proposal bullet, capability row and totals, each repair row.
    companion_mutants = {
        "proposal bullet": (
            PROPOSAL,
            b"A claim that renders Unknown may carry",
            b"A claim that renders Unknown may hide",
            "proposal does not carry the dismissal obligation",
        ),
        "capability row": (
            CAPABILITY_COVERAGE,
            CAPABILITY_ROW.encode(),
            CAPABILITY_ROW.replace("covered —", "Unknown —").encode(),
            "capability coverage does not carry row 32 exactly once",
        ),
        "capability totals": (
            CAPABILITY_COVERAGE,
            CAPABILITY_TOTALS.encode(),
            CAPABILITY_TOTALS.replace("32 total", "31 total").encode(),
            "capability coverage population or totals are not 32",
        ),
    }
    for repair_id, (supersedes, disposition) in REPAIR_DISPOSITIONS.items():
        flipped = (
            "unknown-uncovered" if disposition != "unknown-uncovered" else "covered:PWB-REQ-007"
        )
        row = re.search(
            rf"^\| {re.escape(repair_id)} \|[^\n]*$",
            proposed[CONTRACT_REPAIR].decode(),
            re.MULTILINE,
        ).group(0).encode()
        companion_mutants[f"repair row {repair_id}"] = (
            CONTRACT_REPAIR,
            row,
            row.replace(f"| {disposition} |".encode(), f"| {flipped} |".encode()),
            f"{repair_id} does not supersede {supersedes} as {disposition}",
        )
    for name, (rel, old, new, expected) in companion_mutants.items():
        mutated = dict(proposed)
        mutated[rel] = proposed[rel].replace(old, new, 1)
        if mutated[rel] == proposed[rel] or expected not in companion_findings(mutated):
            return _fail(f"{name} mutation passed")
        killed += 1

    # Patch drift: a corrupted spec patch neither applies nor composes.
    with tempfile.TemporaryDirectory() as scratch:
        broken = pathlib.Path(scratch) / "spec.md.patch"
        original = (ROOT / PROPOSED / "spec.md.patch").read_text()
        corrupted = original.replace(
            " - **Case (sweep)**: enumerate every project entity",
            " - **Case (sweep)**: enumerate each project entity",
            1,
        )
        if corrupted == original:
            return _fail("patch-drift fixture matched nothing")
        broken.write_text(corrupted)
        try:
            proposed_bytes(patches=[broken])
        except ValueError:
            pass
        else:
            return _fail("patch drift passed")
    killed += 1

    # check() itself: every predicate is wired in, not only correct as a
    # function. Each case changes one input of check() and requires its own
    # finding; the proposed bytes check() builds are edited through
    # proposed_bytes (population_findings passes patches and is left alone).
    kept = (MANIFEST_OUT, patch_files, proposed_bytes)

    def through_check(edit=None, patches=None, manifest=None) -> list[str]:
        global MANIFEST_OUT, patch_files, proposed_bytes
        if patches is not None:
            patch_files = lambda: patches  # noqa: E731
        if manifest is not None:
            MANIFEST_OUT = manifest
        if edit is not None:
            def edited(overrides=None, patches=None):
                built = kept[2](overrides, patches)
                return built if patches is not None else edit(dict(built))
            proposed_bytes = edited
        try:
            return check()
        finally:
            MANIFEST_OUT, patch_files, proposed_bytes = kept

    def edit_of(rel, old, new):
        def edit(built):
            if old not in built[rel]:
                raise AssertionError(f"check() fixture matched nothing: {rel}")
            built[rel] = built[rel].replace(old, new, 1)
            return built
        return edit

    spec_text = proposed[SPEC]
    all_patches = kept[1]()
    with tempfile.TemporaryDirectory() as scratch:
        scratch_dir = pathlib.Path(scratch)
        stale = scratch_dir / "stale.txt"
        stale.write_text(baseline.replace(rows[0][0], "0" * 64, 1))
        swapped = scratch_dir / "swapped.txt"
        swapped.write_text(
            baseline.replace(
                f"{rows[0][0]}  {rows[0][1]}\n{rows[1][0]}  {rows[1][1]}",
                f"{rows[1][0]}  {rows[1][1]}\n{rows[0][0]}  {rows[0][1]}",
            )
        )
        extra_lines = current[first].decode("utf-8").splitlines()
        extra = scratch_dir / f"{first.name}.patch"
        extra.write_text(
            f"diff --git a/{first.as_posix()} b/{first.as_posix()}\n"
            f"--- a/{first.as_posix()}\n+++ b/{first.as_posix()}\n"
            f"@@ -{len(extra_lines)} +{len(extra_lines)},2 @@\n {extra_lines[-1]}\n+undeclared drift\n"
        )
        check_cases = {
            "check() clean": (dict(), None),
            "check() manifest content": (
                dict(manifest=stale),
                "manifest differs from exact regeneration over proposed bytes",
            ),
            "check() manifest order": (
                dict(manifest=swapped),
                "manifest path population or order differs",
            ),
            "check() manifest missing": (
                dict(manifest=scratch_dir / "absent.txt"),
                "manifest missing: ",
            ),
            "check() patch population": (
                dict(patches=[p for p in all_patches if p.name != "proposal.md.patch"]),
                "proposed patch population differs from declared subjects",
            ),
            "check() undeclared subject": (
                dict(patches=sorted(all_patches + [extra], key=lambda p: p.name)),
                f"undeclared subject change: {first}",
            ),
            "check() requirement pin": (
                dict(edit=edit_of(SPEC, b"### Requirement: PWB-REQ-004", b"### Requirement: PWB-REQ-004\n\nA dismissal MAY apply here.")),
                "proposed spec differs from the pinned text",
            ),
            "check() pin leading edge": (
                dict(edit=edit_of(SPEC, spec_text[:12], b"~" + spec_text[:12])),
                "proposed spec differs from the pinned text at line 1",
            ),
            "check() dependencies": (
                dict(edit=edit_of(DEPENDENCIES, proposed[DEPENDENCIES][:20], b"~" + proposed[DEPENDENCIES][:20])),
                "proposed GOVERNING-DEPENDENCIES.md differs from regeneration",
            ),
            "check() proposal token": (
                dict(edit=edit_of(PROPOSAL, b"recorded, attributed", b"recorded, ~attributed")),
                "proposal does not carry the dismissal obligation",
            ),
            "check() capability population": (
                dict(edit=edit_of(CAPABILITY_COVERAGE, b"Population: 32 positive", b"Population: 31 positive")),
                "capability coverage population or totals are not 32",
            ),
            "check() contract coverage": (
                dict(edit=edit_of(CONTRACT_COVERAGE, proposed[CONTRACT_COVERAGE][:20], b"~" + proposed[CONTRACT_COVERAGE][:20])),
                "proposed CONTRACT-COVERAGE.md differs from regeneration",
            ),
        }
        for name, (arguments, expected) in check_cases.items():
            found = through_check(**arguments)
            if expected is None:
                if found:
                    return _fail(f"{name} does not pass: {found}")
            elif not any(expected in finding for finding in found):
                return _fail(f"{name} passed")
            killed += 1
    MANIFEST_OUT, patch_files, proposed_bytes = kept

    # The mutant tables above are also the rules they test, so a rule deleted
    # from a table deletes its own mutant. Pin the once-only population and
    # the total here, as literals, so a deletion fails this selftest.
    if SCENARIO_ONCE != {
        SCENARIOS[0]: ("the first evaluation renders", "without the sibling state"),
    }:
        return _fail("once-only scenario phrase population changed")
    if rule_tables_digest() != RULE_TABLES_SHA256:
        return _fail("rule tables changed without their pinned digest")
    if killed != EXPECTED_KILLED:
        return _fail(f"{killed} mutants killed, expected {EXPECTED_KILLED}")
    print(
        f"selftest: {killed} mutants killed — stale manifest, path order, patch "
        f"population, {len(PARAGRAPH_RULES)} paragraph rules, paragraph "
        f"missing/duplicate/placement, {len(SCENARIOS)} scenarios x "
        "missing/duplicate/placement, "
        f"{sum(len(rules) for rules in SCENARIO_RULES.values())} scenario-body "
        f"rules, {len(FORBIDDEN)} forbidden wordings x paragraph/scenario, "
        f"{sum(len(p) for p in SCENARIO_ONCE.values())} once-only scenario "
        "phrases, a dropped fact, the scenario-2 reversion, three round-3 "
        f"mutants, {len(round4)} round-4 mutants against the whole-spec pin, "
        f"{len(SPEC_EDITS)} drifted pin anchors, {len(fixtures)} case-swapped "
        "forbidden wordings, "
        f"{len(REQUIRED_WARRANTS)} warrants, "
        "dependency and contract-coverage drift, proposal, capability row and "
        f"totals, {len(REPAIR_DISPOSITIONS)} repair rows, patch drift, "
        "12 check() cases (manifest content/order/missing, patch population, "
        "undeclared subject, pin edges, dependencies, proposal, capability, "
        "contract coverage), "
        "all fail closed"
    )
    return 0


def apply(at_adoption: bool) -> int:
    if not at_adoption:
        print(
            "refusing: --apply is an adoption-time operation; pass --at-adoption "
            "only in the owner's act change"
        )
        return 2
    findings = check()
    if findings:
        print("refusing to apply: package does not verify")
        for finding in findings:
            print(f"  {finding}")
        return 1
    proposed = proposed_bytes()
    for rel in PATCHED:
        (ROOT / rel).write_bytes(proposed[rel])
        print(f"applied {rel.as_posix()}")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--at-adoption", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        # After sign-off the fixtures need the pre-adoption subjects: run this
        # file's current bytes in an archive of the sign-off's parent commit
        # (syzygy-tmkb). Before sign-off the record is absent and this is None.
        import pwb_signed_selftest
        rerun = pwb_signed_selftest.rerun_before_signoff(
            __file__,
            ".syzygy/governance/decisions/PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md",
            "9bf3ea5eb63243a1bd423758d01ab1e497b1292a",  # parent of sign-off 5de4ce7f
        )
        return selftest() if rerun is None else rerun
    if args.diff:
        for patch in patch_files():
            sys.stdout.write(patch.read_text())
        return 0
    if args.apply:
        return apply(args.at_adoption)
    if args.check:
        findings = check()
        if findings:
            print("PWB dismissal-expiry package does not verify:")
            for finding in findings:
                print(f"  {finding}")
            return 1
        print(
            f"PWB dismissal-expiry manifest matches {len(BEHAVIOR_SUBJECTS)} "
            f"proposed subjects ({len(PATCHED)} patched, "
            f"{len(BEHAVIOR_SUBJECTS) - len(PATCHED)} unchanged); requirement, "
            "companion, dependency regeneration, "
            "and the pinned rule tables verify"
        )
        return 0
    if not args.write:
        print(
            "refusing: regenerating the manifest retires copied act arguments; "
            "pass --write and update every registered digest copy"
        )
        return 2
    proposed = proposed_bytes()
    structure = (
        population_findings(patch_files())
        + requirement_findings(proposed[SPEC])
        + dependency_findings(proposed)
        + companion_findings(proposed)
    )
    if structure:
        for finding in structure:
            print(f"  {finding}")
        return 1
    target = ROOT / MANIFEST_OUT
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(proposed))
    print(f"wrote {MANIFEST_OUT.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
