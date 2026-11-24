#!/usr/bin/env python3
"""Verify research-document consistency, provenance links and saved calculation inputs."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]

def main():
    concepts=json.loads((ROOT/'Research/ConceptData.json').read_text())
    refs=set(re.findall(r'^## (R\d{3})\b',(ROOT/'References/Bibliography.md').read_text(),re.M))
    assert len(concepts)==33 and len(refs)==30
    types={k:sum(c['kind']==k for c in concepts) for k in ['plant','enabler','testbed']}
    assert types==dict(plant=19,enabler=12,testbed=2)
    errors=[];links=0
    for f in ROOT.rglob('*.md'):
        if '.git' in f.parts:continue
        body=f.read_text()
        for target in re.findall(r'\]\(([^\s)]+)\)',body):
            if target.startswith(('http:','https:','mailto:','#')):continue
            target=target.split('#')[0];links+=1
            if not (f.parent/target).exists():errors.append(f'{f.relative_to(ROOT)}: missing {target}')
        for ref in set(re.findall(r'\bR\d{3}\b',body)):
            if ref not in refs:errors.append(f'{f.relative_to(ROOT)}: unknown {ref}')
    for c in concepts:
        f=ROOT/f"TheoreticalConcepts/{c['id']}.md";body=f.read_text()
        sections=set(map(int,re.findall(r'^## (\d+)\.',body,re.M)))
        assert set(range(1,21))<=sections,(c['id'],sections)
        assert all(r in refs for r in c['refs'])
        for key,value in c['scores'].items():
            assert f'| {key} | {value} |' in body,(c['id'],key)
    result=json.loads((ROOT/'Simulations/Results.json').read_text())
    assert result['input_sha256']==hashlib.sha256((ROOT/'Research/ConceptData.json').read_bytes()).hexdigest()
    assert not errors,'\n'.join(errors)
    print(f'PASS: {len(concepts)} dossiers, 20 required sections each, {len(refs)} reference IDs, {links} local links, score and input-hash consistency; types={types}')
    print('This verifies document/model consistency, not scientific validity or bibliography completeness.')
if __name__=='__main__':main()
