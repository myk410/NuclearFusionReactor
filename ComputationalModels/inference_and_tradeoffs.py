#!/usr/bin/env python3
"""Analytical statistical identifiability and illustrative coupled-loss stress tests."""
from pathlib import Path
import json
import math
from analyze import net,threshold,WEIGHTS,ordered
ROOT=Path(__file__).resolve().parents[1]

def fisher(counts,slopes):
    # theta=(log density, dimensionless screening parameter).
    return [[sum(counts),sum(n*k for n,k in zip(counts,slopes))],
            [sum(n*k for n,k in zip(counts,slopes)),sum(n*k*k for n,k in zip(counts,slopes))]]

def det(m):return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def main():
    single=fisher([1000],[2]);same=fisher([1000,1000],[2,2]);distinct=fisher([1000,1000],[1,2])
    assert det(single)==det(same)==0
    assert det(distinct)==1000*1000*(1-2)**2
    frac=.15;z=1.959963984540054;z_power=.8416212335729143
    # Approximate two independent equal-duration Poisson-rate measurements.
    significance_baseline=(z*z*(2+frac))/(frac*frac)
    power_baseline=((z+z_power)**2*(2+frac))/(frac*frac)
    # Arbitrary tradeoff example: baseline Q=10, eta_d=.5, eta_t=.4, c=.95, a=.08.
    # A proposed change adds .02 gross-conversion efficiency and .03 auxiliary load.
    base=net(10,.5,.4,.95,.08)
    isolated=net(10,.5,.42,.95,.08)
    coupled=net(10,.5,.42,.95,.11)
    assert isolated>base>coupled
    # Score sensitivity to changing one criterion by one point at a time.
    data=json.loads((ROOT/'Research/ConceptData.json').read_text())
    plants=[c for c in data if c['kind']=='plant']
    env={c['id']:[] for c in plants}
    for c in plants:
        for k in WEIGHTS:
            for delta in [-1,1]:
                changed=[dict(x,scores=dict(x['scores'])) for x in plants]
                target=next(x for x in changed if x['id']==c['id'])
                target['scores'][k]=max(0,min(10,target['scores'][k]+delta))
                for rank,x in enumerate(ordered(changed,WEIGHTS),1):env[x['id']].append(rank)
    result={'status':'Executed analytic/synthetic studies; not fitted to Thunderbird or a plant',
       'fisher_examples':{'one_measurement_det':det(single),'equal_slope_det':det(same),'distinct_slope_det':det(distinct)},
       'counting_approximation':{'rate_ratio':1+frac,'baseline_counts_for_z_1_96':significance_baseline,'baseline_counts_with_approx_80pct_power':power_baseline,'limitations':'Independent Poisson counts, equal duration, no background or drift. Not a replication protocol or analysis of published uncertainty.'},
       'coupled_tradeoff':{'baseline_x':base,'conversion_only_x':isolated,'conversion_plus_auxiliary_penalty_x':coupled},
       'one_score_at_a_time_rank_envelopes':{k:{'best':min(v),'worst':max(v)} for k,v in env.items()}}
    (ROOT/'Simulations/InferenceAndTradeoffs.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: singular one-observable inference, independent-slope determinant, coupled-loss sign reversal')
    print('Coupled tradeoff:',result['coupled_tradeoff'])
if __name__=='__main__':main()
