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
  is equally a terminal record.
- R2 exact subject bytes: a digest act's successor column equals its
  manifest rows, and every signed subject on disk hashes to its row. A
  versioned sign-off's manifest rows equal the subjects on disk. A child's
  later successors compose in order: each one's act instant is strictly
  later than the act before it, each one's predecessor column names exactly
  the row the chain has reached for that subject, and its successor row then
  becomes the row the subject must hash to.
- R3 populations: CAP1-REQ, POC-REQ, PWB-REQ and the effective
  REQ-polaris-generation composition are each parsed by two independent
  methods (a regular-expression parser and a line state machine with no
  regular expressions; Polaris composes by ID line in one and by requirement
  name in the other). Both must agree, identifiers must be unique, and the
  result must equal the hard-coded literal census below and the committed
  `census.json`.
- R4 generated rows: each generated dependency file's source digest and
  requirement count match the spec; every full or continuation-form
  identifier mention in the five change directories and the default route
  pages resolves to the population; the CAP1 and PWB capability coverage
  tables carry the whole population.
- R5 default routes: `openspec/README.md` has one row per tracked change
  directory naming its terminal record; `PROJECT-STATUS.md` cites every
  terminal record and states the Polaris composition the census computes.
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
The R7 case `union-after-successor-act` does the same with the
`syzygy-c51h` successor package's proposed union. Before that act it
required R2, and only R2, to fail by design; the reconciliation was
re-derived on 2026-10-02 to name the act as the understanding child's
successor, so the case now requires every predicate to pass.

A later act over any subject fails R2 by design: the reconciliation is then
re-derived, never carried forward. The first re-derivation (2026-10-02)
added the dependency-union successor act to the understanding child.

Usage:
  python3 scripts/check_spec_reconciliation.py --check
  python3 scripts/check_spec_reconciliation.py --census > <record>/census.json
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
PIN_BEAD = "syzygy-jloi"
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
                 "PWB-READABILITY-SUCCESSOR-MANIFEST.txt"},
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

#: Hard-coded literal census (requirement suffix -> scenario count), taken at
#: main bd47409 on 2026-10-02 and cross-checked by the OpenSpec 1.9.0 CLI in
#: the record. Never derived from the parsers below.
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
        (1, 6, 1, 3, 5, 3, 5, 2, 5, 1, 1, 1, 1, 1, 1, 2, 5))),
    "POLARIS": None,  # totals only below; per-requirement counts in census.json
}
EXPECTED_TOTALS = {"CAP1": (42, 47), "POC": (24, 24), "PWB": (17, 44),
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
            want = (f"Package: {child['package']}",
                    f"Version: {child['version']}",
                    f"Tag: {child['package']}-v{child['version']}")
            missing = [w for w in want if w not in record.splitlines()]
            if missing:
                r1.append(f"{tag}: sign-off record lacks {missing}")
            marker = (f"<!-- versioned-signoff:{child['package']}:"
                      f"v{child['version']} -->")
            count = aggregate.count(marker)
            if count != 1:
                r1.append(f"{tag}: aggregate act record carries the sign-off "
                          f"block {count} times, expected 1")
        # Later successors compose in act order over the rows reached so far.
        reached = ACT_INSTANT.findall(record)
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
    report.add("R1", "terminal outcome for every child", records, r1,
               f"{len(CHILDREN)} children; digest acts: phrase = manifest "
               "sha256 and in the aggregate; versioned: package/version/tag "
               "and one aggregate block")
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


def compose_polaris_by_id(base, overlay):
    """Method A: compose base + overlay keyed by each block's ID line."""
    comp, problems = {}, []
    for label, text in (("base", base), ("overlay", overlay)):
        for kind, ids, name, scen in _polaris_blocks_regex(text):
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


def compose_polaris_by_name(base, overlay):
    """Method B: compose by normalized requirement name; IDs attached last."""
    comp, problems = {}, []

    def norm(name):
        return " ".join(name.split()).casefold()

    for label, text in (("base", base), ("overlay", overlay)):
        for block in _polaris_blocks_manual(text):
            key = norm(block["name"])
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
    if base is None or overlay is None:
        findings.append("POLARIS: base or overlay spec missing")
    else:
        a, pa = compose_polaris_by_id(base, overlay)
        b, pb = compose_polaris_by_name(base, overlay)
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


def check_census(root, report):
    pop, findings = census(root)
    examined = 0
    for family, (n_req, n_scen) in EXPECTED_TOTALS.items():
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
            want = {f"{POLARIS_ID}{i:03d}" for i in range(1, 32)}
            if set(reqs) != want:
                findings.append("POLARIS: identities are not exactly 001–031")
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
    files += list(ROUTE_PAGES)
    mentions = 0
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
                if num not in numbers.get(family, set()):
                    findings.append(f"`{rel}`: {family} identifier {num} "
                                    f"resolves to no requirement "
                                    f"(in `{m.group(0)[:48]}`)")
    report.add("R4", "generated dependency and coverage rows resolve",
               examined + mentions, findings,
               f"{examined} generated anchors, {mentions} identifier mentions "
               f"(full and continuation forms) over {len(files)} files")


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
        manifest = read_text(root, child["manifest"]) or ""
        paths |= {p for _d, p in ROW.findall(manifest)}
        paths |= set(tracked(root, f"{CHANGES}/{child['change']}"))
    paths |= set(tracked(root, CHANGES))
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


def _repin_package(root):
    """Map each pinned subject's current text to the re-pin package's bytes."""
    sys.path.insert(0, str(root / "scripts"))
    import build_pwb_behavior_contract_repin as repin
    by_text = {}
    for subject in repin.SUBJECTS:
        current = read_text(root, subject.path.as_posix())
        by_text[current] = repin.proposed_bytes(root, subject).decode("utf-8")

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
        ("pins-after-repin-acts", (REGISTRY, POLICY), _repin_package(root),
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
        ("union-extra-decision",
         f"{CHANGES}/{UNDERSTANDING_CHANGE}/GOVERNING-DEPENDENCIES.md",
         _replace("## decisions\n\nSDR-3\n", "## decisions\n\nSDR-3, SDR-99\n"),
         "R7~"),
        ("status-figure", STATUS,
         _replace("31 requirements and 182 scenarios",
                  "31 requirements and 177 scenarios"), "R5"),
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
        for name, rel, mutate, expect in mutants(ROOT):
            tree = Path(tmp) / name
            shutil.copytree(base, tree)
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
            if expect.endswith("~"):
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
    print(f"SELFTEST PASS: clean scratch copy passes; {len(witnesses)} of "
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


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--census", action="store_true")
    mode.add_argument("--selftest", action="store_true")
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
    report = run(ROOT)
    print("\n".join(report.lines))
    ok = 7 - len(report.failed)
    print(f"{ok} of 7 predicates without FAIL; "
          f"{'FAIL' if report.failed else 'PASS'} — counts derived, not "
          "asserted")
    return 1 if report.failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
