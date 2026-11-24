# Executed computational findings — 2026-11-24

PASS: accounting identities, bounds, limiting cases, monotonicity, portfolio structure

## Electrical gain screen

At eta_t=0.4, capture=0.95, auxiliaries=0.08 P_f, no drive-heat recovery and M=1:

| Assumed driver efficiency | Required Q at breakeven |
|---:|---:|
| 0.5 | 6.6667 |
| 0.15 | 22.2222 |
| 0.01 | 333.3333 |

## Synthetic uncertainty propagation

The following are arbitrary scenario boxes, not forecasts or calibrated machine models. x is net on-state electricity divided by fusion power.

| Scenario | x 5th percentile | Median x | x 95th percentile | Positive-box fraction |
|---|---:|---:|---:|---:|
| hypothetical_magnetic | -0.0947 | 0.1398 | 0.2810 | 0.8691 |
| hypothetical_efficient_pulsed | -1.3611 | -0.2409 | 0.0804 | 0.1522 |
| inefficient_pulsed_stress | -18.3990 | -5.9515 | -2.5900 | 0.0000 |

## Weight sensitivity

Top-five plant IDs by priority profile:

- base: C001, C002, C003, C006, C004
- evidence_heavy: C001, C002, C003, C006, C004
- engineering_heavy: C001, C002, C003, C006, C011
- net_heavy: C001, C002, C003, C006, C004

All individual rank envelopes and top-five frequencies are in Results.json. These frequencies reflect chosen weight perturbations, not evidence uncertainty or chance of success.

## Muon accounting screen

For an assumed 150 D–T fusions per delivered muon and 40% conversion, at most 1056 MeV equivalent electricity is available per muon before auxiliaries. A hypothetical 5000 MeV wall-energy source cost would require 710.23 useful fusions per delivered muon before auxiliaries. These are algebraic scenario calculations, not a source-development simulation or newly measured muon performance.

## Limits

No MHD, kinetic, radiation transport, materials damage or neutron-transport simulation was run. No evidence-based likelihood or discovery is inferred from these calculations. Independent-input ranges may conceal correlations; next studies must use source-specific coupled constraints.
