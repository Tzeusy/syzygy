#!/usr/bin/env python3
"""Perform the install change that follows the Redis sitting's act records.

Candidate tooling. It performs no owner act and writes no act record; it makes
the repository's checks agree with acts the recorders have already written.
`scripts/simulate_redis_sitting.py` runs it in a scratch clone and requires the
end state to be green; the runbook (`docs/polaris-generation/REDIS-SITTING-RUNBOOK.md`)
lists each step with the finding it answers.

Run from the repository root after every recorder has run:

  python3 scripts/install_redis_sitting.py            # install
  python3 scripts/install_redis_sitting.py --check    # report what is not installed
  python3 scripts/install_redis_sitting.py --selftest

It refuses (exit 2, nothing written) unless every required act record exists.
It is idempotent: a second run changes nothing and says so. Each step asserts
that the text it patches carries its anchor exactly once, so a drifted
`check_governance.py` fails loudly instead of being patched in the wrong place.

Steps (finding numbers are the runbook's):

  registrations   F5   performed admission and registry records become registered
                       act-copy files; their `manifest SHA-256:` heading is a
                       checked exemption
  rfc5            F6   the RFC-0005 patch applies to both mirrors; the active
                       manifest row and the directive register are regenerated;
                       the amendment becomes a row-argument contract chain link
  policy          F4,F10  the screening-scope act becomes the policy's chain link (the
                       2026-10-02 re-pin turns to history); when the version-2 act
                       exists it is the final link and version 1 turns to history
                       too; the read gate, its tests and the status battery and
                       workflow follow the final act, once (an act pair recorded
                       in the wrong order is refused)
  profile         F8,F11  the narrative-profile spec moves from proposed/ to
                       specs/; package prose naming the old path is rewritten;
                       the status page figure follows the recount tool (both
                       figures, once the dossier addition is signed off) and
                       its lead-in names the profile and its adoption record;
                       the openspec/README.md row names the record
  reconcile       B3   `check_spec_reconciliation.py --regenerate`: the census
                       and each installed addition's generated union
"""
from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECISIONS = ".syzygy/governance/decisions"
CAND = ".syzygy/governance/contracts/candidates"
CG = "scripts/check_governance.py"

#: Act records every sitting must have produced before this runs. The provider
#: route is one of two substitutes (RFC4-1): exactly one of ROUTE_A and ROUTE_B.
REQUIRED_RECORDS = (
    f"{DECISIONS}/PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md",
    f"{DECISIONS}/PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md",
    f"{DECISIONS}/PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-ACT.md",
    f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md",
    f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md",
    f"{DECISIONS}/POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md",
)
ROUTE_A = ("PUBLIC_REGISTRY_ACTS[0][0]", "PUBLIC-ADMISSION-REGISTRY-PROVIDER-ROUTE-ACT.md", "PUBLIC_REGISTRY_MANIFEST")
ROUTE_B = ("MESSAGES_API_ACTS[0][0]", "PUBLIC-ADMISSION-REGISTRY-MESSAGES-API-ROUTE-ACT.md", "MESSAGES_API_MANIFEST")

#: (label expression, record file, manifest constant) for the records that become
#: registered act-copy files; the provider route is added by `performed()`.
PERFORMED_COMMON = (
    ("PUBLIC_ADMISSION_ACTS[0][0]", "PUBLIC-REPO-ADMISSION-REQUESTS-OBSERVATION-ACT.md", "PUBLIC_ADMISSION_MANIFEST"),
    ("PUBLIC_ADMISSION_ACTS[1][0]", "PUBLIC-REPO-ADMISSION-REDIS-OBSERVATION-ACT.md", "PUBLIC_ADMISSION_MANIFEST"),
    ("PUBLIC_REGISTRY_ACTS[1][0]", "PUBLIC-ADMISSION-REGISTRY-GIT-SOURCE-ACT.md", "PUBLIC_REGISTRY_MANIFEST"),
)


#: The egress consent is one of two versions; the sitting offers version 2 in place of version 1
#: (packet row 8 against row 6), so version 1 may stay unperformed. At least one must exist, and each
#: that exists is registered.
EGRESS_V1 = ("PUBLIC_ADMISSION_ACTS[2][0]", "PUBLIC-REPO-ADMISSION-EGRESS-ANTHROPIC-ACT.md", "PUBLIC_ADMISSION_MANIFEST")
EGRESS_V2 = ("PUBLIC_EGRESS_V2_ACTS[0][0]", "PUBLIC-EGRESS-V2-ANTHROPIC-ACT.md", "PUBLIC_EGRESS_V2_MANIFEST")


def egress_records(root: pathlib.Path) -> list[tuple[str, str, str]]:
    return [e for e in (EGRESS_V1, EGRESS_V2) if (root / DECISIONS / e[1]).is_file()]


def provider_routes(root: pathlib.Path) -> list[tuple[str, str, str]]:
    return [r for r in (ROUTE_A, ROUTE_B) if (root / DECISIONS / r[1]).is_file()]


def performed(root: pathlib.Path) -> tuple[tuple[str, str, str], ...]:
    routes = provider_routes(root)
    if len(routes) != 1:
        raise Refusal(f"exactly one provider route record must exist (the two routes are substitutes, "
                      f"RFC4-1); found {[r[1] for r in routes]}")
    egress = egress_records(root)
    if not egress:
        raise Refusal("no egress consent record exists (version 2, or version 1)")
    return PERFORMED_COMMON + (routes[0],) + tuple(egress)


RFC5_PKG = f"{CAND}/rfc5-project-documentation-class"
RFC5_MODULE = "rfcs/RFC-0005/consent-egress-secrets.md"
BUDGET_SCRIPT = f"{CAND}/scripts/build_budget_report.py"
BUDGET_REPORT = f"{CAND}/CONTEXT-BUDGET-REPORT.md"
RFC5_ACT = f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md"
SCOPE_PKG = f"{CAND}/public-source-screening-scope"
SCOPE_MANIFEST = f"{SCOPE_PKG}/PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt"
SCOPE_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md"
V2_PKG = f"{CAND}/public-source-screening-scope-v2"
V2_MANIFEST = f"{V2_PKG}/PUBLIC-SOURCE-SCREENING-SCOPE-V2-MANIFEST.txt"
V2_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md"
V1_SCRIPT = "record_public_source_screening_scope_act"
V2_SCRIPT = "record_public_source_screening_scope_v2_act"
REPIN_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md"
AMENDMENT_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md"
POLICY_JSON = ".syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json"
WORKFLOW = ".github/workflows/governance-docs.yml"
INPUTS_TS = "apps/three-surface-poc/src/governance-inputs.ts"
INPUTS_TEST = "apps/three-surface-poc/src/governance-inputs.test.ts"
PIN_FILES = (INPUTS_TS, INPUTS_TEST,
             "packages/three-surface-poc-core/src/git-object-reader.ts",
             "packages/three-surface-poc-core/src/content-classification.test.ts",
             "packages/three-surface-poc-core/src/project-shape-model.test.ts")
PROFILE_CHANGE = "openspec/changes/polaris-non-governed-narrative-profile"
PROFILE_PKG = f"{CAND}/non-governed-narrative-profile"
STATUS = "PROJECT-STATUS.md"

# ---- text of the check_governance.py insertions ----------------------------

REGISTRATIONS_MARK = "_activate_public_admission_performed_registries"
REGISTRATIONS_ANCHOR = "_activate_public_admission_manifest_copy_registry()\n"
EXEMPTION_DICT = "BARE_DIGEST_HEADING_MANIFEST_EXEMPTIONS = {"


def registrations_code(perf) -> str:
    lines = ["", "",
             f"def {REGISTRATIONS_MARK}():",
             '    """Install change: each performed admission or registry record is an act-copy file."""',
             '    aggregate = f"{DECISIONS}/ACCEPTANCE-ACT-RECORD.md"',
             "    for label, rel in ("]
    for label, record, _manifest in perf:
        lines.append(f'            ({label}, f"{{DECISIONS}}/{record}"),')
    lines += ["    ):",
              "        if not os.path.isfile(os.path.join(ROOT, rel)):",
              "            continue",
              "        labels = ACT_DIGEST_COPY_FILES.get(aggregate, ())",
              "        if label not in labels:",
              "            ACT_DIGEST_COPY_FILES[aggregate] = labels + (label,)",
              "        ACT_DIGEST_COPY_FILES[rel] = (label,)",
              "", "", f"{REGISTRATIONS_MARK}()", ""]
    return "\n".join(lines)


def exemptions_code(perf) -> str:
    return "".join(f'    (f"{{DECISIONS}}/{record}", "manifest"): {manifest},\n'
                   for _l, record, manifest in perf)


