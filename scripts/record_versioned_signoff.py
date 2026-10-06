#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Record/check an owner's version-tagged sign-off of a candidate package.

Scope A of `decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`:
for implementation-phase governed artifacts the owner signs off by selecting an
option in a structured question that names the package and a `major.minor`
version. No typed phrase and no digest argument exists. The sign-off binds a
git tag, `<package>-v<major>.<minor>`, on the commit that carries the applied
result; a later edit is a new version, never a retirement of the earlier one.

`--record <package> --version M.m --date YYYY-MM-DD --review <raw>
--owner-selection-quote "<the option label and question the owner answered>"`
validates, in this order, and writes nothing until every step passes:

1. the version is `major.minor` (no leading zeros) and the date a calendar
   form; the owner's selection quote is one non-empty line carrying no
   64-hex digest;
2. the version is not already recorded for the package;
3. the review raw's first four non-blank lines carry exactly one
   `Reviewed commit: <40 hex>`, one `Manifest SHA-256: <64 hex>` and one
   `Verdict:` line, which is `CONFIRM` or `CONFIRM WITH EXCEPTIONS`; REVISE or
   any other verdict refuses. A package that declares its reviewed `subject`
   is bound by that head digest: it must equal the sha256 of the subject's
   bytes in the working tree, before anything is applied. The reviewed commit
   is provenance and the base of step 5's comparison, never the binding; a
   rebase-merged review commit stays fetchable from its pull request's ref.
   The raw must also name the package's key, so a review of another package
   cannot be offered for this one;
