"""Reviewer identity and byte-sweep checks for PR 513. Read-only over the clone.
Usage: python3 identity.py <clone>
"""
import hashlib, json, subprocess, sys

ROOT = sys.argv[1]
HEAD, BASE, LANE_BASE, LANE_HEAD, RUN = 'a670f988', 'a0406967', '4b31531c', '375a1e74', '73772882'
TEST = 'packages/polaris-dossier/src/waiting-sessions.test.ts'
READER = 'packages/polaris-dossier/src/waiting-sessions.ts'
EVID = 'docs/evidence/waiting-sessions-outside-raw-cleanup-2026-10-22.json'


def git(*args, binary=False):
    out = subprocess.run(['git', '-C', ROOT, *args], capture_output=True, check=True).stdout
    return out if binary else out.decode('utf8')


def sha(b):
    return hashlib.sha256(b).hexdigest()


res = {}
res['full'] = {c: git('rev-parse', c).strip() for c in (HEAD, BASE, LANE_BASE, LANE_HEAD, RUN)}
res['mergeBase'] = git('merge-base', BASE, HEAD).strip()
res['diffHeadVsBaseSha256'] = sha(git('diff', BASE, HEAD, binary=True))
res['diffLaneSha256'] = sha(git('diff', LANE_BASE, LANE_HEAD, binary=True))
res['laneIsAncestorOfHead'] = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', LANE_HEAD, HEAD]).returncode == 0
res['runIsAncestorOfHead'] = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', RUN, HEAD]).returncode == 0
names = [n for n in git('diff', '--name-only', '-z', BASE, HEAD).split('\0') if n]
res['changedPaths'] = names
tracked = [n for n in git('ls-tree', '-r', '-z', '--name-only', HEAD).split('\0') if n]
res['trackedAtHead'] = len(tracked)
tracked_lane = [n for n in git('ls-tree', '-r', '-z', '--name-only', LANE_HEAD).split('\0') if n]
res['trackedAtLaneHead'] = len(tracked_lane)


def production(p):
    if p.startswith(('packages/', 'apps/', 'scripts/')):
        return not (p.endswith('.test.ts') or p.endswith('.testkit.ts'))
    return '/' not in p


res['productionOrRootChanged'] = [p for p in names if production(p)]
# Method 2: per-path blob comparison over every tracked path at HEAD and BASE.
ls = lambda c: dict(
    (line.split('\t', 1)[1], line.split('\t', 1)[0].split()[2])
    for line in git('ls-tree', '-r', '-z', c).split('\0') if line)
h, b = ls(HEAD), ls(BASE)
res['method2Differing'] = sorted(p for p in set(h) | set(b) if h.get(p) != b.get(p))
res['method2Population'] = len(set(h) | set(b))
quiet = subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', BASE, HEAD, '--', '.', f':(exclude){TEST}', f':(exclude){EVID}']).returncode
res['method3DiffQuietExitExcludingTwo'] = quiet
res['testSha256'] = {c: sha(git('show', f'{c}:{TEST}', binary=True)) for c in (BASE, LANE_BASE, RUN, LANE_HEAD, HEAD)}
res['readerSha256'] = {c: sha(git('show', f'{c}:{READER}', binary=True)) for c in (BASE, LANE_BASE, RUN, HEAD)}
res['evidenceSha256AtHead'] = sha(git('show', f'{HEAD}:{EVID}', binary=True))
ev = json.loads(git('show', f'{HEAD}:{EVID}'))
res['evidenceKeys'] = list(ev)
res['evidenceCommitBase'] = [ev['commit'], ev['base']]
res['evidenceEmbeddedHarnessSha256'] = sha(ev['harnessSource'].encode('utf8'))
res['evidenceAddedAt'] = git('log', '--format=%h %s', '--diff-filter=A', HEAD, '--', EVID).strip()
res['testChangedAt'] = git('log', '--format=%h %s', f'{BASE}..{HEAD}', '--', TEST).strip()
print(json.dumps(res, indent=1))
