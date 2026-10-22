"""Distinct answers vs distinct labels (verdict + reason, texts and digests dropped) per reader in a differential record."""
import json
import re
import sys

doc = json.load(open(sys.argv[1], encoding='utf-8'))
total_answers = total_labels = 0
for name, answers in doc['answersPerReader'].items():
    labels = {re.sub(r'\s+over \d+$', '', a['label']) for a in answers}
    verdicts = {a['label'].split(':')[0].split(' ')[0] for a in answers}
    total_answers += len(answers)
    total_labels += len(labels)
    print(f'{name:<45} answers {len(answers):>5}  labels {len(labels):>3}  verdict words {sorted(verdicts)[:6]}')
print('sum over readers: distinct answers', total_answers, 'distinct labels', total_labels)
