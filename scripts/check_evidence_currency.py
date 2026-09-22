#!/usr/bin/env python3
"""Read-only sha256 drift sweep over three evidence populations (N11 slice 1,
bead syzygy-u05.11): a) the reading-plan anchors named in
`apps/three-surface-poc/src/polaris-reading-plan.ts`; b) every
`docs/evidence/*.json` record that names a subject digest; c) the retained
mutation records, a subset of (b).

Digests are recomputed only from `git show <rev>:<path>` bytes (never the
working tree, never a live daemon, never a Butlers repository body) so a
report is valid only for the commit it names (AGENTS.md rule 7). This
includes *enumeration*: which `docs/evidence/*.json` files exist is itself
read from `git ls-tree -r --name-only -z <rev> -- docs/evidence`, never from
a working-tree `glob()` -- an uncommitted edit or an untracked extra file in
the working tree must never change a `--rev`-scoped report (see the
`rev_pinned_enumeration_ignores_working_tree` selftest check). Where a
population's subject is Butlers repository body content and is never stored
in the Syzygy git tree, this sweep reports Unknown/not-measured with a
stated reason instead of reading it (a hard prohibition, not a gap).

No "zero/all/100%" claim is made without a stated denominator (rule 2, rule
9); a record with no recognizable subject-digest key is Unknown, never
counted as passing or as zero drift (rule: no evidence -> Unknown).

Some subjects are pinned to a named historical commit by design (a review's
'reviewed_files_at_that_commit' snapshot, a proposal's 'baseline'/'governing'
digest list, a known append-only ledger such as DECISION-HISTORY.md or
ACCEPTANCE-ACT-RECORD.md): their digest is *expected* to drift from the
subject's current bytes as the subject keeps moving, and that drift is not
actionable the way a claimed-current digest's drift is. This sweep marks
such leaves 'historical' (see HISTORICAL_MARKER_KEY_FRAGMENTS and
HISTORICAL_LEDGER_BASENAMES) and reports the historical/actionable split
inside every drift count -- it never folds the two together and never hides
either class (see classify_record).

Usage:
  python3 scripts/check_evidence_currency.py               # human report
  python3 scripts/check_evidence_currency.py --json         # JSON report
  python3 scripts/check_evidence_currency.py --out FILE.json --json
  python3 scripts/check_evidence_currency.py --rev <sha>     # pin a commit
  python3 scripts/check_evidence_currency.py --selftest      # rule-6 fixtures

Exit status: 0 = report produced (drift found or not -- drift is data, not
failure; this is an instrument, not a gate). --selftest: 0 = every fixture
predicate behaved as asserted, 1 = a fixture failed or raised (each
selftest check runs independently: one raising predicate is caught, counted
as a failure, and does not prevent the remaining checks from running). 2 =
usage error.

Standard library only. Read-only: makes no writes, no network, no Butlers
reads. Python 3.9+.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
READING_PLAN_FILE = "apps/three-surface-poc/src/polaris-reading-plan.ts"
EVIDENCE_DIR_REL_DEFAULT = "docs/evidence"

# Sibling keys tried, in priority order, to resolve a digest leaf's subject path.
SUBJECT_SIBLING_KEYS = (
    "path", "sourcePath", "file", "subject", "testFile", "packet",
    "originalPath", "retainedPath",
)

DIGEST_KEY_RE = re.compile(r"(sha[_-]?256|digest)", re.IGNORECASE)
HEX64_RE = re.compile(r"^[0-9a-fA-F]{64}$")
PATH_LIKE_RE = re.compile(r"^[A-Za-z0-9._/-]+\.[A-Za-z0-9]{1,6}$|^[A-Za-z0-9._/-]*/[A-Za-z0-9._/-]+$")

# Dict keys (underscore/hyphen/case insensitive) whose subtree is a
# historical, pinned-at-a-named-commit snapshot by design -- drift under one
# of these is expected, not actionable. Real corpus examples: a review's
# 'reviewed_files_at_that_commit' map, a proposal's 'baseline'/'governing'
# digest list, an 'asOf'/'capturedAt'/'atCommit'/'snapshotCommit' anchor.
HISTORICAL_MARKER_KEY_FRAGMENTS = (
    "reviewedfilesatthatcommit", "baseline", "governing", "atthiscommit",
    "presentatthiscommit", "reviewedcommit", "asof", "atcommit",
    "capturedat", "snapshotcommit", "describescommit",
)

# Subject basenames that are known append-only ledgers: appending to them is
# expected, ordinary operation, so a stored digest of one is a historical
# snapshot regardless of which key it sits under.
HISTORICAL_LEDGER_BASENAMES = {
    "DECISION-HISTORY.md",
    "ACCEPTANCE-ACT-RECORD.md",
}


# --------------------------------------------------------------------------
# git-tree byte access (never the working tree, never a live daemon)
# --------------------------------------------------------------------------

def make_git_reader(rev: str, repo_root: Path = REPO_ROOT) -> Tuple[Callable[[str], Optional[bytes]], Dict[str, Optional[bytes]]]:
    """Returns a (read_bytes, cache) pair. read_bytes(path) returns the exact
    bytes of `path` as recorded at `rev`, or None if `path` does not resolve
    to a blob at that commit. Cached because a handful of subject paths are
    referenced by many digest leaves. `repo_root` defaults to this repo but
    is overridable so selftest fixtures can point at a disposable temp repo."""
    cache: Dict[str, Optional[bytes]] = {}

    def read_bytes(path: str) -> Optional[bytes]:
        if path in cache:
            return cache[path]
        result = subprocess.run(
            ["git", "show", f"{rev}:{path}"],
            cwd=repo_root, capture_output=True, check=False,
        )
        value = result.stdout if result.returncode == 0 else None
        cache[path] = value
        return value

    return read_bytes, cache


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def resolve_rev(rev: str, repo_root: Path = REPO_ROOT) -> str:
    result = subprocess.run(
        ["git", "rev-parse", rev], cwd=repo_root, capture_output=True,
        text=True, check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"usage error: cannot resolve rev {rev!r}: {result.stderr.strip()}")
    return result.stdout.strip()


def list_top_level_json_at_rev(rev: str, dir_rel: str, repo_root: Path = REPO_ROOT) -> List[str]:
    """Enumerates the *.json files directly inside `dir_rel` (one path
    segment deep, matching the old glob("*.json")'s non-recursive scope) as
    recorded at `rev` -- never the working tree. Uses `git ls-tree -r
    --name-only -z` (AGENTS.md: "git ls-tree needs -z, or quoted paths break
    the parser") so a path with a space or a quote character is handled
    correctly; -r is required to include files nested under a directory
    tracked as a subtree entry rather than expanded at this level, but the
    one-segment-deep filter below still excludes any entry further nested
    (e.g. docs/evidence/launch-gate-v2.5/*.json), matching the prior glob's
    scope exactly."""
    prefix = dir_rel.rstrip("/") + "/"
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "-z", rev, "--", dir_rel],
        cwd=repo_root, capture_output=True, check=False,
    )
    if result.returncode != 0:
        return []
    names = [entry for entry in result.stdout.decode("utf-8").split("\0") if entry]
    top_level_json = []
    for name in names:
        if not name.startswith(prefix):
            continue
        remainder = name[len(prefix):]
        if remainder.endswith(".json") and "/" not in remainder:
            top_level_json.append(name)
    return sorted(top_level_json)


# --------------------------------------------------------------------------
# Population (a): reading-plan anchors
# --------------------------------------------------------------------------

PLAN_RE = re.compile(
    r'export const (\w+)\s*=\s*\{[^}]*?"statementSha256"\s*:\s*"([0-9a-f]{64})"',
    re.DOTALL,
)

# Which project-account key each named plan feeds (see
# apps/three-surface-poc/src/polaris-reading.ts:projectReading), and why its
# subject text is never present in the Syzygy git tree: PROJECT_ACCOUNT_KEYS
# in packages/three-surface-poc-core/src/project-shape-extraction.ts marks
# both 'v1-scope' and 'architecture' as Butlers-sourced, fetched live through
# the daemon's observation pipeline for exactly this render, never stored.
PLAN_ACCOUNT_KEY = {
    "V1_READING_PLAN": "v1-scope",
    "ARCHITECTURE_READING_PLAN": "architecture",
}


def extract_reading_plan_anchors(source_text: str) -> List[Dict[str, str]]:
    """Pure: parses the TS source for every `export const NAME = { "statementSha256": "<hex>" ...`
    block. Returns one entry per plan found, in file order."""
    anchors = []
    for match in PLAN_RE.finditer(source_text):
        name, digest = match.group(1), match.group(2)
        anchors.append({"name": name, "statementSha256": digest})
    return anchors


def classify_reading_plan_anchor(name: str) -> Dict[str, str]:
    """Pure, and — by design — independent of any digest value or byte
    content: the subject of every currently-defined reading plan is a
    Butlers-sourced project-account key (see PLAN_ACCOUNT_KEY), which this
    sweep is prohibited from reading (AGENTS.md hard prohibition: 'Never read
    a repository body without per-repository consent...'; the task
    explicitly directs Unknown/not-measured with a stated reason here rather
    than a daemon read). No sha256 recomputation is attempted."""
    account_key = PLAN_ACCOUNT_KEY.get(name, "unknown")
    return {
        "name": name,
        "status": "not-measured",
        "reason": (
            f"subject is Butlers repository body content (project-account key "
            f"'{account_key}'), fetched live via the daemon observation "
            f"pipeline and never stored in the Syzygy git tree; this sweep "
            f"never reads Butlers repository bodies"
        ),
    }


def sweep_reading_plans(rev: str, repo_root: Path = REPO_ROOT) -> Dict[str, object]:
    read_bytes, _ = make_git_reader(rev, repo_root)
    raw = read_bytes(READING_PLAN_FILE)
    if raw is None:
        return {
            "file": READING_PLAN_FILE, "rev": rev, "found": 0, "anchors": [],
            "note": f"{READING_PLAN_FILE} does not resolve to a blob at {rev}",
        }
    text = raw.decode("utf-8")
    anchors = extract_reading_plan_anchors(text)
    results = []
    for anchor in anchors:
        classification = classify_reading_plan_anchor(anchor["name"])
        results.append({**anchor, **classification})
    return {"file": READING_PLAN_FILE, "rev": rev, "found": len(results), "anchors": results}


# --------------------------------------------------------------------------
# Population (b): docs/evidence/*.json subject-digest records
# --------------------------------------------------------------------------

def _looks_path_like(value: object) -> bool:
    if not isinstance(value, str) or " " in value or value == "":
        return False
    return bool(PATH_LIKE_RE.match(value))


def _is_historical_marker_key(key: str) -> bool:
    normalized = key.replace("_", "").replace("-", "").lower()
    return any(fragment in normalized for fragment in HISTORICAL_MARKER_KEY_FRAGMENTS)


def _is_historical_ledger_subject(subject: Optional[str]) -> bool:
    if not subject:
        return False
    return subject.rsplit("/", 1)[-1] in HISTORICAL_LEDGER_BASENAMES


def _classify_historical(via_marker_key: bool, subject: Optional[str]) -> Tuple[bool, Optional[str]]:
    """Pure. Decides whether a leaf is historical-by-design and why, so the
    reason is always inspectable rather than a bare bool (item 3: 'don't
    hide either class')."""
    ledger = _is_historical_ledger_subject(subject)
    if via_marker_key and ledger:
        return True, "nested under a historical-marker key and subject is a known append-only ledger"
    if via_marker_key:
        return True, "nested under a historical-marker key (e.g. reviewed_files_at_that_commit, baseline, governing)"
    if ledger:
        return True, "subject is a known append-only ledger (DECISION-HISTORY.md/ACCEPTANCE-ACT-RECORD.md class)"
    return False, None


def find_digest_leaves(node: object, parent_key: Optional[str] = None, historical: bool = False) -> List[Dict[str, object]]:
    """Pure recursive walk. Returns a list of leaf descriptors:
    {'digest': hex, 'digestKey': key, 'subject': path-or-None, 'via': how-resolved,
    'historical': bool, 'historicalReason': str-or-None}
    covering both single digest+sibling-path leaves and flat digest maps
    (a digest-ish key whose value is itself an all-path->hex64 dict).

    'historical' is True when the leaf sits under a key matching
    HISTORICAL_MARKER_KEY_FRAGMENTS (inherited by every descendant once set,
    since a 'reviewed_files_at_that_commit' map is historical all the way
    down) or when its resolved subject is a known append-only ledger
    (HISTORICAL_LEDGER_BASENAMES) -- see classify_record for how this
    changes drift reporting, never leaf discovery itself."""
    leaves: List[Dict[str, object]] = []
    if isinstance(node, dict):
        # First: flat digest maps directly under this dict (checked before
        # descending, since we do not want to also re-walk its hex values).
        for key, value in node.items():
            if DIGEST_KEY_RE.search(key) and isinstance(value, dict) and value:
                if all(_looks_path_like(k) and isinstance(v, str) and HEX64_RE.match(v) for k, v in value.items()):
                    via_marker_key = historical or _is_historical_marker_key(key)
                    for subject, digest in value.items():
                        is_hist, hist_reason = _classify_historical(via_marker_key, subject)
                        leaves.append({"digest": digest.lower(), "digestKey": key, "subject": subject, "via": "flat-map",
                                       "historical": is_hist, "historicalReason": hist_reason})
                    continue  # do not also treat this dict's entries as ordinary sub-nodes' digest leaves
        # Second: single digest-ish keys at this level, resolved via sibling or parent-key.
        for key, value in node.items():
            if DIGEST_KEY_RE.search(key) and isinstance(value, str) and HEX64_RE.match(value):
                subject = None
                via = "unresolved"
                for sibling in SUBJECT_SIBLING_KEYS:
                    candidate = node.get(sibling)
                    if _looks_path_like(candidate):
                        subject = candidate
                        via = f"sibling:{sibling}"
                        break
                if subject is None and _looks_path_like(parent_key):
                    subject = parent_key
                    via = "parent-key"
                via_marker_key = historical or _is_historical_marker_key(key)
                is_hist, hist_reason = _classify_historical(via_marker_key, subject)
                leaves.append({"digest": value.lower(), "digestKey": key, "subject": subject, "via": via,
                               "historical": is_hist, "historicalReason": hist_reason})
        # Recurse into every child (dicts and lists), passing this node's own
        # key (in ITS parent) down is not needed here; parent-key applies at
        # the immediate child level, so pass each key as parent_key downward.
        # 'historical' is inherited (once true under a marker key, every
        # descendant leaf stays historical) and re-checked at each level so a
        # marker key nested deeper still turns it on.
        for key, value in node.items():
            if isinstance(value, (dict, list)):
                child_historical = historical or _is_historical_marker_key(key)
                leaves.extend(find_digest_leaves(value, parent_key=key, historical=child_historical))
    elif isinstance(node, list):
        for item in node:
            leaves.extend(find_digest_leaves(item, parent_key=None, historical=historical))
    return leaves


def classify_record(leaves: List[Dict[str, object]], read_bytes: Callable[[str], Optional[bytes]]) -> Dict[str, object]:
    """Pure given a leaf list and a byte reader. Classifies one evidence
    record. Never claims zero/all without counting; every count below is a
    denominator-bearing field in the returned dict.

    'status' keeps its original three values (current/drift/unknown) for
    backward compatibility; 'driftClass' (present, possibly None, on every
    return) splits a 'drift' status into 'actionable', 'historical-by-design'
    or 'mixed' without ever collapsing status itself to hide a drift --
    a record with only historical-by-design drift still reports status
    'drift', never silently promoted to 'current'."""
    if not leaves:
        return {"status": "unknown", "driftClass": None, "reason": "no-subject-digest-key", "leafCount": 0,
                "resolvedCount": 0, "inTreeCount": 0, "matchCount": 0, "driftCount": 0,
                "driftHistoricalCount": 0, "driftActionableCount": 0}
    resolved = [leaf for leaf in leaves if leaf["subject"] is not None]
    in_tree = []
    match = []
    drift = []
    for leaf in resolved:
        current = read_bytes(leaf["subject"])
        if current is None:
            continue
        in_tree.append(leaf)
        if sha256_hex(current) == leaf["digest"]:
            match.append(leaf)
        else:
            drift.append(leaf)
    drift_historical = [leaf for leaf in drift if leaf.get("historical")]
    drift_actionable = [leaf for leaf in drift if not leaf.get("historical")]
    summary = {
        "leafCount": len(leaves), "resolvedCount": len(resolved),
        "inTreeCount": len(in_tree), "matchCount": len(match), "driftCount": len(drift),
        "driftHistoricalCount": len(drift_historical), "driftActionableCount": len(drift_actionable),
    }
    if drift:
        if drift_actionable and drift_historical:
            drift_class = "mixed"
        elif drift_historical:
            drift_class = "historical-by-design"
        else:
            drift_class = "actionable"
        reason = (f"{len(drift)}/{len(in_tree)} in-tree subject digest(s) mismatch current bytes "
                  f"({len(drift_historical)} historical-by-design, {len(drift_actionable)} actionable)")
        return {"status": "drift", "driftClass": drift_class, "reason": reason, **summary}
    if in_tree:
        return {"status": "current", "driftClass": None,
                "reason": f"{len(match)}/{len(in_tree)} in-tree subject digest(s) match current bytes", **summary}
    return {"status": "unknown", "driftClass": None,
            "reason": "digest key(s) present but no subject resolved to an in-tree path", **summary}


def sweep_evidence_records(rev: str, evidence_dir_rel: str, repo_root: Path = REPO_ROOT) -> Dict[str, object]:
    """Enumerates and reads docs/evidence/*.json entirely through `rev` (via
    list_top_level_json_at_rev + the rev-pinned read_bytes) -- never
    Path.glob or path.read_text against the working tree (rule 7; this was
    the item-1 bug the independent review of the first cut caught)."""
    read_bytes, _ = make_git_reader(rev, repo_root)
    files = list_top_level_json_at_rev(rev, evidence_dir_rel, repo_root)
    per_file = []
    for rel in files:
        raw = read_bytes(rel)
        if raw is None:
            per_file.append({"file": rel, "status": "unknown", "driftClass": None,
                              "reason": f"{rel} does not resolve to a blob at {rev} (enumerated by git ls-tree but unreadable via git show)",
                              "leafCount": 0, "resolvedCount": 0, "inTreeCount": 0, "matchCount": 0, "driftCount": 0,
                              "driftHistoricalCount": 0, "driftActionableCount": 0})
            continue
        try:
            data = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            per_file.append({"file": rel, "status": "unknown", "driftClass": None, "reason": f"unparseable JSON: {error}",
                              "leafCount": 0, "resolvedCount": 0, "inTreeCount": 0, "matchCount": 0, "driftCount": 0,
                              "driftHistoricalCount": 0, "driftActionableCount": 0})
            continue
        leaves = find_digest_leaves(data)
        classification = classify_record(leaves, read_bytes)
        per_file.append({"file": rel, **classification})
    denominator = len(per_file)
    counts = {"current": 0, "drift": 0, "unknown": 0}
    for entry in per_file:
        counts[entry["status"]] += 1
    drift_records = [e for e in per_file if e["status"] == "drift"]
    drift_records_historical_only = sum(1 for e in drift_records if e["driftClass"] == "historical-by-design")
    drift_records_with_actionable = sum(1 for e in drift_records if e["driftClass"] in ("actionable", "mixed"))
    return {
        "denominator": denominator,
        "carriesDigestKey": sum(1 for e in per_file if e["leafCount"] > 0),
        "current": counts["current"], "drift": counts["drift"], "unknown": counts["unknown"],
        "driftRecordsHistoricalOnly": drift_records_historical_only,
        "driftRecordsWithActionableDrift": drift_records_with_actionable,
        "records": per_file,
    }


# --------------------------------------------------------------------------
# Population (c): retained mutation records (a subset of (b))
# --------------------------------------------------------------------------

def is_mutation_record(filename: str, data: object) -> bool:
    """Pure. A record is a retained mutation record if its filename names a
    mutation run, or its top-level shape carries a mutants/mutations list, or
    a single-mutant old/new/restored shape."""
    if "mutation" in filename.lower():
        return True
    if isinstance(data, dict):
        for key in ("mutations", "mutants"):
            value = data.get(key)
            if isinstance(value, list) and len(value) > 0:
                return True
        if {"old", "new", "restored"}.issubset(data.keys()):
            return True
    return False


def _mutant_dicts(data: object) -> List[Dict[str, object]]:
    """Pure. Returns every dict in this record that carries old/new mutant
    fragment text: the top-level record itself if shaped that way, and every
    item of a mutations/mutants list that is itself so shaped."""
    found = []
    if isinstance(data, dict):
        if "old" in data and "new" in data:
            found.append(data)
        for key in ("mutations", "mutants"):
            value = data.get(key)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and "old" in item and "new" in item:
                        found.append(item)
    return found


def _mutant_subject(mutant: Dict[str, object], record: Dict[str, object]) -> Optional[str]:
    for key in SUBJECT_SIBLING_KEYS:
        candidate = mutant.get(key)
        if _looks_path_like(candidate):
            return candidate
    if isinstance(record, dict):
        for key in SUBJECT_SIBLING_KEYS:
            candidate = record.get(key)
            if _looks_path_like(candidate):
                return candidate
    return None


def classify_mutant_fragment(old_fragment: object, subject_bytes: Optional[bytes]) -> str:
    """Pure. Auxiliary rule-6-style signal distinct from whole-file digest
    match/drift: does the recorded 'old' fragment still appear verbatim in
    the current subject bytes?"""
    if subject_bytes is None:
        return "subject-unresolved"
    if not isinstance(old_fragment, str):
        return "subject-unresolved"
    try:
        text = subject_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return "subject-unresolved"
    return "still-present" if old_fragment in text else "moved-on"


def sweep_mutation_records(rev: str, evidence_dir_rel: str, repo_root: Path = REPO_ROOT) -> Dict[str, object]:
    """Same rev-pinned enumeration/reading discipline as sweep_evidence_records
    (rule 7; item-1 fix applies here identically)."""
    read_bytes, _ = make_git_reader(rev, repo_root)
    files = list_top_level_json_at_rev(rev, evidence_dir_rel, repo_root)
    per_file = []
    for rel in files:
        raw = read_bytes(rel)
        if raw is None:
            continue
        try:
            data = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        filename = rel.rsplit("/", 1)[-1]
        if not is_mutation_record(filename, data):
            continue
        leaves = find_digest_leaves(data)
        digest_classification = classify_record(leaves, read_bytes)
        mutants = _mutant_dicts(data)
        fragment_results = {"still-present": 0, "moved-on": 0, "subject-unresolved": 0}
        for mutant in mutants:
            subject = _mutant_subject(mutant, data if isinstance(data, dict) else {})
            subject_bytes = read_bytes(subject) if subject else None
            fragment_results[classify_mutant_fragment(mutant.get("old"), subject_bytes)] += 1
        per_file.append({
            "file": rel, "digest": digest_classification,
            "mutantFragmentDenominator": len(mutants), "mutantFragments": fragment_results,
        })
    return {"denominator": len(per_file), "records": per_file}


# --------------------------------------------------------------------------
# Report assembly
# --------------------------------------------------------------------------

def build_report(rev_arg: str, evidence_dir_rel: str, repo_root: Path = REPO_ROOT) -> Dict[str, object]:
    resolved_rev = resolve_rev(rev_arg, repo_root)
    return {
        "instrument": "scripts/check_evidence_currency.py",
        "measuredOn": {"rev": rev_arg, "resolvedCommit": resolved_rev},
        "populationA_readingPlanAnchors": sweep_reading_plans(resolved_rev, repo_root),
        "populationB_evidenceRecords": sweep_evidence_records(resolved_rev, evidence_dir_rel, repo_root),
        "populationC_mutationRecords": sweep_mutation_records(resolved_rev, evidence_dir_rel, repo_root),
    }


def render_human(report: Dict[str, object]) -> str:
    lines = []
    lines.append(f"check_evidence_currency: rev={report['measuredOn']['rev']} -> {report['measuredOn']['resolvedCommit']}")
    a = report["populationA_readingPlanAnchors"]
    lines.append(f"\nPopulation (a) reading-plan anchors in {a['file']}: {a['found']} found")
    for anchor in a["anchors"]:
        lines.append(f"  - {anchor['name']}: {anchor['status']} ({anchor['reason']})")
    b = report["populationB_evidenceRecords"]
    lines.append(f"\nPopulation (b) docs/evidence/*.json records (enumerated at rev via git ls-tree, never the working tree): "
                 f"{b['denominator']} total, {b['carriesDigestKey']} carry >=1 recognizable subject-digest key")
    lines.append(f"  current={b['current']}  drift={b['drift']}  unknown={b['unknown']}  (of {b['denominator']})")
    if b["drift"]:
        lines.append(f"  of {b['drift']} drifted records: {b['driftRecordsHistoricalOnly']} historical-by-design only "
                     f"(e.g. 'reviewed_files_at_that_commit' snapshots, baseline/governing lists, append-only ledgers), "
                     f"{b['driftRecordsWithActionableDrift']} carry >=1 actionable drifted subject")
        lines.append("  drifted records:")
        for entry in b["records"]:
            if entry["status"] == "drift":
                lines.append(f"    - {entry['file']} [{entry['driftClass']}]: {entry['reason']}")
    c = report["populationC_mutationRecords"]
    lines.append(f"\nPopulation (c) retained mutation records: {c['denominator']} total")
    for entry in c["records"]:
        d = entry["digest"]
        drift_class_suffix = f"[{d['driftClass']}]" if d.get("driftClass") else ""
        lines.append(f"  - {entry['file']}: digest={d['status']}{drift_class_suffix} ({d.get('reason', '')}); "
                     f"mutant fragments {entry['mutantFragments']} (of {entry['mutantFragmentDenominator']})")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# --selftest (AGENTS.md rule 6: mutate the input and confirm the check fails)
# --------------------------------------------------------------------------

def _assert(condition: bool, message: str, failures: List[str]) -> None:
    if not condition:
        failures.append(message)


def _check_reading_plan_extraction(failures: List[str]) -> None:
    fixture_ts = (
        'export const ARCHITECTURE_READING_PLAN = {\n'
        '  "statementSha256": "' + ("a" * 64) + '",\n'
        '  "passages": [{"start": 0, "end": 1}]\n'
        '} as const;\n\n'
        'export const V1_READING_PLAN = {\n'
        '  "statementSha256": "' + ("b" * 64) + '",\n'
        '  "passages": []\n'
        '} as const;\n'
    )
    anchors = extract_reading_plan_anchors(fixture_ts)
    _assert(anchors == [
        {"name": "ARCHITECTURE_READING_PLAN", "statementSha256": "a" * 64},
        {"name": "V1_READING_PLAN", "statementSha256": "b" * 64},
    ], "extract_reading_plan_anchors: expected both fixture plans in file order", failures)
    # Mutate: corrupt the digest value; confirm the parser reflects exactly the corrupted bytes
    # (rule 6: mutate the input and confirm the affected predicate changes).
    mutated_ts = fixture_ts.replace("a" * 64, "c" * 64)
    mutated_anchors = extract_reading_plan_anchors(mutated_ts)
    _assert(mutated_anchors[0]["statementSha256"] == "c" * 64,
            "extract_reading_plan_anchors: mutating the source digest did not change the extracted digest", failures)
    # Mutate: remove a plan entirely; confirm it is no longer found (denominator predicate).
    removed_ts = fixture_ts.split("export const V1_READING_PLAN")[0]
    _assert(len(extract_reading_plan_anchors(removed_ts)) == 1,
            "extract_reading_plan_anchors: removing a plan block did not reduce the anchor count", failures)


def _check_reading_plan_classification(failures: List[str]) -> None:
    # By design this predicate never depends on digest content (the subject is never read),
    # so its mutation test is a stability check across distinct inputs, not a match/drift flip.
    c1 = classify_reading_plan_anchor("V1_READING_PLAN")
    c2 = classify_reading_plan_anchor("ARCHITECTURE_READING_PLAN")
    _assert(c1["status"] == "not-measured" and c2["status"] == "not-measured",
            "classify_reading_plan_anchor: both known plans must classify not-measured", failures)
    _assert("Butlers" in c1["reason"] and "v1-scope" in c1["reason"],
            "classify_reading_plan_anchor: V1_READING_PLAN reason must name its Butlers account key", failures)
    _assert("architecture" in c2["reason"],
            "classify_reading_plan_anchor: ARCHITECTURE_READING_PLAN reason must name its Butlers account key", failures)
    c3 = classify_reading_plan_anchor("SOME_FUTURE_PLAN")
    _assert(c3["status"] == "not-measured",
            "classify_reading_plan_anchor: an unrecognized plan name must still classify not-measured, never green", failures)


def _check_digest_leaf_sibling(failures: List[str]) -> None:
    record_sibling = {"kind": "x", "path": "packages/foo/bar.ts", "sha256": "d" * 64}
    leaves = find_digest_leaves(record_sibling)
    _assert(len(leaves) == 1 and leaves[0]["subject"] == "packages/foo/bar.ts" and leaves[0]["via"] == "sibling:path",
            "find_digest_leaves: did not resolve a digest via its 'path' sibling", failures)
    # Mutate: remove the sibling; confirm resolution now fails (via becomes unresolved).
    record_no_sibling = {"kind": "x", "sha256": "d" * 64}
    leaves_no_sibling = find_digest_leaves(record_no_sibling)
    _assert(leaves_no_sibling[0]["subject"] is None,
            "find_digest_leaves: removing the sibling path must leave the leaf unresolved", failures)


def _check_digest_leaf_parent_key(failures: List[str]) -> None:
    record_parent_key = {"packages/foo/baz.ts": {"sha256": "e" * 64, "bytes": 12}}
    leaves_pk = find_digest_leaves(record_parent_key)
    _assert(len(leaves_pk) == 1 and leaves_pk[0]["subject"] == "packages/foo/baz.ts" and leaves_pk[0]["via"] == "parent-key",
            "find_digest_leaves: did not resolve a digest via its own dict key as the parent-key path", failures)
    # Mutate: replace the path-shaped key with a non-path-like key; confirm resolution now fails.
    record_bad_parent_key = {"not a path": {"sha256": "e" * 64, "bytes": 12}}
    leaves_bad_pk = find_digest_leaves(record_bad_parent_key)
    _assert(leaves_bad_pk[0]["subject"] is None,
            "find_digest_leaves: a non-path-like parent key must not resolve", failures)


def _check_digest_leaf_flat_map(failures: List[str]) -> None:
    record_flat = {"sourceDigestsBefore": {"packages/a.ts": "f" * 64, "packages/b.ts": "1" * 64}}
    leaves_flat = find_digest_leaves(record_flat)
    _assert(len(leaves_flat) == 2 and {leaf["subject"] for leaf in leaves_flat} == {"packages/a.ts", "packages/b.ts"},
            "find_digest_leaves: did not resolve both entries of a flat digest map", failures)
    # Mutate: make one value non-hex64; confirm the map is no longer recognized as a flat digest map
    # (falls through to zero leaves, since 'sourceDigestsBefore' itself is not a bare hex64 string).
    record_flat_broken = {"sourceDigestsBefore": {"packages/a.ts": "f" * 64, "packages/b.ts": "not-a-digest"}}
    leaves_flat_broken = find_digest_leaves(record_flat_broken)
    _assert(len(leaves_flat_broken) == 0,
            "find_digest_leaves: one non-hex64 entry must disqualify the whole map from flat-map recognition", failures)


def _check_classify_record(failures: List[str]) -> None:
    fixture_bytes = {"packages/foo/bar.ts": b"hello world"}
    correct_digest = sha256_hex(b"hello world")

    def fake_reader(path: str) -> Optional[bytes]:
        return fixture_bytes.get(path)

    match_leaves = [{"digest": correct_digest, "digestKey": "sha256", "subject": "packages/foo/bar.ts", "via": "sibling:path", "historical": False, "historicalReason": None}]
    result = classify_record(match_leaves, fake_reader)
    _assert(result["status"] == "current", "classify_record: matching bytes must classify current", failures)
    # Mutate: flip one byte of the recorded digest; confirm the predicate now reports drift.
    drift_leaves = [{"digest": "0" * 64, "digestKey": "sha256", "subject": "packages/foo/bar.ts", "via": "sibling:path", "historical": False, "historicalReason": None}]
    result_drift = classify_record(drift_leaves, fake_reader)
    _assert(result_drift["status"] == "drift", "classify_record: mismatched bytes must classify drift, not current", failures)
    # Mutate: the subject no longer resolves in the tree; confirm unknown/unresolved, never current.
    missing_leaves = [{"digest": correct_digest, "digestKey": "sha256", "subject": "packages/gone.ts", "via": "sibling:path", "historical": False, "historicalReason": None}]
    result_missing = classify_record(missing_leaves, fake_reader)
    _assert(result_missing["status"] == "unknown", "classify_record: a subject absent from the tree must classify unknown, never current", failures)
    # Mutate: zero digest leaves at all; confirm no-subject-digest-key reason.
    result_none = classify_record([], fake_reader)
    _assert(result_none["status"] == "unknown" and result_none["reason"] == "no-subject-digest-key",
            "classify_record: zero digest leaves must classify unknown/no-subject-digest-key", failures)


def _check_is_mutation_record(failures: List[str]) -> None:
    _assert(is_mutation_record("foo-mutation-run-2026-09-01.json", {}) is True,
            "is_mutation_record: a 'mutation' filename must be included", failures)
    _assert(is_mutation_record("foo.json", {"mutations": [{"old": "a", "new": "b"}]}) is True,
            "is_mutation_record: a non-empty mutations list must be included", failures)
    _assert(is_mutation_record("foo.json", {"old": "a", "new": "b", "restored": True}) is True,
            "is_mutation_record: an old/new/restored shape must be included", failures)
    not_mutation = {"kind": "unrelated", "sha256": "a" * 64}
    _assert(is_mutation_record("foo.json", not_mutation) is False,
            "is_mutation_record: an unrelated record must be excluded", failures)
    # Mutate: add a mutants list to the same record; confirm it now flips to included.
    mutated_into_population = dict(not_mutation, mutants=[{"old": "a", "new": "b"}])
    _assert(is_mutation_record("foo.json", mutated_into_population) is True,
            "is_mutation_record: adding a mutants list must flip the record into the population", failures)


def _check_classify_mutant_fragment(failures: List[str]) -> None:
    _assert(classify_mutant_fragment("hello", b"hello world") == "still-present",
            "classify_mutant_fragment: an intact fragment must classify still-present", failures)
    # Mutate: change the subject bytes so the fragment is gone; confirm it flips to moved-on.
    _assert(classify_mutant_fragment("hello", b"goodbye world") == "moved-on",
            "classify_mutant_fragment: a fragment no longer present must classify moved-on, not still-present", failures)
    _assert(classify_mutant_fragment("hello", None) == "subject-unresolved",
            "classify_mutant_fragment: an unresolved subject must classify subject-unresolved", failures)


def _check_historical_classification(failures: List[str]) -> None:
    """item 3: a leaf nested under a historical-marker key (e.g. the real
    corpus key 'reviewed_files_at_that_commit') or naming a known
    append-only ledger subject must be marked historical, and classify_record
    must split drift into historical/actionable counts without ever hiding
    either or silently promoting all-historical drift to 'current'."""
    historical_record = {
        "review1": {
            "reviewed_files_at_that_commit": {
                "docs/design/SOME-FUNNEL.md": {"bytes": 123, "sha256": "a" * 64},
            }
        }
    }
    leaves = find_digest_leaves(historical_record)
    _assert(len(leaves) == 1 and leaves[0]["subject"] == "docs/design/SOME-FUNNEL.md" and leaves[0]["historical"] is True,
            "find_digest_leaves: a leaf nested under 'reviewed_files_at_that_commit' must be marked historical", failures)
    # Mutate: rename the marker key to something with no historical meaning; the same leaf,
    # resolved the same way, must now classify as NOT historical (proves the marker key, not
    # some other property of the shape, is doing the work).
    renamed_record = {
        "review1": {
            "unrelated_files_list": {
                "docs/design/SOME-FUNNEL.md": {"bytes": 123, "sha256": "a" * 64},
            }
        }
    }
    renamed_leaves = find_digest_leaves(renamed_record)
    _assert(len(renamed_leaves) == 1 and renamed_leaves[0]["historical"] is False,
            "find_digest_leaves: renaming away the historical-marker key must drop the historical flag", failures)

    # A known append-only ledger subject is historical regardless of the key path it sits under.
    ledger_record = {"kind": "x", "path": ".syzygy/governance/decisions/DECISION-HISTORY.md", "sha256": "b" * 64}
    ledger_leaves = find_digest_leaves(ledger_record)
    _assert(len(ledger_leaves) == 1 and ledger_leaves[0]["historical"] is True,
            "find_digest_leaves: a DECISION-HISTORY.md subject must be marked historical by basename alone", failures)
    # Mutate: point the same shape at an unrelated file; historical must flip off.
    non_ledger_record = {"kind": "x", "path": "packages/foo/bar.ts", "sha256": "b" * 64}
    non_ledger_leaves = find_digest_leaves(non_ledger_record)
    _assert(len(non_ledger_leaves) == 1 and non_ledger_leaves[0]["historical"] is False,
            "find_digest_leaves: an unrelated subject basename must not be marked historical", failures)

    # classify_record must split drift into historical vs actionable, hiding neither.
    def fake_reader(path: str) -> Optional[bytes]:
        return {"docs/design/SOME-FUNNEL.md": b"current bytes", "packages/foo/bar.ts": b"current bytes"}.get(path)

    mixed_leaves = [
        {"digest": "0" * 64, "digestKey": "sha256", "subject": "docs/design/SOME-FUNNEL.md", "via": "parent-key", "historical": True, "historicalReason": "marker"},
        {"digest": "0" * 64, "digestKey": "sha256", "subject": "packages/foo/bar.ts", "via": "sibling:path", "historical": False, "historicalReason": None},
    ]
    result = classify_record(mixed_leaves, fake_reader)
    _assert(result["status"] == "drift" and result["driftClass"] == "mixed"
            and result["driftHistoricalCount"] == 1 and result["driftActionableCount"] == 1,
            "classify_record: a record with one historical and one actionable drifted leaf must report both counts and class 'mixed'", failures)
    # Mutate: make both leaves historical; class must become historical-by-design, and status
    # must still say 'drift' (never silently promoted to 'current' because it is all-historical).
    all_historical_leaves = [dict(leaf, historical=True) for leaf in mixed_leaves]
    result_all_historical = classify_record(all_historical_leaves, fake_reader)
    _assert(result_all_historical["driftClass"] == "historical-by-design" and result_all_historical["status"] == "drift"
            and result_all_historical["driftActionableCount"] == 0,
            "classify_record: a record whose drift is entirely historical-by-design must say so, and must still report status 'drift'", failures)


def _check_rev_pinned_enumeration_ignores_working_tree(failures: List[str]) -> None:
    """item 1 (BLOCKING repair): sweep_evidence_records/sweep_mutation_records
    must enumerate and read docs/evidence/*.json entirely through --rev, not
    the working tree. Builds a disposable temp git repo, commits one evidence
    record, then dirties the working tree strictly after that commit (edits
    the stored digest in place, adds an uncommitted extra evidence file) and
    asserts the rev-pinned sweep sees neither change. The final block proves
    the fixture is not vacuous per rule 6: it re-derives what the OLD, buggy
    glob()+read_text() approach would have seen on this same working tree,
    and confirms it disagrees with the fixed, rev-pinned result -- i.e. if
    the fix regressed to the old approach, the assertions above would fail."""
    with tempfile.TemporaryDirectory(prefix="check-evidence-currency-selftest-") as tmp:
        repo = Path(tmp)

        def run(*args: str) -> None:
            subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=True)

        run("init", "-q")
        run("config", "user.email", "selftest@example.invalid")
        run("config", "user.name", "selftest")
        (repo / "docs" / "evidence").mkdir(parents=True)
        (repo / "subject.txt").write_text("hello world", encoding="utf-8")
        correct_digest = sha256_hex(b"hello world")
        record_path = repo / "docs" / "evidence" / "fixture-record.json"
        record_path.write_text(json.dumps({"kind": "fixture", "path": "subject.txt", "sha256": correct_digest}), encoding="utf-8")
        run("add", "-A")
        run("commit", "-q", "-m", "fixture commit")
        committed_rev = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True,
        ).stdout.strip()

        # Dirty the working tree strictly after the commit: edit the stored digest in place
        # (would read as drift if the working tree were consulted) and add an uncommitted
        # extra evidence file (would inflate the denominator if the working tree were consulted).
        record_path.write_text(json.dumps({"kind": "fixture", "path": "subject.txt", "sha256": "0" * 64}), encoding="utf-8")
        extra_path = repo / "docs" / "evidence" / "uncommitted-extra.json"
        extra_path.write_text(json.dumps({"kind": "extra", "path": "subject.txt", "sha256": correct_digest}), encoding="utf-8")

        report = sweep_evidence_records(committed_rev, "docs/evidence", repo_root=repo)
        _assert(report["denominator"] == 1,
                "sweep_evidence_records: --rev output must count only the committed record, not an uncommitted working-tree file", failures)
        _assert(report["current"] == 1 and report["drift"] == 0,
                "sweep_evidence_records: --rev output must read the committed digest bytes, not a dirtied uncommitted edit", failures)

        mutation_report = sweep_mutation_records(committed_rev, "docs/evidence", repo_root=repo)
        _assert(mutation_report["denominator"] == 0,
                "sweep_mutation_records: --rev output must be built only from the committed tree (this fixture's one record is not "
                "mutation-shaped, so the correct denominator is 0; an uncommitted extra file must not change it either way)", failures)

        # Prove the fixture is not vacuous (rule 6): the exact bug this guards against --
        # Path(evidence_dir).glob('*.json') plus path.read_text() -- reads the working tree
        # directly and must disagree with the rev-pinned result on this same fixture.
        buggy_files = sorted((repo / "docs" / "evidence").glob("*.json"))
        buggy_denominator = len(buggy_files)
        buggy_record = json.loads((repo / "docs" / "evidence" / "fixture-record.json").read_text(encoding="utf-8"))
        _assert(buggy_denominator == 2 and buggy_denominator != report["denominator"],
                "fixture self-check: a naive working-tree glob must see 2 files (the dirtied tree) where the rev-pinned "
                "sweep sees 1, or this fixture cannot distinguish the fix from the bug it repairs", failures)
        _assert(buggy_record["sha256"] == "0" * 64 and buggy_record["sha256"] != correct_digest,
                "fixture self-check: the working-tree copy of the record must carry the dirtied digest, or the drift "
                "half of this counterexample is not real", failures)


SELFTEST_CHECKS: List[Tuple[str, Callable[[List[str]], None]]] = [
    ("reading_plan_extraction", _check_reading_plan_extraction),
    ("reading_plan_classification", _check_reading_plan_classification),
    ("digest_leaf_sibling", _check_digest_leaf_sibling),
    ("digest_leaf_parent_key", _check_digest_leaf_parent_key),
    ("digest_leaf_flat_map", _check_digest_leaf_flat_map),
    ("classify_record", _check_classify_record),
    ("is_mutation_record", _check_is_mutation_record),
    ("classify_mutant_fragment", _check_classify_mutant_fragment),
    ("historical_vs_actionable_drift_classification", _check_historical_classification),
    ("rev_pinned_enumeration_ignores_working_tree", _check_rev_pinned_enumeration_ignores_working_tree),
]


def selftest() -> int:
    """Runs every check in SELFTEST_CHECKS independently: each gets its own
    try/except around a shared `failures` accumulator, so one check whose
    fixture-building code *raises* (not just fails an _assert -- e.g. an
    IndexError from a broken key regex) is caught, reported as a failure
    naming which check raised, and does not prevent the remaining,
    independent checks from running."""
    failures: List[str] = []
    raised: List[str] = []
    for name, fn in SELFTEST_CHECKS:
        try:
            fn(failures)
        except Exception as error:  # noqa: BLE001 - a raising predicate must not abort the remaining checks
            raised.append(name)
            failures.append(f"{name}: predicate raised {type(error).__name__}: {error}")
    if failures:
        raised_note = f" ({len(raised)} check(s) raised and were caught rather than aborting the run: {', '.join(raised)})" if raised else ""
        sys.stderr.write(f"selftest: {len(failures)} assertion(s) FAILED across {len(SELFTEST_CHECKS)} independent checks{raised_note}\n")
        for failure in failures:
            sys.stderr.write(f"  FAIL: {failure}\n")
        return 1
    sys.stderr.write(f"selftest: all fixture predicates behaved as asserted across {len(SELFTEST_CHECKS)} independent checks (mutate-and-confirm-fails, rule 6)\n")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rev", default="HEAD", help="git rev to read subject bytes at (default: HEAD)")
    parser.add_argument("--evidence-dir", default=EVIDENCE_DIR_REL_DEFAULT,
                         help="evidence directory, relative to the repo root. Its *.json files are enumerated "
                              "and read entirely from --rev via git ls-tree/git show, never the working tree; "
                              "this flag's default existence check below is the only working-tree read of it.")
    parser.add_argument("--json", action="store_true", help="print the report as JSON instead of a human summary")
    parser.add_argument("--out", default=None, help="also write the JSON report to this path")
    parser.add_argument("--selftest", action="store_true", help="run rule-6 fixtures and exit")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    evidence_dir_rel = args.evidence_dir.strip("/")
    if not (REPO_ROOT / evidence_dir_rel).is_dir():
        parser.error(f"--evidence-dir {args.evidence_dir!r} does not exist in the working tree "
                      f"(this is argument validation only; enumeration itself reads --rev via git ls-tree, never the working tree)")

    report = build_report(args.rev, evidence_dir_rel)

    if args.out:
        Path(args.out).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_human(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
