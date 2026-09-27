#!/usr/bin/env python3
"""Check or record the owner-gated Three-Surface POC readability successor.

The candidate is inert. Only --record with the owner's exact two lines may
install its four changed subjects and two act records. A common-Git-dir journal
makes interrupted installation visible and recoverable from a linked worktree.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import uuid


SCRIPT = Path(__file__).resolve()
ROOT = SCRIPT.parents[1]
CHANGE = "openspec/changes/three-surface-poc-experience/"
PACKAGE = ".syzygy/governance/contracts/candidates/three-surface-poc-readability-successor/"
MANIFEST = PACKAGE + "THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt"
REVIEW = "docs/reviews/R-POC-READABILITY-SUCCESSOR-REVIEW-4-RAW.md"
ORIGINAL_ACT = ".syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md"
BOOTSTRAP_ACT = ".syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md"
DEDICATED = ".syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md"
AGGREGATE = ".syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md"
ROUTER = ".syzygy/governance/decisions/README.md"
STATUS = "PROJECT-STATUS.md"
LABEL = "SIGN OFF THREE-SURFACE POC READABILITY SUCCESSOR"
ACT_TYPE = "adopt specification amendment (readability-only successor)"
PROJECT_ID = "project:syzygy"
ARTIFACT_ID = "specification:syzygy:three-surface-poc-experience"
MARKER = "THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT"
MANIFEST_SHA = "221f1ececa321bf0cc6cd5e01f401e9eada38466c3c00dde43095f8cb8a0cd4d"
REVIEW_SHA = "7434a6be2adeb827e1110efd35535f9972d8fde749370d27622e0d7800aa33ef"
REVIEWED_CANDIDATE = "ab31201ad3844de197d89b67cda47df0e7928982"
ORIGINAL_ACT_SHA = "289d4e358aaeb9d2ea2f4e80b507bf376c15b7f8141c2da9337cb7618b73f004"
BOOTSTRAP_ACT_SHA = "3534db031087eb1de0f5eaae8fcfbc50e8f546e44b8440e0a5e4936e394ede8c"
ACT_ID = "act:syzygy:three-surface-poc-readability-successor:" + MANIFEST_SHA
LOCK_NAME = "syzygy-three-surface-poc-readability-successor.lock"
TX_NAME = "syzygy-transactions/three-surface-poc-readability-successor"
JOURNAL_VERSION = 1

# Exactly the effective predecessor chain: the later bootstrap act owns coverage.
ROWS = (
    (CHANGE + ".openspec.yaml", "9187547d8cc17017ebd44132527d2d5e096d1ef9705de80cc4f1cf34531f6976", "9187547d8cc17017ebd44132527d2d5e096d1ef9705de80cc4f1cf34531f6976"),
    (CHANGE + "CONTRACT-COVERAGE.md", "f29a01f6a5725f4ac7085fa04a62de757fd16153d507ae5e415ae0b501fdc0a4", "f29a01f6a5725f4ac7085fa04a62de757fd16153d507ae5e415ae0b501fdc0a4"),
    (CHANGE + "GOVERNING-DEPENDENCIES.md", "4bdcf6c6dbd07aad7d44fb1d6fbb9ae37ea56bed2ed66532231cdc37a71c1da4", "f8b66a710f9e3242f79b26b9c02eb4f44c55cd8368b517cd856da80b2ecbe1c5"),
    (CHANGE + "design.md", "0847bf5f78155712c13535a3de4a25be300ee6a726b5199e84e318103c28695c", "6d39ea6f6111abaea32c74ce96c975ae53e077485f0ed8f7c97545e64d7ba295"),
    (CHANGE + "proposal.md", "6459f56cba26e0bc38c71a4a93ea571aa11eabdc847c96c81f8afcf30b72eddb", "0650a6a3bc50158dc793802b9dcd40057b3199b3f7e9f8341a5bdc79cbea941a"),
    (CHANGE + "specs/three-surface-poc-experience/spec.md", "f0eda5b9ec8766e2b4b961fb2940c4ece7aa97b1c397e10d570abb04f5dd960e", "bb9112a55a1cf2afdd6911815e80fa645f517f8a4e8b1b262ecf7381be515410"),
)
PATCHES = (
    (PACKAGE + "proposed/GOVERNING-DEPENDENCIES.md.patch", "1279267298f8f86141a71c634020a98cd20ac91eeaeb4bae93cc9a89dac09e13"),
    (PACKAGE + "proposed/design.md.patch", "8725bebcd862403324e902230cf008a2f2693a02470fa648918064d229bdb363"),
    (PACKAGE + "proposed/proposal.md.patch", "4e1f433e6c8f824ccc665bc91825c6578983c0927fcfc37db8efe16d2a132ef1"),
    (PACKAGE + "proposed/spec.md.patch", "71378d557ddc7f6c1823fff57e44d47bef2019df59faf853d14d851ec9beaec0"),
)
PINS = (
    (REVIEW, REVIEW_SHA),
    (ORIGINAL_ACT, ORIGINAL_ACT_SHA),
    (BOOTSTRAP_ACT, BOOTSTRAP_ACT_SHA),
    ("scripts/build_three_surface_poc_readability_successor.py", "822882d90aba6b1ca85ddb03ec4ba465ab7adb436943c91018e00411c3b26087"),
    ("scripts/fixtures/three_surface_poc_readability_serial_apply_mutation.json", "9dcbf4aab581894e41f9e06bf75dcd380695fe5231bcec910d0d157961871aa5"),
    ("docs/reviews/R-POC-READABILITY-SUCCESSOR-RAW.md", "a567e71e7da131530245a2278792036ff0a0824ccd433a27885b16c6cb7e467e"),
    ("docs/reviews/R-POC-READABILITY-SUCCESSOR-REVIEW-2-RAW.md", "b16d102fe1801c70f4d816e891633b40dd9ceac7714cd166dff854244328f942"),
    ("docs/reviews/R-POC-READABILITY-SUCCESSOR-REVIEW-3-RAW.md", "47a9efc0bbfbb4ec257107724a198c19cc5b2ed73245a9b583b984531a5852fe"),
    (PACKAGE + "IMPACT-LEDGER.md", "351f044257f8bd5687ea1280c69fa372f229a9bd7a6e368a5cb71cad452074e9"),
    (PACKAGE + "OWNER-DECISION-PACKET.md", "7c4527847f2008681258c0920e5b946c10c766cc3829e88ba0b3dcc1a099883d"),
    (PACKAGE + "REVIEW-BRIEF.md", "d47944b03bcbd11c50a454f17ee485e23ae5d0298ac6e503f7cc0d5604905c80"),
    (PACKAGE + "SEMANTIC-DELTA.md", "4a60b0cc59f30fe4ca012270ab7054e6d9ecb46e3ff33e6a4fa78dc71f05df22"),
    (PACKAGE + "SEMANTIC-MAP.json", "a9dcf09896d84e73b6aa23df0b8753f52647a8484a69e4ebe8aa74644c83837c"),
    *PATCHES,
)
TARGETS = tuple(row[0] for row in ROWS if row[1] != row[2]) + (DEDICATED, AGGREGATE, ROUTER, STATUS)
PHRASE_RE = re.compile(r"SIGN OFF THREE-SURFACE POC READABILITY SUCCESSOR: ([0-9a-f]{64})\Z", re.ASCII)
INSTANT_RE = re.compile(r"ACT INSTANT: ([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z)\Z", re.ASCII)
ROW_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$", re.M)


class Refusal(ValueError):
    """An input or recovery state fails a named transaction invariant."""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def git_path(root: Path, flag: str) -> Path:
    run = subprocess.run(["git", "-C", str(root), "rev-parse", "--path-format=absolute", flag], capture_output=True, text=True)
    if run.returncode or not run.stdout.strip():
        raise Refusal(f"worktree identity unavailable: {flag}")
    return Path(run.stdout.strip()).resolve(strict=True)


def identities(root: Path) -> tuple[Path, Path, Path]:
    if root.is_symlink() or not root.is_dir() or root.resolve(strict=True) != root:
        raise Refusal("worktree root missing, relocated or symlinked")
    if git_path(root, "--show-toplevel") != root:
        raise Refusal("worktree root identity mismatch")
    return root, git_path(root, "--git-dir"), git_path(root, "--git-common-dir")


def safe_target(root: Path, relative: str, *, absent_ok: bool = False) -> Path:
    p = PurePosixPath(relative)
    if p.is_absolute() or p.as_posix() != relative or any(x in ("", ".", "..") for x in p.parts):
        raise Refusal(f"noncanonical target: {relative}")
    target = root.joinpath(*p.parts)
    if os.path.commonpath((str(root), str(target))) != str(root):
        raise Refusal(f"escaping target: {relative}")
    current = root
    for part in p.parts:
        current = current / part
        if current.is_symlink():
            raise Refusal(f"symlinked target component: {relative}")
    if not absent_ok and not target.is_file():
        raise Refusal(f"missing target: {relative}")
    if target.exists() and not target.is_file():
        raise Refusal(f"non-file target: {relative}")
    if target.resolve(strict=not absent_ok) != target:
        raise Refusal(f"noncanonical absolute target: {relative}")
    return target


def read(root: Path, relative: str) -> bytes:
    return safe_target(root, relative).read_bytes()


def checked_file(root: Path, relative: str, expected: str) -> bytes:
    data = read(root, relative)
    if sha(data) != expected:
        raise Refusal(f"frozen input drift: {relative}")
    return data


def candidate(root: Path) -> dict[str, bytes]:
    manifest = checked_file(root, MANIFEST, MANIFEST_SHA).decode()
    expected = [(new, path) for path, _old, new in ROWS]
    if ROW_RE.findall(manifest) != expected or len(ROW_RE.findall(manifest)) != 6:
        raise Refusal("six-row manifest path/order/digest mismatch")
    for path, digest in PINS:
        checked_file(root, path, digest)
    review = read(root, REVIEW).decode()
    if f"Reviewed commit: {REVIEWED_CANDIDATE}" not in review.splitlines()[:8] or "Verdict: CONFIRM" not in review.splitlines()[:8] or MANIFEST_SHA not in review.splitlines()[:8][3]:
        raise Refusal("semantic review head does not confirm frozen candidate")
    original = read(root, ORIGINAL_ACT).decode()
    bootstrap = read(root, BOOTSTRAP_ACT).decode()
    for path, old, _new in ROWS:
        name = path.removeprefix(CHANGE)
        source = bootstrap if name == "CONTRACT-COVERAGE.md" else original
        if name not in source or old not in source:
            raise Refusal(f"effective predecessor act row missing: {path}")
    if "0c8472a9a6da59453d93bcde5347c6ba21f478e1d1071bac08bc40bbe154d9ce" not in original:
        raise Refusal("historical coverage predecessor missing")
    with tempfile.TemporaryDirectory() as name:
        scratch = Path(name)
        for path, old, _new in ROWS:
            data = read(root, path)
            if sha(data) not in (old, _new):
                raise Refusal(f"subject is neither predecessor nor successor: {path}")
            target = scratch / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        # In a performed clone the old commit need not be reachable (for
        # example after a squash merge). The frozen patches are reversible;
        # reconstruct predecessor bytes from the installed successor.
        for (patch, _digest), path in zip(PATCHES, TARGETS[:4]):
            if sha((scratch / path).read_bytes()) == dict((p, n) for p, _o, n in ROWS)[path]:
                undone = subprocess.run(["git", "apply", "--reverse", "--whitespace=nowarn", str(root / patch)], cwd=scratch, capture_output=True, text=True)
                if undone.returncode:
                    raise Refusal(f"frozen patch cannot recover predecessor: {patch}: {undone.stderr.strip()}")
        for path, old, _new in ROWS:
            if sha((scratch / path).read_bytes()) != old:
                raise Refusal(f"effective predecessor reconstruction failed: {path}")
        for patch, _digest in PATCHES:
            done = subprocess.run(["git", "apply", "--whitespace=nowarn", str(root / patch)], cwd=scratch, capture_output=True, text=True)
            if done.returncode:
                raise Refusal(f"frozen patch does not apply: {patch}: {done.stderr.strip()}")
        proposed = {path: (scratch / path).read_bytes() for path, _old, _new in ROWS}
    for path, _old, new in ROWS:
        if sha(proposed[path]) != new:
            raise Refusal(f"proposed subject digest mismatch: {path}")
    return proposed


def owner_inputs(phrase: str | None, instant_line: str | None) -> str:
    match = PHRASE_RE.fullmatch(phrase or "")
    if match is None or match.group(1) != MANIFEST_SHA:
        raise Refusal("owner phrase is absent, malformed or has the wrong manifest digest")
    match = INSTANT_RE.fullmatch(instant_line or "")
    if match is None:
        raise Refusal("owner ACT INSTANT line is absent or malformed")
    instant = match.group(1)
    try:
        datetime.strptime(instant, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as error:
        raise Refusal("owner ACT INSTANT is not a real UTC calendar instant") from error
    return instant


def dedicated_body(phrase: str, instant_line: str) -> bytes:
    instant = owner_inputs(phrase, instant_line)
    rows = "".join(f"| `{path}` | `{old}` | `{new}` |\n" for path, old, new in ROWS)
    return f"""# Three-Surface POC readability successor — owner act

