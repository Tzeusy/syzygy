#!/usr/bin/env python3
"""Repository-wide governance checks for Syzygy — read-only, portable.

Run from the repository root:

    python3 scripts/check_governance.py

Exit status: 0 = no findings, 1 = at least one FAIL finding, 2 = usage error.

Design constraints (charter §17, "public, portable validation"):

  * **Repository-relative.** The repo root is derived from this file's own
    location; no founder-machine absolute path appears anywhere.
  * **Standard library only**, Python 3.9+. No installs, no network.
  * **Read-only.** This script never writes, moves, or rewrites a governance
    artifact. When a check finds a defect it *reports* it; correcting a
    normative artifact is a human act under the normative-change workflow.
  * **Every summary line states its denominator.** A check that examined zero
    items reports WARN — "PASS over nothing examined" is the failure mode this
    project exists to prevent (VIS-2: no evidence yields Unknown, never green).
  * **Allowlists are declared inline, counted, and printed.** A silent
    exemption is indistinguishable from a missing check.

Checks
------
  CG-1   internal links and path references resolve
  CG-2   retired acceptance phrase / `about/` authority path absent from
         active instructions
  CG-3   stale bootstrap routing (`_bootstrap/prompts/`) absent
  CG-4   candidate homes carry candidate banners
  CG-5   canonical craft banners are truthful
  CG-6   accepted homes do not exist yet (created only by owner acts)
  CG-7   ACTIVE-CONTRACT-MANIFEST digests are valid, and the acceptance
         record's act-1 argument still matches the manifest
  CG-8   context budgets reported (never enforced — charter §11.4 triggers)
  CG-9   duplicate authority homes absent
  CG-10  pending-decision register as-of line reported
  CG-11  `.syzygy/cache/` and `.syzygy/local/` are git-ignored
  CG-12  no active artifact cites a `_bootstrap/` path as a required source

Status vocabulary: OK (examined > 0, no findings) · WARN (nothing examined, or
a report-only observation) · FAIL (findings that fail the run).
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_REL = os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, "/")

CANDIDATES = ".syzygy/governance/contracts/candidates"
TOPOLOGY_CANDIDATES = ".syzygy/map/topology-candidates"
CRAFT = ".syzygy/governance/policies/craft-and-care"
DOCTRINE = ".syzygy/governance/doctrine"
DECISIONS = ".syzygy/governance/decisions"


# --------------------------------------------------------------- results

class Results:
    """One summary line per check, plus finding detail lines beneath it."""

    def __init__(self):
        self.summaries = []
        self._fail = False

    def add(self, status, name, examined, findings, unit="item",
            note=None, details=()):
        if status == "FAIL":
            self._fail = True
        self.summaries.append((status, name, examined, findings, unit, note,
                               list(details)))

    def failed(self):
        return self._fail

    @staticmethod
    def _plural(n, unit):
        if n == 1:
            return unit
        return unit[:-1] + "ies" if unit.endswith("y") else unit + "s"

    def report(self):
        for status, name, examined, findings, unit, note, details in self.summaries:
            line = (f"{status:4s}  {name} — {examined} "
                    f"{self._plural(examined, unit)} examined, "
                    f"{findings} finding{'' if findings == 1 else 's'}")
            if note:
                line += f" — {note}"
            print(line)
            for d in details:
                print(f"        {d}")
        n_fail = sum(1 for s, *_ in self.summaries if s == "FAIL")
        n_warn = sum(1 for s, *_ in self.summaries if s == "WARN")
        n_ok = sum(1 for s, *_ in self.summaries if s == "OK")
        print(f"\n{n_ok} OK, {n_warn} WARN, {n_fail} FAIL "
              f"({len(self.summaries)} checks) — counts derived, not asserted")


# --------------------------------------------------------------- corpus

def _git(*args):
    try:
        out = subprocess.run(["git", "-C", ROOT, *args],
                             capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    return out.stdout.splitlines()


def corpus_paths(scope):
    """Repo-relative paths a clone would (or will) contain.

    `tracked` is `git ls-files`. The default `clone` scope adds untracked
    files that are not git-ignored — the candidate governance package is
    exactly that today, and a tracked-only corpus would give checks CG-4,
    CG-7, CG-8, CG-9 and CG-12 a **zero denominator**, i.e. a vacuous pass
    over the material those checks exist for. Both counts are printed so the
    scope is never implicit.

    Returns (paths, tracked_set, source). `source` is "git" normally and
    "walk" when git is unavailable — an exported or archived copy of the
    tree, where the corpus is a filesystem walk and *nothing is known to be
    tracked*. The walk is a degraded mode, printed as such: it cannot honor
    `--scope tracked` and it cannot distinguish ignored files, so CG-11 is
    reported Unknown rather than passed.
    """
    tracked = _git("ls-files")
    if tracked is None:
        walked = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames
                           if d not in {".git", "__pycache__", "node_modules"}]
            for fn in filenames:
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                walked.append(rel.replace(os.sep, "/"))
        return sorted(walked), set(), "walk"
    tracked = [p for p in tracked if p]
    if scope == "tracked":
        return sorted(set(tracked)), set(tracked), "git"
    others = _git("ls-files", "--others", "--exclude-standard") or []
    return (sorted(set(tracked) | {p for p in others if p}),
            set(tracked), "git")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def md_files(paths):
    return [p for p in paths if p.endswith(".md")]


def words(rel):
    return len(read(rel).split())


# --------------------------------------------------------------- CG-1

MD_LINK = re.compile(r"\[[^\]]*\]\(\s*(?P<t>[^)\s]+)")
#: Path references in this corpus are overwhelmingly inline code spans, not
#: markdown links (39 relative links against 478 code-span paths at the time
#: of writing). A link-only check would report a confident PASS over ~8% of
#: the population that can actually dangle.
CODE_PATH = re.compile(r"`(?P<t>[A-Za-z0-9_.\-/]+\.(?:md|py|sh|ya?ml|json|txt))`")
EXTERNAL = ("http://", "https://", "mailto:", "ftp://")

#: Artifacts that do not exist yet **by design** — an owner act creates them,
#: or they belong to a governed project that does not exist. A reference to
#: one is correct, not broken. Declared, counted, and printed on every run.
FORWARD_REFS = (
    ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md",  # created by act 1
    ".syzygy/governance/contracts/rfcs/",                     # act-1 install home
    ".syzygy/map/topology/",                                  # act-3 install home
    ".syzygy/project.yaml",                                   # no governed project yet
    "openspec/",                                              # does not exist yet
    "RFC-000n",                                               # glob placeholder
)


#: Target *shapes* that name the frozen rev9 working packet — a tree that
#: lived under the git-excluded `_bootstrap/` and whose internal layout these
#: derivation records cite relatively (`final-prespec/…`, `../rfcs/RFC-0007-
#: polaris-intent-surface.md`, `reviews/08-…`). Such a reference is
#: unresolvable in a clone by construction, which is a §18 observation about
#: history, not a broken pointer in active material. Classified — not
#: silenced: every one is printed under CG-1b-history.
HISTORICAL_PACKET_TARGET = (
    re.compile(r"^(\.\./)*final-prespec/"),
    re.compile(r"^(\.\./)*rfcs/RFC-\d{4}-[a-z0-9-]+\.md$"),
    re.compile(r"^(\.\./)*(topology|history|matrix-rows)/"),
    re.compile(r"^(\.\./)*reviews/\d{2}-"),
    re.compile(r"^(\.\./)*scripts/verify_(rfcs|rev7)\.(py|sh)$"),
)


def _is_forward(target):
    return any(f in target for f in FORWARD_REFS)


def _is_historical_packet(target):
    return any(p.match(target) for p in HISTORICAL_PACKET_TARGET)


def _resolve(citing, target, all_paths):
    """Resolve relative to the citing file, to the repo root, or as a suffix.

    Path references here are written as *citations* — `RFC-0002/README.md`
    cited from a package report means the module of that name, wherever the
    package keeps it — so suffix matching models how they are actually
    written. Anything resolving only by suffix still resolves in a clone.
    """
    for cand in (os.path.join(os.path.dirname(citing), target),
                 os.path.join(ROOT, target)):
        if os.path.exists(os.path.normpath(os.path.join(ROOT, cand)
                                           if not os.path.isabs(cand) else cand)):
            return True
    t = os.path.normpath(target).replace(os.sep, "/").lstrip("./")
    if not t:
        return False
    return any(p == t or p.endswith("/" + t) for p in all_paths)


def cg1_links(paths, res):
    all_paths = set(paths)
    n_links = n_paths = 0
    broken_links, broken_paths, forward, historical = [], [], set(), []
    for rel in md_files(paths):
        txt = read(rel)
        for m in MD_LINK.finditer(txt):
            t = m.group("t").split("#")[0].strip()
            if not t or t.startswith(EXTERNAL):
                continue
            n_links += 1
            if _is_forward(t):
                forward.add(t)
                continue
            if not _resolve(rel, t, all_paths):
                broken_links.append(f"{rel} -> {t}")
        for m in CODE_PATH.finditer(txt):
            t = m.group("t")
            if "/" not in t or t.startswith(EXTERNAL):
                continue
            # `_bootstrap/**` is git-excluded by design; CG-12 owns it.
            if t.startswith("_bootstrap/"):
                continue
            n_paths += 1
            if _is_forward(t):
                forward.add(t)
                continue
            if not _resolve(rel, t, all_paths):
                if _is_historical_packet(t):
                    historical.append(f"{rel} -> {t}")
                else:
                    broken_paths.append(f"{rel} -> {t}")

    if n_links == 0:
        res.add("WARN", "CG-1a  markdown links resolve", 0, 0, "link",
                note="nothing examined — check verified nothing")
    else:
        res.add("FAIL" if broken_links else "OK", "CG-1a  markdown links resolve",
                n_links, len(broken_links), "link",
                details=sorted(set(broken_links)))
    if n_paths == 0:
        res.add("WARN", "CG-1b  code-span path references resolve", 0, 0, "reference",
                note="nothing examined — check verified nothing")
    else:
        res.add("FAIL" if broken_paths else "OK",
                "CG-1b  code-span path references resolve",
                n_paths, len(broken_paths), "reference",
                details=sorted(set(broken_paths)))
    res.add("WARN", "CG-1c  declared forward references", len(forward), 0, "target",
            note="skipped by design — an owner act creates these",
            details=sorted(forward))
    uniq_hist = sorted(set(historical))
    res.add("WARN", "CG-1d  frozen-packet references", len(uniq_hist), 0,
            "reference",
            note="unresolvable in a clone by construction — the rev9 working "
                 "packet lived under the git-excluded `_bootstrap/`",
            details=uniq_hist)


# --------------------------------------------------------------- CG-2

RETIRED_PHRASE = "ACCEPT FOUNDATIONAL RFCS"

#: A retirement notice must be able to name the phrase it retires, and the
#: historical record must be able to quote what was superseded. Allowlisted
#: by path prefix, each with the reason it is allowed to carry the phrase.
RETIRED_PHRASE_ALLOW = (
    (f"{CRAFT}/INSTALL-RECORD.md", "states the phrase is retired and satisfies nothing"),
    (f"{CANDIDATES}/round-2026-08/", "this round's process record and delta register"),
    (f"{CANDIDATES}/history/", "frozen rev9 corpus and per-RFC amendment history"),
    (f"{CANDIDATES}/reviews/", "raw reviewer output, stored verbatim"),
    (f"{CANDIDATES}/00-README.md", "records the phrase as retired at rev10"),
    (f"{CANDIDATES}/10-EXIT-REPORT.md", "records the phrase as retired at rev10"),
    (f"{CANDIDATES}/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md",
     "the acceptance record that retires it"),
    (f"{DECISIONS}/OWNER-ANSWERS-2026-08-01.md",
     "owner ruling that the phrase was not performed"),
    ("AGENTS.md", "states the phrase is retired and satisfies nothing"),
    (f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
     "owner-supplied round charter; quotes the phrase as a search token"),
    (SELF_REL, "this checker names the phrase in order to detect it"),
)

#: `about/**` is the upstream skill convention; this repository deliberately
#: has no such tree. Naming it as *guidance not to create one*, or as a
#: historical divergence note, is correct. Naming it as an authority path is
#: the defect.
ABOUT_SCOPE = ("AGENTS.md", "README.md")
ABOUT_ALLOW = (
    (".claude/skills/heart-and-soul/SKILL.md", "no-about/-tree guidance"),
    (".codex/skills/heart-and-soul/SKILL.md", "no-about/-tree guidance"),
    (f"{CRAFT}/README.md", "historical note on the upstream pillar home"),
)
ABOUT_PAT = re.compile(r"(?<![\w/.-])about/")


def _allow_hit(rel, allow):
    for prefix, reason in allow:
        if rel == prefix or rel.startswith(prefix):
            return reason
    return None


def cg2_retired_tokens(paths, res):
    files = [p for p in paths
             if p.endswith((".md", ".txt", ".yaml", ".yml", ".py"))]
    findings, allowed = [], []
    for rel in files:
        txt = read(rel)
        if RETIRED_PHRASE not in txt:
            continue
        reason = _allow_hit(rel, RETIRED_PHRASE_ALLOW)
        lines = [i for i, ln in enumerate(txt.splitlines(), 1)
                 if RETIRED_PHRASE in ln]
        if reason:
            allowed.append(f"{rel}:{','.join(str(i) for i in lines)} — {reason}")
        else:
            findings += [f"{rel}:{i} — retired phrase outside the allowlist"
                         for i in lines]
    res.add("FAIL" if findings else "OK",
            "CG-2a  retired acceptance phrase confined", len(files),
            len(findings), "file", details=findings)
    res.add("WARN", "CG-2b  retired-phrase allowlist", len(allowed), 0, "file",
            note="declared historical/quoting contexts", details=sorted(allowed))

    scope = [p for p in ABOUT_SCOPE if p in set(paths)]
    hits = []
    for rel in scope:
        for i, ln in enumerate(read(rel).splitlines(), 1):
            if ABOUT_PAT.search(ln):
                hits.append(f"{rel}:{i} — `about/` named in an instruction file")
    res.add("FAIL" if hits else ("OK" if scope else "WARN"),
            "CG-2c  `about/` absent from AGENTS/README", len(scope),
            len(hits), "file",
            note=None if scope else "neither file present — nothing examined",
            details=hits)
    allow_present = [f"{p} — {r}" for p, r in ABOUT_ALLOW if p in set(paths)]
    res.add("WARN", "CG-2d  `about/` allowlist", len(allow_present), 0, "file",
            note="guidance and historical mentions, out of CG-2c scope",
            details=allow_present)


# --------------------------------------------------------------- CG-3

STALE_ROUTES = ("_bootstrap/prompts/",)


def cg3_stale_routing(paths, res):
    files = [p for p in paths if p.endswith((".md", ".txt", ".yaml", ".yml"))]
    findings = []
    for rel in files:
        if rel == SELF_REL:
            continue
        for i, ln in enumerate(read(rel).splitlines(), 1):
            for route in STALE_ROUTES:
                if route in ln:
                    findings.append(f"{rel}:{i} — routes to `{route}`")
    res.add("FAIL" if findings else "OK",
            "CG-3   stale bootstrap routing absent", len(files),
            len(findings), "file", details=findings)


# --------------------------------------------------------------- CG-4

BANNER_LINES = 10
#: A manifest is a digest list; a banner would change its digest surface, and
#: the acceptance record owns its candidate status.
BANNER_EXEMPT = (f"{TOPOLOGY_CANDIDATES}/BUNDLE-MANIFEST.md",)


def cg4_candidate_banners(paths, res):
    targets = []
    top_readme = f"{CANDIDATES}/00-README.md"
    if top_readme in set(paths):
        targets.append(top_readme)
    #: Topology bundle members are digest-bound by BUNDLE-MANIFEST.md (the
    #: act-3 subject); stuffing a banner word into each member would churn
    #: the offered digest for labeling alone. The directory-level candidate
    #: marker (TRACKING-NOTE.md, outside the member set) satisfies CG-4 for
    #: the members, provided it exists and itself carries the banner.
    topology_note = f"{TOPOLOGY_CANDIDATES}/TRACKING-NOTE.md"
    topology_note_ok = (topology_note in set(paths)
                        and "candidate" in "\n".join(
                            read(topology_note).splitlines()[:BANNER_LINES]).lower())
    for rel in paths:
        if rel.startswith(f"{CANDIDATES}/policy-candidates/") and rel.endswith(".md"):
            targets.append(rel)
        elif (rel.startswith(f"{TOPOLOGY_CANDIDATES}/") and rel.endswith(".md")
              and rel not in BANNER_EXEMPT):
            if rel == topology_note or not topology_note_ok:
                targets.append(rel)
    if topology_note in set(paths) and topology_note not in targets:
        targets.append(topology_note)
    findings = []
    for rel in sorted(set(targets)):
        head = "\n".join(read(rel).splitlines()[:BANNER_LINES]).lower()
        if "candidate" not in head:
            findings.append(f"{rel} — no 'candidate' in the first "
                            f"{BANNER_LINES} lines")
    status = "FAIL" if findings else ("OK" if targets else "WARN")
    res.add(status, "CG-4   candidate homes carry candidate banners",
            len(set(targets)), len(findings), "file",
            note=None if targets else "no candidate-home files found — nothing examined",
            details=findings)


# --------------------------------------------------------------- CG-5

FALSE_BANNERS = (
    "this copy is the bootstrap-phase record",
    "this file is the bootstrap-phase record",
    "this directory is the bootstrap-phase record",
)
CANONICAL_MARK = "canonical home"
BANNER_POSITIVE_LINES = 3
#: The install record is provenance, not a policy banner: it describes where
#: the policies came from and is expected to name the bootstrap-phase copy.
CRAFT_POSITIVE_EXEMPT = (f"{CRAFT}/INSTALL-RECORD.md",)


def cg5_craft_banners(paths, res):
    craft_files = sorted(p for p in paths
                         if p.startswith(f"{CRAFT}/") and p.endswith(".md"))
    findings = []
    for rel in craft_files:
        low = read(rel).lower()
        for bad in FALSE_BANNERS:
            if bad in low:
                findings.append(f"{rel} — claims \"{bad}\" at the canonical home")
        if rel in CRAFT_POSITIVE_EXEMPT:
            continue
        head = "\n".join(read(rel).splitlines()[:BANNER_POSITIVE_LINES]).lower()
        if CANONICAL_MARK not in head:
            findings.append(f"{rel} — banner does not name this the "
                            f"{CANONICAL_MARK} in its first "
                            f"{BANNER_POSITIVE_LINES} lines")
    status = "FAIL" if findings else ("OK" if craft_files else "WARN")
    res.add(status, "CG-5   canonical craft banners truthful", len(craft_files),
            len(findings), "file",
            note=None if craft_files else "craft tree absent — nothing examined",
            details=findings)


# --------------------------------------------------------------- CG-6

ACCEPTED_HOMES = (
    (".syzygy/governance/contracts/rfcs", "created only by owner act 1"),
    (".syzygy/map/topology", "created only by owner act 3"),
)


def cg6_accepted_homes(res):
    findings = []
    for rel, why in ACCEPTED_HOMES:
        if os.path.exists(os.path.join(ROOT, rel)):
            findings.append(f"{rel} exists — {why}; no act has been recorded")
    res.add("FAIL" if findings else "OK",
            "CG-6   accepted homes not yet created", len(ACCEPTED_HOMES),
            len(findings), "home", details=findings)


# --------------------------------------------------------------- CG-7

MANIFEST = f"{CANDIDATES}/ACTIVE-CONTRACT-MANIFEST.txt"
DIGEST_ROW = re.compile(r"^(?P<sha>[0-9a-f]{64})\s+(?P<path>\S.*)$")
#: The manifest's *own* sha256 is the argument of owner act 1, so the
#: acceptance record and the manifest must agree. They are edited by
#: different hands at different times; nothing but a check keeps them
#: together.
ACCEPTANCE_RECORD = f"{CANDIDATES}/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md"
ACT1_ARG = re.compile(r"ACCEPT COMPACTED FOUNDATIONAL RFCS:\s*(?P<sha>[0-9a-f]{64})")


def sha256_file(abspath):
    h = hashlib.sha256()
    with open(abspath, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cg7_manifest(paths, res):
    if MANIFEST not in set(paths):
        res.add("WARN", "CG-7a  manifest digests valid", 0, 0, "entry",
                note=f"{MANIFEST} not present — nothing examined")
        res.add("WARN", "CG-7b  act-1 argument matches the manifest", 0, 0,
                "record", note="no manifest to compare against — nothing examined")
        return
    findings, n = [], 0
    for i, ln in enumerate(read(MANIFEST).splitlines(), 1):
        m = DIGEST_ROW.match(ln.strip())
        if not m:
            continue
        n += 1
        target = os.path.join(ROOT, CANDIDATES, m.group("path").strip())
        if not os.path.exists(target):
            findings.append(f"{MANIFEST}:{i} — {m.group('path')} does not exist")
            continue
        actual = sha256_file(target)
        if actual != m.group("sha"):
            findings.append(f"{MANIFEST}:{i} — {m.group('path')} digest "
                            f"{actual[:12]}… != manifest {m.group('sha')[:12]}…")
    manifest_sha = sha256_file(os.path.join(ROOT, MANIFEST))
    status = "FAIL" if findings else ("OK" if n else "WARN")
    res.add(status, "CG-7a  manifest digests valid", n, len(findings), "entry",
            note=(f"manifest sha256 {manifest_sha} (the act-1 argument)"
                  if n else "no digest rows parsed — nothing examined"),
            details=findings)

    if ACCEPTANCE_RECORD not in set(paths):
        res.add("WARN", "CG-7b  act-1 argument matches the manifest", 0, 0,
                "record", note=f"{ACCEPTANCE_RECORD} not present — nothing examined")
        return
    stated = ACT1_ARG.findall(read(ACCEPTANCE_RECORD))
    if not stated:
        res.add("WARN", "CG-7b  act-1 argument matches the manifest", 1, 0,
                "record", note="no `ACCEPT COMPACTED FOUNDATIONAL RFCS: <sha>` "
                               "found — nothing compared")
        return
    bad = [s for s in set(stated) if s != manifest_sha]
    res.add("FAIL" if bad else "OK", "CG-7b  act-1 argument matches the manifest",
            len(set(stated)), len(bad), "argument",
            details=[f"{ACCEPTANCE_RECORD} offers {s[:12]}… but the manifest "
                     f"now hashes to {manifest_sha[:12]}… — the act would bind "
                     f"a package that no longer exists" for s in sorted(bad)])

    # CG-7c — the other three digest-bound acts. Act 1 alone was checked until
    # 2026-08-05, so a truthful "1 examined" covered a population of 4 and
    # three stale act arguments passed unseen (round review RB-3 F1).
    record = read(ACCEPTANCE_RECORD)
    others = [
        ("act 2 (craft CC-TEST-2)",
         os.path.join(ROOT, CRAFT, "testing-and-verification.md"),
         re.compile(r"CC-TEST-2@([0-9a-f]{64})")),
        ("act 3 (topology bundle)",
         os.path.join(ROOT, TOPOLOGY_CANDIDATES, "BUNDLE-MANIFEST.md"),
         re.compile(r"ACCEPT TOPOLOGY:\s*`?([0-9a-f]{64})")),
        ("act 4 (project overview)",
         os.path.join(ROOT, ".syzygy/intent/OVERVIEW.md"),
         re.compile(r"ADOPT PROJECT OVERVIEW:\s*`?([0-9a-f]{64})")),
    ]
    findings, examined = [], 0
    for label, subject, pat in others:
        args = set(pat.findall(record))
        if not args:
            findings.append(f"{label} — no digest argument found in "
                            f"{ACCEPTANCE_RECORD}; the act cannot be performed "
                            f"as written")
            examined += 1
            continue
        if not os.path.exists(subject):
            findings.append(f"{label} — subject {subject} does not exist")
            examined += len(args)
            continue
        actual = sha256_file(subject)
        for a in sorted(args):
            examined += 1
            if a != actual:
                findings.append(f"{label} — record offers {a[:12]}… but the "
                                f"subject hashes to {actual[:12]}… — the act "
                                f"would bind an artifact state that no longer "
                                f"exists")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-7c  acts 2/3/4 arguments match their subjects",
            examined, len(findings), "argument",
            note=None if examined else "no act arguments found — nothing examined",
            details=findings)

    cg7d_quoted_elsewhere(paths, res)


#: Every act phrase, with the artifact whose sha256 is its only valid
#: argument. CG-7d applies these to *every* file in the corpus, because the
#: round's headline defect was a digest that was correct in the manifest and
#: stale in the document that offered it (six independent reviewers, RB-1 F1
#: … RB-8 F1). A digest quoted anywhere is a promise about an artifact; the
#: artifact is the only thing that can keep it.
ACT_SUBJECTS = (
    ("ACCEPT COMPACTED FOUNDATIONAL RFCS", MANIFEST,
     re.compile(r"ACCEPT COMPACTED FOUNDATIONAL RFCS:\s*`?([0-9a-f]{64})")),
    ("CONFIRM CRAFT AMENDMENT: CC-TEST-2",
     f"{CRAFT}/testing-and-verification.md",
     re.compile(r"CC-TEST-2@([0-9a-f]{64})")),
    ("ACCEPT TOPOLOGY", f"{TOPOLOGY_CANDIDATES}/BUNDLE-MANIFEST.md",
     re.compile(r"ACCEPT TOPOLOGY:\s*`?([0-9a-f]{64})")),
    ("ADOPT PROJECT OVERVIEW", ".syzygy/intent/OVERVIEW.md",
     re.compile(r"ADOPT PROJECT OVERVIEW:\s*`?([0-9a-f]{64})")),
)

#: Files that quote a stale act argument *as* a retired value, on purpose —
#: the revision table in the acceptance record and the round's own records.
#: They are read as history, so a mismatch there is the point, not a defect.
#: Raw reviewer output is never edited, so it is exempt by construction.
ACT_QUOTE_EXEMPT = (
    f"{CANDIDATES}/round-2026-08/reviews/",
    f"{CANDIDATES}/reviews/",
    f"{CANDIDATES}/history/",
    f"{CANDIDATES}/fixtures/",
    f"{CANDIDATES}/00-README.md",
    f"{CANDIDATES}/10-EXIT-REPORT.md",
    f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
    SELF_REL,
)


def cg7d_quoted_elsewhere(paths, res):
    """Any file quoting an act phrase must quote its subject's current digest.

    A digest is owned by the artifact it names. Quoting one elsewhere is
    convenience, and convenience goes stale silently — which is exactly how
    all four act arguments in the acceptance record came to offer packages
    that no longer existed. This check makes every copy load-bearing.
    """
    #: A digest that its own line calls retired/stale/superseded is history,
    #: not an offer. This is the one exemption granted per-line rather than
    #: per-file, so a record can keep what it used to offer without the
    #: keeping being read as an offer.
    retired = re.compile(r"\b(retired|stale|superseded|pre-amendment|"
                         r"historical)\b", re.I)
    #: The marker must sit in the 60 characters immediately *before* the
    #: quotation. A marker later in the line does not exempt it — the
    #: acceptance record's own rows say "the rev9 argument is stale" after
    #: offering the current one, and those offers must stay checked.
    LOOKBEHIND = 60
    subjects = {}
    for label, rel, pat in ACT_SUBJECTS:
        full = os.path.join(ROOT, rel)
        subjects[label] = sha256_file(full) if os.path.exists(full) else None
    findings, examined = [], 0
    for rel in paths:
        if any(rel.startswith(x) or rel == x for x in ACT_QUOTE_EXEMPT):
            continue
        if not rel.endswith(".md"):
            continue
        body = read(rel)
        if not body:
            continue
        for label, subj_rel, pat in ACT_SUBJECTS:
            for line_no, line in enumerate(body.splitlines(), 1):
                for m in pat.finditer(line):
                    arg = m.group(1)
                    if retired.search(line[max(0, m.start() - LOOKBEHIND):
                                           m.start()]):
                        continue
                    examined += 1
                    current = subjects[label]
                    if current is None:
                        findings.append(
                            f"{rel}:{line_no} — quotes `{label}` but its "
                            f"subject {subj_rel} does not exist")
                    elif arg != current:
                        findings.append(
                            f"{rel}:{line_no} — quotes `{label}: {arg[:12]}…` "
                            f"but {subj_rel} hashes to {current[:12]}… — this "
                            f"copy is stale")
    res.add("FAIL" if findings else ("OK" if examined else "WARN"),
            "CG-7d  act digests quoted anywhere match their subjects",
            examined, len(findings), "quotation",
            note=(None if examined else
                  "no act digest quoted outside the exempt history — "
                  "nothing examined"),
            details=findings)


# --------------------------------------------------------------- CG-8

#: Charter §11.4 review triggers. These are decomposition triggers, not
#: validity laws — reported, never enforced. They are deliberately tighter
#: than the 7,000-word hard ceiling that
#: `candidates/scripts/verify_final_prespec.py` enforces with declared
#: justifications; the two are different instruments, not a contradiction.
BUDGETS = (
    ("README.md", 1200, "root README review trigger"),
    ("AGENTS.md", 1500, "AGENTS review trigger"),
)
MODULE_TRIGGER = 4000
MODULE_DECOMPOSE = 5000


def cg8_budgets(paths, res):
    present = set(paths)
    lines, n = [], 0
    for rel, limit, label in BUDGETS:
        if rel not in present:
            continue
        n += 1
        w = words(rel)
        if w > limit:
            lines.append(f"{rel} — {w} words, over the {limit}-word {label} "
                         f"(§11.4 trigger; review, not failure)")
    modules = sorted(p for p in paths
                     if p.startswith(f"{CANDIDATES}/rfcs/") and p.endswith(".md"))
    for rel in modules:
        n += 1
        w = words(rel)
        if w > MODULE_DECOMPOSE:
            lines.append(f"{rel} — {w} words, above {MODULE_DECOMPOSE}: §11.4 "
                         f"focused decomposition review")
        elif w > MODULE_TRIGGER:
            lines.append(f"{rel} — {w} words, over the {MODULE_TRIGGER}-word "
                         f"active-module trigger (§11.4)")
    res.add("WARN" if (lines or n == 0) else "OK",
            "CG-8   context budgets reported", n, len(lines), "artifact",
            note=("report-only — §11.4 triggers are decomposition prompts, "
                  "not failures" if n else "nothing examined"),
            details=lines)


# --------------------------------------------------------------- CG-9

#: Each authority type has exactly one home. A second copy in the candidate
#: package is a duplicate authority home — the reader cannot tell which one
#: binds.
AUTHORITY_HOMES = (
    ("doctrine", DOCTRINE, ("/doctrine/",)),
    ("craft-and-care", CRAFT, ("/craft-and-care/",)),
)


def cg9_duplicate_homes(paths, res):
    findings, n = [], 0
    for label, home, markers in AUTHORITY_HOMES:
        for rel in paths:
            if not rel.endswith(".md"):
                continue
            if any(mk in "/" + rel for mk in markers):
                n += 1
                if not rel.startswith(home + "/"):
                    findings.append(f"{rel} — {label} material outside its one "
                                    f"home {home}/")
    status = "FAIL" if findings else ("OK" if n else "WARN")
    res.add(status, "CG-9   duplicate authority homes absent", n,
            len(findings), "file",
            note=None if n else "no authority-home files found — nothing examined",
            details=findings)


# --------------------------------------------------------------- CG-10

PENDING = f"{DECISIONS}/PENDING-OWNER-DECISIONS.md"
ASOF = re.compile(r"as[- ]of\b[^\n]*", re.I)


def cg10_pending_asof(paths, res):
    if PENDING not in set(paths):
        res.add("WARN", "CG-10  pending register as-of reported", 0, 0, "register",
                note=f"{PENDING} not present — nothing examined")
        return
    head = read(PENDING).splitlines()[:40]
    hits = [f"{PENDING}:{i} — {ASOF.search(ln).group(0).strip()}"
            for i, ln in enumerate(head, 1) if ASOF.search(ln)]
    if not hits:
        res.add("FAIL", "CG-10  pending register as-of reported", 1, 1, "register",
                details=[f"{PENDING} — no 'As-of' line in the first 40 lines"])
        return
    res.add("WARN", "CG-10  pending register as-of reported", 1, 0, "register",
            note="reported for human currency judgement, never auto-verified",
            details=hits)


# --------------------------------------------------------------- CG-11

MUST_IGNORE = (".syzygy/cache/", ".syzygy/local/")


def cg11_ignored(res):
    gi = os.path.join(ROOT, ".gitignore")
    if not os.path.exists(gi):
        res.add("FAIL", "CG-11  cache/local git-ignored", 0, 1, "pattern",
                details=[".gitignore is absent"])
        return
    txt = read(".gitignore")
    entries = {ln.strip() for ln in txt.splitlines() if ln.strip()}
    findings = [f"{p} not present in .gitignore" for p in MUST_IGNORE
                if p not in entries and p.rstrip("/") not in entries]
    res.add("FAIL" if findings else "OK", "CG-11  cache/local git-ignored",
            len(MUST_IGNORE), len(findings), "pattern", details=findings)


# --------------------------------------------------------------- CG-12

#: A `_bootstrap/` mention is acceptable when it marks the target as
#: historical, founder-local, or otherwise unavailable to a clone. It is a
#: finding when an active artifact points a reader there for meaning it
#: cannot get elsewhere.
BOOTSTRAP_MARKERS = (
    "histor", "founder-local", "excluded", "unavailable", "archive",
    "bootstrap record", "bootstrap-phase", "fd-021", "fd-037",
    "frozen", "verbatim", "preserved", "process mirror", "never edit",
    "do not load", "do not cite", "not a source", "extracted under",
    "invisible to clone", "before this round", "source:", "git-excluded",
    "machine-local", "prior draft", "supersede", "not authority",
    "bootstrap home",
)
#: A marker rarely lands on the same physical line as the path in wrapped
#: prose — "`_bootstrap/…/DIRECTIVE.md` (owner-supplied,\npreserved verbatim…)"
#: is one sentence across two lines, and a section heading that marks a whole
#: list ("Research corpus links (archived, non-authoritative)") sits two lines
#: above its first entry. The window is ±2 lines; anything needing more than
#: that is not marked clearly enough for a reader either.
#: Absence markers. A sentence that says the tree is *not* there, *not*
#: read, or deliberately removed is not a citation of it — the round's own
#: reports say so repeatedly, and Test E's whole subject is the absence.
#: Kept separate from the historical markers above because they justify a
#: mention for a different reason.
BOOTSTRAP_ABSENCE_MARKERS = (
    "no `_bootstrap", "no _bootstrap", "without `_bootstrap",
    "without _bootstrap", "-free clone", "remove access",
    "no access", "did not read", "does not read", "cannot read",
    "no hidden semantic dependency", "nothing under `_bootstrap",
)

MARKER_WINDOW = 2

#: A file may instead carry one prominent disclosure covering every pointer in
#: it — the pending-decision register does exactly this. Recognised only near
#: the top, where a reader meets it before the pointers.
DISCLOSURE_LINES = 40
DISCLOSURE_MARKERS = ("git-excluded", "founder-local", "absent from clones",
                      "unavailable", "cannot resolve those pointers")


def _has_file_disclosure(all_lines):
    head = all_lines[:DISCLOSURE_LINES]
    for i, ln in enumerate(head):
        if "_bootstrap/" not in ln:
            continue
        window = "\n".join(head[max(0, i - 2):i + 3]).lower()
        if any(mk in window for mk in DISCLOSURE_MARKERS):
            return window.strip().splitlines()[0][:80]
    return None
#: Derivation and archive subtrees: their whole job is to name the frozen
#: rev9 inputs a clause was migrated from. Allowlisted by prefix, counted,
#: printed.
BOOTSTRAP_ALLOW_PREFIX = (
    (f"{CANDIDATES}/history/", "frozen rev9 corpus and amendment history"),
    (f"{CANDIDATES}/reviews/", "raw reviewer output, stored verbatim"),
    (f"{CANDIDATES}/round-2026-08/reviews/",
     "raw reviewer output, stored verbatim — never edited, so a reviewer's "
     "own mention of the excluded tree (usually to record that they did not "
     "read it) is evidence, not an active citation"),
    (f"{CANDIDATES}/matrix-rows/", "per-RFC clause-migration provenance rows"),
    (f"{CANDIDATES}/04-CLAUSE-MIGRATION-MATRIX.md",
     "clause-migration provenance, cites frozen rev9 sources by construction"),
    (f"{CANDIDATES}/COMPACTION-CHARTER.md",
     "the superseded round's own working charter"),
    (f"{CANDIDATES}/round-2026-08/OWNER-ROUND-CHARTER.md",
     "owner-supplied round charter, quoted verbatim"),
    (SELF_REL, "this checker names the path in order to detect it"),
)


def cg12_bootstrap_sources(paths, res):
    files = [p for p in paths if p.endswith((".md", ".txt", ".yaml", ".yml"))]
    findings, allowed_files = [], []
    n_lines = 0
    for rel in files:
        reason = _allow_hit(rel, BOOTSTRAP_ALLOW_PREFIX)
        all_lines = read(rel).splitlines()
        hit_lines = [(i, ln) for i, ln in enumerate(all_lines, 1)
                     if "_bootstrap/" in ln]
        if not hit_lines:
            continue
        if not reason and _has_file_disclosure(all_lines):
            reason = "file-level disclosure that these pointers are git-excluded"
        if reason:
            allowed_files.append(f"{rel} ({len(hit_lines)} line(s)) — {reason}")
            continue
        for i, ln in hit_lines:
            n_lines += 1
            lo = max(0, i - 1 - MARKER_WINDOW)
            # Whitespace-normalized: a marker and its pointer routinely
            # land on opposite sides of a line wrap, and a matcher that
            # silently misses those would manufacture findings.
            window = " ".join(" ".join(all_lines[lo:i + MARKER_WINDOW]).split()).lower()
            if not any(mk in window for mk in
                       BOOTSTRAP_MARKERS + BOOTSTRAP_ABSENCE_MARKERS):
                findings.append(f"{rel}:{i} — cites `_bootstrap/` with no "
                                f"historical/unavailable marker: {ln.strip()[:90]}")
    status = "FAIL" if findings else ("OK" if n_lines else "WARN")
    res.add(status, "CG-12  no `_bootstrap/` cited as a required source",
            n_lines, len(findings), "citation",
            note=None if n_lines else "no citations examined",
            details=findings)
    res.add("WARN", "CG-12b `_bootstrap/` citation allowlist", len(allowed_files),
            0, "file", note="derivation and archive records",
            details=sorted(allowed_files))


# --------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(
        description="Read-only governance checks. Never rewrites anything.")
    ap.add_argument("--scope", choices=("clone", "tracked"), default="clone",
                    help="clone (default): tracked files plus untracked files "
                         "git does not ignore — what a clone will contain once "
                         "committed. tracked: `git ls-files` only.")
    args = ap.parse_args()

    paths, tracked, source = corpus_paths(args.scope)

    existing = [p for p in paths if os.path.exists(os.path.join(ROOT, p))]
    missing = len(paths) - len(existing)
    print(f"repo root: {ROOT}")
    if source == "walk":
        print(f"scope:     filesystem walk — {len(existing)} file(s) examined. "
              "git is unavailable here, so tracked/ignored status is Unknown: "
              "CG-11 cannot run and `--scope tracked` is not honored. Every "
              "other check runs over the walked corpus.\n")
    else:
        print(f"scope:     {args.scope} — {len(existing)} file(s) examined "
              f"({len(tracked)} tracked, "
              f"{len(existing) - len([p for p in existing if p in tracked])} "
              f"untracked-not-ignored"
              f"{f', {missing} listed but absent' if missing else ''})\n")

    res = Results()
    cg1_links(existing, res)
    cg2_retired_tokens(existing, res)
    cg3_stale_routing(existing, res)
    cg4_candidate_banners(existing, res)
    cg5_craft_banners(existing, res)
    cg6_accepted_homes(res)
    cg7_manifest(existing, res)
    cg8_budgets(existing, res)
    cg9_duplicate_homes(existing, res)
    cg10_pending_asof(existing, res)
    if source == "git":
        cg11_ignored(res)
    else:
        res.add("WARN", "CG-11 ignore rules", 0, 0, unit="rule",
                note="git unavailable — ignore status is Unknown, "
                     "not clean; re-run inside a git checkout")
    cg12_bootstrap_sources(existing, res)
    res.report()
    return 1 if res.failed() else 0


if __name__ == "__main__":
    sys.exit(main())
