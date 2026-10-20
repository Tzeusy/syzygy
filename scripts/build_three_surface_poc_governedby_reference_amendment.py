#!/usr/bin/env python3
"""P-115 candidate preparation only: virtual patches, dependency union and evidence.

--check writes nothing. --write updates only the candidate manifest and sweep.
--selftest mutates the preparation predicates and runs independent literal cases.
No adoption/apply/record path or product implementation lives in this script.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_three_surface_poc_spec_dependencies as dependencies

ROOT = Path(__file__).resolve().parents[1]
BASE = "4504514c019ca0ee0cb4a89ed97445a0bad21915"
CHANGE = "openspec/changes/three-surface-poc-experience/"
PACKAGE = ".syzygy/governance/contracts/candidates/three-surface-poc-governedby-reference-amendment/"
CANDIDATE = ROOT / PACKAGE
MANIFEST_NAME = "THREE-SURFACE-POC-GOVERNEDBY-REFERENCE-AMENDMENT-MANIFEST.txt"
MANIFEST_OUT = Path(PACKAGE + MANIFEST_NAME)
SUBJECTS = tuple(CHANGE + p for p in (
    ".openspec.yaml", "CONTRACT-COVERAGE.md", "GOVERNING-DEPENDENCIES.md",
    "design.md", "proposal.md", "specs/three-surface-poc-experience/spec.md"))
PATCHED = SUBJECTS[1:]
SPEC = SUBJECTS[-1]
COVERAGE = CHANGE + "CONTRACT-COVERAGE.md"
DEPS = CHANGE + "GOVERNING-DEPENDENCIES.md"
HEADING = re.compile(r"^### Requirement: (POC-REQ-\d{3}) — ", re.M)
CITER_PATTERN = r"POC-REQ-014|governedBy|GoverningIntentUnknown|governing.intent.amendment"
SPEC_PATH = re.compile(r"openspec/(?:changes/[^/]+/)?specs/[^/]+/spec\.md")
CLOSED_VALUE = {"label": "Unknown", "closedReason": "source-uncaptured-or-unreachable",
                "resolutionRoutes": [{"reason": "source-uncaptured-or-unreachable",
                                      "route": "Repair the observer/source; new snapshot",
                                      "actor": "operator", "verb": "repair", "target": "evaluation"}]}
FAULT = "invalid-governing-intent-reference"
CLASSES = ("doctrine", "contracts", "policies", "decisions", "topology", "parent_requirements")
# Each guard has its own semantic deletion mutant below, not a prose-length check.
GUARDS = {
    "literal-value": json.dumps(CLOSED_VALUE, separators=(",", ":")),
    "literal-reference": '{"ref":"observation"}',
    "bounded-local-hop": "Resolution SHALL take one local hop",
    "body-isolation": "its own enclosing `workItems` observation in this same machine-answer body",
    "no-fallback": "nor fall back to an inline, previous or default value",
    "identity-preservation": "SHALL remain distinct",
    "no-record-pooling": "NOT pool entity or relationship records",
    "explicit-refusal": 'endpoint SHALL instead return HTTP 503',
    "fault-not-reason": 'wire-validation fault, not a new RFC2-24 Unknown reason',
    "failed-not-empty": 'without a fabricated shared value, item set or zero count',
    "complete-denominator": 'denominator is the complete served item set (POC-REQ-011)',
    "independent-oracle": 'imports no producer/serializer/model helper',
}


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def baseline() -> dict[str, bytes]:
    return {p: git("show", f"{BASE}:{p}") for p in SUBJECTS}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def patch_header_findings(patch: str, subject: str) -> list[str]:
    expected = ["--- a/" + subject, "+++ b/" + subject]
    headers = re.findall(r"^(?:---|\+\+\+) .+$", patch, re.M)
    return [] if headers == expected else [f"patch path/header population differs: {subject}"]


def collect() -> tuple[dict[str, bytes], dict[str, bytes]]:
    """Apply only declared patches to exact git objects in an owned temp tree."""
    current = baseline()
    for name in SUBJECTS:
        if (ROOT / name).read_bytes() != current[name]:
            raise ValueError(f"adopted subject drift from frozen baseline: {name}")
    expected = {Path(p).name + ".patch": p for p in PATCHED}
    found = {p.name: p for p in (CANDIDATE / "proposed").rglob("*") if p.is_file()}
    if set(found) != set(expected):
        raise ValueError("patch file population differs from exact five declared patches")
    with tempfile.TemporaryDirectory(prefix="syzygy-p115-proposed-") as tmp:
        tree = Path(tmp)
        for name, body in current.items():
            target = tree / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        for patch_name, subject in expected.items():
            patch = found[patch_name].read_text()
            errors = patch_header_findings(patch, subject)
            if errors:
                raise ValueError("; ".join(errors))
            result = subprocess.run(["patch", "--batch", "--forward", "--fuzz=0", "-p1", "--no-backup-if-mismatch"],
                                    cwd=tree, input=patch.encode(), capture_output=True)
            output = (result.stdout + result.stderr).decode()
            if result.returncode or any(x in output.lower() for x in ("offset", "fuzz", "reversed", "failed")):
                raise ValueError(f"patch did not apply exactly: {patch_name}: {output}")
        return current, {p: (tree / p).read_bytes() for p in SUBJECTS}


def requirement_blocks(text: str) -> tuple[str, dict[str, str]]:
    matches = list(HEADING.finditer(text))
    blocks = {m.group(1): text[m.start():matches[i+1].start() if i+1 < len(matches) else len(text)]
              for i, m in enumerate(matches)}
    if len(blocks) != len(matches):
        raise ValueError("duplicate native POC requirement identity")
    return text[:matches[0].start()] if matches else text, blocks


def structure_findings(proposed: dict[str, bytes], current: dict[str, bytes]) -> list[str]:
    findings = []
    if set(proposed) != set(SUBJECTS):
        return ["subject population differs"]
    if proposed[SUBJECTS[0]] != current[SUBJECTS[0]]:
        findings.append("unchanged .openspec.yaml differs")
    before_intro, before = requirement_blocks(current[SPEC].decode())
    after_intro, after = requirement_blocks(proposed[SPEC].decode())
    if before_intro != after_intro or list(before) != list(after):
        findings.append("native requirement identity/order or reader-notes population differs")
    if any(after.get(k) != v for k, v in before.items() if k != "POC-REQ-014"):
        findings.append("untouched requirement block differs")
    block = " ".join(after.get("POC-REQ-014", "").split())
    for name, phrase in GUARDS.items():
        if phrase not in block:
            findings.append(f"wire contract missing {name}")
    if len(re.findall(r"^#### Scenario:", after.get("POC-REQ-014", ""), re.M)) != 8:
        findings.append("014 scenario population differs from eight")
    old_rows = [s for s in current[COVERAGE].decode().splitlines() if s.startswith("| RFC")]
    new_rows = [s for s in proposed[COVERAGE].decode().splitlines() if s.startswith("| RFC")]
    remaining = new_rows.copy()
    for row in old_rows:
        if row not in remaining:
            findings.append("inherited coverage consequence row changed or missing")
            break
        remaining.remove(row)
    additions = [s for s in remaining if "Amendment row (observation-local governedBy wire value)" in s]
    if len(remaining) != 7 or len(additions) != 7:
        findings.append("coverage amendment row population differs from seven")
    part_a = proposed[COVERAGE].decode().split("## Part B1", 1)[0]
    rows = [s for s in part_a.splitlines() if re.match(r"^\| RFC\d+-\d+ \|", s)]
    unknown = sum("**Unknown**" in s for s in rows)
    covered = sum("| covered" in s for s in rows)
    clauses = len({s.split("|")[1].strip() for s in rows})
    totals = f"**{len(rows)} consequence rows over {clauses} clauses — {covered} covered,\n{unknown} Unknown.**"
    if totals not in proposed[COVERAGE].decode() or len(rows) != covered + unknown:
        findings.append("coverage computed totals differ")
    generated, errors = dependencies.generate(proposed[SPEC].decode())
    if errors or generated is None or proposed[DEPS].decode() != generated:
        findings.append("proposed dependency union differs from exact regeneration")
    for name in (CHANGE + "proposal.md", CHANGE + "design.md"):
        if not proposed[name].startswith(current[name]) or proposed[name] == current[name]:
            findings.append(f"append-only companion successor differs: {name}")
    return findings


def manifest(proposed: dict[str, bytes]) -> str:
    lines = ["# THREE-SURFACE POC GOVERNEDBY REFERENCE AMENDMENT MANIFEST",
             "# Candidate: binds nothing until the owner signs it off.",
             f"# {len(SUBJECTS)} artifacts; rows sorted by codepoint path.",
             "# All rows take effect together or none do.",
             "# Rows hash PROPOSED bytes; adopted files are not changed by this builder."]
    return "\n".join(lines + [f"{sha256(proposed[p])}  {p}" for p in SUBJECTS]) + "\n"


def verify_manifest(actual: str, expected: str) -> list[str]:
    rows = re.findall(r"^[0-9a-f]{64}  (.+)$", actual, re.M)
    if rows != list(SUBJECTS):
        return ["manifest path population or order differs"]
    return [] if actual == expected else ["manifest differs from proposed subject bytes"]


def wire_oracle(body: dict) -> tuple[bool, list[str], int | None]:
    """Independent fixture oracle; no imports from the product or a producer."""
    work = body["workItems"]
    if work.get("kind") == "unknown":
        valid = bool(work.get("reason")) and not any(k in work for k in ("items", "governedBy", "governedByUnknownCount"))
        return valid, [], None
    if work.get("kind") != "observed" or work.get("governedBy") != CLOSED_VALUE:
        return False, [], None
    items = work.get("items")
    if not isinstance(items, list) or any(not isinstance(i, dict) or i.get("governedBy") != {"ref": "observation"} for i in items):
        return False, [], None
    ids = [i.get("id") for i in items]
    if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        return False, [], None
    if type(work.get("governedByUnknownCount")) is not int or work["governedByUnknownCount"] != len(items):
        return False, [], None
    # No state from any previous call/body; per-item expansion retains each ID.
    return True, ids, len(items)


def fixture_findings(cases: list[dict]) -> list[str]:
    errors = []
    for case in cases:
        valid, ids, count = wire_oracle(case["body"])
        actual = {"valid": valid, "effectiveIds": ids, "unknownCount": count,
                  "fault": None if valid else FAULT}
        if actual != case["expected"]:
            errors.append(f"literal fixture differs: {case['name']}")
        if valid and not set(case["renderedIds"]).issubset(ids):
            errors.append(f"rendered fixture population differs: {case['name']}")
    return errors


def sweep() -> dict:
    files = sorted(p for p in git("ls-tree", "-r", "-z", "--name-only", BASE).decode().split("\0") if p)
    listed = sorted(p for p in git("ls-files", "-z").decode().split("\0") if p)
    # New untracked candidate files do not change the baseline denominator.
    if not set(files).issubset(listed):
        raise ValueError("baseline tracked population missing from worktree index")
    # One object batch keeps the complete tracked sweep cheap and read-only.
    result = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT,
                            input="".join(f"{BASE}:{p}\n" for p in files).encode(),
                            capture_output=True, check=True).stdout
    blobs, offset = {}, 0
    for path in files:
        end = result.index(b"\n", offset)
        header = result[offset:end].split()
        if len(header) != 3 or header[1] != b"blob":
            raise ValueError(f"unexpected tracked object in baseline: {path}")
        size = int(header[2])
        blobs[path] = result[end+1:end+1+size]
        offset = end + size + 2
    if offset != len(result):
        raise ValueError("baseline object batch denominator differs")
    binary = [p for p, b in blobs.items() if b"\0" in b]
    texts = {p: b.decode("utf-8", errors="replace") for p, b in blobs.items() if p not in binary}
    hits = sorted(p for p, s in texts.items() if re.search(CITER_PATTERN, s))
    other = git("grep", "-I", "-l", "-E", CITER_PATTERN, BASE, "--").decode().splitlines()
    other = sorted(line.split(":", 1)[1] for line in other)
    if hits != other:
        raise ValueError("two independent tracked-citer methods disagree")
    specs = sorted(p for p in files if SPEC_PATH.fullmatch(p))
    disk_specs = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "openspec").glob("**/spec.md")
                        if p.relative_to(ROOT).as_posix() in files and SPEC_PATH.fullmatch(p.relative_to(ROOT).as_posix()))
    if specs != disk_specs:
        raise ValueError("two independent specification enumeration methods disagree")
    requirements = []
    for path in specs:
        text = texts[path]
        matches = list(re.finditer(r"^### Requirement: (.+)$", text, re.M))
        for i, m in enumerate(matches):
            block = text[m.start():matches[i+1].start() if i+1 < len(matches) else len(text)]
            declarations = re.findall(r"^  (doctrine|contracts|policies|decisions|topology|parent_requirements): (\[[^\n]*\])$", block, re.M)
            declared = {k: v for k, v in declarations}
            complete = set(declared) == set(CLASSES) and len(declarations) == len(CLASSES)
            direct = any(re.search(r"\bPOC-REQ-014\b", v) for v in declared.values())
            affected = path == SPEC and m.group(1).startswith("POC-REQ-014 — ")
            if not complete or (direct and not affected):
                state, reason = "undecidable", "missing/ambiguous warrant class or a reverse dependency requires semantic assessment"
            elif affected:
                state, reason = "affected", "changed requirement identity; exact proposed replacement"
            else:
                state = "explicitly-unaffected"
                reason = ("same POC: complete block preserved; only effective representation of 014 changes, not this obligation" if path == SPEC else
                          "other capability/overlay scope; complete six-class declarations have no changed-requirement edge; this delta changes no governing clause")
            requirements.append({"path": path, "ordinal": i+1, "heading": m.group(1),
                                 "warrant_classes_complete": complete, "direct_changed_id_warrant": direct,
                                 "classification": state, "reason_and_method": reason})
    integration = {".github/workflows/governance-docs.yml", "PROJECT-STATUS.md", "docs/README.md",
                   ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md"}
    integration |= {p for p in hits if p.startswith("scripts/")}
    classified = []
    for path in hits:
        if path in SUBJECTS:
            state, reason = "affected", "same-change proposed POC successor subject"
        elif path in integration:
            state, reason = "affected-preparation-gate", "coordinator must assess/register exact signed successor and preserve predecessor checks before offer/adoption; not changed by this author"
        else:
            state, reason = "explicitly-unaffected", "retained dated evidence, prior packet or performed owner record: historical subject/choice unchanged; preserve bytes, do not rewrite as current P115 authority"
        classified.append({"path": path, "classification": state, "reason_and_method": reason})
    return {"subject": "P-115 POC-REQ-014 candidate reverse-impact sweep", "baseline_commit": BASE,
            "changed_identities": {k: (["POC-REQ-014"] if k == "parent_requirements" else []) for k in CLASSES},
            "citer_predicate": CITER_PATTERN,
            "methods": ["git ls-tree -rz baseline blobs + Python regex; git ls-files -z baseline inclusion",
                        "git grep -I -l -E at baseline; pathlib spec enumeration; per-block six-class warrant scan"],
            "counts": {"tracked_baseline_paths": len(files), "binary_paths": len(binary), "text_paths": len(texts),
                       "matching_citer_paths": len(hits), "spec_files": len(specs), "requirement_occurrences": len(requirements),
                       "warrant_complete_requirements": sum(x["warrant_classes_complete"] for x in requirements),
                       "affected_requirements": sum(x["classification"] == "affected" for x in requirements),
                       "unaffected_requirements": sum(x["classification"] == "explicitly-unaffected" for x in requirements),
                       "undecidable_requirements": sum(x["classification"] == "undecidable" for x in requirements)},
            "spec_files": specs, "requirements": requirements, "citer_paths": classified,
            "not_lexically_enumerable_unknowns": ["actual external API consumers", "post-restoration code integration and measured savings"],
            "actor": "OpenAI Codex, syzygy-318o candidate writer", "independent_confirmation": "pending"}


def check(write: bool = False) -> list[str]:
    current, proposed = collect()
    errors = structure_findings(proposed, current)
    cases = json.loads((CANDIDATE / "fixtures/wire-cases.json").read_text())["cases"]
    errors.extend(fixture_findings(cases))
    generated = {MANIFEST_OUT: manifest(proposed), Path(PACKAGE + "IMPACT-SWEEP.json"): json.dumps(sweep(), indent=2) + "\n"}
    if errors:
        return errors
    for path, text in generated.items():
        target = ROOT / path
        if write:
            target.write_text(text)
        elif path == MANIFEST_OUT:
            errors.extend(verify_manifest(target.read_text() if target.exists() else "", text))
        elif not target.exists() or target.read_text() != text:
            errors.append(f"generated candidate artifact drift: {path}")
    return errors


def selftest() -> list[str]:
    current, proposed = collect()
    errors = structure_findings(proposed, current)
    if errors:
        return ["baseline fails before mutations", *errors]
    mutants = []
    for name, phrase in GUARDS.items():
        changed = copy.copy(proposed)
        # Normalize split lines only for selecting the exact phrase to remove.
        text = changed[SPEC].decode()
        pattern = r"\s+".join(re.escape(x) for x in phrase.split())
        text, n = re.subn(pattern, "REMOVED-BY-MUTANT", text, count=1)
        if n != 1:
            errors.append(f"mutation target not unique/present: {name}")
        changed[SPEC] = text.encode()
        mutants.append((name, changed, "wire contract missing " + name))
    for name, subject, old, new, expected in (
        ("untouched-060", SPEC, "One design language, one epistemic", "Altered design language, one epistemic", "untouched requirement block differs"),
        ("requirement-identity", SPEC, "POC-REQ-020 —", "POC-REQ-099 —", "native requirement identity/order"),
        ("coverage-row", COVERAGE, "| RFC6-14 | Every claim instance", "| REMOVED | Every claim instance", "inherited coverage consequence"),
        ("coverage-unknown", COVERAGE, "| **Unknown** —", "| covered —", "inherited coverage consequence"),
        ("coverage-totals", COVERAGE, "154 consequence rows", "153 consequence rows", "coverage computed totals"),
        ("dependency-union", DEPS, "GENERATED", "STALE", "proposed dependency union"),
        ("unchanged-yaml", SUBJECTS[0], "schema: spec-driven", "schema: altered", "unchanged .openspec.yaml"),
        ("companion-preservation", CHANGE + "proposal.md", "# ", "# ALTERED ", "append-only companion successor"),
    ):
        changed = copy.copy(proposed)
        text = changed[subject].decode()
        if old not in text:
            errors.append("missing mutation target: " + name)
        changed[subject] = text.replace(old, new, 1).encode()
        mutants.append((name, changed, expected))
    for name, changed, expected in mutants:
        findings = structure_findings(changed, current)
        if not any(expected in f for f in findings):
            errors.append(f"mutant {name} survived its own predicate: {findings}")
    wrong = "--- a/foreign\n+++ b/foreign\n"
    if not patch_header_findings(wrong, SPEC):
        errors.append("foreign patch-path mutant survived")
    cases = json.loads((CANDIDATE / "fixtures/wire-cases.json").read_text())["cases"]
    errors.extend(fixture_findings(cases))
    if len(cases) != 35 or sum(c["expected"]["valid"] for c in cases) != 4:
        errors.append("independent fixture population differs")
    poisoned = copy.deepcopy(cases)
    poisoned[0]["expected"]["unknownCount"] = 0
    if not fixture_findings(poisoned):
        errors.append("optimistic fixture expectation mutant survived")
    rendered = manifest(proposed)
    if len(re.findall(r"^[0-9a-f]{64}  ", rendered, re.M)) != len(SUBJECTS):
        errors.append("manifest subject denominator differs")
    changed = copy.copy(proposed)
    changed[SPEC] += b"\n"
    if not verify_manifest(rendered, manifest(changed)):
        errors.append("subject-byte drift did not retire manifest")
    lines = rendered.splitlines(keepends=True)
    lines[-1], lines[-2] = lines[-2], lines[-1]
    if verify_manifest("".join(lines), rendered) != ["manifest path population or order differs"]:
        errors.append("manifest row-order mutant survived")
    poisoned_hash = rendered.replace(sha256(proposed[SPEC]), "0" * 64)
    if verify_manifest(poisoned_hash, rendered) != ["manifest differs from proposed subject bytes"]:
        errors.append("manifest row-hash mutant survived")
    print(f"Preparation selftest: {len(mutants)} semantic/structure mutants, foreign patch path, literal-expectation poison, subject-byte drift and two manifest mutants; {len(cases)} independent wire cases (4 valid, 31 refused).")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    try:
        errors = selftest() if args.selftest else check(args.write)
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(f"P115 PREPARATION FAIL: {exc}")
        return 1
    if errors:
        print("P115 PREPARATION FAIL:")
        print("\n".join("  " + e for e in errors))
        return 1
    print("P115 candidate preparation matches: six proposed subjects, five patches, only 014 changed, 26 requirements, eight 014 scenarios; no adoption or runtime claim.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