CHAIN_MARK = "RFC5_CLASS_LABEL"
CHAIN_CONSTANTS = '''#: The RFC5-14 project-documentation amendment (one module). Its act takes the
#: SHA-256 of the patched module, which is the manifest's one row, not the
#: manifest file's digest, so the link is a row-argument link
#: (`ROW_ARGUMENT_LINK_LABELS`): CG-7h reads the argument from the row.
RFC5_CLASS_LABEL = "AMEND RFC5-14 WITH THE PROJECT-DOCUMENTATION CONTENT CLASS"
RFC5_CLASS_DIR = f"{CANDIDATES}/rfc5-project-documentation-class"
RFC5_CLASS_SUBJECT = f"{RFC5_CLASS_DIR}/CONTRACT-AMENDMENT-MANIFEST.txt"
RFC5_CLASS_ACT = f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md"
RFC5_CLASS_MODULE = ".syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md"
RFC5_CLASS_PATHS = ("rfcs/RFC-0005/consent-egress-secrets.md",)
ROW_ARGUMENT_LINK_LABELS = frozenset({RFC5_CLASS_LABEL})
#: The file whose digest is the act argument of a row-argument link: the
#: installed module, which the manifest row hashes in its proposed form.
ROW_ARGUMENT_SUBJECTS = {RFC5_CLASS_LABEL: RFC5_CLASS_MODULE}


def _activate_rfc5_class_act_copy_registry():
    """Require both record copies and the manifest row once the record exists."""
    if not os.path.isfile(os.path.join(ROOT, RFC5_CLASS_ACT)):
        return
    labels = ACT_DIGEST_COPY_FILES.get(PERFORMED_ACT_RECORD, ())
    if RFC5_CLASS_LABEL not in labels:
        ACT_DIGEST_COPY_FILES[PERFORMED_ACT_RECORD] = labels + (RFC5_CLASS_LABEL,)
    ACT_DIGEST_COPY_FILES[RFC5_CLASS_ACT] = (RFC5_CLASS_LABEL,)
    ACT_DIGEST_COPY_FILES[RFC5_CLASS_SUBJECT] = (RFC5_CLASS_LABEL,)


'''
RFC5_EXEMPTION = ('    (f"{DECISIONS}/RFC5-PROJECT-DOCUMENTATION-CLASS-AMENDMENT-ACT.md", '
                  '"manifest file"): RFC5_CLASS_SUBJECT,\n')
CHAIN_EDITS = (
    # (anchor, replacement); every anchor must occur exactly once
    ("CONTRACT_SUCCESSOR_CHAIN = (\n    (POLARIS_NO_SIGNAL_LABEL,",
     CHAIN_CONSTANTS + "CONTRACT_SUCCESSOR_CHAIN = (\n    (POLARIS_NO_SIGNAL_LABEL,"),
    ("     CONTRACT_RESTYLE_PATHS),\n)\nfor _label",
     "     CONTRACT_RESTYLE_PATHS),\n    (RFC5_CLASS_LABEL, RFC5_CLASS_SUBJECT, RFC5_CLASS_ACT,\n"
     "     _activate_rfc5_class_act_copy_registry, RFC5_CLASS_PATHS),\n)\nfor _label"),
    ("    for label, subject, _act, _activate, _paths in CONTRACT_SUCCESSOR_CHAIN:\n        out.append((label, subject,",
     "    for label, subject, _act, _activate, _paths in CONTRACT_SUCCESSOR_CHAIN:\n"
     "        out.append((label, ROW_ARGUMENT_SUBJECTS.get(label, subject),"),
    ("            link_digest = current_digest(subject)\n        else:",
     "            link_digest = current_digest(subject)\n"
     "            if label in ROW_ARGUMENT_LINK_LABELS:\n"
     '                rows_ = re.findall(r"^([0-9a-f]{64})  \\S+$", link_body or "", re.M)\n'
     "                link_digest = rows_[0] if len(rows_) == 1 else None\n        else:"),
    ("        if body_digest != link_digest:",
     "        if label not in ROW_ARGUMENT_LINK_LABELS and body_digest != link_digest:"),
    # the selftest pins the chain's link paths; it gains the RFC5-14 link too
    # (found by the local-agent rehearsal: CG-7h "closed link tuples" failed)
    ("                  == [POLARIS_NO_SIGNAL_PATHS, CONTRACT_RESTYLE_PATHS]))",
     "                  == [POLARIS_NO_SIGNAL_PATHS, CONTRACT_RESTYLE_PATHS,\n"
     "                      RFC5_CLASS_PATHS]))"),
)


# ---- helpers ---------------------------------------------------------------

class Refusal(Exception):
    pass


class Journal:
    """Remembers each file before the first write so a refusal restores the tree."""

    def __init__(self):
        self.saved: dict[pathlib.Path, bytes | None] = {}

    def save(self, path: pathlib.Path) -> None:
        if path not in self.saved:
            self.saved[path] = path.read_bytes() if path.is_file() else None

    def write(self, path: pathlib.Path, text: str) -> None:
        self.save(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def restore(self) -> None:
        for path, data in self.saved.items():
            if data is None:
                if path.is_file():
                    path.unlink()
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)


J = Journal()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def once(text: str, anchor: str, what: str) -> int:
    n = text.count(anchor)
    if n != 1:
        raise Refusal(f"{what}: anchor found {n} times, expected exactly once "
                      f"(check_governance.py has drifted; patch by hand and update this script)")
    return text.index(anchor)


def add_exemptions(text: str, lines: str) -> str:
    """Insert exemption rows before the closing brace of the exemptions dict."""
    start = once(text, EXEMPTION_DICT, "heading exemptions")
    end = text.index("\n}\n", start)
    return text[:end + 1] + lines + text[end + 1:]


def missing_records(root: pathlib.Path) -> list[str]:
    missing = [r for r in REQUIRED_RECORDS if not (root / r).is_file()]
    if not provider_routes(root):
        missing.append(f"{DECISIONS}/{ROUTE_A[1]}  (route A)  or  {DECISIONS}/{ROUTE_B[1]}  (route B)")
    if not egress_records(root):
        missing.append(f"{DECISIONS}/{EGRESS_V2[1]}  (egress version 2, row 8)  or  {DECISIONS}/{EGRESS_V1[1]}  (version 1, row 6)")
    return missing


STAGE_MAP_TS = "apps/three-surface-poc/src/polaris-generation/dossier-stage-authority.ts"
STAGE_MAP_ROWS = (("EGRESS_V1_DIGEST", EGRESS_V1, "[...NARRATIVE_STAGES]"),
                  ("EGRESS_V2_DIGEST", EGRESS_V2, "[...NARRATIVE_STAGES, ...DISCOVERY_STAGES]"))


