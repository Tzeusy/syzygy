#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""Derive and check the tracked docs/reviews campaign partition."""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable


REVIEW_PREFIX = "docs/reviews/"
README = Path("docs/README.md")


@dataclasses.dataclass(frozen=True)
class Campaign:
    key: str
    display: str
    patterns: tuple[str, ...]


def campaign(key: str, display: str, *patterns: str) -> Campaign:
    return Campaign(key, display, tuple(patterns))


CAMPAIGNS = (
    campaign("cap1-slices", "`R-S2` … `R-S7`", r"R-S[2567]-RISK-FLOOR-REVIEW\.md"),
    campaign("cap1-runtime", "`R-RT-*`", r"R-RT-.*\.md"),
    campaign("three-surface-poc", "`R-POC-*`", r"R-POC-.*\.md"),
    campaign(
        "polaris-project-wide",
        "Project-wide Polaris specification and observation gate",
        r"POLARIS-PROJECT-WIDE-SIGNOFF-PACKET\.md",
        r"R-POLARIS-(?:A1-LOCAL-AUDIT-BOUNDARY|PRECONDITION-READ-BOUNDARY-INCIDENT)\.md",
        r"R-POLARIS-(?:OBSERVATION-GATE-CONFIRMATION|POC-EXCEPTION-(?:INDEPENDENT|SECURITY)|TRUSTED-BOOTSTRAP-CONFIRMATION)-RAW\.md",
        r"R-POLARIS-PROJECT-WIDE-.*\.md",
    ),
    campaign(
        "general-trusted-bootstrap",
        "`R-GENERAL-TRUSTED-*`",
        r"R-GENERAL-TRUSTED-.*\.md",
    ),
    campaign("pwb-state1", "`R-PWB-STATE1-*`", r"R-PWB-STATE1-.*\.md"),
    campaign("pwb-effect", "`R-PWB-EFFECT-*`", r"R-PWB-EFFECT-.*\.md"),
    campaign("pwb-truth", "`R-PWB-TRUTH-*`", r"R-PWB-TRUTH-.*\.md"),
    campaign(
        "pwb-live",
        "PWB live exact-head",
        r"(?:R-PWB-LIVE-.*|2026-09-05-pwb-live-.*)\.md",
    ),
    campaign(
        "pwb-recovery",
        "PWB recovery reconciliation",
        r"(?:R-PWB-RECOVERY-.*|2026-09-06-pwb-recovery-.*)\.md",
    ),
    campaign("pwb-p63", "`R-PWB-P63-*`", r"R-PWB-P63-.*\.md"),
    campaign(
        "orrery-height",
        "Orrery height finding",
        r"R-POLARIS-ORRERY-HEIGHT-FINDING-RAW\.md",
    ),
    campaign(
        "polaris-editorial",
        "Polaris editorial repair",
        r"(?:2026-09-09-polaris-editorial-repair|R-POLARIS-EDITORIAL-.*)\.md",
    ),
    campaign(
        "polaris-manifesto",
        "Polaris manifesto design and code",
        r"R-POLARIS-MANIFESTO-.*\.md",
    ),
    campaign(
        "polaris-reading-assets",
        "Polaris reading assets and navigation",
        r"R-POLARIS-(?:GUIDE-NAVIGATION|LIVE-READING|READING-ASSETS)-.*\.md",
    ),
    campaign(
        "pwb-declared-home", "PWB declared-home repair", r"R-PWB-DECLARED-HOME-.*\.md"
    ),
    campaign(
        "pwb-walkthrough", "PWB owner-walkthrough capture", r"R-PWB-WALKTHROUGH-.*\.md"
    ),
    campaign(
        "polaris-diagrams",
        "Polaris visible diagrams",
        r"R-POLARIS-(?:DIAGRAM-VISIBILITY|VISIBLE-DIAGRAMS)-.*\.md",
    ),
    campaign(
        "polaris-generation-kit",
        "Polaris generation kit",
        r"R-POLARIS-GENERATION-KIT-.*\.md",
    ),
    campaign(
        "polaris-generator-product",
        "Polaris generator product and scope",
        r"R-POLARIS-GENERATOR-(?:FRESH-PRODUCT|PRODUCT-READINESS|SCOPE-CONFIRMATION)-.*\.md",
    ),
    campaign(
        "polaris-generator-authority",
        "Polaris generator authority and recorder",
        r"R-POLARIS-GENERATOR-(?:AUTHORITY-PAIRING-CONFIRMATION|AUTHORITY-READINESS|AUTHORITY-STAGING-CONFIRMATION|CONCRETE-OFFER|FINAL-READINESS|FRESH-AUTHORITY|RECORDER-CONFIRMATION)-.*\.md",
    ),
    campaign(
        "polaris-understanding",
        "Polaris understanding amendment",
        r"R-POLARIS-UNDERSTANDING-.*\.md",
    ),
    campaign("pwb-m1-lane-a", "PWB M1 lane A", r"R-PWB-M1-POLARIS-LANE-A-RAW\.md"),
    campaign(
        "pwb-scoped-attributes",
        "P-68 scoped-attributes package",
        r"R-PWB-SCOPED-ATTRIBUTES-.*\.md",
    ),
    *(
        campaign(
            f"polaris-m{number}",
            f"Polaris M{number} funnel",
            rf"R-POLARIS-M{number}-.*-FUNNEL(?:-[0-9]+)?-RAW\.md",
        )
        for number in range(2, 17)
    ),
    campaign(
        "retention-posture",
        "P-79 retention-posture gate",
        r"R-POLARIS-RETENTION-POSTURE-.*\.md",
    ),
    campaign("exact-source", "P-81 exact-source gate", r"R-PWB-EXACT-SOURCE-.*\.md"),
    campaign("machine-view", "P-72 machine-view gate", r"R-PWB-MACHINE-VIEW-.*\.md"),
    campaign("opening-band", "P-71 opening-band gate", r"R-PWB-OPENING-BAND-.*\.md"),
    campaign(
        "registry-currency",
        "P-69/P-72 registry gate",
        r"R-PWB-REGISTRY-CURRENCY-.*\.md",
    ),
)


