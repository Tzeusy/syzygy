"""Find owner-notice and bead-8.1 mentions in a bd show --json dump (description, notes, comments, design, acceptance). Usage: notice.py <file>"""
import json, re, sys
text = open(sys.argv[1]).read()
data = json.loads(text[text.index('['):])
bead = data[0]
fields = {k: v for k, v in bead.items() if isinstance(v, str)}
for c in bead.get('comments') or []:
    fields[f"comment {c.get('id')} {c.get('created_at')}"] = c.get('text', '')
pat = re.compile(r'owner notice|notice|8\.1(?![0-9])|bpyt\.8\.1(?![0-9])', re.I)
print('fields', list(fields)[:30], 'comments', len(bead.get('comments') or []))
for k, v in fields.items():
    for m in pat.finditer(v):
        print(f'[{k}] ...{v[max(0, m.start() - 160):m.end() + 160]}...'.replace('\n', ' '))