def check_stage_map(root: pathlib.Path) -> str:
    """The wiring's per-digest stage map must name the digest of each performed egress record (the
    act's argument) and give version 2 the narrative and the two discovery stages, version 1 the
    narrative stages only. Read-only. Returns a note; refuses on a mismatch. A tree without the
    wiring (its pull request unmerged) is reported, not refused: nothing there reads the map."""
    path = root / STAGE_MAP_TS
    if not path.is_file():
        return "stage map: not in this tree (the wiring pull request is unmerged); not checked [Unknown]"
    text = path.read_text()
    checked = []
    for const, (_label, record, _m), stages in STAGE_MAP_ROWS:
        rec = root / DECISIONS / record
        if not rec.is_file():
            continue
        args = re.findall(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`", rec.read_text(), re.M)
        decl = re.findall(rf"export const {const} = '([0-9a-f]{{64}})'", text)
        if len(args) != 1 or len(decl) != 1:
            raise Refusal(f"stage map: {record} carries {len(args)} argument lines and the map declares {const} {len(decl)} times, expected one each")
        if args[0] != decl[0]:
            raise Refusal(f"stage map: {const} is not the digest {record} bound; the gate would authorise no stage for the record in force")
        if f"[{const}, Object.freeze({stages})]" not in text:
            raise Refusal(f"stage map: {const} does not map to the stages {stages}")
        checked.append(const)
    return f"stage map: {', '.join(checked)} equal the recorded act arguments"


def rfc5_precondition(root: pathlib.Path) -> None:
    record = (root / RFC5_ACT).read_text()
    if len(re.findall(r"^Act instant: \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", record, re.M)) != 1:
        raise Refusal("the RFC5-14 act record carries no single 'Act instant:' line; the recorder "
                      "predates act-instant support, so the contract chain link cannot order it "
                      "(runbook finding F12: re-run the recorder from a build that writes it)")


def rfc5_act_argument(root: pathlib.Path) -> str:
    """The digest the row-7 act bound; the installed RFC-0005 bytes must be exactly this."""
    m = re.findall(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`", (root / RFC5_ACT).read_text(), re.M)
    if len(m) != 1:
        raise Refusal(f"the RFC5-14 act record carries {len(m)} 'Exact digest (SHA-256)' lines, expected one")
    return m[0]


def rfc5_installed_matches(root: pathlib.Path, act_arg: str) -> None:
    for mirror in ("rfcs", "candidates/rfcs"):
        module = root / ".syzygy/governance/contracts" / mirror / "RFC-0005/consent-egress-secrets.md"
        if not module.is_file() or sha(module.read_bytes()) != act_arg:
            raise Refusal(f"installed {module} does not hash to the row-7 act's argument")


# ---- steps -----------------------------------------------------------------

def step_registrations(root: pathlib.Path, write: bool) -> bool:
    """True when the step changed (or would change) anything."""
    perf = performed(root)
    path = root / CG
    text = path.read_text()
    changed = False
    if REGISTRATIONS_MARK not in text:
        i = once(text, REGISTRATIONS_ANCHOR, "registrations") + len(REGISTRATIONS_ANCHOR)
        text = text[:i] + registrations_code(perf) + text[i:]
        text = add_exemptions(text, exemptions_code(perf))
        changed = True
    else:
        absent = [rec for _l, rec, _m in perf if f'/{rec}", "manifest")' not in text]
        if absent:
            raise Refusal(f"registrations are installed for another record set; {absent} are not "
                          "registered (add them by hand or revert the earlier install)")
    if changed and write:
        J.write(path, text)
    return changed


def step_rfc5(root: pathlib.Path, write: bool) -> bool:
    changed = False
    manifest = (root / RFC5_PKG / "CONTRACT-AMENDMENT-MANIFEST.txt").read_text()
    rows = re.findall(r"^([0-9a-f]{64})  (\S+)$", manifest, re.M)
    if [p for _d, p in rows] != [RFC5_MODULE]:
        raise Refusal(f"rfc5 manifest rows are {[p for _d, p in rows]}, expected exactly [{RFC5_MODULE}]")
    row = rows[0][0]
    act_arg = rfc5_act_argument(root)
    if row != act_arg:
        raise Refusal("the rfc5 manifest row is not the digest the row-7 act bound; refusing to install "
                      "text the act did not bind")
    patch = root / RFC5_PKG / "proposed/RFC-0005/consent-egress-secrets.md.patch"
    for mirror in ("rfcs", "candidates/rfcs"):
        module = root / ".syzygy/governance/contracts" / mirror / "RFC-0005/consent-egress-secrets.md"
        if sha(module.read_bytes()) == row:
            continue
        changed = True
        if write:
            J.save(module)
            r = subprocess.run(["patch", "-s", "-p0", str(module), "-i", str(patch)], capture_output=True, text=True)
            if r.returncode or sha(module.read_bytes()) != row:
                raise Refusal(f"patch did not produce the manifest row for {module}: {r.stdout}{r.stderr}")
    if write or not changed:
        rfc5_installed_matches(root, act_arg)
    active = root / CAND / "ACTIVE-CONTRACT-MANIFEST.txt"
    lines = active.read_text().split("\n")
    idx = [i for i, l in enumerate(lines) if l.endswith(f"  {RFC5_MODULE}")]
    if len(idx) != 1:
        raise Refusal(f"active manifest names {RFC5_MODULE} {len(idx)} times, expected once")
    if not lines[idx[0]].startswith(row):
        changed = True
        lines[idx[0]] = f"{row}  {RFC5_MODULE}"
        if write:
            J.write(active, "\n".join(lines))
    cg = root / CG
    text = cg.read_text()
    if CHAIN_MARK not in text:
        changed = True
        for anchor, replacement in CHAIN_EDITS:
            once(text, anchor, "contract chain link")
            text = text.replace(anchor, replacement)
        text = add_exemptions(text, RFC5_EXEMPTION)
        if write:
            J.write(cg, text)
    if changed and write:
        J.save(root / "DIRECTIVE-REGISTER.md")
        subprocess.run([sys.executable, "scripts/build_directive_register.py"], cwd=root,
                       capture_output=True, check=True)
    # the context-budget report counts every module's words, RFC-0005 included
    if (root / BUDGET_SCRIPT).is_file() and subprocess.run(
            [sys.executable, BUDGET_SCRIPT, "--check"], cwd=root, capture_output=True).returncode:
        changed = True
        if write:
            fixtures = sorted((root / CAND / "fixtures").glob("context-selection-*.md"))
            before = {p: p.read_bytes() for p in fixtures}
            for p in [root / BUDGET_REPORT, *fixtures]:
                J.save(p)
            subprocess.run([sys.executable, BUDGET_SCRIPT], cwd=root, capture_output=True, check=True)
            moved = [p.name for p, body in before.items() if p.read_bytes() != body]
            if moved:
                raise Refusal(f"regenerating the budget report rewrote fixture anchors in {moved}; "
                              "only the report may move with the rfc5 module")
    return changed


def step_profile(root: pathlib.Path, write: bool) -> bool:
    changed = False
    src = root / PROFILE_CHANGE / "proposed/polaris-generation/spec.md"
    dst = root / PROFILE_CHANGE / "specs/polaris-generation/spec.md"
    if src.is_file():
        changed = True
        if write:
            J.save(src)
            J.save(dst)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            for leftover in (src.parent, src.parent.parent):
                if leftover.is_dir() and not any(leftover.iterdir()):
                    leftover.rmdir()
    elif not dst.is_file():
        raise Refusal("the narrative-profile spec is in neither proposed/ nor specs/")
    old_new = (
        ("openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md",
         "openspec/changes/polaris-non-governed-narrative-profile/specs/polaris-generation/spec.md"),
        ("`proposed/polaris-generation/spec.md`", "`specs/polaris-generation/spec.md`"),
    )
    for rel in (f"{PROFILE_PKG}/REVIEW-BRIEF.md", f"{PROFILE_PKG}/SEMANTIC-DELTA.md",
                f"{PROFILE_CHANGE}/GOVERNING-DEPENDENCIES.md", f"{PROFILE_CHANGE}/design.md"):
        p = root / rel
        text = p.read_text()
        new = text
        for a, b in old_new:
            new = new.replace(a, b)
        if new != text:
            changed = True
            if write:
                J.write(p, new)
    # the status page figure follows the recount tool, which this step then runs
    r = subprocess.run([sys.executable, "scripts/count_polaris_effective_scenarios.py"], cwd=root,
                       capture_output=True, text=True)
    m = re.search(r"TOTAL: (\d+) requirements, (\d+) scenarios", r.stdout)
    if not m:
        raise Refusal("the recount tool does not compose the three specs "
                      f"(land the recount fix first): {r.stdout[-200:]}{r.stderr[-200:]}")
    status = root / STATUS
    text = status.read_text()
    new = status_figures(root, profile_lead_in(text),
                         f"{m.group(1)} requirements and {m.group(2)} scenarios")
    if new != text:
        changed = True
        if write:
            J.write(status, new)
    readme = root / OPENSPEC_README
    text = readme.read_text()
    new = profile_readme(text, adoption_date(root))
    if new != text:
        changed = True
        if write:
            J.write(readme, new)
    return changed


OPENSPEC_README = "openspec/README.md"
PROFILE_RECORD = f"{DECISIONS}/POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md"
#: The status page's Polaris figure follows this link; the profile joins it.
AMENDMENT_LINK = ("[the adopted amendment](openspec/changes/polaris-manifesto-understanding-amendment"
                  "/specs/polaris-generation/spec.md)")
PROFILE_LEAD_IN = (
    f"{AMENDMENT_LINK}\n"
    "    and the adopted\n"
    f"    [non-governed narrative profile]({PROFILE_CHANGE}/specs/polaris-generation/spec.md)\n"
    f"    ([adoption record]({PROFILE_RECORD}))")
#: The openspec/README.md table's lead paragraph, before the profile's adoption
#: (main; #353 merged; the dossier signed off) -> after it. The third and the
#: dossier sign-off's 2b block are pinned to that package's route-edits file.
README_LEADS = {
    "A sixth row below is a candidate that no act binds; it is listed so that the\n"
    "table stays one row per directory, and it is not one of the five.":
    "The narrative-profile row below is an addition to the Polaris generator\n"
    "composition, adopted by an owner direction rather than an act; the effective\n"
    "composition is the base read with the understanding amendment and each\n"
    "addition. It is not one of the five.",
    "The sixth and seventh rows below are candidates that no act binds; they are\n"
    "listed so that the table stays one row per directory, and neither is one of\n"
    "the five.":
    "The narrative-profile row below is an addition to the Polaris generator\n"
    "composition, adopted by an owner direction rather than an act; the effective\n"
    "composition is the base read with the understanding amendment and each\n"
    "addition. The dossier local-agent row is a candidate that no act binds,\n"
    "listed so that the table stays one row per directory. Neither is one of the\n"
    "five.",
    "The dossier local-agent row below is a signed addition to the Polaris\n"
    "generator composition, bound by a version-tagged sign-off rather than an\n"
    "act; the effective composition is the base read with the understanding\n"
    "amendment and each addition. The narrative-profile row is a candidate that\n"
    "no act binds, listed so that the table stays one row per directory. Neither\n"
    "is one of the five.":
    "The dossier local-agent and narrative-profile rows below are additions to\n"
    "the Polaris generator composition, bound by a version-tagged sign-off and\n"
    "an owner direction respectively rather than by an act; the effective\n"
    "composition is the base read with the understanding amendment and each\n"
    "addition. Neither is one of the five.",
}
PROFILE_ROW_PREFIX = "| [`polaris-non-governed-narrative-profile`](changes/polaris-non-governed-narrative-profile) |"


def profile_row(date: str) -> str:
    name = pathlib.PurePosixPath(PROFILE_RECORD).name
    return (f"{PROFILE_ROW_PREFIX} A Polaris generator requirement for narrating an observed repository "
            f"that has no Syzygy declarations | **Adopted {date} by owner direction** (requirement 032). "
            f"An addition to the generator composition; amend only through CC-REV-2 | "
            f"[`{name}`](../{PROFILE_RECORD}) ({date}) |")


def adoption_date(root: pathlib.Path) -> str:
    dates = re.findall(r"^Date: (\d{4}-\d{2}-\d{2})$", (root / PROFILE_RECORD).read_text(), re.M)
    if len(dates) != 1:
        raise Refusal(f"{PROFILE_RECORD}: expected one Date: line, found {len(dates)}")
    return dates[0]


def profile_lead_in(text: str) -> str:
    """The status page's Polaris figure names the profile beside the amendment (R-365-2 N2)."""
    if PROFILE_LEAD_IN in text:
        return text
    if text.count(AMENDMENT_LINK + ":") != 1:
        raise Refusal(f"{STATUS}: expected the understanding amendment's figure lead-in once")
    return text.replace(AMENDMENT_LINK + ":", PROFILE_LEAD_IN + ":")


def profile_readme(text: str, date: str) -> str:
    """openspec/README.md: the profile row names its adoption record; the lead paragraph says so."""
    rows = [ln for ln in text.split("\n") if ln.startswith(PROFILE_ROW_PREFIX)]
    if len(rows) != 1:
        raise Refusal(f"{OPENSPEC_README}: expected one narrative-profile row, found {len(rows)}")
    text = text.replace(rows[0], profile_row(date))
    if not any(new in text for new in README_LEADS.values()):
        olds = [old for old in README_LEADS if old in text]
        if len(olds) != 1:
            raise Refusal(f"{OPENSPEC_README}: the table's lead paragraph is none of the known forms")
        text = text.replace(olds[0], README_LEADS[olds[0]])
    return text


def step_reconcile(root: pathlib.Path, write: bool) -> bool:
    """The reconciliation follows the profile install (R-365-2 B3): census and addition unions."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_dependency_unions as unions
    import check_spec_reconciliation as recon
    targets = [root / recon.CENSUS] + [root / unions.union_file(c) for c in unions.additions(root)]
    if not write:
        pop, findings = recon.census(root)
        if findings:
            return True
        stale = [c for c in unions.additions(root) if (root / unions.union_file(c)).read_text()
                 != unions.regenerate(root, c)]
        return bool(stale) or (root / recon.CENSUS).read_text() != recon.census_json(pop)
    before = {t: t.read_bytes() if t.is_file() else None for t in targets}
    for t in targets:
        J.save(t)
    try:
        recon.regenerate(root)
    except SystemExit as exc:
        raise Refusal(f"the reconciliation refuses the installed tree: {exc}") from exc
    return any((t.read_bytes() if t.is_file() else None) != b for t, b in before.items())


def status_figures(root: pathlib.Path, text: str, total: str) -> str:
    """The status text with its figures following the recount.

    Once the dossier local-agent addition is signed off the page gives two
    figures, without it and with it; rewriting only the second leaves the
    first false (R-364-2 Finding 1), so the dossier builder rewrites both.
    """
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_dossier_local_agent_mode as dossier
    if dossier.WITHOUT_RE.search(text):
        try:
            return dossier.refigure(root, text)
        except dossier.Refusal as exc:
            raise Refusal(str(exc)) from exc
    figure = re.search(r"(\d+) requirements and (\d+) scenarios in the effective composition", text)
    if figure is None:
        raise Refusal("PROJECT-STATUS.md has no effective-composition figure")
    return text.replace(figure.group(0), f"{total} in the effective composition")


# ---- policy step (F4/F10) ------------------------------------------------------

_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
          9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
          15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
_TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def number_word(n: int) -> str:
    if n in _WORDS:
        return _WORDS[n]
    if 20 <= n <= 99:
        return _TENS[n // 10] + ("" if n % 10 == 0 else "-" + _WORDS[n % 10])
    raise Refusal(f"battery count {n} is outside the range the status sentence can spell")


def grab(pattern: str, text: str, what: str, flags: int = re.M) -> str:
    found = re.findall(pattern, text, flags)
    if len(found) != 1:
        raise Refusal(f"{what}: expected exactly one match of {pattern!r}, found {len(found)}")
    return found[0]


def replace_all_counted(text: str, old: str, new: str, what: str, minimum: int = 1) -> str:
    n = text.count(old)
    if n < minimum:
        raise Refusal(f"{what}: {old!r} found {n} times, expected at least {minimum}")
    return text.replace(old, new)


CHAIN_ROW_ANCHOR = '''     "2356b9ed3235b3dff79caeb352803a30c446b7365a2a7ea74df302b9fa51386a"),
)
#: For a chained amendment row'''
OFFERINGS_ANCHOR = '''        f"{CANDIDATES}/pwb-registry-currency-briefing-amendment/PWB-EFFECT-AMENDMENT-MANIFEST.txt": "row",
    },
}'''
REPIN_MANIFEST_ANCHOR = '''        ACT_DIGEST_COPY_FILES[PWB_BEHAVIOR_REPIN_MANIFEST] = (
            PWB_EFFECT_ACTS[1][0], PWB_EFFECT_ACTS[2][0])
'''
REPIN_DIR_ANCHOR = 'PWB_BEHAVIOR_REPIN_MANIFEST = f"{PWB_BEHAVIOR_REPIN_DIR}/PWB-EFFECT-REPIN-MANIFEST.txt"\n'
REPIN_CALL_ANCHOR = "_activate_pwb_behavior_repin_manifest_copy_registry()\n"
POLICY_MARK = "PWB_SCOPE_ACT"


def policy_cg_edits(text: str, old_arg: str) -> str:
    """The screening-scope act becomes the policy's chain link; the re-pin is history."""
    if POLICY_MARK in text:
        return text
    i = once(text, CHAIN_ROW_ANCHOR, "policy chain row") + len(CHAIN_ROW_ANCHOR) - len(")\n#: For a chained amendment row")
    row = ('    # The public-source screening-scope act supersedes the 2026-10-02 re-pin\n'
           '    # act for the policy subject.\n'
           '    (PWB_EFFECT_ACTS[1][0], PWB_EFFECT_ACTS[1][1],\n'
           '     f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md",\n'
           '     f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md",\n'
           f'     "{old_arg}"),\n')
    text = text[:i] + row + text[i:]
    i = once(text, OFFERINGS_ANCHOR, "policy offerings") + len(OFFERINGS_ANCHOR) - 2
    text = text[:i] + (
        '    # The 2026-10-02 policy re-pin was offered as a row of the re-pin manifest;\n'
        '    # its packet by design carries no digest.\n'
        '    f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md": {\n'
        '        PWB_BEHAVIOR_REPIN_MANIFEST: "row",\n'
        '    },\n') + text[i:]
    i = once(text, REPIN_MANIFEST_ANCHOR, "re-pin manifest registry") + len(REPIN_MANIFEST_ANCHOR)
    text = text[:i] + (
        '        # Once the screening-scope act supersedes the policy re-pin, the\n'
        '        # policy row is history (registered by the amendment registries).\n'
        '        if os.path.isfile(os.path.join(ROOT, PWB_SCOPE_ACT)):\n'
        '            ACT_DIGEST_COPY_FILES[PWB_BEHAVIOR_REPIN_MANIFEST] = (\n'
        '                PWB_EFFECT_ACTS[2][0],)\n') + text[i:]
    i = once(text, REPIN_DIR_ANCHOR, "re-pin directory constants") + len(REPIN_DIR_ANCHOR)
    text = text[:i] + (
        'PWB_SCOPE_DIR = f"{CANDIDATES}/public-source-screening-scope"\n'
        'PWB_SCOPE_MANIFEST = f"{PWB_SCOPE_DIR}/PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt"\n'
        'PWB_SCOPE_ACT = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md"\n') + text[i:]
    i = once(text, REPIN_CALL_ANCHOR, "re-pin registry call") + len(REPIN_CALL_ANCHOR)
    text = text[:i] + '''

def _activate_pwb_scope_manifest_copy_registry():
    """The screening-scope manifest carries the policy's proposed argument.

    Existence-gated candidate file: a current copy of the policy argument
    while it exists.
    """
    if os.path.isfile(os.path.join(ROOT, PWB_SCOPE_MANIFEST)):
        ACT_DIGEST_COPY_FILES[PWB_SCOPE_MANIFEST] = (PWB_EFFECT_ACTS[1][0],)


_activate_pwb_scope_manifest_copy_registry()
''' + text[i:]
    return add_exemptions(text, '    (PWB_SCOPE_ACT, "manifest"): PWB_SCOPE_MANIFEST,\n')


V2_CHAIN_MARK = "screening-scope v2 chain row"
OFFERINGS_END_ANCHOR = "}\nPWB_STATE1_SUBJECTS = tuple(sorted(("
V1_MANIFEST_GATE_OLD = ("    if os.path.isfile(os.path.join(ROOT, PWB_SCOPE_MANIFEST)):\n"
                        "        ACT_DIGEST_COPY_FILES[PWB_SCOPE_MANIFEST] = (PWB_EFFECT_ACTS[1][0],)\n")
V1_MANIFEST_GATE_NEW = ("    if (os.path.isfile(os.path.join(ROOT, PWB_SCOPE_MANIFEST))\n"
                        '            and not os.path.isfile(os.path.join(ROOT, f"{DECISIONS}/'
                        'PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md"))):\n'
                        "        # once the version-2 act supersedes it, the version-1 manifest row is history\n"
                        "        ACT_DIGEST_COPY_FILES[PWB_SCOPE_MANIFEST] = (PWB_EFFECT_ACTS[1][0],)\n")


def policy_cg_v2_edits(text: str, v1_arg: str) -> str:
    """The version-2 act supersedes the version-1 act for the policy subject. Applies on top of
    `policy_cg_edits`; the version-1 manifest becomes history and the version-2 manifest, which
    check_governance registers once the performed record exists, takes its place."""
    if V2_CHAIN_MARK in text:
        return text
    if POLICY_MARK not in text:
        raise Refusal("the version-2 chain row needs the version-1 install first (policy_cg_edits)")
    i = once(text, ")\n#: For a chained amendment row", "policy chain end")
    row = ('    # The public-source screening-scope version-2 act supersedes the version-1 act for\n'
           f'    # the policy subject ({V2_CHAIN_MARK}).\n'
           '    (PWB_EFFECT_ACTS[1][0], PWB_EFFECT_ACTS[1][1],\n'
           '     f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md",\n'
           '     f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md",\n'
           f'     "{v1_arg}"),\n')
    text = text[:i] + row + text[i:]
    i = once(text, OFFERINGS_END_ANCHOR, "policy offerings end")
    text = text[:i] + (
        '    # The version-1 screening-scope act was offered as the one row of its manifest;\n'
        '    # its packet by design carries no digest.\n'
        '    f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-ACT.md": {\n'
        '        f"{CANDIDATES}/public-source-screening-scope/PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt": "row",\n'
        '    },\n') + text[i:]
    once(text, V1_MANIFEST_GATE_OLD, "version-1 manifest registration")
    text = text.replace(V1_MANIFEST_GATE_OLD, V1_MANIFEST_GATE_NEW, 1)
    return add_exemptions(text, '    (PUBLIC_SOURCE_SCOPE_V2_ACT, "manifest"): PUBLIC_SOURCE_SCOPE_V2_MANIFEST,\n')


def battery_lines(record: str, new_arg: str, date: str, script: str = V1_SCRIPT) -> tuple[str, str]:
    """The scope recorder's --check line needs the owner's selection text, read back from the record."""
    opening = " ".join(grab(r'that opened "(.+?)" by selecting', record, "question opening", re.S).split())
    rows = re.findall(r'^\| "(.*)" \| "(.*)" \|$', record, re.M)
    if len(rows) != 1:
        raise Refusal(f"the scope act record carries {len(rows)} selection table rows, expected one")
    label, desc = rows[0]
    for s in (opening, label, desc):
        if ": " in s or " #" in s or "'" in s:
            raise Refusal("the owner's selection text contains ': ', ' #' or a quote, which a plain YAML "
                          "workflow line and the battery splitter cannot carry; add the --check line "
                          "to PROJECT-STATUS.md and the workflow by hand")
    cmd = (f"python3 scripts/{script}.py --check {new_arg} --date {date} "
           f"--question-opening '{opening}' --selection-label '{label}' --selection-description '{desc}'")
    return cmd, f"python3 scripts/{script}.py --selftest"


def edit_battery(status: str, workflow: str, check_cmd: str, selftest_cmd: str,
                 script: str = V1_SCRIPT) -> tuple[str, str]:
    """Idempotent. Three starting states: the re-pin lines (install the final recorder's lines in
    their place), the version-1 recorder's lines (replace them when the final recorder is
    version 2), or the final recorder's lines already (nothing to do)."""
    if f"{script}.py --check" in status:
        return status, workflow
    note = "   # screening-scope policy act: record, aggregate block and applied subject"
    if script != V1_SCRIPT and f"{V1_SCRIPT}.py --check" in status:
        lines = status.split("\n")
        out, hit = [], 0
        for ln in lines:
            if ln.startswith(f"python3 scripts/{V1_SCRIPT}.py --check"):
                out.append(check_cmd + note)
                hit += 1
            elif ln.startswith(f"python3 scripts/{V1_SCRIPT}.py --selftest"):
                out.append(selftest_cmd)
                hit += 1
            else:
                out.append(ln)
        if hit != 2:
            raise Refusal("status battery: expected to replace exactly the version-1 check and selftest lines")
        status = "\n".join(out)
        wl = workflow.split("\n")
        out, hit = [], 0
        for ln in wl:
            st = ln.strip()
            if st == f"- name: {V1_SCRIPT} --check":
                out.append(ln.replace(V1_SCRIPT, script))
                hit += 1
            elif st == f"- name: {V1_SCRIPT} --selftest":
                out.append(ln.replace(V1_SCRIPT, script))
                hit += 1
            elif st.startswith(f"run: python3 scripts/{V1_SCRIPT}.py --check"):
                out.append("        run: " + check_cmd)
            elif st.startswith(f"run: python3 scripts/{V1_SCRIPT}.py --selftest"):
                out.append("        run: " + selftest_cmd)
            else:
                out.append(ln)
        if hit != 2:
            raise Refusal("workflow: expected to replace exactly the version-1 check and selftest steps")
        return status, "\n".join(out)
    drop_b = "python3 scripts/build_pwb_behavior_contract_repin.py --check"
    drop_r = "python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy "
    lines = status.split("\n")
    keep = []
    for ln in lines:
        if ln.startswith(drop_b) or ln.startswith(drop_r):
            continue
        keep.append(ln)
        if ln.startswith("python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest"):
            keep.append(check_cmd + note)
            keep.append(selftest_cmd)
    if len(keep) != len(lines):
        raise Refusal("status battery: expected to drop exactly two lines and add two")
    status = "\n".join(keep)
    skip = 0
    wlines = workflow.split("\n")
    out = []
    i = 0
    while i < len(wlines):
        ln = wlines[i]
        if ln.strip() in ("- name: build_pwb_behavior_contract_repin --check",
                          "- name: record_pwb_behavior_contract_repin_acts --check policy"):
            i += 3 if i + 2 < len(wlines) and wlines[i + 2].strip() == "" else 2
            skip += 1
            continue
        out.append(ln)
        if ln.strip() == "run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest":
            out += ["", f"      - name: {script} --check",
                    f"        run: {check_cmd}", "",
                    f"      - name: {script} --selftest",
                    f"        run: {selftest_cmd}"]
        i += 1
    if skip != 2:
        raise Refusal(f"workflow: expected to drop two steps, dropped {skip}")
    workflow = "\n".join(out)
    m = re.search(r"\bThe ([a-z]+(?:-[a-z]+)*) checks above are the same ([a-z]+(?:-[a-z]+)*)\b", status)
    if not m:
        raise Refusal("PROJECT-STATUS.md carries no 'The N checks above are the same N' sentence")
    block = re.search(r"## How to verify this page.*?```sh\n(.*?)```", status, re.S).group(1)
    n = len([ln for ln in block.split("\n") if ln.startswith("python3 ")])
    word = number_word(n)
    status = status.replace(m.group(0), f"The {word} checks above are the same {word}")
    return status, workflow


@dataclass
class PolicyAct:
    key: str
    path: str
    text: str
    arg: str
    identity: str
    tag: str
    date: str
    instant: str
    script: str
    supersedes: str          # the act record this one supersedes in the read gate's pair
    manifest: str


def read_policy_act(root: pathlib.Path, key: str, path: str, script: str, manifest: str,
                    supersedes: str) -> PolicyAct:
    if not (root / path).is_file():
        raise Refusal(f"the {key} policy act record is absent: {path}")
    text = (root / path).read_text()
    return PolicyAct(
        key, path, text,
        grab(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`$", text, f"{key} act digest"),
        grab(r"^Act identity: `([^`]+)`$", text, f"{key} act identity"),
        grab(r"recording tag: `([^`]+)`", text, f"{key} recording tag"),
        grab(r"^Date: (\d{4}-\d{2}-\d{2})$", text, f"{key} act date"),
        grab(r"^Recorded at \(UTC\): (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$", text, f"{key} recorded instant"),
        script, supersedes, manifest)


def policy_acts(root: pathlib.Path) -> list[PolicyAct]:
    """The policy acts in force, in order: version 1, then version 2 when it exists. Refuses an
    order or a pair the records themselves contradict, so the wrong order is never installed."""
    v1 = read_policy_act(root, "v1", SCOPE_ACT, V1_SCRIPT, SCOPE_MANIFEST, REPIN_ACT)
    acts = [v1]
    if (root / V2_ACT).is_file():
        v2 = read_policy_act(root, "v2", V2_ACT, V2_SCRIPT, V2_MANIFEST, SCOPE_ACT)
        if v2.arg == v1.arg:
            raise Refusal("the version-2 act carries the version-1 act's argument: it cannot supersede it")
        if v2.instant <= v1.instant:
            raise Refusal(f"the version-2 act ({v2.instant}) is not recorded after the version-1 act "
                          f"({v1.instant}): it supersedes the version-1 act, so the order is v1 then v2")
        if SCOPE_ACT not in v2.text or v1.arg not in v2.text:
            raise Refusal("the version-2 act record does not name the version-1 act and its argument "
                          "as the act it supersedes")
        acts.append(v2)
    policy = sha((root / POLICY_JSON).read_bytes())
    if policy != acts[-1].arg:
        raise Refusal(f"the policy on disk does not hash to the final policy act's argument "
                      f"({acts[-1].key}); the acts and the policy disagree")
    return acts


GATE_POLICY_POINTER = re.compile(
    r"policy: '(\.syzygy/governance/decisions/PWB-SECRET-CLASSIFICATION-POLICY-[A-Z0-9-]+-ACT\.md)'")
GATE_COMMENT = re.compile(r"// The policy act is the [^\n]*\n(?://[^\n]*\n)*(?=export const PWB_ACT_RECORDS:)")


def repoint_gate(inputs: str, desired: list[str], comment: str) -> str:
    """Rewrite the two policy record pointers to (final act, the act it supersedes) and the
    explanatory comment, whatever pair the file carries now."""
    if len(GATE_POLICY_POINTER.findall(inputs)) != 2:
        raise Refusal("governance-inputs.ts does not carry exactly two policy record pointers")
    count = iter(range(2))
    out = GATE_POLICY_POINTER.sub(lambda m: f"policy: '{desired[next(count)]}'", inputs)
    out = GATE_COMMENT.sub("", out)
    marker = "export const PWB_ACT_RECORDS:"
    once(out, marker, "gate act-records marker")
    return out.replace(marker, comment + marker, 1)


def gate_comment(acts: list[PolicyAct]) -> str:
    final = acts[-1]
    if final.key == "v2":
        return (f"// The policy act is the {final.date} public-source screening-scope version 2 act, superseding the\n"
                f"// {acts[0].date} version-1 act; the registry act is still its 2026-10-02 re-pin act.\n")
    return (f"// The policy act is the {final.date} public-source screening-scope act, superseding the\n"
            f"// 2026-10-02 policy re-pin act; the registry act is still its 2026-10-02 re-pin act.\n")


def step_policy(root: pathlib.Path, write: bool) -> bool:
    acts = policy_acts(root)
    final = acts[-1]
    repin = (root / REPIN_ACT).read_text()
    repin_arg = grab(r"^Exact digest \(SHA-256\): `([0-9a-f]{64})`$", repin, "re-pin digest")
    new_ver = json.loads((root / POLICY_JSON).read_text())["policyVersion"]
    reader = (root / "packages/three-surface-poc-core/src/git-object-reader.ts").read_text()
    old_ver = grab(r"policyVersion: '([^']+)'", reader, "reader policy version") if "policyVersion: '" in reader else new_ver
    inputs = (root / INPUTS_TS).read_text()
    changed = False
    # check_governance supersession: the version-1 link, then the version-2 link on top of it
    cg = root / CG
    text = cg.read_text()
    new_text = policy_cg_edits(text, repin_arg)
    if final.key == "v2":
        new_text = policy_cg_v2_edits(new_text, acts[0].arg)
    if new_text != text:
        changed = True
        if write:
            J.write(cg, new_text)
    # the read gate and its tests follow the final act, once: its policy pointer pair is
    # (final act, the act it supersedes)
    desired = [final.path, final.supersedes]
    found = GATE_POLICY_POINTER.findall(inputs)
    if len(found) != 2:
        raise Refusal(f"governance-inputs.ts carries {len(found)} policy record pointers, expected two")
    if found != desired:
        changed = True
        if write:
            old_id = grab(r"actIdentity: '(PWB-SECRET-CLASSIFICATION-POLICY-[^']+)'", inputs, "gate policy identity")
            old_tag = grab(r"recordingTag: '(pwb-approve-policy-[^']+)'", inputs, "gate policy tag")
            for rel in PIN_FILES:
                p = root / rel
                s = p.read_text()
                for a, b in ((old_id, final.identity), (old_tag, final.tag), (old_ver, new_ver)):
                    if a in s:
                        s = s.replace(a, b)
                J.write(p, s)
            J.write(root / INPUTS_TS, repoint_gate((root / INPUTS_TS).read_text(), desired, gate_comment(acts)))
            t = (root / INPUTS_TEST).read_text()
            t = re.sub(r"const EVALUATION_INSTANT = '[^']+';", f"const EVALUATION_INSTANT = '{final.date}T00:00:00Z';", t)
            J.write(root / INPUTS_TEST, t)
    # the status battery and the hosted workflow carry the final recorder's lines
    check_cmd, selftest_cmd = battery_lines(final.text, final.arg, final.date, final.script)
    status = (root / STATUS).read_text()
    workflow = (root / WORKFLOW).read_text()
    ns, nw = edit_battery(status, workflow, check_cmd, selftest_cmd, final.script)
    if (ns, nw) != (status, workflow):
        changed = True
        if write:
            J.write(root / STATUS, ns)
            J.write(root / WORKFLOW, nw)
    return changed


STEPS = (("registrations", step_registrations), ("rfc5", step_rfc5), ("policy", step_policy), ("profile", step_profile),
         ("reconcile", step_reconcile))


def run(root: pathlib.Path, write: bool) -> int:
    global J
    J = Journal()
    missing = missing_records(root)
    if missing:
        print("REFUSED: required act records are missing (nothing written):")
        for m in missing:
            print(f"  {m}")
        return 2
    try:
        rfc5_precondition(root)
        print(check_stage_map(root))
        pending = []
        for name, fn in STEPS:
            if fn(root, write):
                pending.append(name)
    except Refusal as exc:
        J.restore()
        print(f"REFUSED: {exc} (tree restored)")
        return 2
    if write:
        print("installed: " + (", ".join(pending) if pending else "nothing to do (already installed)"))
        return 0
    print("not installed: " + (", ".join(pending) if pending else "none"))
    return 1 if pending else 0


# ---- selftest ----------------------------------------------------------------

def policy_selftests() -> list[tuple[str, bool]]:
    """The two-policy-act install: order, pairs, the chain edits, the gate pointers, the battery."""
    ok: list[tuple[str, bool]] = []

    def refused(fn) -> bool:
        try:
            fn()
        except Refusal:
            return True
        return False

    def record(arg, ident, tag, date, instant, extra=""):
        return (f"# act\n\nDate: {date}\n\nRecorded at (UTC): {instant}\n\nAct identity: `{ident}`\n\n"
                f"Exact digest (SHA-256): `{arg}`\n\n- recording tag: `{tag}`, on the commit\n{extra}\n"
                'that opened "Q one" by selecting the\n| "L" | "D d" |\n')

    a1, a2, repin = "1" * 64, "2" * 64, "0" * 64
    pol1, pol2 = b'{"policyVersion": "1.2.0"}\n', b'{"policyVersion": "1.3.0"}\n'
    a1, a2 = sha(pol1), sha(pol2)

    def tree(t, v2=True, v2_instant="2026-10-04T10:00:00Z", v2_arg=None, policy=None, naming=True, v1=True):
        root = pathlib.Path(t)
        (root / SCOPE_ACT).parent.mkdir(parents=True, exist_ok=True)
        if v1:
            (root / SCOPE_ACT).write_text(record(a1, "ID1", "tag1", "2026-10-04", "2026-10-04T09:00:00Z"))
        (root / REPIN_ACT).write_text(record(repin, "ID0", "tag0", "2026-10-02", "2026-10-02T09:00:00Z"))
        if v2:
            extra = f"supersedes `{SCOPE_ACT}` argument `{a1}`\n" if naming else "\n"
            (root / V2_ACT).write_text(record(v2_arg or a2, "ID2", "tag2", "2026-10-04", v2_instant, extra))
        (root / POLICY_JSON).parent.mkdir(parents=True, exist_ok=True)
        (root / POLICY_JSON).write_bytes(policy if policy is not None else (pol2 if v2 else pol1))
        return root

    with tempfile.TemporaryDirectory() as t:
        got = policy_acts(tree(t, v2=False))
        ok.append(("policy acts: version 1 alone is the final act, superseding the re-pin",
                   [a.key for a in got] == ["v1"] and got[-1].supersedes == REPIN_ACT))
    with tempfile.TemporaryDirectory() as t:
        got = policy_acts(tree(t))
        ok.append(("policy acts: version 1 then version 2, the final act supersedes version 1",
                   [a.key for a in got] == ["v1", "v2"] and got[-1].supersedes == SCOPE_ACT
                   and got[-1].script == V2_SCRIPT and got[-1].arg == a2))
    for name, kwargs in (("version 2 recorded before version 1", dict(v2_instant="2026-10-04T08:00:00Z")),
                         ("version 2 recorded at the same instant", dict(v2_instant="2026-10-04T09:00:00Z")),
                         ("version 2 carrying version 1's argument", dict(v2_arg=a1, policy=pol1)),
                         ("version 2 that does not name version 1", dict(naming=False)),
                         ("the policy still at version 1's bytes after version 2", dict(policy=pol1)),
                         ("version 2 without version 1", dict(v1=False))):
        with tempfile.TemporaryDirectory() as t:
            root = tree(t, **kwargs)
            ok.append((f"policy acts refuse the wrong order or pair: {name}", refused(lambda: policy_acts(root))))
    with tempfile.TemporaryDirectory() as t:
        root = tree(t, v2=False, policy=pol2)
        ok.append(("policy acts: a policy that is not the final act's argument is refused",
                   refused(lambda: policy_acts(root))))

    # the check_governance edits: version 1, then version 2 on top, in that order only
    cg_text = (ROOT / CG).read_text()
    try:
        v1_only = policy_cg_edits(cg_text, "a" * 64)
        both = policy_cg_v2_edits(v1_only, "b" * 64)
        ast.parse(both)
        ok.append(("chain edits: version 2 on top of version 1 is valid Python", True))
        ok.append(("chain edits: one version-2 row, one offering, the version-1 manifest gated, one exemption",
                   both.count(V2_CHAIN_MARK) == 1
                   and both.count('PWB-SECRET-CLASSIFICATION-POLICY-PUBLIC-SOURCE-SCOPE-V2-ACT.md": ') == 0
                   and both.count("PUBLIC-SOURCE-SCREENING-SCOPE-MANIFEST.txt\": \"row\"") == 1
                   and V1_MANIFEST_GATE_NEW in both and V1_MANIFEST_GATE_OLD not in both
                   and both.count("PUBLIC_SOURCE_SCOPE_V2_MANIFEST,") == 1 + cg_text.count("PUBLIC_SOURCE_SCOPE_V2_MANIFEST,")))
        ok.append(("chain edits: version 2 is idempotent", policy_cg_v2_edits(both, "b" * 64) == both))
        ok.append(("chain edits: the argument quoted is version 1's", f'"{"b" * 64}"),' in both))
    except (SyntaxError, Refusal) as exc:
        print(f"  (chain edit failure: {exc})")
        ok.append(("chain edits: version 2 on top of version 1 is valid Python", False))
    ok.append(("chain edits: version 2 without version 1 is refused",
               refused(lambda: policy_cg_v2_edits(cg_text, "b" * 64))))

    # the read gate pointers, from each starting state to the final pair
    mark = "export const PWB_ACT_RECORDS: x = 1;\n"

    def gate(cur, sup, comment=""):
        return (f"{{ policy: '{cur}',\n registry: 'r' }}\n{{ policy: '{sup}',\n registry: 'r2' }}\n{comment}{mark}")
    amend = f"{DECISIONS}/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md"
    acts_v1 = [PolicyAct("v1", SCOPE_ACT, "", "", "", "", "2026-10-04", "", V1_SCRIPT, REPIN_ACT, "")]
    acts_v2 = [acts_v1[0], PolicyAct("v2", V2_ACT, "", "", "", "", "2026-10-05", "", V2_SCRIPT, SCOPE_ACT, "")]
    for name, start, acts in (("re-pin to version 1", gate(REPIN_ACT, amend), acts_v1),
                              ("re-pin straight to version 2", gate(REPIN_ACT, amend), acts_v2),
                              ("version 1 up to version 2", gate(SCOPE_ACT, REPIN_ACT, gate_comment(acts_v1)), acts_v2)):
        desired = [acts[-1].path, acts[-1].supersedes]
        done = repoint_gate(start, desired, gate_comment(acts))
        ok.append((f"gate pointers: {name}",
                   GATE_POLICY_POINTER.findall(done) == desired and done.count("// The policy act is the") == 1
                   and repoint_gate(done, desired, gate_comment(acts)) == done))
    ok.append(("gate pointers: a file with one policy pointer is refused",
               refused(lambda: repoint_gate(f"policy: '{SCOPE_ACT}'\n{mark}", [V2_ACT, SCOPE_ACT], ""))))

    # the battery, from each starting state
    st = ("## How to verify this page\n```sh\n"
          "python3 scripts/build_pwb_behavior_contract_repin.py --check   # x\n"
          "python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy abc --date d\n"
          "python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest\n```\n"
          "The three checks above are the same three the hosted workflow runs.\n")
    wf = ("      - name: build_pwb_behavior_contract_repin --check\n"
          "        run: python3 scripts/build_pwb_behavior_contract_repin.py --check\n\n"
          "      - name: record_pwb_behavior_contract_repin_acts --check policy\n"
          "        run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy abc --date d\n\n"
          "      - name: record_pwb_behavior_contract_repin_acts --selftest\n"
          "        run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest\n")
    c1, s1 = f"python3 scripts/{V1_SCRIPT}.py --check z", f"python3 scripts/{V1_SCRIPT}.py --selftest"
    c2, s2 = f"python3 scripts/{V2_SCRIPT}.py --check y", f"python3 scripts/{V2_SCRIPT}.py --selftest"
    n1, w1 = edit_battery(st, wf, c1, s1, V1_SCRIPT)
    n2, w2 = edit_battery(st, wf, c2, s2, V2_SCRIPT)
    n12, w12 = edit_battery(n1, w1, c2, s2, V2_SCRIPT)
    ok.append(("battery: re-pin to version 1 adds its two lines", c1 in n1 and s1 in n1 and V1_SCRIPT in w1))
    ok.append(("battery: re-pin straight to version 2 adds only version 2's lines",
               c2 in n2 and V1_SCRIPT not in n2 + w2 and "--check policy" not in n2 + w2))
    ok.append(("battery: version 1 up to version 2 replaces its lines in place",
               V1_SCRIPT not in n12 + w12 and (n12, w12) == (n2, w2)))
    ok.append(("battery: every final state is idempotent",
               edit_battery(n1, w1, c1, s1, V1_SCRIPT) == (n1, w1) and edit_battery(n2, w2, c2, s2, V2_SCRIPT) == (n2, w2)))
    ok.append(("battery: version 2's lines keep the count at three",
               "The three checks above are the same three" in n2 and n2.count("python3 ") == 3))
    ok.append(("battery: a workflow without the version-1 steps is refused on upgrade",
               refused(lambda: edit_battery(n1, wf, c2, s2, V2_SCRIPT))))
    return ok


def egress_selftests() -> list[tuple[str, bool]]:
    """Which egress version is recorded, and the stage map against the recorded arguments."""
    ok: list[tuple[str, bool]] = []

    def refused(fn) -> bool:
        try:
            fn()
        except Refusal:
            return True
        return False

    d1, d2 = "1" * 64, "2" * 64

    def act(arg):
        return f"# act\n\nExact digest (SHA-256): `{arg}`\n"

    def stage_map(c1, c2, v1_stages="[...NARRATIVE_STAGES]", v2_stages="[...NARRATIVE_STAGES, ...DISCOVERY_STAGES]"):
        return (f"export const EGRESS_V1_DIGEST = '{c1}';\nexport const EGRESS_V2_DIGEST = '{c2}';\n"
                f"new Map([[EGRESS_V1_DIGEST, Object.freeze({v1_stages})],\n  [EGRESS_V2_DIGEST, Object.freeze({v2_stages})]]);\n")

    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        (root / DECISIONS).mkdir(parents=True)
        ok.append(("egress: none recorded is refused as missing", egress_records(root) == []
                   and any("egress" in m for m in missing_records(root))))
        (root / DECISIONS / EGRESS_V2[1]).write_text(act(d2))
        ok.append(("egress: version 2 alone is enough and v1 stays unregistered", egress_records(root) == [EGRESS_V2]))
        (root / DECISIONS / EGRESS_V1[1]).write_text(act(d1))
        ok.append(("egress: both versions are registered when both exist", egress_records(root) == [EGRESS_V1, EGRESS_V2]))
        ok.append(("stage map: absent file is reported, not refused", "not checked" in check_stage_map(root)))
        ts = root / STAGE_MAP_TS
        ts.parent.mkdir(parents=True)
        ts.write_text(stage_map(d1, d2))
        ok.append(("stage map: constants equal the recorded arguments", "equal the recorded" in check_stage_map(root)))
        ts.write_text(stage_map(d1, "3" * 64))
        ok.append(("stage map: a constant that is not the bound argument is refused", refused(lambda: check_stage_map(root))))
        ts.write_text(stage_map(d1, d2, v2_stages="[...NARRATIVE_STAGES]"))
        ok.append(("stage map: version 2 without the discovery stages is refused", refused(lambda: check_stage_map(root))))
        ts.write_text(stage_map(d1, d2, v1_stages="[...NARRATIVE_STAGES, ...DISCOVERY_STAGES]"))
        ok.append(("stage map: version 1 with the discovery stages is refused", refused(lambda: check_stage_map(root))))
        ts.write_text(stage_map(d1, d2).replace("export const EGRESS_V2_DIGEST", "const EGRESS_V2_DIGEST"))
        ok.append(("stage map: an undeclared constant is refused", refused(lambda: check_stage_map(root))))
        (root / DECISIONS / EGRESS_V1[1]).unlink()
        ts.write_text(stage_map("9" * 64, d2))
        ok.append(("stage map: an unperformed version's constant is not checked", "EGRESS_V2_DIGEST" in check_stage_map(root)))
    return ok


def profile_figure_selftests() -> list[tuple[str, bool]]:
    """The profile install after the dossier sign-off rewrites both figures."""
    import contextlib
    import io
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_polaris_dossier_local_agent_mode as dossier
    ok: list[tuple[str, bool]] = []
    profile = pathlib.Path(PROFILE_CHANGE) / "specs/polaris-generation/spec.md"
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        dossier._fixture(root)
        ok.append(("before the dossier: one figure, digits rewritten",
                   status_figures(root, "x 2 requirements and 3 scenarios in the effective composition.",
                                  "9 requirements and 9 scenarios")
                   == "x 9 requirements and 9 scenarios in the effective composition."))
        with contextlib.redirect_stdout(io.StringIO()):
            dossier.apply(root)
        (root / profile).parent.mkdir(parents=True)
        (root / profile).write_text("## ADDED Requirements\n\n" + dossier._req("Gamma", 2))
        reqs, scenarios, _n = dossier.recount(root)
        text = (root / STATUS).read_text()
        (root / STATUS).write_text(status_figures(root, text, f"{reqs} requirements and {scenarios} scenarios"))
        ok.append(("profile after dossier: both figures follow the recount and the dossier check passes",
                   dossier.check(root) == []
                   and "3 requirements and 5 scenarios without" in (root / STATUS).read_text()
                   and "7 requirements and 9 scenarios in the effective" in (root / STATUS).read_text()))
        try:
            status_figures(root, text + text, "x")
            ok.append(("profile after dossier: a doubled figure is refused", False))
        except Refusal:
            ok.append(("profile after dossier: a doubled figure is refused", True))
    ok.extend(profile_route_selftests())
    return ok


def profile_route_selftests() -> list[tuple[str, bool]]:
    """The status lead-in and the openspec/README.md row and lead paragraph."""
    ok: list[tuple[str, bool]] = []

    def refused(fn) -> bool:
        try:
            fn()
            return False
        except Refusal:
            return True

    status = (f"  - Read the predecessor together with\n    {AMENDMENT_LINK}:\n"
              "    31 requirements and 182 scenarios in the effective composition.\n")
    once = profile_lead_in(status)
    ok.append(("lead-in: the figure names the profile and its adoption record, once",
               PROFILE_LEAD_IN + ":" in once and profile_lead_in(once) == once
               and once.count(PROFILE_RECORD) == 1))
    ok.append(("lead-in: a page without the amendment's lead-in is refused",
               refused(lambda: profile_lead_in("no figure here\n"))))
    row = PROFILE_ROW_PREFIX + " A candidate | **Candidate — binds nothing** | None |"
    for i, (old, new) in enumerate(README_LEADS.items()):
        got = profile_readme(f"intro\n{old}\n\n| h |\n{row}\n", "2026-10-07")
        ok.append((f"readme lead form {i}: replaced, row names the record, idempotent",
                   new in got and old not in got and profile_row("2026-10-07") in got
                   and profile_readme(got, "2026-10-07") == got))
    ok.append(("readme: an unknown lead paragraph is refused",
               refused(lambda: profile_readme(f"Some other lead.\n{row}\n", "2026-10-07"))))
    ok.append(("readme: two profile rows are refused",
               refused(lambda: profile_readme(f"{list(README_LEADS)[0]}\n{row}\n{row}\n", "d"))))
    ok.append(("lead-in: the amendment's lead-in twice is refused",
               refused(lambda: profile_lead_in(status + status))))
    with tempfile.TemporaryDirectory() as t0:
        rec = pathlib.Path(t0) / PROFILE_RECORD
        rec.parent.mkdir(parents=True)
        rec.write_text("# Adoption\n\nDate: 2026-10-07\n\nBody.\n")
        one = adoption_date(pathlib.Path(t0)) == "2026-10-07"
        rec.write_text("# Adoption\n\nDate: 2026-10-07\n\nDate: 2026-10-08\n")
        ok.append(("adoption date: one Date: line is read; two are refused",
                   one and refused(lambda: adoption_date(pathlib.Path(t0)))))
    # The dossier sign-off's route edits quote two of these forms; they must agree.
    edits = (ROOT / CAND / "POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-ROUTE-EDITS.txt").read_text()
    blocks = re.findall(r"(?m)^----\n(.*?)\n----$", edits, re.S)
    leads = list(README_LEADS.items())
    ok.append(("the dossier route edits' block 2 writes the lead this step reads, and 2b is this step's",
               leads[1][0] in blocks and leads[2][0] in blocks
               and leads[1][1] in blocks and leads[2][1] in blocks))
    ok.extend(reconcile_selftests())
    return ok


def reconcile_selftests() -> list[tuple[str, bool]]:
    """The reconcile step runs last, and its check mode sees a stale census (R-365-3 N3)."""
    global J
    names = [name for name, _fn in STEPS]
    ok = [("steps: reconcile is a step and runs last, after profile",
           names[-2:] == ["profile", "reconcile"]
           and dict(STEPS)["reconcile"] is step_reconcile)]
    sys.path.insert(0, str(ROOT / "scripts"))
    import check_spec_reconciliation as recon
    with tempfile.TemporaryDirectory() as t0:
        tree = pathlib.Path(t0)
        recon.scratch(ROOT, tree)
        fresh = step_reconcile(tree, False)
        census = tree / recon.CENSUS
        census.write_text(census.read_text().replace("\n", "\n ", 1))
        stale = step_reconcile(tree, False)
        saved, J = J, Journal()
        try:
            wrote = step_reconcile(tree, True)
        finally:
            J = saved
        ok.append(("reconcile: check mode reports nothing on a current tree, "
                   "the stale census, and write mode regenerates it",
                   fresh is False and stale is True and wrote is True
                   and step_reconcile(tree, False) is False))
    return ok


def selftest() -> int:
    ok: list[tuple[str, bool]] = []
    both = {"a": PERFORMED_COMMON + (ROUTE_A, EGRESS_V2), "b": PERFORMED_COMMON + (ROUTE_B, EGRESS_V2, EGRESS_V1)}
    ok.append(("registrations code defines and calls its function",
               registrations_code(both["a"]).count(REGISTRATIONS_MARK) == 2))
    for route, perf in both.items():
        ok.append((f"route {route}: every performed record is registered once",
                   all(registrations_code(perf).count(rec) == 1 for _l, rec, _m in perf)))
        ok.append((f"route {route}: exemptions cover every performed record",
                   all(exemptions_code(perf).count(rec) == 1 for _l, rec, _m in perf)))
    sample = "X = 1\n" + EXEMPTION_DICT + "\n    (1, 2): 3,\n}\nY = 2\n"
    got = add_exemptions(sample, "    (4, 5): 6,\n")
    ok.append(("exemption rows land inside the dict", got.index("(4, 5)") < got.index("}\nY")
               and got.index("(1, 2)") < got.index("(4, 5)")))
    jr = Journal()
    with tempfile.TemporaryDirectory() as t0:
        f1 = pathlib.Path(t0) / "a.txt"
        f2 = pathlib.Path(t0) / "new.txt"
        f1.write_text("old")
        jr.write(f1, "new")
        jr.write(f2, "created")
        jr.restore()
        ok.append(("a journal restores a changed file and removes a created one",
                   f1.read_text() == "old" and not f2.exists()))
    ok.append(("every required record is a performed record or the rfc5 act",
               {pathlib.PurePosixPath(r).name for r in REQUIRED_RECORDS}
               == {rec for _l, rec, _m in PERFORMED_COMMON}
               | {pathlib.PurePosixPath(RFC5_ACT).name, pathlib.PurePosixPath(SCOPE_ACT).name,
                  "POLARIS-NON-GOVERNED-NARRATIVE-PROFILE-ADOPTION.md"}))
    ok.append(("number words round-trip the spelled range",
               [number_word(n) for n in (7, 19, 20, 69, 70, 73)]
               == ["seven", "nineteen", "twenty", "sixty-nine", "seventy", "seventy-three"]))
    try:
        number_word(100)
        ok.append(("a count past ninety-nine is refused", False))
    except Refusal:
        ok.append(("a count past ninety-nine is refused", True))
    rec = ('that opened "Q one" by selecting the\n| "L" | "D d" |\n')
    cmd, _st = battery_lines(rec, "a" * 64, "2026-10-04")
    ok.append(("battery line carries the owner's selection text",
               "--question-opening 'Q one' --selection-label 'L' --selection-description 'D d'" in cmd))
    try:
        battery_lines('that opened "Q: x" by selecting the\n| "L" | "D" |\n', "a" * 64, "2026-10-04")
        ok.append(("selection text a workflow line cannot carry is refused", False))
    except Refusal:
        ok.append(("selection text a workflow line cannot carry is refused", True))
    st = ("## How to verify this page\n```sh\n"
          "python3 scripts/build_pwb_behavior_contract_repin.py --check   # x\n"
          "python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy abc --date d\n"
          "python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest\n```\n"
          "The three checks above are the same three the hosted workflow runs.\n")
    wf = ("      - name: build_pwb_behavior_contract_repin --check\n"
          "        run: python3 scripts/build_pwb_behavior_contract_repin.py --check\n\n"
          "      - name: record_pwb_behavior_contract_repin_acts --check policy\n"
          "        run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --check policy abc --date d\n\n"
          "      - name: record_pwb_behavior_contract_repin_acts --selftest\n"
          "        run: python3 scripts/record_pwb_behavior_contract_repin_acts.py --selftest\n")
    ns, nw = edit_battery(st, wf, "python3 scripts/record_public_source_screening_scope_act.py --check z",
                          "python3 scripts/record_public_source_screening_scope_act.py --selftest")
    ok.append(("battery edit drops two lines, adds two, and respells the count",
               "The three checks above are the same three" in ns and ns.count("python3 ") == 3
               and nw.count("run: python3") == 3 and "--check policy" not in ns + nw))
    ok.append(("battery edit is idempotent", edit_battery(ns, nw, "x", "y") == (ns, nw)))
    ok.extend(policy_selftests())
    try:
        once("a b a", "a", "x")
        ok.append(("a repeated anchor is refused", False))
    except Refusal:
        ok.append(("a repeated anchor is refused", True))
    try:
        once("a b", "z", "x")
        ok.append(("an absent anchor is refused", False))
    except Refusal:
        ok.append(("an absent anchor is refused", True))
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        ok.append(("an empty tree is refused for every record and for the provider route",
                   missing_records(root)[:len(REQUIRED_RECORDS)] == list(REQUIRED_RECORDS)
                   and len(missing_records(root)) == len(REQUIRED_RECORDS) + 2))
        ok.append(("refusal writes nothing", run(root, True) == 2 and not any(root.iterdir())))
        act = root / RFC5_ACT
        act.parent.mkdir(parents=True)
        for good, name in (("Act instant: 2026-10-04T10:00:00Z\n", "single instant"),
                           ("", "no instant"),
                           ("Act instant: 2026-10-04T10:00:00Z\nAct instant: 2026-10-04T11:00:00Z\n", "two instants"),
                           ("Act instant: 2026-10-04 10:00\n", "malformed instant")):
            act.write_text("# x\n" + good)
            try:
                rfc5_precondition(root)
                passed = True
            except Refusal:
                passed = False
            ok.append((f"act instant precondition: {name}", passed == (name == "single instant")))
    with tempfile.TemporaryDirectory() as t:
        root = pathlib.Path(t)
        good = b"rfc five text\n"
        arg = sha(good)
        (root / RFC5_ACT).parent.mkdir(parents=True)
        (root / RFC5_ACT).write_text(f"# x\nExact digest (SHA-256): `{arg}`\n")
        ok.append(("the row-7 act argument is read from its record", rfc5_act_argument(root) == arg))
        (root / RFC5_ACT).write_text(f"# x\nExact digest (SHA-256): `{arg}`\nExact digest (SHA-256): `{arg}`\n")
        try:
            rfc5_act_argument(root)
            ok.append(("two argument lines in the row-7 record are refused", False))
        except Refusal:
            ok.append(("two argument lines in the row-7 record are refused", True))
        mods = [root / ".syzygy/governance/contracts" / m / "RFC-0005/consent-egress-secrets.md"
                for m in ("rfcs", "candidates/rfcs")]
        for m in mods:
            m.parent.mkdir(parents=True)
            m.write_bytes(good)
        rfc5_installed_matches(root, arg)
        ok.append(("installed RFC-0005 bytes equal to the act argument pass", True))
        for which in (0, 1):
            mods[which].write_bytes(good + b"x")
            try:
                rfc5_installed_matches(root, arg)
                ok.append((f"a mirror {which} not hashing to the act argument is refused", False))
            except Refusal:
                ok.append((f"a mirror {which} not hashing to the act argument is refused", True))
            mods[which].write_bytes(good)
        mods[1].unlink()
        try:
            rfc5_installed_matches(root, arg)
            ok.append(("a missing mirror is refused", False))
        except Refusal:
            ok.append(("a missing mirror is refused", True))
    ok.extend(egress_selftests())
    ok.extend(profile_figure_selftests())
    failed = [n for n, g in ok if not g]
    for n, g in ok:
        print(("ok   " if g else "FAIL ") + n)
    print(f"selftest: {len(ok) - len(failed)} of {len(ok)} predicates held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=str(ROOT))
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    return run(pathlib.Path(a.root), write=not a.check)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
