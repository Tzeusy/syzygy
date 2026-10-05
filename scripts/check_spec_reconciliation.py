#!/usr/bin/env python3
"""Check the reconciled effective specification composition (bead syzygy-73e.5.6).

The five readability successors of the adopted OpenSpec changes (Capability
1, Three-Surface POC, Polaris generator base, Polaris understanding amendment
and PWB) each ended in an owner outcome. This read-only checker re-derives,
from tracked Syzygy authority only, that every outcome is terminal and still
binds the bytes on disk, and that the requirement and scenario populations,
generated dependency and coverage rows, and default routes agree with them.
The reconciliation record is
`docs/evidence/spec-readability-reconciliation-2026-10-02/README.md`.

Predicates, each printed with its denominator:

- R1 terminal outcomes: every child has its dedicated record, and that
  record's binding resolves. A digest act's phrase argument equals the
  sha256 of its package manifest and appears in the aggregate act record; a
  version-tagged sign-off names its package, version and tag, and its marker
  block appears once in the aggregate record. A missing record is a FAIL,
  never a skipped row. A child may name later digest acts (`successors`)
  that superseded some of its subjects; each one is checked the same way and
  is equally a terminal record. A signed Polaris addition (below) is a
  child too: it needs a version-tagged sign-off record in `decisions/` whose
  `Package:` line names its change, checked the same way, and one record per
  version; an installed addition with no such record is a FAIL. An addition
  has no R2 row: no manifest hashes its `spec.md`, and the sign-off binds it
  by the tag on the recording commit, so an edit after sign-off re-passes
  here once `--regenerate` is rerun. Such an edit is a new version, which the
  recorder and review discipline govern, not this checker.
- R2 exact subject bytes: a digest act's successor column equals its
  manifest rows, and every signed subject on disk hashes to its row. A
  versioned sign-off's manifest rows equal the subjects on disk. A child's
  later successors compose in order: each one's act instant is strictly
  later than the act before it, each one's predecessor column names exactly
  the row the chain has reached for that subject, and its successor row then
  becomes the row the subject must hash to. A later version-tagged sign-off
  carries no instant or predecessor column, so its marker block must follow
  the act before it in the append-only aggregate record (its `Date:` on or
  after), and its own `proposed/` patches stand in for the predecessor
  column: each moved row has exactly one patch, which reversed over the
  bytes at the successor row yields exactly the row reached; a row with no
  patch must not move, and no patch may target a path outside the manifest.
- R3 populations: CAP1-REQ, POC-REQ, PWB-REQ and the effective
  REQ-polaris-generation composition are each parsed by two independent
  methods (a regular-expression parser and a line state machine with no
  regular expressions; Polaris composes by ID line in one and by requirement
  name in the other). Both must agree, identifiers must be unique, and the
  result must equal the hard-coded literal census below and the committed
  `census.json`. A signed Polaris addition is any other change whose
  `specs/polaris-generation/spec.md` a version-tagged sign-off's builder has
  installed; it may only ADD requirements and is composed after the overlay
  by both methods. Each method also refuses, independent of requirement
  blocks, every level-2 heading in an addition other than exactly
  `## ADDED Requirements` and every heading of any level, case or spacing
  that names a delta section (a RENAMED list or a name-only REMOVED list
  carries no requirement block). The expected Polaris totals and identities are derived,
  never raised by hand: the base-and-overlay literal (31 / 182, IDs 001–031)
  plus what each signed addition ADDs, read by both block parsers from the
  addition alone. An unsigned addition adds nothing to the expected
  population, so it fails here as well as in R1, and `--regenerate` refuses.
- R4 generated rows: each generated dependency file's source digest and
  requirement count match the spec; every full or continuation-form
  identifier mention in the five change directories, each signed addition's
  directory and the default route pages resolves to the population; the CAP1
  and PWB capability coverage tables carry the whole population; and each
  signed addition's generated union equals its spec's warrants (a FAIL,
  since that union is generated and never signed).
- R5 default routes: `openspec/README.md` has one row per tracked change
  directory naming its terminal record; `PROJECT-STATUS.md` cites every
  terminal record (a signed addition's sign-off record included) and states
  the Polaris composition the census computes.
- R6 behaviour-contract pins (report only, never green): the observer
  registry entry and the secret-classification policy pin a PWB `spec.md`
  digest. A pin that differs from the current bytes is Unknown and needs its
  own owner act; this checker never repairs it.
- R7 Polaris dependency unions (report only, never green): each of the two
  generated Polaris unions is recomputed from its spec's warrants blocks.
  Both files are bound bytes, regenerated (never written) by
  `scripts/build_polaris_dependency_unions.py`, so a difference is Unknown
  and needs a signed successor.

`--selftest` copies every input into a scratch tree, confirms it passes,
then applies each rule-6 mutant and requires its expected predicate to fail
(or, for R6 and R7, to change what it reports); `--witnesses FILE` stores
each mutant's path, old and new fragment and the commit it ran at. One R6
case is strict rather than a change: with the `syzygy-jloi` re-pin package's
proposed bytes in place of both pinned subjects (what that package's
recorder applies at its acts), R6 must examine both pins and report exactly
zero findings, with no other predicate failing. Once the acts are performed
the tree already carries those bytes, and the case requires zero there.
Since the 2026-10-03 tree-framing sign-off moved `spec.md` past the pinned
row, the case also replays `spec.md` as the pinned bytes (the re-pin
builder's `spec_at_pin`, every later signed patch reversed): R6 must read
zero over that tree, and R2, R3 and R4, which then see bytes no act binds,
must fail exactly. On the tree itself R6 reports both pins until their own
re-pin act. The strict case `pins-after-tree-framing-repin-acts` does the
same for the `syzygy-2g0d` package, which re-pins both to the tree-framing
`spec.md` row: with its proposed bytes in place of both subjects, R6 must
examine both pins and report zero, and no other predicate may fail.
The R7 case `union-after-successor-act` does the same with the
`syzygy-c51h` successor package's proposed union. Before that act it
required R2, and only R2, to fail by design; the reconciliation was
re-derived on 2026-10-02 to name the act as the understanding child's
successor, so the case now requires every predicate to pass.

`--selftest` also installs a synthetic signed addition into a scratch copy
(spec, sign-off record, aggregate block, route row, status figure, then
`--regenerate`), requires it to pass, and kills one mutant per addition
predicate.

A Polaris addition's recording commit runs one command after the recorder
has applied the package through its builder:

  python3 scripts/check_spec_reconciliation.py --regenerate

It writes the addition's generated `GOVERNING-DEPENDENCIES.md` (through
`scripts/build_polaris_dependency_unions.py --write-additions`) and
`census.json`, and refuses while any installed addition is unsigned. It
never writes a signed subject, a route page or this script.

A later act over any subject fails R2 by design: the reconciliation is then
re-derived, never carried forward. The first re-derivation (2026-10-02)
added the dependency-union successor act to the understanding child; the
second (2026-10-03) added the tree-framing sign-off v1.0 to the PWB child
and re-derived the PWB census (PWB-REQ-014 gained seven scenarios).

Usage:
  python3 scripts/check_spec_reconciliation.py --check
  python3 scripts/check_spec_reconciliation.py --census > <record>/census.json
  python3 scripts/check_spec_reconciliation.py --regenerate
  python3 scripts/check_spec_reconciliation.py --selftest [--witnesses FILE]
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ".syzygy/governance/decisions"
CANDIDATES = ".syzygy/governance/contracts/candidates"
AGGREGATE = f"{DECISIONS}/ACCEPTANCE-ACT-RECORD.md"
RECORD_DIR = "docs/evidence/spec-readability-reconciliation-2026-10-02"
CENSUS = f"{RECORD_DIR}/census.json"
CHANGES = "openspec/changes"
STATUS = "PROJECT-STATUS.md"
OPENSPEC_README = "openspec/README.md"
ROUTE_PAGES = (STATUS, OPENSPEC_README, "README.md", "AGENTS.md")
REGISTRY = (".syzygy/governance/declarations/adapter-registry/"
            "POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json")
POLICY = (".syzygy/governance/policies/"
          "POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json")
PIN_BEAD = "syzygy-2g0d"
UNION_SUCCESSOR = (f"{CANDIDATES}/"
                   "polaris-understanding-dependency-union-successor")
UNION_BEAD = "syzygy-c51h"

CAP1_CHANGE = "project-registration-and-honest-shape-visibility"
POC_CHANGE = "three-surface-poc-experience"
PWB_CHANGE = "polaris-project-wide-butlers-model"
BASE_CHANGE = "polaris-manifesto-generation"
UNDERSTANDING_CHANGE = "polaris-manifesto-understanding-amendment"

#: The five children of syzygy-73e.5, each with its terminal outcome record.
CHILDREN = (
    {"key": "cap1", "bead": "syzygy-73e.5.1", "kind": "digest",
     "change": CAP1_CHANGE,
     "label": "SIGN OFF CAPABILITY 1 READABILITY SUCCESSOR",
     "record": f"{DECISIONS}/CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md",
     "manifest": f"{CANDIDATES}/capability-1-readability-successor/"
                 "SUCCESSOR-MANIFEST.txt"},
    {"key": "poc", "bead": "syzygy-73e.5.2", "kind": "digest",
     "change": POC_CHANGE,
     "label": "SIGN OFF THREE-SURFACE POC READABILITY SUCCESSOR",
     "record": f"{DECISIONS}/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md",
     "manifest": f"{CANDIDATES}/three-surface-poc-readability-successor/"
                 "THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt"},
    {"key": "polaris-base", "bead": "syzygy-73e.5.3", "kind": "digest",
     "change": BASE_CHANGE,
     "label": "SIGN OFF POLARIS GENERATOR BASE READABILITY SUCCESSOR",
     "record": f"{DECISIONS}/POLARIS-GENERATOR-BASE-READABILITY-SUCCESSOR-ACT.md",
     "manifest": f"{CANDIDATES}/polaris-generator-base-readability-successor/"
                 "SUCCESSOR-MANIFEST.txt"},
    {"key": "polaris-understanding", "bead": "syzygy-73e.5.4",
     "kind": "digest", "change": UNDERSTANDING_CHANGE,
     "label": "SIGN OFF POLARIS UNDERSTANDING READABILITY SUCCESSOR",
     "record": f"{DECISIONS}/POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md",
     "manifest": f"{CANDIDATES}/polaris-understanding-readability-successor/"
                 "SUCCESSOR-MANIFEST.txt",
     # Later digest acts over some of this child's subjects, in act order.
     "successors": (
         {"label": "SIGN OFF POLARIS UNDERSTANDING DEPENDENCY UNION SUCCESSOR",
          "record": f"{DECISIONS}/"
                    "POLARIS-UNDERSTANDING-DEPENDENCY-UNION-SUCCESSOR-ACT.md",
          "manifest": f"{UNION_SUCCESSOR}/SUCCESSOR-MANIFEST.txt"},
     )},
    {"key": "pwb", "bead": "syzygy-73e.5.5", "kind": "versioned",
     "change": PWB_CHANGE, "package": "pwb-readability-successor",
     "version": "1.0",
     "record": f"{DECISIONS}/PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md",
     "manifest": f"{CANDIDATES}/pwb-readability-successor/"
                 "PWB-READABILITY-SUCCESSOR-MANIFEST.txt",
     # Later version-tagged sign-offs over this child's subjects, in act
     # order (re-derived 2026-10-03). Each one's patches under `proposed/`
     # must reverse the successor row to exactly the row the chain reached.
     "successors": (
         {"kind": "versioned", "package": "pwb-tree-framing-amendment",
          "version": "1.0",
          "record": f"{DECISIONS}/PWB-TREE-FRAMING-AMENDMENT-SIGNOFF-v1.0.md",
          "manifest": f"{CANDIDATES}/pwb-tree-framing-amendment/"
                      "PWB-TREE-FRAMING-AMENDMENT-MANIFEST.txt",
          "proposed": f"{CANDIDATES}/pwb-tree-framing-amendment/proposed"},
     )},
)


def spec_path(change, capability=None):
    return f"{CHANGES}/{change}/specs/{capability or change}/spec.md"


FAMILY_SPECS = {
    "CAP1": spec_path(CAP1_CHANGE),
    "POC": spec_path(POC_CHANGE),
    "PWB": spec_path(PWB_CHANGE),
}
POLARIS_BASE_SPEC = spec_path(BASE_CHANGE, "polaris-generation")
POLARIS_OVERLAY_SPEC = spec_path(UNDERSTANDING_CHANGE, "polaris-generation")
POLARIS_ID = "REQ-polaris-generation-"
POLARIS_ADDITION_GLOB = "*/specs/polaris-generation/spec.md"
SIGNOFF_RECORD_GLOB = "*-SIGNOFF-v*.md"
VERSION_LINE = re.compile(r"^Version: (\d+\.\d+)$", re.M)


def polaris_additions(root):
    """Signed-addition candidates: [(change, spec path)], by change name.

    Every change other than the base and the overlay whose Polaris requirements
    sit installed at `specs/polaris-generation/spec.md` (a version-tagged
    sign-off's builder moves them there from `proposed/`). Read from the tree,
    not the index, so `--regenerate` sees the move before it is committed.
    """
    base = root / CHANGES
    found = sorted(p.parent.parent.parent.name for p in
                   base.glob(POLARIS_ADDITION_GLOB)) if base.is_dir() else []
    return [(c, spec_path(c, "polaris-generation")) for c in found
            if c not in (BASE_CHANGE, UNDERSTANDING_CHANGE)]


def addition_records(root, change):
    """[(record path, text, version)] of each versioned sign-off of `change`."""
    out = []
    base = root / DECISIONS
    for path in sorted(base.glob(SIGNOFF_RECORD_GLOB)) if base.is_dir() else ():
        text = path.read_text(encoding="utf-8")
        if f"Package: {change}" in text.splitlines():
            versions = VERSION_LINE.findall(text)
            out.append((path.relative_to(root).as_posix(), text,
                        versions[0] if len(versions) == 1 else None))
    return out

#: Hard-coded literal census (requirement suffix -> scenario count), taken at
#: main bd47409 on 2026-10-02 and cross-checked by the OpenSpec 1.9.0 CLI in
#: the record; PWB re-derived 2026-10-03 after the tree-framing sign-off
#: (PWB-REQ-014: 1 -> 8 scenarios). Never derived from the parsers below.
EXPECTED = {
    "CAP1": dict(zip(
        "001 002 003 004 005 006 010 011 012 013 014 015 016 020 021 022 023 "
        "030 031 032 033 034 035 036 037 038 040 041 042 043 044 045 046 050 "
        "051 052 053 060 061 062 063 064".split(),
        (1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1))),
    "POC": dict.fromkeys(
        "001 002 003 004 010 011 012 013 020 021 022 030 031 032 040 041 042 "
        "043 050 051 052 053 060 061".split(), 1),
    "PWB": dict(zip(
        "001 002 003 004 005 006 007 010 011 012 013 014 015 016 020 021 "
        "022".split(),
        (1, 6, 1, 3, 5, 3, 5, 2, 5, 1, 1, 8, 1, 1, 1, 2, 5))),
    "POLARIS": None,  # totals only below; per-requirement counts in census.json
}
EXPECTED_TOTALS = {"CAP1": (42, 47), "POC": (24, 24), "PWB": (17, 51),
                   "POLARIS": (31, 182)}

ROW = re.compile(r"^([0-9a-f]{64})  (\S[^\n]*)$", re.M)
ACT_TABLE_ROW = re.compile(
    r"^\| `([^`]+)` \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|$", re.M)
DEPS_SOURCE = re.compile(
    r"Source: `spec\.md` sha256 `([0-9a-f]{64})` — (\d+) requirement\(s\)")
ID_MENTION = re.compile(
    r"\b(?:(CAP1|POC|PWB)-REQ-|REQ-polaris-generation-)(\d{3})"
    r"((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)")
STATUS_FIGURE = re.compile(
    r"(\d+) requirements and (\d+) scenarios in the effective composition")


class Report:
    def __init__(self):
        self.lines = []
        self.failed = set()
        self.findings = {}

    def add(self, rid, title, examined, findings, note=""):
        word = "FAIL" if findings else "OK"
        self.findings[rid] = list(findings)
        if findings:
            self.failed.add(rid)
        tail = f" — {note}" if note else ""
        self.lines.append(
            f"{word:5} {rid}  {title} — {examined} examined, "
            f"{len(findings)} findings{tail}")
        self.lines.extend(f"        {f}" for f in findings)

    def warn(self, rid, title, examined, findings, note=""):
        tail = f" — {note}" if note else ""
        word = "WARN" if findings else "OK"
        self.findings[rid] = list(findings)
        self.lines.append(
            f"{word:5} {rid}  {title} — {examined} examined, "
            f"{len(findings)} findings{tail}")
        self.lines.extend(f"        {f}" for f in findings)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(root, rel):
    path = root / rel
    return path.read_bytes() if path.is_file() else None


def read_text(root, rel):
    data = read_bytes(root, rel)
    return None if data is None else data.decode("utf-8")


# --------------------------------------------------------------------------
# R1 and R2: terminal outcomes and exact subject bytes.
# --------------------------------------------------------------------------

ACT_INSTANT = re.compile(r"^Act instant: (\S+)$", re.M)


def check_digest_act(act, tag, aggregate, record, manifest_bytes, r1, r2):
    """R1 and R2 checks of one digest act; its signed table, or None."""
    rows = {path: digest for digest, path in
            ROW.findall(manifest_bytes.decode("utf-8"))}
    phrase = re.compile(
        rf"^{re.escape(act['label'])}: ([0-9a-f]{{64}})$", re.M)
    args = phrase.findall(record)
    if len(args) != 1:
        r1.append(f"{tag}: record carries {len(args)} phrase lines, "
                  "expected exactly 1")
        return None
    if args[0] != sha(manifest_bytes):
        r1.append(f"{tag}: stale act — the phrase argument is not the "
                  f"sha256 of `{act['manifest']}`")
    agg = phrase.findall(aggregate)
    if args[0] not in agg:
        r1.append(f"{tag}: stale act — the aggregate act record does "
                  "not carry this record's phrase")
    table = {p: (pred, succ) for p, pred, succ in
             ACT_TABLE_ROW.findall(record)}
    if {p: s for p, (_pr, s) in table.items()} != rows:
        r2.append(f"{tag}: the record's successor column differs from "
                  "the manifest rows")
    return table


DATE_LINE = re.compile(r"^Date: (\d{4}-\d{2}-\d{2})$", re.M)
DIFF_TARGET = re.compile(r"^\+\+\+ b/(\S[^\n]*)$", re.M)


def versioned_marker(entry):
    return (f"<!-- versioned-signoff:{entry['package']}:"
            f"v{entry['version']} -->")


def check_versioned(entry, tag, aggregate, record, r1):
    """R1 checks of one version-tagged sign-off record."""
    want = (f"Package: {entry['package']}",
            f"Version: {entry['version']}",
            f"Tag: {entry['package']}-v{entry['version']}")
    missing = [w for w in want if w not in record.splitlines()]
    if missing:
        r1.append(f"{tag}: sign-off record lacks {missing}")
    count = aggregate.count(versioned_marker(entry))
    if count != 1:
        r1.append(f"{tag}: aggregate act record carries the sign-off "
                  f"block {count} times, expected 1")


def aggregate_position(entry, aggregate, record):
    """Where an entry's binding sits in the append-only aggregate record."""
    if entry.get("kind", "digest") == "versioned":
        pos = aggregate.find(versioned_marker(entry))
        return pos if pos >= 0 and aggregate.count(
            versioned_marker(entry)) == 1 else None
    m = re.search(rf"^{re.escape(entry['label'])}: ([0-9a-f]{{64}})$",
                  record, re.M)
    pos = aggregate.find(f"{entry['label']}: {m.group(1)}") if m else -1
    return pos if pos >= 0 else None


def package_patches(root, proposed):
    """{target path: [patch paths]} for every patch under `proposed`."""
    out = {}
    base = root / proposed
    for patch in sorted(base.glob("*.patch")) if base.is_dir() else ():
        rel = patch.relative_to(root).as_posix()
        targets = DIFF_TARGET.findall(patch.read_text(encoding="utf-8"))
        for target in targets or ["<no target>"]:
            out.setdefault(target, []).append(rel)
    return out


def reverse_apply(root, patch_rel, target_rel, body):
    """`body` with the patch reversed, or None when it does not reverse."""
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / target_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(body)
        done = subprocess.run(
            ["git", "apply", "-R", "--whitespace=nowarn",
             str((root / patch_rel).resolve())],
            cwd=tmp, capture_output=True)
        return dest.read_bytes() if done.returncode == 0 else None


def compose_versioned(root, later, ltag, rows, r2):
    """Follow one version-tagged successor over the rows reached so far.

    A versioned record carries no predecessor column, so the package's own
    patches stand in for it: each moved row must have exactly one patch, and
    reversing it over the bytes that hash to the successor row must yield
    exactly the row the chain reached. A row with no patch must not move.
    """
    lrows = {path: digest for digest, path in
             ROW.findall(read_text(root, later["manifest"]) or "")}
    patches = package_patches(root, later["proposed"])
    for target in sorted(set(patches) - set(lrows)):
        r2.append(f"{ltag}: patch {patches[target]} targets `{target}`, "
                  "which the manifest does not carry")
    for path, succ in sorted(lrows.items()):
        if path not in rows:
            r2.append(f"{ltag}: `{path}` is not a subject of this child")
            continue
        found = patches.get(path, [])
        if len(found) > 1:
            r2.append(f"{ltag}: broken chain — {len(found)} patches target "
                      f"`{path}`")
        elif found:
            current = read_bytes(root, path)
            prior = (reverse_apply(root, found[0], path, current)
                     if current is not None and sha(current) == succ else None)
            if prior is None or sha(prior) != rows[path]:
                r2.append(f"{ltag}: broken chain — reversing `{found[0]}` "
                          f"over the successor row of `{path}` does not "
                          "yield the row the chain reached")
        elif succ != rows[path]:
            r2.append(f"{ltag}: broken chain — the row of `{path}` moved "
                      "with no patch")
        rows[path] = succ


def check_outcomes(root, report):
    aggregate = read_text(root, AGGREGATE) or ""
    r1, r2, subjects_seen, records = [], [], 0, 0
    for child in CHILDREN:
        tag = f"{child['key']} ({child['bead']})"
        records += 1 + len(child.get("successors", ()))
        record = read_text(root, child["record"])
        manifest_bytes = read_bytes(root, child["manifest"])
        if record is None:
            r1.append(f"{tag}: missing child — no terminal record "
                      f"`{child['record']}`; the outcome is Unknown")
            continue
        if manifest_bytes is None:
            r1.append(f"{tag}: package manifest `{child['manifest']}` missing")
            continue
        rows = {path: digest for digest, path in
                ROW.findall(manifest_bytes.decode("utf-8"))}
        if child["kind"] == "digest":
            if check_digest_act(child, tag, aggregate, record, manifest_bytes,
                                r1, r2) is None:
                continue
        else:
            check_versioned(child, tag, aggregate, record, r1)
        # Later successors compose in act order over the rows reached so far.
        reached = ACT_INSTANT.findall(record)
        position = aggregate_position(child, aggregate, record)
        dates = DATE_LINE.findall(record)
        for later in child.get("successors", ()):
            name = Path(later["record"]).name
            ltag = f"{tag} successor {name}"
            ltext = read_text(root, later["record"])
            lmanifest = read_bytes(root, later["manifest"])
            if ltext is None:
                r1.append(f"{ltag}: missing successor — no terminal record "
                          f"`{later['record']}`; the outcome is Unknown")
                continue
            if lmanifest is None:
                r1.append(f"{ltag}: package manifest `{later['manifest']}` "
                          "missing")
                continue
            if later.get("kind", "digest") == "versioned":
                # No act instant: order is the append-only aggregate record
                # (strictly after the act before it) and a date on or after.
                check_versioned(later, ltag, aggregate, ltext, r1)
                lpos = aggregate_position(later, aggregate, ltext)
                ldates = DATE_LINE.findall(ltext)
                if lpos is None or position is None or not lpos > position:
                    r2.append(f"{ltag}: its aggregate block does not follow "
                              "the act before it")
                if (len(ldates) != 1 or len(dates) != 1
                        or not ldates[0] >= dates[0]):
                    r2.append(f"{ltag}: date {ldates} is not on or after the "
                              f"act before it {dates}")
                position, dates = lpos, ldates
                compose_versioned(root, later, ltag, rows, r2)
                continue
            table = check_digest_act(later, ltag, aggregate, ltext, lmanifest,
                                     r1, r2)
            if table is None:
                continue
            instant = ACT_INSTANT.findall(ltext)
            if (len(instant) != 1 or len(reached) != 1
                    or not instant[0] > reached[0]):
                r2.append(f"{ltag}: act instant {instant} is not strictly "
                          f"later than the act before it {reached}")
            reached = instant
            position = aggregate_position(later, aggregate, ltext)
            dates = [i[:10] for i in instant]
            for path, (pred, succ) in sorted(table.items()):
                if path not in rows:
                    r2.append(f"{ltag}: `{path}` is not a subject of this "
                              "child")
                elif pred != rows[path]:
                    r2.append(f"{ltag}: broken chain — the predecessor of "
                              f"`{path}` is not the row the chain reached")
                else:
                    rows[path] = succ
        for path, digest in sorted(rows.items()):
            subjects_seen += 1
            current = read_bytes(root, path)
            if current is None:
                r2.append(f"{tag}: signed subject `{path}` missing")
            elif sha(current) != digest:
                r2.append(f"{tag}: stale digest — `{path}` no longer hashes "
                          "to its signed row")
    # Signed Polaris additions (reconciled-child hook): each installed
    # addition is a child whose terminal outcome is its versioned sign-off.
    additions = polaris_additions(root)
    for change, spec_rel in additions:
        tag = f"polaris addition {change}"
        found = addition_records(root, change)
        records += max(1, len(found))
        if not found:
            r1.append(f"{tag}: unsigned addition — `{spec_rel}` is installed "
                      f"but no `{SIGNOFF_RECORD_GLOB}` record names `Package: "
                      f"{change}`; the outcome is Unknown")
        versions = [v for _r, _t, v in found]
        for version in sorted({v for v in versions if v and versions.count(v) > 1}):
            r1.append(f"{tag}: {versions.count(version)} records sign version "
                      f"{version}; expected one")
        for rel, text, version in found:
            if version is None:
                r1.append(f"{tag}: `{rel}` carries no single `Version:` line")
                continue
            check_versioned({"package": change, "version": version},
                            f"{tag} ({Path(rel).name})", aggregate, text, r1)
    report.add("R1", "terminal outcome for every child", records, r1,
               f"{len(CHILDREN)} children and {len(additions)} signed Polaris "
               "additions; digest acts: phrase = manifest sha256 and in the "
               "aggregate; versioned: package/version/tag and one aggregate "
               "block")
    report.add("R2", "signed subjects hash to their rows", subjects_seen, r2)


# --------------------------------------------------------------------------
# R3: populations, two methods each.
# --------------------------------------------------------------------------

def parse_regex(text, prefix):
    """Method A: regular expressions over headings."""
    reqs = {}
    order = []
    marks = [(m.start(), "R", m.group(1), m.group(2)) for m in re.finditer(
        rf"^### Requirement: ({re.escape(prefix)}-REQ-\d{{3}}) — (.+?)[ \t]*$",
        text, re.M)]
    marks += [(m.start(), "S", m.group(1), None) for m in re.finditer(
        r"^#### Scenario: (.+?)[ \t]*$", text, re.M)]
    current = None
    dupes = []
    for _pos, kind, value, name in sorted(marks):
        if kind == "R":
            if value in reqs:
                dupes.append(value)
            reqs[value] = {"name": name, "scenarios": []}
            order.append(value)
            current = value
        elif current is None:
            dupes.append(f"scenario before any requirement: {value}")
        else:
            reqs[current]["scenarios"].append(value)
    return reqs, dupes


def parse_manual(text, prefix):
    """Method B: a line state machine with no regular expressions."""
    reqs, dupes, current = {}, [], None
    head_r, head_s = "### Requirement: ", "#### Scenario: "
    for line in text.split("\n"):
        if line.startswith(head_r):
            rest = line[len(head_r):]
            ident, sep, name = rest.partition(" — ")
            if not sep or not ident.startswith(prefix + "-REQ-"):
                dupes.append(f"unparsed requirement heading: {rest[:40]}")
                current = None
                continue
            if ident in reqs:
                dupes.append(ident)
            reqs[ident] = {"name": name.rstrip(" \t"), "scenarios": []}
            current = ident
        elif line.startswith(head_s):
            if current is None:
                dupes.append("scenario before any requirement")
            else:
                reqs[current]["scenarios"].append(
                    line[len(head_s):].rstrip(" \t"))
    return reqs, dupes


def _polaris_blocks_regex(text):
    sections = list(re.finditer(
        r"^## (ADDED|MODIFIED|REMOVED|RENAMED) Requirements[ \t]*$", text, re.M))
    out = []
    for i, sec in enumerate(sections):
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        body = text[sec.end():end]
        heads = list(re.finditer(r"^### Requirement: (.+?)[ \t]*$", body, re.M))
        for j, head in enumerate(heads):
            stop = heads[j + 1].start() if j + 1 < len(heads) else len(body)
            block = body[head.start():stop]
            ids = re.findall(rf"^ID: ({POLARIS_ID}\d{{3}})[ \t]*$", block, re.M)
            scen = re.findall(r"^#### Scenario: (.+?)[ \t]*$", block, re.M)
            out.append((sec.group(1), ids, head.group(1), scen))
    return out


ADDED_HEADING = "## ADDED Requirements"
DELTA_WORDS = ("added", "modified", "removed", "renamed")


def _foreign_headings_regex(text):
    """Method A: every heading a signed addition may not carry.

    Fails closed, independent of requirement blocks: any level-2 heading
    other than exactly `## ADDED Requirements`, and any heading of any level,
    case or spacing that names a delta section, unless it is that line.
    """
    level2 = re.findall(r"^[ \t]*##(?!#)[^\n]*$", text, re.M)
    delta = re.findall(r"^[ \t]*#+[ \t]*(?:added|modified|removed|renamed)[ \t]+"
                       r"requirements?\b[^\n]*$", text, re.M | re.I)
    return [h for h in dict.fromkeys(level2 + delta) if h != ADDED_HEADING]


def _foreign_headings_manual(text):
    """Method B: the same set, by a line scan with no regular expressions."""
    out = []
    for line in text.split("\n"):
        if line == ADDED_HEADING:
            continue
        stripped = line.lstrip(" \t")
        if not stripped.startswith("#"):
            continue
        hashes = len(stripped) - len(stripped.lstrip("#"))
        words = stripped.lstrip("#").split()
        names_delta = (len(words) >= 2 and words[0].casefold() in DELTA_WORDS
                       and words[1].casefold().rstrip("s") == "requirement")
        if (hashes == 2 or names_delta) and line not in out:
            out.append(line)
    return out


def compose_polaris_by_id(base, overlay, *additions):
    """Method A: compose base + overlay (+ signed additions) by ID line.

    Each addition is a (label, text) pair and may only ADD requirements.
    """
    comp, problems = {}, []
    for label, text in additions:
        problems += [f"addition {label}: heading `{h.strip()}`; a signed addition "
                     "is ADDED-only" for h in _foreign_headings_regex(text)]
    for label, text in (("base", base), ("overlay", overlay), *additions):
        for kind, ids, name, scen in _polaris_blocks_regex(text):
            if label not in ("base", "overlay") and kind != "ADDED":
                problems.append(f"addition {label}: {kind} section; a signed "
                                "addition is ADDED-only")
                continue
            if len(ids) != 1:
                problems.append(f"{label} `{name}`: {len(ids)} ID lines")
                continue
            ident = ids[0]
            if kind == "ADDED":
                if ident in comp:
                    problems.append(f"{label}: ADDED {ident} already composed")
                comp[ident] = {"name": name, "scenarios": scen}
            elif kind == "MODIFIED":
                if ident not in comp:
                    problems.append(f"{label}: MODIFIED {ident} is dangling")
                comp[ident] = {"name": name, "scenarios": scen}
            else:
                problems.append(f"{label}: unsupported {kind} section")
    return comp, problems


def _polaris_blocks_manual(text):
    out, section, current = [], None, None
    for line in text.split("\n"):
        if line.startswith("## ") and line.rstrip().endswith(" Requirements"):
            section = line[3:].split(" ", 1)[0]
            current = None
        elif line.startswith("### Requirement: "):
            current = {"section": section,
                       "name": line[len("### Requirement: "):].rstrip(" \t"),
                       "ids": [], "scenarios": []}
            out.append(current)
        elif current is not None and line.startswith("ID: " + POLARIS_ID):
            current["ids"].append(line[4:].rstrip(" \t"))
        elif current is not None and line.startswith("#### Scenario: "):
            current["scenarios"].append(
                line[len("#### Scenario: "):].rstrip(" \t"))
    return out


def compose_polaris_by_name(base, overlay, *additions):
    """Method B: compose by normalized requirement name; IDs attached last."""
    comp, problems = {}, []

    def norm(name):
        return " ".join(name.split()).casefold()

    for label, text in additions:
        problems += [f"addition {label}: heading `{h.strip()}`; a signed addition "
                     "is ADDED-only" for h in _foreign_headings_manual(text)]
    for label, text in (("base", base), ("overlay", overlay), *additions):
        for block in _polaris_blocks_manual(text):
            key = norm(block["name"])
            if label not in ("base", "overlay") and block["section"] != "ADDED":
                problems.append(f"addition {label}: {block['section']} "
                                "section; a signed addition is ADDED-only")
                continue
            if block["section"] == "ADDED":
                if key in comp:
                    problems.append(f"{label}: ADDED `{block['name']}` collides")
                comp[key] = block
            elif block["section"] == "MODIFIED":
                if key not in comp:
                    problems.append(
                        f"{label}: MODIFIED `{block['name']}` is dangling")
                comp[key] = block
            else:
                problems.append(f"{label}: unsupported {block['section']} section")
    by_id = {}
    for block in comp.values():
        if len(block["ids"]) != 1:
            problems.append(f"`{block['name']}`: {len(block['ids'])} ID lines")
            continue
        if block["ids"][0] in by_id:
            problems.append(f"duplicate {block['ids'][0]}")
        by_id[block["ids"][0]] = {"name": block["name"],
                                  "scenarios": block["scenarios"]}
    return by_id, problems


def census(root):
    """Return ({family: {id: {name, scenarios}}}, findings)."""
    out, findings = {}, []
    for family, rel in FAMILY_SPECS.items():
        text = read_text(root, rel)
        if text is None:
            findings.append(f"{family}: `{rel}` missing")
            continue
        a, pa = parse_regex(text, family)
        b, pb = parse_manual(text, family)
        findings += [f"{family} method A: duplicate or orphan {p}" for p in pa]
        findings += [f"{family} method B: duplicate or orphan {p}" for p in pb]
        if a != b:
            findings.append(f"{family}: the two methods disagree "
                            f"({len(a)} vs {len(b)} requirements)")
        out[family] = a
    base = read_text(root, POLARIS_BASE_SPEC)
    overlay = read_text(root, POLARIS_OVERLAY_SPEC)
    additions = [(change, read_text(root, rel))
                 for change, rel in polaris_additions(root)]
    for change, _text in additions:
        if not addition_records(root, change):
            findings.append(f"POLARIS: addition `{change}` has no versioned "
                            "sign-off record, so its requirements are not "
                            "expected")
    if base is None or overlay is None:
        findings.append("POLARIS: base or overlay spec missing")
    else:
        a, pa = compose_polaris_by_id(base, overlay, *additions)
        b, pb = compose_polaris_by_name(base, overlay, *additions)
        findings += [f"POLARIS method A: {p}" for p in pa]
        findings += [f"POLARIS method B: {p}" for p in pb]
        if a != b:
            findings.append("POLARIS: ID-keyed and name-keyed compositions "
                            "disagree")
        out["POLARIS"] = a
    return out, findings


def census_json(pop):
    doc = {"note": "Generated by scripts/check_spec_reconciliation.py "
                   "--census; requirement identity, name and scenario titles "
                   "in the effective composition. Navigation evidence, "
                   "never authority.",
           "families": {}}
    for family in ("CAP1", "POC", "PWB", "POLARIS"):
        reqs = pop.get(family, {})
        doc["families"][family] = {
            "requirements": len(reqs),
            "scenarios": sum(len(r["scenarios"]) for r in reqs.values()),
            "members": {k: reqs[k] for k in sorted(reqs)},
        }
    return json.dumps(doc, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def polaris_expected(root, findings):
    """Expected Polaris (requirements, scenarios, ids), derived.

    The base-and-overlay literal (31 / 182, IDs 001–031) plus, for each signed
    addition, the requirements that addition ADDs, read by both block parsers
    from the addition alone (never from the composition) and required to agree.
    """
    n_req, n_scen = EXPECTED_TOTALS["POLARIS"]
    ids = {f"{POLARIS_ID}{i:03d}" for i in range(1, n_req + 1)}
    for change, rel in polaris_additions(root):
        if not addition_records(root, change):
            continue
        text = read_text(root, rel) or ""
        by_regex = sorted((tuple(i), len(s)) for kind, i, _n, s in
                          _polaris_blocks_regex(text) if kind == "ADDED")
        by_lines = sorted((tuple(b["ids"]), len(b["scenarios"])) for b in
                          _polaris_blocks_manual(text) if b["section"] == "ADDED")
        if by_regex != by_lines:
            findings.append(f"POLARIS addition `{change}`: the two parsers "
                            "disagree on what it adds")
        added = {i[0] for i, _s in by_regex if len(i) == 1}
        if added & ids:
            findings.append(f"POLARIS addition `{change}`: re-adds "
                            f"{sorted(added & ids)}")
        ids |= added
        n_req += len(by_regex)
        n_scen += sum(s for _i, s in by_regex)
    return n_req, n_scen, ids


def check_census(root, report):
    pop, findings = census(root)
    examined = 0
    p_req, p_scen, p_ids = polaris_expected(root, findings)
    totals = dict(EXPECTED_TOTALS, POLARIS=(p_req, p_scen))
    for family, (n_req, n_scen) in totals.items():
        reqs = pop.get(family, {})
        got = (len(reqs), sum(len(r["scenarios"]) for r in reqs.values()))
        examined += got[0]
        if got != (n_req, n_scen):
            findings.append(f"{family}: {got[0]} requirements / {got[1]} "
                            f"scenarios, expected {n_req} / {n_scen}")
        literal = EXPECTED.get(family)
        if literal is not None:
            prefix = f"{family}-REQ-"
            have = {k[len(prefix):]: len(v["scenarios"]) for k, v in reqs.items()}
            if have != literal:
                diff = sorted(set(have.items()) ^ set(literal.items()))
                findings.append(f"{family}: per-requirement census differs "
                                f"from the literal at {diff[:6]}")
        elif family == "POLARIS":
            if set(reqs) != p_ids:
                findings.append("POLARIS: identities are not exactly 001–031 "
                                "and the signed additions' IDs "
                                f"(off by {sorted(set(reqs) ^ p_ids)[:6]})")
    committed = read_text(root, CENSUS)
    if committed is None:
        findings.append(f"`{CENSUS}` missing")
    elif committed != census_json(pop):
        findings.append(f"`{CENSUS}` differs from regeneration "
                        "(a name or scenario title moved)")
    report.add("R3", "populations agree by two methods and match the census",
               examined, findings,
               "requirements examined across CAP1, POC, PWB and Polaris")
    return pop


# --------------------------------------------------------------------------
# R4: generated dependency and coverage rows.
# --------------------------------------------------------------------------

def tracked(root, prefix):
    """Tracked files under `prefix` (git when available, else the tree)."""
    if (root / ".git").exists():
        out = subprocess.run(["git", "ls-files", "-z", "--", prefix], cwd=root,
                             capture_output=True, check=True).stdout
        return sorted(p for p in out.decode("utf-8").split("\0") if p)
    base = root / prefix
    if base.is_file():
        return [prefix]
    return sorted(p.relative_to(root).as_posix()
                  for p in base.rglob("*") if p.is_file())


def check_generated(root, pop, report):
    findings, examined = [], 0
    for family, change in (("CAP1", CAP1_CHANGE), ("POC", POC_CHANGE),
                           ("PWB", PWB_CHANGE)):
        rel = f"{CHANGES}/{change}/GOVERNING-DEPENDENCIES.md"
        text = read_text(root, rel) or ""
        found = DEPS_SOURCE.findall(text)
        examined += 1
        spec = read_bytes(root, FAMILY_SPECS[family]) or b""
        if len(found) != 1:
            findings.append(f"`{rel}`: {len(found)} source lines, expected 1")
        elif found[0][0] != sha(spec):
            findings.append(f"`{rel}`: source digest is not the current "
                            "spec.md")
        elif int(found[0][1]) != len(pop.get(family, {})):
            findings.append(f"`{rel}`: states {found[0][1]} requirements, "
                            f"census has {len(pop.get(family, {}))}")
    for family, change in (("CAP1", CAP1_CHANGE), ("PWB", PWB_CHANGE)):
        rel = f"{CHANGES}/{change}/CAPABILITY-COVERAGE.md"
        cited = set(re.findall(rf"\b{family}-REQ-\d{{3}}\b",
                               read_text(root, rel) or ""))
        examined += 1
        if cited != set(pop.get(family, {})):
            findings.append(f"`{rel}`: covers {len(cited)} of "
                            f"{len(pop.get(family, {}))} requirements")
    numbers = {fam: {k[-3:] for k in reqs} for fam, reqs in pop.items()}
    files = []
    for child in CHILDREN:
        files += tracked(root, f"{CHANGES}/{child['change']}")
    addition_dirs = tuple(f"{CHANGES}/{change}/"
                          for change, _rel in polaris_additions(root))
    for prefix in addition_dirs:
        files += tracked(root, prefix.rstrip("/"))
    files += list(ROUTE_PAGES)
    # An addition may cite a candidate Polaris requirement still under
    # another change's `proposed/` (no act binds it); such a mention resolves
    # to that candidate and is counted apart, never as in force.
    candidates = set()
    for spec in sorted((root / CHANGES).glob("*/proposed/polaris-generation/"
                                             "spec.md")):
        candidates |= {i[-3:] for kind, ids, _n, _s in _polaris_blocks_regex(
            spec.read_text(encoding="utf-8")) if kind == "ADDED" for i in ids}
    mentions = candidate_refs = 0
    for rel in files:
        if not rel.endswith((".md", ".json", ".yaml")):
            continue
        text = read_text(root, rel)
        if text is None:
            continue
        for m in ID_MENTION.finditer(text):
            family = m.group(1) or "POLARIS"
            for num in [m.group(2)] + re.findall(r"\d{3}", m.group(3)):
                mentions += 1
                if (family == "POLARIS" and rel.startswith(addition_dirs)
                        and num not in numbers.get(family, set())
                        and num in candidates):
                    candidate_refs += 1
                    continue
                if num not in numbers.get(family, set()):
                    findings.append(f"`{rel}`: {family} identifier {num} "
                                    f"resolves to no requirement "
                                    f"(in `{m.group(0)[:48]}`)")
    # A signed addition's union is generated, never signed, so a difference
    # is a FAIL here rather than R7's report-only Unknown.
    for change, spec_rel in polaris_additions(root):
        rel = f"{CHANGES}/{change}/GOVERNING-DEPENDENCIES.md"
        spec, deps = read_text(root, spec_rel), read_text(root, rel)
        examined += 1
        if spec is None or deps is None:
            findings.append(f"`{rel}` or its spec missing")
            continue
        computed, declared = warrant_union(spec), declared_union(deps)
        if computed != declared:
            findings.append(f"`{rel}`: differs from its spec's warrants; run "
                            "`--regenerate`")
    report.add("R4", "generated dependency and coverage rows resolve",
               examined + mentions, findings,
               f"{examined} generated anchors, {mentions} identifier mentions "
               f"(full and continuation forms) over {len(files)} files, "
               f"{candidate_refs} of them an addition's reference to a "
               "candidate Polaris requirement under `proposed/`")


# --------------------------------------------------------------------------
# R5: default routes.
# --------------------------------------------------------------------------

def check_routes(root, pop, report):
    findings, examined = [], 0
    readme = read_text(root, OPENSPEC_README) or ""
    status = read_text(root, STATUS) or ""
    changes = sorted({p.split("/")[2] for p in tracked(root, CHANGES)
                      if p.count("/") >= 3})
    changes = [c for c in changes if c != "archive"]
    rows = {}
    for line in readme.splitlines():
        m = re.match(r"^\| \[`([^`]+)`\]\(changes/", line)
        if m:
            rows.setdefault(m.group(1), []).append(line)
    for change in changes:
        examined += 1
        if len(rows.get(change, [])) != 1:
            findings.append(f"`{OPENSPEC_README}`: {len(rows.get(change, []))} "
                            f"rows for tracked change `{change}`, expected 1")
    for extra in sorted(set(rows) - set(changes)):
        findings.append(f"`{OPENSPEC_README}`: row for untracked `{extra}`")
    for child in CHILDREN:
        for record in (child["record"], *(later["record"] for later in
                                          child.get("successors", ()))):
            examined += 2
            name = Path(record).name
            if not any(name in line for line in rows.get(child["change"], [])):
                findings.append(f"`{OPENSPEC_README}`: the `{child['change']}` "
                                f"row does not name its terminal record "
                                f"`{name}`")
            if record not in status and name not in status:
                findings.append(f"`{STATUS}` cites no terminal record `{name}`")
    for change, _rel in polaris_additions(root):
        for record, _text, _version in addition_records(root, change):
            examined += 2
            name = Path(record).name
            if not any(name in line for line in rows.get(change, [])):
                findings.append(f"`{OPENSPEC_README}`: the `{change}` row does "
                                f"not name its terminal record `{name}`")
            if record not in status and name not in status:
                findings.append(f"`{STATUS}` cites no terminal record `{name}`")
    figures = STATUS_FIGURE.findall(status)
    examined += 1
    reqs = pop.get("POLARIS", {})
    want = (str(len(reqs)), str(sum(len(r["scenarios"]) for r in reqs.values())))
    if figures != [want]:
        findings.append(f"`{STATUS}`: Polaris composition figure {figures} "
                        f"!= census {want}")
    report.add("R5", "default routes name the terminal records", examined,
               findings, f"{len(changes)} tracked change directories")


# --------------------------------------------------------------------------
# R6: behaviour-contract pins (reported, never green, never repaired).
# --------------------------------------------------------------------------

def check_pins(root, report):
    spec = read_bytes(root, FAMILY_SPECS["PWB"]) or b""
    current = "sha256:" + sha(spec)
    findings, examined = [], 0

    def pins(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "governingBehaviorContract" and isinstance(value, dict):
                    yield value.get("version")
                else:
                    yield from pins(value)
        elif isinstance(node, list):
            for value in node:
                yield from pins(value)

    for rel in (REGISTRY, POLICY):
        text = read_text(root, rel)
        if text is None:
            findings.append(f"`{rel}` missing: pin Unknown")
            continue
        found = list(pins(json.loads(text)))
        if not found:
            findings.append(f"`{rel}`: no governingBehaviorContract; "
                            "pin Unknown")
        for pinned in found:
            examined += 1
            if pinned != current:
                findings.append(
                    f"`{rel}`: pins {pinned}, current PWB spec.md is "
                    f"{current} — Unknown until its own owner act "
                    f"({PIN_BEAD})")
    report.warn("R6", "behaviour-contract pins (report only)", examined,
                findings,
                "a stale pin is Unknown, never green; repair needs an owner "
                "act this checker never performs")


# --------------------------------------------------------------------------
# R7: Polaris dependency unions (reported, never green, never repaired).
# --------------------------------------------------------------------------

WARRANTS = re.compile(r"^```yaml\nwarrants:\n(.*?)^```", re.M | re.S)


def warrant_union(text):
    """Union of every warrant class over one spec's warrants blocks."""
    union = {}
    for block in WARRANTS.findall(text):
        key = None
        for line in block.split("\n"):
            m = re.match(r"^  (\w+):[ \t]*(.*?)[ \t]*$", line)
            if m:
                key, value = m.group(1), m.group(2)
                union.setdefault(key, set())
                if value.startswith("[") and value.endswith("]"):
                    union[key] |= {v.strip() for v in value[1:-1].split(",")
                                   if v.strip()}
                elif value:
                    union[key].add(value)
                continue
            m = re.match(r"^\s+- (.+?)[ \t]*$", line)
            if m and key:
                union[key].add(m.group(1))
    return union


def declared_union(text):
    """The classes a generated union file declares (JSON or `## class` lists)."""
    m = re.search(r"```json\n(.*?)```", text, re.S)
    if m:
        return {k: set(v) for k, v in json.loads(m.group(1)).items()}
    out = {}
    for sec in re.finditer(r"^## (\w+)\n\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        body = sec.group(2).strip()
        out[sec.group(1)] = (set() if body.startswith("None declared")
                             else {v.strip() for v in body.split(",") if v.strip()})
    return out


def check_unions(root, report):
    findings, examined = [], 0
    for spec_rel, change in ((POLARIS_BASE_SPEC, BASE_CHANGE),
                             (POLARIS_OVERLAY_SPEC, UNDERSTANDING_CHANGE)):
        rel = f"{CHANGES}/{change}/GOVERNING-DEPENDENCIES.md"
        spec, deps = read_text(root, spec_rel), read_text(root, rel)
        if spec is None or deps is None:
            findings.append(f"`{rel}` or its spec missing: union Unknown")
            continue
        computed, declared = warrant_union(spec), declared_union(deps)
        if "primary" not in declared:
            # The base union is declared over the six warrant classes only.
            computed.pop("primary", None)
        for cls in sorted(set(computed) | set(declared)):
            examined += 1
            missing = sorted(computed.get(cls, set()) - declared.get(cls, set()))
            extra = sorted(declared.get(cls, set()) - computed.get(cls, set()))
            if missing or extra:
                findings.append(
                    f"`{rel}` {cls}: lacks {missing}, carries extra {extra} — "
                    f"bound bytes; Unknown until a signed successor "
                    f"({UNION_BEAD})")
    report.warn("R7", "Polaris dependency unions match their warrants "
                "(report only)", examined, findings,
                "regenerated by scripts/build_polaris_dependency_unions.py; "
                "a change to a signed union needs a signed successor")


def run(root):
    report = Report()
    check_outcomes(root, report)
    pop = check_census(root, report)
    check_generated(root, pop, report)
    check_routes(root, pop, report)
    check_pins(root, report)
    check_unions(root, report)
    return report


# --------------------------------------------------------------------------
# Self-test: rule-6 mutations over a scratch copy of the inputs.
# --------------------------------------------------------------------------

def inputs(root):
    paths = {AGGREGATE, CENSUS, STATUS, REGISTRY, POLICY, *ROUTE_PAGES}
    for child in CHILDREN:
        paths |= {child["record"], child["manifest"]}
        for later in child.get("successors", ()):
            paths |= {later["record"], later["manifest"]}
            if "proposed" in later:
                paths |= set(tracked(root, later["proposed"]))
        manifest = read_text(root, child["manifest"]) or ""
        paths |= {p for _d, p in ROW.findall(manifest)}
        paths |= set(tracked(root, f"{CHANGES}/{child['change']}"))
    paths |= set(tracked(root, CHANGES))
    for change, rel in polaris_additions(root):
        paths |= {rel} | {r for r, _t, _v in addition_records(root, change)}
    return sorted(paths)


def scratch(root, dest):
    for rel in inputs(root):
        src = root / rel
        if src.is_file():
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest / rel)


def _replace(old, new, count=1):
    def apply(text):
        if old not in text:
            raise AssertionError(f"mutation target absent: {old[:60]!r}")
        return text.replace(old, new, count)
    return apply


def _first_hex_flip(label):
    def apply(text):
        m = re.search(rf"^{re.escape(label)}: ([0-9a-f]{{64}})$", text, re.M)
        arg = m.group(1)
        flipped = ("1" if arg[0] != "1" else "2") + arg[1:]
        return text.replace(f"{label}: {arg}", f"{label}: {flipped}")
    return apply


def _pin_moved(root):
    current = sha(read_bytes(root, FAMILY_SPECS["PWB"]) or b"")

    def apply(text):
        def swap(m):
            target = current if m.group(2) != current else "0" * 64
            return m.group(1) + target + '"'
        return re.sub(r'("version": "sha256:)([0-9a-f]{64})"', swap, text, 1)
    return apply


def _repin_package(root, module="build_pwb_behavior_contract_repin"):
    """Map each pinned subject's current text to a re-pin package's bytes."""
    sys.path.insert(0, str(root / "scripts"))
    repin = __import__(module)
    by_text = {}
    for subject in repin.SUBJECTS:
        current = read_text(root, subject.path.as_posix())
        by_text[current] = repin.proposed_bytes(root, subject).decode("utf-8")
    # The spec.md bytes the pins name: the tree with every later signed
    # spec.md patch reversed (identity until a later sign-off moves it).
    by_text[read_text(root, FAMILY_SPECS["PWB"])] = (
        repin.spec_at_pin(root).decode("utf-8"))

    def apply(text):
        if text not in by_text:
            raise AssertionError("pinned subject differs from the tree it was read from")
        return by_text[text]
    return apply


def _union_successor(root):
    """The understanding union as the c51h successor package proposes it."""
    rel = f"{CHANGES}/{UNDERSTANDING_CHANGE}/GOVERNING-DEPENDENCIES.md"
    proposed = read_text(root, f"{UNION_SUCCESSOR}/proposed/{rel}.proposed")

    def apply(text):
        if proposed is None:
            raise AssertionError("the union successor package proposes no union")
        return proposed
    return apply


def _removed_line_altered(text):
    """Alter the first removed content line of a patch: it still reverses,
    but to bytes that are not the row the chain reached."""
    lines = text.split("\n")
    i = next((i for i, line in enumerate(lines)
              if line.startswith("-") and not line.startswith("---")), None)
    if i is None:
        raise AssertionError("patch carries no removed content line")
    lines[i] += " x"
    return "\n".join(lines)


def _block_moved_before(marker, before):
    """Move one aggregate block (marker to its closing marker) to sit before
    another marker, so append order no longer matches act order."""
    close = marker.replace("<!-- ", "<!-- /", 1)

    def apply(text):
        start, end = text.find(marker), text.find(close)
        at = text.find(before)
        if min(start, end, at) < 0 or not at < start:
            raise AssertionError("aggregate blocks not found in act order")
        end += len(close) + 1
        block = text[start:end]
        rest = text[:start] + text[end:]
        at = rest.find(before)
        return rest[:at] + block + "\n" + rest[at:]
    return apply


def _chain_predecessor_moved(text):
    """Point every row of a successor record's table at a digest no act signed."""
    out, n = ACT_TABLE_ROW.subn(
        lambda m: f"| `{m.group(1)}` | `{'0' * 64}` | `{m.group(3)}` |", text)
    if not n:
        raise AssertionError("successor record carries no signed-subject row")
    return out


def mutants(root):
    cap1, poc, base, und, pwb = CHILDREN
    union_act = und["successors"][0]
    tree_act = pwb["successors"][0]
    poc_spec = FAMILY_SPECS["POC"]
    pwb_spec = FAMILY_SPECS["PWB"]
    return (
        ("stale-act-phrase", cap1["record"], _first_hex_flip(cap1["label"]),
         "R1"),
        ("stale-act-aggregate", AGGREGATE, _first_hex_flip(und["label"]), "R1"),
        # Record and aggregate flipped together: only the manifest-digest
        # comparison can see it.
        ("stale-act-consistent", (poc["record"], AGGREGATE),
         _first_hex_flip(poc["label"]), "R1"),
        ("stale-manifest-row", base["manifest"],
         lambda t: t.replace(ROW.search(t).group(1),
                             "0" * 64, 1), "R1"),
        ("stale-subject-digest", f"{CHANGES}/{POC_CHANGE}/proposal.md",
         lambda t: t + "\n", "R2"),
        ("stale-versioned-subject", f"{CHANGES}/{PWB_CHANGE}/design.md",
         lambda t: t.replace(" ", "  ", 1), "R2"),
        ("missing-child-pwb", pwb["record"], None, "R1"),
        ("missing-child-understanding", und["record"], None, "R1"),
        ("versioned-tag-line", pwb["record"],
         _replace("Tag: pwb-readability-successor-v1.0",
                  "Tag: pwb-readability-successor-v0.9"), "R1"),
        ("versioned-aggregate-block", AGGREGATE,
         _replace("<!-- versioned-signoff:pwb-readability-successor:v1.0 -->",
                  "<!-- versioned-signoff:pwb-readability-successor:v1.1 -->"),
         "R1"),
        ("scenario-removed", poc_spec,
         _replace("#### Scenario: ", "#### Scenery: "), "R3"),
        ("duplicate-id", pwb_spec,
         _replace("### Requirement: PWB-REQ-002 — ",
                  "### Requirement: PWB-REQ-001 — "), "R3"),
        # Seen by one method and not the other: an em dash lost from a
        # heading, and a MODIFIED name that no longer matches its base.
        ("method-split-heading", poc_spec,
         _replace("### Requirement: POC-REQ-010 — ",
                  "### Requirement: POC-REQ-010 - "), "R3"),
        ("polaris-renamed-modified", POLARIS_OVERLAY_SPEC,
         _replace("### Requirement: Understandable reading depths\n",
                  "### Requirement: Understandable reading depth\n"), "R3"),
        ("polaris-dangling-modified", POLARIS_OVERLAY_SPEC,
         _replace("ID: REQ-polaris-generation-002\n",
                  "ID: REQ-polaris-generation-099\n"), "R3"),
        ("census-drift", CENSUS, _replace('"scenarios": [\n',
                                          '"scenarios": [\n        "x",\n'),
         "R3"),
        ("deps-source-digest", f"{CHANGES}/{POC_CHANGE}/GOVERNING-DEPENDENCIES.md",
         lambda t: re.sub(r"sha256 `[0-9a-f]", "sha256 `f", t, 1)
         if "sha256 `f" not in t else re.sub(r"sha256 `f", "sha256 `0", t, 1),
         "R4"),
        ("dangling-coverage-id",
         f"{CHANGES}/{CAP1_CHANGE}/CAPABILITY-COVERAGE.md",
         lambda t: t + "\nCAP1-REQ-099\n", "R4"),
        ("dangling-continuation-id", "AGENTS.md",
         lambda t: t + "\nPWB-REQ-005/009\n", "R4"),
        ("route-row-record", OPENSPEC_README,
         _replace("PWB-READABILITY-SUCCESSOR-SIGNOFF-v1.0.md",
                  "PWB-READABILITY-SUCCESSOR-ACT.md", -1), "R5"),
        # Report-only predicates: the mutant must change what they report.
        # Once the pin is current (after the syzygy-jloi acts) the mutant
        # moves it off the current digest instead, so it still changes R6.
        ("pin-made-current", POLICY, _pin_moved(root), "R6~"),
        # The syzygy-jloi package's proposed bytes, as its recorder applies
        # them at the act: R6 must then report exactly zero. After the acts
        # the tree already carries those bytes and R6 must read zero there.
        # spec.md is replayed at the pinned row (later signed patches
        # reversed); once a later sign-off moved it, R2-R4 fail by design.
        ("pins-after-repin-acts", (REGISTRY, POLICY, FAMILY_SPECS["PWB"]),
         _repin_package(root), "R6=0|R2,R3,R4"),
        # The syzygy-2g0d package's proposed bytes, pinned to the current
        # (tree-framing) spec.md: R6 reads zero and nothing else fails.
        ("pins-after-tree-framing-repin-acts",
         (REGISTRY, POLICY, FAMILY_SPECS["PWB"]),
         _repin_package(root, "build_pwb_behavior_contract_repin_tree_framing"),
         "R6=0"),
        # The syzygy-c51h successor package's proposed union, as
        # readability_successor.py installs it at the act: R7 must then
        # report exactly zero. Before the re-derivation R2 failed by design
        # over the readability act's superseded row ("R7=0|R2"); with the act
        # named as the understanding child's successor nothing else fails.
        ("union-after-successor-act",
         f"{CHANGES}/{UNDERSTANDING_CHANGE}/GOVERNING-DEPENDENCIES.md",
         _union_successor(root), "R7=0"),
        # The understanding child's later successor (re-derived 2026-10-02).
        ("missing-successor-record", union_act["record"], None, "R1"),
        ("stale-successor-aggregate", AGGREGATE,
         _first_hex_flip(union_act["label"]), "R1"),
        ("successor-broken-chain", union_act["record"],
         _chain_predecessor_moved, "R2"),
        ("successor-instant-order", union_act["record"],
         lambda t: re.sub(r"^Act instant: \S+$",
                          "Act instant: 2026-09-01T00:00:00Z", t, 1, re.M), "R2"),
        ("route-successor-record", OPENSPEC_README,
         _replace(Path(union_act["record"]).name, "DEPENDENCY-UNION-ACT.md", -1),
         "R5"),
        # The PWB child's later version-tagged successor (re-derived
        # 2026-10-03): its record, aggregate block, order and patches.
        ("missing-versioned-successor", tree_act["record"], None, "R1"),
        ("versioned-successor-tag", tree_act["record"],
         _replace("Tag: pwb-tree-framing-amendment-v1.0",
                  "Tag: pwb-tree-framing-amendment-v0.9"), "R1"),
        ("versioned-successor-aggregate", AGGREGATE,
         _replace(versioned_marker(tree_act),
                  versioned_marker(dict(tree_act, version="1.1"))), "R1"),
        ("versioned-successor-order", AGGREGATE,
         _block_moved_before(versioned_marker(tree_act),
                             versioned_marker(pwb)), "R2"),
        ("versioned-successor-date", tree_act["record"],
         _replace("Date: 2026-10-03", "Date: 2026-09-01"), "R2"),
        # The tree still hashes to every row: only the chain sees these.
        ("versioned-successor-reversal", f"{tree_act['proposed']}/spec.md.patch",
         _removed_line_altered, "R2"),
        ("versioned-successor-patch-missing",
         f"{tree_act['proposed']}/design.md.patch", None, "R2"),
        ("versioned-successor-foreign-patch",
         f"{tree_act['proposed']}/proposal.md.patch",
         _replace(f"+++ b/{CHANGES}/{PWB_CHANGE}/proposal.md",
                  f"+++ b/{CHANGES}/{PWB_CHANGE}/proposal-x.md"), "R2"),
        ("route-versioned-successor", OPENSPEC_README,
         _replace(Path(tree_act["record"]).name, "PWB-TREE-FRAMING-ACT.md", -1),
         "R5"),
        ("union-extra-decision",
         f"{CHANGES}/{UNDERSTANDING_CHANGE}/GOVERNING-DEPENDENCIES.md",
         _replace("## decisions\n\nSDR-3\n", "## decisions\n\nSDR-3, SDR-99\n"),
         "R7~"),
        ("status-figure", STATUS, _status_figure_moved, "R5"),
    )


def _status_figure_moved(text):
    """The PROJECT-STATUS Polaris figure, five scenarios short."""
    m = STATUS_FIGURE.search(text)
    if not m:
        raise AssertionError("mutation target absent: the Polaris figure")
    return (text[:m.start(2)] + str(int(m.group(2)) - 5)
            + text[m.end(2):])


# A synthetic signed addition, installed by `_install_addition` into a scratch
# tree the way a version-tagged sign-off and `--regenerate` would leave it.
ADDITION = "polaris-selftest-addition"
ADDITION_RECORD = f"{DECISIONS}/POLARIS-SELFTEST-ADDITION-SIGNOFF-v1.0.md"
ADDITION_ID = f"{POLARIS_ID}099"
ADDITION_SPEC = (
    "## ADDED Requirements\n\n### Requirement: Selftest addition\n\n"
    f"ID: {ADDITION_ID}\n\n```yaml\nwarrants:\n"
    "  primary: [VIS-2]\n  doctrine: [VIS-2]\n  contracts: []\n"
    "  policies: []\n  decisions: []\n  topology: []\n"
    "  parent_requirements: []\n```\n\n"
    "#### Scenario: Selftest one\n\n- **WHEN** x\n- **THEN** y\n\n"
    "#### Scenario: Selftest two\n\n- **WHEN** x\n- **THEN** y\n")


def _install_addition(tree):
    """Sign, install and regenerate one synthetic addition in `tree`."""
    spec = tree / spec_path(ADDITION, "polaris-generation")
    spec.parent.mkdir(parents=True)
    spec.write_text(ADDITION_SPEC, encoding="utf-8")
    cited = _candidate_id(tree)
    (tree / CHANGES / ADDITION / "proposal.md").write_text(
        f"# Selftest addition\n\nAdds {ADDITION_ID}.\n"
        + (f"\nBeside the candidate {cited}.\n" if cited else ""),
        encoding="utf-8")
    marker = versioned_marker({"package": ADDITION, "version": "1.0"})
    (tree / ADDITION_RECORD).write_text(
        f"# Selftest\n\nDate: 2026-10-06\n\nPackage: {ADDITION}\n\n"
        f"Version: 1.0\n\nTag: {ADDITION}-v1.0\n", encoding="utf-8")
    with open(tree / AGGREGATE, "a", encoding="utf-8") as fh:
        fh.write(f"\n{marker}\nSelftest block.\n"
                 f"{marker.replace('<!-- ', '<!-- /')}\n")
    name = Path(ADDITION_RECORD).name
    with open(tree / OPENSPEC_README, "a", encoding="utf-8") as fh:
        fh.write(f"\n| [`{ADDITION}`](changes/{ADDITION}) | Selftest | "
                 f"Signed: `{name}` | — |\n")
    status = (tree / STATUS).read_text(encoding="utf-8")
    m = STATUS_FIGURE.search(status)
    status = (status[:m.start()] + f"{int(m.group(1)) + 1} requirements and "
              f"{int(m.group(2)) + 2} scenarios in the effective composition"
              + status[m.end():] + f"\nSelftest addition: `{name}`.\n")
    (tree / STATUS).write_text(status, encoding="utf-8")
    regenerate(tree)


def _candidate_id(root):
    """The first candidate Polaris ID under any change's `proposed/`, if any."""
    for spec in sorted((root / CHANGES).glob("*/proposed/polaris-generation/"
                                             "spec.md")):
        for kind, ids, _n, _s in _polaris_blocks_regex(
                spec.read_text(encoding="utf-8")):
            if kind == "ADDED" and ids:
                return ids[0]
    return None


def _restates_base(text):
    """The addition replaced by a verbatim MODIFIED copy of base 001.

    Composition, totals and census are then unchanged, so only the
    ADDED-only guard can see it.
    """
    base = (ROOT / POLARIS_BASE_SPEC).read_text(encoding="utf-8")
    heads = list(re.finditer(r"^#{2,3} ", base, re.M))
    for i, head in enumerate(heads):
        stop = heads[i + 1].start() if i + 1 < len(heads) else len(base)
        block = base[head.start():stop]
        if (block.startswith("### Requirement: ")
                and f"\nID: {POLARIS_ID}001\n" in block):
            return "## MODIFIED Requirements\n\n" + block
    raise AssertionError("mutation target absent: base 001")


def addition_mutants():
    union = f"{CHANGES}/{ADDITION}/GOVERNING-DEPENDENCIES.md"
    spec = spec_path(ADDITION, "polaris-generation")
    marker = versioned_marker({"package": ADDITION, "version": "1.0"})
    # Each guard is pinned in both methods: R3 must carry both findings.
    heading_both = (f"R3:method A: addition {ADDITION}: heading"
                    f"&method B: addition {ADDITION}: heading")
    modified_both = (f"R3:method A: addition {ADDITION}: MODIFIED section"
                     f"&method B: addition {ADDITION}: MODIFIED section")
    return (
        ("addition-unsigned", ADDITION_RECORD, None, "R1"),
        ("addition-unsigned-not-expected", ADDITION_RECORD, None,
         "R3:no versioned sign-off record"),
        # Fail-closed headings: a delta with no requirement block still fails.
        ("addition-renamed-section", spec,
         lambda t: t + "\n## RENAMED Requirements\n\n- FROM: `### Requirement: "
                       "Selftest addition`\n- TO: `### Requirement: Renamed`\n",
         heading_both),
        ("addition-removed-names-only", spec,
         lambda t: t + "\n## REMOVED Requirements\n\n- Selftest addition\n",
         heading_both),
        ("addition-lower-case-delta-heading", spec,
         lambda t: t + "\n## removed requirements\n", heading_both),
        ("addition-level-3-delta-heading", spec,
         lambda t: t + "\n### MODIFIED Requirements\n", heading_both),
        ("addition-respaced-added-heading", spec,
         _replace("## ADDED Requirements", "##  ADDED  Requirements"),
         heading_both),
        ("addition-other-level-2-heading", spec,
         lambda t: t + "\n## Notes\n\nProse.\n", heading_both),

        # A record naming another package does not sign this addition.
        ("addition-record-names-another-package", ADDITION_RECORD,
         _replace(f"Package: {ADDITION}\n", "Package: some-other-package\n"),
         "R1:unsigned addition"),
        ("addition-record-package", ADDITION_RECORD,
         _replace(f"Tag: {ADDITION}-v1.0", f"Tag: {ADDITION}-v0.9"), "R1"),
        ("addition-aggregate-block", AGGREGATE, _replace(marker, "<!-- x -->"),
         "R1"),
        ("addition-not-added-only", spec,
         _replace("## ADDED Requirements", "## MODIFIED Requirements"),
         modified_both),
        ("addition-restates-base", spec, _restates_base, modified_both),
        ("addition-re-adds-base-id", spec,
         _replace(f"ID: {ADDITION_ID}", f"ID: {POLARIS_ID}001"), "R3:re-adds"),
        # 030 is the overlay's own ADDED requirement, not the base's.
        ("addition-re-adds-overlay-id", spec,
         _replace(f"ID: {ADDITION_ID}", f"ID: {POLARIS_ID}030"), "R3:re-adds"),
        ("addition-scenario-dropped", spec,
         _replace("#### Scenario: Selftest two", "#### Scenery: Selftest two"),
         "R3"),
        ("addition-census-stale", CENSUS,
         _replace(f'"{ADDITION_ID}": {{', '"REQ-polaris-generation-098": {'),
         "R3"),
        ("addition-dangling-mention", f"{CHANGES}/{ADDITION}/proposal.md",
         _replace(f"Adds {ADDITION_ID}.", f"Adds {POLARIS_ID}097."), "R4"),
        # A candidate ID resolves inside an addition only, never on a route.
        *((("candidate-mention-on-route", "AGENTS.md",
            lambda t: t + f"\n{_candidate_id(ROOT)}\n", "R4"),)
          if _candidate_id(ROOT) else ()),
        ("addition-route-row", OPENSPEC_README,
         _replace(f"Signed: `{Path(ADDITION_RECORD).name}`", "Signed"), "R5"),
        ("addition-status-figure", STATUS, _status_figure_moved, "R5"),
        ("addition-union-stale", union,
         _replace("## primary\n\nVIS-2\n", "## primary\n\nVIS-3\n"),
         "R4:differs from its spec's warrants"),
    )


def selftest(witness_path=None):
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                            capture_output=True, text=True).stdout.strip()
    witnesses, failures = [], []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "base"
        scratch(ROOT, base)
        clean = run(base)
        if clean.failed:
            print("\n".join(clean.lines))
            print("SELFTEST FAIL: the unmutated scratch copy does not pass")
            return 1
        # The signed-addition hook: a synthetic addition, signed and
        # regenerated, must pass, and each of its mutants must fail.
        added = Path(tmp) / "with-signed-addition"
        shutil.copytree(base, added)
        _install_addition(added)
        with_addition = run(added)
        if with_addition.failed:
            print("\n".join(with_addition.lines))
            print("SELFTEST FAIL: the scratch copy with a signed addition "
                  "does not pass")
            return 1
        cases = ([(base, clean, m) for m in mutants(ROOT)]
                 + [(added, with_addition, m) for m in addition_mutants()])
        for start, clean, (name, rel, mutate, expect) in cases:
            tree = Path(tmp) / name
            shutil.copytree(start, tree)
            rels = rel if isinstance(rel, tuple) else (rel,)
            unchanged, applied = False, False
            for one in rels:
                target = tree / one
                before = target.read_text(encoding="utf-8")
                if mutate is None:
                    target.unlink()
                    old, new = "<file present>", "<file deleted>"
                    continue
                after = mutate(before)
                if after == before and "=0" in expect:
                    old, new = "<already applied>", "<already applied>"
                    continue
                applied = True
                if after == before:
                    unchanged = True
                    break
                target.write_text(after, encoding="utf-8")
                old, new = _fragment(before, after)
            if unchanged:
                failures.append(f"{name}: mutation changed nothing")
                continue
            rel = " + ".join(rels)
            got = run(tree)
            if ":" in expect:
                # The predicate must fail with this finding, not another.
                # `&` joins needles that must each be found (both methods).
                rid, _sep, needles = expect.partition(":")
                caught = all(any(n in f for f in got.findings.get(rid, []))
                             for n in needles.split("&"))
            elif expect.endswith("~"):
                rid = expect[:-1]
                caught = got.findings.get(rid) != clean.findings.get(rid)
            elif "=0" in expect:
                # Strict: the report-only predicate examined its population
                # and reports exactly zero findings. Nothing else fails, except
                # the predicates named after `|`, which must fail exactly when
                # the mutant applied new bytes (a later act over a signed
                # subject fails R2 by design until the reconciliation is
                # re-derived); once the tree already carries the bytes they
                # may only be a subset.
                head, _sep, tail = expect.partition("|")
                rid = head[:-2]
                allowed = set(filter(None, tail.split(",")))
                failed_ok = (got.failed == allowed if applied
                             else got.failed <= allowed)
                caught = (got.findings.get(rid) == [] and failed_ok
                          and any(int(m.group(1)) > 0 for m in (
                              re.match(rf"OK +{rid}  .* — (\d+) examined", line)
                              for line in got.lines) if m))
            else:
                caught = expect in got.failed
            witnesses.append({"mutant": name, "path": rel, "old": old,
                              "new": new, "expected": expect,
                              "failed": sorted(got.failed),
                              "outcome": "killed" if caught else "SURVIVED"})
            if not caught:
                failures.append(f"{name}: expected {expect} to fail, got "
                                f"{sorted(got.failed) or 'nothing'}")
        # Two cases a one-file mutation cannot express. A second record of the
        # same version fails R1 by its own finding; --regenerate refuses an
        # unsigned addition and writes nothing.
        for name, setup, expect in (
                ("addition-duplicate-version-record",
                 lambda tree: shutil.copyfile(
                     tree / ADDITION_RECORD,
                     tree / ADDITION_RECORD.replace("SELFTEST-ADDITION",
                                                    "SELFTEST-ADDITION-COPY")),
                 "R1:records sign version"),
                ("regenerate-refuses-unsigned",
                 lambda tree: (tree / ADDITION_RECORD).unlink(), "refused")):
            tree = Path(tmp) / name
            shutil.copytree(added, tree)
            setup(tree)
            if expect == "refused":
                before = {p: p.read_bytes() for p in tree.rglob("*") if p.is_file()}
                try:
                    regenerate(tree)
                    caught = False
                except SystemExit as exc:
                    caught = "census refused" in str(exc)
                after = {p: p.read_bytes() for p in tree.rglob("*") if p.is_file()}
                caught = caught and before == after
                got_failed = []
            else:
                got = run(tree)
                rid, _sep, needle = expect.partition(":")
                caught = any(needle in f for f in got.findings.get(rid, []))
                got_failed = sorted(got.failed)
            witnesses.append({"mutant": name, "path": "<scripted case>", "old": "",
                              "new": "", "expected": expect, "failed": got_failed,
                              "outcome": "killed" if caught else "SURVIVED"})
            if not caught:
                failures.append(f"{name}: expected {expect}")
    doc = {"commit": commit, "script": "scripts/check_spec_reconciliation.py",
           "mutants": witnesses}
    if witness_path:
        Path(witness_path).write_text(json.dumps(doc, indent=2,
                                                 ensure_ascii=False) + "\n",
                                      encoding="utf-8")
    for w in witnesses:
        print(f"{w['outcome']:8} {w['mutant']:28} {w['expected']} "
              f"(failed: {', '.join(w['failed'])})")
    if failures:
        print("\n".join(f"SELFTEST FAIL: {f}" for f in failures))
        return 1
    print(f"SELFTEST PASS: clean scratch copy and its signed-addition variant "
          f"pass; {len(witnesses)} of "
          f"{len(witnesses)} mutants killed by their expected predicate "
          f"(commit {commit[:12]})")
    return 0


def _fragment(before, after):
    """The smallest differing window, for re-runnable witnesses."""
    i = 0
    while i < min(len(before), len(after)) and before[i] == after[i]:
        i += 1
    j = 0
    while (j < min(len(before), len(after)) - i
           and before[-1 - j] == after[-1 - j]):
        j += 1
    lo = max(0, i - 30)
    return before[lo:len(before) - j][:160], after[lo:len(after) - j][:160]


def regenerate(root):
    """Write each signed addition's union and `census.json`; return paths.

    The one command a Polaris addition's recording commit runs after its
    builder installs the requirements. The base and understanding unions are
    signed subjects and are never written.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_polaris_dependency_unions as unions
    pop, findings = census(root)
    if findings:
        raise SystemExit("census refused:\n" + "\n".join(findings))
    written = unions.write_additions(root)
    body = census_json(pop)
    if read_text(root, CENSUS) != body:
        (root / CENSUS).write_text(body, encoding="utf-8")
        written.append(CENSUS)
    return written


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--census", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    mode.add_argument("--regenerate", action="store_true")
    parser.add_argument("--witnesses", help="selftest: write rule-6 JSON here")
    args = parser.parse_args(argv)
    if args.census:
        pop, findings = census(ROOT)
        if findings:
            print("\n".join(findings), file=sys.stderr)
            return 1
        sys.stdout.write(census_json(pop))
        return 0
    if args.selftest:
        return selftest(args.witnesses)
    if args.regenerate:
        for rel in regenerate(ROOT):
            print(f"wrote {rel}")
        return 0
    report = run(ROOT)
    print("\n".join(report.lines))
    ok = 7 - len(report.failed)
    print(f"{ok} of 7 predicates without FAIL; "
          f"{'FAIL' if report.failed else 'PASS'} — counts derived, not "
          "asserted")
    return 1 if report.failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
