#!/usr/bin/env python3
"""Validate and summarize the consequence-granular Polaris RFC matrix.

Semantic judgments live in three frozen normalized matrix parts and an
explicit repair delta. This script makes no applicability judgment. It checks
identities, accepted-clause coverage, dispositions, current requirement
warrants and deterministic drift, then generates the matrix manifest.
"""

import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_capability_1_spec_dependencies as base
import build_polaris_project_wide_spec_dependencies as dependencies

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CHANGE = os.path.join(ROOT, "openspec", "changes", "polaris-project-wide-butlers-model")
INDEX = os.path.join(
    ROOT, ".syzygy", "governance", "contracts", "candidates", "05-CONTRACT-INDEX.yaml"
)
PARTS = (
    os.path.join(CHANGE, "contract-coverage-matrix", "RFC-0001-0003.md"),
    os.path.join(CHANGE, "contract-coverage-matrix", "RFC-0004-0006.md"),
    os.path.join(CHANGE, "contract-coverage-matrix", "RFC-0007-0009.md"),
)
REPAIR = os.path.join(CHANGE, "CONTRACT-COVERAGE-REPAIR-DELTA.md")
OUT = os.path.join(CHANGE, "CONTRACT-COVERAGE.md")

INDEX_RE = re.compile(r"^\s+- \{id: (RFC[1-9]-\d+(?:\([a-z]\))?),", re.M)
BASE_ROW_RE = re.compile(
    r"^\|\s*([^|]+\.c\d+)\s*\|\s*(RFC[1-9]-\d+(?:\([a-z]\))?)\s*\|"
    r"\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*(yes|no|unknown)\s*\|"
    r"\s*([^|]+)\s*\|\s*(covered:[^|]+|unknown-uncovered|believed-not-applicable)\s*\|$",
    re.M,
)
REPAIR_ROW_RE = re.compile(
    r"^\|\s*([^|]+\.r\d+)\s*\|\s*([^|]+\.c\d+)\s*\|"
    r"\s*(RFC[1-9]-\d+(?:\([a-z]\))?)\s*\|\s*([^|]+)\s*\|"
    r"\s*(covered:[^|]+|unknown-uncovered|believed-not-applicable)\s*\|$",
    re.M,
)
REQ_ID_RE = re.compile(r"PWB-REQ-\d{3}")


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def parse_inputs(part_texts=None, repair_text=None):
    if part_texts is None:
        part_texts = [base.read(path) for path in PARTS]
    if repair_text is None:
        repair_text = base.read(REPAIR)

    accepted = INDEX_RE.findall(base.read(INDEX))
    if len(accepted) != 324 or len(set(accepted)) != 324:
        raise ValueError(
            f"accepted denominator must be 324 unique clauses, got {len(accepted)}/{len(set(accepted))}"
        )
    accepted_set = set(accepted)

    base_rows = {}
    for part_text in part_texts:
        for match in BASE_ROW_RE.finditer(part_text):
            consequence_id, clause, authority, consequence, applicability, reason, disposition = (
                value.strip() for value in match.groups()
            )
            if consequence_id in base_rows:
                raise ValueError(f"duplicate base consequence ID: {consequence_id}")
            if clause not in accepted_set:
                raise ValueError(f"base row uses unaccepted clause: {clause}")
            base_rows[consequence_id] = {
                "id": consequence_id,
                "clause": clause,
                "authority": authority,
                "consequence": consequence,
                "applicability": applicability,
                "reason": reason,
                "disposition": disposition,
            }

    repair_rows = {}
    superseded = set()
    for match in REPAIR_ROW_RE.finditer(repair_text):
        consequence_id, prior_id, clause, consequence, disposition = (
            value.strip() for value in match.groups()
        )
        if consequence_id in repair_rows:
            raise ValueError(f"duplicate repair consequence ID: {consequence_id}")
        if prior_id not in base_rows:
            raise ValueError(f"repair supersedes missing base consequence: {prior_id}")
        if clause != base_rows[prior_id]["clause"]:
            raise ValueError(
                f"repair clause mismatch for {consequence_id}: {clause} != {base_rows[prior_id]['clause']}"
            )
        repair_rows[consequence_id] = {
            "id": consequence_id,
            "clause": clause,
            "authority": base_rows[prior_id]["authority"],
            "consequence": consequence,
            "applicability": "yes" if disposition != "believed-not-applicable" else "no",
            "reason": "repair delta",
            "disposition": disposition,
            "supersedes": prior_id,
        }
        superseded.add(prior_id)

    effective = {
        consequence_id: row
        for consequence_id, row in base_rows.items()
        if consequence_id not in superseded
    }
    effective.update(repair_rows)

    represented = {row["clause"] for row in effective.values()}
    missing_clauses = accepted_set - represented
    if missing_clauses:
        raise ValueError(f"accepted clauses without a consequence row: {sorted(missing_clauses)}")

    requirements, errors = dependencies.parse(base.read(dependencies.SPEC))
    if errors:
        raise ValueError("spec warrants do not validate: " + " | ".join(errors))
    warrants = {
        requirement_id: set(requirement_warrants["contracts"])
        for requirement_id, requirement_warrants in requirements
    }
    for row in effective.values():
        disposition = row["disposition"]
        if not disposition.startswith("covered:"):
            continue
        requirement_ids = REQ_ID_RE.findall(disposition)
        if not requirement_ids:
            raise ValueError(f"covered consequence has no requirement: {row['id']}")
        for requirement_id in requirement_ids:
            if requirement_id not in warrants:
                raise ValueError(
                    f"covered consequence cites missing requirement {requirement_id}: {row['id']}"
                )
            if row["clause"] not in warrants[requirement_id]:
                raise ValueError(
                    f"covered consequence {row['id']} cites {requirement_id}, but its warrants omit {row['clause']}"
                )

    return accepted, base_rows, repair_rows, effective


