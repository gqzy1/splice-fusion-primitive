# Appended ONLY to a temporary schema-stage probe. Never part of deployable source.
# Synthetic fixture; no storage, wallet, LLM or transaction calls.
_probe_candidate = {"name":"Moon Moth Laundromat","description":"A memory-laundering moth folds moonlight into glowing wings, using its antennae to spin lost memories into clean silver thread.","features":["folds moonlight into wings","antennae spin lost memories","silver memory thread"],"bridge":"Moonlight folding powers the moth antennae to weave laundered memories into silver thread."}
_probe_parents = [{"features":["folds moonlight","cleans forgotten memories"]},{"features":["antennae spin silver thread"]}]
_probe_review = {"parent_a_preserved":True,"parent_b_preserved":True,"integrated":True,"safe":True,
"evidence_a":{"feature_index":0,"source_quote":"folds moonlight","field":"description","index":0,"quote":"folds moonlight into glowing wings"},
"evidence_b":{"feature_index":0,"source_quote":"antennae spin silver thread","field":"description","index":0,"quote":"antennae to spin lost memories into clean silver thread"},
"interaction":{"field":"description","index":0,"quote":"folds moonlight into glowing wings, using its antennae to spin lost memories into clean silver thread"}}
_probe_raw=canonical(_probe_candidate)
_probe_snapshot=canonical({"version":VERSION,"parents":_probe_parents})
_probe_checks=0
for _raw in (_probe_raw,' \t\r\n'+_probe_raw+'\n','```json\n'+_probe_raw+'\n```','```\n'+_probe_raw+'\n```'):
    assert parse_candidate(_raw)==_probe_candidate,'V2_VALID_JSON_FAILED'
    _probe_checks+=1
for _raw in ('','null','[]','words '+_probe_raw,_probe_raw+' words',_probe_raw+_probe_raw,_probe_raw[:-1],'{"name":"overridden",'+_probe_raw[1:],'```json\n'+_probe_raw,' '*2401):
    try:
        parse_candidate(_raw)
    except Exception:
        _probe_checks+=1
    else:
        raise Exception('V2_INVALID_JSON_ACCEPTED')
for _raw in ('{"n":NaN}','{"n":Infinity}','{"n":-Infinity}','{"n":1e999}','{"a":{"x":1,"x":2}}'):
    try:
        model_json(_raw,1800)
    except Exception:
        _probe_checks+=1
    else:
        raise Exception('V2_CONSTANT_OR_DUPLICATE_ACCEPTED')
assert review_decision(canonical(_probe_review),_probe_snapshot,_probe_raw)=='ACCEPT','V2_VALID_REFERENCE_FAILED'
_probe_checks+=1
for _section,_key,_value in (('evidence_a','source_quote','antennae spin silver thread'),('evidence_b','source_quote','folds moonlight'),('evidence_a','quote','missing quotation'),('evidence_a','feature_index',True),('evidence_a','index',False),('interaction','field','bridge')):
    _r=json.loads(canonical(_probe_review));_r[_section][_key]=_value
    assert review_decision(canonical(_r),_probe_snapshot,_probe_raw)=='REFERENCE_INVALID','V2_REFERENCE_CHECK_FAILED'
    _probe_checks+=1
for _flag in ('parent_a_preserved','parent_b_preserved','integrated','safe'):
    _r=json.loads(canonical(_probe_review));_r[_flag]=False
    assert review_decision(canonical(_r),_probe_snapshot,_probe_raw)=='VALIDATOR_NEGATIVE','V2_NEGATIVE_ACCEPTED'
    _probe_checks+=1
print('V2_RUNTIME_HELPERS_PASS:'+str(_probe_checks))
