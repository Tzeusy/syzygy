#!/usr/bin/env python3
"""Build and verify the Polaris dossier local-agent mode candidate (PR #353).

The candidate holds its four ADDED requirements in
``openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md``,
not ``specs/``, because a file under ``specs/`` joins the Polaris effective
composition that ``scripts/count_polaris_effective_scenarios.py`` recounts.
Placing it there is the install step of the owner's version-tagged sign-off
(``tasks.md``, "After sign-off"), and this module is the builder
``scripts/record_versioned_signoff.py`` runs for it. No digest argument
exists: the sign-off binds the tag ``polaris-dossier-local-agent-mode-v1.0``.

``--check`` verifies the package in either state and writes nothing:

- unapplied: the spec is in ``proposed/`` only; it carries exactly one
  ``## ADDED Requirements`` section naming the four requirements below; a
  scratch copy of the composition with it installed composes under both of
  the recount tool's parsers; the status page's figure equals the recount of
  the tree as it stands; and each package file that cites the proposed path
  in full still does (the install rewrites exactly those citations);
- applied: the spec is in ``specs/`` only, with the same shape; the status
  page's figure equals the recount, which composes the four requirements;
  and no package file cites the proposed path in full.

``--apply --at-sign-off`` is the one mode that writes. It refuses unless the
unapplied package verifies; then it moves the spec, removes the emptied
``proposed/`` directories, rewrites the full-path citations (a short
``proposed/polaris-generation/spec.md`` mention is prose about the move and
is left alone), and sets the status page's figure from the recount. A
candidate commit, review or merge performs no owner act.

``--selftest`` runs a mutation fixture per predicate in temporary trees.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import count_polaris_effective_scenarios as counter  # noqa: E402

CHANGE = pathlib.Path("openspec/changes/polaris-dossier-local-agent-mode")
CANDIDATE = pathlib.Path(
    ".syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode"
)
PROPOSED_SPEC = CHANGE / "proposed/polaris-generation/spec.md"
INSTALLED_SPEC = CHANGE / "specs/polaris-generation/spec.md"
STATUS = pathlib.Path(counter.STATUS_PAGE_REL)
REQUIREMENTS = (
    "Operator-agent authoring mode",
    "Agent brief and mechanically checked draft",
    "Fresh-context review in the operator-agent mode",
    "Self-reported discovery and in-session clarification",
)
#: Package files whose code spans name the proposed path in full. CG-1b
#: requires such a span to resolve, so the install rewrites them.
PATH_CITERS = (CANDIDATE / "REVIEW-BRIEF.md", CANDIDATE / "SEMANTIC-DELTA.md")
FIGURE_RE = re.compile(r"(\d+) requirements and (\d+) scenarios in the effective composition")


class Refusal(RuntimeError):
    """The package does not verify; nothing is written."""


def state(root: pathlib.Path) -> str:
    proposed = (root / PROPOSED_SPEC).is_file()
    installed = (root / INSTALLED_SPEC).is_file()
    if proposed and not installed:
        return "unapplied"
    if installed and not proposed:
        return "applied"
    return "both" if proposed else "neither"


def spec_findings(text: str, label: str) -> list[str]:
    findings = []
    sections = [m.group(1) for m in counter.SECTION_HEADER_RE.finditer(text)]
    if sections != ["ADDED"]:
        findings.append(f"{label}: sections {sections}, expected exactly one ADDED section")
    try:
        names = tuple(entry.name for entry in counter.parse_regex(text, label).added)
        manual = tuple(entry.name for entry in counter.parse_manual(text, label).added)
    except counter.ScenarioCountError as exc:
        return findings + [str(exc)]
    if names != manual:
        findings.append(f"{label}: the recount tool's two parsers disagree on requirement names")
    if names != REQUIREMENTS:
        findings.append(f"{label}: requirements {list(names)}, expected {list(REQUIREMENTS)}")
    return findings


def recount(root: pathlib.Path) -> tuple[int, int, set[str]]:
    """Requirement and scenario totals, and normalized composed names, of a tree."""
    result = counter.build_composition(root)
    names = {counter.normalize_name(name) for name, _count in result.per_requirement.values()}
    return len(result.per_requirement), result.total, names


def recount_installed(root: pathlib.Path) -> tuple[int, int, set[str]]:
    """Recount a scratch copy of the composition with the proposed spec installed."""
    files = counter.discover_composition_files(root)
    with tempfile.TemporaryDirectory(prefix="dossier-install-") as tmp:
        scratch = pathlib.Path(tmp)
        for path in files:
            rel = path.relative_to(root)
            (scratch / rel).parent.mkdir(parents=True, exist_ok=True)
            (scratch / rel).write_bytes(path.read_bytes())
        (scratch / INSTALLED_SPEC).parent.mkdir(parents=True, exist_ok=True)
        (scratch / INSTALLED_SPEC).write_bytes((root / PROPOSED_SPEC).read_bytes())
        return recount(scratch)


def status_figure(root: pathlib.Path) -> tuple[int, int]:
    found = FIGURE_RE.findall((root / STATUS).read_text(encoding="utf-8"))
    if len(found) != 1:
        raise Refusal(f"{STATUS}: expected one effective-composition figure, found {len(found)}")
    return int(found[0][0]), int(found[0][1])


def check(root: pathlib.Path = ROOT) -> list[str]:
    current = state(root)
    if current not in ("unapplied", "applied"):
        return [f"the spec is in {current} of proposed/ and specs/"]
    spec = PROPOSED_SPEC if current == "unapplied" else INSTALLED_SPEC
    findings = spec_findings((root / spec).read_text(encoding="utf-8"), spec.as_posix())
    if findings:
        return findings
    try:
        reqs, scenarios, _names = recount(root)
        if status_figure(root) != (reqs, scenarios):
            findings.append(f"{STATUS} figure {status_figure(root)} differs from the recount "
                            f"{(reqs, scenarios)}")
        if current == "unapplied":
            _r, _s, names = recount_installed(root)
        else:
            names = _names
        missing = {counter.normalize_name(n) for n in REQUIREMENTS} - names
        if missing:
            findings.append(f"the composition does not carry {sorted(missing)}")
    except (counter.ScenarioCountError, Refusal, OSError) as exc:
        findings.append(str(exc))
    full = PROPOSED_SPEC.as_posix()
    for citer in PATH_CITERS:
        text = (root / citer).read_text(encoding="utf-8")
        if current == "unapplied" and full not in text:
            findings.append(f"{citer}: does not cite {full}; the install would rewrite nothing")
        if current == "applied" and full in text:
            findings.append(f"{citer}: still cites {full}")
    return findings


def applied(root: pathlib.Path = ROOT) -> bool:
    return state(root) == "applied" and not check(root)


def apply(root: pathlib.Path = ROOT) -> int:
    if state(root) != "unapplied":
        print(f"REFUSED: the package is {state(root)}, not unapplied; nothing written")
        return 2
    findings = check(root)
    if findings:
        print("REFUSED: the package does not verify; nothing written")
        for finding in findings:
            print(f"  - {finding}")
        return 2
    src, dst = root / PROPOSED_SPEC, root / INSTALLED_SPEC
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    for leftover in (src.parent, src.parent.parent):
        if leftover.is_dir() and not any(leftover.iterdir()):
            leftover.rmdir()
    full, installed = PROPOSED_SPEC.as_posix(), INSTALLED_SPEC.as_posix()
    for citer in PATH_CITERS:
        path = root / citer
        path.write_text(path.read_text(encoding="utf-8").replace(full, installed), encoding="utf-8")
    reqs, scenarios, _names = recount(root)
    status = root / STATUS
    text = status.read_text(encoding="utf-8")
    figure = FIGURE_RE.search(text)
    assert figure is not None  # check() required exactly one
    status.write_text(text.replace(
        figure.group(0), f"{reqs} requirements and {scenarios} scenarios in the effective composition"),
        encoding="utf-8")
    after = check(root)
    if after:
        print("FAILED after apply: " + " | ".join(after))
        return 1
    print(f"installed {installed}; {STATUS} now reads {reqs} requirements and {scenarios} scenarios")
    return 0


# --- selftest ---------------------------------------------------------------

def _req(name: str, scenarios: int) -> str:
    return f"### Requirement: {name}\n\nText.\n\n" + "".join(
        f"#### Scenario: s{i}\n\n- WHEN x\n- THEN y\n\n" for i in range(scenarios))


def _fixture(root: pathlib.Path, *, dossier: str | None = None, figure: str = "2 requirements and 3 scenarios",
             citers: bool = True) -> None:
    def write(rel: pathlib.Path | str, text: str) -> None:
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    write("openspec/changes/base/specs/polaris-generation/spec.md",
          "## ADDED Requirements\n\n" + _req("Alpha", 1) + _req("Beta", 1))
    write("openspec/changes/overlay/specs/polaris-generation/spec.md",
          "## MODIFIED Requirements\n\n" + _req("Beta", 2))
    write(STATUS, f"Polaris carries {figure} in the effective composition.\n")
    write(PROPOSED_SPEC, dossier if dossier is not None else
          "## ADDED Requirements\n\n" + "".join(_req(n, 1) for n in REQUIREMENTS))
    for citer in PATH_CITERS:
        write(citer, f"Subject: `{PROPOSED_SPEC.as_posix()}`\n" if citers else "Subject: elsewhere\n")


def selftest() -> int:
    import contextlib
    import io

    results: list[tuple[str, bool]] = []

    def quiet(fn, *args):
        with contextlib.redirect_stdout(io.StringIO()):
            return fn(*args)

    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        _fixture(root)
        results.append(("unapplied package verifies", check(root) == []))
        results.append(("unapplied package is not applied", not applied(root)))
        results.append(("apply installs and returns 0", quiet(apply, root) == 0))
        results.append(("applied package verifies", applied(root)))
        results.append(("proposed directory removed", not (root / CHANGE / "proposed").exists()))
        results.append(("status figure follows the recount",
                        status_figure(root) == (6, 7)))
        results.append(("full-path citations rewritten",
                        all(INSTALLED_SPEC.as_posix() in (root / c).read_text() for c in PATH_CITERS)))
        results.append(("second apply refuses", quiet(apply, root) == 2))

    def refused(name: str, mutate=None, **fixture) -> None:
        with tempfile.TemporaryDirectory() as t:
            root = pathlib.Path(t)
            _fixture(root, **fixture)
            if mutate:
                mutate(root)
            before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
            code = quiet(apply, root)
            after = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
            results.append((f"refused: {name}", bool(check(root)) and code == 2 and before == after))

    refused("a fifth requirement",
            dossier="## ADDED Requirements\n\n" + "".join(_req(n, 1) for n in (*REQUIREMENTS, "Extra")))
    refused("a requirement missing",
            dossier="## ADDED Requirements\n\n" + "".join(_req(n, 1) for n in REQUIREMENTS[:3]))
    refused("a MODIFIED section in the candidate",
            dossier="## ADDED Requirements\n\n" + "".join(_req(n, 1) for n in REQUIREMENTS)
            + "## MODIFIED Requirements\n\n" + _req("Beta", 1))
    def collide(root: pathlib.Path) -> None:
        base = root / "openspec/changes/base/specs/polaris-generation/spec.md"
        base.write_text(base.read_text() + _req(REQUIREMENTS[0], 1))
        (root / STATUS).write_text("Polaris carries 3 requirements and 4 scenarios in the effective composition.\n")
    refused("a name colliding with the composition", mutate=collide)
    refused("status figure stale before install", figure="2 requirements and 4 scenarios")
    refused("a citer no longer naming the proposed path", citers=False)
    refused("spec in both proposed/ and specs/", mutate=lambda root: (
        (root / INSTALLED_SPEC).parent.mkdir(parents=True),
        shutil.copy(root / PROPOSED_SPEC, root / INSTALLED_SPEC)))
    refused("spec in neither", mutate=lambda root: (root / PROPOSED_SPEC).unlink())

    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        _fixture(root)
        quiet(apply, root)
        (root / STATUS).write_text("Polaris carries 2 requirements and 3 scenarios in the effective composition.\n")
        results.append(("applied: a stale status figure fails", not applied(root)))
        quiet(apply, root)
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        _fixture(root)
        quiet(apply, root)
        citer = root / PATH_CITERS[0]
        citer.write_text(citer.read_text() + f"`{PROPOSED_SPEC.as_posix()}`\n")
        results.append(("applied: a remaining full-path citation fails", not applied(root)))

    failing = 0
    for name, ok in results:
        failing += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"{len(results)} fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--selftest", action="store_true")
    parser.add_argument("--at-sign-off", action="store_true",
                        help="required with --apply: only the sign-off recorder installs")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.apply:
        if not args.at_sign_off:
            parser.error("--apply writes signed subjects; pass --at-sign-off")
        return apply(ROOT)
    findings = check(ROOT)
    if findings:
        print("FAILED")
        for finding in findings:
            print(f"  - {finding}")
        return 1
    print(f"OK: the package verifies ({state(ROOT)})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
