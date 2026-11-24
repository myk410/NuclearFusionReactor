# Project hypotheses — falsifiable proposals, novelty unestablished

These are original formulations within this project, not claims that no prior researcher considered them. Prior-art searches and experimental collaboration remain necessary.

## H001 — density/screening separation changes the value of electrochemical enhancement
A single yield ratio is insufficient to attribute enhancement to electron screening. Under Y_i=A_i n exp(k_i u), with dimensionless screening parameter u and log-density theta, the Poisson Fisher matrix has entries sum N_i, sum N_i k_i and sum N_i k_i². A single observation, or multiple observations with identical sensitivity k, produces zero determinant. For two independent sensitivities the determinant is N1 N2(k1-k2)². The code verifies these identities for synthetic inputs.

Prediction: an apparent screening estimate will be unstable to independently measured density/stopping constraints if it is actually a density surrogate. Falsification: a density-only model fails held-out measurements while a jointly constrained screening model predicts them with calibrated uncertainty. This does not guarantee large screening or useful net energy. Next: retrieve R002 raw data; construct nuisance-aware likelihood with stopping, background and temporal drift. No such fit was performed here.

## H002 — favorable subsystem improvements can reverse sign after coupled penalties
A higher conversion temperature may increase electrical parasitics or reduce material life. In a synthetic E001 example, eta_t increases from .40 to .42 while a rises from .08 to .11; Q=10, eta_d=.5 and c=.95 remain fixed. Calculated x changes from .100 to .119 if the auxiliary penalty is ignored, but falls to .089 when included. The intervention would be falsely promoted by a subsystem-only evaluation.

Prediction: ranking interventions by isolated efficiency can differ from ranking by constrained cycle-average electricity. Falsification: a calibrated coupled model finds penalties too small to change the decision across defensible uncertainty ranges. Useful research output: architecture-specific Pareto sets for temperature, lifetime, pumping and breeding. C032 implements the research direction; no new reactor physics is implied.

## H003 — loss recovery has a ceiling that couples to self-heating
Recovering escaping charged particles can improve electrical balance while leaving or worsening the confinement loss that set Q. Treating Q, recovery fraction and alpha heating as independently favorable variables produces impossible combinations.

Prediction: some high-output model points disappear after imposing one alpha-energy partition, species energy balances and circuit energy conservation. Falsification: an integrated distribution-and-circuit calculation retains the proposed point with independently verified residuals and all power flows. Compare C011 and C029; R028 motivates residual checks without itself proving this hypothesis.

## H004 — value of information can favor a low-feasibility testbed
A cheap, discriminating negative result on a claimed mechanism may have more scientific value per research effort than another optimistic plant point design. C030/C031 should therefore be ranked by identifiable uncertainty reduced, independently of net-electric feasibility.

This is a research-allocation hypothesis, not a fusion law. Test by predefining decisions, expected evidence discrimination and study burden; reject it if it does not change any defensible research decision. No numeric expected-value model or cost claim has been validated here.
