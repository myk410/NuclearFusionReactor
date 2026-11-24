#!/usr/bin/env python3
"""Non-operational accounting and subjective ranking sensitivity; Python stdlib only."""
from pathlib import Path
import csv
import json
import math
import random
import hashlib

ROOT=Path(__file__).resolve().parents[1]
WEIGHTS=dict(physics=20,net=20,evidence=15,theory=10,engineering=10,barriers=10,scale=5,materials=5,economics=5)

def net(q,eta_d,eta_t,c,a,r=0,m=1):
    if q<=0 or not 0<eta_d<=1 or not 0<=eta_t<=1 or not 0<=c<=1 or not 0<=r<=1 or a<0 or m<1:
        raise ValueError('Unphysical accounting inputs')
    return eta_t*(c*m+r/q)-1/(eta_d*q)-a

def threshold(eta_d,eta_t,c,a,r=0,m=1):
    margin=eta_t*c*m-a
    return (1/eta_d-eta_t*r)/margin if margin>0 else math.inf

def score(c,w):
    if c['physics_gate'].startswith('reject'):
        return 0.0
    return sum(w[k]*c['scores'][k]/10 for k in w)

def ordered(concepts,w):
    return sorted(concepts,key=lambda c:(-score(c,w),c['id']))

def quantile(v,p):
    v=sorted(v);x=p*(len(v)-1);i=int(x);f=x-i
    return v[i]*(1-f)+v[min(i+1,len(v)-1)]*f

def checks(concepts):
    assert sum(WEIGHTS.values())==100
    assert len(concepts)>=30 and len({c['id'] for c in concepts})==len(concepts)
    for c in concepts:
        assert set(c['scores'])==set(WEIGHTS)==set(c['rationale'])
        assert all(0<=v<=10 for v in c['scores'].values())
        assert 0<=score(c,WEIGHTS)<=100
    assert abs(net(10,.5,.4,.95,.08)-.1)<1e-12
    assert abs(threshold(.5,.4,.95,.08)-20/3)<1e-12
    assert abs(threshold(1,.4,1,0)-2.5)<1e-12
    assert threshold(.5,.4,.5,.3)==math.inf
    assert abs(net(10,1,1,1,0,1)-1)<1e-12 # input recovered once, fusion remains sole net source
    assert net(20,.5,.4,.95,.08)>net(10,.5,.4,.95,.08)
    assert abs(net(threshold(.3,.4,.95,.08),.3,.4,.95,.08))<1e-12
    assert abs(.4*(.95*1000)-100/.5-80-1000*net(10,.5,.4,.95,.08))<1e-10
    return 'PASS: accounting identities, bounds, limiting cases, monotonicity, portfolio structure'

