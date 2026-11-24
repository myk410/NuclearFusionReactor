# Skeptical audit — single-analysis review, not independent peer review

## Project-wide vulnerabilities
1. Initial literature access is often abstract-level and institution-authored; neither peer review nor an official announcement independently validates this project's extrapolation.
2. Scores are subjective and correlated: physics, theory and evidence may partially count related strengths. Weight sensitivity does not cure that. Economics and materials scores have particularly weak quantitative foundations.
3. The initial portfolio omitted the indirect-drive baseline. Corrected by C033 with an explicit ranking history. This illustrates why no final conclusion should precede a coverage audit.
4. Uniform Monte Carlo boxes are not empirical posteriors and have no demonstrated feasible joint region. Their positive fractions must never be called technological probabilities.
5. Mechanism compatibility does not prove adequate rates. Every concept with a high physics score may still have extremely poor energy potential.
6. Closely related architectures share failures. A long list is not a portfolio of independent successes.
7. No full irradiation, neutronics, turbulent transport or cost model is implemented. The executed studies validate accounting and inference logic only.
8. Some rank criteria lack a defensible impact ordering; conditional impact tiers are explicitly incomplete.

## Mandatory attempted falsification by concept
Every dossier section 14 gives its own failure criterion. The leading-ten reviews apply additional source-specific criticism. Proposals should be stopped or reclassified when their own criterion fails; interestingness and prior project effort are not reasons to retain a favorable score.

## Specific traps tested
- Energy recovery cannot create extra energy: ideal recovery test in analyze.py returns only fusion input as net when external heat is perfectly recycled.
- Better conversion can worsen net electricity: executed coupled-tradeoff example falls from x=.100 to .089 after a .03 auxiliary penalty.
- A yield increase cannot identify screening uniquely: executed Fisher example is singular with one sensitivity.
- Solver convergence cannot replace equation residuals: R028 is a concrete published correction; future nonlinear models require independent power/species residuals and physical admissibility.
- Heating cannot substitute for confinement: R030 motivates a counter-test of compressed FRCs.

## Needed outside scrutiny
An actual independent expert review, blinded scoring elicitation and reproduction of published model points are not yet done. Do not describe this document as expert consensus or independent validation.
