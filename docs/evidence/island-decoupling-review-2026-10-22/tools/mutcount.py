"""Count each mutant's `old` occurrences in its file. Usage: mutcount.py <tree> <spec.json>"""
import json, pathlib, sys
tree = pathlib.Path(sys.argv[1])
for m in json.loads(pathlib.Path(sys.argv[2]).read_text())['mutants']:
    print(m['id'], (tree / m['file']).read_text(encoding='utf8').count(m['old']))