def render(part_texts=None, repair_text=None):
    accepted, base_rows, repair_rows, effective = parse_inputs(part_texts, repair_text)
    counts = {key: 0 for key in ("covered", "unknown-uncovered", "believed-not-applicable")}
    for row in effective.values():
        disposition = row["disposition"]
        key = "covered" if disposition.startswith("covered:") else disposition
        counts[key] += 1

    lines = [
        "# Contract coverage — polaris-project-wide-butlers-model",
        "",
        "> **GENERATED MANIFEST — do not edit.** The consequence judgments live in",
        "> `contract-coverage-matrix/`; reviewed repairs live in",
        "> `CONTRACT-COVERAGE-REPAIR-DELTA.md`. This file summarizes and verifies",
        "> them. The generator makes no semantic applicability decision.",
        "",
        "## Effective population",
        "",
        f"Accepted RFC 0001–0009 clauses: **{len(accepted)}**.",
        f"Effective consequence rows: **{len(effective)}** — "
        f"{counts['covered']} covered, {counts['unknown-uncovered']} Unknown uncovered, "
        f"{counts['believed-not-applicable']} believed not applicable.",
        "",
        "Every accepted clause has at least one effective consequence row. A",
        "`believed-not-applicable` row is an author/reviewer judgment, never an",
        "owner-reviewed N/A. Every `unknown-uncovered` row remains a disclosed gap.",
        "",
        "## Matrix parts",
        "",
        "| Artifact | sha256 | Base consequences |",
        "|---|---|---:|",
    ]
    for path in PARTS:
        text = base.read(path)
        count = len(BASE_ROW_RE.findall(text))
        rel = os.path.relpath(path, CHANGE)
        lines.append(f"| `{rel}` | `{digest(text)}` | {count} |")
    repair_text_actual = base.read(REPAIR) if repair_text is None else repair_text
    lines.extend(
        [
            "",
            "## Repair overlay",
            "",
            f"`CONTRACT-COVERAGE-REPAIR-DELTA.md` sha256 `{digest(repair_text_actual)}`",
            f"supersedes {len({row['supersedes'] for row in repair_rows.values()})} base rows with {len(repair_rows)} effective rows.",
            "",
            "## Verification",
            "",
            "```sh",
            "python3 scripts/build_polaris_project_wide_spec_dependencies.py --check",
            "python3 scripts/build_polaris_project_wide_contract_coverage.py --check",
            "python3 scripts/build_polaris_project_wide_contract_coverage.py --selftest",
            "```",
            "",
            "The checks enforce accepted-clause representation, unique consequence",
            "identities, valid repair supersession, closed dispositions and exact",
            "requirement-warrant agreement. They do not confirm semantic judgments;",
            "fresh review does.",
            "",
        ]
    )
    return "\n".join(lines)


def selftest():
    part_texts = [base.read(path) for path in PARTS]
    repair_text = base.read(REPAIR)
    output = render(part_texts, repair_text)

    first_repair = REPAIR_ROW_RE.search(repair_text)
    if first_repair is None:
        print("SELFTEST FAILED: no repair rows")
        return 1
    duplicated = repair_text + "\n" + first_repair.group(0) + "\n"
    try:
        render(part_texts, duplicated)
    except ValueError as error:
        if "duplicate repair" not in str(error):
            print(f"SELFTEST FAILED: wrong duplicate error: {error}")
            return 1
    else:
        print("SELFTEST FAILED: duplicate repair passed")
        return 1

    mutated = repair_text.replace("covered:PWB-REQ-001", "covered:PWB-REQ-999", 1)
    try:
        render(part_texts, mutated)
    except ValueError as error:
        if "missing requirement" not in str(error):
            print(f"SELFTEST FAILED: wrong warrant error: {error}")
            return 1
    else:
        print("SELFTEST FAILED: missing requirement passed")
        return 1

    if output != render(part_texts, repair_text):
        print("SELFTEST FAILED: output is nondeterministic")
        return 1
    print("selftest: duplicate repair, warrant mismatch and determinism predicates hold")
    return 0


def main(argv):
    if "--selftest" in argv:
        return selftest()
    output = render()
    if "--check" in argv:
        if not os.path.exists(OUT) or base.read(OUT) != output:
            print("DRIFT: CONTRACT-COVERAGE.md differs from verified matrices")
            return 1
        print("Polaris consequence matrix matches regeneration — 324 clauses represented")
        return 0
    with open(OUT, "w", encoding="utf-8") as file_handle:
        file_handle.write(output)
    print("wrote CONTRACT-COVERAGE.md consequence manifest")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
