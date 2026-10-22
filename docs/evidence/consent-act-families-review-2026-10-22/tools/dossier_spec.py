"""Re-run spec for the record's mutants whose recorded command names another project than the record's top-level one: the
runner's output carries no per-mutant `project`, so replaying the record as a spec runs them under the wrong project.
argv[1] = the PR's mutants record, argv[2] = output spec. The project is taken from each mutant's recorded `command`."""
import json
import re
import sys

rec = json.load(open(sys.argv[1], encoding='utf-8'))
out = []
for m in rec['mutants']:
    project = re.search(r'--project (\S+)', m['command']).group(1)
    if project != rec['project']:
        out.append({'id': m['id'], 'file': m['file'], 'old': m['old'], 'new': m['new'], 'tests': m['tests'], 'project': project})
json.dump({'project': rec['project'], 'mutants': out}, open(sys.argv[2], 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(out), 'mutants with another project:', ', '.join(f"{m['id']} ({m['project']})" for m in out))