class PartitionError(RuntimeError):
    pass


def git(*args: str) -> bytes:
    return subprocess.check_output(("git", *args), stderr=subprocess.STDOUT)


def tracked_regular_paths() -> list[str]:
    records = git("ls-files", "--stage", "-z", "--", "docs/reviews/").split(b"\0")
    paths: list[str] = []
    for record in records:
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, _object_id, stage = metadata.decode("ascii").split()
        path = raw_path.decode("utf-8", "surrogateescape")
        if stage == "0" and mode.startswith("100") and path.startswith(REVIEW_PREFIX):
            paths.append(path)
    return sorted(paths)


def tree_regular_paths() -> list[str]:
    records = git("ls-tree", "-r", "-z", "HEAD", "--", "docs/reviews/").split(b"\0")
    paths: list[str] = []
    for record in records:
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, object_type, _object_id = metadata.decode("ascii").split()
        path = raw_path.decode("utf-8", "surrogateescape")
        if (
            mode.startswith("100")
            and object_type == "blob"
            and path.startswith(REVIEW_PREFIX)
        ):
            paths.append(path)
    return sorted(paths)


def matches(path: str, campaigns: Iterable[Campaign] = CAMPAIGNS) -> list[str]:
    basename = path.removeprefix(REVIEW_PREFIX)
    return [
        item.key
        for item in campaigns
        if any(re.fullmatch(pattern, basename) for pattern in item.patterns)
    ]


def partition(
    paths: Iterable[str], campaigns: Iterable[Campaign] = CAMPAIGNS
) -> dict[str, list[str]]:
    campaigns = tuple(campaigns)
    result = {item.key: [] for item in campaigns}
    unmatched: list[str] = []
    overlaps: dict[str, list[str]] = {}
    for path in paths:
        memberships = matches(path, campaigns)
        if not memberships:
            unmatched.append(path)
        elif len(memberships) > 1:
            overlaps[path] = memberships
        else:
            result[memberships[0]].append(path)
    if unmatched or overlaps:
        lines = ["review campaign partition failed"]
        lines.extend(f"unmatched: {path}" for path in unmatched)
        lines.extend(
            f"overlap: {path}: {', '.join(groups)}" for path, groups in overlaps.items()
        )
        raise PartitionError("\n".join(lines))
    return result


