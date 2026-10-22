"""Write `git show <rev>:<path>` of repo argv[1] to argv[3]."""
import subprocess
import sys

repo, spec, out = sys.argv[1], sys.argv[2], sys.argv[3]
data = subprocess.run(['git', '-C', repo, 'show', spec], check=True, capture_output=True).stdout
open(out, 'wb').write(data)
print(len(data), 'bytes')