def main():
    concepts=json.loads((ROOT/'Research/ConceptData.json').read_text())
    result={'checks':checks(concepts),'seed':20261124,'draws_per_case':20000,
            'model':'Equation E001(1); synthetic independent ranges; no plasma/kinetic simulation',
            'input_sha256':hashlib.sha256((ROOT/'Research/ConceptData.json').read_bytes()).hexdigest()}
    result['threshold_scenarios']=[dict(eta_d=e,eta_t=.4,c=.95,a=.08,r=0,m=1,q_min=threshold(e,.4,.95,.08)) for e in [.5,.15,.01]]
    rng=random.Random(20261124)
    common=[(rng.uniform(5,30),rng.uniform(.3,.5),rng.uniform(.85,.98),rng.uniform(.03,.15),rng.random()) for _ in range(20000)]
    cases={'hypothetical_magnetic':(.3,.7),'hypothetical_efficient_pulsed':(.05,.2),'inefficient_pulsed_stress':(.005,.015)}
    result['monte_carlo']={}
    for name,(lo,hi) in cases.items():
        values=[net(q,lo+(hi-lo)*u,t,c,a) for q,t,c,a,u in common]
        result['monte_carlo'][name]={'eta_driver_range':[lo,hi],'net_over_fusion_q05':quantile(values,.05),'median':quantile(values,.5),'q95':quantile(values,.95),'positive_scenario_fraction':sum(v>0 for v in values)/len(values)}
    # Availability screen at normalized on-net x=.1 and off-load b=.02.
    # d*x-(1-d)*b>0 iff d>b/(x+b), before explicit starts/maintenance.
    result['availability']={'on_net_over_fusion':.1,'off_load_over_fusion':.02,'duty_min':.02/.12}
    # N is a hypothetical illustrative useful fusion count, not an experimental input.
    result['muon_screen']={'N_assumed':150,'E_DT_MeV':17.6,'eta_t_assumed':.4,'max_source_plus_aux_MeV_per_delivered_muon':150*17.6*.4,'source_cost_scenario_MeV':5000,'cycles_required_at_scenario_source_cost':5000/(.4*17.6)}
    plants=[c for c in concepts if c['kind']=='plant']
    base=ordered(plants,WEIGHTS)
    envelopes={c['id']:[] for c in plants}
    rng=random.Random(20261125)
    for _ in range(1000):
        raw={k:v*rng.uniform(.5,1.5) for k,v in WEIGHTS.items()};den=sum(raw.values())
        w={k:v*100/den for k,v in raw.items()}
        for rank,c in enumerate(ordered(plants,w),1):envelopes[c['id']].append(rank)
    profiles={'base':WEIGHTS,
      'evidence_heavy':dict(physics=20,net=15,evidence=30,theory=10,engineering=5,barriers=5,scale=5,materials=5,economics=5),
      'engineering_heavy':dict(physics=15,net=15,evidence=10,theory=5,engineering=25,barriers=10,scale=5,materials=10,economics=5),
      'net_heavy':dict(physics=20,net=35,evidence=10,theory=10,engineering=5,barriers=5,scale=5,materials=5,economics=5)}
    for w in profiles.values():assert sum(w.values())==100
    result['weight_profiles']=profiles
    result['profile_top_five']={name:[c['id'] for c in ordered(plants,w)[:5]] for name,w in profiles.items()}
    result['weight_sensitivity']={k:dict(best=min(v),worst=max(v),top_five_fraction=sum(i<=5 for i in v)/len(v)) for k,v in envelopes.items()}
    out=ROOT/'Simulations';out.mkdir(exist_ok=True)
    (out/'Results.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ROOT/'Rankings/Master.csv').open('w',newline='') as f:
        writer=csv.writer(f,lineterminator="\n");writer.writerow(['overall_rank','id','name','type','score','evidence_confidence','scientific_maturity','primary_obstacle','research_priority','status'])
        for rank,c in enumerate(ordered(concepts,WEIGHTS),1):
            writer.writerow([rank,c['id'],c['name'],c['kind'],round(score(c,WEIGHTS),2),c['confidence'],'preliminary mechanism/component evidence',c['science'],c['potential'],c['status']])
    def table(items):
        return '| Rank | Concept | Score /100 | Evidence confidence | Primary obstacle |\n|---:|---|---:|---|---|\n'+''.join(f"| {i} | [{c['id']} — {c['name']}](../TheoreticalConcepts/{c['id']}.md) | {score(c,WEIGHTS):.1f} | {c['confidence']} | {c['science']} |\n" for i,c in enumerate(items,1))
    md='# Preliminary comparative rankings — 2026-11-24\n\nScores are ordinal expert-style judgments made by this project, not measured probabilities. Differences of a few points are not meaningful evidence of superiority. See [method](Methodology.md), [CSV](Master.csv) and [sensitivity results](../Simulations/Results.json).\n\n## Plant candidates\n\n'+table(base)
    md+='\n## Enabling interventions and scientific testbeds\n\nConditional on a host plant. These are not competing standalone power sources.\n\n'+table(ordered([c for c in concepts if c['kind']!='plant'],WEIGHTS))
    md+='\n## Independent views\n\nThese use stated proxies rather than invented probability estimates. Ties are ordered by ID. Rankings involving enablers are conditional.\n'
    views={
      'Scientific plausibility (physics then theory)':sorted(plants,key=lambda c:(-c['scores']['physics'],-c['scores']['theory'],c['id'])),
      'Net-electric potential (net then total)':sorted(plants,key=lambda c:(-c['scores']['net'],-score(c,WEIGHTS),c['id'])),
      'Experimental support (evidence then total)':sorted(plants,key=lambda c:(-c['scores']['evidence'],-score(c,WEIGHTS),c['id'])),
      'Unconventional approaches (total score, selected family)':ordered([c for c in plants if c['id'] in ['C011','C012','C013','C014','C015','C016','C017','C018']],WEIGHTS),
      'Long-term research potential (subjective potential)':sorted(concepts,key=lambda c:(-c['potential'],-score(c,WEIGHTS),c['id'])),
      'Fewest unresolved barriers (barriers score)':sorted(plants,key=lambda c:(-c['scores']['barriers'],-score(c,WEIGHTS),c['id']))}
    for name,items in views.items():md+='\n### '+name+'\n\n'+', '.join(c['id'] for c in items)+'\n'
    md+='\n### Impact if validated\n\nNo defensible single impact ordering is assigned yet: impact requires scale, resource and cost assumptions absent here. Tier A (potential broad plant benefit): C021, C024, C025, C032; tier B (alternative source or fuel route): C011, C015, C016; tier C (measurement clarification): C030, C031. These conditional tiers are not a success ranking; a quantitative impact ranking is outstanding.\n'
    (ROOT/'Rankings/Master.md').write_text(md)
    summary='# Executed computational findings — 2026-11-24\n\n'+result['checks']+'\n\n## Electrical gain screen\n\n'
    summary+='At eta_t=0.4, capture=0.95, auxiliaries=0.08 P_f, no drive-heat recovery and M=1:\n\n| Assumed driver efficiency | Required Q at breakeven |\n|---:|---:|\n'
    for row in result['threshold_scenarios']:summary+=f"| {row['eta_d']} | {row['q_min']:.4f} |\n"
    summary+='\n## Synthetic uncertainty propagation\n\nThe following are arbitrary scenario boxes, not forecasts or calibrated machine models. x is net on-state electricity divided by fusion power.\n\n| Scenario | x 5th percentile | Median x | x 95th percentile | Positive-box fraction |\n|---|---:|---:|---:|---:|\n'
    for name,r in result['monte_carlo'].items():summary+=f"| {name} | {r['net_over_fusion_q05']:.4f} | {r['median']:.4f} | {r['q95']:.4f} | {r['positive_scenario_fraction']:.4f} |\n"
    summary+='\n## Weight sensitivity\n\nTop-five plant IDs by priority profile:\n\n'+''.join(f"- {name}: {', '.join(ids)}\n" for name,ids in result['profile_top_five'].items())
    summary+='\nAll individual rank envelopes and top-five frequencies are in Results.json. These frequencies reflect chosen weight perturbations, not evidence uncertainty or chance of success.\n\n## Muon accounting screen\n\nFor an assumed 150 D–T fusions per delivered muon and 40% conversion, at most 1056 MeV equivalent electricity is available per muon before auxiliaries. A hypothetical 5000 MeV wall-energy source cost would require 710.23 useful fusions per delivered muon before auxiliaries. These are algebraic scenario calculations, not a source-development simulation or newly measured muon performance.\n\n## Limits\n\nNo MHD, kinetic, radiation transport, materials damage or neutron-transport simulation was run. No evidence-based likelihood or discovery is inferred from these calculations. Independent-input ranges may conceal correlations; next studies must use source-specific coupled constraints.\n'
    (out/'Findings.md').write_text(summary)
    print(result['checks']);print('Plant top ten:',', '.join(c['id'] for c in base[:10]));print('Plant top five:',', '.join(c['id'] for c in base[:5]));print('Outputs: Simulations/Results.json, Simulations/Findings.md, Rankings/Master.md, Rankings/Master.csv')
if __name__=='__main__':main()
