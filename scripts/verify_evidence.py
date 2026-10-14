from pathlib import Path
import hashlib, json
root=Path(__file__).resolve().parents[1]
e=json.loads((root/'evidence/SPLICE_V2_EVIDENCE.json').read_text())
source=root/('intelligent-contract/contracts/creative_fusion.py' if (root/'intelligent-contract').exists() else 'contracts/creative_fusion.py')
assert hashlib.sha256(source.read_bytes()).hexdigest()==e['sourceSHA256']=='4a92361b30f2b504ec02e699a816bab78cac47504dafafa9a2ca158c947f07b1'
assert source.read_bytes().hex() in json.dumps(e['steps']['T01'])
assert e['network']['chainId']==61999 and e['deployment']=='0x834f53cf56AE590F63cee321eE1A8CE566F3E9c4'
for step in e['steps'].values():
 assert step['status']=='VERIFIED' and step['decoded']['statusName']=='FINALIZED'
 assert step['decoded']['result']==6 and step['decoded']['consensus_data']['leader_receipt'][0]['execution_result']=='SUCCESS'
 assert step['actualFee']['networkFee']=='0'
f=e['steps']['T04']['reads']; w=f['work']; parents=f['parents']
canonical=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True)
digest=lambda x:hashlib.sha256(canonical(x).encode()).hexdigest()
assert w['id']==3 and w['version']=='SPLICE-V2' and w['parents']==[1,2]
assert len(set(p['creator'].lower() for p in parents))==2
assert w['parent_creators']==[p['creator'] for p in parents]
assert w['parent_hashes']==[digest(p) for p in parents]
assert w['input_hash']==digest({'version':'SPLICE-V2','parents':parents})
assert w['request_fingerprint']==digest({'snapshot':canonical({'version':'SPLICE-V2','parents':parents})})
assert f['lineage']=={'parents':parents,'work':w}
assert e['steps']['T04']['decoded']['last_round']['validator_votes_name'].count('AGREE')==3
assert e['status']=='REAL ONCHAIN FUSION VERIFIED'
assert e['semantic']['mode']=='HUMAN_CONFIRMED_VISIBLE_COMPARISON'
if (root/'src/verified-evidence.json').exists():
 snapshot=json.loads((root/'src/verified-evidence.json').read_text())
 assert snapshot['works']==f['list'] and snapshot['lineage']==f['lineage']
print('EVIDENCE_INTEGRITY_PASS: four finalized successful receipts, deployed source bytes, two contributors, parent/input fingerprints, separate human review')