4. for `CONFIRM WITH EXCEPTIONS`, the raw's `## Findings` section numbers its
   findings continuously as `**Finding N — title** (blocking|revise|note)`,
   where the severity word may carry a qualifier after it ("(note, for the
   owner)", "(note: reported for the owner, not resolved)"); the leading
   word is the severity, and a `note` whose qualifier names "blocking" or
   "revise" is refused as ambiguous rather than read either way; every
   finding is a `note`. A note's qualifier fails closed: it is read as a note
   only when each comma-separated clause is one of `QUALIFIER_CLAUSES`
   ("for the owner", "for the owner's view", "reported for the owner", "not
   resolved", "editorial"), and any other wording refuses as ambiguous; and `--disposition <record>` names the raw on a
   `Reviewed record:` line and numbers exactly the raw's findings;
5. the candidate package directory, and any further directory the package
   declares (a specification change under `openspec/changes/`), at the
   working tree equals the package at the commit the review read (sibling
   `ROUND-<n>-DISPOSITIONS.md` records inside the candidate directory, and
   the named disposition, are not package bytes; in a further directory
   every file is);
6. the package's own builder check passes on the unapplied package.

Then the package's patches are applied through its builder, the dedicated
record `decisions/<STEM>-SIGNOFF-v<M.m>.md` is written, one marked block is
appended to `ACCEPTANCE-ACT-RECORD.md`, and the tag to create is printed.

`--check <package> --version M.m` reports "not performed" and exits 0 when no
record exists, fails on a partial record, re-validates the review head and
findings, regenerates the record and the aggregate block exactly, and, when the
version is the package's latest, requires the applied tree. `--selftest` runs
a mutation fixture per predicate in temporary git repositories.
"""
from __future__ import annotations

import argparse
import importlib
import pathlib
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from typing import Callable

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import record_pwb_behavior_amendment_acts as beh  # noqa: E402

DECISIONS = pathlib.Path(".syzygy/governance/decisions")
AGGREGATE_REL = DECISIONS / "ACCEPTANCE-ACT-RECORD.md"
DIRECTION_REL = DECISIONS / "OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md"
CANDIDATES = pathlib.Path(".syzygy/governance/contracts/candidates")
VERSION_RE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
HEX64_RE = re.compile(r"[0-9a-f]{64}")
COMMIT_LINE_RE = re.compile(r"^Reviewed commit: ([0-9a-f]{40})$")
MANIFEST_LINE_RE = re.compile(r"^Manifest SHA-256: [0-9a-f]{64}$")
VERDICT_LINE_RE = re.compile(r"^Verdict:\s*(.*?)\s*$")
VERDICTS = ("CONFIRM", "CONFIRM WITH EXCEPTIONS")
SEVERITY_RE = re.compile(
    r"^\*\*Finding (\d+) [—–-] [^\n]*?\*\*\s*\((blocking|revise|note)(?![A-Za-z])([^)\n]*)\)",
    re.MULTILINE)
#: The only clauses a `note` qualifier may carry; anything else, a stronger
#: severity in any spelling included, makes the finding ambiguous.
QUALIFIER_CLAUSES = ("for the owner", "for the owner's view", "reported for the owner",
                     "not resolved", "editorial")
MANIFEST_DIGEST_RE = re.compile(r"^Manifest SHA-256: ([0-9a-f]{64})$")
SIBLING_RECORD_RE = re.compile(r"(^|/)ROUND-\d+-DISPOSITIONS\.md$")
FINDINGS_HEADING = "## Findings"


@dataclass(frozen=True)
class Package:
    """One covered package. The three callables take the repository root."""
    key: str
    title: str
    kind: str                        # "contract successor" | "behavior amendment"
    candidate: pathlib.Path
    record_stem: str
    check: Callable[[pathlib.Path], list[str]]
    apply: Callable[[pathlib.Path], int]
    applied: Callable[[pathlib.Path], bool]
    #: Further directories whose bytes the review read (an OpenSpec change).
    also: tuple[pathlib.Path, ...] = ()
    #: The reviewed subject, pre-apply; the raw's head digest must hash it.
    subject: pathlib.Path | None = None
    #: The subject's reviewed bytes when they are not the file on disk (a
    #: successor carried as patches to an installed version): computed
    #: pre-apply from the tree, and hashed in place of ``subject``.
    subject_bytes: Callable[[pathlib.Path], bytes] | None = None
    #: Owner-selectable options (``--option``); the record names those taken.
    options: tuple[str, ...] = ()
    #: For a package with options: apply with the options taken.
    apply_with: Callable[[pathlib.Path, frozenset[str]], int] | None = None
    #: For a package with options: the options the applied tree carries, so
    #: ``--check`` holds the record's options line to the tree.
    applied_options: Callable[[pathlib.Path], frozenset[str]] | None = None


def _module(name: str):
    return importlib.import_module(name)


def _rows_hash_tree(root: pathlib.Path, manifest: pathlib.Path) -> bool:
    target = root / manifest
    if not target.is_file():
        return False
    rows = beh.ROW_RE.findall(target.read_text(encoding="utf-8"))
    if not rows:
        return False
    for sha, path in rows:
        file = root / path
        if not file.is_file():
            return False
        actual = beh.digest(file.read_bytes())
        # A later performed act or sign-off may have re-patched this row; it
        # is history when the tree hashes to that source's own manifest row.
        if actual != sha and actual not in beh._later_rows(
                root, None, path, skip_manifest=manifest):
            return False
    return True


def real_packages() -> dict[str, Package]:
    missing = lambda: _module("build_pwb_missing_currency_disclosure_scenario")  # noqa: E731
    dismissal = lambda: _module("build_pwb_dismissal_expiry_amendment")  # noqa: E731
    container = lambda: _module("build_pwb_container_shape_profile_amendment")  # noqa: E731
    item_depth = lambda: _module("build_pwb_item_depth_amendment")  # noqa: E731
    readability = lambda: _module("build_pwb_readability_successor")  # noqa: E731
    tree_framing = lambda: _module("build_pwb_tree_framing_amendment")  # noqa: E731
    dossier = lambda: _module("build_polaris_dossier_local_agent_mode")  # noqa: E731
    dossier11 = lambda: _module("build_polaris_dossier_local_agent_mode_v1_1")  # noqa: E731
    return {
        "pwb-missing-currency-disclosure-scenario": Package(
            "pwb-missing-currency-disclosure-scenario",
            "PWB missing-currency disclosure scenario",
            "behavior amendment",
            CANDIDATES / "pwb-missing-currency-disclosure-scenario",
            "PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO",
            lambda root: missing().check(),
            lambda root: missing().apply(True),
            lambda root: _rows_hash_tree(root, missing().MANIFEST_OUT),
        ),
        "pwb-dismissal-expiry-amendment": Package(
            "pwb-dismissal-expiry-amendment",
            "PWB dismissal-expiry amendment",
            "behavior amendment",
            CANDIDATES / "pwb-dismissal-expiry-amendment",
            "PWB-DISMISSAL-EXPIRY-AMENDMENT",
            lambda root: dismissal().check(),
            lambda root: dismissal().apply(True),
            lambda root: _rows_hash_tree(root, dismissal().MANIFEST_OUT),
        ),
        "pwb-container-shape-profile-amendment": Package(
            "pwb-container-shape-profile-amendment",
            "PWB container-shape profile amendment",
            "behavior amendment",
            CANDIDATES / "pwb-container-shape-profile-amendment",
            "PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT",
            lambda root: container().check(),
            lambda root: container().apply(True),
            lambda root: _rows_hash_tree(root, container().MANIFEST_OUT),
        ),
        "pwb-item-depth-amendment": Package(
            "pwb-item-depth-amendment",
            "PWB item-depth amendment",
            "behavior amendment",
            CANDIDATES / "pwb-item-depth-amendment",
            "PWB-ITEM-DEPTH-AMENDMENT",
            lambda root: item_depth().check()[0],
            lambda root: item_depth().apply(True),
            lambda root: _rows_hash_tree(root, item_depth().MANIFEST_OUT),
        ),
        "pwb-readability-successor": Package(
            "pwb-readability-successor",
            "PWB readability successor",
            "behavior amendment",
            CANDIDATES / "pwb-readability-successor",
            "PWB-READABILITY-SUCCESSOR",
            lambda root: readability().check()[0],
            lambda root: readability().apply(True),
            lambda root: _rows_hash_tree(root, readability().MANIFEST_OUT),
        ),
        "pwb-tree-framing-amendment": Package(
            "pwb-tree-framing-amendment",
            "PWB tree-framing amendment",
            "behavior amendment",
            CANDIDATES / "pwb-tree-framing-amendment",
            "PWB-TREE-FRAMING-AMENDMENT",
            lambda root: tree_framing().check()[0],
            lambda root: tree_framing().apply(True),
            lambda root: _rows_hash_tree(root, tree_framing().MANIFEST_OUT),
        ),
        "polaris-dossier-local-agent-mode": Package(
            "polaris-dossier-local-agent-mode",
            "Polaris dossier local-agent mode",
            "specification delta",
            CANDIDATES / "polaris-dossier-local-agent-mode",
            "POLARIS-DOSSIER-LOCAL-AGENT-MODE",
            lambda root: dossier().check(root),
            lambda root: dossier().apply(root),
            lambda root: dossier().applied(root),
            also=(pathlib.Path("openspec/changes/polaris-dossier-local-agent-mode"),),
            subject=pathlib.Path("openspec/changes/polaris-dossier-local-agent-mode/"
                                 "proposed/polaris-generation/spec.md"),
        ),
        # Version 1.1 patches the installed v1.0: its own candidate directory,
        # builder and reviewed bytes, under the same key, record stem and tag
        # series. ``package_for`` selects it for ``--version 1.1``.
        "polaris-dossier-local-agent-mode@1.1": Package(
            "polaris-dossier-local-agent-mode",
            "Polaris dossier local-agent mode",
            "specification delta",
            CANDIDATES / "polaris-dossier-local-agent-mode-v1-1",
            "POLARIS-DOSSIER-LOCAL-AGENT-MODE",
            lambda root: dossier11().check(root),
            lambda root: dossier11().apply(root),
            lambda root: dossier11().applied(root),
            also=(pathlib.Path("openspec/changes/polaris-dossier-local-agent-mode"),),
            subject=pathlib.Path("openspec/changes/polaris-dossier-local-agent-mode/"
                                 "specs/polaris-generation/spec.md"),
            subject_bytes=lambda root: dossier11().subject_bytes(root),
            options=("n6",),
            apply_with=lambda root, options: dossier11().apply(root, options),
            applied_options=lambda root: dossier11().state(root)[1],
        ),
    }


def package_for(packages: dict[str, Package], key: str, version: str) -> Package | None:
    """The entry for ``key`` at ``version``: a ``key@version`` entry, else ``key``."""
    return packages.get(f"{key}@{version}") or packages.get(key)


# --- names ------------------------------------------------------------------

def tag_for(pkg: Package, version: str) -> str:
    return f"{pkg.key}-v{version}"


def record_rel(pkg: Package, version: str) -> pathlib.Path:
    return DECISIONS / f"{pkg.record_stem}-SIGNOFF-v{version}.md"


def block_markers(pkg: Package, version: str) -> tuple[str, str]:
    return (f"<!-- versioned-signoff:{pkg.key}:v{version} -->",
            f"<!-- /versioned-signoff:{pkg.key}:v{version} -->")


def recorded_versions(root: pathlib.Path, pkg: Package) -> list[tuple[int, int]]:
    found = []
    for path in (root / DECISIONS).glob(f"{pkg.record_stem}-SIGNOFF-v*.md"):
        m = re.fullmatch(rf"{re.escape(pkg.record_stem)}-SIGNOFF-v(\d+)\.(\d+)\.md", path.name)
        if m:
            found.append((int(m.group(1)), int(m.group(2))))
    return sorted(found)


# --- validation -------------------------------------------------------------

def validate_inputs(version: str, date: str, quote: str) -> None:
    if not VERSION_RE.fullmatch(version):
        raise ValueError(f"version {version!r} is not major.minor without leading zeros")
    if not DATE_RE.fullmatch(date):
        raise ValueError("--date must be YYYY-MM-DD")
    if not quote.strip() or "\n" in quote or "\r" in quote:
        raise ValueError("owner selection quote must be one non-empty line")
    if HEX64_RE.search(quote):
        raise ValueError("owner selection quote must not carry a digest; "
                         "a version-tagged sign-off names the version, not bytes")


def parse_head(review: str) -> tuple[str, str]:
    """(reviewed commit, verdict) from the first four non-blank lines."""
    head = [line for line in review.splitlines() if line.strip()][:4]
    commits = [m.group(1) for line in head if (m := COMMIT_LINE_RE.fullmatch(line))]
    manifests = [line for line in head if MANIFEST_LINE_RE.fullmatch(line)]
    verdicts = [m.group(1) for line in head if (m := VERDICT_LINE_RE.fullmatch(line))]
    if len(commits) != 1:
        raise ValueError("review head does not carry exactly one `Reviewed commit:` line")
    if len(manifests) != 1:
        raise ValueError("review head does not carry exactly one `Manifest SHA-256:` line")
    if len(verdicts) != 1:
        raise ValueError("review head does not carry exactly one `Verdict:` line")
    if verdicts[0] not in VERDICTS:
        raise ValueError(f"review verdict {verdicts[0]!r} is not CONFIRM or "
                         "CONFIRM WITH EXCEPTIONS")
    return commits[0], verdicts[0]


def qualifier_allowed(qualifier: str) -> bool:
    """True for no qualifier, or one whose every clause is an allowed one."""
    if not qualifier.strip():
        return True
    if qualifier[0] not in ",:":
        return False
    clauses = [c.strip().replace("\u2019", "'") for c in qualifier[1:].split(",")]
    return all(c in QUALIFIER_CLAUSES for c in clauses)


def review_findings(review: str) -> dict[int, str]:
    section = beh._raw_findings_section(review, FINDINGS_HEADING)
    numbers = beh._finding_number_set(
        section, label="review findings", forms=beh.RAW_FINDING_FORMS)
    severities = {}
    for n, sev, qualifier in SEVERITY_RE.findall(section):
        if sev == "note" and not qualifier_allowed(qualifier):
            raise ValueError(f"review finding {n} is tagged ({sev}{qualifier}); a note "
                             f"qualifier other than {list(QUALIFIER_CLAUSES)} is ambiguous")
        severities[int(n)] = sev
    unclassified = sorted(numbers - set(severities))
    if unclassified:
        raise ValueError(f"review findings {unclassified} carry no "
                         "(blocking|revise|note) severity")
    return {n: severities[n] for n in numbers}


def validate_disposition(root: pathlib.Path, review_rel: str, disposition_rel: str | None,
                         findings: dict[int, str]) -> None:
    if not disposition_rel:
        raise ValueError("CONFIRM WITH EXCEPTIONS needs --disposition: a record "
                         "beside the package that dispositions every note")
    path = root / disposition_rel
    if not path.is_file():
        raise ValueError(f"missing disposition record: {disposition_rel}")
    text = path.read_text(encoding="utf-8")
    if f"Reviewed record: {review_rel}" not in text.splitlines():
        raise ValueError("disposition record does not name the reviewed raw on a "
                         "`Reviewed record:` line")
    actual = beh._finding_number_set(
        text, label="disposition record", forms=beh.DISPOSITION_FINDING_FORMS)
    if actual != set(findings):
        raise ValueError(f"disposition record findings {sorted(actual)} do not match "
                         f"the review's {sorted(findings)}")


def validate_review(root: pathlib.Path, review_rel: str, disposition_rel: str | None
                    ) -> tuple[str, str]:
    path = root / review_rel
    if not path.is_file():
        raise ValueError(f"missing review raw: {review_rel}")
    review = path.read_text(encoding="utf-8")
    commit, verdict = parse_head(review)
    if verdict == "CONFIRM WITH EXCEPTIONS":
        findings = review_findings(review)
        if not findings:
            raise ValueError("CONFIRM WITH EXCEPTIONS carries no countable finding; "
                             "a notes-only verdict with no note is a parse failure")
        bad = {n: s for n, s in findings.items() if s != "note"}
        if bad:
            raise ValueError(f"review carries non-note findings {bad}; "
                             "only a notes-only round clears the bytes")
        validate_disposition(root, review_rel, disposition_rel, findings)
    return commit, verdict


def review_binds(root: pathlib.Path, pkg: Package, review_rel: str) -> None:
    """The raw names this package and, when one is declared, its subject digest."""
    review = (root / review_rel).read_text(encoding="utf-8")
    if pkg.key not in review:
        raise ValueError(f"review raw does not name the package `{pkg.key}`")
    if pkg.subject is None:
        return
    head = [line for line in review.splitlines() if line.strip()][:4]
    digests = [m.group(1) for line in head if (m := MANIFEST_DIGEST_RE.fullmatch(line))]
    subject = root / pkg.subject
    if not subject.is_file():
        raise ValueError(f"reviewed subject {pkg.subject.as_posix()} is missing")
    actual = beh.digest(pkg.subject_bytes(root) if pkg.subject_bytes else subject.read_bytes())
    if digests != [actual]:
        raise ValueError(f"review head digest is not the sha256 of the reviewed subject "
                         f"{pkg.subject.as_posix()}")


def verify_reviewed(root: pathlib.Path, pkg: Package, review_rel: str,
                    disposition_rel: str | None) -> tuple[str, str]:
    """Every check that binds the bytes on disk to the review; writes nothing."""
    commit, verdict = validate_review(root, review_rel, disposition_rel)
    review_binds(root, pkg, review_rel)
    package_unchanged(root, pkg, commit, disposition_rel)
    return commit, verdict


def _git(root: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)


def package_unchanged(root: pathlib.Path, pkg: Package, commit: str,
                      disposition_rel: str | None) -> None:
    if _git(root, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0:
        raise ValueError(f"reviewed commit {commit[:12]} is not in this repository; fetch "
                         "it (a rebase-merged review commit stays on its pull request's ref)")
    directories = [d.as_posix() for d in (pkg.candidate, *pkg.also)]
    changed = _git(root, "diff", "--name-only", commit, "--", *directories).stdout.split()
    changed += _git(root, "ls-files", "--others", "--exclude-standard",
                    "--", *directories).stdout.split()
    candidate = pkg.candidate.as_posix() + "/"
    subject = [c for c in changed
               if not (c.startswith(candidate) and SIBLING_RECORD_RE.search(c))
               and c != disposition_rel]
    if subject:
        raise ValueError(f"package bytes changed since the commit the review read: "
                         f"{sorted(set(subject))}")


# --- records ----------------------------------------------------------------

DIRECTION_NOTE = (
    "Signed under `" + DIRECTION_REL.as_posix() + "`: the owner's selection of "
    "an option naming this package and version is the sign-off; no phrase or "
    "digest argument exists.")


def options_line(pkg: Package, options: frozenset[str]) -> str:
    """The record's options line; empty for a package that declares none."""
    if not pkg.options:
        return ""
    return f"Options: {', '.join(sorted(options)) or 'none'}\n\n"


def render_record(pkg: Package, version: str, date: str, quote: str, review: str,
                  commit: str, verdict: str, disposition: str | None,
                  options: frozenset[str] = frozenset()) -> str:
    return f"""# {pkg.title} — version-tagged sign-off v{version}

Date: {date}

Owner: Tzeusy

Package: {pkg.key}

Version: {version}

Tag: {tag_for(pkg, version)}

Kind: {pkg.kind}

Owner selection: {quote}

Review: {review}

Reviewed commit: {commit}

Review verdict: {verdict}

Disposition: {disposition or "none"}

{options_line(pkg, options)}{DIRECTION_NOTE}

## What this records

The owner signed off version {version} of `{pkg.candidate.as_posix()}` by the
selection quoted above. The review named above read the package bytes this
sign-off applies; the recorder confirmed that the package directory still
equals the package at the reviewed commit (disposition records excepted) and
that the package's own builder check passed before its patches were applied
through the builder.

The binding is the annotated tag `{tag_for(pkg, version)}` on the commit that
carries this record and the applied result. A later edit to the package is a
new version signed separately; it does not retire this one.

## What this does not do

It authorizes no implementation of the signed semantics, widens no consent,
read, write or egress, and approves no registry or policy byte. Every
exclusion of the acts in force stands.
"""


def render_aggregate(pkg: Package, version: str, date: str, review: str,
                     verdict: str, disposition: str | None) -> str:
    start, end = block_markers(pkg, version)
    review_row = f"`{review}`: `{verdict}`"
    if disposition:
        review_row += f"; disposition: `{disposition}`"
    return f"""{start}
## Versioned sign-off — {pkg.key} — v{version} — recorded {date}

The owner signed off version {version} by selecting an option in the
Claude Code CLI (quoted in the dedicated record).

| | |
|---|---|
| Project / owner | `project:syzygy` / Tzeusy |
| Kind | {pkg.kind} |
| Review outcome | {review_row} |
| Recording | `{record_rel(pkg, version).as_posix()}`; annotated tag `{tag_for(pkg, version)}` on the commit carrying these records and the applied result |
| Direction | `{DIRECTION_REL.as_posix()}` |

This sign-off authorizes no implementation, widens no consent, read, write or
egress, and a later version of the package is signed separately.
{end}
"""


def aggregate_text(root: pathlib.Path) -> str:
    return (root / AGGREGATE_REL).read_text(encoding="utf-8")


def aggregate_copies(root: pathlib.Path, pkg: Package, version: str) -> int:
    start, _end = block_markers(pkg, version)
    return aggregate_text(root).count(start)


def parse_record(text: str) -> dict[str, str]:
    fields = {}
    for key in ("Date", "Owner selection", "Review", "Reviewed commit",
                "Review verdict", "Disposition"):
        m = re.search(rf"^{re.escape(key)}: (.+)$", text, re.MULTILINE)
        if not m:
            raise ValueError(f"record carries no `{key}:` line")
        fields[key] = m.group(1)
    return fields


# --- commands ---------------------------------------------------------------

def parse_options(pkg: Package, text: str) -> frozenset[str]:
    if not pkg.options:
        return frozenset()
    m = re.search(r"^Options: (.+)$", text, re.MULTILINE)
    if not m:
        raise ValueError("record carries no `Options:` line")
    return frozenset() if m.group(1) == "none" else frozenset(m.group(1).split(", "))


def record(root: pathlib.Path, pkg: Package, version: str, date: str, quote: str,
           review_rel: str, disposition_rel: str | None,
           options: frozenset[str] = frozenset()) -> int:
    try:
        validate_inputs(version, date, quote)
        unknown = sorted(set(options) - set(pkg.options))
        if unknown:
            raise ValueError(f"options {unknown} are not this package's; "
                             f"it offers {list(pkg.options) or 'none'}")
        if (root / record_rel(pkg, version)).exists():
            raise ValueError(f"sign-off already recorded: {record_rel(pkg, version).as_posix()}")
        if aggregate_copies(root, pkg, version):
            raise ValueError("the aggregate record already carries this version's block")
        commit, verdict = verify_reviewed(root, pkg, review_rel, disposition_rel)
        findings = pkg.check(root)
        if findings:
            raise ValueError("package does not verify: " + " | ".join(findings))
    except (ValueError, OSError) as exc:
        print(f"FAILED (before applying anything): {exc}")
        return 1
    code = pkg.apply_with(root, options) if pkg.apply_with else pkg.apply(root)
    if code != 0:
        print(f"FAILED: the builder's apply returned {code}; nothing recorded")
        return 1
    if not pkg.applied(root):
        print("FAILED after apply: the tree does not carry the applied package; "
              "restore it with git checkout before retrying")
        return 1
    disposition = disposition_rel if verdict == "CONFIRM WITH EXCEPTIONS" else None
    (root / record_rel(pkg, version)).write_text(
        render_record(pkg, version, date, quote, review_rel, commit, verdict, disposition,
                      options),
        encoding="utf-8")
    block = render_aggregate(pkg, version, date, review_rel, verdict, disposition)
    aggregate = root / AGGREGATE_REL
    body = aggregate.read_text(encoding="utf-8")
    aggregate.write_text(body.rstrip("\n") + "\n\n" + block, encoding="utf-8")
    print(f"wrote {record_rel(pkg, version).as_posix()}")
    print(f"appended the {pkg.key} v{version} block to {AGGREGATE_REL.as_posix()}")
    print(f"next: git add the applied subjects and both records, commit, then "
          f"`git tag -a {tag_for(pkg, version)}` on that commit and push the tag")
    return 0


def check(root: pathlib.Path, pkg: Package, version: str) -> int:
    if not VERSION_RE.fullmatch(version):
        print(f"FAILED: version {version!r} is not major.minor")
        return 1
    rec = root / record_rel(pkg, version)
    copies = aggregate_copies(root, pkg, version)
    if not rec.exists() and not copies:
        print(f"{pkg.key} v{version}: not performed")
        return 0
    try:
        if not rec.exists() or copies != 1:
            raise ValueError(f"partial record: record exists={rec.exists()}, "
                             f"aggregate copies={copies}")
        text = rec.read_text(encoding="utf-8")
        f = parse_record(text)
        disposition = None if f["Disposition"] == "none" else f["Disposition"]
        commit, verdict = validate_review(root, f["Review"], disposition)
        if (commit, verdict) != (f["Reviewed commit"], f["Review verdict"]):
            raise ValueError("record's reviewed commit or verdict differs from the review")
        if text != render_record(pkg, version, f["Date"], f["Owner selection"], f["Review"],
                                 commit, verdict, disposition, parse_options(pkg, text)):
            raise ValueError("dedicated record differs from its regeneration")
        block = render_aggregate(pkg, version, f["Date"], f["Review"], verdict, disposition)
        if aggregate_text(root).count(block) != 1:
            raise ValueError("aggregate block differs from its regeneration")
        versions = recorded_versions(root, pkg)
        latest = versions[-1] == tuple(int(x) for x in version.split("."))
        if latest and not pkg.applied(root):
            raise ValueError("the latest signed version is not applied to the tree")
        if latest and pkg.applied_options and (
                pkg.applied_options(root) != parse_options(pkg, text)):
            raise ValueError(f"the tree carries options {sorted(pkg.applied_options(root))}, "
                             f"the record names {sorted(parse_options(pkg, text))}")
    except (ValueError, OSError) as exc:
        print(f"FAILED: {exc}")
        return 1
    print(f"recorded {pkg.key} v{version} sign-off regenerates exactly"
          + ("; applied tree verified" if latest else "; superseded by a later version"))
    return 0


# --- selftest ---------------------------------------------------------------

STUB_REVIEW = "docs/reviews/R-STUB-RAW.md"
STUB_DISPOSITION = "pkg/stub/ROUND-1-DISPOSITIONS.md"
STUB_DIR = pathlib.Path("pkg/stub")


STUB_ALSO = pathlib.Path("spec/stub")


def stub_package() -> Package:
    def check_fn(root):
        return ["stub builder failure"] if (root / STUB_DIR / "BROKEN").exists() else []

    def apply_fn(root):
        (root / "applied.txt").write_text("applied\n")
        return 0

    return Package("stub-package", "Stub package", "behavior amendment", STUB_DIR,
                   "STUB", check_fn, apply_fn, lambda root: (root / "applied.txt").exists(),
                   also=(STUB_ALSO,), subject=STUB_ALSO / "spec.md")


STUB_SUBJECT_BYTES = b"specification bytes\n"


def stub_review(commit: str, verdict: str = "CONFIRM", findings: str = "No findings.",
                extra_head: str = "") -> str:
    return (f"# Review — stub-package\nReviewed commit: {commit}\n"
            f"Manifest SHA-256: {beh.digest(STUB_SUBJECT_BYTES)}\nVerdict: {verdict}\n{extra_head}\n"
            f"## Findings\n\n{findings}\n")


NOTES = ("**Finding 1 — first** (note) evidence\n\n"
         "**Finding 2 — second** (note) evidence\n")


def stub_disposition(review: str = STUB_REVIEW, numbers=(1, 2)) -> str:
    body = "".join(f"### {n} — note\n\nLeft.\n\n" for n in numbers)
    return f"Reviewed record: {review}\n\n{body}"


def make_fixture(tmp: pathlib.Path, review_text=None, disposition_text=None,
                 aggregate: str = "# Record\n",
                 package_files: dict | None = None) -> tuple[pathlib.Path, str]:
    def run(*args):
        subprocess.run(["git", "-C", str(tmp), "-c", "user.email=t@t", "-c", "user.name=t",
                        *args], check=True, capture_output=True)
    run("init", "-q")
    (tmp / STUB_DIR).mkdir(parents=True)
    (tmp / STUB_DIR / "manifest.txt").write_text("package bytes\n")
    (tmp / STUB_ALSO).mkdir(parents=True)
    (tmp / STUB_ALSO / "spec.md").write_bytes(STUB_SUBJECT_BYTES)
    (tmp / STUB_ALSO / "proposal.md").write_text("proposal bytes\n")
    for name, body in (package_files or {}).items():
        (tmp / STUB_DIR / name).write_text(body)
    (tmp / AGGREGATE_REL).parent.mkdir(parents=True)
    (tmp / AGGREGATE_REL).write_text(aggregate)
    run("add", "-A")
    run("commit", "-qm", "package")
    commit = subprocess.run(["git", "-C", str(tmp), "rev-parse", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    (tmp / "docs/reviews").mkdir(parents=True)
    (tmp / STUB_REVIEW).write_text(
        review_text(commit) if callable(review_text) else (review_text or stub_review(commit)))
    if disposition_text is not None:
        (tmp / STUB_DISPOSITION).write_text(disposition_text)
    run("add", "-A")
    run("commit", "-qm", "review")
    return tmp, commit


def selftest() -> int:
    pkg = stub_package()
    results: list[tuple[str, bool]] = []
    args = dict(version="1.0", date="2026-10-02", quote='Selected "Sign off" on the stub question',
                review_rel=STUB_REVIEW, disposition_rel=None)

    def run_record(tmp, **override):
        merged = {**args, **override}
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = record(tmp, pkg, merged["version"], merged["date"], merged["quote"],
                          merged["review_rel"], merged["disposition_rel"])
        return code, out.getvalue()

    def run_check(tmp, version):
        import io
        import contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            return check(tmp, pkg, version)

    def refused(name, *, review=None, disposition=None, mutate=None, expect=None, **override):
        with tempfile.TemporaryDirectory() as t:
            tmp, commit = make_fixture(pathlib.Path(t), review, disposition)
            if mutate:
                mutate(tmp, commit)
            code, out = run_record(tmp, **override)
            clean = not (tmp / "applied.txt").exists() and not (tmp / record_rel(pkg, "1.0")).exists()
            results.append((f"refused: {name}",
                            code == 1 and clean and (expect is None or expect in out)))

    # the happy paths, and --check over them
    with tempfile.TemporaryDirectory() as t:
        tmp, commit = make_fixture(pathlib.Path(t))
        code, _ = run_record(tmp)
        rec = tmp / record_rel(pkg, "1.0")
        results.append(("CONFIRM records, applies and writes both records",
                        code == 0 and rec.exists() and (tmp / "applied.txt").exists()
                        and aggregate_copies(tmp, pkg, "1.0") == 1))
        results.append(("check passes over a fresh record", run_check(tmp, "1.0") == 0))
        results.append(("check reports not performed for an unrecorded version",
                        run_check(tmp, "9.9") == 0))
        code2, out2 = run_record(tmp)
        results.append(("refused: version already recorded",
                        code2 == 1 and "already recorded" in out2))
        code3, _ = run_record(tmp, version="1.1")
        results.append(("a second version records beside the first", code3 == 0))
        results.append(("check on the superseded version passes",
                        run_check(tmp, "1.0") == 0 and run_check(tmp, "1.1") == 0))
        original = rec.read_text()
        rec.write_text(original.replace("Stub package", "Edited package", 1))
        results.append(("check fails on an edited record", run_check(tmp, "1.0") == 1))
        rec.write_text(original)
        agg = (tmp / AGGREGATE_REL).read_text()
        (tmp / AGGREGATE_REL).write_text(agg.replace("recorded 2026-10-02", "recorded 2026-10-03", 1))
        results.append(("check fails on an edited aggregate block", run_check(tmp, "1.0") == 1))
        start, end = block_markers(pkg, "1.0")
        block = agg[agg.index(start):agg.index(end) + len(end) + 1]
        (tmp / AGGREGATE_REL).write_text(agg + "\n" + block)
        results.append(("check fails on a duplicated aggregate block", run_check(tmp, "1.0") == 1))
        (tmp / AGGREGATE_REL).write_text(agg)
        (tmp / record_rel(pkg, "1.1")).unlink()
        results.append(("check fails on a partial record (aggregate without dedicated)",
                        run_check(tmp, "1.1") == 1))
        (tmp / "applied.txt").unlink()
        results.append(("check fails when the latest version is not applied",
                        run_check(tmp, "1.0") == 1))

    with tempfile.TemporaryDirectory() as t:
        # A row a later performed sign-off re-patched is history; any other
        # drift still fails.
        root = pathlib.Path(t)
        later_record, later_manifest = next(iter(beh.VERSIONED_LATER.values()))
        own = pathlib.Path("own-manifest.txt")
        target = "subject.md"
        (root / target).write_text("v2\n")
        sha_old, sha_new = beh.digest(b"v1\n"), beh.digest(b"v2\n")
        (root / own).write_text(f"{sha_old}  {target}\n")
        results.append(("applied: a row the tree no longer hashes to fails with no later source",
                        not _rows_hash_tree(root, own)))
        (root / later_record).parent.mkdir(parents=True, exist_ok=True)
        (root / later_record).write_text("record\n")
        (root / later_manifest).parent.mkdir(parents=True, exist_ok=True)
        (root / later_manifest).write_text(f"{sha_new}  {target}\n")
        results.append(("applied: a row a later performed sign-off re-patched is history",
                        _rows_hash_tree(root, own)))
        (root / later_manifest).write_text(f"{beh.digest(b'other')}  {target}\n")
        results.append(("applied: a later manifest digest the tree does not hash to still fails",
                        not _rows_hash_tree(root, own)))

    with tempfile.TemporaryDirectory() as t:
        tmp, commit = make_fixture(pathlib.Path(t), lambda c: stub_review(
            c, "CONFIRM WITH EXCEPTIONS", NOTES), stub_disposition())
        code, _ = run_record(tmp, disposition_rel=STUB_DISPOSITION)
        results.append(("CONFIRM WITH EXCEPTIONS, notes only and dispositioned, records",
                        code == 0 and run_check(tmp, "1.0") == 0))
        results.append(("the disposition record is not package bytes",
                        "Disposition: " + STUB_DISPOSITION in (tmp / record_rel(pkg, "1.0")).read_text()))

    for bad in ("1", "1.0.0", "v1.0", "01.0", "1.00", "1.x", ""):
        refused(f"version {bad!r}", version=bad, expect="major.minor")
    refused("bad date", date="2026-1-2", expect="YYYY-MM-DD")
    refused("empty selection quote", quote="  ", expect="one non-empty line")
    refused("multi-line selection quote", quote="a\nb", expect="one non-empty line")
    refused("selection quote carrying a digest", quote="Sign " + "ab" * 32, expect="digest")
    refused("REVISE verdict", review=lambda c: stub_review(c, "REVISE"), expect="not CONFIRM")
    refused("free-form verdict", review=lambda c: stub_review(c, "APPROVED"), expect="not CONFIRM")
    refused("two verdict lines in the head",
            review=lambda c: f"Reviewed commit: {c}\nManifest SHA-256: {'ab' * 32}\n"
                             f"Verdict: CONFIRM\nVerdict: CONFIRM\n", expect="exactly one `Verdict:`")
    refused("head without a reviewed commit",
            review="# R\nManifest SHA-256: " + "ab" * 32 + "\nVerdict: CONFIRM\n", expect="Reviewed commit")
    refused("head without a manifest line",
            review=lambda c: f"# R\nReviewed commit: {c}\nVerdict: CONFIRM\n", expect="Manifest SHA-256")
    refused("verdict pushed past the four-line head",
            review=lambda c: f"# R\nReviewed commit: {c}\n\nManifest SHA-256: {'ab' * 32}\n"
                             f"\nsome line\nVerdict: CONFIRM\n", expect="exactly one `Verdict:`")
    refused("missing review raw", review_rel="docs/reviews/none-RAW.md", expect="missing review raw")
    refused("reviewed commit unknown to the repository",
            review=lambda c: stub_review("1" * 40), expect="not in this repository")
    revise_findings = "**Finding 1 — first** (revise) evidence\n"
    refused("a revise-severity finding under CONFIRM WITH EXCEPTIONS",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS", revise_findings),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="non-note")
    refused("a blocking finding under CONFIRM WITH EXCEPTIONS",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS",
                                         "**Finding 1 — first** (blocking) evidence\n"),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="non-note")
    refused("an ASCII-hyphen revise finding under CONFIRM WITH EXCEPTIONS",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS",
                                         "**Finding 1 - first** (revise) evidence\n"),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="non-note")
    for qualified in ("(note, for the owner's view)", "(note, for the owner)",
                      "(note: reported for the owner, not resolved)"):
        with tempfile.TemporaryDirectory() as t:
            tmp, commit = make_fixture(pathlib.Path(t), lambda c, q=qualified: stub_review(
                c, "CONFIRM WITH EXCEPTIONS",
                f"**Finding 1 — first** {q} evidence\n\n**Finding 2 — second** (note) evidence\n"),
                stub_disposition())
            code, _ = run_record(tmp, disposition_rel=STUB_DISPOSITION)
            results.append((f"a qualified note {qualified} reads as a note and records",
                            code == 0 and run_check(tmp, "1.0") == 0))
    for qualified in ("(blocking, for the owner)", "(revise: before sign-off)", "(revise — owner)"):
        refused(f"a qualified non-note {qualified} stays non-note",
                review=lambda c, q=qualified: stub_review(c, "CONFIRM WITH EXCEPTIONS",
                                                          f"**Finding 1 — first** {q} evidence\n"),
                disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
                expect="non-note")
    for qualified in ("(note, editorial)", "(note: not resolved)",
                      "(note, for the owner\u2019s view)"):
        with tempfile.TemporaryDirectory() as t:
            tmp, commit = make_fixture(pathlib.Path(t), lambda c, q=qualified: stub_review(
                c, "CONFIRM WITH EXCEPTIONS",
                f"**Finding 1 — first** {q} evidence\n\n**Finding 2 — second** (note) evidence\n"),
                stub_disposition())
            code, _ = run_record(tmp, disposition_rel=STUB_DISPOSITION)
            results.append((f"an allowed qualifier {qualified} records", code == 0))
    for qualified in ("(note_blocking)", "(note, blocker)", "(note, revises the clause)",
                      "(note, REVISE)", "(note, Blocking)", "(note, non-blocking)",
                      "(note — for the owner)", "(note for the owner)",
                      "(note, for the owner, blocking)"):
        refused(f"a note qualifier outside the allow-list {qualified} is ambiguous",
                review=lambda c, q=qualified: stub_review(c, "CONFIRM WITH EXCEPTIONS",
                                                          f"**Finding 1 — first** {q} evidence\n"),
                disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
                expect="ambiguous")
    refused("a note whose qualifier names a stronger severity",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS",
                                         "**Finding 1 — first** (note, but revise-level) evidence\n"),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="ambiguous")
    refused("a severity word run into another word",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS",
                                         "**Finding 1 — first** (notes) evidence\n"),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="no (blocking|revise|note) severity")
    refused("a finding with no severity",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS", "**Finding 1 — first** evidence\n"),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="no (blocking|revise|note) severity")
    refused("CONFIRM WITH EXCEPTIONS with no countable finding",
            review=lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS", "No findings.\n"),
            disposition=stub_disposition(numbers=(1,)), disposition_rel=STUB_DISPOSITION,
            expect="no countable finding")
    cwe = lambda c: stub_review(c, "CONFIRM WITH EXCEPTIONS", NOTES)  # noqa: E731
    refused("CONFIRM WITH EXCEPTIONS without --disposition", review=cwe, expect="needs --disposition")
    refused("CONFIRM WITH EXCEPTIONS with a missing disposition file", review=cwe,
            disposition_rel="pkg/stub/ROUND-9-DISPOSITIONS.md", expect="missing disposition record")
    refused("disposition missing a finding", review=cwe, disposition=stub_disposition(numbers=(1,)),
            disposition_rel=STUB_DISPOSITION, expect="do not match")
    refused("disposition with an extra finding", review=cwe,
            disposition=stub_disposition(numbers=(1, 2, 3)), disposition_rel=STUB_DISPOSITION,
            expect="do not match")
    refused("disposition naming another raw", review=cwe,
            disposition=stub_disposition(review="docs/reviews/other-RAW.md"),
            disposition_rel=STUB_DISPOSITION, expect="does not name the reviewed raw")

    def edit_package(tmp, commit):
        (tmp / STUB_DIR / "manifest.txt").write_text("edited after the review\n")

    def add_package_file(tmp, commit):
        (tmp / STUB_DIR / "new.txt").write_text("new\n")

    def edit_also(tmp, commit):
        (tmp / STUB_ALSO / "proposal.md").write_text("edited after the review\n")

    def add_also_file(tmp, commit):
        (tmp / STUB_ALSO / "new.md").write_text("untracked\n")

    def add_also_sibling(tmp, commit):
        (tmp / STUB_ALSO / "ROUND-9-DISPOSITIONS.md").write_text("not a candidate record\n")

    def edit_subject(tmp, commit):
        (tmp / STUB_ALSO / "spec.md").write_text("edited after the review\n")

    refused("a file added to a declared further directory", mutate=add_also_file,
            expect="package bytes changed")
    refused("a sibling-named record inside a further directory is package bytes",
            mutate=add_also_sibling, expect="package bytes changed")
    refused("the reviewed subject edited after the review", mutate=edit_subject,
            expect="head digest is not the sha256")
    refused("a head digest that is not the subject's",
            review=lambda c: stub_review(c).replace(beh.digest(STUB_SUBJECT_BYTES), "f" * 64),
            expect="head digest is not the sha256")
    refused("a raw that does not name the package",
            review=lambda c: stub_review(c).replace("stub-package", "other-package"),
            expect="does not name the package")
    refused("the reviewed subject missing",
            mutate=lambda tmp, commit: (tmp / STUB_ALSO / "spec.md").unlink(),
            expect="reviewed subject " + (STUB_ALSO / "spec.md").as_posix() + " is missing")
    real = real_packages()["polaris-dossier-local-agent-mode"]
    results.append(("the real dossier package binds its builder's proposed spec as the subject",
                    real.subject is not None
                    and real.subject == _module("build_polaris_dossier_local_agent_mode").PROPOSED_SPEC))

    # Versioned entries, options and a computed subject (dossier v1.1).
    import contextlib
    import dataclasses
    import io
    packages = real_packages()
    results.append(("package_for selects a key@version entry and falls back to the key",
                    package_for(packages, "polaris-dossier-local-agent-mode", "1.1")
                    is packages["polaris-dossier-local-agent-mode@1.1"]
                    and package_for(packages, "polaris-dossier-local-agent-mode", "1.0")
                    is packages["polaris-dossier-local-agent-mode"]))
    real11 = packages["polaris-dossier-local-agent-mode@1.1"]
    v11 = _module("build_polaris_dossier_local_agent_mode_v1_1")
    results.append(("the real v1.1 entry shares v1.0's key and record stem, binds the computed "
                    "subject and offers n6",
                    real11.key == real.key and real11.record_stem == real.record_stem
                    and real11.subject == v11.SPEC and real11.subject_bytes is not None
                    and real11.options == tuple(v11.OPTIONS) and real11.apply_with is not None
                    and real11.applied_options is not None))
    taken: list[frozenset[str]] = []

    def apply_with(root, options):
        taken.append(options)
        (root / "applied.txt").write_text(f"applied {sorted(options)}\n")
        return 0

    def applied_options(root):
        text = (root / "applied.txt").read_text()
        return frozenset(["n6"]) if "n6" in text else frozenset()

    optioned = dataclasses.replace(pkg, options=("n6",), apply_with=apply_with,
                                   applied_options=applied_options)

    def run(package, tmp, *, options=frozenset(), version="1.0"):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            code = record(tmp, package, version, args["date"], args["quote"], STUB_REVIEW,
                          None, options)
        return code, out.getvalue()

    def checked(package, tmp, version="1.0"):
        with contextlib.redirect_stdout(io.StringIO()):
            return check(tmp, package, version)

    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, _ = run(optioned, tmp, options=frozenset({"n6"}))
        rec = tmp / record_rel(optioned, "1.0")
        results.append(("an option taken is applied and named in the record",
                        code == 0 and taken[-1] == frozenset({"n6"})
                        and "\nOptions: n6\n" in rec.read_text()
                        and checked(optioned, tmp) == 0))
        rec.write_text(rec.read_text().replace("Options: n6", "Options: none"))
        results.append(("an edited options line fails --check", checked(optioned, tmp) == 1))
    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, _ = run(optioned, tmp)
        results.append(("no option taken: the record says none",
                        code == 0 and taken[-1] == frozenset()
                        and "\nOptions: none\n" in (tmp / record_rel(optioned, "1.0")).read_text()))
    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, out = run(optioned, tmp, options=frozenset({"n7"}))
        results.append(("refused: an option the package does not offer",
                        code == 1 and "not this package's" in out and not (tmp / "applied.txt").exists()))
    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, out = run(pkg, tmp, options=frozenset({"n6"}))
        results.append(("refused: an option for a package that offers none",
                        code == 1 and "offers none" in out))
    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, _ = run(pkg, tmp)
        results.append(("a package without options writes no options line",
                        code == 0 and "Options:" not in (tmp / record_rel(pkg, "1.0")).read_text()))
    # The subject file holds other bytes than the reviewed ones (the installed
    # predecessor); only the computed bytes match the review head.
    on_disk = dataclasses.replace(pkg, subject=STUB_DIR / "manifest.txt")
    computed = dataclasses.replace(on_disk, subject_bytes=lambda root: STUB_SUBJECT_BYTES)
    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, _ = run(computed, tmp)
        results.append(("a computed subject equal to the reviewed bytes records", code == 0))
    with tempfile.TemporaryDirectory() as t:
        tmp, _commit = make_fixture(pathlib.Path(t))
        code, out = run(on_disk, tmp)
        results.append(("refused: the same subject hashed from disk, not computed",
                        code == 1 and "head digest is not the sha256" in out))
    with tempfile.TemporaryDirectory() as t:
        tmp, commit = make_fixture(pathlib.Path(t))
        wrong = dataclasses.replace(pkg, subject_bytes=lambda root: b"other bytes\n")
        code, out = run(wrong, tmp)
        results.append(("refused: a computed subject that is not the reviewed bytes",
                        code == 1 and "head digest is not the sha256" in out
                        and not (tmp / "applied.txt").exists()))

    refused("package edited after the review", mutate=edit_package, expect="package bytes changed")
    refused("a declared further directory edited after the review", mutate=edit_also,
            expect="package bytes changed")
    refused("a package file added after the review", mutate=add_package_file,
            expect="package bytes changed")
    with tempfile.TemporaryDirectory() as t:
        tmp, commit = make_fixture(pathlib.Path(t), package_files={"BROKEN": "x\n"})
        code, out = run_record(tmp)
        results.append(("refused: builder check failing, before anything is applied",
                        code == 1 and "does not verify" in out
                        and not (tmp / "applied.txt").exists()))
    with tempfile.TemporaryDirectory() as t:
        tmp, commit = make_fixture(pathlib.Path(t), None, stub_disposition())
        (tmp / STUB_DISPOSITION).write_text(stub_disposition() + "edited note\n")
        code, _ = run_record(tmp)
        results.append(("an edited sibling disposition record is not package bytes", code == 0))

    failing = 0
    for name, ok in results:
        failing += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"{len(results)} fixtures, {failing} failing")
    return 0 if failing == 0 else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--record", metavar="PACKAGE")
    mode.add_argument("--check", metavar="PACKAGE")
    mode.add_argument("--selftest", action="store_true")
    parser.add_argument("--version")
    parser.add_argument("--date")
    parser.add_argument("--review", help="the retained raw review, repo-relative")
    parser.add_argument("--disposition", help="the record beside the package (notes-only)")
    parser.add_argument("--owner-selection-quote", dest="quote")
    parser.add_argument("--option", action="append", default=[],
                        help="an option the owner took (repeatable; the package declares them)")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    packages = real_packages()
    key = args.record or args.check
    if key not in packages:
        print(f"unknown package {key!r}; covered: {sorted(k for k in packages if '@' not in k)}")
        return 2
    if not args.version:
        parser.error("--version is required")
    pkg = package_for(packages, key, args.version)
    if args.check:
        return check(ROOT, pkg, args.version)
    for needed in ("date", "review", "quote"):
        if not getattr(args, needed):
            parser.error(f"--{ 'owner-selection-quote' if needed == 'quote' else needed} "
                         "is required with --record")
    return record(ROOT, pkg, args.version, args.date, args.quote,
                  args.review, args.disposition, frozenset(args.option))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