Owner: Tzeusy
Act instant: {instant}
Instant source: owner-supplied `{instant_line}` line in the same response as the phrase
Act identity: {ACT_ID}
Act type: {ACT_TYPE}
Project identity: {PROJECT_ID}
Artifact identity: {ARTIFACT_ID}
Provenance state: owner-adopted (bootstrap, uncorrelated)
A1 audit-record identity: explicitly absent

The owner performed the exact-digest successor by writing exactly:

```text
{phrase}
```

Manifest: `{MANIFEST}`; SHA-256: `{MANIFEST_SHA}`.
Reviewed semantic/fresh-reader raw: `{REVIEW}`; SHA-256: `{REVIEW_SHA}`.

| Signed subject | Effective predecessor SHA-256 | Successor SHA-256 |
|---|---|---|
{rows}
The later general trusted-bootstrap act supplies the effective coverage
predecessor. The original POC sign-off and that later act remain unchanged
history. Four subjects change; `.openspec.yaml` and `CONTRACT-COVERAGE.md`
remain byte-identical. `tasks.md` is outside the signed set.

Scope: readability-only specification amendment. It grants no new
implementation, observed-project read, provider egress, deployment or release
authority. Review, CI and this record are not independent verification.
""".encode()


def aggregate_block(dedicated: bytes) -> bytes:
    return (f"\n<!-- {MARKER}:BEGIN -->\n".encode() + dedicated + f"<!-- {MARKER}:END -->\n".encode())


def router_row(instant: str) -> bytes:
    date = instant[:10]
    return (f"| {date} | [`THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`](THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md) | Readability-only six-subject POC specification successor; see the owner act and aggregate record for authority |\n").encode()


def status_statement(instant: str) -> bytes:
    return (f"\n[Observed — owner act recorded {instant}] The six-subject Three-Surface POC readability successor is current at manifest `{MANIFEST_SHA}` under [`THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`](.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md). This is specification adoption only; existing POC implementation authority is unchanged.\n").encode()


def rendered_targets(proposed: dict[str, bytes], phrase: str, instant_line: str,
                     aggregate: bytes, router: bytes, status: bytes) -> dict[str, bytes]:
    instant = owner_inputs(phrase, instant_line)
    body = dedicated_body(phrase, instant_line)
    if MARKER.encode() in aggregate or LABEL.encode() in aggregate:
        raise Refusal("existing or partial successor act record")
    if b"THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md" in router or status_statement(instant).split(b" at manifest ")[0] in status:
        raise Refusal("existing or partial successor router/status")
    anchor = b"\nDates are each file's first-commit date"
    if router.count(anchor) != 1:
        raise Refusal("decisions act-router insertion anchor changed")
    result = {path: proposed[path] for path in TARGETS[:4]}
    result[DEDICATED] = body
    result[AGGREGATE] = aggregate.rstrip(b"\n") + b"\n" + aggregate_block(body)
    result[ROUTER] = router.replace(anchor, router_row(instant) + anchor)
    result[STATUS] = status.rstrip(b"\n") + b"\n" + status_statement(instant)
    return result


def outputs(root: Path, proposed: dict[str, bytes], phrase: str, instant_line: str) -> dict[str, bytes]:
    if safe_target(root, DEDICATED, absent_ok=True).exists():
        raise Refusal("existing or partial successor act record")
    return rendered_targets(proposed, phrase, instant_line,
                            read(root, AGGREGATE), read(root, ROUTER), read(root, STATUS))


def context(root: Path) -> tuple[Path, Path, Path, Path]:
    bound, git_dir, common = identities(root)
    tx = common / TX_NAME
    safe_tx(common, tx)
    return bound, git_dir, common, tx


def safe_tx(common: Path, tx: Path) -> None:
    if tx != common / TX_NAME or common.resolve(strict=True) != common:
        raise Refusal("noncanonical common transaction directory")
    current = common
    for part in Path(TX_NAME).parts:
        current = current / part
        if current.is_symlink() or (current.exists() and not current.is_dir()):
            raise Refusal("symlinked or non-directory journal component")
    for child in ("journal.json", "backups", "staged", "completed.json.pending", "completed.json"):
        target = tx / child
        if target.is_symlink():
            raise Refusal(f"symlinked journal evidence: {child}")


@contextmanager
def locked(common: Path, exclusive: bool):
    path = common / LOCK_NAME
    if path.is_symlink():
        raise Refusal("symlinked common lock")
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise Refusal("common lock is not a regular file")
        fcntl.flock(fd, fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_fsync(path: Path, data: bytes, *, exclusive: bool = False) -> None:
    flags = os.O_WRONLY | os.O_CREAT | (os.O_EXCL if exclusive else os.O_TRUNC)
    fd = os.open(path, flags, 0o600)
    try:
        with os.fdopen(fd, "wb", closefd=False) as stream:
            stream.write(data)
            stream.flush()
            os.fsync(fd)
    finally:
        os.close(fd)
    fsync_dir(path.parent)


def atomic_file(path: Path, data: bytes, mode: int = 0o644) -> None:
    fd, name = tempfile.mkstemp(prefix=".syzygy-tx-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fchmod(stream.fileno(), mode)
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        with path.open("rb") as stream:
            os.fsync(stream.fileno())
        fsync_dir(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def journal_path(tx: Path) -> Path:
    return tx / "journal.json"


def receipt_path(tx: Path) -> Path:
    return tx / "completed.json"


def journal_present(tx: Path) -> bool:
    safe_tx(tx.parents[1], tx)
    if journal_path(tx).exists():
        return True
    return any((tx / part).exists() for part in ("backups", "staged", "completed.json.pending"))


def validate_receipt(root: Path, common: Path, tx: Path, *, required: bool = False) -> dict | None:
    path = receipt_path(tx)
    if not path.exists():
        if required:
            raise Refusal("completion receipt missing")
        return None
    if path.is_symlink():
        raise Refusal("completion receipt symlinked")
    try:
        record = json.loads(path.read_bytes())
    except (OSError, json.JSONDecodeError) as error:
        raise Refusal("completion receipt malformed") from error
    expected_keys = {"version", "act_id", "manifest_sha256", "phrase_sha256", "instant_line_sha256", "worktree_root", "git_dir", "common_dir", "common_dev", "common_ino", "outputs", "checksum_sha256"}
    if not isinstance(record, dict) or set(record) != expected_keys or record["version"] != 1 or record["act_id"] != ACT_ID or record["manifest_sha256"] != MANIFEST_SHA:
        raise Refusal("completion receipt schema or act identity mismatch")
    if (any(type(record[key]) is not str for key in ("checksum_sha256", "phrase_sha256", "instant_line_sha256", "worktree_root", "git_dir", "common_dir"))
            or any(type(record[key]) is not int for key in ("common_dev", "common_ino"))):
        raise Refusal("completion receipt field types invalid")
    if record["checksum_sha256"] != sha(canonical_json({key: value for key, value in record.items() if key != "checksum_sha256"})):
        raise Refusal("completion receipt checksum mismatch")
    if record["common_dir"] != str(common) or (record["common_dev"], record["common_ino"]) != (common.stat().st_dev, common.stat().st_ino):
        raise Refusal("completion receipt common Git directory identity mismatch")
    bound = Path(record["worktree_root"])
    try:
        _bound, git_dir, bound_common = identities(bound)
    except (OSError, Refusal) as error:
        raise Refusal("completion receipt bound worktree identity mismatch") from error
    if bound_common != common or str(git_dir) != record["git_dir"]:
        raise Refusal("completion receipt bound worktree Git identity mismatch")
    if not isinstance(record["outputs"], dict) or set(record["outputs"]) != set(TARGETS) or any(type(value) is not str or not re.fullmatch(r"[0-9a-f]{64}", value) for value in record["outputs"].values()):
        raise Refusal("completion receipt output population/digest mismatch")
    body = read(bound, DEDICATED)
    phrase, instant_line = parse_body(body)
    if record["phrase_sha256"] != sha(phrase.encode()) or record["instant_line_sha256"] != sha(instant_line.encode()):
        raise Refusal("completion receipt owner-input digest mismatch")
    if record["outputs"][DEDICATED] != sha(body):
        raise Refusal("completion receipt dedicated output digest mismatch")
    for target in TARGETS[:4]:
        if record["outputs"][target] != sha(read(bound, target)):
            raise Refusal(f"completion receipt subject output digest mismatch: {target}")
    return record


def parse_body(body: bytes) -> tuple[str, str]:
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError as error:
        raise Refusal("dedicated act is not UTF-8") from error
    phrase_matches = re.findall(r"^SIGN OFF THREE-SURFACE POC READABILITY SUCCESSOR: [^\n]+$", text, re.M)
    instant_matches = re.findall(r"^Instant source: owner-supplied `(ACT INSTANT: [^`\n]+)` line in the same response as the phrase$", text, re.M)
    if len(phrase_matches) != 1 or len(instant_matches) != 1:
        raise Refusal("dedicated act owner phrase/instant population mismatch")
    owner_inputs(phrase_matches[0], instant_matches[0])
    return phrase_matches[0], instant_matches[0]


def check_state(root: Path, common: Path, tx: Path, *, allow_journal: bool = False) -> str:
    if journal_present(tx) and not allow_journal:
        raise Refusal("recovery required: live transaction journal")
    proposed = candidate(root)
    receipt = validate_receipt(root, common, tx)
    actual = [(path, sha(read(root, path))) for path, _old, _new in ROWS]
    old = [(path, digest) for path, digest, _new in ROWS]
    new = [(path, digest) for path, _old, digest in ROWS]
    dedicated = safe_target(root, DEDICATED, absent_ok=True)
    aggregate = read(root, AGGREGATE)
    router = read(root, ROUTER)
    status = read(root, STATUS)
    begin = f"<!-- {MARKER}:BEGIN -->".encode()
    end = f"<!-- {MARKER}:END -->".encode()
    markers = (aggregate.count(begin), aggregate.count(end))
    if actual == old and not dedicated.exists() and markers == (0, 0) and LABEL.encode() not in aggregate:
        if b"THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md" in router or b"The six-subject Three-Surface POC readability successor is current" in status or receipt:
            raise Refusal("candidate-unperformed invalid: performed route/status/receipt present")
        return "candidate-unperformed"
    if actual != new:
        state = "mixed predecessor/successor subjects" if actual != old else "predecessor subjects with records"
        raise Refusal(state + ": exact six-row state invalid")
    if markers[0] > 1 or markers[1] > 1:
        raise Refusal("aggregate successor block duplicated or conflicting")
    if not dedicated.exists() or markers != (1, 1):
        raise Refusal("installed subjects without both exact records")
    body = dedicated.read_bytes()
    phrase, instant_line = parse_body(body)
    if body != dedicated_body(phrase, instant_line):
        raise Refusal("dedicated act differs from deterministic performed template")
    block = aggregate_block(body)
    if aggregate.count(block) != 1 or aggregate.find(begin) > aggregate.find(end) or LABEL.encode() in aggregate.replace(block, b""):
        raise Refusal("aggregate successor block missing, duplicated or conflicting")
    instant = owner_inputs(phrase, instant_line)
    row = router_row(instant)
    if router.count(row) != 1 or router.count(b"THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md") != 2:
        raise Refusal("decisions act-router row missing, duplicated or conflicting")
    statement = status_statement(instant)
    if status.count(statement) != 1 or status.count(b"The six-subject Three-Surface POC readability successor is current") != 1:
        raise Refusal("PROJECT-STATUS current-successor statement missing, duplicated or conflicting")
    if b"Three-Surface POC readability successor" in status.replace(statement, b""):
        raise Refusal("PROJECT-STATUS carries a conflicting successor-current claim")
    if receipt is not None and receipt["worktree_root"] == str(root):
        expected_receipt = receipt_from_outputs(root, common, phrase, instant_line, {
            path: receipt["outputs"][path] for path in TARGETS
        })
        if receipt != expected_receipt:
            raise Refusal("completion receipt content conflicts with performed act")
    return "performed-exact"


def receipt_from_outputs(root: Path, common: Path, phrase: str, instant_line: str, digests: dict[str, str]) -> dict:
    _root, git_dir, _common = identities(root)
    result = {"version": 1, "act_id": ACT_ID, "manifest_sha256": MANIFEST_SHA,
            "phrase_sha256": sha(phrase.encode()), "instant_line_sha256": sha(instant_line.encode()),
            "worktree_root": str(root), "git_dir": str(git_dir), "common_dir": str(common),
            "common_dev": common.stat().st_dev, "common_ino": common.stat().st_ino,
            "outputs": digests}
    result["checksum_sha256"] = sha(canonical_json(result))
    return result


def failpoint(name: str) -> None:
    # Test-only failure injection is restricted to disposable fixture worktrees.
    if os.environ.get("SYZYGY_RECORDER_TESTING") != "1":
        return
    if os.environ.get("SYZYGY_RECORDER_FAIL_AT") == name:
        raise RuntimeError(f"injected exception: {name}")
    if os.environ.get("SYZYGY_RECORDER_KILL_AT") == name:
        os.kill(os.getpid(), 9)


def persist_journal(tx: Path, journal: dict, *, exclusive: bool = False) -> None:
    path = journal_path(tx)
    journal["checksum_sha256"] = sha(canonical_json({key: value for key, value in journal.items() if key != "checksum_sha256"}))
    if exclusive:
        write_fsync(path, canonical_json(journal), exclusive=True)
    else:
        atomic_file(path, canonical_json(journal), 0o600)


def prepare(root: Path, git_dir: Path, common: Path, tx: Path, rendered: dict[str, bytes], phrase: str, instant_line: str) -> dict:
    tx.mkdir(parents=True, exist_ok=True)
    fsync_dir(tx.parent)
    if journal_present(tx) or receipt_path(tx).exists():
        raise Refusal("recovery required or act already completed")
    backups = tx / "backups"
    staged = tx / "staged"
    backups.mkdir()
    staged.mkdir()
    records = []
    for index, relative in enumerate(TARGETS):
        target = safe_target(root, relative, absent_ok=True)
        existed = target.exists()
        old = target.read_bytes() if existed else None
        successor = rendered[relative]
        if target.parent.stat().st_dev != staged.stat().st_dev:
            raise Refusal(f"cross-filesystem staging refused: {relative}")
        backup = backups / f"{index:02d}.bin"
        stage = staged / f"{index:02d}.bin"
        if existed:
            write_fsync(backup, old, exclusive=True)
        write_fsync(stage, successor, exclusive=True)
        if existed and sha(backup.read_bytes()) != sha(old) or sha(stage.read_bytes()) != sha(successor):
            raise Refusal(f"backup/staged digest mismatch: {relative}")
        records.append({"relative": relative, "absolute": str(target), "existed": existed,
                        "predecessor_sha256": sha(old) if existed else None,
                        "successor_sha256": sha(successor),
                        "backup": str(backup) if existed else None,
                        "backup_sha256": sha(old) if existed else None,
                        "staged": str(stage), "staged_sha256": sha(successor),
                        "mode": stat.S_IMODE(target.stat().st_mode) if existed else 0o644})
    fsync_dir(backups)
    fsync_dir(staged)
    journal = {"version": JOURNAL_VERSION, "uuid": str(uuid.uuid4()), "phase": "prepared", "next_index": 0,
               "worktree_root": str(root), "git_dir": str(git_dir), "common_dir": str(common),
               "common_dev": common.stat().st_dev, "common_ino": common.stat().st_ino,
               "manifest_sha256": MANIFEST_SHA, "phrase_sha256": sha(phrase.encode()),
               "instant_line_sha256": sha(instant_line.encode()), "targets": records}
    persist_journal(tx, journal, exclusive=True)
    fsync_dir(tx)
    failpoint("prepared")
    return journal


def validate_journal(common: Path, tx: Path) -> tuple[dict, Path]:
    safe_tx(common, tx)
    path = journal_path(tx)
    if not path.is_file() or path.is_symlink():
        raise Refusal("recovery required: missing or symlinked journal")
    try:
        j = json.loads(path.read_bytes())
    except (OSError, json.JSONDecodeError) as error:
        raise Refusal("recovery journal malformed") from error
    keys = {"version", "uuid", "phase", "next_index", "worktree_root", "git_dir", "common_dir", "common_dev", "common_ino", "manifest_sha256", "phrase_sha256", "instant_line_sha256", "targets", "checksum_sha256"}
    if not isinstance(j, dict) or set(j) != keys or j["version"] != JOURNAL_VERSION or j["phase"] not in ("prepared", "installing", "installed", "verified", "committed") or type(j["next_index"]) is not int or not 0 <= j["next_index"] <= len(TARGETS):
        raise Refusal("recovery journal version/phase/index invalid")
    if (any(type(j[key]) is not str for key in ("checksum_sha256", "uuid", "worktree_root", "git_dir", "common_dir", "manifest_sha256", "phrase_sha256", "instant_line_sha256"))
            or any(type(j[key]) is not int for key in ("common_dev", "common_ino"))):
        raise Refusal("recovery journal field types invalid")
    if j["checksum_sha256"] != sha(canonical_json({key: value for key, value in j.items() if key != "checksum_sha256"})):
        raise Refusal("recovery journal checksum mismatch")
    if (j["phase"] == "prepared" and j["next_index"] != 0) or (j["phase"] in ("installed", "verified", "committed") and j["next_index"] != len(TARGETS)):
        raise Refusal("recovery journal phase/index mismatch")
    try:
        uuid.UUID(j["uuid"])
    except (KeyError, ValueError, TypeError) as error:
        raise Refusal("recovery journal UUID invalid") from error
    if j["common_dir"] != str(common) or (j["common_dev"], j["common_ino"]) != (common.stat().st_dev, common.stat().st_ino) or j["manifest_sha256"] != MANIFEST_SHA:
        raise Refusal("recovery journal common-dir or manifest identity mismatch")
    if not all(re.fullmatch(r"[0-9a-f]{64}", j[key] or "") for key in ("phrase_sha256", "instant_line_sha256")):
        raise Refusal("recovery journal owner-input digest malformed")
    root = Path(j["worktree_root"])
    try:
        _root, git_dir, bound_common = identities(root)
    except (OSError, Refusal) as error:
        raise Refusal("recovery journal bound worktree missing, relocated or identity-mismatched") from error
    if bound_common != common or str(git_dir) != j["git_dir"]:
        raise Refusal("recovery journal bound Git identity mismatch")
    if not isinstance(j["targets"], list) or len(j["targets"]) != len(TARGETS):
        raise Refusal("recovery journal target population invalid")
    for index, record in enumerate(j["targets"]):
        rel = TARGETS[index]
        target = safe_target(root, rel, absent_ok=True)
        keys = {"relative", "absolute", "existed", "predecessor_sha256", "successor_sha256", "backup", "backup_sha256", "staged", "staged_sha256", "mode"}
        if not isinstance(record, dict) or set(record) != keys or record["relative"] != rel or record["absolute"] != str(target) or type(record["existed"]) is not bool or type(record["mode"]) is not int or not 0 <= record["mode"] <= 0o777:
            raise Refusal(f"recovery journal target schema/path invalid: {rel}")
        if (any(type(record[key]) is not str for key in ("relative", "absolute", "successor_sha256", "staged", "staged_sha256"))
                or (record["existed"] and any(type(record[key]) is not str for key in ("predecessor_sha256", "backup", "backup_sha256")))):
            raise Refusal(f"recovery journal target field types invalid: {rel}")
        expected_new = dict((p, n) for p, _o, n in ROWS).get(rel)
        if expected_new and record["successor_sha256"] != expected_new:
            raise Refusal(f"recovery journal successor digest invalid: {rel}")
        for key in ("successor_sha256", "staged_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", record[key] or ""):
                raise Refusal(f"recovery journal {key} invalid: {rel}")
        if record["successor_sha256"] != record["staged_sha256"] or record["staged"] != str(tx / "staged" / f"{index:02d}.bin"):
            raise Refusal(f"recovery journal staged binding invalid: {rel}")
        if record["existed"]:
            if record["backup"] != str(tx / "backups" / f"{index:02d}.bin") or record["predecessor_sha256"] != record["backup_sha256"] or not re.fullmatch(r"[0-9a-f]{64}", record["backup_sha256"] or ""):
                raise Refusal(f"recovery journal backup binding invalid: {rel}")
            expected_old = dict((p, o) for p, o, _n in ROWS).get(rel)
            if expected_old and record["predecessor_sha256"] != expected_old:
                raise Refusal(f"recovery journal predecessor digest invalid: {rel}")
        elif record["backup"] is not None or record["backup_sha256"] is not None or record["predecessor_sha256"] is not None or rel != DEDICATED:
            raise Refusal(f"recovery journal absent-target binding invalid: {rel}")
        if target.parent.stat().st_dev != tx.stat().st_dev:
            raise Refusal(f"recovery journal cross-filesystem staging: {rel}")
        if j["phase"] != "committed":
            if record["existed"] and (Path(record["backup"]).is_symlink() or not Path(record["backup"]).is_file() or sha(Path(record["backup"]).read_bytes()) != record["backup_sha256"]):
                raise Refusal(f"recovery backup missing or corrupt: {rel}")
            if Path(record["staged"]).is_symlink() or not Path(record["staged"]).is_file() or sha(Path(record["staged"]).read_bytes()) != record["staged_sha256"]:
                raise Refusal(f"recovery staged file missing or corrupt: {rel}")
        else:
            for field, digest in (("backup", "backup_sha256"), ("staged", "staged_sha256")):
                name = record[field]
                if name and Path(name).exists() and (Path(name).is_symlink() or sha(Path(name).read_bytes()) != record[digest]):
                    raise Refusal(f"recovery committed {field} corrupt: {rel}")
    if j["phase"] != "committed":
        staged_body = Path(j["targets"][4]["staged"]).read_bytes()
        phrase, instant_line = parse_body(staged_body)
        if sha(phrase.encode()) != j["phrase_sha256"] or sha(instant_line.encode()) != j["instant_line_sha256"]:
            raise Refusal("recovery journal owner-input digests disagree with staged act")
        preimages = [Path(j["targets"][index]["backup"]).read_bytes() for index in (5, 6, 7)]
        expected = rendered_targets(candidate(root), phrase, instant_line, *preimages)
        for record in j["targets"]:
            rel = record["relative"]
            if sha(expected[rel]) != record["successor_sha256"] or Path(record["staged"]).read_bytes() != expected[rel]:
                raise Refusal(f"recovery journal output differs from reviewed template: {rel}")
    return j, root


def cleanup(tx: Path) -> None:
    failpoint("cleanup-start")
    for name in ("backups", "staged"):
        folder = tx / name
        if folder.exists():
            for child in folder.iterdir():
                child.unlink()
            folder.rmdir()
            fsync_dir(tx)
    journal_path(tx).unlink(missing_ok=True)
    fsync_dir(tx)


def recover(common: Path, tx: Path) -> str:
    if not journal_present(tx):
        return "no-recovery-needed"
    j, bound = validate_journal(common, tx)
    if j["phase"] == "committed":
        for record in j["targets"]:
            if sha(read(bound, record["relative"])) != record["successor_sha256"]:
                raise Refusal(f"committed output drift; manual intervention required: {record['relative']}")
        body = read(bound, DEDICATED)
        phrase, instant_line = parse_body(body)
        if sha(phrase.encode()) != j["phrase_sha256"] or sha(instant_line.encode()) != j["instant_line_sha256"]:
            raise Refusal("committed owner inputs disagree with journal")
        receipt = receipt_from_outputs(bound, common, phrase, instant_line, {r["relative"]: r["successor_sha256"] for r in j["targets"]})
        pending = tx / "completed.json.pending"
        if pending.exists() and pending.read_bytes() != canonical_json(receipt):
            raise Refusal("pending completion receipt conflicts with committed journal")
        if receipt_path(tx).exists():
            if receipt_path(tx).read_bytes() != canonical_json(receipt):
                raise Refusal("completion receipt conflicts with committed journal")
        else:
            if not pending.exists():
                write_fsync(pending, canonical_json(receipt), exclusive=True)
            os.replace(pending, receipt_path(tx))
            fsync_dir(tx)
        if pending.exists():
            pending.unlink()
            fsync_dir(tx)
        check_state(bound, common, tx, allow_journal=True)
        cleanup(tx)
        return "performed-exact"
    if receipt_path(tx).exists():
        raise Refusal("premature completion receipt in pre-commit journal")
    for record in reversed(j["targets"]):
        target = safe_target(bound, record["relative"], absent_ok=True)
        if record["existed"]:
            atomic_file(target, Path(record["backup"]).read_bytes(), record["mode"])
        elif target.exists():
            target.unlink()
            fsync_dir(target.parent)
    (tx / "completed.json.pending").unlink(missing_ok=True)
    fsync_dir(tx)
    if check_state(bound, common, tx, allow_journal=True) != "candidate-unperformed":
        raise Refusal("pre-commit rollback did not restore inert candidate")
    cleanup(tx)
    return "candidate-unperformed"


def record(root: Path, git_dir: Path, common: Path, tx: Path, phrase: str, instant_line: str, expected_manifest: str | None) -> str:
    owner_inputs(phrase, instant_line)
    if journal_present(tx):
        recover(common, tx)
    if receipt_path(tx).exists():
        validate_receipt(root, common, tx)
        raise Refusal("repository-wide replay refused: act already completed")
    if check_state(root, common, tx) != "candidate-unperformed":
        raise Refusal("record requires exact inert candidate")
    proposed = candidate(root)
    rendered = outputs(root, proposed, phrase, instant_line)
    digests = {path: sha(rendered[path]) for path in TARGETS}
    if expected_manifest is None or expected_manifest != sha(canonical_json(digests)):
        raise Refusal("rendered eight-output manifest digest must match reviewed preflight")
    failpoint("before-install")
    j = prepare(root, git_dir, common, tx, rendered, phrase, instant_line)
    try:
        j["phase"] = "installing"
        persist_journal(tx, j)
        for index, relative in enumerate(TARGETS):
            record_row = j["targets"][index]
            target = safe_target(root, relative, absent_ok=True)
            atomic_file(target, rendered[relative], record_row["mode"])
            j["next_index"] = index + 1
            persist_journal(tx, j)
            failpoint(f"target-{index + 1}")
        j["phase"] = "installed"
        persist_journal(tx, j)
        if check_state(root, common, tx, allow_journal=True) != "performed-exact":
            raise Refusal("installed state failed exact performed verification")
        failpoint("installed-verified")
        j["phase"] = "verified"
        persist_journal(tx, j)
        receipt = receipt_from_outputs(root, common, phrase, instant_line, digests)
        pending = tx / "completed.json.pending"
        write_fsync(pending, canonical_json(receipt), exclusive=True)
        failpoint("pending-receipt")
        j["phase"] = "committed"
        persist_journal(tx, j)
        failpoint("committed-phase")
        os.replace(pending, receipt_path(tx))
        fsync_dir(tx)
        failpoint("final-receipt")
        if check_state(root, common, tx, allow_journal=True) != "performed-exact":
            raise Refusal("committed readback failed")
        cleanup(tx)
        return check_state(root, common, tx)
    except Exception:
        # SIGKILL cannot run this handler; the next exclusive holder recovers.
        if journal_present(tx):
            recover(common, tx)
        raise


def render(root: Path, common: Path, tx: Path, phrase: str, instant_line: str) -> dict:
    if check_state(root, common, tx) != "candidate-unperformed":
        raise Refusal("render requires exact inert candidate")
    proposal = outputs(root, candidate(root), phrase, instant_line)
    digests = {path: sha(proposal[path]) for path in TARGETS}
    return {"state": "candidate-unperformed", "manifest_sha256": MANIFEST_SHA,
            "act_id": ACT_ID, "outputs": digests,
            "output_manifest_sha256": sha(canonical_json(digests))}


def cli(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    for mode in ("check", "preflight", "render-performed", "record", "recover", "selftest"):
        modes.add_argument("--" + mode, action="store_true")
    parser.add_argument("--phrase", help="one exact owner phrase line")
    parser.add_argument("--act-instant", help="one exact owner ACT INSTANT line")
    parser.add_argument("--expected-output-manifest-sha256", help="digest printed by reviewed --render-performed")
    args = parser.parse_args(argv)
    if args.selftest:
        from test_three_surface_poc_readability_recorder import selftest
        return selftest()
    root, git_dir, common, tx = context(ROOT)
    try:
        with locked(common, args.record or args.recover):
            if args.recover:
                print(recover(common, tx))
            elif args.record:
                print(record(root, git_dir, common, tx, args.phrase, args.act_instant, args.expected_output_manifest_sha256))
            elif args.render_performed:
                print(canonical_json(render(root, common, tx, args.phrase, args.act_instant)).decode(), end="")
            else:
                state = check_state(root, common, tx)
                print(f"{state}: 6 signed subjects, 4 changed / 2 unchanged; manifest {MANIFEST_SHA}")
        return 0
    except (Refusal, OSError, RuntimeError) as error:
        print(f"REFUSED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(cli(sys.argv[1:]))