def add_date(path: str) -> str:
    output = (
        git("log", "--follow", "--diff-filter=A", "--format=%cs", "--", path)
        .decode()
        .splitlines()
    )
    if not output:
        raise PartitionError(f"no add date: {path}")
    return output[-1]


def date_span(paths: Iterable[str]) -> str:
    dates = sorted({add_date(path) for path in paths})
    if not dates:
        raise PartitionError("campaign has no paths")
    return dates[0] if len(dates) == 1 else f"{dates[0]} → {dates[-1]}"


def report(paths: list[str]) -> dict[str, object]:
    grouped = partition(paths)
    rows = []
    for item in CAMPAIGNS:
        members = grouped[item.key]
        if not members:
            raise PartitionError(f"empty campaign: {item.key}")
        rows.append(
            {
                "key": item.key,
                "display": item.display,
                "count": len(members),
                "recorded": date_span(members),
                "paths": members,
            }
        )
    return {
        "denominator_predicate": "stage-0 tracked regular files recursively under docs/reviews/ at HEAD",
        "total": len(paths),
        "raw": sum(path.endswith("-RAW.md") for path in paths),
        "other": sum(not path.endswith("-RAW.md") for path in paths),
        "assigned": sum(int(row["count"]) for row in rows),
        "unmatched": [],
        "overlaps": {},
        "observed_date": dt.date.today().isoformat(),
        "campaigns": rows,
    }


def logical_markdown_lines(text: str) -> list[str]:
    logical: list[str] = []
    pending = ""
    fence: str | None = None
    for physical in text.splitlines():
        marker = re.match(r"^\s*(```+|~~~+)", physical)
        if marker:
            token = marker.group(1)[0]
            fence = None if fence == token else token
            if pending:
                logical.append(pending)
                pending = ""
            logical.append(physical)
            continue
        if fence:
            logical.append(physical)
            continue
        pending = f"{pending}{physical.lstrip()}" if pending else physical
        if len(re.findall(r"(?<!\\)`", pending)) % 2 == 0:
            logical.append(pending)
            pending = ""
    if pending:
        raise PartitionError("unclosed Markdown code span")
    return logical


def path_line_citations(text: str) -> list[tuple[str, int]]:
    joined = "\n".join(logical_markdown_lines(text))
    return [
        (path, int(line)) for path, line in re.findall(r"`([^`\n]+\.md):(\d+)`", joined)
    ]


ID_SEED = re.compile(r"(?P<prefix>[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-)(?P<number>\d+)")


def expand_continuation_ids(text: str) -> tuple[set[str], list[str]]:
    joined = "\n".join(logical_markdown_lines(text))
    found = {match.group(0) for match in ID_SEED.finditer(joined)}
    unresolved: list[str] = []
    for seed in ID_SEED.finditer(joined):
        prefix = seed.group("prefix")
        width = len(seed.group("number"))
        start = int(seed.group("number"))
        tail = joined[seed.end() : seed.end() + 120]
        range_match = re.match(
            r"\s*(\.\.|…|–)\s*(?:" + re.escape(prefix) + r")?(\d+)", tail
        )
        if range_match:
            end = int(range_match.group(2))
            if end < start or end - start > 500:
                unresolved.append(seed.group(0) + range_match.group(0))
            else:
                found.update(
                    f"{prefix}{number:0{width}d}" for number in range(start, end + 1)
                )
            continue
        list_tail = tail
        while True:
            item = re.match(
                r"\s*(?:/|,|\band\b)\s*(?:" + re.escape(prefix) + r")?(\d+)",
                list_tail,
            )
            if not item:
                break
            found.add(f"{prefix}{int(item.group(1)):0{width}d}")
            list_tail = list_tail[item.end() :]
        dangling = re.match(r"\s*(?:/|,|\band\b|\.\.|…|–)(?:\s|$)", list_tail)
        if dangling:
            unresolved.append(seed.group(0) + dangling.group(0))
    return found, sorted(set(unresolved))


