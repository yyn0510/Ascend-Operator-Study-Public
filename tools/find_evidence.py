"""Search the publication member index without extracting archives."""
from pathlib import Path
import argparse, json, gzip

p=argparse.ArgumentParser()
p.add_argument('--query', required=True)
p.add_argument('--limit', type=int, default=30)
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
n=0
with gzip.open(root/'metadata/member_manifest.jsonl.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        row=json.loads(line)
        if a.query.casefold() in (row['source']+' '+row['published']).casefold():
            n+=1
            if n<=a.limit:print(row['published'])
print(f'{n} matches; displayed at most {a.limit}.')
