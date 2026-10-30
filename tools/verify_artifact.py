"""Verify public bytes and declared cohort counts. No network or NPU use."""
from pathlib import Path
import csv, hashlib, json, zipfile, collections, gzip, re

root=Path(__file__).resolve().parents[1]
errors=[]
def digest(b):return hashlib.sha256(b).hexdigest()
def check(condition,message):
    if not condition:errors.append(message)

release=json.loads((root/'metadata/release_files.json').read_text('utf-8'))
for row in release:
    f=root/row['file']
    check(f.is_file(),f"Missing: {row['file']}")
    if f.is_file():check(digest(f.read_bytes())==row['sha256'],f"Hash mismatch: {row['file']}")

members=collections.defaultdict(list)
with gzip.open(root/'metadata/member_manifest.jsonl.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        row=json.loads(line)
        if '::' in row['published']:
            archive,name=row['published'].split('::',1);members[archive].append((name,row))
        else:
            file=root/row['published']
            check(file.is_file(),f"Missing member: {row['published']}")
            if file.is_file():check(digest(file.read_bytes())==row['sha256'],f"Member mismatch: {row['published']}")
count=0
archived_rounds=set()
for archive,entries in members.items():
    with zipfile.ZipFile(root/archive) as z:
        check(len(z.namelist())==len(set(z.namelist())),f'Duplicate archive paths: {archive}')
        for name,row in entries:
            if archive.startswith('01_v3/evidence/'):
                m=re.match(r'([^/]+)/.*?/level1_([^/]+)/(trajectory_\d+)/round_(\d+)(?:/|$)',name)
                if m:archived_rounds.add((m[1],m[2],m[3],int(m[4])))
            try:b=z.read(name)
            except KeyError:errors.append(f'Missing {archive}::{name}');continue
            check(len(b)==row['bytes'] and digest(b)==row['sha256'],f'Member mismatch: {archive}::{name}')
            count+=1

with (root/'01_v3/tables/v3_rounds.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
check(len(rows)==1080,'V3 round count differs from 1080')
check(len({r['model'] for r in rows})==9,'V3 model count differs from 9')
check(len({(r['model'],r['operator'],r['trajectory']) for r in rows})==216,'V3 trajectory count differs from 216')
check(not any('opus' in r['model'].lower() for r in rows),'Opus entered formal cohort')
round_ids=[(r['model'],r['operator'],r['trajectory'],r['round']) for r in rows]
check(len(set(round_ids))==1080,'Duplicate V3 round keys')
expected_rounds={(r['experiment_dir'],r['operator'],r['trajectory'],int(r['round'])) for r in rows}
check(archived_rounds==expected_rounds,'Archived round keys differ from the 1080 formal CSV keys')
root_tables=root/'02_model_transfer/tables'
formal=0;all_rows=0
for dataset,n in [('AI2D',22),('MMStar',10),('DocVQA',10),('COCO',23)]:
    a=json.loads((root_tables/f'{dataset}_任务与条件对照.json').read_text('utf-8-sig'))
    actual=sum(r['记录类型']=='正式任务' for r in a)
    check(actual==n,f'{dataset}: expected {n} formal comparisons, got {actual}')
    formal+=actual;all_rows+=len(a)
check(formal==65 and all_rows==79,'Transfer task totals differ from 65/79')
t=json.loads((root_tables/'模型完整路径计时.json').read_text('utf-8-sig'))
check(len(t['条件汇总'])==101,'Timing condition count differs from 101')
check(len(t['独立时段'])==303,'Timing session count differs from 303')
s=json.loads((root_tables/'真实输入扫描.json').read_text('utf-8-sig'))
check(len(s['实际回放'])==600,'Input scan count differs from 600')
check(len(s['超出接口范围'])==4,'Out-of-contract condition count differs from 4')
f=json.loads((root_tables/'ForeachNorm准入与故障定位.json').read_text('utf-8-sig'))
c=f['九候选分阶段状态']['counts']
check((c['fixed_sources_attempted'],c['benchmark_full_correct'],c['real_input_gate_passed'])==(9,8,7),'ForeachNorm gate counts differ from 9/8/7')
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(release)} release files; {count} archived members; V3 9/216/1080; transfer 65 formal comparisons.')
print('This verifies artifact integrity and summary counts, not a new execution of the experiments.')