def parse_campaign_table(readme: str) -> dict[str, tuple[int, str, str]]:
    lines = readme.splitlines()
    try:
        start = lines.index(
            "| Campaign | Files | Recorded | What was under review | Last verdict of record, and where the findings landed |"
        )
    except ValueError as error:
        raise PartitionError("review campaign table header missing") from error
    rows: dict[str, tuple[int, str, str]] = {}
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            raise PartitionError(f"malformed campaign row: {line}")
        display, count, recorded, _subject, verdict = cells
        if display in rows:
            raise PartitionError(f"duplicate campaign row: {display}")
        try:
            rows[display] = (int(count), recorded, verdict)
        except ValueError as error:
            raise PartitionError(
                f"non-integer campaign count: {display}: {count}"
            ) from error
    return rows


def validate_verdict_citation(verdict: str, display: str) -> None:
    citations = path_line_citations(verdict)
    if not citations:
        raise PartitionError(f"campaign lacks exact verdict citation: {display}")
    resolved = False
    for raw_path, line_number in citations:
        path = (
            Path(raw_path)
            if raw_path.startswith(REVIEW_PREFIX)
            else Path("docs/reviews") / raw_path
        )
        if not path.is_file():
            raise PartitionError(
                f"missing verdict citation target: {display}: {raw_path}"
            )
        lines = path.read_text(encoding="utf-8").splitlines()
        if line_number < 1 or line_number > len(lines):
            raise PartitionError(
                f"verdict citation line out of range: {display}: {raw_path}:{line_number}"
            )
        if re.search(
            r"CONFIRM|PASS|READY|REVISE|CHANGES REQUESTED|FAIL",
            lines[line_number - 1],
            re.IGNORECASE,
        ):
            resolved = True
    if not resolved:
        raise PartitionError(
            f"campaign citation does not resolve to a verdict line: {display}"
        )


def check_readme(readme_path: Path, data: dict[str, object]) -> None:
    text = readme_path.read_text(encoding="utf-8")
    actual_rows = parse_campaign_table(text)
    expected_rows = {str(row["display"]): row for row in data["campaigns"]}  # type: ignore[index]
    validate_campaign_rows(actual_rows, expected_rows)
    for display, (_count, _recorded, verdict) in actual_rows.items():
        validate_verdict_citation(verdict, display)
    summary = re.search(
        r"The\s+(\d+)\s+rows\s+partition\s+the\s+tracked\s+directory\s+at\s+HEAD:\s+"
        r"(\d+)\s+files,\s+(\d+)\s+assigned,\s+no\s+remainder\s+"
        r"\[Observed\s+—\s+re-derived\s+(\d{4}-\d{2}-\d{2})",
        text,
    )
    if not summary:
        raise PartitionError("derived partition summary missing or malformed")
    expected_summary = (
        len(expected_rows),
        int(data["total"]),
        int(data["assigned"]),
        str(data["observed_date"]),
    )
    actual_summary = (
        int(summary.group(1)),
        int(summary.group(2)),
        int(summary.group(3)),
        summary.group(4),
    )
    if actual_summary != expected_summary:
        raise PartitionError(
            f"stale partition summary: README={actual_summary}; derived={expected_summary}"
        )


def validate_campaign_rows(
    actual_rows: dict[str, tuple[int, str, str]],
    expected_rows: dict[str, dict[str, object]],
) -> None:
    missing = sorted(set(expected_rows) - set(actual_rows))
    extra = sorted(set(actual_rows) - set(expected_rows))
    if missing or extra:
        raise PartitionError(
            f"README campaign rows differ; missing={missing}; extra={extra}"
        )
    for display, expected in expected_rows.items():
        count, recorded, _verdict = actual_rows[display]
        if count != expected["count"] or recorded != expected["recorded"]:
            raise PartitionError(
                f"stale campaign row: {display}: README=({count}, {recorded}); derived=({expected['count']}, {expected['recorded']})"
            )


def validate_denominator_sets(primary: list[str], secondary: list[str]) -> None:
    only_primary = sorted(set(primary) - set(secondary))
    only_secondary = sorted(set(secondary) - set(primary))
    if only_primary or only_secondary:
        raise PartitionError(
            "denominator methods disagree\n"
            + "\n".join(f"ls-files only: {path}" for path in only_primary)
            + "\n"
            + "\n".join(f"ls-tree only: {path}" for path in only_secondary)
        )


def second_method(primary: list[str]) -> None:
    secondary = tree_regular_paths()
    validate_denominator_sets(primary, secondary)
    print(
        f"second-method PASS: git ls-files={len(primary)}; git ls-tree={len(secondary)}; exact path sets equal"
    )


def selftest() -> None:
    fixtures = 0

    fixtures += 1
    assert logical_markdown_lines("See `R-EXAMPLE-\nRAW.md:3` now") == [
        "See `R-EXAMPLE-RAW.md:3` now"
    ]
    assert path_line_citations("See `R-EXAMPLE-\nRAW.md:3` now") == [
        ("R-EXAMPLE-RAW.md", 3)
    ]

    fixtures += 1
    ids, unresolved = expand_continuation_ids("Repair PWB-LIVE-02, 03, 05 and 15.")
    assert {
        "PWB-LIVE-02",
        "PWB-LIVE-03",
        "PWB-LIVE-05",
        "PWB-LIVE-15",
    } <= ids and not unresolved

    fixtures += 1
    ids, unresolved = expand_continuation_ids("P-68…P-83")
    assert {"P-68", "P-83"} <= ids and len(ids) == 16 and not unresolved
    ids, unresolved = expand_continuation_ids("PWB-LIVE-02/03/05/15")
    assert {
        "PWB-LIVE-02",
        "PWB-LIVE-03",
        "PWB-LIVE-05",
        "PWB-LIVE-15",
    } <= ids and not unresolved

    fixtures += 1
    _ids, unresolved = expand_continuation_ids("P-83..P-68")
    assert unresolved

    fixtures += 1
    try:
        partition(
            ["docs/reviews/R-OTHER-RAW.md"],
            (campaign("known", "known", r"R-KNOWN-RAW\.md"),),
        )
    except PartitionError as error:
        assert "unmatched" in str(error)
    else:
        raise AssertionError("unassigned-path mutant survived")

    fixtures += 1
    try:
        partition(
            ["docs/reviews/R-DUP-RAW.md"],
            (campaign("a", "a", r"R-.*"), campaign("b", "b", r"R-DUP-.*")),
        )
    except PartitionError as error:
        assert "overlap" in str(error)
    else:
        raise AssertionError("overlap mutant survived")

    fixtures += 1
    sample = """| Campaign | Files | Recorded | What was under review | Last verdict of record, and where the findings landed |
|---|---|---|---|---|
| example | 1 | 2026-01-01 | subject | `R-EXAMPLE-RAW.md:1` |
"""
    try:
        validate_campaign_rows(
            parse_campaign_table(sample),
            {"example": {"count": 2, "recorded": "2026-01-01"}},
        )
    except PartitionError as error:
        assert "stale campaign row" in str(error)
    else:
        raise AssertionError("stale-row-count mutant survived")

    fixtures += 1
    try:
        validate_denominator_sets(["docs/reviews/A.md"], ["docs/reviews/B.md"])
    except PartitionError as error:
        assert "denominator" in str(error)
    else:
        raise AssertionError("denominator-mismatch mutant survived")

    print(f"selftest PASS: {fixtures} fixtures")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, metavar="README")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--second-method", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return 0
    paths = tracked_regular_paths()
    data = report(paths)
    if args.second_method:
        second_method(paths)
    if args.check:
        check_readme(args.check, data)
        print(
            f"partition PASS: denominator={data['total']}; assigned={data['assigned']}; "
            f"raw={data['raw']}; other={data['other']}; unmatched=0; overlaps=0; campaigns={len(CAMPAIGNS)}"
        )
    elif args.json:
        print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
    elif not args.second_method:
        for row in data["campaigns"]:  # type: ignore[index]
            print(f"{row['display']}\t{row['count']}\t{row['recorded']}")
        print(
            f"total={data['total']} assigned={data['assigned']} raw={data['raw']} "
            f"other={data['other']} unmatched=0 overlaps=0 observed={data['observed_date']}"
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (PartitionError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
